# Using `docs-ref/` to ground a mapping

`docs-ref/` is the reason v2 can do better than v1 at the one thing this tool is for. Read this
together with `MAPPING_DISCIPLINE.md`. It is **read-only, mapping-time only** — no runtime code
opens it.

## What is actually in there

| Source | Size | What it is |
|---|---|---|
| `ArkTS-Harmonyos-apis-and-kits/kits/@kit.*.d.ts` | **47 files** | Kit barrel declarations — which modules a kit re-exports. The authority on kit ownership. |
| `ArkTS-Harmonyos-apis-and-kits/api/@ohos.*.d.ts` | ~700 files | Real module declarations with real signatures. |
| `ArkTS-Harmonyos-apis-and-kits/component/`, `arkts/` | | ArkUI component and ArkTS language declarations. |
| `harmonos-official-docs-ref-and-examples/data/harmonyos-guides` | | How-to and conceptual docs, one `document.md` per page. |
| `…/harmonyos-references` | | API and kit reference pages. |
| `…/harmonyos-faqs` | | Errors, pitfalls, migration pain points. |

`…/AGENT_GUIDE.md` in the docs corpus states the intended search order. Follow it.

---

## The one caveat that will otherwise cost you a wrong "NO"

> **`kits/` holds only the 47 OPEN SDK kits. A kit missing from it is not a kit that
> does not exist.**

Verified: `@kit.ScanKit`, `@kit.PushKit`, `@kit.MapKit`, `@kit.PaymentKit`, `@kit.AccountKit`,
`@kit.IAPKit` and the rest of the closed / HMS-side kits have **no `.d.ts` here at all** — and
every one of them is real and documented in the docs corpus
(`harmonyos-guides/media/scan-kit`, `…/application-services/push-kit`, `…/map-kit`).

So the absence rule is: **`.d.ts` absent → check the docs corpus → only then say unconfirmed.**
This is the same failure mode as v1's `NOT FOUND` in `hmos_api_index.json`, which reversed two
cuts and nearly lost `@kit.ScanKit`. Do not rebuild it in a new form.

---

## Search order for "does kit X own API Y?"

1. **`kits/@kit.X.d.ts`** — if the kit is open SDK, this settles ownership outright. It lists the
   modules the kit re-exports; no keyword guessing.
2. **`api/@ohos.<module>.d.ts`** — the declaration itself: method names, parameters, return
   types, and whether the thing you need actually exists on it rather than something similarly
   named.
3. **`harmonyos-references/**/document.md`** — required for closed/HMS kits, which have no
   `.d.ts`; also the place to confirm a kit's real product name.
4. **`harmonyos-guides/**/document.md`** — for whether the capability exists *as a workflow*, not
   just as a symbol. This is what decides `high` vs `medium`: a symbol match with a different
   shape is `medium`, and the guide is where the shape shows.
5. **`harmonyos-faqs/**/document.md`** — often states limits and missing pieces explicitly, which
   is the fastest way to find the half of a library that does *not* port.
6. `engine/data/reference/hmos_api_index.json` — still useful for a fast method-name sweep, but
   it is now the **last** resort, not the first. It keys on normalised simple method names, so it
   produces false negatives by construction.

Cite the path you used in the mapping row's `note`. A row whose evidence cannot be re-found is a
row nobody can audit later.

---

## Already found — v1 questions this corpus answers

Two are recorded here because they were left explicitly open in v1 and are now settled or
actionable. Both are M5 work.

- **`@kit.RemoteCommunicationKit` is real.** v1 wrote: *"`rcp` was NOT used: the index attests it
  zero times… If `rcp` is real and merely absent from `hmos_api_index.json`, these rows deserve a
  revisit."* The corpus has `harmonyos-guides/system/network/remote-communication-kit/` with
  About This Kit, *Network Communication Using HTTP*, HTTP transmission performance and URPC
  scenarios. So the eight HTTP-client rows written to `@kit.NetworkKit` in v1.10.0
  (`dc.squareup.okhttp3`, `io.ktor`, `com.mr.http`, `org.springframework.http`,
  `org.apache.commons.httpclient`, …) need exactly the revisit v1 asked for — `rcp` may be the
  better target for a *client*, with `NetworkKit` remaining right for sockets and connection
  state.
- **Every rejection in `docs/v1/MAPPING_CANDIDATES_2026-08-20.md` and the six recorded genuine
  gaps rest on index absence.** They were correct given what v1 could check. They must be re-run
  against the `.d.ts` corpus before being treated as settled — starting with
  `android.credentials` (passkeys/WebAuthn), `com.google.android.flexbox` (declarative built-ins
  are invisible to a method index by construction, so the `component/` declarations are the right
  place), and `org.altbeacon`.

---

## Guardrails

- **Do not import anything from `docs-ref/` at runtime.** It is 110 MB of reference; the engine
  must keep working in a clone that has it stripped.
- **Do not edit it.** It is a crawled corpus. If it needs refreshing, re-crawl and replace whole.
- **Do not paste large excerpts into mapping notes.** A path plus the one attested symbol is the
  evidence; the corpus is the archive.
