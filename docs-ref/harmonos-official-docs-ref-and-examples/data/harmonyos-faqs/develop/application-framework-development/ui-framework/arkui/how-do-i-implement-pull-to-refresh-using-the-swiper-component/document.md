# How do I implement pull-to-refresh using the Swiper component?

The **Swiper** component is used to create a swiper view container. You can use the **Refresh** component to implement the pull-to-refresh effect.

@Entry
@Component
struct SwiperItemLeak {
  @State isStopSwiperSlide: boolean = false;
  @State positionY: number = 0;
  private swiperController: SwiperController = new SwiperController();
  @State curSwiperIndex: number = 0;
  private list: number\[\] = \[\];

  aboutToAppear(): void {
    for (let i = 1; i <= 10; i++) {
      this.list.push(i);
    }
  }

  build() {
    Refresh({ refreshing: $$this.isStopSwiperSlide}) {
      Swiper(this.swiperController) {
        ForEach(this.list, (item: number) => {
          Text(item.toString())
            .width('100%')
            .height('100%')
            .backgroundColor(0xAFEEEE \* ((item + 1) / 0x0f))
            .textAlign(TextAlign.Center)
            .fontSize(30)
        },(item: number) => JSON.stringify(item))
      }
      .vertical(true)
      .width('100%')
      .height('100%')
      .cachedCount(3)
      .index(0)
      .autoPlay(false)
      .indicator(false)
      .effectMode(EdgeEffect.None)
      .loop(false)
      .duration(100)
      .disableSwipe(this.isStopSwiperSlide)
      .displayCount(1)
      .itemSpace(0)
      .curve(Curve.Linear)
      .backgroundColor(Color.Red)
      .position({ y: this.positionY })
      .onChange((index: number) => {
        this.curSwiperIndex = index;
      })
    }
    .onRefreshing(() => {
      setTimeout(() => {
        this.isStopSwiperSlide = false
      }, 2000)
    })
    .backgroundColor(0x89CFF0)
    .refreshOffset(64)
    .pullToRefresh(true)
    .width('100%')
    .height('100%')
  }
}

**Reference**

[Refresh](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-refresh)
