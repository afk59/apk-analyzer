# net\_http.h

#### Overview

Defines the APIs of the HTTP request module.

**File to include**: <network/netstack/net\_http.h>

**Library**: libnet\_http.so

**System capability**: SystemCapability.Communication.NetStack

**Since**: 20

**Related module**: [netstack](../../modules/netstack/document.md)

#### Summary

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [Http\_Headers \*OH\_Http\_CreateHeaders(void)](#oh_http_createheaders) | Creates an HTTP request or response header. |
| [void OH\_Http\_DestroyHeaders(Http\_Headers \*\*headers)](#oh_http_destroyheaders) | Destroys an HTTP request or response header. |
| [uint32\_t OH\_Http\_SetHeaderValue(struct Http\_Headers \*headers, const char \*name, const char \*value)](#oh_http_setheadervalue) | Sets the key-value pairs of an HTTP request or response header. |
| [Http\_HeaderValue \*OH\_Http\_GetHeaderValue(Http\_Headers \*headers, const char \*name)](#oh_http_getheadervalue) | Obtains the value of an HTTP request or response header based on the specified key. |
| [Http\_HeaderEntry \*OH\_Http\_GetHeaderEntries(Http\_Headers \*headers)](#oh_http_getheaderentries) | Obtains all key-value pairs from an HTTP request or response header. |
| [void OH\_Http\_DestroyHeaderEntries(Http\_HeaderEntry \*\*headerEntry)](#oh_http_destroyheaderentries) | Destroys all key-value pairs obtained from **OH\_Http\_GetHeaderEntries**. |
| [Http\_Request \*OH\_Http\_CreateRequest(const char \*url)](#oh_http_createrequest) | Creates an HTTP request. |
| [int OH\_Http\_Request(Http\_Request \*request, Http\_ResponseCallback callback, Http\_EventsHandler handler)](#oh_http_request) | Initiates an HTTP request. |
| [void OH\_Http\_Destroy(struct Http\_Request \*\*request)](#oh_http_destroy) | Destroys an HTTP request. |

#### Function Description

#### \[h2\]OH\_Http\_CreateHeaders()

Http\_Headers \*OH\_Http\_CreateHeaders(void)

**Overview**

Creates an HTTP request or response header.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/dXAakWptSWWdEXM17EgNnA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062347Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BBFB31EE2E3B2B88C70159B9850B4E9BF5C05EE02D8D085DF9095F31E7C0DD02)

You are advised to call [OH\_Http\_DestroyHeaders](#oh_http_destroyheaders) to destroy the HTTP request or response header and clear resources after the HTTP request is complete.

**System capability**: SystemCapability.Communication.NetStack

**Since**: 20

**Return value**

| Type | Description |
| :-- | :-- |
| [Http\_Headers](../../structs/http-headers/document.md) \* | Pointer to the HTTP request or response header. |

#### \[h2\]OH\_Http\_DestroyHeaders()

void OH\_Http\_DestroyHeaders(Http\_Headers \*\*headers)

**Overview**

Destroys an HTTP request or response header.

**System capability**: SystemCapability.Communication.NetStack

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [Http\_Headers](../../structs/http-headers/document.md) \*\*headers | HTTP request or response header to be destroyed. The header is generated using **OH\_Http\_CreateHeaders**. |

#### \[h2\]OH\_Http\_SetHeaderValue()

uint32\_t OH\_Http\_SetHeaderValue(struct Http\_Headers \*headers, const char \*name, const char \*value)

**Overview**

Sets the key-value pairs of an HTTP request or response header.

**System capability**: SystemCapability.Communication.NetStack

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [struct Http\_Headers](../../structs/http-headers/document.md) \*headers | Pointer to **Http\_Headers**. |
| const char \*name | Key name. |
| const char \*value | Key value. |

**Return value**

| Type | Description |
| :-- | :-- |
| uint32\_t | 
A status code of the uint32\_t type.

**0**: Success.

**401**: Parameter error.

**2300027**: Insufficient memory.

 |

#### \[h2\]OH\_Http\_GetHeaderValue()

Http\_HeaderValue \*OH\_Http\_GetHeaderValue(Http\_Headers \*headers, const char \*name)

**Overview**

Obtains the value of an HTTP request or response header based on the specified key.

**System capability**: SystemCapability.Communication.NetStack

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [Http\_Headers](../../structs/http-headers/document.md) \*headers | Pointer to **Http\_Headers**. |
| const char \*name | Key name. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Http\_HeaderValue](../../structs/http-headervalue/document.md) \* | Pointer to **Http\_HeaderValue**. |

#### \[h2\]OH\_Http\_GetHeaderEntries()

Http\_HeaderEntry \*OH\_Http\_GetHeaderEntries(Http\_Headers \*headers)

**Overview**

Obtains all key-value pairs from an HTTP request or response header.

**System capability**: SystemCapability.Communication.NetStack

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [Http\_Headers](../../structs/http-headers/document.md) \*headers | Pointer to **Http\_Headers**. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Http\_HeaderEntry](../../structs/http-headerentry/document.md) \* | Pointer to **Http\_HeaderEntry**. |

#### \[h2\]OH\_Http\_DestroyHeaderEntries()

void OH\_Http\_DestroyHeaderEntries(Http\_HeaderEntry \*\*headerEntry)

**Overview**

Destroys all key-value pairs obtained from **OH\_Http\_GetHeaderEntries**.

**System capability**: SystemCapability.Communication.NetStack

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [Http\_HeaderEntry](../../structs/http-headerentry/document.md) \*\*headerEntry | Pointer to **Http\_HeaderEntry**, which is obtained through **OH\_Http\_GetHeaderEntries**. |

#### \[h2\]OH\_Http\_CreateRequest()

Http\_Request \*OH\_Http\_CreateRequest(const char \*url)

**Overview**

Creates an HTTP request.

**System capability**: SystemCapability.Communication.NetStack

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| const char \*url | Request URL. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Http\_Request](../../structs/http-request/document.md) \* | Pointer to **Http\_Request**. |

#### \[h2\]OH\_Http\_Request()

int OH\_Http\_Request(Http\_Request \*request, Http\_ResponseCallback callback, Http\_EventsHandler handler)

**Overview**

Initiates an HTTP request.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/k6oat9quT92UTCI6qeVAtw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062347Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EF4C41F70DEA7BB14084BE62EAEBB43B8E205C072793FA5F7856F28BE28825B3)

You are advised to call [OH\_Http\_Destroy](#oh_http_destroy) to interrupt the HTTP request after the HTTP request receives a response and the response is processed.

**System capability**: SystemCapability.Communication.NetStack

**Required permission**: ohos.permission.INTERNET

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [Http\_Request](../../structs/http-request/document.md) \*request | Pointer to **Http\_Request**. |
| [Http\_ResponseCallback](../net-http-type-h/document.md#http_responsecallback) callback | HTTP response callback. |
| [Http\_EventsHandler](../../structs/http-eventshandler/document.md) handler | HTTP event handler. |

**Return value**

| Type | Description |
| :-- | :-- |
| int | 
**0** if the operation is successful; an error code otherwise. For details about the error code description, see **Http\_ErrCode**.

**Http\_ResponseCallback** also carries **errCode**, indicating that the operation is successful but server communication is abnormal due to some reasons. For details, see **Http\_ErrCode**.

 |

#### \[h2\]OH\_Http\_Destroy()

void OH\_Http\_Destroy(struct Http\_Request \*\*request)

**Overview**

Stops the HTTP request.

**System capability**: SystemCapability.Communication.NetStack

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [struct Http\_Request](../../structs/http-request/document.md) \*\*request | Pointer to the request to be interrupted, which is a pointer to **Http\_Request**. For details, see [Http\_Request](../../structs/http-request/document.md). |
