# ScrollBar

The **ScrollBar** component is designed to be used together with scrollable components such as [ArcList](../arclist/document.md), [List](../list/document.md), [Grid](../grid/document.md), [Scroll](../scroll/document.md), and [WaterFlow](../waterflow/document.md).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/Zpn_GwcxSROfzRCyI8OnFA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062239Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AA45F81CA2BD39A5A8E910A8DEF61052EBCE5DC9A3D49764B4238248075B999C)

-   This component is supported since API version 8. Updates will be marked with a superscript to indicate their earliest API version.
-   If the size of the main axis direction is not set for **ScrollBar**, the **maxSize** value in the [layout constraints](../../../arkts-api/ui/arkui/framenode/document.md#layoutconstraint12) of the parent component is used. If the parent component of the **ScrollBar** component contains a scrollable component, such as [ArcList](../arclist/document.md), [List](../list/document.md), [Grid](../grid/document.md), [Scroll](../scroll/document.md), or [WaterFlow](../waterflow/document.md), you are advised to set the size in the main axis direction of the **ScrollBar**; otherwise, the size in the main axis direction of **ScrollBar** may become infinite.

#### Child Components

This component can contain a single child component.

#### APIs

ScrollBar(value: ScrollBarOptions)

Creates a scroll bar.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ScrollBarOptions](#scrollbaroptions) | Yes | Parameters of the **ScrollBar** component. |

#### Attributes

In addition to the [universal attributes](../../universal-attributes/document.md), the following attributes are supported.

#### \[h2\]enableNestedScroll14+

enableNestedScroll(enabled: Optional<boolean>)

Sets whether nested scrolling is enabled.

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| enabled | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<boolean> | Yes | 
Whether nested scrolling is enabled. The value **true** means that nested scrolling is enabled, and **false** means the opposite.

Default value: **false**

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/aCE6r23dRs292yjYnu8YCQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062239Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1638F9480A80592243905EC323909FB60D76811840B4C47BB1AEE3779DDDEBD8)

When nested scrolling is enabled, the scroll offset is first passed to the inner scrollable component, which then passes it to the outer parent scrollable component based on the set nested scrolling priority.

Nested scrolling is not supported when the **WaterFlow** component is in [WaterFlowLayoutMode.SLIDING\_WINDOW](../waterflow/document.md#waterflowlayoutmode12) layout mode.

When the nested scrolling mode is set to [PARALLEL](../../common-definitions/enums/document.md#nestedscrollmode10), both the parent and child components scroll simultaneously. You need to manage the scroll order in the [onScrollFrameBegin](../scroll/document.md#onscrollframebegin9) event according to the desired logic.

#### \[h2\]scrollBarColor20+

scrollBarColor(color: Optional<ColorMetrics>)

Sets the color of the scrollbar slider. This parameter is valid only when the scrollbar does not contain child components.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| color | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<[ColorMetrics](../../../arkts-api/ui/arkui/graphics/document.md#colormetrics12)\> | Yes | 
Scrollbar color.

Default value: **ColorMetrics.numeric(0x66182431)**

 |

#### ScrollBarOptions

Parameters of the **ScrollBar** component.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/J13u6D21QXSWhL4xomHE7g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062239Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4CBB0187121169572C8A7EB6973820819A52191B7272AFA429B7CF8277DC4FB0)

-   The **ScrollBar** component defines the behavior style of the scrollable area, and its child nodes define the behavior style of the scrollbar.
-   This component is bound to a scrollable component through **scroller**, and can be used to scroll the scrollable component only when their directions are the same. The **ScrollBar** component can be bound to only one scrollable component, and vice versa.
-   Since API version 12, the **ScrollBar** component displays a default scrollbar style when without child nodes.
-   The visibility of the **ScrollBar** component is set through **BarState**. The component automatically adjusts **opacity** based on the **BarState** setting to control its visibility. Therefore, setting the [opacity](../../universal-attributes/visual-effects/opacity-control/document.md#opacity18) attribute for the **ScrollBar** component does not take effect.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| scroller | [Scroller](../scroll/document.md#scroller) | No | No | Scroller, which can be bound to scrollable components for scrolling control. |
| direction | [ScrollBarDirection](#scrollbardirection) | No | Yes | 
Scrollbar direction in which scrollable components scroll.

Default value: **ScrollBarDirection.Vertical**

 |
| state | [BarState](../../common-definitions/enums/document.md#barstate) | No | Yes | 

Scrollbar state.

Default value: **BarState.Auto**

 |

#### ScrollBarDirection

Enumerates the scrolling directions.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| Vertical | 0 | Vertical scrollbar. |
| Horizontal | 1 | Horizontal scrollbar. |

#### Example 1: Implementing a ScrollBar Component with Child Components

This example illustrates the style of a **ScrollBar** component with child components.

// xxx.ets
@Entry
@Component
struct ScrollBarExample {
  private scroller: Scroller = new Scroller();
  private arr: number\[\] = \[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15\];

  build() {
    Column() {
      Stack({ alignContent: Alignment.End }) {
        Scroll(this.scroller) {
          Flex({ direction: FlexDirection.Column }) {
            ForEach(this.arr, (item: number) => {
              Row() {
                Text(item.toString())
                  .width('80%')
                  .height(60)
                  .backgroundColor('#3366CC')
                  .borderRadius(15)
                  .fontSize(16)
                  .textAlign(TextAlign.Center)
                  .margin({ top: 5 })
              }
            }, (item: number) => item.toString())
          }.margin({ right: 15 })
        }
        .width('90%')
        .scrollBar(BarState.Off)
        .scrollable(ScrollDirection.Vertical)

        ScrollBar({ scroller: this.scroller, direction: ScrollBarDirection.Vertical, state: BarState.Auto }) {
          Text()
            .width(20)
            .height(100)
            .borderRadius(10)
            .backgroundColor('#C0C0C0')
        }.width(20).backgroundColor('#ededed')
      }
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/yVRE4li2SEStqZO-tKvrBA/en-us_image_0000002537925496.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062239Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=55D01F68C25E92D955621A77803DDCA27B1573F4DA1DF05BEA62B5C9F800F815)

#### Example 2: Implementing a ScrollBar Component Without Child Components

This example illustrates the style of a **ScrollBar** component without child components. The [scrollBarColor](#scrollbarcolor20) attribute is added since API version 20.

import { ColorMetrics } from '@kit.ArkUI'

@Entry
@Component
struct ScrollBarExample {
  private scroller: Scroller = new Scroller();
  private arr: number\[\] = \[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15\];
  @State scrollBarColor: ColorMetrics = ColorMetrics.rgba(24, 35, 48, 0.4);

  build() {
    Column() {
      Stack({ alignContent: Alignment.End }) {
        Scroll(this.scroller) {
          Flex({ direction: FlexDirection.Column }) {
            ForEach(this.arr, (item: number) => {
              Row() {
                Text(item.toString())
                  .width('80%')
                  .height(60)
                  .backgroundColor('#3366CC')
                  .borderRadius(15)
                  .fontSize(16)
                  .textAlign(TextAlign.Center)
                  .margin({ top: 5 })
              }
            }, (item: number) => item.toString())
          }.margin({ right: 15 })
        }
        .width('90%')
        .scrollBar(BarState.Off)
        .scrollable(ScrollDirection.Vertical)

        ScrollBar({ scroller: this.scroller, direction: ScrollBarDirection.Vertical, state: BarState.Auto })
          .scrollBarColor(this.scrollBarColor)
      }
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/5rLdJ8CKRleZO2MNZKu4MQ/en-us_image_0000002568685273.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062239Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=35EF5F39A9A3ECD16A70D72EA0D89EBA2BFD3D24B84576DD4D4C53818506BE7D)

#### Example 3: Enabling Nested Scrolling

This example demonstrates how to enable nested scrolling for a **ScrollBar** component using the [enableNestedScroll](#enablenestedscroll14) attribute. This feature is available from API version 20.

import { ColorMetrics } from '@kit.ArkUI'

@Entry
@Component
struct StickyNestedScroll {
  listScroller: Scroller = new Scroller();
  @State array: number\[\] = \[\];
  @State scrollBarColor: ColorMetrics = ColorMetrics.rgba(24, 35, 48, 0.4);

  @Styles
  listCard() {
    .backgroundColor(Color.White)
    .height(72)
    .width('100%')
    .borderRadius(12)
  }

  build() {
    Stack() {
      Scroll() {
        Column() {
          Text('Scroll Area')
            .width('100%')
            .height('40%')
            .backgroundColor('#0080DC')
            .textAlign(TextAlign.Center)
          List({ space: 10, scroller: this.listScroller }) {
            ForEach(this.array, (item: number) => {
              ListItem() {
                Text('item' + item)
                  .fontSize(16)
              }
              .listCard()
            }, (item: number) => item.toString())
          }
          .scrollBar(BarState.Off)
          .nestedScroll({
            scrollForward: NestedScrollMode.PARENT\_FIRST,
            scrollBackward: NestedScrollMode.SELF\_FIRST
          })
          .height('100%')
        }
        .width('100%')
      }
      .edgeEffect(EdgeEffect.Spring)
      .backgroundColor('#DCDCDC')
      .scrollBar(BarState.Off)
      .width('100%')
      .height('100%')

      ScrollBar({ scroller: this.listScroller })
        .position({ right: 0 })
        .enableNestedScroll(true)
        .scrollBarColor(this.scrollBarColor)
    }
  }

  aboutToAppear() {
    for (let i = 0; i < 15; i++) {
      this.array.push(i);
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/vwQ3OgfrS6aOloLsMwIZ0Q/en-us_image_0000002568765283.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062239Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8F531C71E00326AD762EFBB667CED8085658C5E30E0ABE55337F81B961867281)
