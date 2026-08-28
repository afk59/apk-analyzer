# Interface (AudioCapturer)

This interface provides APIs for audio capture.

Before calling any API in AudioCapturer, you must use [createAudioCapturer](../functions/document.md#audiocreateaudiocapturer8) to create an AudioCapturer instance.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/piFaXjqATh2kYkTc8mn8MQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062417Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A06339850ADA0B1EB3A494FF890C23C87077567249F8747DCEF526B25FA55C00)

-   The initial APIs of this module are supported since API version 7. Newly added APIs will be marked with a superscript to indicate their earliest API version.
-   The initial APIs of this interface are supported since API version 8.

#### Modules to Import

import { audio } from '@kit.AudioKit';

#### Properties

**System capability**: SystemCapability.Multimedia.Audio.Capturer

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| state8+ | [AudioState](../enums/document.md#audiostate8) | Yes | No | Audio capturer state. |

**Example**

import { audio } from '@kit.AudioKit';

let state: audio.AudioState = audioCapturer.state;

#### getCapturerInfo8+

getCapturerInfo(callback: AsyncCallback<AudioCapturerInfo>): void

Obtains the audio capturer information. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Capturer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[AudioCapturerInfo](../interfaces-others/document.md#audiocapturerinfo8)\> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the capturer information obtained; otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

audioCapturer.getCapturerInfo((err: BusinessError, capturerInfo: audio.AudioCapturerInfo) => {
  if (err) {
    console.error('Failed to get capture info');
  } else {
    console.info('Capturer getCapturerInfo:');
    console.info(\`Capturer source: ${capturerInfo.source}\`);
    console.info(\`Capturer flags: ${capturerInfo.capturerFlags}\`);
  }
});

#### getCapturerInfo8+

getCapturerInfo(): Promise<AudioCapturerInfo>

Obtains the audio capturer information. This API uses a promise to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Capturer

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[AudioCapturerInfo](../interfaces-others/document.md#audiocapturerinfo8)\> | Promise used to return the audio capturer information. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

audioCapturer.getCapturerInfo().then((audioParamsGet: audio.AudioCapturerInfo) => {
  if (audioParamsGet != undefined) {
    console.info('AudioFrameworkRecLog: Capturer CapturerInfo:');
    console.info(\`AudioFrameworkRecLog: Capturer SourceType: ${audioParamsGet.source}\`);
    console.info(\`AudioFrameworkRecLog: Capturer capturerFlags: ${audioParamsGet.capturerFlags}\`);
  } else {
    console.info(\`AudioFrameworkRecLog: audioParamsGet is : ${audioParamsGet}\`);
    console.info('AudioFrameworkRecLog: audioParams getCapturerInfo are incorrect');
  }
}).catch((err: BusinessError) => {
  console.error(\`AudioFrameworkRecLog: CapturerInfo :ERROR: ${err}\`);
})

#### getCapturerInfoSync10+

getCapturerInfoSync(): AudioCapturerInfo

Obtains the audio capturer information. This API returns the result synchronously.

**System capability**: SystemCapability.Multimedia.Audio.Capturer

**Return value**

| Type | Description |
| :-- | :-- |
| [AudioCapturerInfo](../interfaces-others/document.md#audiocapturerinfo8) | Audio capturer information. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let audioParamsGet: audio.AudioCapturerInfo = audioCapturer.getCapturerInfoSync();
  console.info(\`AudioFrameworkRecLog: Capturer SourceType: ${audioParamsGet.source}\`);
  console.info(\`AudioFrameworkRecLog: Capturer capturerFlags: ${audioParamsGet.capturerFlags}\`);
} catch (err) {
  let error = err as BusinessError;
  console.error(\`AudioFrameworkRecLog: CapturerInfo :ERROR: ${error}\`);
}

#### getStreamInfo8+

getStreamInfo(callback: AsyncCallback<AudioStreamInfo>): void

Obtains the stream information of this audio capturer. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Capturer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[AudioStreamInfo](../interfaces-others/document.md#audiostreaminfo8)\> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the stream information obtained; otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

audioCapturer.getStreamInfo((err: BusinessError, streamInfo: audio.AudioStreamInfo) => {
  if (err) {
    console.error('Failed to get stream info');
  } else {
    console.info('Capturer GetStreamInfo:');
    console.info(\`Capturer sampling rate: ${streamInfo.samplingRate}\`);
    console.info(\`Capturer channel: ${streamInfo.channels}\`);
    console.info(\`Capturer format: ${streamInfo.sampleFormat}\`);
    console.info(\`Capturer encoding type: ${streamInfo.encodingType}\`);
  }
});

#### getStreamInfo8+

getStreamInfo(): Promise<AudioStreamInfo>

Obtains the stream information of this audio capturer. This API uses a promise to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Capturer

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[AudioStreamInfo](../interfaces-others/document.md#audiostreaminfo8)\> | Promise used to return the stream information. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

audioCapturer.getStreamInfo().then((audioParamsGet: audio.AudioStreamInfo) => {
  console.info('getStreamInfo:');
  console.info(\`sampleFormat: ${audioParamsGet.sampleFormat}\`);
  console.info(\`samplingRate: ${audioParamsGet.samplingRate}\`);
  console.info(\`channels: ${audioParamsGet.channels}\`);
  console.info(\`encodingType: ${audioParamsGet.encodingType}\`);
}).catch((err: BusinessError) => {
  console.error(\`getStreamInfo :ERROR: ${err}\`);
});

#### getStreamInfoSync10+

getStreamInfoSync(): AudioStreamInfo

Obtains the stream information of this audio capturer. This API returns the result synchronously.

**System capability**: SystemCapability.Multimedia.Audio.Capturer

**Return value**

| Type | Description |
| :-- | :-- |
| [AudioStreamInfo](../interfaces-others/document.md#audiostreaminfo8) | Stream information. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let audioParamsGet: audio.AudioStreamInfo = audioCapturer.getStreamInfoSync();
  console.info(\`sampleFormat: ${audioParamsGet.sampleFormat}\`);
  console.info(\`samplingRate: ${audioParamsGet.samplingRate}\`);
  console.info(\`channels: ${audioParamsGet.channels}\`);
  console.info(\`encodingType: ${audioParamsGet.encodingType}\`);
} catch (err) {
  let error = err as BusinessError;
  console.error(\`getStreamInfo :ERROR: ${error}\`);
}

#### getAudioStreamId9+

getAudioStreamId(callback: AsyncCallback<number>): void

Obtains the stream ID of this audio capturer. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Capturer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<number> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the stream ID obtained; otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

audioCapturer.getAudioStreamId((err: BusinessError, streamId: number) => {
  console.info(\`audioCapturer GetStreamId: ${streamId}\`);
});

#### getAudioStreamId9+

getAudioStreamId(): Promise<number>

Obtains the stream ID of this audio capturer. This API uses a promise to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Capturer

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the stream ID. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

audioCapturer.getAudioStreamId().then((streamId: number) => {
  console.info(\`audioCapturer getAudioStreamId: ${streamId}\`);
}).catch((err: BusinessError) => {
  console.error(\`ERROR: ${err}\`);
});

#### getAudioStreamIdSync10+

getAudioStreamIdSync(): number

Obtains the stream ID of this audio capturer. This API returns the result synchronously.

**System capability**: SystemCapability.Multimedia.Audio.Capturer

**Return value**

| Type | Description |
| :-- | :-- |
| number | Stream ID. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let streamId: number = audioCapturer.getAudioStreamIdSync();
  console.info(\`audioCapturer getAudioStreamIdSync: ${streamId}\`);
} catch (err) {
  let error = err as BusinessError;
  console.error(\`ERROR: ${error}\`);
}

#### start8+

start(callback: AsyncCallback<void>): void

Starts this audio capturer to start capturing audio data. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Capturer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | 
Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. If the operation fails, an error object with the following error code is returned:

Error code 6800301: indicates abnormal status, focus preemption failure, and abnormal system processing. For details, see system logs.

 |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

audioCapturer.start((err: BusinessError) => {
  if (err) {
    console.error('Capturer start failed.');
  } else {
    console.info('Capturer start success.');
  }
});

#### start8+

start(): Promise<void>

Starts this audio capturer to start capturing audio data. This API uses a promise to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Capturer

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | 
Promise object, which indicates that the capturer is started successfully. If the operation fails, an error object with the following error code is returned:

Error code 6800301: indicates abnormal status, focus preemption failure, and abnormal system processing. For details, see system logs.

 |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

audioCapturer.start().then(() => {
  console.info('Succeeded in doing start.');
  if (audioCapturer.state == audio.AudioState.STATE\_RUNNING) {
    console.info('AudioFrameworkRecLog: AudioCapturer is in Running State');
  }
}).catch((err: BusinessError) => {
  console.error(\`Failed to start. Code: ${err.code}, message: ${err.message}\`);
});

#### stop8+

stop(callback: AsyncCallback<void>): void

Stops this audio capturer, ceasing the input audio stream. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Capturer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

audioCapturer.stop((err: BusinessError) => {
  if (err) {
    console.error('Capturer stop failed');
  } else {
    console.info('Capturer stopped.');
  }
});

#### stop8+

stop(): Promise<void>

Stops this audio capturer, ceasing the input audio stream. This API uses a promise to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Capturer

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

audioCapturer.stop().then(() => {
  console.info('Succeeded in doing stop.');
  if (audioCapturer.state == audio.AudioState.STATE\_STOPPED){
    console.info('AudioFrameworkRecLog: State is Stopped:');
  }
}).catch((err: BusinessError) => {
  console.error(\`Failed to stop. Code: ${err.code}, message: ${err.message}\`);
});

#### release8+

release(callback: AsyncCallback<void>): void

Releases this audio capturer. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Capturer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

audioCapturer.release((err: BusinessError) => {
  if (err) {
    console.error('capturer release failed');
  } else {
    console.info('capturer released.');
  }
});

#### release8+

release(): Promise<void>

Releases this audio capturer. This API uses a promise to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Capturer

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

audioCapturer.release().then(() => {
  console.info('AudioFrameworkRecLog: ---------RELEASE RECORD---------');
  console.info('AudioFrameworkRecLog: Capturer release : SUCCESS');
  console.info(\`AudioFrameworkRecLog: AudioCapturer : STATE : ${audioCapturer.state}\`);
}).catch((err: BusinessError) => {
  console.error(\`AudioFrameworkRecLog: Capturer stop: ERROR: ${err}\`);
});

#### getAudioTime8+

getAudioTime(callback: AsyncCallback<number>): void

Obtains the timestamp of the current recording position, measured in nanoseconds from the Unix epoch (January 1, 1970). This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Capturer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<number> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the number of nanoseconds obtained; otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

audioCapturer.getAudioTime((err: BusinessError, timestamp: number) => {
  console.info(\`Current timestamp: ${timestamp}\`);
});

#### getAudioTime8+

getAudioTime(): Promise<number>

Obtains the timestamp of the current recording position, measured in nanoseconds from the Unix epoch (January 1, 1970). This API uses a promise to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Capturer

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the number of nanoseconds elapsed from the Unix epoch. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

audioCapturer.getAudioTime().then((audioTime: number) => {
  console.info(\`AudioFrameworkRecLog: AudioCapturer getAudioTime : Success ${audioTime}\`);
}).catch((err: BusinessError) => {
  console.error(\`AudioFrameworkRecLog: AudioCapturer Created : ERROR : ${err}\`);
});

#### getAudioTimeSync10+

getAudioTimeSync(): number

Obtains the timestamp of the current recording position, measured in nanoseconds from the Unix epoch (January 1, 1970). This API returns the result synchronously.

**System capability**: SystemCapability.Multimedia.Audio.Capturer

**Return value**

| Type | Description |
| :-- | :-- |
| number | Timestamp. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let audioTime: number = audioCapturer.getAudioTimeSync();
  console.info(\`AudioFrameworkRecLog: AudioCapturer getAudioTimeSync : Success ${audioTime}\`);
} catch (err) {
  let error = err as BusinessError;
  console.error(\`AudioFrameworkRecLog: AudioCapturer getAudioTimeSync : ERROR : ${error}\`);
}

#### getAudioTimestampInfo19+

getAudioTimestampInfo(): Promise<AudioTimestampInfo>

Obtains the timestamp and position information of an input audio stream.

This API obtains the actual recording position (specified by **framePos**) of the audio channel and the timestamp when recording to that position (specified by **timestamp**, in nanoseconds).

**System capability**: SystemCapability.Multimedia.Audio.Capturer

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[AudioTimestampInfo](../interfaces-others/document.md#audiotimestampinfo19)\> | Promise used to return the timestamp and position information. |

**Error codes**

For details about the error codes, see [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6800103 | Operation not permit at current state. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

audioCapturer.getAudioTimestampInfo().then((audioTimestampInfo: audio.AudioTimestampInfo) => {
  console.info(\`Current timestamp: ${audioTimestampInfo.timestamp}\`);
}).catch((err: BusinessError) => {
  console.error(\`ERROR: ${err}\`);
});

#### getAudioTimestampInfoSync19+

getAudioTimestampInfoSync(): AudioTimestampInfo

Obtains the timestamp and position information of an input audio stream. This API returns the result synchronously.

**System capability**: SystemCapability.Multimedia.Audio.Capturer

**Return value**

| Type | Description |
| :-- | :-- |
| [AudioTimestampInfo](../interfaces-others/document.md#audiotimestampinfo19) | Information about the timestamp and position information. |

**Error codes**

For details about the error codes, see [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6800103 | Operation not permit at current state. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let audioTimestampInfo: audio.AudioTimestampInfo = audioCapturer.getAudioTimestampInfoSync();
  console.info(\`Current timestamp: ${audioTimestampInfo.timestamp}\`);
} catch (err) {
  let error = err as BusinessError;
  console.error(\`ERROR: ${error}\`);
}

#### getBufferSize8+

getBufferSize(callback: AsyncCallback<number>): void

Obtains a reasonable minimum buffer size in bytes for capturing. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Capturer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<number> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the minimum buffer size obtained; otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

audioCapturer.getBufferSize((err: BusinessError, bufferSize: number) => {
  if (err) {
    console.error(\`Failed to get buffer size. Code: ${err.code}, message: ${err.message}\`);
  } else {
    console.info(\`Succeeded in getting buffer size, BufferSize: ${bufferSize}.\`);
  }
});

#### getBufferSize8+

getBufferSize(): Promise<number>

Obtains a reasonable minimum buffer size in bytes for capturing. This API uses a promise to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Capturer

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the buffer size. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

audioCapturer.getBufferSize().then((bufferSize: number) => {
  console.info(\`Succeeded in getting buffer size, BufferSize: ${bufferSize}.\`);
}).catch((err: BusinessError) => {
  console.error(\`Failed to get buffer size. Code: ${err.code}, message: ${err.message}\`);
});

#### getBufferSizeSync10+

getBufferSizeSync(): number

Obtains a reasonable minimum buffer size in bytes for capturing. This API returns the result synchronously.

**System capability**: SystemCapability.Multimedia.Audio.Capturer

**Return value**

| Type | Description |
| :-- | :-- |
| number | Buffer size. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let bufferSize = audioCapturer.getBufferSizeSync();
  console.info(\`Succeeded in getting buffer size, BufferSize: ${bufferSize}.\`);
} catch (err) {
  let error = err as BusinessError;
  console.error(\`Failed to get buffer size. Code: ${error.code}, message: ${error.message}\`);
}

#### getCurrentInputDevices11+

getCurrentInputDevices(): AudioDeviceDescriptors

Obtains the information of the current input devices. This API returns the result synchronously.

**System capability**: SystemCapability.Multimedia.Audio.Device

**Return value**

| Type | Description |
| :-- | :-- |
| [AudioDeviceDescriptors](../types/document.md#audiodevicedescriptors) | An array of the audio device descriptors. |

**Example**

let deviceDescriptors: audio.AudioDeviceDescriptors = audioCapturer.getCurrentInputDevices();
console.info(\`Device id: ${deviceDescriptors\[0\].id}\`);
console.info(\`Device type: ${deviceDescriptors\[0\].deviceType}\`);
console.info(\`Device role: ${deviceDescriptors\[0\].deviceRole}\`);
console.info(\`Device name: ${deviceDescriptors\[0\].name}\`);
console.info(\`Device address: ${deviceDescriptors\[0\].address}\`);
console.info(\`Device samplerates: ${deviceDescriptors\[0\].sampleRates\[0\]}\`);
console.info(\`Device channelcounts: ${deviceDescriptors\[0\].channelCounts\[0\]}\`);
console.info(\`Device channelmask: ${deviceDescriptors\[0\].channelMasks\[0\]}\`);
if (deviceDescriptors\[0\].encodingTypes) {
  console.info(\`Device encodingTypes: ${deviceDescriptors\[0\].encodingTypes\[0\]}\`);
}

#### getCurrentAudioCapturerChangeInfo11+

getCurrentAudioCapturerChangeInfo(): AudioCapturerChangeInfo

Obtains the configuration changes of the current audio capturer. This API returns the result synchronously.

**System capability**: SystemCapability.Multimedia.Audio.Device

**Return value**

| Type | Description |
| :-- | :-- |
| [AudioCapturerChangeInfo](../interfaces-others/document.md#audiocapturerchangeinfo9) | Configuration changes of the audio capturer. |

**Example**

let info: audio.AudioCapturerChangeInfo = audioCapturer.getCurrentAudioCapturerChangeInfo();
console.info(\`Info streamId: ${info.streamId}\`);
console.info(\`Info source: ${info.capturerInfo.source}\`);
console.info(\`Info capturerFlags: ${info.capturerInfo.capturerFlags}\`);
console.info(\`Info muted: ${info.muted}\`);
console.info(\`Info type: ${info.deviceDescriptors\[0\].deviceType}\`);
console.info(\`Info role: ${info.deviceDescriptors\[0\].deviceRole}\`);
console.info(\`Info name: ${info.deviceDescriptors\[0\].name}\`);
console.info(\`Info address: ${info.deviceDescriptors\[0\].address}\`);
console.info(\`Info samplerates: ${info.deviceDescriptors\[0\].sampleRates\[0\]}\`);
console.info(\`Info channelcounts: ${info.deviceDescriptors\[0\].channelCounts\[0\]}\`);
console.info(\`Info channelmask: ${info.deviceDescriptors\[0\].channelMasks\[0\]}\`);
if (info.deviceDescriptors\[0\].encodingTypes) {
  console.info(\`Device encodingTypes: ${info.deviceDescriptors\[0\].encodingTypes\[0\]}\`);
}

#### on('audioInterrupt')10+

on(type: 'audioInterrupt', callback: Callback<InterruptEvent>): void

Subscribes to the audio interruption event, which is triggered when the audio focus is changed. This API uses an asynchronous callback to return the result.

The AudioCapturer instance proactively gains the focus when the **start** event occurs and releases the focus when the **pause** or **stop** event occurs. Therefore, you do not need to request to gain or release the focus.

After this API is called, an [InterruptEvent](../interfaces-others/document.md#interruptevent9) is received when the AudioCapturer instance fails to obtain the focus or an audio interruption event occurs (for example, the audio stream is interrupted by others). It is recommended that the application perform further processing based on the **InterruptEvent** information. For details, see [Introduction to Audio Focus](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/audio-playback-concurrency).

**System capability**: SystemCapability.Multimedia.Audio.Interrupt

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'audioInterrupt'** is triggered when the audio focus is changed. |
| callback | Callback<[InterruptEvent](../interfaces-others/document.md#interruptevent9)\> | Yes | Callback used to return the event information. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |

**Example**

import { audio } from '@kit.AudioKit';

let isCapturing: boolean = false; // An identifier specifying whether capturing is in progress.

audioCapturer.on('audioInterrupt', (interruptEvent: audio.InterruptEvent) => {
  // When an audio interruption event occurs, the AudioCapturer receives the interruptEvent callback and performs processing based on the content in the callback.
  // 1. (Optional) The AudioRenderer reads the value of interruptEvent.forceType to see whether the system has forcibly performed the operation.
  // Note: In the default focus strategy, INTERRUPT\_HINT\_RESUME maps to the force type INTERRUPT\_SHARE, and others map to INTERRUPT\_FORCE. Therefore, the value of forceType does not need to be checked.
  // 2. (Mandatory) The AudioRenderer then reads the value of interruptEvent.hintType and performs corresponding processing.
  if (interruptEvent.forceType == audio.InterruptForceType.INTERRUPT\_FORCE) {
    // The audio focus event has been forcibly executed by the system. The application needs to update its status and displayed content.
    switch (interruptEvent.hintType) {
      case audio.InterruptHint.INTERRUPT\_HINT\_PAUSE:
        // The audio stream has been paused and temporarily loses the focus. It will receive the interruptEvent corresponding to resume when it is able to regain the focus.
        console.info('Force paused. Update capturing status and stop reading');
        isCapturing = false; // A simplified processing indicating several operations for switching the application to the paused state.
        break;
      case audio.InterruptHint.INTERRUPT\_HINT\_STOP:
        // The audio stream has been stopped and permanently loses the focus. The user must manually trigger the operation to resume capturing.
        console.info('Force stopped. Update capturing status and stop reading');
        isCapturing = false; // A simplified processing indicating several operations for switching the application to the paused state.
        break;
      default:
        console.info('Invalid interruptEvent');
        break;
    }
  } else if (interruptEvent.forceType == audio.InterruptForceType.INTERRUPT\_SHARE) {
    // The audio focus event needs to be operated by the application, which can choose the processing mode. It is recommended that the application process the event according to the value of InterruptHint.
    switch (interruptEvent.hintType) {
      case audio.InterruptHint.INTERRUPT\_HINT\_RESUME:
        // It is recommended that the application continue capturing. (The audio stream has been forcibly paused and temporarily lost the focus. It can resume capturing now.)
        // The INTERRUPT\_HINT\_RESUME operation must be proactively executed by the application and cannot be forcibly executed by the system. Therefore, the INTERRUPT\_HINT\_RESUME event must map to INTERRUPT\_SHARE.
        console.info('Resume force paused renderer or ignore');
        // To continue capturing, the application must perform the required operations.
        break;
      default:
        console.info('Invalid interruptEvent');
        break;
    }
  }
});

#### off('audioInterrupt')10+

off(type: 'audioInterrupt'): void

Unsubscribes from the audio interruption event.

**System capability**: SystemCapability.Multimedia.Audio.Interrupt

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'audioInterrupt'** is triggered when the audio focus is changed. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |

**Example**

audioCapturer.off('audioInterrupt');

#### on('inputDeviceChange')11+

on(type: 'inputDeviceChange', callback: Callback<AudioDeviceDescriptors>): void

Subscribes to the audio input device change event, which is triggered when an audio input device is changed. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Device

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'inputDeviceChange'** is triggered when an audio input device is changed. |
| callback | Callback<[AudioDeviceDescriptors](../types/document.md#audiodevicedescriptors) > | Yes | Callback used to return the updated information about the audio input device. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |

**Example**

audioCapturer.on('inputDeviceChange', (deviceChangeInfo: audio.AudioDeviceDescriptors) => {
  console.info(\`inputDevice id: ${deviceChangeInfo\[0\].id}\`);
  console.info(\`inputDevice deviceRole: ${deviceChangeInfo\[0\].deviceRole}\`);
  console.info(\`inputDevice deviceType: ${deviceChangeInfo\[0\].deviceType}\`);
});

#### off('inputDeviceChange')11+

off(type: 'inputDeviceChange', callback?: Callback<AudioDeviceDescriptors>): void

Unsubscribes from the audio input device change event. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Device

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'inputDeviceChange'** is triggered when an audio input device is changed. |
| callback | Callback<[AudioDeviceDescriptors](../types/document.md#audiodevicedescriptors) > | No | Callback used to return the information about the audio input device. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |

**Example**

// Cancel all subscriptions to the event.
audioCapturer.off('inputDeviceChange');

// For the same event, if the callback parameter passed to the off API is the same as that passed to the on API, the off API cancels the subscription registered with the specified callback parameter.
let inputDeviceChangeCallback = (deviceChangeInfo: audio.AudioDeviceDescriptors) => {
  console.info(\`inputDevice id: ${deviceChangeInfo\[0\].id}\`);
  console.info(\`inputDevice deviceRole: ${deviceChangeInfo\[0\].deviceRole}\`);
  console.info(\`inputDevice deviceType: ${deviceChangeInfo\[0\].deviceType}\`);
};

audioCapturer.on('inputDeviceChange', inputDeviceChangeCallback);

audioCapturer.off('inputDeviceChange', inputDeviceChangeCallback);

#### on('audioCapturerChange')11+

on(type: 'audioCapturerChange', callback: Callback<AudioCapturerChangeInfo>): void

Subscribes to the audio capturer configuration change event, which is triggered when the audio recording stream status or device is changed. This API uses an asynchronous callback to return the result. The subscription is implemented asynchronously and the callback, which is triggered when the audio capturer configuration changes, may fail to reflect the actual condition.

**System capability**: SystemCapability.Multimedia.Audio.Capturer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'audioCapturerChange'** is triggered when the audio recording stream status or device is changed. |
| callback | Callback<[AudioCapturerChangeInfo](../interfaces-others/document.md#audiocapturerchangeinfo9)\> | Yes | Callback used to return the current configuration and status information of the audio capturer. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |

**Example**

audioCapturer.on('audioCapturerChange', (capturerChangeInfo: audio.AudioCapturerChangeInfo) => {
  console.info(\`Succeeded in using on function, AudioCapturerChangeInfo: ${capturerChangeInfo}.\`);
});

#### off('audioCapturerChange')11+

off(type: 'audioCapturerChange', callback?: Callback<AudioCapturerChangeInfo>): void

Unsubscribes from the audio capturer configuration change event. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Capturer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'audioCapturerChange'** is triggered when the audio capturer configuration is changed. |
| callback | Callback<[AudioCapturerChangeInfo](../interfaces-others/document.md#audiocapturerchangeinfo9)\> | No | Callback used for unsubscription. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |

**Example**

// Cancel all subscriptions to the event.
audioCapturer.off('audioCapturerChange');

// For the same event, if the callback parameter passed to the off API is the same as that passed to the on API, the off API cancels the subscription registered with the specified callback parameter.
let audioCapturerChangeCallback = (capturerChangeInfo: audio.AudioCapturerChangeInfo) => {
  console.info(\`Succeeded in using on or off function, AudioCapturerChangeInfo: ${capturerChangeInfo}.\`);
};

audioCapturer.on('audioCapturerChange', audioCapturerChangeCallback);

audioCapturer.off('audioCapturerChange', audioCapturerChangeCallback);

#### on('markReach')8+

on(type: 'markReach', frame: number, callback: Callback<number>): void

Subscribes to the mark reached event, which is triggered (only once) when the number of frames captured reaches the value of the **frame** parameter. This API uses an asynchronous callback to return the result.

For example, if **frame** is set to **100**, the callback is invoked when the number of captured frames reaches the 100th frame.

**System capability**: SystemCapability.Multimedia.Audio.Capturer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'markReach'** is triggered when the number of frames captured reaches the value of the **frame** parameter. |
| frame | number | Yes | Number of frames to trigger the event. The value must be greater than **0**. |
| callback | Callback<number> | Yes | Callback used to return the value of the **frame** parameter. |

**Example**

audioCapturer.on('markReach', 1000, (position: number) => {
  if (position == 1000) {
    console.info('ON Triggered successfully');
  }
});

#### off('markReach')8+

off(type: 'markReach', callback?: Callback<number>): void

Unsubscribes from the mark reached event. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Capturer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'markReach'** is triggered when the number of frames captured reaches the value of the **frame** parameter. |
| callback18+ | Callback<number> | No | Callback used to return the value of the **frame** parameter. |

**Example**

// Cancel all subscriptions to the event.
audioCapturer.off('markReach');

// For the same event, if the callback parameter passed to the off API is the same as that passed to the on API, the off API cancels the subscription registered with the specified callback parameter.
let markReachCallback = (position: number) => {
  if (position == 1000) {
    console.info('ON Triggered successfully');
  }
};

audioCapturer.on('markReach', 1000, markReachCallback);

audioCapturer.off('markReach', markReachCallback);

#### on('periodReach')8+

on(type: 'periodReach', frame: number, callback: Callback<number>): void

Subscribes to the period reached event, which is triggered each time the number of frames captured reaches the value of the **frame** parameter. In other words, the information is reported periodically. This API uses an asynchronous callback to return the result.

For example, if **frame** is set to **10**, the callback is invoked each time 10 frames are captured, for example, when the number of frames captured reaches the 10th frame, 20th frame, and 30th frame.

**System capability**: SystemCapability.Multimedia.Audio.Capturer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'periodReach'** is triggered each time the number of frames captured reaches the value of the **frame** parameter. |
| frame | number | Yes | Number of frames to trigger the event. The value must be greater than **0**. |
| callback | Callback<number> | Yes | Callback used to return the value of the **frame** parameter. |

**Example**

audioCapturer.on('periodReach', 1000, (position: number) => {
  if (position == 1000) {
    console.info('ON Triggered successfully');
  }
});

#### off('periodReach')8+

off(type: 'periodReach', callback?: Callback<number>): void

Unsubscribes from the period reached event. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Capturer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'periodReach'** is triggered each time the number of frames captured reaches the value of the **frame** parameter. |
| callback18+ | Callback<number> | No | Callback used to return the value of the **frame** parameter. |

**Example**

// Cancel all subscriptions to the event.
audioCapturer.off('periodReach');

// For the same event, if the callback parameter passed to the off API is the same as that passed to the on API, the off API cancels the subscription registered with the specified callback parameter.
let periodReachCallback = (position: number) => {
  if (position == 1000) {
    console.info('ON Triggered successfully');
  }
};

audioCapturer.on('periodReach', 1000, periodReachCallback);

audioCapturer.off('periodReach', periodReachCallback);

#### on('stateChange')8+

on(type: 'stateChange', callback: Callback<AudioState>): void

Subscribes to the audio capturer state change event, which is triggered when the state of the audio capturer is changed. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Capturer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'stateChange'** is triggered when the state of the audio capturer is changed. |
| callback | Callback<[AudioState](../enums/document.md#audiostate8)\> | Yes | Callback used to return the audio status. |

**Example**

audioCapturer.on('stateChange', (state: audio.AudioState) => {
  if (state == 1) {
    console.info('audio capturer state is: STATE\_PREPARED');
  }
  if (state == 2) {
    console.info('audio capturer state is: STATE\_RUNNING');
  }
});

#### off('stateChange')18+

off(type: 'stateChange', callback?: Callback<AudioState>): void

Unsubscribes from the audio capturer state change event. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Capturer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'stateChange'** is triggered when the listening for audio capturer state change event is canceled. |
| callback | Callback<[AudioState](../enums/document.md#audiostate8)\> | No | Callback used to return the audio status. |

**Error codes**

For details about the error codes, see [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6800101 | Parameter verification failed. |

**Example**

// Cancel all subscriptions to the event.
audioCapturer.off('stateChange');

// For the same event, if the callback parameter passed to the off API is the same as that passed to the on API, the off API cancels the subscription registered with the specified callback parameter.
let stateChangeCallback = (state: audio.AudioState) => {
  if (state == 1) {
    console.info('audio renderer state is: STATE\_PREPARED');
  }
  if (state == 2) {
    console.info('audio renderer state is: STATE\_RUNNING');
  }
};

audioCapturer.on('stateChange', stateChangeCallback);

audioCapturer.off('stateChange', stateChangeCallback);

#### on('readData')11+

on(type: 'readData', callback: Callback<ArrayBuffer>): void

Subscribes to the audio data read event, which is triggered when audio stream data needs to be read. This API uses an asynchronous callback to return the result.

The callback function is used only to read audio data. Do not call AudioCapturer APIs in it.

**System capability**: SystemCapability.Multimedia.Audio.Capturer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'readData'** is triggered when audio stream data needs to be read. |
| callback | Callback<ArrayBuffer> | Yes | Callback used to return the buffer from which the data is read. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo as fs } from '@kit.CoreFileKit';
import { common } from '@kit.AbilityKit';

class Options {
  offset?: number;
  length?: number;
}

let bufferSize: number = 0;
// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let path = context.cacheDir;
let filePath = path + '/StarWars10s-2C-48000-4SW.pcm';
let file: fs.File = fs.openSync(filePath, fs.OpenMode.READ\_WRITE | fs.OpenMode.CREATE);
let readDataCallback = (buffer: ArrayBuffer) => {
  let options: Options = {
    offset: bufferSize,
    length: buffer.byteLength
  };
  fs.writeSync(file.fd, buffer, options);
  bufferSize += buffer.byteLength;
}

audioCapturer.on('readData', readDataCallback);

audioCapturer.start((err: BusinessError) => {
  if (err) {
    console.error('Capturer start failed.');
  } else {
    console.info('Capturer start success.');
  }
});

#### off('readData')11+

off(type: 'readData', callback?: Callback<ArrayBuffer>): void

Unsubscribes from the audio data read event. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Capturer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'readData'** is triggered when audio stream data needs to be read. |
| callback | Callback<ArrayBuffer> | No | Callback used to return the buffer from which the data is read. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |

**Example**

// Cancel all subscriptions to the event.
audioCapturer.off('readData');

// For the same event, if the callback parameter passed to the off API is the same as that passed to the on API, the off API cancels the subscription registered with the specified callback parameter.
let readDataCallback = (data: ArrayBuffer) => {
    console.info(\`read data: ${data}\`);
};

audioCapturer.on('readData', readDataCallback);

audioCapturer.off('readData', readDataCallback);

#### getOverflowCount12+

getOverflowCount(): Promise<number>

Obtains the number of overflow audio frames in the audio stream that is being captured. This API uses a promise to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Capturer

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the number of overflow audio frames. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

audioCapturer.getOverflowCount().then((value: number) => {
  console.info(\`Get overflow count Success! ${value}\`);
}).catch((err: BusinessError) => {
  console.error(\`Get overflow count Fail: ${err}\`);
});

#### getOverflowCountSync12+

getOverflowCountSync(): number

Obtains the number of overflow audio frames in the audio stream that is being captured. This API returns the result synchronously.

**System capability**: SystemCapability.Multimedia.Audio.Capturer

**Return value**

| Type | Description |
| :-- | :-- |
| number | Number of overflow audio frames. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let value: number = audioCapturer.getOverflowCountSync();
  console.info(\`Get overflow count Success! ${value}\`);
} catch (err) {
  let error = err as BusinessError;
  console.error(\`Get overflow count Fail: ${error}\`);
}

#### setWillMuteWhenInterrupted20+

setWillMuteWhenInterrupted(muteWhenInterrupted: boolean): Promise<void>

Sets whether to [mute the current audio recording stream when an audio interruption occurs](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/using-audiocapturer-for-recording#setting-the-mute-interruption-mode). This API uses a promise to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Capturer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| muteWhenInterrupted | boolean | Yes | Whether to mute the current audio recording stream during an audio interruption. **true** to mute, **false** otherwise. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6800103 | Operation not permitted at current state. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

audioCapturer.setWillMuteWhenInterrupted(true).then(() => {
  console.info('setWillMuteWhenInterrupted Success!');
}).catch((err: BusinessError) => {
  console.error(\`setWillMuteWhenInterrupted Fail: ${err}\`);
});

#### read(deprecated)

read(size: number, isBlockingRead: boolean, callback: AsyncCallback<ArrayBuffer>): void

Reads the buffer. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/UaDBc8A9S0i0V_is_2yH2g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062417Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2D8A31E8FD84855205975D2608FAC3D125117C838F83D64F468B2CFC5AD5C7DC)

This API is supported since API version 8 and deprecated since API version 11. You are advised to use [on('readData')](#onreaddata11) instead.

**System capability**: SystemCapability.Multimedia.Audio.Capturer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| size | number | Yes | Number of bytes to read. |
| isBlockingRead | boolean | Yes | Whether to block the read operation. **true** to block, **false** otherwise. |
| callback | AsyncCallback<ArrayBuffer> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the buffer read; otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

audioCapturer.getBufferSize().then((bufferSize: number) => {
  console.info('Succeeded in doing getBufferSize.');
  audioCapturer.read(bufferSize, true, (err: BusinessError, buffer: ArrayBuffer) => {
    if (err) {
      console.error(\`Failed to read. Code: ${err.code}, message: ${err.message}\`);
      return;
    }
    console.info('Succeeded in doing read.');
  });
}).catch((err: BusinessError) => {
  console.error(\`Failed to getBufferSize. Code: ${err.code}, message: ${err.message}\`);
});

#### read(deprecated)

read(size: number, isBlockingRead: boolean): Promise<ArrayBuffer>

Reads the buffer. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/SaQcSULgRXC_X-PeZvroxA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062417Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EC8F221E9EA5C7F878CB5AEFD9A63810890EA63F0B32132E8C6B85BC354F9F45)

This API is supported since API version 8 and deprecated since API version 11. You are advised to use [on('readData')](#onreaddata11) instead.

**System capability**: SystemCapability.Multimedia.Audio.Capturer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| size | number | Yes | Number of bytes to read. |
| isBlockingRead | boolean | Yes | Whether to block the read operation. **true** to block, **false** otherwise. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<ArrayBuffer> | Promise used to return the data read from the buffer. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

audioCapturer.getBufferSize().then((bufferSize: number) => {
  console.info('Succeeded in doing getBufferSize.');
  audioCapturer.read(bufferSize, true).then((buffer: ArrayBuffer) => {
    console.info('Succeeded in doing read.');
  }).catch((err: BusinessError) => {
    console.error(\`Failed to read. Code: ${err.code}, message: ${err.message}\`);
  });
}).catch((err: BusinessError) => {
  console.error(\`Failed to getBufferSize. Code: ${err.code}, message: ${err.message}\`);
});
