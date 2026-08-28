# RotationGesture

**RotationGesture** is used to trigger a rotation gesture, which recognizes rotational movements using two to five fingers, with a minimum angular change of 1 degree. This gesture cannot be triggered using a two-finger rotation operation on a trackpad.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/J4kjqlLoTm2o2Xb5myGZvQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062237Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0D2E0F03197841DBC82FBA25CB1DC7D893815D700C32683A2A09EECBE49E4EC4)

The initial APIs of this module are supported since API version 7. Updates will be marked with a superscript to indicate their earliest API version.

#### APIs

#### \[h2\]RotationGesture

RotationGesture(value?: { fingers?: number; angle?: number })

Sets the parameters for the rotation gesture. Inherits from [GestureInterface<T>](../../gesture-common-apis/document.md#gestureinterfacet11).

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | { fingers?: number; angle?: number } | No | 
Parameters for the rotation gesture.

\- **fingers**: minimum number of fingers to trigger the rotation gesture.

Default value: **2**

Value range: \[2, 5\]. Values less than 2 or greater than 5 are automatically adjusted to the default value.

While more fingers than the minimum number can be pressed to trigger the gesture, only the first two fingers participate in gesture calculation.

\- **angle**: minimum angular change required to trigger the rotation gesture; unit: deg.

Default value: **1**

**NOTE**

If the value is less than or equal to 0 or greater than 360, it will be converted to the default value.

 |

#### \[h2\]RotationGesture15+

RotationGesture(options?: RotationGestureHandlerOptions)

Sets the parameters for the rotation gesture. Compared with [RotationGesture](#rotationgesture-1), this API adds the **isFingerCountLimited** parameter to **options**, which determines whether to enforce the exact number of fingers touching the screen.

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [RotationGestureHandlerOptions](../../gesture-binding/gesture-handler/document.md#rotationgesturehandleroptions) | No | Parameters of the rotation gesture handler. |

#### Events

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/2HDfKHbmTbeFh0EN_jvHDw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062237Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1F02966AF7F3B251EF4B8FB7560C3BA4544D3E9DC8E52038249B4057F4505E3B)

In **fingerList** of [GestureEvent](../../gesture-common-apis/document.md#gestureevent), the index of a finger corresponds to its position, that is, the ID of a finger in **fingerList\[index\]** refers to its index. If a finger is pressed first and does not participate in triggering of the current gesture, its position in **fingerList** is left empty. You are advised to use **fingerInfos** when possible.

#### \[h2\]onActionStart

onActionStart(event: (event: GestureEvent) => void)

Triggered when the rotation gesture is recognized successfully.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | (event: [GestureEvent](../../gesture-common-apis/document.md#gestureevent)) => void | Yes | Callback for the gesture event. |

#### \[h2\]onActionUpdate

onActionUpdate(event: (event: GestureEvent) => void)

Triggered during the movement of the rotation gesture.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | (event: [GestureEvent](../../gesture-common-apis/document.md#gestureevent)) => void | Yes | Callback for the gesture event. |

#### \[h2\]onActionEnd

onActionEnd(event: (event: GestureEvent) => void)

Triggered when the last finger used for the rotation gesture is lifted.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | (event: [GestureEvent](../../gesture-common-apis/document.md#gestureevent)) => void | Yes | Callback for the gesture event. |

#### \[h2\]onActionCancel

onActionCancel(event: () => void)

Triggered when a tap cancellation event is received after the rotation gesture is recognized. This callback does not return gesture event information.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | () => void | Yes | Callback for the gesture event. |

#### \[h2\]onActionCancel18+

onActionCancel(event: Callback<GestureEvent>)

Triggered when a tap cancellation event is received after the rotation gesture is recognized. Compared with [onActionCancel](#onactioncancel), this callback returns gesture event information.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | Callback<[GestureEvent](../../gesture-common-apis/document.md#gestureevent)\> | Yes | Callback for the gesture event. |

#### Example

This example demonstrates the recognition of a two-finger rotation gesture using **RotationGesture**.

// xxx.ets
@Entry
@Component
struct RotationGestureExample {
  @State angle: number = 0;
  @State rotateValue: number = 0;

  build() {
    Column() {
      Column() {
        Text('RotationGesture angle:' + this.angle)
      }
      .height(200)
      .width(300)
      .padding(20)
      .border({ width: 3 })
      .margin(80)
      .rotate({ angle: this.angle })
      // The gesture event is triggered by rotating with two fingers.
      .gesture(
      RotationGesture()
        .onActionStart((event: GestureEvent) => {
          console.info('Rotation start')
        })
        .onActionUpdate((event: GestureEvent) => {
          if (event) {
            this.angle = this.rotateValue + event.angle
          }
        })
        .onActionEnd((event: GestureEvent) => {
          this.rotateValue = this.angle
          console.info('Rotation end')
        })
      )
    }.width('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/7im-s-KwQieKQOtGL0YFPQ/en-us_image_0000002537765492.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062237Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=404332DC1B7FFCF01BFDA5BA76132BAFAB97E41047DDF0299E99888F45C3D6A9)
