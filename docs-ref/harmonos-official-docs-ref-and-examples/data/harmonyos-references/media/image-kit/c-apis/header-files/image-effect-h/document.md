# image\_effect.h

#### Overview

The file declares the APIs related to an image effector.

You can use the APIs to add, delete, and query image effect filters. You can connect multiple filters in series to implement complex effect adjustment.

The effector supports multiple input types, such as PixelMap, URI, surface, and picture. Different input types are converted into buffer objects in the effector, and effect processing is implemented through the filters.

**File to include**: <multimedia/image\_effect/image\_effect.h>

**Library**: libimage\_effect.so

**System capability**: SystemCapability.Multimedia.ImageEffect.Core

**Since**: 12

**Related module**: [ImageEffect](../../modules/imageeffect/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_ImageEffect](../../structs/oh-imageeffect/document.md) | OH\_ImageEffect | Describes the image effector. |

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [OH\_ImageEffect \*OH\_ImageEffect\_Create(const char \*name)](#oh_imageeffect_create) | Creates an OH\_ImageEffect instance. The instance must be released by calling [OH\_ImageEffect\_Release](#oh_imageeffect_release) when it is no longer needed. |
| [OH\_EffectFilter \*OH\_ImageEffect\_AddFilter(OH\_ImageEffect \*imageEffect, const char \*filterName)](#oh_imageeffect_addfilter) | Adds a filter. |
| [ImageEffect\_ErrorCode OH\_ImageEffect\_AddFilterByFilter(OH\_ImageEffect \*imageEffect, OH\_EffectFilter \*filter)](#oh_imageeffect_addfilterbyfilter) | Adds a specified filter. |
| [OH\_EffectFilter \*OH\_ImageEffect\_InsertFilter(OH\_ImageEffect \*imageEffect, uint32\_t index, const char \*filterName)](#oh_imageeffect_insertfilter) | Inserts a filter. |
| [ImageEffect\_ErrorCode OH\_ImageEffect\_InsertFilterByFilter(OH\_ImageEffect \*imageEffect, uint32\_t index, OH\_EffectFilter \*filter)](#oh_imageeffect_insertfilterbyfilter) | Inserts a filter to the specified position. |
| [int32\_t OH\_ImageEffect\_RemoveFilter(OH\_ImageEffect \*imageEffect, const char \*filterName)](#oh_imageeffect_removefilter) | Removes a filter. |
| [ImageEffect\_ErrorCode OH\_ImageEffect\_RemoveFilterByIndex(OH\_ImageEffect \*imageEffect, uint32\_t index)](#oh_imageeffect_removefilterbyindex) | Removes a filter from the specified position. |
| [OH\_EffectFilter \*OH\_ImageEffect\_ReplaceFilter(OH\_ImageEffect \*imageEffect, uint32\_t index, const char \*filterName)](#oh_imageeffect_replacefilter) | Replaces a filter. |
| [ImageEffect\_ErrorCode OH\_ImageEffect\_ReplaceFilterByFilter(OH\_ImageEffect \*imageEffect, uint32\_t index, OH\_EffectFilter \*filter)](#oh_imageeffect_replacefilterbyfilter) | Replaces a filter at the specified position. |
| [int32\_t OH\_ImageEffect\_GetFilterCount(OH\_ImageEffect \*imageEffect)](#oh_imageeffect_getfiltercount) | Obtains the number of added filters. |
| [OH\_EffectFilter \*OH\_ImageEffect\_GetFilter(OH\_ImageEffect \*imageEffect, uint32\_t index)](#oh_imageeffect_getfilter) | Obtains the information about a filter. |
| [ImageEffect\_ErrorCode OH\_ImageEffect\_Configure(OH\_ImageEffect \*imageEffect, const char \*key, const ImageEffect\_Any \*value)](#oh_imageeffect_configure) | Configures an image effector. |
| [ImageEffect\_ErrorCode OH\_ImageEffect\_SetOutputSurface(OH\_ImageEffect \*imageEffect, OHNativeWindow \*nativeWindow)](#oh_imageeffect_setoutputsurface) | Sets an output surface. |
| [ImageEffect\_ErrorCode OH\_ImageEffect\_GetInputSurface(OH\_ImageEffect \*imageEffect, OHNativeWindow \*\*nativeWindow)](#oh_imageeffect_getinputsurface) | Obtains an input surface. |
| [ImageEffect\_ErrorCode OH\_ImageEffect\_SetInputPixelmap(OH\_ImageEffect \*imageEffect, OH\_PixelmapNative \*pixelmap)](#oh_imageeffect_setinputpixelmap) | Sets an input PixelMap. |
| [ImageEffect\_ErrorCode OH\_ImageEffect\_SetOutputPixelmap(OH\_ImageEffect \*imageEffect, OH\_PixelmapNative \*pixelmap)](#oh_imageeffect_setoutputpixelmap) | Sets an output PixelMap. |
| [ImageEffect\_ErrorCode OH\_ImageEffect\_SetInputNativeBuffer(OH\_ImageEffect \*imageEffect, OH\_NativeBuffer \*nativeBuffer)](#oh_imageeffect_setinputnativebuffer) | Sets an input native buffer. |
| [ImageEffect\_ErrorCode OH\_ImageEffect\_SetOutputNativeBuffer(OH\_ImageEffect \*imageEffect, OH\_NativeBuffer \*nativeBuffer)](#oh_imageeffect_setoutputnativebuffer) | Sets an output native buffer. |
| [ImageEffect\_ErrorCode OH\_ImageEffect\_SetInputUri(OH\_ImageEffect \*imageEffect, const char \*uri)](#oh_imageeffect_setinputuri) | Sets an input URI. |
| [ImageEffect\_ErrorCode OH\_ImageEffect\_SetOutputUri(OH\_ImageEffect \*imageEffect, const char \*uri)](#oh_imageeffect_setoutputuri) | Sets an output URI. |
| [ImageEffect\_ErrorCode OH\_ImageEffect\_SetInputPicture(OH\_ImageEffect \*imageEffect, OH\_PictureNative \*picture)](#oh_imageeffect_setinputpicture) | Sets an input picture. |
| [ImageEffect\_ErrorCode OH\_ImageEffect\_SetOutputPicture(OH\_ImageEffect \*imageEffect, OH\_PictureNative \*picture)](#oh_imageeffect_setoutputpicture) | Sets an output picture. |
| [ImageEffect\_ErrorCode OH\_ImageEffect\_SetInputTextureId(OH\_ImageEffect \*imageEffect, int32\_t textureId,int32\_t colorSpace)](#oh_imageeffect_setinputtextureid) | Sets the ID of the input texture that contains the image information. |
| [ImageEffect\_ErrorCode OH\_ImageEffect\_SetOutputTextureId(OH\_ImageEffect \*imageEffect, int32\_t textureId)](#oh_imageeffect_setoutputtextureid) | Sets the ID of the output texture that contains the rendered image information. |
| [ImageEffect\_ErrorCode OH\_ImageEffect\_Start(OH\_ImageEffect \*imageEffect)](#oh_imageeffect_start) | Starts an image effector. |
| [ImageEffect\_ErrorCode OH\_ImageEffect\_Stop(OH\_ImageEffect \*imageEffect)](#oh_imageeffect_stop) | Stops an image effector. |
| [ImageEffect\_ErrorCode OH\_ImageEffect\_Release(OH\_ImageEffect \*imageEffect)](#oh_imageeffect_release) | Releases an OH\_ImageEffect instance. |
| [ImageEffect\_ErrorCode OH\_ImageEffect\_Save(OH\_ImageEffect \*imageEffect, char \*\*info)](#oh_imageeffect_save) | Serializes an image effector. |
| [OH\_ImageEffect \*OH\_ImageEffect\_Restore(const char \*info)](#oh_imageeffect_restore) | Deserializes an image effector. |

#### Function Description

#### \[h2\]OH\_ImageEffect\_Create()

OH\_ImageEffect \*OH\_ImageEffect\_Create(const char \*name)

**Description**

Creates an OH\_ImageEffect instance. The instance must be released by calling [OH\_ImageEffect\_Release](#oh_imageeffect_release) when it is no longer needed.

**System capability**: SystemCapability.Multimedia.ImageEffect.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const char \*name | Pointer to the image effector name, which is used to identify the effector and can be customized. You are advised to set it to a non-empty string. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_ImageEffect](../../structs/oh-imageeffect/document.md) \* | Pointer to the OH\_ImageEffect instance created. If the operation fails, a null pointer is returned. |

#### \[h2\]OH\_ImageEffect\_AddFilter()

OH\_EffectFilter \*OH\_ImageEffect\_AddFilter(OH\_ImageEffect \*imageEffect, const char \*filterName)

**Description**

Adds a filter.

**System capability**: SystemCapability.Multimedia.ImageEffect.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_ImageEffect](../../structs/oh-imageeffect/document.md) \*imageEffect | Pointer to the image effector. |
| const char \*filterName | Pointer to the filter name. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_EffectFilter](../../structs/oh-effectfilter/document.md) \* | Pointer to the OH\_EffectFilter instance created. If the effector is invalid, a null pointer is returned. |

#### \[h2\]OH\_ImageEffect\_AddFilterByFilter()

ImageEffect\_ErrorCode OH\_ImageEffect\_AddFilterByFilter(OH\_ImageEffect \*imageEffect, OH\_EffectFilter \*filter)

**Description**

Adds a specified filter.

**System capability**: SystemCapability.Multimedia.ImageEffect.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_ImageEffect](../../structs/oh-imageeffect/document.md) \*imageEffect | Pointer to the image effector. |
| [OH\_EffectFilter](../../structs/oh-effectfilter/document.md) \*filter | Pointer to the filter. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ImageEffect\_ErrorCode](../image-effect-errors-h/document.md#imageeffect_errorcode) | 
**EFFECT\_SUCCESS**: The function is successfully called.

**EFFECT\_ERROR\_PARAM\_INVALID**: A parameter is a null pointer.

 |

#### \[h2\]OH\_ImageEffect\_InsertFilter()

OH\_EffectFilter \*OH\_ImageEffect\_InsertFilter(OH\_ImageEffect \*imageEffect, uint32\_t index, const char \*filterName)

**Description**

Inserts a filter.

**System capability**: SystemCapability.Multimedia.ImageEffect.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_ImageEffect](../../structs/oh-imageeffect/document.md) \*imageEffect | Pointer to the image effector. |
| uint32\_t index | Index of the filter. |
| const char \*filterName | Pointer to the filter name. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_EffectFilter](../../structs/oh-effectfilter/document.md) \* | Pointer to the OH\_EffectFilter instance created. If the operation fails, a null pointer is returned. |

#### \[h2\]OH\_ImageEffect\_InsertFilterByFilter()

ImageEffect\_ErrorCode OH\_ImageEffect\_InsertFilterByFilter(OH\_ImageEffect \*imageEffect, uint32\_t index,OH\_EffectFilter \*filter)

**Description**

Inserts a filter to the specified position.

**System capability**: SystemCapability.Multimedia.ImageEffect.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_ImageEffect](../../structs/oh-imageeffect/document.md) \*imageEffect | Pointer to the image effector. |
| uint32\_t index | Index of the filter. |
| [OH\_EffectFilter](../../structs/oh-effectfilter/document.md) \*filter | Pointer to the filter. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ImageEffect\_ErrorCode](../image-effect-errors-h/document.md#imageeffect_errorcode) | 
**EFFECT\_SUCCESS**: The function is successfully called.

**EFFECT\_ERROR\_PARAM\_INVALID**: A parameter is a null pointer.

 |

#### \[h2\]OH\_ImageEffect\_RemoveFilter()

int32\_t OH\_ImageEffect\_RemoveFilter(OH\_ImageEffect \*imageEffect, const char \*filterName)

**Description**

Removes a filter.

**System capability**: SystemCapability.Multimedia.ImageEffect.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_ImageEffect](../../structs/oh-imageeffect/document.md) \*imageEffect | Pointer to the image effector. |
| const char \*filterName | Pointer to the filter name. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | Number of filters. |

#### \[h2\]OH\_ImageEffect\_RemoveFilterByIndex()

ImageEffect\_ErrorCode OH\_ImageEffect\_RemoveFilterByIndex(OH\_ImageEffect \*imageEffect, uint32\_t index)

**Description**

Removes a filter from the specified position.

**System capability**: SystemCapability.Multimedia.ImageEffect.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_ImageEffect](../../structs/oh-imageeffect/document.md) \*imageEffect | Pointer to the image effector. |
| uint32\_t index | Index of the filter. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ImageEffect\_ErrorCode](../image-effect-errors-h/document.md#imageeffect_errorcode) | 
**EFFECT\_SUCCESS**: The function is successfully called.

**EFFECT\_ERROR\_PARAM\_INVALID**: A parameter is a null pointer.

 |

#### \[h2\]OH\_ImageEffect\_ReplaceFilter()

OH\_EffectFilter \*OH\_ImageEffect\_ReplaceFilter(OH\_ImageEffect \*imageEffect, uint32\_t index, const char \*filterName)

**Description**

Replaces a filter.

**System capability**: SystemCapability.Multimedia.ImageEffect.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_ImageEffect](../../structs/oh-imageeffect/document.md) \*imageEffect | Pointer to the image effector. |
| const char \*filterName | Pointer to the filter name. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_EffectFilter](../../structs/oh-effectfilter/document.md) \* | Pointer to the OH\_EffectFilter instance created. If the operation fails, a null pointer is returned. |

#### \[h2\]OH\_ImageEffect\_ReplaceFilterByFilter()

ImageEffect\_ErrorCode OH\_ImageEffect\_ReplaceFilterByFilter(OH\_ImageEffect \*imageEffect, uint32\_t index, OH\_EffectFilter \*filter)

**Description**

Replaces a filter at the specified position.

**System capability**: SystemCapability.Multimedia.ImageEffect.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_ImageEffect](../../structs/oh-imageeffect/document.md) \*imageEffect | Pointer to the image effector. |
| uint32\_t index | Index of the filter. |
| [OH\_EffectFilter](../../structs/oh-effectfilter/document.md) \*filter | Pointer to the filter. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ImageEffect\_ErrorCode](../image-effect-errors-h/document.md#imageeffect_errorcode) | 
**EFFECT\_SUCCESS**: The function is successfully called.

**EFFECT\_ERROR\_PARAM\_INVALID**: A parameter is a null pointer.

 |

#### \[h2\]OH\_ImageEffect\_GetFilterCount()

int32\_t OH\_ImageEffect\_GetFilterCount(OH\_ImageEffect \*imageEffect)

**Description**

Obtains the number of added filters.

**System capability**: SystemCapability.Multimedia.ImageEffect.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_ImageEffect](../../structs/oh-imageeffect/document.md) \*imageEffect | Pointer to the image effector. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | Number of filters. |

#### \[h2\]OH\_ImageEffect\_GetFilter()

OH\_EffectFilter \*OH\_ImageEffect\_GetFilter(OH\_ImageEffect \*imageEffect, uint32\_t index)

**Description**

Obtains the information about a filter.

**System capability**: SystemCapability.Multimedia.ImageEffect.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_ImageEffect](../../structs/oh-imageeffect/document.md) \*imageEffect | Pointer to the image effector. |
| uint32\_t index | Index of the filter. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_EffectFilter](../../structs/oh-effectfilter/document.md) \* | Pointer to the OH\_EffectFilter instance created. If the operation fails, a null pointer is returned. |

#### \[h2\]OH\_ImageEffect\_Configure()

ImageEffect\_ErrorCode OH\_ImageEffect\_Configure(OH\_ImageEffect \*imageEffect, const char \*key,const ImageEffect\_Any \*value)

**Description**

Configures an image effector.

**System capability**: SystemCapability.Multimedia.ImageEffect.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_ImageEffect](../../structs/oh-imageeffect/document.md) \*imageEffect | Pointer to the image effector. |
| const char \*key | Pointer to the key of a configuration parameter. |
| [const ImageEffect\_Any](../../structs/imageeffect-any/document.md) \*value | Pointer to the value of a configuration parameter. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ImageEffect\_ErrorCode](../image-effect-errors-h/document.md#imageeffect_errorcode) | 
**EFFECT\_SUCCESS**: The function is successfully called.

**EFFECT\_ERROR\_PARAM\_INVALID**: A parameter is a null pointer.

**EFFECT\_KEY\_ERROR**: A parameter is invalid.

**EFFECT\_PARAM\_ERROR**: A parameter value is invalid.

 |

#### \[h2\]OH\_ImageEffect\_SetOutputSurface()

ImageEffect\_ErrorCode OH\_ImageEffect\_SetOutputSurface(OH\_ImageEffect \*imageEffect, OHNativeWindow \*nativeWindow)

**Description**

Sets an output surface.

**System capability**: SystemCapability.Multimedia.ImageEffect.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_ImageEffect](../../structs/oh-imageeffect/document.md) \*imageEffect | Pointer to the image effector. |
| OHNativeWindow \*nativeWindow | Pointer to the OHNativeWindow instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ImageEffect\_ErrorCode](../image-effect-errors-h/document.md#imageeffect_errorcode) | 
**EFFECT\_SUCCESS**: The function is successfully called.

**EFFECT\_ERROR\_PARAM\_INVALID**: A parameter is a null pointer.

 |

#### \[h2\]OH\_ImageEffect\_GetInputSurface()

ImageEffect\_ErrorCode OH\_ImageEffect\_GetInputSurface(OH\_ImageEffect \*imageEffect, OHNativeWindow \*\*nativeWindow)

**Description**

Obtains an input surface.

**System capability**: SystemCapability.Multimedia.ImageEffect.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_ImageEffect](../../structs/oh-imageeffect/document.md) \*imageEffect | Pointer to the image effector. |
| OHNativeWindow \*\*nativeWindow | Double pointer to the OHNativeWindow instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ImageEffect\_ErrorCode](../image-effect-errors-h/document.md#imageeffect_errorcode) | 
**EFFECT\_SUCCESS**: The function is successfully called.

**EFFECT\_ERROR\_PARAM\_INVALID**: A parameter is a null pointer.

 |

#### \[h2\]OH\_ImageEffect\_SetInputPixelmap()

ImageEffect\_ErrorCode OH\_ImageEffect\_SetInputPixelmap(OH\_ImageEffect \*imageEffect, OH\_PixelmapNative \*pixelmap)

**Description**

Sets an input PixelMap.

**System capability**: SystemCapability.Multimedia.ImageEffect.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_ImageEffect](../../structs/oh-imageeffect/document.md) \*imageEffect | Pointer to the image effector. |
| [OH\_PixelmapNative](../../structs/oh-pixelmapnative/document.md) \*pixelmap | Pointer to the OH\_PixelmapNative instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ImageEffect\_ErrorCode](../image-effect-errors-h/document.md#imageeffect_errorcode) | 
**EFFECT\_SUCCESS**: The function is successfully called.

**EFFECT\_ERROR\_PARAM\_INVALID**: A parameter is a null pointer.

 |

#### \[h2\]OH\_ImageEffect\_SetOutputPixelmap()

ImageEffect\_ErrorCode OH\_ImageEffect\_SetOutputPixelmap(OH\_ImageEffect \*imageEffect, OH\_PixelmapNative \*pixelmap)

**Description**

Sets an output PixelMap.

**System capability**: SystemCapability.Multimedia.ImageEffect.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_ImageEffect](../../structs/oh-imageeffect/document.md) \*imageEffect | Pointer to the image effector. |
| [OH\_PixelmapNative](../../structs/oh-pixelmapnative/document.md) \*pixelmap | Pointer to the OH\_PixelmapNative instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ImageEffect\_ErrorCode](../image-effect-errors-h/document.md#imageeffect_errorcode) | 
**EFFECT\_SUCCESS**: The function is successfully called.

**EFFECT\_ERROR\_PARAM\_INVALID**: A parameter is a null pointer.

**EFFECT\_PARAM\_ERROR**: The call fails because of abnormal parameters.

 |

#### \[h2\]OH\_ImageEffect\_SetInputNativeBuffer()

ImageEffect\_ErrorCode OH\_ImageEffect\_SetInputNativeBuffer(OH\_ImageEffect \*imageEffect, OH\_NativeBuffer \*nativeBuffer)

**Description**

Sets an input native buffer.

**System capability**: SystemCapability.Multimedia.ImageEffect.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_ImageEffect](../../structs/oh-imageeffect/document.md) \*imageEffect | Pointer to the image effector. |
| [OH\_NativeBuffer](../../../../../graphics/arkgraphics-2d/c-apis/structs/oh-nativebuffer/document.md) \*nativeBuffer | Pointer to the OH\_NativeBuffer instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ImageEffect\_ErrorCode](../image-effect-errors-h/document.md#imageeffect_errorcode) | 
**EFFECT\_SUCCESS**: The function is successfully called.

**EFFECT\_ERROR\_PARAM\_INVALID**: A parameter is a null pointer.

 |

#### \[h2\]OH\_ImageEffect\_SetOutputNativeBuffer()

ImageEffect\_ErrorCode OH\_ImageEffect\_SetOutputNativeBuffer(OH\_ImageEffect \*imageEffect, OH\_NativeBuffer \*nativeBuffer)

**Description**

Sets an output native buffer.

**System capability**: SystemCapability.Multimedia.ImageEffect.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_ImageEffect](../../structs/oh-imageeffect/document.md) \*imageEffect | Pointer to the image effector. |
| [OH\_NativeBuffer](../../../../../graphics/arkgraphics-2d/c-apis/structs/oh-nativebuffer/document.md) \*nativeBuffer | Pointer to an OH\_NativeBuffer instance. The value can be NULL. If NULL is passed, the rendering result is returned to the input OH\_NativeBuffer object. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ImageEffect\_ErrorCode](../image-effect-errors-h/document.md#imageeffect_errorcode) | 
**EFFECT\_SUCCESS**: The function is successfully called.

**EFFECT\_ERROR\_PARAM\_INVALID**: A parameter is a null pointer.

**EFFECT\_PARAM\_ERROR**: The call fails because of abnormal parameters.

 |

#### \[h2\]OH\_ImageEffect\_SetInputUri()

ImageEffect\_ErrorCode OH\_ImageEffect\_SetInputUri(OH\_ImageEffect \*imageEffect, const char \*uri)

**Description**

Sets an input URI.

**System capability**: SystemCapability.Multimedia.ImageEffect.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_ImageEffect](../../structs/oh-imageeffect/document.md) \*imageEffect | Pointer to the image effector. |
| const char \*uri | Pointer to the URI of the image. Only JPEG and HEIF images are supported. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ImageEffect\_ErrorCode](../image-effect-errors-h/document.md#imageeffect_errorcode) | 
**EFFECT\_SUCCESS**: The function is successfully called.

**EFFECT\_ERROR\_PARAM\_INVALID**: A parameter is a null pointer.

 |

#### \[h2\]OH\_ImageEffect\_SetOutputUri()

ImageEffect\_ErrorCode OH\_ImageEffect\_SetOutputUri(OH\_ImageEffect \*imageEffect, const char \*uri)

**Description**

Sets an output URI.

**System capability**: SystemCapability.Multimedia.ImageEffect.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_ImageEffect](../../structs/oh-imageeffect/document.md) \*imageEffect | Pointer to the image effector. |
| const char \*uri | Pointer to the URI of the image. The format of the output URI is the same as that of the input URI. If HEIF encoding is not supported, JPEG encoding is used. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ImageEffect\_ErrorCode](../image-effect-errors-h/document.md#imageeffect_errorcode) | 
**EFFECT\_SUCCESS**: The function is successfully called.

**EFFECT\_ERROR\_PARAM\_INVALID**: A parameter is a null pointer.

 |

#### \[h2\]OH\_ImageEffect\_SetInputPicture()

ImageEffect\_ErrorCode OH\_ImageEffect\_SetInputPicture(OH\_ImageEffect \*imageEffect, OH\_PictureNative \*picture)

**Description**

Sets an input picture.

**System capability**: SystemCapability.Multimedia.ImageEffect.Core

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_ImageEffect](../../structs/oh-imageeffect/document.md) \*imageEffect | Pointer to the image effector. |
| [OH\_PictureNative](../../structs/oh-picturenative/document.md) \*picture | Pointer to an OH\_PictureNative instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ImageEffect\_ErrorCode](../image-effect-errors-h/document.md#imageeffect_errorcode) | 
**EFFECT\_SUCCESS**: The function is successfully called.

**EFFECT\_ERROR\_PARAM\_INVALID**: A parameter is a null pointer.

 |

#### \[h2\]OH\_ImageEffect\_SetOutputPicture()

ImageEffect\_ErrorCode OH\_ImageEffect\_SetOutputPicture(OH\_ImageEffect \*imageEffect, OH\_PictureNative \*picture)

**Description**

Sets an output picture.

**System capability**: SystemCapability.Multimedia.ImageEffect.Core

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_ImageEffect](../../structs/oh-imageeffect/document.md) \*imageEffect | Pointer to the image effector. |
| [OH\_PictureNative](../../structs/oh-picturenative/document.md) \*picture | Pointer to an OH\_PictureNative instance. The value can be NULL. If NULL is passed, the rendering result is returned to the input OH\_PictureNative object. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ImageEffect\_ErrorCode](../image-effect-errors-h/document.md#imageeffect_errorcode) | 
**EFFECT\_SUCCESS**: The function is successfully called.

**EFFECT\_ERROR\_PARAM\_INVALID**: A parameter is a null pointer.

**EFFECT\_PARAM\_ERROR**: The call fails because of abnormal parameters.

 |

#### \[h2\]OH\_ImageEffect\_SetInputTextureId()

ImageEffect\_ErrorCode OH\_ImageEffect\_SetInputTextureId(OH\_ImageEffect \*imageEffect, int32\_t textureId,int32\_t colorSpace)

**Description**

Sets the ID of the input texture that contains the image information.

**System capability**: SystemCapability.Multimedia.ImageEffect.Core

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_ImageEffect](../../structs/oh-imageeffect/document.md) \*imageEffect | Pointer to an instance of the OH\_ImageEffect struct. |
| int32\_t textureId | ID of the texture that contains the image information. This ID must be valid and have been bound to a texture of a GL\_TEXTURE\_2D type. |
| int32\_t colorSpace | Color space of the image. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ImageEffect\_ErrorCode](../image-effect-errors-h/document.md#imageeffect_errorcode) | 
**EFFECT\_SUCCESS**: The function is successfully called.

**EFFECT\_ERROR\_PARAM\_INVALID**: A parameter is a null pointer or a parameter value is out of range.

**EFFECT\_PARAM\_ERROR**: A parameter is missing or incorrect.

 |

#### \[h2\]OH\_ImageEffect\_SetOutputTextureId()

ImageEffect\_ErrorCode OH\_ImageEffect\_SetOutputTextureId(OH\_ImageEffect \*imageEffect, int32\_t textureId)

**Description**

Sets the ID of the output texture that contains the rendered image information.

**System capability**: SystemCapability.Multimedia.ImageEffect.Core

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_ImageEffect](../../structs/oh-imageeffect/document.md) \*imageEffect | Pointer to an instance of the OH\_ImageEffect struct. |
| int32\_t textureId | 
ID of the texture that contains the rendered image information. This ID must be valid.

If it is not bound to a texture, it will automatically be bound to a GL\_TEXTURE\_2D type.

If the texture is already bound and the size is inappropriate, the rendered result may be cropped or partially filled into this texture.

 |

**Returns**

| Type | Description |
| :-- | :-- |
| [ImageEffect\_ErrorCode](../image-effect-errors-h/document.md#imageeffect_errorcode) | 
**EFFECT\_SUCCESS**: The function is successfully called.

**EFFECT\_ERROR\_PARAM\_INVALID**: A parameter is a null pointer or a parameter value is out of range.

**EFFECT\_PARAM\_ERROR**: A parameter is missing or incorrect.

 |

#### \[h2\]OH\_ImageEffect\_Start()

ImageEffect\_ErrorCode OH\_ImageEffect\_Start(OH\_ImageEffect \*imageEffect)

**Description**

Starts an image effector.

**System capability**: SystemCapability.Multimedia.ImageEffect.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_ImageEffect](../../structs/oh-imageeffect/document.md) \*imageEffect | Pointer to the image effector. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ImageEffect\_ErrorCode](../image-effect-errors-h/document.md#imageeffect_errorcode) | 
**EFFECT\_SUCCESS**: The function is successfully called.

**EFFECT\_ERROR\_PARAM\_INVALID**: A parameter is a null pointer.

**EFFECT\_INPUT\_OUTPUT\_NOT\_SUPPORTED**: The data types of the input and output images to be processed are different.

**EFFECT\_COLOR\_SPACE\_NOT\_MATCH**: The color spaces of the input and output images do not match.

**EFFECT\_ALLOCATE\_MEMORY\_FAILED**: Memory allocation fails.

 |

#### \[h2\]OH\_ImageEffect\_Stop()

ImageEffect\_ErrorCode OH\_ImageEffect\_Stop(OH\_ImageEffect \*imageEffect)

**Description**

Stops an image effector.

**System capability**: SystemCapability.Multimedia.ImageEffect.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_ImageEffect](../../structs/oh-imageeffect/document.md) \*imageEffect | Pointer to the image effector. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ImageEffect\_ErrorCode](../image-effect-errors-h/document.md#imageeffect_errorcode) | 
**EFFECT\_SUCCESS**: The function is successfully called.

**EFFECT\_ERROR\_PARAM\_INVALID**: A parameter is a null pointer.

 |

#### \[h2\]OH\_ImageEffect\_Release()

ImageEffect\_ErrorCode OH\_ImageEffect\_Release(OH\_ImageEffect \*imageEffect)

**Description**

Releases an OH\_ImageEffect instance.

**System capability**: SystemCapability.Multimedia.ImageEffect.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_ImageEffect](../../structs/oh-imageeffect/document.md) \*imageEffect | Pointer to the image effector. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ImageEffect\_ErrorCode](../image-effect-errors-h/document.md#imageeffect_errorcode) | 
**EFFECT\_SUCCESS**: The function is successfully called.

**EFFECT\_ERROR\_PARAM\_INVALID**: A parameter is a null pointer.

 |

#### \[h2\]OH\_ImageEffect\_Save()

ImageEffect\_ErrorCode OH\_ImageEffect\_Save(OH\_ImageEffect \*imageEffect, char \*\*info)

**Description**

Serializes an image effector.

**System capability**: SystemCapability.Multimedia.ImageEffect.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_ImageEffect](../../structs/oh-imageeffect/document.md) \*imageEffect | Pointer to the image effector. |
| char \*\*info | Double pointer to a char array holding a serialized JSON string. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ImageEffect\_ErrorCode](../image-effect-errors-h/document.md#imageeffect_errorcode) | 
**EFFECT\_SUCCESS**: The function is successfully called.

**EFFECT\_ERROR\_PARAM\_INVALID**: A parameter is a null pointer.

 |

#### \[h2\]OH\_ImageEffect\_Restore()

OH\_ImageEffect \*OH\_ImageEffect\_Restore(const char \*info)

**Description**

Deserializes an image effector.

**System capability**: SystemCapability.Multimedia.ImageEffect.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const char \*info | Pointer to a serialized JSON string. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_ImageEffect](../../structs/oh-imageeffect/document.md) \* | OH\_ImageEffect instance. If the deserialization fails, a null pointer is returned. |
