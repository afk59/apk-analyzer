# Class (WebResourceResponse)

Implements the **WebResourceResponse** object. For details about the sample code, see [onHttpErrorReceive](../events/document.md#onhttperrorreceive).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/eo-PcU9-RLSsPOeiRmK6Eg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062316Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DC0448FC0E4BB20A7E79503C4204F79BD61179258B83C67E13E47E359C513A1F)

-   The initial APIs of this component are supported since API version 8. Updates will be marked with a superscript to indicate their earliest API version.
    
-   The initial APIs of this class are supported since API version 8.
    
-   The sample effect is subject to the actual device.
    

#### constructor

constructor()

Constructs a **WebResourceResponse**.

**System capability**: SystemCapability.Web.Webview.Core

#### getReasonMessage

getReasonMessage(): string

Obtains the status code description of the resource response.

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| string | Status code description of the resource response. |

#### getResponseCode

getResponseCode(): number

Obtains the status code of the resource response.

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| number | Status code of the resource response. |

#### getResponseData

getResponseData(): string

Obtains the data in the resource response.

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| string | Data in the resource response. |

#### getResponseEncoding

getResponseEncoding(): string

Obtains the encoding string of the resource response.

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| string | Encoding string of the resource response. |

#### getResponseHeader

getResponseHeader() : Array<Header>

Obtains the resource response header.

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Array<[Header](../interfaces-others/document.md#header)\> | Resource response header. |

#### getResponseMimeType

getResponseMimeType(): string

Obtains the MIME type of the resource response.

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| string | MIME type of the resource response. |

#### getResponseDataEx13+

getResponseDataEx(): string | number | ArrayBuffer | Resource | undefined

Obtains the data in the resource response. Multiple data types are supported.

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| string | number | ArrayBuffer | [Resource](../../../../arkui/arkts-components/common-definitions/basic-types/document.md#resource) | undefined | An HTML string when the type is string; a file descriptor when the type is number; binary data when the type is ArrayBuffer; a **$rawfile** resource when the type is resource; or **undefined** if no data is available. |

#### getResponseIsReady13+

getResponseIsReady(): boolean

Obtains whether the response data is ready.

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | **true** indicates that the response data is ready, and **false** indicates the opposite. |

#### setResponseData9+

setResponseData(data: string | number | Resource | ArrayBuffer): void

Sets the data in the resource response.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| data | string | number | [Resource](../../../../arkui/arkts-components/common-definitions/basic-types/document.md#resource) | ArrayBuffer11+ | Yes | Resource response data to set. When set to a string, the value indicates a string in HTML format. When set to a number, the value indicates a file handle, which is closed by the system **Web** component. When set to a **Resource** object, the value indicates the file resources in the **rawfile** directory of the application. When set to an **ArrayBuffer** object, the value indicates the original binary data of a resource. |

#### setResponseEncoding9+

setResponseEncoding(encoding: string): void

Sets the encoding string of the resource response.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| encoding | string | Yes | Encoding string to set. |

#### setResponseMimeType9+

setResponseMimeType(mimeType: string): void

Sets the MIME type of the resource response.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| mimeType | string | Yes | MIME type to set. |

#### setReasonMessage9+

setReasonMessage(reason: string): void

Sets the status code description of the resource response.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| reason | string | Yes | Status code description to set. |

#### setResponseHeader9+

setResponseHeader(header: Array<Header>): void

Sets the resource response header.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| header | Array<[Header](../interfaces-others/document.md#header)\> | Yes | Resource response header to set. |

#### setResponseCode9+

setResponseCode(code: number): void

Sets the status code of the resource response.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| code | number | Yes | Status code to set. If the resource ends with an error, set the error code by referring to [@ohos.web.netErrorList](../../../arkts-api/ohos-web-neterrorlist-the-list-of-arkweb-network-protocol-stack-errors/document.md). Do not set the error code to **ERR\_IO\_PENDING**, which may block the synchronous **XMLHttpRequest**. |

#### setResponseIsReady9+

setResponseIsReady(IsReady: boolean): void

Sets whether the resource response data is ready.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| IsReady | boolean | Yes | 
Whether the resource response data is ready.

The value **true** indicates that the resource response data is ready, and **false** indicates the opposite.

If the data is provided asynchronously, this parameter must be explicitly set to **false**. If this parameter is set to an invalid value, for example, **null** or **undefined**, or is not set, the data is considered ready.

 |
