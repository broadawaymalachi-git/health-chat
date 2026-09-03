"""Turn messy menu rows into comparable numbers.

This is the part that makes the tool better than reading deal pages: a "30% off"
banner is meaningless next to a store whose everyday price is already lower.
Everything here exists to answer "what does a gram actually cost me, out the
door, at this store, today" so unlike things can be ranked against each other.
"""
from __future__ import annotations

import math
import re
import statistics
from dataclasses import dataclass, field

GRAMS_PER_OZ = 28.0

# Ordered longest-first so "half ounce" wins over "ounce".
_WEIGHT_WORDS: list[tuple[str, float]] = [
    ("half ounce", GRAMS_PER_OZ / 2),
    ("half oz", GRAMS_PER_OZ / 2),
    ("quarter pound", GRAMS_PER_OZ * 4),
    ("quarter ounce", GRAMS_PER_OZ / 4),
    ("quarter oz", GRAMS_PER_OZ / 4),
    ("eighth", GRAMS_PER_OZ / 8),
    ("quarter", GRAMS_PER_OZ / 4),
    ("ounce", GRAMS_PER_OZ),
]

_FRACTIONS: dict[str, float] = {
    "1/8": GRAMS_PER_OZ / 8,
    "1/4": GRAMS_PER_OZ / 4,
    "1/2": GRAMS_PER_OZ / 2,
    "3/4": GRAMS_PER_OZ * 3 / 4,
    "1/16": GRAMS_PER_OZ / 16,
}

_GRAM_RE = re.compile(r"(\d+(?:\.\d+)?)\s*(?:g|gr|gram|grams)\b", re.I)
_MG_RE = re.compile(r"(\d+(?:\.\d+)?)\s*mg\b", re.I)
_OZ_NUM_RE = re.compile(r"(?<![/\d.])(\d+(?:\.\d+)?)\s*(?:oz|ounce|ounces)\b", re.I)
_FRACTION_OZ_RE = re.compile(r"(\d+/\d+)\s*(?:oz|ounce|ounces)?\b", re.I)
_PACK_RE = re.compile(r"(\d+)\s*(?:pk|pack|ct|count|pc|pcs|piece[s]?)\b", re.I)
_MULTI_LEAD_RE = re.compile(r"(\d+)\s*[x\u00d7]\s*\d", re.I)   # "2 x 1g"
_MULTI_TRAIL_RE = re.compile(r"[x\u00d7]\s*(\d+)\b", re.I)      # "10mg x 10"
_PERCENT_RE = re.compile(r"(\d+(?:\.\d+)?)\s*%")

def _pack_count(low: str) -> int | None:
    """How many pieces are in the package, from "5pk", "2 x 1g", or "10mg x 10"."""
    for rx in (_PACK_RE, _MULTI_LEAD_RE, _MULTI_TRAIL_RE):
        m = rx.search(low)
        if m:
            return int(m.group(1))
    return None


# Category buckets. Order matters -- first match wins.
_CATEGORY_RULES: list[tuple[str, tuple[str, ...]]] = [
    ("preroll", ("preroll", "pre-roll", "pre roll", "joint", "blunt", "infused roll")),
    ("vape", ("cart", "cartridge", "vape", "disposable", "pod", "aio", "all-in-one")),
    ("concentrate", (
        "concentrate", "wax", "shatter", "rosin", "resin", "badder", "batter",
        "budder", "diamond", "sauce", "sugar", "crumble", "hash", "kief", "dab",
    )),
    ("edible", ("edible", "gumm", "chocolate", "cookie", "brownie", "chew",
                "mint", "lozenge", "beverage", "drink", "seltzer", "syrup", "caramel")),
    ("tincture", ("tincture", "sublingual", "oil drops")),
    ("topical", ("topical", "balm", "salve", "lotion", "cream", "patch", "bath")),
    ("flower", ("flower", "bud", "smalls", "shake", "trim", "popcorn", "eighth", "ounce")),
]

# How each category is priced for comparison.
UNIT_BY_CATEGORY = {
    "flower": "per_gram",
    "concentrate": "per_gram",
    "vape": "per_gram",
    "preroll": "per_gram",
    "edible": "per_100mg_thc",
    "tincture": "per_100mg_thc",
    "topical": "per_item",
    "accessory": "per_item",
    "unknown": "per_item",
}

UNIT_LABEL = {
    "per_gram": "$/g",
    "per_100mg_thc": "$/100mg THC",
    "per_item": "$/item",
}


def categorize(*texts: str | None) -> str:
    """Best-guess product category from any combination of name/category strings."""
    blob = " ".join(t for t in texts if t).lower()
    if not blob:
        return "unknown"
    for label, needles in _CATEGORY_RULES:
        if any(n in blob for n in needles):
            return label
    return "unknown"


def parse_weight_grams(*texts: str | None) -> float | None:
    """Extract a product's weight in grams from its name / size / variant text.

    Handles "3.5g", "1/8 oz", "eighth", "half ounce", "2 x 0.5g", "5pk .5g".
    Returns total grams (pack count multiplied in) or None.
    """
    blob = " ".join(t for t in texts if t)
    if not blob:
        return None
    low = blob.lower()

    grams: float | None = None

    m = _GRAM_RE.search(low)
    if m:
        grams = float(m.group(1))
    if grams is None:
        m = _FRACTION_OZ_RE.search(low)
        if m and m.group(1) in _FRACTIONS:
            grams = _FRACTIONS[m.group(1)]
    if grams is None:
        m = _OZ_NUM_RE.search(low)
        if m:
            grams = float(m.group(1)) * GRAMS_PER_OZ
    if grams is None:
        for word, value in _WEIGHT_WORDS:
            if word in low:
                grams = value
                break

    if grams is None:
        return None

    # "5pk 0.5g" / "2 x 1g" -> multiply, but only when the weight looks per-unit.
    count = _pack_count(low)
    if count and 1 < count <= 100 and grams <= 2.0:
        grams *= count

    return round(grams, 4) if grams > 0 else None


def parse_thc_mg(*texts: str | None) -> float | None:
    """Total THC in milligrams, for edibles/tinctures ("100mg", "10mg x 10")."""
    blob = " ".join(t for t in texts if t)
    if not blob:
        return None
    low = blob.lower()
    m = _MG_RE.search(low)
    if not m:
        return None
    mg = float(m.group(1))
    count = _pack_count(low)
    # A "100mg" package label is already the total; a "10mg" one is per-piece.
    if count and 1 < count <= 200 and mg <= 25:
        mg *= count
    return mg if mg > 0 else None


def parse_thc_percent(*texts: str | None) -> float | None:
    blob = " ".join(t for t in texts if t)
    if not blob:
        return None
    for m in _PERCENT_RE.finditer(blob):
        value = float(m.group(1))
        if 0 < value <= 100:
            return value
    return None


@dataclass
class Offer:
    """One purchasable thing at one store, with everything needed to rank it."""

    dispensary_id: str
    dispensary_name: str
    name: str
    brand: str | None = None
    raw_category: str | None = None
    size_text: str | None = None
    menu_price: float | None = None
    base_price: float | None = None       # pre-discount, when the menu exposes it
    thc_percent: float | None = None
    url: str | None = None
    promo_text: str | None = None
    drive_minutes: float | None = None

    # Derived
    category: str = "unknown"
    grams: float | None = None
    thc_mg: float | None = None
    out_the_door: float | None = None
    unit_basis: str = "per_item"
    unit_price: float | None = None
    percent_off: float | None = None
    absolute_savings: float | None = None
    market_percentile: float | None = None
    score: float = 0.0
    score_reasons: list[str] = field(default_factory=list)

    def enrich(self, tax) -> "Offer":
        self.category = categorize(self.raw_category, self.name)
        self.grams = parse_weight_grams(self.size_text, self.name)
        self.thc_mg = parse_thc_mg(self.size_text, self.name)
        if self.thc_percent is None:
            self.thc_percent = parse_thc_percent(self.name, self.size_text)

        if self.menu_price is not None:
            self.out_the_door = tax.out_the_door(self.menu_price)

        if self.base_price and self.menu_price and self.base_price > self.menu_price:
            self.absolute_savings = round(
                tax.out_the_door(self.base_price) - (self.out_the_door or 0), 2
            )
            self.percent_off = round(
                100 * (self.base_price - self.menu_price) / self.base_price, 1
            )

        self.unit_basis = UNIT_BY_CATEGORY.get(self.category, "per_item")
        self.unit_price = self._unit_price()
        return self

    def _unit_price(self) -> float | None:
        if self.out_the_door is None:
            return None
        if self.unit_basis == "per_gram" and self.grams:
            return round(self.out_the_door / self.grams, 2)
        if self.unit_basis == "per_100mg_thc" and self.thc_mg:
            return round(self.out_the_door / (self.thc_mg / 100.0), 2)
        if self.unit_basis == "per_item":
            return self.out_the_door
        # Right basis, missing denominator: fall back rather than drop the offer.
        self.unit_basis = "per_item"
        return self.out_the_door

    @property
    def size_bucket(self) -> str:
        """Group like with like so an eighth isn't ranked against an ounce."""
        if self.unit_basis == "per_gram" and self.grams:
            for edge, label in ((1.1, "≤1g"), (4.0, "3.5g"), (8.0, "7g"),
                                (15.0, "14g"), (30.0, "28g")):
                if self.grams <= edge:
                    return label
            return ">28g"
        if self.unit_basis == "per_100mg_thc" and self.thc_mg:
            return "≤100mg" if self.thc_mg <= 100 else ">100mg"
        return "item"

    @property
    def peer_key(self) -> tuple[str, str]:
        return (self.category, self.size_bucket)


def score_offers(offers: list[Offer]) -> list[Offer]:
    """Rank offers against *today's actual market*, not against their own banner.

    An offer earns points three ways:
      * market  -- how far below the median unit price for its peer group it is
      * discount-- how deep the advertised markdown is
      * savings -- how many real dollars come off the price

    Market dominates deliberately. A store with no banner at all can top the
    list by simply being cheaper, which is the whole point.
    """
    peers: dict[tuple[str, str], list[float]] = {}
    for o in offers:
        if o.unit_price is not None:
            peers.setdefault(o.peer_key, []).append(o.unit_price)

    medians = {k: statistics.median(v) for k, v in peers.items() if len(v) >= 3}

    for o in offers:
        o.score = 0.0
        o.score_reasons = []

        if o.unit_price is not None and o.peer_key in medians:
            prices = sorted(peers[o.peer_key])
            below = sum(1 for p in prices if p < o.unit_price)
            o.market_percentile = round(100.0 * below / len(prices), 1)
            median = medians[o.peer_key]
            if median > 0:
                delta = (median - o.unit_price) / median
                market_points = max(-20.0, min(60.0, delta * 120))
                o.score += market_points
                if delta > 0.05:
                    o.score_reasons.append(
                        f"{delta * 100:.0f}% under the {o.size_bucket} "
                        f"{o.category} median ({UNIT_LABEL[o.unit_basis]} "
                        f"{o.unit_price:.2f} vs {median:.2f})"
                    )

        if o.percent_off:
            o.score += min(25.0, o.percent_off * 0.5)
            o.score_reasons.append(f"{o.percent_off:.0f}% off")

        if o.absolute_savings:
            o.score += min(15.0, math.log1p(max(o.absolute_savings, 0)) * 4)
            o.score_reasons.append(f"saves ${o.absolute_savings:.2f}")

        # A close store is worth a little, but never enough to outrank real value.
        if o.drive_minutes is not None:
            o.score += max(0.0, (20 - o.drive_minutes) * 0.25)

        o.score = round(o.score, 2)

    offers.sort(key=lambda x: x.score, reverse=True)
    return offers
