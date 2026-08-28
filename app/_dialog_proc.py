"""A native dialog in a throwaway process. `python -m app._dialog_proc file|folder`

Prints the chosen absolute path on stdout, or nothing when cancelled.

WHY A SEPARATE PROCESS
    Both tkinter and pywebview want the GUI main thread, and ours is already
    owned by the webview window. Marshalling a dialog back onto it is possible
    but fiddly and platform-specific; spawning a process that owns its own main
    thread has no such problem, costs ~200 ms, and works identically whether the
    app is running in a webview window or as a fallback browser tab.

    This is the safety net. app/services/dialogs.py tries pywebview's own dialog
    first, because that one is parented to the app window.
"""

import sys


def main(argv: list[str]) -> int:
    kind = argv[0] if argv else "file"

    import tkinter as tk
    from tkinter import filedialog

    root = tk.Tk()
    root.withdraw()
    # Without this the dialog opens BEHIND the app window on Windows and looks
    # like a freeze. -topmost has to be set before the dialog is created.
    root.attributes("-topmost", True)

    if kind == "folder":
        path = filedialog.askdirectory(title="Select a folder to analyse")
    else:
        path = filedialog.askopenfilename(
            title="Select a file to analyse",
            filetypes=[
                ("Supported", "*.apk *.exe *.dll *.ipa"),
                ("Android APK", "*.apk"),
                ("Windows binary", "*.exe *.dll"),
                ("iOS IPA", "*.ipa"),
                ("All files", "*.*"),
            ],
        )

    root.destroy()
    if path:
        # stdout is a pipe here, so force UTF-8: a path under a CJK or Turkish
        # user folder is otherwise a UnicodeEncodeError under the locale
        # codepage, which is the same failure that cost v1 11 apps in one run.
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        print(path)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
