# CodecBase

#### Overview

The CodecBase module provides the variables, attributes, and functions for basic audio and video multiplexing, demultiplexing, encoding, and decoding.

**System capability**: SystemCapability.Multimedia.Media.CodecBase

**Since**: 9

#### Files

| Name | Description |
| :-- | :-- |
| [avcodec\_audio\_channel\_layout.h](../../apis-no-longer-maintained/header-files/avcodec-audio-channel-layout-h/document.md) | Declares the enums used for audio codec channel layouts. |
| [native\_avcodec\_base.h](../../header-files/native-avcodec-base-h/document.md) | Declares the native APIs used for basic audio and video multiplexing, demultiplexing, encoding, and decoding. |

#### Media Codec Formats

The table below lists the media codec formats. The type is a constant string.

| Name | Description |
| :-- | :-- |
| OH\_AVCODEC\_MIMETYPE\_AUDIO\_AAC | MIME type of the AAC audio codec. |
| OH\_AVCODEC\_MIMETYPE\_AUDIO\_FLAC | MIME type of the FLAC audio codec. |
| OH\_AVCODEC\_MIMETYPE\_AUDIO\_OPUS | MIME type of the Opus audio codec. |
| OH\_AVCODEC\_MIMETYPE\_AUDIO\_G711MU | MIME type of the G.711 mu-law audio codec. |
| OH\_AVCODEC\_MIMETYPE\_AUDIO\_G711A | MIME type of the G.711 a-law audio decoder. |
| OH\_AVCODEC\_MIMETYPE\_AUDIO\_RAW | MIME type of raw audio streams. |
| OH\_AVCODEC\_MIMETYPE\_AUDIO\_VORBIS | MIME type of the Vorbis audio decoder. |
| OH\_AVCODEC\_MIMETYPE\_AUDIO\_MPEG | MIME type of the MP3 audio codec. |
| OH\_AVCODEC\_MIMETYPE\_AUDIO\_VIVID | MIME type of the Audio Vivid audio decoder. |
| OH\_AVCODEC\_MIMETYPE\_AUDIO\_AMR\_NB | MIME type of the AMR-NB audio decoder. |
| OH\_AVCODEC\_MIMETYPE\_AUDIO\_AMR\_WB | MIME type of the AMR-WB audio decoder. |
| OH\_AVCODEC\_MIMETYPE\_AUDIO\_APE | MIME type of the APE audio decoder. |
| OH\_AVCODEC\_MIMETYPE\_AUDIO\_ALAC | MIME type of the Apple Lossless Audio Codec (ALAC) audio decoder. |
| OH\_AVCODEC\_MIMETYPE\_AUDIO\_AC3 | MIME type of the Dolby Audio Coding 3 (AC 3) audio decoder. |
| OH\_AVCODEC\_MIMETYPE\_AUDIO\_EAC3 | MIME type of the Enhanced AC-3 (EAC3) audio decoder. |
| OH\_AVCODEC\_MIMETYPE\_AUDIO\_WMAV1 | MIME type of the Windows Media Audio (WMA) V1 audio decoder. |
| OH\_AVCODEC\_MIMETYPE\_AUDIO\_WMAV2 | MIME type of the WMA V2 audio decoder. |
| OH\_AVCODEC\_MIMETYPE\_AUDIO\_WMAPRO | MIME type of the WMA Pro audio decoder. |
| OH\_AVCODEC\_MIMETYPE\_AUDIO\_GSM | MIME type of the Global System for Mobile Communications (GSM) audio decoder. |
| OH\_AVCODEC\_MIMETYPE\_AUDIO\_GSM\_MS | MIME type of the GSM Microsoft variant (MS) audio decoder. |
| OH\_AVCODEC\_MIMETYPE\_VIDEO\_VVC | MIME type of the VVC (H.266) video codec. |
| OH\_AVCODEC\_MIMETYPE\_VIDEO\_HEVC | MIME type of the HEVC (H.265) video codec. |
| OH\_AVCODEC\_MIMETYPE\_VIDEO\_AVC | MIME type of the AVC (H.264) video codec. |
| OH\_AVCODEC\_MIMETYPE\_VIDEO\_H263 | MIME type of the H.263 video codec. |
| OH\_AVCODEC\_MIMETYPE\_VIDEO\_VC1 | 
MIME type of the VC-1 video codec.

This specification is supported since API version 22.

 |
| OH\_AVCODEC\_MIMETYPE\_VIDEO\_MSVIDEO1 | 

MIME type of the Microsoft Video 1 (MSVIDEO1) video codec.

This specification is supported since API version 22.

 |
| OH\_AVCODEC\_MIMETYPE\_VIDEO\_WMV3 | 

MIME type of the WMV3 video codec.

This specification is supported since API version 22.

 |
| OH\_AVCODEC\_MIMETYPE\_VIDEO\_MJPEG | 

MIME type of the Motion JPEG (MJPEG) video codec.

This specification is supported since API version 22.

 |
| OH\_AVCODEC\_MIMETYPE\_VIDEO\_MPEG4 | MIME type of the MPEG4 video encoder, which is used only for multiplexing MPEG4 video streams. (It is deprecated from API version 11.) |
| OH\_AVCODEC\_MIMETYPE\_VIDEO\_MPEG4\_PART2 | MIME type of the MPEG4 Part 2 video codec. |
| OH\_AVCODEC\_MIMETYPE\_VIDEO\_MPEG2 | MIME type of the MPEG2 video codec. |
| OH\_AVCODEC\_MIMETYPE\_IMAGE\_JPG | MIME type of the JPG image encoder, which is used only for multiplexing JPG covers. |
| OH\_AVCODEC\_MIMETYPE\_IMAGE\_PNG | MIME type of the PNG image encoder, which is used only for multiplexing PNG covers. |
| OH\_AVCODEC\_MIMETYPE\_IMAGE\_BMP | MIME type of the BMP image encoder, which is used only for multiplexing BMP covers. |
| OH\_AVCODEC\_MIMETYPE\_SUBTITLE\_WEBVTT | MIME type of the WEBVTT subtitle demuxer. |
| OH\_AVCODEC\_MIMETYPE\_SUBTITLE\_SRT | MIME type of the SRT subtitle demuxer. |

#### Media Data Key-Value Pairs

The tables below list the key-value pairs used to describe media data. The key type is a constant string, and the value type can be int32\_t, int64\_t, float, double, char \*, or uint8\_t \*.

The [OH\_AVFormat](../../structs/oh-avformat/document.md) API is used to configure or query parameters.

#### \[h2\]Key-Value Pairs Dedicated for Capability Query

| Name | Description |
| :-- | :-- |
| OH\_FEATURE\_PROPERTY\_KEY\_VIDEO\_ENCODER\_MAX\_LTR\_FRAME\_COUNT | Maximum number of long-term reference (LTR) frames obtained during video encoding. The value type is int32\_t. |

#### \[h2\]Common Key-value Pairs of Audio and Video

| Name | Description |
| :-- | :-- |
| OH\_MD\_KEY\_CODEC\_CONFIG | Codec-specific data. In the case of video, data carried in **SPS/PPS** is transferred. In the case of audio, data carried in **extraData** is transferred. The value type is uint8\_t\*. This key is optional. |
| OH\_MD\_MAX\_INPUT\_BUFFER\_COUNT | Maximum number of input buffers. The value type is int32\_t. This key is optional. |
| OH\_MD\_MAX\_OUTPUT\_BUFFER\_COUNT | Maximum number of output buffers. The value type is int32\_t. This key is optional. |
| OH\_MD\_KEY\_BITRATE | Bit rate. The value type is int64\_t. This key is used in audio and video encoding scenarios. It is optional in video encoding scenarios. |
| OH\_MD\_KEY\_PROFILE | Encoding grading. The value type is int32\_t. For details, see [OH\_AVCProfile](../../header-files/native-avcodec-base-h/document.md#oh_avcprofile), [OH\_HEVCProfile](../../header-files/native-avcodec-base-h/document.md#oh_hevcprofile), and [OH\_AACProfile](../../header-files/native-avcodec-base-h/document.md#oh_aacprofile). This key is optional. |
| OH\_MD\_KEY\_MAX\_INPUT\_SIZE | Maximum size of an input stream to decode. The value type is int32\_t. This key is optional. |
| OH\_MD\_KEY\_ENABLE\_SYNC\_MODE | Enabled status of audio/video codec synchronization. The value type is int32\_t. **1** if enabled, **0** otherwise. This key is optional. By default, the feature is disabled. The key is used in the configuration phase. |

#### \[h2\]Key-Value Pairs Dedicated for Video

| Name | Description |
| :-- | :-- |
| OH\_ED\_KEY\_TIME\_STAMP | Surface buffer timestamp. The value is of the int64\_t type. This key is optional. (It is deprecated from API version 14.) |
| OH\_ED\_KEY\_EOS | End of stream for the surface buffer. The value type is int32\_t. This key is optional. (It is deprecated from API version 14.) |
| OH\_MD\_KEY\_WIDTH | Video width. The value type is int32\_t. |
| OH\_MD\_KEY\_HEIGHT | Video height. The value type is int32\_t. |
| OH\_MD\_KEY\_PIXEL\_FORMAT | Video pixel format. The value type is int32\_t. For details, see [OH\_AVPixelFormat](../../header-files/native-avformat-h/document.md#oh_avpixelformat). |
| OH\_MD\_KEY\_FRAME\_RATE | Video frame rate. The value type is double. This key is optional. |
| OH\_MD\_KEY\_RANGE\_FLAG | Video YUV value range flag. The value type is int32\_t. The value **1** means a full range, and **0** means a limited range. This key is optional. |
| OH\_MD\_KEY\_COLOR\_PRIMARIES | Video primary colors. The value type is int32\_t. For details, see [OH\_ColorPrimary](../../header-files/native-avcodec-base-h/document.md#oh_colorprimary). The value complies with Table 2 in H.273. This key is optional. |
| OH\_MD\_KEY\_TRANSFER\_CHARACTERISTICS | Video transfer characteristics. The value type is int32\_t. For details, see [OH\_TransferCharacteristic](../../header-files/native-avcodec-base-h/document.md#oh_transfercharacteristic). The value complies with Table 3 in H.273. This key is optional. |
| OH\_MD\_KEY\_MATRIX\_COEFFICIENTS | Video matrix coefficients. The value type is int32\_t. For details, see [OH\_MatrixCoefficient](../../header-files/native-avcodec-base-h/document.md#oh_matrixcoefficient). The value complies with Table 4 in H.273. This key is optional. |
| OH\_MD\_KEY\_VIDEO\_STRIDE | Stride of the video frame. The value type is int32\_t. This key is optional. |
| OH\_MD\_KEY\_VIDEO\_SLICE\_HEIGHT | Height of the video frame. The value type is int32\_t. This key is optional. |
| OH\_MD\_KEY\_VIDEO\_PIC\_WIDTH | Width of the video frame. The value type is int32\_t. This key is optional. |
| OH\_MD\_KEY\_VIDEO\_PIC\_HEIGHT | Height of the video frame. The value type is int32\_t. This key is optional. |
| OH\_MD\_KEY\_VIDEO\_ENABLE\_LOW\_LATENCY | Enabled status of low-latency video codec. The value type is int32\_t. **1** if enabled, **0** otherwise. This key is optional. By default, the feature is disabled. The key is used in the configuration phase. |
| OH\_MD\_KEY\_VIDEO\_ENCODE\_BITRATE\_MODE | Video encoding bit rate mode. The value type is int32\_t. For details, see [OH\_BitrateMode](../../header-files/native-avcodec-base-h/document.md#oh_bitratemode). This key is optional. |
| OH\_MD\_KEY\_QUALITY | Required encoding quality. The value type is int32\_t. This key applies only to encoders configured in constant quality mode. This key is optional. |
| OH\_MD\_KEY\_REQUEST\_I\_FRAME | Request for immediate encoding of I-frames. The value type is int32\_t. This key is optional. |
| OH\_MD\_KEY\_I\_FRAME\_INTERVAL | Key frame interval, in milliseconds. The value type is int32\_t. This key is optional and is used only for video encoding. |
| OH\_MD\_KEY\_VIDEO\_ENCODER\_ENABLE\_TEMPORAL\_SCALABILITY | Enabled status of temporal scalability. The value type is int32\_t. **1** if enabled, **0** otherwise. This key is optional and used only for video encoding. By default, this feature is disabled. The key is used in the configuration phase. |
| OH\_MD\_KEY\_VIDEO\_ENCODER\_TEMPORAL\_GOP\_SIZE | Size of a temporal image group. The value type is int32\_t. This key is valid only when temporal scalability is enabled. This key is optional and used only in the configuration phase of video encoding. |
| OH\_MD\_KEY\_VIDEO\_ENCODER\_TEMPORAL\_GOP\_REFERENCE\_MODE | Reference mode in a temporal image group. The value type is int32\_t. For details, see [OH\_TemporalGopReferenceMode](../../header-files/native-avcodec-base-h/document.md#oh_temporalgopreferencemode). This key is valid only when temporal scalability is enabled. This key is optional and used only in the configuration phase of video encoding. |
| OH\_MD\_KEY\_VIDEO\_ENCODER\_LTR\_FRAME\_COUNT | Number of LTR frames. The value type is int32\_t. The value must be within the supported value range. This key is optional and is used only for video encoding. |
| OH\_MD\_KEY\_VIDEO\_ENCODER\_PER\_FRAME\_MARK\_LTR | Whether the current frame is marked as an LTR frame. The value type is int32\_t. **1** if marked, **0** otherwise. This key is optional and is used only for video encoding. |
| OH\_MD\_KEY\_VIDEO\_ENCODER\_PER\_FRAME\_USE\_LTR | POC number of the LTR frame referenced by the current frame. The value type is int32\_t. This key is optional and is used only for video encoding. |
| OH\_MD\_KEY\_VIDEO\_PER\_FRAME\_IS\_LTR | Whether the frame corresponding to the stream output from the current [OH\_AVBuffer](../../structs/oh-avbuffer/document.md) is marked as an LTR frame. The value type is int32\_t. **1** if marked, **0** otherwise. This key is optional and used only for video encoding. The default value is **0**. |
| OH\_MD\_KEY\_VIDEO\_PER\_FRAME\_POC | POC number of the frame. The value type is int32\_t. This key is optional and is used only for video encoding. |
| OH\_MD\_KEY\_VIDEO\_ENCODER\_QP\_MAX | Maximum Quantization Parameter (QP) allowed by the video encoder. The value type is int32\_t. This key is optional and is used only for video encoding. |
| OH\_MD\_KEY\_VIDEO\_ENCODER\_QP\_MIN | Minimum QP allowed by the video encoder. The value type is int32\_t. This key is optional and is used only for video encoding. |
| OH\_MD\_KEY\_VIDEO\_ENCODER\_QP\_AVERAGE | Average QP of video frames. The value type is int32\_t. This key is optional and is used only for video encoding. |
| OH\_MD\_KEY\_VIDEO\_ENCODER\_MSE | Mean Squared Error (MSE) of video frames. The value type is double. This key is optional and is used only for video encoding. |
| OH\_MD\_KEY\_VIDEO\_ENCODER\_REPEAT\_PREVIOUS\_FRAME\_AFTER | Duration (in milliseconds) for which the last frame will be resubmitted repeatedly, if no new frame is available after the previous frame is submitted to the encoder. The value type is int32\_t. This key is used only in the configuration phase of video encoding in surface mode. |
| OH\_MD\_KEY\_VIDEO\_ENCODER\_REPEAT\_PREVIOUS\_MAX\_COUNT | Maximum number of times the encoder can repeat encoding the previous frame when no new frame is available. The value type is int32\_t. This key takes effect only when **OH\_MD\_KEY\_VIDEO\_ENCODER\_REPEAT\_PREVIOUS\_FRAME\_AFTER** is available and is used only in the configuration phase. |
| OH\_MD\_KEY\_VIDEO\_DECODER\_OUTPUT\_COLOR\_SPACE | Output color space of the video decoder. The value type is int32\_t. The supported value is **OH\_COLORSPACE\_BT709\_LIMIT**. |
| OH\_MD\_KEY\_ROTATION | Rotation angle of the surface, with a clockwise direction. The value type is int32\_t, and the value range is {0, 90, 180, 270}. The default value is 0. This key is optional and is used only for video decoding in surface mode This key is optional. |
| OH\_MD\_KEY\_SCALING\_MODE | Video scaling mode. The value type is int32\_t. For details, see [OH\_ScalingMode](../../header-files/native-avcodec-base-h/document.md#oh_scalingmode). This key is optional and is used only for video decoding in surface mode. You are advised to set the scaling mode by calling [OH\_NativeWindow\_NativeWindowSetScalingModeV2](../../../../../graphics/arkgraphics-2d/c-apis/header-files/external-window-h/document.md#oh_nativewindow_nativewindowsetscalingmodev2). (It is deprecated from API version 14.) |
| OH\_MD\_KEY\_VIDEO\_CROP\_TOP | Y-coordinate of the top edge of the crop rectangle. The value type is int32\_t. This key is optional and is used only for video decoding. |
| OH\_MD\_KEY\_VIDEO\_CROP\_BOTTOM | Y-coordinate of the bottom edge of the crop rectangle. The value type is int32\_t. This key is optional and is used only for video decoding. |
| OH\_MD\_KEY\_VIDEO\_CROP\_LEFT | X-coordinate of the left edge of the crop rectangle. The value type is int32\_t. This key is optional and is used only for video decoding. |
| OH\_MD\_KEY\_VIDEO\_CROP\_RIGHT | X-coordinate of the right edge of the crop rectangle. The value type is int32\_t. This key is optional and is used only for video decoding. |
| OH\_MD\_KEY\_VIDEO\_DECODER\_OUTPUT\_ENABLE\_VRR | Whether the decoder enables the video variable frame rate feature. The value type is int32\_t. This key is optional and is used only for video decoding. |
| OH\_MD\_KEY\_SQR\_FACTOR | Quality parameter in SQR mode. The value range is \[0, 51\] (same as the QP value in encoding). A smaller value indicates a higher output bit rate and better quality. The value type is int32\_t. This key is optional and is used only for video encoding. |
| OH\_MD\_KEY\_MAX\_BITRATE | Maximum bit rate in SQR mode. The value range can be obtained by calling [OH\_AVCapability\_GetEncoderBitrateRange](../../header-files/native-avcapability-h/document.md#oh_avcapability_getencoderbitraterange) and is the same as that of **OH\_MD\_KEY\_BITRATE**. The unit is bit/s. The value type is int64\_t. This key is optional and is used only for video encoding. |
| OH\_MD\_KEY\_VIDEO\_ENCODER\_ROI\_PARAMS | ROI encoding parameters, including the ROI area and deltaQp. The value type is char \*. This key is optional and is used only for video encoding. |
| OH\_MD\_KEY\_VIDEO\_ENCODER\_ENABLE\_PTS\_BASED\_RATECONTROL | Key for enabling the PTS-based bit rate control mode. The value type is int32\_t. **1** to enable, **0** otherwise. This key is optional and used only for video encoding. The default value is **0**. If this feature is enabled, each video frame must contain PTS information and be sent to the encoder. It is used in the configuration phase. |
| OH\_MD\_KEY\_VIDEO\_ENCODER\_ENABLE\_B\_FRAME | 
Key for enabling bidirectional predictive frame (B-frame) encoding. The value type is int32\_t. **1** to enable, **0** otherwise. This key is optional and used only for video encoding. The default value is **0**.

If enabled, the video encoder uses B-frame encoding, resulting in a decoding sequence different from the display sequence.

For a device that does not support B-frame encoding, the configured key does not take effect.

To check the device capability, use the [OH\_AVCapability\_IsFeatureSupported](../../header-files/native-avcapability-h/document.md#oh_avcapability_isfeaturesupported) API and the enumerated value [OH\_AVCapabilityFeature](../../header-files/native-avcapability-h/document.md#oh_avcapabilityfeature).VIDEO\_ENCODER\_B\_FRAME.

This key is used only by calling [OH\_VideoEncoder\_Configure](../../header-files/native-avcodec-videoencoder-h/document.md#oh_videoencoder_configure).

 |
| OH\_MD\_KEY\_VIDEO\_ENCODER\_MAX\_B\_FRAMES | 

Pointer to the key that describes the maximum number of consecutive B-frames supported by the video encoder. The value type is int32\_t. Note: This key is used only to query the encoder capability.

The usage specifications are as follows:

1\. To check whether the feature is supported, use the [OH\_AVCapability\_IsFeatureSupported](../../header-files/native-avcapability-h/document.md#oh_avcapability_isfeaturesupported) API and the enumerated value [OH\_AVCapabilityFeature](../../header-files/native-avcapability-h/document.md#oh_avcapabilityfeature).VIDEO\_ENCODER\_B\_FRAME.

2\. Obtain the OH\_AVFormat pointer through the [OH\_AVCapability\_GetFeatureProperties](../../header-files/native-avcapability-h/document.md#oh_avcapability_getfeatureproperties) API and the enumerated value [OH\_AVCapabilityFeature](../../header-files/native-avcapability-h/document.md#oh_avcapabilityfeature).VIDEO\_ENCODER\_B\_FRAME.

3\. Obtain the maximum number of B-frames through the [OH\_AVFormat\_GetIntValue](../../header-files/native-avformat-h/document.md#oh_avformat_getintvalue) API and this key.

 |
| OH\_MD\_KEY\_VIDEO\_DECODER\_BLANK\_FRAME\_ON\_SHUTDOWN | 

Pointer to the key that specifies whether to output blank frames when the video decoder is disabled. The value type is int32\_t. **1** to output, **0** otherwise. The default value is **0**. If this parameter is set to a non-zero value, the value **1** is used. This key is optional and is used only for video decoding in surface mode.

After this feature is enabled, the video decoder outputs blank frames (usually black) when the [OH\_VideoDecoder\_Stop](../../header-files/native-avcodec-videodecoder-h/document.md#oh_videodecoder_stop) or [OH\_VideoDecoder\_Destroy](../../header-files/native-avcodec-videodecoder-h/document.md#oh_videodecoder_destroy) API is called. This mechanism prevents frozen frames caused by sudden termination of the decoder.

 |
| OH\_MD\_KEY\_VIDEO\_NATIVE\_BUFFER\_FORMAT | 

Pointer to the key that is used to query the native buffer pixel format in video encoding and decoding. The value type is int32\_t.

For details, see the pixel formats defined in [OH\_NativeBuffer\_Format](../../../../../graphics/arkgraphics-2d/c-apis/header-files/buffer-common-h/document.md#oh_nativebuffer_format). This key is used in the following scenarios:

1\. Video decoding: Call [OH\_VideoDecoder\_GetOutputDescription](../../header-files/native-avcodec-videodecoder-h/document.md#oh_videodecoder_getoutputdescription) or [OH\_AVCodecOnStreamChanged](../../header-files/native-avcodec-base-h/document.md#oh_avcodeconstreamchanged) to obtain the current output format from the returned OH\_AVFormat object.

2\. Video encoding: Call [OH\_VideoEncoder\_GetInputDescription](../../header-files/native-avcodec-videoencoder-h/document.md#oh_videoencoder_getinputdescription) to obtain the current input format from the returned OH\_AVFormat object.

 |

#### \[h2\]Key-Value Pairs Dedicated for Audio

| Name | Description |
| :-- | :-- |
| OH\_MD\_KEY\_AUDIO\_SAMPLE\_FORMAT | Original audio format. The value type is int32\_t. For details, see [OH\_BitsPerSample](../../header-files/native-avcodec-base-h/document.md#oh_bitspersample). |
| OH\_MD\_KEY\_AUD\_CHANNEL\_COUNT | Number of audio channels. The value type is int32\_t. |
| OH\_MD\_KEY\_AUD\_SAMPLE\_RATE | Audio sampling rate. The value type is int32\_t. |
| OH\_MD\_KEY\_AUDIO\_COMPRESSION\_LEVEL | Audio codec compression level. The value type is int32\_t type. This key is used only for audio encoding. This key is optional. |
| OH\_MD\_KEY\_CHANNEL\_LAYOUT | Required encoding channel layout. The value type is int64\_t. This key applies only to encoders. For details, see [OH\_AudioChannelLayout](../../header-files/native-audio-channel-layout-h/document.md#oh_audiochannellayout). |
| OH\_MD\_KEY\_BITS\_PER\_CODED\_SAMPLE | 
Number of bits per sample. The value type is int32\_t. This key is optional.

In versions earlier than API version 20, this parameter must be set to **1** for FLAC encoding. Otherwise, **OH\_AudioCodec\_Configure** returns the error code **AV\_ERR\_INVALID\_VAL**. However, this parameter has no actual effect and does not affect the encoding result. Starting from API version 20, you do not need to set it anymore.

 |
| OH\_MD\_KEY\_SBR | AAC SBR format. The value type is int32\_t. This key applies to AAC encoders. This key is optional. |
| OH\_MD\_KEY\_COMPLIANCE\_LEVEL | FLAC compliance level. The value type is int32\_t. This key is used only for audio encoding. This key is optional. |
| OH\_MD\_KEY\_AAC\_IS\_ADTS | AAC format, which can be ADTS or LATM. The value type is int32\_t. This key applies to AAC decoders. This key is optional. |
| OH\_MD\_KEY\_IDENTIFICATION\_HEADER | Vorbis identification header. The value type is uint8\_t\*. This key applies only to Vorbis decoders. This key is optional. |
| OH\_MD\_KEY\_SETUP\_HEADER | Vorbis setup header. The value type is uint8\_t\*. This key applies only to Vorbis decoders. This key is optional. |
| OH\_MD\_KEY\_AUDIO\_OBJECT\_NUMBER | Number of audio objects. The value type is int32\_t. This key is used only for Audio Vivid decoding. This key is optional. |
| OH\_MD\_KEY\_AUDIO\_VIVID\_METADATA | Audio Vivid metadata. The value type is uint8\_t\*. This key is used only for Audio Vivid decoding. This key is optional. |
| OH\_MD\_KEY\_BLOCK\_ALIGN | Size of the audio data block, in bytes. The value type is int32\_t. This key is supported since API version 22 and must be configured only for WMAV1, WMAV2, and WMA PRO decoding. |

#### \[h2\]Key-Value Pairs Dedicated for Multiplexing and Demultiplexing

| Name | Description |
| :-- | :-- |
| OH\_MD\_KEY\_VIDEO\_IS\_HDR\_VIVID | Whether the video track in a media file is HDR Vivid. The value type is int32\_t. This key is used for both multiplexing and demultiplexing. This key is optional. |
| OH\_MD\_KEY\_START\_TIME | Start time of the first frame in a media file, measured in microseconds. The value type is int64\_t. This key is optional. |
| OH\_MD\_KEY\_TRACK\_START\_TIME | Start time of the track, measured in microseconds. The value type is int64\_t. This key is optional. |
| OH\_MD\_KEY\_TRACK\_TYPE | Track type in a media file. The value type is int32\_t. For details, see [OH\_MediaType](../../header-files/native-avcodec-base-h/document.md#oh_mediatype). This key is optional. |
| OH\_MD\_KEY\_DURATION | Duration in a media file. The value type is int64\_t. This key is optional. |
| OH\_MD\_KEY\_TITLE | Title of a media file . The value type is char \*. This key is optional. |
| OH\_MD\_KEY\_ARTIST | Artist. The value type is char \*. This key is optional. |
| OH\_MD\_KEY\_ALBUM | Album media file. The value type is char \*. This key is optional. |
| OH\_MD\_KEY\_ALBUM\_ARTIST | Album artist. The value type is char \*. This key is optional. |
| OH\_MD\_KEY\_DATE | Date of a media file, for example, 2024. The value type is char \*. This key is optional. |
| OH\_MD\_KEY\_COMMENT | Comment of a media file. The value type is char \*. This key is optional. |
| OH\_MD\_KEY\_GENRE | Genre in a media file. The value type is char \*. This key is optional. |
| OH\_MD\_KEY\_COPYRIGHT | Copyright of a media file. The value type is char \*. This key is optional. |
| OH\_MD\_KEY\_LANGUAGE | Language of a media file. The value type is char \*. This key is optional. |
| OH\_MD\_KEY\_DESCRIPTION | Description of a media file. The value type is char \*. This key is optional. |
| OH\_MD\_KEY\_LYRICS | Lyrics in a media file. The value type is char \*. This key is optional. |
| OH\_MD\_KEY\_TRACK\_COUNT | Number of tracks in a media file. The value type is int32\_t. This key is optional. |
| OH\_MD\_KEY\_BUFFER\_DURATION | Duration corresponding to the audio, video, or subtitle sample carried in AVBuffer, in microseconds. The value type is int64\_t. This key is optional. |
| OH\_MD\_KEY\_DECODING\_TIMESTAMP | Decoding timestamp corresponding to the audio, video, or subtitle sample carried in AVBuffer, in microseconds. The value type is int64\_t. This key is optional. |
| OH\_MD\_KEY\_CODEC\_MIME | [MIME](#media-codec-formats) type of the codec. The value type is char \*. This key is optional. |
| OH\_MD\_KEY\_VIDEO\_SAR | Aspect ratio of the sample. The value type is double. |
| OH\_MD\_KEY\_CREATION\_TIME | Media file creation time. The value type is char \*. |
| OH\_MD\_KEY\_REFERENCE\_TRACK\_IDS | Reference relationship between media file tracks. The value type is int32\_t\*. |
| OH\_MD\_KEY\_TRACK\_REFERENCE\_TYPE | Auxiliary track type of a media file. The value type is char \*. |
| OH\_MD\_KEY\_TRACK\_DESCRIPTION | Auxiliary track description of a media file. The value type is char \*. |
