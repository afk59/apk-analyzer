# Select

The **Select** component provides a drop-down menu that allows users to select among multiple options.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/aOsTo-byQZycsIltzo5wew/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062241Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BA8421BC62039D77C8861BC49A3CF1ABE048B1AFB235A0AC81CE3BD348FE7EB7)

This component is supported since API version 8. Updates will be marked with a superscript to indicate their earliest API version.

#### Child Components

Not supported

#### APIs

Select(options: Array<SelectOption>)

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | Array<[SelectOption](#selectoption)\> | Yes | Options of the drop-down menu. |

#### SelectOption

Provides information about the drop-down menu options.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| value | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | No | 
Value of the drop-down menu option.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| icon | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 

Icon of the drop-down menu option.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| symbolIcon12+ | [SymbolGlyphModifier](../../universal-attributes/modifiers-and-custom-property/symbol-glyph-modifier/document.md) | No | Yes | 

Symbol icon of drop-down menu option.

**symbolIcon** takes precedence over **icon**.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |

#### Attributes

In addition to the [universal attributes](../../universal-attributes/document.md), the following attributes are supported.

#### \[h2\]selected

selected(value: number | Resource)

Sets the index of the initially selected option in the drop-down menu, where the first option has an index of 0. When **selected** is set to an invalid value or is not set, the default default **\-1** is used, which indicates no selection. When **selected** is set to **undefined** or **null**, the first option is selected.

Since API version 10, this attribute supports two-way binding through [$$](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-two-way-sync).

Since API version 18, this attribute supports two-way binding through [!!](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-new-binding#two-way-binding-between-built-in-component-parameters).

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | [Resource](../../common-definitions/basic-types/document.md#resource)11+ | Yes | Index of the initially selected option. The index is zero-based. |

#### \[h2\]selected18+

selected(numCount: Optional<number | Resource>)

Sets the index of the initially selected option in the drop-down menu, where the first option has an index of 0. When **selected** is set to an invalid value or is not set, the default default **\-1** is used, which indicates no selection. When **selected** is set to **undefined** or **null**, the first option is selected.

This attribute supports two-way binding through [$$](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-two-way-sync) and [!!](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-new-binding#two-way-binding-between-built-in-component-parameters).

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| numCount | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<number | [Resource](../../common-definitions/basic-types/document.md#resource)\> | Yes | 
Index of the initially selected option.

When **numCount** is set to **undefined**, the first option is selected.

 |

#### \[h2\]value

value(value: ResourceStr)

Sets the text content of drop-down button. After a menu option is selected, the button text will automatically update to display the selected option's text.

Since API version 10, this attribute supports two-way binding through [$$](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-two-way-sync).

Since API version 18, this attribute supports two-way binding through [!!](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-new-binding#two-way-binding-between-built-in-component-parameters).

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr)11+ | Yes | 
Text of the drop-down button.

Note: If the text exceeds the column width, it will be truncated.

 |

#### \[h2\]value18+

value(resStr: Optional<ResourceStr>)

Sets the text content of drop-down button. After a menu option is selected, the button text will automatically update to display the selected option's text. Compared with [value](#value), this API supports the **undefined** type for the **resStr** parameter.

This attribute supports two-way binding through [$$](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-two-way-sync) and [!!](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-new-binding#two-way-binding-between-built-in-component-parameters).

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resStr | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<[ResourceStr](../../common-definitions/basic-types/document.md#resourcestr)\> | Yes | 
Text of the drop-down button.

If **resStr** is set to **undefined**, the previous value is retained.

 |

#### \[h2\]controlSize12+

controlSize(value: ControlSize)

Sets the size of the **Select** component.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ControlSize](../button/document.md#controlsize11)11+ | Yes | 
Size of the **Select** component.

Default value: **ControlSize.NORMAL**

 |

The priorities of **controlSize**, **width**, and **height** are as follows:

1.  If only **width** and **height** are set and the text is too large to fit in the component, the text exceeds the component size and overflow text is displayed as an ellipsis (...).
    
2.  If **controlSize** is set but **width** and **height** are not set, the component size automatically adapts to the text content. The text will not exceed the component, and the **minWidth** and **minHeight** settings are automatically applied.
    
3.  If **controlSize**, **width**, and **height** are all set, the values of **width** and **height** take effect. However, if the values of **width** and **height** are less than the values of **minWidth** and **minHeight** set by **controlSize**, they will not take effect. In this case, the minimum width (**minWidth**) and minimum height (**minHeight**) settings will be enforced instead.
    

#### \[h2\]controlSize18+

controlSize(size: Optional<ControlSize>)

Sets the size of the **Select** component. Compared with [controlSize](#controlsize12)12+, this API supports the **undefined** type for **size** parameter.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| size | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<[ControlSize](../button/document.md#controlsize11)\> | Yes | 
Size of the **Select** component.

If **size** is set to **undefined**, the default value **ControlSize.NORMAL** is used.

 |

The priorities of **controlSize**, **width**, and **height** are as follows:

1.  If only **width** and **height** are set and the text is too large to fit in the component, the text exceeds the component size and overflow text is displayed as an ellipsis (...).
    
2.  If **controlSize** is set but **width** and **height** are not set, the component size automatically adapts to the text content. The text will not exceed the component, and the **minWidth** and **minHeight** settings are automatically applied.
    
3.  If **controlSize**, **width**, and **height** are all set, the values of **width** and **height** take effect. However, if the values of **width** and **height** are less than the values of **minWidth** and **minHeight** set by **controlSize**, they will not take effect. In this case, the minimum width (**minWidth**) and minimum height (**minHeight**) settings will be enforced instead.
    

#### \[h2\]menuItemContentModifier12+

menuItemContentModifier(modifier: ContentModifier<MenuItemConfiguration>)

Creates a content modifier for the drop-down menu. After **menuItemContentModifier** is applied, the drop-down menu content will be completely customized by the developer, and the **Select** component's attributes, including the divider, option color, and drop-down menu font color, will not take effect.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/AWP-tnlGQ3mRgSvVfbpNXw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062241Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EDA509F6D101C433D522D4B345180E32E45AEE2AB3B80DC51360721EFE572238)

This API cannot be called within [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| modifier | [ContentModifier](../../universal-attributes/modifiers-and-custom-property/content-modifier/document.md#contentmodifiert)[<MenuItemConfiguration>](#menuitemconfiguration12) | Yes | 
Content modifier to apply to the drop-down menu.

**modifier**: content modifier. You need a custom class to implement the **ContentModifier** API.

 |

#### \[h2\]menuItemContentModifier18+

menuItemContentModifier(modifier: Optional<ContentModifier<MenuItemConfiguration>>)

Creates a content modifier for the drop-down menu. Compared with [menuItemContentModifier](#menuitemcontentmodifier12)12+, this API supports the **undefined** type for **modifier** parameter. After **menuItemContentModifier** is applied, the drop-down menu content will be completely customized by the developer, and the **Select** component's attributes, including the divider, option color, and drop-down menu font color, will not take effect.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/XnGDTZVJRsGg7S-Vm5X1NA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062241Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=645D170E591C0024063D358E15A96D553864A2F46086F403E63E898440BB5FE5)

This API cannot be called within [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier).

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| modifier | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<[ContentModifier](../../universal-attributes/modifiers-and-custom-property/content-modifier/document.md#contentmodifiert)[<MenuItemConfiguration>](#menuitemconfiguration12)\> | Yes | 
Content modifier to apply to the drop-down menu.

**modifier**: content modifier. You need a custom class to implement the **ContentModifier** API.

If **modifier** is set to **undefined**, no content modifier is used.

 |

#### \[h2\]divider12+

divider(options: Optional<DividerOptions> | null)

Sets the divider style. If this attribute is not set, the divider is displayed based on the default value.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<[DividerOptions](../textpicker/document.md#divideroptions12)\> | null | Yes | 
Divider options.

1\. If **DividerOptions** is set, the divider is displayed in the configured style.

Default value:

{

strokeWidth: '1px' ,

color: '#33182431'

}

2\. If this parameter is set to **null**, the divider is not displayed.

3\. If the value of **strokeWidth** is too larger, the divider may overlap the text. The divider extends both upwards and downwards from the bottom of each item.

4\. The default values for **startMargin** and **endMargin** are consistent with the style of the divider when the **divider** attribute is not set. If the sum of **startMargin** and **endMargin** is equal to the value of **optionWidth**, the divider is not displayed. If the sum of **startMargin** and **endMargin** exceeds the value of **optionWidth**, the divider line is displayed in the default style.

 |

#### \[h2\]dividerStyle19+

dividerStyle(style: Optional<DividerStyleOptions>)

Sets the divider style. If this attribute is not set, the divider is displayed based on the default value. This attribute cannot be used together with the **divider** attribute. The last one called will take effect.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| style | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<[DividerStyleOptions](../../common-definitions/basic-types/document.md#dividerstyleoptions12)\> | Yes | 
Divider options.

1\. If **DividerOptions** is set, the divider is displayed in the configured style.

Default value:

{

strokeWidth: '1px' ,

color: '#33182431'

}

2\. If this parameter is set to **null** or **undefined**, the default divider is displayed.

3\. When **mode** is set to **FLOAT\_ABOVE\_MENU**, be careful with the **strokeWidth** settings to avoid covering text. The divider extends both upwards and downwards from the bottom of each item. When **mode** is **EMBEDDED\_IN\_MENU**, the divider expands to fill its own space within the menu.

4\. The default values for **startMargin** and **endMargin** are consistent with the style of the divider when the **divider** attribute is not set. If the sum of **startMargin** and **endMargin** is equal to the value of **optionWidth**, the divider is not displayed. If the sum of **startMargin** and **endMargin** exceeds the value of **optionWidth**, the divider line is displayed in the default style.

 |

#### \[h2\]font

font(value: Font)

Sets the text style of the drop-down button. When **size** is set to **0**, the text is not displayed. When **size** is set to a negative value, the text is displayed at its default size.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [Font](../../common-definitions/basic-types/document.md#font) | Yes | 
Text style of the drop-down list button.

For API versions 11 and earlier, the default value is as follows:

{

size: $r('sys.float.ohos\_id\_text\_size\_button1'),

weight: FontWeight.Medium

}

Since API version 12: The default value of **size** is **$r('sys.float.ohos\_id\_text\_size\_button2')** in the case of **controlSize.SMALL** and **$r('sys.float.ohos\_id\_text\_size\_button1')** in other cases.

 |

#### \[h2\]font18+

font(selectFont: Optional<Font>)

Sets the text style of the drop-down button. When **size** is set to **0**, the text is not displayed. When **size** is set to a negative value, the text is displayed at its default size. Compared with [font](#font), this API supports the **undefined** type for the **selectFont** parameter.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| selectFont | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<[Font](../../common-definitions/basic-types/document.md#font)\> | Yes | 
Text style of the drop-down list button.

If **controlSize** is set to **controlSize.SMALL**, the default value of **size** is **$r('sys.float.ohos\_id\_text\_size\_button2')**. Otherwise, the default value is **$r('sys.float.ohos\_id\_text\_size\_button1')**.

If **selectFont** is set to **undefined**, the default font style is used.

 |

#### \[h2\]fontColor

fontColor(value: ResourceColor)

Sets the font color of the drop-down button.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | Yes | 
Font color of the drop-down button.

Default value: **$r('sys.color.ohos\_id\_color\_text\_primary')** with the opacity of **$r('sys.color.ohos\_id\_alpha\_content\_primary')**

 |

#### \[h2\]fontColor18+

fontColor(resColor: Optional<ResourceColor>)

Sets the font color of the drop-down button. Compared with [fontColor](#fontcolor), this API supports the **undefined** type for the **resColor** parameter.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resColor | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<[ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor)\> | Yes | 
Font color of the drop-down button.

When **resColor** is set to **undefined**, the default value is a blend of **$r('sys.color.ohos\_id\_color\_text\_primary')** with the opacity of **$r('sys.color.ohos\_id\_alpha\_content\_primary')**.

If **value** is set to **undefined**, the previous value is retained.

 |

#### \[h2\]selectedOptionBgColor

selectedOptionBgColor(value: ResourceColor)

Sets the background color of the selected option in the drop-down menu.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | Yes | 
Background color of the selected option in the drop-down menu.

Default value: **$r('sys.color.ohos\_id\_color\_component\_activated')** with the opacity of **$r('sys.color.ohos\_id\_alpha\_highlight\_bg')**

 |

#### \[h2\]selectedOptionBgColor18+

selectedOptionBgColor(resColor: Optional<ResourceColor>)

Sets the background color of the selected option in the drop-down menu. Compared with [selectedOptionBgColor](#selectedoptionbgcolor), this API supports the **undefined** type for the **resColor** parameter.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resColor | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<[ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor)\> | Yes | 
Background color of the selected option in the drop-down menu.

When **resColor** is set to **undefined**, the default value is a blend of **$r('sys.color.ohos\_id\_color\_component\_activated')** with the opacity of **$r('sys.color.ohos\_id\_alpha\_highlight\_bg')**.

 |

#### \[h2\]selectedOptionFont

selectedOptionFont(value: Font)

Sets the text font of the selected option in the drop-down menu. When **size** is set to **0**, the text is not displayed. When **size** is set to a negative value, the text is displayed at its default size.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [Font](../../common-definitions/basic-types/document.md#font) | Yes | 
Text font of the selected option in the drop-down menu.

Default value:

{

size: $r('sys.float.ohos\_id\_text\_size\_body1'),

weight: FontWeight.Regular

}

 |

#### \[h2\]selectedOptionFont18+

selectedOptionFont(selectFont: Optional<Font>)

Sets the text font of the selected option in the drop-down menu. When **size** is set to **0**, the text is not displayed. When **size** is set to a negative value, the text is displayed at its default size. Compared with [selectedOptionFont](#selectedoptionfont), this API supports the **undefined** type for the **selectFont** parameter.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| selectFont | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<[Font](../../common-definitions/basic-types/document.md#font)\> | Yes | 
Text font of the selected option in the drop-down menu.

If **selectFont** is set to **undefined**, the default value is used:

{

size: $r('sys.float.ohos\_id\_text\_size\_body1'),

weight: FontWeight.Regular

}

 |

#### \[h2\]selectedOptionFontColor

selectedOptionFontColor(value: ResourceColor)

Sets the font color of the selected option in the drop-down menu.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | Yes | 
Font color of the selected option in the drop-down menu.

Default value: **$r('sys.color.ohos\_id\_color\_text\_primary\_activated')**

 |

#### \[h2\]selectedOptionFontColor18+

selectedOptionFontColor(resColor: Optional<ResourceColor>)

Sets the font color of the selected option in the drop-down menu. Compared with [selectedOptionFontColor](#selectedoptionfontcolor), this API supports the **undefined** type for the **resColor** parameter.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resColor | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<[ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor)\> | Yes | 
Font color of the selected option in the drop-down menu.

If **resColor** is set to **undefined**, the default value **$r('sys.color.ohos\_id\_color\_text\_primary\_activated')** is used.

 |

#### \[h2\]optionBgColor

optionBgColor(value: ResourceColor)

Sets the background color of options in the drop-down menu.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | Yes | 
Background color of options in the drop-down menu.

Default value:

Versions earlier than API version 11: **Color.White**

Since API version 11: **Color.Transparent**

 |

#### \[h2\]optionBgColor18+

optionBgColor(resColor: Optional<ResourceColor>)

Sets the background color of options in the drop-down menu. Compared with [optionBgColor](#optionbgcolor), this API supports the **undefined** type for the **resColor** parameter.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resColor | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<[ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor)\> | Yes | 
Background color of options in the drop-down menu.

When the value of resColor is undefined, the background color of the drop-down menu item is Color.White.

 |

#### \[h2\]optionFont

optionFont(value: Font)

Sets the text font of options in the drop-down menu. When **size** is set to **0**, the text is not displayed. When **size** is set to a negative value, the text is displayed at its default size.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [Font](../../common-definitions/basic-types/document.md#font) | Yes | 
Text font of options in the drop-down menu.

Default value:

{

size: $r('sys.float.ohos\_id\_text\_size\_body1'),

weight: FontWeight.Regular

}

 |

#### \[h2\]optionFont18+

optionFont(selectFont: Optional<Font>)

Sets the text font of options in the drop-down menu. When **size** is set to **0**, the text is not displayed. When **size** is set to a negative value, the text is displayed at its default size.

Compared with [optionFont](#optionfont), this API supports the **undefined** type for the **selectFont** parameter.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| selectFont | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<[Font](../../common-definitions/basic-types/document.md#font)\> | Yes | 
Text font of options in the drop-down menu.

If **selectFont** is set to **undefined**, the default value is used:

{

size: $r('sys.float.ohos\_id\_text\_size\_body1'),

weight: FontWeight.Regular

}

 |

#### \[h2\]optionFontColor

optionFontColor(value: ResourceColor)

Sets the font color of options in the drop-down menu.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | Yes | 
Font color of options in the drop-down menu.

Default value: **$r('sys.color.ohos\_id\_color\_text\_primary')**

 |

#### \[h2\]optionFontColor18+

optionFontColor(resColor: Optional<ResourceColor>)

Sets the font color of options in the drop-down menu. Compared with [optionFontColor](#optionfontcolor), this API supports the **undefined** type for the **resColor** parameter.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resColor | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<[ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor)\> | Yes | 
Font color of options in the drop-down menu.

If **resColor** is set to **undefined**, the default value **$r('sys.color.ohos\_id\_color\_text\_primary')** is used.

 |

#### \[h2\]space10+

space(value: Length)

Sets the spacing between the text and arrow of a drop-down menu option. This attribute cannot be set in percentage. If the value specified is **null**, **undefined**, or less than or equal to 8, the default value is used.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [Length](../../common-definitions/basic-types/document.md#length) | Yes | 
Spacing between the text and arrow of a drop-down menu option.

Default value: **8**

Note: For the string type, percentage values are not supported.

 |

#### \[h2\]space18+

space(spaceLength: Optional<Length>)

Sets the spacing between the text and arrow of a drop-down menu option. This attribute cannot be set in percentage. If the value specified is **null**, **undefined**, or less than or equal to 8, the default value is used.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| spaceLength | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<[Length](../../common-definitions/basic-types/document.md#length)\> | Yes | 
Spacing between the text and arrow of an option.

If **spaceLength** is set to **undefined**, the default value **8** is used.

 |

#### \[h2\]arrowPosition10+

arrowPosition(value: ArrowPosition)

Sets the alignment between the text and arrow of an option.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ArrowPosition](#arrowposition10) | Yes | 
Alignment between the text and arrow of an option.

Default value: **ArrowPosition.END**

 |

#### \[h2\]arrowPosition18+

arrowPosition(position: Optional<ArrowPosition>)

Sets the alignment between the text and arrow of an option. Compared with [arrowPosition](#arrowposition10), this API supports the **undefined** type for the **position** parameter.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| position | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<[ArrowPosition](#arrowposition10)\> | Yes | 
Alignment between the text and arrow of an option.

If **position** is set to **undefined**, the default value **ArrowPosition.END** is used.

 |

#### \[h2\]menuAlign10+

menuAlign(alignType: MenuAlignType, offset?: Offset)

Sets the alignment between the drop-down button and the drop-down menu.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| alignType | [MenuAlignType](#menualigntype10) | Yes | 
Alignment type.

Default value: **MenuAlignType.START**

 |
| offset | [Offset](../../common-definitions/basic-types/document.md#offset) | No | 

Offset of the drop-down menu relative to the drop-down button after alignment based on the alignment type.

Default value: **{dx: 0, dy: 0}**

 |

#### \[h2\]menuAlign18+

menuAlign(alignType: Optional<MenuAlignType>, offset?: Offset)

Sets the alignment between the drop-down button and the drop-down menu. Compared with [menuAlign](#menualign10)10+, this API supports the **undefined** type for the **alignType** parameter.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| alignType | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<[MenuAlignType](#menualigntype10)\> | Yes | 
Alignment type.

If **alignType** is set to **undefined**, the default value **MenuAlignType.START** is used.

 |
| offset | [Offset](../../common-definitions/basic-types/document.md#offset) | No | 

Offset of the drop-down menu relative to the drop-down button after alignment based on the alignment type.

Default value: **{dx: 0, dy: 0}**

 |

#### \[h2\]optionWidth11+

optionWidth(value: Dimension | OptionWidthMode )

Sets the width for the drop-down menu option. Percentage values are not supported. **OptionWidthMode** specifies whether to inherit the width of the drop-down button.

If an invalid value or a value less than the minimum width of 56 vp is set, the attribute has no effect. In this case, the option width uses the default value, which is the width of two columns.

The **Select** component maintains 16 vp spacing from both left and right screen edges by default. This creates a 32 vp total horizontal margin (16 vp × 2). To prevent horizontal shifting when the drop-down menu is displayed, set the width of the component itself and its menu options to a value less than or equal to **calc(100% - 32 vp)**.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [Dimension](../../common-definitions/basic-types/document.md#dimension10) | [OptionWidthMode](../../common-definitions/enums/document.md#optionwidthmode11) | Yes | Width of the drop-down menu option. |

#### \[h2\]optionWidth18+

optionWidth(width: Optional<Dimension | OptionWidthMode> )

Sets the width for the drop-down menu option. Percentage values are not supported. **OptionWidthMode** specifies whether to inherit the width of the drop-down button. Compared with [optionWidth](#optionwidth11)11+, this API supports the **undefined** type for the **width** parameter.

If an invalid value or a value less than the minimum width of 56 vp is set, the attribute has no effect. In this case, the option width uses the default value, which is the width of two columns.

The **Select** component maintains 16 vp spacing from both left and right screen edges by default. This creates a 32 vp total horizontal margin (16 vp × 2). To prevent horizontal shifting when the drop-down menu is displayed, set the width of the component itself and its menu options to a value less than or equal to **calc(100% - 32 vp)**.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| width | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<[Dimension](../../common-definitions/basic-types/document.md#dimension10) | [OptionWidthMode](../../common-definitions/enums/document.md#optionwidthmode11)\> | Yes | 
Width of the drop-down menu option.

If **width** is set to **undefined**, it has no effect. In this case, the option width uses the default value, which is the width of two columns.

 |

#### \[h2\]optionHeight11+

optionHeight(value: Dimension)

Sets the maximum height for the drop-down menu. Percentage values are not supported. The default maximum height is 80% of the available screen height, and any custom maximum height setting must not exceed this limit.

This attribute has no effect when set to abnormal values or zero.

If the actual height of all drop-down menu options is less than the set height, the menu will automatically adjust to the actual content height.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [Dimension](../../common-definitions/basic-types/document.md#dimension10) | Yes | Maximum height of the drop-down menu. |

#### \[h2\]optionHeight18+

optionHeight(height: Optional<Dimension>)

Sets the maximum height for the drop-down menu. Percentage values are not supported. The default maximum height is 80% of the available screen height, and any custom maximum height setting must not exceed this limit. Compared with [optionHeight](#optionheight11)11+, this API supports the **undefined** type for the **height** parameter.

This attribute has no effect when set to abnormal values or zero.

If the actual height of all drop-down menu options is less than the set height, the menu will automatically adjust to the actual content height.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| height | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<[Dimension](../../common-definitions/basic-types/document.md#dimension10)\> | Yes | 
Maximum height of the drop-down menu.

If **height** is set to **undefined**, the default value, which is 80% of the available screen height, is used.

 |

#### \[h2\]menuBackgroundColor11+

menuBackgroundColor(value: ResourceColor)

Sets the background color of the drop-down menu.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/E05ta6uVQDu0rrfdf5C7gA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062241Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D62307C3D99B8395CFFA7FB36E8607CD780D723DD6E92934C3488CA7130AD8E0)

This API can be called within [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier) since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | Yes | 
Background color of the drop-down menu.

Default value:

Versions earlier than API version 11: **$r('sys.color.ohos\_id\_color\_card\_bg')**

Since API version 11: **Color.Transparent**

 |

#### \[h2\]menuBackgroundColor18+

menuBackgroundColor(resColor: Optional<ResourceColor>)

Sets the background color of the drop-down menu. Compared with [menuBackgroundColor](#menubackgroundcolor11)11+, this API supports the **undefined** type for the **resColor** parameter.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resColor | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<[ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor)\> | Yes | 
Background color of the drop-down menu.

If **resColor** is set to **undefined**, the default value **Color.Transparent** is used.

 |

#### \[h2\]menuBackgroundBlurStyle11+

menuBackgroundBlurStyle(value: BlurStyle)

Sets the background blur style of the drop-down menu.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/6HIUYLTkQoan0--QqiTrxg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062241Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=68A4D1447FB031EB5F2ED7631B3D3507A1690719B65721D1CED84B031D52712C)

This API can be called within [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier) since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [BlurStyle](../../universal-attributes/basic-attributes/background/document.md#blurstyle9) | Yes | 
Background blur style of the drop-down menu.

Default value: **BlurStyle.COMPONENT\_ULTRA\_THICK**

 |

#### \[h2\]menuBackgroundBlurStyle18+

menuBackgroundBlurStyle(style: Optional<BlurStyle>)

Sets the background blur style of the drop-down menu. Compared with [menuBackgroundBlurStyle](#menubackgroundblurstyle11)11+, this API supports the **undefined** type for the **style** parameter.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| style | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<[BlurStyle](../../universal-attributes/basic-attributes/background/document.md#blurstyle9)\> | Yes | 
Background blur style of the drop-down menu.

If **style** is set to **undefined**, the default value **BlurStyle.COMPONENT\_ULTRA\_THICK** is used.

 |

#### \[h2\]avoidance19+

avoidance(mode: AvoidanceMode)

Sets the avoidance mode for the drop-down menu.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| mode | [AvoidanceMode](#avoidancemode19) | Yes | 
Avoidance mode for the drop-down menu.

Default value: **AvoidanceMode.COVER\_TARGET**

 |

#### \[h2\]menuOutline20+

menuOutline(outline: MenuOutlineOptions)

Sets the outline style for the drop-down menu.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| outline | [MenuOutlineOptions](#menuoutlineoptions20) | Yes | Outline style of the drop-down menu. |

#### \[h2\]showDefaultSelectedIcon20+

showDefaultSelectedIcon(show: boolean)

Sets whether to display the default selection icon.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| show | boolean | Yes | 
Whether to display the default selection icon.

true: The default icon is displayed. false: The default icon is not displayed. The background color is highlighted to indicate that the icon is selected.

Default value: **false**

When show is set to true and the background color of the selected option is set, the background color of the selected option and the icon selected by default are displayed. If the background color of the selected item is not set using selectedOptionBgColor, the background color is not highlighted and only the icon selected by default is displayed.

 |

#### \[h2\]textModifier20+

textModifier(modifier: Optional<[TextModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md)\>)

Creates a text modifier to customize the text style of the **Select** button. After **textModifier** is applied, the text style of the **Select** button will be completely customized by the developer.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/uk7lPnbSRkWTorSRgv-r2Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062241Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1625FD029703388C4D80A77015C554428A88E7D4991F2C965B9959FC9F58E026)

This API cannot be called within [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier).

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| modifier | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<[TextModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md)\> | Yes | Text modifier to apply to the **Select** button for customizing the text style. |

#### \[h2\]arrowModifier20+

arrowModifier(modifier: Optional<SymbolGlyphModifier>)

Creates an arrow modifier to customize the drop-down arrow icon style of the **Select** button. After **arrowModifier** is applied, the drop-down arrow icon style of the **Select** button will be completely customized by the developer.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/aknbGBz9Qf2gtXy5dPTkCw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062241Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C7B612305FE465B2EF3640AEECD523328D9E9B487D6D0C12791AF8AC6B026073)

This API cannot be called within [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier).

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| modifier | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<[SymbolGlyphModifier](../../universal-attributes/modifiers-and-custom-property/symbol-glyph-modifier/document.md)\> | Yes | Arrow modifier to apply to the **Select** button for customizing the drop-down arrow icon style. |

#### \[h2\]optionTextModifier20+

optionTextModifier(modifier: Optional<[TextModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md)\>)

Creates an option text modifier to customize the text style of unselected options in the drop-down menu. After **optionTextModifier** is applied, the unselected option text style will be completely customized by the developer.

If both [optionFont](#optionfont) and **Font** of **optionTextModifier** are set, [optionFont](#optionfont) takes precedence. Any unspecified attributes in **optionFont** will use default values.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/FZ_ZxP44Qjebgc-hcUqK4w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062241Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=56EBF1300251E17C9B9F393010F44829B71FB3BDBCE86D6B54BB0E700A3AAA25)

This API cannot be called within [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier).

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| modifier | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<[TextModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md)\> | Yes | Option text modifier to apply to the **Select** component for customizing the text style of unselected options in the drop-down menu. |

#### \[h2\]selectedOptionTextModifier20+

selectedOptionTextModifier(modifier: Optional<[TextModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md)\>)

Creates a selected-option text modifier to customize the text style of selected options in the drop-down menu. After **selectedOptionTextModifier** is applied, the selected-option text style will be completely customized by the developer.

If both [selectedOptionFont](#selectedoptionfont) and **Font** of **selectedOptionTextModifier** are set, [selectedOptionFont](#selectedoptionfont) takes precedence. If **selectedOptionFont** is not set, [optionFont](#optionfont) settings are applied. Any unspecified attributes in **selectedOptionFont** or **optionFont** will use default values.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/zLiI8yPDQ76WFf430QxAoA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062241Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3BA9A37C883853F49AB05D49CE99022D29D55F83A58B234A514B38710479BE3D)

This API cannot be called within [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier).

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| modifier | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<[TextModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md)\> | Yes | 
Selected-option text modifier to apply to the **Select** component for customizing the text style of selected options in the drop-down menu.

You can manage and maintain the text style as needed.

 |

#### \[h2\]showInSubWindow20+

showInSubWindow(showInSubWindow:Optional<boolean>)

Sets whether the drop-down menu is displayed in the subwindow. If this API is not used, the drop-down menu is not displayed in the subwindow by default.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior difference**: This API is supported on PCs and 2-in-1 devices but not available on other devices.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| showInSubWindow | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<boolean> | Yes | 
Whether the drop-down menu is displayed in the subwindow.

**true**: The drop-down menu is displayed in the subwindow.

**false**: The drop-down menu is not displayed in the subwindow.

 |

#### ArrowPosition10+

Enumerates arrow positions.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| END | 0 | The text is in front of the arrow. |
| START | 1 | The arrow is in front of the text. |

#### MenuAlignType10+

Enumerates drop-down menu alignment modes.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| START | 0 | Aligned with the start edge in the same direction as the language in use. |
| CENTER | 1 | Aligned with the center. |
| END | 2 | Aligned with the end edge in the same direction as the language in use. |

#### AvoidanceMode19+

Enumerates the drop-down menu avoidance modes.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Description |
| :-- | :-- |
| COVER\_TARGET | If there is not enough space below the target component, cover the target component. |
| AVOID\_AROUND\_TARGET | If there is not enough space around the target component, compress and display in the largest available space (scrollable). |

#### MenuItemConfiguration12+

You need a custom class to implement the **ContentModifier** API. Inherits from [CommonConfiguration](../../universal-attributes/modifiers-and-custom-property/content-modifier/document.md#commonconfigurationt).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| value | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | No | 
Text content of the drop-down menu option.

**NOTE**

If the length of the text exceeds the width of the menu item text area, the text will be truncated.

 |
| icon | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 

Icon of the drop-down menu option.

**NOTE**

The string type can be used to load network images and local images.

 |
| symbolIcon | [SymbolGlyphModifier](../../universal-attributes/modifiers-and-custom-property/symbol-glyph-modifier/document.md) | No | Yes | Symbol icon of the drop-down menu option. |
| selected | boolean | No | No | 

Whether the drop-down menu option is selected. The value **true** means that the option is selected, and **false** means the opposite.

Default value: **false**

 |
| index | number | No | No | Index of the drop-down menu option. The index is zero-based. |
| triggerSelect | (index: number, value: string) :void | No | No | 

Invoked when a drop-down menu option is selected.

**index**: index of the selected option.

**value**: text of the selected option.

**NOTE**

The value of **index** will be assigned to the **index** parameter in the [onSelect](#onselect) callback; the value of **value** will be returned to the **Select** component for display and will also be assigned to the **value** parameter in the [onSelect](#onselect) callback.

 |

#### MenuOutlineOptions20+

Defines the outline of the drop-down menu.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| width | [Dimension](../../common-definitions/basic-types/document.md#dimension10) | [EdgeOutlineWidths](../../common-definitions/basic-types/document.md#edgeoutlinewidths11) | No | Yes | 
Width of the outline. Percentage values are not supported.

Default value: **0**

 |
| color | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | [EdgeColors](../../common-definitions/basic-types/document.md#edgecolors9) | No | Yes | 

Color of the outline.

Default value: **#19ffffff**

 |

#### Events

#### \[h2\]onSelect

onSelect(callback: (index: number, value: string) => void)

Triggered when a drop-down menu option is selected.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| index | number | Yes | Index of the selected option. The index is zero-based. |
| value | string | Yes | Value of the selected option. |

#### \[h2\]onSelect18+

onSelect(callback: Optional<OnSelectCallback> )

Triggered when a drop-down menu option is selected. Compared with [onSelect](#onselect), this API supports the **undefined** type for the **callback** parameter.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<[OnSelectCallback](#onselectcallback18)\> | Yes | 
Callback invoked when a drop-down menu option is selected.

If **callback** is set to **undefined**, the callback function is not used.

 |

#### OnSelectCallback18+

type OnSelectCallback = (index: number, selectStr: string) => void

Defines the callback invoked when a drop-down menu option is selected.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| index | number | Yes | Index of the selected option. The index is zero-based. |
| selectStr | string | Yes | Value of the selected option. |

#### Example 1: Creating a Drop-down Menu

This example demonstrates how to create a drop-down menu by configuring [SelectOption](#selectoption) and how to implement menu avoidance using the [avoidance](#avoidance19) attribute, available since API version 19.

// xxx.ets
@Entry
@Component
struct SelectExample {
  @State text: string = "TTTTT";
  @State index: number = 2;
  @State space: number = 8;
  @State arrowPosition: ArrowPosition = ArrowPosition.END;

  build() {
    Column() {
      // Replace $r('app.media.selection') with the image resource file you use.
      Select(\[{ value: 'aaa', icon: $r("app.media.selection") },
        { value: 'bbb', icon: $r("app.media.selection") },
        { value: 'ccc', icon: $r("app.media.selection") },
        { value: 'ddd', icon: $r("app.media.selection") }\])
        .selected(this.index)
        .value(this.text)
        .font({ size: 16, weight: 500 })
        .fontColor('#182431')
        .selectedOptionFont({ size: 16, weight: 400 })
        .optionFont({ size: 16, weight: 400 })
        .space(this.space)
        .arrowPosition(this.arrowPosition)
        .menuAlign(MenuAlignType.START, { dx: 0, dy: 0 })
        .optionWidth(200)
        .optionHeight(300)
        .onSelect((index: number, text?: string | undefined) => {
          console.info('Select:' + index);
          this.index = index;
          if (text) {
            this.text = text;
          }
        })
        .avoidance(AvoidanceMode.COVER\_TARGET);
    }.width('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/4fvQYeZfSiaYI9EejykU8w/en-us_image_0000002568685337.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062241Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=94687B5B5EAC1FCCE50B2A0DC1EFF0085B92895305A520D969299E1D496F809F)

#### Example 2: Setting the Symbol Icon

This example demonstrates how to create a drop-down menu with symbol icons in the **Select** component and implement menu avoidance using the [avoidance](#avoidance19) attribute, available since API version 19.

// xxx.ets
import { SymbolGlyphModifier } from '@kit.ArkUI';

@Entry
@Component
struct SelectExample {
  @State text: string = "TTTTT";
  @State index: number = 2;
  @State space: number = 8;
  @State arrowPosition: ArrowPosition = ArrowPosition.END;
  @State symbolModifier1: SymbolGlyphModifier =
    new SymbolGlyphModifier($r('sys.symbol.ohos\_wifi')).fontColor(\[Color.Green\]);
  @State symbolModifier2: SymbolGlyphModifier =
    new SymbolGlyphModifier($r('sys.symbol.ohos\_star')).fontColor(\[Color.Red\]);
  @State symbolModifier3: SymbolGlyphModifier =
    new SymbolGlyphModifier($r('sys.symbol.ohos\_trash')).fontColor(\[Color.Gray\]);
  @State symbolModifier4: SymbolGlyphModifier =
    new SymbolGlyphModifier($r('sys.symbol.exposure')).fontColor(\[Color.Gray\]);

  build() {
    Column() {
      Select(\[{ value: 'aaa', symbolIcon: this.symbolModifier1 },
        { value: 'bbb', symbolIcon: this.symbolModifier2 },
        { value: 'ccc', symbolIcon: this.symbolModifier3 },
        { value: 'ddd', symbolIcon: this.symbolModifier4 }\])
        .selected(this.index)
        .value(this.text)
        .font({ size: 16, weight: 500 })
        .fontColor('#182431')
        .selectedOptionFont({ size: 16, weight: 400 })
        .optionFont({ size: 16, weight: 400 })
        .space(this.space)
        .arrowPosition(this.arrowPosition)
        .menuAlign(MenuAlignType.START, { dx: 0, dy: 0 })
        .onSelect((index: number, text?: string | undefined) => {
          console.info('Select:' + index);
          this.index = index;
          if (text) {
            this.text = text;
          }
        })
        .avoidance(AvoidanceMode.COVER\_TARGET);
    }.width('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/Ir8OnCQ1RjqguHWkodByng/en-us_image_0000002568765347.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062241Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=50DE375C967AF7FF1493A353C9FDF3F7C3E7CF3ED055E364F007756AA9CC6B36)

#### Example 3: Implementing a Custom Drop-down Menu

This example implements a custom drop-down menu, each option of which consists of text + symbol + blank area + text + drawn triangle. After a menu option is clicked, the text content of the menu option is displayed.

import { SymbolGlyphModifier } from '@kit.ArkUI';

class MyMenuItemContentModifier implements ContentModifier<MenuItemConfiguration> {
  modifierText: string = "";

  constructor(text: string) {
    this.modifierText = text;
  }

  applyContent(): WrappedBuilder<\[MenuItemConfiguration\]> {
    return wrapBuilder(MenuItemBuilder);
  }
}

@Builder
function MenuItemBuilder(configuration: MenuItemConfiguration) {
  Row() {
    Text(configuration.value)
    Blank()
    if (configuration.symbolIcon) {
      SymbolGlyph().attributeModifier(configuration.symbolIcon).fontSize(24)
    } else if (configuration.icon) {
      Image(configuration.icon).size({ width: 24, height: 24 })
    }
    Blank(30)
    Text((configuration.contentModifier as MyMenuItemContentModifier).modifierText)
    Blank(30)
    Path()
      .width('100px')
      .height('150px')
      .commands('M40 0 L80 100 L0 100 Z')
      .fillOpacity(0)
      .stroke(Color.Black)
      .strokeWidth(3)
  }
  .onClick(() => {
    configuration.triggerSelect(configuration.index, configuration.value.valueOf().toString());
  })
}

@Entry
@Component
struct SelectExample {
  @State text: string = "Content Modifier Select";
  @State symbolModifier1: SymbolGlyphModifier =
    new SymbolGlyphModifier($r('sys.symbol.ohos\_trash')).fontColor(\[Color.Gray\]);
  @State symbolModifier2: SymbolGlyphModifier =
    new SymbolGlyphModifier($r('sys.symbol.exposure')).fontColor(\[Color.Gray\]);

  build() {
    Column() {
      Row() {
        // Replace $r('app.media.icon') with the image resource file you use.
        Select(\[{ value: 'item1', icon: $r('app.media.icon'), symbolIcon: this.symbolModifier1 },
          { value: 'item1', icon: $r('app.media.icon'), symbolIcon: this.symbolModifier2 }\])
          .value(this.text)
          .onSelect((index: number, text?: string) => {
            console.info('Select index:' + index);
            console.info('Select text:' + text);
          })
          .menuItemContentModifier(new MyMenuItemContentModifier("Content Modifier"))

      }.alignItems(VerticalAlign.Center).height('50%')
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/3RZ8UtrNRGa_drc4xnc3BQ/en-us_image_0000002537765622.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062241Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2AC4C013069DA646E11A1DDA7E8ECFF2C946B0342599592E981F0CE4095630E9)

#### Example 4: Using the Divider Style

This example uses **DividerOptions** to create a divider-style drop-down menu and implements menu avoidance using the [avoidance](#avoidance19) attribute, available since API version 19.

// xxx.ets
@Entry
@Component
struct SelectExample {
  @State text: string = "TTTTT";
  @State index: number = -1;
  @State arrowPosition: ArrowPosition = ArrowPosition.END;

  build() {
    Column() {
      // Replace $r('app.media.icon') with the image resource file you use.
      Select(\[{ value: 'aaa', icon: $r("app.media.icon") },
        { value: 'bbb', icon: $r("app.media.icon") },
        { value: 'ccc', icon: $r("app.media.icon") },
        { value: 'ddd', icon: $r("app.media.icon") }\])
        .selected(this.index)
        .value(this.text)
        .font({ size: 16, weight: 500 })
        .fontColor('#182431')
        .selectedOptionFont({ size: 16, weight: 400 })
        .optionFont({ size: 16, weight: 400 })
        .arrowPosition(this.arrowPosition)
        .menuAlign(MenuAlignType.START, { dx: 0, dy: 0 })
        .optionWidth(200)
        .optionHeight(300)
        .divider({
          strokeWidth: 5,
          color: Color.Blue,
          startMargin: 10,
          endMargin: 10
        })
        .onSelect((index: number, text?: string | undefined) => {
          console.info('Select:' + index);
          this.index = index;
          if (text) {
            this.text = text;
          }
        })
        .avoidance(AvoidanceMode.COVER\_TARGET);
    }.width('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/sJ71Sts3TR6gbvfHGRhBLg/en-us_image_0000002537925562.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062241Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AF1FDC98C077834233921D2E379ACC6CE04715E12C9C8145657C91B126E74440)

#### Example 5: Using the No-Divider Style

This example sets the **divider** attribute to **null** to remove dividers, and implements menu avoidance using the [avoidance](#avoidance19) attribute, available since API version 19.

// xxx.ets
@Entry
@Component
struct SelectExample {
  @State text: string = "TTTTT";
  @State index: number = -1;
  @State arrowPosition: ArrowPosition = ArrowPosition.END;

  build() {
    Column() {
      // Replace $r('app.media.icon') with the image resource file you use.
      Select(\[{ value: 'aaa', icon: $r("app.media.icon") },
        { value: 'bbb', icon: $r("app.media.icon") },
        { value: 'ccc', icon: $r("app.media.icon") },
        { value: 'ddd', icon: $r("app.media.icon") }\])
        .selected(this.index)
        .value(this.text)
        .font({ size: 16, weight: 500 })
        .fontColor('#182431')
        .selectedOptionFont({ size: 16, weight: 400 })
        .optionFont({ size: 16, weight: 400 })
        .arrowPosition(this.arrowPosition)
        .menuAlign(MenuAlignType.START, { dx: 0, dy: 0 })
        .optionWidth(200)
        .optionHeight(300)
        .divider(null)
        .onSelect((index: number, text?: string | undefined) => {
          console.info('Select:' + index);
          this.index = index;
          if (text) {
            this.text = text;
          }
        })
        .avoidance(AvoidanceMode.COVER\_TARGET);
    }.width('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/YA2TFJSgTfGS-eIun5fabw/en-us_image_0000002568685339.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062241Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CF72486AD187740576330908588E1AC94F2D1EE9CAF53A0F10ED42A53FA351BA)

#### Example 6: Setting the Text and Arrow Styles of the Select Component

This example illustrates how to configure the text and arrow styles of the **Select** component using the [textModifier](#textmodifier20) and [arrowModifier](#arrowmodifier20) attributes, available since API version 20.

import { TextModifier, SymbolGlyphModifier } from "@kit.ArkUI";

@Entry
@Component
struct SelectExample {
  @State text: string = "TTTTTTTTTT".repeat(3);
  @State index: number = 2;
  textModifier: TextModifier = new TextModifier();
  symbolGlyphModifier: SymbolGlyphModifier = new SymbolGlyphModifier();

  aboutToAppear(): void {
    this.textModifier
      .maxLines(2)
      .fontSize(18)
      .textAlign(TextAlign.Center)
      .fontColor('#333333')
      .fontWeight(FontWeight.Medium)
      .textOverflow({overflow:TextOverflow.Clip})

    this.symbolGlyphModifier
      .fontSize(25)
      .fontColor(\['#999999'\])
  }

  build() {
    Column() {
      Select(\[
        // Replace $r('app.media.startIcon') with the image resource file you use.
        { value: 'A very long option text that should be truncated nicely'.repeat(3), icon: $r("app.media.startIcon") },
        { value: 'Option B', icon: $r("app.media.startIcon") },
        { value: 'Option C', icon: $r("app.media.startIcon") },
        { value: 'Option D', icon: $r("app.media.startIcon") }
      \])
        .selected(this.index)
        .value(this.text)
        .textModifier(this.textModifier)
        .arrowModifier(this.symbolGlyphModifier)
        .onSelect((index: number, text?: string) => {
          console.info('Select:' + index);
          this.index = index;
          if (text) {
            this.text = text;
          }
        })
        .margin({ top: 20,left:30 })
        .borderRadius(12)
        .width(200)
        .padding(9)
        .backgroundColor(Color.White)
        .shadow({ radius: 10, color: '#888888', offsetX: 0, offsetY: 10 })
    }
    .alignItems(HorizontalAlign.Start)
    .padding(10)
    .backgroundColor('#F0F2F5')
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/ehwVpdlURUKusfPw4dnTQw/en-us_image_0000002568765349.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062241Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9F918B5660A9251BF1DCB3D6CE7F11F13C0BA0EFF8DCA4E0B0A13F122C86B9C6)

#### Example 7: Setting the Text Styles of Selected and Unselected Drop-Down Menu Options

This example demonstrates how to use the [optionTextModifier](#optiontextmodifier20) and [selectedOptionTextModifier](#selectedoptiontextmodifier20) attributes to set text styles for unselected and selected drop-down menu options, available since API version 20.

import { TextModifier } from "@kit.ArkUI";

@Entry
@Component
struct SelectExample {
  @State text: string = "TTTTTTTTTT".repeat(3);
  @State index: number = 2;
  optionTextModifier: TextModifier = new TextModifier();
  selectedOptionTextModifier: TextModifier = new TextModifier();
  aboutToAppear(): void {
    this.optionTextModifier
      .maxLines(1)
      .fontSize(16)
      .textAlign(TextAlign.Start)
      .fontColor('#666666')
      .fontWeight(FontWeight.Normal)
      .width(200)

    this.selectedOptionTextModifier
      .maxLines(1)
      .fontSize(18)
      .textAlign(TextAlign.Start)
      .fontColor('#007BFF')
      .fontWeight(FontWeight.Bold)
      .width(200)
  }

  build() {
    Column() {
      Select(\[
        // Replace $r('app.media.startIcon') with the image resource file you use.
        { value: 'A very long option text that should be truncated nicely'.repeat(3), icon: $r("app.media.startIcon") },
        { value: 'Option B', icon: $r("app.media.startIcon") },
        { value: 'Option C', icon: $r("app.media.startIcon") },
        { value: 'Option D', icon: $r("app.media.startIcon") }
      \])
        .selected(this.index)
        .value(this.text)
        .onSelect((index: number, text?: string) => {
          console.info('Select:' + index);
          this.index = index;
          if (text) {
            this.text = text;
          }
        })
        .optionTextModifier(this.optionTextModifier)
        .selectedOptionTextModifier(this.selectedOptionTextModifier)
        .margin({ top: 20,left:30 })
        .borderRadius(12)
        .width(200)
        .padding(9)
        .backgroundColor(Color.White)
        .shadow({ radius: 10, color: '#888888', offsetX: 0, offsetY: 10 })
    }
    .alignItems(HorizontalAlign.Start)
    .padding(10)
    .backgroundColor('#F0F2F5')
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/jUu_O6JHRgiE5xERVpaqQg/en-us_image_0000002537765624.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062241Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C73CBE9A93AAE2BD9DA29A41F7AE40D00492195A1C2240E254EB8F328B3C54BC)

#### Example 8: Setting the Divider Mode

This example shows how to set the divider mode by configuring the **mode** property of [DividerStyleOptions](../../common-definitions/basic-types/document.md#dividerstyleoptions12), supported since API version 19.

import { LengthMetrics } from '@kit.ArkUI'

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Select(\[{ value: "SelectItem" }, { value: "SelectItem" }, { value: "SelectItem" },\])
        .value("Select")
        .dividerStyle({
          strokeWidth: LengthMetrics.vp(5),
          color: '#d5d5d5',
          mode: DividerMode.EMBEDDED\_IN\_MENU
        })
    }
    .height('100%')
    .width('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/le7XOdUjTIy01Od__k_J3w/en-us_image_0000002537925564.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062241Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=227956CA65D2491048C328D5EA5C154C3FDB3DBBF7C736CB9FA97F518357849C)

#### Example 9: Setting the Outline Style of the Drop-Down Menu

This example shows how to set the outline style of the drop-down menu using the **width** and **color** properties of **menuOutline**, supported since API version 20.

// xxx.ets
@Entry
@Component
struct SelectExample {
  @State text: string = "TTTTT";
  @State index: number = -1;
  @State arrowPosition: ArrowPosition = ArrowPosition.END;

  build() {
    Column() {
      Select(\[{ value: 'aaa' },
        { value: 'bbb' },
        { value: 'ccc' },
        { value: 'ddd' }\])
        .selected(this.index)
        .value(this.text)
        .font({ size: 16, weight: 500 })
        .fontColor('#182431')
        .selectedOptionFont({ size: 16, weight: 400 })
        .optionFont({ size: 16, weight: 400 })
        .arrowPosition(this.arrowPosition)
        .menuAlign(MenuAlignType.START, { dx: 0, dy: 0 })
        .optionWidth(200)
        .optionHeight(300)
        .menuOutline({
          width: '5vp',
          color: Color.Blue
        })
        .onSelect((index: number, text?: string | undefined) => {
          console.info('Select:' + index);
          this.index = index;
          if (text) {
            this.text = text;
          }
        })
    }
    .width('100%')
    .height('100%')
    .backgroundColor('#F0F2F5')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/L-FiNlyiRK2_a73th3kn6Q/en-us_image_0000002568685341.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062241Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3DFB84D7EDF5BCDE1959FF348C3DA13A0C36815D95FB8BCC9B865FF62D1A713E)
