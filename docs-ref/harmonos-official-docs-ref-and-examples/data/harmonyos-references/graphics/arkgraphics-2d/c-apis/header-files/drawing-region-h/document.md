# drawing\_region.h

#### Overview

This file declares the functions related to the region in the drawing module, including creating a region, setting the boundary, and destroying a region.

**File to include**: <native\_drawing/drawing\_region.h>

**Library**: libnative\_drawing.so

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Related module**: [Drawing](../../modules/drawing/document.md)

#### Summary

#### \[h2\]Enumerated value

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_Drawing\_RegionOpMode](#oh_drawing_regionopmode) | OH\_Drawing\_RegionOpMode | Defines an enum for the operation modes available for a region. |

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Region\* OH\_Drawing\_RegionCreate(void)](#oh_drawing_regioncreate) | Creates an **OH\_Drawing\_Region** object for more accurate graphical control. |
| [OH\_Drawing\_Region\* OH\_Drawing\_RegionCopy(const OH\_Drawing\_Region\* region)](#oh_drawing_regioncopy) | Creates a copy of a region object. |
| [bool OH\_Drawing\_RegionContains(OH\_Drawing\_Region\* region, int32\_t x, int32\_t y)](#oh_drawing_regioncontains) | 
Checks whether a region contains the specified point.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **region** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [bool OH\_Drawing\_RegionOp(OH\_Drawing\_Region\* region, const OH\_Drawing\_Region\* other, OH\_Drawing\_RegionOpMode op)](#oh_drawing_regionop) | 

Combines two regions based on the specified operation mode.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **region** or **dst** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

If **op** is not set to one of the enumerated values, **OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE** is returned.

 |
| [bool OH\_Drawing\_RegionSetRect(OH\_Drawing\_Region\* region, const OH\_Drawing\_Rect\* rect)](#oh_drawing_regionsetrect) | 

Sets the boundary for an **OH\_Drawing\_Region** object.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **region** or **rect** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [bool OH\_Drawing\_RegionSetPath(OH\_Drawing\_Region\* region, const OH\_Drawing\_Path\* path, const OH\_Drawing\_Region\* clip)](#oh_drawing_regionsetpath) | 

Sets a region to the area described by the path.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **region**, **path**, or **clip** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [void OH\_Drawing\_RegionDestroy(OH\_Drawing\_Region\* region)](#oh_drawing_regiondestroy) | Destroys an **OH\_Drawing\_Region** object and reclaims the memory occupied by the object. |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_RegionEmpty(OH\_Drawing\_Region\* region)](#oh_drawing_regionempty) | Sets the existing region to empty. |

#### Enum Description

#### \[h2\]OH\_Drawing\_RegionOpMode

enum OH\_Drawing\_RegionOpMode

**Description**

Enumerates the operation modes available for a region.

**Since**: 12

| Value | Description |
| :-- | :-- |
| REGION\_OP\_MODE\_DIFFERENCE | Difference operation. |
| REGION\_OP\_MODE\_INTERSECT | Intersection operation. |
| REGION\_OP\_MODE\_UNION | Union operation. |
| REGION\_OP\_MODE\_XOR | XOR operation. |
| REGION\_OP\_MODE\_REVERSE\_DIFFERENCE | Reverse difference operation. |
| REGION\_OP\_MODE\_REPLACE | Replacement operation. |

#### Function Description

#### \[h2\]OH\_Drawing\_RegionCreate()

OH\_Drawing\_Region\* OH\_Drawing\_RegionCreate(void)

**Description**

Creates an **OH\_Drawing\_Region** object for more accurate graphical control.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_Region](../../structs/oh-drawing-region/document.md)\* | Returns the pointer to the [OH\_Drawing\_Region](../../structs/oh-drawing-region/document.md) object created. |

#### \[h2\]OH\_Drawing\_RegionCopy()

OH\_Drawing\_Region\* OH\_Drawing\_RegionCopy(const OH\_Drawing\_Region\* region)

**Description**

Creates a copy of a region object.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| const [OH\_Drawing\_Region](../../structs/oh-drawing-region/document.md)\* region | Pointer to the [OH\_Drawing\_Region](../../structs/oh-drawing-region/document.md) object to be copied. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_Region](../../structs/oh-drawing-region/document.md)\* | Returns the pointer to the **OH\_Drawing\_Region** object created. |

#### \[h2\]OH\_Drawing\_RegionContains()

bool OH\_Drawing\_RegionContains(OH\_Drawing\_Region\* region, int32\_t x, int32\_t y)

**Description**

Checks whether a region contains the specified point.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **region** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Region](../../structs/oh-drawing-region/document.md)\* region | Pointer to the [OH\_Drawing\_Region](../../structs/oh-drawing-region/document.md) object. |
| int32\_t x | X coordinate of the point. |
| int32\_t y | Y coordinate of the point. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | Returns **true** if the region contains the specified point; returns **false** otherwise. |

#### \[h2\]OH\_Drawing\_RegionOp()

bool OH\_Drawing\_RegionOp(OH\_Drawing\_Region\* region, const OH\_Drawing\_Region\* other, OH\_Drawing\_RegionOpMode op)

**Description**

Combines two regions based on the specified operation mode.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **region** or **dst** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

If **op** is not set to one of the enumerated values, **OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Region](../../structs/oh-drawing-region/document.md)\* region | Pointer to an [OH\_Drawing\_Region](../../structs/oh-drawing-region/document.md) object, in which the resulting region is saved. |
| const [OH\_Drawing\_Region](../../structs/oh-drawing-region/document.md)\* other | Pointer to the [OH\_Drawing\_Region](../../structs/oh-drawing-region/document.md) object. |
| [OH\_Drawing\_RegionOpMode](#oh_drawing_regionopmode) op | Operation mode of the region. For details about the available options, see [OH\_Drawing\_RegionOpMode](#oh_drawing_regionopmode). |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | Returns **true** if the resulting region is not empty; returns false otherwise. |

#### \[h2\]OH\_Drawing\_RegionSetRect()

bool OH\_Drawing\_RegionSetRect(OH\_Drawing\_Region\* region, const OH\_Drawing\_Rect\* rect)

**Description**

Sets the boundary for an **OH\_Drawing\_Region** object.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **region** or **rect** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Region](../../structs/oh-drawing-region/document.md)\* region | Pointer to the [OH\_Drawing\_Region](../../structs/oh-drawing-region/document.md) object. |
| const [OH\_Drawing\_Rect](../../structs/oh-drawing-rect/document.md)\* rect | Pointer to an **OH\_Drawing\_Rect** object. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | Returns **true** if the setting is successful; returns **false** otherwise. |

#### \[h2\]OH\_Drawing\_RegionSetPath()

bool OH\_Drawing\_RegionSetPath(OH\_Drawing\_Region\* region, const OH\_Drawing\_Path\* path, const OH\_Drawing\_Region\* clip)

**Description**

Sets a region to the area described by the path.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **region**, **path**, or **clip** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Region](../../structs/oh-drawing-region/document.md)\* region | Pointer to the [OH\_Drawing\_Region](../../structs/oh-drawing-region/document.md) object. |
| const [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md)\* path | Pointer to the [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md) object. |
| const [OH\_Drawing\_Region](../../structs/oh-drawing-region/document.md)\* clip | Pointer to the [OH\_Drawing\_Region](../../structs/oh-drawing-region/document.md) object. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | Returns **true** if the resulting region is not empty; returns false otherwise. |

#### \[h2\]OH\_Drawing\_RegionDestroy()

void OH\_Drawing\_RegionDestroy(OH\_Drawing\_Region\* region)

**Description**

Destroys an **OH\_Drawing\_Region** object and reclaims the memory occupied by the object.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Region](../../structs/oh-drawing-region/document.md)\* region | Pointer to the [OH\_Drawing\_Region](../../structs/oh-drawing-region/document.md) object. |

#### \[h2\]OH\_Drawing\_RegionEmpty()

OH\_Drawing\_ErrorCode OH\_Drawing\_RegionEmpty(OH\_Drawing\_Region\* region)

**Description**

Sets the existing region to empty.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Region](../../structs/oh-drawing-region/document.md)\* region | Pointer to the [OH\_Drawing\_Region](../../structs/oh-drawing-region/document.md) object. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_ErrorCode](../drawing-error-code-h/document.md#oh_drawing_errorcode) | 
Returns one of the following result codes:

**OH\_DRAWING\_SUCCESS** if the operation is successful.

**OH\_DRAWING\_ERROR\_INCORRECT\_PARAMETER** if the **region** parameter is empty.

 |
