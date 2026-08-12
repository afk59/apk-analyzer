# Native mapping backlog

Pool entries that the OHPM review (Phase 2D) found are covered by a **native
`@kit.*`**, not by an ohpm package. They are recorded here rather than written,
because they belong in `mapping.json` and deserve a dedicated native round with
its own verification pass — not a drive-by append during an OHPM slice.

**Nothing in this file has been written to `mapping.json` yet.**

Every kit token below was confirmed against `src/data/reference/hmos_api_index.json`
by looking up a distinctive method name — the same discipline as the Sprint 10/12
mapping rounds. The "attested by" column is the index key that resolved it; where
an `import` statement is quoted, it appears verbatim in the index.

`N` = number of APKs in the 41-app batch whose `Common Unmapped` sheet contains
the namespace (union across the listed namespaces).

## Slice 1 (2026-08-12)

| Android namespace(s) | Capability | Native kit | Attested by | N |
|---|---|---|---|---|
| `android.service.media.MediaBrowserService` | Media session / MediaBrowser | `@kit.AVSessionKit` | `createAVSession`, `setAVMetadata` → `import { avSession } from '@kit.AVSessionKit'` | 16 |
| `com.learnium.RNDeviceInfo`, `dev.fluttercommunity.plus.device_info` | Device info (model/os/uuid) | `@kit.BasicServicesKit` | `import { deviceInfo } from '@kit.BasicServicesKit'` | 14 |
| `cl.json`, `dev.fluttercommunity.plus.share` | Social share sheet | `@kit.ShareKit` | `SharedData` → `import { systemShare } from '@kit.ShareKit'` | 11 |
| `com.wix.reactnativenotifications`, `com.dieam.reactnativepushnotification`, `app.notifee` | Local notifications | `@kit.NotificationKit` | `addSlot`, `requestEnableNotification` → `import { notificationManager } from '@kit.NotificationKit'` | 11 |
| `com.reactnative.ivpusic.imagepicker`, `com.imagepicker`, `com.reactnativecommunity.cameraroll`, `com.dmcbig.mediapicker` | Image picker / camera roll | `@kit.MediaLibraryKit` | `photoAccessHelper`, `PhotoSelectOptions` | 10 |
| `org.apache.commons.codec`, `.io`, `.logging` | Base64 / digest / IO utils | `@kit.ArkTS` + `@kit.CryptoArchitectureKit` | `Base64Helper`, `encodeSync` → `import { util } from '@kit.ArkTS'`; `createMd` → `import { cryptoFramework } from '@kit.CryptoArchitectureKit'` | 10 |
| `com.zoontek.rnpermissions`, `com.hjq.permissions` | Runtime permission request | `@kit.AbilityKit` | `verifyAccessToken`, `checkAccessToken` → `import { abilityAccessCtrl } from '@kit.AbilityKit'` | 9 |
| `io.invertase.firebase.messaging` | FCM push messaging | `@kit.PushKit` | kit token present in `KIT_DOC_URLS` | 9 |
| `com.reactnativecommunity.netinfo`, `dev.fluttercommunity.plus.connectivity` | Network connectivity state | `@kit.NetworkKit` | `hasDefaultNet`, `getNetCapabilities`, `createNetConnection` → `import { connection } from '@kit.NetworkKit'` | 8 |
| `net.lingala.zip4j`, `com.rnziparchive` | Zip / archive compression | `@kit.BasicServicesKit` | `compressFile`, `decompressFile` → `import { zlib } from '@kit.BasicServicesKit'` | 7 |
| `org.greenrobot.eventbus` | Pub/sub event messaging | `@kit.BasicServicesKit` | `import { emitter } from '@kit.BasicServicesKit'` | 7 |
| `io.invertase.firebase.analytics` | Analytics events | `@kit.AnalyticsKit` | existing `mapping.json` precedent (kit already in use) | 7 |

### Two of these correct earlier decisions — do not re-cut them

- **`android.service.media` → `@kit.AVSessionKit`.** Sprint 10 left it unmapped
  with the note *"AVSession is the likely target but the exact kit token could
  not be confirmed against the index"*. It is now confirmed: `createAVSession`
  and `setAVMetadata` both resolve to `import { avSession } from '@kit.AVSessionKit'`.
- **`com.learnium.RNDeviceInfo` → `@kit.BasicServicesKit`.** Sprint 12 cut it
  because `@ohos.deviceInfo` was absent from the index and a search for
  `deviceinfo` surfaced only `remoteDevice` from `@kit.NearLinkKit`. That search
  used the wrong token: `import { deviceInfo } from '@kit.BasicServicesKit'`
  **is** attested verbatim. Only the individual property names (`productModel`,
  `osFullName`, `udid`) are unindexed, which is normal — the index keys on method
  names, not properties.

## Slice 2 (2026-08-12)

Native-first routed **24 of 29** reviewed capabilities away from OHPM in this slice — including
six that were expected to be third-party ports (barcode, JSON, logging, PDF, icon fonts,
cookies). Only 3 OHPM mappings survived.

| Android namespace(s) | Capability | Native kit | Attested by | N |
|---|---|---|---|---|
| `com.journeyapps.barcodescanner`, `com.dcloud.zxing2`, `org.reactnative.barcodedetector` | Barcode / QR scan | `@kit.ScanKit` | `import { detectBarcode } from '@kit.ScanKit'`; also `generateBarcode`, `scanCore` | 6 |
| `com.alibaba.fastjson` | JSON serialization | `@kit.ArkTS` | `ArkTSUtils` parse/stringify; plus the JS builtin `JSON` | 6 |
| `com.rnbiometrics`, `com.rnfingerprint` | Biometric / fingerprint auth | `@kit.UserAuthenticationKit` | `import { userAuth } from '@kit.UserAuthenticationKit'` — `getUserAuthInstance`, `UserAuthType`, `AuthParam` | 6 |
| `com.oblador.vectoricons` | Icon font rendering | `@kit.ArkUI` | `registerFont`, `SymbolGlyph`, `fontFamily` | 6 |
| `com.oblador.keychain` | Secure keystore / keychain | `@kit.UniversalKeystoreKit` | `import { huks } from '@kit.UniversalKeystoreKit'` — `generateKeyItem`, `importKeyItem`, `exportKeyItem` | 5 |
| `com.github.barteksc`, `com.shockwave.pdfium`, `org.wonday.pdf` | PDF rendering | `@kit.PDFKit` | `import { pdfService } from '@kit.PDFKit'` — `PdfDocument`, `loadDocument` | 5 |
| `com.rnfs` | File system read/write | `@kit.CoreFileKit` | `import { fileIo } from '@kit.CoreFileKit'` — `openSync`, `readSync`, `mkdirSync`, `listFileSync` | 5 |
| `com.facebook.crypto`, `com.facebook.android.crypto` | Conceal encrypted storage | `@kit.CryptoArchitectureKit` | `import { cryptoFramework } from '@kit.CryptoArchitectureKit'` — `createCipher`, `createSymKeyGenerator`, `doFinal` | 5 |
| `org.reactnative.maskedview` | Masked view overlay | `@kit.ArkUI` | `Mask`, `maskShape` | 5 |
| `org.slf4j` | Logging facade | `@kit.PerformanceAnalysisKit` | `import { hilog } from '@kit.PerformanceAnalysisKit'` — `debug`, `isLoggable` | 4 |
| `com.lwansbrough.RCTCamera`, `org.reactnative.camera`, `com.google.android.cameraview` | Camera capture | `@kit.CameraKit` | `import { camera } from '@kit.CameraKit'` — `getSupportedCameras`, `createPreviewOutput` | 4 |
| `com.reactnativecommunity.cookies` | Cookie management | `@kit.ArkWeb` | `import { webview } from '@kit.ArkWeb'` — `configCookieSync`, `fetchCookieSync`, `saveCookieAsync` | 4 |
| `com.reactnativecommunity.checkbox` | Checkbox control | `@kit.ArkUI` | `Checkbox`, `CheckboxGroup` | 4 |
| `com.jakewharton.processphoenix`, `com.reactnativerestart` | App restart | `@kit.ArkTS` / `@kit.AbilityKit` | `process.exit`; `terminateSelf` | 4 |
| `android.credentials`, `android.service.credentials` | Credential Manager (passkeys/autofill) | `@kit.BasicServicesKit` — **UNCERTAIN** | `appAccount.getCredential` — see caveat below | 4 |
| `com.henninghall.date_picker` | Date picker | `@kit.ArkUI` | `showDatePickerDialog`, `DatePickerOptions` | 3 |
| `com.reactnativecommunity.toolbarandroid` | Toolbar | `@kit.ArkUI` | `Toolbar` | 3 |
| `com.scwang.smartrefresh` | Pull-to-refresh | `@kit.ArkUI` | `Refresh` | 3 |
| `org.devio.rn` | Splash screen | `@kit.ArkUI` | `window.setWindowLayoutFullScreen` | 3 |
| `com.reactnativecommunity.geolocation` | Geolocation | `@kit.LocationKit` | `import { geoLocationManager } from '@kit.LocationKit'` — `getCurrentLocation` | 3 |
| `com.calendarevents` | Calendar events | `@kit.CalendarKit` | `import { calendarManager } from '@kit.CalendarKit'` — `getCalendarManager`, `addEvent` | 3 |
| `com.caverock.androidsvg` | SVG rendering | `@kit.ImageKit` / `@kit.ArkGraphics2D` | `svg tags` → ImageKit; `buildFromSVGString` → ArkGraphics2D | 3 |
| `com.brentvatne`; `androidtranscoder` | Video player; transcoding | `@kit.MediaKit` | `media.createAVPlayer`; `media.createAVTranscoder` | 3 ea |
| `org.altbeacon` | iBeacon / BLE ranging | `@kit.ConnectivityKit` | `import { ble } from '@kit.ConnectivityKit'` — `startBLEScan`, `createGattClientDevice` | 3 |
| `net.time4j` | Date/time + timezone | `@kit.LocalizationKit` | `import { i18n } from '@kit.LocalizationKit'` — `getTimeZone`, `getCalendar` | 3 |
| `com.google.android.odml` | On-device ML | `@kit.MindSporeLiteKit` | `import { mindSporeLite } from '@kit.MindSporeLiteKit'` — `loadModelFromFile`, `runStep` | 3 |
| `com.drew` (EXIF half) | Image EXIF read/write | `@kit.ImageKit` | `getImageProperty`, `getImagePropertySync`, `modifyImageProperty` | 3 |
| `dev.fluttercommunity.plus.wakelock` | Screen keep-awake | `@kit.BasicServicesKit` | `import {runningLock} from '@kit.BasicServicesKit'` — `RunningLockType` | 2 |
| `dev.fluttercommunity.plus.packageinfo` | Package/version info | `@kit.AbilityKit` | `import { bundleManager } from '@kit.AbilityKit'` — `getBundleInfoForSelf`, `getBundleInfo` | 2 |

> The last two rows exhaust the mappable pool: after slice 2 there are **zero** unreviewed
> capabilities left in the `Common Unmapped` demand list. See CLAUDE.md for the closing tally.

### Two rows the native round must NOT accept on trust

- **`org.slf4j` → `@kit.PerformanceAnalysisKit` is a rough fit, not an equivalence.** `hilog`
  is a *platform log sink*; SLF4J is a **pluggable-backend logging facade** whose whole purpose
  is that the application binds a backend (logback, log4j, …) at deploy time. HarmonyOS has no
  facade/binding layer, so an app leaning on SLF4J's appenders, MDC or per-logger levels will
  need real rework, not a symbol swap. Map it, but do not mark it `high`.
- **`android.credentials` → `@kit.BasicServicesKit` is UNCONFIRMED.** `appAccount.getCredential`
  is *app account* credential storage; Android's Credential Manager is passkey/WebAuthn plus
  password autofill. Parity was **not** established — no passkey or autofill API was found in
  the index. Re-check this properly in the native round; leaving it unmapped is preferable to a
  wrong row. Same disposition as `android.service.media` had before Sprint 2D confirmed it.

### Notes for whoever runs the native round

- `@kit.AVSessionKit` and `@kit.ShareKit` are **not** in `KIT_DOC_URLS`
  (`core/mapping.py`), joining `@kit.ArkTS`, `@kit.LocalizationKit` and
  `@kit.MediaLibraryKit` on that list. Rows using them render without an
  "Official Docs" anchor — cosmetic, not a broken link, but worth fixing all of
  them together at some point.
- `org.apache.commons` splits across two kits (util vs cryptoFramework), so it
  cannot be a single prefix row; `.codec` and `.io`/`.logging` need separate
  entries.
- Several of these prefixes are broader than the namespaces actually observed.
  Check for shadowing against existing `mapping.json` entries before appending,
  the way the Sprint 12 round did (it measured 0 shadowed rows).
