"""OHPM registry fetcher — the second online capability in this tool.

Isolated for the same reason `play_meta.py` is: no engine, renderer or mapping
code opens a socket. Everything here degrades to an empty/partial result rather
than raising, and every request is bounded by `_TIMEOUT_SEC`.

Unlike `play_meta.py` this needs **no third-party dependency** — the OHPM API is
plain JSON over stdlib `urllib`, so there is no `_ensure_*` hook and nothing to
pip-install. It is a manually-run builder script in the mould of `api_index.py`:

    python src/core/ohpm_fetch.py            # resume/refresh the sweep
    python src/core/ohpm_fetch.py --force    # discard and re-sweep from page 1
    python src/core/ohpm_fetch.py --check @ohos/lottie

Endpoints (discovered by reading the SPA bundle `/assets/index-*.js`, which
inlines the base-URL table `mP="/ohpmweb/registry"`, `Loe="/ohpm"`):

  search    GET /ohpmweb/registry/oh-package/openapi/v1/search
            ?condition=&pageNum=N&pageSize=100&sortedType=relevancy&isHomePage=false
            All five params are REQUIRED. `sortedType` must be the literal
            "relevancy" — "relevance" returns HTTP 400 {"message":"参数异常"}.
            An empty `condition` enumerates the whole registry.
  detail    GET /ohpmweb/registry/oh-package/openapi/v1/detail/{urlencoded}[/{ver}]
  tech-map  GET /ohpm/tech-map   (note: /ohpm/, NOT /ohpmweb/)

Three behaviours of this API are load-bearing and easy to get wrong:

1. **A missing package returns HTTP 200, not 404.** `body` degrades from an
   object to the literal string "success". Existence is therefore
   `isinstance(body, dict)` and nothing else — neither the HTTP status nor the
   `code` field distinguishes a real package from a typo.
2. **A Huawei WAF fronts the site.** `GET /` sets HWWAFSESID + HWWAFSESTIME;
   those cookies plus a `Referer` header must ride on every subsequent request
   or repeated calls get challenged. Hence the seeded CookieJar in `_Session`.
3. **Responses are gzip** and urllib does not decompress automatically, so
   Content-Encoding is honoured by hand in `_Session.get_json`.

There is **no import statement anywhere in the API** — unlike `hmos_api_index`
rows, an OHPM package is consumed via `ohpm install <name>`. `install_cmd()`
builds that string; do not invent a `harmony_import` for OHPM rows.
"""

import argparse
import gzip
import json
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime
from http.cookiejar import CookieJar
from pathlib import Path


_BASE     = "https://ohpm.openharmony.cn"
_SEARCH   = "/ohpmweb/registry/oh-package/openapi/v1/search"
_DETAIL   = "/ohpmweb/registry/oh-package/openapi/v1/detail/"
_TECH_MAP = "/ohpm/tech-map"

# The server rejects pageSize=200 with HTTP 400; 100 is the usable maximum and
# covers the ~3499-package registry in 35 requests.
_PAGE_SIZE      = 100
_SORTED_TYPE    = "relevancy"
_TIMEOUT_SEC    = 20
_PAGE_DELAY_SEC = 0.4          # politeness between pages; also keeps the WAF calm
_PAGE_RETRIES   = 2            # per page, before the sweep parks for resume
_CACHE_SCHEMA   = "1.0"

_UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
       "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36")

# Search-row fields kept per package. `description` is search-ONLY — the detail
# endpoint does not return it — which is why the sweep harvests search rows and
# not details. Conversely repository/downloads/readme URLs are detail-only and
# are deliberately left to the Phase-2D shortlist rather than 3499 extra calls.
_PKG_FIELDS = (
    ("name",              "name"),
    ("org",               "org"),
    ("description",       "description"),
    ("keywords",          "keywords"),
    ("license",           "license"),
    ("popularity",        "popularity"),
    ("likes",             "likes"),
    ("points",            "points"),
    ("latest_version",    "latestVersion"),
    ("latest_publish_ms", "latestPublishTime"),
    ("author_name",       "authorName"),
    ("publisher_name",    "publisherName"),
    ("package_type",      "packageType"),
)


def cache_path_for(script_dir: Path) -> Path:
    """Mirror of play_meta.cache_path_for — `script_dir` is the `src/` root."""
    return script_dir / "data" / "reference" / "ohpm_registry_cache.json"


def install_cmd(package_name: str) -> str:
    """The OHPM equivalent of an import statement. The API provides no import."""
    return f"ohpm install {package_name}"


# ---------------------------------------------------------------------------
# transport
# ---------------------------------------------------------------------------

class _Session:
    """Cookie-jar-backed JSON GET helper. Never raises out of `get_json`.

    The jar is seeded from `GET /` on first use so the WAF's HWWAFSESID rides on
    every API request. `request_count` is exposed so a sweep can report exactly
    how many HTTP calls it made.
    """

    def __init__(self, timeout: int = _TIMEOUT_SEC):
        self._opener  = None
        self._timeout = timeout
        self.request_count = 0

    def _ensure_opener(self) -> bool:
        if self._opener is not None:
            return True
        jar    = CookieJar()
        opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(jar))
        opener.addheaders = [
            ("User-Agent",      _UA),
            ("Accept",          "application/json, text/plain, */*"),
            ("Accept-Encoding", "gzip"),
            ("Accept-Language", "en-US,en;q=0.9"),
            ("Referer",         _BASE + "/"),
        ]
        try:
            self.request_count += 1
            opener.open(_BASE + "/", timeout=self._timeout).read()
        except Exception:
            return False                      # DNS / TLS / proxy / timeout
        self._opener = opener      # the processor owns `jar` and keeps it alive
        return True

    def get_json(self, path: str):
        """GET `path`, return (payload, error) with error in:

            None       — payload is the decoded JSON object
            "offline"  — transport failed (DNS/TLS/timeout/proxy)
            "http"     — the server answered with a non-2xx status
            "parse"    — a 2xx body that is not JSON (a WAF challenge page)
        """
        if not self._ensure_opener():
            return None, "offline"
        try:
            self.request_count += 1
            resp = self._opener.open(_BASE + path, timeout=self._timeout)
            raw, headers = resp.read(), resp.headers
        except urllib.error.HTTPError:
            return None, "http"
        except Exception:
            return None, "offline"

        try:
            if (headers.get("Content-Encoding") or "").lower() == "gzip":
                raw = gzip.decompress(raw)
            return json.loads(raw.decode("utf-8", "replace")), None
        except Exception:
            # 2xx that will not parse means the WAF served a challenge/interstitial
            # rather than the API. Treat as a hard stop, not a per-item miss.
            return None, "parse"


def _body(payload):
    """OHPM wraps everything as {"code":200,"body":...}. Returns body or None."""
    if isinstance(payload, dict):
        return payload.get("body")
    return None


# ---------------------------------------------------------------------------
# cache
# ---------------------------------------------------------------------------

def _empty_cache() -> dict:
    return {
        "schema_version": _CACHE_SCHEMA,
        "fetched_at":     None,
        "sweep":          {"complete": False, "pages_done": 0,
                           "total_pages": None, "total": None,
                           "page_size": _PAGE_SIZE},
        "packages":       {},
        "tech_map":       {},
    }


def load_cache(path: Path) -> dict:
    """Read the registry cache; a missing/corrupt file degrades to an empty one."""
    try:
        raw = json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return _empty_cache()
    if not isinstance(raw, dict) or not isinstance(raw.get("packages"), dict):
        return _empty_cache()
    base = _empty_cache()
    base.update({k: raw.get(k, base[k]) for k in base})
    if not isinstance(base.get("sweep"), dict):
        base["sweep"] = _empty_cache()["sweep"]
    if not isinstance(base.get("tech_map"), dict):
        base["tech_map"] = {}
    return base


def _save_cache(path: Path, cache: dict) -> bool:
    """Write the cache. Returns False (with a printed warning) on any OS error."""
    cache["fetched_at"] = datetime.now().isoformat(timespec="seconds")
    try:
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        tmp = path.with_suffix(path.suffix + ".tmp")
        tmp.write_text(json.dumps(cache, ensure_ascii=False, indent=1),
                       encoding="utf-8")
        tmp.replace(path)                    # atomic-ish: a kill mid-write cannot
        return True                          # truncate an already-good cache
    except OSError as exc:
        print(f"[!] Could not write OHPM cache - {exc}")
        return False


def load_registry(cache_path: Path) -> dict:
    """Offline accessor for downstream phases: {"packages":…, "tech_map":…}."""
    return load_cache(cache_path)


# ---------------------------------------------------------------------------
# tech-map
# ---------------------------------------------------------------------------

def _flatten_tech_map(payload) -> dict:
    """{packageName: "L1 > L2 > L3"} from the nested category tree.

    Measured: 1062 packages, each appearing in exactly one category, so the
    mapping is 1:1 and a later category wins nothing — but last-write-wins is
    kept rather than asserted, since that is the API's guarantee to change.
    """
    data = payload.get("data") if isinstance(payload, dict) else None
    cats = data.get("categories") if isinstance(data, dict) else None
    if not isinstance(cats, list):
        return {}

    out = {}

    def walk(node, trail):
        if not isinstance(node, dict):
            return
        label = node.get("categoryNameEn") or node.get("categoryName") or "?"
        path  = trail + [str(label)]
        for pkg in (node.get("packageList") or []):
            if isinstance(pkg, dict) and pkg.get("packageName"):
                out[pkg["packageName"]] = " > ".join(path)
        for child in (node.get("childCategories") or []):
            walk(child, path)

    for top in cats:
        walk(top, [])
    return out


def fetch_tech_map(session: _Session = None) -> dict:
    """One request. Returns {} on any failure — callers treat it as optional."""
    session = session or _Session()
    payload, err = session.get_json(_TECH_MAP)
    if err:
        return {}
    return _flatten_tech_map(payload)


# ---------------------------------------------------------------------------
# existence check
# ---------------------------------------------------------------------------

def validate_package_exists(package_name: str, session: _Session = None,
                            cache: dict = None):
    """True / False / None(indeterminate — offline or WAF).

    A missing package answers HTTP 200 with body == "success" (a string), so the
    only reliable test is `isinstance(body, dict)`. Serving from `cache` first
    means a fully-swept cache can existence-check the whole mapping file with
    zero network traffic.
    """
    name = (package_name or "").strip()
    if not name:
        return False
    if cache and name in (cache.get("packages") or {}):
        return True

    session = session or _Session()
    payload, err = session.get_json(_DETAIL + urllib.parse.quote(name, safe=""))
    if err:
        return None
    return isinstance(_body(payload), dict)


# ---------------------------------------------------------------------------
# sweep
# ---------------------------------------------------------------------------

def _row_to_pkg(row: dict) -> dict:
    return {ours: row.get(theirs) for ours, theirs in _PKG_FIELDS}


def _search_path(page: int) -> str:
    params = urllib.parse.urlencode({
        "condition":  "",
        "pageNum":    page,
        "pageSize":   _PAGE_SIZE,
        "sortedType": _SORTED_TYPE,
        "isHomePage": "false",
    })
    return f"{_SEARCH}?{params}"


def sweep_registry(cache_path: Path, force: bool = False,
                   verbose: bool = True) -> dict:
    """Enumerate the whole OHPM registry into `cache_path`. Never raises.

    Resumable: `sweep.pages_done` records the highest *contiguous* page written
    and the cache is saved after every page, so a kill (or a dropped link) mid
    sweep resumes at the next page instead of restarting. Packages are keyed by
    name, so the re-fetch of a partially-written page is idempotent — which also
    absorbs the pagination drift caused by publishes landing during the sweep
    (empty-condition ordering is newest-first).

    Returns the cache dict whether the sweep completed, resumed, or stalled.
    """
    cache = _empty_cache() if force else load_cache(cache_path)

    # A cache paginated at a different _PAGE_SIZE cannot be resumed — its
    # pages_done counts pages of a different size — so start clean.
    if cache["sweep"].get("page_size") != _PAGE_SIZE:
        cache = _empty_cache()
    sweep = cache["sweep"]

    session = _Session()

    if not cache["tech_map"] or force:
        tech = fetch_tech_map(session)
        if tech:
            cache["tech_map"] = tech
            if verbose:
                print(f"[+] tech-map: {len(tech)} packages categorised")
        elif verbose:
            print("[!] tech-map unavailable - continuing without categories")

    if sweep.get("complete") and not force:
        if verbose:
            print(f"[=] Sweep already complete: {len(cache['packages'])} packages "
                  f"(delete the cache or pass --force to re-sweep)")
        _save_cache(cache_path, cache)
        return cache

    start = int(sweep.get("pages_done") or 0) + 1
    if verbose and start > 1:
        print(f"[=] Resuming sweep at page {start} "
              f"({len(cache['packages'])} packages already cached)")

    page = start
    while True:
        payload, err = None, None
        for attempt in range(_PAGE_RETRIES):
            payload, err = session.get_json(_search_path(page))
            if not err:
                break
            if err == "offline" and attempt + 1 < _PAGE_RETRIES:
                time.sleep(1.0 + attempt)     # brief backoff, then give up
        if err:
            reason = {"offline": "no connection",
                      "http":    "server rejected the request",
                      "parse":   "non-JSON response (WAF challenge?)"}[err]
            print(f"[!] Sweep stopped at page {page} - {reason}. "
                  f"Re-run to resume from here.")
            break

        body = _body(payload)
        if not isinstance(body, dict):
            print(f"[!] Sweep stopped at page {page} - unexpected response shape.")
            break

        rows = body.get("rows") or []
        for row in rows:
            if isinstance(row, dict) and row.get("name"):
                cache["packages"][row["name"]] = _row_to_pkg(row)

        sweep["pages_done"]  = page
        sweep["total"]       = body.get("total")
        sweep["total_pages"] = body.get("pages")
        total_pages = body.get("pages") or 0

        if not rows or (total_pages and page >= total_pages):
            sweep["complete"] = True
            _save_cache(cache_path, cache)
            if verbose:
                print(f"[+] Sweep complete: {len(cache['packages'])} packages "
                      f"in {page} pages, {session.request_count} HTTP requests")
            break

        _save_cache(cache_path, cache)
        if verbose:
            print(f"    page {page}/{total_pages} - "
                  f"{len(cache['packages'])}/{sweep['total']} packages")

        page += 1
        time.sleep(_PAGE_DELAY_SEC)

    if not sweep.get("complete"):
        _save_cache(cache_path, cache)
    return cache


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    _SRC = Path(__file__).resolve().parent.parent

    ap = argparse.ArgumentParser(description="OHPM registry sweep / cache builder")
    ap.add_argument("--force", action="store_true",
                    help="discard the existing cache and sweep from page 1")
    ap.add_argument("--check", metavar="PKG",
                    help="existence-check one package and exit")
    ap.add_argument("--cache", type=Path, default=cache_path_for(_SRC))
    args = ap.parse_args()

    if args.check:
        verdict = validate_package_exists(args.check, cache=load_cache(args.cache))
        print(f"{args.check}: "
              + {True: "EXISTS", False: "NOT FOUND", None: "INDETERMINATE"}[verdict])
    else:
        print(f"Sweeping OHPM registry into {args.cache} ...")
        result = sweep_registry(args.cache, force=args.force)
        print(f"Packages: {len(result['packages'])}  "
              f"Categorised: {len(result['tech_map'])}  "
              f"Complete: {result['sweep'].get('complete')}")
