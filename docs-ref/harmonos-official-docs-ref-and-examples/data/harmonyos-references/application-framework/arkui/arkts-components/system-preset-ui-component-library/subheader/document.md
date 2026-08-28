# SubHeader

The **SubHeader** component is positioned at the top of list items or content sections, organizing lists or content into distinct groups. The subheader text summarizes the content within each respective section.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/RHcbxNwpRNK4vQhhTovTYA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062251Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D13FF9E9B5D0B5A3B4BF35D4481BF1AC352559FD1D36E45E6AADF699774C713F)

This component is supported since API version 10. Updates will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { SubHeader } from '@kit.ArkUI';

#### Child Components

Not supported

#### Attributes

The [universal attributes](../../universal-attributes/document.md) are not supported.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/t99q1a3SQ1SA-pnomwQAig/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062251Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B50A240AC9B85B234CA1BEEE17061A893C05996534767CE3C1CE902486A03F38)

Text-related settings are not supported.

#### SubHeader

SubHeader({icon?: ResourceStr, iconSymbolOptions?: SymbolOptions, primaryTitle?: ResourceStr, secondaryTitle?: ResourceStr, select?: SelectOptions, operationType?: OperationType, operationItem?: Array<OperationOption>, operationSymbolOptions?: Array<SymbolOptions>, primaryTitleModifier?: TextModifier, secondaryTitleModifier?: TextModifier, titleBuilder?: () => void, contentMargin?: LocalizedMargin, contentPadding?: LocalizedPadding})

**Decorator**: @Component

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Type | Mandatory | Decorator | Description |
| :-- | :-- | :-- | :-- | :-- |
| icon | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | @Prop | 
Icon.

The **icon** attribute takes effect only when the **secondaryTitle** attribute is used.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| iconSymbolOptions12+ | [SymbolOptions](#symboloptions12) | No | \- | 

Icon symbol options. This parameter is available when **icon** is set to a [symbol glyph](../../text-and-input/symbolglyph/document.md).

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| primaryTitle | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | @Prop | 

Primary title.

When the **primaryTitle**, **secondaryTitle**, and **icon** attributes are used simultaneously, the **primaryTitle** attribute will not take effect.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| secondaryTitle | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | @Prop | 

Secondary title.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| select | [SelectOptions](#selectoptions) | No | \- | 

Content and events for selection.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| operationType | [OperationType](#operationtype) | No | @Prop | 

Style of elements in the operation area (right).

Default value: **OperationType.BUTTON**

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| operationItem | Array<[OperationOption](#operationoption)\> | No | \- | 

Items in the operation area (right).

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| operationSymbolOptions12+ | Array<[SymbolOptions](#symboloptions12)\> | No | \- | 

Icon symbol options.

This parameter is available when **operationType** is set to **OperationType.ICON\_GROUP** and **operationItem** is set to an array of [symbol glyphs](../../text-and-input/symbolglyph/document.md).

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| primaryTitleModifier12+ | [TextModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#custom-modifier) | No | \- | 

Text attributes of the primary title, such as the font color, font size, and font weight.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| secondaryTitleModifier12+ | [TextModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#custom-modifier) | No | \- | 

Text attributes of the secondary title, such as the font color, font size, and font weight.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| titleBuilder12+ | () => void | No | @BuilderParam | 

Content of the custom title area.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| contentMargin12+ | [LocalizedMargin](../../common-definitions/basic-types/document.md#localizedmargin12) | No | @Prop | 

Margin of the content. Negative numbers are not supported.

Default value:

{start: LengthMetrics.resource(

$r('sys.float.margin\_left')),

end: LengthMetrics.resource(

$r('sys.float.margin\_right'))}

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| contentPadding12+ | [LocalizedPadding](../../common-definitions/basic-types/document.md#localizedpadding12) | No | @Prop | 

Padding of the content.

Default value:

If a secondary title, with or without an icon, is displayed on the left:

{start: LengthMetrics.vp(12), end: LengthMetrics.vp(12)}

**Atomic service API**: This API can be used in atomic services since API version 12.

 |

#### OperationType

Defines the style of elements in the subheader operation area.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Value | Description |
| :-- | :-- | :-- |
| TEXT\_ARROW | 0 | Text button with a right arrow. |
| BUTTON | 1 | Text button without a right arrow. |
| ICON\_GROUP | 2 | Icon-attached button (A maximum of three icons can be configured.) |
| LOADING | 3 | Loading animation. |

#### SelectOptions

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| options | Array<[SelectOption](../../buttons-and-selections/select/document.md#selectoption)\> | No | No | 
Options of an item in the drop-down list box.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| selected | number | No | Yes | 

Index of the initially selected item in the drop-down list box.

The value must be greater than or equal to -1.

The index of the first item is 0.

If this attribute is not set, the default value **\-1** is used, indicating that the option is not selected.

Values less than -1 are treated as no selection.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| value | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 

Text content of the drop-down list button itself.

The default value is an empty string.

Note: If the text length exceeds the column width, it will be truncated. The Resource type is supported since API version 20.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| onSelect | (index: number, value?: string) => void | No | Yes | 

Callback invoked when an item in the drop-down list box is selected.

\- **index**: index of the selected option.

\- **value**: value of the selected option.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| defaultFocus18+ | boolean | No | Yes | 

Whether the drop-down button is the default focus.

**true**: The drop-down button is the default focus.

**false**: The drop-down button is not the default focus.

Default value: **false**

**Atomic service API**: This API can be used in atomic services since API version 18.

 |

#### OperationOption

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| value | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | No | 
Text content.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| action | ()=>void | No | Yes | 

Right-side button click event.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| accessibilityLevel18+ | string | No | Yes | 

Accessibility level. It determines whether the component can be recognized by accessibility services.

The options are as follows:

**"auto"**: This option is treated as "yes" by the system for this component.

**"yes"**: The component can be recognized by accessibility services.

**"no"**: The component cannot be recognized by accessibility services.

**"no-hide-descendants"**: Neither the component nor its child components can be recognized by accessibility services.

Default value: **"auto"**

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| accessibilityText18+ | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 

Accessibility text, that is, accessible label name. If a component does not contain text information, it will not be announced by the screen reader when selected. In this case, the screen reader user cannot know which component is selected. To solve this problem, you can set accessibility text for components without text information. When such a component is selected, the screen reader announces the specified accessibility text, informing the user which component is selected.

Default value: value of the **value** property if the operation type is **TEXT\_ARROW** or **BUTTON** and an empty string otherwise.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| accessibilityDescription18+ | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 

Accessible description. You can provide comprehensive text explanations to help users understand the operation they are about to perform and its potential consequences, especially when these cannot be inferred from the component's attributes and accessibility text alone. If a component contains both text information and the accessible description, the text is announced first and then the accessible description, when the component is selected.

Default value: "Loading" when the operation type is **LOADING** and **"Double-tap to activate"** otherwise.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| defaultFocus18+ | boolean | No | Yes | 

Whether to receive default focus.

**true**: Receive default focus.

**false**: Do not receive default focus.

Default value: **false**

**Atomic service API**: This API can be used in atomic services since API version 18.

 |

#### SymbolOptions12+

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| fontColor | Array<[ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor)\> | No | Yes | 
Color of the [symbol glyph](../../text-and-input/symbolglyph/document.md).

Default value: depending on the rendering strategy

 |
| fontSize | number | string | [Resource](../../common-definitions/basic-types/document.md#resource) | No | Yes | 

Size of the [symbol glyph](../../text-and-input/symbolglyph/document.md).

For the number type, the value must be greater than or equal to 0.

For the string type, numeric string values with optional units, for example, **"10"** or **"10fp"**, are supported.

Default value: system default value

 |
| fontWeight | number | [FontWeight](../../common-definitions/enums/document.md#fontweight) | string | No | Yes | 

Weight of the [symbol glyph](../../text-and-input/symbolglyph/document.md).

For the number type, the value ranges from 100 to 900, at an interval of 100. A larger value indicates a heavier font weight. The default value is **400**.

For the string type, only strings of the number type are supported, for example, **"400"**, **"bold"**, **"bolder"**, **"lighter"**, **"regular"**, and **"medium"**, which correspond to the enumerated values in **FontWeight**.

Default value: **FontWeight.Normal**.

 |
| renderingStrategy | [SymbolRenderingStrategy](../../text-and-input/symbolglyph/document.md#symbolrenderingstrategy11) | No | Yes | 

Rendering strategy of the [symbol glyph](../../text-and-input/symbolglyph/document.md).

Default value: **SymbolRenderingStrategy.SINGLE**.

**NOTE**

For the resources referenced in **$r('sys.symbol.ohos\_\*')**, only **ohos\_trash\_circle**, **ohos\_folder\_badge\_plus**, and **ohos\_lungs** support the **MULTIPLE\_COLOR** modes.

 |
| effectStrategy | [SymbolEffectStrategy](../../text-and-input/symbolglyph/document.md#symboleffectstrategy11) | No | Yes | 

Effect strategy of the [symbol glyph](../../text-and-input/symbolglyph/document.md).

Default value: **SymbolEffectStrategy.NONE**.

**NOTE**

For the resources referenced in **$r('sys.symbol.ohos\_\*')**, only **ohos\_wifi** supports the hierarchical effect.

 |

#### Events

The [universal events](../../universal-events/document.md) are not supported.

#### Example

## Example 1: Implementing an Efficiency-oriented Subheader

This example demonstrates how to implement a subheader where the left side contains an icon and a secondary title, and the right side has a text button.

import { Prompt, OperationType, SubHeader } from '@kit.ArkUI';

@Entry
@Component
struct SubHeaderExample {
  build() {
    Column() {
      SubHeader({
        icon: $r('sys.media.ohos\_ic\_public\_email'),
        secondaryTitle: 'Secondary title',
        operationType: OperationType.BUTTON,
        operationItem: \[{
          value: 'Operation',
          action: () => {
            Prompt.showToast({ message: 'demo' });
          }
        }\]
      })
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/fmNei-ZkTYaqgyC6y06DwA/en-us_image_0000002568765719.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062251Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=24B981FDF7562DC9905431A28F02CA35AB1B8A2329EC0941277F6BB3C15FAC7D)

## Example 2: Implementing a Double-Line Text Content-Rich Subheader

This example showcases a subheader with a primary title and a secondary title on the left, and a text button with a right arrow on the right.

import { Prompt, OperationType, SubHeader } from '@kit.ArkUI';

@Entry
@Component
struct SubHeaderExample {
  build() {
    Column() {
      SubHeader({
        primaryTitle: 'Title',
        secondaryTitle: 'Secondary title',
        operationType: OperationType.TEXT\_ARROW,
        operationItem: \[{
          value: 'More',
          action: () => {
            Prompt.showToast({ message: 'demo' });
          }
        }\]
      })
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/Sri9uitMQumM3E7uH2Yx8Q/en-us_image_0000002537765994.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062251Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=236AAD8C7994D3A057A8EB1E0091F0125ED9F4730A9B91DB1E1C1B3F66944E52)

## Example 3: Implementing a Spinner Content-Rich Subheader

This example showcases a subheader with content and events for selection on the left, and an icon-attached button on the right.

import { Prompt, OperationType, SubHeader } from '@kit.ArkUI';

@Entry
@Component
struct SubHeaderExample {
  build() {
    Column() {
      SubHeader({
        // The left side is a drop-down box for selection.
        select: {
          options: \[{ value: 'aaa' }, { value: 'bbb' }, { value: 'ccc' }\],
          value: 'selectDemo',
          selected: 2,
          onSelect: () => {
            Prompt.showToast({ message: 'demo' });
          }
        },
        operationType: OperationType.ICON\_GROUP,
        // The right side has three icons.
        operationItem: \[{
          value: $r('sys.media.ohos\_ic\_public\_email'),
          action: () => {
            Prompt.showToast({ message: 'demo' })
          }
        }, {
          value: $r('sys.media.ohos\_ic\_public\_email'),
          action: () => {
            Prompt.showToast({ message: 'demo' });
          }
        }, {
          value: $r('sys.media.ohos\_ic\_public\_email'),
          action: () => {
            Prompt.showToast({ message: 'demo' });
          }
        }\]
      })
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/v6FAX3FZTji0fseEhRFcGg/en-us_image_0000002537925934.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062251Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=ECE44EC0EFC2E988F12B96547BA18AB9E2007B929CAA5B9DC52EF3D53CDC4A57)

## Example 4: Setting the Icon Symbol for the Left Side

This example demonstrates how to set the icon symbol for the left side of the subheader.

import { Prompt, OperationType, SubHeader } from '@kit.ArkUI';

@Entry
@Component
struct SubHeaderExample {
  build() {
    Column() {
      SubHeader({
        // Set the icon to a symbol icon.
        icon: $r('sys.symbol.ohos\_wifi'),
        iconSymbolOptions: {
          effectStrategy: SymbolEffectStrategy.HIERARCHICAL,
        },
        secondaryTitle: 'Title',
        operationType: OperationType.BUTTON,
        operationItem: \[{
          value: 'Operation',
          action: () => {
            Prompt.showToast({ message: 'demo' });
          }
        }\]
      })
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/lIkfw2cPSJK20SjYdF7p2w/en-us_image_0000002568685711.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062251Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6A8CB19A0AD3C9224BCC9A80D150632002E6B5915AC8CE21BCB222980390ED6A)

## Example 5: Setting the Icon Symbol for the Right Side

The following example shows how to set **operationType** to **OperationType.ICON\_GROUP** for the right side of the subheader, with **operationItem** set to a symbol icon.

import { Prompt, OperationType, SubHeader } from '@kit.ArkUI';

@Entry
@Component
struct SubHeaderExample {
  build() {
    Column() {
      SubHeader({
        // Set the left side to a drop-down box for selection.
        select: {
          options: \[{ value: 'aaa' }, { value: 'bbb' }, { value: 'ccc' }\],
          value: 'selectDemo',
          selected: 2,
          onSelect: () => {
            Prompt.showToast({ message: 'demo' });
          }
        },
        operationType: OperationType.ICON\_GROUP,
        // Set the right side to icons.
        operationItem: \[{
          value: $r('sys.symbol.ohos\_lungs'),
          action: () => {
            Prompt.showToast({ message: 'icon1' });
          }
        }, {
          value: $r('sys.symbol.ohos\_lungs'),
          action: () => {
            Prompt.showToast({ message: 'icon2' });
          }
        }, {
          value: $r('sys.symbol.ohos\_lungs'),
          action: () => {
            Prompt.showToast({ message: 'icon3' });
          }
        }\],
        // Set the symbol style for the right side icons.
        operationSymbolOptions: \[{
          fontWeight: FontWeight.Lighter,
        }, {
          renderingStrategy: SymbolRenderingStrategy.MULTIPLE\_COLOR,
          fontColor: \[Color.Blue, Color.Grey, Color.Green\],
        }, {
          renderingStrategy: SymbolRenderingStrategy.MULTIPLE\_OPACITY,
          fontColor: \[Color.Blue, Color.Grey, Color.Green\],
        }\]
      })
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/_jDkZ1fRSiOKubhg_aqtAg/en-us_image_0000002568765721.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062251Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=53AA9947A0D70157F449ABB21F3E644197AA4C9A5507BE1A541B51B61133E2D1)

## Example 6: Customizing Title Content

This example demonstrates how to customize the title content with a **titleBuilder** object for the subheader.

import { Prompt, OperationType, SubHeader } from '@kit.ArkUI';

@Entry
@Component
struct SubHeaderExample {
  // Set the custom title on the left side.
  @Builder
  TitleBuilder(): void {
    Text('Custom title')
      .fontSize(24)
      .fontColor(Color.Blue)
      .fontWeight(FontWeight.Bold)
  }

  build() {
    Column() {
      SubHeader({
        // Call the custom title builder.
        titleBuilder: () => {
          this.TitleBuilder();
        },
        primaryTitle: 'Primary title',
        secondaryTitle: 'Secondary title',
        icon: $r('sys.symbol.ohos\_star'),
        operationType: OperationType.TEXT\_ARROW,
        operationItem: \[{
          value: 'More info',
          action: () => {
            Prompt.showToast({ message: 'demo' });
          }
        }\]
      })
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/-06XGcFgQeuWuINMI_UBNQ/en-us_image_0000002537765996.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062251Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2276E2B08962EFBDA12D6CA8CEBC9BB38CC9C3FED75EE355786AB082FB5C6BB9)

## Example 7: Customizing the Title Style

This example demonstrates how to set the font style, margin, and padding for the primary and secondary titles in the subheader.

import { Prompt, OperationType, SubHeader, LengthMetrics, TextModifier } from '@kit.ArkUI';

@Entry
@Component
struct SubHeaderExample {
  // Set the font color for the primary and secondary titles.
  @State primaryModifier: TextModifier = new TextModifier().fontColor(Color.Blue);
  @State secondaryModifier: TextModifier = new TextModifier().fontColor(Color.Blue);

  build() {
    Column() {
      SubHeader({
        primaryTitle: 'primaryTitle',
        secondaryTitle: 'secondaryTitle',
        primaryTitleModifier: this.primaryModifier,
        secondaryTitleModifier: this.secondaryModifier,
        operationType: OperationType.TEXT\_ARROW,
        operationItem: \[{
          value: 'More info',
          action: () => {
            Prompt.showToast({ message: 'demo' });
          }
        }\],
        // Set the margin and padding for the subheader.
        contentMargin: { start: LengthMetrics.vp(20), end: LengthMetrics.vp(20) },
        contentPadding: { start: LengthMetrics.vp(20), end: LengthMetrics.vp(20) }
      })
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/duzcZkRbSlONbOJCJl9YgQ/en-us_image_0000002537925936.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062251Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6FC9150388C66F38E41445A1D3CFF9DD2BCACB480E61656A87260E7FE56C5A29)

## Example 8: Implementing Announcement for the Button on the Right Side

This example customizes the screen reader announcement text by setting the **accessibilityText**, **accessibilityDescription**, and **accessibilityLevel** properties of the button on the right side of the **SubHeader** component. This functionality is supported since API version 18.

import { Prompt, OperationType, SubHeader } from '@kit.ArkUI';

@Entry
@Component
struct SubHeaderExample {
  build() {
    Column() {
      Divider().color('grey').width('100%').height('2vp')
      SubHeader({
        // Icon + secondary title, with a button on the right
        icon: $r('sys.media.ohos\_ic\_public\_email'),
        secondaryTitle: 'Secondary title',
        operationType: OperationType.BUTTON,
        operationItem: \[{
          value: 'Operation',
          action: () => {
            Prompt.showToast({ message: 'demo' })
          }
        }\]
      })
      Divider().color('grey').width('100%').height('2vp')
      SubHeader({
        // Text button with a right-side arrow
        primaryTitle: 'Primary title',
        secondaryTitle: 'Secondary title',
        operationType: OperationType.TEXT\_ARROW,
        operationItem: \[{
          value: 'More',
          action: () => {
            Prompt.showToast({ message: 'demo' })
          }
        }\]
      })
      Divider().color('grey').width('100%').height('2vp')
      SubHeader({
        // Selection on the left and icons (focused in sequence) on the right
        select: {
          options: \[{ value: 'aaa' }, { value: 'bbb' }, { value: 'ccc' }\],
          value: 'selectDemo',
          selected: 0,
          onSelect: (index: number, value?: string) => {
            console.info(\`SubHeader onSelect index : ${index}, value: ${value}\`);
          }
        },
        operationType: OperationType.ICON\_GROUP,
        operationItem: \[{
          value: $r('sys.media.ohos\_ic\_public\_email'),
          accessibilityText: 'Icon 1',
          accessibilityLevel: 'yes',
        }, {
          value: $r('sys.media.ohos\_ic\_public\_email'),
          accessibilityText: 'Icon 2',
          accessibilityLevel: 'no',
        }, {
          value: $r('sys.media.ohos\_ic\_public\_email'),
          accessibilityText: 'Icon 3',
          accessibilityDescription: 'Tap to operate icon 3',
        }\]
      })
      Divider().color('grey').width('100%').height('2vp')
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/i2znb7xaQZibBF99OLMzdQ/en-us_image_0000002568685713.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062251Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E18C172DD17FA8F55D1AF0278CB936A59C44348A88F18FEF1C4B2B3434BAAF59)

## Example 9: Setting the Right-Side Button to Obtain Focus by Default

This example demonstrates how to set the **defaultFocus** attribute in **SubHeader** to ensure the right-side button obtains focus by default in the focused state.

The **defaultFocus** API is added to [OperationOption](#operationoption) since API version 18.

import { Prompt, OperationType, SubHeader } from '@kit.ArkUI';

@Entry
@Component
struct SubHeaderExample {
  build() {
    Column() {
      SubHeader({
        // Icon + secondary title, with a button on the right
        icon: $r('sys.media.ohos\_ic\_public\_email'),
        secondaryTitle: 'Secondary title',
        operationType: OperationType.BUTTON,
        operationItem: \[{
          value: 'Operation',
          defaultFocus: true,
          action: () => {
            Prompt.showToast({ message: 'demo' })
          }
        }\]
      })
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/0fNyvmRpSgWoNbgRUuNzsA/en-us_image_0000002568765723.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062251Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=986889A53D6D5443A5E9C7F04ED7A470C5EBE899E1C3BF931F39421B337A01F8)
