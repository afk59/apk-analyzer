# Interfaces (Others)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/YVS_Hq6ySvmgaC6nyVKhug/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062424Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9910D3A84C2EA917ADA1DEB46B1CA70C133DCBD08C9E50D7A715BCDDD4153971)

The initial APIs of this module are supported since API version 9. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### AVCastControlCommand10+

Describes the command that can be received by a cast controller.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.AVCast

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| command | [AVCastControlCommandType](../types/document.md#avcastcontrolcommandtype10) | No | No | Command. The parameters carried in each command are different. For details, see [AVCastControlCommandType](../types/document.md#avcastcontrolcommandtype10). |
| parameter | [media.PlaybackSpeed](../../../../media-kit/arkts-apis/ohos-multimedia-media-media/enums/document.md#playbackspeed8) | number | string | [LoopMode](../enums/document.md#loopmode10) | No | Yes | Parameters carried in the command. |

#### CastDisplayInfo12+

Describes the information about the cast display in the case of extended screens.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.ExtendedDisplayCast

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| id | number | No | No | ID of the cast display. The value must be an integer. |
| name | string | No | No | Name of the cast display. |
| state | [CastDisplayState](../enums/document.md#castdisplaystate12) | No | No | State of the cast display. |
| width | number | No | No | Screen width of the cast display, in px. The value must be an integer. |
| height | number | No | No | Screen height of the cast display, in px. The value must be an integer. |

#### AVMetadata10+

Describes the media metadata.

**System capability**: SystemCapability.Multimedia.AVSession.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| assetId | string | No | No | 
Media asset ID. It is the unique ID of a song and defined by the application. If this property changes, all other metadata properties will be refreshed.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| title | string | No | Yes | 

Title.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| artist | string | No | Yes | 

Artist.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| author | string | No | Yes | 

Author.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| avQueueName12+ | string | No | Yes | Playlist name. |
| avQueueId11+ | string | No | Yes | Unique ID of the playlist. |
| avQueueImage11+ | [image.PixelMap](../../../../image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md) | string | No | Yes | 

Cover image of the playlist,

which can be pixel data of an image or an image path (local path or network path). Applications call **setAVMetadata** to set the image data.

\- If the data type is set to **PixelMap**, the data obtained by calling **getAVMetadata** is the pixel data of an image.

\- If the data type is set to **url**, the data obtained is an image path.

 |
| album | string | No | Yes | 

Album name.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| writer | string | No | Yes | 

Writer.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| composer | string | No | Yes | composer. |
| duration | number | No | Yes | 

Media duration, in ms.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| mediaImage | [image.PixelMap](../../../../image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md) | string | No | Yes | 

Pixel data of an image or an image path (local path or network path). Applications call **setAVMetadata** to set the image data.

\- If the data type is set to **PixelMap**, the data obtained by calling **getAVMetadata** is the pixel data of an image.

\- If the data type is set to **url**, the data obtained is an image path.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| bundleIcon18+ | [image.PixelMap](../../../../image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md) | Yes | Yes | Pixel data of the image that is used as the application icon. It is read-only and cannot be set on the application side. |
| publishDate | Date | No | Yes | Release date. |
| subtitle | string | No | Yes | 

Subtitle.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| description | string | No | Yes | 

Media description.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| lyric | string | No | Yes | 

Lyrics. The application needs to combine the lyrics into a string.

The string length must be less than 40,960 bytes.

**NOTE**: The system supports lyrics in the simple LRC format. If the lyrics are not standard (for example, having duplicate timestamps), the lyrics fail to be parsed and cannot be displayed properly in the system.

 |
| singleLyricText17+ | string | No | Yes | 

Lyrics of a single media asset. The application must combine the lyrics into a string (excluding the timestamp).

The string length must be less than 40,960 bytes.

**Atomic service API**: This API can be used in atomic services since API version 17.

 |
| previousAssetId | string | No | Yes | 

ID of the previous media asset.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| nextAssetId | string | No | Yes | 

ID of the next media asset.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| filter11+ | number | No | Yes | 

Protocol supported by the media session. The default value is **TYPE\_CAST\_PLUS\_STREAM**. For details, see [ProtocolType](../enums/document.md#protocoltype11).

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| drmSchemes12+ | Array<string> | No | Yes | DRM scheme supported by the media session. The value is the UUID of the DRM scheme. |
| skipIntervals11+ | [SkipIntervals](../enums/document.md#skipintervals11) | No | Yes | Intervals supported for fast-forwarding and rewinding. The default value is **SECONDS\_15**, that is, 15 seconds. |
| displayTags11+ | number | No | Yes | Display tags of the media asset. For details, see [DisplayTag](../enums/document.md#displaytag11). |

#### AVMediaDescription10+

Describes the properties related to the media metadata in the playlist.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| assetId | string | No | No | 
Media ID in the playlist.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| title | string | No | Yes | 

Name of the media asset in the playlist.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| subtitle | string | No | Yes | 

Subname of the media asset in the playlist. This property is not supported in audio casting scenarios where the Cast+ protocol is used.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| description | string | No | Yes | 

Description of the media asset in the playlist.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| mediaImage | [image.PixelMap](../../../../image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md) | string | No | Yes | 

Pixel data of the media image for the playback list.

When the input parameter is of the string type:

\- Only network URIs are supported for setting the cover. Local URIs are not supported.

\- This parameter serves the same purpose as the **albumCoverUri** attribute, but takes precedence over it.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| extras | {\[key: string\]: Object;} | No | Yes | 

Additional fields of the media asset in the playlist.

**System capability**: SystemCapability.Multimedia.AVSession.Core

 |
| mediaUri | string | No | Yes | 

URI of the media asset in the playlist.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| mediaType | string | No | Yes | 

Type of the media asset in the playlist.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| mediaSize | number | No | Yes | 

Size of the media asset in the playlist.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| albumTitle | string | No | Yes | 

Album name of the media asset in the playlist.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| albumCoverUri | string | No | Yes | 

URI of the album cover of the media asset in the playlist.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| lyricContent | string | No | Yes | 

Lyric content of the media asset in the playlist.

The string length must be less than 40,960 bytes.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| lyricUri | string | No | Yes | 

Lyric URI of the media asset in the playlist.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| artist | string | No | Yes | 

Author of the lyric of the media asset in the playlist.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| fdSrc | [media.AVFileDescriptor](../../../../media-kit/arkts-apis/ohos-multimedia-media-media/interfaces-others/document.md#avfiledescriptor9) | No | Yes | 

Handle to the local media file in the playlist.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| dataSrc12+ | [media.AVDataSrcDescriptor](../../../../media-kit/arkts-apis/ohos-multimedia-media-media/interfaces-others/document.md#avdatasrcdescriptor10) | No | Yes | 

Descriptor of the data source in the playlist.

**System capability**: SystemCapability.Multimedia.AVSession.Core

 |
| pcmSrc20+ | boolean | No | Yes | 

Whether the playlist uses a PCM data source. **true** if the PCM data source used, **false** otherwise.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Atomic service API**: This API can be used in atomic services since API version 20.

 |
| drmScheme12+ | string | No | Yes | 

DRM scheme supported by the playlist. The value is the UUID of the DRM scheme.

**System capability**: SystemCapability.Multimedia.AVSession.Core

 |
| duration | number | No | Yes | 

Playback duration of the media asset in the playlist.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| startPosition | number | No | Yes | 

Start position for playing the media asset in the playlist.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| creditsPosition | number | No | Yes | 

Position for playing the closing credits of the media asset in the playlist.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| appName | string | No | Yes | 

Name of the application provided by the playlist.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| displayTags11+ | number | No | Yes | 

Display tags of the media asset. For details, see [DisplayTag](../enums/document.md#displaytag11). This property is not supported in audio casting scenarios where the Cast+ protocol is used.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| launchClientData20+ | string | No | Yes | 

Custom data sent by the application to the receiver during casting.

**System capability**: SystemCapability.Multimedia.AVSession.AVCast

**Atomic service API**: This API can be used in atomic services since API version 20.

 |

#### AVQueueItem10+

Describes the properties of an item in the playlist.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| itemId | number | No | No | ID of an item in the playlist. |
| description | [AVMediaDescription](#avmediadescription10) | No | Yes | Media metadata of the item in the playlist. |

#### AVPlaybackState10+

Describes the information related to the media playback state.

**System capability**: SystemCapability.Multimedia.AVSession.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| state | [PlaybackState](../enums/document.md#playbackstate10) | No | Yes | 
Playback state.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| speed | number | No | Yes | 

Playback speed.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| position | [PlaybackPosition](#playbackposition10) | No | Yes | 

Playback position.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| bufferedTime | number | No | Yes | 

Buffered time.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| loopMode | [LoopMode](../enums/document.md#loopmode10) | No | Yes | 

Loop mode.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| isFavorite | boolean | No | Yes | 

Whether the media asset is marked as a favorite. **true** if marked, **false** otherwise.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| activeItemId | number | No | Yes | 

ID of the item that is being played.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| volume | number | No | Yes | 

Media volume.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| maxVolume11+ | number | No | Yes | 

Maximum volume.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| muted11+ | boolean | No | Yes | 

Whether the media asset is muted. **true** if muted, **false** otherwise.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| duration11+ | number | No | Yes | Duration of the media asset. |
| videoWidth11+ | number | No | Yes | 

Video width of the media asset, in px.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| videoHeight11+ | number | No | Yes | 

Video height of the media asset, in px.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| extras | {\[key: string\]: Object;} | No | Yes | 

Custom media data.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |

#### PlaybackPosition10+

Describes the information related to the playback position.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| elapsedTime | number | No | No | Elapsed time, in ms. |
| updateTime | number | No | No | Updated time, in ms. |

#### CallMetadata11+

Describes the properties related to call metadata.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| name | string | No | Yes | Name (alias) of the caller. |
| phoneNumber | string | No | Yes | Phone number of the caller. |
| avatar | [image.PixelMap](../../../../image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md) | No | Yes | Profile picture of the caller. |

#### AVCallState11+

Describes the properties related to the call state.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| state | [CallState](../enums/document.md#callstate11) | No | No | Call state. |
| muted | boolean | No | No | Whether the microphone is muted. **true** if muted, **false** otherwise. |

#### DeviceInfo10+

Describes the information related to the output device.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| castCategory | [AVCastCategory](../enums/document.md#avcastcategory10) | No | No | 
Cast category.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| deviceId | string | No | No | 

ID of the output device.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| deviceName | string | No | No | 

Name of the output device.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| deviceType | DeviceType | No | No | 

Type of the output device.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| supportedProtocols11+ | number | No | Yes | 

Protocol supported by the output device. The default value is **TYPE\_LOCAL**. For details, see [ProtocolType](../enums/document.md#protocoltype11).

**System capability**: SystemCapability.Multimedia.AVSession.AVCast

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| supportedDrmCapabilities12+ | Array<string> | No | Yes | 

DRM capability supported by the output device.

**System capability**: SystemCapability.Multimedia.AVSession.AVCast

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| manufacturer13+ | string | No | Yes | 

Manufacturer of the output device.

**System capability**: SystemCapability.Multimedia.AVSession.AVCast

**Atomic service API**: This API can be used in atomic services since API version 13.

 |
| modelName13+ | string | No | Yes | 

Model name of the output device.

**System capability**: SystemCapability.Multimedia.AVSession.AVCast

**Atomic service API**: This API can be used in atomic services since API version 13.

 |
| audioCapabilities20+ | [AudioCapabilities](#audiocapabilities20) | No | Yes | 

Audio capabilities supported by the output device.

**System capability**: SystemCapability.Multimedia.AVSession.AVCast

**Atomic service API**: This API can be used in atomic services since API version 20.

 |
| supportedPullClients20+ | Array<number> | No | Yes | 

IDs of supported pull clients. (This field is returned only for devices that support 4K casting.)

**System capability**: SystemCapability.Multimedia.AVSession.AVCast

**Atomic service API**: This API can be used in atomic services since API version 20.

 |

#### OutputDeviceInfo10+

Describes the information related to the output device.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| devices | Array<[DeviceInfo](#deviceinfo10)\> | No | No | Output devices. |

#### AVControlCommand10+

Describes the command that can be received by the session.

**System capability**: SystemCapability.Multimedia.AVSession.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| command | [AVControlCommandType](../types/document.md#avcontrolcommandtype10) | No | No | 
Command. (Different commands correspond to different parameters.)

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| parameter | [LoopMode](../enums/document.md#loopmode10) | string | number | No | Yes | 

Parameters carried in the command.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| commandInfo22+ | [CommandInfo](#commandinfo22) | No | Yes | Command information. |

#### AVCastPickerOptions14+

Describes the configurable attributes of a casting component that is called.

**System capability**: SystemCapability.Multimedia.AVSession.AVCast

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| sessionType | [AVSessionType](../types/document.md#avsessiontype10) | No | Yes | 
Session type. The default value is **audio**.

Currently, only **audio** and **video** are supported. If **voice\_call** or **video\_call** is passed, **audio** is used by default.

**Atomic service API**: This API can be used in atomic services since API version 14.

 |
| pickerStyle22+ | [AVCastPickerStyle](../../ohos-multimedia-avcastpickerparam-avcastpicker-parameters/document.md#avcastpickerstyle12) | No | Yes | Component style. |
| menuPosition22+ | [MenuPosition](#menuposition-22) | No | Yes | This parameter can be set when the value of **pickerStyle** is **STYLE\_MENU** |

#### AudioCapabilities20+

Describes the audio capabilities supported by the casting device.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Multimedia.AVSession.AVCast

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| streamInfos | Array<[audio.AudioStreamInfo](../../../../audio-kit/arkts-apis/ohos-multimedia-audio-audio-management/interfaces-others/document.md#audiostreaminfo8)\> | Yes | No | Audio capability parameters. |

#### CommandInfo22+

Describes the command information to be sent to the session.

**System capability**: SystemCapability.Multimedia.AVSession.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| callerBundleName | string | No | Yes | Bundle name of the caller. |
| callerModuleName | string | No | Yes | Module name of the caller. |
| callerDeviceId | string | No | Yes | Device IP address of the caller. |
| callerType | [CallerType](../enums/document.md#callertype22) | No | Yes | Source of the caller. |

#### MenuPosition 22+

Defines the position of a component that can pop up a menu.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.Multimedia.AVSession.AVCast

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| x | number | No | No | Position coordinate of a component on the X axis. The unit is vp. |
| y | number | No | No | Position coordinate of a component on the Y axis. The unit is vp. |
| width | number | No | No | Component width. The unit is vp. |
| height | number | No | No | Component height. The unit is vp. |
