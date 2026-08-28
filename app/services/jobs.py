"""Job queue: spawns one worker subprocess per input file. M2 in ROADMAP.md.

CONTRACT

    JobRunner.submit(paths, target) -> run_id
    JobRunner.events(run_id)        -> iterator of dicts, for the SSE endpoint
    JobRunner.cancel(run_id)

BEHAVIOUR THAT IS NOT NEGOTIABLE, and why

    Sequential, one worker at a time.
        Parallelism is tempting and wrong here. androguard's peak commit on the
        heaviest corpus file was ~30 GB against 15.8 GB of RAM; two at once
        swaps the machine rather than halving the time. If this is ever
        revisited it needs a memory-aware scheduler, not a thread pool.

    Per-file isolation.
        A worker that dies takes only its own file with it. The run continues
        and records that file as failed, exactly as v1's batch loop does.

    Resume.
        Skip a file whose outputs already exist. An interrupted run then costs
        only the file in flight -- which is what made v1's per-process runner
        practical over a 43-app corpus.

    Reap with a timeout.
        Do not wait indefinitely for a child to exit. v1's heaviest file wrote
        all of its outputs, printed its completion line, and then LINGERED
        holding 8-11 GB while burning CPU; everything started afterwards ran
        2-3x slower until it was killed by hand. Treat "outputs written and
        done emitted" as completion, then terminate the child if it overstays.

    UTF-8 on the pipe.
        Spawn with encoding="utf-8" and errors="replace". stdout here is always
        a pipe, which is the exact condition under which v1 lost 11 of 26 apps
        to a UnicodeEncodeError on a CJK app name.

    Progress is forwarded, not invented.
        Parse the worker's JSONL and pass it on. Never synthesise a percentage
        from elapsed time: files in this corpus range from 1.8 s (packed) to
        1039 s (HSBC), so a clock-driven bar is wrong precisely when someone is
        watching it.
"""
