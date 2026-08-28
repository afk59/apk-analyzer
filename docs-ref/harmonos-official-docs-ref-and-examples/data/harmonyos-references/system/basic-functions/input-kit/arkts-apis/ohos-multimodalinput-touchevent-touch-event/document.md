# @ohos.multimodalInput.touchEvent (Touch Event)

The **touchEvent** module provides touch events reported by a device. It is inherited from [InputEvent](../ohos-multimodalinput-inputevent-input-event/document.md).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/bxg5RYqsQVuhIgoY7TlgZg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062404Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0F7594BA286F48816450A5AEDB2E6D408D49414EEABDCE1A2DDEF9FDFB533D36)

-   The initial APIs of this module are supported since API version 9. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { Action,ToolType,SourceType,Touch,TouchEvent } from '@kit.InputKit';

#### Action

Enumerates the touch event types.

**System capability**: SystemCapability.MultimodalInput.Input.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| CANCEL | 0 | Touch cancellation. The down event of the touchscreen is interrupted unexpectedly and does not close normally. For example, the **CANCEL** event is triggered when the finger is pressed but not lifted, the screen is rotated or folded, or a new hover occurs. |
| DOWN | 1 | Touch press. |
| MOVE | 2 | Touch moving. |
| UP | 3 | Touch release. |

#### ToolType

Enumerates touch tool types.

**System capability**: SystemCapability.MultimodalInput.Input.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| FINGER | 0 | Finger. |
| PEN | 1 | Stylus. |
| RUBBER | 2 | Eraser. |
| BRUSH | 3 | Brush. |
| PENCIL | 4 | Pencil. |
| AIRBRUSH | 5 | Air brush. |
| MOUSE | 6 | Mouse. |
| LENS | 7 | Lens. |

#### SourceType

Enumerates touch sources. Currently, only the touchscreen and touchpad are supported.

**System capability**: SystemCapability.MultimodalInput.Input.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| TOUCH\_SCREEN | 0 | Touchscreen. |
| PEN | 1 | Stylus. |
| TOUCH\_PAD | 2 | Touchpad. |

#### Touch

Defines the touch point information.

**System capability**: SystemCapability.MultimodalInput.Input.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| id | number | No | No | Touch event ID. |
| pressedTime | number | No | No | Press timestamp, in μs. |
| screenX | number | No | No | X coordinate of the touch event in the relative coordinate system with the upper-left corner of the specified screen as the origin. The value can only be an integer. |
| screenY | number | No | No | Y coordinate of the touch event in the relative coordinate system with the upper-left corner of the specified screen as the origin. The value can only be an integer. |
| windowX | number | No | No | X coordinate in the relative coordinate system with the upper-left corner of the window where the touch is located as the origin. The value can only be an integer. |
| windowY | number | No | No | Y coordinate in the relative coordinate system with the upper-left corner of the window where the touch is located as the origin. The value can only be an integer. |
| pressure | number | No | No | Pressure value. The value range is \[0.0, 1.0\]. The value **0.0** indicates that the pressure is not supported. |
| width | number | No | No | Width of the touch area. The value can only be an integer. |
| height | number | No | No | Height of the touch area. The value can only be an integer. |
| tiltX | number | No | No | Angle relative to the YZ plane. The value range is \[-90, 90\]. A positive value indicates a rightward tilt. |
| tiltY | number | No | No | Angle relative to the XZ plane. The value range is \[-90, 90\]. A positive value indicates a downward tilt. |
| toolX | number | No | No | X coordinate of the tool area center in the relative coordinate system with the upper-left corner of the specified screen as the origin. The value can only be an integer. |
| toolY | number | No | No | Y coordinate of the tool area center in the relative coordinate system with the upper-left corner of the specified screen as the origin. The value can only be an integer. |
| toolWidth | number | No | No | Width of the tool area. The value can only be an integer. |
| toolHeight | number | No | No | Height of the tool area. The value can only be an integer. |
| rawX | number | No | No | X coordinate of the input device. The value can only be an integer. |
| rawY | number | No | No | Y coordinate of the input device. The value can only be an integer. |
| toolType | [ToolType](#tooltype) | No | No | Tool type. |
| globalX20+ | number | No | Yes | X coordinate of the touch event in the global coordinate system with the upper-left corner of the primary screen as the origin. When being used as an output parameter, its value is reported by the system. |
| globalY20+ | number | No | Yes | Y coordinate of the touch event in the global coordinate system with the upper-left corner of the primary screen as the origin. When being used as an output parameter, its value is reported by the system. |

#### TouchEvent

Defines a touch event.

**System capability**: SystemCapability.MultimodalInput.Input.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| action | [Action](#action) | No | No | Event type. |
| touch | [Touch](#touch) | No | No | Current touch point. |
| touches | [Touch](#touch)\[\] | No | No | All touch points. |
| sourceType | [SourceType](#sourcetype) | No | No | Device type of the touch source. |
