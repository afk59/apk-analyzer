# Interface (FlashQuery)

FlashQuery provides APIs to query the flash status and mode of a camera device.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/lCU7N54NQYqyz9uETpEt5g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062426Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DD47991E7482C43D7614DE08412EFBB808437BEB87E040B58A599DC5F4E0BE05)

-   The initial APIs of this module are supported since API version 10. Newly added APIs will be marked with a superscript to indicate their earliest API version.
-   This interface was first introduced in API version 12. In this version, a compatibility change was made that preserved the initial version information of inner elements. As a result, you might see outer element's @since version number being higher than that of the inner elements. However, this discrepancy does not affect the functionality of the interface.

#### Modules to Import

import { camera } from '@kit.CameraKit';

#### hasFlash11+

hasFlash(): boolean

Checks whether the camera device has flash.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result for whether the camera device has flash. **true** if it has flash, **false** otherwise. If the operation fails, an error code defined in [CameraErrorCode](../enums/document.md#cameraerrorcode) is returned. |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400103 | Session not config, only throw in session usage. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function hasFlash(photoSession: camera.PhotoSession): boolean {
  let status: boolean = false;
  try {
    status = photoSession.hasFlash();
  } catch (error) {
    // If the operation fails, error.code is returned and processed.
    let err = error as BusinessError;
    console.error(\`The hasFlash call failed. error code: ${err.code}\`);
  }
  return status;
}

#### isFlashModeSupported11+

isFlashModeSupported(flashMode: FlashMode): boolean

Checks whether a flash mode is supported.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| flashMode | [FlashMode](../enums/document.md#flashmode) | Yes | Flash mode. If the input parameter is null or undefined, it is treated as 0 and the flash is turned off. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result for the support of the flash mode. **true** if supported, **false** otherwise. If the operation fails, undefined is returned and an error code defined in [CameraErrorCode](../enums/document.md#cameraerrorcode) is thrown. |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400103 | Session not config, only throw in session usage. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function isFlashModeSupported(photoSession: camera.PhotoSession): boolean {
  let status: boolean = false;
  try {
    status = photoSession.isFlashModeSupported(camera.FlashMode.FLASH\_MODE\_AUTO);
  } catch (error) {
    // If the operation fails, error.code is returned and processed.
    let err = error as BusinessError;
    console.error(\`The isFlashModeSupported call failed. error code: ${err.code}\`);
  }
  return status;
}
