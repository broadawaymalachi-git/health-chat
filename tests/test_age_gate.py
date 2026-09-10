"""The age gate must be clicked AND the page reloaded, against a real browser.

gate2.html deliberately uses a storage key the scraper does not pre-seed, so
the gate can only be passed by actually clicking it, and it does not fetch the
menu on click -- only a fresh load mounts it. That combination is what real
dispensary sites do, and an earlier version of this test passed for the wrong
reason: the pre-seeded key satisfied the gate and no click ever happened.
"""
from __future__ import annotations

import asyncio
import shutil
import subprocess
import sys
import time
from pathlib import Path

from vegasdeals.harvest import harvest
from vegasdeals.parsers import offers_from_payloads

SITE = Path(__file__).parent / "fixtures" / "site"
PORT = 8907


def test_gate_clicked_and_reloaded(tmp_path: Path):
    server = subprocess.Popen([sys.executable, str(SITE / "server.py")],
                              stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    try:
        time.sleep(2)
        state = tmp_path / "state"
        shutil.rmtree(state, ignore_errors=True)
        cap = asyncio.run(harvest(
            [("g2", f"http://127.0.0.1:8901/gate2.html")],
            headless=True, concurrency=1, delay_seconds=0.1, storage_dir=state,
        ))[0]
        assert cap.gate_found, "age gate was not detected"
        assert cap.reloaded, "page was not reloaded after clearing the gate"
        offers = offers_from_payloads(cap.payloads, "g2", "Gated Shop 2")
        assert offers, "menu JSON was never captured"
        assert {o.size_text for o in offers} == {"1g", "0.5g"}
    finally:
        server.terminate()
