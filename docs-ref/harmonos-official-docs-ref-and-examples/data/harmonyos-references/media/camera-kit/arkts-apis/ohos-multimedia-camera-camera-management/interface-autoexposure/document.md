# Interface (AutoExposure)

AutoExposure inherits from [AutoExposureQuery](../interface-autoexposurequery/document.md).

It provides APIs related to auto exposure.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/dFF1fJjSQ9KRJ9TklxIDnw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062425Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E065A0235559F85C796D31255E281746490EDBDDF25FDC2B41BAD30E618855AF)

-   The initial APIs of this module are supported since API version 10. Newly added APIs will be marked with a superscript to indicate their earliest API version.
-   The initial APIs of this interface are supported since API version 11.

#### Modules to Import

import { camera } from '@kit.CameraKit';

#### getExposureMode11+

getExposureMode(): ExposureMode

Obtains the exposure mode in use.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/TJZiQRmJRC-9bdYvIsldZA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062425Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6BB55BFADAAB1595684840C7A969CA3BC6013C4F153CD23655DF5721E8392199)

This API directly returns an invalid value if you have not set the exposure mode using [setExposureMode](#setexposuremode11).

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [ExposureMode](../enums/document.md#exposuremode) | Exposure mode obtained. If the operation fails, undefined is returned and an error code defined in [CameraErrorCode](../enums/document.md#cameraerrorcode) is thrown. |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400103 | Session not config. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function getExposureMode(photoSession: camera.PhotoSession): camera.ExposureMode | undefined {
  let exposureMode: camera.ExposureMode | undefined = undefined;
  try {
    exposureMode = photoSession.getExposureMode();
  } catch (error) {
    // If the operation fails, error.code is returned and processed.
    let err = error as BusinessError;
    console.error(\`The getExposureMode call failed. error code: ${err.code}\`);
  }
  return exposureMode;
}

#### setExposureMode11+

setExposureMode(aeMode: ExposureMode): void

Sets an exposure mode. Before the setting, call [isExposureModeSupported](../interface-autoexposurequery/document.md#isexposuremodesupported11) to check whether the exposure mode is supported.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| aeMode | [ExposureMode](../enums/document.md#exposuremode) | Yes | Exposure mode. If the input parameter is null or undefined, it is treated as 0 and exposure is locked. |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400102 | Operation not allowed. |
| 7400103 | Session not config. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function setExposureMode(photoSession: camera.PhotoSession): void {
  try {
    photoSession.setExposureMode(camera.ExposureMode.EXPOSURE\_MODE\_LOCKED);
  } catch (error) {
    // If the operation fails, error.code is returned and processed.
    let err = error as BusinessError;
    console.error(\`The setExposureMode call failed. error code: ${err.code}\`);
  }
}

#### getMeteringPoint11+

getMeteringPoint(): Point

Obtains the metering point of the camera device.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [Point](../interfaces-others/document.md#point) | Metering point obtained. If the operation fails, an error code defined in [CameraErrorCode](../enums/document.md#cameraerrorcode) is returned. |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400103 | Session not config. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function getMeteringPoint(photoSession: camera.PhotoSession): camera.Point | undefined {
  let exposurePoint: camera.Point | undefined = undefined;
  try {
    exposurePoint = photoSession.getMeteringPoint();
  } catch (error) {
    // If the operation fails, error.code is returned and processed.
    let err = error as BusinessError;
    console.error(\`The getMeteringPoint call failed. error code: ${err.code}\`);
  }
  return exposurePoint;
}

#### setMeteringPoint11+

setMeteringPoint(point: Point): void

Sets the metering point, which is the center point of the metering rectangle. The metering point must be in the coordinate system (0-1), where the top-left corner is {0, 0} and the bottom-right corner is {1, 1}.

The coordinate system is based on the horizontal device direction with the device's charging port on the right. If the layout of the preview screen of an application is based on the vertical direction with the charging port on the lower side, the layout width and height are {w, h}, and the touch point is {x, y}, then the coordinate point after conversion is {y/h, 1-x/w}.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| point | [Point](../interfaces-others/document.md#point) | Yes | Metering point. The value range of x and y must be within \[0, 1\]. If a value less than 0 is passed, the value **0** is used. If a value greater than **1** is passed, the value **1** is used. |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400103 | Session not config. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function setMeteringPoint(photoSession: camera.PhotoSession): void {
  const point: camera.Point = {x: 1, y: 1};
  try {
    photoSession.setMeteringPoint(point);
  } catch (error) {
    // If the operation fails, error.code is returned and processed.
    let err = error as BusinessError;
    console.error(\`The setMeteringPoint call failed. error code: ${err.code}\`);
  }
}

#### setExposureBias11+

setExposureBias(exposureBias: number): void

Sets an exposure compensation value (EV).

Before the setting, you are advised to use [getExposureBiasRange](../interface-autoexposurequery/document.md#getexposurebiasrange11) to obtain the supported values.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| exposureBias | number | Yes | 
EV. The supported EV range can be obtained by calling [getExposureBiasRange](../interface-autoexposurequery/document.md#getexposurebiasrange11). If the value passed is not within the supported range, the nearest critical point is used.

Exposure compensation is adjusted in steps, and the step size may vary across devices due to hardware differences. For example, if the step size is 0.5, setting a value of 1.2 would result in an actual effective exposure compensation value of 1.0.

If the operation fails, an error code defined in [CameraErrorCode](../enums/document.md#cameraerrorcode) is returned.

 |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400102 | Operation not allowed. |
| 7400103 | Session not config. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function setExposureBias(photoSession: camera.PhotoSession, biasRangeArray: Array<number>): void {
  if (biasRangeArray && biasRangeArray.length > 0) {
    let exposureBias = biasRangeArray\[0\];
    try {
      photoSession.setExposureBias(exposureBias);
    } catch (error) {
      // If the operation fails, error.code is returned and processed.
      let err = error as BusinessError;
      console.error(\`The setExposureBias call failed. error code: ${err.code}\`);
    }
  }
}

#### getExposureValue11+

getExposureValue(): number

Obtains the exposure value in use.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Return value**

| Type | Description |
| :-- | :-- |
| number | 
Exposure value obtained. There is a step for EV. For example, if the step is 0.5 and this parameter is set to 1.2, the EV that takes effect is 1.0.

If the operation fails, an error code defined in [CameraErrorCode](../enums/document.md#cameraerrorcode) is returned.

 |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400103 | Session not config. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function getExposureValue(photoSession: camera.PhotoSession): number {
  const invalidValue: number = -1;
  let exposureValue: number = invalidValue;
  try {
    exposureValue = photoSession.getExposureValue();
  } catch (error) {
    // If the operation fails, error.code is returned and processed.
    let err = error as BusinessError;
    console.error(\`The getExposureValue call failed. error code: ${err.code}\`);
  }
  return exposureValue;
}
