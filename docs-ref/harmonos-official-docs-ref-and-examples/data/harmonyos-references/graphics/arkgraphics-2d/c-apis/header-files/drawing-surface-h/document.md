# drawing\_surface.h

#### Overview

This file declares the functions related to the surface in the drawing module, including creating, destroying, and using the surface.

**File to include**: <native\_drawing/drawing\_surface.h>

**Library**: libnative\_drawing.so

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Related module**: [Drawing](../../modules/drawing/document.md)

#### Summary

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Surface\* OH\_Drawing\_SurfaceCreateFromGpuContext(OH\_Drawing\_GpuContext\* gpuContext, bool flag, OH\_Drawing\_Image\_Info imageInfo)](#oh_drawing_surfacecreatefromgpucontext) | 
Creates an **OH\_Drawing\_Surface** object using the GPU context to manage the content drawn on the canvas.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **gpuContext** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [OH\_Drawing\_Surface\* OH\_Drawing\_SurfaceCreateOnScreen(OH\_Drawing\_GpuContext\* gpuContext, OH\_Drawing\_Image\_Info imageInfo, void\* window)](#oh_drawing_surfacecreateonscreen) | 

Creates an **OH\_Drawing\_Surface** object bound to the window using the GPU context to manage the content drawn on the canvas.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

**OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** if **gpuContext** or **window** is NULL.

 |
| [OH\_Drawing\_Canvas\* OH\_Drawing\_SurfaceGetCanvas(OH\_Drawing\_Surface\* surface)](#oh_drawing_surfacegetcanvas) | 

Obtains a canvas from an **OH\_Drawing\_Surface** object.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **surface** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_SurfaceFlush(OH\_Drawing\_Surface\* surface)](#oh_drawing_surfaceflush) | Pushes the drawing content from an **OH\_Drawing\_Surface** object to the GPU for rendering. |
| [void OH\_Drawing\_SurfaceDestroy(OH\_Drawing\_Surface\* surface)](#oh_drawing_surfacedestroy) | Destroys an **OH\_Drawing\_Surface** object and reclaims the memory occupied. |

#### Function Description

#### \[h2\]OH\_Drawing\_SurfaceCreateFromGpuContext()

OH\_Drawing\_Surface\* OH\_Drawing\_SurfaceCreateFromGpuContext(OH\_Drawing\_GpuContext\* gpuContext, bool flag, OH\_Drawing\_Image\_Info imageInfo)

**Description**

Creates an **OH\_Drawing\_Surface** object using the GPU context to manage the content drawn on the canvas.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **gpuContext** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_GpuContext](../../structs/oh-drawing-gpucontext/document.md)\* gpuContext | Pointer to an [OH\_Drawing\_GpuContext](../../structs/oh-drawing-gpucontext/document.md) object. |
| bool flag | Whether the memory allocation is counted in the cache budget. **true** means yes; **false** otherwise. |
| [OH\_Drawing\_Image\_Info](../../structs/oh-drawing-image-info/document.md) imageInfo | Image information struct. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_Surface](../../structs/oh-drawing-surface/document.md)\* | Returns a pointer to the created [OH\_Drawing\_Surface](../../structs/oh-drawing-surface/document.md) object. |

#### \[h2\]OH\_Drawing\_SurfaceCreateOnScreen()

OH\_Drawing\_Surface\* OH\_Drawing\_SurfaceCreateOnScreen(OH\_Drawing\_GpuContext\* gpuContext, OH\_Drawing\_Image\_Info imageInfo, void\* window)

**Description**

Creates an **OH\_Drawing\_Surface** object bound to the window using the GPU context to manage the content drawn on the canvas.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

**OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** if **gpuContext** or **window** is NULL.

The width and height of imageInfo must be the same as those of window.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 16

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_GpuContext](../../structs/oh-drawing-gpucontext/document.md)\* gpuContext | 
Pointer to an [OH\_Drawing\_GpuContext](../../structs/oh-drawing-gpucontext/document.md) object.

This object must be created by [OH\_Drawing\_GpuContextCreate](../drawing-gpu-context-h/document.md#oh_drawing_gpucontextcreate). Otherwise, the **OH\_Drawing\_Surface** object fails to be created.

 |
| [OH\_Drawing\_Image\_Info](../../structs/oh-drawing-image-info/document.md) imageInfo | Image information struct. |
| void\* window | Pointer to the window object. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_Surface](../../structs/oh-drawing-surface/document.md)\* | Returns a pointer to the created [OH\_Drawing\_Surface](../../structs/oh-drawing-surface/document.md) object. |

#### \[h2\]OH\_Drawing\_SurfaceGetCanvas()

OH\_Drawing\_Canvas\* OH\_Drawing\_SurfaceGetCanvas(OH\_Drawing\_Surface\* surface)

**Description**

Obtains a canvas from an **OH\_Drawing\_Surface** object.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **surface** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Surface](../../structs/oh-drawing-surface/document.md)\* surface | Pointer to an **OH\_Drawing\_Surface** object. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_Canvas](../../structs/oh-drawing-canvas/document.md)\* | Returns a pointer to the created [OH\_Drawing\_Canvas](../../structs/oh-drawing-canvas/document.md) object. The pointer returned does not need to be managed by the caller. |

#### \[h2\]OH\_Drawing\_SurfaceFlush()

OH\_Drawing\_ErrorCode OH\_Drawing\_SurfaceFlush(OH\_Drawing\_Surface\* surface)

**Description**

Pushes the drawing content from an **OH\_Drawing\_Surface** object to the GPU for rendering.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 16

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Surface](../../structs/oh-drawing-surface/document.md)\* surface | Pointer to the created [OH\_Drawing\_Surface](../../structs/oh-drawing-surface/document.md) object. This object must be created by calling [OH\_Drawing\_SurfaceCreateOnScreen](#oh_drawing_surfacecreateonscreen). Otherwise, calling the current API has no effect. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_ErrorCode](../drawing-error-code-h/document.md#oh_drawing_errorcode) | 
Returns one of the following result codes:

**OH\_DRAWING\_SUCCESS** if the operation is successful.

**OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** if **surface** is NULL.

 |

#### \[h2\]OH\_Drawing\_SurfaceDestroy()

void OH\_Drawing\_SurfaceDestroy(OH\_Drawing\_Surface\* surface)

**Description**

Destroys an **OH\_Drawing\_Surface** object and reclaims the memory occupied.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Surface](../../structs/oh-drawing-surface/document.md)\* surface | Pointer to an **OH\_Drawing\_Surface** object. |
