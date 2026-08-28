# Interface (AudioLoopback)

This interface provides APIs for audio monitoring.

Before calling any API in AudioLoopback, you must use [audio.createAudioLoopback](../functions/document.md#audiocreateaudioloopback20) to create an AudioLoopback instance.

When audio loopback is enabled, the system creates a low-latency renderer and capturer to implement low-latency in-ear monitoring. The audio captured is routed back to the renderer through an internal path. The renderer follows the audio focus strategy for [STREAM\_USAGE\_MUSIC](../enums/document.md#streamusage), whereas the capturer follows the strategy for [SOURCE\_TYPE\_MIC](../enums/document.md#sourcetype8).

The system automatically chooses the input and output devices. If these devices do not support low latency, audio loopback does not work. If another audio stream takes over the audio focus or if the input or output device changes to the one that does not support low latency, the system disables audio loopback automatically.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/Uy3ws78AT02e-BZe5Lbr_A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062417Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C5241F529AF5371BCC463A18E43E278565A77DF880F6F92FC17BF8EA1EA8DC44)

-   The initial APIs of this module are supported since API version 7. Newly added APIs will be marked with a superscript to indicate their earliest API version.
-   The initial APIs of this interface are supported since API version 20.

#### Modules to Import

import { audio } from '@kit.AudioKit';

#### getStatus20+

getStatus(): Promise<AudioLoopbackStatus>

Obtains the audio loopback status. This API uses a promise to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Capturer

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[AudioLoopbackStatus](../enums/document.md#audioloopbackstatus20)\> | Promise used to return the audio loopback status. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

audioLoopback.getStatus().then((status: audio.AudioLoopbackStatus) => {
  console.info(\`AudioLoopback: Status: ${status}\`);
}).catch((err: BusinessError) => {
  console.error(\`AudioLoopback: Status :ERROR: ${err}\`);
})

#### setVolume20+

setVolume(volume: number): Promise<void>

Sets the volume for audio loopback. This API uses a promise to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Capturer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| volume | number | Yes | Volume to set, which is in the range \[0.0, 1.0\]. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6800101 | Parameter verification failed, form 0.0 to 1.0. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

audioLoopback.setVolume(0.5).then(() => {
  console.info('setVolume Success!');
}).catch((err: BusinessError) => {
  console.error(\`setVolume Fail: ${err}\`);
});

#### on('statusChange')20+

on(type: 'statusChange', callback: Callback<AudioLoopbackStatus>): void

Subscribes to the audio loopback status change event, which is triggered when the status of the audio loopback is changed. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Capturer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'statusChange'** is triggered when the status of the audio loopback is changed. |
| callback | Callback<[AudioLoopbackStatus](../enums/document.md#audioloopbackstatus20)\> | Yes | Callback used to return the audio loopback status. |

**Error codes**

For details about the error codes, see [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6800101 | Parameter verification failed. |

**Example**

audioLoopback.on('statusChange', (status: audio.AudioLoopbackStatus) => {
  if (status == audio.AudioLoopbackStatus.UNAVAILABLE\_DEVICE) {
    console.info('audio loopback status is: UNAVAILABLE\_DEVICE');
  } else if (status == audio.AudioLoopbackStatus.UNAVAILABLE\_SCENE) {
    console.info('audio loopback status is: UNAVAILABLE\_SCENE');
  } else if (status == audio.AudioLoopbackStatus.AVAILABLE\_IDLE) {
    console.info('audio loopback status is: AVAILABLE\_IDLE');
  } else if (status == audio.AudioLoopbackStatus.AVAILABLE\_RUNNING) {
    console.info('audio loopback status is: AVAILABLE\_RUNNING');
  }
});

#### off('statusChange')20+

off(type: 'statusChange', callback?: Callback<AudioLoopbackStatus>): void

Unsubscribes from the audio loopback status event. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Capturer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'statusChange'** is triggered when the status of the audio loopback is changed. |
| callback | Callback<[AudioLoopbackStatus](../enums/document.md#audioloopbackstatus20)\> | No | Callback used to return the audio loopback status. |

**Error codes**

For details about the error codes, see [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6800101 | Parameter verification failed. |

**Example**

// Cancel all subscriptions to the event.
audioLoopback.off('statusChange');

// For the same event, if the callback parameter passed to the off API is the same as that passed to the on API, the off API cancels the subscription registered with the specified callback parameter.
let statusChangeCallback = (status: audio.AudioLoopbackStatus) => {
  if (status == audio.AudioLoopbackStatus.UNAVAILABLE\_DEVICE) {
    console.info('audio loopback status is: UNAVAILABLE\_DEVICE');
  } else if (status == audio.AudioLoopbackStatus.UNAVAILABLE\_SCENE) {
    console.info('audio loopback status is: UNAVAILABLE\_SCENE');
  } else if (status == audio.AudioLoopbackStatus.AVAILABLE\_IDLE) {
    console.info('audio loopback status is: AVAILABLE\_IDLE');
  } else if (status == audio.AudioLoopbackStatus.AVAILABLE\_RUNNING) {
    console.info('audio loopback status is: AVAILABLE\_RUNNING');
  }
};

audioLoopback.on('statusChange', statusChangeCallback);

audioLoopback.off('statusChange', statusChangeCallback);

#### enable20+

enable(enable: boolean): Promise<boolean>

Enables or disables audio loopback. This API uses a promise to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Capturer

**Required permissions**: ohos.permission.MICROPHONE

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| enable | boolean | Yes | Whether to enable or disable audio loopback. **true** to enable, **false** otherwise. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return the result, indicating whether the API call is successful. **true** is successful, **false** otherwise. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 6800101 | Parameter verification failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

audioLoopback.enable(true).then((isSuccess) => {
  if (isSuccess) {
    console.info('audio loopback enable success');
  } else {
    console.info('audio loopback enable fail');
  }
}).catch((err: BusinessError) => {
  console.error(\`ERROR: ${err}\`);
});

#### setReverbPreset21+

setReverbPreset(preset: AudioLoopbackReverbPreset): boolean

Sets the reverb mode for audio loopback.

**System capability**: SystemCapability.Multimedia.Audio.Capturer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| preset | [AudioLoopbackReverbPreset](../enums/document.md#audioloopbackreverbpreset21) | Yes | Reverb mode. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Setting result. **true** if successful, **false** otherwise. |

**Error codes**

For details about the error codes, see [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6800101 | Parameter verification failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
try {
  audioLoopback.setReverbPreset(audio.AudioLoopbackReverbPreset.THEATER);
} catch (err) {
  console.error(\`setReverbPreset :ERROR: ${err}\`);
}

#### getReverbPreset21+

getReverbPreset(): AudioLoopbackReverbPreset

Obtains the reverb mode of audio loopback.

**System capability**: SystemCapability.Multimedia.Audio.Capturer

**Return value**

| Type | Description |
| :-- | :-- |
| [AudioLoopbackReverbPreset](../enums/document.md#audioloopbackreverbpreset21) | 
Reverb mode.

If no reverb mode has been set, the default reverb mode is **THEATER**.

 |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
try {
  let reverbPreset = audioLoopback.getReverbPreset();
} catch (err) {
  console.error(\`getReverbPreset:ERROR: ${err}\`);
}

#### setEqualizerPreset21+

setEqualizerPreset(preset: AudioLoopbackEqualizerPreset): boolean

Sets the equalizer type for audio loopback.

**System capability**: SystemCapability.Multimedia.Audio.Capturer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| preset | [AudioLoopbackEqualizerPreset](../enums/document.md#audioloopbackequalizerpreset21) | Yes | Equalizer type. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Setting result. **true** if successful, **false** otherwise. |

**Error codes**

For details about the error codes, see [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6800101 | Parameter verification failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
try {
  audioLoopback.setEqualizerPreset(audio.AudioLoopbackEqualizerPreset.FULL);
} catch (err) {
  console.error(\`setEqualizerPreset :ERROR: ${err}\`);
}

#### getEqualizerPreset21+

getEqualizerPreset(): AudioLoopbackEqualizerPreset

Obtains the equalizer type of audio loopback.

**System capability**: SystemCapability.Multimedia.Audio.Capturer

**Return value**

| Type | Description |
| :-- | :-- |
| [AudioLoopbackEqualizerPreset](../enums/document.md#audioloopbackequalizerpreset21) | 
Equalizer type.

If no equalizer type has been set, the default equalizer type is **FULL**.

 |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
try {
  let reverbPreset = audioLoopback.getEqualizerPreset();
} catch (err) {
  console.error(\`getEqualizerPreset:ERROR: ${err}\`);
}
