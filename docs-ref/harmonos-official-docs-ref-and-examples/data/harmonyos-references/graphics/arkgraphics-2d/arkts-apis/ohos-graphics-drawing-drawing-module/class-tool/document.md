# Class (Tool)

A utility class that provides only static methods to convert data structs defined in other modules and [common2D](../../ohos-graphics-common2d-common-data-types-of-2d-graphics/document.md).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/TCR1-OKoTF6-88shiATGZQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062448Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AC14A34166106330263F78B4BC0453E43254608AF6858E1E09942D8EE3124F40)

-   The initial APIs of this module are supported since API version 11. Newly added APIs will be marked with a superscript to indicate their earliest API version.
    
-   The initial APIs of this class are supported since API version 15.
    
-   This module uses the physical pixel unit, px.
    
-   The module operates under a single-threaded model. The caller needs to manage thread safety and context state transitions.
    

#### Modules to Import

import { drawing } from '@kit.ArkGraphics2D';

#### makeColorFromResourceColor15+

static makeColorFromResourceColor(resourceColor: ResourceColor): common2D.Color

Converts a color value of the **ResourceColor** type to a **common2D.Color** object.

**System capability**: SystemCapability.Graphics.Drawing

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resourceColor | [ResourceColor](../../../../../application-framework/arkui/arkts-components/common-definitions/basic-types/document.md#resourcecolor) | Yes | Color value of the **ResourceColor** type. (All four types of inputs are supported. The following provides 13 example inputs.) The fourth type of [Resource](../../../../../application-framework/arkui/arkts-components/common-definitions/basic-types/document.md#resource) supports only the construction method **$r('belonging.type.name')**. Ensure that the resource has been defined in the **main/resources/base/element** directory. (The types **color**, **string**, and **integer** are available for the belonging **app**, whereas only the type **color** is available for the belonging **sys**.) |

**Returns**

| Type | Description |
| :-- | :-- |
| [common2D.Color](../../ohos-graphics-common2d-common-data-types-of-2d-graphics/document.md#color) | **Common2D.Color** object. If the conversion fails, a null pointer is returned. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types. |

**Example**

import { drawing, common2D } from '@kit.ArkGraphics2D';

// Color
let color1: common2D.Color = drawing.Tool.makeColorFromResourceColor(Color.Blue);

// Number
let color2: common2D.Color = drawing.Tool.makeColorFromResourceColor(0xffc0cb);
let color3: common2D.Color = drawing.Tool.makeColorFromResourceColor(0x11ffa500);

// String
let color4: common2D.Color = drawing.Tool.makeColorFromResourceColor('#ff0000');
let color5: common2D.Color = drawing.Tool.makeColorFromResourceColor('#110000ff');
let color6: common2D.Color = drawing.Tool.makeColorFromResourceColor('#00f');
let color7: common2D.Color = drawing.Tool.makeColorFromResourceColor('#100f');
let color8: common2D.Color = drawing.Tool.makeColorFromResourceColor('rgb(255, 100, 255)');
let color9: common2D.Color = drawing.Tool.makeColorFromResourceColor('rgba(255, 100, 255, 0.5)');

// Resource
let color10: common2D.Color = drawing.Tool.makeColorFromResourceColor($r('sys.color.ohos\_id\_color\_secondary'));

// Use color
let brush = new drawing.Brush();
brush.setColor(color1);
