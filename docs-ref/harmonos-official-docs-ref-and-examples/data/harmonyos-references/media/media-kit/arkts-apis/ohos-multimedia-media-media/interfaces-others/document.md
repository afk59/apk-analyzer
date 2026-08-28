# Interfaces (Others)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/aVHBcp5XSNmPVA2_8DEhvw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062437Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=284C6D993FB50266FECDCEB72D81C37CDE97E1FBC8E3B5923D089101E9BEFDCD)

The initial APIs of this module are supported since API version 6. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### AVFileDescriptor9+

Describes an audio and video file asset. It is used to specify a particular asset for playback based on its offset and length within a file.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Multimedia.Media.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| fd | number | No | No | Resource handle, which is obtained by calling [resourceManager.getRawFd](../../../../../application-framework/localization-kit/arkts-apis/ohos-resourcemanager-resource-management/document.md#getrawfd9) or [fs.open](../../../../../application-framework/core-file-kit/arkts-apis/ohos-file-fs-file-management/document.md#fsopen). |
| offset | number | No | Yes | Resource offset, which needs to be entered based on the preset asset information. The default value is **0**. An invalid value causes a failure to parse audio and video assets. |
| length | number | No | Yes | Resource length, which needs to be entered based on the preset asset information. The default value is the remaining bytes from the offset in the file. An invalid value causes a failure to parse audio and video assets. |

#### AVDataSrcDescriptor10+

Defines the descriptor of an audio and video file, which is used in DataSource playback mode.

Use scenario: An application can create a playback instance and start playback before it finishes downloading the audio and video resources.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Multimedia.Media.AVPlayer

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| fileSize | number | No | No | Size of the file to play, in bytes. The value **\-1** indicates that the size is unknown. If **fileSize** is set to **\-1**, the playback mode is similar to the live mode. In this mode, the **seek** and **setSpeed** operations cannot be performed, and the **loop** property cannot be set, indicating that loop playback is unavailable. |
| callback | (buffer: ArrayBuffer, length: number, pos?: number) => number | No | No | 
Callback used to fill in data.

\- **buffer**: memory to be filled. This parameter is mandatory.

\- **length**: maximum length of the memory to be filled. This parameter is mandatory.

\- **pos**: position of the data to be filled in the file. This parameter is optional. When **fileSize** is set to **\-1**, this parameter cannot be used.

\- Return value: length of the data filled, which is of the number type. If **\-1** is returned, the end of stream is reached. If **\-2** is returned, an unrecoverable error occurs.

 |

#### SubtitleInfo12+

Describes the external subtitle information. When a subtitle update event is subscribed to, the information about the external subtitle is returned through a callback.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.Media.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| text | string | No | Yes | Text information of the subtitle. |
| startTime | number | No | Yes | Start time for displaying the subtitle, in milliseconds. |
| duration | number | No | Yes | Duration for displaying the subtitle, in milliseconds. |

#### SeiMessage18+

Describes the information of an SEI message.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.Multimedia.Media.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| payloadType | number | No | No | Payload type of the SEI message. |
| payload | ArrayBuffer | No | No | Payload data of the SEI message. |

#### MediaDescription8+

Defines media information in key-value mode.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Multimedia.Media.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| \[key: string\] | Object | No | Yes | For details about the key range supported and the object type and range of each key, see [MediaDescriptionKey](../enums/document.md#mediadescriptionkey8). |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { media } from '@kit.MediaKit';

function printfItemDescription(obj: media.MediaDescription, key: string) {
  let property: Object = obj\[key\];
  console.info('audio key is ' + key); // Obtain the value of the key. For details about the keys, see MediaDescriptionKey.
  console.info('audio value is ' + property); // Obtain the value of the key. The value can be any type. For details about the types, see MediaDescriptionKey.
}

let avPlayer: media.AVPlayer | undefined = undefined;
media.createAVPlayer((err: BusinessError, player: media.AVPlayer) => {
  if(player != null) {
    avPlayer = player;
    console.info(\`Succeeded in creating AVPlayer\`);
    avPlayer.getTrackDescription((error: BusinessError, arrList: Array<media.MediaDescription>) => {
      if (arrList != null) {
        for (let i = 0; i < arrList.length; i++) {
          printfItemDescription(arrList\[i\], media.MediaDescriptionKey.MD\_KEY\_TRACK\_TYPE);  // Print the MD\_KEY\_TRACK\_TYPE value of each track.
        }
      } else {
        console.error(\`Failed to get TrackDescription, error:${error}\`);
      }
    });
  } else {
    console.error(\`Failed to create AVPlayer, error message:${err.message}\`);
  }
});

#### PlaybackInfo12+

Defines the playback information in key-value pairs.

**System capability**: SystemCapability.Multimedia.Media.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| \[key: string\] | Object | No | Yes | 
For details about the value range of each key, see [PlaybackInfoKey](../enums/document.md#playbackinfokey12).

For details about the object type and range of each key, see [PlaybackInfoKey](../enums/document.md#playbackinfokey12).

 |

#### AVRecorderConfig9+

Describes the audio and video recording parameters.

The **audioSourceType** and **videoSourceType** parameters are used to distinguish audio-only recording, video-only recording, and audio and video recording. For audio-only recording, set only **audioSourceType**. For video-only recording, set only **videoSourceType**. For audio and video recording, set both **audioSourceType** and **videoSourceType**.

**System capability**: SystemCapability.Multimedia.Media.AVRecorder

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| audioSourceType | [AudioSourceType](../enums/document.md#audiosourcetype9) | No | Yes | 
Type of the audio source to record. This parameter is mandatory for audio recording.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| videoSourceType | [VideoSourceType](../enums/document.md#videosourcetype9) | No | Yes | Type of the video source to record. This parameter is mandatory for video recording. |
| profile | [AVRecorderProfile](#avrecorderprofile9) | No | No | 

Recording profile. This parameter is mandatory.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| url | string | No | No | 

Recording output URL: fd://xx (fd number).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/iNZXPSc0RxmVHwfB3MD1AA/en-us_image_0000002568686121.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062437Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=22F316AEF6F581C90515BDE66161AC44ADF7A5CBEBE9C1FAA39D2D20379EB506)

This parameter is mandatory.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| fileGenerationMode12+ | [FileGenerationMode](../enums/document.md#filegenerationmode12) | No | Yes | Mode for creating the file, which is used together with [on('photoAssetAvailable')](../interface-avrecorder/document.md#onphotoassetavailable12). |
| rotation(deprecated) | number | No | Yes | 

Rotation angle of the recorded video. The value can be 0 (default), 90, 180, or 270 for MP4 videos.

This API is supported since API version 6 and deprecated since API version 12. You are advised to use **[AVMetadata](#avmetadata11).videoOrientation** instead.

If both parameters are set, **[AVMetadata](#avmetadata11).videoOrientation** is used.

 |
| location(deprecated) | [Location](#location) | No | Yes | 

Geographical location of the recorded video. By default, the geographical location information is not recorded.

This API is supported since API version 6 and deprecated since API version 12. You are advised to use **[AVMetadata](#avmetadata11).location** instead.

If both parameters are set, **[AVMetadata](#avmetadata11).location** is used.

 |
| metadata12+ | [AVMetadata](#avmetadata11) | No | Yes | Metadata. For details, see [AVMetadata](#avmetadata11). |
| maxDuration18+ | number | No | Yes | Maximum recording duration, in seconds. The value range is \[1, 2^31-1\]. If an invalid value is provided, it is reset to the maximum allowed duration. Once the recording reaches the specified duration, it stops automatically and notifies via the stateChange callback that the recording has stopped: [AVRecorderState](../types/document.md#avrecorderstate9) = 'stopped', [StateChangeReason](../enums/document.md#statechangereason9) = BACKGROUND. |

#### AVRecorderProfile9+

Describes the audio and video recording profile.

**System capability**: SystemCapability.Multimedia.Media.AVRecorder

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| audioBitrate | number | No | Yes | 
Audio encoding bit rate. This parameter is mandatory for audio recording.

Supported bit rate ranges:

\- Range \[32000, 500000\] for the AAC encoding format.

\- 64000 for the G.711 μ-law encoding format.

\- Range \[8000, 16000, 32000, 40000, 48000, 56000, 64000, 80000, 96000, 112000, 128000, 160000, 192000, 224000, 256000, 320000\] for the MP3 encoding format.

When the MP3 encoding format is used, the mapping between the sample rate and bit rate is as follows:

\- When the sample rate is lower than 16 kHZ, the bit rate range is \[8000 - 64000\].

\- When the sample rate ranges from 16 kHz to 32 kHz, the bit rate range is \[8000, 160000\].

\- When the sample rate is greater than 32 kHz, the bit rate range is \[32000, 320000\].

\- Range \[4750, 5150, 5900, 6700, 7400, 7950, 10200, 12200\] for the AMR-NB encoding format.

\- Range \[6600, 8850, 12650, 14250, 15850, 18250, 19850, 23050, 23850\] for the AMR-WB encoding format.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| audioChannels | number | No | Yes | 

Audio channel count. This parameter is mandatory for audio recording.

\- Range \[1, 2\] for the AAC encoding format.

\- 1 for the G.711 μ-law encoding format.

\- Range \[1, 2\] for the MP3 encoding format.

\- 1 for the AMR-NB and AMR-WB encoding formats.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| audioCodec | [CodecMimeType](../enums/document.md#codecmimetype8) | No | Yes | 

Audio encoding format. This parameter is mandatory for audio recording.

Currently, AUDIO\_AAC, AUDIO\_MP3, AUDIO\_G711MU, AUDIO\_AMR\_NB, and AUDIO\_AMR\_WB are supported.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| aacProfile22+ | [AacProfile](../enums/document.md#aacprofile22) | No | Yes | 

Extended audio encoding format. The default value is **AAC\_LC**.

Currently, the following formats are supported: **AAC\_LC**, **AAC\_HE**, and **AAC\_HE\_V2**.

**Atomic service API**: This API can be used in atomic services since API version 22.

 |
| audioSampleRate | number | No | Yes | 

Audio sample rate. This parameter is mandatory for audio recording.

Supported sample rate ranges:

\- Range \[8000, 11025, 12000, 16000, 22050, 24000, 32000, 44100, 48000, 64000, 88200, 96000\] for the AAC encoding format.

\- 8000 for the G.711 μ-law encoding format.

\- Range \[8000, 11025, 12000, 16000, 22050, 24000, 32000, 44100, 48000\] for the MP3 encoding format.

\- 8000 for the AMR-NB encoding format.

\- 16000 for the AMR-WB encoding format.

Variable bit rate. The bit rate is for reference only.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| fileFormat | [ContainerFormatType](../enums/document.md#containerformattype8) | No | No | 

Container format of a file. This parameter is mandatory. Currently, the MP4, M4A, MP3, WAV, AMR, and AAC container formats are supported. The default container format for AAC audio is ADTS frame format. The AUDIO\_MP3 encoding format is not supported within the MP4 container format.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| videoBitrate | number | No | Yes | Video encoding bit rate. This parameter is mandatory for video recording. The value range is \[10000, 100000000\]. |
| videoCodec | [CodecMimeType](../enums/document.md#codecmimetype8) | No | Yes | Video encoding format. This parameter is mandatory for video recording. Currently, **VIDEO\_AVC** and **VIDEO\_HEVC** are supported. |
| videoFrameWidth | number | No | Yes | Width of a video frame. This parameter is mandatory for video recording. The value range is \[176, 4096\]. |
| videoFrameHeight | number | No | Yes | Height of a video frame. This parameter is mandatory for video recording. The value range is \[144, 4096\]. |
| videoFrameRate | number | No | Yes | Video frame rate. This parameter is mandatory for video recording. The recommended value range is \[1, 60\]. |
| isHdr11+ | boolean | No | Yes | HDR encoding. This parameter is optional for video recording. The default value is **false**, and there is no requirement on the encoding format. When **isHdr** is set to **true**, the encoding format must be **video/hevc**. |
| enableTemporalScale12+ | boolean | No | Yes | Whether temporal layered encoding is supported. This parameter is optional for video recording. The default value is **false**. If this parameter is set to **true**, some frames in the video output streams can be skipped without being encoded. |
| enableBFrame20+ | boolean | No | Yes | 

Whether B-frame encoding is enabled for video recording. **true** if enabled (valid only when the video encoding format is H.265 and the device hardware supports B-frame encoding), **false** otherwise.

This parameter is optional in video recording scenarios. The default value is **false**.

 |

## Audio Parameters

The following table lists the audio parameters. For details about each parameter, see the field description below.

| Encoding Format | Container Format | Sample Rate | Bit Rate | Audio Channel Count |
| :-- | :-- | :-- | :-- | :-- |
| AUDIO\_AAC | MP4, M4A | \[8000, 11025, 12000, 16000, 22050, 24000, 32000, 44100, 48000, 64000, 88200, 96000\] | \[32000-500000\] | \[1-2\] |
| AUDIO\_MP3 | MP3 | \[8000, 11025, 12000, 16000, 22050, 24000, 32000, 44100, 48000\] | 
\- When the sample rate is lower than 16000, the bit rate range is \[8000, 16000, 32000, 40000, 48000, 56000, 64000\].

\- When the sample rate ranges from 16000 to 32000, the bit rate range is \[8000, 16000, 32000, 40000, 48000, 56000, 64000, 80000, 96000, 112000, 128000, 160000\].

\- When the sample rate is greater than 32000, the bit rate range is \[32000, 40000, 48000, 56000, 64000, 80000, 96000, 112000, 128000, 160000, 192000, 224000, 256000, 320000\].

 | \[1-2\] |
| AUDIO\_G711MU | WAV | \[8000\] | \[64000\] | \[1\] |
| AUDIO\_AMR\_NB18+ | AMR | \[8000\] | \[4750, 5150, 5900, 6700, 7400, 7950, 10200, 12200\] | \[1\] |
| AUDIO\_AMR\_WB18+ | AMR | \[16000\] | \[6600, 8850, 12650, 14250, 15850, 18250, 19850, 23050, 23850\] | \[1\] |

#### Location

Describes the geographical location of the recorded video.

**System capability**: SystemCapability.Multimedia.Media.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| latitude | number | No | No | Latitude of the geographical location. The value range is \[-90, 90\]. |
| longitude | number | No | No | Longitude of the geographical location. The value range is \[-180, 180\]. |

#### EncoderInfo11+

Describes the information about an encoder.

**System capability**: SystemCapability.Multimedia.Media.AVRecorder

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| mimeType | [CodecMimeType](../enums/document.md#codecmimetype8) | No | No | MIME type of the encoder. |
| type | string | No | No | Encoder type. The value **audio** means an audio encoder, and **video** means a video encoder. |
| bitRate | [Range](#range11) | No | Yes | Bit rate range of the encoder, with the minimum and maximum bit rates specified. |
| frameRate | [Range](#range11) | No | Yes | Video frame rate range, with the minimum and maximum frame rates specified. This parameter is available only for video encoders. |
| width | [Range](#range11) | No | Yes | Video frame width range, with the minimum and maximum widths specified. This parameter is available only for video encoders. |
| height | [Range](#range11) | No | Yes | Video frame height range, with the minimum and maximum heights specified. This parameter is available only for video encoders. |
| channels | [Range](#range11) | No | Yes | Audio channel count for the audio capturer, with the minimum and maximum numbers of audio channels specified. This parameter is available only for audio encoders. |
| sampleRate | Array<number> | No | Yes | Audio sample rate, including all available audio sample rates. The value depends on the encoder type, and this parameter is available only for audio encoders. |

#### Range11+

Describes a range.

**System capability**: SystemCapability.Multimedia.Media.AVRecorder

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| min | number | No | No | Minimum value. |
| max | number | No | No | Maximum value. |

#### AVTranscoderConfig12+

Describes the video transcoding parameters.

**System capability**: SystemCapability.Multimedia.Media.AVTranscoder

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| audioBitrate | number | No | Yes | 
Bit rate of the output audio, in bit/s. The value range is \[1, 500000\]. The default value is 48 kbit/s.

**Atomic service API**: This API can be used in atomic services since API version 22.

 |
| audioCodec | [CodecMimeType](../enums/document.md#codecmimetype8) | No | Yes | 

Encoding format of the output audio. Currently, only AAC is supported. The default value is **AAC**.

**Atomic service API**: This API can be used in atomic services since API version 22.

 |
| fileFormat | [ContainerFormatType](../enums/document.md#containerformattype8) | No | No | 

Container format of the output video file. Currently, only MP4 is supported.

**Atomic service API**: This API can be used in atomic services since API version 22.

 |
| videoBitrate | number | No | Yes | 

Bit rate of the output video, in bit/s. The default bit rate depends on the resolution of the output video. The default bit rate is 1 Mbit/s for the resolution in the range \[240p, 480P\], 2 Mbit/s for the range (480P, 720P\], 4 Mbit/s for the range (720P, 1080P\], and 8 Mbit/s for 1080p or higher.

**Atomic service API**: This API can be used in atomic services since API version 22.

 |
| videoCodec | [CodecMimeType](../enums/document.md#codecmimetype8) | No | Yes | 

Encoding format of the output video. Currently, only AVC and HEVC are supported. If the source video is in HEVC format, the default value is **HEVC**. Otherwise, the default value is **AVC**.

**Atomic service API**: This API can be used in atomic services since API version 22.

 |
| videoFrameWidth | number | No | Yes | 

Width of the output video frame, in px. The value range is \[240, 3840\]. The default value is the width of the source video frame.

**Atomic service API**: This API can be used in atomic services since API version 22.

 |
| videoFrameHeight | number | No | Yes | 

Height of the output video frame, in px. The value range is \[240, 2160\]. The default value is the height of the source video frame.

**Atomic service API**: This API can be used in atomic services since API version 22.

 |
| enableBFrame20+ | boolean | No | Yes | 

Whether B-frame encoding is enabled for transcoding. **true** if enabled, **false** otherwise.

For details about the restrictions on B-frame video encoding, see [Constraints in B-Frame Video Encoding](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/video-encoding-b-frame#constraints). If the current environment does not meet these constraints, B-frames will be skipped, and encoding will proceed as if B-frame video encoding were not enabled.

**Atomic service API**: This API can be used in atomic services since API version 22.

 |

#### AVMetadata11+

Defines the audio and video metadata.

**System capability**: SystemCapability.Multimedia.Media.AVMetadataExtractor

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| album | string | No | Yes | Title of the album. This property cannot be set for the AVRecorder. |
| albumArtist | string | No | Yes | Artist of the album. This property cannot be set for the AVRecorder. |
| artist | string | No | Yes | Artist of the media asset. This property cannot be set for the AVRecorder. |
| author | string | No | Yes | Author of the media asset. This property cannot be set for the AVRecorder. |
| dateTime | string | No | Yes | Time when the media asset is created. This property cannot be set for the AVRecorder. |
| dateTimeFormat | string | No | Yes | Time when the media asset is created. The value is in the YYYY-MM-DD HH:mm:ss format. This property cannot be set for the AVRecorder. |
| composer | string | No | Yes | Composer of the media asset. This property cannot be set for the AVRecorder. |
| duration | string | No | Yes | Duration of the media asset. This property cannot be set for the AVRecorder. |
| genre | string | No | Yes | Type or genre of the media asset. |
| hasAudio | string | No | Yes | Whether the media asset contains audio. This property cannot be set for the AVRecorder. |
| hasVideo | string | No | Yes | Whether the media asset contains a video. This property cannot be set for the AVRecorder. |
| mimeType | string | No | Yes | MIME type of the media asset. This property cannot be set for the AVRecorder. |
| trackCount | string | No | Yes | Number of tracks of the media asset. This property cannot be set for the AVRecorder. |
| sampleRate | string | No | Yes | Audio sample rate, in Hz. This property cannot be set for the AVRecorder. |
| title | string | No | Yes | Title of the media asset. This parameter is read-only in the current version. This property cannot be set for the AVRecorder. |
| videoHeight | string | No | Yes | Video height, in px. This property cannot be set for the AVRecorder. |
| videoWidth | string | No | Yes | Video width, in px. This property cannot be set for the AVRecorder. |
| videoOrientation | string | No | Yes | Video rotation direction, in degrees. |
| hdrType12+ | [HdrType](../enums/document.md#hdrtype12) | No | Yes | HDR type of the media asset. This property cannot be set for the AVRecorder. |
| location12+ | [Location](#location) | No | Yes | Geographical location of the media asset. |
| customInfo12+ | Record<string, string> | No | Yes | Custom key-value mappings obtained from **moov.meta.list**. |
| tracks20+ | Array<[MediaDescription](#mediadescription8)\> | No | Yes | Track information of the media asset. This property cannot be set for the AVRecorder. |

## MediaDescriptionKey8+ Values Supported by AVMetadata.tracks

The following table lists the values of [MediaDescriptionKey](../enums/document.md#mediadescriptionkey8) supported by AVMetadata.tracks.

| Name | Value | Applicable Track Type |
| :-- | :-- | :-- |
| MD\_KEY\_TRACK\_INDEX | 'track\_index' | All |
| MD\_KEY\_TRACK\_TYPE | 'track\_type' | All |
| MD\_KEY\_CODEC\_MIME | 'codec\_mime' | Audio and video |
| MD\_KEY\_WIDTH | 'width' | Video |
| MD\_KEY\_HEIGHT | 'height' | Video |
| MD\_KEY\_FRAME\_RATE | 'frame\_rate' | Video |
| MD\_KEY\_AUD\_CHANNEL\_COUNT | 'channel\_count' | Audio |
| MD\_KEY\_AUD\_SAMPLE\_RATE | 'sample\_rate' | Audio |
| MD\_KEY\_HDR\_TYPE12+ | 'hdr\_type' | Video |
| MD\_KEY\_ORIGINAL\_WIDTH21+ | 'original\_width' | Video |
| MD\_KEY\_ORIGINAL\_HEIGHT21+ | 'original\_height' | Video |
| MD\_KEY\_BITRATE | 'bitrate' | Audio and video (supported since API version 21) |
| MD\_KEY\_AUD\_SAMPLE\_DEPTH12+ | 'sample\_depth' | Audio (supported since API version 21) |

#### PixelMapParams12+

Defines the format parameters of the video thumbnail to be obtained.

**System capability**: SystemCapability.Multimedia.Media.AVImageGenerator

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| width | number | No | Yes | Width of the thumbnail. The value must be greater than 0 and less than or equal to the width of the original video. Otherwise, the returned thumbnail will not be scaled. |
| height | number | No | Yes | Height of the thumbnail. The value must be greater than 0 and less than or equal to the height of the original video. Otherwise, the returned thumbnail will not be scaled. |

#### OutputSize20+

Describes the output size of the video thumbnail fetched.

**System capability**: SystemCapability.Multimedia.Media.AVImageGenerator

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| width | number | No | Yes | 
Width of the thumbnail.

\- If this parameter is set to a value less than 0, the width will be the original video width.

\- If the value is **0** or is not assigned, the scaling ratio is the same as the height ratio.

\- If neither width nor height is assigned, the output is the width and height of the original video frame.

 |
| height | number | No | Yes | 

Height of the thumbnail.

\- If this parameter is set to a value less than 0, the height will be the original video height.

\- If the value is **0** or is not assigned, the scaling ratio is the same as the width ratio.

\- If neither width nor height is assigned, the output is the width and height of the original video frame.

 |

#### MediaStream19+

Defines the media stream data information.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Media.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| url | string | No | No | URL of the media resource. Only HTTP and HTTPS are supported. |
| width | number | No | No | Video width of the media resource. If the video width is unknown, set it to **0**. In this case, [PlaybackStrategy](#playbackstrategy12) cannot be used for optimal matching. |
| height | number | No | No | Video height of the media resource. If the video width is unknown, set it to **0**. In this case, [PlaybackStrategy](#playbackstrategy12) cannot be used for optimal matching. |
| bitrate | number | No | No | Bit rate of media resources, in bit/s. |

#### MediaSourceLoader18+

Defines a media data loader, which needs to be implemented by applications.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.Multimedia.Media.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| open | [SourceOpenCallback](../types/document.md#sourceopencallback18) | No | No | Callback function implemented by applications to handle resource open requests. |
| read | [SourceReadCallback](../types/document.md#sourcereadcallback18) | No | No | Callback function implemented by applications to handle resource read requests. |
| close | [SourceCloseCallback](../types/document.md#sourceclosecallback18) | No | No | Callback function implemented by applications to handle resource close requests. |

**Example**

import { HashMap } from '@kit.ArkTS';
import { media } from '@kit.MediaKit';

let headers: Record<string, string> = {"User-Agent" : "User-Agent-Value"};
let mediaSource : media.MediaSource = media.createMediaSourceWithUrl("http://xxx",  headers);
let uuid: number = 1;
let requests: HashMap<number, media.MediaSourceLoadingRequest> = new HashMap();
let mediaSourceLoader: media.MediaSourceLoader = {
  open: (request: media.MediaSourceLoadingRequest) => {
    console.info(\`Opening resource: ${request.url}\`);
    // Open the resource and return a unique handle, ensuring the mapping between the UUID and request.
    uuid += 1;
    requests.set(uuid, request);
    return uuid;
  },
  read: (uuid: number, requestedOffset: number, requestedLength: number) => {
    console.info(\`Reading resource with handle ${uuid}, offset: ${requestedOffset}, length: ${requestedLength}\`);
    // Check whether the UUID is valid and store the read request. Avoid blocking the request while pushing data and header information.
  },
  close: (uuid: number) => {
    console.info(\`Closing resource with handle ${uuid}\`);
    // Clear resources related to the current UUID.
    requests.remove(uuid);
  }
};

mediaSource.setMediaResourceLoaderDelegate(mediaSourceLoader);
let playStrategy : media.PlaybackStrategy = {
  preferredBufferDuration: 20,
};

async function setupPlayer() {
  let player = await media.createAVPlayer();
  player.setMediaSource(mediaSource, playStrategy);
}

#### PlaybackStrategy12+

Describes the playback strategy.

**System capability**: SystemCapability.Multimedia.Media.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| preferredWidth | number | No | Yes | 
Preferred width, in px. The value is an integer greater than 0, for example, 1080.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| preferredHeight | number | No | Yes | 

Preferred height, in px. The value is an integer greater than 0, for example, 1920.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| preferredBufferDuration | number | No | Yes | 

Preferred buffer duration, in seconds. The value range is \[1, 20\].

For details, see [Minimizing Stuttering in Online Video Playback](https://developer.huawei.com/consumer/en/doc/best-practices/bpta-online-video-playback-lags-practice).

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| preferredHdr | boolean | No | Yes | 

Whether HDR is preferred. **true** if preferred, **false** otherwise. The default value is **false**.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| enableSuperResolution18+ | boolean | No | Yes | 

Whether to enable super resolution. **true** to enable, **false** otherwise. The default value is **false**.

If super resolution is disabled, super resolution APIs cannot be called. If super resolution is enabled, the default target resolution is 1920 x 1080, in px.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| showFirstFrameOnPrepare17+ | boolean | No | Yes | 

Whether to show the first frame after **prepare** is called. **true** to show, **false** otherwise. The default value is **false**.

**Atomic service API**: This API can be used in atomic services since API version 17.

 |
| mutedMediaType | [MediaType](../enums/document.md#mediatype8) | No | Yes | 

Type of the media to mute.

From API version 12 to 19, only **MediaType.MEDIA\_TYPE\_AUD** can be set. Starting from API version 20, **MediaType.MEDIA\_TYPE\_VID** is added.

 |
| preferredAudioLanguage13+ | string | No | Yes | 

Preferred audio track language. Set this parameter based on service requirements in DASH scenarios. In non-DASH scenarios, this parameter is not supported, and you are advised to retain the default value.

**Atomic service API**: This API can be used in atomic services since API version 13.

 |
| preferredSubtitleLanguage13+ | string | No | Yes | 

Preferred subtitle language. Set this parameter based on service requirements in DASH scenarios. In non-DASH scenarios, this parameter is not supported, and you are advised to retain the default value.

**Atomic service API**: This API can be used in atomic services since API version 13.

 |
| preferredBufferDurationForPlaying18+ | number | No | Yes | 

Preferred buffer duration for playback, in seconds. The playback starts once the buffering time exceeds this value. The value range is \[0, 20\].

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| thresholdForAutoQuickPlay18+ | number | No | Yes | 

Thread for starting smart frame catching, in seconds. The value must be greater than or equal to 2s and greater than **preferredBufferDurationForPlaying**. The default value is 5s.

You can use the playback strategy to maintain the real-time quality of live streams by adjusting the smart frame-catch threshold. For FLV live streams, you can set this parameter based on service requirements. This parameter is not supported for non-FLV live streams yet. Fluctuations in network conditions can cause the player to build up a lot of data over time. The player periodically checks the gap between the current playback time and the timestamp of the latest frame in the cache. If this gap is too big, the player starts catching up at 1.2x speed. The [on('speedDone')](../interface-avplayer/document.md#onspeeddone9) event will call back a specific value of **100**, indicating that the smart frame catching feature is enabled successfully. Once the gap falls below **preferredBufferDurationForPlaying**, the player stops catching up and resumes the normal playback speed.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| keepDecodingOnMute20+ | boolean | No | Yes | 

Whether the decoder continues to run when the video media is muted, which helps in quickly opening the media. Currently, this feature is available only for videos. The default value is **false**, indicating that the decoder stops running when the media is muted, reducing power consumption.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |

#### AVScreenCaptureStrategy20+

Describes the screen capture strategy.

**System capability**: SystemCapability.Multimedia.Media.AVScreenCapture

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| keepCaptureDuringCall | boolean | No | Yes | Whether to keep screen capture during a cellular call. The value **true** means to keep screen capture during a cellular call, and **false** means the opposite. The default value is **false**. |
| enableBFrame | boolean | No | Yes | 
Whether to enable B-frame encoding for screen capture. **true** to enable, **false** otherwise. The default value is **false**.

For details about the restrictions on B-frame video encoding, see [Constraints in B-Frame Video Encoding](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/video-encoding-b-frame#constraints). If the current environment does not meet the restrictions, B-frames will be skipped during screen capture, and no error will be returned.

 |

#### AVScreenCaptureRecordConfig12+

Defines the screen capture parameters.

**System capability**: SystemCapability.Multimedia.Media.AVScreenCapture

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| fd | number | No | No | FD of the file output. |
| frameWidth | number | No | Yes | 
Width of the screen recording video, in pixels.

The default screen width varies depending on the screen.

 |
| frameHeight | number | No | Yes | 

Height of the screen recording video, in pixels.

The default screen height varies depending on the screen.

 |
| videoBitrate | number | No | Yes | 

Bit rate of the screen recording video.

The default value is **10000000**.

 |
| audioSampleRate | number | No | Yes | 

Audio sampling rate of the screen recording.

This value is used for both the system sound and microphone. Only **48000** (default) and **16000** are supported.

 |
| audioChannelCount | number | No | Yes | Audio channel count. This value is used for both internal capture and external capture (using microphones). Only **1** and **2** (default) are supported. |
| audioBitrate | number | No | Yes | Audio bit rate. This value is used for both internal capture and external capture (using microphones). The default value is **96000**. |
| preset | [AVScreenCaptureRecordPreset](../enums/document.md#avscreencapturerecordpreset12) | No | Yes | Encoding and container format used. The default value is **SCREEN\_RECORD\_PRESET\_H264\_AAC\_MP4**. |
| displayId15+ | number | No | Yes | ID of the display used for screen capture. By default, the main screen is captured. |
| fillMode18+ | [AVScreenCaptureFillMode](../enums/document.md#avscreencapturefillmode18) | No | Yes | Video fill mode during screen capture. |
| strategy20+ | [AVScreenCaptureStrategy](#avscreencapturestrategy20) | No | Yes | Screen capture strategy. |

#### AudioRecorderConfig(deprecated)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/lRZ4EAnkRhGnw4NLW161yw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062437Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8BD904D8B5CE0D7895347AC8306AAB8B77E3AECB30625E1678A874074202A6FC)

This API is supported since API version 6 and deprecated since API version 9. You are advised to use [AVRecorderConfig](#avrecorderconfig9) instead.

Describes audio recording configurations.

**System capability**: SystemCapability.Multimedia.Media.AudioRecorder

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| audioEncoder | [AudioEncoder](../enums/document.md#audioencoderdeprecated) | No | Yes | 
Audio encoding format. The default value is **AAC\_LC**.

Note: This parameter is supported since API version 6 and deprecated since API version 8. You are advised to use **audioEncoderMime** instead.

 |
| audioEncodeBitRate | number | No | Yes | 

Audio encoding bit rate. The default value is **48000**.

Note: This parameter is supported since API version 6 and deprecated since API version 9. You are advised to use **audioBitrate** in [AVRecorderProfile](#avrecorderprofile9) instead.

 |
| audioSampleRate | number | No | Yes | 

Audio sample rate. The default value is **48000**.

Variable bit rate. The bit rate is for reference only.

Note: This parameter is supported since API version 6 and deprecated since API version 9. You are advised to use **audioSampleRate** in [AVRecorderProfile](#avrecorderprofile9) instead.

 |
| numberOfChannels | number | No | Yes | 

Audio channel count. The default value is **2**.

Note: This parameter is supported since API version 6 and deprecated since API version 9. You are advised to use **audioChannels** in [AVRecorderProfile](#avrecorderprofile9) instead.

 |
| format | [AudioOutputFormat](../enums/document.md#audiooutputformatdeprecated) | No | Yes | 

Audio output format. The default value is **MPEG\_4**.

Note: This parameter is supported since API version 6 and deprecated since API version 8. You are advised to use **fileFormat** instead.

 |
| location | [Location](#location) | No | Yes | 

Geographical location of the recorded audio.

Note: This parameter is supported since API version 6 and deprecated since API version 9. You are advised to use **location** in [AVMetadata](#avmetadata11) instead.

 |
| uri | string | No | No | 

Audio output URI. Supported: fd://xx (fd number)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/h5QlA81GTge1rhmDSu8m6Q/en-us_image_0000002568686121.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062437Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DC28AC3A686FE31515EDFC26393BE58A358914BB099350AE30B9B16FB5E0C6FF)

The file must be created by the caller and granted with proper permissions.

Note: This parameter is supported since API version 6 and deprecated since API version 9. You are advised to use **url** in [AVRecorderConfig](#avrecorderconfig9) instead.

 |
| audioEncoderMime8+ | [CodecMimeType](../enums/document.md#codecmimetype8) | No | Yes | 

Container encoding format.

Note: This parameter is supported since API version 8 and deprecated since API version 9. You are advised to use **audioCodec** in [AVRecorderProfile](#avrecorderprofile9) instead.

 |
| fileFormat8+ | [ContainerFormatType](../enums/document.md#containerformattype8) | No | Yes | 

Audio encoding format.

Note: This parameter is supported since API version 8 and deprecated since API version 9. You are advised to use **fileFormat** in [AVRecorderProfile](#avrecorderprofile9) instead.

 |
