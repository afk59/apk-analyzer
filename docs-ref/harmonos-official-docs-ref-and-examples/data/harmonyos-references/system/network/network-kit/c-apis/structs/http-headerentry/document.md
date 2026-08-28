# Http\_HeaderEntry

typedef struct Http\_HeaderEntry {...} Http\_HeaderEntry

#### Overview

Defines all key-value pairs in the request or response header.

**Since**: 20

**Related module**: [netstack](../../modules/netstack/document.md)

**Header file**: [net\_http\_type.h](../../header-files/net-http-type-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| char \*key | Key in the request or response header. |
| [Http\_HeaderValue](../http-headervalue/document.md) \*value | Value of the key in the request or response header. For details, see [Http\_HeaderValue](../http-headervalue/document.md). |
| struct Http\_HeaderEntry \*next | Pointer to Pointer to the next **Http\_HeaderEntry**. |
