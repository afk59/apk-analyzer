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
