# TextArea

The **TextArea** component provides multi-line text input and automatically wraps text to ensure that no line extends beyond the component's width.

If the component does not have its height set, it adapts its height to the content. If the component does not have its width set, it stretches to fill the maximum available width.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/RJb6XuaLQz6NH9Dmz5xZIA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=55A08A1B29513977A1E28297AE6233510ED24D0A5CE6D4E260615D56BC51069B)

This component is supported since API version 7. Updates will be marked with a superscript to indicate their earliest API version.

#### Child Components

Not supported

#### APIs

TextArea(value?: TextAreaOptions)

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [TextAreaOptions](#textareaoptions) | No | Parameters of the **TextArea** component. |

#### TextAreaOptions

Describes the initialization options of the **TextArea** component.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| placeholder | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 
Text displayed when there is no input.

When only the **placeholder** attribute is set, the text selection handle is still available; the caret stays at the beginning of the placeholder text when the handle is released.

 |
| text | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 

Current text input.

You are advised to bind the state variable to the text in real time through the **onChange** event, so as to prevent display errors when the component is updated.

Since API version 10, this parameter supports two-way binding through [$$](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-two-way-sync).

Since API version 18, this parameter supports two-way binding through [!!](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-new-binding#two-way-binding-between-built-in-component-parameters).

 |
| controller8+ | [TextAreaController](#textareacontroller8) | No | Yes | Text area controller. |

#### Attributes

In addition to the [universal attributes](../../universal-attributes/document.md), the following attributes are supported.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/i0nPg9uNSReFjMCkr6Y00Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5627A2E3A7BAF21B9FB12F6895091147B4D21168533D48E4CAB119EC570741E8)

The default value of the universal attribute [padding](../../universal-attributes/layout-and-borders/sizing/document.md#padding) is as follows:

{

top: '8vp',

right: '16vp',

bottom: '8vp',

left: '16vp'

}

Since API version 11, **.width('auto')** can be set for the **TextArea** component. Under this setting, the component auto-adapts its width to the text width, while respecting the **constraintSize** configuration and the maximum and minimum width restrictions received by the parent container. For details, see [Size](../../universal-attributes/layout-and-borders/sizing/document.md).

#### \[h2\]placeholderColor

placeholderColor(value: ResourceColor)

Sets the placeholder text color.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | Yes | 
Placeholder text color.

The default value follows the theme.

 |

#### \[h2\]placeholderFont

placeholderFont(value: Font)

Placeholder text style, including the font size, font weight, font family, and font style.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/fJeDDkBmSImL4_m1sy4HTQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0F33F5CDCB5D336B525078E9193DEC2F37D7014A071215840E54292713C466D0)

You can use [loadFontSync](../../../../../graphics/arkgraphics-2d/arkts-apis/ohos-graphics-text-text/document.md#loadfontsync) to register custom fonts.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [Font](../../common-definitions/basic-types/document.md#font) | Yes | Placeholder text style. |

#### \[h2\]textAlign

textAlign(value: TextAlign)

Sets the horizontal alignment of the text.

Available options are **TextAlign.Start**, **TextAlign.Center**, and **TextAlign.End**. **TextAlign.JUSTIFY** is available since API version 11.

The vertical position of the text paragraph can be controlled by the [align](../../universal-attributes/layout-and-borders/location/document.md#align) attribute, but the horizontal position cannot be controlled by **align** in this component.

-   **Alignment.TopStart**, **Alignment.Top**, **Alignment.TopEnd**: Content aligns to the top.
    
-   **Alignment.Start**, **Alignment.Center**, **Alignment.End**: Content is centered vertically.
    
-   **Alignment.BottomStart**, **Alignment.Bottom**, **Alignment.BottomEnd:** Content aligns to the bottom.
    

When **textAlign** is set to **TextAlign.JUSTIFY**, the text in the last line is horizontally aligned with the start edge.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [TextAlign](../../common-definitions/enums/document.md#textalign) | Yes | 
Horizontal alignment of the text.

Default value: **TextAlign.Start**

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/RihUISE8QBCc2nLn45VrGw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4CD265CB31DF1AB25572D63DEA64B384C09D88B6BDDFAC83FA9E1A34CF6898E4)

**textAlign** only adjusts the overall text layout and does not affect character display order. For character display order adjustment, see [Bidirectional Text Layout and Alignment](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-internationalization#bidirectional-text-layout-and-alignment).

#### \[h2\]caretColor

caretColor(value: ResourceColor)

Sets the color of the caret in the text box.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | Yes | 
Color of the caret in the text box.

Default value: **'#007DFF'**

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/BaCQ-6IwTq-qLgsKqAr8tQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EE81BFD122BA7E66B8D45F100F7669E58664F670BACA4CAC56EC3549C22368A7)

Since API version 12, this API can be used to set the text handle color, which is the same as the caret color.

#### \[h2\]fontColor

fontColor(value: ResourceColor)

Sets the font color.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | Yes | Font color. |

#### \[h2\]fontSize

fontSize(value: Length)

Sets the text size.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [Length](../../common-definitions/basic-types/document.md#length) | Yes | Font size. If **fontSize** is of the number type, the unit fp is used. The default font size is 16 fp on non-wearable devices and 18 fp on wearable devices. This parameter cannot be set in percentage. |

#### \[h2\]fontStyle

fontStyle(value: FontStyle)

Sets the font style.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [FontStyle](../../common-definitions/enums/document.md#fontstyle) | Yes | 
Font style.

Default value: **FontStyle.Normal**

 |

#### \[h2\]fontWeight

fontWeight(value: number | FontWeight | ResourceStr)

Sets the font weight. If the value is too large, the text may be clipped depending on the font.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | [FontWeight](../../common-definitions/enums/document.md#fontweight) | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | Yes | 
Font weight. For the number type, the value range is \[100, 900\], at an interval of 100. The default value is **400**. A larger value indicates a heavier font weight. For the string type, only strings that represent a number, for example, **"400"**, and the following enumerated values of **FontWeight** are supported: **"bold"**, **"bolder"**, **"lighter"**, **"regular"**, and **"medium"**.

Default value: **FontWeight.Normal**

The Resource type is supported since API version 20.

 |

#### \[h2\]fontFamily

fontFamily(value: ResourceStr)

Sets the font family.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | Yes | 
Font family. Default font: **'HarmonyOS Sans'**

To specify multiple fonts, separate them with commas (,), and fonts are applied in priority order. Example: **'Arial, HarmonyOS Sans'**.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/ur_n90Y2TvOQ2zGIPMBXEQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=ED8B5EA4B2EE23425393CCBE08826207B48623775AEF02FD7628F97C5EA11524)

You are advised to use [loadFontSync](../../../../../graphics/arkgraphics-2d/arkts-apis/ohos-graphics-text-text/document.md#loadfontsync) to register custom fonts.

#### \[h2\]inputFilter8+

inputFilter(value: ResourceStr, error?: (value: string) => void)

Sets the regular expression for input filtering. Only inputs that comply with the regular expression can be displayed. Other inputs are filtered out.

For single-character input scenarios, only single-character matching is supported; for multi-character input scenarios (such as pasting), string matching is supported.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | Yes | Regular expression. |
| error | (value: string) => void | No | Filtered-out content to return when regular expression matching fails. No return when regular expression matching succeeds. |

#### \[h2\]copyOption9+

copyOption(value: CopyOptions)

Sets whether the input text can be copied. If this attribute is set to **CopyOptions.None**, only paste and select all operations are supported.

If this attribute is set to **CopyOptions.None**, drag and drop operations are not supported.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [CopyOptions](../../common-definitions/enums/document.md#copyoptions9) | Yes | 
Whether the input text can be copied.

Default value: **CopyOptions.LocalDevice**

 |

#### \[h2\]maxLength10+

maxLength(value: number)

Sets the maximum number of characters for text input. By default, there is no maximum number of characters. When the maximum number is reached, no more characters can be entered, and the border turns red.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | Yes | 
Maximum number of characters for text input.

Values less than 0 are treated as the default value, meaning no limit is set.

Default value: **uint32\_max** (i.e., 2^32-1)

 |

#### \[h2\]showCounter10+

showCounter(value: boolean, options?: InputCounterOptions)

Sets the character counter displayed when the number of characters entered exceeds the threshold. If the **showCounter** API is not called, the character counter is not displayed by default.

**options** can be set only when **value** is set to **true**, in which case a character counter is displayed below the text box. This attribute must be used together with **maxLength**. The character counter is displayed in this format: Number of characters entered/Character limit.

It is visible when the number of characters entered is greater than the character limit multiplied by the threshold percentage value. If **options** is not set, the text box border and character counter subscript turn red when the number of characters entered reaches the limit. If **value** is set to **true** and **options** is set, the text box border and character counter subscript turn red and the text box shakes when the number of characters entered reaches the limit, provided that the value of **thresholdPercentage** is valid. If **highlightBorder** is set to **false**, the text box border does not turn red. By default, **highlightBorder** is set to **true**. The character counter is not displayed for text boxes in inline input style.

[Example 2: Implementing a Counter](#example-2-implementing-a-counter) shows the effect of setting **showCounter**.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | boolean | Yes | 
Whether to display the character counter.

**true**: Character counter is displayed. **false**: Character counter is not displayed.

 |
| options11+ | [InputCounterOptions](../text-box-component-common-apis/document.md#inputcounteroptions11) | No | Configuration options for the character counter. |

#### \[h2\]style10+

style(value: TextContentStyle)

Sets the polymorphic style of the text box. The inline input style is only available for the **TextAreaType.NORMAL** type.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [TextContentStyle](../../common-definitions/enums/document.md#textcontentstyle10) | Yes | 
Polymorphic style of the text box.

Default value: **TextContentStyle.DEFAULT**

 |

#### \[h2\]enableKeyboardOnFocus10+

enableKeyboardOnFocus(value: boolean)

Sets whether to pop up the soft keyboard when the **TextArea** component obtains focus in a way other than clicking.

Since API version 10, the **TextArea** component is bound to the input method by default when it obtains focus.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | boolean | Yes | 
Whether to pop up the soft keyboard when the **TextArea** component obtains focus in a way other than clicking.

**true**: The soft keyboard pops up. **false**: The soft keyboard does not pop up.

Default value: **true**

 |

#### \[h2\]selectionMenuHidden10+

selectionMenuHidden(value: boolean)

Sets whether to hide the system text selection menu.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | boolean | Yes | 
Whether to hide the system text selection menu.

**true**: The system text selection menu is hidden when a user clicks the text box caret, long-presses the text box, double-taps the text box, triple-taps the text box, or right-clicks the text box.

**false**: The system text selection menu appears.

Default value: **false**

 |

#### \[h2\]barState10+

barState(value: BarState)

Sets the scrollbar display mode.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [BarState](../../common-definitions/enums/document.md#barstate) | Yes | 
Scrollbar display mode.

Default value: **BarState.Auto**

 |

#### \[h2\]maxLines10+

maxLines(value: number)

Sets the maximum number of lines that can be displayed. When **textOverflow** is set, text is truncated if the content exceeds this limit. When **textOverflow** is not set, in inline style, the text is scrollable if the content exceeds the limit while the text box is focused; **maxLines** does not apply when the text box is not focused. In non-inline style, the text is truncated according to the number of lines.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | Yes | 
Maximum number of lines that can be displayed with the inline style in the editing state.

Default value: **3**. In non-inline style, the default value is **UINT32\_MAX**.

Value range: (0, UINT32\_MAX\]

 |

#### \[h2\]maxLines20+

maxLines(lines: number, options: MaxLinesOptions)

Sets the maximum number of visible lines when used with [textOverflow](#textoverflow12). Excess content can be truncated or made scrollable based on configuration. Without **textOverflow**:

\- With focus in inline mode: Text exceeding the **maxLines** limit becomes scrollable.

\- Without focus in inline mode: **maxLines** has no effect.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| lines | number | Yes | 
Maximum number of lines that can be displayed with the inline style in the editing state.

Default value: **3** with the inline style; **+∞** with the non-inline style, indicating that there is no maximum number of lines

Value range: (0, +∞)

 |
| options | [MaxLinesOptions](../text-component-common-apis/document.md#maxlinesoptions20) | Yes | 

Display effect for overflow text.

Default value: **MaxLinesMode.CLIP**.

 |

#### \[h2\]minLines20+

minLines(lines: Optional<number>)

Sets the minimum number of lines displayed for the component. When [constraintSize](../../universal-attributes/layout-and-borders/sizing/document.md#constraintsize) is set, the component's final height respects the defined constraints.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| lines | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<number> | Yes | 
Minimum number of lines.

Default value: **1**

Value range: \[1, INT32\_MAX\]

Values less than 1 are treated as the default value.

 |

#### \[h2\]customKeyboard10+

customKeyboard(value: CustomBuilder | ComponentContent | undefined, options?: KeyboardOptions)

Sets the custom keyboard.

When a custom keyboard is set, activating the text box opens the specified custom component, instead of the system input method.

The height of the custom keyboard can be set using the **height** property of the custom component's root node, while the width uses the system default value.

The custom keyboard is presented by overlaying the original screen, which is not compressed or lifted if avoid mode is not enabled or avoidance is not needed for the text box.

The custom keyboard cannot obtain the focus, but it blocks gesture events.

By default, the custom keyboard is closed when the input component loses the focus. You can also use the [TextAreaController](#textareacontroller8).[stopEditing](#stopediting10) API to close the keyboard.

When setting a custom keyboard, you can bind the [onKeyPrelme](../../universal-events/basic-input-events/key-event/document.md#onkeypreime12) event to prevent input from the physical keyboard.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/M7sHyW5hROSIAvrmx25XOA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E3C185EF7C79944B71F0C03D48C4AF5536D8596B7BB9B18B1F046D0D6EAEB161)

This API cannot be called within [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier).

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [CustomBuilder](../../common-definitions/basic-types/document.md#custombuilder8) | [ComponentContent](../../../arkts-api/ui/arkui/componentcontent/document.md#componentcontent-1)22+ | undefined22+ | Yes | Custom keyboard. If the value is **undefined**, the custom keyboard is closed. |
| options12+ | [KeyboardOptions](../richeditor/document.md#keyboardoptions12) | No | Whether to support keyboard avoidance. |

#### \[h2\]type11+

type(value: TextAreaType)

Sets the text box type.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [TextAreaType](#textareatype11) | Yes | 
Text box type.

Default value: **TextAreaType.NORMAL**.

 |

#### \[h2\]enterKeyType11+

enterKeyType(value: EnterKeyType)

Sets the type of the Enter key.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/o4rhwLF8SYGki4eaVtMoDQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BD4B965372DA4CB9B7CD36BFFD02B4EEA3F55DA1EA74F481E99DE880F7EC1BE3)

This API can be called within [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier) since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [EnterKeyType](../textinput/document.md#enterkeytype) | Yes | 
Type of the Enter key.

Default value: **EnterKeyType.NEW\_LINE**

 |

#### \[h2\]enableAutoFill12+

enableAutoFill(value: boolean)

Sets whether to enable autofill.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | boolean | Yes | 
Whether to enable autofill.

**true** to enable, **false** otherwise.

Default value: **true**

 |

#### \[h2\]enableSelectedDataDetector22+

enableSelectedDataDetector(enable: boolean | undefined)

Sets whether to enable entity recognition for selected text. This API only works on devices that provide text recognition.

When **enableSelectedDataDetector** is set to **true**, all entity types are recognized by default.

This feature is only effective when [CopyOptions](../../common-definitions/enums/document.md#copyoptions9) is set to **CopyOptions.LocalDevice** or **CopyOptions.CrossDevice**.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| enable | boolean | undefined | Yes | 
Whether to enable entity recognition for selected text.

**true**: Entity recognition is enabled. **false**: Entity recognition is disabled. Default value: **true**

 |

#### \[h2\]contentType12+

contentType(contentType: ContentType)

Sets the content type for autofill.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| contentType | [ContentType](../textinput/document.md#contenttype12) | Yes | Content type for autofill. |

#### \[h2\]lineHeight12+

lineHeight(value: number | string | Resource)

Text line height. If the value is less than or equal to 0, the line height is not limited and the font size is adaptive.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | string | [Resource](../../common-definitions/basic-types/document.md#resource) | Yes | 
Text line height. String type. Specifies the length [pixel unit](../../common-definitions/pixel-units/document.md) explicitly, for example, **'10px'**, or provides the length in percentage, for example, **'100%'**.

Note: If no pixel unit is specified, the default unit is fp, in which case **'10'** is equivalent to 10 fp.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/gjvPEOIiR5W9bLkxn8aucA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B9ECA1DC1B9D36E42ECFBBCD61DE3CFBBCCD9C346F44AF2ED70511B3068C3440)

If certain characters have significantly taller glyphs than others on the same line, layout anomalies such as clipping, overlap, or misalignment may occur. In this case, adjust component attributes such as height and line height to ensure proper layout rendering.

#### \[h2\]decoration12+

decoration(value: TextDecorationOptions)

Sets the color, type, and style of the text decorative line.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [TextDecorationOptions](../text-box-component-common-apis/document.md#textdecorationoptions12) | Yes | 
Text decorative line options.

Default value: {

type: TextDecorationType.None,

color: Color.Black,

style: TextDecorationStyle.SOLID

}

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/uRx4vFWUR52SlkOW9WtKuw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FBDD963AB8A170A3384EFB734E897AC184C1D4794D95A43A10D7DF2E4B27C501)

When the bottom contour of a character intersects with the decoration, underline avoidance is triggered, commonly affecting characters like "g", "j", "y", "q", and "p."

If the decoration color is set to **Color.Transparent**, it inherits the text color of the first character in each line. If the decoration color is set to **"#00FFFFFF"**, the line becomes fully transparent.

#### \[h2\]letterSpacing12+

letterSpacing(value: number | string | Resource)

Sets the letter spacing for a text style. Percentage values follow default display behavior. If the value specified is **0**, the default value is used. For the string type, numeric string values with optional units, for example, **"10"** or **"10fp"**, are supported.

If the value specified is a negative value, the text is compressed. A negative value too small may result in the text being compressed to 0 and no content being displayed.

This setting applies to every character, including those at line endings.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | string | [Resource](../../common-definitions/basic-types/document.md#resource) | Yes | 
Letter spacing.

Unit: [fp](../../common-definitions/pixel-units/document.md)

 |

#### \[h2\]fontFeature12+

fontFeature(value: string)

Sets the font feature, for example, monospaced digits.

Format: normal | <feature-tag-value>

Format of **<feature-tag-value>**: <string> \[ <integer> | on | off \]

There can be multiple **<feature-tag-value>** values, which are separated by commas (,).

For example, the input format for monospaced clock fonts is "ss01" on.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | string | Yes | Font feature. |

For details about the supported font features, see the [font feature list](../text/document.md#fontfeature12).

Font features are advanced typographic features, such as ligatures and monospace, for OpenType fonts. They are typically used in custom fonts and require the support of the font itself.

For more information about the font features, see [the font-feature-settings property](https://www.w3.org/TR/css-fonts-3/#font-feature-settings-prop) and [The Complete CSS Demo for OpenType Features](https://sparanoid.com/lab/opentype-features/).

#### \[h2\]wordBreak12+

wordBreak(value: WordBreak)

Sets the word break rule. This attribute does not take effect for the placeholder text.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [WordBreak](../../common-definitions/enums/document.md#wordbreak11) | Yes | 
Word break rule.

Default value: **WordBreak.BREAK\_WORD**

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/8-HqeWPmR_myW82nwxCUjQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=266FD613B6D5314D6AC5DCBC47932491E7EA6D27F73006F3652FE8888B87B693)

The component does not support the **clip** attribute. Therefore, setting this attribute does not affect text clipping.

#### \[h2\]selectedBackgroundColor12+

selectedBackgroundColor(value: ResourceColor)

Sets the background color of the selected text. If the opacity is not set, a 20% opacity will be used.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | Yes | Background color of the selected text. |

#### \[h2\]caretStyle12+

caretStyle(value: CaretStyle)

Sets the caret style.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [CaretStyle](../text-component-common-apis/document.md#caretstyle10) | Yes | Caret style. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/V0yxgoPpRK28gFURQelhwA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=82C8179F890EDA2112C4082AC3542D42E9A6F0300D175F57097583781E228FD6)

When both **caretColor** and the **color** parameter in **caretStyle** are configured, the last-set value takes precedence.

Since API version 12, this API can be used to set the text handle color, which is the same as the caret color.

#### \[h2\]textIndent12+

textIndent(value: Dimension)

Sets the indent of the first line text.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [Dimension](../../common-definitions/basic-types/document.md#dimension10) | Yes | 
Indent of the first line text.

Default value: **0**

 |

#### \[h2\]textOverflow12+

textOverflow(value: TextOverflow)

Sets the display mode when the text is too long.

In inline style, the effect of truncating text according to [maxLines](#maxlines10) only applies when **textOverflow** is set.

Text is clipped at the transition between words. To clip text in the middle of a word, set [wordBreak](../../common-definitions/enums/document.md#wordbreak11) to **WordBreak.BREAK\_ALL**.

If **textOverflow** is set to **TextOverflow.None**, **TextOverflow.Clip**, or **TextOverflow.Ellipsis**, this attribute must be used with [maxLines](#maxlines10) for the settings to take effect. **TextOverflow.None** produces the same effect as **TextOverflow.Clip**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/zQy610ikSJOj3m2xXu1F5A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9EEDE824C4528634C7816C28A684C870FBE1A9F73C6063EA191FA24982077147)

The **TextArea** component does not support the **TextOverflow.MARQUEE** mode. If this attribute is set to **TextOverflow.MARQUEE**, **TextOverflow.Clip** is used instead.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [TextOverflow](../../common-definitions/enums/document.md#textoverflow) | Yes | 
Display mode when the text is too long.

Default value: **TextOverflow.Clip**

 |

#### \[h2\]minFontSize12+

minFontSize(value: number | string | Resource)

Sets the minimum font size. For the string type, numeric string values with optional units, for example, **"10"** or **"10fp"**, are supported.

For the setting to take effect, this attribute must be used together with [maxFontSize](#maxfontsize12) and [maxLines](#maxlines10), or layout constraint settings.

When the adaptive font size is used, the **fontSize** settings do not take effect.

If the value of **minFontSize** is less than or equal to 0, the adaptive font sizing feature is disabled. In such cases, the [fontSize](#fontsize) attribute is used instead. If **fontSize** is not explicitly set, its default value will apply.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | string | [Resource](../../common-definitions/basic-types/document.md#resource) | Yes | 
Minimum font size.

Unit: [fp](../../common-definitions/pixel-units/document.md)

 |

#### \[h2\]maxFontSize12+

maxFontSize(value: number | string | Resource)

Sets the maximum font size. For the string type, numeric string values with optional units, for example, **"10"** or **"10fp"**, are supported.

For the setting to take effect, this attribute must be used together with [minFontSize](#minfontsize12) and [maxLines](#maxlines10), or layout constraint settings.

When the adaptive font size is used, the **fontSize** settings do not take effect.

If the value of **maxFontSize** is less than or equal to 0 or is less than the value of **minFontSize**, the adaptive font sizing feature is disabled. In such cases, the [fontSize](#fontsize) attribute is used instead. If **fontSize** is not explicitly set, its default value will apply.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | string | [Resource](../../common-definitions/basic-types/document.md#resource) | Yes | 
Maximum font size.

Unit: [fp](../../common-definitions/pixel-units/document.md)

 |

#### \[h2\]heightAdaptivePolicy12+

heightAdaptivePolicy(value: TextHeightAdaptivePolicy)

Sets how the adaptive height is determined for the text.

When this attribute is set to **TextHeightAdaptivePolicy.MAX\_LINES\_FIRST**, the [maxLines](#maxlines10) attribute takes precedence for adjusting the text height. If the **maxLines** setting results in a layout beyond the layout constraints, the text will shrink to a font size between [minFontSize](#minfontsize12) and [maxFontSize](#maxfontsize12) to allow for more content to be shown.

If the text box is in inline input style, the font size in the editing state is different from that in the non-editing state.

If this attribute is set to **TextHeightAdaptivePolicy.MIN\_FONT\_SIZE\_FIRST**, the **minFontSize** attribute takes precedence for adjusting the text height. If the text can fit in one line with the **minFontSize** setting, the text will enlarge to the largest possible font size between **minFontSize** and **maxFontSize**.

If this attribute is set to **TextHeightAdaptivePolicy.LAYOUT\_CONSTRAINT\_FIRST**, the layout constraints take precedence for adjusting the text height. If the resultant layout is beyond the layout constraints, the text will shrink to a font size between **minFontSize** and **maxFontSize** to respect the layout constraints.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [TextHeightAdaptivePolicy](../../common-definitions/enums/document.md#textheightadaptivepolicy10) | Yes | 
How the adaptive height is determined for the text.

Default value: **TextHeightAdaptivePolicy.MAX\_LINES\_FIRST**

 |

#### \[h2\]lineSpacing12+

lineSpacing(value: LengthMetrics)

Sets the line spacing of the text. If the value specified is less than or equal to 0, the default value **0** is used.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [LengthMetrics](../../../arkts-api/ui/arkui/graphics/document.md#lengthmetrics12) | Yes | Line spacing. Default value: **0** |

#### \[h2\]lineSpacing20+

lineSpacing(value: LengthMetrics, options?: LineSpacingOptions)

Sets the line spacing for text. When **LineSpacingOptions** is not specified, line spacing is applied above the first line and below the last line by default.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [LengthMetrics](../../../arkts-api/ui/arkui/graphics/document.md#lengthmetrics12) | Yes | Line spacing. Values less than or equal to 0 are treated as the default value **0**. |
| options | [LineSpacingOptions](../text-component-common-apis/document.md#linespacingoptions20) | No | 
Line spacing configuration options.

Default value: **{ onlyBetweenLines: false }**.

 |

#### \[h2\]lineBreakStrategy12+

lineBreakStrategy(strategy: LineBreakStrategy)

Sets the line break rule. This attribute takes effect only when [wordBreak](#wordbreak12) is not **WordBreak.BREAK\_ALL**. Hyphens are not supported.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| strategy | [LineBreakStrategy](../../common-definitions/enums/document.md#linebreakstrategy12) | Yes | 
Line break rule.

Default value: **LineBreakStrategy.GREEDY**

 |

#### \[h2\]editMenuOptions12+

editMenuOptions(editMenu: EditMenuOptions)

Sets the extended options of the custom context menu on selection, including the text content, icon, and callback.

When [disableMenuItems](../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-textmenucontroller/document.md#disablemenuitems20) or [disableSystemServiceMenuItems](../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-textmenucontroller/document.md#disablesystemservicemenuitems20) is used to disable system service menu items in the context menu on selection, the disabled menu options will be excluded from the parameter list in the [onCreateMenu](../text-component-common-apis/document.md#oncreatemenu12) callback of **editMenuOptions**.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| editMenu | [EditMenuOptions](../text-component-common-apis/document.md#editmenuoptions) | Yes | Extended options of the custom context menu on selection. |

#### \[h2\]enablePreviewText12+

enablePreviewText(enable: boolean)

Sets whether to enable preview text.

The preview content is defined as a temporary, uncommitted input state. Currently, the text interception function is not supported.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| enable | boolean | Yes | 
Whether to enable preview text.

**true**: Preview text is enabled. **false**: Preview text is disabled.

Default value: **true**

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/iftvDe_PQBy7AykJHF1jmw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=74E74E5F0FDEF3344373B640489821850160D0C0044A4875AA2A06BC9B92811A)

Preview text represents a temporary, uncommitted input state. This feature requires support from the input method with pre-commit text functionality enabled. During text entry, when candidate words have not been confirmed yet, the text box displays marked text in a provisional state. For example, when typing Chinese using Pinyin input, the Pinyin letters appear in the input box before selecting from the candidate word list. This intermediate state constitutes preview text.

#### \[h2\]enableHapticFeedback13+

enableHapticFeedback(isEnabled: boolean)

Specifies whether to enable haptic feedback.

To enable haptic feedback, you must declare the **ohos.permission.VIBRATE** permission under **requestPermissions** in the [module.json5](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/module-configuration-file) file of the project.

"requestPermissions": \[
 {
    "name": "ohos.permission.VIBRATE",
 }
\]

**Atomic service API**: This API can be used in atomic services since API version 13.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| isEnabled | boolean | Yes | 
Whether to enable haptic feedback.

**true** to enable, **false** otherwise.

Default value: **true**

 |

#### \[h2\]autoCapitalizationMode20+

autoCapitalizationMode(mode: AutoCapitalizationMode)

Sets the auto-capitalization text mode. This API provides the capability, but actual implementation depends on the input method application.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| mode | [AutoCapitalizationMode](../text-component-common-apis/document.md#autocapitalizationmode20) | Yes | Auto-capitalization mode. The default state is inactive. |

#### \[h2\]keyboardAppearance15+

keyboardAppearance(appearance: Optional<KeyboardAppearance>)

Sets the keyboard appearance for the text box.

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| appearance | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<[KeyboardAppearance](../text-component-common-apis/document.md#keyboardappearance15)\> | Yes | 
Appearance of the keyboard.

Default value: **KeyboardAppearance.NONE\_IMMERSIVE**

 |

#### \[h2\]strokeWidth20+

strokeWidth(width: Optional<LengthMetrics>)

Sets the text stroke width.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| width | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<[LengthMetrics](../../../arkts-api/ui/arkui/graphics/document.md#lengthmetrics12)\> | Yes | 
Text stroke width. When the unit of **LengthMetrics** is **px**:

Values < 0: solid text. Values > 0: outlined text.

Default value: **0** (no stroke)

 |

#### \[h2\]strokeColor20+

strokeColor(color: Optional<ResourceColor>)

Sets the text stroke color.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| color | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<[ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor)\> | Yes | Stroke color. Default value: font color. Invalid values are treated as the default value. |

#### \[h2\]stopBackPress15+

stopBackPress(isStopped: Optional<boolean>)

Sets whether to prevent the back key event from being propagated.

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| isStopped | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<boolean> | Yes | 
Whether to prevent the back button press from being propagated to other components or applications.

**true**: Propagation is prevented. **false**: Propagation is allowed.

Default value: **true** The default value is used for abnormal values.

 |

#### \[h2\]halfLeading18+

halfLeading(halfLeading: Optional<boolean>)

Enables half leading for text, which splits the leading equally between the top and bottom of the line.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| halfLeading | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<boolean> | Yes | 
Whether half leading is enabled. Half leading refers to splitting the leading in half and applying it equally to the top and bottom of the line.

**true**: Half leading is enabled. **false**: Half leading is not enabled.

Default value: **false**

 |

#### \[h2\]minFontScale18+

minFontScale(scale: Optional<number | Resource>)

Sets the minimum font scale factor for text.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| scale | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<number | [Resource](../../common-definitions/basic-types/document.md#resource)\> | Yes | 
Minimum font scale factor for text. The **undefined** type is supported.

Value range: \[0, 1\]

**NOTE**

A value less than 0 is handled as **0**. A value greater than 1 is handled as **1**. Abnormal values are ineffective by default.

Before use, the **configuration.json** file and **app.json5** file must be configured in the project. For details, see [Example 17: Setting the Minimum and Maximum Font Scale Factors](#example-17-setting-the-minimum-and-maximum-font-scale-factors).

 |

#### \[h2\]maxFontScale18+

maxFontScale(scale: Optional<number | Resource>)

Sets the maximum font scale factor for text.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| scale | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<number | [Resource](../../common-definitions/basic-types/document.md#resource)\> | Yes | 
Maximum font scale factor for text. The **undefined** type is supported.

Value range: \[1, +∞)

**NOTE**

Values less than 1 are treated as **1**. Abnormal values are ineffective by default.

Before use, the **configuration.json** file and **app.json5** file must be configured in the project. For details, see [Example 17: Setting the Minimum and Maximum Font Scale Factors](#example-17-setting-the-minimum-and-maximum-font-scale-factors).

 |

#### \[h2\]ellipsisMode18+

ellipsisMode(mode: Optional<EllipsisMode>)

Sets the ellipsis position. For the settings to work, [textOverflow](#textoverflow12) must be set to **TextOverflow.Ellipsis** and [maxLines](#maxlines10) must be specified. Setting **ellipsisMode** alone does not take effect.

**EllipsisMode.START** and **EllipsisMode.CENTER** take effect only when [maxLines](#maxlines10) is set to **1**.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| mode | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<[EllipsisMode](../../common-definitions/enums/document.md#ellipsismode11)\> | Yes | 
Ellipsis position.

Default value: **EllipsisMode.END**

 |

#### \[h2\]enableAutoSpacing20+

enableAutoSpacing(enabled: Optional<boolean>)

Sets whether to enable automatic spacing between Chinese and Western characters.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| enabled | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<boolean> | Yes | 
Whether to enable automatic spacing between Chinese and Western characters.

**true** to enable, **false** otherwise.

Default value: **false**

 |

#### \[h2\]scrollBarColor22+

scrollBarColor(thumbColor: ColorMetrics | undefined)

Sets the color of the scrollbar.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| thumbColor | [ColorMetrics](../../../arkts-api/ui/arkui/graphics/document.md#colormetrics12) | undefined | Yes | 
Scrollbar color.

Default value: **'#66182431'**, displayed as gray.

 |

#### Events

In addition to the [universal events](../../universal-events/document.md), the following events are supported.

#### \[h2\]onChange

onChange(callback: EditableTextOnChangeCallback)

Called when the input in the text box changes.

In this callback, if caret operations are performed, you must adjust the caret logic based on the **previewText** parameter of [EditableTextOnChangeCallback](../text-component-common-apis/document.md#editabletextonchangecallback12) to ensure it works seamlessly within the preview display scenario.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | [EditableTextOnChangeCallback](../text-component-common-apis/document.md#editabletextonchangecallback12) | Yes | Callback invoked when the input in the text box changes. |

#### \[h2\]onEditChange10+

onEditChange(callback: (isEditing: boolean) => void)

Called when the input state changes. The text box is in the editing state when it has the caret placed in it, and is in the non-editing state otherwise.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| isEditing | boolean | Yes | 
Whether the component is in the editing state.

**true**: Editing state. **false**: Non-editing state.

 |

#### \[h2\]onCopy8+

onCopy(callback: (value: string) => void)

Called when a copy operation is performed.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | string | Yes | Text that is copied. |

#### \[h2\]onCut8+

onCut(callback: (value: string) => void)

Called when a cut operation is performed.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | string | Yes | Text that is cut. |

#### \[h2\]onPaste

onPaste(callback: (value: string, event: PasteEvent) => void)

Called when a paste operation is performed.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | string | Yes | Text to be pasted. |
| event11+ | [PasteEvent](../richeditor/document.md#pasteevent11) | Yes | Custom paste event. |

#### \[h2\]onTextSelectionChange10+

onTextSelectionChange(callback: (selectionStart: number, selectionEnd: number) => void)

Called when the text selection changes or the caret position changes during editing.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| selectionStart | number | Yes | Start position of the selected text. The start position of text is **0**. |
| selectionEnd | number | Yes | End position of the selected text. |

#### \[h2\]onContentScroll10+

onContentScroll(callback: (totalOffsetX: number, totalOffsetY: number) => void)

Called when the text content is scrolled.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| totalOffsetX | number | Yes | 
Horizontal offset of the text within the content area.

Unit: [px](../../common-definitions/pixel-units/document.md)

 |
| totalOffsetY | number | Yes | 

Vertical offset of the text within the content area.

Unit: [px](../../common-definitions/pixel-units/document.md)

 |

#### \[h2\]onSubmit11+

onSubmit(callback: (enterKey: EnterKeyType) => void)

Called when the Enter key on the soft keyboard is pressed.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| enterKey | [EnterKeyType](../textinput/document.md#enterkeytype) | Yes | Type of the Enter key. If it is **EnterKeyType.NEW\_LINE** and the text box is in inline input style, **onSubmit** is not triggered. |

#### \[h2\]onSubmit14+

onSubmit(callback: TextAreaSubmitCallback)

Called when the Enter key on the soft keyboard is pressed, providing methods to maintain the editing state of the **TextArea** component upon submission.

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | [TextAreaSubmitCallback](#textareasubmitcallback14) | Yes | Called when the Enter key on the soft keyboard is pressed. |

#### \[h2\]onWillInsert12+

onWillInsert(callback: Callback<InsertValue, boolean>)

Called when text is about to be inserted.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | Callback<[InsertValue](../text-component-common-apis/document.md#insertvalue12), boolean> | Yes | 
Callback invoked when text is about to be inserted.

It returns **true** if the text is inserted; returns **false** otherwise.

This callback is not invoked for pre-edit or candidate word operations.

It is available only for system input methods.

 |

#### \[h2\]onDidInsert12+

onDidInsert(callback: Callback<InsertValue>)

Called when text is inserted.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | Callback<[InsertValue](../text-component-common-apis/document.md#insertvalue12)\> | Yes | 
Callback triggered when text is inserted.

It is available only for system input methods.

 |

#### \[h2\]onWillDelete12+

onWillDelete(callback: Callback<DeleteValue, boolean>)

Called when text is about to be deleted.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | Callback<[DeleteValue](../text-component-common-apis/document.md#deletevalue12), boolean> | Yes | 
Callback invoked when text is about to be deleted.

It returns **true** if the text is deleted; returns **false** otherwise.

This callback is not invoked for text preview.

It is available only for system input methods.

 |

#### \[h2\]onDidDelete12+

onDidDelete(callback: Callback<DeleteValue>)

Called when text is deleted.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | Callback<[DeleteValue](../text-component-common-apis/document.md#deletevalue12)\> | Yes | 
Callback triggered when text is deleted.

It is available only for system input methods.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/XQVZNx_aSuC7vjQPBl_uMw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8A3858A5F16DDF548D5C02ABF5D712606C251EFC4D76B9C1A7C985053B14D4F0)

Clicking the clear button does not trigger the **onDidDelete** callback.

#### \[h2\]onWillChange15+

onWillChange(callback: Callback<EditableTextChangeValue, boolean>)

Called when the text content is about to change.

This callback is triggered after **onWillInsert** and **onWillDelete**, but before **onDidInsert** and **onDidDelete**.

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | Callback<[EditableTextChangeValue](../text-component-common-apis/document.md#editabletextchangevalue15), boolean> | Yes | 
Callback triggered when the text content is about to change.

**true**: The change is allowed. **false**: The change is canceled.

 |

#### \[h2\]onWillAttachIME22+

onWillAttachIME(callback: Callback<IMEClient> | undefined)

Called when the input box is about to be bound to an input method.

From API version 22, the [setExtraConfig](../text-component-common-apis/document.md#setextraconfig22) method of [IMEClient](../text-component-common-apis/document.md#imeclient20) can be called to set input method extension information. After the input method is bound, it receives this extension information which can be used to implement custom functionality.

**IMEClient** is valid only during the execution of **onWillAttachIME** and cannot be called asynchronously.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | Callback<[IMEClient](../text-component-common-apis/document.md#imeclient20)\> | undefined | Yes | Callback invoked when the input box is about to be bound to an input method. |

#### TextAreaController8+

The controller for the **TextArea** component inherits from [TextContentControllerBase](../text-box-component-common-apis/document.md#textcontentcontrollerbase). The APIs involved are as follows: [getTextContentRect](../text-box-component-common-apis/document.md#gettextcontentrect), [getTextContentLineCount](../text-box-component-common-apis/document.md#gettextcontentlinecount), [getCaretOffset](../text-box-component-common-apis/document.md#getcaretoffset11), [addText](../text-box-component-common-apis/document.md#addtext15), [deleteText](../text-box-component-common-apis/document.md#deletetext15), [getSelection](../text-box-component-common-apis/document.md#getselection15), [clearPreviewText](../text-box-component-common-apis/document.md#clearpreviewtext17), and [setStyledPlaceholder](../text-box-component-common-apis/document.md#setstyledplaceholder22).

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

## Objects to Import

controller: TextAreaController = new TextAreaController()

#### \[h2\]constructor8+

constructor()

A constructor used to create a **TextAreaController** object.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### \[h2\]caretPosition8+

caretPosition(value: number): void

Sets the position of the caret.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | Yes | 
Length from the start of the string to the position where the caret is located.

Values less than 0 are treated as **0**. Values greater than the string length are treated as the string length.

 |

#### \[h2\]setTextSelection10+

setTextSelection(selectionStart: number, selectionEnd: number, options?: SelectionOptions): void

Sets the text selection range and highlights the selected text when the component is focused. This API works only when the value of **selectionStart** is less than that of **selectionEnd**.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| selectionStart | number | Yes | 
Start position of the text selection range. The start position of text in the text box is 0.

Values less than 0 are treated as **0**. Values greater than the maximum text length are treated as the maximum text length.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| selectionEnd | number | Yes | 

End position of the text selection range.

Values less than 0 are treated as **0**. Values greater than the maximum text length are treated as the maximum text length.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| options12+ | [SelectionOptions](../text-box-component-common-apis/document.md#selectionoptions12) | No | 

Configuration options for text selection.

Default value: **MenuPolicy.DEFAULT**

**Atomic service API**: This API can be used in atomic services since API version 12.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2/v3/hVe4OLFIQku1TM7lGfjjOQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BF5050E0EC37C3B4E4E1E173955F7649AC732D9A4DB196A2BC475D22BCCF9F69)

If **selectionMenuHidden** is set to **true** or a 2-in-1 device is used, calling **setTextSelection** does not display the context menu even when **options** is set to **MenuPolicy.SHOW**.

If the selected text contains an emoji, the emoji is selected when its start position is within the text selection range.

#### \[h2\]stopEditing10+

stopEditing(): void

Exits the editing state.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### TextAreaType11+

Multi-line text input box type.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| NORMAL | 0 | 
Basic input mode with no special restrictions.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| NUMBER | 2 | 

Digit input mode.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| PHONE\_NUMBER | 3 | 

Phone number input mode.

In this mode, the following characters are allowed: digits, spaces, plus signs (+), hyphens (-), asterisks (\*), and number signs (#); the length is not limited.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| EMAIL | 5 | 

Email address input mode.

This mode accepts only digits, letters, underscores (\_), dots (.), and the following special characters: ! # $ % & ' \* + - / = ? ^ \` { | } ~ @ (which can only appear once)

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| NUMBER\_DECIMAL12+ | 12 | 

Decimal number input mode.

The value can contain digits and one decimal point.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| URL12+ | 13 | 

URL input mode with no special restrictions.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| ONE\_TIME\_CODE20+ | 14 | 

One-time code (verification code) input mode with no special restrictions.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |

#### TextAreaSubmitCallback14+

type TextAreaSubmitCallback = (enterKeyType: EnterKeyType, event?: SubmitEvent) => void

Represents the callback invoked when the Enter key on the soft keyboard is pressed.

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| enterKeyType | [EnterKeyType](../textinput/document.md#enterkeytype) | Yes | 
Type of the Enter key.

If the type is **EnterKeyType.NEW\_LINE**, **onSubmit** is not triggered.

 |
| event | [SubmitEvent](../textinput/document.md#submitevent11) | No | Submit event. |

#### Example

## Example 1: Setting and Obtaining the Caret Position

This example shows how to set and obtain the caret position using [controller](#textareacontroller8), available since API version 8.

// xxx.ets
@Entry
@Component
struct TextAreaExample {
  @State text: string = '';
  @State positionInfo: CaretOffset = { index: 0, x: 0, y: 0 };
  controller: TextAreaController = new TextAreaController();

  build() {
    Column() {
      TextArea({
        text: this.text,
        placeholder: 'The text area can hold an unlimited amount of text. input your word...',
        controller: this.controller
      })
        .placeholderFont({ size: 16, weight: 400 })
        .width(336)
        .height(56)
        .margin(20)
        .fontSize(16)
        .fontColor('#182431')
        .backgroundColor('#FFFFFF')
        .onChange((value: string) => {
          this.text = value;
        })
      Text(this.text)
      Button('Set caretPosition 1')
        .backgroundColor('#007DFF')
        .margin(15)
        .onClick(() => {
          // Move the caret to after the first entered character.
          this.controller.caretPosition(1);
        })
      Button('Get CaretOffset')
        .backgroundColor('#007DFF')
        .margin(15)
        .onClick(() => {
          this.positionInfo = this.controller.getCaretOffset();
        })
    }.width('100%').height('100%').backgroundColor('#F1F3F5')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/L9aFs5P5TNWmd1iGI12csQ/en-us_image_0000002568685357.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C007C56DD9FC21FC86CD5248CEFBFDC340FAE7FA5AA50ED9149C1C56A41255BE)

## Example 2: Implementing a Counter

This example demonstrates how to implement the character counter functionality using the [maxLength](#maxlength10) and [showCounter](#showcounter10) attributes, both available since API version 10.

// xxx.ets
@Entry
@Component
struct TextAreaExample {
  @State text: string = '';
  controller: TextAreaController = new TextAreaController();

  build() {
    Column() {
      TextArea({
        text: this.text,
        placeholder: 'The text area can hold an unlimited amount of text. input your word...',
        controller: this.controller
      })
        .placeholderFont({ size: 16, weight: 400 })
        .width(336)
        .height(56)
        .margin(20)
        .fontSize(16)
        .fontColor('#182431')
        .backgroundColor('#FFFFFF')
        .maxLength(4)
        .showCounter(true, { thresholdPercentage: 50, highlightBorder: true })
          // The character counter is in this format: Number of characters that have been entered/Maximum number of characters allowed, which is specified by maxLength().
          // The character counter is displayed when the number of characters that have been entered is greater than the maximum number of characters multiplied by 50% (threshold percentage).
          // When highlightBorder is set to false, the text box border does not turn red when the input exceeds the maximum character limit. The default value is true.
        .onChange((value: string) => {
          this.text = value;
        })
    }.width('100%').height('100%').backgroundColor('#F1F3F5')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/W2IOJcWySQaVjtMHmDeX2g/en-us_image_0000002568765367.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=437D39DD15BA31C64B686D28FE03BB4D18005AB99FE7E5E87A9C00171B007FF6)

## Example 3: Implementing a Custom Keyboard

This example implements a custom keyboard using the [customKeyboard](#customkeyboard10) attribute (available since API version 10) to set the input parameter type in **value** to [CustomBuilder](../../common-definitions/basic-types/document.md#custombuilder8) and [ComponentContent](../../../arkts-api/ui/arkui/componentcontent/document.md#componentcontent-1).

Since API version 22, [ComponentContent](../../../arkts-api/ui/arkui/componentcontent/document.md#componentcontent-1) is added to the input parameter type of [customKeyboard](#customkeyboard10).

// xxx.ets
import { ComponentContent } from '@kit.ArkUI';
class BuilderParams {
  inputValue: string;
  controller: TextAreaController;

  constructor(inputValue: string, controller: TextAreaController) {
    this.inputValue = inputValue;
    this.controller = controller;
  }
}
@Builder
function CustomKeyboardBuilder(builderParams: BuilderParams) {
  Column() {
    Row() {
      Button('x').onClick(() => {
        // Disable the custom keyboard.
        builderParams.controller.stopEditing();
      }).margin(10)
    }

    Grid() {
      ForEach(\[1, 2, 3, 4, 5, 6, 7, 8, 9, '\*', 0, '#'\], (item: number | string) => {
        GridItem() {
          Button(item + "")
            .width(110).onClick(() => {
            builderParams.inputValue += item;
          })
        }
      })
    }.maxCount(3).columnsGap(10).rowsGap(10).padding(5)
  }.backgroundColor(Color.Gray)
}
@Entry
@Component
struct TextAreaExample {
  controller: TextAreaController = new TextAreaController();
  @State inputValue: string = "";
  @State componentContent ?: ComponentContent<BuilderParams> = undefined;
  @State builderParam: BuilderParams = new BuilderParams(this.inputValue, this.controller);
  @State supportAvoidance: boolean = true;

  aboutToAppear(): void {
    // Create a ComponentContent instance.
    this.componentContent = new ComponentContent(this.getUIContext(), wrapBuilder(CustomKeyboardBuilder), this.builderParam);
  }
  build(){
    Column() {
      Text('Builder').margin(10).border({ width: 1 })
      TextArea({ controller: this.builderParam.controller, text: this.builderParam.inputValue })
        .customKeyboard(this.componentContent, { supportAvoidance: this.supportAvoidance })
        .margin(10).border({ width: 1 }).height('48vp')

      Text('ComponentContent').margin(10).border({ width: 1 })
      TextArea({ controller: this.builderParam.controller, text: this.builderParam.inputValue })
        .customKeyboard(CustomKeyboardBuilder(this.builderParam), { supportAvoidance: this.supportAvoidance })
        .margin(10).border({ width: 1 }).height('48vp')
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/WMOVsBUORQWL9X1oAu2_gg/en-us_image_0000002537765642.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=366D9AD93D69F795F1BC312F7060464AF7E40227AEB878783D760A3FAFB63061)

## Example 4: Setting the Enter Key Type

This example shows how to use the [enterKeyType](#enterkeytype11) attribute, which is supported since API version 11, to dynamically change the effect of the **Enter** key on the soft keyboard.

// xxx.ets
@Entry
@Component
struct TextAreaExample {
  @State text: string = '';
  @State enterTypes: Array<EnterKeyType> =
    \[EnterKeyType.Go, EnterKeyType.Search, EnterKeyType.Send, EnterKeyType.Done, EnterKeyType.Next,
      EnterKeyType.PREVIOUS, EnterKeyType.NEW\_LINE\];
  @State index: number = 0;

  build() {
    Column({ space: 20 }) {
      TextArea({ placeholder: 'Enter user name', text: this.text })
        .width(380)
        .enterKeyType(this.enterTypes\[this.index\])
        .onChange((value: string) => {
          this.text = value;
        })
        .onSubmit((enterKey: EnterKeyType) => {
          console.info("trigger area onSubmit" + enterKey);
        })
      Button('Change EnterKeyType').onClick(() => {
        this.index = (this.index + 1) % this.enterTypes.length;
      })

    }.width('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/jcorX-1nRIqMVBAjUC-iQw/en-us_image_0000002537925582.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=26122D43FB630E21E41EAAC140A4932BCA44A76C2B191B1BCC027490410C7825)

## Example 5: Setting Text Wrapping Rules

This example demonstrates the effects of different text wrapping rules using the [wordBreak](#wordbreak12) attribute, available since API version 12.

// xxx.ets
@Entry
@Component
struct TextAreaExample {
  build() {
    Column() {
      Text("WordBreakType as NORMAL").fontSize(16).fontColor(0xFF0000)
      TextArea({
        text: 'This is set wordBreak to WordBreak text Taumatawhakatangihangakoauauotamateaturipukakapikimaungahoronukupokaiwhenuakitanatahu.'
      })
        .fontSize(16)
        .border({ width: 1 })
        .wordBreak(WordBreak.NORMAL)
      Text("WordBreakType as BREAK\_ALL").fontSize(16).fontColor(0xFF0000)
      TextArea({
        text: 'This is set wordBreak to WordBreak text Taumatawhakatangihangakoauauotamateaturipukakapikimaungahoronukupokaiwhenuakitanatahu.'
      })
        .fontSize(16)
        .border({ width: 1 })
        .wordBreak(WordBreak.BREAK\_ALL)
      Text("WordBreakType as BREAK\_ALL, Chinese Text").fontSize(16).fontColor(0xFF0000)
      TextArea({
        text: '多行文本输入框组件，当输入的文本内容超过组件宽度时会自动换行显示。\\n高度未设置时，组件无默认高度，自适应内容高度。宽度未设置时，默认撑满最大宽度。'
      })
        .fontSize(16)
        .border({ width: 1 })
        .wordBreak(WordBreak.BREAK\_ALL)
      Text("WordBreakType as BREAK\_WORD").fontSize(16).fontColor(0xFF0000)
      TextArea({
        text: 'This is set wordBreak to WordBreak text Taumatawhakatangihangakoauauotamateaturipukakapikimaungahoronukupokaiwhenuakitanatahu.'
      })
        .fontSize(16)
        .border({ width: 1 })
        .wordBreak(WordBreak.BREAK\_WORD)
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/9e991RroQ2-rtwHlvS5tkw/en-us_image_0000002568685359.jpeg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9DEFD73B5107EE2BD5E4F7CEBF6213B6940A0F505D8070F79E37AA515402B14F)

## Example 6: Setting the Text Style

This example showcases various text styles by using the [lineHeight](#lineheight12), [letterSpacing](#letterspacing12), and [decoration](#decoration12) attributes, which are supported since API version 12.

// xxx.ets
@Entry
@Component
struct TextAreaExample {
  build() {
    Row() {
      Column() {
        Text('lineHeight').fontSize(9).fontColor(0xCCCCCC)
        TextArea({ text: 'lineHeight unset' })
          .border({ width: 1 }).padding(10).margin(5)
        TextArea({ text: 'lineHeight 15' })
          .border({ width: 1 }).padding(10).margin(5).lineHeight(15)
        TextArea({ text: 'lineHeight 30' })
          .border({ width: 1 }).padding(10).margin(5).lineHeight(30)

        Text('letterSpacing').fontSize(9).fontColor(0xCCCCCC)
        TextArea({ text: 'letterSpacing 0' })
          .border({ width: 1 }).padding(5).margin(5).letterSpacing(0)
        TextArea({ text: 'letterSpacing 3' })
          .border({ width: 1 }).padding(5).margin(5).letterSpacing(3)
        TextArea({ text: 'letterSpacing -1' })
          .border({ width: 1 }).padding(5).margin(5).letterSpacing(-1)

        Text('decoration').fontSize(9).fontColor(0xCCCCCC)
        TextArea({ text: 'LineThrough, Red\\nsecond line' })
          .border({ width: 1 }).padding(5).margin(5)
          .decoration({ type: TextDecorationType.LineThrough, color: Color.Red })
        TextArea({ text: 'Overline, Red, DOTTED\\nsecond line' })
          .border({ width: 1 }).padding(5).margin(5)
          .decoration({ type: TextDecorationType.Overline, color: Color.Red, style: TextDecorationStyle.DOTTED })
        TextArea({ text: 'Underline, Red, WAVY\\nsecond line' })
          .border({ width: 1 }).padding(5).margin(5)
          .decoration({ type: TextDecorationType.Underline, color: Color.Red, style: TextDecorationStyle.WAVY })
      }.height('90%')
    }
    .width('90%')
    .margin(10)
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/4SWPKTRURiaeEwRLKgWd7w/en-us_image_0000002568765369.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E3A9CAD9BA437382642002B447308EAD52F861D60E51F5A79B04716CCD2A0000)

## Example 7: Setting Text Feature Effects

This example demonstrates how to display text with various typographic features using the [fontFeature](#fontfeature12) attribute, available since API version 12.

// xxx.ets
@Entry
@Component
struct TextAreaExample {
  @State text1: string = 'This is ss01 on : 0123456789';
  @State text2: string = 'This is ss01 off: 0123456789';

  build() {
    Column() {
      TextArea({ text: this.text1 })
        .fontSize(20)
        .margin({ top: 200 })
        .fontFeature("\\"ss01\\" on")
      TextArea({ text: this.text2 })
        .margin({ top: 10 })
        .fontSize(20)
        .fontFeature("\\"ss01\\" off")
    }
    .width("90%")
    .margin("5%")
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/RE888NiAToakdgOBN67u2g/en-us_image_0000002537765644.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=65331BF29D27121B9FA5D23A009A1503850D47091EC30A4DB87AC7998099184D)

## Example 8: Setting Custom Keyboard Avoidance

This example implements the custom keyboard avoidance effect by configuring the [KeyboardOptions](../richeditor/document.md#keyboardoptions12) API (available since API version 12) through the [customKeyboard](#customkeyboard10) attribute (available since API version 10).

// xxx.ets
@Entry
@Component
struct TextAreaExample {
  controller: TextAreaController = new TextAreaController();
  @State inputValue: string = "";
  @State height1: string | number = '80%';
  @State height2: number = 100;
  @State supportAvoidance: boolean = true;

  // Create a custom keyboard component.
  @Builder
  CustomKeyboardBuilder() {
    Column() {
      Row() {
        Button('x').onClick(() => {
          // Disable the custom keyboard.
          this.controller.stopEditing();
        }).margin(10)
      }

      Grid() {
        ForEach(\[1, 2, 3, 4, 5, 6, 7, 8, 9, '\*', 0, '#'\], (item: number | string) => {
          GridItem() {
            Button(item + "")
              .width(110).onClick(() => {
              this.inputValue += item;
            })
          }
        })
      }.maxCount(3).columnsGap(10).rowsGap(10).padding(5)
    }.backgroundColor(Color.Gray)
  }

  build() {
    Column() {
      Row() {
        Button("20%")
          .fontSize(24)
          .onClick(() => {
            this.height1 = "20%";
          })
        Button("80%")
          .fontSize(24)
          .margin({ left: 20 })
          .onClick(() => {
            this.height1 = "80%";
          })
      }
      .justifyContent(FlexAlign.Center)
      .alignItems(VerticalAlign.Bottom)
      .height(this.height1)
      .width("100%")
      .padding({ bottom: 50 })

      TextArea({ controller: this.controller, text: this.inputValue })// Bind the custom keyboard.
        .height(100)
        .customKeyboard(this.CustomKeyboardBuilder(), { supportAvoidance: this.supportAvoidance })
        .margin(10)
        .border({ width: 1 })
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/7x3xyy-6T---jx_RpTJhqQ/en-us_image_0000002537925584.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FA871F9F3D356DD3A8A32D5B27871902581EDFF63B641C70955B5C72D065C5A1)

## Example 9: Setting Text Auto-Adaptation

This example shows how to implement adaptive font sizing for text through the [minFontSize](#minfontsize12), [maxFontSize](#maxfontsize12), and [heightAdaptivePolicy](#heightadaptivepolicy12) attributes, available since API version 12.

// xxx.ets
@Entry
@Component
struct TextAreaExample {
  build() {
    Row() {
      Column() {
        Text('heightAdaptivePolicy').fontSize(9).fontColor(0xCCCCCC)
        TextArea({text: 'This is the text with the height adaptive policy set'})
          .width('80%').height(90).borderWidth(1).margin(1)
          .minFontSize(4)
          .maxFontSize(40)
          .maxLines(3)
          .heightAdaptivePolicy(TextHeightAdaptivePolicy.MAX\_LINES\_FIRST)
        TextArea({text: 'This is the text with the height adaptive policy set'})
          .width('80%').height(90).borderWidth(1).margin(1)
          .minFontSize(4)
          .maxFontSize(40)
          .maxLines(3)
          .heightAdaptivePolicy(TextHeightAdaptivePolicy.MIN\_FONT\_SIZE\_FIRST)
        TextArea({text: 'This is the text with the height adaptive policy set'})
          .width('80%').height(90).borderWidth(1).margin(1)
          .minFontSize(4)
          .maxFontSize(40)
          .maxLines(3)
          .heightAdaptivePolicy(TextHeightAdaptivePolicy.LAYOUT\_CONSTRAINT\_FIRST)
      }.height('90%')
    }
    .width('90%')
    .margin(10)
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/9CLZWtMOT1uGEHdnvTIVNQ/en-us_image_0000002568685361.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9D93D8D6EBE42C68569C7B147F652CBE7AF40FFE086A27ED2D919A446DDC6EC1)

## Example 10: Setting the Text Line Spacing

This example demonstrates the display effect of text under different line spacing settings through the [lineSpacing](#linespacing12) attribute, available since API version 12. The **onlyBetweenLines** property in [LineSpacingOptions](../text-component-common-apis/document.md#linespacingoptions20) (available since API version 20) controls whether line spacing applies only between lines.

// xxx.ets
import { LengthMetrics } from '@kit.ArkUI';

@Entry
@Component
struct TextAreaExample {
  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Start, justifyContent: FlexAlign.SpaceBetween }) {
      Text('TextArea lineSpacing.').fontSize(9).fontColor(0xCCCCCC)
      TextArea({ text: 'This is the TextArea with no lineSpacing set.' })
        .fontSize(12)
      TextArea({ text: 'This is the TextArea with lineSpacing set to 20\_px.' })
        .fontSize(12)
        .lineSpacing(LengthMetrics.px(20))
      TextArea({ text: 'This is the TextArea with lineSpacing set to 20\_vp.' })
        .fontSize(12)
        .lineSpacing(LengthMetrics.vp(20))
      TextArea({ text: 'This is the TextArea with lineSpacing set to 20\_fp.' })
        .fontSize(12)
        .lineSpacing(LengthMetrics.fp(20))
      TextArea({ text: 'This is the TextArea with lineSpacing set to 20\_lpx.' })
        .fontSize(12)
        .lineSpacing(LengthMetrics.lpx(20))
      TextArea({ text: 'This is the TextArea with lineSpacing set to 100%.' })
        .fontSize(12)
        .lineSpacing(LengthMetrics.percent(1))
      TextArea({ text: 'The line spacing of this TextArea is set to 20\_px, and the spacing is effective only between the lines.' })
        .fontSize(12)
        .lineSpacing(LengthMetrics.px(20), { onlyBetweenLines: true })
    }.height(600).width(350).padding({ left: 35, right: 35, top: 35 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/QrJVAmuUQ6-1MId3Yk0iVg/en-us_image_0000002568765371.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BDF24835DDEDA2EF64CBBBC7C4E0C7EB67CA21A7C14953C9C71028A2DFC7C208)

## Example 11: Setting Autofill

This example illustrates how to implement the autofill feature for text input using the [contentType](#contenttype12) and [enableAutoFill](#enableautofill12) attributes, available since API version 12.

// xxx.ets
@Entry
@Component
struct TextAreaExample {
  @State text: string = '';

  build() {
    Column() {
      // Email address autofill.
      TextArea({ placeholder: 'input your email...' })
        .width('95%')
        .height(40)
        .margin(20)
        .contentType(ContentType.EMAIL\_ADDRESS)
        .enableAutoFill(true)
        .maxLength(20)
      // Full street address autofill.
      TextArea({ placeholder: 'input your street address...' })
        .width('95%')
        .height(40)
        .margin(20)
        .contentType(ContentType.FULL\_STREET\_ADDRESS)
        .enableAutoFill(true)
        .maxLength(20)
    }.width('100%').height('100%').backgroundColor('#F1F3F5')
  }
}

## Example 12: Setting Line Break Rules

This example demonstrates the effects of different line break rules using the [lineBreakStrategy](#linebreakstrategy12) attribute, available since API version 12.

// xxx.ets
@Entry
@Component
struct TextAreaExample {
  @State message1: string =
    "They can be classified as built-in components–those directly provided by the ArkUI framework and custom components – those defined by developers" +
      "The built-in components include buttons radio buttonsprogress indicators and text You can set the rendering effect of these components in method chaining mode," +
      "page components are divided into independent UI units to implement independent creation development and reuse of different units on pages making pages more engineering-oriented.";
  @State lineBreakStrategyIndex: number = 0;
  @State lineBreakStrategy: LineBreakStrategy\[\] =
    \[LineBreakStrategy.GREEDY, LineBreakStrategy.HIGH\_QUALITY, LineBreakStrategy.BALANCED\];
  @State lineBreakStrategyStr: string\[\] = \['GREEDY', 'HIGH\_QUALITY', 'BALANCED'\];

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Start }) {
      Text('lineBreakStrategy').fontSize(9).fontColor(0xCCCCCC)
      TextArea({ text: this.message1 })
        .fontSize(12)
        .border({ width: 1 })
        .padding(10)
        .width('100%')
        .lineBreakStrategy(this.lineBreakStrategy\[this.lineBreakStrategyIndex\])
      Row() {
        Button('Current lineBreakStrategy value: ' + this.lineBreakStrategyStr\[this.lineBreakStrategyIndex\]).onClick(() => {
          this.lineBreakStrategyIndex++;
          if (this.lineBreakStrategyIndex > (this.lineBreakStrategyStr.length - 1)) {
            this.lineBreakStrategyIndex = 0;
          }
        })
      }.padding({ top: 10 })
    }.height(700).width(370).padding({ left: 35, right: 35, top: 35 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/i_L35IB5T7-y_3fpSwq1Ww/en-us_image_0000002537765646.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=21BD6DF4B6D4FA182861582650EC393FD0CF4DD3195A0273DB88142BC2058EAC)

## Example 13: Setting Insert and Delete Callbacks

This example showcases the implementation of insert and delete operations using the [onWillInsert](#onwillinsert12), [onDidInsert](#ondidinsert12), [onWillDelete](#onwilldelete12), and [onDidDelete](#ondiddelete12) APIs, available since API version 12.

// xxx.ets
@Entry
@Component
struct TextAreaExample {
  @State insertValue: string = "";
  @State deleteValue: string = "";
  @State insertOffset: number = 0;
  @State deleteOffset: number = 0;
  @State deleteDirection: number = 0;

  build() {
    Row() {
      Column() {
        TextArea({ text: "Insert callbacks" })
          .width(300)
          .height(60)
          .onWillInsert((info: InsertValue) => {
            this.insertValue = info.insertValue;
            return true;
          })
          .onDidInsert((info: InsertValue) => {
            this.insertOffset = info.insertOffset;
          })

        Text("insertValue:" + this.insertValue + "  insertOffset:" + this.insertOffset).height(30)

        TextArea({ text: "Delete callbacks" })
          .width(300)
          .height(60)
          .onWillDelete((info: DeleteValue) => {
            this.deleteValue = info.deleteValue;
            this.deleteDirection = info.direction;
            return true;
          })
          .onDidDelete((info: DeleteValue) => {
            this.deleteOffset = info.deleteOffset;
            this.deleteDirection = info.direction;
          })

        Text("deleteValue:" + this.deleteValue + "  deleteOffset:" + this.deleteOffset).height(30)
        Text("deleteDirection:" + (this.deleteDirection == 0 ? "BACKWARD" : "FORWARD")).height(30)

      }.width('100%')
    }
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/kc1YZ6d-S7qUGJDJ_Eor1Q/en-us_image_0000002537925586.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=768468C3995C5450BEAD300262EBB9D9D48D1C6400FB9B1BEA600E352E82F08D)

## Example 14: Setting Custom Menu Extensions

This example implements custom menu extension items for text using the [editMenuOptions](#editmenuoptions12) API (available since API version 12), allowing configuration of text content, icons, and callbacks. Menu data can also be configured through the [onPrepareMenu](../text-component-common-apis/document.md#properties-1) callback (available since API version 20).

// xxx.ets
@Entry
@Component
struct TextAreaExample {
  @State text: string = 'TextArea editMenuOptions';
  @State endIndex: number = 0;
  onCreateMenu = (menuItems: Array<TextMenuItem>) => {
    // Replace $r('app.media.startIcon') with the image resource file you use.
    let item1: TextMenuItem = {
      content: 'create1',
      icon: $r('app.media.startIcon'),
      id: TextMenuItemId.of('create1'),
    };
    let item2: TextMenuItem = {
      content: 'create2',
      id: TextMenuItemId.of('create2'),
      icon: $r('app.media.startIcon'),
    };
    menuItems.push(item1);
    menuItems.unshift(item2);
    return menuItems;
  }
  onMenuItemClick = (menuItem: TextMenuItem, textRange: TextRange) => {
    if (menuItem.id.equals(TextMenuItemId.of("create2"))) {
      console.info("Intercept id: create2 start:" + textRange.start + "; end:" + textRange.end);
      return true;
    }
    if (menuItem.id.equals(TextMenuItemId.of("prepare1"))) {
      console.info("Intercept id: prepare1 start:" + textRange.start + "; end:" + textRange.end);
      return true;
    }
    if (menuItem.id.equals(TextMenuItemId.COPY)) {
      console.info("Intercept COPY start:" + textRange.start + "; end:" + textRange.end);
      return true;
    }
    if (menuItem.id.equals(TextMenuItemId.SELECT\_ALL)) {
      console.info("Do not intercept SELECT\_ALL start:" + textRange.start + "; end:" + textRange.end);
      return false;
    }
    return false;
  }
  onPrepareMenu = (menuItems: Array<TextMenuItem>) => {
    // Replace $r('app.media.startIcon') with the image resource file you use.
    let item1: TextMenuItem = {
      content: 'prepare1\_' + this.endIndex,
      icon: $r('app.media.startIcon'),
      id: TextMenuItemId.of('prepare1'),
    };
    menuItems.unshift(item1);
    return menuItems;
  }
  @State editMenuOptions: EditMenuOptions = {
    onCreateMenu: this.onCreateMenu,
    onMenuItemClick: this.onMenuItemClick,
    onPrepareMenu: this.onPrepareMenu
  };

  build() {
    Column() {
      TextArea({ text: this.text })
        .width('95%')
        .height(56)
        .editMenuOptions(this.editMenuOptions)
        .margin({ top: 100 })
        .onTextSelectionChange((selectionStart: number, selectionEnd: number) => {
          this.endIndex = selectionEnd;
        })
    }
    .width("90%")
    .margin("5%")
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/vhRskxvOQHepAqu1HtKERg/en-us_image_0000002568685363.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9DAB89CBB8A53D1F5862DE416B215B1A39125DEB8C06F1B76E54700674843900)

## Example 15: Setting Text Overflow

This example demonstrates how to clip text with an ellipsis and adjust its position using the [textOverflow](#textoverflow12) (available since API version 12), [ellipsisMode](#ellipsismode18) (available since API version 18), and [maxLines](#maxlines10) (available since API version 10) attributes.

// xxx.ets
@Entry
@Component
struct EllipsisModeExample {
  @State textIndex: number = 0;
  @State text: string = "As the sun begins to set, casting a warm golden hue across the sky," +
    "the world seems to slow down and breathe a sigh of relief. The sky is painted with hues of orange, " +
    " pink, and lavender, creating a breath taking tapestry that stretches as far as the eye can see." +
    "The air is filled with the sweet scent of blooming flowers, mingling with the earthy aroma of freshly turned soil.";
  @State ellipsisModeIndex: number = 0;
  @State ellipsisMode: (EllipsisMode | undefined | null)\[\] =
    \[EllipsisMode.START, EllipsisMode.END, EllipsisMode.CENTER, undefined, null\];
  @State ellipsisModeStr: string\[\] = \['START ', 'END', 'CENTER', 'undefined', 'null'\];
  @State textOverflowIndex: number = 0;
  @State textOverflow: TextOverflow\[\] = \[TextOverflow.Ellipsis, TextOverflow.Clip\];
  @State textOverflowStr: string\[\] = \['Ellipsis', 'Clip'\];
  @State maxLinesIndex: number = 0;
  @State maxLines: number\[\] = \[1, 2, 3\];
  @State maxLinesStr: string\[\] = \['1', '2', '3'\];
  @State styleAreaIndex: number = 0;
  @State styleArea: TextContentStyle\[\] = \[TextContentStyle.INLINE, TextContentStyle.DEFAULT\];
  @State styleAreaStr: string\[\] = \['INLINE', 'DEFAULT'\];

  build() {
    Column({ space: 20 }) {
      TextArea({ text: this.text })
        .textOverflow(this.textOverflow\[this.textOverflowIndex\])
        .ellipsisMode(this.ellipsisMode\[this.ellipsisModeIndex\])
        .maxLines(this.maxLines\[this.maxLinesIndex\])
        .style(this.styleArea\[this.styleAreaIndex\])
        .fontSize(30)
        .margin(30)

      Button('ellipsisMode Value: ' + this.ellipsisModeStr\[this.ellipsisModeIndex\]).onClick(() => {
        this.ellipsisModeIndex++;
        if (this.ellipsisModeIndex > (this.ellipsisModeStr.length - 1)) {
          this.ellipsisModeIndex = 0;
        }
      }).fontSize(20)
      Button('textOverflow Value: ' + this.textOverflowStr\[this.textOverflowIndex\]).onClick(() => {
        this.textOverflowIndex++;
        if (this.textOverflowIndex > (this.textOverflowStr.length - 1)) {
          this.textOverflowIndex = 0;
        }
      }).fontSize(20)
      Button('maxLines Value: ' + this.maxLinesStr\[this.maxLinesIndex\]).onClick(() => {
        this.maxLinesIndex++;
        if (this.maxLinesIndex > (this.maxLinesStr.length - 1)) {
          this.maxLinesIndex = 0;
        }
      }).fontSize(20)
      Button('Style Value: ' + this.styleAreaStr\[this.styleAreaIndex\]).onClick(() => {
        this.styleAreaIndex++;
        if (this.styleAreaIndex > (this.styleAreaStr.length - 1)) {
          this.styleAreaIndex = 0;
        }
      }).fontSize(20)
    }.height(600).width('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/fSzXr_sRSgW2jwqLQ4AizA/en-us_image_0000002568765373.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=817418354B5D86CDFA41E633136AF08FD34F8ACF74A39721E3B41B1A81080679)

## Example 16: Implementing Custom Copy, Cut, and Paste Behavior

This example demonstrates how to listen for text selection menu actions using [onCopy](#oncopy8), [onCut](#oncut8), and [onPaste](#onpaste) APIs. It shows how to intercept system paste functionality and implement custom paste behavior. In addition, the example uses [maxFontScale](#maxfontscale18) and [minFontScale](#minfontscale18) attributes to configure font scaling limits.

// xxx.ets
@Entry
@Component
struct TextAreaExample {
  @State text: string = '';
  controller: TextAreaController = new TextAreaController();

  build() {
    Column() {
      TextArea({
        text: this.text,
        placeholder: 'placeholder',
        controller: this.controller
      })
        .placeholderColor(Color.Red)
        .textAlign(TextAlign.Center)
        .caretColor(Color.Green)
        .caretStyle({ width: '2vp' })
        .fontStyle(FontStyle.Italic)
        .fontWeight(FontWeight.Bold)
        .fontFamily('HarmonyOS Sans')
        .inputFilter('\[a-zA-Z\]+', (value) => { // Only alphabetic input is allowed.
          console.error(\`unsupported char ${value}\`);
        })
        .copyOption(CopyOptions.LocalDevice)
        .enableKeyboardOnFocus(false)
        .selectionMenuHidden(false)
        .barState(BarState.On)
        .type(TextAreaType.NORMAL)
        .selectedBackgroundColor(Color.Orange)
        .textIndent(2)
        .halfLeading(true)
        .minFontScale(1)
        .maxFontScale(2)
        .enablePreviewText(true)
        .enableHapticFeedback(true)
        .stopBackPress(false)// Delegate back press to other components.
        .width(336)
        .height(56)
        .margin(20)
        .fontSize(16)
        .onEditChange((isEditing: boolean) => {
          console.info(\`isEditing ${isEditing}\`);
        })
        .onCopy((value) => {
          console.info(\`copy ${value}\`);
        })
        .onCut((value) => {
          console.info(\`cut ${value}\`);
        })
        .onPaste((value, event) => {
          // Prevent the default system paste behavior and implement custom logic.
          if (event.preventDefault) {
            event.preventDefault();
          }
          console.info(\`paste:${value}\`);
          this.text = value;
        })
        .onTextSelectionChange((start: number, end: number) => {
          console.info(\`onTextSelectionChange start ${start}, end ${end}\`);
        })
        .onContentScroll((totalOffsetX: number, totalOffsetY: number) => {
          console.info(\`onContentScroll offsetX ${totalOffsetX}, offsetY ${totalOffsetY}\`);
        })
    }.width('100%').height('100%').backgroundColor('#F1F3F5')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/APm1gCEvSu6k4qwUNMTYQQ/en-us_image_0000002537765648.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D18ABEBE8AFB31A110F194E948E4EEFFB6E5CD872102F6D9EEC3E27C66292208)

## Example 17: Setting the Minimum and Maximum Font Scale Factors

This example demonstrates how to set the minimum and maximum font scale factors using [minFontScale](#minfontscale18) and [maxFontScale](#maxfontscale18), available since API version 18.

// Enable application font scaling to follow system settings.
// Create a new directory named profile in the following path: AppScope/resources/base.
// Inside the newly created profile directory, create a file named configuration.json.
// Add the following code to the configuration.json file:
{
  "configuration": {
    "fontSizeScale": "followSystem",
    "fontSizeMaxScale": "3.2"
  }
}

// Modify the app.json5 file in AppScope as follows:
{
  "app": {
    "bundleName": "com.example.myapplication",
    "vendor": "example",
    "versionCode": 1000000,
    "versionName": "1.0.0",
    "icon": "$media:app\_icon",
    "label": "$string:app\_name",
    "configuration": "$profile:configuration"
  }
}

// xxx.ets
@Entry
@Component
struct TextAreaExample {
  @State minFontScale: number = 0.85;
  @State maxFontScale: number = 2;

  build() {
    Column() {
      Column({ space: 30 }) {
        Text("Use minFontScale and maxFontScale to adjust the maximum and minimum font scale factors of the text display.")
        TextArea({
          placeholder: 'The text area can hold an unlimited amount of text. input your word...',
          text: 'Use minFontScale and maxFontScale to adjust the maximum and minimum font scale factors of the text display.'
        })
          .minFontScale(this.minFontScale)// Set the minimum font scale factor. If the parameter is set to undefined, the default scale factor is used.
          .maxFontScale(this.maxFontScale) // Set the maximum font scale factor. If the parameter is set to undefined, the default scale factor is used.
      }.width('100%')
    }
  }
}

## Example 18: Setting Text Selection for a Specified Region

This example demonstrates how to set text selection for a specified region and the display/hide strategy of the menu using the [setTextSelection](#settextselection10) API, available since API version 10.

// xxx.ets

@Entry
@Component
struct TextAreaExample {
  controller: TextAreaController = new TextAreaController();
  @State startIndex: number = 0;
  @State endIndex: number = 0;

  build() {
    Column({ space: 3 }) {
      Text('Selection start:' + this.startIndex + ' end:' + this.endIndex)
      TextArea({ text: 'Hello World', controller: this.controller })
        .width('95%')
        .height(80)
        .margin(10)
        .defaultFocus(true)
        .enableKeyboardOnFocus(true)
        .onTextSelectionChange((selectionStart: number, selectionEnd: number) => {
          this.startIndex = selectionStart;
          this.endIndex = selectionEnd;
        })

      Button('setTextSelection \[0,3\], set menuPolicy is MenuPolicy.SHOW')
        .onClick(() => {
          this.controller.setTextSelection(0, 3, { menuPolicy: MenuPolicy.SHOW });
        })
    }
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/vCke_wYVSluXhDT7OT8ZSA/en-us_image_0000002537925588.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=25C39DD4B431FA4E2FA0ED43C139F8EFB95A37AF37B409E8670E23B760B08FE4)

## Example 19: Setting Text Stroke

This example demonstrates how to set the stroke width and color for text using the [strokeWidth](#strokewidth20) and [strokeColor](#strokecolor20) attributes, available since API version 20.

// xxx.ets
import { LengthMetrics } from '@kit.ArkUI';

@Entry
@Component
struct TextAreaExample {
  build() {
    Row() {
      Column() {
        Text('stroke feature').fontSize(9).fontColor(0xCCCCCC)

        TextArea({ text: 'Text without stroke' })
          .width('100%')
          .height(60)
          .borderWidth(1)
          .fontSize(40)
        TextArea({ text: 'Text with stroke' })
          .width('100%')
          .height(60)
          .borderWidth(1)
          .fontSize(40)
          .strokeWidth(LengthMetrics.px(-3.0))
          .strokeColor(Color.Red)
        TextArea({ text: 'Text with stroke' })
          .width('100%')
          .height(60)
          .borderWidth(1)
          .fontSize(40)
          .strokeWidth(LengthMetrics.px(3.0))
          .strokeColor(Color.Red)
      }.height('90%')
    }
    .width('90%')
    .margin(10)
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/G0mqJ_mGS661lhLMYrM6Nw/en-us_image_0000002568685365.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=03AF81BE78439139ED65FF72D6955015D743756836178D9A36C1A8A57A60C8F8)

## Example 20: Configuring Automatic Spacing Between Chinese and Western Text

This example shows how to configure automatic spacing between Chinese and Western characters using the [enableAutoSpacing](#enableautospacing20) attribute, available since API version 20.

// xxx.ets
@Entry
@Component
struct TextAreaExample {
  build() {
    Row() {
      Column() {
        Text('Automatic spacing: Enabled').margin(5)
        TextArea({text: '中文 Text'})
          .enableAutoSpacing(true)
        Text('Automatic spacing: Disabled').margin(5)
        TextArea({text: '中文Text'})
          .enableAutoSpacing(false)
      }.height('100%')
    }
    .width('60%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/DjFWGnjzQjyMCB6-B5ybWg/en-us_image_0000002568765375.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D1F47E1AD2F58F442BE5253450ED6FBA014BB026C3C602589BE6E924BBC85517)

## Example 21: Setting the Maximum Number of Lines

This example shows how to set the maximum number of lines using the [maxLines](#maxlines20) attribute, available since API version 20. The text becomes scrollable when the maximum number of lines is exceeded.

// xxx.ets
@Entry
@Component
struct TextAreaExample {
  build() {
    Row() {
      Column() {
        TextArea({ text: '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20' })
          .fontSize(50)
          .width('50%')
          .borderWidth(1)
          .margin(100)
          .textOverflow(TextOverflow.Clip)
          .maxLines(3, { overflowMode: MaxLinesMode.SCROLL })
      }.height('90%')
    }
    .width('90%')
    .margin(10)
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/xm9hFU9VSmS8Oz-B8dR3Mw/en-us_image_0000002537765650.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2B81E8167BE2045F6EC336199A8DC959FCAFC502487498A3B0B96173F77AEA8D)

## Example 22: Setting the Minimum Number of Lines

This example shows how to set the minimum number of lines using the [minLines](#minlines20) attribute, available since API version 20.

// xxx.ets
@Entry
@Component
struct Index {
  @State message: string = 'Hello World';

  build() {
    Row() {
      Column() {
        TextArea({ text: this.message })
          .width('95%')
          .fontSize(20)
          .margin(10)
          .minLines(3)
      }
    }
    .width('90%')
    .margin(10)
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/CR3EHlxvQ2WxNBEmX0isGg/en-us_image_0000002537925590.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1E647DD00D2E1E60F27527EFF7086D5DB9631439C1E2C6457DDB585291DFF9F5)

## Example 23 Setting the Normal and Overflow Colors of the Character Counter

This example demonstrates how to set the normal and overflow colors of the character counter using the **counterTextColor** and **counterTextOverflowColor** parameters (available since API version 22) of the [showCounter](#showcounter10) attribute.

import { ColorMetrics } from '@kit.ArkUI';

// xxx.ets
@Entry
@Component
struct TextAreaExample {
  @State text: string = '';
  controller: TextAreaController = new TextAreaController();

  build() {
    Column() {
      TextArea({
        text: this.text,
        placeholder: 'The text area can hold an unlimited amount of text. input your word...',
        controller: this.controller
      })
        .placeholderFont({ size: 16, weight: 400 })
        .width(336)
        .height(56)
        .margin(20)
        .fontSize(16)
        .fontColor('#182431')
        .backgroundColor('#FFFFFF')
        .maxLength(4)
        .showCounter(true, {
          thresholdPercentage: 50,
          highlightBorder: true,
          counterTextColor: ColorMetrics.resourceColor(Color.Red),
          counterTextOverflowColor: ColorMetrics.resourceColor(Color.Orange)
        })
    }.width('100%').height('100%').backgroundColor('#F1F3F5')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/0FOVlAH2QuKy0vQwURFHdA/en-us_image_0000002568685367.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=12E0EF59288B2075B631758E7277BC41F8740A860EEA09729D9DCBA8AF415AE8)

## Example 24 Setting the Scrollbar Color

This example demonstrates how to set the color of the scrollbar using the [scrollBarColor](#scrollbarcolor22) attribute, available since API version 22.

// xxx.ets
import { ColorMetrics } from '@kit.ArkUI';
@Entry
@Component
struct Index {
  controller: TextAreaController = new TextAreaController();
  build() {
      Column() {
        TextArea({
          text: "Hello World TextArea\\nHello World TextArea\\nHello World TextArea\\nHello World TextArea",
          placeholder: 'Type to text area...',
          controller: this.controller
        })
          .width(336)
          .height(56)
          .margin({bottom:5})
          .fontSize(16)
          .fontColor('#182431')
          .backgroundColor('#FFFFFF')
          .barState(BarState.On)
          .scrollBarColor(undefined)
        TextArea({
          text: "Hello World TextArea\\nHello World TextArea\\nHello World TextArea\\nHello World TextArea",
          placeholder: 'Type to text area...',
          controller: this.controller
        })
          .width(336)
          .height(56)
          .margin({bottom:5})
          .fontSize(16)
          .fontColor('#182431')
          .backgroundColor('#FFFFFF')
          .barState(BarState.On)
          .scrollBarColor(ColorMetrics.resourceColor(Color.Orange))
        TextArea({
          text: "Hello World TextArea\\nHello World TextArea\\nHello World TextArea\\nHello World TextArea",
          placeholder: 'Type to text area...',
          controller: this.controller
        })
          .width(336)
          .height(56)
          .margin({bottom:5})
          .fontSize(16)
          .fontColor('#182431')
          .backgroundColor('#FFFFFF')
          .barState(BarState.On)
          .scrollBarColor(ColorMetrics.rgba(255, 100, 255))
      }
      .backgroundColor(Color.Blue).width('100%').height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/kepdI5EvTPaE7QmT2ZX3Cg/en-us_image_0000002568765377.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0773D387EB4887A89808F3E8CA2E0088F60EF3836ABE30616C6AA7A1F709E27D)

## Example 25: Setting the Placeholder Rich Text Style

This example demonstrates how to set the placeholder rich text style using the [setStyledPlaceholder](../text-box-component-common-apis/document.md#setstyledplaceholder22) API, available since API version 22.

// xxx.ets
import { LengthMetrics } from '@kit.ArkUI';

@Entry
@Component
struct TextAreaExample {
  styledString: MutableStyledString =
    new MutableStyledString("段落标题\\n正文第一段\\n正文第二段indent 40 vp\\n正文第三段textAlign居中对齐",
      \[
        {
          start: 0,
          length: 4,
          styledKey: StyledStringKey.FONT,
          styledValue: new TextStyle({ fontSize: LengthMetrics.vp(24), fontWeight: FontWeight.Bolder })
        },
        {
          start: 5,
          length: 5,
          styledKey: StyledStringKey.FONT,
          styledValue: new TextStyle({ fontColor: Color.Gray })
        },
        {
          start: 11,
          length: 1,
          styledKey: StyledStringKey.PARAGRAPH\_STYLE,
          styledValue: new ParagraphStyle({
            textIndent: LengthMetrics.vp(40),
            maxLines: 1,
            overflow: TextOverflow.Ellipsis
          })
        },
        {
          start: 29,
          length: 1,
          styledKey: StyledStringKey.PARAGRAPH\_STYLE,
          styledValue: new ParagraphStyle({
            textAlign: TextAlign.Center
          })
        }
      \]);
  controller: TextAreaController = new TextAreaController();

  aboutToAppear() {
    this.controller.setStyledPlaceholder(this.styledString)
  }

  build() {
    Scroll() {
      Column() {
        Text("TextArea placeholder富文本")
          .fontSize(8)
        TextArea({ controller: this.controller })
          .width(200)
          .fontSize(24)
          .margin(10)
      }
      .width('100%')
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/ONtUq4aZTluE56w64Z5ddg/en-us_image_0000002537765652.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4C72D5FA1B4E6EFAD5711DA65115A85443E226D001E25800686F55EB59A98A44)

## Example 26 Setting Input Method Extension Information

This example demonstrates how to set input method extension information using the **setExtraConfig** method of [IMEClient](../text-component-common-apis/document.md#imeclient20), available since API version 22.

// xxx.ets
@Entry
@Component
struct TextAreaExample {
  build() {
    Column() {
      TextArea({ text: 'Execute the onWillAttachIME callback before starting the input method.'})
        .onWillAttachIME((client: IMEClient) => {
          client.setExtraConfig({
            customSettings: {
              name: "TextArea", // Custom property
              id: client.nodeId // Custom property
            }
          })
        })
    }.height('100%')
  }
}
