"""downloader: verification, bundle handling, and failure shapes.

Nothing here touches the network. The source adapter is stubbed, so these run
offline and cannot be flaky because a mirror is down -- and the failure paths
are what matters, since a mirror will be down eventually.
"""

import unittest
import zipfile
from pathlib import Path

from tests.support import IsolatedTest, SAMPLE_APK, requires_apk


class FakeSource:
    """Serves a prepared file instead of a mirror."""

    name = "fake"

    def __init__(self, payload: Path | None, raise_on_resolve=False):
        self.payload = payload
        self.raise_on_resolve = raise_on_resolve
        self.resolved = []

    def resolve(self, package):
        self.resolved.append(package)
        if self.raise_on_resolve:
            raise RuntimeError("mirror exploded")
        if self.payload is None:
            return None
        from app.services.downloader import Candidate
        return Candidate(package, "file://" + str(self.payload), self.name,
                         self.payload.stat().st_size, "application/octet-stream")


def with_source(dl, source):
    """Swap SOURCES and also the downloader used for the real fetch."""
    dl.SOURCES = [source]

    def fake_download(candidate, dest, on_progress=None):
        data = Path(candidate.url[7:]).read_bytes()
        dest.write_bytes(data)
        if on_progress:
            on_progress(len(data), len(data))
        return dest

    dl._download = fake_download


class TestNameValidation(IsolatedTest):

    def test_rejects_path_separators_and_blanks(self):
        from app.services import downloader as dl
        for bad in ("", "   ", "../../etc/passwd", "a/b", "a\\b"):
            r = dl.fetch(bad, self.config.INPUT_DIR)
            self.assertEqual(r.state, "failed", f"accepted {bad!r}")
            self.assertIn("package name", (r.error or "").lower())


class TestVerification(IsolatedTest):
    """_verify decides what may reach the engine. Every branch has a test."""

    def test_rejects_a_non_zip(self):
        from app.services import downloader as dl
        p = self.tmp / "x.apk"
        p.write_bytes(b"<html>404</html>")
        ok, _, why = dl._verify(p, "com.x")
        self.assertFalse(ok)
        self.assertIn("ZIP", why)

    def test_rejects_a_zip_with_no_manifest(self):
        from app.services import downloader as dl
        p = self.make_zip(self.tmp / "x.apk", {"readme.txt": b"hi"})
        ok, _, why = dl._verify(p, "com.x")
        self.assertFalse(ok)
        self.assertIn("AndroidManifest", why)

    def test_rejects_a_manifest_with_no_dex(self):
        from app.services import downloader as dl
        p = self.make_zip(self.tmp / "x.apk", {"AndroidManifest.xml": b"x"})
        ok, _, why = dl._verify(p, "com.x")
        self.assertFalse(ok)
        self.assertIn("classes.dex", why)

    def test_names_a_split_bundle_as_such(self):
        from app.services import downloader as dl
        p = self.make_bundle(self.tmp / "x.apk", splits=4)
        ok, _, why = dl._verify(p, "com.x")
        self.assertFalse(ok)
        self.assertIn("bundle", why)
        self.assertIn("5", why)          # base + 4 splits

    @requires_apk
    def test_accepts_a_real_apk_under_its_own_name(self):
        from app.services import downloader as dl
        from androguard.core.apk import APK
        pkg = APK(str(SAMPLE_APK)).get_package()
        ok, version, why = dl._verify(SAMPLE_APK, pkg)
        self.assertTrue(ok, why)
        self.assertIsNotNone(version)

    @requires_apk
    def test_rejects_a_real_apk_under_the_wrong_name(self):
        """A real APK of a DIFFERENT app must be rejected. Automating downloads
        makes that case more likely, not less."""
        from app.services import downloader as dl
        ok, _, why = dl._verify(SAMPLE_APK, "com.definitely.not.this")
        self.assertFalse(ok)
        self.assertIn("com.definitely.not.this", why)
        self.assertIn("different app", why)


class TestBundleExtraction(IsolatedTest):

    def test_extracts_base_apk_and_reports_the_splits(self):
        from app.services import downloader as dl
        p = self.make_bundle(self.tmp / "b.apk", splits=3)
        ok, note = dl._extract_base(p)
        self.assertTrue(ok)
        self.assertIn("3 config split", note)
        self.assertEqual(p.read_bytes(), b"P" * 5000)      # now the base itself

    def test_falls_back_to_the_largest_inner_apk(self):
        from app.services import downloader as dl
        p = self.make_zip(self.tmp / "b.apk", {
            "com.example.main.apk": b"B" * 900,
            "split_a.apk": b"S" * 10,
        })
        ok, note = dl._extract_base(p)
        self.assertTrue(ok)
        self.assertEqual(p.read_bytes(), b"B" * 900)

    def test_reports_a_bundle_with_nothing_to_extract(self):
        from app.services import downloader as dl
        p = self.make_zip(self.tmp / "b.apk", {"only.txt": b"x"})
        ok, note = dl._extract_base(p)
        self.assertFalse(ok)
        self.assertIn("no inner", note)

    def test_is_bundle_recognises_the_shape(self):
        from app.services import downloader as dl
        self.assertTrue(dl._is_bundle(["base.apk", "split_config.arm64.apk"]))
        self.assertFalse(dl._is_bundle(["AndroidManifest.xml", "classes.dex"]))
        self.assertFalse(dl._is_bundle(["readme.txt"]))


class TestFetchFlow(IsolatedTest):

    def test_not_found_names_every_source_tried(self):
        from app.services import downloader as dl
        src = FakeSource(None)
        with_source(dl, src)
        r = dl.fetch("com.nope", self.config.INPUT_DIR)
        self.assertEqual(r.state, "not_found")
        self.assertEqual(r.tried, ["fake"])
        self.assertIn("fake", r.error)

    def test_a_raising_source_is_skipped_not_fatal(self):
        from app.services import downloader as dl
        with_source(dl, FakeSource(None, raise_on_resolve=True))
        r = dl.fetch("com.x", self.config.INPUT_DIR)
        self.assertEqual(r.state, "not_found")       # skipped, not crashed

    def test_a_bad_payload_is_deleted_so_it_cannot_be_analysed_later(self):
        """A wrong or truncated APK left in input/ is one the next folder run
        picks up. Verification failure must clean up after itself."""
        from app.services import downloader as dl
        bad = self.tmp / "payload.bin"
        bad.write_bytes(b"not a zip at all")
        with_source(dl, FakeSource(bad))
        r = dl.fetch("com.x", self.config.INPUT_DIR)
        self.assertEqual(r.state, "failed")
        self.assertFalse((self.config.INPUT_DIR / "com.x.apk").exists())
        self.assertFalse((self.config.INPUT_DIR / "com.x.apk.part").exists())

    @requires_apk
    def test_a_good_payload_lands_and_verifies(self):
        from app.services import downloader as dl
        from androguard.core.apk import APK
        pkg = APK(str(SAMPLE_APK)).get_package()
        with_source(dl, FakeSource(SAMPLE_APK))
        seen = []
        r = dl.fetch(pkg, self.config.INPUT_DIR,
                     lambda got, total, note=None: seen.append((got, total, note)))
        self.assertEqual(r.state, "ready")
        self.assertEqual(r.source, "fake")
        self.assertIsNotNone(r.version)
        self.assertTrue(r.path.exists())
        self.assertTrue(any(g is not None for g, _, _ in seen), "no progress reported")

    @requires_apk
    def test_a_payload_for_the_wrong_package_is_rejected_and_deleted(self):
        from app.services import downloader as dl
        with_source(dl, FakeSource(SAMPLE_APK))
        r = dl.fetch("com.someone.elses.app", self.config.INPUT_DIR)
        self.assertEqual(r.state, "failed")
        self.assertIn("different app", r.error)
        self.assertFalse((self.config.INPUT_DIR / "com.someone.elses.app.apk").exists())

    def test_a_bundle_payload_is_unwrapped_and_the_loss_is_reported(self):
        from app.services import downloader as dl
        bundle = self.tmp / "bundle.bin"
        self.make_bundle(bundle, splits=2)
        with_source(dl, FakeSource(bundle))
        notes = []
        r = dl.fetch("com.x", self.config.INPUT_DIR,
                     lambda got, total, note=None: note and notes.append(note))
        # base.apk here is not a real APK, so verification still fails -- but the
        # UNWRAP must have happened first and been announced.
        self.assertTrue(any("App Bundle" in n for n in notes), notes)


if __name__ == "__main__":
    unittest.main()
