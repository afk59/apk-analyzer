# Class (JsGeolocation)

Implements the **PermissionRequest** object. For details about the sample code, see [onGeolocationShow](../events/document.md#ongeolocationshow).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/E48UKuFsTPuiPKHihreRdw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062315Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7A3F2EFD14343B93CB6BFB0EF07D13D210CA0B46F3809435495B3E8889B4F9D3)

-   The initial APIs of this component are supported since API version 8. Updates will be marked with a superscript to indicate their earliest API version.
    
-   The initial APIs of this class are supported since API version 8.
    
-   The sample effect is subject to the actual device.
    

#### constructor

constructor()

Constructs a **JsGeolocation** object.

**System capability**: SystemCapability.Web.Webview.Core

#### invoke

invoke(origin: string, allow: boolean, retain: boolean): void

Sets the geolocation permission status of a web page.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| origin | string | Yes | Index of the origin. |
| allow | boolean | Yes | 
Geolocation permission status.

The value **true** means to enable the geolocation permission, and **false** means the opposite.

 |
| retain | boolean | Yes | 

Whether the geolocation permission status can be saved to the system. You can manage the geolocation permissions saved to the system through the [GeolocationPermissions9+](../../../arkts-api/ohos-web-webview-webview/class-geolocationpermissions/document.md) API.

The value **true** indicates that the geolocation permission status can be saved to the system, and **false** indicates the opposite.

 |
