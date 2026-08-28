# Class (WebResourceError)

Implements the **WebResourceError** object to manage resource errors. For details about the sample code, see [onErrorReceive](../events/document.md#onerrorreceive).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/8n2fYz_WSJqGYPRYthfS2w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062315Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A645249B1CAB439D142A9FDBF8BC405B164CD3AE5EFCFE82F871A47A969ED2B1)

-   The initial APIs of this component are supported since API version 8. Updates will be marked with a superscript to indicate their earliest API version.
    
-   The initial APIs of this class are supported since API version 8.
    
-   The sample effect is subject to the actual device.
    

#### constructor

constructor()

Constructs a **WebResourceError** object.

**System capability**: SystemCapability.Web.Webview.Core

#### getErrorCode

getErrorCode(): number

Obtains the error code for resource loading.

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| number | Error code for resource loading. For details about the error code, see [WebNetErrorList](../../../arkts-api/ohos-web-neterrorlist-the-list-of-arkweb-network-protocol-stack-errors/document.md#webneterrorlist) and HTTP status codes. |

#### getErrorInfo

getErrorInfo(): string

Obtains error information about resource loading.

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| string | Error information about resource loading. |
