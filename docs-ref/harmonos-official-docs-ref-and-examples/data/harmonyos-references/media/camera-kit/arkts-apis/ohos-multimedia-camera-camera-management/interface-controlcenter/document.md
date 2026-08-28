# Interface (ControlCenter)

ControlCenter inherits from [ControlCenterQuery](../interface-controlcenterquery/document.md).

It is used to enable the camera controller.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/nuTKgS3TQRiPKNMnWW7XtA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062426Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=22B439341B6D30E19B461082DC801F1B67FF4E152BCDC14F6BFD0F46B36A92E9)

-   The initial APIs of this module are supported since API version 10. Newly added APIs will be marked with a superscript to indicate their earliest API version.
-   The initial APIs of this interface are supported since API version 20.

#### Modules to Import

import { camera } from '@kit.CameraKit';

#### enableControlCenter20+

enableControlCenter(enabled: boolean): void

Enables the camera controller.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| enabled | boolean | Yes | Whether to enable or disable the camera controller. **true** to enable, **false** otherwise. |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400103 | Session not config. |

**Example**

function enableControlCenter(videoSession: camera.VideoSession, enable: boolean): void {
    let isSupported: boolean = videoSession.isControlCenterSupported();
    if (isSupported) {
        videoSession.enableControlCenter(enable);
    }
}
