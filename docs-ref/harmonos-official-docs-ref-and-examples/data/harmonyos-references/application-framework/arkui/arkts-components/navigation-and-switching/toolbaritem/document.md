# ToolBarItem

You can use the **ToolBarItem** component to add toolbar items to the title bar using the [toolbar](../../universal-attributes/other/toolbar-configuration/document.md#toolbar) universal attribute.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/gBQ9ySgYSHi95-KaYwCYvQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=79FF1C40B1BCEAC3FE336D5B4A784502E1FC0E7725AB7E7391A38D69DC020428)

This component is supported since API version 20. Updates will be marked with a superscript to indicate their earliest API version.

This component is typically used with the [toolbar](../../universal-attributes/other/toolbar-configuration/document.md#toolbar) universal attribute.

#### Child Components

This component can contain a single child component.

#### APIs

#### \[h2\]ToolBarItem

ToolBarItem(options?: ToolBarItemOptions)

Creates a toolbar item at the beginning of the corresponding column in the title bar by default. The column position is determined by the component's [toolbar](../../universal-attributes/other/toolbar-configuration/document.md#toolbar) attribute configuration.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [ToolBarItemOptions](#toolbaritemoptions) | No | 
Optional parameters for **ToolBarItem**, including the **placement** parameter of the [ToolBarItemPlacement](#toolbaritemplacement) type.

Default value: **placement: ToolBarItemPlacement.TOP\_BAR\_LEADING**

 |

#### Attributes

The [universal attributes](../../universal-attributes/document.md) are not supported.

#### ToolBarItemOptions

Provides optional parameters for **ToolBarItem** configuration.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| placement | [ToolBarItemPlacement](#toolbaritemplacement) | No | Yes | 
Placement position of the toolbar item.

Default value: **ToolBarItemPlacement.TOP\_BAR\_LEADING**.

**ToolBarItemPlacement.TOP\_BAR\_LEADING**: places the item at the start of the top bar.

**ToolBarItemPlacement.TOP\_BAR\_TRAILING**: places the item at the end of the top bar.

 |

#### ToolBarItemPlacement

Enumerates the placement options for toolbar items in the title bar.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| TOP\_BAR\_LEADING | 0 | Places the item at the start of the top bar. |
| TOP\_BAR\_TRAILING | 1 | Places the item at the end of the top bar. |

#### Example

See [toolbar](../../universal-attributes/other/toolbar-configuration/document.md#example).
