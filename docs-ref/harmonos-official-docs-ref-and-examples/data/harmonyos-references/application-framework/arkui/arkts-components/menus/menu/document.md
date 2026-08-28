# Menu

The **Menu** component is a vertical list of items presented to the user.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/oZgf_-aZQjS8UCgCXzakmw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062246Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=57D781CBECCBDE3D3C6430C756E911F6F0EEA86F17FED456AB1CCB1C2722AAE3)

-   This component is supported since API version 9. Newly added APIs will be marked with a superscript to indicate their earliest API version.
    
-   The **Menu** component must be used together with the [bindMenu](../../universal-attributes/dialog-box-control/menu-control/document.md#bindmenu) or [bindContextMenu](../../universal-attributes/dialog-box-control/menu-control/document.md#bindcontextmenu8) method. It does not work when used alone.
    

#### Child Components

This component contains the [MenuItem](../menuitem/document.md) and [MenuItemGroup](../menuitemgroup/document.md) child components.

#### APIs

Menu()

Creates a fixed container for a menu. This API does not have any parameters.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/ofzcENJqRIOcz1eJeIR55g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062246Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=709011EDEC150F37EF8CB687CFE3DB91BC8FB6AAF7D004A9529CA9A39C249A3A)

-   Rules for calculating the width of menus and menu items:
    
    -   During the layout, the width of each menu item is expected to be the same. If a child component has its width set, the [size calculation rule](../../universal-attributes/layout-and-borders/sizing/document.md#constraintsize) prevails.
        
    -   If no width is set for the **Menu** component, it applies a default two-column width to the **MenuItem** and **MenuItemGroup** child components. If a menu item's content area exceeds the two-column width, the **Menu** component automatically expands the menu item's content area.
        
    -   When an explicit width is set for the **Menu** component, its child components **MenuItem** and **MenuItemGroup** adopt a fixed width (equal to the **Menu** component's configured width minus the padding).
        
    -   The minimum width is 64 vp.
        
-   Universal attributes unsupported by **Menu**: [outline](../../universal-attributes/visual-effects/outline-styling/document.md) attributes and the [shadow](../../universal-attributes/visual-effects/image-effect/document.md#shadow) attribute
    

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### Attributes

In addition to the [universal attributes](../../universal-attributes/document.md), the following attributes are supported.

#### \[h2\]font10+

font(value: Font)

Sets the size of all text within the menu.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [Font](../../common-definitions/basic-types/document.md#font) | Yes | 
Size of all text within the menu.

Default value:

{

size: 16,

family: 'HarmonyOS Sans',

weight: FontWeight.Medium,

style: FontStyle.Normal

}

 |

#### \[h2\]fontColor10+

fontColor(value: ResourceColor)

Sets the font color of all text within the menu.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | Yes | Font color of all text within the menu. |

#### \[h2\]radius10+

radius(value: Dimension | BorderRadiuses)

Sets the radius of the menu border corners.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [Dimension](../../common-definitions/basic-types/document.md#dimension10) | [BorderRadiuses](../../common-definitions/basic-types/document.md#borderradiuses9) | Yes | 
Radius of the menu border corners.

Default value: **8vp** for 2-in-1 devices and **20vp** for other devices

Since API version 12, if the sum of the two maximum corner radii in the horizontal direction exceeds the menu width, or if the sum of the two maximum corner radii in the vertical direction exceeds the menu height, the default corner radius will be used for all four corners of the menu.

When the Dimension type is used: Invalid input values will trigger a fallback to the default corner radius.

When the BorderRadiuses type is used: Invalid input values will result in the menu having no rounded corners by default.

 |

#### \[h2\]menuItemDivider12+

menuItemDivider(options: DividerStyleOptions | undefined)

Sets the style of the menu item divider. If this attribute is not set, the divider will not be displayed.

If the sum of **startMargin** and **endMargin** exceeds the component width, both **startMargin** and **endMargin** will be set to **0**.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [DividerStyleOptions](../../common-definitions/basic-types/document.md#dividerstyleoptions12) | undefined | Yes | 
Style of the menu item divider.

\- **strokeWidth**: stroke width of the divider.

\- **color**: color of the divider.

\- **startMargin**: distance between the divider and the start edge of the menu item.

\- **endMargin**: distance between the divider and the end edge of the menu item.

\- **mode**: mode of the divider, which is **FLOATING\_ABOVE\_MENU** by default.

 |

#### \[h2\]menuItemGroupDivider12+

menuItemGroupDivider(options: DividerStyleOptions | undefined)

Sets the style of the top and bottom dividers for the menu item group. If this attribute is not set, the dividers will be displayed by default.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [DividerStyleOptions](../../common-definitions/basic-types/document.md#dividerstyleoptions12) | undefined | Yes | 
Style of the top and bottom dividers for the menu item group.

\- **strokeWidth**: stroke width of the divider. The default value is 1 px.

\- **color**: color of the divider. The default value is **#33000000**.

\- **startMargin**: distance between the divider and the start edge of the menu item group. The default value is 16 vp.

\- **endMargin**: distance between the divider and the end edge of the menu item group. The default value is 16 vp.

\- **mode**: mode of the divider, which is **FLOATING\_ABOVE\_MENU** by default.

 |

#### \[h2\]subMenuExpandingMode12+

subMenuExpandingMode(mode: SubMenuExpandingMode)

Sets the submenu expanding mode of the menu.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| mode | [SubMenuExpandingMode](#submenuexpandingmode12) | Yes | 
Submenu expanding mode of the menu.

Default value: **SubMenuExpandingMode.SIDE\_EXPAND**

 |

#### \[h2\]subMenuExpandSymbol20+

subMenuExpandSymbol(symbol: SymbolGlyphModifier)

Sets the submenu expand symbol of the menu.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| symbol | [SymbolGlyphModifier](../../universal-attributes/modifiers-and-custom-property/symbol-glyph-modifier/document.md) | Yes | 
Submenu expand symbol of the menu.

1\. **SubMenuExpandingMode.SIDE\_EXPAND**: The expand symbol is not displayed.

2\. **SubMenuExpandingMode.EMBEDDED\_EXPAND**: The symbol rotates 180° clockwise upon expansion.

Default value: **$r('sys.symbol.chevron\_down').fontSize('24vp')**.

3\. **SubMenuExpandingMode.STACK\_EXPAND**: The symbol rotates 90° clockwise upon expansion.

Default value: **$r('sys.symbol.chevron\_forward').fontSize('20vp').padding('2vp')**.

 |

#### \[h2\]fontSize(deprecated)

fontSize(value: Length)

Sets the size of all text within the menu.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e/v3/xuW0-tqyQuKcUEwQfYbXmg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062246Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FDE5501CEC1BC2EB9439C247E2DFF51A926E23711CD5542D093243B2C4D1F470)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [font](#font10) instead.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [Length](../../common-definitions/basic-types/document.md#length) | Yes | Size of all text within the menu. If the value of the Length type is a number, the unit is fp. Percentage values are not supported. |

#### SubMenuExpandingMode12+

Enumerates the submenu expanding modes.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| SIDE\_EXPAND | 0 | Default mode. Submenus are expanded on the side on the same plane. |
| EMBEDDED\_EXPAND | 1 | Embedded mode. Submenus are expanded while embedded within the main menu. |
| STACK\_EXPAND | 2 | Stack mode. Submenus are expanded above the main menu. |

#### Example

## Example 1: Implementing a Multi-Level Menu

This example demonstrates how to implement a multi-level menu by configuring the **builder** parameter in **MenuItem**.

@Entry
@Component
struct Index {
  @State select: boolean = true;
  // Replace $r('app.media.xxx') with the image resource file you use.
  private iconStr: ResourceStr = $r("app.media.view\_list\_filled");
  private iconStr2: ResourceStr = $r("app.media.arrow\_right\_filled");

  @Builder
  SubMenu() {
    Menu() {
      MenuItem({ content: "Copy", labelInfo: "Ctrl+C" })
      MenuItem({ content: "Paste", labelInfo: "Ctrl+V" })
    }
  }

  @Builder
  MyMenu(){
    Menu() {
      MenuItem({ startIcon: $r("app.media.icon"), content: "Menu item" })
      MenuItem({ startIcon: $r("app.media.icon"), content: "Menu item" })
        .enabled(false)
      MenuItem({
        startIcon: this.iconStr,
        content: "Menu item",
        endIcon: this.iconStr2,
        builder: ():void=>this.SubMenu()
      })
      MenuItemGroup({ header: 'Subtitle' }) {
        MenuItem({
          startIcon: this.iconStr,
          content: "Menu item",
          endIcon: this.iconStr2,
          builder: ():void=>this.SubMenu()
        })
        MenuItem({
          startIcon: $r("app.media.app\_icon"),
          content: "Menu item",
          endIcon: this.iconStr2,
          builder: ():void=>this.SubMenu()
        })
      }
      MenuItem({
        startIcon: this.iconStr,
        content: "Menu item",
      })
    }
  }

  build() {
    Row() {
      Column() {
        Text('click to show menu')
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
      }
      .bindMenu(this.MyMenu)
      .width('100%')
    }
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/8MrFFO7pTcq10MIhRAslCA/en-us_image_0000002568685609.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062246Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E3BE35E76B4466333281FD6A3153BA97E0984195A98F52869496229D3901AB55)

## Example 2: Setting the Symbol Icon

This example demonstrates how to implement a menu with symbol icons by configuring **symbolStartIcon** and **symbolEndIcon**.

// xxx.ets
import { SymbolGlyphModifier } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State startIconModifier: SymbolGlyphModifier = new SymbolGlyphModifier($r('sys.symbol.ohos\_mic')).fontSize('24vp');
  @State endIconModifier: SymbolGlyphModifier = new SymbolGlyphModifier($r('sys.symbol.ohos\_trash')).fontSize('24vp');
  @State selectIconModifier: SymbolGlyphModifier =
    new SymbolGlyphModifier($r('sys.symbol.checkmark')).fontSize('24vp');
  @State select: boolean = true;

  @Builder
  SubMenu() {
    Menu() {
      MenuItem({ content: "Copy", labelInfo: "Ctrl+C" })
      MenuItem({ content: "Paste", labelInfo: "Ctrl+V" })
    }
  }

  @Builder
  MyMenu() {
    Menu() {
      MenuItem({ symbolStartIcon: this.startIconModifier, content: "Menu item" })
      MenuItem({ symbolStartIcon: this.startIconModifier, content: "Menu item" })
        .enabled(false)
      MenuItem({
        symbolStartIcon: this.startIconModifier,
        content: "Menu item",
        symbolEndIcon: this.endIconModifier,
        builder: (): void => this.SubMenu()
      })
      MenuItemGroup({ header: 'Subtitle' }) {
        MenuItem({
          symbolStartIcon: this.startIconModifier,
          content: "Menu item",
          symbolEndIcon: this.endIconModifier,
          builder: (): void => this.SubMenu()
        })
        MenuItem({
          symbolStartIcon: this.startIconModifier,
          content: "Menu item",
          symbolEndIcon: this.endIconModifier,
          builder: (): void => this.SubMenu()
        })
      }
      MenuItem({
        content: "Menu item",
      }).selected(this.select).selectIcon(this.selectIconModifier)
    }
  }

  build() {
    Row() {
      Column() {
        Text('click to show menu')
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
      }
      .bindMenu(this.MyMenu)
      .width('100%')
    }
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/RzTKRTrEQ4WdMvUfFJEaug/en-us_image_0000002568765619.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062246Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7A562C8674CD032EC4D30FA28A92C185439A3A9EF579B7F36895DD1AC13AB192)

## Example 3: Setting the Menu Submenu Expand Symbol

This example demonstrates how to configure the expand symbol color for menu submenus using **subMenuExpandSymbol**.

import { SymbolGlyphModifier } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State startIconModifier: SymbolGlyphModifier = new SymbolGlyphModifier($r('sys.symbol.ohos\_star'))
  @State endIconModifier: SymbolGlyphModifier = new SymbolGlyphModifier($r('sys.symbol.ohos\_mic'))
  @State expandSymbolModifier: SymbolGlyphModifier =
    new SymbolGlyphModifier($r('sys.symbol.chevron\_down')).fontColor(\[Color.Red\]).fontSize('24vp')

  @Builder
  SubMenu() {
    Menu() {
      MenuItem({
        symbolStartIcon: this.startIconModifier,
        content: "Icons"
      })
      MenuItem({
        symbolStartIcon: this.startIconModifier,
        content: "List"
      })
    }.backgroundColor(Color.Grey)
  }

  @Builder
  MyMenu() {
    Menu() {
      MenuItem({
        symbolStartIcon: this.startIconModifier,
        symbolEndIcon: this.endIconModifier,
        content: "New folder",
        builder: (): void => this.SubMenu(),
      })
      MenuItem({
        symbolStartIcon: this.startIconModifier,
        content: "Sort",
        builder: (): void => this.SubMenu(),
      })
      MenuItem({
        symbolStartIcon: this.startIconModifier,
        content: "View",
        builder: (): void => this.SubMenu(),
      })
    }
    .subMenuExpandingMode(SubMenuExpandingMode.EMBEDDED\_EXPAND)
    .backgroundColor(Color.Grey)
    .subMenuExpandSymbol(this.expandSymbolModifier)
  }

  build() {
    Button('click to show menu')
      .position({ top: 40, left: 40 })
      .bindMenu(this.MyMenu)
  }
}

## Example 4: Using the Divider Style

This example demonstrates how to implement the divider style using **menuItemGroupDivider**.

import { LengthMetrics } from '@kit.ArkUI'

@Entry
@Component
struct Index {

  @Builder
  MyMenu() {
    Menu() {
      MenuItem({ content: "Item Content" })
      MenuItem({ content: "Item Content" })
      MenuItem({ content: "Item Content" })
      MenuItemGroup() {
        MenuItem({ content: "Group Child" })
        MenuItem({ content: "Group Child" })
      }
      MenuItem({ content: "Item Content" })
    }
    .menuItemDivider({
      strokeWidth: LengthMetrics.vp(5),
      color: '#d5d5d5',
      mode: DividerMode.EMBEDDED\_IN\_MENU
    })
    .menuItemGroupDivider({
      strokeWidth: LengthMetrics.vp(5),
      color: '#707070',
      mode: DividerMode.EMBEDDED\_IN\_MENU
    })
  }

  build() {
    RelativeContainer() {
      Button("show menu")
        .bindMenu(this.MyMenu())
    }
    .height('100%')
    .width('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/iK7JmErqQqePInrR-eq0Ag/en-us_image_0000002537765894.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062246Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0C3B6DD69F0DD877956B6DF7DBF886D16EA9E3AE7363AB7826449DD84E89D57D)
