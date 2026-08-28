# image\_effect\_filter.h

#### Overview

The file declares the APIs related to an image effect filter.

With these APIs, you can quickly implement basic effect processing or connect multiple filters in series in an image effector to implement complex effect processing. The system provides basic effect processing filters such as brightness and crop filters.

**File to include**: <multimedia/image\_effect/image\_effect\_filter.h>

**Library**: libimage\_effect.so

**System capability**: SystemCapability.Multimedia.ImageEffect.Core

**Since**: 12

**Related module**: [ImageEffect](../../modules/imageeffect/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [ImageEffect\_DataValue](../../structs/imageeffect-datavalue/document.md) | ImageEffect\_DataValue | Describes the data values. |
| [ImageEffect\_Any](../../structs/imageeffect-any/document.md) | ImageEffect\_Any | Describes the image effect parameters. |
| [ImageEffect\_FilterNames](../../structs/imageeffect-filternames/document.md) | ImageEffect\_FilterNames | Describes the filter name information. |
| [ImageEffect\_FilterDelegate](../../structs/imageeffect-filterdelegate/document.md) | ImageEffect\_FilterDelegate | Describes the callback functions of a custom filter. |
| [ImageEffect\_Region](../../structs/imageeffect-region/document.md) | ImageEffect\_Region | Describes the image region. |
| [ImageEffect\_Size](../../structs/imageeffect-size/document.md) | ImageEffect\_Size | Describes the image size. |
| [OH\_EffectFilter](../../structs/oh-effectfilter/document.md) | OH\_EffectFilter | Describes the image effect filter. |
| [OH\_EffectFilterInfo](../../structs/oh-effectfilterinfo/document.md) | OH\_EffectFilterInfo | Describes the filter information. |
| [OH\_EffectBufferInfo](../../structs/oh-effectbufferinfo/document.md) | OH\_EffectBufferInfo | Describes the buffer information. |

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [ImageEffect\_DataType](#imageeffect_datatype) | ImageEffect\_DataType | Enumerates the data types. |
| [ImageEffect\_Format](#imageeffect_format) | ImageEffect\_Format | Enumerates the pixel formats. |
| [ImageEffect\_BufferType](#imageeffect_buffertype) | ImageEffect\_BufferType | Enumerates the buffer types. |

#### \[h2\]Macros

| Name | Description |
| :-- | :-- |
| OH\_EFFECT\_BRIGHTNESS\_FILTER "Brightness" | 
Brightness filter. The corresponding parameter is **OH\_EFFECT\_FILTER\_INTENSITY\_KEY** and the parameter type is [EFFECT\_DATA\_TYPE\_FLOAT](#imageeffect_datatype).

**Since**: 12

**System capability**: SystemCapability.Multimedia.ImageEffect.Core

 |
| OH\_EFFECT\_CONTRAST\_FILTER "Contrast" | 

Contrast filter. The corresponding parameter is **OH\_EFFECT\_FILTER\_INTENSITY\_KEY** and the parameter type is [EFFECT\_DATA\_TYPE\_FLOAT](#imageeffect_datatype).

**Since**: 12

**System capability**: SystemCapability.Multimedia.ImageEffect.Core

 |
| OH\_EFFECT\_CROP\_FILTER "Crop" | 

Crop filter. The corresponding parameter is **OH\_EFFECT\_FILTER\_REGION\_KEY**, the parameter type is [EFFECT\_DATA\_TYPE\_PTR](#imageeffect_datatype), and the parameter value is [ImageEffect\_Region](../../structs/imageeffect-region/document.md).

**Since**: 12

**System capability**: SystemCapability.Multimedia.ImageEffect.Core

 |
| OH\_EFFECT\_FILTER\_INTENSITY\_KEY "FilterIntensity" | 

Intensity filter.

**Since**: 12

**System capability**: SystemCapability.Multimedia.ImageEffect.Core

 |
| OH\_EFFECT\_FILTER\_REGION\_KEY "FilterRegion" | 

Image region filter.

**Since**: 12

**System capability**: SystemCapability.Multimedia.ImageEffect.Core

 |

#### \[h2\]Functions

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_EffectFilterInfo \*OH\_EffectFilterInfo\_Create()](#oh_effectfilterinfo_create) | \- | Creates an OH\_EffectFilterInfo instance. The instance must be released by calling [OH\_EffectFilterInfo\_Release](#oh_effectfilterinfo_release) when it is no longer needed. |
| [ImageEffect\_ErrorCode OH\_EffectFilterInfo\_SetFilterName(OH\_EffectFilterInfo \*info, const char \*name)](#oh_effectfilterinfo_setfiltername) | \- | Sets a filter name. |
| [ImageEffect\_ErrorCode OH\_EffectFilterInfo\_GetFilterName(OH\_EffectFilterInfo \*info, char \*\*name)](#oh_effectfilterinfo_getfiltername) | \- | Obtains a filter name. |
| [ImageEffect\_ErrorCode OH\_EffectFilterInfo\_SetSupportedBufferTypes(OH\_EffectFilterInfo \*info, uint32\_t size, ImageEffect\_BufferType \*bufferTypeArray)](#oh_effectfilterinfo_setsupportedbuffertypes) | \- | Sets the buffer types supported by a filter. |
| [ImageEffect\_ErrorCode OH\_EffectFilterInfo\_GetSupportedBufferTypes(OH\_EffectFilterInfo \*info, uint32\_t \*size, ImageEffect\_BufferType \*\*bufferTypeArray)](#oh_effectfilterinfo_getsupportedbuffertypes) | \- | Obtains the buffer types supported by a filter. |
| [ImageEffect\_ErrorCode OH\_EffectFilterInfo\_SetSupportedFormats(OH\_EffectFilterInfo \*info, uint32\_t size, ImageEffect\_Format \*formatArray)](#oh_effectfilterinfo_setsupportedformats) | \- | Sets the pixel formats supported by a filter. |
| [ImageEffect\_ErrorCode OH\_EffectFilterInfo\_GetSupportedFormats(OH\_EffectFilterInfo \*info, uint32\_t \*size, ImageEffect\_Format \*\*formatArray)](#oh_effectfilterinfo_getsupportedformats) | \- | Obtains the pixel formats supported by a filter. |
| [ImageEffect\_ErrorCode OH\_EffectFilterInfo\_Release(OH\_EffectFilterInfo \*info)](#oh_effectfilterinfo_release) | \- | Destroys an OH\_EffectFilterInfo instance. |
| [OH\_EffectBufferInfo \*OH\_EffectBufferInfo\_Create()](#oh_effectbufferinfo_create) | \- | Creates an OH\_EffectBufferInfo instance. The instance must be released by calling [OH\_EffectBufferInfo\_Release](#oh_effectbufferinfo_release) when it is no longer needed. |
| [ImageEffect\_ErrorCode OH\_EffectBufferInfo\_SetAddr(OH\_EffectBufferInfo \*info, void \*addr)](#oh_effectbufferinfo_setaddr) | \- | Sets the address of an effect buffer. |
| [ImageEffect\_ErrorCode OH\_EffectBufferInfo\_GetAddr(OH\_EffectBufferInfo \*info, void \*\*addr)](#oh_effectbufferinfo_getaddr) | \- | Obtains the address of an effect buffer. |
| [ImageEffect\_ErrorCode OH\_EffectBufferInfo\_SetWidth(OH\_EffectBufferInfo \*info, int32\_t width)](#oh_effectbufferinfo_setwidth) | \- | Sets the image width. |
| [ImageEffect\_ErrorCode OH\_EffectBufferInfo\_GetWidth(OH\_EffectBufferInfo \*info, int32\_t \*width)](#oh_effectbufferinfo_getwidth) | \- | Obtains the image width. |
| [ImageEffect\_ErrorCode OH\_EffectBufferInfo\_SetHeight(OH\_EffectBufferInfo \*info, int32\_t height)](#oh_effectbufferinfo_setheight) | \- | Sets the image height. |
| [ImageEffect\_ErrorCode OH\_EffectBufferInfo\_GetHeight(OH\_EffectBufferInfo \*info, int32\_t \*height)](#oh_effectbufferinfo_getheight) | \- | Obtains the image height. |
| [ImageEffect\_ErrorCode OH\_EffectBufferInfo\_SetRowSize(OH\_EffectBufferInfo \*info, int32\_t rowSize)](#oh_effectbufferinfo_setrowsize) | \- | Sets the number of bytes per row for an image. |
| [ImageEffect\_ErrorCode OH\_EffectBufferInfo\_GetRowSize(OH\_EffectBufferInfo \*info, int32\_t \*rowSize)](#oh_effectbufferinfo_getrowsize) | \- | Obtains the number of bytes per row of an image. |
| [ImageEffect\_ErrorCode OH\_EffectBufferInfo\_SetEffectFormat(OH\_EffectBufferInfo \*info, ImageEffect\_Format format)](#oh_effectbufferinfo_seteffectformat) | \- | Sets the pixel format for an image. |
| [ImageEffect\_ErrorCode OH\_EffectBufferInfo\_GetEffectFormat(OH\_EffectBufferInfo \*info, ImageEffect\_Format \*format)](#oh_effectbufferinfo_geteffectformat) | \- | Obtains the pixel format of an image. |
| [ImageEffect\_ErrorCode OH\_EffectBufferInfo\_SetTextureId(OH\_EffectBufferInfo \*info, int32\_t textureId)](#oh_effectbufferinfo_settextureid) | \- | Sets the texture ID of the image for an OH\_EffectBufferInfo struct. |
| [ImageEffect\_ErrorCode OH\_EffectBufferInfo\_GetTextureId(OH\_EffectBufferInfo \*info, int32\_t \*textureId)](#oh_effectbufferinfo_gettextureid) | \- | Obtains the texture ID of an image from an OH\_EffectBufferInfo struct. |
| [ImageEffect\_ErrorCode OH\_EffectBufferInfo\_Release(OH\_EffectBufferInfo \*info)](#oh_effectbufferinfo_release) | \- | Destroys an OH\_EffectBufferInfo instance. |
| [typedef bool (\*OH\_EffectFilterDelegate\_SetValue)(OH\_EffectFilter \*filter, const char \*key, const ImageEffect\_Any \*value)](#oh_effectfilterdelegate_setvalue) | OH\_EffectFilterDelegate\_SetValue | Defines a pointer to the callback function for setting parameters of a custom filter. It is used to verify parameters and parameter values. |
| [typedef void (\*OH\_EffectFilterDelegate\_PushData)(OH\_EffectFilter \*filter, OH\_EffectBufferInfo \*info)](#oh_effectfilterdelegate_pushdata) | OH\_EffectFilterDelegate\_PushData | Defines a pointer to the callback function used by a custom filter to push image data to the next-level filter. The function pointer must be actively called in the callback of [OH\_EffectFilterDelegate\_Render](#oh_effectfilterdelegate_render). |
| [typedef bool (\*OH\_EffectFilterDelegate\_Render)(OH\_EffectFilter \*filter, OH\_EffectBufferInfo \*info, OH\_EffectFilterDelegate\_PushData pushData)](#oh_effectfilterdelegate_render) | OH\_EffectFilterDelegate\_Render | Defines a pointer to the callback function for rendering an image using a custom filter. |
| [typedef bool (\*OH\_EffectFilterDelegate\_Save)(OH\_EffectFilter \*filter, char \*\*info)](#oh_effectfilterdelegate_save) | OH\_EffectFilterDelegate\_Save | Defines a pointer to the callback function for serializing a custom filter. Filters are serialized in JSON format. |
| [typedef OH\_EffectFilter \*(\*OH\_EffectFilterDelegate\_Restore)(const char \*info)](#oh_effectfilterdelegate_restore) | OH\_EffectFilterDelegate\_Restore | Defines a pointer to the callback function for deserializing a custom filter. |
| [OH\_EffectFilter \*OH\_EffectFilter\_Create(const char \*name)](#oh_effectfilter_create) | \- | Creates an OH\_EffectFilter instance. The instance must be released by calling [OH\_EffectFilter\_Release](#oh_effectfilter_release) when it is no longer needed. |
| [ImageEffect\_ErrorCode OH\_EffectFilter\_SetValue(OH\_EffectFilter \*filter, const char \*key, const ImageEffect\_Any \*value)](#oh_effectfilter_setvalue) | \- | Sets a filter parameter. |
| [ImageEffect\_ErrorCode OH\_EffectFilter\_GetValue(OH\_EffectFilter \*filter, const char \*key, ImageEffect\_Any \*value)](#oh_effectfilter_getvalue) | \- | Obtains a filter parameter. |
| [ImageEffect\_ErrorCode OH\_EffectFilter\_Register(const OH\_EffectFilterInfo \*info, const ImageEffect\_FilterDelegate \*delegate)](#oh_effectfilter_register) | \- | Registers a custom filter. |
| [ImageEffect\_FilterNames \*OH\_EffectFilter\_LookupFilters(const char \*key)](#oh_effectfilter_lookupfilters) | \- | Obtains filters that meet given conditions. |
| [void OH\_EffectFilter\_ReleaseFilterNames()](#oh_effectfilter_releasefilternames) | \- | Releases filter name memory resources. |
| [ImageEffect\_ErrorCode OH\_EffectFilter\_LookupFilterInfo(const char \*name, OH\_EffectFilterInfo \*info)](#oh_effectfilter_lookupfilterinfo) | \- | Obtains the filter information. |
| [ImageEffect\_ErrorCode OH\_EffectFilter\_Render(OH\_EffectFilter \*filter, OH\_PixelmapNative \*inputPixelmap, OH\_PixelmapNative \*outputPixelmap)](#oh_effectfilter_render) | \- | Starts image rendering. |
| [ImageEffect\_ErrorCode OH\_EffectFilter\_RenderWithTextureId(OH\_EffectFilter \*filter, int32\_t inputTextureId, int32\_t outputTextureId, int32\_t colorSpace)](#oh_effectfilter_renderwithtextureid) | \- | Applies the filter effect using texture IDs. This function does not support using the same texture for both input and output. |
| [ImageEffect\_ErrorCode OH\_EffectFilter\_Release(OH\_EffectFilter \*filter)](#oh_effectfilter_release) | \- | Destroys an OH\_EffectFilter instance. |
| [ImageEffect\_ErrorCode OH\_EffectBufferInfo\_SetTimestamp(OH\_EffectBufferInfo \*info, int64\_t timestamp)](#oh_effectbufferinfo_settimestamp) | \- | Sets the filter timestamp. |
| [ImageEffect\_ErrorCode OH\_EffectBufferInfo\_GetTimestamp(OH\_EffectBufferInfo \*info, int64\_t \*timestamp)](#oh_effectbufferinfo_gettimestamp) | \- | Obtains the filter timestamp. |

#### Enum Description

#### \[h2\]ImageEffect\_DataType

enum ImageEffect\_DataType

**Description**

Enumerates the data types.

**System capability**: SystemCapability.Multimedia.ImageEffect.Core

**Since**: 12

| Enum Item | Description |
| :-- | :-- |
| EFFECT\_DATA\_TYPE\_UNKNOWN = 0 | Undefined. |
| EFFECT\_DATA\_TYPE\_INT32 = 1 | Integer. |
| EFFECT\_DATA\_TYPE\_FLOAT = 2 | Single-precision floating point. |
| EFFECT\_DATA\_TYPE\_DOUBLE = 3 | Double-precision floating point. |
| EFFECT\_DATA\_TYPE\_CHAR = 4 | Byte. |
| EFFECT\_DATA\_TYPE\_LONG = 5 | Long integer. |
| EFFECT\_DATA\_TYPE\_BOOL = 6 | Boolean. |
| EFFECT\_DATA\_TYPE\_PTR = 7 | Pointer. |

#### \[h2\]ImageEffect\_Format

enum ImageEffect\_Format

**Description**

Enumerates the pixel formats.

**System capability**: SystemCapability.Multimedia.ImageEffect.Core

**Since**: 12

| Enum Item | Description |
| :-- | :-- |
| EFFECT\_PIXEL\_FORMAT\_UNKNOWN = 0 | Undefined. |
| EFFECT\_PIXEL\_FORMAT\_RGBA8888 = 1 | RGBA8888. |
| EFFECT\_PIXEL\_FORMAT\_NV21 = 2 | NV21. |
| EFFECT\_PIXEL\_FORMAT\_NV12 = 3 | NV12. |
| EFFECT\_PIXEL\_FORMAT\_RGBA1010102 = 4 | 10-bit RGBA. |
| EFFECT\_PIXEL\_FORMAT\_YCBCR\_P010 = 5 | 10-bit YCBCR420. |
| EFFECT\_PIXEL\_FORMAT\_YCRCB\_P010 = 6 | 10-bit YCRCB420. |

#### \[h2\]ImageEffect\_BufferType

enum ImageEffect\_BufferType

**Description**

Enumerates the buffer types.

**System capability**: SystemCapability.Multimedia.ImageEffect.Core

**Since**: 12

| Enum Item | Description |
| :-- | :-- |
| EFFECT\_BUFFER\_TYPE\_UNKNOWN = 0 | Undefined. |
| EFFECT\_BUFFER\_TYPE\_PIXEL = 1 | Pixel image type. |
| EFFECT\_BUFFER\_TYPE\_TEXTURE = 2 | Texture type. |

#### Function Description

#### \[h2\]OH\_EffectFilterInfo\_Create()

OH\_EffectFilterInfo \*OH\_EffectFilterInfo\_Create()

**Description**

Creates an OH\_EffectFilterInfo instance. The instance must be released by calling [OH\_EffectFilterInfo\_Release](#oh_effectfilterinfo_release) when it is no longer needed.

**System capability**: SystemCapability.Multimedia.ImageEffect.Core

**Since**: 12

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_EffectFilterInfo](../../structs/oh-effectfilterinfo/document.md) \* | Pointer to the OH\_EffectFilterInfo instance created. If the operation fails, a null pointer is returned. |

#### \[h2\]OH\_EffectFilterInfo\_SetFilterName()

ImageEffect\_ErrorCode OH\_EffectFilterInfo\_SetFilterName(OH\_EffectFilterInfo \*info, const char \*name)

**Description**

Sets a filter name.

**System capability**: SystemCapability.Multimedia.ImageEffect.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_EffectFilterInfo](../../structs/oh-effectfilterinfo/document.md) \*info | Pointer to the filter information. |
| const char \*name | Pointer to the filter name, for example, **OH\_EFFECT\_BRIGHTNESS\_FILTER**. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ImageEffect\_ErrorCode](../image-effect-errors-h/document.md#imageeffect_errorcode) | 
**EFFECT\_SUCCESS**: The function is successfully called.

**EFFECT\_ERROR\_PARAM\_INVALID**: A parameter is a null pointer.

 |

#### \[h2\]OH\_EffectFilterInfo\_GetFilterName()

ImageEffect\_ErrorCode OH\_EffectFilterInfo\_GetFilterName(OH\_EffectFilterInfo \*info, char \*\*name)

**Description**

Obtains a filter name.

**System capability**: SystemCapability.Multimedia.ImageEffect.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_EffectFilterInfo](../../structs/oh-effectfilterinfo/document.md) \*info | Pointer to the filter information. |
| char \*\*name | Double pointer to the char array holding the filter name. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ImageEffect\_ErrorCode](../image-effect-errors-h/document.md#imageeffect_errorcode) | 
**EFFECT\_SUCCESS**: The function is successfully called.

**EFFECT\_ERROR\_PARAM\_INVALID**: A parameter is a null pointer.

 |

#### \[h2\]OH\_EffectFilterInfo\_SetSupportedBufferTypes()

ImageEffect\_ErrorCode OH\_EffectFilterInfo\_SetSupportedBufferTypes(OH\_EffectFilterInfo \*info, uint32\_t size, ImageEffect\_BufferType \*bufferTypeArray)

**Description**

Sets the buffer types supported by a filter.

**System capability**: SystemCapability.Multimedia.ImageEffect.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_EffectFilterInfo](../../structs/oh-effectfilterinfo/document.md) \*info | Pointer to the filter information. |
| uint32\_t size | Number of buffer types supported, each of which is [ImageEffect\_BufferType](#imageeffect_buffertype). |
| [ImageEffect\_BufferType](#imageeffect_buffertype) \*bufferTypeArray | Pointer to the array holding the buffer types supported, each of which is [ImageEffect\_BufferType](#imageeffect_buffertype). |

**Returns**

| Type | Description |
| :-- | :-- |
| [ImageEffect\_ErrorCode](../image-effect-errors-h/document.md#imageeffect_errorcode) | 
**EFFECT\_SUCCESS**: The function is successfully called.

**EFFECT\_ERROR\_PARAM\_INVALID**: A parameter is a null pointer.

 |

#### \[h2\]OH\_EffectFilterInfo\_GetSupportedBufferTypes()

ImageEffect\_ErrorCode OH\_EffectFilterInfo\_GetSupportedBufferTypes(OH\_EffectFilterInfo \*info, uint32\_t \*size, ImageEffect\_BufferType \*\*bufferTypeArray)

**Description**

Obtains the buffer types supported by a filter.

**System capability**: SystemCapability.Multimedia.ImageEffect.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_EffectFilterInfo](../../structs/oh-effectfilterinfo/document.md) \*info | Pointer to the filter information. |
| uint32\_t \*size | Number of buffer types supported, each of which is [ImageEffect\_BufferType](#imageeffect_buffertype). |
| [ImageEffect\_BufferType](#imageeffect_buffertype) \*\*bufferTypeArray | Double pointer to the array holding the buffer types supported, each of which is [ImageEffect\_BufferType](#imageeffect_buffertype). |

**Returns**

| Type | Description |
| :-- | :-- |
| [ImageEffect\_ErrorCode](../image-effect-errors-h/document.md#imageeffect_errorcode) | 
**EFFECT\_SUCCESS**: The function is successfully called.

**EFFECT\_ERROR\_PARAM\_INVALID**: A parameter is a null pointer.

 |

#### \[h2\]OH\_EffectFilterInfo\_SetSupportedFormats()

ImageEffect\_ErrorCode OH\_EffectFilterInfo\_SetSupportedFormats(OH\_EffectFilterInfo \*info, uint32\_t size, ImageEffect\_Format \*formatArray)

**Description**

Sets the pixel formats supported by a filter.

**System capability**: SystemCapability.Multimedia.ImageEffect.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_EffectFilterInfo](../../structs/oh-effectfilterinfo/document.md) \*info | Pointer to the filter information. |
| uint32\_t size | Number of pixel formats supported, each of which is [ImageEffect\_Format](#imageeffect_format). |
| [ImageEffect\_Format](#imageeffect_format) \*formatArray | Pointer to the array holding the pixel formats supported, each of which is [ImageEffect\_Format](#imageeffect_format). |

**Returns**

| Type | Description |
| :-- | :-- |
| [ImageEffect\_ErrorCode](../image-effect-errors-h/document.md#imageeffect_errorcode) | 
**EFFECT\_SUCCESS**: The function is successfully called.

**EFFECT\_ERROR\_PARAM\_INVALID**: A parameter is a null pointer.

 |

#### \[h2\]OH\_EffectFilterInfo\_GetSupportedFormats()

ImageEffect\_ErrorCode OH\_EffectFilterInfo\_GetSupportedFormats(OH\_EffectFilterInfo \*info, uint32\_t \*size, ImageEffect\_Format \*\*formatArray)

**Description**

Obtains the pixel formats supported by a filter.

**System capability**: SystemCapability.Multimedia.ImageEffect.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_EffectFilterInfo](../../structs/oh-effectfilterinfo/document.md) \*info | Pointer to the filter information. |
| uint32\_t \*size | Pointer to the number of pixel formats supported, each of which is [ImageEffect\_Format](#imageeffect_format). |
| [ImageEffect\_Format](#imageeffect_format) \*\*formatArray | Double pointer to the array holding the pixel formats supported, each of which is [ImageEffect\_Format](#imageeffect_format). |

**Returns**

| Type | Description |
| :-- | :-- |
| [ImageEffect\_ErrorCode](../image-effect-errors-h/document.md#imageeffect_errorcode) | 
**EFFECT\_SUCCESS**: The function is successfully called.

**EFFECT\_ERROR\_PARAM\_INVALID**: A parameter is a null pointer.

 |

#### \[h2\]OH\_EffectFilterInfo\_Release()

ImageEffect\_ErrorCode OH\_EffectFilterInfo\_Release(OH\_EffectFilterInfo \*info)

**Description**

Destroys an OH\_EffectFilterInfo instance.

**System capability**: SystemCapability.Multimedia.ImageEffect.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_EffectFilterInfo](../../structs/oh-effectfilterinfo/document.md) \*info | Pointer to the filter information. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ImageEffect\_ErrorCode](../image-effect-errors-h/document.md#imageeffect_errorcode) | 
**EFFECT\_SUCCESS**: The function is successfully called.

**EFFECT\_ERROR\_PARAM\_INVALID**: A parameter is a null pointer.

 |

#### \[h2\]OH\_EffectBufferInfo\_Create()

OH\_EffectBufferInfo \*OH\_EffectBufferInfo\_Create()

**Description**

Creates an OH\_EffectBufferInfo instance. The instance must be released by calling [OH\_EffectBufferInfo\_Release](#oh_effectbufferinfo_release) when it is no longer needed.

**System capability**: SystemCapability.Multimedia.ImageEffect.Core

**Since**: 12

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_EffectBufferInfo](../../structs/oh-effectbufferinfo/document.md) \* | Pointer to the OH\_EffectBufferInfo instance created. If the operation fails, a null pointer is returned. |

#### \[h2\]OH\_EffectBufferInfo\_SetAddr()

ImageEffect\_ErrorCode OH\_EffectBufferInfo\_SetAddr(OH\_EffectBufferInfo \*info, void \*addr)

**Description**

Sets the address of an effect buffer.

**System capability**: SystemCapability.Multimedia.ImageEffect.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_EffectBufferInfo](../../structs/oh-effectbufferinfo/document.md) \*info | Pointer to the image information. |
| void \*addr | Pointer to the virtual address of the image buffer. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ImageEffect\_ErrorCode](../image-effect-errors-h/document.md#imageeffect_errorcode) | 
**EFFECT\_SUCCESS**: The function is successfully called.

**EFFECT\_ERROR\_PARAM\_INVALID**: A parameter is a null pointer.

 |

#### \[h2\]OH\_EffectBufferInfo\_GetAddr()

ImageEffect\_ErrorCode OH\_EffectBufferInfo\_GetAddr(OH\_EffectBufferInfo \*info, void \*\*addr)

**Description**

Obtains the address of an effect buffer.

**System capability**: SystemCapability.Multimedia.ImageEffect.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_EffectBufferInfo](../../structs/oh-effectbufferinfo/document.md) \*info | Pointer to the image information. |
| void \*\*addr | Double pointer to the virtual address of the image buffer. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ImageEffect\_ErrorCode](../image-effect-errors-h/document.md#imageeffect_errorcode) | 
**EFFECT\_SUCCESS**: The function is successfully called.

**EFFECT\_ERROR\_PARAM\_INVALID**: A parameter is a null pointer.

 |

#### \[h2\]OH\_EffectBufferInfo\_SetWidth()

ImageEffect\_ErrorCode OH\_EffectBufferInfo\_SetWidth(OH\_EffectBufferInfo \*info, int32\_t width)

**Description**

Sets the image width.

**System capability**: SystemCapability.Multimedia.ImageEffect.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_EffectBufferInfo](../../structs/oh-effectbufferinfo/document.md) \*info | Pointer to the image information. |
| int32\_t width | Image width, in px. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ImageEffect\_ErrorCode](../image-effect-errors-h/document.md#imageeffect_errorcode) | 
**EFFECT\_SUCCESS**: The function is successfully called.

**EFFECT\_ERROR\_PARAM\_INVALID**: A parameter is a null pointer.

 |

#### \[h2\]OH\_EffectBufferInfo\_GetWidth()

ImageEffect\_ErrorCode OH\_EffectBufferInfo\_GetWidth(OH\_EffectBufferInfo \*info, int32\_t \*width)

**Description**

Obtains the image width.

**System capability**: SystemCapability.Multimedia.ImageEffect.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_EffectBufferInfo](../../structs/oh-effectbufferinfo/document.md) \*info | Pointer to the image information. |
| int32\_t \*width | Pointer to the image width, in px. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ImageEffect\_ErrorCode](../image-effect-errors-h/document.md#imageeffect_errorcode) | 
**EFFECT\_SUCCESS**: The function is successfully called.

**EFFECT\_ERROR\_PARAM\_INVALID**: A parameter is a null pointer.

 |

#### \[h2\]OH\_EffectBufferInfo\_SetHeight()

ImageEffect\_ErrorCode OH\_EffectBufferInfo\_SetHeight(OH\_EffectBufferInfo \*info, int32\_t height)

**Description**

Sets the image height.

**System capability**: SystemCapability.Multimedia.ImageEffect.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_EffectBufferInfo](../../structs/oh-effectbufferinfo/document.md) \*info | Pointer to the image information. |
| int32\_t height | Image height, in px. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ImageEffect\_ErrorCode](../image-effect-errors-h/document.md#imageeffect_errorcode) | 
**EFFECT\_SUCCESS**: The function is successfully called.

**EFFECT\_ERROR\_PARAM\_INVALID**: A parameter is a null pointer.

 |

#### \[h2\]OH\_EffectBufferInfo\_GetHeight()

ImageEffect\_ErrorCode OH\_EffectBufferInfo\_GetHeight(OH\_EffectBufferInfo \*info, int32\_t \*height)

**Description**

Obtains the image height.

**System capability**: SystemCapability.Multimedia.ImageEffect.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_EffectBufferInfo](../../structs/oh-effectbufferinfo/document.md) \*info | Pointer to the image information. |
| int32\_t \*height | Pointer to the image height, in px. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ImageEffect\_ErrorCode](../image-effect-errors-h/document.md#imageeffect_errorcode) | 
**EFFECT\_SUCCESS**: The function is successfully called.

**EFFECT\_ERROR\_PARAM\_INVALID**: A parameter is a null pointer.

 |

#### \[h2\]OH\_EffectBufferInfo\_SetRowSize()

ImageEffect\_ErrorCode OH\_EffectBufferInfo\_SetRowSize(OH\_EffectBufferInfo \*info, int32\_t rowSize)

**Description**

Sets the number of bytes per row for an image.

**System capability**: SystemCapability.Multimedia.ImageEffect.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_EffectBufferInfo](../../structs/oh-effectbufferinfo/document.md) \*info | Pointer to the image information. |
| int32\_t rowSize | Number of bytes per row, in bytes. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ImageEffect\_ErrorCode](../image-effect-errors-h/document.md#imageeffect_errorcode) | 
**EFFECT\_SUCCESS**: The function is successfully called.

**EFFECT\_ERROR\_PARAM\_INVALID**: A parameter is a null pointer.

 |

#### \[h2\]OH\_EffectBufferInfo\_GetRowSize()

ImageEffect\_ErrorCode OH\_EffectBufferInfo\_GetRowSize(OH\_EffectBufferInfo \*info, int32\_t \*rowSize)

**Description**

Obtains the number of bytes per row of an image.

**System capability**: SystemCapability.Multimedia.ImageEffect.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_EffectBufferInfo](../../structs/oh-effectbufferinfo/document.md) \*info | Pointer to the image information. |
| int32\_t \*rowSize | Pointer to the number of bytes per row, in bytes. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ImageEffect\_ErrorCode](../image-effect-errors-h/document.md#imageeffect_errorcode) | 
**EFFECT\_SUCCESS**: The function is successfully called.

**EFFECT\_ERROR\_PARAM\_INVALID**: A parameter is a null pointer.

 |

#### \[h2\]OH\_EffectBufferInfo\_SetEffectFormat()

ImageEffect\_ErrorCode OH\_EffectBufferInfo\_SetEffectFormat(OH\_EffectBufferInfo \*info, ImageEffect\_Format format)

**Description**

Sets the pixel format for an image.

**System capability**: SystemCapability.Multimedia.ImageEffect.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_EffectBufferInfo](../../structs/oh-effectbufferinfo/document.md) \*info | Pointer to the image information. |
| [ImageEffect\_Format](#imageeffect_format) format | Pixel format. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ImageEffect\_ErrorCode](../image-effect-errors-h/document.md#imageeffect_errorcode) | 
**EFFECT\_SUCCESS**: The function is successfully called.

**EFFECT\_ERROR\_PARAM\_INVALID**: A parameter is a null pointer.

 |

#### \[h2\]OH\_EffectBufferInfo\_GetEffectFormat()

ImageEffect\_ErrorCode OH\_EffectBufferInfo\_GetEffectFormat(OH\_EffectBufferInfo \*info, ImageEffect\_Format \*format)

**Description**

Obtains the pixel format of an image.

**System capability**: SystemCapability.Multimedia.ImageEffect.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_EffectBufferInfo](../../structs/oh-effectbufferinfo/document.md) \*info | Pointer to the image information. |
| [ImageEffect\_Format](#imageeffect_format) \*format | Pointer to the pixel format. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ImageEffect\_ErrorCode](../image-effect-errors-h/document.md#imageeffect_errorcode) | 
**EFFECT\_SUCCESS**: The function is successfully called.

**EFFECT\_ERROR\_PARAM\_INVALID**: A parameter is a null pointer.

 |

#### \[h2\]OH\_EffectBufferInfo\_SetTextureId()

ImageEffect\_ErrorCode OH\_EffectBufferInfo\_SetTextureId(OH\_EffectBufferInfo \*info, int32\_t textureId)

**Description**

Sets the texture ID of the image for an OH\_EffectBufferInfo struct.

**System capability**: SystemCapability.Multimedia.ImageEffect.Core

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_EffectBufferInfo](../../structs/oh-effectbufferinfo/document.md) \*info | Pointer to an instance of the OH\_EffectBufferInfo struct. |
| int32\_t textureId | Texture ID of the image. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ImageEffect\_ErrorCode](../image-effect-errors-h/document.md#imageeffect_errorcode) | 
**EFFECT\_SUCCESS**: The function is successfully called.

**EFFECT\_ERROR\_PARAM\_INVALID**: A parameter is missing.

 |

#### \[h2\]OH\_EffectBufferInfo\_GetTextureId()

ImageEffect\_ErrorCode OH\_EffectBufferInfo\_GetTextureId(OH\_EffectBufferInfo \*info, int32\_t \*textureId)

**Description**

Obtains the texture ID of an image from an OH\_EffectBufferInfo struct.

**System capability**: SystemCapability.Multimedia.ImageEffect.Core

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_EffectBufferInfo](../../structs/oh-effectbufferinfo/document.md) \*info | Pointer to an instance of the OH\_EffectBufferInfo struct. |
| int32\_t \*textureId | Pointer to the texture ID of the image. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ImageEffect\_ErrorCode](../image-effect-errors-h/document.md#imageeffect_errorcode) | 
**EFFECT\_SUCCESS**: The function is successfully called.

**EFFECT\_ERROR\_PARAM\_INVALID**: A parameter is missing.

 |

#### \[h2\]OH\_EffectBufferInfo\_Release()

ImageEffect\_ErrorCode OH\_EffectBufferInfo\_Release(OH\_EffectBufferInfo \*info)

**Description**

Destroys an OH\_EffectBufferInfo instance.

**System capability**: SystemCapability.Multimedia.ImageEffect.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_EffectBufferInfo](../../structs/oh-effectbufferinfo/document.md) \*info | Pointer to the image information. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ImageEffect\_ErrorCode](../image-effect-errors-h/document.md#imageeffect_errorcode) | 
**EFFECT\_SUCCESS**: The function is successfully called.

**EFFECT\_ERROR\_PARAM\_INVALID**: A parameter is a null pointer.

 |

#### \[h2\]OH\_EffectFilterDelegate\_SetValue()

typedef bool (\*OH\_EffectFilterDelegate\_SetValue)(OH\_EffectFilter \*filter, const char \*key, const ImageEffect\_Any \*value)

**Description**

Defines a pointer to the callback function for setting parameters of a custom filter. It is used to verify parameters and parameter values.

**System capability**: SystemCapability.Multimedia.ImageEffect.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_EffectFilter](../../structs/oh-effectfilter/document.md) \*filter | Pointer to the filter. |
| const char \*key | Pointer to the key of a filter parameter. |
| [const ImageEffect\_Any](../../structs/imageeffect-any/document.md) \*value | Pointer to the value of the filter parameter. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | 
**true**: The parameter is valid.

**false**: The parameter is invalid.

 |

#### \[h2\]OH\_EffectFilterDelegate\_PushData()

typedef void (\*OH\_EffectFilterDelegate\_PushData)(OH\_EffectFilter \*filter, OH\_EffectBufferInfo \*info)

**Description**

Defines a pointer to the callback function used by a custom filter to push image data to the next-level filter. The function pointer must be actively called in the callback of [OH\_EffectFilterDelegate\_Render](#oh_effectfilterdelegate_render).

**System capability**: SystemCapability.Multimedia.ImageEffect.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_EffectFilter](../../structs/oh-effectfilter/document.md) \*filter | Pointer to the filter. |
| [OH\_EffectBufferInfo](../../structs/oh-effectbufferinfo/document.md) \*info | Pointer to the buffer information, which is **OH\_EffectBufferInfo**. |

#### \[h2\]OH\_EffectFilterDelegate\_Render()

typedef bool (\*OH\_EffectFilterDelegate\_Render)(OH\_EffectFilter \*filter, OH\_EffectBufferInfo \*info, OH\_EffectFilterDelegate\_PushData pushData)

**Description**

Defines a pointer to the callback function for rendering an image using a custom filter.

**System capability**: SystemCapability.Multimedia.ImageEffect.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_EffectFilter](../../structs/oh-effectfilter/document.md) \*filter | Pointer to the filter. |
| [OH\_EffectBufferInfo](../../structs/oh-effectbufferinfo/document.md) \*info | Pointer to the buffer information, which is **OH\_EffectBufferInfo**. |
| [OH\_EffectFilterDelegate\_PushData](#oh_effectfilterdelegate_pushdata) pushData | Callback function **OH\_EffectFilterDelegate\_PushData** used by the custom filter to push image data to the next-level filter. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | 
**true**: The operation is successful.

**false**: The operation fails.

 |

#### \[h2\]OH\_EffectFilterDelegate\_Save()

typedef bool (\*OH\_EffectFilterDelegate\_Save)(OH\_EffectFilter \*filter, char \*\*info)

**Description**

Defines a pointer to the callback function for serializing a custom filter. Filters are serialized in JSON format.

**System capability**: SystemCapability.Multimedia.ImageEffect.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_EffectFilter](../../structs/oh-effectfilter/document.md) \*filter | Pointer to the filter. |
| char \*\*info | Double pointer to a char array holding a serialized JSON string. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | 
**true**: The operation is successful.

**false**: The operation fails.

 |

#### \[h2\]OH\_EffectFilterDelegate\_Restore()

typedef OH\_EffectFilter \*(\*OH\_EffectFilterDelegate\_Restore)(const char \*info)

**Description**

Defines a pointer to the callback function for deserializing a custom filter.

**System capability**: SystemCapability.Multimedia.ImageEffect.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const char \*info | Pointer to a serialized JSON string. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_EffectFilter](../../structs/oh-effectfilter/document.md) \* | OH\_EffectFilter instance. If the operation fails, a null pointer is returned. |

#### \[h2\]OH\_EffectFilter\_Create()

OH\_EffectFilter \*OH\_EffectFilter\_Create(const char \*name)

**Description**

Creates an OH\_EffectFilter instance. The instance must be released by calling [OH\_EffectFilter\_Release](#oh_effectfilter_release) when it is no longer needed.

**System capability**: SystemCapability.Multimedia.ImageEffect.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const char \*name | Pointer to the filter name, for example, **OH\_EFFECT\_BRIGHTNESS\_FILTER**. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_EffectFilter](../../structs/oh-effectfilter/document.md) \* | Pointer to the OH\_EffectFilter instance created. If the operation fails, a null pointer is returned. |

#### \[h2\]OH\_EffectFilter\_SetValue()

ImageEffect\_ErrorCode OH\_EffectFilter\_SetValue(OH\_EffectFilter \*filter, const char \*key, const ImageEffect\_Any \*value)

**Description**

Sets a filter parameter.

**System capability**: SystemCapability.Multimedia.ImageEffect.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_EffectFilter](../../structs/oh-effectfilter/document.md) \*filter | Pointer to the filter. |
| const char \*key | Pointer to the key of the filter parameter, for example, **OH\_EFFECT\_FILTER\_INTENSITY\_KEY**. |
| [const ImageEffect\_Any](../../structs/imageeffect-any/document.md) \*value | Pointer to the value of the filter parameter. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ImageEffect\_ErrorCode](../image-effect-errors-h/document.md#imageeffect_errorcode) | 
**EFFECT\_SUCCESS**: The function is successfully called.

**EFFECT\_ERROR\_PARAM\_INVALID**: A parameter is a null pointer.

**EFFECT\_KEY\_ERROR**: A parameter is invalid.

**EFFECT\_PARAM\_ERROR**: A parameter value is invalid.

 |

#### \[h2\]OH\_EffectFilter\_GetValue()

ImageEffect\_ErrorCode OH\_EffectFilter\_GetValue(OH\_EffectFilter \*filter, const char \*key, ImageEffect\_Any \*value)

**Description**

Obtains a filter parameter.

**System capability**: SystemCapability.Multimedia.ImageEffect.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_EffectFilter](../../structs/oh-effectfilter/document.md) \*filter | Pointer to the filter. |
| const char \*key | Pointer to the key of the filter parameter, for example, **OH\_EFFECT\_FILTER\_INTENSITY\_KEY**. |
| [ImageEffect\_Any](../../structs/imageeffect-any/document.md) \*value | Pointer to the value of the filter parameter. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ImageEffect\_ErrorCode](../image-effect-errors-h/document.md#imageeffect_errorcode) | 
**EFFECT\_SUCCESS**: The function is successfully called.

**EFFECT\_ERROR\_PARAM\_INVALID**: A parameter is a null pointer.

**EFFECT\_KEY\_ERROR**: A parameter is invalid.

 |

#### \[h2\]OH\_EffectFilter\_Register()

ImageEffect\_ErrorCode OH\_EffectFilter\_Register(const OH\_EffectFilterInfo \*info, const ImageEffect\_FilterDelegate \*delegate)

**Description**

Registers a custom filter.

**System capability**: SystemCapability.Multimedia.ImageEffect.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [const OH\_EffectFilterInfo](../../structs/oh-effectfilterinfo/document.md) \*info | Pointer to the filter information, which is **OH\_EffectFilterInfo**. |
| [const ImageEffect\_FilterDelegate](../../structs/imageeffect-filterdelegate/document.md) \*delegate | Pointer to the callback function **ImageEffect\_FilterDelegate** of the filter. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ImageEffect\_ErrorCode](../image-effect-errors-h/document.md#imageeffect_errorcode) | 
**EFFECT\_SUCCESS**: The function is successfully called.

**EFFECT\_ERROR\_PARAM\_INVALID**: A parameter is a null pointer.

 |

#### \[h2\]OH\_EffectFilter\_LookupFilters()

ImageEffect\_FilterNames \*OH\_EffectFilter\_LookupFilters(const char \*key)

**Description**

Obtains filters that meet given conditions.

**System capability**: SystemCapability.Multimedia.ImageEffect.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const char \*key | Pointer to the conditions. You can use the keyword **Default** to obtain all filters. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ImageEffect\_FilterNames](../../structs/imageeffect-filternames/document.md) \* | Pointer to a list of filter names. |

#### \[h2\]OH\_EffectFilter\_ReleaseFilterNames()

void OH\_EffectFilter\_ReleaseFilterNames()

**Description**

Releases filter name memory resources.

**System capability**: SystemCapability.Multimedia.ImageEffect.Core

**Since**: 12

#### \[h2\]OH\_EffectFilter\_LookupFilterInfo()

ImageEffect\_ErrorCode OH\_EffectFilter\_LookupFilterInfo(const char \*name, OH\_EffectFilterInfo \*info)

**Description**

Obtains the filter information.

**System capability**: SystemCapability.Multimedia.ImageEffect.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const char \*name | Pointer to the filter name. |
| [OH\_EffectFilterInfo](../../structs/oh-effectfilterinfo/document.md) \*info | Pointer to the filter information, which is **OH\_EffectFilterInfo**. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ImageEffect\_ErrorCode](../image-effect-errors-h/document.md#imageeffect_errorcode) | 
**EFFECT\_SUCCESS**: The function is successfully called.

**EFFECT\_ERROR\_PARAM\_INVALID**: A parameter is a null pointer or an invalid value.

 |

#### \[h2\]OH\_EffectFilter\_Render()

ImageEffect\_ErrorCode OH\_EffectFilter\_Render(OH\_EffectFilter \*filter, OH\_PixelmapNative \*inputPixelmap, OH\_PixelmapNative \*outputPixelmap)

**Description**

Starts image rendering.

**System capability**: SystemCapability.Multimedia.ImageEffect.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_EffectFilter](../../structs/oh-effectfilter/document.md) \*filter | Pointer to the filter. |
| [OH\_PixelmapNative](../../structs/oh-pixelmapnative/document.md) \*inputPixelmap | Pointer to the input image. |
| [OH\_PixelmapNative](../../structs/oh-pixelmapnative/document.md) \*outputPixelmap | Pointer to the output image. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ImageEffect\_ErrorCode](../image-effect-errors-h/document.md#imageeffect_errorcode) | 
**EFFECT\_SUCCESS**: The function is successfully called.

**EFFECT\_ERROR\_PARAM\_INVALID**: A parameter is a null pointer.

 |

#### \[h2\]OH\_EffectFilter\_RenderWithTextureId()

ImageEffect\_ErrorCode OH\_EffectFilter\_RenderWithTextureId(OH\_EffectFilter \*filter, int32\_t inputTextureId, int32\_t outputTextureId, int32\_t colorSpace)

**Description**

Applies the filter effect using texture IDs. This function does not support using the same texture for both input and output.

**System capability**: SystemCapability.Multimedia.ImageEffect.Core

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_EffectFilter](../../structs/oh-effectfilter/document.md) \*filter | Pointer to an instance of the OH\_EffectFilter struct. |
| int32\_t inputTextureId | ID of the input texture. This ID must be valid and bound to a texture of the GL\_TEXTURE\_2D type. |
| int32\_t outputTextureId | 
ID of the output texture. This ID must be valid.

If it is not bound to a texture, it will automatically be bound to a GL\_TEXTURE\_2D type.

If the texture is already bound and the size is inappropriate, the rendered result may be cropped or partially filled into this texture.

 |
| int32\_t colorSpace | Color space of the image. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ImageEffect\_ErrorCode](../image-effect-errors-h/document.md#imageeffect_errorcode) | 
**EFFECT\_SUCCESS**: The function is successfully called.

**EFFECT\_ERROR\_PARAM\_INVALID**: A parameter is missing.

 |

#### \[h2\]OH\_EffectFilter\_Release()

ImageEffect\_ErrorCode OH\_EffectFilter\_Release(OH\_EffectFilter \*filter)

**Description**

Destroys an OH\_EffectFilter instance.

**System capability**: SystemCapability.Multimedia.ImageEffect.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_EffectFilter](../../structs/oh-effectfilter/document.md) \*filter | Pointer to the filter. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ImageEffect\_ErrorCode](../image-effect-errors-h/document.md#imageeffect_errorcode) | 
**EFFECT\_SUCCESS**: The function is successfully called.

**EFFECT\_ERROR\_PARAM\_INVALID**: A parameter is a null pointer.

 |

#### \[h2\]OH\_EffectBufferInfo\_SetTimestamp()

ImageEffect\_ErrorCode OH\_EffectBufferInfo\_SetTimestamp(OH\_EffectBufferInfo \*info, int64\_t timestamp)

**Description**

Sets the filter timestamp.

**System capability**: SystemCapability.Multimedia.ImageEffect.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_EffectBufferInfo](../../structs/oh-effectbufferinfo/document.md) \*info | Pointer to the image information. |
| int64\_t timestamp | Timestamp of the image frame data. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ImageEffect\_ErrorCode](../image-effect-errors-h/document.md#imageeffect_errorcode) | 
**EFFECT\_SUCCESS**: The function is successfully called.

**EFFECT\_ERROR\_PARAM\_INVALID**: A parameter is a null pointer.

 |

#### \[h2\]OH\_EffectBufferInfo\_GetTimestamp()

ImageEffect\_ErrorCode OH\_EffectBufferInfo\_GetTimestamp(OH\_EffectBufferInfo \*info, int64\_t \*timestamp)

**Description**

Obtains the filter timestamp.

**System capability**: SystemCapability.Multimedia.ImageEffect.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_EffectBufferInfo](../../structs/oh-effectbufferinfo/document.md) \*info | Pointer to the image information. |
| int64\_t \*timestamp | Pointer to the timestamp of the image frame data. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ImageEffect\_ErrorCode](../image-effect-errors-h/document.md#imageeffect_errorcode) | 
**EFFECT\_SUCCESS**: The function is successfully called.

**EFFECT\_ERROR\_PARAM\_INVALID**: A parameter is a null pointer.

 |
