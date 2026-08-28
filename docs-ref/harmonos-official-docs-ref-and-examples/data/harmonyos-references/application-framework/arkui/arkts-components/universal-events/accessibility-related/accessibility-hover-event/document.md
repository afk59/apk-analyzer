# Accessibility Hover Event

In accessibility mode, touch events are converted to accessibility hover events.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/N3dphQvZRZqn0J-xmbXXGQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062232Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=16292793358000D4250238A415A205853BE465E40B0E301124C09559760829E5)

-   This event is supported since API version 12. Updates will be marked with a superscript to indicate their earliest API version.
-   Currently, accessibility hover events are only triggered when accessibility mode is enabled.

#### onAccessibilityHover

onAccessibilityHover(callback: AccessibilityCallback): T

Triggered in accessibility mode when a single finger touches the bound component.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/qGvKUjYWTy-ygtdLaWU-Dw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062232Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6E1EAA75E0A0A44BBE11A419B7092C96D36A865B007DEF400647148D6116CC20)

This API cannot be called within [attributeModifier](../../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | [AccessibilityCallback](#accessibilitycallback) | Yes | Callback invoked in accessibility mode when a single finger touches the bound component. |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### AccessibilityCallback

type AccessibilityCallback = (isHover: boolean, event: AccessibilityHoverEvent) => void

Defines the callback type for accessibility hover events, active in accessibility mode.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| isHover | boolean | Yes | Hover state. **true**: The finger enters the component. **false**: The finger exits the component. |
| event | [AccessibilityHoverEvent](#accessibilityhoverevent) | Yes | **AccessibilityHoverEvent** object. |

#### AccessibilityHoverEvent

Inherits from [BaseEvent](../../../gesture-handling/gesture-control/custom-gesture-judgment/document.md#baseevent8).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| type | [AccessibilityHoverType](../../../common-definitions/enums/document.md#accessibilityhovertype12) | No | No | Accessibility hover type. |
| x | number | No | No | 
X-coordinate of the finger's position relative to the upper left corner of the component.

Unit: vp

 |
| y | number | No | No | 

Y-coordinate of the finger's position relative to the upper left corner of the component.

Unit: vp

 |
| windowX | number | No | No | 

X-coordinate of the finger's position relative to the upper left corner of the application window.

Unit: vp

 |
| windowY | number | No | No | 

Y-coordinate of the finger's position relative to the upper left corner of the application window.

Unit: vp

 |
| displayX | number | No | No | 

X-coordinate of the finger's position relative to the upper left corner of the application screen.

Unit: vp

 |
| displayY | number | No | No | 

Y-coordinate of the finger's position relative to the upper left corner of the application screen.

Unit: vp

 |
| globalDisplayX20+ | number | No | Yes | 

X-coordinate of the finger position relative to the upper left corner of the global display.

Unit: vp

Value range: \[0, +∞).

**Atomic service API**: This API can be used in atomic services since API version 20.

 |
| globalDisplayY20+ | number | No | Yes | 

Y-coordinate of the finger position relative to the upper left corner of the global display.

Unit: vp

Value range: \[0, +∞).

**Atomic service API**: This API can be used in atomic services since API version 20.

 |

#### onAccessibilityHoverTransparent20+

onAccessibilityHoverTransparent(callback: AccessibilityTransparentCallback): T

This callback is triggered if a finger touch occurs within the component area while an accessibility service is running, but the accessibility system finds no focusable elements within the component hierarchy. It then returns an accessibility hover event. This callback only supports finger touches. It has no effect in the following scenarios: [UIExtension](../../../../arkts-api/ui/ohos-arkui-uiextension-uiextension/document.md), [Web](../../../../../arkweb/arkts-components/web/components/document.md), and [XComponent](../../../rendering-drawing/xcomponent/document.md) integrated with a third-party UI framework.

The main reasons why a component cannot be identified as focusable by the accessibility hover event are as follows: The [accessibilityLevel](../../../universal-attributes/accessibility/document.md#accessibilitylevel) attribute of the component is set to **no** or **no-hide-descendants**; the component has no text and no [accessibilityText](../../../universal-attributes/accessibility/document.md#accessibilitytext) configured, and does not support the tap or long press operation.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | [AccessibilityTransparentCallback](#accessibilitytransparentcallback20) | Yes | Callback invoked when a touch interaction occurs within the area of the component that does not respond to the accessibility hover event. |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### AccessibilityTransparentCallback20+

type AccessibilityTransparentCallback = (event: TouchEvent) => void

Defines the callback type for touch events that do not trigger accessibility responses in accessibility mode.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | [TouchEvent](../../basic-input-events/touch-event/document.md#touchevent) | Yes | 
Original touch event.

Note: The **TouchEvent** object's [TouchType](../../../common-definitions/enums/document.md#touchtype) corresponds to four accessibility hover event types: **HOVER\_ENTER**, **HOVER\_MOVE**, **HOVER\_EXIT**, and HOVER\_CANCEL.

 |

#### Example

## Example 1: Using the onAccessibilityHover Event

This example demonstrates how to use the **onAccessibilityHover** event to customize a button in accessibility mode.

// xxx.ets
@Entry
@Component
struct OnAccessibilityHoverEventExample {
  @State hoverText: string = 'no hover';
  @State color: Color = Color.Blue;

  build() {
    Column({ space: 20 }) {
      Button(this.hoverText)
        .width(180).height(80)
        .backgroundColor(this.color)
        .onAccessibilityHover((isHover: boolean, event: AccessibilityHoverEvent) => {
          // Use the onAccessibilityHover event to dynamically change the text content and background color of a button when the finger is hovered on it.
          if (isHover) {
            this.hoverText = 'hover';
            this.color = Color.Pink;
          } else {
            this.hoverText = 'no hover';
            this.color = Color.Blue;
          }
        })
    }.padding({ top: 30 }).width('100%')
  }
}

## Example 2: Capturing a Touch Event on a Non-Focusable Component

This example shows how to capture touch events from a component that cannot receive focus in accessibility mode using the **onAccessibilityHoverTransparent** API and display event details in the text area below.

Starting from API version 20, the [onAccessibilityHoverTransparent](#onaccessibilityhovertransparent20) API with the input parameter **AccessibilityTransparentCallback** has been added.

@Entry
@Component
struct TestExample {
  @State text: string = '';
  @State eventType: string = '';

  build() {
    Column({ space: 50 }) {
      Column() {
        Button("Test Button")
          .accessibilityLevel("no")
      }.margin({ top: 20 })

      Text(this.text)
    }
    .width('100%')
    .height('100%')
    .onAccessibilityHoverTransparent((event?: TouchEvent) => {
      if (event) {
        // Triggered on finger press.
        if (event.type === TouchType.HOVER\_ENTER) {
          this.eventType = 'HOVER\_ENTER';
        }
        // Triggered on touch move.
        if (event.type === TouchType.HOVER\_MOVE) {
          this.eventType = 'HOVER\_MOVE';
        }
        // Triggered on hand raise.
        if (event.type === TouchType.HOVER\_EXIT) {
          this.eventType = 'HOVER\_EXIT';
        }
        // Cancel the current event.
        if (event.type === TouchType.HOVER\_CANCEL) {
          this.eventType = 'HOVER\_CANCEL';
        }
        this.text = 'TouchType:' + this.eventType + '\\nDistance between touch point and touch element:\\nx: '
          + event.touches\[0\].x + '\\n' + 'y: ' + event.touches\[0\].y + '\\nComponent globalPos:('
          + event.target.area.globalPosition.x + ',' + event.target.area.globalPosition.y + ')\\nwidth:'
          + event.target.area.width + '\\nheight:' + event.target.area.height;
      }
    })
  }
}
