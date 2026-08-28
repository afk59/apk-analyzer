# OH\_NativeXComponent\_HistoricalPoint

typedef struct {...} OH\_NativeXComponent\_HistoricalPoint

#### Overview

Represents a historical touch point.

**Since**: 10

**Related module**: [OH\_NativeXComponent Native XComponent](../../modules/oh-nativexcomponent-native-xcomponent/document.md)

**Header file**: [native\_interface\_xcomponent.h](../../header-files/native-interface-xcomponent-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| int32\_t id | Unique identifier of the finger. |
| float screenX | X-coordinate of the touch point relative to the upper left corner of the application window where the XComponent is located. |
| float screenY | Y-coordinate of the touch point relative to the upper left corner of the application window where the XComponent is located. |
| float x | X-coordinate of the touch point relative to the left edge of the XComponent. |
| float y | Y-coordinate of the touch point relative to the upper edge of the XComponent. |
| [OH\_NativeXComponent\_TouchEventType](../../header-files/native-interface-xcomponent-h/document.md#oh_nativexcomponent_toucheventtype) type | Touch type of the touch event. |
| double size | Contact area between the finger pad and the screen. |
| float force | Pressure of the touch event. |
| int64\_t timeStamp | Timestamp of the touch event. It is interval between the time when the event is triggered and the time when the system starts, in nanoseconds. |
| float titlX | Angle between the projection on the x-y plane and the z-axis of the touch event. |
| float titlY | Angle between the projection on the y-z plane and the z-axis of the current touch event. |
| [OH\_NativeXComponent\_TouchEvent\_SourceTool](../../header-files/native-interface-xcomponent-h/document.md#oh_nativexcomponent_touchevent_sourcetool) sourceTool | Source tool of the touch event. |
