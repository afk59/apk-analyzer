# Chip

The **Chip** component is designed for scenarios including search history display and email recipient lists.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/08/v3/Hh0TSAJiRHqUZKpI1dX6eg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062249Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=62A993944A1B326767EE74E1C430F446199E17889EDF5C1FCB6C540A7779F875)

This component is supported since API version 11. Updates will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { Chip, ChipOptions, ChipSize } from '@kit.ArkUI';

#### Child Components

Not supported

#### Chip

Chip(options:ChipOptions): void

**Decorator**: @Builder

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [ChipOptions](#chipoptions) | Yes | Parameters of the chip. |

#### ChipOptions

Defines the type and style parameters of the chip.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| size | [ChipSize](#chipsize) | [SizeOptions](../../common-definitions/basic-types/document.md#sizeoptions) | No | Yes | 
Chip size.

Default value: **ChipSize.NORMAL**

The SizeOptions type parameter does not support percentage values. If an invalid value is provided, the system will use the default value instead.

**Atomic service API**: This API can be used in atomic services since API version 12.

Note: [Aging-friendly design implementation](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkui-support-for-aging-adaptation) does not take effect when size specifies specific width and height, except when size is set to { height: 0, width: 0 }.

 |
| enabled | boolean | No | Yes | 

Whether the chip can be selected.

Default value: **true**

**true**: The chip can be selected.

**false**: The chip cannot be selected.

If the value is **undefined**, the default value is used.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| activated12+ | boolean | No | Yes | 

Whether the chip is activated.

Default value: **false**

**true**: The chip is activated.

**false**: The chip is not activated.

If the value is **undefined**, the default value is used.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| prefixIcon | [PrefixIconOptions](#prefixiconoptions) | No | Yes | 

Prefix icon of the chip.

Default value: The prefix icon is not displayed.

If the value is **undefined**, the default value is used.

If both **prefixIcon** and **prefixSymbol** are set, the effect specified by **prefixSymbol** will be displayed, and **prefixIcon** will be ignored.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| prefixSymbol12+ | [ChipSymbolGlyphOptions](#chipsymbolglyphoptions12) | No | Yes | 

Symbol-type prefix icon of the chip.

Default value: The prefix icon is not displayed.

If the value is **undefined**, the default value is used.

If both **prefixIcon** and **prefixSymbol** are set, the effect specified by **prefixSymbol** will be displayed, and **prefixIcon** will be ignored.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| label | [LabelOptions](#labeloptions) | No | No | 

Text of the chip.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| suffixIcon | [SuffixIconOptions](#suffixiconoptions) | No | Yes | 

Suffix icon of the chip.

Default value: The suffix icon is not displayed.

If the value is **undefined**, the default value is used.

If both **suffixIcon** and **suffixSymbol** are set, the effect specified by **suffixSymbol** will be displayed, and **suffixIcon** will be ignored.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| suffixSymbol12+ | [ChipSymbolGlyphOptions](#chipsymbolglyphoptions12) | No | Yes | 

Symbol-type suffix icon of the chip.

Default value: The suffix icon is not displayed.

If the value is **undefined**, the default value is used.

If both **suffixIcon** and **suffixSymbol** are set, the effect specified by **suffixSymbol** will be displayed, and **suffixIcon** will be ignored.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| suffixSymbolOptions14+ | [ChipSuffixSymbolGlyphOptions](#chipsuffixsymbolglyphoptions14) | No | Yes | 

Accessibility settings of the symbol-type suffix icon.

Default value: The suffix icon is not displayed.

If the value is **undefined**, the default value is used.

**Atomic service API**: This API can be used in atomic services since API version 14.

 |
| backgroundColor | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | No | Yes | 

Chip background color.

Default value: **$r('sys.color.ohos\_id\_color\_button\_normal')**

If the value is **undefined**, the default value is used.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| activatedBackgroundColor12+ | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | No | Yes | 

Background color of the chip when it is activated.

Default value: **$r('sys.color.ohos\_id\_color\_emphasize')**

If the value is **undefined**, the default value is used.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| borderRadius | [Dimension](../../common-definitions/basic-types/document.md#dimension10) | No | Yes | 

Radius of the rounded corner of the chip background. Percentage is not supported.

Default value: **$r('sys.float.ohos\_id\_corner\_radius\_button')**

If the value is **undefined**, the default value is used.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| allowClose | boolean | No | Yes | 

Whether to display the close icon.

Default value: **true**

The value **true** means to show the delete icon, and **false** means the opposite.

If the value is **undefined**, the default value is used.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| onClose | ()=>void | No | Yes | 

Event triggered when the close icon is clicked.

If the value is **undefined**, clicking the close icon will not trigger any event.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| onClicked12+ | Callback<void> | No | Yes | 

Chip click event.

If the value is **undefined**, the chip cannot be clicked.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| direction12+ | [Direction](../../common-definitions/enums/document.md#direction) | No | Yes | 

Layout direction.

Default value: **Direction.Auto**

If the value is **undefined**, the default value is used.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| closeOptions14+ | [CloseOptions](#closeoptions14) | No | Yes | 

Accessibility settings of the default close icon.

If the value is **undefined**, the default value is used.

**Atomic service API**: This API can be used in atomic services since API version 14.

 |
| accessibilityDescription14+ | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 

Accessible description of the chip. You can provide comprehensive text explanations to help users understand the operation they are about to perform and its potential consequences, especially when these cannot be inferred from the component's attributes and accessibility text alone. If a component contains both text information and the accessible description, the text is announced first and then the accessible description, when the component is selected.

The default value is an empty string.

If the value is **undefined**, the default value is used.

**Atomic service API**: This API can be used in atomic services since API version 14.

 |
| accessibilityLevel14+ | string | No | Yes | 

Accessibility level of the chip. It determines whether the component can be recognized by accessibility services.

The options are as follows:

**"auto"**: It is treated as "yes" by the system.

**"yes"**: The component can be recognized by accessibility services.

**"no"**: The component cannot be recognized by accessibility services.

**"no-hide-descendants"**: Neither the component nor its child components can be recognized by accessibility services.

Default value: **"auto"**

If the value is **undefined**, the default value is used.

**Atomic service API**: This API can be used in atomic services since API version 14.

 |
| accessibilitySelectedType14+ | [AccessibilitySelectedType](#accessibilityselectedtype14) | No | Yes | 

Type of selected state for the chip.

Default value:

If the **activated** property is set but **accessibilitySelectedType** is not specified, the default type is **CHECKED**. If the **activated** property is not set, the default type is **CLICKED**.

If the value is **undefined**, the default value is used.

**Atomic service API**: This API can be used in atomic services since API version 14.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/GLHpB5vXRES5hKbI4euUig/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062249Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0FF71234C4C183CD844EF4F2AD40C963C920C1E18A28E5B6A5DF97B5D8F2ABDD)

1.  When **suffixSymbol** is provided with an argument, **suffixIcon** and **allowClose** will not take effect. If **suffixSymbol** is not provided, but **suffixIcon** is, **allowClose** still will not take effect. When neither **suffixSymbol** nor **suffixIcon** is provided with arguments, **allowClose** determines whether the deletion icon is displayed.
    
2.  If **undefined** is assigned to **backgroundColor** or **activatedBackgroundColor**, the default background color is used. If an invalid value is specified, the background color is transparent.
    
3.  Default font colors for **prefixSymbol** and **suffixSymbol**: **normalFontColor**: **\[$r('sys.color.ohos\_id\_color\_primary')\]**; **activatedFontColor**: **\[$r('sys.color.ohos\_id\_color\_text\_primary\_contrary')\]**. The default value of **fontColor** is **16**.
    
4.  The default value of **fillColor** is **$r('sys.color.ohos\_id\_color\_secondary')** for **prefixIcon** and **$r('sys.color.ohos\_id\_color\_primary')** for **suffixIcon**. The color parsing of **fillColor** is the same as that of the **Image** component.
    
5.  The default value of **activatedFillColor** in **prefixIcon** and **suffixIcon** is **$r('sys.color.ohos\_id\_color\_text\_primary\_contrary')**. The color parsing of **activatedFillColor** is the same as that of the **Image** component.
    

#### ChipSize

Enumerates the chip size types.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Value | Description |
| :-- | :-- | :-- |
| NORMAL | "NORMAL" | Normal size. |
| SMALL | "SMALL" | Small size. |

#### AccessibilitySelectedType14+

Enumerates the selected state types of the chip. It allows you to specify how accessibility services convey the component's selected state to users. Different selected state types provide distinct semantics and user experiences.

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Value | Description |
| :-- | :-- | :-- |
| CLICKED | 0 | Click type. The chip acts as a regular clickable component, without reporting any selected state to accessibility services. Use this type when the chip triggers an action but does not maintain a selected state. |
| CHECKED | 1 | Checkbox type. The chip reports its selected state to accessibility services using the [accessibilityChecked](../../universal-attributes/accessibility/document.md#accessibilitychecked13) attribute. Use this type for multi-select scenarios, such as tag filtering and attribute selection. |
| SELECTED | 2 | Radio type. The chip reports its selected state to accessibility services using the [accessibilitySelected](../../universal-attributes/accessibility/document.md#accessibilityselected13) attribute. Use this type for single-select scenarios, such as navigation bar tabs and radio buttons. |

#### IconCommonOptions

Defines the common icon options of the chip.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| src | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | No | Icon source, which can be a specific image path or an image reference. |
| size | [SizeOptions](../../common-definitions/basic-types/document.md#sizeoptions) | No | Yes | 
Icon size. This parameter cannot be set in percentage.

Default value:

\- When **ChipSize.SMALL** is used: **{width: $r('sys.float.chip\_small\_icon\_size'), height: $r('sys.float.chip\_small\_icon\_size')}**.

\- When **ChipSize.NORMAL** is used: **{width: $r('sys.float.chip\_normal\_icon\_size'), height: $r('sys.float.chip\_normal\_icon\_size')}**.

Unit: vp.

If the value is **undefined**, the default value is used.

 |
| fillColor | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | No | Yes | 

Icon fill color.

Default value: **$r('sys.color.chip\_usually\_icon\_color')**

If the value is **undefined**, the default value is used.

 |
| activatedFillColor12+ | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | No | Yes | 

Icon fill color when the chip is activated.

Default value: **$r('sys.color.chip\_active\_icon\_color')**

If the value is **undefined**, the default value is used.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/4IOfLMQ4RPyiUgTuBCZ6jA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062249Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3D0EB427A9B4D320CDAC835D063B1420EC05342D7F739395BBE3133F8179F42F)

**fillColor** and **activatedFillColor** take effect only when the icon format is SVG.

#### PrefixIconOptions

Defines the prefix icon options.

Inherits from [IconCommonOptions](#iconcommonoptions).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

#### SuffixIconOptions

Defines the suffix icon options.

Inherits from [IconCommonOptions](#iconcommonoptions).

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| action | () => void | No | Yes | 
Action of the suffix icon.

If the value is **undefined**, no action is configured for the suffix icon.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| accessibilityText14+ | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 

Accessibility text, that is, accessibility label name, of the suffix icon. If a component does not contain text information, it will not be announced by the screen reader when selected. In this case, the screen reader user cannot know which component is selected. To solve this problem, you can set accessibility text for components without text information. When such a component is selected, the screen reader announces the specified accessibility text, informing the user which component is selected.

Default value: **' '**

If the value is **undefined**, the default value is used.

**Atomic service API**: This API can be used in atomic services since API version 14.

 |
| accessibilityDescription14+ | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 

Accessible description of the suffix icon. You can provide comprehensive text explanations to help users understand the operation they are about to perform and its potential consequences, especially when these cannot be inferred from the component's attributes and accessibility text alone. If a component contains both text information and the accessible description, the text is announced first and then the accessible description, when the component is selected.

Default value: **' '**

If the value is **undefined**, the default value is used.

**Atomic service API**: This API can be used in atomic services since API version 14.

 |
| accessibilityLevel14+ | string | No | Yes | 

Accessibility level of the suffix icon. It determines whether the component can be recognized by accessibility services.

The options are as follows:

**"auto"**: It is treated as "yes" when **action** is set for the component and as "no" otherwise.

**"yes"**: The component can be recognized by accessibility services.

**"no"**: The component cannot be recognized by accessibility services.

**"no-hide-descendants"**: Neither the component nor its child components can be recognized by accessibility services.

Default value: **"auto"**

If the value is **undefined**, the default value is used.

**Atomic service API**: This API can be used in atomic services since API version 14.

 |

#### AccessibilityOptions14+

Defines the accessibility options of the suffix icon.

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| accessibilityText | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 
Accessibility text, that is, accessible label name. If a component does not contain text information, it will not be announced by the screen reader when selected. In this case, the screen reader user cannot know which component is selected. To solve this problem, you can set accessibility text for components without text information. When such a component is selected, the screen reader announces the specified accessibility text, informing the user which component is selected.

Default value: **' '**

If the value is **undefined**, the default value is used.

 |
| accessibilityDescription | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 

Accessibility description. You can provide comprehensive text explanations to help users understand the operation they are about to perform and its consequences, especially when these cannot be inferred from the component's attributes and accessibility text alone. If a component contains both text information and the accessible description, the text is announced first and then the accessible description, when the component is selected.

Default value: **' '**

If the value is **undefined**, the default value is used.

 |
| accessibilityLevel | string | No | Yes | 

Accessibility level. It determines whether the component can be recognized by accessibility services.

The options are as follows:

**"auto"**: It is treated as "yes" by the system.

**"yes"**: The component can be recognized by accessibility services.

**"no"**: The component cannot be recognized by accessibility services.

**"no-hide-descendants"**: Neither the component nor its child components can be recognized by accessibility services.

Default value: **"auto"**

If the value is **undefined**, the default value is used.

 |

#### ChipSuffixSymbolGlyphOptions14+

Defines the accessibility options of the symbol-type suffix icon.

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| action | [VoidCallback](../../common-definitions/basic-types/document.md#voidcallback12) | No | Yes | 
Action of the suffix icon.

Default value: **undefined**

 |
| normalAccessibility | [AccessibilityOptions](#accessibilityoptions14) | No | Yes | 

Accessibility settings for the normal state.

Default value: **undefined**

 |
| activatedAccessibility | [AccessibilityOptions](#accessibilityoptions14) | No | Yes | 

Accessibility settings for the activated state.

Default value: **undefined**

 |

#### ChipSymbolGlyphOptions12+

Defines the prefix and suffix icon options.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| normal | [SymbolGlyphModifier](../../universal-attributes/modifiers-and-custom-property/symbol-glyph-modifier/document.md#symbolglyphmodifier) | No | Yes | 
Sets the icon in the inactive state.

Default value: The prefix or suffix icon is not displayed.

If the value is **undefined**, the default value is used.

 |
| activated | [SymbolGlyphModifier](../../universal-attributes/modifiers-and-custom-property/symbol-glyph-modifier/document.md#symbolglyphmodifier) | No | Yes | 

Icon settings for the activated state.

Default value: The prefix or suffix icon is not displayed.

If the value is **undefined**, the default value is used.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/01/v3/mmLLbnm4RI6lJ0A9PhkT5w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062249Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D416389C34F440907058479F373AF01650C7D9CED1B5A698317323EF320523C8)

The animation type cannot be modified via [SymbolEffect](../../text-and-input/symbolglyph/document.md#symboleffect12) and animations cannot be set via **effectStrategy**.

#### LabelOptions

Defines text configuration options.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| text | string | No | No | Text content. |
| fontSize | [Dimension](../../common-definitions/basic-types/document.md#dimension10) | No | Yes | 
Font size. This parameter cannot be set in percentage.

Default value: **$r('sys.float.ohos\_id\_text\_size\_button2')**

If the value is **undefined**, the default value is used.

 |
| fontColor | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | No | Yes | 

Font color.

Default value: **$r('sys.color.ohos\_id\_color\_text\_primary')**

If the value is **undefined**, the default value is used.

 |
| activatedFontColor12+ | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | No | Yes | 

Font color when the chip is activated.

Default value: **$r('sys.color.ohos\_id\_color\_text\_primary\_contrary')**

If the value is **undefined**, the default value is used.

 |
| fontFamily | string | No | Yes | 

Font family.

Default value: **"HarmonyOS Sans"**

If the value is **undefined**, the default value is used.

 |
| labelMargin | [LabelMarginOptions](#labelmarginoptions) | No | Yes | 

Spacing between the text and the left and right icons.

Default value:

When **size** is **ChipSize.SMALL**: **{ left: 4, right: 4 }**.

When **size** is **ChipSize.NORMAL**: **{ left: 6, right: 6 }**.

Unit: vp.

If the value is **undefined**, the default value is used.

 |
| localizedLabelMargin12+ | [LocalizedLabelMarginOptions](#localizedlabelmarginoptions12) | No | Yes | 

Spacing between the localized text and the left and right icons.

Default value:

When **size** is set to **ChipSize.SMALL**, the default value is as follows:

{ start: LengthMetrics.resource($r('sys.float.chip\_small\_text\_margin')), end: LengthMetrics.resource($r('sys.float.chip\_small\_text\_margin')) }

When **size** is set to **ChipSize.NORMAL**, the default value is as follows:

{ start: LengthMetrics.resource($r('sys.float.chip\_normal\_text\_margin')), end: LengthMetrics.resource($r('sys.float.chip\_normal\_text\_margin')) }

If the value is **undefined**, the default value is used.

 |

#### CloseOptions14+

Closes the accessibility attributes for the chip by default. The default value of **accessibilityText** is **"Delete"**.

Inherits from [AccessibilityOptions](#accessibilityoptions14).

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

#### LabelMarginOptions

Defines the spacing between the text and the left and right icons.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| left | [Dimension](../../common-definitions/basic-types/document.md#dimension10) | No | Yes | 
Spacing between the text and the left icon. This parameter cannot be set in percentage.

Default value:

When **size** is set to **ChipSize.SMALL**, the default value of **left** is **4**.

When **size** is set to **ChipSize.NORMAL**, the default value of **left** is **6**.

Unit: vp.

If the value is out of the range, the default value is used.

Value range: \[0, +∞)

 |
| right | [Dimension](../../common-definitions/basic-types/document.md#dimension10) | No | Yes | 

Spacing between the text and the right icon. This parameter cannot be set in percentage.

Default value:

When **size** is set to **ChipSize.SMALL**, the default value of **right** is **4**.

When **size** is set to **ChipSize.NORMAL**, the default value of **right** is **6**.

Unit: vp.

If the value is out of the range, the default value is used.

Value range: \[0, +∞)

 |

#### LocalizedLabelMarginOptions12+

Defines the spacing between the localized text and the left and right icons.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| start | [LengthMetrics](../../../arkts-api/ui/arkui/graphics/document.md#lengthmetrics12) | No | Yes | 
Spacing between the text and the left icon. This parameter cannot be set in percentage.

Default value:

When **size** is set to **ChipSize.SMALL**, the default value of **start** is as follows:

LengthMetrics.resource($r('sys.float.chip\_small\_text\_margin'))

When **size** is set to **ChipSize.NORMAL**, the default value of **start** is as follows:

LengthMetrics.resource($r('sys.float.chip\_normal\_text\_margin'))

If the value is **undefined**, the default value is used.

 |
| end | [LengthMetrics](../../../arkts-api/ui/arkui/graphics/document.md#lengthmetrics12) | No | Yes | 

Spacing between the text and the right icon. This parameter cannot be set in percentage.

Default value:

When **size** is set to **ChipSize.SMALL**, the default value of **end** is as follows:

LengthMetrics.resource($r('sys.float.chip\_small\_text\_margin'))

When **size** is set to **ChipSize.NORMAL**, the default value of **end** is as follows:

LengthMetrics.resource($r('sys.float.chip\_normal\_text\_margin'))

If the value is **undefined**, the default value is used.

 |

#### Example

## Example 1: Setting a Custom Suffix Icon

This example sets a custom suffix icon by configuring **suffixIcon**.

import { Chip, ChipSize } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  build() {
    Column({ space: 10 }) {
      Chip({
        prefixIcon: {
          // Replace 'app.media.chips' with your actual icon resource.
          src: $r('app.media.chips'),
          size: { width: 16, height: 16 },
          fillColor: Color.Red
        },
        label: {
          text: 'Chip',
          fontSize: 12,
          fontColor: Color.Blue,
          fontFamily: 'HarmonyOS Sans',
          labelMargin: { left: 20, right: 30 }
        },
        suffixIcon: {
          // Replace 'app.media.close' with your actual icon resource.
          src: $r('app.media.close'),
          size: { width: 16, height: 16 },
          fillColor: Color.Red
        },
        size: ChipSize.NORMAL,
        allowClose: false,
        enabled: true,
        backgroundColor: $r('sys.color.ohos\_id\_color\_button\_normal'),
        borderRadius: $r('sys.float.ohos\_id\_corner\_radius\_button')
      })
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/Z57iKFyyRmeI4yEmVav6SA/en-us_image_0000002537765958.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062249Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=46263C2C47CADE8774D1D329DA1C38B45DE995F1145BCCF7CFE54E3A2582411F)

## Example 2: Using the Default Suffix Icon

This example demonstrates how to display the default suffix delete icon by setting **allowClose** to **true**.

import { Chip, ChipSize } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  build() {
    Column({ space: 10 }) {
      Chip({
        prefixIcon: {
          // Replace 'app.media.chips' with your actual icon resource.
          src: $r('app.media.chips'),
          size: { width: 16, height: 16 },
          fillColor: Color.Blue
        },
        label: {
          text: 'Chip',
          fontSize: 12,
          fontColor: Color.Blue,
          fontFamily: 'HarmonyOS Sans',
          labelMargin: { left: 20, right: 30 }
        },
        size: ChipSize.NORMAL,
        allowClose: true,
        enabled: true,
        backgroundColor: $r('sys.color.ohos\_id\_color\_button\_normal'),
        borderRadius: $r('sys.float.ohos\_id\_corner\_radius\_button')
      })
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/MIbJKj0lQyaa1WVtdLyusA/en-us_image_0000002537925898.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062249Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=18638F45865FA9A13BE834BCE44571BB5D3B39E285EE8AFD3F1E594A571A5B6C)

## Example 3: Displaying No Suffix Icon

This example demonstrates how to hide the default suffix delete icon by setting **allowClose** to **false**.

import { Chip, ChipSize } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  build() {
    Column({ space: 10 }) {
      Chip({
        prefixIcon: {
          // Replace 'app.media.chips' with your actual icon resource.
          src: $r('app.media.chips'),
          size: { width: 16, height: 16 },
          fillColor: Color.Blue
        },
        label: {
          text: 'Chip',
          fontSize: 12,
          fontColor: Color.Blue,
          fontFamily: 'HarmonyOS Sans',
          labelMargin: { left: 20, right: 30 }
        },
        size: ChipSize.SMALL,
        allowClose: false,
        enabled: true,
        backgroundColor: $r('sys.color.ohos\_id\_color\_button\_normal'),
        borderRadius: $r('sys.float.ohos\_id\_corner\_radius\_button'),
        onClose: () => {
          console.info('chip on close');
        }
      })
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/Mn0IQ8oES5a_CqnZbMAoSg/en-us_image_0000002568685675.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062249Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=98124E24C312FF658E090E11DB39EB7864007C0E1B504510918B76C68FF23842)

## Example 4: Implementing the Activated State

This example shows how to implement the activated state for a chip by configuring **activated**.

import { Chip, ChipSize } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State isActivated: boolean = false;

  build() {
    Column({ space: 10 }) {
      Chip({
        prefixIcon: {
          // Replace 'app.media.chips' with your actual icon resource.
          src: $r('app.media.chips'),
          size: { width: 16, height: 16 },
          fillColor: Color.Blue,
          activatedFillColor: $r('sys.color.ohos\_id\_color\_text\_primary\_contrary')
        },
        label: {
          text: 'Chip',
          fontSize: 12,
          fontColor: Color.Blue,
          activatedFontColor: $r('sys.color.ohos\_id\_color\_text\_primary\_contrary'),
          fontFamily: 'HarmonyOS Sans',
          labelMargin: { left: 20, right: 30 }
        },
        size: ChipSize.NORMAL,
        allowClose: true,
        enabled: true,
        activated: this.isActivated,
        backgroundColor: $r('sys.color.ohos\_id\_color\_button\_normal'),
        activatedBackgroundColor: $r('sys.color.ohos\_id\_color\_emphasize'),
        borderRadius: $r('sys.float.ohos\_id\_corner\_radius\_button'),
        onClose: () => {
          console.info('chip on close');
        },
        onClicked: () => {
          console.info('chip on clicked');
        }
      })

      Button('Activate/Deactivate')
        .onClick(() => {
          this.isActivated = !this.isActivated;
        })
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/FpcFiKGlT7GDWYWOZh198w/en-us_image_0000002568765685.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062249Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8798A79B14DC75810F88E731B14FBD80026F627703363F239C24F3A0286DE771)

## Example 5: Setting the Symbol Icon

This example implements symbol-type prefix and suffix icons for the **Chip** component.

import { Chip, ChipSize, SymbolGlyphModifier } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State isActivated: boolean = false;

  build() {
    Column({ space: 10 }) {
      Chip({
        prefixSymbol: {
          normal: new SymbolGlyphModifier($r('sys.symbol.ohos\_star')).fontSize(16).fontColor(\[Color.Green\]),
          activated: new SymbolGlyphModifier($r('sys.symbol.ohos\_star')).fontSize(16).fontColor(\[Color.Red\]),
        },
        label: {
          text: 'Chip',
          fontSize: 12,
          fontColor: Color.Blue,
          activatedFontColor: $r('sys.color.ohos\_id\_color\_text\_primary\_contrary'),
          fontFamily: 'HarmonyOS Sans',
          labelMargin: { left: 20, right: 30 },
        },
        size: ChipSize.NORMAL,
        allowClose: true,
        enabled: true,
        activated: this.isActivated,
        backgroundColor: $r('sys.color.ohos\_id\_color\_button\_normal'),
        activatedBackgroundColor: $r('sys.color.ohos\_id\_color\_emphasize'),
        borderRadius: $r('sys.float.ohos\_id\_corner\_radius\_button'),
        onClose: () => {
          console.info('chip on close');
        },
        onClicked: () => {
          console.info('chip on clicked');
        }
      })

      Button('Activate/Deactivate')
        .onClick(() => {
          this.isActivated = !this.isActivated;
        })
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/GaAKAP0pQV65I7RF8p_bqg/en-us_image_0000002537765960.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062249Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B435C5C70FC18E4988E703FEDDEE5204041A632BC0E5A012D5DE6344064D6B90)

## Example 6: Implementing a Mirrored Layout

This example shows how to implement a chip mirrored layout by configuring **direction**.

import { Chip, ChipSize, LengthMetrics } from '@kit.ArkUI';

@Entry
@Component
struct ChipPage {
  build() {
    Column() {
      Chip({
        direction: Direction.Rtl,
        prefixIcon: {
          // Replace 'app.media.chips' with your actual icon resource.
          src: $r('app.media.chips'),
          size: { width: 16, height: 16 },
          fillColor: Color.Red,
        },
        label: {
          text: 'Chip',
          fontSize: 12,
          fontColor: Color.Blue,
          fontFamily: 'HarmonyOS Sans',
          localizedLabelMargin: { start: LengthMetrics.vp(20), end: LengthMetrics.vp(20) },
        },
        suffixIcon: {
          // Replace 'app.media.close' with your actual icon resource.
          src: $r('app.media.close'),
          size: { width: 16, height: 16 },
          fillColor: Color.Red,
        },
        size: ChipSize.NORMAL,
        allowClose: false,
        enabled: true,
        backgroundColor: $r('sys.color.ohos\_id\_color\_button\_normal'),
        borderRadius: $r('sys.float.ohos\_id\_corner\_radius\_button')
      })
    }
    .justifyContent(FlexAlign.Center)
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/QUyOaYtaTHutg1-WBA9nEQ/en-us_image_0000002537925900.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062249Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=46665C0EA433BBE9A5AF46A26641C9BB71C8D1788F18BC1AAA038AD2F633156B)

## Example 7: Implementing Accessibility for an Image-Type Suffix Icon

This example demonstrates how to implement the accessibility feature for a chip with an image-type suffix icon. Clicking the suffix icon triggers the announcement of "icon, button, usage hints."

import { Chip } from '@kit.ArkUI';

@Builder
function DefaultFunction(): void {
}

@Component
struct SectionGroup {
  @Prop
  @Require
  title: ResourceStr;
  @BuilderParam
  @Require
  content: () => void = DefaultFunction;

  build() {
    Column({ space: 4 }) {
      Text(this.title)
        .fontColor('#FF666666')
        .fontSize(12)
      Column({ space: 8 }) {
        this.content()
      }
    }
    .alignItems(HorizontalAlign.Start)
    .width('100%')
  }
}

@Component
struct SectionItem {
  @Prop
  @Require
  title: ResourceStr;
  @BuilderParam
  @Require
  content: () => void = DefaultFunction;

  build() {
    Column({ space: 12 }) {
      Text(this.title)
      this.content()
    }
    .backgroundColor('#FFFFFFFF')
    .borderRadius(12)
    .padding(12)
    .width('100%')
  }
}

@Entry
@Component
struct ChipExample2 {
  @State activated: boolean = false;

  build() {
    NavDestination() {
      Scroll() {
        SectionGroup({ title: 'Suffix icon announcement' }) {
          SectionItem({ title: 'Custom announcement' }) {
            Chip({
              label: { text: 'Chip' },
              suffixIcon: {
                src: $r('sys.media.ohos\_ic\_public\_cut'),
                accessibilityText: 'Icon', // Read "Icon, button, usage hints."
                accessibilityDescription: 'Usage hints',
                action: () => {
                  this.getUIContext().getPromptAction().showToast({
                    message: 'Suffix icon clicked.'
                  });
                }
              },
              onClicked: () => {
                this.getUIContext().getPromptAction().showToast({
                  message: 'Chip clicked.'
                });
              }
            })
          }
        }
      }
    }
  }
}

## Example 8: Implementing Accessibility for a Symbol-Type Suffix Icon

This example demonstrates how to implement the accessibility feature for a chip with a symbol-type suffix icon. Clicking the suffix icon triggers the announcement of "music, button, usage hints."

import { Chip, SymbolGlyphModifier } from '@kit.ArkUI';

@Builder
function DefaultFunction(): void {
}

@Component
struct SectionGroup {
  @Prop
  @Require
  title: ResourceStr;
  @BuilderParam
  @Require
  content: () => void = DefaultFunction;

  build() {
    Column({ space: 4 }) {
      Text(this.title)
        .fontColor('#FF666666')
        .fontSize(12)
      Column({ space: 8 }) {
        this.content()
      }
    }
    .alignItems(HorizontalAlign.Start)
    .width('100%')
  }
}

@Component
struct SectionItem {
  @Prop
  @Require
  title: ResourceStr;
  @BuilderParam
  @Require
  content: () => void = DefaultFunction;

  build() {
    Column({ space: 12 }) {
      Text(this.title)
      this.content()
    }
    .backgroundColor('#FFFFFFFF')
    .borderRadius(12)
    .padding(12)
    .width('100%')
  }
}

@Entry
@Component
struct ChipExample2 {
  @State activated: boolean = false;

  build() {
    NavDestination() {
      Scroll() {
        SectionGroup({ title: 'Suffix symbol announcement' }) {
          SectionItem({ title: 'activatedAccessibility' }) {
            Chip({
              label: { text: 'Chip' },
              activated: true,
              suffixSymbol: {
                activated: new SymbolGlyphModifier($r('sys.symbol.media\_sound'))
                  .fontSize(72),
              },
              suffixSymbolOptions: {
                activatedAccessibility: {
                  accessibilityText: 'Music', // Read "Music, button, usage hints."
                  accessibilityDescription: 'Usage hints'
                },
                action: () => {
                  this.getUIContext().getPromptAction().showToast({
                    message: 'Suffix symbol clicked.'
                  });
                }
              },
              onClicked: () => {
                this.getUIContext().getPromptAction().showToast({
                  message: 'Chip clicked.'
                });
              }
            })
          }

          SectionItem({ title: 'normalAccessibility' }) {
            Chip({
              label: { text: 'Chip' },
              suffixSymbol: {
                normal: new SymbolGlyphModifier($r('sys.symbol.media\_sound'))
                  .fontSize(72),
              },
              suffixSymbolOptions: {
                normalAccessibility: {
                  accessibilityText: 'Music', // Read "Music, button, usage hints."
                  accessibilityDescription: 'Usage hints'
                },
                action: () => {
                  this.getUIContext().getPromptAction().showToast({
                    message: 'Suffix symbol clicked.'
                  });
                }
              },
              onClicked: () => {
                this.getUIContext().getPromptAction().showToast({
                  message: 'Chip clicked.'
                });
              }
            })
          }
        }
      }
    }
    .padding({
      top: 8,
      bottom: 8,
      left: 16,
      right: 16,
    })
  }
}

## Example 9: Implementing Chip Accessibility

This example demonstrates how to set accessibility properties for the chip, including different selected state types.

import { AccessibilitySelectedType, Chip, ChipSize } from '@kit.ArkUI';

@Entry
@Component
struct ChipAccessibilityExample {
  @State clickedChipActivated: boolean = false;
  @State checkedChipActivated: boolean = false;
  @State selectedChipActivated: boolean = false;

  build() {
    Column({ space: 20 }) {
      Text('Chip accessibility example').fontSize(20).fontWeight(FontWeight.Bold)

      // Clickable chip - CLICKED type
      Chip({
        label: { text: 'Clickable chip' },
        prefixIcon: {
          src: $r('sys.media.ohos\_app\_icon'),
          fillColor: Color.Blue
        },
        size: ChipSize.NORMAL,
        accessibilitySelectedType: AccessibilitySelectedType.CLICKED, // Clickable type
        accessibilityDescription: 'This is a clickable chip.', // Overall accessibility description.
        accessibilityLevel: 'yes', // Make sure it can be recognized by accessibility services.
        closeOptions: {
          accessibilityDescription: 'Delete this chip. This operation cannot be undone.' // Provide detailed description for the delete button.
        },
        activated: this.clickedChipActivated,
        onClicked: () => {
          this.clickedChipActivated = !this.clickedChipActivated;
          this.getUIContext().getPromptAction().showToast({ message: 'Clickable chip is clicked.' });
        },
        onClose: () => {
          this.getUIContext().getPromptAction().showToast({ message: 'The close icon of the clickable chip is clicked.' });
        }
      })

      // Checkbox chip - CHECKED type
      Chip({
        label: { text: 'Checkbox chip' },
        prefixIcon: {
          src: $r('sys.media.ohos\_app\_icon'),
          fillColor: Color.Green
        },
        size: ChipSize.NORMAL,
        accessibilitySelectedType: AccessibilitySelectedType.CHECKED, // Checkbox chip
        accessibilityDescription: 'This is a checkbox chip.', // Overall accessibility description.
        activated: this.checkedChipActivated,
        onClicked: () => {
          this.checkedChipActivated = !this.checkedChipActivated;
          this.getUIContext().getPromptAction().showToast({
            message: this.checkedChipActivated ? 'Checkbox chip is selected.' : 'Checkbox chip is deselected.'
          });
        }
      })

      // Radio chip - SELECTED type
      Chip({
        label: { text: 'Radio chip' },
        prefixIcon: {
          src: $r('sys.media.ohos\_app\_icon'),
          fillColor: Color.Red
        },
        size: ChipSize.NORMAL,
        accessibilitySelectedType: AccessibilitySelectedType.SELECTED, // Radio type
        accessibilityDescription: 'This is a radio chip.', // Overall accessibility description.
        activated: this.selectedChipActivated,
        onClicked: () => {
          this.selectedChipActivated = !this.selectedChipActivated;
          this.getUIContext().getPromptAction().showToast({
            message: this.selectedChipActivated ? 'Radio chip is selected.' : 'Radio chip is deselected.'
          });
        }
      })

      // Example of setting the accessibility level
      Chip({
        label: { text: 'Accessibility level is set to no.' },
        size: ChipSize.NORMAL,
        accessibilityLevel: 'no', // This chip cannot be recognized by accessibility services.
        closeOptions: {
          accessibilityLevel: 'no'
        },
        backgroundColor: '#CCCCCC',
        onClicked: () => {
          this.getUIContext().getPromptAction().showToast({ message: 'This chip cannot be recognized by accessibility services.' });
        }
      })
    }
    .width('100%')
    .padding(16)
  }
}
