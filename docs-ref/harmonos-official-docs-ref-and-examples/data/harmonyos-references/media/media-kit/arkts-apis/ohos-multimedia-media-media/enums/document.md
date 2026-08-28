# Enums

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/zewNhjSoQQabM7dUDQHx0Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062437Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8D5C3B0BE91E1A5783436D149518604BA6704E2BCEEF43DCB44F176F0594625A)

The initial APIs of this module are supported since API version 6. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### AVErrorCode9+

Enumerates the types of [Media error codes](../../../error-codes/media-error-codes/document.md).

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Multimedia.Media.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| AVERR\_OK | 0 | The operation is successful. |
| AVERR\_NO\_PERMISSION | 201 | No permission to perform the operation. |
| AVERR\_INVALID\_PARAMETER | 401 | Invalid input parameter. |
| AVERR\_UNSUPPORT\_CAPABILITY | 801 | Unsupported API. |
| AVERR\_NO\_MEMORY | 5400101 | The system memory is insufficient or the number of services reaches the upper limit. |
| AVERR\_OPERATE\_NOT\_PERMIT | 5400102 | The operation is not allowed in the current state or you do not have the permission to perform the operation. |
| AVERR\_IO | 5400103 | The data stream is abnormal. |
| AVERR\_TIMEOUT | 5400104 | The system or network response times out. |
| AVERR\_SERVICE\_DIED | 5400105 | The service process is dead. |
| AVERR\_UNSUPPORT\_FORMAT | 5400106 | The format of the media asset is not supported. |
| AVERR\_AUDIO\_INTERRUPTED11+ | 5400107 | The audio focus is interrupted. |
| AVERR\_IO\_HOST\_NOT\_FOUND14+ | 5411001 | 
Failed to parse the server address or connect to the server.

**Atomic service API**: This API can be used in atomic services since API version 14.

 |
| AVERR\_IO\_CONNECTION\_TIMEOUT14+ | 5411002 | 

Network connection times out.

**Atomic service API**: This API can be used in atomic services since API version 14.

 |
| AVERR\_IO\_NETWORK\_ABNORMAL14+ | 5411003 | 

Data or links are abnormal due to network exceptions.

**Atomic service API**: This API can be used in atomic services since API version 14.

 |
| AVERR\_IO\_NETWORK\_UNAVAILABLE14+ | 5411004 | 

The network is disabled.

**Atomic service API**: This API can be used in atomic services since API version 14.

 |
| AVERR\_IO\_NO\_PERMISSION14+ | 5411005 | 

No access permission.

**Atomic service API**: This API can be used in atomic services since API version 14.

 |
| AVERR\_IO\_REQUEST\_DENIED14+ | 5411006 | 

The client request parameter is incorrect or exceeds the processing capability.

**Atomic service API**: This API can be used in atomic services since API version 14.

 |
| AVERR\_IO\_RESOURCE\_NOT\_FOUND14+ | 5411007 | 

No network resource is available.

**Atomic service API**: This API can be used in atomic services since API version 14.

 |
| AVERR\_IO\_SSL\_CLIENT\_CERT\_NEEDED14+ | 5411008 | 

The server fails to verify the client certificate.

**Atomic service API**: This API can be used in atomic services since API version 14.

 |
| AVERR\_IO\_SSL\_CONNECTION\_FAILED14+ | 5411009 | 

The SSL connection fails.

**Atomic service API**: This API can be used in atomic services since API version 14.

 |
| AVERR\_IO\_SSL\_SERVER\_CERT\_UNTRUSTED14+ | 5411010 | 

The client fails to verify the server certificate.

**Atomic service API**: This API can be used in atomic services since API version 14.

 |
| AVERR\_IO\_UNSUPPORTED\_REQUEST14+ | 5411011 | 

The request is not supported due to a network protocol error.

**Atomic service API**: This API can be used in atomic services since API version 14.

 |
| AVERR\_SEEK\_CONTINUOUS\_UNSUPPORTED18+ | 5410002 | 

The seek operation in SEEK\_CONTINUOUS mode is not supported.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| AVERR\_SUPER\_RESOLUTION\_UNSUPPORTED18+ | 5410003 | 

Super resolution is not supported.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| AVERR\_SUPER\_RESOLUTION\_NOT\_ENABLED18+ | 5410004 | 

Super resolution is not enabled.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| AVERR\_PARAMETER\_OUT\_OF\_RANGE20+ | 5400108 | 

The parameter value is out of range.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |

#### MediaType8+

Enumerates the media types.

**System capability**: SystemCapability.Multimedia.Media.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| MEDIA\_TYPE\_UNSUPPORTED20+ | \-1 | 
The media type is not supported.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |
| MEDIA\_TYPE\_AUD | 0 | 

Media.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| MEDIA\_TYPE\_VID | 1 | 

Video.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| MEDIA\_TYPE\_SUBTITLE12+ | 2 | 

Subtitle.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| MEDIA\_TYPE\_ATTACHMENT20+ | 3 | 

Attachment information (for example, an embedded external file).

**Atomic service API**: This API can be used in atomic services since API version 20.

 |
| MEDIA\_TYPE\_DATA20+ | 4 | 

Data.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |
| MEDIA\_TYPE\_TIMED\_METADATA20+ | 5 | 

Metadata with a timestamp.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |
| MEDIA\_TYPE\_AUXILIARY20+ | 6 | 

Auxiliary (track) information.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |

#### CodecMimeType8+

Enumerates the codec MIME types.

**System capability**: SystemCapability.Multimedia.Media.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| VIDEO\_H263 | 'video/h263' | Video in H.263 format. |
| VIDEO\_AVC | 'video/avc' | 
Video in AVC format.

**Atomic service API**: This API can be used in atomic services since API version 22.

 |
| VIDEO\_MPEG2 | 'video/mpeg2' | Video in MPEG-2 format. |
| VIDEO\_MPEG4 | 'video/mp4v-es' | Video in MPEG-4 format. |
| VIDEO\_VP8 | 'video/x-vnd.on2.vp8' | Video in VP8 format. |
| VIDEO\_HEVC11+ | 'video/hevc' | 

Video in H.265 format.

**Atomic service API**: This API can be used in atomic services since API version 22.

 |
| AUDIO\_AAC | 'audio/mp4a-latm' | 

Audio in MP4A-LATM format.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| AUDIO\_VORBIS | 'audio/vorbis' | Audio in Vorbis format. |
| AUDIO\_FLAC | 'audio/flac' | Audio in FLAC format. |
| AUDIO\_MP312+ | 'audio/mpeg' | Audio in MPEG format. |
| AUDIO\_G711MU12+ | 'audio/g711mu' | Audio in G.711 μ-law format. |
| AUDIO\_AMR\_NB18+ | 'audio/3gpp' | Audio in AMR-NB format. |
| AUDIO\_AMR\_WB18+ | 'audio/amr-wb' | Audio in AMR-WB format. |

#### AacProfile22+

Enumerates the supported Advanced Audio Coding (AAC) formats.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.Multimedia.Media.AVRecorder

| Name | Value | Description |
| :-- | :-- | :-- |
| AAC\_LC | 0 | Standard AAC Low Complexity profile. |
| AAC\_HE | 1 | Standard AAC High Efficiency profile. |
| AAC\_HE\_V2 | 2 | AAC High Efficiency Version 2 profile (also known as HE-AAC v2). |

#### MediaDescriptionKey8+

Enumerates the media description keys.

**System capability**: SystemCapability.Multimedia.Media.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| MD\_KEY\_TRACK\_INDEX | 'track\_index' | 
Track index. The corresponding key value type is number.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| MD\_KEY\_TRACK\_TYPE | 'track\_type' | 

Track type. The corresponding key value type is number. For details, see [MediaType](#mediatype8).

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| MD\_KEY\_CODEC\_MIME | 'codec\_mime' | 

Codec MIME type. The corresponding key value type is string.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| MD\_KEY\_DURATION | 'duration' | 

Media duration. The corresponding key value type is number, measured in ms.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| MD\_KEY\_BITRATE | 'bitrate' | 

Bit rate. The corresponding key value type is number, measured in bit/s. If the value is **undefined** or **0**, the bit rate is abnormal.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| MD\_KEY\_WIDTH | 'width' | 

Video width. The corresponding key value type is number, measured in px.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| MD\_KEY\_HEIGHT | 'height' | 

Video height. The corresponding key value type is number, measured in px.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| MD\_KEY\_FRAME\_RATE | 'frame\_rate' | 

Video frame rate. The corresponding key value type is number, measured in frames per 100 seconds.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| MD\_KEY\_AUD\_CHANNEL\_COUNT | 'channel\_count' | 

Audio channel count. The corresponding key value type is number.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| MD\_KEY\_AUD\_SAMPLE\_RATE | 'sample\_rate' | 

Sample rate. The corresponding key value type is number, measured in Hz.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| MD\_KEY\_AUD\_SAMPLE\_DEPTH12+ | 'sample\_depth' | 

Bit depth. The corresponding key value type is number, measured in bits.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| MD\_KEY\_LANGUAGE12+ | 'language' | 

Subtitle language. The corresponding key value type is string.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| MD\_KEY\_TRACK\_NAME12+ | 'track\_name' | 

Track name. The corresponding key value type is string.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| MD\_KEY\_HDR\_TYPE12+ | 'hdr\_type' | 

Codec track type. The corresponding key value type is string.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| MD\_KEY\_ORIGINAL\_WIDTH21+ | 'original\_width' | 

Original video width. The corresponding key value type is number, measured in px.

**Atomic service API**: This API can be used in atomic services since API version 21.

 |
| MD\_KEY\_ORIGINAL\_HEIGHT21+ | 'original\_height' | 

Original video height. The corresponding key value type is number, measured in px.

**Atomic service API**: This API can be used in atomic services since API version 21.

 |

#### PlaybackInfoKey12+

Enumerates the playback description keys.

**System capability**: SystemCapability.Multimedia.Media.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| SERVER\_IP\_ADDRESS | 'server\_ip\_address' | IP address of the server. The corresponding key value type is string. |
| AVG\_DOWNLOAD\_RATE | 'average\_download\_rate' | Average download rate. The corresponding key value type is number, measured in bit/s. |
| DOWNLOAD\_RATE | 'download\_rate' | Download rate in one second. The corresponding key value type is number, measured in bit/s. |
| IS\_DOWNLOADING | 'is\_downloading' | Download status. The corresponding key value type is number. The value **1** means that the downloaded is in progress, and **0** means that the download is complete. |
| BUFFER\_DURATION | 'buffer\_duration' | Duration that the cached data can be played. The corresponding key value type is number, measured in seconds. |

#### BufferingInfoType8+

Enumerates the buffering event types.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.Media.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| BUFFERING\_START | 1 | 
Buffering starts. When this event is triggered, the player pauses the playback.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| BUFFERING\_END | 2 | 

Buffering ends. When this event is triggered, the player resumes the playback.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| BUFFERING\_PERCENT | 3 | 

Buffering percentage. You can use this event to monitor the buffering status.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| CACHED\_DURATION | 4 | 

Estimated duration, in ms, that the buffered data can be played. This event is triggered once the data change amount in the buffer exceeds 500 ms. You can use this event to develop a progress bar.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |

#### StateChangeReason9+

Enumerates the reasons for the state transition of the AVPlayer or AVRecorder instance. The enum value is reported together with **state**.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Multimedia.Media.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| USER | 1 | State transition triggered by user behavior. It happens when a user or the client calls an API. |
| BACKGROUND | 2 | State transition caused by background system behavior. For example, if an application does not have the permission of Media Controller, the application is forcibly suspended or stopped by the system when it switches to the background. |

#### SeekMode8+

Enumerates the video playback seek modes, which can be passed in the **seek** API.

**System capability**: SystemCapability.Multimedia.Media.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| SEEK\_NEXT\_SYNC | 0 | 
Seeks to the next key frame at the specified position. You are advised to use this value for the rewind operation.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| SEEK\_PREV\_SYNC | 1 | 

Seeks to the previous key frame at the specified position. You are advised to use this value for the fast-forward operation.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| SEEK\_CLOSEST12+ | 2 | 

Seeks to the frame closest to the specified position. You are advised to use this value for accurate seek.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| SEEK\_CONTINUOUS18+ | 3 | 

Offers a smooth and fluid visual experience for seeking. Applications can use a progress bar component to continuously invoke the **seek** method, and the AVPlayer will update the video frames smoothly in response to these calls.

Applications can call [isSeekContinuousSupported](../interface-avplayer/document.md#isseekcontinuoussupported18) to check whether the video source supports this seeking mode.

If the video source does not support this mode, calling **seek** will result in an **AVERR\_SEEK\_CONTINUOUS\_UNSUPPORTED** error (see [AVErrorCode](#averrorcode9)), and the smoothness of frame updates will be compromised.

This seek mode does not trigger the [on('seekDone')](../interface-avplayer/document.md#onseekdone9) event.

To exit this seeking mode, applications must call **seek(-1, SeekMode.SEEK\_CONTINUOUS)** to end the seeking process.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |

#### SwitchMode12+

Enumerates the track switching modes for video playback. The mode can be passed in to **selectTrack**. Currently, this enum is valid only for DASH video tracks.

**System capability**: SystemCapability.Multimedia.Media.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| SMOOTH | 0 | 
Smooth playback is ensured after the switching. This mode has a delay, that is, the switching does not take effect immediately.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| SEGMENT | 1 | 

The playback starts from the start position of the current segment after the switching. In this mode, the switching takes effect immediately and repeated playback may occur.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| CLOSEST | 2 | 

The playback starts from the frame closest to the current playback time. In this mode, the switching takes effect immediately, and the playback is suspended for 3s to 5s and then resumed.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |

#### PlaybackSpeed8+

Enumerates the video playback speeds, which can be passed in the **setSpeed** API.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.Media.VideoPlayer

| Name | Value | Description |
| :-- | :-- | :-- |
| SPEED\_FORWARD\_0\_75\_X | 0 | 
Plays the video at 0.75 times the normal speed.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| SPEED\_FORWARD\_1\_00\_X | 1 | 

Plays the video at the normal speed.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| SPEED\_FORWARD\_1\_25\_X | 2 | 

Plays the video at 1.25 times the normal speed.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| SPEED\_FORWARD\_1\_75\_X | 3 | 

Plays the video at 1.75 times the normal speed.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| SPEED\_FORWARD\_2\_00\_X | 4 | 

Plays the video at 2.00 times the normal speed.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| SPEED\_FORWARD\_0\_50\_X12+ | 5 | 

Plays the video at 0.50 times the normal speed.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| SPEED\_FORWARD\_1\_50\_X12+ | 6 | 

Plays the video at 1.50 times the normal speed.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| SPEED\_FORWARD\_3\_00\_X13+ | 7 | 

Plays the video at 3.00 times the normal speed.

**Atomic service API**: This API can be used in atomic services since API version 13.

 |
| SPEED\_FORWARD\_0\_25\_X12+ | 8 | 

Plays the video at 0.25 times the normal speed.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| SPEED\_FORWARD\_0\_125\_X12+ | 9 | 

Plays the video at 0.125 times the normal speed.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |

#### VideoScaleType9+

Enumerates the video scale modes.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.Media.VideoPlayer

| Name | Value | Description |
| :-- | :-- | :-- |
| VIDEO\_SCALE\_TYPE\_FIT | 0 | Default mode. The video will be stretched to fit the window. |
| VIDEO\_SCALE\_TYPE\_FIT\_CROP | 1 | Maintains the video's aspect ratio, and scales to fill the shortest side of the window, with the longer side cropped. |
| VIDEO\_SCALE\_TYPE\_SCALED\_ASPECT20+ | 2 | 
Maintains the video's aspect ratio, and scales to fill the longer side of the window, with the shorter side centered and unfilled parts left black.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |

#### AudioSourceType9+

Enumerates the audio source types for video recording.

**System capability**: SystemCapability.Multimedia.Media.AVRecorder

| Name | Value | Description |
| :-- | :-- | :-- |
| AUDIO\_SOURCE\_TYPE\_DEFAULT | 0 | Default audio input source. |
| AUDIO\_SOURCE\_TYPE\_MIC | 1 | 
Microphone audio input source.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| AUDIO\_SOURCE\_TYPE\_VOICE\_RECOGNITION12+ | 2 | Audio source in speech recognition scenarios. |
| AUDIO\_SOURCE\_TYPE\_VOICE\_COMMUNICATION12+ | 7 | Voice communication source. |
| AUDIO\_SOURCE\_TYPE\_VOICE\_MESSAGE12+ | 10 | Voice message source. |
| AUDIO\_SOURCE\_TYPE\_CAMCORDER12+ | 13 | Audio source in camera recording scenarios. |

#### VideoSourceType9+

Enumerates the video source types for video recording.

**System capability**: SystemCapability.Multimedia.Media.AVRecorder

| Name | Value | Description |
| :-- | :-- | :-- |
| VIDEO\_SOURCE\_TYPE\_SURFACE\_YUV | 0 | The input surface carries raw data. |
| VIDEO\_SOURCE\_TYPE\_SURFACE\_ES | 1 | The input surface carries ES data. |

#### ContainerFormatType8+

Enumerates the container format types (CFTs).

**System capability**: SystemCapability.Multimedia.Media.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| CFT\_MPEG\_4 | 'mp4' | 
Video container format MP4.

**Atomic service API**: This API can be used in atomic services since API version 22.

 |
| CFT\_MPEG\_4A | 'm4a' | 

Audio container format M4A.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| CFT\_MP312+ | 'mp3' | Audio container format MP3. |
| CFT\_WAV12+ | 'wav' | Audio container format WAV. |
| CFT\_AMR18+ | 'amr' | Audio container format AMR. |
| CFT\_AAC20+ | 'aac' | Audio container format AAC. The default format is ADTS frame header. |

#### FileGenerationMode12+

Enumerates the modes for creating media files.

**System capability**: SystemCapability.Multimedia.Media.AVRecorder

| Name | Value | Description |
| :-- | :-- | :-- |
| APP\_CREATE | 0 | The application creates a media file in the sandbox. |
| AUTO\_CREATE\_CAMERA\_SCENE | 1 | The system creates a media file. Currently, this mode takes effect only in camera recording scenarios. The URL set by the application is ignored. |

#### HdrType12+

Enumerates the HDR types.

**System capability**: SystemCapability.Multimedia.Media.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| AV\_HDR\_TYPE\_NONE | 0 | No HDR. |
| AV\_HDR\_TYPE\_VIVID | 1 | HDR VIVID. |

#### AVImageQueryOptions12+

Enumerates the relationship between the video frame and the time at which the video thumbnail is obtained.

The time passed in for obtaining the thumbnail may be different from the time of the video frame for which the thumbnail is actually obtained. Therefore, you need to specify their relationship.

**System capability**: SystemCapability.Multimedia.Media.AVImageGenerator

| Name | Value | Description |
| :-- | :-- | :-- |
| AV\_IMAGE\_QUERY\_NEXT\_SYNC | 0 | The key frame at or next to the specified time is selected. |
| AV\_IMAGE\_QUERY\_PREVIOUS\_SYNC | 1 | The key frame at or prior to the specified time is selected. |
| AV\_IMAGE\_QUERY\_CLOSEST\_SYNC | 2 | The key frame closest to the specified time is selected. |
| AV\_IMAGE\_QUERY\_CLOSEST | 3 | The frame (not necessarily a key frame) closest to the specified time is selected. |

#### LoadingRequestError18+

Enumerates the reasons for data loading status changes.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.Multimedia.Media.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| LOADING\_ERROR\_SUCCESS | 0 | Returned by the client to indicate that the end of the resource. |
| LOADING\_ERROR\_NOT\_READY | 1 | Returned by the client to indicate that the resource is not ready for access. |
| LOADING\_ERROR\_NO\_RESOURCE | 2 | Returned by the client to indicate that the requested resource URL does not exist. |
| LOADING\_ERROR\_INVAID\_HANDLE | 3 | Returned by the client to indicate that the ID of the requested resource handle (specified by **uuid**) is invalid. |
| LOADING\_ERROR\_ACCESS\_DENIED | 4 | Returned by the client to indicate that the client does not have permission to request the resource. |
| LOADING\_ERROR\_ACCESS\_TIMEOUT | 5 | Returned by the client to indicate that the access to the resource times out. |
| LOADING\_ERROR\_AUTHORIZE\_FAILED | 6 | Returned by the client to indicate that authorization fails. |

#### AVMimeTypes12+

Enumerates the MIME type, which is set by using [setMimeType](../interface-mediasource/document.md#setmimetype12).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.Media.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| APPLICATION\_M3U8 | application/m3u8 | Local M3U8 file. |

#### AVScreenCaptureRecordPreset12+

Enumerates the encoding and container formats used during screen capture.

**System capability**: SystemCapability.Multimedia.Media.AVScreenCapture

| Name | Value | Description |
| :-- | :-- | :-- |
| SCREEN\_RECORD\_PRESET\_H264\_AAC\_MP4 | 0 | The H.264 video encoding format, AAC audio encoding format, and MP4 container format are used. |
| SCREEN\_RECORD\_PRESET\_H265\_AAC\_MP4 | 1 | The H.265 video encoding format, AAC audio encoding format, and MP4 container format are used. |

#### AVScreenCaptureStateCode12+

Enumerates the screen capture states used in callbacks.

**System capability**: SystemCapability.Multimedia.Media.AVScreenCapture

| Name | Value | Description |
| :-- | :-- | :-- |
| SCREENCAPTURE\_STATE\_STARTED | 0 | Screen capture is started. |
| SCREENCAPTURE\_STATE\_CANCELED | 1 | Screen capture is canceled. |
| SCREENCAPTURE\_STATE\_STOPPED\_BY\_USER | 2 | Screen capture is manually stopped by the user. |
| SCREENCAPTURE\_STATE\_INTERRUPTED\_BY\_OTHER | 3 | Screen capture is interrupted by another screen capture. |
| SCREENCAPTURE\_STATE\_STOPPED\_BY\_CALL | 4 | Screen capture is interrupted by an incoming call. |
| SCREENCAPTURE\_STATE\_MIC\_UNAVAILABLE | 5 | The microphone is unavailable during screen capture. |
| SCREENCAPTURE\_STATE\_MIC\_MUTED\_BY\_USER | 6 | The microphone is muted by the user. |
| SCREENCAPTURE\_STATE\_MIC\_UNMUTED\_BY\_USER | 7 | The microphone is unmuted by the user. |
| SCREENCAPTURE\_STATE\_ENTER\_PRIVATE\_SCENE | 8 | The system enters a privacy page during screen capture. |
| SCREENCAPTURE\_STATE\_EXIT\_PRIVATE\_SCENE | 9 | The system exits a privacy page during screen capture. |
| SCREENCAPTURE\_STATE\_STOPPED\_BY\_USER\_SWITCHES | 10 | Screen capture is interrupted by system user switchover. |

#### AVScreenCaptureFillMode18+

Enumerates the video fill modes during screen capture.

**System capability**: SystemCapability.Multimedia.Media.AVScreenCapture

| Name | Value | Description |
| :-- | :-- | :-- |
| PRESERVE\_ASPECT\_RATIO | 0 | Keeps the original aspect ratio, matching the aspect ratio of the physical screen. |
| SCALE\_TO\_FILL | 1 | Stretches the image to fit the specified dimensions. |

#### PickerMode22+

Enumerates the display mode for the screen capture picker.

**System capability**: SystemCapability.Multimedia.Media.AVScreenCapture

| Name | Value | Description |
| :-- | :-- | :-- |
| WINDOW\_ONLY | 0 | Displays only a list of windows. |
| SCREEN\_ONLY | 1 | Displays only a list of screens. |
| SCREEN\_AND\_WINDOW | 2 | Displays both screens and windows. |

#### AudioEncoder(deprecated)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/23MaIk8YRiCzCLGuPj132A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062437Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A47DE974171BFC66C7A30E8EE2DA21720D047223B6F5276D4D526C204E4347C2)

This API is supported since API version 6 and deprecated since API version 8. You are advised to use [CodecMimeType](#codecmimetype8) instead.

Enumerates the audio encoding formats.

**System capability**: SystemCapability.Multimedia.Media.AudioRecorder

| Name | Value | Description |
| :-- | :-- | :-- |
| DEFAULT | 0 | 
Default encoding format.

This API is defined but not implemented yet.

Note: It is supported since API version 6 and deprecated since API version 8. You are advised to use **AUDIO\_AAC** in [CodecMimeType](#codecmimetype8) instead.

 |
| AMR\_NB | 1 | 

AMR-NB.

This API is defined but not implemented yet.

Note: It is supported since API version 6 and deprecated since API version 8. You are advised to use **AUDIO\_AMR\_NB** in [CodecMimeType](#codecmimetype8) instead.

 |
| AMR\_WB | 2 | 

Adaptive Multi Rate-Wide Band Speech Codec (AMR-WB).

This API is defined but not implemented yet.

Note: It is supported since API version 6 and deprecated since API version 8. You are advised to use **AUDIO\_AMR\_WB** in [CodecMimeType](#codecmimetype8) instead.

 |
| AAC\_LC | 3 | 

Advanced Audio Coding Low Complexity (AAC-LC).

Note: It is supported since API version 6 and deprecated since API version 8. You are advised to use **AUDIO\_AAC** in [CodecMimeType](#codecmimetype8) instead.

 |
| HE\_AAC | 4 | 

High-Efficiency Advanced Audio Coding (HE\_AAC).

This API is defined but not implemented yet.

Note: It is supported since API version 6 and deprecated since API version 8. You are advised to use **AUDIO\_AAC** in [CodecMimeType](#codecmimetype8) instead.

 |

#### AudioOutputFormat(deprecated)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/RrmITmOVQDidKqB_UXZcrA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062437Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D7839036C780164A2E31FC8410A8A1E2B45A1E927B4133E543AED8EA8E8155A3)

This API is supported since API version 6 and deprecated since API version 8. You are advised to use [ContainerFormatType](#containerformattype8) instead.

Enumerates the audio output formats.

**System capability**: SystemCapability.Multimedia.Media.AudioRecorder

| Name | Value | Description |
| :-- | :-- | :-- |
| DEFAULT | 0 | 
Default output format.

This API is defined but not implemented yet.

Note: It is supported since API version 6 and deprecated since API version 8. You are advised to select one from [ContainerFormatType](#containerformattype8) as required.

 |
| MPEG\_4 | 2 | 

MPEG-4.

Note: It is supported since API version 6 and deprecated since API version 8. You are advised to use **CFT\_MPEG\_4** in [ContainerFormatType](#containerformattype8) instead.

 |
| AMR\_NB | 3 | 

AMR\_NB.

This API is defined but not implemented yet.

Note: It is supported since API version 6 and deprecated since API version 8. You are advised to use **CFT\_AMR** in [ContainerFormatType](#containerformattype8) instead. For the encoding format, use **AUDIO\_AMR\_NB** in [CodecMimeType](#codecmimetype8).

 |
| AMR\_WB | 4 | 

AMR\_WB.

This API is defined but not implemented yet.

Note: It is supported since API version 6 and deprecated since API version 8. You are advised to use **CFT\_AMR** in [ContainerFormatType](#containerformattype8) instead. For the encoding format, use **AUDIO\_AMR\_WB** in [CodecMimeType](#codecmimetype8).

 |
| AAC\_ADTS | 6 | 

Audio Data Transport Stream (ADTS), which is a transport stream format of AAC-based audio.

Note: It is supported since API version 6 and deprecated since API version 8. You are advised to use **CFT\_AAC** in [ContainerFormatType](#containerformattype8) instead.

 |

#### MediaErrorCode(deprecated)

Enumerates the media error codes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/AVgLOOh3QOa9BoZkDLqp9g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062437Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F5C1152A565654DAF409FAEEECA4663BD445CDD0E33DF4B92092CBFEC0AF4BC4)

This API is supported since API version 8 and deprecated since API version 11. You are advised to use [AVErrorCode](#averrorcode9) instead.

**System capability**: SystemCapability.Multimedia.Media.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| MSERR\_OK | 0 | The operation is successful. |
| MSERR\_NO\_MEMORY | 1 | Failed to allocate memory. The system may have no available memory. |
| MSERR\_OPERATION\_NOT\_PERMIT | 2 | No permission to perform the operation. |
| MSERR\_INVALID\_VAL | 3 | Invalid input parameter. |
| MSERR\_IO | 4 | An I/O error occurs. |
| MSERR\_TIMEOUT | 5 | The operation times out. |
| MSERR\_UNKNOWN | 6 | An unknown error occurs. |
| MSERR\_SERVICE\_DIED | 7 | Invalid server. |
| MSERR\_INVALID\_STATE | 8 | The operation is not allowed in the current state. |
| MSERR\_UNSUPPORTED | 9 | The operation is not supported in the current version. |
