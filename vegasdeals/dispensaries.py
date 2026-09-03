"""The store list, and how it gets filled in.

The seed deliberately carries only names and public websites. Addresses, menu
platforms and menu URLs are *resolved at run time* from each store's own site
rather than baked in here, for two reasons: dispensaries move, rebrand and
switch menu vendors constantly, and a hardcoded address that is quietly wrong
is worse than no address at all -- it silently drops a store from your radius.

Run `python -m vegasdeals resolve` once to populate them, and again whenever a
store starts coming back empty.
"""
from __future__ import annotations

import json
import logging
import re
from dataclasses import asdict, dataclass, field
from pathlib import Path

log = logging.getLogger(__name__)

# Which menu platform a site embeds, detected from its HTML.
PLATFORM_SIGNATURES: list[tuple[str, re.Pattern]] = [
    ("dutchie", re.compile(r"dutchie\.com|dutchie-embed|embedded-menu", re.I)),
    ("jane", re.compile(r"iheartjane\.com|jane-frame|api\.iheartjane", re.I)),
    ("weedmaps", re.compile(r"weedmaps\.com|wm-embed|api-g\.weedmaps", re.I)),
    ("leafly", re.compile(r"leafly\.com/(dispensary|embed)", re.I)),
    ("tymber", re.compile(r"tymber\.io|getTymber", re.I)),
    ("sweed", re.compile(r"sweed\.menu|sweedpos", re.I)),
    ("dispense", re.compile(r"dispenseapp\.com", re.I)),
    ("treez", re.compile(r"treez\.io|swifthq", re.I)),
]

IFRAME_RE = re.compile(r"<iframe[^>]+src=[\"']([^\"']+)[\"']", re.I)
ADDRESS_RE = re.compile(
    r"(\d{3,6}\s+[\w.\- ]{3,40},?\s+(?:North\s+Las\s+Vegas|Las\s+Vegas|Henderson|"
    r"Paradise|Spring\s+Valley|Enterprise)\s*,?\s*NV\s*\d{5})", re.I,
)


@dataclass
class Dispensary:
    id: str
    name: str
    website: str
    menu_url: str | None = None
    platform: str | None = None
    address: str | None = None
    lat: float | None = None
    lon: float | None = None
    drive_minutes: float | None = None
    enabled: bool = True
    notes: str = ""

    @property
    def scrape_url(self) -> str:
        return self.menu_url or self.website


def detect_platform(html: str) -> str | None:
    for name, pattern in PLATFORM_SIGNATURES:
        if pattern.search(html):
            return name
    return None


def find_menu_url(html: str, base_url: str) -> str | None:
    """Prefer an embedded menu iframe; fall back to a likely on-site menu path."""
    for src in IFRAME_RE.findall(html):
        if any(p.search(src) for _, p in PLATFORM_SIGNATURES):
            if src.startswith("//"):
                return "https:" + src
            if src.startswith("http"):
                return src
    for path in ("/menu", "/shop", "/order", "/specials", "/deals", "/products"):
        if re.search(rf'href=["\'][^"\']*{path}\b', html, re.I):
            return base_url.rstrip("/") + path
    return None


def extract_address(html: str) -> str | None:
    """Street address from schema.org markup if present, else a text match."""
    for block in re.findall(
        r'<script[^>]+application/ld\+json[^>]*>(.*?)</script>', html, re.S | re.I
    ):
        try:
            data = json.loads(block.strip())
        except Exception:
            continue
        for node in (data if isinstance(data, list) else [data]):
            if not isinstance(node, dict):
                continue
            addr = node.get("address")
            if isinstance(addr, dict):
                parts = [
                    addr.get("streetAddress"), addr.get("addressLocality"),
                    addr.get("addressRegion"), addr.get("postalCode"),
                ]
                joined = ", ".join(str(p) for p in parts if p)
                if joined.strip(", "):
                    return joined
    m = ADDRESS_RE.search(re.sub(r"<[^>]+>", " ", html))
    return m.group(1).strip() if m else None


def load(path: Path) -> list[Dispensary]:
    if not path.exists():
        return []
    raw = json.loads(path.read_text())
    return [Dispensary(**d) for d in raw]


def save(path: Path, stores: list[Dispensary]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps([asdict(s) for s in stores], indent=2) + "\n")
