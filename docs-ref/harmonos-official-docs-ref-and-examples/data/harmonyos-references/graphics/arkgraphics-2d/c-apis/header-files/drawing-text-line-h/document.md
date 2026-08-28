# drawing\_text\_line.h

#### Overview

This file declares the capabilities for obtaining the character position in a text line, obtaining the run information, and truncating text by line.

**File to include**: <native\_drawing/drawing\_text\_line.h>

**Library**: libnative\_drawing.so

**Since**: 18

**Related module**: [Drawing](../../modules/drawing/document.md)

#### Summary

#### \[h2\]Functions

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_Drawing\_Array\* OH\_Drawing\_TypographyGetTextLines(OH\_Drawing\_Typography\* typography)](#oh_drawing_typographygettextlines) | \- | Obtains the array of text lines in a typography object. This array contains one or more text line objects. Release this pointer by calling [OH\_Drawing\_DestroyTextLines](#oh_drawing_destroytextlines) when this object is no longer needed. |
| [void OH\_Drawing\_DestroyTextLines(OH\_Drawing\_Array\* lines)](#oh_drawing_destroytextlines) | \- | Releases the memory occupied by a text line array. |
| [void OH\_Drawing\_DestroyTextLine(OH\_Drawing\_TextLine\* line)](#oh_drawing_destroytextline) | \- | Releases the memory occupied by a text line object. This is applicable only to text line objects that have requested memory on their own and not to a particular text line object within a text line array. |
| [OH\_Drawing\_TextLine\* OH\_Drawing\_GetTextLineByIndex(OH\_Drawing\_Array\* lines, size\_t index)](#oh_drawing_gettextlinebyindex) | \- | Obtains the text line object with the specified index in a text line array. |
| [double OH\_Drawing\_TextLineGetGlyphCount(OH\_Drawing\_TextLine\* line)](#oh_drawing_textlinegetglyphcount) | \- | Obtains the number of glyphs in a text line object. |
| [void OH\_Drawing\_TextLineGetTextRange(OH\_Drawing\_TextLine\* line, size\_t\* start, size\_t\* end)](#oh_drawing_textlinegettextrange) | \- | Obtains the range of the text in a text line object in the entire paragraph. |
| [OH\_Drawing\_Array\* OH\_Drawing\_TextLineGetGlyphRuns(OH\_Drawing\_TextLine\* line)](#oh_drawing_textlinegetglyphruns) | \- | Obtains the array of glyph runs in a text line object. |
| [void OH\_Drawing\_DestroyRuns(OH\_Drawing\_Array\* runs)](#oh_drawing_destroyruns) | \- | Releases the memory occupied by a glyph run array. |
| [OH\_Drawing\_Run\* OH\_Drawing\_GetRunByIndex(OH\_Drawing\_Array\* runs, size\_t index)](#oh_drawing_getrunbyindex) | \- | Obtains the glyph run object with the specified index in a glyph run array. |
| [void OH\_Drawing\_TextLinePaint(OH\_Drawing\_TextLine\* line, OH\_Drawing\_Canvas\* canvas, double x, double y)](#oh_drawing_textlinepaint) | \- | Paints a text line on the canvas with the coordinate point (x, y) as the upper left corner. |
| [OH\_Drawing\_TextLine\* OH\_Drawing\_TextLineCreateTruncatedLine(OH\_Drawing\_TextLine\* line, double width, int mode,const char\* ellipsis)](#oh_drawing_textlinecreatetruncatedline) | \- | Creates a truncated text line object. |
| [double OH\_Drawing\_TextLineGetTypographicBounds(OH\_Drawing\_TextLine\* line, double\* ascent, double\* descent,double\* leading)](#oh_drawing_textlinegettypographicbounds) | \- | 
Obtains the typographic boundary of a text line object. The typographic boundary is related to the font and font size used for typography, but not the characters within the text.

For example, for the string " a b " (which has a space before "a" and a space after "b"), the typographic boundary encompasses the spaces at the beginning and end. For the strings "j" and "E", the typographic boundaries are the same, indicating that they are irrelevant to specific characters.

 |
| [OH\_Drawing\_Rect\* OH\_Drawing\_TextLineGetImageBounds(OH\_Drawing\_TextLine\* line)](#oh_drawing_textlinegetimagebounds) | \- | 

Obtains the image boundary of a text line object. The image boundary, equivalent to a visual boundary, is related to the font, font size, and characters.

For example, for the string " a b " (which has a space before "a" and a space after "b"), only "a b" are visible to users, and therefore the image boundary does not include these spaces at the beginning and end.

For the strings "j" and "E", their image boundaries are different. Specifically, the width of the boundary for "j" is narrower than that for "E", and the height of the boundary for "j" is taller than that for "E".

 |
| [double OH\_Drawing\_TextLineGetTrailingSpaceWidth(OH\_Drawing\_TextLine\* line)](#oh_drawing_textlinegettrailingspacewidth) | \- | Obtains the width of the spaces at the end of a text line object. |
| [int32\_t OH\_Drawing\_TextLineGetStringIndexForPosition(OH\_Drawing\_TextLine\* line, OH\_Drawing\_Point\* point)](#oh_drawing_textlinegetstringindexforposition) | \- | Obtains the index of a character at the specified position in a text line object. |
| [double OH\_Drawing\_TextLineGetOffsetForStringIndex(OH\_Drawing\_TextLine\* line, int32\_t index)](#oh_drawing_textlinegetoffsetforstringindex) | \- | Obtains the offset of a character with the specified index in a text line object. |
| [typedef bool (\*Drawing\_CaretOffsetsCallback)(double offset, int32\_t index, bool leadingEdge)](#drawing_caretoffsetscallback) | Drawing\_CaretOffsetsCallback | Defines a custom callback used to receive the offset and index of each character in a text line object as its parameters. |
| [void OH\_Drawing\_TextLineEnumerateCaretOffsets(OH\_Drawing\_TextLine\* line, Drawing\_CaretOffsetsCallback callback)](#oh_drawing_textlineenumeratecaretoffsets) | \- | Enumerates the offset and index of each character in a text line object and passes them to a custom callback function. You can use the offset and index array for other operations. |
| [double OH\_Drawing\_TextLineGetAlignmentOffset(OH\_Drawing\_TextLine\* line, double alignmentFactor, double alignmentWidth)](#oh_drawing_textlinegetalignmentoffset) | \- | Obtains the offset of a text line object after alignment based on the alignment factor and alignment width. |

#### Function Description

#### \[h2\]OH\_Drawing\_TypographyGetTextLines()

OH\_Drawing\_Array\* OH\_Drawing\_TypographyGetTextLines(OH\_Drawing\_Typography\* typography)

**Description**

Obtains the array of text lines in a typography object. This array contains one or more text line objects. Release this pointer by calling [OH\_Drawing\_DestroyTextLines](#oh_drawing_destroytextlines) when this object is no longer needed.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Typography](../../structs/oh-drawing-typography/document.md)\* typography | Pointer to the [OH\_Drawing\_Typography](../../structs/oh-drawing-typography/document.md) object. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_Array](../../structs/oh-drawing-array/document.md)\* | Pointer to the [OH\_Drawing\_Array](../../structs/oh-drawing-array/document.md) object. |

#### \[h2\]OH\_Drawing\_DestroyTextLines()

void OH\_Drawing\_DestroyTextLines(OH\_Drawing\_Array\* lines)

**Description**

Releases the memory occupied by a text line array.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Array](../../structs/oh-drawing-array/document.md)\* lines | Pointer to the [OH\_Drawing\_Array](../../structs/oh-drawing-array/document.md) object. |

#### \[h2\]OH\_Drawing\_DestroyTextLine()

void OH\_Drawing\_DestroyTextLine(OH\_Drawing\_TextLine\* line)

**Description**

Releases the memory occupied by a text line object. This is applicable only to text line objects that have requested memory on their own and not to a particular text line object within a text line array.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TextLine](../../structs/oh-drawing-textline/document.md)\* line | Pointer to the [OH\_Drawing\_TextLine](../../structs/oh-drawing-textline/document.md) object. |

#### \[h2\]OH\_Drawing\_GetTextLineByIndex()

OH\_Drawing\_TextLine\* OH\_Drawing\_GetTextLineByIndex(OH\_Drawing\_Array\* lines, size\_t index)

**Description**

Obtains the text line object with the specified index in a text line array.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Array](../../structs/oh-drawing-array/document.md)\* lines | Pointer to the [OH\_Drawing\_Array](../../structs/oh-drawing-array/document.md) object. |
| size\_t index | Index of the text line array. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_TextLine](../../structs/oh-drawing-textline/document.md)\* | Returns a pointer to the [OH\_Drawing\_TextLine](../../structs/oh-drawing-textline/document.md) object at the specified index. |

#### \[h2\]OH\_Drawing\_TextLineGetGlyphCount()

double OH\_Drawing\_TextLineGetGlyphCount(OH\_Drawing\_TextLine\* line)

**Description**

Obtains the number of glyphs in a text line object.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TextLine](../../structs/oh-drawing-textline/document.md)\* line | Pointer to the [OH\_Drawing\_TextLine](../../structs/oh-drawing-textline/document.md) object. |

**Returns**

| Type | Description |
| :-- | :-- |
| double | Returns the number of glyphs in the text line object. |

#### \[h2\]OH\_Drawing\_TextLineGetTextRange()

void OH\_Drawing\_TextLineGetTextRange(OH\_Drawing\_TextLine\* line, size\_t\* start, size\_t\* end)

**Description**

Obtains the range of the text in a text line object in the entire paragraph.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TextLine](../../structs/oh-drawing-textline/document.md)\* line | Pointer to the [OH\_Drawing\_TextLine](../../structs/oh-drawing-textline/document.md) object. |
| size\_t\* start | Pointer to the start of the range. |
| size\_t\* end | Pointer to the end of the range. |

#### \[h2\]OH\_Drawing\_TextLineGetGlyphRuns()

OH\_Drawing\_Array\* OH\_Drawing\_TextLineGetGlyphRuns(OH\_Drawing\_TextLine\* line)

**Description**

Obtains the array of glyph runs in a text line object.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TextLine](../../structs/oh-drawing-textline/document.md)\* line | Pointer to the [OH\_Drawing\_TextLine](../../structs/oh-drawing-textline/document.md) object. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_Array](../../structs/oh-drawing-array/document.md)\* | Returns a pointer to the [OH\_Drawing\_Array](../../structs/oh-drawing-array/document.md) array, which holds multiple [OH\_Drawing\_Run](../../structs/oh-drawing-run/document.md) objects. Release this pointer by calling [OH\_Drawing\_DestroyRuns](#oh_drawing_destroyruns) when this object is no longer needed. |

#### \[h2\]OH\_Drawing\_DestroyRuns()

void OH\_Drawing\_DestroyRuns(OH\_Drawing\_Array\* runs)

**Description**

Releases the memory occupied by a glyph run array.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Array](../../structs/oh-drawing-array/document.md)\* runs | Pointer to the [OH\_Drawing\_Array](../../structs/oh-drawing-array/document.md) array, which holds multiple [OH\_Drawing\_Run](../../structs/oh-drawing-run/document.md) objects. |

#### \[h2\]OH\_Drawing\_GetRunByIndex()

OH\_Drawing\_Run\* OH\_Drawing\_GetRunByIndex(OH\_Drawing\_Array\* runs, size\_t index)

**Description**

Obtains the glyph run object with the specified index in a glyph run array.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Array](../../structs/oh-drawing-array/document.md)\* runs | Pointer to the [OH\_Drawing\_Array](../../structs/oh-drawing-array/document.md) array, which holds multiple [OH\_Drawing\_Run](../../structs/oh-drawing-run/document.md) objects. |
| size\_t index | Index of the glyph run array. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_Run](../../structs/oh-drawing-run/document.md)\* | Returns a pointer to the [OH\_Drawing\_Run](../../structs/oh-drawing-run/document.md) object at the specified index. |

#### \[h2\]OH\_Drawing\_TextLinePaint()

void OH\_Drawing\_TextLinePaint(OH\_Drawing\_TextLine\* line, OH\_Drawing\_Canvas\* canvas, double x, double y)

**Description**

Paints a text line on the canvas with the coordinate point (x, y) as the upper left corner.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TextLine](../../structs/oh-drawing-textline/document.md)\* line | Pointer to the [OH\_Drawing\_TextLine](../../structs/oh-drawing-textline/document.md) object. |
| [OH\_Drawing\_Canvas](../../structs/oh-drawing-canvas/document.md)\* canvas | Pointer to the target canvas [OH\_Drawing\_Canvas](../../structs/oh-drawing-canvas/document.md). |
| double x | Horizontal coordinate of the upper left corner, in px. |
| double y | Vertical coordinate of the upper left corner, in px. |

#### \[h2\]OH\_Drawing\_TextLineCreateTruncatedLine()

OH\_Drawing\_TextLine\* OH\_Drawing\_TextLineCreateTruncatedLine(OH\_Drawing\_TextLine\* line, double width, int mode,const char\* ellipsis)

**Description**

Creates a truncated text line object.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TextLine](../../structs/oh-drawing-textline/document.md)\* line | Pointer to the [OH\_Drawing\_TextLine](../../structs/oh-drawing-textline/document.md) object. |
| double width | Line width after truncation. |
| int mode | Truncation type. The value is an enumerated value of [OH\_Drawing\_EllipsisModal](../drawing-text-typography-h/document.md#oh_drawing_ellipsismodal). Currently, only **ELLIPSIS\_MODAL\_HEAD** and **ELLIPSIS\_MODAL\_TAIL** are supported. |
| const char\* ellipsis | Pointer to the string used to mark a truncation. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_TextLine](../../structs/oh-drawing-textline/document.md)\* | Returns a pointer to the [OH\_Drawing\_TextLine](../../structs/oh-drawing-textline/document.md) object of the truncated text line. |

#### \[h2\]OH\_Drawing\_TextLineGetTypographicBounds()

double OH\_Drawing\_TextLineGetTypographicBounds(OH\_Drawing\_TextLine\* line, double\* ascent, double\* descent,double\* leading)

**Description**

Obtains the typographic boundary of a text line object. The typographic boundary is related to the font and font size used for typography, but not the characters within the text.

For example, for the string " a b " (which has a space before "a" and a space after "b"), the typographic boundaries include the spaces at the beginning and end of the line. Similarly, the strings "j" and "E" have identical typographic boundaries, which are independent of the characters themselves.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TextLine](../../structs/oh-drawing-textline/document.md)\* line | Pointer to the [OH\_Drawing\_TextLine](../../structs/oh-drawing-textline/document.md) object. height = ascent + descent + leading. |
| double\* ascent | Pointer to the ascent of the text line object. |
| double\* descent | Pointer to the descent of the text line object. |
| double\* leading | Pointer to the leading of the text line object. |

**Returns**

| Type | Description |
| :-- | :-- |
| double | Returns the total width of the layout boundary. |

#### \[h2\]OH\_Drawing\_TextLineGetImageBounds()

OH\_Drawing\_Rect\* OH\_Drawing\_TextLineGetImageBounds(OH\_Drawing\_TextLine\* line)

**Description**

Obtains the image boundary of a text line object. The image boundary, equivalent to a visual boundary, is related to the font, font size, and characters.

For example, for the string " a b " (which has a space before "a" and a space after "b"), only "a b" are visible to users, and therefore the image boundary does not include these spaces at the beginning and end.

For the strings "j" and "E", their image boundaries are different. Specifically, the width of the boundary for "j" is narrower than that for "E", and the height of the boundary for "j" is taller than that for "E".

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TextLine](../../structs/oh-drawing-textline/document.md)\* line | Pointer to the [OH\_Drawing\_TextLine](../../structs/oh-drawing-textline/document.md) object. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_Rect](../../structs/oh-drawing-rect/document.md)\* | Returns the pointer to [OH\_Drawing\_Rect](../../structs/oh-drawing-rect/document.md) of the text line object. Release this pointer by calling [OH\_Drawing\_RectDestroy](../drawing-rect-h/document.md#oh_drawing_rectdestroy) when this object is no longer needed. |

#### \[h2\]OH\_Drawing\_TextLineGetTrailingSpaceWidth()

double OH\_Drawing\_TextLineGetTrailingSpaceWidth(OH\_Drawing\_TextLine\* line)

**Description**

Obtains the width of the spaces at the end of a text line object.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TextLine](../../structs/oh-drawing-textline/document.md)\* line | Pointer to the [OH\_Drawing\_TextLine](../../structs/oh-drawing-textline/document.md) object. |

**Returns**

| Type | Description |
| :-- | :-- |
| double | Returns the pointer to the width of the spaces. |

#### \[h2\]OH\_Drawing\_TextLineGetStringIndexForPosition()

int32\_t OH\_Drawing\_TextLineGetStringIndexForPosition(OH\_Drawing\_TextLine\* line, OH\_Drawing\_Point\* point)

**Description**

Obtains the index of a character at the specified position in a text line object.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TextLine](../../structs/oh-drawing-textline/document.md)\* line | Pointer to the [OH\_Drawing\_TextLine](../../structs/oh-drawing-textline/document.md) object. |
| [OH\_Drawing\_Point](../../structs/oh-drawing-point/document.md)\* point | Pointer to the index specified, which is an [OH\_Drawing\_Point](../../structs/oh-drawing-point/document.md) object. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | Returns the index of the character. For example, for the string "abc", the index of "a" is 0, the index of "b" is 1, and the index of "c" is 2. If the specified position is at "a", then **0** is returned. |

#### \[h2\]OH\_Drawing\_TextLineGetOffsetForStringIndex()

double OH\_Drawing\_TextLineGetOffsetForStringIndex(OH\_Drawing\_TextLine\* line, int32\_t index)

**Description**

Obtains the offset of a character with the specified index in a text line object.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TextLine](../../structs/oh-drawing-textline/document.md)\* line | Pointer to the [OH\_Drawing\_TextLine](../../structs/oh-drawing-textline/document.md) object. |
| int32\_t index | Index of the character. |

**Returns**

| Type | Description |
| :-- | :-- |
| double | Returns the offset. |

#### \[h2\]Drawing\_CaretOffsetsCallback()

typedef bool (\*Drawing\_CaretOffsetsCallback)(double offset, int32\_t index, bool leadingEdge)

**Description**

Defines a custom callback used to receive the offset and index of each character in a text line object as its parameters.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| double offset | Offset of each character in the text line object. |
| int32\_t index | Index of each character in the text line object. |
| bool leadingEdge | Whether the cursor is located at the leading edge of a character. **true** means that the cursor is located at the front of the character, that is, the offset does not contain the character width. **false** means that the cursor is located at the rear of the character, that is, the offset contains the character width. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | Whether to stop calling the callback. **true** means to stop; **false** otherwise. |

#### \[h2\]OH\_Drawing\_TextLineEnumerateCaretOffsets()

void OH\_Drawing\_TextLineEnumerateCaretOffsets(OH\_Drawing\_TextLine\* line, Drawing\_CaretOffsetsCallback callback)

**Description**

Enumerates the offset and index of each character in a text line object and passes them to a custom callback function. You can use the offset and index array for other operations.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TextLine](../../structs/oh-drawing-textline/document.md)\* line | Pointer to the [OH\_Drawing\_TextLine](../../structs/oh-drawing-textline/document.md) object. |
| [Drawing\_CaretOffsetsCallback](#drawing_caretoffsetscallback) callback | User-defined function [Drawing\_CaretOffsetsCallback](#drawing_caretoffsetscallback). |

#### \[h2\]OH\_Drawing\_TextLineGetAlignmentOffset()

double OH\_Drawing\_TextLineGetAlignmentOffset(OH\_Drawing\_TextLine\* line, double alignmentFactor, double alignmentWidth)

**Description**

Obtains the offset of a text line object after alignment based on the alignment factor and alignment width.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TextLine](../../structs/oh-drawing-textline/document.md)\* line | Pointer to the [OH\_Drawing\_TextLine](../../structs/oh-drawing-textline/document.md) object. |
| double alignmentFactor | Alignment factor, which determines how text is aligned. A value less than or equal to 0.0 means that the text is left-aligned; a value between 0.0 and 0.5 means that the text is slightly left-aligned; the value 0.5 means that the text is centered; a value between 0.5 and 1 means that the text is slightly right-aligned; a value greater than or equal to 1.0 means that the text is right-aligned. |
| double alignmentWidth | Alignment width, that is, the offset of the lower right corner of the text line object relative to the start position. If the specified alignment width is less than the actual width of the text line object, **0** is returned. |

**Returns**

| Type | Description |
| :-- | :-- |
| double | Returns the offset obtained. |
