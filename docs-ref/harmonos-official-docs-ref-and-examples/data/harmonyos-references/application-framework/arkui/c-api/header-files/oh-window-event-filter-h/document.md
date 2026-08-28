# oh\_window\_event\_filter.h

#### Overview

The file declares the APIs for a window to filter multimodal key events. When a multimodal input event passes through the window, the window can interrupt the event to prevent it from being further distributed.

**File to include**: <window\_manager/oh\_window\_event\_filter.h>

**Library**: libnative\_window\_manager.so

**System capability**: SystemCapability.Window.SessionManager

**Since**: 12

**Related module**: [WindowManager](../../modules/windowmanager/document.md)

#### Summary

#### \[h2\]Functions

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [typedef bool (\*OH\_NativeWindowManager\_KeyEventFilter)(Input\_KeyEvent\* keyEvent)](#oh_nativewindowmanager_keyeventfilter) | OH\_NativeWindowManager\_KeyEventFilter | Defines a function for filtering multimodal key events. |
| [WindowManager\_ErrorCode OH\_NativeWindowManager\_RegisterKeyEventFilter(int32\_t windowId,OH\_NativeWindowManager\_KeyEventFilter keyEventFilter)](#oh_nativewindowmanager_registerkeyeventfilter) | \- | Registers a function for filtering multimodal key events. |
| [WindowManager\_ErrorCode OH\_NativeWindowManager\_UnregisterKeyEventFilter(int32\_t windowId)](#oh_nativewindowmanager_unregisterkeyeventfilter) | \- | Unregisters a function for filtering multimodal key events. |
| [typedef bool (\*OH\_NativeWindowManager\_MouseEventFilter)(Input\_MouseEvent\* mouseEvent)](#oh_nativewindowmanager_mouseeventfilter) | OH\_NativeWindowManager\_MouseEventFilter | Defines a function for filtering multimodal mouse events. |
| [WindowManager\_ErrorCode OH\_NativeWindowManager\_RegisterMouseEventFilter(int32\_t windowId,OH\_NativeWindowManager\_MouseEventFilter mouseEventFilter)](#oh_nativewindowmanager_registermouseeventfilter) | \- | Registers a function for filtering multimodal mouse events. |
| [WindowManager\_ErrorCode OH\_NativeWindowManager\_UnregisterMouseEventFilter(int32\_t windowId)](#oh_nativewindowmanager_unregistermouseeventfilter) | \- | Unregisters a function for filtering multimodal mouse events. |
| [typedef bool (\*OH\_NativeWindowManager\_TouchEventFilter)(Input\_TouchEvent\* touchEvent)](#oh_nativewindowmanager_toucheventfilter) | OH\_NativeWindowManager\_TouchEventFilter | Defines a function for filtering multimodal touch events. |
| [WindowManager\_ErrorCode OH\_NativeWindowManager\_RegisterTouchEventFilter(int32\_t windowId,OH\_NativeWindowManager\_TouchEventFilter touchEventFilter)](#oh_nativewindowmanager_registertoucheventfilter) | \- | Registers a function for filtering multimodal touch events. |
| [WindowManager\_ErrorCode OH\_NativeWindowManager\_UnregisterTouchEventFilter(int32\_t windowId)](#oh_nativewindowmanager_unregistertoucheventfilter) | \- | Unregisters a function for filtering multimodal touch events. |

#### Function Description

#### \[h2\]OH\_NativeWindowManager\_KeyEventFilter()

typedef bool (\*OH\_NativeWindowManager\_KeyEventFilter)(Input\_KeyEvent\* keyEvent)

**Description**

Defines a function for filtering multimodal key events.

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [Input\_KeyEvent](../../../../../system/basic-functions/input-kit/c-apis/structs/input-keyevent/document.md)\* keyEvent | Pointer to the multimodal key event. For details, see [Input\_KeyEvent](../../../../../system/basic-functions/input-kit/c-apis/structs/input-keyevent/document.md). The event is defined in **oh\_input\_manager**. |

**Return value**

| Type | Description |
| :-- | :-- |
| bool | Whether the event will be intercepted. **true** if intercepted, **false** otherwise. |

#### \[h2\]OH\_NativeWindowManager\_RegisterKeyEventFilter()

WindowManager\_ErrorCode OH\_NativeWindowManager\_RegisterKeyEventFilter(int32\_t windowId,OH\_NativeWindowManager\_KeyEventFilter keyEventFilter)

**Description**

Registers a function for filtering multimodal key events.

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| int32\_t windowId | ID of the window for which the function is registered. |
| [OH\_NativeWindowManager\_KeyEventFilter](#oh_nativewindowmanager_keyeventfilter) keyEventFilter | Function to register. |

**Return value**

| Type | Description |
| :-- | :-- |
| [WindowManager\_ErrorCode](../oh-window-comm-h/document.md#windowmanager_errorcode) | Status code defined in [WindowManager\_ErrorCode](../oh-window-comm-h/document.md#windowmanager_errorcode). |

#### \[h2\]OH\_NativeWindowManager\_UnregisterKeyEventFilter()

WindowManager\_ErrorCode OH\_NativeWindowManager\_UnregisterKeyEventFilter(int32\_t windowId)

**Description**

Unregisters a function for filtering multimodal key events.

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| int32\_t windowId | ID of the window for which the function is unregistered. |

**Return value**

| Type | Description |
| :-- | :-- |
| [WindowManager\_ErrorCode](../oh-window-comm-h/document.md#windowmanager_errorcode) | Status code defined in [WindowManager\_ErrorCode](../oh-window-comm-h/document.md#windowmanager_errorcode). |

#### \[h2\]OH\_NativeWindowManager\_MouseEventFilter()

typedef bool (\*OH\_NativeWindowManager\_MouseEventFilter)(Input\_MouseEvent\* mouseEvent)

**Description**

Defines a function for filtering multimodal mouse events.

**Since**: 15

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [Input\_MouseEvent](../../../../../system/basic-functions/input-kit/c-apis/structs/input-mouseevent/document.md)\* mouseEvent | Pointer to the multimodal mouse event. For details, see [Input\_MouseEvent](../../../../../system/basic-functions/input-kit/c-apis/structs/input-mouseevent/document.md). The event is defined in **oh\_input\_manager**. |

**Return value**

| Type | Description |
| :-- | :-- |
| bool | Whether the event will be intercepted. **true** if the event will be intercepted; returns **false** otherwise. |

#### \[h2\]OH\_NativeWindowManager\_RegisterMouseEventFilter()

WindowManager\_ErrorCode OH\_NativeWindowManager\_RegisterMouseEventFilter(int32\_t windowId,OH\_NativeWindowManager\_MouseEventFilter mouseEventFilter)

**Description**

Registers a function for filtering multimodal mouse events.

**Since**: 15

**Parameters**

| Parameter | Description |
| :-- | :-- |
| int32\_t windowId | ID of the window for which the function is registered. |
| [OH\_NativeWindowManager\_MouseEventFilter](#oh_nativewindowmanager_mouseeventfilter) mouseEventFilter | Function to register. |

**Return value**

| Type | Description |
| :-- | :-- |
| [WindowManager\_ErrorCode](../oh-window-comm-h/document.md#windowmanager_errorcode) | Status code defined in [WindowManager\_ErrorCode](../oh-window-comm-h/document.md#windowmanager_errorcode). |

#### \[h2\]OH\_NativeWindowManager\_UnregisterMouseEventFilter()

WindowManager\_ErrorCode OH\_NativeWindowManager\_UnregisterMouseEventFilter(int32\_t windowId)

**Description**

Unregisters a function for filtering multimodal mouse events.

**Since**: 15

**Parameters**

| Parameter | Description |
| :-- | :-- |
| int32\_t windowId | ID of the window for which the function is unregistered. |

**Return value**

| Type | Description |
| :-- | :-- |
| [WindowManager\_ErrorCode](../oh-window-comm-h/document.md#windowmanager_errorcode) | Status code defined in [WindowManager\_ErrorCode](../oh-window-comm-h/document.md#windowmanager_errorcode). |

#### \[h2\]OH\_NativeWindowManager\_TouchEventFilter()

typedef bool (\*OH\_NativeWindowManager\_TouchEventFilter)(Input\_TouchEvent\* touchEvent)

**Description**

Defines a function for filtering multimodal touch events.

**Since**: 15

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [Input\_TouchEvent](../../../../../system/basic-functions/input-kit/c-apis/structs/input-touchevent/document.md)\* touchEvent | Pointer to the multimodal touch event. For details, see [Input\_TouchEvent](../../../../../system/basic-functions/input-kit/c-apis/structs/input-touchevent/document.md). The event is defined in **oh\_input\_manager**. |

**Return value**

| Type | Description |
| :-- | :-- |
| bool | Whether the event will be intercepted. **true** if the event will be intercepted; returns **false** otherwise. |

#### \[h2\]OH\_NativeWindowManager\_RegisterTouchEventFilter()

WindowManager\_ErrorCode OH\_NativeWindowManager\_RegisterTouchEventFilter(int32\_t windowId,OH\_NativeWindowManager\_TouchEventFilter touchEventFilter)

**Description**

Registers a function for filtering multimodal touch events.

**Since**: 15

**Parameters**

| Parameter | Description |
| :-- | :-- |
| int32\_t windowId | ID of the window for which the function is registered. |
| [OH\_NativeWindowManager\_TouchEventFilter](#oh_nativewindowmanager_toucheventfilter) touchEventFilter | Function to register. |

**Return value**

| Type | Description |
| :-- | :-- |
| [WindowManager\_ErrorCode](../oh-window-comm-h/document.md#windowmanager_errorcode) | Status code defined in [WindowManager\_ErrorCode](../oh-window-comm-h/document.md#windowmanager_errorcode). |

#### \[h2\]OH\_NativeWindowManager\_UnregisterTouchEventFilter()

WindowManager\_ErrorCode OH\_NativeWindowManager\_UnregisterTouchEventFilter(int32\_t windowId)

**Description**

Unregisters a function for filtering multimodal touch events.

**Since**: 15

**Parameters**

| Parameter | Description |
| :-- | :-- |
| int32\_t windowId | ID of the window for which the function is unregistered. |

**Return value**

| Type | Description |
| :-- | :-- |
| [WindowManager\_ErrorCode](../oh-window-comm-h/document.md#windowmanager_errorcode) | Status code defined in [WindowManager\_ErrorCode](../oh-window-comm-h/document.md#windowmanager_errorcode). |
