# ArcScrollBar

The **ArcScrollBar** component is designed to be used together with scrollable components such as [ArcList](../arclist/document.md), [List](../list/document.md), [Grid](../grid/document.md), [Scroll](../scroll/document.md), and [WaterFlow](../waterflow/document.md).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/YQd6reXRTcq7i0mdOzZybw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062239Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6025351CDE33232BA13D1461AAA0DE302BBC56445E06F9E7FA9357367773029D)

-   This component is supported since API version 18. Updates will be marked with a superscript to indicate their earliest API version.
-   When the width and height of the **ArcScrollBar** component are not set, the **maxSize** value in the [layout constraint](../../../arkts-api/ui/arkui/framenode/document.md#layoutconstraint12) of its parent component is used as the width and height. If the parent component of the **ArcScrollBar** component contains scrollable components, such as [ArcList](../arclist/document.md), [List](../list/document.md), [Grid](../grid/document.md), [Scroll](../scroll/document.md), or [WaterFlow](../waterflow/document.md), you are advised to set the width and height of the **ArcScrollBar** component. Otherwise, the width and height of the component may be infinite.

#### Child Components

Not supported

#### APIs

ArcScrollBar(options: ArcScrollBarOptions)

A constructor used to create an **ArcScrollBar** instance.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Circle

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [ArcScrollBarOptions](#arcscrollbaroptions) | Yes | Parameters of the **ArcScrollBar** component. |

#### ArcScrollBarOptions

Represents the parameters used to construct an **ArcScrollBar** component.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Circle

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| scroller | [Scroller](../scroll/document.md#scroller) | No | No | Scroller, which can be bound to scrollable components for scrolling control. |
| state | [BarState](../../common-definitions/enums/document.md#barstate) | No | Yes | 
State of the scrollbar.

Default value: **BarState.Auto**

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/I8Tgr5CoTmWdT0Eh-DIy3w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062239Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DE10192214886902D5AC0A557B1C0D8A4FBBFD0E652FCC30BF75D9953AC279F9)

**ArcScrollBar** must be bound to a scrollable component through **scroller** to achieve synchronization. Only a one-to-one binding is allowed between **ArcScrollBar** and a scrollable component.

#### Example

This example demonstrates how to synchronize **ArcScrollBar** with the [Scroll](../scroll/document.md) component to implement an arc scrollbar.

import { ArcScrollBar } from '@kit.ArkUI';

@Entry
@Component
struct ArcScrollBarExample {
  private scroller: Scroller = new Scroller();
  private arr: number\[\] = \[0, 1, 2, 3, 4, 5, 6, 7, 8, 9\];

  build() {
    Stack({ alignContent: Alignment.Center }) {
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

      ArcScrollBar({ scroller: this.scroller, state: BarState.Auto })
    }
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/BqLSzrllQdaD1iy1ipXRmA/en-us_image_0000002537925502.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062239Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=30439B9ABC9805C7DF28CC8FF0C5D65CACE0B8CCE0E28AD2298D2777AE4BC475)
