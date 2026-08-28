# Deprecated Interface (AudioPlayer, deprecated)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/IlO4BnAqSHurz0WazuqPvg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062437Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D5B613A20787A5A7AABB0B5FE37EF3AA438E73D695B24552BC7EDA9DC7301D31)

This API is supported since API version 6 and deprecated since API version 9. You are advised to use [AVPlayer](../interface-avplayer/document.md) instead.

AudioPlayer is a class for audio playback management. It provides APIs to manage and play audio. Before calling any API in AudioPlayer, you must use [createAudioPlayer()](../functions/document.md#mediacreateaudioplayerdeprecated) to create an AudioPlayer instance.

#### Modules to Import

import { media } from '@kit.MediaKit';

#### Properties(deprecated)

**System capability**: SystemCapability.Multimedia.Media.AudioPlayer

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| src | string | No | No | 
Audio file URI. The mainstream audio formats (M4A, AAC, MP3, OGG, WAV, and AMR) are supported.

**Example of supported URLs**:

1\. FD: fd://xx

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/2y5JTyyKR2mwHdqefEg3Fw/en-us_image_0000002568686121.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062437Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BEC4A7E815702C7ED7DF4CE2728EB6F3CAEBE4E9667FB5B96365F9F4C14964C9)

2\. HTTP: http://xx

3\. HTTPS: https://xx

4\. HLS: http://xx or https://xx

**Required permissions**: ohos.permission.READ\_MEDIA or ohos.permission.INTERNET

 |
| fdSrc9+ | [AVFileDescriptor](../interfaces-others/document.md#avfiledescriptor9) | No | No | 

Description of the audio file. This property is required when audio assets of an application are continuously stored in a file.

**Example:**

Assume that a music file that stores continuous music assets consists of the following:

Music 1 (address offset: 0, byte length: 100)

Music 2 (address offset: 101; byte length: 50)

Music 3 (address offset: 151, byte length: 150)

1\. To play music 1: AVFileDescriptor { fd = resource handle; offset = 0; length = 100; }

2\. To play music 2: AVFileDescriptor { fd = resource handle; offset = 101; length = 50; }

3\. To play music 3: AVFileDescriptor { fd = resource handle; offset = 151; length = 150; }

To play an independent music file, use **src=fd://xx**.

 |
| loop | boolean | No | No | Whether to loop audio playback. **true** to loop, **false** otherwise. |
| audioInterruptMode9+ | [audio.InterruptMode](../../../../audio-kit/arkts-apis/ohos-multimedia-audio-audio-management/enums/document.md#interruptmode9) | No | Yes | Audio interruption mode. |
| currentTime | number | Yes | No | Current audio playback position, in ms. |
| duration | number | Yes | No | Audio duration, in ms. |
| state | [AudioState](../types/document.md#audiostatedeprecated) | Yes | No | Audio playback state. This state cannot be used as the condition for triggering the call of **play()**, **pause()**, or **stop()**. |

#### play(deprecated)

play(): void

Starts to play an audio asset. This API can be called only after the **'dataLoad'** event is triggered.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/SEkhEPFjRNqCGDg6Ho3w9w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062437Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=90ED3F27691151288BCF5953F7C98A54FE4B7DC5C4111BB85F504CC08F5C5E3F)

This API is supported since API version 6 and deprecated since API version 9. You are advised to use [AVPlayer.play](../interface-avplayer/document.md#play9) instead.

**System capability**: SystemCapability.Multimedia.Media.AudioPlayer

**Example**

audioPlayer.on('play', () => {    // Set the 'play' event callback.
  console.info('audio play called');
});
audioPlayer.play();

#### pause(deprecated)

pause(): void

Pauses audio playback.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/J3dmgpKsQRGMWS4pMwCAGw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062437Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DCCA357D283EBFD3E9F136098F02EBDDC1DCDE8C156E425D4F3034BE89A23120)

This API is supported since API version 6 and deprecated since API version 9. You are advised to use [AVPlayer.pause](../interface-avplayer/document.md#pause9) instead.

**System capability**: SystemCapability.Multimedia.Media.AudioPlayer

**Example**

audioPlayer.on('pause', () => {    // Set the 'pause' event callback.
  console.info('audio pause called');
});
audioPlayer.pause();

#### stop(deprecated)

stop(): void

Stops audio playback.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/L_FivyC_RoOcHdOc-kWSSw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062437Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=64D70296862BEB3C2FA2BB57F4D84B015F4784A199A4A63B250AEF194806A0A6)

This API is supported since API version 6 and deprecated since API version 9. You are advised to use [AVPlayer.stop](../interface-avplayer/document.md#stop9) instead.

**System capability**: SystemCapability.Multimedia.Media.AudioPlayer

**Example**

audioPlayer.on('stop', () => {    // Set the 'stop' event callback.
  console.info('audio stop called');
});
audioPlayer.stop();

#### reset(deprecated)

reset(): void

Resets the audio asset to be played.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/FZPCh5L3Q82QUP0udlC64w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062437Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B364952650094D9C7EFF68287D00E68C54D68D6C76E56FAFFF94D08F8C3EF9F5)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [AVPlayer.reset](../interface-avplayer/document.md#reset9) instead.

**System capability**: SystemCapability.Multimedia.Media.AudioPlayer

**Example**

audioPlayer.on('reset', () => {    // Set the 'reset' event callback.
  console.info('audio reset called');
});
audioPlayer.reset();

#### seek(deprecated)

seek(timeMs: number): void

Seeks to the specified playback position.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/9RUlgbEtR3GcSyLnt4Pw8w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062437Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=75D27A08686DB47CADE9B9F3A0E2B9F57C73995EBB25E1D230FEC158414BE3E3)

This API is supported since API version 6 and deprecated since API version 9. You are advised to use [AVPlayer.seek](../interface-avplayer/document.md#seek9) instead.

**System capability**: SystemCapability.Multimedia.Media.AudioPlayer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| timeMs | number | Yes | Position to seek to, in ms. The value range is \[0, duration\]. |

**Example**

audioPlayer.on('timeUpdate', (seekDoneTime: number) => {    // Set the 'timeUpdate' event callback.
  if (seekDoneTime == null) {
    console.error('Failed to seek');
    return;
  }
  console.info('Succeeded in seek. seekDoneTime: ' + seekDoneTime);
});
audioPlayer.seek(30000); // Seek to 30000 ms.

#### setVolume(deprecated)

setVolume(vol: number): void

Sets the volume.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/iD7Jv7QhQJeQbWcvZoRWCQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062437Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=596F53E1ACB4940468F7A49089327E27A0B28010F6215B7171B77FA8D82CD00F)

This API is supported since API version 6 and deprecated since API version 9. You are advised to use [AVPlayer.setVolume](../interface-avplayer/document.md#setvolume9) instead.

**System capability**: SystemCapability.Multimedia.Media.AudioPlayer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| vol | number | Yes | Relative volume. The value ranges from 0.00 to 1.00. The value **1.00** indicates the maximum volume (100%). |

**Example**

audioPlayer.on('volumeChange', () => {    // Set the 'volumeChange' event callback.
  console.info('audio volumeChange called');
});
audioPlayer.setVolume(1);    // Set the volume to 100%.

#### release(deprecated)

release(): void

Releases the audio playback resources.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/44FGmR4gRsWolcTqV2wWlA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062437Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=60BF561C800ADC5723C2C16E27A22E6D26D3E4D18FD3E8E8F2A46BC85E8FCE02)

This API is supported since API version 6 and deprecated since API version 9. You are advised to use [AVPlayer.release](../interface-avplayer/document.md#release9) instead.

**System capability**: SystemCapability.Multimedia.Media.AudioPlayer

**Example**

audioPlayer.release();
audioPlayer = undefined;

#### getTrackDescription(deprecated)

getTrackDescription(callback: AsyncCallback<Array<MediaDescription>>): void

Obtains the audio track information. It can be called only after the **'dataLoad'** event is triggered. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/w3QE1ptAQdKF9PFriSRiNQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062437Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A90D56A8B23768526DFA83C5BBCDCFA58202F52A389F495509B809826D481B36)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [AVPlayer.getTrackDescription](../interface-avplayer/document.md#gettrackdescription9) instead.

**System capability**: SystemCapability.Multimedia.Media.AudioPlayer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<Array<[MediaDescription](../interfaces-others/document.md#mediadescription8)\>> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the MediaDescription array obtained; otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

audioPlayer.getTrackDescription((error: BusinessError, arrList: Array<media.MediaDescription>) => {
  if (arrList != null) {
    console.info('Succeeded in getting TrackDescription');
  } else {
    console.error(\`Failed to get TrackDescription, error:${error}\`);
  }
});

#### getTrackDescription(deprecated)

getTrackDescription(): Promise<Array<MediaDescription>>

Obtains the audio track information. It can be called only after the **'dataLoad'** event is triggered. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/8Uf5F0TGQqyGwNHvsLxodQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062437Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7A995E5B00B401DBEDDE8CB34C44BFA0F488FF9FCA6478CC7D3B3DE04125420E)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [AVPlayer.getTrackDescription](../interface-avplayer/document.md#gettrackdescription9-1) instead.

**System capability**: SystemCapability.Multimedia.Media.AudioPlayer

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<[MediaDescription](../interfaces-others/document.md#mediadescription8)\>> | Promise used to return a **MediaDescription** array, which records the audio track information. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

audioPlayer.getTrackDescription().then((arrList: Array<media.MediaDescription>) => {
  console.info('Succeeded in getting TrackDescription');
}).catch((error: BusinessError) => {
  console.error(\`Failed to get TrackDescription, error:${error}\`);
});

#### on('bufferingUpdate')(deprecated)

on(type: 'bufferingUpdate', callback: (infoType: BufferingInfoType, value: number) => void): void

Subscribes to the audio buffering update event. This API works only under online playback.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/DE0aj9sKQhKFcN5N-cyCZQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062437Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CF25E1314025214A51A1F697671020E0A666A2644A67A2345BE2D2A7C642D434)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [AVPlayer.on('bufferingUpdate')](../interface-avplayer/document.md#onbufferingupdate9) instead.

**System capability**: SystemCapability.Multimedia.Media.AudioPlayer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which is **'bufferingUpdate'** in this case. |
| callback | function | Yes | 
Callback invoked when the event is triggered.

The value of [BufferingInfoType](../enums/document.md#bufferinginfotype8) is fixed at **0**.

 |

**Example**

audioPlayer.on('bufferingUpdate', (infoType: media.BufferingInfoType, value: number) => {
  console.info('audio bufferingInfo type: ' + infoType);
  console.info('audio bufferingInfo value: ' + value);
});

#### on('play' | 'pause' | 'stop' | 'reset' | 'dataLoad' | 'finish' | 'volumeChange')(deprecated)

on(type: 'play' | 'pause' | 'stop' | 'reset' | 'dataLoad' | 'finish' | 'volumeChange', callback: () => void): void

Subscribes to the audio playback events.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/hLUZoqkgTNquIv9v5YfVsg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062437Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E3EEED27243CBF70BFCCE5F28BD73BEFF291681446D2839069246806E448FDB4)

This API is supported since API version 6 and deprecated since API version 9. You are advised to use [AVPlayer.on('stateChange')](../interface-avplayer/document.md#onstatechange9) instead.

**System capability**: SystemCapability.Multimedia.Media.AudioPlayer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type. The following events are supported:

\- 'play': triggered when the [play()](#playdeprecated) API is called and audio playback starts.

\- 'pause': triggered when the [pause()](#pausedeprecated) API is called and audio playback is paused.

\- 'stop': triggered when the [stop()](#stopdeprecated) API is called and audio playback stops.

\- 'reset': triggered when the [reset()](#resetdeprecated) API is called and audio playback is reset.

\- 'dataLoad': triggered when the audio data is loaded, that is, when the **src** property is configured.

\- 'finish': triggered when the audio playback is finished.

\- 'volumeChange': triggered when the [setVolume()](#setvolumedeprecated) API is called and the playback volume is changed.

 |
| callback | () => void | Yes | Callback invoked when the event is triggered. |

**Example**

import { fileIo as fs } from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';

let audioPlayer: media.AudioPlayer = media.createAudioPlayer();  // Create an AudioPlayer instance.
audioPlayer.on('dataLoad', () => {            // Set the 'dataLoad' event callback, which is triggered when the src property is set successfully.
  console.info('audio set source called');
  audioPlayer.play();                       // Start the playback and trigger the 'play' event callback.
});
audioPlayer.on('play', () => {                // Set the 'play' event callback.
  console.info('audio play called');
  audioPlayer.seek(30000);                  // Call the seek() API and trigger the 'timeUpdate' event callback.
});
audioPlayer.on('pause', () => {               // Set the 'pause' event callback.
  console.info('audio pause called');
  audioPlayer.stop();                       // Stop the playback and trigger the 'stop' event callback.
});
audioPlayer.on('reset', () => {               // Set the 'reset' event callback.
  console.info('audio reset called');
  audioPlayer.release();                    // Release the AudioPlayer instance.
  audioPlayer = undefined;
});
audioPlayer.on('timeUpdate', (seekDoneTime: number) => {  // Set the 'timeUpdate' event callback.
  if (seekDoneTime == null) {
    console.error('Failed to seek');
    return;
  }
  console.info('Succeeded in seek, and seek time is ' + seekDoneTime);
  audioPlayer.setVolume(0.5);                // Set the volume to 50% and trigger the 'volumeChange' event callback.
});
audioPlayer.on('volumeChange', () => {         // Set the 'volumeChange' event callback.
  console.info('audio volumeChange called');
  audioPlayer.pause();                       // Pause the playback and trigger the 'pause' event callback.
});
audioPlayer.on('finish', () => {               // Set the 'finish' event callback.
  console.info('audio play finish');
  audioPlayer.stop();                        // Stop the playback and trigger the 'stop' event callback.
});
audioPlayer.on('error', (error: BusinessError) => {  // Set the 'error' event callback.
  console.error(\`audio error called, error: ${error}\`);
});

// Set the FD (local playback) of the audio file selected by the user.
let fdPath = 'fd://';
// The stream in the path can be pushed to the device by running the "hdc file send D:\\xxx\\01.mp3 /data/accounts/account\_0/appdata" command.
let path = '/data/accounts/account\_0/appdata/ohos.xxx.xxx.xxx/01.mp3';
fs.open(path).then((file) => {
  fdPath = fdPath + '' + file.fd;
  console.info('Succeeded in opening fd, fd is' + fdPath);
  audioPlayer.src = fdPath;  // Set the src property and trigger the 'dataLoad' event callback.
}, (err: BusinessError) => {
  console.error('Failed to open fd, err is' + err);
}).catch((err: BusinessError) => {
  console.error('Failed to open fd, err is' + err);
});

#### on('timeUpdate')(deprecated)

on(type: 'timeUpdate', callback: Callback<number>): void

Subscribes to the **'timeUpdate'** event. This event is reported every second when the audio playback is in progress.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/BhUPtHPBS4K-Dje0uDBxaA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062437Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=239F0EBE162C2684D49C89719F1A2C38B5C4E42F501815C990A7598ADE47AF08)

This API is supported since API version 6 and deprecated since API version 9. You are advised to use [AVPlayer.on('timeUpdate')](../interface-avplayer/document.md#ontimeupdate9) instead.

**System capability**: SystemCapability.Multimedia.Media.AudioPlayer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type, which is **'timeUpdate'** in this case.

The **'timeUpdate'** event is triggered when the audio playback starts after an audio playback timestamp update.

 |
| callback | Callback<number> | Yes | Callback invoked when the event is triggered. The input parameter is the updated timestamp. |

**Example**

audioPlayer.on('timeUpdate', (newTime: number) => {    // Set the 'timeUpdate' event callback.
  if (newTime == null) {
    console.error('Failed to do timeUpdate');
    return;
  }
  console.info('Succeeded in doing timeUpdate. seekDoneTime: ' + newTime);
});
audioPlayer.play();    // The 'timeUpdate' event is triggered when the playback starts.

#### on('audioInterrupt')(deprecated)

on(type: 'audioInterrupt', callback: (info: audio.InterruptEvent) => void): void

Subscribes to the audio interruption event. For details, see [audio.InterruptEvent](../../../../audio-kit/arkts-apis/ohos-multimedia-audio-audio-management/interfaces-others/document.md#interruptevent9).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/jyn8CYeZSQOezwnd-PDZrA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062437Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=30BB2F83790FCE5E51F4A363D18633F5AE1ED3EDDD187CFF8C6B2FFCBDCEC7F7)

This API is supported since API version 9 and deprecated since API version 9. You are advised to use [AVPlayer.on('audioInterrupt')](../interface-avplayer/document.md#onaudiointerrupt9) instead.

**System capability**: SystemCapability.Multimedia.Media.AudioPlayer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which is **'audioInterrupt'** in this case. |
| callback | function | Yes | Callback invoked when the event is triggered. |

**Example**

import { audio } from '@kit.AudioKit';

audioPlayer.on('audioInterrupt', (info: audio.InterruptEvent) => {
  console.info('audioInterrupt called,and InterruptEvent info is:' + info);
});

#### on('error')(deprecated)

on(type: 'error', callback: ErrorCallback): void

Subscribes to audio playback error events. After an error event is reported, you must handle the event and exit the playback.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/MZkFvhhpSAmTM2xnJEYy_Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062437Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3372FC6E6BBFF11F5B1596A2EDAA41E40B2DAC149DB912453516C4659EB7023C)

This API is supported since API version 6 and deprecated since API version 9. You are advised to use [AVPlayer.on('error')](../interface-avplayer/document.md#onerror9) instead.

**System capability**: SystemCapability.Multimedia.Media.AudioPlayer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type, which is **'error'** in this case.

This event is triggered when an error occurs during audio playback.

 |
| callback | [ErrorCallback](../../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#errorcallback) | Yes | Callback invoked when the event is triggered. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

audioPlayer.on('error', (error: BusinessError) => {  // Set the 'error' event callback.
  console.error(\`audio error called, error: ${error}\`);
});
audioPlayer.setVolume(3); // Set volume to an invalid value to trigger the 'error' event.
