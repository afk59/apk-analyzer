# @ohos.multimodalInput.mouseEvent (Mouse Event)

The **mouseEvent** module provides mouse events reported by a device. It is inherited from [InputEvent](../ohos-multimodalinput-inputevent-input-event/document.md).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/wFGrwCxBQVWrmQk71T7h6A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062404Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DD9B1D65058FAD99167BCB9B714C49710FEF8AF06FF856699E5C769154DC6339)

-   The initial APIs of this module are supported since API version 9. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { Action, Button, Axis, AxisValue, MouseEvent } from '@kit.InputKit';

#### Action

Enumerates mouse event types.

**System capability**: SystemCapability.MultimodalInput.Input.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| CANCEL | 0 | Canceled. The down event of the mouse is interrupted unexpectedly and does not close normally. For example, the **CANCEL** event is triggered when the mouse button is pressed but not released, the window transitions to the background, or an abnormal destruction occurs. |
| MOVE | 1 | Moving of the mouse pointer. |
| BUTTON\_DOWN | 2 | Mouse button press. |
| BUTTON\_UP | 3 | Mouse button release. |
| AXIS\_BEGIN | 4 | Beginning of the mouse axis event. |
| AXIS\_UPDATE | 5 | Updating of the mouse axis event. |
| AXIS\_END | 6 | Mouse axis event ended. |
| ACTION\_DOWN11+ | 7 | Touchpad press. |
| ACTION\_UP11+ | 8 | Touchpad release. |

#### Button

Enumerates mouse buttons.

**System capability**: SystemCapability.MultimodalInput.Input.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| LEFT | 0 | Left button. |
| MIDDLE | 1 | Middle button. |
| RIGHT | 2 | Right button |
| SIDE | 3 | Side button. |
| EXTRA | 4 | Extended button. |
| FORWARD | 5 | Forward button. |
| BACK | 6 | Back button. |
| TASK | 7 | Task button. |

#### Axis

Enumerates mouse axis types.

**System capability**: SystemCapability.MultimodalInput.Input.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| SCROLL\_VERTICAL | 0 | Vertical scroll axis of the mouse. |
| SCROLL\_HORIZONTAL | 1 | Horizontal scroll axis of the mouse. |
| PINCH | 2 | Pinch axis of the mouse. |

#### AxisValue

Defines the mouse axis type and axis value.

**System capability**: SystemCapability.MultimodalInput.Input.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| axis | [Axis](#axis) | No | No | Enumerates mouse axis types. |
| value | number | No | No | Mouse axis value. |

#### ToolType11+

Enumerates tool types.

**System capability**: SystemCapability.MultimodalInput.Input.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| UNKNOWN | 0 | Unknown type. |
| MOUSE | 1 | Mouse. |
| JOYSTICK | 2 | Joystick. |
| TOUCHPAD | 3 | Touchpad. |

#### MouseEvent

Defines the mouse event.

**System capability**: SystemCapability.MultimodalInput.Input.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| action | [Action](#action) | No | No | Enumerates mouse event types. |
| screenX | number | No | No | X coordinate of the mouse event in the relative coordinate system with the upper-left corner of the specified screen as the origin. The value can only be set to an integer. |
| screenY | number | No | No | Y coordinate of the mouse event in the relative coordinate system with the upper-left corner of the specified screen as the origin. The value can only be set to an integer. |
| windowX | number | No | No | X coordinate in the relative coordinate system with the upper-left corner of the window where the mouse is located as the origin. The value can only be set to an integer. |
| windowY | number | No | No | Y coordinate in the relative coordinate system with the upper-left corner of the window where the mouse is located as the origin. The value can only be set to an integer. |
| rawDeltaX | number | No | No | X coordinate offset of the current mouse event relative to the last event. The value can only be set to an integer. |
| rawDeltaY | number | No | No | Y coordinate offset of the current mouse event relative to the last event. The value can only be set to an integer. |
| button | [Button](#button) | No | No | Enumerates mouse buttons. |
| pressedButtons | [Button](#button)\[\] | No | No | Button being pressed. |
| axes | [AxisValue](#axisvalue)\[\] | No | No | Defines the mouse axis type and axis value. |
| pressedKeys | [KeyCode](../ohos-multimodalinput-keycode-keycode/document.md#keycode)\[\] | No | No | List of pressed keys. |
| ctrlKey | boolean | No | No | 
Whether ctrlKey is being pressed.

The value **true** indicates that the key is pressed, and the value **false** indicates the opposite.

 |
| altKey | boolean | No | No | 

Whether altKey is being pressed.

The value **true** indicates that the key is pressed, and the value **false** indicates the opposite.

 |
| shiftKey | boolean | No | No | 

Whether shiftKey is being pressed.

The value **true** indicates that the key is pressed, and the value **false** indicates the opposite.

 |
| logoKey | boolean | No | No | 

Whether logoKey is being pressed.

The value **true** indicates that the key is pressed, and the value **false** indicates the opposite.

 |
| fnKey | boolean | No | No | 

Whether fnKey is being pressed.

The value **true** indicates that the key is pressed, and the value **false** indicates the opposite.

 |
| capsLock | boolean | No | No | 

Whether capsLock is enabled.

The value **true** indicates that capsLock is enabled, and the value **false** indicates the opposite.

 |
| numLock | boolean | No | No | 

Whether numLock is enabled.

The value **true** indicates that numLock is enabled, and the value **false** indicates the opposite.

 |
| scrollLock | boolean | No | No | 

Whether scrollLock is enabled.

The value **true** indicates that scrollLock is enabled, and the value **false** indicates the opposite.

 |
| toolType11+ | [ToolType](#tooltype11) | No | No | Tool type. |
| globalX20+ | number | No | Yes | X coordinate of the mouse event in the global coordinate system with the upper-left corner of the primary screen as the origin. When being used as an output parameter, its value is reported by the system. |
| globalY20+ | number | No | Yes | Y coordinate of the mouse event in the global coordinate system with the upper-left corner of the primary screen as the origin. When being used as an output parameter, its value is reported by the system. |
