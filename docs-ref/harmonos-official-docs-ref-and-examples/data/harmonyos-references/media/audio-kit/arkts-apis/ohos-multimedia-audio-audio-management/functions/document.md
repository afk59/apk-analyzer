# Functions

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/3b4DS6pDQbOqAhSG3ZohmA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062417Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A43CBD104BC2A29EC5BFB157511A181F0E0318456ADE4BCC8B2E53274E51723B)

The initial APIs of this module are supported since API version 7. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { audio } from '@kit.AudioKit';

#### audio.getAudioManager

getAudioManager(): AudioManager

Obtains an AudioManager instance.

**System capability**: SystemCapability.Multimedia.Audio.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [AudioManager](../interface-audiomanager/document.md) | AudioManager instance. |

**Example**

import { audio } from '@kit.AudioKit';

let audioManager = audio.getAudioManager();

#### audio.createAudioRenderer8+

createAudioRenderer(options: AudioRendererOptions, callback: AsyncCallback<AudioRenderer>): void

Creates an AudioRenderer instance. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Renderer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [AudioRendererOptions](../interfaces-others/document.md#audiorendereroptions8) | Yes | Renderer configurations. |
| callback | AsyncCallback<[AudioRenderer](../interface-audiorenderer/document.md)\> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the AudioRenderer instance obtained; otherwise, **err** is an error object. |

**Example**

import { audio } from '@kit.AudioKit';

let audioStreamInfo: audio.AudioStreamInfo = {
  samplingRate: audio.AudioSamplingRate.SAMPLE\_RATE\_48000, // Sampling rate.
  channels: audio.AudioChannel.CHANNEL\_2, // Channel.
  sampleFormat: audio.AudioSampleFormat.SAMPLE\_FORMAT\_S16LE, // Sampling format.
  encodingType: audio.AudioEncodingType.ENCODING\_TYPE\_RAW // Encoding format.
};

let audioRendererInfo: audio.AudioRendererInfo = {
  usage: audio.StreamUsage.STREAM\_USAGE\_MUSIC, // Audio stream usage type: music. Set this parameter based on the service scenario.
  rendererFlags: 0 // AudioRenderer flag.
};

let audioRendererOptions: audio.AudioRendererOptions = {
  streamInfo: audioStreamInfo,
  rendererInfo: audioRendererInfo
};

let audioRenderer: audio.AudioRenderer;

audio.createAudioRenderer(audioRendererOptions,(err, data) => {
  if (err) {
    console.error(\`AudioRenderer Created: Error: ${err}\`);
  } else {
    console.info('AudioRenderer Created: SUCCESS');
    audioRenderer = data;
  }
});

#### audio.createAudioRenderer8+

createAudioRenderer(options: AudioRendererOptions): Promise<AudioRenderer>

Creates an AudioRenderer instance. This API uses a promise to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Renderer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [AudioRendererOptions](../interfaces-others/document.md#audiorendereroptions8) | Yes | Renderer configurations. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[AudioRenderer](../interface-audiorenderer/document.md)\> | Promise used to return the AudioRenderer instance. |

**Example**

import { audio } from '@kit.AudioKit';
import { BusinessError } from '@kit.BasicServicesKit';

let audioStreamInfo: audio.AudioStreamInfo = {
  samplingRate: audio.AudioSamplingRate.SAMPLE\_RATE\_48000, // Sampling rate.
  channels: audio.AudioChannel.CHANNEL\_2, // Channel.
  sampleFormat: audio.AudioSampleFormat.SAMPLE\_FORMAT\_S16LE, // Sampling format.
  encodingType: audio.AudioEncodingType.ENCODING\_TYPE\_RAW // Encoding format.
};

let audioRendererInfo: audio.AudioRendererInfo = {
  usage: audio.StreamUsage.STREAM\_USAGE\_MUSIC, // Audio stream usage type: music. Set this parameter based on the service scenario.
  rendererFlags: 0 // AudioRenderer flag.
};

let audioRendererOptions: audio.AudioRendererOptions = {
  streamInfo: audioStreamInfo,
  rendererInfo: audioRendererInfo
};

let audioRenderer: audio.AudioRenderer;

audio.createAudioRenderer(audioRendererOptions).then((data) => {
  audioRenderer = data;
  console.info('AudioFrameworkRenderLog: AudioRenderer Created : SUCCESS');
}).catch((err: BusinessError) => {
  console.error(\`AudioFrameworkRenderLog: AudioRenderer Created : ERROR : ${err}\`);
});

#### audio.createAudioCapturer8+

createAudioCapturer(options: AudioCapturerOptions, callback: AsyncCallback<AudioCapturer>): void

Creates an AudioCapturer instance. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Capturer

**Required permissions**: ohos.permission.MICROPHONE

This permission is required when [SourceType](../enums/document.md#sourcetype8) is set to **SOURCE\_TYPE\_MIC**, **SOURCE\_TYPE\_VOICE\_RECOGNITION**, **SOURCE\_TYPE\_VOICE\_COMMUNICATION**, **SOURCE\_TYPE\_VOICE\_MESSAGE**, or **SOURCE\_TYPE\_CAMCORDER**.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [AudioCapturerOptions](../interfaces-others/document.md#audiocaptureroptions8) | Yes | Capturer configurations. |
| callback | AsyncCallback<[AudioCapturer](../interface-audiocapturer/document.md)\> | Yes | 
Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the AudioCapturer instance obtained; otherwise, **err** is an error object. If the operation fails, an error object with one of the following error codes is returned:

Error code 6800301: indicates a parameter verification exception, permission verification exception, or system processing exception. For details, see system logs.

Error code 6800101: indicates that a mandatory parameter is null or the parameter type is incorrect.

 |

**Example**

import { audio } from '@kit.AudioKit';

let audioStreamInfo: audio.AudioStreamInfo = {
  samplingRate: audio.AudioSamplingRate.SAMPLE\_RATE\_48000, // Sampling rate.
  channels: audio.AudioChannel.CHANNEL\_2, // Channel.
  sampleFormat: audio.AudioSampleFormat.SAMPLE\_FORMAT\_S16LE, // Sampling format.
  encodingType: audio.AudioEncodingType.ENCODING\_TYPE\_RAW // Encoding format.
};

let audioCapturerInfo: audio.AudioCapturerInfo = {
  source: audio.SourceType.SOURCE\_TYPE\_MIC, // Audio source type: microphone. Set this parameter based on the service scenario.
  capturerFlags: 0 // AudioCapturer flag.
};

let audioCapturerOptions: audio.AudioCapturerOptions = {
  streamInfo: audioStreamInfo,
  capturerInfo: audioCapturerInfo
};

let audioCapturer: audio.AudioCapturer;

audio.createAudioCapturer(audioCapturerOptions, (err, data) => {
  if (err) {
    console.error(\`AudioCapturer Created : Error: ${err}\`);
  } else {
    console.info('AudioCapturer Created : SUCCESS');
    audioCapturer = data;
  }
});

#### audio.createAudioCapturer8+

createAudioCapturer(options: AudioCapturerOptions): Promise<AudioCapturer>

Creates an AudioCapturer instance. This API uses a promise to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Capturer

**Required permissions**: ohos.permission.MICROPHONE

This permission is required when [SourceType](../enums/document.md#sourcetype8) is set to **SOURCE\_TYPE\_MIC**, **SOURCE\_TYPE\_VOICE\_RECOGNITION**, **SOURCE\_TYPE\_VOICE\_COMMUNICATION**, **SOURCE\_TYPE\_VOICE\_MESSAGE**, or **SOURCE\_TYPE\_CAMCORDER**.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [AudioCapturerOptions](../interfaces-others/document.md#audiocaptureroptions8) | Yes | Capturer configurations. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[AudioCapturer](../interface-audiocapturer/document.md)\> | 
Promise used to return the result. If the operation is successful, an AudioCapturer instance is returned; otherwise, an error object with either of the following error codes is returned:

Error code 6800301: indicates a parameter verification exception, permission verification exception, or system processing exception. For details, see system logs.

Error code 6800101: indicates that a mandatory parameter is null or the parameter type is incorrect.

 |

**Example**

import { audio } from '@kit.AudioKit';
import { BusinessError } from '@kit.BasicServicesKit';

let audioStreamInfo: audio.AudioStreamInfo = {
  samplingRate: audio.AudioSamplingRate.SAMPLE\_RATE\_48000, // Sampling rate.
  channels: audio.AudioChannel.CHANNEL\_2, // Channel.
  sampleFormat: audio.AudioSampleFormat.SAMPLE\_FORMAT\_S16LE, // Sampling format.
  encodingType: audio.AudioEncodingType.ENCODING\_TYPE\_RAW // Encoding format.
};

let audioCapturerInfo: audio.AudioCapturerInfo = {
  source: audio.SourceType.SOURCE\_TYPE\_MIC, // Audio source type: microphone. Set this parameter based on the service scenario.
  capturerFlags: 0 // AudioCapturer flag.
};

let audioCapturerOptions:audio.AudioCapturerOptions = {
  streamInfo: audioStreamInfo,
  capturerInfo: audioCapturerInfo
};

let audioCapturer: audio.AudioCapturer;

audio.createAudioCapturer(audioCapturerOptions).then((data) => {
  audioCapturer = data;
  console.info('AudioCapturer Created : SUCCESS');
}).catch((err: BusinessError) => {
  console.error(\`AudioCapturer Created : ERROR : ${err}\`);
});

#### audio.createAudioLoopback20+

createAudioLoopback(mode: AudioLoopbackMode): Promise<AudioLoopback>

Creates an AudioLoopback instance. This API uses a promise to return the result.

Before using **createAudioLoopback**, call [isAudioLoopbackSupported](../interface-audiostreammanager/document.md#isaudioloopbacksupported20) to check whether the system supports the audio loopback mode.

**System capability**: SystemCapability.Multimedia.Audio.Capturer

**Required permissions**: ohos.permission.MICROPHONE

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| mode | [AudioLoopbackMode](../enums/document.md#audioloopbackmode20) | Yes | Audio loopback mode. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[AudioLoopback](../interface-audioloopback/document.md)\> | Promise used to return the result. If the operation is successful, an AudioLoopback instance is returned; otherwise, an error object is returned. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Unsupported API. |
| 6800101 | Parameter verification failed. |
| 6800104 | Loopback mode is unsupported. |

**Example**

import { audio } from '@kit.AudioKit';
import { BusinessError } from '@kit.BasicServicesKit';

let audioLoopback: audio.AudioLoopback;

audio.createAudioLoopback(audio.AudioLoopbackMode.HARDWARE).then((data) => {
  audioLoopback = data;
  console.info('AudioLoopback Created : SUCCESS');
}).catch((err: BusinessError) => {
  console.error(\`AudioLoopback Created : ERROR : ${err}\`);
});
