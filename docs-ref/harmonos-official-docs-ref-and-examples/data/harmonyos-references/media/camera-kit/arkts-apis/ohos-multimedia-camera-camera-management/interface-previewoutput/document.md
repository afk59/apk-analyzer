# Interface (PreviewOutput)

**PreviewOutput** implements preview output. It inherits from [CameraOutput](../interface-cameraoutput/document.md).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/67aF0eVlQSOUGwNXhFPYHA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062426Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=14C9B751682F322105C2ABF0D8BEC8633FE058D1254F65E0716FBE622F84F24C)

The initial APIs of this module are supported since API version 10. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { camera } from '@kit.CameraKit';

#### on('frameStart')

on(type: 'frameStart', callback: AsyncCallback<void>): void

Subscribes to preview frame start events. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/c8j1kOdvROiCbhUnHb5q6g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062426Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=469A3DAF1D93BA307D75655C49DFC86158BBA52DE7096848B9FB41A86D5BE34D)

Currently, you cannot use **off()** to unregister the callback in the callback method of **on()**.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'frameStart'**. The event can be listened for when a previewOutput instance is created. This event is triggered and returned when the bottom layer starts exposure for the first time. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. The preview starts as long as this event is returned. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function callback(err: BusinessError): void {
  if (err !== undefined && err.code !== 0) {
    console.error(\`Callback Error, errorCode: ${err.code}\`);
    return;
  }
  console.info('Preview frame started');
}

function registerPreviewOutputFrameStart(previewOutput: camera.PreviewOutput): void {
  previewOutput.on('frameStart', callback);
}

#### off('frameStart')

off(type: 'frameStart', callback?: AsyncCallback<void>): void

Unsubscribes from preview frame start events.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'frameStart'**. The event can be listened for when a previewOutput instance is created. |
| callback | AsyncCallback<void> | No | Callback used to return the result. If this parameter is specified, the subscription to the specified event with the specified callback is canceled. (The callback object cannot be an anonymous function.) Otherwise, the subscriptions to the specified event with all the callbacks are canceled. |

**Example**

function unregisterPreviewOutputFrameStart(previewOutput: camera.PreviewOutput): void {
  previewOutput.off('frameStart');
}

#### on('frameEnd')

on(type: 'frameEnd', callback: AsyncCallback<void>): void

Subscribes to preview frame end events. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/lVum6tWERbK47kAhuUz9KQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062426Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F436A42C968D2CFC1299B507F84EAAF0291197BFE71DA18C989155BD50883826)

Currently, you cannot use **off()** to unregister the callback in the callback method of **on()**.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'frameEnd'**. The event can be listened for when a previewOutput instance is created. This event is triggered and returned when the last frame of preview ends. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. The preview ends as long as this event is returned. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function callback(err: BusinessError): void {
  if (err !== undefined && err.code !== 0) {
    console.error(\`Callback Error, errorCode: ${err.code}\`);
    return;
  }
  console.info('Preview frame ended');
}

function registerPreviewOutputFrameEnd(previewOutput: camera.PreviewOutput): void {
  previewOutput.on('frameEnd', callback);
}

#### off('frameEnd')

off(type: 'frameEnd', callback?: AsyncCallback<void>): void

Unsubscribes from preview frame end events.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'frameEnd'**. The event can be listened for when a previewOutput instance is created. |
| callback | AsyncCallback<void> | No | Callback used to return the result. If this parameter is specified, the subscription to the specified event with the specified callback is canceled. (The callback object cannot be an anonymous function.) Otherwise, the subscriptions to the specified event with all the callbacks are canceled. |

**Example**

function unregisterPreviewOutputFrameEnd(previewOutput: camera.PreviewOutput): void {
  previewOutput.off('frameEnd');
}

#### on('error')

on(type: 'error', callback: ErrorCallback): void

Subscribes to PreviewOutput error events. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3/v3/bn0svcpRQT6f4x0Ef7xCtQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062426Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=39929FD409770E8EA8EAEB279E7D487C5C666EF1B19779FDC7FA10E6D1E7DB44)

Currently, you cannot use **off()** to unregister the callback in the callback method of **on()**.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'error'**. The event can be listened for when a previewOutput instance is created. This event is triggered and the corresponding error message is returned when an error occurs during the use of a preview-related API such as [Session.start](../interface-session/document.md#start11-1) or [CameraOutput.release](../interface-cameraoutput/document.md#release-1). |
| callback | [ErrorCallback](../../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#errorcallback) | Yes | Callback used to return an error code defined in [CameraErrorCode](../enums/document.md#cameraerrorcode). |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function callback(previewOutputError: BusinessError): void {
  console.error(\`Preview output error code: ${previewOutputError.code}\`);
}

function registerPreviewOutputError(previewOutput: camera.PreviewOutput): void {
  previewOutput.on('error', callback)
}

#### off('error')

off(type: 'error', callback?: ErrorCallback): void

Unsubscribes from PreviewOutput error events.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'error'**. The event can be listened for when a previewOutput instance is created. |
| callback | [ErrorCallback](../../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#errorcallback) | No | Callback used to return the result. If this parameter is specified, the subscription to the specified event with the specified callback is canceled. (The callback object cannot be an anonymous function.) Otherwise, the subscriptions to the specified event with all the callbacks are canceled. |

**Example**

function unregisterPreviewOutputError(previewOutput: camera.PreviewOutput): void {
  previewOutput.off('error');
}

#### getSupportedFrameRates12+

getSupportedFrameRates(): Array<FrameRateRange>

Obtains the supported frame rates.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Array<[FrameRateRange](../interfaces-others/document.md#frameraterange)\> | Array of supported frame rates. If the API call fails, undefined is returned. |

**Example**

function getSupportedFrameRates(previewOutput: camera.PreviewOutput): Array<camera.FrameRateRange> {
  let supportedFrameRatesArray: Array<camera.FrameRateRange> = previewOutput.getSupportedFrameRates();
  return supportedFrameRatesArray;
}

#### setFrameRate12+

setFrameRate(minFps: number, maxFps: number): void

Sets a frame rate range for preview streams. The range must be within the supported frame rate range,

which can be obtained by calling [getSupportedFrameRates](#getsupportedframerates12).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/-jsp-vvHTLuxYA51IkqvaQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062426Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E307D7FE9D8D9834661E3A3D4CD3288C7FF89FB6E16EF1ACB84D8D9FA93E11B5)

This API is valid only in [PhotoSession](../interface-photosession/document.md) or [VideoSession](../interface-videosession/document.md) mode.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| minFps | number | Yes | Minimum frame rate, in fps. When the maximum value is less than the minimum value, the API does not take effect. |
| maxFps | number | Yes | Maximum frame rate, in fps. When the minimum value is greater than the maximum value, the API does not take effect. |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400101 | Parameter missing or parameter type incorrect. |
| 7400110 | Unresolved conflicts with current configurations. |

**Example**

function setFrameRateRange(previewOutput: camera.PreviewOutput, frameRateRange: Array<number>): void {
  previewOutput.setFrameRate(frameRateRange\[0\], frameRateRange\[1\]);
}

#### getActiveFrameRate12+

getActiveFrameRate(): FrameRateRange

Obtains the configured frame rate range.

This API is valid only after [setFrameRate](#setframerate12) is called to set a frame rate range for preview streams.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [FrameRateRange](../interfaces-others/document.md#frameraterange) | Frame rate range. |

**Example**

function getActiveFrameRate(previewOutput: camera.PreviewOutput): camera.FrameRateRange {
  let activeFrameRate: camera.FrameRateRange = previewOutput.getActiveFrameRate();
  return activeFrameRate;
}

#### getActiveProfile12+

getActiveProfile(): Profile

Obtains the profile that takes effect currently.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [Profile](../interfaces-others/document.md#profile) | Profile obtained. |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400201 | Camera service fatal error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function testGetActiveProfile(previewOutput: camera.PreviewOutput): camera.Profile | undefined {
  let activeProfile: camera.Profile | undefined = undefined;
  try {
    activeProfile = previewOutput.getActiveProfile();
  } catch (error) {
    // If the operation fails, error.code is returned and processed.
    let err = error as BusinessError;
    console.error(\`The previewOutput.getActiveProfile call failed. error code: ${err.code}\`);
  }
  return activeProfile;
}

#### getPreviewRotation12+

getPreviewRotation(displayRotation: number): ImageRotation

Obtains the preview rotation angle.

-   Device's natural orientation: The default orientation of the device (phone) is in portrait mode, with the charging port facing downward.
-   Camera lens angle: equivalent to the angle at which the camera is rotated clockwise to match the device's natural direction. The rear camera sensor of a phone is installed in landscape mode. Therefore, it needs to be rotated by 90 degrees clockwise to match the device's natural direction.
-   Screen orientation: The top-left corner of the image displayed on the screen is the first pixel, which is the coordinate origin. In the case of lock screen, the direction is the same as the device's natural orientation.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| displayRotation | number | Yes | Screen rotation angle of the display. It is obtained by calling [display.getDefaultDisplaySync](../../../../../application-framework/arkui/arkts-api/display-management/ohos-display-display/document.md#displaygetdefaultdisplaysync9). |

**Return value**

| Type | Description |
| :-- | :-- |
| [ImageRotation](../enums/document.md#imagerotation) | Obtains the preview rotation angle. If the API call fails, undefined is returned. |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400101 | Parameter missing or parameter type incorrect. |
| 7400201 | Camera service fatal error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function testGetPreviewRotation(previewOutput: camera.PreviewOutput, imageRotation : camera.ImageRotation): camera.ImageRotation {
  let previewRotation: camera.ImageRotation = camera.ImageRotation.ROTATION\_0;
  try {
    previewRotation = previewOutput.getPreviewRotation(imageRotation);
    console.info(\`Preview rotation is: ${previewRotation}\`);
  } catch (error) {
    // If the operation fails, error.code is returned and processed.
    let err = error as BusinessError;
    console.error(\`The previewOutput.getPreviewRotation call failed. error code: ${err.code}\`);
  }
  return previewRotation;
}

#### setPreviewRotation12+

setPreviewRotation(previewRotation: ImageRotation, isDisplayLocked?: boolean): void

Sets the preview rotation angle.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| previewRotation | [ImageRotation](../enums/document.md#imagerotation) | Yes | Preview rotation angle. |
| isDisplayLocked | boolean | No | Whether the orientation of the surface is locked when the screen rotates. If this parameter is not set, the default value **false** is used, indicating that the orientation is not locked. **true** if locked, **false** otherwise. For details, see [SurfaceRotationOptions](../../../../../application-framework/arkui/arkts-components/rendering-drawing/xcomponent/document.md#surfacerotationoptions12). |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400101 | Parameter missing or parameter type incorrect. |
| 7400201 | Camera service fatal error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function testSetPreviewRotation(previewOutput: camera.PreviewOutput, previewRotation : camera.ImageRotation, isDisplayLocked: boolean): void {
  try {
    previewOutput.setPreviewRotation(previewRotation, isDisplayLocked);
  } catch (error) {
    // If the operation fails, error.code is returned and processed.
    let err = error as BusinessError;
    console.error(\`The previewOutput.setPreviewRotation call failed. error code: ${err.code}\`);
  }
  return;
}

#### start(deprecated)

start(callback: AsyncCallback<void>): void

Starts to output preview streams. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/Ppl9X0agRreWLni4gJKv1A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062426Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4E618642E62E4297200D1AFA9C8C800E533B60A16FE2EC4DE318D9E5F896AA35)

This API is supported since API version 10 and deprecated since API version 11. You are advised to use [Session.start](../interface-session/document.md#start11) instead.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the preview stream output starts successfully, **err** is **undefined**; otherwise, **err** is an error object with an error code defined in [CameraErrorCode](../enums/document.md#cameraerrorcode). |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400103 | Session not config. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function startPreviewOutput(previewOutput: camera.PreviewOutput): void {
  previewOutput.start((err: BusinessError) => {
    if (err) {
      console.error(\`Failed to start the preview output, error code: ${err.code}.\`);
      return;
    }
    console.info('Callback returned with preview output started.');
  });
}

#### start(deprecated)

start(): Promise<void>

Starts to output preview streams. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/XrjEjjlEQDmG1lM_qQmlEQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062426Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=61832ECC59A50868CCE6A87F64B7A368F2C9DA8D770F42F377EEFD92D593DB94)

This API is supported since API version 10 and deprecated since API version 11. You are advised to use [Session.start](../interface-session/document.md#start11-1) instead.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400103 | Session not config. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function startPreviewOutput(previewOutput: camera.PreviewOutput): void {
  previewOutput.start().then(() => {
    console.info('Promise returned with preview output started.');
  }).catch((error: BusinessError) => {
    console.error(\`Failed to preview output start, error code: ${error.code}.\`);
  });
}

#### stop(deprecated)

stop(callback: AsyncCallback<void>): void

Stops outputting preview streams. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/uMmFMEqbTnma_CP8Af4jkg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062426Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0526259078491AD4D022311DA75B491112C1DC36CF1CD91785D813B21CA5F386)

This API is supported since API version 10 and deprecated since API version 11. You are advised to use [Session.stop](../interface-session/document.md#stop11) instead.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the preview stream output stops successfully, **err** is **undefined**; otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function stopPreviewOutput(previewOutput: camera.PreviewOutput): void {
  previewOutput.stop((err: BusinessError) => {
    if (err) {
      console.error(\`Failed to stop the preview output, error code: ${err.code}.\`);
      return;
    }
    console.info('Returned with preview output stopped.');
  })
}

#### stop(deprecated)

stop(): Promise<void>

Stops outputting preview streams. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/drOy35R2Q1mYnrxHpZJ77w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062426Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6C4248664306552AAF364A47DAF1BDCEE9746A3EF2DBBCA491D4ABEAAA96B67F)

This API is supported since API version 10 and deprecated since API version 11. You are advised to use [Session.stop](../interface-session/document.md#stop11-1) instead.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function stopPreviewOutput(previewOutput: camera.PreviewOutput): void {
  previewOutput.stop().then(() => {
    console.info('Callback returned with preview output stopped.');
  }).catch((error: BusinessError) => {
    console.error(\`Failed to preview output stop, error code: ${error.code}.\`);
  });
}
