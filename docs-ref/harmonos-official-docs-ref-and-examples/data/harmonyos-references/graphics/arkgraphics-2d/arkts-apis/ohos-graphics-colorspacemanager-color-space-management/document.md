# @ohos.graphics.colorSpaceManager (Color Space Management)

The **colorSpaceManager** module provides APIs for creating and managing color space objects and obtaining basic color space attributes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/ZAg0DVEUREuW3nKXMQIZUQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062446Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=19E412D64D7B07139C187E1C7C54CA7DEF82B50722AF97C34F35D196E05B081E)

The initial APIs of this module are supported since API version 9. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { colorSpaceManager } from '@kit.ArkGraphics2D';

#### ColorSpace

Enumerates the color space types.

**System capability**: SystemCapability.Graphic.Graphic2D.ColorManager.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| UNKNOWN | 0 | Unknown type. |
| ADOBE\_RGB\_1998 | 1 | 
Adobe RGB (1998).

The conversion function is of the Adobe RGB (1998) type.

The encoding range is of the Full type.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| DCI\_P3 | 2 | 

DCI-P3.

The conversion function is of the Gamma 2.6 type.

The encoding range is of the Full type.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| DISPLAY\_P3 | 3 | 

Display P3.

The conversion function is of the SRGB type.

The encoding range is of the Full type.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| SRGB | 4 | 

SRGB.

The conversion function is of the SRGB type.

The encoding range is of the Full type.

This is the default color space type.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| CUSTOM | 5 | 

Custom type.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| BT70911+ | 6 | 

BT709.

The conversion function is of the BT709 type.

The encoding range is of the Full type.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| BT601\_EBU11+ | 7 | 

BT601\_P.

The conversion function is of the BT709 type.

The encoding range is of the Full type.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| BT601\_SMPTE\_C11+ | 8 | 

BT601\_N.

The conversion function is of the BT709 type.

The encoding range is of the Full type.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| BT2020\_HLG11+ | 9 | 

BT2020.

The conversion function is of the HLG type.

The encoding range is of the Full type.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| BT2020\_PQ11+ | 10 | 

BT2020.

The conversion function is of the PQ type.

The encoding range is of the Full type.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| P3\_HLG11+ | 11 | 

Display P3.

The conversion function is of the HLG type.

The encoding range is of the Full type.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| P3\_PQ11+ | 12 | 

Display P3.

The conversion function is of the PQ type.

The encoding range is of the Full type.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| ADOBE\_RGB\_1998\_LIMIT11+ | 13 | 

Adobe RGB (1998).

The conversion function is of the Adobe RGB (1998) type.

The encoding range is of the Limit type.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| DISPLAY\_P3\_LIMIT11+ | 14 | 

Display P3.

The conversion function is of the SRGB type.

The encoding range is of the Limit type.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| SRGB\_LIMIT11+ | 15 | 

SRGB.

The conversion function is of the SRGB type.

The encoding range is of the Limit type.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| BT709\_LIMIT11+ | 16 | 

BT709.

The conversion function is of the BT709 type.

The encoding range is of the Limit type.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| BT601\_EBU\_LIMIT11+ | 17 | 

BT601\_P.

The conversion function is of the BT709 type.

The encoding range is of the Limit type.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| BT601\_SMPTE\_C\_LIMIT11+ | 18 | 

BT601\_N.

The conversion function is of the BT709 type.

The encoding range is of the Limit type.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| BT2020\_HLG\_LIMIT11+ | 19 | 

BT2020.

The conversion function is of the HLG type.

The encoding range is of the Limit type.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| BT2020\_PQ\_LIMIT11+ | 20 | 

BT2020.

The conversion function is of the PQ type.

The encoding range is of the Limit type.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| P3\_HLG\_LIMIT11+ | 21 | 

Display P3.

The conversion function is of the HLG type.

The encoding range is of the Limit type.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| P3\_PQ\_LIMIT11+ | 22 | 

Display P3.

The conversion function is of the PQ type.

The encoding range is of the Limit type.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| LINEAR\_P311+ | 23 | 

Display P3.

The conversion function is of the Linear type.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| LINEAR\_SRGB11+ | 24 | 

SRGB.

The conversion function is of the Linear type.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| LINEAR\_BT70911+ | 24 | 

Same as that of LINEAR\_SRGB.

BT709.

The conversion function is of the Linear type.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| LINEAR\_BT202011+ | 25 | 

BT2020.

The conversion function is of the Linear type.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| H\_LOG18+ | 26 | 

BT2020.

The conversion function is of the LOG type.

 |
| DISPLAY\_BT2020\_SRGB20+ | 27 | 

DISPLAY BT2020.

The conversion function is of the SRGB type.

The encoding range is of the Full type.

 |
| DISPLAY\_SRGB11+ | 4 | 

Same as that of SRGB.

SRGB.

The conversion function is of the SRGB type.

The encoding range is of the Full type.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| DISPLAY\_P3\_SRGB11+ | 3 | 

Same as that of DISPLAY\_P3.

Display P3.

The conversion function is of the SRGB type.

The encoding range is of the Full type.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| DISPLAY\_P3\_HLG11+ | 11 | 

Same as that of P3\_HLG.

Display P3.

The conversion function is of the HLG type.

The encoding range is of the Full type.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| DISPLAY\_P3\_PQ11+ | 12 | 

Same as that of P3\_PQ.

Display P3.

The conversion function is of the PQ type.

The encoding range is of the Full type.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |

#### ColorSpacePrimaries

Defines the color space primaries. A color space is defined by chromaticity coordinates of the red, green, and blue additive primaries, the white point, and the gamma.

**System capability**: SystemCapability.Graphic.Graphic2D.ColorManager.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| redX | number | No | No | X coordinate of the red color in the color space. |
| redY | number | No | No | Y coordinate of the red color in the color space. |
| greenX | number | No | No | X coordinate of the green color in the color space. |
| greenY | number | No | No | Y coordinate of the green color in the color space. |
| blueX | number | No | No | X coordinate of the blue color in the color space. |
| blueY | number | No | No | Y coordinate of the blue color in the color space. |
| whitePointX | number | No | No | X coordinate of the white point in the color space. |
| whitePointY | number | No | No | Y coordinate of the white point in the color space. |

#### colorSpaceManager.create

create(colorSpaceName: ColorSpace): ColorSpaceManager

Creates a standard color space object.

**System capability**: SystemCapability.Graphic.Graphic2D.ColorManager.Core

**Parameters**

| Parameter | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| colorSpaceName | [ColorSpace](#colorspace) | Yes | 
Type of the color space.

**UNKNOWN** and **CUSTOM** cannot be used when creating standard color space objects.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [ColorSpaceManager](#colorspacemanager) | Color space object created. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [colorSpaceManager Error Codes](../../error-codes/colorspacemanager-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible cause: 1.Incorrect parameter type. 2.Parameter verification failed. |
| 18600001 | The parameter value is abnormal. |

**Example**

let colorSpace: colorSpaceManager.ColorSpaceManager;
try {
    colorSpace = colorSpaceManager.create(colorSpaceManager.ColorSpace.SRGB);
} catch (err) {
    console.error(\`Failed to create SRGB colorSpace. Cause: \` + JSON.stringify(err));
}

#### colorSpaceManager.create

create(primaries: ColorSpacePrimaries, gamma: number): ColorSpaceManager

Creates a custom color space object.

**System capability**: SystemCapability.Graphic.Graphic2D.ColorManager.Core

**Parameters**

| Parameter | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| primaries | [ColorSpacePrimaries](#colorspaceprimaries) | Yes | Primaries of the color space. |
| gamma | number | Yes | Gamma value of the color space, which is a floating point number greater than 0. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ColorSpaceManager](#colorspacemanager) | 
Color space object created.

The color space type is **CUSTOM** of [ColorSpace](#colorspace).

 |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [colorSpaceManager Error Codes](../../error-codes/colorspacemanager-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible cause: 1.Incorrect parameter type. 2.Parameter verification failed. |
| 18600001 | Invalid parameter value. Possible cause: Used UNKNOWN or CUSTOM color space type enum values to directly create a colorSpaceManager object. |

**Example**

let colorSpace: colorSpaceManager.ColorSpaceManager;
try {
    let primaries: colorSpaceManager.ColorSpacePrimaries = {
        redX: 0.1,
        redY: 0.1,
        greenX: 0.2,
        greenY: 0.2,
        blueX: 0.3,
        blueY: 0.3,
        whitePointX: 0.4,
        whitePointY: 0.4
    };
    let gamma = 2.2;
    colorSpace = colorSpaceManager.create(primaries, gamma);
} catch (err) {
    console.error(\`Failed to create colorSpace with customized primaries and gamma. Cause: \` + JSON.stringify(err));
}

#### ColorSpaceManager

Implements management of color space objects.

Before calling any of the following APIs, you must use [create()](#colorspacemanagercreate) to create a color space manager.

#### \[h2\]getColorSpaceName

getColorSpaceName(): ColorSpace

Obtains the color space type.

**System capability**: SystemCapability.Graphic.Graphic2D.ColorManager.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [ColorSpace](#colorspace) | Color space type. |

**Error codes**

For details about the error codes, see [colorSpaceManager Error Codes](../../error-codes/colorspacemanager-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 18600001 | The parameter value is abnormal. |

**Example**

try {
    let spaceName = colorSpace.getColorSpaceName();
} catch (err) {
    console.error(\`Fail to get colorSpace's name. Cause: \` + JSON.stringify(err));
}

#### \[h2\]getWhitePoint

getWhitePoint(): Array<number>

Obtains the coordinates of the white point in the color space.

**System capability**: SystemCapability.Graphic.Graphic2D.ColorManager.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Array<number> | Coordinates \[x, y\] of the white point. |

**Error codes**

For details about the error codes, see [colorSpaceManager Error Codes](../../error-codes/colorspacemanager-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 18600001 | Invalid parameter value. Possible cause: Used UNKNOWN or CUSTOM color space type enum values to directly create a colorSpaceManager object. |

**Example**

try {
    let point = colorSpace.getWhitePoint();
} catch (err) {
    console.error(\`Failed to get white point. Cause: \` + JSON.stringify(err));
}

#### \[h2\]getGamma

getGamma(): number

Obtains the gamma of the color space.

**System capability**: SystemCapability.Graphic.Graphic2D.ColorManager.Core

**Return value**

| Type | Description |
| :-- | :-- |
| number | Gamma of the color space. |

**Error codes**

For details about the error codes, see [colorSpaceManager Error Codes](../../error-codes/colorspacemanager-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 18600001 | Invalid parameter value. Possible cause: Used UNKNOWN or CUSTOM color space type enum values to directly create a colorSpaceManager object. |

**Example**

try {
    let gamma = colorSpace.getGamma();
} catch (err) {
    console.error(\`Failed to get gamma. Cause: \` + JSON.stringify(err));
}
