# Indicator

The **Indicator** component provides two types of navigation indicators: dot indicators and digit indicators.

It encapsulates the existing [indicator](../../scroll-and-swipe/swiper/document.md#indicator) capabilities—previously part of the [Swiper](../../scroll-and-swipe/swiper/document.md) component—and delivers them as a standalone component. You can use the **Indicator** component independently or bind it to a **Swiper** component through **IndicatorComponentController**.

When multiple **Indicator** components are bound to a single **Swiper**, only the last bound **Indicator** is active.

Conversely, if an **Indicator** is bound to multiple **Swiper** components, only the last bound **Swiper** works with the **Indicator**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/DnzRoa5MQZex2js06T7jmA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C1065DA5DE82FC118BE0F411BB5E2463A2ADAB33EB7F8736AC1C7E097573B10F)

This component is supported since API version 15. Updates will be marked with a superscript to indicate their earliest API version.

#### Child Components

Not supported

#### APIs

#### \[h2\]IndicatorComponent

IndicatorComponent(controller?: IndicatorComponentController)

A constructor used to create an **Indicator** component. You can optionally pass a controller to manage the **Indicator** component.

**Widget capability**: This API can be used in ArkTS widgets since API version 15.

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| controller | [IndicatorComponentController](#indicatorcomponentcontroller) | No | Controller to manage the **Indicator** component. |

#### Attributes

In addition to the [universal attributes](../../universal-attributes/document.md), the following attributes are supported.

#### \[h2\]style

style(indicatorStyle: DotIndicator | DigitIndicator)

Sets the style of the navigation indicator.

**Widget capability**: This API can be used in ArkTS widgets since API version 15.

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| indicatorStyle | [DotIndicator](../../scroll-and-swipe/swiper/document.md#dotindicator10) | [DigitIndicator](../../scroll-and-swipe/swiper/document.md#digitindicator10) | Yes | 
Style of the navigation indicator.

\- **DotIndicator**: dot style.

\- **DigitIndicator**: digit style.

Default style: **DotIndicator**

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/ThTJ4BmlToWRoIzIcT_PXg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F5C057CA5C1B8CB67056D28193B97748A15B6D8DA507DE209DA93267E40E6AC2)

The **maxDisplayCount** property has no effect when the **DotIndicator** type (configured in **indicatorStyle**) is not bound to a **Swiper** component.

#### \[h2\]count

count(totalCount: number)

Sets the total number of navigation points.

When the **Indicator** component is used with a **Swiper** component, the count is subject to the number of pages in the **Swiper** component.

**Widget capability**: This API can be used in ArkTS widgets since API version 15.

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| totalCount | number | Yes | 
Total number of navigation points.

Default value: **2**

 |

#### \[h2\]initialIndex

initialIndex(index: number)

Sets the initial index of the navigation indicator when it first appears. If the value is less than 0 or greater than or equal to the total count, the default value **0** is used.

This attribute does not take effect when the **Indicator** component is bound to a **Swiper** component.

**Widget capability**: This API can be used in ArkTS widgets since API version 15.

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| index | number | Yes | 
Initial index of the navigation indicator when it first appears.

Default value: **0**

 |

#### \[h2\]loop

loop(isLoop: boolean)

Sets whether to enable looping.

This attribute does not take effect when the **Indicator** component is bound to a **Swiper** component.

**Widget capability**: This API can be used in ArkTS widgets since API version 15.

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| isLoop | boolean | Yes | 
Whether to enable looping. The value **true** means to enable looping, and **false** means the opposite.

Default value: **true**

 |

#### \[h2\]vertical

vertical(isVertical: boolean)

Sets whether vertical swiping is used.

This attribute does not take effect when the **Indicator** component is bound to a **Swiper** component.

**Widget capability**: This API can be used in ArkTS widgets since API version 15.

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| isVertical | boolean | Yes | 
Whether vertical swiping is used. The value **true** means vertical swiping, and **false** means horizontal swiping.

Default value: **false**.

 |

#### Events

In addition to the [universal events](../../universal-events/document.md), the following events are supported.

#### \[h2\]onChange

onChange(event: Callback<number>)

Triggered when the currently selected navigation index changes. The callback provides the new index.

**Widget capability**: This API can be used in ArkTS widgets since API version 15.

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | [Callback](../../common-definitions/basic-types/document.md#callback12)<number> | Yes | Callback triggered when the index changes. |

#### IndicatorComponentController

Implements a controller for the **Indicator** component, allowing you to control navigation.

#### \[h2\]constructor

constructor()

A constructor used to create an **IndicatorComponentController** object.

**Widget capability**: This API can be used in ArkTS widgets since API version 15.

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### \[h2\]showNext

showNext(): void

Moves to the next navigation point.

**Widget capability**: This API can be used in ArkTS widgets since API version 15.

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### \[h2\]showPrevious

showPrevious(): void

Moves to the previous navigation point.

**Widget capability**: This API can be used in ArkTS widgets since API version 15.

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### \[h2\]changeIndex

changeIndex(index: number, useAnimation?: boolean): void

Navigates to the specified indicator.

**Widget capability**: This API can be used in ArkTS widgets since API version 15.

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| index | number | Yes | 
Target indicator index.

**NOTE**

If the value specified is less than 0 or greater than the maximum indicator index, the value **0** is used.

 |
| useAnimation | boolean | No | 

Whether to use an animation for when the target index is reached. The value **true** means to use an animation, and **false** means the opposite.

Default value: **false**.

 |

#### Example

## Example 1: Using a Dot Indicator with a Swiper Component

This example binds the same [IndicatorComponentController](#indicatorcomponentcontroller) object to both the [indicator](../../scroll-and-swipe/swiper/document.md#indicator) API of the [Swiper](../../scroll-and-swipe/swiper/document.md) component and the [IndicatorComponent](#indicatorcomponent) constructor, enabling interaction between the dot indicator and the **Swiper** component.

@Entry
@Component
struct DotIndicatorDemo {
  private indicatorController: IndicatorComponentController = new IndicatorComponentController();
  private swiperController: SwiperController = new SwiperController();
  @State list: number\[\] = \[\];
  aboutToAppear(): void {
    for (let i = 1; i <= 6; i++) {
      this.list.push(i);
    }
  }

  build() {
    Column() {
      Swiper(this.swiperController) {
        ForEach(this.list, (item: string) => {
          Text(item.toString())
            .width('100%')
            .height(160)
            .backgroundColor(0xAFEEEE)
            .textAlign(TextAlign.Center)
            .fontSize(30)
        }, (item: string) => item)
      }
      .cachedCount(2)
      .index(0)
      .autoPlay(true)
      .interval(2000)
      .indicator(this.indicatorController)
      .loop(true)
      .duration(1000)
      .itemSpace(0)
      .curve(Curve.Linear)
      .onChange((index: number) => {
        console.info(index.toString());
      })

      IndicatorComponent(this.indicatorController)
        .initialIndex(0)
        .style(
          new DotIndicator()
            .itemWidth(15)
            .itemHeight(15)
            .selectedItemWidth(15)
            .selectedItemHeight(15)
            .color(Color.Gray)
            .selectedColor(Color.Blue))
        .loop(true)
        .count(6)
        .vertical(true)
        .onChange((index: number) => {
          console.info("current index: " + index );
        })
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/_c-jbVP_RdiJ1HR1uaR8WA/en-us_image_0000002537925504.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=90C855E765D164F6D2744DC59B63024B59AA378CD000E00CFD2F272C8EB7339A)

## Example 2: Using a Digit Indicator with a Swiper Component

This example binds the same [IndicatorComponentController](#indicatorcomponentcontroller) object to both the [indicator](../../scroll-and-swipe/swiper/document.md#indicator) API of the [Swiper](../../scroll-and-swipe/swiper/document.md) component and the [IndicatorComponent](#indicatorcomponent) constructor, enabling interaction between the digit indicator and the **Swiper** component.

@Entry
@Component
struct DigitIndicatorDemo {
  private indicatorController: IndicatorComponentController = new IndicatorComponentController();
  private swiperController: SwiperController = new SwiperController();
  @State list: number\[\] = \[\];
  aboutToAppear(): void {
    for (let i = 1; i <= 6; i++) {
      this.list.push(i);
    }
  }

  build() {
    Column() {
      Swiper(this.swiperController) {
        ForEach(this.list, (item: string) => {
          Text(item.toString())
            .width('100%')
            .height(160)
            .backgroundColor(0xAFEEEE)
            .textAlign(TextAlign.Center)
            .fontSize(30)
        }, (item: string) => item)
      }
      .cachedCount(2)
      .index(0)
      .autoPlay(true)
      .interval(2000)
      .indicator(this.indicatorController)
      .loop(true)
      .duration(1000)
      .itemSpace(0)
      .curve(Curve.Linear)
      .onChange((index: number) => {
        console.info(index.toString());
      })

      IndicatorComponent(this.indicatorController)
        .initialIndex(0)
        .style(Indicator.digit()
          .fontColor(Color.Gray)
          .selectedFontColor(Color.Gray)
          .digitFont({ size: 20, weight: FontWeight.Bold })
          .selectedDigitFont({ size: 20, weight: FontWeight.Normal }))
        .loop(true)
        .count(6)
        .vertical(true)
        .onChange((index: number) => {
          console.info("current index: " + index );
        })
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/lr4kJ3sKRNWl_6lWcWzPFA/en-us_image_0000002568685281.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EEAFA588629D2076AE9F65F738480EA3817B5B6EAA112E7804559689DB49F004)
