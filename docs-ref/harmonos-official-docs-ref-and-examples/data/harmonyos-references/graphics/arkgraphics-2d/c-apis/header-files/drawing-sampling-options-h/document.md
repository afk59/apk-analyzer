# drawing\_sampling\_options.h

#### Overview

This file declares the functions related to sampling in the drawing module. It is used for image or texture sampling.

**File to include**: <native\_drawing/drawing\_sampling\_options.h>

**Library**: libnative\_drawing.so

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Related module**: [Drawing](../../modules/drawing/document.md)

#### Summary

#### \[h2\]Enumerated value

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_Drawing\_FilterMode](#oh_drawing_filtermode) | OH\_Drawing\_FilterMode | Defines an enum for the filter modes. |
| [OH\_Drawing\_MipmapMode](#oh_drawing_mipmapmode) | OH\_Drawing\_MipmapMode | Defines an enum for the mipmap modes. |

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_SamplingOptions\* OH\_Drawing\_SamplingOptionsCreate(OH\_Drawing\_FilterMode filterMode,OH\_Drawing\_MipmapMode mipmapMode)](#oh_drawing_samplingoptionscreate) | 
Creates an **OH\_Drawing\_SamplingOptions** object.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **mipmapMode** is not set to one of the enumerated values, **OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE** is returned.

 |
| [OH\_Drawing\_SamplingOptions\* OH\_Drawing\_SamplingOptionsCopy(OH\_Drawing\_SamplingOptions\* samplingOptions)](#oh_drawing_samplingoptionscopy) | 

Creates a copy of an [OH\_Drawing\_SamplingOptions](../../structs/oh-drawing-samplingoptions/document.md) object.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **samplingOptions** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [void OH\_Drawing\_SamplingOptionsDestroy(OH\_Drawing\_SamplingOptions\* samplingOptions)](#oh_drawing_samplingoptionsdestroy) | Destroys an **OH\_Drawing\_SamplingOptions** object and reclaims the memory occupied by the object. |

#### Enum Description

#### \[h2\]OH\_Drawing\_FilterMode

enum OH\_Drawing\_FilterMode

**Description**

Defines an enum for the filter modes.

**Since**: 12

| Value | Description |
| :-- | :-- |
| FILTER\_MODE\_NEAREST | Nearest filter mode. |
| FILTER\_MODE\_LINEAR | Linear filter mode. |

#### \[h2\]OH\_Drawing\_MipmapMode

enum OH\_Drawing\_MipmapMode

**Description**

Defines an enum for the mipmap modes.

**Since**: 12

| Value | Description |
| :-- | :-- |
| MIPMAP\_MODE\_NONE | Mipmap level ignored. |
| MIPMAP\_MODE\_NEAREST | Nearest sampling from two adjacent mipmap levels. |
| MIPMAP\_MODE\_LINEAR | Linear interpolation sampling between two adjacent mipmap levels. |

#### Function Description

#### \[h2\]OH\_Drawing\_SamplingOptionsCreate()

OH\_Drawing\_SamplingOptions\* OH\_Drawing\_SamplingOptionsCreate(OH\_Drawing\_FilterMode filterMode,OH\_Drawing\_MipmapMode mipmapMode)

**Description**

Creates an **OH\_Drawing\_SamplingOptions** object.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **mipmapMode** is not set to one of the enumerated values, **OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_FilterMode](#oh_drawing_filtermode) filterMode | Filter sampling mode. |
| [OH\_Drawing\_MipmapMode](#oh_drawing_mipmapmode) mipmapMode | Mipmap mode. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_SamplingOptions](../../structs/oh-drawing-samplingoptions/document.md)\* | Returns a pointer to the created [OH\_Drawing\_SamplingOptions](../../structs/oh-drawing-samplingoptions/document.md) object. |

#### \[h2\]OH\_Drawing\_SamplingOptionsCopy()

OH\_Drawing\_SamplingOptions\* OH\_Drawing\_SamplingOptionsCopy(OH\_Drawing\_SamplingOptions\* samplingOptions)

**Description**

Creates a copy of an [OH\_Drawing\_SamplingOptions](../../structs/oh-drawing-samplingoptions/document.md) object.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **samplingOptions** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_SamplingOptions](../../structs/oh-drawing-samplingoptions/document.md)\* samplingOptions | Pointer to the [OH\_Drawing\_SamplingOptions](../../structs/oh-drawing-samplingoptions/document.md) object. |

**Returns**

| Type | Description |
| :-- | :-- |
| OH\_Drawing\_SamplingOptions\* | Returns a pointer to the created [OH\_Drawing\_SamplingOptions](../../structs/oh-drawing-samplingoptions/document.md) object copy. If NULL is returned, the creation fails. The possible failure cause is that no memory is available or **samplingOptions** is NULL. |

#### \[h2\]OH\_Drawing\_SamplingOptionsDestroy()

void OH\_Drawing\_SamplingOptionsDestroy(OH\_Drawing\_SamplingOptions\* samplingOptions)

**Description**

Destroys an **OH\_Drawing\_SamplingOptions** object and reclaims the memory occupied by the object.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_SamplingOptions](../../structs/oh-drawing-samplingoptions/document.md)\* samplingOptions | Pointer to the [OH\_Drawing\_SamplingOptions](../../structs/oh-drawing-samplingoptions/document.md) object. |
