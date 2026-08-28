# drawing\_gpu\_context.h

#### Overview

This file declares the functions related to the GPU context in the drawing module.

**File to include**: <native\_drawing/drawing\_gpu\_context.h>

**Library**: libnative\_drawing.so

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Related module**: [Drawing](../../modules/drawing/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_Drawing\_GpuContextOptions](../../structs/oh-drawing-gpucontextoptions/document.md) | OH\_Drawing\_GpuContextOptions | Describes the options about the GPU context. |

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_GpuContext\* OH\_Drawing\_GpuContextCreateFromGL(OH\_Drawing\_GpuContextOptions gpuContextOptions)](#oh_drawing_gpucontextcreatefromgl) | Creates an **OH\_Drawing\_GpuContext** object that uses OpenGL as the backend interface. |
| [OH\_Drawing\_GpuContext\* OH\_Drawing\_GpuContextCreate(void)](#oh_drawing_gpucontextcreate) | Creates an **OH\_Drawing\_GpuContext** object, for which the backend type depends on the device. |
| [void OH\_Drawing\_GpuContextDestroy(OH\_Drawing\_GpuContext\* gpuContext)](#oh_drawing_gpucontextdestroy) | Destroys an **OH\_Drawing\_GpuContext** object and reclaims the memory occupied by the object. |

#### Function Description

#### \[h2\]OH\_Drawing\_GpuContextCreateFromGL()

OH\_Drawing\_GpuContext\* OH\_Drawing\_GpuContextCreateFromGL(OH\_Drawing\_GpuContextOptions gpuContextOptions)

**Description**

Creates an **OH\_Drawing\_GpuContext** object that uses OpenGL as the backend interface.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Deprecated from**: 18

**Substitute**: OH\_Drawing\_GpuContextCreate

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_GpuContextOptions](../../structs/oh-drawing-gpucontextoptions/document.md) gpuContextOptions | GPU context options, which is [OH\_Drawing\_GpuContextOptions](../../structs/oh-drawing-gpucontextoptions/document.md). |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_GpuContext](../../structs/oh-drawing-gpucontext/document.md)\* | Returns the pointer to the [OH\_Drawing\_GpuContext](../../structs/oh-drawing-gpucontext/document.md) object created. |

#### \[h2\]OH\_Drawing\_GpuContextCreate()

OH\_Drawing\_GpuContext\* OH\_Drawing\_GpuContextCreate(void)

**Description**

Creates an **OH\_Drawing\_GpuContext** object, for which the backend type depends on the device.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 16

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_GpuContext](../../structs/oh-drawing-gpucontext/document.md)\* | Returns the pointer to the [OH\_Drawing\_GpuContext](../../structs/oh-drawing-gpucontext/document.md) object created. |

#### \[h2\]OH\_Drawing\_GpuContextDestroy()

void OH\_Drawing\_GpuContextDestroy(OH\_Drawing\_GpuContext\* gpuContext)

**Description**

Destroys an **OH\_Drawing\_GpuContext** object and reclaims the memory occupied by the object.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_GpuContext](../../structs/oh-drawing-gpucontext/document.md)\* gpuContext | Pointer to an [OH\_Drawing\_GpuContext](../../structs/oh-drawing-gpucontext/document.md) object. |
