# drawing\_filter.h

#### Overview

This file declares the functions related to the filter in the drawing module.

**File to include**: <native\_drawing/drawing\_filter.h>

**Library**: libnative\_drawing.so

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 11

**Related module**: [Drawing](../../modules/drawing/document.md)

#### Summary

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Filter\* OH\_Drawing\_FilterCreate(void)](#oh_drawing_filtercreate) | Creates an **OH\_Drawing\_Filter** object. |
| [void OH\_Drawing\_FilterSetImageFilter(OH\_Drawing\_Filter\* filter, OH\_Drawing\_ImageFilter\* imageFilter)](#oh_drawing_filtersetimagefilter) | 
Sets an **OH\_Drawing\_ImageFilter** object for an **OH\_Drawing\_Filter** object.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **filter** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [void OH\_Drawing\_FilterSetMaskFilter(OH\_Drawing\_Filter\* filter, OH\_Drawing\_MaskFilter\* maskFilter)](#oh_drawing_filtersetmaskfilter) | 

Sets an **OH\_Drawing\_MaskFilter** object for an **OH\_Drawing\_Filter** object.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **filter** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [void OH\_Drawing\_FilterSetColorFilter(OH\_Drawing\_Filter\* filter, OH\_Drawing\_ColorFilter\* colorFilter)](#oh_drawing_filtersetcolorfilter) | 

Sets an **OH\_Drawing\_ColorFilter** object for an **OH\_Drawing\_Filter** object.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **filter** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [void OH\_Drawing\_FilterGetColorFilter(OH\_Drawing\_Filter\* filter, OH\_Drawing\_ColorFilter\* colorFilter)](#oh_drawing_filtergetcolorfilter) | 

Obtains an **OH\_Drawing\_ColorFilter** object from an **OH\_Drawing\_Filter** object.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **filter** or **colorFilter** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [void OH\_Drawing\_FilterDestroy(OH\_Drawing\_Filter\* filter)](#oh_drawing_filterdestroy) | Destroys an **OH\_Drawing\_Filter** object and reclaims the memory occupied by the object. |

#### Function Description

#### \[h2\]OH\_Drawing\_FilterCreate()

OH\_Drawing\_Filter\* OH\_Drawing\_FilterCreate(void)

**Description**

Creates an **OH\_Drawing\_Filter** object.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 11

**Return value**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_Filter](../../structs/oh-drawing-filter/document.md)\* | Returns the pointer to the **OH\_Drawing\_Filter** object created. |

#### \[h2\]OH\_Drawing\_FilterSetImageFilter()

void OH\_Drawing\_FilterSetImageFilter(OH\_Drawing\_Filter\* filter, OH\_Drawing\_ImageFilter\* imageFilter)

**Description**

Sets an **OH\_Drawing\_ImageFilter** object for an **OH\_Drawing\_Filter** object.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **filter** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Filter](../../structs/oh-drawing-filter/document.md)\* filter | Pointer to an [OH\_Drawing\_Filter](../../structs/oh-drawing-filter/document.md) object. |
| [OH\_Drawing\_ImageFilter](../../structs/oh-drawing-imagefilter/document.md)\* imageFilter | Pointer to an [OH\_Drawing\_ImageFilter](../../structs/oh-drawing-imagefilter/document.md) object. If NULL is passed in, the image filter effect of the object will be cleared. |

#### \[h2\]OH\_Drawing\_FilterSetMaskFilter()

void OH\_Drawing\_FilterSetMaskFilter(OH\_Drawing\_Filter\* filter, OH\_Drawing\_MaskFilter\* maskFilter)

**Description**

Sets an **OH\_Drawing\_MaskFilter** object for an **OH\_Drawing\_Filter** object.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **filter** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Filter](../../structs/oh-drawing-filter/document.md)\* filter | Pointer to an [OH\_Drawing\_Filter](../../structs/oh-drawing-filter/document.md) object. |
| [OH\_Drawing\_MaskFilter](../../structs/oh-drawing-maskfilter/document.md)\* maskFilter | Pointer to an [OH\_Drawing\_MaskFilter](../../structs/oh-drawing-maskfilter/document.md) object. If NULL is passed in, the mask filter effect of the object will be cleared. |

#### \[h2\]OH\_Drawing\_FilterSetColorFilter()

void OH\_Drawing\_FilterSetColorFilter(OH\_Drawing\_Filter\* filter, OH\_Drawing\_ColorFilter\* colorFilter)

**Description**

Sets an **OH\_Drawing\_ColorFilter** object for an **OH\_Drawing\_Filter** object.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **filter** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Filter](../../structs/oh-drawing-filter/document.md)\* filter | Pointer to an [OH\_Drawing\_Filter](../../structs/oh-drawing-filter/document.md) object. |
| [OH\_Drawing\_ColorFilter](../../structs/oh-drawing-colorfilter/document.md)\* colorFilter | Pointer to an [OH\_Drawing\_ColorFilter](../../structs/oh-drawing-colorfilter/document.md) object. If NULL is passed in, the color filter effect of the object will be cleared. |

#### \[h2\]OH\_Drawing\_FilterGetColorFilter()

void OH\_Drawing\_FilterGetColorFilter(OH\_Drawing\_Filter\* filter, OH\_Drawing\_ColorFilter\* colorFilter)

**Description**

Obtains an **OH\_Drawing\_ColorFilter** object from an **OH\_Drawing\_Filter** object.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **filter** or **colorFilter** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Filter](../../structs/oh-drawing-filter/document.md)\* filter | Pointer to an [OH\_Drawing\_Filter](../../structs/oh-drawing-filter/document.md) object. |
| [OH\_Drawing\_ColorFilter](../../structs/oh-drawing-colorfilter/document.md)\* colorFilter | Pointer to an [OH\_Drawing\_ColorFilter](../../structs/oh-drawing-colorfilter/document.md) object. |

#### \[h2\]OH\_Drawing\_FilterDestroy()

void OH\_Drawing\_FilterDestroy(OH\_Drawing\_Filter\* filter)

**Description**

Destroys an **OH\_Drawing\_Filter** object and reclaims the memory occupied by the object.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Filter](../../structs/oh-drawing-filter/document.md)\* filter | Pointer to an [OH\_Drawing\_Filter](../../structs/oh-drawing-filter/document.md) object. |
