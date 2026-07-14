
import sys
import os
from pathlib import Path


if os.name == "nt":
    import ctypes
    _kernel = ctypes.windll.kernel32
    _handle = _kernel.GetStdHandle(-11)
    _mode   = ctypes.c_ulong()
    if _kernel.GetConsoleMode(_handle, ctypes.byref(_mode)):
        _kernel.SetConsoleMode(_handle, _mode.value | 0x0004)


class C:
    RESET  = "\033[0m"
    BOLD   = "\033[1m"
    RED    = "\033[38;5;160m"
    GREEN  = "\033[38;5;40m"
    YELLOW = "\033[38;5;220m"
    CYAN   = "\033[38;5;45m"
    WHITE  = "\033[38;5;255m"
    GRAY   = "\033[38;5;245m"
    DRED   = "\033[38;5;124m"
    PURPLE = "\033[38;5;141m"


def _c(text: str, *codes: str) -> str:
    return "".join(codes) + str(text) + C.RESET


def print_info(msg: str) -> None:
    print(f"  {_c('[*]', C.BOLD, C.CYAN)}  {msg}")


def print_ok(msg: str) -> None:
    print(f"  {_c('[OK]', C.BOLD, C.GREEN)}  {_c(msg, C.WHITE)}")


def print_warn(msg: str) -> None:
    print(f"  {_c('[!]', C.BOLD, C.RED)}  {_c(msg, C.WHITE)}")


def tui_select(prompt: str, options: list) -> int:
    selected = 0

    try:
        import tty, termios
        HAS_TTY = True
    except ImportError:
        HAS_TTY = False

    try:
        import msvcrt
        HAS_MSVCRT = True
    except ImportError:
        HAS_MSVCRT = False

    def _render():
        sys.stdout.write(f"  {_c(prompt, C.BOLD, C.WHITE)}\n")
        for i, opt in enumerate(options):
            if i == selected:
                marker = _c(" > ", C.BOLD, C.GREEN)
                line   = _c(opt, C.BOLD, C.WHITE)
            else:
                marker = "   "
                line   = _c(opt, C.GRAY)
            sys.stdout.write(f"  {marker}{line}\n")
        sys.stdout.write(f"\033[{len(options)+1}A")
        sys.stdout.flush()

    if HAS_TTY:

        fd  = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            _render()
            while True:
                ch = sys.stdin.read(1)
                if ch == "\x1b":
                    ch2 = sys.stdin.read(1)
                    ch3 = sys.stdin.read(1)
                    if ch2 == "[":
                        if ch3 == "A" and selected > 0:
                            selected -= 1
                        elif ch3 == "B" and selected < len(options) - 1:
                            selected += 1
                elif ch in ("\r", "\n", " "):
                    break
                elif ch == "\x03":
                    raise KeyboardInterrupt
                _render()
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old)
        sys.stdout.write(f"\033[{len(options)+1}B\n")
        sys.stdout.flush()

    elif HAS_MSVCRT:

        _render()
        while True:
            ch = msvcrt.getch()
            if ch in (b"\x00", b"\xe0"):

                ch2 = msvcrt.getch()
                if ch2 == b"H" and selected > 0:
                    selected -= 1
                elif ch2 == b"P" and selected < len(options) - 1:
                    selected += 1
            elif ch in (b"\r", b"\n", b" "):
                break
            elif ch == b"\x03":
                raise KeyboardInterrupt
            _render()
        sys.stdout.write(f"\033[{len(options)+1}B\n")
        sys.stdout.flush()

    else:

        print(f"\n  {_c(prompt, C.BOLD, C.WHITE)}")
        for i, opt in enumerate(options):
            print(f"  {_c(f'[{i+1}]', C.BOLD, C.CYAN)}  {_c(opt, C.WHITE)}")
        while True:
            try:
                sys.stdout.write(f"  {_c(f'Enter number (1-{len(options)}): ', C.YELLOW)}")
                sys.stdout.flush()
                val = int(input()) - 1
                if 0 <= val < len(options):
                    selected = val
                    break
            except (ValueError, EOFError):
                pass
    return selected


def print_banner() -> None:
    w      = 59
    border = "  " + _c("+" + "-" * w + "+", C.BOLD, C.DRED)
    title  = "Migration Analyzer v2.0  --  Huawei DTSE Turkey"
    pad_l  = (w - len(title)) // 2
    pad_r  = w - len(title) - pad_l - 2
    print()
    print(border)
    print(
        "  " + _c("|", C.BOLD, C.DRED)
        + " " * pad_l
        + _c(title, C.BOLD, C.WHITE)
        + " " * pad_r
        + " " + _c("|", C.BOLD, C.DRED)
    )
    print(border)
    print()


def interactive_session(script_dir: Path):
    print_banner()

    input_types = [
        "APK  (Android → HarmonyOS NEXT / HMS)",
        "EXE  (Windows → HarmonyOS NEXT)",
        "IPA  (iOS → HarmonyOS NEXT)  [limited: App Store binaries are encrypted]",
        "Batch  (all APK + EXE + IPA files in input/)",
        "EXE Folder  (analyze all .exe/.dll in an input/pc/<folder>/)",
    ]
    type_idx = tui_select("Select input type  (arrow keys + Enter):", input_types)
    print()

    if type_idx == 3:
        targets    = ["HarmonyOS NEXT", "HMS Core  (APKs; EXE/IPA always → NEXT)"]
        target_idx = tui_select("Select APK target:", targets)
        target     = "hmos" if target_idx == 0 else "hms"
        label_t    = "HarmonyOS NEXT" if target == "hmos" else "HMS Core"
        print(f"  {_c('Selected target :', C.CYAN)}  {_c(label_t, C.BOLD, C.WHITE)}")
        print()
        return None, "batch", target

    if type_idx == 4:
        pc_dir = script_dir / "pc"
        pc_dir.mkdir(exist_ok=True)
        subfolders = sorted(p for p in pc_dir.iterdir() if p.is_dir())
        if not subfolders:
            print_warn(f"No subfolders found in {pc_dir}")
            print(f"         {_c('Create a folder like input/pc/cppcheck/ with .exe/.dll files and run again.', C.GRAY)}\n")
            sys.exit(0)
        folder_idx  = tui_select("Select folder to analyze  (arrow keys + Enter):", [p.name for p in subfolders])
        folder_path = subfolders[folder_idx]
        print()
        print(f"  {_c('Selected folder :', C.CYAN)}  {_c(folder_path.name, C.BOLD, C.WHITE)}")
        print(f"  {_c('Selected target :', C.CYAN)}  {_c('HarmonyOS NEXT', C.BOLD, C.WHITE)}")
        print()
        return folder_path, "exe_folder", "hmos"

    if type_idx == 0:
        mode, ext, label = "apk", "*.apk", "APK"
    elif type_idx == 1:
        mode, ext, label = "exe", "*.exe", "EXE"
    else:
        mode, ext, label = "ipa", "*.ipa", "IPA"

    print_info(f"Place your {label} file in the " + _c("input/", C.BOLD, C.WHITE) + " folder:")
    print(f"         {_c(str(script_dir), C.CYAN)}")
    print()

    files = sorted(script_dir.glob(ext))
    if not files:
        print_warn(f"No {ext} files found in this folder.")
        print(f"         {_c('Copy your file here and run again.', C.GRAY)}\n")
        sys.exit(0)

    file_idx  = tui_select(f"Select {label}  (arrow keys + Enter):", [f.name for f in files])
    file_path = files[file_idx]

    print()
    print(f"  {_c(f'Selected {label:<4}:', C.CYAN)}  {_c(file_path.name, C.BOLD, C.WHITE)}")

    if mode == "apk":
        targets    = ["HarmonyOS NEXT", "HMS Core"]
        target_idx = tui_select("Select migration target:", targets)
        target     = "hmos" if target_idx == 0 else "hms"
        label_t    = "HarmonyOS NEXT" if target == "hmos" else "HMS Core"
    else:
        target  = "hmos"
        label_t = "HarmonyOS NEXT"

    print(f"  {_c('Selected target :', C.CYAN)}  {_c(label_t, C.BOLD, C.WHITE)}")
    print()
    return file_path, mode, target


def print_summary_apk(result: dict) -> None:
    conf_colors = {"high": (C.BOLD, C.GREEN), "medium": (C.BOLD, C.YELLOW), "low": (C.BOLD, C.RED)}
    conf_labels = {"high": "HIGH", "medium": "MED ", "low": "LOW "}
    print()
    print(f"  {_c('-' * 50, C.DRED)}")
    print(f"  {_c('SUMMARY  —  APK', C.BOLD, C.WHITE)}")
    print(f"  {_c('-' * 50, C.DRED)}")
    print(f"  {_c('Package     :', C.CYAN)}  {result['package_name']}")
    print(f"  {_c('App         :', C.CYAN)}  {result['app_name']} v{result['version_name']}")
    print(f"  {_c('Kit matches :', C.CYAN)}  {_c(str(len(result['kit_matches'])), C.BOLD, C.WHITE)}")
    print(f"  {_c('Permissions :', C.CYAN)}  {len(result['permission_matches'])} / {len(result['permissions'])} matched")
    print()
    for km in result["kit_matches"]:
        conf  = km["confidence"]
        clrs  = conf_colors.get(conf, (C.RESET,))
        label = _c(f"[{conf_labels.get(conf,'???')}]", *clrs)
        print(f"  {label}  {_c(km['kit_name'], C.WHITE)}")


def print_summary_exe(result: dict) -> None:
    conf_colors = {"high": (C.BOLD, C.GREEN), "medium": (C.BOLD, C.YELLOW), "low": (C.BOLD, C.RED)}
    conf_labels = {"high": "HIGH", "medium": "MED ", "low": "LOW "}
    total_funcs = sum(len(v) for v in result["imports"].values())
    print()
    print(f"  {_c('-' * 50, C.DRED)}")
    print(f"  {_c('SUMMARY  —  EXE', C.BOLD, C.WHITE)}")
    print(f"  {_c('-' * 50, C.DRED)}")
    print(f"  {_c('File        :', C.CYAN)}  {result['file_name']}")
    print(f"  {_c('Arch        :', C.CYAN)}  {result['machine']}")
    print(f"  {_c('Subsystem   :', C.CYAN)}  {result['subsystem']}")
    if result["is_dotnet"]:
        print(f"  {_c('Runtime     :', C.CYAN)}  {_c('.NET / CLR detected', C.BOLD, C.YELLOW)}")
    print(f"  {_c('Imports     :', C.CYAN)}  {len(result['imports'])} DLLs  /  {total_funcs} functions")
    print(f"  {_c('Kit matches :', C.CYAN)}  {_c(str(len(result['kit_matches'])), C.BOLD, C.WHITE)}")
    print(f"  {_c('Unmapped    :', C.CYAN)}  {len(result['unmapped_dlls'])} DLLs")
    print()
    for km in result["kit_matches"]:
        conf  = km["confidence"]
        clrs  = conf_colors.get(conf, (C.RESET,))
        label = _c(f"[{conf_labels.get(conf,'???')}]", *clrs)
        print(f"  {label}  {_c(km['kit_name'], C.WHITE)}")


def print_summary_exe_folder(result: dict) -> None:
    conf_colors = {"high": (C.BOLD, C.GREEN), "medium": (C.BOLD, C.YELLOW), "low": (C.BOLD, C.RED)}
    conf_labels = {"high": "HIGH", "medium": "MED ", "low": "LOW "}
    total_funcs = sum(len(v) for v in result["imports"].values())
    errors = [f for f in result["files"] if f.get("error")]
    print()
    print(f"  {_c('-' * 50, C.DRED)}")
    print(f"  {_c('SUMMARY  —  EXE FOLDER', C.BOLD, C.WHITE)}")
    print(f"  {_c('-' * 50, C.DRED)}")
    print(f"  {_c('Folder      :', C.CYAN)}  {result['folder_name']}")
    print(f"  {_c('Files       :', C.CYAN)}  {result['file_count']} analyzed" + (f"  ({len(errors)} failed)" if errors else ""))
    print(f"  {_c('Imports     :', C.CYAN)}  {len(result['imports'])} DLLs  /  {total_funcs} functions")
    print(f"  {_c('Kit matches :', C.CYAN)}  {_c(str(len(result['kit_matches'])), C.BOLD, C.WHITE)}")
    print(f"  {_c('Unmapped    :', C.CYAN)}  {len(result['unmapped_dlls'])} DLLs")
    print()
    for km in result["kit_matches"]:
        conf  = km["confidence"]
        clrs  = conf_colors.get(conf, (C.RESET,))
        label = _c(f"[{conf_labels.get(conf,'???')}]", *clrs)
        print(f"  {label}  {_c(km['kit_name'], C.WHITE)}")


def print_summary_ipa(result: dict) -> None:
    conf_colors = {"high": (C.BOLD, C.GREEN), "medium": (C.BOLD, C.YELLOW), "low": (C.BOLD, C.RED)}
    conf_labels = {"high": "HIGH", "medium": "MED ", "low": "LOW "}
    print()
    print(f"  {_c('-' * 50, C.DRED)}")
    print(f"  {_c('SUMMARY  —  IPA', C.BOLD, C.WHITE)}")
    print(f"  {_c('-' * 50, C.DRED)}")
    print(f"  {_c('Bundle ID   :', C.CYAN)}  {result.get('bundle_id') or 'N/A'}")
    print(f"  {_c('App         :', C.CYAN)}  {result.get('app_name') or 'N/A'} v{result.get('version') or '?'}")
    print(f"  {_c('Min iOS     :', C.CYAN)}  {result.get('min_ios_version') or '?'}")
    print(f"  {_c('Frameworks  :', C.CYAN)}  {len(result['frameworks'])} ({len(result['unmapped_frameworks'])} unmapped)")
    print(f"  {_c('Kit matches :', C.CYAN)}  {_c(str(len(result['kit_matches'])), C.BOLD, C.WHITE)}")
    print(f"  {_c('Permissions :', C.CYAN)}  {len(result['permission_matches'])} / {len(result['permissions'])} matched")
    print()
    for km in result["kit_matches"]:
        conf  = km["confidence"]
        clrs  = conf_colors.get(conf, (C.RESET,))
        label = _c(f"[{conf_labels.get(conf,'???')}]", *clrs)
        print(f"  {label}  {_c(km['kit_name'], C.WHITE)}")