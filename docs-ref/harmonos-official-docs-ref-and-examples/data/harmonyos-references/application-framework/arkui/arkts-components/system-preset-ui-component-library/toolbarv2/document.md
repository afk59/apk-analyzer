# ToolBarV2

The **Toolbar** component is designed to present a set of action options related to the current screen, displayed at the bottom of the screen. It can display up to five child components. If there are six or more child components, the first four are shown directly, and the additional ones are grouped under a **More** item on the rightmost side of the toolbar.

This component is implemented based on [state management V2](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-state-management-overview#state-management-v2). Compared with [state management V1](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-state-management-overview#state-management-v1), V2 offers a higher level of observation and management over data objects beyond the component level. You can now more easily manage toolbar data and states with greater flexibility, leading to faster UI updates.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/aOzDbnn3QaOE3rO9kW6FQQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062251Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0F4AE1C47D11DCF6ECF8E3736162C801B688B890B551ED93276A8229317FD5D5)

-   This component is supported since API version 18. Updates will be marked with a superscript to indicate their earliest API version.
    
-   If the **ToolBarV2** component has [universal attributes](../../universal-attributes/document.md) and [universal events](../../universal-events/document.md) configured, the compiler toolchain automatically generates an additional ****Common**** node and mounts the universal attributes and universal events on this node rather than the **ToolBarV2** component itself. As a result, the configured universal attributes and universal events may fail to take effect or behave as intended. For this reason, avoid using universal attributes and events with the **ToolBarV2** component.
    
-   The toolbar background color does not automatically switch when the system changes between light and dark modes.
    

#### Modules to Import

import { ToolBarV2 } from '@kit.ArkUI';

#### Child Components

Not supported

#### ToolBarV2

ToolbarV2({toolBarList: ToolBarV2Item\[\], activatedIndex?: number, dividerModifier: DividerModifier, toolBarModifier: ToolBarV2Modifier})

Creates a toolbar.

**Decorator**: @ComponentV2

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Type | Mandatory | Decorator | Description |
| :-- | :-- | :-- | :-- | :-- |
| toolBarList | [ToolBarV2Item](#toolbarv2item)\[\] | Yes | 
@Param

@Require

 | Toolbar list. |
| activatedIndex | number | No | @Param | 

Index of the active item.

Default value: **\-1**, indicating that no toolbar item is activated

Value range: \[-1, 4\]

 |
| dividerModifier | [DividerModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#custom-modifier) | No | @Param | 

Modifier for the toolbar header divider, which can be used to customize the divider's height, color, and other attributes.

This parameter does not take effect by default.

 |
| toolBarModifier | [ToolBarV2Modifier](#toolbarv2modifier) | No | @Param | 

Modifier for the toolbar, which can be used to set the toolbar's height, background color, padding (which only takes effect when there are fewer than five toolbar items), and whether to display the pressed state.

This parameter does not take effect by default.

 |

#### ToolBarV2Item

Defines an item in the toolbar.

**Decorator**: @ObservedV2

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

## Properties

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| content | [ToolBarV2ItemText](#toolbarv2itemtext) | No | No | 
Text of the toolbar item.

Decorator: @Trace

 |
| action | [ToolBarV2ItemAction](#toolbarv2itemaction) | No | Yes | 

Click event of the toolbar item.

By default, there is no click event.

Decorator: @Trace

 |
| icon | [ToolBarV2ItemIconType](#toolbarv2itemicontype) | No | Yes | 

Icon of the toolbar item.

By default, there is no icon.

Decorator: @Trace

 |
| state | [ToolBarV2ItemState](#toolbarv2itemstate) | No | Yes | 

State of the toolbar item.

Default value: **ToolBarV2ItemState.ENABLE**

Decorator: @Trace

 |
| accessibilityText | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 

Accessibility text, that is, accessible label name, of the toolbar item. If a component does not contain text information, it will not be announced by the screen reader when selected. In this case, the screen reader user cannot know which component is selected. To solve this problem, you can set accessibility text for components without text information. When such a component is selected, the screen reader announces the specified accessibility text, informing the user which component is selected.

Default value: value of **content**

Decorator: @Trace

 |
| accessibilityDescription | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 

Accessible description of the toolbar item. You can provide comprehensive text explanations to help users understand the operation they are about to perform and its potential consequences, especially when these cannot be inferred from the component's attributes and accessibility text alone. If a component contains both text information and the accessible description, the text is announced first and then the accessible description, when the component is selected.

Default value: **"Double-tap to activate"**

Decorator: @Trace

 |
| accessibilityLevel | string | No | Yes | 

Accessibility level of the toolbar item. It determines whether the component can be recognized by accessibility services.

The options are as follows:

**"auto"**: This option is treated as "yes" by the system for this component.

**"yes"**: The component can be recognized by accessibility services.

**"no"**: The component cannot be recognized by accessibility services.

**"no-hide-descendants"**: Neither the component nor its child components can be recognized by accessibility services.

Default value: **"auto"**

Decorator: @Trace

 |

#### \[h2\]constructor

constructor(options: ToolBarV2ItemOptions)

A constructor used to create a **ToolBarV2Item** instance.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [ToolBarV2ItemOptions](#toolbarv2itemoptions) | Yes | Configuration options of the toolbar item. |

#### ToolBarV2ItemOptions

Defines the options for initializing a **ToolBarV2Item** object.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| content | [ToolBarV2ItemText](#toolbarv2itemtext) | No | No | Text of the toolbar item. |
| action | [ToolBarV2ItemAction](#toolbarv2itemaction) | No | Yes | 
Click event of the toolbar item.

By default, there is no click event.

 |
| icon | [ToolBarV2ItemIconType](#toolbarv2itemicontype) | No | Yes | 

Icon of the toolbar item.

By default, there is no icon.

 |
| state | [ToolBarV2ItemState](#toolbarv2itemstate) | No | Yes | 

State of the toolbar item.

Default value: **ToolBarV2ItemState.ENABLE**

 |
| accessibilityText | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 

Accessibility text, that is, accessible label name, of the toolbar item. If a component does not contain text information, it will not be announced by the screen reader when selected. In this case, the screen reader user cannot know which component is selected. To solve this problem, you can set accessibility text for components without text information. When such a component is selected, the screen reader announces the specified accessibility text, informing the user which component is selected.

Default value: value of **content**

 |
| accessibilityDescription | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 

Accessible description of the toolbar item. You can provide comprehensive text explanations to help users understand the operation they are about to perform and its potential consequences, especially when these cannot be inferred from the component's attributes and accessibility text alone. If a component contains both text information and the accessible description, the text is announced first and then the accessible description, when the component is selected.

Default value: **"Double-tap to activate"**

 |
| accessibilityLevel | string | No | Yes | 

Accessibility level of the toolbar item. It determines whether the component can be recognized by accessibility services.

The options are as follows:

**"auto"**: This option is treated as "yes" by the system for this component.

**"yes"**: The component can be recognized by accessibility services.

**"no"**: The component cannot be recognized by accessibility services.

**"no-hide-descendants"**: Neither the component nor its child components can be recognized by accessibility services.

Default value: **"auto"**

 |

#### ToolBarV2ItemAction

type ToolBarV2ItemAction = (index: number) => void

Defines the callback for the click event of a toolbar item.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| index | number | Yes | 
Index of the toolbar item that triggers the click event.

 |

#### ToolBarV2ItemText

Defines the text of a toolbar item.

**Decorator**: @ObservedV2

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

## Properties

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| text | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | No | 
Text of the toolbar item.

Decorator: @Trace

 |
| color | [ColorMetrics](../../../arkts-api/ui/arkui/graphics/document.md#colormetrics12) | No | Yes | 

Font color of the toolbar item.

Default value: **$r('sys.color.font\_primary')**

Decorator: @Trace

 |
| activatedColor | [ColorMetrics](../../../arkts-api/ui/arkui/graphics/document.md#colormetrics12) | No | Yes | 

Font color of the toolbar item in the activated state.

Default value: **$r('sys.color.font\_emphasize')**

Decorator: @Trace

 |

#### \[h2\]constructor

constructor(options: ToolBarV2ItemTextOptions)

A constructor used to create a **ToolBarV2ItemText** instance.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [ToolBarV2ItemTextOptions](#toolbarv2itemtextoptions) | Yes | Configuration options of the text content. |

#### ToolBarV2ItemTextOptions

Defines the options for initializing a **ToolBarV2ItemText** object.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| text | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | No | Text of the toolbar item. |
| color | [ColorMetrics](../../../arkts-api/ui/arkui/graphics/document.md#colormetrics12) | No | Yes | 
Font color of the toolbar item.

Default value: **$r('sys.color.font\_primary')**

 |
| activatedColor | [ColorMetrics](../../../arkts-api/ui/arkui/graphics/document.md#colormetrics12) | No | Yes | 

Font color of the toolbar item in the activated state.

Default value: **$r('sys.color.font\_emphasize')**

 |

#### ToolBarV2ItemImage

Defines the icon content of a toolbar item.

**Decorator**: @ObservedV2

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

## Properties

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| src | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | No | 
Icon of the toolbar item.

Decorator: @Trace

 |
| color | [ColorMetrics](../../../arkts-api/ui/arkui/graphics/document.md#colormetrics12) | No | Yes | 

Color of the icon.

Default value: **$r('sys.color.icon\_primary')**

Decorator: @Trace

 |
| activatedColor | [ColorMetrics](../../../arkts-api/ui/arkui/graphics/document.md#colormetrics12) | No | Yes | 

Color of the icon when the toolbar item is activated.

Default value: **$r('sys.color.icon\_emphasize')**

Decorator: @Trace

 |

#### \[h2\]constructor

constructor(options: ToolBarV2ItemImageOptions)

A constructor used to create a **ToolBarV2ItemImage** instance.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [ToolBarV2ItemImageOptions](#toolbarv2itemimageoptions) | Yes | Configuration options for the icon content of the toolbar item. |

#### ToolBarV2ItemImageOptions

Defines the options for initializing a **ToolBarV2ItemImage** object.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| src | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | No | Icon of the toolbar item. |
| color | [ColorMetrics](../../../arkts-api/ui/arkui/graphics/document.md#colormetrics12) | No | Yes | 
Color of the icon.

Default value: **$r('sys.color.icon\_primary')**

 |
| activatedColor | [ColorMetrics](../../../arkts-api/ui/arkui/graphics/document.md#colormetrics12) | No | Yes | 

Color of the icon when the toolbar item is activated.

Default value: **$r('sys.color.icon\_emphasize')**

 |

#### ToolBarV2ItemIconType

type ToolBarV2ItemIconType = ToolBarV2ItemImage | ToolBarV2SymbolGlyph

Defines the union type for the icon content of a toolbar item.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Type | Description |
| :-- | :-- |
| [ToolBarV2ItemImage](#toolbarv2itemimage) | Type for defining a common icon. |
| [ToolBarV2SymbolGlyph](#toolbarv2symbolglyph) | Type for defining a symbol icon. |

#### ToolBarV2Modifier

Provides APIs for setting the height (**height**), background color (**backgroundColor**), left and right padding (**padding**, which only takes effect when there are fewer than five items) of the toolbar, and whether to display the pressed state effect (**stateEffect**).

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

#### \[h2\]backgroundColor

backgroundColor(backgroundColor: ColorMetrics): ToolBarV2Modifier

Sets the background color of the toolbar. By overriding this API, you can implement custom drawing for the background color of the toolbar.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| backgroundColor | [ColorMetrics](../../../arkts-api/ui/arkui/graphics/document.md#colormetrics12) | Yes | 
Toolbar background color

Default value: **$r('sys.color.ohos\_id\_color\_toolbar\_bg')**

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [ToolBarV2Modifier](#toolbarv2modifier) | **ToolBarV2Modifier** object after the background color is set. |

#### \[h2\]padding

padding(padding: LengthMetrics): ToolBarV2Modifier

Sets the left and right padding of the toolbar. By overriding this API, you can implement custom drawing for the left and right padding of the toolbar.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| padding | [LengthMetrics](../../../arkts-api/ui/arkui/graphics/document.md#lengthmetrics12) | Yes | 
Left and right padding of the toolbar, which is effective only when there are fewer than five items.

By default, the left and right padding is set to 24 vp when there are fewer than five items, and 0 vp when there are five or more items.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [ToolBarV2Modifier](#toolbarv2modifier) | **ToolBarV2Modifier** object after the padding is set. |

#### \[h2\]height

height(height: LengthMetrics): ToolBarV2Modifier

Sets the height of the toolbar. By overriding this API, you can implement custom drawing for the height of the toolbar, which does not include the height of the divider.

**Atomic service API**: This API can be used in atomic services since API version 18.

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
| [ToolBarV2Modifier](#toolbarv2modifier) | **ToolBarV2Modifier** object after the height is set. |

#### \[h2\]stateEffect

stateEffect(stateEffect: boolean): ToolBarV2Modifier

Sets whether to display the pressed state effect.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| stateEffect | boolean | Yes | 
Whether to display the pressed state effect on the toolbar.

**true**: Display the pressed state effect.

**false**: Do not display the pressed state effect.

Default value: **true**

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [ToolBarV2Modifier](#toolbarv2modifier) | **ToolBarV2Modifier** object after the pressed state effect is set. |

#### ToolBarV2ItemState

Enumerates the states of the toolbar item.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Value | Description |
| :-- | :-- | :-- |
| ENABLE | 1 | The toolbar item is enabled. |
| DISABLE | 2 | The toolbar item is disabled. |
| ACTIVATE | 3 | The toolbar item is activated. |

#### ToolBarV2SymbolGlyph

Defines the icon symbol options.

**Decorator**: @ObservedV2

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

## Properties

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| normal | [SymbolGlyphModifier](../../universal-attributes/modifiers-and-custom-property/symbol-glyph-modifier/document.md#symbolglyphmodifier) | No | No | 
Icon symbol of the toolbar item in normal state.

Decorator: @Trace

 |
| activated | [SymbolGlyphModifier](../../universal-attributes/modifiers-and-custom-property/symbol-glyph-modifier/document.md#symbolglyphmodifier) | No | Yes | 

Icon symbol of the toolbar item in activated state.

Default value:

**fontColor**: **$r('sys.color.icon\_emphasize')**, **fontSize**: **24vp**

Decorator: @Trace

 |

#### \[h2\]constructor

constructor(options: ToolBarV2SymbolGlyphOptions)

A constructor used to create a **ToolBarV2SymbolGlyph** object.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [ToolBarV2SymbolGlyphOptions](#toolbarv2symbolglyphoptions) | Yes | Configuration options of the symbol icon. |

#### ToolBarV2SymbolGlyphOptions

Defines the options for initializing a **ToolBarV2SymbolGlyph** object.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| normal | [SymbolGlyphModifier](../../universal-attributes/modifiers-and-custom-property/symbol-glyph-modifier/document.md#symbolglyphmodifier) | No | No | Icon symbol of the toolbar item in normal state. |
| activated | [SymbolGlyphModifier](../../universal-attributes/modifiers-and-custom-property/symbol-glyph-modifier/document.md#symbolglyphmodifier) | No | Yes | 
Icon symbol of the toolbar item in activated state.

Default value:

**fontColor**: **$r('sys.color.icon\_emphasize')**, **fontSize**: **24vp**

 |

#### Example

## Example 1: Setting Toolbar Items to Different States

This example shows the various display effects when the **state** property of toolbar items is set to **ENABLE**, **DISABLE**, or **ACTIVATE**.

import { ToolBarV2ItemImage, ToolBarV2ItemState, ToolBarV2ItemText, ToolBarV2Item, ToolBarV2 } from '@kit.ArkUI';

@Entry
@ComponentV2
struct Index {
  @Local toolbarList: ToolBarV2Item\[\] = \[\]

  aboutToAppear() {
    this.toolbarList.push(new ToolBarV2Item({
      content: new ToolBarV2ItemText(
        {
          text: Long long long long long'
        }
      ),
      icon: new ToolBarV2ItemImage({
        src: $r('sys.media.ohos\_ic\_public\_share')
      }),
      action: () => {
      },
    }))
    this.toolbarList.push(
      new ToolBarV2Item({
        content: new ToolBarV2ItemText(
          {
            text: 'Copy'
          }
        ),
        icon: new ToolBarV2ItemImage({
          src: $r('sys.media.ohos\_ic\_public\_copy')
        }),
        action: () => {
        },
        state: ToolBarV2ItemState.DISABLE
      })
    )
    this.toolbarList.push(
      new ToolBarV2Item({
        content: new ToolBarV2ItemText(
          {
            text: 'Paste'
          }
        ),
        icon: new ToolBarV2ItemImage({
          src: $r('sys.media.ohos\_ic\_public\_paste')
        }),
        action: () => {
        },
        state: ToolBarV2ItemState.ACTIVATE
      })
    )
    this.toolbarList.push(
      new ToolBarV2Item({
        content: new ToolBarV2ItemText(
          {
            text: 'All'
          }
        ),
        icon: new ToolBarV2ItemImage({
          src: $r('sys.media.ohos\_ic\_public\_select\_all')
        }),
        action: () => {
        },
      })
    )
    this.toolbarList.push(
      new ToolBarV2Item({
        content: new ToolBarV2ItemText(
          {
            text: 'Share'
          }
        ),
        icon: new ToolBarV2ItemImage({
          src: $r('sys.media.ohos\_ic\_public\_share')
        }),
        action: () => {
        },
      })
    )
    this.toolbarList.push(
      new ToolBarV2Item({
        content: new ToolBarV2ItemText(
          {
            text: 'Share'
          }
        ),
        icon: new ToolBarV2ItemImage({
          src: $r('sys.media.ohos\_ic\_public\_share')
        }),
        action: () => {
        },
      })
    )
  }

  build() {
    Row() {
      Stack() {
        Column() {
          ToolBarV2({
            activatedIndex: 2,
            toolBarList: this.toolbarList,
          })
        }
      }.align(Alignment.Bottom)
      .width('100%').height('100%')
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/E-IzrItyTLK11EazhrSEdQ/en-us_image_0000002537925940.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062251Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4905F7E77EABB505C88D89FF520A20B079725F147991FC26F2C579CFE15A9634)

## Example 2: Customizing the Toolbar Style

This example demonstrates how to customize the toolbar's height, background color, and other styles using **ToolBarV2Modifier**.

import {
  SymbolGlyphModifier,
  DividerModifier,
  LengthMetrics,
  ColorMetrics,
  ToolBarV2Item,
  ToolBarV2Modifier,
  ToolBarV2ItemText,
  ToolBarV2ItemImage,
  ToolBarV2,
  ToolBarV2ItemState,
  ToolBarV2SymbolGlyph
} from '@kit.ArkUI';

@Entry
@ComponentV2
struct Index {
  @Local toolbarList: ToolBarV2Item\[\] = \[\];
  private toolBarModifier: ToolBarV2Modifier =
    new ToolBarV2Modifier().height(LengthMetrics.vp(52))
      .backgroundColor(ColorMetrics.resourceColor(Color.Transparent))
      .stateEffect(false);
  @Local dividerModifier: DividerModifier = new DividerModifier().height(0);

  aboutToAppear() {
    this.toolbarList.push(
      new ToolBarV2Item({
        content: new ToolBarV2ItemText({
          text: 'Long long long long long long long long text',
          activatedColor: ColorMetrics.resourceColor($r('sys.color.font\_primary'))
        }),
        icon: new ToolBarV2SymbolGlyph({
          normal: new SymbolGlyphModifier($r('sys.symbol.ohos\_star')).fontColor(\[Color.Green\]),
          activated: new SymbolGlyphModifier($r('sys.symbol.ohos\_star')).fontColor(\[Color.Red\]),
        }),
        action: () => {
        },
        state: ToolBarV2ItemState.ACTIVATE,
      })
    )
    this.toolbarList.push(
      new ToolBarV2Item({
        content: new ToolBarV2ItemText({
          text: 'Copy',
          activatedColor: ColorMetrics.resourceColor('#ffec5d5d')
        }),
        icon: new ToolBarV2ItemImage({
          src: $r('sys.media.ohos\_ic\_public\_copy'),
          color: ColorMetrics.resourceColor('#ff18cb53'),
          activatedColor: ColorMetrics.resourceColor('#ffec5d5d'),
        }),
        action: () => {
        },
        state: ToolBarV2ItemState.DISABLE,
      }))
    this.toolbarList.push(
      new ToolBarV2Item({
        content: new ToolBarV2ItemText({
          text: 'Paste',
          color: ColorMetrics.resourceColor('#ff18cb53')
        }),
        icon: new ToolBarV2ItemImage({
          src: $r('sys.media.ohos\_ic\_public\_paste'),
        }),
        action: () => {
        },
        state: ToolBarV2ItemState.ACTIVATE,
      })
    )
    this.toolbarList.push(
      new ToolBarV2Item({
        content: new ToolBarV2ItemText({
          text: 'All',
        }),
        icon: new ToolBarV2ItemImage({
          src: $r('sys.media.ohos\_ic\_public\_select\_all'),
        }),
        action: () => {
        },
        state: ToolBarV2ItemState.ACTIVATE,
      }))
    this.toolbarList.push(
      new ToolBarV2Item({
        content: new ToolBarV2ItemText({
          text: 'Share',
        }),
        icon: new ToolBarV2ItemImage({
          src: $r('sys.media.ohos\_ic\_public\_share'),
        }),
        action: () => {
        },
      }))
    this.toolbarList.push(
      new ToolBarV2Item({
        content: new ToolBarV2ItemText({
          text: 'Share'
        }),
        icon: new ToolBarV2ItemImage({
          src: $r('sys.media.ohos\_ic\_public\_share'),
        }),
        action: () => {
        },
      })
    )
  }

  build() {
    Row() {
      Stack() {
        Column() {
          ToolBarV2({
            toolBarModifier: this.toolBarModifier,
            dividerModifier: this.dividerModifier,
            activatedIndex: 0,
            toolBarList: this.toolbarList,
          })
            .height(52)
        }
      }.align(Alignment.Bottom)
      .width('100%').height('100%')
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/NnS36ggKTF-EYuajvEtLqw/en-us_image_0000002568685717.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062251Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FC9DD9572ADB39AEE5656348D7359B6E1E97466AB70353E38BF99AFCB5ABE183)

## Example 3: Implementing Screen Reader Announcement

This example customizes the screen reader announcement text by setting the **accessibilityText**, **accessibilityDescription**, and **accessibilityLevel** properties of the toolbar item.

import {
  DividerModifier,
  LengthMetrics,
  ColorMetrics,
  ToolBarV2Item,
  ToolBarV2Modifier,
  ToolBarV2ItemText,
  ToolBarV2ItemImage,
  ToolBarV2,
  ToolBarV2ItemState,
} from '@kit.ArkUI';

@Entry
@ComponentV2
struct Index {
  @Local toolbarList: ToolBarV2Item\[\] = \[\];
  private toolBarModifier: ToolBarV2Modifier =
    new ToolBarV2Modifier().height(LengthMetrics.vp(52))
      .backgroundColor(ColorMetrics.resourceColor(Color.Transparent))
      .stateEffect(false);
  @Local dividerModifier: DividerModifier = new DividerModifier().height(0);

  aboutToAppear() {
    this.toolbarList.push(
      new ToolBarV2Item({
        content: new ToolBarV2ItemText({
          text: Long long long long long'
        }),
        icon: new ToolBarV2ItemImage({
          src: $r('sys.media.ohos\_ic\_public\_share')
        }),
        action: () => {
        },
        accessibilityText: 'Clip', // Screen reader announcement text for the item.
        accessibilityDescription: 'Double-tap to clip', // Screen reader announcement description for the item.
        accessibilityLevel: 'yes'  // Configure this element to be focused by accessibility screen readers.
      })
    )
    this.toolbarList.push(
      new ToolBarV2Item({
        content: new ToolBarV2ItemText({
          text: 'Copy',
        }),
        icon: new ToolBarV2ItemImage({
          src: $r('sys.media.ohos\_ic\_public\_copy'),
        }),
        action: () => {
        },
        state: ToolBarV2ItemState.DISABLE,
        accessibilityLevel: 'no'  // Configure this element not to be focused by accessibility screen readers.
      }))
    this.toolbarList.push(
      new ToolBarV2Item({
        content: new ToolBarV2ItemText({
          text: 'Paste',
        }),
        icon: new ToolBarV2ItemImage({
          src: $r('sys.media.ohos\_ic\_public\_paste'),
        }),
        action: () => {
        },
        state: ToolBarV2ItemState.ACTIVATE,
      })
    )
    this.toolbarList.push(
      new ToolBarV2Item({
        content: new ToolBarV2ItemText({
          text: 'All',
        }),
        icon: new ToolBarV2ItemImage({
          src: $r('sys.media.ohos\_ic\_public\_select\_all'),
        }),
        action: () => {
        },
      }))
    this.toolbarList.push(
      new ToolBarV2Item({
        content: new ToolBarV2ItemText({
          text: 'Share'
        }),
        icon: new ToolBarV2ItemImage({
          src: $r('sys.media.ohos\_ic\_public\_share'),
        }),
        action: () => {
        },
      }))
    this.toolbarList.push(
      new ToolBarV2Item({
        content: new ToolBarV2ItemText({
          text: 'Share'
        }),
        icon: new ToolBarV2ItemImage({
          src: $r('sys.media.ohos\_ic\_public\_share'),
        }),
        action: () => {
        },
      })
    )
  }

  build() {
    Row() {
      Stack() {
        Column() {
          ToolBarV2({
            toolBarModifier: this.toolBarModifier,
            dividerModifier: this.dividerModifier,
            activatedIndex: 0,
            toolBarList: this.toolbarList,
          })
            .height(52)
        }
      }.align(Alignment.Bottom)
      .width('100%').height('100%')
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/nWG2FmAXSh217c-4IwaIgQ/en-us_image_0000002537925940.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062251Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AC32C90292FAA09FC769568E8630167D154A022B9DF520AC40164CA7749CF845)
