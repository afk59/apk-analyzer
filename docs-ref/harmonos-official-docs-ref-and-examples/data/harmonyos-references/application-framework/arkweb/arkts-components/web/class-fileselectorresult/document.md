# Class (FileSelectorResult)

Implements the **FileSelectorResult** object to notify the file selection result. For details about the sample code, see [onShowFileSelector](../events/document.md#onshowfileselector9).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/YRC9M3t-SH6sa9gjAeBfiw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062315Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8A83B49CB60A9E386F488F053A9C9E76E6F5F040521408A27ABAE672905743CD)

-   The initial APIs of this component are supported since API version 8. Updates will be marked with a superscript to indicate their earliest API version.
    
-   The initial APIs of this class are supported since API version 9.
    
-   The sample effect is subject to the actual device.
    

#### constructor9+

constructor()

Constructs a **FileSelectorResult**.

**System capability**: SystemCapability.Web.Webview.Core

#### handleFileList9+

handleFileList(fileList: Array<string>): void

Instructs the **Web** component to select a file.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| fileList | Array<string> | Yes | List of files to operate. |
