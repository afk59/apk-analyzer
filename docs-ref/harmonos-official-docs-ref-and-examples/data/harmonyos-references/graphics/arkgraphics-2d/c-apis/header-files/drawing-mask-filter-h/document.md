# drawing\_mask\_filter.h

#### Overview

This file declares the functions related to the mask filter in the drawing module.

**File to include**: <native\_drawing/drawing\_mask\_filter.h>

**Library**: libnative\_drawing.so

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 11

**Related module**: [Drawing](../../modules/drawing/document.md)

#### Summary

#### \[h2\]Enumerated value

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_Drawing\_BlurType](#oh_drawing_blurtype) | OH\_Drawing\_BlurType | Defines an enum for the blur types. |

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_MaskFilter\* OH\_Drawing\_MaskFilterCreateBlur(OH\_Drawing\_BlurType blurType, float sigma, bool respectCTM)](#oh_drawing_maskfiltercreateblur) | Creates an **OH\_Drawing\_MaskFilter** object with a blur type. |
| [void OH\_Drawing\_MaskFilterDestroy(OH\_Drawing\_MaskFilter\* maskFilter)](#oh_drawing_maskfilterdestroy) | Destroys an **OH\_Drawing\_MaskFilter** object and reclaims the memory occupied by the object. |

#### Enum Description

#### \[h2\]OH\_Drawing\_BlurType

enum OH\_Drawing\_BlurType

**Description**

Defines an enum for the blur types.

**Since**: 11

| Value | Description |
| :-- | :-- |
| NORMAL | Blurs both inside and outside the original border. |
| SOLID | Draws solid inside the border, and blurs outside. |
| OUTER | Draws nothing inside the border, and blurs outside. |
| INNER | Blurs inside the border, and draws nothing outside. |

#### Function Description

#### \[h2\]OH\_Drawing\_MaskFilterCreateBlur()

OH\_Drawing\_MaskFilter\* OH\_Drawing\_MaskFilterCreateBlur(OH\_Drawing\_BlurType blurType, float sigma, bool respectCTM)

**Description**

Creates an **OH\_Drawing\_MaskFilter** object with a blur type.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_BlurType](#oh_drawing_blurtype) blurType | Blur type. |
| float sigma | Standard deviation of the Gaussian blur to apply. The value must be greater than 0. |
| bool respectCTM | Whether the blur standard deviation is modified by the current transformation matrix (CTM). The default value is **true**. **true**: The blur standard deviation is affected by the CTM. **false**: The blur standard deviation is fixed and not affected by the CTM. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_MaskFilter](../../structs/oh-drawing-maskfilter/document.md)\* | Returns the pointer to the **OH\_Drawing\_MaskFilter** object created. |

#### \[h2\]OH\_Drawing\_MaskFilterDestroy()

void OH\_Drawing\_MaskFilterDestroy(OH\_Drawing\_MaskFilter\* maskFilter)

**Description**

Destroys an **OH\_Drawing\_MaskFilter** object and reclaims the memory occupied by the object.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_MaskFilter](../../structs/oh-drawing-maskfilter/document.md)\* maskFilter | Pointer to an **OH\_Drawing\_MaskFilter** object. |
