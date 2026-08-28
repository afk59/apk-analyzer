# Interface (Focus)

Focus inherits from [FocusQuery](../interface-focusquery/document.md).

It provides APIs related to focus operations.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/QmCQSwSVSSi2iroXQJLeng/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062426Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9418CFD07A7A3EB84D73F2A39C704809D221117C212750C67424FDDC497BA00F)

-   The initial APIs of this module are supported since API version 10. Newly added APIs will be marked with a superscript to indicate their earliest API version.
-   The initial APIs of this interface are supported since API version 11.

#### Modules to Import

import { camera } from '@kit.CameraKit';

#### setFocusMode11+

setFocusMode(afMode: FocusMode): void

Sets a focus mode.

Before the setting, call [isFocusModeSupported](../interface-focusquery/document.md#isfocusmodesupported11) to check whether the focus mode is supported.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| afMode | [FocusMode](../enums/document.md#focusmode) | Yes | Focus mode. If the input parameter is null or undefined, it is treated as 0 and manual focus is used. |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400103 | Session not config. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function setFocusMode(photoSession: camera.PhotoSession): void {
  try {
    photoSession.setFocusMode(camera.FocusMode.FOCUS\_MODE\_AUTO);
  } catch (error) {
    // If the operation fails, error.code is returned and processed.
    let err = error as BusinessError;
    console.error(\`The setFocusMode call failed. error code: ${err.code}\`);
  }
}

#### getFocusMode11+

getFocusMode(): FocusMode

Obtains the focus mode in use.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [FocusMode](../enums/document.md#focusmode) | Focus mode obtained. If the operation fails, undefined is returned and an error code defined in [CameraErrorCode](../enums/document.md#cameraerrorcode) is thrown. |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400103 | Session not config. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function getFocusMode(photoSession: camera.PhotoSession): camera.FocusMode | undefined {
  let afMode: camera.FocusMode | undefined = undefined;
  try {
    afMode = photoSession.getFocusMode();
  } catch (error) {
    // If the operation fails, error.code is returned and processed.
    let err = error as BusinessError;
    console.error(\`The getFocusMode call failed. error code: ${err.code}\`);
  }
  return afMode;
}

#### setFocusPoint11+

setFocusPoint(point: Point): void

Sets the focal point. The focal point must be in the coordinate system (0-1), where the top-left corner is {0, 0} and the bottom-right corner is {1, 1}.

The coordinate system is based on the horizontal device direction with the device's charging port on the right. If the layout of the preview screen of an application is based on the vertical direction with the charging port on the lower side, the layout width and height are {w, h}, and the touch point is {x, y}, then the coordinate point after conversion is {y/h, 1-x/w}.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| point | [Point](../interfaces-others/document.md#point) | Yes | Focal point. The value range of x and y must be within \[0, 1\]. If a value less than 0 is passed, the value **0** is used. If a value greater than **1** is passed, the value **1** is used. |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400103 | Session not config. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function setFocusPoint(photoSession: camera.PhotoSession): void {
  const focusPoint: camera.Point = {x: 1, y: 1};
  try {
    photoSession.setFocusPoint(focusPoint);
  } catch (error) {
    // If the operation fails, error.code is returned and processed.
    let err = error as BusinessError;
    console.error(\`The setFocusPoint call failed. error code: ${err.code}\`);
  }
}

#### getFocusPoint11+

getFocusPoint(): Point

Obtains the focal point in use.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [Point](../interfaces-others/document.md#point) | Focal point obtained. If the operation fails, an error code defined in [CameraErrorCode](../enums/document.md#cameraerrorcode) is returned. |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400103 | Session not config. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function getFocusPoint(photoSession: camera.PhotoSession): camera.Point | undefined {
  let point: camera.Point | undefined = undefined;
  try {
    point = photoSession.getFocusPoint();
  } catch (error) {
    // If the operation fails, error.code is returned and processed.
    let err = error as BusinessError;
    console.error(\`The getFocusPoint call failed. error code: ${err.code}\`);
  }
  return point;
}

#### getFocalLength11+

getFocalLength(): number

Obtains the focal length in use.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Return value**

| Type | Description |
| :-- | :-- |
| number | Focal length, in mm. If the operation fails, an error code defined in [CameraErrorCode](../enums/document.md#cameraerrorcode) is returned. |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400103 | Session not config. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function getFocalLength(photoSession: camera.PhotoSession): number {
  const invalidValue: number = -1;
  let focalLength: number = invalidValue;
  try {
    focalLength = photoSession.getFocalLength();
  } catch (error) {
    // If the operation fails, error.code is returned and processed.
    let err = error as BusinessError;
    console.error(\`The getFocalLength call failed. error code: ${err.code}\`);
  }
  return focalLength;
}
