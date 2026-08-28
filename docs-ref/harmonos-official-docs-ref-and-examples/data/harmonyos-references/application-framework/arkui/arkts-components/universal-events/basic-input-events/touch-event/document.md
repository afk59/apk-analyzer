# Touch Event

A touch event is triggered when a finger, stylus, or left mouse button is pressed against, swipes on, or is lifted from a component.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/9mYNfLiuRs20BJVnqlmNOA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062231Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D3C40EA4070334FAF2ECB6687478423397692477CB48CEA6BAB768399CB56075)

-   The initial APIs of this module are supported since API version 7. Newly added APIs will be marked with a superscript to indicate their earliest API version.
    
-   For details about event dispatch, see [Event Interaction Pipeline](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-interaction-basic-principles#event-interaction-pipeline). For details about gesture event handling, see [Multi-level Gesture Events](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-gesture-events-multi-level-gesture).
    
-   For details about how to bind gesture events, see [Gesture Binding](../../../gesture-handling/gesture-binding/gesture-binding/document.md).
    

#### onTouch

onTouch(event: (event: TouchEvent) => void): T

Invoked when a touch event is triggered. Touch events [bubble](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-interaction-basic-principles#event-bubbling) by default and can be consumed by multiple components. To prevent event bubbling, use the **stopPropagation** API of [TouchEvent](#touchevent). Mouse left-click events are converted to touch events and will also trigger this callback.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | (event: [TouchEvent](#touchevent)) => void | Yes | **TouchEvent** object. |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### TouchEvent

Inherits from [BaseEvent](../../../gesture-handling/gesture-control/custom-gesture-judgment/document.md#baseevent8). In non-event injection scenarios, **changedTouches** contains points resampled at the screen refresh rate, while **touches** contains points reported at the device's refresh rate. As such, **changedTouches** data may differ from **touches**.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| type | [TouchType](../../../common-definitions/enums/document.md#touchtype) | No | No | 
Type of the touch event.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| touches | [TouchObject](#touchobject)\[\] | No | No | 

Information about all touch points (for multi-touch). Each element represents one touch point. When using this property, you need to check whether it is empty.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| changedTouches | [TouchObject](#touchobject)\[\] | No | No | 

Information about touch points that changed and triggered the event. When using this property, you need to check whether it is empty.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| stopPropagation | () => void | No | No | 

Disables [event bubbling](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-interaction-basic-principles#event-bubbling) propagation.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| preventDefault12+ | () => void | No | No | 

Blocks the default event.

Note: This API is only supported by the [Hyperlink](../../../text-and-input/hyperlink/document.md) component. Using it with unsupported components throws an exception. Asynchronous calls and **Modifier** API integration are not yet supported.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |

**Error codes**

For details about the error codes, see [Interaction Event Error Codes](../../../../error-codes/ui/interaction-event-error-codes/document.md).

| Error Code | Error Message |
| :-- | :-- |
| 100017 | Component does not support prevent function. |

#### \[h2\]getHistoricalPoints10+

getHistoricalPoints(): Array<HistoricalPoint>

Obtains all historical touch points for the current frame. The touch event frequency per frame varies by device. This API can be called only in [TouchEvent](#touchevent). This API is only available within [TouchEvent](#touchevent) during [onTouch](#ontouch) invocations. Typically, [onTouch](#ontouch) is invoked once per frame. If multiple [TouchEvent](#touchevent) instances are received in a single frame, the last point is returned through **onTouch**, and the remaining points are stored as historical points. For multi-touch events within the same frame, multiple\*\* onTouch\*\* calls may occur.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| Array<[HistoricalPoint](#historicalpoint10)\> | Array of historical points. |

#### TouchObject

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| type | [TouchType](../../../common-definitions/enums/document.md#touchtype) | No | No | 
Type of the touch event.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| id | number | No | No | 

Unique identifier of a finger.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| x | number | No | No | 

X coordinate of the touch point in the [component coordinate system](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkui-glossary#component-coordinate-system) based on the event-responsive component.

Unit: vp.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| y | number | No | No | 

Y coordinate of the touch point in the [component coordinate system](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkui-glossary#component-coordinate-system) based on the event-responsive component.

Unit: vp.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| windowX10+ | number | No | No | 

X coordinate of the touch point in the coordinate system of the current application window.

Unit: vp.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| windowY10+ | number | No | No | 

Y coordinate of the touch point in the coordinate system of the current application window.

Unit: vp.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| displayX10+ | number | No | No | 

X coordinate of the touch point in the coordinate system of the current application screen.

Unit: vp.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| displayY10+ | number | No | No | 

Y coordinate of the touch point in the coordinate system of the current application screen.

Unit: vp.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| screenX(deprecated) | number | No | No | 

X coordinate of the touch point in the coordinate system of the current application window.

Unit: vp.

Note: This API is supported since API version 7 and deprecated since API version 10. You are advised to use **windowX** instead.

 |
| screenY(deprecated) | number | No | No | 

Y coordinate of the touch point in the coordinate system of the current application window.

Unit: vp.

Note: This API is supported since API version 7 and deprecated since API version 10. You are advised to use **windowY** instead.

 |
| pressedTime15+ | number | No | Yes | 

Time when the finger is pressed.

Unit: ns

**Atomic service API**: This API can be used in atomic services since API version 15.

 |
| pressure15+ | number | No | Yes | 

Pressure value of finger contact.

Value range: \[0, 65535), where higher values indicate stronger pressure.

**Atomic service API**: This API can be used in atomic services since API version 15.

 |
| width15+ | number | No | Yes | 

Width of the finger contact area.

Unit: vp.

**Atomic service API**: This API can be used in atomic services since API version 15.

 |
| height15+ | number | No | Yes | 

Height of the finger contact area.

Unit: vp.

**Atomic service API**: This API can be used in atomic services since API version 15.

 |
| hand15+ | [InteractionHand](../../../common-definitions/enums/document.md#interactionhand15) | No | Yes | 

Whether the event was triggered by a left-hand or right-hand tap.

**Atomic service API**: This API can be used in atomic services since API version 15.

 |
| globalDisplayX20+ | number | No | Yes | 

X coordinate of the touch point in the [global coordinate system](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/window-terminology#global-coordinate-system).

Unit: vp.

Value range: \[0, +∞).

**Atomic service API**: This API can be used in atomic services since API version 20.

 |
| globalDisplayY20+ | number | No | Yes | 

Y coordinate of the touch point in the [global coordinate system](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/window-terminology#global-coordinate-system).

Unit: vp.

Value range: \[0, +∞).

**Atomic service API**: This API can be used in atomic services since API version 20.

 |

#### HistoricalPoint10+

Provides historical touch point information.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| touchObject | [TouchObject](#touchobject) | No | No | Basic touch event information for the historical point. |
| size | number | No | No | 
Size of the contact area size between the finger and screen in the touch event corresponding to the historical point.

Default value: **0**

 |
| force | number | No | No | 

Touch pressure value of the historical point.

Default value: **0**

Value range: \[0, 65535), where higher values indicate stronger pressure.

 |
| timestamp | number | No | No | 

Timestamp of the touch event corresponding to the historical point, representing the time interval from system boot when the event is triggered.

Unit: ns

 |

#### Example

This example shows how to configure a touch event for a button. When the button is touched, it obtains relevant parameters of the event.

// xxx.ets
@Entry
@Component
struct TouchExample {
  @State text: string = '';
  @State eventType: string = '';

  build() {
    Column() {
      Button('Touch').height(40).width(100)
        .onTouch((event?: TouchEvent) => {
          if (event && event.sourceTool === SourceTool.Finger) {
            if (event.type === TouchType.Down) {
              this.eventType = 'Down';
            }
            if (event.type === TouchType.Up) {
              this.eventType = 'Up';
            }
            if (event.type === TouchType.Move) {
              this.eventType = 'Move';
            }
            // 1. The cancel event is triggered when the user touches the home button to return to the home screen while keeping a finger on the screen.
            // 2. On a foldable phone, the cancel event is triggered when the user folds the phone to switch to the external screen while keeping a finger on the screen.
            if (event.type === TouchType.Cancel) {
              this.eventType = 'Cancel';
            }
            if (event.touches) {
              this.text = 'TouchType:' + this.eventType
                + '\\nDistance between touch point and touch element:'
                + '\\n  x: ' + event.touches\[0\].x + '\\n  y: ' + event.touches\[0\].y
                + '\\n  width: ' + event.touches\[0\].width + '\\n  height: ' + event.touches\[0\].height
                + '\\n  pressedTime: ' + event.touches\[0\].pressedTime
                + '\\n  pressure: ' + event.touches\[0\].pressure
                + '\\nComponent globalPos:'
                + '\\n  x: ' + event.target.area.globalPosition.x + '\\n  y: ' + event.target.area.globalPosition.y
                + '\\n  width: ' + event.target.area.width + '\\n  height: ' + event.target.area.height
                + '\\ntargetDisplayId: ' + event.targetDisplayId;
            }
          }
        })
      Button('Touch').height(50).width(200).margin(20)
        .onTouch((event?: TouchEvent) => {
          if (event) {
            if (event.type === TouchType.Down) {
              this.eventType = 'Down';
            }
            if (event.type === TouchType.Up) {
              this.eventType = 'Up';
            }
            if (event.type === TouchType.Move) {
              this.eventType = 'Move';
            }
            // 1. The cancel event is triggered when the user touches the home button to return to the home screen while keeping a finger on the screen.
            // 2. On a foldable phone, the cancel event is triggered when the user folds the phone to switch to the external screen while keeping a finger on the screen.
            if (event.type === TouchType.Cancel) {
              this.eventType = 'Cancel';
            }
            if (event.touches) {
              this.text = 'TouchType:' + this.eventType
                + '\\nDistance between touch point and touch element:'
                + '\\n  x: ' + event.touches\[0\].x + '\\n  y: ' + event.touches\[0\].y
                + '\\n  width: ' + event.touches\[0\].width + '\\n  height: ' + event.touches\[0\].height
                + '\\n  pressedTime: ' + event.touches\[0\].pressedTime
                + '\\n  pressure: ' + event.touches\[0\].pressure
                + '\\nComponent globalPos:'
                + '\\n  x: ' + event.target.area.globalPosition.x + '\\n  y: ' + event.target.area.globalPosition.y
                + '\\n  width: ' + event.target.area.width + '\\n  height: ' + event.target.area.height
                + '\\ntargetDisplayId: ' + event.targetDisplayId;
            }
          }
        })
      Text(this.text)
    }.width('100%').padding(30)
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/jJ3RcjUNSKK8ihleGqmj0g/en-us_image_0000002537925314.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062231Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6BEE62AA8C4319DF0B95646A896657B5786A8DEA046DB866664091CEF0858F69)
