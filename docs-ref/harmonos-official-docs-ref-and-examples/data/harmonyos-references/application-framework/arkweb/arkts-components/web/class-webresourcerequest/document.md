# Class (WebResourceRequest)

Implements the **WebResourceRequest** object to obtain resource requests. For details about the sample code, see [onErrorReceive](../events/document.md#onerrorreceive).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/BbSKwoPXQmSqtpB3XUus1g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062316Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D725F1622E625883CC2ACE3130C8949B69FA2DB0236FA4194A141A106FDDDE54)

-   The initial APIs of this component are supported since API version 8. Updates will be marked with a superscript to indicate their earliest API version.
    
-   The initial APIs of this class are supported since API version 8.
    
-   The sample effect is subject to the actual device.
    

#### constructor

constructor()

Constructs a **WebResourceRequest** object.

**System capability**: SystemCapability.Web.Webview.Core

#### getRequestHeader

getRequestHeader(): Array<Header>

Obtains the information about the resource request header.

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Array<[Header](../interfaces-others/document.md#header)\> | Information about the resource request header. |

#### getRequestUrl

getRequestUrl(): string

Obtains the URL of the resource request.

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| string | URL of the resource request. |

#### isMainFrame

isMainFrame(): boolean

Checks whether the resource request is for the main frame.

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | 
Whether the resource request is for the main frame.

The value **true** indicates that the resource request is for the main frame, and **false** indicates the opposite.

 |

#### isRedirect

isRedirect(): boolean

Checks whether the resource request is redirected by the server.

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | 
Whether the resource request is redirected by the server.

The value **true** indicates that the resource request is redirected by the server, and **false** indicates the opposite.

 |

#### isRequestGesture

isRequestGesture(): boolean

Checks whether the resource request is associated with a gesture (for example, a tap).

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | 
Whether the resource request is associated with a gesture (for example, a tap).

The value **true** indicates that the resource request is associated with a gesture, and **false** indicates the opposite.

 |

#### getRequestMethod9+

getRequestMethod(): string

Obtains the request method.

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| string | Request method. |
