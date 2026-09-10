"""Recreational, tax-inclusive pricing is a hard requirement, not a default.

Every price this tool reports is what the register will actually charge:
Nevada's 10% adult-use excise, Clark County's 3% cannabis tax and 8.375% sales
tax. Quoting a menu price would understate the real cost by more than a fifth,
so these tests fail if the recreational default ever changes or if a priced
offer escapes without tax applied.
"""
from __future__ import annotations

from vegasdeals.config import TaxModel, load_settings
from vegasdeals.normalize import Offer


def test_default_is_recreational():
    tax = load_settings().tax
    assert tax.medical_card is False, "must default to recreational (pays the excise)"
    assert abs(tax.multiplier - 1.21375) < 1e-9, "Clark County adult-use total"
    assert tax.out_the_door(100) == 121.38


def test_medical_is_cheaper_but_never_the_default():
    assert TaxModel(medical_card=True).multiplier < TaxModel().multiplier


def test_every_priced_offer_carries_tax():
    tax = TaxModel()
    for menu in (5.0, 15.25, 40.0, 199.99):
        offer = Offer(dispensary_id="d", dispensary_name="D", name="X",
                      raw_category="vape", size_text="1g",
                      menu_price=menu).enrich(tax)
        assert offer.out_the_door is not None
        assert offer.out_the_door > offer.menu_price, "price escaped without tax"
        assert abs(offer.out_the_door - round(menu * 1.21375, 2)) < 0.01
        # Unit price must be derived from the taxed figure, never the menu one.
        assert offer.unit_price == offer.out_the_door


def test_unit_price_is_taxed_for_multi_gram():
    tax = TaxModel()
    offer = Offer(dispensary_id="d", dispensary_name="D", name="2g Disposable",
                  raw_category="vape", size_text="2g", menu_price=40.0).enrich(tax)
    assert offer.grams == 2.0
    assert offer.unit_price == round(40.0 * 1.21375 / 2, 2)   # $24.28/g, not $20
