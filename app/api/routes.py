"""HTTP surface. M1: pickers, opening a result, listing what is on disk.

Two endpoints here have consequences beyond returning JSON:

    POST /api/pick   opens a NATIVE dialog and returns a real absolute path.
                     A browser cannot produce one -- see docs/decisions/0001.

    POST /api/open   asks the OS to open a file. GUARDED: the path must resolve
                     to somewhere inside engine/result/. The window will open
                     whatever it is handed, so the refusal has to live here, and
                     the path must be RESOLVED before comparing -- a naive
                     prefix test lets "result/../../../anything" through.

Nothing in this module computes coverage, confidence or matching. That is the
engine's job and duplicating it is how a report and the UI start disagreeing.
"""

import json
import os
import subprocess
import sys
from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from app import config
from app.services import dialogs

app = FastAPI(title="Migration Analyzer", docs_url=None, redoc_url=None)


# --------------------------------------------------------------- models
class PickRequest(BaseModel):
    kind: str = "file"


class OpenRequest(BaseModel):
    path: str


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
        # Say what is in there before anything is analysed. A folder with no
        # supported files should be a message in the UI, not a silent no-op.
        files = [p for p in sorted(path.glob("*"))
                 if p.suffix.lower() in config.SUPPORTED_INPUTS]
        bundles = [p for p in sorted(path.glob("*"))
                   if p.suffix.lower() in config.BUNDLE_INPUTS]
        info["file_count"] = len(files)
        info["files"] = [p.name for p in files]
        # APKM/XAPK are ZIPs of split APKs with no dex of their own. The engine
        # refuses them honestly; the UI should not pretend they were included.
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


# --------------------------------------------------------------- results
def _agent_json_for(report: Path):
    """The agent JSON that belongs to a report, if it was written.

    Both names are built from the same stem in engine/analyzer.py:
        <stem>_<mode>_<target>_report.html
        agent_outputs/<stem>_<mode>_<target>_agent.json
    """
    cand = config.AGENT_DIR / (report.name.replace("_report.html", "_agent.json"))
    return cand if cand.exists() else None


@app.get("/api/results")
def results():
    """What is already on disk, newest first.

    A filesystem scan on purpose: M3 replaces this with the SQLite index, and
    the index has to be rebuildable from exactly this information (see
    docs/decisions/0002). Doing it this way first proves that is true.
    """
    if not config.RESULT_DIR.exists():
        return {"items": []}

    items = []
    for report in config.RESULT_DIR.glob("*_report.html"):
        item = {
            "name": report.stem.replace("_report", ""),
            "report": config.rel_to_root(report),
            "modified": report.stat().st_mtime,
            "app_name": None, "package": None, "kits": None,
            "framework": None, "mode": None, "xlsx": None,
        }
        xlsx = report.with_suffix(".xlsx")
        if xlsx.exists():
            item["xlsx"] = config.rel_to_root(xlsx)

        agent = _agent_json_for(report)
        if agent:
            try:
                doc = json.loads(agent.read_text(encoding="utf-8"))
            except (OSError, ValueError):
                doc = {}
            meta = doc.get("app_metadata") or {}
            item["mode"]      = doc.get("mode")
            item["app_name"]  = meta.get("app_name") or meta.get("folder_name") or meta.get("file_name")
            item["package"]   = meta.get("package_name") or meta.get("bundle_id")
            item["kits"]      = len(doc.get("kit_list") or [])
            fw = doc.get("framework") or {}
            item["framework"] = fw.get("framework")
            item["packer"]    = (fw.get("detail") or {}).get("packer")
        items.append(item)

    items.sort(key=lambda i: i["modified"], reverse=True)
    return {"items": items}


# --------------------------------------------------------------- static
# Mounted last: a route defined above always wins over a file with the same path.
app.mount("/", StaticFiles(directory=str(config.WEB_DIR), html=True), name="web")
