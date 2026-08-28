# Class (ShadowLayer)

Implements a shadow layer.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/7PKNyvNhT32y2_jH44CQog/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062448Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5A6F26DA36067B8C595A2A29EC2D5EC24AE468156F3D971CF726C734006FC904)

-   The initial APIs of this module are supported since API version 11. Newly added APIs will be marked with a superscript to indicate their earliest API version.
    
-   The initial APIs of this class are supported since API version 12.
    
-   This module uses the physical pixel unit, px.
    
-   This module operates under a single-threaded model. The caller needs to manage thread safety and context state transitions.
    

#### Modules to Import

import { drawing } from '@kit.ArkGraphics2D';

#### create12+

static create(blurRadius: number, x: number, y: number, color: common2D.Color): ShadowLayer

Creates a **ShadowLayer** object.

**System capability**: SystemCapability.Graphics.Drawing

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| blurRadius | number | Yes | Radius of the shadow layer. The value must be a floating point number greater than 0. |
| x | number | Yes | Offset on the X axis. The value is a floating point number. |
| y | number | Yes | Offset on the Y axis. The value is a floating point number. |
| color | [common2D.Color](../../ohos-graphics-common2d-common-data-types-of-2d-graphics/document.md#color) | Yes | Color in ARGB format. The value of each color channel is an integer ranging from 0 to 255. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ShadowLayer](#) | **ShadowLayer** object created. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types;3.Parameter verification failed. |

**Example**

import { RenderNode } from '@kit.ArkUI';
import { common2D, drawing } from '@kit.ArkGraphics2D';

class DrawingRenderNode extends RenderNode {
  draw(context : DrawContext) {
    const canvas = context.canvas;
    let color : common2D.Color = {alpha: 0xFF, red: 0x00, green: 0xFF, blue: 0x00};
    let shadowLayer = drawing.ShadowLayer.create(3, -3, 3, color);
  }
}

#### create18+

static create(blurRadius: number, x: number, y: number, color: common2D.Color | number): ShadowLayer

Creates a **ShadowLayer** object.

**System capability**: SystemCapability.Graphics.Drawing

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| blurRadius | number | Yes | Radius of the shadow layer. The value must be a floating point number greater than 0. |
| x | number | Yes | Offset on the X axis. The value is a floating point number. |
| y | number | Yes | Offset on the Y axis. The value is a floating point number. |
| color | [common2D.Color](../../ohos-graphics-common2d-common-data-types-of-2d-graphics/document.md#color) | number | Yes | Color, represented by an unsigned integer in hexadecimal ARGB format. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ShadowLayer](#) | **ShadowLayer** object created. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types;3.Parameter verification failed. |

**Example**

import { RenderNode } from '@kit.ArkUI';
import { drawing } from '@kit.ArkGraphics2D';

class DrawingRenderNode extends RenderNode {
  draw(context : DrawContext) {
    const canvas = context.canvas;
    let shadowLayer = drawing.ShadowLayer.create(3, -3, 3, 0xff00ff00);
  }
}
