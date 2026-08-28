# Interface (Flash)

Flash inherits from [FlashQuery](../interface-flashquery/document.md).

It provides APIs related to the flash.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/yaTprlarRz-wY78RQx_atA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062426Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F7ACDF0139EE64FDF8D11E1A08E372B6839CB4A7D97F4666CA4000845A51AD4B)

-   The initial APIs of this module are supported since API version 10. Newly added APIs will be marked with a superscript to indicate their earliest API version.
-   The initial APIs of this interface are supported since API version 11.

#### Modules to Import

import { camera } from '@kit.CameraKit';

#### setFlashMode11+

setFlashMode(flashMode: FlashMode): void

Sets a flash mode.

Before the setting, do the following checks:

1.  Use [hasFlash](../interface-flashquery/document.md#hasflash11) to check whether the camera device has flash.
2.  Use [isFlashModeSupported](../interface-flashquery/document.md#isflashmodesupported11) to check whether the camera device supports the flash mode.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| flashMode | [FlashMode](../enums/document.md#flashmode) | Yes | Flash mode. If the input parameter is null or undefined, it is treated as 0 and the flash is turned off. |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400103 | Session not config. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function setFlashMode(photoSession: camera.PhotoSession): void {
  try {
    photoSession.setFlashMode(camera.FlashMode.FLASH\_MODE\_AUTO);
  } catch (error) {
    // If the operation fails, error.code is returned and processed.
    let err = error as BusinessError;
    console.error(\`The setFlashMode call failed. error code: ${err.code}\`);
  }
}

#### getFlashMode11+

getFlashMode(): FlashMode

Obtains the flash mode in use.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [FlashMode](../enums/document.md#flashmode) | Flash mode obtained. If the operation fails, undefined is returned and an error code defined in [CameraErrorCode](../enums/document.md#cameraerrorcode) is thrown. |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400103 | Session not config. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function getFlashMode(photoSession: camera.PhotoSession): camera.FlashMode | undefined {
  let flashMode: camera.FlashMode | undefined = undefined;
  try {
    flashMode = photoSession.getFlashMode();
  } catch (error) {
    // If the operation fails, error.code is returned and processed.
    let err = error as BusinessError;
    console.error(\`The getFlashMode call failed.error code: ${err.code}\`);
  }
  return flashMode;
}
