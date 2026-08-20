"""Which framework was this APK built with? Descriptive metadata only.

Nothing here feeds mapping or matching. `analyze_apk` stores the result under
result["framework"] and every consumer treats it as a label, exactly like
package_name or version_name. No mapping file is read and none is written.

Isolation follows play_meta.py / ohpm_fetch.py: this module is imported by the
engine but imports nothing from it, opens no socket, and never raises -- any
failure degrades to {"framework": "Unknown", ...} so a malformed APK can never
take down an analysis run.

WHY THE SIGNATURE TABLE IS ASSET-FIRST
--------------------------------------
The obvious signatures are native libraries (libflutter.so, libreactnativejni.so)
and that is what the published detectors key on. Measured against this project's
43-app corpus, **27 of 43 APKs (63%) contain no lib/ directory at all** -- they
are the base split of an App Bundle, and every .so lives in a sibling
split_config.*.apk that is not part of the file being analysed. All ten Flutter
apps in the corpus are in that group: not one carries libflutter.so.

So asset-path signatures are primary and .so names are corroboration. That
inversion is the difference between detecting 34 of 43 apps and detecting 16.

TWO FALSE POSITIVES THAT SHAPED THE MATCHING RULES
--------------------------------------------------
* Substring matching is unsafe. Probing for "dcloud" flagged a Capacitor app as
  uni-app because it shipped `assets/public/svg/logo-soundcloud.svg` -- "soun|dcloud".
  Every signature here is matched anchored (exact name, path prefix, or basename),
  never as a bare substring.
* `res/xml/config.xml` is NOT Cordova evidence. Capacitor emits it too, and using
  it alone misclassified com.secmenu.chineselearning, which has no cordova.js at
  all. Cordova requires assets/www/cordova.js or cordova_plugins.js. For the same
  reason `assets/www/` alone proves nothing -- the Flutter app com.tamjai.android
  ships one.
"""

import re
import json
import zipfile

# ---------------------------------------------------------------- signatures
# kind:  "exact"  full archive path
#        "prefix" path prefix (directory)
#        "base"   basename of a lib/<abi>/*.so entry
#        "re"     anchored regex over the full path
# weight: 3 = unique to the framework, 2 = strong but shared, 1 = corroboration
#         only (never enough on its own to name a framework)
_SIGS = [
    # ---- Flutter
    ("Flutter",        "prefix", "assets/flutter_assets/",            3),
    ("Flutter",        "base",   "libflutter.so",                     3),
    ("Flutter",        "re",     r"^assets/flutter_assets/.*kernel_blob\.bin$", 3),
    ("Flutter",        "base",   "libapp.so",                         1),

    # ---- React Native
    ("React Native",   "re",     r"^assets/index\.android\.bundle$",  3),
    ("React Native",   "base",   "libreactnativejni.so",              3),
    ("React Native",   "base",   "libreact_nativemodule_core.so",     2),
    ("React Native",   "base",   "libjsi.so",                         1),
    ("React Native",   "base",   "libyoga.so",                        1),

    # ---- Expo (a React Native distribution, never standalone)
    ("Expo",           "exact",  "assets/app.manifest",               2),
    ("Expo",           "prefix", "assets/EXSplash",                   2),
    ("Expo",           "base",   "libexpo-modules-core.so",           2),

    # ---- Cordova. cordova.js is mandatory; config.xml alone is not evidence.
    ("Cordova",        "exact",  "assets/www/cordova.js",             3),
    ("Cordova",        "exact",  "assets/www/cordova_plugins.js",     3),

    # ---- Capacitor
    ("Capacitor",      "exact",  "capacitor.config.json",             3),
    ("Capacitor",      "exact",  "assets/capacitor.config.json",      3),
    ("Capacitor",      "exact",  "assets/capacitor.plugins.json",     3),
    ("Capacitor",      "prefix", "assets/public/",                    2),

    # ---- Xamarin / MAUI
    ("Xamarin/MAUI",   "base",   "libmonodroid.so",                   3),
    ("Xamarin/MAUI",   "base",   "libmonosgen-2.0.so",                3),
    ("Xamarin/MAUI",   "base",   "libxamarin-app.so",                 3),
    ("Xamarin/MAUI",   "prefix", "assemblies/",                       2),

    # ---- Unity
    ("Unity",          "base",   "libunity.so",                       3),
    ("Unity",          "base",   "libil2cpp.so",                      2),
    ("Unity",          "prefix", "assets/bin/Data/",                  3),

    # ---- Unreal
    ("Unreal Engine",  "base",   "libUE4.so",                         3),
    ("Unreal Engine",  "base",   "libUnreal.so",                      3),

    # ---- NativeScript
    ("NativeScript",   "base",   "libNativeScript.so",                3),
    ("NativeScript",   "exact",  "assets/app/package.json",           2),

    # ---- uni-app / DCloud. The __UNI__ app id makes this unmistakable.
    ("uni-app/DCloud", "re",     r"^assets/apps/__UNI__[A-Za-z0-9]+/", 3),
    ("uni-app/DCloud", "exact",  "assets/data/dcloud_control.xml",    3),
    ("uni-app/DCloud", "exact",  "assets/data/dcloud_properties.json", 3),
    ("uni-app/DCloud", "base",   "libdcloud.so",                      2),

    # ---- Weex (Alibaba)
    ("Weex",           "base",   "libweexcore.so",                    3),
    ("Weex",           "prefix", "assets/weex/",                      2),

    # ---- Alipay mPaaS mini-program container
    ("mPaaS (Alipay)", "base",   "libmpaascpu.so",                    3),
    ("mPaaS (Alipay)", "base",   "libmpaas_crypto.so",                3),

    # ---- APICloud
    ("APICloud",       "exact",  "assets/widget/config.xml",          3),

    # ---- Qt
    ("Qt",             "re",     r"^lib/[^/]+/libQt\d?Core[^/]*\.so$", 3),

    # ---- Kony / LibGDX, from the reference table; unexercised in this corpus
    ("Kony",           "exact",  "assets/konyframework.js",           3),
    ("LibGDX",         "base",   "libgdx.so",                         3),
]

# Primary-framework tie-break when scores are equal. A container/shell framework
# outranks the UI toolkit it hosts, and Expo is never primary -- it is a React
# Native distribution, so an Expo app is a React Native app.
_PRIORITY = [
    "uni-app/DCloud", "mPaaS (Alipay)", "APICloud", "Flutter", "React Native",
    "Unity", "Unreal Engine", "Xamarin/MAUI", "NativeScript", "Weex",
    "Capacitor", "Cordova", "Qt", "Kony", "LibGDX", "Expo",
]

# ---------------------------------------------------------------- packers
# A DEX packer encrypts the real classes and unpacks them at runtime. Under one,
# "no cross-platform signature was found" says nothing at all -- the classes that
# would carry the signature were never in the file we read.
#
# Detected from the archive and, when the caller supplies it, from the namespace
# list the engine already built. Both are needed: com.wlb.android shows a packer
# in the ZIP (libDexHelper.so, assets/bangcle_*) while mo.gov.safp.portal shows
# one only in the DEX (com.antsafe.sec.wrapper).
#
# libmpaas*.so is deliberately NOT here. It is the mPaaS *framework* signature;
# listing it as a packer would report "packer: mPaaS", which is simply untrue.
# Both mPaaS apps in the corpus are still caught, by the markers above.
_PACKER_ZIP = [
    ("360 Jiagu",  "re",     r"^assets/libjiagu[^/]*\.so$"),
    ("360 Jiagu",  "re",     r"^lib/[^/]+/libjiagu[^/]*\.so$"),
    ("Bangcle",    "base",   "libDexHelper.so"),
    ("Bangcle",    "base",   "libDexHelper-x86.so"),
    ("Bangcle",    "prefix", "assets/bangcle_"),
    ("SecNeo",     "base",   "libDexHelper.so"),
    ("Tencent Legu", "base", "libshella.so"),
    ("Ijiami",     "base",   "libexec.so"),
]
_PACKER_NS = [
    ("SecNeo",       "com.secneo"),
    ("360 Jiagu",    "com.stub.StubApp"),
    ("Ant hardening", "com.antsafe"),
    ("Bangcle",      "com.bangcle"),
    ("Qihoo",        "com.qihoo.util"),
    ("Tencent Legu", "com.tencent.StubShell"),
]
# A marker alone is not enough. com.ctm carries com.bangcle.andJni.JniLib* and
# still exposes 19,156 namespaces -- that is a JNI helper, not an encrypted DEX.
# Packing is only concluded when the visible DEX is also effectively empty.
_PACKED_NS_LIMIT = 500

_HERMES_MAGIC = bytes.fromhex("c61fbc03c103191f")
_UNKNOWN = {
    "framework": "Unknown", "confidence": "none", "engine": "N/A",
    "version": "N/A", "version_confidence": "none", "hybrid": [],
    "evidence": [], "detail": {},
}


def _matches(sig_kind, needle, names, lib_bases):
    """Anchored match -- never a bare substring. Returns the triggering path."""
    if sig_kind == "exact":
        return needle if needle in names else None
    if sig_kind == "prefix":
        for n in names:
            if n.startswith(needle):
                return n
        return None
    if sig_kind == "base":
        return lib_bases.get(needle)
    if sig_kind == "re":
        rx = re.compile(needle)
        for n in names:
            if rx.match(n):
                return n
    return None


def _read(z, name, limit=None):
    try:
        with z.open(name) as f:
            return f.read() if limit is None else f.read(limit)
    except Exception:
        return b""


# ---------------------------------------------------------------- engine/version
def _react_native_engine(z, names, lib_bases):
    """Hermes vs JSC, decided by the bundle's own magic number.

    The bundle is authoritative: hk.ust.student ships BOTH libhermes.so and
    libjscinstance.so, so a library-presence test cannot separate them, while the
    bundle header settles it in 12 bytes.
    """
    detail, engine = {}, "N/A"
    if "assets/index.android.bundle" in names:
        head = _read(z, "assets/index.android.bundle", 12)
        if head[:8] == _HERMES_MAGIC:
            engine = "Hermes"
            if len(head) >= 12:
                # Reported as the raw bytecode version. It is NOT mapped to a
                # React Native release: that table is not derivable from the file
                # and guessing it would be inventing a version.
                detail["hermes_bytecode_version"] = int.from_bytes(head[8:12], "little")
        elif head:
            engine = "JSC"
    if engine == "N/A":
        if "libhermes.so" in lib_bases:
            engine = "Hermes"
        elif "libjsc.so" in lib_bases or "libjscexecutor.so" in lib_bases:
            engine = "JSC"
    if any(k in lib_bases for k in ("libreact_newarchdefaults.so", "libfabricjni.so",
                                    "librninstance.so")):
        detail["new_architecture"] = "likely (Fabric/TurboModule libraries present)"
    return engine, detail


def _cordova_version(z, names):
    for cand in ("assets/www/cordova.js", "assets/www/cordova_plugins.js"):
        if cand not in names:
            continue
        txt = _read(z, cand, 400_000).decode("utf-8", "replace")
        m = re.search(r"PLATFORM_VERSION_BUILD_LABEL\s*=\s*['\"]([^'\"]+)", txt)
        if m:
            return m.group(1), "high"
    return "N/A", "none"


def _capacitor_detail(z, names):
    """capacitor.config.json carries appId/appName/webDir but NO version field,
    so a Capacitor version is genuinely unavailable from the APK."""
    for cand in ("capacitor.config.json", "assets/capacitor.config.json"):
        if cand not in names:
            continue
        try:
            j = json.loads(_read(z, cand, 200_000).decode("utf-8", "replace"))
        except Exception:
            return {}
        return {k: j[k] for k in ("appId", "appName", "webDir") if k in j}
    return {}


def _uniapp_detail(z, names):
    """The __UNI__ id and the project version, from the app's own manifest.

    Deliberately NOT reported as `version`: this is the *app* version compiled by
    uni-app, not the uni-app framework version, and conflating them would be a
    lie in a field named "version".
    """
    rx = re.compile(r"^assets/apps/(__UNI__[A-Za-z0-9]+)/www/manifest\.json$")
    for n in names:
        m = rx.match(n)
        if not m:
            continue
        out = {"uniapp_app_id": m.group(1)}
        try:
            j = json.loads(_read(z, n, 400_000).decode("utf-8", "replace"))
        except Exception:
            return out
        if isinstance(j.get("version"), dict):
            out["uniapp_app_version"] = j["version"].get("name") or "N/A"
        return out
    return {}


def _flutter_version(z, names, lib_bases):
    """Engine commit hash out of libflutter.so, when the .so is in this APK.

    Not derivable otherwise: NOTICES.Z holds only licence text (checked -- no
    engine hash, no version), and no other flutter_assets member carries one. In
    a base-split APK there is no libflutter.so, so this is honestly N/A.
    """
    path = lib_bases.get("libflutter.so")
    if not path:
        return "N/A", "none", {}
    blob = _read(z, path)
    if not blob:
        return "N/A", "none", {}
    m = re.search(rb"([0-9a-f]{40})", blob)
    if m:
        return "N/A", "none", {"flutter_engine_commit": m.group(1).decode()}
    return "N/A", "none", {}


def _unity_version(z, names, lib_bases):
    """Unity writes its version as plain text; unexercised in this corpus."""
    for cand in ("assets/bin/Data/globalgamemanagers", "assets/bin/Data/data.unity3d"):
        if cand in names:
            blob = _read(z, cand, 400_000)
            m = re.search(rb"(\d+\.\d+\.\d+[a-z]\d+)", blob)
            if m:
                return m.group(1).decode(), "high"
    return "N/A", "none"


def _qt_version(names):
    for n in names:
        m = re.match(r"^lib/[^/]+/libQt(\d)Core[^/]*\.so$", n)
        if m:
            return "Qt%s (major only, from soname)" % m.group(1), "medium"
    return "N/A", "none"


# ---------------------------------------------------------------- entry point
def _find_packer(names, lib_bases, namespaces):
    """(packer name or None, packed?) -- see _PACKER_ZIP / _PACKED_NS_LIMIT."""
    marker = None
    for name, kind, needle in _PACKER_ZIP:
        if _matches(kind, needle, names, lib_bases):
            marker = name
            break
    if marker is None and namespaces:
        for name, prefix in _PACKER_NS:
            if any(ns == prefix or ns.startswith(prefix) for ns in namespaces):
                marker = name
                break
    if marker is None:
        return None, False
    # Without a namespace list there is no way to tell an encrypted DEX from a
    # packer's helper library, so the marker is reported but packing is not
    # asserted. Claiming it on a marker alone is what the com.ctm case rules out.
    packed = namespaces is not None and len(namespaces) < _PACKED_NS_LIMIT
    return marker, packed


def detect_framework(apk_path: str, names=None, package_name=None,
                     namespaces=None) -> dict:
    """Identify the build framework. Never raises; returns _UNKNOWN on any failure.

    `names` lets a caller that already listed the archive hand the list over; the
    zip is still opened here because engine/version extraction has to read a few
    small members (12 bytes of the RN bundle, cordova.js, a manifest).

    `package_name` is optional and used only to tell an app's OWN framework from
    one bundled inside a third-party SDK -- see _EMBEDDED_NOTE.

    `namespaces` is the engine's detected_namespaces keys, when the caller has
    them. Data flows one way -- this module still imports nothing from the engine
    -- and it buys the packed-DEX test, which cannot be done from the ZIP alone.
    """
    try:
        return _detect(apk_path, names, package_name, namespaces)
    except Exception:
        return dict(_UNKNOWN)


# A Capacitor/Cordova config declares the appId of whatever shipped it. When that
# id is not the APK's own package, the web runtime belongs to an embedded SDK, not
# to the app: com.fairwood.app is a React Native app whose capacitor.config.json
# reads "com.aigens.sdk" (an ordering SDK). Scoring alone called it Capacitor,
# because the SDK contributes three signature files against React Native's one
# bundle. The id comparison is evidence, not a guess, so it decides.
_EMBEDDED_NOTE = "config appId %r is not the app package -- embedded SDK, not the app's own framework"


def _detect(apk_path, names, package_name=None, namespaces=None):
    with zipfile.ZipFile(apk_path) as z:
        if names is None:
            names = z.namelist()
        name_set = set(names)
        lib_bases = {}
        for n in names:
            m = re.match(r"^lib/[^/]+/(lib.+\.so)$", n)
            if m:
                lib_bases.setdefault(m.group(1), n)

        scores, evidence = {}, {}
        for fw, kind, needle, weight in _SIGS:
            hit = _matches(kind, needle, name_set if kind == "exact" else names,
                           lib_bases)
            if hit:
                scores[fw] = scores.get(fw, 0) + weight
                evidence.setdefault(fw, []).append(hit)

        packer, packed = _find_packer(names, lib_bases, namespaces)

        # weight-1 signatures corroborate, they never name a framework alone
        strong = {fw: s for fw, s in scores.items() if s >= 2}
        if not strong:
            # "Native" here is an inference from absence, and under a packed DEX
            # the absence is an artefact of the packer, not a property of the app.
            # Two corpus apps (com.huayuan.namkwong 33 namespaces / 360 Jiagu,
            # hk.gov.ogcio.iamsmart 52 / SecNeo) would otherwise be asserted
            # Native on no evidence whatsoever.
            if packed:
                return {**_UNKNOWN, "framework": "Unknown", "confidence": "none",
                        "detail": {"packer": packer,
                                   "note": "DEX is packed -- the real classes are "
                                           "encrypted, so the framework cannot be "
                                           "determined from this file"}}
            return {**_UNKNOWN, "framework": "Native (Java/Kotlin)",
                    "confidence": "medium",
                    "detail": {"note": "no cross-platform signature found"}}

        embedded = {}
        cap_detail = _capacitor_detail(z, name_set) if "Capacitor" in strong else {}
        cap_id = cap_detail.get("appId")
        if cap_id and package_name and cap_id != package_name and len(strong) > 1:
            embedded["Capacitor"] = _EMBEDDED_NOTE % cap_id

        def rank(fw):
            return (1 if fw in embedded else 0,
                    -strong[fw],
                    _PRIORITY.index(fw) if fw in _PRIORITY else 99)

        ordered = sorted(strong, key=rank)
        # Expo is a React Native distribution, never the primary answer
        if ordered[0] == "Expo" and "React Native" in strong:
            ordered.remove("Expo")
            ordered.insert(0, "React Native")

        primary = ordered[0]
        engine, version, vconf, detail = "N/A", "N/A", "none", {}

        if primary == "React Native" or "React Native" in strong:
            engine, d = _react_native_engine(z, name_set, lib_bases)
            detail.update(d)
        if "Cordova" in strong:
            v, c = _cordova_version(z, name_set)
            if v != "N/A":
                version, vconf = v, c
        if "Capacitor" in strong:
            detail.update(cap_detail)
        if "uni-app/DCloud" in strong:
            detail.update(_uniapp_detail(z, names))
        if "Flutter" in strong:
            _, _, d = _flutter_version(z, names, lib_bases)
            detail.update(d)
        if "Unity" in strong:
            v, c = _unity_version(z, name_set, lib_bases)
            if v != "N/A":
                version, vconf = v, c
        if "Qt" in strong:
            v, c = _qt_version(names)
            if v != "N/A":
                version, vconf = v, c
        if "Expo" in strong:
            detail["expo"] = "yes"

        def conf(fw):
            c = "high" if strong[fw] >= 3 else "medium"
            # A real signature file still proves the framework is linked in, but
            # with the DEX encrypted nothing corroborates it, so it stops being a
            # high-confidence claim.
            if packed and c == "high":
                return "medium"
            return c

        if packer:
            detail["packer"] = packer
        if packed:
            detail["note"] = "DEX packed, corroboration unavailable"

        return {
            "framework":          primary,
            "confidence":         conf(primary),
            "engine":             engine,
            "version":            version,
            "version_confidence": vconf,
            "hybrid": [{"framework": fw, "confidence": conf(fw),
                        "evidence": sorted(set(evidence[fw]))[:4],
                        **({"note": embedded[fw]} if fw in embedded else {})}
                       for fw in ordered[1:]],
            "evidence": sorted(set(evidence[primary]))[:6],
            "detail":   detail,
        }
