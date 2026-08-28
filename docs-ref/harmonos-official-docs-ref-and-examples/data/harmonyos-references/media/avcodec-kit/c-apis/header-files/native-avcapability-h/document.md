# native\_avcapability.h

#### Overview

The file declares the native APIs used to query the codec capability.

**File to include**: <multimedia/player\_framework/native\_avcapability.h>

**Library**: libnative\_media\_codecbase.so

**System capability**: SystemCapability.Multimedia.Media.CodecBase

**Since**: 10

**Related module**: [AVCapability](../../modules/avcapability/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_AVRange](../../structs/oh-avrange/document.md) | OH\_AVRange | Describes the value range, which contains the minimum value and maximum value. |
| [OH\_AVCapability](../../structs/oh-avcapability/document.md) | OH\_AVCapability | Describes a native object for the OH\_AVCapability interface. |

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_AVCodecCategory](#oh_avcodeccategory) | OH\_AVCodecCategory | Enumerates the codec categories. |
| [OH\_AVCapabilityFeature](#oh_avcapabilityfeature) | OH\_AVCapabilityFeature | Enumerates the optional features that can be used in specific codec scenarios. |

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [OH\_AVCapability \*OH\_AVCodec\_GetCapability(const char \*mime, bool isEncoder)](#oh_avcodec_getcapability) | Obtains the codec capability recommended by the system. |
| [OH\_AVCapability \*OH\_AVCodec\_GetCapabilityByCategory(const char \*mime, bool isEncoder, OH\_AVCodecCategory category)](#oh_avcodec_getcapabilitybycategory) | Obtains the codec capability by category, which can be a hardware codec or software codec. |
| [bool OH\_AVCapability\_IsHardware(OH\_AVCapability \*capability)](#oh_avcapability_ishardware) | Checks whether a codec capability instance describes a hardware codec. |
| [const char \*OH\_AVCapability\_GetName(OH\_AVCapability \*capability)](#oh_avcapability_getname) | Obtains the codec name. |
| [int32\_t OH\_AVCapability\_GetMaxSupportedInstances(OH\_AVCapability \*capability)](#oh_avcapability_getmaxsupportedinstances) | Obtains the maximum number of codec instances supported by a codec. |
| [OH\_AVErrCode OH\_AVCapability\_GetEncoderBitrateRange(OH\_AVCapability \*capability, OH\_AVRange \*bitrateRange)](#oh_avcapability_getencoderbitraterange) | Obtains the bit rate range supported by an encoder. |
| [bool OH\_AVCapability\_IsEncoderBitrateModeSupported(OH\_AVCapability \*capability, OH\_BitrateMode bitrateMode)](#oh_avcapability_isencoderbitratemodesupported) | Checks whether an encoder supports a specific bit rate mode. |
| [OH\_AVErrCode OH\_AVCapability\_GetEncoderQualityRange(OH\_AVCapability \*capability, OH\_AVRange \*qualityRange)](#oh_avcapability_getencoderqualityrange) | Obtains the quality range supported by an encoder. |
| [OH\_AVErrCode OH\_AVCapability\_GetEncoderComplexityRange(OH\_AVCapability \*capability, OH\_AVRange \*complexityRange)](#oh_avcapability_getencodercomplexityrange) | Obtains the complexity range supported by an encoder. |
| [OH\_AVErrCode OH\_AVCapability\_GetAudioSupportedSampleRates(OH\_AVCapability \*capability, const int32\_t \*\*sampleRates, uint32\_t \*sampleRateNum)](#oh_avcapability_getaudiosupportedsamplerates) | Obtains the sample rates supported by an audio codec. |
| [OH\_AVErrCode OH\_AVCapability\_GetAudioSupportedSampleRateRanges(OH\_AVCapability \*capability, OH\_AVRange \*\*sampleRateRanges, uint32\_t \*rangesNum)](#oh_avcapability_getaudiosupportedsamplerateranges) | Obtains the sample rate ranges supported by an audio codec. |
| [OH\_AVErrCode OH\_AVCapability\_GetAudioChannelCountRange(OH\_AVCapability \*capability, OH\_AVRange \*channelCountRange)](#oh_avcapability_getaudiochannelcountrange) | Obtains the count range of audio channels supported by an audio codec. |
| [OH\_AVErrCode OH\_AVCapability\_GetVideoWidthAlignment(OH\_AVCapability \*capability, int32\_t \*widthAlignment)](#oh_avcapability_getvideowidthalignment) | Obtains the video width alignment supported by a video codec. |
| [OH\_AVErrCode OH\_AVCapability\_GetVideoHeightAlignment(OH\_AVCapability \*capability, int32\_t \*heightAlignment)](#oh_avcapability_getvideoheightalignment) | Obtains the video height alignment supported by a video codec. |
| [OH\_AVErrCode OH\_AVCapability\_GetVideoWidthRangeForHeight(OH\_AVCapability \*capability, int32\_t height, OH\_AVRange \*widthRange)](#oh_avcapability_getvideowidthrangeforheight) | Obtains the video width range supported by a video codec based on a given height. |
| [OH\_AVErrCode OH\_AVCapability\_GetVideoHeightRangeForWidth(OH\_AVCapability \*capability, int32\_t width, OH\_AVRange \*heightRange)](#oh_avcapability_getvideoheightrangeforwidth) | Obtains the video height range supported by a video codec based on a given width. |
| [OH\_AVErrCode OH\_AVCapability\_GetVideoWidthRange(OH\_AVCapability \*capability, OH\_AVRange \*widthRange)](#oh_avcapability_getvideowidthrange) | Obtains the video width range supported by a video codec. |
| [OH\_AVErrCode OH\_AVCapability\_GetVideoHeightRange(OH\_AVCapability \*capability, OH\_AVRange \*heightRange)](#oh_avcapability_getvideoheightrange) | Obtains the video height range supported by a video codec. |
| [bool OH\_AVCapability\_IsVideoSizeSupported(OH\_AVCapability \*capability, int32\_t width, int32\_t height)](#oh_avcapability_isvideosizesupported) | Checks whether a video codec supports a specific video size. |
| [OH\_AVErrCode OH\_AVCapability\_GetVideoFrameRateRange(OH\_AVCapability \*capability, OH\_AVRange \*frameRateRange)](#oh_avcapability_getvideoframeraterange) | Obtains the video frame rate range supported by a video codec. |
| [OH\_AVErrCode OH\_AVCapability\_GetVideoFrameRateRangeForSize(OH\_AVCapability \*capability, int32\_t width, int32\_t height, OH\_AVRange \*frameRateRange)](#oh_avcapability_getvideoframeraterangeforsize) | Obtains the video frame rate range supported by a video codec based on a given video size. |
| [bool OH\_AVCapability\_AreVideoSizeAndFrameRateSupported(OH\_AVCapability \*capability, int32\_t width, int32\_t height, int32\_t frameRate)](#oh_avcapability_arevideosizeandframeratesupported) | Checks whether a video codec supports the combination of a video size and frame rate. |
| [OH\_AVErrCode OH\_AVCapability\_GetVideoSupportedPixelFormats(OH\_AVCapability \*capability, const int32\_t \*\*pixelFormats, uint32\_t \*pixelFormatNum)](#oh_avcapability_getvideosupportedpixelformats) | Obtains the video pixel formats supported by a video codec. |
| [OH\_AVErrCode OH\_AVCapability\_GetVideoSupportedNativeBufferFormats(OH\_AVCapability \*capability, const OH\_NativeBuffer\_Format \*\*nativeBufferFormats, uint32\_t \*nativeBufferFormatNum)](#oh_avcapability_getvideosupportednativebufferformats) | Obtains the OH\_NativeBuffer formats supported by a video codec. This function provides the OH\_NativeBuffer formats that can be processed by a video codec. For details, see OH\_NativeBuffer\_Format. |
| [OH\_AVErrCode OH\_AVCapability\_GetSupportedProfiles(OH\_AVCapability \*capability, const int32\_t \*\*profiles, uint32\_t \*profileNum)](#oh_avcapability_getsupportedprofiles) | Obtains the profiles supported by a codec. |
| [OH\_AVErrCode OH\_AVCapability\_GetSupportedLevelsForProfile(OH\_AVCapability \*capability, int32\_t profile, const int32\_t \*\*levels, uint32\_t \*levelNum)](#oh_avcapability_getsupportedlevelsforprofile) | Obtains the codec levels supported by a profile. |
| [bool OH\_AVCapability\_AreProfileAndLevelSupported(OH\_AVCapability \*capability, int32\_t profile, int32\_t level)](#oh_avcapability_areprofileandlevelsupported) | Checks whether a codec supports the combination of a profile and level. |
| [bool OH\_AVCapability\_IsFeatureSupported(OH\_AVCapability \*capability, OH\_AVCapabilityFeature feature)](#oh_avcapability_isfeaturesupported) | Checks whether a codec supports a feature. |
| [OH\_AVFormat \*OH\_AVCapability\_GetFeatureProperties(OH\_AVCapability \*capability, OH\_AVCapabilityFeature feature)](#oh_avcapability_getfeatureproperties) | Obtains the properties of a feature. You must manually release the OH\_AVFormat instance in the return value. |

#### Enum Description

#### \[h2\]OH\_AVCodecCategory

enum OH\_AVCodecCategory

**Description**

Enumerates the codec categories.

**System capability**: SystemCapability.Multimedia.Media.CodecBase

**Since**: 10

| Value | Description |
| :-- | :-- |
| HARDWARE = 0 | Hardware codec. |
| SOFTWARE | Software codec. |

#### \[h2\]OH\_AVCapabilityFeature

enum OH\_AVCapabilityFeature

**Description**

Enumerates the optional features that can be used in specific codec scenarios.

**System capability**: SystemCapability.Multimedia.Media.CodecBase

**Since**: 12

| Value | Description |
| :-- | :-- |
| VIDEO\_ENCODER\_TEMPORAL\_SCALABILITY = 0 | Temporal scalability feature, which is available only in video encoding scenarios. |
| VIDEO\_ENCODER\_LONG\_TERM\_REFERENCE = 1 | Long-term reference frame feature, which is available only in video encoding scenarios. |
| VIDEO\_LOW\_LATENCY = 2 | Low latency feature, which is available only in video decoding scenarios. |
| VIDEO\_ENCODER\_B\_FRAME = 7 | 
B-frame encoding feature, which is available only in video encoding scenarios.

**Since**: 20

 |

#### Function Description

#### \[h2\]OH\_AVCodec\_GetCapability()

OH\_AVCapability \*OH\_AVCodec\_GetCapability(const char \*mime, bool isEncoder)

**Description**

Obtains the codec capability recommended by the system.

**System capability**: SystemCapability.Multimedia.Media.CodecBase

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| const char \*mime | Pointer to a string that describes the MIME type. For details, see [AVCODEC\_MIME\_TYPE](../native-avcodec-base-h/document.md#variables). |
| bool isEncoder | Whether the instance is an encoder. The value **true** means an encoder and **false** means a decoder. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVCapability](../../structs/oh-avcapability/document.md) \* | Pointer to the codec capability instance. If no existing codec matches, NULL is returned. |

#### \[h2\]OH\_AVCodec\_GetCapabilityByCategory()

OH\_AVCapability \*OH\_AVCodec\_GetCapabilityByCategory(const char \*mime, bool isEncoder, OH\_AVCodecCategory category)

**Description**

Obtains the codec capability by category, which can be a hardware codec or software codec.

**System capability**: SystemCapability.Multimedia.Media.CodecBase

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| const char \*mime | Pointer to a string that describes the MIME type. For details, see [AVCODEC\_MIME\_TYPE](../native-avcodec-base-h/document.md#variables). |
| bool isEncoder | Whether the instance is an encoder. The value **true** means an encoder and **false** means a decoder. |
| [OH\_AVCodecCategory](#oh_avcodeccategory) category | Codec category. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVCapability](../../structs/oh-avcapability/document.md) \* | Pointer to the codec capability instance. If no existing codec matches, NULL is returned. |

#### \[h2\]OH\_AVCapability\_IsHardware()

bool OH\_AVCapability\_IsHardware(OH\_AVCapability \*capability)

**Description**

Checks whether a codec capability instance describes a hardware codec.

**System capability**: SystemCapability.Multimedia.Media.CodecBase

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVCapability](../../structs/oh-avcapability/document.md) \*capability | Pointer to the codec capability. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | Check result for whether the codec capability instance describes a hardware codec. **true** if it describes a hardware codec, **false** otherwise. |

#### \[h2\]OH\_AVCapability\_GetName()

const char \*OH\_AVCapability\_GetName(OH\_AVCapability \*capability)

**Description**

Obtains the codec name.

**System capability**: SystemCapability.Multimedia.Media.CodecBase

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVCapability](../../structs/oh-avcapability/document.md) \*capability | Pointer to the codec capability. |

**Returns**

| Type | Description |
| :-- | :-- |
| const char \* | Codec name string. |

#### \[h2\]OH\_AVCapability\_GetMaxSupportedInstances()

int32\_t OH\_AVCapability\_GetMaxSupportedInstances(OH\_AVCapability \*capability)

**Description**

Obtains the maximum number of codec instances supported by a codec.

**System capability**: SystemCapability.Multimedia.Media.CodecBase

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVCapability](../../structs/oh-avcapability/document.md) \*capability | Pointer to the codec capability. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | Maximum number of codec instances supported. |

#### \[h2\]OH\_AVCapability\_GetEncoderBitrateRange()

OH\_AVErrCode OH\_AVCapability\_GetEncoderBitrateRange(OH\_AVCapability \*capability, OH\_AVRange \*bitrateRange)

**Description**

Obtains the bit rate range supported by an encoder.

**System capability**: SystemCapability.Multimedia.Media.CodecBase

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVCapability](../../structs/oh-avcapability/document.md) \*capability | Pointer to the encoder capability. If a pointer to the decoder capability is provided, undefined behavior occurs. |
| [OH\_AVRange](../../structs/oh-avrange/document.md) \*bitrateRange | Pointer to the bit rate range supported. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: The capability instance is invalid or the pointer to the bit rate range is null.

 |

#### \[h2\]OH\_AVCapability\_IsEncoderBitrateModeSupported()

bool OH\_AVCapability\_IsEncoderBitrateModeSupported(OH\_AVCapability \*capability, OH\_BitrateMode bitrateMode)

**Description**

Checks whether an encoder supports a specific bit rate mode.

**System capability**: SystemCapability.Multimedia.Media.CodecBase

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVCapability](../../structs/oh-avcapability/document.md) \*capability | Pointer to the encoder capability. If a pointer to the decoder capability is provided, undefined behavior occurs. |
| [OH\_BitrateMode](../native-avcodec-base-h/document.md#oh_bitratemode) bitrateMode | Bit rate mode. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | Check result for the support of the bit rate mode. **true** if supported, **false** otherwise. |

#### \[h2\]OH\_AVCapability\_GetEncoderQualityRange()

OH\_AVErrCode OH\_AVCapability\_GetEncoderQualityRange(OH\_AVCapability \*capability, OH\_AVRange \*qualityRange)

**Description**

Obtains the quality range supported by an encoder.

**System capability**: SystemCapability.Multimedia.Media.CodecBase

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVCapability](../../structs/oh-avcapability/document.md) \*capability | Pointer to the encoder capability. If a pointer to the decoder capability is provided, undefined behavior occurs. |
| [OH\_AVRange](../../structs/oh-avrange/document.md) \*qualityRange | Pointer to the quality range supported. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: The capability instance is invalid or the pointer to the quality range is null.

 |

#### \[h2\]OH\_AVCapability\_GetEncoderComplexityRange()

OH\_AVErrCode OH\_AVCapability\_GetEncoderComplexityRange(OH\_AVCapability \*capability, OH\_AVRange \*complexityRange)

**Description**

Obtains the complexity range supported by an encoder.

**System capability**: SystemCapability.Multimedia.Media.CodecBase

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVCapability](../../structs/oh-avcapability/document.md) \*capability | Pointer to the encoder capability. If a pointer to the decoder capability is provided, undefined behavior occurs. |
| [OH\_AVRange](../../structs/oh-avrange/document.md) \*complexityRange | Pointer to the complexity range supported. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: The capability instance is invalid or the pointer to the complexity range is null.

 |

#### \[h2\]OH\_AVCapability\_GetAudioSupportedSampleRates()

OH\_AVErrCode OH\_AVCapability\_GetAudioSupportedSampleRates(OH\_AVCapability \*capability, const int32\_t \*\*sampleRates, uint32\_t \*sampleRateNum)

**Description**

Obtains the sample rates supported by an audio codec.

**System capability**: SystemCapability.Multimedia.Media.CodecBase

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVCapability](../../structs/oh-avcapability/document.md) \*capability | Pointer to the audio codec capability. If a pointer to the video codec capability is provided, undefined behavior occurs. |
| const int32\_t \*\*sampleRates | Double pointer to the sample rate array. |
| uint32\_t \*sampleRateNum | Pointer to the number of elements in the array. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: The capability instance is invalid, the pointer to the sample rate array is null, or the pointer to the number of elements in the array is null.

**AV\_ERR\_UNKNOWN**: An unknown error occurs.

**AV\_ERR\_NO\_MEMORY**: Internal memory allocation failed.

 |

#### \[h2\]OH\_AVCapability\_GetAudioSupportedSampleRateRanges()

OH\_AVErrCode OH\_AVCapability\_GetAudioSupportedSampleRateRanges(OH\_AVCapability \*capability, OH\_AVRange \*\*sampleRateRanges, uint32\_t \*rangesNum)

**Description**

Obtains the sample rate ranges supported by an audio codec.

**System capability**: SystemCapability.Multimedia.Media.CodecBase

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVCapability](../../structs/oh-avcapability/document.md) \*capability | Pointer to the audio codec capability. If a pointer to the video codec capability is provided, undefined behavior occurs. |
| [OH\_AVRange](../../structs/oh-avrange/document.md) \*\*sampleRateRanges | Double pointer to the sample rate range array. |
| uint32\_t \*rangesNum | Pointer to the number of elements in the array. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: The capability instance is invalid, the pointer to the sample rate range array is null, or the pointer to the number of elements in the array is null.

**AV\_ERR\_UNKNOWN**: An unknown error occurs.

**AV\_ERR\_NO\_MEMORY**: Internal memory allocation failed.

 |

#### \[h2\]OH\_AVCapability\_GetAudioChannelCountRange()

OH\_AVErrCode OH\_AVCapability\_GetAudioChannelCountRange(OH\_AVCapability \*capability, OH\_AVRange \*channelCountRange)

**Description**

Obtains the count range of audio channels supported by an audio codec.

**System capability**: SystemCapability.Multimedia.Media.CodecBase

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVCapability](../../structs/oh-avcapability/document.md) \*capability | Pointer to the audio codec capability. If a pointer to the video codec capability is provided, undefined behavior occurs. |
| [OH\_AVRange](../../structs/oh-avrange/document.md) \*channelCountRange | Pointer to the count range of audio channels supported. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: The capability instance is invalid or the pointer to the count range of audio channels is null.

 |

#### \[h2\]OH\_AVCapability\_GetVideoWidthAlignment()

OH\_AVErrCode OH\_AVCapability\_GetVideoWidthAlignment(OH\_AVCapability \*capability, int32\_t \*widthAlignment)

**Description**

Obtains the video width alignment supported by a video codec.

**System capability**: SystemCapability.Multimedia.Media.CodecBase

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVCapability](../../structs/oh-avcapability/document.md) \*capability | Pointer to the video codec capability. If a pointer to the audio codec capability is provided, undefined behavior occurs. |
| int32\_t \*widthAlignment | Pointer to the video width alignment supported. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: The capability instance is invalid or the pointer to the video width alignment is null.

 |

#### \[h2\]OH\_AVCapability\_GetVideoHeightAlignment()

OH\_AVErrCode OH\_AVCapability\_GetVideoHeightAlignment(OH\_AVCapability \*capability, int32\_t \*heightAlignment)

**Description**

Obtains the video height alignment supported by a video codec.

**System capability**: SystemCapability.Multimedia.Media.CodecBase

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVCapability](../../structs/oh-avcapability/document.md) \*capability | Pointer to the video codec capability. If a pointer to the audio codec capability is provided, undefined behavior occurs. |
| int32\_t \*heightAlignment | Pointer to the video height alignment supported. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: The capability instance is invalid or the pointer to the video height alignment is null.

 |

#### \[h2\]OH\_AVCapability\_GetVideoWidthRangeForHeight()

OH\_AVErrCode OH\_AVCapability\_GetVideoWidthRangeForHeight(OH\_AVCapability \*capability, int32\_t height, OH\_AVRange \*widthRange)

**Description**

Obtains the video width range supported by a video codec based on a given height.

**System capability**: SystemCapability.Multimedia.Media.CodecBase

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVCapability](../../structs/oh-avcapability/document.md) \*capability | Pointer to the video codec capability. If a pointer to the audio codec capability is provided, undefined behavior occurs. |
| int32\_t height | Number of vertical video pixels. |
| [OH\_AVRange](../../structs/oh-avrange/document.md) \*widthRange | Pointer to the video width range supported. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: The capability instance is invalid, the height is not within the supported height range obtained through [OH\_AVCapability\_GetVideoHeightRange](#oh_avcapability_getvideoheightrange), or the pointer to the width range is null.

 |

#### \[h2\]OH\_AVCapability\_GetVideoHeightRangeForWidth()

OH\_AVErrCode OH\_AVCapability\_GetVideoHeightRangeForWidth(OH\_AVCapability \*capability, int32\_t width, OH\_AVRange \*heightRange)

**Description**

Obtains the video height range supported by a video codec based on a given width.

**System capability**: SystemCapability.Multimedia.Media.CodecBase

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVCapability](../../structs/oh-avcapability/document.md) \*capability | Pointer to the video codec capability. If a pointer to the audio codec capability is provided, undefined behavior occurs. |
| int32\_t width | Number of horizontal video pixels. |
| [OH\_AVRange](../../structs/oh-avrange/document.md) \*heightRange | Pointer to the video height range supported. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: The capability instance is invalid, the width is not within the supported width range obtained through [OH\_AVCapability\_GetVideoWidthRange](#oh_avcapability_getvideowidthrange), or the pointer to the height range is null.

 |

#### \[h2\]OH\_AVCapability\_GetVideoWidthRange()

OH\_AVErrCode OH\_AVCapability\_GetVideoWidthRange(OH\_AVCapability \*capability, OH\_AVRange \*widthRange)

**Description**

Obtains the video width range supported by a video codec.

**System capability**: SystemCapability.Multimedia.Media.CodecBase

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVCapability](../../structs/oh-avcapability/document.md) \*capability | Pointer to the video codec capability. If a pointer to the audio codec capability is provided, undefined behavior occurs. |
| [OH\_AVRange](../../structs/oh-avrange/document.md) \*widthRange | Pointer to the video width range supported. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: The capability instance is invalid or the pointer to the video width range is null.

 |

#### \[h2\]OH\_AVCapability\_GetVideoHeightRange()

OH\_AVErrCode OH\_AVCapability\_GetVideoHeightRange(OH\_AVCapability \*capability, OH\_AVRange \*heightRange)

**Description**

Obtains the video height range supported by a video codec.

**System capability**: SystemCapability.Multimedia.Media.CodecBase

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVCapability](../../structs/oh-avcapability/document.md) \*capability | Pointer to the video codec capability. If a pointer to the audio codec capability is provided, undefined behavior occurs. |
| [OH\_AVRange](../../structs/oh-avrange/document.md) \*heightRange | Pointer to the video height range supported. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: The capability instance is invalid or the pointer to the video height range is null.

 |

#### \[h2\]OH\_AVCapability\_IsVideoSizeSupported()

bool OH\_AVCapability\_IsVideoSizeSupported(OH\_AVCapability \*capability, int32\_t width, int32\_t height)

**Description**

Checks whether a video codec supports a specific video size.

**System capability**: SystemCapability.Multimedia.Media.CodecBase

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVCapability](../../structs/oh-avcapability/document.md) \*capability | Pointer to the video codec capability. If a pointer to the audio codec capability is provided, undefined behavior occurs. |
| int32\_t width | Number of horizontal video pixels. |
| int32\_t height | Number of vertical video pixels. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | Check result for the support of the video size. **true** if supported, **false** otherwise. |

#### \[h2\]OH\_AVCapability\_GetVideoFrameRateRange()

OH\_AVErrCode OH\_AVCapability\_GetVideoFrameRateRange(OH\_AVCapability \*capability, OH\_AVRange \*frameRateRange)

**Description**

Obtains the video frame rate range supported by a video codec.

**System capability**: SystemCapability.Multimedia.Media.CodecBase

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVCapability](../../structs/oh-avcapability/document.md) \*capability | Pointer to the video codec capability. If a pointer to the audio codec capability is provided, undefined behavior occurs. |
| [OH\_AVRange](../../structs/oh-avrange/document.md) \*frameRateRange | Pointer to the video frame rate range supported. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: The capability instance is invalid or the pointer to the video frame rate range is null.

 |

#### \[h2\]OH\_AVCapability\_GetVideoFrameRateRangeForSize()

OH\_AVErrCode OH\_AVCapability\_GetVideoFrameRateRangeForSize(OH\_AVCapability \*capability, int32\_t width, int32\_t height, OH\_AVRange \*frameRateRange)

**Description**

Obtains the video frame rate range supported by a video codec based on a given video size.

**System capability**: SystemCapability.Multimedia.Media.CodecBase

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVCapability](../../structs/oh-avcapability/document.md) \*capability | Pointer to the video codec capability. If a pointer to the audio codec capability is provided, undefined behavior occurs. |
| int32\_t width | Number of horizontal video pixels. |
| int32\_t height | Number of vertical video pixels. |
| [OH\_AVRange](../../structs/oh-avrange/document.md) \*frameRateRange | Pointer to the video frame rate range supported. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: The capability instance is invalid, the combination of the width and height is not supported, or the pointer to the frame rate range is null.

 |

#### \[h2\]OH\_AVCapability\_AreVideoSizeAndFrameRateSupported()

bool OH\_AVCapability\_AreVideoSizeAndFrameRateSupported(OH\_AVCapability \*capability, int32\_t width, int32\_t height, int32\_t frameRate)

**Description**

Checks whether a video codec supports the combination of a video size and frame rate.

**System capability**: SystemCapability.Multimedia.Media.CodecBase

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVCapability](../../structs/oh-avcapability/document.md) \*capability | Pointer to the video codec capability. If a pointer to the audio codec capability is provided, undefined behavior occurs. |
| int32\_t width | Number of horizontal video pixels. |
| int32\_t height | Number of vertical video pixels. |
| int32\_t frameRate | Number of frames per second. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | Check result for the support of the combination of the video size and frame rate. **true** if supported, **false** otherwise. |

#### \[h2\]OH\_AVCapability\_GetVideoSupportedPixelFormats()

OH\_AVErrCode OH\_AVCapability\_GetVideoSupportedPixelFormats(OH\_AVCapability \*capability, const int32\_t \*\*pixelFormats, uint32\_t \*pixelFormatNum)

**Description**

Obtains the video pixel formats supported by a video codec.

**System capability**: SystemCapability.Multimedia.Media.CodecBase

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVCapability](../../structs/oh-avcapability/document.md) \*capability | Pointer to the video codec capability. If a pointer to the audio codec capability is provided, undefined behavior occurs. |
| const int32\_t \*\*pixelFormats | Double pointer to the video pixel format array. |
| uint32\_t \*pixelFormatNum | Pointer to the number of elements in the array. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: The capability instance is invalid, the pointer to the video pixel format array is null, or the pointer to the number of elements in the array is null.

**AV\_ERR\_UNKNOWN**: An unknown error occurs.

**AV\_ERR\_NO\_MEMORY**: Internal memory allocation failed.

 |

#### \[h2\]OH\_AVCapability\_GetVideoSupportedNativeBufferFormats()

OH\_AVErrCode OH\_AVCapability\_GetVideoSupportedNativeBufferFormats(OH\_AVCapability \*capability, const OH\_NativeBuffer\_Format \*\*nativeBufferFormats, uint32\_t \*nativeBufferFormatNum)

**Description**

Obtains the OH\_NativeBuffer formats supported by a video codec. This function provides the OH\_NativeBuffer formats that can be processed by a video codec. For details, see OH\_NativeBuffer\_Format.

**System capability**: SystemCapability.Multimedia.Media.CodecBase

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVCapability](../../structs/oh-avcapability/document.md) \*capability | Pointer to the video codec capability. |
| const [OH\_NativeBuffer\_Format](../../../../../graphics/arkgraphics-2d/c-apis/header-files/buffer-common-h/document.md#oh_nativebuffer_format) \*\*nativeBufferFormats | Double pointer to the OH\_NativeBuffer\_Format array. |
| uint32\_t \*nativeBufferFormatNum | Pointer to the number of elements in the array. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: The capability instance is invalid, the capability instance is an audio codec capability, the pointer to the OH\_NativeBuffer\_Format array is nullptr,

or the pointer to the number of elements in the array is nullptr.

**AV\_ERR\_UNKNOWN**: An unknown error occurs.

**AV\_ERR\_NO\_MEMORY**: Internal memory allocation failed.

 |

#### \[h2\]OH\_AVCapability\_GetSupportedProfiles()

OH\_AVErrCode OH\_AVCapability\_GetSupportedProfiles(OH\_AVCapability \*capability, const int32\_t \*\*profiles, uint32\_t \*profileNum)

**Description**

Obtains the profiles supported by a codec.

**System capability**: SystemCapability.Multimedia.Media.CodecBase

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVCapability](../../structs/oh-avcapability/document.md) \*capability | Pointer to the codec capability. |
| const int32\_t \*\*profiles | Double pointer to the profile array. |
| uint32\_t \*profileNum | Pointer to the number of profiles in the array. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: The capability instance is invalid, the pointer to the profile array is null, or the pointer to the number of elements in the array is null.

**AV\_ERR\_UNKNOWN**: An unknown error occurs.

**AV\_ERR\_NO\_MEMORY**: Internal memory allocation failed.

 |

#### \[h2\]OH\_AVCapability\_GetSupportedLevelsForProfile()

OH\_AVErrCode OH\_AVCapability\_GetSupportedLevelsForProfile(OH\_AVCapability \*capability, int32\_t profile, const int32\_t \*\*levels, uint32\_t \*levelNum)

**Description**

Obtains the codec levels supported by a profile.

**System capability**: SystemCapability.Multimedia.Media.CodecBase

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVCapability](../../structs/oh-avcapability/document.md) \*capability | Pointer to the codec capability. |
| int32\_t profile | Codec profile. |
| const int32\_t \*\*levels | Double pointer to the codec level array. |
| uint32\_t \*levelNum | Pointer to the number of elements in the array. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: The capability instance is invalid, the level is not in the supported level array obtained through [OH\_AVCapability\_GetSupportedProfiles](#oh_avcapability_getsupportedprofiles), the pointer to the level array is null, or the pointer to the number of elements in the array is null.

**AV\_ERR\_UNKNOWN**: An unknown error occurs.

**AV\_ERR\_NO\_MEMORY**: Internal memory allocation failed.

 |

#### \[h2\]OH\_AVCapability\_AreProfileAndLevelSupported()

bool OH\_AVCapability\_AreProfileAndLevelSupported(OH\_AVCapability \*capability, int32\_t profile, int32\_t level)

**Description**

Checks whether a codec supports the combination of a profile and level.

**System capability**: SystemCapability.Multimedia.Media.CodecBase

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVCapability](../../structs/oh-avcapability/document.md) \*capability | Pointer to the codec capability. |
| int32\_t profile | Codec profile. |
| int32\_t level | Level of the codec. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | Check result for the support of the combination of the profile and level. **true** if supported, **false** otherwise. |

#### \[h2\]OH\_AVCapability\_IsFeatureSupported()

bool OH\_AVCapability\_IsFeatureSupported(OH\_AVCapability \*capability, OH\_AVCapabilityFeature feature)

**Description**

Checks whether a codec supports a feature.

**System capability**: SystemCapability.Multimedia.Media.CodecBase

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVCapability](../../structs/oh-avcapability/document.md) \*capability | Pointer to the codec capability. |
| [OH\_AVCapabilityFeature](#oh_avcapabilityfeature) feature | Codec feature. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | Check result for the feature. **true** if supported, **false** otherwise. |

#### \[h2\]OH\_AVCapability\_GetFeatureProperties()

OH\_AVFormat \*OH\_AVCapability\_GetFeatureProperties(OH\_AVCapability \*capability, OH\_AVCapabilityFeature feature)

**Description**

Obtains the properties of a feature. You must manually release the OH\_AVFormat instance in the return value.

**System capability**: SystemCapability.Multimedia.Media.CodecBase

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVCapability](../../structs/oh-avcapability/document.md) \*capability | Pointer to the codec capability. |
| [OH\_AVCapabilityFeature](#oh_avcapabilityfeature) feature | Codec feature. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVFormat](../../structs/oh-avformat/document.md) \* | Pointer to an OH\_AVFormat instance. |
