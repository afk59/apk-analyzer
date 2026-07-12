
import re
import sys
import time
import math
from pathlib import Path
from collections import defaultdict
from datetime import datetime

import pefile as _pefile

from ui.terminal import print_info, print_ok, print_warn, _c, C


_SUBSYSTEM = {
    0: "Unknown", 1: "Native", 2: "Windows GUI", 3: "Windows Console (CUI)",
    5: "OS/2 Console", 7: "POSIX Console", 9: "Windows CE GUI",
    10: "EFI Application", 11: "EFI Boot Service Driver",
    12: "EFI Runtime Driver", 13: "EFI ROM", 14: "Xbox",
    16: "Windows Boot Application",
}

_MACHINE = {
    0x0000: "Unknown",   0x014c: "x86 (i386)",
    0x0200: "IA-64",     0x8664: "x86-64 (AMD64)",
    0xAA64: "ARM64",     0x01c0: "ARM (Thumb-2)",
    0x01c4: "ARMv7 Thumb-2",
}


def _read_version_info(pe) -> dict:
    info = {}
    try:
        for finfo in pe.FileInfo:
            for entry in finfo:
                if entry.name == "StringFileInfo":
                    for table in entry.StringTable:
                        for k, v in table.entries.items():
                            key = k.decode("utf-8", errors="replace") if isinstance(k, bytes) else k
                            val = v.decode("utf-8", errors="replace") if isinstance(v, bytes) else v
                            info[key.strip()] = val.strip()
    except Exception:
        pass
    return info


def _is_dotnet(pe) -> bool:
    try:
        return bool(pe.OPTIONAL_HEADER.DATA_DIRECTORY[14].VirtualAddress)
    except Exception:
        return False


def _section_entropy(pe) -> float:
    def _ent(data: bytes) -> float:
        if not data:
            return 0.0
        freq = [0] * 256
        for b in data:
            freq[b] += 1
        n = len(data)
        return -sum((c / n) * math.log2(c / n) for c in freq if c)

    all_secs = [s for s in pe.sections if s.SizeOfRawData > 0]
    if all_secs:
        return round(sum(_ent(s.get_data()) for s in all_secs) / len(all_secs), 3)
    try:
        raw = pe.__data__
        return round(_ent(raw[:min(len(raw), 2 * 1024 * 1024)]), 3)
    except Exception:
        return 0.0


def _detect_packer(pe, sections: list, entropy: float) -> str | None:
    packer_sections = {
        "UPX0": "UPX", "UPX1": "UPX", "UPX2": "UPX",
        ".aspack": "ASPack", ".adata": "ASPack",
        ".MPRESS1": "MPRESS", ".MPRESS2": "MPRESS",
        "themida": "Themida", ".themida": "Themida",
        ".enigma1": "Enigma", ".enigma2": "Enigma",
        ".nsp0": "NsPack", ".nsp1": "NsPack",
        ".vmp0": "VMProtect", ".vmp1": "VMProtect",
        ".pelock": "PELock", ".petite": "Petite",
    }
    for s in sections:
        label = packer_sections.get(s["name"].strip())
        if label:
            return label
    if entropy >= 7.0:
        if not any(s["name"].strip() in (".text", ".code", "CODE") for s in sections):
            return "Unknown packer/protector (high entropy, no standard sections)"
        return "Possibly packed (high section entropy)"
    if not sections and entropy >= 7.0:
        return "Single-segment packed binary"
    return None


def _string_scan_imports(exe_path: str, dll_map: dict, pe_sections: list = None) -> tuple[dict, list]:
    SCAN_ENTROPY_THRESHOLD = 7.0
    ALWAYS_SKIP = {".itext", ".nsp1", ".nsp2", ".themida"}

    print_info("Import table empty — running " + _c("section-aware string-scan", C.BOLD, C.YELLOW) + "...")

    scan_ranges: list = []
    scannable_names: list = []

    if pe_sections:
        try:
            pe2 = _pefile.PE(exe_path, fast_load=False)
            sec_map = {
                s.Name.decode("utf-8", errors="replace").rstrip("\x00"): s
                for s in pe2.sections
            }
            for s_info in pe_sections:
                name    = s_info["name"].rstrip("\x00")
                entropy = s_info["entropy"]
                raw     = s_info["raw_size"]
                if name in ALWAYS_SKIP or raw == 0:
                    continue
                if entropy >= SCAN_ENTROPY_THRESHOLD:
                    continue
                pe_sec = sec_map.get(name)
                if pe_sec and pe_sec.SizeOfRawData > 0:
                    scan_ranges.append((pe_sec.PointerToRawData, pe_sec.SizeOfRawData))
                    scannable_names.append(name)
            pe2.close()
        except Exception as e:
            print_warn(f"Section map build failed: {e} — falling back to full scan")

    scan_ranges.insert(0, (0, 4096))

    if len(scan_ranges) > 1:
        print_info(f"Scanning sections: {_c(', '.join(scannable_names), C.CYAN)}")
        with open(exe_path, "rb") as f:
            chunks = []
            for offset, size in scan_ranges:
                f.seek(offset)
                chunks.append(f.read(size))
        data = b"".join(chunks)
    else:
        print_warn("No low-entropy sections found — full-file scan (may produce noise)")
        with open(exe_path, "rb") as f:
            data = f.read()

    raw_strings = [s.decode("ascii") for s in re.findall(rb"[\x20-\x7e]{5,}", data)]
    wide = [s.decode("utf-16-le", errors="ignore")
            for s in re.findall(rb"(?:[\x20-\x7e]\x00){5,}", data)]
    wide_clean = [s for s in wide if s.isprintable() and len(s) >= 5]
    all_strings = list(dict.fromkeys(raw_strings + wide_clean))
    print_info(f"Extracted {_c(str(len(all_strings)), C.BOLD, C.WHITE)} candidate strings")

    _api_hints = [
        (r"^(Create(Thread|Process|File|Mutex|Event|Semaphore|Pipe|NamedPipe)|"
         r"Virtual(Alloc|Free|Protect|Query)|GetProcAddress|LoadLibrary|"
         r"(Get|Set)LastError|CloseHandle|WriteFile|ReadFile|Sleep|"
         r"HeapAlloc|HeapFree|GetCommandLine|GetModuleHandle)([AW]?)$", "kernel32.dll"),
        (r"^(CreateWindow|DefWindowProc|RegisterClass|GetMessage|"
         r"DispatchMessage|PostMessage|SendMessage|ShowWindow|UpdateWindow|"
         r"MessageBox|SetWindowPos|GetClientRect|InvalidateRect|"
         r"DrawText|TextOut|GetDC|ReleaseDC)([AW]?)$", "user32.dll"),
        (r"^(WSAStartup|WSACleanup|socket|connect|bind|listen|accept|"
         r"send|recv|closesocket|gethostbyname|getaddrinfo|"
         r"WSA(Send|Recv|Connect|Accept|EventSelect)|select)$", "ws2_32.dll"),
        (r"^WinHttp(Open|Connect|OpenRequest|SendRequest|ReceiveResponse|"
         r"ReadData|SetOption|QueryHeaders|CloseHandle)$", "winhttp.dll"),
        (r"^(BitBlt|StretchBlt|CreateCompatibleDC|CreateBitmap|SelectObject|"
         r"DeleteObject|GetStockObject|CreateFont|SetBkMode|SetTextColor)([AW]?)$", "gdi32.dll"),
        (r"^(Crypt(Acquire|Release|Import|Export|Encrypt|Decrypt|Hash|Sign|Verify)"
         r"|BCrypt(OpenAlgorithmProvider|CreateHash|HashData|FinishHash|"
         r"GenerateSymmetricKey|Encrypt|Decrypt))$", "bcrypt.dll"),
        (r"^(Reg(OpenKey|CreateKey|QueryValue|SetValue|CloseKey|DeleteKey|"
         r"EnumKey|EnumValue)|OpenSCManager|CreateService|StartService|"
         r"AdjustTokenPrivileges|LookupPrivilege)([AW]?)$", "advapi32.dll"),
        (r"^(CoInitialize|CoUninitialize|CoCreateInstance|CoCreateGuid|"
         r"StringFromGUID|CLSIDFromString)$", "ole32.dll"),
        (r"^(ShellExecute|SHGetFolderPath|SHGetSpecialFolderPath|"
         r"SHBrowseForFolder|SHGetPathFromIDList|DragAcceptFiles)([AW]?)$", "shell32.dll"),
        (r"^gl(Begin|End|Vertex|Color|Normal|TexCoord|MatrixMode|"
         r"LoadIdentity|Ortho|Frustum|Viewport|Clear|ClearColor|"
         r"Enable|Disable|BindTexture|GenTextures)$", "opengl32.dll"),
        (r"^(D3D11CreateDevice|D3D11CreateDeviceAndSwapChain)$", "d3d11.dll"),
        (r"^(DirectSoundCreate|DirectSoundEnumerate|"
         r"waveOutOpen|waveOutWrite|waveOutClose|waveInOpen)([AW]?)$", "dsound.dll"),
        (r"^(malloc|calloc|realloc|free|memcpy|memmove|memset|memcmp|"
         r"strlen|strcpy|strcat|strcmp|sprintf|printf|fprintf|"
         r"fopen|fclose|fread|fwrite|fseek|ftell|exit|abort)$", "msvcrt.dll"),
        (r"^sqlite3_", "sqlite3.dll"),
        (r"^(SSL_CTX_new|SSL_new|SSL_connect|SSL_read|SSL_write|"
         r"TLS_client_method|OpenSSL_add_all|EVP_).*$", "libssl"),
    ]

    found_imports: dict = defaultdict(set)
    known_dll_set = set(dll_map.keys())

    for ds in [s for s in all_strings if s.lower().endswith(".dll")]:
        if ds.lower() in known_dll_set:
            found_imports[ds.lower()]

    for s in all_strings:
        for pattern, dll_hint in _api_hints:
            if re.match(pattern, s):
                found_imports[dll_hint].add(s)
                break

    for s in all_strings:
        sl = s.lower()
        if sl in known_dll_set and sl not in found_imports:
            found_imports[sl]

    return {dll: sorted(funcs) for dll, funcs in found_imports.items()}, all_strings


def analyze_exe(exe_path: str, mapping: dict) -> dict:
    print_info(f"Loading EXE: {_c(Path(exe_path).name, C.CYAN)}")
    t0 = time.time()

    try:
        pe = _pefile.PE(exe_path, fast_load=False)
    except _pefile.PEFormatError as e:
        print_warn(f"Not a valid PE file: {e}")
        sys.exit(1)

    result = {
        "mode":              "exe",
        "exe_path":          exe_path,
        "target":            "hmos",
        "file_name":         Path(exe_path).name,
        "machine":           _MACHINE.get(pe.FILE_HEADER.Machine, f"0x{pe.FILE_HEADER.Machine:04X}"),
        "subsystem":         _SUBSYSTEM.get(pe.OPTIONAL_HEADER.Subsystem, str(pe.OPTIONAL_HEADER.Subsystem)),
        "is_dll":            bool(pe.FILE_HEADER.Characteristics & 0x2000),
        "is_dotnet":         _is_dotnet(pe),
        "entry_point":       f"0x{pe.OPTIONAL_HEADER.AddressOfEntryPoint + pe.OPTIONAL_HEADER.ImageBase:016X}",
        "image_base":        f"0x{pe.OPTIONAL_HEADER.ImageBase:016X}",
        "timestamp":         datetime.fromtimestamp(pe.FILE_HEADER.TimeDateStamp, tz=__import__('datetime').timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
        "image_size":        pe.OPTIONAL_HEADER.SizeOfImage,
        "version_info":      {},
        "sections":          [],
        "imports":           {},
        "delay_imports":     {},
        "exports":           [],
        "kit_matches":       [],
        "unmapped_dlls":     [],
        "is_packed":         False,
        "packer_hint":       None,
        "string_scan_mode":  False,
        "analysis_time_sec": 0,
    }

    result["version_info"] = _read_version_info(pe)

    for s in pe.sections:
        name = s.Name.decode("utf-8", errors="replace").rstrip("\x00")
        result["sections"].append({
            "name":     name,
            "vsize":    s.Misc_VirtualSize,
            "raw_size": s.SizeOfRawData,
            "entropy":  round(s.get_entropy(), 2),
            "exec":     bool(s.Characteristics & 0x20000000),
        })

    avg_entropy            = _section_entropy(pe)
    packer_hint            = _detect_packer(pe, result["sections"], avg_entropy)
    result["avg_entropy"]  = avg_entropy
    result["packer_hint"]  = packer_hint
    result["is_packed"]    = packer_hint is not None

    print_info("Parsing import table...")
    if hasattr(pe, "DIRECTORY_ENTRY_IMPORT"):
        for entry in pe.DIRECTORY_ENTRY_IMPORT:
            dll   = entry.dll.decode("utf-8", errors="replace").lower()
            funcs = []
            for imp in entry.imports:
                funcs.append(imp.name.decode("utf-8", errors="replace") if imp.name else f"ordinal#{imp.ordinal}")
            result["imports"][dll] = funcs

    if hasattr(pe, "DIRECTORY_ENTRY_DELAY_IMPORT"):
        for entry in pe.DIRECTORY_ENTRY_DELAY_IMPORT:
            dll   = entry.dll.decode("utf-8", errors="replace").lower()
            funcs = []
            for imp in entry.imports:
                funcs.append(imp.name.decode("utf-8", errors="replace") if imp.name else f"ordinal#{imp.ordinal}")
            result["delay_imports"][dll] = funcs

    if hasattr(pe, "DIRECTORY_ENTRY_EXPORT"):
        for exp in pe.DIRECTORY_ENTRY_EXPORT.symbols:
            if exp.name:
                result["exports"].append(exp.name.decode("utf-8", errors="replace"))

    pe.close()

    dll_map_full = {m["dll_name"].lower(): m for m in mapping.get("dll_mappings", [])}

    if not result["imports"] and not result["delay_imports"]:
        scanned, all_strings    = _string_scan_imports(exe_path, dll_map_full, result["sections"])
        result["imports"]       = scanned
        result["string_scan_mode"] = True
        result["all_strings"]   = all_strings
        print_warn(
            f"Import table empty (entropy={avg_entropy}, packer={packer_hint or 'none'}) "
            "— string-scan results are best-effort"
        )

    print_info(f"Matching {_c('HarmonyOS NEXT', C.BOLD, C.CYAN)} kits...")

    matched_kits: dict = {}
    all_dlls = {**result["imports"], **result["delay_imports"]}

    for dll, funcs in all_dlls.items():
        entry = dll_map_full.get(dll)
        if not entry:
            stem = Path(dll).stem
            for key in dll_map_full:
                if dll.startswith(Path(key).stem) or Path(key).stem == stem:
                    entry = dll_map_full[key]
                    break

        if entry:
            kit = entry["harmony_kit"]
            if kit not in matched_kits:
                matched_kits[kit] = {
                    "kit_name":      kit,
                    "harmony_import": entry.get("harmony_import"),
                    "confidence":    entry["confidence"],
                    "note":          entry["note"],
                    "sample_url":    entry.get("sample_url"),
                    "codelab_url":   entry.get("codelab_url"),
                    "dll_sources":   [],
                }
            matched_kits[kit]["dll_sources"].append({
                "dll_name":     dll,
                "dll_display":  entry["dll_display"],
                "func_count":   len(funcs),
                "sample_funcs": funcs[:10],
                "is_delay":     dll in result["delay_imports"],
            })
        else:
            if not any(dll.startswith(s) for s in ["api-ms-win", "ext-ms-win", "_codegen"]):
                result["unmapped_dlls"].append({
                    "dll_name":     dll,
                    "func_count":   len(funcs),
                    "sample_funcs": funcs[:8],
                    "is_delay":     dll in result["delay_imports"],
                })

    for kit_data in matched_kits.values():
        kit_data["dll_sources"].sort(key=lambda x: x["func_count"], reverse=True)

    result["kit_matches"]  = sorted(matched_kits.values(), key=lambda x: x["kit_name"])
    result["unmapped_dlls"].sort(key=lambda x: x["func_count"], reverse=True)

    result["analysis_time_sec"] = round(time.time() - t0, 2)
    print_ok(f"Analysis complete in {_c(str(result['analysis_time_sec']) + 's', C.BOLD, C.GREEN)}")
    return result
