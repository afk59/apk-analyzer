# drawing\_point.h

#### Overview

This file declares the functions related to the coordinate point in the drawing module.

**File to include**: <native\_drawing/drawing\_point.h>

**Library**: libnative\_drawing.so

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 11

**Related module**: [Drawing](../../modules/drawing/document.md)

#### Summary

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Point\* OH\_Drawing\_PointCreate(float x, float y)](#oh_drawing_pointcreate) | Creates an **OH\_Drawing\_Point** object. |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_PointGetX(const OH\_Drawing\_Point\* point, float\* x)](#oh_drawing_pointgetx) | Obtains the X coordinate of a point. |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_PointGetY(const OH\_Drawing\_Point\* point, float\* y)](#oh_drawing_pointgety) | Obtains the Y coordinate of a point. |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_PointSet(OH\_Drawing\_Point\* point, float x, float y)](#oh_drawing_pointset) | Sets the X and Y coordinates of a point. |
| [void OH\_Drawing\_PointDestroy(OH\_Drawing\_Point\* point)](#oh_drawing_pointdestroy) | Destroys an **OH\_Drawing\_Point** object and reclaims the memory occupied by the object. |

#### Function Description

#### \[h2\]OH\_Drawing\_PointCreate()

OH\_Drawing\_Point\* OH\_Drawing\_PointCreate(float x, float y)

**Description**

Creates an **OH\_Drawing\_Point** object.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| float x | X coordinate of the point. |
| float y | Y coordinate of the point. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_Point](../../structs/oh-drawing-point/document.md)\* | Returns the pointer to the **OH\_Drawing\_Point** object created. |

#### \[h2\]OH\_Drawing\_PointGetX()

OH\_Drawing\_ErrorCode OH\_Drawing\_PointGetX(const OH\_Drawing\_Point\* point, float\* x)

**Description**

Obtains the X coordinate of a point.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [OH\_Drawing\_Point](../../structs/oh-drawing-point/document.md)\* point | Pointer to an [OH\_Drawing\_Point](../../structs/oh-drawing-point/document.md) object. |
| float\* x | Pointer to the X coordinate. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_ErrorCode](../drawing-error-code-h/document.md#oh_drawing_errorcode) | 
Returns one of the following result codes:

**OH\_DRAWING\_SUCCESS** if the operation is successful.

**OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** if either **point** or **x** is NULL.

 |

#### \[h2\]OH\_Drawing\_PointGetY()

OH\_Drawing\_ErrorCode OH\_Drawing\_PointGetY(const OH\_Drawing\_Point\* point, float\* y)

**Description**

Obtains the Y coordinate of a point.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [OH\_Drawing\_Point](../../structs/oh-drawing-point/document.md)\* point | Pointer to an [OH\_Drawing\_Point](../../structs/oh-drawing-point/document.md) object. |
| float\* y | Pointer to the Y coordinate. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_ErrorCode](../drawing-error-code-h/document.md#oh_drawing_errorcode) | 
Returns one of the following result codes:

**OH\_DRAWING\_SUCCESS** if the operation is successful.

**OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** if either **point** or **y** is NULL.

 |

#### \[h2\]OH\_Drawing\_PointSet()

OH\_Drawing\_ErrorCode OH\_Drawing\_PointSet(OH\_Drawing\_Point\* point, float x, float y)

**Description**

Sets the X and Y coordinates of a point.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Point](../../structs/oh-drawing-point/document.md)\* point | Pointer to an [OH\_Drawing\_Point](../../structs/oh-drawing-point/document.md) object. |
| float x | Pointer to the X coordinate. |
| float y | Pointer to the Y coordinate. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_ErrorCode](../drawing-error-code-h/document.md#oh_drawing_errorcode) | 
Returns one of the following result codes:

**OH\_DRAWING\_SUCCESS** if the operation is successful.

**OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** if **point** is NULL.

 |

#### \[h2\]OH\_Drawing\_PointDestroy()

void OH\_Drawing\_PointDestroy(OH\_Drawing\_Point\* point)

**Description**

Destroys an **OH\_Drawing\_Point** object and reclaims the memory occupied by the object.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Point](../../structs/oh-drawing-point/document.md)\* point | Pointer to an **OH\_Drawing\_Point** object. |
