# Tests

```
python -m unittest discover -s tests -t .          # everything (~21 min)
python -m unittest tests.test_store                # one module
MA_SKIP_SLOW=1 python -m unittest discover -s tests -t .   # skip real analyses
MA_SKIP_UI=1   python -m unittest discover -s tests -t .   # skip the webview
```

No test dependency: plain `unittest`, which matters because adding one more
thing to `pip install` on a locked-down machine is exactly the friction this
project keeps avoiding.

## What each module covers

| Module | Covers |
|---|---|
| `test_config` | Path resolution and the `/api/open` guard — traversal, siblings sharing a prefix, device paths |
| `test_store` | Schema, cascade deletes, migration-by-rebuild, and **the rescan invariant** |
| `test_downloader` | Every verification branch, bundle extraction, failure shapes. **No network** |
| `test_jobs` | Queue order, per-file isolation, cancel, skip, reaping a worker that will not exit |
| `test_aggregate` | Cross-app aggregation, ERROR rows, set-based app counts, the offline path |
| `test_worker` | Input classification, stage mapping, side-car shape, one real analysis |
| `test_api` | Every endpoint against a **real server**, plus SSE to completion |
| `test_ui` | The page in a **real webview**: elements, handlers, panels, themes, JS errors |
| `test_parity` | The worker's artifacts vs the v1 CLI's, and engine determinism |
| `test_batch_features` | Program-folder batches (recursion, `.resources.dll`, combined mode, output-name collisions, resumed EXE rows — one run on real PE files), downloads overlapping analysis, deleting a result from disk/manifests/index |

## Isolation

Everything writes into a temp directory. `app/config.py` honours `MA_RESULT_DIR`,
`MA_DB_PATH` and `MA_INPUT_DIR`, and `tests/support.py` sets all three per test,
so a run can never touch real analysis output.

`ENGINE_DIR`, `WEB_DIR` and `DOCS_REF_DIR` are deliberately **not** redirectable:
they locate code and reference material, and a test that pointed them elsewhere
would be testing something other than this application.

> **`test_parity` is the one exception, by necessity.** The engine is frozen v1
> code that resolves `script_dir / "result"` from its own location and knows
> nothing about the environment, so comparing against the CLI means letting both
> sides write into `engine/result/`. That module backs up anything it would
> overwrite and restores it in `tearDown`, including on failure. Verified: the
> folder has the same contents before and after.

## Tests that need a real APK

A synthetic zip covers every shape check, but "this file really is package X"
needs a real binary `AndroidManifest.xml`, which cannot be faked cheaply. Those
tests look for the smallest APK in `engine/input/` or the sibling v1 checkout,
or `MA_TEST_APK`, and **skip** when there is none — a missing corpus is not a
broken build, and corpus binaries are gitignored.

## Bugs this suite found on its first run

Worth recording, because they are the argument for having it:

1. **The reap timeout was unreachable in the case it was written for.**
   `for line in proc.stdout` only ends when the child closes stdout, so a worker
   that announced its result and then lingered — the exact v1 shape where the
   heaviest file held 8–11 GB after finishing — blocked the reader forever and
   the timeout below never ran. Fixed by breaking on the terminal event.
2. **The worker ignored the configured result directory**, resolving
   `engine/result` directly, so every redirection was a lie and the suite would
   have written into real output.
3. **A file-handle leak per run** in the aggregate step: neither pipe was closed.
   Surfaced as a `ResourceWarning` under `-W error::ResourceWarning`.

## Writing a new test

Subclass `tests.support.IsolatedTest`. It gives you `self.tmp`, a reloaded
`self.config`, and fixture builders: `make_fake_apk`, `make_bundle`,
`make_report`, `make_agent_json`, `make_sidecar`, `make_zip`.

Prefer asserting the *contract* over the current output. `test_store` originally
asserted stored paths contained no backslash; that was wrong — the contract is
"relative when inside the repo, absolute otherwise, always resolvable", and the
test now says so.
