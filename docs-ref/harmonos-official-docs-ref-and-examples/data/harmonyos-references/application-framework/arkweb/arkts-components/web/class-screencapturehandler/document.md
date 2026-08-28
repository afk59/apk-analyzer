# Class (ScreenCaptureHandler)

Implements the **ScreenCaptureHandler** object for accepting or rejecting a screen capture request. For details about the sample code, see [onScreenCaptureRequest](../events/document.md#onscreencapturerequest10).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/oSYeN_gYSVi19Vlm83075w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062315Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=138A9207712486CA3C793AC70F90BF9157B3BE8ABFA34BA477B8107634BD5E76)

-   The initial APIs of this component are supported since API version 8. Updates will be marked with a superscript to indicate their earliest API version.
    
-   The initial APIs of this class are supported since API version 10.
    
-   The sample effect is subject to the actual device.
    

#### constructor10+

constructor()

Constructs a **ScreenCaptureHandler** object.

**System capability**: SystemCapability.Web.Webview.Core

#### deny10+

deny(): void

Rejects this screen capture request.

**System capability**: SystemCapability.Web.Webview.Core

#### getOrigin10+

getOrigin(): string

Obtains the origin of this web page.

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| string | Origin of the web page that requests the permission. |

#### grant10+

grant(config: ScreenCaptureConfig): void

Grants the screen capture permission.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/RDTpsXeDRxyr_nV4Mq2veA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062315Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CDA7EC6D0C8B88AF9FF9E62F89B37280B4DC9EF714AA4D31D6FF8AF21B089969)

The **ohos.permission.MICROPHONE** permission must be declared.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| config | [ScreenCaptureConfig](../interfaces-others/document.md#screencaptureconfig10) | Yes | Screen capture configuration. |
