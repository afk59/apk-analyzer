# drawing\_text\_font\_descriptor.h

#### Overview

This file declares the capabilities of font information, such as obtaining font information and searching for a font.

**File to include**: <native\_drawing/drawing\_text\_font\_descriptor.h>

**Library**: libnative\_drawing.so

**Since**: 14

**Related module**: [Drawing](../../modules/drawing/document.md)

#### Summary

#### \[h2\]Enumerated value

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_Drawing\_SystemFontType](#oh_drawing_systemfonttype) | OH\_Drawing\_SystemFontType | Defines an enum for the system font types. |
| [OH\_Drawing\_FontFullDescriptorAttributeId](#oh_drawing_fontfulldescriptorattributeid) | OH\_Drawing\_FontFullDescriptorAttributeId | Enumerates font descriptor attributes. You can use the corresponding APIs to obtain the attributes of different font descriptor types. For example, if the font descriptor attribute **FULL\_DESCRIPTOR\_ATTR\_I\_WEIGHT** is of the int type, use the [OH\_Drawing\_GetFontFullDescriptorAttributeInt](#oh_drawing_getfontfulldescriptorattributeint) API to obtain the attribute value. |

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_FontDescriptor\* OH\_Drawing\_MatchFontDescriptors(OH\_Drawing\_FontDescriptor\* desc, size\_t\* num)](#oh_drawing_matchfontdescriptors) | 
Obtains all system font descriptors that match a font descriptor. In the [OH\_Drawing\_FontDescriptor](../../structs/oh-drawing-fontdescriptor/document.md) struct, the **path** field is not used for matching, and other fields are valid only when they are not set to their default values.

If all fields in **desc** are set to their default values, all system font descriptors are returned.

If no matching is found, NULL is returned. Call [OH\_Drawing\_DestroyFontDescriptors](#oh_drawing_destroyfontdescriptors) to release this pointer when the object is no longer needed.

 |
| [void OH\_Drawing\_DestroyFontDescriptors(OH\_Drawing\_FontDescriptor\* descriptors, size\_t num)](#oh_drawing_destroyfontdescriptors) | Releases an array of [OH\_Drawing\_FontDescriptor](../../structs/oh-drawing-fontdescriptor/document.md) objects. |
| [OH\_Drawing\_FontDescriptor\* OH\_Drawing\_GetFontDescriptorByFullName(const OH\_Drawing\_String\* fullName,OH\_Drawing\_SystemFontType fontType)](#oh_drawing_getfontdescriptorbyfullname) | 

Obtains a font descriptor based on the font name and type. System fonts, style fonts, and user-installed fonts are supported.

A font descriptor is a data structure that describes font features. It contains details of the font appearance and properties.

 |
| [OH\_Drawing\_Array\* OH\_Drawing\_GetSystemFontFullNamesByType(OH\_Drawing\_SystemFontType fontType)](#oh_drawing_getsystemfontfullnamesbytype) | Obtains an array of font names by font type. |
| [const OH\_Drawing\_String\* OH\_Drawing\_GetSystemFontFullNameByIndex(OH\_Drawing\_Array\* fullNameArray, size\_t index)](#oh_drawing_getsystemfontfullnamebyindex) | Obtains the font name with the specified index in the font name array. |
| [void OH\_Drawing\_DestroySystemFontFullNames(OH\_Drawing\_Array\* fullNameArray)](#oh_drawing_destroysystemfontfullnames) | Releases the memory occupied by the font name array obtained by font type. |
| [OH\_Drawing\_Array\* OH\_Drawing\_GetFontFullDescriptorsFromStream(const void\* data, size\_t size)](#oh_drawing_getfontfulldescriptorsfromstream) | Obtains the font descriptor array based on the original binary data. |
| [OH\_Drawing\_Array\* OH\_Drawing\_GetFontFullDescriptorsFromPath(const char\* path)](#oh_drawing_getfontfulldescriptorsfrompath) | Obtains the font descriptor array based on the font file path. |
| [const OH\_Drawing\_FontFullDescriptor\* OH\_Drawing\_GetFontFullDescriptorByIndex(OH\_Drawing\_Array\* descriptorArray, size\_t index)](#oh_drawing_getfontfulldescriptorbyindex) | Obtains the font descriptor in the font descriptor array based on the index. |
| [void OH\_Drawing\_DestroyFontFullDescriptors(OH\_Drawing\_Array\* descriptorArray)](#oh_drawing_destroyfontfulldescriptors) | Releases the memory occupied by the font descriptor array. |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_GetFontFullDescriptorAttributeInt(const OH\_Drawing\_FontFullDescriptor\* descriptor, OH\_Drawing\_FontFullDescriptorAttributeId id, int\* value)](#oh_drawing_getfontfulldescriptorattributeint) | Obtains the attributes of the font descriptor of the int type. |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_GetFontFullDescriptorAttributeBool(const OH\_Drawing\_FontFullDescriptor\* descriptor, OH\_Drawing\_FontFullDescriptorAttributeId id, bool\* value)](#oh_drawing_getfontfulldescriptorattributebool) | Obtains the attributes of the font descriptor of the bool type. |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_GetFontFullDescriptorAttributeString(const OH\_Drawing\_FontFullDescriptor\* descriptor, OH\_Drawing\_FontFullDescriptorAttributeId id, OH\_Drawing\_String\* str)](#oh_drawing_getfontfulldescriptorattributestring) | Obtains the attributes of the font descriptor of the [OH\_Drawing\_String](../../structs/oh-drawing-string/document.md) type. |

#### Enum Description

#### \[h2\]OH\_Drawing\_SystemFontType

enum OH\_Drawing\_SystemFontType

**Description**

Defines an enum for the system font types.

**Since**: 14

| Value | Description |
| :-- | :-- |
| ALL = 1 << 0 | All font types. |
| GENERIC = 1 << 1 | System font type. |
| STYLISH = 1 << 2 | Style font type. |
| INSTALLED = 1 << 3 | User-installed font type. |
| CUSTOMIZED = 1 << 4 | 
Custom font type.

**Since**: 18

 |

#### \[h2\]OH\_Drawing\_FontFullDescriptorAttributeId

enum OH\_Drawing\_FontFullDescriptorAttributeId

**Description**

Enumerates font descriptor attributes. You can use the corresponding APIs to obtain the attributes of different font descriptor types. For example, if **FULL\_DESCRIPTOR\_ATTR\_I\_WEIGHT** is of the int type, you can use the [OH\_Drawing\_GetFontFullDescriptorAttributeInt](#oh_drawing_getfontfulldescriptorattributeint) API to obtain its attribute value.

**Since**: 22

| Value | Description |
| :-- | :-- |
| FULL\_DESCRIPTOR\_ATTR\_S\_PATH = 0 | Font file path, of the [OH\_Drawing\_String](../../structs/oh-drawing-string/document.md) type. |
| FULL\_DESCRIPTOR\_ATTR\_S\_POSTSCRIPT\_NAME = 1 | Unique font name, of the [OH\_Drawing\_String](../../structs/oh-drawing-string/document.md) type. |
| FULL\_DESCRIPTOR\_ATTR\_S\_FULL\_NAME = 2 | Font name, of the [OH\_Drawing\_String](../../structs/oh-drawing-string/document.md) type. |
| FULL\_DESCRIPTOR\_ATTR\_S\_FAMILY\_NAME = 3 | Font family name, of the [OH\_Drawing\_String](../../structs/oh-drawing-string/document.md) type. |
| FULL\_DESCRIPTOR\_ATTR\_S\_SUB\_FAMILY\_NAME = 4 | Name of the subfont family, of the [OH\_Drawing\_String](../../structs/oh-drawing-string/document.md) type. |
| FULL\_DESCRIPTOR\_ATTR\_I\_WEIGHT = 5 | Font weight, of the int type. |
| FULL\_DESCRIPTOR\_ATTR\_I\_WIDTH = 6 | Font width style, of the int type. |
| FULL\_DESCRIPTOR\_ATTR\_I\_ITALIC = 7 | Whether the font is italic, of the int type. **1** means that the font is italic; **0** otherwise. |
| FULL\_DESCRIPTOR\_ATTR\_B\_MONO = 8 | Whether the font is compact, of the bool type. **true** means yes; **false** otherwise. |
| FULL\_DESCRIPTOR\_ATTR\_B\_SYMBOLIC = 9 | Whether the font supports the symbol font, of the bool type. **true** means yes; **false** otherwise. |

#### Function Description

#### \[h2\]OH\_Drawing\_MatchFontDescriptors()

OH\_Drawing\_FontDescriptor\* OH\_Drawing\_MatchFontDescriptors(OH\_Drawing\_FontDescriptor\* desc, size\_t\* num)

**Description**

Obtains all system font descriptors that match a font descriptor. In the [OH\_Drawing\_FontDescriptor](../../structs/oh-drawing-fontdescriptor/document.md) struct, the **path** field is not used for matching, and other fields are valid only when they are not set to their default values.

If all fields in **desc** are set to their default values, all system font descriptors are returned.

If no matching is found, NULL is returned. Call [OH\_Drawing\_DestroyFontDescriptors](#oh_drawing_destroyfontdescriptors) to release this pointer when the object is no longer needed.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_FontDescriptor](../../structs/oh-drawing-fontdescriptor/document.md)\* desc | 
Pointer.

You are advised to use [OH\_Drawing\_CreateFontDescriptor](../drawing-text-typography-h/document.md#oh_drawing_createfontdescriptor) to obtain a valid [OH\_Drawing\_FontDescriptor](../../structs/oh-drawing-fontdescriptor/document.md) instance.

For an [OH\_Drawing\_FontDescriptor](../../structs/oh-drawing-fontdescriptor/document.md) instance created by yourself, ensure that the fields that are not used for matching are set to default values.

 |
| size\_t\* num | Pointer to the number of elements in the array. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_FontDescriptor](../../structs/oh-drawing-fontdescriptor/document.md)\* | An array of [OH\_Drawing\_FontDescriptor](../../structs/oh-drawing-fontdescriptor/document.md) objects. Use [OH\_Drawing\_DestroyFontDescriptors](#oh_drawing_destroyfontdescriptors) to release the array. |

#### \[h2\]OH\_Drawing\_DestroyFontDescriptors()

void OH\_Drawing\_DestroyFontDescriptors(OH\_Drawing\_FontDescriptor\* descriptors, size\_t num)

**Description**

Releases an array of [OH\_Drawing\_FontDescriptor](../../structs/oh-drawing-fontdescriptor/document.md) objects.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_FontDescriptor](../../structs/oh-drawing-fontdescriptor/document.md)\* descriptors | Array. |
| size\_t num | Number of members in an array of [OH\_Drawing\_FontDescriptor](../../structs/oh-drawing-fontdescriptor/document.md) objects. |

#### \[h2\]OH\_Drawing\_GetFontDescriptorByFullName()

OH\_Drawing\_FontDescriptor\* OH\_Drawing\_GetFontDescriptorByFullName(const OH\_Drawing\_String\* fullName,OH\_Drawing\_SystemFontType fontType)

**Description**

Obtains a font descriptor based on the font name and type. System fonts, style fonts, and user-installed fonts are supported.

A font descriptor is a data structure that describes font features. It contains details of the font appearance and properties.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 14

**Parameters**

| Name | Description |
| :-- | :-- |
| const [OH\_Drawing\_String](../../structs/oh-drawing-string/document.md)\* fullName | Pointer to the font name, which is [OH\_Drawing\_String](../../structs/oh-drawing-string/document.md). |
| [OH\_Drawing\_SystemFontType](#oh_drawing_systemfonttype) fontType | Enum for the system font types, which is [OH\_Drawing\_SystemFontType](#oh_drawing_systemfonttype). |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_FontDescriptor](../../structs/oh-drawing-fontdescriptor/document.md)\* | Pointer to an [OH\_Drawing\_FontDescriptor](../../structs/oh-drawing-fontdescriptor/document.md) object. Call [OH\_Drawing\_DestroyFontDescriptor](../drawing-text-typography-h/document.md#oh_drawing_destroyfontdescriptor) to release this pointer when the object is no longer needed. |

#### \[h2\]OH\_Drawing\_GetSystemFontFullNamesByType()

OH\_Drawing\_Array\* OH\_Drawing\_GetSystemFontFullNamesByType(OH\_Drawing\_SystemFontType fontType)

**Description**

Obtains an array of font names by font type.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 14

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_SystemFontType](#oh_drawing_systemfonttype) fontType | Enum for the system font types, which is [OH\_Drawing\_SystemFontType](#oh_drawing_systemfonttype). |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_Array](../../structs/oh-drawing-array/document.md)\* | Returns the pointer to the [OH\_Drawing\_Array](../../structs/oh-drawing-array/document.md) object of the corresponding font type. Call [OH\_Drawing\_DestroySystemFontFullNames](#oh_drawing_destroysystemfontfullnames) to release this pointer when the object is no longer needed. |

#### \[h2\]OH\_Drawing\_GetSystemFontFullNameByIndex()

const OH\_Drawing\_String\* OH\_Drawing\_GetSystemFontFullNameByIndex(OH\_Drawing\_Array\* fullNameArray, size\_t index)

**Description**

Obtains the font name with the specified index in the font name array.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 14

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Array](../../structs/oh-drawing-array/document.md)\* fullNameArray | Pointer to an [OH\_Drawing\_Array](../../structs/oh-drawing-array/document.md) object. |
| size\_t index | Index of the font in the array. |

**Returns**

| Type | Description |
| :-- | :-- |
| const [OH\_Drawing\_String](../../structs/oh-drawing-string/document.md)\* | Returns the pointer to the font name, which is an [OH\_Drawing\_String](../../structs/oh-drawing-string/document.md) object. |

#### \[h2\]OH\_Drawing\_DestroySystemFontFullNames()

void OH\_Drawing\_DestroySystemFontFullNames(OH\_Drawing\_Array\* fullNameArray)

**Description**

Releases the memory occupied by the font name array obtained by font type.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 14

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Array](../../structs/oh-drawing-array/document.md)\* fullNameArray | Pointer to an [OH\_Drawing\_Array](../../structs/oh-drawing-array/document.md) object. |

#### \[h2\]OH\_Drawing\_GetFontFullDescriptorsFromStream()

OH\_Drawing\_Array\* OH\_Drawing\_GetFontFullDescriptorsFromStream(const void\* data, size\_t size)

**Description**

Obtains the font descriptor array based on the original binary data.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| const void\* data | Pointer to the raw binary font data buffer. |
| size\_t size | Size of the font data buffer, in bytes. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_Array\*](../../structs/oh-drawing-array/document.md) | 
Returns the pointer to the [OH\_Drawing\_Array](../../structs/oh-drawing-array/document.md) array of the font descriptor corresponding to the font file. Call [OH\_Drawing\_DestroyFontFullDescriptors](#oh_drawing_destroyfontfulldescriptors) to release the pointer when the **OH\_Drawing\_Array** object is no longer needed.

Returns NULL if the operation fails due to an invalid data format or parsing error.

 |

#### \[h2\]OH\_Drawing\_GetFontFullDescriptorsFromPath()

OH\_Drawing\_Array\* OH\_Drawing\_GetFontFullDescriptorsFromPath(const char\* path)

**Description**

Obtains an array of font descriptors by font file path.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| const char\* path | Path of the font file to be queried. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_Array\*](../../structs/oh-drawing-array/document.md) | 
Returns the pointer to the [OH\_Drawing\_Array](../../structs/oh-drawing-array/document.md) array of the font descriptor corresponding to the font file. Call [OH\_Drawing\_DestroyFontFullDescriptors](#oh_drawing_destroyfontfulldescriptors) to release the pointer when the **OH\_Drawing\_Array** object is no longer needed.

Returns NULL if the font file is not found, the font file path is invalid, the font file does not have the required permission, or the file is not in the font format.

 |

#### \[h2\]OH\_Drawing\_GetFontFullDescriptorByIndex()

const OH\_Drawing\_FontFullDescriptor\* OH\_Drawing\_GetFontFullDescriptorByIndex(OH\_Drawing\_Array\* descriptorArray, size\_t index)

**Description**

Obtains the font descriptor from the font descriptor array based on the index.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Array](../../structs/oh-drawing-array/document.md)\* descriptorArray | Pointer to the font descriptor array [OH\_Drawing\_Array](../../structs/oh-drawing-array/document.md). |
| size\_t index | Index of the array, starting from 0. |

**Returns**

| Type | Description |
| :-- | :-- |
| const [OH\_Drawing\_FontFullDescriptor](../../structs/oh-drawing-fontfulldescriptor/document.md)\* | 
Returns a pointer to the font descriptor object {@link OH\_Drawing\_FontFullDescriptor} at the specified index.

Returns NULL if the index is out of range or the array is invalid.

 |

#### \[h2\]OH\_Drawing\_DestroyFontFullDescriptors()

void OH\_Drawing\_DestroyFontFullDescriptors(OH\_Drawing\_Array\* descriptorArray)

**Description**

Releases the memory occupied by the font descriptor array.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Array](../../structs/oh-drawing-array/document.md)\* descriptorArray | Pointer to the font descriptor array [OH\_Drawing\_Array](../../structs/oh-drawing-array/document.md). |

#### \[h2\]OH\_Drawing\_GetFontFullDescriptorAttributeInt()

OH\_Drawing\_ErrorCode OH\_Drawing\_GetFontFullDescriptorAttributeInt(const OH\_Drawing\_FontFullDescriptor\* descriptor, OH\_Drawing\_FontFullDescriptorAttributeId id, int\* value)

**Description**

Obtains the attributes of a font descriptor of the int type.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| const [OH\_Drawing\_FontFullDescriptor](../../structs/oh-drawing-fontfulldescriptor/document.md)\* descriptor | Pointer to the font descriptor object [OH\_Drawing\_FontFullDescriptor](../../structs/oh-drawing-fontfulldescriptor/document.md). |
| [OH\_Drawing\_FontFullDescriptorAttributeId](#oh_drawing_fontfulldescriptorattributeid) id | Font descriptor attribute ID. You can obtain the font descriptor attribute from [OH\_Drawing\_FontFullDescriptorAttributeId](#oh_drawing_fontfulldescriptorattributeid). |
| int\* value | Pointer to the attribute of the **int** type. It is used as an output parameter. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_ErrorCode](../drawing-error-code-h/document.md#oh_drawing_errorcode) | 
Returns the execution result.

**OH\_DRAWING\_SUCCESS** if the operation is successful.

**OH\_DRAWING\_ERROR\_INCORRECT\_PARAMETER** if the descriptor or value parameter is null.

**OH\_DRAWING\_ERROR\_ATTRIBUTE\_ID\_MISMATCH** if the input attribute ID does not match the called function.

 |

#### \[h2\]OH\_Drawing\_GetFontFullDescriptorAttributeBool()

OH\_Drawing\_ErrorCode OH\_Drawing\_GetFontFullDescriptorAttributeBool(const OH\_Drawing\_FontFullDescriptor\* descriptor, OH\_Drawing\_FontFullDescriptorAttributeId id, bool\* value)

**Description**

Obtains the font descriptor attribute of the bool type.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| const [OH\_Drawing\_FontFullDescriptor](../../structs/oh-drawing-fontfulldescriptor/document.md)\* descriptor | Pointer to the font descriptor object [OH\_Drawing\_FontFullDescriptor](../../structs/oh-drawing-fontfulldescriptor/document.md). |
| [OH\_Drawing\_FontFullDescriptorAttributeId](#oh_drawing_fontfulldescriptorattributeid) id | Font descriptor attribute ID. You can obtain the font descriptor attribute from [OH\_Drawing\_FontFullDescriptorAttributeId](#oh_drawing_fontfulldescriptorattributeid). |
| bool\* value | Pointer to the bool attribute It is used as an output parameter. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_ErrorCode](../drawing-error-code-h/document.md#oh_drawing_errorcode) | 
Returns the execution result.

**OH\_DRAWING\_SUCCESS** if the operation is successful.

**OH\_DRAWING\_ERROR\_INCORRECT\_PARAMETER** if the descriptor or value parameter is null.

**OH\_DRAWING\_ERROR\_ATTRIBUTE\_ID\_MISMATCH** if the input attribute ID does not match the called function.

 |

#### \[h2\]OH\_Drawing\_GetFontFullDescriptorAttributeString()

OH\_Drawing\_ErrorCode OH\_Drawing\_GetFontFullDescriptorAttributeString(const OH\_Drawing\_FontFullDescriptor\* descriptor, OH\_Drawing\_FontFullDescriptorAttributeId id, OH\_Drawing\_String\* str)

**Description**

Obtains the attributes of the [OH\_Drawing\_String](../../structs/oh-drawing-string/document.md) font descriptor.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/40irbvghRmWJ8JdmmjlagQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062451Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CD0A5B79BC00ADDAF2719DAFB10EA8C249323BB8C34155F949BCCBB130826C69)

If **OH\_Drawing\_String** is no longer needed, the caller needs to manually release the **strData** member in the **OH\_Drawing\_String** struct.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| const [OH\_Drawing\_FontFullDescriptor](../../structs/oh-drawing-fontfulldescriptor/document.md)\* descriptor | Pointer to the font descriptor object [OH\_Drawing\_FontFullDescriptor](../../structs/oh-drawing-fontfulldescriptor/document.md). |
| [OH\_Drawing\_FontFullDescriptorAttributeId](#oh_drawing_fontfulldescriptorattributeid) id | Font descriptor attribute ID. You can obtain the font descriptor attribute from [OH\_Drawing\_FontFullDescriptorAttributeId](#oh_drawing_fontfulldescriptorattributeid). |
| [OH\_Drawing\_String](../../structs/oh-drawing-string/document.md)\* str | Pointer to the **OH\_Drawing\_String** attribute. It is used as an output parameter. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_ErrorCode](../drawing-error-code-h/document.md#oh_drawing_errorcode) | 
Returns the execution result.

**OH\_DRAWING\_SUCCESS** if the operation is successful.

**OH\_DRAWING\_ERROR\_INCORRECT\_PARAMETER** if **descriptor** or **str** is a null pointer.

**OH\_DRAWING\_ERROR\_ATTRIBUTE\_ID\_MISMATCH** if the input attribute ID does not match the called function.

 |
