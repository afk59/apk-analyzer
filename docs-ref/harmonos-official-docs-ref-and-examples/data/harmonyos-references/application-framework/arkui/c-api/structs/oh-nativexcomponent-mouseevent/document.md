# OH\_NativeXComponent\_MouseEvent

typedef struct {...} OH\_NativeXComponent\_MouseEvent

#### Overview

Defines a mouse event.

**Since**: 9

**Related module**: [OH\_NativeXComponent Native XComponent](../../modules/oh-nativexcomponent-native-xcomponent/document.md)

**Header file**: [native\_interface\_xcomponent.h](../../header-files/native-interface-xcomponent-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| float x | X coordinate of the clicked point relative to the upper left corner of the component. Unit: vp. |
| float y | Y coordinate of the clicked point relative to the upper left corner of the component. Unit: vp. |
| float screenX | X coordinate of the click point relative to the upper left corner of the application screen where the XComponent is located. Unit: vp. |
| float screenY | Y coordinate of the click point relative to the upper left corner of the application screen where the XComponent is located. Unit: vp. |
| int64\_t timestamp | Timestamp of the mouse event. It is interval between the time when the event is triggered and the time when the system starts, in nanoseconds. |
| [OH\_NativeXComponent\_MouseEventAction](../../header-files/native-interface-xcomponent-h/document.md#oh_nativexcomponent_mouseeventaction) action | Action of the mouse event. |
| [OH\_NativeXComponent\_MouseEventButton](../../header-files/native-interface-xcomponent-h/document.md#oh_nativexcomponent_mouseeventbutton) button | Button of the mouse event. |
