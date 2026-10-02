# Mapping round — 2026-10-02

`mapping.json` **v1.11.1 → v1.12.0**: namespaces **311 → 326 (+15)**.
`ohpm_mapping.json` **v1.1.0 → v1.2.0**: **15 → 16 (+1)**.
`win_mapping.json` **v1.1.0 → v1.2.0**: **92 → 101 (+9)**. Permissions unchanged.
Append-only. Driven by apps this corpus did not contain, downloaded through the app's own new
batch downloader, and grounded against `docs-ref/` per `MAPPING_DISCIPLINE.md`.

## Source

Five packages fetched in one run (`org.wikipedia, com.shazam.android, de.danoeh.antennapod,
com.calm.android, com.duolingo`). Four analysed; Duolingo fails inside androguard (see the
session log — engine bug, not a mapping question). **1,219 distinct unmapped namespaces, 364
library roots** between the four.

Ranking was by library root across apps, then every root was put through the gate: already
covered by a prefix? recorded as rejected in an earlier round? native capability that does the
library's *core* work? attested verbatim?

## The rows

| Prefix | Kit | Conf | Evidence (path · symbol) |
|---|---|---|---|
| `coil` (covers `coil3`) | `@kit.ImageKit` | medium | `kits/@kit.ImageKit.d.ts` · `image`; same as `com.bumptech.glide` / `com.squareup.picasso` |
| `org.maplibre.android` | `@kit.MapKit` | medium | `harmonyos-guides/application-services/map-kit` · `import { map, mapCommon, MapComponent } from '@kit.MapKit'`; `…/tileoverlay`, `…/displaying-a-custom-map`; same as `com.mapbox` |
| `com.j256.ormlite` | `@kit.ArkData` | medium | `kits/@kit.ArkData.d.ts` · `relationalStore`; same as `androidx.room` |
| `com.orhanobut.hawk` | `@kit.ArkData` | medium | `kits/@kit.ArkData.d.ts` · `preferences` (encryption half named in the note) |
| `com.fasterxml.uuid` | `@kit.ArkTS` | medium | `api/@ohos.util.d.ts` · `generateRandomUUID` (v4 only) |
| `com.makeramen.roundedimageview` | `@kit.ArkUI` | high | `component/common.d.ts` · `borderRadius`, `border` |
| `com.wang.avi` | `@kit.ArkUI` | medium | `component/loading_progress.d.ts` · `LoadingProgress` |
| `com.skydoves.balloon` | `@kit.ArkUI` | medium | `component/common.d.ts` · `bindPopup` |
| `com.flaviofaria.kenburnsview` | `@kit.ArkUI` | medium | ArkUI `animateTo` on scale/translate |
| `dev.chrisbanes.snapper` | `@kit.ArkUI` | medium | `component/list.d.ts` · `scrollSnapAlign` |
| `it.xabaras.android.recyclerview` | `@kit.ArkUI` | medium | `component/list_item.d.ts` · `swipeAction` |
| `com.google.accompanist.pager` | `@kit.ArkUI` | high | `component/swiper.d.ts` · `Swiper` |
| `com.google.accompanist.flowlayout` | `@kit.ArkUI` | high | `component/flex.d.ts` · `wrap?: FlexWrap` |
| `com.google.accompanist.drawablepainter` | `@kit.ArkUI` | medium | `api/@ohos.arkui.drawableDescriptor.d.ts` · `DrawableDescriptor` (exported by `@kit.ArkUI`) |
| `jp.wasabeef.picasso` | `@kit.ArkGraphics2D` | medium | `api/@ohos.effectKit.d.ts` · `createEffect`, `blur`, `grayscale`, `setColorMatrix` |
| `io.getstream.photoview` (OHPM) | `@ohos/photoview` | high | fork of `com.github.chrisbanes.photoview`, same classes; registry existence re-checked (`isinstance(body, dict)`, with a negative control) |

Accompanist is mapped **per module**, the way Expo was: it is a grab-bag of Compose helpers, and
a blanket prefix would claim modules that have no single counterpart.

Prefixes are at most four segments, because the engine keys namespaces at four
(`apk_engine.py`, `ns_key = ".".join(parts[:4])`) and matches with `startswith`. A five-segment
prefix can never match. `coil` was checked to claim nothing but `coil.*` / `coil3.*` (335 rows
across both corpora, zero others).

## Rejected, and why

| Root | apps | Why not |
|---|---|---|
| `org.jsoup` | 2 | HTML **parser**. ArkTS's `xml` is XML-only; there is no native HTML DOM parser. (Its fetch helper was already rejected as a network row in v1.) |
| `com.google.re2j` | 2 | A regex engine. Regex is the language's own `RegExp`, not a kit, and RE2's linear-time guarantee has no counterpart. |
| `com.lyft.kronos` | 1 | SNTP client. No NTP API in the `.d.ts` or the docs corpus; `systemDateTime` reads the clock, it does not sync it. **Gap.** |
| `android.service.quicksettings` | 1 | Quick Settings tiles. No third-party control-centre tile API found in the docs. **Gap, unconfirmed** — re-check if the docs are re-crawled. |
| `org.maplibre.geojson` | 1 | GeoJSON data model. No kit does that job; `com.mapbox`'s blanket row is not a precedent worth repeating. |
| `jp.co.cyberagent.android` (GPUImage) | 1 | Key truncates at four segments, so the only usable prefix would claim every CyberAgent library. Also: live camera filter chains have no counterpart. |
| `app.rive` | 1 | Rive animation runtime — a renderer with its own file format. Lottie has an OHPM port; Rive does not. |
| `com.google.accompanist` (other modules) | — | Only `pager`, `flowlayout`, `drawablepainter` occur; nothing else is claimed. |
| `com.jayway.jsonpath`, `net.minidev.json` | 1 | JSONPath query language — no native counterpart; json-smart alone is too small to earn a row. |
| `com.datadog`, `com.amplitude`, `com.appsflyer`, `com.iterable`, `com.auth0`, `com.perimeterx`, `com.hcaptcha`, `com.spotify.sdk`, `com.apple.mediaservices`, `com.facebook.*` | 1 | Vendor SDKs — the standing decision. The vendor ships (or does not ship) a HarmonyOS SDK; no kit replaces their backend. |
| `org.jctools`, `org.reactivestreams`, `_COROUTINE`, `com.getkeepsafe.relinker`, `org.bytedeco.javacpp`, `org.objectweb.asm` | 1–2 | Infrastructure: concurrency primitives, interfaces, native-library loading, bytecode. |
| `com.google.api` / `rpc` / `type` / `longrunning` / `logging` / `cloud` | 1 | Protobuf message classes — standing decision from v1. |
| `com.google.androidbrowserhelper` | 1 | Trusted Web Activity / Custom Tabs launcher. ArkWeb is an in-app web view, a different thing. |
| `com.bytehamster.lib` | 1 | SearchPreference — a settings-screen UI with no HarmonyOS preference-screen abstraction (same reason `android.preference.PreferenceActivity` was cut in Sprint 12). |
| `org.conscrypt`, `android.security.NetworkSecurityPolicy`, `com.google.firebase` (plumbing) | 3–4 | Standing decisions, unchanged. |

## Absorption — predicted

Replay of the real match loop (longest-prefix-first, break on first hit) over the side-cars:

| | 4 new apps | 43-app corpus |
|---|---|---|
| distinct namespaces absorbed | **264** | **147** |
| row instances absorbed | **270** | **175** |
| rows shadowed by a pre-existing rule | **0** | **0** |
| new rules matching nothing | 0 | 12 (they come from the new apps) |

Heaviest: `coil` (165 ns in the new apps, 144 in the corpus — `com.ctm`, `com.foodgulu`,
`hk.com.hsbc.hsbchkmobilebanking`), `com.skydoves.balloon` (18 ns / 23 rows, 2 apps),
`org.maplibre.android` (19).

## Absorption — confirmed: NOT YET

The confirming re-run (the four new apps plus `com.ctm`, `com.foodgulu`, HSBC and Octopus,
through the app, under v1.12.0) was **stopped by the host before its first APK finished** — the
machine ran low on memory overnight and the session's background processes were reaped. It was
deliberately not restarted unattended.

What stands: the prediction is a replay of the engine's own loop (`apk_engine.analyze_apk` —
`ns_mappings` longest-first, `startswith`, break on first hit), the mapping-integrity tests pass,
and no new prefix touches a currently-mapped namespace. **What is owed: run those 8 APKs and
compare against the table above** before treating the APK half of this round as closed.

---

# Windows (`win_mapping.json`)

Source: ShareX's 316 binaries run as a program-folder batch, plus WinRAR. After the existing
92 rows, **17 distinct DLLs** stayed unmapped.

| DLL | Kit | Conf | Evidence |
|---|---|---|---|
| `gdiplus.dll` | `@kit.ArkGraphics2D` | medium | `api/@ohos.graphics.drawing.d.ts`; same as `gdi32.dll` |
| `msimg32.dll` | `@kit.ArkGraphics2D` | medium | `ShaderEffect.createLinearGradient` (`api/@ohos.graphics.drawing.d.ts`) |
| `windowscodecs.dll` | `@kit.ImageKit` | medium | `createImageSource`, `createImagePacker` (`api/@ohos.multimedia.image.d.ts`) |
| `usp10.dll` | `@kit.ArkUI` | medium | text engine + `@ohos.graphics.text`; same as `harfbuzz.dll`, `dwrite.dll` |
| `imm32.dll` | `@kit.IMEKit` | medium | `inputMethod.getController`, `attach` (`api/@ohos.inputMethod.d.ts`) |
| `winspool.drv` | `@kit.BasicServicesKit` | medium | `print.print(files)` (`api/@ohos.print.d.ts`, exported by the kit) |
| `shcore.dll` | `@kit.ArkUI` | medium | `display` `densityDPI` / `densityPixels` (`api/@ohos.display.d.ts`) |
| `avicap32.dll` | `@kit.CameraKit` | medium | `camera.getCameraManager` (`api/@ohos.multimedia.camera.d.ts`) |
| `uxtheme.dll` | `@kit.ArkUI` | **low** | `ThemeControl` / `CustomTheme`; owner-drawn theme parts genuinely differ |

**Not mapped, and why:**

| DLL | Why not |
|---|---|
| `mscoree.dll` (103 binaries) | The .NET runtime loader. There is no CLR on HarmonyOS; a .NET binary is a rewrite, and a kit row would say otherwise — same reasoning as Hermes. It is also the most common unmapped DLL in any .NET program folder, which is exactly why it must stay visible. |
| `perl532.dll`, `libgcc_s_seh-1.dll`, `libstdc++-6.dll`, `libwinpthread-1.dll` | Language runtimes bundled with exiftool / MinGW. Not capabilities. |
| `liblzma-5__.dll` | LZMA/xz. `zlib` in `@kit.BasicServicesKit` is deflate/gzip only. **Gap.** |
| `wintrust.dll` | Authenticode verification. Signature checks are the OS's job at install time; no app API. |
| `d3dcompiler_47_cor3.dll` | HLSL shader compiler. No counterpart. |
| `dwmapi.dll` | DWM frame and composition attributes. Window chrome is system-drawn; nothing to point at honestly. |

**Confirmed with the real engine** (`exe_engine.analyze_exe`, old mapping from git vs new, same
binaries): unmapped-DLL instances **166 → 155** over 319 binaries, plus `ffmpeg.exe` separately
(**2 → 0**, gaining `@kit.CameraKit`). Every one of the 9 rows matched something; no binary lost
a kit or gained an unmapped DLL. Windows matching is by exact DLL name, so shadowing cannot occur.

> **Seen in passing, not changed:** the existing `version.dll` row says
> "`@ohos.bundleManager` via BasicServicesKit", but `bundleManager` is AbilityKit. The Windows
> mapping has not had the audit `mapping.json` had on 2026-08-30. Worth doing.
