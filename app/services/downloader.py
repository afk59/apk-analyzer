"""Fetch an APK by package name. M4 in ROADMAP.md, rationale in decisions/0006.

THE ONLY new network code in v2. Isolated exactly like engine/core/play_meta.py:
nothing else here opens a socket, this module imports nothing from the engine,
and it never raises -- every failure becomes a state on the download row.

CONTRACT

    Source(Protocol):
        name: str
        def resolve(package: str) -> Candidate | None     # metadata, no bytes
        def download(c: Candidate, dest: Path) -> Path

    fetch(package, dest_dir) -> Result(state, path|None, source|None, error|None)

    Sources are tried in order and the first that resolves wins. A source that
    raises is logged and skipped, never fatal.

VERIFY WHAT ARRIVED -- all three, before the file reaches the engine

    1. It is really an APK: the ZIP contains classes.dex AND AndroidManifest.xml.
       Otherwise it is a split bundle (APKM/XAPK), an HTML error page saved with
       a .apk name, or a stub. v1's corpus held exactly this case and it
       analysed to nothing while LOOKING analysed.

    2. The manifest package equals the package that was requested. v1's corpus
       contains two files that are the wrong app entirely -- one is Aptoide, one
       is Uptodown, both store apps saved instead of the target -- and every
       conclusion drawn about those two apps was really about a store app.
       Automating the download makes this MORE likely, not less.

    3. Record source and resolved version, so any result can be traced back to
       where its binary came from.

EXPECTATIONS

    * Every adapter is HTML scraping of a third-party mirror. They change markup
      without notice. A dead source is routine maintenance, not an incident --
      the same standing caveat v1 records for google-play-scraper.
    * A failure must name which sources were tried. "failed" alone sends someone
      to read logs that do not exist.
    * Availability is best-effort. Enterprise, internal and delisted apps are
      not on public mirrors, just as 2 of 43 corpus apps are on no Play
      storefront in any region.
    * Downloads land in engine/input/, which is gitignored. Binaries never enter
      the repository.
    * Only for apps the team is authorised to analyse; mirrors carry their own
      terms of use.
"""
