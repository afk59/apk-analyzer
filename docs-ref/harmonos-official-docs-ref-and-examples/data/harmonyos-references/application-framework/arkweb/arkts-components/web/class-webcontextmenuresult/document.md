# Class (WebContextMenuResult)

Implements a **WebContextMenuResult** object. For details about the sample code, see [onContextMenuShow](../events/document.md#oncontextmenushow9).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/u4EKcO5-RxWoYWZkgi9vpQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062315Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=40F47BCBE8D3820BB34114C2CF2EAD71ABCA9EAA04609299F3E17A13438E7EC0)

-   The initial APIs of this component are supported since API version 8. Updates will be marked with a superscript to indicate their earliest API version.
    
-   The initial APIs of this class are supported since API version 9.
    
-   The sample effect is subject to the actual device.
    

#### constructor9+

constructor()

Constructs a **WebContextMenuResult** object.

**System capability**: SystemCapability.Web.Webview.Core

#### closeContextMenu9+

closeContextMenu(): void

Closes this context menu. This API must be called when no operations in **WebContextMenuResult** are performed.

**System capability**: SystemCapability.Web.Webview.Core

#### copyImage9+

copyImage(): void

Copies the image specified in **WebContextMenuParam**.

**System capability**: SystemCapability.Web.Webview.Core

#### copy9+

copy(): void

Copies text related to this context menu.

**System capability**: SystemCapability.Web.Webview.Core

#### paste9+

paste(): void

Performs the paste operation related to this context menu.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/yInpcMDYSDCnpYbg-LY_HA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062315Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3D105B01FFD605A4FF85201D7244ACF2D29A40F5FE3F2B1FCE93169B103A74B4)

The **ohos.permission.READ\_PASTEBOARD** permission must be declared.

**System capability**: SystemCapability.Web.Webview.Core

#### cut9+

cut(): void

Performs the cut operation related to this context menu.

**System capability**: SystemCapability.Web.Webview.Core

#### selectAll9+

selectAll(): void

Performs the select all operation related to this context menu.

**System capability**: SystemCapability.Web.Webview.Core

#### undo20+

undo(): void

Performs the undo operation related to this context menu.

**System capability**: SystemCapability.Web.Webview.Core

#### redo20+

redo(): void

Performs the redo operation related to this context menu, that is, cancels the last undo operation.

**System capability**: SystemCapability.Web.Webview.Core

#### pasteAndMatchStyle20+

pasteAndMatchStyle(): void

Performs the paste operation related to the context menu. The pasted content matches the target format and is displayed in plain text.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/h6VZ8Ub8QAaDRaP5QzAofQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062315Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5948139560E9AA333C835CDCA93589F7B600DF8A1838DB6904DE62A9CEC4C551)

The **ohos.permission.READ\_PASTEBOARD** permission must be declared.

**System capability**: SystemCapability.Web.Webview.Core
