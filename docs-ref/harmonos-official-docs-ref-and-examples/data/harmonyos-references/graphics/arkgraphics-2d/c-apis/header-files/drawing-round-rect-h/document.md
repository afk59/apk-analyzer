# drawing\_round\_rect.h

#### Overview

This file declares the functions related to the rounded rectangle in the drawing module.

**File to include**: <native\_drawing/drawing\_round\_rect.h>

**Library**: libnative\_drawing.so

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 11

**Related module**: [Drawing](../../modules/drawing/document.md)

#### Summary

#### \[h2\]Enumerated value

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_Drawing\_CornerPos](#oh_drawing_cornerpos) | OH\_Drawing\_CornerPos | Defines an enum for the corner positions of a rounded rectangle. |

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_RoundRect\* OH\_Drawing\_RoundRectCreate(const OH\_Drawing\_Rect\* rect, float xRad, float yRad)](#oh_drawing_roundrectcreate) | 
Creates an **OH\_Drawing\_RoundRect** object. This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **rect** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [OH\_Drawing\_RoundRect\* OH\_Drawing\_RoundRectCopy(const OH\_Drawing\_RoundRect\* roundRect)](#oh_drawing_roundrectcopy) | Creates a copy of a rounded rectangle. |
| [void OH\_Drawing\_RoundRectSetCorner(OH\_Drawing\_RoundRect\* roundRect,OH\_Drawing\_CornerPos pos, OH\_Drawing\_Corner\_Radii radii)](#oh_drawing_roundrectsetcorner) | 

Sets the radii of the specified rounded corner in this rounded rectangle.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **roundRect** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [OH\_Drawing\_Corner\_Radii OH\_Drawing\_RoundRectGetCorner(OH\_Drawing\_RoundRect\* roundRect, OH\_Drawing\_CornerPos pos)](#oh_drawing_roundrectgetcorner) | 

Obtains the radii of the specified rounded corner in a rounded rectangle.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **roundRect** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [void OH\_Drawing\_RoundRectDestroy(OH\_Drawing\_RoundRect\* roundRect)](#oh_drawing_roundrectdestroy) | Destroys an **OH\_Drawing\_RoundRect** object and reclaims the memory occupied by the object. |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_RoundRectOffset(OH\_Drawing\_RoundRect\* roundRect, float dx, float dy)](#oh_drawing_roundrectoffset) | Translates a rounded rectangle by an offset along the X axis and Y axis. |

#### Enum Description

#### \[h2\]OH\_Drawing\_CornerPos

enum OH\_Drawing\_CornerPos

**Description**

Defines an enum for the corner positions of a rounded rectangle.

**Since**: 12

| Value | Description |
| :-- | :-- |
| CORNER\_POS\_TOP\_LEFT | Top left corner of the rounded rectangle. |
| CORNER\_POS\_TOP\_RIGHT | Top right corner of the rounded rectangle. |
| CORNER\_POS\_BOTTOM\_RIGHT | Bottom right corner of the rounded rectangle. |
| CORNER\_POS\_BOTTOM\_LEFT | Bottom left corner of the rounded rectangle. |

#### Function Description

#### \[h2\]OH\_Drawing\_RoundRectCreate()

OH\_Drawing\_RoundRect\* OH\_Drawing\_RoundRectCreate(const OH\_Drawing\_Rect\* rect, float xRad, float yRad)

**Description**

Creates an **OH\_Drawing\_RoundRect** object. This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **rect** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| const [OH\_Drawing\_Rect](../../structs/oh-drawing-rect/document.md)\* rect | Pointer to an **OH\_Drawing\_Rect** object. |
| float xRad | Radius of the rounded corner on the X axis. A negative number is invalid. |
| float yRad | Radius of the rounded corner on the Y axis. A negative number is invalid. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_RoundRect](../../structs/oh-drawing-roundrect/document.md)\* | Returns the pointer to the **OH\_Drawing\_RoundRect** object created. |

#### \[h2\]OH\_Drawing\_RoundRectCopy()

OH\_Drawing\_RoundRect\* OH\_Drawing\_RoundRectCopy(const OH\_Drawing\_RoundRect\* roundRect)

**Description**

Creates a copy of a rounded rectangle.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| const [OH\_Drawing\_RoundRect](../../structs/oh-drawing-roundrect/document.md)\* roundRect | Pointer to an [OH\_Drawing\_RoundRect](../../structs/oh-drawing-roundrect/document.md) object. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_RoundRect](../../structs/oh-drawing-roundrect/document.md)\* | Returns the pointer to the new **OH\_Drawing\_RoundRect** object created. |

#### \[h2\]OH\_Drawing\_RoundRectSetCorner()

void OH\_Drawing\_RoundRectSetCorner(OH\_Drawing\_RoundRect\* roundRect,OH\_Drawing\_CornerPos pos, OH\_Drawing\_Corner\_Radii radii)

**Description**

Sets the radii of the specified rounded corner in this rounded rectangle.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **roundRect** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_RoundRect](../../structs/oh-drawing-roundrect/document.md)\* roundRect | Pointer to an **OH\_Drawing\_RoundRect** object. |
| [OH\_Drawing\_CornerPos](#oh_drawing_cornerpos) pos | Position of the rounded corner. For details about the available options, see [OH\_Drawing\_CornerPos](#oh_drawing_cornerpos). |
| [OH\_Drawing\_Corner\_Radii](../../structs/oh-drawing-point2d/document.md) radii | OH\_Drawing\_Corner\_Radii struct, including the radii on the X axis and Y axis. A radius less than or equal to 0 is invalid. |

#### \[h2\]OH\_Drawing\_RoundRectGetCorner()

OH\_Drawing\_Corner\_Radii OH\_Drawing\_RoundRectGetCorner(OH\_Drawing\_RoundRect\* roundRect, OH\_Drawing\_CornerPos pos)

**Description**

Obtains the radii of the specified rounded corner in a rounded rectangle.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **roundRect** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_RoundRect](../../structs/oh-drawing-roundrect/document.md)\* roundRect | Pointer to an **OH\_Drawing\_RoundRect** object. |
| [OH\_Drawing\_CornerPos](#oh_drawing_cornerpos) pos | Position of the rounded corner. For details about the available options, see [OH\_Drawing\_CornerPos](#oh_drawing_cornerpos). |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_Corner\_Radii](../../structs/oh-drawing-point2d/document.md) | Returns an OH\_Drawing\_Corner\_Radii struct, including the radii on the X axis and Y axis. |

#### \[h2\]OH\_Drawing\_RoundRectDestroy()

void OH\_Drawing\_RoundRectDestroy(OH\_Drawing\_RoundRect\* roundRect)

**Description**

Destroys an **OH\_Drawing\_RoundRect** object and reclaims the memory occupied by the object.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_RoundRect](../../structs/oh-drawing-roundrect/document.md)\* roundRect | Pointer to an **OH\_Drawing\_RoundRect** object. |

#### \[h2\]OH\_Drawing\_RoundRectOffset()

OH\_Drawing\_ErrorCode OH\_Drawing\_RoundRectOffset(OH\_Drawing\_RoundRect\* roundRect, float dx, float dy)

**Description**

Translates a rounded rectangle by an offset along the X axis and Y axis.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_RoundRect](../../structs/oh-drawing-roundrect/document.md)\* roundRect | Pointer to an [OH\_Drawing\_Point2D](../../structs/oh-drawing-point2d/document.md) object. |
| float dx | X offset. |
| float dy | Y offset. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_ErrorCode](../drawing-error-code-h/document.md#oh_drawing_errorcode) | 
Returns one of the following result codes:

**OH\_DRAWING\_SUCCESS** if the operation is successful.

**OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** if **roundRect** is NULL.

 |
