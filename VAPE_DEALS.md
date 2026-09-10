# Standing request

**Ask in chat: "What's the best deal today on vapes?" — answer it directly.**

No setup, no commands, no asking the user to run anything. They want an answer,
not a tool.

## The parameters (fixed, do not renegotiate)

- **Every price is RECREATIONAL and TAX-INCLUDED. No exceptions.** Never quote a
  menu/shelf price as if it were the cost. Multiply by **1.21375** (10% NV
  adult-use excise + 3% Clark County cannabis + 8.375% sales, quoted additively
  = 21.375%). A $40 sticker is **$48.55**. He is not using a medical card, so
  the 10% excise always applies. Say "out the door" or "with tax" on the figure.
- **Product: disposable vapes.** Not carts, not flower, not edibles, unless asked.
- **Anchor: ZIP 89148** (Spring Valley / southwest, near Durango & the 215).
- **Mode: delivery to 89148** (Rose Lake St). The drive-time radius is retired —
  what matters is whether a store delivers here and what it costs to clear their
  minimum. A 25-minute store that delivers free beats a 10-minute one that
  doesn't. The exact street address lives in `.env`, which is gitignored; never
  commit it.

## How to answer

Web search reaches live dispensary pricing even where this environment's network
proxy does not (it blocks dutchie/weedmaps/jane/leafly and every dispensary
domain — verified). So: **use WebSearch, not the scraper.**

1. Search for current LV disposable vape specials — a broad query plus targeted
   ones on the in-radius stores below.
2. **Do the delivery math, and lead with it.** Minimums and free-delivery
   thresholds apply to the PRE-TAX subtotal; tax and any fee land on top. Use
   `vegasdeals.pipeline.delivered_cost()` and `data/delivery.json`. A cheap
   sticker price behind a $10 fee loses to a dearer one delivered free — for a
   single item Zen Leaf's fee added 62%. Always show cost per unit at the order
   size they actually want, not just the shelf price.
3. Convert every deal to **out-the-door dollars per gram**:
   `$/g = (price / total_grams) x 1.21375`
   Clark County adult-use: 10% excise + 3% county cannabis + 8.375% sales,
   quoted additively = **21.375%**. A $40 sticker is $48.55.
   Per-gram is what makes a 2g deal comparable to a 1g one — always rank on it,
   never on the sticker price or the advertised percent off.
4. Rank, lead with the single best pick inside 20 minutes, and show the total
   they'll actually pay.
5. Say plainly that the numbers come from search results rather than live menus,
   and that specials rotate daily.

## Delivery terms

`data/delivery.json` holds each store's free-delivery threshold and fee.
Silver Sage ($25) and Cultivate ($30) have the easiest minimums; Zen Leaf
($100, $10 below) has the worst of the eight despite the best sticker prices.

## Stores inside 20 minutes of 89148 (pickup only — kept for reference)

| Store | Address | ~min |
|---|---|---|
| ShowGrow | S Fort Apache Rd, 89147 | <10 |
| The Dispensary NV – Decatur | 5347 S Decatur Blvd, 89118 | 13 |
| Euphoria Wellness | 7780 S Jones Blvd, 89139 | 14 |
| Cultivate – Spring Mountain | 3615 Spring Mountain Rd, 89102 | 15-18 |
| Jardin | Patrick Ln, 89118 | ~15 |

Borderline, name the time rather than assuming: **Planet 13** (2548 W Desert Inn
Rd, 89109) at ~21 min. Outside: **Inyo** (Maryland Pkwy, ~25 min), **Cultivate
Durango** (7105 N Durango, 89149 — that address is far northwest, not the
southwest Durango you'd assume).

## The scraper in `vegasdeals/`

Still there and still works, but it requires the user to run it on their own
machine, which is exactly what they said they don't want. Reach for it only if
they ask for it. Default answer path is web search, in chat.
