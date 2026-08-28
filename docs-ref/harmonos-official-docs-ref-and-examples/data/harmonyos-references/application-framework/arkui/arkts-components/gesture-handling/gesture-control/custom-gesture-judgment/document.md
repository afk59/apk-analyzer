# Custom Gesture Judgment

You can use the custom gesture judgment APIs to specify whether to respond to specific gestures when they are being recognized.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/dyxN0Vg1S6aLVHAlNJpEdA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062237Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=64C1DAAF079D010ED8F4242414CCD48417FCA9693E08B0FC1B4CFB352594907A)

This feature is supported since API version 11. Updates will be marked with a superscript to indicate their earliest API version.

#### onGestureJudgeBegin

onGestureJudgeBegin(callback: (gestureInfo: GestureInfo, event: BaseGestureEvent) => GestureJudgeResult): T

Binds a custom gesture determination callback to the component. When the gesture is about to succeed, the user-defined callback is triggered to obtain the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | (gestureInfo: [GestureInfo](../../gesture-common-apis/document.md#gestureinfo11), event: [BaseGestureEvent](../../gesture-common-apis/document.md#basegestureevent11)) => [GestureJudgeResult](../../gesture-common-apis/document.md#gesturejudgeresult11) | Yes | Custom gesture judgment callback. When the gesture is about to succeed, the user-defined callback is triggered to obtain the result. |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### BaseEvent8+

Basic event type.

#### \[h2\]Properties

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| target | [EventTarget](../../../universal-events/interaction-response-events/click-event/document.md#eventtarget8) | No | No | 
Object that triggers the gesture event.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| timestamp | number | No | No | 

Timestamp of the event. It is the interval between the time when the event is triggered and the time when the system starts.

Unit: ns

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| source | [SourceType](../../gesture-binding/gesture-binding/document.md#sourcetype8) | No | No | 

Type of the event input device.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| pressure9+ | number | No | No | 

Press pressure.

Default value: **0**

Value range: \[0, 1\], typical value 0.913168, where higher values indicate greater pressure. On some devices, the return value may be greater than 1 due to different hardware parameter configurations.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| tiltX9+ | number | No | No | 

Angle between the projection of the stylus on the device plane and the x-axis.

Default value: **0**

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| tiltY9+ | number | No | No | 

Angle between the projection of the stylus on the device plane and the y-axis.

Default value: **0**

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| rollAngle17+ | number | No | Yes | 

Angle between the stylus and the device's surface.

**Widget capability**: This API can be used in ArkTS widgets since API version 17.

**Atomic service API**: This API can be used in atomic services since API version 17.

 |
| sourceTool9+ | [SourceTool](../../gesture-binding/gesture-binding/document.md#sourcetool9) | No | No | 

Event input source type.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| axisHorizontal12+ | number | No | Yes | 

Horizontal axis value.

Default value: **0**

**NOTE**

This value is available only when the pan gesture is triggered by mouse wheel scrolling or two-finger touchpad sliding, or when the pinch gesture is triggered by Ctrl + mouse wheel scrolling.

In the horizontal scrolling scenario triggered by Shift + mouse wheel scrolling, **axisHorizontal** is **0**, and the scrolling value is reflected in **axisVertical**.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| axisVertical12+ | number | No | Yes | 

Vertical axis value.

Default value: **0**

**NOTE**

This value is available only when the pan gesture is triggered by mouse wheel scrolling or two-finger touchpad sliding, or when the pinch gesture is triggered by Ctrl + mouse wheel scrolling.

In the horizontal scrolling scenario triggered by Shift + mouse wheel scrolling, the scrolling value is reflected in **axisVertical**.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| axisPinch21+ | number | No | Yes | 

Two-finger pinch scaling ratio.

Default value: **0**

**NOTE**

This value is available only when a pinch gesture is triggered by a two-finger scaling operation on a touchpad or during axis events.

In other scenarios, the default value is returned. The scaling ratio represents the ratio of the current two-finger distance to the initial two-finger distance when first pressed during a pinch gesture.

Value range: \[0, +∞)

**Widget capability**: This API can be used in ArkTS widgets since API version 21.

**Atomic service API**: This API can be used in atomic services since API version 21.

 |
| deviceId12+ | number | No | Yes | 

ID of the input device that triggers the event.

Default value: **0**

Value range: \[0, +∞)

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| targetDisplayId15+ | number | No | Yes | 

ID of the screen where the event occurs.

Default value: **0**

Value range: \[0, +∞)

**Atomic service API**: This API can be used in atomic services since API version 15.

 |

#### \[h2\]getModifierKeyState12+

getModifierKeyState?(keys: Array<string>): boolean

Obtains the pressed status of modifier keys. For details about the error message, see the following error codes. The Ctrl, Alt, and Shift keys are supported.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/Pcw_2te2Sb6FTVPgebXMVA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062237Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=81E7B3FF2E7A53B3C3D5A6ED39090DA72E7BF5C9736A26C94BDE170594C35D60)

This API is not supported in stylus scenarios.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| keys | Array<string> | Yes | Modifier key list. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Pressed status of modifier keys. Returns **true** if all modifier keys are pressed; returns **false** otherwise. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types. 2. Parameter verification failed. |

#### Example

## Example 1: Implementing Custom Gesture Judgment

This example demonstrates how to implement custom judgment for long press, swipe, and pan gestures using [onGestureJudgeBegin](#ongesturejudgebegin). Starting from API version 21, **axisPinch** property of [BaseEvent](#baseevent8) can be used to obtain the two-finger pinch scale ratio.

// xxx.ets
@Entry
@Component
struct Index {
  @State message: string = '';

  build() {
    Column() {
      Row({ space: 20 }) {
        Text(this.message).width(200).height(80).backgroundColor(Color.Pink)
          .fontSize(25)
      }.margin(20)
    }
    .width('100%')
    .height(200)
    .borderWidth(2)
    .onDragStart(() => {
      this.message = 'drag'
      console.info("Drag start.")
    })
    .gesture(
      TapGesture()
        .tag("tap1")// Tag for the tap gesture.
        .onAction(() => {
          this.message = 'tap1'
        })
    )
    .gesture(
      LongPressGesture()
        .tag("longPress1")// Tag for the long press gesture.
        .onAction(() => {
          this.message = 'longPress'
        })
    )
    .gesture(
      SwipeGesture()
        .tag("swipe1")// Tag for the swipe gesture.
        .onAction(() => {
          this.message = 'swipe1'
        })
    )
    .gesture(
      PanGesture()
        .tag("pan1")// Tag for the pan gesture.
        .onActionStart(() => {
          this.message = 'pan1'
        })
    )
    .gesture(
      PinchGesture()
        .tag("pinch1")// Tag for the pinch gesture.
        .onActionStart(() => {
          this.message = 'pinch1'
        })
    )
    .onGestureJudgeBegin((gestureInfo: GestureInfo, event: BaseGestureEvent) => {
      // If the gesture type is a long press gesture, convert the event to a long press gesture event.
      if (gestureInfo.type == GestureControl.GestureType.LONG\_PRESS\_GESTURE) {
        let longPressEvent = event as LongPressGestureEvent;
        console.info(\`repeat ${longPressEvent.repeat}\`)
      }
      // If the gesture type is a swipe gesture, convert the event to a swipe event.
      if (gestureInfo.type == GestureControl.GestureType.SWIPE\_GESTURE) {
        let swipeEvent = event as SwipeGestureEvent;
        console.info(\`angle ${swipeEvent.angle}\`)
      }
      // If the gesture type is a swipe gesture, convert the event to a swipe gesture event.
      if (gestureInfo.type == GestureControl.GestureType.PAN\_GESTURE) {
        let panEvent = event as PanGestureEvent;
        console.info(\`velocity ${panEvent.velocity}\`)
      }
      // If the gesture type is a pinch gesture, convert the event to a pinch event.
      if (gestureInfo.type == GestureControl.GestureType.PINCH\_GESTURE) {
        let pinchEvent = event as PinchGestureEvent;
        console.info(\`axisPinch ${pinchEvent.axisPinch}\`)
      }
      // Custom criteria
      if (gestureInfo.type == GestureControl.GestureType.DRAG) {
        // If GestureJudgeResult.REJECT is returned, the pan gesture recognition fails.
        return GestureJudgeResult.REJECT;
      } else if (gestureInfo.tag === 'longPress1' && event.fingerList.length > 0 && event.fingerList\[0\].localY < 100) {
        // If GestureJudgeResult.CONTINUE is returned, the system recognition result is retained.
        return GestureJudgeResult.CONTINUE;
      }
      return GestureJudgeResult.CONTINUE;
    })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/qp1q_hcaQgm5rjVXB0jUEw/en-us_image_0000002537765494.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062237Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=481B550D17591F0F89582658B8F74049D38BCDBCF83254612F1DF8B528C84AD9)

## Example 2: Implementing Custom Area Gesture Judgment

This example demonstrates how to use **onGestureJudgeBegin** to determine whether to respond to long press and pan gestures based on the area.

// xxx.ets
import { PromptAction } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  scroller: Scroller = new Scroller()
  promptAction: PromptAction = this.getUIContext().getPromptAction();

  build() {
    Scroll(this.scroller) {
      Column({ space: 8 }) {
        Text("The upper red area is bound to the long press gesture, and the lower blue area is bound to a drag gesture. If a pan is performed after a long press in the upper red area, the area only responds to the long press. In the same case, the lower blue area only responds to the drag.")
          .width('100%')
          .fontSize(20)
          .fontColor('0xffdd00')
          .backgroundColor(0xeeddaa00)
        Stack({ alignContent: Alignment.Center }) {
          Column() {
            // Simulate the upper and lower half areas.
            Stack().width('200vp').height('100vp').backgroundColor(Color.Red)
            Stack().width('200vp').height('100vp').backgroundColor(Color.Blue)
          }.width('200vp').height('200vp')

          // The lower part of the Stack component is the image area bound to the pan gesture.
          Image($r('sys.media.ohos\_app\_icon'))
            .draggable(true)
            .onDragStart(() => {
              this.promptAction.showToast({ message: "When the blue area is dragged, the image responds." })
            })
            .width('200vp').height('200vp')
          // The upper part of the Stack component is the floating area bound to the long press gesture.
          Stack() {
          }
          .width('200vp')
          .height('200vp')
          .hitTestBehavior(HitTestMode.Transparent)
          .onGestureJudgeBegin((gestureInfo: GestureInfo, event: BaseGestureEvent) => {
            // Check whether the tag of gestureInfo has a value.
            if (gestureInfo.tag) {
              console.info(\`gestureInfo tag ${gestureInfo.tag.toString()}\`)
            }
            console.info(\`gestureInfo Type ${gestureInfo.type.toString()}\`);
            console.info(\`isSystemGesture ${gestureInfo.isSystemGesture}\`);
            console.info(\`zqs pressure ${event.pressure}\\nfingerList.length ${event.fingerList.length}\\ntimeStamp ${event.timestamp}\\nsourceType ${event.source.toString()}\\n\` +
              \`tiltX ${event.tiltX}\\ntiltY ${event.tiltY}\\nrollAngle ${event.rollAngle}\\nsourcePool ${event.sourceTool.toString()}\`);
            // If the gesture is a long press gesture, check whether the touch position is in the upper half area.
            if (gestureInfo.type == GestureControl.GestureType.LONG\_PRESS\_GESTURE) {
              if (event.fingerList.length > 0 && event.fingerList\[0\].localY < 100) {
                return GestureJudgeResult.CONTINUE
              } else {
                return GestureJudgeResult.REJECT
              }
            }
            return GestureJudgeResult.CONTINUE
          })
          .gesture(GestureGroup(GestureMode.Parallel,
            LongPressGesture()
              .onAction((event: GestureEvent) => {
                this.promptAction.showToast({ message: "Long-press the upper red area. The red area responds." })
              })
              .tag("tap111")
          ))

        }.width('100%')
      }.width('100%')
    }
  }
}

## Example 3: Implementing Real-time Monitoring of Active Touch Points in Gestures

This example demonstrates real-time monitoring of active touch points participating in gestures, including their count, IDs, and coordinates, by configuring **fingerInfos**.

// xxx.ets
@Entry
@Component
struct GestureDetectorExample {
  @State message: string = 'Touch area'
  @State fingerCount: number = 0
  @State fingerDetails: string = ''

  build() {
    Column() {
      // Information display area
      Column() {
        Text(this.message)
          .fontSize(20)
          .fontWeight(FontWeight.Bold)

        Text(\`Active touch points: ${this.fingerCount}\`)
          .fontSize(16)
          .margin({ top: 8 })

        Text(this.fingerDetails)
          .fontSize(14)
          .margin({ top: 8 })
      }
      .padding(10)
      .border({ width: 1, color: Color.Gray })

      // Gesture detection area
      Column()
        .width('90%')
        .height(200)
        .margin(20)
        .border({ width: 2, color: Color.Black })
        .gesture(
          GestureGroup(GestureMode.Exclusive,
            TapGesture()
              .onAction(() => {
                this.message = 'Tap event'
              }),
            LongPressGesture()
              .onAction(() => {
                this.message = 'Long press event'
              }),
            PanGesture()
              .onActionStart(() => {
                this.message = 'Drag started'
              })
              .onActionUpdate(() => {
                this.message = 'Dragging...'
              })
              .onActionEnd(() => {
                this.message = 'Drag ended'
                this.fingerCount = 0
                this.fingerDetails = ''
              })
          )
        )
        .onGestureJudgeBegin((gestureInfo: GestureInfo, event: BaseGestureEvent) => {
          // Access fingerInfos data.
          if (event?.fingerInfos) {
            this.fingerCount = event.fingerInfos.length
            this.fingerDetails = event.fingerInfos.map(finger =>
            \`ID: ${finger.id}: (${finger.localX.toFixed(1)}, ${finger.localY.toFixed(1)})\`
            ).join('\\n')
            console.info(\`Touch point data: ${JSON.stringify(event.fingerInfos)}\`)
          }
          if (this.fingerCount > 2) {
            return GestureJudgeResult.REJECT
          }
          return GestureJudgeResult.CONTINUE
        })
    }
    .width('100%')
    .height('100%')
    .padding(10)
  }
}
