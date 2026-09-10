"""Explain WHY a store produced no offers.

Zero offers has several very different causes and they are indistinguishable
from the outside: the page never loaded, it loaded but fetched no JSON, it
fetched JSON that holds no products, or it fetched products whose fields we
failed to recognize. Only the last one is a parser bug. This separates them.
"""
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path
from typing import Any

from .parsers import (BASE_PRICE_KEYS, NAME_KEYS, PRICE_KEYS, VARIANT_KEYS,
                      _get, _price, _text, looks_like_product, walk)


def _key_paths(node: Any, prefix: str = "", depth: int = 0,
               out: Counter | None = None) -> Counter:
    """Frequency of every key path in a payload, for spotting product shapes."""
    if out is None:
        out = Counter()
    if depth > 6:
        return out
    if isinstance(node, dict):
        for k, v in node.items():
            path = f"{prefix}.{k}" if prefix else str(k)
            out[path] += 1
            _key_paths(v, path, depth + 1, out)
    elif isinstance(node, list):
        for item in node[:5]:
            _key_paths(item, f"{prefix}[]", depth + 1, out)
    return out


def _near_misses(node: Any, depth: int = 0, acc: dict | None = None) -> dict:
    """Dicts that are *almost* products -- the parser's actual blind spots."""
    if acc is None:
        acc = {"name_no_price": [], "price_no_name": []}
    if depth > 12:
        return acc
    if isinstance(node, dict):
        if not looks_like_product(node):
            name = _text(_get(node, NAME_KEYS))
            price = _price(_get(node, PRICE_KEYS)) or _price(_get(node, BASE_PRICE_KEYS))
            keys = sorted(node.keys())[:14]
            if name and not price and len(node) >= 3:
                acc["name_no_price"].append({"name": name[:44], "keys": keys})
            elif price and not name:
                acc["price_no_name"].append({"price": price, "keys": keys})
        for v in node.values():
            _near_misses(v, depth + 1, acc)
    elif isinstance(node, list):
        for item in node[:25]:
            _near_misses(item, depth + 1, acc)
    return acc


def diagnose_store(path: Path) -> dict:
    data = json.loads(path.read_text())
    payloads = data.get("payloads") or []
    report = {
        "store": data.get("store"),
        "page": data.get("page"),
        "error": data.get("error"),
        "payload_count": data.get("payload_count", 0),
        "sampled": len(payloads),
        "status": data.get("status"),
        "gate_found": data.get("gate_found"),
        "reloaded": data.get("reloaded"),
        "blocked_hint": data.get("blocked_hint"),
        "html_len": data.get("html_len"),
    }

    if data.get("error"):
        report["verdict"] = "page failed to load"
        return report
    if not payloads:
        if data.get("blocked_hint"):
            report["verdict"] = f"blocked before the menu loaded ({data['blocked_hint']})"
        elif data.get("gate_found"):
            report["verdict"] = "age gate cleared and page reloaded, but still no JSON -- menu is server-rendered or behind another step"
        else:
            report["verdict"] = "no age gate found and no JSON fetched -- menu is server-rendered, or the page is a shell"
        return report

    hosts = Counter()
    products = 0
    paths: Counter = Counter()
    misses = {"name_no_price": [], "price_no_name": []}
    for p in payloads:
        url = p.get("url", "")
        hosts[url.split("/")[2] if "://" in url else url] += 1
        body = p.get("body")
        products += sum(1 for _ in walk(body))
        paths.update(_key_paths(body))
        m = _near_misses(body)
        misses["name_no_price"] += m["name_no_price"][:6]
        misses["price_no_name"] += m["price_no_name"][:6]

    report["json_hosts"] = dict(hosts.most_common(6))
    report["products_found"] = products
    report["name_no_price"] = misses["name_no_price"][:6]
    report["price_no_name"] = misses["price_no_name"][:6]
    report["promising_paths"] = [
        p for p, _ in paths.most_common(400)
        if any(w in p.lower() for w in ("product", "price", "menu", "item", "variant", "weight"))
    ][:20]

    if products:
        report["verdict"] = f"{products} product-shaped nodes present -- parser should have caught these"
    elif misses["name_no_price"]:
        report["verdict"] = "named things present but no price the parser recognizes -- PARSER GAP"
    elif misses["price_no_name"]:
        report["verdict"] = "prices present but no name the parser recognizes -- PARSER GAP"
    else:
        report["verdict"] = "JSON captured holds no menu data (wrong URL, or menu loads elsewhere)"
    return report


# How much a verdict tells us. A 404 on a guessed fallback URL is nearly
# worthless; a parser gap on the store's own menu is what we want to surface.
_VERDICT_RANK = [
    ("should have caught", 100),
    ("PARSER GAP", 90),
    ("holds no menu data", 60),
    ("still no JSON", 50),
    ("server-rendered", 40),
    ("blocked before", 30),
    ("failed to load", 20),
]


def _rank(verdict: str) -> int:
    for needle, score in _VERDICT_RANK:
        if needle in verdict:
            return score
    return 0


def run(samples_dir: Path) -> list[dict]:
    """One report per store, built from every URL that was attempted."""
    if not samples_dir.exists():
        return []
    by_store: dict[str, list[dict]] = {}
    for f in sorted(samples_dir.glob("*.json")):
        try:
            report = diagnose_store(f)
        except Exception:
            continue
        by_store.setdefault(report.get("store") or f.stem, []).append(report)

    out = []
    for store, reports in sorted(by_store.items()):
        # Most informative attempt wins; the rest become a one-line trail.
        best = max(reports, key=lambda r: (_rank(r["verdict"]),
                                           r.get("products_found") or 0,
                                           r.get("payload_count") or 0))
        best = dict(best)
        best["attempts"] = len(reports)
        best["trail"] = [
            f"{(r.get('page') or '')[:80]} -> "
            f"{'HTTP ' + str(r['status']) if r.get('status') and r['status'] >= 400 else r['verdict'][:60]}"
            for r in reports
        ]
        out.append(best)
    return out
