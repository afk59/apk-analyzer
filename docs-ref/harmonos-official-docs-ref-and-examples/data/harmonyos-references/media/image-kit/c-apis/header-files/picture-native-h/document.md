# picture\_native.h

#### Overview

The file declares the APIs for obtaining picture data and information.

**File to include**: <multimedia/image\_framework/image/picture\_native.h>

**Library**: libpicture.so

**System capability**: SystemCapability.Multimedia.Image.Core

**Since**: 13

**Related module**: [Image\_NativeModule](../../modules/image-nativemodule/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_PictureNative](../../structs/oh-picturenative/document.md) | OH\_PictureNative | Describes the picture, which is used to perform operations related to the picture. |
| [OH\_AuxiliaryPictureNative](../../structs/oh-auxiliarypicturenative/document.md) | OH\_AuxiliaryPictureNative | Describes the auxiliary picture, which is used to perform operations related to the auxiliary picture. |
| [OH\_AuxiliaryPictureInfo](../../structs/oh-auxiliarypictureinfo/document.md) | OH\_AuxiliaryPictureInfo | Describes the auxiliary picture information, which is used to perform operations related to the auxiliary picture information. |

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [Image\_AuxiliaryPictureType](#image_auxiliarypicturetype) | Image\_AuxiliaryPictureType | Enumerates the auxiliary picture types. |

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [Image\_ErrorCode OH\_PictureNative\_CreatePicture(OH\_PixelmapNative \*mainPixelmap, OH\_PictureNative \*\*picture)](#oh_picturenative_createpicture) | Creates the pointer to an OH\_PictureNative object. |
| [Image\_ErrorCode OH\_PictureNative\_GetMainPixelmap(OH\_PictureNative \*picture, OH\_PixelmapNative \*\*mainPixelmap)](#oh_picturenative_getmainpixelmap) | Obtains the pointer to the OH\_PixelmapNative object of a main picture. |
| [Image\_ErrorCode OH\_PictureNative\_GetHdrComposedPixelmap(OH\_PictureNative \*picture, OH\_PixelmapNative \*\*hdrPixelmap)](#oh_picturenative_gethdrcomposedpixelmap) | Obtains the pointer to the OH\_PixelmapNative object of an HDR picture. |
| [Image\_ErrorCode OH\_PictureNative\_GetGainmapPixelmap(OH\_PictureNative \*picture, OH\_PixelmapNative \*\*gainmapPixelmap)](#oh_picturenative_getgainmappixelmap) | Obtains the pointer to the OH\_PixelmapNative object of a gain map. |
| [Image\_ErrorCode OH\_PictureNative\_SetAuxiliaryPicture(OH\_PictureNative \*picture, Image\_AuxiliaryPictureType type,OH\_AuxiliaryPictureNative \*auxiliaryPicture)](#oh_picturenative_setauxiliarypicture) | Sets an auxiliary picture. |
| [Image\_ErrorCode OH\_PictureNative\_GetAuxiliaryPicture(OH\_PictureNative \*picture, Image\_AuxiliaryPictureType type,OH\_AuxiliaryPictureNative \*\*auxiliaryPicture)](#oh_picturenative_getauxiliarypicture) | Obtains an auxiliary picture by type. |
| [Image\_ErrorCode OH\_PictureNative\_GetMetadata(OH\_PictureNative \*picture, Image\_MetadataType metadataType,OH\_PictureMetadata \*\*metadata)](#oh_picturenative_getmetadata) | Obtains the metadata of a main picture. |
| [Image\_ErrorCode OH\_PictureNative\_SetMetadata(OH\_PictureNative \*picture, Image\_MetadataType metadataType,OH\_PictureMetadata \*metadata)](#oh_picturenative_setmetadata) | Sets the metadata for a main picture. |
| [Image\_ErrorCode OH\_PictureNative\_Release(OH\_PictureNative \*picture)](#oh_picturenative_release) | Releases the pointer to an OH\_PictureNative object. |
| [Image\_ErrorCode OH\_AuxiliaryPictureNative\_Create(uint8\_t \*data, size\_t dataLength, Image\_Size \*size,Image\_AuxiliaryPictureType type, OH\_AuxiliaryPictureNative \*\*auxiliaryPicture)](#oh_auxiliarypicturenative_create) | Creates the pointer to an OH\_AuxiliaryPictureNative object. This API supports only continuous pixel data whose [pixel format](../pixelmap-native-h/document.md#pixel_format) is BGRA\_8888 and creates an auxiliary picture in RGBA\_8888 format. |
| [Image\_ErrorCode OH\_AuxiliaryPictureNative\_WritePixels(OH\_AuxiliaryPictureNative \*auxiliaryPicture, uint8\_t \*source,size\_t bufferSize)](#oh_auxiliarypicturenative_writepixels) | Reads pixels in the buffer and writes the result to an auxiliary picture. |
| [Image\_ErrorCode OH\_AuxiliaryPictureNative\_ReadPixels(OH\_AuxiliaryPictureNative \*auxiliaryPicture, uint8\_t \*destination,size\_t \*bufferSize)](#oh_auxiliarypicturenative_readpixels) | Reads pixels of an auxiliary picture and writes the result to the buffer. |
| [Image\_ErrorCode OH\_AuxiliaryPictureNative\_GetType(OH\_AuxiliaryPictureNative \*auxiliaryPicture,Image\_AuxiliaryPictureType \*type)](#oh_auxiliarypicturenative_gettype) | Obtains the type of an auxiliary picture. |
| [Image\_ErrorCode OH\_AuxiliaryPictureNative\_GetInfo(OH\_AuxiliaryPictureNative \*auxiliaryPicture,OH\_AuxiliaryPictureInfo \*\*info)](#oh_auxiliarypicturenative_getinfo) | Obtains the information of an auxiliary picture. |
| [Image\_ErrorCode OH\_AuxiliaryPictureNative\_SetInfo(OH\_AuxiliaryPictureNative \*auxiliaryPicture,OH\_AuxiliaryPictureInfo \*info)](#oh_auxiliarypicturenative_setinfo) | Sets the information for an auxiliary picture. |
| [Image\_ErrorCode OH\_AuxiliaryPictureNative\_GetMetadata(OH\_AuxiliaryPictureNative \*auxiliaryPicture,Image\_MetadataType metadataType, OH\_PictureMetadata \*\*metadata)](#oh_auxiliarypicturenative_getmetadata) | Obtains the metadata of an auxiliary picture. |
| [Image\_ErrorCode OH\_AuxiliaryPictureNative\_SetMetadata(OH\_AuxiliaryPictureNative \*auxiliaryPicture,Image\_MetadataType metadataType, OH\_PictureMetadata \*metadata)](#oh_auxiliarypicturenative_setmetadata) | Sets the metadata for an auxiliary picture. |
| [Image\_ErrorCode OH\_AuxiliaryPictureNative\_Release(OH\_AuxiliaryPictureNative \*picture)](#oh_auxiliarypicturenative_release) | Releases the pointer to an OH\_AuxiliaryPictureNative object. |
| [Image\_ErrorCode OH\_AuxiliaryPictureInfo\_Create(OH\_AuxiliaryPictureInfo \*\*info)](#oh_auxiliarypictureinfo_create) | Creates an OH\_AuxiliaryPictureInfo object. |
| [Image\_ErrorCode OH\_AuxiliaryPictureInfo\_GetType(OH\_AuxiliaryPictureInfo \*info, Image\_AuxiliaryPictureType \*type)](#oh_auxiliarypictureinfo_gettype) | Obtains the auxiliary picture type in OH\_AuxiliaryPictureInfo. |
| [Image\_ErrorCode OH\_AuxiliaryPictureInfo\_SetType(OH\_AuxiliaryPictureInfo \*info, Image\_AuxiliaryPictureType type)](#oh_auxiliarypictureinfo_settype) | Sets the auxiliary picture type in OH\_AuxiliaryPictureInfo. |
| [Image\_ErrorCode OH\_AuxiliaryPictureInfo\_GetSize(OH\_AuxiliaryPictureInfo \*info, Image\_Size \*size)](#oh_auxiliarypictureinfo_getsize) | Obtains the image size in OH\_AuxiliaryPictureInfo. |
| [Image\_ErrorCode OH\_AuxiliaryPictureInfo\_SetSize(OH\_AuxiliaryPictureInfo \*info, Image\_Size \*size)](#oh_auxiliarypictureinfo_setsize) | Sets the image size in OH\_AuxiliaryPictureInfo. |
| [Image\_ErrorCode OH\_AuxiliaryPictureInfo\_GetRowStride(OH\_AuxiliaryPictureInfo \*info, uint32\_t \*rowStride)](#oh_auxiliarypictureinfo_getrowstride) | Obtains the row stride in OH\_AuxiliaryPictureInfo. |
| [Image\_ErrorCode OH\_AuxiliaryPictureInfo\_SetRowStride(OH\_AuxiliaryPictureInfo \*info, uint32\_t rowStride)](#oh_auxiliarypictureinfo_setrowstride) | Sets the row stride in OH\_AuxiliaryPictureInfo. |
| [Image\_ErrorCode OH\_AuxiliaryPictureInfo\_GetPixelFormat(OH\_AuxiliaryPictureInfo \*info, PIXEL\_FORMAT \*pixelFormat)](#oh_auxiliarypictureinfo_getpixelformat) | Obtains the pixel format in OH\_AuxiliaryPictureInfo. |
| [Image\_ErrorCode OH\_AuxiliaryPictureInfo\_SetPixelFormat(OH\_AuxiliaryPictureInfo \*info, PIXEL\_FORMAT pixelFormat)](#oh_auxiliarypictureinfo_setpixelformat) | Sets the pixel format in OH\_AuxiliaryPictureInfo. |
| [Image\_ErrorCode OH\_AuxiliaryPictureInfo\_Release(OH\_AuxiliaryPictureInfo \*info)](#oh_auxiliarypictureinfo_release) | Releases the pointer to an OH\_AuxiliaryPictureInfo object. |

#### Enum Description

#### \[h2\]Image\_AuxiliaryPictureType

enum Image\_AuxiliaryPictureType

**Description**

Enumerates the auxiliary picture types.

**Since**: 13

| Enum Item | Description |
| :-- | :-- |
| AUXILIARY\_PICTURE\_TYPE\_GAINMAP = 1 | Gain map, a mechanism for transforming an SDR image into an HDR image capable of adjustable display adjustment. It is a set of combinations describing how to apply gain map metadata. |
| AUXILIARY\_PICTURE\_TYPE\_DEPTH\_MAP = 2 | Depth map, which stores the depth data of an image. It captures the distance between each pixel and the camera to provide 3D scene structure. It is usually used for 3D modeling and scene comprehension. |
| AUXILIARY\_PICTURE\_TYPE\_UNREFOCUS\_MAP = 3 | Defocused portrait original image, which provides a method to emphasize background blur in portrait photographing. It helps users select a focus region in post-processing, allowing for greater creative control. |
| AUXILIARY\_PICTURE\_TYPE\_LINEAR\_MAP = 4 | Linear map, which is used to provide additional viewpoints or supplementary information. It is usually used to enhance visual effects and can contain linear representations of lighting, colors, or other visual elements in a scene. |
| AUXILIARY\_PICTURE\_TYPE\_FRAGMENT\_MAP = 5 | Fragment map, which indicates regions obscured by watermarks in the original image. It is used to remove or correct the watermark interference, thereby enhancing the image completeness and visibility. |

#### Function Description

#### \[h2\]OH\_PictureNative\_CreatePicture()

Image\_ErrorCode OH\_PictureNative\_CreatePicture(OH\_PixelmapNative \*mainPixelmap, OH\_PictureNative \*\*picture)

**Description**

Creates the pointer to an OH\_PictureNative object.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_PixelmapNative](../../structs/oh-picturenative/document.md) \*mainPixelmap | Pointer to the OH\_PixelmapNative object of the main picture. |
| [OH\_PictureNative](../../structs/oh-picturenative/document.md) \*\*picture | Double pointer to the OH\_PictureNative object created. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_PictureNative\_GetMainPixelmap()

Image\_ErrorCode OH\_PictureNative\_GetMainPixelmap(OH\_PictureNative \*picture, OH\_PixelmapNative \*\*mainPixelmap)

**Description**

Obtains the pointer to the OH\_PixelmapNative object of a main picture.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_PictureNative](../../structs/oh-picturenative/document.md) \*picture | Pointer to an OH\_PictureNative object. |
| [OH\_PictureNative](../../structs/oh-picturenative/document.md) \*\*mainPixelmap | Double pointer to the OH\_PixelmapNative object obtained. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_PictureNative\_GetHdrComposedPixelmap()

Image\_ErrorCode OH\_PictureNative\_GetHdrComposedPixelmap(OH\_PictureNative \*picture, OH\_PixelmapNative \*\*hdrPixelmap)

**Description**

Obtains the pointer to the OH\_PixelmapNative object of an HDR picture.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_PictureNative](../../structs/oh-picturenative/document.md) \*picture | Pointer to an OH\_PictureNative object. |
| [OH\_PictureNative](../../structs/oh-picturenative/document.md) \*\*hdrPixelmap | Double pointer to the OH\_PixelmapNative object of the HDR picture. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

**IMAGE\_UNSUPPORTED\_OPERATION**: The operation is not supported. For example, the Picture object does not contain a gain map.

 |

#### \[h2\]OH\_PictureNative\_GetGainmapPixelmap()

Image\_ErrorCode OH\_PictureNative\_GetGainmapPixelmap(OH\_PictureNative \*picture, OH\_PixelmapNative \*\*gainmapPixelmap)

**Description**

Obtains the pointer to the OH\_PixelmapNative object of a gain map.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_PictureNative](../../structs/oh-picturenative/document.md) \*picture | Pointer to an OH\_PictureNative object. |
| [OH\_PictureNative](../../structs/oh-picturenative/document.md) \*\*gainmapPixelmap | Double pointer to the OH\_PixelmapNative object of the gain map. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_PictureNative\_SetAuxiliaryPicture()

Image\_ErrorCode OH\_PictureNative\_SetAuxiliaryPicture(OH\_PictureNative \*picture, Image\_AuxiliaryPictureType type,OH\_AuxiliaryPictureNative \*auxiliaryPicture)

**Description**

Sets an auxiliary picture.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_PictureNative](../../structs/oh-picturenative/document.md) \*picture | Pointer to an OH\_PictureNative object. |
| [Image\_AuxiliaryPictureType](#image_auxiliarypicturetype) type | Type of the auxiliary picture. |
| [OH\_AuxiliaryPictureNative](../../structs/oh-auxiliarypicturenative/document.md) \*auxiliaryPicture | Pointer to an OH\_AuxiliaryPictureNative object. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_PictureNative\_GetAuxiliaryPicture()

Image\_ErrorCode OH\_PictureNative\_GetAuxiliaryPicture(OH\_PictureNative \*picture, Image\_AuxiliaryPictureType type,OH\_AuxiliaryPictureNative \*\*auxiliaryPicture)

**Description**

Obtains an auxiliary picture by type.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_PictureNative](../../structs/oh-picturenative/document.md) \*picture | Pointer to an OH\_PictureNative object. |
| [Image\_AuxiliaryPictureType](#image_auxiliarypicturetype) type | Type of the auxiliary picture. |
| [OH\_AuxiliaryPictureNative](../../structs/oh-auxiliarypicturenative/document.md) \*\*auxiliaryPicture | Double pointer to the OH\_AuxiliaryPictureNative object obtained. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_PictureNative\_GetMetadata()

Image\_ErrorCode OH\_PictureNative\_GetMetadata(OH\_PictureNative \*picture, Image\_MetadataType metadataType,OH\_PictureMetadata \*\*metadata)

**Description**

Obtains the metadata of a main picture.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_PictureNative](../../structs/oh-picturenative/document.md) \*picture | Pointer to an OH\_PictureNative object. |
| [Image\_MetadataType](../image-common-h/document.md#image_metadatatype) metadataType | Metadata type. |
| [OH\_PictureMetadata](../../structs/oh-picturemetadata/document.md) \*\*metadata | Double pointer to the metadata. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

**IMAGE\_UNSUPPORTED\_METADATA**: unsupported metadata type.

 |

#### \[h2\]OH\_PictureNative\_SetMetadata()

Image\_ErrorCode OH\_PictureNative\_SetMetadata(OH\_PictureNative \*picture, Image\_MetadataType metadataType,OH\_PictureMetadata \*metadata)

**Description**

Sets the metadata for a main picture.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_PictureNative](../../structs/oh-picturenative/document.md) \*picture | Pointer to an OH\_PictureNative object. |
| [Image\_MetadataType](../image-common-h/document.md#image_metadatatype) metadataType | Metadata type. |
| [OH\_PictureMetadata](../../structs/oh-picturemetadata/document.md) \*metadata | Pointer to the metadata. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

**IMAGE\_UNSUPPORTED\_METADATA**: unsupported metadata type.

 |

#### \[h2\]OH\_PictureNative\_Release()

Image\_ErrorCode OH\_PictureNative\_Release(OH\_PictureNative \*picture)

**Description**

Releases the pointer to an OH\_PictureNative object.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_PictureNative](../../structs/oh-picturenative/document.md) \*picture | Pointer to an OH\_PictureNative object. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_AuxiliaryPictureNative\_Create()

Image\_ErrorCode OH\_AuxiliaryPictureNative\_Create(uint8\_t \*data, size\_t dataLength, Image\_Size \*size,Image\_AuxiliaryPictureType type, OH\_AuxiliaryPictureNative \*\*auxiliaryPicture)

**Description**

Creates the pointer to an OH\_AuxiliaryPictureNative object. This API supports only continuous pixel data whose [pixel format](../pixelmap-native-h/document.md#pixel_format) is BGRA\_8888 and creates an auxiliary picture in RGBA\_8888 format.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| uint8\_t \*data | Pointer to the image data. |
| size\_t dataLength | Length of the image data. |
| [Image\_Size](../../structs/image-size/document.md) \*size | Pointer to the size of the auxiliary picture. |
| [Image\_AuxiliaryPictureType](#image_auxiliarypicturetype) type | Type of the auxiliary picture. |
| [OH\_AuxiliaryPictureNative](../../structs/oh-auxiliarypicturenative/document.md) \*\*auxiliaryPicture | Double pointer to the OH\_AuxiliaryPictureNative object created. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_AuxiliaryPictureNative\_WritePixels()

Image\_ErrorCode OH\_AuxiliaryPictureNative\_WritePixels(OH\_AuxiliaryPictureNative \*auxiliaryPicture, uint8\_t \*source,size\_t bufferSize)

**Description**

Reads pixels in the buffer and writes the result to an auxiliary picture.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AuxiliaryPictureNative](../../structs/oh-auxiliarypicturenative/document.md) \*auxiliaryPicture | Pointer to an OH\_AuxiliaryPictureNative object. |
| uint8\_t \*source | Pixels to be written. |
| size\_t bufferSize | Buffer size. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

**IMAGE\_ALLOC\_FAILED**: memory allocation failure.

**IMAGE\_COPY\_FAILED**: memory copy failure.

 |

#### \[h2\]OH\_AuxiliaryPictureNative\_ReadPixels()

Image\_ErrorCode OH\_AuxiliaryPictureNative\_ReadPixels(OH\_AuxiliaryPictureNative \*auxiliaryPicture, uint8\_t \*destination,size\_t \*bufferSize)

**Description**

Reads pixels of an auxiliary picture and writes the result to the buffer.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AuxiliaryPictureNative](../../structs/oh-auxiliarypicturenative/document.md) \*auxiliaryPicture | Pointer to an OH\_AuxiliaryPictureNative object. |
| uint8\_t \*destination | Pointer to the buffer to which the pixels of the auxiliary data will be written. |
| size\_t \*bufferSize | Pointer to the buffer size. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

**IMAGE\_ALLOC\_FAILED**: memory allocation failure.

**IMAGE\_COPY\_FAILED**: memory copy failure.

 |

#### \[h2\]OH\_AuxiliaryPictureNative\_GetType()

Image\_ErrorCode OH\_AuxiliaryPictureNative\_GetType(OH\_AuxiliaryPictureNative \*auxiliaryPicture,Image\_AuxiliaryPictureType \*type)

**Description**

Obtains the type of an auxiliary picture.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AuxiliaryPictureNative](../../structs/oh-auxiliarypicturenative/document.md) \*auxiliaryPicture | Pointer to an OH\_AuxiliaryPictureNative object. |
| [Image\_AuxiliaryPictureType](#image_auxiliarypicturetype) \*type | Pointer to the auxiliary picture type. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_AuxiliaryPictureNative\_GetInfo()

Image\_ErrorCode OH\_AuxiliaryPictureNative\_GetInfo(OH\_AuxiliaryPictureNative \*auxiliaryPicture,OH\_AuxiliaryPictureInfo \*\*info)

**Description**

Obtains the information of an auxiliary picture.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AuxiliaryPictureNative](../../structs/oh-auxiliarypicturenative/document.md) \*auxiliaryPicture | Pointer to an OH\_AuxiliaryPictureNative object. |
| [OH\_AuxiliaryPictureInfo](../../structs/oh-auxiliarypictureinfo/document.md) \*\*info | Double pointer to the auxiliary picture information. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_AuxiliaryPictureNative\_SetInfo()

Image\_ErrorCode OH\_AuxiliaryPictureNative\_SetInfo(OH\_AuxiliaryPictureNative \*auxiliaryPicture,OH\_AuxiliaryPictureInfo \*info)

**Description**

Sets the information for an auxiliary picture.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AuxiliaryPictureNative](../../structs/oh-auxiliarypicturenative/document.md) \*auxiliaryPicture | Pointer to an OH\_AuxiliaryPictureNative object. |
| [OH\_AuxiliaryPictureInfo](../../structs/oh-auxiliarypictureinfo/document.md) \*info | Pointer to the auxiliary picture information. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_AuxiliaryPictureNative\_GetMetadata()

Image\_ErrorCode OH\_AuxiliaryPictureNative\_GetMetadata(OH\_AuxiliaryPictureNative \*auxiliaryPicture,Image\_MetadataType metadataType, OH\_PictureMetadata \*\*metadata)

**Description**

Obtains the metadata of an auxiliary picture.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AuxiliaryPictureNative](../../structs/oh-auxiliarypicturenative/document.md) \*auxiliaryPicture | Pointer to an OH\_AuxiliaryPictureNative object. |
| [Image\_MetadataType](../image-common-h/document.md#image_metadatatype) metadataType | Metadata type. |
| [OH\_PictureMetadata](../../structs/oh-picturemetadata/document.md) \*\*metadata | Double pointer to the metadata. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

**IMAGE\_UNSUPPORTED\_METADATA**: unsupported metadata type, or mismatch between the metadata type and the auxiliary picture type.

 |

#### \[h2\]OH\_AuxiliaryPictureNative\_SetMetadata()

Image\_ErrorCode OH\_AuxiliaryPictureNative\_SetMetadata(OH\_AuxiliaryPictureNative \*auxiliaryPicture,Image\_MetadataType metadataType, OH\_PictureMetadata \*metadata)

**Description**

Sets the metadata for an auxiliary picture.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AuxiliaryPictureNative](../../structs/oh-auxiliarypicturenative/document.md) \*auxiliaryPicture | Pointer to an OH\_AuxiliaryPictureNative object. |
| [Image\_MetadataType](../image-common-h/document.md#image_metadatatype) metadataType | Metadata type. |
| [OH\_PictureMetadata](../../structs/oh-picturemetadata/document.md) \*metadata | Pointer to the metadata. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

**IMAGE\_UNSUPPORTED\_METADATA**: unsupported metadata type, or mismatch between the metadata type and the auxiliary picture type.

 |

#### \[h2\]OH\_AuxiliaryPictureNative\_Release()

Image\_ErrorCode OH\_AuxiliaryPictureNative\_Release(OH\_AuxiliaryPictureNative \*picture)

**Description**

Releases the pointer to an OH\_AuxiliaryPictureNative object.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AuxiliaryPictureNative](../../structs/oh-auxiliarypicturenative/document.md) \*picture | Pointer to an OH\_AuxiliaryPictureNative object. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_AuxiliaryPictureInfo\_Create()

Image\_ErrorCode OH\_AuxiliaryPictureInfo\_Create(OH\_AuxiliaryPictureInfo \*\*info)

**Description**

Creates an OH\_AuxiliaryPictureInfo object.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AuxiliaryPictureInfo](../../structs/oh-auxiliarypictureinfo/document.md) \*\*info | Double pointer to OH\_AuxiliaryPictureInfo. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_AuxiliaryPictureInfo\_GetType()

Image\_ErrorCode OH\_AuxiliaryPictureInfo\_GetType(OH\_AuxiliaryPictureInfo \*info, Image\_AuxiliaryPictureType \*type)

**Description**

Obtains the auxiliary picture type in OH\_AuxiliaryPictureInfo.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AuxiliaryPictureInfo](../../structs/oh-auxiliarypictureinfo/document.md) \*info | Pointer to OH\_AuxiliaryPictureInfo. |
| [Image\_AuxiliaryPictureType](#image_auxiliarypicturetype) \*type | Pointer to the type of the auxiliary picture. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_AuxiliaryPictureInfo\_SetType()

Image\_ErrorCode OH\_AuxiliaryPictureInfo\_SetType(OH\_AuxiliaryPictureInfo \*info, Image\_AuxiliaryPictureType type)

**Description**

Sets the auxiliary picture type in OH\_AuxiliaryPictureInfo.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AuxiliaryPictureInfo](../../structs/oh-auxiliarypictureinfo/document.md) \*info | Pointer to OH\_AuxiliaryPictureInfo. |
| [Image\_AuxiliaryPictureType](#image_auxiliarypicturetype) type | Type of the auxiliary picture. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_AuxiliaryPictureInfo\_GetSize()

Image\_ErrorCode OH\_AuxiliaryPictureInfo\_GetSize(OH\_AuxiliaryPictureInfo \*info, Image\_Size \*size)

**Description**

Obtains the image size in OH\_AuxiliaryPictureInfo.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AuxiliaryPictureInfo](../../structs/oh-auxiliarypictureinfo/document.md) \*info | Pointer to OH\_AuxiliaryPictureInfo. |
| [Image\_Size](../../structs/image-size/document.md) \*size | Pointer to the size. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_AuxiliaryPictureInfo\_SetSize()

Image\_ErrorCode OH\_AuxiliaryPictureInfo\_SetSize(OH\_AuxiliaryPictureInfo \*info, Image\_Size \*size)

**Description**

Sets the image size in OH\_AuxiliaryPictureInfo.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AuxiliaryPictureInfo](../../structs/oh-auxiliarypictureinfo/document.md) \*info | Pointer to OH\_AuxiliaryPictureInfo. |
| [Image\_Size](../../structs/image-size/document.md) \*size | Pointer to the size. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_AuxiliaryPictureInfo\_GetRowStride()

Image\_ErrorCode OH\_AuxiliaryPictureInfo\_GetRowStride(OH\_AuxiliaryPictureInfo \*info, uint32\_t \*rowStride)

**Description**

Obtains the row stride in OH\_AuxiliaryPictureInfo.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AuxiliaryPictureInfo](../../structs/oh-auxiliarypictureinfo/document.md) \*info | Pointer to OH\_AuxiliaryPictureInfo. |
| uint32\_t \*rowStride | Pointer to the row stride, which is the number of bytes from one row of pixels in memory to the next row of pixels in memory. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_AuxiliaryPictureInfo\_SetRowStride()

Image\_ErrorCode OH\_AuxiliaryPictureInfo\_SetRowStride(OH\_AuxiliaryPictureInfo \*info, uint32\_t rowStride)

**Description**

Sets the row stride in OH\_AuxiliaryPictureInfo.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AuxiliaryPictureInfo](../../structs/oh-auxiliarypictureinfo/document.md) \*info | Pointer to OH\_AuxiliaryPictureInfo. |
| uint32\_t rowStride | Row stride, which is the number of bytes from one row of pixels in memory to the next row of pixels in memory. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_AuxiliaryPictureInfo\_GetPixelFormat()

Image\_ErrorCode OH\_AuxiliaryPictureInfo\_GetPixelFormat(OH\_AuxiliaryPictureInfo \*info, PIXEL\_FORMAT \*pixelFormat)

**Description**

Obtains the pixel format in OH\_AuxiliaryPictureInfo.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AuxiliaryPictureInfo](../../structs/oh-auxiliarypictureinfo/document.md) \*info | Pointer to OH\_AuxiliaryPictureInfo. |
| [PIXEL\_FORMAT](../pixelmap-native-h/document.md#pixel_format) \*pixelFormat | Pointer to the pixel format obtained. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_AuxiliaryPictureInfo\_SetPixelFormat()

Image\_ErrorCode OH\_AuxiliaryPictureInfo\_SetPixelFormat(OH\_AuxiliaryPictureInfo \*info, PIXEL\_FORMAT pixelFormat)

**Description**

Sets the pixel format in OH\_AuxiliaryPictureInfo.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AuxiliaryPictureInfo](../../structs/oh-auxiliarypictureinfo/document.md) \*info | Pointer to OH\_AuxiliaryPictureInfo. |
| [PIXEL\_FORMAT](../pixelmap-native-h/document.md#pixel_format) pixelFormat | Pixel format. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_AuxiliaryPictureInfo\_Release()

Image\_ErrorCode OH\_AuxiliaryPictureInfo\_Release(OH\_AuxiliaryPictureInfo \*info)

**Description**

Releases the pointer to an OH\_AuxiliaryPictureInfo object.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AuxiliaryPictureInfo](../../structs/oh-auxiliarypictureinfo/document.md) \*info | Pointer to OH\_AuxiliaryPictureInfo. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |
