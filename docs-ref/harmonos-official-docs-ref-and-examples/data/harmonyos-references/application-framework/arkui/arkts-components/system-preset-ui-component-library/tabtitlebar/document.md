# TabTitleBar

The **TabTitleBar** component is a tab title bar used to switch between tabs pages. It is applicable only to level-1 pages.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/NP5rIxZCQkWSzrDE9EJMgQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062251Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C3C652810A60F32D6CD7E5373066C603BD7C2A22E06236CA09E8109B29A96BBF)

This component is supported since API version 10. Updates will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { TabTitleBar } from '@kit.ArkUI';

#### Child Components

Not supported

#### Attributes

The [universal attributes](../../universal-attributes/document.md) are not supported.

#### TabTitleBar

TabTitleBar({tabItems: Array<TabTitleBarTabItem>, menuItems?: Array<TabTitleBarMenuItem>, swiperContent: () => void})

**Decorator**: @Component

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Type | Mandatory | Decorator | Description |
| :-- | :-- | :-- | :-- | :-- |
| tabItems | Array<[TabTitleBarTabItem](#tabtitlebartabitem)\> | Yes | \- | List of tab items on the left of the title bar. |
| menuItems | Array<[TabTitleBarMenuItem](#tabtitlebarmenuitem)\> | No | \- | List of menu items on the right of the title bar. |
| swiperContent | () => void | Yes | @BuilderParam | Constructor for page content pertaining to the tab list. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/v9LonPNEQlW5ptuc7wUN_A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062251Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C643FA25CA99481A01DAAE6637CC8F00BA8DF4A1FF458F40DEDE6CA06F1D4384)

The input parameter cannot be **undefined**, that is, calling **TabTitleBar(undefined)** is not allowed.

#### TabTitleBarMenuItem

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| value | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | No | 
Icon resource.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| symbolStyle18+ | [SymbolGlyphModifier](../../universal-attributes/modifiers-and-custom-property/symbol-glyph-modifier/document.md#symbolglyphmodifier) | No | Yes | 

Symbol icon resource, which has higher priority than **value**.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| label13+ | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 

Icon label.

**Atomic service API**: This API can be used in atomic services since API version 13.

 |
| isEnabled | boolean | No | Yes | 

Whether to enable the item. Default value: **false**. The value **true** means to enable the item, and **false** means the opposite.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| action | () => void | No | Yes | 

Action to perform.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| accessibilityLevel18+ | string | No | Yes | 

Accessibility level. It determines whether the component can be recognized by accessibility services.

The options are as follows:

**"auto"**: It is treated as "yes" by the system.

**"yes"**: The component can be recognized by accessibility services.

**"no"**: The component cannot be recognized by accessibility services.

**"no-hide-descendants"**: Neither the component nor its child components can be recognized by accessibility services.

Default value: **"auto"**

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| accessibilityText18+ | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 

Accessibility text, that is, accessibility label name. If a component does not contain text information, it will not be announced by the screen reader when selected. In this case, the screen reader user cannot know which component is selected. To solve this problem, you can set accessibility text for components without text information. When such a component is selected, the screen reader announces the specified accessibility text, informing the user which component is selected.

Default value: value of the **label** property if it is set and an empty string otherwise.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| accessibilityDescription18+ | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 

Accessible description. You can provide comprehensive text explanations to help users understand the operation they are about to perform and its potential consequences, especially when these cannot be inferred from the component's attributes and accessibility text alone. If a component contains both text information and the accessible description, the text is announced first and then the accessible description, when the component is selected.

Default value: **"Double-tap to activate"**

**Atomic service API**: This API can be used in atomic services since API version 18.

 |

#### TabTitleBarTabItem

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| title | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | No | 
Text of the tab.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| icon | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 

Icon of the tab.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| symbolStyle18+ | [SymbolGlyphModifier](../../universal-attributes/modifiers-and-custom-property/symbol-glyph-modifier/document.md#symbolglyphmodifier) | No | Yes | 

Symbol icon of the tab, which has higher priority than **icon**.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |

#### Events

The [universal events](../../universal-events/document.md) are not supported.

#### Example

## Example 1: Implementing a Simple Tab Title Bar

This example demonstrates a tab title bar with tabs on the left and a menu list on the right.

import { TabTitleBar, Prompt, TabTitleBarTabItem, TabTitleBarMenuItem } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @Builder
  // Define the pages associated with the tab list.
  componentBuilder() {
    Text("#1ABC9C\\nTURQUOISE")
      .fontWeight(FontWeight.Bold)
      .fontSize(14)
      .width("100%")
      .textAlign(TextAlign.Center)
      .fontColor("#CCFFFFFF")
      .backgroundColor("#1ABC9C")
    Text("#16A085\\nGREEN SEA")
      .fontWeight(FontWeight.Bold)
      .fontSize(14)
      .width("100%")
      .textAlign(TextAlign.Center)
      .fontColor("#CCFFFFFF")
      .backgroundColor("#16A085")
    Text("#2ECC71\\nEMERALD")
      .fontWeight(FontWeight.Bold)
      .fontSize(14)
      .width("100%")
      .textAlign(TextAlign.Center)
      .fontColor("#CCFFFFFF")
      .backgroundColor("#2ECC71")
    Text("#27AE60\\nNEPHRITIS")
      .fontWeight(FontWeight.Bold)
      .fontSize(14)
      .width("100%")
      .textAlign(TextAlign.Center)
      .fontColor("#CCFFFFFF")
      .backgroundColor("#27AE60")
    Text("#3498DB\\nPETER RIVER")
      .fontWeight(FontWeight.Bold)
      .fontSize(14)
      .width("100%")
      .textAlign(TextAlign.Center)
      .fontColor("#CCFFFFFF")
      .backgroundColor("#3498DB")
  }

  // Define several tab items on the left.
  private readonly tabItems: Array<TabTitleBarTabItem> =
    \[
      { title: 'Tab 1' },
      { title: 'Tab 2' },
      { title: 'Tab 3' },
      { title: 'icon', icon: $r('sys.media.ohos\_app\_icon') },
      { title: 'Tab 4' },
    \]
  // Define several menu items on the right.
  private readonly menuItems: Array<TabTitleBarMenuItem> = \[
    {
      value: $r('sys.media.ohos\_save\_button\_filled'),
      isEnabled: true,
      action: () => Prompt.showToast({ message: "on item click! index 0" })
    },
    {
      value: $r('sys.media.ohos\_ic\_public\_copy'),
      isEnabled: true,
      action: () => Prompt.showToast({ message: "on item click! index 1" })
    },
    {
      value: $r('sys.media.ohos\_ic\_public\_edit'),
      isEnabled: true,
      action: () => Prompt.showToast({ message: "on item click! index 2" })
    },
  \]

  // Display the tab title bar.
  build() {
    Row() {
      Column() {
        TabTitleBar({
          swiperContent: this.componentBuilder,
          tabItems: this.tabItems,
          menuItems: this.menuItems,
        })
      }.width('100%')
    }.height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/iwYIHi0-RSGCXKc7W-fZeQ/en-us_image_0000002568685715.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062251Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A87BB07457318349BDE9211C9A2B801ADA100B24D8A1E0E4A417D64A714B1E2A)

## Example 2: Implementing Announcement for the Custom Button on the Right Side

This example customizes the screen reader announcement text by setting the **accessibilityText**, **accessibilityDescription**, and **accessibilityLevel** properties of the custom button on the right side of the title bar. This functionality is supported since API version 18.

import { TabTitleBar, Prompt, TabTitleBarTabItem, TabTitleBarMenuItem } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @Builder
  // Define the pages associated with the tab list.
  componentBuilder() {
    Text("#1ABC9C\\nTURQUOISE")
      .fontWeight(FontWeight.Bold)
      .fontSize(14)
      .width("100%")
      .textAlign(TextAlign.Center)
      .fontColor("#CCFFFFFF")
      .backgroundColor("#1ABC9C")
    Text("#16A085\\nGREEN SEA")
      .fontWeight(FontWeight.Bold)
      .fontSize(14)
      .width("100%")
      .textAlign(TextAlign.Center)
      .fontColor("#CCFFFFFF")
      .backgroundColor("#16A085")
    Text("#2ECC71\\nEMERALD")
      .fontWeight(FontWeight.Bold)
      .fontSize(14)
      .width("100%")
      .textAlign(TextAlign.Center)
      .fontColor("#CCFFFFFF")
      .backgroundColor("#2ECC71")
    Text("#27AE60\\nNEPHRITIS")
      .fontWeight(FontWeight.Bold)
      .fontSize(14)
      .width("100%")
      .textAlign(TextAlign.Center)
      .fontColor("#CCFFFFFF")
      .backgroundColor("#27AE60")
    Text("#3498DB\\nPETER RIVER")
      .fontWeight(FontWeight.Bold)
      .fontSize(14)
      .width("100%")
      .textAlign(TextAlign.Center)
      .fontColor("#CCFFFFFF")
      .backgroundColor("#3498DB")
  }

  // Define several tab items on the left.
  private readonly tabItems: Array<TabTitleBarTabItem> =
    \[
      { title: 'Tab 1' },
      { title: 'Tab 2' },
      { title: 'Tab 3' },
      { title: 'icon', icon: $r('sys.media.ohos\_app\_icon') },
      { title: 'Tab 4' },
    \]
  // Define several menu items on the right.
  private readonly menuItems: Array<TabTitleBarMenuItem> = \[
    {
      value: $r('sys.media.ohos\_save\_button\_filled'),
      isEnabled: true,
      action: () => Prompt.showToast({ message: "on item click! index 0" }),
      accessibilityText: 'Save',
      // The screen reader will not focus on this item.
      accessibilityLevel: 'no',
      accessibilityDescription: 'Tap to save the icon'
    },
    {
      value: $r('sys.media.ohos\_ic\_public\_copy'),
      isEnabled: true,
      action: () => Prompt.showToast({ message: "on item click! index 1" }),
      accessibilityText: 'Copy',
      accessibilityLevel: 'yes',
      accessibilityDescription: 'Tap to copy the icon'
    },
    {
      value: $r('sys.media.ohos\_ic\_public\_edit'),
      isEnabled: true,
      action: () => Prompt.showToast({ message: "on item click! index 2" }),
      // The screen reader will prioritize this text over the label.
      accessibilityText: 'Edit',
      // The screen reader can focus on this item.
      accessibilityLevel: 'yes',
      // The screen reader will ultimately announce this text.
      accessibilityDescription: 'Tap to edit the icon'
    },
  \]

  // Display the tab title bar.
  build() {
    Row() {
      Column() {
        TabTitleBar({
          swiperContent: this.componentBuilder,
          tabItems: this.tabItems,
          menuItems: this.menuItems,
        })
      }.width('100%')
    }.height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/UhVmm55ASce9f4C87vrJvw/en-us_image_0000002568765725.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062251Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=72D5D0C4172C378A647D23D5159F30E5A812BDF7F716F380D90BD67B952F1AE5)

## Example 3: Setting the Symbol Icon

This example demonstrates how to use **symbolStyle** in **TabTitleBarTabItem** and **TabTitleBarMenuItem** to set custom symbol icons. This functionality is supported since API version 18.

import { TabTitleBar, Prompt, TabTitleBarTabItem, TabTitleBarMenuItem, SymbolGlyphModifier } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @Builder
  // Define the pages associated with the tab list.
  componentBuilder() {
    Text("#1ABC9C\\nTURQUOISE")
      .fontWeight(FontWeight.Bold)
      .fontSize(14)
      .width("100%")
      .textAlign(TextAlign.Center)
      .fontColor("#CCFFFFFF")
      .backgroundColor("#1ABC9C")
    Text("#16A085\\nGREEN SEA")
      .fontWeight(FontWeight.Bold)
      .fontSize(14)
      .width("100%")
      .textAlign(TextAlign.Center)
      .fontColor("#CCFFFFFF")
      .backgroundColor("#16A085")
    Text("#2ECC71\\nEMERALD")
      .fontWeight(FontWeight.Bold)
      .fontSize(14)
      .width("100%")
      .textAlign(TextAlign.Center)
      .fontColor("#CCFFFFFF")
      .backgroundColor("#2ECC71")
    Text("#27AE60\\nNEPHRITIS")
      .fontWeight(FontWeight.Bold)
      .fontSize(14)
      .width("100%")
      .textAlign(TextAlign.Center)
      .fontColor("#CCFFFFFF")
      .backgroundColor("#27AE60")
    Text("#3498DB\\nPETER RIVER")
      .fontWeight(FontWeight.Bold)
      .fontSize(14)
      .width("100%")
      .textAlign(TextAlign.Center)
      .fontColor("#CCFFFFFF")
      .backgroundColor("#3498DB")
  }

  // Define several tab items on the left.
  private readonly tabItems: Array<TabTitleBarTabItem> =
    \[
      { title: 'Tab 1' },
      { title: 'Tab 2' },
      { title: 'Tab 3' },
      {
        title: 'icon',
        icon: $r('sys.media.ohos\_app\_icon'),
        symbolStyle: new SymbolGlyphModifier($r('sys.symbol.car'))
      },
      { title: 'Tab 4' },
    \]
  // Define several menu items on the right.
  private readonly menuItems: Array<TabTitleBarMenuItem> = \[
    {
      value: $r('sys.media.ohos\_save\_button\_filled'),
      symbolStyle: new SymbolGlyphModifier($r('sys.symbol.save')),
      isEnabled: true,
      action: () => Prompt.showToast({ message: "on item click! index 0" }),
      accessibilityText: 'Save',
      // The screen reader will not focus on this item.
      accessibilityLevel: 'no',
      accessibilityDescription: 'Tap to save the icon'
    },
    {
      value: $r('sys.media.ohos\_ic\_public\_copy'),
      symbolStyle: new SymbolGlyphModifier($r('sys.symbol.car')),
      isEnabled: true,
      action: () => Prompt.showToast({ message: "on item click! index 1" }),
      accessibilityText: 'Copy',
      accessibilityLevel: 'yes',
      accessibilityDescription: 'Tap to copy the icon'
    },
    {
      value: $r('sys.media.ohos\_ic\_public\_edit'),
      symbolStyle: new SymbolGlyphModifier($r('sys.symbol.ai\_edit')),
      isEnabled: true,
      action: () => Prompt.showToast({ message: "on item click! index 2" }),
      // The screen reader will prioritize this text over the label.
      accessibilityText: 'Edit',
      // The screen reader can focus on this item.
      accessibilityLevel: 'yes',
      // The screen reader will ultimately announce this text.
      accessibilityDescription: 'Tap to edit the icon'
    },
  \]

  // Display the tab title bar.
  build() {
    Row() {
      Column() {
        TabTitleBar({
          swiperContent: this.componentBuilder,
          tabItems: this.tabItems,
          menuItems: this.menuItems,
        })
      }.width('100%')
    }.height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/LpnbchYPTOe7zFsonnBPtQ/en-us_image_0000002537766000.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062251Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=217D4B318B18A17F2B5C56A4688C6254070F48417F8F9D161C25816EF089336B)
