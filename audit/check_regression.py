"""Audit script 7 -- old local results (engine/result, 2026-08-30, mapping
v1.11.x) vs a fresh run under the current mappings, per app, from the agent JSON.

Rule being checked (MAPPING_AUDIT_2026-08-30.md): adding mapping rows must
never remove a kit from an app. @kit.AnalyticsKit -> @kit.PerformanceAnalysisKit
is the one documented rename and is excused.

    python audit/check_regression.py <new_run_out_dir>
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
old_dir = ROOT / "engine" / "result" / "agent_outputs"
new_dir = Path(sys.argv[1]).resolve() / "result" / "agent_outputs"
RENAMED = {"@kit.AnalyticsKit": "@kit.PerformanceAnalysisKit"}


def kits(p):
    d = json.loads(p.read_text(encoding="utf-8"))
    return {k["kit_name"]: k.get("confidence") for k in d.get("kit_list", [])}, d


rows, lost_total = [], 0
for newf in sorted(new_dir.glob("*_apk_hmos_agent.json")):
    oldf = old_dir / newf.name
    if not oldf.exists():
        rows.append({"app": newf.name, "note": "no old report"})
        continue
    o, od = kits(oldf)
    n, nd = kits(newf)
    o_mapped = {RENAMED.get(k, k) for k in o}
    lost = sorted(o_mapped - set(n))
    added = sorted(set(n) - o_mapped)
    conf = sorted(k for k in set(o) & set(n) if o[k] != n[k])
    ohpm_o, ohpm_n = len(od.get("ohpm_matches") or []), len(nd.get("ohpm_matches") or [])
    lost_total += len(lost)
    rows.append({"app": newf.name.replace("_apk_hmos_agent.json", ""), "kits_old": len(o), "kits_new": len(n),
                 "lost": lost, "added": added, "confidence_changed": conf,
                 "ohpm_old": ohpm_o, "ohpm_new": ohpm_n,
                 "phantom_AnalyticsKit_in_old": "@kit.AnalyticsKit" in o})
out = {"compared": len([r for r in rows if "lost" in r]), "apps_losing_a_kit": sum(1 for r in rows if r.get("lost")),
       "kits_lost_total": lost_total, "rows": rows}
(ROOT / "audit" / "out" / "regression_check.json").write_text(json.dumps(out, indent=1), encoding="utf-8")
print({k: v for k, v in out.items() if k != "rows"})
for r in rows:
    if r.get("lost") or r.get("note"):
        print("  ", r)
added = {}
for r in rows:
    for k in r.get("added", []):
        added[k] = added.get(k, 0) + 1
print("kits gained (apps):", dict(sorted(added.items(), key=lambda x: -x[1])))
