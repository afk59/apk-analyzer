# Interface (StabilizationQuery)

StabilizationQuery provides APIs to check the support for video stabilization.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/HxrG4kchQK2efyZoVDNvwg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062426Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=74F5D854028D915AD003EA881EE3E564F4A17A7EB822873F40E666784A4B7E36)

-   The initial APIs of this module are supported since API version 10. Newly added APIs will be marked with a superscript to indicate their earliest API version.
-   This interface was first introduced in API version 12. In this version, a compatibility change was made that preserved the initial version information of inner elements. As a result, you might see outer element's @since version number being higher than that of the inner elements. However, this discrepancy does not affect the functionality of the interface.

#### Modules to Import

import { camera } from '@kit.CameraKit';

#### isVideoStabilizationModeSupported11+

isVideoStabilizationModeSupported(vsMode: VideoStabilizationMode): boolean

Checks whether a video stabilization mode is supported.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| vsMode | [VideoStabilizationMode](../enums/document.md#videostabilizationmode) | Yes | Video stabilization mode. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result for the support of the video stabilization mode. **true** if supported, **false** otherwise. If the operation fails, undefined is returned and an error code defined in [CameraErrorCode](../enums/document.md#cameraerrorcode) is thrown. |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400103 | Session not config, only throw in session usage. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function isVideoStabilizationModeSupported(videoSession: camera.VideoSession): boolean {
  let isSupported: boolean = false;
  try {
    isSupported = videoSession.isVideoStabilizationModeSupported(camera.VideoStabilizationMode.OFF);
  } catch (error) {
    // If the operation fails, error.code is returned and processed.
    let err = error as BusinessError;
    console.error(\`The isVideoStabilizationModeSupported call failed. error code: ${err.code}\`);
  }
  return isSupported;
}
