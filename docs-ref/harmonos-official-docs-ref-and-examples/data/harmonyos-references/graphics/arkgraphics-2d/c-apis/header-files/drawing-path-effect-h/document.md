# drawing\_path\_effect.h

#### Overview

This file declares the functions related to the path effect in the drawing module.

**File to include**: <native\_drawing/drawing\_path\_effect.h>

**Library**: libnative\_drawing.so

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Related module**: [Drawing](../../modules/drawing/document.md)

#### Summary

#### \[h2\]Enumerated value

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_Drawing\_PathDashStyle](#oh_drawing_pathdashstyle) | OH\_Drawing\_PathDashStyle | Defines an enum for the drawing styles for path effects. |

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_PathEffect\* OH\_Drawing\_CreateComposePathEffect(OH\_Drawing\_PathEffect\* outer, OH\_Drawing\_PathEffect\* inner)](#oh_drawing_createcomposepatheffect) | Creates a path effect by sequentially applying the inner effect and then the outer effect. |
| [OH\_Drawing\_PathEffect\* OH\_Drawing\_CreateCornerPathEffect(float radius)](#oh_drawing_createcornerpatheffect) | Creates a path effect that transforms the sharp angle between line segments into a rounded corner with the specified radius. |
| [OH\_Drawing\_PathEffect\* OH\_Drawing\_CreateDashPathEffect(float\* intervals, int count, float phase)](#oh_drawing_createdashpatheffect) | 
Creates a dashed path effect. The dashed line effect is determined by a group of "on" and "off" intervals.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **intervals** is NULL or **count** is less than or equal to 0, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [OH\_Drawing\_PathEffect\* OH\_Drawing\_CreateDiscretePathEffect(float segLength, float deviation)](#oh_drawing_creatediscretepatheffect) | Creates a path effect that segments the path and scatters the segments in an irregular pattern along the path. |
| [OH\_Drawing\_PathEffect\* OH\_Drawing\_CreatePathDashEffect(const OH\_Drawing\_Path\* path, float advance, float phase,OH\_Drawing\_PathDashStyle type)](#oh_drawing_createpathdasheffect) | Creates a dashed path effect. |
| [OH\_Drawing\_PathEffect\* OH\_Drawing\_CreateSumPathEffect(OH\_Drawing\_PathEffect\* firstPathEffect,OH\_Drawing\_PathEffect\* secondPathEffect)](#oh_drawing_createsumpatheffect) | Creates an overlay path effect based on two distinct path effects that take effect separately. |
| [void OH\_Drawing\_PathEffectDestroy(OH\_Drawing\_PathEffect\* pathEffect)](#oh_drawing_patheffectdestroy) | Destroys an **OH\_Drawing\_PathEffect** object and reclaims the memory occupied by the object. |

#### Enum Description

#### \[h2\]OH\_Drawing\_PathDashStyle

enum OH\_Drawing\_PathDashStyle

**Description**

Enumerates the drawing styles for path effects.

**Since**: 18

| Value | Description |
| :-- | :-- |
| DRAWING\_PATH\_DASH\_STYLE\_TRANSLATE | Translation effect. |
| DRAWING\_PATH\_DASH\_STYLE\_ROTATE | Rotation effect. |
| DRAWING\_PATH\_DASH\_STYLE\_MORPH | Morphing effect. |

#### Function Description

#### \[h2\]OH\_Drawing\_CreateComposePathEffect()

OH\_Drawing\_PathEffect\* OH\_Drawing\_CreateComposePathEffect(OH\_Drawing\_PathEffect\* outer, OH\_Drawing\_PathEffect\* inner)

**Description**

Creates a path effect by sequentially applying the inner effect and then the outer effect.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_PathEffect](../../structs/oh-drawing-patheffect/document.md)\* outer | Pointer to an outer effect, which is an [OH\_Drawing\_PathEffect](../../structs/oh-drawing-patheffect/document.md) object. |
| [OH\_Drawing\_PathEffect](../../structs/oh-drawing-patheffect/document.md)\* inner | Pointer to an inner effect, which is an [OH\_Drawing\_PathEffect](../../structs/oh-drawing-patheffect/document.md) object. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_PathEffect](../../structs/oh-drawing-patheffect/document.md)\* | 
Returns a pointer to the created [OH\_Drawing\_PathEffect](../../structs/oh-drawing-patheffect/document.md) object.

If a null pointer is returned, the creation fails. The possible failure cause is that **inner** or **inner** is a null pointer.

 |

#### \[h2\]OH\_Drawing\_CreateCornerPathEffect()

OH\_Drawing\_PathEffect\* OH\_Drawing\_CreateCornerPathEffect(float radius)

**Description**

Creates a path effect that transforms the sharp angle between line segments into a rounded corner with the specified radius.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| float radius | Radius of the rounded corner. The value is valid only when it is greater than 0. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_PathEffect](../../structs/oh-drawing-patheffect/document.md)\* | 
Returns a pointer to the created [OH\_Drawing\_PathEffect](../../structs/oh-drawing-patheffect/document.md) object.

If a null pointer is returned, the creation fails. The possible failure cause is that **radius** is less than or equal to **0**.

 |

#### \[h2\]OH\_Drawing\_CreateDashPathEffect()

OH\_Drawing\_PathEffect\* OH\_Drawing\_CreateDashPathEffect(float\* intervals, int count, float phase)

**Description**

Creates a dashed path effect. The dashed line effect is determined by a group of "on" and "off" intervals.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **intervals** is NULL or **count** is less than or equal to 0, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| float\* intervals | Pointer to the start address of the dashed line interval array. In the array, an even entry indicates an "on" interval and an odd entry indicates an "off" interval. The unit is px. |
| int count | Number of entries in the dashed line interval array. The value must be an even number greater than 0. |
| float phase | Offset in the dashed line interval array. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_PathEffect](../../structs/oh-drawing-patheffect/document.md)\* | Returns a pointer to the created [OH\_Drawing\_PathEffect](../../structs/oh-drawing-patheffect/document.md) object. |

#### \[h2\]OH\_Drawing\_CreateDiscretePathEffect()

OH\_Drawing\_PathEffect\* OH\_Drawing\_CreateDiscretePathEffect(float segLength, float deviation)

**Description**

Creates a path effect that segments the path and scatters the segments in an irregular pattern along the path.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| float segLength | Distance along the path at which each segment is fragmented. An effect is created when it is greater than 0. |
| float deviation | Maximum amount by which the end points of the segments can be randomly displaced during rendering. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_PathEffect](../../structs/oh-drawing-patheffect/document.md)\* | Returns a pointer to the created [OH\_Drawing\_PathEffect](../../structs/oh-drawing-patheffect/document.md) object. |

#### \[h2\]OH\_Drawing\_CreatePathDashEffect()

OH\_Drawing\_PathEffect\* OH\_Drawing\_CreatePathDashEffect(const OH\_Drawing\_Path\* path, float advance, float phase,OH\_Drawing\_PathDashStyle type)

**Description**

Creates a dashed path effect.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| const [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md)\* path | Pointer to an [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md) object. |
| float advance | Length of each dashed line segment. |
| float phase | Offset of the pattern within the dash segment length. |
| [OH\_Drawing\_PathDashStyle](#oh_drawing_pathdashstyle) type | Style of the dashed path effect. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_PathEffect](../../structs/oh-drawing-patheffect/document.md)\* | 
Returns a pointer to the created [OH\_Drawing\_PathEffect](../../structs/oh-drawing-patheffect/document.md) object.

If a null pointer is returned, the creation fails. The possible failure cause is that **path** is a null pointer or **advance** is less than or equal to **0**.

 |

#### \[h2\]OH\_Drawing\_CreateSumPathEffect()

OH\_Drawing\_PathEffect\* OH\_Drawing\_CreateSumPathEffect(OH\_Drawing\_PathEffect\* firstPathEffect,OH\_Drawing\_PathEffect\* secondPathEffect)

**Description**

Creates an overlay path effect based on two distinct path effects that take effect separately.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_PathEffect](../../structs/oh-drawing-patheffect/document.md)\* firstPathEffect | Pointer to an [OH\_Drawing\_PathEffect](../../structs/oh-drawing-patheffect/document.md) object. |
| [OH\_Drawing\_PathEffect](../../structs/oh-drawing-patheffect/document.md)\* secondPathEffect | Pointer to an [OH\_Drawing\_PathEffect](../../structs/oh-drawing-patheffect/document.md) object. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_PathEffect](../../structs/oh-drawing-patheffect/document.md)\* | 
Returns a pointer to the created [OH\_Drawing\_PathEffect](../../structs/oh-drawing-patheffect/document.md) object.

If a null pointer is returned, the creation fails. The possible failure cause is that **firstPathEffect** or **secondPathEffect** is a null pointer.

 |

#### \[h2\]OH\_Drawing\_PathEffectDestroy()

void OH\_Drawing\_PathEffectDestroy(OH\_Drawing\_PathEffect\* pathEffect)

**Description**

Destroys an **OH\_Drawing\_PathEffect** object and reclaims the memory occupied by the object.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_PathEffect](../../structs/oh-drawing-patheffect/document.md)\* pathEffect | Pointer to an [OH\_Drawing\_PathEffect](../../structs/oh-drawing-patheffect/document.md) object. |
