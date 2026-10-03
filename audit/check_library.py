"""Audit script 5 -- results library (SQLite index + run manifests).

Works on a COPY of a finished harness output (default audit/out/h_ida), never
on real results. Each scenario runs in a fresh subprocess so app.config picks
up its own MA_RESULT_DIR / MA_DB_PATH.

  A  rescan invariant: library before == library after deleting analyzer.db
  B  delete one report: files gone, manifest edited, does not come back on rescan
  C  delete-many incl. a bogus manifest pair and an outside path (index level)
  D  portability: the whole folder is MOVED, then rescanned from its new place
"""
import json
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "audit" / "out" / "h_ida"
WORK = ROOT / "audit" / "out" / "lib_test"

CHILD = r'''
import json, os, sys
sys.path.insert(0, sys.argv[1])
from app.store import index
op = sys.argv[2]
if op == "library":
    lib = index.library()
elif op == "rescan":
    lib = index.rescan()
elif op == "delete":
    from pathlib import Path
    lib = index.delete_report(Path(sys.argv[3]))
elif op == "delete_many":
    from pathlib import Path
    lib = index.delete_many([Path(p) for p in json.loads(sys.argv[3])], [tuple(x) for x in json.loads(sys.argv[4])])
print(json.dumps(lib, default=str))
'''


def run(folder, *args):
    env = dict(**__import__("os").environ)
    env["MA_RESULT_DIR"] = str(folder / "result")
    env["MA_DB_PATH"] = str(folder / "analyzer.db")
    r = subprocess.run([sys.executable, "-c", CHILD, str(ROOT), *args], env=env,
                       capture_output=True, text=True, encoding="utf-8")
    if r.returncode:
        raise SystemExit(r.stderr)
    return json.loads(r.stdout.strip().splitlines()[-1])


def norm(lib):
    """Library without row ids, for comparison."""
    out = []
    for r in lib["runs"]:
        out.append((r["input_path"], r["status"], r["file_count"],
                    sorted((a["source_file"], a["app_name"], a["kit_count"], a["unmapped_count"],
                            a["coverage_status"], a["coverage_pct"], a["status"],
                            tuple(sorted(a["artifacts"].items()))) for a in r["apps"])))
    return out


res = {}
if WORK.exists():
    shutil.rmtree(WORK)
A = WORK / "A"
shutil.copytree(SRC, A)
before = run(A, "library")
(A / "analyzer.db").unlink(missing_ok=True)
for ext in ("-wal", "-shm"):
    (A / ("analyzer.db" + ext)).unlink(missing_ok=True)
run(A, "rescan")
after = run(A, "library")
res["A_rescan_invariant_equal"] = norm(before) == norm(after)
res["A_counts"] = (sum(len(r["apps"]) for r in before["runs"]), sum(len(r["apps"]) for r in after["runs"]))

# B -- delete one report
rep = next(iter(sorted((A / "result").glob("*_report.html"))))
side_before = sorted(p.name for p in (A / "result" / ".sidecars").glob("*"))
out = run(A, "delete", str(rep))
lib = run(A, "library")
names = [a["source_file"] for r in lib["runs"] for a in r["apps"]]
res["B_deleted_files"] = out.get("deleted")
res["B_report_gone"] = not rep.exists()
res["B_sidecars_removed"] = sorted(set(side_before) - set(p.name for p in (A / "result" / ".sidecars").glob("*")))
run(A, "rescan")
lib2 = run(A, "library")
res["B_apps_after_delete_and_rescan"] = sum(len(r["apps"]) for r in lib2["runs"])
res["B_came_back"] = any(a.get("artifacts", {}).get("html", "").endswith(rep.name)
                         for r in lib2["runs"] for a in r["apps"])

# C -- delete_many with an unknown manifest pair (index level: the HTTP guard is not involved)
reps = [str(p) for p in sorted((A / "result").glob("*_report.html"))[:3]]
out = run(A, "delete_many", json.dumps(reps), json.dumps([["run-nope.json", "x"], ["../evil.json", "y"]]))
res["C_delete_many"] = {k: out[k] for k in ("reports", "failures", "manifests_changed", "apps")}

# D -- move the folder, rescan from the new location
D_old = WORK / "D_original"
shutil.copytree(SRC, D_old)
run(D_old, "rescan")
D_new = WORK / "D_moved_elsewhere"
shutil.move(str(D_old), str(D_new))
run(D_new, "rescan")
libm = run(D_new, "library")
apps = [a for r in libm["runs"] for a in r["apps"]]
html = [a["artifacts"].get("html") for a in apps]
res["D_runs"] = [(r["input_path"], len(r["apps"])) for r in libm["runs"]]
res["D_apps_total"] = len(apps)
res["D_html_artifacts_pointing_at_old_location"] = sum(1 for h in html if h and "D_original" in h)
res["D_html_artifacts_existing"] = sum(1 for h in html if h and ((ROOT / h).exists() or Path(h).exists()))
res["D_sample_html_artifact"] = html[0] if html else None
(ROOT / "audit" / "out" / "library_check.json").write_text(json.dumps(res, indent=1, default=str), encoding="utf-8")
print(json.dumps(res, indent=1, default=str))
