# HiTraceId

typedef struct HiTraceId {...} HiTraceId

#### Overview

Defines a **HiTraceId** instance.

**Since**: 12

**Related module**: [HiTrace](../../modules/hitrace/document.md)

**Header file**: [trace.h](../../header-files/trace-h/document.md)

#### Summary

#### \[h2\]Member Variables

A little-endian **HiTraceId** consists of the following fields in sequence:

| Field | Number of Bits | Description |
| :-- | :-- | :-- |
| uint64\_t valid | 1 | Whether a **HiTraceId** instance is valid. |
| uint64\_t ver | 3 | Version number of **HiTraceId**. |
| uint64\_t chainId | 60 | Trace chain ID of **HiTraceId**. |
| uint64\_t flags | 12 | Trace flag of **HiTraceId**. |
| uint64\_t spanId | 26 | Span ID of **HiTraceId**. |
| uint64\_t parentSpanId | 26 | Parent span ID of **HiTraceId**. |

A big-endian **HiTraceId** consists of the following fields in sequence:

| Field | Number of Bits | Description |
| :-- | :-- | :-- |
| uint64\_t chainId | 60 | Trace chain ID of **HiTraceId**. |
| uint64\_t ver | 3 | Version number of **HiTraceId**. |
| uint64\_t valid | 1 | Whether a **HiTraceId** instance is valid. |
| uint64\_t parentSpanId | 26 | Parent span ID of **HiTraceId**. |
| uint64\_t spanId | 26 | Span ID of **HiTraceId**. |
| uint64\_t flags | 12 | Trace flag of **HiTraceId**. |
