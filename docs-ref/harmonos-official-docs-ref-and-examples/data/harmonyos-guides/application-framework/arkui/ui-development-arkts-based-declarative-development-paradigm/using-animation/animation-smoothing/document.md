# Animation Smoothing

When running animations, the UI is also interacting with users in real time. It must respond immediately to changes in user behavior. For example, if the user swipes up to exit in the midst of an application launch process, the UI should immediately transit from the startup animation to the exit animation, rather than finishing the startup animation before exiting. In the scenario where the animation triggered when the user lifts their fingers off the screen, the initial velocity of the animation must inherit the gesture speed, so as to avoid pauses caused by speed disconnection. For the preceding and similar scenarios, the system provides efficient APIs for smoothing between animations and between animations and gestures.

Assume that there is a running animation for an animatable property. If the end value of the property changes due to an operation on the UI, you can create a new animation for it, by changing the property value in the [animateTo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-explicit-animation) closure or by changing the input parameter value of the [animation](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-animatorproperty) API. The system then automatically connects the previous animation with the new animation.

The following example demonstrates how clicking the **Click** button changes the scale property of the red square. When you click **Click** repeatedly, the target value of the **scale** property changes continuously, and the animation smoothly moves toward the new target value.

import { curves } from '@kit.ArkUI';

class SetAnimationVariables {
  isAnimation: boolean = true

  set(): void {
    this.isAnimation = !this.isAnimation;
  }
}

@Entry
@Component
struct AnimationToAnimationDemo {
  // Step 1: Declare the related state variable.
  @State animationController: SetAnimationVariables = new SetAnimationVariables();

  build() {
    Column() {
      Text('ArkUI')
        .fontWeight(FontWeight.Bold)
        .fontSize(12)
        .fontColor(Color.White)
        .textAlign(TextAlign.Center)
        .borderRadius(10)
        .backgroundColor(0xf56c6c)
        .width(100)
        .height(100)
        .scale({
          // Step 2: Set the declared state variable to the related animatable property.
          x: this.animationController.isAnimation ? 2 : 1,
          y: this.animationController.isAnimation ? 2 : 1
        })
        .animation({ curve: curves.springMotion(0.4, 0.8) }) // Step 4: Enable animation. When the animation target value changes, the system automatically applies smooth transition.

      Button('Click')
        .margin({ top: 200 })
        .onClick(() => {
          // Step 3: Change the state variable value through the click event, which updates the property value.
          this.animationController.set()
        })
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/odW5Z7i0RaagT7JrqJxXTA/en-us_image_0000002537924758.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061938Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DF2F7C8A238EB4ED928E52DDC9AAC935E38BB039F57379AB117E0449AEE08FCB)

#### Smoothing Between Gestures and Animations

In scenarios where gestures are used, a property change is generally triggered when the user places or moves their finger (or fingers) on the screen, and continues after the user lifts their finger (or fingers) off the screen until the end value of the property is reached.

The initial velocity of the property change after the user lifts their finger (or fingers) should be consistent with the velocity of the property change at the moment before the user lifts their finger (or fingers). If the former is **0**, it feels like a running car stops suddenly, an unusual abrupt change not comfortable to users.

In cases where smoothing between [tap gestures](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-gestures-tapgesture) and [animations](../animation-overview/document.md) is critical, for example, when scrolling a list, you can apply a responsive spring curve to the property animation running when the user places or moves their finger (or fingers) on the screen; and apply a spring curve to the property animation running after the user lifts their finger (or fingers) off the screen. For the animation following the [springMotion](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-curve#curvesspringmotion9) curve, its portion that is running after the user lifts their finger (or fingers) off the screen automatically inherits the previous velocity and starts from where the previous portion leaves off.

The following example implements a ball moving smoothly with the gesture.

import { curves } from '@kit.ArkUI';
import { hilog } from '@kit.PerformanceAnalysisKit';

const DOMAIN = 0x0000;
const TAG: string = '\[AnimatorTest\]';

@Entry
@Component
struct SpringMotionDemo {
  // Step 1: Declare the related state variable.
  @State positionX: number = 100;
  @State positionY: number = 100;
  diameter: number = 50;

  build() {
    Column() {
      Row() {
        Circle({ width: this.diameter, height: this.diameter })
          .fill(Color.Blue)
          .position ({x: this.positionX, y: this.positionY})// Step 2: Set the declared state variable to the related animatable property.
          .onTouch((event?: TouchEvent) => {
            // Step 3: Change the state variable value for the time when the user places or moves their finger (or fingers) on the screen and use responsiveSpringMotion for movement toward the new value.
            if (event) {
              if (event.type === TouchType.Move) {
                // When the user places or moves their finger on the screen, use the responsiveSpringMotion curve.
                this.getUIContext()?.animateTo({ curve: curves.responsiveSpringMotion() }, () => {
                  // Subtract the radius so that the center of the ball moves to where the finger is placed.
                  this.positionX = event.touches\[0\].windowX - this.diameter / 2;
                  this.positionY = event.touches\[0\].windowY - this.diameter / 2;
                  hilog.info(DOMAIN, TAG, \`move, animateTo x:${this.positionX}, y:${this.positionY}\`);
                })
              } else if (event.type === TouchType.Up) {
                // Step 4: Set the end value of the state variable for after the user lifts their finger (or fingers), and use springMotion for movement toward the new value. The springMotion animation inherits the previous velocity.
                this.getUIContext()?.animateTo({ curve: curves.springMotion() }, () => {
                  this.positionX = 100;
                  this.positionY = 100;
                  hilog.info(DOMAIN, TAG, \`touchUp, animateTo x:100, y:100\`);
                })
              }
            }
          })
      }
      .width('100%').height('80%')
      .clip(true) // If the ball moves beyond the parent component, it is invisible.
      .backgroundColor(Color.Orange)

      Flex({ direction: FlexDirection.Row, alignItems: ItemAlign.Start, justifyContent: FlexAlign.Center }) {
        // Replace $r('app.string.drag') with the actual resource file. In this example, the value in the resource file is "Drag the ball."
        Text($r('app.string.drag')).fontSize(16)
      }
      .width('100%')

      Row() {
        // Replace $r('app.string.location') with the actual resource file. In this example, the value in the resource file is "Clicked at:".
        Text($r('app.string.location') + ' \[x: ' + Math.round(this.positionX) + ', y:' + Math.round(this.positionY) + '\]').fontSize(16)
      }
      .padding(10)
      .width('100%')
    }.height('100%').width('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/fT59Ag2CSpaVNlTe-ZqdSg/en-us_image_0000002568684535.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061938Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=714E3BC878525180673E95977A5F64E3C4D4381FA1CDD4ADE363DE6E22309F42)
