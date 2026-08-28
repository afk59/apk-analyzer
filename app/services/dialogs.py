"""Native file and folder pickers. M1 in ROADMAP.md.

    pick_file(filters)  -> Path | None
    pick_folder()       -> Path | None

Primary implementation is pywebview's own dialog API, which parents the dialog
to the app window. Fallback is tkinter.filedialog -- standard library, so it
works even if pywebview could not start and we are running in a browser tab.

WHY THIS MODULE EXISTS AT ALL
    A browser's <input type="file"> gives file CONTENT, never a path, and there
    is no folder picker in it. The engine needs a real absolute path, and batch
    mode needs a directory. That single gap is what decided the whole stack
    (docs/decisions/0001) -- so this is not a convenience wrapper, it is the
    reason v2 is a local app.

NOTES
    * The dialog must run on the main thread on Windows. Called from a FastAPI
      handler it has to be marshalled, not invoked directly from the worker
      thread, or it deadlocks.
    * Return None on cancel. Cancel is not an error and must not surface as one.
    * Do not filter folders by content. A folder the user picked that contains
      nothing analysable is a message in the UI, not a rejected dialog.
"""
