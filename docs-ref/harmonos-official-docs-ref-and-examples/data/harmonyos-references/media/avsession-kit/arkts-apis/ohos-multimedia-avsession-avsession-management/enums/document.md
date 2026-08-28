# Enums

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/CAuu0queT_iXR5oUvcSwAw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062424Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5795D5DB9DDAAC0B763FFF55E833A8D165E694DA79AD3CA6D441CE87B3461EC4)

The initial APIs of this module are supported since API version 9. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### ProtocolType11+

Enumerates the protocol types supported by the remote device.

**System capability**: SystemCapability.Multimedia.AVSession.AVCast

| Name | Value | Description |
| :-- | :-- | :-- |
| TYPE\_LOCAL11+ | 0 | 
Local device, which can be the built-in speaker or audio jack of the device, or an A2DP device.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| TYPE\_CAST\_PLUS\_STREAM11+ | 2 | 

Cast+ stream mode, indicating that the media asset is being displayed on another device.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| TYPE\_DLNA12+ | 4 | 

DLNA protocol, indicating that the media asset is being displayed on another device.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| TYPE\_CAST\_PLUS\_AUDIO20+ | 8 | 

PCM mode, indicating that the media asset is being displayed on another device.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |

#### CastDisplayState12+

Enumerates the states of the cast display.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.ExtendedDisplayCast

| Name | Value | Description |
| :-- | :-- | :-- |
| STATE\_OFF | 1 | The device is disconnected, and the extended screen does not display any content. |
| STATE\_ON | 2 | The device is connected, and the extended screen is available. |

#### CallerType22+

Enumerates the types of sources for the caller.

**System capability**: SystemCapability.Multimedia.AVSession.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| TYPE\_CAST | "cast" | The caller comes from casting. |
| TYPE\_BLUETOOTH | "bluetooth" | The caller comes from Bluetooth. |
| TYPE\_APP | "app" | The caller comes from an application. |
| TYPE\_NEARLINK | "nearlink" | 
The caller comes from NearLink.

**Model restriction**: This API can be used only in the stage model.

 |

#### ConnectionState10+

Enumerates the connection states.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| STATE\_CONNECTING | 0 | The device is connecting. |
| STATE\_CONNECTED | 1 | The device is connected. |
| STATE\_DISCONNECTED | 6 | The device is disconnected. |

#### CallState11+

Enumerates the call states.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| CALL\_STATE\_IDLE | 0 | The phone is idle. |
| CALL\_STATE\_INCOMING | 1 | The phone is ringing. |
| CALL\_STATE\_ACTIVE | 2 | The call is connected. |
| CALL\_STATE\_DIALING | 3 | The caller is dialing. |
| CALL\_STATE\_WAITING | 4 | The call is waiting for connection. |
| CALL\_STATE\_HOLDING | 5 | The call is placed on hold. |
| CALL\_STATE\_DISCONNECTING | 6 | The call is disconnecting. |

#### DisplayTag11+

Enumerates the display tags of the media asset. The display tag is a special type identifier of the media audio source.

**System capability**: SystemCapability.Multimedia.AVSession.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| TAG\_AUDIO\_VIVID | 1 | AUDIO VIVID |

#### DecoderType19+

Enumerates the decoding formats supported by the device.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.AVSession.AVCast

| Name | Value | Description |
| :-- | :-- | :-- |
| OH\_AVCODEC\_MIMETYPE\_VIDEO\_AVC | "video/avc" | VIDEO AVC. |
| OH\_AVCODEC\_MIMETYPE\_VIDEO\_HEVC | "video/hevc" | VIDEO HEVC. |
| OH\_AVCODEC\_MIMETYPE\_AUDIO\_VIVID | "audio/av3a" | AUDIO AV3A. |

#### ResolutionLevel19+

Enumerates the resolution levels supported by the device.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.AVSession.AVCast

| Name | Value | Description |
| :-- | :-- | :-- |
| RESOLUTION\_480P | 0 | 480p (640 x 480 dpi). |
| RESOLUTION\_720P | 1 | 720p (1280 x 720 dpi). |
| RESOLUTION\_1080P | 2 | 1080p (1920 x 1080 dpi). |
| RESOLUTION\_2K | 3 | 2K (2560 x 1440 dpi). |
| RESOLUTION\_4K | 4 | 4K (4096 x 3840 dpi). |

#### AVCastCategory10+

Enumerates the cast categories.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.AVCast

| Name | Value | Description |
| :-- | :-- | :-- |
| CATEGORY\_LOCAL | 0 | Local playback. The sound is played from the local device or a connected Bluetooth headset by default. |
| CATEGORY\_REMOTE | 1 | Remote playback. The sound or images are played from a remote device. |

#### DeviceType10+

Enumerates the output device types.

**Atomic service API**: This API can be used in atomic services since API version 12.

| Name | Value | Description |
| :-- | :-- | :-- |
| DEVICE\_TYPE\_LOCAL | 0 | 
Local device.

**System capability**: SystemCapability.Multimedia.AVSession.Core

 |
| DEVICE\_TYPE\_BLUETOOTH | 10 | 

Bluetooth device.

**System capability**: SystemCapability.Multimedia.AVSession.Core

 |
| DEVICE\_TYPE\_TV | 2 | 

TV.

**System capability**: SystemCapability.Multimedia.AVSession.AVCast

 |
| DEVICE\_TYPE\_SMART\_SPEAKER | 3 | 

Speaker.

**System capability**: SystemCapability.Multimedia.AVSession.AVCast

 |

#### LoopMode10+

Enumerates the loop modes of media playback.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| LOOP\_MODE\_SEQUENCE | 0 | Sequential playback. |
| LOOP\_MODE\_SINGLE | 1 | Single loop. |
| LOOP\_MODE\_LIST | 2 | Playlist loop. |
| LOOP\_MODE\_SHUFFLE | 3 | Shuffle. |
| LOOP\_MODE\_CUSTOM11+ | 4 | Custom playback. |

#### PlaybackState10+

Enumerates the media playback states.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| PLAYBACK\_STATE\_INITIAL | 0 | Initial. |
| PLAYBACK\_STATE\_PREPARE | 1 | Preparing. |
| PLAYBACK\_STATE\_PLAY | 2 | Playing. |
| PLAYBACK\_STATE\_PAUSE | 3 | Paused. |
| PLAYBACK\_STATE\_FAST\_FORWARD | 4 | Fast-forwarding. |
| PLAYBACK\_STATE\_REWIND | 5 | Rewinding. |
| PLAYBACK\_STATE\_STOP | 6 | Stopped. |
| PLAYBACK\_STATE\_COMPLETED | 7 | Playback complete. |
| PLAYBACK\_STATE\_RELEASED | 8 | Released. |
| PLAYBACK\_STATE\_ERROR | 9 | Error. |
| PLAYBACK\_STATE\_IDLE11+ | 10 | Idle. |
| PLAYBACK\_STATE\_BUFFERING11+ | 11 | Buffering. |

#### AVSessionErrorCode10+

Enumerates the error codes used in the media session.

| Name | Value | Description |
| :-- | :-- | :-- |
| ERR\_CODE\_SERVICE\_EXCEPTION | 6600101 | 
The session server is abnormal.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

 |
| ERR\_CODE\_SESSION\_NOT\_EXIST | 6600102 | 

The session does not exist.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

 |
| ERR\_CODE\_CONTROLLER\_NOT\_EXIST | 6600103 | 

The session controller does not exist.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

 |
| ERR\_CODE\_REMOTE\_CONNECTION\_ERR | 6600104 | 

Connection to the remote session fails.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

 |
| ERR\_CODE\_COMMAND\_INVALID | 6600105 | 

The session command is invalid.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

 |
| ERR\_CODE\_SESSION\_INACTIVE | 6600106 | 

The session is not activated.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

 |
| ERR\_CODE\_MESSAGE\_OVERLOAD | 6600107 | 

Too many commands or messages.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

 |
| ERR\_CODE\_DEVICE\_CONNECTION\_FAILED | 6600108 | 

Connection to the device fails.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

 |
| ERR\_CODE\_REMOTE\_CONNECTION\_NOT\_EXIST | 6600109 | 

The remote session does not exist.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

 |
| ERR\_CODE\_CAST\_CONTROL\_UNSPECIFIED13+ | 6611000 | 

An undefined error occurs during cast control.

**Atomic service API**: This API can be used in atomic services since API version 13.

**System capability**: SystemCapability.Multimedia.AVSession.AVCast

 |
| ERR\_CODE\_CAST\_CONTROL\_REMOTE\_ERROR13+ | 6611001 | 

An unknown error occurs in the remote player.

**Atomic service API**: This API can be used in atomic services since API version 13.

**System capability**: SystemCapability.Multimedia.AVSession.AVCast

 |
| ERR\_CODE\_CAST\_CONTROL\_BEHIND\_LIVE\_WINDOW13+ | 6611002 | 

The playback is delayed.

**Atomic service API**: This API can be used in atomic services since API version 13.

**System capability**: SystemCapability.Multimedia.AVSession.AVCast

 |
| ERR\_CODE\_CAST\_CONTROL\_TIMEOUT13+ | 6611003 | 

The cast control process times out.

**Atomic service API**: This API can be used in atomic services since API version 13.

**System capability**: SystemCapability.Multimedia.AVSession.AVCast

 |
| ERR\_CODE\_CAST\_CONTROL\_RUNTIME\_CHECK\_FAILED13+ | 6611004 | 

The runtime check fails.

**Atomic service API**: This API can be used in atomic services since API version 13.

**System capability**: SystemCapability.Multimedia.AVSession.AVCast

 |
| ERR\_CODE\_CAST\_CONTROL\_PLAYER\_NOT\_WORKING13+ | 6611100 | 

Cross-device data transfer is locked.

**Atomic service API**: This API can be used in atomic services since API version 13.

**System capability**: SystemCapability.Multimedia.AVSession.AVCast

 |
| ERR\_CODE\_CAST\_CONTROL\_SEEK\_MODE\_UNSUPPORTED13+ | 6611101 | 

The specified seek mode is not supported.

**Atomic service API**: This API can be used in atomic services since API version 13.

**System capability**: SystemCapability.Multimedia.AVSession.AVCast

 |
| ERR\_CODE\_CAST\_CONTROL\_ILLEGAL\_SEEK\_TARGET13+ | 6611102 | 

The seek position is out of the media range, or the current seek mode is not supported.

**Atomic service API**: This API can be used in atomic services since API version 13.

**System capability**: SystemCapability.Multimedia.AVSession.AVCast

 |
| ERR\_CODE\_CAST\_CONTROL\_PLAY\_MODE\_UNSUPPORTED13+ | 6611103 | 

The specified playback mode is not supported.

**Atomic service API**: This API can be used in atomic services since API version 13.

**System capability**: SystemCapability.Multimedia.AVSession.AVCast

 |
| ERR\_CODE\_CAST\_CONTROL\_PLAY\_SPEED\_UNSUPPORTED13+ | 6611104 | 

The specified playback speed is not supported.

**Atomic service API**: This API can be used in atomic services since API version 13.

**System capability**: SystemCapability.Multimedia.AVSession.AVCast

 |
| ERR\_CODE\_CAST\_CONTROL\_DEVICE\_MISSING13+ | 6611105 | 

Operation failed because the media source device or media receiver device has been destroyed.

**Atomic service API**: This API can be used in atomic services since API version 13.

**System capability**: SystemCapability.Multimedia.AVSession.AVCast

 |
| ERR\_CODE\_CAST\_CONTROL\_INVALID\_PARAM13+ | 6611106 | 

The parameter is invalid.

**Atomic service API**: This API can be used in atomic services since API version 13.

**System capability**: SystemCapability.Multimedia.AVSession.AVCast

 |
| ERR\_CODE\_CAST\_CONTROL\_NO\_MEMORY13+ | 6611107 | 

Failed to allocate memory.

**Atomic service API**: This API can be used in atomic services since API version 13.

**System capability**: SystemCapability.Multimedia.AVSession.AVCast

 |
| ERR\_CODE\_CAST\_CONTROL\_OPERATION\_NOT\_ALLOWED13+ | 6611108 | 

The operation is not allowed.

**Atomic service API**: This API can be used in atomic services since API version 13.

**System capability**: SystemCapability.Multimedia.AVSession.AVCast

 |
| ERR\_CODE\_CAST\_CONTROL\_IO\_UNSPECIFIED13+ | 6612000 | 

An unspecified input/output error occurs.

**Atomic service API**: This API can be used in atomic services since API version 13.

**System capability**: SystemCapability.Multimedia.AVSession.AVCast

 |
| ERR\_CODE\_CAST\_CONTROL\_IO\_NETWORK\_CONNECTION\_FAILED13+ | 6612001 | 

Network connection fails.

**Atomic service API**: This API can be used in atomic services since API version 13.

**System capability**: SystemCapability.Multimedia.AVSession.AVCast

 |
| ERR\_CODE\_CAST\_CONTROL\_IO\_NETWORK\_CONNECTION\_TIMEOUT13+ | 6612002 | 

Network connection times out.

**Atomic service API**: This API can be used in atomic services since API version 13.

**System capability**: SystemCapability.Multimedia.AVSession.AVCast

 |
| ERR\_CODE\_CAST\_CONTROL\_IO\_INVALID\_HTTP\_CONTENT\_TYPE 13+ | 6612003 | 

The value of **Content-Type** is invalid.

**Atomic service API**: This API can be used in atomic services since API version 13.

**System capability**: SystemCapability.Multimedia.AVSession.AVCast

 |
| ERR\_CODE\_CAST\_CONTROL\_IO\_BAD\_HTTP\_STATUS13+ | 6612004 | 

The HTTP server returns an unexpected HTTP response status code.

**Atomic service API**: This API can be used in atomic services since API version 13.

**System capability**: SystemCapability.Multimedia.AVSession.AVCast

 |
| ERR\_CODE\_CAST\_CONTROL\_IO\_FILE\_NOT\_FOUND13+ | 6612005 | 

The file does not exist.

**Atomic service API**: This API can be used in atomic services since API version 13.

**System capability**: SystemCapability.Multimedia.AVSession.AVCast

 |
| ERR\_CODE\_CAST\_CONTROL\_IO\_NO\_PERMISSION13+ | 6612006 | 

The input/output operation is not allowed.

**Atomic service API**: This API can be used in atomic services since API version 13.

**System capability**: SystemCapability.Multimedia.AVSession.AVCast

 |
| ERR\_CODE\_CAST\_CONTROL\_IO\_CLEARTEXT\_NOT\_PERMITTED13+ | 6612007 | 

The network security configuration of the application does not allow access to plaintext HTTP traffic.

**Atomic service API**: This API can be used in atomic services since API version 13.

**System capability**: SystemCapability.Multimedia.AVSession.AVCast

 |
| ERR\_CODE\_CAST\_CONTROL\_IO\_READ\_POSITION\_OUT\_OF\_RANGE13+ | 6612008 | 

Data is read from data binding.

**Atomic service API**: This API can be used in atomic services since API version 13.

**System capability**: SystemCapability.Multimedia.AVSession.AVCast

 |
| ERR\_CODE\_CAST\_CONTROL\_IO\_NO\_CONTENTS13+ | 6612100 | 

No content can be played in the media.

**Atomic service API**: This API can be used in atomic services since API version 13.

**System capability**: SystemCapability.Multimedia.AVSession.AVCast

 |
| ERR\_CODE\_CAST\_CONTROL\_IO\_READ\_ERROR13+ | 6612101 | 

The media cannot be read.

**Atomic service API**: This API can be used in atomic services since API version 13.

**System capability**: SystemCapability.Multimedia.AVSession.AVCast

 |
| ERR\_CODE\_CAST\_CONTROL\_IO\_CONTENT\_BUSY13+ | 6612102 | 

The resource is in use.

**Atomic service API**: This API can be used in atomic services since API version 13.

**System capability**: SystemCapability.Multimedia.AVSession.AVCast

 |
| ERR\_CODE\_CAST\_CONTROL\_IO\_CONTENT\_EXPIRED13+ | 6612103 | 

The input/output request content has expired.

**Atomic service API**: This API can be used in atomic services since API version 13.

**System capability**: SystemCapability.Multimedia.AVSession.AVCast

 |
| ERR\_CODE\_CAST\_CONTROL\_IO\_USE\_FORBIDDEN13+ | 6612104 | 

The requested content cannot be played.

**Atomic service API**: This API can be used in atomic services since API version 13.

**System capability**: SystemCapability.Multimedia.AVSession.AVCast

 |
| ERR\_CODE\_CAST\_CONTROL\_IO\_NOT\_VERIFIED13+ | 6612105 | 

The allowed content cannot be verified.

**Atomic service API**: This API can be used in atomic services since API version 13.

**System capability**: SystemCapability.Multimedia.AVSession.AVCast

 |
| ERR\_CODE\_CAST\_CONTROL\_IO\_EXHAUSTED\_ALLOWED\_USES13+ | 6612106 | 

The number of times that the content can be used has reached the maximum.

**Atomic service API**: This API can be used in atomic services since API version 13.

**System capability**: SystemCapability.Multimedia.AVSession.AVCast

 |
| ERR\_CODE\_CAST\_CONTROL\_IO\_NETWORK\_PACKET\_SENDING\_FAILED13+ | 6612107 | 

An error occurs when the source device sends data packets to the destination device.

**Atomic service API**: This API can be used in atomic services since API version 13.

**System capability**: SystemCapability.Multimedia.AVSession.AVCast

 |
| ERR\_CODE\_CAST\_CONTROL\_PARSING\_UNSPECIFIED13+ | 6613000 | 

An unspecified content parsing error occurs.

**Atomic service API**: This API can be used in atomic services since API version 13.

**System capability**: SystemCapability.Multimedia.AVSession.AVCast

 |
| ERR\_CODE\_CAST\_CONTROL\_PARSING\_CONTAINER\_MALFORMED13+ | 6613001 | 

The format of the media container bit stream is incorrectly parsed.

**Atomic service API**: This API can be used in atomic services since API version 13.

**System capability**: SystemCapability.Multimedia.AVSession.AVCast

 |
| ERR\_CODE\_CAST\_CONTROL\_PARSING\_MANIFEST\_MALFORMED13+ | 6613002 | 

An error occurred when parsing the media list.

**Atomic service API**: This API can be used in atomic services since API version 13.

**System capability**: SystemCapability.Multimedia.AVSession.AVCast

 |
| ERR\_CODE\_CAST\_CONTROL\_PARSING\_CONTAINER\_UNSUPPORTED13+ | 6613003 | 

The media container format or feature of the file is not supported.

**Atomic service API**: This API can be used in atomic services since API version 13.

**System capability**: SystemCapability.Multimedia.AVSession.AVCast

 |
| ERR\_CODE\_CAST\_CONTROL\_PARSING\_MANIFEST\_UNSUPPORTED13+ | 6613004 | 

The feature is not supported in the media list.

**Atomic service API**: This API can be used in atomic services since API version 13.

**System capability**: SystemCapability.Multimedia.AVSession.AVCast

 |
| ERR\_CODE\_CAST\_CONTROL\_DECODING\_UNSPECIFIED13+ | 6614000 | 

An unspecified decoding error occurs.

**Atomic service API**: This API can be used in atomic services since API version 13.

**System capability**: SystemCapability.Multimedia.AVSession.AVCast

 |
| ERR\_CODE\_CAST\_CONTROL\_DECODING\_INIT\_FAILED13+ | 6614001 | 

Initializing the decoder fails.

**Atomic service API**: This API can be used in atomic services since API version 13.

**System capability**: SystemCapability.Multimedia.AVSession.AVCast

 |
| ERR\_CODE\_CAST\_CONTROL\_DECODING\_QUERY\_FAILED13+ | 6614002 | 

Querying the decoder fails.

**Atomic service API**: This API can be used in atomic services since API version 13.

**System capability**: SystemCapability.Multimedia.AVSession.AVCast

 |
| ERR\_CODE\_CAST\_CONTROL\_DECODING\_FAILED13+ | 6614003 | 

Decoding the media sample fails.

**Atomic service API**: This API can be used in atomic services since API version 13.

**System capability**: SystemCapability.Multimedia.AVSession.AVCast

 |
| ERR\_CODE\_CAST\_CONTROL\_DECODING\_FORMAT\_EXCEEDS\_CAPABILITIES13+ | 6614004 | 

The device cannot decode the current format.

**Atomic service API**: This API can be used in atomic services since API version 13.

**System capability**: SystemCapability.Multimedia.AVSession.AVCast

 |
| ERR\_CODE\_CAST\_CONTROL\_DECODING\_FORMAT\_UNSUPPORTED13+ | 6614005 | 

The decoding format is not supported.

**Atomic service API**: This API can be used in atomic services since API version 13.

**System capability**: SystemCapability.Multimedia.AVSession.AVCast

 |
| ERR\_CODE\_CAST\_CONTROL\_AUDIO\_RENDERER\_UNSPECIFIED13+ | 6615000 | 

An unspecified audio renderer error occurs.

**Atomic service API**: This API can be used in atomic services since API version 13.

**System capability**: SystemCapability.Multimedia.AVSession.AVCast

 |
| ERR\_CODE\_CAST\_CONTROL\_AUDIO\_RENDERER\_INIT\_FAILED 13+ | 6615001 | 

Initializing the audio renderer fails.

**Atomic service API**: This API can be used in atomic services since API version 13.

**System capability**: SystemCapability.Multimedia.AVSession.AVCast

 |
| ERR\_CODE\_CAST\_CONTROL\_AUDIO\_RENDERER\_WRITE\_FAILED13+ | 6615002 | 

Writing data to the audio renderer fails.

**Atomic service API**: This API can be used in atomic services since API version 13.

**System capability**: SystemCapability.Multimedia.AVSession.AVCast

 |
| ERR\_CODE\_CAST\_CONTROL\_DRM\_UNSPECIFIED13+ | 6616000 | 

An unspecified DRM-related error occurs.

**Atomic service API**: This API can be used in atomic services since API version 13.

**System capability**: SystemCapability.Multimedia.AVSession.AVCast

 |
| ERR\_CODE\_CAST\_CONTROL\_DRM\_SCHEME\_UNSUPPORTED13+ | 6616001 | 

The device does not support the selected DRM scheme.

**Atomic service API**: This API can be used in atomic services since API version 13.

**System capability**: SystemCapability.Multimedia.AVSession.AVCast

 |
| ERR\_CODE\_CAST\_CONTROL\_DRM\_PROVISIONING\_FAILED13+ | 6616002 | 

Device configurations fail.

**Atomic service API**: This API can be used in atomic services since API version 13.

**System capability**: SystemCapability.Multimedia.AVSession.AVCast

 |
| ERR\_CODE\_CAST\_CONTROL\_DRM\_CONTENT\_ERROR13+ | 6616003 | 

The DRM-protected content cannot be played.

**Atomic service API**: This API can be used in atomic services since API version 13.

**System capability**: SystemCapability.Multimedia.AVSession.AVCast

 |
| ERR\_CODE\_CAST\_CONTROL\_DRM\_LICENSE\_ACQUISITION\_FAILED13+ | 6616004 | 

Obtaining a license fails.

**Atomic service API**: This API can be used in atomic services since API version 13.

**System capability**: SystemCapability.Multimedia.AVSession.AVCast

 |
| ERR\_CODE\_CAST\_CONTROL\_DRM\_DISALLOWED\_OPERATION13+ | 6616005 | 

The license policy does not allow this operation.

**Atomic service API**: This API can be used in atomic services since API version 13.

**System capability**: SystemCapability.Multimedia.AVSession.AVCast

 |
| ERR\_CODE\_CAST\_CONTROL\_DRM\_SYSTEM\_ERROR13+ | 6616006 | 

An error occurs in the DRM system.

**Atomic service API**: This API can be used in atomic services since API version 13.

**System capability**: SystemCapability.Multimedia.AVSession.AVCast

 |
| ERR\_CODE\_CAST\_CONTROL\_DRM\_DEVICE\_REVOKED13+ | 6616007 | 

The DRM permission has been revoked from the device.

**Atomic service API**: This API can be used in atomic services since API version 13.

**System capability**: SystemCapability.Multimedia.AVSession.AVCast

 |
| ERR\_CODE\_CAST\_CONTROL\_DRM\_LICENSE\_EXPIRED13+ | 6616008 | 

The DRM license that is being loaded has expired.

**Atomic service API**: This API can be used in atomic services since API version 13.

**System capability**: SystemCapability.Multimedia.AVSession.AVCast

 |
| ERR\_CODE\_CAST\_CONTROL\_DRM\_PROVIDE\_KEY\_RESPONSE\_ERROR13+ | 6616100 | 

An error occurs when the DRM processes the key response.

**Atomic service API**: This API can be used in atomic services since API version 13.

**System capability**: SystemCapability.Multimedia.AVSession.AVCast

 |

#### SkipIntervals11+

Enumerates the fast-forward or rewind intervals supported by the media session.

**System capability**: SystemCapability.Multimedia.AVSession.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| SECONDS\_10 | 10 | The time is 10 seconds. |
| SECONDS\_15 | 15 | The time is 15 seconds. |
| SECONDS\_30 | 30 | The time is 30 seconds. |
