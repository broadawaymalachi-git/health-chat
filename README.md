# Vegas Dispensary Deals

Finds the genuinely best cannabis deals within a drive-time radius of your
address in Las Vegas, so you don't have to open twenty dispensary websites.

Ask it things like *"best deal on an eighth"* or *"cheapest carts within 15
minutes"* from your phone, any time.

## What makes it different from a deals page

Weedmaps, Leafly and the local aggregators show you **advertised discounts**.
A "40% off" banner tells you nothing if that store's regular price is high.

This ranks on **what you actually pay**:

1. **Out-the-door price.** Menu prices exclude Clark County's cannabis taxes.
   Everything here is converted to what the register will charge you.
2. **Unit price.** `$/g` for flower, concentrate, carts and prerolls;
   `$/100mg THC` for edibles. An eighth is never compared against an ounce.
3. **Market position.** Every offer is scored against *today's median price for
   the same category and size across every store in your radius.* A store with
   no promotion at all can top the list by simply being cheaper — which is the
   entire point.

So the ranking answers "is $18 for an eighth actually good?" rather than
"who is shouting the loudest today?"

## Setup

```bash
pip install -r requirements.txt
playwright install chromium

cp .env.example .env
# Edit .env: set VD_ANCHOR to your ZIP, cross-streets or address,
# and ANTHROPIC_API_KEY if you want plain-English questions.

python -m vegasdeals resolve    # find each store's menu, address and drive time
python -m vegasdeals refresh    # scrape and score
python -m vegasdeals serve      # http://127.0.0.1:8000
```

`serve` refreshes on its own at 08:00 and 15:00 Pacific.

### Commands

| Command | What it does |
|---|---|
| `resolve` | Detects each store's menu platform, menu URL, address, drive time. Re-run when a store goes quiet. |
| `refresh` | Scrapes every store in range, prices and scores everything, writes a run. |
| `ask "..."` | One question from the terminal. |
| `status` | What the last run collected, per store. |
| `serve` | Web app + scheduled refreshes. |

## How the scraping works

Almost no Las Vegas dispensary hand-rolls its menu — they embed **Dutchie**,
**I Heart Jane**, **Weedmaps**, **Leafly**, Tymber or Sweed, all of which render
client-side from a private JSON API. A plain HTTP GET returns an empty shell.

So `harvest.py` drives a real Chromium via Playwright, and **captures the JSON
the page fetches for itself** rather than calling those APIs directly. That
matters: those endpoints are private and change shape without notice. Pinning a
GraphQL query would break within months; letting the page make its own calls
means that as long as the menu works in a browser, this keeps working.

`parsers.py` then walks whatever JSON came back looking for product-shaped
objects, with a broad field vocabulary covering all four platforms' naming.
It's verified against fixtures for each — see `tests/fixtures/payloads.json`.

**The 21+ age gate** you mentioned is a non-issue. It's a cookie, not a security
control: `harvest.py` pre-seeds the localStorage flags most menus check, clicks
through anything left, and saves the browser state so later runs skip it.

## Out-the-door pricing

Las Vegas adult-use cannabis carries a 10% retail excise tax, Clark County's 3%
cannabis tax, and 8.375% sales tax. Quoted **additively that's 21.375%**, which
is the default here (`VD_TAX_MODE=additive`, $100 → $121.38).

Some registers compound sales tax on the excise-inclusive subtotal instead,
landing nearer 22.5% — set `VD_TAX_MODE=compound` if that matches your receipts.
Set `VD_MEDICAL_CARD=true` to drop the 10% excise.

Ranking is relative, so this barely reorders the leaderboard — but it decides
whether the number shown matches what you hand over. **Check one real receipt
and set it accordingly.**

## Drive-time radius

Without a key, "20 minutes" is straight-line distance at an average Las Vegas
surface-street speed. Workable, but it will underestimate anything with the 215
or a mountain in the way.

For real road-network drive times, get a free
[OpenRouteService key](https://openrouteservice.org/dev/#/signup) (2000
requests/day, far more than this needs) and set `ORS_API_KEY`.

A store whose coordinates never resolved is **kept**, not dropped — a missing
address shouldn't silently hide a dispensary that's next door.

## Honest limitations

- **The scrapers have not been run against live dispensary sites.** They were
  built and verified against captured-shape fixtures for all four platforms,
  because the environment this was written in blocks outbound traffic to those
  domains. Expect to run `resolve`, then `status`, and fix the stores that come
  back `EMPTY`. That's the expected first-run experience, not a malfunction.
- **The seed store list needs your eyes.** `data/dispensaries.seed.json` carries
  names and websites only; everything else is resolved at runtime, deliberately,
  because a hardcoded wrong address silently drops a store from your radius.
  Add, remove and correct entries freely — it's just JSON.
- **Deals ≠ in stock.** Inventory moves faster than any scrape. Confirm before
  you drive.
- **Menu prices can lag the register**, and some promos (first-time patient,
  veteran, happy hour, bundle pricing) never appear on the menu at all.
- **Terms of service.** This fetches the same public menu endpoints your browser
  does, one user, rate-limited, for personal use. Weedmaps' and Leafly's ToS
  prohibit scraping their sites — prefer pointing this at dispensaries' own
  menus. Don't redistribute the output publicly. Not legal advice.

## Already exists?

Partly, and it's worth ten minutes before you run this:

- [Weedmaps LV deals](https://weedmaps.com/deals/united-states/nevada/las-vegas)
  — widest coverage, free, but it's advertiser-driven and ranks nothing.
- [CloudedDeals](https://cloudeddeals.com/las-vegas-dispensary-deals) — scans
  27+ LV dispensaries daily and ranks by discount and value. Closest to this.
- [Chief Trees](https://www.chieftrees.com/vegasdeals) — hand-curated daily
  list of LV dispensary deals.

None of them filter by **drive time from your address**, normalize to
**out-the-door unit price**, or let you **ask in plain English** — which is why
this exists.

## Tests

```bash
python -m pytest tests/ -v      # or run tests/test_end_to_end.py directly
```

`test_value_beats_banner` is the one that matters: it builds a synthetic market
where one store shouts "30% off" from a high base and another is quietly
cheaper, and asserts the quiet one wins.
