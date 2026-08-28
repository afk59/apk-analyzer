# Interface (AVRecorder)

AVRecorder is a class for audio and video recording management. It provides APIs to record media assets. Before calling any API in AVRecorder, you must use [createAVRecorder()](../functions/document.md#mediacreateavrecorder9) to create an AVRecorder instance.

For details about the audio and video recording demo, see [Audio Recording](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/using-avrecorder-for-recording) and [Video Recording](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/video-recording).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/bry0gOnySEOaXiE216J6IA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062437Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DF63FF0727C025C4A030CDF15F945CD184506E044B97955AE9055C26AD1E3D02)

-   The initial APIs of this module are supported since API version 6. Newly added APIs will be marked with a superscript to indicate their earliest API version.
-   The initial APIs of this interface are supported since API version 9.
    
    To use the camera to record videos, the camera module is required. For details about how to use the APIs provided by the camera module, see [Camera Management](../../../../camera-kit/arkts-apis/ohos-multimedia-camera-camera-management/module-description/document.md).
    

#### Modules to Import

import { media } from '@kit.MediaKit';

#### Properties

**System capability**: SystemCapability.Multimedia.Media.AVRecorder

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| state9+ | [AVRecorderState](../types/document.md#avrecorderstate9) | Yes | No | 
AVRecorder state.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |

#### prepare9+

prepare(config: AVRecorderConfig, callback: AsyncCallback<void>): void

Sets audio and video recording parameters. This API uses an asynchronous callback to return the result.

**Required permissions:** ohos.permission.MICROPHONE

This permission is required only if audio recording is involved.

To use the camera to record videos, the camera module is required. For details about how to use the APIs provided by the camera module, see [Camera Management](../../../../camera-kit/arkts-apis/ohos-multimedia-camera-camera-management/module-description/document.md).

**System capability**: SystemCapability.Multimedia.Media.AVRecorder

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| config | [AVRecorderConfig](../interfaces-others/document.md#avrecorderconfig9) | Yes | Audio and video recording parameters to set. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Media Error Codes](../../../error-codes/media-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. Return by callback. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 5400102 | Operate not permit. Return by callback. |
| 5400105 | Service died. Return by callback. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

// Configure the parameters based on those supported by the hardware device.
let avRecorderProfile: media.AVRecorderProfile = {
  audioBitrate : 48000,
  audioChannels : 2,
  audioCodec : media.CodecMimeType.AUDIO\_AAC,
  audioSampleRate : 48000,
  fileFormat : media.ContainerFormatType.CFT\_MPEG\_4,
  videoBitrate : 2000000,
  videoCodec : media.CodecMimeType.VIDEO\_AVC,
  videoFrameWidth : 640,
  videoFrameHeight : 480,
  videoFrameRate : 30
};
let videoMetaData: media.AVMetadata = {
  videoOrientation: '0' // The value can be 0, 90, 180, or 270. If any other value is used, prepare() reports an error.
};
let avRecorderConfig: media.AVRecorderConfig = {
  audioSourceType : media.AudioSourceType.AUDIO\_SOURCE\_TYPE\_MIC,
  videoSourceType : media.VideoSourceType.VIDEO\_SOURCE\_TYPE\_SURFACE\_YUV,
  profile : avRecorderProfile,
  url : 'fd://', // Before passing an FD to this parameter, the file must be created by the caller and granted with the read and write permissions. Example value: fd://45.
  metadata: videoMetaData,
  location : { latitude : 30, longitude : 130 }
};

avRecorder.prepare(avRecorderConfig, (err: BusinessError) => {
  if (err) {
    console.error(\`Failed to prepare and error is: Code: ${err.code}, message: ${err.message}\`);
  } else {
    console.info('Succeeded in preparing');
  }
});

#### prepare9+

prepare(config: AVRecorderConfig): Promise<void>

Sets audio and video recording parameters. This API uses a promise to return the result.

**Required permissions:** ohos.permission.MICROPHONE

This permission is required only if audio recording is involved.

To use the camera to record videos, the camera module is required. For details about how to use the APIs provided by the camera module, see [Camera Management](../../../../camera-kit/arkts-apis/ohos-multimedia-camera-camera-management/module-description/document.md).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.Media.AVRecorder

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| config | [AVRecorderConfig](../interfaces-others/document.md#avrecorderconfig9) | Yes | Audio and video recording parameters to set. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Media Error Codes](../../../error-codes/media-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. Return by promise. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 5400102 | Operate not permit. Return by promise. |
| 5400105 | Service died. Return by promise. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

// Configure the parameters based on those supported by the hardware device.
let avRecorderProfile: media.AVRecorderProfile = {
  audioBitrate : 48000,
  audioChannels : 2,
  audioCodec : media.CodecMimeType.AUDIO\_AAC,
  audioSampleRate : 48000,
  fileFormat : media.ContainerFormatType.CFT\_MPEG\_4,
  videoBitrate : 2000000,
  videoCodec : media.CodecMimeType.VIDEO\_AVC,
  videoFrameWidth : 640,
  videoFrameHeight : 480,
  videoFrameRate : 30
};
let videoMetaData: media.AVMetadata = {
  videoOrientation: '0' // The value can be 0, 90, 180, or 270. If any other value is used, prepare() reports an error.
};
let avRecorderConfig: media.AVRecorderConfig = {
  audioSourceType : media.AudioSourceType.AUDIO\_SOURCE\_TYPE\_MIC,
  videoSourceType : media.VideoSourceType.VIDEO\_SOURCE\_TYPE\_SURFACE\_YUV,
  profile : avRecorderProfile,
  url : 'fd://',  // Before passing an FD to this parameter, the file must be created by the caller and granted with the read and write permissions. Example value: fd://45.
  metadata : videoMetaData,
  location : { latitude : 30, longitude : 130 }
};

avRecorder.prepare(avRecorderConfig).then(() => {
  console.info('Succeeded in preparing');
}).catch((err: Error) => {
  let error: BusinessError = err as BusinessError;
  console.error(\`Failed to prepare and error is: Code: ${error.code}, message: ${error.message}\`);
});

#### getInputSurface9+

getInputSurface(callback: AsyncCallback<string>): void

Obtains the surface required for recording. This API uses an asynchronous callback to return the result.

The caller obtains the surface buffer from this surface and fills in the corresponding video data.

Note that the video data must carry the timestamp (in ns) and buffer size, and the start time of the timestamp must be based on the system startup time.

This API can be called only after the [prepare()](#prepare9) API is called.

**System capability**: SystemCapability.Multimedia.Media.AVRecorder

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<string> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the surface ID obtained; otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Media Error Codes](../../../error-codes/media-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 5400102 | Operate not permit. Return by callback. |
| 5400103 | IO error. Return by callback. |
| 5400105 | Service died. Return by callback. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
let surfaceID: string; // The surfaceID is transferred to the camera API to create a videoOutput instance.

avRecorder.getInputSurface((err: BusinessError, surfaceId: string) => {
  if (err) {
    console.error(\`Failed to do getInputSurface and error is: Code: ${err.code}, message: ${err.message}\`);
  } else {
    console.info('Succeeded in doing getInputSurface');
    surfaceID = surfaceId;
  }
});

#### getInputSurface9+

getInputSurface(): Promise<string>

Obtains the surface required for recording. This API uses a promise to return the result.

The caller obtains the surface buffer from this surface and fills in the corresponding video data.

Note that the video data must carry the timestamp (in ns) and buffer size, and the start time of the timestamp must be based on the system startup time.

This API can be called only after the [prepare()](#prepare9-1) API is called.

**System capability**: SystemCapability.Multimedia.Media.AVRecorder

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<string> | Promise used to return the surface buffer obtained from the surface. |

**Error codes**

For details about the error codes, see [Media Error Codes](../../../error-codes/media-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 5400102 | Operate not permit. Return by promise. |
| 5400103 | IO error. Return by promise. |
| 5400105 | Service died. Return by promise. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
let surfaceID: string; // The surfaceID is transferred to the camera API to create a videoOutput instance.

avRecorder.getInputSurface().then((surfaceId: string) => {
  console.info('Succeeded in getting InputSurface');
  surfaceID = surfaceId;
}).catch((err: Error) => {
  let error: BusinessError = err as BusinessError;
  console.error(\`Failed to get InputSurface and error is: Code: ${error.code}, message: ${error.message}\`);
});

#### updateRotation12+

updateRotation(rotation: number): Promise<void>

Updates the video rotation angle. This API uses a promise to return the result.

This API can be called only after the [prepare()](#prepare9-1) event is triggered and before the [start()](#start9) API is called.

**System capability**: SystemCapability.Multimedia.Media.AVRecorder

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| rotation | number | Yes | Rotation angle, which can only be 0, 90, 180, or 270 degrees. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Media Error Codes](../../../error-codes/media-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 5400102 | Operation not allowed. Return by promise. |
| 5400103 | IO error. Return by promise. |
| 5400105 | Service died. Return by promise. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let rotation = 90;

avRecorder.updateRotation(rotation).then(() => {
  console.info('Succeeded in doing updateRotation');
}).catch((err: Error) => {
  let error: BusinessError = err as BusinessError;
  console.error(\`Failed to do updateRotation and error is: Code: ${error.code}, message: ${error.message}\`);
});

#### setWillMuteWhenInterrupted20+

setWillMuteWhenInterrupted(muteWhenInterrupted: boolean): Promise<void>

Sets whether to mute the current audio recording stream when an audio interruption occurs. This API uses a promise to return the result.

**System capability**: SystemCapability.Multimedia.Media.AVRecorder

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| muteWhenInterrupted | boolean | Yes | Whether to mute the current audio recording stream during an audio interruption. **true** to mute, **false** otherwise. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Media Error Codes](../../../error-codes/media-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 5400102 | Operation not allowed. Return by promise. |
| 5400105 | Service died. Return by promise. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

avRecorder.setWillMuteWhenInterrupted(true).then(() => {
  console.info('Succeeded in doing setWillMuteWhenInterrupted');
}).catch((err: Error) => {
  let error: BusinessError = err as BusinessError;
  console.error(\`Failed to do setWillMuteWhenInterrupted and error is: Code: ${error.code}, message: ${error.message}\`);
});

#### start9+

start(callback: AsyncCallback<void>): void

Starts video recording. This API uses an asynchronous callback to return the result.

For audio-only recording, this API can be called only after the [prepare()](#prepare9) API is called. For video-only recording, this API can be called only after the [getInputSurface()](#getinputsurface9) API is called.

**System capability**: SystemCapability.Multimedia.Media.AVRecorder

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Media Error Codes](../../../error-codes/media-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 5400102 | Operate not permit. Return by callback. |
| 5400103 | IO error. Return by callback. |
| 5400105 | Service died. Return by callback. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

avRecorder.start((err: BusinessError) => {
  if (err) {
    console.error(\`Failed to start AVRecorder and error is: Code: ${err.code}, message: ${err.message}\`);
  } else {
    console.info('Succeeded in starting AVRecorder');
  }
});

#### start9+

start(): Promise<void>

Starts video recording. This API uses a promise to return the result.

For audio-only recording, this API can be called only after the [prepare()](#prepare9-1) API is called. For video-only recording, this API can be called only after the [getInputSurface()](#getinputsurface9-1) API is called.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.Media.AVRecorder

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Media Error Codes](../../../error-codes/media-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 5400102 | Operate not permit. Return by promise. |
| 5400103 | IO error. Return by promise. |
| 5400105 | Service died. Return by promise. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

avRecorder.start().then(() => {
  console.info('Succeeded in starting AVRecorder');
}).catch((err: Error) => {
  let error: BusinessError = err as BusinessError;
  console.error(\`Failed to start AVRecorder and error is: Code: ${error.code}, message: ${error.message}\`);
});

#### pause9+

pause(callback: AsyncCallback<void>): void

Pauses video recording. This API uses an asynchronous callback to return the result.

This API can be called only after the [start()](#start9) API is called. You can call [resume()](#resume9) to resume recording.

**System capability**: SystemCapability.Multimedia.Media.AVRecorder

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Media Error Codes](../../../error-codes/media-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 5400102 | Operate not permit. Return by callback. |
| 5400103 | IO error. Return by callback. |
| 5400105 | Service died. Return by callback. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

avRecorder.pause((err: BusinessError) => {
  if (err) {
    console.error(\`Failed to pause AVRecorder and error is: Code: ${err.code}, message: ${err.message}\`);
  } else {
    console.info('Succeeded in pausing');
  }
});

#### pause9+

pause(): Promise<void>

Pauses video recording. This API uses a promise to return the result.

This API can be called only after the [start()](#start9-1) API is called. You can call [resume()](#resume9-1) to resume recording.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.Media.AVRecorder

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Media Error Codes](../../../error-codes/media-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 5400102 | Operate not permit. Return by promise. |
| 5400103 | IO error. Return by promise. |
| 5400105 | Service died. Return by promise. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

avRecorder.pause().then(() => {
  console.info('Succeeded in pausing');
}).catch((err: Error) => {
  let error: BusinessError = err as BusinessError;
  console.error(\`Failed to pause AVRecorder and error is: Code: ${error.code}, message: ${error.message}\`);
});

#### resume9+

resume(callback: AsyncCallback<void>): void

Resumes video recording. This API uses an asynchronous callback to return the result.

This API can be called only after the [pause()](#pause9) API is called.

**System capability**: SystemCapability.Multimedia.Media.AVRecorder

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Media Error Codes](../../../error-codes/media-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 5400102 | Operate not permit. Return by callback. |
| 5400103 | IO error. Return by callback. |
| 5400105 | Service died. Return by callback. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

avRecorder.resume((err: BusinessError) => {
  if (err) {
    console.error(\`Failed to resume AVRecorder and error is: Code: ${err.code}, message: ${err.message}\`);
  } else {
    console.info('Succeeded in resuming AVRecorder');
  }
});

#### resume9+

resume(): Promise<void>

Resumes video recording. This API uses a promise to return the result.

This API can be called only after the [pause()](#pause9-1) API is called.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.Media.AVRecorder

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Media Error Codes](../../../error-codes/media-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 5400102 | Operate not permit. Return by promise. |
| 5400103 | IO error. Return by promise. |
| 5400105 | Service died. Return by promise. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

avRecorder.resume().then(() => {
  console.info('Succeeded in resuming AVRecorder');
}).catch((err: Error) => {
  let error: BusinessError = err as BusinessError;
  console.error(\`Failed to resume AVRecorder failed and error is: Code: ${error.code}, message: ${error.message}\`);
});

#### stop9+

stop(callback: AsyncCallback<void>): void

Stops video recording. This API uses an asynchronous callback to return the result.

This API can be called only after the [start()](#start9) or [pause()](#pause9) API is called.

For audio-only recording, you can call [prepare()](#prepare9) again for re-recording. For video-only recording or audio and video recording, you can call [prepare()](#prepare9) and [getInputSurface()](#getinputsurface9) again for re-recording.

**System capability**: SystemCapability.Multimedia.Media.AVRecorder

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Media Error Codes](../../../error-codes/media-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 5400102 | Operate not permit. Return by callback. |
| 5400103 | IO error. Return by callback. |
| 5400105 | Service died. Return by callback. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

avRecorder.stop((err: BusinessError) => {
  if (err) {
    console.error(\`Failed to stop AVRecorder and error is: Code: ${err.code}, message: ${err.message}\`);
  } else {
    console.info('Succeeded in stopping AVRecorder');
  }
});

#### stop9+

stop(): Promise<void>

Stops video recording. This API uses a promise to return the result.

This API can be called only after the [start()](#start9-1) or [pause()](#pause9-1) API is called.

For audio-only recording, you can call [prepare()](#prepare9-1) again for re-recording. For video-only recording or audio and video recording, you can call [prepare()](#prepare9-1) and [getInputSurface()](#getinputsurface9-1) again for re-recording.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.Media.AVRecorder

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Media Error Codes](../../../error-codes/media-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 5400102 | Operate not permit. Return by promise. |
| 5400103 | IO error. Return by promise. |
| 5400105 | Service died. Return by promise. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

avRecorder.stop().then(() => {
  console.info('Succeeded in stopping AVRecorder');
}).catch((err: Error) => {
  let error: BusinessError = err as BusinessError;
  console.error(\`Failed to stop AVRecorder and error is: Code: ${error.code}, message: ${error.message}\`);
});

#### reset9+

reset(callback: AsyncCallback<void>): void

Resets audio and video recording. This API uses an asynchronous callback to return the result.

For audio-only recording, you can call [prepare()](#prepare9) again for re-recording. For video-only recording or audio and video recording, you can call [prepare()](#prepare9) and [getInputSurface()](#getinputsurface9) again for re-recording.

**System capability**: SystemCapability.Multimedia.Media.AVRecorder

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Media Error Codes](../../../error-codes/media-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 5400103 | IO error. Return by callback. |
| 5400105 | Service died. Return by callback. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

avRecorder.reset((err: BusinessError) => {
  if (err) {
    console.error(\`Failed to reset AVRecorder and error is: Code: ${err.code}, message: ${err.message}\`);
  } else {
    console.info('Succeeded in resetting AVRecorder');
  }
});

#### reset9+

reset(): Promise<void>

Resets audio and video recording. This API uses a promise to return the result.

For audio-only recording, you can call [prepare()](#prepare9-1) again for re-recording. For video-only recording or audio and video recording, you can call [prepare()](#prepare9-1) and [getInputSurface()](#getinputsurface9-1) again for re-recording.

**System capability**: SystemCapability.Multimedia.Media.AVRecorder

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Media Error Codes](../../../error-codes/media-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 5400103 | IO error. Return by promise. |
| 5400105 | Service died. Return by promise. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

avRecorder.reset().then(() => {
  console.info('Succeeded in resetting AVRecorder');
}).catch((err: Error) => {
  let error: BusinessError = err as BusinessError;
  console.error(\`Failed to reset AVRecorder and error is: Code: ${error.code}, message: ${error.message}\`);
});

#### release9+

release(callback: AsyncCallback<void>): void

Releases the audio and video recording resources. This API uses an asynchronous callback to return the result.

After the resources are released, you can no longer perform any operation on the AVRecorder instance.

**System capability**: SystemCapability.Multimedia.Media.AVRecorder

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Media Error Codes](../../../error-codes/media-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 5400105 | Service died. Return by callback. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

avRecorder.release((err: BusinessError) => {
  if (err) {
    console.error(\`Failed to release AVRecorder and error is: Code: ${err.code}, message: ${err.message}\`);
  } else {
    console.info('Succeeded in releasing AVRecorder');
  }
});

#### release9+

release(): Promise<void>

Releases the audio and video recording resources. This API uses a promise to return the result.

After the resources are released, you can no longer perform any operation on the AVRecorder instance.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.Media.AVRecorder

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Media Error Codes](../../../error-codes/media-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 5400105 | Service died. Return by callback. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

avRecorder.release().then(() => {
  console.info('Succeeded in releasing AVRecorder');
}).catch((err: Error) => {
  let error: BusinessError = err as BusinessError;
  console.error(\`Failed to release AVRecorder and error is: Code: ${error.code}, message: ${error.message}\`);
});

#### getCurrentAudioCapturerInfo11+

getCurrentAudioCapturerInfo(callback: AsyncCallback<audio.AudioCapturerChangeInfo>): void

Obtains the information about the current audio capturer. This API uses an asynchronous callback to return the result.

This API can be called only after the [prepare()](#prepare9) API is called. If this API is called after [stop()](#stop9) is successfully called, an error is reported.

**System capability**: SystemCapability.Multimedia.Media.AVRecorder

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[audio.AudioCapturerChangeInfo](../../../../audio-kit/arkts-apis/ohos-multimedia-audio-audio-management/interfaces-others/document.md#audiocapturerchangeinfo9)\> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the audio.AudioCapturerChangeInfo object obtained; otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Media Error Codes](../../../error-codes/media-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 5400102 | Operation not allowed. |
| 5400103 | I/O error. |
| 5400105 | Service died. Return by callback. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { audio } from '@kit.AudioKit';

let currentCapturerInfo: audio.AudioCapturerChangeInfo;

avRecorder.getCurrentAudioCapturerInfo((err: BusinessError, capturerInfo: audio.AudioCapturerChangeInfo) => {
  if (err) {
    console.error(\`Failed to get CurrentAudioCapturerInfo and error is: Code: ${err.code}, message: ${err.message}\`);
  } else {
    console.info('Succeeded in getting CurrentAudioCapturerInfo');
    currentCapturerInfo = capturerInfo;
  }
});

#### getCurrentAudioCapturerInfo11+

getCurrentAudioCapturerInfo(): Promise<audio.AudioCapturerChangeInfo>

Obtains the information about the current audio capturer. This API uses a promise to return the result.

This API can be called only after the [prepare()](#prepare9) API is called. If this API is called after [stop()](#stop9) is successfully called, an error is reported.

**System capability**: SystemCapability.Multimedia.Media.AVRecorder

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[audio.AudioCapturerChangeInfo](../../../../audio-kit/arkts-apis/ohos-multimedia-audio-audio-management/interfaces-others/document.md#audiocapturerchangeinfo9)\> | Promise used to return the audio capturer information. |

**Error codes**

For details about the error codes, see [Media Error Codes](../../../error-codes/media-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 5400102 | Operation not allowed. |
| 5400103 | I/O error. |
| 5400105 | Service died. Return by promise. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { audio } from '@kit.AudioKit';

let currentCapturerInfo: audio.AudioCapturerChangeInfo;

avRecorder.getCurrentAudioCapturerInfo().then((capturerInfo: audio.AudioCapturerChangeInfo) => {
  console.info('Succeeded in getting CurrentAudioCapturerInfo');
  currentCapturerInfo = capturerInfo;
}).catch((err: Error) => {
  let error: BusinessError = err as BusinessError;
  console.error(\`Failed to get CurrentAudioCapturerInfo and error is: Code: ${error.code}, message: ${error.message}\`);
});

#### getAudioCapturerMaxAmplitude11+

getAudioCapturerMaxAmplitude(callback: AsyncCallback<number>): void

Obtains the maximum amplitude of the current audio capturer. This API uses an asynchronous callback to return the result.

This API can be called only after the [prepare()](#prepare9) API is called. If this API is called after [stop()](#stop9) is successfully called, an error is reported.

The return value is the maximum amplitude within the duration from the time the maximum amplitude is obtained last time to the current time. For example, if you have obtained the maximum amplitude at 1s and you call this API again at 2s, then the return value is the maximum amplitude within the duration from 1s to 2s.

**System capability**: SystemCapability.Multimedia.Media.AVRecorder

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<number> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the maximum amplitude obtained; otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Media Error Codes](../../../error-codes/media-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 5400102 | Operation not allowed. |
| 5400105 | Service died. Return by callback. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let maxAmplitude: number;

avRecorder.getAudioCapturerMaxAmplitude((err: BusinessError, amplitude: number) => {
  if (err) {
    console.error(\`Failed to get AudioCapturerMaxAmplitude and error is: Code: ${err.code}, message: ${err.message}\`);
  } else {
    console.info('Succeeded in getting AudioCapturerMaxAmplitude');
    maxAmplitude = amplitude;
  }
});

#### getAudioCapturerMaxAmplitude11+

getAudioCapturerMaxAmplitude(): Promise<number>

Obtains the maximum amplitude of the current audio capturer. This API uses a promise to return the result.

This API can be called only after the [prepare()](#prepare9) API is called. If this API is called after [stop()](#stop9) is successfully called, an error is reported.

The return value is the maximum amplitude within the duration from the time the maximum amplitude is obtained last time to the current time. For example, if you have obtained the maximum amplitude at 1s and you call this API again at 2s, then the return value is the maximum amplitude within the duration from 1s to 2s.

**System capability**: SystemCapability.Multimedia.Media.AVRecorder

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the maximum amplitude obtained. |

**Error codes**

For details about the error codes, see [Media Error Codes](../../../error-codes/media-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 5400102 | Operation not allowed. |
| 5400105 | Service died. Return by promise. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let maxAmplitude: number;

avRecorder.getAudioCapturerMaxAmplitude().then((amplitude: number) => {
  console.info('Succeeded in getting AudioCapturerMaxAmplitude');
  maxAmplitude = amplitude;
}).catch((err: Error) => {
  let error: BusinessError = err as BusinessError;
  console.error(\`Failed to get AudioCapturerMaxAmplitude and error is: Code: ${error.code}, message: ${error.message}\`);
});

#### getAvailableEncoder11+

getAvailableEncoder(callback: AsyncCallback<Array<EncoderInfo>>): void

Obtains available encoders. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.Media.AVRecorder

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<Array<[EncoderInfo](../interfaces-others/document.md#encoderinfo11)\>> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the available encoders obtained; otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Media Error Codes](../../../error-codes/media-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 5400102 | Operation not allowed. |
| 5400105 | Service died. Return by callback. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let encoderInfo: media.EncoderInfo;

avRecorder.getAvailableEncoder((err: BusinessError, info: media.EncoderInfo\[\]) => {
  if (err) {
    console.error(\`Failed to get AvailableEncoder and error is: Code: ${err.code}, message: ${err.message}\`);
  } else {
    console.info('Succeeded in getting AvailableEncoder');
    if (info.length > 0) {
      encoderInfo = info\[0\];
    } else {
      console.error('No available encoder');
    }
  }
});

#### getAvailableEncoder11+

getAvailableEncoder(): Promise<Array<EncoderInfo>>

Obtains available encoders. This API uses a promise to return the result.

**System capability**: SystemCapability.Multimedia.Media.AVRecorder

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<[EncoderInfo](../interfaces-others/document.md#encoderinfo11)\>> | Promise used to return the information about the available encoders. |

**Error codes**

For details about the error codes, see [Media Error Codes](../../../error-codes/media-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 5400102 | Operation not allowed. |
| 5400105 | Service died. Return by promise. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let encoderInfo: media.EncoderInfo;

avRecorder.getAvailableEncoder().then((info: media.EncoderInfo\[\]) => {
  console.info('Succeeded in getting AvailableEncoder');
    if (info.length > 0) {
      encoderInfo = info\[0\];
    } else {
      console.error('No available encoder');
    }
}).catch((err: Error) => {
  let error: BusinessError = err as BusinessError;
  console.error(\`Failed to get AvailableEncoder and error is: Code: ${error.code}, message: ${error.message}\`);
});

#### getAVRecorderConfig11+

getAVRecorderConfig(callback: AsyncCallback<AVRecorderConfig>): void

Obtains the real-time configuration of this AVRecorder. This API uses an asynchronous callback to return the result.

This API can be called only after [prepare()](#prepare9) is called.

**System capability**: SystemCapability.Multimedia.Media.AVRecorder

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[AVRecorderConfig](../interfaces-others/document.md#avrecorderconfig9)\> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the real-time configuration obtained; otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Media Error Codes](../../../error-codes/media-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 5400102 | Operate not permit. Return by callback. |
| 5400103 | IO error. Return by callback. |
| 5400105 | Service died. Return by callback. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let avConfig: media.AVRecorderConfig;

avRecorder.getAVRecorderConfig((err: BusinessError, config: media.AVRecorderConfig) => {
  if (err) {
    console.error(\`Failed to get avConfig and error is: Code: ${err.code}, message: ${err.message}\`);
  } else {
    console.info('Succeeded in getting AVRecorderConfig');
    avConfig = config;
  }
});

#### getAVRecorderConfig11+

getAVRecorderConfig(): Promise<AVRecorderConfig>;

Obtains the real-time configuration of this AVRecorder. This API uses a promise to return the result.

This API can be called only after [prepare()](#prepare9-1) is called.

**System capability**: SystemCapability.Multimedia.Media.AVRecorder

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[AVRecorderConfig](../interfaces-others/document.md#avrecorderconfig9)\> | Promise used to return the real-time configuration. |

**Error codes**

For details about the error codes, see [Media Error Codes](../../../error-codes/media-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 5400102 | Operate not permit. Return by promise. |
| 5400103 | IO error. Return by promise. |
| 5400105 | Service died. Return by promise. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let avConfig: media.AVRecorderConfig;

avRecorder.getAVRecorderConfig().then((config: media.AVRecorderConfig) => {
  console.info('Succeeded in getting AVRecorderConfig');
  avConfig = config;
}).catch((err: Error) => {
  let error: BusinessError = err as BusinessError;
  console.error(\`Failed to get AVRecorderConfig and error is: Code: ${error.code}, message: ${error.message}\`);
});

#### on('stateChange')9+

on(type: 'stateChange', callback: OnAVRecorderStateChangeHandler): void

Subscribes to AVRecorder state changes. An application can subscribe to only one AVRecorder state change event. When the application initiates multiple subscriptions to this event, the last subscription is applied. This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.Media.AVRecorder

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which is **'stateChange'** in this case. This event can be triggered by both user operations and the system. |
| callback | [OnAVRecorderStateChangeHandler](../types/document.md#onavrecorderstatechangehandler12) | Yes | Callback used to return the state change event. |

**Error codes**

For details about the error codes, see [Media Error Codes](../../../error-codes/media-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 5400103 | IO error. Return by callback. |
| 5400105 | Service died. Return by callback. |

**Example**

avRecorder.on('stateChange', async (state: media.AVRecorderState, reason: media.StateChangeReason) => {
  console.info('case state has changed, new state is: ' + state + ', and reason is: ' + reason);
});

#### off('stateChange')9+

off(type: 'stateChange', callback?: OnAVRecorderStateChangeHandler): void

Unsubscribes from AVRecorder state changes. This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.Media.AVRecorder

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which is **'stateChange'** in this case. This event can be triggered by both user operations and the system. |
| callback12+ | [OnAVRecorderStateChangeHandler](../types/document.md#onavrecorderstatechangehandler12) | No | 
Callback used to return the state change event. If this parameter is specified, the subscription to the specified event with the specified callback is canceled. (The callback object cannot be an anonymous function.) Otherwise, the subscriptions to the specified event with all the callbacks are canceled.

This parameter is supported since API version 12.

 |

**Example**

avRecorder.off('stateChange');

#### on('error')9+

on(type: 'error', callback: ErrorCallback): void

Subscribes to AVRecorder errors. This event is used only for error prompt and does not require the user to stop recording control. If the [AVRecorderState](../types/document.md#avrecorderstate9) is also switched to error, call [reset()](#reset9) or \[release()\][release()](#release9) to exit the recording. This API uses an asynchronous callback to return the result.

An application can subscribe to only one AVRecorder error event. When the application initiates multiple subscriptions to this event, the last subscription is applied.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.Media.AVRecorder

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type, which is **'error'** in this case.

This event is triggered when an error occurs during recording.

 |
| callback | [ErrorCallback](../../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#errorcallback) | Yes | Callback used to return the recording error event. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Media Error Codes](../../../error-codes/media-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 801 | Capability not supported. |
| 5400101 | No memory. |
| 5400102 | Operation not allowed. |
| 5400103 | I/O error. |
| 5400104 | Time out. |
| 5400105 | Service died. |
| 5400106 | Unsupported format. |
| 5400107 | Audio interrupted. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

avRecorder.on('error', (err: BusinessError) => {
  console.error(\`case avRecorder.on(error) called. Code: ${err.code}, message: ${err.message}\`);
});

#### off('error')9+

off(type: 'error', callback?: ErrorCallback): void

Unsubscribes from AVRecorder errors. After the unsubscription, your application can no longer receive AVRecorder errors. This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.Media.AVRecorder

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type, which is **'error'** in this case.

This event is triggered when an error occurs during recording.

 |
| callback12+ | [ErrorCallback](../../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#errorcallback) | No | 

Callback used to return the recording error event. If this parameter is specified, the subscription to the specified event with the specified callback is canceled. (The callback object cannot be an anonymous function.) Otherwise, the subscriptions to the specified event with all the callbacks are canceled.

This parameter is supported since API version 12.

 |

**Example**

avRecorder.off('error');

#### on('audioCapturerChange')11+

on(type: 'audioCapturerChange', callback: Callback<audio.AudioCapturerChangeInfo>): void

Subscribes to audio capturer configuration changes. Any configuration change triggers the callback that returns the entire configuration information. This API uses an asynchronous callback to return the result.

When the application initiates multiple subscriptions to this event, the last subscription is applied.

**System capability**: SystemCapability.Multimedia.Media.AVRecorder

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which is **'audioCapturerChange'** in this case. |
| callback | Callback<[audio.AudioCapturerChangeInfo](../../../../audio-kit/arkts-apis/ohos-multimedia-audio-audio-management/interfaces-others/document.md#audiocapturerchangeinfo9)\> | Yes | Callback used to return the changed audio capturer configuration. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

**Example**

import { audio } from '@kit.AudioKit'

let capturerChangeInfo: audio.AudioCapturerChangeInfo;

avRecorder.on('audioCapturerChange',  (audioCapturerChangeInfo: audio.AudioCapturerChangeInfo) => {
  console.info('audioCapturerChange called');
  capturerChangeInfo = audioCapturerChangeInfo;
});

#### off('audioCapturerChange')11+

off(type: 'audioCapturerChange', callback?: Callback<audio.AudioCapturerChangeInfo>): void

Subscribes to audio capturer configuration changes. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.Media.AVRecorder

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which is **'audioCapturerChange'** in this case. |
| callback12+ | Callback<[audio.AudioCapturerChangeInfo](../../../../audio-kit/arkts-apis/ohos-multimedia-audio-audio-management/interfaces-others/document.md#audiocapturerchangeinfo9)\> | No | 
Callback used to return the changed audio capturer configuration. If this parameter is specified, the subscription to the specified event with the specified callback is canceled. (The callback object cannot be an anonymous function.) Otherwise, the subscriptions to the specified event with all the callbacks are canceled.

This parameter is supported since API version 12.

 |

**Example**

avRecorder.off('audioCapturerChange');

#### on('photoAssetAvailable')12+

on(type: 'photoAssetAvailable', callback: Callback<photoAccessHelper.PhotoAsset>): void

Subscribes to media asset callback events. When [FileGenerationMode](../enums/document.md#filegenerationmode12) is used during media file creation, the [PhotoAsset](../../../../media-library-kit/arkts-apis/ohos-file-photoaccesshelper-album-management/interface-photoasset/document.md) object is called back to the application after the [stop](#stop9) operation is complete. This API uses an asynchronous callback to return the result.

When the application initiates multiple subscriptions to this event, the last subscription is applied.

**System capability**: SystemCapability.Multimedia.Media.AVRecorder

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which is **'photoAssetAvailable'** in this case. The event is triggered when a photo asset is available. |
| callback | Callback<[photoAccessHelper.PhotoAsset](../../../../media-library-kit/arkts-apis/ohos-file-photoaccesshelper-album-management/interface-photoasset/document.md)\> | Yes | Callback used to return the PhotoAsset object corresponding to the resource file created by the system. |

**Error codes**

For details about the error codes, see [Media Error Codes](../../../error-codes/media-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 5400103 | IO error. Return by callback. |
| 5400105 | Service died. Return by callback. |

**Example**

import { photoAccessHelper } from '@kit.MediaLibraryKit';
let photoAsset: photoAccessHelper.PhotoAsset;

// Example: Process the photoAsset callback and save the video.
async function saveVideo(context: Context, asset: photoAccessHelper.PhotoAsset) {
  console.info("saveVideo called");
  try {
    let phAccessHelper = photoAccessHelper.getPhotoAccessHelper(context);
    let assetChangeRequest: photoAccessHelper.MediaAssetChangeRequest = new photoAccessHelper.MediaAssetChangeRequest(asset);
    assetChangeRequest.saveCameraPhoto();
    await phAccessHelper.applyChanges(assetChangeRequest);
    console.info('apply saveVideo successfully');
  } catch (err) {
    console.error(\`apply saveVideo failed with error: ${err.code}, ${err.message}\`);
  }
}
// Subscribe to the photoAsset event.
avRecorder.on('photoAssetAvailable', (asset: photoAccessHelper.PhotoAsset) => {
  console.info('photoAssetAvailable called');
  if (asset != undefined) {
    photoAsset = asset;
    // Process the photoAsset callback.
    // Example: this.saveVideo(context, asset);
  } else {
    console.error('photoAsset is undefined');
  }
});

#### off('photoAssetAvailable')12+

off(type: 'photoAssetAvailable', callback?: Callback<photoAccessHelper.PhotoAsset>): void

Unsubscribes from media asset callback events. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.Media.AVRecorder

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which is **'photoAssetAvailable'** in this case. |
| callback | Callback<[photoAccessHelper.PhotoAsset](../../../../media-library-kit/arkts-apis/ohos-file-photoaccesshelper-album-management/interface-photoasset/document.md)\> | No | Callback used to return the PhotoAsset object corresponding to the resource file created by the system. If this parameter is specified, the subscription to the specified event with the specified callback is canceled. (The callback object cannot be an anonymous function.) Otherwise, the subscriptions to the specified event with all the callbacks are canceled. |

**Example**

avRecorder.off('photoAssetAvailable');
