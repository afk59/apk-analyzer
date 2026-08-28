# 0003 — `engine/` is inherited from v1 and behaviour-frozen

**Date:** 2026-08-28 · **Status:** accepted

## Context

The maintainer's first constraint for v2 was: *"bunu yaparken rule'larımızı mappinglerimizi
kaybetmeyeceğiz"* — the rules and the mappings must not be lost. Those are not incidental assets.
`mapping.json` is 279 grounded rows built over four review rounds; `ohpm_mapping.json` is 15 more;
the engine carries a long tail of hard-won corrections (reproducibility, conservative confidence,
obfuscation filters, packed-DEX honesty) that a rewrite would silently drop.

## Decision

v1's `src/` was moved to `engine/` **unchanged** and is treated as inherited, behaviour-frozen
code. All v2 code lives in `app/`. `app/` imports `engine/`; **`engine/` imports nothing from
`app/`.**

The move was a directory rename only. Internal imports (`core.mapping`, `ui.terminal`) and data
path resolution (`Path(__file__).parent / "data"`) are all relative to that directory, so nothing
inside changed. Verified by running `python engine/analyzer.py <apk>` from the new location and
getting a report.

## Why a rename rather than a restructure

A cleaner package layout (`analyzer/core/`, `analyzer/data/`) was considered and rejected for now.
It would touch every import and every path constant in ~7,100 lines that have **zero automated
tests**, in exchange for aesthetics. The `engine/` ⟷ `app/` split already gives the legibility
that mattered: one directory is inherited and stable, the other is new.

## Consequences

- The v1 CLI keeps working and stays supported: `python engine/analyzer.py <file>`. It is how a
  corpus gets re-run and how anything gets scripted.
- Changing `engine/` requires a written reproduction of a bug. "The UI would be easier if…" is not
  one; adapt in `app/`.
- The one-way import rule makes "the engine is unchanged" true by construction. This is the same
  device v1 used to keep `play_meta`, `ohpm_fetch` and `framework_detect` isolated, and it worked.
- If a restructure is ever wanted, it should follow a test harness, not precede one.
