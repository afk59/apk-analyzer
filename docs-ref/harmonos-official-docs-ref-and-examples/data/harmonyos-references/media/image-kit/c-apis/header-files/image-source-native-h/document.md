# image\_source\_native.h

#### Overview

The file declares the APIs for image decoding.

**File to include**: <multimedia/image\_framework/image/image\_source\_native.h>

**Library**: libimage\_source.so

**System capability**: SystemCapability.Multimedia.Image.ImageSource

**Since**: 12

**Related module**: [Image\_NativeModule](../../modules/image-nativemodule/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_ImageSourceNative](../../structs/oh-imagesourcenative/document.md) | OH\_ImageSourceNative | Describes the image source, which is encapsulated at the native layer and is used to create image data. |
| [OH\_ImageSource\_Info](../../structs/oh-imagesource-info/document.md) | OH\_ImageSource\_Info | Describes the image source information, which is encapsulated at the native layer. The struct cannot be directly operated. Instead, functions must be called to create and release the struct and operate the fields in the struct. |
| [OH\_DecodingOptionsForPicture](../../structs/oh-decodingoptionsforpicture/document.md) | OH\_DecodingOptionsForPicture | Describes the decoding options for pictures. They are obtained by calling [OH\_DecodingOptionsForPicture\_Create](#oh_decodingoptionsforpicture_create). |
| [OH\_DecodingOptions](../../structs/oh-decodingoptions/document.md) | OH\_DecodingOptions | Describes the decoding options, which are encapsulated at the native layer. The struct is used to set decoding options and is passed in as an input parameter for creating a PixelMap. For details, see [OH\_ImageSourceNative\_CreatePixelmap](#oh_imagesourcenative_createpixelmap). |

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [IMAGE\_DYNAMIC\_RANGE](#image_dynamic_range) | IMAGE\_DYNAMIC\_RANGE | Enumerates the desired dynamic range for decoding. |
| [IMAGE\_ALLOCATOR\_TYPE](#image_allocator_type) | IMAGE\_ALLOCATOR\_TYPE | Enumerates the types of allocators used to allocate PixelMap memory. |
| [Image\_CropAndScaleStrategy](#image_cropandscalestrategy) | Image\_CropAndScaleStrategy | Enumerates the cropping and scaling strategies when **desiredSize** and **desiredRegion** are both specified. |

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [Image\_ErrorCode OH\_ImageSourceInfo\_Create(OH\_ImageSource\_Info \*\*info)](#oh_imagesourceinfo_create) | Creates the pointer to an OH\_ImageSource\_Info object. |
| [Image\_ErrorCode OH\_ImageSourceInfo\_GetWidth(OH\_ImageSource\_Info \*info, uint32\_t \*width)](#oh_imagesourceinfo_getwidth) | Obtains the image width. For an SVG image without the **width** tag, the default value **0** is returned. |
| [Image\_ErrorCode OH\_ImageSourceInfo\_GetHeight(OH\_ImageSource\_Info \*info, uint32\_t \*height)](#oh_imagesourceinfo_getheight) | Obtains the image height. For an SVG image without the **height** tag, the default value **0** is returned. |
| [Image\_ErrorCode OH\_ImageSourceInfo\_GetDynamicRange(OH\_ImageSource\_Info \*info, bool \*isHdr)](#oh_imagesourceinfo_getdynamicrange) | Obtains the dynamic range of an image. |
| [Image\_ErrorCode OH\_ImageSourceInfo\_GetMimetype(OH\_ImageSource\_Info \*info, Image\_MimeType \*mimeType)](#oh_imagesourceinfo_getmimetype) | Obtains the MIME type of an image. |
| [Image\_ErrorCode OH\_ImageSourceInfo\_Release(OH\_ImageSource\_Info \*info)](#oh_imagesourceinfo_release) | Releases the pointer to an OH\_ImageSource\_Info object. After this API is called, all attributes related to the OH\_ImageSource\_Info structure are released. Therefore, before calling this API, ensure that the relevant attributes are no longer needed or that a deep copy of these attributes has been completed. |
| [Image\_ErrorCode OH\_DecodingOptions\_Create(OH\_DecodingOptions \*\*options)](#oh_decodingoptions_create) | Creates the pointer to an OH\_DecodingOptions object. |
| [Image\_ErrorCode OH\_DecodingOptions\_GetPixelFormat(OH\_DecodingOptions \*options, int32\_t \*pixelFormat)](#oh_decodingoptions_getpixelformat) | Obtains the pixel format. |
| [Image\_ErrorCode OH\_DecodingOptions\_SetPixelFormat(OH\_DecodingOptions \*options, int32\_t pixelFormat)](#oh_decodingoptions_setpixelformat) | Sets the pixel format. |
| [Image\_ErrorCode OH\_DecodingOptions\_GetIndex(OH\_DecodingOptions \*options, uint32\_t \*index)](#oh_decodingoptions_getindex) | Obtains the index of an image. |
| [Image\_ErrorCode OH\_DecodingOptions\_SetIndex(OH\_DecodingOptions \*options, uint32\_t index)](#oh_decodingoptions_setindex) | Sets the index for an image. |
| [Image\_ErrorCode OH\_DecodingOptions\_GetRotate(OH\_DecodingOptions \*options, float \*rotate)](#oh_decodingoptions_getrotate) | Obtains the rotation degree. |
| [Image\_ErrorCode OH\_DecodingOptions\_SetRotate(OH\_DecodingOptions \*options, float rotate)](#oh_decodingoptions_setrotate) | Sets the rotation angle. |
| [Image\_ErrorCode OH\_DecodingOptions\_GetDesiredSize(OH\_DecodingOptions \*options, Image\_Size \*desiredSize)](#oh_decodingoptions_getdesiredsize) | Obtains the desired output size. |
| [Image\_ErrorCode OH\_DecodingOptions\_SetDesiredSize(OH\_DecodingOptions \*options, Image\_Size \*desiredSize)](#oh_decodingoptions_setdesiredsize) | Sets the desired output size. |
| [Image\_ErrorCode OH\_DecodingOptions\_GetDesiredRegion(OH\_DecodingOptions \*options, Image\_Region \*desiredRegion)](#oh_decodingoptions_getdesiredregion) | 
Obtains the region to decode.

Since the corresponding **SetDesiredRegion** function cannot meet the regional decoding requirements, starting from API version 19, you are advised to use [OH\_DecodingOptions\_GetCropRegion](#oh_decodingoptions_getcropregion) instead.

 |
| [Image\_ErrorCode OH\_DecodingOptions\_SetDesiredRegion(OH\_DecodingOptions \*options, Image\_Region \*desiredRegion)](#oh_decodingoptions_setdesiredregion) | 

Sets the region to decode.

The actual decoding will process the entire original image, without any regional decoding effect. Starting from API version 19, you are advised to use [OH\_DecodingOptions\_SetCropRegion](#oh_decodingoptions_setcropregion) instead.

 |
| [Image\_ErrorCode OH\_DecodingOptions\_GetDesiredDynamicRange(OH\_DecodingOptions \*options, int32\_t \*desiredDynamicRange)](#oh_decodingoptions_getdesireddynamicrange) | Obtains the desired dynamic range configured during decoding. |
| [Image\_ErrorCode OH\_DecodingOptions\_SetDesiredDynamicRange(OH\_DecodingOptions \*options, int32\_t desiredDynamicRange)](#oh_decodingoptions_setdesireddynamicrange) | Sets the desired dynamic range during decoding. |
| [Image\_ErrorCode OH\_DecodingOptions\_GetDesiredColorSpace(OH\_DecodingOptions \*options, int32\_t \*colorSpace)](#oh_decodingoptions_getdesiredcolorspace) | Obtains the color space set in the decoding options. |
| [Image\_ErrorCode OH\_DecodingOptions\_SetDesiredColorSpace(OH\_DecodingOptions \*options, int32\_t colorSpace)](#oh_decodingoptions_setdesiredcolorspace) | Sets the desired color space for the decoding options. |
| [Image\_ErrorCode OH\_DecodingOptions\_SetCropAndScaleStrategy(OH\_DecodingOptions \*options, int32\_t cropAndScaleStrategy)](#oh_decodingoptions_setcropandscalestrategy) | Sets the cropping and scaling strategy used during decoding. |
| [Image\_ErrorCode OH\_DecodingOptions\_GetCropAndScaleStrategy(OH\_DecodingOptions \*options, int32\_t \*cropAndScaleStrategy)](#oh_decodingoptions_getcropandscalestrategy) | Obtains the cropping and scaling strategy used during decoding. |
| [Image\_ErrorCode OH\_DecodingOptions\_GetCropRegion(OH\_DecodingOptions \*options, Image\_Region \*cropRegion)](#oh_decodingoptions_getcropregion) | Obtains the cropping region in the decoding options. |
| [Image\_ErrorCode OH\_DecodingOptions\_SetCropRegion(OH\_DecodingOptions \*options, Image\_Region \*cropRegion)](#oh_decodingoptions_setcropregion) | Sets the cropping region in the decoding options. |
| [Image\_ErrorCode OH\_DecodingOptions\_Release(OH\_DecodingOptions \*options)](#oh_decodingoptions_release) | Releases the pointer to an OH\_DecodingOptions object. |
| [Image\_ErrorCode OH\_ImageSourceNative\_CreateFromUri(char \*uri, size\_t uriSize, OH\_ImageSourceNative \*\*res)](#oh_imagesourcenative_createfromuri) | Creates the pointer to an OH\_ImageSourceNative object based on a URI. |
| [Image\_ErrorCode OH\_ImageSourceNative\_CreateFromFd(int32\_t fd, OH\_ImageSourceNative \*\*res)](#oh_imagesourcenative_createfromfd) | Creates the pointer to an OH\_ImageSourceNative object based on a file descriptor. |
| [Image\_ErrorCode OH\_ImageSourceNative\_CreateFromData(uint8\_t \*data, size\_t dataSize, OH\_ImageSourceNative \*\*res)](#oh_imagesourcenative_createfromdata) | 

Creates the pointer to an OH\_ImageSourceNative object based on buffer data.

The buffer data must be undecoded. Do not pass the pixel buffer data such as RGBA and YUV. If you want to create a PixelMap based on the pixel buffer data, call [OH\_PixelmapNative\_CreatePixelmap](../pixelmap-native-h/document.md#oh_pixelmapnative_createpixelmap).

 |
| [Image\_ErrorCode OH\_ImageSourceNative\_CreateFromDataWithUserBuffer(uint8\_t \*data, size\_t datalength, OH\_ImageSourceNative \*\*imageSource)](#oh_imagesourcenative_createfromdatawithuserbuffer) | Creates an image source from data buffer. The data buffer is directly accessed by the image source object, and therefore the data buffer must remain accessible within the lifecycle of the image source object. |
| [Image\_ErrorCode OH\_ImageSourceNative\_CreateFromRawFile(RawFileDescriptor \*rawFile, OH\_ImageSourceNative \*\*res)](#oh_imagesourcenative_createfromrawfile) | Creates the pointer to an OH\_ImageSourceNative object by using the raw file descriptor of an image resource file. |
| [Image\_ErrorCode OH\_ImageSourceNative\_CreatePixelmap(OH\_ImageSourceNative \*source, OH\_DecodingOptions \*options, OH\_PixelmapNative \*\*pixelmap)](#oh_imagesourcenative_createpixelmap) | Creates the pointer to an OH\_PixelmapNative object based on decoding options. |
| [Image\_ErrorCode OH\_ImageSourceNative\_CreatePixelmapUsingAllocator(OH\_ImageSourceNative \*source, OH\_DecodingOptions \*options, IMAGE\_ALLOCATOR\_TYPE allocator, OH\_PixelmapNative \*\*pixelmap)](#oh_imagesourcenative_createpixelmapusingallocator) | 

Creates an OH\_PixelmapNative object based on decoding options and memory type, where **allocatorType** specifies the memory type of the PixelMap.

By default, the system selects an appropriate memory type based on the image type, image size, and platform capability. When processing the returned PixelMap object, consider the impact of stride.

 |
| [Image\_ErrorCode OH\_ImageSourceNative\_CreatePixelmapList(OH\_ImageSourceNative \*source, OH\_DecodingOptions \*options, OH\_PixelmapNative \*resVecPixMap\[\], size\_t size)](#oh_imagesourcenative_createpixelmaplist) | 

Creates an array of OH\_PixelmapNative objects based on decoding options.

This function decodes all frames at once. If the number of frames is high or the size of individual frames is large, it can lead to significant memory usage. In these cases, you are advised to use the **Image** component for displaying animations. The **Image** component decodes frames one by one, which uses less memory than this function.

 |
| [Image\_ErrorCode OH\_ImageSourceNative\_CreatePicture(OH\_ImageSourceNative \*source, OH\_DecodingOptionsForPicture \*options, OH\_PictureNative \*\*picture)](#oh_imagesourcenative_createpicture) | Creates the pointer to an OH\_PictureNative object based on decoding options. |
| [Image\_ErrorCode OH\_ImageSourceNative\_CreatePictureAtIndex(OH\_ImageSourceNative \*source, uint32\_t index, OH\_PictureNative \*\*picture)](#oh_imagesourcenative_createpictureatindex) | Creates the pointer to an OH\_PictureNative object at the specified index. |
| [Image\_ErrorCode OH\_ImageSourceNative\_GetDelayTimeList(OH\_ImageSourceNative \*source, int32\_t \*delayTimeList, size\_t size)](#oh_imagesourcenative_getdelaytimelist) | Obtains the image delay time list. |
| [Image\_ErrorCode OH\_ImageSourceNative\_GetImageInfo(OH\_ImageSourceNative \*source, int32\_t index, OH\_ImageSource\_Info \*info)](#oh_imagesourcenative_getimageinfo) | Obtains the information about an image with a given index. |
| [Image\_ErrorCode OH\_ImageSourceNative\_GetImageProperty(OH\_ImageSourceNative \*source, Image\_String \*key, Image\_String \*value)](#oh_imagesourcenative_getimageproperty) | Obtains the value of an image property. The **value.data** obtained through this API lacks the string terminator **\\0**. Please use it with caution. |
| [Image\_ErrorCode OH\_ImageSourceNative\_GetImagePropertyWithNull(OH\_ImageSourceNative \*source, Image\_String \*key, Image\_String \*value)](#oh_imagesourcenative_getimagepropertywithnull) | Obtains the value of an image property. The output of **value.data** ends with the string terminator **\\0**. |
| [Image\_ErrorCode OH\_ImageSourceNative\_ModifyImageProperty(OH\_ImageSourceNative \*source, Image\_String \*key, Image\_String \*value)](#oh_imagesourcenative_modifyimageproperty) | Modifies the value of an image property. |
| [Image\_ErrorCode OH\_ImageSourceNative\_GetFrameCount(OH\_ImageSourceNative \*source, uint32\_t \*frameCount)](#oh_imagesourcenative_getframecount) | Obtains the number of image frames. |
| [Image\_ErrorCode OH\_ImageSourceNative\_GetSupportedFormats(Image\_MimeType \*\*supportedFormats, size\_t \*length)](#oh_imagesourcenative_getsupportedformats) | Obtains the supported image formats that can be decoded. |
| [Image\_ErrorCode OH\_ImageSourceNative\_Release(OH\_ImageSourceNative \*source)](#oh_imagesourcenative_release) | Releases the pointer to an OH\_ImageSourceNative object. |
| [Image\_ErrorCode OH\_DecodingOptionsForPicture\_Create(OH\_DecodingOptionsForPicture \*\*options)](#oh_decodingoptionsforpicture_create) | Creates the pointer to an OH\_DecodingOptionsForPicture object. |
| [Image\_ErrorCode OH\_DecodingOptionsForPicture\_GetDesiredAuxiliaryPictures(OH\_DecodingOptionsForPicture \*options, Image\_AuxiliaryPictureType \*\*desiredAuxiliaryPictures, size\_t \*length)](#oh_decodingoptionsforpicture_getdesiredauxiliarypictures) | Obtains desired auxiliary pictures in the decoding options (auxiliary pictures contained in **picture** expected to be decoded.) |
| [Image\_ErrorCode OH\_DecodingOptionsForPicture\_SetDesiredAuxiliaryPictures(OH\_DecodingOptionsForPicture \*options, Image\_AuxiliaryPictureType \*desiredAuxiliaryPictures, size\_t length)](#oh_decodingoptionsforpicture_setdesiredauxiliarypictures) | Sets desired auxiliary pictures in the decoding options. |
| [Image\_ErrorCode OH\_DecodingOptionsForPicture\_Release(OH\_DecodingOptionsForPicture \*options)](#oh_decodingoptionsforpicture_release) | Releases the pointer to an OH\_DecodingOptionsForPicture object. |

#### Enum Description

#### \[h2\]IMAGE\_DYNAMIC\_RANGE

enum IMAGE\_DYNAMIC\_RANGE

**Description**

Enumerates the desired dynamic range for decoding.

**Since**: 12

| Enum Item | Description |
| :-- | :-- |
| IMAGE\_DYNAMIC\_RANGE\_AUTO = 0 | Adaptive processing. |
| IMAGE\_DYNAMIC\_RANGE\_SDR = 1 | Standard dynamic range (SDR). |
| IMAGE\_DYNAMIC\_RANGE\_HDR = 2 | High dynamic range (HDR). |

#### \[h2\]IMAGE\_ALLOCATOR\_TYPE

enum IMAGE\_ALLOCATOR\_TYPE

**Description**

Enumerates the types of allocators used to allocate PixelMap memory.

**Since**: 15

| Enum Item | Description |
| :-- | :-- |
| IMAGE\_ALLOCATOR\_TYPE\_AUTO = 0 | The system determines whether to use DMA memory or shared memory to create a PixelMap. |
| IMAGE\_ALLOCATOR\_TYPE\_DMA = 1 | DMA memory is used to create a PixelMap. |
| IMAGE\_ALLOCATOR\_TYPE\_SHARE\_MEMORY = 2 | Shared memory is used to create a PixelMap. |

#### \[h2\]Image\_CropAndScaleStrategy

enum Image\_CropAndScaleStrategy

**Description**

Enumerates the cropping and scaling strategies when **desiredSize** and **desiredRegion** are both specified.

If the **ImageCropAndScaleStrategy** parameter is not specified in [OH\_DecodingOptions](../../structs/oh-decodingoptions/document.md) and both **desiredRegion** and **desiredSize** are set, the final decoding result may vary slightly due to differences in decoding algorithms used for different image formats.

For example, if the original image size is 200x200, and you specify **desiredSize:{width: 150, height: 150}, desiredRegion:{x: 0, y: 0, width: 100, height: 100}**, the expectation is to decode the top-left 1/4 region of the original image and then scale the pixelMap size to 150x150.

For JPEG and WebP images (as well as some DNG images that decode a JPEG preview within the file and therefore are treated as JPEG format), the system first performs downsampling. For instance, it might downsample by 7/8 and then crop the region based on a 175x175 image size. As a result, the final cropped region will be slightly larger than the top-left 1/4 of the original image.

For SVG images, which are vector-based and can be scaled without losing clarity, the system scales the image based on the ratio of **desiredSize** to the original image size and then crops the region. This results in a decoded region that may differ from the exact 1/4 region of the original image.

To ensure consistent results when both **desiredRegion** and **desiredSize** are set, set the **ImageCropAndScaleStrategy** parameter to **CROP\_FIRST**.

**Since**: 18

| Enum Item | Description |
| :-- | :-- |
| IMAGE\_CROP\_AND\_SCALE\_STRATEGY\_SCALE\_FIRST = 1 | Crops and then scales the image. |
| IMAGE\_CROP\_AND\_SCALE\_STRATEGY\_CROP\_FIRST = 2 | Scales and then crops the image. |

#### Function Description

#### \[h2\]OH\_ImageSourceInfo\_Create()

Image\_ErrorCode OH\_ImageSourceInfo\_Create(OH\_ImageSource\_Info \*\*info)

**Description**

Creates the pointer to an OH\_ImageSource\_Info object.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_ImageSource\_Info](../../structs/oh-imagesource-info/document.md) \*\*info | Double pointer to the OH\_ImageSource\_Info object created. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_ImageSourceInfo\_GetWidth()

Image\_ErrorCode OH\_ImageSourceInfo\_GetWidth(OH\_ImageSource\_Info \*info, uint32\_t \*width)

**Description**

Obtains the image width. For an SVG image without the **width** tag, the default value **0** is returned.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_ImageSource\_Info](../../structs/oh-imagesource-info/document.md) \*info | Pointer to an OH\_ImageSource\_Info object. |
| uint32\_t \*width | Pointer to the image width, in px. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_ImageSourceInfo\_GetHeight()

Image\_ErrorCode OH\_ImageSourceInfo\_GetHeight(OH\_ImageSource\_Info \*info, uint32\_t \*height)

**Description**

Obtains the image height. For an SVG image without the **height** tag, the default value **0** is returned.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_ImageSource\_Info](../../structs/oh-imagesource-info/document.md) \*info | Pointer to an OH\_ImageSource\_Info object. |
| uint32\_t \*height | Pointer to the image height, in px. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_ImageSourceInfo\_GetDynamicRange()

Image\_ErrorCode OH\_ImageSourceInfo\_GetDynamicRange(OH\_ImageSource\_Info \*info, bool \*isHdr)

**Description**

Obtains the dynamic range of an image.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_ImageSource\_Info](../../structs/oh-imagesource-info/document.md) \*info | Pointer to an OH\_ImageSource\_Info object. |
| bool \*isHdr | Whether the image is an HDR image. The value **true** means that the image is an HDR image, and the value **false** means the opposite. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_ImageSourceInfo\_GetMimetype()

Image\_ErrorCode OH\_ImageSourceInfo\_GetMimetype(OH\_ImageSource\_Info \*info, Image\_MimeType \*mimeType)

**Description**

Obtains the MIME type of an image.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/08/v3/oiv3i_nqQQif-OuZ57JXcg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062433Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C054EB9B67C8970F0CDB515423841A35C48D773C9DB584B763534E09FB7280F0)

-   The **data** [member variable of the mimeType structure](../../structs/image-string/document.md#member-variables) is a pointer of type char \*, which points to the address of the mimeType held internally by the info structure. Releasing info will cause the memory corresponding to this address to be released as well.
-   You can make a deep copy of **mimeType.data**, or release info only after mimeType has been used completely to avoid garbled characters.
-   **mimeType.data** is not terminated with **'\\0'** and needs to be used in conjunction with **mimeType.size**.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_ImageSource\_Info](../../structs/oh-imagesource-info/document.md) \*info | Pointer to an OH\_ImageSource\_Info object. |
| [Image\_MimeType](../../structs/image-string/document.md) \*mimeType | Pointer to the MIME type. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_SOURCE\_INVALID\_PARAMETER**: A parameter is incorrect. The **info** or **mimetype** parameter is a null pointer.

 |

#### \[h2\]OH\_ImageSourceInfo\_Release()

Image\_ErrorCode OH\_ImageSourceInfo\_Release(OH\_ImageSource\_Info \*info)

**Description**

Releases the pointer to an OH\_ImageSource\_Info object. After this API is called, all attributes related to the OH\_ImageSource\_Info structure are released. Therefore, before calling this API, ensure that the relevant attributes are no longer needed or that a deep copy of these attributes has been completed.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_ImageSource\_Info](../../structs/oh-imagesource-info/document.md) \*info | Pointer to an OH\_ImageSource\_Info object. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_DecodingOptions\_Create()

Image\_ErrorCode OH\_DecodingOptions\_Create(OH\_DecodingOptions \*\*options)

**Description**

Creates the pointer to an OH\_DecodingOptions object.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_DecodingOptions](../../structs/oh-decodingoptions/document.md) \*\*options | Double pointer to the OH\_DecodingOptions object created. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_DecodingOptions\_GetPixelFormat()

Image\_ErrorCode OH\_DecodingOptions\_GetPixelFormat(OH\_DecodingOptions \*options,int32\_t \*pixelFormat)

**Description**

Obtains the pixel format.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_DecodingOptions](../../structs/oh-decodingoptions/document.md) \*options | Pointer to an OH\_DecodingOptions object. |
| int32\_t \*pixelFormat | Pointer to the pixel format. For details, see [PIXEL\_FORMAT](../pixelmap-native-h/document.md#pixel_format). The default value is **RGBA\_8888**. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_DecodingOptions\_SetPixelFormat()

Image\_ErrorCode OH\_DecodingOptions\_SetPixelFormat(OH\_DecodingOptions \*options,int32\_t pixelFormat)

**Description**

Sets the pixel format.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_DecodingOptions](../../structs/oh-decodingoptions/document.md) \*options | Pointer to an OH\_DecodingOptions object. |
| int32\_t pixelFormat | Pointer to the pixel format. For details, see [PIXEL\_FORMAT](../pixelmap-native-h/document.md#pixel_format). The default value is **RGBA\_8888**. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_DecodingOptions\_GetIndex()

Image\_ErrorCode OH\_DecodingOptions\_GetIndex(OH\_DecodingOptions \*options, uint32\_t \*index)

**Description**

Obtains the index of an image.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_DecodingOptions](../../structs/oh-decodingoptions/document.md) \*options | Pointer to an OH\_DecodingOptions object. |
| uint32\_t \*index | Pointer to the index of the image to decode. The default value is **0**. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_DecodingOptions\_SetIndex()

Image\_ErrorCode OH\_DecodingOptions\_SetIndex(OH\_DecodingOptions \*options, uint32\_t index)

**Description**

Sets the index for an image.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_DecodingOptions](../../structs/oh-decodingoptions/document.md) \*options | Pointer to an OH\_DecodingOptions object. |
| uint32\_t index | Index of the image to decode. The default value is **0**. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_DecodingOptions\_GetRotate()

Image\_ErrorCode OH\_DecodingOptions\_GetRotate(OH\_DecodingOptions \*options, float \*rotate)

**Description**

Obtains the rotation degree.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_DecodingOptions](../../structs/oh-decodingoptions/document.md) \*options | Pointer to an OH\_DecodingOptions object. |
| float \*rotate | Rotation degree. The default value is **0**. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_DecodingOptions\_SetRotate()

Image\_ErrorCode OH\_DecodingOptions\_SetRotate(OH\_DecodingOptions \*options, float rotate)

**Description**

Sets the rotation angle.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_DecodingOptions](../../structs/oh-decodingoptions/document.md) \*options | Pointer to an OH\_DecodingOptions object. |
| float rotate | Rotation degree. The default value is 0. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_DecodingOptions\_GetDesiredSize()

Image\_ErrorCode OH\_DecodingOptions\_GetDesiredSize(OH\_DecodingOptions \*options,Image\_Size \*desiredSize)

**Description**

Obtains the desired output size.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_DecodingOptions](../../structs/oh-decodingoptions/document.md) \*options | Pointer to an OH\_DecodingOptions object. |
| [Image\_Size](../../structs/image-size/document.md) \*desiredSize | Pointer to the desired output size. The default value is the original image size. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_DecodingOptions\_SetDesiredSize()

Image\_ErrorCode OH\_DecodingOptions\_SetDesiredSize(OH\_DecodingOptions \*options,Image\_Size \*desiredSize)

**Description**

Sets the desired output size.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_DecodingOptions](../../structs/oh-decodingoptions/document.md) \*options | Pointer to an OH\_DecodingOptions object. |
| [Image\_Size](../../structs/image-size/document.md) \*desiredSize | Pointer to the desired output size. The default value is the original image size. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_DecodingOptions\_GetDesiredRegion()

Image\_ErrorCode OH\_DecodingOptions\_GetDesiredRegion(OH\_DecodingOptions \*options,Image\_Region \*desiredRegion)

**Description**

Obtains the region to decode.

Since the corresponding **SetDesiredRegion** function cannot meet the regional decoding requirements, starting from API version 19, you are advised to use [OH\_DecodingOptions\_GetCropRegion](#oh_decodingoptions_getcropregion) instead.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_DecodingOptions](../../structs/oh-decodingoptions/document.md) \*options | Pointer to an OH\_DecodingOptions object. |
| [Image\_Region](../../structs/image-region/document.md) \*desiredRegion | Pointer to the region to decode. By default, the entire image is decoded. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_DecodingOptions\_SetDesiredRegion()

Image\_ErrorCode OH\_DecodingOptions\_SetDesiredRegion(OH\_DecodingOptions \*options,Image\_Region \*desiredRegion)

**Description**

Sets the region to decode.

The actual decoding will process the entire original image, without any regional decoding effect. Starting from API version 19, you are advised to use [OH\_DecodingOptions\_SetCropRegion](#oh_decodingoptions_setcropregion) instead.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_DecodingOptions](../../structs/oh-decodingoptions/document.md) \*options | Pointer to an OH\_DecodingOptions object. |
| [Image\_Region](../../structs/image-region/document.md) \*desiredRegion | Pointer to the region to decode. By default, the entire image is decoded. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_DecodingOptions\_GetDesiredDynamicRange()

Image\_ErrorCode OH\_DecodingOptions\_GetDesiredDynamicRange(OH\_DecodingOptions \*options,int32\_t \*desiredDynamicRange)

**Description**

Obtains the desired dynamic range configured during decoding.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_DecodingOptions](../../structs/oh-decodingoptions/document.md) \*options | Pointer to an OH\_DecodingOptions object. |
| int32\_t \*desiredDynamicRange | Pointer to the desired dynamic range. For details, see [IMAGE\_DYNAMIC\_RANGE](#image_dynamic_range). The default value is **SDR**. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_DecodingOptions\_SetDesiredDynamicRange()

Image\_ErrorCode OH\_DecodingOptions\_SetDesiredDynamicRange(OH\_DecodingOptions \*options,int32\_t desiredDynamicRange)

**Description**

Sets the desired dynamic range during decoding.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_DecodingOptions](../../structs/oh-decodingoptions/document.md) \*options | Pointer to an OH\_DecodingOptions object. |
| int32\_t desiredDynamicRange | Desired dynamic range. For details, see [IMAGE\_DYNAMIC\_RANGE](#image_dynamic_range). The default value is **SDR**. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_DecodingOptions\_GetDesiredColorSpace()

Image\_ErrorCode OH\_DecodingOptions\_GetDesiredColorSpace(OH\_DecodingOptions \*options, int32\_t \*colorSpace)

**Description**

Obtains the color space set in the decoding options.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_DecodingOptions](../../structs/oh-decodingoptions/document.md) \*options | Pointer to the decoding options. |
| int32\_t \*colorSpace | Pointer to the color space. For details, see [ColorSpaceName](../../../../../graphics/arkgraphics-2d/c-apis/header-files/native-color-space-manager-h/document.md#colorspacename). |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_SOURCE\_INVALID\_PARAMETER**: A parameter is incorrect. The **options** or **colorSpace** parameter is a null pointer.

 |

#### \[h2\]OH\_DecodingOptions\_SetDesiredColorSpace()

Image\_ErrorCode OH\_DecodingOptions\_SetDesiredColorSpace(OH\_DecodingOptions \*options, int32\_t colorSpace)

**Description**

Sets the desired color space for the decoding options.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_DecodingOptions](../../structs/oh-decodingoptions/document.md) \*options | Pointer to the decoding options. |
| int32\_t colorSpace | Color space. For details, see [ColorSpaceName](../../../../../graphics/arkgraphics-2d/c-apis/header-files/native-color-space-manager-h/document.md#colorspacename). |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_SOURCE\_INVALID\_PARAMETER**: A parameter is incorrect. The **options** parameter is a null pointer or the value of **colorSpace** is not supported.

 |

#### \[h2\]OH\_DecodingOptions\_SetCropAndScaleStrategy()

Image\_ErrorCode OH\_DecodingOptions\_SetCropAndScaleStrategy(OH\_DecodingOptions \*options,int32\_t cropAndScaleStrategy)

**Description**

Sets the cropping and scaling strategy used during decoding.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_DecodingOptions](../../structs/oh-decodingoptions/document.md) \*options | Pointer to an OH\_DecodingOptions object. |
| int32\_t cropAndScaleStrategy | Cropping and scaling strategy that is executed when **desiredSize** and **desiredRegion** are both specified. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: The **options** parameter is a null pointer or the value of **cropAndScaleStrategy** is not within an enumerated value defined by **Image\_CropAndScaleStrategy**.

 |

#### \[h2\]OH\_DecodingOptions\_GetCropAndScaleStrategy()

Image\_ErrorCode OH\_DecodingOptions\_GetCropAndScaleStrategy(OH\_DecodingOptions \*options,int32\_t \*cropAndScaleStrategy)

**Description**

Obtains the cropping and scaling strategy used during decoding.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_DecodingOptions](../../structs/oh-decodingoptions/document.md) \*options | Pointer to an OH\_DecodingOptions object. |
| int32\_t \*cropAndScaleStrategy | Pointer to the cropping and scaling strategy that is executed when **desiredSize** and **desiredRegion** are both specified. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: The **options** or **cropAndScaleStrategy** parameter is a null pointer.

 |

#### \[h2\]OH\_DecodingOptions\_GetCropRegion()

Image\_ErrorCode OH\_DecodingOptions\_GetCropRegion(OH\_DecodingOptions \*options, Image\_Region \*cropRegion)

**Description**

Obtains the cropping region in the decoding options.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_DecodingOptions](../../structs/oh-decodingoptions/document.md) \*options | Pointer to the decoding options. |
| [Image\_Region](../../structs/image-region/document.md) \*cropRegion | Pointer to the cropping region. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_SOURCE\_INVALID\_PARAMETER**: The **options** or **cropRegion** parameter is a null pointer.

 |

#### \[h2\]OH\_DecodingOptions\_SetCropRegion()

Image\_ErrorCode OH\_DecodingOptions\_SetCropRegion(OH\_DecodingOptions \*options, Image\_Region \*cropRegion)

**Description**

Sets the cropping region in the decoding options.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_DecodingOptions](../../structs/oh-decodingoptions/document.md) \*options | Pointer to the decoding options. |
| [Image\_Region](../../structs/image-region/document.md) \*cropRegion | Pointer to the cropping region. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_SOURCE\_INVALID\_PARAMETER**: The **options** or **cropRegion** parameter is a null pointer.

 |

#### \[h2\]OH\_DecodingOptions\_Release()

Image\_ErrorCode OH\_DecodingOptions\_Release(OH\_DecodingOptions \*options)

**Description**

Releases the pointer to an OH\_DecodingOptions object.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_DecodingOptions](../../structs/oh-decodingoptions/document.md) \*options | Pointer to an OH\_DecodingOptions object. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_ImageSourceNative\_CreateFromUri()

Image\_ErrorCode OH\_ImageSourceNative\_CreateFromUri(char \*uri, size\_t uriSize, OH\_ImageSourceNative \*\*res)

**Description**

Creates the pointer to an OH\_ImageSourceNative object based on a URI.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| char \*uri | Pointer to the URI of the image source. Only file URIs or Base64 URIs are accepted. Currently, only absolute paths are supported. |
| size\_t uriSize | URI length. |
| [OH\_ImageSourceNative](../../structs/imagesourcenative/document.md) \*\*res | Double pointer to the OH\_ImageSourceNative object created at the C++ local layer. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

**IMAGE\_BAD\_SOURCE**: The decoding data source is abnormal.

 |

#### \[h2\]OH\_ImageSourceNative\_CreateFromFd()

Image\_ErrorCode OH\_ImageSourceNative\_CreateFromFd(int32\_t fd, OH\_ImageSourceNative \*\*res)

**Description**

Creates the pointer to an OH\_ImageSourceNative object based on a file descriptor.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| int32\_t fd | File descriptor. |
| [OH\_ImageSourceNative](../../structs/imagesourcenative/document.md) \*\*res | Double pointer to the OH\_ImageSourceNative object created at the C++ local layer. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_ImageSourceNative\_CreateFromData()

Image\_ErrorCode OH\_ImageSourceNative\_CreateFromData(uint8\_t \*data, size\_t dataSize, OH\_ImageSourceNative \*\*res)

**Description**

Creates the pointer to an OH\_ImageSourceNative object based on buffer data.

The buffer data must be undecoded. Do not pass the pixel buffer data such as RGBA and YUV. If you want to create a PixelMap based on the pixel buffer data, call [OH\_PixelmapNative\_CreatePixelmap](../pixelmap-native-h/document.md#oh_pixelmapnative_createpixelmap).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| uint8\_t \*data | Pointer to the buffer data. |
| size\_t dataSize | Size of the buffer. |
| [OH\_ImageSourceNative](../../structs/imagesourcenative/document.md) \*\*res | Double pointer to the OH\_ImageSourceNative object created at the C++ local layer. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

**IMAGE\_BAD\_SOURCE**: The decoding data source is abnormal.

 |

#### \[h2\]OH\_ImageSourceNative\_CreateFromDataWithUserBuffer()

Image\_ErrorCode OH\_ImageSourceNative\_CreateFromDataWithUserBuffer(uint8\_t \*data, size\_t datalength,OH\_ImageSourceNative \*\*imageSource)

**Description**

Creates an image source from data buffer. The data buffer is directly accessed by the image source object, and therefore the data buffer must remain accessible within the lifecycle of the image source object.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| uint8\_t \*data | Pointer to the data buffer. |
| size\_t datalength | Size of the data buffer. |
| [OH\_ImageSourceNative](../../structs/oh-imagesourcenative/document.md) \*\*imageSource | Double pointer to the image source. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_SOURCE\_INVALID\_PARAMETER**: The **data** or **imageSource** parameter is a null pointer or the **datalength** parameter is **0**.

 |

#### \[h2\]OH\_ImageSourceNative\_CreateFromRawFile()

Image\_ErrorCode OH\_ImageSourceNative\_CreateFromRawFile(RawFileDescriptor \*rawFile, OH\_ImageSourceNative \*\*res)

**Description**

Creates the pointer to an OH\_ImageSourceNative object by using the raw file descriptor of an image resource file.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [RawFileDescriptor](../../../../../application-framework/localization-kit/c-api/structs/rawfiledescriptor/document.md) \*rawFile | Pointer to the file descriptor of the raw file. |
| [OH\_ImageSourceNative](../../structs/imagesourcenative/document.md) \*\*res | Double pointer to the OH\_ImageSourceNative object created at the C++ local layer. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_ImageSourceNative\_CreatePixelmap()

Image\_ErrorCode OH\_ImageSourceNative\_CreatePixelmap(OH\_ImageSourceNative \*source, OH\_DecodingOptions \*options,OH\_PixelmapNative \*\*pixelmap)

**Description**

Creates the pointer to an OH\_PixelmapNative object based on decoding options.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_ImageSourceNative](../../structs/imagesourcenative/document.md) \*source | Pointer to an OH\_ImageSourceNative object. |
| [OH\_DecodingOptions](../../structs/oh-decodingoptions/document.md) \*options | Pointer to the decoding options. |
| [OH\_PixelmapNative](../../structs/oh-pixelmapnative/document.md) \*\*pixelmap | Double pointer to the OH\_PixelmapNative object created at the C++ local layer. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_ImageSourceNative\_CreatePixelmapUsingAllocator()

Image\_ErrorCode OH\_ImageSourceNative\_CreatePixelmapUsingAllocator(OH\_ImageSourceNative \*source,OH\_DecodingOptions \*options, IMAGE\_ALLOCATOR\_TYPE allocator, OH\_PixelmapNative \*\*pixelmap)

**Description**

Creates an OH\_PixelmapNative object based on decoding options and memory type, where **allocatorType** specifies the memory type of the PixelMap.

By default, the system selects an appropriate memory type based on the image type, image size, and platform capability. When processing the returned PixelMap object, consider the impact of stride.

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_ImageSourceNative](../../structs/imagesourcenative/document.md) \*source | Pointer to an OH\_ImageSourceNative object. |
| [OH\_DecodingOptions](../../structs/oh-decodingoptions/document.md) \*options | Pointer to the decoding options. |
| [IMAGE\_ALLOCATOR\_TYPE](#image_allocator_type) allocator | Memory type used by the returned PixelMap. |
| [OH\_PixelmapNative](../../structs/oh-pixelmapnative/document.md) \*\*pixelmap | Double pointer to the OH\_PixelmapNative object created at the C++ local layer. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

**IMAGE\_BAD\_SOURCE**: The data source is abnormal.

**IMAGE\_SOURCE\_UNSUPPORTED\_MIME\_TYPE**: The MIME type is not supported.

**IMAGE\_SOURCE\_TOO\_LARGE**: The image is too large.

**IMAGE\_SOURCE\_UNSUPPORTED\_ALLOCATOR\_TYPE**: The allocator type is not supported. For example, decoding HDR images using shared memory is not supported because only DMA supports HDR metadata.

**IMAGE\_SOURCE\_UNSUPPORTED\_OPTIONS**: The options are not supported. For example, an image cannot be converted into the required pixel format.

**IMAGE\_DECODE\_FAILED**: Decoding fails.

**IMAGE\_SOURCE\_ALLOC\_FAILED**: The memory allocation fails.

 |

#### \[h2\]OH\_ImageSourceNative\_CreatePixelmapList()

Image\_ErrorCode OH\_ImageSourceNative\_CreatePixelmapList(OH\_ImageSourceNative \*source, OH\_DecodingOptions \*options,OH\_PixelmapNative \*resVecPixMap\[\], size\_t size)

**Description**

Creates an array of OH\_PixelmapNative objects based on decoding options.

This function decodes all frames at once. If the number of frames is high or the size of individual frames is large, it can lead to significant memory usage. In these cases, you are advised to use the **Image** component for displaying animations. The **Image** component decodes frames one by one, which uses less memory than this function.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_ImageSourceNative](../../structs/imagesourcenative/document.md) \*source | Pointer to an OH\_ImageSourceNative object. |
| [OH\_DecodingOptions](../../structs/oh-decodingoptions/document.md) \*options | Pointer to the decoding options. |
| [OH\_PixelmapNative](../../structs/oh-pixelmapnative/document.md) \*resVecPixMap\[\] | Pointer to an array of OH\_PixelmapNative objects created at the C++ local layer. |
| size\_t size | Size of the array. You can use [OH\_ImageSourceNative\_GetFrameCount](#oh_imagesourcenative_getframecount) to obtain the size. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

**IMAGE\_UNSUPPORTED\_OPERATION**: The operation is not supported.

 |

#### \[h2\]OH\_ImageSourceNative\_CreatePicture()

Image\_ErrorCode OH\_ImageSourceNative\_CreatePicture(OH\_ImageSourceNative \*source, OH\_DecodingOptionsForPicture \*options,OH\_PictureNative \*\*picture)

**Description**

Creates the pointer to an OH\_PictureNative object based on decoding options.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_ImageSourceNative](../../structs/imagesourcenative/document.md) \*source | Pointer to an OH\_ImageSourceNative object. |
| [OH\_DecodingOptionsForPicture](../../structs/oh-decodingoptionsforpicture/document.md) \*options | Pointer to the decoding options. |
| [OH\_PictureNative](../../structs/oh-picturenative/document.md) \*\*picture | Double pointer to the OH\_PictureNative object created at the C++ local layer. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

**IMAGE\_DECODE\_FAILED**: Decoding fails.

 |

#### \[h2\]OH\_ImageSourceNative\_CreatePictureAtIndex()

Image\_ErrorCode OH\_ImageSourceNative\_CreatePictureAtIndex(OH\_ImageSourceNative \*source, uint32\_t index,OH\_PictureNative \*\*picture)

**Description**

Creates the pointer to an OH\_PictureNative object at the specified index.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_ImageSourceNative](../../structs/oh-imagesourcenative/document.md) \*source | Pointer to an OH\_ImageSourceNative object. |
| uint32\_t index | Index of the image. |
| [OH\_PictureNative](../../structs/oh-picturenative/document.md) \*\*picture | Double pointer to the OH\_PictureNative object created at the C++ local layer. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_SOURCE**: The data source is abnormal.

**IMAGE\_SOURCE\_UNSUPPORTED\_MIME\_TYPE**: The MIME type is not supported.

**IMAGE\_SOURCE\_TOO\_LARGE**: The image is too large.

**IMAGE\_SOURCE\_UNSUPPORTED\_OPTIONS**: The options are not supported. For example, an invalid image ID.

**IMAGE\_DECODE\_FAILED**: Decoding fails.

 |

#### \[h2\]OH\_ImageSourceNative\_GetDelayTimeList()

Image\_ErrorCode OH\_ImageSourceNative\_GetDelayTimeList(OH\_ImageSourceNative \*source, int32\_t \*delayTimeList, size\_t size)

**Description**

Obtains the image delay time list.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_ImageSourceNative](../../structs/imagesourcenative/document.md) \*source | Pointer to an OH\_ImageSourceNative object. |
| int32\_t \*delayTimeList | Pointer to the delay time list obtained. It cannot be a null pointer. |
| size\_t size | Size of the delay time list. You can use [OH\_ImageSourceNative\_GetFrameCount](#oh_imagesourcenative_getframecount) to obtain the size. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_ImageSourceNative\_GetImageInfo()

Image\_ErrorCode OH\_ImageSourceNative\_GetImageInfo(OH\_ImageSourceNative \*source, int32\_t index,OH\_ImageSource\_Info \*info)

**Description**

Obtains the information about an image with a given index.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_ImageSourceNative](../../structs/imagesourcenative/document.md) \*source | Pointer to an OH\_ImageSourceNative object. |
| int32\_t index | Index of an image. For a GIF image, the value range is \[0, N-1\], where N indicates the number of GIF frames. For an image with only one frame, you can pass in **0**. |
| [OH\_ImageSource\_Info](../../structs/oh-imagesource-info/document.md) \*info | Pointer to the image information obtained, which is an OH\_ImageSource\_Info struct. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_ImageSourceNative\_GetImageProperty()

Image\_ErrorCode OH\_ImageSourceNative\_GetImageProperty(OH\_ImageSourceNative \*source, Image\_String \*key,Image\_String \*value)

**Description**

Obtains the value of an image property. The **value.data** obtained through this API lacks the string terminator **\\0**. Please use it with caution.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_ImageSourceNative](../../structs/imagesourcenative/document.md) \*source | Pointer to an OH\_ImageSourceNative object. OH\_ImageSourceNative must be actively released after use. For details, please refer to [OH\_ImageSourceNative\_Release](#oh_imagesourcenative_release). |
| [Image\_String](../../structs/image-string/document.md) \*key | Pointer to the property. For details about the value range, please refer to the **OHOS\_IMAGE\_PROPERTY\_XXX** series constants defined in [Variables](../image-common-h/document.md#variables) of **image\_common.h**. |
| [Image\_String](../../structs/image-string/document.md) \*value | Pointer to the obtained value (output parameter). Before calling this interface, set **value->data** to a null pointer and **value->size** to **0**. The API will automatically allocate the required memory for **value->data** and assign a value to **value->size**. After finishing using this memory, release the memory pointed to by **value->data** using the **free()** function provided by the C standard library. Otherwise, a memory leak will occur. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_ImageSourceNative\_GetImagePropertyWithNull()

Image\_ErrorCode OH\_ImageSourceNative\_GetImagePropertyWithNull(OH\_ImageSourceNative \*source, Image\_String \*key,Image\_String \*value)

**Description**

Obtains the value of an image property. The output of **value.data** ends with the string terminator **\\0**.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_ImageSourceNative](../../structs/imagesourcenative/document.md) \*source | Pointer to an OH\_ImageSourceNative object. OH\_ImageSourceNative must be actively released after use. For details, please refer to [OH\_ImageSourceNative\_Release](#oh_imagesourcenative_release). |
| [Image\_String](../../structs/image-string/document.md) \*key | Pointer to the property key. For details about the value range, please refer to the **OHOS\_IMAGE\_PROPERTY\_XXX** series constants defined in [Variables](../image-common-h/document.md#variables) of **image\_common.h**. |
| [Image\_String](../../structs/image-string/document.md) \*value | Pointer to the value obtained. Before calling this interface, set **value->data** to a null pointer and **value->size** to **0**. The API will automatically allocate the required memory for **value->data** and assign a value to **value->size**. After finishing using this memory, release the memory pointed to by **value->data** using the **free()** function provided by the C standard library. Otherwise, a memory leak will occur. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_SOURCE\_INVALID\_PARAMETER**: The **source**, **key**, or **value** parameter is a null pointer.

 |

#### \[h2\]OH\_ImageSourceNative\_ModifyImageProperty()

Image\_ErrorCode OH\_ImageSourceNative\_ModifyImageProperty(OH\_ImageSourceNative \*source, Image\_String \*key,Image\_String \*value)

**Description**

Modifies the value of an image property.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_ImageSourceNative](../../structs/imagesourcenative/document.md) \*source | Pointer to an OH\_ImageSourceNative object. OH\_ImageSourceNative must be actively released after use. For details, please refer to [OH\_ImageSourceNative\_Release](#oh_imagesourcenative_release). |
| [Image\_String](../../structs/image-string/document.md) \*key | Pointer to the property key. For details about the value range, please refer to the **OHOS\_IMAGE\_PROPERTY\_XXX** series constants defined in [Variables](../image-common-h/document.md#variables) of **image\_common.h**. |
| [Image\_String](../../structs/image-string/document.md) \*value | Pointer to the new value. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_ImageSourceNative\_GetFrameCount()

Image\_ErrorCode OH\_ImageSourceNative\_GetFrameCount(OH\_ImageSourceNative \*source, uint32\_t \*frameCount)

**Description**

Obtains the number of image frames.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_ImageSourceNative](../../structs/imagesourcenative/document.md) \*source | Pointer to an OH\_ImageSourceNative object. |
| uint32\_t \*frameCount | Pointer to the number of frames obtained. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_ImageSourceNative\_GetSupportedFormats()

Image\_ErrorCode OH\_ImageSourceNative\_GetSupportedFormats(Image\_MimeType \*\*supportedFormats, size\_t \*length)

**Description**

Obtains the supported image formats that can be decoded.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [Image\_MimeType](../../structs/image-string/document.md) \*\*supportedFormats | Double pointer to the supported image formats. |
| size\_t \*length | Pointer to the size of the array. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_SOURCE\_INVALID\_PARAMETER**: The **supportedFormats** or **length** parameter is a null pointer.

 |

#### \[h2\]OH\_ImageSourceNative\_Release()

Image\_ErrorCode OH\_ImageSourceNative\_Release(OH\_ImageSourceNative \*source)

**Description**

Releases the pointer to an OH\_ImageSourceNative object.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_ImageSourceNative](../../structs/imagesourcenative/document.md) \*source | Pointer to an OH\_ImageSourceNative object. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_DecodingOptionsForPicture\_Create()

Image\_ErrorCode OH\_DecodingOptionsForPicture\_Create(OH\_DecodingOptionsForPicture \*\*options)

**Description**

Creates the pointer to an OH\_DecodingOptionsForPicture object.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_DecodingOptionsForPicture](../../structs/oh-decodingoptionsforpicture/document.md) \*\*options | Double pointer to the OH\_DecodingOptionsForPicture object created. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_DecodingOptionsForPicture\_GetDesiredAuxiliaryPictures()

Image\_ErrorCode OH\_DecodingOptionsForPicture\_GetDesiredAuxiliaryPictures(OH\_DecodingOptionsForPicture \*options,Image\_AuxiliaryPictureType \*\*desiredAuxiliaryPictures, size\_t \*length)

**Description**

Obtains desired auxiliary pictures in the decoding options (auxiliary pictures contained in **picture** expected to be decoded.)

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_DecodingOptionsForPicture](../../structs/oh-decodingoptionsforpicture/document.md) \*options | Pointer to an OH\_DecodingOptionsForPicture object. |
| [Image\_AuxiliaryPictureType](../picture-native-h/document.md#image_auxiliarypicturetype) \*\*desiredAuxiliaryPictures | Double pointer to the desired auxiliary pictures. |
| size\_t \*length | Length of the desired auxiliary pictures. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_DecodingOptionsForPicture\_SetDesiredAuxiliaryPictures()

Image\_ErrorCode OH\_DecodingOptionsForPicture\_SetDesiredAuxiliaryPictures(OH\_DecodingOptionsForPicture \*options,Image\_AuxiliaryPictureType \*desiredAuxiliaryPictures, size\_t length)

**Description**

Sets desired auxiliary pictures in the decoding options.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_DecodingOptionsForPicture](../../structs/oh-decodingoptionsforpicture/document.md) \*options | Pointer to an OH\_DecodingOptionsForPicture object. |
| [Image\_AuxiliaryPictureType](../picture-native-h/document.md#image_auxiliarypicturetype) \*desiredAuxiliaryPictures | Pointer to the desired auxiliary pictures. |
| size\_t length | Length of the desired auxiliary pictures. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_DecodingOptionsForPicture\_Release()

Image\_ErrorCode OH\_DecodingOptionsForPicture\_Release(OH\_DecodingOptionsForPicture \*options)

**Description**

Releases the pointer to an OH\_DecodingOptionsForPicture object.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_DecodingOptionsForPicture](../../structs/oh-decodingoptionsforpicture/document.md) \*options | Pointer to an OH\_DecodingOptionsForPicture object. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |
