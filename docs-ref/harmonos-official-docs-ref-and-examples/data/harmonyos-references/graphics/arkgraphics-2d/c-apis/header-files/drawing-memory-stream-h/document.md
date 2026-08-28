# drawing\_memory\_stream.h

#### Overview

This file declares the functions related to the memory stream in the drawing module.

**File to include**: <native\_drawing/drawing\_memory\_stream.h>

**Library**: libnative\_drawing.so

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Related module**: [Drawing](../../modules/drawing/document.md)

#### Summary

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_MemoryStream\* OH\_Drawing\_MemoryStreamCreate(const void\* data, size\_t length, bool copyData)](#oh_drawing_memorystreamcreate) | 
Creates an **OH\_Drawing\_MemoryStream** object.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **data** is NULL or **length** is **0**, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [void OH\_Drawing\_MemoryStreamDestroy(OH\_Drawing\_MemoryStream\* memoryStream)](#oh_drawing_memorystreamdestroy) | Destroys an **OH\_Drawing\_MemoryStream** object and reclaims the memory occupied by the object. |

#### Function Description

#### \[h2\]OH\_Drawing\_MemoryStreamCreate()

OH\_Drawing\_MemoryStream\* OH\_Drawing\_MemoryStreamCreate(const void\* data, size\_t length, bool copyData)

**Description**

Creates an **OH\_Drawing\_MemoryStream** object.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **data** is NULL or **length** is **0**, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const void\* data | Pointer to the data. |
| size\_t length | Length of the data. |
| bool copyData | Whether to copy data. The value **true** means that the **OH\_Drawing\_MemoryStream** object copies the data, and **false** means that the **OH\_Drawing\_MemoryStream** object directly uses the data without copying. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_MemoryStream](../../structs/oh-drawing-memorystream/document.md)\* | Returns the pointer to the [OH\_Drawing\_MemoryStream](../../structs/oh-drawing-memorystream/document.md) object created. |

#### \[h2\]OH\_Drawing\_MemoryStreamDestroy()

void OH\_Drawing\_MemoryStreamDestroy(OH\_Drawing\_MemoryStream\* memoryStream)

**Description**

Destroys an **OH\_Drawing\_MemoryStream** object and reclaims the memory occupied by the object.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_MemoryStream](../../structs/oh-drawing-memorystream/document.md)\* memoryStream | Pointer to an [OH\_Drawing\_MemoryStream](../../structs/oh-drawing-memorystream/document.md) object. |
