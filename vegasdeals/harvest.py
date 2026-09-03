"""Drive a real browser at a dispensary menu and capture what it loads.

Why a browser and not requests+BeautifulSoup: essentially no Las Vegas
dispensary hand-rolls its menu. They embed Dutchie, I Heart Jane, Weedmaps,
Leafly, Tymber or Sweed, all of which render client-side from a JSON API. The
HTML you'd get from a plain GET is an empty shell.

Why interception and not hardcoded API calls: those JSON APIs are private and
their query shapes change without notice. Rather than pin a GraphQL document
that breaks in a month, we let the page make its own calls and harvest the
responses. When a vendor reshuffles their API the page keeps working, so we
keep working.
"""
from __future__ import annotations

import asyncio
import json
import logging
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

log = logging.getLogger(__name__)

# The "are you 21?" interstitial. It is a cookie gate, not a security control --
# clicking through it once per domain and reusing the stored cookie is all it takes.
AGE_GATE_PATTERNS = [
    re.compile(r"^\s*yes\s*$", re.I),
    re.compile(r"i am (over |at least )?21", re.I),
    re.compile(r"(^|\b)21\s*\+?\s*(or older|and over|\+)?\s*$", re.I),
    re.compile(r"\benter\b", re.I),
    re.compile(r"\bconfirm\b", re.I),
    re.compile(r"\baccept\b", re.I),
    re.compile(r"\bagree\b", re.I),
]

# Pre-seeding these saves a click on most menus and is what the page sets anyway.
AGE_GATE_STORAGE = {
    "age_verified": "true", "ageVerified": "true", "is_age_verified": "true",
    "over21": "true", "isOver21": "true", "age_gate_passed": "true",
    "dutchie-age-gate": "true", "jane-age-verified": "true",
}

JSON_HINT = re.compile(
    r"(graphql|/api/|menu|product|dispensar|store|deal|special|promo|catalog|search)",
    re.I,
)


@dataclass
class Capture:
    """Everything one menu page gave up."""

    dispensary_id: str
    url: str
    payloads: list[dict[str, Any]] = field(default_factory=list)
    html: str = ""
    error: str | None = None

    @property
    def ok(self) -> bool:
        return self.error is None and (bool(self.payloads) or bool(self.html))


async def _dismiss_age_gate(page) -> bool:
    """Click through the 21+ interstitial if one is blocking the menu."""
    for pattern in AGE_GATE_PATTERNS:
        for role in ("button", "link"):
            try:
                el = page.get_by_role(role, name=pattern).first
                if await el.count() and await el.is_visible(timeout=800):
                    await el.click(timeout=2500)
                    await page.wait_for_timeout(1200)
                    return True
            except Exception:
                continue
    # Some gates are plain divs with no accessible role.
    for text in ("Yes", "I'm 21+", "I am 21+", "Enter", "Continue"):
        try:
            el = page.get_by_text(text, exact=True).first
            if await el.count() and await el.is_visible(timeout=500):
                await el.click(timeout=2000)
                await page.wait_for_timeout(1200)
                return True
        except Exception:
            continue
    return False


async def capture_menu(
    context,
    dispensary_id: str,
    url: str,
    *,
    settle_ms: int = 4000,
    scrolls: int = 6,
) -> Capture:
    """Load one menu, clear the age gate, scroll it, and keep every JSON response."""
    cap = Capture(dispensary_id=dispensary_id, url=url)
    page = await context.new_page()

    async def on_response(response):
        try:
            if not JSON_HINT.search(response.url):
                return
            ctype = (response.headers or {}).get("content-type", "")
            if "json" not in ctype.lower():
                return
            body = await response.json()
        except Exception:
            return
        if isinstance(body, (dict, list)):
            cap.payloads.append({"url": response.url, "body": body})

    page.on("response", on_response)

    try:
        await page.goto(url, wait_until="domcontentloaded", timeout=45_000)
        await page.wait_for_timeout(1500)
        await _dismiss_age_gate(page)

        # Menus lazy-load; scrolling is what actually triggers the product fetches.
        for _ in range(scrolls):
            await page.mouse.wheel(0, 4000)
            await page.wait_for_timeout(700)

        await page.wait_for_timeout(settle_ms)
        cap.html = await page.content()
    except Exception as exc:  # a dead menu shouldn't kill the run
        cap.error = f"{type(exc).__name__}: {exc}"
        log.warning("capture failed for %s (%s): %s", dispensary_id, url, cap.error)
    finally:
        await page.close()

    return cap


async def harvest(
    targets: list[tuple[str, str]],
    *,
    headless: bool = True,
    concurrency: int = 3,
    delay_seconds: float = 2.0,
    storage_dir: Path | None = None,
) -> list[Capture]:
    """Capture many menus, politely and in parallel.

    `targets` is [(dispensary_id, menu_url), ...].
    """
    from playwright.async_api import async_playwright

    results: list[Capture] = []
    sem = asyncio.Semaphore(max(1, concurrency))
    state_path = None
    if storage_dir:
        storage_dir.mkdir(parents=True, exist_ok=True)
        candidate = storage_dir / "state.json"
        state_path = candidate if candidate.exists() else None

    async with async_playwright() as pw:
        browser = await pw.chromium.launch(headless=headless)
        context = await browser.new_context(
            storage_state=str(state_path) if state_path else None,
            user_agent=(
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
            ),
            viewport={"width": 1400, "height": 1000},
            locale="en-US",
            timezone_id="America/Los_Angeles",
        )
        # Pre-answer the age gate so most pages never show it.
        await context.add_init_script(
            "(() => { const v = %s;"
            " try { for (const [k, val] of Object.entries(v)) {"
            "   localStorage.setItem(k, val); sessionStorage.setItem(k, val); } } catch (e) {} })();"
            % json.dumps(AGE_GATE_STORAGE)
        )

        async def run_one(did: str, url: str) -> Capture:
            async with sem:
                cap = await capture_menu(context, did, url)
                await asyncio.sleep(delay_seconds)
                return cap

        results = list(
            await asyncio.gather(*(run_one(d, u) for d, u in targets))
        )

        if storage_dir:
            try:
                await context.storage_state(path=str(storage_dir / "state.json"))
            except Exception:
                pass
        await context.close()
        await browser.close()

    return results
