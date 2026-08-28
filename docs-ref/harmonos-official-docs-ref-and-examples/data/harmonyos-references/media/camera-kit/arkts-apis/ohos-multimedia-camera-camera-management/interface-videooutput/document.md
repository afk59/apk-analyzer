# Interface (VideoOutput)

**VideoOutput** implements output information used in a video session. It inherits from [CameraOutput](../interface-cameraoutput/document.md).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/S50PWowORmu6iMLErQwt7w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062426Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=228806A3A1E499EFC6980B2F0B86E4A2B8A73241D889CB65E3206EF11362CDA8)

The initial APIs of this module are supported since API version 10. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { camera } from '@kit.CameraKit';

#### start

start(callback: AsyncCallback<void>): void

Starts video recording. This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If video recording starts successfully, **err** is **undefined**; otherwise, **err** is an error object with an error code defined in [CameraErrorCode](../enums/document.md#cameraerrorcode). |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400103 | Session not config. |
| 7400201 | Camera service fatal error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function startVideoOutput(videoOutput: camera.VideoOutput): void {
  videoOutput.start((err: BusinessError) => {
    if (err.code) {
      console.error(\`Failed to start the video output, error code: ${err.code}.\`);
      return;
    }
    console.info('Callback invoked to indicate the video output start success.');
  });
}

#### start

start(): Promise<void>

Starts video recording. This API uses a promise to return the result.

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
| 7400103 | Session not config. |
| 7400201 | Camera service fatal error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function startVideoOutput(videoOutput: camera.VideoOutput): void {
  videoOutput.start().then(() => {
    console.info('Promise returned to indicate that start method execution success.');
  }).catch((error: BusinessError) => {
    console.error(\`Failed to video output start, error code: ${error.code}.\`);
  });
}

#### stop

stop(callback: AsyncCallback<void>): void

Stops video recording. This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If video recording stops successfully, **err** is **undefined**; otherwise, **err** is an error object. |

**Example**

function stopVideoOutput(videoOutput: camera.VideoOutput): void {
  videoOutput.stop(() => {
    console.info('Callback invoked to indicate the video output stop success.');
  });
}

#### stop

stop(): Promise<void>

Stops video recording. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function stopVideoOutput(videoOutput: camera.VideoOutput): void {
  videoOutput.stop().then(() => {
    console.info('Promise returned to indicate that stop method execution success.');
  }).catch((error: BusinessError) => {
    console.error(\`Failed to video output stop, error code: ${error.code}.\`);
  });
}

#### on('frameStart')

on(type: 'frameStart', callback: AsyncCallback<void>): void

Subscribes to video recording start events. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/jOZUmDnaSbOzTBPY45v1pQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062426Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B66EC00256B9C0EF51B332A08A7E96C2218B9A3902C9C016CA21180D5BE319A6)

Currently, you cannot use **off()** to unregister the callback in the callback method of **on()**.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'frameStart'**. The event can be listened for when a videoOutput instance is created. The event is triggered and the corresponding information is returned when the bottom layer starts exposure for the first time. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. The recording starts as long as this event is returned. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function callback(err: BusinessError): void {
  if (err.code) {
    console.error(\`Callback Error, errorCode: ${err.code}\`);
    return;
  }
  console.info('Video frame started');
}

function registerVideoOutputFrameStart(videoOutput: camera.VideoOutput): void {
  videoOutput.on('frameStart', callback);
}

#### off('frameStart')

off(type: 'frameStart', callback?: AsyncCallback<void>): void

Unsubscribes from video recording start events.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/RBfDuNxJQNS55SUJle-Biw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062426Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4108EC5ADD9858B4292E964E6569AEAF8135B642BD8A6F8AA3AF050C7DB1DE95)

Currently, you cannot use **off()** to unregister the callback in the callback method of **on()**.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'frameStart'**. The event can be listened for when a videoOutput instance is created. |
| callback | AsyncCallback<void> | No | Callback used to return the result. If this parameter is specified, the subscription to the specified event with the specified callback is canceled. (The callback object cannot be an anonymous function.) Otherwise, the subscriptions to the specified event with all the callbacks are canceled. |

**Example**

function unregisterVideoOutputFrameStart(videoOutput: camera.VideoOutput): void {
  videoOutput.off('frameStart');
}

#### on('frameEnd')

on(type: 'frameEnd', callback: AsyncCallback<void>): void

Subscribes to video recording stop events. This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'frameEnd'**. The event can be listened for when a videoOutput instance is created. This event is triggered and returned when the last frame of recording is complete. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. The recording ends as long as this event is returned. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function callback(err: BusinessError): void {
  if (err.code) {
    console.error(\`Callback Error, errorCode: ${err.code}\`);
    return;
  }
  console.info('Video frame ended');
}

function registerVideoOutputFrameEnd(videoOutput: camera.VideoOutput): void {
  videoOutput.on('frameEnd', callback);
}

#### off('frameEnd')

off(type: 'frameEnd', callback?: AsyncCallback<void>): void

Unsubscribes from video recording stop events.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'frameEnd'**. The event can be listened for when a videoOutput instance is created. |
| callback | AsyncCallback<void> | No | Callback used to return the result. If this parameter is specified, the subscription to the specified event with the specified callback is canceled. (The callback object cannot be an anonymous function.) Otherwise, the subscriptions to the specified event with all the callbacks are canceled. |

**Example**

function unregisterVideoOutputFrameEnd(videoOutput: camera.VideoOutput): void {
  videoOutput.off('frameEnd');
}

#### on('error')

on(type: 'error', callback: ErrorCallback): void

Subscribes to VideoOutput error events. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/TjclXztbSMyDIgaVic7g7A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062426Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=79CC44F46C2EE05EC5342746F91784603788B00B00726E10642C18362888843C)

Currently, you cannot use **off()** to unregister the callback in the callback method of **on()**.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'error'**. The event can be listened for when a videoOutput instance is created. This event is triggered and the corresponding error message is returned when an error occurs during the use of a recording-related API such as [start](#start-1) or [CameraOutput.release](../interface-cameraoutput/document.md#release-1). |
| callback | [ErrorCallback](../../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#errorcallback) | Yes | Callback used to return an error code defined in [CameraErrorCode](../enums/document.md#cameraerrorcode). |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function callback(err: BusinessError): void {
  console.error(\`Video output error code: ${err.code}\`);
}

function registerVideoOutputError(videoOutput: camera.VideoOutput): void {
  videoOutput.on('error', callback);
}

#### off('error')

off(type: 'error', callback?: ErrorCallback): void

Unsubscribes from VideoOutput error events.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'error'**. The event can be listened for when a photoOutput instance is created. |
| callback | [ErrorCallback](../../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#errorcallback) | No | Callback used to return the result. If this parameter is specified, the subscription to the specified event with the specified callback is canceled. (The callback object cannot be an anonymous function.) Otherwise, the subscriptions to the specified event with all the callbacks are canceled. |

**Example**

function unregisterVideoOutputError(videoOutput: camera.VideoOutput): void {
  videoOutput.off('error');
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

function getSupportedFrameRates(videoOutput: camera.VideoOutput): Array<camera.FrameRateRange> {
  let supportedFrameRatesArray: Array<camera.FrameRateRange> = videoOutput.getSupportedFrameRates();
  return supportedFrameRatesArray;
}

#### setFrameRate12+

setFrameRate(minFps: number, maxFps: number): void

Sets a frame rate range for video streams. The range must be within the supported frame rate range, which can be obtained by calling [getSupportedFrameRates](#getsupportedframerates12).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/oMCgtx58QEWNsP0ko_VnlQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062426Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4BF22F4583E38AAFFC9C4A07F08BBE7605C9F369C73860BE67AA105E16C31659)

This API is valid only in [PhotoSession](../interface-photosession/document.md) or [VideoSession](../interface-videosession/document.md) mode.

Before calling this API, call [getActiveFrameRate](#getactiveframerate12) to obtain the current frame rate of the video session. If the delivered frame rate matches the current frame rate, the delivered frame rate is not applied.

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

function setFrameRateRange(videoOutput: camera.VideoOutput, frameRateRange: Array<number>): void {
  videoOutput.setFrameRate(frameRateRange\[0\], frameRateRange\[1\]);
}

#### getActiveFrameRate12+

getActiveFrameRate(): FrameRateRange

Obtains the configured frame rate range.

This API is valid only after [setFrameRate](#setframerate12) is called to set a frame rate range for video streams.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [FrameRateRange](../interfaces-others/document.md#frameraterange) | Frame rate range. |

**Example**

function getActiveFrameRate(videoOutput: camera.VideoOutput): camera.FrameRateRange {
  let activeFrameRate: camera.FrameRateRange = videoOutput.getActiveFrameRate();
  return activeFrameRate;
}

#### getActiveProfile12+

getActiveProfile(): VideoProfile

Obtains the profile that takes effect currently.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [VideoProfile](../interfaces-others/document.md#videoprofile) | Profile obtained. |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400201 | Camera service fatal error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function testGetActiveProfile(videoOutput: camera.VideoOutput): camera.Profile | undefined {
  let activeProfile: camera.VideoProfile | undefined = undefined;
  try {
    activeProfile = videoOutput.getActiveProfile();
  } catch (error) {
    // If the operation fails, error.code is returned and processed.
    let err = error as BusinessError;
    console.error(\`The videoOutput.getActiveProfile call failed. error code: ${err.code}\`);
  }
  return activeProfile;
}

#### isMirrorSupported15+

isMirrorSupported(): boolean

Checks whether mirror recording is supported.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result for the support of mirror recording. **true** if supported, **false** otherwise. If the API call fails, undefined is returned. |

**Example**

function testIsMirrorSupported(videoOutput: camera.VideoOutput): boolean {
  let isSupported: boolean = videoOutput.isMirrorSupported();
  return isSupported;
}

#### enableMirror15+

enableMirror(enabled: boolean): void

Enables or disables mirror recording.

-   Before calling this API, check whether mirror recording is supported by using [isMirrorSupported](#ismirrorsupported15).
    
-   After enabling or disabling mirror recording, call [getVideoRotation](#getvideorotation12) to obtain the rotation angle and [updateRotation](../../../../media-kit/arkts-apis/ohos-multimedia-media-media/interface-avrecorder/document.md#updaterotation12) to update the rotation angle.
    

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| enabled | boolean | Yes | Whether to enable mirror recording. **true** to enable, **false** otherwise. |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400101 | Parameter missing or parameter type incorrect. |
| 7400103 | Session not config. |

**Example**

import { camera } from '@kit.CameraKit';
import { media } from '@kit.MediaKit';
import { BusinessError } from '@kit.BasicServicesKit';

function enableMirror(videoOutput: camera.VideoOutput, mirrorMode: boolean, aVRecorder: media.AVRecorder, deviceDegree : number): void {
    try {
        videoOutput.enableMirror(mirrorMode);
        aVRecorder.updateRotation(videoOutput.getVideoRotation(deviceDegree));
    } catch (error) {
        let err = error as BusinessError;
    }
}

#### getVideoRotation12+

getVideoRotation(deviceDegree: number): ImageRotation

Obtains the video rotation angle.

-   Device's natural orientation: The default orientation of the device (phone) is in portrait mode, with the charging port facing downward.
-   Camera lens angle: equivalent to the angle at which the camera is rotated clockwise to match the device's natural direction. The rear camera sensor of a phone is installed in landscape mode. Therefore, it needs to be rotated by 90 degrees clockwise to match the device's natural direction.
-   Screen orientation: The top-left corner of the image displayed on the screen is the first pixel, which is the coordinate origin. In the case of lock screen, the direction is the same as the device's natural orientation.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| deviceDegree | number | Yes | Device rotation angle, measured in degrees, within the range of \[0, 360\]. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ImageRotation](../enums/document.md#imagerotation) | Obtains the video rotation angle. |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400101 | Parameter missing or parameter type incorrect. |
| 7400201 | Camera service fatal error. |

**Example**

import { camera } from '@kit.CameraKit';
import { Decimal } from '@kit.ArkTS';
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

async function getVideoRotation(videoOutput: camera.VideoOutput): Promise<camera.ImageRotation> {
  let deviceDegree = await getDeviceDegree();
  let videoRotation: camera.ImageRotation = camera.ImageRotation.ROTATION\_0;
  try {
    videoRotation = videoOutput.getVideoRotation(deviceDegree);
  } catch (error) {
    let err = error as BusinessError;
    console.error('Failed to get video rotation: ' + JSON.stringify(err));
  }
  return videoRotation;
}

// Obtain the device rotation degree.
function getDeviceDegree(): Promise<number> {
  return new Promise<number>((resolve) => {
    try {
      sensor.once(sensor.SensorId.GRAVITY, (data: sensor.GravityResponse) => {
        console.info('Succeeded in invoking once. X-coordinate component: ' + data.x);
        console.info('Succeeded in invoking once. Y-coordinate component: ' + data.y);
        console.info('Succeeded in invoking once. Z-coordinate component: ' + data.z);
        let x = data.x;
        let y = data.y;
        let z = data.z;
        let deviceDegree: number;
        if ((x \* x + y \* y) \* 3 < z \* z) {
          deviceDegree = -1;
        } else {
          let sd: Decimal = Decimal.atan2(y, -x);
          let sc: Decimal = Decimal.round(Number(sd) / 3.141592653589 \* 180)
          deviceDegree = 90 - Number(sc);
          deviceDegree = deviceDegree >= 0 ? deviceDegree% 360 : deviceDegree% 360 + 360;
        }
        resolve(deviceDegree);
      });
    } catch (error) {
      let err = error as BusinessError;
      console.error('Failed to register gravity sensor: ' + JSON.stringify(err));
      resolve(-1); // Return the default value when an exception occurs.
    }
  });
}
