# 0006 — APK download by package name

**Date:** 2026-08-28 · **Status:** accepted · **Decided by:** maintainer

## Context

Getting an APK is currently manual: find it, download it, drop it in `input/`. For a migration
assessment covering dozens of apps that is most of the elapsed time. The request is to type a
package name and have the tool fetch and then analyse it.

## Decision

`app/services/downloader.py`, the only new network code in v2, isolated exactly like
`engine/core/play_meta.py`: nothing else opens a socket, it never raises, and every failure
degrades to a legible state rather than an exception.

Source adapters sit behind one interface and are tried in order. Each is HTML scraping of a
third-party mirror.

## What must be true of every download

**Verify what arrived, before it reaches the engine.** Three checks, all cheap:

1. It is a ZIP containing `classes.dex` **and** `AndroidManifest.xml` — otherwise it is a split
   bundle (APKM/XAPK), an HTML error page, or a stub. v1's corpus contained exactly this: a
   split bundle renamed `.apk` that analysed to nothing and looked analysed.
2. The manifest package matches what was requested. v1's corpus has **two files that are the
   wrong app entirely** — `com.macauwynn.android.apk` is Aptoide and `hk.edu.cityu.mobile.apk` is
   Uptodown, both store apps saved instead of the target. Every conclusion drawn about those two
   apps was actually about a store app. An automatic downloader makes this failure mode *more*
   likely, not less, so the check is mandatory.
3. Record the source and the resolved version in `downloads`, so a result can always be traced to
   where its binary came from.

## Consequences

- Mirrors change their markup without notice. Treat a source going dead as expected maintenance,
  not as an incident — the same standing caveat v1 records for `google-play-scraper`. Failures
  must name which sources were tried.
- Availability is best-effort. Enterprise, internal and delisted apps are simply not on public
  mirrors, exactly as 2 of 43 corpus apps are not on Google Play in any region.
- Use it only for apps the team is authorised to analyse. Third-party mirrors carry their own
  terms of use.
- Downloads land in `input/`, which is gitignored — binaries never enter the repository.
