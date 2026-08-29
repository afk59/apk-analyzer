# Mapping round — 2026-08-30

`mapping.json` **v1.10.0 → v1.11.0**: namespaces **279 → 311 (+32)**, permissions
**38 → 67 (+29, and 3 corrected)**. Append-only for namespaces. Driven by the 43-app
HK/Macau corpus and grounded against `docs-ref/`.

Two things also changed outside the mapping file, both consequences of this round:
`_OHOS_PERM_CATALOGUE` in the engine had four permissions that do not exist, and
`KIT_DOC_URLS` gained the two kits these rows introduce.

---

## 1. The permission catalogue was recommending permissions that do not exist

Found while checking the corpus's 41 unmatched permissions. The gap suggester
(`_suggest_hmos_perm`) matches Android permission words against
`_OHOS_PERM_CATALOGUE`, and **four of that list's 47 entries are not HarmonyOS
permissions at all**:

| In the engine | Reality |
|---|---|
| `ohos.permission.READ_MEDIA_IMAGES` | an **Android** name; HarmonyOS uses `READ_IMAGEVIDEO` |
| `ohos.permission.READ_MEDIA_VIDEO` | same — `READ_IMAGEVIDEO` |
| `ohos.permission.READ_MEDIA_AUDIO` | same — `READ_AUDIO` |
| `ohos.permission.USE_BIOMETRIC` | the real name is `ACCESS_BIOMETRIC` |
| `ohos.permission.ACCESS_NFC` | the real name is `NFC_TAG` |

The first three were being suggested to migrators with **`high` confidence**,
because the keyword matcher scores an exact word overlap highest — so the report
was most confident exactly where it was most wrong. `READ_IMAGEVIDEO`,
`READ_AUDIO` and `ACCESS_BIOMETRIC` were already in the list, so three entries are
simply removed and `ACCESS_NFC` is corrected. 47 → 43, all attested.

**Three `permission_mappings` targets were wrong the same way** and are corrected
(this is a bug fix, with precedent in v1's `e208272`):

| Android | was | now |
|---|---|---|
| `RECEIVE_BOOT_COMPLETED` | `ohos.permission.RECEIVE_BOOT_COMPLETED` | `RECEIVER_STARTUP_COMPLETED` |
| `RECEIVE_SMS` | `ohos.permission.RECEIVE_MESSAGES` | `RECEIVE_SMS` |
| `PACKAGE_USAGE_STATS` | `ohos.permission.BUNDLE_ACTIVESTATE_CHANGED` | `BUNDLE_ACTIVE_INFO` |

### How a permission name is confirmed now

Three independent sources, **748 distinct names** between them:

| Source | Names | Notes |
|---|---|---|
| `engine/data/permissions/*.txt` | 132 | Curated lists with grant tiers. v1 filed these under "unreferenced — inert reference material"; they are in fact the authoritative catalogue. |
| `docs-ref/` crawled documentation | 82 | Partial — the full permission reference page was not crawled. |
| `docs-ref/ArkTS-*/**.d.ts` | **655** | The SDK's own `@permission` annotations. By far the richest source. |

> **No single source is sufficient.** `MANAGE_SECURE_SETTINGS`, `NOTIFICATION_CONTROLLER`
> and `GET_TELEPHONY_STATE` are absent from the txt lists and real in the `.d.ts`;
> `KEEP_BACKGROUND_RUNNING` is in the txt lists. Checking only one would have
> produced false negatives in both directions — the same trap as
> `hmos_api_index.json`.

## 2. Permission mappings: +29

An explicit mapping beats the keyword suggester, which is what makes these worth
adding — several of the suggestions it was producing were wrong.

**Android 13+ granular media** (`READ_MEDIA_IMAGES/VIDEO/AUDIO`, 5+3+2 apps) →
`READ_IMAGEVIDEO` / `READ_AUDIO`.

**`READ_MEDIA_VISUAL_USER_SELECTED`** (7 apps) → **no permission**. HarmonyOS's
photo picker returns a URI without one. The suggester was proposing
`MEDIA_LOCATION`, which is a different thing entirely.

**Vendor launcher badge permissions** — `com.huawei.android.launcher.permission.READ_SETTINGS`
and eight siblings, 11 apps each, the single most common unmatched permission in
the corpus. The suggester proposed `MANAGE_SECURE_SETTINGS` for all of them,
which is simply wrong: on HarmonyOS the badge is `setBadgeNumber`, an **API call
with no permission**. Nine rows now say so.

**Android 14 typed foreground services** (`FOREGROUND_SERVICE_LOCATION`,
`_MICROPHONE`, `_PHONE_CALL`, `_DATA_SYNC`, `_MEDIA_PLAYBACK`,
`_MEDIA_PROJECTION`) → all `KEEP_BACKGROUND_RUNNING`. HarmonyOS expresses this as
one permission plus a declared background mode; the underlying capability
permission is still required separately, which is why every row keeps its own
kit.

**Network and connectivity**: `CHANGE_NETWORK_STATE` (11 apps) →
`SET_NETWORK_INFO`; `CHANGE_WIFI_MULTICAST_STATE` → `SET_WIFI_INFO`;
`NEARBY_WIFI_DEVICES` → `GET_WIFI_INFO`; `BLUETOOTH_ADVERTISE` →
`DISCOVER_BLUETOOTH`. **Audio**: `MODIFY_AUDIO_SETTINGS` (11 apps) →
`MANAGE_AUDIO_CONFIG`, not the suggester's `READ_AUDIO`.

A new `grant_level` value, **`none`**, marks the "no permission needed" rows. The
renderer only counts `system_grant` / `user_grant` / `restricted`, so an unknown
value renders as an uncounted row — verified before use.

## 3. Namespaces: +32

### Expo — the largest single gap in the corpus (12 rows)

**223 unmapped namespaces across 22 module families**, and not one of them was
mapped. React Native's core was already fully covered (`com.facebook.react`
absorbs everything under it), so Expo was where the actual hole was.

Mapped **one module at a time**, not as a blanket `expo.` prefix, because a
blanket rule would also swallow the module *runtime* —
`expo.modules.kotlin` (37 ns), `core`, `adapters`, `interfaces`, `manifests`,
`structuredheaders`, `logbox`, `devlauncher` — which has no counterpart and must
stay visible as unmapped work.

| Module | Kit | Conf |
|---|---|---|
| `filesystem` (38 ns) | `@kit.CoreFileKit` | high |
| `location`, `notifications`, `webview`, `constants`, `keepawake`, `fetch` | LocationKit / NotificationKit / ArkWeb / BasicServicesKit / BasicServicesKit / NetworkKit | high |
| `taskManager` | `@kit.BackgroundTasksKit` | medium |
| `asset` | `@kit.LocalizationKit` (`resourceManager`) | medium |
| `font`, `splashscreen`, `systemui` | `@kit.ArkUI` | medium |

The mediums are all the same shape: the capability exists natively but not as a
drop-in. `expo.modules.taskManager` is `medium` because HarmonyOS splits one Expo
task definition across three mechanisms (transient tasks, a declared background
mode, and deferred `workScheduler` jobs).

**`expo.modules.updates` is deliberately left unmapped** (26 ns, 1 app): it is
OTA JavaScript bundle delivery. AppGallery Kit's in-app update is store-driven
and a different thing.

### HMS SDK — apps already using Huawei (7 rows)

Six corpus apps carry the HMS SDK. Where a kit exists the mapping is near 1:1:
`aaid`/`opendevice` → `@kit.PushKit`, `account` → `@kit.AccountKit`, `network` →
`@kit.NetworkKit`, `safetydetect` → `@kit.DeviceSecurityKit`, `analytics` →
`@kit.PerformanceAnalysisKit` (consistent with this file's existing
`com.google.firebase.analytics` row rather than `@kit.AnalyticsKit`).

> **The HMS SDK plumbing is deliberately NOT mapped** — `api`, `common`, `core`,
> `support`, `framework`, `utils`, `adapter`, `ui`, `update`, `stats`, `hatool`
> (7,144 methods between them). On HarmonyOS NEXT the kits are built into the
> system, so that whole layer *disappears*. There is no kit to point at, and
> inventing one would imply porting work where the honest answer is "this goes
> away".

### Three gaps closed by the documentation corpus (4 rows)

Proposed in `MAPPING_CANDIDATES_2026-08-29.md`, now written:

- `android.credentials` + `android.service.credentials` → `@kit.OnlineAuthenticationKit`
  (`medium` — Credential Manager splits three ways; see the row's note)
- `com.scottyab.rootbeer` → `@kit.DeviceSecurityKit` (`high`)
- `org.reactnative.facedetector` → `@kit.CoreVisionKit` (`high`)

All three rest on kits that have **no `.d.ts` in `kits/`** and are documented
only in the crawled docs — the reason `DOCS_REF_GUIDE.md` insists on searching by
capability rather than by kit token.

### The tail (9 rows)

`com.google.ads`, `com.google.android.ads`, `com.google.android.ump` →
`@kit.AdsKit`. `com.swmansion.worklets` → `@kit.ArkUI` (the runtime split out of
Reanimated, which was already mapped there). `com.facebook.webpsupport` →
`@kit.ImageKit` (`high` — WebP is decoded natively, so Fresco's shim has no
counterpart because it is not needed). `me.dm7.barcodescanner` → `@kit.ScanKit`,
`me.relex.photodraweeview` / `me.relex.largeimage` → `@kit.ImageKit`,
`me.relex.circleindicator` → `@kit.ArkUI` (Swiper has a built-in indicator),
`me.liolin.app_badge_plus` → `@kit.NotificationKit`.

## 4. `KIT_DOC_URLS`: 58 → 60, and every token now resolves

`@kit.DeviceSecurityKit` and `@kit.OnlineAuthenticationKit` were the only kits
used by `mapping.json` without a documentation link. **All 60 kit tokens in the
file now resolve.**

Both URLs are attested **verbatim inside `docs-ref/`** — links the crawler
preserved in the official pages, not slugs guessed from a directory path. That
matters because `developer.huawei.com` is an SPA returning an identical HTTP 200
shell for any slug, so a URL cannot be checked by fetching it.

## 5. Absorption — predicted

Measured by replaying the engine's real match loop (longest-prefix-first, break
on first hit) over the corpus's 12,030 unmapped rows, v1.10.0 vs v1.11.0:

| | predicted |
|---|---|
| distinct namespaces absorbed | **160** |
| per-app row instances absorbed | **249** |
| of those, appearing in ≥2 apps | 38 |
| **rows shadowed by a pre-existing rule** | **0** |
| new rules matching nothing in this corpus | **0** |

Heaviest: `expo.modules.filesystem` (38 ns), `android.service.credentials` (12),
`android.credentials` (10), `com.swmansion.worklets` (5 ns / 19 rows),
`com.facebook.webpsupport` (2 ns / 15 rows).

Every one of the 32 new rules matches something — no dead rows.

## 6. Absorption — confirmed

Real 43-app run through v2's own UI, 2026-08-30: **43/43 analysed, 0 failures,
55 minutes** (HSBC included, in sequence, no manual intervention).

| | predicted | actual |
|---|---|---|
| distinct namespaces absorbed | 161 | **161** ✓ |
| per-app row instances absorbed | 251 | **251** ✓ |
| rows shadowed by a pre-existing rule | 0 | **0** ✓ |
| namespaces covered by a new rule leaking back to unmapped | 0 | **0** ✓ |
| unexpected new namespaces | 0 | **0** ✓ |

Symmetric difference between the predicted and the actual absorbed sets: **zero**.

> **A measurement trap, recorded so it is not repeated.** The first comparison
> read 160/249 and disagreed with the run by one namespace. The engine was
> right and the *reader* was wrong: `batch_unmapped.xlsx` puts its header on row
> 1 and data from row 2, and the script had `min_row=3` — silently dropping the
> first data row of all 43 sheets. It only surfaced as a mismatch because the
> top row of one sheet differed between the two runs. Same family as v1's
> recorded openpyxl gotcha, where an empty-string namespace reads back as
> `None` and a naive filter drops a real row. **Read `batch_unmapped.xlsx` from
> row 2.**

### Corpus totals

| | v1.10.0 | v1.11.0 |
|---|---|---|
| `batch_unmapped.xlsx` rows | 12,072 | **11,821** |
| distinct unmapped namespaces | 8,284 | **8,123** |
| `Common Unmapped` | 1,769 | **1,731** |
| `Common Mapped` | 230 | **243** |
| `OHPM Matches` | 139 | 139 (unchanged — no OHPM rows added) |

Coverage across the 43: 54.3 % – 99.9 %, mean **86.3 %** over 39 rateable apps;
the other 4 are the packed ones and correctly show an em-dash. 1,270 kit matches
in total, 29.5 per app. Framework split unchanged: React Native 17, Flutter 9,
Native 8, uni-app 3, mPaaS 2, Unknown (packed) 2, Capacitor 1, Cordova 1.

`OHPM Matches` staying at exactly 139 is the expected result of adding no OHPM
rows, and a useful negative control: the native additions did not disturb the
second tier.
