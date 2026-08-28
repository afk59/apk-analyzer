# drawing\_color.h

#### Overview

This file declares the functions related to the color in the drawing module.

**File to include**: <native\_drawing/drawing\_color.h>

**Library**: libnative\_drawing.so

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 8

**Related module**: [Drawing](../../modules/drawing/document.md)

#### Summary

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [uint32\_t OH\_Drawing\_ColorSetArgb(uint32\_t alpha, uint32\_t red, uint32\_t green, uint32\_t blue)](#oh_drawing_colorsetargb) | Converts four variables (alpha, red, green, and blue) into a 32-bit (ARGB) variable that describes a color. |

#### Function Description

#### \[h2\]OH\_Drawing\_ColorSetArgb()

uint32\_t OH\_Drawing\_ColorSetArgb(uint32\_t alpha, uint32\_t red, uint32\_t green, uint32\_t blue)

**Description**

Converts four variables (alpha, red, green, and blue) into a 32-bit (ARGB) variable that describes a color.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| uint32\_t alpha | Alpha, which is a variable ranging from 0x00 to 0xFF. |
| uint32\_t red | Read, which is a variable ranging from 0x00 to 0xFF. |
| uint32\_t green | Green, which is a variable ranging from 0x00 to 0xFF. |
| uint32\_t blue | Blue, which is a variable ranging from 0x00 to 0xFF. |

**Return value**

| Type | Description |
| :-- | :-- |
| uint32\_t | Returns a 32-bit (ARGB) variable that describes the color. |
