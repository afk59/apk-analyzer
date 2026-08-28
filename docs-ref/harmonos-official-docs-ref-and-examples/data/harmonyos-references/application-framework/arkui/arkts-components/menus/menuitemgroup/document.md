# MenuItemGroup

The **MenuItemGroup** component represents a group of menu items.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/RkfqXBBZT5uAISHKDPDCRQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062246Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=399857247569DFB29850A64C61C17FE5295AA75AF7C39FCA7781AA3096B648DB)

This component is supported since API version 9. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Child Components

This component contains the [MenuItem](../menuitem/document.md) child component.

#### APIs

MenuItemGroup(value?: MenuItemGroupOptions)

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [MenuItemGroupOptions](#menuitemgroupoptions) | No | Header and footer of the menu item group. |

#### MenuItemGroupOptions

Describes the header and footer of the menu item group.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| header | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | [CustomBuilder](../../common-definitions/basic-types/document.md#custombuilder8) | No | Yes | Header of the menu item group. |
| footer | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | [CustomBuilder](../../common-definitions/basic-types/document.md#custombuilder8) | No | Yes | Footer of the menu item group. |

#### Sample

For details, see [Example in Menu](../menu/document.md#example).
