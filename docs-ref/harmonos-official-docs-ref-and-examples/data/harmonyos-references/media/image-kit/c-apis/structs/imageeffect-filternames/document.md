# ImageEffect\_FilterNames

typedef struct ImageEffect\_FilterDelegate {...} ImageEffect\_FilterNames

#### Overview

The struct describes the filter name information.

**Since**: 12

**Related module**: [ImageEffect](../../modules/imageeffect/document.md)

**Header file**: [image\_effect\_filter.h](../../header-files/image-effect-filter-h/document.md)

#### Summary

#### \[h2\]Member Variables

**The following table lists the declarations supporting C++ syntax.**

| Name | Description |
| :-- | :-- |
| uint32\_t size = 0 | Number of filter names. |
| const char \*\*nameList = nullptr | List of filter names. |

**The following table lists the declarations supporting C syntax.**

| Name | Description |
| :-- | :-- |
| uint32\_t size | Number of filter names. |
| const char \*\*nameList | List of filter names. |

#### \[h2\]Member functions

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_EffectFilterInfo \*OH\_EffectFilterInfo\_Create()](#oh_effectfilterinfo_create) | OH\_EffectFilterInfo\_Create() | 
Creates an OH\_EffectFilterInfo instance. The instance must be released by calling [OH\_EffectFilterInfo\_Release](#oh_effectfilterinfo_release) when it is no longer needed.

**Since**: 12

**System capability**: SystemCapability.Multimedia.ImageEffect.Core

 |
| [ImageEffect\_ErrorCode OH\_EffectFilterInfo\_SetFilterName(OH\_EffectFilterInfo \*info, const char \*name)](#oh_effectfilterinfo_setfiltername) | OH\_EffectFilterInfo\_SetFilterName() | 

Sets a filter name.

**Since**: 12

**System capability**: SystemCapability.Multimedia.ImageEffect.Core

 |
| [ImageEffect\_ErrorCode OH\_EffectFilterInfo\_GetFilterName(OH\_EffectFilterInfo \*info, char \*\*name)](#oh_effectfilterinfo_getfiltername) | OH\_EffectFilterInfo\_GetFilterName() | 

Obtains a filter name.

**Since**: 12

**System capability**: SystemCapability.Multimedia.ImageEffect.Core

 |
| [ImageEffect\_ErrorCode OH\_EffectFilterInfo\_SetSupportedBufferTypes(OH\_EffectFilterInfo \*info, uint32\_t size,ImageEffect\_BufferType \*bufferTypeArray)](#oh_effectfilterinfo_setsupportedbuffertypes) | OH\_EffectFilterInfo\_SetSupportedBufferTypes() | 

Sets the buffer types supported by a filter.

**Since**: 12

**System capability**: SystemCapability.Multimedia.ImageEffect.Core

 |
| [ImageEffect\_ErrorCode OH\_EffectFilterInfo\_GetSupportedBufferTypes(OH\_EffectFilterInfo \*info, uint32\_t \*size,ImageEffect\_BufferType \*\*bufferTypeArray)](#oh_effectfilterinfo_getsupportedbuffertypes) | OH\_EffectFilterInfo\_GetSupportedBufferTypes() | 

Obtains the buffer types supported by a filter.

**Since**: 12

**System capability**: SystemCapability.Multimedia.ImageEffect.Core

 |
| [ImageEffect\_ErrorCode OH\_EffectFilterInfo\_SetSupportedFormats(OH\_EffectFilterInfo \*info, uint32\_t size,ImageEffect\_Format \*formatArray)](#oh_effectfilterinfo_setsupportedformats) | OH\_EffectFilterInfo\_SetSupportedFormats() | 

Sets the pixel formats supported by a filter.

**Since**: 12

**System capability**: SystemCapability.Multimedia.ImageEffect.Core

 |
| [ImageEffect\_ErrorCode OH\_EffectFilterInfo\_GetSupportedFormats(OH\_EffectFilterInfo \*info, uint32\_t \*size,ImageEffect\_Format \*\*formatArray)](#oh_effectfilterinfo_getsupportedformats) | OH\_EffectFilterInfo\_GetSupportedFormats() | 

Obtains the pixel formats supported by a filter.

**Since**: 12

**System capability**: SystemCapability.Multimedia.ImageEffect.Core

 |
| [ImageEffect\_ErrorCode OH\_EffectFilterInfo\_Release(OH\_EffectFilterInfo \*info)](#oh_effectfilterinfo_release) | OH\_EffectFilterInfo\_Release() | 

Destroys an OH\_EffectFilterInfo instance.

**Since**: 12

**System capability**: SystemCapability.Multimedia.ImageEffect.Core

 |

#### Member Function Description

#### \[h2\]OH\_EffectFilterInfo\_Create()

OH\_EffectFilterInfo \*OH\_EffectFilterInfo\_Create()

**Description**

Creates an OH\_EffectFilterInfo instance. The instance must be released by calling [OH\_EffectFilterInfo\_Release](#oh_effectfilterinfo_release) when it is no longer needed.

**System capability**: SystemCapability.Multimedia.ImageEffect.Core

**Since**: 12

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_EffectFilterInfo](../oh-effectfilterinfo/document.md) | Pointer to the OH\_EffectFilterInfo instance created. If the operation fails, a null pointer is returned. |

#### \[h2\]OH\_EffectFilterInfo\_SetFilterName()

ImageEffect\_ErrorCode OH\_EffectFilterInfo\_SetFilterName(OH\_EffectFilterInfo \*info, const char \*name)

**Description**

Sets a filter name.

**System capability**: SystemCapability.Multimedia.ImageEffect.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_EffectFilterInfo](../oh-effectfilterinfo/document.md) \*info | Pointer to the filter information. |
| const char \*name | Pointer to the filter name, for example, **OH\_EFFECT\_BRIGHTNESS\_FILTER**. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ImageEffect\_ErrorCode](../../header-files/image-effect-errors-h/document.md#imageeffect_errorcode) | 
[EFFECT\_SUCCESS](../../header-files/image-effect-errors-h/document.md#imageeffect_errorcode): The function is called successfully.

[EFFECT\_ERROR\_PARAM\_INVALID](../../header-files/image-effect-errors-h/document.md#imageeffect_errorcode): The input parameter is a null pointer.

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
| [OH\_EffectFilterInfo](../oh-effectfilterinfo/document.md) \*info | Pointer to the filter information. |
| char \*\*name | Double pointer to the char array holding the filter name. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ImageEffect\_ErrorCode](../../header-files/image-effect-errors-h/document.md#imageeffect_errorcode) | 
[EFFECT\_SUCCESS](../../header-files/image-effect-errors-h/document.md#imageeffect_errorcode): The function is called successfully.

[EFFECT\_ERROR\_PARAM\_INVALID](../../header-files/image-effect-errors-h/document.md#imageeffect_errorcode): The input parameter is a null pointer.

 |

#### \[h2\]OH\_EffectFilterInfo\_SetSupportedBufferTypes()

ImageEffect\_ErrorCode OH\_EffectFilterInfo\_SetSupportedBufferTypes(OH\_EffectFilterInfo \*info, uint32\_t size,ImageEffect\_BufferType \*bufferTypeArray)

**Description**

Sets the buffer types supported by a filter.

**System capability**: SystemCapability.Multimedia.ImageEffect.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_EffectFilterInfo](../oh-effectfilterinfo/document.md) \*info | Pointer to the filter information. |
| uint32\_t size | Number of buffer types supported, each of which is [ImageEffect\_BufferType](../../header-files/image-effect-filter-h/document.md#imageeffect_buffertype). |
| ImageEffect\_BufferType \*bufferTypeArray | Pointer to the array holding the buffer types supported, each of which is [ImageEffect\_BufferType](../../header-files/image-effect-filter-h/document.md#imageeffect_buffertype). |

**Returns**

| Type | Description |
| :-- | :-- |
| [ImageEffect\_ErrorCode](../../header-files/image-effect-errors-h/document.md#imageeffect_errorcode) | 
[EFFECT\_SUCCESS](../../header-files/image-effect-errors-h/document.md#imageeffect_errorcode): The function is called successfully.

[EFFECT\_ERROR\_PARAM\_INVALID](../../header-files/image-effect-errors-h/document.md#imageeffect_errorcode): The input parameter is a null pointer.

 |

#### \[h2\]OH\_EffectFilterInfo\_GetSupportedBufferTypes()

ImageEffect\_ErrorCode OH\_EffectFilterInfo\_GetSupportedBufferTypes(OH\_EffectFilterInfo \*info, uint32\_t \*size,ImageEffect\_BufferType \*\*bufferTypeArray)

**Description**

Obtains the buffer types supported by a filter.

**System capability**: SystemCapability.Multimedia.ImageEffect.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_EffectFilterInfo](../oh-effectfilterinfo/document.md) \*info | Pointer to the filter information. |
| uint32\_t \*size | Pointer to the number of buffer types supported, each of which is [ImageEffect\_BufferType](../../header-files/image-effect-filter-h/document.md#imageeffect_buffertype). |
| ImageEffect\_BufferType \*\*bufferTypeArray | Double pointer to the array holding the buffer types supported, each of which is [ImageEffect\_BufferType](../../header-files/image-effect-filter-h/document.md#imageeffect_buffertype). |

**Returns**

| Type | Description |
| :-- | :-- |
| [ImageEffect\_ErrorCode](../../header-files/image-effect-errors-h/document.md#imageeffect_errorcode) | 
[EFFECT\_SUCCESS](../../header-files/image-effect-errors-h/document.md#imageeffect_errorcode): The function is called successfully.

[EFFECT\_ERROR\_PARAM\_INVALID](../../header-files/image-effect-errors-h/document.md#imageeffect_errorcode): The input parameter is a null pointer.

 |

#### \[h2\]OH\_EffectFilterInfo\_SetSupportedFormats()

ImageEffect\_ErrorCode OH\_EffectFilterInfo\_SetSupportedFormats(OH\_EffectFilterInfo \*info, uint32\_t size,ImageEffect\_Format \*formatArray)

**Description**

Sets the pixel formats supported by a filter.

**System capability**: SystemCapability.Multimedia.ImageEffect.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_EffectFilterInfo](../oh-effectfilterinfo/document.md) \*info | Pointer to the filter information. |
| uint32\_t size | Number of pixel formats supported, each of which is [ImageEffect\_Format](../../header-files/image-effect-filter-h/document.md#imageeffect_format). |
| ImageEffect\_Format \*formatArray | Pointer to the array holding the pixel formats supported, each of which is [ImageEffect\_Format](../../header-files/image-effect-filter-h/document.md#imageeffect_format). |

**Returns**

| Type | Description |
| :-- | :-- |
| [ImageEffect\_ErrorCode](../../header-files/image-effect-errors-h/document.md#imageeffect_errorcode) | 
[EFFECT\_SUCCESS](../../header-files/image-effect-errors-h/document.md#imageeffect_errorcode): The function is called successfully.

[EFFECT\_ERROR\_PARAM\_INVALID](../../header-files/image-effect-errors-h/document.md#imageeffect_errorcode): The input parameter is a null pointer.

 |

#### \[h2\]OH\_EffectFilterInfo\_GetSupportedFormats()

ImageEffect\_ErrorCode OH\_EffectFilterInfo\_GetSupportedFormats(OH\_EffectFilterInfo \*info, uint32\_t \*size,ImageEffect\_Format \*\*formatArray)

**Description**

Obtains the pixel formats supported by a filter.

**System capability**: SystemCapability.Multimedia.ImageEffect.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_EffectFilterInfo](../oh-effectfilterinfo/document.md) \*info | Pointer to the filter information. |
| uint32\_t \*size | Pointer to the number of pixel formats supported, each of which is [ImageEffect\_Format](../../header-files/image-effect-filter-h/document.md#imageeffect_format). |
| ImageEffect\_Format \*\*formatArray | Double pointer to the array holding the pixel formats supported, each of which is [ImageEffect\_Format](../../header-files/image-effect-filter-h/document.md#imageeffect_format). |

**Returns**

| Type | Description |
| :-- | :-- |
| [ImageEffect\_ErrorCode](../../header-files/image-effect-errors-h/document.md#imageeffect_errorcode) | 
[EFFECT\_SUCCESS](../../header-files/image-effect-errors-h/document.md#imageeffect_errorcode): The function is called successfully.

[EFFECT\_ERROR\_PARAM\_INVALID](../../header-files/image-effect-errors-h/document.md#imageeffect_errorcode): The input parameter is a null pointer.

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
| [OH\_EffectFilterInfo](../oh-effectfilterinfo/document.md) \*info | Pointer to the filter information. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ImageEffect\_ErrorCode](../../header-files/image-effect-errors-h/document.md#imageeffect_errorcode) | 
[EFFECT\_SUCCESS](../../header-files/image-effect-errors-h/document.md#imageeffect_errorcode): The function is called successfully.

[EFFECT\_ERROR\_PARAM\_INVALID](../../header-files/image-effect-errors-h/document.md#imageeffect_errorcode): The input parameter is a null pointer.

 |
