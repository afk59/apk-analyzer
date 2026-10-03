"""HTTP surface: pickers, opening a result, listing what is on disk.

Two endpoints have consequences beyond returning JSON:

    POST /api/pick   opens a NATIVE dialog and returns a real absolute path.

    POST /api/open   asks the OS to open a file. GUARDED: the path must RESOLVE
                     to somewhere inside engine/result/. A naive prefix test
                     lets "result/../../../anything" through.

    POST /api/results/delete   removes a report from disk AND from the run
                     manifests, then rebuilds the index. Same guard as /open:
                     it must only ever touch the result tree.

Nothing here computes coverage, confidence or matching. That is the engine's
job, and duplicating it is how a report and the UI start disagreeing.
"""

import json
import os
import subprocess
import sys
from pathlib import Path

from fastapi import FastAPI, Header, HTTPException
from fastapi.responses import JSONResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from app import config
from app.services import dialogs
from app.services.jobs import runner

app = FastAPI(title="Migration Analyzer", docs_url=None, redoc_url=None)


# --------------------------------------------------------------- models
class PickRequest(BaseModel):
    kind: str = "file"


class OpenRequest(BaseModel):
    path: str


class RunRequest(BaseModel):
    input: str
    target: str = "hmos"
    # Batch runs default to skipping files that already have a report, so an
    # interrupted run costs only the file it was on. A single file picked by
    # hand is an explicit "analyse this now", so it is never skipped.
    skip_existing: bool | None = None
    # A folder holding EXE/DLL files only -- a PC program folder. "batch" gives
    # every binary its own report and the two batch workbooks; "combined" is
    # the engine's exe_folder mode, one merged report for the whole program.
    pc_mode: str = "batch"
    # Program folders keep binaries in subfolders (plugins/, x64/, runtimes/),
    # so a program-folder batch looks into them unless told not to.
    recursive: bool | None = None
    # .NET satellite assemblies: *.resources.dll, one per UI language, holding
    # translated strings and no code -- often hundreds per program. Left out
    # unless asked for.
    include_resources: bool = False


# --------------------------------------------------------------- health
@app.get("/api/health")
def health():
    return {
        "ok": True,
        "root": str(config.ROOT),
        "result_dir": str(config.RESULT_DIR),
        "mappings": (config.MAPPINGS_DIR / "mapping.json").exists(),
    }


# --------------------------------------------------------------- pick
@app.post("/api/pick")
def pick(req: PickRequest):
    if req.kind not in ("file", "folder"):
        raise HTTPException(400, "kind must be 'file' or 'folder'")
    path = dialogs.pick_folder() if req.kind == "folder" else dialogs.pick_file()
    if path is None:
        return {"path": None}          # cancelled: a normal outcome, not an error

    info = {"path": str(path), "name": path.name}
    if req.kind == "folder":
        info.update(folder_info(path))
    return info


def folder_info(path: Path) -> dict:
    """What a picked folder holds, before anything is analysed. For a program
    folder, every count its options can produce, so the number on screen is
    the number that will run."""
    files = [p for p in sorted(path.glob("*"))
             if p.suffix.lower() in config.SUPPORTED_INPUTS]
    bundles = [p for p in sorted(path.glob("*"))
               if p.suffix.lower() in config.BUNDLE_INPUTS]
    info = {
        "file_count": len(files),
        "files": [p.name for p in files],
        # APKM/XAPK are ZIPs of split APKs with no dex of their own; the engine
        # refuses them, and the UI should not pretend they were included.
        "skipped_bundles": [p.name for p in bundles],
    }
    if _is_program_folder(path):
        top = _binaries(path, recursive=False, include_resources=True)
        deep = _binaries(path, recursive=True, include_resources=True)
        info["program"] = {
            "top": sum(1 for p in top if not _is_resources(p)),
            "top_resources": sum(1 for p in top if _is_resources(p)),
            "all": sum(1 for p in deep if not _is_resources(p)),
            "all_resources": sum(1 for p in deep if _is_resources(p)),
        }
    return info


# --------------------------------------------------------------- open
@app.post("/api/open")
def open_path(req: OpenRequest):
    path = Path(req.path)
    if not path.is_absolute():
        path = (config.ROOT / req.path).resolve()
    if not config.is_inside_result(path):
        raise HTTPException(403, "Only files inside the result folder can be opened.")
    if not path.exists():
        raise HTTPException(404, f"Not found: {path.name}")
    try:
        if sys.platform == "win32":
            os.startfile(str(path))                                   # noqa: S606
        elif sys.platform == "darwin":
            subprocess.Popen(["open", str(path)])
        else:
            subprocess.Popen(["xdg-open", str(path)])
    except Exception as exc:
        raise HTTPException(500, f"Could not open the file: {exc}")
    return JSONResponse({"opened": str(path)})


# --------------------------------------------------------------- runs
_PE = (".exe", ".dll")


def _is_resources(p: Path) -> bool:
    return p.name.lower().endswith(".resources.dll")


def _binaries(folder: Path, recursive: bool, include_resources: bool):
    """Every EXE/DLL under `folder`, in a stable order: top level first, then
    each subfolder, so the run walks a program the way its tree reads."""
    found = folder.rglob("*") if recursive else folder.glob("*")
    out = [p for p in found if p.is_file() and p.suffix.lower() in _PE
           and (include_resources or not _is_resources(p))]
    return sorted(out, key=lambda p: (len(p.relative_to(folder).parts),
                                      p.relative_to(folder).as_posix().lower()))


def _is_program_folder(folder: Path) -> bool:
    """EXE/DLL at the top level and no APK/IPA beside them. A mixed folder is a
    corpus of unrelated inputs and keeps the flat batch it always had."""
    top = [p.suffix.lower() for p in folder.glob("*") if p.is_file()]
    return any(s in _PE for s in top) and not any(s in (".apk", ".ipa") for s in top)


def _inputs_for(target_path: Path, pc_mode: str = "batch", recursive=None,
                include_resources: bool = False):
    """(files to analyse, human label, root). A folder expands; a file is itself.

    `root` is the folder the labels are relative to -- set only when a run can
    contain files from subfolders.
    """
    if target_path.is_dir():
        if _is_program_folder(target_path):
            if pc_mode == "combined":
                # The engine's exe_folder mode: one merged report, as the CLI.
                return [target_path], f"{target_path.name} (folder)", None
            # Each binary its own report, through subfolders by default --
            # that is where plugins live.
            deep = True if recursive is None else bool(recursive)
            files = _binaries(target_path, deep, include_resources)
            return files, f"{target_path.name} ({len(files)} files)", target_path
        files = [p for p in sorted(target_path.glob("*"))
                 if p.suffix.lower() in config.SUPPORTED_INPUTS]
        return files, f"{target_path.name} ({len(files)} files)", None
    return [target_path], target_path.name, None


@app.post("/api/runs")
def start_run(req: RunRequest):
    path = Path(req.input)
    if not path.exists():
        raise HTTPException(404, f"Not found: {req.input}")
    if req.target not in ("hmos", "hms"):
        raise HTTPException(400, "target must be 'hmos' or 'hms'")
    if req.pc_mode not in ("batch", "combined"):
        raise HTTPException(400, "pc_mode must be 'batch' or 'combined'")

    files, label, root = _inputs_for(path, req.pc_mode, req.recursive,
                                     req.include_resources)
    if not files:
        raise HTTPException(400, "Nothing analysable in that folder.")

    skip = req.skip_existing
    if skip is None:
        skip = path.is_dir() and len(files) > 1
    run_id = runner.submit(files, req.target, skip_existing=skip, input_label=label,
                           root=root)
    return {"run_id": run_id, "file_count": len(files), "input": label,
            "skip_existing": skip}


class DownloadRequest(BaseModel):
    packages: str                 # newline or comma separated
    target: str = "hmos"


@app.post("/api/downloads")
def start_download(req: DownloadRequest):
    """Fetch one or more packages by name, then analyse them in the same run.

    One run, not a download followed by an analysis, so the UI shows a single
    progress stream and a failed download is isolated like a corrupt file.
    """
    names = [p.strip() for p in req.packages.replace(",", "\n").replace(";", "\n").splitlines()]
    # Order kept, repeats dropped: the same package twice would download twice
    # into the same file and analyse it twice into the same report.
    names = list(dict.fromkeys(n for n in names if n))
    if not names:
        raise HTTPException(400, "Give at least one package name.")
    # Rejected here, by Android's own naming rule, so nothing that could be a
    # path ever reaches the downloader, which builds a file name from it.
    from app.services.downloader import is_package_name
    bad = [n for n in names if not is_package_name(n)]
    if bad:
        raise HTTPException(400, f"Not package names: {', '.join(bad[:3])}")
    if req.target not in ("hmos", "hms"):
        raise HTTPException(400, "target must be 'hmos' or 'hms'")

    label = names[0] if len(names) == 1 else f"{len(names)} packages"
    run_id = runner.submit([], req.target, skip_existing=False,
                           input_label=label, packages=names)
    return {"run_id": run_id, "file_count": len(names), "input": label,
            "skip_existing": False, "packages": names}


# Declared BEFORE /api/runs/{run_id}, which would otherwise claim "latest" and
# answer 422 for it not being an integer.
@app.get("/api/runs/latest")
def latest_run():
    """The run a reloaded page re-attaches to (see JobRunner.latest), or null.
    Run state lives in this process, not in the page."""
    run = runner.latest()
    return {"run": run.snapshot() if run else None}


@app.get("/api/runs/{run_id}")
def run_state(run_id: int):
    run = runner.get(run_id)
    if run is None:
        raise HTTPException(404, "No such run")
    return run.snapshot()


@app.post("/api/runs/{run_id}/cancel")
def cancel_run(run_id: int):
    if not runner.cancel(run_id):
        raise HTTPException(409, "That run is not running.")
    return {"cancelled": run_id}


@app.get("/api/runs/{run_id}/events")
def run_events(run_id: int, cursor: int = 0,
               last_event_id: str | None = Header(None, alias="Last-Event-ID")):
    """SSE. Forwards worker events verbatim, plus queue-level ones.

    A keep-alive goes out whenever the wait lapses: a single file can take
    minutes, and a silent connection that long is one an intermediary may drop.

    Every event carries its position as its SSE id. EventSource reconnects to
    the same URL sending the last id it saw; without ids a reconnect replays the
    run from the start and the UI counts every finished file twice.
    """
    if runner.get(run_id) is None:
        raise HTTPException(404, "No such run")
    if last_event_id is not None and last_event_id.strip().isdigit():
        cursor = max(cursor, int(last_event_id) + 1)

    def stream():
        pos = cursor
        while True:
            start = pos
            events, pos, finished = runner.events(run_id, pos, timeout=15.0)
            if events is None:
                break
            for i, ev in enumerate(events):
                payload = json.dumps(ev, ensure_ascii=False, default=str)
                yield f"id: {start + i}\ndata: {payload}\n\n"
            if finished and not events:
                yield "event: end\ndata: {}\n\n"
                break
            if not events:
                yield ": keep-alive\n\n"

    return StreamingResponse(stream(), media_type="text/event-stream", headers={
        "Cache-Control": "no-cache",
        "X-Accel-Buffering": "no",
    })


# --------------------------------------------------------------- library
@app.get("/api/results")
def results():
    """The library: runs newest first, each with its apps.

    Served from the SQLite index, which is only ever a copy of what is on disk,
    so /api/rescan can rebuild it from nothing. It self-heals on an empty
    database, which is what happens on a first run.
    """
    from app.store import index as store_index
    data = store_index.library()
    if not data["runs"] and any(config.RESULT_DIR.glob("*_report.html")):
        store_index.rescan()
        data = store_index.library()
    return data


class DeleteRequest(BaseModel):
    # One of the two. A report path for an analysed app (relative to the repo
    # root, as /api/results gives it); a manifest name plus a source file for a
    # failed row, which has no report to point at.
    report: str | None = None
    manifest: str | None = None
    source_file: str | None = None


@app.post("/api/results/delete")
def delete_result(req: DeleteRequest):
    """Remove one result from the library: its files on disk, and its entry in
    every run manifest that lists it, then rebuild the index.

    The manifests are edited, not just the database: the index is rebuilt from
    them (docs/decisions/0002). Keyed by path, not row id: ids are reassigned
    on every rescan.
    """
    from app.store import index as store_index
    if req.report:
        path = Path(req.report)
        if not path.is_absolute():
            path = (config.ROOT / req.report).resolve()
        if not config.is_inside_result(path) or not path.name.endswith("_report.html"):
            raise HTTPException(403, "Only reports inside the result folder can be deleted.")
        if _report_in_use(path):
            raise HTTPException(409, "That report is being written by the run in progress.")
        out = store_index.delete_report(path)
        if not out["reports"]:
            raise HTTPException(404, "No such report.")
        return out
    if req.manifest and req.source_file:
        out = store_index.delete_failure(req.manifest, req.source_file)
        if out is None:
            raise HTTPException(404, "No such failed entry.")
        return out
    raise HTTPException(400, "Give a report, or a manifest and a source file.")


class DeleteManyRequest(BaseModel):
    items: list[DeleteRequest]


@app.post("/api/results/delete-many")
def delete_results(req: DeleteManyRequest):
    """The selection on the Results page, deleted in one pass and one rescan.

    Every report goes through the SAME guard as the single delete; one that
    fails it is reported back and skipped without aborting the rest.
    """
    from app.store import index as store_index
    if not req.items:
        raise HTTPException(400, "Nothing selected.")
    reports, failures, refused = [], [], []
    for item in req.items:
        if item.report:
            path = Path(item.report)
            if not path.is_absolute():
                path = (config.ROOT / item.report).resolve()
            if not config.is_inside_result(path) or not path.name.endswith("_report.html"):
                refused.append({"item": item.report, "reason": "outside the result folder"})
            elif _report_in_use(path):
                refused.append({"item": item.report, "reason": "being written by the run in progress"})
            else:
                reports.append(path)
        elif item.manifest and item.source_file:
            failures.append((item.manifest, item.source_file))
        else:
            refused.append({"item": None, "reason": "neither a report nor a manifest entry"})
    out = store_index.delete_many(reports, failures)
    out["refused"] = refused
    return out


def _report_in_use(report: Path) -> bool:
    """True if any running run is analysing the input that writes `report`.
    Every running run, not just the latest: two can overlap."""
    for run in runner.running():
        current = run.current
        if not current:
            continue
        for p in list(run.paths):
            if run.label(p) == current:
                if runner._report_for(p, run.target, run.stems.get(str(p))).resolve() \
                        == report.resolve():
                    return True
                break
    return False


@app.post("/api/rescan")
def rescan():
    from app.store import index as store_index
    return store_index.rescan()


# --------------------------------------------------------------- static
# Mounted last: a route defined above always wins over a file with the same path.
app.mount("/", StaticFiles(directory=str(config.WEB_DIR), html=True), name="web")
