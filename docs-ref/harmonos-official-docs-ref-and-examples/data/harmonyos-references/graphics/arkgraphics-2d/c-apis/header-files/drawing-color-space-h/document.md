# drawing\_color\_space.h

#### Overview

This file declares the functions related to the color space in the drawing module.

**File to include:** <native\_drawing/drawing\_color\_space.h>

**Library**: libnative\_drawing.so

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Related module**: [Drawing](../../modules/drawing/document.md)

#### Summary

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_ColorSpace\* OH\_Drawing\_ColorSpaceCreateSrgb(void)](#oh_drawing_colorspacecreatesrgb) | Creates an sRGB color space. |
| [OH\_Drawing\_ColorSpace\* OH\_Drawing\_ColorSpaceCreateSrgbLinear(void)](#oh_drawing_colorspacecreatesrgblinear) | Creates an sRGB linear (Gamma 1.0) color space. |
| [void OH\_Drawing\_ColorSpaceDestroy(OH\_Drawing\_ColorSpace\* colorSpace)](#oh_drawing_colorspacedestroy) | Destroys an **OH\_Drawing\_ColorSpace** object and reclaims the memory occupied by the object. |

#### Function Description

#### \[h2\]OH\_Drawing\_ColorSpaceCreateSrgb()

OH\_Drawing\_ColorSpace\* OH\_Drawing\_ColorSpaceCreateSrgb(void)

**Description**

Creates an sRGB color space.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_ColorSpace](../../structs/oh-drawing-colorspace/document.md)\* | Returns a pointer to the [OH\_Drawing\_ColorSpace](../../structs/oh-drawing-colorspace/document.md) object created. |

#### \[h2\]OH\_Drawing\_ColorSpaceCreateSrgbLinear()

OH\_Drawing\_ColorSpace\* OH\_Drawing\_ColorSpaceCreateSrgbLinear(void)

**Description**

Creates an sRGB linear (Gamma 1.0) color space.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_ColorSpace](../../structs/oh-drawing-colorspace/document.md)\* | Returns a pointer to the [OH\_Drawing\_ColorSpace](../../structs/oh-drawing-colorspace/document.md) object created. |

#### \[h2\]OH\_Drawing\_ColorSpaceDestroy()

void OH\_Drawing\_ColorSpaceDestroy(OH\_Drawing\_ColorSpace\* colorSpace)

**Description**

Destroys an **OH\_Drawing\_ColorSpace** object and reclaims the memory occupied by the object.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_ColorSpace](../../structs/oh-drawing-colorspace/document.md)\* colorSpace | Pointer to an [OH\_Drawing\_ColorSpace](../../structs/oh-drawing-colorspace/document.md) object. |
