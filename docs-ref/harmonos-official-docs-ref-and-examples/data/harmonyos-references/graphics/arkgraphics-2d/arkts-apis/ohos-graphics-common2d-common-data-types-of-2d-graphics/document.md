# @ohos.graphics.common2D (Common Data Types of 2D Graphics)

This module defines some common data types in the 2D graphics field.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/b95jLZ3ZRH-e5r-Pk1nNlQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062446Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1DB72743DDFB3D1DDE86753C2FB1E5ABFB0C831467D1984791AF06121EB0D35C)

-   The initial APIs of this module are supported since API version 11. Newly added APIs will be marked with a superscript to indicate their earliest API version.
    
-   This module uses the physical pixel unit, px.
    

#### Modules to Import

import { common2D } from '@kit.ArkGraphics2D';

#### Color

Describes a color in ARGB format.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.Graphics.Drawing

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| alpha | number | No | No | Alpha component of the color. The value is an integer ranging from 0 to 255. |
| red | number | No | No | Red component of the color. The value is an integer ranging from 0 to 255. |
| green | number | No | No | Green component of the color. The value is an integer ranging from 0 to 255. |
| blue | number | No | No | Blue component of the color. The value is an integer ranging from 0 to 255. |

#### Rect

Describes a rectangle, which can be defined by two coordinate points: upper left corner point and lower right corner point.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.Graphics.Drawing

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| left | number | No | No | X coordinate of the upper left corner of the rectangle. The value is a floating point number. |
| top | number | No | No | Y coordinate of the upper left corner of the rectangle. The value is a floating point number. |
| right | number | No | No | X coordinate of the lower right corner of the rectangle. The value is a floating point number. |
| bottom | number | No | No | Y coordinate of the lower right corner of the rectangle. The value is a floating point number. |

#### Point12+

Describes a coordinate point.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.Graphics.Drawing

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| x | number | No | No | Horizontal coordinate. The value is a floating point number. |
| y | number | No | No | Vertical coordinate. The value is a floating point number. |

#### Color4f20+

Describes a color in ARGB format.

**System capability**: SystemCapability.Graphics.Drawing

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| alpha | number | No | No | Alpha component of the color. The value is a floating point number ranging from 0.0 to 1.0. |
| red | number | No | No | Red component of the color. The value is a floating point number ranging from 0.0 to 1.0. |
| green | number | No | No | Green component of the color. The value is a floating point number ranging from 0.0 to 1.0. |
| blue | number | No | No | Blue component of the color. The value is a floating point number ranging from 0.0 to 1.0. |

#### Point3d12+

Describes a 3D coordinate point. It inherits from [Point](#point12).

**System capability**: SystemCapability.Graphics.Drawing

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| z | number | No | No | Z-axis coordinate. The value is a floating point number. |
