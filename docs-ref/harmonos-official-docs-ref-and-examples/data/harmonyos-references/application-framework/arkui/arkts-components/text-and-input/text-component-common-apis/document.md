# Text Component Common APIs

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/dUCzJ1-QT5WKDGQQg4GlCw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8CC0CACD9869DEDE930C99A6BC23A819CBB25825DEFD3EAB3EA91593C3F49C64)

This topic covers the common APIs of text components.

The initial APIs of this module are supported since API version 10. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### CaretStyle10+

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| width | [Length](../../common-definitions/basic-types/document.md#length) | No | Yes | 
Caret size. It cannot be set in percentage.

Default value: **'2vp'**.

 |
| color | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | No | Yes | 

Caret color.

Default value: **'#ff007dff'**.

 |

#### LayoutManager12+

Implements a layout manager object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/15x2hV48Q-i8mTRL7boUhA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C2FA3E324A38CB376C84C3BAA4CC30F463E0934A94129328C645D7C08F165033)

After the text content is changed, you must wait for the layout to be completed before you can obtain the most up-to-date layout information.

## Objects to Import

The **Text** component is used as an example. For details, see [Example 10: Obtaining Text Information](../text/document.md#example-10-obtaining-text-information).

controller: TextController = new TextController();
let layoutManager: LayoutManager = this.controller.getLayoutManager();

#### \[h2\]getLineCount12+

getLineCount(): number

Obtains the total number of lines in the component.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| number | Total number of lines in the component. |

#### \[h2\]getGlyphPositionAtCoordinate12+

getGlyphPositionAtCoordinate(x: number, y: number): PositionWithAffinity

Obtains the position of a glyph close to a given coordinate.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| x | number | Yes | 
X coordinate relative to the component.

Unit: [px](../../common-definitions/pixel-units/document.md)

 |
| y | number | Yes | 

Y coordinate relative to the component.

Unit: [px](../../common-definitions/pixel-units/document.md)

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [PositionWithAffinity](#positionwithaffinity12) | Position of the glyph. |

#### \[h2\]getLineMetrics12+

getLineMetrics(lineNumber: number): LineMetrics

Obtains the information about the specified line, including line metrics, text style information, and font properties.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| lineNumber | number | Yes | Line number, which is zero-based. |

**Return value**

| Type | Description |
| :-- | :-- |
| [LineMetrics](#linemetrics12) | 
Information about the specified line, including line metrics, text style information, and font properties.

Returns an invalid value if the line number is less than 0 or exceeds the actual number of lines.

 |

#### \[h2\]getRectsForRange14+

getRectsForRange(range: TextRange, widthStyle: RectWidthStyle, heightStyle: RectHeightStyle): Array<TextBox>

Obtains the drawing area information for characters or placeholders within a specified text range, based on the specified width and height of a rectangle.

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| range | [TextRange](#textrange12) | Yes | Text range for which to obtain the area information. |
| widthStyle | [RectWidthStyle](#rectwidthstyle14) | Yes | Width of the rectangle. |
| heightStyle | [RectHeightStyle](#rectheightstyle14) | Yes | Height of the rectangle. |

**Return value**

| Type | Description |
| :-- | :-- |
| Array<[TextBox](#textbox14)\> | Array holding the rectangles obtained. |

#### PositionWithAffinity12+

Describes the position and affinity of a glyph.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| position | number | No | No | Index of the glyph relative to the paragraph. The value is an integer. |
| affinity | [Affinity](#affinity12) | No | No | Affinity of the position. |

#### TextMenuItemId12+

Defines the unique identifier for a custom menu item. It is used to identify menu items. The IDs for built-in menu items are listed in the table below.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### \[h2\]Properties

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| CUT | [TextMenuItemId](#textmenuitemid12) | Yes | No | 
ID for the default cut menu item.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| COPY | [TextMenuItemId](#textmenuitemid12) | Yes | No | 

ID for the default copy menu item.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| PASTE | [TextMenuItemId](#textmenuitemid12) | Yes | No | 

ID for the default paste menu item.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| SELECT\_ALL | [TextMenuItemId](#textmenuitemid12) | Yes | No | 

ID for the default select-all menu item.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| COLLABORATION\_SERVICE | [TextMenuItemId](#textmenuitemid12) | Yes | No | 

ID for the collaboration service menu item.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| CAMERA\_INPUT | [TextMenuItemId](#textmenuitemid12) | Yes | No | 

ID for the camera input menu item.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| AI\_WRITER13+ | [TextMenuItemId](#textmenuitemid12) | Yes | No | 

ID for the menu item involving text enhancement features, such as polishing, summary extraction, and formatting, for selected text. This menu item requires foundation model capabilities to work.

**Atomic service API**: This API can be used in atomic services since API version 13.

 |
| TRANSLATE15+ | [TextMenuItemId](#textmenuitemid12) | Yes | No | 

ID for the translate menu item. ID for the translate menu item.

**Atomic service API**: This API can be used in atomic services since API version 15.

 |
| SHARE18+ | [TextMenuItemId](#textmenuitemid12) | Yes | No | 

ID for the share menu item. ID for the share menu item, which launches a window for sharing the selected text.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| SEARCH18+ | [TextMenuItemId](#textmenuitemid12) | Yes | No | 

ID for the search menu item. ID for the search menu item, which launches a browser to search the selected text.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| url20+ | [TextMenuItemId](#textmenuitemid12) | Yes | No | 

ID for the URL menu item. Redirection service for the selected URL, launching a browser search or application page.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |
| email20+ | [TextMenuItemId](#textmenuitemid12) | Yes | No | 

ID for the email menu item. Redirection service for the selected email address, launching the email application.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |
| phoneNumber20+ | [TextMenuItemId](#textmenuitemid12) | Yes | No | 

ID for the phone call menu item. Redirection service for the selected phone number, launching the phone dialer page.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |
| address20+ | [TextMenuItemId](#textmenuitemid12) | Yes | No | 

ID for the navigation menu item. Redirection service for the selected address, launching the map application.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |
| dateTime20+ | [TextMenuItemId](#textmenuitemid12) | Yes | No | 

ID for the event creation menu item. Redirection service for the selected date and time, launching the page for creating a calendar event.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |
| askAI20+ | [TextMenuItemId](#textmenuitemid12) | Yes | No | 

ID for the AI assistant menu item, which provides AI query capabilities for the selected text.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |

#### \[h2\]of

static of(id: ResourceStr): TextMenuItemId

Creates a **TextMenuItemId** object based on **id**.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| id | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | Yes | Menu ID. |

**Return value**

| Type | Description |
| :-- | :-- |
| [TextMenuItemId](#textmenuitemid12) | **TextMenuItemId** object. |

#### \[h2\]equals

equals(id: TextMenuItemId): boolean

Checks whether this **TextMenuItemId** object is the same as another **TextMenuItemId** object.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| id | [TextMenuItemId](#textmenuitemid12) | Yes | ID of the **TextMenuItemId** object to compare. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | 
Whether the two **TextMenuItemId** objects are the same.

**true** if the objects are equal; **false** otherwise.

 |

#### TextMenuItem12+

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| content | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | No | 
Menu name.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| icon | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 

Menu icon.

Online images are not supported.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| id | [TextMenuItemId](#textmenuitemid12) | No | No | 

Menu ID.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| labelInfo15+ | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 

Shortcut key hint.

This field is only supported on 2-in-1 devices.

**Atomic service API**: This API can be used in atomic services since API version 15.

 |

#### EditMenuOptions

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### \[h2\]Properties

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| onPrepareMenu20+ | [OnPrepareMenuCallback](#onpreparemenucallback20) | No | Yes | 
Triggered before the menu is displayed after the text selection area changes. Menu data can be configured within this callback.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |

#### \[h2\]onCreateMenu12+

onCreateMenu(menuItems: Array<TextMenuItem>): Array<TextMenuItem>

Triggered when the menu is being created. Menu data can be configured within this callback.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| menuItems | Array<[TextMenuItem](#textmenuitem12)\> | Yes | 
Menu items to be displayed.

**NOTE**

Modifications to the name, icon, or shortcut hint of default menu items do not take effect.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Array<[TextMenuItem](#textmenuitem12)\> | Menu items after the processing. |

#### \[h2\]onMenuItemClick12+

onMenuItemClick(menuItem: TextMenuItem, range: TextRange): boolean

Triggered when the specified menu item is clicked.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| menuItem | [TextMenuItem](#textmenuitem12) | Yes | Menu item. |
| range | [TextRange](#textrange12) | Yes | Selected text. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | 
Execution logic of the menu item.

Returns **true** if the default system logic is intercepted and only the custom logic is executed.

Returns **false** if the custom logic is executed before the default system logic.

 |

#### OnPrepareMenuCallback20+

type OnPrepareMenuCallback = (menuItems: Array<TextMenuItem>) => Array<TextMenuItem>

Triggered before the menu is displayed after the text selection area changes. Menu data can be configured within this callback.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| menuItems | Array<[TextMenuItem](#textmenuitem12)\> | Yes | 
Menu items to be displayed.

**NOTE**

Modifications to the name, icon, or shortcut hint of default menu items do not take effect.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Array<[TextMenuItem](#textmenuitem12)\> | Menu items after the processing. |

#### TextRange12+

Defines the text range.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| start | number | No | Yes | Start index. |
| end | number | No | Yes | End index. |

#### EditableTextOnChangeCallback12+

type EditableTextOnChangeCallback = (value: string, previewText?: PreviewText, options?: TextChangeOptions) => void

Represents the callback triggered when the content in the text box changes.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | string | Yes | Text displayed in the text box. |
| previewText | [PreviewText](#previewtext12) | No | Information about the preview text, including its start position and text content. |
| options15+ | [TextChangeOptions](#textchangeoptions15) | No | Information about the text change, including the selection range, the text content on the screen, and the preview text content. |

#### TextDataDetectorType11+

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| PHONE\_NUMBER | 0 | Phone number. |
| URL | 1 | URL. |
| EMAIL | 2 | Email address. |
| ADDRESS | 3 | Address. |
| DATE\_TIME12+ | 4 | Time. |

#### TextDeleteDirection12+

Defines the direction for deleting text.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| BACKWARD | 0 | Backward delete. |
| FORWARD | 1 | Forward delete. |

#### SuperscriptStyle20+

Enumerates the text superscript and subscript styles.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| NORMAL | 0 | Normal text style. |
| SUPERSCRIPT | 1 | Superscript text style. |
| SUBSCRIPT | 2 | Subscript text style. |

#### MenuType13+

Enumerates the menu types.

**Atomic service API**: This API can be used in atomic services since API version 13.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| SELECTION\_MENU | 0 | Text selection menu. |
| PREVIEW\_MENU | 1 | Preview menu. |

#### KeyboardAppearance15+

Enumerates the appearance modes of the keyboard.

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| NONE\_IMMERSIVE | 0 | Default appearance mode, not using immersive style. |
| IMMERSIVE | 1 | Immersive style, following the system color mode. |
| LIGHT\_IMMERSIVE | 2 | Immersive style in light mode. |
| DARK\_IMMERSIVE | 3 | Immersive style in dark mode. |

#### InsertValue12+

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| insertOffset | number | No | No | Position of the inserted text. |
| insertValue | string | No | No | Content of the inserted text. |

#### DeleteValue12+

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| deleteOffset | number | No | No | Position of the deleted text. |
| direction | [TextDeleteDirection](#textdeletedirection12) | No | No | Direction for deleting the text. |
| deleteValue | string | No | No | Content of the deleted text. |

#### TextDataDetectorConfig11+

This configuration is only available for the [Text](../text/document.md) and [RichEditor](../richeditor/document.md) components.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| types | [TextDataDetectorType](#textdatadetectortype11)\[\] | No | No | 
Entity types for text recognition. Values **null** and **\[\]** indicate that all types of entities can be recognized.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| onDetectResultUpdate | Callback<string> | No | Yes | 

Callback invoked when text recognition succeeds.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| color12+ | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | No | Yes | 

Entity color when text recognition succeeds.

Default value: **'#ff0a59f7'**

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| decoration12+ | [DecorationStyleInterface](../styled-string/document.md#decorationstyleinterface) | No | Yes | 

Style of the entity decoration when text recognition succeeds.

Default value:

{

type: TextDecorationType.Underline,

color: same as the entity

style: TextDecorationStyle.SOLID

}

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| enablePreviewMenu20+ | boolean | No | Yes | 

Whether to enable the preview menu displayed when long-pressing recognized text. The value **true** means to enable the preview menu, and **false** means the opposite.

Default value: **false**.

When [copyOptions](../richeditor/document.md#copyoptions) is set to **None**, even if **enablePreviewMenu** is set to **true**, long-pressing AI entities will not display the preview menu.

**Device behavior differences**: This parameter is supported on phones, tablets, PCs/2-in-1 devices, and wearables, but does not work on other devices.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |

#### PreviewText12+

Preview text.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| offset | number | No | No | Start position of the preview text. |
| value | string | No | No | Content of the preview text. |

#### FontSettingOptions12+

Defines the font settings.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| enableVariableFontWeight | boolean | No | Yes | 
Whether to enable variable font weight adjustment. This parameter serves as the input for the [fontWeight](../text/document.md#fontweight12) API. When the **weight** value in **fontWeight** is a non-hundred value within the \[100, 900\] range, **enableVariableFontWeight** controls whether this **weight** value is applied.

Default value: **false**.

**true**: Enable variable font weight adjustment. If the **weight** value is an integer within the \[100, 900\] range, it is applied as the font weight.

**false**: Disable variable font weight adjustment. If the **weight** value is an integer multiple of 100 within the \[100, 900\] range, it is used as the font weight. If the **weight** value is not an integer multiple of 100, the font weight defaults to 400.

 |

#### OnDidChangeCallback12+

type OnDidChangeCallback = (rangeBefore: TextRange, rangeAfter: TextRange) => void

Represents the callback invoked after text changes.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| rangeBefore | [TextRange](#textrange12) | Yes | Range of the text to be changed. |
| rangeAfter | [TextRange](#textrange12) | Yes | Range of the text added. |

#### StyledStringChangedListener12+

Defines the listener for changes of the styled string text content.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| onWillChange | Callback<[StyledStringChangeValue](#styledstringchangevalue12), boolean> | No | Yes | Callback invoked when text is about to change. |
| onDidChange | [OnDidChangeCallback](#ondidchangecallback12) | No | Yes | Callback invoked when text is changed. |

#### StyledStringChangeValue12+

Describes the text changes of the styled string.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| range | [TextRange](#textrange12) | No | No | Range of the styled string to be replaced in the original string. |
| replacementString | [StyledString](../styled-string/document.md#styledstring) | No | No | Styled string used for replacement. |
| previewText | [StyledString](../styled-string/document.md#styledstring) | No | Yes | Preview styled string. |

#### AutoCapitalizationMode20+

Enumerates automatic capitalization modes. This only provides API capabilities; the specific implementation depends on the input method application.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| NONE | 0 | Default state; automatic capitalization is disabled. |
| WORDS | 1 | Automatic capitalization is applied per word: The first character of each word is capitalized, others are lowercase. |
| SENTENCES | 2 | Automatic capitalization is applied per sentence: The first character of each sentence is capitalized, others are lowercase. |
| ALL\_CHARACTERS | 3 | Automatic capitalization applied to all characters. |

#### TextBaseController12+

Defines a text selection controller.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### \[h2\]setSelection12+

setSelection(selectionStart: number, selectionEnd: number, options?: SelectionOptions): void

Sets the range of content selection. The selected content is highlighted.

If both **selectionStart** and **selectionEnd** are set to **\-1**, the entire content is selected.

The component must be focused for the API call to have effect.

Since API version 12, on 2-in-1 devices, regardless of the value of **options**, calling the **setSelection** API will not display a menu; if a menu is already open, calling the API will close it.

On non-2-in-1 devices, when **options** is set to **MenuPolicy.DEFAULT**, the following rules apply after the API is called:

1.  If the component has a menu with a selection handle, the menu remains open and is relocated according to the selection.
    
2.  If the component has a menu without a selection handle, the menu remains open and its position remains unchanged.
    
3.  If there is no menu open, no menu will appear after the selection.
    

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| selectionStart | number | Yes | 
Start position of the selection.

Values less than 0 are treated as **0**.

 |
| selectionEnd | number | Yes | 

End position of the selection.

If the value exceeds the text length, the current text length is used instead.

 |
| options | [SelectionOptions](../text-box-component-common-apis/document.md#selectionoptions12) | No | Configuration of options. |

#### \[h2\]closeSelectionMenu12+

closeSelectionMenu(): void

Closes the custom or default text selection menu.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### \[h2\]getLayoutManager12+

getLayoutManager(): LayoutManager

Obtains a **LayoutManager** object.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| [LayoutManager](#layoutmanager12) | Implements a **LayoutManager** object. |

#### TextEditControllerEx12+

Implements an extended text editing controller.

Inherits [TextBaseController](#textbasecontroller12).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### \[h2\]isEditing12+

isEditing(): boolean

Obtains the editing status of the rich text.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Editing status of the rich text. **true** means that the text is in editable state, and **false** means the opposite. |

#### \[h2\]stopEditing12+

stopEditing(): void

Stops editing.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### \[h2\]getCaretOffset12+

getCaretOffset(): number

Obtains the current position of the caret.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| number | Position of the caret. |

#### \[h2\]setCaretOffset12+

setCaretOffset(offset: number): boolean

Sets the offset of the caret.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| offset | number | Yes | Offset of the caret. If the offset is outside the range of all content, the setting fails. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | 
Whether the caret offset is set successfully.

Returns **true** if it is set successfully; returns **false** otherwise.

 |

#### \[h2\]getPreviewText12+

getPreviewText?(): PreviewText

Obtains the preview text.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| [PreviewText](#previewtext12) | Preview text. |

#### StyledStringController12+

Defines a styled string controller.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### \[h2\]setStyledString12+

setStyledString(styledString: StyledString): void

Sets the styled string displayed in the rich text component.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| styledString | [StyledString](../styled-string/document.md#styledstring) | Yes | 
Styled string to set.

**NOTE**

The child class [MutableStyledString](../styled-string/document.md#mutablestyledstring) of **StyledString** can also serve as the argument.

 |

#### \[h2\]getStyledString12+

getStyledString(): MutableStyledString

Obtains the styled string displayed in the rich text component.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| [MutableStyledString](../styled-string/document.md#mutablestyledstring) | Styled string displayed in the rich text component. |

#### DecorationStyleResult12+

Provides the text decoration information returned by the backend.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| type | [TextDecorationType](../../common-definitions/enums/document.md#textdecorationtype) | No | No | 
Type of the text decoration.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| color | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | No | No | 

Color of the text decoration.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| style | [TextDecorationStyle](../../common-definitions/enums/document.md#textdecorationstyle12) | No | Yes | 

Style of the text decoration.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| thicknessScale20+ | number | No | Yes | 

Scale factor of the text decoration thickness.

Default value: **1.0**.

Value range: \[0, +∞).

Note: Negative values are treated as the default value.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |

#### LineMetrics12+

type LineMetrics = LineMetrics

Describes the measurement information of a single line of text in the text layout.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Type | Description |
| :-- | :-- |
| [LineMetrics](../../../../../graphics/arkgraphics-2d/arkts-apis/ohos-graphics-text-text/document.md#linemetrics) | Measurement information of a single line of text in the text layout. |

#### Affinity12+

type Affinity = Affinity

Enumerates the affinity modes.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Type | Description |
| :-- | :-- |
| [Affinity](../../../../../graphics/arkgraphics-2d/arkts-apis/ohos-graphics-text-text/document.md#affinity) | Affinity mode enum. |

#### TextBox14+

type TextBox = TextBox

Describes the rectangle that holds the text.

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Type | Description |
| :-- | :-- |
| [TextBox](../../../../../graphics/arkgraphics-2d/arkts-apis/ohos-graphics-text-text/document.md#textbox) | Rectangle that holds the text. |

#### Paragraph20+

type Paragraph = Paragraph

Implements a carrier that stores the text content and style. You can perform operations such as layout and drawing.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Type | Description |
| :-- | :-- |
| [Paragraph](../../../../../graphics/arkgraphics-2d/arkts-apis/ohos-graphics-text-text/document.md#paragraph) | Carrier that stores the text content and style. You can perform operations such as layout and drawing. |

#### RectHeightStyle14+

type RectHeightStyle = RectHeightStyle

Enumerates the rectangle height styles.

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Type | Description |
| :-- | :-- |
| [RectHeightStyle](../../../../../graphics/arkgraphics-2d/arkts-apis/ohos-graphics-text-text/document.md#rectheightstyle) | Rectangle height style. |

#### RectWidthStyle14+

type RectWidthStyle = RectWidthStyle

Enumerates the rectangle width styles.

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Type | Description |
| :-- | :-- |
| [RectWidthStyle](../../../../../graphics/arkgraphics-2d/arkts-apis/ohos-graphics-text-text/document.md#rectwidthstyle) | Rectangle width style. |

#### TextChangeOptions15+

Provides information about the text before and after a change, including the selection ranges.

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| rangeBefore | [TextRange](#textrange12) | No | No | Selection range before the change. |
| rangeAfter | [TextRange](#textrange12) | No | No | Selection range after the change. |
| oldContent | string | No | No | Text content before the change. |
| oldPreviewText | [PreviewText](#previewtext12) | No | No | Preview text before the change. |

#### EditableTextChangeValue15+

Provides detailed information of text changes, including preview text.

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| content | string | No | No | Current text content. |
| previewText | [PreviewText](#previewtext12) | No | Yes | Preview text. |
| options | [TextChangeOptions](#textchangeoptions15) | No | Yes | Information about the text change. |

#### TextMenuShowMode16+

Enumerates the display modes for context menus on selection.

**Atomic service API**: This API can be used in atomic services since API version 16.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| DEFAULT | 0 | 
The menu is displayed in the current window.

 |
| PREFER\_WINDOW | 1 | 

The menu is preferentially displayed in a separate window. If a separate window is not supported, the menu is displayed in the current window.

**NOTE**

The context menu on selection cannot be displayed in a separate window under the following scenarios:

Windows other than the main application window, application subwindows, system modal windows, and system home screen windows

DevEco Studio Previewer

UIExtension

Text component that is already displayed in a child window (for example, **Popup**, **Dialog**, **Toast**, and **Menu**)

**TextInput** or **TextArea** components that support **AutoFill**

 |

#### TextMenuOptions16+

Provides the options for customizing the context menu on selection.

**Atomic service API**: This API can be used in atomic services since API version 16.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| showMode | [TextMenuShowMode](#textmenushowmode16) | No | Yes | 
Menu display mode.

Default value: **TextMenuShowMode.DEFAULT**

 |

#### ShaderStyle20+

Defines the base class for text shader effects.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### LinearGradientStyle20+

Displays a linear gradient. **LinearGradientStyle** inherits from [ShaderStyle](#shaderstyle20).

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### \[h2\]Properties

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| options | [LinearGradientOptions](../../universal-attributes/visual-effects/color-gradient/document.md#lineargradientoptions18) | No | No | Options for displaying a linear gradient. |

#### \[h2\]constructor20+

constructor(options: LinearGradientOptions)

A constructor used to create a **LinearGradientStyle** object.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [LinearGradientOptions](../../universal-attributes/visual-effects/color-gradient/document.md#lineargradientoptions18) | Yes | Options for displaying a linear gradient. |

#### RadialGradientStyle20+

Displays a radial gradient. **RadialGradientStyle** inherits from [ShaderStyle](#shaderstyle20).

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### \[h2\]Properties

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| options | [RadialGradientOptions](../../universal-attributes/visual-effects/color-gradient/document.md#radialgradientoptions18) | No | No | Options for displaying a radial gradient. |

#### \[h2\]constructor20+

constructor(options: RadialGradientOptions)

A constructor used to create a **RadialGradientStyle** object.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [RadialGradientOptions](../../universal-attributes/visual-effects/color-gradient/document.md#radialgradientoptions18) | Yes | Options for displaying a radial gradient. |

#### ColorShaderStyle20+

Displays a solid color. **ColorShaderStyle** inherits from [ShaderStyle](#shaderstyle20).

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### \[h2\]Properties

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| color | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | No | No | Options for displaying a solid color. |

#### \[h2\]constructor20+

constructor(color: ResourceColor)

A constructor used to create a **ColorShaderStyle** object.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| color | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | Yes | Options for displaying a solid color. |

#### IMEClient20+

Defines the input method client type bound to an input component.

#### \[h2\]Properties

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| nodeId | number | No | No | Unique ID of the current input component. The value must be greater than or equal to 0. |

#### \[h2\]setExtraConfig22+

setExtraConfig(config: InputMethodExtraConfig): void

Sets the extension information for an input method.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| config | [InputMethodExtraConfig](#inputmethodextraconfig22) | Yes | Extension information of the input method. |

#### MaxLinesOptions20+

Configures the display effect of the **TextArea** component when the text exceeds the maximum number of lines.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| overflowMode | [MaxLinesMode](#maxlinesmode20) | No | Yes | Non-inline mode of the **TextArea** component. When the text exceeds the set value of **maxLines** (maximum number of lines), a scroll effect is enabled. This requires simultaneous configuration of [textOverflow](../textarea/document.md#textoverflow12), and **MaxLinesMode** takes effect only when **textOverflow** is set to **None** or **Clip**. By default, **MaxLinesMode** is set to **Clip**, indicating that text is clipped when it exceeds the value of **maxLines**. |

#### MaxLinesMode20+

Enumerates the display effects of the **TextArea** component when text exceeds the maximum number of lines. The default value is **CLIP** (truncating text at the maximum line count).

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| CLIP | 0 | Text is clipped when it exceeds the maximum number of lines. |
| SCROLL | 1 | Text can be scrolled when it exceeds the maximum number of lines. |

#### LineSpacingOptions20+

Configures the line spacing of text and whether it applies only between lines.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| onlyBetweenLines | boolean | No | Yes | 
Whether line spacing applies only between lines.

**true**: Line spacing applies only between lines; no extra spacing is added above the first line or below the last line. **false**: Extra line spacing is added both above the first line and below the last line.

Default value: **false**.

 |

#### TextVerticalAlign20+

Defines the vertical alignment mode of text. The default value is **BASELINE** (aligning along the baseline).

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| BASELINE | 0 | Aligns text along the baseline. |
| BOTTOM | 1 | Aligns text to the bottom. |
| CENTER | 2 | Aligns text vertically to the center. |
| TOP | 3 | Aligns text to the top. |

#### ContentTransition20+

Defines the base class for text transitions.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### NumericTextTransition20+

Implements a flip animation for numeric text. It applies only to positive integers (decimals and negative numbers are not supported). Gradient colors and text marquee mode are not supported. Text selection is not supported, and the [copyOption](../text/document.md#copyoption9) property is ineffective. The flip animation fails if the text contains child components or is set via a styled string.

**NumericTextTransition** inherits from [ContentTransition](#contenttransition20).

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### \[h2\]Properties

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| flipDirection | [FlipDirection](#flipdirection20) | No | Yes | 
Direction of the flip animation.

Default value: **FlipDirection.DOWN**.

 |
| enableBlur | boolean | No | Yes | 

Whether to enable the blur effect for the flip animation.

Default value: **false**.

**true**: Enable the blur effect.

**false**: Disable the blur effect.

 |

#### \[h2\]constructor20+

constructor(options?: NumericTextTransitionOptions)

A constructor used to create a **NumericTextTransition** object.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [NumericTextTransitionOptions](#numerictexttransitionoptions20) | No | Options of the numeric flip animation. |

#### NumericTextTransitionOptions20+

Defines the options of the numeric flip animation.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| flipDirection | [FlipDirection](#flipdirection20) | No | Yes | 
Direction of the flip animation.

Default value: **FlipDirection.DOWN**.

 |
| enableBlur | boolean | No | Yes | 

Whether to enable the blur effect for the flip animation.

Default value: **false**.

**true**: Enable the blur effect.

**false**: Disable the blur effect.

 |

#### FlipDirection20+

Enumerates the directions of the flip animation. The default value is **DOWN**.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| DOWN | 0 | Content flips downward. |
| UP | 1 | Content flips upward. |

#### TextLayoutOptions20+

Defines the text layout options.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| constraintWidth | [LengthMetrics](../../../arkts-api/ui/arkui/graphics/document.md#lengthmetrics12) | No | Yes | Layout width of the measured text. If not set, the width is the maximum width occupied by a single-line layout. |

#### TextContentAlign21+

Enumerates the vertical alignment directions of the text content area.

**Atomic service API**: This API can be used in atomic services since API version 21.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| TOP | 0 | Aligns the content area to the top. |
| CENTER | 1 | Aligns the content area to the center. |
| BOTTOM | 2 | Aligns the content area to the bottom. |

#### TextDirection22+

Enumerates the text directions.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| LTR | 0 | From left to right. |
| RTL | 1 | From right to left. |

#### InputMethodExtraConfig22+

type InputMethodExtraConfig = InputMethodExtraConfig

Represents the extension information of an input method.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Type | Description |
| :-- | :-- |
| [InputMethodExtraConfig](../../../../ime-kit/arkts-apis/ohos-inputmethod-extraconfig-input-method-extension-information/document.md#inputmethodextraconfig) | Extension information of an input method. |
