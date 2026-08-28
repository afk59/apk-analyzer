# Interface (NativeMediaPlayerBridge)

Instance of the API class between the web media player and the ArkWeb kernel.

The ArkWeb kernel uses an object of this interface class to control the player created by the application to take over web page media.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/SeACyf9USZGvlsSIYq8T2g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062314Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EFBA8514DCCFAF47492D5581D8BE354A23D4F53BE03541E906712707CED3B0DC)

-   The initial APIs of this module are supported since API version 9. Updates will be marked with a superscript to indicate their earliest API version.
    
-   The initial APIs of this interface are supported since API version 12.
    
-   The sample effect is subject to the actual device.
    

#### updateRect12+

updateRect(x: number, y: number, width: number, height: number): void

Updates the surface position information.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| x | number | Yes | X coordinate of the surface relative to the **Web** component. |
| y | number | Yes | Y coordinate of the surface relative to the **Web** component. |
| width | number | Yes | 
Width of the surface.

Unit: pixel

 |
| height | number | Yes | 

Height of the surface.

Unit: pixel

 |

**Example**

For details about the sample code, see [onCreateNativeMediaPlayer](../class-webviewcontroller/document.md#oncreatenativemediaplayer12).

#### play12+

play(): void

Plays this video.

**System capability**: SystemCapability.Web.Webview.Core

**Example**

For details about the sample code, see [onCreateNativeMediaPlayer](../class-webviewcontroller/document.md#oncreatenativemediaplayer12).

#### pause12+

pause(): void

Pauses playback.

**System capability**: SystemCapability.Web.Webview.Core

**Example**

For details about the sample code, see [onCreateNativeMediaPlayer](../class-webviewcontroller/document.md#oncreatenativemediaplayer12).

#### seek12+

seek(targetTime: number): void

Seeks to a specific time point in the media.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| targetTime | number | Yes | 
Target time point.

Unit: second

 |

**Example**

For details about the sample code, see [onCreateNativeMediaPlayer](../class-webviewcontroller/document.md#oncreatenativemediaplayer12).

#### setVolume12+

setVolume(volume: number): void

Sets the playback volume.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| volume | number | Yes | 
Playback volume.

Value range: \[0, 1.0\]. The value **0** indicates mute, and the value **1.0** indicates the maximum volume.

 |

**System capability**: SystemCapability.Web.Webview.Core

**Example**

For details about the sample code, see [onCreateNativeMediaPlayer](../class-webviewcontroller/document.md#oncreatenativemediaplayer12).

#### setMuted12+

setMuted(muted: boolean): void

Sets the muted status.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| muted | boolean | Yes | 
Whether to mute the player.

The value **true** means to mute the player, and **false** means the opposite.

 |

**Example**

For details about the sample code, see [onCreateNativeMediaPlayer](../class-webviewcontroller/document.md#oncreatenativemediaplayer12).

#### setPlaybackRate12+

setPlaybackRate(playbackRate: number): void

Sets the playback rate.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| playbackRate | number | Yes | 
Playback rate.

Value range: \[0, 10.0\]. The value **1** indicates the original speed of playback.

 |

**Example**

For details about the sample code, see [onCreateNativeMediaPlayer](../class-webviewcontroller/document.md#oncreatenativemediaplayer12).

#### release12+

release(): void

Releases this player.

**System capability**: SystemCapability.Web.Webview.Core

**Example**

For details about the sample code, see [onCreateNativeMediaPlayer](../class-webviewcontroller/document.md#oncreatenativemediaplayer12).

#### enterFullscreen12+

enterFullscreen(): void

Enables the player to enter full screen mode.

**System capability**: SystemCapability.Web.Webview.Core

**Example**

For details about the sample code, see [onCreateNativeMediaPlayer](../class-webviewcontroller/document.md#oncreatenativemediaplayer12).

#### exitFullscreen12+

exitFullscreen(): void

Enables the player to exit full screen mode.

**System capability**: SystemCapability.Web.Webview.Core

**Example**

For details about the sample code, see [onCreateNativeMediaPlayer](../class-webviewcontroller/document.md#oncreatenativemediaplayer12).

#### resumePlayer12+

resumePlayer?(): void

Resumes the player and its status information.

**System capability**: SystemCapability.Web.Webview.Core

**Example**

For details about the sample code, see [onCreateNativeMediaPlayer](../class-webviewcontroller/document.md#oncreatenativemediaplayer12).

#### suspendPlayer12+

suspendPlayer?(type: SuspendType): void

Suspends the player and save its status information.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SuspendType](../enums/document.md#suspendtype12) | Yes | Suspension type of the player. |

**Example**

For details about the sample code, see [onCreateNativeMediaPlayer](../class-webviewcontroller/document.md#oncreatenativemediaplayer12).
