
import re
import time
import zipfile
from pathlib import Path
from collections import defaultdict

from ui.terminal import print_info, print_ok, print_warn, _c, C


_OHOS_PERM_CATALOGUE = [

    "ohos.permission.INTERNET",
    "ohos.permission.MANAGE_WIFI_CONNECTION",
    "ohos.permission.MANAGE_BLUETOOTH",
    "ohos.permission.ACCESS_BLUETOOTH",
    "ohos.permission.ACCESS_NFC",
    "ohos.permission.ACCESS_NEARLINK",

    "ohos.permission.LOCATION",
    "ohos.permission.APPROXIMATELY_LOCATION",
    "ohos.permission.LOCATION_IN_BACKGROUND",
    "ohos.permission.MEDIA_LOCATION",

    "ohos.permission.CAMERA",
    "ohos.permission.MICROPHONE",
    "ohos.permission.READ_IMAGEVIDEO",
    "ohos.permission.WRITE_IMAGEVIDEO",
    "ohos.permission.SHORT_TERM_WRITE_IMAGEVIDEO",
    "ohos.permission.READ_AUDIO",
    "ohos.permission.WRITE_AUDIO",
    "ohos.permission.READ_MEDIA_IMAGES",
    "ohos.permission.READ_MEDIA_VIDEO",
    "ohos.permission.READ_MEDIA_AUDIO",
    "ohos.permission.WRITE_MEDIA",

    "ohos.permission.READ_CONTACTS",
    "ohos.permission.WRITE_CONTACTS",
    "ohos.permission.READ_CALENDAR",
    "ohos.permission.WRITE_CALENDAR",
    "ohos.permission.READ_MESSAGES",
    "ohos.permission.SEND_MESSAGES",
    "ohos.permission.RECEIVE_SMS",
    "ohos.permission.RECEIVE_MMS",
    "ohos.permission.READ_CELL_MESSAGES",

    "ohos.permission.ANSWER_CALL",
    "ohos.permission.READ_CALL_LOG",
    "ohos.permission.WRITE_CALL_LOG",
    "ohos.permission.GET_TELEPHONY_STATE",
    "ohos.permission.MANAGE_VOICEMAIL",

    "ohos.permission.STORE_PERSISTENT_DATA",
    "ohos.permission.DISTRIBUTED_DATASYNC",

    "ohos.permission.ACTIVITY_MOTION",
    "ohos.permission.READ_HEALTH_DATA",
    "ohos.permission.VIBRATE",

    "ohos.permission.ACCESS_BIOMETRIC",
    "ohos.permission.USE_BIOMETRIC",
    "ohos.permission.MANAGE_SECURE_SETTINGS",

    "ohos.permission.NOTIFICATION_CONTROLLER",
    "ohos.permission.PUBLISH_AGENT_REMINDER",
    "ohos.permission.KEEP_BACKGROUND_RUNNING",

    "ohos.permission.GET_INSTALLED_BUNDLE_LIST",
]


_PERM_NOISE = frozenset({
    "ACCESS", "GET", "USE", "SET", "MANAGE", "REQUEST",
    "CHANGE", "RECEIVE", "READ", "WRITE", "SEND",
})


def _suggest_hmos_perm(android_perm: str) -> tuple:
    a_name = android_perm.replace("android.permission.", "").upper()
    a_keys = set(a_name.split("_"))
    a_meaningful = a_keys - _PERM_NOISE

    best_ohos  = None
    best_score = 0

    for ohos in _OHOS_PERM_CATALOGUE:
        o_name = ohos.replace("ohos.permission.", "").upper()
        o_keys = set(o_name.split("_"))
        o_meaningful = o_keys - _PERM_NOISE

        pool = (a_meaningful & o_meaningful) if (a_meaningful and o_meaningful) else (a_keys & o_keys)
        score = len(pool)
        if score > best_score:
            best_score = score
            best_ohos  = ohos

    if best_score == 0 or best_ohos is None:
        return None, None

    o_name = best_ohos.replace("ohos.permission.", "").upper()
    if a_name == o_name or best_score >= 2:
        confidence = "high"
    else:

        o_keys = set(o_name.split("_"))
        word = next(iter((a_meaningful & (o_keys - _PERM_NOISE)) or (a_keys & o_keys)), "")
        confidence = "medium" if len(word) >= 4 else "low"

    return best_ohos, confidence


_OBFUS_SIMPLE = re.compile(r'^[A-Za-z]{1,2}[0-9]{0,2}$')
_OBFUS_SHORT  = re.compile(r'^[A-Z]\.[A-Za-z0-9]{2,5}$')
# An R8/ProGuard-renamed *package root* -- every segment a letter plus at most
# one more char: "f.d.c.a", "k.k0.l.i", "c.h.o.i0".
_OBFUS_PKG    = re.compile(r'^[A-Za-z][A-Za-z0-9]?(\.[A-Za-z][A-Za-z0-9]?)+$')


def _is_obfuscated(class_name: str, method_name: str) -> bool:
    simple = class_name.split(".")[-1]
    return bool(
        _OBFUS_SIMPLE.match(simple)
        or _OBFUS_SHORT.match(class_name)
        or _OBFUS_SIMPLE.match(method_name)
    )


def _is_unresolvable(ns: str) -> bool:
    return (
        "__" in ns
        or "._" in ns
        or "$" in ns
        or ns.startswith("kotlinx.")
        # Obfuscated package root. _is_obfuscated() cannot catch these: the
        # classes underneath are inner classes ("f.d.c.a.a0.a$a"), whose simple
        # name keeps the "$" and so misses _OBFUS_SIMPLE, while the namespace
        # key is truncated to 4 segments and so never contains the "$" either.
        # The result was an obfuscated package leaking into the report's
        # "Unrecognized Third-Party Libraries" table as if it were a real
        # library. Deliberately namespace-level, NOT class-level: a class like
        # "com.bumptech.glide.load.a$a" is obfuscated too, but its *package*
        # still identifies the library, so it must stay attributed to Glide.
        # Verified against all 415 patterns in mapping.json / hms_mapping.json /
        # ohpm_mapping.json - none matches.
        or bool(_OBFUS_PKG.match(ns))
    )


_CTOR_SUFFIXES = (".<init>", ".<clinit>")
# An R8-renamed trailing package segment: "m", "j", "b1", "e1", "a0".
# Deliberately [A-Za-z][0-9]* and not [A-Za-z]{1,2}: two-LETTER segments are
# overwhelmingly real ("com.huawei.hms.ui", "org.spongycastle.math.ec",
# "com.tom_roush.pdfbox.io", "expo.modules.updates.db" -- 77 such namespaces in
# the 43-app corpus) and must not be swept up.
_OBFUS_TAIL = re.compile(r'^[A-Za-z][0-9]{0,3}$')


def _is_synthetic_method(method: str) -> bool:
    """Compiler-generated bridge/lambda: access$000, $r8$lambda$x, -$$Nest$mfoo.

    Note this tests the METHOD name only. A "$" in the class part is an ordinary
    inner class ("com.facebook.hermes.intl.c$b.clone") and says nothing about the
    method, which is the only thing the report renders.
    """
    return "$" in method.split(".")[-1]


def _sample_methods(methods, limit: int = 5) -> list:
    """Pick sample methods worth showing.

    Two kinds of noise crowd out real API surface in an R8 build:

    * synthetic accessors (access$000, $r8$lambda$...) -- pure compiler
      plumbing, dropped outright; they carried 3,004 of the corpus's unmapped
      rows before this filter;
    * "<init>"/"<clinit>", which only say "this class was constructed" (32% of
      all methods under com.fairwood.app's unmapped namespaces). Held back
      rather than dropped, so a namespace with nothing else still shows
      something instead of a blank cell.
    """
    ordered = sorted(m for m in methods if not _is_synthetic_method(m))
    real    = [m for m in ordered if not m.endswith(_CTOR_SUFFIXES)]
    return (real or ordered)[:limit]


def _informative_class(cls: str, ns: str) -> bool:
    """Does any segment of `cls` below `ns` carry a readable name?"""
    rest = cls[len(ns) + 1:] if cls.startswith(ns + ".") else ""
    if not rest:
        return False
    return any(seg.split("$")[0] and not _OBFUS_TAIL.match(seg.split("$")[0])
               for seg in rest.split("."))


def _is_obfuscated_pkg(ns: str, classes) -> bool:
    """An R8-renamed package segment, e.g. "com.google.firebase.m".

    _OBFUS_PKG only catches roots where EVERY segment is obfuscated; R8 also
    renames a single segment under an intact vendor prefix, which then shows up
    in the report as a library called "com.google.firebase.m" or
    "com.facebook.i1.e1".

    The trailing segment alone is not sufficient evidence -- it also matches real
    packages ("org.spongycastle.asn1.x509", "com.dcloud.android.v4",
    "com.zipow.videobox.I420", "com.ibm.security.x509"). What separates them is
    the classes underneath: a real package keeps its class names
    ("x509.AccessDescription"), an R8-renamed one does not ("m.c$b"). Measured
    over the 43-app corpus this splits 82 candidates into 74 obfuscated and 8
    real, with no false positive on either side.
    """
    if not _OBFUS_TAIL.match(ns.split(".")[-1]):
        return False
    return not any(_informative_class(c, ns) for c in classes)


def _is_private_lib(ns: str, package_name: str, ns_mappings: list) -> bool:
    parts = (package_name or "").split(".")
    bundle_root = ".".join(parts[:2]) if len(parts) >= 2 else package_name
    if not bundle_root or not ns.startswith(bundle_root):
        return False
    for entry in ns_mappings:
        pattern = entry["android_namespace"]
        if ns.startswith(pattern) or pattern == ns:
            return False
    return True


def _safe_attr(getter, default=None):
    """androguard's get_androidversion_name/code index self.androidversion[...]
    directly, so any APK without android:versionName/versionCode raises
    KeyError instead of returning None. Every other getter we use is safe."""
    try:
        return getter()
    except Exception:
        return default


def _warn_if_split_bundle(apk_path: str) -> None:
    """APKM/XAPK are ZIPs of split APKs (base.apk + config.*.apk), not APKs.
    Renaming one to .apk gets it past the extension check but androguard then
    finds no manifest/dex and the result is silently meaningless."""
    try:
        with zipfile.ZipFile(apk_path) as z:
            names = z.namelist()
    except Exception:
        return
    if "classes.dex" in names or "AndroidManifest.xml" in names:
        return
    inner = [n for n in names if n.lower().endswith(".apk")]
    if inner:
        print_warn(
            "This looks like a split-APK bundle (APKM/XAPK), not a plain APK — "
            f"it contains {len(inner)} inner .apk file(s)."
        )
        print_warn(
            "Extract it and analyze base.apk instead; results here will be empty or wrong."
        )


def _match_ohpm(ns: str, ohpm_entries: list):
    """Longest-prefix match against the OHPM second tier.

    Deliberately identical in shape to the native matcher in `analyze_apk`:
    `ohpm_entries` arrives sorted longest-`android_namespace`-first, and the
    first prefix hit wins. Returns the row dict or None.
    """
    for entry in ohpm_entries:
        prefix = entry["android_namespace"]
        if ns.startswith(prefix) or prefix == ns:
            return entry
    return None


def _record_second_tier(ns, ns_info, result, ohpm_entries, skip_prefixes) -> None:
    """Route a namespace that found no native kit into OHPM, else unmapped.

    This is the ONLY place either bucket is filled, and it is only ever reached
    from a branch where the native tier has already missed — which is what makes
    "native behaviour is unchanged" true by construction rather than by testing.

    The noise gate (skip_prefixes + method_count >= 2) is applied FIRST, so the
    second tier can never surface a namespace the native tier deliberately
    suppresses. A namespace failing the gate is dropped entirely, exactly as
    before.
    """
    if (any(ns.startswith(p) for p in skip_prefixes)
            or ns_info["method_count"] < 2):
        return

    row = {
        "namespace":      ns,
        "method_count":   ns_info["method_count"],
        "class_count":    ns_info["class_count"],
        "sample_methods": _sample_methods(ns_info["methods"]),
    }

    hit = _match_ohpm(ns, ohpm_entries)
    if hit is None:
        # Last stop before the report: nothing maps this namespace, so if it is
        # an R8-renamed package it is pure noise and belongs in FILTERED.
        #
        # This check MUST stay here, after both tiers have missed, and must never
        # be hoisted into the pre-matching loop. Tried that first and it deleted
        # a real result: com.facebook.login's only non-"$" namespace is
        # "com.facebook.login.u0", so filtering it up front left the
        # com.facebook.login pattern with no source at all and @kit.AccountKit
        # vanished from an app that genuinely uses Facebook Login. A namespace
        # that matches a mapping rule is evidence of a real library no matter how
        # badly R8 mangled its name.
        if _is_obfuscated_pkg(ns, ns_info["classes"]):
            result["unresolvable_namespaces"].append({
                "namespace":      ns,
                "method_count":   ns_info["method_count"],
                "class_count":    ns_info["class_count"],
                "sample_methods": row["sample_methods"],
            })
            return
        row["tier"] = "unmapped"
        result["unmapped_namespaces"].append(row)
        return

    row.update({
        "tier":            "ohpm",
        "matched_prefix":  hit["android_namespace"],
        "android_display": hit.get("android_display"),
        "ohpm_package":    hit["ohpm_package"],
        "install_cmd":     hit.get("install_cmd") or f"ohpm install {hit['ohpm_package']}",
        "category":        hit.get("category"),
        "description":     hit.get("description"),
        "confidence":      hit.get("confidence"),
        "source_repo":     hit.get("source_repo"),
        "popularity":      hit.get("popularity"),
        "note":            hit.get("note"),
    })
    result["ohpm_matches"].append(row)


def analyze_apk(apk_path: str, mapping: dict, target: str,
                ohpm_mapping: dict | None = None) -> dict:
    from androguard.misc import AnalyzeAPK

    kit_field = "hms_kit" if target == "hms" else "harmony_kit"
    is_hmos   = target == "hmos"

    # OHPM packages are ArkTS/HarmonyOS NEXT artifacts. An HMS app is still an
    # Android app and cannot consume them, so the second tier is HMOS-only.
    from core.mapping import build_ohpm_entries
    ohpm_entries = build_ohpm_entries(ohpm_mapping) if is_hmos else []

    print_info(f"Loading APK: {_c(Path(apk_path).name, C.CYAN)}")
    _warn_if_split_bundle(apk_path)
    t0 = time.time()
    a, d_list, dx = AnalyzeAPK(apk_path)
    print_info("Analyzing DEX bytecode...")

    result = {
        "mode":                "apk",
        "apk_path":            apk_path,
        "target":              target,
        "package_name":        a.get_package(),
        "app_name":            a.get_app_name(),
        "version_name":        _safe_attr(a.get_androidversion_name),
        "version_code":        _safe_attr(a.get_androidversion_code),
        "min_sdk":             a.get_min_sdk_version(),
        "target_sdk":          a.get_target_sdk_version(),
        "permissions":         [],
        "activities":          [],
        "services":            [],
        "receivers":           [],
        "providers":           [],
        "native_libs":         [],
        "manifest_xml":        "",
        "detected_namespaces": {},
        "kit_matches":         [],
        "ohpm_matches":        [],
        "permission_matches":  [],
        "unmapped_namespaces":    [],
        "unresolvable_namespaces": [],
        "api_matches":            [],
        "permission_gaps":        [],
        "private_libs":           [],
        "missed_match_count":  0,
        "obfuscated_count":    0,
        "analysis_time_sec":   0,
    }

    result["permissions"] = sorted(a.get_permissions())
    # sorted(): androguard returns these in manifest-parse order, which is not
    # stable between runs, so the Manifest Components table reshuffled on every
    # re-analysis of the same APK.
    result["activities"]  = sorted(a.get_activities())
    result["services"]    = sorted(a.get_services())
    result["receivers"]   = sorted(a.get_receivers())
    result["providers"]   = sorted(a.get_providers())

    try:
        xml_raw = a.get_android_manifest_axml().get_xml()
        result["manifest_xml"] = (
            xml_raw.decode("utf-8", errors="replace")
            if isinstance(xml_raw, bytes) else str(xml_raw)
        )
    except Exception:
        pass

    try:
        with zipfile.ZipFile(apk_path) as z:
            result["native_libs"] = [
                n for n in z.namelist()
                if n.startswith("lib/") and n.endswith(".so")
            ]
    except Exception:
        pass

    print_info("Scanning method references...")
    ns_data: dict = defaultdict(lambda: {"classes": set(), "methods": set()})
    obfuscated_count = 0
    for cls in dx.get_classes():
        for meth in cls.get_methods():
            for _, call, _ in meth.get_xref_to():
                cc = call.class_name.lstrip("L").rstrip(";").replace("/", ".")
                if cc.startswith(result["package_name"]):
                    continue
                if _is_obfuscated(cc, call.name):
                    obfuscated_count += 1
                    continue
                parts  = cc.split(".")
                ns_key = ".".join(parts[:4]) if len(parts) >= 4 else cc
                ns_data[ns_key]["classes"].add(cc)
                ns_data[ns_key]["methods"].add(f"{cc}.{call.name}")

    for ns, data in ns_data.items():
        result["detected_namespaces"][ns] = {
            "classes":      sorted(data["classes"]),
            "methods":      sorted(data["methods"]),
            "method_count": len(data["methods"]),
            "class_count":  len(data["classes"]),
        }

    target_label = "HarmonyOS NEXT" if is_hmos else "HMS Core"
    print_info(f"Matching {_c(target_label, C.BOLD, C.CYAN)} kits...")

    ns_mappings = sorted(
        mapping.get("namespace_mappings", []),
        key=lambda e: len(e["android_namespace"]),
        reverse=True,
    )
    perm_lookup = {p["android"]: p for p in mapping.get("permission_mappings", [])}

    matched_kits: dict = {}
    matched_ns:   set  = set()

    skip_prefixes = [
        "java.", "javax.", "kotlin.", "android.os", "sun.",
        "dalvik.", "libcore.", "com.android.internal.",
        "android.app", "android.content", "android.database",
        "android.net", "android.text", "android.util", "android.hardware",
    ]
    if target == "hms":
        skip_prefixes = skip_prefixes + ["android.", "androidx."]

    for ns, ns_info in result["detected_namespaces"].items():
        if _is_unresolvable(ns):
            result["unresolvable_namespaces"].append({
                "namespace":      ns,
                "method_count":   ns_info["method_count"],
                "class_count":    ns_info["class_count"],
                "sample_methods": _sample_methods(ns_info["methods"]),
            })
            continue

        if _is_private_lib(ns, result["package_name"], ns_mappings):
            result["private_libs"].append({
                "namespace":      ns,
                "method_count":   ns_info["method_count"],
                "class_count":    ns_info["class_count"],
                "sample_methods": _sample_methods(ns_info["methods"]),
            })
            continue


        best_match = None
        for entry in ns_mappings:
            pattern = entry["android_namespace"]
            if ns.startswith(pattern) or pattern == ns:
                best_match = entry
                break

        if best_match:
            kit = best_match[kit_field]

            if not kit:
                # An explicit `harmony_kit: null` row means "no native kit". The
                # namespace was unmapped before the second tier existed, so it is
                # fair game for OHPM.
                _record_second_tier(ns, ns_info, result, ohpm_entries, skip_prefixes)
                continue

            pattern = best_match["android_namespace"]

            if kit not in matched_kits:
                matched_kits[kit] = {
                    "kit_name":    kit,
                    "confidence":  best_match["confidence"],
                    "note":        best_match["note"],
                    "sample_url":  best_match.get("sample_url"),
                    "codelab_url": best_match.get("codelab_url"),
                    "_agg":        {},
                }
                if is_hmos:
                    matched_kits[kit]["harmony_import"] = best_match.get("harmony_import", kit)

            agg = matched_kits[kit]["_agg"]
            if pattern not in agg:
                agg[pattern] = {
                    "android_namespace": pattern,
                    "android_display":   best_match["android_display"],
                    "class_count":       0,
                    "method_count":      0,
                    "sample_methods":    set(),
                }
            agg[pattern]["class_count"]  += ns_info["class_count"]
            agg[pattern]["method_count"] += ns_info["method_count"]
            agg[pattern]["sample_methods"].update(ns_info["methods"])
            matched_ns.add(ns)

        elif ns.startswith("androidx."):

            kit = "@kit.ArkUI"
            if kit not in matched_kits:
                matched_kits[kit] = {
                    "kit_name":    kit,
                    "confidence":  "high",
                    "note":        "AndroidX compatibility library → ArkUI component system",
                    "sample_url":  None,
                    "codelab_url": None,
                    "_agg":        {},
                }
                if is_hmos:
                    matched_kits[kit]["harmony_import"] = kit
            agg = matched_kits[kit]["_agg"]
            if "androidx." not in agg:
                agg["androidx."] = {
                    "android_namespace": "androidx.",
                    "android_display":   "AndroidX Libraries",
                    "class_count":       0,
                    "method_count":      0,
                    "sample_methods":    set(),
                }
            agg["androidx."]["class_count"]  += ns_info["class_count"]
            agg["androidx."]["method_count"] += ns_info["method_count"]
            agg["androidx."]["sample_methods"].update(ns_info["methods"])
            matched_ns.add(ns)

        else:
            _record_second_tier(ns, ns_info, result, ohpm_entries, skip_prefixes)

    for kit_data in matched_kits.values():
        kit_data["android_sources"] = [
            {
                "android_namespace": v["android_namespace"],
                "android_display":   v["android_display"],
                "class_count":       v["class_count"],
                "method_count":      v["method_count"],
                "sample_methods":    _sample_methods(v["sample_methods"], 8),
            }
            for v in kit_data.pop("_agg").values()
        ]

    result["kit_matches"] = sorted(matched_kits.values(), key=lambda x: x["kit_name"])
    result["total_detected_ns"] = len(matched_ns)
    # OHPM matches are counted here even though they are not native matches.
    # Before the second tier existed they sat in unmapped_namespaces, so leaving
    # them out would SHRINK this denominator and silently inflate the native
    # coverage percentage. total_3p_ns must stay exactly what it was.
    result["total_3p_ns"] = (len(matched_ns)
                             + len(result["unmapped_namespaces"])
                             + len(result["ohpm_matches"]))

    for perm in result["permissions"]:
        if perm in perm_lookup:
            result["permission_matches"].append(perm_lookup[perm])

    matched_android_perms = {pm["android"] for pm in result["permission_matches"]}
    unmatched_perms       = [p for p in result["permissions"] if p not in matched_android_perms]
    gaps = []
    for perm in unmatched_perms:
        suggested, conf = _suggest_hmos_perm(perm)
        if suggested:
            gaps.append({"android_perm": perm, "suggested_hmos": suggested, "confidence": conf})
    result["permission_gaps"]    = gaps
    result["missed_match_count"] = len(unmatched_perms)

    # Tie-break on namespace: method_count alone leaves equal-count rows in
    # detected_namespaces order, which varies per run. unresolvable_namespaces
    # was never sorted at all.
    _by_count = lambda x: (-x["method_count"], x["namespace"])
    result["unmapped_namespaces"].sort(key=_by_count)
    result["ohpm_matches"].sort(key=_by_count)
    result["private_libs"].sort(key=_by_count)
    result["unresolvable_namespaces"].sort(key=_by_count)
    result["obfuscated_count"]  = obfuscated_count

    print_info("Matching HarmonyOS APIs...")
    from core.api_matcher import match_methods
    all_methods: list = []
    for ns_info in result["detected_namespaces"].values():
        all_methods.extend(ns_info["methods"])
    # Sorted, because match_methods() de-duplicates by SIMPLE method name and
    # keeps the FIRST occurrence. Unsorted, the winner depends on the order of
    # detected_namespaces, which follows androguard's dx.get_classes() and varies
    # between runs — so which class "owns" a shared name like getApplicationInfo
    # was arbitrary, and the resulting api_matches (hence every kit row's
    # inner_methods, and the HTML/Excel built from them) differed run-to-run for
    # the same APK. Sorting makes the dedup deterministic and reports reproducible.
    result["api_matches"] = match_methods(sorted(all_methods))


    if result["api_matches"]:
        _conf_up = {"low": "medium", "medium": "high", "high": "high"}
        boosted_kits = {m["kit"] for m in result["api_matches"] if m.get("kit")}
        for km in result["kit_matches"]:
            if km["kit_name"] in boosted_kits:
                km["confidence"] = _conf_up.get(km["confidence"], km["confidence"])


    _status_map = {"high": "Supported", "medium": "Replaceable", "low": "Should Confirm"}
    _color_map  = {"high": "green",     "medium": "amber",       "low": "blue"}
    for km in result["kit_matches"]:
        km["status"]       = _status_map.get(km["confidence"], "Should Confirm")
        km["status_color"] = _color_map.get(km["confidence"], "blue")
        km["tier"]         = "native"


    if result["api_matches"]:
        for km in result["kit_matches"]:
            for src in km["android_sources"]:
                ns_prefix = src["android_namespace"]
                inner: list = []
                seen: set   = set()
                for am in result["api_matches"]:
                    m = am.get("android_method", "")
                    if m.startswith(ns_prefix) and m not in seen:
                        seen.add(m)
                        inner.append({
                            "method_name":  m,
                            "hmos_method":  am.get("import_statement", ""),
                            "status":       "Supported",
                            "status_color": "green",
                        })
                if inner:
                    src["inner_methods"] = inner[:8]

    result["analysis_time_sec"] = round(time.time() - t0, 2)
    print_ok(f"Analysis complete in {_c(str(result['analysis_time_sec']) + 's', C.BOLD, C.GREEN)}")
    return result
