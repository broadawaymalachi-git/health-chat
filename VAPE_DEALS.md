# Standing request

**Ask in chat: "What's the best deal today on vapes?" — answer it directly.**

No setup, no commands, no asking the user to run anything. They want an answer,
not a tool.

## The parameters (fixed, do not renegotiate)

- **Product: disposable vapes.** Not carts, not flower, not edibles, unless asked.
- **Anchor: ZIP 89148** (Spring Valley / southwest, near Durango & the 215).
- **Radius: 20 minutes. Exactly.** 21 is out. If a store is borderline, name the
  drive time and let them decide — do not silently include it.

## How to answer

Web search reaches live dispensary pricing even where this environment's network
proxy does not (it blocks dutchie/weedmaps/jane/leafly and every dispensary
domain — verified). So: **use WebSearch, not the scraper.**

1. Search for current LV disposable vape specials — a broad query plus targeted
   ones on the in-radius stores below.
2. Convert every deal to **out-the-door dollars per gram**:
   `$/g = (price / total_grams) x 1.21375`
   Clark County adult-use: 10% excise + 3% county cannabis + 8.375% sales,
   quoted additively = **21.375%**. A $40 sticker is $48.55.
   Per-gram is what makes a 2g deal comparable to a 1g one — always rank on it,
   never on the sticker price or the advertised percent off.
3. Rank, lead with the single best pick inside 20 minutes, and show the total
   they'll actually pay.
4. Say plainly that the numbers come from search results rather than live menus,
   and that specials rotate daily.

## Stores inside 20 minutes of 89148

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
