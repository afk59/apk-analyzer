# drawing\_font.h

#### Overview

This file declares the functions related to the font in the drawing module.

**File to include**: <native\_drawing/drawing\_font.h>

**Library**: libnative\_drawing.so

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 11

**Related module**: [Drawing](../../modules/drawing/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_Drawing\_Font\_Metrics](../../structs/oh-drawing-font-metrics/document.md) | OH\_Drawing\_Font\_Metrics | Describes the measurement information about a font. |

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_Drawing\_FontHinting](#oh_drawing_fonthinting) | OH\_Drawing\_FontHinting | Defines an enum for the font hinting types. |
| [OH\_Drawing\_FontEdging](#oh_drawing_fontedging) | OH\_Drawing\_FontEdging | Defines an enum for the font edging types. |

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_FontGetSpacing(const OH\_Drawing\_Font\* font, float\* spacing)](#oh_drawing_fontgetspacing) | Obtains the recommended line spacing for a font. |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_FontGetPos(const OH\_Drawing\_Font\* font, const uint16\_t\* glyphs, int count,const OH\_Drawing\_Point\* origin, OH\_Drawing\_Point2D\* points)](#oh_drawing_fontgetpos) | Obtains the relative position of each glyph from the specified origin. |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_FontGetWidthsBounds(const OH\_Drawing\_Font\* font, const uint16\_t\* glyphs, int count,const OH\_Drawing\_Brush\* brush, const OH\_Drawing\_Pen\* pen, float\* widths, OH\_Drawing\_Array\* bounds)](#oh_drawing_fontgetwidthsbounds) | Obtains the width and bounding box of each glyph in a glyph array. |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_FontMeasureTextWithBrushOrPen(const OH\_Drawing\_Font\* font, const void\* text,size\_t byteLength, OH\_Drawing\_TextEncoding encoding, const OH\_Drawing\_Brush\* brush, const OH\_Drawing\_Pen\* pen,OH\_Drawing\_Rect\* bounds, float\* textWidth)](#oh_drawing_fontmeasuretextwithbrushorpen) | Obtains the width and bounding box of the text with a brush or pen. |
| [OH\_Drawing\_Font\* OH\_Drawing\_FontCreate(void)](#oh_drawing_fontcreate) | Creates an **OH\_Drawing\_Font** object. |
| [void OH\_Drawing\_FontSetBaselineSnap(OH\_Drawing\_Font\* font, bool baselineSnap)](#oh_drawing_fontsetbaselinesnap) | 
Sets whether to request that baselines be snapped to pixels when the current canvas matrix is axis aligned.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **font** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [bool OH\_Drawing\_FontIsBaselineSnap(const OH\_Drawing\_Font\* font)](#oh_drawing_fontisbaselinesnap) | 

Checks whether baselines are requested to be snapped to pixels when the current canvas matrix is axis aligned.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **font** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [void OH\_Drawing\_FontSetSubpixel(OH\_Drawing\_Font\* font, bool isSubpixel)](#oh_drawing_fontsetsubpixel) | 

Sets whether to use sub-pixel rendering for a font.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **font** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [bool OH\_Drawing\_FontIsSubpixel(const OH\_Drawing\_Font\* font)](#oh_drawing_fontissubpixel) | 

Checks whether sub-pixel rendering is used for a font.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **font** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [void OH\_Drawing\_FontSetForceAutoHinting(OH\_Drawing\_Font\* font, bool isForceAutoHinting)](#oh_drawing_fontsetforceautohinting) | 

Sets whether to forcibly use auto hinting, that is, whether to always hint glyphs.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **font** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [bool OH\_Drawing\_FontIsForceAutoHinting(const OH\_Drawing\_Font\* font)](#oh_drawing_fontisforceautohinting) | 

Checks whether auto hinting is forcibly used.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **font** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [void OH\_Drawing\_FontSetTypeface(OH\_Drawing\_Font\* font, OH\_Drawing\_Typeface\* typeface)](#oh_drawing_fontsettypeface) | 

Sets a typeface for a font.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **font** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [OH\_Drawing\_Typeface\* OH\_Drawing\_FontGetTypeface(OH\_Drawing\_Font\* font)](#oh_drawing_fontgettypeface) | 

Obtains the typeface of a font.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **font** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [void OH\_Drawing\_FontSetTextSize(OH\_Drawing\_Font\* font, float textSize)](#oh_drawing_fontsettextsize) | 

Sets the text size for a font object.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **font** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [float OH\_Drawing\_FontGetTextSize(const OH\_Drawing\_Font\* font)](#oh_drawing_fontgettextsize) | 

Obtains the text size of a font object.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **font** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [int OH\_Drawing\_FontCountText(OH\_Drawing\_Font\* font, const void\* text, size\_t byteLength,OH\_Drawing\_TextEncoding encoding)](#oh_drawing_fontcounttext) | 

Obtains the number of glyphs represented by text.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **font** or **text** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [uint32\_t OH\_Drawing\_FontTextToGlyphs(const OH\_Drawing\_Font\* font, const void\* text, uint32\_t byteLength,OH\_Drawing\_TextEncoding encoding, uint16\_t\* glyphs, int maxGlyphCount)](#oh_drawing_fonttexttoglyphs) | 

Converts text into glyph indices.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If any of **font**, **text**, and **glyphs** is NULL, **byteLength** is **0**, or **maxGlyphCount** is less than or equal to 0, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [void OH\_Drawing\_FontGetWidths(const OH\_Drawing\_Font\* font, const uint16\_t\* glyphs, int count, float\* widths)](#oh_drawing_fontgetwidths) | 

Obtains the width of each glyph in a string of text.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If any of **font**, **glyphs**, and **widths** is NULL or **count** is less than or equal to 0, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_FontMeasureSingleCharacter(const OH\_Drawing\_Font\* font, const char\* str,float\* textWidth)](#oh_drawing_fontmeasuresinglecharacter) | Measures the width of a single character. If the typeface of the current font does not support the character to measure, the system typeface is used to measure the character width. |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_FontMeasureText(const OH\_Drawing\_Font\* font, const void\* text, size\_t byteLength,OH\_Drawing\_TextEncoding encoding, OH\_Drawing\_Rect\* bounds, float\* textWidth)](#oh_drawing_fontmeasuretext) | Obtains the text width and bounding box. |
| [void OH\_Drawing\_FontSetLinearText(OH\_Drawing\_Font\* font, bool isLinearText)](#oh_drawing_fontsetlineartext) | 

Sets linear scaling for a font.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **font** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [bool OH\_Drawing\_FontIsLinearText(const OH\_Drawing\_Font\* font)](#oh_drawing_fontislineartext) | 

Checks whether linear scaling is used for a font object.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **font** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [void OH\_Drawing\_FontSetTextSkewX(OH\_Drawing\_Font\* font, float skewX)](#oh_drawing_fontsettextskewx) | 

Sets a horizontal skew factor for a font.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **font** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [float OH\_Drawing\_FontGetTextSkewX(const OH\_Drawing\_Font\* font)](#oh_drawing_fontgettextskewx) | 

Obtains the horizontal skew factor of a font.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **font** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [void OH\_Drawing\_FontSetFakeBoldText(OH\_Drawing\_Font\* font, bool isFakeBoldText)](#oh_drawing_fontsetfakeboldtext) | 

Sets fake bold for a font by increasing the stroke width.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **font** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [bool OH\_Drawing\_FontIsFakeBoldText(const OH\_Drawing\_Font\* font)](#oh_drawing_fontisfakeboldtext) | 

Checks whether fake bold is used for a font.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **font** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [void OH\_Drawing\_FontSetScaleX(OH\_Drawing\_Font\* font, float scaleX)](#oh_drawing_fontsetscalex) | 

Sets a horizontal scale factor for a font.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **font** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [float OH\_Drawing\_FontGetScaleX(const OH\_Drawing\_Font\* font)](#oh_drawing_fontgetscalex) | 

Obtains the horizontal scale ratio of this font.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **font** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [void OH\_Drawing\_FontSetHinting(OH\_Drawing\_Font\* font, OH\_Drawing\_FontHinting fontHinting)](#oh_drawing_fontsethinting) | 

Sets a font hinting effect.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **font** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

If **fontHinting** is not set to one of the enumerated values, **OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE** is returned.

 |
| [OH\_Drawing\_FontHinting OH\_Drawing\_FontGetHinting(const OH\_Drawing\_Font\* font)](#oh_drawing_fontgethinting) | 

Obtains the font hinting effect.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **font** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [void OH\_Drawing\_FontSetEmbeddedBitmaps(OH\_Drawing\_Font\* font, bool isEmbeddedBitmaps)](#oh_drawing_fontsetembeddedbitmaps) | 

Sets whether to use bitmaps in a font.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **font** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [bool OH\_Drawing\_FontIsEmbeddedBitmaps(const OH\_Drawing\_Font\* font)](#oh_drawing_fontisembeddedbitmaps) | 

Checks whether bitmaps are used in a font.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **font** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [void OH\_Drawing\_FontSetEdging(OH\_Drawing\_Font\* font, OH\_Drawing\_FontEdging fontEdging)](#oh_drawing_fontsetedging) | 

Sets a font edging effect.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **font** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

If **fontEdging** is not set to one of the enumerated values, **OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE** is returned.

 |
| [OH\_Drawing\_FontEdging OH\_Drawing\_FontGetEdging(const OH\_Drawing\_Font\* font)](#oh_drawing_fontgetedging) | 

Obtains the font edging effect.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **font** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [void OH\_Drawing\_FontDestroy(OH\_Drawing\_Font\* font)](#oh_drawing_fontdestroy) | Destroys an **OH\_Drawing\_Font** object and reclaims the memory occupied by the object. |
| [float OH\_Drawing\_FontGetMetrics(OH\_Drawing\_Font\* font, OH\_Drawing\_Font\_Metrics\* fontMetrics)](#oh_drawing_fontgetmetrics) | 

Obtains the measurement information about a font.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **font** or **fontMetrics** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_FontGetBounds(const OH\_Drawing\_Font\* font, const uint16\_t\* glyphs, uint32\_t count,OH\_Drawing\_Array\* bounds)](#oh_drawing_fontgetbounds) | Obtains the rectangular bounding box for each glyph in the glyph array. |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_FontGetPathForGlyph(const OH\_Drawing\_Font\* font, uint16\_t glyph,OH\_Drawing\_Path\* path)](#oh_drawing_fontgetpathforglyph) | Obtains the path of a glyph. |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_FontGetTextPath(const OH\_Drawing\_Font\* font, const void\* text, size\_t byteLength,OH\_Drawing\_TextEncoding encoding, float x, float y, OH\_Drawing\_Path\* path)](#oh_drawing_fontgettextpath) | Obtains the text outline path. |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_FontSetThemeFontFollowed(OH\_Drawing\_Font\* font, bool followed)](#oh_drawing_fontsetthemefontfollowed) | Sets whether to follow the theme font. When **followed** is set to **true**, the theme font is used if it is enabled by the system and no typeface is set. |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_FontIsThemeFontFollowed(const OH\_Drawing\_Font\* font, bool\* followed)](#oh_drawing_fontisthemefontfollowed) | Checks whether the font follows the theme font. By default, the theme font is not followed. |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_FontMeasureSingleCharacterWithFeatures(const OH\_Drawing\_Font\* font, const char\* str,const OH\_Drawing\_FontFeatures\* fontFeatures, float\* textWidth)](#oh_drawing_fontmeasuresinglecharacterwithfeatures) | Measures the width of a single character with font features. If the typeface of the current font does not support the character to measure, the system typeface is used to measure the character width. |
| [OH\_Drawing\_FontFeatures\* OH\_Drawing\_FontFeaturesCreate(void)](#oh_drawing_fontfeaturescreate) | Creates an **OH\_Drawing\_FontFeatures** object. |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_FontFeaturesAddFeature(OH\_Drawing\_FontFeatures\* fontFeatures,const char\* name, float value)](#oh_drawing_fontfeaturesaddfeature) | Adds a font feature to an **OH\_Drawing\_FontFeatures** object. |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_FontFeaturesDestroy(OH\_Drawing\_FontFeatures\* fontFeatures)](#oh_drawing_fontfeaturesdestroy) | Destroys an **OH\_Drawing\_FontFeatures** object and reclaims the memory occupied by the object. |

#### Enum Description

#### \[h2\]OH\_Drawing\_FontHinting

enum OH\_Drawing\_FontHinting

**Description**

Defines an enum for the font hinting types.

**Since**: 12

| Value | Description |
| :-- | :-- |
| FONT\_HINTING\_NONE | No font hinting is used. |
| FONT\_HINTING\_SLIGHT | Slight font hinting is used to improve contrast. |
| FONT\_HINTING\_NORMAL | Normal font hinting is used to improve contrast. |
| FONT\_HINTING\_FULL | Full font hinting is used to improve contrast. |

#### \[h2\]OH\_Drawing\_FontEdging

enum OH\_Drawing\_FontEdging

**Description**

Enumerates the font edging types.

**Since**: 12

| Value | Description |
| :-- | :-- |
| FONT\_EDGING\_ALIAS | No anti-aliasing processing is used. |
| FONT\_EDGING\_ANTI\_ALIAS | Uses anti-aliasing to smooth the jagged edges. |
| FONT\_EDGING\_SUBPIXEL\_ANTI\_ALIAS | Uses sub-pixel anti-aliasing to provide a smoother effect for jagged edges. |

#### Function Description

#### \[h2\]OH\_Drawing\_FontMeasureSingleCharacterWithFeatures()

OH\_Drawing\_ErrorCode OH\_Drawing\_FontMeasureSingleCharacterWithFeatures(const OH\_Drawing\_Font\* font, const char\* str, const OH\_Drawing\_FontFeatures\* fontFeatures, float\* textWidth)

**Description**

Measures the width of a single character with font features. If the typeface of the current font does not support the character to measure, the system typeface is used to measure the character width.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [const OH\_Drawing\_Font](../../structs/oh-drawing-font/document.md)\* font | Pointer to the [OH\_Drawing\_Font](../../structs/oh-drawing-font/document.md) object. |
| const char\* str | Pointer to the single character to measure. A string can be passed in, but only the first character in the string is parsed and measured in UTF-8 encoding. |
| [const OH\_Drawing\_FontFeatures](../../structs/oh-drawing-fontfeatures/document.md)\* fontFeatures | Pointer to the [OH\_Drawing\_FontFeatures](../../structs/oh-drawing-fontfeatures/document.md) object. If no font feature is set, the preset font feature in the TrueType fonts (TTF) file is used. |
| float\* textWidth | Pointer to the obtained text width, which is used as an output parameter. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_ErrorCode](../drawing-error-code-h/document.md#oh_drawing_errorcode) | 
Execution result.

**OH\_DRAWING\_SUCCESS** if the operation is successful.

Returns **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** if at least one of the parameters **font**, **str**, **fontFeatures**, or **textWidth** is NULL, or the length of **str** is **0**.

 |

#### \[h2\]OH\_Drawing\_FontFeaturesCreate()

OH\_Drawing\_FontFeatures\* OH\_Drawing\_FontFeaturesCreate(void)

**Description**

Creates an **OH\_Drawing\_FontFeatures** object.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 20

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_FontFeatures](../../structs/oh-drawing-fontfeatures/document.md)\* | 
Returns a pointer to the created [OH\_Drawing\_FontFeatures](../../structs/oh-drawing-fontfeatures/document.md) object.

If a null pointer is returned, the creation fails. A possible cause is that no memory is available.

 |

#### \[h2\]OH\_Drawing\_FontFeaturesAddFeature()

OH\_Drawing\_ErrorCode OH\_Drawing\_FontFeaturesAddFeature(OH\_Drawing\_FontFeatures\* fontFeatures, const char\* name, float value)

**Description**

Adds a font feature to an **OH\_Drawing\_FontFeatures** object.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_FontFeatures](../../structs/oh-drawing-fontfeatures/document.md)\* fontFeatures | Pointer to the [OH\_Drawing\_FontFeatures](../../structs/oh-drawing-fontfeatures/document.md) object. |
| const char\* name | Name of a font feature. Common font feature names include **liga**, **frac**, and **case**. A font feature needs a TTF file to work. |
| float value | Value of the font feature. You are advised to determine the valid value range by using a font viewing tool or referring to the font document. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_ErrorCode](../drawing-error-code-h/document.md#oh_drawing_errorcode) | 
Execution result.

**OH\_DRAWING\_SUCCESS** if the operation is successful.

Returns **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** if **fontFeatures** or **name** is a null pointer.

 |

#### \[h2\]OH\_Drawing\_FontFeaturesDestroy()

OH\_Drawing\_ErrorCode OH\_Drawing\_FontFeaturesDestroy(OH\_Drawing\_FontFeatures\* fontFeatures)

**Description**

Destroys an **OH\_Drawing\_FontFeatures** object and reclaims the memory occupied by the object.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_FontFeatures](../../structs/oh-drawing-fontfeatures/document.md)\* fontFeatures | Pointer to the [OH\_Drawing\_FontFeatures](../../structs/oh-drawing-fontfeatures/document.md) object. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_ErrorCode](../drawing-error-code-h/document.md#oh_drawing_errorcode) | 
Execution result.

**OH\_DRAWING\_SUCCESS** if the operation is successful.

Returns **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** if **fontFeatures** is NULL.

 |

#### \[h2\]OH\_Drawing\_FontMeasureTextWithBrushOrPen()

OH\_Drawing\_ErrorCode OH\_Drawing\_FontMeasureTextWithBrushOrPen(const OH\_Drawing\_Font\* font, const void\* text,size\_t byteLength, OH\_Drawing\_TextEncoding encoding, const OH\_Drawing\_Brush\* brush, const OH\_Drawing\_Pen\* pen,OH\_Drawing\_Rect\* bounds, float\* textWidth)

**Description**

Obtains the width and bounding box of the text with a brush or pen.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| const OH\_Drawing\_Font\* font | Pointer to the [OH\_Drawing\_Font](../../structs/oh-drawing-font/document.md) object. |
| const void\* text | Pointer to the text. |
| size\_t byteLength | Length of the text, in bytes. |
| [OH\_Drawing\_TextEncoding](../drawing-types-h/document.md#oh_drawing_textencoding) encoding | Encoding type of the text. |
| const OH\_Drawing\_Brush\* brush | Pointer to the [OH\_Drawing\_Brush](../../structs/oh-drawing-brush/document.md) object. |
| const OH\_Drawing\_Pen\* pen | Pointer to the [OH\_Drawing\_Pen](../../structs/oh-drawing-pen/document.md) object. |
| OH\_Drawing\_Rect\* bounds | Pointer to the bounding box. The value can be NULL. |
| float\* textWidth | Pointer to the text width. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_ErrorCode](../drawing-error-code-h/document.md#oh_drawing_errorcode) | 
Operation code.

**OH\_DRAWING\_SUCCESS** if the operation is successful.

Returns **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** if any of **font**, **text**, or **textWidth** is NULL, **byteLength** is **0**, or a brush and a pen both exist.

 |

#### \[h2\]OH\_Drawing\_FontGetWidthsBounds()

OH\_Drawing\_ErrorCode OH\_Drawing\_FontGetWidthsBounds(const OH\_Drawing\_Font\* font, const uint16\_t\* glyphs, int count,const OH\_Drawing\_Brush\* brush, const OH\_Drawing\_Pen\* pen, float\* widths, OH\_Drawing\_Array\* bounds)

**Description**

Obtains the width and bounding box of each glyph in a glyph array.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| const OH\_Drawing\_Font\* font | Pointer to the [OH\_Drawing\_Font](../../structs/oh-drawing-font/document.md) object. |
| const uint16\_t\* glyphs | Pointer to the start address for storing the glyph indices. |
| int count | Number of glyph indices, which must be the same as the size of glyphs array. |
| const OH\_Drawing\_Brush\* brush | Pointer to the [OH\_Drawing\_Brush](../../structs/oh-drawing-brush/document.md) object. |
| const OH\_Drawing\_Pen\* pen | Pointer to the [OH\_Drawing\_Pen](../../structs/oh-drawing-pen/document.md) object. |
| float\* widths | Start address for storing the glyph width. |
| OH\_Drawing\_Array\* bounds | Start address for storing the glyph bounding box. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_ErrorCode](../drawing-error-code-h/document.md#oh_drawing_errorcode) | 
Operation code.

**OH\_DRAWING\_SUCCESS** if the operation is successful.

Returns **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** if either **font** or **glyphs** is NULL, **count** is not greater than **0**, a brush and a pen both exist, or both **widths** and **bounds** are NULL.

 |

#### \[h2\]OH\_Drawing\_FontGetPos()

OH\_Drawing\_ErrorCode OH\_Drawing\_FontGetPos(const OH\_Drawing\_Font\* font, const uint16\_t\* glyphs, int count,const OH\_Drawing\_Point\* origin, OH\_Drawing\_Point2D\* points)

**Description**

Obtains the relative position of each glyph from the specified origin.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| const OH\_Drawing\_Font\* font | Pointer to the [OH\_Drawing\_Font](../../structs/oh-drawing-font/document.md) object. |
| const uint16\_t\* glyphs | Pointer to the start address for storing the glyph indices. |
| int count | Number of glyph indices, which must be the same as the size of glyphs array. |
| const OH\_Drawing\_Point\* origin | Position of the first glyph. The value can be NULL, which means that the default value **(0, 0)** is used. |
| [OH\_Drawing\_Point2D](../../structs/oh-drawing-point2d/document.md)\* points | Start address for storing the relative position of a glyph. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_ErrorCode](../drawing-error-code-h/document.md#oh_drawing_errorcode) | 
Operation code.

**OH\_DRAWING\_SUCCESS** if the operation is successful.

Returns **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** if any of **font**, **glyphs**, and **points** is NULL, or **count** is less than or equal to **0**.

 |

#### \[h2\]OH\_Drawing\_FontGetSpacing()

OH\_Drawing\_ErrorCode OH\_Drawing\_FontGetSpacing(const OH\_Drawing\_Font\* font, float\* spacing)

**Description**

Obtains the recommended line spacing for a font.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| const OH\_Drawing\_Font\* font | Pointer to the [OH\_Drawing\_Font](../../structs/oh-drawing-font/document.md) object. |
| float\* spacing | Recommended line spacing for a font. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_ErrorCode](../drawing-error-code-h/document.md#oh_drawing_errorcode) | 
Operation code.

**OH\_DRAWING\_SUCCESS** if the operation is successful.

Returns **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** if either **font** or **spacing** is NULL.

 |

#### \[h2\]OH\_Drawing\_FontCreate()

OH\_Drawing\_Font\* OH\_Drawing\_FontCreate(void)

**Description**

Creates an **OH\_Drawing\_Font** object.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 11

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_Font](../../structs/oh-drawing-font/document.md)\* | Returns the pointer to the **OH\_Drawing\_Font** object created. |

#### \[h2\]OH\_Drawing\_FontSetBaselineSnap()

void OH\_Drawing\_FontSetBaselineSnap(OH\_Drawing\_Font\* font, bool baselineSnap)

**Description**

Sets whether to request that baselines be snapped to pixels when the current canvas matrix is axis aligned.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **font** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Font](../../structs/oh-drawing-font/document.md)\* font | Pointer to the [OH\_Drawing\_Font](../../structs/oh-drawing-font/document.md) object. |
| bool baselineSnap | Whether the font baseline is snapped to pixels. **true** means yes; **false** otherwise. |

#### \[h2\]OH\_Drawing\_FontIsBaselineSnap()

bool OH\_Drawing\_FontIsBaselineSnap(const OH\_Drawing\_Font\* font)

**Description**

Checks whether baselines are requested to be snapped to pixels when the current canvas matrix is axis aligned.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **font** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [OH\_Drawing\_Font](../../structs/oh-drawing-font/document.md)\* font | Pointer to the [OH\_Drawing\_Font](../../structs/oh-drawing-font/document.md) object. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | Whether the font baseline is snapped to pixels. **true** means yes; **false** otherwise. |

#### \[h2\]OH\_Drawing\_FontSetSubpixel()

void OH\_Drawing\_FontSetSubpixel(OH\_Drawing\_Font\* font, bool isSubpixel)

**Description**

Sets whether to use sub-pixel rendering for a font.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **font** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Font](../../structs/oh-drawing-font/document.md)\* font | Pointer to the [OH\_Drawing\_Font](../../structs/oh-drawing-font/document.md) object. |
| bool isSubpixel | Whether sub-pixel rendering is used for a font. **true** means yes; **false** otherwise. |

#### \[h2\]OH\_Drawing\_FontIsSubpixel()

bool OH\_Drawing\_FontIsSubpixel(const OH\_Drawing\_Font\* font)

**Description**

Checks whether sub-pixel rendering is used for a font.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **font** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [OH\_Drawing\_Font](../../structs/oh-drawing-font/document.md)\* font | Pointer to the [OH\_Drawing\_Font](../../structs/oh-drawing-font/document.md) object. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | Whether sub-pixel rendering is used for a font. **true** means yes; **false** otherwise. |

#### \[h2\]OH\_Drawing\_FontSetForceAutoHinting()

void OH\_Drawing\_FontSetForceAutoHinting(OH\_Drawing\_Font\* font, bool isForceAutoHinting)

**Description**

Sets whether to forcibly use auto hinting, that is, whether to always hint glyphs.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **font** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Font](../../structs/oh-drawing-font/document.md)\* font | Pointer to the [OH\_Drawing\_Font](../../structs/oh-drawing-font/document.md) object. |
| bool isForceAutoHinting | Whether to forcibly use auto hinting, that is, whether to always hint glyphs. **true** means yes; **false** otherwise. |

#### \[h2\]OH\_Drawing\_FontIsForceAutoHinting()

bool OH\_Drawing\_FontIsForceAutoHinting(const OH\_Drawing\_Font\* font)

**Description**

Checks whether auto hinting is forcibly used.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **font** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [OH\_Drawing\_Font](../../structs/oh-drawing-font/document.md)\* font | Pointer to the [OH\_Drawing\_Font](../../structs/oh-drawing-font/document.md) object. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | Whether auto hinting is forcibly used. **true** means yes; **false** otherwise. |

#### \[h2\]OH\_Drawing\_FontSetTypeface()

void OH\_Drawing\_FontSetTypeface(OH\_Drawing\_Font\* font, OH\_Drawing\_Typeface\* typeface)

**Description**

Sets a typeface for a font.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **font** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Font](../../structs/oh-drawing-font/document.md)\* font | Pointer to an **OH\_Drawing\_Font** object. |
| [OH\_Drawing\_Typeface](../../structs/oh-drawing-typeface/document.md)\* typeface | Pointer to an **OH\_Drawing\_Typeface** object. If NULL is passed in, the default **OH\_Drawing\_Typeface** object is used. |

#### \[h2\]OH\_Drawing\_FontGetTypeface()

OH\_Drawing\_Typeface\* OH\_Drawing\_FontGetTypeface(OH\_Drawing\_Font\* font)

**Description**

Obtains the typeface of a font.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **font** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Font](../../structs/oh-drawing-font/document.md)\* font | Pointer to the [OH\_Drawing\_Font](../../structs/oh-drawing-font/document.md) object. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_Typeface](../../structs/oh-drawing-typeface/document.md)\* | Returns a pointer to the [OH\_Drawing\_Typeface](../../structs/oh-drawing-typeface/document.md) object. |

#### \[h2\]OH\_Drawing\_FontSetTextSize()

void OH\_Drawing\_FontSetTextSize(OH\_Drawing\_Font\* font, float textSize)

**Description**

Sets the text size for a font object.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **font** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Font](../../structs/oh-drawing-font/document.md)\* font | Pointer to an **OH\_Drawing\_Font** object. |
| float textSize | Text size. The value is a floating point number. If a negative number is passed in, the size is set to 0. If the size is 0, the text drawn will not be displayed. |

#### \[h2\]OH\_Drawing\_FontGetTextSize()

float OH\_Drawing\_FontGetTextSize(const OH\_Drawing\_Font\* font)

**Description**

Obtains the text size of a font object.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **font** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [OH\_Drawing\_Font](../../structs/oh-drawing-font/document.md)\* font | Pointer to the [OH\_Drawing\_Font](../../structs/oh-drawing-font/document.md) object. |

**Returns**

| Type | Description |
| :-- | :-- |
| float | Returns a floating point number representing the text size. |

#### \[h2\]OH\_Drawing\_FontCountText()

int OH\_Drawing\_FontCountText(OH\_Drawing\_Font\* font, const void\* text, size\_t byteLength,OH\_Drawing\_TextEncoding encoding)

**Description**

Obtains the number of glyphs represented by text.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **font** or **text** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Font](../../structs/oh-drawing-font/document.md)\* font | Pointer to the [OH\_Drawing\_Font](../../structs/oh-drawing-font/document.md) object. |
| const void\* text | Pointer to the start address of the storage. |
| size\_t byteLength | Text length, in bytes. |
| [OH\_Drawing\_TextEncoding](../drawing-types-h/document.md#oh_drawing_textencoding) encoding | Text encoding type [OH\_Drawing\_TextEncoding](../drawing-types-h/document.md#oh_drawing_textencoding). |

**Returns**

| Type | Description |
| :-- | :-- |
| int | Number of glyphs represented by the text. The value is an integer. |

#### \[h2\]OH\_Drawing\_FontTextToGlyphs()

uint32\_t OH\_Drawing\_FontTextToGlyphs(const OH\_Drawing\_Font\* font, const void\* text, uint32\_t byteLength,OH\_Drawing\_TextEncoding encoding, uint16\_t\* glyphs, int maxGlyphCount)

**Description**

Converts text into glyph indices.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If any of **font**, **text**, and **glyphs** is NULL, **byteLength** is **0**, or **maxGlyphCount** is less than or equal to 0, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [OH\_Drawing\_Font](../../structs/oh-drawing-font/document.md)\* font | Pointer to the [OH\_Drawing\_Font](../../structs/oh-drawing-font/document.md) object. |
| const void\* text | Pointer to the start address of the storage. |
| uint32\_t byteLength | Text length, in bytes. |
| [OH\_Drawing\_TextEncoding](../drawing-types-h/document.md#oh_drawing_textencoding) encoding | Text encoding type [OH\_Drawing\_TextEncoding](../drawing-types-h/document.md#oh_drawing_textencoding). |
| uint16\_t\* glyphs | Pointer to the start address for storing the glyph indices. |
| int maxGlyphCount | Maximum number of glyphs. |

**Returns**

| Type | Description |
| :-- | :-- |
| uint32\_t | Returns the number of glyph indices. |

#### \[h2\]OH\_Drawing\_FontGetWidths()

void OH\_Drawing\_FontGetWidths(const OH\_Drawing\_Font\* font, const uint16\_t\* glyphs, int count, float\* widths)

**Description**

Obtains the width of each glyph in a string of text.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If any of **font**, **glyphs**, and **widths** is NULL, or **count** is **0**, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [OH\_Drawing\_Font](../../structs/oh-drawing-font/document.md)\* font | Pointer to the [OH\_Drawing\_Font](../../structs/oh-drawing-font/document.md) object. |
| const uint16\_t\* glyphs | Pointer to the start address for storing the glyph indices. |
| int count | Number of glyph indices. |
| float\* widths | Pointer to the start address for storing the glyph widths. |

#### \[h2\]OH\_Drawing\_FontMeasureSingleCharacter()

OH\_Drawing\_ErrorCode OH\_Drawing\_FontMeasureSingleCharacter(const OH\_Drawing\_Font\* font, const char\* str,float\* textWidth)

**Description**

Measures the width of a single character. If the typeface of the current font does not support the character to measure, the system typeface is used to measure the character width.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [OH\_Drawing\_Font](../../structs/oh-drawing-font/document.md)\* font | Pointer to the [OH\_Drawing\_Font](../../structs/oh-drawing-font/document.md) object. |
| const char\* str | Pointer to the single character to measure. A string can be passed in, but only the first character in the string is parsed and measured in UTF-8 encoding. |
| float\* textWidth | Pointer to the character width obtained. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_ErrorCode](../drawing-error-code-h/document.md#oh_drawing_errorcode) | 
Returns one of the following result codes:

**OH\_DRAWING\_SUCCESS** if the operation is successful.

**OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** if at least one of the parameters **font**, **str**, or **textWidth** is NULL, or the length of **str** is **0**.

 |

#### \[h2\]OH\_Drawing\_FontMeasureText()

OH\_Drawing\_ErrorCode OH\_Drawing\_FontMeasureText(const OH\_Drawing\_Font\* font, const void\* text, size\_t byteLength,OH\_Drawing\_TextEncoding encoding, OH\_Drawing\_Rect\* bounds, float\* textWidth)

**Description**

Obtains the text width and bounding box.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [OH\_Drawing\_Font](../../structs/oh-drawing-font/document.md)\* font | Pointer to the [OH\_Drawing\_Font](../../structs/oh-drawing-font/document.md) object. |
| const void\* text | Pointer to the text. |
| size\_t byteLength | Length of the text, in bytes. |
| [OH\_Drawing\_TextEncoding](../drawing-types-h/document.md#oh_drawing_textencoding) encoding | Encoding type of the text. |
| [OH\_Drawing\_Rect](../../structs/oh-drawing-rect/document.md)\* bounds | Pointer to the bounding box. The value can be NULL. |
| float\* textWidth | Pointer to the text width. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_ErrorCode](../drawing-error-code-h/document.md#oh_drawing_errorcode) | 
Returns one of the following result codes:

**OH\_DRAWING\_SUCCESS** if the operation is successful.

**OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** if at least one of the parameters **font**, **text**, and **textWidth** is NULL, or **byteLength** is **0**.

 |

#### \[h2\]OH\_Drawing\_FontSetLinearText()

void OH\_Drawing\_FontSetLinearText(OH\_Drawing\_Font\* font, bool isLinearText)

**Description**

Sets linear scaling for a font.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **font** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Font](../../structs/oh-drawing-font/document.md)\* font | Pointer to an **OH\_Drawing\_Font** object. |
| bool isLinearText | Whether to enable linear scaling. The value **true** means to enable linear scaling, and **false** means the opposite. |

#### \[h2\]OH\_Drawing\_FontIsLinearText()

bool OH\_Drawing\_FontIsLinearText(const OH\_Drawing\_Font\* font)

**Description**

Checks whether linear scaling is used for a font object.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **font** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [OH\_Drawing\_Font](../../structs/oh-drawing-font/document.md)\* font | Pointer to the [OH\_Drawing\_Font](../../structs/oh-drawing-font/document.md) object. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | Returns **true** if linear scaling is used; returns **false** otherwise. |

#### \[h2\]OH\_Drawing\_FontSetTextSkewX()

void OH\_Drawing\_FontSetTextSkewX(OH\_Drawing\_Font\* font, float skewX)

**Description**

Sets a horizontal skew factor for a font.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **font** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Font](../../structs/oh-drawing-font/document.md)\* font | Pointer to an **OH\_Drawing\_Font** object. |
| float skewX | Skew of the X axis relative to the Y axis. |

#### \[h2\]OH\_Drawing\_FontGetTextSkewX()

float OH\_Drawing\_FontGetTextSkewX(const OH\_Drawing\_Font\* font)

**Description**

Obtains the horizontal skew factor of a font.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **font** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [OH\_Drawing\_Font](../../structs/oh-drawing-font/document.md)\* font | Pointer to the [OH\_Drawing\_Font](../../structs/oh-drawing-font/document.md) object. |

**Returns**

| Type | Description |
| :-- | :-- |
| float | Returns a floating point number representing the horizontal skew factor. |

#### \[h2\]OH\_Drawing\_FontSetFakeBoldText()

void OH\_Drawing\_FontSetFakeBoldText(OH\_Drawing\_Font\* font, bool isFakeBoldText)

**Description**

Sets fake bold for a font by increasing the stroke width.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **font** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Font](../../structs/oh-drawing-font/document.md)\* font | Pointer to an **OH\_Drawing\_Font** object. |
| bool isFakeBoldText | Whether to set fake bold. The value **true** means to set fake bold, and **false** means the opposite. |

#### \[h2\]OH\_Drawing\_FontIsFakeBoldText()

bool OH\_Drawing\_FontIsFakeBoldText(const OH\_Drawing\_Font\* font)

**Description**

Checks whether fake bold is used for a font.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **font** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [OH\_Drawing\_Font](../../structs/oh-drawing-font/document.md)\* font | Pointer to the [OH\_Drawing\_Font](../../structs/oh-drawing-font/document.md) object. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | Whether fake bold is used for a font. **true** means yes; **false** otherwise. |

#### \[h2\]OH\_Drawing\_FontSetScaleX()

void OH\_Drawing\_FontSetScaleX(OH\_Drawing\_Font\* font, float scaleX)

**Description**

Sets a horizontal scale factor for a font.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **font** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Font](../../structs/oh-drawing-font/document.md)\* font | Pointer to the [OH\_Drawing\_Font](../../structs/oh-drawing-font/document.md) object. |
| float scaleX | Horizontal scale factor. |

#### \[h2\]OH\_Drawing\_FontGetScaleX()

float OH\_Drawing\_FontGetScaleX(const OH\_Drawing\_Font\* font)

**Description**

Obtains the horizontal scale ratio of this font.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **font** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [OH\_Drawing\_Font](../../structs/oh-drawing-font/document.md)\* font | Pointer to the [OH\_Drawing\_Font](../../structs/oh-drawing-font/document.md) object. |

**Returns**

| Type | Description |
| :-- | :-- |
| float | Returns the horizontal scale factor. |

#### \[h2\]OH\_Drawing\_FontSetHinting()

void OH\_Drawing\_FontSetHinting(OH\_Drawing\_Font\* font, OH\_Drawing\_FontHinting fontHinting)

**Description**

Sets a font hinting effect.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **font** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

If **fontHinting** is not set to one of the enumerated values, **OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Font](../../structs/oh-drawing-font/document.md)\* font | Pointer to the [OH\_Drawing\_Font](../../structs/oh-drawing-font/document.md) object. |
| [OH\_Drawing\_FontHinting](#oh_drawing_fonthinting) fontHinting | Enumeration of font hinting types [OH\_Drawing\_FontHinting](#oh_drawing_fonthinting). |

#### \[h2\]OH\_Drawing\_FontGetHinting()

OH\_Drawing\_FontHinting OH\_Drawing\_FontGetHinting(const OH\_Drawing\_Font\* font)

**Description**

Obtains the font hinting effect.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **font** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [OH\_Drawing\_Font](../../structs/oh-drawing-font/document.md)\* font | Pointer to the [OH\_Drawing\_Font](../../structs/oh-drawing-font/document.md) object. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_FontHinting](#oh_drawing_fonthinting) | Returns the enumeration of font hinting types [OH\_Drawing\_FontHinting](#oh_drawing_fonthinting). |

#### \[h2\]OH\_Drawing\_FontSetEmbeddedBitmaps()

void OH\_Drawing\_FontSetEmbeddedBitmaps(OH\_Drawing\_Font\* font, bool isEmbeddedBitmaps)

**Description**

Sets whether to use bitmaps in a font.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **font** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Font](../../structs/oh-drawing-font/document.md)\* font | Pointer to the [OH\_Drawing\_Font](../../structs/oh-drawing-font/document.md) object. |
| bool isEmbeddedBitmaps | Whether to use bitmaps in the font. The value **true** means to use bitmaps in the font, and **false** means the opposite. |

#### \[h2\]OH\_Drawing\_FontIsEmbeddedBitmaps()

bool OH\_Drawing\_FontIsEmbeddedBitmaps(const OH\_Drawing\_Font\* font)

**Description**

Checks whether bitmaps are used in a font.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **font** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [OH\_Drawing\_Font](../../structs/oh-drawing-font/document.md)\* font | Pointer to the [OH\_Drawing\_Font](../../structs/oh-drawing-font/document.md) object. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | Returns **true** if bitmaps are used; returns **false** otherwise. |

#### \[h2\]OH\_Drawing\_FontSetEdging()

void OH\_Drawing\_FontSetEdging(OH\_Drawing\_Font\* font, OH\_Drawing\_FontEdging fontEdging)

**Description**

Sets a font edging effect.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **font** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

If **fontEdging** is not set to one of the enumerated values, **OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Font](../../structs/oh-drawing-font/document.md)\* font | Pointer to the [OH\_Drawing\_Font](../../structs/oh-drawing-font/document.md) object. |
| [OH\_Drawing\_FontEdging](#oh_drawing_fontedging) fontEdging | Font edging effect. |

#### \[h2\]OH\_Drawing\_FontGetEdging()

OH\_Drawing\_FontEdging OH\_Drawing\_FontGetEdging(const OH\_Drawing\_Font\* font)

**Description**

Obtains the font edging effect.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **font** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [OH\_Drawing\_Font](../../structs/oh-drawing-font/document.md)\* font | Pointer to the [OH\_Drawing\_Font](../../structs/oh-drawing-font/document.md) object. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_FontEdging](#oh_drawing_fontedging) | Font edging effect. |

#### \[h2\]OH\_Drawing\_FontDestroy()

void OH\_Drawing\_FontDestroy(OH\_Drawing\_Font\* font)

**Description**

Destroys an **OH\_Drawing\_Font** object and reclaims the memory occupied by the object.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Font](../../structs/oh-drawing-font/document.md)\* font | Pointer to an **OH\_Drawing\_Font** object. |

#### \[h2\]OH\_Drawing\_FontGetMetrics()

float OH\_Drawing\_FontGetMetrics(OH\_Drawing\_Font\* font, OH\_Drawing\_Font\_Metrics\* fontMetrics)

**Description**

Obtains the measurement information about a font.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **font** or **fontMetrics** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Font](../../structs/oh-drawing-font/document.md)\* font | Pointer to the [OH\_Drawing\_Font](../../structs/oh-drawing-font/document.md) object. |
| [OH\_Drawing\_Font\_Metrics](../../structs/oh-drawing-font-metrics/document.md)\* fontMetrics | Pointer to the [OH\_Drawing\_Font\_Metrics](../../structs/oh-drawing-font-metrics/document.md) object. |

**Returns**

| Type | Description |
| :-- | :-- |
| float | Returns a floating-point variable that indicates the recommended interline spacing. |

#### \[h2\]OH\_Drawing\_FontGetBounds()

OH\_Drawing\_ErrorCode OH\_Drawing\_FontGetBounds(const OH\_Drawing\_Font\* font, const uint16\_t\* glyphs, uint32\_t count,OH\_Drawing\_Array\* bounds)

**Description**

Obtains the rectangular bounding box for each glyph in the glyph array.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| const [OH\_Drawing\_Font](../../structs/oh-drawing-font/document.md)\* font | Pointer to the [OH\_Drawing\_Font](../../structs/oh-drawing-font/document.md) object. |
| const uint16\_t\* glyphs | Pointer to a glyph array. |
| uint32\_t count | Length of the glyph array. |
| [OH\_Drawing\_Array](../../structs/oh-drawing-array/document.md)\* bounds | Pointer to a rectangular bounding box array. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_ErrorCode](../drawing-error-code-h/document.md#oh_drawing_errorcode) | 
Returns one of the following result codes:

**OH\_DRAWING\_SUCCESS** if the operation is successful.

**OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** if any of **font**, **glyphs**, or **bounds** is NULL or **count** is **0**.

 |

#### \[h2\]OH\_Drawing\_FontGetPathForGlyph()

OH\_Drawing\_ErrorCode OH\_Drawing\_FontGetPathForGlyph(const OH\_Drawing\_Font\* font, uint16\_t glyph,OH\_Drawing\_Path\* path)

**Description**

Obtains the path of a glyph.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| const [OH\_Drawing\_Font](../../structs/oh-drawing-font/document.md)\* font | Pointer to the [OH\_Drawing\_Font](../../structs/oh-drawing-font/document.md) object. |
| uint16\_t glyph | Glyph index. |
| [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md)\* path | Pointer to the [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md) object, which is used to store the glyph path. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_ErrorCode](../drawing-error-code-h/document.md#oh_drawing_errorcode) | 
Returns one of the following result codes:

**OH\_DRAWING\_SUCCESS** if the operation is successful.

**OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** if **font** or **path** is NULL or the specified glyph does not exist.

 |

#### \[h2\]OH\_Drawing\_FontGetTextPath()

OH\_Drawing\_ErrorCode OH\_Drawing\_FontGetTextPath(const OH\_Drawing\_Font\* font, const void\* text, size\_t byteLength,OH\_Drawing\_TextEncoding encoding, float x, float y, OH\_Drawing\_Path\* path)

**Description**

Obtains the text outline path.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| const [OH\_Drawing\_Font](../../structs/oh-drawing-font/document.md)\* font | Pointer to the [OH\_Drawing\_Font](../../structs/oh-drawing-font/document.md) object. |
| const void\* text | Pointer to the text string. |
| size\_t byteLength | Length of the text path. If the length is greater than the length of the text string, undefined behavior occurs. |
| [OH\_Drawing\_TextEncoding](../drawing-types-h/document.md#oh_drawing_textencoding) encoding | Text encoding format. UTF-8, UTF-16, UTF-32, and glyph indices are supported. For details about the format, see [OH\_Drawing\_TextEncoding](../drawing-types-h/document.md#oh_drawing_textencoding). |
| float x | X coordinate of the text in the drawing area, with the origin as the start point. |
| float y | Y coordinate of the text in the drawing area, with the origin as the start point. |
| [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md)\* path | Pointer to the text outline path. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_ErrorCode](../drawing-error-code-h/document.md#oh_drawing_errorcode) | 
Returns one of the following error codes:

Returns [OH\_DRAWING\_SUCCESS](../drawing-error-code-h/document.md#oh_drawing_errorcode) if the operation is successful.

Returns [OH\_DRAWING\_ERROR\_INVALID\_PARAMETER](../drawing-error-code-h/document.md#oh_drawing_errorcode) if any of **font**, **text**, or **path** is NULL.

 |

#### \[h2\]OH\_Drawing\_FontSetThemeFontFollowed()

OH\_Drawing\_ErrorCode OH\_Drawing\_FontSetThemeFontFollowed(OH\_Drawing\_Font\* font, bool followed)

**Description**

Sets whether to follow the theme font. When **followed** is set to **true**, the theme font is used if it is enabled by the system and no typeface is set.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Font](../../structs/oh-drawing-font/document.md)\* font | Pointer to the [OH\_Drawing\_Font](../../structs/oh-drawing-font/document.md) object. |
| bool followed | Whether to follow the theme font. The value **true** means to follow the theme font, and **false** means the opposite. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_ErrorCode](../drawing-error-code-h/document.md#oh_drawing_errorcode) | 
Returns one of the following result codes:

**OH\_DRAWING\_SUCCESS** if the operation is successful.

Returns **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** if **font** is NULL.

 |

#### \[h2\]OH\_Drawing\_FontIsThemeFontFollowed()

OH\_Drawing\_ErrorCode OH\_Drawing\_FontIsThemeFontFollowed(const OH\_Drawing\_Font\* font, bool\* followed)

**Description**

Checks whether the font follows the theme font. By default, the theme font is not followed.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| const [OH\_Drawing\_Font](../../structs/oh-drawing-font/document.md)\* font | Pointer to the [OH\_Drawing\_Font](../../structs/oh-drawing-font/document.md) object. |
| bool\* followed | Check result. The value **true** means that the theme font is followed, and **false** means the opposite. It is used as an output parameter. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_ErrorCode](../drawing-error-code-h/document.md#oh_drawing_errorcode) | 
Returns one of the following result codes:

**OH\_DRAWING\_SUCCESS** if the operation is successful.

Returns **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** if either **font** or **followed** is NULL.

 |
