"""HTTP surface. Not implemented yet -- M1/M2/M3 in docs/ROADMAP.md.

The endpoint list is written down first because the frontend is built against
it and because two of these have security consequences.

    POST /api/pick?kind=file|folder     -> {"path": "C:/..."} | {"path": null}
        Opens a NATIVE dialog on the Python side and returns a real absolute
        path. This exists because a browser <input type=file> never yields one
        and there is no folder picker at all -- the reason v2 is a local app
        and not a web page (docs/decisions/0001).

    POST /api/open   {"path": "..."}    -> 204
        os.startfile(path). GUARDED: config.is_inside_result(path) must hold.
        The window will open whatever it is handed, so the refusal has to live
        server-side, and the path must be resolved before the check -- a naive
        prefix test passes "result/../../../something".

    POST /api/runs   {"input": "...", "target": "hmos"}  -> {"run_id": N}
        Queues one file or a whole folder. Returns immediately; the analysis
        happens in worker subprocesses. Never block the request thread.

    GET  /api/runs/{id}/events          -> text/event-stream
        SSE. Forwards the workers' JSONL progress, plus queue-level events
        (file n of m, cancelled, finished).

    POST /api/runs/{id}/cancel          -> 204
    GET  /api/runs                      -> run list
    GET  /api/runs/{id}                 -> run + its app rows + artifact paths
    POST /api/rescan                    -> rebuild the index from result/ alone
        The proof that the database is only an index (docs/decisions/0002).

    POST /api/downloads {"package": "com.foo"}  -> {"state": "queued"}
    GET  /api/downloads                 -> queue with per-package state
        Verify before analysing: real APK, and manifest package == requested.
        See docs/decisions/0006 -- the corpus already contains two files that
        are the wrong app entirely.

CONVENTIONS
    * Errors return a JSON body with a "detail" the UI can show verbatim. A
      download that fails must name which sources were tried; "failed" alone
      sends someone reading logs.
    * Nothing here computes coverage, confidence or matching. It calls the
      engine and passes results through.
"""

# Nothing is defined yet on purpose: this file is the contract the frontend and
# the JobRunner are written against. M1 fills it in.
