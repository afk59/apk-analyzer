"""HTTP surface: pickers, opening a result, listing what is on disk.

Two endpoints have consequences beyond returning JSON:

    POST /api/pick   opens a NATIVE dialog and returns a real absolute path.

    POST /api/open   asks the OS to open a file. GUARDED: the path must RESOLVE
                     to somewhere inside engine/result/. A naive prefix test
                     lets "result/../../../anything" through.

Nothing here computes coverage, confidence or matching. That is the engine's
job, and duplicating it is how a report and the UI start disagreeing.
"""

import json
import os
import subprocess
import sys
from pathlib import Path

from fastapi import FastAPI, HTTPException
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
        # A folder with no supported files should be a message, not a no-op.
        files = [p for p in sorted(path.glob("*"))
                 if p.suffix.lower() in config.SUPPORTED_INPUTS]
        bundles = [p for p in sorted(path.glob("*"))
                   if p.suffix.lower() in config.BUNDLE_INPUTS]
        info["file_count"] = len(files)
        info["files"] = [p.name for p in files]
        # APKM/XAPK are ZIPs of split APKs with no dex of their own; the engine
        # refuses them, and the UI should not pretend they were included.
        info["skipped_bundles"] = [p.name for p in bundles]
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
def _inputs_for(target_path: Path):
    """(files to analyse, human label). A folder expands; a file is itself."""
    if target_path.is_dir():
        # A directory of .exe/.dll is one logical application (exe_folder mode),
        # not a batch of unrelated binaries. That distinction is the engine's.
        binaries = [p for p in sorted(target_path.glob("*"))
                    if p.suffix.lower() in (".exe", ".dll")]
        others = [p for p in sorted(target_path.glob("*"))
                  if p.suffix.lower() in (".apk", ".ipa")]
        if binaries and not others:
            return [target_path], f"{target_path.name} (folder)"
        return ([p for p in sorted(target_path.glob("*"))
                 if p.suffix.lower() in config.SUPPORTED_INPUTS],
                f"{target_path.name} ({len(others) + len(binaries)} files)")
    return [target_path], target_path.name


@app.post("/api/runs")
def start_run(req: RunRequest):
    path = Path(req.input)
    if not path.exists():
        raise HTTPException(404, f"Not found: {req.input}")
    if req.target not in ("hmos", "hms"):
        raise HTTPException(400, "target must be 'hmos' or 'hms'")

    files, label = _inputs_for(path)
    if not files:
        raise HTTPException(400, "Nothing analysable in that folder.")

    skip = req.skip_existing
    if skip is None:
        skip = path.is_dir() and len(files) > 1
    run_id = runner.submit(files, req.target, skip_existing=skip, input_label=label)
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
    names = [p.strip() for p in req.packages.replace(",", "\n").splitlines()]
    names = [n for n in names if n]
    if not names:
        raise HTTPException(400, "Give at least one package name.")
    # A package name has no separators and no spaces. Rejecting them here keeps
    # a path from reaching the downloader, which builds a filename from it.
    bad = [n for n in names if "/" in n or "\\" in n or " " in n]
    if bad:
        raise HTTPException(400, f"Not package names: {', '.join(bad[:3])}")
    if req.target not in ("hmos", "hms"):
        raise HTTPException(400, "target must be 'hmos' or 'hms'")

    label = names[0] if len(names) == 1 else f"{len(names)} packages"
    run_id = runner.submit([], req.target, skip_existing=False,
                           input_label=label, packages=names)
    return {"run_id": run_id, "file_count": len(names), "input": label,
            "skip_existing": False}


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
def run_events(run_id: int, cursor: int = 0):
    """SSE. Forwards worker events verbatim, plus queue-level ones.

    A keep-alive goes out whenever the wait lapses: a single file can take
    minutes, and a silent connection that long is one an intermediary may drop.
    """
    if runner.get(run_id) is None:
        raise HTTPException(404, "No such run")

    def stream():
        pos = cursor
        while True:
            events, pos, finished = runner.events(run_id, pos, timeout=15.0)
            if events is None:
                break
            for ev in events:
                payload = json.dumps(ev, ensure_ascii=False, default=str)
                yield f"data: {payload}\n\n"
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


@app.post("/api/rescan")
def rescan():
    from app.store import index as store_index
    return store_index.rescan()


# --------------------------------------------------------------- static
# Mounted last: a route defined above always wins over a file with the same path.
app.mount("/", StaticFiles(directory=str(config.WEB_DIR), html=True), name="web")
