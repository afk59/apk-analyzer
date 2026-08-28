# Interface (PhotoOutput)

**PhotoOutput** implements output information used in a photo session. It inherits from [CameraOutput](../interface-cameraoutput/document.md).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/eiuJaSlyR6SfHjNXx98JnQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062426Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=29753FD59967A9E9BF0F6DAC00CEB737B8C1A3C50F63D306212CA39C8C48EB42)

The initial APIs of this module are supported since API version 10. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { camera } from '@kit.CameraKit';

#### capture

capture(callback: AsyncCallback<void>): void

Captures a photo with the default photo capture parameters. This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the photo is successfully captured with the default parameters, **err** is **undefined**; otherwise, **err** is an error object with an error code defined in [CameraErrorCode](../enums/document.md#cameraerrorcode). |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400104 | Session not running. |
| 7400201 | Camera service fatal error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function capture(photoOutput: camera.PhotoOutput): void {
  photoOutput.capture((err: BusinessError) => {
    if (err) {
      console.error(\`Failed to capture the photo, error code: ${err.code}.\`);
      return;
    }
    console.info('Callback invoked to indicate the photo capture request success.');
  });
}

#### capture

capture(): Promise<void>

Captures a photo with the default photo capture parameters. This API uses a promise to return the result.

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
| 7400104 | Session not running. |
| 7400201 | Camera service fatal error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function capture(photoOutput: camera.PhotoOutput): void {
  photoOutput.capture().then(() => {
    console.info('Promise returned to indicate that photo capture request success.');
  }).catch((error: BusinessError) => {
    console.error(\`Failed to photo output capture, error code: ${error.code}.\`);
  });
}

#### capture

capture(setting: PhotoCaptureSetting, callback: AsyncCallback<void>): void

Captures a photo with the specified photo capture parameters. This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| setting | [PhotoCaptureSetting](../interfaces-others/document.md#photocapturesetting) | Yes | Photo capture settings. If the input data is of the **undefined** type, a photo capture operation is triggered based on the default settings. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation fails, an error code defined in [CameraErrorCode](../enums/document.md#cameraerrorcode) is returned. |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400101 | Parameter missing or parameter type incorrect. |
| 7400104 | Session not running. |
| 7400201 | Camera service fatal error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function capture(photoOutput: camera.PhotoOutput): void {
  let captureLocation: camera.Location = {
    latitude: 0,
    longitude: 0,
    altitude: 0
  }
  let settings: camera.PhotoCaptureSetting = {
    quality: camera.QualityLevel.QUALITY\_LEVEL\_LOW,
    rotation: camera.ImageRotation.ROTATION\_0,
    location: captureLocation,
    mirror: false
  }
  photoOutput.capture(settings, (err: BusinessError) => {
    if (err) {
      console.error(\`Failed to capture the photo, error code: ${err.code}.\`);
      return;
    }
    console.info('Callback invoked to indicate the photo capture request success.');
  });
}

#### capture

capture(setting: PhotoCaptureSetting): Promise<void>

Captures a photo with the specified photo capture parameters. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| setting | [PhotoCaptureSetting](../interfaces-others/document.md#photocapturesetting) | Yes | Photo capture settings. If the input data is of the **undefined** type, a photo capture operation is triggered based on the default settings. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400101 | Parameter missing or parameter type incorrect. |
| 7400104 | Session not running. |
| 7400201 | Camera service fatal error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function capture(photoOutput: camera.PhotoOutput): void {
  let captureLocation: camera.Location = {
    latitude: 0,
    longitude: 0,
    altitude: 0
  }
  let settings: camera.PhotoCaptureSetting = {
    quality: camera.QualityLevel.QUALITY\_LEVEL\_LOW,
    rotation: camera.ImageRotation.ROTATION\_0,
    location: captureLocation,
    mirror: false
  }
  photoOutput.capture(settings).then(() => {
    console.info('Promise returned to indicate that photo capture request success.');
  }).catch((error: BusinessError) => {
    console.error(\`Failed to photo output capture, error code: ${error.code}.\`);
  });
}

#### on('photoAvailable')11+

on(type: 'photoAvailable', callback: AsyncCallback<Photo>): void

Subscribes to the events of returning available photos. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/P_kNUcRyShW46XWly1KRow/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062426Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DA37216F4F9E9DA95B288163C27BB4C87966ED051AE7BBD75D8806F41F893124)

Currently, you cannot use **off()** to unregister the callback in the callback method of **on()**.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'photoAvailable'**. The event can be listened for when a **photoOutput** instance is created. |
| callback | AsyncCallback<[Photo](../interface-photo/document.md)\> | Yes | Callback used to listen for the events of returning available photos. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { image } from '@kit.ImageKit';
import { camera } from '@kit.CameraKit';

function callback(err: BusinessError, photo: camera.Photo): void {
  if (err !== undefined && err.code !== 0) {
    console.error(\`Callback Error, errorCode: ${err.code}\`);
    return;
  }
  let mainImage: image.Image = photo.main;
}

function registerPhotoOutputPhotoAvailable(photoOutput: camera.PhotoOutput): void {
  photoOutput.on('photoAvailable', callback);
}

#### off('photoAvailable')11+

off(type: 'photoAvailable', callback?: AsyncCallback<Photo>): void

Unsubscribes from the events of returning available photos.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'photoAvailable'**. The event can be listened for when a **photoOutput** instance is created. |
| callback | AsyncCallback<[Photo](../interface-photo/document.md)\> | No | Callback used to return the result. If this parameter is specified, the subscription to the specified event with the specified callback is canceled. (The callback object cannot be an anonymous function.) Otherwise, the subscriptions to the specified event with all the callbacks are canceled. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { image } from '@kit.ImageKit';

function callback(err: BusinessError, photo: camera.Photo): void {
  if (err !== undefined && err.code !== 0) {
    console.error(\`Callback Error, errorCode: ${err.code}\`);
    return;
  }
  let mainImage: image.Image = photo.main;
}

function unRegisterPhotoOutputPhotoAvailable(photoOutput: camera.PhotoOutput): void {
  photoOutput.off('photoAvailable', callback);
}

#### on('captureStartWithInfo')11+

on(type: 'captureStartWithInfo', callback: AsyncCallback<CaptureStartInfo>): void

Subscribes to capture start events. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/_oYofwlEQPmU9QAie68OXw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062426Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D3201C129CA47946E0305475028984F1D5A62C939C460CFF3E2F7055386D342F)

Currently, you cannot use **off()** to unregister the callback in the callback method of **on()**.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'captureStartWithInfo'**. The event can be listened for when a photoOutput instance is created. |
| callback | AsyncCallback<[CaptureStartInfo](../interfaces-others/document.md#capturestartinfo11)\> | Yes | Callback used to return the capture ID. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function callback(err: BusinessError, captureStartInfo: camera.CaptureStartInfo): void {
  if (err !== undefined && err.code !== 0) {
    console.error(\`Callback Error, errorCode: ${err.code}\`);
    return;
  }
  console.info(\`photo capture started, captureStartInfo : ${captureStartInfo}\`);
}

function registerCaptureStartWithInfo(photoOutput: camera.PhotoOutput): void {
  photoOutput.on('captureStartWithInfo', callback);
}

#### off('captureStartWithInfo')11+

off(type: 'captureStartWithInfo', callback?: AsyncCallback<CaptureStartInfo>): void

Unsubscribes from capture start events.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'captureStartWithInfo'**. The event can be listened for when a photoOutput instance is created. |
| callback | AsyncCallback<[CaptureStartInfo](../interfaces-others/document.md#capturestartinfo11)\> | No | Callback used to return the result. If this parameter is specified, the subscription to the specified event with the specified callback is canceled. (The callback object cannot be an anonymous function.) Otherwise, the subscriptions to the specified event with all the callbacks are canceled. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function unRegisterCaptureStartWithInfo(photoOutput: camera.PhotoOutput): void {
  photoOutput.off('captureStartWithInfo');
}

#### isMovingPhotoSupported12+

isMovingPhotoSupported(): boolean

Checks whether taking moving photos is supported.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result for the support of taking moving photos. **true** if supported, **false** otherwise. If the API call fails, undefined is returned. |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400201 | Camera service fatal error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function isMovingPhotoSupported(photoOutput: camera.PhotoOutput): boolean {
  let isSupported: boolean = false;
  try {
    isSupported = photoOutput.isMovingPhotoSupported();
  } catch (error) {
    // If the operation fails, error.code is returned and processed.
    let err = error as BusinessError;
    console.error(\`The isMovingPhotoSupported call failed. error code: ${err.code}\`);
  }
  return isSupported;
}

#### enableMovingPhoto12+

enableMovingPhoto(enabled: boolean): void

Enables or disables the feature of taking moving photos.

**Required permissions:** ohos.permission.MICROPHONE

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| enabled | boolean | Yes | Whether to enable the feature of taking moving photos. **true** to enable, **false** otherwise. |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | permission denied. |
| 7400101 | Parameter missing or parameter type incorrect. |
| 7400201 | Camera service fatal error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function enableMovingPhoto(photoOutput: camera.PhotoOutput): void {
  try {
    photoOutput.enableMovingPhoto(true);
  } catch (error) {
    // If the operation fails, error.code is returned and processed.
    let err = error as BusinessError;
    console.error(\`The enableMovingPhoto call failed. error code: ${err.code}\`);
  }
}

#### on('photoAssetAvailable')12+

on(type: 'photoAssetAvailable', callback: AsyncCallback<photoAccessHelper.PhotoAsset>): void

Subscribes to photo asset available events. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/9eTY4fNjRqGo8w46_-HXQA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062426Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=081ACA9BCB2FDEC6AAB3353CF669213410C739432B11F4F2271410B8A51961E6)

Currently, you cannot use **off()** to unregister the callback in the callback method of **on()**.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'photoAssetAvailable'**. The event can be listened for when a photoOutput instance is created. |
| callback | AsyncCallback<[photoAccessHelper.PhotoAsset](../../../../media-library-kit/arkts-apis/ohos-file-photoaccesshelper-album-management/interface-photoasset/document.md)\> | Yes | Callback used to return the photo asset. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { photoAccessHelper } from '@kit.MediaLibraryKit';

function photoAssetAvailableCallback(err: BusinessError, photoAsset: photoAccessHelper.PhotoAsset): void {
  if (err) {
    console.info(\`photoAssetAvailable error: ${JSON.stringify(err)}.\`);
    return;
  }
  console.info('photoOutPutCallBack photoAssetAvailable');
  // You can use photoAsset to obtain image information.
}

function onPhotoOutputPhotoAssetAvailable(photoOutput: camera.PhotoOutput): void {
  photoOutput.on('photoAssetAvailable', photoAssetAvailableCallback);
}

#### off('photoAssetAvailable')12+

off(type: 'photoAssetAvailable', callback?: AsyncCallback<photoAccessHelper.PhotoAsset>): void

Unsubscribes from photo asset available events.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'photoAssetAvailable'**. The event can be listened for when a photoOutput instance is created. |
| callback | AsyncCallback<[photoAccessHelper.PhotoAsset](../../../../media-library-kit/arkts-apis/ohos-file-photoaccesshelper-album-management/interface-photoasset/document.md)\> | No | Callback used for unsubscription. If this parameter is specified, the subscription to the specified event with the specified callback is canceled. (The callback object cannot be an anonymous function.) Otherwise, the subscriptions to the specified event with all the callbacks are canceled. |

**Example**

function offPhotoOutputPhotoAssetAvailable(photoOutput: camera.PhotoOutput): void {
  photoOutput.off('photoAssetAvailable');
}

#### isMirrorSupported

isMirrorSupported(): boolean

Checks whether mirror photography is supported.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result for the support of mirror photography. **true** if supported, **false** otherwise. If the API call fails, undefined is returned. |

**Example**

function isMirrorSupported(photoOutput: camera.PhotoOutput): boolean {
  let isSupported: boolean = photoOutput.isMirrorSupported();
  return isSupported;
}

#### enableMirror13+

enableMirror(enabled: boolean): void

Enables or disables mirroring photo capture.

Before calling this API, check whether moving photo capture is supported by calling [isMovingPhotoSupported](#ismovingphotosupported12) and whether mirroring is supported by calling [isMirrorSupported](#ismirrorsupported).

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| enabled | boolean | Yes | Whether to enable mirroring photo capture. **true** to enable, **false** otherwise. |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400101 | Parameter missing or parameter type incorrect. |
| 7400103 | Session not config. |
| 7400201 | Camera service fatal error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function enableMirror(photoOutput: camera.PhotoOutput): void {
  try {
    photoOutput.enableMirror(true);
  } catch (error) {
    // If the operation fails, error.code is returned and processed.
    let err = error as BusinessError;
    console.error(\`The enableMirror call failed. error code: ${err.code}\`);
  }
}

#### getSupportedMovingPhotoVideoCodecTypes13+

getSupportedMovingPhotoVideoCodecTypes(): Array<VideoCodecType>

Obtains the supported video codec types of moving photos.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Array<[VideoCodecType](../enums/document.md#videocodectype13)\> | Array holding the supported video codec types. If the API call fails, undefined is returned. |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400201 | Camera service fatal error. |

**Example**

function getSupportedMovingPhotoVideoCodecType(photoOutput: camera.PhotoOutput): Array<camera.VideoCodecType> {
  let supportedVideoCodecTypesArray: Array<camera.VideoCodecType> = photoOutput.getSupportedMovingPhotoVideoCodecTypes();
  return supportedVideoCodecTypesArray;
}

#### setMovingPhotoVideoCodecType13+

setMovingPhotoVideoCodecType(codecType: VideoCodecType): void

Sets a video codec type for moving photos.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| codecType | [VideoCodecType](../enums/document.md#videocodectype13) | Yes | Video codec type. |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400201 | Camera service fatal error. |

**Example**

function setMovingPhotoVideoCodecTypes(photoOutput: camera.PhotoOutput, videoCodecType: camera.VideoCodecType): void {
  photoOutput.setMovingPhotoVideoCodecType(videoCodecType);
}

#### on('frameShutter')

on(type: 'frameShutter', callback: AsyncCallback<FrameShutterInfo>): void

Subscribes to frame shutter events. This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'frameShutter'**. The event can be listened for when a photoOutput instance is created. |
| callback | AsyncCallback<[FrameShutterInfo](../interfaces-others/document.md#frameshutterinfo)\> | Yes | Callback used to return the result. A new photo capture request can be delivered as long as this event is returned. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function callback(err: BusinessError, frameShutterInfo: camera.FrameShutterInfo): void {
  if (err !== undefined && err.code !== 0) {
    console.error(\`Callback Error, errorCode: ${err.code}\`);
    return;
  }
  console.info(\`CaptureId for frame : ${frameShutterInfo.captureId}\`);
  console.info(\`Timestamp for frame : ${frameShutterInfo.timestamp}\`);
}

function registerPhotoOutputFrameShutter(photoOutput: camera.PhotoOutput): void {
  photoOutput.on('frameShutter', callback);
}

#### off('frameShutter')

off(type: 'frameShutter', callback?: AsyncCallback<FrameShutterInfo>): void

Unsubscribes from frame shutter events.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'frameShutter'**. The event can be listened for when a photoOutput instance is created. |
| callback | AsyncCallback<[FrameShutterInfo](../interfaces-others/document.md#frameshutterinfo)\> | No | Callback used to return the result. If this parameter is specified, the subscription to the specified event with the specified callback is canceled. (The callback object cannot be an anonymous function.) Otherwise, the subscriptions to the specified event with all the callbacks are canceled. |

**Example**

function unregisterPhotoOutputFrameShutter(photoOutput: camera.PhotoOutput): void {
  photoOutput.off('frameShutter');
}

#### on('captureEnd')

on(type: 'captureEnd', callback: AsyncCallback<CaptureEndInfo>): void

Subscribes to capture end events. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/F4X-q0rlTyqcRu2_m-kcHQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062426Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=615A29D4016388C4ABA46E23A1913CC03D00A469AF10396A2BA56CA518DC39BD)

Currently, you cannot use **off()** to unregister the callback in the callback method of **on()**.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'captureEnd'**. The event can be listened for when a photoOutput instance is created. This event is triggered and the corresponding information is returned when the photo capture is complete. |
| callback | AsyncCallback<[CaptureEndInfo](../interfaces-others/document.md#captureendinfo)\> | Yes | Callback used to return the result. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function callback(err: BusinessError, captureEndInfo: camera.CaptureEndInfo): void {
  if (err !== undefined && err.code !== 0) {
    console.error(\`Callback Error, errorCode: ${err.code}\`);
    return;
  }
  console.info(\`photo capture end, captureId : ${captureEndInfo.captureId}\`);
  console.info(\`frameCount : ${captureEndInfo.frameCount}\`);
}

function registerPhotoOutputCaptureEnd(photoOutput: camera.PhotoOutput): void {
  photoOutput.on('captureEnd', callback);
}

#### off('captureEnd')

off(type: 'captureEnd', callback?: AsyncCallback<CaptureEndInfo>): void

Unsubscribes from capture end events.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'captureEnd'**. The event can be listened for when a photoOutput instance is created. |
| callback | AsyncCallback<[CaptureEndInfo](../interfaces-others/document.md#captureendinfo)\> | No | Callback used to return the result. If this parameter is specified, the subscription to the specified event with the specified callback is canceled. (The callback object cannot be an anonymous function.) Otherwise, the subscriptions to the specified event with all the callbacks are canceled. |

**Example**

function unregisterPhotoOutputCaptureEnd(photoOutput: camera.PhotoOutput): void {
  photoOutput.off('captureEnd');
}

#### on('frameShutterEnd')12+

on(type: 'frameShutterEnd', callback: AsyncCallback<FrameShutterEndInfo>): void

Subscribes to frame shutter end events. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2/v3/akQBYR31SmK870bEAFTglA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062426Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B547C2358DD173336B7BD858A53DC141D781AF5027D9FDC829178452EB427077)

Currently, you cannot use **off()** to unregister the callback in the callback method of **on()**.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'frameShutterEnd'**. The event can be listened for when a photoOutput instance is created. |
| callback | AsyncCallback<[FrameShutterEndInfo](../interfaces-others/document.md#frameshutterendinfo12)\> | Yes | Callback used to return the result. It is invoked when the frame shutter ends. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function callback(err: BusinessError, frameShutterEndInfo: camera.FrameShutterEndInfo): void {
  if (err !== undefined && err.code !== 0) {
    console.error(\`Callback Error, errorCode: ${err.code}\`);
    return;
  }
  console.info(\`CaptureId for frame : ${frameShutterEndInfo.captureId}\`);
}

function registerPhotoOutputFrameShutterEnd(photoOutput: camera.PhotoOutput): void {
  photoOutput.on('frameShutterEnd', callback);
}

#### off('frameShutterEnd')12+

off(type: 'frameShutterEnd', callback?: AsyncCallback<FrameShutterEndInfo>): void

Unsubscribes from frame shutter end events.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'frameShutterEnd'**. The event can be listened for when a photoOutput instance is created. |
| callback | AsyncCallback<[FrameShutterEndInfo](../interfaces-others/document.md#frameshutterendinfo12)\> | No | Callback used to return the result. If this parameter is specified, the subscription to the specified event with the specified callback is canceled. (The callback object cannot be an anonymous function.) Otherwise, the subscriptions to the specified event with all the callbacks are canceled. |

**Example**

function unregisterPhotoOutputFrameShutterEnd(photoOutput: camera.PhotoOutput): void {
  photoOutput.off('frameShutterEnd');
}

#### on('captureReady')12+

on(type: 'captureReady', callback: AsyncCallback<void>): void

Subscribes to capture ready events. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/Wg3_rP2hQQaN7qcom6uOzw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062426Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E3B75E3635AC851C65F003F65B280A948E3F92CE88EE2BE4536FC650963DAED9)

Currently, you cannot use **off()** to unregister the callback in the callback method of **on()**.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'captureReady'**. The event can be listened for when a photoOutput instance is created. The event is triggered and the corresponding information is returned when it is ready to take the next photo. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function callback(err: BusinessError): void {
  if (err !== undefined && err.code !== 0) {
    console.error(\`Callback Error, errorCode: ${err.code}\`);
    return;
  }
  console.info(\`photo capture ready\`);
}

function registerPhotoOutputCaptureReady(photoOutput: camera.PhotoOutput): void {
  photoOutput.on('captureReady', callback);
}

#### off('captureReady')12+

off(type: 'captureReady', callback?: AsyncCallback<void>): void

Unsubscribes from capture ready events.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'captureReady'**. The event can be listened for when a photoOutput instance is created. |
| callback | AsyncCallback<void> | No | Callback used to return the result. If this parameter is specified, the subscription to the specified event with the specified callback is canceled. (The callback object cannot be an anonymous function.) Otherwise, the subscriptions to the specified event with all the callbacks are canceled. |

**Example**

function unregisterPhotoOutputCaptureReady(photoOutput: camera.PhotoOutput): void {
  photoOutput.off('captureReady');
}

#### on('estimatedCaptureDuration')12+

on(type: 'estimatedCaptureDuration', callback: AsyncCallback<number>): void

Subscribes to estimated capture duration events. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/K_xZunwYQF-Ws7AjKCrc6w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062426Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D8D58F89E4691ACA79D96E5E0B578CFAACB2E5B235D743A36F4B011D03EE1721)

Currently, you cannot use **off()** to unregister the callback in the callback method of **on()**.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'estimatedCaptureDuration'**. The event can be listened for when a photoOutput instance is created. This event is triggered and the corresponding information is returned when the photo capture is complete. |
| callback | AsyncCallback<number> | Yes | Callback used to return the estimated duration when the sensor captures frames at the bottom layer in a single capture, measured in units of milliseconds. If **–1** is reported, there is no estimated duration. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function callback(err: BusinessError, duration: number): void {
  if (err !== undefined && err.code !== 0) {
    console.error(\`Callback Error, errorCode: ${err.code}\`);
    return;
  }
  console.info(\`photo estimated capture duration : ${duration}\`);
}

function registerPhotoOutputEstimatedCaptureDuration(photoOutput: camera.PhotoOutput): void {
  photoOutput.on('estimatedCaptureDuration', callback);
}

#### off('estimatedCaptureDuration')12+

off(type: 'estimatedCaptureDuration', callback?: AsyncCallback<number>): void

Unsubscribes from estimated capture duration events.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'estimatedCaptureDuration'**. The event can be listened for when a photoOutput instance is created. |
| callback | AsyncCallback<number> | No | Callback used to return the result. If this parameter is specified, the subscription to the specified event with the specified callback is canceled. (The callback object cannot be an anonymous function.) Otherwise, the subscriptions to the specified event with all the callbacks are canceled. |

**Example**

function unregisterPhotoOutputEstimatedCaptureDuration(photoOutput: camera.PhotoOutput): void {
  photoOutput.off('estimatedCaptureDuration');
}

#### on('error')

on(type: 'error', callback: ErrorCallback): void

Subscribes to PhotoOutput error events. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/5ucviKBAReKL8z1RMy13dA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062426Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=794250708D3D9F50AD2B9AAA838A6B68B02BDA6933902E901C97376D42C4038C)

Currently, you cannot use **off()** to unregister the callback in the callback method of **on()**.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'error'**. The event can be listened for when a photoOutput instance is created. This event is triggered and the corresponding error message is returned when an error occurs during the calling of a photo-related API. |
| callback | [ErrorCallback](../../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#errorcallback) | Yes | Callback used to return an error code defined in [CameraErrorCode](../enums/document.md#cameraerrorcode). |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function callback(err: BusinessError): void {
  console.error(\`Photo output error code: ${err.code}\`);
}

function registerPhotoOutputError(photoOutput: camera.PhotoOutput): void {
  photoOutput.on('error', callback);
}

#### off('error')

off(type: 'error', callback?: ErrorCallback): void

Unsubscribes from PhotoOutput error events.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'error'**. The event can be listened for when a photoOutput instance is created. |
| callback | [ErrorCallback](../../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#errorcallback) | No | Callback used to return the result. If this parameter is specified, the subscription to the specified event with the specified callback is canceled. (The callback object cannot be an anonymous function.) Otherwise, the subscriptions to the specified event with all the callbacks are canceled. |

**Example**

function unregisterPhotoOutputError(photoOutput: camera.PhotoOutput): void {
  photoOutput.off('error');
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

function testGetActiveProfile(photoOutput: camera.PhotoOutput): camera.Profile | undefined {
  let activeProfile: camera.Profile | undefined = undefined;
  try {
    activeProfile = photoOutput.getActiveProfile();
  } catch (error) {
    // If the operation fails, error.code is returned and processed.
    let err = error as BusinessError;
    console.error(\`The photoOutput.getActiveProfile call failed. error code: ${err.code}\`);
  }
  return activeProfile;
}

#### getPhotoRotation12+

getPhotoRotation(deviceDegree: number): ImageRotation

Obtains the photo rotation angle.

-   Device's natural orientation: The default orientation of the device (phone) is in portrait mode, with the charging port facing downward.
-   Camera lens angle: equivalent to the angle at which the camera is rotated clockwise to match the device's natural direction. The rear camera sensor of a phone is installed in landscape mode. Therefore, it needs to be rotated by 90 degrees clockwise to match the device's natural direction.
-   Screen orientation: The top-left corner of the image displayed on the screen is the first pixel, which is the coordinate origin. In the case of lock screen, the direction is the same as the device's natural orientation.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| deviceDegree | number | Yes | 
Device rotation angle, measured in degrees, within the range of \[0, 360\].

If the input value goes beyond this range, the system uses the remainder of the input value divided by 360.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [ImageRotation](../enums/document.md#imagerotation) | Obtains the photo rotation angle. If the API call fails, undefined is returned. |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400101 | Parameter missing or parameter type incorrect. |
| 7400201 | Camera service fatal error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function testGetPhotoRotation(photoOutput: camera.PhotoOutput, deviceDegree : number): camera.ImageRotation {
  let photoRotation: camera.ImageRotation = camera.ImageRotation.ROTATION\_0;
  try {
    photoRotation = photoOutput.getPhotoRotation(deviceDegree);
    console.info(\`Photo rotation is: ${photoRotation}\`);
  } catch (error) {
    // If the operation fails, error.code is returned and processed.
    let err = error as BusinessError;
    console.error(\`The photoOutput.getPhotoRotation call failed. error code: ${err.code}\`);
  }
  return photoRotation;
}

#### on('captureStart')(deprecated)

on(type: 'captureStart', callback: AsyncCallback<number>): void

Subscribes to capture start events. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/u7w9Z2OJTvC_eBh_uo3GGw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062426Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=158186F0972B474BA3AFE4A764C965367B222A951A4944E7EC4DC7347E6E15F4)

This API is supported since API version 10 and deprecated since API version 11. You are advised to use [on('captureStartWithInfo')](#oncapturestartwithinfo11) instead.

Currently, you cannot use **off()** to unregister the callback in the callback method of **on()**.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'captureStart'**. The event can be listened for when a photoOutput instance is created. This event is triggered and returned when the bottom layer starts exposure each time a photo is taken. |
| callback | AsyncCallback<number> | Yes | Callback used to return the capture ID. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function callback(err: BusinessError, captureId: number): void {
  if (err !== undefined && err.code !== 0) {
    console.error(\`Callback Error, errorCode: ${err.code}\`);
    return;
  }
  console.info(\`photo capture started, captureId : ${captureId}\`);
}

function registerPhotoOutputCaptureStart(photoOutput: camera.PhotoOutput): void {
  photoOutput.on('captureStart', callback);
}

#### off('captureStart')(deprecated)

off(type: 'captureStart', callback?: AsyncCallback<number>): void

Unsubscribes from capture start events.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/wuEbyWgaRW2HsrsAIMXLQA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062426Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AD7B41950BBCBC9F6A336E26838909020491EABC6CEB6786C4CBEDB673E22BFF)

This API is supported since API version 10 and deprecated since API version 11. You are advised to use [off('captureStartWithInfo')](#offcapturestartwithinfo11) instead.

Currently, you cannot use **off()** to unregister the callback in the callback method of **on()**.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'captureStart'**. The event can be listened for when a photoOutput instance is created. |
| callback | AsyncCallback<number> | No | Callback used to return the result. If this parameter is specified, the subscription to the specified event with the specified callback is canceled. (The callback object cannot be an anonymous function.) Otherwise, the subscriptions to the specified event with all the callbacks are canceled. |

**Example**

function unregisterPhotoOutputCaptureStart(photoOutput: camera.PhotoOutput): void {
  photoOutput.off('captureStart');
}

#### isPhotoQualityPrioritizationSupported21+

isPhotoQualityPrioritizationSupported(qualityPrioritization: PhotoQualityPrioritization): boolean

Checks whether the specified photo quality prioritization strategy is supported.

**Atomic service API**: This API can be used in atomic services since API version 21.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| qualityPrioritization | [PhotoQualityPrioritization](../enums/document.md#photoqualityprioritization21) | Yes | Photo quality prioritization strategy. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result for the support of the specified photo quality prioritization strategy. **true** if supported, **false** otherwise. |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400201 | Camera service fatal error, reconfiguring streams is needed to recover from failure. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { camera } from '@kit.CameraKit';

let photoOutput: camera.PhotoOutput;

function isPhotoQualityPrioritizationSupported(qualityPrioritization: camera.PhotoQualityPrioritization): boolean {
  let isSupported: boolean = false;
  try {
    isSupported = photoOutput.isPhotoQualityPrioritizationSupported(qualityPrioritization);
  } catch (error) {
    let err = error as BusinessError;
    console.error(\`The isPhotoQualityPrioritizationSupported call failed. error code: ${err.code}\`);
  }
  return isSupported;
}

#### setPhotoQualityPrioritization21+

setPhotoQualityPrioritization(qualityPrioritization: PhotoQualityPrioritization): void

Sets the photo quality prioritization strategy.

Before setting the strategy, you can call [isPhotoQualityPrioritizationSupported](#isphotoqualityprioritizationsupported21) to check whether the device supports the specified photo quality prioritization strategy.

**Atomic service API**: This API can be used in atomic services since API version 21.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| qualityPrioritization | [PhotoQualityPrioritization](../enums/document.md#photoqualityprioritization21) | Yes | Photo quality prioritization strategy. |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400102 | Operation not allowed. |
| 7400201 | Camera service fatal error, reconfiguring streams is needed to recover from failure. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { camera } from '@kit.CameraKit';

let photoOutput: camera.PhotoOutput;

function setPhotoQualityPrioritization(qualityPrioritization: camera.PhotoQualityPrioritization): void {
  try {
    photoOutput.setPhotoQualityPrioritization(qualityPrioritization);
  } catch (error) {
    let err = error as BusinessError;
    console.error(\`The setPhotoQualityPrioritization call failed. error code: ${err.code}\`);
  }
}
