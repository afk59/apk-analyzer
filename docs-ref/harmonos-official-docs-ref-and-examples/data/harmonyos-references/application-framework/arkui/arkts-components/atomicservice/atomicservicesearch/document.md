# AtomicServiceSearch

**AtomicServiceSearch** allows you to customize the default search area, customizable selection area, and function area (a maximum of two).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/8asBcQSdQAuGPxYaWAoejQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062248Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A7B7F3C3F7424ECC69A54F0A71AE1DE979CC523A6307AA7382FDE2C62EA06DE6)

This component is supported since API version 18. Updates will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { AtomicServiceSearch } from '@kit.ArkUI';

#### AtomicServiceSearch

AtomicServiceSearch({
  value?: ResourceStr,
  placeholder?: ResourceStr,
  controller?: SearchController,
  select?: SelectParams,
  search?: SearchParams,
  operation?: OperationParams,
})

**Atomic service API**: This API can be used in atomic services since API version 18.

**Decorator**: @Component

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Decorator | Description |
| :-- | :-- | :-- | :-- | :-- |
| value | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | @Prop | Text input in the search text box. The default value is an empty string. |
| placeholder | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | @Prop | Default prompt text displayed in the search box. Default value: **Search**. |
| controller | [SearchController](../../text-and-input/search/document.md#searchcontroller) | No | \- | **Search** component controller, which is used to set the position of the input cursor and exit the editing state. Default value: **undefined**. |
| select | [SelectParams](#selectparams) | No | @Prop | Content, event, and style of the selection area. Default value: **undefined**. |
| search | [SearchParams](#searchparams) | No | @Prop | Events and styles supported by the search area. Default value: **undefined**. |
| operation | [OperationParams](#operationparams) | No | \- | Function setting items on the right of the selection area. Default value: **undefined**. |

#### SelectParams

Provides optional attributes for the selection area.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| options | Array<[SelectOption](../../buttons-and-selections/select/document.md#selectoption)\> | No | Yes | Options of the drop-down menu. Default value: **undefined**. |
| selected | number | No | Yes | Index of the initially selected item in the drop-down list box. The index of the first item is 0. If this attribute is not set, the default value **\-1** is used, indicating that no item is selected. |
| selectValue | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | Text content of the drop-down list button itself. Default value: **undefined**. |
| onSelect | [OnSelectCallback](#onselectcallback) | No | Yes | Callback invoked when an item in the drop-down list box is selected. Default value: **undefined**. |
| menuItemContentModifier | [ContentModifier<MenuItemConfiguration>](../../buttons-and-selections/select/document.md#menuitemconfiguration12) | No | Yes | 
Content modifier to apply to the drop-down list box. Once it is applied, the drop-down list box content will be fully customizable by developers. Note that default style attributes (such as dividers, background color, and font styles) will no longer take effect.

**modifier**: content modifier. You need a custom class to implement the **ContentModifier** API. Default value: **undefined**.

 |
| divider | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<[DividerOptions](../../buttons-and-selections/textpicker/document.md#divideroptions12)\> | null | No | Yes | 

Divider options.

1\. If **DividerOptions** is set, the divider is displayed in the configured style. Default value: **{strokeWidth: '1px', color: '#33182431'}**

2\. If this parameter is set to **null**, the divider is not displayed.

3\. If the value of **strokeWidth** is too larger, the divider may overlap the text. The divider extends both upwards and downwards from the bottom of each item.

4\. The default values for **startMargin** and **endMargin** are consistent with the style of the divider when the **divider** attribute is not set. If the sum of **startMargin** and **endMargin** is equal to the value of **optionWidth**, the divider is not displayed. If the sum of **startMargin** and **endMargin** exceeds the value of **optionWidth**, the divider line is displayed in the default style.

 |
| font | [Font](../../common-definitions/basic-types/document.md#font) | No | Yes | Text font of the drop-down list button. Default value: **{size: $r('sys.float.ohos\_id\_text\_size\_body1')}** |
| fontColor | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | No | Yes | Font color of the selected item in the drop-down list box. Default value: **{fontColor: $r('sys.color.ohos\_id\_color\_text\_primary')}** |
| selectedOptionBgColor | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | No | Yes | Background color of the selected item in the drop-down list box. Default value: **$r('sys.color.ohos\_id\_color\_component\_activated')** with the opacity of **$r('sys.color.ohos\_id\_alpha\_highlight\_bg')** |
| selectedOptionFont | [Font](../../common-definitions/basic-types/document.md#font) | No | Yes | Text font of the selected item in the drop-down list box. Default value: **{size: $r('sys.color.ohos\_id\_text\_size\_body1'), weight: FontWeight.Regular}** |
| selectedOptionFontColor | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | No | Yes | Font color of the selected item in the drop-down list box. Default value: **$r('sys.color.ohos\_id\_color\_text\_primary\_activated')** |
| optionBgColor | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | No | Yes | Background color of items in the drop-down list box. Default value: **Color.Transparent** |
| optionFont | [Font](../../common-definitions/basic-types/document.md#font) | No | Yes | Text font of items in the drop-down list box. Default value: **{size: $r('sys.float.ohos\_id\_text\_size\_body1'), weight: FontWeight.Regular}** |
| optionFontColor | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | No | Yes | Font color of items in the drop-down list box. Default value: **$r('sys.color.ohos\_id\_color\_text\_primary')** |
| optionWidth | [Dimension](../../common-definitions/basic-types/document.md#dimension10) | [OptionWidthMode](../../common-definitions/enums/document.md#optionwidthmode11) | No | Yes | Item width of the drop-down list box. This attribute cannot be set in percentage. **OptionWidthMode** is of the enum type and it determines whether the drop-down list box inherits the width of the drop-down list button. If an invalid value or a value less than the minimum width of 56 vp is set, the attribute does not take effect, and the option width uses the default value, which is two columns. |
| optionHeight | [Dimension](../../common-definitions/basic-types/document.md#dimension10) | No | Yes | Maximum height for items in the drop-down list box. This attribute cannot be set in percentage. The default maximum height is 80% of the available height of the screen. The maximum height set cannot exceed the default maximum height. |
| space | [Length](../../common-definitions/basic-types/document.md#length) | No | Yes | Spacing between the text and arrow of an item. Default value: **8** |
| arrowPosition | [ArrowPosition](../../buttons-and-selections/select/document.md#arrowposition10) | No | Yes | Alignment between the text and arrow of an item. Default value: **ArrowPosition.END** |
| menuAlign | [MenuAlignParams](#menualignparams) | No | Yes | Alignment between the drop-down list button and the drop-down list box. Default value: **{alignType: MenuAlignType.START, offset: {dx: 0, dy: 0}}**. |
| menuBackgroundColor | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | No | Yes | Background color of the drop-down list box. Default value: **Color.Transparent** |
| menuBackgroundBlurStyle | [BlurStyle](../../universal-attributes/basic-attributes/background/document.md#blurstyle9) | No | Yes | Background blur style of the drop-down list box. Default value: **BlurStyle.COMPONENT\_ULTRA\_THICK** |

#### SearchParams

Provides optional attributes for the search area.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| searchKey | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | Search key used to find a unique **search** component. Default value: **undefined**. |
| componentBackgroundColor | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | No | Yes | Background color of a component. Default value: **$r('sys.color.ohos\_id\_color\_text\_field\_sub\_bg')**. |
| pressedBackgroundColor | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | No | Yes | Background color of the pressed component. Default value: **$r('sys.color.ohos\_id\_color\_click\_effect')**. |
| searchButton | [SearchButtonParams](#searchbuttonparams) | No | Yes | 
Search button located next to the search text box. Clicking the search button triggers both **onSubmit** and **onClick** callbacks.

\- **value**: Text on the search button located next to the search text box.

\- **option**: Font of the search text box. Default value: **{fontSize: '16fp', fontColor: '#ff3f97e9'}**

 |
| placeholderColor | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | No | Yes | Placeholder text color. Default value: **$r('sys.color.ohos\_id\_color\_text\_secondary')**. |
| placeholderFont | [Font](../../common-definitions/basic-types/document.md#font) | No | Yes | Placeholder text style, including the font size, font weight, font family, and font style. Default value: **{size: $r('sys\_float.ohos\_id\_text\_size\_body1')}**. |
| textFont | [Font](../../common-definitions/basic-types/document.md#font) | No | Yes | Style of the text entered in the search box, including the font size, font width, font family, and font style. Currently, only the default font family is supported. Default value: **{size: $r('sys\_float.ohos\_id\_text\_size\_body1')}**. |
| textAlign | [TextAlign](../../common-definitions/enums/document.md#textalign) | No | Yes | Text alignment mode in the search text box. Default value: **TextAlign.Start**. |
| copyOptions | [CopyOptions](../../common-definitions/enums/document.md#copyoptions9) | No | Yes | Whether the input text can be copied. Default value: **CopyOptions.LocalDevice**. |
| searchIcon | [IconOptions](../../text-and-input/search/document.md#iconoptions10) | [SymbolGlyphModifier](../../universal-attributes/modifiers-and-custom-property/symbol-glyph-modifier/document.md#symbolglyphmodifier) | No | Yes | 

Style of the search icon on the left.

Default value in light mode: **{size: '16vp', color: '#99182431', src:' '}**.

Default value in dark mode: **{size: '16vp', color: '#99ffffff', src:' '}**.

 |
| cancelIcon | [IconOptions](../../text-and-input/search/document.md#iconoptions10) | No | Yes | 

Style of the cancel button on the right. Default value: **{style: CancelButtonStyle.INPUT, icon: {size: '16vp', color: '#99ffffff', src:' '}}**.

When style is set to **CancelButtonStyle.CONSTANT**, the cancel button is displayed in a default style.

 |
| fontColor | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | No | Yes | Font color of the input text. Default value: **$r('sys.color.ohos\_id\_color\_text\_secondary')**. |
| caretStyle | [CaretStyle](../../text-and-input/text-component-common-apis/document.md#caretstyle10) | No | Yes | Pointer style. Default value: **{width: '1.5vp', color: '#007DFF'}**. |
| enableKeyboardOnFocus | boolean | No | Yes | Whether to automatically open the soft keyboard when the **Search** component gains focus. The value **true** means to automatically open the soft keyboard when the **Search** component gains focus. Default value: **true**. |
| hideSelectionMenu | boolean | No | Yes | 

Whether to hide the system text selection menu.

**true**: The system text selection menu does not appear under the following circumstances: clicking the text box cursor, long-pressing the text box, double-tapping the text box, triple-tapping the text box, or right-clicking the text box. **false**: The system text selection menu appears under the following circumstances: clicking the text box cursor, long-pressing the text box, double-tapping the text box, triple-tapping the text box, or right-clicking the text box. Default value: **false**.

 |
| type | [SearchType](../../text-and-input/search/document.md#searchtype11) | No | Yes | Text box type. Default value: **SearchType.Normal**. |
| maxLength | number | No | Yes | Maximum number of characters in the text input. By default, there is no maximum number of characters. When the maximum number is reached, no more characters can be entered. Default value: **\-1**. |
| enterKeyType | [EnterKeyType](../../text-and-input/textinput/document.md#enterkeytype) | No | Yes | Type of the Enter key. Default value: **EnterKeyType.Search**. |
| decoration | [TextDecorationOptions](../../text-and-input/text-box-component-common-apis/document.md#textdecorationoptions12) | No | Yes | Text decorative line options. Default value: **{type: TextDecorationType.None, color: Color.Black, style: TextDecorationStyle.SOLID}**. |
| letterSpacing | number | string | [Resource](../../common-definitions/basic-types/document.md#resource) | No | Yes | Letter spacing. A positive value causes characters to spread farther apart, and a negative value bring characters closer together. The value for floating point numbers is **0.0**, in units of px. If the input is not a number and cannot be parsed as a number, the default value will be used. |
| fontFeature | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 

Font feature, for example, monospaced digits.

Format: normal | <feature-tag-value>

Syntax for <feature-tag-value>: <string> \[ <integer> | on | off \]

There can be multiple **<feature-tag-value>** values, which are separated by commas (,).

For example, the input format for monospaced digits is "ss01" on. Default value: **undefined**.

 |
| selectedBackgroundColor | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | No | Yes | Background color of the selected text. By default, a 20% opacity is applied. |
| inputFilter | [InputFilterParams](#inputfilterparams) | No | Yes | 

Regular expression for input filtering. Only inputs that comply with the regular expression can be displayed. Other inputs are filtered out. The specified regular expression can match single characters, but not strings. Default value: **undefined**.

\- **value**: regular expression.

\- **error**: Filtered-out content to return when regular expression matching fails.

 |
| textIndent | [Dimension](../../common-definitions/basic-types/document.md#dimension10) | No | Yes | Indent of the first line text. Default value: **0**. |
| minFontSize | number | string | [Resource](../../common-definitions/basic-types/document.md#resource) | No | Yes | Minimum font size. For the setting to take effect, this attribute must be used together with **maxFontSize** or layout constraint settings. Default value: **undefined**. |
| maxFontSize | number | string | [Resource](../../common-definitions/basic-types/document.md#resource) | No | Yes | Maximum font size. For the setting to take effect, this attribute must be used together with **minFontSize** or layout constraint settings. Default value: **undefined**. |
| editMenuOptions | [EditMenuOptions](../../text-and-input/text-component-common-apis/document.md#editmenuoptions) | No | Yes | Extended options of the custom context menu on selection, including the text content, icon, and callback. Default value: **undefined**. |
| enablePreviewText | boolean | No | Yes | 

Whether to enable preview text. The value **true** means to enable preview text. Default value: **true**.

Preview text of the input method should be enabled. Preview text is in a temporary state and does not support text interception. As such, it does not trigger **onWillInsert** and **onDidInsert** callbacks.

 |
| enableHapticFeedback | boolean | No | Yes | Whether to enable haptic feedback. The value **true** means to enable haptic feedback. Default value: **true**. |
| onSubmit | Callback<string> | [SearchSubmitCallback](../../text-and-input/search/document.md#searchsubmitcallback14) | No | Yes | Callback triggered when users click the search icon or the search button, or touch the search button on a soft keyboard. Default value: **undefined**. |
| onChange | [EditableTextOnChangeCallback](../../text-and-input/text-component-common-apis/document.md#editabletextonchangecallback12) | No | Yes | Callback triggered when the content in the text box changes. Default value: **undefined**. |
| onCopy | Callback<string> | No | Yes | Callback triggered when a copy operation is performed. Default value: **undefined**. |
| onCut | Callback<string> | No | Yes | Callback triggered when a cut operation is performed. Default value: **undefined**. |
| onPaste | [OnPasteCallback](#onpastecallback) | No | Yes | Callback triggered when a paste operation is performed. Default value: **undefined**. |
| onTextSelectionChange | [OnTextSelectionChangeCallback](#ontextselectionchangecallback) | No | Yes | Callback triggered when the position of the text selection changes or when the cursor position changes during the editing state. Default value: **undefined**. |
| onContentScroll | [OnContentScrollCallback](#oncontentscrollcallback) | No | Yes | Callback triggered when the text content is scrolled. Default value: **undefined**. |
| onEditChange | Callback<boolean> | No | Yes | Callback triggered when the input status changes. If a cursor is displayed, that is, the value of **isEditing** is **true**, the text box is in the editing state. Default value: **undefined**. |
| onWillInsert | Callback<[InsertValue](../../text-and-input/text-component-common-apis/document.md#insertvalue12), boolean> | No | Yes | Callback triggered when text is about to be inserted. **true**: Insert the input content into the result string. **false**: Do not insert the input content into the result string. Default value: **undefined**. |
| onDidInsert | Callback<[InsertValue](../../text-and-input/text-component-common-apis/document.md#insertvalue12)\> | No | Yes | Callback triggered when text is inserted. Default value: **undefined**. |
| onWillDelete | Callback<[DeleteValue](../../text-and-input/text-component-common-apis/document.md#deletevalue12), boolean> | No | Yes | Callback triggered when text is about to be deleted. **true**: Delete the text. **false**: Do not delete the text. Default value: **undefined**. |
| onDidDelete | Callback<[DeleteValue](../../text-and-input/text-component-common-apis/document.md#deletevalue12)\> | No | Yes | Callback triggered when text is deleted. Default value: **undefined**. |

#### OperationParams

Sets initialization parameters of the function area.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| auxiliaryItem | [OperationOption](../../system-preset-ui-component-library/subheader/document.md#operationoption) | No | Yes | Auxiliary item on the right of the search area. Default value: **undefined**. |
| independentItem | [OperationOption](../../system-preset-ui-component-library/subheader/document.md#operationoption) | No | Yes | Independent item on the right of the search area. Default value: **undefined**. |

#### InputFilterParams

Sets regular expression for input filtering.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| inputFilterValue | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | No | Regular expression. |
| error | Callback<string> | No | Yes | Callback used to return the filtered-out content when regular expression matching fails. Default value: **undefined**. |

#### SearchButtonParams

Sets the search button located next to the search text box.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| searchButtonValue | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | No | Text on the search button located next to the search text box. |
| options | [SearchButtonOptions](../../text-and-input/search/document.md#searchbuttonoptions10) | No | Yes | Font of the search text box. Default value: **{fontSize: '16fp',fontColor: '#ff3f97e9'}** |

#### MenuAlignParams

Sets the alignment between the drop-down list button and the drop-down list box.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| alignType | [MenuAlignType](../../buttons-and-selections/select/document.md#menualigntype10) | No | No | Alignment type. Default value: **MenuAlignType.START** |
| offset | [Offset](../../common-definitions/basic-types/document.md#offset) | No | Yes | Offset of the drop-down list box relative to the drop-down list button after alignment based on the alignment type. Default value: **{dx: 0, dy: 0}** |

#### OnSelectCallback

type OnSelectCallback = (index: number, selectValue: string) => void

Called when an item in the drop-down list box is selected.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| index | number | Yes | Index of the selected option. The index is zero-based. |
| selectValue | string | Yes | Value of the selected option. |

#### OnPasteCallback

type OnPasteCallback = (pasteValue: string, event: PasteEvent) => void

Called when a paste operation is performed.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| pasteValue | string | Yes | Text to be pasted. |
| event | [PasteEvent](../../text-and-input/richeditor/document.md#pasteevent11) | Yes | Custom paste event. |

#### OnTextSelectionChangeCallback

type OnTextSelectionChangeCallback = (selectionStart: number, selectionEnd: number) => void

Called when the position of the text selection changes or when the cursor position changes during the editing state.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| selectionStart | number | Yes | Start position of the text to be selected. |
| selectionEnd | number | Yes | End position of the text to be selected. |

#### OnContentScrollCallback

type OnContentScrollCallback = (totalOffsetX: number, totalOffsetY: number) => void

Called when the text content is scrolled.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| totalOffsetX | number | Yes | Offset of the horizontal coordinate of the upper left corner of the text relative to the horizontal coordinate of the upper left corner of the entire content input area. |
| totalOffsetY | number | Yes | Offset of the vertical coordinate of the upper left corner of the text relative to the vertical coordinate of the upper left corner of the entire content input area. |

#### Example

## Example 1: Adding a Selection Area to AtomicServiceSearch

This example demonstrates how to use the **select** parameter to add a selection area on the left to the **AtomicServiceSearch** component.

import { AtomicServiceSearch } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  build() {
    Column({ space: 6 }) {
      Text('AtomicServiceSearch + selection area').alignSelf(ItemAlign.Start).decoration({
        type: TextDecorationType.Underline,
        color: Color.Black,
        style: TextDecorationStyle.SOLID
      }).margin({ top: 20, bottom: 20 })

      AtomicServiceSearch({
        select: {
          options: \[
            { value: 'Select1', icon: $r("app.media.sweep") }, // Custom resource
            { value: 'Select2', icon: $r("app.media.sweep") }, // Custom resource
            { value: 'Select3', icon: $r("app.media.sweep") }, // Custom resource
            { value: 'Select4', icon: $r("app.media.sweep") } // Custom resource
          \],
          selected: -1,
          selectValue: 'Select1',
          onSelect: (index: number, selectValue: string) => { // Custom event
            if (index === 0) {
              this.alert(\`index: ${index}, selectValue: ${selectValue}\`);
            } else if (index === 1) {
              this.alert(\`index: ${index}, selectValue: ${selectValue}\`);
            } else if (index === 2) {
              this.alert(\`index: ${index}, selectValue: ${selectValue}\`);
            } else if (index === 3) {
              this.alert(\`index: ${index}, selectValue: ${selectValue}\`);
            }
          },
        }
      })
    }.padding({ left: 16, right: 16 })
  }

  private alert(message: string): void {
    this.getUIContext().showAlertDialog({ message: message });
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/L9H7bB9DQiOqoH8qg1j_wg/en-us_image_0000002537765944.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062248Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=20D32DE90D4B62D1662B9353CB4714A1E583D0A57F939B185BAB1E387AA45215)

## Example 2: Adding a Function Item to AtomicServiceSearch

This example demonstrates how to use the **operation** parameter to add a function item on the right to the **AtomicServiceSearch** component.

import { AtomicServiceSearch } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  build() {
    Column({ space: 6 }) {
      Text('AtomicServiceSearch + function items').alignSelf(ItemAlign.Start).decoration({
        type: TextDecorationType.Underline,
        color: Color.Black,
        style: TextDecorationStyle.SOLID
      }).margin({ top: 20, bottom: 20 })
      
      AtomicServiceSearch({
        operation: {
          // Auxiliary item of the Search component.
          auxiliaryItem: {
            value: $r("app.media.sweep"), // Custom resource
            action: () => {
              this.alert('Scan'); // Custom event
            }
          },
          // Independent item of the Search component.
          independentItem: {
            value: $r("app.media.dingding"), // Custom resource
            action: () => {
              this.alert('Notifications'); // Custom event
            }
          }
        }
      })
    }.padding({ left: 16, right: 16 })
  }

  private alert(message: string): void {
    this.getUIContext().showAlertDialog({ message: message });
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/XRYkdHZpTPebSkk3Yp94CA/en-us_image_0000002537925884.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062248Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8BA0FAFC181F0C077ED67B261A12960C18DB14CDD886A9424134F74FEE46E493)

## Example 3: Adding a Selection Area and Function Item to AtomicServiceSearch

This example demonstrates how to add the selection area and function items on the left and right to the AtomicServiceSearch component.

import { AtomicServiceSearch } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  build() {
    Column({ space: 6 }) {
      Text('AtomicServiceSearch + selection area + function items').alignSelf(ItemAlign.Start).decoration({
        type: TextDecorationType.Underline,
        color: Color.Black,
        style: TextDecorationStyle.SOLID
      }).margin({ top: 20, bottom: 20 })

      AtomicServiceSearch({
        select: {
          options: \[
            { value: 'Select1', icon: $r("app.media.sweep") }, // Custom resource
            { value: 'Select2', icon: $r("app.media.sweep") }, // Custom resource
            { value: 'Select3', icon: $r("app.media.sweep") }, // Custom resource
            { value: 'Select4', icon: $r("app.media.sweep") } // Custom resource
          \],
          selected: -1,
          selectValue: 'Select1',
          onSelect: (index: number, selectValue:string) => {
            if (index === 0) {
              this.alert(\`index: ${index}, selectValue: ${selectValue}\`);
            } else if (index === 1) {
              this.alert(\`index: ${index}, selectValue: ${selectValue}\`);
            } else if (index === 2) {
              this.alert(\`index: ${index}, selectValue: ${selectValue}\`);
            } else if (index === 3) {
              this.alert(\`index: ${index}, selectValue: ${selectValue}\`);
            }
          },
        },
        operation: {
          auxiliaryItem: {
            value: $r("app.media.sweep"), // Custom resource
            action: () => {
              this.alert('Scan'); // Custom event
            }
          },
          independentItem: {
            value: $r("app.media.dingding"), // Custom resource
            action: () => {
              this.alert('Notifications'); // Custom event
            }
          }
        }
      })
    }.padding({ left: 16, right: 16 })
  }

  private alert(message: string): void {
    this.getUIContext().showAlertDialog({ message: message });
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/0EFKGU-5RhCPhnC6W-p8dA/en-us_image_0000002568685661.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062248Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C153A3E957C62937E34CA1142B961255F0DB613232809A311E55B03230E6E15E)

## Example 4: Binding the Search Callback Events to AtomicServiceSearch

This example demonstrates how to use the **onWillInsert**, **onDidInsert**, **onWillDelete**, and **onDidDelete** APIs to implement insert and delete operations.

The **onSubmit** API is used to submit content in the search area.

The **onChange** API is used to listen for the content changes in the search area.

import { AtomicServiceSearch } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State insertValue: string = "";
  @State deleteValue: string = "";
  @State insertOffset: number = 0;
  @State deleteOffset: number = 0;
  @State deleteDirection: number = 0;
  @State startIndex: number = 0;
  @State endIndex: number = 0;
  @State offsetX: number = 0;
  @State offsetY: number = 0;
  @State changeValue: string = '';
  @State value: string = 'false';
  @State submitValue: string = '';
  @State text: string = 'Search editMenuOptions';

  build() {
    Column({ space: 6 }) {
      Text('Binding events to AtomicServiceSearch').alignSelf(ItemAlign.Start).decoration({
        type: TextDecorationType.Underline,
        color: Color.Black,
        style: TextDecorationStyle.SOLID
      }).margin({ top: 20, bottom: 20 })

      Column({ space: 6 }) {
        Text('editing: ' + this.value).width('100%').height(25).borderRadius(15).padding({ left: 15 })
          .backgroundColor('rgba(0, 0, 0, 0.1)').maxLines(1).textOverflow({ overflow: TextOverflow.MARQUEE });
        Text('onSubmit:' + this.submitValue).width('100%').height(25).borderRadius(15).padding({ left: 15 })
          .backgroundColor('rgba(0, 0, 0, 0.1)').maxLines(1).textOverflow({ overflow: TextOverflow.MARQUEE });
        Text('onChange:' + this.changeValue).width('100%').height(25).borderRadius(15).padding({ left: 15 })
          .backgroundColor('rgba(0, 0, 0, 0.1)').maxLines(1).textOverflow({ overflow: TextOverflow.MARQUEE });
        Text('offset x:' + this.offsetX + ' y:' + this.offsetY).width('100%').height(25).borderRadius(15).padding({ left: 15 })
          .backgroundColor('rgba(0, 0, 0, 0.1)').maxLines(1).textOverflow({ overflow: TextOverflow.MARQUEE });
        Text("insertValue:" + this.insertValue + "  insertOffset:" + this.insertOffset).width('100%').height(25)
          .borderRadius(15).padding({ left: 15 }).backgroundColor('rgba(0, 0, 0, 0.1)').maxLines(1)
          .textOverflow({ overflow: TextOverflow.MARQUEE });
        Text("deleteValue:" + this.deleteValue + "  deleteOffset:" + this.deleteOffset).width('100%').height(25)
          .borderRadius(15).padding({ left: 15 }).backgroundColor('rgba(0, 0, 0, 0.1)').maxLines(1)
          .textOverflow({ overflow: TextOverflow.MARQUEE });
        Text("deleteDirection:" + (this.deleteDirection == 0 ? "BACKWARD" : "FORWARD")).width('100%').height(25)
          .borderRadius(15).padding({ left: 15 }).backgroundColor('rgba(0, 0, 0, 0.1)').maxLines(1)
          .textOverflow({ overflow: TextOverflow.MARQUEE });
        AtomicServiceSearch({
          select: {
            options: \[
              { value: 'Select1', icon: $r("app.media.sweep") },
              { value: 'Select2', icon: $r("app.media.sweep") },
              { value: 'Select3', icon: $r("app.media.sweep") },
              { value: 'Select4', icon: $r("app.media.sweep") }
            \],
            selected: -1,
            selectValue: 'Select1',
            onSelect: (index: number) => {
              if (index === 0) {
                this.alert('Select1');
              } else if (index === 1) {
                this.alert('Select2');
              } else if (index === 2) {
                this.alert('Select3');
              } else if (index === 3) {
                this.alert('Select4');
              }
            },
          },
          search: {
            onSubmit: (value: string) => {
              this.submitValue = value
            },
            onChange: (value: string) => {
              this.changeValue = value
            },
            onCopy: () => {
              this.alert('onCopy');
            },
            onCut: () => {
              this.alert('onCut');
            },
            onPaste: () => {
              this.alert('onPaste');
            },
            onTextSelectionChange: (selectionStart: number, selectionEnd: number) => {
              this.startIndex = selectionStart
              this.endIndex = selectionEnd
            },
            onContentScroll: (totalOffsetX: number, totalOffsetY: number) => {
              this.offsetX = totalOffsetX
              this.offsetY = totalOffsetY
            },
            onEditChange: (data: boolean) => {
              this.value = data ? 'true' : 'false'
            },
            onWillInsert: (info: InsertValue) => {
              this.insertValue = info.insertValue
              return true;
            },
            onDidInsert: (info: InsertValue) => {
              this.insertOffset = info.insertOffset
            },
            onWillDelete: (info: DeleteValue) => {
              this.deleteValue = info.deleteValue
              info.direction
              return true;
            },
            onDidDelete: (info: DeleteValue) => {
              this.deleteOffset = info.deleteOffset
              this.deleteDirection = info.direction
            }
          }
        })
      }
    }.padding({ left: 16, right: 16 })
  }

  private alert(message: string): void {
    this.getUIContext().showAlertDialog({ message: message });
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/WzLryEomSiuy2gdS6SUCQg/en-us_image_0000002568765671.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062248Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=133788B5EAE31BCFAE15FD4AFFF3B3CAD1116318A9C391C14D331B5692614E49)

## Example 5: Customizing the Style of AtomicServiceSearch

This example demonstrates how to use the **search**, **select**, **value**, and **placeholder** parameters to customize the style of the **AtomicServiceSearch** component.

import { AtomicServiceSearch, SearchParams, SelectParams } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State private placeholder: string = 'Type to Search...';
  @State private defaultValue: string = 'default';
  @State private search?: SearchParams = {};
  @State private select?: SelectParams = {
    options: \[
      { value: 'Select1', icon: $r("app.media.sweep") },
      { value: 'Select2', icon: $r("app.media.sweep") },
      { value: 'Select3', icon: $r("app.media.sweep") },
      { value: 'Select4', icon: $r("app.media.sweep") }
    \],
    selected: -1,
    selectValue: 'Select1',
    onSelect: (index: number) => {
      if (index === 0) {
        this.alert('Select1');
      } else if (index === 1) {
        this.alert('Select2');
      } else if (index === 2) {
        this.alert('Select3');
      } else if (index === 3) {
        this.alert('Select4');
      }
    }
  };

  build() {
    Column({ space: 8 }) {
      Text('Customizing styles').alignSelf(ItemAlign.Start).decoration({
        type: TextDecorationType.Underline,
        color: Color.Black,
        style: TextDecorationStyle.SOLID
      }).margin({ top: 20, bottom: 20 })

      AtomicServiceSearch({
        value: this.defaultValue,
        placeholder: this.placeholder,
        select: this.select,
        search: this.search,
        operation: {
          independentItem: {
            value: $r(\`app.media.dingding\`),
            action: () => {
              this.alert('Notification');
            }
          }
        }
      })
      Button("Change placeholder")
        .width('100%')
        .type(ButtonType.Normal)
        .borderRadius(20)
        .onClick(() => {
          if (this.placeholder === 'Search...') {
            this.placeholder = 'Type to Search...';
          } else {
            this.placeholder = 'Search...';
          }
        });
      Button("Change defaultValue")
        .width('100%')
        .type(ButtonType.Normal)
        .borderRadius(20)
        .onClick(() => {
          if (this.defaultValue === 'value') {
            this.defaultValue = 'defaultValue';
          } else {
            this.defaultValue = 'value';
          }
        });
      Button("Change selection area style")
        .width('100%')
        .type(ButtonType.Normal)
        .borderRadius(20)
        .onClick(() => {
          this.select = {
            options: \[
              { value: 'Option 1', icon: $r("app.media.dingding") },
              { value: 'Option 2', icon: $r("app.media.dingding") },
            \],
            selected: -1,
            selectValue: 'Option 1',
            onSelect: (index: number) => {
              if (index === 0) {
                this.alert('Option 1');
              } else if (index === 1) {
                this.alert('Option 2');
              }
            }
          };
        });

      Button("Change Search Area Style")
        .width('100%')
        .type(ButtonType.Normal)
        .borderRadius(20)
        .onClick(() => {
          this.search = {
            componentBackgroundColor: '#e0eee8'
          }
        });
    }.padding({ left: 16, right: 16 })
  }

  private alert(message: string): void {
    this.getUIContext().showAlertDialog({ message: message });
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/PktqoNXHS8i0fHvwjrsxaA/en-us_image_0000002537765946.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062248Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A929CDA4B86EEEE30A29331BDF20744C6BC0BC71CACC7034DFA1CC6BED786602)

## Example 6: Setting the Caret Position Using controller

This example demonstrates how to use the **controller** parameter to set the caret position, select the content in the specified area, and disable the editing state.

import { AtomicServiceSearch } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  controller: SearchController = new SearchController();

  build() {
    Column({ space : 10 }) {
      Text('Setting the caret position using controller').alignSelf(ItemAlign.Start).decoration({
        type: TextDecorationType.Underline,
        color: Color.Black,
        style: TextDecorationStyle.SOLID
      }).margin({ top: 20, bottom: 20 })

      AtomicServiceSearch(
        {
          value: 'Default Value',
          placeholder: 'Type to Search...',
          controller: this.controller,
          search: {
            searchButton: {
              searchButtonValue: 'SEARCH',
              options: { fontSize: '12fp', fontColor: '#ff0e1216' }
            }
          }
        },
      );
      Button('caretPosition to 1').onClick(() => {
        this.controller.caretPosition(1);
      }).width('100%')
      Button('stopEditing').onClick(() => {
        this.controller.stopEditing();
      }).width('100%')
      Button('Selection \[0,3\]').onClick(() => {
        this.controller.setTextSelection(0, 3)
      }).width('100%')
    }.padding({ left: 16, right: 16 })
  }

  public alert(message: string): void {
    this.getUIContext().showAlertDialog({ message: message });
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/YvXUs2ioSrOxDvI-7Dht0Q/en-us_image_0000002537925886.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062248Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=864FA96D20F07D080618554227546730A6328DB5741388DDB596AC8037F9F825)

## Example 7: Setting the Enter Key Type

This example demonstrates how to use the **enterKeyType** attribute to dynamically change the effect of the Enter key on the soft keyboard.

import { AtomicServiceSearch } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State enterTypes: Array<EnterKeyType> = \[EnterKeyType.Go, EnterKeyType.Search, EnterKeyType.Send, EnterKeyType.Done, EnterKeyType.Next, EnterKeyType.PREVIOUS, EnterKeyType.NEW\_LINE\]
  @State index: number = 0

  build() {
    Column({ space : 10 }) {
      Text('Enter key type as search').alignSelf(ItemAlign.Start).decoration({
        type: TextDecorationType.Underline,
        color: Color.Black,
        style: TextDecorationStyle.SOLID
      }).margin({ top: 20, bottom: 20 })

      AtomicServiceSearch({
        placeholder: 'Enter key type as search',
        search: {
          enterKeyType: this.enterTypes\[this.index\]
        }
      })

      Button('Change EnterKeyType').onClick(() => {
        this.index = (this.index + 1) % this.enterTypes.length;
      }).width('100%')

    }.padding({ left: 16, right: 16 })
  }

  public alert(message: string): void {
    this.getUIContext().showAlertDialog({ message: message });
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/_DERbk--QcKA5kYOddMVYQ/en-us_image_0000002568685663.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062248Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=730AE22F11F61B0F99E8515BC8E7BCB2D81749A7C555397CFE53B74F62569980)

## Example 8: Setting Text Feature Effects

This example demonstrates how to use the **fontFeature** attribute to display text with various typographic features.

​​​​import { AtomicServiceSearch } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  build() {
    Column({ space : 10 }) {
      Text('Setting text feature effects').alignSelf(ItemAlign.Start).decoration({
        type: TextDecorationType.Underline,
        color: Color.Black,
        style: TextDecorationStyle.SOLID
      }).margin({ top: 20, bottom: 20 })

      AtomicServiceSearch({
        value: 'This is ss01 on : 0123456789',
        search: {
          fontFeature: "\\"ss01\\" on"
        }
      });

      AtomicServiceSearch({
        value: 'This is ss01 off : 0123456789',
        search: {
          fontFeature: "\\"ss01\\" off"
        }
      });

      AtomicServiceSearch({
        value: 'fiabc1234567DEFGHIJKLMN',
        search: {
          fontFeature: "\\"frac\\" on"
        }
      });

      AtomicServiceSearch({
        value: 'fiabc1234567DEFGHIJKLMN',
        search: {
          fontFeature: "\\"frac\\" off"
        }
      });
    }.padding({ left: 16, right: 16 })
  }

  public alert(message: string): void {
    this.getUIContext().showAlertDialog({ message: message });
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/CQf2pSCSSfyVAynJWiS9Mw/en-us_image_0000002568765673.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062248Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=369DC8CC0D6B03A157E7883AFBE467B6DAA53630A2704549827373EBBD4086D7)

## Example 9: Setting Text Auto-Adaptation

This example demonstrates how to use the **minFontSize** and **maxFontSize** attributes to implement the text auto-adaptation features.

import { AtomicServiceSearch } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  build() {
    Column({ space : 10 }) {
      Text('Setting text auto-adaptation').alignSelf(ItemAlign.Start).decoration({
        type: TextDecorationType.Underline,
        color: Color.Black,
        style: TextDecorationStyle.SOLID
      }).margin({ top: 20, bottom: 20 })

      AtomicServiceSearch({
        value: 'This is the text without the adaptive font',
      }).width('80%').height(40).borderWidth(1).borderRadius(20)

      AtomicServiceSearch({
        value: 'This is the text without the adaptive font',
        search: {
          minFontSize: 4,
          maxFontSize: 40
        }
      }).width('80%').height(40).borderWidth(1).borderRadius(20)
    }.padding({ left: 16, right: 16 })
  }

  public alert(message: string): void {
    this.getUIContext().showAlertDialog({ message: message });
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/ULnYBKqlRDK9SgdW9AWVnw/en-us_image_0000002537765948.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062248Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C9058D452D4668E469F5241CF68DBC73AA45559AC539D9C97D855A9E6E08E8B7)

## Example 10: Setting Custom Menu Extensions

This example demonstrates how to use the **editMenuOptions** API to create custom menu extensions for text settings. It includes customizing text content, icons, and callbacks for these extensions.

import { AtomicServiceSearch, TextMenuController } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  aboutToAppear(): void {
    TextMenuController.disableMenuItems(\[TextMenuItemId.AI\_WRITER\])
  }

  onCreateMenu = (menuItems: Array<TextMenuItem>) => {
    let item1: TextMenuItem = {
      content: 'custom1',
      icon: $r('app.media.startIcon'),
      id: TextMenuItemId.of('custom1'),
    }
    let item2: TextMenuItem = {
      content: 'custom2',
      id: TextMenuItemId.of('custom2'),
      icon: $r('app.media.startIcon'),
    }
    menuItems.push(item1)
    menuItems.unshift(item2)
    return menuItems
  }
  onMenuItemClick = (menuItem: TextMenuItem, textRange: TextRange) => {
    if (menuItem.id.equals(TextMenuItemId.of('custom2'))) {
      console.info('Intercept id: custom2 start:' + textRange.start + '; end:' + textRange.end)
      return true
    }
    if (menuItem.id.equals(TextMenuItemId.COPY)) {
      console.info('Intercept COPY start:' + textRange.start + '; end:' + textRange.end)
      return true
    }
    if (menuItem.id.equals(TextMenuItemId.SELECT\_ALL)) {
      console.info('Do not intercept SELECT\_ALL start:' + textRange.start + '; end:' + textRange.end)
      return false
    }
    return false
  }
  @State editMenuOptions: EditMenuOptions = {
    onCreateMenu: this.onCreateMenu, onMenuItemClick: this.onMenuItemClick
  }

  build() {
    Column({ space: 10 }) {
      Text('Setting custom menu extensions').alignSelf(ItemAlign.Start).decoration({
        type: TextDecorationType.Underline,
        color: Color.Black,
        style: TextDecorationStyle.SOLID
      }).margin({ top: 20, bottom: 20 })

      AtomicServiceSearch({
        value: 'Default input',
        search: {
          editMenuOptions: this.editMenuOptions
        }
      })
    }.padding({ left: 16, right: 16 })
  }

  public alert(message: string): void {
    this.getUIContext().showAlertDialog({ message: message });
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/jijXrj1QRr2GNrafP3-mGQ/en-us_image_0000002537925888.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062248Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0032036C1325E58A32C5AEC76428F06A75F6E1142924272EBFBEA2E7F3A7D4DD)

## Example 11: Setting the Horizontal Alignment, Caret Style, and Background Color of the Selected Text

This example shows how to set the horizontal alignment, caret style, and background color of the selected text using **textAlign**, **caretStyle**, and **selectedBackgroundColor**.

import { AtomicServiceSearch, TextMenuController } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  aboutToAppear(): void {
    TextMenuController.disableMenuItems(\[TextMenuItemId.AI\_WRITER\])
  }

  build() {
    Column() {
      Text('Setting horizontal alignment/caret style/background color of selected text').alignSelf(ItemAlign.Start).decoration({
        type: TextDecorationType.Underline,
        color: Color.Black,
        style: TextDecorationStyle.SOLID
      }).margin({ top: 20, bottom: 20 })

      AtomicServiceSearch({
        value: 'Search textAlign sample',
        search: {
          textAlign: TextAlign.Center,
          caretStyle: { width: 3, color: Color.Green },
          selectedBackgroundColor: Color.Gray
        }
      })
    }.padding({ left: 16, right: 16 })
  }

  public alert(message: string): void {
    this.getUIContext().showAlertDialog({ message: message });
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/09/v3/MpJJP9tDQQKpNgc4NplLkg/en-us_image_0000002568685665.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062248Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D9BD5843208F4A01E237DCF05915B115F8DB2034A23CB24AB2D83FC1AC34E42B)

## Example 12: Setting Input Filtering

This example shows how to set input filtering using **inputFilter**.

import { AtomicServiceSearch } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State filterValue: string = '';

  build() {
    Column() {
      Column({ space: 10 }) {
        Text('Setting input filtering').alignSelf(ItemAlign.Start).decoration({
          type: TextDecorationType.Underline,
          color: Color.Black,
          style: TextDecorationStyle.SOLID
        }).margin({ top: 20, bottom: 20 })
        AtomicServiceSearch({
          placeholder: 'please enter...',
          search: {
            inputFilter: {
              inputFilterValue : '\[a-z\]',
              error: (filterValue: string) => {this.filterValue = filterValue}
            }
          }
        })
        Text('Filter:' + this.filterValue).alignSelf(ItemAlign.Start)

      }
    }.padding({ left: 16, right: 16 })
  }

  public alert(message: string): void {
    this.getUIContext().showAlertDialog({ message: message });
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/8disqYsJREeOuzdLfqjp1Q/en-us_image_0000002568765675.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062248Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1E66AEF67BB7D8581411541EEE2B8E48164D6E9DD0C91415EAD7F8DB225AB07C)
