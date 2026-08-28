# Property Animation (animation)

With property animations, you can animate changes to certain component properties, such as [width](../../universal-attributes/layout-and-borders/sizing/document.md#width), [height](../../universal-attributes/layout-and-borders/sizing/document.md#height), [backgroundColor](../../universal-attributes/basic-attributes/background/document.md#backgroundcolor), [opacity](../../universal-attributes/visual-effects/opacity-control/document.md#opacity), [scale](../../universal-attributes/visual-effects/transformation/document.md#scale), [rotate](../../universal-attributes/visual-effects/transformation/document.md#rotate) and [translate](../../universal-attributes/visual-effects/transformation/document.md#translate). In an animation that involves layout (for example, width and height) changes, a component's content (such as text and [canvas](../../canvas-drawing/canvas/document.md) content) is changed straight to the final state. To enable the content to change with the width and height during the animation process, you can use the [renderFit](../../universal-attributes/visual-effects/render-fit/document.md#renderfit) attribute.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d/v3/Vnx9IIRJSE-De8kI6uYM2A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B0493544B8A86ADF4A62FB092144AEF4411FE1FCB6F17A63F861BD5BA58B11B1)

This feature is supported since API version 7. Updates will be marked with a superscript to indicate their earliest API version.

#### animation

animation(value:AnimateParam): T

Sets a property animation for the component.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/ocBnRXPRQy2ve9JYvH84dA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C9B70938A978EBD27982BC52129EC862E4B4D9DF5F358976F2B5236D71ECD7F5)

-   When a single page contains a large number of components with animations, use [renderGroup](../../universal-attributes/visual-effects/image-effect/document.md#rendergroup10) to minimize frame freezing and improve animation performance. For best practices, see [Animation Usage Guide – Using RenderGroup](https://developer.huawei.com/consumer/en/doc/best-practices/bpta-fair-use-animation#section1223162922415).
    
-   This API cannot be called within [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier).
    

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [AnimateParam](../explicit-animation-animateto/document.md#animateparam) | Yes | Animation settings. |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

Property animations only affect attributes that are specified before the **animation** API and do not affect properties of the component constructor.

@Entry
@Component
struct AnimationExample {
  @State widthSize: number = 250;
  @State heightSize: number = 100;
  @State rotateAngle: number = 0;
  @State flag: boolean = true;
  @State space: number = 10;
  
  build() {
    Column() {
      Column({ space: this.space }) // Changing space in the Column constructor will not be animated.
        .onClick(() => {
          if (this.flag) {
            this.widthSize = 150;
            this.heightSize = 60;
            this.space = 20; // Changing this.space will not be animated.
          } else {
            this.widthSize = 250;
            this.heightSize = 100;
            this.space = 10; //  Changing this.space will not be animated.
          }
          this.flag = !this.flag;
        })
        .backgroundColor(Color.Black)
        .margin(30)
        .width(this.widthSize) // Only effective if specified before the animation API.
        .height(this.heightSize) // Only effective if specified before the animation API.
        .animation({
          duration: 2000,
          curve: Curve.EaseOut,
          iterations: 3,
          playMode: PlayMode.Normal
        })
        // .width(this.widthSize) // The animation API does not take effect here.
        // .height(this.heightSize) //  The animation API does not take effect here.
    }
  }
}

#### Example

This example demonstrates property animations using the animation API.

// xxx.ets
@Entry
@Component
struct AttrAnimationExample {
  @State widthSize: number = 250
  @State heightSize: number = 100
  @State rotateAngle: number = 0
  @State flag: boolean = true

  build() {
    Column() {
      Button('change size')
        .onClick(() => {
          if (this.flag) {
            this.widthSize = 150
            this.heightSize = 60
          } else {
            this.widthSize = 250
            this.heightSize = 100
          }
          this.flag = !this.flag
        })
        .margin(30)
        .width(this.widthSize)
        .height(this.heightSize)
        .animation({
          duration: 2000,
          curve: Curve.EaseOut,
          iterations: 3,
          playMode: PlayMode.Normal
        })
      Button('change rotate angle')
        .onClick(() => {
          this.rotateAngle = 90
        })
        .margin(50)
        .rotate({ angle: this.rotateAngle })
        .animation({
          duration: 1200,
          curve: Curve.Friction,
          delay: 500,
          iterations: -1, // The value -1 indicates that the animation is played for an unlimited number of times.
          playMode: PlayMode.Alternate,
          expectedFrameRateRange: {
            min: 20,
            max: 120,
            expected: 90,
          }
        })
    }.width('100%').margin({ top: 20 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/_F2qfF1EQM6In8o-D6GumQ/en-us_image_0000002568685611.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D1CDE7A0A5F4BFF8B51BAAF99D33207AD824BFA37D1A798F2153F81A9A1E22A9)
