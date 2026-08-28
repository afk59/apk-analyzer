# Class (JsResult)

Implements the **JsResult** object to confirm or cancel a dialog box. For details about the sample code, see [onAlert](../events/document.md#onalert).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/6as0YytFTMWv83TigEN5OA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062315Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=48F58E8AA97E2C722EEEB0EDD483D7D82B86E516B19CD8C6107F7FC8A19D206B)

-   The initial APIs of this component are supported since API version 8. Updates will be marked with a superscript to indicate their earliest API version.
    
-   The initial APIs of this class are supported since API version 8.
    
-   The sample effect is subject to the actual device.
    

#### constructor

constructor()

Constructs a **JsResult** object.

**System capability**: SystemCapability.Web.Webview.Core

#### handleCancel

handleCancel(): void

Notifies the **Web** component of the user's cancel operation in the dialog box.

**System capability**: SystemCapability.Web.Webview.Core

#### handleConfirm

handleConfirm(): void

Notifies the **Web** component of the user's confirm operation in the dialog box.

**System capability**: SystemCapability.Web.Webview.Core

#### handlePromptConfirm9+

handlePromptConfirm(result: string): void

Notifies the **Web** component of the user's confirm operation in the dialog box as well as the dialog box content.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| result | string | Yes | User input in the dialog box. |
