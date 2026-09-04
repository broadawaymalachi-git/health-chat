"""Plain-English questions -> structured filters -> a written answer.

Two Claude calls per question. The first turns "cheapest indica eighth near me
tonight" into a filter dict; the second writes the answer from the rows the
database actually returned. Keeping retrieval in SQL rather than asking the
model to sift the menu is what stops it inventing a deal that isn't there.
"""
from __future__ import annotations

import json
import logging
from typing import Any, Literal

from pydantic import BaseModel, Field

log = logging.getLogger(__name__)

CATEGORIES = ["flower", "preroll", "vape", "concentrate", "edible",
              "tincture", "topical", "unknown"]


class DealQuery(BaseModel):
    """Structured form of whatever the user asked."""

    categories: list[str] = Field(
        default_factory=lambda: ["vape"],
        description=f"Product categories to include. Choose from {CATEGORIES}. "
                    "Defaults to ['vape'] -- disposable vapes are the "
                    "product this is for. Only widen it if the user names "
                    "something else.",
    )
    text: str | None = Field(
        None, description="Free-text match on product or brand name, e.g. a strain "
                          "like 'blue dream'. Null if the user named no specific item.",
    )
    brand: str | None = Field(None, description="Brand name, if one was named.")
    dispensary: str | None = Field(
        None, description="Dispensary name, if the user asked about one store.")
    max_price: float | None = Field(
        None, description="Maximum out-the-door price in dollars, taxes included.")
    size_grams: float | None = Field(
        None, description="Target weight in grams. An eighth is 3.5, a quarter 7, "
                          "a half ounce 14, an ounce 28.",
    )
    min_thc_percent: float | None = Field(None, description="Minimum THC percentage.")
    max_drive_minutes: float | None = Field(
        None, description="Max drive time in minutes, only if the user asked to be "
                          "closer than the configured default.",
    )
    only_discounted: bool = Field(
        False, description="True only if the user explicitly wants marked-down items "
                           "rather than the best value overall.",
    )
    sort: Literal["score", "unit_price", "price", "percent_off", "drive"] = Field(
        "score",
        description="'score' is best overall value and is almost always right. "
                    "'unit_price' for cheapest per gram, 'price' for lowest sticker, "
                    "'percent_off' for deepest markdown, 'drive' for nearest.",
    )
    limit: int = Field(15, ge=1, le=50)


EXTRACT_SYSTEM = """You convert questions about cannabis dispensary menus into \
search filters.

Rules:
- Only set a field the user actually implied. Leave the rest null/empty.
- "deal", "best deal", "what's good" means best value: sort='score', \
only_discounted=False. Real value beats a big banner, so do not force \
only_discounted unless they explicitly ask for sales or markdowns.
- "cheapest" means sort='unit_price' when a weight or category is implied, \
otherwise sort='price'.
- Slang: eighth=3.5g, quarter=7g, half/half-oz=14g, oz/ounce/zip=28g, \
cart/pen=vape, dabs/wax/shatter/rosin=concentrate, gummies/chocolate=edible, \
j/joint/pre-roll=preroll.
- Indica/sativa/hybrid are not categories; put them in `text`."""

ANSWER_SYSTEM = """You help someone pick what to buy at a Las Vegas dispensary.

You are given the ranked results of their query as JSON. Ground every claim in \
those rows and never invent a product, price or store.

- Lead with the single best pick and say plainly why it wins.
- Prices shown are out-the-door (Clark County taxes included) -- say so once.
- Quote unit price ($/g, $/100mg THC) when comparing unlike sizes.
- Mention drive time when it matters.
- If the rows are thin or nothing matches, say so directly rather than padding.
- Remind them menus move fast and to confirm stock before driving, but only once \
and briefly.

Be concise and specific. A short intro, then the picks. No preamble."""


# Keyword fallbacks so the app still answers usefully with no API key set.
_CATEGORY_HINTS = {
    "flower": ("flower", "bud", "eighth", "ounce", "oz", "quarter", "zip", "gram of"),
    "preroll": ("preroll", "pre-roll", "pre roll", "joint", "j ", "blunt"),
    "vape": ("cart", "cartridge", "vape", "pen", "disposable"),
    "concentrate": ("concentrate", "dab", "wax", "shatter", "rosin", "resin",
                    "badder", "budder", "diamond", "hash"),
    "edible": ("edible", "gummy", "gummies", "chocolate", "brownie", "cookie", "drink"),
    "tincture": ("tincture",),
    "topical": ("topical", "balm", "salve", "lotion", "patch"),
}
_SIZE_HINTS = (
    ("eighth", 3.5), ("1/8", 3.5), ("quarter", 7.0), ("1/4", 7.0),
    ("half ounce", 14.0), ("half oz", 14.0), ("1/2 oz", 14.0),
    ("ounce", 28.0), (" oz", 28.0), ("zip", 28.0),
)


def _heuristic_filters(question: str) -> DealQuery:
    """A keyword read of the question -- crude, but far better than a literal
    LIKE on the whole sentence, which matches nothing."""
    low = f" {question.lower()} "
    categories = [
        cat for cat, hints in _CATEGORY_HINTS.items() if any(h in low for h in hints)
    ]
    size = next((g for word, g in _SIZE_HINTS if word in low), None)

    sort = "score"
    if "cheapest" in low or "lowest price" in low:
        sort = "unit_price" if (size or categories) else "price"
    elif "closest" in low or "nearest" in low:
        sort = "drive"
    elif "biggest discount" in low or "deepest" in low or "most off" in low:
        sort = "percent_off"

    return DealQuery(
        categories=categories,
        size_grams=size,
        sort=sort,
        only_discounted=any(w in low for w in ("on sale", "% off", "marked down",
                                               "discounted", "clearance")),
    )


def _client(api_key: str | None):
    import anthropic
    return anthropic.Anthropic(api_key=api_key) if api_key else anthropic.Anthropic()


def extract_filters(question: str, api_key: str | None, model: str) -> DealQuery:
    """Question -> DealQuery. Falls back to a plain text search if the API fails."""
    try:
        response = _client(api_key).messages.parse(
            model=model,
            max_tokens=2000,
            system=EXTRACT_SYSTEM,
            messages=[{"role": "user", "content": question}],
            output_format=DealQuery,
        )
        query = response.parsed_output
        query.categories = [c for c in query.categories if c in CATEGORIES]
        return query
    except Exception as exc:
        log.warning("filter extraction failed (%s); using keyword fallback", exc)
        return _heuristic_filters(question)


def answer(question: str, rows: list[dict[str, Any]], api_key: str | None,
           model: str, context: str = "") -> str:
    """Write the reply from the rows the database returned."""
    if not rows:
        return ("Nothing in today's data matches that. Either no store within your "
                "radius carries it right now, or the last refresh came back empty "
                "for the stores that do — try `python -m vegasdeals refresh`.")

    trimmed = [{
        "product": r["name"], "brand": r.get("brand"), "store": r["dispensary_name"],
        "category": r.get("category"), "size": r.get("size_text"),
        "out_the_door": r.get("out_the_door"), "was": r.get("base_price"),
        "unit_price": r.get("unit_price"), "unit": r.get("unit_basis"),
        "percent_off": r.get("percent_off"), "thc_percent": r.get("thc_percent"),
        "drive_minutes": r.get("drive_minutes"), "why_ranked": r.get("score_reasons"),
        "cheaper_than_pct_of_peers": r.get("market_percentile"),
    } for r in rows[:25]]

    payload = json.dumps({"question": question, "context": context,
                          "results": trimmed}, default=str)
    try:
        response = _client(api_key).messages.create(
            model=model,
            max_tokens=2000,
            system=ANSWER_SYSTEM,
            messages=[{"role": "user", "content": payload}],
            thinking={"type": "adaptive"},
            output_config={"effort": "low"},
        )
        text = "\n".join(b.text for b in response.content if b.type == "text").strip()
        return text or _plain(rows)
    except Exception as exc:
        log.warning("answer generation failed (%s); returning the plain list", exc)
        return _plain(rows)


def _plain(rows: list[dict[str, Any]]) -> str:
    """Deterministic fallback so the app still works with no API key."""
    from .normalize import UNIT_LABEL

    lines = ["Top picks (prices are out-the-door, Clark County taxes included):", ""]
    for i, r in enumerate(rows[:12], 1):
        bits = [f"{i}. {r['name']}"]
        if r.get("size_text"):
            bits.append(f"({r['size_text']})")
        bits.append(f"— {r['dispensary_name']}")
        bits.append(f"${r['out_the_door']:.2f}")
        if r.get("unit_price"):
            label = UNIT_LABEL.get(r.get("unit_basis") or "per_item", "")
            bits.append(f"[{label} {r['unit_price']:.2f}]")
        if r.get("percent_off"):
            bits.append(f"({r['percent_off']:.0f}% off)")
        if r.get("drive_minutes") is not None:
            bits.append(f"· {r['drive_minutes']:.0f} min")
        lines.append(" ".join(bits))
        if r.get("score_reasons"):
            lines.append(f"     {r['score_reasons']}")
    lines += ["", "Menus change fast — confirm stock before you drive."]
    return "\n".join(lines)
