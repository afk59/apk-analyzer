# Http\_Request

typedef struct Http\_Request {...} Http\_Request

#### Overview

Defines an HTTP request.

**Since**: 20

**Related module**: [netstack](../../modules/netstack/document.md)

**Header file**: [net\_http\_type.h](../../header-files/net-http-type-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| uint32\_t requestId | ID of an HTTP request. |
| char \*url | Pointer to the HTTP request URL. |
| [Http\_RequestOptions](../http-requestoptions/document.md) \*options | Pointer to the HTTP request configuration. For details, see [Http\_RequestOptions](../http-requestoptions/document.md). |
