"""Building and reading the SQLite index. See docs/decisions/0002.

THE INVARIANT: delete analyzer.db, rescan, and the library is identical.

That is only true if everything the index holds also exists on disk, so a
finished run writes a small manifest next to its outputs:

    engine/result/.runs/run-<started>-<id>.json

The manifest is the durable record; the database is a queryable copy of it.
Reports that belong to no manifest -- anything produced by the v1 CLI, or by a
run whose manifest was deleted -- are still listed, under a synthetic
"Unfiled" run, so nothing on disk is invisible in the UI.
"""

import json
import re
import sys
from datetime import datetime
from pathlib import Path

from app import config
from app.store.db import connect, rel

def runs_dir() -> Path:
    """Resolved on each call, so a redirected RESULT_DIR is honoured. Binding it
    at import time made the whole module untestable in isolation."""
    return config.RESULT_DIR / ".runs"


# ------------------------------------------------------------------ writing
def write_manifest(snapshot: dict) -> Path:
    d = runs_dir()
    d.mkdir(parents=True, exist_ok=True)
    stamp = (snapshot.get("started_at") or datetime.now().isoformat()).replace(":", "-")
    path = d / f"run-{stamp}-{snapshot.get('id', 0)}.json"
    path.write_text(json.dumps(snapshot, ensure_ascii=False, default=str, indent=1),
                    encoding="utf-8")
    return path


# ------------------------------------------------------------------ reading
def _locate(path) -> Path:
    """Where a report named in a manifest is NOW.

    Manifests hold the absolute path the worker wrote, and every report lives
    directly in RESULT_DIR. So when the result folder has been moved or copied,
    the same file name in the current RESULT_DIR is that report. Trusting the
    stored path instead listed every app twice after a move -- once as a dead
    link to the old folder, once under "Unfiled" -- and a delete in a copy came
    back on the next rescan (audit 2026-10-03, BUG-05).
    """
    p = Path(path)
    here = config.RESULT_DIR / p.name
    return here if here.exists() else p


def _agent_for(report: Path):
    cand = config.AGENT_DIR / report.name.replace("_report.html", "_agent.json")
    return cand if cand.exists() else None


def _from_agent(report: Path) -> dict:
    """What a report can tell us about itself, with no manifest.

    Every field here is read from the agent JSON the engine wrote, so an app
    discovered this way is described by the engine's own output rather than by
    anything this module inferred.
    """
    out = {
        "source_file": report.stem.replace("_report", ""),
        "app_name": None, "package_name": None, "version": None,
        "framework": None, "engine_name": None, "packer": None,
        "kit_count": None, "unmapped_count": None, "ohpm_count": None,
        "permission_count": None, "coverage_pct": None, "coverage_status": None,
        "analysis_time_sec": None, "status": "done", "error": None,
    }
    agent = _agent_for(report)
    if not agent:
        return out
    try:
        doc = json.loads(agent.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return out
    meta = doc.get("app_metadata") or {}
    fw = doc.get("framework") or {}
    pct, status = _coverage_from_report(report, fw)
    out["coverage_pct"], out["coverage_status"] = pct, status
    out.update({
        "app_name": meta.get("app_name") or meta.get("folder_name") or meta.get("file_name"),
        "package_name": meta.get("package_name") or meta.get("bundle_id"),
        "version": meta.get("version_name") or meta.get("version"),
        "framework": fw.get("framework"),
        "engine_name": fw.get("engine"),
        "packer": (fw.get("detail") or {}).get("packer"),
        "kit_count": len(doc.get("kit_list") or []),
        "ohpm_count": len(doc.get("ohpm_matches") or []),
    })
    return out


# total_ohpm_ns is optional: reports written before 2026-09-24 lack it.
_NS_RE = re.compile(rb'"total_detected_ns":\s*(\d+).{0,40}?"total_3p_ns":\s*(\d+)'
                    rb'(?:,\s*"total_ohpm_ns":\s*(\d+))?', re.S)


def _coverage_from_report(report: Path, framework):
    """Recover coverage for a report that has no run manifest.

    The agent JSON does not carry the two namespace counts, but the report
    embeds them in its own report_data block (the renderer puts them there for
    the in-browser export). So they are read back from there and handed to the
    ENGINE's coverage_status() -- the same function the stat card and the batch
    workbook call. Recomputing the percentage here instead would create the
    fourth implementation that v1 spent a commit eliminating.

    Without this, deleting the database would silently lose the coverage column
    for every v1-CLI report, and the "rescan rebuilds everything" invariant in
    docs/decisions/0002 would quietly be false.
    """
    try:
        blob = report.read_bytes()
    except OSError:
        return None, None
    m = _NS_RE.search(blob)
    if not m:
        return None, None
    payload = {
        "total_detected_ns": int(m.group(1)),
        "total_3p_ns": int(m.group(2)),
        "total_ohpm_ns": int(m.group(3) or 0),
        "framework": framework or {},
    }
    try:
        if str(config.ENGINE_DIR) not in sys.path:
            sys.path.insert(0, str(config.ENGINE_DIR))
        from core.renderer import coverage_status
    except Exception:
        return None, None
    return coverage_status(payload)


def _artifacts_for(report: Path):
    out = [("html", report)]
    xlsx = report.with_suffix(".xlsx")
    if xlsx.exists():
        out.append(("xlsx", xlsx))
    agent = _agent_for(report)
    if agent:
        out.append(("agent_json", agent))
    return out


def rescan() -> dict:
    """Rebuild the whole index from disk. Safe to run at any time."""
    conn = connect()
    try:
        conn.execute("DELETE FROM downloads")
        conn.execute("DELETE FROM artifacts")
        conn.execute("DELETE FROM apps")
        conn.execute("DELETE FROM runs")

        claimed = set()
        rd = runs_dir()
        manifests = sorted(rd.glob("run-*.json")) if rd.exists() else []
        for mpath in manifests:
            try:
                snap = json.loads(mpath.read_text(encoding="utf-8"))
            except (OSError, ValueError):
                continue
            skipped = sum(1 for r in snap.get("results", []) if r.get("skipped"))
            cur = conn.execute(
                "INSERT INTO runs (started_at, finished_at, mode, target, status,"
                " input_path, file_count, skipped_count, manifest)"
                " VALUES (?,?,?,?,?,?,?,?,?)",
                (snap.get("started_at"), snap.get("finished_at"),
                 "batch" if (snap.get("file_count") or 0) > 1 else "single",
                 snap.get("target", "hmos"), snap.get("status", "done"),
                 snap.get("input", ""), snap.get("file_count", 0), skipped,
                 mpath.name))
            run_id = cur.lastrowid

            for row in snap.get("results", []):
                report = _locate(row["report"]) if row.get("report") else None
                if row.get("skipped") or not report:
                    # A skipped file was analysed by an EARLIER run and belongs
                    # to that run's manifest. Listing it twice would double-count
                    # the library.
                    continue
                _insert_app(conn, run_id, row, report)
                claimed.add(report.resolve())
            for fail in snap.get("failures", []):
                conn.execute(
                    "INSERT INTO apps (run_id, source_file, status, error)"
                    " VALUES (?,?,?,?)",
                    (run_id, fail.get("source_file", "?"), "failed", fail.get("error")))
            for dl in snap.get("downloads", []):
                conn.execute(
                    "INSERT INTO downloads (run_id, package_name, source, state,"
                    " file_path, version, size, requested_at, error, note)"
                    " VALUES (?,?,?,?,?,?,?,?,?,?)",
                    (run_id, dl.get("package_name", "?"), dl.get("source"),
                     dl.get("state", "failed"),
                     rel(Path(dl["file_path"])) if dl.get("file_path") else None,
                     dl.get("version"), dl.get("size"),
                     dl.get("requested_at") or snap.get("started_at") or "",
                     dl.get("error"), dl.get("note")))

        # Anything on disk that no manifest claims -- v1 CLI output, or a run
        # whose manifest was removed. It is real work and must not vanish from
        # the UI just because its bookkeeping is missing.
        orphans = [p for p in sorted(config.RESULT_DIR.glob("*_report.html"))
                   if p.resolve() not in claimed]
        if orphans:
            # A real timestamp, taken from the newest report it contains, so the
            # pseudo-run sorts into the library where those results actually
            # belong -- and so it is still derived from disk, not invented.
            newest = max(p.stat().st_mtime for p in orphans)
            stamp = datetime.fromtimestamp(newest).isoformat(timespec="seconds")
            cur = conn.execute(
                "INSERT INTO runs (started_at, finished_at, mode, target, status,"
                " input_path, file_count, skipped_count) VALUES (?,?,?,?,?,?,?,?)",
                (stamp, stamp, "single", "hmos", "done", "Unfiled", len(orphans), 0))
            run_id = cur.lastrowid
            for report in orphans:
                _insert_app(conn, run_id, _from_agent(report), report)

        conn.commit()
        counts = {
            "runs": conn.execute("SELECT COUNT(*) FROM runs").fetchone()[0],
            "apps": conn.execute("SELECT COUNT(*) FROM apps").fetchone()[0],
            "artifacts": conn.execute("SELECT COUNT(*) FROM artifacts").fetchone()[0],
            "downloads": conn.execute("SELECT COUNT(*) FROM downloads").fetchone()[0],
            "manifests": len(manifests),
            "orphans": len(orphans),
        }
        return counts
    finally:
        conn.close()


def _insert_app(conn, run_id: int, row: dict, report: Path):
    merged = {**_from_agent(report), **{k: v for k, v in row.items() if v is not None}}
    cur = conn.execute(
        "INSERT INTO apps (run_id, source_file, package_name, app_name, version,"
        " framework, engine_name, packer, coverage_pct, coverage_status,"
        " kit_count, unmapped_count, ohpm_count, permission_count,"
        " analysis_time_sec, status, error)"
        " VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
        (run_id, merged.get("source_file") or report.name,
         merged.get("package_name"), merged.get("app_name"), merged.get("version"),
         merged.get("framework"), merged.get("engine_name"), merged.get("packer"),
         merged.get("coverage_pct"), merged.get("coverage_status"),
         merged.get("kit_count"), merged.get("unmapped_count"),
         merged.get("ohpm_count"), merged.get("permission_count"),
         merged.get("analysis_time_sec"), merged.get("status", "done"),
         merged.get("error")))
    app_id = cur.lastrowid
    for kind, path in _artifacts_for(report):
        conn.execute("INSERT INTO artifacts (app_id, kind, path) VALUES (?,?,?)",
                     (app_id, kind, rel(path)))
    return app_id


# ------------------------------------------------------------------ deleting
_REPORT_NAME = re.compile(r"^(?P<stem>.+)_(?P<mode>apk|exe_folder|exe|ipa)_"
                          r"(?P<target>hmos|hms)_report\.html$")


def _files_of(report: Path) -> list:
    """Every file on disk that belongs to one report: the report, its
    workbook, its agent JSON, and the side-car the batch workbooks read."""
    out = [report, report.with_suffix(".xlsx"),
           config.AGENT_DIR / report.name.replace("_report.html", "_agent.json")]
    m = _REPORT_NAME.match(report.name)
    if m:
        from app.worker import sidecar_name
        out.append(config.RESULT_DIR / ".sidecars"
                   / sidecar_name(m["stem"], m["mode"], m["target"]))
    return out


def _same(a, b: Path) -> bool:
    try:
        return Path(a).resolve() == b.resolve()
    except (OSError, ValueError):
        return False


def _edit_manifests(keep) -> int:
    """Rewrite every manifest through `keep(kind, entry, manifest) -> bool`,
    kind being "result" or "failure" and manifest the file's name. A manifest left with nothing to show -- no analysed
    app and no failure, only files it skipped -- is removed, since its run
    would otherwise sit in the library as an empty group. Returns how many
    manifests changed."""
    changed = 0
    rd = runs_dir()
    for mpath in sorted(rd.glob("run-*.json")) if rd.exists() else []:
        try:
            snap = json.loads(mpath.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            continue
        results = [r for r in snap.get("results", []) if keep("result", r, mpath.name)]
        failures = [f for f in snap.get("failures", []) if keep("failure", f, mpath.name)]
        if (len(results) == len(snap.get("results", []))
                and len(failures) == len(snap.get("failures", []))):
            continue
        changed += 1
        if not failures and not any(not r.get("skipped") for r in results):
            mpath.unlink(missing_ok=True)
            continue
        snap["results"], snap["failures"] = results, failures
        mpath.write_text(json.dumps(snap, ensure_ascii=False, default=str, indent=1),
                         encoding="utf-8")
    return changed


def delete_report(report: Path) -> dict:
    """Delete one analysed app: its files, its manifest entries, its index row.

    One report file can be listed by several runs -- analysing the same input
    again overwrites the same report -- so EVERY manifest that points at it is
    edited. The batch workbooks are left alone: they are a record of the batch
    they summarise, not a view of the library.
    """
    return delete_many([report], [])


def delete_failure(manifest: str, source_file: str):
    """Drop one failed entry from one run. None if there is no such entry."""
    if not _failure_exists(manifest, source_file):
        return None
    return delete_many([], [(manifest, source_file)])


def _failure_exists(manifest: str, source_file: str) -> bool:
    if "/" in manifest or "\\" in manifest or not _MANIFEST_NAME.match(manifest):
        return False
    try:
        snap = json.loads((runs_dir() / manifest).read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return False
    return any(f.get("source_file") == source_file for f in snap.get("failures", []))


def delete_many(reports, failures) -> dict:
    """Delete several results in one pass: every report's files, every listed
    failure, one sweep over the manifests and ONE rescan.

    Deleting a selection one item at a time would rescan the whole result
    tree once per item -- a 300-row selection of a program-folder batch would
    rebuild the index 300 times. `reports` are paths already checked by the
    caller; `failures` are (manifest name, source file) pairs, and a pair
    naming a manifest that does not look like one is ignored.
    """
    targets = {Path(r).resolve() for r in reports}
    removed = []
    # Reports that actually had something to delete -- a file, or an entry in
    # some manifest. Counting the request instead told the UI "Deleted: 1" for
    # a report that never existed (audit 2026-10-03, BUG-13).
    hit = set()
    for report in sorted(targets):
        for f in _files_of(report):
            try:
                if f.exists():
                    f.unlink()
                    removed.append(f.name)
                    hit.add(report)
            except OSError:
                pass
    keys = {(m, sf) for m, sf in failures
            if "/" not in m and "\\" not in m and _MANIFEST_NAME.match(m)}

    def keep(kind, entry, manifest):
        if kind == "result":
            rep = entry.get("report")
            # By the stored path, or by the same name in the current result
            # folder (see _locate): the file is already gone at this point, so
            # _locate itself can no longer tell a moved folder's entry apart.
            if not rep:
                return True
            for cand in (_resolved(rep), _resolved(config.RESULT_DIR / Path(rep).name)):
                if cand in targets:
                    hit.add(cand)
                    return False
            return True
        return (manifest, entry.get("source_file")) not in keys

    changed = _edit_manifests(keep)
    return {"deleted": removed, "reports": len(hit), "failures": len(keys),
            "manifests_changed": changed, **rescan()}


def _resolved(path):
    try:
        return Path(path).resolve()
    except (OSError, ValueError):
        return None


_MANIFEST_NAME = re.compile(r"^run-[\w.\-]+\.json$")


def library() -> dict:
    """Runs newest first, each with its apps and their artifact paths."""
    conn = connect()
    try:
        runs = []
        for r in conn.execute(
                "SELECT * FROM runs ORDER BY COALESCE(started_at,'') DESC, id DESC"):
            run = dict(r)
            apps = []
            for a in conn.execute("SELECT * FROM apps WHERE run_id=? ORDER BY id", (r["id"],)):
                app = dict(a)
                app["artifacts"] = {
                    x["kind"]: x["path"] for x in
                    conn.execute("SELECT kind, path FROM artifacts WHERE app_id=?", (a["id"],))
                }
                apps.append(app)
            run["apps"] = apps
            run["downloads"] = [
                {k: d[k] for k in d.keys() if k not in ("id", "run_id")} for d in
                conn.execute("SELECT * FROM downloads WHERE run_id=? ORDER BY id", (r["id"],))
            ]
            # The two batch workbooks are per-result-directory, not per-app, so
            # they hang off the run rather than off any one row.
            runs.append(run)
        workbooks = {}
        for name in ("batch_summary.xlsx", "batch_unmapped.xlsx"):
            p = config.RESULT_DIR / name
            if p.exists():
                workbooks[name] = rel(p)
        return {"runs": runs, "workbooks": workbooks}
    finally:
        conn.close()
