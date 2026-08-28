# imageFeaturePicker

Main entrance for accessing the functions of the global color picker.

**System capability**: SystemCapability.Stylus.ColorPicker

**Start version**: 5.0.0(12)

#### Module Import

import { imageFeaturePicker } from '@kit.Penkit';

#### PickedColorInfo

Object of the color picker, including the basic information about the color picker.

**System capability**: SystemCapability.Stylus.ColorPicker

**Start version**: 5.0.0(12)

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

color

 | 

[common2D.Color](../../../../../graphics/arkgraphics-2d/arkts-apis/ohos-graphics-common2d-common-data-types-of-2d-graphics/document.md#color)

 | 

No

 | 

No

 | 

Color value.

 |
| 

colorSpace

 | 

[colorSpaceManager.ColorSpace](../../../../../graphics/arkgraphics-2d/arkts-apis/ohos-graphics-colorspacemanager-color-space-management/document.md#colorspace)

 | 

No

 | 

No

 | 

Color space.

 |
| 

timestamp

 | 

number

 | 

No

 | 

No

 | 

Timestamp, which is the time elapsed since the system startup, in ms.

 |

#### pickForResult

pickForResult(x?:number, y?:number):Promise<PickedColorInfo>

Picks up colors. This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.Stylus.ColorPicker

**Start version**: 5.0.0(12)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

x

 | 

number

 | 

No

 | 

X coordinate of the initial position of the color picker. The value ranges from 0 to the actual screen width, in pixels. The default value is **100**.

 |
| 

y

 | 

number

 | 

No

 | 

Y coordinate of the initial position of the color picker. The value ranges from 0 to the actual screen height, in pixels. The default value is **100**.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[PickedColorInfo](#section579673518478)\>

 | 

Promise used to return the color pick-up execution result.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Parameter error. Possible causes:

1\. Mandatory parameters are left unspecified.

2\. Incorrect parameter types.

3\. Parameter verification failed.

 |
| 

801

 | 

api is not supported.

 |
| 

1013900001

 | 

IPC communication failed.

 |
| 

1013900002

 | 

memory is insufficient.

 |
| 

1013900003

 | 

service is invalid.

 |
| 

1013900004

 | 

multi app call.

 |
| 

1013900005

 | 

background service call.

 |

**Example**:

async colorPick(x?: number, y?: number): Promise<imageFeaturePicker.PickedColorInfo> {
  const pickedColorInfo = await imageFeaturePicker.pickForResult(x, y);
  return pickedColorInfo;
}

#### pickForResult

pickForResult(x?:number, y?:number, showValue?:boolean):Promise<PickedColorInfo>

Picks up colors. This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.Stylus.ColorPicker

**Start version**: 5.1.0(18)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

x

 | 

number

 | 

No

 | 

X coordinate of the initial position of the color picker. The value ranges from 0 to the actual screen width, in pixels. The default value is **100**.

 |
| 

y

 | 

number

 | 

No

 | 

Y coordinate of the initial position of the color picker. The value ranges from 0 to the actual screen height, in pixels. The default value is **100**.

 |
| 

showValue

 | 

boolean

 | 

No

 | 

Indicates whether to display the RGB value. The options are **true** and **false**.

The default value is **false**.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[PickedColorInfo](#section579673518478)\>

 | 

Promise used to return the color pick-up execution result.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Parameter error. Possible causes:

1\. Mandatory parameters are left unspecified.

2\. Incorrect parameter types.

3\. Parameter verification failed.

 |
| 

801

 | 

api is not supported.

 |
| 

1013900001

 | 

IPC communication failed.

 |
| 

1013900002

 | 

memory is insufficient.

 |
| 

1013900003

 | 

service is invalid.

 |
| 

1013900004

 | 

multi app call.

 |
| 

1013900005

 | 

background service call.

 |

**Example**:

async colorPick(x?: number, y?: number): Promise<imageFeaturePicker.PickedColorInfo> {
  const pickedColorInfo = await imageFeaturePicker.pickForResult(x, y, true);
  return pickedColorInfo;
}
