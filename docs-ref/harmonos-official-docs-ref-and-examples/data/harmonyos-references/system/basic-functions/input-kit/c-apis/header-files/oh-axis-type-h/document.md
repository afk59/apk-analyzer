# oh\_axis\_type.h

#### Overview

Defines the axis event structures and enumerations.

**File to include**: <multimodalinput/oh\_axis\_type.h>

**Library**: libohinput.so

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Since**: 12

**Related module**: [input](../../modules/input/document.md)

#### Summary

#### \[h2\]Enums

| **Name** | typedef Keyword | Description |
| :-- | :-- | :-- |
| [InputEvent\_AxisType](#inputevent_axistype) | InputEvent\_AxisType | Provides axis types of the input device. |
| [InputEvent\_AxisEventType](#inputevent_axiseventtype) | InputEvent\_AxisEventType | Provides event types of the input device. |
| [InputEvent\_AxisAction](#inputevent_axisaction) | InputEvent\_AxisAction | Provides actions of the input device. |

#### Enum Description

#### \[h2\]InputEvent\_AxisType

enum InputEvent\_AxisType

**Description**

Defines the axis type of an input device.

**Since**: 12

| Enum | Description |
| :-- | :-- |
| AXIS\_TYPE\_UNKNOWN | Unknown axis type, which is usually used as the initial value. |
| AXIS\_TYPE\_SCROLL\_VERTICAL | Vertical scroll axis. When you scroll the mouse wheel or slide with one or two fingers on the touchpad, the status of the vertical scroll axis changes. |
| AXIS\_TYPE\_SCROLL\_HORIZONTAL | Horizontal scroll axis. When you scroll the mouse wheel or slide with two fingers on the touchpad, the status of the horizontal scroll axis changes. |
| AXIS\_TYPE\_PINCH | Pinch axis, which is used to describe a two-finger pinch gesture on the touchpad. |
| AXIS\_TYPE\_ROTATE | Rotation axis, which is used to describe a two-finger rotation gesture on the touchpad. |

#### \[h2\]InputEvent\_AxisEventType

enum InputEvent\_AxisEventType

**Description**

Event type of the input device.

**Since**: 12

| Enum | Description |
| :-- | :-- |
| AXIS\_EVENT\_TYPE\_PINCH = 1 | 
Two-finger pinch event. The value can be **AXIS\_TYPE\_PINCH** or **AXIS\_TYPE\_ROTATE**.

**Since**: 12

 |
| AXIS\_EVENT\_TYPE\_SCROLL = 2 | 

Scroll axis event. The value can be **AXIS\_TYPE\_SCROLL\_VERTICAL** and **AXIS\_TYPE\_SCROLL\_HORIZONTAL**. For mouse wheel events, the value can only be **AXIS\_TYPE\_SCROLL\_VERTICAL**.

**Since**: 12

 |

#### \[h2\]InputEvent\_AxisAction

enum InputEvent\_AxisAction

**Description**

Action of the input device.

**Since**: 12

| Enum | Description |
| :-- | :-- |
| AXIS\_ACTION\_CANCEL = 0 | Cancellation of an axis input event. |
| AXIS\_ACTION\_BEGIN | Start of an axis input event. |
| AXIS\_ACTION\_UPDATE | Update of an axis input event. |
| AXIS\_ACTION\_END | End of an axis input event. |
