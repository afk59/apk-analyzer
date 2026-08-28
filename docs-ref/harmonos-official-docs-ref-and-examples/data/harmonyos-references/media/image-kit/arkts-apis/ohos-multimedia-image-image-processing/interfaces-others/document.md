# Interfaces (Others)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/t60-XePMQLOBGu5M1GP2xw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062432Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AEFE25C1D8D31523525EA76D9853A764563EA2F934697C4CAD0C34C0B6B57D1F)

The initial APIs of this module are supported since API version 6. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### PositionArea7+

Describes area information in an image.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Multimedia.Image.Core

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| pixels | ArrayBuffer | No | No | Pixels of the image. Only pixel data in BGRA\_8888 format is supported. |
| offset | number | No | No | Offset for data reading, in bytes. |
| stride | number | No | No | Number of bytes from one row of pixels in memory to the next row of pixels in memory. in bytes. The value of **stride** must be greater than or equal to the value of **region.size.width** multiplied by 4. |
| region | [Region](#region8) | No | No | Region to read or write. The width of the region to write plus the X coordinate cannot be greater than the width of the original image. The height of the region to write plus the Y coordinate cannot be greater than the height of the original image. |

#### ImageInfo

Describes image information.

**System capability**: SystemCapability.Multimedia.Image.Core

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| size6+ | [Size](#size) | No | No | 
Image size.

**Atomic service API**: This API can be used in atomic services since API version 11.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

 |
| density9+ | number | No | No | 

Pixel density, in ppi.

**Atomic service API**: This API can be used in atomic services since API version 11.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

 |
| stride11+ | number | No | No | 

Number of bytes from one row of pixels in memory to the next row of pixels in memory. in bytes.stride >= region.size.width\*4

**Atomic service API**: This API can be used in atomic services since API version 11.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

 |
| pixelFormat12+ | [PixelMapFormat](../enums/document.md#pixelmapformat7) | No | No | 

Pixel format.

**Atomic service API**: This API can be used in atomic services since API version 12.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

 |
| alphaType12+ | [AlphaType](../enums/document.md#alphatype9) | No | No | 

Alpha type.

**Atomic service API**: This API can be used in atomic services since API version 12.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

 |
| mimeType12+ | string | No | No | 

Actual image format (MIME type).

The supported formats for image decoding and image encoding are different. Do not directly use the actual image format obtained after decoding as the value of **format** in [PackingOption](#packingoption) during image encoding.

You can use the **supportedFormats** property of [ImageSource](../interface-imagesource/document.md#properties) and of [ImagePacker](../interface-imagepacker/document.md#properties) to view the supported formats for decoding and encoding.

 |
| isHdr12+ | boolean | No | No | Whether the image is an HDR image. The value **true** means an HDR image, and **false** means an SDR image. For [ImageSource](../interface-imagesource/document.md), this parameter specifies whether the source image is in HDR format. For [PixelMap](../interface-pixelmap/document.md), this parameter specifies whether the decoded PixelMap is in HDR format. |

#### Size

Describes the size of an image.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Multimedia.Image.Core

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| height | number | No | No | Image height, in px. |
| width | number | No | No | Image width, in px. |

#### AuxiliaryPictureInfo13+

Describes the auxiliary picture information.

**System capability**: SystemCapability.Multimedia.Image.Core

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| auxiliaryPictureType | [AuxiliaryPictureType](../enums/document.md#auxiliarypicturetype13) | No | No | Auxiliary picture type. |
| size | [Size](#size) | No | No | Image size. |
| rowStride | number | No | No | Row stride. |
| pixelFormat | [PixelMapFormat](../enums/document.md#pixelmapformat7) | No | No | Pixel format. |
| colorSpace | [colorSpaceManager.ColorSpaceManager](../../../../../graphics/arkgraphics-2d/arkts-apis/ohos-graphics-colorspacemanager-color-space-management/document.md#colorspacemanager) | No | No | Color space. |

#### SourceOptions9+

Defines image source initialization options.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Multimedia.Image.Core

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| sourceDensity | number | No | No | 
Pixel density of the image resource, in ppi.

If **desiredSize** is not set in [DecodingOptions](#decodingoptions7) and **SourceOptions.sourceDensity** and **DecodingOptions.fitDensity** are not 0, the PixelMap output after decoding will be scaled.

The formula for calculating the width after scaling is as follows (the same applies to the height): (width \* fitDensity + (sourceDensity >> 1)) / sourceDensity.

 |
| sourcePixelFormat | [PixelMapFormat](../enums/document.md#pixelmapformat7) | No | Yes | Image pixel format. The default value is **UNKNOWN**. |
| sourceSize | [Size](#size) | No | Yes | Image pixel size. The default value is null. |

#### InitializationOptions8+

Defines PixelMap initialization options.

**System capability**: SystemCapability.Multimedia.Image.Core

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| alphaType9+ | [AlphaType](../enums/document.md#alphatype9) | No | Yes | 
Alpha type. The default value is **IMAGE\_ALPHA\_TYPE\_PREMUL**.

**Atomic service API**: This API can be used in atomic services since API version 11.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

 |
| editable | boolean | No | Yes | 

Whether the image pixels are editable. **true** if editable, **false** otherwise. The value **false** provides better image rendering and transmission performance. The default value is **false**.

**Atomic service API**: This API can be used in atomic services since API version 11.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

 |
| srcPixelFormat12+ | [PixelMapFormat](../enums/document.md#pixelmapformat7) | No | Yes | Pixel format of the passed-in buffer data. The default value is **BGRA\_8888**. |
| pixelFormat | [PixelMapFormat](../enums/document.md#pixelmapformat7) | No | Yes | 

Pixel format of the generated PixelMap. The default value is **RGBA\_8888**.

**Atomic service API**: This API can be used in atomic services since API version 11.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

 |
| scaleMode9+ | [ScaleMode](../enums/document.md#scalemode9) | No | Yes | 

Scale mode. The default value is **0**.

**Atomic service API**: This API can be used in atomic services since API version 11.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

 |
| size | [Size](#size) | No | No | 

Image size.

**Atomic service API**: This API can be used in atomic services since API version 11.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

 |

#### DecodingOptions7+

Describes the image decoding options.

**System capability**: SystemCapability.Multimedia.Image.ImageSource

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| sampleSize | number | No | Yes | 
Sampling size of the thumbnail. The default value is **1**. Currently, the value can only be **1**.

**Atomic service API**: This API can be used in atomic services since API version 11.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

 |
| rotate | number | No | Yes | 

Rotation angle. The default value is **0**.

**Atomic service API**: This API can be used in atomic services since API version 11.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

 |
| editable | boolean | No | Yes | 

Whether pixels are editable. **true** if editable, **false** otherwise. The default value is **false**.

If this parameter is set to **false**, the image rendering and transmission performance is improved, but the image cannot be edited. For example, the writePixels operation will fail.

**Atomic service API**: This API can be used in atomic services since API version 11.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

 |
| desiredSize | [Size](#size) | No | Yes | 

Expected output size. The value must be a positive integer and defaults to the original image size. If the output size is different from the original size, the output is stretched or scaled to the specified size.

Note: If both **desiredSize** and **desiredRegion** are passed to the decoding API, you must also include **cropAndScaleStrategy** to determine whether to crop or scale first. **CROP\_FIRST** is recommended.

**Atomic service API**: This API can be used in atomic services since API version 11.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

 |
| desiredRegion | [Region](#region8) | No | Yes | 

Rectangle specified by **Region** in the decoded image. When the original image is large and only a specific part of the image is required, you can set this parameter to improve performance. The default value is the original image size.

Note: If both **desiredSize** and **desiredRegion** are passed to the decoding API, you must also include **cropAndScaleStrategy** to determine whether to crop or scale first. **CROP\_FIRST** is recommended.

**Atomic service API**: This API can be used in atomic services since API version 11.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

 |
| desiredPixelFormat | [PixelMapFormat](../enums/document.md#pixelmapformat7) | No | Yes | 

Pixel format for decoding. The default value is **RGBA\_8888**. Only RGBA\_8888, BGRA\_8888, and RGB\_565 are supported. RGB\_565 is not supported for images with alpha channels, such as PNG, GIF, ICO, and WEBP.

**Atomic service API**: This API can be used in atomic services since API version 11.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

 |
| index | number | No | Yes | 

Index of the image to decode. The default value is **0**, indicating the first image. If this parameter is set to N, the (N+1)th image is used. For single-frame images, the value is always **0**. For multi-frame images such as animations, the value ranges from 0 to (Number of frames – 1).

**Atomic service API**: This API can be used in atomic services since API version 11.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

 |
| fitDensity9+ | number | No | Yes | 

Pixel density, in ppi. The default value is **0**.

**Atomic service API**: This API can be used in atomic services since API version 11.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

 |
| desiredColorSpace11+ | [colorSpaceManager.ColorSpaceManager](../../../../../graphics/arkgraphics-2d/arkts-apis/ohos-graphics-colorspacemanager-color-space-management/document.md#colorspacemanager) | No | Yes | Target color space. The default value is **UNKNOWN**. |
| desiredDynamicRange12+ | [DecodingDynamicRange](../enums/document.md#decodingdynamicrange12) | No | Yes | 

Desired dynamic range. The default value is **SDR**.

This property cannot be set for an image source created using [CreateIncrementalSource](../functions/document.md#imagecreateincrementalsource9). By default, the image source is decoded as SDR content.

If the platform does not support HDR, the setting is invalid and the content is decoded as SDR content by default.

 |
| cropAndScaleStrategy18+ | [CropAndScaleStrategy](../enums/document.md#cropandscalestrategy18) | No | Yes | 

If **desiredRegion** and **desiredSize** are both specified, the order of cropping and scaling is determined.

Only **SCALE\_FIRST** and **CROP\_FIRST** are supported.

 |

#### DecodingOptionsForPicture13+

Describes the image decoding options.

**System capability**: SystemCapability.Multimedia.Image.ImageSource

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| desiredAuxiliaryPictures | Array<[AuxiliaryPictureType](../enums/document.md#auxiliarypicturetype13)\> | No | No | 
Auxiliary picture type. If no auxiliary picture type is specified or an empty array is passed, the system decodes all available auxiliary picture types.

To exclude all auxiliary picture, you can decode the auxiliary picture to a PixelMap and use the PixelMap to create a Picture that contains only the main picture.

 |

#### Region8+

Describes the region information.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Multimedia.Image.Core

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| size7+ | [Size](#size) | No | No | Region size. |
| x7+ | number | No | No | X coordinate of the top-left corner of the region, in px. |
| y7+ | number | No | No | Y coordinate of the top-left corner of the region, in px. |

#### PackingOption

Describes the options for image encoding.

**System capability**: SystemCapability.Multimedia.Image.ImagePacker

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| format | string | No | No | 
Format of the packed image.

\- When [the input is ImageSource or PixelMap](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/image-encoding), the following formats are supported: image/jpeg, image/webp, image/png, image/heic (or image/heif)12+, image/sdr\_astc\_4x418+, image/sdr\_sut\_superfast\_4x418+ (depending on the hardware), and image/hdr\_astc\_4x420+.

\- When [the input is Picture](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/image-picture-encoding), only image/jpeg and image/heic (or image/heif)12+ are supported.

\- GIF image encoding requires input of multiple **PixelMap** objects, with the format specified as image/gif. The encoding can be performed using [packToDataFromPixelmapSequence](../interface-imagepacker/document.md#packtodatafrompixelmapsequence18) or [packToFileFromPixelmapSequence](../interface-imagepacker/document.md#packtofilefrompixelmapsequence18).

**NOTE**: The JPEG format does not support the alpha channel. If the JPEG format with the alpha channel is used for data encoding, the transparent color turns black.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| quality | number | No | No | 

1\. Quality of the output image set. This parameter takes effect only for JPEG and HEIF images. The value range is \[0, 100\]. The value **0** means the lowest quality, and **100** means the highest quality. The higher the quality, the larger the space occupied by the generated image. WebP and PNG images are lossless.

2\. In the case of sdr\_astc\_4x4 encoding, the parameter can be set to **92** and **85**.

3\. In the case of sut encoding, the parameter can be set to **92**.

4\. (Available since API version 20) In the case of hdr\_astc\_4x4 encoding, the parameter can be set to **85**.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| bufferSize9+ | number | No | Yes | 

Size of the buffer for receiving the encoded data, in bytes. If this parameter is not set, the default value 25 MB is used. If the size of an image exceeds 25 MB, you must specify the size. The value of **bufferSize** must be greater than the size of the encoded image. The use of [packToFile](../interface-imagepacker/document.md#packtofile11) is not restricted by this parameter.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| desiredDynamicRange12+ | [PackingDynamicRange](../enums/document.md#packingdynamicrange12) | No | Yes | Desired dynamic range. The default value is **SDR**. |
| needsPackProperties12+ | boolean | No | Yes | Whether encoding image property information, for example, Exif, is required. **true** if required, **false** otherwise. The default value is **false**. |

#### PackingOptionsForSequence18+

Defines the options for encoding animated images.

**System capability**: SystemCapability.Multimedia.Image.ImagePacker

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| frameCount | number | No | No | Number of frames specified in GIF encoding. |
| delayTimeList | Array<number> | No | No | 
Delay time of each frame in GIF encoding. The value must be greater than 0.

The unit is 10 milliseconds. For example, if this parameter is set to 10, the actual delay per frame is 100 ms.

If the array length is less than **frameCount**, the last value in the array will be used for the remaining frames.

 |
| disposalTypes | Array<number> | No | Yes | 

Array that defines how each image frame transitions. If the array length is less than **frameCount**, the last value in the array will be used for the remaining frames. The values can be:

\- **0**: No operation is required.

\- **1**: Keeps the image unchanged.

\- **2**: Restores the background color.

\- **3**: Restores to the previous state.

 |
| loopCount | number | No | Yes | 

Number of times that the output image in GIF encoding loops. The value range is \[0, 65535\].

The value **0** means an infinite loop. If this field is not carried, loop playback is not performed.

 |

#### ImagePropertyOptions11+

Describes the image properties.

**System capability**: SystemCapability.Multimedia.Image.ImageSource

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| index | number | No | Yes | Index of the image. The default value is **0**. |
| defaultValue | string | No | Yes | Default property value. The default value is null. |

#### Component9+

Describes the color components of an image.

**System capability**: SystemCapability.Multimedia.Image.Core

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| componentType | [ComponentType](../enums/document.md#componenttype9) | Yes | No | Color component type. |
| rowStride | number | Yes | No | Row stride. The camera preview stream data needs to be read by stride. For details, see [Solution to Screen Artifacts During Camera Preview](https://developer.huawei.com/consumer/en/doc/best-practices/bpta-deal-stride-solution). |
| pixelStride | number | Yes | No | Pixel stride. |
| byteBuffer | ArrayBuffer | Yes | No | Component buffer. |

#### HdrStaticMetadata12+

Describes the static metadata keys, that is, the values available for **HDR\_STATIC\_METADATA** in [HdrMetadataKey](../enums/document.md#hdrmetadatakey12).

**System capability**: SystemCapability.Multimedia.Image.Core

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| displayPrimariesX | Array<number> | No | No | X coordinate of the three primary colors of the display device after normalization. The array length is 3. The unit is 0.00002. The value range is \[0.0, 1.0\]. |
| displayPrimariesY | Array<number> | No | No | Y coordinate of the three primary colors of the display device after normalization. The array length is 3. The unit is 0.00002. The value range is \[0.0, 1.0\]. |
| whitePointX | number | No | No | X coordinate of the white point after normalization. The unit is 0.00002. The value range is \[0.0, 1.0\]. |
| whitePointY | number | No | No | Y coordinate of the white point after normalization. The unit is 0.00002. The value range is \[0.0, 1.0\]. |
| maxLuminance | number | No | No | Maximum luminance of the main monitor. The unit is 1, and the maximum value is 65535. |
| minLuminance | number | No | No | Minimum luminance of the main monitor. The unit is 0.0001, and the maximum value is 6.55535. |
| maxContentLightLevel | number | No | No | Maximum luminance of the displayed content. The unit is 1, and the maximum value is 65535. |
| maxFrameAverageLightLevel | number | No | No | Maximum average luminance of the displayed content. The unit is 1, and the maximum value is 65535. |

#### GainmapChannel12+

Describes the data content of a single channel of the gain map. For details, see ISO 21496-1.

**System capability**: SystemCapability.Multimedia.Image.Core

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| gainmapMax | number | No | No | Maximum value of the gain map. For details, see ISO 21496-1. |
| gainmapMin | number | No | No | Minimum value of the gain map. For details, see ISO 21496-1. |
| gamma | number | No | No | Gamma. For details, see ISO 21496-1. |
| baseOffset | number | No | No | Offset of the base graphic. For details, see ISO 21496-1. |
| alternateOffset | number | No | No | Offset of the alternative graphic that can be extracted. For details, see ISO 21496-1. |

#### HdrGainmapMetadata12+

Describes the metadata keys used by a gain map, that is, the values available for **HDR\_GAINMAP\_METADATA** in [HdrMetadataKey](../enums/document.md#hdrmetadatakey12). For details, see ISO 21496-1.

**System capability**: SystemCapability.Multimedia.Image.Core

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| writerVersion | number | No | No | Version used by the metadata editor. |
| miniVersion | number | No | No | Minimum version that needs to be understood for metadata parsing. |
| gainmapChannelCount | number | No | No | Number of color channels of the gain map. When the value is 3, the metadata values of the RGB channels are different. When the value is 1, the metadata values of the RGB channels are the same. For details, see ISO 21496-1. |
| useBaseColorFlag | boolean | No | No | Whether the color space of the base graphic is used. For details, see ISO 21496-1. **true** if used, **false** otherwise. |
| baseHeadroom | number | No | No | Headroom of the base graphic, which means the additional brightness that can be added to the base graphic. For details, see ISO 21496-1. |
| alternateHeadroom | number | No | No | Headroom of the alternate graphic. For details, see ISO 21496-1. |
| channels | Array<[GainmapChannel](#gainmapchannel12)\> | No | No | Number of channels. The length is 3. For details, see ISO 21496-1. |

#### GetImagePropertyOptions(deprecated)

Describes the image properties.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/tcue12ZORVq15MmNq209Pg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062432Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=59D2B8CABE7429848016A16DC07E53795DDBB362F630CF9198E3E9515C3E7DDC)

This API is supported since API version 7 and is deprecated since API version 11. You are advised to use [ImagePropertyOptions](#imagepropertyoptions11) instead.

**System capability**: SystemCapability.Multimedia.Image.ImageSource

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| index | number | No | Yes | Index of the image. The default value is **0**. |
| defaultValue | string | No | Yes | Default property value. The default value is null. |
