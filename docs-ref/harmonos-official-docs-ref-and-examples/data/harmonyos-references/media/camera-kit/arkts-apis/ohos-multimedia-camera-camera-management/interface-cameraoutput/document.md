# Interface (CameraOutput)

CameraOutput implements output information used in [Session](../interface-session/document.md). It is the base class of **output**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/hxOp6sz_RzaO-xAVa8S-0g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062425Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1C76798C49DAC88A5C9A4317C8CE1EA66F3DCBC1F2BE2AF7C5F0B606FB804621)

The initial APIs of this module are supported since API version 10. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { camera } from '@kit.CameraKit';

#### release

release(callback: AsyncCallback<void>): void

Releases output resources. This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the output resources are released successfully, **err** is **undefined**; otherwise, **err** is an error object with an error code defined in [CameraErrorCode](../enums/document.md#cameraerrorcode). |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400201 | Camera service fatal error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function releasePreviewOutput(previewOutput: camera.PreviewOutput): void {
  previewOutput.release((err: BusinessError) => {
    if (err) {
      console.error(\`Failed to release the Preview output instance ${err.code}\`);
      return;
    }
    console.info('Callback invoked to indicate that the preview output instance is released successfully.');
  });
}

function releaseVideoOutput(videoOutput: camera.VideoOutput): void {
  videoOutput.release((err: BusinessError) => {
    if (err) {
      console.error(\`Failed to release the video output instance ${err.code}\`);
      return;
    }
    console.info('Callback invoked to indicate that the video output instance is released successfully.');
  });
}

#### release

release(): Promise<void>

Releases output resources. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400201 | Camera service fatal error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function releasePreviewOutput(previewOutput: camera.PreviewOutput): void {
  previewOutput.release().then(() => {
    console.info('Promise returned to indicate that the preview output instance is released successfully.');
  }).catch((error: BusinessError) => {
    console.error(\`Failed to preview output release, error code: ${error.code}\`);
  });
}

function releaseVideoOutput(videoOutput: camera.VideoOutput): void {
  videoOutput.release().then(() => {
    console.info('Promise returned to indicate that the video output instance is released successfully.');
  }).catch((error: BusinessError) => {
    console.error(\`Failed to video output release, error code: ${error.code}\`);
  });
}
