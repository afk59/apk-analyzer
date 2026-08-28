# Mouse Event

If a mouse action triggers multiple events, the order of these events is fixed. By default, mouse events bubble.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/4VwqHK-6SomQDf9bNG5CUg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062231Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F81F34A17D687F7712D6C0FE21701E8F94EB178BE2F3AD97EBF221A7C0886827)

-   The initial APIs of this module are supported since API version 8. Newly added APIs will be marked with a superscript to indicate their earliest API version.
    
-   For the time being, a mouse event can be triggered only by an external mouse device.
    

#### onMouse

onMouse(event: (event: MouseEvent) => void): T

Triggered when the component is clicked by a mouse button or the mouse pointer moves on the component.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | (event: [MouseEvent](#mouseevent)) => void | Yes | Timestamp, mouse button, action, coordinates of the clicked point on the entire screen, and coordinates of the clicked point relative to the component when the event is triggered. |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### MouseEvent

Inherits from [BaseEvent](../../../gesture-handling/gesture-control/custom-gesture-judgment/document.md#baseevent8).

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| x | number | No | No | 
X coordinate of the mouse point in the [component coordinate system](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkui-glossary#component-coordinate-system) based on the event-responsive component.

Unit: vp.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| y | number | No | No | 

Y coordinate of the mouse point in the [component coordinate system](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkui-glossary#component-coordinate-system) based on the event-responsive component.

Unit: vp.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| button | [MouseButton](../../../common-definitions/enums/document.md#mousebutton8) | No | No | 

Mouse button.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| action | [MouseAction](../../../common-definitions/enums/document.md#mouseaction8) | No | No | 

Mouse action.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| stopPropagation | () => void | No | No | 

Disables [event bubbling](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-interaction-basic-principles#event-bubbling) propagation.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| windowX10+ | number | No | No | 

X coordinate of the mouse position in the coordinate system of the current application window.

Unit: vp.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| windowY10+ | number | No | No | 

Y coordinate of the mouse position in the coordinate system of the current application window.

Unit: vp.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| displayX10+ | number | No | No | 

X coordinate of the mouse position in the coordinate system of the current screen window.

Unit: vp.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| displayY10+ | number | No | No | 

Y coordinate of the mouse position in the coordinate system of the current screen window.

Unit: vp.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| screenX(deprecated) | number | No | No | 

X coordinate of the mouse position in the coordinate system of the current application window.

Unit: vp.

Note: This API is supported since API version 8 and deprecated since API version 10. You are advised to use **windowX** instead.

 |
| screenY(deprecated) | number | No | No | 

Y coordinate of the mouse position in the coordinate system of the current application window.

Unit: vp.

Note: This API is supported since API version 8 and deprecated since API version 10. You are advised to use **windowY** instead.

 |
| rawDeltaX15+ | number | No | Yes | 

Movement increment of the mouse along the X axis in a two-dimensional plane. The value is the original movement data of the mouse hardware, which is expressed in the unit of the mouse movement distance in the physical world. The reported value is determined by the hardware, not the physical or logical pixels of the screen.

**Atomic service API**: This API can be used in atomic services since API version 15.

 |
| rawDeltaY15+ | number | No | Yes | 

Movement increment of the mouse along the Y axis in a two-dimensional plane. The value is the original movement data of the mouse hardware, which is expressed in the unit of the mouse movement distance in the physical world. The reported value is determined by the hardware, not the physical or logical pixels of the screen.

**Atomic service API**: This API can be used in atomic services since API version 15.

 |
| pressedButtons15+ | MouseButton\[\] | No | Yes | 

Set of buttons being pressed.

**Atomic service API**: This API can be used in atomic services since API version 15.

 |
| globalDisplayX20+ | number | No | Yes | 

X coordinate of the mouse position in the [global coordinate system](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/window-terminology#global-coordinate-system).

Unit: vp.

Value range: \[0, +∞).

**Atomic service API**: This API can be used in atomic services since API version 20.

 |
| globalDisplayY20+ | number | No | Yes | 

Y coordinate of the mouse position in the [global coordinate system](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/window-terminology#global-coordinate-system).

Unit: vp.

Value range: \[0, +∞).

**Atomic service API**: This API can be used in atomic services since API version 20.

 |

#### Example

This example demonstrates how to set a mouse event on a button. When the button is clicked using a mouse device, the [onMouse](#onmouse) event is triggered to obtain relevant mouse event parameters. Starting from API version 15, the [MouseEvent](#mouseevent) object provides access to the **targetDisplayId**, **rawDeltaX**, **rawDeltaY**, and **pressedButtons** parameters.

For mouse wheel event examples, see [Axis Event](../axis-event/document.md#example).

// xxx.ets
@Entry
@Component
struct MouseEventExample {
  @State hoverText: string = 'no hover';
  @State mouseText: string = '';
  @State action: string = '';
  @State mouseBtn: string = '';
  @State color: Color = Color.Blue;

  build() {
    Column({ space: 20 }) {
      Button(this.hoverText)
        .width(180)
        .height(80)
        .backgroundColor(this.color)
        .fontSize(24)
        .onHover((isHover: boolean, event: HoverEvent) => {
          // Use the onHover event to dynamically change the text content and background color of a button when the mouse pointer is hovered on it.
          if (isHover) {
            this.hoverText = 'hover';
            this.color = Color.Pink;
          } else {
            this.hoverText = 'no hover';
            this.color = Color.Blue;
          }
        })
      Button('onMouse')
        .width(180).height(80)
        .fontSize(24)
        // Use onMouse to listen for mouse events, parse the buttons, actions, coordinates, and other information, and combines the information.
        .onMouse((event: MouseEvent): void => {
          if (event) {
            // Determine the type of the pressed mouse button.
            switch (event.button) {
              case MouseButton.None:
                this.mouseBtn = 'None';
                break;
              case MouseButton.Left:
                this.mouseBtn = 'Left';
                break;
              case MouseButton.Right:
                this.mouseBtn = 'Right';
                break;
              case MouseButton.Back:
                this.mouseBtn = 'Back';
                break;
              case MouseButton.Forward:
                this.mouseBtn = 'Forward';
                break;
              case MouseButton.Middle:
                this.mouseBtn = 'Middle';
                break;
            }
            // Determine the type of the triggered mouse action.
            switch (event.action) {
              case MouseAction.Hover:
                this.action = 'Hover';
                break;
              case MouseAction.Press:
                this.action = 'Press';
                break;
              case MouseAction.Move:
                this.action = 'Move';
                break;
              case MouseAction.Release:
                this.action = 'Release';
                break;
            }
            // Combine and display all information about the mouse event.
            this.mouseText = 'onMouse:\\nButton = ' + this.mouseBtn +
              '\\nAction = ' + this.action + '\\nXY=(' + event.x + ',' + event.y + ')' +
              '\\nwindowXY=(' + event.windowX + ',' + event.windowY + ')' +
              '\\ntargetDisplayId = ' + event.targetDisplayId +
              '\\nrawDeltaX = ' + event.rawDeltaX +
              '\\nrawDeltaY = ' + event.rawDeltaY +
              '\\nlength = ' + event.pressedButtons?.length;
          }
        })
      Text(this.mouseText)
    }.padding({ top: 30 }).width('100%')
  }
}

The figure below shows how the button looks when clicked.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/ZvpelZEZRnqFqn9fOLf19g/en-us_image_0000002568685091.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062231Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C56232743B8F8AADDE7035CCFC232FCA83AB47650A2BAC2D6EC00D827861FFB8)
