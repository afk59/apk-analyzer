# drawing\_text\_lineTypography.h

#### Overview

This file declares the functions related to line typography, including functions to determine the number of characters that can be formatted from a given position within the text.

**File to include**: <native\_drawing/drawing\_text\_lineTypography.h>

**Library**: libnative\_drawing.so

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 18

**Related module**: [Drawing](../../modules/drawing/document.md)

#### Summary

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_LineTypography\* OH\_Drawing\_CreateLineTypography(OH\_Drawing\_TypographyCreate\* handler)](#oh_drawing_createlinetypography) | Creates a pointer to an [OH\_Drawing\_LineTypography](../../structs/oh-drawing-linetypography/document.md) object, which stores the text content and style and can be used to compute typography details for individual lines of text. |
| [void OH\_Drawing\_DestroyLineTypography(OH\_Drawing\_LineTypography\* lineTypography)](#oh_drawing_destroylinetypography) | Releases the memory occupied by an [OH\_Drawing\_LineTypography](../../structs/oh-drawing-linetypography/document.md) object. |
| [size\_t OH\_Drawing\_LineTypographyGetLineBreak(OH\_Drawing\_LineTypography\* lineTypography,size\_t startIndex, double width)](#oh_drawing_linetypographygetlinebreak) | Obtains the number of characters that can fit in the layout from the specified position within a limited layout width. |
| [OH\_Drawing\_TextLine\* OH\_Drawing\_LineTypographyCreateLine(OH\_Drawing\_LineTypography\* lineTypography,size\_t startIndex, size\_t count)](#oh_drawing_linetypographycreateline) | Creates a pointer to an [OH\_Drawing\_TextLine](../../structs/oh-drawing-textline/document.md) object based on the text content in a specified range. |

#### Function Description

#### \[h2\]OH\_Drawing\_CreateLineTypography()

OH\_Drawing\_LineTypography\* OH\_Drawing\_CreateLineTypography(OH\_Drawing\_TypographyCreate\* handler)

**Description**

Creates a pointer to an [OH\_Drawing\_LineTypography](../../structs/oh-drawing-linetypography/document.md) object, which stores the text content and style and can be used to compute typography details for individual lines of text.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TypographyCreate](../../structs/oh-drawing-typographycreate/document.md)\* handler | Pointer to the [OH\_Drawing\_TypographyCreate](../../structs/oh-drawing-typographycreate/document.md) object, which is obtained from [OH\_Drawing\_CreateTypographyHandler](../drawing-text-typography-h/document.md#oh_drawing_createtypographyhandler). |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_LineTypography](../../structs/oh-drawing-linetypography/document.md)\* | Returns the pointer to the [OH\_Drawing\_LineTypography](../../structs/oh-drawing-linetypography/document.md) object created. |

#### \[h2\]OH\_Drawing\_DestroyLineTypography()

void OH\_Drawing\_DestroyLineTypography(OH\_Drawing\_LineTypography\* lineTypography)

**Description**

Releases the memory occupied by an [OH\_Drawing\_LineTypography](../../structs/oh-drawing-linetypography/document.md) object.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_LineTypography](../../structs/oh-drawing-linetypography/document.md)\* lineTypography | Pointer to the [OH\_Drawing\_LineTypography](../../structs/oh-drawing-linetypography/document.md) object, which is obtained from [OH\_Drawing\_CreateLineTypography](#oh_drawing_createlinetypography). |

#### \[h2\]OH\_Drawing\_LineTypographyGetLineBreak()

size\_t OH\_Drawing\_LineTypographyGetLineBreak(OH\_Drawing\_LineTypography\* lineTypography,size\_t startIndex, double width)

**Description**

Obtains the number of characters that can fit in the layout from the specified position within a limited layout width.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_LineTypography](../../structs/oh-drawing-linetypography/document.md)\* lineTypography | Pointer to the [OH\_Drawing\_LineTypography](../../structs/oh-drawing-linetypography/document.md) object, which is obtained from [OH\_Drawing\_CreateLineTypography](#oh_drawing_createlinetypography). |
| size\_t startIndex | Start position (inclusive) for layout calculation. The value must be an integer in the range \[0, total number of text characters\]. |
| double width | Layout width. The value is a floating point number greater than 0, in px. |

**Returns**

| Type | Description |
| :-- | :-- |
| size\_t | Returns the number of characters. |

#### \[h2\]OH\_Drawing\_LineTypographyCreateLine()

OH\_Drawing\_TextLine\* OH\_Drawing\_LineTypographyCreateLine(OH\_Drawing\_LineTypography\* lineTypography,size\_t startIndex, size\_t count)

**Description**

Creates a pointer to an [OH\_Drawing\_TextLine](../../structs/oh-drawing-textline/document.md) object based on the text content in a specified range.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_LineTypography](../../structs/oh-drawing-linetypography/document.md)\* lineTypography | Pointer to the [OH\_Drawing\_LineTypography](../../structs/oh-drawing-linetypography/document.md) object, which is obtained from [OH\_Drawing\_CreateLineTypography](#oh_drawing_createlinetypography). |
| size\_t startIndex | Start position for layout calculation. The value is an integer in the range \[0, total number of text characters). |
| size\_t count | 
Number of characters from the specified start position. The value is an integer in the range \[0, total number of text characters). The sum of **startIndex** and **count** cannot be greater than the total number of text characters.

You can use [OH\_Drawing\_LineTypographyGetLineBreak](#oh_drawing_linetypographygetlinebreak) to obtain the number of characters that can fit in the layout. If the value is set to **0**, a null pointer is returned.

 |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_TextLine](../../structs/oh-drawing-textline/document.md)\* | Pointer to the [OH\_Drawing\_TextLine](../../structs/oh-drawing-textline/document.md) object. |
