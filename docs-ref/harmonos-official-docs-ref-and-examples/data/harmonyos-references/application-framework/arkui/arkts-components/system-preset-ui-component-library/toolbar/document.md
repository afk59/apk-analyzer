# ToolBar

The **Toolbar** component is designed to present a set of action options related to the current screen, displayed at the bottom of the screen. It can display up to five child components. If there are six or more child components, the first four are shown directly, and the additional ones are grouped under a **More** item on the rightmost side of the toolbar.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0b/v3/er3diAiFSL2NY_Xbgm6dbA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062251Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=86E91CE1FE6E8F92902786FF66D4F26A9549FABAD7A67BC4F94F30F3E09D53FD)

This component is supported since API version 10. Updates will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { SymbolGlyphModifier, DividerModifier, ToolBar, ToolBarOptions, ToolBarModifier, ItemState, LengthMetrics } from '@kit.ArkUI';

#### Child Components

Not supported

#### Attributes

The [universal attributes](../../universal-attributes/document.md) are not supported.

#### ToolBar

Toolbar({toolBarList: ToolBarOptions, activateIndex?: number, controller: TabsController, dividerModifier?: DividerModifier, toolBarModifier?: ToolBarModifier})

The **Toolbar** component is designed to present a set of action options related to the current screen, displayed at the bottom of the screen. It can display up to five child components. If there are six or more child components, the first four are shown directly, and the additional ones are grouped under a **More** item on the rightmost side of the toolbar.

**Decorator**: @Component

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Type | Mandatory | Decorator | Description |
| :-- | :-- | :-- | :-- | :-- |
| toolBarList | [ToolBarOptions](#toolbaroptions) | Yes | @ObjectLink | 
Toolbar list.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| activateIndex | number | No | @Prop | 

Index of the active item.

The value must be greater than or equal to -1.

The default value is **\-1**, indicating that there is no active item. Values less than -1 are treated as no active item.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| controller | [TabsController](../../navigation-and-switching/tabs/document.md#tabscontroller) | Yes | \- | 

Toolbar controller, which cannot be used for controlling individual toolbar items.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| dividerModifier13+ | [DividerModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#custom-modifier) | No | @Prop | 

Modifier for the toolbar header divider, which can be used to customize the divider's height, color, and other attributes.

Default value: system default value

**Atomic service API**: This API can be used in atomic services since API version 13.

 |
| toolBarModifier13+ | [ToolBarModifier](#toolbarmodifier13) | No | @Prop | 

Modifier for the toolbar, which can be used to set the toolbar's height, background color, padding (which only takes effect when there are fewer than five toolbar items), and whether to display the pressed state.

Default value:

Height of the toolbar: **56vp**

Background color: **ohos\_id\_toolbar\_bg**

Padding: **24vp**

Whether to display the pressed state: yes

**Atomic service API**: This API can be used in atomic services since API version 13.

 |

#### ToolBarOptions

Inherits Array<[ToolBarOption](#toolbaroption)\>.

**Decorator Type**: @Observed

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

#### ToolBarOption

Defines the content and attributes of a toolbar.

**Decorator Type**: @Observed

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| content | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | No | 
Text of the toolbar item.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| action | () => void | No | Yes | 

Click event of the toolbar item.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| icon | [Resource](../../common-definitions/basic-types/document.md#resource) | No | Yes | 

Icon of the toolbar item.

If this parameter is not set or is set to **undefined**, the icon is not displayed.

If **toolBarSymbolOptions** has input parameters, **icon** is ineffective.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| state | [ItemState](#itemstate) | No | Yes | 

State of the toolbar item.

Default value: **ItemState.ENABLE**

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| iconColor13+ | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | No | Yes | 

Icon fill color of the toolbar item.

Default value: **$r('sys.color.icon\_primary')**

**Atomic service API**: This API can be used in atomic services since API version 13.

 |
| activatedIconColor13+ | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | No | Yes | 

Icon fill color of the toolbar option in the activated state.

Default value: **$r('sys.color.icon\_emphasize')**

**Atomic service API**: This API can be used in atomic services since API version 13.

 |
| textColor13+ | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | No | Yes | 

Font color of the toolbar item.

Default value: **$r('sys.color.font\_primary')**

**Atomic service API**: This API can be used in atomic services since API version 13.

 |
| activatedTextColor13+ | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | No | Yes | 

Font color of the toolbar item in the activated state.

Default value: **$r('sys.color.font\_emphasize')**

**Atomic service API**: This API can be used in atomic services since API version 13.

 |
| toolBarSymbolOptions13+ | [ToolBarSymbolGlyphOptions](#toolbarsymbolglyphoptions13) | No | Yes | 

Icon symbol options of the toolbar item.

**Atomic service API**: This API can be used in atomic services since API version 13.

 |
| accessibilityText18+ | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 

Accessibility text, that is, accessible label name, of the toolbar item. If a component does not contain text information, it will not be announced by the screen reader when selected. In this case, the screen reader user cannot know which component is selected. To solve this problem, you can set accessibility text for components without text information. When such a component is selected, the screen reader announces the specified accessibility text, informing the user which component is selected.

Default value: value of **content**

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| accessibilityDescription18+ | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 

Accessible description of the toolbar item. You can provide comprehensive text explanations to help users understand the operation they are about to perform and its potential consequences, especially when these cannot be inferred from the component's attributes and accessibility text alone. If a component contains both text information and the accessible description, the text is announced first and then the accessible description, when the component is selected.

Default value: **"Double-tap to activate"**

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| accessibilityLevel18+ | string | No | Yes | 

Accessibility level of the toolbar item. It determines whether the component can be recognized by accessibility services.

The options are as follows:

**"auto"**: This option is treated as "yes" by the system for this component.

**"yes"**: The component can be recognized by accessibility services.

**"no"**: The component cannot be recognized by accessibility services.

**"no-hide-descendants"**: Neither the component nor its child components can be recognized by accessibility services.

Default value: **"auto"**

**Atomic service API**: This API can be used in atomic services since API version 18.

 |

#### ToolBarModifier13+

Provides APIs for setting the height (**height**), background color (**backgroundColor**), left and right padding (**padding**, which only takes effect when there are fewer than five items) of the toolbar, and whether to display the pressed state effect (**stateEffect**).

**Atomic service API**: This API can be used in atomic services since API version 13.

#### \[h2\]backgroundColor13+

backgroundColor(backgroundColor: ResourceColor): ToolBarModifier

Sets the background color of the toolbar. By overriding this API, you can implement custom drawing for the background color of the toolbar.

**Atomic service API**: This API can be used in atomic services since API version 13.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| backgroundColor | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | Yes | 
Toolbar background color

Default value: **$r('sys.color.ohos\_id\_color\_toolbar\_bg')**

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [ToolBarModifier](#toolbarmodifier13) | **ToolBarModifier** object after the background color is set. |

#### \[h2\]padding13+

padding(padding: LengthMetrics): ToolBarModifier

Sets the left and right padding of the toolbar. By overriding this API, you can implement custom drawing for the left and right padding of the toolbar.

**Atomic service API**: This API can be used in atomic services since API version 13.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| padding | [LengthMetrics](../../../arkts-api/ui/arkui/graphics/document.md#lengthmetrics12) | Yes | 
Left and right padding of the toolbar, which is effective only when there are fewer than five items.

By default, the padding is 24 vp when there are fewer than five items and 0 when there are five or more items.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [ToolBarModifier](#toolbarmodifier13) | **ToolBarModifier** object after the padding is set. |

#### \[h2\]height13+

height(height: LengthMetrics): ToolBarModifier

Sets the height of the toolbar. By overriding this API, you can implement custom drawing for the height of the toolbar, which does not include the height of the divider.

**Atomic service API**: This API can be used in atomic services since API version 13.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| height | [LengthMetrics](../../../arkts-api/ui/arkui/graphics/document.md#lengthmetrics12) | Yes | 
Height of the toolbar.

The default height of the toolbar is 56 vp, which does not include the divider.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [ToolBarModifier](#toolbarmodifier13) | **ToolBarModifier** object after the height is set. |

#### \[h2\]stateEffect13+

stateEffect(stateEffect: boolean): ToolBarModifier

Sets whether to display the pressed state effect.

**Atomic service API**: This API can be used in atomic services since API version 13.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| stateEffect | boolean | Yes | 
Whether to display the pressed state effect on the toolbar.

The value **true** means to display the pressed state effect on the toolbar, and **false** means the opposite.

Default value: **true**

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [ToolBarModifier](#toolbarmodifier13) | **ToolBarModifier** object after the pressed state effect is set. |

#### ItemState

Enumerates toolbar item states.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Value | Description |
| :-- | :-- | :-- |
| ENABLE | 1 | The toolbar item is enabled. |
| DISABLE | 2 | The toolbar item is disabled. |
| ACTIVATE | 3 | The toolbar item is activated. |

#### ToolBarSymbolGlyphOptions13+

Defines the icon symbol options.

**Atomic service API**: This API can be used in atomic services since API version 13.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| normal | [SymbolGlyphModifier](../../universal-attributes/modifiers-and-custom-property/symbol-glyph-modifier/document.md#symbolglyphmodifier) | No | Yes | 
Icon symbol of the toolbar item in normal state.

Default value: **fontColor: $r('sys.color.icon\_primary'), fontSize: 24vp**

 |
| activated | [SymbolGlyphModifier](../../universal-attributes/modifiers-and-custom-property/symbol-glyph-modifier/document.md#symbolglyphmodifier) | No | Yes | 

Icon symbol of the toolbar item in activated state.

Default value: **fontColor: $r('sys.color.icon\_emphasize'), fontSize: 24vp**

 |

#### Events

The [universal events](../../universal-events/document.md) are not supported.

#### Example

## Example 1: Setting Toolbar Items to Different States

This example shows the various display effects when the **state** property of toolbar items is set to **ENABLE**, **DISABLE**, or **ACTIVATE**.

import { ToolBar, ToolBarOptions, ItemState } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State toolbarList: ToolBarOptions = new ToolBarOptions();

  aboutToAppear() {
    this.toolbarList.push({
      content: 'Cut Super Long Text',
      icon: $r('sys.media.ohos\_ic\_public\_share'),
      action: () => {
      },
    })
    this.toolbarList.push({
      content: 'Copy',
      icon: $r('sys.media.ohos\_ic\_public\_copy'),
      action: () => {
      },
      state: ItemState.DISABLE
    })
    this.toolbarList.push({
      content: 'Paste',
      icon: $r('sys.media.ohos\_ic\_public\_paste'),
      action: () => {
      },
      state: ItemState.ACTIVATE
    })
    this.toolbarList.push({
      content: 'Select all',
      icon: $r('sys.media.ohos\_ic\_public\_select\_all'),
      action: () => {
      },
    })
    this.toolbarList.push({
      content: 'Share',
      icon: $r('sys.media.ohos\_ic\_public\_share'),
      action: () => {
      },
    })
    this.toolbarList.push({
      content: 'Share',
      icon: $r('sys.media.ohos\_ic\_public\_share'),
      action: () => {
      },
    })
  }

  build() {
    Row() {
      Stack() {
        Column() {
          ToolBar({
            activateIndex: 2,
            toolBarList: this.toolbarList,
          })
        }
      }
      .align(Alignment.Bottom)
      .width('100%')
      .height('100%')
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/bZRNdjFUTqWP_U8I6o9UYg/en-us_image_0000002537925940.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062251Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C78FE4CFB7DAA3ABF02C7FC1ADB1CE889C01E5F350ACD8D5A3531D518D6B43F0)

## Example 2: Customizing the Toolbar Style

This example demonstrates how to customize the toolbar's height, background color, and other styles using **ToolBarModifier**. This functionality is supported since API version 13.

import {
  SymbolGlyphModifier,
  DividerModifier,
  ToolBar,
  ToolBarOptions,
  ToolBarModifier,
  ItemState,
  LengthMetrics,
} from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State toolbarList: ToolBarOptions = new ToolBarOptions();
  // Custom toolbar style
  private toolBarModifier: ToolBarModifier =
    new ToolBarModifier().height(LengthMetrics.vp(52)).backgroundColor(Color.Transparent).stateEffect(false);
  @State dividerModifier: DividerModifier = new DividerModifier().height(0);

  aboutToAppear() {
    // Add toolbar items.
    this.toolbarList.push({
      content: 'Long long long long long long long long text',
      icon: $r('sys.media.ohos\_ic\_public\_share'),
      action: () => {
      },
      state: ItemState.ACTIVATE,
      toolBarSymbolOptions: {
        normal: new SymbolGlyphModifier($r('sys.symbol.ohos\_star')).fontColor(\[Color.Green\]), // Symbol icon in the normal state.
        activated: new SymbolGlyphModifier($r('sys.symbol.ohos\_star')).fontColor(\[Color.Red\]), // Symbol icon in the activated state.
      },
      activatedTextColor: $r('sys.color.font\_primary'),
    })
    this.toolbarList.push({
      content: 'Copy',
      icon: $r('sys.media.ohos\_ic\_public\_copy'),
      action: () => {
      },
      state: ItemState.DISABLE,
      iconColor: '#ff18cb53',
      activatedIconColor: '#ffec5d5d', // Icon fill color of the toolbar item in the activated state.
      activatedTextColor: '#ffec5d5d', // Font color of the toolbar item in the activated state.
    })
    this.toolbarList.push({
      content: 'Paste',
      icon: $r('sys.media.ohos\_ic\_public\_paste'),
      action: () => {
      },
      state: ItemState.ACTIVATE,
      textColor: '#ff18cb53',
    })
    this.toolbarList.push({
      content: 'All',
      icon: $r('sys.media.ohos\_ic\_public\_select\_all'),
      action: () => {
      },
      state: ItemState.ACTIVATE,
    })
    this.toolbarList.push({
      content: 'Share',
      icon: $r('sys.media.ohos\_ic\_public\_share'),
      action: () => {
      },
    })
    this.toolbarList.push({
      content: 'Share',
      icon: $r('sys.media.ohos\_ic\_public\_share'),
      action: () => {
      },
    })
  }

  build() {
    Row() {
      Stack() {
        Column() {
          ToolBar({
            toolBarModifier: this.toolBarModifier,
            dividerModifier: this.dividerModifier,
            activateIndex: 0,
            toolBarList: this.toolbarList,
          })
            .height(52)
        }
      }
      .align(Alignment.Bottom)
      .width('100%')
      .height('100%')
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/U_vzXOYxQj-doV3Hgo7BTg/en-us_image_0000002568685717.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062251Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1628153F441AF4CD657B9737E9BA95E02DDA5105B67EE513D3D68F98316089E6)

## Example 3: Implementing Screen Reader Announcement

This example customizes the screen reader announcement text by setting the **accessibilityText**, **accessibilityDescription**, and **accessibilityLevel** properties of the toolbar item. This functionality is supported since API version 18.

import { ToolBar, ToolBarOptions, ItemState } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State toolbarList: ToolBarOptions = new ToolBarOptions();

  aboutToAppear() {
    // Add toolbar items.
    this.toolbarList.push({
      content: 'Cut Super Long Text',
      icon: $r('sys.media.ohos\_ic\_public\_share'),
      action: () => {
      },
      accessibilityText: 'Clip', // Screen reader announcement for the item.
      accessibilityDescription: 'Double-tap to clip', // Screen reader announcement for the item.
      accessibilityLevel: 'yes' // Configure this element to be focused by accessibility screen readers.
    })
    this.toolbarList.push({
      content: 'Copy',
      icon: $r('sys.media.ohos\_ic\_public\_copy'),
      action: () => {
      },
      state: ItemState.DISABLE,
      accessibilityLevel: 'no' // Configure this button to be not recognizable by screen readers.
    })
    this.toolbarList.push({
      content: 'Paste',
      icon: $r('sys.media.ohos\_ic\_public\_paste'),
      action: () => {
      },
      state: ItemState.ACTIVATE
    })
    this.toolbarList.push({
      content: 'Select all',
      icon: $r('sys.media.ohos\_ic\_public\_select\_all'),
      action: () => {
      },
    })
    this.toolbarList.push({
      content: 'Share',
      icon: $r('sys.media.ohos\_ic\_public\_share'),
      action: () => {
      },
    })
    this.toolbarList.push({
      content: 'Share',
      icon: $r('sys.media.ohos\_ic\_public\_share'),
      action: () => {
      },
    })
  }

  build() {
    Row() {
      Stack() {
        Column() {
          ToolBar({
            activateIndex: 2,
            toolBarList: this.toolbarList,
          })
        }
      }
      .align(Alignment.Bottom)
      .width('100%')
      .height('100%')
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/VWz4KofCR52UuANaugcXyg/en-us_image_0000002537925940.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062251Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=40425B6EEA75E98A51CF8A392C9FE3BFCC62AA3FD87DD531DA18DB09D9453BD3)
