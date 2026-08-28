# OH\_NativeXComponent\_MouseEvent\_Callback

typedef struct OH\_NativeXComponent\_MouseEvent\_Callback {...} OH\_NativeXComponent\_MouseEvent\_Callback

#### Overview

Registers callbacks for the mouse event.

**Since**: 9

**Related module**: [OH\_NativeXComponent Native XComponent](../../modules/oh-nativexcomponent-native-xcomponent/document.md)

**Header file**: [native\_interface\_xcomponent.h](../../header-files/native-interface-xcomponent-h/document.md)

#### Summary

#### \[h2\]Member Functions

| Name | Description |
| :-- | :-- |
| [void (\*DispatchMouseEvent)(OH\_NativeXComponent\* component, void\* window)](#dispatchmouseevent) | Invoked when a mouse event is triggered. |
| [void (\*DispatchHoverEvent)(OH\_NativeXComponent\* component, bool isHover)](#dispatchhoverevent) | Invoked when a hover event is triggered. |

#### Member Function Description

#### \[h2\]DispatchMouseEvent()

void (\*DispatchMouseEvent)(OH\_NativeXComponent\* component, void\* window)

**Description**

Invoked when a mouse event is triggered.

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NativeXComponent](../oh-nativexcomponent/document.md)\* component | Pointer to an [OH\_NativeXComponent](../oh-nativexcomponent/document.md) instance. |
| void\* window | Handle to the **NativeWindow** instance. |

#### \[h2\]DispatchHoverEvent()

void (\*DispatchHoverEvent)(OH\_NativeXComponent\* component, bool isHover)

**Description**

Invoked when a hover event is triggered.

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NativeXComponent](../oh-nativexcomponent/document.md)\* component | Pointer to an [OH\_NativeXComponent](../oh-nativexcomponent/document.md) instance. |
| bool isHover | Whether the mouse pointer or stylus is hovering over the component. **true**: The mouse pointer or stylus has entered the component. **false**: The mouse pointer or stylus has left the component. |
