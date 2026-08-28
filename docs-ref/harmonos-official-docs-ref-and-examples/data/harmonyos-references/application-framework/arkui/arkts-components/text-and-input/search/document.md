# Search

The **Search** component provides an area for users to enter search queries.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/XRni8Tb4Q2OS01MvJAvT-Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BCE30DCF3EFED56B9B671CF544954F9B200339E3FEEA406129769FC522900EF9)

This component is supported since API version 8. Updates will be marked with a superscript to indicate their earliest API version.

This component supports plain text only. For rich text, use the [RichEditor](../richeditor/document.md) component.

#### Child Components

Not supported

#### APIs

Search(options?: SearchOptions)

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [SearchOptions](#searchoptions18) | No | Initialization options of the **Search** component. |

#### SearchOptions18+

Describes the initialization options of the **Search** component.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/DDZYx7GXTkGm2inIB9OK3g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A351A2B74498656E8A96F15C00ED105F6421CE4F3F15F99B19BEB7A2FB4BDB2D)

To standardize anonymous object definitions, the element definitions here have been revised in API version 18. While historical version information is preserved for anonymous objects, there may be cases where the outer element's @since version number is higher than inner elements'. This does not affect interface usability.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| value8+ | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 
Sets the text input in the search text box.

Since API version 10, this parameter supports two-way binding through [$$](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-two-way-sync).

Since API version 18, this parameter supports two-way binding through [!!](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-new-binding#two-way-binding-between-built-in-component-parameters).

**Atomic service API**: This API can be used in atomic services since API version 11.

The Resource type is supported since API version 20.

 |
| placeholder8+ | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 

Text displayed when there is no input.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| icon8+ | string | No | Yes | 

Path to the search icon. By default, the system search icon is used.

**NOTE**

The icon data source supports both [relative paths](../../images-and-videos/image/document.md#example-25-displaying-an-image-using-a-relative-path) and network images.

\- The supported formats include PNG, JPG, BMP, SVG, GIF, pixelmap, and HEIF.

\- The Base64 string is supported in the following format: data:image/\[png|jpeg|bmp|webp|heif\];base64,\[base64 data\], where \[base64 data\] is a Base64 string.

If this attribute and the **searchIcon** attribute are both set, the **searchIcon** attribute takes precedence.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| controller8+ | [SearchController](#searchcontroller) | No | Yes | 

Controller of the **Search** component.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |

#### Attributes

In addition to the [universal attributes](../../universal-attributes/document.md), the following attributes are supported.

#### \[h2\]searchButton

searchButton(value: ResourceStr, option?: SearchButtonOptions)

Sets the text on the search button located next to the search text box.

Clicking the search button triggers both **onSubmit** and **onClick** callbacks.

The default font size on wearable devices is 18 fp.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | Yes | 
Text on the search button located next to the search text box.

The Resource type is supported since API version 20.

 |
| option | [SearchButtonOptions](#searchbuttonoptions10) | No | 

Text style of the search button located next to the search text box.

Default value:

{

fontSize: '16fp',

fontColor: '#ff3f97e9'

}

 |

#### \[h2\]placeholderColor

placeholderColor(value: ResourceColor)

Sets the placeholder text color. The default value on wearable devices is **'#99ffffff'**.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | Yes | 
Placeholder text color.

Default value: **'#99182431'**

 |

#### \[h2\]placeholderFont

placeholderFont(value?: Font)

Placeholder text style, including the font size, font weight, font family, and font style.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [Font](../../common-definitions/basic-types/document.md#font) | No | Placeholder text style. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/Ji2GR_-ZS5WZGJPX7km9Ng/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=99E225D97845427C315DABD15CB92D81D1B6B909427E87B8A3227965AC2B3191)

You can use [loadFontSync](../../../../../graphics/arkgraphics-2d/arkts-apis/ohos-graphics-text-text/document.md#loadfontsync) to register custom fonts.

#### \[h2\]textFont

textFont(value?: Font)

Style of the text entered in the search box, including the font size, font weight, font family, and font style.

The default font size on wearable devices is 18 fp.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [Font](../../common-definitions/basic-types/document.md#font) | No | Text font of the search text box. |

#### \[h2\]textAlign9+

textAlign(value: TextAlign)

Sets the text alignment mode in the search text box. Currently, the following alignment modes are supported: **TextAlign.Start**, **TextAlign.Center**, and **TextAlign.End**. **TextAlign.JUSTIFY** behaves the same as **TextAlign.Start**.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [TextAlign](../../common-definitions/enums/document.md#textalign) | Yes | 
Text alignment mode in the search text box.

Default value: **TextAlign.Start**

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c/v3/KbuzbrrPS8yvJKK3cB_GaQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=78A57CA7C494BA44D5E30B7A5D4B0EF906D52D664962939C3BDE9A3E61CE8CCE)

**textAlign** only adjusts the overall text layout and does not affect character display order. For character display order adjustment, see [Bidirectional Text Layout and Alignment](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-internationalization#bidirectional-text-layout-and-alignment).

#### \[h2\]copyOption9+

copyOption(value: CopyOptions)

Sets whether the input text can be copied. If this attribute is set to **CopyOptions.None**, the **Search** component supports paste and select-all operations, while other operations such as copy, cut, translate, and share, as well as the Celia Writer assisted writing feature, are disabled.

Dragging is not allowed when **CopyOptions.None** is set.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [CopyOptions](../../common-definitions/enums/document.md#copyoptions9) | Yes | 
Whether the input text can be copied.

Default value: **CopyOptions.LocalDevice**

 |

#### \[h2\]searchIcon10+

searchIcon(value: IconOptions | SymbolGlyphModifier)

Sets the style of the search icon on the left.

The default icon size on wearable devices is 16 vp.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [IconOptions](#iconoptions10) | [SymbolGlyphModifier](../text-box-component-common-apis/document.md#symbolglyphmodifier12) | Yes | 
Style of the search icon on the left.

Default value in light mode:

{

size: '16vp',

color: '#99000000',

src: ' '

}

Default value in dark mode:

{

size: '16vp',

color: '#99ffffff',

src: ' '

}

 |

#### \[h2\]cancelButton10+

cancelButton(value: CancelButtonOptions | CancelButtonSymbolOptions)

Sets the style of the cancel button on the right. For details, see [Example 2: Setting Search and Delete Icons](#example-2-setting-search-and-delete-icons) and [Example 11: Setting a Custom Symbol-Type Cancel Button](#example-11-setting-a-custom-symbol-type-cancel-button).

The default icon size on wearable devices is 18 fp.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [CancelButtonOptions](#cancelbuttonoptions12) | [CancelButtonSymbolOptions](#cancelbuttonsymboloptions12) | Yes | 
Style of the cancel button on the right.

Default value:

{

style: CancelButtonStyle.INPUT,

icon: {

size: '16vp',

color: '#99ffffff',

src: ' '

}

}

When style is set to **CancelButtonStyle.CONSTANT**, the cancel button is displayed in a default style.

 |

#### \[h2\]fontColor10+

fontColor(value: ResourceColor)

Sets the font color of the input text. **fontSize**, **fontStyle**, **fontWeight**, and **fontFamily** are set in the [textFont](#textfont) attribute.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | Yes | 
Font color of the input text.

Default value: **'#FF182431'**

Default value on wearable devices: \*\*'#dbffffff' \*\*

 |

#### \[h2\]caretStyle10+

caretStyle(value: CaretStyle)

Sets the caret style.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [CaretStyle](../text-component-common-apis/document.md#caretstyle10) | Yes | 
Caret style.

Default value:

{

width: '2.0vp',

color: '#007DFF'

}

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/MQQ7OH3ISjij3qGozKlV0g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=808399BBA95905109C54E9B7D4436BE41CC81061931FC0361BDB5850480CC2FB)

Since API version 12, this API can be used to set the text handle color, which is the same as the caret color.

#### \[h2\]enableKeyboardOnFocus10+

enableKeyboardOnFocus(value: boolean)

Sets whether to pop up the soft keyboard when the **Search** component obtains focus in a way other than clicking.

Since API version 10, the **Search** component is bound to the input method by default when it obtains focus.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | boolean | Yes | 
Whether to automatically pop up the soft keyboard when the **Search** component gains focus.

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

**true**: Tapping, long-pressing, double-tapping, triple-tapping, or right-clicking the text box will not trigger the system text selection menu.

**false**: Tapping, long-pressing, double-tapping, triple-tapping, or right-clicking the text box will trigger the system text selection menu.

Default value: **false**

 |

#### \[h2\]customKeyboard10+

customKeyboard(value: CustomBuilder | ComponentContent | undefined, options?: KeyboardOptions)

Sets the custom keyboard.

When a custom keyboard is set, activating the text box opens the specified custom component, instead of the system input method.

The custom keyboard's height can be set through the **height** attribute of the custom component's root node, and its width is fixed at the default value.

The custom keyboard is presented by overlaying the original screen. It is not compressed or lifted if avoid mode is not enabled or avoidance is not needed for the text box.

The custom keyboard cannot obtain focus, but it blocks gesture events.

By default, the custom keyboard is closed when the input component loses focus. You can also use the [stopEditing](#stopediting10) API to close the keyboard.

When setting a custom keyboard, you can bind the [onKeyPreIme](../../universal-events/basic-input-events/key-event/document.md#onkeypreime12) event to prevent input from the physical keyboard.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/1_7_MwY7RXOxxGxhEqP1WQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F640774B5313CB9E09F185CEA39A2A5F9DB11A55A5332F3D4CE65B4EBACA1DDD)

This API cannot be called within [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier).

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [CustomBuilder](../../common-definitions/basic-types/document.md#custombuilder8) | [ComponentContent](../../../arkts-api/ui/arkui/componentcontent/document.md#componentcontent-1)22+ | undefined22+ | Yes | Custom keyboard. If the value is **undefined**, the custom keyboard is closed. |
| options12+ | [KeyboardOptions](../richeditor/document.md#keyboardoptions12) | No | Whether to support keyboard avoidance. |

#### \[h2\]type11+

type(value: SearchType)

Sets the text box type.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [SearchType](#searchtype11) | Yes | 
Text box type.

Default value: **SearchType.NORMAL**

 |

#### \[h2\]maxLength11+

maxLength(value: number)

Sets the maximum number of characters for text input. By default, there is no maximum number of characters. When the maximum number is reached, no more characters can be entered.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | Yes | 
Maximum number of characters for text input.

When the value is less than 0, the default value is used and no limit is applied.

 |

#### \[h2\]enterKeyType12+

enterKeyType(value: EnterKeyType)

Sets the type of the Enter key.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [EnterKeyType](../textinput/document.md#enterkeytype) | Yes | 
Type of the Enter key.

Default value: **EnterKeyType.Search**

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

#### \[h2\]lineHeight12+

lineHeight(value: number | string | Resource)

Sets the text line height. If the value is less than or equal to **0**, the line height is not limited and the font size is adaptive. If the value is of the number type, the unit fp is used.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | string | [Resource](../../common-definitions/basic-types/document.md#resource) | Yes | Text line height. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/LWF0-0CFQzGG0yp6hE8i3w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=05193F90C5A76AB856A0C1E154B715DA305258504B4008AED5B3545D57D778AD)

If certain characters have significantly taller glyphs than others in the same line, layout anomalies such as clipping, overlapping, or misalignment may occur. In this case, adjust component attributes such as height and line height to ensure proper layout rendering.

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/W1Njb9bTS5yPmkb7wbPkiQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6C8C8E65B1AF9DD16AD6AF3B7483567F32FC04AC63BDDC36A30539A70062FF5B)

When the bottom contour of a character intersects with the decoration, underline avoidance is triggered, commonly affecting characters like "g", "j", "y", "q", and "p."

If the decoration color is set to **Color.Transparent**, it inherits the text color of the first character in each line. If the decoration color is set to **"#00FFFFFF"**, the line becomes fully transparent.

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

#### \[h2\]selectedBackgroundColor12+

selectedBackgroundColor(value: ResourceColor)

Sets the background color of the selected text. If the opacity is not set, a 20% opacity will be used.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | Yes | Background color of the selected text. |

#### \[h2\]inputFilter12+

inputFilter(value: ResourceStr, error?: Callback< string >)

Sets the regular expression for input filtering. Only inputs that comply with the regular expression can be displayed. Other inputs are filtered out.

For single-character input scenarios, only single-character matching is supported; for multi-character input scenarios (such as pasting), string matching is supported.

If **inputFilter** is set and the entered characters are not null, the filtering effect attached to the text box type (specified through the **type** attribute) does not take effect.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | Yes | Regular expression. |
| error | Callback< string > | No | Filtered-out content to return when regular expression matching fails. |

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

For the setting to take effect, this attribute must be used together with [maxFontSize](#maxfontsize12) or layout constraint settings.

When the adaptive font size is used, the **fontSize** settings do not take effect.

If **minFontSize** is less than or equal to 0, the adaptive font size does not take effect. In this case, the value of **size** in the [textFont](#textfont) attribute takes effect. If **size** is not set, the default value applies.

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

For the setting to take effect, this attribute must be used together with [minFontSize](#minfontsize12) or layout constraint settings.

When the adaptive font size is used, the **fontSize** settings do not take effect.

If **maxFontSize** is less than or equal to 0 or **maxFontSize** is less than **minFontSize**, the adaptive font size does not take effect. In this case, the value of **size** in the [textFont](#textfont) attribute takes effect. If **size** is not set, the default value applies.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | string | [Resource](../../common-definitions/basic-types/document.md#resource) | Yes | 
Maximum font size.

Unit: [fp](../../common-definitions/pixel-units/document.md)

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

Before use, you need to configure the [configuration.json](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-configuration-file#tags-in-the-configuration-file) and [app.json5](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-configuration-file) files in the project. For details, see [Example 19: Setting the Minimum and Maximum Font Scale Factors](#example-19-setting-the-minimum-and-maximum-font-scale-factors).

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

A value less than 1 is handled as **1**. Abnormal values are ineffective by default.

After the **maxFontScale** attribute is set, the content of the **Search** component can be scaled up to 2 times at most.

Before use, you need to configure the [configuration.json](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-configuration-file#tags-in-the-configuration-file) and [app.json5](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-configuration-file) files in the project. For details, see [Example 19: Setting the Minimum and Maximum Font Scale Factors](#example-19-setting-the-minimum-and-maximum-font-scale-factors).

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/ga9X7j4dQDudAeCsRIEXjA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1C035D43F467F97E167D1AA136DA21EAB21049C93D2568F6E8F9B94A43499AEA)

Preview text represents a temporary, uncommitted input state. This feature requires support from the input method with pre-commit text functionality enabled. During text entry, when candidate words have not been confirmed yet, the text box displays marked text in a provisional state. For example, when users enter Chinese using Pinyin input, the Pinyin letters appear in the input box before a word is selected from the candidate word list. This intermediate state constitutes preview text.

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

**true**: Haptic feedback is enabled. **false**: Haptic feedback is disabled.

Default value: **true**

 |

#### \[h2\]autoCapitalizationMode20+

autoCapitalizationMode(mode: AutoCapitalizationMode)

Sets the text auto-capitalization mode. This API provides the capability, but actual implementation depends on the input method application.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| mode | [AutoCapitalizationMode](../text-component-common-apis/document.md#autocapitalizationmode20) | Yes | Auto-capitalization mode. The default state is inactive. |

#### \[h2\]keyboardAppearance15+

keyboardAppearance(appearance: Optional<KeyboardAppearance>)

Sets the keyboard appearance for the text box. When the keyboard style is set to immersive mode, the keyboard blends with the background in a semi-transparent manner. This API provides only the capability; the actual implementation depends on the input method application.

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
Text stroke width. When the unit of **LengthMetrics** is px:

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
Whether to prevent the back key event from being propagated.

**true**: Propagation is prevented. **false**: Propagation is allowed.

Default value: **true** Invalid values are treated as the default value.

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

**true**: Enabled. **false**: Disabled.

Default value: **false**

 |

#### IconOptions10+

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| size | [Length](../../common-definitions/basic-types/document.md#length) | No | Yes | Icon size. It cannot be set in percentage. |
| color | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | No | Yes | Icon color. |
| src | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | Image source of the icon. |

#### SearchButtonOptions10+

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| fontSize | [Length](../../common-definitions/basic-types/document.md#length) | No | Yes | Font size of the button. It cannot be set in percentage. **Atomic service API**: This API can be used in atomic services since API version 11. |
| fontColor | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | No | Yes | Font color of the button. **Atomic service API**: This API can be used in atomic services since API version 11. |
| autoDisable18+ | Boolean | No | Yes | 
Whether to disable the search button when there is no text input.

Default value: **false**

**true**: The search button is disabled when there is no text input. **false**: The search button remains enabled regardless of the text input.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |

#### CancelButtonStyle10+

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Description |
| :-- | :-- |
| CONSTANT | The Cancel button is always displayed. |
| INVISIBLE | The Cancel button is always hidden. |
| INPUT | The Cancel button is displayed when there is text input. |

#### SearchType11+

Enumerates the text input types of a search box.

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

In this mode, the following characters are allowed: digits, spaces, plus signs (+), hyphens (-), asterisks (\*), and number signs (#), opening parentheses ((), and closing parenthesis ()); the length is not limited.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| EMAIL | 5 | 

Email address input mode.

This mode accepts only digits, letters, underscores (\_), dots (.), and the following special characters: ! # $ % & ' \* + - / = ? ^ \` { | } ~ @ (which can only appear once)

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| NUMBER\_DECIMAL12+ | 12 | 

Number input mode with a decimal point.

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

#### CancelButtonOptions12+

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| style | [CancelButtonStyle](#cancelbuttonstyle10) | No | Yes | Display state of the Cancel button on the right. |
| icon | [IconOptions](#iconoptions10) | No | Yes | Icon of the Cancel button on the right. |

#### CancelButtonSymbolOptions12+

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| style | [CancelButtonStyle](#cancelbuttonstyle10) | No | Yes | Display state of the Cancel button on the right. |
| icon | [SymbolGlyphModifier](../text-box-component-common-apis/document.md#symbolglyphmodifier12) | No | Yes | Symbol icon of the Cancel button on the right. |

#### Events

In addition to the [universal events](../../universal-events/document.md), the following events are supported.

#### \[h2\]onSubmit

onSubmit(callback: Callback<string>)

Called when the search icon, search button, or soft keyboard search button is clicked.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | Callback<string> | Yes | Search submission callback, which returns the text content currently in the search box. |

#### \[h2\]onSubmit14+

onSubmit(callback: SearchSubmitCallback)

Invoked when the search icon, search button, or soft keyboard search button is clicked. The submission event provides a method to maintain the edit state of the **Search** component.

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | [SearchSubmitCallback](#searchsubmitcallback14) | Yes | Callback invoked when the search icon, search button, or soft keyboard search button is clicked. |

#### \[h2\]onChange

onChange(callback: EditableTextOnChangeCallback)

Called when the input in the text box changes.

In this callback, if caret operations are performed, you must adjust the caret logic based on the **previewText** parameter to ensure it works seamlessly within the preview display scenario.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | [EditableTextOnChangeCallback](../text-component-common-apis/document.md#editabletextonchangecallback12) | Yes | Callback invoked when the input in the text box changes. |

#### \[h2\]onCopy

onCopy(callback:Callback<string>)

Called when a copy operation is performed.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | Callback<string> | Yes | Callback used to return the copied text content. |

#### \[h2\]onCut

onCut(callback:Callback<string>)

Called when a cut operation is performed.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | Callback<string> | Yes | Callback used to return the cut text content. |

#### \[h2\]onPaste

onPaste(callback:OnPasteCallback )

Called when a paste operation is performed.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | [OnPasteCallback](../textinput/document.md#onpastecallback18) | Yes | Callback used to return the pasted text content. |

#### \[h2\]onTextSelectionChange10+

onTextSelectionChange(callback: OnTextSelectionChangeCallback)

Called when the text selection changes or the caret position changes during editing.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | [OnTextSelectionChangeCallback](../textinput/document.md#ontextselectionchangecallback18) | Yes | Callback for text selection changes or caret position changes. |

#### \[h2\]onContentScroll10+

onContentScroll(callback: OnContentScrollCallback)

Called when the text content is scrolled.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | [OnContentScrollCallback](../textinput/document.md#oncontentscrollcallback18) | Yes | Callback for text content scrolling. |

#### \[h2\]onEditChange12+

onEditChange(callback: Callback< boolean >)

Called when the input state changes. The text box is in the editing state when it has the caret placed in it, and is in the non-editing state otherwise.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | Callback< boolean > | Yes | Callback for editing state changes. The value **true** indicates that the text is being inserted, and **false** indicates that the text box is out of focus and text cannot be inserted. |

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
Callback invoked when text is inserted.

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
Callback invoked when text is deleted.

It is available only for system input methods.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/9fdxPvUUQAKya4ANJEPAxg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FDBDDD78A5CC062FCE8B8D101B9D6875063BB251AA6F1BBFB1BCEEB869A1F27B)

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
Callback invoked when the text content is about to change.

Returning **true** allows the change to proceed, while returning **false** cancels the change.

 |

#### \[h2\]onWillAttachIME20+

onWillAttachIME(callback: Callback<IMEClient>)

Called when the search box is about to be bound to an input method.

From API version 22, the [setExtraConfig](../text-component-common-apis/document.md#setextraconfig22) method of [IMEClient](../text-component-common-apis/document.md#imeclient20) can be called to set input method extension information. After the input method is bound, it receives this extension information, which can be used to implement custom functionality.

**IMEClient** is valid only during the execution of **onWillAttachIME** and cannot be called asynchronously.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/0z-Gt_e_T8WHAbE-cecnBw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=51EB9E0804BADCFD073FF4DCA6BA745A0A8208291A950718723C4ED2373440EC)

This API cannot be called within [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier).

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | Callback<[IMEClient](../text-component-common-apis/document.md#imeclient20)\> | Yes | Called when the search box is about to be bound to an input method. |

#### SearchController

The controller for the **Search** component inherits from [TextContentControllerBase](../text-box-component-common-apis/document.md#textcontentcontrollerbase). The APIs involved are as follows: [getTextContentRect](../text-box-component-common-apis/document.md#gettextcontentrect), [getTextContentLineCount](../text-box-component-common-apis/document.md#gettextcontentlinecount), [getCaretOffset](../text-box-component-common-apis/document.md#getcaretoffset11), [addText](../text-box-component-common-apis/document.md#addtext15), [deleteText](../text-box-component-common-apis/document.md#deletetext15), [getSelection](../text-box-component-common-apis/document.md#getselection15), [clearPreviewText](../text-box-component-common-apis/document.md#clearpreviewtext17), and [setStyledPlaceholder](../text-box-component-common-apis/document.md#setstyledplaceholder22).

## Objects to Import

controller: SearchController = new SearchController();

#### \[h2\]constructor

constructor()

A constructor used to create a **SearchController** object.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### \[h2\]caretPosition

caretPosition(value: number): void

Sets the position of the caret.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | Yes | 
Length from the start of the character string to the position where the caret is located.

Values less than 0 are treated as **0**. Values greater than the string length are treated as the string length.

 |

#### \[h2\]stopEditing10+

stopEditing(): void

Exits the editing state.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### \[h2\]setTextSelection12+

setTextSelection(selectionStart: number, selectionEnd: number, options?: SelectionOptions): void;

Sets the text selection range and highlights the selected text when the component is focused. This API works only when the value of **selectionStart** is less than that of **selectionEnd**.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| selectionStart | number | Yes | 
Start position of the text selection range. The start position of text in the text box is 0.

A value less than 0 is handled as **0**. A value greater than the maximum text length is handled as the maximum text length.

 |
| selectionEnd | number | Yes | 

End position of the text selection range.

A value less than 0 is handled as **0**. A value greater than the maximum text length is handled as the maximum text length.

 |
| options | [SelectionOptions](../text-box-component-common-apis/document.md#selectionoptions12) | No | 

Configuration options for text selection.

Default value: **MenuPolicy.DEFAULT**

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c/v3/4l_slezATPyIq4NepUEpgQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B08035D8BC16AF6F940AA5F25C8952E7BA95847BAF2CF4A0D1AB5DEF167B6F29)

If **selectionStart** or **selectionEnd** is set to **undefined**, the value **0** will be used.

If **selectionMenuHidden** is set to **true** or a 2-in-1 device is used, calling **setTextSelection** does not display the text selection menu even when **options** is set to **MenuPolicy.SHOW**.

If the selected text contains an emoji, the emoji is selected when its start position is within the text selection range.

#### SearchSubmitCallback14+

type SearchSubmitCallback = (searchContent: string, event?: SubmitEvent) => void

Called when the search icon, search button, or soft keyboard search button is clicked.

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| searchContent | string | Yes | Current text input. |
| event | [SubmitEvent](../textinput/document.md#submitevent11) | No | Submit event. |

#### Example

## Example 1: Setting and Obtaining the Caret Position

This example demonstrates how to set and obtain the caret position using [controller](#searchcontroller), available since API version 8.

// xxx.ets
@Entry
@Component
struct SearchExample {
  @State changeValue: string = '';
  @State submitValue: string = '';
  @State positionInfo: CaretOffset = { index: 0, x: 0, y: 0 };
  controller: SearchController = new SearchController();

  build() {
    Column({space: 10}) {
      Text('onSubmit:' + this.submitValue).fontSize(18).margin(15)
      Text('onChange:' + this.changeValue).fontSize(18).margin(15)
      Search({ value: this.changeValue, placeholder: 'Type to search...', controller: this.controller })
        .searchButton('SEARCH')
        .width('95%')
        .height(40)
        .backgroundColor('#F5F5F5')
        .placeholderColor(Color.Grey)
        .placeholderFont({ size: 14, weight: 400 })
        .textFont({ size: 14, weight: 400 })
        .onSubmit((value: string) => {
          this.submitValue = value;
        })
        .onChange((value: string) => {
          this.changeValue = value;
        })
        .margin(20)
      Button('Set caretPosition 1')
        .onClick(() => {
          // Move the caret to after the first entered character.
          this.controller.caretPosition(1);
        })
      Button('Get CaretOffset')
        .onClick(() => {
          this.positionInfo = this.controller.getCaretOffset();
        })
    }.width('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/Khnrs6c1SEShsh3T51eMQw/en-us_image_0000002568685391.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=10A332AB740898C33D5E34472A4D8ADC4FCBC745228D5FAE4E89892F35DFF3BB)

## Example 2: Setting Search and Delete Icons

This example demonstrates the effect of setting the search and delete icons using the [searchButton](#searchbutton) (available since API version 8), [searchIcon](#searchicon10) (available since API version 10), and [cancelButton](#cancelbutton10) (available since API version 10) attributes.

// xxx.ets
@Entry
@Component
struct SearchExample {
  @State changeValue: string = '';
  @State submitValue: string = '';

  build() {
    Column() {
      Text('onSubmit:' + this.submitValue).fontSize(18).margin(15)
      Search({ value: this.changeValue, placeholder: 'Type to search...' })
        .searchButton('SEARCH')
        .searchIcon({
          src: $r('sys.media.ohos\_ic\_public\_search\_filled')
        })
        .cancelButton({
          style: CancelButtonStyle.CONSTANT,
          icon: {
            src: $r('sys.media.ohos\_ic\_public\_cancel\_filled')
          }
        })
        .width('90%')
        .height(40)
        .maxLength(20)
        .backgroundColor('#F5F5F5')
        .placeholderColor(Color.Grey)
        .placeholderFont({ size: 14, weight: 400 })
        .textFont({ size: 14, weight: 400 })
        .onSubmit((value: string) => {
          this.submitValue = value;
        })
        .onChange((value: string) => {
          this.changeValue = value;
        })
        .margin(20)
    }.width('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/b1Y5s1d0RaKlkknqN8QoMQ/en-us_image_0000002568765401.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EAC9E0D058C3ADC3120688A6D45C241F54D5B466B5E677BCF0CC8497264B4C61)

## Example 3: Implementing a Custom Keyboard

This example implements a custom keyboard using the [customKeyboard](#customkeyboard10) attribute (available since API version 10) to set the input parameter type in **value** to [CustomBuilder](../../common-definitions/basic-types/document.md#custombuilder8) and [ComponentContent](../../../arkts-api/ui/arkui/componentcontent/document.md#componentcontent-1).

Since API version 22, [ComponentContent](../../../arkts-api/ui/arkui/componentcontent/document.md#componentcontent-1) is added to the input parameter type of [customKeyboard](#customkeyboard10).

// xxx.ets
import { ComponentContent } from '@kit.ArkUI';
class BuilderParams {
  inputValue: string;
  controller: SearchController;

  constructor(inputValue: string, controller: SearchController) {
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
struct SearchExample {
  controller: SearchController = new SearchController();
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
      Search({ controller: this.builderParam.controller, value: this.builderParam.inputValue })
        .customKeyboard(this.componentContent, { supportAvoidance: this.supportAvoidance })
        .margin(10).border({ width: 1 }).height('48vp')

      Text('ComponentContent').margin(10).border({ width: 1 })
      Search({ controller: this.builderParam.controller, value: this.builderParam.inputValue })
        .customKeyboard(CustomKeyboardBuilder(this.builderParam), { supportAvoidance: this.supportAvoidance })
        .margin(10).border({ width: 1 }).height('48vp')
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/cVSxmVrAQS6FaxhnO8ov-A/en-us_image_0000002537765676.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1E48F05D3905DA4D0D54588B3B35C799B305226754C1C74409E3D7CA62DCBFD2)

## Example 4: Setting the Enter Key Type

This example demonstrates how to dynamically switch the enter key type using the [enterKeyType](#enterkeytype12) attribute, available since API version 12.

// xxx.ets
@Entry
@Component
struct SearchExample {
  @State text: string = '';
  @State enterTypes: Array<EnterKeyType> = \[EnterKeyType.Go, EnterKeyType.Search, EnterKeyType.Send, EnterKeyType.Done, EnterKeyType.Next, EnterKeyType.PREVIOUS, EnterKeyType.NEW\_LINE\];
  @State index: number = 0;
  build() {
    Column({ space: 20 }) {
      Search({ placeholder: 'Enter text', value: this.text })
        .width(380)
        .enterKeyType(this.enterTypes\[this.index\])
        .onChange((value: string) => {
          this.text = value;
        })
        .onSubmit((value: string) => {
          console.info("trigger search onsubmit" + value);
        })

      Button('Change EnterKeyType').onClick(() => {
        this.index = (this.index + 1) % this.enterTypes.length;
      })
    }.width('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/nAqkZgxqSeWNIynt-KJibg/en-us_image_0000002537925616.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2DC0FB41811E4D5493B31D5D5BD4198F9C5F04C85CE57039599C3BF3E02A9EA8)

## Example 5: Setting the Text Style

This example showcases various text styles by using the [lineHeight](#lineheight12), [letterSpacing](#letterspacing12), and [decoration](#decoration12) attributes, available since API version 12.

// xxx.ets
@Entry
@Component
struct SearchExample {
  build() {
    Row() {
      Column() {
        Text('lineHeight').fontSize(9).fontColor(0xCCCCCC)
        Search({value: 'lineHeight unset'})
          .border({ width: 1 }).padding(10)
        Search({value: 'lineHeight 15'})
          .border({ width: 1 }).padding(10).lineHeight(15)
        Search({value: 'lineHeight 30'})
          .border({ width: 1 }).padding(10).lineHeight(30)

        Text('letterSpacing').fontSize(9).fontColor(0xCCCCCC)
        Search({value: 'letterSpacing 0'})
          .border({ width: 1 }).padding(5).letterSpacing(0)
        Search({value: 'letterSpacing 3'})
          .border({ width: 1 }).padding(5).letterSpacing(3)
        Search({value: 'letterSpacing -1'})
          .border({ width: 1 }).padding(5).letterSpacing(-1)

        Text('decoration').fontSize(9).fontColor(0xCCCCCC)
        Search({value: 'LineThrough, Red'})
          .border({ width: 1 }).padding(5)
          .decoration({type: TextDecorationType.LineThrough, color: Color.Red})
        Search({value: 'Overline, Red, DOTTED'})
          .border({ width: 1 }).padding(5)
          .decoration({type: TextDecorationType.Overline, color: Color.Red, style: TextDecorationStyle.DOTTED})
        Search({value: 'Underline, Red, WAVY'})
          .border({ width: 1 }).padding(5)
          .decoration({type: TextDecorationType.Underline, color: Color.Red, style: TextDecorationStyle.WAVY})
      }.height('90%')
    }
    .width('90%')
    .margin(10)
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/akZxQpOERLC8ZAXAtKIG4w/en-us_image_0000002568685393.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F1E3147C8488CA6A33F93A22E7B4409CF5F49CFE7234A43947E81E5C069B891F)

## Example 6: Setting Text Feature Effects

This example demonstrates how to display text with different font features using the [fontFeature](#fontfeature12) attribute, available since API version 12.

// xxx.ets
@Entry
@Component
struct SearchExample {
  @State text1: string = 'This is ss01 on : 0123456789';
  @State text2: string = 'This is ss01 off: 0123456789';

  build() {
    Column(){
      Search({value: this.text1})
        .margin({top:200})
        .fontFeature("\\"ss01\\" on")
      Search({value: this.text2})
        .margin({top:10})
        .fontFeature("\\"ss01\\" off")
    }
    .width("90%")
    .margin("5%")
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/V_8dulHJTo21ndSme4Ra2A/en-us_image_0000002568765403.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=291A82E1B17C06B36DEEB174A9C7290161713EE0D6E56A962DD21B4961B1F055)

## Example 7: Setting Custom Keyboard Avoidance

This example implements the custom keyboard avoidance effect by configuring the [KeyboardOptions](../richeditor/document.md#keyboardoptions12) API (available since API version 12) through the [customKeyboard](#customkeyboard10) attribute (available since API version 10).

// xxx.ets
@Entry
@Component
struct SearchExample {
  controller: SearchController = new SearchController();
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
    }
    .backgroundColor(Color.Gray)
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

      Search({ controller: this.controller, value: this.inputValue })// Bind a custom keyboard.
        .customKeyboard(this.CustomKeyboardBuilder(), { supportAvoidance: this.supportAvoidance })
        .margin(10)
        .border({ width: 1 })
        .onChange((value: string) => {
          this.inputValue = value;
        })
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/2lPF6WMuTmiqSwuas8oATg/en-us_image_0000002537765678.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=59D706F0D63A3C7F3F4F86D79F329DB2F88BCAB59EFD7DE15B1490B7FEF49AB8)

## Example 8: Setting Text Auto-Adaptation

This example implements the text auto-adaptation effect by using the [minFontSize](#minfontsize12) and [maxFontSize](#maxfontsize12) attributes, both available since API version 12.

// xxx.ets
@Entry
@Component
struct SearchExample {
  build() {
    Row() {
      Column() {
        Text('adaptive font').fontSize(9).fontColor(0xCCCCCC)

        Search({value: 'This is the text without the adaptive font'})
          .width('80%').height(90).borderWidth(1)
        Search({value: 'This is the text without the adaptive font'})
          .width('80%').height(90).borderWidth(1)
          .minFontSize(4)
          .maxFontSize(40)
      }.height('90%')
    }
    .width('90%')
    .margin(10)
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/Cr-UidWgQGi1xiwgs_6B9A/en-us_image_0000002537925618.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=40D95BA844B68E6654A1D158A6CC1CBA6B838D8E8075F4E637B70A7553C90C4C)

## Example 9: Setting Insert and Delete Callbacks

This example implements the text insertion and deletion effects using the [onWillInsert](#onwillinsert12), [onDidInsert](#ondidinsert12), [onWillDelete](#onwilldelete12), and [onDidDelete](#ondiddelete12) APIs, available since API version 12. The [onWillChange](#onwillchange15) API, available since API version 15, is used to display detailed information about the text content to be changed.

// xxx.ets
class ChangeState {
  changeContent: string = "";
  changePreviewOffset: number | undefined = 0;
  changePreviewValue: string | undefined = "";
  changeTextChangeRangeBeforeX: number | undefined = 0;
  changeTextChangeRangeBeforeY: number | undefined = 0;
  changeTextChangeRangeAfterX: number | undefined = 0;
  changeTextChangeRangeAfterY: number | undefined = 0;
  changeTextChangeOldContent: string | undefined = "";
  changeTextChangechangePreviewOffset: number | undefined = 0;
  changeTextChangechangePreviewValue: string | undefined = "";

  SetInfo(info: EditableTextChangeValue) {
    this.changeContent = info.content;
    this.changePreviewOffset = info.previewText?.offset;
    this.changePreviewValue = info.previewText?.value;
    this.changeTextChangeRangeBeforeX = info.options?.rangeBefore.start;
    this.changeTextChangeRangeBeforeY = info.options?.rangeBefore.end;
    this.changeTextChangeRangeAfterX = info.options?.rangeAfter.start;
    this.changeTextChangeRangeAfterY = info.options?.rangeAfter.end;
    this.changeTextChangeOldContent = info.options?.oldContent;
    this.changeTextChangechangePreviewOffset = info.options?.oldPreviewText.offset;
    this.changeTextChangechangePreviewValue = info.options?.oldPreviewText.value;
  }
}

@Entry
@Component
struct SearchExample {
  @State insertValue: string = "";
  @State deleteValue: string = "";
  @State insertOffset: number = 0;
  @State deleteOffset: number = 0;
  @State deleteDirection: number = 0;
  @State changeState1: ChangeState = new ChangeState();
  @State changeState2: ChangeState = new ChangeState();

  build() {
    Row() {
      Column() {
        Search({ value: "Insert callbacks are supported" })
          .height(60)
          .onWillInsert((info: InsertValue) => {
            this.insertValue = info.insertValue;
            return true;
          })
          .onWillChange((info: EditableTextChangeValue) => {
            this.changeState1.SetInfo(info);
            return true;
          })
          .onDidInsert((info: InsertValue) => {
            this.insertOffset = info.insertOffset;
          })

        Text("insertValue:" + this.insertValue + "  insertOffset:" + this.insertOffset).height(20)

        Blank(30)

        Text("context:" + this.changeState1.changeContent).height(20)
        Text("previewText-offset:" + this.changeState1.changePreviewOffset).height(20)
        Text("previewText-value:" + this.changeState1.changePreviewValue).height(20)
        Text("options-rangeBefore-start:" + this.changeState1.changeTextChangeRangeBeforeX).height(20)
        Text("options-rangeBefore-end:" + this.changeState1.changeTextChangeRangeBeforeY).height(20)
        Text("options-rangeAfter-start:" + this.changeState1.changeTextChangeRangeAfterX).height(20)
        Text("options-rangeAfter-end:" + this.changeState1.changeTextChangeRangeAfterY).height(20)
        Text("options-oldContent:" + this.changeState1.changeTextChangeOldContent).height(20)
        Text("options-oldPreviewText-offset:" + this.changeState1.changeTextChangechangePreviewOffset).height(20)
        Text("options-oldPreviewText-value:" + this.changeState1.changeTextChangechangePreviewValue).height(20)

        Search({ value: "Delete callbacks are supported" })
          .height(60)
          .onWillDelete((info: DeleteValue) => {
            this.deleteValue = info.deleteValue;
            this.deleteDirection = info.direction;
            return true;
          })
          .onWillChange((info: EditableTextChangeValue) => {
            this.changeState2.SetInfo(info);
            return true;
          })
          .onDidDelete((info: DeleteValue) => {
            this.deleteOffset = info.deleteOffset;
            this.deleteDirection = info.direction;
          })

        Text("deleteValue:" + this.deleteValue + "  deleteOffset:" + this.deleteOffset).height(20)
        Text("deleteDirection:" + (this.deleteDirection == 0 ? "BACKWARD" : "FORWARD")).height(20)

        Blank(30)

        Text("context:" + this.changeState2.changeContent).height(20)
        Text("previewText-offset:" + this.changeState2.changePreviewOffset).height(20)
        Text("previewText-value:" + this.changeState2.changePreviewValue).height(20)
        Text("options-rangeBefore-start:" + this.changeState2.changeTextChangeRangeBeforeX).height(20)
        Text("options-rangeBefore-end:" + this.changeState2.changeTextChangeRangeBeforeY).height(20)
        Text("options-rangeAfter-start:" + this.changeState2.changeTextChangeRangeAfterX).height(20)
        Text("options-rangeAfter-end:" + this.changeState2.changeTextChangeRangeAfterY).height(20)
        Text("options-oldContent:" + this.changeState2.changeTextChangeOldContent).height(20)
        Text("options-oldPreviewText-offset:" + this.changeState2.changeTextChangechangePreviewOffset).height(20)
        Text("options-oldPreviewText-value:" + this.changeState2.changeTextChangechangePreviewValue).height(20)

      }.width('100%')
    }
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/xRALIGYZRo2UUk6jwo38Zw/en-us_image_0000002568685395.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B0881D928422A197E9F4CDDBC11D62195D01F7EE280867C433087DCAB7740B93)

## Example 10: Setting Custom Menu Extensions

This example implements custom menu extension items for text using the [editMenuOptions](#editmenuoptions12) API (available since API version 12), allowing configuration of text content, icons, and callbacks. Menu data can also be configured through the [onPrepareMenu](../text-component-common-apis/document.md#properties-1) callback (available since API version 20).

// xxx.ets
@Entry
@Component
struct SearchExample {
  @State text: string = 'Search editMenuOptions';
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
    let targetIndex = menuItems.findIndex(item => item.id.equals(TextMenuItemId.AI\_WRITER));
    if (targetIndex !== -1) {
      menuItems.splice(targetIndex, 1); // Delete an element at the target index.
    }
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
      Search({ value: this.text })
        .width('95%')
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/cexSLzkgR1OK9K8HcqGYvw/en-us_image_0000002568765405.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B80A2220F3856E189C58A03B0A244F46E031E5F293B34AAACFF931E29721DA57)

## Example 11: Setting a Custom Symbol-Type Cancel Button

This example demonstrates how to use the [searchIcon](#searchicon10) and [cancelButton](#cancelbutton10) attributes to customize the style of the symbol-type cancel button on the right side of the text box, available since API version 10.

// xxx.ets
import { SymbolGlyphModifier } from '@kit.ArkUI';

@Entry
@Component
struct SearchExample {
  controller: SearchController = new SearchController();
  @State changeValue: string = '';
  @State submitValue: string = '';

  build() {
    Column() {
      Search({ value: this.changeValue, placeholder: 'Type to search...', controller: this.controller })
        .searchIcon(new SymbolGlyphModifier($r('sys.symbol.magnifyingglass')).fontColor(\[Color.Red\]))
        .cancelButton({
          style: CancelButtonStyle.CONSTANT,
          icon: new SymbolGlyphModifier($r('sys.symbol.xmark')).fontColor(\[Color.Green\])
        })
        .searchButton('SEARCH')
        .width('95%')
        .height(40)
        .backgroundColor('#F5F5F5')
        .placeholderColor(Color.Grey)
        .placeholderFont({ size: 14, weight: 400 })
        .textFont({ size: 14, weight: 400 })
        .margin(10)
    }
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0f/v3/WwfZ712KQhOgF-gs4rPazQ/en-us_image_0000002537765680.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=605D8E8DD0ED3DAB2B0E1EA337DCFD77FAAE1FE52824F95FF21E261BA644656F)

## Example 12: Setting Whether Text is Copyable

This example demonstrates how to set whether text is copyable using the [copyOption](#copyoption9) attribute, available since API version 9.

// xxx.ets

@Entry
@Component
struct SearchExample {
  controller: SearchController = new SearchController();
  @State copyValue: string = '';
  @State cutValue: string = '';

  build() {
    Column({ space: 3 }) {
      Text("copy: " + this.copyValue)
      Text("cut:" + this.cutValue)
      Search({ value: 'Search CopyOption:None', controller: this.controller })
        .width('95%')
        .height(40)
        .copyOption(CopyOptions.None)
        .onCopy((value: string) => {
          this.copyValue = value;
        })
        .onCut((value: string) => {
          this.cutValue = value;
        })
      Search({ value: 'Search CopyOption:InApp', controller: this.controller })
        .width('95%')
        .height(40)
        .copyOption(CopyOptions.InApp)
        .onCopy((value: string) => {
          this.copyValue = value;
        })
        .onCut((value: string) => {
          this.cutValue = value;
        })
      Search({ value: 'Search CopyOption:LocalDevice', controller: this.controller })
        .width('95%')
        .height(40)
        .copyOption(CopyOptions.LocalDevice)
        .onCopy((value: string) => {
          this.copyValue = value;
        })
        .onCut((value: string) => {
          this.cutValue = value;
        })
    }
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/fviwoa6XS6SqotW1mx_dUw/en-us_image_0000002537925620.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=977125E92B57E656A092C4F8C97AAD2D75303C5FB333853F63C91BC91E15CC53)

## Example 13: Setting the Horizontal Alignment, Caret Style, and Background Color of the Selected Text

This example demonstrates how to set the horizontal alignment, caret style, and background color of the selected text using the [textAlign](#textalign9) (available since API version 9), [caretStyle](#caretstyle10) (available since API version 10), and [selectedBackgroundColor](#selectedbackgroundcolor12) (available since API version 12) attributes.

// xxx.ets

@Entry
@Component
struct SearchExample {
  controller: SearchController = new SearchController();

  build() {
    Column({ space: 3 }) {
      Search({ value: 'Search textAlign sample', controller: this.controller })
        .width('95%')
        .height(40)
        .stopBackPress(true)
        .textAlign(TextAlign.Center)
        .caretStyle({ width: 3, color: Color.Green })
        .selectedBackgroundColor(Color.Gray)
    }
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/nGUvi6jYRt26jrjShiz8IA/en-us_image_0000002568685397.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8C742EDBDBCA56B3A0734127BEC333201E1136E073A91C4ADC807F5BB1B805E4)

## Example 14: Configuring the Text Box to Receive Default Focus and Bring Up the Soft Keyboard

This example demonstrates how to configure the text box to receive default focus and bring up the soft keyboard using the [defaultFocus](../../universal-attributes/interaction-properties/focus-control/document.md#defaultfocus9) (available since API version 9) and [enableKeyboardOnFocus](#enablekeyboardonfocus10) (available since API version 10) attributes.

// xxx.ets

@Entry
@Component
struct SearchExample {
  controller: SearchController = new SearchController();
  @State value: string = 'false';

  build() {
    Column({ space: 3 }) {
      Text('editing: ' + this.value)
      Search({ placeholder: 'please enter...', controller: this.controller })
        .width('95%')
        .height(40)
        .defaultFocus(true)
        .enableKeyboardOnFocus(true)
        .enablePreviewText(true)
        .enableHapticFeedback(true)
        .onEditChange((data: boolean) => {
          this.value = data ? 'true' : 'false';
        })
    }
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/wSc9c3VzRHKSlcWUXcEHQQ/en-us_image_0000002568765407.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D8E74C78BE5EBDED8E85803CDC1283CD3B2ABA58EE2699A9DD768585574C2154)

## Example 15: Disabling the System Text Selection Menu

This example demonstrates how to disable the system text selection menu by using the [selectionMenuHidden](#selectionmenuhidden10) attribute, available since API version 10.

// xxx.ets

@Entry
@Component
struct SearchExample {
  controller: SearchController = new SearchController();

  build() {
    Column({ space: 3 }) {
      Search({ value: '123456', controller: this.controller })
        .width('95%')
        .height(40)
        .type(SearchType.NUMBER)
        .selectionMenuHidden(true)
    }
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/OO_K1tcYQpOFOkK67Hhqvw/en-us_image_0000002537765682.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=26F2CFB1D9D1EEDD0E4B9785F5992140B74BDA55E58AD26FDBF5E1A40FD983AC)

## Example 16: Setting Input Filtering

This example demonstrates how to set input filtering using the [inputFilter](#inputfilter12) attribute, available since API version 12.

// xxx.ets

@Entry
@Component
struct SearchExample {
  controller: SearchController = new SearchController();
  @State filterValue: string = '';

  build() {
    Column({ space: 3 }) {
      Text('Filter:' + this.filterValue)
      Search({ placeholder: 'please enter...', controller: this.controller })
        .width('95%')
        .height(40)
        .textIndent(5)
        .halfLeading(true)
        .inputFilter('\[a-z\]', (filterValue: string) => {
          this.filterValue = filterValue;
        })
    }
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/Y452xG5-R66S3pLa-J3qmg/en-us_image_0000002537925622.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5D0449B78A3D327A3857488636A7467806E8EDA75119F86F56527AB8142E028E)

## Example 17: Setting Text Selection for a Specified Region

This example demonstrates how to set text selection for a specified region and the display/hide strategy of the menu using the [setTextSelection](#settextselection12) API, available since API version 12.

// xxx.ets

@Entry
@Component
struct SearchExample {
  controller: SearchController = new SearchController();
  @State startIndex: number = 0;
  @State endIndex: number = 0;

  build() {
    Column({ space: 3 }) {
      Text('Selection start:' + this.startIndex + ' end:' + this.endIndex)
      Search({ value: 'Hello World', controller: this.controller })
        .width('95%')
        .height(40)
        .minFontScale(1)
        .maxFontScale(1.5)
        .defaultFocus(true)
        .onTextSelectionChange((selectionStart: number, selectionEnd: number) => {
          this.startIndex = selectionStart;
          this.endIndex = selectionEnd;
        })

      Button('Selection \[0,3\]')
        .onClick(() => {
          this.controller.setTextSelection(0, 3, { menuPolicy: MenuPolicy.SHOW });
        })
    }
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/H78MPy_dQT2_-7rO7B1W8w/en-us_image_0000002568685399.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1F5FC205184D424F5EDBD5C054647945AFE9A445DC8A59D6DB7ACC214C6F055B)

## Example 18: Handling Text Scrolling Events

This example demonstrates how to set the callback for text scrolling events using the [onContentScroll](#oncontentscroll10) event, available since API version 10.

// xxx.ets

@Entry
@Component
struct SearchExample {
  controller: SearchController = new SearchController();
  @State offsetX: number = 0;
  @State offsetY: number = 0;

  build() {
    Column({ space: 3 }) {
      Text('offset x:' + this.offsetX + ' y:' + this.offsetY)
      Search({ value: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', controller: this.controller })
        .width(200)
        .height(40)
        .onContentScroll((totalOffsetX: number, totalOffsetY: number) => {
          this.offsetX = totalOffsetX;
          this.offsetY = totalOffsetY;
        })
    }
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/YVO9MHxYSsatJP9IO0zvRg/en-us_image_0000002568765409.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3AA32918C2608BE963D01FF906CF8F2F01FBBC13771FE973BEE3631FDFB1F6CD)

## Example 19: Setting the Minimum and Maximum Font Scale Factors

Since API version 18, [minFontScale](#minfontscale18) and [maxFontScale](#maxfontscale18) are used to set the minimum and maximum font scale factors. When the system font size is adjusted, the text font size remains within the range defined by [minFontScale](#minfontscale18) and [maxFontScale](#maxfontscale18). The following example demonstrates how the **Search** component scales its font size according to system font size changes, within different font size limits.

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
struct SearchExample {
  @State minFontScale: number = 1.0;
  @State maxFontScale: number = 1.0;
  @State minFontScale2: number = 0.5;
  @State maxFontScale2: number = 2.0;

  build() {
    Column() {
      Column() {
        Text("System font scales up and down: aaaaaaaAAAAAA")
        Blank(30)
        Text("minFontScale = " + this.minFontScale)
        Text("maxFontScale = " + this.maxFontScale)
        Search({
          placeholder: 'The text area can hold an unlimited amount of text. input your word...',
        })
          .minFontScale(this.minFontScale) // Set the minimum font scale factor. If the parameter is set to undefined, the default scale factor is used.
          .maxFontScale(this.maxFontScale) // Set the maximum font scale factor. If the parameter is set to undefined, the default scale factor is used.

        Blank(30)

        Text("minFontScale = " + this.minFontScale2)
        Text("maxFontScale = " + this.maxFontScale2)
        Search({
          placeholder: 'The text area can hold an unlimited amount of text. input your word...',
        })
          .minFontScale(this.minFontScale2) // Set the minimum font scale factor. If the parameter is set to undefined, the default scale factor is used.
          .maxFontScale(this.maxFontScale2) // Set the maximum font scale factor. If the parameter is set to undefined, the default scale factor is used.
      }.width('100%')
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/7LpXPXP5TvGnRpe7nc5-rQ/en-us_image_0000002537765684.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3941C8F15B5676B3E49F9110DC467003A10BD3C7AB4A61E69DBA8855FD1E8F2B) ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/UtZtm83cSqmNi9Xf59HyRA/en-us_image_0000002537925624.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=30588DA44C34B52188DC0DE137AFED14689F728DC714FA5FE563487374667B77)

## Example 20: Setting Text Stroke

This example demonstrates how to set the stroke width and color for text using the [strokeWidth](#strokewidth20) and [strokeColor](#strokecolor20) attributes, available since API version 20.

// xxx.ets
import { LengthMetrics } from '@kit.ArkUI';

@Entry
@Component
struct SearchExample {
  build() {
    Row() {
      Column() {
        Text('stroke feature').fontSize(9).fontColor(0xCCCCCC)

        Search({ value: 'Text without stroke' })
          .width('100%')
          .height(60)
          .borderWidth(1)
          .minFontSize(40)
          .maxFontSize(40)
        Search({ value: 'Text with stroke' })
          .width('100%')
          .height(60)
          .borderWidth(1)
          .minFontSize(40)
          .maxFontSize(40)
          .strokeWidth(LengthMetrics.px(-3.0))
          .strokeColor(Color.Red)
        Search({ value: 'Text with stroke' })
          .width('100%')
          .height(60)
          .borderWidth(1)
          .minFontSize(40)
          .maxFontSize(40)
          .strokeWidth(LengthMetrics.px(3.0))
          .strokeColor(Color.Red)
      }.height('90%')
    }
    .width('90%')
    .margin(10)
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/o2NtyEs2RHezQpup7wdJyg/en-us_image_0000002568685401.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AE24C5DCBA8D904D16D7C0941BF3BB266B756F17D353A1DC0A3188507A1E836D)

## Example 21: Configuring Automatic Spacing Between Chinese and Western Text

This example demonstrates how to configure automatic spacing between Chinese and Western characters using the [enableAutoSpacing](#enableautospacing20) attribute, available since API version 20.

// xxx.ets
@Entry
@Component
struct SearchExample {
  build() {
    Row() {
      Column() {
        Text('Automatic spacing: Enabled').margin(5)
        Search({value: '中文 Text'})
          .enableAutoSpacing(true)
        Text('Automatic spacing: Disabled').margin(5)
        Search({value: '中文Text'})
          .enableAutoSpacing(false)
      }.height('100%')
    }
    .width('60%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/1jK0hG8hSTa3MMZafD7VNQ/en-us_image_0000002568765411.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3EFE1D19D8204DEC30992576B8DC04DB4AB17E680F83C8CD36D9C4C40F06A701)

## Example 22: Setting the Placeholder Rich Text Style

This example illustrates how to set the placeholder rich text style using the [setStyledPlaceholder](../text-box-component-common-apis/document.md#setstyledplaceholder22) API, available since API version 22.

// xxx.ets
import { LengthMetrics } from '@kit.ArkUI';

@Entry
@Component
struct SearchExample {
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
  controller: SearchController = new SearchController();

  aboutToAppear() {
    this.controller.setStyledPlaceholder(this.styledString)
  }

  build() {
    Scroll() {
      Column() {
        Text("Search Placeholder Rich Text"")
          .fontSize(8)
        Search({
          controller: this.controller
        })
          .textFont({ size: 24 })
          .margin(10)
      }
      .width('100%')
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/Q5NbDVpDRd-zXR9iyAiVYw/en-us_image_0000002537765686.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6DD8A15F34B1D554FD452DE241CAE9A04499C4F3942168606A925996130B0B91)

## Example 23: Setting Input Method Extension Information

This example illustrates how to set input method extension information using the **setExtraConfig** method of [IMEClient](../text-component-common-apis/document.md#imeclient20), available since API version 22.

// xxx.ets
@Entry
@Component
struct SearchExample {
  build() {
    Column() {
      Search({ value: 'Execute onWillAttachIME callback before launching the input method' })
        .onWillAttachIME((client: IMEClient) => {
          client.setExtraConfig({
            customSettings: {
              name: "Search", // Custom property
              id: client.nodeId // Custom Property
            }
          })
        })
    }.height('100%')
  }
}
