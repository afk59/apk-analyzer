# Mapping candidates from the 43-app batch — 2026-08-20

> **STATUS — this file is now a record, not a pending proposal.** Everything in the Tier A table
> below was reviewed and written into `mapping.json` as **v1.9.0** (263 → 271), and the round-2
> section appended at the end was written in as **v1.10.0** (271 → 279). `ohpm_mapping.json` is
> untouched at v1.1.0 / 15 rows. The "not proposed" tables are the part that stays live: they are
> there so the same candidates are not re-litigated in a later sweep.

Originally written as a proposal, in the same slice-and-review shape the Sprint 10 / 12 and
native-round work used.

Source: the 43-app run of 2026-08-20 — 13,299 unmapped rows across 43 APKs, ranked by how many
distinct APKs a namespace appears in, then collapsed onto a library root. Anything an existing
`mapping.json` / `ohpm_mapping.json` prefix already claims is excluded up front, so nothing
below is already covered.

Every row was grounded against `hmos_api_index.json` **before** being written, by both routes:
the normalized method key and — the technique that keeps earning its keep — a grep over the
index's `import_statement` values. Rows that could not be grounded are in "not proposed", not
in the table.

---

## First, the React Native question: `com.facebook.react` is ALREADY mapped

The obvious idea — "if an app ships a React Native button, can that not become an ArkUI
button?" — is already implemented, and at the only granularity the engine can act on:

```
com.facebook.react    -> @kit.ArkUI   (medium)
com.facebook.fbreact  -> @kit.ArkUI   (medium)
com.facebook.yoga     -> @kit.ArkUI   (medium)   # RN's flexbox layout engine
```

The matcher is **longest-prefix, break on first hit**, so `com.facebook.react.views.view`,
`...views.text`, `...views.scroll`, `...uimanager` and every other RN view package already
resolve to `@kit.ArkUI` through that one row. Adding `com.facebook.react.views.button` would
change **nothing** in the output — it would be shadowed by the existing prefix. (The absorption
run below confirms this shape: 0 shadowed rows means no proposed prefix duplicates existing
coverage.)

What is genuinely missing is **not a namespace row but component-level detail** — the report
tells a migrator "React Native → ArkUI" without saying which ArkUI component replaces which RN
one. That belongs in the row's `note` or a reference page, not in a new mapping entry:

| React Native | ArkUI |
|---|---|
| `View` | `Column` / `Row` / `Stack` / `Flex` |
| `Text` | `Text` |
| `Image` | `Image` |
| `ScrollView` | `Scroll` |
| `FlatList` / `SectionList` | `List` + `ListItem` / `ListItemGroup` |
| `TextInput` | `TextInput` / `TextArea` |
| `Switch` | `Toggle({type: ToggleType.Switch})` |
| `ActivityIndicator` | `LoadingProgress` |
| `Modal` | `CustomDialog` |
| `TouchableOpacity` / `Pressable` | `Button`, or any component plus `.onClick()` |
| `Animated` | `animateTo` / `@AnimatableExtend` |

> **These cannot be index-attested and must not be presented as if they were.** ArkUI containers
> are declarative built-ins, not imported APIs — a grep for `Flex` over the index's import
> statements returns **0**, exactly as it does for `Column` and `Row`. The table above rests on
> ArkUI documentation and on the precedent this repo already set with `com.facebook.yoga`, not
> on `hmos_api_index.json`. Anything written into a `note` should say so.

---

## Tier A — grounded, ready for review

`apps` = distinct APKs of 43. `rows` = per-app unmapped row instances the prefix would absorb.

| # | Android namespace | apps | rows | Proposed | Conf | Attestation in `hmos_api_index.json` |
|---|---|---|---|---|---|---|
| 1 | `okio` | 20 | 733 | `@kit.ArkTS` | medium | `import { buffer } from '@kit.ArkTS'` (60 entries); `util.encodeSync`/`decodeSync` for Base64 |
| 2 | `bolts` | 16 | 144 | `@kit.ArkTS` | medium | `import { taskpool } from '@kit.ArkTS'` (33 entries) |
| 3 | `com.facebook.widget.text` | 16 | 16 | `@kit.ArkUI` | medium | `import { MeasureText } from '@kit.ArkUI'` (3 entries) |
| 4 | `com.facebook.animated` | 13 | 25 | `@kit.ImageKit` | high | `createImageSource`, `getFrameCount`, `createPixelMap` → `import { image } from '@kit.ImageKit'` |
| 5 | `com.facebook.systrace` | 11 | 22 | `@kit.PerformanceAnalysisKit` | medium | `startTrace` / `finishTrace` → `import { hiTraceMeter } from '@kit.PerformanceAnalysisKit'` |
| 6 | `com.google.android.flexbox` | 5 | 5 | `@kit.ArkUI` | medium | none — precedent row, see note |
| 7 | `com.google.android.cameraview` | 3 | 3 | `@kit.CameraKit` | high | `createCameraInput`, `createPreviewOutput`, `getSupportedCameras` → `import { camera } from '@kit.CameraKit'` |
| 8 | `io.invertase.googlemobileads` | 1 | 13 | `@kit.AdsKit` | medium | `import { advertising } from '@kit.AdsKit'` (18 entries) |

### Notes that must travel with the rows

- **`okio` straddles three kits and the note has to say so.** Its core (`Buffer`, `ByteString`,
  `Source`/`Sink`, `Utf8`, `Base64`) is `buffer` + `util` from `@kit.ArkTS`; its filesystem half
  (`FileSystem`, `FileHandle`, `Path`, `ZipFileSystem` — 7 apps) is `fileIo` from
  `@kit.CoreFileKit`; its compression half (`GzipSource`, `GzipSink`, `DeflaterSink`,
  `InflaterSource`) is `zlib` from `@kit.BasicServicesKit` (`createGzip`, `inflate` both
  attested). One prefix can only carry one kit, so the dominant one wins and the other two go in
  the note — the shape `org.apache.commons.codec` already uses.
- **`okio` and `bolts` were both cut in Sprint 10**, listed there as "proposed and cut during
  review" with no recorded reason. They are re-proposed because (a) the grounding now exists and
  is verbatim, and (b) the accepted `org.apache.commons.io → @kit.CoreFileKit` row is the same
  shape: a Java utility library whose function is carried by a platform module. If the original
  cut had a reason that still stands, write it down this time so a third round does not
  re-propose them.
- **`bolts` is medium for a semantic reason, not as a confidence hedge.** Bolts `Task` is a
  continuation chain with cancellation tokens; `taskpool` is worker-thread dispatch and Promise
  is the chaining primitive. A migrator gets the capability but not a symbol swap — the same
  caveat already recorded for `org.greenrobot.eventbus` and `org.slf4j`.
- **`com.google.android.flexbox` has no index attestation and rests entirely on precedent.**
  It is Google's flexbox layout container; `com.facebook.yoga` — the same capability, RN's own
  flexbox engine — is already `@kit.ArkUI` medium. Consistent, but the note must state that the
  basis is precedent, exactly as `@kit.PushKit` on `io.invertase.firebase.messaging` does.
- **`io.invertase.googlemobileads` appears in one app only.** Included because it is an exact
  1:1 (Google Mobile Ads → Huawei Ads Kit) and 13 rows is not nothing. Drop it if the reviewer
  prefers a ≥2-app floor for the native tier.

### Predicted absorption — measure before, confirm after

Replaying the real match loop (longest-prefix-first, break on first hit) over all 13,299 rows
with these eight prefixes appended:

| Metric | Predicted |
|---|---|
| Row instances absorbed | **961** of 13,299 (7.2%) |
| Distinct namespaces absorbed | **100** |
| **Rows shadowed by a pre-existing rule** | **0** |

Heaviest per app: `app.hkbus` −72 rows, `com.ctm` −70, `com.foodgulu` −69, `hk.ust.staffapp` −69.
Confirm these numbers against real `analyze_apk` output before committing, as every previous
round did.

---

## Not proposed, and why — so nobody re-litigates them

These are the next-largest unmapped roots. Each is left alone deliberately; a wrong row is worse
than an honest gap.

| Namespace | apps | Why not |
|---|---|---|
| `org.conscrypt.Conscrypt` | 36 | JSSE provider internals; TLS is platform-managed. Standing decision from Sprint 10. |
| `com.google.firebase` (DI/telemetry) | 30 | `datatransport`, `events`, `heartbeatinfo`, `inject`, `platforminfo`, `tracing` are container plumbing. `FirebaseApp`/`FirebaseOptions` already route to the OHPM tier. |
| `android.security.NetworkSecurityPolicy` | 29 | Expressed as app configuration on HarmonyOS, not an API. |
| `com.facebook.common` | 27 | Heterogeneous Fresco utility grab-bag — no single kit is true for it. |
| `com.facebook.soloader` / `jni` / `hermes` | 18 / 17 / 16 | Build and runtime infrastructure. Hermes is the JS engine itself; an ArkTS rewrite has no counterpart. |
| `com.facebook.cache` / `datasource` / `binaryresource` / `memory` | 18 | Fresco pipeline plumbing, same category as above. |
| `com.facebook.infer` / `com.google.errorprone` | 18 / 17 | Compile-time annotations, zero runtime. |
| `android.system.ErrnoException` | 17 | POSIX errno wrappers. |
| `com.google.android.libraries` | 11 | The namespace key truncates at 4 segments, so the actual library is invisible. Cut in Sprint 12 for the same reason. |
| `io.invertase.firebase.common` / `utils` / `interfaces` | 12 / 12 / 7 | RN-Firebase bridge plumbing, not a capability. |
| `org.openjsse.javax` | 13 | JSSE internals — identical in kind to `org.conscrypt`. |
| `android.preference.PreferenceActivity` | 14 | A *UI* class; `@kit.ArkData` is the storage half and HarmonyOS has no preference-screen abstraction. Cut in Sprint 12. |
| `com.google.android.odml` | 4 | Image-container data type vs inference runtime — different layers. Cut in slice 2b. |
| `com.google.android.youtube` / `ump` / `finsky` | 2 / 2 / 2 | Vendor services with no HarmonyOS counterpart, or config-not-API. |

One candidate is genuinely open rather than cut: **`com.facebook.hermes.intl`** (part of the
16-app `com.facebook.hermes` root) is an ECMA-402 `Intl` implementation, and
`@kit.LocalizationKit` `intl` is a real counterpart. It is not proposed because the prefix that
would catch it also catches the Hermes engine internals, which do not port — splitting it needs
its own review.

---

## Method note

Ranking used the per-app unmapped rows straight out of the batch, not the `Common Unmapped`
sheet, so single-app namespaces stay visible — that is how `com.google.android.cameraview`
(923 methods across 3 apps) surfaced at all. 2,675 distinct library roots remain unmapped after
these eight; 65 of them appear in 10 or more apps, and the table above is what survived
grounding out of that 65.

---

# Round 2 — HTTP stacks and WebRTC — APPLIED as v1.10.0 (2026-08-20)

Unlike the Tier A table above, these were written straight into `mapping.json`
(**v1.9.0 → v1.10.0, 271 → 279**) after verification. Prompted by two direct questions: can the
`http`-bearing namespaces in `Common Unmapped` go to a network kit, and can WebRTC's audio go to
Media/Audio Kit.

## Verification of the Tier A rows already shipped in v1.9.0

Re-checked against `hmos_api_index.json` before adding anything new. **7 of 8 carry verbatim
attestation; 1 rests on precedent and says so in its own note.**

| Row | Attestation | Verdict |
|---|---|---|
| `okio` → `@kit.ArkTS` | `import { buffer } from '@kit.ArkTS'` ×60, `util.encodeSync` | confirmed |
| `bolts` → `@kit.ArkTS` | `import { taskpool } from '@kit.ArkTS'` ×33 | confirmed |
| `com.facebook.widget.text` → `@kit.ArkUI` | `import { MeasureText } from '@kit.ArkUI'` ×3 | confirmed |
| `com.facebook.animated` → `@kit.ImageKit` | `createImageSource`, `getFrameCount` → `image` | confirmed |
| `com.facebook.systrace` → `@kit.PerformanceAnalysisKit` | `startTrace`/`finishTrace` → `hiTraceMeter` | confirmed |
| `com.google.android.cameraview` → `@kit.CameraKit` | `createCameraInput`, `createPreviewOutput` | confirmed |
| `io.invertase.googlemobileads` → `@kit.AdsKit` | `import { advertising } from '@kit.AdsKit'` ×18 | confirmed |
| `com.google.android.flexbox` → `@kit.ArkUI` | **none — and none is possible** | precedent only |

## The eight new rows

`@kit.NetworkKit` is attested with `http` (58), `socket` (64), `webSocket` (24) and
`connection` (75). **`@kit.RemoteCommunicationKit` (`rcp`) is NOT in the index at all — zero
entries — so it was not used**, despite being the obvious modern answer for an HTTP client. If it
is real and simply missing from `hmos_api_index.json`, these rows should be revisited; the index
is not exhaustive, and NOT FOUND means unconfirmed, not nonexistent.

| Android namespace | apps | rows | Kit | Conf |
|---|---|---|---|---|
| `dc.squareup.okhttp3` | 3 | 90 | `@kit.NetworkKit` | high |
| `dc.squareup.okio` | 3 | 75 | `@kit.ArkTS` | medium |
| `io.ktor` | 1 | 30 | `@kit.NetworkKit` | medium |
| `com.mr.http` | 1 | 20 | `@kit.NetworkKit` | medium |
| `org.webrtc.Camera` | 2 | 18 | `@kit.CameraKit` | medium |
| `org.webrtc.audio` | 2 | 18 | `@kit.AudioKit` | medium |
| `org.springframework.http` | 4 | 12 | `@kit.NetworkKit` | medium |
| `org.apache.commons.httpclient` | 1 | 1 | `@kit.NetworkKit` | high |

`dc.squareup.*` is the DCloud/uni-app runtime's **shaded copy** of OkHttp and Okio — identical
APIs, renamed packages — so both simply follow their originals, which are already mapped.

**WebRTC is mapped by half, on purpose.** `org.webrtc` as a whole stays unmapped; only the two
sub-packages whose *own* core work has a native counterpart are claimed:

- `org.webrtc.audio` → `audio.createAudioCapturer` / `createAudioRenderer` /
  `get|setAudioEffectMode` (`@kit.AudioKit`) — microphone in, speaker out, AEC/NS.
- `org.webrtc.Camera*` → `camera.createCameraInput` / `createPreviewOutput` (`@kit.CameraKit`).

Everything else — `PeerConnection`, ICE/SDP negotiation, SRTP/DTLS, `RtpSender`/`RtpTransceiver`,
`DataChannel` — has no HarmonyOS counterpart and must be hand-rolled or replaced with a vendor
RTC SDK. This is the same test that **cut** `org.altbeacon` in slice 2b: map a layer only when
the native API does that layer's core work, not merely the transport underneath it. Measured on
`com.mpsaps.cmoffice`: 123 `org.webrtc` namespaces, 20 absorbed by the two new rows, **103 still
unmapped** — which is the honest picture.

The video codec path (`HardwareVideoEncoder`, `AndroidVideoDecoder`, `MediaCodecWrapper`) was
considered and **left unmapped**: neither `@kit.AVCodecKit` nor any `createVideoEncoder` /
`createVideoDecoder` key appears in the index.

## `http` in the name is not evidence — nine families rejected

The `Common Unmapped` sweep found **123 namespaces containing "http"**. Fewer than half are HTTP
clients.

| Family | apps | Why not |
|---|---|---|
| `com.google.api.Http`, `HttpRule`, `HttpBody`, `CustomHttpPattern` | 2 | **Protobuf message classes** from the googleapis annotations, not a client. `addAllRules`, `checkByteStringIsUtf8` are generated-code methods. |
| `freemarker.ext.servlet.Http*` | 1 | Server-side template-engine servlet models. Nothing on a device corresponds. |
| `io.grpc.okhttp.*` | 2 | gRPC's HTTP/2 transport. gRPC is an RPC framework over protobuf; NetworkKit gives you `http`/`socket`, not gRPC. "Swap to NetworkKit" would be wrong — you need a gRPC client. |
| `cn.jiguang.net.Http*` | 2 | JPush vendor SDK internals — standing decision on vendor SDKs. |
| `com.taobao.weex.http`, `io.dcloud.net.XMLHttpRequest` | 3 | Parts of cross-platform runtimes that do not port at all. (`dc.squareup.*` is different: a *stock library* that merely ships inside one.) |
| `anet.channel.*`, `anetwork.channel.*` | 1 | Alibaba networking-stack internals, vendor. |
| `org.jsoup.helper.HttpConnection` | 2 | jsoup is an HTML **parser**; its fetch helper is incidental. Mapping the parser to a network kit would be a category error. |
| `com.facebook.HttpMethod` | 4 | A four-value enum. |
| `com.egoo.sdk.http`, `com.allstar.http.*`, `com.android.api.http`, `util.http.*`, `com.growingio.android.okhttp3` | 1 each | Single-app vendor internals. |

`org.springframework` was mapped **only** at `.http`. Its `.core`, `.util` and especially
`.web.servlet` packages are general framework and server-side code and stay unmapped.

## Absorption — predicted, and confirmed on two real runs

| Metric | Predicted | Actual |
|---|---|---|
| Row instances absorbed | 264 of 12,338 (2.1%) | see below |
| Distinct namespaces absorbed | 129 | — |
| Rows shadowed by a pre-existing rule | 0 | **0** |

Two apps re-analysed end to end with the real engine:

| App | Unmapped before | after | Δ |
|---|---|---|---|
| `com.hopetrip.gzhkbus` | 350 | 292 | **−58** (predicted −58) |
| `com.mpsaps.cmoffice` | 164 | 144 | **−20** (predicted −20) |

`com.hopetrip.gzhkbus`'s `@kit.NetworkKit` now draws on six namespaces —
`dc.squareup.okhttp3`, `java.net`, `okhttp3`, `org.apache.http`, `org.apache.http.client`,
`org.springframework.http` — and `com.mpsaps.cmoffice` shows `@kit.AudioKit` fed by
`android.media.audiofx` + `org.webrtc.audio` and `@kit.CameraKit` by `android.hardware.camera2` +
`org.webrtc.Camera`.
