"""Audit script 4 -- how the real match loop behaves on the corpus namespaces.

Replays apk_engine's matcher (namespace_mappings sorted longest-first,
`ns.startswith(pattern) or pattern == ns`, first hit wins) over every namespace
recorded in a side-car (mapped + unmapped), and reports:

  * mid-segment matches: the pattern matched but the next char of the
    namespace is not '.', e.g. pattern 'com.amap.api.maps' claiming
    'com.amap.api.maps2d', or 'io.grpc' claiming 'io.grpcx'
  * rows that match nothing in the corpus (dead in practice)
  * rows that can never match by construction (> 4 segments)
  * coverage composition: how many "covered" namespaces are Android platform
    namespaces (android.*), which the engine only counts when they match

Usage: python audit/check_matching.py [sidecar_dir ...]
"""
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
dirs = [Path(p) for p in sys.argv[1:]] or [ROOT / "engine" / "result" / ".sidecars"]
m = json.loads((ROOT / "engine" / "data" / "mappings" / "mapping.json").read_text(encoding="utf-8"))
rows = sorted(m["namespace_mappings"], key=lambda e: len(e["android_namespace"]), reverse=True)
o = json.loads((ROOT / "engine" / "data" / "mappings" / "ohpm_mapping.json").read_text(encoding="utf-8"))
orows = sorted(o["ohpm_mappings"], key=lambda e: len(e["android_namespace"]), reverse=True)

SKIP = ["java.", "javax.", "kotlin.", "android.os", "sun.", "dalvik.", "libcore.",
        "com.android.internal.", "android.app", "android.content", "android.database",
        "android.net", "android.text", "android.util", "android.hardware"]


def match(ns, table):
    for e in table:
        p = e["android_namespace"]
        if ns.startswith(p) or p == ns:
            return e
    return None


hits = Counter()
mid = defaultdict(set)
apps_cov = []
for d in dirs:
    for f in sorted(d.glob("*.json")):
        s = json.loads(f.read_text(encoding="utf-8"))
        if s.get("mode") not in (None, "apk"):
            continue
        all_ns = [x["namespace"] for x in s.get("mapped", [])] + \
                 [x["namespace"] for x in s.get("unmapped", [])] + \
                 [x["namespace"] for x in s.get("ohpm", [])]
        for ns in all_ns:
            e = match(ns, rows)
            if e is None:
                e2 = match(ns, orows)
                if e2:
                    hits["ohpm:" + e2["android_namespace"]] += 1
                    p = e2["android_namespace"]
                    if len(ns) > len(p) and ns[len(p)] != "." and not p.endswith("."):
                        mid["ohpm:" + p].add(ns)
                continue
            p = e["android_namespace"]
            hits[p] += 1
            if len(ns) > len(p) and ns[len(p)] != "." and not p.endswith("."):
                mid[p].add(ns)
        # coverage composition, as the engine computes it
        mapped = [x["namespace"] for x in s.get("mapped", [])]
        plat = [n for n in mapped if any(n.startswith(p) for p in SKIP)]
        det, tot, ohpm = s.get("total_detected_ns", 0), s.get("total_3p_ns", 0), s.get("total_ohpm_ns", 0)
        if tot:
            # the engine's figure, and the figure with skip-prefixed platform namespaces
            # removed from both sides (they can only ever be counted as covered)
            cov = (det + ohpm) / tot * 100
            adj = (det + ohpm - len(set(plat))) / max(1, tot - len(set(plat))) * 100
            apps_cov.append((f.stem, tot, len(set(plat)), round(cov, 1), round(adj, 1)))

never = [r["android_namespace"] for r in rows if r["android_namespace"] not in hits]
over4 = [r["android_namespace"] for r in rows if len([s for s in r["android_namespace"].split(".") if s]) > 4]
out = {
    "sidecar_dirs": [str(d) for d in dirs],
    "rows_total": len(rows),
    "rows_matching_something": len([r for r in rows if r["android_namespace"] in hits]),
    "rows_matching_nothing": len(never),
    "rows_over_4_segments": over4,
    "mid_segment_matches": {k: sorted(v) for k, v in mid.items()},
    "coverage_platform_effect": apps_cov,
}
(ROOT / "audit" / "out" / ("matching_check_" + dirs[0].parent.name + ".json")).write_text(
    json.dumps(out, indent=1, ensure_ascii=False), encoding="utf-8")
print(f"rows {len(rows)}; matching something {out['rows_matching_something']}; nothing {len(never)}")
print("mid-segment matches:")
for k, v in sorted(mid.items()):
    print(f"   {k:45} -> {sorted(v)[:6]}{' ...' if len(v) > 6 else ''}")
print("coverage: app, total_3p, platform ns counted as covered, engine %, % without them")
for a in sorted(apps_cov, key=lambda x: x[3] - x[4], reverse=True)[:12]:
    print("  ", a)
if apps_cov:
    diffs = [a[3] - a[4] for a in apps_cov]
    print(f"   mean inflation {sum(diffs)/len(diffs):.2f} pp, max {max(diffs):.2f} pp over {len(apps_cov)} apps")
