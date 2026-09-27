"""Fetch an APK by package name. Rationale in docs/decisions/0006.

THE ONLY new network code in v2. Isolated exactly like engine/core/play_meta.py:
nothing else here opens a socket, this module imports nothing from the engine,
and it never raises -- every failure becomes a Result with a reason attached.

    fetch("com.example.app", dest_dir, on_progress) -> Result

Sources are tried in order and the first that resolves wins. A source that
raises is recorded and skipped, never fatal, and the failure names every source
that was tried -- "failed" alone sends someone looking for logs that do not
exist.

WHAT IS VERIFIED BEFORE THE FILE IS HANDED ON

  1. It is really an APK: the ZIP contains classes.dex AND AndroidManifest.xml.
     Otherwise it is a split bundle, an HTML error page saved with a .apk name,
     or a stub. v1's corpus contained exactly that case and it analysed to
     nothing while LOOKING analysed.

  2. The manifest package equals the package that was requested. v1's corpus
     holds two files that are the wrong app entirely -- one is Aptoide, one is
     Uptodown, both store apps saved instead of the target -- and every
     conclusion drawn about those two apps was really about a store app.
     Automating the download makes that failure MORE likely, not less, so this
     check is mandatory and a mismatch is a hard failure.

A failed verification deletes the file. Leaving a wrong or truncated APK in the
input folder is how it ends up analysed by the next folder run.

NOTE ON EXPECTATIONS
Every adapter is a third-party mirror and will change without notice, the same
standing caveat v1 records for google-play-scraper. Availability is best-effort:
enterprise, internal and delisted apps are not on public mirrors, just as 2 of
43 corpus apps are on no Play storefront in any region. Use only for apps the
team is authorised to analyse; mirrors carry their own terms of use.
"""

import shutil
import urllib.error
import urllib.request
import zipfile
from dataclasses import dataclass, field
from pathlib import Path

_UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
       "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36")
_CONNECT_TIMEOUT = 20
_CHUNK = 256 * 1024


@dataclass
class Candidate:
    package: str
    url: str
    source: str
    size: int | None = None
    content_type: str | None = None


@dataclass
class Result:
    package: str
    state: str                      # ready | not_found | failed
    path: Path | None = None
    source: str | None = None
    version: str | None = None
    size: int | None = None
    error: str | None = None
    note: str | None = None         # e.g. "served as an App Bundle; ..."
    tried: list = field(default_factory=list)


class Unusable(Exception):
    """A source answered, but not with an APK and not with "no such app".

    Kept apart from None ("this source does not have it") because the two lead
    to opposite conclusions: a web filter's block page read as "not found"
    tells someone the app is missing when the network is the problem.
    """


def _describe(exc: Exception) -> str:
    if isinstance(exc, Unusable):
        return str(exc)
    return f"{type(exc).__name__}: {exc}"


def _request(url: str, method: str = "GET"):
    return urllib.request.Request(url, method=method, headers={
        "User-Agent": _UA,
        "Accept": "*/*",
    })


class ApkPure:
    """d.apkpure.com's direct endpoint. No HTML parsing, so nothing to break
    when they restyle the site -- and a missing package answers 404 outright.

    Requests /b/APK/ and never /b/XAPK/, which always serves a bundle.

    /b/APK/ does NOT guarantee a single APK. For some apps it does -- a 124 MB
    app that publishes both forms returned a real APK here -- but for one
    published as an App Bundle it returns the bundle at this path anyway
    (measured: com.foodgulu, 143.9 MB, base.apk plus 3 config splits). fetch()
    unwraps that case; see _extract_base.
    """

    name = "apkpure"

    def resolve(self, package: str):
        url = f"https://d.apkpure.com/b/APK/{package}?version=latest"
        try:
            with urllib.request.urlopen(_request(url, "HEAD"), timeout=_CONNECT_TIMEOUT) as r:
                if r.status != 200:
                    return None
                ctype = (r.headers.get("Content-Type") or "").lower()
                if "html" in ctype:
                    # Not "this source does not have it": a missing package is
                    # a 404 here. An HTML page is something in between -- most
                    # often a web filter or proxy block page, sometimes a
                    # mirror interstitial -- and the URL it ended up at is
                    # usually what says which.
                    raise Unusable(f"answered with an HTML page instead of an APK "
                                   f"(ended at {r.url}) - typically a web filter or "
                                   f"proxy block page, or a mirror interstitial")
                size = r.headers.get("Content-Length")
                return Candidate(package, url, self.name,
                                 int(size) if size and size.isdigit() else None, ctype)
        except urllib.error.HTTPError as exc:
            if exc.code == 404:
                return None
            raise
        return None


SOURCES = [ApkPure()]


def _download(candidate: Candidate, dest: Path, on_progress=None) -> Path:
    tmp = dest.with_suffix(dest.suffix + ".part")
    got = 0
    with urllib.request.urlopen(_request(candidate.url), timeout=_CONNECT_TIMEOUT) as r, \
            open(tmp, "wb") as fh:
        total = candidate.size
        if total is None:
            length = r.headers.get("Content-Length")
            total = int(length) if length and length.isdigit() else None
        while True:
            chunk = r.read(_CHUNK)
            if not chunk:
                break
            fh.write(chunk)
            got += len(chunk)
            if on_progress:
                on_progress(got, total)
    # Move into place only once the body is complete, so an interrupted
    # download can never be mistaken for a finished file by a later folder run.
    tmp.replace(dest)
    return dest


def _extract_base(path: Path):
    """A split bundle in, base.apk out. Returns (ok, note).

    APKPure's /b/APK/ endpoint does NOT always serve a single APK: for an app
    published as an App Bundle it hands over the bundle, and that is now the
    default on Play. Measured here on a 143.9 MB download that turned out to
    hold base.apk plus split_config.* members.

    Extracting base.apk is what v1's own notes prescribe for this shape, and it
    is not a degraded case in practice: 27 of the 43 apps in v1's corpus are
    base splits with no lib/ directory at all, which is exactly why
    framework_detect was built asset-first rather than around .so names.

    What IS lost is whatever lives only in the config splits -- native libraries
    and some resources -- so the caller reports it rather than quietly swapping
    the file.
    """
    try:
        with zipfile.ZipFile(path) as z:
            names = z.namelist()
            base = next((n for n in names if Path(n).name.lower() == "base.apk"), None)
            if base is None:
                # Some bundles name it after the package. Fall back to the
                # largest inner APK, which is the base in every layout seen.
                apks = [i for i in z.infolist() if i.filename.lower().endswith(".apk")]
                if not apks:
                    return False, "no inner .apk to extract"
                base = max(apks, key=lambda i: i.file_size).filename
            splits = [n for n in names
                      if n.lower().endswith(".apk") and n != base]
            blob = z.read(base)
    except Exception as exc:
        return False, f"could not read the bundle ({type(exc).__name__})"

    try:
        path.write_bytes(blob)
    except OSError as exc:
        return False, f"could not write base.apk ({exc})"

    note = (f"served as an App Bundle; analysed base.apk and omitted "
            f"{len(splits)} config split(s)")
    return True, note


def _is_bundle(names) -> bool:
    return ("AndroidManifest.xml" not in names
            and any(n.lower().endswith(".apk") for n in names))


def _verify(path: Path, package: str):
    """(ok, version, error). See the module docstring for why both checks exist."""
    try:
        with zipfile.ZipFile(path) as z:
            names = set(z.namelist())
    except Exception as exc:
        return False, None, f"not a readable ZIP ({type(exc).__name__})"

    if "AndroidManifest.xml" not in names:
        inner = [n for n in names if n.lower().endswith(".apk")]
        if inner:
            return False, None, (f"this is a split-APK bundle with {len(inner)} inner "
                                 f".apk file(s), not an APK")
        return False, None, "no AndroidManifest.xml - not an APK"
    if "classes.dex" not in names:
        return False, None, "no classes.dex - nothing to analyse"

    try:
        # loguru first: androguard logs the whole API-level table at DEBUG on
        # import, and here stdout is a protocol stream.
        try:
            from loguru import logger
            logger.remove()
        except ImportError:
            pass
        from androguard.core.apk import APK
        apk = APK(str(path))
        found = apk.get_package()
        version = apk.get_androidversion_name()
    except Exception as exc:
        return False, None, f"could not read the manifest ({type(exc).__name__})"

    if found != package:
        return False, None, (f"this file is {found!r}, not {package!r} - the mirror "
                             f"served a different app")
    return True, version, None


def fetch(package: str, dest_dir: Path, on_progress=None) -> Result:
    package = (package or "").strip()
    if not package or "/" in package or "\\" in package:
        return Result(package, "failed", error="Not a package name.")

    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = dest_dir / f"{package}.apk"
    tried = []
    # Sources that answered with something other than an APK or "not here".
    # While any exist, nothing has shown the app to be missing.
    problems = []

    for source in SOURCES:
        tried.append(source.name)
        try:
            candidate = source.resolve(package)
        except Exception as exc:
            problems.append(f"{source.name}: {_describe(exc)}")
            if on_progress:
                on_progress(None, None, problems[-1])
            continue
        if candidate is None:
            continue

        try:
            _download(candidate, dest,
                      (lambda got, total: on_progress(got, total, None)) if on_progress else None)
        except Exception as exc:
            _cleanup(dest)
            return Result(package, "failed", tried=tried,
                          error=f"{source.name}: download failed ({type(exc).__name__}: {exc})")

        # An App Bundle is a normal answer from this endpoint, not a failure --
        # it is simply how the app is published. Unwrap it before verifying, and
        # tell the caller, because the config splits do not survive.
        note = None
        try:
            with zipfile.ZipFile(dest) as z:
                bundle = _is_bundle(z.namelist())
        except Exception:
            bundle = False
        if bundle:
            if on_progress:
                on_progress(None, None, f"{package}: App Bundle - extracting base.apk")
            ok, note = _extract_base(dest)
            if not ok:
                _cleanup(dest)
                return Result(package, "failed", tried=tried, source=source.name,
                              error=f"{source.name} served an App Bundle and {note}")

        ok, version, why = _verify(dest, package)
        if not ok:
            # Deleted on purpose: a wrong or truncated APK left in the input
            # folder is one that gets analysed by the next folder run.
            _cleanup(dest)
            return Result(package, "failed", tried=tried, source=source.name,
                          error=f"{source.name} served a file that failed verification - {why}")

        return Result(package, "ready", path=dest, source=source.name,
                      version=version, size=dest.stat().st_size, tried=tried,
                      note=note)

    if problems:
        return Result(package, "failed", tried=tried,
                      error="No source gave a usable answer, so this does NOT show the "
                            "app is missing - " + "; ".join(problems))
    return Result(package, "not_found", tried=tried,
                  error=f"Not available from: {', '.join(tried)}. "
                        f"Enterprise, internal and delisted apps are often on no public mirror.")


def _cleanup(path: Path):
    for p in (path, path.with_suffix(path.suffix + ".part")):
        try:
            if p.exists():
                p.unlink()
        except OSError:
            pass
