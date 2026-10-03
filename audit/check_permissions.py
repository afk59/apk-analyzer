"""Audit script 2 -- permission mapping accuracy.

For every ohos.permission.* that the product can put in front of a migrator
(mapping.json permission rows, ios_permission_mapping.json, and the engine's
gap-suggester catalogue) this measures, from the SDK .d.ts doc comments:

  * how many API declarations carry `@permission <name>`
  * how many of those blocks are ALSO `@systemapi` (system apps only)

A permission whose every annotated API is @systemapi cannot be granted to a
third-party app -- recommending it as the HarmonyOS counterpart of an ordinary
Android permission tells the migrator something that is not available to them.

Also replays the engine's keyword-overlap gap suggester (_suggest_hmos_perm)
over every Android permission name seen in the corpus reports, so its
suggestions can be sample-reviewed.

Writes audit/out/permission_check.json.
"""
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ENG = ROOT / "engine"
sys.path.insert(0, str(ENG))
OUT = ROOT / "audit" / "out"

BLOCK = re.compile(r"/\*\*(.*?)\*/", re.S)
PERM = re.compile(r"ohos\.permission\.[A-Za-z0-9_]+")

stats = defaultdict(lambda: {"apis": 0, "systemapi": 0, "files": set()})
for p in (ROOT / "docs-ref" / "ArkTS-Harmonyos-apis-and-kits").rglob("*.d.ts"):
    text = p.read_text(encoding="utf-8", errors="ignore")
    for b in BLOCK.finditer(text):
        body = b.group(1)
        if "@permission" not in body:
            continue
        line = next((ln for ln in body.splitlines() if "@permission" in ln), "")
        sysapi = "@systemapi" in body
        for name in set(PERM.findall(line)):
            s = stats[name]
            s["apis"] += 1
            s["systemapi"] += int(sysapi)
            s["files"].add(p.name)

txt_lists = defaultdict(set)
for p in (ENG / "data" / "permissions").glob("*.txt"):
    for n in PERM.findall(p.read_text(encoding="utf-8")):
        txt_lists[n].add(p.stem)

docs_hits = defaultdict(int)
for p in (ROOT / "docs-ref" / "harmonos-official-docs-ref-and-examples" / "data").rglob("*.md"):
    for n in PERM.findall(p.read_text(encoding="utf-8", errors="ignore")):
        docs_hits[n] += 1


def verdict(name):
    s = stats.get(name)
    if s and s["apis"] and s["systemapi"] == s["apis"]:
        return "SYSTEM-APP ONLY (every annotated API is @systemapi)"
    if s and s["apis"]:
        return f"open ({s['apis'] - s['systemapi']}/{s['apis']} annotated APIs are public)"
    if name in txt_lists:
        return "in permission .txt list only (no .d.ts annotation)"
    if docs_hits.get(name):
        return "docs only"
    return "UNATTESTED"


def describe(name):
    s = stats.get(name, {"apis": 0, "systemapi": 0, "files": set()})
    return {"name": name, "verdict": verdict(name), "dts_apis": s["apis"],
            "dts_systemapi": s["systemapi"], "txt_lists": sorted(txt_lists.get(name, [])),
            "docs_md_hits": docs_hits.get(name, 0)}


rows = []
m = json.loads((ENG / "data" / "mappings" / "mapping.json").read_text(encoding="utf-8"))
for p in m["permission_mappings"]:
    for t in PERM.findall(p.get("harmony") or ""):
        rows.append({"source": "mapping.json", "android": p["android"], "grant_level_in_row": p.get("grant_level"),
                     **describe(t)})
ip = json.loads((ENG / "data" / "mappings" / "ios_permission_mapping.json").read_text(encoding="utf-8"))
for p in ip["permission_mappings"]:
    for t in PERM.findall(p.get("harmony") or ""):
        rows.append({"source": "ios_permission_mapping.json", "android": p["ios_key"], **describe(t)})

from core.apk_engine import _OHOS_PERM_CATALOGUE, _suggest_hmos_perm  # noqa: E402
cat = [describe(n) for n in _OHOS_PERM_CATALOGUE]

# Suggester replay over every Android permission name the corpus reports carry
android_perms = set()
for f in (ENG / "result" / "agent_outputs").glob("*_agent.json"):
    d = json.loads(f.read_text(encoding="utf-8"))
    for g in d.get("permission_gaps") or []:
        android_perms.add(g.get("android_perm"))
for f in (ROOT / "audit" / "out").rglob("*_agent.json"):
    d = json.loads(f.read_text(encoding="utf-8"))
    for g in d.get("permission_gaps") or []:
        android_perms.add(g.get("android_perm"))
mapped = {p["android"] for p in m["permission_mappings"]}
sugg = []
for a in sorted(x for x in android_perms if x):
    s, c = _suggest_hmos_perm(a)
    sugg.append({"android": a, "suggested": s, "confidence": c, "in_mapping": a in mapped,
                 "suggested_verdict": verdict(s) if s else None})

doc = {"mapping_targets": rows, "suggester_catalogue": cat, "suggester_replay": sugg}
(OUT / "permission_check.json").write_text(json.dumps(doc, indent=1, ensure_ascii=False), encoding="utf-8")

print("== mapping.json / ios permission targets")
for r in rows:
    print(f"{r['source'][:8]:8} {r['android'][:52]:52} -> {r['name'][16:]:30} {r['verdict']}  txt={r['txt_lists']} docs={r['docs_md_hits']}")
print("\n== suggester catalogue")
for c in cat:
    if not c["verdict"].startswith("open"):
        print(f"   {c['name']:50} {c['verdict']}")
print(f"\n== suggester replay: {len(sugg)} android permissions seen in reports")
for s in sugg:
    if not s["in_mapping"] and s["suggested"]:
        print(f"   {s['android'][:60]:60} -> {s['suggested'][16:]:28} [{s['confidence']}] {s['suggested_verdict']}")
