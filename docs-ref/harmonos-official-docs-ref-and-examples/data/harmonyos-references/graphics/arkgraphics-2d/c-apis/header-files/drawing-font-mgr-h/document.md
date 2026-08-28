# drawing\_font\_mgr.h

#### Overview

This file declares the functions related to font management in the drawing module. The functions can be used to load fonts and match available fonts in the system.

**File to include**: <native\_drawing/drawing\_font\_mgr.h>

**Library**: libnative\_drawing.so

**Since**: 12

**Related module**: [Drawing](../../modules/drawing/document.md)

#### Summary

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_FontMgr\* OH\_Drawing\_FontMgrCreate(void)](#oh_drawing_fontmgrcreate) | Creates an **OH\_Drawing\_FontMgr** object, which can be used only to manage system fonts. |
| [void OH\_Drawing\_FontMgrDestroy(OH\_Drawing\_FontMgr\* drawingFontMgr)](#oh_drawing_fontmgrdestroy) | Destroys an **OH\_Drawing\_FontMgr** object and reclaims the memory occupied by the object. |
| [int OH\_Drawing\_FontMgrGetFamilyCount(OH\_Drawing\_FontMgr\* drawingFontMgr)](#oh_drawing_fontmgrgetfamilycount) | Obtains the number of font families. |
| [char\* OH\_Drawing\_FontMgrGetFamilyName(OH\_Drawing\_FontMgr\* drawingFontMgr, int index)](#oh_drawing_fontmgrgetfamilyname) | Obtains the font family name based on an index. |
| [void OH\_Drawing\_FontMgrDestroyFamilyName(char\* familyName)](#oh_drawing_fontmgrdestroyfamilyname) | Reclaims the memory occupied by a font family name. |
| [OH\_Drawing\_FontStyleSet\* OH\_Drawing\_FontMgrCreateFontStyleSet(OH\_Drawing\_FontMgr\* drawingFontMgr, int index)](#oh_drawing_fontmgrcreatefontstyleset) | Creates a font style set from an **OH\_Drawing\_FontMgr** object. |
| [void OH\_Drawing\_FontMgrDestroyFontStyleSet(OH\_Drawing\_FontStyleSet\* drawingFontStyleSet)](#oh_drawing_fontmgrdestroyfontstyleset) | Reclaims the memory occupied by a font style set. |
| [OH\_Drawing\_FontStyleSet\* OH\_Drawing\_FontMgrMatchFamily(OH\_Drawing\_FontMgr\* drawingFontMgr, const char\* familyName)](#oh_drawing_fontmgrmatchfamily) | Obtains a font style set based on a font family name. |
| [OH\_Drawing\_Typeface\* OH\_Drawing\_FontMgrMatchFamilyStyle(OH\_Drawing\_FontMgr\* drawingFontMgr,const char\* familyName, OH\_Drawing\_FontStyleStruct fontStyle)](#oh_drawing_fontmgrmatchfamilystyle) | Obtains a typeface based on the font style information and font family name. |
| [OH\_Drawing\_Typeface\* OH\_Drawing\_FontMgrMatchFamilyStyleCharacter(OH\_Drawing\_FontMgr\* drawingFontMgr,const char\* familyName, OH\_Drawing\_FontStyleStruct fontStyle,const char\* bcp47\[\], int bcp47Count, int32\_t character)](#oh_drawing_fontmgrmatchfamilystylecharacter) | Obtains a typeface for the specified character. A null pointer is returned only when no typeface corresponding to the input UTF-8 character is found in the **OH\_Drawing\_FontMgr** object. |
| [OH\_Drawing\_Typeface\* OH\_Drawing\_FontStyleSetCreateTypeface(OH\_Drawing\_FontStyleSet\* fontStyleSet, int index)](#oh_drawing_fontstylesetcreatetypeface) | Creates a typeface for the specified index. |
| [OH\_Drawing\_FontStyleStruct OH\_Drawing\_FontStyleSetGetStyle(OH\_Drawing\_FontStyleSet\* fontStyleSet, int32\_t index,char\*\* styleName)](#oh_drawing_fontstylesetgetstyle) | Obtains the font style. Call [OH\_Drawing\_FontStyleSetFreeStyleName](#oh_drawing_fontstylesetfreestylename) to release **styleName** when it is no longer needed, freeing up the allocated memory. |
| [void OH\_Drawing\_FontStyleSetFreeStyleName(char\*\* styleName)](#oh_drawing_fontstylesetfreestylename) | Frees the memory occupied by a font style. |
| [OH\_Drawing\_Typeface\* OH\_Drawing\_FontStyleSetMatchStyle(OH\_Drawing\_FontStyleSet\* fontStyleSet,OH\_Drawing\_FontStyleStruct fontStyleStruct)](#oh_drawing_fontstylesetmatchstyle) | Obtains the typeface closest to the font style. |
| [int OH\_Drawing\_FontStyleSetCount(OH\_Drawing\_FontStyleSet\* fontStyleSet)](#oh_drawing_fontstylesetcount) | Obtains the number of fonts in the font style set. |

#### Function Description

#### \[h2\]OH\_Drawing\_FontMgrCreate()

OH\_Drawing\_FontMgr\* OH\_Drawing\_FontMgrCreate(void)

**Description**

Creates an **OH\_Drawing\_FontMgr** object, which can be used only to manage system fonts.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Return value**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_FontMgr](../../structs/oh-drawing-fontmgr/document.md)\* | Pointer to the [OH\_Drawing\_FontMgr](../../structs/oh-drawing-fontmgr/document.md) object created. |

#### \[h2\]OH\_Drawing\_FontMgrDestroy()

void OH\_Drawing\_FontMgrDestroy(OH\_Drawing\_FontMgr\* drawingFontMgr)

**Description**

Destroys an **OH\_Drawing\_FontMgr** object and reclaims the memory occupied by the object.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_FontMgr](../../structs/oh-drawing-fontmgr/document.md)\* drawingFontMgr | Pointer to an [OH\_Drawing\_FontMgr](../../structs/oh-drawing-fontmgr/document.md) object, which is obtained from [OH\_Drawing\_FontMgrCreate](#oh_drawing_fontmgrcreate). |

#### \[h2\]OH\_Drawing\_FontMgrGetFamilyCount()

int OH\_Drawing\_FontMgrGetFamilyCount(OH\_Drawing\_FontMgr\* drawingFontMgr)

**Description**

Obtains the number of font families.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_FontMgr](../../structs/oh-drawing-fontmgr/document.md)\* drawingFontMgr | Pointer to an [OH\_Drawing\_FontMgr](../../structs/oh-drawing-fontmgr/document.md) object, which is obtained from [OH\_Drawing\_FontMgrCreate](#oh_drawing_fontmgrcreate). |

**Return value**

| Type | Description |
| :-- | :-- |
| int | Returns the number of font families. |

#### \[h2\]OH\_Drawing\_FontMgrGetFamilyName()

char\* OH\_Drawing\_FontMgrGetFamilyName(OH\_Drawing\_FontMgr\* drawingFontMgr, int index)

**Description**

Obtains the font family name based on an index.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_FontMgr](../../structs/oh-drawing-fontmgr/document.md)\* drawingFontMgr | Pointer to an [OH\_Drawing\_FontMgr](../../structs/oh-drawing-fontmgr/document.md) object, which is obtained from [OH\_Drawing\_FontMgrCreate](#oh_drawing_fontmgrcreate). |
| int index | Index of the font family name. |

**Return value**

| Type | Description |
| :-- | :-- |
| char\* | Returns the font family name. When the font family name is no longer required, call [OH\_Drawing\_FontMgrDestroyFamilyName](#oh_drawing_fontmgrdestroyfamilyname) to release the pointer to the object. |

#### \[h2\]OH\_Drawing\_FontMgrDestroyFamilyName()

void OH\_Drawing\_FontMgrDestroyFamilyName(char\* familyName)

**Description**

Reclaims the memory occupied by a font family name.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| char\* familyName | Pointer to a font family name. |

#### \[h2\]OH\_Drawing\_FontMgrCreateFontStyleSet()

OH\_Drawing\_FontStyleSet\* OH\_Drawing\_FontMgrCreateFontStyleSet(OH\_Drawing\_FontMgr\* drawingFontMgr, int index)

**Description**

Creates a font style set from an **OH\_Drawing\_FontMgr** object.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_FontMgr](../../structs/oh-drawing-fontmgr/document.md)\* drawingFontMgr | Pointer to an [OH\_Drawing\_FontMgr](../../structs/oh-drawing-fontmgr/document.md) object, which is obtained from [OH\_Drawing\_FontMgrCreate](#oh_drawing_fontmgrcreate). |
| int index | Index of the font style set. |

**Return value**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_FontStyleSet](../../structs/oh-drawing-fontstyleset/document.md)\* | Returns a pointer to the [OH\_Drawing\_FontStyleSet](../../structs/oh-drawing-fontstyleset/document.md) object created. |

#### \[h2\]OH\_Drawing\_FontMgrDestroyFontStyleSet()

void OH\_Drawing\_FontMgrDestroyFontStyleSet(OH\_Drawing\_FontStyleSet\* drawingFontStyleSet)

**Description**

Reclaims the memory occupied by a font style set.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_FontStyleSet](../../structs/oh-drawing-fontstyleset/document.md)\* drawingFontStyleSet | Pointer to an [OH\_Drawing\_FontStyleSet](../../structs/oh-drawing-fontstyleset/document.md) object. |

#### \[h2\]OH\_Drawing\_FontMgrMatchFamily()

OH\_Drawing\_FontStyleSet\* OH\_Drawing\_FontMgrMatchFamily(OH\_Drawing\_FontMgr\* drawingFontMgr, const char\* familyName)

**Description**

Obtains a font style set based on a font family name.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_FontMgr](../../structs/oh-drawing-fontmgr/document.md)\* drawingFontMgr | Pointer to an [OH\_Drawing\_FontMgr](../../structs/oh-drawing-fontmgr/document.md) object, which is obtained from [OH\_Drawing\_FontMgrCreate](#oh_drawing_fontmgrcreate). |
| const char\* familyName | Pointer to a font family name. |

**Return value**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_FontStyleSet](../../structs/oh-drawing-fontstyleset/document.md)\* | Returns a pointer to an [OH\_Drawing\_FontStyleSet](../../structs/oh-drawing-fontstyleset/document.md) object. Call [OH\_Drawing\_FontMgrDestroyFontStyleSet](#oh_drawing_fontmgrdestroyfontstyleset) to release this pointer when it is no longer needed. |

#### \[h2\]OH\_Drawing\_FontMgrMatchFamilyStyle()

OH\_Drawing\_Typeface\* OH\_Drawing\_FontMgrMatchFamilyStyle(OH\_Drawing\_FontMgr\* drawingFontMgr,const char\* familyName, OH\_Drawing\_FontStyleStruct fontStyle)

**Description**

Obtains a typeface based on the font style information and font family name.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_FontMgr](../../structs/oh-drawing-fontmgr/document.md)\* drawingFontMgr | Pointer to an [OH\_Drawing\_FontMgr](../../structs/oh-drawing-fontmgr/document.md) object, which is obtained from [OH\_Drawing\_FontMgrCreate](#oh_drawing_fontmgrcreate). |
| const char\* familyName | Pointer to a font family name. |
| [OH\_Drawing\_FontStyleStruct](../../structs/oh-drawing-fontstylestruct/document.md) fontStyle | Font style, including the font weight, width, and slant. |

**Return value**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_Typeface](../../structs/oh-drawing-typeface/document.md)\* | Returns a pointer to an [OH\_Drawing\_Typeface](../../structs/oh-drawing-typeface/document.md) object. Call [OH\_Drawing\_TypefaceDestroy](../drawing-typeface-h/document.md#oh_drawing_typefacedestroy) to release this pointer when it is no longer needed. |

#### \[h2\]OH\_Drawing\_FontMgrMatchFamilyStyleCharacter()

OH\_Drawing\_Typeface\* OH\_Drawing\_FontMgrMatchFamilyStyleCharacter(OH\_Drawing\_FontMgr\* drawingFontMgr,const char\* familyName, OH\_Drawing\_FontStyleStruct fontStyle,const char\* bcp47\[\], int bcp47Count, int32\_t character)

**Description**

Obtains a typeface for the specified character. A null pointer is returned only when no typeface corresponding to the input UTF-8 character is found in the **OH\_Drawing\_FontMgr** object.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_FontMgr](../../structs/oh-drawing-fontmgr/document.md)\* drawingFontMgr | Pointer to an [OH\_Drawing\_FontMgr](../../structs/oh-drawing-fontmgr/document.md) object, which is obtained from [OH\_Drawing\_FontMgrCreate](#oh_drawing_fontmgrcreate). |
| const char\* familyName | Pointer to a font family name. |
| [OH\_Drawing\_FontStyleStruct](../../structs/oh-drawing-fontstylestruct/document.md) fontStyle | Font style, including the font weight, width, and slant. |
| bcp47 | Pointer to the character language code array, which is a combination of ISO 639, 15924, and 3166-1 language codes. |
| int bcp47Count | Size of the character language code array. |
| int32\_t character | UTF8 character used for matching. |

**Return value**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_Typeface](../../structs/oh-drawing-typeface/document.md)\* | Returns a typeface object, which is [OH\_Drawing\_Typeface](../../structs/oh-drawing-typeface/document.md). |

#### \[h2\]OH\_Drawing\_FontStyleSetCreateTypeface()

OH\_Drawing\_Typeface\* OH\_Drawing\_FontStyleSetCreateTypeface(OH\_Drawing\_FontStyleSet\* fontStyleSet, int index)

**Description**

Creates a typeface for the specified index.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_FontStyleSet](../../structs/oh-drawing-fontstyleset/document.md)\* fontStyleSet | Pointer to an [OH\_Drawing\_FontStyleSet](../../structs/oh-drawing-fontstyleset/document.md) object. |
| int index | Index of the typeface. |

**Return value**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_Typeface](../../structs/oh-drawing-typeface/document.md)\* | Returns the pointer to the [OH\_Drawing\_Typeface](../../structs/oh-drawing-typeface/document.md) object created if the operation is successful; returns a null pointer otherwise. |

#### \[h2\]OH\_Drawing\_FontStyleSetGetStyle()

OH\_Drawing\_FontStyleStruct OH\_Drawing\_FontStyleSetGetStyle(OH\_Drawing\_FontStyleSet\* fontStyleSet, int32\_t index,char\*\* styleName)

**Description**

Obtains the font style. Call [OH\_Drawing\_FontStyleSetFreeStyleName](#oh_drawing_fontstylesetfreestylename) to release **styleName** when it is no longer needed, freeing up the allocated memory.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_FontStyleSet](../../structs/oh-drawing-fontstyleset/document.md)\* fontStyleSet | Pointer to an [OH\_Drawing\_FontStyleSet](../../structs/oh-drawing-fontstyleset/document.md) object. |
| int32\_t index | Index of the font style. |
| char\*\* styleName | String specifying the font style name. Call [OH\_Drawing\_FontStyleSetFreeStyleName](#oh_drawing_fontstylesetfreestylename) to release it when it is no longer needed, freeing up the allocated memory. |

**Return value**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_FontStyleStruct](../../structs/oh-drawing-fontstylestruct/document.md) | Returns the font style. |

#### \[h2\]OH\_Drawing\_FontStyleSetFreeStyleName()

void OH\_Drawing\_FontStyleSetFreeStyleName(char\*\* styleName)

**Description**

Frees the memory occupied by a font style.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| char\*\* styleName | Double pointer to the string that specifies the font style name. |

#### \[h2\]OH\_Drawing\_FontStyleSetMatchStyle()

OH\_Drawing\_Typeface\* OH\_Drawing\_FontStyleSetMatchStyle(OH\_Drawing\_FontStyleSet\* fontStyleSet,OH\_Drawing\_FontStyleStruct fontStyleStruct)

**Description**

Obtains the typeface closest to the font style.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_FontStyleSet](../../structs/oh-drawing-fontstyleset/document.md)\* fontStyleSet | Pointer to an [OH\_Drawing\_FontStyleSet](../../structs/oh-drawing-fontstyleset/document.md) object. |
| [OH\_Drawing\_FontStyleStruct](../../structs/oh-drawing-fontstylestruct/document.md) fontStyleStruct | Font style, including the font weight, width, and slant. |

**Return value**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_Typeface](../../structs/oh-drawing-typeface/document.md)\* | Returns a typeface object, which is [OH\_Drawing\_Typeface](../../structs/oh-drawing-typeface/document.md). |

#### \[h2\]OH\_Drawing\_FontStyleSetCount()

int OH\_Drawing\_FontStyleSetCount(OH\_Drawing\_FontStyleSet\* fontStyleSet)

**Description**

Obtains the number of fonts in the font style set.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_FontStyleSet](../../structs/oh-drawing-fontstyleset/document.md)\* fontStyleSet | Pointer to an [OH\_Drawing\_FontStyleSet](../../structs/oh-drawing-fontstyleset/document.md) object. |

**Return value**

| Type | Description |
| :-- | :-- |
| int | Returns the number of fonts. |
