# Types

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/kWUYu2TYSP6uRAVugb8_Mg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062424Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F59439D4ECCFBCCDF6EC9344E25644357990AB72678C8887D28DDCA4EFABFAFC)

The initial APIs of this module are supported since API version 9. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { avSession } from '@kit.AVSessionKit';

#### AVSessionType10+

type AVSessionType = 'audio' | 'video' | 'voice\_call' | 'video\_call' | 'photo'

Defines the session type supported by the session.

You can use the strings listed in the following table.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

| Type | Description |
| :-- | :-- |
| 'audio' | Audio session. |
| 'video' | Video session. |
| 'voice\_call'11+ | Voice call. |
| 'video\_call'12+ | Video call. |
| 'photo'22+ | Image. |

#### AVCastControlCommandType10+

type AVCastControlCommandType = 'play' | 'pause' | 'stop' | 'playNext' | 'playPrevious' | 'fastForward' | 'rewind' |

'seek' | 'setVolume' | 'setSpeed' | 'setLoopMode' | 'toggleFavorite' | 'toggleMute'

Defines the commands that can be sent by a cast controller.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.AVCast

| Type | Description |
| :-- | :-- |
| 'play' | Play the media. No parameter is required. |
| 'pause' | Pause the playback. No parameter is required. |
| 'stop' | Stop the playback. No parameter is required. |
| 'playNext' | Play the next media asset. No parameter is required. |
| 'playPrevious' | Play the previous media asset. No parameter is required. |
| 'fastForward' | Fast-forward. No parameter is required. |
| 'rewind' | Rewind. No parameter is required. |
| 'seek' | Seek to a playback position. The corresponding parameter is of the number type. |
| 'setVolume' | Set the volume. The corresponding parameter is of the number type. You can use [AVPlaybackState.maxVolume](../interfaces-others/document.md#avplaybackstate10) to obtain the maximum system volume. |
| 'setSpeed' | Set the playback speed. The corresponding parameter is [media.PlaybackSpeed](../../../../media-kit/arkts-apis/ohos-multimedia-media-media/enums/document.md#playbackspeed8). |
| 'setLoopMode' | Set the loop mode. The corresponding parameter is [LoopMode](../enums/document.md#loopmode10). |
| 'toggleFavorite' | Favorite the media asset. The corresponding parameter is [AVMetadata.assetId](../interfaces-others/document.md#avmetadata10). |
| 'toggleMute' | Set the muted status. No parameter is required. |

#### ExtraInfo18+

type ExtraInfo = {\[key: string\]: Object;}

Defines the custom media packet set by the provider.

**System capability**: SystemCapability.Multimedia.AVSession.Core

| Type | Description |
| :-- | :-- |
| {\[key: string\]: Object;} | 
**key** specifies the remote distributed event type. Currently, the following event types are supported:

**AUDIO\_GET\_VOLUME**: obtains the volume of the remote device.

**AUDIO\_GET\_AVAILABLE\_DEVICES**: obtains all remote devices that can be connected.

**AUDIO\_GET\_PREFERRED\_OUTPUT\_DEVICE\_FOR\_RENDERER\_INFO**: obtains the actual remote audio device.

The provider returns the corresponding media packet object based on the event type.

 |

#### KeyRequestCallback12+

type KeyRequestCallback = (assetId: string, requestData: Uint8Array) => void

Defines the callback invoked for the media key request event.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.AVCast

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| assetId | string | Yes | Media asset ID. |
| requestData | Uint8Array | Yes | Data carried in the media key request. |

**Example**

let keyRequestCallback: avSession.KeyRequestCallback = async(assetId: string, requestData: Uint8Array) => {
  console.info(\`Succeeded in keyRequestCallback. assetId: ${assetId}, requestData: ${requestData}\`);
}

#### AVControlCommandType10+

type AVControlCommandType = 'play' | 'pause' | 'stop' | 'playNext' | 'playPrevious' | 'fastForward' | 'rewind' |

'seek' | 'setSpeed' | 'setLoopMode' | 'toggleFavorite' | 'playFromAssetId' | 'playWithAssetId' | 'answer' | 'hangUp' | 'toggleCallMute' | 'setTargetLoopMode'

Defines the commands that can be sent to a session.

You can use the union of the strings listed in the following table.

**System capability**: SystemCapability.Multimedia.AVSession.Core

| Type | Description |
| :-- | :-- |
| 'play' | 
Play the media. No parameter is required.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| 'pause' | 

Pause the playback. No parameter is required.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| 'stop' | 

Stop the playback. No parameter is required.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| 'playNext' | 

Play the next media asset. No parameter is required.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| 'playPrevious' | 

Play the previous media asset. No parameter is required.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| 'fastForward' | 

Fast-forward. For details about the corresponding parameters, see [SkipIntervals](../enums/document.md#skipintervals11).

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| 'rewind' | 

Rewind. For details about the corresponding parameters, see [SkipIntervals](../enums/document.md#skipintervals11).

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| 'seek' | 

Seek to a playback position. The corresponding parameter is of the number type.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| 'setSpeed' | 

Set the playback speed. The corresponding parameter is of the number type.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| 'setLoopMode' | 

Set the loop mode. The corresponding parameter is [LoopMode](../enums/document.md#loopmode10).

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| 'setTargetLoopMode' 18+ | 

Set the target loop mode. The recommended parameter is [LoopMode](../enums/document.md#loopmode10).

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| 'toggleFavorite' | 

Favorite the media asset. The corresponding parameter is [AVMetadata.assetId](../interfaces-others/document.md#avmetadata10).

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| 'playFromAssetId' 11+ | 

Play the media asset with the specified asset ID.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| 'playWithAssetId' 20+ | 

Play the media asset with the specified asset ID. The corresponding parameter is [AVMetadata.assetId](../interfaces-others/document.md#avmetadata10).

The string length must be less than 40960 bytes.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |
| 'answer' 11+ | 

Answer a call. No parameter is required.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| 'hangUp' 11+ | 

The call is disconnecting. No parameter is required.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| 'toggleCallMute' 11+ | 

Set the mute status for a call. No parameter is required.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |

#### NoParamCallback22+

type NoParamCallback = () => void

Defines a callback function type that takes no parameters.

**System capability**: SystemCapability.Multimedia.AVSession.Core

#### TwoParamCallback22+

type TwoParamCallback<T, G> = (data1: T, data2: G) => void

Defines a callback type that takes two parameters.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| data1 | T | Yes | Parameter 1. |
| data2 | G | Yes | Parameter 2. |
