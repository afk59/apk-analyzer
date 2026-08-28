# drawing\_text\_blob.h

#### Overview

This file declares the functions related to the text blob in the drawing module.

**File to include**: <native\_drawing/drawing\_text\_blob.h>

**Library**: libnative\_drawing.so

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 11

**Related module**: [Drawing](../../modules/drawing/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_Drawing\_RunBuffer](../../structs/oh-drawing-runbuffer/document.md) | OH\_Drawing\_RunBuffer | Describes a run, which provides storage for glyphs and positions. |

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TextBlobBuilder\* OH\_Drawing\_TextBlobBuilderCreate(void)](#oh_drawing_textblobbuildercreate) | Creates an **OH\_Drawing\_TextBlobBuilder** object. |
| [OH\_Drawing\_TextBlob\* OH\_Drawing\_TextBlobCreateFromText(const void\* text, size\_t byteLength,const OH\_Drawing\_Font\* font, OH\_Drawing\_TextEncoding textEncoding)](#oh_drawing_textblobcreatefromtext) | 
Creates an **OH\_Drawing\_TextBlob** object from the text.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **text** or **font** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

If **textEncoding** is not set to one of the enumerated values, **OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE** is returned.

 |
| [OH\_Drawing\_TextBlob\* OH\_Drawing\_TextBlobCreateFromPosText(const void\* text, size\_t byteLength,OH\_Drawing\_Point2D\* point2D, const OH\_Drawing\_Font\* font, OH\_Drawing\_TextEncoding textEncoding)](#oh_drawing_textblobcreatefrompostext) | 

Creates an **OH\_Drawing\_TextBlob** object from the text. The coordinates of each character in the **OH\_Drawing\_TextBlob** object are determined by the coordinate information in the **OH\_Drawing\_Point2D** array.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If any of **text**, **point2D**, and **font** is NULL or **byteLength** is **0**, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

If **textEncoding** is not set to one of the enumerated values, **OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE** is returned.

 |
| [OH\_Drawing\_TextBlob\* OH\_Drawing\_TextBlobCreateFromString(const char\* str,const OH\_Drawing\_Font\* font, OH\_Drawing\_TextEncoding textEncoding)](#oh_drawing_textblobcreatefromstring) | 

Creates an **OH\_Drawing\_TextBlob** object from a string.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **str** or **font** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

If **textEncoding** is not set to one of the enumerated values, **OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE** is returned.

 |
| [void OH\_Drawing\_TextBlobGetBounds(OH\_Drawing\_TextBlob\* textBlob, OH\_Drawing\_Rect\* rect)](#oh_drawing_textblobgetbounds) | 

Obtains the bounds of an **OH\_Drawing\_TextBlob** object.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **textBlob** or **rect** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [uint32\_t OH\_Drawing\_TextBlobUniqueID(const OH\_Drawing\_TextBlob\* textBlob)](#oh_drawing_textblobuniqueid) | 

Obtains the unique identifier of a text blob. The identifier is a non-zero value.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **textBlob** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [const OH\_Drawing\_RunBuffer\* OH\_Drawing\_TextBlobBuilderAllocRunPos(OH\_Drawing\_TextBlobBuilder\* textBlobBuilder,const OH\_Drawing\_Font\* font, int32\_t count, const OH\_Drawing\_Rect\* rect)](#oh_drawing_textblobbuilderallocrunpos) | 

Allocates a run to store glyphs and positions. The pointer returned does not need to be managed by the caller. It can no longer be used after [OH\_Drawing\_TextBlobBuilderMake](#oh_drawing_textblobbuildermake) is called.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **textBlobBuilder** or **font** is NULL or **count** is less than or equal to 0, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [OH\_Drawing\_TextBlob\* OH\_Drawing\_TextBlobBuilderMake(OH\_Drawing\_TextBlobBuilder\* textBlobBuilder)](#oh_drawing_textblobbuildermake) | 

Makes an **OH\_Drawing\_TextBlob** object from an **OH\_Drawing\_TextBlobBuilder**.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **textBlobBuilder** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [void OH\_Drawing\_TextBlobDestroy(OH\_Drawing\_TextBlob\* textBlob)](#oh_drawing_textblobdestroy) | Destroys an **OH\_Drawing\_TextBlob** object and reclaims the memory occupied by the object. |
| [void OH\_Drawing\_TextBlobBuilderDestroy(OH\_Drawing\_TextBlobBuilder\* textBlobBuilder)](#oh_drawing_textblobbuilderdestroy) | Destroys an **OH\_Drawing\_TextBlobBuilder** object and reclaims the memory occupied by the object. |

#### Function Description

#### \[h2\]OH\_Drawing\_TextBlobBuilderCreate()

OH\_Drawing\_TextBlobBuilder\* OH\_Drawing\_TextBlobBuilderCreate(void)

**Description**

Creates an **OH\_Drawing\_TextBlobBuilder** object.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 11

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_TextBlobBuilder](../../structs/oh-drawing-textblobbuilder/document.md)\* | Returns the pointer to the **OH\_Drawing\_TextBlobBuilder** object created. |

#### \[h2\]OH\_Drawing\_TextBlobCreateFromText()

OH\_Drawing\_TextBlob\* OH\_Drawing\_TextBlobCreateFromText(const void\* text, size\_t byteLength,const OH\_Drawing\_Font\* font, OH\_Drawing\_TextEncoding textEncoding)

**Description**

Creates an **OH\_Drawing\_TextBlob** object from the text.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **text** or **font** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

If **textEncoding** is not set to one of the enumerated values, **OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const void\* text | Pointer to the text. |
| size\_t byteLength | Length of the text, in bytes. |
| const [OH\_Drawing\_Font](../../structs/oh-drawing-font/document.md)\* font | Pointer to the [OH\_Drawing\_Font](../../structs/oh-drawing-font/document.md) object. |
| [OH\_Drawing\_TextEncoding](../drawing-types-h/document.md#oh_drawing_textencoding) textEncoding | Text encoding type [OH\_Drawing\_TextEncoding](../drawing-types-h/document.md#oh_drawing_textencoding). |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_TextBlob](../../structs/oh-drawing-textblob/document.md)\* | Returns a pointer to the created [OH\_Drawing\_TextBlob](../../structs/oh-drawing-textblob/document.md) object. |

#### \[h2\]OH\_Drawing\_TextBlobCreateFromPosText()

OH\_Drawing\_TextBlob\* OH\_Drawing\_TextBlobCreateFromPosText(const void\* text, size\_t byteLength,OH\_Drawing\_Point2D\* point2D, const OH\_Drawing\_Font\* font, OH\_Drawing\_TextEncoding textEncoding)

**Description**

Creates an **OH\_Drawing\_TextBlob** object from the text. The coordinates of each character in the **OH\_Drawing\_TextBlob** object are determined by the coordinate information in the **OH\_Drawing\_Point2D** array.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If any of **text**, **point2D**, and **font** is NULL or **byteLength** is **0**, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

If **textEncoding** is not set to one of the enumerated values, **OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const void\* text | Pointer to the text. |
| size\_t byteLength | Length of the text, in bytes. |
| [OH\_Drawing\_Point2D](../../structs/oh-drawing-point2d/document.md)\* point2D | Pointer to the start address of the [OH\_Drawing\_Point2D](../../structs/oh-drawing-point2d/document.md) array. The number of entries in the array is determined by [OH\_Drawing\_FontCountText](../drawing-font-h/document.md#oh_drawing_fontcounttext). |
| const [OH\_Drawing\_Font](../../structs/oh-drawing-font/document.md)\* font | Pointer to the [OH\_Drawing\_Font](../../structs/oh-drawing-font/document.md) object. |
| [OH\_Drawing\_TextEncoding](../drawing-types-h/document.md#oh_drawing_textencoding) textEncoding | Text encoding type [OH\_Drawing\_TextEncoding](../drawing-types-h/document.md#oh_drawing_textencoding). |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_TextBlob](../../structs/oh-drawing-textblob/document.md)\* | Returns a pointer to the created [OH\_Drawing\_TextBlob](../../structs/oh-drawing-textblob/document.md) object. |

#### \[h2\]OH\_Drawing\_TextBlobCreateFromString()

OH\_Drawing\_TextBlob\* OH\_Drawing\_TextBlobCreateFromString(const char\* str,const OH\_Drawing\_Font\* font, OH\_Drawing\_TextEncoding textEncoding)

**Description**

Creates an **OH\_Drawing\_TextBlob** object from a string.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **str** or **font** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

If **textEncoding** is not set to one of the enumerated values, **OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const char\* str | Pointer to a string. |
| const [OH\_Drawing\_Font](../../structs/oh-drawing-font/document.md)\* font | Pointer to the [OH\_Drawing\_Font](../../structs/oh-drawing-font/document.md) object. |
| [OH\_Drawing\_TextEncoding](../drawing-types-h/document.md#oh_drawing_textencoding) textEncoding | Text encoding type [OH\_Drawing\_TextEncoding](../drawing-types-h/document.md#oh_drawing_textencoding). |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_TextBlob](../../structs/oh-drawing-textblob/document.md)\* | Returns a pointer to the created [OH\_Drawing\_TextBlob](../../structs/oh-drawing-textblob/document.md) object. |

#### \[h2\]OH\_Drawing\_TextBlobGetBounds()

void OH\_Drawing\_TextBlobGetBounds(OH\_Drawing\_TextBlob\* textBlob, OH\_Drawing\_Rect\* rect)

**Description**

Obtains the bounds of an **OH\_Drawing\_TextBlob** object.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **textBlob** or **rect** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TextBlob](../../structs/oh-drawing-textblob/document.md)\* textBlob | Pointer to the [OH\_Drawing\_TextBlob](../../structs/oh-drawing-textblob/document.md) object. |
| [OH\_Drawing\_Rect](../../structs/oh-drawing-rect/document.md)\* rect | Pointer to the [OH\_Drawing\_Rect](../../structs/oh-drawing-rect/document.md) object. You can call [OH\_Drawing\_Rect](../../structs/oh-drawing-rect/document.md) to create a rectangle object. |

#### \[h2\]OH\_Drawing\_TextBlobUniqueID()

uint32\_t OH\_Drawing\_TextBlobUniqueID(const OH\_Drawing\_TextBlob\* textBlob)

**Description**

Obtains the unique identifier of a text blob. The identifier is a non-zero value.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **textBlob** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [OH\_Drawing\_TextBlob](../../structs/oh-drawing-textblob/document.md)\* textBlob | Pointer to the [OH\_Drawing\_TextBlob](../../structs/oh-drawing-textblob/document.md) object. |

**Returns**

| Type | Description |
| :-- | :-- |
| uint32\_t | Returns the unique identifier of the text blob. |

#### \[h2\]OH\_Drawing\_TextBlobBuilderAllocRunPos()

const OH\_Drawing\_RunBuffer\* OH\_Drawing\_TextBlobBuilderAllocRunPos(OH\_Drawing\_TextBlobBuilder\* textBlobBuilder,const OH\_Drawing\_Font\* font, int32\_t count, const OH\_Drawing\_Rect\* rect)

**Description**

Allocates a run to store glyphs and positions. The pointer returned does not need to be managed by the caller. It can no longer be used after [OH\_Drawing\_TextBlobBuilderMake](#oh_drawing_textblobbuildermake) is called.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **textBlobBuilder** or **font** is NULL or **count** is less than or equal to 0, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TextBlobBuilder](../../structs/oh-drawing-textblobbuilder/document.md)\* textBlobBuilder | Pointer to an **OH\_Drawing\_TextBlobBuilder** object. |
| const [OH\_Drawing\_Font](../../structs/oh-drawing-font/document.md)\* font | Pointer to an **OH\_Drawing\_Font** object. |
| int32\_t count | Number of text blobs. |
| const [OH\_Drawing\_Rect](../../structs/oh-drawing-rect/document.md)\* rect | Rectangle of the text blob. The value NULL means that no rectangle is set. |

#### \[h2\]OH\_Drawing\_TextBlobBuilderMake()

OH\_Drawing\_TextBlob\* OH\_Drawing\_TextBlobBuilderMake(OH\_Drawing\_TextBlobBuilder\* textBlobBuilder)

**Description**

Makes an **OH\_Drawing\_TextBlob** object from an **OH\_Drawing\_TextBlobBuilder**.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **textBlobBuilder** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TextBlobBuilder](../../structs/oh-drawing-textblobbuilder/document.md)\* textBlobBuilder | Pointer to an **OH\_Drawing\_TextBlobBuilder** object. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_TextBlob](../../structs/oh-drawing-textblob/document.md)\* | Returns the pointer to the **OH\_Drawing\_TextBlob** object created. |

#### \[h2\]OH\_Drawing\_TextBlobDestroy()

void OH\_Drawing\_TextBlobDestroy(OH\_Drawing\_TextBlob\* textBlob)

**Description**

Destroys an **OH\_Drawing\_TextBlob** object and reclaims the memory occupied by the object.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TextBlob](../../structs/oh-drawing-textblob/document.md)\* textBlob | Pointer to an **OH\_Drawing\_TextBlob** object. |

#### \[h2\]OH\_Drawing\_TextBlobBuilderDestroy()

void OH\_Drawing\_TextBlobBuilderDestroy(OH\_Drawing\_TextBlobBuilder\* textBlobBuilder)

**Description**

Destroys an **OH\_Drawing\_TextBlobBuilder** object and reclaims the memory occupied by the object.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TextBlobBuilder](../../structs/oh-drawing-textblobbuilder/document.md)\* textBlobBuilder | Pointer to an **OH\_Drawing\_TextBlobBuilder** object. |
