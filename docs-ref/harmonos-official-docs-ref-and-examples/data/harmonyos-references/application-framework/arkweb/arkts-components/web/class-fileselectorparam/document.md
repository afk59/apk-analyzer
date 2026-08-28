# Class (FileSelectorParam)

Implements the **FileSelectorParam** object to obtain files. For details about the sample code, see [onShowFileSelector](../events/document.md#onshowfileselector9).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/hdBiEmHzQneh0ZarRPLOeA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062315Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E43527B8C6761AB5796E40D9124200288F80A75703DE151FDE2855D5FE5E088C)

-   The initial APIs of this component are supported since API version 8. Updates will be marked with a superscript to indicate their earliest API version.
    
-   The initial APIs of this class are supported since API version 9.
    
-   The sample effect is subject to the actual device.
    

#### constructor9+

constructor()

Constructs a **FileSelectorParam**.

**System capability**: SystemCapability.Web.Webview.Core

#### getTitle9+

getTitle(): string

Obtains the title of this file selector.

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| string | Title of the file selector. |

#### getMode9+

getMode(): FileSelectorMode

Obtains the mode of the file selector.

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [FileSelectorMode](../enums/document.md#fileselectormode9) | Mode of the file selector. |

#### getAcceptType9+

getAcceptType(): Array<string>

Obtains the file filtering type.

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Array<string> | File filtering type. |

#### isCapture9+

isCapture(): boolean

Checks whether multimedia capabilities are invoked.

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | 
Whether multimedia capabilities are invoked.

The value **true** indicates that multimedia capabilities are invoked, and **false** indicates the opposite.

 |

#### getMimeTypes18+

getMimeTypes(): Array<string>

Obtains the MIME type of a file.

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Array<string> | MIME type of a file. |
