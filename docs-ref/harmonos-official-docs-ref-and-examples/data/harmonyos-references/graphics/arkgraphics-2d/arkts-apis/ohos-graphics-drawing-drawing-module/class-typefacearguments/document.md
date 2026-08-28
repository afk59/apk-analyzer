# Class (TypefaceArguments)

This module defines a struct for setting typeface arguments.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/eLsu9DmkRGGdorpVAg6FOQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062448Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F5CD3DA3D2EF38B562FF5590203493EEAB82E9533244A199A201F5D237378795)

-   The initial APIs of this module are supported since API version 11. Newly added APIs will be marked with a superscript to indicate their earliest API version.
    
-   The initial APIs of this class are supported since API version 20.
    
-   This module uses the physical pixel unit, px.
    
-   The module operates under a single-threaded model. The caller needs to manage thread safety and context state transitions.
    

#### Modules to Import

import { drawing } from '@kit.ArkGraphics2D';

#### constructor20+

constructor()

Constructor for typeface arguments.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.Graphics.Drawing

**Example**

import { drawing } from '@kit.ArkGraphics2D';
let typeFaceArgument = new drawing.TypefaceArguments();

#### addVariation20+

addVariation(axis: string, value: number)

Defines the typeface weight.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.Graphics.Drawing

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| axis | string | Yes | The **'wght'** tag for the weight variation in the **typeFaceArgument** object. Whether the tag is supported depends on the loaded typeface file. For details, check the typeface file. |
| value | number | Yes | Value linked to the **'wght'** tag for the weight variation in the **typeFaceArgument** object. The value must be within the range defined in the typeface file. Otherwise, the value does not take effect. Values below the minimum will be set to the minimum and values above the maximum to the maximum. For details, check the typeface file. |

**Error codes**

For details about the following error code, see [Drawing and Display Error Codes](../../../error-codes/drawing-and-display-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 25900001 | Parameter error.Possible causes: Incorrect parameter range. |

**Example**

import { drawing } from '@kit.ArkGraphics2D';

let typeFaceArgument = new drawing.TypefaceArguments();
typeFaceArgument.addVariation('wght', 10);
