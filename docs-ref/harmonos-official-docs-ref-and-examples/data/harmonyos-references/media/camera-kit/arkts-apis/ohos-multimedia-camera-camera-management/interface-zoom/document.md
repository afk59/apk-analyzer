# Interface (Zoom)

Zoom inherits from [ZoomQuery](../interface-zoomquery/document.md).

It provides APIs related to zoom operations.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/ZMwhpMRIQ12IGiSJIGPH6Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062427Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=68D27A5F7C7C090AB76CD223E0C438CA333E2FC521E2F72DCCFC0FB3371CCD37)

-   The initial APIs of this module are supported since API version 10. Newly added APIs will be marked with a superscript to indicate their earliest API version.
-   The initial APIs of this interface are supported since API version 11.

#### Modules to Import

import { camera } from '@kit.CameraKit';

#### setZoomRatio11+

setZoomRatio(zoomRatio: number): void

Sets a zoom ratio, with a maximum precision of two decimal places.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| zoomRatio | number | Yes | 
Zoom ratio. The supported zoom ratio range can be obtained by calling [getZoomRatioRange](../interface-zoomquery/document.md#getzoomratiorange11). If the value passed in is not within the supported range, the value within the precision range is retained.

It takes some time for the zoom ratio to take effect at the bottom layer. To obtain the correct zoom ratio, you need to wait for one to two frames.

 |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400103 | Session not config. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function setZoomRatio(photoSession: camera.PhotoSession, zoomRatioRange: Array<number>): void {
  if (zoomRatioRange === undefined || zoomRatioRange.length <= 0) {
    return;
  }
  let zoomRatio = zoomRatioRange\[0\];
  try {
    photoSession.setZoomRatio(zoomRatio);
  } catch (error) {
    // If the operation fails, error.code is returned and processed.
    let err = error as BusinessError;
    console.error(\`The setZoomRatio call failed. error code: ${err.code}\`);
  }
}

#### getZoomRatio11+

getZoomRatio(): number

Obtains the zoom ratio in use.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Return value**

| Type | Description |
| :-- | :-- |
| number | Zoom ratio obtained. If the operation fails, an error code defined in [CameraErrorCode](../enums/document.md#cameraerrorcode) is returned. |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400103 | Session not config. |
| 7400201 | Camera service fatal error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function getZoomRatio(photoSession: camera.PhotoSession): number {
  const invalidValue: number = -1;
  let zoomRatio: number = invalidValue;
  try {
    zoomRatio = photoSession.getZoomRatio();
  } catch (error) {
    // If the operation fails, error.code is returned and processed.
    let err = error as BusinessError;
    console.error(\`The getZoomRatio call failed. error code: ${err.code}\`);
  }
  return zoomRatio;
}

#### setSmoothZoom11+

setSmoothZoom(targetRatio: number, mode?: SmoothZoomMode): void

Sets smooth zoom.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| targetRatio | number | Yes | Target zoom ratio. The supported zoom ratio range can be obtained by calling [getZoomRatioRange](../interface-zoomquery/document.md#getzoomratiorange11). If the value passed in is not within the supported range, the value within the precision range is retained. |
| mode | [SmoothZoomMode](../enums/document.md#smoothzoommode11) | No | Smooth zoom mode. The default value is **0**. |

**Example**

function setSmoothZoom(sessionExtendsZoom: camera.Zoom, targetZoomRatio: number, mode: camera.SmoothZoomMode): void {
  sessionExtendsZoom.setSmoothZoom(targetZoomRatio, mode);
}
