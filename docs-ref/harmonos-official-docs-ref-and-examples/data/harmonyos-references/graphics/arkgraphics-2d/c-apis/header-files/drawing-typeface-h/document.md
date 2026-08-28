# drawing\_typeface.h

#### Overview

This file declares the functions related to the typeface in the drawing module.

Different platforms have their own default typefaces. You can also parse the .ttf file to obtain the typefaces specified by the third party, such as SimSun and SimHei.

**File to include**: <native\_drawing/drawing\_typeface.h>

**Library**: libnative\_drawing.so

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 11

**Related module**: [Drawing](../../modules/drawing/document.md)

#### Summary

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Typeface\* OH\_Drawing\_TypefaceCreateDefault(void)](#oh_drawing_typefacecreatedefault) | Creates a default **OH\_Drawing\_Typeface** object. |
| [OH\_Drawing\_Typeface\* OH\_Drawing\_TypefaceCreateFromFile(const char\* path, int index)](#oh_drawing_typefacecreatefromfile) | 
Creates an **OH\_Drawing\_Typeface** object through a file.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **path** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [OH\_Drawing\_Typeface\* OH\_Drawing\_TypefaceCreateFromFileWithArguments(const char\* path,const OH\_Drawing\_FontArguments\* fontArguments)](#oh_drawing_typefacecreatefromfilewitharguments) | 

Creates an **OH\_Drawing\_Typeface** object with font arguments through a file.

If the **OH\_Drawing\_Typeface** object does not support the variation described in the font arguments, this function creates an **OH\_Drawing\_Typeface** object with the default font arguments.

In this case, this function provides the same capability as [OH\_Drawing\_TypefaceCreateFromFile](#oh_drawing_typefacecreatefromfile).

 |
| [OH\_Drawing\_Typeface\* OH\_Drawing\_TypefaceCreateFromCurrent(const OH\_Drawing\_Typeface\* current,const OH\_Drawing\_FontArguments\* fontArguments)](#oh_drawing_typefacecreatefromcurrent) | Creates an **OH\_Drawing\_Typeface** object with font arguments based on an existing **OH\_Drawing\_Typeface** object. |
| [OH\_Drawing\_Typeface\* OH\_Drawing\_TypefaceCreateFromStream(OH\_Drawing\_MemoryStream\* memoryStream, int32\_t index)](#oh_drawing_typefacecreatefromstream) | 

Creates an **OH\_Drawing\_Typeface** object through a memory stream. If the memory stream is an invalid font file, a null pointer is returned. After the memory stream is passed in, the ownership is transferred and you cannot release it.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **memoryStream** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [void OH\_Drawing\_TypefaceDestroy(OH\_Drawing\_Typeface\* typeface)](#oh_drawing_typefacedestroy) | Destroys an **OH\_Drawing\_Typeface** object and reclaims the memory occupied by the object. |
| [OH\_Drawing\_FontArguments\* OH\_Drawing\_FontArgumentsCreate(void)](#oh_drawing_fontargumentscreate) | Creates an **OH\_Drawing\_FontArguments** object. The font arguments are used to create an **OH\_Drawing\_Typeface** object with custom attributes. |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_FontArgumentsAddVariation(OH\_Drawing\_FontArguments\* fontArguments,const char\* axis, float value)](#oh_drawing_fontargumentsaddvariation) | Adds a variation to an **OH\_Drawing\_FontArguments** object. |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_FontArgumentsDestroy(OH\_Drawing\_FontArguments\* fontArguments)](#oh_drawing_fontargumentsdestroy) | Destroys an **OH\_Drawing\_FontArguments** object. |

#### Function Description

#### \[h2\]OH\_Drawing\_TypefaceCreateDefault()

OH\_Drawing\_Typeface\* OH\_Drawing\_TypefaceCreateDefault(void)

**Description**

Creates a default **OH\_Drawing\_Typeface** object.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 11

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_Typeface](../../structs/oh-drawing-typeface/document.md)\* | Returns the pointer to the **OH\_Drawing\_Typeface** object created. |

#### \[h2\]OH\_Drawing\_TypefaceCreateFromFile()

OH\_Drawing\_Typeface\* OH\_Drawing\_TypefaceCreateFromFile(const char\* path, int index)

**Description**

Creates an **OH\_Drawing\_Typeface** object through a file.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **path** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const char\* path | Pointer to the file path. |
| int index | File index. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_Typeface](../../structs/oh-drawing-typeface/document.md)\* | Returns a pointer to the created [OH\_Drawing\_Typeface](../../structs/oh-drawing-typeface/document.md) object. |

#### \[h2\]OH\_Drawing\_TypefaceCreateFromFileWithArguments()

OH\_Drawing\_Typeface\* OH\_Drawing\_TypefaceCreateFromFileWithArguments(const char\* path,const OH\_Drawing\_FontArguments\* fontArguments)

**Description**

Creates an **OH\_Drawing\_Typeface** object with font arguments through a file.

If the **OH\_Drawing\_Typeface** object does not support the variation described in the font arguments, this function creates an **OH\_Drawing\_Typeface** object with the default font arguments.

In this case, this function provides the same capability as [OH\_Drawing\_TypefaceCreateFromFile](#oh_drawing_typefacecreatefromfile).

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| const char\* path | Pointer to the file path. |
| const [OH\_Drawing\_FontArguments](../../structs/oh-drawing-fontarguments/document.md)\* fontArguments | Pointer to an [OH\_Drawing\_FontArguments](../../structs/oh-drawing-fontarguments/document.md) object. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_Typeface](../../structs/oh-drawing-typeface/document.md)\* | 
Returns a pointer to the created [OH\_Drawing\_Typeface](../../structs/oh-drawing-typeface/document.md) object.

If a null pointer is returned, the creation fails. Possible causes are that no memory is available, the passed-in **path** or **fontArguments** is NULL, or the path is invalid.

 |

#### \[h2\]OH\_Drawing\_TypefaceCreateFromCurrent()

OH\_Drawing\_Typeface\* OH\_Drawing\_TypefaceCreateFromCurrent(const OH\_Drawing\_Typeface\* current,const OH\_Drawing\_FontArguments\* fontArguments)

**Description**

Creates an **OH\_Drawing\_Typeface** object with font arguments based on an existing **OH\_Drawing\_Typeface** object.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| const [OH\_Drawing\_Typeface](../../structs/oh-drawing-typeface/document.md)\* current | Pointer to the [OH\_Drawing\_Typeface](../../structs/oh-drawing-typeface/document.md) object. |
| const [OH\_Drawing\_FontArguments](../../structs/oh-drawing-fontarguments/document.md)\* fontArguments | Pointer to an [OH\_Drawing\_FontArguments](../../structs/oh-drawing-fontarguments/document.md) object. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_Typeface](../../structs/oh-drawing-typeface/document.md)\* | 
Returns a pointer to the created [OH\_Drawing\_Typeface](../../structs/oh-drawing-typeface/document.md) object.

If a null pointer is returned, the creation fails. Possible causes are that no memory is available, the passed-in **path** or **fontArguments** is NULL, or the existing **OH\_Drawing\_FontArguments** object does not support the variation described in the font arguments.

 |

#### \[h2\]OH\_Drawing\_TypefaceCreateFromStream()

OH\_Drawing\_Typeface\* OH\_Drawing\_TypefaceCreateFromStream(OH\_Drawing\_MemoryStream\* memoryStream, int32\_t index)

**Description**

Creates an **OH\_Drawing\_Typeface** object through a memory stream. If the memory stream is an invalid font file, a null pointer is returned. After the memory stream is passed in, the ownership is transferred and you cannot release it.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **memoryStream** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_MemoryStream](../../structs/oh-drawing-memorystream/document.md)\* memoryStream | Pointer to an [OH\_Drawing\_MemoryStream](../../structs/oh-drawing-memorystream/document.md) object. |
| int32\_t index | Index of the memory stream. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_Typeface](../../structs/oh-drawing-typeface/document.md)\* | Returns a pointer to the created [OH\_Drawing\_Typeface](../../structs/oh-drawing-typeface/document.md) object. |

#### \[h2\]OH\_Drawing\_TypefaceDestroy()

void OH\_Drawing\_TypefaceDestroy(OH\_Drawing\_Typeface\* typeface)

**Description**

Destroys an **OH\_Drawing\_Typeface** object and reclaims the memory occupied by the object.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Typeface](../../structs/oh-drawing-typeface/document.md)\* typeface | Pointer to an **OH\_Drawing\_Typeface** object. |

#### \[h2\]OH\_Drawing\_FontArgumentsCreate()

OH\_Drawing\_FontArguments\* OH\_Drawing\_FontArgumentsCreate(void)

**Description**

Creates an **OH\_Drawing\_FontArguments** object. The font arguments are used to create an **OH\_Drawing\_Typeface** object with custom attributes.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 13

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_FontArguments](../../structs/oh-drawing-fontarguments/document.md)\* | Returns the pointer to the **OH\_Drawing\_FontArguments** object created. |

#### \[h2\]OH\_Drawing\_FontArgumentsAddVariation()

OH\_Drawing\_ErrorCode OH\_Drawing\_FontArgumentsAddVariation(OH\_Drawing\_FontArguments\* fontArguments,const char\* axis, float value)

**Description**

Adds a variation to an **OH\_Drawing\_FontArguments** object.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_FontArguments](../../structs/oh-drawing-fontarguments/document.md)\* fontArguments | Pointer to an [OH\_Drawing\_FontArguments](../../structs/oh-drawing-fontarguments/document.md) object. |
| const char\* axis | Pointer to the label of the variation. The value must contain four ASCII characters. The supported labels depend on the loaded font file. For example, **'wght'** is the font weight label. |
| float value | Value of the variation label. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_ErrorCode](../drawing-error-code-h/document.md#oh_drawing_errorcode) | 
Returns one of the following result codes:

**OH\_DRAWING\_SUCCESS** if the operation is successful.

**OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** if either **fontArguments** or **axis** is NULL or the length of **axis** is not 4.

 |

#### \[h2\]OH\_Drawing\_FontArgumentsDestroy()

OH\_Drawing\_ErrorCode OH\_Drawing\_FontArgumentsDestroy(OH\_Drawing\_FontArguments\* fontArguments)

**Description**

Destroys an **OH\_Drawing\_FontArguments** object.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_FontArguments](../../structs/oh-drawing-fontarguments/document.md)\* fontArguments | Pointer to an [OH\_Drawing\_FontArguments](../../structs/oh-drawing-fontarguments/document.md) object. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_ErrorCode](../drawing-error-code-h/document.md#oh_drawing_errorcode) | 
Returns one of the following result codes:

**OH\_DRAWING\_SUCCESS** if the operation is successful.

**OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** if **fontArguments** is NULL.

 |
