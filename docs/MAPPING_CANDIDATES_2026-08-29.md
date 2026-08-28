# Mapping candidates — 2026-08-29 (M5, first pass)

**Nothing here has been written to `mapping.json`.** This is a proposal for row-by-row review,
which is how every mapping round in this project has worked. `mapping.json` is still v1.10.0 /
279 rows.

## Why this pass exists

Every "no counterpart" verdict in v1 rested on `hmos_api_index.json`, where **NOT FOUND means
*unconfirmed*, not *nonexistent*** — a limitation v1 wrote down after two cuts had to be reversed
for exactly that reason. `docs-ref/` now makes the question answerable: 47 SDK `.d.ts` kit
declarations plus the crawled official documentation.

The first thing that pass found is that **the `.d.ts` set alone would have reproduced the same
mistake in a new form.** It covers only the open SDK. Every kit named below as a *new* answer is
absent from `kits/` and present in the docs corpus. Search order is in `DOCS_REF_GUIDE.md` and it
matters.

---

## 1. The six recorded "genuine gaps", re-tested

v1's closing tally listed six gaps left unmapped on purpose. Three now have a documented
counterpart, two are confirmed as real gaps, one is unchanged.

### 1.1 `android.credentials` / `android.service.credentials` — **counterpart found**

v1: *"No `passkey`/`webauthn`/`fido` in the index; only password autofill (`autoFillManager`).
Half of Credential Manager is not parity."*

The docs corpus has **passkey in 47 files, FIDO in 48, WebAuthn in 6**, and they belong to one
kit: `harmonyos-guides/system/security/online-authentication-kit` (7 files) and
`harmonyos-references/system/security/online-authentication-kit` (32).

> **`@kit.OnlineAuthenticationKit`** — attested 10× in those pages. *"Secure passwordless
> authentication … in compliance with the standards of FIDO, FIDO2, IIFAA and SOTER."*

Android's Credential Manager spans three things, and HarmonyOS now covers two and a half:

| Credential Manager | HarmonyOS |
|---|---|
| passkeys (FIDO2/WebAuthn) | `@kit.OnlineAuthenticationKit` |
| password autofill | `autoFillManager` (`@kit.AbilityKit`) — v1 already found this |
| federated sign-in | `@kit.AccountKit`, **Huawei ID only** |

**Proposed:** map at `medium`, with the note naming the split and the federated caveat. It is not
`high` because there is no single API that replaces `CredentialManager`; a migrator wires two kits
together, and the third-party federated case does not port at all.

### 1.2 `com.scottyab.rootbeer` — **counterpart found, and v1's reasoning was wrong**

v1: *"Zero OHPM hits, no native attestation API."* The second half does not hold.

> **`@kit.DeviceSecurityKit`**, SafetyDetect module: *"Checks whether the device environment is
> secure, for example, whether it has been jailbroken or is a non-real device."*
> (`harmonyos-guides/system/security/device-security-kit/about-this-kit`)

That is what RootBeer does, expressed as a platform service instead of a library of heuristics.

**Proposed:** map at `high` on function. Worth saying in the note that the shape inverts —
RootBeer runs local checks in-process, SafetyDetect is a device/server attestation with a token
and a nonce — so the migration is a redesign of the check, not a symbol swap.

### 1.3 `org.reactnative.facedetector` — **counterpart found; v1 checked the wrong kit**

v1: *"`@kit.VisionKit` offers only `interactiveLiveness` / `visionImageAnalyzer`, not face
landmarks."* True of `@kit.VisionKit` — but the face APIs are in a **different kit**, one v1's own
`KIT_DOC_URLS` comment already warns is easy to confuse with it.

> **`@kit.CoreVisionKit`** — attested 40× under `harmonyos-references/ai/core-vision-kit/`, which
> has `facedetector-face-detection/` and `facecomparator-face-verification/` as first-class API
> pages. "facial landmark" appears in 3 files.

**Proposed:** map at `high`. `@kit.CoreVisionKit` is already in `KIT_DOC_URLS`, so no doc-URL work
is needed.

### 1.4 `net.openid.appauth` / `com.rnappauth` — **gap CONFIRMED**

OAuth appears in 51 files, OpenID in 55, OIDC in 30 — and they are all **Huawei's own authorisation
server**: `account-kit/rest-apis` (16), `account-kit/sign-in` (5), `game-service-kit/rest-apis` (3),
`push-kit/rest-apis` (2). There is no generic OAuth2/OIDC client for arbitrary providers.

v1's judgement stands unchanged: hand-roll over `@kit.NetworkKit` + `@kit.ArkWeb`. **Leave unmapped.**

### 1.5 `org.altbeacon` — **gap CONFIRMED**

"beacon" appears in 5 files, "iBeacon" in 1, **"Eddystone" in 0**. No beacon protocol layer, exactly
as v1 concluded when it cut this row for being transport-only. **Leave unmapped.**

### 1.6 `com.google.android.odml` — **unchanged**

Not re-opened. v1 cut it because ODML is an image-*container data type* used with ML Kit while
`@kit.MindSporeLiteKit` is an *inference runtime* — a layer mismatch that documentation cannot
resolve. `visionImageAnalyzer` (6 files) is an analyzer, not a container type. **Leave unmapped.**

---

## 2. `@kit.RemoteCommunicationKit` — v1 asked for this revisit; my recommendation is **do not act**

v1 wrote, when mapping eight HTTP-client rows to `@kit.NetworkKit`:

> *"`rcp` was NOT used: the index attests it zero times… If `rcp` is real and merely absent from
> `hmos_api_index.json`, these rows deserve a revisit."*

**`rcp` is real.** `harmonyos-guides/system/network/remote-communication-kit/` documents it, and
the API is attested verbatim: `import { rcp } from '@kit.RemoteCommunicationKit'`,
`rcp.createSession(...)`, `session.get()`, `session.post()`, `session.close()`,
`rcp.UploadFromStream` / `rcp.DownloadToStream`, plus `import { urpc } from …` for RPC.

It affects **13 rows**, not 8 — `okhttp3`, `retrofit2`, `com.squareup.okhttp`,
`com.android.volley`, `com.loopj.android.http`, `cz.msebera.android.httpclient`,
`org.apache.http`, `org.apache.http.client`, `org.apache.commons.httpclient`,
`org.springframework.http`, `io.ktor`, `com.mr.http`, `dc.squareup.okhttp3`.

**Recommendation: change nothing.** Three reasons, in order of weight:

1. **Huawei says both are correct.** From Remote Communication Kit's own About This Kit:
   *"Compared with the HTTP request capability of Network Kit, Remote Communication Kit provides
   scenario-based APIs that are easier to employ… **You can select the kit that best suits your
   needs.**"* The existing rows are not wrong, and this project's rule is that a wrong row is worse
   than a gap — not that a defensible row should be traded for a differently defensible one.
2. **`mapping.json` is append-only.** "Never modify or reorder an existing entry" exists so the
   file stays auditable. Rewriting 13 rows for a preference would be the first exception, and a
   preference is the weakest possible reason to make one.
3. **The advantage is real but partial.** `rcp` is session-based — client object, base URL, PATCH,
   redirect control — which is the shape of OkHttp/Retrofit/Ktor. But `@kit.NetworkKit`'s `http`
   is not merely primitive: `http.HttpInterceptorChain` is attested, so interceptors exist on both
   sides. And `NetworkKit` is the right answer for the socket / WebSocket / connection-state half
   of that same code, which several of these libraries also touch.

**What I would do instead**, if you want the finding to reach a migrator: say it once, in the
report, not thirteen times in the mapping file. A single sentence under the `@kit.NetworkKit` kit
row — "for session-style HTTP clients, `@kit.RemoteCommunicationKit` (`rcp`) is the closer shape"
— costs no mapping churn and lands where it is read. That is a renderer change, and it needs your
call before I write it.

---

## 3. What this pass says about the method

- **The `.d.ts` corpus is necessary but not sufficient.** All three kits found above —
  `OnlineAuthenticationKit`, `DeviceSecurityKit`, `CoreVisionKit` — have **no `.d.ts` in
  `kits/`**. A rule of "absent from `kits/` means it does not exist" would have reproduced v1's
  index mistake exactly. `DOCS_REF_GUIDE.md` already states this; this pass is the evidence.
- **Two of the three reversals were caused by looking at the wrong token**, not by missing data:
  `@kit.VisionKit` instead of `@kit.CoreVisionKit`, and searching for capability words rather than
  for the kit that owns them. Searching the corpus by *capability* and then reading which kit the
  path belongs to was what worked.
- **Confirmations matter as much as reversals.** `net.openid.appauth` and `org.altbeacon` are now
  gaps that have been tested against the full documentation rather than an index — which is worth
  more than the original cut, and means they should not be re-proposed a fourth time.

## Next, once these are reviewed

The 1,771-row `Common Unmapped` pool has not been re-ranked yet. Doing that against the docs
corpus is the bulk of M5 and should follow the same shape: propose, measure absorption before and
after, confirm zero shadowing.
