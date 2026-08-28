# Types

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/JRiKV9L-QqyqAbTZjL032w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062314Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BBF13B2683D418F266D1ED89261CAC4D028228E0AEF41C30CAF41ECB7FDAD16E)

-   The initial APIs of this module are supported since API version 9. Updates will be marked with a superscript to indicate their earliest API version.
    
-   The sample effect is subject to the actual device.
    

#### WebMessage

type WebMessage = ArrayBuffer | string

Defines the data types supported by [WebMessagePort](../interface-webmessageport/document.md).

**System capability**: SystemCapability.Web.Webview.Core

| Type | Description |
| :-- | :-- |
| string | String type. |
| ArrayBuffer | Binary type. |

#### OnProxyConfigChangeCallback15+

type OnProxyConfigChangeCallback = () => void

Defines a callback triggered when the proxy is set successfully.

**System capability**: SystemCapability.Web.Webview.Core

**Example**

For details about the sample code, see [removeProxyOverride](../class-proxycontroller/document.md#removeproxyoverride15).

#### CreateNativeMediaPlayerCallback12+

type CreateNativeMediaPlayerCallback = (handler: NativeMediaPlayerHandler, mediaInfo: MediaInfo) => NativeMediaPlayerBridge

Defines a **CreateNativeMediaPlayerCallback** object used as a parameter of the [onCreateNativeMediaPlayer](../class-webviewcontroller/document.md#oncreatenativemediaplayer12) callback. This object is used to create a player to take over media playback of the web page.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| handler | [NativeMediaPlayerHandler](../interface-nativemediaplayerhandler/document.md) | Yes | Object used to report the player status to the ArkWeb engine. |
| mediaInfo | [MediaInfo](../interfaces-others/document.md#mediainfo12) | Yes | Information about the media on the web page. |

**Return value**

| Type | Description |
| :-- | :-- |
| [NativeMediaPlayerBridge](../interface-nativemediaplayerbridge/document.md) | 
Instance of the interface class between the player that takes over web media and the ArkWeb kernel.

The application needs to implement this interface class.

The ArkWeb engine uses an object of this interface class to control the player created by the application to take over web page media.

If the application returns **null**, the application does not take over the media playback, and the media will be played by the ArkWeb engine.

 |

**Example**

For details about the sample code, see [onCreateNativeMediaPlayer](../class-webviewcontroller/document.md#oncreatenativemediaplayer12).
