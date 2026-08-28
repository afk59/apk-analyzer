# Mapping discipline

These rules produced v1's 279 native rows and 15 OHPM rows with **zero shadowing across every
slice**. They are not style preferences — each one exists because breaking it produced a wrong
row that had to be found later. Read this before touching any mapping file.

**A wrong mapping is worse than an honest gap.** A gap tells a migrator to investigate. A wrong
row tells them the work is done.

---

## The gate every proposed row must pass

1. **Native first.** Check whether a native `@kit.*` already covers the capability. If it does,
   no OHPM row may be written. In OHPM slice 1 this disqualified 12 of 21 reviewed capabilities;
   in slice 2, 24 of 29 — including six that were confidently expected to be third-party ports
   (barcode, JSON, logging, PDF, icon fonts, cookies) and are all native.

2. **Match on function, never on name.** `com.google.api.HttpRule` contains "Http" and is a
   protobuf message class. `org.jsoup.helper.HttpConnection` belongs to an HTML parser. Of 123
   unmapped namespaces containing "http", fewer than half were HTTP clients.

3. **Ground it, verbatim.** The row must be backed by an attested import or declaration —
   `docs-ref/ArkTS-Harmonyos-apis-and-kits/kits/@kit.X.d.ts` first, then
   `api/@ohos.*.d.ts`, then `hmos_api_index.json`, then the docs corpus. Record the evidence in
   the row's `note`. See `DOCS_REF_GUIDE.md`.

4. **`NOT FOUND` means unconfirmed, not nonexistent.** Two v1 cuts were reversed for exactly this
   (`android.service.media`, `com.learnium.RNDeviceInfo`), and `@kit.ScanKit` was nearly written
   off as having no native path because its methods are indexed under other names. With the SDK
   `.d.ts` corpus now available this excuse is largely gone — but the principle stands.

5. **Does the native API do the layer's *core* work, or only carry it?** This is the test that
   cut `org.altbeacon`: `ble.startBLEScan` is transport, while AltBeacon is a beacon *protocol*
   with no counterpart. The same test *kept* `org.slf4j` → `hilog`, where the core work (logging)
   is native and only the pluggable-backend facade is missing. Partial parity is `medium` with
   the missing half named in the note — never `high`, and never silence.

6. **Popularity never overrides function.** `@ohos/photoview` (popularity 364) beat
   `@rv/image-preview` (1300) because the latter is a lightbox gallery, not a zoomable ImageView.

7. **Existence-check before writing an OHPM row.** The registry returns **HTTP 200** for a
   missing package, with `body` degrading from an object to the literal string `"success"`.
   Existence is `isinstance(body, dict)` and nothing else. This caught a real error:
   `@hw-agconnect/core` does not exist.

8. **Record what you rejected and why.** Every round that skipped this re-proposed the same
   candidates. `okio` and `bolts` were cut in Sprint 10 with no recorded reason and came back two
   rounds later; nobody could say whether the original cut had been right.

---

## Mechanics

- **Append-only.** Never modify or reorder an existing entry. Bump `version`; `last_updated` is
  `YYYY-MM`.
- `harmony_import` is the **kit token**, not the import line. The verbatim import goes in `note`.
  (278 of 279 rows follow this; `android.renderscript` is a pre-existing exception.)
- Matching is **longest-prefix-first, break on first match**. A new sub-prefix under an existing
  entry changes nothing — `com.facebook.react` already swallows `com.facebook.react.views.*`.
  Check this before proposing a row, or you will propose a no-op.
- OHPM rows live in `ohpm_mapping.json` under the key `ohpm_mappings` with `tier: "ohpm"`, so
  they can never be loaded into the native matcher by accident. They carry `install_cmd`, not
  `harmony_import` — an OHPM package has no import statement.
- HMS gets far fewer rows than HMOS, structurally: an HMS app is still an Android app, so Java/RN/
  Flutter libraries run unchanged there and mapping them would falsely imply migration work. Only
  a Google service with a real Huawei counterpart qualifies.

## Measure it, before and after

Every v1 mapping round predicted its effect and then confirmed it. Do the same.

1. **Predict:** replay the real match loop (`ns_mappings` sorted longest-first, break on first
   match) over the per-app sheets of `batch_unmapped.xlsx`, old mapping vs old+new. Produce:
   distinct namespaces absorbed · per-app row instances absorbed · `Common Unmapped` rows
   absorbed · **rows shadowed by a pre-existing entry**.
2. **Confirm:** run the real engine and compare.

> **"Shadowed" has a precise meaning.** It counts rows where a *new* prefix wins **and** an old
> prefix would also have matched — i.e. the new row duplicates or overrides existing coverage. It
> is not "rows already matched by pre-existing entries", which is simply prior coverage;
> measuring it that way returns a large number that says nothing about the round.

Expect the prediction to land exactly. In v1 it did, every time: 141/141, 425/425, 264/264.

## Confidence

`high` / `medium` / `low`, and a kit's badge is the **minimum** across all rows feeding it —
weakest contributor wins, because this is a migration *risk* tool. Cost measured over the corpus:
high 821 → 554, medium 358 → 570, low 40 → 95. That looks worse and is more honest.

Use `medium` when the capability exists natively but not as a drop-in, and name the missing half
in the note. Use `low` when the target is plausible but the shape genuinely differs.
