# TapGesture

**TapGesture** is used to trigger a tap gesture with one, two, or more taps.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/8wic4aAmSuu_PIUMw4a5sg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062237Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F6F0E5D9491F1CE7ED115B17B022BA5E3893726236AEAE1C01249A5BCC7BAE3E)

The gesture is supported since API version 7. Updates will be marked with a superscript to indicate their earliest API version.

When both double-tap and single-tap gestures are bound to a component with the double-tap gesture bound first, the single-tap gesture will have a 300 ms delay.

#### APIs

TapGesture(value?: TapGestureParameters)

Creates a tap gesture. Inherits from [GestureInterface<T>](../../gesture-common-apis/document.md#gestureinterfacet11).

When triggered by keyboard or gamepad input, the gesture event's [SourceTool](../../gesture-binding/gesture-binding/document.md#sourcetool9) is **Unknown**, and [SourceType](../../gesture-binding/gesture-binding/document.md#sourcetype8) is **KEY** or **JOYSTICK**.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [TapGestureParameters](#tapgestureparameters12) | No | Parameters for the tap gesture. |

#### TapGestureParameters12+

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/j27XlZlzQaeFbakAuNpv5g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062237Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E7437BA5AA30E0BB68260CC63FDCD486C221EEB954C9A0A5F7225C187DB7EF42)

To standardize anonymous object definitions, the element definitions here have been revised in API version 12. While historical version information is preserved for anonymous objects, there may be cases where the outer element's @since version number is higher than inner elements'. This does not affect interface usability.

Defines tap gesture parameters. Inheritsfrom [BaseHandlerOptions](../../gesture-binding/gesture-handler/document.md#basehandleroptions15).

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| count11+ | number | No | Yes | 
Number of consecutive taps. If the value is less than 1 or is not set, the default value is used.

Default value: **1**

Value range: \[0, +∞).

**NOTE**

1\. If multi-tap is configured, the timeout interval between a lift and the next tap is 300 ms.

2\. If the distance between the last tapped position and the current tapped position exceeds 60 vp, gesture recognition fails. In multi-finger scenarios, the tapped position is the average position of all fingers involved in the gesture response.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| fingers11+ | number | No | Yes | 

Number of fingers required to trigger a tap. The value ranges from 1 to 10. If the value is less than 1 or is not set, the default value is used.

Default value: **1**

**NOTE**

1\. For a multi-finger gesture, recognition fails if the required number of fingers is not pressed within 300 ms after the first finger; when fingers are lifted, if the remaining number of fingers is below the threshold after lifting, all fingers must be lifted within 300 ms for the gesture to be successfully recognized.

2\. When the number of fingers touching the screen exceeds the set value, the gesture can be recognized.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| distanceThreshold | number | No | Yes | 

Movement threshold for the tap gesture. If the value is less than or equal to 0 or is not set, the default value is used.

Default value: 2³¹-1

Unit: vp.

**NOTE**

If the finger movement exceeds the preset movement threshold, the tap gesture recognition fails. If the default threshold is used during initialization and the finger moves beyond the component's touch target, the tap gesture recognition fails.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |

#### Events

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/czx1BwoXT8-vSYiFAWdsyA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062237Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B49050B2F5377A8610B24DBDDFA1202A4BB6ABA85F774E596530FB9A972C5F2F)

The component binds gesture objects of different **GestureType** instances through gesture events. Each gesture object provides gesture-related information in the gesture response event. In the following example, the **TapGesture** object provides gesture-related information in the [onAction](#onaction) event. For details about the event definitions of other gestures, see the corresponding gesture sections. To bind multiple gestures, use [combined gestures](../../combined-gestures/document.md).

In **fingerList** of [GestureEvent](../../gesture-common-apis/document.md#gestureevent), the index of a finger corresponds to its position, that is, the ID of a finger in **fingerList\[index\]** refers to its index. If a finger is pressed first and does not participate in triggering of the current gesture, its position in **fingerList** is left empty. You are advised to use **fingerInfos** when possible.

#### \[h2\]onAction

onAction(event: (event: GestureEvent) => void)

Triggered when the tap gesture is recognized.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | (event: [GestureEvent](../../gesture-common-apis/document.md#gestureevent)) => void | Yes | Callback for the tap event. |

#### EventLocationInfo20+

Provides coordinate information for tap gestures.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| x | number | No | No | 
X coordinate relative to the upper left corner of the component.

Value range: \[0, +∞).

Unit: vp.

 |
| y | number | No | No | 

Y coordinate relative to the upper left corner of the component.

Value range: \[0, +∞).

Unit: vp.

 |
| windowX | number | No | No | 

X coordinate relative to the upper left corner of the window.

Value range: \[0, +∞).

Unit: vp.

 |
| windowY | number | No | No | 

Y coordinate relative to the upper left corner of the window.

Value range: \[0, +∞).

Unit: vp.

 |
| displayX | number | No | No | 

X coordinate relative to the upper left corner of the screen.

Value range: \[0, +∞).

Unit: vp.

 |
| displayY | number | No | No | 

Y coordinate relative to the upper left corner of the screen.

Value range: \[0, +∞).

Unit: vp.

 |

#### Example

## Example 1: Implementing Double-Tap Gesture Recognition

This example demonstrates the recognition of a double-tap gesture using **TapGesture**.

// xxx.ets
@Entry
@Component
struct TapGestureExample {
  @State value: string = '';

  build() {
    Column() {
      // The gesture event is triggered by double-tapping.
      Text('Click twice').fontSize(28)
        .gesture(
        TapGesture({ count: 2 })
          .onAction((event: GestureEvent) => {
            if (event) {
              this.value = JSON.stringify(event.fingerList\[0\])
            }
          })
        )
      Text(this.value)
    }
    .height(300)
    .width(300)
    .padding(20)
    .border({ width: 3 })
    .margin(30)
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/eZdaDAkxQnSH7xrYkBQqlA/en-us_image_0000002537925428.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062237Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D884BDF1859FAEAF30AC037ECD797C2D0957492D05EC5B78333C22218E8C6DDD)

## Example 2: Obtaining Coordinates of a Single-Tap Gesture

This example demonstrates how to obtain the coordinates of a single-tap gesture using **TapGesture**.

// xxx.ets
@Entry
@Component
struct TapGestureExample {

  build() {
    Column() {
      Text('Click Once').fontSize(28)
        .gesture(
          TapGesture({ count: 1, fingers: 1 })
            .onAction((event: GestureEvent | undefined) => {
              if (event) {
                console.info(\`x = ${JSON.stringify(event.tapLocation?.x)}\`)
                console.info(\`y = ${JSON.stringify(event.tapLocation?.y)}\`)
                console.info(\`windowX = ${JSON.stringify(event.tapLocation?.windowX)}\`)
                console.info(\`windowY = ${JSON.stringify(event.tapLocation?.windowY)}\`)
                console.info(\`displayX = ${JSON.stringify(event.tapLocation?.displayX)}\`)
                console.info(\`displayY = ${JSON.stringify(event.tapLocation?.displayY)}\`)
              }
            })
        )
    }
    .height(200)
    .width(300)
    .padding(20)
    .border({ width: 3 })
    .margin(30)
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/5O-lK82PQwer84zPwGGNHg/en-us_image_0000002568685205.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062237Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B1586DBB32575E925ABC887B7A8E59676FB3663A9F4B670AAE6B8A777A9A3797)
