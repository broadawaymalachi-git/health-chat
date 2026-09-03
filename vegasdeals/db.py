"""SQLite storage. One row per offer per refresh, so price history is free."""
from __future__ import annotations

import sqlite3
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path

from .normalize import Offer

SCHEMA = """
CREATE TABLE IF NOT EXISTS runs (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    started_at  TEXT NOT NULL,
    finished_at TEXT,
    stores_ok   INTEGER DEFAULT 0,
    stores_failed INTEGER DEFAULT 0,
    offer_count INTEGER DEFAULT 0,
    notes       TEXT
);
CREATE TABLE IF NOT EXISTS offers (
    id             INTEGER PRIMARY KEY AUTOINCREMENT,
    run_id         INTEGER NOT NULL REFERENCES runs(id),
    dispensary_id  TEXT NOT NULL,
    dispensary_name TEXT NOT NULL,
    name           TEXT NOT NULL,
    brand          TEXT,
    category       TEXT,
    size_text      TEXT,
    grams          REAL,
    thc_mg         REAL,
    thc_percent    REAL,
    menu_price     REAL,
    base_price     REAL,
    out_the_door   REAL,
    unit_basis     TEXT,
    unit_price     REAL,
    percent_off    REAL,
    absolute_savings REAL,
    market_percentile REAL,
    score          REAL,
    score_reasons  TEXT,
    promo_text     TEXT,
    drive_minutes  REAL,
    url            TEXT
);
CREATE INDEX IF NOT EXISTS idx_offers_run ON offers(run_id);
CREATE INDEX IF NOT EXISTS idx_offers_cat ON offers(run_id, category);
CREATE INDEX IF NOT EXISTS idx_offers_score ON offers(run_id, score DESC);
CREATE TABLE IF NOT EXISTS store_status (
    dispensary_id TEXT PRIMARY KEY,
    last_ok       TEXT,
    last_error    TEXT,
    last_offers   INTEGER DEFAULT 0
);
"""


def now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


@contextmanager
def connect(path: Path):
    path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    try:
        conn.executescript(SCHEMA)
        yield conn
        conn.commit()
    finally:
        conn.close()


def start_run(conn) -> int:
    cur = conn.execute("INSERT INTO runs (started_at) VALUES (?)", (now(),))
    return int(cur.lastrowid)


def finish_run(conn, run_id: int, ok: int, failed: int, count: int, notes: str = "") -> None:
    conn.execute(
        "UPDATE runs SET finished_at=?, stores_ok=?, stores_failed=?, offer_count=?, notes=?"
        " WHERE id=?",
        (now(), ok, failed, count, notes, run_id),
    )


def insert_offers(conn, run_id: int, offers: list[Offer]) -> None:
    conn.executemany(
        """INSERT INTO offers (run_id, dispensary_id, dispensary_name, name, brand,
           category, size_text, grams, thc_mg, thc_percent, menu_price, base_price,
           out_the_door, unit_basis, unit_price, percent_off, absolute_savings,
           market_percentile, score, score_reasons, promo_text, drive_minutes, url)
           VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
        [(run_id, o.dispensary_id, o.dispensary_name, o.name, o.brand, o.category,
          o.size_text, o.grams, o.thc_mg, o.thc_percent, o.menu_price, o.base_price,
          o.out_the_door, o.unit_basis, o.unit_price, o.percent_off, o.absolute_savings,
          o.market_percentile, o.score, " · ".join(o.score_reasons), o.promo_text,
          o.drive_minutes, o.url) for o in offers],
    )


def record_status(conn, dispensary_id: str, ok: bool, count: int, error: str | None) -> None:
    conn.execute(
        """INSERT INTO store_status (dispensary_id, last_ok, last_error, last_offers)
           VALUES (?,?,?,?)
           ON CONFLICT(dispensary_id) DO UPDATE SET
             last_ok=COALESCE(excluded.last_ok, store_status.last_ok),
             last_error=excluded.last_error, last_offers=excluded.last_offers""",
        (dispensary_id, now() if ok else None, error, count),
    )


def latest_run_id(conn) -> int | None:
    row = conn.execute(
        "SELECT id FROM runs WHERE finished_at IS NOT NULL ORDER BY id DESC LIMIT 1"
    ).fetchone()
    return int(row["id"]) if row else None


def query_offers(conn, run_id: int, filters: dict) -> list[dict]:
    """Ranked offers for a run, narrowed by the filter dict `ask` produces."""
    where = ["run_id = ?"]
    params: list = [run_id]

    if filters.get("categories"):
        marks = ",".join("?" * len(filters["categories"]))
        where.append(f"category IN ({marks})")
        params += filters["categories"]
    if filters.get("max_price") is not None:
        where.append("out_the_door <= ?")
        params.append(filters["max_price"])
    if filters.get("max_drive_minutes") is not None:
        where.append("(drive_minutes IS NULL OR drive_minutes <= ?)")
        params.append(filters["max_drive_minutes"])
    if filters.get("min_thc_percent") is not None:
        where.append("thc_percent >= ?")
        params.append(filters["min_thc_percent"])
    if filters.get("dispensary"):
        where.append("LOWER(dispensary_name) LIKE ?")
        params.append(f"%{filters['dispensary'].lower()}%")
    if filters.get("brand"):
        where.append("LOWER(COALESCE(brand,'')) LIKE ?")
        params.append(f"%{filters['brand'].lower()}%")
    if filters.get("text"):
        where.append("(LOWER(name) LIKE ? OR LOWER(COALESCE(brand,'')) LIKE ?)")
        needle = f"%{filters['text'].lower()}%"
        params += [needle, needle]
    if filters.get("only_discounted"):
        where.append("percent_off IS NOT NULL AND percent_off > 0")
    if filters.get("size_grams") is not None:
        target = float(filters["size_grams"])
        where.append("grams IS NOT NULL AND grams BETWEEN ? AND ?")
        params += [target * 0.85, target * 1.15]

    order = {
        "score": "score DESC",
        "unit_price": "unit_price ASC",
        "price": "out_the_door ASC",
        "percent_off": "percent_off DESC",
        "drive": "drive_minutes ASC",
    }.get(filters.get("sort") or "score", "score DESC")

    limit = int(filters.get("limit") or 25)
    sql = (f"SELECT * FROM offers WHERE {' AND '.join(where)} "
           f"ORDER BY {order} LIMIT ?")
    params.append(limit)
    return [dict(r) for r in conn.execute(sql, params).fetchall()]
