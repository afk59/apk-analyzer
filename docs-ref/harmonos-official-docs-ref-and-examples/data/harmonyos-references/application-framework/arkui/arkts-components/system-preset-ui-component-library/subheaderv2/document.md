# SubHeaderV2

The **SubHeader** component is positioned at the top of list items or content sections, organizing lists or content into distinct groups. The subheader text summarizes the content within each respective section.

This component is implemented based on [state management V2](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-state-management-overview#state-management-v2). Compared with [state management V1](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-state-management-overview#state-management-v1), V2 offers a higher level of observation and management over data objects beyond the component level. You can now more easily manage subheader data and states with greater flexibility, leading to faster UI updates.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/2zvii0lZSiaFn9Uwdse-XA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062251Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=16464385DEAC8434C196A2AAC5E48E8FE3F46DEFEF97309EB14FB1A8F8AA1C7C)

-   This component is supported since API version 18. Updates will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { SubHeaderV2 } from '@kit.ArkUI';

#### Child Components

Not supported

#### Attributes

The [universal attributes](../../universal-attributes/document.md) are not supported.

#### SubHeaderV2

SubHeaderV2({ icon?: SubHeaderV2IconType, title?: SubHeaderV2Title, select?: SubHeaderV2Select, operationType?: SubHeaderV2OperationType, operationItems?: SubHeaderV2OperationItem\[\], titleBuild?: SubHeaderV2TitleBuilder; })

The **SubHeader** component represents a subheader that signifies the top of a list or the beginning a subdivision of content and tells the user what the list or subdivision is about.

**Decorator**: @ComponentV2

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Type | Mandatory | Decorator | Description |
| :-- | :-- | :-- | :-- | :-- |
| icon | [SubHeaderV2IconType](#subheaderv2icontype) | No | @Param | 
Icon.

Default value: **undefined**

The **icon** attribute takes effect only when the **secondaryTitle** attribute is used for **title**.

 |
| title | [SubHeaderV2Title](#subheaderv2title) | No | @Param | 

Title of the subheader.

Default value: **undefined**

 |
| select | [SubHeaderV2Select](#subheaderv2select) | No | @Param | 

Content and events for selection.

Default value: **undefined**

 |
| operationType | [SubHeaderV2OperationType](#subheaderv2operationtype) | No | @Param | 

Style of elements in the operation area.

Default value: **SubHeaderV2OperationType.BUTTON**

 |
| operationItems | [SubHeaderV2OperationItem](#subheaderv2operationitem)\[\] | No | @Param | 

Items in the operation area.

Default value: **undefined**

 |
| titleBuilder | [SubHeaderV2TitleBuilder](#subheaderv2titlebuilder) | No | @BuilderParam | 

Custom content for the title area.

Default value: **() => void**

 |

#### SubHeaderV2IconType

type SubHeaderV2IconType = ResourceStr | SymbolGlyphModifier

Defines the union type for the icon content.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Type | Description |
| :-- | :-- |
| [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | Resource type for defining common icons. |
| [SymbolGlyphModifier](../../universal-attributes/modifiers-and-custom-property/symbol-glyph-modifier/document.md#symbolglyphmodifier) | Symbol type for defining symbol icons. |

#### SubHeaderV2Title

Defines the title settings for the subheader.

**Decorator**: @ObservedV2

#### \[h2\]Properties

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| primaryTitle | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 
Primary title.

When the **primaryTitle**, **secondaryTitle**, and **icon** attributes are used simultaneously in [SubHeaderV2](#subheaderv2-1), the **primaryTitle** attribute will not take effect.

Default value: **undefined**

Decorator: @Trace

 |
| secondaryTitle | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 

Secondary title.

Default value: **undefined**

Decorator: @Trace

 |
| primaryTitleModifier | [TextModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#custom-modifier) | No | Yes | 

Text attributes of the primary title, such as the font color, font size, and font weight.

Default value: **undefined**

Decorator: @Trace

 |
| secondaryTitleModifier | [TextModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#custom-modifier) | No | Yes | 

Text attributes of the secondary title, such as the font color, font size, and font weight.

Default value: **undefined**

Decorator: @Trace

 |

#### \[h2\]constructor

constructor(options: SubHeaderV2TitleOptions)

A constructor used to create a **SubHeaderV2Title** object.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [SubHeaderV2TitleOptions](#subheaderv2titleoptions) | Yes | Options for initializing the title. |

#### SubHeaderV2TitleOptions

Defines the options for initializing a **SubHeaderV2Title** object.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| primaryTitle | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 
Primary title.

Default value: **undefined**

 |
| secondaryTitle | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 

Secondary title.

Default value: **undefined**

 |
| primaryTitleModifier | [TextModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#custom-modifier) | No | Yes | 

Text attributes of the primary title, such as the font color, font size, and font weight.

Default value: **undefined**

 |
| secondaryTitleModifier | [TextModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#custom-modifier) | No | Yes | 

Text attributes of the secondary title, such as the font color, font size, and font weight.

Default value: **undefined**

 |

#### SubHeaderV2Select

Defines the content and events for selection.

**Decorator**: @ObservedV2

#### \[h2\]Properties

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| options | [SelectOption](../../buttons-and-selections/select/document.md#selectoption)\[\] | No | No | 
Options for the drop-down list box.

Decorator: @Trace

 |
| selectedIndex | number | No | Yes | 

Index of the initially selected item in the drop-down list box.

The index of the first item is 0.

If this property is not set, the default value **\-1** is used, indicating that no item is selected.

Decorator: @Trace

 |
| selectedContent | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 

Text content of the drop-down button. Default value: **''**. The Resource type is supported since API version 20.

Decorator: @Trace

 |
| onSelect | [SubHeaderV2SelectOnSelect](#subheaderv2selectonselect) | No | Yes | 

Callback invoked when an item in the drop-down list box is selected.

Default value: **undefined**

Decorator: @Trace

 |
| defaultFocus | boolean | No | Yes | 

Whether the drop-down button is the default focus.

**true**: The drop-down button is the default focus.

**false**: The drop-down button is not the default focus.

Default value: **false**

Decorator: @Trace

 |

#### \[h2\]constructor

constructor(options: SubHeaderV2SelectOptions)

A constructor used to create a **SubHeaderV2SelectOptions** object.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [SubHeaderV2SelectOptions](#subheaderv2selectoptions) | Yes | Options of the drop-down list box. |

#### SubHeaderV2SelectOptions

Defines the options for initializing a **SubHeaderV2Select** object.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| options | [SelectOption](../../buttons-and-selections/select/document.md#selectoption)\[\] | No | No | Options for the drop-down list box. |
| selectedIndex | number | No | Yes | 
Index of the initially selected item in the drop-down list box.

The index of the first item is 0.

If this property is not set, the default value **\-1** is used, indicating that no item is selected.

 |
| selectedContent | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | Text content of the drop-down button. Default value: **''**. The Resource type is supported since API version 20. |
| onSelect | [SubHeaderV2SelectOnSelect](#subheaderv2selectonselect) | No | Yes | 

Callback invoked when an item in the drop-down list box is selected.

Default value: **undefined**

 |
| defaultFocus | boolean | No | Yes | 

Whether the drop-down button is the default focus.

**true**: The drop-down button is the default focus.

**false**: The drop-down button is not the default focus.

Default value: **false**

 |

#### SubHeaderV2SelectOnSelect

type SubHeaderV2SelectOnSelect = (selectedIndex: number, selectedContent?: string) => void

Defines the callback invoked when an item in the drop-down list box is selected.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| selectedIndex | number | Yes | Callback invoked when an item in the drop-down list box is selected. Index of the selected item. |
| selectedContent | string | No | Callback invoked when an item in the drop-down list box is selected. Value of the selected item. |

#### SubHeaderV2OperationType

Defines the style of elements in the operation area.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Value | Description |
| :-- | :-- | :-- |
| TEXT\_ARROW | 0 | Text button with a right arrow. |
| BUTTON | 1 | Text button without a right arrow. |
| ICON\_GROUP | 2 | Icon-attached button (A maximum of three icons can be configured.) |
| LOADING | 3 | Loading animation. |

#### SubHeaderV2OperationItemType

type SubHeaderV2OperationItemType = ResourceStr | SymbolGlyphModifier

Defines the union type for the content of elements in the operation area.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Type | Description |
| :-- | :-- |
| [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | String type for defining text display or common icons; resource type for defining common icons. |
| [SymbolGlyphModifier](../../universal-attributes/modifiers-and-custom-property/symbol-glyph-modifier/document.md#symbolglyphmodifier) | Symbol type for defining symbol icons. |

#### SubHeaderV2OperationItem

Represents an item in the operation area.

**Decorator**: @ObservedV2

#### \[h2\]Properties

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| content | [SubHeaderV2OperationItemType](#subheaderv2operationitemtype) | No | No | 
Content of the item in the operation area.

Decorator: @Trace

 |
| action | [SubHeaderV2OperationItemAction](#subheaderv2operationitemaction) | No | Yes | 

Event triggered when the item is operated. Default value: **() => void**

Decorator: @Trace

 |
| accessibilityText | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 

Accessibility text of the icon on the right side of the subheader.

Default value: **undefined**

Decorator: @Trace

 |
| accessibilityLevel | string | No | Yes | 

Accessibility level of the icon on the right side of the subheader.

The options are as follows:

**"auto"**: The icon's recognizability by accessibility services is determined by the accessibility grouping service and ArkUI.

**"yes"**: The icon can be recognized by accessibility services.

**"no"**: The icon cannot be recognized by accessibility services.

**"no-hide-descendants"**: Neither the icon nor its child components can be recognized by accessibility services.

Default value: **"yes"**

Decorator: @Trace

 |
| accessibilityDescription | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 

Accessibility description.

Default value: **"Double-tap to activate"**

Decorator: @Trace

 |
| defaultFocus | boolean | No | Yes | 

Whether to receive default focus.

**true**: Receive default focus.

**false**: Do not receive default focus.

Default value: **false**

Decorator: @Trace

 |

#### \[h2\]constructor

constructor(options: SubHeaderV2OperationItemOptions)

A constructor used to create a **SubHeaderV2OperationItem** object.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [SubHeaderV2OperationItemOptions](#subheaderv2operationitemoptions) | Yes | Options of the drop-down list box. |

#### SubHeaderV2OperationItemAction

type SubHeaderV2OperationItemAction = () => void

Defines the callback for items in the operation area.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

#### SubHeaderV2OperationItemOptions

Defines the options for initializing a **SubHeaderV2OperationItem** object.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| content | [SubHeaderV2OperationItemType](#subheaderv2operationitemtype) | No | No | Content of the item in the operation area. |
| action | [SubHeaderV2OperationItemAction](#subheaderv2operationitemaction) | No | Yes | Event triggered when the item is operated. Default value: **() => void** |
| accessibilityText | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 
Accessibility text of the icon on the right side of the subheader.

Default value: **undefined**

 |
| accessibilityLevel | string | No | Yes | 

Accessibility level of the icon on the right side of the subheader.

The options are as follows:

**"auto"**: The icon's recognizability by accessibility services is determined by the accessibility grouping service and ArkUI.

**"yes"**: The icon can be recognized by accessibility services.

**"no"**: The icon cannot be recognized by accessibility services.

**"no-hide-descendants"**: Neither the icon nor its child components can be recognized by accessibility services.

Default value: **"yes"**

 |
| accessibilityDescription | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 

Accessibility description.

Default value: **"Double-tap to activate"**

 |
| defaultFocus | boolean | No | Yes | 

Whether to receive default focus.

**true**: Receive default focus.

**false**: Do not receive default focus.

Default value: **false**

 |

#### SubHeaderV2TitleBuilder

type SubHeaderV2TitleBuilder= () => void

Defines the callback used to customize the content of the title area.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

#### Events

The [universal events](../../universal-events/document.md) are not supported.

#### Example

## Example 1: Implementing an Efficiency-oriented Subheader

This example demonstrates how to implement a subheader where the left side contains an icon and a secondary title, and the right side has a text button.

import {
  SubHeaderV2OperationType,
  SubHeaderV2,
  SubHeaderV2Title,
  SubHeaderV2OperationItem,
  Prompt,
  TextModifier
} from '@kit.ArkUI';

@Entry
@ComponentV2
struct SubHeaderExample {
  @Local selectText: string = "TTTTT"
  @Local selectIndex: number = 2
  @Local flag: boolean = true;
  @Local index: number = 1;
  @Local primaryTitle: ResourceStr = 'Primary title';
  @Local secondaryTitle: ResourceStr = 'Secondary title';
  @Local subHeaderIcon: Resource = $r('sys.media.ohos\_ic\_public\_email');
  @Local title: SubHeaderV2Title = new SubHeaderV2Title({ primaryTitle: 'Primary title' });
  @Local primaryModifier: TextModifier = new TextModifier().fontColor(Color.Red);
  @Local secondaryModifier: TextModifier = new TextModifier().fontColor(Color.Red);
  @Local subHeaderOperationType: SubHeaderV2OperationType = SubHeaderV2OperationType.BUTTON;
  @Local operationItems: SubHeaderV2OperationItem\[\] = \[\];

  aboutToAppear(): void {
    this.title = new SubHeaderV2Title({
      primaryTitle: this.primaryTitle,
      secondaryTitle: this.secondaryTitle,
    });
    this.operationItems = \[new SubHeaderV2OperationItem({
      content: 'Operation',
      action: () => {
        Prompt.showToast({ message: 'demo2' })
      }
    })\]
  }

  build() {
    Column() {
      Column() {
        SubHeaderV2({
          icon: this.subHeaderIcon,
          title: this.title,
          operationType: this.subHeaderOperationType,
          operationItems: this.operationItems
        });
      }
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/3kLqx_4QQA6OLmUn0PaX7Q/en-us_image_0000002568765719.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062251Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=34E9C68FFE21E134F1E49BBA26937E76B8C5F915679ABCBBBADB781128D0C0AF)

## Example 2: Implementing a Double-Line Text Content-rich Subheader

This example showcases a subheader with a primary title and a secondary title on the left, and a text button with a right arrow on the right.

import {
  SubHeaderV2OperationType,
  SubHeaderV2,
  SubHeaderV2Title,
  SubHeaderV2OperationItem,
  Prompt,
  TextModifier
} from '@kit.ArkUI';

@Entry
@ComponentV2
struct SubHeaderExample {
  @Local title: SubHeaderV2Title = new SubHeaderV2Title({ primaryTitle: 'Primary title', secondaryTitle: 'Secondary title' });
  @Local primaryModifier: TextModifier = new TextModifier().fontColor(Color.Red);
  @Local secondaryModifier: TextModifier = new TextModifier().fontColor(Color.Red);
  @Local subHeaderOperationType: SubHeaderV2OperationType = SubHeaderV2OperationType.TEXT\_ARROW;
  @Local operationItems: SubHeaderV2OperationItem\[\] = \[\];

  aboutToAppear(): void {
    this.title = new SubHeaderV2Title({
      primaryTitle: 'Title',
      secondaryTitle: 'Secondary title'
    });
    this.operationItems = \[new SubHeaderV2OperationItem({
      content: 'More',
      action: () => {
        Prompt.showToast({ message: 'demo2' })
      }
    })\]
  }

  build() {
    Column() {
      Column() {
        SubHeaderV2({
          title: this.title,
          operationType: this.subHeaderOperationType,
          operationItems: this.operationItems
        });
      }
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/s3m5WXlETJGNqoSGeUSjlQ/en-us_image_0000002537765994.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062251Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=999A8D309683FBC6B7F11F082075054465EB380176421164D5C3FD116ECEE6AF)

## Example 3: Implementing a Spinner Content-rich Subheader

This example showcases a subheader with content and events for selection on the left, and an icon-attached button on the right.

import {
  SubHeaderV2,
  SubHeaderV2OperationType,
  SubHeaderV2OperationItem,
  SubHeaderV2Title,
  SubHeaderV2Select,
  Prompt
} from '@kit.ArkUI';

@Entry
@ComponentV2
struct SubHeaderExample {
  @Local selectedValue: string = 'aaa';
  @Local selectedIndex: number = 0;
  @Local title: SubHeaderV2Title = new SubHeaderV2Title({ primaryTitle: 'Primary title', secondaryTitle: 'Secondary title' });
  @Local operationItems: SubHeaderV2OperationItem\[\] = \[\];
  @Local select: SubHeaderV2Select =
    new SubHeaderV2Select({ options: \[{ value: 'aaa' }, { value: 'bbb' }, { value: 'ccc' }\] });

  aboutToAppear(): void {

    this.title = new SubHeaderV2Title({
      primaryTitle: 'Primary title',
      secondaryTitle: 'Secondary title'
    });

    this.selectedValue = 'selectDemo';
    this.select = new SubHeaderV2Select({
      options: \[{ value: 'aaa' }, { value: 'bbb' }, { value: 'ccc' }\],
      selectedContent: this.selectedValue,
      selectedIndex: this.selectedIndex,
      onSelect: (index: number, value?: string) => {
        Prompt.showToast({ message: 'selectDemo' })
      }
    })

    this.operationItems = \[
      new SubHeaderV2OperationItem({
        content: $r('sys.media.ohos\_ic\_public\_email'),
        action: () => {
          Prompt.showToast({ message: 'demo' })
        }
      }),
      new SubHeaderV2OperationItem({
        content: $r('sys.media.ohos\_ic\_public\_email'),
        action: () => {
          Prompt.showToast({ message: 'demo' })
        }
      }),
      new SubHeaderV2OperationItem({
        content: $r('sys.media.ohos\_ic\_public\_email'),
        action: () => {
          Prompt.showToast({ message: 'demo' })
        }
      })\]
  }

  build() {
    Column() {
      Column() {
        SubHeaderV2({
          select: this.select,
          operationType: SubHeaderV2OperationType.ICON\_GROUP,
          operationItems: this.operationItems
        })
      }
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/SCGUpLoXSa235nA-W1VeWQ/en-us_image_0000002537925934.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062251Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=89607A5D6E9438750FA70631085E9BD9C4BBB8A96EFB34DD3D802F3D0514BA26)

## Example 4: Setting the Icon Symbol for the Left Side

This example demonstrates how to set the icon symbol for the left side of the subheader.

import {
  SubHeaderV2,
  SubHeaderV2OperationType,
  SubHeaderV2OperationItem,
  SubHeaderV2Title,
  Prompt,
  SymbolGlyphModifier
} from '@kit.ArkUI';

@Entry
@ComponentV2
struct SubHeaderExample {
  @Local icon: SymbolGlyphModifier = new SymbolGlyphModifier($r('sys.symbol.ohos\_wifi'));

  aboutToAppear(): void {
    this.icon = new SymbolGlyphModifier($r('sys.symbol.ohos\_wifi')).fontSize(24);
    this.icon.effectStrategy(SymbolEffectStrategy.HIERARCHICAL)
  }

  build() {
    Column() {
      SubHeaderV2({
        icon: this.icon,
        title: new SubHeaderV2Title({ secondaryTitle: 'Title' }),
        operationType: SubHeaderV2OperationType.BUTTON,
        operationItems: \[new SubHeaderV2OperationItem({
          content: 'Operation',
          action: () => {
            Prompt.showToast({ message: 'demo' })
          }
        })\]
      })
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/h7AEXKtBQS6sJdVOnP1vfg/en-us_image_0000002568685711.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062251Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=756F7DCD8DC424B2C7F3C8E5A6ECC92DBBD4DC628997F3FF72CEAA990734758D)

## Example 5: Setting the Icon Symbol for the Right Side

The following example shows how to set **operationType** to **OperationType.ICON\_GROUP** for the right side of the subheader, with **operationItem** set to a symbol icon.

import {
  SubHeaderV2,
  SubHeaderV2OperationType,
  SubHeaderV2OperationItem,
  SubHeaderV2Title,
  SubHeaderV2Select,
  Prompt,
  SymbolGlyphModifier
} from '@kit.ArkUI';

@Entry
@ComponentV2
struct SubHeaderExample {
  @Local icon: SymbolGlyphModifier = new SymbolGlyphModifier($r('sys.symbol.ohos\_wifi'));
  @Local selectedValue: string = 'aaa';
  @Local selectedIndex: number = 2;
  @Local title: SubHeaderV2Title = new SubHeaderV2Title({ primaryTitle: 'Primary title', secondaryTitle: 'Secondary title' });
  @Local operationItem: SubHeaderV2OperationItem\[\] = \[\];
  @Local select: SubHeaderV2Select =
    new SubHeaderV2Select({ options: \[{ value: 'aaa' }, { value: 'bbb' }, { value: 'ccc' }\] });

  aboutToAppear(): void {
    this.icon = new SymbolGlyphModifier($r('sys.symbol.ohos\_wifi'));
    this.icon.effectStrategy(SymbolEffectStrategy.HIERARCHICAL);

    this.selectedValue = 'selectDemo';
    this.selectedIndex = 2;
    this.title = new SubHeaderV2Title({
      primaryTitle: 'Primary title',
      secondaryTitle: 'Secondary title'
    });
    this.select = new SubHeaderV2Select({
      options: \[{ value: 'aaa' }, { value: 'bbb' }, { value: 'ccc' }\],
      selectedContent: this.selectedValue,
      selectedIndex: this.selectedIndex,
      onSelect: (index: number, value?: string) => {
        Prompt.showToast({ message: 'demo' })
      }
    })

    this.operationItem = \[
      new SubHeaderV2OperationItem({
        content: new SymbolGlyphModifier($r('sys.symbol.ohos\_lungs')).fontWeight(FontWeight.Lighter),
        action: () => {
          Prompt.showToast({ message: 'demo1' })
        }
      }),
      new SubHeaderV2OperationItem({
        content: new SymbolGlyphModifier($r('sys.symbol.ohos\_lungs'))
          .renderingStrategy(SymbolRenderingStrategy.MULTIPLE\_COLOR)
          .fontColor(\[Color.Blue, Color.Grey, Color.Green\])
      ,
        action: () => {
          Prompt.showToast({ message: 'demo2' })
        }
      }),
      new SubHeaderV2OperationItem({
        content: new SymbolGlyphModifier($r('sys.symbol.ohos\_lungs'))
          .renderingStrategy(SymbolRenderingStrategy.MULTIPLE\_OPACITY)
          .fontColor(\[Color.Blue, Color.Grey, Color.Green\])
      ,
        action: () => {
          Prompt.showToast({ message: 'demo3' })
        }
      })\]
  }

  build() {
    Column() {
      SubHeaderV2({
        select: this.select,
        operationType: SubHeaderV2OperationType.ICON\_GROUP,
        operationItems: this.operationItem
      })
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/sWskJ5NPQnuScrpU3sy6XQ/en-us_image_0000002568765721.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062251Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AF59B7FC80D6F5E4C2EC08386BC317213B9BC5DA8140DE95B70C8E7E4979F607)

## Example 6: Customizing Title Content

This example demonstrates how to customize the title content with a **titleBuilder** object for the **SubHeaderV2** component.

import {
  SubHeaderV2,
  SubHeaderV2OperationType,
  SubHeaderV2OperationItem,
  SubHeaderV2Title,
  Prompt
} from '@kit.ArkUI';

@Entry
@ComponentV2
struct SubHeaderExample {
  @Local title: SubHeaderV2Title = new SubHeaderV2Title({ primaryTitle: 'Primary title' });
  @Local operationItem: SubHeaderV2OperationItem\[\] = \[\];

  aboutToAppear(): void {
    this.title = new SubHeaderV2Title({
      primaryTitle: 'Primary title',
      secondaryTitle: 'Secondary title'
    });
    this.operationItem = \[new SubHeaderV2OperationItem({
      content: 'More info',
      action: () => {
        Prompt.showToast({ message: 'demo' })
      }
    })\]
  }

  @Builder
  TitleBuilder(): void {
    Text('Custom title')
      .fontSize(24)
      .fontColor(Color.Blue)
      .fontWeight(FontWeight.Bold)
  }

  build() {
    Column() {
      SubHeaderV2({
        titleBuilder: () => {
          this.TitleBuilder();
        },
        title: this.title,

        operationType: SubHeaderV2OperationType.TEXT\_ARROW,
        operationItems: this.operationItem
      })
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/cIbQvMktTuKk1ozYuvRcMg/en-us_image_0000002537765996.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062251Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E1DB96B831266A105FB11D62120FEF46E4F8F4BC64780BA82EED589BCB358A46)

## Example 7: Customizing the Title Style

This example demonstrates how to set custom font styles for the primary and secondary titles in the **SubHeaderV2** component.

import {
  SubHeaderV2,
  SubHeaderV2OperationType,
  SubHeaderV2OperationItem,
  SubHeaderV2Title,
  Prompt,
  TextModifier
} from '@kit.ArkUI';

@Entry
@ComponentV2
struct SubHeaderExample {
  @Local primaryModifier: TextModifier = new TextModifier().fontColor(Color.Blue);
  @Local secondaryModifier: TextModifier = new TextModifier().fontColor(Color.Blue);
  @Local title: SubHeaderV2Title = new SubHeaderV2Title({ primaryTitle: 'Primary title' });
  @Local operationItems4: SubHeaderV2OperationItem\[\] = \[\];

  aboutToAppear(): void {
    this.title = new SubHeaderV2Title({
      primaryTitle: 'Primary title',
      primaryTitleModifier: this.primaryModifier,
      secondaryTitle: 'Secondary title',
      secondaryTitleModifier: this.secondaryModifier
    });
    this.operationItems4 = \[new SubHeaderV2OperationItem({
      content: 'More info',
      action: () => {
        Prompt.showToast({ message: 'demo' })
      }
    })\]
  }

  build() {
    Column() {
      SubHeaderV2({
        title: this.title,
        operationType: SubHeaderV2OperationType.TEXT\_ARROW,
        operationItems: this.operationItems4
      })
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/-lSvrG8hQV-A1EASwPUi5w/en-us_image_0000002537765998.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062251Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C051571DD5088FC3BEFF453280326AEB8AAEBFBA726F5F1DD7E9659B23C0B47E)

## Example 8: Implementing Announcement for the Button on the Right Side

This example customizes the screen reader announcement text by setting the **accessibilityText**, **accessibilityDescription**, and **accessibilityLevel** properties of the button on the right side of the **SubHeaderV2** component.

import {
  SubHeaderV2OperationType,
  SubHeaderV2,
  SubHeaderV2Title,
  SubHeaderV2OperationItem,
  SubHeaderV2IconType,
  SubHeaderV2Select,
  Prompt
} from '@kit.ArkUI';

@Entry
@ComponentV2
struct SubHeaderExample {
  @Local index: number = 1;
  @Local primaryTitle: ResourceStr = 'Primary title';
  @Local secondaryTitle: ResourceStr = 'Secondary title';
  @Local subHeaderIcon: SubHeaderV2IconType | undefined = $r('sys.media.ohos\_ic\_public\_email');
  @Local title: SubHeaderV2Title = new SubHeaderV2Title({ primaryTitle: 'Primary title' });
  @Local title2: SubHeaderV2Title = new SubHeaderV2Title({ primaryTitle: 'Primary title', secondaryTitle: 'Secondary title' });
  @Local subHeaderOperationType: SubHeaderV2OperationType = SubHeaderV2OperationType.BUTTON;
  @Local subHeaderOperationType2: SubHeaderV2OperationType = SubHeaderV2OperationType.TEXT\_ARROW;
  @Local subHeaderOperationType3: SubHeaderV2OperationType = SubHeaderV2OperationType.ICON\_GROUP;
  @Local operationItems: SubHeaderV2OperationItem\[\] = \[\];
  @Local selectedValue: string | undefined = 'selectDemo';
  @Local selectedIndex: number = 0;
  @Local select: SubHeaderV2Select =
    new SubHeaderV2Select({ options: \[{ value: 'aaa' }, { value: 'bbb' }, { value: 'ccc' }\] });

  aboutToAppear(): void {
    this.select = new SubHeaderV2Select({ options: \[\] });
    this.title = new SubHeaderV2Title({
      primaryTitle: this.primaryTitle,
      secondaryTitle: this.secondaryTitle,
    });
    this.operationItems = \[new SubHeaderV2OperationItem({
      content: 'Operation',
      action: () => {
        Prompt.showToast({ message: 'demo2' })
      }
    })\]
  }

  build() {
    Column() {
      Column() {
        SubHeaderV2({
          icon: this.subHeaderIcon,
          title: this.title,
          select: this.select,
          operationType: this.subHeaderOperationType,
          operationItems: this.operationItems
        });
        Divider().color('grey').width('100%').height('2vp')
        SubHeaderV2({
          title: this.title2,
          select: this.select,
          operationType: this.subHeaderOperationType2,
          operationItems: this.operationItems
        });
        Divider().color('grey').width('100%').height('2vp')
        SubHeaderV2({
          select: new SubHeaderV2Select({
            options: \[{ value: 'aaa' }, { value: 'bbb' }, { value: 'ccc' }\],
            selectedIndex: this.selectedIndex,
            selectedContent: this.selectedValue,
            onSelect: (index: number, value?: string) => {
              this.selectedIndex = index;
              this.selectedValue = value;
              Prompt.showToast({ message: this.selectedValue })
            }
          }),
          operationType: this.subHeaderOperationType3,
          operationItems: \[new SubHeaderV2OperationItem({
            content: $r('sys.media.ohos\_ic\_public\_email'),
            accessibilityText: 'Icon 1',
            accessibilityLevel: 'yes',
          }), new SubHeaderV2OperationItem({
            content: $r('sys.media.ohos\_ic\_public\_email'),
            accessibilityText: 'Icon 2',
            accessibilityLevel: 'no',
          }), new SubHeaderV2OperationItem({
            content: $r('sys.media.ohos\_ic\_public\_email'),
            accessibilityText: 'Icon 3',
            accessibilityDescription: 'Tap to operate icon 3',
          })\]
        });
      }
      Divider().color('grey').width('100%').height('2vp')
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/sNfX7FEKT4SYe033D0eV2g/en-us_image_0000002568685713.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062251Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4B4EB63E7D13C56AC9450422CD55AE302F0C8CD9E1E131805B444631D0B7D065)

## Example 9: Setting the Right-Side Button to Obtain Focus by Default

This example demonstrates how to set the **defaultFocus** attribute in **SubHeaderV2** to ensure the right-side button obtains focus by default in the focused state.

The **defaultFocus** API is added to [SubHeaderV2OperationItem](#subheaderv2operationitemoptions) since API version 18.

import {
  SubHeaderV2OperationType,
  SubHeaderV2,
  SubHeaderV2Title,
  SubHeaderV2OperationItem,
  Prompt,
  TextModifier
} from '@kit.ArkUI';

@Entry
@ComponentV2
struct SubHeaderExample {
  @Local selectText: string = "TTTTT"
  @Local selectIndex: number = 2
  @Local flag: boolean = true;
  @Local index: number = 1;
  @Local primaryTitle: ResourceStr = 'Primary title';
  @Local secondaryTitle: ResourceStr = 'Secondary title';
  @Local subHeaderIcon: Resource = $r('sys.media.ohos\_ic\_public\_email');
  @Local title: SubHeaderV2Title = new SubHeaderV2Title({ primaryTitle: 'Primary title' });
  @Local primaryModifier: TextModifier = new TextModifier().fontColor(Color.Red);
  @Local secondaryModifier: TextModifier = new TextModifier().fontColor(Color.Red);
  @Local subHeaderOperationType: SubHeaderV2OperationType = SubHeaderV2OperationType.BUTTON;
  @Local operationItems: SubHeaderV2OperationItem\[\] = \[\];

  aboutToAppear(): void {
    this.title = new SubHeaderV2Title({
      secondaryTitle: this.secondaryTitle,
    });
    this.operationItems = \[new SubHeaderV2OperationItem({
      content: 'Action',
      defaultFocus: true,
      action: () => {
        Prompt.showToast({ message: 'demo2' })
      }
    })\]
  }

  build() {
    Column() {
      Column() {
        SubHeaderV2({
          icon: this.subHeaderIcon,
          title: this.title,
          operationType: this.subHeaderOperationType,
          operationItems: this.operationItems
        });
      }
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/98TbqYWpRR2iJedelBaGFQ/en-us_image_0000002568765723.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062251Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=34D45A7AA1E29DBD1D454B087F309EEF7A18F5E9E9ED543BEC6421514C87C865)
