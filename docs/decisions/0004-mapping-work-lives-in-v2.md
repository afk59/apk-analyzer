# 0004 — Mapping re-grounding happens only on `v2`

**Date:** 2026-08-28 · **Status:** accepted · **Decided by:** maintainer

## Context

`docs-ref/` makes it possible to re-ground every mapping decision against the SDK declarations and
the official docs, rather than against a generated method-name index. That is a large body of work
and it changes `engine/data/mappings/*.json` — a file that `main` also ships.

Two options were put to the maintainer: develop mappings on `main` so live work benefits
immediately and v2 inherits them, or keep all of it on `v2`.

## Decision

**All mapping work happens on `v2`.** `main` is frozen except for bug fixes.

## Consequences

- No merge conflicts on `mapping.json`: exactly one branch edits it.
- Active engagements keep running v1 with `mapping.json` v1.10.0 / 279 rows until v2 is stable.
  This is the accepted cost, and it is the maintainer's call, not a technical constraint.
- If something urgent is found — a mapping that is actively *wrong*, not merely absent — that is a
  bug fix and may go to `main` on its own. Additions do not qualify.
- When v2 stabilises, `v2` merges forward and carries the mappings with it.

## Note for whoever merges

`main` and `v2` have diverged structurally: `src/` → `engine/`, and v1's `CLAUDE.md`,
`OTURUM_2026-08-20.txt`, `MAPPING_CANDIDATES_2026-08-20.md` and `NATIVE_CANDIDATES.md` moved under
`docs/v1/`. A bug fix cherry-picked from `main` into `v2` will need its path adjusted. Nothing was
deleted — every v1 document is present, only relocated.
