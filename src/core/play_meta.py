"""Google Play app-metadata fetch — the only online capability in this tool.

Deliberately isolated: no engine imports network code, and every failure mode
here degrades to a placeholder string rather than raising. The batch's HTML
reports, agent JSON and the other Excel sheets are produced identically whether
this module succeeds, finds no internet, or is never able to import its
optional dependency at all.

Two placeholder strings reach the sheet:
  NO_INTERNET   — the connectivity probe failed; the whole phase is skipped.
  NOT_AVAILABLE — internet is up but this one app could not be resolved
                  (removed from Play, region-locked, or an unexpected shape).
Neither is ever cached, so both retry on the next online run.
"""

import json
import socket
from datetime import datetime, timedelta
from pathlib import Path

from ui.terminal import print_info, print_ok, print_warn


NO_INTERNET   = "No internet connection"
NOT_AVAILABLE = "N/A"

_PROBE_TIMEOUT_SEC = 5
_CACHE_TTL_DAYS    = 30
_CACHE_SCHEMA      = "1.0"

# Sheet column order minus "Package Name", which never comes from Play.
_META_FIELDS = [
    "app_name", "category", "installs", "rating",
    "rating_count", "developer", "last_updated", "version",
]


def cache_path_for(script_dir: Path) -> Path:
    return script_dir / "data" / "reference" / "play_metadata_cache.json"


def _load_cache(path: Path) -> dict:
    """Return {package_name: {"fetched_at": iso, "data": {...}}}; {} on any problem."""
    try:
        raw = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}
    apps = raw.get("apps")
    return apps if isinstance(apps, dict) else {}


def _save_cache(path: Path, apps: dict) -> None:
    payload = {
        "schema_version": _CACHE_SCHEMA,
        "generated_at":   datetime.now().isoformat(timespec="seconds"),
        "apps":           apps,
    }
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(payload, ensure_ascii=False, indent=2),
                        encoding="utf-8")
    except OSError as exc:
        print_warn(f"Could not write metadata cache — {exc}")


def _is_fresh(entry: dict) -> bool:
    if not isinstance(entry, dict) or not isinstance(entry.get("data"), dict):
        return False
    try:
        stamped = datetime.fromisoformat(entry["fetched_at"])
    except (KeyError, TypeError, ValueError):
        return False
    return datetime.now() - stamped < timedelta(days=_CACHE_TTL_DAYS)


def _placeholder_row(value: str, app_name_fallback: str = "") -> dict:
    row = {f: value for f in _META_FIELDS}
    if value == NOT_AVAILABLE and app_name_fallback:
        row["app_name"] = app_name_fallback
    return row


def _extract(detail: dict, app_name_fallback: str = "") -> dict:
    """Map google-play-scraper's detail dict onto our nine sheet columns.

    NOTE: there is no size field. Play removed it from the detail page and the
    library exposes no equivalent, so the sheet has no Size column by design.
    """
    last_updated = detail.get("lastUpdatedOn")
    if not last_updated and detail.get("updated"):
        try:
            last_updated = datetime.fromtimestamp(detail["updated"]).strftime("%b %d, %Y")
        except (OSError, OverflowError, TypeError, ValueError):
            last_updated = None

    score = detail.get("score")
    return {
        "app_name":     detail.get("title") or app_name_fallback or NOT_AVAILABLE,
        "category":     detail.get("genre") or NOT_AVAILABLE,
        "installs":     detail.get("installs") or NOT_AVAILABLE,
        "rating":       round(score, 2) if isinstance(score, (int, float)) else NOT_AVAILABLE,
        "rating_count": detail.get("ratings") if isinstance(detail.get("ratings"), int) else NOT_AVAILABLE,
        "developer":    detail.get("developer") or NOT_AVAILABLE,
        "last_updated": last_updated or NOT_AVAILABLE,
        "version":      detail.get("version") or NOT_AVAILABLE,
    }


def _import_play(ensure_dep=None):
    """Import the optional scraper, invoking `ensure_dep` once if it is absent.

    Returns (app_fn, exception_class) or (None, None). The install hook is only
    reached when something actually needs fetching, so a fully-cached offline
    run never attempts a pip install.
    """
    for attempt in (0, 1):
        try:
            from google_play_scraper import app as play_app
            from google_play_scraper.exceptions import GooglePlayScraperException
            return play_app, GooglePlayScraperException
        except ImportError:
            if attempt or ensure_dep is None:
                return None, None
            ensure_dep()
    return None, None


def fetch_metadata(apps: list, cache_path: Path, ensure_dep=None) -> dict:
    """Fetch Play metadata for `apps`, serving from cache wherever possible.

    `apps` is a list of (package_name, apk_app_name) pairs in report order.
    Returns an ordered {package_name: {field: value}} dict covering every input
    app — no key is ever missing, so the sheet always has one row per APK.

    Never raises. Never blocks longer than the socket timeout per read.
    """
    ordered, seen = [], set()
    for pkg, apk_name in apps:
        pkg = (pkg or "").strip()
        if not pkg or pkg in seen:
            continue
        seen.add(pkg)
        ordered.append((pkg, apk_name or ""))

    if not ordered:
        return {}

    cache   = _load_cache(cache_path)
    results = {}
    pending = []
    for pkg, apk_name in ordered:
        entry = cache.get(pkg)
        if _is_fresh(entry):
            results[pkg] = dict(entry["data"])
        else:
            results[pkg] = None          # placeholder, filled below
            pending.append((pkg, apk_name))

    cached_n = len(ordered) - len(pending)
    if not pending:
        print_ok(f"App metadata: {cached_n} app(s) from cache — no network needed")
        return results

    print_info("Fetching app metadata from Google Play (requires internet)...")
    if cached_n:
        print_info(f"{cached_n} app(s) already cached, {len(pending)} to fetch")

    _play_app, GooglePlayScraperException = _import_play(ensure_dep)
    if _play_app is None:
        # Installing it needs pypi, so this is in practice the offline case.
        print_warn("google-play-scraper unavailable — skipping metadata, "
                   "batch continues with offline analysis")
        for pkg, _apk_name in pending:
            results[pkg] = _placeholder_row(NO_INTERNET)
        return results

    fetched  = 0
    offline  = False
    prev_timeout = socket.getdefaulttimeout()
    try:
        socket.setdefaulttimeout(_PROBE_TIMEOUT_SEC)
        for idx, (pkg, apk_name) in enumerate(pending):
            if offline:
                results[pkg] = _placeholder_row(NO_INTERNET)
                continue
            try:
                results[pkg] = _extract(_play_app(pkg), apk_name)
                cache[pkg] = {
                    "fetched_at": datetime.now().isoformat(timespec="seconds"),
                    "data":       results[pkg],
                }
                fetched += 1
            except GooglePlayScraperException:
                # Internet is up; this one app is gone or region-locked.
                # Common and expected for HK/Macau titles — not an error.
                results[pkg] = _placeholder_row(NOT_AVAILABLE, apk_name)
            except Exception as exc:
                # Connection-level failure: DNS, timeout, TLS, proxy. On the
                # probe this decides the whole phase; later it means the link
                # dropped mid-run. Either way stop hammering dead sockets.
                offline = True
                results[pkg] = _placeholder_row(NO_INTERNET)
                if idx == 0:
                    print_warn("No internet — skipping metadata, batch continues "
                               "with offline analysis")
                else:
                    print_warn(f"Connection lost after {fetched} app(s) "
                               f"({type(exc).__name__}) — remaining apps skipped")
    finally:
        socket.setdefaulttimeout(prev_timeout)

    if fetched:
        _save_cache(cache_path, cache)
        print_ok(f"App metadata: {fetched} fetched, {cached_n} from cache")

    return results
