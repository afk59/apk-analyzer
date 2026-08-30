# Migration Analyzer — v2

Analyses Android APKs, Windows EXE/DLLs and iOS IPAs and maps what they use onto
HarmonyOS NEXT kits. **v1 is the shipped CLI tool and stays in production on `main`.**
This branch adds a desktop UI, an APK downloader, a SQLite index and a documentation-grounded
mapping expansion — without touching the analysis engine's behaviour.

> **Start with `docs/HANDOFF.md`** — current state, the one unfinished item, and
> the rules that keep being re-learned. Then come back here.

> **This file is deliberately short.** v1's `CLAUDE.md` grew to 149 KB, and it was loaded in
> full at the start of every session. Detail lives in `docs/`, one file per concern, and you
> read only what the task needs. Keep it that way: when you finish a piece of work, append to
> the right `docs/` file — not here.

---

## Hard rules

1. **`engine/` is inherited and behaviour-frozen.** It is v1's analysis code, moved from
   `src/` unchanged. Change it only for a bug with a written reproduction, and never as a
   convenience for the UI. If the UI needs a different shape, adapt in `app/`, not in the engine.
2. **Never lose a mapping or a rule.** `engine/data/mappings/*.json` are the product. They are
   append-only, version-bumped, and every row is grounded before it is written — see
   `docs/MAPPING_DISCIPLINE.md`. A wrong mapping is worse than a gap.
3. **Outputs do not change.** The HTML reports and Excel workbooks v1 produces are what the
   business consumes. The UI *links to* them; it does not replace or reformat them.
4. **One analysis per subprocess.** `run_batch` in a single long-lived process does not survive
   a real corpus on this machine. See `docs/decisions/0005-process-isolation.md`.
5. **Network code is quarantined.** Only `engine/core/play_meta.py`, `engine/core/ohpm_fetch.py`
   and `app/services/downloader.py` may open a socket. Each must degrade to a placeholder and
   never raise.
6. **Ground every claim.** This project's whole value is that its mappings are checked, not
   guessed. `NOT FOUND` in an index means *unconfirmed*, never *nonexistent*.

## Where things are

| Path | What it is | Read when |
|---|---|---|
| `docs/HANDOFF.md` | **Read first.** State, what is unfinished, environment | Every session |
| `docs/ARCHITECTURE.md` | Module map, process model, SQLite schema, data flow | Touching `app/` |
| `docs/ROADMAP.md` | v2 milestones and their acceptance criteria | Starting any feature |
| `docs/MAPPING_DISCIPLINE.md` | The rules every mapping row must pass | Adding/changing a mapping |
| `docs/DOCS_REF_GUIDE.md` | How to use `docs-ref/` to ground a mapping | Adding/changing a mapping |
| `docs/decisions/` | Why the stack is what it is (ADRs) | Questioning a design choice |
| `docs/SESSION_LOG.md` | Running work log, Turkish, maintainer-facing | Start of a session |
| `docs/v1/ENGINE_REFERENCE.md` | v1's full 149 KB history — engine internals, every sprint | Debugging engine behaviour |
| `docs/v1/SESSION_LOG_2026-08-20.txt` | v1's Turkish work log | Chasing a v1 decision |
| `docs/v1/MAPPING_CANDIDATES_2026-08-20.md` | Mapping proposals **and rejections**, with reasons | Before re-proposing anything |
| `engine/` | v1 analysis code (frozen) + `data/` mappings + reference | |
| `app/` | v2 shell: FastAPI, pywebview, frontend, SQLite, downloader | |
| `docs-ref/` | HarmonyOS SDK `.d.ts` + official docs corpus (read-only) | Grounding a mapping |

## Running

```
run.bat                      # v2 desktop app
python -m app                # same thing, from a shell
python -m unittest discover -s tests -t .     # 169 tests, ~2.5 min
python engine/analyzer.py <file> --no-open    # v1 CLI, still works and still supported
```

**Run the tests before and after any change.** They found six real bugs on their
first runs, and five of them guard the mapping files themselves.

## Working agreements

- The maintainer works in **Turkish**; code, comments and commit messages are in **English**.
- **Raise bugs when you find them** rather than silently fixing them, and state what you
  measured rather than what you assume.
- Scope decisions are the maintainer's. Propose, then wait.
- A change that alters analysis output gets **its own commit**, separate from anything that
  claims to be output-neutral. v1 established this rule twice and both times it paid off.
