# HdsSideMenu

This module allows menu bar style configuration for you to set a two-level menu for the sidebar and display the number of new messages for each menu item.

**Start version**: 6.0.0(20)

#### Modules to Import

import { HdsSideMenu, HdsSideMenuMainItem, HdsSideMenuSubItem, HdsSideMenuBadgeParam} from '@kit.UIDesignKit';

#### API

HdsSideMenu({items?: HdsSideMenuMainItem\[\], selectedIndex: number, $selectedIndex?: OnSelectedIndexChange, maxItemTextLines?: number})

Defines the sidebar menu component information.

**Decorator type**: @ComponentV2

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.UIDesign.HDSPattern.Standard

**Start version**: 6.0.0(20)

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Decorator Type

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

items

 | 

[HdsSideMenuMainItem](#section1050510599502)\[\]

 | 

No

 | 

@Param

 | 

Array of level-1 menu items. Up to five items are supported.

 |
| 

selectedIndex

 | 

number

 | 

Yes

 | 

@Param

@Require

 | 

Menu item that is selected.

The value must be an integer greater than or equal to **\-1**.

The value **\-1** indicates that no menu item is currently selected from the side menu.

 |
| 

$selectedIndex

 | 

[OnSelectedIndexChange](#section58771018173714)

 | 

No

 | 

@Event

 | 

Binds **selectedIndex** bidirectionally.

 |
| 

maxItemTextLines

 | 

number

 | 

No

 | 

@Param

 | 

Maximum number of text lines of a menu item.

The default value is **1**.

The value is an integer in the range (0, +∞).

 |

#### build

build(): void

Default constructor of a struct. This method cannot be directly called.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.UIDesign.HDSPattern.Standard

**Start version**: 6.0.0(20)

#### HdsSideMenuMainItem

Defines the level-1 menu of the **HdsSideMenu** component.

**Decorator type**: @ObservedV2

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.UIDesign.HDSPattern.Standard

**Start version**: 6.0.0(20)

#### \[h2\]constructor

constructor(param: HdsSideMenuMainItemParam)

Constructor for **HdsSideMenuMainItem**.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.UIDesign.HDSPattern.Standard

**Start version**: 6.0.0(20)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

param

 | 

[HdsSideMenuMainItemParam](#section292095817402)

 | 

Yes

 | 

Level-1 menu parameters of the **HdsSideMenu** component.

 |

#### \[h2\]getSideMenuSubItem

getSideMenuSubItem(): HdsSideMenuSubItem\[\]

Obtains the array of level-2 menu item objects under the currently selected level-1 menu item from the level-1 menu item object.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.UIDesign.HDSPattern.Standard

**Start version**: 6.0.0(20)

**Returns:**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[HdsSideMenuSubItem](#section144191823155313)\[\]

 | 

Array of level-2 menu item objects under the currently selected level-1 menu item.

 |

#### \[h2\]updateBadge

updateBadge(badge?: HdsSideMenuBadgeParam): HdsSideMenuMainItem

Updates the badge icon attribute for a level-1 menu item.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.UIDesign.HDSPattern.Standard

**Start version**: 6.0.0(20)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

badge

 | 

[HdsSideMenuBadgeParam](#section10384044394)

 | 

No

 | 

Menu icon settings of the **HdsSideMenu** component, including the reminder badge.

 |

**Returns:**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[HdsSideMenuMainItem](#section1050510599502)

 | 

Level-1 menu object under the current menu.

 |

#### HdsSideMenuSubItem

Defines the level-2 menu of the **HdsSideMenu** component.

**Decorator type**: @ObservedV2

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.UIDesign.HDSPattern.Standard

**Start version**: 6.0.0(20)

#### \[h2\]constructor

constructor(param: HdsSideMenuSubItemParam)

Constructor for **HdsSideMenuSubItem**.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.UIDesign.HDSPattern.Standard

**Start version**: 6.0.0(20)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

param

 | 

[HdsSideMenuSubItemParam](#section730054414319)

 | 

Yes

 | 

Level-2 menu parameters of the **HdsSideMenu** component.

 |

#### \[h2\]updateBadge

updateBadge(badge?: HdsSideMenuBadgeParam): HdsSideMenuSubItem

Updates the badge icon attribute for a level-2 menu item.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.UIDesign.HDSPattern.Standard

**Start version**: 6.0.0(20)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

badge

 | 

[HdsSideMenuBadgeParam](#section10384044394)

 | 

No

 | 

Menu icon settings of the **HdsSideMenu** component, including the reminder badge.

 |

**Returns:**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[HdsSideMenuSubItem](#section144191823155313)

 | 

Level-2 menu object under the currently selected level-1 menu item.

 |

#### HdsSideMenuBadgeParam

Menu icon settings of the **HdsSideMenu** component, including the reminder badge.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.UIDesign.HDSPattern.Standard

**Start version**: 6.0.0(20)

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

count

 | 

number

 | 

No

 | 

Yes

 | 

Message count displayed on the message reminder badge. If the value is 0, no badge is displayed. If the value is **1**, a dot (·) is displayed. If the value is greater than 99, **99+** is displayed. This parameter cannot be set to a negative value.

The default value is **0**.

 |
| 

value

 | 

string

 | 

No

 | 

Yes

 | 

Text message. A long text will be displayed in multiple lines.

Default value: **""**

 |

#### HdsSideMenuBaseItemParam

Provides the basic class for the **HdsSideMenu** component.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.UIDesign.HDSPattern.Standard

**Start version**: 6.0.0(20)

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

itemId

 | 

string

 | 

No

 | 

Yes

 | 

Menu item ID.

Default value: **""**

 |
| 

label

 | 

[ResourceStr](../../../arkui/arkts-components/common-definitions/basic-types/document.md#resourcestr)

 | 

No

 | 

Yes

 | 

Text displayed for a menu item.

 |
| 

action

 | 

[Callback](../../../arkui/arkts-components/common-definitions/basic-types/document.md#callback12)<void>

 | 

No

 | 

Yes

 | 

Triggered when a menu item is tapped.

 |

#### HdsSideMenuMainItemParam

Inherits from [HdsSideMenuBaseItemParam](#section131215146362) and defines level-1 menu parameters of the **HdsSideMenu** component.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.UIDesign.HDSPattern.Standard

**Start version**: 6.0.0(20)

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

icon

 | 

[ResourceStr](../../../arkui/arkts-components/common-definitions/basic-types/document.md#resourcestr)

 | 

No

 | 

Yes

 | 

Icon of a level-1 menu item. This parameter takes precedence over **symbol**.

 |
| 

symbol

 | 

[SymbolGlyphModifier](../../../arkui/arkts-components/universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#custom-modifier)

 | 

No

 | 

Yes

 | 

Level-1 menu item icon.

 |
| 

hdsSideMenuSubItem

 | 

[HdsSideMenuSubItem](#section144191823155313)\[\]

 | 

No

 | 

Yes

 | 

Array of the level-2 menu items under the level-1 menu item. Up to five level-2 menu items are supported.

 |
| 

badge

 | 

[HdsSideMenuBadgeParam](#section10384044394)

 | 

No

 | 

Yes

 | 

Reminder badge information for menu items under a level-1 menu item.

 |

#### HdsSideMenuSubItemParam

Inherits from [HdsSideMenuBaseItemParam](#section131215146362) and defines level-2 menu parameters of the **HdsSideMenu** component.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.UIDesign.HDSPattern.Standard

**Start version**: 6.0.0(20)

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

badge

 | 

[HdsSideMenuBadgeParam](#section10384044394)

 | 

No

 | 

Yes

 | 

Reminder badge information for level-2 menu items.

 |

#### Events

#### OnSelectedIndexChange

type OnSelectedIndexChange = (selectedIndex: number) => void

Triggered when **selectedIndex** of **HdsSideMenu** changes.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.UIDesign.HDSPattern.Standard

**Start version**: 6.0.0(20)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

selectedIndex

 | 

number

 | 

Yes

 | 

Sequence number of the selected menu item.

 |

#### Example

The following is a menu bar style configuration example of the **HdsSideMenu** component:

import { HdsSideMenu, HdsSideMenuMainItem,  HdsSideBar } from '@kit.UIDesignKit';
import { SymbolGlyphModifier } from '@kit.ArkUI';

@Entry
@ComponentV2
struct Index {
  @Local isShowSidebar: boolean = true;
  @Local selectedIndex: number = 1;
  listOptionsDefault?: HdsSideMenuMainItem\[\] = \[
    new HdsSideMenuMainItem({
      symbol: new SymbolGlyphModifier($r('sys.symbol.doc\_plaintext')),
      label: 'All notes',
    }),
    new HdsSideMenuMainItem({
      symbol: new SymbolGlyphModifier($r('sys.symbol.star')),
      label: 'Favorites',
    }),
    new HdsSideMenuMainItem({
      symbol: new SymbolGlyphModifier($r('sys.symbol.lock')),
      label: 'Locked',
    }),
    new HdsSideMenuMainItem({
      symbol: new SymbolGlyphModifier($r('sys.symbol.trash')),
      label: 'Recently deleted',
    }),
    new HdsSideMenuMainItem({
      label: 'Folders',
    }),
  \]

  @Builder
  SideBarPanelBuilder() {
    Column() {
      HdsSideMenu({
        items: this.listOptionsDefault,
        selectedIndex: this.selectedIndex,
        $selectedIndex: (selectedIndex: number) => {
          this.selectedIndex = selectedIndex;
        },
      })
    }
    .width('100%')
    .height('100%')
    .margin(40)
  }

  @Builder
  ContentPanelBuilder() {
    Column() {
      Image($r('sys.media.ohos\_ic\_public\_albums'))
        .width('120vp')
        .height('120vp')
    }
    .margin({ top: 250 })
  }

  @BuilderParam contentBuilder: () => void = this.ContentPanelBuilder
  @BuilderParam sideBarBuilder: () => void = this.SideBarPanelBuilder

  @Builder
  build() {
    Stack({ alignContent: Alignment.TopStart }) {
      Button() {
        SymbolGlyph(this.isShowSidebar ? $r('sys.symbol.open\_sidebar') : $r('sys.symbol.close\_sidebar'))
          .fontWeight(FontWeight.Normal)
          .fontSize($r('sys.float.ohos\_id\_text\_size\_headline7'))
          .fontColor(\[$r('sys.color.ohos\_id\_color\_titlebar\_icon')\])
          .hitTestBehavior(HitTestMode.None)
      }
      .id('side\_bar\_button')
      .backgroundColor($r('sys.color.ohos\_id\_color\_button\_normal'))
      .height(30)
      .width(30)
      .onClick(() => {
        this.isShowSidebar = !this.isShowSidebar;
      })
      .zIndex(1)
      .margin({ top: 10, left: 10 })

      HdsSideBar({
        sideBarPanelBuilder: (): void => {
          this.sideBarBuilder()
        },
        contentPanelBuilder: (): void => {
          this.contentBuilder()
        },
        isShowSideBar: this.isShowSidebar,
        $isShowSideBar: (isShowSidebar: boolean) => {
          this.isShowSidebar = !isShowSidebar
        },
      })
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/oKQ53KLOQWmBREKNYwfUAQ/en-us_image_0000002500424072.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062328Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D0A5E6FCA3F1E6F4D9038F344DBD6C03420C865D48A65A9CDAC8E2184CBCEC19)
