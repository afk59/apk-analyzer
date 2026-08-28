# Types

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/sFkeyRPqQumnS9ZIH_nW-g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062437Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D874BFA16E9E0A7776A85A710DD183B3EAC21226654900E121813CF9BCF8C90D)

The initial APIs of this module are supported since API version 6. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### SoundPool10+

type SoundPool = \_SoundPool

SoundPool, which provides APIs for loading, unloading, playing, and stopping playing system sounds, setting the volume, and setting the number of loops.

**System capability**: SystemCapability.Multimedia.Media.SoundPool

| Type | Description |
| :-- | :-- |
| [\_SoundPool](../../multimedia/soundpool-sound-pool/document.md#soundpool) | Provides APIs for loading, unloading, playing, and stopping playing system sounds, setting the volume, and setting the number of loops. |

#### PlayParameters10+

type PlayParameters = \_PlayParameters

Describes the playback parameters of the sound pool.

**System capability**: SystemCapability.Multimedia.Media.SoundPool

| Type | Description |
| :-- | :-- |
| [\_PlayParameters](../../multimedia/soundpool-sound-pool/document.md#playparameters) | Playback parameters of the sound pool. |

#### AVPlayerState9+

type AVPlayerState = 'idle' | 'initialized' | 'prepared' | 'playing' | 'paused' | 'completed' | 'stopped' | 'released' | 'error'

Describes the state of the [AVPlayer](../interface-avplayer/document.md). Your application can proactively obtain the AVPlayer state through the **state** property or obtain the reported AVPlayer state by subscribing to the [stateChange](../interface-avplayer/document.md#onstatechange9) event. For details about the rules for state transition, see [Audio Playback](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/using-avplayer-for-playback).

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Multimedia.Media.AVPlayer

| Type | Description |
| :-- | :-- |
| 'idle' | 
The AVPlayer enters this state after [createAVPlayer()](../functions/document.md#mediacreateavplayer9) or [reset()](../interface-avplayer/document.md#reset9) is called.

In case [createAVPlayer()](../functions/document.md#mediacreateavplayer9) is used, all properties are set to their default values.

In case [reset()](../interface-avplayer/document.md#reset9) is called, the **url9+**, **fdSrc9+**, or **dataSrc10+** property and the **loop** property are reset, and other properties are retained.

 |
| 'initialized' | The AVPlayer enters this state after **url9+** or **fdSrc9+** property is set in the idle state. In this case, you can configure static properties such as the window and audio. |
| 'prepared' | The AVPlayer enters this state when [prepare()](../interface-avplayer/document.md#prepare9) is called in the initialized state. In this case, the playback engine has prepared the resources. |
| 'playing' | The AVPlayer enters this state when [play()](../interface-avplayer/document.md#play9) is called in the prepared, paused, or completed state. |
| 'paused' | The AVPlayer enters this state when **pause()** is called in the playing state. |
| 'completed' | The AVPlayer enters this state when a media asset finishes playing and loop playback is not set (no **loop = true**). In this case, if [play()](../interface-avplayer/document.md#play9) is called, the AVPlayer enters the playing state and replays the media asset; if [stop()](../interface-avplayer/document.md#stop9) is called, the AVPlayer enters the stopped state. |
| 'stopped' | The AVPlayer enters this state when [stop()](../interface-avplayer/document.md#stop9) is called in the prepared, playing, paused, or completed state. In this case, the playback engine retains the properties but releases the memory resources. You can call [prepare()](../interface-avplayer/document.md#prepare9) to prepare the resources again, call [reset()](../interface-avplayer/document.md#reset9) to reset the properties, or call [release()](../interface-avplayer/document.md#release9) to destroy the playback engine. |
| 'released' | The AVPlayer enters this state when [release()](../interface-avplayer/document.md#release9) is called. The playback engine associated with the AVPlayer instance is destroyed, and the playback process ends. This is the final state. |
| 'error' | 

The AVPlayer enters this state when an irreversible error occurs in the playback engine. You can call [reset()](../interface-avplayer/document.md#reset9) to reset the properties or call [release()](../interface-avplayer/document.md#release9) to destroy the playback engine. For details about the error codes, see [Media Error Codes](../../../error-codes/media-error-codes/document.md).

**NOTE**

Distinguishing the error state from the [on('error')](../interface-avplayer/document.md#onerror9) state:

1\. When the AVPlayer enters the error state, the **on('error')** event is triggered. You can obtain the detailed error information through this event.

2\. When the AVPlayer enters the error state, the playback service stops. This requires the client to design a fault tolerance mechanism to call [reset()](../interface-avplayer/document.md#reset9) or [release()](../interface-avplayer/document.md#release9).

3\. The client receives **on('error')** event but the AVPlayer does not enter the error state. This situation occurs due to either of the following reasons:

Cause 1: The client calls an API in an incorrect state or passes in an incorrect parameter, and the AVPlayer intercepts the call. If this is the case, the client must correct its code logic.

Cause 2: A stream error is detected during playback. As a result, the container and decoding are abnormal for a short period of time, but continuous playback and playback control operations are not affected. If this is the case, the client does not need to design a fault tolerance mechanism.

 |

#### OnTrackChangeHandler12+

type OnTrackChangeHandler = (index: number, isSelected: boolean) => void

Describes the callback invoked for the track change event.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.Media.AVPlayer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| index | number | Yes | Index of the track that has changed. |
| isSelected | boolean | Yes | Whether the track at the current index is selected. **true** if selected, **false** otherwise. |

#### OnAVPlayerStateChangeHandle12+

type OnAVPlayerStateChangeHandle = (state: AVPlayerState, reason: StateChangeReason) => void

Describes the callback invoked for the AVPlayer state change event.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.Media.AVPlayer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| state | [AVPlayerState](#avplayerstate9) | Yes | State of the AVPlayer. |
| reason | [StateChangeReason](../enums/document.md#statechangereason9) | Yes | Reason for the state change. |

#### OnBufferingUpdateHandler12+

type OnBufferingUpdateHandler = (infoType: BufferingInfoType, value: number) => void

Describes the callback invoked for the buffering update event.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.Media.AVPlayer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| infoType | [BufferingInfoType](../enums/document.md#bufferinginfotype8) | Yes | Buffering information type. |
| value | number | Yes | Value of the buffering information type. |

#### OnVideoSizeChangeHandler12+

type OnVideoSizeChangeHandler = (width: number, height: number) => void

Describes the callback invoked for the video size change event.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.Media.AVPlayer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| width | number | Yes | Video width, in px. |
| height | number | Yes | Video height, in px. |

#### OnSuperResolutionChanged 18+

type OnSuperResolutionChanged = (enabled: boolean) => void

Describes the callback used to listen for video super resolution status changes. If super resolution is enabled by using [PlaybackStrategy](../interfaces-others/document.md#playbackstrategy12), this callback is invoked to report the super resolution status changes. It is also invoked to report the initial status when the video starts. However, this callback is not invoked when super resolution is not enabled.

Super resolution is automatically disabled in either of the following cases:

-   The current super resolution algorithm only works with videos that have a frame rate of 30 fps or lower. If the video frame rate exceeds 30 fps, or if the input frame rate exceeds the processing capability of the super resolution algorithm in scenarios such as fast playback, super resolution is automatically disabled.
-   The current super resolution algorithm supports input resolutions from 320 × 320 to 1920 × 1080, in px. If the input video resolution exceeds the range during playback, super resolution is automatically disabled.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.Multimedia.Media.AVPlayer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| enabled | boolean | Yes | Whether super resolution is enabled. **true** if enabled, **false** otherwise. |

#### OnSeiMessageHandle18+

type OnSeiMessageHandle = (messages: Array<SeiMessage>, playbackPosition?: number) => void

Describes the handle used to obtain SEI messages. This is used when in subscriptions to SEI message events, and the callback returns detailed SEI information.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.Multimedia.Media.AVPlayer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| messages | Array<[SeiMessage](../interfaces-others/document.md#seimessage18)\> | Yes | Array of SEI messages. |
| playbackPosition | number | No | Current playback position, in milliseconds. |

#### OnPlaybackRateDone20+

type OnPlaybackRateDone = (rate: number) => void

Describes the callback invoked for the event indicating that the playback rate setting is complete.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Multimedia.Media.AVPlayer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| rate | number | Yes | Playback rate. |

#### AVRecorderState9+

type AVRecorderState = 'idle' | 'prepared' | 'started' | 'paused' | 'stopped' | 'released' | 'error'

Enumerates the AVRecorder states. You can obtain the state through the **state** property.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.Media.AVRecorder

| Type | Description |
| :-- | :-- |
| 'idle' | The AVRecorder enters this state after it is just created or the [AVRecorder.reset()](../interface-avrecorder/document.md#reset9) API is called when the AVRecorder is in any state except released. In this state, you can call [AVRecorder.prepare()](../interface-avrecorder/document.md#prepare9) to set recording parameters. The AVRecorder enters this state after it is just created or the [AVRecorder.reset()](../interface-avrecorder/document.md#reset9) API is called when the AVRecorder is in any state except released. |
| 'prepared' | The AVRecorder enters this state when the parameters are set. In this state, you can call [AVRecorder.start()](../interface-avrecorder/document.md#start9) to start recording. |
| 'started' | The AVRecorder enters this state when the recording starts. In this state, you can call [AVRecorder.pause()](../interface-avrecorder/document.md#pause9) to pause recording or call [AVRecorder.stop()](../interface-avrecorder/document.md#stop9) to stop recording. |
| 'paused' | The AVRecorder enters this state when the recording is paused. In this state, you can call [AVRecorder.resume()](../interface-avrecorder/document.md#resume9) to continue recording or call [AVRecorder.stop()](../interface-avrecorder/document.md#stop9) to stop recording. |
| 'stopped' | The AVRecorder enters this state when the recording stops. In this state, you can call [AVRecorder.prepare()](../interface-avrecorder/document.md#prepare9) to set recording parameters so that the AVRecorder enters the prepared state again. |
| 'released' | The AVRecorder enters this state when the recording resources are released. In this state, no operation can be performed. In any other state, you can call [AVRecorder.release()](../interface-avrecorder/document.md#release9) to enter the released state. |
| 'error' | The AVRecorder enters this state when an irreversible error occurs in the AVRecorder instance. In this state, the [AVRecorder.on('error') event](../interface-avrecorder/document.md#onerror9) is reported, with the detailed error cause. In the error state, you must call [AVRecorder.reset()](../interface-avrecorder/document.md#reset9) to reset the AVRecorder instance or call [AVRecorder.release()](../interface-avrecorder/document.md#release9) to release the resources. |

#### OnAVRecorderStateChangeHandler12+

type OnAVRecorderStateChangeHandler = (state: AVRecorderState, reason: StateChangeReason) => void

Describes the callback invoked for the AVRecorder state change event.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.Media.AVRecorder

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| state | [AVRecorderState](#avrecorderstate9) | Yes | AVRecorder state. |
| reason | [StateChangeReason](../enums/document.md#statechangereason9) | Yes | Reason for the state change. |

#### SourceOpenCallback18+

type SourceOpenCallback = (request: MediaSourceLoadingRequest) => number

This callback function is implemented by applications to handle resource open requests and return a unique handle for the opened resource.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/clopyPTjQ5S0L2DvaHESRg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062437Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F7A1D03381230FFB31BEDC4E668C6985CCAF1C903F3DDA6EE7E4070736C57B65)

The client must return the handle immediately after processing the request.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.Multimedia.Media.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| request | [MediaSourceLoadingRequest](../interface-mediasourceloadingrequest/document.md) | Yes | Parameters for the resource open request, including detailed information about the requested resource and the data push method. |

**Return value**

| Type | Description |
| :-- | :-- |
| number | 
Handle for the current resource open request. A value greater than 0 means the request is successful, whereas a value less than or equal to 0 means it fails.

\- The handle for the request object is unique.

 |

**Example**

import { HashMap } from '@kit.ArkTS';
import { media } from '@kit.MediaKit';

let uuid: number = 1;
let requests: HashMap<number, media.MediaSourceLoadingRequest> = new HashMap();

let sourceOpenCallback: media.SourceOpenCallback = (request: media.MediaSourceLoadingRequest) => {
  console.info(\`Opening resource: ${request.url}\`);
  // Open the resource and return a unique handle, ensuring the mapping between the UUID and request.
  uuid += 1;
  requests.set(uuid, request);
  return uuid;
};

#### SourceReadCallback18+

type SourceReadCallback = (uuid: number, requestedOffset: number, requestedLength: number) => void

This callback function is implemented by applications to handle resource read requests. When data is available, applications should push it to the player using the [respondData](../interface-mediasourceloadingrequest/document.md#responddata18) API of the corresponding MediaSourceLoadingRequest object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/1vT_V183TfW58WyTz3VMQg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062437Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7B820DC676EE18C84582AF13B6B81AE6AE9AD7FEAE9F61681F5C626BDB18B339)

The client must return the handle immediately after processing the request.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.Multimedia.Media.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| uuid | number | Yes | ID for the resource handle. |
| requestedOffset | number | Yes | Offset of the current media data relative to the start of the resource. |
| requestedLength | number | Yes | Length of the current request. The value **\-1** indicates reaching the end of the resource. After pushing the data, call [finishLoading](../interface-mediasourceloadingrequest/document.md#finishloading18) to notify the player that the push is complete. |

**Example**

let sourceReadCallback: media.SourceReadCallback = (uuid: number, requestedOffset: number, requestedLength: number) => {
  console.info(\`Reading resource with handle ${uuid}, offset: ${requestedOffset}, length: ${requestedLength}\`);
  // Check whether the UUID is valid and store the read request. Avoid blocking the request while pushing data and header information.
};

#### SourceCloseCallback18+

type SourceCloseCallback = (uuid: number) => void

This callback function is implemented by applications to release related resources.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/bydjCMHoS7-nhvZbrUi81g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062437Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B880551EDBF188FB7149660AF48BB77F01946373F86FBD3D5E9D2EA917DC1634)

The client must return the handle immediately after processing the request.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.Multimedia.Media.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| uuid | number | Yes | ID for the resource handle. |

**Example**

import { HashMap } from '@kit.ArkTS';

let requests: HashMap<number, media.MediaSourceLoadingRequest> = new HashMap();

let sourceCloseCallback: media.SourceCloseCallback = (uuid: number) => {
  console.info(\`Closing resource with handle ${uuid}\`);
  // Clear resources related to the current UUID.
  requests.remove(uuid);
};

#### AudioState(deprecated)

type AudioState = 'idle' | 'playing' | 'paused' | 'stopped' | 'error'

Describes the audio playback state. You can obtain the state through the **state** property.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/Xq_yaiD4QUK7ApTGfJpqCw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062437Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=92BD693E82AC31D7881A69BC67E6AE83F697166F05CE20A28F5AF6D3DD37B312)

This API is supported since API version 6 and deprecated since API version 9. You are advised to use [AVPlayerState](#avplayerstate9) instead.

**System capability**: SystemCapability.Multimedia.Media.AudioPlayer

| Type | Description |
| :-- | :-- |
| 'idle' | No audio playback is in progress. The audio player is in this state after the **'dataload'** or **'reset'** event is triggered. |
| 'playing' | Audio playback is in progress. The audio player is in this state after the **'play'** event is triggered. |
| 'paused' | Audio playback is paused. The audio player is in this state after the **'pause'** event is triggered. |
| 'stopped' | Audio playback is stopped. The audio player is in this state after the **'stop'** event is triggered. |
| 'error' | Audio playback is in the error state. |

#### VideoPlayState(deprecated)

type VideoPlayState = 'idle' | 'prepared' | 'playing' | 'paused' | 'stopped' | 'error'

Describes the video playback state. You can obtain the state through the **state** property.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/pcuKHWZgQQCoGVzzCG9MNA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062437Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2E9DD2395903BF4A4FE0550EAC8322C3CFE3D0DA04919083911582EA6B0AFE47)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [AVPlayerState](#avplayerstate9) instead.

**System capability**: SystemCapability.Multimedia.Media.VideoPlayer

| Type | Description |
| :-- | :-- |
| 'idle' | The video player is idle. |
| 'prepared' | Video playback is being prepared. |
| 'playing' | Video playback is in progress. |
| 'paused' | Video playback is paused. |
| 'stopped' | Video playback is stopped. |
| 'error' | The AVRecorder enters this state |
