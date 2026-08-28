# AVCodec Supported Formats

The capabilities for encoding and decoding audio and video, as well as for multiplexing and demultiplexing file formats, vary across different platforms in terms of functionality and specifications. You can obtain the supported capabilities and specifications by following the instructions provided in [Obtaining Supported Codecs](../audio-and-video-codecs/obtaining-supported-codecs/document.md).

#### Media Codec

## Video Decoding

Currently, the following decoding capabilities are supported:

| Video Decoding Type | MIME Type for Video Decoding Format |
| :-- | :-- |
| MSVIDEO122+ | [OH\_AVCODEC\_MIMETYPE\_VIDEO\_MSVIDEO1](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avcodec-base-h#variables) |
| WMV322+ | [OH\_AVCODEC\_MIMETYPE\_VIDEO\_WMV3](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avcodec-base-h#variables) |
| MJPEG 22+ | [OH\_AVCODEC\_MIMETYPE\_VIDEO\_MJPEG](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avcodec-base-h#variables) |
| MPEG2 | [OH\_AVCODEC\_MIMETYPE\_VIDEO\_MPEG2](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avcodec-base-h#variables) |
| MPEG4 | [OH\_AVCODEC\_MIMETYPE\_VIDEO\_MPEG4](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avcodec-base-h#variables) |
| H.263 | [OH\_AVCODEC\_MIMETYPE\_VIDEO\_H263](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avcodec-base-h#variables) |
| AVC(H.264) | [OH\_AVCODEC\_MIMETYPE\_VIDEO\_AVC](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avcodec-base-h#variables) |
| HEVC(H.265) | [OH\_AVCODEC\_MIMETYPE\_VIDEO\_HEVC](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avcodec-base-h#variables) |
| , VVC (H.266) |  |

When you attempt to create a decoder using the MIME type, if the system supports hardware decoding, the system preferentially creates a hardware decoder instance. If the system does not support hardware decoding or the hardware decoder resources are insufficient, the system creates a software decoder instance.

The decoding capability provided by the system is closely related to the device. You can obtain the supported capabilities and specifications by following the instructions provided in [Obtaining Supported Codecs](../audio-and-video-codecs/obtaining-supported-codecs/document.md).

For example, you can query the hardware decoding capabilities of H.264, H.265, and H.266 by using OH\_AVCODEC\_MIMETYPE\_VIDEO\_AVC, OH\_AVCODEC\_MIMETYPE\_VIDEO\_HEVC, OH\_AVCODEC\_MIMETYPE\_VIDEO\_VVC.

For details about the development guide, see [Video Decoding](../audio-and-video-codecs/video-decoding/document.md).

## Video Encoding

Currently, the following encoding capabilities are supported:

| Video Encoding Type | MIME Type for Video Encoding Format |
| :-- | :-- |
| HEVC(H.265) | [OH\_AVCODEC\_MIMETYPE\_VIDEO\_HEVC](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avcodec-base-h#variables) |
| AVC(H.264) | [OH\_AVCODEC\_MIMETYPE\_VIDEO\_AVC](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avcodec-base-h#variables) |

If the system does not support the required encoding capability, the encoder instance fails to be created.

Supported MIME types for encoder creation include H.264 (OH\_AVCODEC\_MIMETYPE\_VIDEO\_AVC) and H.265 (OH\_AVCODEC\_MIMETYPE\_VIDEO\_HEVC).

You can obtain the supported capabilities and specifications by following the instructions provided in [Obtaining Supported Codecs](../audio-and-video-codecs/obtaining-supported-codecs/document.md).

For details about the development guide, see [Video Encoding](../audio-and-video-codecs/video-encoding/document.md).

## Audio Decoding

Currently, the following decoding capabilities are supported:

| Audio Decoding Type | MIME Type for Audio Decoding Format |
| :-- | :-- |
| AAC | [OH\_AVCODEC\_MIMETYPE\_AUDIO\_AAC](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avcodec-base-h#variables) |
| MPEG(MP3) | [OH\_AVCODEC\_MIMETYPE\_AUDIO\_MPEG](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avcodec-base-h#variables) |
| Flac | [OH\_AVCODEC\_MIMETYPE\_AUDIO\_FLAC](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avcodec-base-h#variables) |
| Vorbis | [OH\_AVCODEC\_MIMETYPE\_AUDIO\_VORBIS](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avcodec-base-h#variables) |
| AMR (AMR-NB and AMR-WB) | [OH\_AVCODEC\_MIMETYPE\_AUDIO\_AMR\_NB](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avcodec-base-h#variables) and [OH\_AVCODEC\_MIMETYPE\_AUDIO\_AMR\_WB](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avcodec-base-h#variables) |
| G711mu | [OH\_AVCODEC\_MIMETYPE\_AUDIO\_G711MU](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avcodec-base-h#variables) |
| APE | [OH\_AVCODEC\_MIMETYPE\_AUDIO\_APE](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avcodec-base-h#variables) |
| G711a20+ | [OH\_AVCODEC\_MIMETYPE\_AUDIO\_G711A](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avcodec-base-h#variables) |
| ALAC22+ | [OH\_AVCODEC\_MIMETYPE\_AUDIO\_ALAC](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avcodec-base-h#variables) |
| AC322+ | [OH\_AVCODEC\_MIMETYPE\_AUDIO\_AC3](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avcodec-base-h#variables) |
| WMA22+(V1, V2, PRO) | [OH\_AVCODEC\_MIMETYPE\_AUDIO\_WMAV1](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avcodec-base-h#variables), [OH\_AVCODEC\_MIMETYPE\_AUDIO\_WMAV2](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avcodec-base-h#variables), and [OH\_AVCODEC\_MIMETYPE\_AUDIO\_WMAPRO](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avcodec-base-h#variables) |
| GSM22+ | [OH\_AVCODEC\_MIMETYPE\_AUDIO\_GSM](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avcodec-base-h#variables) |
| GSM\_MS22+ | [OH\_AVCODEC\_MIMETYPE\_AUDIO\_GSM\_MS](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avcodec-base-h#variables) |
| , Audio ViVid11+, Opus |  |

If the system does not support the required decoding capability, the decoder instance fails to be created.

The decoding capability provided by the system is closely related to the device. You can obtain the supported capabilities and specifications by following the instructions provided in [Obtaining Supported Codecs](../audio-and-video-codecs/obtaining-supported-codecs/document.md).

For details about the development guide, see [Audio Decoding](../audio-and-video-codecs/audio-decoding/document.md).

## Audio Encoding

Currently, the following encoding capabilities are supported:

| Audio Encoding Type | MIME Type for Audio Encoding Format |
| :-- | :-- |
| AAC | [OH\_AVCODEC\_MIMETYPE\_AUDIO\_AAC](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avcodec-base-h#variables) |
| Flac | [OH\_AVCODEC\_MIMETYPE\_AUDIO\_FLAC](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avcodec-base-h#variables) |
| MPEG(MP3) | [OH\_AVCODEC\_MIMETYPE\_AUDIO\_MPEG](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avcodec-base-h#variables) |
| G711mu | [OH\_AVCODEC\_MIMETYPE\_AUDIO\_G711MU](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avcodec-base-h#variables) |
| , AMR (AMR-NB, AMR-WB), Opus |  |

-   H265(OH\_AVCODEC\_MIMETYPE\_VIDEO\_HEVC)

If the system does not support the required encoding capability, the encoder instance fails to be created.

The encoding capability provided by the system is closely related to the device. You can obtain the supported capabilities and specifications by following the instructions provided in [Obtaining Supported Codecs](../audio-and-video-codecs/obtaining-supported-codecs/document.md).

For details about the development guide, see [Audio Encoding](../audio-and-video-codecs/audio-encoding/document.md).

#### Media Data Multiplexing and Demultiplexing

## Media Data Demultiplexing

The following formats are supported:

| Media Format | Container Format | Track Format |
| :-- | :-- | :-- |
| Audio/Video | mp4 | 
Video track: AVC (H.264), HEVC (H.265), VVC (H.266), MPEG4

Audio track: AAC, MPEG (MP3), Audio Vivid

Subtitle track: WEBVTT

Auxiliary track: PREY (H.265), DEPTH (H.265), AUXL (AAC and MP3)

Timed metadata track

 |
| Audio/Video | fmp4 | 

Video track: AVC (H.264), HEVC(H.265)

Audio track: AAC, MPEG (MP3), Audio Vivid

 |
| Audio/Video | mkv | 

Video track: AVC (H.264), HEVC(H.265)

Audio track: AAC, MPEG (MP3), Opus

 |
| Audio/Video | mpeg-ts | 

Video track: AVC (H.264), HEVC (H.265), MPEG2, MPEG4

Audio track: AAC, MPEG (MP3), Audio Vivid

 |
| Audio/Video | flv | 

Video track: AVC (H.264), HEVC(H.265)

Audio track: AAC

 |
| Audio/Video | mpeg-ps | 

Video track: AVC (H.264), MPEG2

Audio track: MPEG (MP2, MP3)

 |
| Audio/Video | avi | 

Video track: H.263, AVC(H.264), MPEG2, MPEG4, MJPEG22+, MSVIDEO122+

Audio track: AAC, MPEG (MP2, MP3), PCM, GSM\_MS22+, ADPCM\_YAMAHA22+, ADPCM\_G72222+

 |
| Audio/Video | 3gp22+ | 

Video track: H.263, AVC (H.264), MPEG4

Audio track: AAC, AMR (amrnb and amrwb)

 |
| Audio/Video | 3g222+ | 

Video track: H.263, AVC (H.264), MPEG4

Audio track: AAC, AMR (amrnb and amrwb)

 |
| Audio/Video | m4v22+ | 

, HEVC (H.265)

Audio track: AAC, ALAC, AC3

 |
| Audio/Video | wmv22+ | 

Video track: AVC (H.264), WMV3

Audio track: WMAV1, WMAV2, WMAPRO

 |
| Audio | m4a | Audio track: AAC, Audio Vivid |
| Audio | aac | Audio track: AAC |
| Audio | mp3 | Audio track: MPEG (MP3) |
| Audio | ogg | Audio track: Vorbis |
| Audio | flac | Audio track: FLAC |
| Audio | wav | Audio track: PCM, G711mu, G711a, GSM\_MS22+, ADPCM\_YAMAHA22+, ADPCM\_G72222+, ADPCM\_G72622+ |
| Audio | amr | Audio track: AMR (amrnb and amrwb) |
| Audio | ape | Audio track: APE |
| Audio | wma22+ | Audio track: AC3, WMAV1, WMAV2, Vorbis, Flac, AMR (amrnb and amrwb), AAC, MPEG (MP2 and MP3), GSM\_MS, G711mu, G711a, PCM, ADPCM\_G722, ADPCM\_G726, ADPCM\_IMA\_WAV, ADPCM\_MS, ADPCM\_YAMAHA |
| External subtitle | srt | Subtitle track: SRT |
| External subtitle | webvtt | Subtitle track: WEBVTT |

The DRM demultiplexing capability supports the following formats: mp4 (H.264, H.265, and AAC), MPEG-TS (H.264, H.265, and AAC).

For details about the development guide, see [Media Data Demultiplexing](../media-data-multiplexing-and-demultiplexing/media-data-demultiplexing/document.md).

## Media Data Multiplexing

Currently, the following muxer capabilities are supported:

| Container Format | Video Codec Type | Audio Codec Type | Cover Type |
| :-- | :-- | :-- | :-- |
| mp4 | AVC (H.264) , HEVC (H.265) | AAC, MPEG (MP3) | jpeg, png, bmp |
| m4a | \- | AAC | jpeg, png, bmp |
| mp3 | \- | MPEG (MP3) | \- |
| amr | \- | AMR (AMR-NB and AMR-WB) | \- |
| wav | \- | G711mu (pcm-mulaw), raw (pcm) | \- |
| aac | \- | AAC | \- |
| flac | \- | Flac | jpeg, png, bmp |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/s9sy96qVTVSJDc9GfjG3Kw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062035Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C2E7ECB8F51C97F84F3CED349FB240CA4D285F924C26906E752F36E2E410BC3B)

-   When the container format is mp4 and the audio codec type is MPEG (MP3), the sample rate must be greater than or equal to 16000 Hz.
-   When the container format is mp4 or m4a and the audio codec type is AAC, the number of audio channels ranges from 1 to 7.

The keys defined for file-level data are as follows:

| key | Description |
| :-- | :-- |
| OH\_MD\_KEY\_CREATION\_TIME | Media file creation time. The value type is string. This key is supported since API version 14. |
| OH\_MD\_KEY\_COMMENT | Comment in a media file. The value type is string. This key is supported since API version 20. |
| OH\_MD\_KEY\_ENABLE\_MOOV\_FRONT | Whether the moov metadata should be at the front of a media file. The value type is int32\_t. This key is supported since API version 20. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/caphfMD_QB2bMQ4sxb4i0g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062035Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=59AC1A35E00C8A8609EF5D40C51550574EC655A4DA00233E105FBE45E38A8ABA)

Custom keys must start with **"com.openharmony."**. The value type can be int32\_t, float, or string. The value type uint8\_t\* is supported since API version 20.

Key values of configuration options are described as follows:

mp4 container format:

| key | Description | aac | mp3 | H.264 | H.265 | jpg | png | bmp |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| OH\_MD\_KEY\_AUD\_SAMPLE\_RATE | Sample rate. | Mandatory | Mandatory | \- | \- | \- | \- | \- |
| OH\_MD\_KEY\_AUD\_CHANNEL\_COUNT | Audio channel count. | Mandatory | Mandatory | \- | \- | \- | \- | \- |
| OH\_MD\_KEY\_AUDIO\_SAMPLE\_FORMAT | Output audio stream format. | Optional | Optional | \- | \- | \- | \- | \- |
| OH\_MD\_KEY\_CHANNEL\_LAYOUT | Channel layout. | Optional | Optional | \- | \- | \- | \- | \- |
| OH\_MD\_KEY\_PROFILE | Encoding profile. | Optional | \- | \- | \- | \- | \- | \- |
| OH\_MD\_KEY\_BITRATE | Bit rate. | Optional | Optional | Optional | Optional | \- | \- | \- |
| OH\_MD\_KEY\_CODEC\_CONFIG | Codec-specific data. | Optional | \- | Optional | Optional | \- | \- | \- |
| OH\_MD\_KEY\_WIDTH | Width. | \- | \- | Mandatory | Mandatory | Mandatory | Mandatory | Mandatory |
| OH\_MD\_KEY\_HEIGHT | Height. | \- | \- | Mandatory | Mandatory | Mandatory | Mandatory | Mandatory |
| OH\_MD\_KEY\_FRAME\_RATE | Video stream frame rate. | \- | \- | Optional | Optional | \- | \- | \- |
| OH\_MD\_KEY\_COLOR\_PRIMARIES | Video color gamut. | \- | \- | Optional | Optional | \- | \- | \- |
| OH\_MD\_KEY\_TRANSFER\_CHARACTERISTICS | Video transfer characteristics function. | \- | \- | Optional | Optional | \- | \- | \- |
| OH\_MD\_KEY\_MATRIX\_COEFFICIENTS | Video matrix coefficient. | \- | \- | Optional | Optional | \- | \- | \- |
| OH\_MD\_KEY\_RANGE\_FLAG | Value range flag. | \- | \- | Optional | Optional | \- | \- | \- |
| OH\_MD\_KEY\_VIDEO\_IS\_HDR\_VIVID | Whether the video track is an HDR Vivid. | \- | \- | \- | Optional | \- | \- | \- |

MP4 container format of the auxiliary track:

| key | Description | aac | mp3 | H.264 | H.265 |
| :-- | :-- | :-- | :-- | :-- | :-- |
| OH\_MD\_KEY\_TRACK\_TYPE | Media type of the track. | Mandatory | Mandatory | Mandatory | Mandatory |
| OH\_MD\_KEY\_TRACK\_REFERENCE\_TYPE | Reference type of the track. | Mandatory | Mandatory | Mandatory | Mandatory |
| OH\_MD\_KEY\_TRACK\_DESCRIPTION | Track ID. | Mandatory | Mandatory | Mandatory | Mandatory |
| OH\_MD\_KEY\_REFERENCE\_TRACK\_IDS | Reference track number. | Mandatory | Mandatory | Mandatory | Mandatory |
| OH\_MD\_KEY\_AUD\_SAMPLE\_RATE | Sample rate. | Mandatory | Mandatory | \- | \- |
| OH\_MD\_KEY\_AUD\_CHANNEL\_COUNT | Audio channel count. | Mandatory | Mandatory | \- | \- |
| OH\_MD\_KEY\_AUDIO\_SAMPLE\_FORMAT | Output audio stream format. | Optional | Optional | \- | \- |
| OH\_MD\_KEY\_CHANNEL\_LAYOUT | Channel layout. | Optional | Optional | \- | \- |
| OH\_MD\_KEY\_PROFILE | Encoding profile. | Optional | \- | \- | \- |
| OH\_MD\_KEY\_BITRATE | Bit rate. | Optional | Optional | Optional | Optional |
| OH\_MD\_KEY\_CODEC\_CONFIG | Codec-specific data. | Optional | \- | Optional | Optional |
| OH\_MD\_KEY\_WIDTH | Width. | \- | \- | Mandatory | Mandatory |
| OH\_MD\_KEY\_HEIGHT | Height. | \- | \- | Mandatory | Mandatory |
| OH\_MD\_KEY\_FRAME\_RATE | Video stream frame rate. | \- | \- | Optional | Optional |
| OH\_MD\_KEY\_COLOR\_PRIMARIES | Video color gamut. | \- | \- | Optional | Optional |
| OH\_MD\_KEY\_TRANSFER\_CHARACTERISTICS | Video transfer characteristics function. | \- | \- | Optional | Optional |
| OH\_MD\_KEY\_MATRIX\_COEFFICIENTS | Video matrix coefficient. | \- | \- | Optional | Optional |
| OH\_MD\_KEY\_RANGE\_FLAG | Value range flag. | \- | \- | Optional | Optional |
| OH\_MD\_KEY\_VIDEO\_IS\_HDR\_VIVID | Whether the video track is an HDR Vivid. | \- | \- | \- | Optional |

m4a container format:

| key | Description | aac | jpg | png | bmp |
| :-- | :-- | :-- | :-- | :-- | :-- |
| OH\_MD\_KEY\_AUD\_SAMPLE\_RATE | Sample rate. | Mandatory | \- | \- | \- |
| OH\_MD\_KEY\_AUD\_CHANNEL\_COUNT | Audio channel count. | Mandatory | \- | \- | \- |
| OH\_MD\_KEY\_AUDIO\_SAMPLE\_FORMAT | Output audio stream format. | Optional | \- | \- | \- |
| OH\_MD\_KEY\_CHANNEL\_LAYOUT | Channel layout. | Optional | \- | \- | \- |
| OH\_MD\_KEY\_PROFILE | Encoding profile. | Optional | \- | \- | \- |
| OH\_MD\_KEY\_BITRATE | Bit rate. | Optional | \- | \- | \- |
| OH\_MD\_KEY\_CODEC\_CONFIG | Codec-specific data. | Optional | \- | \- | \- |
| OH\_MD\_KEY\_WIDTH | Width. | \- | Mandatory | Mandatory | Mandatory |
| OH\_MD\_KEY\_HEIGHT | Height. | \- | Mandatory | Mandatory | Mandatory |

amr container format:

| key | Description | amr\_nb | amr\_wb |
| :-- | :-- | :-- | :-- |
| OH\_MD\_KEY\_AUD\_SAMPLE\_RATE | Sample rate. | Mandatory | Mandatory |
| OH\_MD\_KEY\_AUD\_CHANNEL\_COUNT | Audio channel count. | Mandatory | Mandatory |
| OH\_MD\_KEY\_AUDIO\_SAMPLE\_FORMAT | Output audio stream format. | Optional | Optional |
| OH\_MD\_KEY\_CHANNEL\_LAYOUT | Channel layout. | Optional | Optional |
| OH\_MD\_KEY\_BITRATE | Bit rate. | Optional | Optional |

mp3 container format:

| key | Description | mp3 | jpg |
| :-- | :-- | :-- | :-- |
| OH\_MD\_KEY\_AUD\_SAMPLE\_RATE | Sample rate. | Mandatory | \- |
| OH\_MD\_KEY\_AUD\_CHANNEL\_COUNT | Audio channel count. | Mandatory | \- |
| OH\_MD\_KEY\_AUDIO\_SAMPLE\_FORMAT | Output audio stream format. | Optional | \- |
| OH\_MD\_KEY\_CHANNEL\_LAYOUT | Channel layout. | Optional | \- |
| OH\_MD\_KEY\_BITRATE | Bit rate. | Optional | \- |
| OH\_MD\_KEY\_WIDTH | Width. | \- | Mandatory |
| OH\_MD\_KEY\_HEIGHT | Height. | \- | Mandatory |

wav container format:

| key | Description | g711mu | raw |
| :-- | :-- | :-- | :-- |
| OH\_MD\_KEY\_AUD\_SAMPLE\_RATE | Sample rate. | Mandatory | Mandatory |
| OH\_MD\_KEY\_AUD\_CHANNEL\_COUNT | Audio channel count. | Mandatory | Mandatory |
| OH\_MD\_KEY\_AUDIO\_SAMPLE\_FORMAT | Output audio stream format. | Optional | Mandatory |
| OH\_MD\_KEY\_CHANNEL\_LAYOUT | Channel layout. | Optional | Optional |
| OH\_MD\_KEY\_BITRATE | Bit rate. | Mandatory | Optional |

aac container format:

| key | Description | aac |
| :-- | :-- | :-- |
| OH\_MD\_KEY\_AUD\_SAMPLE\_RATE | Sample rate. | Mandatory |
| OH\_MD\_KEY\_AUD\_CHANNEL\_COUNT | Audio channel count. | Mandatory |
| OH\_MD\_KEY\_AUDIO\_SAMPLE\_FORMAT | Output audio stream format. | Optional |
| OH\_MD\_KEY\_CHANNEL\_LAYOUT | Channel layout. | Optional |
| OH\_MD\_KEY\_BITRATE | Bit rate. | Optional |
| OH\_MD\_KEY\_PROFILE | Encoding profile. | Mandatory |
| OH\_MD\_KEY\_AAC\_IS\_ADTS | Whether the format is ADTS. | Mandatory |

flac container format:

| key | Description | flac |
| :-- | :-- | :-- |
| OH\_MD\_KEY\_AUD\_SAMPLE\_RATE | Sample rate. | Mandatory |
| OH\_MD\_KEY\_AUD\_CHANNEL\_COUNT | Audio channel count. | Mandatory |
| OH\_MD\_KEY\_AUDIO\_SAMPLE\_FORMAT | Output audio stream format. | Mandatory |
| OH\_MD\_KEY\_CHANNEL\_LAYOUT | Channel layout. | Optional |
| OH\_MD\_KEY\_BITRATE | Bit rate. | Optional |
| OH\_MD\_KEY\_CODEC\_CONFIG | Codec-specific data. | Optional |

For details about the development guide, see [Media Data Multiplexing](../media-data-multiplexing-and-demultiplexing/media-data-multiplexing/document.md).
