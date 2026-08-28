# Immediate Delivery of Explicit Animation (animateToImmediately)

The **animateToImmediately** API implements immediate delivery for [explicit animations](../explicit-animation-animateto/document.md). When multiple property animations are loaded at once, you can call this API to immediately execute the transition animation for state changes caused by the specified closure function.

Unlike [animateTo](../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-uicontext/document.md#animateto), which waits for the VSync signal, **animateToImmediately** instantly sends animation commands to the rendering layer for execution. This is particularly useful in scenarios where you need to prioritize certain animations or update part of the UI in advance, especially when your application's main thread is occupied with time-consuming operations. Note that **animateToImmediately** is limited to property animations on the rendering layer, and cannot be used for frame-by-frame animations on the UI side.

In addition, this API captures the current state at the time of the call and sends it alongside the newly generated animation to the rendering layer. This means that the rendering output will reflect the state at the time of the call. Ensure that the state is complete when the API is called. Otherwise, rendering exceptions may occur in the first few frames.

Therefore, you are advised to use [animateTo](../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-uicontext/document.md#animateto) to prevent interference with the display timing of the framework and avoid potential display errors caused by incomplete state settings at the start of the animation.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/ahPTBIDVQZ62Srdoux3Ylg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7D02CF01D07C1B14A2857213A0059E13D716FF8462ECBB158BBD2170E849B2E7)

The initial APIs of this module are supported since API version 12. Updates will be marked with a superscript to indicate their earliest API version.

#### APIs

#### animateToImmediately

animateToImmediately(value: AnimateParam , event: () => void): void

Delivers an explicit animation immediately.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [AnimateParam](../explicit-animation-animateto/document.md#animateparam) | Yes | Animation settings. |
| event | () => void | Yes | Closure function that displays the animation. The system automatically inserts a transition animation for state changes caused by the closure function. |

#### Example

This example demonstrates how to use the [animateToImmediately](#animatetoimmediately) API to deliver an explicit animation immediately.

// xxx.ets
@Entry
@Component
struct AnimateToImmediatelyExample {
  @State widthSize: number = 250;
  @State heightSize: number = 100;
  @State opacitySize: number = 0;
  private flag: boolean = true;

  build() {
    Column() {
      Column()
      .width(this.widthSize)
      .height(this.heightSize)
      .backgroundColor(Color.Green)
      .opacity(this.opacitySize)
      Button('change size')
        .margin(30)
        .onClick(() => {
          if (this.flag) {
            animateToImmediately({
              delay: 0,
              duration: 1000
            }, () => {
              this.opacitySize = 1;
            })
            this.getUIContext()?.animateTo({
              delay: 1000,
              duration: 1000
            }, () => {
              this.widthSize = 150;
              this.heightSize = 60;
            })
          } else {
            animateToImmediately({
              delay: 0,
              duration: 1000
            }, () => {
              this.widthSize = 250;
              this.heightSize = 100;
            })
            this.getUIContext()?.animateTo({
              delay: 1000,
              duration: 1000
            }, () => {
              this.opacitySize = 0;
            })
          }
          this.flag = !this.flag;
        })
    }.width('100%').margin({ top: 5 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1/v3/02uGXofeRRWlut003xLuRg/en-us_image_0000002568765631.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=658898CABAE29338E578F6B82AFF202E301BE4E8C9739386CE85EDBD42996A3A)
