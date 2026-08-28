# drawing\_rect.h

#### Overview

This file declares the functions related to the rectangle in the drawing module.

**File to include**: <native\_drawing/drawing\_rect.h>

**Library**: libnative\_drawing.so

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 11

**Related module**: [Drawing](../../modules/drawing/document.md)

#### Summary

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Rect\* OH\_Drawing\_RectCreate(float left, float top, float right, float bottom)](#oh_drawing_rectcreate) | Creates an **OH\_Drawing\_Rect** object, without sorting the coordinates passed in. This means that the coordinates of the upper left corner of the rectangle can be greater than those of the lower right corner. |
| [bool OH\_Drawing\_RectIntersect(OH\_Drawing\_Rect\* rect, const OH\_Drawing\_Rect\* other)](#oh_drawing_rectintersect) | 
Checks whether two rectangles intersect and if yes, sets **rect** to the area of intersection.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **rect** or **other** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [bool OH\_Drawing\_RectJoin(OH\_Drawing\_Rect\* rect, const OH\_Drawing\_Rect\* other)](#oh_drawing_rectjoin) | 

Obtains the union of two rectangles.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **rect** or **other** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [void OH\_Drawing\_RectSetLeft(OH\_Drawing\_Rect\* rect, float left)](#oh_drawing_rectsetleft) | 

Sets the horizontal coordinate of the upper left corner of a rectangle.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **rect** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [void OH\_Drawing\_RectSetTop(OH\_Drawing\_Rect\* rect, float top)](#oh_drawing_rectsettop) | 

Sets the vertical coordinate of the upper left corner of a rectangle.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **rect** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [void OH\_Drawing\_RectSetRight(OH\_Drawing\_Rect\* rect, float right)](#oh_drawing_rectsetright) | 

Sets the horizontal coordinate of the lower right corner of a rectangle.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **rect** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [void OH\_Drawing\_RectSetBottom(OH\_Drawing\_Rect\* rect, float bottom)](#oh_drawing_rectsetbottom) | 

Sets the vertical coordinate of the lower right corner of a rectangle.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **rect** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [float OH\_Drawing\_RectGetLeft(OH\_Drawing\_Rect\* rect)](#oh_drawing_rectgetleft) | 

Obtains the X coordinate of the upper left corner of a rectangle.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **rect** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [float OH\_Drawing\_RectGetTop(OH\_Drawing\_Rect\* rect)](#oh_drawing_rectgettop) | 

Obtains the Y coordinate of the upper left corner of a rectangle.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **rect** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [float OH\_Drawing\_RectGetRight(OH\_Drawing\_Rect\* rect)](#oh_drawing_rectgetright) | 

Obtains the X coordinate of the lower right corner of a rectangle.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **rect** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [float OH\_Drawing\_RectGetBottom(OH\_Drawing\_Rect\* rect)](#oh_drawing_rectgetbottom) | 

Obtains the Y coordinate of the lower right corner of a rectangle.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **rect** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [float OH\_Drawing\_RectGetHeight(OH\_Drawing\_Rect\* rect)](#oh_drawing_rectgetheight) | 

Obtains the height of a rectangle. The height is calculated by using the Y coordinate of the lower right corner of the rectangle minus the Y coordinate of the upper left corner.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **rect** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [float OH\_Drawing\_RectGetWidth(OH\_Drawing\_Rect\* rect)](#oh_drawing_rectgetwidth) | 

Obtains the width of a rectangle. The width is calculated by using the X coordinate of the lower right corner of the rectangle minus the X coordinate of the upper left corner.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **rect** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [void OH\_Drawing\_RectCopy(OH\_Drawing\_Rect\* src, OH\_Drawing\_Rect\* dst)](#oh_drawing_rectcopy) | 

Copies a source rectangle to create a new one.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **src** or **dst** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [void OH\_Drawing\_RectDestroy(OH\_Drawing\_Rect\* rect)](#oh_drawing_rectdestroy) | Destroys an **OH\_Drawing\_Rect** object and reclaims the memory occupied by the object. |
| [OH\_Drawing\_Array\* OH\_Drawing\_RectCreateArray(size\_t size)](#oh_drawing_rectcreatearray) | Creates a rectangle array object to store multiple rectangle objects. Release this pointer by calling [OH\_Drawing\_RectDestroyArray](#oh_drawing_rectdestroyarray) when this object is no longer needed. |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_RectGetArraySize(OH\_Drawing\_Array\* rectArray, size\_t\* pSize)](#oh_drawing_rectgetarraysize) | Obtains the size of an [OH\_Drawing\_Array](../../structs/oh-drawing-array/document.md) object. |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_RectGetArrayElement(OH\_Drawing\_Array\* rectArray, size\_t index,OH\_Drawing\_Rect\*\* rect)](#oh_drawing_rectgetarrayelement) | Obtains the rectangle with the specified index in a rectangle array. |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_RectDestroyArray(OH\_Drawing\_Array\* rectArray)](#oh_drawing_rectdestroyarray) | Destroys an **OH\_Drawing\_Array** object and reclaims the memory occupied by the object. |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_RectContains(OH\_Drawing\_Rect\* rect, const OH\_Drawing\_Rect\* other, bool\* isContains)](#oh_drawing_rectcontains) | Checks whether a rectangle completely contains another rectangle. |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_RectInset(OH\_Drawing\_Rect\* rect, float left, float top, float right, float bottom)](#oh_drawing_rectinset) | Adds a specified value to the bounds of a rectangle. |

#### Function Description

#### \[h2\]OH\_Drawing\_RectCreate()

OH\_Drawing\_Rect\* OH\_Drawing\_RectCreate(float left, float top, float right, float bottom)

**Description**

Creates an **OH\_Drawing\_Rect** object, without sorting the coordinates passed in. This means that the coordinates of the upper left corner of the rectangle can be greater than those of the lower right corner.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| float left | X coordinate of the upper left corner of the rectangle. |
| float top | Y coordinate of the upper left corner of the rectangle. |
| float right | X coordinate of the lower right corner of the rectangle. |
| float bottom | Y coordinate of the lower right corner of the rectangle. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_Rect](../../structs/oh-drawing-rect/document.md)\* | Returns the pointer to the **OH\_Drawing\_Rect** object created. |

#### \[h2\]OH\_Drawing\_RectIntersect()

bool OH\_Drawing\_RectIntersect(OH\_Drawing\_Rect\* rect, const OH\_Drawing\_Rect\* other)

**Description**

Checks whether two rectangles intersect and if yes, sets **rect** to the area of intersection.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **rect** or **other** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Rect](../../structs/oh-drawing-rect/document.md)\* rect | Pointer to an **OH\_Drawing\_Rect** object. |
| const [OH\_Drawing\_Rect](../../structs/oh-drawing-rect/document.md)\* other | Pointer to an **OH\_Drawing\_Rect** object. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | Returns **true** if they intersect (**rect** is set to the intersection area); returns **false** otherwise (**rect** remains unchanged). |

#### \[h2\]OH\_Drawing\_RectJoin()

bool OH\_Drawing\_RectJoin(OH\_Drawing\_Rect\* rect, const OH\_Drawing\_Rect\* other)

**Description**

Obtains the union of two rectangles.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **rect** or **other** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Rect](../../structs/oh-drawing-rect/document.md)\* rect | Pointer to an **OH\_Drawing\_Rect** object. |
| const [OH\_Drawing\_Rect](../../structs/oh-drawing-rect/document.md)\* other | Pointer to an **OH\_Drawing\_Rect** object. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | Returns **true** if the union is obtained; returns **false** otherwise. The possible failure cause is that at least one of the parameters **rect** and **other** is NULL or the size of the rectangle specified by **other** is empty. |

#### \[h2\]OH\_Drawing\_RectSetLeft()

void OH\_Drawing\_RectSetLeft(OH\_Drawing\_Rect\* rect, float left)

**Description**

Sets the horizontal coordinate of the upper left corner of a rectangle.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **rect** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Rect](../../structs/oh-drawing-rect/document.md)\* rect | Pointer to an **OH\_Drawing\_Rect** object. |
| float left | X coordinate of the upper left corner of the rectangle. |

#### \[h2\]OH\_Drawing\_RectSetTop()

void OH\_Drawing\_RectSetTop(OH\_Drawing\_Rect\* rect, float top)

**Description**

Sets the vertical coordinate of the upper left corner of a rectangle.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **rect** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Rect](../../structs/oh-drawing-rect/document.md)\* rect | Pointer to an **OH\_Drawing\_Rect** object. |
| float top | Y coordinate of the upper left corner of the rectangle. |

#### \[h2\]OH\_Drawing\_RectSetRight()

void OH\_Drawing\_RectSetRight(OH\_Drawing\_Rect\* rect, float right)

**Description**

Sets the horizontal coordinate of the lower right corner of a rectangle.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **rect** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Rect](../../structs/oh-drawing-rect/document.md)\* rect | Pointer to an **OH\_Drawing\_Rect** object. |
| float right | X coordinate of the lower right corner of the rectangle. |

#### \[h2\]OH\_Drawing\_RectSetBottom()

void OH\_Drawing\_RectSetBottom(OH\_Drawing\_Rect\* rect, float bottom)

**Description**

Sets the vertical coordinate of the lower right corner of a rectangle.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **rect** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Rect](../../structs/oh-drawing-rect/document.md)\* rect | Pointer to an **OH\_Drawing\_Rect** object. |
| float bottom | Y coordinate of the lower right corner of the rectangle. |

#### \[h2\]OH\_Drawing\_RectGetLeft()

float OH\_Drawing\_RectGetLeft(OH\_Drawing\_Rect\* rect)

**Description**

Obtains the X coordinate of the upper left corner of a rectangle.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **rect** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Rect](../../structs/oh-drawing-rect/document.md)\* rect | Pointer to an **OH\_Drawing\_Rect** object. |

**Returns**

| Type | Description |
| :-- | :-- |
| float | X coordinate of the upper left corner of the rectangle. |

#### \[h2\]OH\_Drawing\_RectGetTop()

float OH\_Drawing\_RectGetTop(OH\_Drawing\_Rect\* rect)

**Description**

Obtains the Y coordinate of the upper left corner of a rectangle.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **rect** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Rect](../../structs/oh-drawing-rect/document.md)\* rect | Pointer to an **OH\_Drawing\_Rect** object. |

**Returns**

| Type | Description |
| :-- | :-- |
| float | Y coordinate of the upper left corner of the rectangle. |

#### \[h2\]OH\_Drawing\_RectGetRight()

float OH\_Drawing\_RectGetRight(OH\_Drawing\_Rect\* rect)

**Description**

Obtains the X coordinate of the lower right corner of a rectangle.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **rect** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Rect](../../structs/oh-drawing-rect/document.md)\* rect | Pointer to an **OH\_Drawing\_Rect** object. |

**Returns**

| Type | Description |
| :-- | :-- |
| float | X coordinate of the lower right corner of the rectangle. |

#### \[h2\]OH\_Drawing\_RectGetBottom()

float OH\_Drawing\_RectGetBottom(OH\_Drawing\_Rect\* rect)

**Description**

Obtains the Y coordinate of the lower right corner of a rectangle.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **rect** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Rect](../../structs/oh-drawing-rect/document.md)\* rect | Pointer to an **OH\_Drawing\_Rect** object. |

**Returns**

| Type | Description |
| :-- | :-- |
| float | Y coordinate of the lower right corner of the rectangle. |

#### \[h2\]OH\_Drawing\_RectGetHeight()

float OH\_Drawing\_RectGetHeight(OH\_Drawing\_Rect\* rect)

**Description**

Obtains the height of a rectangle. The height is calculated by using the Y coordinate of the lower right corner of the rectangle minus the Y coordinate of the upper left corner.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **rect** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Rect](../../structs/oh-drawing-rect/document.md)\* rect | Pointer to an **OH\_Drawing\_Rect** object. |

**Returns**

| Type | Description |
| :-- | :-- |
| float | Returns the height of the rectangle, in pixels. |

#### \[h2\]OH\_Drawing\_RectGetWidth()

float OH\_Drawing\_RectGetWidth(OH\_Drawing\_Rect\* rect)

**Description**

Obtains the width of a rectangle. The width is calculated by using the X coordinate of the lower right corner of the rectangle minus the X coordinate of the upper left corner.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **rect** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Rect](../../structs/oh-drawing-rect/document.md)\* rect | Pointer to an **OH\_Drawing\_Rect** object. |

**Returns**

| Type | Description |
| :-- | :-- |
| float | Returns the weight of the rectangle, in pixels. |

#### \[h2\]OH\_Drawing\_RectCopy()

void OH\_Drawing\_RectCopy(OH\_Drawing\_Rect\* src, OH\_Drawing\_Rect\* dst)

**Description**

Copies a source rectangle to create a new one.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **src** or **dst** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Rect](../../structs/oh-drawing-rect/document.md)\* src | Pointer to a source rectangle, which is an **OH\_Drawing\_Rect** object. |
| [OH\_Drawing\_Rect](../../structs/oh-drawing-rect/document.md)\* dst | Pointer to a destination rectangle, which is an **OH\_Drawing\_Rect** object. |

#### \[h2\]OH\_Drawing\_RectDestroy()

void OH\_Drawing\_RectDestroy(OH\_Drawing\_Rect\* rect)

**Description**

Destroys an **OH\_Drawing\_Rect** object and reclaims the memory occupied by the object.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Rect](../../structs/oh-drawing-rect/document.md)\* rect | Pointer to an **OH\_Drawing\_Rect** object. |

#### \[h2\]OH\_Drawing\_RectCreateArray()

OH\_Drawing\_Array\* OH\_Drawing\_RectCreateArray(size\_t size)

**Description**

Creates a rectangle array object to store multiple rectangle objects. Release this pointer by calling [OH\_Drawing\_RectDestroyArray](#oh_drawing_rectdestroyarray) when this object is no longer needed.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| size\_t size | Size of the rectangle array. The value cannot exceed 65536, which is the maximum number of glyph indices. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_Array](../../structs/oh-drawing-array/document.md)\* | 
Returns the pointer to the [OH\_Drawing\_Array](../../structs/oh-drawing-array/document.md) object created. If the returned object pointer is null, the creation fails.

Possible causes are that no memory is available or an input parameter is incorrect.

 |

#### \[h2\]OH\_Drawing\_RectGetArraySize()

OH\_Drawing\_ErrorCode OH\_Drawing\_RectGetArraySize(OH\_Drawing\_Array\* rectArray, size\_t\* pSize)

**Description**

Obtains the size of an [OH\_Drawing\_Array](../../structs/oh-drawing-array/document.md) object.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Array](../../structs/oh-drawing-array/document.md)\* rectArray | Pointer to an [OH\_Drawing\_Array](../../structs/oh-drawing-array/document.md) object. |
| size\_t\* pSize | Pointer to the size\_t type, which is used as an output parameter to store the size of the rectangle array. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_ErrorCode](../drawing-error-code-h/document.md#oh_drawing_errorcode) | 
Returns one of the following result codes:

**OH\_DRAWING\_SUCCESS** if the operation is successful.

**OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** if either **rectArray** or **pSize** is NULL.

 |

#### \[h2\]OH\_Drawing\_RectGetArrayElement()

OH\_Drawing\_ErrorCode OH\_Drawing\_RectGetArrayElement(OH\_Drawing\_Array\* rectArray, size\_t index,OH\_Drawing\_Rect\*\* rect)

**Description**

Obtains the rectangle with the specified index in a rectangle array.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Array](../../structs/oh-drawing-array/document.md)\* rectArray | Pointer to an [OH\_Drawing\_Array](../../structs/oh-drawing-array/document.md) object. |
| size\_t index | Index of the rectangle array. |
| [OH\_Drawing\_Rect](../../structs/oh-drawing-rect/document.md)\*\* rect | Double pointer to [OH\_Drawing\_Rect](../../structs/oh-drawing-rect/document.md), which is returned to the caller as an output parameter. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_ErrorCode](../drawing-error-code-h/document.md#oh_drawing_errorcode) | 
Returns one of the following result codes:

**OH\_DRAWING\_SUCCESS** if the operation is successful.

**OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** if **rectArray** or **rect** is null or **index** is out of range.

 |

#### \[h2\]OH\_Drawing\_RectDestroyArray()

OH\_Drawing\_ErrorCode OH\_Drawing\_RectDestroyArray(OH\_Drawing\_Array\* rectArray)

**Description**

Destroys an **OH\_Drawing\_Array** object and reclaims the memory occupied by the object.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Array](../../structs/oh-drawing-array/document.md)\* rectArray | Pointer to an [OH\_Drawing\_Array](../../structs/oh-drawing-array/document.md) object. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_ErrorCode](../drawing-error-code-h/document.md#oh_drawing_errorcode) | 
Returns one of the following result codes:

**OH\_DRAWING\_SUCCESS** if the operation is successful.

**OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** if **rectArray** is NULL.

 |

#### \[h2\]OH\_Drawing\_RectContains()

OH\_Drawing\_ErrorCode OH\_Drawing\_RectContains(OH\_Drawing\_Rect\* rect, const OH\_Drawing\_Rect\* other, bool\* isContains)

**Description**

Checks whether a rectangle completely contains another rectangle.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Rect](../../structs/oh-drawing-rect/document.md)\* rect | Pointer to the [OH\_Drawing\_Rect](../../structs/oh-drawing-rect/document.md) object. This rectangle is used to check whether another rectangle (**other**) is contained. |
| [const OH\_Drawing\_Rect](../../structs/oh-drawing-rect/document.md)\* other | Pointer to the [OH\_Drawing\_Rect](../../structs/oh-drawing-rect/document.md) object. This rectangle is used to check whether it is contained by another rectangle (**rect**). |
| bool\* isContains | Result of whether a rectangle completely contains another rectangle. It is used as an output parameter. **true** indicates that **rect** completely contains **other**. **false** indicates that **rect** does not completely contain **other**. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_ErrorCode](../drawing-error-code-h/document.md#oh_drawing_errorcode) | 
Returns one of the following result codes:

**OH\_DRAWING\_SUCCESS** if the operation is successful.

**OH\_DRAWING\_ERROR\_INCORRECT\_PARAMETER** if the **rect**, **other**, or **isContains** parameter is empty.

 |

#### \[h2\]OH\_Drawing\_RectInset()

OH\_Drawing\_ErrorCode OH\_Drawing\_RectInset(OH\_Drawing\_Rect\* rect, float left, float top, float right, float bottom)

**Description**

Adds a specified value to the bounds of a rectangle.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Rect](../../structs/oh-drawing-rect/document.md)\* rect | Pointer to the [OH\_Drawing\_Rect](../../structs/oh-drawing-rect/document.md) object. |
| float left | Value to be added to the left bound of the rectangle (X coordinate of the upper left corner of the rectangle). |
| float top | Value to be added to the top bound of the rectangle (Y coordinate of the upper left corner of the rectangle). |
| float right | Value to be added to the right bound of the rectangle (X coordinate of the lower right corner of the rectangle). |
| float bottom | Value to be added to the bottom bound of the rectangle (Y coordinate of the lower right corner of the rectangle). |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_ErrorCode](../drawing-error-code-h/document.md#oh_drawing_errorcode) | 
Returns one of the following result codes:

**OH\_DRAWING\_SUCCESS** if the operation is successful.

**OH\_DRAWING\_ERROR\_INCORRECT\_PARAMETER** if the **rect** parameter is empty.

 |
