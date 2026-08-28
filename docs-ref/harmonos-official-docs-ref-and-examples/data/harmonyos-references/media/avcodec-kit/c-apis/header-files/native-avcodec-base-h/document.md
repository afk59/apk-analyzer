# native\_avcodec\_base.h

#### Overview

The file declares the native APIs used for basic audio and video multiplexing, demultiplexing, encoding, and decoding.

**File to include**: <multimedia/player\_framework/native\_avcodec\_base.h>

**Library**: libnative\_media\_codecbase.so

**System capability**: SystemCapability.Multimedia.Media.CodecBase

**Since**: 9

**Related module**: [CodecBase](../../modules/codecbase/document.md)

**Sample**: [AVCodec](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/BasicFeature/Media/AVCodec)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_AVCodecAsyncCallback](../../structs/oh-avcodecasynccallback/document.md) | OH\_AVCodecAsyncCallback | Describes all the asynchronous callback function pointers of an OH\_AVCodec instance. To ensure the normal running of OH\_AVCodec, you must register the instance of this struct with the OH\_AVCodec instance and process the information reported by the callback function. (It is deprecated from API version 11.) |
| [OH\_AVCodecCallback](../../structs/oh-avcodeccallback/document.md) | OH\_AVCodecCallback | Describes all the asynchronous callback function pointers of an OH\_AVCodec instance. To ensure the normal running of OH\_AVCodec, you must register the instance of this struct with the OH\_AVCodec instance and process the information reported by the callback function. |
| [OH\_AVDataSource](../../structs/oh-avdatasource/document.md) | OH\_AVDataSource | Describes a user-defined data source. |
| [OH\_AVDataSourceExt](../../structs/oh-avdatasourceext/document.md) | OH\_AVDataSourceExt | Describes a user-defined data source. User-defined data can be passed to its callback functions through the **userData** parameter. |
| [NativeWindow](../../structs/nativewindow/document.md) | OHNativeWindow | Describes a native object for the graphics interface. |
| [OH\_AVCodec](../../structs/oh-avcodec/document.md) | OH\_AVCodec | Describes a native object for the audio and video codec interface. |

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_MediaType](#oh_mediatype) | OH\_MediaType | Enumerates the media types. |
| [OH\_AACProfile](#oh_aacprofile) | OH\_AACProfile | Enumerates the Advanced Audio Coding (AAC) profiles. |
| [OH\_AVCProfile](#oh_avcprofile) | OH\_AVCProfile | Enumerates the Advanced Video Coding (AVC) profiles. |
| [OH\_HEVCProfile](#oh_hevcprofile) | OH\_HEVCProfile | Enumerates the High Efficiency Video Coding (HEVC) profiles. |
| [OH\_VVCProfile](#oh_vvcprofile) | OH\_VVCProfile | Enumerates the VVC profiles. |
| [OH\_MPEG2Profile](#oh_mpeg2profile) | OH\_MPEG2Profile | Enumerates the MPEG2 profiles. |
| [OH\_MPEG4Profile](#oh_mpeg4profile) | OH\_MPEG4Profile | Enumerates the MPEG4 profiles. |
| [OH\_H263Profile](#oh_h263profile) | OH\_H263Profile | Enumerates the H.263 profiles. |
| [OH\_VC1Profile](#oh_vc1profile) | OH\_VC1Profile | Enumerates the VC-1 profiles. |
| [OH\_WMV3Profile](#oh_wmv3profile) | OH\_WMV3Profile | Enumerates the WMV3 profiles. |
| [OH\_AVOutputFormat](#oh_avoutputformat) | OH\_AVOutputFormat | Enumerates the output file formats supported by a muxer. |
| [OH\_AVSeekMode](#oh_avseekmode) | OH\_AVSeekMode | Enumerates the seek modes. |
| [OH\_ScalingMode](#oh_scalingmode) | OH\_ScalingMode | Enumerates the scaling modes. This enum is used only in surface mode. (It is deprecated from API version 14.) |
| [OH\_BitsPerSample](#oh_bitspersample) | OH\_BitsPerSample | Enumerates the number of audio bits for each coded sample. |
| [OH\_ColorPrimary](#oh_colorprimary) | OH\_ColorPrimary | Enumerates the primary colors. This enum is used for both encoding and decoding. |
| [OH\_TransferCharacteristic](#oh_transfercharacteristic) | OH\_TransferCharacteristic | Enumerates the transfer characteristics. This enum is used for both encoding and decoding. |
| [OH\_MatrixCoefficient](#oh_matrixcoefficient) | OH\_MatrixCoefficient | Enumerates the matrix coefficients. This enum is used for both encoding and decoding. |
| [OH\_AVCLevel](#oh_avclevel) | OH\_AVCLevel | Enumerates the AVC levels. |
| [OH\_HEVCLevel](#oh_hevclevel) | OH\_HEVCLevel | Enumerates the HEVC levels. |
| [OH\_VVCLevel](#oh_vvclevel) | OH\_VVCLevel | Enumerates the VVC levels. |
| [OH\_MPEG2Level](#oh_mpeg2level) | OH\_MPEG2Level | Enumerates the MPEG2 levels. |
| [OH\_MPEG4Level](#oh_mpeg4level) | OH\_MPEG4Level | Enumerates the MPEG4 levels. |
| [OH\_H263Level](#oh_h263level) | OH\_H263Level | Enumerates the H.263 levels. |
| [OH\_VC1Level](#oh_vc1level) | OH\_VC1Level | Enumerates the VC-1 levels. |
| [OH\_WMV3Level](#oh_wmv3level) | OH\_WMV3Level | Enumerates the WMV3 levels. |
| [OH\_TemporalGopReferenceMode](#oh_temporalgopreferencemode) | OH\_TemporalGopReferenceMode | Enumerates the reference modes of temporal image groups. |
| [OH\_BitrateMode](#oh_bitratemode) | OH\_BitrateMode | Enumerates the bit rate modes of an encoder. |

#### \[h2\]Functions

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [typedef void (\*OH\_AVCodecOnError)(OH\_AVCodec \*codec, int32\_t errorCode, void \*userData)](#oh_avcodeconerror) | OH\_AVCodecOnError | Defines the pointer to the function that is called to report error information when an error occurs during the running of an OH\_AVCodec instance. |
| [typedef void (\*OH\_AVCodecOnStreamChanged)(OH\_AVCodec \*codec, OH\_AVFormat \*format, void \*userData)](#oh_avcodeconstreamchanged) | OH\_AVCodecOnStreamChanged | 
Defines the pointer to the function that is called to report the new stream description when the resolution of the input video stream being decoded or the output video stream that has been encoded changes.

Starting from API version 15, this function pointer is called to report the new stream description when the stream sampling rate, number of audio channels, or audio sampling format changes during audio decoding. The decoding formats that can detect these changes include AAC, FLAC, MP3, and VORBIS.

Note that the lifecycle of the pointer to the OH\_AVFormat instance is valid only when the function pointer is being called. Do not access the pointer to the instance after the function pointer is called.

 |
| [typedef void (\*OH\_AVCodecOnNeedInputData)(OH\_AVCodec \*codec, uint32\_t index, OH\_AVMemory \*data, void \*userData)](#oh_avcodeconneedinputdata) | OH\_AVCodecOnNeedInputData | Defines the pointer to the function that is called when new input data is required during the running of an OH\_AVCodec instance. The function carries a buffer to fill in new input data. (It is deprecated from API version 11.) |
| [typedef void (\*OH\_AVCodecOnNewOutputData)(OH\_AVCodec \*codec, uint32\_t index, OH\_AVMemory \*data, OH\_AVCodecBufferAttr \*attr, void \*userData)](#oh_avcodeconnewoutputdata) | OH\_AVCodecOnNewOutputData | Defines the pointer to the function that is called when new output data is generated during the running of an OH\_AVCodec instance. The function carries a buffer filled with new output data. Note that the lifecycle of the pointer to the OH\_AVCodecBufferAttr instance is valid only when the function pointer is being called. Do not access the pointer to the instance after the function pointer is called. (It is deprecated from API version 11.) |
| [typedef void (\*OH\_AVCodecOnNeedInputBuffer)(OH\_AVCodec \*codec, uint32\_t index, OH\_AVBuffer \*buffer, void \*userData)](#oh_avcodeconneedinputbuffer) | OH\_AVCodecOnNeedInputBuffer | Defines the pointer to the function that is called when new input data is required during the running of an OH\_AVCodec instance. The function carries a buffer to fill in new input data. |
| [typedef void (\*OH\_AVCodecOnNewOutputBuffer)(OH\_AVCodec \*codec, uint32\_t index, OH\_AVBuffer \*buffer, void \*userData)](#oh_avcodeconnewoutputbuffer) | OH\_AVCodecOnNewOutputBuffer | Defines the pointer to the function that is called when new output data is generated during the running of an OH\_AVCodec instance. The function carries a buffer filled with new output data. |
| [typedef int32\_t (\*OH\_AVDataSourceReadAt)(OH\_AVBuffer \*data, int32\_t length, int64\_t pos)](#oh_avdatasourcereadat) | OH\_AVDataSourceReadAt | Defines a function pointer used to provide the capability of obtaining user-defined media data. |
| [typedef int32\_t (\*OH\_AVDataSourceReadAtExt)(OH\_AVBuffer \*data, int32\_t length, int64\_t pos, void \*userData)](#oh_avdatasourcereadatext) | OH\_AVDataSourceReadAtExt | Defines a function pointer used to provide the capability of obtaining user-defined media data. |

#### \[h2\]Variables

| Name | Description |
| :-- | :-- |
| const char \* OH\_AVCODEC\_MIMETYPE\_VIDEO\_AVC | 
Pointer to the key that describes the MIME type of the AVC (H.264) video codec.

**Since**: 9

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_AVCODEC\_MIMETYPE\_AUDIO\_AAC | 

Pointer to the key that describes the MIME type of the AAC audio codec.

**Since**: 9

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_AVCODEC\_MIMETYPE\_AUDIO\_FLAC | 

Pointer to the key that describes the MIME type of the FLAC audio codec.

**Since**: 10

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_AVCODEC\_MIMETYPE\_AUDIO\_VORBIS | 

Pointer to the key that describes the MIME type of the Vorbis audio decoder.

**Since**: 10

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_AVCODEC\_MIMETYPE\_AUDIO\_MPEG | 

Pointer to the key that describes the MIME type of the MP3 audio codec.

**Since**: 10

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_AVCODEC\_MIMETYPE\_VIDEO\_HEVC | 

Pointer to the key that describes the MIME type of the HEVC (H.265) video codec.

**Since**: 10

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_AVCODEC\_MIMETYPE\_VIDEO\_MPEG4 | 

Pointer to the key that describes the MIME type of the MPEG4 video encoder, which is used only for multiplexing MPEG4 video streams.

**Since**: 10

**Deprecated from**: 11

**Substitute**: OH\_AVCODEC\_MIMETYPE\_VIDEO\_MPEG4\_PART2

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_AVCODEC\_MIMETYPE\_VIDEO\_MPEG4\_PART2 | 

Pointer to the key that describes the MIME type of the MPEG4 Part 2 video codec.

**Since**: 17

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_AVCODEC\_MIMETYPE\_VIDEO\_MPEG2 | 

Pointer to the key that describes the MIME type of the MPEG2 video codec.

**Since**: 17

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_AVCODEC\_MIMETYPE\_VIDEO\_H263 | 

Pointer to the key that describes the MIME type of the H.263 video codec.

**Since**: 17

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_AVCODEC\_MIMETYPE\_VIDEO\_VC1 | 

Pointer to the key that describes the MIME type of the VC-1 video codec.

**Since**: 22

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_AVCODEC\_MIMETYPE\_VIDEO\_MSVIDEO1 | 

Pointer to the key that describes the MIME type of the Microsoft Video 1 (MSVIDEO1) video codec.

**Since**: 22

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_AVCODEC\_MIMETYPE\_VIDEO\_WMV3 | 

Pointer to the key that describes the MIME type of the WMV3 video codec.

**Since**: 22

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_AVCODEC\_MIMETYPE\_VIDEO\_MJPEG | 

Pointer to the key that describes the MIME type of the Motion JPEG (MJPEG) video codec.

**Since**: 22

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_AVCODEC\_MIMETYPE\_IMAGE\_JPG | 

Pointer to the key that describes the MIME type of the JPG image encoder, which is used only for multiplexing JPG covers.

**Since**: 10

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_AVCODEC\_MIMETYPE\_IMAGE\_PNG | 

Pointer to the key that describes the MIME type of the PNG image encoder, which is used only for multiplexing PNG covers.

**Since**: 10

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_AVCODEC\_MIMETYPE\_IMAGE\_BMP | 

Pointer to the key that describes the MIME type of the BMP image encoder, which is used only for multiplexing BMP covers.

**Since**: 10

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_AVCODEC\_MIMETYPE\_AUDIO\_VIVID | 

Pointer to the key that describes the MIME type of the Audio Vivid audio decoder.

**Since**: 11

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_AVCODEC\_MIMETYPE\_AUDIO\_AMR\_NB | 

Pointer to the key that describes the MIME type of the AMR-NB audio decoder.

**Since**: 11

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_AVCODEC\_MIMETYPE\_AUDIO\_AMR\_WB | 

Pointer to the key that describes the MIME type of the AMR-WB audio decoder.

**Since**: 11

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_AVCODEC\_MIMETYPE\_AUDIO\_OPUS | 

Pointer to the key that describes the MIME type of the Opus audio codec.

**Since**: 11

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_AVCODEC\_MIMETYPE\_AUDIO\_G711MU | 

Pointer to the key that describes the MIME type of the G.711 mu-law audio codec.

**Since**: 11

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_AVCODEC\_MIMETYPE\_AUDIO\_ALAC | 

Pointer to the key that describes the MIME type of the Apple Lossless Audio Codec (ALAC) audio decoder.

**Since**: 22

 |
| const char \* OH\_AVCODEC\_MIMETYPE\_AUDIO\_AC3 | 

Pointer to the key that describes the MIME type of the Dolby Audio Coding 3 (AC 3) audio decoder.

**Since**: 22

 |
| const char \* OH\_AVCODEC\_MIMETYPE\_AUDIO\_EAC3 | 

Pointer to the key that describes the MIME type of the Enhanced AC-3 (EAC3) audio decoder.

**Since**: 22

 |
| const char \* OH\_AVCODEC\_MIMETYPE\_AUDIO\_WMAV1 | 

Pointer to the key that describes the MIME type of the Windows Media Audio (WMA) V1 audio decoder.

**Since**: 22

 |
| const char \* OH\_AVCODEC\_MIMETYPE\_AUDIO\_WMAV2 | 

Pointer to the key that describes the MIME type of the WMA V2 audio decoder.

**Since**: 22

 |
| const char \* OH\_AVCODEC\_MIMETYPE\_AUDIO\_WMAPRO | 

Pointer to the key that describes the MIME type of the WMA Pro audio decoder.

**Since**: 22

 |
| const char \* OH\_MD\_KEY\_BLOCK\_ALIGN | 

Size of the audio data block, in bytes. The value type is int32\_t. This key is used only for WMA (V1, V2, and PRO) decoders.

The allowed MIME types include **OH\_AVCODEC\_MIMETYPE\_AUDIO\_WMAV1**, **OH\_AVCODEC\_MIMETYPE\_AUDIO\_WMAV2**, and **OH\_AVCODEC\_MIMETYPE\_AUDIO\_WMAPRO**.

**Since**: 22

 |
| const char \* OH\_AVCODEC\_MIMETYPE\_AUDIO\_GSM | 

Pointer to the key that describes the MIME type of the Global System for Mobile Communications (GSM) audio decoder.

**Since**: 22

 |
| const char \* OH\_AVCODEC\_MIMETYPE\_AUDIO\_GSM\_MS | 

Pointer to the key that describes the MIME type of the GSM Microsoft variant (MS) audio decoder.

**Since**: 22

 |
| const char \* OH\_AVCODEC\_MIMETYPE\_VIDEO\_VVC | 

Pointer to the key that describes the MIME type of the VVC (H.266) video codec.

**Since**: 12

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_AVCODEC\_MIMETYPE\_AUDIO\_APE | 

Pointer to the key that describes the MIME type of the APE audio decoder.

**Since**: 12

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_AVCODEC\_MIMETYPE\_SUBTITLE\_SRT | 

Pointer to the key that describes the MIME type of the SRT subtitle demuxer.

**Since**: 12

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_AVCODEC\_MIMETYPE\_SUBTITLE\_WEBVTT | 

Pointer to the key that describes the MIME type of the WEBVTT subtitle demuxer.

**Since**: 12

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_AVCODEC\_MIMETYPE\_AUDIO\_RAW | 

Pointer to the key that describes the MIME type of raw audio streams.

**Since**: 18

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_AVCODEC\_MIMETYPE\_AUDIO\_G711A | 

Pointer to the key that describes the MIME type of the G.711 a-law audio decoder.

**Since**: 20

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_ED\_KEY\_TIME\_STAMP | 

Pointer to the key that describes the surface buffer timestamp. The value is of the int64\_t type.

**Since**: 9

**Deprecated from**: 14

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_ED\_KEY\_EOS | 

Pointer to the key that describes the end of stream for the surface buffer. The value type is int32\_t.

**Since**: 9

**Deprecated from**: 14

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_MD\_KEY\_TRACK\_TYPE | 

Pointer to the key that describes the track type in a media file. The value type is int32\_t. For details, see [OH\_MediaType](#oh_mediatype).

**Since**: 9

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_MD\_KEY\_CODEC\_MIME | 

Pointer to the key that describes the MIME type of the codec. The value type is char \*.

**Since**: 9

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_MD\_KEY\_DURATION | 

Pointer to the key that describes the duration in a media file, in microseconds. The value type is int64\_t.

**Since**: 9

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_MD\_KEY\_BITRATE | 

Pointer to the key that describes the bit rate. The value type is int64\_t. You can call [OH\_AVCapability\_GetEncoderBitrateRange](../native-avcapability-h/document.md#oh_avcapability_getencoderbitraterange) to obtain the value range.

**Since**: 9

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_MD\_KEY\_MAX\_INPUT\_SIZE | 

Pointer to the key that describes the maximum size of an input stream to decode. The value type is int32\_t.

**Since**: 9

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_MD\_KEY\_WIDTH | 

Pointer to the key that describes the video width. The value type is int32\_t.

This key is used to set the display width of a video frame when **Configure** is called during video encoding and decoding. You can call [OH\_AVCapability\_GetVideoWidthRange](../native-avcapability-h/document.md#oh_avcapability_getvideowidthrange) to obtain the value range.

**Since**: 9

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_MD\_KEY\_HEIGHT | 

Pointer to the key that describes the video height. The value type is int32\_t.

This key is used to set the display height of a video frame when **Configure** is called during video encoding and decoding. You can call [OH\_AVCapability\_GetVideoHeightRange](../native-avcapability-h/document.md#oh_avcapability_getvideoheightrange) to obtain the value range.

**Since**: 9

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_MD\_KEY\_PIXEL\_FORMAT | 

Pointer to the key that describes the video pixel format. The value type is int32\_t. For details, see [OH\_AVPixelFormat](../native-avformat-h/document.md#oh_avpixelformat).

**Since**: 9

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_MD\_KEY\_AUDIO\_SAMPLE\_FORMAT | 

Pointer to the key that describes the original audio format. The value type is int32\_t. For details, see [OH\_BitsPerSample](#oh_bitspersample).

**Since**: 9

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_MD\_KEY\_FRAME\_RATE | 

Pointer to the key that describes the video frame rate. The value type is double. The value must be greater than **0**. You can call [OH\_AVCapability\_GetVideoFrameRateRange](../native-avcapability-h/document.md#oh_avcapability_getvideoframeraterange) to obtain the value range.

**Since**: 9

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_MD\_KEY\_VIDEO\_ENCODE\_BITRATE\_MODE | 

Pointer to the key that describes the video encoding bit rate mode. The value type is int32\_t. For details, see [OH\_BitrateMode](#oh_bitratemode).

**Since**: 9

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_MD\_KEY\_PROFILE | 

Pointer to the key that describes the encoding grading. The value type is int32\_t. For details, see [OH\_AVCProfile](#oh_avcprofile), [OH\_HEVCProfile](#oh_hevcprofile), and [OH\_AACProfile](#oh_aacprofile). You can call [OH\_AVCapability\_GetSupportedProfiles](../native-avcapability-h/document.md#oh_avcapability_getsupportedprofiles) to obtain the supported profiles.

**Since**: 9

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_MD\_KEY\_AUD\_CHANNEL\_COUNT | 

Pointer to the key that describes the number of audio channels. The value type is int32\_t.

**Since**: 9

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_MD\_KEY\_AUD\_SAMPLE\_RATE | 

Pointer to the key that describes the audio sampling rate. The value type is int32\_t.

**Since**: 9

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_MD\_KEY\_I\_FRAME\_INTERVAL | 

Pointer to the key frame interval, in milliseconds. The value type is int32\_t. This key is optional and is used only for video encoding.

A negative value means that only the first frame is a keyframe. The value **0** means that all frames are keyframes. A positive value means one keyframe every (frameRate \* value)/1000 frames. The default value is **1000**.

**Since**: 9

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_MD\_KEY\_ROTATION | 

Pointer to the key that describes the rotation angle of the surface, with a clockwise direction. The value type is int32\_t, and the value range is {0, 90, 180, 270}. The default value is 0.

This key is optional and is used only for video decoding in surface mode

You are advised to use the **OH\_MD\_KEY\_VIDEO\_TRANSFORM\_TYPE** key to set the rotation angle of the surface for video decoding.

**Since**: 9

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_MD\_KEY\_VIDEO\_TRANSFORM\_TYPE | 

Pointer to the key that describes the video rotation angle. The value type is int32\_t. For details, see [OH\_NativeBuffer\_TransformType](../../../../../graphics/arkgraphics-2d/c-apis/header-files/buffer-common-h/document.md#oh_nativebuffer_transformtype).

This key is used to set the rotation angle of the surface for video decoding. The default value is **0** ([NATIVEBUFFER\_ROTATE\_NONE](../../../../../graphics/arkgraphics-2d/c-apis/header-files/buffer-common-h/document.md#oh_nativebuffer_transformtype)).

This key is mutually exclusive with **OH\_MD\_KEY\_ROTATION**. If both of them are set, **OH\_MD\_KEY\_VIDEO\_TRANSFORM\_TYPE** is used. **OH\_MD\_KEY\_VIDEO\_TRANSFORM\_TYPE** is recommended.

Note: The angle specified in **OH\_NativeBuffer\_TransformType** indicates a counter-clockwise rotation, which is opposite to the rotation direction defined by **OH\_MD\_KEY\_ROTATION**.

The mapping is as follows.

\- [NATIVEBUFFER\_ROTATE\_NONE](../../../../../graphics/arkgraphics-2d/c-apis/header-files/buffer-common-h/document.md#oh_nativebuffer_transformtype) is equivalent to OH\_MD\_KEY\_ROTATION = 0.

\- [NATIVEBUFFER\_ROTATE\_90](../../../../../graphics/arkgraphics-2d/c-apis/header-files/buffer-common-h/document.md#oh_nativebuffer_transformtype) is equivalent to OH\_MD\_KEY\_ROTATION = 270.

\- [NATIVEBUFFER\_ROTATE\_180](../../../../../graphics/arkgraphics-2d/c-apis/header-files/buffer-common-h/document.md#oh_nativebuffer_transformtype) is equivalent to OH\_MD\_KEY\_ROTATION = 180.

\- [NATIVEBUFFER\_ROTATE\_270](../../../../../graphics/arkgraphics-2d/c-apis/header-files/buffer-common-h/document.md#oh_nativebuffer_transformtype) is equivalent to OH\_MD\_KEY\_ROTATION = 90.

**Since**: 22

 |
| const char \* OH\_MD\_KEY\_RANGE\_FLAG | 

Pointer to the key that describes the video YUV value range flag. The value type is int32\_t. The value **1** means a full range, and **0** means a limited range. The default value is **0**. If this parameter is set to a non-zero value, the value **1** is used.

**Since**: 10

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_MD\_KEY\_COLOR\_PRIMARIES | 

Pointer to the key that describes the video primary colors. The value type is int32\_t. The default value is **COLOR\_PRIMARY\_UNSPECIFIED**. For details, see [OH\_ColorPrimary](#oh_colorprimary). The value complies with Table 2 in H.273.

**Since**: 10

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_MD\_KEY\_TRANSFER\_CHARACTERISTICS | 

Pointer to the key that describes the video transfer characteristics. The value type is int32\_t. The default value is **TRANSFER\_CHARACTERISTIC\_UNSPECIFIED**. For details, see [OH\_TransferCharacteristic](#oh_transfercharacteristic). The value complies with Table 3 in H.273.

**Since**: 10

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_MD\_KEY\_MATRIX\_COEFFICIENTS | 

Pointer to the key that describes the video matrix coefficients. The value type is int32\_t. The default value is **MATRIX\_COEFFICIENT\_UNSPECIFIED**. For details, see [OH\_MatrixCoefficient](#oh_matrixcoefficient). The value must comply with Table 4 in H.273.

**Since**: 10

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_MD\_KEY\_REQUEST\_I\_FRAME | 

Pointer to the key that describes the request for immediate encoding of I-frames. The value type is int32\_t. This key is used in [OH\_VideoEncoder\_SetParameter](../native-avcodec-videoencoder-h/document.md#oh_videoencoder_setparameter) or takes effect immediately with each frame.

**Since**: 10

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_MD\_KEY\_QUALITY | 

Pointer to the key that describes the required encoding quality. The value type is int32\_t. The default value is **50**. In H.264 and H.265 encoding scenarios, the value range can be obtained by calling [OH\_AVCapability\_GetEncoderQualityRange](../native-avcapability-h/document.md#oh_avcapability_getencoderqualityrange). This key applies only to the encoder in constant quality mode.

**Since**: 10

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_MD\_KEY\_CODEC\_CONFIG | 

Pointer to the key that describes the codec-specific data. In the case of video, data carried in **SPS/PPS** is transferred. In the case of audio, data carried in **extraData** is transferred. The value type is uint8\_t\*.

**Since**: 10

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_MD\_KEY\_TITLE | 

Pointer to the key that describes the title of a media file . The value type is char \*.

**Since**: 10

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_MD\_KEY\_ARTIST | 

Pointer to the key that describes the artist in a media file. The value type is char \*.

**Since**: 10

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_MD\_KEY\_ALBUM | 

Pointer to the key that describes the album media file. The value type is char \*.

**Since**: 10

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_MD\_KEY\_ALBUM\_ARTIST | 

Pointer to the key that describes the album artist. The value type is char \*.

**Since**: 10

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_MD\_KEY\_DATE | 

Pointer to the key that describes the date of a media file, for example, 2024. The value type is char \*.

**Since**: 10

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_MD\_KEY\_COMMENT | 

Pointer to the key that describes the comment of a media file. The value type is char \*.

**Since**: 10

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_MD\_KEY\_ENABLE\_MOOV\_FRONT | 

Pointer to the key that specifies whether the moov metadata should be at the front of a media file. The value type is int32\_t. The value **1** indicates that the moov metadata should be at the front of a media file, and **0** indicates that the moov metadata should not be at the front of a media file. The default value is **0**.

**Since**: 20

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_MD\_KEY\_GENRE | 

Pointer to the key that describes the genre in a media file. The value type is char \*.

**Since**: 10

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_MD\_KEY\_COPYRIGHT | 

Pointer to the key that describes the copyright of a media file. The value type is char \*.

**Since**: 10

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_MD\_KEY\_LANGUAGE | 

Pointer to the key that describes the language of a media file. The value type is char \*.

**Since**: 10

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_MD\_KEY\_DESCRIPTION | 

Pointer to the key that describes the description of a media file. The value type is char \*.

**Since**: 10

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_MD\_KEY\_LYRICS | 

Pointer to the key that describes the lyrics in a media file. The value type is char \*.

**Since**: 10

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_MD\_KEY\_TRACK\_COUNT | 

Pointer to the key that describes the number of tracks in a media file. The value type is int32\_t.

**Since**: 10

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_MD\_KEY\_CHANNEL\_LAYOUT | 

Pointer to the key that describes the required encoding channel layout. The value type is int64\_t. This key applies only to encoders. For details, see [OH\_AudioChannelLayout](../native-audio-channel-layout-h/document.md#oh_audiochannellayout).

**Since**: 10

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_MD\_KEY\_BITS\_PER\_CODED\_SAMPLE | 

Pointer to the key that describes the number of bits per sample. The value type is int32\_t.

In versions earlier than API version 20, this parameter must be set to **1** for FLAC encoding. Otherwise, **OH\_AudioCodec\_Configure** returns the error code **AV\_ERR\_INVALID\_VAL**. However, this parameter has no actual effect and does not affect the encoding result.

Starting from API version 20, you do not need to set it anymore.

**Since**: 10

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_MD\_KEY\_AAC\_IS\_ADTS | 

Pointer to the key that describes the AAC format, which can be ADTS or LATM. The value type is int32\_t. The value **0** means the LATM format, and **1** means the ADTS format. This key is supported by AAC decoders.

**Since**: 10

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_MD\_KEY\_SBR | 

Pointer to the key that describes the AAC SBR format. The value type is int32\_t. This key applies to AAC encoders.

**Since**: 10

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_MD\_KEY\_COMPLIANCE\_LEVEL | 

Pointer to the key that describes the FLAC compliance level. The value type is int32\_t. This key is used only for audio encoding.

**Since**: 10

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_MD\_KEY\_IDENTIFICATION\_HEADER | 

Pointer to the key that describes the vorbis identification header. The value type is uint8\_t\*. This key applies only to Vorbis decoders.

**Since**: 10

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_MD\_KEY\_SETUP\_HEADER | 

Pointer to the key that describes the vorbis setup header. The value type is uint8\_t\*. This key applies only to Vorbis decoders.

**Since**: 10

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_MD\_KEY\_SCALING\_MODE | 

Pointer to the key that describes the video scaling mode. The value type is int32\_t. For details, see [OH\_ScalingMode](#oh_scalingmode).

You are advised to set the scaling mode by calling [OH\_NativeWindow\_NativeWindowSetScalingModeV2](../../../../../graphics/arkgraphics-2d/c-apis/header-files/external-window-h/document.md#oh_nativewindow_nativewindowsetscalingmodev2). This key is optional and is used only for video decoding in surface mode.

**Since**: 10

**Deprecated from**: 14

**Substitute**: [OH\_NativeWindow\_NativeWindowSetScalingModeV2](../../../../../graphics/arkgraphics-2d/c-apis/header-files/external-window-h/document.md#oh_nativewindow_nativewindowsetscalingmodev2)

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_MD\_MAX\_INPUT\_BUFFER\_COUNT | 

Pointer to the key that describes the maximum number of input buffers. The value type is int32\_t.

**Since**: 10

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_MD\_MAX\_OUTPUT\_BUFFER\_COUNT | 

Pointer to the key that describes the maximum number of output buffers. The value type is int32\_t.

**Since**: 10

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_MD\_KEY\_AUDIO\_COMPRESSION\_LEVEL | 

Pointer to the key that describes the audio codec compression level. The value type is int32\_t type. This key is used only for audio encoding.

**Since**: 11

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_MD\_KEY\_VIDEO\_IS\_HDR\_VIVID | 

Pointer to the key that specifies whether the video track in a media file is HDR Vivid. The value type is int32\_t. This key is used for both multiplexing and demultiplexing.

The value **1** means the HDR Vivid video track, and **0** means other cases.

**Since**: 11

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_MD\_KEY\_AUDIO\_OBJECT\_NUMBER | 

Pointer to the key that describes the number of audio objects. The value type is int32\_t. This key is used only for Audio Vivid decoding.

**Since**: 11

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_MD\_KEY\_AUDIO\_VIVID\_METADATA | 

Pointer to the key that describes the Audio Vivid metadata. The value type is uint8\_t\*. This key is used only for Audio Vivid decoding.

**Since**: 11

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_FEATURE\_PROPERTY\_KEY\_VIDEO\_ENCODER\_MAX\_LTR\_FRAME\_COUNT | 

Pointer to the key that describes the maximum number of long-term reference (LTR) frames obtained during video encoding. The value type is int32\_t.

You can use the API [OH\_AVCapability\_GetFeatureProperties](../native-avcapability-h/document.md#oh_avcapability_getfeatureproperties) and the enumerated value **VIDEO\_ENCODER\_LONG\_TERM\_REFERENCE** in [OH\_AVCapabilityFeature](../native-avcapability-h/document.md#oh_avcapabilityfeature) to query the maximum number.

**Since**: 12

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_MD\_KEY\_VIDEO\_ENCODER\_ENABLE\_TEMPORAL\_SCALABILITY | 

Pointer to the key that describes the enabled status of temporal scalability. The value type is int32\_t. **1** if enabled, **0** otherwise. The default value is **0**. If this parameter is set to a non-zero value, the value **1** is used.

You can use the API [OH\_AVCapability\_IsFeatureSupported](../native-avcapability-h/document.md#oh_avcapability_isfeaturesupported) and the enumerated value **VIDEO\_ENCODER\_TEMPORAL\_SCALABILITY** in [OH\_AVCapabilityFeature](../native-avcapability-h/document.md#oh_avcapabilityfeature) to check whether the current video encoder supports temporal scalability.

For details, see [Temporally Scalable Video Coding](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/video-encoding-temporal-scalability#available-apis).

This key is optional and used only in the configuration phase of video encoding.

**Since**: 12

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_MD\_KEY\_VIDEO\_ENCODER\_TEMPORAL\_GOP\_SIZE | 

Pointer to the key that describes the size of a temporal image group. The value type is int32\_t. This key is valid only when temporal scalability is enabled.

This key is optional and used only in the configuration phase of video encoding.

**Since**: 12

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_MD\_KEY\_VIDEO\_ENCODER\_TEMPORAL\_GOP\_REFERENCE\_MODE | 

Pointer to the key that describes the reference mode in a temporal image group. The value type is int32\_t. For details, see [OH\_TemporalGopReferenceMode](#oh_temporalgopreferencemode). This key is valid only when temporal scalability is enabled.

This key is optional and used only in the configuration phase of video encoding.

**Since**: 12

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_MD\_KEY\_VIDEO\_ENCODER\_LTR\_FRAME\_COUNT | 

Pointer to the key that describes the number of LTR frames. The value type is int32\_t. The value must be within the supported value range.

Before using this key, you can use the API [OH\_AVCapability\_GetFeatureProperties](../native-avcapability-h/document.md#oh_avcapability_getfeatureproperties) and the enumerated value **VIDEO\_ENCODER\_LONG\_TERM\_REFERENCE** in [OH\_AVCapabilityFeature](../native-avcapability-h/document.md#oh_avcapabilityfeature) to query the number of supported LTR frames.

This key is optional and used only in the configuration phase of video encoding.

**Since**: 12

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_MD\_KEY\_VIDEO\_ENCODER\_PER\_FRAME\_MARK\_LTR | 

Pointer to the key that specifies whether the current frame is marked as an LTR frame. The value type is int32\_t. **1** if marked, **0** otherwise. The default value is **0**. If this parameter is set to a non-zero value, the value **1** is used.

This key takes effect only after the number of LTR frames is configured.

This key is optional and is used only for video encoding input rotation. The configuration takes effect immediately.

For details, see [Temporally Scalable Video Coding](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/video-encoding-temporal-scalability#available-apis).

**Since**: 12

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_MD\_KEY\_VIDEO\_ENCODER\_PER\_FRAME\_USE\_LTR | 

Pointer to the key that describes the POC number of the LTR frame referenced by the current frame. The value type is int32\_t.

This key is optional and is used only for video encoding input rotation. The configuration takes effect immediately.

For details, see [Temporally Scalable Video Coding](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/video-encoding-temporal-scalability#available-apis).

**Since**: 12

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_MD\_KEY\_VIDEO\_PER\_FRAME\_IS\_LTR | 

Pointer to the key that specifies whether the frame corresponding to the stream output from the current OH\_AVBuffer is marked as an LTR frame. The value type is int32\_t. **1** if marked, **0** otherwise. The default value is **0**. If this parameter is set to a non-zero value, the value **1** is used.

This key is optional and is used only for video encoding output rotation.

It indicates the attribute of a frame.

**Since**: 12

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_MD\_KEY\_VIDEO\_PER\_FRAME\_POC | 

Pointer to the key that describes the POC of the frame. The value type is int32\_t.

This key is optional and is used only for video encoding output rotation.

It indicates the attribute of a frame.

**Since**: 12

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_MD\_KEY\_VIDEO\_CROP\_TOP | 

Pointer to the key that describes the top coordinate (y) of the cropped rectangle. The value type is int32\_t.

The row at the top of the cropped rectangle is contained, and the row index starts from 0.

This key is used only for video decoding.

**Since**: 12

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_MD\_KEY\_VIDEO\_CROP\_BOTTOM | 

Pointer to the key that describes the bottom coordinate (y) of the cropped rectangle. The value type is int32\_t.

The row at the bottom of the cropped rectangle is contained, and the row index starts from 0.

This key is used only for video decoding.

**Since**: 12

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_MD\_KEY\_VIDEO\_CROP\_LEFT | 

Pointer to the key that describes the left coordinate (x) of the cropped rectangle. The value type is int32\_t.

The leftmost column of the cropped rectangle is contained, and the column index starts from 0.

This key is used only for video decoding.

**Since**: 12

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_MD\_KEY\_VIDEO\_CROP\_RIGHT | 

Pointer to the key that describes the right coordinate (x) of the cropped rectangle. The value type is int32\_t.

The rightmost column of the cropped rectangle is contained, and the column index starts from 0.

This key is used only for video decoding.

**Since**: 12

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_MD\_KEY\_VIDEO\_STRIDE | 

Pointer to the key that describes the stride of the video frame. The value type is int32\_t.

The stride is the difference between the index of the pixel and the index of the pixel right below.

For the YUV420 format, the stride corresponds to the Y plane. The stride of the U/V plane can be calculated based on the color format, but it is usually not defined and depends on the device and version.

For details, see step 3 in buffer mode in [Video Encoding](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/video-encoding#buffer-mode).

For details about the image arrangement and usage examples of **width**, **height**, **wStride**, and **hStride**, see step 8 in buffer mode in [Video Encoding](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/video-encoding#buffer-mode) or step 11 in buffer mode in [Video Decoding](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/video-decoding#buffer-mode).

**Since**: 12

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_MD\_KEY\_VIDEO\_SLICE\_HEIGHT | 

Pointer to the key that describes the height of the video frame. The value type is int32\_t.

The height is the number of rows that must be offset from the top of the Y plane to the top of the U plane. Essentially, the offset of the U plane is sliceHeight \* stride.

The height of the U/V plane can be calculated based on the color format, but it is usually not defined and depends on the device and version.

For details, see step 3 in buffer mode in [Video Encoding](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/video-encoding#buffer-mode).

For details about the image arrangement and usage examples of **width**, **height**, **wStride**, and **hStride**, see step 8 in buffer mode in [Video Encoding](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/video-encoding#buffer-mode) or step 11 in buffer mode in [Video Decoding](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/video-decoding#buffer-mode).

**Since**: 12

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_MD\_KEY\_VIDEO\_PIC\_WIDTH | 

Pointer to the key that describes the width of the video frame. The value type is int32\_t.

When [OH\_VideoDecoder\_GetOutputDescription](../native-avcodec-videodecoder-h/document.md#oh_videodecoder_getoutputdescription) is called during video decoding, the width can be parsed from the returned OH\_AVFormat instance.

When the decoded output stream changes, the width can be parsed from the OH\_AVFormat instance returned by [OH\_AVCodecOnStreamChanged](#oh_avcodeconstreamchanged).

The width and height parsed from the OH\_AVFormat instance are aligned, which are different from **OH\_MD\_KEY\_WIDTH** and **OH\_MD\_KEY\_HEIGHT** set by calling **Configure**.

For details about the image arrangement and usage examples of **width**, **height**, **wStride**, and **hStride**, see step 8 in buffer mode in [Video Encoding](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/video-encoding#buffer-mode) or step 11 in buffer mode in [Video Decoding](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/video-decoding#buffer-mode).

**Since**: 12

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_MD\_KEY\_VIDEO\_PIC\_HEIGHT | 

Pointer to the key that describes the height of the video frame. The value type is int32\_t.

When [OH\_VideoDecoder\_GetOutputDescription](../native-avcodec-videodecoder-h/document.md#oh_videodecoder_getoutputdescription) is called during video decoding, the height can be parsed from the returned OH\_AVFormat instance.

When the decoded output stream changes, the height can be parsed from the OH\_AVFormat instance returned by [OH\_AVCodecOnStreamChanged](#oh_avcodeconstreamchanged).

The width and height parsed from the OH\_AVFormat instance are aligned, which are different from **OH\_MD\_KEY\_WIDTH** and **OH\_MD\_KEY\_HEIGHT** set by calling **Configure**.

For details about the image arrangement and usage examples of **width**, **height**, **wStride**, and **hStride**, see step 8 in buffer mode in [Video Encoding](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/video-encoding#buffer-mode) or step 11 in buffer mode in [Video Decoding](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/video-decoding#buffer-mode).

**Since**: 12

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_MD\_KEY\_VIDEO\_ENABLE\_LOW\_LATENCY | 

Pointer to the key that describes the enabled status of low-latency video decoding. The value type is int32\_t. **1** if enabled, **0** otherwise. The default value is **0**. If this parameter is set to a non-zero value, the value **1** is used.

This key is optional and used only in the configuration phase.

If enabled, the input and output data held by the video decoder does not exceed the amount required by the decoder standard.

You can call [OH\_AVCapability\_IsFeatureSupported](../native-avcapability-h/document.md#oh_avcapability_isfeaturesupported) to check whether a specific decoder supports low-latency decoding. If supported, the video decoder outputs frames in the decoding sequence when low-latency video codec is enabled.

**Since**: 12

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_MD\_KEY\_VIDEO\_ENCODER\_QP\_MAX | 

Pointer to the key that describes the maximum Quantization Parameter (QP) allowed by the video encoder. The value type is int32\_t.

This key is used in the configuration or parameter setting phase or takes effect immediately with each frame.

**Since**: 12

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_MD\_KEY\_VIDEO\_ENCODER\_QP\_MIN | 

Pointer to the key that describes the minimum QP allowed by the video encoder. The value type is int32\_t.

This key is used in the configuration or parameter setting phase or takes effect immediately with each frame.

**Since**: 12

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_MD\_KEY\_VIDEO\_ENCODER\_QP\_AVERAGE | 

Pointer to the key that describes the average QP of video frames. The value type is int32\_t.

Pointer to the key that describes the average QP value of the current frame encoding block. It is output with [OH\_AVBuffer](../../structs/oh-avbuffer/document.md).

**Since**: 12

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_MD\_KEY\_VIDEO\_ENCODER\_MSE | 

Pointer to the key that describes the Mean Squared Error (MSE) of video frames. The value type is double.

Pointer to the key that describes the average MSE value of the current frame encoding block. It is output with [OH\_AVBuffer](../../structs/oh-avbuffer/document.md).

**Since**: 12

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_MD\_KEY\_DECODING\_TIMESTAMP | 

Pointer to the key that describes the decoding timestamp corresponding to the audio, video, or subtitle sample carried in AVBuffer, in microseconds. The value type is int64\_t.

**Since**: 12

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_MD\_KEY\_BUFFER\_DURATION | 

Pointer to the key that describes the duration corresponding to the audio, video, or subtitle sample carried in AVBuffer, in microseconds. The value type is int64\_t.

**Since**: 12

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_MD\_KEY\_VIDEO\_SAR | 

Pointer to the key that describes the aspect ratio of the sample. The value type is double.

**Since**: 12

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_MD\_KEY\_START\_TIME | 

Pointer to the key that describes the start time of the first frame in a media file, measured in microseconds. The value type is int64\_t.

**Since**: 12

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_MD\_KEY\_TRACK\_START\_TIME | 

Pointer to the key that describes the start time of the track, measured in microseconds. The value type is int64\_t.

**Since**: 12

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_MD\_KEY\_VIDEO\_DECODER\_OUTPUT\_COLOR\_SPACE | 

Pointer to the key that describes the output color space of the video decoder. The value type is int32\_t.

The supported value is **OH\_COLORSPACE\_BT709\_LIMIT**. For details, see [OH\_NativeBuffer\_ColorSpace](../../../../../graphics/arkgraphics-2d/c-apis/header-files/buffer-common-h/document.md#oh_nativebuffer_colorspace).

It is used in [OH\_VideoDecoder\_Configure](../native-avcodec-videodecoder-h/document.md#oh_videodecoder_configure).

Before calling **OH\_VideoDecoder\_Start**, you must call **OH\_VideoDecoder\_Prepare**.

If Color Space Conversion (CSC) is supported and this key is configured, the video decoder automatically transcodes the HDR Vivid video to the specified color space.

If CSC is not supported, the error code **AV\_ERR\_VIDEO\_UNSUPPORTED\_COLOR\_SPACE\_CONVERSION** in [OH\_AVErrCode](../native-averrors-h/document.md#oh_averrcode) is returned when [OH\_VideoDecoder\_Configure](../native-avcodec-videodecoder-h/document.md#oh_videodecoder_configure) is called. If the input video is not an HDR Vivid video, the callback function [OH\_AVCodecOnError](#oh_avcodeconerror) is invoked to report the error code **AV\_ERR\_VIDEO\_UNSUPPORTED\_COLOR\_SPACE\_CONVERSION** in [OH\_AVErrCode](../native-averrors-h/document.md#oh_averrcode).

**Since**: 12

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_MD\_KEY\_VIDEO\_DECODER\_OUTPUT\_ENABLE\_VRR | 

Pointer to the key that specifies whether the decoder enables the video variable frame rate feature. The value type is int32\_t.

**1** if enabled, **0** otherwise.

**Since**: 15

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_MD\_KEY\_CREATION\_TIME | 

Pointer to the key that describes the media file creation time. The value type is char \*. The value must be in the UTC time format complying with ISO 8601. Time format example: 2024-12-28T00:00:00:000000Z

**Since**: 14

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_MD\_KEY\_VIDEO\_ENCODER\_REPEAT\_PREVIOUS\_FRAME\_AFTER | 

Pointer to the key that describes the duration (in milliseconds) for which the last frame will be resubmitted repeatedly, if no new frame is available after the previous frame is submitted to the encoder. The value type is int32\_t.

This key is used only in the configuration phase of video encoding in surface mode.

Configured value.

\- If the value is less than or equal to 0, the request is intercepted in the configuration phase and **ERROR AV\_ERR\_INVALID\_VAL** is returned.

\- If the value is greater than 0, the last frame will be resubmitted repeatedly in the specified duration, measured in milliseconds.

**Since**: 18

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_MD\_KEY\_VIDEO\_ENCODER\_REPEAT\_PREVIOUS\_MAX\_COUNT | 

Pointer to the key that describes the maximum number of times the encoder can repeat encoding the previous frame when no new frame is available. The value type is int32\_t.

This key takes effect only when **OH\_MD\_KEY\_VIDEO\_ENCODER\_REPEAT\_PREVIOUS\_FRAME\_AFTER** is available and is used only in the configuration phase.

Configured value.

\- If the value is equal to 0, the request is intercepted in the configuration phase and **ERROR AV\_ERR\_INVALID\_VAL** is returned.

\- If the value is less than 0 and no new frame is available, the encoder repeatedly encodes the previous frame until the upper limit of the system is reached.

\- If the value is greater than 0 and no new frame is available, the encoder repeatedly encodes the previous frame until the maximum number specified is reached.

**Since**: 18

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_MD\_KEY\_VIDEO\_ENCODER\_ENABLE\_B\_FRAME | 

Pointer to the key that describes the enabled status of B-frame encoding. The value type is int32\_t (**0** or **1**). **1** if enabled, **0** otherwise. This key is optional and used only for video encoding. The default value is **0**.

If enabled, the video encoder uses B-frames, resulting in a different decoding order from the display order.

If the platform does not support this feature, the configuration of this key does not take effect.

To check whether the platform supports B-frame encoding, use the [OH\_AVCapability\_IsFeatureSupported](../native-avcapability-h/document.md#oh_avcapability_isfeaturesupported) API and the enumerated value [OH\_AVCapabilityFeature](../native-avcapability-h/document.md#oh_avcapabilityfeature).VIDEO\_ENCODER\_B\_FRAME.

This key is used only in the configuration phase.

**Since**: 20

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_MD\_KEY\_VIDEO\_ENCODER\_MAX\_B\_FRAMES | 

Pointer to the key that describes the maximum number of consecutive B-frames supported by the video encoder. The value type is int32\_t. Note: This key is used only to query the encoder capability.

The usage specifications are as follows:

1\. To check whether the platform supports B-frame encoding, use the [OH\_AVCapability\_IsFeatureSupported](../native-avcapability-h/document.md#oh_avcapability_isfeaturesupported) API and the enumerated value [OH\_AVCapabilityFeature](../native-avcapability-h/document.md#oh_avcapabilityfeature).VIDEO\_ENCODER\_B\_FRAME.

2\. Obtain the OH\_AVFormat pointer through the [OH\_AVCapability\_GetFeatureProperties](../native-avcapability-h/document.md#oh_avcapability_getfeatureproperties) API and the enumerated value [OH\_AVCapabilityFeature](../native-avcapability-h/document.md#oh_avcapabilityfeature).VIDEO\_ENCODER\_B\_FRAME.

3\. Obtain the maximum number of B-frames through the [OH\_AVFormat\_GetIntValue](../native-avformat-h/document.md#oh_avformat_getintvalue) API and this key.

**Since**: 20

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_MD\_KEY\_VIDEO\_ENCODER\_ROI\_PARAMS | 

Pointer to the key that describes the enabled status of ROI encoding in video encoding, with ROI parameters delivered. The parameters take effect immediately with the frame.

The value must be in the format of "Top1,Left1-Bottom1,Right1=Offset1;Top2,Left2-Bottom2,Right2=Offset2;", where multiple ROI parameters are separated by semicolons (;).

**Top**, **Left**, **Bottom**, and **Right** specify the upper, left, bottom, and right boundaries of an ROI area, respectively. **Offset** specifies deltaQP. **(=Offset)** can be omitted. If it is omitted, the default value (**–3**) is used.

**Since**: 20

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_MD\_KEY\_SQR\_FACTOR | 

Pointer to the key that describes the quality parameter in SQR mode. The value range is \[0, 51\] (same as the QP value in encoding). A smaller value indicates a higher output bit rate and better quality.

It is used in the configuration or parameter setting phase.

**Since**: 20

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_MD\_KEY\_MAX\_BITRATE | 

Pointer to the key that describes the maximum bit rate in SQR mode. The value range can be obtained by calling [OH\_AVCapability\_GetEncoderBitrateRange](../native-avcapability-h/document.md#oh_avcapability_getencoderbitraterange) and is the same as that of **OH\_MD\_KEY\_BITRATE**. The unit is bit/s. The value type is int64\_t.

It is used in the configuration or parameter setting phase.

**Since**: 20

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_MD\_KEY\_VIDEO\_ENCODER\_ENABLE\_PTS\_BASED\_RATECONTROL | 

Pointer to the key that describes the enabled status of the PTS-based bit rate control mode. The value type is int32\_t. **1** if enabled, **0** otherwise. The default value is **0**. If this parameter is set to a non-zero value, the value **1** is used.

This key is optional and is used only for video encoding.

If this feature is enabled, each video frame must contain PTS information and be sent to the encoder. In surface mode, the PTS is set by calling [OH\_NativeWindow\_NativeWindowHandleOpt](../../../../../graphics/arkgraphics-2d/c-apis/header-files/external-window-h/document.md#oh_nativewindow_nativewindowhandleopt), in units of nanosecond (ns). In buffer mode, the PTS is set by calling [OH\_AVBuffer\_SetBufferAttr](../native-avbuffer-h/document.md#oh_avbuffer_setbufferattr), in units of microsecond (us).

It is used in the configuration phase.

**Since**: 20

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_MD\_KEY\_REFERENCE\_TRACK\_IDS | 

Pointer to the key that describes the reference relationship between media file tracks. The value type is int32\_t\*.

**Since**: 20

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_MD\_KEY\_TRACK\_REFERENCE\_TYPE | 

Pointer to the auxiliary track type of a media file. The value type is char \*.

**Since**: 20

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_MD\_KEY\_TRACK\_DESCRIPTION | 

Pointer to the auxiliary track description of a media file. The value type is char \*.

**Since**: 20

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_MD\_KEY\_ENABLE\_SYNC\_MODE | 

Pointer to the key that describes the enabled status of audio/video codec synchronization. The value type is int32\_t. **1** if enabled, **0** otherwise. The default value is **0**. If this parameter is set to a non-zero value, the value **1** is used. This key is optional.

If this feature is enabled, pay attention to the following:

1\. The codec cannot have a callback function.

2\. You must use the buffer query API instead of the callback function.

3\. The key can be used only in the configuration phase.

**Since**: 20

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_MD\_KEY\_VIDEO\_DECODER\_BLANK\_FRAME\_ON\_SHUTDOWN | 

Pointer to the key that specifies whether to output blank frames when the video decoder is disabled. The value type is int32\_t. **1** to output, **0** otherwise. The default value is **0**. If this parameter is set to a non-zero value, the value **1** is used. This key is optional and is used only for video decoding in surface mode.

After this function is enabled, the video decoder outputs a blank frame (usually black) when the [OH\_VideoDecoder\_Stop](../native-avcodec-videodecoder-h/document.md#oh_videodecoder_stop) or [OH\_VideoDecoder\_Destroy](../native-avcodec-videodecoder-h/document.md#oh_videodecoder_destroy) API is called. This mechanism prevents frozen frames caused by sudden termination of the decoder.

**Since**: 20

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |
| const char \* OH\_MD\_KEY\_VIDEO\_NATIVE\_BUFFER\_FORMAT | 

Pointer to the key that is used to query the native buffer pixel format in video encoding and decoding. The value type is int32\_t.

For details, see the pixel formats defined in [OH\_NativeBuffer\_Format](../../../../../graphics/arkgraphics-2d/c-apis/header-files/buffer-common-h/document.md#oh_nativebuffer_format). This key is used in the following scenarios:

1\. Video decoding: Call [OH\_VideoDecoder\_GetOutputDescription](../native-avcodec-videodecoder-h/document.md#oh_videodecoder_getoutputdescription) or [OH\_AVCodecOnStreamChanged](#oh_avcodeconstreamchanged) to obtain the current output format from the returned OH\_AVFormat object.

2\. Video encoding: Call [OH\_VideoEncoder\_GetInputDescription](../native-avcodec-videoencoder-h/document.md#oh_videoencoder_getinputdescription) to obtain the current input format from the returned OH\_AVFormat object.

**Since**: 22

**System capability**: SystemCapability.Multimedia.Media.CodecBase

 |

#### Enum Description

#### \[h2\]OH\_MediaType

enum OH\_MediaType

**Description**

Enumerates the media types.

**System capability**: SystemCapability.Multimedia.Media.CodecBase

**Since**: 9

| Value | Description |
| :-- | :-- |
| MEDIA\_TYPE\_AUD = 0 | Audio track. |
| MEDIA\_TYPE\_VID = 1 | Video track. |
| MEDIA\_TYPE\_SUBTITLE = 2 | 
Subtitle track.

**Since**: 12

 |
| MEDIA\_TYPE\_TIMED\_METADATA = 5 | 

Timed metadata track.

**Since**: 20

 |
| MEDIA\_TYPE\_AUXILIARY = 6 | 

Auxiliary track.

**Since**: 20

 |

#### \[h2\]OH\_AACProfile

enum OH\_AACProfile

**Description**

Enumerates the AAC profiles.

**System capability**: SystemCapability.Multimedia.Media.CodecBase

**Since**: 9

| Value | Description |
| :-- | :-- |
| AAC\_PROFILE\_LC = 0 | AAC profile of the low complexity level. |
| AAC\_PROFILE\_HE = 3 | 
AAC profile of the high efficiency level.

**Since**: 14

 |
| AAC\_PROFILE\_HE\_V2 = 4 | 

AAC profile of the high efficiency V2 level.

**Since**: 14

 |

#### \[h2\]OH\_AVCProfile

enum OH\_AVCProfile

**Description**

Enumerates the AVC profiles.

**System capability**: SystemCapability.Multimedia.Media.CodecBase

**Since**: 9

| Value | Description |
| :-- | :-- |
| AVC\_PROFILE\_BASELINE = 0 | AVC baseline profile. |
| AVC\_PROFILE\_HIGH = 4 | AVC high profile. |
| AVC\_PROFILE\_MAIN = 8 | AVC main profile. |

#### \[h2\]OH\_HEVCProfile

enum OH\_HEVCProfile

**Description**

Enumerates the HEVC profiles.

**System capability**: SystemCapability.Multimedia.Media.CodecBase

**Since**: 10

| Value | Description |
| :-- | :-- |
| HEVC\_PROFILE\_MAIN = 0 | HEVC profile of the main level. |
| HEVC\_PROFILE\_MAIN\_10 = 1 | HEVC profile of the 10-bit main level. |
| HEVC\_PROFILE\_MAIN\_STILL = 2 | HEVC profile of the main still picture level. |
| HEVC\_PROFILE\_MAIN\_10\_HDR10 = 3 | 
HEVC profile of the main 10 HDR10 level.

**Deprecated from**: 14

 |
| HEVC\_PROFILE\_MAIN\_10\_HDR10\_PLUS = 4 | 

HEVC profile of the main 10 HDR10+ level.

**Deprecated from**: 14

 |

#### \[h2\]OH\_VVCProfile

enum OH\_VVCProfile

**Description**

Enumerates the VVC profiles.

**System capability**: SystemCapability.Multimedia.Media.CodecBase

**Since**: 15

| Value | Description |
| :-- | :-- |
| VVC\_PROFILE\_MAIN\_10 = 1 | VVC profile of the 10-bit main level. |
| VVC\_PROFILE\_MAIN\_12 = 2 | VVC profile of the 12-bit main level. |
| VVC\_PROFILE\_MAIN\_12\_INTRA = 10 | VVC profile of the 12-bit intra main level. |
| VVC\_PROFILE\_MULTI\_MAIN\_10 = 17 | VVC profile of the 10-bit main level for multi-layer encoding. |
| VVC\_PROFILE\_MAIN\_10\_444 = 33 | VVC profile of the 10-bit full-sample main level. |
| VVC\_PROFILE\_MAIN\_12\_444 = 34 | VVC profile of the 12-bit full-sample main level. |
| VVC\_PROFILE\_MAIN\_16\_444 = 36 | VVC profile of the 16-bit full-sample main level. |
| VVC\_PROFILE\_MAIN\_12\_444\_INTRA = 42 | VVC profile of the 12-bit full-sample intra main level. |
| VVC\_PROFILE\_MAIN\_16\_444\_INTRA = 44 | VVC profile of the 16-bit full-sample intra main level. |
| VVC\_PROFILE\_MULTI\_MAIN\_10\_444 = 49 | VVC profile of the 10-bit full-sample main level for multi-layer encoding. |
| VVC\_PROFILE\_MAIN\_10\_STILL = 65 | VVC profile of the 10-bit still picture main level. |
| VVC\_PROFILE\_MAIN\_12\_STILL = 66 | VVC profile of the 12-bit still picture main level. |
| VVC\_PROFILE\_MAIN\_10\_444\_STILL = 97 | VVC profile of the 10-bit full-sample still picture main level. |
| VVC\_PROFILE\_MAIN\_12\_444\_STILL = 98 | VVC profile of the 12-bit full-sample still picture main level. |
| VVC\_PROFILE\_MAIN\_16\_444\_STILL = 100 | VVC profile of the 16-bit full-sample still picture main level. |

#### \[h2\]OH\_MPEG2Profile

enum OH\_MPEG2Profile

**Description**

Enumerates the MPEG2 profiles.

**System capability**: SystemCapability.Multimedia.Media.CodecBase

**Since**: 17

| Value | Description |
| :-- | :-- |
| MPEG2\_PROFILE\_SIMPLE = 0 | Simple profile. |
| MPEG2\_PROFILE\_MAIN = 1 | Main profile. |
| MPEG2\_PROFILE\_SNR\_SCALABLE = 2 | Signal-to-Noise Ratio (SNR) scalable profile. |
| MPEG2\_PROFILE\_SPATIALLY\_SCALABLE = 3 | Spatial scalable profile. |
| MPEG2\_PROFILE\_HIGH = 4 | High profile. |
| MPEG2\_PROFILE\_422 = 5 | 4:2:2 profile. |

#### \[h2\]OH\_MPEG4Profile

enum OH\_MPEG4Profile

**Description**

Enumerates the MPEG4 profiles.

**System capability**: SystemCapability.Multimedia.Media.CodecBase

**Since**: 17

| Value | Description |
| :-- | :-- |
| MPEG4\_PROFILE\_SIMPLE = 0 | Simple profile. |
| MPEG4\_PROFILE\_SIMPLE\_SCALABLE = 1 | Simple scalable profile. |
| MPEG4\_PROFILE\_CORE = 2 | Core profile. |
| MPEG4\_PROFILE\_MAIN = 3 | Main profile. |
| MPEG4\_PROFILE\_N\_BIT = 4 | N-bit profile. |
| MPEG4\_PROFILE\_HYBRID = 5 | Hybrid profile. |
| MPEG4\_PROFILE\_BASIC\_ANIMATED\_TEXTURE = 6 | Basic animated texture profile. |
| MPEG4\_PROFILE\_SCALABLE\_TEXTURE = 7 | Scalable texture profile. |
| MPEG4\_PROFILE\_SIMPLE\_FA = 8 | Simple FA profile. |
| MPEG4\_PROFILE\_ADVANCED\_REAL\_TIME\_SIMPLE = 9 | Advanced real-time simple profile. |
| MPEG4\_PROFILE\_CORE\_SCALABLE = 10 | Core scalable profile. |
| MPEG4\_PROFILE\_ADVANCED\_CODING\_EFFICIENCY = 11 | Advanced coding efficiency profile. |
| MPEG4\_PROFILE\_ADVANCED\_CORE = 12 | Advanced core profile. |
| MPEG4\_PROFILE\_ADVANCED\_SCALABLE\_TEXTURE = 13 | Advanced scalable texture profile. |
| MPEG4\_PROFILE\_ADVANCED\_SIMPLE = 17 | Advanced simple profile. |

#### \[h2\]OH\_H263Profile

enum OH\_H263Profile

**Description**

Enumerates the H.263 profiles.

**System capability**: SystemCapability.Multimedia.Media.CodecBase

**Since**: 17

| Value | Description |
| :-- | :-- |
| H263\_PROFILE\_BASELINE = 0 | Baseline profile. |
| H263\_PROFILE\_VERSION\_1\_BACKWARD\_COMPATIBILITY = 2 | Version 1 backward compatibility. |

#### \[h2\]OH\_VC1Profile

enum OH\_VC1Profile

**Description**

Enumerates the VC-1 profiles.

**System capability**: SystemCapability.Multimedia.Media.CodecBase

**Since**: 22

| Value | Description |
| :-- | :-- |
| VC1\_PROFILE\_SIMPLE = 0 | Simple profile. |
| VC1\_PROFILE\_MAIN = 1 | Main profile. |
| VC1\_PROFILE\_ADVANCED = 2 | High profile. |

#### \[h2\]OH\_WMV3Profile

enum OH\_WMV3Profile

**Description**

Enumerates the WMV3 profiles.

**System capability**: SystemCapability.Multimedia.Media.CodecBase

**Since**: 22

| Value | Description |
| :-- | :-- |
| WMV3\_PROFILE\_SIMPLE = 0 | Simple profile. |
| WMV3\_PROFILE\_MAIN = 1 | Main profile. |

#### \[h2\]OH\_AVOutputFormat

enum OH\_AVOutputFormat

**Description**

Enumerates the output file formats supported by a muxer.

**System capability**: SystemCapability.Multimedia.Media.CodecBase

**Since**: 10

| Value | Description |
| :-- | :-- |
| AV\_OUTPUT\_FORMAT\_DEFAULT = 0 | Default format, which is MP4. |
| AV\_OUTPUT\_FORMAT\_MPEG\_4 = 2 | MP4. |
| AV\_OUTPUT\_FORMAT\_M4A = 6 | M4A. |
| AV\_OUTPUT\_FORMAT\_AMR = 8 | 
AMR.

**Since**: 12

 |
| AV\_OUTPUT\_FORMAT\_MP3 = 9 | 

MP3.

**Since**: 12

 |
| AV\_OUTPUT\_FORMAT\_WAV = 10 | 

WAV.

**Since**: 12

 |
| AV\_OUTPUT\_FORMAT\_AAC = 11 | 

AAC.

**Since**: 18

 |
| AV\_OUTPUT\_FORMAT\_FLAC = 12 | 

FLAC.

**Since**: 20

 |

#### \[h2\]OH\_AVSeekMode

enum OH\_AVSeekMode

**Description**

Enumerates the seek modes.

**System capability**: SystemCapability.Multimedia.Media.CodecBase

**Since**: 10

| Value | Description |
| :-- | :-- |
| SEEK\_MODE\_NEXT\_SYNC = 0 | Seeks to the next I-frame at the specified position. If there is no I-frame after the specified position, the seek operation may fail. |
| SEEK\_MODE\_PREVIOUS\_SYNC | Seeks to the previous I-frame at the specified position. |
| SEEK\_MODE\_CLOSEST\_SYNC | Seeks to the latest I-frame at the specified position. |

#### \[h2\]OH\_ScalingMode

enum OH\_ScalingMode

**Description**

Enumerates the scaling modes. This enum is used only in surface mode.

**System capability**: SystemCapability.Multimedia.Media.CodecBase

**Since**: 10

**Deprecated from**: 14

**Substitute**: [OHScalingModeV2](../../../../../graphics/arkgraphics-2d/c-apis/header-files/external-window-h/document.md#ohscalingmodev2)

| Value | Description |
| :-- | :-- |
| SCALING\_MODE\_SCALE\_TO\_WINDOW = 1 | 
Scales the image based on the window size.

**Substitute**: [OHScalingModeV2](../../../../../graphics/arkgraphics-2d/c-apis/header-files/external-window-h/document.md#ohscalingmodev2).OH\_SCALING\_MODE\_SCALE\_TO\_WINDOW\_V2

 |
| SCALING\_MODE\_SCALE\_CROP = 2 | 

Crops the image based on the window size.

**Substitute**: [OHScalingModeV2](../../../../../graphics/arkgraphics-2d/c-apis/header-files/external-window-h/document.md#ohscalingmodev2).OH\_SCALING\_MODE\_SCALE\_CROP\_V2

 |

#### \[h2\]OH\_BitsPerSample

enum OH\_BitsPerSample

**Description**

Enumerates the number of audio bits for each coded sample.

**System capability**: SystemCapability.Multimedia.Media.CodecBase

**Since**: 10

| Value | Description |
| :-- | :-- |
| SAMPLE\_U8 = 0 | 8-bit unsigned integer sampling. |
| SAMPLE\_S16LE = 1 | 16-bit signed integer sampling. |
| SAMPLE\_S24LE = 2 | 24-bit signed integer sampling. |
| SAMPLE\_S32LE = 3 | 32-bit signed integer sampling. |
| SAMPLE\_F32LE = 4 | 32-bit floating-point sampling. |
| SAMPLE\_U8P = 5 | 8-bit unsigned integer plane sampling. |
| SAMPLE\_S16P = 6 | 16-bit signed integer plane sampling. |
| SAMPLE\_S24P = 7 | 24-bit signed integer plane sampling. |
| SAMPLE\_S32P = 8 | 32-bit signed integer plane sampling. |
| SAMPLE\_F32P = 9 | 32-bit floating-point plane sampling. |
| INVALID\_WIDTH = -1 | Invalid sampling format. |

#### \[h2\]OH\_ColorPrimary

enum OH\_ColorPrimary

**Description**

Enumerates the primary colors. This enum is used for both encoding and decoding.

**System capability**: SystemCapability.Multimedia.Media.CodecBase

**Since**: 10

| Value | Description |
| :-- | :-- |
| COLOR\_PRIMARY\_BT709 = 1 | BT709 color gamut. |
| COLOR\_PRIMARY\_UNSPECIFIED = 2 | Unspecified color gamut. |
| COLOR\_PRIMARY\_BT470\_M = 4 | BT470\_M color gamut. |
| COLOR\_PRIMARY\_BT601\_625 = 5 | BT601\_625 color gamut. |
| COLOR\_PRIMARY\_BT601\_525 = 6 | BT601\_525 color gamut. |
| COLOR\_PRIMARY\_SMPTE\_ST240 = 7 | SMPTE\_ST240 color gamut. |
| COLOR\_PRIMARY\_GENERIC\_FILM = 8 | GENERIC\_FILM color gamut. |
| COLOR\_PRIMARY\_BT2020 = 9 | BT2020 color gamut. |
| COLOR\_PRIMARY\_SMPTE\_ST428 = 10 | SMPTE\_ST428 color gamut. |
| COLOR\_PRIMARY\_P3DCI = 11 | P3DCI color gamut. |
| COLOR\_PRIMARY\_P3D65 = 12 | P3D65 color gamut. |

#### \[h2\]OH\_TransferCharacteristic

enum OH\_TransferCharacteristic

**Description**

Enumerates the transfer characteristics. This enum is used for both encoding and decoding.

**System capability**: SystemCapability.Multimedia.Media.CodecBase

**Since**: 10

| Value | Description |
| :-- | :-- |
| TRANSFER\_CHARACTERISTIC\_BT709 = 1 | BT709 transfer function. |
| TRANSFER\_CHARACTERISTIC\_UNSPECIFIED = 2 | Unspecified transfer function. |
| TRANSFER\_CHARACTERISTIC\_GAMMA\_2\_2 = 4 | GAMMA\_2\_2 transfer function. |
| TRANSFER\_CHARACTERISTIC\_GAMMA\_2\_8 = 5 | GAMMA\_2\_8 transfer function. |
| TRANSFER\_CHARACTERISTIC\_BT601 = 6 | BT601 transfer function. |
| TRANSFER\_CHARACTERISTIC\_SMPTE\_ST240 = 7 | SMPTE\_ST240 transfer function. |
| TRANSFER\_CHARACTERISTIC\_LINEAR = 8 | Linear transfer function. |
| TRANSFER\_CHARACTERISTIC\_LOG = 9 | Log transfer function. |
| TRANSFER\_CHARACTERISTIC\_LOG\_SQRT = 10 | LOG\_SQRT transfer function. |
| TRANSFER\_CHARACTERISTIC\_IEC\_61966\_2\_4 = 11 | IEC\_61966\_2\_4 transfer function. |
| TRANSFER\_CHARACTERISTIC\_BT1361 = 12 | BT1361 transfer function. |
| TRANSFER\_CHARACTERISTIC\_IEC\_61966\_2\_1 = 13 | IEC\_61966\_2\_1 transfer function. |
| TRANSFER\_CHARACTERISTIC\_BT2020\_10BIT = 14 | BT2020\_10BIT transfer function. |
| TRANSFER\_CHARACTERISTIC\_BT2020\_12BIT = 15 | BT2020\_12BIT transfer function. |
| TRANSFER\_CHARACTERISTIC\_PQ = 16 | PQ transfer function. |
| TRANSFER\_CHARACTERISTIC\_SMPTE\_ST428 = 17 | SMPTE\_ST428 transfer function. |
| TRANSFER\_CHARACTERISTIC\_HLG = 18 | HLG transfer function. |

#### \[h2\]OH\_MatrixCoefficient

enum OH\_MatrixCoefficient

**Description**

Enumerates the matrix coefficients. This enum is used for both encoding and decoding.

**System capability**: SystemCapability.Multimedia.Media.CodecBase

**Since**: 10

| Value | Description |
| :-- | :-- |
| MATRIX\_COEFFICIENT\_IDENTITY = 0 | Identity matrix. |
| MATRIX\_COEFFICIENT\_BT709 = 1 | BT709 conversion matrix. |
| MATRIX\_COEFFICIENT\_UNSPECIFIED = 2 | Unspecified conversion matrix. |
| MATRIX\_COEFFICIENT\_FCC = 4 | FCC conversion matrix. |
| MATRIX\_COEFFICIENT\_BT601\_625 = 5 | BT601\_625 conversion matrix. |
| MATRIX\_COEFFICIENT\_BT601\_525 = 6 | BT601\_525 conversion matrix. |
| MATRIX\_COEFFICIENT\_SMPTE\_ST240 = 7 | SMPTE\_ST240 conversion matrix. |
| MATRIX\_COEFFICIENT\_YCGCO = 8 | YCGCO conversion matrix. |
| MATRIX\_COEFFICIENT\_BT2020\_NCL = 9 | BT2020\_NCL conversion matrix. |
| MATRIX\_COEFFICIENT\_BT2020\_CL = 10 | BT2020\_CL conversion matrix. |
| MATRIX\_COEFFICIENT\_SMPTE\_ST2085 = 11 | SMPTE\_ST2085 conversion matrix. |
| MATRIX\_COEFFICIENT\_CHROMATICITY\_NCL = 12 | CHROMATICITY\_NCL conversion matrix. |
| MATRIX\_COEFFICIENT\_CHROMATICITY\_CL = 13 | CHROMATICITY\_CL conversion matrix. |
| MATRIX\_COEFFICIENT\_ICTCP = 14 | ICTCP conversion matrix. |

#### \[h2\]OH\_AVCLevel

enum OH\_AVCLevel

**Description**

Enumerates the AVC levels.

**System capability**: SystemCapability.Multimedia.Media.CodecBase

**Since**: 12

| Value | Description |
| :-- | :-- |
| AVC\_LEVEL\_1 = 0 | Level 1. |
| AVC\_LEVEL\_1b = 1 | Level 1b. |
| AVC\_LEVEL\_11 = 2 | Level 1.1. |
| AVC\_LEVEL\_12 = 3 | Level 1.2. |
| AVC\_LEVEL\_13 = 4 | Level 1.3. |
| AVC\_LEVEL\_2 = 5 | Level 2. |
| AVC\_LEVEL\_21 = 6 | Level 2.1. |
| AVC\_LEVEL\_22 = 7 | Level 2.2. |
| AVC\_LEVEL\_3 = 8 | Level 3. |
| AVC\_LEVEL\_31 = 9 | Level 3.1. |
| AVC\_LEVEL\_32 = 10 | Level 3.2. |
| AVC\_LEVEL\_4 = 11 | Level 4. |
| AVC\_LEVEL\_41 = 12 | Level 4.1. |
| AVC\_LEVEL\_42 = 13 | Level 4.2. |
| AVC\_LEVEL\_5 = 14 | Level 5. |
| AVC\_LEVEL\_51 = 15 | Level 5.1. |
| AVC\_LEVEL\_52 = 16 | Level 5.2. |
| AVC\_LEVEL\_6 = 17 | Level 6. |
| AVC\_LEVEL\_61 = 18 | Level 6.1. |
| AVC\_LEVEL\_62 = 19 | Level 6.2. |

#### \[h2\]OH\_HEVCLevel

enum OH\_HEVCLevel

**Description**

Enumerates the HEVC levels.

**System capability**: SystemCapability.Multimedia.Media.CodecBase

**Since**: 12

| Value | Description |
| :-- | :-- |
| HEVC\_LEVEL\_1 = 0 | Level 1. |
| HEVC\_LEVEL\_2 = 1 | Level 2. |
| HEVC\_LEVEL\_21 = 2 | Level 2.1. |
| HEVC\_LEVEL\_3 = 3 | Level 3. |
| HEVC\_LEVEL\_31 = 4 | Level 3.1. |
| HEVC\_LEVEL\_4 = 5 | Level 4. |
| HEVC\_LEVEL\_41 = 6 | Level 4.1. |
| HEVC\_LEVEL\_5 = 7 | Level 5. |
| HEVC\_LEVEL\_51 = 8 | Level 5.1. |
| HEVC\_LEVEL\_52 = 9 | Level 5.2. |
| HEVC\_LEVEL\_6 = 10 | Level 6. |
| HEVC\_LEVEL\_61 = 11 | Level 6.1. |
| HEVC\_LEVEL\_62 = 12 | Level 6.2. |

#### \[h2\]OH\_VVCLevel

enum OH\_VVCLevel

**Description**

Enumerates the VVC levels.

**System capability**: SystemCapability.Multimedia.Media.CodecBase

**Since**: 15

| Value | Description |
| :-- | :-- |
| VVC\_LEVEL\_1 = 16 | Level 1.0. |
| VVC\_LEVEL\_2 = 32 | Level 2.0. |
| VVC\_LEVEL\_21 = 35 | Level 2.1. |
| VVC\_LEVEL\_3 = 48 | Level 3.0. |
| VVC\_LEVEL\_31 = 51 | Level 3.1. |
| VVC\_LEVEL\_4 = 64 | Level 4.0. |
| VVC\_LEVEL\_41 = 67 | Level 4.1. |
| VVC\_LEVEL\_5 = 80 | Level 5.0. |
| VVC\_LEVEL\_51 = 83 | Level 5.1. |
| VVC\_LEVEL\_52 = 86 | Level 5.2. |
| VVC\_LEVEL\_6 = 96 | Level 6.0. |
| VVC\_LEVEL\_61 = 99 | Level 6.1. |
| VVC\_LEVEL\_62 = 102 | Level 6.2. |
| VVC\_LEVEL\_63 = 105 | Level 6.3. |
| VVC\_LEVEL\_155 = 255 | Level 15.5. |

#### \[h2\]OH\_MPEG2Level

enum OH\_MPEG2Level

**Description**

Enumerates the MPEG2 levels.

**System capability**: SystemCapability.Multimedia.Media.CodecBase

**Since**: 17

| Value | Description |
| :-- | :-- |
| MPEG2\_LEVEL\_LOW = 0 | Low level. |
| MPEG2\_LEVEL\_MAIN = 1 | Main level. |
| MPEG2\_LEVEL\_HIGH\_1440 = 2 | High 1440 level. |
| MPEG2\_LEVEL\_HIGH = 3 | High level. |

#### \[h2\]OH\_MPEG4Level

enum OH\_MPEG4Level

**Description**

Enumerates the MPEG4 levels.

**System capability**: SystemCapability.Multimedia.Media.CodecBase

**Since**: 17

| Value | Description |
| :-- | :-- |
| MPEG4\_LEVEL\_0 = 0 | Level 0. |
| MPEG4\_LEVEL\_0B = 1 | Level 0B. |
| MPEG4\_LEVEL\_1 = 2 | Level 1. |
| MPEG4\_LEVEL\_2 = 3 | Level 2. |
| MPEG4\_LEVEL\_3 = 4 | Level 3. |
| MPEG4\_LEVEL\_3B = 5 | Level 3B. |
| MPEG4\_LEVEL\_4 = 6 | Level 4. |
| MPEG4\_LEVEL\_4A = 7 | Level 4A. |
| MPEG4\_LEVEL\_5 = 8 | Level 5. |
| MPEG4\_LEVEL\_6 = 9 | Level 6. |

#### \[h2\]OH\_H263Level

enum OH\_H263Level

**Description**

Enumerates the H.263 levels.

**System capability**: SystemCapability.Multimedia.Media.CodecBase

**Since**: 17

| Value | Description |
| :-- | :-- |
| H263\_LEVEL\_10 = 0 | Level 10. |
| H263\_LEVEL\_20 = 1 | Level 20. |
| H263\_LEVEL\_30 = 2 | Level 30. |
| H263\_LEVEL\_40 = 3 | Level 40. |
| H263\_LEVEL\_45 = 4 | Level 45. |
| H263\_LEVEL\_50 = 5 | Level 50. |
| H263\_LEVEL\_60 = 6 | Level 60. |
| H263\_LEVEL\_70 = 7 | Level 70. |

#### \[h2\]OH\_VC1Level

enum OH\_VC1Level

**Description**

Enumerates the VC-1 levels.

**System capability**: SystemCapability.Multimedia.Media.CodecBase

**Since**: 22

| Value | Description |
| :-- | :-- |
| VC1\_LEVEL\_L0 = 0 | Level L0. |
| VC1\_LEVEL\_L1 = 1 | Level L1. |
| VC1\_LEVEL\_L2 = 2 | Level L2. |
| VC1\_LEVEL\_L3 = 3 | Level L3. |
| VC1\_LEVEL\_L4 = 4 | Level L4. |
| VC1\_LEVEL\_LOW = 5 | Low level. |
| VC1\_LEVEL\_MEDIUM = 6 | Medium level. |
| VC1\_LEVEL\_HIGH = 7 | High level. |

#### \[h2\]OH\_WMV3Level

enum OH\_WMV3Level

**Description**

Enumerates the WMV3 levels.

**System capability**: SystemCapability.Multimedia.Media.CodecBase

**Since**: 22

| Value | Description |
| :-- | :-- |
| WMV3\_LEVEL\_LOW = 0 | Low level. |
| WMV3\_LEVEL\_MEDIUM = 1 | Medium level. |
| WMV3\_LEVEL\_HIGH = 2 | High level. |

#### \[h2\]OH\_TemporalGopReferenceMode

enum OH\_TemporalGopReferenceMode

**Description**

Enumerates the reference modes of temporal image groups.

**System capability**: SystemCapability.Multimedia.Media.CodecBase

**Since**: 12

| Value | Description |
| :-- | :-- |
| ADJACENT\_REFERENCE = 0 | Refers to the nearest short-term reference frame. |
| JUMP\_REFERENCE = 1 | Refers to the latest LTR frame. |
| UNIFORMLY\_SCALED\_REFERENCE = 2 | Drops video frames at the highest level, and evenly distributes the remaining frames. The number of temporal image groups must be a power of 2. |

#### \[h2\]OH\_BitrateMode

enum OH\_BitrateMode

**Description**

Enumerates the bit rate modes of an encoder.

**System capability**: SystemCapability.Multimedia.Media.CodecBase

**Since**: 10

| Value | Description |
| :-- | :-- |
| BITRATE\_MODE\_CBR = 0 | Constant bit rate. |
| BITRATE\_MODE\_VBR = 1 | Variable bit rate. |
| BITRATE\_MODE\_CQ = 2 | Constant quality. |
| BITRATE\_MODE\_SQR = 3 | 
Stable quality. It is supported only for H.265 (HEVC).

**Since**: 20

 |

#### Function Description

#### \[h2\]OH\_AVCodecOnError()

typedef void (\*OH\_AVCodecOnError)(OH\_AVCodec \*codec, int32\_t errorCode, void \*userData)

**Description**

Defines the pointer to the function that is called to report error information when an error occurs during the running of an OH\_AVCodec instance.

| Use Case | Error Code |
| :-- | :-- |
| Audio encoding/decoding | **AV\_ERR\_DRM\_DECRYPT\_FAILED**: DRM decryption failed. |
| Video encoding/decoding | 
**AV\_ERROR\_NO\_MEMORY**: System resources are insufficient.

**AV\_ERROR\_UNKNOWN**: An unknown error occurs. Analyze the error based on specific logs.

**AV\_ERR\_SERVICE\_DIED**: The service is dead.

 |
| Video decoding | **AV\_ERR\_VIDEO\_UNSUPPORTED\_COLOR\_SPACE\_CONVERSION**: The current input does not support CSC. |

**System capability**: SystemCapability.Multimedia.Media.CodecBase

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVCodec](../../structs/oh-avcodec/document.md) \*codec | Pointer to an OH\_AVCodec instance. |
| int32\_t errorCode | Error code. |
| void \*userData | Pointer to the data on which the caller depends when executing the callback. |

#### \[h2\]OH\_AVCodecOnStreamChanged()

typedef void (\*OH\_AVCodecOnStreamChanged)(OH\_AVCodec \*codec, OH\_AVFormat \*format, void \*userData)

**Description**

Defines the pointer to the function that is called to report the new stream description when the resolution of the input video stream being decoded or the output video stream that has been encoded changes.

Starting from API version 15, this function pointer is called to report the new stream description when the stream sampling rate, number of audio channels, or audio sampling format changes during audio decoding. The decoding formats that can detect these changes include AAC, FLAC, MP3, and VORBIS.

Note that the lifecycle of the pointer to the OH\_AVFormat instance is valid only when the function pointer is being called. Do not access the pointer to the instance after the function pointer is called.

**System capability**: SystemCapability.Multimedia.Media.CodecBase

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVCodec](../../structs/oh-avcodec/document.md) \*codec | Pointer to an OH\_AVCodec instance. |
| [OH\_AVFormat](../../structs/oh-avformat/document.md) \*format | Pointer to the description information about the new output stream. |
| void \*userData | Pointer to the data on which the caller depends when executing the callback. |

#### \[h2\]OH\_AVCodecOnNeedInputData()

typedef void (\*OH\_AVCodecOnNeedInputData)(OH\_AVCodec \*codec, uint32\_t index, OH\_AVMemory \*data, void \*userData)

**Description**

Defines the pointer to the function that is called when new input data is required during the running of an OH\_AVCodec instance. The function carries a buffer to fill in new input data.

**System capability**: SystemCapability.Multimedia.Media.CodecBase

**Since**: 9

**Deprecated from**: 11

**Substitute**: [OH\_AVCodecOnNeedInputBuffer](#oh_avcodeconneedinputbuffer)

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVCodec](../../structs/oh-avcodec/document.md) \*codec | Pointer to an OH\_AVCodec instance. |
| uint32\_t index | Index of the new input buffer. |
| [OH\_AVMemory](../../structs/oh-avmemory/document.md) \*data | Pointer to the data to fill in the new input buffer. |
| void \*userData | Pointer to the data on which the caller depends when executing the callback. |

#### \[h2\]OH\_AVCodecOnNewOutputData()

typedef void (\*OH\_AVCodecOnNewOutputData)(OH\_AVCodec \*codec, uint32\_t index, OH\_AVMemory \*data, OH\_AVCodecBufferAttr \*attr, void \*userData)

**Description**

Defines the pointer to the function that is called when new output data is generated during the running of an OH\_AVCodec instance. The function carries a buffer filled with new output data. Note that the lifecycle of the pointer to the OH\_AVCodecBufferAttr instance is valid only when the function pointer is being called. Do not access the pointer to the instance after the function pointer is called.

**System capability**: SystemCapability.Multimedia.Media.CodecBase

**Since**: 9

**Deprecated from**: 11

**Substitute**: [OH\_AVCodecOnNewOutputBuffer](#oh_avcodeconnewoutputbuffer)

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVCodec](../../structs/oh-avcodec/document.md) \*codec | Pointer to an OH\_AVCodec instance. |
| uint32\_t index | Index of the new output buffer. |
| [OH\_AVMemory](../../structs/oh-avmemory/document.md) \*data | Pointer to the data filled in the new output buffer. |
| [OH\_AVCodecBufferAttr](../../structs/oh-avcodecbufferattr/document.md) \*attr | Pointer to the description information about the new output buffer. |
| void \*userData | Pointer to the data on which the caller depends when executing the callback. |

#### \[h2\]OH\_AVCodecOnNeedInputBuffer()

typedef void (\*OH\_AVCodecOnNeedInputBuffer)(OH\_AVCodec \*codec, uint32\_t index, OH\_AVBuffer \*buffer, void \*userData)

**Description**

Defines the pointer to the function that is called when new input data is required during the running of an OH\_AVCodec instance. The function carries a buffer to fill in new input data.

**System capability**: SystemCapability.Multimedia.Media.CodecBase

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVCodec](../../structs/oh-avcodec/document.md) \*codec | Pointer to an OH\_AVCodec instance. |
| uint32\_t index | Index of the new input buffer. |
| [OH\_AVBuffer](../../structs/oh-avbuffer/document.md) \*buffer | Pointer to the data to fill in the new input buffer. |
| void \*userData | Pointer to the data on which the caller depends when executing the callback. |

#### \[h2\]OH\_AVCodecOnNewOutputBuffer()

typedef void (\*OH\_AVCodecOnNewOutputBuffer)(OH\_AVCodec \*codec, uint32\_t index, OH\_AVBuffer \*buffer, void \*userData)

**Description**

Defines the pointer to the function that is called when new output data is generated during the running of an OH\_AVCodec instance. The function carries a buffer filled with new output data.

**System capability**: SystemCapability.Multimedia.Media.CodecBase

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVCodec](../../structs/oh-avcodec/document.md) \*codec | Pointer to an OH\_AVCodec instance. |
| uint32\_t index | Index of the new output buffer. |
| [OH\_AVBuffer](../../structs/oh-avbuffer/document.md) \*buffer | Pointer to the data filled in the new output buffer. |
| void \*userData | Pointer to the data on which the caller depends when executing the callback. |

#### \[h2\]OH\_AVDataSourceReadAt()

typedef int32\_t (\*OH\_AVDataSourceReadAt)(OH\_AVBuffer \*data, int32\_t length, int64\_t pos)

**Description**

Defines a function pointer used to provide the capability of obtaining user-defined media data.

**System capability**: SystemCapability.Multimedia.Media.CodecBase

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVBuffer](../../structs/oh-avbuffer/document.md) \*data | Pointer to the buffer to be filled in. |
| int32\_t length | Length of the data to read. |
| int64\_t pos | Offset from which the data is read. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | Actual length of the data read to the buffer. |

#### \[h2\]OH\_AVDataSourceReadAtExt()

typedef int32\_t (\*OH\_AVDataSourceReadAtExt)(OH\_AVBuffer \*data, int32\_t length, int64\_t pos, void \*userData)

**Description**

Defines a function pointer used to provide the capability of obtaining user-defined media data.

**System capability**: SystemCapability.Multimedia.Media.CodecBase

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVBuffer](../../structs/oh-avbuffer/document.md) \*data | Pointer to the buffer to be filled in. |
| int32\_t length | Length of the data to read. |
| int64\_t pos | Offset from which the data is read. |
| void \*userData | Pointer to user-defined data. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | Actual length of the data read to the buffer. |
