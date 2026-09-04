"""Resolve stores, scrape menus, score offers, write a run to the database."""
from __future__ import annotations

import asyncio
import json
import logging
import os
import urllib.request
from pathlib import Path

from . import db, dispensaries as ds
from .config import Settings, DATA_DIR, DB_PATH, SEED_PATH, STORAGE_STATE_DIR
from .geo import Point, drive_minutes_matrix, geocode
from .harvest import harvest
from .normalize import Offer, score_offers
from .parsers import offers_from_payloads

log = logging.getLogger(__name__)

# How many candidate URLs to try per store before giving up on it.
MAX_URL_ROUNDS = 4


def _save_sample(store_id: str, cap) -> None:
    """Dump a slice of raw captured JSON for diagnosing parser gaps.

    Without this there is no way to tell a store that blocked us from one whose
    fields we simply failed to recognize -- both look like zero offers.
    """
    out = DATA_DIR / "samples"
    out.mkdir(parents=True, exist_ok=True)
    sample = [{"url": p["url"], "body": p["body"]} for p in cap.payloads[:8]]
    try:
        text = json.dumps(
            {"store": store_id, "page": cap.url, "error": cap.error,
             "payload_count": len(cap.payloads), "payloads": sample},
            default=str)[:2_000_000]
        (out / f"{store_id}.json").write_text(text)
    except Exception as exc:
        log.debug("could not save sample for %s: %s", store_id, exc)


def _get_html(url: str, timeout: int = 20) -> str:
    req = urllib.request.Request(url, headers={
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
    })
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read().decode("utf-8", errors="replace")


def resolve(settings: Settings, seed_path: Path = SEED_PATH) -> list[ds.Dispensary]:
    """Fill in each store's menu URL, platform, address and drive time.

    Safe to re-run; it only overwrites fields it successfully resolves, so a
    store you corrected by hand keeps your correction unless the site changes.
    """
    stores = ds.load(seed_path)
    origin = geocode(settings.anchor)
    if origin is None:
        log.warning("could not geocode anchor %r -- drive times will be blank",
                    settings.anchor)

    for store in stores:
        try:
            html = _get_html(store.website)
        except Exception as exc:
            log.warning("%s: could not load %s (%s)", store.name, store.website, exc)
            store.notes = f"unreachable: {type(exc).__name__}"
            continue

        store.platform = ds.detect_platform(html) or store.platform
        store.menu_url = ds.find_menu_url(html, store.website) or store.menu_url
        store.address = ds.extract_address(html) or store.address
        if store.address and store.lat is None:
            point = geocode(store.address)
            if point:
                store.lat, store.lon = point.lat, point.lon
        log.info("%-28s platform=%-9s menu=%s", store.name,
                 store.platform or "?", store.menu_url or store.website)

    if origin:
        located = [s for s in stores if s.lat is not None and s.lon is not None]
        if located:
            minutes = drive_minutes_matrix(
                origin, [Point(s.lat, s.lon) for s in located],  # type: ignore[arg-type]
                settings.ors_api_key, settings.fallback_mph,
            )
            for store, mins in zip(located, minutes):
                store.drive_minutes = mins

    ds.save(seed_path, stores)
    return stores


def in_radius(stores: list[ds.Dispensary], minutes: int) -> list[ds.Dispensary]:
    """Stores inside the drive-time budget.

    A store whose drive time never resolved is kept rather than dropped -- a
    missing coordinate shouldn't silently hide a dispensary that's next door.
    """
    return [
        s for s in stores
        if s.enabled and (s.drive_minutes is None or s.drive_minutes <= minutes)
    ]


async def refresh(settings: Settings, db_path: Path = DB_PATH,
                  seed_path: Path = SEED_PATH) -> dict:
    """One full scrape cycle. Returns a summary dict."""
    stores = ds.load(seed_path)
    if not stores:
        raise RuntimeError(f"no dispensaries in {seed_path}")

    targets = in_radius(stores, settings.drive_minutes)
    log.info("refreshing %d of %d stores within %d minutes",
             len(targets), len(stores), settings.drive_minutes)

    by_id = {s.id: s for s in targets}
    all_offers: list[Offer] = []
    ok = failed = 0
    statuses: list[tuple[str, bool, int, str | None]] = []

    # Round-robin the candidate URLs: everyone tries their best URL, then only
    # the stores that came back empty try their next one. This keeps the common
    # case to a single page load per store while still rescuing the ones whose
    # menu isn't where we first guessed.
    pending = {s.id: list(s.candidate_urls) for s in targets}
    found: dict[str, list[Offer]] = {}
    last_error: dict[str, str | None] = {s.id: None for s in targets}

    for round_no in range(MAX_URL_ROUNDS):
        batch = [(sid, urls.pop(0)) for sid, urls in pending.items()
                 if urls and sid not in found]
        if not batch:
            break
        log.info("round %d: trying %d store URLs", round_no + 1, len(batch))
        captures = await harvest(
            batch,
            headless=settings.headless,
            concurrency=settings.concurrency,
            delay_seconds=settings.delay_seconds,
            storage_dir=STORAGE_STATE_DIR,
        )
        for cap in captures:
            store = by_id[cap.dispensary_id]
            offers = offers_from_payloads(cap.payloads, store.id, store.name)
            for o in offers:
                o.drive_minutes = store.drive_minutes
                o.enrich(settings.tax)
            offers = [o for o in offers if o.out_the_door is not None]
            if os.getenv("VD_SAVE_SAMPLES"):
                _save_sample(store.id, cap)
            if offers:
                found[store.id] = offers
                # Remember what worked so the next run goes straight there.
                store.menu_url = cap.url
                log.info("%-28s %4d offers via %s", store.name, len(offers), cap.url)
            else:
                last_error[store.id] = cap.error or "loaded but no offers parsed"

    for store in targets:
        offers = found.get(store.id, [])
        all_offers.extend(offers)
        if offers:
            ok += 1
        else:
            failed += 1
        statuses.append((store.id, bool(offers), len(offers),
                         None if offers else last_error[store.id]))

    ds.save(seed_path, stores)

    score_offers(all_offers)

    with db.connect(db_path) as conn:
        run_id = db.start_run(conn)
        db.insert_offers(conn, run_id, all_offers)
        for sid, succeeded, count, err in statuses:
            db.record_status(conn, sid, succeeded, count, err)
        db.finish_run(conn, run_id, ok, failed, len(all_offers))

    return {
        "run_id": run_id, "stores_ok": ok, "stores_failed": failed,
        "offers": len(all_offers),
        "top": [
            {"name": o.name, "store": o.dispensary_name, "price": o.out_the_door,
             "unit_price": o.unit_price, "why": o.score_reasons}
            for o in all_offers[:10]
        ],
    }


def refresh_sync(settings: Settings, **kw) -> dict:
    return asyncio.run(refresh(settings, **kw))
