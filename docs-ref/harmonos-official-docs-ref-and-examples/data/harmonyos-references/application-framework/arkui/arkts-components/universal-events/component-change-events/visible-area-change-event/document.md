# Visible Area Change Event

The visible area change event of a component refers to the change in the visual portion of the component on the screen. It can be used to determine whether the component is completely or partially displayed on the screen. It is usually applicable to scenarios such as advertisement exposure tracing.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/l_6-Rb6YQtCf1fV5Jj_dYQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062233Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=15B62912C63183043C30D992998F17E347934DD7B04B7CD3F14DFC158E4FD16A)

The APIs of this module are supported since API version 9. Updates will be marked with a superscript to indicate their earliest API version.

#### onVisibleAreaChange

onVisibleAreaChange(ratios: Array<number>, event: VisibleAreaChangeCallback): T

Called when the visible area of the component changes. For details about the development guidelines and FAQs, see [Detecting Component Visibility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-manage-components-visibility).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/SYKBgiAzQ_m2cJYyTL9neg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062233Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7E3B8055436EC6DD0BFD3A901B363CBFE6DF4460FDF436341CE3A07F3C72990A)

-   This API can be called in [attributeModifier](../../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier) since API version 20.
    
-   This API only takes into account the relative clipped area ratio of the component with respect to all ancestor nodes (up to the window boundary) and its own area.
    
-   The following calculation scenarios are not supported: clipping by sibling nodes, clipping by siblings of any ancestor node, window-level occlusion, and component rotation. Examples include layouts using [Stack](../../../rows-columns-and-stacking/stack/document.md), [z-order control](../../../universal-attributes/basic-attributes/z-order-control/document.md), and [rotate](../../../universal-attributes/visual-effects/transformation/document.md#rotate) transformations.
    
-   It does not support visibility change calculations for nodes that are not in the component tree. For example, preloaded nodes or custom nodes mounted using the [overlay](../../../universal-attributes/basic-attributes/overlay-control/document.md#overlay) capability.
    
-   This API does not support the [scale](../../../universal-attributes/visual-effects/transformation/document.md#scale) attribute. To enable support for the [scale](../../../universal-attributes/visual-effects/transformation/document.md#scale) attribute, use [onVisibleAreaChange22+](#onvisibleareachange22) and set **measureFromViewport** to **true**.
    

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| ratios | Array<number> | Yes | 
Threshold array. Each threshold represents a ratio of the component's visible area (that is, the area of the component that is visible on screen; only the area within the parent component is counted) to the component's total area. This callback is invoked when the ratio of the component's visible area to its total area is greater than or less than the threshold. The value of each threshold ranges from 0.0 to 1.0. If a threshold value is less than 0.0, it is clamped to 0.0; if it is greater than 1.0, it is clamped to 1.0.

**NOTE**

When the value is close to the boundary 0 or 1, it is rounded off with a round-off error not greater than 0.001. For example, 0.9997 is rounded off to 1.

 |
| event | [VisibleAreaChangeCallback](#visibleareachangecallback12) | Yes | Callback for visible area changes of the component. |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### onVisibleAreaChange22+

onVisibleAreaChange(ratios: Array<number>, event: VisibleAreaChangeCallback, measureFromViewport: boolean): T

Called when the visible area of the component changes. You can use **measureFromViewport** to set the visible area calculation mode. For details about the development guidelines and FAQs, see [Detecting Component Visibility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-manage-components-visibility).

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| ratios | Array<number> | Yes | 
Threshold array. Each threshold represents the ratio of the component's visible area to its own total area. This callback is invoked when the ratio of the component's visible area to its total area is greater than or less than the threshold. The value of each threshold ranges from 0.0 to 1.0. If a threshold value is less than 0.0, it is clamped to 0.0; if it is greater than 1.0, it is clamped to 1.0.

**NOTE**

When the value is close to the boundary 0 or 1, it is rounded off with a round-off error not greater than 0.001. For example, 0.9997 is rounded off to 1.

 |
| event | [VisibleAreaChangeCallback](#visibleareachangecallback12) | Yes | Callback for visible area changes of the component. |
| measureFromViewport | boolean | Yes | 

Visible area calculation mode.

**true**: considers the parent's [clip](../../../universal-attributes/visual-effects/shape-clipping/document.md#clip12) attribute. If [clip](../../../universal-attributes/visual-effects/shape-clipping/document.md#clip12) is **false**, areas of the child component beyond the parent's bounds are counted as visible; if [clip](../../../universal-attributes/visual-effects/shape-clipping/document.md#clip12) is **true**, such areas are counted as invisible. **false**: ignores the parent's [clip](../../../universal-attributes/visual-effects/shape-clipping/document.md#clip12) attribute, treating areas beyond the parent's bounds as invisible.

When **measureFromViewport** is set to **true**, and an ancestor node has the [scale](../../../universal-attributes/visual-effects/transformation/document.md#scale) attribute set, the component's visible ratio will be correctly calculated.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/umm-DNJcQqKL0bUXfWIgEw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062233Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=50596344EC24E47AEAABE849EBD2534218F1BCC60994CA8ED81C088CA1337B74)

-   This API only takes into account the relative clipped area ratio of the component with respect to all ancestor nodes (up to the window boundary) and its own area.
    
-   The following calculation scenarios are not supported: clipping by sibling nodes, clipping by siblings of any ancestor node, window-level occlusion, and component rotation. Examples include layouts using [Stack](../../../rows-columns-and-stacking/stack/document.md), [z-order control](../../../universal-attributes/basic-attributes/z-order-control/document.md), and [rotate](../../../universal-attributes/visual-effects/transformation/document.md#rotate) transformations.
    
-   It does not support visibility change calculations for nodes that are not in the component tree. For example, preloaded nodes or custom nodes mounted using the [overlay](../../../universal-attributes/basic-attributes/overlay-control/document.md#overlay) capability.
    

#### onVisibleAreaApproximateChange17+

onVisibleAreaApproximateChange(options: VisibleAreaEventOptions, event: VisibleAreaChangeCallback | undefined): T

Configures a callback for the **onVisibleAreaApproximateChange** event, with options to limit the callback execution interval.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/aShIA-jVS-WlYv3n0Upu3Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062233Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=761717EEBB6A8186DC640C158D1FADD3FAC781B09C1380F0EEB4D416C3CB84C5)

This API can be called within [attributeModifier](../../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier) since API version 23.

**Atomic service API**: This API can be used in atomic services since API version 17.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [VisibleAreaEventOptions](#visibleareaeventoptions12) | Yes | Visible area change configuration options. |
| event | [VisibleAreaChangeCallback](#visibleareachangecallback12) | undefined | Yes | Callback for the **onVisibleAreaChange** event. This callback is triggered when the ratio of the component's visible area to its total area approaches the threshold set in **options**. |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/RSMvs2tJTWG330RIkb-omw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062233Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=255F5F7E59FC5FB8C4E9C4C76E89DE7246925302C26560D5AF499677F5C8F28E)

-   Compared with [onVisibleAreaChange](#onvisibleareachange), this API reduces calculation frequency to optimize performance when many nodes are registered. The calculation interval is controlled by the **expectedUpdateInterval** parameter in [VisibleAreaEventOptions](#visibleareaeventoptions12).
    
-   By default, the interval threshold of the visible area change callback includes 0. This means that, if the provided threshold is \[0.5\], the effective threshold will be \[0.0, 0.5\].
    
-   This API can be called in custom components since API version 18.
    
-   This API does not support the [scale](../../../universal-attributes/visual-effects/transformation/document.md#scale) attribute. To enable support for the [scale](../../../universal-attributes/visual-effects/transformation/document.md#scale) attribute, set **measureFromViewport** in [VisibleAreaEventOptions](#visibleareaeventoptions12) to **true**.
    
-   Since API version 21, the return value type is changed from **void** to **T**.
    

#### VisibleAreaEventOptions12+

Describes visible area change configuration options.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| ratios | Array<number> | No | No | 
Threshold array. Each threshold represents a ratio of the component's visible area (that is, the area of the component that is visible on screen; only the area within the parent component is counted) to the component's total area. The value of each threshold ranges from 0.0 to 1.0. If a threshold value is less than 0.0, it is clamped to 0.0; if it is greater than 1.0, it is clamped to 1.0.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| expectedUpdateInterval | number | No | Yes | 

Expected calculation interval, in ms.

Default value: **1000**.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| measureFromViewport22+ | boolean | No | Yes | 

Visible area calculation mode.

**true**: considers the parent's [clip](../../../universal-attributes/visual-effects/shape-clipping/document.md#clip12) attribute. If [clip](../../../universal-attributes/visual-effects/shape-clipping/document.md#clip12) is **false**, areas of the child component beyond the parent's bounds are counted as visible; if [clip](../../../universal-attributes/visual-effects/shape-clipping/document.md#clip12) is **true**, such areas are counted as invisible. **false**: ignores the parent's [clip](../../../universal-attributes/visual-effects/shape-clipping/document.md#clip12) attribute, treating areas beyond the parent's bounds as invisible.

Default value: **false**.

When **measureFromViewport** is set to **true**, and an ancestor node has the [scale](../../../universal-attributes/visual-effects/transformation/document.md#scale) attribute set, the component's visible ratio will be correctly calculated.

**Atomic service API**: This API can be used in atomic services since API version 22.

 |

#### VisibleAreaChangeCallback12+

type VisibleAreaChangeCallback = (isExpanding: boolean, currentRatio: number) => void

Represents a callback for visible area changes of the component.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| isExpanding | boolean | Yes | Whether the component's visible area has increased or decreased relative to its total area since the last callback. The value **true** indicates that the visible area has increased, and **false** indicates that the visible area has decreased. |
| currentRatio | number | Yes | Ratio of the component's visible area to its own area at the moment the callback is triggered. |

#### Example

## Example 1: Using onVisibleAreaChange to Listen for Visible Area Changes

This example demonstrates how to set an [onVisibleAreaChange](#onvisibleareachange) event for a component, which triggers the callback when the component is fully displayed or completely hidden.

// xxx.ets
@Entry
@Component
struct ScrollExample {
  scroller: Scroller = new Scroller()
  private arr: number\[\] = \[0, 1, 2, 3, 4, 5, 6, 7, 8, 9\]
  @State testTextStr: string = 'test'
  @State testRowStr: string = 'test'

  build() {
    Column() {
      Column() {
        Text(this.testTextStr)
          .fontSize(20)

        Text(this.testRowStr)
          .fontSize(20)
      }
      .height(100)
      .backgroundColor(Color.Gray)
      .opacity(0.3)

      Scroll(this.scroller) {
        Column() {
          Text("Test Text Visible Change")
            .fontSize(20)
            .height(200)
            .margin({ top: 50, bottom: 20 })
            .backgroundColor(Color.Green)
            // Set ratios to \[0.0, 1.0\] to invoke the callback when the component is fully visible or invisible on screen.
            .onVisibleAreaChange(\[0.0, 1.0\], (isExpanding: boolean, currentRatio: number) => {
              console.info(\`Test Text isExpanding: ${isExpanding}, currentRatio: ${currentRatio}\`)
              if (isExpanding && currentRatio >= 1.0) {
                console.info(\`Test Text is fully visible. currentRatio: ${currentRatio}\`)
                this.testTextStr = 'Test Text is fully visible'
              }

              if (!isExpanding && currentRatio <= 0.0) {
                console.info('Test Text is completely invisible.')
                this.testTextStr = 'Test Text is completely invisible'
              }
            })

          Row() {
            Text('Test Row Visible Change')
              .fontSize(20)
              .margin({ bottom: 20 })

          }
          .height(200)
          .backgroundColor(Color.Yellow)
          .onVisibleAreaChange(\[0.0, 1.0\], (isExpanding: boolean, currentRatio: number) => {
            console.info(\`Test Text isExpanding: ${isExpanding}, currentRatio: ${currentRatio}\`)
            if (isExpanding && currentRatio >= 1.0) {
              console.info('Test Row is fully visible.')
              this.testRowStr = 'Test Row is fully visible'
            }

            if (!isExpanding && currentRatio <= 0.0) {
              console.info('Test Row is completely invisible.')
              this.testRowStr = 'Test Row is completely invisible'
            }
          })

          ForEach(this.arr, (item: number) => {
            Text(item.toString())
              .width('90%')
              .height(150)
              .backgroundColor(0xFFFFFF)
              .borderRadius(15)
              .fontSize(16)
              .textAlign(TextAlign.Center)
              .margin({ top: 10 })
          }, (item: number) => (item.toString()))

        }.width('100%')
      }
      .backgroundColor(0x317aff)
      .scrollable(ScrollDirection.Vertical)
      .scrollBar(BarState.On)
      .scrollBarColor(Color.Gray)
      .scrollBarWidth(10)
      .onWillScroll((xOffset: number, yOffset: number, scrollState: ScrollState) => {
        console.info(\`${xOffset} ${yOffset}\`)
      })
      .onScrollEdge((side: Edge) => {
        console.info('To the edge')
      })
      .onScrollStop(() => {
        console.info('Scroll Stop')
      })

    }.width('100%').height('100%').backgroundColor(0xDCDCDC)
  }
}

## Example 2: Using onVisibleAreaApproximateChange to Listen for Visible Area Changes

This example demonstrates how to set an [onVisibleAreaApproximateChange](#onvisibleareaapproximatechange17) event for a component, which triggers the callback when the component is fully displayed or completely hidden. This feature is supported from API version 17.

// xxx.ets
@Entry
@Component
struct ScrollExample {
  scroller: Scroller = new Scroller()
  private arr: number\[\] = \[0, 1, 2, 3, 4, 5, 6, 7, 8, 9\]
  @State testTextStr: string = 'test'
  @State testRowStr: string = 'test'

  build() {
    Column() {
      Column() {
        Text(this.testTextStr)
          .fontSize(20)

        Text(this.testRowStr)
          .fontSize(20)
      }
      .height(100)
      .backgroundColor(Color.Gray)
      .opacity(0.3)

      Scroll(this.scroller) {
        Column() {
          Text("Test Text Visible Change")
            .fontSize(20)
            .height(200)
            .margin({ top: 50, bottom: 20 })
            .backgroundColor(Color.Green)
            // Set ratios to \[0.0, 1.0\] to invoke the callback when the component is fully visible or invisible on screen.
            .onVisibleAreaApproximateChange({ ratios: \[0.0, 1.0\], expectedUpdateInterval: 1000 },
              (isExpanding: boolean, currentRatio: number) => {
                console.info(\`Test Text isExpanding: ${isExpanding}, currentRatio: ${currentRatio}\`)
                if (isExpanding && currentRatio >= 1.0) {
                  console.info(\`Test Text is fully visible. currentRatio: ${currentRatio}\`)
                  this.testTextStr = 'Test Text is fully visible'
                }

                if (!isExpanding && currentRatio <= 0.0) {
                  console.info('Test Text is completely invisible.')
                  this.testTextStr = 'Test Text is completely invisible'
                }
              })

          Row() {
            Text('Test Row Visible Change')
              .fontSize(20)
              .margin({ bottom: 20 })

          }
          .height(200)
          .backgroundColor(Color.Yellow)
          .onVisibleAreaChange(\[0.0, 1.0\], (isExpanding: boolean, currentRatio: number) => {
            console.info(\`Test Text isExpanding: ${isExpanding}, currentRatio: ${currentRatio}\`)
            if (isExpanding && currentRatio >= 1.0) {
              console.info('Test Row is fully visible.')
              this.testRowStr = 'Test Row is fully visible'
            }

            if (!isExpanding && currentRatio <= 0.0) {
              console.info('Test Row is completely invisible.')
              this.testRowStr = 'Test Row is completely invisible'
            }
          })

          ForEach(this.arr, (item: number) => {
            Text(item.toString())
              .width('90%')
              .height(150)
              .backgroundColor(0xFFFFFF)
              .borderRadius(15)
              .fontSize(16)
              .textAlign(TextAlign.Center)
              .margin({ top: 10 })
          }, (item: number) => (item.toString()))

        }.width('100%')
      }
      .backgroundColor(0x317aff)
      .scrollable(ScrollDirection.Vertical)
      .scrollBar(BarState.On)
      .scrollBarColor(Color.Gray)
      .scrollBarWidth(10)
      .onWillScroll((xOffset: number, yOffset: number, scrollState: ScrollState) => {
        console.info(\`${xOffset} ${yOffset}\`)
      })
      .onScrollEdge((side: Edge) => {
        console.info('To the edge')
      })
      .onScrollStop(() => {
        console.info('Scroll Stop')
      })

    }.width('100%').height('100%').backgroundColor(0xDCDCDC)
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/1zGEpe-pSLyZFkNjEqH0Vg/en-us_image_0000002568765113.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062233Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=067AA01837C54E37D9340762C542903BDE0576E98AFD0A12738DE083488B33FC)

## Example 3: Setting measureFromViewport When a Child Component Extend Beyond the Parent for Display

In API version 22 and later versions, this example demonstrates the effect comparison of setting **measureFromViewport** in the **onVisibleAreaChange** event. The core difference lies in the returned component visible ratio (**currentRatio**): When **measureFromViewport** is set to **true**, the returned **currentRatio** value better aligns with the actual visual effect. The **currentRatio** value varies slightly on different devices.

@Entry
@Component
struct OnVisibleAreaChangeSample {
  @State ratio1: number = 0.0;
  @State ratio2: number = 0.0;
  @State ratio3: number = 0.0;

  build() {
    Column() {
      Text(\`onVisibleChange1 with measureFromViewport \\nratio: ${this.ratio1}\`)
      Column() {
        Row() {
          Row() {

          }
          .backgroundColor(Color.Blue)
          .height(120)
          .width(120)
          .offset({ x: 0, y: 60 })
          // If measureFromViewport is set to true and clip(true) is not set for the parent component, any area of the child component that extends beyond its parent component's bounds is regarded as a visible area.
          .onVisibleAreaApproximateChange({
            ratios: \[0.0, 1.0\],
            expectedUpdateInterval: 500,
            measureFromViewport: true
          }, (isExpanding: boolean, currentRatio: number) => {
            console.info(\`onVisibleAreaApproximateChange1 isExpanding: ${isExpanding} currentRatio: ${currentRatio}\`)
          })
          .onVisibleAreaChange(\[0.0, 1.0\], (isExpanding: boolean, currentRatio: number) => {
            this.ratio1 = currentRatio
          }, true)
        }
        .backgroundColor(Color.Pink)
        .height(120)
        .width(120)
      }
      .padding(5)
      .borderWidth(1)
      .height(200)
      .width(200)

      Text(\`onVisibleChange2 without measureFromViewport \\nratio: ${this.ratio2}\`)
      Column() {
        Row() {
          Row() {

          }
          .backgroundColor(Color.Blue)
          .height(120)
          .width(120)
          .offset({ x: 0, y: 60 })
          // If measureFromViewport is not set (which will be treated as false) and clip(true) is not set for the parent component, any area of the child component that extends beyond its parent component's bounds is regarded as an invisible area.
          .onVisibleAreaApproximateChange({ ratios: \[0.0, 1.0\], expectedUpdateInterval: 500 },
            (isExpanding: boolean, currentRatio: number) => {
              console.info(\`onVisibleAreaApproximateChange2 isExpanding: ${isExpanding} currentRatio: ${currentRatio}\`)
            })
          .onVisibleAreaChange(\[0.0, 1.0\], (isExpanding: boolean, currentRatio: number) => {
            this.ratio2 = currentRatio
          })
        }
        .backgroundColor(Color.Pink)
        .height(120)
        .width(120)
      }
      .padding(5)
      .borderWidth(1)
      .height(200)
      .width(200)

      Text(\`parent set clip(true) onVisibleChange3 with measureFromViewport \\nratio: ${this.ratio3}\`)
      Column() {
        Row() {
          Row() {

          }
          .backgroundColor(Color.Blue)
          .height(120)
          .width(120)
          .offset({ x: 0, y: 60 })
          // If measureFromViewport is set to true and clip(true) is set for the parent component, any area of the child component that extends beyond its parent component regarded as an invisible area.
          .onVisibleAreaApproximateChange({
            ratios: \[0.0, 1.0\],
            expectedUpdateInterval: 500,
            measureFromViewport: true
          }, (isExpanding: boolean, currentRatio: number) => {
            console.info(\`onVisibleAreaApproximateChange3 isExpanding: ${isExpanding} currentRatio: ${currentRatio}\`)
          })
          .onVisibleAreaChange(\[0.0, 1.0\], (isExpanding: boolean, currentRatio: number) => {
            this.ratio3 = currentRatio
          }, true)
        }
        .clip(true)
        .backgroundColor(Color.Pink)
        .height(120)
        .width(120)
      }
      .padding(5)
      .borderWidth(1)
      .height(200)
      .width(200)
    }
    .height('100%')
    .width('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/gbyK5pFzSka__9uj3A-VNA/en-us_image_0000002537765388.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062233Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3F16A83FC26BF5CB122733E72431B4F14336C072A620E9B0BCC7BAE69F06666D)
