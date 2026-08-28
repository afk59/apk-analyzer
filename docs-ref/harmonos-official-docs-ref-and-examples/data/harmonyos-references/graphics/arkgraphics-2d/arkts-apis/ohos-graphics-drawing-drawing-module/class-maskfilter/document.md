# Class (MaskFilter)

Implements a mask filter.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/NEcZOoqgQtay7s_pApxaMg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062447Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4218983C1DFD499CEAA1EA790893CAAD3701E30D6B9C42AF535735959896A48E)

-   The initial APIs of this module are supported since API version 11. Newly added APIs will be marked with a superscript to indicate their earliest API version.
    
-   The initial APIs of this class are supported since API version 12.
    
-   This module uses the physical pixel unit, px.
    
-   This module operates under a single-threaded model. The caller needs to manage thread safety and context state transitions.
    

#### Modules to Import

import { drawing } from '@kit.ArkGraphics2D';

#### createBlurMaskFilter12+

static createBlurMaskFilter(blurType: BlurType, sigma: number): MaskFilter

Creates a mask filter with a blur effect.

**System capability**: SystemCapability.Graphics.Drawing

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| blurType | [BlurType](../enums/document.md#blurtype12) | Yes | Blur type. |
| sigma | number | Yes | Standard deviation of the Gaussian blur to apply. The value must be a floating point number greater than 0. |

**Returns**

| Type | Description |
| :-- | :-- |
| [MaskFilter](#) | **Maskfilter** object created. |

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
    let maskFilter = drawing.MaskFilter.createBlurMaskFilter(drawing.BlurType.OUTER, 10);
  }
}
