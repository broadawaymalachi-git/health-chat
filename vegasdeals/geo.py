"""Geocoding and the 20-minute drive-time filter."""
from __future__ import annotations

import json
import logging
import math
import urllib.parse
import urllib.request
from dataclasses import dataclass

log = logging.getLogger(__name__)

UA = {"User-Agent": "vegasdeals/0.1 (personal deal finder)"}
LAS_VEGAS_BBOX = (-115.55, 35.85, -114.85, 36.40)  # w, s, e, n


@dataclass(frozen=True)
class Point:
    lat: float
    lon: float


def _fetch(url: str, timeout: int = 20) -> dict | list | None:
    try:
        req = urllib.request.Request(url, headers=UA)
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return json.loads(resp.read().decode())
    except Exception as exc:
        log.debug("fetch failed %s: %s", url, exc)
        return None


def geocode(query: str) -> Point | None:
    """Address / ZIP / cross-street -> lat-lon.

    Census first (free, no key, no rate limit, US-only and accurate for street
    addresses), then Nominatim, then a small local ZIP table so a plain ZIP works
    even fully offline.
    """
    census = (
        "https://geocoding.geo.census.gov/geocoder/locations/onelineaddress?"
        + urllib.parse.urlencode({
            "address": query, "benchmark": "Public_AR_Current", "format": "json",
        })
    )
    data = _fetch(census)
    try:
        matches = data["result"]["addressMatches"]  # type: ignore[index]
        if matches:
            c = matches[0]["coordinates"]
            return Point(lat=float(c["y"]), lon=float(c["x"]))
    except Exception:
        pass

    nominatim = "https://nominatim.openstreetmap.org/search?" + urllib.parse.urlencode({
        "q": query if "vegas" in query.lower() or "nv" in query.lower()
        else f"{query}, Las Vegas, NV",
        "format": "json", "limit": 1,
    })
    data = _fetch(nominatim)
    if isinstance(data, list) and data:
        return Point(lat=float(data[0]["lat"]), lon=float(data[0]["lon"]))

    zip_code = "".join(ch for ch in query if ch.isdigit())[:5]
    if zip_code in LV_ZIP_CENTROIDS:
        lat, lon = LV_ZIP_CENTROIDS[zip_code]
        log.info("geocoded %s from the local ZIP table", zip_code)
        return Point(lat, lon)
    return None


def haversine_miles(a: Point, b: Point) -> float:
    r = 3958.8
    dlat = math.radians(b.lat - a.lat)
    dlon = math.radians(b.lon - a.lon)
    h = (math.sin(dlat / 2) ** 2
         + math.cos(math.radians(a.lat)) * math.cos(math.radians(b.lat))
         * math.sin(dlon / 2) ** 2)
    return 2 * r * math.asin(math.sqrt(h))


def drive_minutes_matrix(
    origin: Point, destinations: list[Point], ors_api_key: str | None, fallback_mph: float
) -> list[float | None]:
    """Minutes from origin to each destination.

    With an OpenRouteService key this is a real road-network duration. Without
    one it's straight-line distance at an average Las Vegas surface-street speed
    -- good enough to sort stores into "close" and "not close", but it will
    under-estimate anything the 215 or a mountain sits between.
    """
    if ors_api_key and destinations:
        result = _ors_matrix(origin, destinations, ors_api_key)
        if result:
            return result
    return [
        round(haversine_miles(origin, d) / fallback_mph * 60, 1) for d in destinations
    ]


def _ors_matrix(origin: Point, destinations: list[Point], key: str) -> list[float | None] | None:
    body = json.dumps({
        "locations": [[origin.lon, origin.lat]] + [[d.lon, d.lat] for d in destinations],
        "sources": [0],
        "destinations": list(range(1, len(destinations) + 1)),
        "metrics": ["duration"],
    }).encode()
    req = urllib.request.Request(
        "https://api.openrouteservice.org/v2/matrix/driving-car",
        data=body,
        headers={"Authorization": key, "Content-Type": "application/json", **UA},
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode())
        durations = data["durations"][0]
        return [round(d / 60.0, 1) if d is not None else None for d in durations]
    except Exception as exc:
        log.warning("ORS matrix failed (%s); falling back to straight-line", exc)
        return None


# Centroids for Las Vegas valley ZIPs, so `VD_ANCHOR=89123` resolves with no
# network at all. Approximate by design -- a ZIP centroid is not an address.
LV_ZIP_CENTROIDS: dict[str, tuple[float, float]] = {
    "89101": (36.1745, -115.1372), "89102": (36.1516, -115.1889),
    "89103": (36.1114, -115.2064), "89104": (36.1553, -115.1130),
    "89106": (36.1806, -115.1633), "89107": (36.1714, -115.2136),
    "89108": (36.2028, -115.2189), "89109": (36.1215, -115.1620),
    "89110": (36.1706, -115.0503), "89113": (36.0641, -115.2523),
    "89117": (36.1428, -115.2833), "89118": (36.0736, -115.2136),
    "89119": (36.0842, -115.1428), "89120": (36.0742, -115.0925),
    "89121": (36.1108, -115.0919), "89122": (36.1064, -115.0447),
    "89123": (36.0353, -115.1522), "89128": (36.1975, -115.2586),
    "89129": (36.2364, -115.2839), "89130": (36.2531, -115.2153),
    "89131": (36.2969, -115.2447), "89134": (36.1994, -115.3050),
    "89135": (36.1189, -115.3308), "89138": (36.1631, -115.3617),
    "89139": (36.0264, -115.2072), "89141": (35.9931, -115.2019),
    "89142": (36.1522, -115.0389), "89143": (36.3033, -115.2864),
    "89144": (36.1725, -115.3197), "89145": (36.1583, -115.2833),
    "89146": (36.1400, -115.2306), "89147": (36.1058, -115.2778),
    "89148": (36.0728, -115.3169), "89149": (36.2811, -115.3078),
    "89156": (36.1811, -115.0342), "89158": (36.1080, -115.1760),
    "89166": (36.2986, -115.3564), "89169": (36.1256, -115.1381),
    "89178": (36.0053, -115.2761), "89179": (35.9611, -115.2489),
    "89183": (36.0031, -115.1614), "89052": (35.9908, -115.1281),
    "89012": (36.0175, -115.0450), "89014": (36.0553, -115.0644),
    "89015": (36.0367, -114.9689), "89011": (36.0783, -114.9333),
    "89074": (36.0431, -115.0872), "89002": (35.9967, -114.9861),
    "89030": (36.2044, -115.1236), "89031": (36.2603, -115.1500),
    "89032": (36.2183, -115.1600), "89081": (36.2708, -115.1069),
    "89084": (36.2933, -115.1367), "89086": (36.2775, -115.1319),
}
