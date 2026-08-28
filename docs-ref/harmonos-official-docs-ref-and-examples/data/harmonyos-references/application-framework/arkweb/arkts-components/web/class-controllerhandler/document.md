# Class (ControllerHandler)

Implements a **WebviewController** object for new **Web** components. For details about the sample code, see [onWindowNew](../events/document.md#onwindownew9).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/d2LseBIuRxCYi0ZssikTzg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062315Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=68AF04E910FEB7CCC2BEC28466F9B8F4C61DEA38DD7A58CAA869C6C2F137AE8A)

-   The initial APIs of this component are supported since API version 8. Updates will be marked with a superscript to indicate their earliest API version.
    
-   The initial APIs of this class are supported since API version 9.
    
-   The sample effect is subject to the actual device.
    

#### constructor9+

constructor()

Constructs a **ControllerHandler** API.

**System capability**: SystemCapability.Web.Webview.Core

#### setWebController9+

setWebController(controller: WebviewController): void

Sets a **WebviewController** object. If opening a new window is not needed, set the parameter to **null**.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| controller | [WebviewController](../../../arkts-api/ohos-web-webview-webview/class-webviewcontroller/document.md) | Yes | **WebviewController** object of the **Web** component. If opening a new window is not needed, set it to **null**. |
