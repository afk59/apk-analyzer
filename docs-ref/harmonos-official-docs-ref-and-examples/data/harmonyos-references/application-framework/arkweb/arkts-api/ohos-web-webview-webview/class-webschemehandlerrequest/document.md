# Class (WebSchemeHandlerRequest)

Represents a request intercepted by the **WebSchemeHandler** object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/Clc32C9SRpihakk6adz9zA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062313Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C3F60F5DDD090D14050868E21AFF09BB81564CE66F06546B07BFFF9E892A99F2)

-   The initial APIs of this module are supported since API version 9. Updates will be marked with a superscript to indicate their earliest API version.
    
-   The initial APIs of this class are supported since API version 12.
    
-   The sample effect is subject to the actual device.
    

#### getHeader12+

getHeader(): Array<WebHeader>

Obtains the information about the resource request header.

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Array<[WebHeader](../interfaces-others/document.md#webheader)\> | Information about the resource request header. |

**Example**

For the complete sample code, see [onRequestStart](../class-webschemehandler/document.md#onrequeststart12).

#### getRequestUrl12+

getRequestUrl(): string

Obtains the URL of the resource request.

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| string | URL of the resource request. |

**Example**

For the complete sample code, see [onRequestStart](../class-webschemehandler/document.md#onrequeststart12).

#### getRequestMethod12+

getRequestMethod(): string

Obtains the request method.

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| string | Request method. |

**Example**

For the complete sample code, see [onRequestStart](../class-webschemehandler/document.md#onrequeststart12).

#### getReferrer12+

getReferrer(): string

Obtains the referrer.

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| string | Obtained referrer. |

**Example**

For the complete sample code, see [onRequestStart](../class-webschemehandler/document.md#onrequeststart12).

#### isMainFrame12+

isMainFrame(): boolean

Checks whether the resource request is for the main frame.

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Whether the resource request is for the main frame. If the resource request is for the main frame, **true** is returned. Otherwise, **false** is returned. |

**Example**

For the complete sample code, see [onRequestStart](../class-webschemehandler/document.md#onrequeststart12).

#### hasGesture12+

hasGesture(): boolean

Checks whether the resource request is associated with a gesture (for example, a tap).

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Whether the resource request is associated with a gesture (for example, a tap). If the resource request is associated with a gesture, **true** is returned. Otherwise, **false** is returned. |

**Example**

For the complete sample code, see [onRequestStart](../class-webschemehandler/document.md#onrequeststart12).

#### getHttpBodyStream12+

getHttpBodyStream(): WebHttpBodyStream | null

Obtains the **WebHttpBodyStream** instance in this resource request.

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [WebHttpBodyStream](../class-webhttpbodystream/document.md) | null | **WebHttpBodyStream** instance in the resource request. If there is no **WebHttpBodyStream** instance, **null** is returned. |

**Example**

For the complete sample code, see [onRequestStart](../class-webschemehandler/document.md#onrequeststart12).

#### getRequestResourceType12+

getRequestResourceType(): WebResourceType

Obtains the resource type of this resource request.

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [WebResourceType](../enums/document.md#webresourcetype12) | Resource type of the resource request. |

**Example**

For the complete sample code, see [onRequestStart](../class-webschemehandler/document.md#onrequeststart12).

#### getFrameUrl12+

getFrameUrl(): string

Obtains the URL of the frame that triggers this request.

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| string | URL of the frame that triggers the request. |

**Example**

For the complete sample code, see [onRequestStart](../class-webschemehandler/document.md#onrequeststart12).
