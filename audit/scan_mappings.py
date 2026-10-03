"""Audit script 1 -- mapping consistency / schema scanner.

Reads every engine/data/mappings/*.json plus the engine's hard-coded tables and
checks them against the reference corpora in docs-ref/ and engine/data/.
Writes audit/out/mapping_scan.json (machine-readable) and prints a summary.

Run from the repo root:  python audit/scan_mappings.py
Read-only: touches nothing outside audit/out/.
"""
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ENG = ROOT / "engine"
MAP = ENG / "data" / "mappings"
REF = ROOT / "docs-ref"
OUT = ROOT / "audit" / "out"
OUT.mkdir(parents=True, exist_ok=True)
sys.path.insert(0, str(ENG))

findings = []          # (severity, file, key, check, detail)


def F(sev, file, key, check, detail):
    findings.append({"severity": sev, "file": file, "key": key, "check": check, "detail": detail})


def load(name):
    return json.loads((MAP / name).read_text(encoding="utf-8"))


# ------------------------------------------------------------------ evidence
KIT_RE = re.compile(r"@kit\.[A-Za-z0-9]+")
PERM_RE = re.compile(r"ohos\.permission\.[A-Za-z0-9_]+")

kit_dts = {p.name[:-5] for p in (REF / "ArkTS-Harmonyos-apis-and-kits" / "kits").glob("@kit.*.d.ts")}
kit_docs, perm_docs, perm_dts = set(), set(), set()
doc_files = list((REF / "harmonos-official-docs-ref-and-examples" / "data").rglob("*.md"))
for p in doc_files:
    try:
        t = p.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        continue
    kit_docs.update(KIT_RE.findall(t))
    perm_docs.update(PERM_RE.findall(t))
dts_files = list((REF / "ArkTS-Harmonyos-apis-and-kits").rglob("*.d.ts")) + \
            list((REF / "ArkTS-Harmonyos-apis-and-kits").rglob("*.d.ets"))
for p in dts_files:
    t = p.read_text(encoding="utf-8", errors="ignore")
    perm_dts.update(PERM_RE.findall(t))
    kit_docs.update(KIT_RE.findall(t))

idx = json.loads((ENG / "data" / "reference" / "hmos_api_index.json").read_text(encoding="utf-8"))
kit_index = set()
for v in idx.values():
    kit_index.update(KIT_RE.findall(str(v.get("import_statement") or "")))

perm_txt = {}
for p in (ENG / "data" / "permissions").glob("*.txt"):
    for name in PERM_RE.findall(p.read_text(encoding="utf-8")):
        perm_txt.setdefault(name, set()).add(p.stem)

KITS_ALL = kit_dts | kit_docs | kit_index
PERMS_ALL = perm_docs | perm_dts | set(perm_txt)

evidence = {
    "doc_md_files": len(doc_files), "dts_files": len(dts_files),
    "kit_tokens_dts_barrels": len(kit_dts), "kit_tokens_docs_or_dts_text": len(kit_docs),
    "kit_tokens_api_index": len(kit_index), "kit_tokens_union": len(KITS_ALL),
    "perm_names_docs": len(perm_docs), "perm_names_dts": len(perm_dts),
    "perm_names_txt": len(perm_txt), "perm_names_union": len(PERMS_ALL),
}

# Permission .txt lists: are THEIR names attested elsewhere? (they carry
# "[cite: N]" markers -- worth checking they are not themselves invented)
for name, files in sorted(perm_txt.items()):
    if name not in perm_docs and name not in perm_dts:
        F("medium", "permissions/" + "+".join(sorted(files)), name, "perm-txt-unattested",
          "permission listed in engine/data/permissions/*.txt but found in neither the docs corpus nor the .d.ts")
multi = {n: f for n, f in perm_txt.items() if len(f) > 1}
for n, f in sorted(multi.items()):
    F("low", "permissions", n, "perm-txt-in-several-lists", f"listed in {sorted(f)} -- grant class ambiguous")

# ------------------------------------------------------------------ helpers
CONF = {"high", "medium", "low"}


def check_conf(file, key, row):
    if row.get("confidence") not in CONF:
        F("high", file, key, "schema-confidence", f"confidence={row.get('confidence')!r}")


def check_kit(file, key, kit, field="harmony_kit"):
    if kit is None:
        return
    if not KIT_RE.fullmatch(kit or ""):
        F("high", file, key, "kit-token-shape", f"{field}={kit!r} is not an @kit.* token")
    elif kit not in KITS_ALL:
        F("high", file, key, "kit-unattested", f"{field}={kit} appears in no reference source")


def check_perm_target(file, key, perm):
    for p in PERM_RE.findall(perm or ""):
        if p not in PERMS_ALL:
            F("high", file, key, "perm-target-unattested", f"{p} appears in no reference source")


from core.mapping import KIT_DOC_URLS, HMS_DOC_URLS  # noqa: E402

# ------------------------------------------------------------------ mapping.json
m = load("mapping.json")
ns_rows = m["namespace_mappings"]
seen = Counter(r["android_namespace"] for r in ns_rows)
for ns, n in seen.items():
    if n > 1:
        kits = {r.get("harmony_kit") for r in ns_rows if r["android_namespace"] == ns}
        F("high" if len(kits) > 1 else "medium", "mapping.json", ns, "duplicate-prefix",
          f"{n} rows, kits={sorted(map(str, kits))}; the first in file order wins (stable sort)")
REQ = {"android_namespace", "android_display", "harmony_kit", "confidence", "note"}
kits_used = Counter()
for r in ns_rows:
    k = r.get("android_namespace", "?")
    miss = REQ - set(r)
    if miss:
        F("high", "mapping.json", k, "schema-missing", f"missing {sorted(miss)}")
    check_conf("mapping.json", k, r)
    check_kit("mapping.json", k, r.get("harmony_kit"))
    if r.get("harmony_kit"):
        kits_used[r["harmony_kit"]] += 1
        hi = r.get("harmony_import")
        if hi is not None and hi != r["harmony_kit"]:
            F("low", "mapping.json", k, "import-not-kit-token",
              f"harmony_import={hi!r} differs from harmony_kit (rule: import is the kit token)")
    segs = [s for s in k.split(".") if s]
    if len(segs) > 4:
        F("high", "mapping.json", k, "dead-prefix-over-4-segments",
          "engine keys namespaces at 4 segments (apk_engine ns_key) -- this row can never match")
    if k != k.strip() or " " in k:
        F("high", "mapping.json", k, "whitespace-in-prefix", repr(k))
    if not r.get("note"):
        F("medium", "mapping.json", k, "no-evidence-note", "empty note -- grounding not recorded")
for kit in sorted(kits_used):
    if kit not in KIT_DOC_URLS:
        F("medium", "mapping.json", kit, "kit-without-doc-url", f"used by {kits_used[kit]} rows, no KIT_DOC_URLS entry")
for kit in KIT_DOC_URLS:
    check_kit("core/mapping.py KIT_DOC_URLS", kit, kit)
    if "-V5" in KIT_DOC_URLS[kit]:
        F("low", "core/mapping.py KIT_DOC_URLS", kit, "legacy-V5-url", KIT_DOC_URLS[kit])

# shadowing between rows: a shorter prefix that also covers a longer one with a different kit
prefixes = sorted({r["android_namespace"]: r for r in ns_rows}.values(), key=lambda r: len(r["android_namespace"]))
shadow_pairs = []
for i, a in enumerate(prefixes):
    for b in prefixes[i + 1:]:
        if b["android_namespace"].startswith(a["android_namespace"]) and \
                a.get("harmony_kit") != b.get("harmony_kit"):
            boundary = b["android_namespace"][len(a["android_namespace"]):len(a["android_namespace"]) + 1] in (".", "")
            shadow_pairs.append((a["android_namespace"], a.get("harmony_kit"),
                                 b["android_namespace"], b.get("harmony_kit"), boundary))
for a, ak, b, bk, boundary in shadow_pairs:
    if not boundary:
        F("medium", "mapping.json", b, "prefix-overlap-mid-segment",
          f"'{a}' ({ak}) is a string prefix of '{b}' ({bk}) without a '.' boundary -- "
          f"startswith() matching makes '{a}' also claim unrelated roots like '{a}xyz'")

# permissions
for p in m["permission_mappings"]:
    k = p.get("android", "?")
    check_perm_target("mapping.json", k, p.get("harmony"))
    check_kit("mapping.json/permission", k, p.get("kit"), "kit")
    gl = p.get("grant_level")
    targets = PERM_RE.findall(p.get("harmony") or "")
    for t in targets:
        lists = perm_txt.get(t, set())
        expect = {"system_grant": "open_system_grant_permissions",
                  "user_grant": "open_user_grant_permissions",
                  "restricted": "restricted_permissions"}.get(gl)
        if expect and lists and expect not in lists:
            F("medium", "mapping.json/permission", k, "grant-level-vs-list",
              f"grant_level={gl} but {t} is listed in {sorted(lists)}")
    if gl not in ("system_grant", "user_grant", "restricted", "none", None):
        F("low", "mapping.json/permission", k, "grant-level-value", repr(gl))
pdup = Counter(p["android"] for p in m["permission_mappings"])
for k, n in pdup.items():
    if n > 1:
        F("high", "mapping.json/permission", k, "duplicate-permission", f"{n} rows; dict() keeps the LAST")
for p in m["permission_mappings"]:
    a = p["android"]
    if a.startswith("android.permission.") and a != a.strip():
        F("high", "mapping.json/permission", a, "whitespace", repr(a))

# ------------------------------------------------------------------ hms_mapping.json
h = load("hms_mapping.json")
hs = Counter(r["android_namespace"] for r in h["namespace_mappings"])
for ns, n in hs.items():
    if n > 1:
        F("medium", "hms_mapping.json", ns, "duplicate-prefix", f"{n} rows")
for r in h["namespace_mappings"]:
    k = r["android_namespace"]
    check_conf("hms_mapping.json", k, r)
    if len([s for s in k.split(".") if s]) > 4:
        F("high", "hms_mapping.json", k, "dead-prefix-over-4-segments", "can never match")
    if r.get("hms_kit") and r["hms_kit"] not in HMS_DOC_URLS:
        F("low", "hms_mapping.json", k, "hms-kit-without-doc-url", r["hms_kit"])
hp = Counter(p["android"] for p in h["permission_mappings"])
for k, n in hp.items():
    if n > 1:
        F("medium", "hms_mapping.json/permission", k, "duplicate-permission", f"{n} rows")

# ------------------------------------------------------------------ ohpm
o = load("ohpm_mapping.json")
cache = json.loads((ENG / "data" / "reference" / "ohpm_registry_cache.json").read_text(encoding="utf-8"))
reg = cache.get("packages") or cache
reg_names = set(reg) if isinstance(reg, dict) else {x.get("name") for x in reg}
native_sorted = sorted(ns_rows, key=lambda r: len(r["android_namespace"]), reverse=True)
for r in o["ohpm_mappings"]:
    k = r["android_namespace"]
    check_conf("ohpm_mapping.json", k, r)
    if r["ohpm_package"] not in reg_names:
        F("high", "ohpm_mapping.json", k, "ohpm-package-not-in-registry-cache", r["ohpm_package"])
    if r.get("install_cmd") != f"ohpm install {r['ohpm_package']}":
        F("low", "ohpm_mapping.json", k, "install-cmd-mismatch", r.get("install_cmd"))
    if len([s for s in k.split(".") if s]) > 4:
        F("high", "ohpm_mapping.json", k, "dead-prefix-over-4-segments", "can never match")
    # A native row with a kit that covers this prefix wins first -> OHPM row only
    # reachable for namespaces the native row does not cover.
    for nr in native_sorted:
        p = nr["android_namespace"]
        if k.startswith(p) and nr.get("harmony_kit"):
            F("high", "ohpm_mapping.json", k, "ohpm-row-shadowed-by-native",
              f"native '{p}' ({nr['harmony_kit']}) matches every namespace this row could, and wins first")
            break
        if p.startswith(k) and nr.get("harmony_kit"):
            F("info", "ohpm_mapping.json", k, "ohpm-row-partially-shadowed",
              f"native '{p}' ({nr['harmony_kit']}) takes the sub-tree {p}*")
od = Counter(r["android_namespace"] for r in o["ohpm_mappings"])
for k, n in od.items():
    if n > 1:
        F("medium", "ohpm_mapping.json", k, "duplicate-prefix", f"{n} rows")

# ------------------------------------------------------------------ win
w = load("win_mapping.json")
wd = Counter(r["dll_name"].lower() for r in w["dll_mappings"])
for k, n in wd.items():
    if n > 1:
        F("high", "win_mapping.json", k, "duplicate-dll", f"{n} rows; dict() keeps the LAST")
for r in w["dll_mappings"]:
    k = r["dll_name"]
    check_conf("win_mapping.json", k, r)
    check_kit("win_mapping.json", k, r.get("harmony_kit"))
    if r.get("harmony_kit") and r["harmony_kit"] not in KIT_DOC_URLS:
        F("low", "win_mapping.json", k, "kit-without-doc-url", r["harmony_kit"])
    if k != k.lower():
        F("info", "win_mapping.json", k, "dll-name-case", "lower-cased at load; harmless")
# fallback fuzzy match collisions: exe_engine._match_kits tries
#   dll.startswith(Path(key).stem)  in FILE ORDER, first hit wins
stems = [(Path(r["dll_name"].lower()).stem, r["dll_name"].lower(), r["harmony_kit"]) for r in w["dll_mappings"]]
for s1, n1, k1 in stems:
    for s2, n2, k2 in stems:
        if n1 != n2 and s2.startswith(s1) and k1 != k2:
            F("medium", "win_mapping.json", n2, "fuzzy-prefix-collision",
              f"'{n1}' stem is a prefix of '{n2}' with a different kit ({k1} vs {k2}); "
              "only exact-name lookups are safe")

# ------------------------------------------------------------------ ios
i = load("ios_mapping.json")
idup = Counter(r["framework_name"].lower() for r in i["framework_mappings"])
for k, n in idup.items():
    if n > 1:
        F("high", "ios_mapping.json", k, "duplicate-framework", f"{n} rows; dict() keeps the LAST")
for r in i["framework_mappings"]:
    k = r["framework_name"]
    check_conf("ios_mapping.json", k, r)
    check_kit("ios_mapping.json", k, r.get("harmony_kit"))
ip = load("ios_permission_mapping.json")
for p in ip["permission_mappings"]:
    check_perm_target("ios_permission_mapping.json", p["ios_key"], p.get("harmony"))
    check_kit("ios_permission_mapping.json", p["ios_key"], p.get("kit"), "kit")
    if not p["ios_key"].endswith("UsageDescription"):
        F("high", "ios_permission_mapping.json", p["ios_key"], "ios-key-never-matched",
          "ipa_engine only collects Info.plist keys ending in 'UsageDescription'")

# ------------------------------------------------------------------ engine tables
from core.apk_engine import _OHOS_PERM_CATALOGUE  # noqa: E402
for p in _OHOS_PERM_CATALOGUE:
    if p not in PERMS_ALL:
        F("high", "core/apk_engine.py _OHOS_PERM_CATALOGUE", p, "perm-unattested", "")

# ------------------------------------------------------------------ out
sev_rank = {"high": 0, "medium": 1, "low": 2, "info": 3}
findings.sort(key=lambda f: (sev_rank[f["severity"]], f["file"], f["check"], f["key"]))
doc = {
    "evidence": evidence,
    "counts": {
        "mapping.json namespace rows": len(ns_rows), "mapping.json permission rows": len(m["permission_mappings"]),
        "hms namespace rows": len(h["namespace_mappings"]), "hms permission rows": len(h["permission_mappings"]),
        "ohpm rows": len(o["ohpm_mappings"]), "win rows": len(w["dll_mappings"]),
        "ios framework rows": len(i["framework_mappings"]), "ios permission rows": len(ip["permission_mappings"]),
    },
    "by_check": Counter(f["check"] for f in findings),
    "by_severity": Counter(f["severity"] for f in findings),
    "findings": findings,
}
(OUT / "mapping_scan.json").write_text(json.dumps(doc, ensure_ascii=False, indent=1, default=list), encoding="utf-8")
print(json.dumps({k: doc[k] for k in ("evidence", "counts", "by_check", "by_severity")}, indent=1, default=list))
for f in findings:
    if f["severity"] in ("high", "medium"):
        print(f"[{f['severity']}] {f['file']} :: {f['key']} :: {f['check']} :: {f['detail']}")
