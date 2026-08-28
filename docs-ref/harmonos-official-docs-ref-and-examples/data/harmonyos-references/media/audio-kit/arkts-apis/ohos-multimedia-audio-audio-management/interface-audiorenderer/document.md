# Interface (AudioRenderer)

This interface provides APIs for audio rendering.

Before calling any API in AudioRenderer, you must use [createAudioRenderer](../functions/document.md#audiocreateaudiorenderer8) to create an AudioRenderer instance.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/WCoeqO4GT2aG0_PNxfZwRg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062417Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C6FEA23947E04CC2DF4E610D34FD24336824120AAE6C9E89537C8E66B2358DD7)

-   The initial APIs of this module are supported since API version 7. Newly added APIs will be marked with a superscript to indicate their earliest API version.
-   The initial APIs of this interface are supported since API version 8.

#### Modules to Import

import { audio } from '@kit.AudioKit';

#### Properties

**System capability**: SystemCapability.Multimedia.Audio.Renderer

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| state8+ | [AudioState](../enums/document.md#audiostate8) | Yes | No | Audio renderer state. |

**Example**

import { audio } from '@kit.AudioKit';

let state: audio.AudioState = audioRenderer.state;

#### getRendererInfo8+

getRendererInfo(callback: AsyncCallback<AudioRendererInfo>): void

Obtains the information about this audio renderer. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Renderer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[AudioRendererInfo](../interfaces-others/document.md#audiorendererinfo8)\> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the audio renderer information obtained; otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.getRendererInfo((err: BusinessError, audioRendererInfo: audio.AudioRendererInfo) => {
  if (err) {
    console.error(\`Failed to get renderer info. Code: ${err.code}, message: ${err.message}\`);
  } else {
    console.info(\`Succeeded in getting renderer info, AudioRendererInfo: ${JSON.stringify(audioRendererInfo)}.\`);
  }
});

#### getRendererInfo8+

getRendererInfo(): Promise<AudioRendererInfo>

Obtains the information about this audio renderer. This API uses a promise to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Renderer

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[AudioRendererInfo](../interfaces-others/document.md#audiorendererinfo8)\> | Promise used to return the audio renderer information. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.getRendererInfo().then((audioRendererInfo: audio.AudioRendererInfo) => {
  console.info(\`Succeeded in getting renderer info, AudioRendererInfo: ${JSON.stringify(audioRendererInfo)}.\`);
}).catch((err: BusinessError) => {
  console.error(\`Failed to get renderer info. Code: ${err.code}, message: ${err.message}\`);
});

#### getRendererInfoSync10+

getRendererInfoSync(): AudioRendererInfo

Obtains the information about this audio renderer. This API returns the result synchronously.

**System capability**: SystemCapability.Multimedia.Audio.Renderer

**Return value**

| Type | Description |
| :-- | :-- |
| [AudioRendererInfo](../interfaces-others/document.md#audiorendererinfo8) | Audio renderer information. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let audioRendererInfo = audioRenderer.getRendererInfoSync();
  console.info(\`Succeeded in getting renderer info, AudioRendererInfo: ${JSON.stringify(audioRendererInfo)}.\`);
} catch (err) {
  let error = err as BusinessError;
  console.error(\`Failed to get renderer info. Code: ${error.code}, message: ${error.message}\`);
}

#### getStreamInfo8+

getStreamInfo(callback: AsyncCallback<AudioStreamInfo>): void

Obtains the stream information of this audio renderer. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Renderer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[AudioStreamInfo](../interfaces-others/document.md#audiostreaminfo8)\> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the stream information obtained; otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.getStreamInfo((err: BusinessError, streamInfo: audio.AudioStreamInfo) => {
  console.info('Renderer GetStreamInfo:');
  console.info(\`Renderer sampling rate: ${streamInfo.samplingRate}\`);
  console.info(\`Renderer channel: ${streamInfo.channels}\`);
  console.info(\`Renderer format: ${streamInfo.sampleFormat}\`);
  console.info(\`Renderer encoding type: ${streamInfo.encodingType}\`);
});

#### getStreamInfo8+

getStreamInfo(): Promise<AudioStreamInfo>

Obtains the stream information of this audio renderer. This API uses a promise to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Renderer

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[AudioStreamInfo](../interfaces-others/document.md#audiostreaminfo8)\> | Promise used to return the stream information. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.getStreamInfo().then((streamInfo: audio.AudioStreamInfo) => {
  console.info('Renderer GetStreamInfo:');
  console.info(\`Renderer sampling rate: ${streamInfo.samplingRate}\`);
  console.info(\`Renderer channel: ${streamInfo.channels}\`);
  console.info(\`Renderer format: ${streamInfo.sampleFormat}\`);
  console.info(\`Renderer encoding type: ${streamInfo.encodingType}\`);
}).catch((err: BusinessError) => {
  console.error(\`ERROR: ${err}\`);
});

#### getStreamInfoSync10+

getStreamInfoSync(): AudioStreamInfo

Obtains the stream information of this audio renderer. This API returns the result synchronously.

**System capability**: SystemCapability.Multimedia.Audio.Renderer

**Return value**

| Type | Description |
| :-- | :-- |
| [AudioStreamInfo](../interfaces-others/document.md#audiostreaminfo8) | Stream information. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let streamInfo: audio.AudioStreamInfo = audioRenderer.getStreamInfoSync();
  console.info(\`Renderer sampling rate: ${streamInfo.samplingRate}\`);
  console.info(\`Renderer channel: ${streamInfo.channels}\`);
  console.info(\`Renderer format: ${streamInfo.sampleFormat}\`);
  console.info(\`Renderer encoding type: ${streamInfo.encodingType}\`);
} catch (err) {
  let error = err as BusinessError;
  console.error(\`ERROR: ${error}\`);
}

#### getAudioStreamId9+

getAudioStreamId(callback: AsyncCallback<number>): void

Obtains the stream ID of this audio renderer. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Renderer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<number> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the stream ID obtained; otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.getAudioStreamId((err: BusinessError, streamId: number) => {
  console.info(\`Renderer GetStreamId: ${streamId}\`);
});

#### getAudioStreamId9+

getAudioStreamId(): Promise<number>

Obtains the stream ID of this audio renderer. This API uses a promise to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Renderer

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the stream ID. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.getAudioStreamId().then((streamId: number) => {
  console.info(\`Renderer getAudioStreamId: ${streamId}\`);
}).catch((err: BusinessError) => {
  console.error(\`ERROR: ${err}\`);
});

#### getAudioStreamIdSync10+

getAudioStreamIdSync(): number

Obtains the stream ID of this audio renderer. This API returns the result synchronously.

**System capability**: SystemCapability.Multimedia.Audio.Renderer

**Return value**

| Type | Description |
| :-- | :-- |
| number | Stream ID. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let streamId: number = audioRenderer.getAudioStreamIdSync();
  console.info(\`Renderer getAudioStreamIdSync: ${streamId}\`);
} catch (err) {
  let error = err as BusinessError;
  console.error(\`ERROR: ${error}\`);
}

#### setAudioEffectMode10+

setAudioEffectMode(mode: AudioEffectMode, callback: AsyncCallback<void>): void

Sets an audio effect mode. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Renderer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| mode | [AudioEffectMode](../enums/document.md#audioeffectmode10) | Yes | Audio effect mode to set. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. Return by callback. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.setAudioEffectMode(audio.AudioEffectMode.EFFECT\_DEFAULT, (err: BusinessError) => {
  if (err) {
    console.error('Failed to set params');
  } else {
    console.info('Callback invoked to indicate a successful audio effect mode setting.');
  }
});

#### setAudioEffectMode10+

setAudioEffectMode(mode: AudioEffectMode): Promise<void>

Sets an audio effect mode. This API uses a promise to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Renderer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| mode | [AudioEffectMode](../enums/document.md#audioeffectmode10) | Yes | Audio effect mode to set. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. Return by promise. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.setAudioEffectMode(audio.AudioEffectMode.EFFECT\_DEFAULT).then(() => {
  console.info('setAudioEffectMode SUCCESS');
}).catch((err: BusinessError) => {
  console.error(\`ERROR: ${err}\`);
});

#### getAudioEffectMode10+

getAudioEffectMode(callback: AsyncCallback<AudioEffectMode>): void

Obtains the audio effect mode in use. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Renderer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[AudioEffectMode](../enums/document.md#audioeffectmode10)\> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the audio effect mode obtained; otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.getAudioEffectMode((err: BusinessError, effectMode: audio.AudioEffectMode) => {
  if (err) {
    console.error('Failed to get params');
  } else {
    console.info(\`getAudioEffectMode: ${effectMode}\`);
  }
});

#### getAudioEffectMode10+

getAudioEffectMode(): Promise<AudioEffectMode>

Obtains the audio effect mode in use. This API uses a promise to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Renderer

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[AudioEffectMode](../enums/document.md#audioeffectmode10)\> | Promise used to return the audio effect mode. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.getAudioEffectMode().then((effectMode: audio.AudioEffectMode) => {
  console.info(\`getAudioEffectMode: ${effectMode}\`);
}).catch((err: BusinessError) => {
  console.error(\`ERROR: ${err}\`);
});

#### start8+

start(callback: AsyncCallback<void>): void

Starts this audio renderer. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Renderer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | 
Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. If the operation fails, an error object with one of the following error codes is returned:

Error code 6800301: indicates abnormal status, focus preemption failure, and abnormal system processing. For details, see system logs.

 |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.start((err: BusinessError) => {
  if (err) {
    console.error('Renderer start failed.');
  } else {
    console.info('Renderer start success.');
  }
});

#### start8+

start(): Promise<void>

Starts this audio renderer. This API uses a promise to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Renderer

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | 
Promise object, which indicates that the renderer is started successfully. If the operation fails, an error object with one of the following error codes is returned:

Error code 6800301: indicates abnormal status, focus preemption failure, and abnormal system processing. For details, see system logs.

 |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.start().then(() => {
  console.info('Renderer started');
}).catch((err: BusinessError) => {
  console.error(\`ERROR: ${err}\`);
});

#### pause8+

pause(callback: AsyncCallback<void>): void

Pauses this audio renderer. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Renderer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.pause((err: BusinessError) => {
  if (err) {
    console.error('Renderer pause failed');
  } else {
    console.info('Renderer paused.');
  }
});

#### pause8+

pause(): Promise<void>

Pauses this audio renderer. This API uses a promise to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Renderer

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.pause().then(() => {
  console.info('Renderer paused');
}).catch((err: BusinessError) => {
  console.error(\`ERROR: ${err}\`);
});

#### drain8+

drain(callback: AsyncCallback<void>): void

Drains the playback buffer. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Renderer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.drain((err: BusinessError) => {
  if (err) {
    console.error('Renderer drain failed');
  } else {
    console.info('Renderer drained.');
  }
});

#### drain8+

drain(): Promise<void>

Drains the playback buffer. This API uses a promise to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Renderer

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.drain().then(() => {
  console.info('Renderer drained successfully');
}).catch((err: BusinessError) => {
  console.error(\`ERROR: ${err}\`);
});

#### flush11+

flush(): Promise<void>

Flushes the buffer. This API is available when [AudioState](../enums/document.md#audiostate8) is **STATE\_RUNNING**, **STATE\_PAUSED**, or **STATE\_STOPPED**. This API uses a promise to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Renderer

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6800103 | Operation not permit at current state. Return by promise. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.flush().then(() => {
  console.info('Renderer flushed successfully');
}).catch((err: BusinessError) => {
  console.error(\`ERROR: ${err}\`);
});

#### stop8+

stop(callback: AsyncCallback<void>): void

Stops this audio renderer. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Renderer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.stop((err: BusinessError) => {
  if (err) {
    console.error('Renderer stop failed');
  } else {
    console.info('Renderer stopped.');
  }
});

#### stop8+

stop(): Promise<void>

Stops this audio renderer. This API uses a promise to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Renderer

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.stop().then(() => {
  console.info('Renderer stopped successfully');
}).catch((err: BusinessError) => {
  console.error(\`ERROR: ${err}\`);
});

#### release8+

release(callback: AsyncCallback<void>): void

Releases the renderer. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Renderer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.release((err: BusinessError) => {
  if (err) {
    console.error('Renderer release failed');
  } else {
    console.info('Renderer released.');
  }
});

#### release8+

release(): Promise<void>

Releases the renderer. This API uses a promise to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Renderer

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.release().then(() => {
  console.info('Renderer released successfully');
}).catch((err: BusinessError) => {
  console.error(\`ERROR: ${err}\`);
});

#### getAudioTime8+

getAudioTime(callback: AsyncCallback<number>): void

Obtains the timestamp of the current playback position, measured in nanoseconds from the Unix epoch (January 1, 1970). This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Renderer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<number> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the number of nanoseconds obtained; otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.getAudioTime((err: BusinessError, timestamp: number) => {
  console.info(\`Current timestamp: ${timestamp}\`);
});

#### getAudioTime8+

getAudioTime(): Promise<number>

Obtains the timestamp of the current playback position, measured in nanoseconds from the Unix epoch (January 1, 1970). This API uses a promise to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Renderer

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the timestamp. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.getAudioTime().then((timestamp: number) => {
  console.info(\`Current timestamp: ${timestamp}\`);
}).catch((err: BusinessError) => {
  console.error(\`ERROR: ${err}\`);
});

#### getAudioTimeSync10+

getAudioTimeSync(): number

Obtains the timestamp of the current playback position, measured in nanoseconds from the Unix epoch (January 1, 1970). This API returns the result synchronously.

**System capability**: SystemCapability.Multimedia.Audio.Renderer

**Return value**

| Type | Description |
| :-- | :-- |
| number | Timestamp. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let timestamp: number = audioRenderer.getAudioTimeSync();
  console.info(\`Current timestamp: ${timestamp}\`);
} catch (err) {
  let error = err as BusinessError;
  console.error(\`ERROR: ${error}\`);
}

#### getAudioTimestampInfo19+

getAudioTimestampInfo(): Promise<AudioTimestampInfo>

Obtains the timestamp and position information of an output audio stream. It adapts to the speed adjustment interface. This API uses a promise to return the result.

This information is commonly used for audio and video synchronization.

Note that when the actual playback position (**framePosition**) is 0, the timestamp remains fixed until the stream begins to play. The playback position is also reset when **Flush** is called.

Additionally, changes in the audio stream route, such as switching devices or output types, will reset the playback position, whereas the timestamp keeps increasing. You are advised to call this API to obtain the corresponding value only when the actual playback position and timestamp are stable. This API adapts to the speed adjustment interface. For example, if the playback speed is set to 2x, the rate at which the playback position increases is also twice the normal speed.

**System capability**: SystemCapability.Multimedia.Audio.Renderer

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[AudioTimestampInfo](../interfaces-others/document.md#audiotimestampinfo19)\> | Promise used to return the audio stream timestamp and the current data frame position. |

**Error codes**

For details about the error codes, see [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6800103 | Operation not permit at current state. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.getAudioTimestampInfo().then((audioTimestampInfo: audio.AudioTimestampInfo) => {
  console.info(\`Current timestamp: ${audioTimestampInfo.timestamp}\`);
}).catch((err: BusinessError) => {
  console.error(\`ERROR: ${err}\`);
});

#### getAudioTimestampInfoSync19+

getAudioTimestampInfoSync(): AudioTimestampInfo

Obtains the information about the audio stream timestamp and the current data frame position. This API returns the result synchronously.

**System capability**: SystemCapability.Multimedia.Audio.Renderer

**Return value**

| Type | Description |
| :-- | :-- |
| [AudioTimestampInfo](../interfaces-others/document.md#audiotimestampinfo19) | Information about the audio stream timestamp and the current data frame position. |

**Error codes**

For details about the error codes, see [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6800103 | Operation not permit at current state. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let audioTimestampInfo: audio.AudioTimestampInfo = audioRenderer.getAudioTimestampInfoSync();
  console.info(\`Current timestamp: ${audioTimestampInfo.timestamp}\`);
} catch (err) {
  let error = err as BusinessError;
  console.error(\`ERROR: ${error}\`);
}

#### getBufferSize8+

getBufferSize(callback: AsyncCallback<number>): void

Obtains a reasonable minimum buffer size in bytes for rendering. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Renderer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<number> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the minimum buffer size obtained; otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let bufferSize: number;

audioRenderer.getBufferSize((err: BusinessError, data: number) => {
  if (err) {
    console.error('getBufferSize error');
  } else {
    console.info(\`AudioFrameworkRenderLog: getBufferSize: SUCCESS ${data}\`);
    bufferSize = data;
  }
});

#### getBufferSize8+

getBufferSize(): Promise<number>

Obtains a reasonable minimum buffer size in bytes for rendering. This API uses a promise to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Renderer

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the buffer size. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let bufferSize: number;

audioRenderer.getBufferSize().then((data: number) => {
  console.info(\`AudioFrameworkRenderLog: getBufferSize: SUCCESS ${data}\`);
  bufferSize = data;
}).catch((err: BusinessError) => {
  console.error(\`AudioFrameworkRenderLog: getBufferSize: ERROR: ${err}\`);
});

#### getBufferSizeSync10+

getBufferSizeSync(): number

Obtains a reasonable minimum buffer size in bytes for rendering. This API returns the result synchronously.

**System capability**: SystemCapability.Multimedia.Audio.Renderer

**Return value**

| Type | Description |
| :-- | :-- |
| number | Buffer size. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let bufferSize: number = 0;

try {
  bufferSize = audioRenderer.getBufferSizeSync();
  console.info(\`AudioFrameworkRenderLog: getBufferSize: SUCCESS ${bufferSize}\`);
} catch (err) {
  let error = err as BusinessError;
  console.error(\`AudioFrameworkRenderLog: getBufferSize: ERROR: ${error}\`);
}

#### setSpeed11+

setSpeed(speed: number): void

Sets the playback speed.

**System capability**: SystemCapability.Multimedia.Audio.Renderer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| speed | number | Yes | Playback rate, which ranges from 0.25 to 4.0. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |

**Example**

audioRenderer.setSpeed(1.5);

#### getSpeed11+

getSpeed(): number

Obtains the playback speed.

**System capability**: SystemCapability.Multimedia.Audio.Renderer

**Return value**

| Type | Description |
| :-- | :-- |
| number | Playback speed. |

**Example**

let speed = audioRenderer.getSpeed();

#### setInterruptMode9+

setInterruptMode(mode: InterruptMode): Promise<void>

Sets the audio interruption mode for the application. This API uses a promise to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Interrupt

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| mode | [InterruptMode](../enums/document.md#interruptmode9) | Yes | Audio interruption mode. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let mode = 0;

audioRenderer.setInterruptMode(mode).then(() => {
  console.info('setInterruptMode Success!');
}).catch((err: BusinessError) => {
  console.error(\`setInterruptMode Fail: ${err}\`);
});

#### setInterruptMode9+

setInterruptMode(mode: InterruptMode, callback: AsyncCallback<void>): void

Sets the audio interruption mode for the application. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Interrupt

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| mode | [InterruptMode](../enums/document.md#interruptmode9) | Yes | Audio interruption mode. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let mode = 1;

audioRenderer.setInterruptMode(mode, (err: BusinessError) => {
  if(err){
    console.error(\`setInterruptMode Fail: ${err}\`);
  }
  console.info('setInterruptMode Success!');
});

#### setInterruptModeSync10+

setInterruptModeSync(mode: InterruptMode): void

Sets the audio interruption mode for the application. This API returns the result synchronously.

**System capability**: SystemCapability.Multimedia.Audio.Interrupt

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| mode | [InterruptMode](../enums/document.md#interruptmode9) | Yes | Audio interruption mode. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  audioRenderer.setInterruptModeSync(0);
  console.info('setInterruptMode Success!');
} catch (err) {
  let error = err as BusinessError;
  console.error(\`setInterruptMode Fail: ${error}\`);
}

#### setVolume9+

setVolume(volume: number): Promise<void>

Sets the volume for the audio stream. This API uses a promise to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Renderer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| volume | number | Yes | Volume to set, which is in the range \[0.0, 1.0\]. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.setVolume(0.5).then(() => {
  console.info('setVolume Success!');
}).catch((err: BusinessError) => {
  console.error(\`setVolume Fail: ${err}\`);
});

#### setVolume9+

setVolume(volume: number, callback: AsyncCallback<void>): void

Sets the volume for the audio stream. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Renderer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| volume | number | Yes | Volume to set, which is in the range \[0.0, 1.0\]. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.setVolume(0.5, (err: BusinessError) => {
  if(err){
    console.error(\`setVolume Fail: ${err}\`);
    return;
  }
  console.info('setVolume Success!');
});

#### getVolume12+

getVolume(): number

Obtains the volume of the audio stream. This API returns the result synchronously.

**System capability**: SystemCapability.Multimedia.Audio.Renderer

**Return value**

| Type | Description |
| :-- | :-- |
| number | Volume, in the range \[0.0, 1.0\]. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let value: number = audioRenderer.getVolume();
  console.info(\`Indicate that the volume is obtained ${value}.\`);
} catch (err) {
  let error = err as BusinessError;
  console.error(\`Failed to obtain the volume, error ${error}.\`);
}

#### getMinStreamVolume10+

getMinStreamVolume(callback: AsyncCallback<number>): void

Obtains the minimum volume of the audio stream. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Renderer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<number> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the minimum volume (range \[0, 1\]) obtained; otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.getMinStreamVolume((err: BusinessError, minVolume: number) => {
  if (err) {
    console.error(\`getMinStreamVolume error: ${err}\`);
  } else {
    console.info(\`getMinStreamVolume Success! ${minVolume}\`);
  }
});

#### getMinStreamVolume10+

getMinStreamVolume(): Promise<number>

Obtains the minimum volume of the audio stream. This API uses a promise to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Renderer

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the minimum volume, which is in the range \[0, 1\]. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.getMinStreamVolume().then((value: number) => {
  console.info(\`Get min stream volume Success! ${value}\`);
}).catch((err: BusinessError) => {
  console.error(\`Get min stream volume Fail: ${err}\`);
});

#### getMinStreamVolumeSync10+

getMinStreamVolumeSync(): number

Obtains the minimum volume of the audio stream. This API returns the result synchronously.

**System capability**: SystemCapability.Multimedia.Audio.Renderer

**Return value**

| Type | Description |
| :-- | :-- |
| number | Minimum volume, which is in the range \[0, 1\]. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let value: number = audioRenderer.getMinStreamVolumeSync();
  console.info(\`Get min stream volume Success! ${value}\`);
} catch (err) {
  let error = err as BusinessError;
  console.error(\`Get min stream volume Fail: ${error}\`);
}

#### getMaxStreamVolume10+

getMaxStreamVolume(callback: AsyncCallback<number>): void

Obtains the maximum volume of the audio stream. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Renderer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<number> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the maximum volume (range \[0, 1\]) obtained; otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.getMaxStreamVolume((err: BusinessError, maxVolume: number) => {
  if (err) {
    console.error(\`getMaxStreamVolume Fail: ${err}\`);
  } else {
    console.info(\`getMaxStreamVolume Success! ${maxVolume}\`);
  }
});

#### getMaxStreamVolume10+

getMaxStreamVolume(): Promise<number>

Obtains the maximum volume of the audio stream. This API uses a promise to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Renderer

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the maximum volume, which is in the range \[0, 1\]. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.getMaxStreamVolume().then((value: number) => {
  console.info(\`Get max stream volume Success! ${value}\`);
}).catch((err: BusinessError) => {
  console.error(\`Get max stream volume Fail: ${err}\`);
});

#### getMaxStreamVolumeSync10+

getMaxStreamVolumeSync(): number

Obtains the maximum volume of the audio stream. This API returns the result synchronously.

**System capability**: SystemCapability.Multimedia.Audio.Renderer

**Return value**

| Type | Description |
| :-- | :-- |
| number | Maximum volume, which is in the range \[0, 1\]. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let value: number = audioRenderer.getMaxStreamVolumeSync();
  console.info(\`Get max stream volume Success! ${value}\`);
} catch (err) {
  let error = err as BusinessError;
  console.error(\`Get max stream volume Fail: ${error}\`);
}

#### getUnderflowCount10+

getUnderflowCount(callback: AsyncCallback<number>): void

Obtains the number of underflow audio frames in the audio stream that is being played. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Renderer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<number> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the number of underloaded audio frames obtained; otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.getUnderflowCount((err: BusinessError, underflowCount: number) => {
  if (err) {
    console.error(\`getUnderflowCount Fail: ${err}\`);
  } else {
    console.info(\`getUnderflowCount Success! ${underflowCount}\`);
  }
});

#### getUnderflowCount10+

getUnderflowCount(): Promise<number>

Obtains the number of underflow audio frames in the audio stream that is being played. This API uses a promise to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Renderer

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the number of underflow audio frames. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.getUnderflowCount().then((value: number) => {
  console.info(\`Get underflow count Success! ${value}\`);
}).catch((err: BusinessError) => {
  console.error(\`Get underflow count Fail: ${err}\`);
});

#### getUnderflowCountSync10+

getUnderflowCountSync(): number

Obtains the number of underflow audio frames in the audio stream that is being played. This API returns the result synchronously.

**System capability**: SystemCapability.Multimedia.Audio.Renderer

**Return value**

| Type | Description |
| :-- | :-- |
| number | Number of underflow audio frames. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let value: number = audioRenderer.getUnderflowCountSync();
  console.info(\`Get underflow count Success! ${value}\`);
} catch (err) {
  let error = err as BusinessError;
  console.error(\`Get underflow count Fail: ${error}\`);
}

#### getCurrentOutputDevices10+

getCurrentOutputDevices(callback: AsyncCallback<AudioDeviceDescriptors>): void

Obtains the output device information of the audio stream. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Device

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[AudioDeviceDescriptors](../types/document.md#audiodevicedescriptors)\> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the output device information obtained; otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.getCurrentOutputDevices((err: BusinessError, deviceInfo: audio.AudioDeviceDescriptors) => {
  if (err) {
    console.error(\`getCurrentOutputDevices Fail: ${err}\`);
  } else {
    for (let i = 0; i < deviceInfo.length; i++) {
      console.info(\`DeviceInfo id: ${deviceInfo\[i\].id}\`);
      console.info(\`DeviceInfo type: ${deviceInfo\[i\].deviceType}\`);
      console.info(\`DeviceInfo role: ${deviceInfo\[i\].deviceRole}\`);
      console.info(\`DeviceInfo name: ${deviceInfo\[i\].name}\`);
      console.info(\`DeviceInfo address: ${deviceInfo\[i\].address}\`);
      console.info(\`DeviceInfo samplerate: ${deviceInfo\[i\].sampleRates\[0\]}\`);
      console.info(\`DeviceInfo channelcount: ${deviceInfo\[i\].channelCounts\[0\]}\`);
      console.info(\`DeviceInfo channelmask: ${deviceInfo\[i\].channelMasks\[0\]}\`);
    }
  }
});

#### getCurrentOutputDevices10+

getCurrentOutputDevices(): Promise<AudioDeviceDescriptors>

Obtains the output device information of the audio stream. This API uses a promise to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Device

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[AudioDeviceDescriptors](../types/document.md#audiodevicedescriptors)\> | Promise used to return the output device information. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.getCurrentOutputDevices().then((deviceInfo: audio.AudioDeviceDescriptors) => {
  for (let i = 0; i < deviceInfo.length; i++) {
    console.info(\`DeviceInfo id: ${deviceInfo\[i\].id}\`);
    console.info(\`DeviceInfo type: ${deviceInfo\[i\].deviceType}\`);
    console.info(\`DeviceInfo role: ${deviceInfo\[i\].deviceRole}\`);
    console.info(\`DeviceInfo name: ${deviceInfo\[i\].name}\`);
    console.info(\`DeviceInfo address: ${deviceInfo\[i\].address}\`);
    console.info(\`DeviceInfo samplerate: ${deviceInfo\[i\].sampleRates\[0\]}\`);
    console.info(\`DeviceInfo channelcount: ${deviceInfo\[i\].channelCounts\[0\]}\`);
    console.info(\`DeviceInfo channelmask: ${deviceInfo\[i\].channelMasks\[0\]}\`);
  }
}).catch((err: BusinessError) => {
  console.error(\`Get current output devices Fail: ${err}\`);
});

#### getCurrentOutputDevicesSync10+

getCurrentOutputDevicesSync(): AudioDeviceDescriptors

Obtains the output device information of the audio stream. This API returns the result synchronously.

**System capability**: SystemCapability.Multimedia.Audio.Device

**Return value**

| Type | Description |
| :-- | :-- |
| [AudioDeviceDescriptors](../types/document.md#audiodevicedescriptors) | Output device information. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let deviceInfo: audio.AudioDeviceDescriptors = audioRenderer.getCurrentOutputDevicesSync();
  for (let i = 0; i < deviceInfo.length; i++) {
    console.info(\`DeviceInfo id: ${deviceInfo\[i\].id}\`);
    console.info(\`DeviceInfo type: ${deviceInfo\[i\].deviceType}\`);
    console.info(\`DeviceInfo role: ${deviceInfo\[i\].deviceRole}\`);
    console.info(\`DeviceInfo name: ${deviceInfo\[i\].name}\`);
    console.info(\`DeviceInfo address: ${deviceInfo\[i\].address}\`);
    console.info(\`DeviceInfo samplerate: ${deviceInfo\[i\].sampleRates\[0\]}\`);
    console.info(\`DeviceInfo channelcount: ${deviceInfo\[i\].channelCounts\[0\]}\`);
    console.info(\`DeviceInfo channelmask: ${deviceInfo\[i\].channelMasks\[0\]}\`);
  }
} catch (err) {
  let error = err as BusinessError;
  console.error(\`Get current output devices Fail: ${error}\`);
}

#### setChannelBlendMode11+

setChannelBlendMode(mode: ChannelBlendMode): void

Sets the audio channel blending mode. This API returns the result synchronously.

**System capability**: SystemCapability.Multimedia.Audio.Renderer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| mode | [ChannelBlendMode](../enums/document.md#channelblendmode11) | Yes | Audio channel blending mode. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |
| 6800103 | Operation not permit at current state. |

**Example**

let mode = audio.ChannelBlendMode.MODE\_DEFAULT;

audioRenderer.setChannelBlendMode(mode);
console.info(\`BlendMode: ${mode}\`);

#### setVolumeWithRamp11+

setVolumeWithRamp(volume: number, duration: number): void

Sets a volume ramp. This API returns the result synchronously.

**System capability**: SystemCapability.Multimedia.Audio.Renderer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| volume | number | Yes | Target volume, within the range \[0.0, 1.0\]. |
| duration | number | Yes | Time range during which the ramp applies, in ms. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |

**Example**

let volume = 0.5;
let duration = 1000;

audioRenderer.setVolumeWithRamp(volume, duration);
console.info(\`setVolumeWithRamp: ${volume}\`);

#### setSilentModeAndMixWithOthers12+

setSilentModeAndMixWithOthers(on: boolean): void

Sets the silent mode in concurrent playback for the audio stream.

If the silent mode in concurrent playback is enabled, the system mutes the audio stream and does not interrupt other audio streams. If the silent mode in concurrent playback is disabled, the audio stream can gain focus based on the system focus strategy.

**System capability**: SystemCapability.Multimedia.Audio.Renderer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| on | boolean | Yes | Whether to enable or disable the silent mode in concurrent playback for the audio stream. **true** to enable, **false** otherwise. |

**Example**

audioRenderer.setSilentModeAndMixWithOthers(true);

#### getSilentModeAndMixWithOthers12+

getSilentModeAndMixWithOthers(): boolean

Obtains the silent mode in concurrent playback for the audio stream.

**System capability**: SystemCapability.Multimedia.Audio.Renderer

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Enabled status of the silent mode in concurrent playback. **true** if enabled, **false** otherwise. |

**Example**

let on = audioRenderer.getSilentModeAndMixWithOthers();

#### setDefaultOutputDevice12+

setDefaultOutputDevice(deviceType: DeviceType): Promise<void>

Sets the default audio output device. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9/v3/asoUe3olQa6A2wXv5Pkg0A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062417Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3D8438E83515BAEEA2D995B6E98A1B27DE40BB8F74B789EBA6227A35C1643C06)

-   This API applies only to the scenarios where [StreamUsage](../enums/document.md#streamusage) is set to voice message, VoIP voice calls, or VoIP video calls. It supports only receivers, speakers, and system default devices.
-   This API can be called at any time after an AudioRenderer instance is created. When this API is called, the system registers the specified device as the default built-in audio output device for the application. If an external audio device, such as a Bluetooth speaker or wired headset, is connected when the application starts, the system preferentially uses the external device for audio playback. In the absence of an external device, the system uses the device specified by this API for playback.

**System capability**: SystemCapability.Multimedia.Audio.Renderer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| deviceType | [DeviceType](../enums/document.md#devicetype) | Yes | 
Device type.

The options are **EARPIECE**, **SPEAKER**, and **DEFAULT**.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |
| 6800103 | Operation not permit at current state. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

// This API can be called at any time after an AudioRenderer instance is created.
// If the API is called when no audio is being played, the system records the default device set by the application. When the application starts playing, the sound is played from this default device.
// If the API is called when audio is being played and no external device, such as a Bluetooth or wired headset, is connected, the system immediately switches to the default device. If an external device is connected, the system records the default device and switches to it once the external device is disconnected.
audioRenderer.setDefaultOutputDevice(audio.DeviceType.SPEAKER).then(() => {
  console.info('setDefaultOutputDevice Success!');
}).catch((err: BusinessError) => {
  console.error(\`setDefaultOutputDevice Fail: ${err}\`);
});

#### on('audioInterrupt')9+

on(type: 'audioInterrupt', callback: Callback<InterruptEvent>): void

Subscribes to the audio interruption event, which is triggered when the audio focus is changed. This API uses an asynchronous callback to return the result.

The AudioRenderer instance proactively gains the focus when the **start** event occurs and releases the focus when the **pause** or **stop** event occurs. Therefore, you do not need to request to gain or release the focus.

After this API is called, an [InterruptEvent](../interfaces-others/document.md#interruptevent9) is received when the AudioRenderer instance fails to obtain the focus or an audio interruption event occurs (for example, the audio stream is interrupted by others). It is recommended that the application perform further processing based on the **InterruptEvent** information. For details, see [Introduction to Audio Focus](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/audio-playback-concurrency).

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

let isPlaying: boolean = false; // An identifier specifying whether rendering is in progress.
let isDucked: boolean = false; // An identifier specifying whether the audio volume is reduced.

audioRenderer.on('audioInterrupt', (interruptEvent: audio.InterruptEvent) => {
  // When an audio interruption event occurs, the AudioRenderer receives the interruptEvent callback and performs processing based on the content in the callback.
  // 1. (Optional) The AudioRenderer reads the value of interruptEvent.forceType to see whether the system has forcibly performed the operation.
  // Note: In the default focus strategy, INTERRUPT\_HINT\_RESUME maps to the force type INTERRUPT\_SHARE, and others map to INTERRUPT\_FORCE. Therefore, the value of forceType does not need to be checked.
  // 2. (Mandatory) The AudioRenderer then reads the value of interruptEvent.hintType and performs corresponding processing.
  if (interruptEvent.forceType == audio.InterruptForceType.INTERRUPT\_FORCE) {
    // The audio focus event has been forcibly executed by the system. The application needs to update its status and displayed content.
    switch (interruptEvent.hintType) {
      case audio.InterruptHint.INTERRUPT\_HINT\_PAUSE:
        // The audio stream has been paused and temporarily loses the focus. It will receive the interruptEvent corresponding to resume when it is able to regain the focus.
        console.info('Force paused. Update playing status and stop writing');
        isPlaying = false; // A simplified processing indicating several operations for switching the application to the paused state.
        break;
      case audio.InterruptHint.INTERRUPT\_HINT\_STOP:
        // The audio stream has been stopped and permanently loses the focus. The user must manually trigger the operation to resume rendering.
        console.info('Force stopped. Update playing status and stop writing');
        isPlaying = false; // A simplified processing indicating several operations for switching the application to the paused state.
        break;
      case audio.InterruptHint.INTERRUPT\_HINT\_DUCK:
        // The audio stream is rendered at a reduced volume.
        console.info('Force ducked. Update volume status');
        isDucked = true; // A simplified processing indicating several operations for updating the volume status.
        break;
      case audio.InterruptHint.INTERRUPT\_HINT\_UNDUCK:
        // The audio stream is rendered at the normal volume.
        console.info('Force unducked. Update volume status');
        isDucked = false; // A simplified processing indicating several operations for updating the volume status.
        break;
      default:
        console.info('Invalid interruptEvent');
        break;
    }
  } else if (interruptEvent.forceType == audio.InterruptForceType.INTERRUPT\_SHARE) {
    // The audio focus event needs to be operated by the application, which can choose the processing mode. It is recommended that the application process the event according to the value of InterruptHint.
    switch (interruptEvent.hintType) {
      case audio.InterruptHint.INTERRUPT\_HINT\_RESUME:
        // It is recommended that the application continue rendering. (The audio stream has been forcibly paused and temporarily lost the focus. It can resume rendering now.)
        // The INTERRUPT\_HINT\_RESUME operation must be proactively executed by the application and cannot be forcibly executed by the system. Therefore, the INTERRUPT\_HINT\_RESUME event must map to INTERRUPT\_SHARE.
        console.info('Resume force paused renderer or ignore');
        // To continue rendering, the application must perform the required operations.
        break;
      default:
        console.info('Invalid interruptEvent');
        break;
    }
  }
});

#### off('audioInterrupt')18+

off(type: 'audioInterrupt', callback?: Callback<InterruptEvent>): void

Unsubscribes from the audio interruption event. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Interrupt

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'audioInterrupt'** is triggered when the audio focus is changed. |
| callback | Callback<[InterruptEvent](../interfaces-others/document.md#interruptevent9)\> | No | Callback used to return the event information. |

**Error codes**

For details about the error codes, see [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6800101 | Parameter verification failed. |

**Example**

// Cancel all subscriptions to the event.
audioRenderer.off('audioInterrupt');

// For the same event, if the callback parameter passed to the off API is the same as that passed to the on API, the off API cancels the subscription registered with the specified callback parameter.
let isPlaying: boolean; // An identifier specifying whether rendering is in progress.
let isDucked: boolean; // An identifier specifying whether the audio volume is reduced.

let audioInterruptCallback = (interruptEvent: audio.InterruptEvent) => {
  // When an audio interruption event occurs, the AudioRenderer receives the interruptEvent callback and performs processing based on the content in the callback.
  // 1. (Optional) The AudioRenderer reads the value of interruptEvent.forceType to see whether the system has forcibly performed the operation.
  // Note: In the default focus strategy, INTERRUPT\_HINT\_RESUME maps to the force type INTERRUPT\_SHARE, and others map to INTERRUPT\_FORCE. Therefore, the value of forceType does not need to be checked.
  // 2. (Mandatory) The AudioRenderer then reads the value of interruptEvent.hintType and performs corresponding processing.
  if (interruptEvent.forceType == audio.InterruptForceType.INTERRUPT\_FORCE) {
    // The audio focus event has been forcibly executed by the system. The application needs to update its status and displayed content.
    switch (interruptEvent.hintType) {
      case audio.InterruptHint.INTERRUPT\_HINT\_PAUSE:
        // The audio stream has been paused and temporarily loses the focus. It will receive the interruptEvent corresponding to resume when it is able to regain the focus.
        console.info('Force paused. Update playing status and stop writing');
        isPlaying = false; // A simplified processing indicating several operations for switching the application to the paused state.
        break;
      case audio.InterruptHint.INTERRUPT\_HINT\_STOP:
        // The audio stream has been stopped and permanently loses the focus. The user must manually trigger the operation to resume rendering.
        console.info('Force stopped. Update playing status and stop writing');
        isPlaying = false; // A simplified processing indicating several operations for switching the application to the paused state.
        break;
      case audio.InterruptHint.INTERRUPT\_HINT\_DUCK:
        // The audio stream is rendered at a reduced volume.
        console.info('Force ducked. Update volume status');
        isDucked = true; // A simplified processing indicating several operations for updating the volume status.
        break;
      case audio.InterruptHint.INTERRUPT\_HINT\_UNDUCK:
        // The audio stream is rendered at the normal volume.
        console.info('Force unducked. Update volume status');
        isDucked = false; // A simplified processing indicating several operations for updating the volume status.
        break;
      default:
        console.info('Invalid interruptEvent');
        break;
    }
  } else if (interruptEvent.forceType == audio.InterruptForceType.INTERRUPT\_SHARE) {
    // The audio focus event needs to be operated by the application, which can choose the processing mode. It is recommended that the application process the event according to the value of InterruptHint.
    switch (interruptEvent.hintType) {
      case audio.InterruptHint.INTERRUPT\_HINT\_RESUME:
        // It is recommended that the application continue rendering. (The audio stream has been forcibly paused and temporarily lost the focus. It can resume rendering now.)
        // The INTERRUPT\_HINT\_RESUME operation must be proactively executed by the application and cannot be forcibly executed by the system. Therefore, the INTERRUPT\_HINT\_RESUME event must map to INTERRUPT\_SHARE.
        console.info('Resume force paused renderer or ignore');
        // To continue rendering, the application must perform the required operations.
        break;
      default:
        console.info('Invalid interruptEvent');
        break;
    }
  }
};

audioRenderer.on('audioInterrupt', audioInterruptCallback);

audioRenderer.off('audioInterrupt', audioInterruptCallback);

#### on('markReach')8+

on(type: 'markReach', frame: number, callback: Callback<number>): void

Subscribes to the mark reached event, which is triggered (only once) when the number of frames rendered reaches the value of the **frame** parameter. This API uses an asynchronous callback to return the result.

For example, if **frame** is set to **100**, the callback is invoked when the number of rendered frames reaches the 100th frame.

**System capability**: SystemCapability.Multimedia.Audio.Renderer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'markReach'** is triggered when the number of frames rendered reaches the value of the **frame** parameter. |
| frame | number | Yes | Number of frames to trigger the event. The value must be greater than **0**. |
| callback | Callback<number> | Yes | Callback used to return the value of the **frame** parameter. |

**Example**

audioRenderer.on('markReach', 1000, (position: number) => {
  if (position == 1000) {
    console.info('ON Triggered successfully');
  }
});

#### off('markReach')8+

off(type: 'markReach', callback?: Callback<number>): void

Unsubscribes from the mark reached event. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Renderer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'markReach'** is triggered when the number of frames rendered reaches the value of the **frame** parameter. |
| callback18+ | Callback<number> | No | Callback used to return the value of the **frame** parameter. |

**Example**

// Cancel all subscriptions to the event.
audioRenderer.off('markReach');

// For the same event, if the callback parameter passed to the off API is the same as that passed to the on API, the off API cancels the subscription registered with the specified callback parameter.
let markReachCallback = (position: number) => {
  if (position == 1000) {
    console.info('ON Triggered successfully');
  }
};

audioRenderer.on('markReach', 1000, markReachCallback);

audioRenderer.off('markReach', markReachCallback);

#### on('periodReach')8+

on(type: 'periodReach', frame: number, callback: Callback<number>): void

Subscribes to the period reached event, which is triggered each time the number of frames rendered reaches the value of the **frame** parameter. In other words, the information is reported periodically. This API uses an asynchronous callback to return the result.

For example, if **frame** is set to **10**, the callback is invoked each time 10 frames are rendered, for example, when the number of frames rendered reaches the 10th frame, 20th frame, and 30th frame.

**System capability**: SystemCapability.Multimedia.Audio.Renderer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'periodReach'** is triggered each time the number of frames rendered reaches the value of the **frame** parameter. |
| frame | number | Yes | Number of frames to trigger the event. The value must be greater than **0**. |
| callback | Callback<number> | Yes | Callback used to return the value of the **frame** parameter. |

**Example**

audioRenderer.on('periodReach', 1000, (position: number) => {
  if (position == 1000) {
    console.info('ON Triggered successfully');
  }
});

#### off('periodReach')8+

off(type: 'periodReach', callback?: Callback<number>): void

Unsubscribes from the period reached event. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Renderer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'periodReach'** is triggered each time the number of frames rendered reaches the value of the **frame** parameter. |
| callback18+ | Callback<number> | No | Callback used to return the value of the **frame** parameter. |

**Example**

// Cancel all subscriptions to the event.
audioRenderer.off('periodReach');

// For the same event, if the callback parameter passed to the off API is the same as that passed to the on API, the off API cancels the subscription registered with the specified callback parameter.
let periodReachCallback = (position: number) => {
  if (position == 1000) {
    console.info('ON Triggered successfully');
  }
};

audioRenderer.on('periodReach', 1000, periodReachCallback);

audioRenderer.off('periodReach', periodReachCallback);

#### on('stateChange')8+

on(type: 'stateChange', callback: Callback<AudioState>): void

Subscribes to the audio renderer state change event, which is triggered when the state of the audio renderer is changed. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Renderer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'stateChange'** is triggered when the state of the audio renderer is changed. |
| callback | Callback<[AudioState](../enums/document.md#audiostate8)\> | Yes | Callback used to return the audio status. |

**Example**

audioRenderer.on('stateChange', (state: audio.AudioState) => {
  if (state == 1) {
    console.info('audio renderer state is: STATE\_PREPARED');
  }
  if (state == 2) {
    console.info('audio renderer state is: STATE\_RUNNING');
  }
});

#### off('stateChange')18+

off(type: 'stateChange', callback?: Callback<AudioState>): void

Unsubscribes from the audio renderer state change event. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Renderer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'stateChange'** is triggered when the listening for audio renderer state change event is canceled. |
| callback | Callback<[AudioState](../enums/document.md#audiostate8)\> | No | Callback used to return the audio status. |

**Error codes**

For details about the error codes, see [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6800101 | Parameter verification failed. |

**Example**

// Cancel all subscriptions to the event.
audioRenderer.off('stateChange');

// For the same event, if the callback parameter passed to the off API is the same as that passed to the on API, the off API cancels the subscription registered with the specified callback parameter.
let stateChangeCallback = (state: audio.AudioState) => {
  if (state == 1) {
    console.info('audio renderer state is: STATE\_PREPARED');
  }
  if (state == 2) {
    console.info('audio renderer state is: STATE\_RUNNING');
  }
};

audioRenderer.on('stateChange', stateChangeCallback);

audioRenderer.off('stateChange', stateChangeCallback);

#### on('outputDeviceChange')10+

on(type: 'outputDeviceChange', callback: Callback<AudioDeviceDescriptors>): void

Subscribes to the audio output device change event, which is triggered when an audio output device is changed. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Device

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'outputDeviceChange'** is triggered when an audio output device is changed. |
| callback | Callback<[AudioDeviceDescriptors](../types/document.md#audiodevicedescriptors)\> | Yes | Callback used to return the output device descriptor of the current audio stream. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |

**Example**

audioRenderer.on('outputDeviceChange', (deviceInfo: audio.AudioDeviceDescriptors) => {
  console.info(\`DeviceInfo id: ${deviceInfo\[0\].id}\`);
  console.info(\`DeviceInfo name: ${deviceInfo\[0\].name}\`);
  console.info(\`DeviceInfo address: ${deviceInfo\[0\].address}\`);
});

#### off('outputDeviceChange')10+

off(type: 'outputDeviceChange', callback?: Callback<AudioDeviceDescriptors>): void

Unsubscribes from the audio output device change event. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Device

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'outputDeviceChange'** is triggered when an audio output device is changed. |
| callback | Callback<[AudioDeviceDescriptors](../types/document.md#audiodevicedescriptors)\> | No | Callback used to return the output device descriptor of the current audio stream. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |

**Example**

// Cancel all subscriptions to the event.
audioRenderer.off('outputDeviceChange');

// For the same event, if the callback parameter passed to the off API is the same as that passed to the on API, the off API cancels the subscription registered with the specified callback parameter.
let outputDeviceChangeCallback = (deviceInfo: audio.AudioDeviceDescriptors) => {
  console.info(\`DeviceInfo id: ${deviceInfo\[0\].id}\`);
  console.info(\`DeviceInfo name: ${deviceInfo\[0\].name}\`);
  console.info(\`DeviceInfo address: ${deviceInfo\[0\].address}\`);
};

audioRenderer.on('outputDeviceChange', outputDeviceChangeCallback);

audioRenderer.off('outputDeviceChange', outputDeviceChangeCallback);

#### on('outputDeviceChangeWithInfo')11+

on(type: 'outputDeviceChangeWithInfo', callback: Callback<AudioStreamDeviceChangeInfo>): void

Subscribes to the change event of audio output devices and reasons, which is triggered when an audio output device is changed, and the change reason is reported. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Device

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'outputDeviceChangeWithInfo'** is triggered when an audio output device is changed, and the change reason is reported. |
| callback | Callback<[AudioStreamDeviceChangeInfo](../interfaces-others/document.md#audiostreamdevicechangeinfo11)\> | Yes | Callback used to return the output device descriptor of the current audio stream and the change reason. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |

**Example**

audioRenderer.on('outputDeviceChangeWithInfo', (deviceChangeInfo: audio.AudioStreamDeviceChangeInfo) => {
  console.info(\`DeviceInfo id: ${deviceChangeInfo.devices\[0\].id}\`);
  console.info(\`DeviceInfo name: ${deviceChangeInfo.devices\[0\].name}\`);
  console.info(\`DeviceInfo address: ${deviceChangeInfo.devices\[0\].address}\`);
  console.info(\`Device change reason: ${deviceChangeInfo.changeReason}\`);
});

#### off('outputDeviceChangeWithInfo')11+

off(type: 'outputDeviceChangeWithInfo', callback?: Callback<AudioStreamDeviceChangeInfo>): void

Unsubscribes from the change event of audio output devices and reasons. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Device

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'outputDeviceChangeWithInfo'** is triggered when an audio output device is changed, and the change reason is reported. |
| callback | Callback<[AudioStreamDeviceChangeInfo](../interfaces-others/document.md#audiostreamdevicechangeinfo11)\> | No | Callback used to return the output device descriptor of the current audio stream and the change reason. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |

**Example**

// Cancel all subscriptions to the event.
audioRenderer.off('outputDeviceChangeWithInfo');

// For the same event, if the callback parameter passed to the off API is the same as that passed to the on API, the off API cancels the subscription registered with the specified callback parameter.
let outputDeviceChangeWithInfoCallback = (deviceChangeInfo: audio.AudioStreamDeviceChangeInfo) => {
  console.info(\`DeviceInfo id: ${deviceChangeInfo.devices\[0\].id}\`);
  console.info(\`DeviceInfo name: ${deviceChangeInfo.devices\[0\].name}\`);
  console.info(\`DeviceInfo address: ${deviceChangeInfo.devices\[0\].address}\`);
  console.info(\`Device change reason: ${deviceChangeInfo.changeReason}\`);
};

audioRenderer.on('outputDeviceChangeWithInfo', outputDeviceChangeWithInfoCallback);

audioRenderer.off('outputDeviceChangeWithInfo', outputDeviceChangeWithInfoCallback);

#### on('writeData')11+

on(type: 'writeData', callback: AudioRendererWriteDataCallback): void

Subscribes to the audio data write event, which is triggered when audio data needs to be written. This API uses an asynchronous callback to return the result.

The callback function is used only to write audio data. Do not call AudioRenderer APIs in it.

**System capability**: SystemCapability.Multimedia.Audio.Renderer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'writeData'** is triggered when audio data needs to be written. |
| callback | [AudioRendererWriteDataCallback](../types/document.md#audiorendererwritedatacallback12) | Yes | 
Callback used to write the data to the buffer.

API version 11 does not support the return of the callback result. API version 12 and later support the return of the callback result [AudioDataCallbackResult](../enums/document.md#audiodatacallbackresult12).

 |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import {fileIo as fs} from '@kit.CoreFileKit';
import { common } from '@kit.AbilityKit';

class Options {
  offset?: number;
  length?: number;
}

let bufferSize: number = 0;
// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let path = context.cacheDir;
// This is just an example. Replace the file with the PCM file to be played by the application.
let filePath = path + '/StarWars10s-2C-48000-4SW.pcm';
let file: fs.File = fs.openSync(filePath, fs.OpenMode.READ\_ONLY);
let writeDataCallback = (buffer: ArrayBuffer) => {
  let options: Options = {
    offset: bufferSize,
    length: buffer.byteLength
  };

  try {
    fs.readSync(file.fd, buffer, options);
    bufferSize += buffer.byteLength;
    // This API does not return a callback result in API version 11, but does so in API version 12 and later versions.
    return audio.AudioDataCallbackResult.VALID;
  } catch (error) {
    console.error('Error reading file:', error);
    // This API does not return a callback result in API version 11, but does so in API version 12 and later versions.
    return audio.AudioDataCallbackResult.INVALID;
  }
};

audioRenderer.on('writeData', writeDataCallback);
audioRenderer.start().then(() => {
  console.info('Renderer started');
}).catch((err: BusinessError) => {
  console.error(\`ERROR: ${err}\`);
});

#### off('writeData')11+

off(type: 'writeData', callback?: AudioRendererWriteDataCallback): void

Unsubscribes from the audio data write event. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Renderer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'writeData'** is triggered when audio data needs to be written. |
| callback | [AudioRendererWriteDataCallback](../types/document.md#audiorendererwritedatacallback12) | No | 
Callback used to write the data to the buffer.

API version 11 does not support the return of the callback result. API version 12 and later support the return of the callback result [AudioDataCallbackResult](../enums/document.md#audiodatacallbackresult12).

 |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 6800101 | Parameter verification failed. |

**Example**

// Cancel all subscriptions to the event.
audioRenderer.off('writeData');

// For the same event, if the callback parameter passed to the off API is the same as that passed to the on API, the off API cancels the subscription registered with the specified callback parameter.
let writeDataCallback = (data: ArrayBuffer) => {
    console.info(\`write data: ${data}\`);
};

audioRenderer.on('writeData', writeDataCallback);

audioRenderer.off('writeData', writeDataCallback);

#### write(deprecated)

write(buffer: ArrayBuffer, callback: AsyncCallback<number>): void

Writes the buffer. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/Gbz8KeV7RaCsFF2RuuuqTw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062417Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=68939147A72D085DFF2AA7D08C502699B8E8C6A9FAC59D5C5E13A85B3CFF2C6A)

This API is supported since API version 8 and deprecated since API version 11. You are advised to use [on('writeData')](#onwritedata11) instead.

**System capability**: SystemCapability.Multimedia.Audio.Renderer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| buffer | ArrayBuffer | Yes | Data to be written to the buffer. |
| callback | AsyncCallback<number> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the number of bytes written; otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo as fs } from '@kit.CoreFileKit';
import { common } from '@kit.AbilityKit';

let bufferSize: number;
class Options {
  offset?: number;
  length?: number;
}
audioRenderer.getBufferSize().then((data: number)=> {
  console.info(\`AudioFrameworkRenderLog: getBufferSize: SUCCESS ${data}\`);
  bufferSize = data;
  console.info(\`Buffer size: ${bufferSize}\`);
  // Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
  let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  let path = context.cacheDir;
  // This is just an example. Replace the file with the PCM file to be played by the application.
  let filePath = path + '/StarWars10s-2C-48000-4SW.pcm';
  let file: fs.File = fs.openSync(filePath, fs.OpenMode.READ\_ONLY);
  fs.stat(filePath).then(async (stat: fs.Stat) => {
    let buf = new ArrayBuffer(bufferSize);
    let len = stat.size % bufferSize == 0 ? Math.floor(stat.size / bufferSize) : Math.floor(stat.size / bufferSize + 1);
    for (let i = 0;i < len; i++) {
      let options: Options = {
        offset: i \* bufferSize,
        length: bufferSize
      };
      await fs.read(file.fd, buf, options);
      await new Promise((resolve,reject)=>{
        audioRenderer.write(buf,(err: BusinessError, writeSize: number)=>{
          if(err){
            reject(err)
          }else{
            resolve(writeSize)
          }
        })
      })
    }
  });
  }).catch((err: BusinessError) => {
    console.error(\`AudioFrameworkRenderLog: getBufferSize: ERROR: ${err}\`);
});

#### write(deprecated)

write(buffer: ArrayBuffer): Promise<number>

Writes the buffer. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/Kf5Cs1zzTVu2_HTXWXXIxA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062417Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=31C444D71268FA8F2AC4B6593E9CBBEC98330E0DE53FEEE3B54EA34BE2D34E72)

This API is supported since API version 8 and deprecated since API version 11. You are advised to use [on('writeData')](#onwritedata11) instead.

**System capability**: SystemCapability.Multimedia.Audio.Renderer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| buffer | ArrayBuffer | Yes | Data to be written to the buffer. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the number of written bytes. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo as fs } from '@kit.CoreFileKit';
import { common } from '@kit.AbilityKit';

let bufferSize: number;
class Options {
  offset?: number;
  length?: number;
}
audioRenderer.getBufferSize().then((data: number) => {
  console.info(\`AudioFrameworkRenderLog: getBufferSize: SUCCESS ${data}\`);
  bufferSize = data;
  console.info(\`BufferSize: ${bufferSize}\`);
  // Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
  let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  let path = context.cacheDir;
  // This is just an example. Replace the file with the PCM file to be played by the application.
  let filePath = path + '/StarWars10s-2C-48000-4SW.pcm';
  let file: fs.File = fs.openSync(filePath, fs.OpenMode.READ\_ONLY);
  fs.stat(filePath).then(async (stat: fs.Stat) => {
    let buf = new ArrayBuffer(bufferSize);
    let len = stat.size % bufferSize == 0 ? Math.floor(stat.size / bufferSize) : Math.floor(stat.size / bufferSize + 1);
    for (let i = 0;i < len; i++) {
      let options: Options = {
        offset: i \* bufferSize,
        length: bufferSize
      };
      await fs.read(file.fd, buf, options);
      try{
        await audioRenderer.write(buf);
      } catch(err) {
        let error = err as BusinessError;
        console.error(\`audioRenderer.write err: ${error}\`);
      }
    }
  });
}).catch((err: BusinessError) => {
  console.error(\`AudioFrameworkRenderLog: getBufferSize: ERROR: ${err}\`);
});

#### setRenderRate(deprecated)

setRenderRate(rate: AudioRendererRate, callback: AsyncCallback<void>): void

Sets the render rate. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/zXQVLVFcQs-1PFh6rjCvhA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062417Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FB379CE5AD8BA5B3BAC6F43EFA8067B6F0283F718D7538CF3026FF9994B3345F)

This API is supported since API version 8 and deprecated since API version 11. You are advised to use \[uninitialize\][setSpeed](#setspeed11) instead.

**System capability**: SystemCapability.Multimedia.Audio.Renderer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| rate | [AudioRendererRate](../enums/document.md#audiorendererrate8) | Yes | Audio render rate. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.setRenderRate(audio.AudioRendererRate.RENDER\_RATE\_NORMAL, (err: BusinessError) => {
  if (err) {
    console.error('Failed to set params');
  } else {
    console.info('Callback invoked to indicate a successful render rate setting.');
  }
});

#### setRenderRate(deprecated)

setRenderRate(rate: AudioRendererRate): Promise<void>

Sets the render rate. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/Q51hNtPRRPOAKaTm3kugcg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062417Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7004E20ED8AF3B33061AC94DE0AC3DEDA9393906B851648D767C825EA43D5CF7)

This API is supported since API version 8 and deprecated since API version 11. You are advised to use \[uninitialize\][setSpeed](#setspeed11) instead.

**System capability**: SystemCapability.Multimedia.Audio.Renderer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| rate | [AudioRendererRate](../enums/document.md#audiorendererrate8) | Yes | Audio render rate. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.setRenderRate(audio.AudioRendererRate.RENDER\_RATE\_NORMAL).then(() => {
  console.info('setRenderRate SUCCESS');
}).catch((err: BusinessError) => {
  console.error(\`ERROR: ${err}\`);
});

#### getRenderRate(deprecated)

getRenderRate(callback: AsyncCallback<AudioRendererRate>): void

Obtains the audio renderer rate. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/dfHDkke6SKmFHY-O2GUJCw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062417Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3F687DC41D4AC8390E6CC6B5C86A820181F511E4484BC440FBB19C8D29B7C97E)

This API is supported since API version 8 and deprecated since API version 11. You are advised to use [getSpeed](#getspeed11) instead.

**System capability**: SystemCapability.Multimedia.Audio.Renderer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[AudioRendererRate](../enums/document.md#audiorendererrate8)\> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the render rate obtained; otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.getRenderRate((err: BusinessError, renderRate: audio.AudioRendererRate) => {
  console.info(\`getRenderRate: ${renderRate}\`);
});

#### getRenderRate(deprecated)

getRenderRate(): Promise<AudioRendererRate>

Obtains the audio renderer rate. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/zDaNvn48TAiDGZ3X2CadFw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062417Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CB9D964B016C6D18D123AD067DF000E62F483479C73F9B46FD7A332909CBB48D)

This API is supported since API version 8 and deprecated since API version 11. You are advised to use [getSpeed](#getspeed11) instead.

**System capability**: SystemCapability.Multimedia.Audio.Renderer

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[AudioRendererRate](../enums/document.md#audiorendererrate8)\> | Promise used to return the render rate. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.getRenderRate().then((renderRate: audio.AudioRendererRate) => {
  console.info(\`getRenderRate: ${renderRate}\`);
}).catch((err: BusinessError) => {
  console.error(\`ERROR: ${err}\`);
});

#### getRenderRateSync(deprecated)

getRenderRateSync(): AudioRendererRate

Obtains the audio renderer rate. This API returns the result synchronously.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9/v3/SWpyeMMyRJ29VGhnfJcqWw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062417Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1B6C428C82F3D174EB741CF134F0DF24ADCF4FA860D372DEE535F0DD031AB118)

This API is supported since API version 10 and deprecated since API version 11. You are advised to use [getSpeed](#getspeed11) instead.

**System capability**: SystemCapability.Multimedia.Audio.Renderer

**Return value**

| Type | Description |
| :-- | :-- |
| [AudioRendererRate](../enums/document.md#audiorendererrate8) | Audio render rate. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let renderRate: audio.AudioRendererRate = audioRenderer.getRenderRateSync();
  console.info(\`getRenderRate: ${renderRate}\`);
} catch (err) {
  let error = err as BusinessError;
  console.error(\`ERROR: ${error}\`);
}

#### setLoudnessGain20+

setLoudnessGain(loudnessGain: number): Promise<void>

Sets the playback loudness. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c/v3/rNTXzDatRMyIz0IipDM1aw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062417Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1A301E402DCC322B6A3C382E7948FADB1CF291391E02799A39D6039D4D6C0AF6)

-   This API applies only to audio streams of the [STREAM\_USAGE\_MUSIC](../enums/document.md#streamusage), [STREAM\_USAGE\_MOVIE](../enums/document.md#streamusage), or [STREAM\_USAGE\_AUDIOBOOK](../enums/document.md#streamusage) type.
-   Loudness settings are not supported for high-definition channels.
-   Due to the buffer between the audio framework and hardware, there may be a delay in the actual effect of loudness adjustment. The delay duration depends on the buffer length.
-   You are advised to set the loudness before starting playback of different audio streams to achieve the optimal balance effect.

**System capability**: SystemCapability.Multimedia.Audio.Renderer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| loudnessGain | number | Yes | Loudness, in the range \[-90.0, 24.0\], in dB. The default value is 0.0 dB. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6800101 | Parameter verification failed. |
| 6800104 | 
Operation is not supported on this renderer, e.g. the stream usage of this renderer is not one of [STREAM\_USAGE\_MUSIC](../enums/document.md#streamusage),

[STREAM\_USAGE\_MOVIE](../enums/document.md#streamusage), or [STREAM\_USAGE\_AUDIOBOOK](../enums/document.md#streamusage), or this renderer is routed through the high-resolution playback path.

 |

**Example**

audioRenderer.setLoudnessGain(1.0);

#### getLoudnessGain20+

getLoudnessGain(): number

Obtains the playback loudness.

**System capability**: SystemCapability.Multimedia.Audio.Renderer

**Return value**

| Type | Description |
| :-- | :-- |
| number | Playback loudness. |

**Example**

let loudnessGain = audioRenderer.getLoudnessGain();
