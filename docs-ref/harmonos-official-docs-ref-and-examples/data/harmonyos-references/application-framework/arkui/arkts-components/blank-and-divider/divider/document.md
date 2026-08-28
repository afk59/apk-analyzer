# Divider

The **Divider** component is used to separate content blocks and content elements.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/KZhdAZ2MSNu058UyS9AjWg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=13D707C8D965EE6C80CB429B2A161E4491E52308D1E5EAA85CFD9D2815570EEC)

This component is supported since API version 7. Updates will be marked with a superscript to indicate their earliest API version.

If the divider appears with inconsistent thickness or becomes invisible, follow the instructions in [FAQs](../../universal-attributes/layout-and-borders/component-level-pixel-rounding/document.md#faqs).

#### Child Components

Not supported

#### APIs

Divider()

Creates a **Divider** component.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### Attributes

In addition to the [universal attributes](../../universal-attributes/document.md), the following attributes are supported.

#### \[h2\]vertical

vertical(value: boolean)

Sets the direction of the divider. This attribute can be dynamically set using [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier).

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | boolean | Yes | 
Whether the divider is vertical or horizontal.

**false**: A horizontal divider is used.

**true**: A vertical divider is used.

Default value: **false**

Invalid values are treated as the default value.

 |

#### \[h2\]color

color(value: ResourceColor)

Sets the color of the divider. This attribute can be dynamically set using [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier).

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | Yes | 
Color of the divider.

Default value: **'#33182431'**

Invalid values are treated as the default value.

You can set a common divider color using [WithTheme](../../themes/withtheme/document.md).

 |

#### \[h2\]strokeWidth

strokeWidth(value: number | string)

Sets the stroke width of the divider. This attribute can be dynamically set using [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier).

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | string | Yes | 
Stroke width of the divider.

Default value: **1px**

Invalid values are treated as the default value.

Unit: vp

**NOTE**

Percentage values are not supported. This attribute has lower priority than the [height](../../universal-attributes/layout-and-borders/sizing/document.md#height) attribute. If its value exceeds the **height** setting, cropping is performed based on the **height** constraint. Due to hardware limitations on some devices where 1 px dividers may not display properly after rounding, you are advised to use the **2px** value.

 |

#### \[h2\]lineCap

lineCap(value: LineCapStyle)

Sets the line cap style of the divider. This attribute can be dynamically set using [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier).

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [LineCapStyle](../../common-definitions/enums/document.md#linecapstyle) | Yes | 
Line cap style of the divider.

Default value: **LineCapStyle.Butt**

Invalid values are treated as the default value.

 |

#### Events

The [universal events](../../universal-events/document.md) are supported.

#### Example

## Example 1: Configuring the Divider Direction, Color, and Stroke Width

This example demonstrates how to configure a divider's direction, color, and stroke width.

// xxx.ets
@Entry
@Component
struct DividerExample {
  build() {
    Column() {
      // Use horizontal dividers.
      Text('Horizontal divider').fontSize(9).fontColor(0xCCCCCC)
      List() {
        ForEach(\[1, 2, 3\], (item: number) => {
          ListItem() {
            Text('list' + item).width('100%').fontSize(14).fontColor('#182431').textAlign(TextAlign.Start)
          }.width(244).height(48)
        }, (item: number) => item.toString())
      }.padding({ left: 24, bottom: 8 })

      Divider().strokeWidth(8).color('#F1F3F5')
      List() {
        ForEach(\[4, 5\], (item: number) => {
          ListItem() {
            Text('list' + item).width('100%').fontSize(14).fontColor('#182431').textAlign(TextAlign.Start)
          }.width(244).height(48)
        }, (item: number) => item.toString())
      }.padding({ left: 24, top: 8 })

      // Use vertical dividers.
      Text('Vertical divider').fontSize(9).fontColor(0xCCCCCC)
      Column() {
        Column() {
          Row().width(288).height(64).backgroundColor('#30C9F0').opacity(0.3)
          Row() {
            Button('Button')
              .width(136)
              .height(22)
              .fontSize(16)
              .fontColor('#007DFF')
              .fontWeight(500)
              .backgroundColor(Color.Transparent)
            Divider()
              .vertical(true)
              .height(22)
              .color('#182431')
              .opacity(0.6)
              .margin({ left: 8, right: 8 })
            Button('Button')
              .width(136)
              .height(22)
              .fontSize(16)
              .fontColor('#007DFF')
              .fontWeight(500)
              .backgroundColor(Color.Transparent)
          }.margin({ top: 17 })
        }
        .width(336)
        .height(152)
        .backgroundColor('#FFFFFF')
        .borderRadius(24)
        .padding(24)
      }
      .width('100%')
      .height(168)
      .backgroundColor('#F1F3F5')
      .justifyContent(FlexAlign.Center)
      .margin({ top: 8 })
    }.width('100%').padding({ top: 24 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/ynprwt-XR76YrVy4UmXU7w/en-us_image_0000002537765798.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=92613FEBACE68726AF61F233C2A09965BBBBAE71F6742436AEC9192504146DD0)

## Example 2: Configuring the Divider Line Cap Style

This example shows how to define the line cap style for a divider.

// xxx.ets
@Entry
@Component
struct DividerExample {
  build() {
    Column({space:30}) {
      Text("LineCap:Butt")
      Divider()
        .strokeWidth(20)
        .width("90%")
        .color('#F1F3F5')
        .lineCap(LineCapStyle.Butt)

      Text("LineCap:Round")
      Divider()
        .strokeWidth(20)
        .width("90%")
        .color('#F1F3F5')
        .lineCap(LineCapStyle.Round)

      Text("LineCap:Square")
      Divider()
        .strokeWidth(20)
        .width("90%")
        .color('#F1F3F5')
        .lineCap(LineCapStyle.Square)

    }.width('100%').padding({ top: 24 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/NJ13agNSSlCdSnA_8VbIeA/en-us_image_0000002537925738.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6B153E27704155D9BA14C94A9C1B8D43EDAD2A44CDAEA81940C992CF87B1DA75)
