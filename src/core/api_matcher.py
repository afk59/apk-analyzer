
import re
import json
from pathlib import Path
from typing import Optional

_INDEX_PATH = Path(__file__).parent.parent / "data" / "reference" / "hmos_api_index.json"
_VER_RE     = re.compile(r'\d+\+?\s*$')

_index: dict = {}
_loaded = False


def _norm(s: str) -> str:
    return _VER_RE.sub('', s).strip().lower()


def _simple(name: str) -> str:
    return _norm(name.split('.')[-1])


def _load() -> None:
    global _index, _loaded
    if _loaded:
        return
    _loaded = True
    if not _INDEX_PATH.exists():
        return
    _index = json.loads(_INDEX_PATH.read_text(encoding="utf-8"))


def _build_match(android_method: str, entry: dict) -> dict:
    return {
        "android_method":   android_method,
        "import_statement": entry.get("import_statement"),
        "doc_url":          entry.get("doc_url"),
        "kit":              entry.get("kit"),
        "match_type":       "exact",
        "score":            1.0,
    }


def match_method(android_method: str) -> Optional[dict]:
    _load()
    if not _index:
        return None
    skey = _simple(android_method)
    if skey in _index:
        return _build_match(android_method, _index[skey])
    return None


def match_methods(android_methods: list) -> list:
    _load()
    if not _index:
        return []
    results = []
    seen: set = set()
    for method in android_methods:
        skey = _simple(method)
        if skey in seen:
            continue
        seen.add(skey)
        hit = match_method(method)
        if hit:
            results.append(hit)
    return results
