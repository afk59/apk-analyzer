# PanGesture

**PanGesture** is used to trigger a pan gesture when the movement distance of a finger on the screen reaches the minimum value.

The table below describes the scenarios that can trigger a pan gesture:

| Trigger Mode | Input Source Type | Input Device Type | Remarks |
| :-- | :-- | :-- | :-- |
| Swiping with a finger press | [SourceTool](../../gesture-binding/gesture-binding/document.md#sourcetool9).Finger | [SourceType](../../gesture-binding/gesture-binding/document.md#sourcetype8).TouchScreen | Both **axisVertical** and **axisHorizontal** are 0. |
| Swiping with a left mouse button press | [SourceTool](../../gesture-binding/gesture-binding/document.md#sourcetool9).MOUSE | [SourceType](../../gesture-binding/gesture-binding/document.md#sourcetype8).Mouse | Both **axisVertical** and **axisHorizontal** are 0. |
| Scrolling with a mouse wheel | [SourceTool](../../gesture-binding/gesture-binding/document.md#sourcetool9).MOUSE | [SourceType](../../gesture-binding/gesture-binding/document.md#sourcetype8).Mouse | Either **axisVertical** or **axisHorizontal** is non-zero. |
| Swiping after pressing the left button on a touchpad | [SourceTool](../../gesture-binding/gesture-binding/document.md#sourcetool9).MOUSE | [SourceType](../../gesture-binding/gesture-binding/document.md#sourcetype8).Mouse | Both **axisVertical** and **axisHorizontal** are 0. |
| Swiping with two fingers on a touchpad | [SourceTool](../../gesture-binding/gesture-binding/document.md#sourcetool9).TOUCHPAD | [SourceType](../../gesture-binding/gesture-binding/document.md#sourcetype8).Mouse | Either **axisVertical** or **axisHorizontal** is non-zero. |
| Swiping with a stylus | [SourceTool](../../gesture-binding/gesture-binding/document.md#sourcetool9).Pen | [SourceType](../../gesture-binding/gesture-binding/document.md#sourcetype8).TouchScreen | Both **axisVertical** and **axisHorizontal** are 0. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/1JX_4FZVRiSBL7LGBK2Mlg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062237Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C0D6AA45DDF4F3F8F7D1C77784DB3DAE5BA384852DC7EBDA295D48A1DCC6D834)

This API is supported since API version 7. Updates will be marked with a superscript to indicate their earliest API version.

#### APIs

#### \[h2\]PanGesture

PanGesture(value?: { fingers?: number; direction?: PanDirection; distance?: number } | PanGestureOptions)

Creates a pan gesture. Inherits from [GestureInterface<T>](../../gesture-common-apis/document.md#gestureinterfacet11).

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | { fingers?: number; direction?: [PanDirection](#pandirection); distance?: number } | [PanGestureOptions](#pangestureoptions) | No | 
Parameters for the pan gesture.

\- **fingers**: minimum number of fingers to trigger a pan gesture. The value ranges from 1 to 10.

Default value: **1**

Value range: \[1, 10\]

**NOTE**

If the value is less than 1 or is not set, the default value is used.

\- **direction**: pan direction. The value supports the AND (&) and OR (|) operations.

Default value: **PanDirection.All**

\- **distance**: minimum pan distance to trigger the gesture, in vp.

Value range: \[0, +∞)

Default value: **8** for the stylus and **5** for other input sources.

**NOTE**

If a pan gesture and a [tab](../../../navigation-and-switching/tabs/document.md) swipe occur at the same time, set **distance** to **1** to make the gesture more easily recognizable.

If the value specified is less than **0**, the default value is used.

When the [scale](../../../universal-attributes/visual-effects/transformation/document.md#scale) attribute is applied to the component, the actual pan distance is adjusted based on the **scale** ratio.

 |

#### \[h2\]PanGesture15+

PanGesture(options?: PanGestureHandlerOptions)

Creates a pan gesture. Compared with [PanGesture](#pangesture-1), this API adds the **isFingerCountLimited** and **distanceMap** parameters to **options**, which control whether to enforce the exact number of fingers touching the screen and specify the minimum pan distance required to trigger the gesture for different input sources, respectively.

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [PanGestureHandlerOptions](../../gesture-binding/gesture-handler/document.md#pangesturehandleroptions) | No | Parameters of the swipe gesture handler. |

#### PanDirection

Enumerates the pan directions. Unlike **SwipeDirection**, **PanDirection** has no angular restrictions.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| All | \- | All directions. |
| Horizontal | \- | Horizontal direction. |
| Vertical | \- | Vertical direction. |
| Left | \- | Leftward. |
| Right | \- | Rightward. |
| Up | \- | Upward. |
| Down | \- | Downward. |
| None | \- | Panning disabled. |

#### PanGestureOptions

#### \[h2\]constructor

constructor(value?: { fingers?: number; direction?: PanDirection; distance?: number })

Creates a pan gesture configuration object. The **PanGestureOptions** API enables dynamic updates to pan gesture properties without requiring state variable modifications that would trigger UI re-renders.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | { fingers?: number; direction?: [PanDirection](#pandirection); distance?: number } | No | 
Pan gesture configuration.

**fingers**: minimum number of fingers required. The value ranges from 1 to 10.

Default value: **1**

**direction**: pan direction. The value supports the AND (&) and OR (|) operations.

Default value: **PanDirection.All**

**distance**: minimum pan distance to trigger the gesture, in vp.

Default value: **8** for the stylus and **5** for other input sources.

**NOTE**

If a pan gesture and a [tab](../../../navigation-and-switching/tabs/document.md) swipe occur at the same time, set **distance** to **1** to make the gesture more easily recognizable.

If the value specified is less than **0**, the default value is used.

To avoid slow response and lagging during scrolling, set a reasonable pan distance.

When the [scale](../../../universal-attributes/visual-effects/transformation/document.md#scale) attribute is applied to the component, the actual pan distance is adjusted based on the **scale** ratio.

 |

#### \[h2\]setDirection

setDirection(value: PanDirection)

Sets the pan direction.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [PanDirection](#pandirection) | Yes | 
Pan direction. The value supports the AND (&) and OR (|) operations.

Default value: **PanDirection.All**

 |

#### \[h2\]setDistance

setDistance(value: number)

Sets the minimum pan distance to trigger the gesture, in vp. To avoid performance degradation due to excessive response delays or accidental releases, avoid excessively large values. For best practices, see [Reducing the Pan Distance for Gesture Recognition](https://developer.huawei.com/consumer/en/doc/best-practices/bpta-application-latency-optimization-cases#section1116134115286).

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | Yes | 
Minimum pan distance to trigger the gesture, in vp.

Default value: **8** for the stylus and **5** for other input sources.

**NOTE**

If a pan gesture and a [tab](../../../navigation-and-switching/tabs/document.md) swipe occur at the same time, set **distance** to **1** to make the gesture more easily recognizable.

If the value specified is less than **0**, the default value is used.

To avoid slow response and lagging during scrolling, set a reasonable pan distance.

When the [scale](../../../universal-attributes/visual-effects/transformation/document.md#scale) attribute is applied to the component, the actual pan distance is adjusted based on the **scale** ratio.

 |

#### \[h2\]setFingers

setFingers(value: number)

Sets the minimum number of fingers to trigger the gesture.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | Yes | 
Minimum number of fingers to trigger a pan gesture. The value ranges from 1 to 10.

Default value: **1**

 |

#### \[h2\]getDirection12+

getDirection(): PanDirection

Obtains the pan direction.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| [PanDirection](#pandirection) | Pan direction. |

#### \[h2\]getDistance18+

getDistance(): number

Obtains the minimum pan distance to trigger the gesture.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| number | Minimum pan distance to trigger the gesture. |

#### Events

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/J4oJenSiQhCeikPUHwSHPA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062237Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DECF938798F9C2886DE974F4CBE4D4D5C9975CFE56F558600B3409B0A034279B)

In **fingerList** of [GestureEvent](../../gesture-common-apis/document.md#gestureevent), the index of a finger corresponds to its position, that is, the ID of a finger in **fingerList\[index\]** refers to its index. If a finger is pressed first and does not participate in triggering of the current gesture, its position in **fingerList** is left empty. You are advised to use **fingerInfos** when possible.

#### \[h2\]onActionStart

onActionStart(event: (event: GestureEvent) => void)

Registers the callback for successful pan gesture recognition.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | (event: [GestureEvent](../../gesture-common-apis/document.md#gestureevent)) => void | Yes | Callback for successful pan gesture recognition. |

#### \[h2\]onActionUpdate

onActionUpdate(event: (event: GestureEvent) => void)

Registers the callback for pan gesture updates. If **fingerList** contains multiple fingers, this callback updates the location information of only one finger each time.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | (event: [GestureEvent](../../gesture-common-apis/document.md#gestureevent)) => void | Yes | Callback for pan gesture updates. |

#### \[h2\]onActionEnd

onActionEnd(event: (event: GestureEvent) => void)

Registers the callback for pan gesture completion. This callback is triggered when all fingers are lifted after successful pan gesture recognition.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | (event: [GestureEvent](../../gesture-common-apis/document.md#gestureevent)) => void | Yes | Callback for pan gesture completion. |

#### \[h2\]onActionCancel

onActionCancel(event: () => void)

Registers the callback for pan gesture cancellation. This callback is triggered when a touch cancellation event occurs after successful pan gesture recognition. No gesture event information is returned.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | () => void | Yes | Callback for pan gesture cancellation. |

#### \[h2\]onActionCancel18+

onActionCancel(event: Callback<GestureEvent>)

Registers the callback for pan gesture cancellation. This callback is triggered when a touch cancellation event occurs after successful pan gesture recognition. Gesture event information is returned.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | Callback<[GestureEvent](../../gesture-common-apis/document.md#gestureevent)\> | Yes | Callback for pan gesture cancellation. |

#### Example

This example demonstrates the recognition of single-finger and double-finger pan gestures using **PanGesture**.

// xxx.ets
@Entry
@Component
struct PanGestureExample {
  @State offsetX: number = 0;
  @State offsetY: number = 0;
  @State positionX: number = 0;
  @State positionY: number = 0;
  private panOption: PanGestureOptions = new PanGestureOptions({ direction: PanDirection.Left | PanDirection.Right });

  build() {
    Column() {
      Column() {
        Text('PanGesture offset:\\nX: ' + this.offsetX + '\\n' + 'Y: ' + this.offsetY)
      }
      .height(200)
      .width(300)
      .padding(20)
      .border({ width: 3 })
      .margin(50)
      .translate({ x: this.offsetX, y: this.offsetY, z: 0}) // Move the component with its upper left corner as the coordinate origin.
      // Pan left and right to trigger the gesture event
      .gesture(
      PanGesture(this.panOption)
        .onActionStart((event: GestureEvent) => {
          console.info('Pan start');
          console.info(\`Pan start timeStamp is: ${event.timestamp}\`);
        })
        .onActionUpdate((event: GestureEvent) => {
          if (event) {
            this.offsetX = this.positionX + event.offsetX;
            this.offsetY = this.positionY + event.offsetY;
          }
        })
        .onActionEnd((event: GestureEvent) => {
          this.positionX = this.offsetX;
          this.positionY = this.offsetY;
          console.info('Pan end');
          console.info(\`Pan end timeStamp is: ${event.timestamp}\`);
        })
      )

      Button('Set PanGesture Trigger Condition')
        .onClick(() => {
          // Change the trigger condition to double-finger panning in any direction.
          this.panOption.setDirection(PanDirection.All);
          this.panOption.setFingers(2);
        })
    }
  }
}

**Diagrams**

Panning left:

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/SbsHO66sSJWvjv2rNUydYg/en-us_image_0000002537765490.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062237Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E5004E7CBD6B6563EABB45626FE63F3C5ED017C54FEF3E7B1054F5DFB5F88DE0)

Click **Set PanGesture Trigger Condition** to set the pan gesture to be triggered by two fingers moving toward the lower left corner.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2/v3/oHbnXKKUSvK-wFQv2YPQhg/en-us_image_0000002537925430.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062237Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3F7BC7A42AB8C5301F34AAC8BCD6E828BDF46321D712BFBC93D5E0403135C60A)
