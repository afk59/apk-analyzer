# Http\_Response

typedef struct Http\_Response {...} Http\_Response

#### Overview

Defines the structure of HTTP responses.

**Since**: 20

**Related module**: [netstack](../../modules/netstack/document.md)

**Header file**: [net\_http\_type.h](../../header-files/net-http-type-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| [Http\_Buffer](../http-buffer/document.md) body | HTTP response data. For details, see [Http\_Buffer](../http-buffer/document.md). |
| [Http\_ResponseCode](../../header-files/net-http-type-h/document.md#http_responsecode) responseCode | HTTP response code. For details, see [Http\_ResponseCode](../../header-files/net-http-type-h/document.md#http_responsecode). |
| [Http\_Headers](../http-headers/document.md) \*headers | Pointer to the HTTP response header. For details, see [Http\_Headers](../http-headers/document.md). |
| char \*cookies | Pointer to the HTTP response cookies. |
| [Http\_PerformanceTiming](../http-performancetiming/document.md) \*performanceTiming | Pointer to the HTTP response timing. For details, see [Http\_PerformanceTiming](../http-performancetiming/document.md). |

#### \[h2\]Member Functions

| Name | Description |
| :-- | :-- |
| [void (\*destroyResponse)(struct Http\_Response \*\*response)](#destroyresponse) | Callback function for destroying an HTTP response. |

#### Member Function Description

#### \[h2\]destroyResponse()

void (\*destroyResponse)(struct Http\_Response \*\*response)

**Description**

Callback function for destroying an HTTP response.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| struct [Http\_Response](#) \*\*response | Pointer to the HTTP response to be destroyed. For details, see [Http\_Response](#). |
