# Class (VerifyPinHandler)

Defines the PIN verification handler object returned by the **Web** component. For details about the sample code, see [onVerifyPin](../../../arkts-components/web/events/document.md#onverifypin22).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/EyZ7CjOIQAytOasLry34fw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062314Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F87E471F4E6F0CF9A700CBB87E41F4232A6A12F75300A7A8A91FFC0537C4DCF9)

-   This component is supported since API version 22. Updates will be marked with a superscript to indicate their earliest API version.
    
-   The initial APIs of this class are supported since API version 22.
    
-   The sample effect is subject to the actual device.
    

#### constructor22+

constructor()

A constructor used to create a **VerifyPinHandler** instance.

**System capability**: SystemCapability.Web.Webview.Core

#### confirm22+

confirm(result: PinVerifyResult): void

Notifies the **Web** component of the PIN verification result.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| result | [PinVerifyResult](../../../arkts-components/web/enums/document.md#pinverifyresult22) | Yes | PIN verification result. |
