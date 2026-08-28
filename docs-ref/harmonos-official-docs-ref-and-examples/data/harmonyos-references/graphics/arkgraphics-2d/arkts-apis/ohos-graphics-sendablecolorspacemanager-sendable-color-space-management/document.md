# @ohos.graphics.sendableColorSpaceManager (Sendable Color Space Management)

The **sendableColorSpaceManager** module provides APIs for creating and managing sendable color space objects and obtaining basic attributes of sendable color spaces.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/CXO7FJpcQ0SkbkPk7W-mqg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062446Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F37D84878815A6ED38178C040B14E113675908205820C64F93FFF4794ADC2A95)

The initial APIs of this module are supported since API version 12. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { sendableColorSpaceManager } from '@kit.ArkGraphics2D';

#### ISendable

type ISendable = lang.ISendable

**ISendable** is the parent type of all sendable types except null and undefined. It does not have any necessary methods or properties.

**System capability**: SystemCapability.Graphic.Graphic2D.ColorManager.Core

| Type | Description |
| :-- | :-- |
| [lang.ISendable](../../../../application-framework/arkts/arkts-apis/arkts-lang-arkts-base-capability/document.md#langisendable) | Parent type of all sendable types. |

#### sendableColorSpaceManager.create

create(colorSpaceName: colorSpaceManager.ColorSpace): ColorSpaceManager

Creates a standard color space object that is sendable.

**System capability**: SystemCapability.Graphic.Graphic2D.ColorManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| colorSpaceName | [colorSpaceManager.ColorSpace](../ohos-graphics-colorspacemanager-color-space-management/document.md#colorspace) | Yes | 
Type of the color space.

**UNKNOWN** and **CUSTOM** cannot be used when creating standard color space objects.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [ColorSpaceManager](#colorspacemanager) | 
Sendable color space object created.

This instance inherits from **ISendable** and can be passed by reference between concurrent ArkTS instances (including the main thread and the worker threads of TaskPool or Worker). For details, see [Using Sendable Objects](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/sendable-guide).

 |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [colorSpaceManager Error Codes](../../error-codes/colorspacemanager-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible cause: 1.Incorrect parameter type. 2.Parameter verification failed. |
| 18600001 | The parameter value is abnormal. |

**Example**

import { colorSpaceManager, sendableColorSpaceManager } from '@kit.ArkGraphics2D';
let colorSpace: sendableColorSpaceManager.ColorSpaceManager;
colorSpace = sendableColorSpaceManager.create(colorSpaceManager.ColorSpace.SRGB);

#### sendableColorSpaceManager.create

create(primaries: colorSpaceManager.ColorSpacePrimaries, gamma: number): ColorSpaceManager

Creates a custom color space object that is sendable.

**System capability**: SystemCapability.Graphic.Graphic2D.ColorManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| primaries | [colorSpaceManager.ColorSpacePrimaries](../ohos-graphics-colorspacemanager-color-space-management/document.md#colorspaceprimaries) | Yes | Primaries of the color space. |
| gamma | number | Yes | Gamma value of the color space, which is a floating point number greater than 0. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ColorSpaceManager](#colorspacemanager) | 
Sendable color space object created.

The color space type is **CUSTOM**, which is one of the enumerated values of [colorSpaceManager.ColorSpace](../ohos-graphics-colorspacemanager-color-space-management/document.md#colorspace).

This instance inherits from **ISendable** and can be passed by reference between concurrent ArkTS instances (including the main thread and the worker threads of TaskPool or Worker). For details, see [Using Sendable Objects](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/sendable-guide).

 |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [colorSpaceManager Error Codes](../../error-codes/colorspacemanager-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible cause: 1.Incorrect parameter type. 2.Parameter verification failed. |
| 18600001 | The parameter value is abnormal. |

**Example**

import { colorSpaceManager, sendableColorSpaceManager } from '@kit.ArkGraphics2D';
let colorSpace: sendableColorSpaceManager.ColorSpaceManager;
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
let gamma: number = 2.2;
colorSpace = sendableColorSpaceManager.create(primaries, gamma);

#### ColorSpaceManager

Implements management of color space objects.

Before calling any of the following APIs, you must use [create()](#sendablecolorspacemanagercreate) to create a color space manager.

#### \[h2\]getColorSpaceName

getColorSpaceName(): colorSpaceManager.ColorSpace

Obtains the color space type.

**System capability**: SystemCapability.Graphic.Graphic2D.ColorManager.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [colorSpaceManager.ColorSpace](../ohos-graphics-colorspacemanager-color-space-management/document.md#colorspace) | Color space type. |

**Error codes**

For details about the error codes, see [colorSpaceManager Error Codes](../../error-codes/colorspacemanager-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 18600001 | The parameter value is abnormal. |

**Example**

let spaceName: colorSpaceManager.ColorSpace = colorSpace.getColorSpaceName();

#### \[h2\]getWhitePoint

getWhitePoint(): collections.Array<number>

Obtains the coordinates of the white point in the color space.

**System capability**: SystemCapability.Graphic.Graphic2D.ColorManager.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [collections.Array<number>](../../../../application-framework/arkts/arkts-apis/arkts-collections-arkts-collections/class-array/document.md) | Coordinates \[x, y\] of the white point. |

**Error codes**

For details about the error codes, see [colorSpaceManager Error Codes](../../error-codes/colorspacemanager-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 18600001 | The parameter value is abnormal. |

**Example**

import { collections } from '@kit.ArkTS';
let point: collections.Array<number> = colorSpace.getWhitePoint();

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
| 18600001 | The parameter value is abnormal. |

**Example**

let gamma: number = colorSpace.getGamma();
