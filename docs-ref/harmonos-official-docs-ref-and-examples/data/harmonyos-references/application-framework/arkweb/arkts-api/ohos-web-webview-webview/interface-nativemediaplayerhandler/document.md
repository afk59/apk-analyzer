# Interface (NativeMediaPlayerHandler)

Implements a **NativeMediaPlayerHandler** object used as a parameter of the [CreateNativeMediaPlayerCallback](../types/document.md#createnativemediaplayercallback12) callback. The application uses this object to report the player status to the ArkWeb engine.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/l7nf3A9cQrq-VNHJgQ6SfA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062314Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=15A1364BB891FAAF4AC38A3EB81E45833AB81F095E88C89DD3E403951F7BE51A)

-   The initial APIs of this module are supported since API version 9. Updates will be marked with a superscript to indicate their earliest API version.
    
-   The initial APIs of this interface are supported since API version 12.
    
-   The sample effect is subject to the actual device.
    

#### handleStatusChanged12+

handleStatusChanged(status: PlaybackStatus): void

Called to notify the ArkWeb engine of the playback status of the player when the playback status changes.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| status | [PlaybackStatus](../enums/document.md#playbackstatus12) | Yes | Player status. |

**Example**

For details about the sample code, see [onCreateNativeMediaPlayer](../class-webviewcontroller/document.md#oncreatenativemediaplayer12).

#### handleVolumeChanged12+

handleVolumeChanged(volume: number): void

Called to notify the ArkWeb engine of the volume of the player when the volume changes.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| volume | number | Yes | Volume of the player. The value range is \[0, 1.0\]. |

**Example**

For details about the sample code, see [onCreateNativeMediaPlayer](../class-webviewcontroller/document.md#oncreatenativemediaplayer12).

#### handleMutedChanged12+

handleMutedChanged(muted: boolean): void

Called to notify the ArkWeb engine of the muted status of the player when the muted status changes.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| muted | boolean | Yes | 
Whether the player is muted.

The value **true** indicates that the player is muted, and **false** indicates the opposite.

 |

**Example**

For details about the sample code, see [onCreateNativeMediaPlayer](../class-webviewcontroller/document.md#oncreatenativemediaplayer12).

#### handlePlaybackRateChanged12+

handlePlaybackRateChanged(playbackRate: number): void

Called to notify the ArkWeb engine of the playback rate of the player when the playback rate changes.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| playbackRate | number | Yes | Playback rate. The value range is \[0, +∞). |

**Example**

For details about the sample code, see [onCreateNativeMediaPlayer](../class-webviewcontroller/document.md#oncreatenativemediaplayer12).

#### handleDurationChanged12+

handleDurationChanged(duration: number): void

Called to notify the ArkWeb engine of the total duration of the media.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| duration | number | Yes | 
Total duration of the media.

Unit: second. Value range: \[0,+∞)

 |

**Example**

For details about the sample code, see [onCreateNativeMediaPlayer](../class-webviewcontroller/document.md#oncreatenativemediaplayer12).

#### handleTimeUpdate12+

handleTimeUpdate(currentPlayTime: number): void

Called to notify the ArkWeb engine of the playback progress when the playback progress changes.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| currentPlayTime | number | Yes | 
Current progress.

Unit: second. Value range: \[0, duration\]

 |

**Example**

For details about the sample code, see [onCreateNativeMediaPlayer](../class-webviewcontroller/document.md#oncreatenativemediaplayer12).

#### handleBufferedEndTimeChanged12+

handleBufferedEndTimeChanged(bufferedEndTime: number): void

Called to notify the ArkWeb engine of the buffer time when the buffer time changes.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| bufferedEndTime | number | Yes | 
Duration of media data in the buffer.

Unit: second. Value range: \[0, duration\]

 |

**Example**

For details about the sample code, see [onCreateNativeMediaPlayer](../class-webviewcontroller/document.md#oncreatenativemediaplayer12).

#### handleEnded12+

handleEnded(): void

Called to notify the ArkWeb engine that the media playback ends.

**System capability**: SystemCapability.Web.Webview.Core

**Example**

For details about the sample code, see [onCreateNativeMediaPlayer](../class-webviewcontroller/document.md#oncreatenativemediaplayer12).

#### handleNetworkStateChanged12+

handleNetworkStateChanged(state: NetworkState): void

Called to notify the ArkWeb engine of the network status of the player when the network status changes.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| state | [NetworkState](../enums/document.md#networkstate12) | Yes | Network status of the player. |

**Example**

For details about the sample code, see [onCreateNativeMediaPlayer](../class-webviewcontroller/document.md#oncreatenativemediaplayer12).

#### handleReadyStateChanged12+

handleReadyStateChanged(state: ReadyState): void

Called to notify the ArkWeb engine of the cache status of the player when the cache status changes.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| state | [ReadyState](../enums/document.md#readystate12) | Yes | Cache status of the player. |

**Example**

For details about the sample code, see [onCreateNativeMediaPlayer](../class-webviewcontroller/document.md#oncreatenativemediaplayer12).

#### handleFullscreenChanged12+

handleFullscreenChanged(fullscreen: boolean): void

Called to notify the ArkWeb engine of the full screen status of the player when the full screen status changes.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| fullscreen | boolean | Yes | 
Whether the player is in full screen.

The value **true** means that the player is in full screen, and **false** means the opposite.

 |

**Example**

For details about the sample code, see [onCreateNativeMediaPlayer](../class-webviewcontroller/document.md#oncreatenativemediaplayer12).

#### handleSeeking12+

handleSeeking(): void

Called to notify the ArkWeb engine that the player enters the seek state.

**System capability**: SystemCapability.Web.Webview.Core

**Example**

For details about the sample code, see [onCreateNativeMediaPlayer](../class-webviewcontroller/document.md#oncreatenativemediaplayer12).

#### handleSeekFinished12+

handleSeekFinished(): void

Called to notify the ArkWeb engine that the seek operation is complete.

**System capability**: SystemCapability.Web.Webview.Core

**Example**

For details about the sample code, see [onCreateNativeMediaPlayer](../class-webviewcontroller/document.md#oncreatenativemediaplayer12).

#### handleError12+

handleError(error: MediaError, errorMessage: string): void

Called to notify the ArkWeb engine that an error occurs with the player.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| error | [MediaError](../enums/document.md#mediaerror12) | Yes | Error object type. |
| errorMessage | string | Yes | Error message. |

**Example**

For details about the sample code, see [onCreateNativeMediaPlayer](../class-webviewcontroller/document.md#oncreatenativemediaplayer12).

#### handleVideoSizeChanged12+

handleVideoSizeChanged(width: number, height: number): void

Called to notify the ArkWeb engine of the video size of the player.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| width | number | Yes | Video width, in pixels. Value range: \[0,+∞) |
| height | number | Yes | Video height, in pixels. Value range: \[0,+∞) |

**Example**

For details about the sample code, see [onCreateNativeMediaPlayer](../class-webviewcontroller/document.md#oncreatenativemediaplayer12).
