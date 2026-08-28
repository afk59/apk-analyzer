# Http\_HeaderValue

typedef struct Http\_HeaderValue {...} Http\_HeaderValue

#### Overview

Defines the type of a mapped value in a request or response header.

**Since**: 20

**Related module**: [netstack](../../modules/netstack/document.md)

**Header file**: [net\_http\_type.h](../../header-files/net-http-type-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| char \*value | Value of a key-value pair in the header. |
| struct Http\_HeaderValue \*next | Pointer to Pointer to the next **Http\_HeaderValue**. |
