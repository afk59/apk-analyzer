# Click Event

A click event is triggered when a component is clicked.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/8WCq4JVQSouzyOD5vhPDZw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062232Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4110070DF994D62D334745249CB6D1882BF9216546B1A133F60A52D5D336DC00)

-   The event is supported since API version 7. Updates will be marked with a superscript to indicate their earliest API version.
    
-   Click events follow the [touch event](../../basic-input-events/touch-event/document.md) dispatch mechanism, supporting custom behaviors like event blocking and bubbling.
    
-   For details about event dispatch, see [Event Interaction Pipeline](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-interaction-basic-principles#event-interaction-pipeline). For details about gesture event handling, see [Multi-level Gesture Events](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-gesture-events-multi-level-gesture).
    
-   When triggered via keyboard or gamepad, click events skip the [onGestureJudgeBegin](../../../gesture-handling/gesture-control/custom-gesture-judgment/document.md#ongesturejudgebegin), [onGestureRecognizerJudgeBegin](../../../gesture-handling/gesture-control/gesture-blocking-enhancement/document.md#ongesturerecognizerjudgebegin), and [willClick](../../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-uiobserver/document.md#onwillclick12) callbacks.
    

#### onClick12+

onClick(event: Callback<ClickEvent>, distanceThreshold: number): T

Called when a click event occurs.

When triggered by keyboard or gamepad input, the event's [SourceTool](../../../gesture-handling/gesture-binding/gesture-binding/document.md#sourcetool9) is **Unknown**, and [SourceType](../../../gesture-handling/gesture-binding/gesture-binding/document.md#sourcetype8) is **KEY** or **JOYSTICK**.

Compared with the original **onClick** API, this API has the **distanceThreshold** parameter that specifies the finger movement threshold for click events. If the finger's movement exceeds the set threshold, the gesture recognition will fail. The click gesture recognition will fail if finger movement exceeds this threshold.

For scenarios where there is no restriction on the finger movement distance during a click, the original API is preferred. To limit finger movement range during a click, use this new API.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/07/v3/Xrxd_0i6SGmE0wbuqsXhFQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062232Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=14B3AE906FEF3BFCC2B6E7A73A09D5614256A40941819EE87255B656A5EB576E)

-   Since API version 12, the following constraints apply when this API is used in service widgets:
    
    1.  Click events will not be triggered if the finger is pressed for more than 800 ms.
    2.  Click events will not be triggered if the finger moves more than 20 px after pressing down.
-   This API cannot be called within [attributeModifier](../../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier).
    

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | Callback<[ClickEvent](#clickevent)\> | Yes | Callback for the click event. |
| distanceThreshold | number | Yes | 
Finger movement threshold for click events. If the value specified is less than or equal to 0, it will be converted to the default value.

Default value: 2^31-1

Unit: vp

**NOTE**

If the finger movement exceeds the preset movement threshold, the gesture recognition fails. If the default threshold is used during initialization and the finger moves beyond the component's touch target, the gesture recognition fails.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/3Pbo9FhfR-mgxw24ouqiZA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062232Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=199ACEEFACAB0ACD94D63E0EF4B90DEDECEADD908B901B659CA08CA4C162AC37)

If finger movement during a swipe exceeds the threshold but remains within the touch target boundaries upon release, the click event is still triggered.

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### onClick

onClick(event: (event: ClickEvent) => void): T

Called when a click event occurs.

When triggered by keyboard or gamepad input, the event's **SourceTool** is **Unknown**, and [SourceType](../../../gesture-handling/gesture-binding/gesture-binding/document.md#sourcetype8) is **KEY** or **JOYSTICK**.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/ltyxtB6yQoG8pwByjUQhdA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062232Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0234F774D3BC3A29664D8A539AA04C7E495395AB83A0796ACF88495C78F9F4E9)

Since API version 9, the following constraints apply when this API is used in service widgets:

1.  Click events will not be triggered if the finger is pressed for more than 800 ms.
2.  Click events will not be triggered if the finger moves more than 20 px after pressing down.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | (event: [ClickEvent](#clickevent)) => void | Yes | Callback for the click event. |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### ClickEvent

Inherits from [BaseEvent](../../../gesture-handling/gesture-control/custom-gesture-judgment/document.md#baseevent8).

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| x | number | No | No | 
X coordinate of the click position in the [component coordinate system](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkui-glossary#component-coordinate-system) based on the clicked element. After [distanceThreshold](#onclick12) is set for **onClick**, the click position is the lift-off point. If the event is triggered by a keyboard or gamepad device, the click position is the center of the clicked element.

Unit: vp

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| y | number | No | No | 

Y coordinate of the click position in the [component coordinate system](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkui-glossary#component-coordinate-system) based on the clicked element. After distanceThreshold is set for **onClick**, the click position is the lift-off point. If the event is triggered by a keyboard or gamepad device, the click position is the center of the clicked element.

Unit: vp

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| windowX10+ | number | No | No | 

X coordinate of the click position in the coordinate system of the current application window. After distanceThreshold is set for **onClick**, the click position is the lift-off point.

Unit: vp

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| windowY10+ | number | No | No | 

Y coordinate of the click position in the coordinate system of the current application window. After distanceThreshold is set for **onClick**, the click position is the lift-off point.

Unit: vp

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| displayX10+ | number | No | No | 

X coordinate of the click position in the coordinate system of the current application screen.

Unit: vp

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| displayY10+ | number | No | No | 

Y coordinate of the click position in the coordinate system of the current application screen.

Unit: vp

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| screenX(deprecated) | number | No | No | 

X coordinate of the click position in the coordinate system of the current application window.

Unit: vp

Note: This API is supported since API version 7 and deprecated since API version 10. You are advised to use **windowX** instead.

 |
| screenY(deprecated) | number | No | No | 

Y coordinate of the click position in the coordinate system of the current application window.

Unit: vp

Note: This API is supported since API version 7 and deprecated since API version 10. You are advised to use **windowY** instead.

 |
| preventDefault12+ | () => void | No | No | 

Blocks the default event.

Note: This API is only supported by the following components: **RichEditor** and **Hyperlink**. An exception is thrown when this API is used with unsupported components. Currently, asynchronous calls and Modifier APIs are not supported.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| hand15+ | [InteractionHand](../../../common-definitions/enums/document.md#interactionhand15) | No | Yes | 

Whether the event is triggered by a left-hand or right-hand tap.

**Atomic service API**: This API can be used in atomic services since API version 15.

 |
| globalDisplayX20+ | number | No | Yes | 

X coordinate of the click position in the [global coordinate system](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/window-terminology#global-coordinate-system).

Unit: vp

Value range: \[0, +∞).

**Atomic service API**: This API can be used in atomic services since API version 20.

 |
| globalDisplayY20+ | number | No | Yes | 

Y coordinate of the click position in the [global coordinate system](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/window-terminology#global-coordinate-system).

Unit: vp

Value range: \[0, +∞).

**Atomic service API**: This API can be used in atomic services since API version 20.

 |

**Error codes**

For details about the error codes, see [Interaction Event Error Codes](../../../../error-codes/ui/interaction-event-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 100017 | Component does not support prevent function. |

#### EventTarget8+

Defines the type of the **target** parameter in [BaseEvent](../../../gesture-handling/gesture-control/custom-gesture-judgment/document.md#baseevent8).

Represents the display area of the element object that triggers the event.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| area | [Area](../../../common-definitions/basic-types/document.md#area8) | No | No | 
Area information of the target element.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| id15+ | string | No | Yes | 

Custom node [ID](../../../universal-attributes/basic-attributes/component-id/document.md#id). Default value: **undefined**.

**Widget capability**: This API can be used in ArkTS widgets since API version 15.

**Atomic service API**: This API can be used in atomic services since API version 15.

 |

#### Example

This example configures a click event for a button. When the button is clicked, it obtains relevant parameters of the click event.

// xxx.ets
@Entry
@Component
struct ClickExample {
  @State text: string = '';

  build() {
    Column() {
      Row({ space: 20 }) {
        Button('Click1').width(100).height(40).id('click1')
          .onClick((event?: ClickEvent) => {
            if (event) {
              this.text =
                \`Click Point:\\n  windowX:${event.windowX}\\n  windowY:${event.windowY}\\n  x:${event.x}\\n  y:${event.y}\\n target:\\n  component globalPos:(${event.target.area.globalPosition.x},${event.target.area.globalPosition.y})\\n  width:${event.target.area.width}\\n  height:${event.target.area.height}\\n  id:${event.target.id}\\ntargetDisplayId:${event.targetDisplayId}\\ntimestamp${event.timestamp}\`
            }
          }, 20)
        Button('Click2').width(200).height(50).id('click2')
          .onClick((event?: ClickEvent) => {
            if (event) {
              this.text =
                \`Click Point:\\n  windowX:${event.windowX}\\n  windowY:${event.windowY}\\n  x:${event.x}\\n  y:${event.y}\\n target:\\n  component globalPos:(${event.target.area.globalPosition.x},${event.target.area.globalPosition.y})\\n  width:${event.target.area.width}\\n  height:${event.target.area.height}\\n  id:${event.target.id}\\ntargetDisplayId:${event.targetDisplayId}\\ntimestamp${event.timestamp}\`
            }
          }, 20)
      }.margin(20)

      Text(this.text).margin(15)
    }.width('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/GCLRunMPTXahQr4BbgaaGQ/en-us_image_0000002537765378.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062232Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5B4BAC4681EF2AD75DC1DBD6FEBE30287C4637155C4967FA7B8C329BB5BB41F5)
