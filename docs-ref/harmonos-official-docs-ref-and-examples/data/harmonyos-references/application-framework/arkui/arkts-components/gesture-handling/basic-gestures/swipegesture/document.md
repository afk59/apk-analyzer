# SwipeGesture

**SwipeGesture** is used to trigger a swipe gesture. This gesture is successfully recognized when the swipe speed exceeds the specified threshold, which is 100 vp/s by default.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/QoG60VJZT9CE78bzrSvWgA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062237Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=38D04CC602FACE9BC45754C1225B35858ABC63B611F3D13F81C88A270CA8CF0F)

This gesture is supported since API version 8. Updates will be marked with a superscript to indicate their earliest API version.

#### APIs

#### \[h2\]SwipeGesture

SwipeGesture(value?: { fingers?: number; direction?: SwipeDirection; speed?: number })

Sets the parameters for the swipe gesture. Inherits from [GestureInterface<T>](../../gesture-common-apis/document.md#gestureinterfacet11).

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | { fingers?: number; direction?: SwipeDirection; speed?: number } | No | 
Parameters for the swipe gesture.

\- **fingers**: minimum number of fingers to trigger the swipe gesture.

Default value: **1**

Value range: \[1, 10\].

\- **direction**: direction in which the swipe gesture can be recognized.

Default value: **SwipeDirection.All**

\- **speed**: minimum speed of the swipe gesture.

Default value: 100 vp/s

Value range: (0, +∞).

**NOTE**

If the value is less than or equal to 0, it will be converted to the default value.

 |

#### \[h2\]SwipeGesture15+

SwipeGesture(options?: SwipeGestureHandlerOptions)

Sets the parameters for the swipe gesture. Compared with [SwipeGesture](#swipegesture-1), this API adds the **isFingerCountLimited** parameter to **options**, which determines whether to enforce the exact number of fingers touching the screen.

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [SwipeGestureHandlerOptions](../../gesture-binding/gesture-handler/document.md#swipegesturehandleroptions) | No | Parameters of the swipe gesture handler. |

#### SwipeDirection

Enumerates the directions in which the swipe gesture can be recognized.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| All | \- | All directions. |
| Horizontal | \- | Horizontal direction. The gesture is triggered when the angle between the finger moving direction and the x-axis is less than 45 degrees. |
| Vertical | \- | Vertical direction. The gesture is triggered when the angle between the finger moving direction and the y-axis is less than 45 degrees. |
| None | \- | Swiping disabled. |

#### Events

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/MZ4uunjyQbKRJp5PZVC-dg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062237Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B6A402B9C4510F0B41F124354DF4BA34E6FE07683A402B11C73D9A7F9B8EA544)

In **fingerList** of [GestureEvent](../../gesture-common-apis/document.md#gestureevent), the index of a finger corresponds to its position, that is, the ID of a finger in **fingerList\[index\]** refers to its index. If a finger is pressed first and does not participate in triggering of the current gesture, its position in **fingerList** is left empty. You are advised to use **fingerInfos**.

#### \[h2\]onAction

onAction(event: (event: GestureEvent) => void)

Triggered when the swipe gesture is recognized.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | (event: [GestureEvent](../../gesture-common-apis/document.md#gestureevent)) => void | Yes | Callback for the gesture event. |

#### Example

This example demonstrates how to implement swipe gesture recognition.

// xxx.ets
@Entry
@Component
struct SwipeGestureExample {
  @State rotateAngle: number = 0;
  @State speed: number = 1;

  build() {
    Column() {
      Column() {
        Text("SwipeGesture speed\\n" + this.speed)
        Text("SwipeGesture angle\\n" + this.rotateAngle)
      }
      .border({ width: 3 })
      .width(300)
      .height(200)
      .margin(100)
      .rotate({ angle: this.rotateAngle })
      // This event is triggered when the user swipes vertically with one finger.
      .gesture(
      SwipeGesture({ direction: SwipeDirection.Vertical })
        .onAction((event: GestureEvent) => {
          if (event) {
            this.speed = event.speed
            this.rotateAngle = event.angle
          }
        })
      )
    }.width('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/MkBmIR1TQG-0pOeZ_AeKpQ/en-us_image_0000002537925432.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062237Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8CC74C793CDEE991202265F65576DBB76EC5E228840A5FDEC4FF74F6297201E6)
