# Mapping audit — 2026-08-30

Every row of every mapping file, checked against the reference corpora. Nothing
was taken on trust, including rows this project wrote itself.

**Result: 9 hallucinated values found and corrected. After the fix, all six
mapping files are clean.** The audit is now a permanent test, so this cannot
regress silently.

---

## Method

Four independent evidence sources, indexed once:

| Source | Covers | Caveat |
|---|---|---|
| `docs-ref/ArkTS-*/kits/@kit.*.d.ts` | **47** kit barrels | Authoritative for module→kit ownership, but only the OPEN SDK — closed kits are absent |
| `docs-ref/ArkTS-*/api/*.d.ts` | module declarations, `@permission` annotations | 655 permission names |
| crawled documentation | 96 kit tokens | The only place closed/HMS kits (ScanKit, PushKit, MapKit, PaymentKit) appear |
| `hmos_api_index.json` | 77 kit tokens | Keys on normalised method names; produces false negatives by construction, so it is consulted last |

**97 distinct kit tokens and 748 permission names** between them. A value is real
if **any** source attests it — absence from one proves nothing, which is the
mistake this project has had to correct twice already.

## What was wrong

### `@kit.AnalyticsKit` does not exist — 13 rows

The string **"AnalyticsKit" appears nowhere in the 110 MB corpus.** Not as a kit
token, not as a word, in any of the four sources.

It was used by:

- `mapping.json` ×3 — `com.google.android.datatransport`, `com.facebook.appevents`,
  `com.adjust.sdk`
- `ios_mapping.json` ×10 — FirebaseAnalytics, FirebaseCore, AdjustSDK,
  AppsFlyerLib, Branch, Mixpanel, Amplitude, Segment, GoogleAppMeasurement(+IdentitySupport)
- `KIT_DOC_URLS` ×1, pointing at an **HMS product page** — a different platform

Two things should have caught it earlier. The rows' own notes said the target was
"AGConnect Analytics", which is an **ohpm package**, not a `@kit.*`. And v1's
comment beside the doc URL already admitted no HarmonyOS page for it could be
confirmed — the link was kept anyway.

**All 13 now point at `@kit.PerformanceAnalysisKit`** (`hiAppEvent`), which is
where HarmonyOS's app-event facility lives (19 doc files) and where this same
file already routed `com.google.firebase.analytics` for exactly this reason. The
three `mapping.json` notes were rewritten with the real import, and
`com.adjust.sdk` now states plainly that **attribution has no native counterpart**
— only its event-logging half ports.

### `@kit.RelationalStoreKit` does not exist — 3 rows

`ios_mapping.json`: Realm, RealmSwift, FMDB. `relationalStore` is exported by the
**`@kit.ArkData`** barrel — `kits/@kit.ArkData.d.ts`, the most authoritative
source there is for module ownership. Corrected.

### Five iOS permission targets carried Android names

`ios_permission_mapping.json`, never audited since v1.0.0 in June:

| iOS key | was | now |
|---|---|---|
| `NSPhotoLibraryUsageDescription` | `READ_MEDIA_IMAGES` | `READ_IMAGEVIDEO` |
| `NSPhotoLibraryAddUsageDescription` | `WRITE_MEDIA_IMAGES` | `WRITE_IMAGEVIDEO` |
| `NSVideoSubscriberAccountUsageDescription` | `READ_MEDIA_VIDEO` | `READ_IMAGEVIDEO` |
| `NSAppleMusicUsageDescription` | `READ_MEDIA_AUDIO` | `READ_AUDIO` |
| `NSHealthUpdateUsageDescription` | `WRITE_HEALTH_DATA` | `HEALTH_DATA` |

The first four are the same Android-name confusion the engine's suggester had:
HarmonyOS groups images and video under one permission.

`WRITE_HEALTH_DATA` is different and worth stating precisely: **there is no
write-specific health permission.** The corpus has `HEALTH`, `HEALTH_DATA`,
`READ_HEALTH_DATA` and `READ_HEALTH_MOTION`, all annotating `@ohos.sensor` reads.
The row now points at the attested `HEALTH_DATA` rather than an invented name;
a migrator writing health data goes through Health Service Kit's own APIs.

`NSUserTrackingUsageDescription` also had `kit: @kit.AnalyticsKit`. Its
permission, `APP_TRACKING_CONSENT`, annotates `@ohos.identifier.oaid` — the
advertising identifier — so the kit is **`@kit.AdsKit`**.

## What was already correct

Everything else, which is worth recording because it is most of the product:

- `mapping.json` — 311 namespace rows, 67 permission rows: every remaining kit
  token and every `ohos.permission.*` target attested
- `hms_mapping.json` — 137 rows, 48 kits: clean
- `win_mapping.json` — 92 rows, 27 kits: clean
- `ohpm_mapping.json` — 15 rows, 11 packages: **all present in the registry
  cache**, which matters because the registry answers HTTP 200 for a missing
  package and existence is `isinstance(body, dict)` and nothing else
- `_OHOS_PERM_CATALOGUE` — 43 permissions, all attested (after the earlier fix)
- `KIT_DOC_URLS` — 59 entries after removing the phantom, all real

## v1.10.0 → v1.11.0 on the corpus, app by app

The v1.11.0 run compared against the archived v1.10.0 run, per app, from the
agent JSON:

| | |
|---|---|
| kit types **added** | 4 — `@kit.DeviceSecurityKit` (5 apps), `@kit.OnlineAuthenticationKit` (4), `@kit.AdsKit` (1), `@kit.CoreVisionKit` (1) |
| kit types **lost** | **0** |
| confidence changed | 3 rows |
| OHPM counts changed | 0 |
| framework detections changed | 0 |
| permission gaps closed | 29 distinct permissions |

**No kit disappeared from any app.** That is the property that matters: adding
rows must never remove a result.

The three confidence changes are the min-confidence policy working as designed —
a kit's badge is its weakest contributor, and each of these gained a `medium`
contributor:

| App | Kit | | Caused by |
|---|---|---|---|
| `app.hkbus` | `@kit.LocalizationKit` | high → medium | `expo.modules.asset` (medium) |
| `app.hkbus` | `@kit.BackgroundTasksKit` | high → medium | `expo.modules.taskManager` (medium) |
| `com.foodgulu` | `@kit.NotificationKit` | high → medium | `me.liolin.app_badge_plus` (medium) |

The 12 permissions still unmatched are all vendor- or app-specific and correctly
have no HarmonyOS counterpart: `DOWNLOAD_WITHOUT_NOTIFICATION`,
`com.hihonor.push.*`, `MODIFY_PHONE_STATE`, `READ_PRIVILEGED_PHONE_STATE`,
app-private permissions like `com.mpsaps.cmoffice.PERMISSION_CALL`, and
`android.permission.write_settings` — which is a **lower-case typo in that app's
own manifest** and is left alone deliberately.

## The guard

Five tests in `tests/test_scenarios.py::TestMappingDataIntegrity` now run this
audit on every suite run:

- no mapping file may name a kit that no source attests
- no doc URL may describe a kit that does not exist
- every OHPM package must be in the registry cache
- every `ohos.permission.*` target in every mapping file must exist
- every permission the engine can suggest must exist

They skip cleanly when `docs-ref/` is absent (as on `main`), so the product
branch is unaffected.
