"""Pull product offers out of whatever JSON a menu happened to load.

Deliberately shape-agnostic. Dutchie, Jane, Weedmaps and Leafly all describe the
same idea -- a named thing, at a weight, for a price, sometimes marked down --
but each names the fields differently and renames them periodically. Rather than
maintain four brittle schemas, we walk the JSON, recognize anything that looks
like a product, and read it with a broad field vocabulary.

The tradeoff is that we occasionally pick up a non-product; `looks_like_product`
and the sanity bounds in `_price` are what keep that noise out.
"""
from __future__ import annotations

import re
from typing import Any, Iterator

from .normalize import Offer

NAME_KEYS = ("name", "productname", "title", "product_name", "displayname")
BRAND_KEYS = ("brand", "brandname", "brand_name", "producer", "vendor", "cultivator")
CATEGORY_KEYS = ("category", "type", "producttype", "product_type", "kind",
                 "categoryname", "category_name", "root_subtype", "subtype")
# Sale prices are checked before regular ones: when a menu exposes both, the
# sale price is what you pay and the regular price is the "was" we discount from.
SALE_PRICE_KEYS = ("saleprice", "sale_price", "specialprice", "special_price",
                   "discountedprice", "discounted_price", "discounted_price_each",
                   "promoprice", "promo_price", "currentprice", "current_price",
                   "bestprice", "best_price")
REG_PRICE_KEYS = ("price", "priceeach", "price_each", "reccprice", "recprice",
                  "rec_price", "unitprice", "unit_price", "amount", "standardprice")
PRICE_KEYS = SALE_PRICE_KEYS + REG_PRICE_KEYS
BASE_PRICE_KEYS = ("originalprice", "original_price", "baseprice", "base_price",
                   "listprice", "list_price", "wasprice", "was_price", "msrp",
                   "standardprice", "standard_price", "pricebeforediscount",
                   "regularprice", "regular_price", "compareatprice")
SIZE_KEYS = ("weight", "size", "label", "option", "unit", "grams", "weight_label",
             "displayweight", "display_weight", "variant", "packagesize", "net_weight")
THC_KEYS = ("thc", "thcpercent", "thc_percent", "percentthc", "potencythc",
            "thccontent", "thc_content", "thc_potency")
PROMO_KEYS = ("specialdata", "special_data", "specialname", "special_name",
              "promotion", "promo", "specials", "special", "deals", "deal",
              "discount", "offer")
URL_KEYS = ("url", "producturl", "product_url", "link", "href", "permalink", "slug")

# Containers whose entries are per-weight variants of one product.
SALE_ARRAY_KEYS = ("recspecialprices", "specialprices", "saleprices",
                   "discountedprices", "medspecialprices", "medicalspecialprices")

# Jane encodes weight in the key itself: price_eighth_ounce, discounted_price_gram.
JANE_WEIGHTS = {
    "gram": "1g", "two_gram": "2g", "eighth_ounce": "1/8 oz",
    "quarter_ounce": "1/4 oz", "half_ounce": "1/2 oz", "ounce": "1 oz",
    "half_gram": "0.5g", "each": None,
}

VARIANT_KEYS = ("prices", "variants", "options", "pricetiers", "price_tiers",
                "weights", "available_weights", "price_variants", "skus",
                "packages", "priceoptions", "price_options")

_NUM = re.compile(r"-?\d+(?:\.\d+)?")


def _norm(key: str) -> str:
    return re.sub(r"[^a-z0-9]", "", str(key).lower())


def _get(d: dict, keys: tuple[str, ...]) -> Any:
    lookup = {_norm(k): v for k, v in d.items()}
    for k in keys:
        v = lookup.get(_norm(k))
        if v not in (None, "", [], {}):
            return v
    return None


def _text(value: Any) -> str | None:
    """Flatten a field that might be a string, a {name: ...}, or a list of either."""
    if value is None:
        return None
    if isinstance(value, str):
        return value.strip() or None
    if isinstance(value, bool):
        return None          # `special: true` is a flag, not a promo name
    if isinstance(value, (int, float)):
        return str(value)
    if isinstance(value, dict):
        for k in ("name", "title", "label", "displayName", "value", "text"):
            if isinstance(value.get(k), str):
                return value[k].strip() or None
        return None
    if isinstance(value, list):
        parts = [p for p in (_text(v) for v in value) if p]
        return ", ".join(dict.fromkeys(parts)) or None
    return None


def _price(value: Any) -> float | None:
    """Coerce a price field to a float, rejecting values outside menu reality."""
    if value is None or isinstance(value, bool):
        return None
    if isinstance(value, (int, float)):
        price = float(value)
    elif isinstance(value, str):
        m = _NUM.search(value.replace(",", ""))
        if not m:
            return None
        price = float(m.group())
    elif isinstance(value, dict):
        return _price(_get(value, PRICE_KEYS))
    elif isinstance(value, list):
        prices = [p for p in (_price(v) for v in value) if p is not None]
        return min(prices) if prices else None
    else:
        return None
    # Menu prices live between a dollar and a pound of flower. Anything else is
    # an id, a timestamp, a THC reading, or cents -- not a price we can rank.
    return price if 0.5 <= price <= 5000 else None


def _percent(value: Any) -> float | None:
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        v = float(value)
        return v if 0 < v <= 100 else None
    if isinstance(value, str):
        m = _NUM.search(value)
        if m:
            v = float(m.group())
            return v if 0 < v <= 100 else None
    if isinstance(value, dict):
        return _percent(_get(value, THC_KEYS))
    return None


def _resolve_prices(d: dict) -> tuple[float | None, float | None]:
    """(what you pay, what it was) for one product or variant dict."""
    sale = _price(_get(d, SALE_PRICE_KEYS))
    regular = _price(_get(d, REG_PRICE_KEYS))
    explicit_base = _price(_get(d, BASE_PRICE_KEYS))

    for candidate_base in (regular, explicit_base):
        if sale is not None and candidate_base is not None and candidate_base > sale:
            return sale, candidate_base

    price = sale if sale is not None else regular
    if price is not None and explicit_base is not None and explicit_base > price:
        return price, explicit_base
    return price, None


def _jane_weight_offers(node: dict) -> list[tuple[str | None, float, float | None]]:
    """Read Jane's price_<weight> / discounted_price_<weight> key pairs."""
    out = []
    for key, value in node.items():
        k = str(key).lower()
        if not k.startswith("price_"):
            continue
        weight = k[len("price_"):]
        # Only real Jane weight tokens -- "price_variants" is a container, not a price.
        if weight not in JANE_WEIGHTS or isinstance(value, (list, dict)):
            continue
        price = _price(value)
        if price is None:
            continue
        discounted = _price(node.get(f"discounted_price_{weight}"))
        size = JANE_WEIGHTS[weight]
        if discounted is not None and discounted < price:
            out.append((size, discounted, price))
        else:
            out.append((size, price, None))
    return out


def looks_like_product(node: Any) -> bool:
    """A product needs a name and some reachable price."""
    if not isinstance(node, dict) or len(node) < 2:
        return False
    if _text(_get(node, NAME_KEYS)) is None:
        return False
    if _price(_get(node, PRICE_KEYS)) is not None:
        return True
    # Price may only exist inside a variant list, or in Jane's price_<weight> keys.
    variants = _get(node, VARIANT_KEYS)
    if isinstance(variants, list) and any(_price(v) is not None for v in variants):
        return True
    return bool(_jane_weight_offers(node))


def walk(node: Any, depth: int = 0) -> Iterator[dict]:
    """Yield every product-shaped dict in an arbitrary JSON tree."""
    if depth > 14:
        return
    if isinstance(node, dict):
        if looks_like_product(node):
            yield node
            # Don't descend into a product; its children are its own variants.
            return
        for value in node.values():
            yield from walk(value, depth + 1)
    elif isinstance(node, list):
        for item in node:
            yield from walk(item, depth + 1)


def _variant_offers(node: dict) -> list[tuple[str | None, float | None, float | None]]:
    """Expand a product into (size, price, base_price) -- one tuple per weight."""
    jane = _jane_weight_offers(node)
    if jane:
        return list(jane)

    variants = _get(node, VARIANT_KEYS)
    out: list[tuple[str | None, float | None, float | None]] = []

    if isinstance(variants, list):
        for v in variants:
            if isinstance(v, dict):
                price, base = _resolve_prices(v)
                if price is None:
                    price = _price(v)
                if price is None:
                    continue
                out.append((_text(_get(v, SIZE_KEYS)), price, base))
            else:
                # Dutchie-style parallel arrays: Prices[] lines up with Options[].
                price = _price(v)
                if price is not None:
                    out.append((None, price, None))

    # A parallel sale array turns those regular prices into markdowns.
    sale_array = _get(node, SALE_ARRAY_KEYS)
    if out and isinstance(sale_array, list) and len(sale_array) == len(out):
        rebuilt = []
        for (size, regular, base), raw_sale in zip(out, sale_array):
            sale = _price(raw_sale)
            if sale is not None and regular is not None and sale < regular:
                rebuilt.append((size, sale, regular))
            else:
                rebuilt.append((size, regular, base))
        out = rebuilt

    # Pair a bare price array with the matching option/weight labels.
    if out and all(size is None for size, _, _ in out):
        for key in ("options", "weights", "available_weights", "sizes", "optionsbelowthreshold"):
            labels = _get(node, (key,))
            if isinstance(labels, list) and len(labels) == len(out):
                out = [(_text(labels[i]), out[i][1], out[i][2]) for i in range(len(out))]
                break

    if not out:
        price, base = _resolve_prices(node)
        if price is not None:
            out.append((_text(_get(node, SIZE_KEYS)), price, base))
    return out


def offers_from_payloads(
    payloads: list[dict[str, Any]],
    dispensary_id: str,
    dispensary_name: str,
) -> list[Offer]:
    """Every distinct offer found across one store's captured JSON."""
    offers: list[Offer] = []
    seen: set[tuple] = set()

    for payload in payloads:
        for node in walk(payload.get("body")):
            name = _text(_get(node, NAME_KEYS))
            if not name:
                continue
            brand = _text(_get(node, BRAND_KEYS))
            category = _text(_get(node, CATEGORY_KEYS))
            thc = _percent(_get(node, THC_KEYS))
            promo = _text(_get(node, PROMO_KEYS))
            url = _text(_get(node, URL_KEYS))

            for size, price, base in _variant_offers(node):
                if price is None:
                    continue
                # Some menus invert the pair; the cheaper number is always the price.
                if base is not None and base < price:
                    price, base = base, price
                key = (dispensary_id, name.lower(), size, round(price, 2))
                if key in seen:
                    continue
                seen.add(key)
                offers.append(Offer(
                    dispensary_id=dispensary_id,
                    dispensary_name=dispensary_name,
                    name=name,
                    brand=brand,
                    raw_category=category,
                    size_text=size,
                    menu_price=price,
                    base_price=base,
                    thc_percent=thc,
                    promo_text=promo,
                    url=url if (url or "").startswith("http") else None,
                ))
    return offers
