# Class (PermissionRequest)

Implements the **PermissionRequest** object. For details about the sample code, see [onPermissionRequest](../events/document.md#onpermissionrequest9).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/jp8Bmf8DRe6Nd0ONVd6ABA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062315Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5C1E2543413FC6AA03571ADF4E44A74CBF3D53B18BD0490F2C878BAF183F5859)

-   The initial APIs of this component are supported since API version 8. Updates will be marked with a superscript to indicate their earliest API version.
    
-   The initial APIs of this class are supported since API version 9.
    
-   The sample effect is subject to the actual device.
    

#### constructor9+

constructor()

Constructs a **PermissionRequest** object.

**System capability**: SystemCapability.Web.Webview.Core

#### deny9+

deny(): void

Denies the permission requested by the web page.

**System capability**: SystemCapability.Web.Webview.Core

#### getOrigin9+

getOrigin(): string

Obtains the origin of this web page.

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| string | Origin of the web page that requests the permission. |

#### getAccessibleResource9+

getAccessibleResource(): Array<string>

Obtains the list of accessible resources requested for the web page. For details about the resource types, see [ProtectedResourceType](../enums/document.md#protectedresourcetype9).

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Array<string> | List of accessible resources requested by the web page. |

#### grant9+

grant(resources: Array<string>): void

Grants the permission for resources requested by the web page.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resources | Array<string> | Yes | List of resources that can be requested by the web page with the permission to grant. |
