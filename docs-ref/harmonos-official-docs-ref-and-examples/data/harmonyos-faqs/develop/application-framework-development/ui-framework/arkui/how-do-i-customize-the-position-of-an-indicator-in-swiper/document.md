# How do I customize the position of an indicator in Swiper?

**Symptom**

The UI style of the built-in [indicator](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-swiper#indicator) of the [Swiper](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-swiper) component has a fixed width and height and cannot be customized.

**Solution**

Solution 1. Use custom indicators. Currently, **DotIndicator** has a fixed padding, which cannot meet the requirements. You can perform the following steps to implement an indicator without padding:

1.  Create a **Swiper** component and a **Column** component in the **Stack** component.
2.  Use [LazyForEach](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-rendering-control-lazyforeach) to render the **Column** component and set a proper height and margin. For example, set the [alignContent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-stack#aligncontent): Alignment.Bottom parameter in the **Stack** component to align the indicator at the bottom, or set the [location](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-universal-attributes-location) attribute to specify the indicator position.
3.  Compare the value of **index** with that of **currentIndex**. When the two values are the same, change the width and color of the **Column** component to implement the indicator effect.

The sample code is as follows:

@Entry
@Component
struct SwiperExample {
  private swiperController: SwiperController = new SwiperController();
  @State arr: string\[\] = \['1', '2', '3', '4', '5', '6'\];
  @State widthLength: number = 0;
  @State heightLength: number = 0;
  @State currentIndex: number = 0;

  build() {
    Column({ space: 5 }) {
      Stack({ alignContent: Alignment.Bottom }) {
        Swiper(this.swiperController) {
          ForEach(this.arr, (item: string) => {
            Text(item)
              .width('90%')
              .height(200)
              .backgroundColor(0xAFEEEE)
              .textAlign(TextAlign.Center)
              .fontSize(30)
          }, (item: string) => item)
        }
        .cachedCount(2)
        .index(0)
        .indicator(false)
        .onChange((index: number) => {
          this.currentIndex = index;
        })

        Row() {
          ForEach(this.arr, (\_: string, index: number) => {
            Column()
              .width(this.currentIndex == index ? 15 : 5)
              .height(5)
              .margin(5)
              .backgroundColor(this.currentIndex == index ? Color.Gray : Color.White)
          }, (item: string) => item)
        }
      }
    }
    .width('100%')
    .height('100%')
  }
}

Solution 2: Use the **Indicator** component of API version 15. The **Indicator** component uses the default indicator style of the **Swiper** component and its interaction area height cannot exceed 32 vp. However, this component separates the **Swiper** component from the indicator. Therefore, you can use the **Column** component to encapsulate the **Indicator** component and use the **clip** attribute to control its height. Then, use the **Stack** component for encapsulation. The implementation is as follows:

@Entry
@Component
struct DotIndicatorDemo {
  private indicatorController: IndicatorComponentController = new IndicatorComponentController();
  private swiperController: SwiperController = new SwiperController();
  @State list: string\[\] = \['1', '2', '3', '4', '5', '6'\];

  build() {
    Stack({ alignContent: Alignment.Bottom }) {
      Swiper(this.swiperController) {
        ForEach(this.list, (item: string) => {
          Text(item)
            .width('90%')
            .height(200)
            .backgroundColor(0xAFEEEE)
            .textAlign(TextAlign.Center)
            .fontSize(30)
        }, (item: string) => item)
      }
      .cachedCount(2)
      .index(0)
      .indicator(this.indicatorController)

      Column() {
        IndicatorComponent(this.indicatorController)
          .style(
            new DotIndicator()
              .itemWidth(10)
              .itemHeight(10)
              .selectedItemWidth(20)
              .selectedItemHeight(10)
              .color(Color.White)
              .selectedColor(Color.Gray)
          )
      }
      .height(25)
      .clip(true)
    }
    .width('100%')
  }
}

NOTE: If the background of the indicator in solution 2 is transparent, **clip** is not required. You can also use the **margin** attribute to set the bottom to a negative value to achieve a similar effect.
