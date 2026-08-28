# 0002 — SQLite as an index over file outputs, not as the output

**Date:** 2026-08-28 · **Status:** accepted · **Decided by:** maintainer

## Context

The UI needs to list past runs, show per-app cards, filter, and eventually compare two runs of the
same app. v1 stores everything as files: one HTML report and one agent JSON per app, plus two
workbooks per batch. Answering "show me every app under 60% coverage" means opening 43 JSON files.

## Decision

A single SQLite file, `app/store/analyzer.db`, holding `runs` / `apps` / `artifacts` /
`downloads`. `sqlite3` is in the standard library, so this adds no dependency and no install step.

**The database is an index. The files remain the deliverable.** Every column is derivable from an
artifact on disk, and deleting the database must be recoverable by a rescan of `result/`.

## Why not JSON

It is the honest alternative and it is what v1 does. Rejected because every list screen becomes a
hand-written scan over every file, and the interesting v2 features — history, comparison, download
state — are exactly the ones that want a query rather than a scan. JSON also has no answer for the
downloader's queue, which has mutable per-package state.

## Consequences

- Nothing that exists *only* in the database may ever become a business output. If a number
  matters, it is in the report or the workbook first.
- `coverage_pct` / `coverage_status` are read from `engine.core.renderer.coverage_status()`, which
  v1 extracted precisely so the report and the workbook could not disagree. The database is a
  third consumer of that same function, never a fourth implementation.
- Paths are stored relative to the repo root, so moving or sharing the folder does not orphan the
  index.
- Schema changes are applied on open, forward-only, and the rescan path is the safety net: if a
  migration is ever wrong, delete the file and rebuild.
