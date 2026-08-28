# Interface (FocusQuery)

FocusQuery provides APIs to check whether a focus mode is supported.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/WmW5bN_ERpmPFV1Q4k7EJA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062426Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=70BB20053A69F43594F423A68FCB6768CF75D432F52AF85FDC70A778248C8D22)

-   The initial APIs of this module are supported since API version 10. Newly added APIs will be marked with a superscript to indicate their earliest API version.
-   This interface was first introduced in API version 12. In this version, a compatibility change was made that preserved the initial version information of inner elements. As a result, you might see outer element's @since version number being higher than that of the inner elements. However, this discrepancy does not affect the functionality of the interface.

#### Modules to Import

import { camera } from '@kit.CameraKit';

#### isFocusModeSupported11+

isFocusModeSupported(afMode: FocusMode): boolean

Checks whether a focus mode is supported.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| afMode | [FocusMode](../enums/document.md#focusmode) | Yes | Focus mode. If the input parameter is null or undefined, it is treated as 0 and manual focus is used. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result for the support of the focus mode. **true** if supported, **false** otherwise. If the operation fails, undefined is returned and an error code defined in [CameraErrorCode](../enums/document.md#cameraerrorcode) is thrown. |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400103 | Session not config, only throw in session usage. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function isFocusModeSupported(photoSession: camera.PhotoSession): boolean {
  let status: boolean = false;
  try {
    status = photoSession.isFocusModeSupported(camera.FocusMode.FOCUS\_MODE\_AUTO);
  } catch (error) {
    // If the operation fails, error.code is returned and processed.
    let err = error as BusinessError;
    console.error(\`The isFocusModeSupported call failed. error code: ${err.code}\`);
  }
  return status;
}
