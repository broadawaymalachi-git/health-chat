"""CLI: python -m vegasdeals <resolve|refresh|ask|serve|status>"""
from __future__ import annotations

import argparse
import asyncio
import json
import logging
import sys

from . import ask as ask_mod, db, dispensaries as ds
from .config import DB_PATH, SEED_PATH, load_settings
from .pipeline import in_radius, refresh, resolve


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="vegasdeals")
    sub = parser.add_subparsers(dest="cmd", required=True)
    sub.add_parser("resolve", help="Find each store's menu URL, address and drive time")
    sub.add_parser("refresh", help="Scrape every store in range and score the offers")
    sub.add_parser("status", help="Show what the last run managed to collect")
    p_rad = sub.add_parser(
        "radius", help="Show which parts of the valley fall inside your drive-time budget")
    p_rad.add_argument("--minutes", type=int, default=None,
                       help="Override VD_DRIVE_MINUTES for this check")
    p_ask = sub.add_parser("ask", help="Ask a question about today's deals")
    p_ask.add_argument("question", nargs="+")
    p_serve = sub.add_parser("serve", help="Run the web app")
    p_serve.add_argument("--host", default="127.0.0.1")
    p_serve.add_argument("--port", type=int, default=8000)

    args = parser.parse_args(argv)
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    settings = load_settings()

    if args.cmd == "resolve":
        stores = resolve(settings)
        near = in_radius(stores, settings.drive_minutes)
        print(f"\nResolved {len(stores)} stores; {len(near)} within "
              f"{settings.drive_minutes} min of {settings.anchor}:")
        for s in sorted(near, key=lambda x: x.drive_minutes or 999):
            mins = f"{s.drive_minutes:.0f}m" if s.drive_minutes is not None else "  ?"
            print(f"  {mins:>4}  {s.name:<32} {s.platform or '?':<9} {s.scrape_url}")
        return 0

    if args.cmd == "radius":
        from .geo import LV_ZIP_CENTROIDS, Point, drive_minutes_matrix, geocode

        budget = args.minutes or settings.drive_minutes
        origin = geocode(settings.anchor)
        if origin is None:
            print(f"Could not geocode {settings.anchor!r}.")
            return 1

        zips = sorted(LV_ZIP_CENTROIDS)
        minutes = drive_minutes_matrix(
            origin, [Point(*LV_ZIP_CENTROIDS[z]) for z in zips],
            settings.ors_api_key, settings.fallback_mph,
        )
        mode = "road-network (OpenRouteService)" if settings.ors_api_key else \
               f"straight-line at {settings.fallback_mph:g} mph"
        print(f"Anchor {settings.anchor} · budget {budget} min · {mode}\n")

        ranked = sorted((m, z) for z, m in zip(zips, minutes) if m is not None)
        inside = [(m, z) for m, z in ranked if m <= budget]
        near = [(m, z) for m, z in ranked if budget < m <= budget + 6]

        print(f"Inside the budget ({len(inside)} ZIPs):")
        print("  " + "  ".join(f"{z}({m:.0f})" for m, z in inside))
        if near:
            print(f"\nJust outside ({len(near)} ZIPs) -- these are the ones a real")
            print("road route may well pull in, especially near the 215:")
            print("  " + "  ".join(f"{z}({m:.0f})" for m, z in near))
        if not settings.ors_api_key and near:
            print("\nStraight-line distance is a rough proxy. If any of those "
                  "near-miss ZIPs\nmatter to you, set ORS_API_KEY for real drive "
                  "times (free, 2000/day),\nor raise VD_FALLBACK_MPH.")
        return 0

    if args.cmd == "refresh":
        summary = asyncio.run(refresh(settings))
        print(json.dumps(summary, indent=2, default=str))
        return 0

    if args.cmd == "status":
        with db.connect(DB_PATH) as conn:
            run_id = db.latest_run_id(conn)
            if run_id is None:
                print("No completed runs yet. Try: python -m vegasdeals refresh")
                return 1
            run = dict(conn.execute("SELECT * FROM runs WHERE id=?", (run_id,)).fetchone())
            rows = [dict(r) for r in conn.execute(
                "SELECT * FROM store_status ORDER BY last_offers DESC").fetchall()]
        print(f"Run {run['id']} finished {run['finished_at']}: "
              f"{run['offer_count']} offers from {run['stores_ok']} stores "
              f"({run['stores_failed']} empty)")
        for r in rows:
            flag = "ok " if r["last_offers"] else "EMPTY"
            print(f"  {flag} {r['dispensary_id']:<16} {r['last_offers']:>5} offers "
                  f"{r['last_error'] or ''}")
        return 0

    if args.cmd == "ask":
        question = " ".join(args.question)
        with db.connect(DB_PATH) as conn:
            run_id = db.latest_run_id(conn)
            if run_id is None:
                print("No menu data yet. Run: python -m vegasdeals refresh")
                return 1
            query = ask_mod.extract_filters(
                question, settings.anthropic_api_key, settings.model)
            filters = query.model_dump()
            if filters.get("max_drive_minutes") is None:
                filters["max_drive_minutes"] = settings.drive_minutes
            rows = db.query_offers(conn, run_id, filters)
        print(ask_mod.answer(question, rows, settings.anthropic_api_key, settings.model))
        return 0

    if args.cmd == "serve":
        import uvicorn
        uvicorn.run("vegasdeals.web:app", host=args.host, port=args.port)
        return 0

    return 1


if __name__ == "__main__":
    sys.exit(main())
