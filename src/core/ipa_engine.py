
import json
import os
import tempfile
import time
import zipfile
import plistlib
from pathlib import Path

from ui.terminal import print_info, print_ok, print_warn, _c, C


def _find_info_plist(zf: zipfile.ZipFile) -> bytes | None:
    for name in zf.namelist():
        parts = Path(name).parts
        if (len(parts) == 3
                and parts[0] == "Payload"
                and parts[1].endswith(".app")
                and parts[2] == "Info.plist"):
            return zf.read(name)

    for name in zf.namelist():
        parts = Path(name).parts
        if len(parts) >= 3 and parts[-2].endswith(".app") and parts[-1] == "Info.plist":
            return zf.read(name)
    return None


def _list_frameworks(zf: zipfile.ZipFile) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for name in zf.namelist():
        parts = Path(name).parts

        if (len(parts) >= 4
                and parts[0] == "Payload"
                and parts[1].endswith(".app")
                and parts[2] == "Frameworks"):
            fw = parts[3]
            if fw.endswith(".framework") and fw not in seen:
                seen.add(fw)
                result.append(fw[: -len(".framework")])
    return sorted(result)


def _list_plugins(zf: zipfile.ZipFile) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for name in zf.namelist():
        parts = Path(name).parts
        if (len(parts) >= 4
                and parts[0] == "Payload"
                and parts[1].endswith(".app")
                and parts[2] == "PlugIns"):
            ext = parts[3]
            if ext.endswith(".appex") and ext not in seen:
                seen.add(ext)
                result.append(ext[: -len(".appex")])
    return sorted(result)


def _is_binary_encrypted(zf: zipfile.ZipFile, executable_name: str | None) -> bool:
    try:
        from macholib import MachO
    except ImportError:
        return False


    app_folder: str | None = None
    for name in zf.namelist():
        parts = Path(name).parts
        if len(parts) >= 2 and parts[0] == "Payload" and parts[1].endswith(".app"):
            app_folder = parts[1]
            break
    if not app_folder:
        return False

    binary_name = executable_name or app_folder[: -len(".app")]
    binary_zip_path = f"Payload/{app_folder}/{binary_name}"
    if binary_zip_path not in zf.namelist():
        return False

    tmp_path: str | None = None
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".macho") as tmp:
            tmp.write(zf.read(binary_zip_path))
            tmp_path = tmp.name
        macho = MachO.MachO(tmp_path)
        for header in macho.headers:
            for lc, cmd, _ in header.commands:

                if lc.cmd in (0x21, 0x2C):
                    if getattr(cmd, "cryptid", 0) != 0:
                        return True
        return False
    except Exception:
        return False
    finally:
        if tmp_path:
            try:
                os.unlink(tmp_path)
            except OSError:
                pass


def _load_permission_map() -> dict:
    perm_path = Path(__file__).parent.parent / "data" / "mappings" / "ios_permission_mapping.json"
    if not perm_path.exists():
        print_warn("ios_permission_mapping.json not found — permission matching disabled")
        return {}
    try:
        data = json.loads(perm_path.read_text(encoding="utf-8"))
        return {p["ios_key"]: p for p in data.get("permission_mappings", [])}
    except Exception as exc:
        print_warn(f"Failed to load ios_permission_mapping.json: {exc}")
        return {}


def analyze_ipa(ipa_path: str, mapping: dict) -> dict:
    print_info(f"Loading IPA: {_c(Path(ipa_path).name, C.CYAN)}")
    t0 = time.time()

    result: dict = {
        "mode":                "ipa",
        "target":              "hmos",
        "file_name":           Path(ipa_path).name,
        "bundle_id":           None,
        "app_name":            None,
        "version":             None,
        "min_ios_version":     None,
        "permissions":         [],
        "frameworks":          [],
        "extensions":          [],
        "url_schemes":         [],
        "kit_matches":           [],
        "unmapped_frameworks":   [],
        "permission_matches":    [],
        "is_encrypted":          False,
        "is_encrypted_warning":  None,
        "static_linking_likely": False,
        "analysis_time_sec":     0,
    }

    try:
        zf = zipfile.ZipFile(ipa_path, "r")
    except zipfile.BadZipFile as exc:
        print_warn(f"Not a valid IPA (ZIP archive): {exc}")
        import sys; sys.exit(1)

    with zf:

        plist_data = _find_info_plist(zf)
        executable_name: str | None = None
        if plist_data:
            try:
                info = plistlib.loads(plist_data)
                result["bundle_id"]       = info.get("CFBundleIdentifier")
                result["app_name"]        = (info.get("CFBundleDisplayName")
                                             or info.get("CFBundleName"))
                result["version"]         = (info.get("CFBundleShortVersionString")
                                             or info.get("CFBundleVersion"))
                result["min_ios_version"] = info.get("MinimumOSVersion")
                executable_name           = info.get("CFBundleExecutable")


                result["permissions"] = sorted(
                    k for k in info if k.endswith("UsageDescription")
                )


                schemes: list[str] = []
                for url_type in info.get("CFBundleURLTypes", []):
                    for scheme in url_type.get("CFBundleURLSchemes", []):
                        if scheme not in schemes:
                            schemes.append(scheme)
                result["url_schemes"] = schemes

            except Exception as exc:
                print_warn(f"Failed to parse Info.plist: {exc}")
        else:
            print_warn("Info.plist not found — IPA structure may be non-standard")

        result["frameworks"] = _list_frameworks(zf)
        result["extensions"] = _list_plugins(zf)


        encrypted = _is_binary_encrypted(zf, executable_name)
        result["is_encrypted"] = encrypted
        if encrypted:
            result["is_encrypted_warning"] = (
                "Binary is encrypted (App Store build). Framework analysis only."
            )
            print_warn("Binary is encrypted (App Store build) — framework analysis only")

    result["static_linking_likely"] = (
        len(result["frameworks"]) < 3 and result["is_encrypted"]
    )

    print_info(
        f"Found {_c(str(len(result['frameworks'])), C.BOLD, C.WHITE)} frameworks, "
        f"{_c(str(len(result['permissions'])), C.BOLD, C.WHITE)} permission key(s)"
    )


    print_info(f"Matching {_c('HarmonyOS NEXT', C.BOLD, C.CYAN)} kits...")

    fw_map = {
        m["framework_name"].lower(): m
        for m in mapping.get("framework_mappings", [])
    }
    matched_kits: dict = {}

    for fw in result["frameworks"]:
        entry = fw_map.get(fw.lower())
        if entry:
            kit = entry["harmony_kit"]
            if kit not in matched_kits:
                matched_kits[kit] = {
                    "kit_name":          kit,
                    "harmony_import":    entry.get("harmony_import"),
                    "confidence":        entry["confidence"],
                    "note":              entry["note"],
                    "framework_sources": [],
                }
            matched_kits[kit]["framework_sources"].append({
                "framework_name":    fw,
                "framework_display": entry.get("framework_display", fw),
            })
        else:
            result["unmapped_frameworks"].append(fw)

    result["kit_matches"] = sorted(matched_kits.values(), key=lambda x: x["kit_name"])
    result["unmapped_frameworks"].sort()


    permission_map = _load_permission_map()
    for perm_key in result["permissions"]:
        if perm_key in permission_map:
            pm = permission_map[perm_key]
            result["permission_matches"].append({
                "ios_key":     perm_key,
                "ios_display": pm.get("ios_display", perm_key),
                "harmony":     pm.get("harmony"),
                "kit":         pm.get("kit"),
            })

    result["analysis_time_sec"] = round(time.time() - t0, 2)
    print_ok(
        f"Analysis complete in {_c(str(result['analysis_time_sec']) + 's', C.BOLD, C.GREEN)}"
    )
    return result
