# OH\_NativeXComponent\_TouchEvent

typedef struct {...} OH\_NativeXComponent\_TouchEvent

#### Overview

Defines the touch event.

**Since**: 8

**Related module**: [OH\_NativeXComponent Native XComponent](../../modules/oh-nativexcomponent-native-xcomponent/document.md)

**Header file**: [native\_interface\_xcomponent.h](../../header-files/native-interface-xcomponent-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| int32\_t id | Unique identifier of the finger. |
| float screenX | X coordinate of the touch point relative to the upper left corner of the application window where the XComponent is located. |
| float screenY | Y coordinate of the touch point relative to the upper left corner of the application window where the XComponent is located. |
| float x | X coordinate of the touch point relative to the left edge of the XComponent. |
| float y | Y coordinate of the touch point relative to the upper edge of the XComponent. |
| [OH\_NativeXComponent\_TouchEventType](../../header-files/native-interface-xcomponent-h/document.md#oh_nativexcomponent_toucheventtype) type | Touch type of the touch event. |
| double size | Contact area between the finger pad and the screen. |
| float force | Pressure of the touch event. |
| int64\_t deviceId | ID of the device where the current touch event is triggered. |
| int64\_t timeStamp | Timestamp of the touch point. It is interval between the time when the event is triggered and the time when the system starts, in nanoseconds. |
| [OH\_NativeXComponent\_TouchPoint](../oh-nativexcomponent-touchpoint/document.md) touchPoints[\[OH\_NATIVE\_XCOMPONENT\_MAX\_TOUCH\_POINTS\_NUMBER\]](../../header-files/native-interface-xcomponent-h/document.md#variables) | Array of the touch points. |
| uint32\_t numPoints | Number of current touch points. The value **1** indicates single-finger touch, while a value greater than **1** indicates multi-finger touch. |
