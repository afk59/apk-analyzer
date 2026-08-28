# 0005 — One analysis per subprocess

**Date:** 2026-08-28 · **Status:** accepted

## Context

v1's `run_batch` analyses every file in one long-lived process. On the maintainer's machine
(15.8 GB RAM) that does not survive the 43-app corpus. Measured over several weeks:

- Four consecutive `--batch` runs died at three different points — HSBC mid-`AnalyzeAPK` twice,
  and `com.foodgulu` once after hanging **6 h 11 min**. `com.foodgulu` had completed fine in
  earlier runs, so the failure follows the process, not the file.
- A runner spawning a fresh `python` per APK did the same 26 apps in **17 min** that `run_batch`
  took **40 min** to do, then finished the rest: **42/43 apps, 0 failures.** Later runs did the
  full corpus in ~29 minutes.
- `hk.com.hsbc.hsbchkmobilebanking.apk` alone went from "37 minutes, sometimes fails" to
  **17.3 min** when nothing else had been analysed in that process first.

The cause is androguard: `AnalyzeAPK` builds the full DEX cross-reference graph in memory, cost
tracks method count rather than file size, and the memory is not returned within the process.

## Decision

`app/services/jobs.py` spawns **one subprocess per input file** (`python -m app.worker <path>`).
The worker analyses, writes its outputs, prints JSONL progress to stdout, and exits.

## Consequences

- Each analysis starts on a clean heap and returns its memory to the OS on exit.
- A crash or a kill costs only the file in flight; everything already written stays.
- Progress must cross a process boundary, so it is a line protocol on stdout rather than a
  callback. This is a feature: the worker cannot corrupt the UI process.
- Skip files whose outputs already exist, so an interrupted run resumes cheaply.
- The worker must set UTF-8 stdio. v1 fixed exactly this (`_force_utf8_stdio`) after a run lost
  11 of 26 apps to a `UnicodeEncodeError` on a CJK app name when stdout was a pipe — and in v2
  stdout is **always** a pipe.

## Known operational note, carried from v1

The HSBC worker historically did **not** exit after finishing: it wrote its outputs, printed its
completion line, then lingered holding 8–11 GB. Everything started afterwards ran 2–3× slower.
The JobRunner must therefore treat "outputs written" as completion and reap the child with a
timeout, rather than waiting indefinitely for it to die on its own.
