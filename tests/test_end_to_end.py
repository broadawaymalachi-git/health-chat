"""End-to-end over synthetic menus: parse -> price -> score -> store -> query."""
from __future__ import annotations

import json
from pathlib import Path

from vegasdeals import db
from vegasdeals.config import TaxModel
from vegasdeals.normalize import Offer, score_offers
from vegasdeals.parsers import offers_from_payloads

FIXTURES = Path(__file__).parent / "fixtures"


def dutchie_store(name, eighth_price, special=None):
    """A Dutchie-shaped menu with one flower product at a given eighth price."""
    prices = [eighth_price]
    product = {
        "id": f"{name}-1", "Name": f"House Flower ({name})",
        "brand": {"name": "House"}, "type": "Flower",
        "Options": ["3.5g"], "Prices": prices,
    }
    if special:
        product["recSpecialPrices"] = [special]
    return {"url": "https://dutchie.com/graphql", "body": {"data": {
        "filteredProducts": {"products": [product]}}}}


def test_value_beats_banner():
    """A store with no discount but a lower price should still win.

    This is the whole premise of the tool: "40% off" at a store whose regular
    price is high is worse than everyday-cheap somewhere else.
    """
    tax = TaxModel()
    offers = []
    # Four stores at $45 create a median; the discounter marks down from $60.
    for i in range(4):
        offers += offers_from_payloads([dutchie_store(f"mid{i}", 45)], f"m{i}", f"Mid {i}")
    offers += offers_from_payloads([dutchie_store("loud", 60, special=42)], "loud", "Loud Deals")
    offers += offers_from_payloads([dutchie_store("quiet", 30)], "quiet", "Quiet Value")

    for o in offers:
        o.enrich(tax)
    score_offers(offers)

    assert offers[0].dispensary_name == "Quiet Value", \
        f"expected the cheapest store to win, got {offers[0].dispensary_name}"
    loud = next(o for o in offers if o.dispensary_id == "loud")
    quiet = offers[0]
    assert quiet.score > loud.score
    assert quiet.unit_price < loud.unit_price
    return offers


def test_db_roundtrip(tmp_path: Path):
    tax = TaxModel()
    payloads = json.loads((FIXTURES / "payloads.json").read_text())
    offers = []
    for p in payloads:
        offers += offers_from_payloads([p], "d1", "Test Store")
    for o in offers:
        o.drive_minutes = 11.0
        o.enrich(tax)
    score_offers(offers)

    path = tmp_path / "t.db"
    with db.connect(path) as conn:
        run_id = db.start_run(conn)
        db.insert_offers(conn, run_id, offers)
        db.finish_run(conn, run_id, ok=1, failed=0, count=len(offers))
    with db.connect(path) as conn:
        assert db.latest_run_id(conn) == run_id
        flower = db.query_offers(conn, run_id, {"categories": ["flower"], "sort": "unit_price"})
        assert flower and all(r["category"] == "flower" for r in flower)
        assert flower == sorted(flower, key=lambda r: r["unit_price"])
        eighths = db.query_offers(conn, run_id, {"size_grams": 3.5})
        assert all(3.0 <= r["grams"] <= 4.0 for r in eighths)
        discounted = db.query_offers(conn, run_id, {"only_discounted": True})
        assert all(r["percent_off"] > 0 for r in discounted)
    return len(offers)


def test_tax_models():
    additive = TaxModel(mode="additive")
    compound = TaxModel(mode="compound")
    assert abs(additive.multiplier - 1.21375) < 1e-6
    assert compound.multiplier > additive.multiplier
    assert TaxModel(medical_card=True).multiplier < additive.multiplier
    assert additive.out_the_door(100) == 121.38
