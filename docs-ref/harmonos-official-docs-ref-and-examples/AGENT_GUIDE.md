# Harmony Docs Agent Guide

This directory is a local HarmonyOS documentation corpus intended for coding agents and LLMs.

Read this file first before answering HarmonyOS or ArkTS questions.

## Purpose

Use this corpus as the first source of truth for:
- ArkTS syntax and usage
- ArkUI components and layout patterns
- HarmonyOS SDK APIs, methods, parameters, and return types
- common build, signing, and troubleshooting questions

Prefer this local corpus over web search when the question is about HarmonyOS development.

## Corpus Layout

- `data/harmonyos-guides`: conceptual and how-to documentation
- `data/harmonyos-references`: API and kit reference documentation
- `data/harmonyos-faqs`: troubleshooting, pitfalls, and practical issues

Each document is stored as `document.md`.

Each catalog also contains `.meta/` with crawler metadata. Do not treat `.meta/` as primary content unless you specifically need indexing details.

## Search Strategy

For HarmonyOS or ArkTS questions, use this order:

1. Search file and folder names under `data/`.
2. Search inside the most likely catalog with keyword grep.
3. Read the most relevant `document.md` files.
4. If needed, cross-check between guides, references, and FAQs.
5. Answer using the local docs, citing file paths when useful.

## Catalog Selection

Use `harmonyos-guides` first when the question is about:
- how to implement something
- layout patterns
- app structure
- routing, UI flow, resource usage
- tutorials and conceptual explanations

Use `harmonyos-references` first when the question is about:
- a specific API
- a component name
- a method, property, event, or parameter
- exact SDK behavior
- kit/module-level reference details

Use `harmonyos-faqs` first when the question is about:
- an error
- build/signing/debugging issues
- practical limitations
- migration pain points
- why something is not working as expected

## Query Routing Examples

- `How to use Grid?` -> `harmonyos-guides`, then `harmonyos-references`
- `GridRow GridCol span offset order` -> `harmonyos-guides`, then `harmonyos-references`
- `router pushUrl / navigation` -> `harmonyos-guides`, then `harmonyos-references`
- `What are the events of text input component` -> `harmonyos-references`
- `@State @Prop @Link differences` -> `harmonyos-guides`, then `harmonyos-references`
- `How to ask for a permission?` -> `harmonyos-guides`, then `harmonyos-faqs`
- `signing / certificate / run on device sorunu` -> `harmonyos-faqs`, then `harmonyos-guides`
- `why build fails` -> `harmonyos-faqs`, then relevant `guides`
- `Which kit has which API?` -> `harmonyos-references`
- `ArkTS project structure` -> `harmonyos-guides`
- `What is SystemCapability` -> `harmonyos-references`

## Practical Retrieval Pattern

If the user asks a broad question:
- start in `harmonyos-guides`
- use `harmonyos-references` to refine exact API details
- use `harmonyos-faqs` if implementation issues or edge cases appear

If the user asks a narrow API question:
- start in `harmonyos-references`
- fall back to `harmonyos-guides` for examples or conceptual usage

If the user reports a bug or tool failure:
- start in `harmonyos-faqs`
- then use guides/references to confirm the intended usage

## Recommended Agent Behavior

- Do not answer from memory if the local docs likely contain the answer.
- Search the local corpus first.
- When useful, mention the supporting local file path in the answer.
- If guides and references disagree in detail, trust references for exact API behavior.
- If no answer is found locally, say that clearly and then use another source.

## Portability

This docs package may be moved or symlinked into other workspaces.

Treat the directory containing this file as the docs root.
Do not assume a fixed absolute path.

If your host environment provides a docs-root variable such as `HARMONY_DOCS_ROOT`, resolve this file relative to that root and start here.
