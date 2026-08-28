# styled\_string.h

#### Overview

Defines the text style and layout manager for the component whose [type](../native-node-h/document.md#arkui_nodetype) is set to **ARKUI\_NODE\_TEXT** on the native side.

**File to include**: <arkui/styled\_string.h>

**Library**: libace\_ndk.z.so

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Since**: 12

**Related module**: [ArkUI\_NativeModule](../../modules/arkui-nativemodule/document.md)

**Sample**: [StyledStringSample](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/ArkUISample/StyledStringSample)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [ArkUI\_StyledString](../../structs/arkui-styledstring/document.md) | ArkUI\_StyledString | Defines a styled string object supported by the text component. |
| [ArkUI\_TextLayoutManager](../../structs/arkui-textlayoutmanager/document.md) | ArkUI\_TextLayoutManager | Defines a text layout manager. |

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [ArkUI\_StyledString\* OH\_ArkUI\_StyledString\_Create(OH\_Drawing\_TypographyStyle\* style, OH\_Drawing\_FontCollection\* collection)](#oh_arkui_styledstring_create) | Creates a pointer to the **ArkUI\_StyledString** object. |
| [void OH\_ArkUI\_StyledString\_Destroy(ArkUI\_StyledString\* handle)](#oh_arkui_styledstring_destroy) | Destroys an **ArkUI\_StyledString** object and reclaims the memory occupied by the object. |
| [void OH\_ArkUI\_StyledString\_PushTextStyle(ArkUI\_StyledString\* handle, OH\_Drawing\_TextStyle\* style)](#oh_arkui_styledstring_pushtextstyle) | Pushes a text style to the top of the style stack of a styled string. |
| [void OH\_ArkUI\_StyledString\_AddText(ArkUI\_StyledString\* handle, const char\* content)](#oh_arkui_styledstring_addtext) | Adds text for a styled string. |
| [void OH\_ArkUI\_StyledString\_PopTextStyle(ArkUI\_StyledString\* handle)](#oh_arkui_styledstring_poptextstyle) | Pops the style at the top of the style stack of a styled string. |
| [OH\_Drawing\_Typography\* OH\_ArkUI\_StyledString\_CreateTypography(ArkUI\_StyledString\* handle)](#oh_arkui_styledstring_createtypography) | Creates a pointer to the [OH\_Drawing\_Typography](../../../../../graphics/arkgraphics-2d/c-apis/structs/oh-drawing-typography/document.md) object based on an **ArkUI\_StyledString** object for text measurement and typesetting in advance. |
| [void OH\_ArkUI\_StyledString\_AddPlaceholder(ArkUI\_StyledString\* handle, OH\_Drawing\_PlaceholderSpan\* placeholder)](#oh_arkui_styledstring_addplaceholder) | Adds a placeholder. |
| [ArkUI\_StyledString\_Descriptor\* OH\_ArkUI\_StyledString\_Descriptor\_Create(void)](#oh_arkui_styledstring_descriptor_create) | Creates an **ArkUI\_StyledString\_Descriptor** object. |
| [void OH\_ArkUI\_StyledString\_Descriptor\_Destroy(ArkUI\_StyledString\_Descriptor\* descriptor)](#oh_arkui_styledstring_descriptor_destroy) | Releases the memory occupied by the [ArkUI\_StyledString\_Descriptor](../../structs/arkui-styledstring-descriptor/document.md) object. |
| [int32\_t OH\_ArkUI\_UnmarshallStyledStringDescriptor(uint8\_t\* buffer, size\_t bufferSize, ArkUI\_StyledString\_Descriptor\* descriptor)](#oh_arkui_unmarshallstyledstringdescriptor) | Unmarshals a byte array containing styled string information into a styled string. |
| [int32\_t OH\_ArkUI\_MarshallStyledStringDescriptor(uint8\_t\* buffer, size\_t bufferSize, ArkUI\_StyledString\_Descriptor\* descriptor, size\_t\* resultSize)](#oh_arkui_marshallstyledstringdescriptor) | Marshals the styled string information into a byte array. |
| [const char\* OH\_ArkUI\_ConvertToHtml(ArkUI\_StyledString\_Descriptor\* descriptor)](#oh_arkui_converttohtml) | Converts styled string information into HTML. |
| [void OH\_ArkUI\_TextLayoutManager\_Dispose(ArkUI\_TextLayoutManager\* layoutManager)](#oh_arkui_textlayoutmanager_dispose) | Releases the memory occupied by the text layout manager. |
| [ArkUI\_ErrorCode OH\_ArkUI\_TextLayoutManager\_GetLineCount(ArkUI\_TextLayoutManager\* layoutManager, int32\_t\* outLineCount)](#oh_arkui_textlayoutmanager_getlinecount) | Obtains the number of lines. |
| [ArkUI\_ErrorCode OH\_ArkUI\_TextLayoutManager\_GetRectsForRange(ArkUI\_TextLayoutManager\* layoutManager, int32\_t start, int32\_t end, OH\_Drawing\_RectWidthStyle widthStyle, OH\_Drawing\_RectHeightStyle heightStyle, OH\_Drawing\_TextBox\*\* outTextBoxes)](#oh_arkui_textlayoutmanager_getrectsforrange) | Obtains the drawing area information of characters or placeholders within a specified text range under the given rectangle width and height. |
| [ArkUI\_ErrorCode OH\_ArkUI\_TextLayoutManager\_GetGlyphPositionAtCoordinate(ArkUI\_TextLayoutManager\* layoutManager, double dx, double dy, OH\_Drawing\_PositionAndAffinity\*\* outPos)](#oh_arkui_textlayoutmanager_getglyphpositionatcoordinate) | Obtains the position of the glyph closest to the given coordinates. |
| [ArkUI\_ErrorCode OH\_ArkUI\_TextLayoutManager\_GetLineMetrics(ArkUI\_TextLayoutManager\* layoutManager, int32\_t lineNumber, OH\_Drawing\_LineMetrics\* outMetrics)](#oh_arkui_textlayoutmanager_getlinemetrics) | Obtains the information about the specified line, including line metrics, text style information, and font properties. |

#### Function Description

#### \[h2\]OH\_ArkUI\_StyledString\_Create()

ArkUI\_StyledString\* OH\_ArkUI\_StyledString\_Create(OH\_Drawing\_TypographyStyle\* style, OH\_Drawing\_FontCollection\* collection)

**Description**

Creates a pointer to the **ArkUI\_StyledString** object.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TypographyStyle](../../../../../graphics/arkgraphics-2d/c-apis/structs/oh-drawing-typographystyle/document.md)\* style | Pointer to an **OH\_Drawing\_TypographyStyle** object, obtained using [OH\_Drawing\_CreateTypographyStyle](../../../../../graphics/arkgraphics-2d/c-apis/header-files/drawing-text-typography-h/document.md#oh_drawing_createtypographystyle). |
| [OH\_Drawing\_FontCollection](../../../../../graphics/arkgraphics-2d/c-apis/structs/oh-drawing-fontcollection/document.md)\* collection | Pointer to an **OH\_Drawing\_FontCollection** object, obtained using [OH\_Drawing\_CreateFontCollection](../../../../../graphics/arkgraphics-2d/c-apis/header-files/drawing-font-collection-h/document.md#oh_drawing_createfontcollection). |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_StyledString](../../structs/arkui-styledstring/document.md)\* | Pointer to the newly created **ArkUI\_StyledString** object. If a null pointer is returned, the creation fails. Possible causes include a full application address space or parameter errors, such as a null pointer being passed for the **style** or **collection** parameter. |

#### \[h2\]OH\_ArkUI\_StyledString\_Destroy()

void OH\_ArkUI\_StyledString\_Destroy(ArkUI\_StyledString\* handle)

**Description**

Destroys an **ArkUI\_StyledString** object and reclaims the memory occupied by the object.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_StyledString](../../structs/arkui-styledstring/document.md)\* handle | Pointer to an **ArkUI\_StyledString** object. |

#### \[h2\]OH\_ArkUI\_StyledString\_PushTextStyle()

void OH\_ArkUI\_StyledString\_PushTextStyle(ArkUI\_StyledString\* handle, OH\_Drawing\_TextStyle\* style)

**Description**

Pushes a text style to the top of the style stack of a styled string.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_StyledString](../../structs/arkui-styledstring/document.md)\* handle | Pointer to an **ArkUI\_StyledString** object. |
| [OH\_Drawing\_TextStyle](../../../../../graphics/arkgraphics-2d/c-apis/structs/oh-drawing-textstyle/document.md)\* style | Pointer to an **OH\_Drawing\_TextStyle** object. |

#### \[h2\]OH\_ArkUI\_StyledString\_AddText()

void OH\_ArkUI\_StyledString\_AddText(ArkUI\_StyledString\* handle, const char\* content)

**Description**

Adds text for a styled string.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_StyledString](../../structs/arkui-styledstring/document.md)\* handle | Pointer to an **ArkUI\_StyledString** object. |
| const char\* content | Pointer to the text content. |

#### \[h2\]OH\_ArkUI\_StyledString\_PopTextStyle()

void OH\_ArkUI\_StyledString\_PopTextStyle(ArkUI\_StyledString\* handle)

**Description**

Pops the style at the top of the style stack of a styled string.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_StyledString](../../structs/arkui-styledstring/document.md)\* handle | Pointer to an **ArkUI\_StyledString** object. |

#### \[h2\]OH\_ArkUI\_StyledString\_CreateTypography()

OH\_Drawing\_Typography\* OH\_ArkUI\_StyledString\_CreateTypography(ArkUI\_StyledString\* handle)

**Description**

Creates an **OH\_Drawing\_Typography** object based on an **ArkUI\_StyledString** object.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_StyledString](../../structs/arkui-styledstring/document.md)\* handle | Pointer to an **ArkUI\_StyledString** object. |

**Return value**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_Typography](../../../../../graphics/arkgraphics-2d/c-apis/structs/oh-drawing-typography/document.md)\* | Pointer to the **OH\_Drawing\_Typography** object. If a null pointer is returned, the creation fails. A possible cause is that a parameter error, for example, a null pointer for the **handle** parameter, occurs. |

#### \[h2\]OH\_ArkUI\_StyledString\_AddPlaceholder()

void OH\_ArkUI\_StyledString\_AddPlaceholder(ArkUI\_StyledString\* handle, OH\_Drawing\_PlaceholderSpan\* placeholder)

**Description**

Adds a placeholder.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_StyledString](../../structs/arkui-styledstring/document.md)\* handle | Pointer to an **ArkUI\_StyledString** object. |
| [OH\_Drawing\_PlaceholderSpan](../../../../../graphics/arkgraphics-2d/c-apis/structs/oh-drawing-placeholderspan/document.md)\* placeholder | Pointer to an **OH\_Drawing\_PlaceholderSpan** object. |

#### \[h2\]OH\_ArkUI\_StyledString\_Descriptor\_Create()

ArkUI\_StyledString\_Descriptor\* OH\_ArkUI\_StyledString\_Descriptor\_Create(void)

**Description**

Creates an **ArkUI\_StyledString\_Descriptor** object.

**Since**: 14

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_StyledString\_Descriptor](../../structs/arkui-styledstring-descriptor/document.md)\* | Pointer to an **ArkUI\_StyledString\_Descriptor** object. |

#### \[h2\]OH\_ArkUI\_StyledString\_Descriptor\_Destroy()

void OH\_ArkUI\_StyledString\_Descriptor\_Destroy(ArkUI\_StyledString\_Descriptor\* descriptor)

**Description**

Destroys an **ArkUI\_StyledString\_Descriptor** object and reclaims the memory occupied by the object.

**Since**: 14

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_StyledString\_Descriptor](../../structs/arkui-styledstring-descriptor/document.md)\* descriptor | Pointer to an **ArkUI\_StyledString\_Descriptor** object. |

#### \[h2\]OH\_ArkUI\_UnmarshallStyledStringDescriptor()

int32\_t OH\_ArkUI\_UnmarshallStyledStringDescriptor(uint8\_t\* buffer, size\_t bufferSize, ArkUI\_StyledString\_Descriptor\* descriptor)

**Description**

Unmarshals a byte array containing styled string information into a styled string.

**Since**: 14

**Parameters**

| Name | Description |
| :-- | :-- |
| uint8\_t\* buffer | Pointer to the byte array to be deserialized. |
| size\_t bufferSize | Length of the byte array. |
| [ArkUI\_StyledString\_Descriptor](../../structs/arkui-styledstring-descriptor/document.md)\* descriptor | Pointer to an **ArkUI\_StyledString\_Descriptor** object. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_MarshallStyledStringDescriptor()

int32\_t OH\_ArkUI\_MarshallStyledStringDescriptor(uint8\_t\* buffer, size\_t bufferSize, ArkUI\_StyledString\_Descriptor\* descriptor, size\_t\* resultSize)

**Description**

Marshals the styled string information into a byte array.

**Since**: 14

**Parameters**

| Name | Description |
| :-- | :-- |
| uint8\_t\* buffer | Pointer to the byte array where the serialized data will be stored. |
| size\_t bufferSize | Length of the byte array. |
| [ArkUI\_StyledString\_Descriptor](../../structs/arkui-styledstring-descriptor/document.md)\* descriptor | Pointer to an **ArkUI\_StyledString\_Descriptor** object. |
| size\_t\* resultSize | Pointer to the actual length of the resulting byte array after deserialization. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_INVALID\_STYLED\_STRING](../native-type-h/document.md#arkui_errorcode) if the styled string is invalid.

 |

#### \[h2\]OH\_ArkUI\_ConvertToHtml()

const char\* OH\_ArkUI\_ConvertToHtml(ArkUI\_StyledString\_Descriptor\* descriptor)

**Description**

Converts styled string information into HTML.

**Since**: 14

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_StyledString\_Descriptor](../../structs/arkui-styledstring-descriptor/document.md)\* descriptor | Pointer to an **ArkUI\_StyledString\_Descriptor** object. |

**Return value**

| Type | Description |
| :-- | :-- |
| const char\* | Pointer to the HTML object. This pointer is internally managed and is released when [OH\_ArkUI\_StyledString\_Descriptor\_Destroy()](#oh_arkui_styledstring_descriptor_destroy) is called. |

#### \[h2\]OH\_ArkUI\_TextLayoutManager\_Dispose()

void OH\_ArkUI\_TextLayoutManager\_Dispose(ArkUI\_TextLayoutManager\* layoutManager)

**Description**

Releases the memory occupied by the text layout manager.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_TextLayoutManager](../../structs/arkui-textlayoutmanager/document.md)\* layoutManager | Pointer to the **ArkUI\_TextLayoutManager** object. |

#### \[h2\]OH\_ArkUI\_TextLayoutManager\_GetLineCount()

ArkUI\_ErrorCode OH\_ArkUI\_TextLayoutManager\_GetLineCount(ArkUI\_TextLayoutManager\* layoutManager, int32\_t\* outLineCount)

**Description**

Obtains the number of lines.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_TextLayoutManager](../../structs/arkui-textlayoutmanager/document.md)\* layoutManager | Pointer to the **ArkUI\_TextLayoutManager** object. |
| int32\_t\* outLineCount | Pointer to the number of text lines. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_ErrorCode](../native-type-h/document.md#arkui_errorcode) | 
Return result.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_TextLayoutManager\_GetRectsForRange()

ArkUI\_ErrorCode OH\_ArkUI\_TextLayoutManager\_GetRectsForRange(ArkUI\_TextLayoutManager\* layoutManager, int32\_t start, int32\_t end, OH\_Drawing\_RectWidthStyle widthStyle, OH\_Drawing\_RectHeightStyle heightStyle, OH\_Drawing\_TextBox\*\* outTextBoxes)

**Description**

Obtains the drawing area information of characters or placeholders within a specified text range under the given rectangle width and height.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_TextLayoutManager](../../structs/arkui-textlayoutmanager/document.md)\* layoutManager | Pointer to the **ArkUI\_TextLayoutManager** object. |
| int32\_t start | Start index. The value of **start** must be greater than or equal to **0**. Otherwise, a parameter error is returned. |
| int32\_t end | End index. The value of **end** must be greater than or equal to that of **start**. Otherwise, a parameter error is returned. |
| [OH\_Drawing\_RectWidthStyle](../../../../../graphics/arkgraphics-2d/c-apis/header-files/drawing-text-typography-h/document.md#oh_drawing_rectwidthstyle) widthStyle | Width style of the rectangle. |
| [OH\_Drawing\_RectHeightStyle](../../../../../graphics/arkgraphics-2d/c-apis/header-files/drawing-text-typography-h/document.md#oh_drawing_rectheightstyle) heightStyle | Height style of the rectangle. |
| [OH\_Drawing\_TextBox](../../../../../graphics/arkgraphics-2d/c-apis/structs/oh-drawing-textbox/document.md)\*\* outTextBoxes | Level-2 pointer to the **OH\_Drawing\_TextBox** object. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_ErrorCode](../native-type-h/document.md#arkui_errorcode) | 
Return result.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_TextLayoutManager\_GetGlyphPositionAtCoordinate()

ArkUI\_ErrorCode OH\_ArkUI\_TextLayoutManager\_GetGlyphPositionAtCoordinate(ArkUI\_TextLayoutManager\* layoutManager, double dx, double dy, OH\_Drawing\_PositionAndAffinity\*\* outPos)

**Description**

Obtains the position of the glyph closest to the given coordinates.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_TextLayoutManager](../../structs/arkui-textlayoutmanager/document.md)\* layoutManager | Pointer to the **ArkUI\_TextLayoutManager** object. |
| double dx | X coordinate relative to the control, in px. |
| double dy | Y coordinate relative to the control, in px. |
| [OH\_Drawing\_PositionAndAffinity](../../../../../graphics/arkgraphics-2d/c-apis/structs/oh-drawing-positionandaffinity/document.md)\*\* outPos | Level-2 pointer to the **OH\_Drawing\_PositionAndAffinity** object. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_ErrorCode](../native-type-h/document.md#arkui_errorcode) | 
Return result.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_TextLayoutManager\_GetLineMetrics()

ArkUI\_ErrorCode OH\_ArkUI\_TextLayoutManager\_GetLineMetrics(ArkUI\_TextLayoutManager\* layoutManager, int32\_t lineNumber, OH\_Drawing\_LineMetrics\* outMetrics)

**Description**

Obtains the information about the specified line, including line metrics, text style information, and font properties.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_TextLayoutManager](../../structs/arkui-textlayoutmanager/document.md)\* layoutManager | Pointer to the **ArkUI\_TextLayoutManager** object. |
| int32\_t lineNumber | Index of the line number. It starts from **0**. If the value of **lineNumber** is less than **0** or greater than or equal to the number of text lines, a parameter error is returned. |
| [OH\_Drawing\_LineMetrics](../../../../../graphics/arkgraphics-2d/c-apis/structs/oh-drawing-linemetrics/document.md)\* outMetrics | Pointer to the **OH\_Drawing\_LineMetrics** object. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_ErrorCode](../native-type-h/document.md#arkui_errorcode) | 
Return result.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |
