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
import os
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
AGE_GATE_COOKIE_NAMES = [
    "age_verified", "ageVerified", "age_gate", "ageGate", "is_age_verified",
    "over21", "isOver21", "age_gate_passed", "tymber-age-gate", "dutchie_age",
    "jane_age_verified", "wm_age_gate", "leafly_age_gate", "_age_verified",
]

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
    gate_found: bool = False      # a 21+ gate was detected and clicked
    reloaded: bool = False        # the page was reloaded after clearing it
    status: int | None = None     # HTTP status of the main document
    blocked_hint: str | None = None

    @property
    def ok(self) -> bool:
        return self.error is None and (bool(self.payloads) or bool(self.html))


# Signatures of a bot check or a hard block, which look exactly like an empty
# page from the outside but need a completely different remedy.
BLOCK_SIGNATURES: list[tuple[str, str]] = [
    ("just a moment", "Cloudflare challenge"),
    ("checking your browser", "Cloudflare challenge"),
    ("cf-browser-verification", "Cloudflare challenge"),
    ("attention required", "Cloudflare block"),
    ("access denied", "access denied"),
    ("403 forbidden", "403 forbidden"),
    ("captcha", "CAPTCHA"),
    ("are you a robot", "bot check"),
    ("enable javascript", "JS-gated shell"),
    ("request blocked", "request blocked"),
    ("unusual traffic", "rate limited"),
]


def _detect_block(html: str, status: int | None) -> str | None:
    """Name the wall, when there is one."""
    if status and status >= 400:
        return f"HTTP {status}"
    low = (html or "")[:20000].lower()
    for needle, label in BLOCK_SIGNATURES:
        if needle in low:
            return label
    if len(html or "") < 1200:
        return "near-empty document"
    return None


async def _fill_birthdate(frame) -> bool:
    """Some gates want a date of birth instead of a yes/no button."""
    filled = False
    try:
        for sel, value in (("input[name*='year' i]", "1990"),
                           ("input[name*='month' i]", "01"),
                           ("input[name*='day' i]", "01"),
                           ("input[type='date']", "1990-01-01"),
                           ("input[placeholder*='YYYY' i]", "1990"),
                           ("input[placeholder*='MM' i]", "01"),
                           ("input[placeholder*='DD' i]", "01")):
            el = frame.locator(sel).first
            if await el.count() and await el.is_visible(timeout=400):
                await el.fill(value, timeout=1500)
                filled = True
    except Exception:
        pass
    return filled


async def _click_gate_in(frame) -> bool:
    """Try every way a 21+ gate exposes its confirm control, in one frame."""
    for pattern in AGE_GATE_PATTERNS:
        for role in ("button", "link"):
            try:
                el = frame.get_by_role(role, name=pattern).first
                if await el.count() and await el.is_visible(timeout=500):
                    await el.click(timeout=2500)
                    return True
            except Exception:
                continue
    # Plain divs and spans with no accessible role.
    for text in ("Yes", "YES", "I'm 21+", "I am 21+", "I am over 21",
                 "Enter", "ENTER", "Continue", "Confirm", "Agree", "21+"):
        try:
            el = frame.get_by_text(text, exact=True).first
            if await el.count() and await el.is_visible(timeout=400):
                await el.click(timeout=2000)
                return True
        except Exception:
            continue
    # Last resort: attribute hints the copy doesn't reveal.
    for sel in ("[id*='age' i] button", "[class*='age' i] button",
                "[data-testid*='age' i]", "button[class*='confirm' i]",
                "[id*='verify' i] button", "[class*='gate' i] button"):
        try:
            el = frame.locator(sel).first
            if await el.count() and await el.is_visible(timeout=400):
                await el.click(timeout=2000)
                return True
        except Exception:
            continue
    return False


async def _dismiss_age_gate(page) -> bool:
    """Clear the 21+ interstitial, wherever it is and whenever it shows up.

    Gates appear on the top page and inside embed iframes, sometimes a second
    or two after load, and some ask for a birthdate rather than yes/no. Missing
    any of those leaves the menu unmounted and the page looks simply empty.
    """
    dismissed = False
    for attempt in range(3):
        frames = [page] + list(page.frames)
        for frame in frames:
            try:
                if await _click_gate_in(frame):
                    dismissed = True
                    await page.wait_for_timeout(1200)
                    break
                if await _fill_birthdate(frame):
                    if await _click_gate_in(frame):
                        dismissed = True
                        await page.wait_for_timeout(1200)
                        break
            except Exception:
                continue
        if dismissed:
            break
        await page.wait_for_timeout(1500)   # a late-rendering gate
    return dismissed


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
            ctype = (response.headers or {}).get("content-type", "").lower()
            if "json" in ctype:
                body = await response.json()
            elif any(x in ctype for x in ("html", "css", "image", "font",
                                          "javascript", "video", "octet-stream")) \
                    and "octet-stream" not in ctype:
                return
            else:
                # Menu APIs mislabel their content-type often enough that
                # trusting the header alone loses real product data. If the URL
                # looks like an API, try to parse it regardless.
                text = await response.text()
                stripped = text.lstrip()[:1]
                if stripped not in ("{", "["):
                    return
                body = json.loads(text)
        except Exception:
            return
        if isinstance(body, (dict, list)):
            cap.payloads.append({"url": response.url, "body": body})

    page.on("response", on_response)

    try:
        response = await page.goto(url, wait_until="domcontentloaded", timeout=45_000)
        if response is not None:
            cap.status = response.status
        await page.wait_for_timeout(1500)
        cap.gate_found = await _dismiss_age_gate(page)
        if cap.gate_found:
            cap.reloaded = True
            # Clicking "yes" does not re-issue the menu request -- the app never
            # mounted, so its fetches never fired. Reload now that the gate flag
            # is set, and capture the requests the second load actually makes.
            cap.payloads.clear()
            await page.goto(url, wait_until="domcontentloaded", timeout=45_000)
            await page.wait_for_timeout(2000)
            await _dismiss_age_gate(page)

        # Menus lazy-load; scrolling is what actually triggers the product fetches.
        for _ in range(scrolls):
            await page.mouse.wheel(0, 4000)
            await page.wait_for_timeout(700)

        await page.wait_for_timeout(settle_ms)
        cap.html = await page.content()
        cap.blocked_hint = _detect_block(cap.html, cap.status)
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
        # Honour a preinstalled Chromium when the environment ships one whose
        # build doesn't match the installed playwright package.
        launch_kwargs: dict = {"headless": headless}
        explicit = os.getenv("VD_CHROMIUM_PATH")
        if explicit and Path(explicit).exists():
            launch_kwargs["executable_path"] = explicit
        browser = await pw.chromium.launch(**launch_kwargs)
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
            "(() => { const v = %s, c = %s;"
            " try { for (const [k, val] of Object.entries(v)) {"
            "   localStorage.setItem(k, val); sessionStorage.setItem(k, val); } } catch (e) {}"
            " try { for (const k of c) {"
            "   document.cookie = k + '=true; path=/; max-age=31536000; SameSite=Lax'; } } catch (e) {}"
            " })();"
            % (json.dumps(AGE_GATE_STORAGE), json.dumps(AGE_GATE_COOKIE_NAMES))
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
