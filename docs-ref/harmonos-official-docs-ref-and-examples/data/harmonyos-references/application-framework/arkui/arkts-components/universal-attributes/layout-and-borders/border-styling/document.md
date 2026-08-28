# Border Styling

The border attributes are used to set border styles for components.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/kt6F8truQACErdE5p4HfAA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062233Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A70A7EECB051E3224C5BF0C1EB50B458CFD6609B5692A817FAD8E6071B9A4DBE)

The initial APIs of this module are supported since API version 7. Updates will be marked with a superscript to indicate their earliest API version.

#### border

border(value: BorderOptions): T

Sets the border.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [BorderOptions](../../../common-definitions/basic-types/document.md#borderoptions) | Yes | 
Unified border style.

**NOTE**

The default value is **0**, indicating that no border is displayed.

Since API version 9, the parent node's border is displayed above child node content.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/YuBmMnvpTzKo1tgJviBPdw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062233Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=11F386B85027FD1609AC74F74EBBF75A562BBABE6476A5D8DE024D30816EB9DF)

When neither **color** nor **radius** is specified, set [borderColor](#bordercolor) and [borderRadius](#borderradius) after [border](#border) to ensure they take effect.

#### borderStyle

borderStyle(value: BorderStyle | EdgeStyles): T

Sets the border style.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [BorderStyle](../../../common-definitions/enums/document.md#borderstyle) | [EdgeStyles](../../../common-definitions/basic-types/document.md#edgestyles9)9+ | Yes | 
Border style.

Default value: **BorderStyle.Solid**

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### borderWidth

borderWidth(value: Length | EdgeWidths | LocalizedEdgeWidths): T

Sets the border width.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [Length](../../../common-definitions/basic-types/document.md#length) | [EdgeWidths](../../../common-definitions/basic-types/document.md#edgewidths9)9+ | [LocalizedEdgeWidths](../../../common-definitions/basic-types/document.md#localizededgewidths12)12+ | Yes | Border width. This parameter cannot be set in percentage. |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### borderColor

borderColor(value: ResourceColor | EdgeColors | LocalizedEdgeColors): T

Sets the border color.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ResourceColor](../../../common-definitions/basic-types/document.md#resourcecolor) | [EdgeColors](../../../common-definitions/basic-types/document.md#edgecolors9)9+ | [LocalizedEdgeColors](../../../common-definitions/basic-types/document.md#localizededgecolors12)12+ | Yes | 
Border color.

Default value: **Color.Black**

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### borderRadius

borderRadius(value: Length | BorderRadiuses | LocalizedBorderRadiuses): T

Sets the border radius.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [Length](../../../common-definitions/basic-types/document.md#length) | [BorderRadiuses](../../../common-definitions/basic-types/document.md#borderradiuses9)9+ | [LocalizedBorderRadiuses](../../../common-definitions/basic-types/document.md#localizedborderradiuses12)12+ | Yes | Radius of the border corners. The value can be expressed as a percentage of the component's width. When combined with the [clip](../../visual-effects/shape-clipping/document.md#clip12) attribute, this setting clips child components to prevent them from extending beyond the component's boundaries. |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### borderRadius22+

borderRadius(value: Length | BorderRadiuses | LocalizedBorderRadiuses, type?: RenderStrategy): T

Sets the border corner radius and the rendering strategy for rounded corners.

**Widget capability**: This API can be used in ArkTS widgets since API version 22.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [Length](../../../common-definitions/basic-types/document.md#length) | [BorderRadiuses](../../../common-definitions/basic-types/document.md#borderradiuses9) | [LocalizedBorderRadiuses](../../../common-definitions/basic-types/document.md#localizedborderradiuses12) | Yes | Radius of the border corners. The value can be expressed as a percentage of the component's width. When combined with the [clip](../../visual-effects/shape-clipping/document.md#clip12) attribute, this setting clips child components to prevent them from extending beyond the component's boundaries. |
| type | [RenderStrategy](../../../common-definitions/enums/document.md#renderstrategy22) | No | 
Rendering strategy for drawing rounded corners.

Default value: **RenderStrategy.FAST**.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### Example

## Example 1: Setting Basic Styles

This example shows how to set the border width, color, border radius, and styles such as dotted or dashed lines.

// xxx.ets
@Entry
@Component
struct BorderExample {
  build() {
    Column() {
      Flex({ justifyContent: FlexAlign.SpaceAround, alignItems: ItemAlign.Center }) {
        // Dashed border
        Text('dashed')
          .borderStyle(BorderStyle.Dashed).borderWidth(5).borderColor(0xAFEEEE).borderRadius(10)
          .width(120).height(120).textAlign(TextAlign.Center).fontSize(16)
        // Dotted border
        Text('dotted')
          .border({ width: 5, color: 0x317AF7, radius: 10, style: BorderStyle.Dotted })
          .width(120).height(120).textAlign(TextAlign.Center).fontSize(16)
      }.width('100%').height(150)

      Text('.border')
        .fontSize(50)
        .width(300)
        .height(300)
        .border({
          width: { left: 3, right: 6, top: 10, bottom: 15 },
          color: { left: '#e3bbbb', right: Color.Blue, top: Color.Red, bottom: Color.Green },
          radius: { topLeft: 10, topRight: 20, bottomLeft: 40, bottomRight: 80 },
          style: {
            left: BorderStyle.Dotted,
            right: BorderStyle.Dotted,
            top: BorderStyle.Solid,
            bottom: BorderStyle.Dashed
          }
        }).textAlign(TextAlign.Center)
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/64UI8vLsQ26E1zyk3onshA/en-us_image_0000002537925354.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062233Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3955E68029E4634D7BB864EBC4796C27785DB8B1879220F896A616B8E16098A7)

## Example 2: Setting the Border Width Type and Border Color

In this example, the **width**, **radius**, and **color** properties of the **border** attribute use the **LocalizedEdgeWidths** and **LocalizedEdgeColors** types.

// xxx.ets
import { LengthMetrics } from '@kit.ArkUI';
@Entry
@Component
struct BorderExample {
  build() {
    Column() {
      Flex({ justifyContent: FlexAlign.SpaceAround, alignItems: ItemAlign.Center }) {
        // Dashed border
        Text('dashed')
          .borderStyle(BorderStyle.Dashed)
          .borderWidth(5)
          .borderColor(0xAFEEEE)
          .borderRadius(10)
          .width(120)
          .height(120)
          .textAlign(TextAlign.Center)
          .fontSize(16)
        // Dotted border
        Text('dotted')
          .border({ width: 5, color: 0x317AF7, radius: 10, style: BorderStyle.Dotted })
          .width(120)
          .height(120)
          .textAlign(TextAlign.Center)
          .fontSize(16)
      }.width('100%').height(150)

      Text('.border')
        .fontSize(50)
        .width(300)
        .height(300)
        .border({
          width: {
            start: LengthMetrics.vp(3),
            end: LengthMetrics.vp(6),
            top: LengthMetrics.vp(10),
            bottom: LengthMetrics.vp(15)
          },
          color: { start: '#e3bbbb', end: Color.Blue, top: Color.Red, bottom: Color.Green },
          radius: {
            topStart: LengthMetrics.vp(10),
            topEnd: LengthMetrics.vp(20),
            bottomStart: LengthMetrics.vp(40),
            bottomEnd: LengthMetrics.vp(80)
          },
          style: {
            left: BorderStyle.Dotted,
            right: BorderStyle.Dotted,
            top: BorderStyle.Solid,
            bottom: BorderStyle.Dashed
          }
        })
        .textAlign(TextAlign.Center)
    }
  }
}

The following shows how the example is represented with left-to-right scripts.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/I6jfjkCeRj64bANkBZ1jLw/en-us_image_0000002568685131.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062233Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EFF26BD44737CB619A2975A5993D42E318D2435984A5977526D33E2A9D04EA29)

The following shows how the example is represented with right-to-left scripts.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/JU1ke6meQd2NKCkmhELMLw/en-us_image_0000002568765141.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062233Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=767BC1F44875D17F680E74C69F1D813A68548BAB4DE109B84DB9C1CEA8F8B429)

## Example 3: Configuring Offscreen Rounded Corners

This example demonstrates how to set the rendering strategy for drawing rounded corners on components, supported since API version 22.

// xxx.ets
@Entry
@Component
struct RenderStrategyExample {
  build() {
    NavDestination() {
      Column({ space: 20 }) {
        Stack() {
          Column()
            .width(320)
            .height(320)
            .backgroundColor(Color.Black)

          Stack() {
            Stack() {
              Scroll(new Scroller()) {
                Image($r('app.media.startIcon')).width('100%').height('200%')
              }

              Column()
                .blur(50)
                .width(300)
                .height(100)
                .position({ x: 0, y: 0 })
            }
          }
          .width(300)
          .height(300)
          .backgroundColor(Color.Pink)
          .borderRadius(50, RenderStrategy.FAST)
          .clip(true)
        }

        Stack() {
          Column()
            .width(320)
            .height(320)
            .backgroundColor(Color.Black)

          Stack() {
            Stack() {
              Scroll(new Scroller()) {
                Image($r('app.media.startIcon')).width('100%').height('200%')
              }

              Column()
                .blur(50)
                .width(300)
                .height(100)
                .position({ x: 0, y: 0 })
            }
          }
          .width(300)
          .height(300)
          .backgroundColor(Color.Pink)
          .borderRadius(50, RenderStrategy.OFFSCREEN)
          .clip(true)
        }
      }
    }
    .width('100%')
    .height('100%')
  }
}

The following illustration compares online rendering (top) with offscreen rendering (bottom) modes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/IDUkY25nRf6x9evW8a3pJg/en-us_image_0000002537765416.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062233Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C53F113E851A85EEC548ACB606EC64EFB6FF46C6AD831B508C6FFA7E0B1D5DDF)
