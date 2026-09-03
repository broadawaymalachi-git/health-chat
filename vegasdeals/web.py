"""FastAPI app: a nightly refresh plus a page you can ask questions on."""
from __future__ import annotations

import asyncio
import logging
from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from . import ask as ask_mod, db, dispensaries as ds
from .config import DB_PATH, SEED_PATH, load_settings
from .pipeline import in_radius, refresh

log = logging.getLogger(__name__)
STATIC = Path(__file__).parent / "static"

_refresh_lock = asyncio.Lock()


async def _run_refresh() -> dict:
    """Scrape, guarded so a scheduled run and a manual one can't overlap."""
    if _refresh_lock.locked():
        return {"status": "already running"}
    async with _refresh_lock:
        settings = load_settings()
        try:
            return await refresh(settings)
        except Exception as exc:
            log.exception("refresh failed")
            return {"status": "failed", "error": f"{type(exc).__name__}: {exc}"}


@asynccontextmanager
async def lifespan(app: FastAPI):
    from apscheduler.schedulers.asyncio import AsyncIOScheduler
    from apscheduler.triggers.cron import CronTrigger

    scheduler = AsyncIOScheduler(timezone="America/Los_Angeles")
    # Twice daily: early enough for morning specials, again for afternoon drops.
    scheduler.add_job(_run_refresh, CronTrigger(hour="8,15", minute=0),
                      id="refresh", max_instances=1, coalesce=True)
    scheduler.start()
    log.info("scheduler started (refresh at 08:00 and 15:00 Pacific)")
    try:
        yield
    finally:
        scheduler.shutdown(wait=False)


app = FastAPI(title="Vegas Dispensary Deals", lifespan=lifespan)


class AskBody(BaseModel):
    question: str


@app.get("/")
async def index():
    return FileResponse(STATIC / "index.html")


@app.get("/api/status")
async def status():
    settings = load_settings()
    stores = ds.load(SEED_PATH)
    with db.connect(DB_PATH) as conn:
        run_id = db.latest_run_id(conn)
        run = None
        if run_id:
            run = dict(conn.execute(
                "SELECT * FROM runs WHERE id=?", (run_id,)).fetchone())
        store_rows = [dict(r) for r in conn.execute(
            "SELECT * FROM store_status ORDER BY last_offers DESC").fetchall()]
    return {
        "anchor": settings.anchor,
        "drive_minutes": settings.drive_minutes,
        "tax_multiplier": round(settings.tax.multiplier, 4),
        "stores_total": len(stores),
        "stores_in_radius": len(in_radius(stores, settings.drive_minutes)),
        "latest_run": run,
        "stores": store_rows,
    }


@app.post("/api/refresh")
async def trigger_refresh():
    return await _run_refresh()


@app.post("/api/ask")
async def ask(body: AskBody):
    settings = load_settings()
    with db.connect(DB_PATH) as conn:
        run_id = db.latest_run_id(conn)
        if run_id is None:
            return JSONResponse(
                {"answer": "No menu data yet. Run a refresh first "
                           "(`python -m vegasdeals refresh`, or the button above).",
                 "results": []},
                status_code=200,
            )
        query = await asyncio.to_thread(
            ask_mod.extract_filters, body.question,
            settings.anthropic_api_key, settings.model,
        )
        filters = query.model_dump()
        filters.setdefault("max_drive_minutes", None)
        if filters.get("max_drive_minutes") is None:
            filters["max_drive_minutes"] = settings.drive_minutes
        rows = db.query_offers(conn, run_id, filters)

    context = (f"Anchor {settings.anchor}, within {settings.drive_minutes} minutes' "
               f"drive. Prices include Clark County taxes.")
    answer_text = await asyncio.to_thread(
        ask_mod.answer, body.question, rows,
        settings.anthropic_api_key, settings.model, context,
    )
    return {"answer": answer_text, "filters": filters, "results": rows}


if STATIC.exists():
    app.mount("/static", StaticFiles(directory=STATIC), name="static")
