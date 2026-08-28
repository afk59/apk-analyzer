# TextInput

The **TextInput** component provides single-line text input.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/YtvZvQ8tRvGWr-dPl34EoQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B4379D23C22A5DDA736C1F0A7783D3CD5D98F9CB6380B82CC38EA3DC84BF1C6B)

This component is supported since API version 7. Updates will be marked with a superscript to indicate their earliest API version.

This component supports plain text only. For rich text, use the [RichEditor](../richeditor/document.md) component.

#### Child Components

Not supported

#### APIs

TextInput(value?: TextInputOptions)

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [TextInputOptions](#textinputoptions) | No | Parameters of the **TextInput** component. |

#### TextInputOptions

**TextInput** initialization parameters.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| placeholder | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | Text displayed when there is no input. |
| text | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 
Current text input.

You are advised to bind the state variable to the text in real time through the **onChange** event, so as to prevent display errors when the component is updated.

Since API version 10, this parameter supports two-way binding through [$$](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-two-way-sync).

Since API version 18, this parameter supports two-way binding through [!!](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-new-binding#two-way-binding-between-built-in-component-parameters).

 |
| controller8+ | [TextInputController](#textinputcontroller8) | No | Yes | Text input controller. |

#### Attributes

In addition to the [universal attributes](../../universal-attributes/document.md), the following attributes are supported.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/dy_PiGZsRY-3Ckg0SUYLAA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=34F80D0D9000C2623219E88029D5399CF21662088F5C6748C010B8EF55A7920F)

When no underline is set, the default value of the universal attribute [padding](../../universal-attributes/layout-and-borders/sizing/document.md#padding) is as follows:

{

top: '8vp',

right: '16vp',

bottom: '8vp',

left: '16vp'

}

When an underline is set, the default value of **padding** is as follows:

{

top: '12vp',

right: '0vp',

bottom: '12vp',

left: '0vp'

}

When **padding** is set to **0** for the text input box, you can set [borderRadius](../../universal-attributes/layout-and-borders/border-styling/document.md#borderradius) to **0** to prevent the caret from being clipped. If the caret is displayed abnormally at the edge of the text box, check whether it is caused by the **padding** or **borderRadius** attribute.

Since API version 10, **.width('auto')** can be set for the **TextInput** component to adapt its width to the text width. During adaptation, the component width is subject to the **constraintSize** attribute and the maximum and minimum width constraints passed from the parent container. For details, see [Sizing](../../universal-attributes/layout-and-borders/sizing/document.md).

#### \[h2\]type

type(value: InputType)

Sets the text box type.

Different **InputType** values trigger corresponding keyboard types and enforce input restrictions.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [InputType](#inputtype) | Yes | 
Text box type.

Default value: **InputType.Normal**

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/rVmKBfvVTLOoJ8f5DHShXw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D59765B2F9C2CAD05328F10B5981EA320C9C860F3B60A48E1AA9033ABC0971A6)

The password filling service requires a specific input box type.For details about how to use the password filling service, see [Quick Adaptation](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/passwordvault-quick-adaptation).

In the [password mode](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-common-components-text-input#password-mode), the decoration line [decoration](#decoration12) and underline [showUnderline](#showunderline10) have no effect.

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

Default value on wearables: **'#99ffffff'**

 |

#### \[h2\]placeholderFont

placeholderFont(value?: Font)

Sets the placeholder text style, including the font size, font weight, font family, and font style.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [Font](../../common-definitions/basic-types/document.md#font) | No | 
Placeholder text style.

Default value on wearables: **18fp**

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/AAvSiAKMSdC-3XTFPchwOA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=05430274C1C992F9EEDFF092FA06557B51104EE53CF08B4068447A1A8E7BDC9C)

You are advised to use [loadFontSync](../../../../../graphics/arkgraphics-2d/arkts-apis/ohos-graphics-text-text/document.md#loadfontsync) to register custom fonts.

#### \[h2\]enterKeyType

enterKeyType(value: EnterKeyType)

Sets the type of the Enter key.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [EnterKeyType](#enterkeytype) | Yes | 
Type of the Enter key.

Default value: **EnterKeyType.Done**

 |

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/FqM2x-MkSnCZv-ke8PufBA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1359CD25E7215F4C9EC20084475A8456429BCAB28D799B733F2C287F688121C8)

Since API version 12, this API can be used to set the text handle color, which is the same as the caret color.

#### \[h2\]maxLength

maxLength(value: number)

Sets the maximum number of characters for text input.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | Yes | 
Maximum number of characters for text input.

Default value: **Infinity**, indicating that there is no upper limit on the number of characters that can be entered

**NOTE**

If this attribute is not set or set to an invalid value, the default value is used. If a decimal value is provided, only its integer part is applied. If the value exceeds 2^31-1, exceptions may occur.

 |

#### \[h2\]fontColor

fontColor(value: ResourceColor)

Sets the font color.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | Yes | 
Font color.

Default value on wearables: \*\*'#dbffffff' \*\*

 |

#### \[h2\]fontSize

fontSize(value: Length)

Sets the font size.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [Length](../../common-definitions/basic-types/document.md#length) | Yes | 
Font size. If **fontSize** is of the number type, the unit fp is used. The default font size is 16 fp. The value cannot be a percentage.

Default value on wearables: **18fp**

 |

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

The 'HarmonyOS Sans' font and custom fonts are supported for applications.

Only the **'HarmonyOS Sans'** font is supported for widgets.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/SjobxF-PRJO3HCaxxfivYw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5D2C1F435E46640E76D627A05B96FA60F03E07E2F8DC113BE64376724AC27D2F)

You are advised to use [loadFontSync](../../../../../graphics/arkgraphics-2d/arkts-apis/ohos-graphics-text-text/document.md#loadfontsync) to register custom fonts.

#### \[h2\]inputFilter8+

inputFilter(value: ResourceStr, error?: Callback<string>)

Sets the regular expression for input filtering. Only inputs that comply with the regular expression can be displayed. Other inputs are filtered out.

For single-character input scenarios, only single-character matching is supported; for multi-character input scenarios (such as pasting), string matching is supported.

Since API version 11, setting **inputFilter** with a non-empty string invalidates the text filtering effect attached to the [type](#type) API.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | Yes | Regular expression. |
| error | Callback<string> | No | Filtered-out content to return when regular expression matching fails. |

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

#### \[h2\]showPasswordIcon9+

showPasswordIcon(value: boolean)

Sets whether to display the password icon at the end of the password text box.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | boolean | Yes | 
Whether to display the password icon at the end of the password text box.

**true** to display, **false** otherwise.

Default value: **false** for TV devices; **true** for other devices

 |

#### \[h2\]style9+

style(value: TextInputStyle | TextContentStyle)

Sets the text input style. The inline style only supports **InputType.Normal**.

For details about the text box types, see [type](#type).

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [TextInputStyle](#textinputstyle9) | [TextContentStyle](../../common-definitions/enums/document.md#textcontentstyle10) | Yes | 
Text input style.

Default value: **TextInputStyle.Default**

 |

#### \[h2\]textAlign9+

textAlign(value: TextAlign)

Sets the horizontal alignment of the text.

Available options are **TextAlign.Start**, **TextAlign.Center**, and **TextAlign.End**. **TextAlign.JUSTIFY** behaves the same as **TextAlign.Start**.

The vertical position of the text paragraph can be controlled by the [align](../../universal-attributes/layout-and-borders/location/document.md#align) attribute, but the horizontal position cannot be controlled by **align** in this component.

-   **Alignment.TopStart**, **Alignment.Top**, **Alignment.TopEnd**: Content aligns to the top.
    
-   **Alignment.Start**, **Alignment.Center**, **Alignment.End**: Content is centered vertically.
    
-   **Alignment.BottomStart**, **Alignment.Bottom**, **Alignment.BottomEnd:** Content aligns to the bottom.
    

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [TextAlign](../../common-definitions/enums/document.md#textalign) | Yes | 
Horizontal alignment of the text.

Default value: **TextAlign.Start**

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/Aj5tDDUfQbCRwo0_wN6W8w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B73E39326D9F68FE8F2ED10D53693A1A9A877BC96AD537E0F8D751A1EC724BB2)

**textAlign** only adjusts the overall text layout and does not affect character display order. For character display order adjustment, see [Bidirectional Text Layout and Alignment](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-internationalization#bidirectional-text-layout-and-alignment).

#### \[h2\]selectedBackgroundColor10+

selectedBackgroundColor(value: ResourceColor)

Sets the background color of the selected text. If the opacity is not set, a 20% opacity will be used.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | Yes | Background color of the selected text. |

#### \[h2\]caretStyle10+

caretStyle(value: CaretStyle)

Sets the caret style.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [CaretStyle](../text-component-common-apis/document.md#caretstyle10) | Yes | Caret style. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/FfrUCs-5SP6NSE575WvDog/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=05CEFE6BA0D93D8BD6DDED17E8C14FEB0FD99C6CC628A37812C6D0242D14BD95)

When the **color** parameter is configured in both the **caretColor** and **caretStyle** attributes, the later-set value takes precedence.

Since API version 12, this API can be used to set the text handle color, which is the same as the caret color.

#### \[h2\]caretPosition10+

caretPosition(value: number)

Sets the caret position.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | Yes | 
Caret position.

The position before the first character is 0.

 |

#### \[h2\]showUnit10+

showUnit(value: CustomBuilder)

Sets the unit displayed with the text box. This attribute effective only when [showUnderline](#showunderline10) is set to **true**.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [CustomBuilder](../../common-definitions/basic-types/document.md#custombuilder8) | Yes | Unit displayed with the text box. |

#### \[h2\]showError10+

showError(value?: ResourceStr | undefined)

Sets the error message displayed when an error occurs.

If the data type is **ResourceStr** and the input content does not comply with specifications, the error message is displayed. If the error message does not fit in one line, an ellipsis (…) is displayed to represent clipped text. If the data type is **undefined**, no error message is displayed. For details, see [Example 2](#example-2-setting-underlines).

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | undefined | No | 
Error message displayed when an error occurs.

By default, no error message is displayed.

On wearables, the font size is 13 fp and the alignment mode is center alignment.

**NOTE**

The Resource type is supported since API version 12.

 |

#### \[h2\]showUnderline10+

showUnderline(value: boolean)

Sets whether to enable an underline.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | boolean | Yes | 
Whether to enable an underline.

**true** to enable, **false** otherwise.

Default value: **false**

By default, the underline comes in the color of **'#33182431'**, thickness of 1 px, and text box size of 48 vp. The underline is only available for the **InputType.Normal** type.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/eIVOeEuDSPCavj61sNHXLA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=34ECFC74EC71CCD8365D237C8B4396DCDB8DF6EA2A338C5CD413F1A1C531160E)

In the [password mode](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-common-components-text-input#password-mode), the decoration line [decoration](#decoration12) and underline [showUnderline](#showunderline10) have no effect.

#### \[h2\]passwordIcon10+

passwordIcon(value: PasswordIcon)

Sets the password icon to display at the end of the password text box.

Images in JPG, PNG, BMP, HEIC, and WEBP formats are supported.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [PasswordIcon](#passwordicon10) | Yes | 
Password icon to display at the end of the password text box.

By default, the system-provided icon is used.

The icon size is fixed at 24 vp (or 28 vp on wearables), regardless of the source image size.

 |

#### \[h2\]enableKeyboardOnFocus10+

enableKeyboardOnFocus(value: boolean)

Sets whether to pop up the soft keyboard when the **TextInput** component obtains focus in a way other than clicking.

Since API version 10, the **TextInput** component is bound to the input method by default when it obtains focus.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | boolean | Yes | 
Whether to pop up the soft keyboard when the **TextInput** component obtains focus in a way other than clicking.

**true**: The soft keyboard pops up. **false**: The soft keyboard does not pop up.

Default value: **false** for TV devices; **true** for other devices

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

**true**: The system text selection menu is hidden when a user clicks the text box cursor, long-presses the text box, double-taps the text box, triple-taps the text box, or right-clicks the text box.

**false**: The system text selection menu is displayed.

Default value: **false**

 |

#### \[h2\]barState10+

barState(value: BarState)

Sets the scrollbar display mode for the inline style in the editing state.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [BarState](../../common-definitions/enums/document.md#barstate) | Yes | 
Scrollbar display mode for the inline style in the editing state.

Default value: **BarState.Auto**

 |

#### \[h2\]maxLines10+

maxLines(value: number)

Sets the maximum number of lines that can be displayed with the inline style in the editing state.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | Yes | 
Maximum number of lines that can be displayed with the inline style in the editing state.

Default value: **3**

Value range: (0, UINT32\_MAX\]

 |

#### \[h2\]customKeyboard10+

customKeyboard(value: CustomBuilder | ComponentContent | undefined, options?: KeyboardOptions)

Sets a custom keyboard.

When a custom keyboard is set, activating the text box opens the specified custom component, instead of the system input method.

The custom keyboard's height can be set through the **height** attribute of the custom component's root node, and its width is fixed at the default value.

The custom keyboard is presented by overlaying the original screen, which is not compressed or lifted if avoid mode is not enabled or avoidance is not needed for the text box.

The custom keyboard cannot obtain the focus, but it blocks gesture events.

By default, the custom keyboard is closed when the input component loses the focus. You can also use the [TextInputController](#textinputcontroller8).[stopEditing](#stopediting10) API to close the keyboard.

When setting a custom keyboard, you can bind the [onKeyPrelme](../../universal-events/basic-input-events/key-event/document.md#onkeypreime12) event to prevent input from the physical keyboard.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/KwVOtCSPSfScd6ORdTmoMg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7560A8FAA8800E35BF2A1278F6DA2BED9B8B5F654D0B94430CCBB8793614C6B5)

This API cannot be called within [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier).

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [CustomBuilder](../../common-definitions/basic-types/document.md#custombuilder8) | [ComponentContent](../../../arkts-api/ui/arkui/componentcontent/document.md#componentcontent-1)22+ | undefined22+ | Yes | Custom keyboard. If the value is **undefined**, the custom keyboard is closed. |
| options12+ | [KeyboardOptions](../richeditor/document.md#keyboardoptions12) | No | Whether to support keyboard avoidance. |

#### \[h2\]enableAutoFill11+

enableAutoFill(value: boolean)

Sets whether to enable autofill.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | boolean | Yes | 
Whether to enable autofill.

**true** to enable; **false** otherwise.

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

#### \[h2\]passwordRules11+

passwordRules(value: string)

Defines the rules for generating passwords. When autofill is used, these rules are transparently transmitted to Password Vault for generating a new password.

For details, see [Suggestions on Automatically Generating Strong Passwords for Applications](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/passwordvault-custom-strong-password-rules).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | string | Yes | Rules for generating passwords. |

#### \[h2\]cancelButton11+

cancelButton(options: CancelButtonOptions)

Sets the style of the cancel button on the right. Only icons of the image type are supported. The [inline style](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-common-components-text-input#inline-style) is not supported. For details, see [Example 4 Customizing the Cancel Button Style on the Right](#example-4-customizing-the-cancel-button-style-on-the-right).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [CancelButtonOptions](../search/document.md#cancelbuttonoptions12) | Yes | 
Options of the cancel button on the right.

Default value:

{

style: CancelButtonStyle.INPUT

}

Default value on wearables: **28vp**

 |

#### \[h2\]selectAll11+

selectAll(value: boolean)

Sets whether to select all text in the initial state. The [inline style](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-common-components-text-input#inline-style) is not supported.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | boolean | Yes | 
Whether to select all text in the initial state.

**true**: Selecting all text is enabled. **false**: Selecting all text is disabled.

Default value: **false**

 |

#### \[h2\]showCounter11+

showCounter(value: boolean, options?: InputCounterOptions)

Sets the character counter displayed when the number of characters entered exceeds the threshold. If the **showCounter** API is not called, the character counter is not displayed by default.

**options** can be set only when **value** is set to **true**, in which case a character counter is displayed below the text box. This attribute must be used together with [maxLength](#maxlength). The character counter is displayed in this format: Number of characters entered/Character limit.

It is visible when the number of characters entered is greater than the character limit multiplied by the threshold percentage value. If **options** is not set, the text box border and character counter subscript turn red when the number of characters entered exceeds the limit. If **value** is set to **true** and [InputCounterOptions](../text-box-component-common-apis/document.md#inputcounteroptions11) is set, the text box border and character counter subscript turn red and the text box shakes when the number of characters entered reaches the limit, provided that the value of **thresholdPercentage** is valid. If **highlightBorder** is set to **false**, the text box border does not turn red. By default, **highlightBorder** is set to **true**.

The character counter is not displayed in the [inline style](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-common-components-text-input#inline-style) and [password mode](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-common-components-text-input#password-mode).

[Example 5: Setting a Character Counter](#example-5-setting-a-character-counter) shows the effect of setting **showCounter**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/ngtNyxrHQVuy-gNkT5XR0g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1E61D9D2B50C9216E0353690AB8FD2BF91A3EED7CE90EE514C8B604D46DD0B90)

This API can be called within [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier) since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | boolean | Yes | 
Whether to display the character counter.

**true**: Character counter is displayed. **false**: Character counter is not displayed.

 |
| options | [InputCounterOptions](../text-box-component-common-apis/document.md#inputcounteroptions11) | No | Configuration options for the character counter. |

#### \[h2\]contentType12+

contentType(value: ContentType)

Sets the content type for autofill.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ContentType](#contenttype12) | Yes | Content type for autofill. |

#### \[h2\]underlineColor12+

underlineColor(value: ResourceColor|UnderlineColor|undefined)

Color of the underline.

When [showUnderline](#showunderline10) is enabled, the underline color can be configured.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | [UnderlineColor](#underlinecolor12) | undefined | Yes | 
Color of the underline.

The underline color changes with the underline mode. If the underline color is only set for the normal state, you can directly enter a value of the ResourceColor type. If the value specified is **undefined**, **null**, or invalid, all underlines are restored to the default value.

Default value: underline color configured for the theme. The default underline color in the theme is **'#33182431'**.

 |

#### \[h2\]lineHeight12+

lineHeight(value: number | string | Resource)

Sets the text line height.

If the value is less than or equal to **0**, the line height is unrestricted and adapts to the font size. When the value is a number, the unit is fp. For the string type, numeric string values with optional units, for example, **"10"** or **"10fp"**, are supported.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/08/v3/HMAoeylgSGmlt3LtuKHreQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=911074891A5E7DCFB8B964E2EA6138011871C12196DEBEF8EB837C825698E8A7)

-   If certain characters have significantly taller glyphs than others in the same line, layout anomalies such as clipping, overlapping, or misalignment may occur. In this case, adjust component attributes such as height and line height to ensure proper layout rendering.
    
-   When the [password mode](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-common-components-text-input#password-mode) is set, [lineHeight](#lineheight12) set by this API does not take effect.
    

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | string | [Resource](../../common-definitions/basic-types/document.md#resource) | Yes | Text line height. |

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/rAJaLTZiRX-7ukcXYSwssQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=085EC051184C22BD860FEA3D3DC175E58593C82F4270BCAD99B1BC0E248CA36A)

When the bottom contour of a character intersects with the decoration, underline avoidance is triggered, commonly affecting characters like "g", "j", "y", "q", and "p".

If the decoration color is set to **Color.Transparent**, it inherits the text color of the first character in each line. If the decoration color is set to **"#00FFFFFF"**, the line becomes fully transparent.

In the [password mode](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-common-components-text-input#password-mode), the decoration line [decoration](#decoration12) and underline [showUnderline](#showunderline10) have no effect.

#### \[h2\]letterSpacing12+

letterSpacing(value: number | string | Resource)

Sets the letter spacing for a text style. If the value specified is a percentage or **0**, the default value is used. For the string type, numeric string values with optional units, for example, **"10"** or **"10fp"**, are supported.

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

For more information about the font features, see [Low-level font feature settings control: the font-feature-settings property](https://www.w3.org/TR/css-fonts-3/#font-feature-settings-prop) and [The Complete CSS Demo for OpenType Features](https://sparanoid.com/lab/opentype-features/).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/PfJdlNSnRUGHmkUpj9XCjQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F95A5E721189847B78EE5FC57B7A1CD2D49F90D0627AECE0AF7E34C06B52E88D)

When the [password mode](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-common-components-text-input#password-mode) is set, the **fontFeature** attribute cannot be used to set the text style.

#### \[h2\]wordBreak12+

wordBreak(value: WordBreak)

Sets the word break rule. This attribute takes effect when the [inline style](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-common-components-text-input#inline-style) is set for the component, but has no effect on placeholder text.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [WordBreak](../../common-definitions/enums/document.md#wordbreak11) | Yes | 
Word break rule in the inline style.

Default value: **WordBreak.BREAK\_WORD**

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/5TtOAkbPRbi3OcQxg1QdDw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=60DC882FFBBCCE479401BA851CEF45F02DB5B56814A4C3474FFB14CF19A5EDB3)

The component does not support the **clip** attribute. Therefore, setting this attribute does not affect text clipping.

#### \[h2\]textOverflow12+

textOverflow(value: TextOverflow)

Sets the display mode for overflowing text. This attribute is supported only in the editing and non-editing states of the [inline style](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-common-components-text-input#inline-style).

Chinese text is truncated by character. English text is truncated by word. To truncate English text by letter, set **wordBreak** to **WordBreak.BREAK\_ALL**.

When **overflow** is set to **TextOverflow.None**, the effect is the same as **TextOverflow.Clip**.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [TextOverflow](../../common-definitions/enums/document.md#textoverflow) | Yes | 
Display mode of overflowing text.

Default value for the [inline style](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-common-components-text-input#inline-style) in the non-editing state: **TextOverflow.Ellipsis**

Default value for the inline style in the editing state: **TextOverflow.Clip**

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/mAynS-V0QEKeWFejcldUJw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4059E946D1192D51BDD4A61D55BEB91A10F169A1C78ECAA8D2764FB86BFEFD6E)

The **TextInput** component does not support the **TextOverflow.MARQUEE** mode. When the **TextOverflow.MARQUEE** mode is set, the **TextOverflow.Ellipsis** mode is used for the non-editing state of the [inline style](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-common-components-text-input#inline-style), and **TextOverflow.Clip** mode is used for the editing state of the inline style as well as for the non-inline mode.

If inline mode is not set, the text displays in the default style, and any **textOverflow** setting will not take effect.

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

#### \[h2\]minFontSize12+

minFontSize(value: number | string | Resource)

Sets the minimum font size. For the string type, numeric string values with optional units, for example, **"10"** or **"10fp"**, are supported.

This attribute takes effect only when used together with [maxFontSize](#maxfontsize12) and [maxLines](#maxlines10) (for the editing state of the inline style), or layout constraint settings.

When the adaptive font size is used, the **fontSize** settings do not take effect.

If the value of **minFontSize** is less than or equal to 0, the adaptive font sizing feature is disabled. In such cases, the [fontSize](#fontsize) attribute is used instead. If **fontSize** is not set, the default value will apply.

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

This attribute takes effect only when used together with [minFontSize](#minfontsize12) and [maxLines](#maxlines10) (for the editing state of the inline style), or layout constraint settings.

When the adaptive font size is used, the **fontSize** settings do not take effect.

If the value of **maxFontSize** is less than or equal to 0 or is less than the value of **minFontSize**, the adaptive font sizing feature is disabled. In such cases, the [fontSize](#fontsize) attribute is used instead. If **fontSize** is not set, the default value will apply.

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

Sets how the adaptive height is determined for the text in the inline style.

When this attribute is set to **TextHeightAdaptivePolicy.MAX\_LINES\_FIRST**, the [maxLines](#maxlines10) attribute takes precedence for adjusting the text height. If the **maxLines** setting results in a layout beyond the layout constraints, the text will shrink to a font size between [minFontSize](#minfontsize12) and [maxFontSize](#maxfontsize12) to allow for more content to be shown.

If this attribute is set to **TextHeightAdaptivePolicy.MIN\_FONT\_SIZE\_FIRST**, the **minFontSize** attribute takes precedence for adjusting the text height. If the text can fit in one line with the **minFontSize** setting, the text will enlarge to the maximum available font size between **minFontSize** and **maxFontSize**.

**TextHeightAdaptivePolicy.LAYOUT\_CONSTRAINT\_FIRST** produces the same effect as **TextHeightAdaptivePolicy.MIN\_FONT\_SIZE\_FIRST**.

When the component is in the non-inline style, the three values of **TextHeightAdaptivePolicy** have the same effect, that is, the text will shrink to a font size between **minFontSize** and **maxFontSize** to allow for more content to be shown.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/XGz-RCCTQ_CPHrAkkCPtNg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=41999D9317D3207B0503F586641F2C927D4EA42B8ECF29C674237CB8B0753BC4)

If the text box is in the inline style, the font size in the editing state is different from that in the non-editing state.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [TextHeightAdaptivePolicy](../../common-definitions/enums/document.md#textheightadaptivepolicy10) | Yes | 
How the adaptive height is determined for the text.

Default value: **TextHeightAdaptivePolicy.MAX\_LINES\_FIRST**

 |

#### \[h2\]showPassword12+

showPassword(visible: boolean)

Sets whether to show the password.

This API has effect only when the [input type](#inputtype) is set to **Password**, **NEWPASSWORD**, or **NUMBERPASSWORD** mode. It does not work in other modes.

In the [password mode](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-common-components-text-input#password-mode), inconsistencies between the backend state of the text box and the frontend application's state management variables may cause abnormal behavior of the trailing icon. To avoid such issues, use the [onSecurityStateChange](#onsecuritystatechange12) callback to sync the states. For details, see [Example 1: Setting and Obtaining the Caret Position](#example-1-setting-and-obtaining-the-caret-position).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| visible | boolean | Yes | 
Whether to show the password.

**true**: The password is shown. **false**: The password is not shown.

Default value: **false**

 |

#### \[h2\]lineBreakStrategy12+

lineBreakStrategy(strategy: LineBreakStrategy)

Sets the line break rule. This attribute takes effect when **wordBreak** is not set to **breakAll**. Hyphens are not supported.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| strategy | [LineBreakStrategy](../../common-definitions/enums/document.md#linebreakstrategy12) | Yes | 
Line break rule.

Default value: **LineBreakStrategy.GREEDY**

**NOTE**

This attribute takes effect only when the [inline style](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-common-components-text-input#inline-style) is set.

 |

#### \[h2\]editMenuOptions12+

editMenuOptions(editMenu: EditMenuOptions)

Sets the extended options of the custom menu, including the text content, icon, and callback.

When [disableMenuItems](../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-textmenucontroller/document.md#disablemenuitems20) or [disableSystemServiceMenuItems](../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-textmenucontroller/document.md#disablesystemservicemenuitems20) is used to disable system service menu items in the text selection menu, the disabled menu options will be excluded from the parameter list in the [onCreateMenu](../text-component-common-apis/document.md#oncreatemenu12) callback of **editMenuOptions**.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| editMenu | [EditMenuOptions](../text-component-common-apis/document.md#editmenuoptions) | Yes | Extended options of the custom menu. |

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/OT32Ae8nQ2OmP4BMBjYwlw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AD05CA3392449BCE10DB66BE76EF66CE6202EA2B373E2F104BD01C9D2B3C7A10)

Preview text represents a temporary, uncommitted input state. This feature requires support from the input method with pre-commit text functionality enabled. During text entry, when candidate words have not been confirmed yet, the text box displays marked text in a provisional state. For example, when users enter Chinese using Pinyin input, the Pinyin letters appear in the input box before a word is selected from the candidate word list. This intermediate state constitutes preview text.

#### \[h2\]enableHapticFeedback13+

enableHapticFeedback(isEnabled: boolean)

Sets whether to enable haptic feedback.

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

**true**: Haptic feedback is enabled. **false**: Haptic feedback is disabled.

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

Values < 0: solid text.

Values > 0: outlined text.

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

Default value: **true** Invalid values are treated as the default value.

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

A value less than 0 is handled as **0**. A value greater than 1 is handled as **1**. Invalid values are not applied by default.

Before use, you need to configure the [configuration.json](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-configuration-file#tags-in-the-configuration-file) and [app.json5](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-configuration-file) files in the project. For details, see [Example 18: Setting the Minimum and Maximum Font Scale Factors](#example-18-setting-the-minimum-and-maximum-font-scale-factors).

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

Values less than 1 are treated as **1**. Invalid values are not applied by default.

After the **maxFontScale** attribute is set, the error message set by **showError** can be enlarged to a maximum of twice the original size.

Before use, you need to configure the [configuration.json](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-configuration-file#tags-in-the-configuration-file) and [app.json5](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-configuration-file) files in the project. For details, see [Example 18: Setting the Minimum and Maximum Font Scale Factors](#example-18-setting-the-minimum-and-maximum-font-scale-factors).

 |

#### \[h2\]cancelButton18+

cancelButton(symbolOptions: CancelButtonSymbolOptions)

Sets the style of the cancel button on the right. Only symbol-type icons are supported. The [inline style](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-common-components-text-input#inline-style) is not supported. For details, see [Example 15: Setting a Symbol-Type Cancel Button](#example-15-setting-a-symbol-type-cancel-button).

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| symbolOptions | [CancelButtonSymbolOptions](../search/document.md#cancelbuttonsymboloptions12) | Yes | 
Style of the cancel button on the right.

Default value:

{

style: CancelButtonStyle.INPUT

}

 |

#### \[h2\]ellipsisMode18+

ellipsisMode(mode: Optional<EllipsisMode>)

Sets the ellipsis position. The **ellipsisMode** attribute takes effect only in the [inline style](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-common-components-text-input#inline-style). It must be used together with **overflow** set to **TextOverflow.Ellipsis**. The **ellipsisMode** attribute does not take effect if set alone.

This attribute works normally in the non-editing state. In the editing state, **EllipsisMode.START** and **EllipsisMode.CENTER** take effect only when **maxLines** is set to **1**, while **EllipsisMode.END** takes effect normally.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| mode | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<[EllipsisMode](../../common-definitions/enums/document.md#ellipsismode11)\> | Yes | 
Ellipsis position.

Default value: **EllipsisMode.END**

 |

#### \[h2\]enableAutoFillAnimation20+

enableAutoFillAnimation(enabled: Optional<boolean>)

Sets whether to enable the autofill animation.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| enabled | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<boolean> | Yes | 
Whether to enable the autofill animation.

**true** to enable; **false** otherwise.

Default value: **true**

**NOTE**

When enabled, the animation takes effect only for text boxes where [InputType](#inputtype) is set to **Password**, **NEW\_PASSWORD**, or **NUMBER\_PASSWORD**.

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

#### InputType

Sets the single-line text box type.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| Normal | 0 | 
Normal input mode. In this mode, there is no special restriction on the input characters.

The inline style supports only the **InputType.Normal** type.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| Number | 2 | 

Digit input mode.

Negative numbers and decimals are not supported.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| PhoneNumber9+ | 3 | 

Phone number input mode.

In this mode, the following characters are allowed: digits, spaces, plus signs (+), hyphens (-), asterisks (\*), and number signs (#), opening parentheses ((), and closing parenthesis ()); the length is not limited.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| Email | 5 | 

Email address input mode.

This mode accepts only digits, letters, underscores (\_), dots (.), and the following special characters: ! # $ % & ' " \* + - / = ? ^ \` { | } ~ @ (which can only appear once)

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| Password | 7 | 

Password input mode.

The entered text is briefly displayed before turning to dots by default. Since API version 12, the entered text is directly displayed as dots on PCs and 2-in-1 devices.

The eye icon at the end of the input box is hidden by default on TV devices, and shown by default on other devices.

The [decoration](#decoration12), [showUnderline](#showunderline10), and [lineHeight](#lineheight12) attributes do not take effect in password input mode.

If Password Vault is enabled, autofill is available for the username and password.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| NUMBER\_PASSWORD11+ | 8 | 

Numeric password input mode.

The entered text is briefly displayed before turning to dots by default. Since API version 12, the entered text is directly displayed as dots on PCs and 2-in-1 devices.

The eye icon at the end of the input box is hidden by default on TV devices, and shown by default on other devices.

The password input mode does not support underlines. If Password Vault is enabled, autofill is available for the username and password.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| USER\_NAME11+ | 10 | 

User name input mode with no special restrictions.

If Password Vault is enabled, autofill is available for the username and password.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| NEW\_PASSWORD11+ | 11 | 

New password input mode with no special restrictions.

The entered text is briefly displayed before turning to dots by default. Since API version 12, the entered text is directly displayed as dots on PCs and 2-in-1 devices.

The eye icon at the end of the input box is hidden by default on TV devices, and shown by default on other devices.

If Password Vault is enabled, a new password can be automatically generated.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| NUMBER\_DECIMAL11+ | 12 | 

Number input mode with a decimal point.

The value can contain digits and only one decimal point. Negative decimals are not supported. For the input mode of negative decimals, use **inputFilter**.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| URL12+ | 13 | 

URL input mode with no special restrictions.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| ONE\_TIME\_CODE20+ | 14 | 

One-time code (verification code) input mode with no special restrictions.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |

#### ContentType12+

Enumerates the content types for autofill.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| USER\_NAME | 0 | 
Username. Password Vault, when enabled, can automatically save and fill in usernames.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| PASSWORD | 1 | 

Password. Password Vault, when enabled, can automatically save and fill in passwords.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| NEW\_PASSWORD | 2 | 

New password. Password Vault, when enabled, can automatically generate a new password.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| FULL\_STREET\_ADDRESS | 3 | 

Full street address. The scenario-based autofill feature, when enabled, can automatically save and fill in full street addresses.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| HOUSE\_NUMBER | 4 | 

House number. The scenario-based autofill feature, when enabled, can automatically save and fill in house numbers.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| DISTRICT\_ADDRESS | 5 | 

District and county. The scenario-based autofill feature, when enabled, can automatically save and fill in districts and counties.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| CITY\_ADDRESS | 6 | 

City. The scenario-based autofill feature, when enabled, can automatically save and fill in cities.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| PROVINCE\_ADDRESS | 7 | 

Province. The scenario-based autofill feature, when enabled, can automatically save and fill in provinces.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| COUNTRY\_ADDRESS | 8 | 

Country. The scenario-based autofill feature, when enabled, can automatically save and fill in countries.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| PERSON\_FULL\_NAME | 9 | 

Full name. The scenario-based autofill feature, when enabled, can automatically save and fill in full names.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| PERSON\_LAST\_NAME | 10 | 

Last name. The scenario-based autofill feature, when enabled, can automatically save and fill in last names.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| PERSON\_FIRST\_NAME | 11 | 

First name. The scenario-based autofill feature, when enabled, can automatically save and fill in first names.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| PHONE\_NUMBER | 12 | 

Phone number. The scenario-based autofill feature, when enabled, can automatically save and fill in phone numbers.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| PHONE\_COUNTRY\_CODE | 13 | 

Country code. The scenario-based autofill feature, when enabled, can automatically save and fill in country codes.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| FULL\_PHONE\_NUMBER | 14 | 

Phone number with country code. The scenario-based autofill feature, when enabled, can automatically save and fill in phone numbers with country codes.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| EMAIL\_ADDRESS | 15 | 

Email address. The scenario-based autofill feature, when enabled, can automatically save and fill in email addresses.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| BANK\_CARD\_NUMBER | 16 | 

Bank card number. The scenario-based autofill feature, when enabled, can automatically save and fill in bank card numbers.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| ID\_CARD\_NUMBER | 17 | 

ID card number. The scenario-based autofill feature, when enabled, can automatically save and fill in ID card numbers.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| NICKNAME | 23 | 

Nickname. The scenario-based autofill feature, when enabled, can automatically save and fill in nicknames.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| DETAIL\_INFO\_WITHOUT\_STREET | 24 | 

Address information without street address. The scenario-based autofill feature, when enabled, can automatically save and fill in address information without street addresses.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| FORMAT\_ADDRESS | 25 | 

Standard address. The scenario-based autofill feature, when enabled, can automatically save and fill in standard addresses.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| PASSPORT\_NUMBER18+ | 26 | 

Passport number. The scenario-based autofill feature, when enabled, can automatically save and fill in passport numbers.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| VALIDITY18+ | 27 | 

Passport validity period. The scenario-based autofill feature, when enabled, can automatically save and fill in passport validity periods.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| ISSUE\_AT18+ | 28 | 

Passport place of issue. The scenario-based autofill feature, when enabled, can automatically save and fill in the place of issue for passports.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| ORGANIZATION18+ | 29 | 

Invoice title. The scenario-based autofill feature, when enabled, can automatically save and fill in invoice titles.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| TAX\_ID18+ | 30 | 

Tax ID. The scenario-based autofill feature, when enabled, can automatically save and fill in tax IDs.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| ADDRESS\_CITY\_AND\_STATE18+ | 31 | 

Location. The scenario-based autofill feature, when enabled, can automatically save and fill in locations.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| FLIGHT\_NUMBER18+ | 32 | 

Flight number. Currently not supported for automatic saving and auto-filling.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| LICENSE\_NUMBER18+ | 33 | 

Driver's license number. Currently not supported for automatic saving and auto-filling.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| LICENSE\_FILE\_NUMBER18+ | 34 | 

Driver's license file number. Currently not supported for automatic saving and auto-filling.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| LICENSE\_PLATE18+ | 35 | 

License plate number. The scenario-based autofill feature, when enabled, can automatically save and fill in license plate numbers.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| ENGINE\_NUMBER18+ | 36 | 

Vehicle registration engine number. Currently not supported for automatic saving and auto-filling.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| LICENSE\_CHASSIS\_NUMBER18+ | 37 | 

Chassis number. Currently not supported for automatic saving and auto-filling.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |

#### TextInputStyle9+

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Description |
| :-- | :-- |
| Default | Default style. The caret width is fixed at 1.5 vp, and the caret height is subject to the background height and font size of the selected text. |
| Inline | 
Inline style. The background height of the selected text is the same as the height of the text box.

This style is used in scenarios where editing and non-editing states are obvious, for example, renaming in the file list view.

The **showError** attribute is not supported for this style.

In the [inline style](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-common-components-text-input#inline-style), text cannot be dragged into the text box.

 |

#### PasswordIcon10+

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| onIconSrc | string | [Resource](../../common-definitions/basic-types/document.md#resource) | No | Yes | 
Displays the icon when the password is toggled to visible in the password input mode.

The string type can be used to load network images and local images.

 |
| offIconSrc | string | [Resource](../../common-definitions/basic-types/document.md#resource) | No | Yes | 

Displays the icon when the password is toggled to hidden in the password input mode.

The string type can be used to load network images and local images.

 |

#### EnterKeyType

Type of the Enter key.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| Go | 2 | 
The Enter key is labeled "Go."

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| Search | 3 | 

The Enter key is labeled "Search."

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| Send | 4 | 

The Enter key is labeled "Send."

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| Next | 5 | 

The Enter key is labeled "Next."

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| Done | 6 | 

The Enter key is labeled "Done."

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| PREVIOUS11+ | 7 | 

The Enter key is labeled "Previous."

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| NEW\_LINE11+ | 8 | 

The Enter key is labeled "New Line."

**Atomic service API**: This API can be used in atomic services since API version 12.

 |

#### Events

In addition to the [universal events](../../universal-events/document.md), the following events are supported.

#### \[h2\]onChange

onChange(callback: EditableTextOnChangeCallback)

Triggered when the input in the text box changes.

In this callback, if caret operations are performed, you must adjust the caret logic based on the **previewText** parameter to ensure it works seamlessly within the preview display scenario.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | [EditableTextOnChangeCallback](../text-component-common-apis/document.md#editabletextonchangecallback12) | Yes | Callback invoked when the input in the text box changes. |

#### \[h2\]onSubmit

onSubmit(callback: OnSubmitCallback)

Triggered when the Enter key on the keyboard is pressed for submission.

On non-TV devices, the input box loses focus and the keyboard is dismissed by default when the Enter key is pressed. You can configure whether to dismiss the keyboard in **OnSubmitCallback**. For details, see [Example 2: Setting Underlines](#example-2-setting-underlines).

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | [OnSubmitCallback](#onsubmitcallback18) | Yes | Callback for submission. |

#### \[h2\]onEditChanged(deprecated)

onEditChanged(callback: (isEditing: boolean) => void)

Triggered when the input status changes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/JeerfXR4SMSvUl1dUabakQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C7FB1D33772A2C340251F71E09CFD83D498920E2C947FE77EA39DADC87E0989F)

This API is supported since API version 7 and deprecated since API version 8. You are advised to use [onEditChange](#oneditchange8) instead.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| isEditing | boolean | Yes | 
Whether the input is in progress.

**true**: Input is in progress. **false**: No input is in progress.

 |

#### \[h2\]onEditChange8+

onEditChange(callback: Callback<boolean>)

Triggered when the input status changes. The text box is in the editing state when it has the caret placed in it, and is in the non-editing state otherwise.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | Callback<boolean> | Yes | Callback for the input status change. Returns **true** if the input box is in the editing state; returns **false** if the input box is in the non-editing state. |

#### \[h2\]onCopy8+

onCopy(callback: Callback<string>)

Triggered when a copy operation is performed.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | Callback<string> | Yes | Callback used to return the copied text content. |

#### \[h2\]onCut8+

onCut(callback: Callback<string>)

Triggered when a cut operation is performed.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | Callback<string> | Yes | Callback used to return the cut text content. |

#### \[h2\]onPaste8+

onPaste(callback: OnPasteCallback)

Triggered when a paste operation is performed.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | [OnPasteCallback](#onpastecallback18) | Yes | Callback used to return the pasted text content. |

#### \[h2\]onTextSelectionChange10+

onTextSelectionChange(callback: OnTextSelectionChangeCallback)

Triggered when the text selection changes or the caret position changes during editing.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | [OnTextSelectionChangeCallback](#ontextselectionchangecallback18) | Yes | Callback for text selection changes or caret position changes. |

#### \[h2\]onContentScroll10+

onContentScroll(callback: OnContentScrollCallback)

Triggered when the text content is scrolled.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | [OnContentScrollCallback](#oncontentscrollcallback18) | Yes | Callback for text content scrolling. |

#### \[h2\]onSecurityStateChange12+

onSecurityStateChange(callback: Callback<boolean>)

Triggered when the password visibility state is toggled.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/hY3FJTaiSnm0kEJy-X_s4g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7895CBEF0E2286A3D2AFB565739C3EEC4F0074F24489C5699906D2B8DD1AC477)

This API can be called in [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier) since API version 20.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | Callback<boolean> | Yes | 
Callback used to return the result.

Returns **true** if the state is toggled; returns **false** otherwise.

 |

#### \[h2\]onWillInsert12+

onWillInsert(callback: Callback<InsertValue, boolean>)

Triggered when text is about to be inserted.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | Callback<[InsertValue](../text-component-common-apis/document.md#insertvalue12), boolean> | Yes | 
Callback triggered when text is about to be inserted.

It returns **true** if the text is inserted; returns **false** otherwise.

This callback is not triggered for pre-edit or candidate word operations.

It is available only for system input methods.

 |

#### \[h2\]onDidInsert12+

onDidInsert(callback: Callback<InsertValue>)

Triggered when text is inserted.

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

Triggered when text is about to be deleted.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | Callback<[DeleteValue](../text-component-common-apis/document.md#deletevalue12), boolean> | Yes | 
Callback triggered when text is about to be deleted.

It returns **true** if the text is deleted; returns **false** otherwise.

This callback is not called for text preview.

It is available only for system input methods.

 |

#### \[h2\]onDidDelete12+

onDidDelete(callback: Callback<DeleteValue>)

Triggered when text is deleted.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | Callback<[DeleteValue](../text-component-common-apis/document.md#deletevalue12)\> | Yes | 
Callback triggered when text is deleted.

It is available only for system input methods.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/FpfY91t8QTuFThz1UDjX1g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=50C365398F4A81BC0CBD343B1780F03B3B542BC2B468B5D59A027407F91FA842)

Clicking the clear button does not trigger the **onDidDelete** callback.

#### \[h2\]onWillChange15+

onWillChange(callback: Callback<EditableTextChangeValue, boolean>)

Triggered when the text content is about to change.

This callback is triggered after **onWillInsert** and **onWillDelete**, but before **onDidInsert** and **onDidDelete**.

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | Callback<[EditableTextChangeValue](../text-component-common-apis/document.md#editabletextchangevalue15), boolean> | Yes | 
Callback triggered when the text content is about to change.

Returning **true** allows the change to proceed, while returning **false** cancels the change.

 |

#### \[h2\]onWillAttachIME20+

onWillAttachIME(callback: Callback<IMEClient>)

Called when the input box is about to be bound to an input method.

From API version 22, the [setExtraConfig](../text-component-common-apis/document.md#setextraconfig22) method of [IMEClient](../text-component-common-apis/document.md#imeclient20) can be called to set input method extension information. After the input method is bound, it receives this extension information which can be used to implement custom functionality.

**IMEClient** is valid only during the execution of **onWillAttachIME** and cannot be called asynchronously.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3/v3/0AtAV7wvSJiHbJQRKZeMrA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C6BDAB080F8931DE5B9D6AED1930B6722F162901D7F438CD8DCD84805FA6D43F)

This API cannot be called within [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier).

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | Callback<[IMEClient](../text-component-common-apis/document.md#imeclient20) > | Yes | Callback invoked when the input box is about to be bound to an input method. |

#### TextInputController8+

The controller for the **TextInput** component inherits from [TextContentControllerBase](../text-box-component-common-apis/document.md#textcontentcontrollerbase). The APIs involved are as follows: [getTextContentRect](../text-box-component-common-apis/document.md#gettextcontentrect), [getTextContentLineCount](../text-box-component-common-apis/document.md#gettextcontentlinecount), [getCaretOffset](../text-box-component-common-apis/document.md#getcaretoffset11), [addText](../text-box-component-common-apis/document.md#addtext15), [deleteText](../text-box-component-common-apis/document.md#deletetext15), [getSelection](../text-box-component-common-apis/document.md#getselection15), [clearPreviewText](../text-box-component-common-apis/document.md#clearpreviewtext17), and [setStyledPlaceholder](../text-box-component-common-apis/document.md#setstyledplaceholder22).

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

## Objects to Import

controller: TextInputController = new TextInputController();

#### \[h2\]constructor8+

constructor()

A constructor used to create a **TextInputController** object.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### \[h2\]caretPosition8+

caretPosition(value: number): void

Sets the position of the caret. If the value is less than 0, the value **0** is used. If the value exceeds the text length, the caret is placed at the end of the text.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | Yes | Length from the start of the string to the position where the caret is located. |

#### \[h2\]setTextSelection10+

setTextSelection(selectionStart: number, selectionEnd: number, options?: SelectionOptions): void

Sets the text selection area, which will be highlighted.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| selectionStart | number | Yes | Start position of the text selection range. The start position of text in the text box is 0. |
| selectionEnd | number | Yes | End position of the text selection range. If **selectionEnd** is less than 0, it is handled as **0**. If **selectionEnd** exceeds the text length, it is clamped to the text length. |
| options12+ | [SelectionOptions](../text-box-component-common-apis/document.md#selectionoptions12) | No | 
Configuration options for text selection.

Default value: **MenuPolicy.DEFAULT**

This API can be used in atomic services since API version 12.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/41l0rZnxRY-BaArylPcglQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9BD1876CA70252343CF3B7FAEF399861D17F686C34BDD122261EE816B67A15FC)

If **selectionStart** or **selectionEnd** is set to **undefined**, the value **0** will be used.

If **selectionMenuHidden** is set to **true** or a 2-in-1 device is used, calling **setTextSelection** does not display the text selection menu even when **options** is set to **MenuPolicy.SHOW**.

When an emoji is truncated by the text selection range, it will be selected if its start position lies within the range.

#### \[h2\]stopEditing10+

stopEditing(): void

Exits the editing state.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### UnderlineColor12+

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| typing | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | undefined | No | Yes | Underline color in the typing state. If no value is specified or if the value specified is **undefined**, **null**, or invalid, the default value is used. |
| normal | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | undefined | No | Yes | Underline color in the normal state. If no value is specified or if the value specified is **undefined**, **null**, or invalid, the default value is used. |
| error | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | undefined | No | Yes | Underline color when an error occurs. If no value is specified or if the value specified is **undefined**, **null**, or invalid, the default value is used. This option changes the color used in the **showCounter** attribute when the maximum number of characters is reached. |
| disable | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | undefined | No | Yes | Underline color in the disabled state. If no value is specified or if the value specified is **undefined**, **null**, or invalid, the default value is used. |

#### SubmitEvent11+

Defines the user submission event.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### \[h2\]Attributes

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| text | string | No | No | Text in the text box. |

#### \[h2\]keepEditableState11+

keepEditableState(): void

Maintains the editable state of the text box when called.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### OnPasteCallback18+

type OnPasteCallback = (content: string, event: PasteEvent) => void

Defines the callback used to return the pasted text content.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| content | string | Yes | Text to be pasted. |
| event | [PasteEvent](../richeditor/document.md#pasteevent11) | Yes | Custom paste event. |

#### OnSubmitCallback18+

type OnSubmitCallback = (enterKey: EnterKeyType, event: SubmitEvent) => void

Defines the callback for submission.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| enterKey | [EnterKeyType](#enterkeytype) | Yes | Type of the Enter key. |
| event | [SubmitEvent](#submitevent11) | Yes | Submit event. It can be used to control whether to dismiss the keyboard. |

#### OnTextSelectionChangeCallback18+

type OnTextSelectionChangeCallback = (selectionStart: number, selectionEnd: number) => void

Defines the callback for text selection changes or caret position changes.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| selectionStart | number | Yes | Start position of the selected text. The start position of text is 0. |
| selectionEnd | number | Yes | End position of the selected text. |

#### OnContentScrollCallback18+

type OnContentScrollCallback = (totalOffsetX: number, totalOffsetY: number) => void

Defines the callback for text content scrolling.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| totalOffsetX | number | Yes | Offset in the X coordinate of the text in the content area, in px. |
| totalOffsetY | number | Yes | Offset in the Y coordinate of the text in the content area, in px. |

#### Example

## Example 1: Setting and Obtaining the Caret Position

This example demonstrates how to set and obtain the caret position using [controller](#textinputcontroller8), available since API version 8. You can use **!!** to implement two-way data binding for the **text** parameter, available since API version 18.

// xxx.ets
@Entry
@Component
struct TextInputExample {
  @State text: string = '';
  @State positionInfo: CaretOffset = { index: 0, x: 0, y: 0 };
  @State passwordState: boolean = false;
  controller: TextInputController = new TextInputController();

  build() {
    Column() {
      TextInput({ text: this.text!!, placeholder: 'input your word...', controller: this.controller })
        .placeholderColor(Color.Grey)
        .placeholderFont({ size: 14, weight: 400 })
        .caretColor(Color.Blue)
        .width('95%')
        .height(40)
        .margin(20)
        .fontSize(14)
        .fontColor(Color.Black)
        .inputFilter('\[a-z\]', (e) => {
          console.info(JSON.stringify(e));
        })
      Text(this.text)
      Button('Set caretPosition 1')
        .margin(15)
        .onClick(() => {
          // Move the caret to after the first entered character.
          this.controller.caretPosition(1);
        })
      Button('Get CaretOffset')
        .margin(15)
        .onClick(() => {
          this.positionInfo = this.controller.getCaretOffset();
        })
      // Password text box.
      TextInput({ placeholder: 'input your password...' })
        .width('95%')
        .height(40)
        .margin(20)
        .type(InputType.Password)
        .maxLength(9)
        .showPasswordIcon(true)
        .showPassword(this.passwordState)
        .onSecurityStateChange(((isShowPassword: boolean) => {
          // Update the password visibility.
          console.info('isShowPassword', isShowPassword);
          this.passwordState = isShowPassword;
        }))
      // Email address autofill.
      TextInput({ placeholder: 'input your email...' })
        .width('95%')
        .height(40)
        .margin(20)
        .contentType(ContentType.EMAIL\_ADDRESS)
        .maxLength(9)
      // Inline-style text box.
      TextInput({ text: 'inline style' })
        .width('95%')
        .height(50)
        .margin(20)
        .borderRadius(0)
        .style(TextInputStyle.Inline)
    }.width('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/81zvzyVvRIasnqRlsVRdWQ/en-us_image_0000002537925592.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=66448BBC2704F27DED8FF0AA7D960B133B1608C0B7059E363ECD29C322D09A5E)

## Example 2: Setting Underlines

This example demonstrates the display effects of underlines in different scenarios through [showUnderline](#showunderline10), [showError](#showerror10), [showUnit](#showunit10), and [passwordIcon](#passwordicon10) attributes, available since API version 10. The [underlineColor](#underlinecolor12) attribute (available since API version 12) can be used to configure the underline color.

// xxx.ets
@Entry
@Component
struct TextInputExample {
  // Replace $r('app.media.ImageOne') with the image resource file you use.
  @State passWordSrc1: Resource = $r('app.media.ImageOne');
  // Replace $r('app.media.ImageTwo') with the image resource file you use.
  @State passWordSrc2: Resource = $r('app.media.ImageTwo');
  @State textError: string = '';
  @State text: string = '';
  @State nameText: string = 'test';

  @Builder
  itemEnd() {
    Select(\[{ value: 'KB' },
      { value: 'MB' },
      { value: 'GB' },
      { value: 'TB', }\])
      .height("48vp")
      .borderRadius(0)
      .selected(2)
      .align(Alignment.Center)
      .value('MB')
      .font({ size: 20, weight: 500 })
      .fontColor('#182431')
      .selectedOptionFont({ size: 20, weight: 400 })
      .optionFont({ size: 20, weight: 400 })
      .backgroundColor(Color.Transparent)
      .responseRegion({
        height: "40vp",
        width: "80%",
        x: '10%',
        y: '6vp'
      })
      .onSelect((index: number) => {
        console.info('Select:' + index);
      })
  }

  build() {
    Column({ space: 20 }) {
      // Customize the password icon.
      TextInput({ placeholder: 'Custom password icon' })
        .type(InputType.Password)
        .width(350)
        .height(60)
        .passwordIcon({ onIconSrc: this.passWordSrc1, offIconSrc: this.passWordSrc2 })
      // Show an underline.
      TextInput({ placeholder: 'Underline style' })
        .showUnderline(true)
        .width(350)
        .height(60)
        .showError('Error')
        .showUnit(this.itemEnd)

      Text(\`User name: ${this.text}\`)
        .width(350)
      TextInput({ placeholder: 'Enter user name', text: this.text })
        .showUnderline(true)
        .width(350)
        .showError(this.textError)
        .onChange((value: string) => {
          this.text = value;
        })
        .onSubmit((enterKey: EnterKeyType, event: SubmitEvent) => {
          // If the entered user name is incorrect, clear the text box and display an error message.
          if (this.text == this.nameText) {
            this.textError = '';
          } else {
            this.textError = 'Incorrect user name.';
            this.text = '';
            // Call keepEditableState to maintain the editable state of the text box.
            event.keepEditableState();
          }
        })
      // Set the color of the underline.
      TextInput({ placeholder: 'Placeholder text' })
        .width(350)
        .showUnderline(true)
        .underlineColor({
          normal: Color.Orange,
          typing: Color.Green,
          error: Color.Red,
          disable: Color.Gray
        })
      TextInput({ placeholder: 'Placeholder text' })
        .width(350)
        .showUnderline(true)
        .underlineColor(Color.Gray);

    }.width('100%').margin({ top: 10 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/xLt0twzMQ0CP8GXhaN24hA/en-us_image_0000002568685369.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CA0B50574C091CDD06280AE9EC6A741195B09D4FF9660BAFE3DBF432457156CB)

## Example 3: Implementing a Custom Keyboard

This example implements a custom keyboard using the [customKeyboard](#customkeyboard10) attribute (available since API version 10) to set the input parameter type in **value** to [CustomBuilder](../../common-definitions/basic-types/document.md#custombuilder8) and [ComponentContent](../../../arkts-api/ui/arkui/componentcontent/document.md#componentcontent-1).

Since API version 22, [ComponentContent](../../../arkts-api/ui/arkui/componentcontent/document.md#componentcontent-1) is added to the input parameter type of [customKeyboard](#customkeyboard10).

// xxx.ets
import { ComponentContent } from '@kit.ArkUI';
class BuilderParams {
  inputValue: string;
  controller: TextInputController;

  constructor(inputValue: string, controller: TextInputController) {
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
struct TextInputExample {
  controller: TextInputController = new TextInputController();
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
      TextInput({ controller: this.builderParam.controller, text: this.builderParam.inputValue })
        .customKeyboard(this.componentContent, { supportAvoidance: this.supportAvoidance })
        .margin(10).border({ width: 1 }).height('48vp')

      Text('ComponentContent').margin(10).border({ width: 1 })
      TextInput({ controller: this.builderParam.controller, text: this.builderParam.inputValue })
        .customKeyboard(CustomKeyboardBuilder(this.builderParam), { supportAvoidance: this.supportAvoidance })
        .margin(10).border({ width: 1 }).height('48vp')
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/whhwk-TdQty0aS2PmTNN0A/en-us_image_0000002568765379.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=18C95B6647378E1B16047FF959040764D7C03474E1F3ACE7A7DAB2DA12C86BD3)

## Example 4: Customizing the Cancel Button Style on the Right

This example demonstrates how to use the [cancelButton](#cancelbutton11) attribute to customize the style of the cancel button on the right side of the text box.

// xxx.ets
@Entry
@Component
struct TextInputExample {
  @State text: string = '';
  controller: TextInputController = new TextInputController();

  build() {
    Column() {
      TextInput({ placeholder: 'input ...', controller: this.controller })
        .width(380)
        .height(60)
        .cancelButton({
          style: CancelButtonStyle.CONSTANT,
          icon: {
            size: 45,
            // Replace $r('app.media.startIcon') with the image resource file you use.
            src: $r('app.media.startIcon'),
            color: Color.Blue
          }
        })
        .onChange((value: string) => {
          this.text = value;
        })
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/F7k8iP40QR-rTlNEs2y8sA/en-us_image_0000002537765654.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5EDA575214A9B6A7E8B733A9C3426B7465D4A2D97E8E3EE1A1FF5746ECFD3E39)

## Example 5: Setting a Character Counter

This example demonstrates how to implement a character counter using the [maxLength](#maxlength), [showCounter](#showcounter11) (available since API version 11), and [showUnderline](#showunderline10) (available since API version 10) attributes.

// xxx.ets
@Entry
@Component
struct TextInputExample {
  @State text: string = '';
  controller: TextInputController = new TextInputController();

  build() {
    Column() {
      TextInput({ text: this.text, controller: this.controller })
        .placeholderFont({ size: 16, weight: 400 })
        .width(336)
        .height(56)
        .maxLength(6)
        .showUnderline(true)
        .showCounter(true,
          { thresholdPercentage: 50, highlightBorder: true })// The character counter is in this format: Number of characters that have been entered/Maximum number of characters allowed, which is specified by maxLength().
          // The character counter is displayed when the number of characters that have been entered is greater than the maximum number of characters multiplied by 50% (threshold percentage).
          // When highlightBorder is set to false, the text box border does not turn red when the input exceeds the maximum character limit. The default value is true.
        .onChange((value: string) => {
          this.text = value;
        })
    }.width('100%').height('100%').backgroundColor('#F1F3F5')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/OyFSwj8lRwWJUzwmX6ibMg/en-us_image_0000002537925594.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E50E69D80488D467A105DF86DD7E73081619756EA5734C63021A8E2A4D53CC48)

## Example 6: Formatting a Phone Number

This example demonstrates how to format a phone number as "XXX XXXX XXXX" through the [onChange](#onchange) callback.

// xxx.ets
@Entry
@Component
struct TextInputExample {
  @State submitValue: string = '';
  @State text: string = '';
  public readonly NUM\_TEXT\_MAXSIZE\_LENGTH = 13;
  @State telNumberNoSpace: string = "";
  @State nextCaret: number = -1; // Used to record the position for the next caret setting.
  @State actualCh: number = -1; // Used to record the insertion or deletion position relative to the i-th digit of the caret.
  @State lastCaretPosition: number = 0;
  @State lastCaretPositionEnd: number = 0;
  controller: TextInputController = new TextInputController();

  isEmpty(str?: string): boolean {
    return str == 'undefined' || !str || !new RegExp("\[^\\\\s\]").test(str);
  }

  checkNeedNumberSpace(numText: string) {
    let isSpace: RegExp = new RegExp('\[\\\\+;,#\\\\\*\]', 'g');
    let isRule: RegExp = new RegExp('^\\\\+.\*');

    if (isSpace.test(numText)) {
      // If the phone number contains special characters, no space is added.
      if (isRule.test(numText)) {
        return true;
      } else {
        return false;
      }
    }
    return true;
  }

  removeSpace(str: string): string {
    if (this.isEmpty(str)) {
      return '';
    }
    return str.replace(new RegExp("\[\\\\s\]", "g"), '');
  }

  setCaret() {
    if (this.nextCaret != -1) {
      console.info("to keep caret position right, change caret to", this.nextCaret);
      this.controller.caretPosition(this.nextCaret);
      this.nextCaret = -1;
    }
  }

  calcCaretPosition(nextText: string) {
    let befNumberNoSpace: string = this.removeSpace(this.text);
    this.actualCh = 0;
    if (befNumberNoSpace.length < this.telNumberNoSpace.length) { // Insertion scenario
      for (let i = 0; i < this.lastCaretPosition; i++) {
        if (this.text\[i\] != ' ') {
          this.actualCh += 1;
        }
      }
      this.actualCh += this.telNumberNoSpace.length - befNumberNoSpace.length;
      console.info("actualCh: " + this.actualCh);
      for (let i = 0; i < nextText.length; i++) {
        if (nextText\[i\] != ' ') {
          this.actualCh -= 1;
          if (this.actualCh <= 0) {
            this.nextCaret = i + 1;
            break;
          }
        }
      }
    } else if (befNumberNoSpace.length > this.telNumberNoSpace.length) { // Deletion scenario
      if (this.lastCaretPosition === this.text.length) {
        console.info("Caret at last, no need to change");
      } else if (this.lastCaretPosition === this.lastCaretPositionEnd) {
        // Scenario where the backspace key on the keyboard is used to delete characters one by one
        for (let i = this.lastCaretPosition; i < this.text.length; i++) {
          if (this.text\[i\] != ' ') {
            this.actualCh += 1;
          }
        }
        for (let i = nextText.length - 1; i >= 0; i--) {
          if (nextText\[i\] != ' ') {
            this.actualCh -= 1;
            if (this.actualCh <= 0) {
              this.nextCaret = i;
              break;
            }
          }
        }
      } else {
        // When cutting or selecting text with a handle to delete multiple characters at once
        this.nextCaret = this.lastCaretPosition; // Maintain the caret position.
      }
    }
  }

  build() {
    Column() {
      Row() {
        TextInput({ text: \`${this.text}\`, controller: this.controller }).type(InputType.PhoneNumber).height('48vp')
          .onChange((value: string) => {
            this.telNumberNoSpace = this.removeSpace(value);
            let nextText: string = "";
            if (this.telNumberNoSpace.length > this.NUM\_TEXT\_MAXSIZE\_LENGTH - 2) {
              nextText = this.telNumberNoSpace;
            } else if (this.checkNeedNumberSpace(value)) {
              if (this.telNumberNoSpace.length <= 3) {
                nextText = this.telNumberNoSpace;
              } else {
                let split1: string = this.telNumberNoSpace.substring(0, 3);
                let split2: string = this.telNumberNoSpace.substring(3);
                nextText = split1 + ' ' + split2;
                if (this.telNumberNoSpace.length > 7) {
                  split2 = this.telNumberNoSpace.substring(3, 7);
                  let split3: string = this.telNumberNoSpace.substring(7);
                  nextText = split1 + ' ' + split2 + ' ' + split3;
                }
              }
            } else {
              nextText = value;
            }
            console.info("onChange Triggered:" + this.text + "|" + nextText + "|" + value);
            if (this.text === nextText && nextText === value) {
              // The number has been formatted. Changing the caret position at this time will not reset the number.
              this.setCaret();
            } else {
              this.calcCaretPosition(nextText);
            }
            this.text = nextText;
          })
          .onTextSelectionChange((selectionStart, selectionEnd) => {
            // Record the caret position.
            console.info("selection change: ", selectionStart, selectionEnd);
            this.lastCaretPosition = selectionStart;
            this.lastCaretPositionEnd = selectionEnd;
          })// Supported since API version 10
      }
    }
    .width('100%')
    .height("100%")
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/jWxu90tqTlOj_jttEC83YQ/en-us_image_0000002568685371.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E7130BA838917AB2D40E9A26AE1A90FBCB12232CD442D7D2687F88E5A6BBF696)

## Example 7: Setting Text Wrapping Rules

This example demonstrates the effects of different text wrapping rules using the [wordBreak](#wordbreak12) attribute, available since API version 12.

// xxx.ets
@Entry
@Component
struct TextInputExample {
  @State textStrEn: string =
    'This is set wordBreak to WordBreak text Taumatawhakatangihangakoauauotamateaturipukakapikimaungahoronukupokaiwhenuakitanatahu.';
  @State textStrZn: string =
    '多行文本输入框组件，当输入的文本内容超过组件宽度时会自动换行显示。\\n高度未设置时，组件无默认高度，自适应内容高度。宽度未设置时，默认撑满最大宽度。';

  build() {
    Row() {
      Column() {
        Text("WordBreakType as NORMAL in the inline style:").fontSize(16).fontColor(0xCCCCCC)
        TextInput({
          text: this.textStrEn
        })
          .margin(10)
          .fontSize(16)
          .style(TextInputStyle.Inline)// Inline style
          .wordBreak(WordBreak.NORMAL) // This attribute does not take effect for the non-inline style.

        Text("WordBreakType as BREAK\_ALL in the inline style:").fontSize(16).fontColor(0xCCCCCC)
        TextInput({
          text: this.textStrEn
        })
          .margin(10)
          .fontSize(16)
          .style(TextInputStyle.Inline)
          .wordBreak(WordBreak.BREAK\_ALL)

        Text("WordBreakType as BREAK\_ALL in the inline style, Chinese text:").fontSize(16).fontColor(0xCCCCCC)
        TextInput({
          text: this.textStrZn
        })
          .margin(10)
          .fontSize(16)
          .style(TextInputStyle.Inline)
          .wordBreak(WordBreak.BREAK\_ALL)

        Text("WordBreakType as BREAK\_WORD in the inline style:").fontSize(16).fontColor(0xCCCCCC)
        TextInput({
          text: this.textStrEn
        })
          .margin(10)
          .fontSize(16)
          .style(TextInputStyle.Inline)
          .wordBreak(WordBreak.BREAK\_WORD)
      }.width('100%')
    }.height('100%').margin(10)
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/YgQO9_SKTwKUuC1OokovGg/en-us_image_0000002568765381.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F4D72A8C2B4C5A955AA709B45966642F16D86AFC70E39E7EDBB4C0D5A38B52E7)

## Example 8: Setting the Text Style

This example demonstrates various text styles using the [lineHeight](#lineheight12), [letterSpacing](#letterspacing12), and [decoration](#decoration12) attributes, available since API version 12.

// xxx.ets
@Entry
@Component
struct TextInputExample {
  build() {
    Row() {
      Column() {
        Text('lineHeight').fontSize(9).fontColor(0xCCCCCC)
        TextInput({ text: 'lineHeight unset' })
          .border({ width: 1 }).padding(10).margin(5)
        TextInput({ text: 'lineHeight 15' })
          .border({ width: 1 }).padding(10).margin(5).lineHeight(15)
        TextInput({ text: 'lineHeight 30' })
          .border({ width: 1 }).padding(10).margin(5).lineHeight(30)

        Text('letterSpacing').fontSize(9).fontColor(0xCCCCCC)
        TextInput({ text: 'letterSpacing 0' })
          .border({ width: 1 }).padding(5).margin(5).letterSpacing(0)
        TextInput({ text: 'letterSpacing 3' })
          .border({ width: 1 }).padding(5).margin(5).letterSpacing(3)
        TextInput({ text: 'letterSpacing -1' })
          .border({ width: 1 }).padding(5).margin(5).letterSpacing(-1)

        Text('decoration').fontSize(9).fontColor(0xCCCCCC)
        TextInput({ text: 'LineThrough, Red' })
          .border({ width: 1 }).padding(5).margin(5)
          .decoration({ type: TextDecorationType.LineThrough, color: Color.Red })
        TextInput({ text: 'Overline, Red, DASHED' })
          .border({ width: 1 }).padding(5).margin(5)
          .decoration({ type: TextDecorationType.Overline, color: Color.Red, style: TextDecorationStyle.DASHED })
        TextInput({ text: 'Underline, Red, WAVY' })
          .border({ width: 1 }).padding(5).margin(5)
          .decoration({ type: TextDecorationType.Underline, color: Color.Red, style: TextDecorationStyle.WAVY })
      }.height('90%')
    }
    .width('90%')
    .margin(10)
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/HuDv0AkfQPmv0evivCj3_w/en-us_image_0000002537765656.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=497A099A59E582F60D60520B1B470D023AB30760675400FE795709E299910843)

## Example 9: Setting Text Feature Effects

This example demonstrates how to display text with various typographic features using the [fontFeature](#fontfeature12) attribute, available since API version 12.

// xxx.ets
@Entry
@Component
struct TextInputExample {
  @State text1: string = 'This is ss01 on : 0123456789';
  @State text2: string = 'This is ss01 off: 0123456789';

  build() {
    Column() {
      TextInput({ text: this.text1 })
        .fontSize(20)
        .margin({ top: 200 })
        .fontFeature("\\"ss01\\" on")
      TextInput({ text: this.text2 })
        .margin({ top: 10 })
        .fontSize(20)
        .fontFeature("\\"ss01\\" off")
    }
    .width("90%")
    .margin("5%")
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/Rjzh5xUNQBacw5bTLQbUiw/en-us_image_0000002537925596.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3B6C72D0547F99F36C9827C97BC7F234FB456044F5E5EE8CA01FB9F3FEFCA8DC)

## Example 10: Setting Custom Keyboard Avoidance

This example implements the custom keyboard avoidance effect by configuring the [KeyboardOptions](../richeditor/document.md#keyboardoptions12) API (available since API version 12) through the [customKeyboard](#customkeyboard10) attribute (available since API version 10).

// xxx.ets
@Entry
@Component
struct TextInputExample {
  controller: TextInputController = new TextInputController();
  @State inputValue: string = "";
  @State height1: string | number = '80%';
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

      TextInput({ controller: this.controller, text: this.inputValue })// Bind a custom keyboard.
        .customKeyboard(this.CustomKeyboardBuilder(), { supportAvoidance: this.supportAvoidance })
        .margin(10)
        .border({ width: 1 })

    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/YLu96RUlR3iRaQJiRHRNXg/en-us_image_0000002568685373.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=80AD6123DC5CB933484F4D7444226B48C691DA5E0ADF59F61E91D23D7A281149)

## Example 11: Setting Text Auto-Adaptation

This example implements text auto-adaptation using the [minFontSize](#minfontsize12), [maxFontSize](#maxfontsize12), and [heightAdaptivePolicy](#heightadaptivepolicy12) attributes, all available since API version 12.

// xxx.ets
@Entry
@Component
struct TextInputExample {
  build() {
    Row() {
      Column() {
        Text('heightAdaptivePolicy').fontSize(9).fontColor(0xCCCCCC)
        TextInput({ text: 'This is the text without the height adaptive policy set' })
          .width('80%').height(50).borderWidth(1).margin(1)
        TextInput({ text: 'This is the text with the height adaptive policy set' })
          .width('80%')
          .height(50)
          .borderWidth(1)
          .margin(1)
          .minFontSize(4)
          .maxFontSize(40)
          .maxLines(3)
          .heightAdaptivePolicy(TextHeightAdaptivePolicy.MAX\_LINES\_FIRST)
        TextInput({ text: 'This is the text with the height adaptive policy set' })
          .width('80%')
          .height(50)
          .borderWidth(1)
          .margin(1)
          .minFontSize(4)
          .maxFontSize(40)
          .maxLines(3)
          .heightAdaptivePolicy(TextHeightAdaptivePolicy.MIN\_FONT\_SIZE\_FIRST)
        TextInput({ text: 'This is the text with the height adaptive policy set' })
          .width('80%')
          .height(50)
          .borderWidth(1)
          .margin(1)
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/lj0-d38rR3-IqDaMqQ7WQw/en-us_image_0000002568765383.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C8EA2E99E55C43CCACE3BCBC4FF01D0D6B3B18AB3DE29FE9FD86E6812989F187)

## Example 12: Setting Line Break Rules

This example demonstrates the effects of different line break rules using the [lineBreakStrategy](#linebreakstrategy12) attribute, available since API version 12.

// xxx.ets
@Entry
@Component
struct TextInputExample {
  @State message1: string =
    "They can be classified as built-in components–those directly provided by the ArkUI framework and custom components – those defined by developers" +
      "The built-in components include buttons radio progress indicators and text You can set the rendering effect of these components in method chaining mode," +
      "page components are divided into independent UI units to implementindependent creation development and reuse of different units on pages making pages more engineering-oriented.";
  @State lineBreakStrategyIndex: number = 0;
  @State lineBreakStrategy: LineBreakStrategy\[\] =
    \[LineBreakStrategy.GREEDY, LineBreakStrategy.HIGH\_QUALITY, LineBreakStrategy.BALANCED\];
  @State lineBreakStrategyStr: string\[\] = \['GREEDY', 'HIGH\_QUALITY', 'BALANCED'\];

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center }) {
      Text('lineBreakStrategy').fontSize(16).fontColor(Color.Black)
      TextInput({ text: this.message1 })
        .fontSize(12)
        .border({ width: 1 })
        .padding(10)
        .width('100%')
        .maxLines(12)
        .style(TextInputStyle.Inline)
        .lineBreakStrategy(this.lineBreakStrategy\[this.lineBreakStrategyIndex\])
      Row() {
        Button('Current lineBreakStrategy value: ' + this.lineBreakStrategyStr\[this.lineBreakStrategyIndex\]).onClick(() => {
          this.lineBreakStrategyIndex++;
          if (this.lineBreakStrategyIndex > (this.lineBreakStrategyStr.length - 1)) {
            this.lineBreakStrategyIndex = 0;
          }
        })
      }.margin({ top: 20 })
    }.height(700).width(370).padding({ left: 35, right: 35, top: 35 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/uc4W3B0XRkWGU9DUGpShyg/en-us_image_0000002537765658.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6A2386A75272969238D62F09ADCA8255CDDE6DBD7A57EF73ED031458C6E84698)

## Example 13: Setting Insert and Delete Callbacks

This example implements the text insertion and deletion effects using the [onWillInsert](#onwillinsert12), [onDidInsert](#ondidinsert12), [onWillDelete](#onwilldelete12), and [onDidDelete](#ondiddelete12) APIs, available since API version 12.

// xxx.ets
@Entry
@Component
struct TextInputExample {
  @State insertValue: string = "";
  @State deleteValue: string = "";
  @State insertOffset: number = 0;
  @State deleteOffset: number = 0;
  @State deleteDirection: number = 0;

  build() {
    Row() {
      Column() {
        TextInput({ text: "Insert callbacks" })
          .height(60)
          .onWillInsert((info: InsertValue) => {
            this.insertValue = info.insertValue;
            return true;
          })
          .onDidInsert((info: InsertValue) => {
            this.insertOffset = info.insertOffset;
          })

        Text("insertValue:" + this.insertValue + "  insertOffset:" + this.insertOffset).height(30)

        TextInput({ text: "Delete callbacks" })
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/xYSGAU4BSR2xpXlmn1nQOg/en-us_image_0000002537925598.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B130EA665EEA308F0AD1F1C83BCEA14E7B4429F8130E0E9AD96699133823AB5D)

## Example 14: Setting Custom Menu Extensions

This example implements custom menu extension items for text using the [editMenuOptions](#editmenuoptions12) API (available since API version 12), allowing configuration of text content, icons, and callbacks. Menu data can be configured through the [onPrepareMenu](../text-component-common-apis/document.md#properties-1) callback (available since API version 20).

// xxx.ets
@Entry
@Component
struct TextInputExample {
  @State text: string = 'TextInput editMenuOptions';
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
  // Replace $r('app.media.startIcon') with the image resource file you use.
  onPrepareMenu = (menuItems: Array<TextMenuItem>) => {
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
      TextInput({ text: this.text })
        .width('95%')
        .height(50)
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/NYAkFngTTnig3K6gjgJoag/en-us_image_0000002568685375.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F980ECA34294DB53FE35D6CA84486E6B26B9AEC086A5312524A906557DB5AB51)

## Example 15: Setting a Symbol-Type Cancel Button

This example demonstrates how to set the style of the symbol-type cancel button on the right side within the text box using the [cancelButton](#cancelbutton18) attribute, available from API version 18.

import { SymbolGlyphModifier } from '@kit.ArkUI';

// xxx.ets
@Entry
@Component
struct TextInputExample {
  @State text: string = '';
  symbolModifier: SymbolGlyphModifier =
    new SymbolGlyphModifier($r('sys.symbol.trash')).fontColor(\[Color.Red\]).fontSize(16).fontWeight(FontWeight.Regular);

  build() {
    Column() {
      TextInput({ text: this.text, placeholder: 'input your word...' })
        .cancelButton({
          style: CancelButtonStyle.CONSTANT,
          icon: this.symbolModifier
        })
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/fs3afdwURIKpj7CJ2-UYdA/en-us_image_0000002568765385.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7E82C00985861B66DB446FD1738936B6C2A6CFD47A3F896684431CE5A45BFF5A)

## Example 16: Setting Text Overflow

This example demonstrates how to clip text with an ellipsis and adjust its position using the [textOverflow](#textoverflow12) (available since API version 12), [ellipsisMode](#ellipsismode18) (available since API version 18), and [style](#style9) (available since API version 9) attributes.

// xxx.ets
@Entry
@Component
struct EllipsisModeExample {
  @State text: string = "As the sun begins to set, casting a warm golden hue across the sky," +
    "the world seems to slow down and breathe a sigh of relief. The sky is painted with hues of orange, " +
    " pink, and lavender, creating a breath taking tapestry that stretches as far as the eye can see." +
    "The air is filled with the sweet scent of blooming flowers, mingling with the earthy aroma of freshly turned soil.";
  @State ellipsisModeIndex: number = 0;
  @State ellipsisMode: (EllipsisMode | undefined | null)\[\] =
    \[EllipsisMode.END, EllipsisMode.START, EllipsisMode.CENTER\];
  @State ellipsisModeStr: string\[\] = \['END ', 'START', 'CENTER'\];
  @State textOverflowIndex: number = 0;
  @State textOverflow: TextOverflow\[\] = \[TextOverflow.Ellipsis, TextOverflow.Clip\];
  @State textOverflowStr: string\[\] = \['Ellipsis', 'Clip'\];
  @State styleInputIndex: number = 0;
  @State styleInput: TextInputStyle\[\] = \[TextInputStyle.Inline, TextInputStyle.Default\];
  @State styleInputStr: string\[\] = \['Inline', 'Default'\];

  build() {
    Row() {
      Column({ space: 20 }) {
        TextInput({ text: this.text })
          .textOverflow(this.textOverflow\[this.textOverflowIndex\])
          .ellipsisMode(this.ellipsisMode\[this.ellipsisModeIndex\])
          .style(this.styleInput\[this.styleInputIndex\])
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
        Button('Style Value: ' + this.styleInputStr\[this.styleInputIndex\]).onClick(() => {
          this.styleInputIndex++;
          if (this.styleInputIndex > (this.styleInputStr.length - 1)) {
            this.styleInputIndex = 0;
          }
        }).fontSize(20)
      }
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/8aCorMq0Sn66AjWAsL7VIA/en-us_image_0000002537765660.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FDEA36C86076DC865D66C2C8FA670EE41430C15A8A24A8BE4886967AB9F8183B)

## Example 17: Implementing Callbacks for Input Status Changes and More

This example uses the [onEditChange](#oneditchange8), [onCopy](#oncopy8), [onCut](#oncopy8), [onPaste](#onpaste8) (available since API version 8) and [onContentScroll](#oncontentscroll10) (from API version 10) callbacks to monitor the input status change and handle copy, cut, paste, and content scrolling events. The [selectAll](#selectall11) (available since API version 11) attribute can be used to determine whether to select all text in the text box in the initial state.

// xxx.ets
@Entry
@Component
struct TextInputExample {
  @State editStatus: boolean = false;
  @State copyValue: string = "";
  @State cutValue: string = "";
  @State pasteValue: string = "";
  @State totalOffsetX: number = 0;
  @State totalOffsetY: number = 0;

  build() {
    Row() {
      Column() {
        TextInput({ text: "TextInput supports the callback on input status changes" })
          .height(60)
          .fontStyle(FontStyle.Italic)
          .fontWeight(FontWeight.Bold)
          .fontFamily("HarmonyOS Sans")
          .copyOption(CopyOptions.LocalDevice)
          .textAlign(TextAlign.Center)
          .selectedBackgroundColor(Color.Blue)
          .caretStyle({ width: '4vp' })
          .caretPosition(10)
          .selectionMenuHidden(true)
          .onEditChange((status: boolean) => {
            this.editStatus = status;
          })
          .defaultFocus(true)// Set the TextInput component to obtain focus by default.
          .enableKeyboardOnFocus(false)
          .selectAll(false)

        Text("editStatus:" + this.editStatus).height(30)

        TextInput({ text: "TextInput supports the callback on copy operations" })
          .height(60)
          .fontStyle(FontStyle.Italic)
          .fontWeight(FontWeight.Bold)
          .fontFamily("HarmonyOS Sans")
          .copyOption(CopyOptions.LocalDevice)
          .textAlign(TextAlign.Center)
          .selectedBackgroundColor(Color.Blue)
          .caretStyle({ width: '4vp' })
          .onCopy((copyValue: string) => {
            this.copyValue = copyValue;
          })

        Text("copyValue:" + this.copyValue).height(30)

        TextInput({ text: "TextInput supports the callback on cut operations" })
          .height(60)
          .fontStyle(FontStyle.Italic)
          .fontWeight(FontWeight.Bold)
          .fontFamily("HarmonyOS Sans")
          .copyOption(CopyOptions.LocalDevice)
          .textAlign(TextAlign.Center)
          .selectedBackgroundColor(Color.Blue)
          .caretStyle({ width: '4vp' })
          .onCut((cutValue: string) => {
            this.cutValue = cutValue;
          })

        Text("cutValue:" + this.cutValue).height(30)

        TextInput({ text: "TextInput supports the callback on paste operations" })
          .height(60)
          .fontStyle(FontStyle.Italic)
          .fontWeight(FontWeight.Bold)
          .fontFamily("HarmonyOS Sans")
          .copyOption(CopyOptions.LocalDevice)
          .textAlign(TextAlign.Center)
          .selectedBackgroundColor(Color.Blue)
          .caretStyle({ width: '4vp' })
          .onPaste((pasteValue: string) => {
            this.pasteValue = pasteValue;
          })

        Text("pasteValue:" + this.pasteValue).height(30)

        TextInput({ text: "TextInput supports the callback on content scrolling: Scroll the text to see offset changes when the text width exceeds the text box width" })
          .height(60)
          .fontStyle(FontStyle.Italic)
          .fontWeight(FontWeight.Bold)
          .fontFamily("HarmonyOS Sans")
          .copyOption(CopyOptions.LocalDevice)
          .textAlign(TextAlign.Center)
          .selectedBackgroundColor(Color.Blue)
          .caretStyle({ width: '4vp' })
          .onContentScroll((totalOffsetX: number, totalOffsetY: number) => {
            this.totalOffsetX = totalOffsetX;
            this.totalOffsetY = totalOffsetY;
          })

        Text("totalOffsetX:" + this.totalOffsetX + "  totalOffsetY:" + this.totalOffsetY).height(30)

      }.width('100%')
    }
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/ajFyDpmlQtGSfge4Wkqzxg/en-us_image_0000002537925600.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=54D4F2DAF1CE23BBFCAAD7FF9A99227D40079DF9296887F6766A1323690AAAC3)

## Example 18: Setting the Minimum and Maximum Font Scale Factors

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
Entry
Component
struct TextInputExample {
  @State minFontScale: number = 0.85;
  @State maxFontScale: number = 2;

  build() {
    Column() {
      Column({ space: 30 }) {
        Text("Use minFontScale and maxFontScale to adjust the maximum and minimum font scale factors of the text display.")
        TextInput({
          placeholder: 'The text area can hold an unlimited amount of text. input your word...',
          text: 'Use minFontScale and maxFontScale to adjust the maximum and minimum font scale factors of the text display.'
        })
          .minFontScale(this.minFontScale)// Set the minimum font scale factor. If the parameter is set to undefined, the default scale factor is used.
          .maxFontScale(this.maxFontScale) // Set the maximum font scale factor. If the parameter is set to undefined, the default scale factor is used.
      }.width('100%')
    }
  }
}

| System font scale factor: 2x | System font scale factor: 3.2x |
| :-- | :-- |
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/ZPcaKS7ZQeipC7v2b10ZXQ/en-us_image_0000002568685377.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2F0E3AA0B8519A36CFA2148E8E482176E93802DF9EC81C5FBA5A95E30E5BAC09) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/U7AITMBzSUiwtByR-TuVTA/en-us_image_0000002568765387.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6650514DCF18C93543880A283B594974B1298B9652B7B1B70BA1FF4B085DEA01) |

## Example 19: Setting Text Selection for a Specified Region

This example demonstrates how to set text selection for a specified region and the display/hide strategy of the menu using the [setTextSelection](#settextselection10) API, available since API version 10.

// xxx.ets

@Entry
@Component
struct TextInputExample {
  controller: TextInputController = new TextInputController();
  @State startIndex: number = 0;
  @State endIndex: number = 0;

  build() {
    Column({ space: 3 }) {
      Text('Selection start:' + this.startIndex + ' end:' + this.endIndex)
      TextInput({ text: 'Hello World', controller: this.controller })
        .width('95%')
        .height(40)
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/ZOOlyqKiQ3ioYsu_k7FELA/en-us_image_0000002537765662.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E96E8E51E1C78259AEA39B410988EBDACEFF691C669AEBBC1A96BDEDAAC80B96)

## Example 20: Setting Text Stroke

This example demonstrates how to set the stroke width and color for text using the [strokeWidth](#strokewidth20) and [strokeColor](#strokecolor20) attributes, available since API version 20.

// xxx.ets
import { LengthMetrics } from '@kit.ArkUI';

@Entry
@Component
struct TextInputExample {
  build() {
    Row() {
      Column() {
        Text('stroke feature').fontSize(9).fontColor(0xCCCCCC)

        TextInput({ text: 'Text without stroke' })
          .width('100%')
          .height(60)
          .borderWidth(1)
          .fontSize(40)
        TextInput({ text: 'Text with stroke' })
          .width('100%')
          .height(60)
          .borderWidth(1)
          .fontSize(40)
          .strokeWidth(LengthMetrics.px(-3.0))
          .strokeColor(Color.Red)
        TextInput({ text: 'Text with stroke' })
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/YJ2fNfbsRD-gRDyi7IPg7g/en-us_image_0000002537925602.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BA9F73F6BB93823825B2566BB697D4C20DBD0908D2FB0C31CCB4886069FF3D16)

## Example 21: Configuring Automatic Spacing Between Chinese and Western Text

This example demonstrates how to configure automatic spacing between Chinese and Western characters using the [enableAutoSpacing](#enableautospacing20) attribute, available since API version 20.

// xxx.ets
@Entry
@Component
struct TextInputExample {
  build() {
    Row() {
      Column() {
        Text('Automatic spacing: Enabled').margin(5)
        TextInput({text: '中文 Text'})
          .enableAutoSpacing(true)
        Text('Automatic spacing: Disabled').margin(5)
        TextInput({text: '中文Text'})
          .enableAutoSpacing(false)
      }.height('100%')
    }
    .width('60%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/QT2qXYlkSEKsCy39Xy8G6g/en-us_image_0000002568685379.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6CDF78527043977E7E28FA78B89DD3418C3C0A401C32F4C29C616302C42E3FA1)

## Example 22 Setting the Normal and Overflow Colors of the Character Counter

This example demonstrates how to set the normal and overflow colors of the character counter using the **counterTextColor** and **counterTextOverflowColor** parameters (available since API version 22) of the [showCounter](#showcounter11) attribute.

import { ColorMetrics } from '@kit.ArkUI';

// xxx.ets
@Entry
@Component
struct TextInputExample {
  @State text: string = '';
  controller: TextInputController = new TextInputController();

  build() {
    Column() {
      TextInput({ text: this.text, controller: this.controller })
        .placeholderFont({ size: 16, weight: 400 })
        .width(336)
        .height(56)
        .maxLength(6)
        .showCounter(true, {
          thresholdPercentage: 50,
          highlightBorder: true,
          counterTextColor: ColorMetrics.resourceColor(Color.Red),
          counterTextOverflowColor: ColorMetrics.resourceColor(Color.Orange)
        })
        .onChange((value: string) => {
          this.text = value;
        })
    }.width('100%').height('100%').backgroundColor('#F1F3F5')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/S9y5bNzSQd6wV2d0IxyCJA/en-us_image_0000002568765389.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B9448181893225243B7223182BC8F6A3B858A7C393DA55BCE1A56E6506B61754)

## Example 23: Setting the Placeholder Rich Text Style

This example demonstrates how to set the placeholder rich text style using the [setStyledPlaceholder](../text-box-component-common-apis/document.md#setstyledplaceholder22) API, available since API version 22.

// xxx.ets
import { LengthMetrics } from '@kit.ArkUI';
@Entry
@Component
struct TextInputExample  {
  styledString: MutableStyledString =
    new MutableStyledString("Text box rich text: Text",
      \[
        {
          start: 0,
          length: 7,
          styledKey: StyledStringKey.FONT,
          styledValue: new TextStyle({
            fontColor: Color.Orange,
            fontSize: LengthMetrics.fp(24)
          })
        },
        {
          start: 7,
          length: 4,
          styledKey: StyledStringKey.FONT,
          styledValue: new TextStyle({
            fontColor: Color.Gray,
            fontSize: LengthMetrics.fp(20),
            strokeWidth: LengthMetrics.px(-5),
            strokeColor: Color.Black,
          })
        },
        {
          start: 0,
          length: 1,
          styledKey: StyledStringKey.PARAGRAPH\_STYLE,
          styledValue: new ParagraphStyle({
            textVerticalAlign: TextVerticalAlign.CENTER
          })
        }
      \]);
  controllerInput: TextInputController = new TextInputController();

  aboutToAppear() {
    this.controllerInput.setStyledPlaceholder(this.styledString)
  }

  build() {
    Scroll() {
      Column() {
        Text ("TextInput Placeholder Rich Text")
          .fontSize(8)
        TextInput({
          controller: this.controllerInput
        })
          .fontSize(24)
          .margin(10)
      }
      .width('100%')
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3/v3/jpr0XtaxRNugaF8t0W8dgQ/en-us_image_0000002537765664.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D2FB4FE558EE8080E4C20F375344EB0F5B5B7FC2430F98DAEC826A7B41540B59)

## Example 24 Setting Input Method Extension Information

This example demonstrates how to set input method extension information using the **setExtraConfig** method of [IMEClient](../text-component-common-apis/document.md#imeclient20), available since API version 22.

// xxx.ets
@Entry
@Component
struct TextInputExample {
  build() {
    Column() {
      TextInput({ text: 'Execute the onWillAttachIME callback before starting the input method.'})
        .onWillAttachIME((client: IMEClient) => {
          client.setExtraConfig({
            customSettings: {
              name: "TextInput", // Custom property
              id: client.nodeId // Custom Property
            }
          })
        })
    }.height('100%')
  }
}
