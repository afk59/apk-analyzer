# Stepper

The **Stepper** component provides a step navigator, suitable for guiding users through a step-by-step task completion process.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/Lh4uG6qxSj2rwVd2HfMKCQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062253Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9465FDDFFB2AD9797434D25F9C3E758069DF40BFB948B79399E0D631FD9EC005)

-   This API is supported since API version 8 and deprecated since API version 22. You are advised to use [Swiper](../../scroll-and-swipe/swiper/document.md) instead. For details, see [Example 2](#example-2-using-swiper-as-a-substitute-for-stepper).
    
-   This component is supported since API version 8. Updates will be marked with a superscript to indicate their earliest API version.
    

#### Child Components

Only the child component [StepperItem](../stepperitem/document.md) is supported.

#### APIs

Stepper(value?: { index?: number })

Creates a **Stepper** component.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/mnZWOF2kSYOvla7i5bBnTw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062253Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2558DFB96437D9D08888FD9C924D75F115825F179AE252D385D0A6640B5E2C64)

This API is supported since API version 8 and deprecated since API version 22. You are advised to use [index](../../scroll-and-swipe/swiper/document.md#index) instead.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | { index?: number } | No | 
Index of the **StepperItem** that is currently displayed.

Default value: **0**

Since API version 10, this parameter supports two-way binding through [$$](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-two-way-sync).

 |

#### Attributes

None

#### Events

#### \[h2\]onFinish(deprecated)

onFinish(callback: () => void)

Triggered when [nextLabel](../stepperitem/document.md#nextlabeldeprecated) of the last [StepperItem](../stepperitem/document.md) in the stepper is clicked and the [ItemState](../stepperitem/document.md#itemstate) attribute is **Normal**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/HMPFfgqUTKSr-uBEcubWng/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062253Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9243ABDF6F5DD6A2F8E577B98583B31558B6B9049303F858F12357619E29EB07)

This API is supported since API version 8 and deprecated since API version 22. You are advised to use [onChange](../../scroll-and-swipe/swiper/document.md#onchange) instead.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | () => void | Yes | Invoked when the **nextLabel** of the last **StepperItem** in the **Stepper** is clicked and the **ItemState** attribute is set to **Normal**. |

#### \[h2\]onSkip(deprecated)

onSkip(callback: () => void)

Triggered when [nextLabel](../stepperitem/document.md#nextlabeldeprecated) is clicked and the [StepperItem](../stepperitem/document.md) status is **ItemState.Skip**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/szgekk2XSjOjxbvzokW7uQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062253Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=09EE801BF8605C73236152C5F7263CE76A92A1525885E13F407D4848ABAF5340)

This API is supported since API version 8 and deprecated since API version 22. You are advised to use [onChange](../../scroll-and-swipe/swiper/document.md#onchange) instead.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | () => void | Yes | Invoked when the current **StepperItem** is **ItemState.Skip** and the **nextLabel** is clicked. |

#### \[h2\]onChange(deprecated)

onChange(callback: (prevIndex: number, index: number) => void)

Triggered when the step navigation switches by clicking [prevLabel](../stepperitem/document.md#prevlabeldeprecated) of the **StepperItem** component; or when clicking [nextLabel](../stepperitem/document.md#nextlabeldeprecated) of the current **StepperItem** component, provided that the current page is not the last **StepperItem** in the stepper and the [ItemState](../stepperitem/document.md#itemstate) attribute is **Normal**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/qpG6JcrrRiWj_uVfNE-HFQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062253Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D6790956356C689AD6E73F9FBCCFE5CC4089F0F21F2745C7B723C65E988BBAD4)

This API is supported since API version 8 and deprecated since API version 22. You are advised to use [onChange](../../scroll-and-swipe/swiper/document.md#onchange) instead.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| prevIndex | number | Yes | 
Index of the step page before the switching.

Value range: \[0, +∞).

 |
| index | number | Yes | 

Index of the step page after the switching, that is, index of the previous or next page.

Value range: \[0, +∞).

 |

#### \[h2\]onNext(deprecated)

onNext(callback: (index: number, pendingIndex: number) => void)

Triggered when switching to the next step by clicking [nextLabel](../stepperitem/document.md#nextlabeldeprecated) of a **StepperItem**, provided that the current page is not the last **StepperItem** in the stepper and the [ItemState](../stepperitem/document.md#itemstate) attribute is **Normal**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/sCyr7O6lS6OInpikyLbyzg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062253Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2BB16DB24D1D67768BE7492AA2B8835A2A8C89E34D6E04D58308207BC83ABF09)

This API is supported since API version 8 and deprecated since API version 22. You are advised to use [onChange](../../scroll-and-swipe/swiper/document.md#onchange) instead.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| index | number | Yes | Index of the current step page. |
| pendingIndex | number | Yes | Index of the next step page. |

#### \[h2\]onPrevious(deprecated)

onPrevious(callback: (index: number, pendingIndex: number) => void)

Triggered when switching to the previous step by clicking [prevLabel](../stepperitem/document.md#prevlabeldeprecated) of a **StepperItem**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/Pj4fvIqFRY2oJj9JF7RAhA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062253Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9FE607E32E3347B70AAA8F9287CA5335099828F2847CF5C8BC4BC01BD921C7C1)

This API is supported since API version 8 and deprecated since API version 22. You are advised to use [onChange](../../scroll-and-swipe/swiper/document.md#onchange) instead.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| index | number | Yes | Index of the current step page. |
| pendingIndex | number | Yes | Index of the previous step page. |

#### Example

## Example 1: Using the Stepper Component

This example demonstrates how to use the **Stepper** component.

// xxx.ets
@Styles function itemStyle () {
  .width(336)
  .height(621)
  .margin({ top: 48, left: 12 })
  .borderRadius(24)
  .backgroundColor('#FFFFFF')
}

@Extend(Text) function itemTextStyle () {
  .fontColor('#182431')
  .fontSize(36)
  .fontWeight(500)
  .opacity(0.4)
  .margin({ top: 82, bottom: 40 })
}

@Entry
@Component
struct StepperExample {
  @State currentIndex: number = 0;
  @State firstState: ItemState = ItemState.Normal;
  @State secondState: ItemState = ItemState.Normal;
  @State thirdState: ItemState = ItemState.Normal;

  build() {
    Stepper({
      index: this.currentIndex
    }) {
      // First step page
      StepperItem() {
        Column() {
          Text('Page One')
            .itemTextStyle()
          Button('change status:' + this.firstState)
            .backgroundColor('#007dFF')
            .onClick(() => {
              this.firstState = this.firstState === ItemState.Skip ? ItemState.Normal : ItemState.Skip;
            })
        }.itemStyle()
      }
      .nextLabel('Next')
      .status(this.firstState)
      // Second step page
      StepperItem() {
        Column() {
          Text('Page Two')
            .itemTextStyle()
          Button('change status:' + this.secondState)
            .backgroundColor('#007dFF')
            .onClick(() => {
              this.secondState = this.secondState === ItemState.Disabled ? ItemState.Normal : ItemState.Disabled;
            })
        }.itemStyle()
      }
      .nextLabel('Next')
      .prevLabel('Previous')
      .status(this.secondState)
      // Third step page
      StepperItem() {
        Column() {
          Text('Page Three')
            .itemTextStyle()
          Button('change status:' + this.thirdState)
            .backgroundColor('#007dFF')
            .onClick(() => {
              this.thirdState = this.thirdState === ItemState.Waiting ? ItemState.Normal : ItemState.Waiting;
            })
        }.itemStyle()
      }
      .status(this.thirdState)
      // Fourth step page
      StepperItem() {
        Column() {
          Text('Page Four')
            .itemTextStyle()
        }.itemStyle()
      }
    }
    .backgroundColor('#F1F3F5')
    .onFinish(() => {
      // Define the processing logic for when Finish on the last page is clicked, for example, redirection.
      console.info('onFinish');
    })
    .onSkip(() => {
      // Define the processing logic for when Skip on the page is clicked, for example, dynamically changing the index of the Stepper to redirect to a specific step.
      console.info('onSkip');
    })
    .onChange((prevIndex?: number, index?: number) => {
      if(index){
        this.currentIndex = index;
      }
    })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/WcJ0rh_wTdyw-1QxXaQf5g/en-us_image_0000002568765757.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062253Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BE82CDFC55968F7831F0A18011E4DA31C619F5398CF50A5205A5BD8EAD6CE3FC)

## Example 2: Using Swiper as a Substitute for Stepper

This example demonstrates how to use the **Swiper** component to achieve the functionality of the **Stepper** component. The resulting effect is the same as in Example 1.

@Styles
function itemStyle() {
  .width(336)
  .height(621)
  .margin({ top: 48, left: 12 })
  .borderRadius(24)
  .backgroundColor('#FFFFFF')
}

@Extend(Text)
function itemTextStyle() {
  .fontColor('#182431')
  .fontSize(36)
  .fontWeight(500)
  .opacity(0.4)
  .margin({ top: 82, bottom: 40 })
}

@Entry
@Component
struct StepperExample {
  @State currentIndex: number = 0;
  @State status: number = 0;
  @State nextLabel: string = "Next";
  @State prevLabel: string = "Previous";
  private swiperController: SwiperController = new SwiperController();

  build() {
    Column() {
      Swiper(this.swiperController) {
        // First step page
        Column() {
          Text('Page One')
            .itemTextStyle()
          Button('change status:' + this.status)
            .backgroundColor('#007dFF')
            .onClick(() => {
              if (this.status < 3) {
                this.status += 1
              } else {
                this.status = 0
              }
            })
        }.itemStyle()
        // Second step page
        Column() {
          Text('Page Two')
            .itemTextStyle()
          Button('change status:' + this.status)
            .backgroundColor('#007dFF')
            .onClick(() => {
              if (this.status < 3) {
                this.status += 1
              } else {
                this.status = 0
              }
            })
        }.itemStyle()
        // Third step page
        Column() {
          Text('Page Three')
            .itemTextStyle()
          Button('change status:' + this.status)
            .backgroundColor('#007dFF')
            .onClick(() => {
              if (this.status < 3) {
                this.status += 1
              } else {
                this.status = 0
              }
            })
        }.itemStyle()
        // Fourth step page
        Column() {
          Text('Page Four')
            .itemTextStyle()
        }.itemStyle()
      }
      .index(this.currentIndex)
      .disableSwipe(true)
      .loop(false)
      .indicator(false)
      .backgroundColor('#fff5f2f2')
      .onChange((index) => {
        console.info("Changed")
        this.currentIndex = index
        this.nextLabel = this.currentIndex == 2? "Next" : "Next"
        this.prevLabel = this.currentIndex == 2? "Back" : "Previous";
      })
      // Bottom buttons
      Row() {
        if (this.currentIndex > 0) {
          Row() {
            SymbolGlyph($r("sys.symbol.chevron\_left"))
              .fontSize(20)
              .margin({ right: 5 })
            Text(this.prevLabel)
            // Use onClick here to replace the onPrevious of the original Stepper.
              .onClick(() => {
                this.swiperController.showPrevious()
              })
          }
          .justifyContent(FlexAlign.Start)
          .width(100)
          .height(20)
          .position({ left: 20 })
        }
        Row() {
          if (this.currentIndex == 3) {
            Text("Start")
            // Use onClick here to replace the onFinish of the original Stepper.
              .onClick(() => {
                console.info("Finish")
              })
          } else if (this.status == 0) {
            Text(this.nextLabel)
            // Use onClick here to replace the onNext of the original Stepper.
              .onClick(() => {
                this.swiperController.showNext()
              })
            SymbolGlyph($r("sys.symbol.chevron\_right"))
              .fontSize(20)
              .margin({ left: 5 })
          } else if (this.status == 1) {
            Text(this.nextLabel)
              .fontColor('#ff818181')
            SymbolGlyph($r("sys.symbol.chevron\_right"))
              .fontSize(20)
              .fontColor(\['#ff818181'\])
              .margin({ left: 5 })
          } else if (this.status == 2) {
            LoadingProgress()
              .width(25)
          } else if (this.status == 3) {
            Text ("Skip")
            // Use onClick here to replace the original onSkip of Stepper.
              .onClick(() => {
                console.info("Skip")
              })
            SymbolGlyph($r("sys.symbol.chevron\_right"))
              .fontSize(20)
              .margin({ left: 5 })
          }
        }
        .justifyContent(FlexAlign.End)
        .width(100)
        .height(20)
        .position({ right: 20 })
      }
      .backgroundColor('#fff5f2f2')
      .position({ bottom: 30 })
      .width("100%")
    }
    .backgroundColor('#fff5f2f2')
    .width("100%")
    .height("100%")
  }
}
