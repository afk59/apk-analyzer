# pixelmap\_native.h

#### Overview

The file declares the APIs for accessing a PixelMap.

**File to include**: <multimedia/image\_framework/image/pixelmap\_native.h>

**Library**: libpixelmap.so

**System capability**: SystemCapability.Multimedia.Image.Core

**Since**: 12

**Related module**: [Image\_NativeModule](../../modules/image-nativemodule/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_Pixelmap\_HdrStaticMetadata](../../structs/oh-pixelmap-hdrstaticmetadata/document.md) | OH\_Pixelmap\_HdrStaticMetadata | Describes the static metadata values available for the key **HDR\_STATIC\_METADATA**. |
| [OH\_Pixelmap\_HdrDynamicMetadata](../../structs/oh-pixelmap-hdrdynamicmetadata/document.md) | OH\_Pixelmap\_HdrDynamicMetadata | Describes the dynamic metadata values available for the key **HDR\_DYNAMIC\_METADATA**. |
| [OH\_Pixelmap\_HdrGainmapMetadata](../../structs/oh-pixelmap-hdrgainmapmetadata/document.md) | OH\_Pixelmap\_HdrGainmapMetadata | Describes the gain map metadata values available for the key **HDR\_GAINMAP\_METADATA**. For details, see ISO 21496-1. |
| [OH\_Pixelmap\_HdrMetadataValue](../../structs/oh-pixelmap-hdrmetadatavalue/document.md) | OH\_Pixelmap\_HdrMetadataValue | Describes the HDR metadata values used by the PixelMap and available for the key **OH\_Pixelmap\_HdrMetadataKey**. It is used in [OH\_PixelmapNative\_SetMetadata](#oh_pixelmapnative_setmetadata) and [OH\_PixelmapNative\_GetMetadata](#oh_pixelmapnative_getmetadata). |
| [OH\_PixelmapNative](../../structs/oh-pixelmapnative/document.md) | \- | 
Describes an uncompressed PixelMap format, which is encapsulated at the native layer after images are decoded.

To create an OH\_PixelmapNative object, call [OH\_PixelmapNative\_CreatePixelmap](#oh_pixelmapnative_createpixelmap). By default, BGRA\_8888 is used for data processing.

To release an OH\_PixelmapNative object, call [OH\_PixelmapNative\_Release](#oh_pixelmapnative_release).

 |
| [OH\_NativeBuffer](../../structs/oh-nativebuffer/document.md) | \- | Describes the native buffer, which is used to perform operations related to the native buffer. |
| [OH\_NativeColorSpaceManager](../../structs/oh-nativecolorspacemanager/document.md) | OH\_NativeColorSpaceManager | Describes the native color space manager, which is used to perform operations related to the native color space manager. |
| [OH\_Pixelmap\_InitializationOptions](../../structs/oh-pixelmap-initializationoptions/document.md) | \- | 

Describes the initialization options encapsulated at the native layer. The struct is used to set the initialization parameters for a PixelMap.

To create an OH\_Pixelmap\_InitializationOptions object, call [OH\_PixelmapInitializationOptions\_Create](#oh_pixelmapinitializationoptions_create).

To release an OH\_Pixelmap\_InitializationOptions object, call [OH\_PixelmapInitializationOptions\_Release](#oh_pixelmapinitializationoptions_release).

 |
| [OH\_Pixelmap\_ImageInfo](../../structs/oh-pixelmap-imageinfo/document.md) | \- | Describes the image information. |

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [PIXELMAP\_ALPHA\_TYPE](#pixelmap_alpha_type) | PIXELMAP\_ALPHA\_TYPE | Enumerates the alpha types of a PixelMap. |
| [PIXEL\_FORMAT](#pixel_format) | PIXEL\_FORMAT | Enumerates the image pixel formats. |
| [OH\_PixelmapNative\_AntiAliasingLevel](#oh_pixelmapnative_antialiasinglevel) | OH\_PixelmapNative\_AntiAliasingLevel | Enumerates the anti-aliasing levels used for scaling PixelMaps. |
| [OH\_Pixelmap\_HdrMetadataKey](#oh_pixelmap_hdrmetadatakey) | OH\_Pixelmap\_HdrMetadataKey | Enumerates the keys of the HDR related metadata information used by the PixelMap. It is used in [OH\_PixelmapNative\_SetMetadata](#oh_pixelmapnative_setmetadata) and [OH\_PixelmapNative\_GetMetadata](#oh_pixelmapnative_getmetadata). |
| [OH\_Pixelmap\_HdrMetadataType](#oh_pixelmap_hdrmetadatatype) | OH\_Pixelmap\_HdrMetadataType | Enumerates the HDR metadata types, which are the values of **HDR\_METADATA\_TYPE**. |

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [Image\_ErrorCode OH\_PixelmapInitializationOptions\_Create(OH\_Pixelmap\_InitializationOptions \*\*options)](#oh_pixelmapinitializationoptions_create) | Creates the pointer to an OH\_Pixelmap\_InitializationOptions struct. |
| [Image\_ErrorCode OH\_PixelmapInitializationOptions\_GetWidth(OH\_Pixelmap\_InitializationOptions \*options, uint32\_t \*width)](#oh_pixelmapinitializationoptions_getwidth) | Obtains the image width. |
| [Image\_ErrorCode OH\_PixelmapInitializationOptions\_SetWidth(OH\_Pixelmap\_InitializationOptions \*options, uint32\_t width)](#oh_pixelmapinitializationoptions_setwidth) | Sets the image width. |
| [Image\_ErrorCode OH\_PixelmapInitializationOptions\_GetHeight(OH\_Pixelmap\_InitializationOptions \*options, uint32\_t \*height)](#oh_pixelmapinitializationoptions_getheight) | Obtains the image height. |
| [Image\_ErrorCode OH\_PixelmapInitializationOptions\_SetHeight(OH\_Pixelmap\_InitializationOptions \*options, uint32\_t height)](#oh_pixelmapinitializationoptions_setheight) | Sets the image height. |
| [Image\_ErrorCode OH\_PixelmapInitializationOptions\_GetPixelFormat(OH\_Pixelmap\_InitializationOptions \*options, int32\_t \*pixelFormat)](#oh_pixelmapinitializationoptions_getpixelformat) | Obtains the pixel format. |
| [Image\_ErrorCode OH\_PixelmapInitializationOptions\_SetPixelFormat(OH\_Pixelmap\_InitializationOptions \*options, int32\_t pixelFormat)](#oh_pixelmapinitializationoptions_setpixelformat) | Sets the pixel format. |
| [Image\_ErrorCode OH\_PixelmapInitializationOptions\_GetSrcPixelFormat(OH\_Pixelmap\_InitializationOptions \*options, int32\_t \*srcpixelFormat)](#oh_pixelmapinitializationoptions_getsrcpixelformat) | Obtains the source pixel format. |
| [Image\_ErrorCode OH\_PixelmapInitializationOptions\_SetSrcPixelFormat(OH\_Pixelmap\_InitializationOptions \*options, int32\_t srcpixelFormat)](#oh_pixelmapinitializationoptions_setsrcpixelformat) | Sets the source pixel format. |
| [Image\_ErrorCode OH\_PixelmapInitializationOptions\_GetRowStride(OH\_Pixelmap\_InitializationOptions \*options, int32\_t \*rowStride)](#oh_pixelmapinitializationoptions_getrowstride) | 
Obtains the row stride.

The stride is the actual memory size occupied by each row of the image, in bytes. Stride = Width \*Number of bytes per pixel + Padding, where padding refers to the extra space added at the end of each row for memory alignment purposes.

 |
| [Image\_ErrorCode OH\_PixelmapInitializationOptions\_SetRowStride(OH\_Pixelmap\_InitializationOptions \*options, int32\_t rowStride)](#oh_pixelmapinitializationoptions_setrowstride) | 

Sets the row stride.

The stride is the actual memory size occupied by each row of the image, in bytes. Stride = Width \*Number of bytes per pixel + Padding, where padding refers to the extra space added at the end of each row for memory alignment purposes.

 |
| [Image\_ErrorCode OH\_PixelmapInitializationOptions\_GetAlphaType(OH\_Pixelmap\_InitializationOptions \*options, int32\_t \*alphaType)](#oh_pixelmapinitializationoptions_getalphatype) | Obtains the alpha type. |
| [Image\_ErrorCode OH\_PixelmapInitializationOptions\_SetAlphaType(OH\_Pixelmap\_InitializationOptions \*options, int32\_t alphaType)](#oh_pixelmapinitializationoptions_setalphatype) | Sets the alpha type. |
| [Image\_ErrorCode OH\_PixelmapInitializationOptions\_GetEditable(OH\_Pixelmap\_InitializationOptions \*options, bool \*editable)](#oh_pixelmapinitializationoptions_geteditable) | Obtains the editable flag. |
| [Image\_ErrorCode OH\_PixelmapInitializationOptions\_SetEditable(OH\_Pixelmap\_InitializationOptions \*options, bool editable)](#oh_pixelmapinitializationoptions_seteditable) | Sets the editable flag. |
| [Image\_ErrorCode OH\_PixelmapInitializationOptions\_Release(OH\_Pixelmap\_InitializationOptions \*options)](#oh_pixelmapinitializationoptions_release) | Releases the pointer to an OH\_Pixelmap\_InitializationOptions struct. |
| [Image\_ErrorCode OH\_PixelmapImageInfo\_Create(OH\_Pixelmap\_ImageInfo \*\*info)](#oh_pixelmapimageinfo_create) | Creates the pointer to an OH\_Pixelmap\_ImageInfo struct. |
| [Image\_ErrorCode OH\_PixelmapImageInfo\_GetWidth(OH\_Pixelmap\_ImageInfo \*info, uint32\_t \*width)](#oh_pixelmapimageinfo_getwidth) | Obtains the image width. |
| [Image\_ErrorCode OH\_PixelmapImageInfo\_GetHeight(OH\_Pixelmap\_ImageInfo \*info, uint32\_t \*height)](#oh_pixelmapimageinfo_getheight) | Obtains the image height. |
| [Image\_ErrorCode OH\_PixelmapImageInfo\_GetAlphaMode(OH\_Pixelmap\_ImageInfo \*info, int32\_t \*AlphaMode)](#oh_pixelmapimageinfo_getalphamode) | Obtains the alpha type of an image. |
| [Image\_ErrorCode OH\_PixelmapImageInfo\_GetRowStride(OH\_Pixelmap\_ImageInfo \*info, uint32\_t \*rowStride)](#oh_pixelmapimageinfo_getrowstride) | Obtains the row stride. |
| [Image\_ErrorCode OH\_PixelmapImageInfo\_GetPixelFormat(OH\_Pixelmap\_ImageInfo \*info, int32\_t \*pixelFormat)](#oh_pixelmapimageinfo_getpixelformat) | Obtains the pixel format. |
| [Image\_ErrorCode OH\_PixelmapImageInfo\_GetAlphaType(OH\_Pixelmap\_ImageInfo \*info, int32\_t \*alphaType)](#oh_pixelmapimageinfo_getalphatype) | Obtains the default alpha type from OH\_PixelmapImageInfo. To obtain the current alpha type of the image, call [OH\_PixelmapImageInfo\_GetAlphaMode](#oh_pixelmapimageinfo_getalphamode). |
| [Image\_ErrorCode OH\_PixelmapImageInfo\_GetDynamicRange(OH\_Pixelmap\_ImageInfo \*info, bool \*isHdr)](#oh_pixelmapimageinfo_getdynamicrange) | Obtains the dynamic range of a PixelMap. |
| [Image\_ErrorCode OH\_PixelmapImageInfo\_Release(OH\_Pixelmap\_ImageInfo \*info)](#oh_pixelmapimageinfo_release) | Releases the pointer to an OH\_Pixelmap\_ImageInfo struct. |
| [Image\_ErrorCode OH\_PixelmapNative\_CreatePixelmap(uint8\_t \*data, size\_t dataLength, OH\_Pixelmap\_InitializationOptions \*options, OH\_PixelmapNative \*\*pixelmap)](#oh_pixelmapnative_createpixelmap) | Creates a PixelMap based on properties. By default, the BGRA\_8888 format is used for data processing. For details about other formats, see [OH\_PixelmapInitializationOptions\_SetSrcPixelFormat](#oh_pixelmapinitializationoptions_setsrcpixelformat). |
| [Image\_ErrorCode OH\_PixelmapNative\_CreatePixelmapUsingAllocator(uint8\_t \*data, size\_t dataLength, OH\_Pixelmap\_InitializationOptions \*options, IMAGE\_ALLOCATOR\_MODE allocator, OH\_PixelmapNative \*\*pixelmap)](#oh_pixelmapnative_createpixelmapusingallocator) | Creates a PixelMap object based on the options and memory type, where **allocator** specifies the memory type of the PixelMap. By default, the system selects an appropriate memory type based on the image type, image size, and platform capability. When processing the returned PixelMap object, consider the impact of stride. |
| [Image\_ErrorCode OH\_PixelmapNative\_ConvertPixelmapNativeToNapi(napi\_env env, OH\_PixelmapNative \*pixelmapNative, napi\_value \*pixelmapNapi)](#oh_pixelmapnative_convertpixelmapnativetonapi) | Converts a nativePixelMap object to a PixelMapnapi object. |
| [Image\_ErrorCode OH\_PixelmapNative\_ConvertPixelmapNativeFromNapi(napi\_env env, napi\_value pixelmapNapi, OH\_PixelmapNative \*\*pixelmapNative)](#oh_pixelmapnative_convertpixelmapnativefromnapi) | Converts a PixelMapnapi object to a nativePixelMap object. |
| [Image\_ErrorCode OH\_PixelmapNative\_ReadPixels(OH\_PixelmapNative \*pixelmap, uint8\_t \*destination, size\_t \*bufferSize)](#oh_pixelmapnative_readpixels) | Reads the pixels of a PixelMap and writes the result to the buffer based on the pixel format of the PixelMap. |
| [Image\_ErrorCode OH\_PixelmapNative\_WritePixels(OH\_PixelmapNative \*pixelmap, uint8\_t \*source, size\_t bufferSize)](#oh_pixelmapnative_writepixels) | Reads the pixels in the buffer and writes the result to the PixelMap based on the pixel format of the PixelMap. |
| [Image\_ErrorCode OH\_PixelmapNative\_ReadPixelsFromArea(OH\_PixelmapNative \*pixelmap, Image\_PositionArea \*area)](#oh_pixelmapnative_readpixelsfromarea) | Reads pixels from the specified area in a PixelMap and stores the result to the buffer. The read data is in BGRA\_8888 format. |
| [Image\_ErrorCode OH\_PixelmapNative\_WritePixelsToArea(OH\_PixelmapNative \*pixelmap, Image\_PositionArea \*area)](#oh_pixelmapnative_writepixelstoarea) | Writes pixels in the buffer to the specified area in a PixelMap. The data source must be in BGRA\_8888 format. |
| [Image\_ErrorCode OH\_PixelmapNative\_GetArgbPixels(OH\_PixelmapNative \*pixelmap, uint8\_t \*destination, size\_t \*bufferSize)](#oh_pixelmapnative_getargbpixels) | Reads data in ARGB format from a PixelMap. |
| [Image\_ErrorCode OH\_PixelmapNative\_ToSdr(OH\_PixelmapNative \*pixelmap)](#oh_pixelmapnative_tosdr) | Converts a PixelMap from the HDR format to the SDR format. |
| [Image\_ErrorCode OH\_PixelmapNative\_GetImageInfo(OH\_PixelmapNative \*pixelmap, OH\_Pixelmap\_ImageInfo \*imageInfo)](#oh_pixelmapnative_getimageinfo) | Obtains the image information of a PixelMap. |
| [Image\_ErrorCode OH\_PixelmapNative\_Opacity(OH\_PixelmapNative \*pixelmap, float rate)](#oh_pixelmapnative_opacity) | Sets the opacity rate to enable the PixelMap to achieve the corresponding opacity effect. |
| [Image\_ErrorCode OH\_PixelmapNative\_Scale(OH\_PixelmapNative \*pixelmap, float scaleX, float scaleY)](#oh_pixelmapnative_scale) | Scales a PixelMap based on a given width and height. |
| [Image\_ErrorCode OH\_PixelmapNative\_ScaleWithAntiAliasing(OH\_PixelmapNative \*pixelmap, float scaleX, float scaleY, OH\_PixelmapNative\_AntiAliasingLevel level)](#oh_pixelmapnative_scalewithantialiasing) | Scales a PixelMap based on the specified anti-aliasing level, width, and height. |
| [Image\_ErrorCode OH\_PixelmapNative\_CreateScaledPixelMap(OH\_PixelmapNative \*srcPixelmap, OH\_PixelmapNative \*\*dstPixelmap, float scaleX, float scaleY)](#oh_pixelmapnative_createscaledpixelmap) | Creates a PixelMap that has been resized based on the specified scale factors of the width and height. |
| [Image\_ErrorCode OH\_PixelmapNative\_CreateScaledPixelMapWithAntiAliasing(OH\_PixelmapNative \*srcPixelmap, OH\_PixelmapNative \*\*dstPixelmap, float scaleX, float scaleY, OH\_PixelmapNative\_AntiAliasingLevel level)](#oh_pixelmapnative_createscaledpixelmapwithantialiasing) | Creates a PixelMap that has been resized based on the specified anti-aliasing level and the scale factors of the width and height. |
| [Image\_ErrorCode OH\_PixelmapNative\_CreateAlphaPixelmap(OH\_PixelmapNative \*srcPixelmap, OH\_PixelmapNative \*\*dstPixelmap)](#oh_pixelmapnative_createalphapixelmap) | Creates a PixelMap that contains only the alpha channel from the source PixelMap. |
| [Image\_ErrorCode OH\_PixelmapNative\_Clone(OH\_PixelmapNative \*srcPixelmap, OH\_PixelmapNative \*\*dstPixelmap)](#oh_pixelmapnative_clone) | Clones a new PixelMap from the source PixelMap. |
| [Image\_ErrorCode OH\_PixelmapNative\_CreateCroppedAndScaledPixelMap(OH\_PixelmapNative \*srcPixelmap, Image\_Region \*region, Image\_Scale \*scale, OH\_PixelmapNative\_AntiAliasingLevel level, OH\_PixelmapNative \*\*dstPixelmap)](#oh_pixelmapnative_createcroppedandscaledpixelmap) | Creates a PixelMap that is cropped and resized based on the source PixelMap. |
| [Image\_ErrorCode OH\_PixelmapNative\_Translate(OH\_PixelmapNative \*pixelmap, float x, float y)](#oh_pixelmapnative_translate) | Translates a PixelMap based on given coordinates. |
| [Image\_ErrorCode OH\_PixelmapNative\_Rotate(OH\_PixelmapNative \*pixelmap, float angle)](#oh_pixelmapnative_rotate) | Rotates a PixelMap based on a given angle. |
| [Image\_ErrorCode OH\_PixelmapNative\_Flip(OH\_PixelmapNative \*pixelmap, bool shouldFlipHorizontally, bool shouldFlipVertically)](#oh_pixelmapnative_flip) | Flips a PixelMap based on a given angle. |
| [Image\_ErrorCode OH\_PixelmapNative\_Crop(OH\_PixelmapNative \*pixelmap, Image\_Region \*region)](#oh_pixelmapnative_crop) | Crops a PixelMap based on a given size. |
| [Image\_ErrorCode OH\_PixelmapNative\_Release(OH\_PixelmapNative \*pixelmap)](#oh_pixelmapnative_release) | Releases the pointer to an OH\_PixelmapNative object. [OH\_PixelmapNative\_Destroy](#oh_pixelmapnative_destroy) is recommended. |
| [Image\_ErrorCode OH\_PixelmapNative\_Destroy(OH\_PixelmapNative \*\*pixelmap)](#oh_pixelmapnative_destroy) | Releases the pointer to an OH\_PixelmapNative object. |
| [Image\_ErrorCode OH\_PixelmapNative\_ConvertAlphaFormat(OH\_PixelmapNative\* srcpixelmap, OH\_PixelmapNative\* dstpixelmap, const bool isPremul)](#oh_pixelmapnative_convertalphaformat) | Converts pixel data of a PixelMap from premultiplied alpha to non-premultiplied alpha, or vice versa. |
| [Image\_ErrorCode OH\_PixelmapNative\_CreateEmptyPixelmap(OH\_Pixelmap\_InitializationOptions \*options, OH\_PixelmapNative \*\*pixelmap)](#oh_pixelmapnative_createemptypixelmap) | Creates an empty PixelMap object based on **OH\_Pixelmap\_InitializationOptions**. The memory data is 0. |
| [Image\_ErrorCode OH\_PixelmapNative\_CreateEmptyPixelmapUsingAllocator(OH\_Pixelmap\_InitializationOptions \*options, IMAGE\_ALLOCATOR\_MODE allocator, OH\_PixelmapNative \*\*pixelmap)](#oh_pixelmapnative_createemptypixelmapusingallocator) | Creates an empty PixelMap object based on the options and memory type, where **allocator** specifies the memory type of the PixelMap. By default, the system selects an appropriate memory type based on the image type, image size, and platform capability. When processing the returned PixelMap object, consider the impact of stride. |
| [Image\_ErrorCode OH\_PixelmapNative\_CreatePixelmapFromSurface(const char \*surfaceId, size\_t length, OH\_PixelmapNative \*\*pixelmap)](#oh_pixelmapnative_createpixelmapfromsurface) | Creates a PixelMap from a surface with the specified surface ID. |
| [Image\_ErrorCode OH\_PixelmapNative\_CreatePixelmapFromNativeBuffer(OH\_NativeBuffer \*nativeBuffer, OH\_PixelmapNative \*\*pixelmap)](#oh_pixelmapnative_createpixelmapfromnativebuffer) | 

Creates a PixelMap using a NativeBuffer. If the [CPU access permission](../../../../../graphics/arkgraphics-2d/c-apis/header-files/native-buffer-h/document.md#oh_nativebuffer_usage) is not configured for the NativeBuffer, the PixelMap cannot be created.

The supported pixel formats are RGBA\_8888, NV21, NV12, YCBCR\_P010, and YCRCB\_P010.

 |
| [Image\_ErrorCode OH\_PixelmapNative\_GetNativeBuffer(OH\_PixelmapNative \*pixelmap, OH\_NativeBuffer \*\*nativeBuffer)](#oh_pixelmapnative_getnativebuffer) | Obtains the NativeBuffer object from a PixelMap in the DMA memory. |
| [Image\_ErrorCode OH\_PixelmapNative\_GetMetadata(OH\_PixelmapNative \*pixelmap, OH\_Pixelmap\_HdrMetadataKey key, OH\_Pixelmap\_HdrMetadataValue \*\*value)](#oh_pixelmapnative_getmetadata) | Obtains the metadata. |
| [Image\_ErrorCode OH\_PixelmapNative\_SetMetadata(OH\_PixelmapNative \*pixelmap, OH\_Pixelmap\_HdrMetadataKey key, OH\_Pixelmap\_HdrMetadataValue \*value)](#oh_pixelmapnative_setmetadata) | Sets the metadata. |
| [Image\_ErrorCode OH\_PixelmapNative\_SetColorSpaceNative(OH\_PixelmapNative \*pixelmap, OH\_NativeColorSpaceManager \*colorSpaceNative)](#oh_pixelmapnative_setcolorspacenative) | Sets a NativeColorSpaceManager object. |
| [Image\_ErrorCode OH\_PixelmapNative\_GetColorSpaceNative(OH\_PixelmapNative \*pixelmap, OH\_NativeColorSpaceManager \*\*colorSpaceNative)](#oh_pixelmapnative_getcolorspacenative) | Obtains a NativeColorSpaceManager object. |
| [Image\_ErrorCode OH\_PixelmapNative\_SetMemoryName(OH\_PixelmapNative \*pixelmap, char \*name, size\_t \*size)](#oh_pixelmapnative_setmemoryname) | Sets the memory name of a PixelMap. |
| [Image\_ErrorCode OH\_PixelmapNative\_GetByteCount(OH\_PixelmapNative \*pixelmap, uint32\_t \*byteCount)](#oh_pixelmapnative_getbytecount) | Obtains the total number of bytes occupied by all pixels in a PixelMap, excluding any memory padding. |
| [Image\_ErrorCode OH\_PixelmapNative\_GetAllocationByteCount(OH\_PixelmapNative \*pixelmap, uint32\_t \*allocationByteCount)](#oh_pixelmapnative_getallocationbytecount) | Obtains the number of bytes in the memory allocated by a PixelMap to store pixels. |
| [Image\_ErrorCode OH\_PixelmapNative\_AccessPixels(OH\_PixelmapNative \*pixelmap, void \*\*addr)](#oh_pixelmapnative_accesspixels) | 

Obtains the memory address where the pixels of a PixelMap are stored and locks the memory.

When the memory is locked, any attempts to alter or free the pixel data of the PixelMap will fail or be ineffective.

 |
| [Image\_ErrorCode OH\_PixelmapNative\_UnaccessPixels(OH\_PixelmapNative \*pixelmap)](#oh_pixelmapnative_unaccesspixels) | 

Unlocks the memory allocated to store the pixels of a PixelMap.

This function must be used together with [OH\_PixelmapNative\_AccessPixels](#oh_pixelmapnative_accesspixels).

 |
| [Image\_ErrorCode OH\_PixelmapNative\_GetUniqueId(OH\_PixelmapNative \*pixelmap, uint32\_t \*uniqueId)](#oh_pixelmapnative_getuniqueid) | Obtains the unique ID of a PixelMap. |
| [Image\_ErrorCode OH\_PixelmapNative\_IsReleased(OH\_PixelmapNative \*pixelmap, bool \*released)](#oh_pixelmapnative_isreleased) | Checks whether a PixelMap is released. If released, any attempt to access the internal data of this object will fail. |

#### Enum Description

#### \[h2\]PIXELMAP\_ALPHA\_TYPE

enum PIXELMAP\_ALPHA\_TYPE

**Description**

Enumerates the alpha types of a PixelMap.

**Since**: 12

| Enum Item | Description |
| :-- | :-- |
| PIXELMAP\_ALPHA\_TYPE\_UNKNOWN = 0 | Unknown format. |
| PIXELMAP\_ALPHA\_TYPE\_OPAQUE = 1 | Opaque format. |
| PIXELMAP\_ALPHA\_TYPE\_PREMULTIPLIED = 2 | Premultiplied format. |
| PIXELMAP\_ALPHA\_TYPE\_UNPREMULTIPLIED = 3 | Non-premultiplied format. |

#### \[h2\]PIXEL\_FORMAT

enum PIXEL\_FORMAT

**Description**

Enumerates the image pixel formats.

**Since**: 12

| Enum Item | Description |
| :-- | :-- |
| PIXEL\_FORMAT\_UNKNOWN = 0 | Unknown format. |
| PIXEL\_FORMAT\_RGB\_565 = 2 | RGB\_565 format. |
| PIXEL\_FORMAT\_RGBA\_8888 = 3 | RGBA\_8888 format. |
| PIXEL\_FORMAT\_BGRA\_8888 = 4 | BGRA\_8888 format. |
| PIXEL\_FORMAT\_RGB\_888 = 5 | RGB\_888 format. |
| PIXEL\_FORMAT\_ALPHA\_8 = 6 | ALPHA\_8 format. |
| PIXEL\_FORMAT\_RGBA\_F16 = 7 | RGBA\_F16 format. |
| PIXEL\_FORMAT\_NV21 = 8 | NV21 format. |
| PIXEL\_FORMAT\_NV12 = 9 | NV12 format. |
| PIXEL\_FORMAT\_RGBA\_1010102 = 10 | RGBA\_1010102 format. |
| PIXEL\_FORMAT\_YCBCR\_P010 = 11 | YCBCR\_P010 format. |
| PIXEL\_FORMAT\_YCRCB\_P010 = 12 | YCRCB\_P010 format. |

#### \[h2\]OH\_PixelmapNative\_AntiAliasingLevel

enum OH\_PixelmapNative\_AntiAliasingLevel

**Description**

Enumerates the anti-aliasing levels used for scaling PixelMaps.

**Since**: 12

| Enum Item | Description |
| :-- | :-- |
| OH\_PixelmapNative\_AntiAliasing\_NONE = 0 | Nearest neighbor interpolation. |
| OH\_PixelmapNative\_AntiAliasing\_LOW = 1 | Bilinear interpolation. |
| OH\_PixelmapNative\_AntiAliasing\_MEDIUM = 2 | Bilinear interpolation with mipmap enabled. You are advised to use this value when zooming out an image. |
| OH\_PixelmapNative\_AntiAliasing\_HIGH = 3 | Cubic interpolation. |

#### \[h2\]OH\_Pixelmap\_HdrMetadataKey

enum OH\_Pixelmap\_HdrMetadataKey

**Description**

Enumerates the keys of the HDR related metadata information used by the PixelMap. It is used in [OH\_PixelmapNative\_SetMetadata](#oh_pixelmapnative_setmetadata) and [OH\_PixelmapNative\_GetMetadata](#oh_pixelmapnative_getmetadata).

**Since**: 12

| Enum Item | Description |
| :-- | :-- |
| HDR\_METADATA\_TYPE = 0 | Metadata type used by the PixelMap. |
| HDR\_STATIC\_METADATA = 1 | Static metadata. |
| HDR\_DYNAMIC\_METADATA = 2 | Dynamic metadata. |
| HDR\_GAINMAP\_METADATA = 3 | Metadata used by gain maps. |

#### \[h2\]OH\_Pixelmap\_HdrMetadataType

enum OH\_Pixelmap\_HdrMetadataType

**Description**

Enumerates the HDR metadata types, which are the values of **HDR\_METADATA\_TYPE**.

**Since**: 12

| Enum Item | Description |
| :-- | :-- |
| HDR\_METADATA\_TYPE\_NONE = 0 | No metadata. |
| HDR\_METADATA\_TYPE\_BASE = 1 | Metadata used for base graphics. |
| HDR\_METADATA\_TYPE\_GAINMAP = 2 | Metadata used for gain maps. |
| HDR\_METADATA\_TYPE\_ALTERNATE = 3 | Metadata used for synthesized HDR graphics. |

#### Function Description

#### \[h2\]OH\_PixelmapInitializationOptions\_Create()

Image\_ErrorCode OH\_PixelmapInitializationOptions\_Create(OH\_Pixelmap\_InitializationOptions \*\*options)

**Description**

Creates the pointer to an OH\_Pixelmap\_InitializationOptions struct.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Pixelmap\_InitializationOptions](../../structs/oh-pixelmap-initializationoptions/document.md) \*\*options | Double pointer to the OH\_Pixelmap\_InitializationOptions struct created. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_PixelmapInitializationOptions\_GetWidth()

Image\_ErrorCode OH\_PixelmapInitializationOptions\_GetWidth(OH\_Pixelmap\_InitializationOptions \*options, uint32\_t \*width)

**Description**

Obtains the image width.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Pixelmap\_InitializationOptions](../../structs/oh-pixelmap-initializationoptions/document.md) \*options | Pointer to an OH\_Pixelmap\_InitializationOptions struct. |
| uint32\_t \*width | Pointer to the image width, in px. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_PixelmapInitializationOptions\_SetWidth()

Image\_ErrorCode OH\_PixelmapInitializationOptions\_SetWidth(OH\_Pixelmap\_InitializationOptions \*options, uint32\_t width)

**Description**

Sets the image width.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Pixelmap\_InitializationOptions](../../structs/oh-pixelmap-initializationoptions/document.md) \*options | Pointer to an OH\_Pixelmap\_InitializationOptions struct. |
| uint32\_t width | Image width, in px. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_PixelmapInitializationOptions\_GetHeight()

Image\_ErrorCode OH\_PixelmapInitializationOptions\_GetHeight(OH\_Pixelmap\_InitializationOptions \*options, uint32\_t \*height)

**Description**

Obtains the image height.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Pixelmap\_InitializationOptions](../../structs/oh-pixelmap-initializationoptions/document.md) \*options | Pointer to an OH\_Pixelmap\_InitializationOptions struct. |
| uint32\_t \*height | Pointer to the image height, in px. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_PixelmapInitializationOptions\_SetHeight()

Image\_ErrorCode OH\_PixelmapInitializationOptions\_SetHeight(OH\_Pixelmap\_InitializationOptions \*options, uint32\_t height)

**Description**

Sets the image height.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Pixelmap\_InitializationOptions](../../structs/oh-pixelmap-initializationoptions/document.md) \*options | Pointer to an OH\_Pixelmap\_InitializationOptions struct. |
| uint32\_t height | Image height, in px. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_PixelmapInitializationOptions\_GetPixelFormat()

Image\_ErrorCode OH\_PixelmapInitializationOptions\_GetPixelFormat(OH\_Pixelmap\_InitializationOptions \*options, int32\_t \*pixelFormat)

**Description**

Obtains the pixel format.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Pixelmap\_InitializationOptions](../../structs/oh-pixelmap-initializationoptions/document.md) \*options | Pointer to an OH\_Pixelmap\_InitializationOptions struct. |
| int32\_t \*pixelFormat | Pointer to the pixel format. For details about the available options, see [PIXEL\_FORMAT](#pixel_format). |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_PixelmapInitializationOptions\_SetPixelFormat()

Image\_ErrorCode OH\_PixelmapInitializationOptions\_SetPixelFormat(OH\_Pixelmap\_InitializationOptions \*options, int32\_t pixelFormat)

**Description**

Sets the pixel format.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Pixelmap\_InitializationOptions](../../structs/oh-pixelmap-initializationoptions/document.md) \*options | Pointer to an OH\_Pixelmap\_InitializationOptions struct. |
| int32\_t pixelFormat | Pixel format. For details about the available options, see [PIXEL\_FORMAT](#pixel_format). |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_PixelmapInitializationOptions\_GetSrcPixelFormat()

Image\_ErrorCode OH\_PixelmapInitializationOptions\_GetSrcPixelFormat(OH\_Pixelmap\_InitializationOptions \*options, int32\_t \*srcpixelFormat)

**Description**

Obtains the source pixel format.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Pixelmap\_InitializationOptions](../../structs/oh-pixelmap-initializationoptions/document.md) \*options | Pointer to an OH\_Pixelmap\_InitializationOptions struct. |
| int32\_t \*srcpixelFormat | Pointer to the pixel format. For details about the available options, see [PIXEL\_FORMAT](#pixel_format). |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_PixelmapInitializationOptions\_SetSrcPixelFormat()

Image\_ErrorCode OH\_PixelmapInitializationOptions\_SetSrcPixelFormat(OH\_Pixelmap\_InitializationOptions \*options, int32\_t srcpixelFormat)

**Description**

Sets the source pixel format.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Pixelmap\_InitializationOptions](../../structs/oh-pixelmap-initializationoptions/document.md) \*options | Pointer to an OH\_Pixelmap\_InitializationOptions struct. |
| int32\_t srcpixelFormat | Source pixel format. For details about the available options, see [PIXEL\_FORMAT](#pixel_format). |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_PixelmapInitializationOptions\_GetRowStride()

Image\_ErrorCode OH\_PixelmapInitializationOptions\_GetRowStride(OH\_Pixelmap\_InitializationOptions \*options, int32\_t \*rowStride)

**Description**

Obtains the row stride.

The stride is the actual memory size occupied by each row of the image, in bytes. Stride = Width \*Number of bytes per pixel + Padding, where padding refers to the extra space added at the end of each row for memory alignment purposes.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Pixelmap\_InitializationOptions](../../structs/oh-pixelmap-initializationoptions/document.md) \*options | Pointer to an OH\_Pixelmap\_InitializationOptions struct. |
| int32\_t \*rowStride | Pointer to the stride, in bytes. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

**IMAGE\_UNKNOWN\_ERROR**: The struct that **options** points to is released.

 |

#### \[h2\]OH\_PixelmapInitializationOptions\_SetRowStride()

Image\_ErrorCode OH\_PixelmapInitializationOptions\_SetRowStride(OH\_Pixelmap\_InitializationOptions \*options, int32\_t rowStride)

**Description**

Sets the row stride.

The stride is the actual memory size occupied by each row of the image, in bytes. Stride = Width \*Number of bytes per pixel + Padding, where padding refers to the extra space added at the end of each row for memory alignment purposes.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Pixelmap\_InitializationOptions](../../structs/oh-pixelmap-initializationoptions/document.md) \*options | Pointer to an OH\_Pixelmap\_InitializationOptions struct. |
| int32\_t rowStride | Stride, in bytes. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

**IMAGE\_UNKNOWN\_ERROR**: The struct that **options** points to is released.

 |

#### \[h2\]OH\_PixelmapInitializationOptions\_GetAlphaType()

Image\_ErrorCode OH\_PixelmapInitializationOptions\_GetAlphaType(OH\_Pixelmap\_InitializationOptions \*options, int32\_t \*alphaType)

**Description**

Obtains the alpha type.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Pixelmap\_InitializationOptions](../../structs/oh-pixelmap-initializationoptions/document.md) \*options | Pointer to an OH\_Pixelmap\_InitializationOptions struct. |
| int32\_t \*alphaType | Pointer to the alpha type. For details about the available options, see [PIXELMAP\_ALPHA\_TYPE](#pixelmap_alpha_type). |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_PixelmapInitializationOptions\_SetAlphaType()

Image\_ErrorCode OH\_PixelmapInitializationOptions\_SetAlphaType(OH\_Pixelmap\_InitializationOptions \*options, int32\_t alphaType)

**Description**

Sets the alpha type.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Pixelmap\_InitializationOptions](../../structs/oh-pixelmap-initializationoptions/document.md) \*options | Pointer to an OH\_Pixelmap\_InitializationOptions struct. |
| int32\_t alphaType | Alpha type. For details about the available options, see [PIXELMAP\_ALPHA\_TYPE](#pixelmap_alpha_type). |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_PixelmapInitializationOptions\_GetEditable()

Image\_ErrorCode OH\_PixelmapInitializationOptions\_GetEditable(OH\_Pixelmap\_InitializationOptions \*options, bool \*editable)

**Description**

Obtains the editable flag.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Pixelmap\_InitializationOptions](../../structs/oh-pixelmap-initializationoptions/document.md) \*options | Pointer to an OH\_Pixelmap\_InitializationOptions struct. |
| bool \*editable | Pointer to the editable flag. **true** if editable, **false** otherwise. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_PixelmapInitializationOptions\_SetEditable()

Image\_ErrorCode OH\_PixelmapInitializationOptions\_SetEditable(OH\_Pixelmap\_InitializationOptions \*options, bool editable)

**Description**

Sets the editable flag.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Pixelmap\_InitializationOptions](../../structs/oh-pixelmap-initializationoptions/document.md) \*options | Pointer to an OH\_Pixelmap\_InitializationOptions struct. |
| bool editable | Editable flag. **true** if editable, **false** otherwise. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_PixelmapInitializationOptions\_Release()

Image\_ErrorCode OH\_PixelmapInitializationOptions\_Release(OH\_Pixelmap\_InitializationOptions \*options)

**Description**

Releases the pointer to an OH\_Pixelmap\_InitializationOptions struct.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Pixelmap\_InitializationOptions](../../structs/oh-pixelmap-initializationoptions/document.md) \*options | Pointer to an OH\_Pixelmap\_InitializationOptions struct. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_PixelmapImageInfo\_Create()

Image\_ErrorCode OH\_PixelmapImageInfo\_Create(OH\_Pixelmap\_ImageInfo \*\*info)

**Description**

Creates the pointer to an OH\_Pixelmap\_ImageInfo struct.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Pixelmap\_ImageInfo](../../structs/oh-pixelmap-imageinfo/document.md) \*\*info | Double pointer to the OH\_Pixelmap\_ImageInfo struct created. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_PixelmapImageInfo\_GetWidth()

Image\_ErrorCode OH\_PixelmapImageInfo\_GetWidth(OH\_Pixelmap\_ImageInfo \*info, uint32\_t \*width)

**Description**

Obtains the image width.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Pixelmap\_ImageInfo](../../structs/oh-pixelmap-imageinfo/document.md) \*info | Pointer to an OH\_Pixelmap\_ImageInfo struct. |
| uint32\_t \*width | Pointer to the image width, in px. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_PixelmapImageInfo\_GetHeight()

Image\_ErrorCode OH\_PixelmapImageInfo\_GetHeight(OH\_Pixelmap\_ImageInfo \*info, uint32\_t \*height)

**Description**

Obtains the image height.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Pixelmap\_ImageInfo](../../structs/oh-pixelmap-imageinfo/document.md) \*info | Pointer to an OH\_Pixelmap\_ImageInfo struct. |
| uint32\_t \*height | Pointer to the image height, in px. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_PixelmapImageInfo\_GetAlphaMode()

Image\_ErrorCode OH\_PixelmapImageInfo\_GetAlphaMode(OH\_Pixelmap\_ImageInfo \*info, int32\_t \*AlphaMode)

**Description**

Obtains the alpha type of an image.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Pixelmap\_ImageInfo](../../structs/oh-pixelmap-imageinfo/document.md) \*info | Pointer to an OH\_Pixelmap\_ImageInfo struct. |
| int32\_t \*AlphaMode | Pointer to the alpha format. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_PixelmapImageInfo\_GetRowStride()

Image\_ErrorCode OH\_PixelmapImageInfo\_GetRowStride(OH\_Pixelmap\_ImageInfo \*info, uint32\_t \*rowStride)

**Description**

Obtains the row stride.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Pixelmap\_ImageInfo](../../structs/oh-pixelmap-imageinfo/document.md) \*info | Pointer to an OH\_Pixelmap\_ImageInfo struct. |
| uint32\_t \*rowStride | Pointer to the row stride, which is the number of bytes from one row of pixels in memory to the next row of pixels in memory. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_PixelmapImageInfo\_GetPixelFormat()

Image\_ErrorCode OH\_PixelmapImageInfo\_GetPixelFormat(OH\_Pixelmap\_ImageInfo \*info, int32\_t \*pixelFormat)

**Description**

Obtains the pixel format.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Pixelmap\_ImageInfo](../../structs/oh-pixelmap-imageinfo/document.md) \*info | Pointer to an OH\_Pixelmap\_ImageInfo struct. |
| int32\_t \*pixelFormat | Pointer to the pixel format. For details about the available options, see [PIXEL\_FORMAT](#pixel_format). |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_PixelmapImageInfo\_GetAlphaType()

Image\_ErrorCode OH\_PixelmapImageInfo\_GetAlphaType(OH\_Pixelmap\_ImageInfo \*info, int32\_t \*alphaType)

**Description**

Obtains the default alpha type from OH\_PixelmapImageInfo. To obtain the current alpha type of the image, call [OH\_PixelmapImageInfo\_GetAlphaMode](#oh_pixelmapimageinfo_getalphamode).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Pixelmap\_ImageInfo](../../structs/oh-pixelmap-imageinfo/document.md) \*info | Pointer to an OH\_Pixelmap\_ImageInfo struct. |
| int32\_t \*alphaType | Pointer to the alpha type. For details about the available options, see [PIXELMAP\_ALPHA\_TYPE](#pixelmap_alpha_type). |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_PixelmapImageInfo\_GetDynamicRange()

Image\_ErrorCode OH\_PixelmapImageInfo\_GetDynamicRange(OH\_Pixelmap\_ImageInfo \*info, bool \*isHdr)

**Description**

Obtains the dynamic range of a PixelMap.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Pixelmap\_ImageInfo](../../structs/oh-pixelmap-imageinfo/document.md) \*info | Pointer to an OH\_Pixelmap\_ImageInfo struct. |
| bool \*isHdr | Pointer to whether the image is an HDR image. The value **true** means that the image is an HDR image, and the value **false** means the opposite. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_PixelmapImageInfo\_Release()

Image\_ErrorCode OH\_PixelmapImageInfo\_Release(OH\_Pixelmap\_ImageInfo \*info)

**Description**

Releases the pointer to an OH\_Pixelmap\_ImageInfo struct.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Pixelmap\_ImageInfo](../../structs/oh-pixelmap-imageinfo/document.md) \*info | Pointer to an OH\_Pixelmap\_ImageInfo struct. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_PixelmapNative\_CreatePixelmap()

Image\_ErrorCode OH\_PixelmapNative\_CreatePixelmap(uint8\_t \*data, size\_t dataLength, OH\_Pixelmap\_InitializationOptions \*options, OH\_PixelmapNative \*\*pixelmap)

**Description**

Creates a PixelMap based on properties. By default, the BGRA\_8888 format is used for data processing. For details about other formats, see [OH\_PixelmapInitializationOptions\_SetSrcPixelFormat](#oh_pixelmapinitializationoptions_setsrcpixelformat).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| uint8\_t \*data | Pointer to the color array in BGRA\_8888 format. |
| size\_t dataLength | Size of the array. |
| [OH\_Pixelmap\_InitializationOptions](../../structs/oh-pixelmap-initializationoptions/document.md) \*options | Pointer to the properties. |
| [OH\_PixelmapNative](../../structs/oh-pixelmapnative/document.md) \*\*pixelmap | Double pointer to the OH\_PixelmapNative object created. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

**IMAGE\_UNSUPPORTED\_OPERATION**: The operation is not supported.

 |

#### \[h2\]OH\_PixelmapNative\_CreatePixelmapUsingAllocator()

Image\_ErrorCode OH\_PixelmapNative\_CreatePixelmapUsingAllocator(uint8\_t \*data, size\_t dataLength, OH\_Pixelmap\_InitializationOptions \*options, IMAGE\_ALLOCATOR\_MODE allocator, OH\_PixelmapNative \*\*pixelmap)

**Description**

Creates a PixelMap object based on the options and memory type, where **allocator** specifies the memory type of the PixelMap. By default, the system selects an appropriate memory type based on the image type, image size, and platform capability. When processing the returned PixelMap object, consider the impact of stride.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| uint8\_t \*data | Pointer to the color array in BGRA\_8888 format. |
| size\_t dataLength | Size of the array. |
| [OH\_Pixelmap\_InitializationOptions](../../structs/oh-pixelmap-initializationoptions/document.md) \*options | Pointer to the options used for creating the PixelMap. |
| [IMAGE\_ALLOCATOR\_MODE](../image-common-h/document.md#image_allocator_mode) allocator | Type of memory allocation for the PixelMap. |
| [OH\_PixelmapNative](../../structs/oh-pixelmapnative/document.md) \*\*pixelmap | Double pointer to the OH\_PixelmapNative object created. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

**IMAGE\_UNSUPPORTED\_OPERATION**: The operation is not supported.

**IMAGE\_TOO\_LARGE**: The image is too large to allocate memory.

**IMAGE\_DMA\_OPERATION\_FAILED**: The DMA memory operation fails.

**IMAGE\_ALLOCATOR\_MODE\_UNSUPPORTED**: The current memory allocation type is not supported, for example, creating an HDR image using shared memory.

 |

#### \[h2\]OH\_PixelmapNative\_ConvertPixelmapNativeToNapi()

Image\_ErrorCode OH\_PixelmapNative\_ConvertPixelmapNativeToNapi(napi\_env env, OH\_PixelmapNative \*pixelmapNative, napi\_value \*pixelmapNapi)

**Description**

Converts a nativePixelMap object to a PixelMapnapi object.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| napi\_env env | Pointer to the NAPI environment. |
| [OH\_PixelmapNative](../../structs/oh-pixelmapnative/document.md) \*pixelmapNative | Pointer to an OH\_PixelmapNative object. |
| napi\_value \*pixelmapNapi | Double pointer to the PixelMapnapi object. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: The **pixelmapNative** parameter is nullptr.

 |

#### \[h2\]OH\_PixelmapNative\_ConvertPixelmapNativeFromNapi()

Image\_ErrorCode OH\_PixelmapNative\_ConvertPixelmapNativeFromNapi(napi\_env env, napi\_value pixelmapNapi, OH\_PixelmapNative \*\*pixelmapNative)

**Description**

Converts a PixelMapnapi object to a nativePixelMap object.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| napi\_env env | Pointer to the NAPI environment. |
| napi\_value pixelmapNapi | PixelMapnapi object. |
| [OH\_PixelmapNative](../../structs/oh-pixelmapnative/document.md) \*\*pixelmapNative | Double pointer to the OH\_PixelmapNative object. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: **pixelmapNative** is nullptr or is not an OH\_PixelmapNative object.

 |

#### \[h2\]OH\_PixelmapNative\_ReadPixels()

Image\_ErrorCode OH\_PixelmapNative\_ReadPixels(OH\_PixelmapNative \*pixelmap, uint8\_t \*destination, size\_t \*bufferSize)

**Description**

Reads the pixels of a PixelMap and writes the result to the buffer based on the pixel format of the PixelMap.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_PixelmapNative](../../structs/oh-pixelmapnative/document.md) \*pixelmap | Pointer to an OH\_PixelmapNative object. |
| uint8\_t \*destination | Pointer to the buffer to which the pixels will be written. |
| size\_t \*bufferSize | Pointer to the buffer size. The buffer size of the RGBA format is equal to width \* height \* 4, and the buffer size of the NV21 and NV12 formats is equal to width \* height+((width+1)/2) \* ((height+1)/2) \* 2. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

**IMAGE\_UNKNOWN\_ERROR**: An unknown error occurs.

 |

#### \[h2\]OH\_PixelmapNative\_WritePixels()

Image\_ErrorCode OH\_PixelmapNative\_WritePixels(OH\_PixelmapNative \*pixelmap, uint8\_t \*source, size\_t bufferSize)

**Description**

Reads the pixels in the buffer and writes the result to the PixelMap based on the pixel format of the PixelMap.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_PixelmapNative](../../structs/oh-pixelmapnative/document.md) \*pixelmap | Pointer to an OH\_PixelmapNative object. |
| uint8\_t \*source | Pointer to the buffer from which the pixels will be read. |
| size\_t bufferSize | Buffer size. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

**IMAGE\_UNSUPPORTED\_OPERATION**: The operation is not supported.

**IMAGE\_UNKNOWN\_ERROR**: An unknown error occurs.

 |

#### \[h2\]OH\_PixelmapNative\_ReadPixelsFromArea()

Image\_ErrorCode OH\_PixelmapNative\_ReadPixelsFromArea(OH\_PixelmapNative \*pixelmap, Image\_PositionArea \*area)

**Description**

Reads pixels from the specified area in a PixelMap and stores the result to the buffer. The read data is in BGRA\_8888 format.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_PixelmapNative](../../structs/oh-pixelmapnative/document.md) \*pixelmap | Pointer to the PixelMap from which pixels are read. |
| [Image\_PositionArea](../../structs/image-positionarea/document.md) \*area | Pointer to the area in the PixelMap. The data is read and copied to area->pixels. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: Invalid parameters. For example, **pixelmap** or **area** is incorrect.

**IMAGE\_UNKNOWN\_ERROR**: Unknown internal error. For example, the pixel format is not supported.

 |

#### \[h2\]OH\_PixelmapNative\_WritePixelsToArea()

Image\_ErrorCode OH\_PixelmapNative\_WritePixelsToArea(OH\_PixelmapNative \*pixelmap, Image\_PositionArea \*area)

**Description**

Writes pixels in the buffer to the specified area in a PixelMap. The data source must be in BGRA\_8888 format.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_PixelmapNative](../../structs/oh-pixelmapnative/document.md) \*pixelmap | Pointer to the PixelMap to which pixels are written. |
| [Image\_PositionArea](../../structs/image-positionarea/document.md) \*area | Pointer to the area in the PixelMap. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: Invalid parameters. For example, **pixelmap** or **area** is incorrect.

**IMAGE\_UNSUPPORTED\_OPERATION**: The PixelMap is not editable.

**IMAGE\_UNKNOWN\_ERROR**: Unknown internal error. For example, the pixel format is not supported.

 |

#### \[h2\]OH\_PixelmapNative\_GetArgbPixels()

Image\_ErrorCode OH\_PixelmapNative\_GetArgbPixels(OH\_PixelmapNative \*pixelmap, uint8\_t \*destination, size\_t \*bufferSize)

**Description**

Reads data in ARGB format from a PixelMap.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_PixelmapNative](../../structs/oh-pixelmapnative/document.md) \*pixelmap | Pointer to an OH\_PixelmapNative object. |
| uint8\_t \*destination | Pointer to the buffer to which the pixels will be written. |
| size\_t \*bufferSize | Pointer to the buffer size. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

IMAGE\_UNSUPPORTED\_CONVERSION: The PixelMap format does not support reading ARGB data.

**IMAGE\_ALLOC\_FAILED**: Memory allocation fails.

**IMAGE\_COPY\_FAILED**: Memory data copy, read, or operation fails.

 |

#### \[h2\]OH\_PixelmapNative\_ToSdr()

Image\_ErrorCode OH\_PixelmapNative\_ToSdr(OH\_PixelmapNative \*pixelmap)

**Description**

Converts a PixelMap from the HDR format to the SDR format.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_PixelmapNative](../../structs/oh-pixelmapnative/document.md) \*pixelmap | Pointer to an OH\_PixelmapNative object. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

**IMAGE\_UNSUPPORTED\_OPERATION**: The operation is not supported.

 |

#### \[h2\]OH\_PixelmapNative\_GetImageInfo()

Image\_ErrorCode OH\_PixelmapNative\_GetImageInfo(OH\_PixelmapNative \*pixelmap, OH\_Pixelmap\_ImageInfo \*imageInfo)

**Description**

Obtains the image information of a PixelMap.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_PixelmapNative](../../structs/oh-pixelmapnative/document.md) \*pixelmap | Pointer to an OH\_PixelmapNative object. |
| [OH\_Pixelmap\_ImageInfo](../../structs/oh-pixelmap-imageinfo/document.md) \*imageInfo | Pointer to the image information. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_PixelmapNative\_Opacity()

Image\_ErrorCode OH\_PixelmapNative\_Opacity(OH\_PixelmapNative \*pixelmap, float rate)

**Description**

Sets the opacity rate to enable the PixelMap to achieve the corresponding opacity effect.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_PixelmapNative](../../structs/oh-pixelmapnative/document.md) \*pixelmap | Pointer to an OH\_PixelmapNative object. |
| float rate | Opacity rate. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_PixelmapNative\_Scale()

Image\_ErrorCode OH\_PixelmapNative\_Scale(OH\_PixelmapNative \*pixelmap, float scaleX, float scaleY)

**Description**

Scales a PixelMap based on a given width and height.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_PixelmapNative](../../structs/oh-pixelmapnative/document.md) \*pixelmap | Pointer to an OH\_PixelmapNative object. |
| float scaleX | Scale ratio of the width. |
| float scaleY | Scale ratio of the height. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_PixelmapNative\_ScaleWithAntiAliasing()

Image\_ErrorCode OH\_PixelmapNative\_ScaleWithAntiAliasing(OH\_PixelmapNative \*pixelmap, float scaleX, float scaleY, OH\_PixelmapNative\_AntiAliasingLevel level)

**Description**

Scales a PixelMap based on the specified anti-aliasing level, width, and height.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_PixelmapNative](../../structs/oh-pixelmapnative/document.md) \*pixelmap | Pointer to an OH\_PixelmapNative object. |
| float scaleX | Scale ratio of the width. |
| float scaleY | Scale ratio of the height. |
| [OH\_PixelmapNative\_AntiAliasingLevel](#oh_pixelmapnative_antialiasinglevel) level | Anti-aliasing level. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

**IMAGE\_TOO\_LARGE**: The image is too large.

**IMAGE\_ALLOC\_FAILED**: Memory allocation fails.

**IMAGE\_UNKNOWN\_ERROR**: The struct that **pixelmap** points to is released.

 |

#### \[h2\]OH\_PixelmapNative\_CreateScaledPixelMap()

Image\_ErrorCode OH\_PixelmapNative\_CreateScaledPixelMap(OH\_PixelmapNative \*srcPixelmap, OH\_PixelmapNative \*\*dstPixelmap, float scaleX, float scaleY)

**Description**

Creates a PixelMap that has been resized based on the specified scale factors of the width and height.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_PixelmapNative](../../structs/oh-pixelmapnative/document.md) \*srcPixelmap | Pointer to the source PixelMap, which is an OH\_PixelmapNative object. |
| [OH\_PixelmapNative](../../structs/oh-pixelmapnative/document.md) \*\*dstPixelmap | Double pointer to the destination PixelMap, which is an OH\_PixelmapNative object. |
| float scaleX | Scale ratio of the width. |
| float scaleY | Scale ratio of the height. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_PixelmapNative\_CreateScaledPixelMapWithAntiAliasing()

Image\_ErrorCode OH\_PixelmapNative\_CreateScaledPixelMapWithAntiAliasing(OH\_PixelmapNative \*srcPixelmap, OH\_PixelmapNative \*\*dstPixelmap, float scaleX, float scaleY, OH\_PixelmapNative\_AntiAliasingLevel level)

**Description**

Creates a PixelMap that has been resized based on the specified anti-aliasing level and the scale factors of the width and height.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_PixelmapNative](../../structs/oh-pixelmapnative/document.md) \*srcPixelmap | Pointer to the source PixelMap, which is an OH\_PixelmapNative object. |
| [OH\_PixelmapNative](../../structs/oh-pixelmapnative/document.md) \*\*dstPixelmap | Double pointer to the destination PixelMap, which is an OH\_PixelmapNative object. |
| float scaleX | Scale ratio of the width. |
| float scaleY | Scale ratio of the height. |
| [OH\_PixelmapNative\_AntiAliasingLevel](#oh_pixelmapnative_antialiasinglevel) level | Anti-aliasing level. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

**IMAGE\_TOO\_LARGE**: The image is too large.

**IMAGE\_ALLOC\_FAILED**: Memory allocation fails.

 |

#### \[h2\]OH\_PixelmapNative\_CreateAlphaPixelmap()

Image\_ErrorCode OH\_PixelmapNative\_CreateAlphaPixelmap(OH\_PixelmapNative \*srcPixelmap, OH\_PixelmapNative \*\*dstPixelmap)

**Description**

Creates a PixelMap that contains only the alpha channel from the source PixelMap.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_PixelmapNative](../../structs/oh-pixelmapnative/document.md) \*srcPixelmap | Pointer to the source PixelMap. |
| [OH\_PixelmapNative](../../structs/oh-pixelmapnative/document.md) \*\*dstPixelmap | Double pointer to the destination PixelMap created. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: Invalid parameters. For example, **srcPixelmap** or **dstPixelmap** is incorrect.

 |

#### \[h2\]OH\_PixelmapNative\_Clone()

Image\_ErrorCode OH\_PixelmapNative\_Clone(OH\_PixelmapNative \*srcPixelmap, OH\_PixelmapNative \*\*dstPixelmap)

**Description**

Clones a new PixelMap from the source PixelMap.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_PixelmapNative](../../structs/oh-pixelmapnative/document.md) \*srcPixelmap | Pointer to the source PixelMap. |
| [OH\_PixelmapNative](../../structs/oh-pixelmapnative/document.md) \*\*dstPixelmap | Double pointer to the destination PixelMap created. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: Invalid parameters. For example, **srcPixelmap** or **dstPixelmap** is incorrect.

**IMAGE\_UNSUPPORTED\_DATA\_FORMAT**: The pixel format is not supported.

**IMAGE\_TOO\_LARGE**: The source PixelMap is too large.

**IMAGE\_INIT\_FAILED**: The destination PixelMap fails to be initialized.

**IMAGE\_ALLOC\_FAILED**: Memory allocation or data copy fails.

 |

#### \[h2\]OH\_PixelmapNative\_CreateCroppedAndScaledPixelMap()

Image\_ErrorCode OH\_PixelmapNative\_CreateCroppedAndScaledPixelMap(OH\_PixelmapNative \*srcPixelmap, Image\_Region \*region, Image\_Scale \*scale, OH\_PixelmapNative\_AntiAliasingLevel level, OH\_PixelmapNative \*\*dstPixelmap)

**Description**

Creates a PixelMap that is cropped and resized based on the source PixelMap.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_PixelmapNative](../../structs/oh-pixelmapnative/document.md) \*srcPixelmap | Pointer to the source PixelMap. |
| [Image\_Region](../../structs/image-region/document.md) \*region | Pointer to the region to crop. |
| [Image\_Scale](../../structs/image-scale/document.md) \*scale | Pointer to the scale factor of the width and height. It must not be **0**. |
| [OH\_PixelmapNative\_AntiAliasingLevel](#oh_pixelmapnative_antialiasinglevel) level | Scale interpolation algorithm. |
| [OH\_PixelmapNative](../../structs/oh-pixelmapnative/document.md) \*\*dstPixelmap | Double pointer to the destination PixelMap created. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: Invalid parameters. For example, **srcPixelmap**, **region**, **scale**, or **dstPixelmap** is incorrect.

**IMAGE\_UNSUPPORTED\_DATA\_FORMAT**: The pixel format is not supported.

**IMAGE\_TOO\_LARGE**: The source PixelMap is too large.

**IMAGE\_INIT\_FAILED**: The destination PixelMap fails to be initialized.

**IMAGE\_ALLOC\_FAILED**: Memory allocation or data copy fails.

 |

#### \[h2\]OH\_PixelmapNative\_Translate()

Image\_ErrorCode OH\_PixelmapNative\_Translate(OH\_PixelmapNative \*pixelmap, float x, float y)

**Description**

Translates a PixelMap based on given coordinates.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_PixelmapNative](../../structs/oh-pixelmapnative/document.md) \*pixelmap | Pointer to an OH\_PixelmapNative object. |
| float x | X coordinate to translate. |
| float y | Y coordinate to translate. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_PixelmapNative\_Rotate()

Image\_ErrorCode OH\_PixelmapNative\_Rotate(OH\_PixelmapNative \*pixelmap, float angle)

**Description**

Rotates a PixelMap based on a given angle.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_PixelmapNative](../../structs/oh-pixelmapnative/document.md) \*pixelmap | Pointer to an OH\_PixelmapNative object. |
| float angle | Image rotation angle, in degrees. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_PixelmapNative\_Flip()

Image\_ErrorCode OH\_PixelmapNative\_Flip(OH\_PixelmapNative \*pixelmap, bool shouldFlipHorizontally, bool shouldFlipVertically)

**Description**

Flips a PixelMap based on a given angle.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_PixelmapNative](../../structs/oh-pixelmapnative/document.md) \*pixelmap | Pointer to an OH\_PixelmapNative object. |
| bool shouldFlipHorizontally | Whether to flip the image horizontally. Whether to flip the image horizontally. **true** to flip the image horizontally, **false** otherwise. |
| bool shouldFlipVertically | Whether to flip the image vertically. Whether to flip the image vertically. **true** to flip the image vertically, **false** otherwise. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_PixelmapNative\_Crop()

Image\_ErrorCode OH\_PixelmapNative\_Crop(OH\_PixelmapNative \*pixelmap, Image\_Region \*region)

**Description**

Crops a PixelMap based on a given size.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_PixelmapNative](../../structs/oh-pixelmapnative/document.md) \*pixelmap | Pointer to an OH\_PixelmapNative object. |
| [Image\_Region](../../structs/image-region/document.md) \*region | Pointer to the region of the image after cropping. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_PixelmapNative\_Release()

Image\_ErrorCode OH\_PixelmapNative\_Release(OH\_PixelmapNative \*pixelmap)

**Description**

Releases the pointer to an OH\_PixelmapNative object. [OH\_PixelmapNative\_Destroy](#oh_pixelmapnative_destroy) is recommended.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_PixelmapNative](../../structs/oh-pixelmapnative/document.md) \*pixelmap | Pointer to an OH\_PixelmapNative object. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_PixelmapNative\_Destroy()

Image\_ErrorCode OH\_PixelmapNative\_Destroy(OH\_PixelmapNative \*\*pixelmap)

**Description**

Releases the pointer to an OH\_PixelmapNative object.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_PixelmapNative](../../structs/oh-pixelmapnative/document.md) \*\*pixelmap | Pointer to an OH\_PixelmapNative object. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_PixelmapNative\_ConvertAlphaFormat()

Image\_ErrorCode OH\_PixelmapNative\_ConvertAlphaFormat(OH\_PixelmapNative\* srcpixelmap, OH\_PixelmapNative\* dstpixelmap, const bool isPremul)

**Description**

Converts pixel data of a PixelMap from premultiplied alpha to non-premultiplied alpha, or vice versa.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_PixelmapNative](../../structs/oh-pixelmapnative/document.md)\* srcpixelmap | Pointer to the source PixelMap, which is an OH\_PixelmapNative object. |
| [OH\_PixelmapNative](../../structs/oh-pixelmapnative/document.md)\* dstpixelmap | Pointer to the destination PixelMap, which is an OH\_PixelmapNative object. |
| const bool isPremul | Conversion mode. The value **true** means a conversion from premultiplied alpha to non-premultiplied alpha, and **false** means a conversion from non-premultiplied alpha to premultiplied alpha. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_PixelmapNative\_CreateEmptyPixelmap()

Image\_ErrorCode OH\_PixelmapNative\_CreateEmptyPixelmap(OH\_Pixelmap\_InitializationOptions \*options, OH\_PixelmapNative \*\*pixelmap)

**Description**

Creates an empty PixelMap object based on **OH\_Pixelmap\_InitializationOptions**. The memory data is 0.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Pixelmap\_InitializationOptions](../../structs/oh-pixelmap-initializationoptions/document.md) \*options | Pointer to the properties. |
| [OH\_PixelmapNative](../../structs/oh-pixelmapnative/document.md) \*\*pixelmap | Double pointer to the OH\_PixelmapNative object created. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_PixelmapNative\_CreateEmptyPixelmapUsingAllocator()

Image\_ErrorCode OH\_PixelmapNative\_CreateEmptyPixelmapUsingAllocator(OH\_Pixelmap\_InitializationOptions \*options, IMAGE\_ALLOCATOR\_MODE allocator, OH\_PixelmapNative \*\*pixelmap)

**Description**

Creates an empty PixelMap object based on the options and memory type, where **allocator** specifies the memory type of the PixelMap. By default, the system selects an appropriate memory type based on the image type, image size, and platform capability. When processing the returned PixelMap object, consider the impact of stride.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Pixelmap\_InitializationOptions](../../structs/oh-pixelmap-initializationoptions/document.md) \*options | Pointer to the options used for creating the PixelMap. |
| [IMAGE\_ALLOCATOR\_MODE](../image-common-h/document.md#image_allocator_mode) allocator | Type of memory allocation for the PixelMap. |
| [OH\_PixelmapNative](../../structs/oh-pixelmapnative/document.md) \*\*pixelmap | Double pointer to the OH\_PixelmapNative object created. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

**IMAGE\_UNSUPPORTED\_OPERATION**: The operation is not supported.

**IMAGE\_TOO\_LARGE**: The image is too large to allocate memory.

**IMAGE\_DMA\_OPERATION\_FAILED**: The DMA memory operation fails.

**IMAGE\_ALLOCATOR\_MODE\_UNSUPPORTED**: The current memory allocation type is not supported, for example, creating an HDR image using shared memory.

 |

#### \[h2\]OH\_PixelmapNative\_CreatePixelmapFromSurface()

Image\_ErrorCode OH\_PixelmapNative\_CreatePixelmapFromSurface(const char \*surfaceId, size\_t length, OH\_PixelmapNative \*\*pixelmap)

**Description**

Creates a PixelMap from a surface with the specified surface ID.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| const char \*surfaceId | Pointer to the string of the surface ID. |
| size\_t length | Length of the surface ID string. |
| [OH\_PixelmapNative](../../structs/oh-pixelmapnative/document.md) \*\*pixelmap | Double pointer to the PixelMap created. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: Invalid parameters. For example, **surfaceId** or **pixelmap** is incorrect.

**IMAGE\_CREATE\_PIXELMAP\_FAILED**: Creating the PixelMap fails.

 |

#### \[h2\]OH\_PixelmapNative\_CreatePixelmapFromNativeBuffer()

Image\_ErrorCode OH\_PixelmapNative\_CreatePixelmapFromNativeBuffer(OH\_NativeBuffer \*nativeBuffer, OH\_PixelmapNative \*\*pixelmap)

**Description**

Creates a PixelMap using a NativeBuffer. If the [CPU access permission](../../../../../graphics/arkgraphics-2d/c-apis/header-files/native-buffer-h/document.md#oh_nativebuffer_usage) is not configured for the NativeBuffer, the PixelMap cannot be created.

The supported pixel formats are RGBA\_8888, NV21, NV12, YCBCR\_P010, and YCRCB\_P010.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NativeBuffer](../../structs/oh-nativebuffer/document.md) \*nativeBuffer | Pointer to the NativeBuffer object that contains PixelMap data. |
| [OH\_PixelmapNative](../../structs/oh-pixelmapnative/document.md) \*\*pixelmap | Double pointer to the PixelMap created. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: The parameter is invalid. For example, **nativeBuffer** or **pixelmap** is incorrect, the pixel format is not supported, or the [CPU access permission](../../../../../graphics/arkgraphics-2d/c-apis/header-files/native-buffer-h/document.md#oh_nativebuffer_usage) is not configured.

**IMAGE\_CREATE\_PIXELMAP\_FAILED**: Creating the PixelMap fails.

 |

#### \[h2\]OH\_PixelmapNative\_GetNativeBuffer()

Image\_ErrorCode OH\_PixelmapNative\_GetNativeBuffer(OH\_PixelmapNative \*pixelmap, OH\_NativeBuffer \*\*nativeBuffer)

**Description**

Obtains the NativeBuffer object from a PixelMap in the DMA memory.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_PixelmapNative](../../structs/oh-pixelmapnative/document.md) \*pixelmap | Pointer to the PixelMap. |
| [OH\_NativeBuffer](../../structs/oh-nativebuffer/document.md) \*\*nativeBuffer | Double pointer to the NativeBuffer object obtained. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

**IMAGE\_DMA\_NOT\_EXIST**: DMA memory does not exist.

**IMAGE\_DMA\_OPERATION\_FAILED**: The DMA memory operation fails.

 |

#### \[h2\]OH\_PixelmapNative\_GetMetadata()

Image\_ErrorCode OH\_PixelmapNative\_GetMetadata(OH\_PixelmapNative \*pixelmap, OH\_Pixelmap\_HdrMetadataKey key, OH\_Pixelmap\_HdrMetadataValue \*\*value)

**Description**

Obtains the metadata.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_PixelmapNative](../../structs/oh-pixelmapnative/document.md) \*pixelmap | Pointer to an OH\_PixelmapNative object. |
| [OH\_Pixelmap\_HdrMetadataKey](#oh_pixelmap_hdrmetadatakey) key | HDR metadata key. |
| [OH\_Pixelmap\_HdrMetadataValue](../../structs/oh-pixelmap-hdrmetadatavalue/document.md) \*\*value | Double pointer to the value of the metadata key. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

**IMAGE\_DMA\_NOT\_EXIST**: DMA memory does not exist.

**IMAGE\_COPY\_FAILED**: Memory copy fails.

 |

#### \[h2\]OH\_PixelmapNative\_SetMetadata()

Image\_ErrorCode OH\_PixelmapNative\_SetMetadata(OH\_PixelmapNative \*pixelmap, OH\_Pixelmap\_HdrMetadataKey key, OH\_Pixelmap\_HdrMetadataValue \*value)

**Description**

Sets the metadata.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_PixelmapNative](../../structs/oh-pixelmapnative/document.md) \*pixelmap | Pointer to an OH\_PixelmapNative object. |
| [OH\_Pixelmap\_HdrMetadataKey](#oh_pixelmap_hdrmetadatakey) key | HDR metadata key. |
| [OH\_Pixelmap\_HdrMetadataValue](../../structs/oh-pixelmap-hdrmetadatavalue/document.md) \*value | Pointer to the value of the metadata key. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

**IMAGE\_DMA\_NOT\_EXIST**: DMA memory does not exist.

**IMAGE\_COPY\_FAILED**: Memory copy fails.

 |

#### \[h2\]OH\_PixelmapNative\_SetColorSpaceNative()

Image\_ErrorCode OH\_PixelmapNative\_SetColorSpaceNative(OH\_PixelmapNative \*pixelmap, OH\_NativeColorSpaceManager \*colorSpaceNative)

**Description**

Sets a NativeColorSpaceManager object.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_PixelmapNative](../../structs/oh-pixelmapnative/document.md) \*pixelmap | Pointer to the target PixelMap of the NativeColorSpaceManager object. |
| [OH\_NativeColorSpaceManager](../../structs/oh-nativecolorspacemanager/document.md) \*colorSpaceNative | Pointer to a NativeColorSpaceManager object. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_PixelmapNative\_GetColorSpaceNative()

Image\_ErrorCode OH\_PixelmapNative\_GetColorSpaceNative(OH\_PixelmapNative \*pixelmap, OH\_NativeColorSpaceManager \*\*colorSpaceNative)

**Description**

Obtains a NativeColorSpaceManager object.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_PixelmapNative](../../structs/oh-pixelmapnative/document.md) \*pixelmap | Pointer to the source PixelMap of the NativeColorSpaceManager. |
| [OH\_NativeColorSpaceManager](../../structs/oh-nativecolorspacemanager/document.md) \*\*colorSpaceNative | Double pointer to the NativeColorSpaceManager object obtained. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_PixelmapNative\_SetMemoryName()

Image\_ErrorCode OH\_PixelmapNative\_SetMemoryName(OH\_PixelmapNative \*pixelmap, char \*name, size\_t \*size)

**Description**

Sets the memory name of a PixelMap.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_PixelmapNative](../../structs/oh-pixelmapnative/document.md) \*pixelmap | Pointer to an OH\_PixelmapNative object. |
| char \*name | Pointer to the memory name. |
| size\_t \*size | Pointer to the memory size (in bytes). |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: The name length exceeds the value range. The name length for DMA memory settings should be within the range of 1 to 255 bytes. For ASHMEM memory settings, the name length should be within the range of 1 to 244 bytes.

**IMAGE\_UNSUPPORTED\_MEMORY\_FORMAT**: The memory is neither DMA memory nor ASHMEM memory.

 |

#### \[h2\]OH\_PixelmapNative\_GetByteCount()

Image\_ErrorCode OH\_PixelmapNative\_GetByteCount(OH\_PixelmapNative \*pixelmap, uint32\_t \*byteCount)

**Description**

Obtains the total number of bytes occupied by all pixels in a PixelMap, excluding any memory padding.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_PixelmapNative](../../structs/oh-pixelmapnative/document.md) \*pixelmap | Pointer to a PixelMap. |
| uint32\_t \*byteCount | Pointer to the number of bytes obtained. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**Image\_BAD\_PARAMETER**: The **pixelmap** or **byteCount** parameter is invalid.

 |

#### \[h2\]OH\_PixelmapNative\_GetAllocationByteCount()

Image\_ErrorCode OH\_PixelmapNative\_GetAllocationByteCount(OH\_PixelmapNative \*pixelmap, uint32\_t \*allocationByteCount)

**Description**

Obtains the number of bytes in the memory allocated by a PixelMap to store pixels.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_PixelmapNative](../../structs/oh-pixelmapnative/document.md) \*pixelmap | Pointer to a PixelMap. |
| uint32\_t \*allocationByteCount | Pointer to the number of bytes obtained. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**Image\_BAD\_PARAMETER**: The **pixelmap** or **allocationByteCount** parameter is invalid.

 |

#### \[h2\]OH\_PixelmapNative\_AccessPixels()

Image\_ErrorCode OH\_PixelmapNative\_AccessPixels(OH\_PixelmapNative \*pixelmap, void \*\*addr)

**Description**

Obtains the memory address where the pixels of a PixelMap are stored and locks the memory.

When the memory is locked, any attempts to alter or free the pixel data of the PixelMap will fail or be ineffective.

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_PixelmapNative](../../structs/oh-pixelmapnative/document.md) \*pixelmap | Pointer to a PixelMap. |
| void \*\*addr | Double pointer to the memory address. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**Image\_BAD\_PARAMETER**: The **pixelmap** or **addr** parameter is invalid.

**Image\_LOCK\_UNLOCK\_FAILED**: Memory locking fails.

 |

#### \[h2\]OH\_PixelmapNative\_UnaccessPixels()

Image\_ErrorCode OH\_PixelmapNative\_UnaccessPixels(OH\_PixelmapNative \*pixelmap)

**Description**

Unlocks the memory allocated to store the pixels of a PixelMap.

This function must be used together with [OH\_PixelmapNative\_AccessPixels](#oh_pixelmapnative_accesspixels).

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_PixelmapNative](../../structs/oh-pixelmapnative/document.md) \*pixelmap | Pointer to a PixelMap. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**Image\_BAD\_PARAMETER**: The **pixelmap** parameter is invalid.

**IMAGE\_LOCK\_UNLOCK\_FAILED**: Memory unlocking fails.

 |

#### \[h2\]OH\_PixelmapNative\_GetUniqueId()

Image\_ErrorCode OH\_PixelmapNative\_GetUniqueId(OH\_PixelmapNative \*pixelmap, uint32\_t \*uniqueId)

**Description**

Obtains the unique ID of a PixelMap.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_PixelmapNative](../../structs/oh-pixelmapnative/document.md) \*pixelmap | Pointer to the PixelMap. |
| uint32\_t \*uniqueId | Pointer to the unique ID obtained. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: Invalid parameters. For example, **pixelmap** or **uniqueId** is incorrect.

 |

#### \[h2\]OH\_PixelmapNative\_IsReleased()

Image\_ErrorCode OH\_PixelmapNative\_IsReleased(OH\_PixelmapNative \*pixelmap, bool \*released)

**Description**

Checks whether a PixelMap is released. If released, any attempt to access the internal data of this object will fail.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_PixelmapNative](../../structs/oh-pixelmapnative/document.md) \*pixelmap | Pointer to the PixelMap. |
| bool \*released | Release status of the obtained PixelMap. The value **true** means that the PixelMap is released, and **false** means the opposite. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: Invalid parameters. For example, **pixelmap** or **released** is incorrect.

 |
