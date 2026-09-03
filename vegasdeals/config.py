"""Runtime configuration, loaded from environment / .env."""
from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
DB_PATH = DATA_DIR / "deals.db"
STORAGE_STATE_DIR = DATA_DIR / "storage_state"
SEED_PATH = DATA_DIR / "dispensaries.seed.json"


def _f(name: str, default: float) -> float:
    try:
        return float(os.getenv(name, default))
    except (TypeError, ValueError):
        return default


def _b(name: str, default: bool) -> bool:
    return os.getenv(name, str(default)).strip().lower() in {"1", "true", "yes", "on"}


@dataclass(frozen=True)
class TaxModel:
    """Clark County adult-use cannabis taxes.

    Two models are supported because the commonly-quoted "21.35% in Las Vegas"
    is the *additive* sum of 10% excise + 3% county cannabis + 8.375% sales,
    while some registers compound sales tax on top of the excise-inclusive
    subtotal (which lands nearer 22.5%). Neither is wrong everywhere; registers
    differ. Ranking is relative, so the choice barely moves the leaderboard --
    but check a real receipt and set VD_TAX_MODE to whichever matches.
    """

    mode: str = "additive"
    excise: float = 0.10
    local_cannabis: float = 0.03
    sales: float = 0.08375
    medical_card: bool = False

    @property
    def multiplier(self) -> float:
        excise = 0.0 if self.medical_card else self.excise
        if self.mode == "compound":
            return (1 + excise) * (1 + self.local_cannabis + self.sales)
        return 1 + excise + self.local_cannabis + self.sales

    def out_the_door(self, menu_price: float) -> float:
        return round(menu_price * self.multiplier, 2)


@dataclass(frozen=True)
class Settings:
    anchor: str = "89148"
    drive_minutes: int = 20
    ors_api_key: str | None = None
    anthropic_api_key: str | None = None
    model: str = "claude-opus-5"
    concurrency: int = 3
    delay_seconds: float = 2.0
    headless: bool = True
    # Used only when no ORS key is present: Las Vegas surface-street average.
    fallback_mph: float = 26.0
    tax: TaxModel = TaxModel()


def load_settings() -> Settings:
    return Settings(
        anchor=os.getenv("VD_ANCHOR", "89148"),
        drive_minutes=int(_f("VD_DRIVE_MINUTES", 20)),
        ors_api_key=os.getenv("ORS_API_KEY") or None,
        anthropic_api_key=os.getenv("ANTHROPIC_API_KEY") or None,
        model=os.getenv("VD_MODEL", "claude-opus-5"),
        concurrency=int(_f("VD_CONCURRENCY", 3)),
        delay_seconds=_f("VD_DELAY_SECONDS", 2.0),
        headless=_b("VD_HEADLESS", True),
        fallback_mph=_f("VD_FALLBACK_MPH", 26.0),
        tax=TaxModel(
            mode=os.getenv("VD_TAX_MODE", "additive"),
            excise=_f("VD_EXCISE_RATE", 0.10),
            local_cannabis=_f("VD_LOCAL_CANNABIS_RATE", 0.03),
            sales=_f("VD_SALES_TAX_RATE", 0.08375),
            medical_card=_b("VD_MEDICAL_CARD", False),
        ),
    )
