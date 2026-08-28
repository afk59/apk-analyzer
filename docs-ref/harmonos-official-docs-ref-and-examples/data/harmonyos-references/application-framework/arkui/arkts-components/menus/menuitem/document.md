# MenuItem

The **MenuItem** component represents an item in a menu.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/8tAtprleQhavAooAFY96KA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062246Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E95C01525A233D2B7E8364C2A1F846E665D1DD6DCF4FF052D77E248FD5858064)

This component is supported since API version 9. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Child Components

Not supported

#### APIs

MenuItem(value?: MenuItemOptions | CustomBuilder)

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [MenuItemOptions](#menuitemoptions) | [CustomBuilder](../../common-definitions/basic-types/document.md#custombuilder8) | No | Information about the menu item. |

#### MenuItemOptions

Provides information about the menu item.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| startIcon | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 
Start icon of the menu item. Symbol icons are not supported. If a symbol icon is used, **symbolStartIcon** must be used.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| content | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 

Content of the menu item.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| endIcon | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 

End icon of the menu item. Symbol icons are not supported. If the symbol icon is used, **symbolEndIcon** must be used.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| labelInfo | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 

Label information at the end of the menu item, such as shortcut keys like Ctrl+C.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| builder | [CustomBuilder](../../common-definitions/basic-types/document.md#custombuilder8) | No | Yes | 

Builder for a level-2 menu.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| symbolStartIcon12+ | [SymbolGlyphModifier](../../universal-attributes/modifiers-and-custom-property/symbol-glyph-modifier/document.md) | No | Yes | 

Symbol icon at the start of a menu item. When this parameter is set, the icon set through **startIcon** is not displayed.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| symbolEndIcon12+ | [SymbolGlyphModifier](../../universal-attributes/modifiers-and-custom-property/symbol-glyph-modifier/document.md) | No | Yes | 

Symbol icon at the end of a menu item. When this parameter is set, the icon set through **endIcon** is not displayed.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |

#### Attributes

In addition to the [universal attributes](../../universal-attributes/document.md), the following attributes are supported.

#### \[h2\]selected

selected(value: boolean)

Sets whether the menu item is selected.

Since API version 10, this parameter supports two-way binding through [$$](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-two-way-sync).

Since API version 18, this parameter supports two-way binding through [!!](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-new-binding#two-way-binding-between-built-in-component-parameters).

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | boolean | Yes | 
Whether the menu item is selected.

**true**: The menu item is selected. **false**: The menu item is not selected.

Default value: **false**.

 |

#### \[h2\]selectIcon

selectIcon(value: boolean | ResourceStr | SymbolGlyphModifier)

Sets whether to display the selected icon when the menu item is selected.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | boolean | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr)10+| [SymbolGlyphModifier](../../universal-attributes/modifiers-and-custom-property/symbol-glyph-modifier/document.md)12+ | Yes | 
Whether to display the selected icon when the menu item is selected.

**true**: Display the default check mark icon. **false**: Hide the selected state icon.

**ResourceStr**: Display the specified custom icon resource.

**SymbolGlyphModifier**: Display the specified HMSymbol icon.

Default value: **false**.

 |

#### \[h2\]contentFont10+

contentFont(value: Font)

Sets the font style of the menu item content.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [Font](../../common-definitions/basic-types/document.md#font) | Yes | Font style of the menu item content. |

#### \[h2\]contentFontColor10+

contentFontColor(value: ResourceColor)

Sets the font color of the menu item content.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | Yes | 
Font color of the menu item content.

Default value: **'#E5000000'**

 |

#### \[h2\]labelFont10+

labelFont(value: Font)

Sets the font style of the menu item label.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [Font](../../common-definitions/basic-types/document.md#font) | Yes | Font style of the menu item label. |

#### \[h2\]labelFontColor10+

labelFontColor(value: ResourceColor)

Sets the font color of the menu item label.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | Yes | 
Font color of the menu item label.

Default value: **'#99000000'**

 |

#### Events

#### \[h2\]onChange

onChange(callback: (selected: boolean) => void)

Triggered when the selection status of the menu item is changed manually.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| selected | boolean | Yes | 
Invoked when the selected status changes.

**true**: selected; **false**: unselected.

 |

#### Example

See the example of [Menu](../menu/document.md#example).
