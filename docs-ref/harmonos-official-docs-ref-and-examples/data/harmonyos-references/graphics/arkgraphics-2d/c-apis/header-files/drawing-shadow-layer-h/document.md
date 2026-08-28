# drawing\_shadow\_layer.h

#### Overview

This file declares the functions related to the shadow in the drawing module.

**File to include**: <native\_drawing/drawing\_shadow\_layer.h>

**Library**: libnative\_drawing.so

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Related module**: [Drawing](../../modules/drawing/document.md)

#### Summary

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_ShadowLayer\* OH\_Drawing\_ShadowLayerCreate(float blurRadius, float x, float y, uint32\_t color)](#oh_drawing_shadowlayercreate) | 
Creates an **OH\_Drawing\_ShadowLayer** object.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **blurRadius** is less than or equal to 0, **OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE** is returned.

 |
| [void OH\_Drawing\_ShadowLayerDestroy(OH\_Drawing\_ShadowLayer\* shadowLayer)](#oh_drawing_shadowlayerdestroy) | Destroys an **OH\_Drawing\_ShadowLayer** object and reclaims the memory occupied by the object. |

#### Function Description

#### \[h2\]OH\_Drawing\_ShadowLayerCreate()

OH\_Drawing\_ShadowLayer\* OH\_Drawing\_ShadowLayerCreate(float blurRadius, float x, float y, uint32\_t color)

**Description**

Creates an **OH\_Drawing\_ShadowLayer** object.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **blurRadius** is less than or equal to 0, **OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| float blurRadius | Radius of the shadow layer. The value must be greater than 0. |
| float x | Offset on the X axis. |
| float y | Offset on the Y axis. |
| uint32\_t color | Color of the shadow. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_ShadowLayer](../../structs/oh-drawing-shadowlayer/document.md)\* | Returns the pointer to the **OH\_Drawing\_ShadowLayer** object created. |

#### \[h2\]OH\_Drawing\_ShadowLayerDestroy()

void OH\_Drawing\_ShadowLayerDestroy(OH\_Drawing\_ShadowLayer\* shadowLayer)

**Description**

Destroys an **OH\_Drawing\_ShadowLayer** object and reclaims the memory occupied by the object.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_ShadowLayer](../../structs/oh-drawing-shadowlayer/document.md)\* shadowLayer | Pointer to the shadow layer. |
