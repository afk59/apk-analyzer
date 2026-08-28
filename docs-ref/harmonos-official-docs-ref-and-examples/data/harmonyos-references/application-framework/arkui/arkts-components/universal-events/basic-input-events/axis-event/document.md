# Axis Event

An axis event is triggered when the pointer from a device like a mouse or touchpad is within a component's area, and an action such as scrolling the wheel or sliding two fingers along a specific direction (axis) on the touchpad is performed. "Axis" refers to a direction in a two-dimensional coordinate system, categorized into horizontal (x-axis) and vertical (y-axis) directions.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/7BPkAdy7QCKVxmC-dM4pWg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062232Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=90DBFC36FF52F22C7DF1A0F1E75574C2D6F6DFA0A7493D9FA7B22CC2FEC2375F)

The initial APIs of this module are supported since API version 17. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### onAxisEvent

onAxisEvent(event: Callback<AxisEvent>): T

Triggered by mouse wheel scrolling, a two-finger sliding gesture, or a pinch gesture on the touchpad.

**Atomic service API**: This API can be used in atomic services since API version 17.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | Callback<[AxisEvent](#axisevent)\> | Yes | [AxisEvent](#axisevent) object. |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### AxisEvent

Describes the axis event object. Inherits from [BaseEvent](../../../gesture-handling/gesture-control/custom-gesture-judgment/document.md#baseevent8).

**Atomic service API**: This API can be used in atomic services since API version 17.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### \[h2\]Properties

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| action | [AxisAction](../../../common-definitions/enums/document.md#axisaction17) | No | No | 
Action type of the axis event.

**Atomic service API**: This API can be used in atomic services since API version 17.

 |
| x | number | No | No | 

X coordinate of the cursor in the [component coordinate system](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkui-glossary#component-coordinate-system) based on the clicked element.

Unit: vp

**Atomic service API**: This API can be used in atomic services since API version 17.

 |
| y | number | No | No | 

Y coordinate of the cursor in the [component coordinate system](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkui-glossary#component-coordinate-system) based on the clicked element.

Unit: vp

**Atomic service API**: This API can be used in atomic services since API version 17.

 |
| windowX | number | No | No | 

X coordinate of the cursor in the coordinate system of the current application window.

Unit: vp

**Atomic service API**: This API can be used in atomic services since API version 17.

 |
| windowY | number | No | No | 

Y coordinate of the cursor in the coordinate system of the current application window.

Unit: vp

**Atomic service API**: This API can be used in atomic services since API version 17.

 |
| displayX | number | No | No | 

X coordinate of the cursor in the coordinate system of the current application screen.

Unit: vp

**Atomic service API**: This API can be used in atomic services since API version 17.

 |
| displayY | number | No | No | 

Y coordinate of the cursor in the coordinate system of the current application screen.

Unit: vp

**Atomic service API**: This API can be used in atomic services since API version 17.

 |
| scrollStep | number | No | Yes | 

Scroll step length for the mouse wheel.

Note: Only the mouse wheel is supported. The value ranges from 0 to 65535.

**Atomic service API**: This API can be used in atomic services since API version 17.

 |
| propagation | Callback<void> | No | No | 

Enables [event bubbling](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-interaction-basic-principles#event-bubbling) propagation.

**Atomic service API**: This API can be used in atomic services since API version 17.

 |
| globalDisplayX20+ | number | No | Yes | 

X coordinate of the cursor in the [global coordinate system](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/window-terminology#global-coordinate-system).

Unit: vp

Value range: \[0, +∞).

**Atomic service API**: This API can be used in atomic services since API version 20.

 |
| globalDisplayY20+ | number | No | Yes | 

Y coordinate of the cursor in the [global coordinate system](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/window-terminology#global-coordinate-system).

Unit: vp

Value range: \[0, +∞).

**Atomic service API**: This API can be used in atomic services since API version 20.

 |

#### \[h2\]getHorizontalAxisValue

getHorizontalAxisValue(): number

Obtains the horizontal axis value of this axis event.

**Atomic service API**: This API can be used in atomic services since API version 17.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| number | 
Horizontal axis value.

Unit: vp

 |

#### \[h2\]getVerticalAxisValue

getVerticalAxisValue(): number

Obtains the vertical axis value of this axis event.

**Atomic service API**: This API can be used in atomic services since API version 17.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| number | 
Vertical axis value.

Unit: vp

 |

#### \[h2\]getPinchAxisScaleValue21+

getPinchAxisScaleValue(): number

Obtains the two-finger pinch zoom ratio from the axis event.

**Atomic service API**: This API can be used in atomic services since API version 21.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| number | 
Two-finger pinch zoom ratio.

Note: This ratio is calculated as the current distance between two fingers during a touchpad pinch event divided by the initial distance when the fingers first made contact.

Default value: **0**.

Value range: \[0, +∞).

 |

#### \[h2\]hasAxis22+

hasAxis(axisType: AxisType): boolean

Checks whether this axis event contains the specified axis type.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| axisType | [AxisType](../../../common-definitions/enums/document.md#axistype22) | Yes | Axis type to check for. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | 
Whether the axis event contains the specified axis type.

**true** if the axis event contains the specified axis type; **false** otherwise.

 |

#### Example

This example shows how to set up an axis event on a button. When the user scrolls the mouse wheel over the button, the event parameters are captured and displayed. Starting from API version 21, this example uses [axisPinch](../../../gesture-handling/gesture-control/custom-gesture-judgment/document.md#properties) and [getPinchAxisScaleValue](#getpinchaxisscalevalue21) to obtain the two-finger pinch scale ratio. Starting from API version 22, this example uses [hasAxis](#hasaxis22) to determine whether the axis event contains the specified axis type.

// xxx.ets
@Entry
@Component
struct AxisEventExample {
  @State text: string = ''

  build() {
    Column() {
      Row({ space: 20 }) {
        Button('AxisEvent').width(100).height(40)
          .onAxisEvent((event?: AxisEvent) => {
            if (event) {
              this.text =
                'AxisEvent:' + '\\n  action:' + event.action + '\\n  displayX:' + event.displayX + '\\n  displayY:' +
                event.displayY + '\\n  windowX:' + event.windowX + '\\n  windowY:' + event.windowY + '\\n  x:' + event.x +
                  '\\n  y:' + event.y + '\\n VerticalAxisValue:' + event.getVerticalAxisValue() +
                  '\\n HorizontalAxisValue:' + event.getHorizontalAxisValue() + '\\n axisPinch:' + event.axisPinch +
                  '\\n PinchAxisScaleValue:' + event.getPinchAxisScaleValue() +
                  '\\n HasAxis:' + event.hasAxis(AxisType.VERTICAL\_AXIS);
            }
          })
      }.margin(20)

      Text(this.text).margin(15)
    }.width('100%')
  }
}

The figure below shows the event parameters captured when the user scrolls the mouse wheel.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/xTAqyUH6ThSyLWZbhZZZ7g/en-us_image_0000002568765101.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062232Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=ACDBF37394DDE03D4E94E6928C1F7322141D329772D64F26D9BD87C184AF11F6)
