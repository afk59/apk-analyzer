# Creating a Swiper (Swiper)

The [Swiper](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-swiper) component is a container that is able to display child components in looping mode. It is typically used in scenarios such as display of recommended content on the home page.

The **Swiper** component provides a preloading mechanism, which you can use to improve the swipe experience in complex scenarios. This mechanism allows for prebuilding and prerendering components when the main thread is idle.

#### Layout and Constraints

The **Swiper** component follows its own size settings if they are configured. If the component does not have its own size settings configured, it follows the size of its parent component when the [prevMargin](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-swiper#prevmargin10) or [nextMargin](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-swiper#nextmargin10) attribute is set, or adapts its size to its child components otherwise.

#### Loop Playback

The [loop](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-swiper#loop) attribute sets whether to enable loop playback. The default value is **true**.

When **loop** is set to **true**, the user can switch to the previous or next page when they are on the first or last page. When **loop** is set to **false**, this behavior is disabled.

-   Example of setting **loop** to **true**:

  Swiper() {
    Text('0')
      .width('90%')
      .height('100%')
      .backgroundColor(Color.Gray)
      .textAlign(TextAlign.Center)
      .fontSize(30)

    Text('1')
      .width('90%')
      .height('100%')
      .backgroundColor(Color.Green)
      .textAlign(TextAlign.Center)
      .fontSize(30)

    Text('2')
      .width('90%')
      .height('100%')
      .backgroundColor(Color.Pink)
      .textAlign(TextAlign.Center)
      .fontSize(30)
  }
// ···
  .loop(true)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/XWiZF1nkSsmY6fEqGXG7yQ/en-us_image_0000002568684405.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061934Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=84687E4773FE16AC2F0CBE3974B5C489B7D68A9BE7504CA325A29A3D1D13FF9F)

-   Example of setting **loop** to **false**:

  Swiper() {
    // ···
  }
// ···
  .loop(false)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/qt5WFP2bSEymNHK_PO1hjQ/en-us_image_0000002568764415.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061934Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=457975A2D4A7BFB44026AC8AC52198AC257DFEABBB274FAAB99B823ED728FD1A)

#### Automatic Playback

The [autoPlay](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-swiper#autoplay) attribute sets whether to enable automatic playback for child component switching. Its default value is **false**.

When **autoPlay** is set to **true**, automatic playback is enabled for child component switching. The playback interval is specified by the **interval** attribute, which is **3000** by default, in milliseconds.

  Swiper() {
    // ···
  }
// ···
  .loop(true)
  .autoPlay(true)
  .interval(1000)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/vwWZg2SITwi5GIacLdKMnw/en-us_image_0000002537764690.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061934Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1DC4234E6025AC6C8A3B0B432CEA8C1E1A03DFBD6724408176F4FED8853F9F10)

#### Navigation Indicator

The **Swiper** component comes with default indicator and arrow styles, with the indicators centered at the bottom and arrows hidden by default. You can customize the position and style of the indicator using the [indicator](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-swiper#indicator) attribute.

With the **indicator** attribute, you can set the position of the indicator relative to the edges of the **Swiper** component, in addition to the size, color, and mask of each indicator as well as the color of the selected indicator.

-   Example of using the navigation indicator in its default style:

Swiper() {
  Text('0')
    .width('90%')
    .height('100%')
    .backgroundColor(Color.Gray)
    .textAlign(TextAlign.Center)
    .fontSize(30)

  Text('1')
    .width('90%')
    .height('100%')
    .backgroundColor(Color.Green)
    .textAlign(TextAlign.Center)
    .fontSize(30)

  Text('2')
    .width('90%')
    .height('100%')
    .backgroundColor(Color.Pink)
    .textAlign(TextAlign.Center)
    .fontSize(30)
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/dhHYilniQXqXz1JK-fS3EQ/en-us_image_0000002537924630.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061934Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A0B46F8BC2F7D717F7DED19E23B61CAF7EBE4EF9ADF0F79E5804604C1B93C626)

-   Example of customizing the style of the navigation indicator

The selected navigation indicator has a diameter of 30 vp with blue color, while unselected indicators have a diameter of 15 vp with red color.

  Swiper() {
    // ···
  }
// ···
  .indicator(
    Indicator.dot()
      .left(0)
      .itemWidth(15)
      .itemHeight(15)
      .selectedItemWidth(30)
      .selectedItemHeight(15)
      .color(Color.Red)
      .selectedColor(Color.Blue)
  )

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/miY9Qn_GTjmbR_Iv5NmzTg/en-us_image_0000002568684407.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061934Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7B78DAACB59232BDB53E85790CE6FE14B4C85F00474CEBA98D5D21AB8F13EED2)

You can set the [displayArrow](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-swiper#displayarrow10) attribute of **Swiper** to control the size, position, color, and background of navigation point arrows, and whether to display arrows on mouse hover.

-   Example of using the navigation point arrows in the default style:

  Swiper() {
    // ···
  }
// ···
  .displayArrow(true, false)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/CBq_HlwdSfyyx8zdTaTufw/en-us_image_0000002568764417.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061934Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4F39F9865D152F5B7946D95C684C3EA1330C42F7A372807BD96970299179C7BE "Click to enlarge")

-   Example of customizing the style of navigation point arrows:

In this example, the arrows are displayed on both sides of the component, with a size of 18 vp and a color of blue.

  Swiper() {
    // ···
  }
// ···
  .displayArrow({
    showBackground: true,
    isSidebarMiddle: true,
    backgroundSize: 24,
    backgroundColor: Color.White,
    arrowSize: 18,
    arrowColor: Color.Blue
  }, false)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/SCczkmJdQDGK-uTXsB5LoQ/en-us_image_0000002537764692.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061934Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A18E2482C6643E373DBA78A5E3BC8C69EE124331DB6117434451591F8AA2193B "Click to enlarge")

#### Page Switching Mode

The **Swiper** component supports three page switching modes: swiping with fingers, touching navigation points, and using a controller. The following example shows how to switch between pages using a controller.

@Entry
@Component
export struct SwiperPageSwitchMethod {
  private swiperBackgroundColors: Color\[\] = \[Color.Blue, Color.Brown, Color.Gray, Color.Green, Color.Orange,
    Color.Pink, Color.Red, Color.Yellow\];
  private swiperAnimationMode: (SwiperAnimationMode | boolean | undefined)\[\] = \[undefined, true, false,
    SwiperAnimationMode.NO\_ANIMATION, SwiperAnimationMode.DEFAULT\_ANIMATION, SwiperAnimationMode.FAST\_ANIMATION\];
  private swiperController: SwiperController = new SwiperController();
  private animationModeIndex: number = 0;
  private animationMode: (SwiperAnimationMode | boolean | undefined) = undefined;
  @State animationModeStr: string = 'undefined';
  @State targetIndex: number = 0;

  aboutToAppear(): void {
    this.toSwiperAnimationModeStr();
  }

  build() {
    // ···
          Column({ space: 5 }) {
            Swiper(this.swiperController) {
              ForEach(this.swiperBackgroundColors, (backgroundColor: Color, index: number) => {
                Text(index.toString())
                  .width(250)
                  .height(250)
                  .backgroundColor(backgroundColor)
                  .textAlign(TextAlign.Center)
                  .fontSize(30)
              })
            }
            // ···
            .indicator(true)

            Row({ space: 12 }) {
              Button('showNext')
                .onClick(() => {
                  this.swiperController.showNext(); // Switch to the next page using the controller.
                })
              Button('showPrevious')
                .onClick(() => {
                  this.swiperController.showPrevious(); // Switch to the previous page using the controller.
                })
            }.margin(5)

            Row({ space: 12 }) {
              Text('Index:')
              Button(this.targetIndex.toString())
                .onClick(() => {
                  this.targetIndex = (this.targetIndex + 1) % this.swiperBackgroundColors.length;
                })
            }.margin(5)
            Row({ space: 12 }) {
              Text('AnimationMode:')
              Button(this.animationModeStr)
                .onClick(() => {
                  this.animationModeIndex = (this.animationModeIndex + 1) % this.swiperAnimationMode.length;
                  this.toSwiperAnimationModeStr();
                })
            }.margin(5)

            Row({ space: 12 }) {
              Button('changeIndex(' + this.targetIndex + ', ' + this.animationModeStr + ')')
                .onClick(() => {
                  this.swiperController.changeIndex(this.targetIndex, this.animationMode); // Switch to the specified page using the controller.
                })
            }.margin(5)
          }
        // ···
  }

  private toSwiperAnimationModeStr() {
    this.animationMode = this.swiperAnimationMode\[this.animationModeIndex\];
    if ((this.animationMode === true) || (this.animationMode === false)) {
      this.animationModeStr = '' + this.animationMode;
    } else if ((this.animationMode === SwiperAnimationMode.NO\_ANIMATION) ||
      (this.animationMode === SwiperAnimationMode.DEFAULT\_ANIMATION) ||
      (this.animationMode === SwiperAnimationMode.FAST\_ANIMATION)) {
      this.animationModeStr = SwiperAnimationMode\[this.animationMode\];
    } else {
      this.animationModeStr = 'undefined';
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/-e4Lv9_NQq-dMVrwrZgY-g/en-us_image_0000002537924632.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061934Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0D1AB48BE441CF6595A1E6F220A94AC82E512859FE4B65D083EF3C1A60D8492D)

#### Playback Direction

The **Swiper** component supports both horizontal and vertical swiping, controlled primarily by the [vertical](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-swiper#vertical) attribute.

When **vertical** is set to **true**, vertical swiping is used. When **vertical** is set to **false**, horizontal swiping is used. The default value of **vertical** is **false**.

-   Example of using horizontal swiping:

Swiper(
// ···
) {
// ···
}
// ···
.indicator(true)
.vertical(false)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/_O9z8lRFTh2WjYWvZHFrew/en-us_image_0000002568684409.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061934Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=186204B60ED480BB034D79E1188107289591A363274ABF35BD5E9000A6CA5160)

-   Example of using vertical swiping:

Swiper(
// ···
) {
// ···
}
// ···
.indicator(true)
.vertical(true)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/Y6H-NNsYSXCpEChD-LEv8A/en-us_image_0000002568764419.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061934Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4390D8A1477B3CF4DCCEBACC114C60BE19242697DDE5A32266604755990EC11C)

#### Child Components Per Page

You can set the number of child components per page for the **Swiper** component through its [displayCount](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-swiper#displaycount8) attribute.

  Swiper() {
    Text('0')
      .width(250)
      .height(250)
      .backgroundColor(Color.Gray)
      .textAlign(TextAlign.Center)
      .fontSize(30)
    Text('1')
      .width(250)
      .height(250)
      .backgroundColor(Color.Green)
      .textAlign(TextAlign.Center)
      .fontSize(30)
    Text('2')
      .width(250)
      .height(250)
      .backgroundColor(Color.Pink)
      .textAlign(TextAlign.Center)
      .fontSize(30)
    Text('3')
      .width(250)
      .height(250)
      .backgroundColor(Color.Yellow)
      .textAlign(TextAlign.Center)
      .fontSize(30)
  }
// ···
  .indicator(true)
  .displayCount(2)
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/UlWu3wDjS1S1pUBEEroa2g/en-us_image_0000002537764694.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061934Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=511F21EC6B66844686D74EF5EA545A4CD74AF93E7F39C51F2118CAAA4409CE53)

#### Customizing Transition Animation

Use the [customContentTransition](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-swiper#customcontenttransition12) attribute to set a custom transition animation for **Swiper**. Define the animation by adjusting opacity, scale, translation, and rendering layer for all pages within the viewport frame by frame in the callback.

@Entry
@Component
export struct SwiperCustomAnimation {
  private DISPLAY\_COUNT: number = 2;
  private MIN\_SCALE: number = 0.75;
  @State backgroundColors: Color\[\] = \[Color.Green, Color.Blue, Color.Yellow, Color.Pink, Color.Gray, Color.Orange\];
  @State opacityList: number\[\] = \[\];
  @State scaleList: number\[\] = \[\];
  @State translateList: number\[\] = \[\];
  @State zIndexList: number\[\] = \[\];

  aboutToAppear(): void {
    for (let i = 0; i < this.backgroundColors.length; i++) {
      this.opacityList.push(1.0);
      this.scaleList.push(1.0);
      this.translateList.push(0.0);
      this.zIndexList.push(0);
    }
  }

  build() {
    // ···
      Column({ space: 12 }) {
        // ···
          Swiper() {
            ForEach(this.backgroundColors, (backgroundColor: Color, index: number) => {
              Text(index.toString())
                .width('100%')
                .height('100%')
                .fontSize(50)
                .textAlign(TextAlign.Center)
                .backgroundColor(backgroundColor)
                .opacity(this.opacityList\[index\])
                .scale({ x: this.scaleList\[index\], y: this.scaleList\[index\] })
                .translate({ x: this.translateList\[index\] })
                .zIndex(this.zIndexList\[index\])
            })
          }
          .height(300)
          .indicator(false)
          .displayCount(this.DISPLAY\_COUNT, true)
          .customContentTransition({
            timeout: 1000,
            transition: (proxy: SwiperContentTransitionProxy) => {
              if (proxy.position <= proxy.index % this.DISPLAY\_COUNT ||
                proxy.position >= this.DISPLAY\_COUNT + proxy.index % this.DISPLAY\_COUNT) {
                // When a group of pages is completely scrolled out of the viewport, reset the attribute values.
                this.opacityList\[proxy.index\] = 1.0;
                this.scaleList\[proxy.index\] = 1.0;
                this.translateList\[proxy.index\] = 0.0;
                this.zIndexList\[proxy.index\] = 0;
              } else {
                // When a group of pages is not scrolled out of the viewport, adjust the attribute values frame by frame for the left and right pages in the group based on the position.
                if (proxy.index % this.DISPLAY\_COUNT === 0) {
                  this.opacityList\[proxy.index\] = 1 - proxy.position / this.DISPLAY\_COUNT;
                  this.scaleList\[proxy.index\] =
                    this.MIN\_SCALE + (1 - this.MIN\_SCALE) \* (1 - proxy.position / this.DISPLAY\_COUNT);
                  this.translateList\[proxy.index\] = -proxy.position \* proxy.mainAxisLength +
                    (1 - this.scaleList\[proxy.index\]) \* proxy.mainAxisLength / 2.0;
                } else {
                  this.opacityList\[proxy.index\] = 1 - (proxy.position - 1) / this.DISPLAY\_COUNT;
                  this.scaleList\[proxy.index\] =
                    this.MIN\_SCALE + (1 - this.MIN\_SCALE) \* (1 - (proxy.position - 1) / this.DISPLAY\_COUNT);
                  this.translateList\[proxy.index\] = -(proxy.position - 1) \* proxy.mainAxisLength -
                    (1 - this.scaleList\[proxy.index\]) \* proxy.mainAxisLength / 2.0;
                }
                this.zIndexList\[proxy.index\] = -1;
              }
            }
          })
        // ···
      }
      .width('100%')
    // ···
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/H0M4oVi4TXiDefF1ZnzSFQ/en-us_image_0000002537924634.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061934Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F0AD6B33B8E19F9F807855F9C9E8F98840C4A25B21D572F778791BB8E89115E6)

#### Synchronizing the Swiper with the Tabs

When the selected item in the **Swiper** changes, the new index is passed to the [onSelected](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-swiper#onselected18) callback. You can then call [tabsController.changeIndex(index)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-tabs#changeindex) to synchronize the **Tabs** component.

// xxx.ets
class MyDataSource implements IDataSource {
  private list: number\[\] = \[\];

  constructor(list: number\[\]) {
    this.list = list;
  }

  totalCount(): number {
    return this.list.length;
  }

  getData(index: number): number {
    return this.list\[index\];
  }

  registerDataChangeListener(listener: DataChangeListener): void {
  }

  unregisterDataChangeListener() {
  }
}

@Entry
@Component
export struct SwiperAndTabsLinkage {
  @State fontColor: string = '#182431';
  @State selectedFontColor: string = '#007DFF';
  @State currentIndex: number = 0;
  private list: number\[\] = \[\];
  private tabsController: TabsController = new TabsController();
  private swiperController: SwiperController = new SwiperController();
  private swiperData: MyDataSource = new MyDataSource(\[\]);
  private context = this.getUIContext().getHostContext() as common.UIAbilityContext;

  aboutToAppear(): void {
    for (let i = 0; i <= 9; i++) {
      this.list.push(i);
    }
    this.swiperData = new MyDataSource(this.list);
  }

  @Builder tabBuilder(index: number, name: string) {
    Column() {
      Text(name)
        .fontColor(this.currentIndex === index ? this.selectedFontColor : this.fontColor)
        .fontSize(16)
        .fontWeight(this.currentIndex === index ? 500 : 400)
        .lineHeight(22)
        .margin({ top: 17, bottom: 7 })
      Divider()
        .strokeWidth(2)
        .color('#007DFF')
        .opacity(this.currentIndex === index ? 1 : 0)
    }.width('20%')
  }

  build() {
    // ...
          Column() {
            Tabs({ barPosition: BarPosition.Start, controller: this.tabsController }) {
              ForEach(this.list, (index: number) =>{
                // Configure a resource whose name is 'swiper\_text1' and value is a non-empty string in the resources\\base\\element\\string.json file.
                TabContent().tabBar(this.tabBuilder(index,
                  this.context.resourceManager.getStringByNameSync('swiper\_text1') + this.list\[index\]))
              })
            }
            .onTabBarClick((index: number) => {
              this.currentIndex = index;
              this.swiperController.changeIndex(index, true);
            })
            .barMode(BarMode.Scrollable)
            .backgroundColor('#F1F3F5')
            .height(56)
            .width('100%')

            Swiper(this.swiperController) {
              LazyForEach(this.swiperData, (item: string) => {
                Text(item.toString())
                  .onAppear(()=>{
                    console.info('onAppear ' + item.toString());
                  })
                  .onDisAppear(()=>{
                    console.info('onDisAppear ' + item.toString());
                  })
                  .width('100%')
                  .height('40%')
                  .backgroundColor(0xAFEEEE)
                  .textAlign(TextAlign.Center)
                  .fontSize(30)
              }, (item: string) => item)
            }
            .loop(false)
            .onSelected((index: number) => {
              console.info('onSelected:' + index);
              this.currentIndex = index;
              this.tabsController.changeIndex(index);
            })
          }
          // ...
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/9wR-4EWdTIC6L5AF8onuaw/en-us_image_0000002568684411.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061934Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8B7EEE8C6D19B3A9F8317ACD6EF277AB493315C44D96048ED82ADF73E175C240)

#### Setting the Spacing Between Dots

Use the [space](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-swiper#space19) attribute of **DotIndicator** to set the spacing between dots.

Swiper(
  // ···
) {
  // ···
}
.indicator(new DotIndicator()
  .space(this.space)
  // ···
)

#### Ignoring the Navigation Indicator Component Size

After the [bottom](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-swiper#bottom) of the navigation point is set to **0**, there is still a certain spacing between the bottom of the navigation point and the bottom of the **Swiper**. To remove this gap, apply the **bottom(bottom, ignoreSize)** attribute. Set **ignoreSize** to **true** to ignore the navigation indicator component size.

-   Ignoring the dot navigation indicator component size:

Swiper(
  // ···
) {
  // ···
}
.indicator(new DotIndicator()
  // ···
  .bottom(LengthMetrics.vp(0), this.ignoreSize) // true
  // ···
)

-   Ignoring the digit navigation indicator component size:

Swiper(
  // ···
) {
  // ···
}
.indicator(new DigitIndicator()
  .bottom(LengthMetrics.vp(0), true)
)

Complete sample code for setting the dot spacing and ignoring the component size for a dot navigation indicator:

import { LengthMetrics } from '@kit.ArkUI';
// ···

class MyDataSource implements IDataSource {
  private list: number\[\] = \[\];

  constructor(list: number\[\]) {
    this.list = list;
  }

  totalCount(): number {
    return this.list.length;
  }

  getData(index: number): number {
    return this.list\[index\];
  }

  registerDataChangeListener(listener: DataChangeListener): void {
  }

  unregisterDataChangeListener() {
  }
}

@Entry
@Component
export struct SwiperIgnoreComponentSize {

  @State space: LengthMetrics = LengthMetrics.vp(0);
  @State spacePool: LengthMetrics\[\] = \[LengthMetrics.vp(0), LengthMetrics.px(3), LengthMetrics.vp(10)\];
  @State spaceIndex: number = 0;

  @State ignoreSize: boolean = false;
  @State ignoreSizePool: boolean\[\] = \[false, true\];
  @State ignoreSizeIndex: number = 0;

  private swiperController1: SwiperController = new SwiperController();
  private data1: MyDataSource = new MyDataSource(\[\]);

  aboutToAppear(): void {
    let list1: number\[\] = \[\];
    for (let i = 1; i <= 10; i++) {
      list1.push(i);
    }
    this.data1 = new MyDataSource(list1);
  }

  build() {
    // ···
          Scroll() {
            Column({ space: 20 }) {
              Swiper(
                this.swiperController1
              ) {
                LazyForEach(this.data1, (item: string) => {
                  Text(item.toString())
                    .width('90%')
                    .height(120)
                    .backgroundColor(0xAFEEEE)
                    .textAlign(TextAlign.Center)
                    .fontSize(30)
                }, (item: string) => item)
              }
              .indicator(new DotIndicator()
                .space(this.space)
                .bottom(LengthMetrics.vp(0), this.ignoreSize) // true
                .itemWidth(15)
                .itemHeight(15)
                .selectedItemWidth(15)
                .selectedItemHeight(15)
                .color(Color.Gray)
                .selectedColor(Color.Blue)
              )
              .displayArrow({
                showBackground: true,
                isSidebarMiddle: true,
                backgroundSize: 24,
                backgroundColor: Color.White,
                arrowSize: 18,
                arrowColor: Color.Blue
              }, false)

              Column({ space: 4 }) {
                Button('spaceIndex:' + this.spaceIndex).onClick(() => {
                  this.spaceIndex = (this.spaceIndex + 1) % this.spacePool.length;
                  this.space = this.spacePool\[this.spaceIndex\];
                }).margin(10)

                Button('ignoreSizeIndex:' + this.ignoreSizeIndex).onClick(() => {
                  this.ignoreSizeIndex = (this.ignoreSizeIndex + 1) % this.ignoreSizePool.length;
                  this.ignoreSize = this.ignoreSizePool\[this.ignoreSizeIndex\];
                }).margin(10)
              }.margin(2)
            }.width('100%')
          }
        // ···
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/TmVRsp_PToKslZ5eMb4v0A/en-us_image_0000002568764421.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061934Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F93CC3C19BF12967267E083A6F7E35C7A965993A28559E2BFD337414FC632654)

#### Maintaining the Visible Content Position

When using **LazyForEach** to load data (for example, adding data through **onDataAdd**), set the [maintainVisibleContentPosition](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-swiper#maintainvisiblecontentposition20) attribute to keep the visible content position stable, preventing view jumps caused by data addition or deletion. The default value is **false**.

When **maintainVisibleContentPosition** is set to **true**, the visible content position remains unchanged when data is inserted or deleted above or before the display area.

For details about how to use **LazyForEach**, see the example in [LazyForEach: Lazy Data Loading](../../ui-paradigm-rendering-control/lazyforeach-lazy-data-loading/document.md).

// xxx.ets
class MyDataSource implements IDataSource {
  private listeners: DataChangeListener\[\] = \[\];
  private dataArray: string\[\] = \['0', '1', '2', '3', '4', '5', '6'\];

  public totalCount(): number {
    return this.dataArray.length;
  }

  public getData(index: number): string | undefined {
    return this.dataArray\[index\];
  }

  public addData(index: number, data: string): void {
    this.dataArray.splice(index, 0, data);
    this.listeners.forEach(listener => {
      listener.onDataAdd(index);
    })
  }

  public deleteData(index: number): void {
    this.dataArray.splice(index, 1);
    this.listeners.forEach(listener => {
      listener.onDataDelete(index);
    })
  }

  registerDataChangeListener(listener: DataChangeListener): void {
    if (this.listeners.indexOf(listener) < 0) {
      hilog.info(DOMAIN, 'testTag', 'add listener');
      this.listeners.push(listener);
    }
  }

  unregisterDataChangeListener(listener: DataChangeListener): void {
    const pos = this.listeners.indexOf(listener);
    if (pos >= 0) {
      hilog.info(DOMAIN, 'testTag', 'remove listener');
      this.listeners.splice(pos, 1);
    }
  }
}

@Entry
@Component
export struct SwiperVisibleContentPosition {
  private data: MyDataSource = new MyDataSource();
  @State index: number = 3;

  build() {
    // ...
      Column({ space: 12 }) {
        // ...
            Swiper() {
              LazyForEach(this.data, (item: string) => {
                Text(item.toString())
                  .width('90%')
                  .height(160)
                  .backgroundColor(0xAFEEEE)
                  .textAlign(TextAlign.Center)
                  .fontSize(30)
              })
            }
            .onChange((index) => {
              this.index = index;
            })
            .index(3)
            .maintainVisibleContentPosition(true)
            // ...

            Column({ space: 12 }) {
              Text('index:' + this.index).fontSize(20)
              Row() {
                // Insert data at index 0 of the LazyForEach data source.
                Button('header data add').height(30).onClick(() => {
                  this.data.addData(0, 'header Data');
                })
                // Delete data at index 0 of the LazyForEach data source.
                Button('header data delete').height(30).onClick(() => {
                  this.data.deleteData(0);
                })
              }
            }.margin(5)
            // ...
      }.width('100%')
      .margin({ top: 5 })
      // ...
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/EeBztHN7ToGEW4iiPWRVkA/en-us_image_0000002537764696.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061934Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B0C878E213CD88D8E299943C484F009D3C97B372ECDF9193DC292234B99D9D40)
