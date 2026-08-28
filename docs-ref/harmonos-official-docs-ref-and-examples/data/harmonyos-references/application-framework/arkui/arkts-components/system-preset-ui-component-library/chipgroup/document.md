# ChipGroup

The **ChipGroup** component provides a set of chips for organizing and categorizing files or resource content.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/eTaVvjm-Qu6-Wt6K8haPQg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062249Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=43C00CC8E78D91BEC3569E88BF508EA0F4A5FCB5E7E11E367B2ED925DEC206E1)

This component is supported since API version 12. Updates will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { ChipSize, ChipGroup } from '@kit.ArkUI';

#### Child Components

Not supported

#### ChipGroup

ChipGroup({
  items: ChipGroupItemOptions\[\],
  itemStyle?: ChipItemStyle,
  selectedIndexes?: Array<number>,
  multiple?: boolean,
  chipGroupSpace?: ChipGroupSpaceOptions,
  chipGroupPadding?: ChipGroupPaddingOptions,
  onChange?: Callback<Array<number>>,
  suffix?: Callback<void>
})

**Decorator**: @Component

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Type | Mandatory | Decorator | Description |
| :-- | :-- | :-- | :-- | :-- |
| items | [ChipGroupItemOptions\[\]](#chipgroupitemoptions) | Yes | @Require @Prop | 
Specific attributes of each chip. For details, see [ChipGroupItemOptions\[\]](#chipgroupitemoptions).

If the value is **undefined**, the **ChipGroup** component is empty by default.

 |
| itemStyle | [ChipItemStyle](#chipitemstyle) | No | @Prop | 

Style attributes of the chip, such as the color and size. For details, see [ChipItemStyle](#chipitemstyle).

Default value:

{ size: ChipSize.NORMAL, backgroundColor: $r('sys.color.ohos\_id\_color\_button\_normal'), fontColor: $r('sys.color.ohos\_id\_color\_text\_primary'), selectedFontColor: $r('sys.color.ohos\_id\_color\_text\_primary\_contrary'), selectedBackgroundColor: $r('sys.color.ohos\_id\_color\_emphasize') }

If the value is **undefined**, the default value is used.

 |
| selectedIndexes | Array<number> | No | @Prop | 

Index of the selected chip.

Default value: **\[0\]**.

If the value is **undefined**, the default value is used.

 |
| multiple | boolean | No | @Prop | 

Whether to select multiple chips.

**true**: Multiple chips can be selected. **false**: Only one chip can be selected.

Default value: **false**.

If the value is **undefined**, the default value is used.

 |
| chipGroupSpace | [ChipGroupSpaceOptions](#chipgroupspaceoptions) | No | @Prop | 

Left and right padding and spacing between chips. For details, see [ChipGroupSpaceOptions](#chipgroupspaceoptions).

Default value: { itemSpace: 8, startSpace: 16, endSpace: 16 }

Unit: vp

If the value is **undefined**, the default value is used.

 |
| chipGroupPadding | [ChipGroupPaddingOptions](#chipgrouppaddingoptions) | No | @Prop | 

Top and bottom padding, used to control the overall height. The type is [ChipGroupPaddingOptions](#chipgrouppaddingoptions).

Default value: { top: 14, bottom: 14 }

Unit: vp

If the value is **undefined**, the default value is used.

 |
| onChange | Callback<Array<number>> | No | \- | 

Callback invoked when the chip status changes.

If the value is **undefined**, the event is unbound.

 |
| suffix | Callback<void> | No | @BuilderParam | 

Callback used to customize a builder. To display custom content on the far right side of the component, configure the **suffix** property. Use of the **suffix** property requires referencing the [IconGroupSuffix](#icongroupsuffix) API.

By default, if this parameter is not passed, there is no suffix.

If the value is **undefined**, there is no suffix.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/yYvL_yajSXaj4wmtagp-XA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062249Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=968D74D214519D06716D7136610F982377DB16EF27B75FD58E02ECFCB4E50D9D)

1.  When **multiple** is set to **false**, if **selectedIndexes** is not passed in, the first chip is automatically selected by default. However, if the provided **selectedIndexes** includes multiple elements, the chip at the first index is selected by default.
    
2.  To use the suffix functionality, the **IconGroupSuffix** API must be imported. If this API is not provided, the suffix area will remain empty.
    
3.  The icon fill colors (**fillColor** and **activedFillColor**) must match the font color (**fontColor**). If different colors need to be set, use **prefixSymbol** when passing in [ChipGroupSpaceOptions](#chipgroupspaceoptions).
    

#### ChipGroupItemOptions

Defines the specific attributes of individual chips.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| prefixIcon | [IconOptions](#iconoptions) | No | Yes | 
Prefix image icon of the chip.

Default value: no prefix image icon.

If the value is **undefined**, the default value is used.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| prefixSymbol | [ChipSymbolGlyphOptions](../chip/document.md#chipsymbolglyphoptions12) | No | Yes | 

Prefix symbol glyph icon of the chip.

Default value: no prefix symbol glyph icon.

If the value is **undefined**, the default value is used.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| label | [LabelOptions](#labeloptions) | No | No | 

Text of the chip.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| suffixIcon(deprecated) | [IconOptions](#iconoptions) | No | Yes | 

Suffix image icon of the chip.

Default value: no suffix image icon.

If the value is **undefined**, the default value is used.

**Atomic service API**: This API can be used in atomic services since API version 12.

Note: This API is supported since API version 12 and deprecated since API version 14. You are advised to use **suffixImageIcon** instead.

 |
| suffixSymbol | [ChipSymbolGlyphOptions](../chip/document.md#chipsymbolglyphoptions12) | No | Yes | 

Suffix symbol glyph icon of the chip.

Default value: no suffix symbol glyph icon.

If the value is **undefined**, the default value is used.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| allowClose | boolean | No | Yes | 

Whether to show the delete icon.

**true** to show, **false** to hide.

Default value: **false**.

If the value is **undefined**, the default value is used.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| suffixImageIcon14+ | [SuffixImageIconOptions](#suffiximageiconoptions14) | No | Yes | 

Suffix image icon of the chip.

Default value: no suffix image icon.

If the value is **undefined**, the default value is used.

**Atomic service API**: This API can be used in atomic services since API version 14.

 |
| suffixSymbolOptions14+ | [ChipSuffixSymbolGlyphOptions](../chip/document.md#chipsuffixsymbolglyphoptions14) | No | Yes | 

Suffix symbol icon of the chip.

Default value: The suffix symbol icon has no function.

If the value is **undefined**, the default value is used.

**Atomic service API**: This API can be used in atomic services since API version 14.

 |
| closeOptions14+ | [CloseOptions](../chip/document.md#closeoptions14) | No | Yes | 

Accessibility options of the default close icon.

If the value is **undefined**, the default value is used.

**Atomic service API**: This API can be used in atomic services since API version 14.

 |
| accessibilityDescription14+ | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 

Accessible description of the chip. You can provide comprehensive text explanations of the chip in **ChipGroup** to help users understand the action they are about to perform and its potential consequences. This is particularly important when such outcomes cannot be directly inferred from the chip's own properties or its accessibility text. If a chip contains both text information and the accessible description, the text is announced first and then the accessible description, when the chip is selected.

The default value is an empty string.

If the value is **undefined**, the default value is used.

**Atomic service API**: This API can be used in atomic services since API version 14.

 |
| accessibilityLevel14+ | string | No | Yes | 

Accessibility level of the chip. It determines whether the chip can be recognized by accessibility services.

The options are as follows:

**"auto"**: It is treated as "yes" by the system.

**"yes"**: The chip can be recognized by accessibility services.

**"no"**: The chip cannot be recognized by accessibility services.

**"no-hide-descendants"**: Neither the chip nor its child components can be recognized by accessibility services.

Default value: **"auto"**

If the value is **undefined**, the default value is used.

**Atomic service API**: This API can be used in atomic services since API version 14.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/lqCbwZWrQ4ecYuHcNvzEMQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062249Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A2B948D3F16D4F14F31D635D739A20D2A32629BA9DB752FDFF6CEEFEA2DE1756)

If **suffixIcon** is specified, **allowClose** has no effect.

#### ChipItemStyle

Defines the common attributes shared by all chips.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| size | [ChipSize](../chip/document.md#chipsize) | [SizeOptions](../../common-definitions/basic-types/document.md#sizeoptions) | No | Yes | 
Chip size. The ChipSize type needs to be imported from the Chip component.

Default value: ChipSize.NORMAL or { height: 0, width: 0 }

If the value is **undefined**, the default value is used.

 |
| backgroundColor | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | No | Yes | 

Chip background color.

Default value: **$r('sys.color.ohos\_id\_color\_button\_normal').**

If this parameter is set to **undefined**, the default value is used.

 |
| fontColor | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | No | Yes | 

Chip text color.

Default value: **$r('sys.color.ohos\_id\_color\_text\_primary')**

If this parameter is set to **undefined**, the default value is used.

 |
| selectedFontColor | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | No | Yes | 

Text color of the chip when it is activated.

Default value: **$r('sys.color.ohos\_id\_color\_text\_primary\_contrary').**

If this parameter is set to **undefined**, the default value is used.

 |
| selectedBackgroundColor | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | No | Yes | 

Background color of the chip when it is activated.

Default value: **$r('sys.color.ohos\_id\_color\_emphasize')**

If this parameter is set to **undefined**, the default value is used.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/b2Hk_-8cTaGpb4rT5fthWA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062249Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A44F41F8B34B1A3403BD08FF2D2FA88949B0A3DF86CC1DDDFAE4DBA40DA40C5A)

1.  The size settings for chips can be of two types: (1) **ChipSize**, which conveniently offers two size options, **NORMAL** and **SMALL**; (2) **SizeOptions**.
    
2.  If **backgroundColor** or **selectedBackgroundColor** is set to **undefined**, the default background color is used. If an invalid value is provided, the background color is transparent.
    

#### ChipGroupSpaceOptions

Defines the left and right padding of the chip group, and the spacing between chips.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| itemSpace | string | number | No | Yes | 
Spacing between chips. Percentage values are not supported.

Value range:

Number type: a value greater than or equal to 0 (for example, **0**, **8**, **16**, or **24.5**)

String type: a string with units fp |vp |px |lpx and a numeric part greater than or equal to 0, for example, **"8vp"**, **"16fp"**, **"12px"**, or **"10lpx"**.

Not supported: negative values, percentage units, and invalid string formats.

Default value: **8**

Unit: vp

If the value is **undefined**, the default value is used.

 |
| startSpace | [Length](../../common-definitions/basic-types/document.md#length) | No | Yes | 

Left padding. Percentage values are not supported.

Default value: **16**

Unit: vp

If this parameter is set to **undefined**, the default value is used.

 |
| endSpace | [Length](../../common-definitions/basic-types/document.md#length) | No | Yes | 

Right padding. Percentage values are not supported.

Default value: **16**

Unit: vp

If the value is **undefined**, the default value is used.

 |

#### ChipGroupPaddingOptions

Defines the top and bottom padding of a **ChipGroup** component, which is used to control the overall height of the ChipGroup.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| top | [Length](../../common-definitions/basic-types/document.md#length) | No | No | 
Top padding. Percentage values are not supported.

Default value: **14**

Unit: vp

If the value is **undefined**, the default value is used.

 |
| bottom | [Length](../../common-definitions/basic-types/document.md#length) | No | No | 

Bottom padding. Percentage values are not supported.

Default value: **14**

Unit: vp

If this parameter is set to **undefined**, the default value is used.

 |

#### SuffixImageIconOptions14+

Defines the configuration options for suffix icons.

Inherits from [IconOptions](#iconoptions).

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| action | [VoidCallback](../../common-definitions/basic-types/document.md#voidcallback12) | No | Yes | 
Action of the suffix icon.

If the value is **undefined**, no suffix icon interaction event is triggered.

 |
| accessibilityText | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 

Accessibility text, that is, accessibility label name, of the suffix icon. If an icon does not contain text information, it will not be announced by the screen reader when selected. In this case, the screen reader user cannot know which icon is selected. To solve this problem, you can set accessibility text for icons without text information. When such an icon is selected, the screen reader announces the specified accessibility text, informing the user which icon is selected.

The default value is an empty string.

If the value is **undefined**, the default value is used.

 |
| accessibilityDescription | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 

Accessible description of the suffix icon. You can provide comprehensive text explanations to help users understand the operation they are about to perform and its potential consequences, especially when these cannot be inferred from the component's attributes and accessibility text alone. If an icon contains both text information and the accessible description, the text is announced first and then the accessible description, when the icon is selected.

The default value is an empty string.

If the value is **undefined**, the default value is used.

 |
| accessibilityLevel | string | No | Yes | 

Accessibility level of the suffix icon. It determines whether the icon can be recognized by accessibility services.

The options are as follows:

**"auto"**: It is treated as "yes" when **action** is set for the icon and as "no" otherwise.

**"yes"**: The icon can be recognized by accessibility services.

**"no"**: The icon cannot be recognized by accessibility services.

**"no-hide-descendants"**: Neither the icon nor its child components can be recognized by accessibility services.

Default value: **"auto"**

If the value is **undefined**, the default value is used.

 |

#### SymbolItemOptions14+

Suffix icon option type of ChipGroup.

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| symbol | [SymbolGlyphModifier](../../universal-attributes/modifiers-and-custom-property/symbol-glyph-modifier/document.md#symbolglyphmodifier) | No | No | Settings of the trailing symbol item. |
| action | [VoidCallback](../../common-definitions/basic-types/document.md#voidcallback12) | No | No | Action of the trailing symbol item. |
| accessibilityText | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 
Accessibility text of the trailing symbol item. If a trailing symbol item does not contain text information, it will not be announced by the screen reader when selected. In this case, the screen reader user cannot know which item is selected. To solve this problem, you can set accessibility text for trailing symbol items without text information. When such a trailing symbol item is selected, the screen reader announces the specified accessibility text, informing the user which item is selected.

The default value is an empty string.

If the value is **undefined**, the default value is used.

 |
| accessibilityDescription | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 

Accessible description of the trailing symbol item. You can provide comprehensive text explanations to help users understand the operation they are about to perform and its potential consequences, especially when these cannot be inferred from the component's attributes and accessibility text alone. If a trailing symbol item contains both text information and the accessible description, the text is announced first and then the accessible description, when the trailing symbol item is selected.

The default value is an empty string.

If the value is **undefined**, the default value is used.

 |
| accessibilityLevel | string | No | Yes | 

Accessibility level of the trailing symbol item. It determines whether the trailing symbol item can be recognized by accessibility services.

The options are as follows:

**"auto"**: It is treated as "yes" by the system.

**"yes"**: The trailing symbol item can be recognized by accessibility services.

**"no"**: The trailing symbol item cannot be recognized by accessibility services.

**"no-hide-descendants"**: Neither the trailing symbol item nor its child components can be recognized by accessibility services.

Default value: **"auto"**

If the value is **undefined**, the default value is used.

 |

#### IconGroupSuffix

**Decorator**: @Component

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Type | Mandatory | Decorator | Description |
| :-- | :-- | :-- | :-- | :-- |
| items | Array<[IconItemOptions](#iconitemoptions) | [SymbolGlyphModifier](../../universal-attributes/modifiers-and-custom-property/symbol-glyph-modifier/document.md#symbolglyphmodifier) | [SymbolItemOptions](#symbolitemoptions14)\> | Yes | @Require @Prop | Custom builder items. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/GOvriEXYQ0qB8zHMr8NMqQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062249Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9FF90BF8764C743798DB17D646F2AF261A96CEE9CC06F0104B8F6C90D410F7FB)

With **SymbolGlyphModifier**, neither modifying the animation type with **symbolEffect** nor setting the effect strategy with [effectStrategy](../../text-and-input/symbolglyph/document.md#effectstrategy) is supported.

#### IconItemOptions

Defines the configuration for the trailing builder, with constraints applied to background size and color settings.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| icon | [IconOptions](#iconoptions) | No | No | 
Custom builder icon.

When the chip size is **ChipSize.SMALL**, the suffix is at {width: 16, height: 16} by default.

When the chip size is **ChipSize.NORMAL**, the suffix is at {width: 24, height: 24} by default.

To dynamically change the size, you must use the [SymbolGlyphModifier](../../universal-attributes/modifiers-and-custom-property/symbol-glyph-modifier/document.md#symbolglyphmodifier) type when importing the [IconGroupSuffix](#icongroupsuffix) API.

If the value is **undefined**, the default value is used.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| action | Callback<void> | No | No | 

Callback of custom builder items.

If the value is **undefined**, the event is unbound.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| accessibilityText14+ | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 

Accessibility text of the trailing symbol item. If a trailing symbol item does not contain text information, it will not be announced by the screen reader when selected. In this case, the screen reader user cannot know which item is selected. To solve this problem, you can set accessibility text for trailing symbol items without text information. When such a trailing symbol item is selected, the screen reader announces the specified accessibility text, informing the user which item is selected.

The default value is an empty string.

If the value is **undefined**, the default value is used.

**Atomic service API**: This API can be used in atomic services since API version 14.

 |
| accessibilityDescription14+ | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 

Accessible description of the trailing symbol item. You can provide comprehensive text explanations to help users understand the operation they are about to perform and its potential consequences, especially when these cannot be inferred from the component's attributes and accessibility text alone. If a trailing symbol item contains both text information and the accessible description, the text is announced first and then the accessible description, when the trailing symbol item is selected.

The default value is an empty string.

If the value is **undefined**, the default value is used.

**Atomic service API**: This API can be used in atomic services since API version 14.

 |
| accessibilityLevel14+ | string | No | Yes | 

Accessibility level of the trailing symbol item. It determines whether the trailing symbol item can be recognized by accessibility services.

The options are as follows:

**"auto"**: It is treated as "yes" by the system.

**"yes"**: The trailing symbol item can be recognized by accessibility services.

**"no"**: The trailing symbol item cannot be recognized by accessibility services.

**"no-hide-descendants"**: Neither the trailing symbol item nor its child components can be recognized by accessibility services.

Default value: **"auto"**

If the value is **undefined**, the default value is used.

**Atomic service API**: This API can be used in atomic services since API version 14.

 |

#### IconOptions

Defines the common attributes of icons.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| src | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | No | Icon source, which can be a specific image resource or an image address reference. For details, see [Image](../../images-and-videos/image/document.md#image-1). |
| size | [SizeOptions](../../common-definitions/basic-types/document.md#sizeoptions) | No | Yes | 
Icon size. This parameter cannot be set in percentage.

Default value: **undefined**.

 |

#### LabelOptions

Defines the label configuration options.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| text | string | No | No | Text of the chip. |

#### Example

## Example 1: Implementing a Chip Group Without a Builder-defined Suffix

This example shows how to implement a chip group without a builder-defined suffix.

import { ChipSize, ChipGroup } from '@kit.ArkUI';

@Entry
@Preview
@Component
struct Index {
  @State selected\_index: Array<number> = \[0, 1, 2, 3, 4, 5, 6\];

  build() {
    Column() {
      ChipGroup({
        items: \[
          {
            // Replace $r('app.media.icon') with the image resource file you use.
            prefixIcon: { src: $r('app.media.icon') },
            label: { text: 'Chip 1' },
            suffixIcon: { src: $r('sys.media.ohos\_ic\_public\_cut') },
            allowClose: false
          },
          {
            prefixIcon: { src: $r('sys.media.ohos\_ic\_public\_copy') },
            label: { text: 'Chip 2' },
            allowClose: true
          },
          {
            prefixIcon: { src: $r('sys.media.ohos\_ic\_public\_clock') },
            label: { text: 'Chip 3' },
            allowClose: true
          },
          {
            prefixIcon: { src: $r('sys.media.ohos\_ic\_public\_cast\_stream') },
            label: { text: 'Chip 4' },
            allowClose: true
          },
          {
            prefixIcon: { src: $r('sys.media.ohos\_ic\_public\_cast\_mirror') },
            label: { text: 'Chip 5' },
            allowClose: true
          },
          {
            prefixIcon: { src: $r('sys.media.ohos\_ic\_public\_cast\_stream') },
            label: { text: 'Chip 6' },
            allowClose: true
          },
        \],
        itemStyle: {
          size: ChipSize.SMALL,
          backgroundColor: $r('sys.color.ohos\_id\_color\_button\_normal'),
          fontColor: $r('sys.color.ohos\_id\_color\_text\_primary'),
          selectedBackgroundColor: $r('sys.color.ohos\_id\_color\_emphasize'),
          selectedFontColor: $r('sys.color.ohos\_id\_color\_text\_primary\_contrary'),
        },
        selectedIndexes: this.selected\_index,
        multiple: false,
        chipGroupSpace: { itemSpace: 8, endSpace: 0 },
        chipGroupPadding: { top: 10, bottom: 10 },
        onChange: (activatedChipsIndex: Array<number>) => {
          console.info('chips on clicked, activated index ' + activatedChipsIndex);
        },
      })
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/2sPWRzldRqaiDSwgGUGdEg/en-us_image_0000002568685677.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062249Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DE913E835EF0728BB9D8D608CB64822EE0EC78F059A529201C51F4891B5AAFB2)

## Example 2: Implementing a Chip Group with a Builder-defined Suffix

This example shows how to implement a chip group with a builder-defined suffix.

import { ChipSize, ChipGroup, IconGroupSuffix } from '@kit.ArkUI';

@Entry
@Preview
@Component
struct Index {
  @State selected\_index: Array<number> = \[0, 1, 2, 3, 4, 5, 6\];
  @State selected\_state: boolean = true;

  @LocalBuilder
  ChipGroupSuffix(): void {
    IconGroupSuffix({
      items: \[{
        icon: { src: $r('sys.media.ohos\_ic\_public\_search\_filled'), size: { width: 36, height: 36 } },
        action: () => {
          if (this.selected\_state == false) {
            this.selected\_index = \[0, 1, 2, 3, 4, 5, 6\];
            this.selected\_state = true;
          } else {
            this.selected\_index = \[\];
            this.selected\_state = false;
          }
        }
      }
      \]
    })
  }

  build() {
    Column() {
      ChipGroup({
        items: \[
          {
            // Replace $r('app.media.icon') with the image resource file you use.
            prefixIcon: { src: $r('app.media.icon') },
            label: { text: 'Chip 1' },
            suffixIcon: { src: $r('sys.media.ohos\_ic\_public\_cut') },
            allowClose: false
          },
          {
            prefixIcon: { src: $r('sys.media.ohos\_ic\_public\_copy') },
            label: { text: 'Chip 2' },
            allowClose: true
          },
          {
            prefixIcon: { src: $r('sys.media.ohos\_ic\_public\_clock') },
            label: { text: 'Chip 3' },
            allowClose: true
          },
          {
            prefixIcon: { src: $r('sys.media.ohos\_ic\_public\_cast\_stream') },
            label: { text: 'Chip 4' },
            allowClose: true
          },
          {
            prefixIcon: { src: $r('sys.media.ohos\_ic\_public\_cast\_mirror') },
            label: { text: 'Chip 5' },
            allowClose: true
          },
          {
            prefixIcon: { src: $r('sys.media.ohos\_ic\_public\_cast\_stream') },
            label: { text: 'Chip 6' },
            allowClose: true
          },
        \],
        itemStyle: {
          size: ChipSize.NORMAL,
          backgroundColor: $r('sys.color.ohos\_id\_color\_button\_normal'),
          fontColor: $r('sys.color.ohos\_id\_color\_text\_primary'),
          selectedBackgroundColor: $r('sys.color.ohos\_id\_color\_emphasize'),
          selectedFontColor: $r('sys.color.ohos\_id\_color\_text\_primary\_contrary'),
        },
        selectedIndexes: this.selected\_index,
        multiple: true,
        chipGroupSpace: { itemSpace: 8, endSpace: 0 },
        chipGroupPadding: { top: 10, bottom: 10 },
        onChange: (activatedChipsIndex: Array<number>) => {
          console.info('chips on clicked, activated index ' + activatedChipsIndex);
        },
        suffix: this.ChipGroupSuffix
      })
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/tlNrJqHESICV1JrP1T4DlQ/en-us_image_0000002568765687.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062249Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=51748632078E313C00CAD961D7D9E781327B9676F712D891D04563E97D05EE6E)

## Example 3: Setting the Symbol Icon

This example implements **IconGroupSuffix** and **ChipGroup** with **SymbolGlyph** resources.

import { ChipSize, ChipGroup, IconGroupSuffix, SymbolGlyphModifier } from '@kit.ArkUI';

@Entry
@Preview
@Component
struct Index {
  @State selected\_index: Array<number> = \[0, 1, 2, 3, 4, 5, 6\];
  @State selected\_state: boolean = true;
  @State prefixModifierNormal: SymbolGlyphModifier = new SymbolGlyphModifier($r('sys.symbol.ohos\_star'));
  @State prefixModifierActivated: SymbolGlyphModifier =
    new SymbolGlyphModifier($r('sys.symbol.ohos\_star')).fontColor(\[Color.Red\]);
  @State suffixModifierNormal: SymbolGlyphModifier = new SymbolGlyphModifier($r('sys.symbol.ohos\_wifi'));
  @State suffixModifierActivated: SymbolGlyphModifier =
    new SymbolGlyphModifier($r('sys.symbol.ohos\_wifi')).fontColor(\[Color.Red\]);

  @LocalBuilder
  ChipGroupSuffix(): void {
    IconGroupSuffix({
      items: \[
        new SymbolGlyphModifier($r('sys.symbol.magnifyingglass'))
          .onClick(() => {
            if (this.selected\_state == false) {
              this.selected\_index = \[0, 1, 2, 3, 4, 5, 6\];
              this.selected\_state = true;
            } else {
              this.selected\_index = \[\];
              this.selected\_state = false;
            }
          })
      \]
    })
  }

  build() {
    Column() {
      ChipGroup({
        items: \[
          {
            prefixSymbol: { normal: this.prefixModifierNormal, activated: this.prefixModifierActivated },
            label: { text: 'Chip 1' },
            suffixSymbol: { normal: this.suffixModifierNormal, activated: this.suffixModifierActivated },
            allowClose: false,
          },
          {
            prefixSymbol: { normal: this.prefixModifierNormal, activated: this.prefixModifierActivated },
            label: { text: 'Chip 2' },
            allowClose: true,
          },
          {
            prefixIcon: { src: $r('sys.media.ohos\_ic\_public\_clock') },
            label: { text: 'Chip 3' },
            allowClose: true,
          },
          {
            prefixIcon: { src: $r('sys.media.ohos\_ic\_public\_cast\_stream') },
            label: { text: 'Chip 4' },
            allowClose: true,
          },
          {
            prefixIcon: { src: $r('sys.media.ohos\_ic\_public\_cast\_mirror') },
            label: { text: 'Chip 5' },
            allowClose: true,
          },
          {
            prefixIcon: { src: $r('sys.media.ohos\_ic\_public\_cast\_stream') },
            label: { text: 'Chip 6' },
            allowClose: true,
          },
        \],
        itemStyle: {
          size: ChipSize.NORMAL,
          backgroundColor: $r('sys.color.ohos\_id\_color\_button\_normal'),
          fontColor: $r('sys.color.ohos\_id\_color\_text\_primary'),
          selectedBackgroundColor: $r('sys.color.ohos\_id\_color\_emphasize'),
          selectedFontColor: $r('sys.color.ohos\_id\_color\_text\_primary\_contrary'),
        },
        selectedIndexes: this.selected\_index,
        multiple: true,
        chipGroupSpace: { itemSpace: 8, endSpace: 0 },
        chipGroupPadding: { top: 10, bottom: 10 },
        onChange: (activatedChipsIndex: Array<number>) => {
          console.info('chips on clicked, activated index ' + activatedChipsIndex);
        },
        suffix: this.ChipGroupSuffix
      })
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/UmbcuE4_QJa-7XBPq4tNAw/en-us_image_0000002537765962.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062249Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1A557CAF74BD1ABC6D9674EC05556175F44C1F217383E7748B57D2828C32D7CE)

## Example 4: Implementing the Screen Reader Feature for the Single-Selection Scenario

This example demonstrates how to implement the screen reader feature for a chip group with and without a suffix area in single-selection mode. The content to be read is the value of the **accessibilityText** attribute.

import { ChipGroup, IconGroupSuffix, SymbolGlyphModifier } from '@kit.ArkUI';

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
export struct ChipGroupExample2 {
  @LocalBuilder
  Suffix() {
    IconGroupSuffix({
      items: \[
        {
          icon: { src: $r('sys.media.ohos\_ic\_public\_more'), },
          accessibilityText: 'More', // Read "More, button, usage hints."
          accessibilityDescription: 'Usage hints',
          action: () => {
            this.getUIContext().getPromptAction().showToast({
              message: 'More icon touched.'
            });
          }
        },
        {
          symbol: new SymbolGlyphModifier($r('sys.symbol.more')),
          accessibilityText: 'More', // Read "More, button, usage hints."
          accessibilityDescription: 'Usage hints',
          action: () => {
            this.getUIContext().getPromptAction().showToast({
              message: 'More icon touched.'
            });
          }
        },
        {
          icon: { src: $r('sys.media.ohos\_ic\_public\_more'), },
          accessibilityText: 'More', // If accessibilityLevel is set to no, accessibilityText and accessibilityDescription do not take effect.
          accessibilityDescription: 'Usage hints',
          accessibilityLevel: 'no',
          action: () => {
            this.getUIContext().getPromptAction().showToast({
              message: 'More icon touched.'
            });
          }
        }
      \]
    })
  }

  build() {
    NavDestination() {
      Scroll() {
        Column({ space: 12 }) {
          SectionGroup({ title: 'Available' }) {
            SectionItem({ title: 'Single selection without suffix area' }) {
              ChipGroup({
                items: \[
                  {
                    prefixIcon: {
                      src: $r('app.media.startIcon')
                    },
                    label: { text: 'Option 1' },
                    suffixImageIcon: {
                      src: $r('sys.media.save\_button\_picture'),
                      accessibilityText: 'Save', // Read "Save, button."
                      action: () => {
                        this.getUIContext().getPromptAction().showToast({
                          message: 'Suffix icon touched.'
                        });
                      },
                    }
                  },
                  {
                    label: { text: 'Option 2' },
                    suffixSymbol: {
                      normal: new SymbolGlyphModifier($r('sys.symbol.save')),
                      activated: new SymbolGlyphModifier($r('sys.symbol.save'))
                    },
                    suffixSymbolOptions: {
                      normalAccessibility: {
                        accessibilityText: 'Save' // Read "Save, button."
                      },
                      action: () => {
                        this.getUIContext().getPromptAction().showToast({
                          message: 'Suffix icon touched.'
                        });
                      }
                    }
                  },
                  {
                    label: { text: 'Option 3' },
                    suffixIcon: { src: $r('sys.media.save\_button\_picture'), }
                  },
                  { label: { text: 'Option 4' } },
                  { label: { text: 'Option 5' } },
                  { label: { text: 'Option 6' } },
                  { label: { text: 'Option 7' } },
                  { label: { text: 'Option 8' } },
                  { label: { text: 'Option 9' } },
                \]
              })
            }

            SectionItem({ title: 'Single selection with suffix area' }) {
              ChipGroup({
                items: \[
                  { label: { text: 'Option 1' } },
                  { label: { text: 'Option 2' } },
                  { label: { text: 'Option 3' } },
                  { label: { text: 'Option 4' } },
                  { label: { text: 'Option 5' } },
                  { label: { text: 'Option 6' } },
                  { label: { text: 'Option 7' } },
                  { label: { text: 'Option 8' } },
                  { label: { text: 'Option 9' } },
                \],
                suffix: this.Suffix,
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
    .title('Basic usage')
    .backgroundColor('#F1F3F5')
  }
}

## Example 5: Implementing the Screen Reader Feature for the Multi-selection Scenario

This example demonstrates how to implement the screen reader feature for a chip group with and without a suffix area in multi-selection mode. The content to be read is the value of the **accessibilityText** attribute.

import { ChipGroup, IconGroupSuffix, SymbolGlyphModifier } from '@kit.ArkUI';

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
export struct ChipGroupExample2 {
  @LocalBuilder
  Suffix() {
    IconGroupSuffix({
      items: \[
        {
          icon: { src: $r('sys.media.ohos\_ic\_public\_more'), },
          accessibilityText: 'More', // Read "More, button, usage hints."
          accessibilityDescription: 'Usage hints',
          action: () => {
            this.getUIContext().getPromptAction().showToast({
              message: 'More icon touched.'
            });
          }
        },
        {
          symbol: new SymbolGlyphModifier($r('sys.symbol.more')),
          accessibilityText: 'More', // Read "More, button, usage hints."
          accessibilityDescription: 'Usage hints',
          action: () => {
            this.getUIContext().getPromptAction().showToast({
              message: 'More icon touched.'
            });
          }
        },
        {
          icon: { src: $r('sys.media.ohos\_ic\_public\_more'), },
          accessibilityText: 'More', // If accessibilityLevel is set to no, accessibilityText and accessibilityDescription do not take effect.
          accessibilityDescription: 'Usage hints',
          accessibilityLevel: 'no',
          action: () => {
            this.getUIContext().getPromptAction().showToast({
              message: 'More icon touched.'
            });
          }
        }
      \]
    })
  }

  build() {
    NavDestination() {
      Scroll() {
        Column({ space: 12 }) {
          SectionGroup({ title: 'Available' }) {
            SectionItem({ title: 'Multi-selection without suffix area' }) {
              ChipGroup({
                items: \[
                  { label: { text: 'Option 1' } },
                  { label: { text: 'Option 2' } },
                  { label: { text: 'Option 3' } },
                  { label: { text: 'Option 4' } },
                  { label: { text: 'Option 5' } },
                  { label: { text: 'Option 6' } },
                  { label: { text: 'Option 7' } },
                  { label: { text: 'Option 8' } },
                  { label: { text: 'Option 9' } },
                \],
                multiple: true
              })
            }

            SectionItem({ title: 'Multi-selection with suffix area' }) {
              ChipGroup({
                items: \[
                  { label: { text: 'Option 1' } },
                  { label: { text: 'Option 2' } },
                  { label: { text: 'Option 3' } },
                  { label: { text: 'Option 4' } },
                  { label: { text: 'Option 5' } },
                  { label: { text: 'Option 6' } },
                  { label: { text: 'Option 7' } },
                  { label: { text: 'Option 8' } },
                  { label: { text: 'Option 9' } },
                \],
                suffix: this.Suffix,
                multiple: true,
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
    .title('Basic usage')
    .backgroundColor('#F1F3F5')
  }
}
