# ComposeListItem

The **ComposeListItem** component is a container that presents a series of items arranged in a column with the same width. You can use it to present data of the same type in a multiple and coherent row style, for example, images or text.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/iVgLWdxNQEG3Uh605jSZDw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062250Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A224229CF6AFFCE41C0FC531343C819E575FE99DE9F40183D52FCDC4C01ED853)

This component is supported since API version 10. Updates will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { ComposeListItem } from "@kit.ArkUI";

#### Child Components

Not supported

#### Attributes

The [universal attributes](../../universal-attributes/document.md) are not supported.

#### ComposeListItem

ComposeListItem({contentItem?: ContentItem, operateItem?: OperateItem})

Creates a **ComposeListItem** component that allows customization of the left, center, and right content areas.

**Decorator**: @Component

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Type | Mandatory | Decorator | Description |
| :-- | :-- | :-- | :-- | :-- |
| contentItem | [ContentItem](#contentitem) | No | @Prop | 
Elements on the left and in the center.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| operateItem | [OperateItem](#operateitem) | No | @Prop | 

Element on the right.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |

#### ContentItem

Defines elements for the left and center areas of the **ComposeListItem** component.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| iconStyle | [IconType](#icontype) | No | Yes | 
Icon style of the element on the left.

If this parameter is not set or is set to **undefined**, the icon is not displayed.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| icon | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 

Icon resource of the element on the left.

If this parameter is not set or is set to **undefined**, the icon is not displayed.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| symbolStyle18+ | [SymbolGlyphModifier](../../universal-attributes/modifiers-and-custom-property/symbol-glyph-modifier/document.md#symbolglyphmodifier) | No | Yes | 

Symbol icon resource of the element on the left, which has higher priority than **icon**. If both **icon** and this parameter are set, only the symbol icon is displayed.

If this parameter is not set or is set to **undefined**, the symbol icon is not displayed.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| primaryText | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 

Primary text of the element in the center.

If this parameter is not set or is set to **undefined**, the primary text is not displayed.

**Text processing rules**: Text will wrap to a new line when it exceeds the length limit.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| secondaryText | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 

Secondary text of the element in the center.

If this parameter is not set or is set to **undefined**, the secondary text is not displayed.

**Text processing rules**: Text will wrap to a new line when it exceeds the length limit.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| description | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 

Description of the element in the center.

If this parameter is not set or is set to **undefined**, the description is not displayed.

**Text processing rules**: Text will wrap to a new line when it exceeds the length limit.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |

#### IconType

Defines the icon type of the element on the left of the **ComposeListItem** component.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Value | Description |
| :-- | :-- | :-- |
| BADGE | 1 | Badge with an icon size of 8 x 8 vp. |
| NORMAL\_ICON | 2 | Small icon with an icon size of 16 x 16 vp. |
| SYSTEM\_ICON | 3 | System icon with an icon size of 24 x 24 vp. |
| HEAD\_SCULPTURE | 4 | Profile picture with an icon size of 40 x 40 vp. |
| APP\_ICON | 5 | Application icon with an icon size of 64 x 64 vp. |
| PREVIEW | 6 | Preview image with an icon size of 96 x 96 vp. |
| LONGITUDINAL | 7 | Icon with a horizontal special ratio (width is greater than height), keeping the longest side at 96 vp. |
| VERTICAL | 8 | Icon with a vertical special ratio (height is greater than width), keeping the longest side at 96 vp. |

#### OperateItem

Defines the type of the element on the right of the **ComposeListItem** component.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| arrow | [OperateIcon](#operateicon) | No | Yes | 
Arrow with a size of 12 x 24 vp.

If this parameter is not set or is set to **undefined**, the arrow is not displayed.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| icon | [OperateIcon](#operateicon) | No | Yes | 

First icon with a size of 24 x 24 vp.

If this parameter is not set or is set to **undefined**, the icon is not displayed.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| subIcon | [OperateIcon](#operateicon) | No | Yes | 

Second icon with a size of 24 x 24 vp.

If this parameter is not set or is set to **undefined**, the icon is not displayed.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| button | [OperateButton](#operatebutton) | No | Yes | 

Button.

If this parameter is not set or is set to **undefined**, the button is not displayed.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| switch | [OperateCheck](#operatecheck) | No | Yes | 

Switch.

If this parameter is not set or is set to **undefined**, the switch is not displayed.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| checkbox | [OperateCheck](#operatecheck) | No | Yes | 

Check box with a size of 24 x 24 vp.

If this parameter is not set or is set to **undefined**, the check box is not displayed.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| radio | [OperateCheck](#operatecheck) | No | Yes | 

Radio button with a size of 24 x 24 vp.

If this parameter is not set or is set to **undefined**, the radio button is not displayed.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| image | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 

Image with a size of 48 x 48 vp.

If this parameter is not set or is set to **undefined**, the image is not displayed.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| symbolStyle18+ | [SymbolGlyphModifier](../../universal-attributes/modifiers-and-custom-property/symbol-glyph-modifier/document.md#symbolglyphmodifier) | No | Yes | 

Symbol icon with a size of 48 x 48 vp.

If this parameter is not set or is set to **undefined**, the symbol icon is not displayed.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| text | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 

Text.

If this parameter is not set or is set to **undefined**, the text is not displayed.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |

#### OperateIcon

Defines the type of the icon element on the right of the **ComposeListItem** component.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| value | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | No | 
Resource of the icon or arrow on the right.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| symbolStyle18+ | [SymbolGlyphModifier](../../universal-attributes/modifiers-and-custom-property/symbol-glyph-modifier/document.md#symbolglyphmodifier) | No | Yes | 

Resource of the symbol icon or arrow on the right, which has higher priority than **value**.

If this parameter is not set or is set to **undefined**, the symbol icon is not displayed.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| action | ()=>void | No | Yes | 

Click event of the icon or arrow on the right.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| accessibilityText18+ | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 

Accessibility text, that is, accessible label name, of the icon or arrow on the right. If a component does not contain text information, it will not be announced by the screen reader when selected. In this case, the screen reader user cannot know which component is selected. To solve this problem, you can set accessibility text for components without text information. When such a component is selected, the screen reader announces the specified accessibility text, informing the user which component is selected.

Default value: **""**.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| accessibilityDescription18+ | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 

Accessible description of the icon or arrow on the right. You can provide comprehensive text explanations to help users understand the operation they are about to perform and its potential consequences, especially when these cannot be inferred from the component's attributes and accessibility text alone. If a component contains both text information and the accessible description, the text is announced first and then the accessible description, when the component is selected.

Default value: **"Double-tap to activate"**

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| accessibilityLevel18+ | string | No | Yes | 

Accessibility level of the icon or arrow on the right. It determines whether the component can be recognized by accessibility services.

The options are as follows:

**"auto"**: It is treated as "no" by the system.

**"yes"**: The component can be recognized by accessibility services.

**"no"**: The component cannot be recognized by accessibility services.

**"no-hide-descendants"**: Neither the component nor its child components can be recognized by accessibility services.

Default value: **"auto"**.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |

#### OperateButton

Defines the type of the button element on the right of the **ComposeListItem** component.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| text | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 
Text of the button on the right.

Default value: **""**.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| accessibilityText18+ | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 

Accessibility text, that is, accessible label name, of the button on the right. If a component does not contain text information, it will not be announced by the screen reader when selected. In this case, the screen reader user cannot know which component is selected. To solve this problem, you can set accessibility text for components without text information. When such a component is selected, the screen reader announces the specified accessibility text, informing the user which component is selected.

Default value: **""**.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| accessibilityDescription18+ | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 

Accessible description of the button on the right. You can provide comprehensive text explanations to help users understand the operation they are about to perform and its potential consequences, especially when these cannot be inferred from the component's attributes and accessibility text alone. If a component contains both text information and the accessible description, the text is announced first and then the accessible description, when the component is selected.

Default value: **"Double-tap to activate"**

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| accessibilityLevel18+ | string | No | Yes | 

Accessibility level of the button on the right. It determines whether the component can be recognized by accessibility services.

The options are as follows:

**"auto"**: It is treated as "no" by the system.

**"yes"**: The component can be recognized by accessibility services.

**"no"**: The component cannot be recognized by accessibility services.

**"no-hide-descendants"**: Neither the component nor its child components can be recognized by accessibility services.

Default value: **"auto"**.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |

#### OperateCheck

Defines the type where the element on the right of the **ComposeListItem** component is **Switch**, **CheckBox**, or **Radio**.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| isCheck | boolean | No | Yes | 
Whether the switch, check box, or radio button on the right is selected.

Default value: **false**.

**true**: selected.

**false**: not selected.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| onChange | (value: boolean)=>void | No | Yes | 

Callback invoked when the selected state of the switch, check box, or radio button on the right is changed.

**true**: from not selected to selected.

**false**: from selected to not selected.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| accessibilityText18+ | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 

Accessibility text, that is, accessible label name, of the switch, check box, or radio button on the right. If a component does not contain text information, it will not be announced by the screen reader when selected. In this case, the screen reader user cannot know which component is selected. To solve this problem, you can set accessibility text for components without text information. When such a component is selected, the screen reader announces the specified accessibility text, informing the user which component is selected.

Default value: **""**.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| accessibilityDescription18+ | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 

Accessible description of the switch, check box, or radio button on the right. You can provide comprehensive text explanations to help users understand the operation they are about to perform and its potential consequences, especially when these cannot be inferred from the component's attributes and accessibility text alone. If a component contains both text information and the accessible description, the text is announced first and then the accessible description, when the component is selected.

By default, the announcement rules for the basic components **Switch**, **CheckBox**, and **Radio** are applied.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| accessibilityLevel18+ | string | No | Yes | 

Accessibility level of the switch, check box, or radio button on the right. It determines whether the component can be recognized by accessibility services.

The options are as follows:

**"auto"**: It is treated as "no" by the system.

**"yes"**: The component can be recognized by accessibility services.

**"no"**: The component cannot be recognized by accessibility services.

**"no-hide-descendants"**: Neither the component nor its child components can be recognized by accessibility services.

Default value: **"auto"**.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |

#### Events

The [universal events](../../universal-events/document.md) are not supported.

#### Example

## Example 1: Configuring a Simple List Item

This example demonstrates how to create a simple list item that includes a primary text, a secondary text, a description, and a button with accompanying text on the right.

// This example demonstrates the basic functionality of the component, including the use of elements on the left and right.
import { IconType, ComposeListItem } from '@kit.ArkUI';

@Entry
@Component
struct ComposeListItemExample {
  build() {
    Column() {
      List() {
        ListItem() {
          ComposeListItem({
            contentItem: ({
              iconStyle: IconType.NORMAL\_ICON,
              icon: $r('sys.media.ohos\_app\_icon'),
              primaryText: 'Double-line list',
              secondaryText: 'Secondary text',
              description: 'Description'
            }),
            operateItem: ({
              icon: {
                value: $r('sys.media.ohos\_app\_icon'),
                action: () => {
                  this.getUIContext().getPromptAction().showToast({
                    message: 'icon'
                  });
                } },
              text: 'Text on the right'
            })
          })
        }
      }
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/LTBA85TLTtull6zpISBvXQ/en-us_image_0000002537925902.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062250Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5790A17603DFD85653E882F28645E4839D2D3DE5FC03B2E41AF67C42126EA888)

## Example 2: Implementing Screen Reader Announcement for Right-Side Elements

This example shows how to use the **accessibilityText**, **accessibilityDescription**, and **accessibilityLevel** properties to customize the screen reader announcements for different right-side elements such as icons, buttons, and radio buttons in a list item. This functionality is supported since API version 18.

import { IconType, ComposeListItem } from '@kit.ArkUI';
@Entry
@Component
struct ComposeListItemExample {
  build() {
    Column() {
      List() {
        ListItem() {
          ComposeListItem({
            contentItem: ({
              iconStyle: IconType.NORMAL\_ICON,
              icon: $r('sys.media.ohos\_app\_icon'),
              primaryText: 'Double-line list',
              secondaryText: 'Secondary text',
              description: 'Description'
            }),
            operateItem: ({
              radio: {
                accessibilityText: 'Radio button', // Screen reader announcement for the radio button.
                accessibilityDescription: 'Unselected', // Description read by screen reader when the radio button is unselected.
                accessibilityLevel: 'yes'  // Configure this element to be focused by accessibility screen readers.
              }
            })
          })
        }

        ListItem() {
          ComposeListItem({
            contentItem: ({
              iconStyle: IconType.NORMAL\_ICON,
              icon: $r('sys.media.ohos\_app\_icon'),
              primaryText: 'Double-line list',
              secondaryText: 'Secondary text',
              description: 'Description'
            }),
            operateItem: ({
              button: {
                text: 'OK',
                accessibilityText: 'This is a button',
                accessibilityDescription: 'Double tap to activate',
                accessibilityLevel: 'no'  // Configure this button to be not recognizable by screen reader services.
              }
            })
          })
        }

        ListItem() {
          ComposeListItem({
            contentItem: ({
              iconStyle: IconType.NORMAL\_ICON,
              icon: $r('sys.media.ohos\_app\_icon'),
              primaryText: 'Double-line list',
              secondaryText: 'Secondary text',
              description: 'Description'
            }),
            operateItem: ({
              icon: {
                value: $r('sys.media.ohos\_app\_icon'),
                action: () => {
                this.getUIContext().getPromptAction().showToast({
                    message: 'icon'
                  });
                },
                accessibilityText: 'This is an icon', // Screen reader announcement for the icon.
                accessibilityDescription: 'Double-tap to show the toast', // Description read by screen reader for the icon action.
                accessibilityLevel: 'yes'  // Configure this element to be focused by accessibility screen readers.
              }
            })
          })
        }
      }
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/0MjH6BlMSC6X2-r2vnncJw/en-us_image_0000002568685679.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062250Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D77F71FD9BB613880771EFC2693F8109302571B80DE65E68C85397C58618325C)

## Example 3: Setting the Symbol Icon

This example demonstrates how to use **symbolStyle** in **ContentItem**, **OperateItem**, and **OperateIcon** to set custom symbol icons. This functionality is supported since API version 18.

import { IconType, ComposeListItem, SymbolGlyphModifier } from '@kit.ArkUI';
@Entry
@Component
struct ComposeListItemExample {
  build() {
    Column() {
      List() {
        ListItem() {
          ComposeListItem({
            contentItem: ({
              iconStyle: IconType.NORMAL\_ICON,
              icon: $r('sys.symbol.house'),
              primaryText: 'Double-line list',
              secondaryText: 'Secondary text',
              description: 'Description'
            }),
            operateItem: ({
              image: $r('sys.symbol.car'),
            })
          })
        }

        ListItem() {
          ComposeListItem({
            contentItem: ({
              iconStyle: IconType.NORMAL\_ICON,
              icon: $r('sys.symbol.house'),
              symbolStyle: new SymbolGlyphModifier($r('sys.symbol.bell')).fontColor(\[Color.Red\]),
              primaryText: 'Double-line list',
              secondaryText: 'Secondary text',
              description: 'Description'
            }),
            operateItem: ({
              image: $r('sys.symbol.car'),
              symbolStyle: new SymbolGlyphModifier($r('sys.symbol.heart')).fontColor(\[Color.Pink\]),
            })
          })
        }

        ListItem() {
          ComposeListItem({
            contentItem: ({
              iconStyle: IconType.NORMAL\_ICON,
              icon: $r('sys.symbol.house'),
              symbolStyle: new SymbolGlyphModifier($r('sys.symbol.bell')).fontColor(\[Color.Blue\]),
              primaryText: 'Double-line list',
              secondaryText: 'Secondary text',
              description: 'Description'
            }),
            operateItem: ({
              icon: {
                value: $r('sys.symbol.car'),
                symbolStyle: new SymbolGlyphModifier($r('sys.symbol.heart')).fontColor(\[Color.Orange\]),
                action: () => {
                  this.getUIContext().getPromptAction().showToast({
                    message: 'icon'
                  });
                }
              }
            })
          })
        }
      }
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/m-QKq9HfQRyvnZvaFoU48g/en-us_image_0000002568765689.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062250Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CBC9AA8848A3DE813BAD8130F46D111BD52C3004CC395C163E08B78CD207D951)
