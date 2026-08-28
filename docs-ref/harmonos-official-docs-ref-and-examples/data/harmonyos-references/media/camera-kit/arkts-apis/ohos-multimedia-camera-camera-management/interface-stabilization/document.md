# Interface (Stabilization)

**Stabilization** inherits from [StabilizationQuery](../interface-stabilizationquery/document.md).

It provides APIs to set video stabilization.

Video stabilization can be set only when the session has a recording stream ([VideoOutput](../interface-videooutput/document.md)). Among the enums of [VideoStabilizationMode](../enums/document.md#videostabilizationmode), the **HIGH** mode only takes effect when the resolution set in [Profile](../interfaces-others/document.md#profile) is 1920×1080.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/TWw7PklHSrWq3_09KQ8SrA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062426Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=99FECB9CA4DD294F5DCAC401263BE780E9FF4141DA6FD824A6E7D613FF1E568C)

-   The initial APIs of this module are supported since API version 10. Newly added APIs will be marked with a superscript to indicate their earliest API version.
-   The initial APIs of this interface are supported since API version 11.

#### Modules to Import

import { camera } from '@kit.CameraKit';

#### getActiveVideoStabilizationMode11+

getActiveVideoStabilizationMode(): VideoStabilizationMode

Obtains the video stabilization mode in use.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [VideoStabilizationMode](../enums/document.md#videostabilizationmode) | Video stabilization mode obtained. If the API call fails, undefined is returned. |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400103 | Session not config. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function getActiveVideoStabilizationMode(videoSession: camera.VideoSession): camera.VideoStabilizationMode | undefined {
  let vsMode: camera.VideoStabilizationMode | undefined = undefined;
  try {
    vsMode = videoSession.getActiveVideoStabilizationMode();
  } catch (error) {
    // If the operation fails, error.code is returned and processed.
    let err = error as BusinessError;
    console.error(\`The getActiveVideoStabilizationMode call failed. error code: ${err.code}\`);
  }
  return vsMode;
}

#### setVideoStabilizationMode11+

setVideoStabilizationMode(mode: VideoStabilizationMode): void

Sets a video stabilization mode. Before the setting, call [isVideoStabilizationModeSupported](../interface-stabilizationquery/document.md#isvideostabilizationmodesupported11) to check whether the target video stabilization mode is supported. It is recommended that you set the video stabilization mode between [commitConfig](../interface-session/document.md#commitconfig11-1) and [Start](../interface-session/document.md#start11-1).

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| mode | [VideoStabilizationMode](../enums/document.md#videostabilizationmode) | Yes | Video stabilization mode. |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400103 | Session not config. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function setVideoStabilizationMode(videoSession: camera.VideoSession): void {
  try {
    videoSession.setVideoStabilizationMode(camera.VideoStabilizationMode.OFF);
  } catch (error) {
    // If the operation fails, error.code is returned and processed.
    let err = error as BusinessError;
    console.error(\`The setVideoStabilizationMode call failed. error code: ${err.code}\`);
  }
}
