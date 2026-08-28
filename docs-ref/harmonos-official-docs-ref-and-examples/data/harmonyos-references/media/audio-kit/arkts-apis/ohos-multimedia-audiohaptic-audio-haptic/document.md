# @ohos.multimedia.audioHaptic (Audio-Haptic)

Audio-haptic enables users to get rhythmic auditory and haptic feedback while having incoming calls or messages.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/j_ckudvORBuouqqYM9RwLA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062418Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DC2D694F9765445ED8D7532DD8EE3B5DDD6C4B6DC62D7100204C8BC5766F61FD)

The initial APIs of this module are supported since API version 11. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { audioHaptic } from '@kit.AudioKit';

#### audioHaptic.getAudioHapticManager

getAudioHapticManager(): AudioHapticManager

Obtains an AudioHapticManager instance.

**System capability**: SystemCapability.Multimedia.AudioHaptic.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [AudioHapticManager](#audiohapticmanager) | AudioHapticManager instance. |

**Example**

let audioHapticManagerInstance: audioHaptic.AudioHapticManager = audioHaptic.getAudioHapticManager();

#### AudioLatencyMode

Enumerates the audio latency modes.

**System capability**: SystemCapability.Multimedia.AudioHaptic.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| AUDIO\_LATENCY\_MODE\_NORMAL | 0 | Normal latency mode. |
| AUDIO\_LATENCY\_MODE\_FAST | 1 | Low latency mode. This mode is applicable to short audio files. A long audio file may be truncated in this mode. It functions the same as [SoundPool](../../../media-kit/arkts-apis/multimedia/soundpool-sound-pool/document.md#soundpool). |

#### AudioHapticPlayerOptions

Describes the options for the audio-haptic player.

**System capability**: SystemCapability.Multimedia.AudioHaptic.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| muteAudio | boolean | No | Yes | Whether to mute the audio. **true** to mute, **false** otherwise. If this parameter is not specified, the default value **false** is used. |
| muteHaptics | boolean | No | Yes | Whether to mute haptics feedback. **true** to mute, **false** otherwise. If this parameter is not specified, the default value **false** is used. |

#### AudioHapticFileDescriptor20+

Describes the audio-haptic file descriptor.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/3y6lvnKvR2qIFsUhkAW0Pw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062418Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=63807D9C92D864ACEBA778F615ED9D7478120668389BC6BD688547C9F65FCA4A)

Ensure that **fd** is an available file descriptor and the values of **offset** and **length** are correct.

**System capability**: SystemCapability.Multimedia.AudioHaptic.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| fd | number | No | No | File descriptor of the audio-haptic file, which is generally greater than or equal to 0. |
| offset | number | No | Yes | Offset in the file from which data will be read. By default, the offset is 0. |
| length | number | No | Yes | Number of bytes to read. By default, the length is the number of bytes remaining in the file from the offset position. |

#### AudioHapticManager

Manages the audio-haptic feature. Before calling any API in AudioHapticManager, you must use [getAudioHapticManager](#audiohapticgetaudiohapticmanager) to create an AudioHapticManager instance.

#### \[h2\]registerSource

registerSource(audioUri: string, hapticUri: string): Promise<number>

Registers audio and haptic resources via URIs. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/Q4wIrX5vR4mtDyeUQkwa4A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062418Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7A260E28CFB50F99F6B24C136DB0608CB972CDAE902A1107EDF498B609D23F3F)

A maximum of 128 resources can be registered at the same time for an application. Any attempt to register beyond this limit will fail (returning a negative resource ID). You are advised to reasonably manage the number of registered resources. For resources that are no longer used, you are advised to unregister them in a timely manner.

**System capability**: SystemCapability.Multimedia.AudioHaptic.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| audioUri | string | Yes | 
URI of the audio source.

\- For details about the supported audio resource formats and path formats in the normal latency mode, see [AVPlayer](../../../media-kit/arkts-apis/ohos-multimedia-media-media/interface-avplayer/document.md).

\- For details about the supported audio resource formats in the low-latency mode, see [SoundPool](../../../media-kit/arkts-apis/multimedia/soundpool-sound-pool/document.md#soundpool). The path format must meet the requirements described in [fs.open](../../../../application-framework/core-file-kit/arkts-apis/ohos-file-fs-file-management/document.md#fsopen).

\- In both modes, you are advised to pass in the absolute path of the file.

 |
| hapticUri | string | Yes | 

URI of the haptic source.

For details about the supported haptic resource formats, see [HapticFileDescriptor](../../../../system/hardware/sensor-service-kit/arkts-api/ohos-vibrator-vibrator/document.md#hapticfiledescriptor10). The path format must meet the requirements described in [fs.open](../../../../application-framework/core-file-kit/arkts-apis/ohos-file-fs-file-management/document.md#fsopen).

You are advised to pass in the absolute path of the file.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | 
Promise, which returns the registered resource ID.

In normal cases, the returned resource ID is a non-negative number. A negative ID indicates a registration failure. In this case, check whether the number of registered resources exceeds the upper limit.

 |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let audioUri = 'data/audioTest.wav'; // Change it to the URI of the target audio source.
let hapticUri = 'data/hapticTest.json'; // Change it to the URI of the target haptic source.
let id = 0;
// A maximum of 128 resources can be registered at the same time for an application. Any attempt to register beyond this limit will fail (returning a negative resource ID). You are advised to reasonably manage the number of registered resources. For resources that are no longer used, you are advised to unregister them in a timely manner.
audioHapticManagerInstance.registerSource(audioUri, hapticUri).then((value: number) => {
  console.info(\`Promise returned to indicate that the source id of the registered source ${value}.\`);
  id = value;
}).catch((err: BusinessError) => {
  console.error(\`Failed to register source ${err}\`);
});

#### \[h2\]registerSourceFromFd20+

registerSourceFromFd(audioFd: AudioHapticFileDescriptor, hapticFd: AudioHapticFileDescriptor): Promise<number>

Registers audio and haptic resources via file descriptors. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/BvndNqS5Qreu1O-jEeEhhw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062418Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=762EA1E51C1F127C01334B158EEBB77B6435B1F34F8A354D5839B3D7F4D3F362)

A maximum of 128 resources can be registered at the same time for an application. Any attempt to register beyond this limit will fail (returning a negative resource ID). You are advised to reasonably manage the number of registered resources. For resources that are no longer used, you are advised to unregister them in a timely manner.

**System capability**: SystemCapability.Multimedia.AudioHaptic.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| audioFd | [AudioHapticFileDescriptor](#audiohapticfiledescriptor20) | Yes | Valid file descriptor object that has been opened, used to describe the audio file. The offset and length must match the actual file length. |
| hapticFd | [AudioHapticFileDescriptor](#audiohapticfiledescriptor20) | Yes | Valid file descriptor object that has been opened, used to describe the haptic file. The offset and length must match the actual file length. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | 
Promise, which returns the registered resource ID.

In normal cases, the returned resource ID is a non-negative number. A negative ID indicates a registration failure. In this case, check whether the number of registered resources exceeds the upper limit.

 |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;

let audioFile = context.resourceManager.getRawFdSync('audioTest.ogg'); // Use the corresponding file in the rawfile directory.
let audioFd: audioHaptic.AudioHapticFileDescriptor = {
  fd: audioFile.fd,
  offset: audioFile.offset,
  length: audioFile.length,
};

let hapticFile = context.resourceManager.getRawFdSync('hapticTest.json'); // Use the corresponding file in the rawfile directory.
let hapticFd: audioHaptic.AudioHapticFileDescriptor = {
  fd: hapticFile.fd,
  offset: hapticFile.offset,
  length: hapticFile.length,
};
let id = 0;
// A maximum of 128 resources can be registered at the same time for an application. Any attempt to register beyond this limit will fail (returning a negative resource ID). You are advised to reasonably manage the number of registered resources. For resources that are no longer used, you are advised to unregister them in a timely manner.
audioHapticManagerInstance.registerSourceFromFd(audioFd, hapticFd).then((value: number) => {
  console.info('Succeeded in doing registerSourceFromFd.');
  id = value;
}).catch((err: BusinessError) => {
  console.error(\`Failed to registerSourceFromFd. Code: ${err.code}, message: ${err.message}\`);
});

#### \[h2\]unregisterSource

unregisterSource(id: number): Promise<void>

Unregisters an audio-haptic source. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/-h7bcgZiQgm8BE2WLslIUg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062418Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C2B0678B5934F2C86AD26D856F9F0E2DAFF88FDAE713CBABDD00718AC5096310)

For resources that are no longer used, you are advised to unregister them in a timely manner to avoid issues such as resource leaks or the number of resources exceeding the upper limit.

**System capability**: SystemCapability.Multimedia.AudioHaptic.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| id | number | Yes | Source ID. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let id = 0; // The ID is obtained using registerSource.

audioHapticManagerInstance.unregisterSource(id).then(() => {
  console.info('Succeeded in doing unregisterSource.');
}).catch((err: BusinessError) => {
  console.error(\`Failed to unregisterSource. Code: ${err.code}, message: ${err.message}\`);
});

#### \[h2\]setAudioLatencyMode

setAudioLatencyMode(id:number, latencyMode: AudioLatencyMode): void

Sets the latency mode for an audio-haptic source.

**System capability**: SystemCapability.Multimedia.AudioHaptic.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| id | number | Yes | Source ID. |
| latencyMode | [AudioLatencyMode](#audiolatencymode) | Yes | Audio latency mode. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Media Error Codes](../../../media-kit/error-codes/media-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 5400102 | Operation not allowed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let id = 0; // The ID is obtained using registerSource.

let latencyMode: audioHaptic.AudioLatencyMode = audioHaptic.AudioLatencyMode.AUDIO\_LATENCY\_MODE\_FAST;

audioHapticManagerInstance.setAudioLatencyMode(id, latencyMode);

#### \[h2\]setStreamUsage

setStreamUsage(id: number, usage: audio.StreamUsage): void

Sets the stream usage for an audio-haptic source.

**System capability**: SystemCapability.Multimedia.AudioHaptic.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| id | number | Yes | Source ID. |
| usage | [audio.StreamUsage](../ohos-multimedia-audio-audio-management/enums/document.md#streamusage) | Yes | Stream usage. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Media Error Codes](../../../media-kit/error-codes/media-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |
| 5400102 | Operation not allowed. |

**Example**

import { audio } from '@kit.AudioKit';
import { BusinessError } from '@kit.BasicServicesKit';

let id = 0; // The ID is obtained using registerSource.

let usage: audio.StreamUsage = audio.StreamUsage.STREAM\_USAGE\_NOTIFICATION;

audioHapticManagerInstance.setStreamUsage(id, usage);

#### \[h2\]createPlayer

createPlayer(id: number, options?: AudioHapticPlayerOptions): Promise<AudioHapticPlayer>

Creates an audio-haptic player. This API uses a promise to return the result.

**Required permissions**: ohos.permission.VIBRATE

If the audio-haptic player needs to trigger vibration, check whether the application has the permission.

**System capability**: SystemCapability.Multimedia.AudioHaptic.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| id | number | Yes | Source ID. |
| options | [AudioHapticPlayerOptions](#audiohapticplayeroptions) | No | Options of the audio-haptic player. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[AudioHapticPlayer](#audiohapticplayer)\> | Promise used to return the audio-haptic player. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Media Error Codes](../../../media-kit/error-codes/media-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 5400102 | Operation not allowed. |
| 5400103 | I/O error. |
| 5400106 | Unsupport format. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let id = 0; // The ID is obtained using registerSource.

let options: audioHaptic.AudioHapticPlayerOptions = {muteAudio: false, muteHaptics: false};
let audioHapticPlayerInstance: audioHaptic.AudioHapticPlayer | undefined = undefined;

audioHapticManagerInstance.createPlayer(id, options).then((value: audioHaptic.AudioHapticPlayer) => {
  audioHapticPlayerInstance = value;
  console.info('Succeeded in doing createPlayer.');
}).catch((err: BusinessError) => {
  console.error(\`Failed to createPlayer. Code: ${err.code}, message: ${err.message}\`);
});

#### AudioHapticType

Enumerates the audio haptic types.

**System capability**: SystemCapability.Multimedia.AudioHaptic.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| AUDIO\_HAPTIC\_TYPE\_AUDIO | 0 | Audio. |
| AUDIO\_HAPTIC\_TYPE\_HAPTIC | 1 | Haptic. |

#### AudioHapticPlayer

Implements audio-haptic playback. Before calling any API in AudioHapticPlayer, you must use [createPlayer](#createplayer) to create an AudioHapticPlayer instance.

#### \[h2\]isMuted

isMuted(type: AudioHapticType): boolean

Checks whether an audio-haptic type is muted.

**System capability**: SystemCapability.Multimedia.AudioHaptic.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [AudioHapticType](#audiohaptictype) | Yes | Audio-haptic type. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result for whether the audio-haptic type is muted. **true** if muted, **false** otherwise. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Parameter verification failed. |

**Example**

let audioHapticType: audioHaptic.AudioHapticType = audioHaptic.AudioHapticType.AUDIO\_HAPTIC\_TYPE\_AUDIO;

let result: boolean = audioHapticPlayerInstance.isMuted(audioHapticType);

#### \[h2\]start

start(): Promise<void>

Starts playback. This API uses a promise to return the result.

**System capability**: SystemCapability.Multimedia.AudioHaptic.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Media Error Codes](../../../media-kit/error-codes/media-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 5400102 | Operate not permit. |
| 5400103 | IO error. |
| 5400105 | Service died. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

audioHapticPlayerInstance.start().then(() => {
  console.info(\`Promise returned to indicate that start playing successfully.\`);
}).catch((err: BusinessError) => {
  console.error(\`Failed to start playing. ${err}\`);
});

#### \[h2\]stop

stop(): Promise<void>

Stops playback. This API uses a promise to return the result.

**System capability**: SystemCapability.Multimedia.AudioHaptic.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Media Error Codes](../../../media-kit/error-codes/media-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 5400102 | Operate not permit. |
| 5400105 | Service died. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

audioHapticPlayerInstance.stop().then(() => {
  console.info(\`Promise returned to indicate that stop playing successfully.\`);
}).catch((err: BusinessError) => {
  console.error(\`Failed to stop playing. ${err}\`);
});

#### \[h2\]release

release(): Promise<void>

Releases this audio-haptic player. This API uses a promise to return the result.

**System capability**: SystemCapability.Multimedia.AudioHaptic.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Media Error Codes](../../../media-kit/error-codes/media-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 5400105 | Service died. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

audioHapticPlayerInstance.release().then(() => {
  console.info(\`Promise returned to indicate that release the audio haptic player successfully.\`);
}).catch((err: BusinessError) => {
  console.error(\`Failed to release the audio haptic player. ${err}\`);
});

#### \[h2\]setVolume20+

setVolume(volume: number): Promise<void>

Sets the volume for this audio-haptic player. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/_qp7Ha-9QKeCejSa93bGKw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062418Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B048B3D2E24946A17EE5A68C3C87F21AAC0779BF0F8B5FD30723CB63D99E1496)

This API must be called before the audio-haptic player is released.

**System capability**: SystemCapability.Multimedia.AudioHaptic.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| volume | number | Yes | Volume, in the range \[0.00, 1.00\], where 1.00 indicates the maximum volume (100%). |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Media Error Codes](../../../media-kit/error-codes/media-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 5400105 | Service died. |
| 5400102 | Operate not permit in current state. |
| 5400108 | Parameter out of range. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

audioHapticPlayerInstance.setVolume(0.5).then(() => {
  console.info('Promise returned to indicate that set volume successfully.');
}).catch((err: BusinessError) => {
  console.error(\`Failed to set volume. ${err}\`);
});

#### \[h2\]setLoop20+

setLoop(loop: boolean): Promise<void>

Sets this audio-haptic player to play in a loop. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/LP0VNrhaS5Gje1_JAo0e6g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062418Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7ACC4C7D1751CEE6476C5BB3F480CE1B98686E973214378863E22651C9B23990)

This API must be called before the audio-haptic player is released.

**System capability**: SystemCapability.Multimedia.AudioHaptic.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| loop | boolean | Yes | Whether to play in a loop. **true** to play in a loop, **false** otherwise. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Media Error Codes](../../../media-kit/error-codes/media-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 5400102 | Operate not permit in current state. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

audioHapticPlayerInstance.setLoop(true).then(() => {
  console.info('Promise returned to indicate that set player loop successfully.');
}).catch((err: BusinessError) => {
  console.error(\`Failed to set player loop. ${err}\`);
});

#### \[h2\]on('endOfStream')

on(type: 'endOfStream', callback: Callback<void>): void

Subscribes to end of stream (EOS) event, which is triggered when the audio stream playback ends. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.AudioHaptic.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'endOfStream'** is triggered when the audio stream playback ends. |
| callback | Callback<void> | Yes | Callback that returns no value. |

**Example**

audioHapticPlayerInstance.on('endOfStream', () => {
  console.info(\`Receive the callback of endOfStream.\`);
});

#### \[h2\]off('endOfStream')

off(type: 'endOfStream', callback?: Callback<void>): void

Unsubscribes from the EOS event. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.AudioHaptic.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'endOfStream'** is triggered when the audio stream playback ends. |
| callback | Callback<void> | No | Callback that returns no value. |

**Example**

// Cancel all subscriptions to the event.
audioHapticPlayerInstance.off('endOfStream');

// For the same event, if the callback parameter passed to the off API is the same as that passed to the on API, the off API cancels the subscription registered with the specified callback parameter.
let endOfStreamCallback = () => {
  console.info(\`Receive the callback of endOfStream.\`);
};

audioHapticPlayerInstance.on('endOfStream', endOfStreamCallback);

audioHapticPlayerInstance.off('endOfStream', endOfStreamCallback);

#### \[h2\]on('audioInterrupt')

on(type: 'audioInterrupt', callback: Callback<audio.InterruptEvent>): void

Subscribes to the audio interruption event, which is triggered when the audio focus is changed. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.AudioHaptic.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'audioInterrupt'** is triggered when the audio focus is changed. |
| callback | Callback<[audio.InterruptEvent](../ohos-multimedia-audio-audio-management/interfaces-others/document.md#interruptevent9)\> | Yes | Callback used to return the event information. |

**Example**

import { audio } from '@kit.AudioKit';

let isPlaying: boolean; // An identifier specifying whether rendering is in progress.
let isDucked: boolean; // An identifier specifying whether the audio volume is reduced.

audioHapticPlayerInstance.on('audioInterrupt', (interruptEvent: audio.InterruptEvent) => {
  // When an audio interruption event occurs, the audioHapticPlayerInstance receives the interruptEvent callback and performs processing based on the content in the callback.
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
        break;
    }
  }
});

#### \[h2\]off('audioInterrupt')

off(type: 'audioInterrupt', callback?: Callback<audio.InterruptEvent>): void

Unsubscribes from the audio interruption event. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.AudioHaptic.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'audioInterrupt'** is triggered when the audio focus is changed. |
| callback | Callback<[audio.InterruptEvent](../ohos-multimedia-audio-audio-management/interfaces-others/document.md#interruptevent9)\> | No | Callback used to return the event information. |

**Example**

import { audio } from '@kit.AudioKit';

// Cancel all subscriptions to the event.
audioHapticPlayerInstance.off('audioInterrupt');

// For the same event, if the callback parameter passed to the off API is the same as that passed to the on API, the off API cancels the subscription registered with the specified callback parameter.
let isPlaying: boolean; // An identifier specifying whether rendering is in progress.
let isDucked: boolean; // An identifier specifying whether the audio volume is reduced.
let audioInterruptCallback = (interruptEvent: audio.InterruptEvent) => {
  // When an audio interruption event occurs, the audioHapticPlayerInstance receives the interruptEvent callback and performs processing based on the content in the callback.
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
        break;
    }
  }
};

audioHapticPlayerInstance.on('audioInterrupt', audioInterruptCallback);

audioHapticPlayerInstance.off('audioInterrupt', audioInterruptCallback);
