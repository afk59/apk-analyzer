# Hover Event

A hover event is triggered when the cursor slides over a component or when a stylus hovers and moves over the screen.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/39oe9kGNRjWt5b1p6ZcopA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062232Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=44C094B6A827B4E53D3FC370AD166C73ACEA49770B59166C6191E728597E4B5B)

-   The initial APIs of this module are supported since API version 8. Updates will be marked with a superscript to indicate their earliest API version.
-   Currently, only an external mouse device, stylus, or touchpad can be used to trigger a hover event.

#### onHover

onHover(event: (isHover: boolean, event: HoverEvent) => void): T

Triggered when the mouse pointer or stylus enters or leaves the component.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | (isHover: boolean, event: [HoverEvent](#hoverevent10)) => void | Yes | 
Callback for mouse or stylus hover status.

**event**: event bubbling control and coordinates of the hover position; available since API version 11.

**isHover**: whether the mouse pointer or stylus is hovering over the component. **true**: The mouse pointer or stylus has entered the component. **false**: The mouse pointer or stylus has left the component.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### onHoverMove15+

onHoverMove(event: Callback<HoverEvent>): T

Triggered when a stylus hovers over the component.

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | Callback<[HoverEvent](#hoverevent10)\> | Yes | Callback that controls event bubbling blocking and obtains the stylus hover position coordinates. |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### HoverEvent10+

Inherits from [BaseEvent](../../../gesture-handling/gesture-control/custom-gesture-judgment/document.md#baseevent8).

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| x15+ | number | No | Yes | 
X coordinate of the cursor or stylus position in the [component coordinate system](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkui-glossary#component-coordinate-system) based on the current component.

Unit: vp.

**Atomic service API**: This API can be used in atomic services since API version 15.

 |
| y15+ | number | No | Yes | 

Y coordinate of the cursor or stylus position in the [component coordinate system](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkui-glossary#component-coordinate-system) based on the current component.

Unit: vp.

**Atomic service API**: This API can be used in atomic services since API version 15.

 |
| windowX15+ | number | No | Yes | 

X coordinate of the cursor or stylus position in the coordinate system of the current application window.

Unit: vp.

**Atomic service API**: This API can be used in atomic services since API version 15.

 |
| windowY15+ | number | No | Yes | 

Y coordinate of the cursor or stylus position in the coordinate system of the current application window.

Unit: vp.

**Atomic service API**: This API can be used in atomic services since API version 15.

 |
| displayX15+ | number | No | Yes | 

X coordinate of the cursor or stylus position in the coordinate system of the current screen window.

Unit: vp.

**Atomic service API**: This API can be used in atomic services since API version 15.

 |
| displayY15+ | number | No | Yes | 

Y coordinate of the cursor or stylus position in the coordinate system of the current screen window.

Unit: vp.

**Atomic service API**: This API can be used in atomic services since API version 15.

 |
| stopPropagation | () => void | No | No | 

Disables [event bubbling](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-interaction-basic-principles#event-bubbling) propagation.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| globalDisplayX20+ | number | No | Yes | 

X coordinate of the cursor or stylus position in the [global coordinate system](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/window-terminology#global-coordinate-system).

Unit: vp.

Value range: \[0, +∞).

**Atomic service API**: This API can be used in atomic services since API version 20.

 |
| globalDisplayY20+ | number | No | Yes | 

Y coordinate of the cursor or stylus position in the [global coordinate system](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/window-terminology#global-coordinate-system).

Unit: vp.

Value range: \[0, +∞).

**Atomic service API**: This API can be used in atomic services since API version 20.

 |

#### Example

## Example 1: Using onHover

This example demonstrates how to set the [onHover](#onhover) event on a button. When the mouse or stylus hovers over the button, the event is triggered to dynamically change the text content and background color of the button.

// xxx.ets
@Entry
@Component
struct HoverEventExample {
  @State hoverText: string = 'no hover';
  @State color: Color = Color.Blue;

  build() {
    Column({ space: 20 }) {
      Button(this.hoverText, { type: ButtonType.Capsule })
        .width(180).height(80)
        .backgroundColor(this.color)
        .onHover((isHover: boolean, event: HoverEvent) => {
          // Use the onHover event to dynamically change the text content and background color of a button when the mouse pointer or stylus is hovered on it.
          // Use event.sourceTool to determine whether the device is a mouse device or stylus.
          if (isHover) {
            if (event.sourceTool == SourceTool.Pen) {
              this.hoverText = 'pen hover';
              this.color = Color.Pink;
            } else if (event.sourceTool == SourceTool.MOUSE) {
              this.hoverText = 'mouse hover';
              this.color = Color.Red;
            }
          } else {
            this.hoverText = 'no hover';
            this.color = Color.Blue;
          }
        })
    }.padding({ top: 30 }).width('100%')
  }
}

Diagrams:

The figure below shows how the button looks in the non-hovered state.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/R_elt61ISo63j7o2E4JF7Q/en-us_image_0000002537765382.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062232Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EEABCDD3F5C6C35AD5DCA97234F70A450B2B5017C8F2F138EF320DC830117D3C)

The figure below shows how the button looks when a stylus hovers on it.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/u9tyqFcPQkuOq8mDNNgW9A/en-us_image_0000002537925322.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062232Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=33BE7226175E1B92748B742A554D99A34D51E351E3536A6D880A62086468BD5B)

## Example 2: Using onHoverMove

This example demonstrates how to configure the [onHoverMove](#onhovermove15) event on a button, available since API version 15. When a stylus hovers over the button, the UI displays the current stylus position.

// xxx.ets
@Entry
@Component
struct OnHoverMoveEventExample {
  @State hoverMoveText: string = '';

  build() {
    Column({ space: 20 }) {
      Button('onHoverMove', { type: ButtonType.Capsule })
        .width(180).height(80)
        .onHoverMove((event: HoverEvent) => {
          this.hoverMoveText = 'onHoverMove:\\nXY = (' + event.x + ', ' + event.y + ')' +
                               '\\nwindowXY = (' + event.windowX + ', ' + event.windowY + ')' +
                               '\\ndisplayXY = (' + event.displayX + ', ' + event.displayY + ')';
        })

      Text(this.hoverMoveText)
    }.padding({ top: 30 }).width('100%')
  }
}

Diagrams:

When a stylus hovers over a button, the UI continuously updates to show the position of the stylus tip.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/tCoa2j-jRFKhMAm0Pwtqyg/en-us_image_0000002568685099.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062232Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4C3897238A434D009FE0BF157A8528AF35962F6F9DA440502A720DD6A5C19D83)
