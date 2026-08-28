# oh\_input\_manager.h

#### Overview

Provides functions such as event injection and status query.

**File to include**: <multimodalinput/oh\_input\_manager.h>

**Library**: libohinput.so

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Since**: 12

**Related module**: [input](../../modules/input/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [Input\_InterceptorEventCallback](../../structs/input-interceptoreventcallback/document.md) | Input\_InterceptorEventCallback | Defines the structure of interceptor callback events, including mouse events, touch events, and axis events. |
| [Input\_DeviceListener](../../structs/input-devicelistener/document.md) | Input\_DeviceListener | Defines a listener for device hot swap events. |
| [OH\_PixelmapNative](../../structs/oh-pixelmapnative/document.md) | OH\_PixelmapNative | Pixel map. |
| [Input\_KeyState](../../structs/input-keystate/document.md) | Input\_KeyState | Defines key information, which identifies a key pressing behavior. For example, the Ctrl key information contains the key value and key type. |
| [Input\_KeyEvent](../../structs/input-keyevent/document.md) | Input\_KeyEvent | Key event object. |
| [Input\_MouseEvent](../../structs/input-mouseevent/document.md) | Input\_MouseEvent | Mouse event object. |
| [Input\_TouchEvent](../../structs/input-touchevent/document.md) | Input\_TouchEvent | **TouchEvent** object. |
| [Input\_AxisEvent](../../structs/input-axisevent/document.md) | Input\_AxisEvent | Axis event object. |
| [Input\_Hotkey](../../structs/input-hotkey/document.md) | Input\_Hotkey | Defines the hotkey structure. |
| [Input\_DeviceInfo](../../structs/input-deviceinfo/document.md) | Input\_DeviceInfo | Defines the input device information. |
| [Input\_InterceptorOptions](../../structs/input-interceptoroptions/document.md) | Input\_InterceptorOptions | Defines event interception options. |
| [Input\_CustomCursor](../../structs/input-customcursor/document.md) | Input\_CustomCursor | Defines the pixel map resource of the custom mouse pointer object. |
| [Input\_CursorConfig](../../structs/input-cursorconfig/document.md) | Input\_CursorConfig | Defines the custom mouse pointer configuration. |
| [Input\_CursorInfo](../../structs/input-cursorinfo/document.md) | Input\_CursorInfo | Defines the mouse pointer information, including the pointer display status, style, size level, and color. |

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [Input\_KeyStateAction](#input_keystateaction) | Input\_KeyStateAction | Provides the enum values of the key status. |
| [Input\_KeyEventAction](#input_keyeventaction) | Input\_KeyEventAction | Provides the enum values of the key event type. |
| [Input\_MouseEventAction](#input_mouseeventaction) | Input\_MouseEventAction | Provides the enum values of mouse actions. |
| [InputEvent\_MouseAxis](#inputevent_mouseaxis) | InputEvent\_MouseAxis | Provides the enum values of mouse axis event types. |
| [Input\_MouseEventButton](#input_mouseeventbutton) | Input\_MouseEventButton | Provides the enum values of mouse buttons. |
| [Input\_TouchEventAction](#input_toucheventaction) | Input\_TouchEventAction | Provides the enum values of touch actions. |
| [Input\_InjectionStatus](#input_injectionstatus) | Input\_InjectionStatus | Provides the enum values of injection permission states. |
| [InputEvent\_SourceType](#inputevent_sourcetype) | InputEvent\_SourceType | Provides the enum values of event source types. |
| [Input\_KeyboardType](#input_keyboardtype) | Input\_KeyboardType | Provides the enum values of keyboard types of the input device. |
| [Input\_Result](#input_result) | Input\_Result | Provides return value enumerations. |

#### \[h2\]Functions

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [typedef void (\*Input\_HotkeyCallback)(Input\_Hotkey\* hotkey)](#input_hotkeycallback) | Input\_HotkeyCallback | Defines the callback used to return hotkey events. |
| [typedef void (\*Input\_KeyEventCallback)(const Input\_KeyEvent\* keyEvent)](#input_keyeventcallback) | Input\_KeyEventCallback | Defines a lifecycle callback for **keyEvent**. If the callback is triggered, **keyEvent** will be destroyed. |
| [typedef void (\*Input\_MouseEventCallback)(const Input\_MouseEvent\* mouseEvent)](#input_mouseeventcallback) | Input\_MouseEventCallback | Defines a lifecycle callback for **mouseEvent**. If the callback is triggered, **mouseEvent** will be destroyed. |
| [typedef void (\*Input\_TouchEventCallback)(const Input\_TouchEvent\* touchEvent)](#input_toucheventcallback) | Input\_TouchEventCallback | Defines the lifecycle callback for **TouchEvent**. If the callback is triggered, **TouchEvent** will be destroyed. |
| [typedef void (\*Input\_AxisEventCallback)(const Input\_AxisEvent\* axisEvent)](#input_axiseventcallback) | Input\_AxisEventCallback | Defines a lifecycle callback for **axisEvent**. If the callback is triggered, **axisEvent** will be destroyed. |
| [typedef void (\*Input\_DeviceAddedCallback)(int32\_t deviceId)](#input_deviceaddedcallback) | Input\_DeviceAddedCallback | Defines a callback used to receive device insertion events. |
| [typedef void (\*Input\_DeviceRemovedCallback)(int32\_t deviceId)](#input_deviceremovedcallback) | Input\_DeviceRemovedCallback | Defines a callback used to receive device removal events. |
| [typedef void (\*Input\_InjectAuthorizeCallback)(Input\_InjectionStatus authorizedStatus)](#input_injectauthorizecallback) | Input\_InjectAuthorizeCallback | Defines a callback used to receive the injection permission authorization status. |
| [Input\_Result OH\_Input\_GetKeyState(struct Input\_KeyState\* keyState)](#oh_input_getkeystate) | \- | Queries a key status enum object. |
| [struct Input\_KeyState\* OH\_Input\_CreateKeyState()](#oh_input_createkeystate) | \- | Creates a key status enum object. You can call [OH\_Input\_DestroyKeyState](#oh_input_destroykeystate) to destroy a key status enum object. |
| [void OH\_Input\_DestroyKeyState(struct Input\_KeyState\*\* keyState)](#oh_input_destroykeystate) | \- | Destroys a key status enum object. |
| [void OH\_Input\_SetKeyCode(struct Input\_KeyState\* keyState, int32\_t keyCode)](#oh_input_setkeycode) | \- | Sets the key value of a key status enum object. |
| [int32\_t OH\_Input\_GetKeyCode(const struct Input\_KeyState\* keyState)](#oh_input_getkeycode) | \- | Obtains the key value of a key status enum object. |
| [void OH\_Input\_SetKeyPressed(struct Input\_KeyState\* keyState, int32\_t keyAction)](#oh_input_setkeypressed) | \- | Sets whether the key specific to a key status enum object is pressed. |
| [int32\_t OH\_Input\_GetKeyPressed(const struct Input\_KeyState\* keyState)](#oh_input_getkeypressed) | \- | Checks whether the key specific to a key status enum object is pressed. |
| [void OH\_Input\_SetKeySwitch(struct Input\_KeyState\* keyState, int32\_t keySwitch)](#oh_input_setkeyswitch) | \- | Sets the key switch of the key status enum object. |
| [int32\_t OH\_Input\_GetKeySwitch(const struct Input\_KeyState\* keyState)](#oh_input_getkeyswitch) | \- | Obtains the key switch of the key status enum object. |
| [int32\_t OH\_Input\_InjectKeyEvent(const struct Input\_KeyEvent\* keyEvent)](#oh_input_injectkeyevent) | \- | Injects a key event. |
| [struct Input\_KeyEvent\* OH\_Input\_CreateKeyEvent()](#oh_input_createkeyevent) | \- | Creates a key event object. You can call [OH\_Input\_DestroyKeyEvent](#oh_input_destroykeyevent) to destroy a key event object. |
| [void OH\_Input\_DestroyKeyEvent(struct Input\_KeyEvent\*\* keyEvent)](#oh_input_destroykeyevent) | \- | Destroys a key event object. |
| [void OH\_Input\_SetKeyEventAction(struct Input\_KeyEvent\* keyEvent, int32\_t action)](#oh_input_setkeyeventaction) | \- | Sets the key event type. |
| [int32\_t OH\_Input\_GetKeyEventAction(const struct Input\_KeyEvent\* keyEvent)](#oh_input_getkeyeventaction) | \- | Obtains the key event type. |
| [void OH\_Input\_SetKeyEventKeyCode(struct Input\_KeyEvent\* keyEvent, int32\_t keyCode)](#oh_input_setkeyeventkeycode) | \- | Sets the key code value for a key event. |
| [int32\_t OH\_Input\_GetKeyEventKeyCode(const struct Input\_KeyEvent\* keyEvent)](#oh_input_getkeyeventkeycode) | \- | Obtains the key code value of a key event. |
| [void OH\_Input\_SetKeyEventActionTime(struct Input\_KeyEvent\* keyEvent, int64\_t actionTime)](#oh_input_setkeyeventactiontime) | \- | Sets the time when a key event occurs. |
| [int64\_t OH\_Input\_GetKeyEventActionTime(const struct Input\_KeyEvent\* keyEvent)](#oh_input_getkeyeventactiontime) | \- | Obtains the time when a key event occurs. |
| [void OH\_Input\_SetKeyEventWindowId(struct Input\_KeyEvent\* keyEvent, int32\_t windowId)](#oh_input_setkeyeventwindowid) | \- | Sets the window ID of a key event. |
| [int32\_t OH\_Input\_GetKeyEventWindowId(const struct Input\_KeyEvent\* keyEvent)](#oh_input_getkeyeventwindowid) | \- | Obtains the window ID of a key event. |
| [void OH\_Input\_SetKeyEventDisplayId(struct Input\_KeyEvent\* keyEvent, int32\_t displayId)](#oh_input_setkeyeventdisplayid) | \- | Sets the screen ID of a key event. |
| [int32\_t OH\_Input\_GetKeyEventDisplayId(const struct Input\_KeyEvent\* keyEvent)](#oh_input_getkeyeventdisplayid) | \- | Obtains the screen ID of a key event. |
| [struct Input\_MouseEvent\* OH\_Input\_CreateMouseEvent()](#oh_input_createmouseevent) | \- | Creates a mouse event object. You can call [OH\_Input\_DestroyMouseEvent](#oh_input_destroymouseevent) to destroy a mouse event object. |
| [void OH\_Input\_DestroyMouseEvent(struct Input\_MouseEvent\*\* mouseEvent)](#oh_input_destroymouseevent) | \- | Destroys a mouse event object. |
| [void OH\_Input\_SetMouseEventAction(struct Input\_MouseEvent\* mouseEvent, int32\_t action)](#oh_input_setmouseeventaction) | \- | Sets the action for a mouse event. |
| [int32\_t OH\_Input\_GetMouseEventAction(const struct Input\_MouseEvent\* mouseEvent)](#oh_input_getmouseeventaction) | \- | Obtains the action of a mouse event. |
| [void OH\_Input\_SetMouseEventDisplayX(struct Input\_MouseEvent\* mouseEvent, int32\_t displayX)](#oh_input_setmouseeventdisplayx) | \- | Sets the X coordinate of the mouse event in the relative coordinate system with the upper-left corner of the specified screen as the origin. |
| [int32\_t OH\_Input\_GetMouseEventDisplayX(const struct Input\_MouseEvent\* mouseEvent)](#oh_input_getmouseeventdisplayx) | \- | Obtains the X coordinate of the mouse event in the relative coordinate system with the upper-left corner of the specified screen as the origin. |
| [void OH\_Input\_SetMouseEventDisplayY(struct Input\_MouseEvent\* mouseEvent, int32\_t displayY)](#oh_input_setmouseeventdisplayy) | \- | Sets the Y coordinate of the mouse event in the relative coordinate system with the upper-left corner of the specified screen as the origin. |
| [int32\_t OH\_Input\_GetMouseEventDisplayY(const struct Input\_MouseEvent\* mouseEvent)](#oh_input_getmouseeventdisplayy) | \- | Obtains the Y coordinate of the mouse event in the relative coordinate system with the upper-left corner of the specified screen as the origin. |
| [void OH\_Input\_SetMouseEventButton(struct Input\_MouseEvent\* mouseEvent, int32\_t button)](#oh_input_setmouseeventbutton) | \- | Sets the button for a mouse event. |
| [int32\_t OH\_Input\_GetMouseEventButton(const struct Input\_MouseEvent\* mouseEvent)](#oh_input_getmouseeventbutton) | \- | Obtains the button of a mouse event. |
| [void OH\_Input\_SetMouseEventAxisType(struct Input\_MouseEvent\* mouseEvent, int32\_t axisType)](#oh_input_setmouseeventaxistype) | \- | Sets the axis type for a mouse event. |
| [int32\_t OH\_Input\_GetMouseEventAxisType(const struct Input\_MouseEvent\* mouseEvent)](#oh_input_getmouseeventaxistype) | \- | Obtains the axis type of a mouse event. |
| [void OH\_Input\_SetMouseEventAxisValue(struct Input\_MouseEvent\* mouseEvent, float axisValue)](#oh_input_setmouseeventaxisvalue) | \- | Sets the axis value for a mouse axis event. |
| [float OH\_Input\_GetMouseEventAxisValue(const struct Input\_MouseEvent\* mouseEvent)](#oh_input_getmouseeventaxisvalue) | \- | Obtains the axis value of a mouse axis event. |
| [void OH\_Input\_SetMouseEventActionTime(struct Input\_MouseEvent\* mouseEvent, int64\_t actionTime)](#oh_input_setmouseeventactiontime) | \- | Sets the time when a mouse event occurs. |
| [int64\_t OH\_Input\_GetMouseEventActionTime(const struct Input\_MouseEvent\* mouseEvent)](#oh_input_getmouseeventactiontime) | \- | Obtains the time when a mouse event occurs. |
| [void OH\_Input\_SetMouseEventWindowId(struct Input\_MouseEvent\* mouseEvent, int32\_t windowId)](#oh_input_setmouseeventwindowid) | \- | Sets the window ID of a mouse event. |
| [int32\_t OH\_Input\_GetMouseEventWindowId(const struct Input\_MouseEvent\* mouseEvent)](#oh_input_getmouseeventwindowid) | \- | Obtains the window ID of a mouse event. |
| [void OH\_Input\_SetMouseEventDisplayId(struct Input\_MouseEvent\* mouseEvent, int32\_t displayId)](#oh_input_setmouseeventdisplayid) | \- | Sets the screen ID of a mouse event. |
| [struct Input\_TouchEvent\* OH\_Input\_CreateTouchEvent()](#oh_input_createtouchevent) | \- | Creates a **TouchEvent** object. You can call [OH\_Input\_DestroyTouchEvent](#oh_input_destroytouchevent) to destroy a touch event object. |
| [void OH\_Input\_DestroyTouchEvent(struct Input\_TouchEvent\*\* touchEvent)](#oh_input_destroytouchevent) | \- | Destroys a **TouchEvent** object. |
| [void OH\_Input\_SetTouchEventAction(struct Input\_TouchEvent\* touchEvent, int32\_t action)](#oh_input_settoucheventaction) | \- | Sets the action of a touch event. |
| [int32\_t OH\_Input\_GetTouchEventAction(const struct Input\_TouchEvent\* touchEvent)](#oh_input_gettoucheventaction) | \- | Obtains the action of a touch event. |
| [void OH\_Input\_SetTouchEventFingerId(struct Input\_TouchEvent\* touchEvent, int32\_t id)](#oh_input_settoucheventfingerid) | \- | Sets the finger ID of a touch event. |
| [int32\_t OH\_Input\_GetTouchEventFingerId(const struct Input\_TouchEvent\* touchEvent)](#oh_input_gettoucheventfingerid) | \- | Obtains the finger ID of a touch event. |
| [void OH\_Input\_SetTouchEventDisplayX(struct Input\_TouchEvent\* touchEvent, int32\_t displayX)](#oh_input_settoucheventdisplayx) | \- | Sets the X coordinate of the touch event in the relative coordinate system with the upper-left corner of the specified screen as the origin. |
| [int32\_t OH\_Input\_GetTouchEventDisplayX(const struct Input\_TouchEvent\* touchEvent)](#oh_input_gettoucheventdisplayx) | \- | Obtains the X coordinate of the touch event in the relative coordinate system with the upper-left corner of the specified screen as the origin. |
| [void OH\_Input\_SetTouchEventDisplayY(struct Input\_TouchEvent\* touchEvent, int32\_t displayY)](#oh_input_settoucheventdisplayy) | \- | Sets the Y coordinate of the touch event in the relative coordinate system with the upper-left corner of the specified screen as the origin. |
| [int32\_t OH\_Input\_GetTouchEventDisplayY(const struct Input\_TouchEvent\* touchEvent)](#oh_input_gettoucheventdisplayy) | \- | Obtains the Y coordinate of the touch event in the relative coordinate system with the upper-left corner of the specified screen as the origin. |
| [void OH\_Input\_SetTouchEventActionTime(struct Input\_TouchEvent\* touchEvent, int64\_t actionTime)](#oh_input_settoucheventactiontime) | \- | Sets the time when a touch event occurs. |
| [int64\_t OH\_Input\_GetTouchEventActionTime(const struct Input\_TouchEvent\* touchEvent)](#oh_input_gettoucheventactiontime) | \- | Obtains the time when a touch event occurs. |
| [void OH\_Input\_SetTouchEventWindowId(struct Input\_TouchEvent\* touchEvent, int32\_t windowId)](#oh_input_settoucheventwindowid) | \- | Sets the window ID of a touch event. |
| [int32\_t OH\_Input\_GetTouchEventWindowId(const struct Input\_TouchEvent\* touchEvent)](#oh_input_gettoucheventwindowid) | \- | Obtains the window ID of a touch event. |
| [void OH\_Input\_SetTouchEventDisplayId(struct Input\_TouchEvent\* touchEvent, int32\_t displayId)](#oh_input_settoucheventdisplayid) | \- | Sets the screen ID of a touch event. |
| [int32\_t OH\_Input\_GetTouchEventDisplayId(const struct Input\_TouchEvent\* touchEvent)](#oh_input_gettoucheventdisplayid) | \- | Obtains the screen ID of a touch event. |
| [void OH\_Input\_CancelInjection()](#oh_input_cancelinjection) | \- | Stops event injection and revokes authorization. |
| [Input\_Result OH\_Input\_RequestInjection(Input\_InjectAuthorizeCallback callback)](#oh_input_requestinjection) | \- | Requests the permission for [OH\_Input\_InjectKeyEvent](#oh_input_injectkeyevent), [OH\_Input\_InjectTouchEvent](#oh_input_injecttouchevent), and [OH\_Input\_InjectMouseEvent](#oh_input_injectmouseevent). |
| [Input\_Result OH\_Input\_QueryAuthorizedStatus(Input\_InjectionStatus\* status)](#oh_input_queryauthorizedstatus) | \- | Queries the injection permission authorization status of the current application. |
| [Input\_AxisEvent\* OH\_Input\_CreateAxisEvent(void)](#oh_input_createaxisevent) | \- | Creates an axis event object. You can call [OH\_Input\_DestroyAxisEvent](#oh_input_destroyaxisevent) to destroy an axis event object. |
| [Input\_Result OH\_Input\_DestroyAxisEvent(Input\_AxisEvent\*\* axisEvent)](#oh_input_destroyaxisevent) | \- | Destroys an axis event object. |
| [Input\_Result OH\_Input\_SetAxisEventAction(Input\_AxisEvent\* axisEvent, InputEvent\_AxisAction action)](#oh_input_setaxiseventaction) | \- | Sets the action for an axis event. |
| [Input\_Result OH\_Input\_GetAxisEventAction(const Input\_AxisEvent\* axisEvent, InputEvent\_AxisAction \*action)](#oh_input_getaxiseventaction) | \- | Obtains the action of an axis event. |
| [Input\_Result OH\_Input\_SetAxisEventDisplayX(Input\_AxisEvent\* axisEvent, float displayX)](#oh_input_setaxiseventdisplayx) | \- | Sets the X coordinate of the axis event in the relative coordinate system with the upper-left corner of the specified screen as the origin. |
| [Input\_Result OH\_Input\_GetAxisEventDisplayX(const Input\_AxisEvent\* axisEvent, float\* displayX)](#oh_input_getaxiseventdisplayx) | \- | Obtains the X coordinate of the axis event in the relative coordinate system with the upper-left corner of the specified screen as the origin. |
| [Input\_Result OH\_Input\_SetAxisEventDisplayY(Input\_AxisEvent\* axisEvent, float displayY)](#oh_input_setaxiseventdisplayy) | \- | Sets the Y coordinate of the axis event in the relative coordinate system with the upper-left corner of the specified screen as the origin. |
| [Input\_Result OH\_Input\_GetAxisEventDisplayY(const Input\_AxisEvent\* axisEvent, float\* displayY)](#oh_input_getaxiseventdisplayy) | \- | Obtains the Y coordinate of the axis event in the relative coordinate system with the upper-left corner of the specified screen as the origin. |
| [Input\_Result OH\_Input\_SetAxisEventAxisValue(Input\_AxisEvent\* axisEvent,InputEvent\_AxisType axisType, double axisValue)](#oh_input_setaxiseventaxisvalue) | \- | Sets the axis value of the axis type specified by the axis event. |
| [Input\_Result OH\_Input\_GetAxisEventAxisValue(const Input\_AxisEvent\* axisEvent,InputEvent\_AxisType axisType, double\* axisValue)](#oh_input_getaxiseventaxisvalue) | \- | Obtains the axis value for the specified axis type of the axis event. |
| [Input\_Result OH\_Input\_SetAxisEventActionTime(Input\_AxisEvent\* axisEvent, int64\_t actionTime)](#oh_input_setaxiseventactiontime) | \- | Sets the time when an axis event occurs. |
| [Input\_Result OH\_Input\_GetAxisEventActionTime(const Input\_AxisEvent\* axisEvent, int64\_t\* actionTime)](#oh_input_getaxiseventactiontime) | \- | Obtains the time when an axis event occurs. |
| [Input\_Result OH\_Input\_SetAxisEventType(Input\_AxisEvent\* axisEvent, InputEvent\_AxisEventType axisEventType)](#oh_input_setaxiseventtype) | \- | Sets the axis event type. |
| [Input\_Result OH\_Input\_GetAxisEventType(const Input\_AxisEvent\* axisEvent, InputEvent\_AxisEventType\* axisEventType)](#oh_input_getaxiseventtype) | \- | Obtains the axis event type. |
| [Input\_Result OH\_Input\_SetAxisEventSourceType(Input\_AxisEvent\* axisEvent, InputEvent\_SourceType sourceType)](#oh_input_setaxiseventsourcetype) | \- | Sets the axis event source type. |
| [Input\_Result OH\_Input\_GetAxisEventSourceType(const Input\_AxisEvent\* axisEvent, InputEvent\_SourceType\* sourceType)](#oh_input_getaxiseventsourcetype) | \- | Obtains the axis event source type. |
| [Input\_Result OH\_Input\_SetAxisEventWindowId(Input\_AxisEvent\* axisEvent, int32\_t windowId)](#oh_input_setaxiseventwindowid) | \- | Sets the window ID of an axis event. |
| [Input\_Result OH\_Input\_GetAxisEventWindowId(const Input\_AxisEvent\* axisEvent, int32\_t\* windowId)](#oh_input_getaxiseventwindowid) | \- | Obtains the window ID of an axis event. |
| [Input\_Result OH\_Input\_SetAxisEventDisplayId(Input\_AxisEvent\* axisEvent, int32\_t displayId)](#oh_input_setaxiseventdisplayid) | \- | Sets the screen ID of an axis event. |
| [Input\_Result OH\_Input\_GetAxisEventDisplayId(const Input\_AxisEvent\* axisEvent, int32\_t\* displayId)](#oh_input_getaxiseventdisplayid) | \- | Obtains the screen ID of an axis event. |
| [Input\_Result OH\_Input\_AddKeyEventMonitor(Input\_KeyEventCallback callback)](#oh_input_addkeyeventmonitor) | \- | Adds a listener for key events. Only the initial addition takes effect. Subsequent attempts will be ignored. |
| [Input\_Result OH\_Input\_AddMouseEventMonitor(Input\_MouseEventCallback callback)](#oh_input_addmouseeventmonitor) | \- | Adds a listener for mouse events, including mouse click and movement events, but not scroll wheel events. Scroll wheel events are axis events. |
| [Input\_Result OH\_Input\_AddTouchEventMonitor(Input\_TouchEventCallback callback)](#oh_input_addtoucheventmonitor) | \- | Adds a listener for touch input events. |
| [Input\_Result OH\_Input\_AddAxisEventMonitorForAll(Input\_AxisEventCallback callback)](#oh_input_addaxiseventmonitorforall) | \- | Adds a listener for all types of axis events, which are defined in [InputEvent\_AxisEventType](../oh-axis-type-h/document.md#inputevent_axiseventtype). |
| [Input\_Result OH\_Input\_AddAxisEventMonitor(InputEvent\_AxisEventType axisEventType, Input\_AxisEventCallback callback)](#oh_input_addaxiseventmonitor) | \- | Adds a listener for the specified type of axis events, which are defined in [InputEvent\_AxisEventType](../oh-axis-type-h/document.md#inputevent_axiseventtype). |
| [Input\_Result OH\_Input\_RemoveKeyEventMonitor(Input\_KeyEventCallback callback)](#oh_input_removekeyeventmonitor) | \- | Removes the listener for key events. |
| [Input\_Result OH\_Input\_RemoveMouseEventMonitor(Input\_MouseEventCallback callback)](#oh_input_removemouseeventmonitor) | \- | Removes the listener for mouse events. |
| [Input\_Result OH\_Input\_RemoveTouchEventMonitor(Input\_TouchEventCallback callback)](#oh_input_removetoucheventmonitor) | \- | Removes the listener for touch events. |
| [Input\_Result OH\_Input\_RemoveAxisEventMonitorForAll(Input\_AxisEventCallback callback)](#oh_input_removeaxiseventmonitorforall) | \- | Removes the listener for all types of axis events. |
| [Input\_Result OH\_Input\_RemoveAxisEventMonitor(InputEvent\_AxisEventType axisEventType, Input\_AxisEventCallback callback)](#oh_input_removeaxiseventmonitor) | \- | Removes the listener for the specified type of axis events, which are defined in [InputEvent\_AxisEventType](../oh-axis-type-h/document.md#inputevent_axiseventtype). |
| [Input\_Result OH\_Input\_AddKeyEventInterceptor(Input\_KeyEventCallback callback, Input\_InterceptorOptions \*option)](#oh_input_addkeyeventinterceptor) | \- | Adds a key event interceptor. Only the first addition takes effect. Subsequent requests will return error code [INPUT\_REPEAT\_INTERCEPTOR](#input_result). Key events are intercepted only when the application gains focus. |
| [Input\_Result OH\_Input\_AddInputEventInterceptor(Input\_InterceptorEventCallback \*callback,Input\_InterceptorOptions \*option)](#oh_input_addinputeventinterceptor) | \- | Adds an interceptor for input events, including mouse, touch, and axis events. Only the first addition takes effect. Subsequent requests will return error code [INPUT\_REPEAT\_INTERCEPTOR](#input_result). Key events are intercepted only when the application window is hit. |
| [Input\_Result OH\_Input\_RemoveKeyEventInterceptor(void)](#oh_input_removekeyeventinterceptor) | \- | Removes the interceptor for key events. |
| [Input\_Result OH\_Input\_RemoveInputEventInterceptor(void)](#oh_input_removeinputeventinterceptor) | \- | Removes the interceptor for input events, including mouse, touch, and axis events. |
| [Input\_Result OH\_Input\_GetIntervalSinceLastInput(int64\_t \*timeInterval)](#oh_input_getintervalsincelastinput) | \- | Obtains the interval since the last system input event. |
| [Input\_Hotkey \*OH\_Input\_CreateHotkey(void)](#oh_input_createhotkey) | \- | Creates a hotkey object. You can call [OH\_Input\_DestroyHotkey](#oh_input_destroyhotkey) to destroy a hotkey object. |
| [void OH\_Input\_DestroyHotkey(Input\_Hotkey \*\*hotkey)](#oh_input_destroyhotkey) | \- | Destroys a hotkey object. |
| [void OH\_Input\_SetPreKeys(Input\_Hotkey \*hotkey, int32\_t \*preKeys, int32\_t size)](#oh_input_setprekeys) | \- | Sets the modifier keys. |
| [Input\_Result OH\_Input\_GetPreKeys(const Input\_Hotkey \*hotkey, int32\_t \*\*preKeys, int32\_t \*preKeyCount)](#oh_input_getprekeys) | \- | Obtains the modifier key. |
| [void OH\_Input\_SetFinalKey(Input\_Hotkey\* hotkey, int32\_t finalKey)](#oh_input_setfinalkey) | \- | Sets the modified key. |
| [Input\_Result OH\_Input\_GetFinalKey(const Input\_Hotkey\* hotkey, int32\_t \*finalKeyCode)](#oh_input_getfinalkey) | \- | Obtains the modified key. |
| [Input\_Hotkey \*\*OH\_Input\_CreateAllSystemHotkeys(int32\_t count)](#oh_input_createallsystemhotkeys) | \- | Creates an [Input\_Hotkey](../../structs/input-hotkey/document.md) array. You can call [OH\_Input\_DestroyAllSystemHotkeys](#oh_input_destroyallsystemhotkeys) to destroy the array of the [Input\_Hotkey](../../structs/input-hotkey/document.md) instance and reclaim the memory. |
| [void OH\_Input\_DestroyAllSystemHotkeys(Input\_Hotkey \*\*hotkeys, int32\_t count)](#oh_input_destroyallsystemhotkeys) | \- | Destroys an [Input\_Hotkey](../../structs/input-hotkey/document.md) array and reclaims the memory. |
| [Input\_Result OH\_Input\_GetAllSystemHotkeys(Input\_Hotkey \*\*hotkey, int32\_t \*count)](#oh_input_getallsystemhotkeys) | \- | Obtains all configured hotkeys. |
| [void OH\_Input\_SetRepeat(Input\_Hotkey\* hotkey, bool isRepeat)](#oh_input_setrepeat) | \- | Specifies whether to report repeated key events. |
| [Input\_Result OH\_Input\_GetRepeat(const Input\_Hotkey\* hotkey, bool \*isRepeat)](#oh_input_getrepeat) | \- | Checks whether to report repeated key events. |
| [Input\_Result OH\_Input\_AddHotkeyMonitor(const Input\_Hotkey\* hotkey, Input\_HotkeyCallback callback)](#oh_input_addhotkeymonitor) | \- | Subscribes to hotkey events. |
| [Input\_Result OH\_Input\_RemoveHotkeyMonitor(const Input\_Hotkey\* hotkey, Input\_HotkeyCallback callback)](#oh_input_removehotkeymonitor) | \- | Unsubscribes from hotkey events. |
| [Input\_Result OH\_Input\_RegisterDeviceListener(Input\_DeviceListener\* listener)](#oh_input_registerdevicelistener) | \- | Registers a listener for device hot swap events. |
| [Input\_Result OH\_Input\_UnregisterDeviceListener(Input\_DeviceListener\* listener)](#oh_input_unregisterdevicelistener) | \- | Unregisters the listener for device hot swap events. |
| [Input\_Result OH\_Input\_UnregisterDeviceListeners()](#oh_input_unregisterdevicelisteners) | \- | Unregisters the listener for all device hot swap events. |
| [Input\_Result OH\_Input\_GetDeviceIds(int32\_t \*deviceIds, int32\_t inSize, int32\_t \*outSize)](#oh_input_getdeviceids) | \- | Obtains the IDs of all input devices. |
| [Input\_Result OH\_Input\_GetDevice(int32\_t deviceId, Input\_DeviceInfo \*\*deviceInfo)](#oh_input_getdevice) | \- | Obtains information about the input device. |
| [Input\_DeviceInfo\* OH\_Input\_CreateDeviceInfo(void)](#oh_input_createdeviceinfo) | \- | Creates a **deviceInfo** object. You can call [OH\_Input\_DestroyDeviceInfo](#oh_input_destroydeviceinfo) to destroy an input device information object. |
| [void OH\_Input\_DestroyDeviceInfo(Input\_DeviceInfo \*\*deviceInfo)](#oh_input_destroydeviceinfo) | \- | Destroys a **deviceInfo** object. |
| [Input\_Result OH\_Input\_GetKeyboardType(int32\_t deviceId, int32\_t \*keyboardType)](#oh_input_getkeyboardtype) | \- | Obtains the keyboard type of the input device. |
| [Input\_Result OH\_Input\_GetDeviceId(Input\_DeviceInfo \*deviceInfo, int32\_t \*id)](#oh_input_getdeviceid) | \- | Obtains the ID of an input device. |
| [Input\_Result OH\_Input\_GetDeviceName(Input\_DeviceInfo \*deviceInfo, char \*\*name)](#oh_input_getdevicename) | \- | Obtains the name of an input device. |
| [Input\_Result OH\_Input\_GetCapabilities(Input\_DeviceInfo \*deviceInfo, int32\_t \*capabilities)](#oh_input_getcapabilities) | \- | Obtains the capabilities of an input device, for example, a touchscreen, touchpad, or keyboard. |
| [Input\_Result OH\_Input\_GetDeviceVersion(Input\_DeviceInfo \*deviceInfo, int32\_t \*version)](#oh_input_getdeviceversion) | \- | Obtains the version information of an input device. |
| [Input\_Result OH\_Input\_GetDeviceProduct(Input\_DeviceInfo \*deviceInfo, int32\_t \*product)](#oh_input_getdeviceproduct) | \- | Obtains the product information of an input device. |
| [Input\_Result OH\_Input\_GetDeviceVendor(Input\_DeviceInfo \*deviceInfo, int32\_t \*vendor)](#oh_input_getdevicevendor) | \- | Obtains the vendor information of an input device. |
| [Input\_Result OH\_Input\_GetDeviceAddress(Input\_DeviceInfo \*deviceInfo, char \*\*address)](#oh_input_getdeviceaddress) | \- | Obtains the physical address of an input device. |
| [Input\_Result OH\_Input\_GetFunctionKeyState(int32\_t keyCode, int32\_t \*state)](#oh_input_getfunctionkeystate) | \- | Obtains the function key status. |
| [int32\_t OH\_Input\_InjectTouchEvent(const struct Input\_TouchEvent\* touchEvent)](#oh_input_injecttouchevent) | \- | Injects a touch event by using coordinates in the relative coordinate system with the upper-left corner of the specified screen as the origin. |
| [int32\_t OH\_Input\_InjectMouseEvent(const struct Input\_MouseEvent\* mouseEvent)](#oh_input_injectmouseevent) | \- | Injects a mouse event by using coordinates in the relative coordinate system with the upper-left corner of the specified screen as the origin. |
| [int32\_t OH\_Input\_GetMouseEventDisplayId(const struct Input\_MouseEvent\* mouseEvent)](#oh_input_getmouseeventdisplayid) | \- | Obtains the screen ID of a mouse event. |
| [Input\_Result OH\_Input\_QueryMaxTouchPoints(int32\_t \*count)](#oh_input_querymaxtouchpoints) | \- | Queries the maximum number of touch points supported by the device. |
| [int32\_t OH\_Input\_InjectMouseEventGlobal(const struct Input\_MouseEvent\* mouseEvent)](#oh_input_injectmouseeventglobal) | \- | Injects a mouse event by using coordinates in the global coordinate system with the upper-left corner of the primary screen as the origin. |
| [void OH\_Input\_SetMouseEventGlobalX(struct Input\_MouseEvent\* mouseEvent, int32\_t globalX)](#oh_input_setmouseeventglobalx) | \- | Sets the X coordinate of the mouse event in the global coordinate system with the upper-left corner of the primary screen as the origin. |
| [int32\_t OH\_Input\_GetMouseEventGlobalX(const struct Input\_MouseEvent\* mouseEvent)](#oh_input_getmouseeventglobalx) | \- | Obtains the X coordinate of the mouse event in the global coordinate system with the upper-left corner of the primary screen as the origin. |
| [void OH\_Input\_SetMouseEventGlobalY(struct Input\_MouseEvent\* mouseEvent, int32\_t globalY)](#oh_input_setmouseeventglobaly) | \- | Sets the Y coordinate of the mouse event in the global coordinate system with the upper-left corner of the primary screen as the origin. |
| [int32\_t OH\_Input\_GetMouseEventGlobalY(const struct Input\_MouseEvent\* mouseEvent)](#oh_input_getmouseeventglobaly) | \- | Obtains the Y coordinate of the mouse event in the global coordinate system with the upper-left corner of the primary screen as the origin. |
| [int32\_t OH\_Input\_InjectTouchEventGlobal(const struct Input\_TouchEvent\* touchEvent)](#oh_input_injecttoucheventglobal) | \- | Injects a touch event by using coordinates in the global coordinate system with the upper-left corner of the primary screen as the origin. |
| [void OH\_Input\_SetTouchEventGlobalX(struct Input\_TouchEvent\* touchEvent, int32\_t globalX)](#oh_input_settoucheventglobalx) | \- | Sets the X coordinate of the touch event in the global coordinate system with the upper-left corner of the primary screen as the origin. |
| [int32\_t OH\_Input\_GetTouchEventGlobalX(const struct Input\_TouchEvent\* touchEvent)](#oh_input_gettoucheventglobalx) | \- | Obtains the X coordinate of the touch event in the global coordinate system with the upper-left corner of the primary screen as the origin. |
| [void OH\_Input\_SetTouchEventGlobalY(struct Input\_TouchEvent\* touchEvent, int32\_t globalY)](#oh_input_settoucheventglobaly) | \- | Sets the Y coordinate of the touch event in the global coordinate system with the upper-left corner of the primary screen as the origin. |
| [int32\_t OH\_Input\_GetTouchEventGlobalY(const struct Input\_TouchEvent\* touchEvent)](#oh_input_gettoucheventglobaly) | \- | Obtains the Y coordinate of the touch event in the global coordinate system with the upper-left corner of the primary screen as the origin. |
| [Input\_Result OH\_Input\_SetAxisEventGlobalX(struct Input\_AxisEvent\* axisEvent, int32\_t globalX)](#oh_input_setaxiseventglobalx) | \- | Sets the X coordinate of the axis event in the global coordinate system with the upper-left corner of the primary screen as the origin. |
| [Input\_Result OH\_Input\_GetAxisEventGlobalX(const Input\_AxisEvent\* axisEvent, int32\_t\* globalX)](#oh_input_getaxiseventglobalx) | \- | Obtains the X coordinate of the axis event in the global coordinate system with the upper-left corner of the primary screen as the origin. |
| [Input\_Result OH\_Input\_SetAxisEventGlobalY(struct Input\_AxisEvent\* axisEvent, int32\_t globalY)](#oh_input_setaxiseventglobaly) | \- | Sets the Y coordinate of the axis event in the global coordinate system with the upper-left corner of the primary screen as the origin. |
| [Input\_Result OH\_Input\_GetAxisEventGlobalY(const Input\_AxisEvent\* axisEvent, int32\_t\* globalY)](#oh_input_getaxiseventglobaly) | \- | Obtains the Y coordinate of the axis event in the global coordinate system with the upper-left corner of the primary screen as the origin. |
| [Input\_Result OH\_Input\_GetPointerLocation(int32\_t \*displayId, double \*displayX, double \*displayY)](#oh_input_getpointerlocation) | \- | Obtains the coordinates of the mouse pointer on the screen. |
| [Input\_Result OH\_Input\_GetKeyEventId(const struct Input\_KeyEvent\* keyEvent, int32\_t\* eventId)](#oh_input_getkeyeventid) | \- | Obtains the ID of a key event. |
| [Input\_Result OH\_Input\_AddKeyEventHook(Input\_KeyEventCallback callback)](#oh_input_addkeyeventhook) | \- | Adds a hook function for key event interception. |
| [Input\_Result OH\_Input\_RemoveKeyEventHook(Input\_KeyEventCallback callback)](#oh_input_removekeyeventhook) | \- | Removes the hook function for key event interception. |
| [Input\_Result OH\_Input\_DispatchToNextHandler(int32\_t eventId)](#oh_input_dispatchtonexthandler) | \- | Redispatches key events. |
| [Input\_Result OH\_Input\_SetPointerVisible(bool visible)](#oh_input_setpointervisible) | \- | Sets the visible status of the mouse pointer in the current window. |
| [Input\_Result OH\_Input\_GetPointerStyle(int32\_t windowId, int32\_t \*pointerStyle)](#oh_input_getpointerstyle) | \- | Obtains the mouse pointer style of the specified window. |
| [Input\_Result OH\_Input\_SetPointerStyle(int32\_t windowId, int32\_t pointerStyle)](#oh_input_setpointerstyle) | \- | Sets the mouse pointer style of the specified window. |
| [Input\_CustomCursor\* OH\_Input\_CustomCursor\_Create(OH\_PixelmapNative\* pixelMap, int32\_t anchorX, int32\_t anchorY)](#oh_input_customcursor_create) | \- | Creates a custom mouse pointer object. You can call [OH\_Input\_CustomCursor\_Destroy](#oh_input_customcursor_destroy) to destroy a custom mouse pointer resource object. |
| [void OH\_Input\_CustomCursor\_Destroy(Input\_CustomCursor\*\* customCursor)](#oh_input_customcursor_destroy) | \- | Destroys a custom mouse pointer object. |
| [Input\_Result OH\_Input\_CustomCursor\_GetPixelMap(Input\_CustomCursor\* customCursor, OH\_PixelmapNative\*\* pixelMap)](#oh_input_customcursor_getpixelmap) | \- | Obtains the pixel map of a custom mouse pointer object. |
| [Input\_Result OH\_Input\_CustomCursor\_GetAnchor(Input\_CustomCursor\* customCursor, int32\_t\* anchorX, int32\_t\* anchorY)](#oh_input_customcursor_getanchor) | \- | Obtains the focus coordinates of a custom mouse pointer object. |
| [Input\_CursorConfig\* OH\_Input\_CursorConfig\_Create(bool followSystem)](#oh_input_cursorconfig_create) | \- | Creates a custom mouse pointer configuration object. You can call [OH\_Input\_CursorConfig\_Destroy](#oh_input_cursorconfig_destroy) to destroy a custom mouse pointer configuration object. |
| [void OH\_Input\_CursorConfig\_Destroy(Input\_CursorConfig\*\* cursorConfig)](#oh_input_cursorconfig_destroy) | \- | Destroys a custom mouse pointer configuration object. |
| [Input\_Result OH\_Input\_CursorConfig\_IsFollowSystem(Input\_CursorConfig \*cursorConfig, bool \*followSystem)](#oh_input_cursorconfig_isfollowsystem) | \- | Queries whether the custom mouse pointer configuration follows the system setting to adjust the pointer size. |
| [Input\_Result OH\_Input\_SetCustomCursor(int32\_t windowId, Input\_CustomCursor\* customCursor, Input\_CursorConfig\* cursorConfig)](#oh_input_setcustomcursor) | \- | Sets the custom mouse pointer style. |
| [struct Input\_CursorInfo\* OH\_Input\_CursorInfo\_Create()](#oh_input_cursorinfo_create) | \- | Creates a mouse pointer information object. You can call [OH\_Input\_CursorInfo\_Destroy](#oh_input_cursorinfo_destroy) to destroy a mouse pointer information object. |
| [void OH\_Input\_CursorInfo\_Destroy(Input\_CursorInfo\*\* cursorInfo)](#oh_input_cursorinfo_destroy) | \- | Destroys the mouse pointer information object. |
| [Input\_Result OH\_Input\_CursorInfo\_IsVisible(Input\_CursorInfo\* cursorInfo, bool\* visible)](#oh_input_cursorinfo_isvisible) | \- | Obtains the pointer visible status of the specified mouse pointer information object. |
| [Input\_Result OH\_Input\_CursorInfo\_GetStyle(Input\_CursorInfo\* cursorInfo, Input\_PointerStyle\* style)](#oh_input_cursorinfo_getstyle) | \- | Obtains the pointer style of the specified mouse pointer information object. |
| [Input\_Result OH\_Input\_CursorInfo\_GetSizeLevel(Input\_CursorInfo\* cursorInfo, int32\_t\* sizeLevel)](#oh_input_cursorinfo_getsizelevel) | \- | Obtains the pointer size level of the specified mouse pointer information object. |
| [Input\_Result OH\_Input\_CursorInfo\_GetColor(Input\_CursorInfo\* cursorInfo, uint32\_t\* color)](#oh_input_cursorinfo_getcolor) | \- | Obtains the pointer color of the specified mouse pointer information object. |
| [Input\_Result OH\_Input\_GetMouseEventCursorInfo(const struct Input\_MouseEvent\* mouseEvent, Input\_CursorInfo\* cursorInfo)](#oh_input_getmouseeventcursorinfo) | \- | Obtains the mouse pointer information of the mouse event, including the pointer visible status, pointer style, pointer size level, and pointer color. |
| [Input\_Result OH\_Input\_GetCursorInfo(Input\_CursorInfo\* cursorInfo, OH\_PixelmapNative\*\* pixelmap)](#oh_input_getcursorinfo) | \- | Obtains the mouse pointer information, including the pointer visible status, pointer style, pointer size level, and pointer color. If the **pixelmap** parameter is not empty and the pointer style is [DEVELOPER\_DEFINED\_ICON](../oh-pointer-style-h/document.md#input_pointerstyle), the **PixelMap** object of the pointer is returned. |

#### Enum Description

#### \[h2\]Input\_KeyStateAction

enum Input\_KeyStateAction

**Description**

Provides the enum values of the key status.

**Since**: 12

| Enum | Description |
| :-- | :-- |
| KEY\_DEFAULT = -1 | Default state. |
| KEY\_PRESSED = 0 | Key press. |
| KEY\_RELEASED = 1 | Key release. |
| KEY\_SWITCH\_ON = 2 | Key switch enabled. |
| KEY\_SWITCH\_OFF = 3 | Key switch disabled. |

#### \[h2\]Input\_KeyEventAction

enum Input\_KeyEventAction

**Description**

Provides the enum values of the key event type.

**Since**: 12

| Enum | Description |
| :-- | :-- |
| KEY\_ACTION\_CANCEL = 0 | Button action canceled. |
| KEY\_ACTION\_DOWN = 1 | Key press. |
| KEY\_ACTION\_UP = 2 | Key release. |

#### \[h2\]Input\_MouseEventAction

enum Input\_MouseEventAction

**Description**

Provides the enum values of mouse actions.

**Since**: 12

| Enum | Description |
| :-- | :-- |
| MOUSE\_ACTION\_CANCEL = 0 | Cancellation of the mouse action. |
| MOUSE\_ACTION\_MOVE = 1 | Moving of the mouse pointer. |
| MOUSE\_ACTION\_BUTTON\_DOWN = 2 | Pressing of the mouse button. |
| MOUSE\_ACTION\_BUTTON\_UP = 3 | Release of the mouse button. |
| MOUSE\_ACTION\_AXIS\_BEGIN = 4 | Beginning of the mouse axis event. |
| MOUSE\_ACTION\_AXIS\_UPDATE = 5 | Updating of the mouse axis event. |
| MOUSE\_ACTION\_AXIS\_END = 6 | End of the mouse axis event. |

#### \[h2\]InputEvent\_MouseAxis

enum InputEvent\_MouseAxis

**Description**

Provides the enum values of mouse axis event types.

**Since**: 12

| Enum | Description |
| :-- | :-- |
| MOUSE\_AXIS\_SCROLL\_VERTICAL = 0 | Vertical scroll axis. |
| MOUSE\_AXIS\_SCROLL\_HORIZONTAL = 1 | Horizontal scroll axis. |

#### \[h2\]Input\_MouseEventButton

enum Input\_MouseEventButton

**Description**

Provides the enum values of mouse buttons.

**Since**: 12

| Enum | Description |
| :-- | :-- |
| MOUSE\_BUTTON\_NONE = -1 | Invalid button. |
| MOUSE\_BUTTON\_LEFT = 0 | Left button. |
| MOUSE\_BUTTON\_MIDDLE = 1 | Middle button. |
| MOUSE\_BUTTON\_RIGHT = 2 | Right button. |
| MOUSE\_BUTTON\_FORWARD = 3 | Forward button. |
| MOUSE\_BUTTON\_BACK = 4 | Back button. |

#### \[h2\]Input\_TouchEventAction

enum Input\_TouchEventAction

**Description**

Provides the enum values of touch actions.

**Since**: 12

| Enum | Description |
| :-- | :-- |
| TOUCH\_ACTION\_CANCEL = 0 | Touch cancellation. |
| TOUCH\_ACTION\_DOWN = 1 | Touch press. |
| TOUCH\_ACTION\_MOVE = 2 | Touch moving. |
| TOUCH\_ACTION\_UP = 3 | Touch release. |

#### \[h2\]Input\_InjectionStatus

enum Input\_InjectionStatus

**Description**

Provides the enum values of injection permission states.

**Since**: 20

| Enum | Description |
| :-- | :-- |
| UNAUTHORIZED = 0 | Permission not granted. |
| AUTHORIZING = 1 | Permission being granted. |
| AUTHORIZED = 2 | Permission granted. |

#### \[h2\]InputEvent\_SourceType

enum InputEvent\_SourceType

**Description**

Provides the enum values of event source types.

**Since**: 12

| Enum | Description |
| :-- | :-- |
| SOURCE\_TYPE\_MOUSE = 1 | Source that generates events similar to mouse pointer movement, button press and release, and wheel scrolling. |
| SOURCE\_TYPE\_TOUCHSCREEN = 2 | Source that generates a touchscreen multi-touch event. |
| SOURCE\_TYPE\_TOUCHPAD = 3 | Source that generates a touchpad multi-touch event. |

#### \[h2\]Input\_KeyboardType

enum Input\_KeyboardType

**Description**

Provides the enum values of keyboard types of the input device.

**Since**: 13

| Enum | Description |
| :-- | :-- |
| KEYBOARD\_TYPE\_NONE = 0 | Keyboard without keys. |
| KEYBOARD\_TYPE\_UNKNOWN = 1 | Keyboard with unknown keys. |
| KEYBOARD\_TYPE\_ALPHABETIC = 2 | Full keyboard. |
| KEYBOARD\_TYPE\_DIGITAL = 3 | Numeric keypad. |
| KEYBOARD\_TYPE\_STYLUS = 4 | Stylus. |
| KEYBOARD\_TYPE\_REMOTE\_CONTROL = 5 | Remote control. |

#### \[h2\]Input\_Result

enum Input\_Result

**Description**

Provides return value enumerations.

**Since**: 12

| Enum | Description |
| :-- | :-- |
| INPUT\_SUCCESS = 0 | Operation succeeded. |
| INPUT\_PERMISSION\_DENIED = 201 | Permission verification failed. |
| INPUT\_NOT\_SYSTEM\_APPLICATION = 202 | Non-system application. |
| INPUT\_PARAMETER\_ERROR = 401 | Parameter check fails. |
| INPUT\_DEVICE\_NOT\_SUPPORTED = 801 | Function not supported. |
| INPUT\_SERVICE\_EXCEPTION = 3800001 | Service error. |
| INPUT\_REPEAT\_INTERCEPTOR = 4200001 | Interceptor repeatedly created. |
| INPUT\_OCCUPIED\_BY\_SYSTEM = 4200002 | 
Input device occupied by a system application.

**Since**: 14

 |
| INPUT\_OCCUPIED\_BY\_OTHER = 4200003 | 

Input device occupied by another application.

**Since**: 14

 |
| INPUT\_KEYBOARD\_DEVICE\_NOT\_EXIST = 3900002 | 

Keyboard not connected.

**Since**: 15

 |
| INPUT\_INJECTION\_AUTHORIZING = 3900005 | 

Authorization in progress.

**Since**: 20

 |
| INPUT\_INJECTION\_OPERATION\_FREQUENT = 3900006 | 

Repeated request.

**Since**: 20

 |
| INPUT\_INJECTION\_AUTHORIZED = 3900007 | 

Permission granted to the current application.

**Since**: 20

 |
| INPUT\_INJECTION\_AUTHORIZED\_OTHERS = 3900008 | 

Permission granted to other applications.

**Since**: 20

 |
| INPUT\_APP\_NOT\_FOCUSED = 3900009 | 

Application not in focus.

**Since**: 20

 |
| INPUT\_DEVICE\_NO\_POINTER = 3900010 | 

No mouse device.

**Since**: 20

 |
| INPUT\_INVALID\_WINDOWID = 26500001 | 

Invalid window ID.

**Since**: 22

 |

#### Function Description

#### \[h2\]Input\_HotkeyCallback()

typedef void (\*Input\_HotkeyCallback)(Input\_Hotkey\* hotkey)

**Description**

Defines the callback used to return hotkey events.

**Since**: 14

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [Input\_Hotkey](../../structs/input-hotkey/document.md)\* hotkey | Hotkey object. |

#### \[h2\]Input\_KeyEventCallback()

typedef void (\*Input\_KeyEventCallback)(const Input\_KeyEvent\* keyEvent)

**Description**

Defines a lifecycle callback for **keyEvent**. If the callback is triggered, **keyEvent** will be destroyed.

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| const [Input\_KeyEvent](../../structs/input-keyevent/document.md)\* keyEvent | 
**KeyEvent** object, which can be created through [OH\_Input\_CreateKeyEvent](#oh_input_createkeyevent).

If the key event object is no longer needed, destroy it by calling [OH\_Input\_DestroyKeyEvent](#oh_input_destroykeyevent).

 |

#### \[h2\]Input\_MouseEventCallback()

typedef void (\*Input\_MouseEventCallback)(const Input\_MouseEvent\* mouseEvent)

**Description**

Defines a lifecycle callback for **mouseEvent**. If the callback is triggered, **mouseEvent** will be destroyed.

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| const [Input\_MouseEvent](../../structs/input-mouseevent/document.md)\* mouseEvent | 
Mouse event object. You can call [OH\_Input\_CreateMouseEvent](#oh_input_createmouseevent) to create a mouse event object.

If the mouse event object is no longer needed, destroy it by calling [OH\_Input\_DestroyMouseEvent](#oh_input_destroymouseevent).

 |

#### \[h2\]Input\_TouchEventCallback()

typedef void (\*Input\_TouchEventCallback)(const Input\_TouchEvent\* touchEvent)

**Description**

Defines the lifecycle callback for **TouchEvent**. If the callback is triggered, **TouchEvent** will be destroyed.

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| const [Input\_TouchEvent](../../structs/input-touchevent/document.md)\* touchEvent | 
**TouchEvent** object, which can be created through [OH\_Input\_CreateTouchEvent](#oh_input_createtouchevent).

If the **TouchEvent** object is no longer needed, destroy it by calling [OH\_Input\_DestroyTouchEvent](#oh_input_destroytouchevent).

 |

#### \[h2\]Input\_AxisEventCallback()

typedef void (\*Input\_AxisEventCallback)(const Input\_AxisEvent\* axisEvent)

**Description**

Defines a lifecycle callback for **axisEvent**. If the callback is triggered, **axisEvent** will be destroyed.

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| const [Input\_AxisEvent](../../structs/input-axisevent/document.md)\* axisEvent | 
Axis event object. You can call [OH\_Input\_CreateAxisEvent](#oh_input_createaxisevent) to create an axis event object.

If the axis event object is no longer needed, destroy it by calling [OH\_Input\_DestroyAxisEvent](#oh_input_destroyaxisevent).

 |

#### \[h2\]Input\_DeviceAddedCallback()

typedef void (\*Input\_DeviceAddedCallback)(int32\_t deviceId)

**Description**

Defines a callback used to receive device insertion events.

**Since**: 13

**Parameters**

| Parameter | Description |
| :-- | :-- |
| int32\_t deviceId | Unique ID of the input device. If a physical device is repeatedly reinstalled or restarted, its ID may change. |

#### \[h2\]Input\_DeviceRemovedCallback()

typedef void (\*Input\_DeviceRemovedCallback)(int32\_t deviceId)

**Description**

Defines a callback used to receive device removal events.

**Since**: 13

**Parameters**

| Parameter | Description |
| :-- | :-- |
| int32\_t deviceId | Unique ID of the input device. If a physical device is repeatedly reinstalled or restarted, its ID may change. |

#### \[h2\]Input\_InjectAuthorizeCallback()

typedef void (\*Input\_InjectAuthorizeCallback)(Input\_InjectionStatus authorizedStatus)

**Description**

Defines a callback used to receive the injection permission authorization status.

**Since**: 20

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [Input\_InjectionStatus](#input_injectionstatus) authorizedStatus | Injection permission authorization status. |

#### \[h2\]OH\_Input\_GetKeyState()

Input\_Result OH\_Input\_GetKeyState(struct Input\_KeyState\* keyState)

**Description**

Queries a key status enum object.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| struct [Input\_KeyState](../../structs/input-keystate/document.md)\* keyState | Key status enum object. For details, see [Input\_KeyStateAction](#input_keystateaction). |

**Return value**

| Type | Description |
| :-- | :-- |
| [Input\_Result](#input_result) | 
[INPUT\_SUCCESS](#input_result) if the operation is successful;

an error code defined in [Input\_Result](#input_result) otherwise.

 |

#### \[h2\]OH\_Input\_CreateKeyState()

struct Input\_KeyState\* OH\_Input\_CreateKeyState()

**Description**

Creates a key status enum object. You can call [OH\_Input\_DestroyKeyState](#oh_input_destroykeystate) to destroy a key status enum object.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Since**: 12

**Return value**

| Type | Description |
| :-- | :-- |
| struct | [Input\_KeyState](../../structs/input-keystate/document.md) pointer object if the operation is successful; a null pointer otherwise. |

#### \[h2\]OH\_Input\_DestroyKeyState()

void OH\_Input\_DestroyKeyState(struct Input\_KeyState\*\* keyState)

**Description**

Destroys a key status enum object.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| struct [Input\_KeyState](../../structs/input-keystate/document.md)\*\* keyState | Key status enum object. For details, see [Input\_KeyStateAction](#input_keystateaction). |

#### \[h2\]OH\_Input\_SetKeyCode()

void OH\_Input\_SetKeyCode(struct Input\_KeyState\* keyState, int32\_t keyCode)

**Description**

Sets the key value of a key status enum object.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| struct [Input\_KeyState](../../structs/input-keystate/document.md)\* keyState | Key status enum object. For details, see [Input\_KeyStateAction](#input_keystateaction). |
| int32\_t keyCode | Key code. |

#### \[h2\]OH\_Input\_GetKeyCode()

int32\_t OH\_Input\_GetKeyCode(const struct Input\_KeyState\* keyState)

**Description**

Obtains the key value of a key status enum object.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| const struct [Input\_KeyState](../../structs/input-keystate/document.md)\* keyState | Key status enum object. For details, see [Input\_KeyStateAction](#input_keystateaction). |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | Key value of the key status enum object. For details, see [Input\_KeyStateAction](#input_keystateaction). |

#### \[h2\]OH\_Input\_SetKeyPressed()

void OH\_Input\_SetKeyPressed(struct Input\_KeyState\* keyState, int32\_t keyAction)

**Description**

Sets whether the key specific to a key status enum object is pressed.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| struct [Input\_KeyState](../../structs/input-keystate/document.md)\* keyState | Key status enum object. For details, see [Input\_KeyStateAction](#input_keystateaction). |
| int32\_t keyAction | Whether a key is pressed. For details, see [Input\_KeyEventAction](#input_keyeventaction). |

#### \[h2\]OH\_Input\_GetKeyPressed()

int32\_t OH\_Input\_GetKeyPressed(const struct Input\_KeyState\* keyState)

**Description**

Checks whether the key specific to a key status enum object is pressed.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| const struct [Input\_KeyState](../../structs/input-keystate/document.md)\* keyState | Key status enum object. For details, see [Input\_KeyStateAction](#input_keystateaction). |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | Key pressing status of the key status enum object. For details, see [Input\_KeyStateAction](#input_keystateaction). |

#### \[h2\]OH\_Input\_SetKeySwitch()

void OH\_Input\_SetKeySwitch(struct Input\_KeyState\* keyState, int32\_t keySwitch)

**Description**

Sets the key switch of the key status enum object.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| struct [Input\_KeyState](../../structs/input-keystate/document.md)\* keyState | Key status enum object. For details, see [Input\_KeyStateAction](#input_keystateaction). |
| int32\_t keySwitch | Key switch. |

#### \[h2\]OH\_Input\_GetKeySwitch()

int32\_t OH\_Input\_GetKeySwitch(const struct Input\_KeyState\* keyState)

**Description**

Obtains the key switch of the key status enum object.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| const struct [Input\_KeyState](../../structs/input-keystate/document.md)\* keyState | Key status enum object. For details, see [Input\_KeyStateAction](#input_keystateaction). |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | Key switch of the key status enum object. For details, see [Input\_KeyStateAction](#input_keystateaction). |

#### \[h2\]OH\_Input\_InjectKeyEvent()

int32\_t OH\_Input\_InjectKeyEvent(const struct Input\_KeyEvent\* keyEvent)

**Description**

Injects a key event.

This API does not take effect if the event injection permission is not granted.

Since API version 20, you are advised to use [OH\_Input\_RequestInjection](#oh_input_requestinjection) to request the required permission before calling this API. If the status returned by [OH\_Input\_QueryAuthorizedStatus](#oh_input_queryauthorizedstatus) is [AUTHORIZED](#input_injectionstatus), then you can call this API.

Since API version 22, if the key press event (**KEY\_ACTION\_DOWN**) of a modifier key (**KEYCODE\_META\_LEFT**, **KEYCODE\_META\_RIGHT**, **KEYCODE\_CTRL\_LEFT**, **KEYCODE\_CTRL\_RIGHT**, **KEYCODE\_ALT\_LEFT**, **KEYCODE\_ALT\_RIGHT**, **KEYCODE\_SHIFT\_LEFT**, **KEYCODE\_SHIFT\_RIGHT**, **KEYCODE\_CAPS\_LOCK**, **KEYCODE\_SCROLL\_LOCK**, or **KEYCODE\_NUM\_LOCK**) is injected, the release event (**KEY\_ACTION\_UP**) of the key needs to be injected in a timely manner to avoid the key being pressed for a long time.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| const struct [Input\_KeyEvent](../../structs/input-keyevent/document.md)\* keyEvent | 
**KeyEvent** object, which can be created through [OH\_Input\_CreateKeyEvent](#oh_input_createkeyevent). You can call [OH\_Input\_SetKeyEventKeyCode](#oh_input_setkeyeventkeycode) and [OH\_Input\_SetKeyEventAction](#oh_input_setkeyeventaction) to set the key value and key event type of the key event object.

If the key event object is no longer needed, destroy it by calling [OH\_Input\_DestroyKeyEvent](#oh_input_destroykeyevent).

 |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Return value of the **OH\_Input\_InjectKeyEvent** function.

\- [INPUT\_SUCCESS](#input_result) if the operation is successful;

\- [INPUT\_PERMISSION\_DENIED](#input_result) if the required permission is missing;

\- [INPUT\_PARAMETER\_ERROR](#input_result) if the input parameter is incorrect.

 |

#### \[h2\]OH\_Input\_CreateKeyEvent()

struct Input\_KeyEvent\* OH\_Input\_CreateKeyEvent()

**Description**

Creates a key event object. You can call [OH\_Input\_DestroyKeyEvent](#oh_input_destroykeyevent) to destroy a key event object.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Since**: 12

**Return value**

| Type | Description |
| :-- | :-- |
| struct | [Input\_KeyEvent](../../structs/input-keyevent/document.md) pointer object if the operation is successful; a null pointer otherwise. |

#### \[h2\]OH\_Input\_DestroyKeyEvent()

void OH\_Input\_DestroyKeyEvent(struct Input\_KeyEvent\*\* keyEvent)

**Description**

Destroys a key event object.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| struct [Input\_KeyEvent](../../structs/input-keyevent/document.md)\*\* keyEvent | Key event object. |

#### \[h2\]OH\_Input\_SetKeyEventAction()

void OH\_Input\_SetKeyEventAction(struct Input\_KeyEvent\* keyEvent, int32\_t action)

**Description**

Sets the key event type.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| struct [Input\_KeyEvent](../../structs/input-keyevent/document.md)\* keyEvent | 
**KeyEvent** object, which can be created through [OH\_Input\_CreateKeyEvent](#oh_input_createkeyevent).

If the key event object is no longer needed, destroy it by calling [OH\_Input\_DestroyKeyEvent](#oh_input_destroykeyevent).

 |
| int32\_t action | Key event type. For details, see [Input\_KeyEventAction](#input_keyeventaction). |

#### \[h2\]OH\_Input\_GetKeyEventAction()

int32\_t OH\_Input\_GetKeyEventAction(const struct Input\_KeyEvent\* keyEvent)

**Description**

Obtains the key event action.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| const struct [Input\_KeyEvent](../../structs/input-keyevent/document.md)\* keyEvent | 
**KeyEvent** object, which can be created through [OH\_Input\_CreateKeyEvent](#oh_input_createkeyevent).

If the key event object is no longer needed, destroy it by calling [OH\_Input\_DestroyKeyEvent](#oh_input_destroykeyevent).

 |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | Key event type. For details, see [Input\_KeyEventAction](#input_keyeventaction). |

#### \[h2\]OH\_Input\_SetKeyEventKeyCode()

void OH\_Input\_SetKeyEventKeyCode(struct Input\_KeyEvent\* keyEvent, int32\_t keyCode)

**Description**

Sets the key code value for a key event.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| struct [Input\_KeyEvent](../../structs/input-keyevent/document.md)\* keyEvent | 
**KeyEvent** object, which can be created through [OH\_Input\_CreateKeyEvent](#oh_input_createkeyevent).

If the key event object is no longer needed, destroy it by calling [OH\_Input\_DestroyKeyEvent](#oh_input_destroykeyevent).

 |
| int32\_t keyCode | Key value. |

#### \[h2\]OH\_Input\_GetKeyEventKeyCode()

int32\_t OH\_Input\_GetKeyEventKeyCode(const struct Input\_KeyEvent\* keyEvent)

**Description**

Obtains the key code value of a key event.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| const struct [Input\_KeyEvent](../../structs/input-keyevent/document.md)\* keyEvent | 
**KeyEvent** object, which can be created through [OH\_Input\_CreateKeyEvent](#oh_input_createkeyevent).

If the key event object is no longer needed, destroy it by calling [OH\_Input\_DestroyKeyEvent](#oh_input_destroykeyevent).

 |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | Key code of a key event. For details, see [Input\_KeyCode](../oh-key-code-h/document.md#input_keycode). |

#### \[h2\]OH\_Input\_SetKeyEventActionTime()

void OH\_Input\_SetKeyEventActionTime(struct Input\_KeyEvent\* keyEvent, int64\_t actionTime)

**Description**

Sets the time when a key event occurs.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| struct [Input\_KeyEvent](../../structs/input-keyevent/document.md)\* keyEvent | 
**KeyEvent** object, which can be created through [OH\_Input\_CreateKeyEvent](#oh_input_createkeyevent).

If the key event object is no longer needed, destroy it by calling [OH\_Input\_DestroyKeyEvent](#oh_input_destroykeyevent).

 |
| int64\_t actionTime | Time when a key event occurs, in microseconds since the system starts. |

#### \[h2\]OH\_Input\_GetKeyEventActionTime()

int64\_t OH\_Input\_GetKeyEventActionTime(const struct Input\_KeyEvent\* keyEvent)

**Description**

Obtains the time when a key event occurs.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| const struct [Input\_KeyEvent](../../structs/input-keyevent/document.md)\* keyEvent | 
**KeyEvent** object, which can be created through [OH\_Input\_CreateKeyEvent](#oh_input_createkeyevent).

If the key event object is no longer needed, destroy it by calling [OH\_Input\_DestroyKeyEvent](#oh_input_destroykeyevent).

 |

**Return value**

| Type | Description |
| :-- | :-- |
| int64\_t | Time when a key event occurs. |

#### \[h2\]OH\_Input\_SetKeyEventWindowId()

void OH\_Input\_SetKeyEventWindowId(struct Input\_KeyEvent\* keyEvent, int32\_t windowId)

**Description**

Sets the window ID of a key event.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Since**: 15

**Parameters**

| Parameter | Description |
| :-- | :-- |
| struct [Input\_KeyEvent](../../structs/input-keyevent/document.md)\* keyEvent | 
**KeyEvent** object, which can be created through [OH\_Input\_CreateKeyEvent](#oh_input_createkeyevent).

If the key event object is no longer needed, destroy it by calling [OH\_Input\_DestroyKeyEvent](#oh_input_destroykeyevent).

 |
| int32\_t windowId | Window ID of the key event. |

#### \[h2\]OH\_Input\_GetKeyEventWindowId()

int32\_t OH\_Input\_GetKeyEventWindowId(const struct Input\_KeyEvent\* keyEvent)

**Description**

Obtains the window ID of a key event.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Since**: 15

**Parameters**

| Parameter | Description |
| :-- | :-- |
| const struct [Input\_KeyEvent](../../structs/input-keyevent/document.md)\* keyEvent | 
**KeyEvent** object, which can be created through [OH\_Input\_CreateKeyEvent](#oh_input_createkeyevent).

If the key event object is no longer needed, destroy it by calling [OH\_Input\_DestroyKeyEvent](#oh_input_destroykeyevent).

 |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | Window ID of the key event. |

#### \[h2\]OH\_Input\_GetKeyEventDisplayId()

int32\_t OH\_Input\_GetKeyEventDisplayId(const struct Input\_KeyEvent\* keyEvent)

**Description**

Obtains the screen ID of a key event.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Since**: 15

**Parameters**

| Parameter | Description |
| :-- | :-- |
| const struct [Input\_KeyEvent](../../structs/input-keyevent/document.md)\* keyEvent | 
**KeyEvent** object, which can be created through [OH\_Input\_CreateKeyEvent](#oh_input_createkeyevent).

If the key event object is no longer needed, destroy it by calling [OH\_Input\_DestroyKeyEvent](#oh_input_destroykeyevent).

 |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | Screen ID of the key event. |

#### \[h2\]OH\_Input\_SetKeyEventDisplayId()

void OH\_Input\_SetKeyEventDisplayId(struct Input\_KeyEvent\* keyEvent, int32\_t displayId)

**Description**

Sets the screen ID of a key event.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Since**: 15

**Parameters**

| Parameter | Description |
| :-- | :-- |
| struct [Input\_KeyEvent](../../structs/input-keyevent/document.md)\* keyEvent | 
**KeyEvent** object, which can be created through [OH\_Input\_CreateKeyEvent](#oh_input_createkeyevent).

If the key event object is no longer needed, destroy it by calling [OH\_Input\_DestroyKeyEvent](#oh_input_destroykeyevent).

 |
| int32\_t displayId | Screen ID of the key event. |

#### \[h2\]OH\_Input\_CreateMouseEvent()

struct Input\_MouseEvent\* OH\_Input\_CreateMouseEvent()

**Description**

Creates a mouse event object. You can call [OH\_Input\_DestroyMouseEvent](#oh_input_destroymouseevent) to destroy a mouse event object.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Since**: 12

**Return value**

| Type | Description |
| :-- | :-- |
| struct | [Input\_MouseEvent](../../structs/input-mouseevent/document.md) pointer object if the operation is successful; a null pointer otherwise. |

#### \[h2\]OH\_Input\_DestroyMouseEvent()

void OH\_Input\_DestroyMouseEvent(struct Input\_MouseEvent\*\* mouseEvent)

**Description**

Destroys a mouse event object.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| struct [Input\_MouseEvent](../../structs/input-mouseevent/document.md)\*\* mouseEvent | Mouse event object. |

#### \[h2\]OH\_Input\_SetMouseEventAction()

void OH\_Input\_SetMouseEventAction(struct Input\_MouseEvent\* mouseEvent, int32\_t action)

**Description**

Sets the action for a mouse event.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| struct [Input\_MouseEvent](../../structs/input-mouseevent/document.md)\* mouseEvent | 
Mouse event object. You can call [OH\_Input\_CreateMouseEvent](#oh_input_createmouseevent) to create a mouse event object.

If the mouse event object is no longer needed, destroy it by calling [OH\_Input\_DestroyMouseEvent](#oh_input_destroymouseevent).

 |
| int32\_t action | Mouse action. For details, see [Input\_MouseEventAction](#input_mouseeventaction). |

#### \[h2\]OH\_Input\_GetMouseEventAction()

int32\_t OH\_Input\_GetMouseEventAction(const struct Input\_MouseEvent\* mouseEvent)

**Description**

Obtains the action of a mouse event.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| const struct [Input\_MouseEvent](../../structs/input-mouseevent/document.md)\* mouseEvent | 
Mouse event object. You can call [OH\_Input\_CreateMouseEvent](#oh_input_createmouseevent) to create a mouse event object.

If the mouse event object is no longer needed, destroy it by calling [OH\_Input\_DestroyMouseEvent](#oh_input_destroymouseevent).

 |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | Mouse action. For details, see [Input\_MouseEventAction](#input_mouseeventaction). |

#### \[h2\]OH\_Input\_SetMouseEventDisplayX()

void OH\_Input\_SetMouseEventDisplayX(struct Input\_MouseEvent\* mouseEvent, int32\_t displayX)

**Description**

Sets the X coordinate of the mouse event in the relative coordinate system with the upper-left corner of the specified screen as the origin.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| struct [Input\_MouseEvent](../../structs/input-mouseevent/document.md)\* mouseEvent | 
Mouse event object. You can call [OH\_Input\_CreateMouseEvent](#oh_input_createmouseevent) to create a mouse event object.

If the mouse event object is no longer needed, destroy it by calling [OH\_Input\_DestroyMouseEvent](#oh_input_destroymouseevent).

 |
| int32\_t displayX | X coordinate of the mouse event in the relative coordinate system with the upper-left corner of the specified screen as the origin. |

#### \[h2\]OH\_Input\_GetMouseEventDisplayX()

int32\_t OH\_Input\_GetMouseEventDisplayX(const struct Input\_MouseEvent\* mouseEvent)

**Description**

Obtains the X coordinate of the mouse event in the relative coordinate system with the upper-left corner of the specified screen as the origin.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| const struct [Input\_MouseEvent](../../structs/input-mouseevent/document.md)\* mouseEvent | 
Mouse event object. You can call [OH\_Input\_CreateMouseEvent](#oh_input_createmouseevent) to create a mouse event object.

If the mouse event object is no longer needed, destroy it by calling [OH\_Input\_DestroyMouseEvent](#oh_input_destroymouseevent).

 |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | X coordinate of the mouse event in the relative coordinate system with the upper-left corner of the specified screen as the origin. |

#### \[h2\]OH\_Input\_SetMouseEventDisplayY()

void OH\_Input\_SetMouseEventDisplayY(struct Input\_MouseEvent\* mouseEvent, int32\_t displayY)

**Description**

Sets the Y coordinate of the mouse event in the relative coordinate system with the upper-left corner of the specified screen as the origin.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| struct [Input\_MouseEvent](../../structs/input-mouseevent/document.md)\* mouseEvent | 
Mouse event object. You can call [OH\_Input\_CreateMouseEvent](#oh_input_createmouseevent) to create a mouse event object.

If the mouse event object is no longer needed, destroy it by calling [OH\_Input\_DestroyMouseEvent](#oh_input_destroymouseevent).

 |
| int32\_t displayY | Y coordinate of the mouse event in the relative coordinate system with the upper-left corner of the specified screen as the origin. |

#### \[h2\]OH\_Input\_GetMouseEventDisplayY()

int32\_t OH\_Input\_GetMouseEventDisplayY(const struct Input\_MouseEvent\* mouseEvent)

**Description**

Obtains the Y coordinate of the mouse event in the relative coordinate system with the upper-left corner of the specified screen as the origin.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| const struct [Input\_MouseEvent](../../structs/input-mouseevent/document.md)\* mouseEvent | 
Mouse event object. You can call [OH\_Input\_CreateMouseEvent](#oh_input_createmouseevent) to create a mouse event object.

If the mouse event object is no longer needed, destroy it by calling [OH\_Input\_DestroyMouseEvent](#oh_input_destroymouseevent).

 |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | Y coordinate of the mouse event in the relative coordinate system with the upper-left corner of the specified screen as the origin. |

#### \[h2\]OH\_Input\_SetMouseEventButton()

void OH\_Input\_SetMouseEventButton(struct Input\_MouseEvent\* mouseEvent, int32\_t button)

**Description**

Sets the button for a mouse event.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| struct [Input\_MouseEvent](../../structs/input-mouseevent/document.md)\* mouseEvent | 
Mouse event object. You can call [OH\_Input\_CreateMouseEvent](#oh_input_createmouseevent) to create a mouse event object.

If the mouse event object is no longer needed, destroy it by calling [OH\_Input\_DestroyMouseEvent](#oh_input_destroymouseevent).

 |
| int32\_t button | Mouse button. For details, see [Input\_MouseEventButton](#input_mouseeventbutton). |

#### \[h2\]OH\_Input\_GetMouseEventButton()

int32\_t OH\_Input\_GetMouseEventButton(const struct Input\_MouseEvent\* mouseEvent)

**Description**

Obtains the button of a mouse event.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| const struct [Input\_MouseEvent](../../structs/input-mouseevent/document.md)\* mouseEvent | 
Mouse event object. You can call [OH\_Input\_CreateMouseEvent](#oh_input_createmouseevent) to create a mouse event object.

If the mouse event object is no longer needed, destroy it by calling [OH\_Input\_DestroyMouseEvent](#oh_input_destroymouseevent).

 |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | Mouse button. For details, see [Input\_MouseEventButton](#input_mouseeventbutton). |

#### \[h2\]OH\_Input\_SetMouseEventAxisType()

void OH\_Input\_SetMouseEventAxisType(struct Input\_MouseEvent\* mouseEvent, int32\_t axisType)

**Description**

Sets the axis type for a mouse event.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| struct [Input\_MouseEvent](../../structs/input-mouseevent/document.md)\* mouseEvent | 
Mouse event object. You can call [OH\_Input\_CreateMouseEvent](#oh_input_createmouseevent) to create a mouse event object.

If the mouse event object is no longer needed, destroy it by calling [OH\_Input\_DestroyMouseEvent](#oh_input_destroymouseevent).

 |
| int32\_t axisType | Mouse axis type, such as vertical axis and horizontal axis. For details, see [InputEvent\_MouseAxis](#inputevent_mouseaxis). |

#### \[h2\]OH\_Input\_GetMouseEventAxisType()

int32\_t OH\_Input\_GetMouseEventAxisType(const struct Input\_MouseEvent\* mouseEvent)

**Description**

Obtains the axis type of a mouse event.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| const struct [Input\_MouseEvent](../../structs/input-mouseevent/document.md)\* mouseEvent | 
Mouse event object. You can call [OH\_Input\_CreateMouseEvent](#oh_input_createmouseevent) to create a mouse event object.

If the mouse event object is no longer needed, destroy it by calling [OH\_Input\_DestroyMouseEvent](#oh_input_destroymouseevent).

 |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | Enumerates mouse axis types. For details, see [InputEvent\_MouseAxis](#inputevent_mouseaxis). |

#### \[h2\]OH\_Input\_SetMouseEventAxisValue()

void OH\_Input\_SetMouseEventAxisValue(struct Input\_MouseEvent\* mouseEvent, float axisValue)

**Description**

Sets the axis value for a mouse axis event.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| struct [Input\_MouseEvent](../../structs/input-mouseevent/document.md)\* mouseEvent | 
Mouse event object. You can call [OH\_Input\_CreateMouseEvent](#oh_input_createmouseevent) to create a mouse event object.

If the mouse event object is no longer needed, destroy it by calling [OH\_Input\_DestroyMouseEvent](#oh_input_destroymouseevent).

 |
| float axisValue | Axis event value. A positive number means scrolling forward (for example, 1.0 equals one unit forward), and a negative number means scrolling backward (for example, -1.0 equals one unit backward). |

#### \[h2\]OH\_Input\_GetMouseEventAxisValue()

float OH\_Input\_GetMouseEventAxisValue(const struct Input\_MouseEvent\* mouseEvent)

**Description**

Obtains the axis value of a mouse axis event.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| const struct [Input\_MouseEvent](../../structs/input-mouseevent/document.md)\* mouseEvent | 
Mouse event object. You can call [OH\_Input\_CreateMouseEvent](#oh_input_createmouseevent) to create a mouse event object.

If the mouse event object is no longer needed, destroy it by calling [OH\_Input\_DestroyMouseEvent](#oh_input_destroymouseevent).

 |

**Return value**

| Type | Description |
| :-- | :-- |
| float | Axis event value. |

#### \[h2\]OH\_Input\_SetMouseEventActionTime()

void OH\_Input\_SetMouseEventActionTime(struct Input\_MouseEvent\* mouseEvent, int64\_t actionTime)

**Description**

Sets the time when a mouse event occurs.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| struct [Input\_MouseEvent](../../structs/input-mouseevent/document.md)\* mouseEvent | 
Mouse event object. You can call [OH\_Input\_CreateMouseEvent](#oh_input_createmouseevent) to create a mouse event object.

If the mouse event object is no longer needed, destroy it by calling [OH\_Input\_DestroyMouseEvent](#oh_input_destroymouseevent).

 |
| int64\_t actionTime | Time when a mouse event occurs, in microseconds since the system starts. |

#### \[h2\]OH\_Input\_GetMouseEventActionTime()

int64\_t OH\_Input\_GetMouseEventActionTime(const struct Input\_MouseEvent\* mouseEvent)

**Description**

Obtains the time when a mouse event occurs.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| mouseEvent | 
Mouse event object. You can call [OH\_Input\_CreateMouseEvent](#oh_input_createmouseevent) to create a mouse event object.

If the mouse event object is no longer needed, destroy it by calling [OH\_Input\_DestroyMouseEvent](#oh_input_destroymouseevent).

 |

**Return value**

| Type | Description |
| :-- | :-- |
| int64\_t | Time when the mouse event occurs. |

#### \[h2\]OH\_Input\_SetMouseEventWindowId()

void OH\_Input\_SetMouseEventWindowId(struct Input\_MouseEvent\* mouseEvent, int32\_t windowId)

**Description**

Sets the window ID of a mouse event.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Since**: 15

**Parameters**

| Parameter | Description |
| :-- | :-- |
| struct [Input\_MouseEvent](../../structs/input-mouseevent/document.md)\* mouseEvent | 
Mouse event object. You can call [OH\_Input\_CreateMouseEvent](#oh_input_createmouseevent) to create a mouse event object.

If the mouse event object is no longer needed, destroy it by calling [OH\_Input\_DestroyMouseEvent](#oh_input_destroymouseevent).

 |
| int32\_t windowId | Window ID of the mouse event. |

#### \[h2\]OH\_Input\_GetMouseEventWindowId()

int32\_t OH\_Input\_GetMouseEventWindowId(const struct Input\_MouseEvent\* mouseEvent)

**Description**

Obtains the window ID of a mouse event.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Since**: 15

**Parameters**

| Parameter | Description |
| :-- | :-- |
| const struct [Input\_MouseEvent](../../structs/input-mouseevent/document.md)\* mouseEvent | 
Mouse event object. You can call [OH\_Input\_CreateMouseEvent](#oh_input_createmouseevent) to create a mouse event object.

If the mouse event object is no longer needed, destroy it by calling [OH\_Input\_DestroyMouseEvent](#oh_input_destroymouseevent).

 |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | Window ID of the mouse event. |

#### \[h2\]OH\_Input\_SetMouseEventDisplayId()

void OH\_Input\_SetMouseEventDisplayId(struct Input\_MouseEvent\* mouseEvent, int32\_t displayId)

**Description**

Sets the screen ID of a mouse event.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Since**: 15

**Parameters**

| Parameter | Description |
| :-- | :-- |
| struct [Input\_MouseEvent](../../structs/input-mouseevent/document.md)\* mouseEvent | 
Mouse event object. You can call [OH\_Input\_CreateMouseEvent](#oh_input_createmouseevent) to create a mouse event object.

If the mouse event object is no longer needed, destroy it by calling [OH\_Input\_DestroyMouseEvent](#oh_input_destroymouseevent).

 |
| int32\_t displayId | Screen ID of the mouse event. |

#### \[h2\]OH\_Input\_CreateTouchEvent()

struct Input\_TouchEvent\* OH\_Input\_CreateTouchEvent()

**Description**

Creates a **TouchEvent** object. You can call [OH\_Input\_DestroyTouchEvent](#oh_input_destroytouchevent) to destroy a touch event object.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Since**: 12

**Return value**

| Type | Description |
| :-- | :-- |
| struct | [Input\_TouchEvent](../../structs/input-touchevent/document.md) pointer object if the operation is successful; a null pointer otherwise. |

#### \[h2\]OH\_Input\_DestroyTouchEvent()

void OH\_Input\_DestroyTouchEvent(struct Input\_TouchEvent\*\* touchEvent)

**Description**

Destroys a **TouchEvent** object.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| struct [Input\_TouchEvent](../../structs/input-touchevent/document.md)\*\* touchEvent | **TouchEvent** object. |

#### \[h2\]OH\_Input\_SetTouchEventAction()

void OH\_Input\_SetTouchEventAction(struct Input\_TouchEvent\* touchEvent, int32\_t action)

**Description**

Sets the action of a touch event.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| struct [Input\_TouchEvent](../../structs/input-touchevent/document.md)\* touchEvent | 
**TouchEvent** object, which can be created through [OH\_Input\_CreateTouchEvent](#oh_input_createtouchevent).

If the **TouchEvent** object is no longer needed, destroy it by calling [OH\_Input\_DestroyTouchEvent](#oh_input_destroytouchevent).

 |
| int32\_t action | Action of the touch event. For details, see [Input\_TouchEventAction](#input_toucheventaction). |

#### \[h2\]OH\_Input\_GetTouchEventAction()

int32\_t OH\_Input\_GetTouchEventAction(const struct Input\_TouchEvent\* touchEvent)

**Description**

Obtains the action of a touch event.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| const struct [Input\_TouchEvent](../../structs/input-touchevent/document.md)\* touchEvent | 
**TouchEvent** object, which can be created through [OH\_Input\_CreateTouchEvent](#oh_input_createtouchevent).

If the **TouchEvent** object is no longer needed, destroy it by calling [OH\_Input\_DestroyTouchEvent](#oh_input_destroytouchevent).

 |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | Action of the touch event. For details, see [Input\_TouchEventAction](#input_toucheventaction). |

#### \[h2\]OH\_Input\_SetTouchEventFingerId()

void OH\_Input\_SetTouchEventFingerId(struct Input\_TouchEvent\* touchEvent, int32\_t id)

**Description**

Sets the finger ID of a touch event.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| struct [Input\_TouchEvent](../../structs/input-touchevent/document.md)\* touchEvent | 
**TouchEvent** object, which can be created through [OH\_Input\_CreateTouchEvent](#oh_input_createtouchevent).

If the **TouchEvent** object is no longer needed, destroy it by calling [OH\_Input\_DestroyTouchEvent](#oh_input_destroytouchevent).

 |
| int32\_t id | Finger ID of a touch event. The ID of the first finger touching the screen is 0, the second is 1, and so on incrementally. |

#### \[h2\]OH\_Input\_GetTouchEventFingerId()

int32\_t OH\_Input\_GetTouchEventFingerId(const struct Input\_TouchEvent\* touchEvent)

**Description**

Obtains the finger ID of a touch event.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| const struct [Input\_TouchEvent](../../structs/input-touchevent/document.md)\* touchEvent | 
**TouchEvent** object, which can be created through [OH\_Input\_CreateTouchEvent](#oh_input_createtouchevent).

If the **TouchEvent** object is no longer needed, destroy it by calling [OH\_Input\_DestroyTouchEvent](#oh_input_destroytouchevent).

 |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | Finger ID of a touch event. The ID of the first finger touching the screen is 0, the second is 1, and so on incrementally. |

#### \[h2\]OH\_Input\_SetTouchEventDisplayX()

void OH\_Input\_SetTouchEventDisplayX(struct Input\_TouchEvent\* touchEvent, int32\_t displayX)

**Description**

Sets the X coordinate of the touch event in the relative coordinate system with the upper-left corner of the specified screen as the origin.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| struct [Input\_TouchEvent](../../structs/input-touchevent/document.md)\* touchEvent | 
**TouchEvent** object, which can be created through [OH\_Input\_CreateTouchEvent](#oh_input_createtouchevent).

If the **TouchEvent** object is no longer needed, destroy it by calling [OH\_Input\_DestroyTouchEvent](#oh_input_destroytouchevent).

 |
| int32\_t displayX | X coordinate of the touch event in the relative coordinate system with the upper-left corner of the specified screen as the origin. |

#### \[h2\]OH\_Input\_GetTouchEventDisplayX()

int32\_t OH\_Input\_GetTouchEventDisplayX(const struct Input\_TouchEvent\* touchEvent)

**Description**

Obtains the X coordinate of the touch event in the relative coordinate system with the upper-left corner of the specified screen as the origin.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| const struct [Input\_TouchEvent](../../structs/input-touchevent/document.md)\* touchEvent | 
**TouchEvent** object, which can be created through [OH\_Input\_CreateTouchEvent](#oh_input_createtouchevent).

If the **TouchEvent** object is no longer needed, destroy it by calling [OH\_Input\_DestroyTouchEvent](#oh_input_destroytouchevent).

 |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | X coordinate of the touch event in the relative coordinate system with the upper-left corner of the specified screen as the origin. |

#### \[h2\]OH\_Input\_SetTouchEventDisplayY()

void OH\_Input\_SetTouchEventDisplayY(struct Input\_TouchEvent\* touchEvent, int32\_t displayY)

**Description**

Sets the Y coordinate of the touch event in the relative coordinate system with the upper-left corner of the specified screen as the origin.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| struct [Input\_TouchEvent](../../structs/input-touchevent/document.md)\* touchEvent | 
**TouchEvent** object, which can be created through [OH\_Input\_CreateTouchEvent](#oh_input_createtouchevent).

If the **TouchEvent** object is no longer needed, destroy it by calling [OH\_Input\_DestroyTouchEvent](#oh_input_destroytouchevent).

 |
| int32\_t displayY | Y coordinate of the touch event in the relative coordinate system with the upper-left corner of the specified screen as the origin. |

#### \[h2\]OH\_Input\_GetTouchEventDisplayY()

int32\_t OH\_Input\_GetTouchEventDisplayY(const struct Input\_TouchEvent\* touchEvent)

**Description**

Obtains the Y coordinate of the touch event in the relative coordinate system with the upper-left corner of the specified screen as the origin.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| const struct [Input\_TouchEvent](../../structs/input-touchevent/document.md)\* touchEvent | 
**TouchEvent** object, which can be created through [OH\_Input\_CreateTouchEvent](#oh_input_createtouchevent).

If the **TouchEvent** object is no longer needed, destroy it by calling [OH\_Input\_DestroyTouchEvent](#oh_input_destroytouchevent).

 |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | Y coordinate of the touch event in the relative coordinate system with the upper-left corner of the specified screen as the origin. |

#### \[h2\]OH\_Input\_SetTouchEventActionTime()

void OH\_Input\_SetTouchEventActionTime(struct Input\_TouchEvent\* touchEvent, int64\_t actionTime)

**Description**

Sets the time when the touch event occurs.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| touchEvent | 
**TouchEvent** object, which can be created through [OH\_Input\_CreateTouchEvent](#oh_input_createtouchevent).

If the **TouchEvent** object is no longer needed, destroy it by calling [OH\_Input\_DestroyTouchEvent](#oh_input_destroytouchevent).

 |
| int64\_t actionTime | Time when a touch event occurs, in microseconds since the system starts. |

#### \[h2\]OH\_Input\_GetTouchEventActionTime()

int64\_t OH\_Input\_GetTouchEventActionTime(const struct Input\_TouchEvent\* touchEvent)

**Description**

Obtains the time when the touch event occurs.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| touchEvent | 
**TouchEvent** object, which can be created through [OH\_Input\_CreateTouchEvent](#oh_input_createtouchevent).

If the **TouchEvent** object is no longer needed, destroy it by calling [OH\_Input\_DestroyTouchEvent](#oh_input_destroytouchevent).

 |

**Return value**

| Type | Description |
| :-- | :-- |
| int64\_t | Time when a touch event occurs. |

#### \[h2\]OH\_Input\_SetTouchEventWindowId()

void OH\_Input\_SetTouchEventWindowId(struct Input\_TouchEvent\* touchEvent, int32\_t windowId)

**Description**

Sets the window ID of a touch event.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Since**: 15

**Parameters**

| Parameter | Description |
| :-- | :-- |
| struct [Input\_TouchEvent](../../structs/input-touchevent/document.md)\* touchEvent | 
**TouchEvent** object, which can be created through [OH\_Input\_CreateTouchEvent](#oh_input_createtouchevent).

If the **TouchEvent** object is no longer needed, destroy it by calling [OH\_Input\_DestroyTouchEvent](#oh_input_destroytouchevent).

 |
| int32\_t windowId | Window ID of a touch event. |

#### \[h2\]OH\_Input\_GetTouchEventWindowId()

int32\_t OH\_Input\_GetTouchEventWindowId(const struct Input\_TouchEvent\* touchEvent)

**Description**

Obtains the window ID of a touch event.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Since**: 15

**Parameters**

| Parameter | Description |
| :-- | :-- |
| const struct [Input\_TouchEvent](../../structs/input-touchevent/document.md)\* touchEvent | 
**TouchEvent** object, which can be created through [OH\_Input\_CreateTouchEvent](#oh_input_createtouchevent).

If the **TouchEvent** object is no longer needed, destroy it by calling [OH\_Input\_DestroyTouchEvent](#oh_input_destroytouchevent).

 |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | Window ID of a touch event. |

#### \[h2\]OH\_Input\_SetTouchEventDisplayId()

void OH\_Input\_SetTouchEventDisplayId(struct Input\_TouchEvent\* touchEvent, int32\_t displayId)

**Description**

Sets the screen ID of a touch event.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Since**: 15

**Parameters**

| Parameter | Description |
| :-- | :-- |
| struct [Input\_TouchEvent](../../structs/input-touchevent/document.md)\* touchEvent | 
**TouchEvent** object, which can be created through [OH\_Input\_CreateTouchEvent](#oh_input_createtouchevent).

If the **TouchEvent** object is no longer needed, destroy it by calling [OH\_Input\_DestroyTouchEvent](#oh_input_destroytouchevent).

 |
| int32\_t displayId | Screen ID of a touch event. |

#### \[h2\]OH\_Input\_GetTouchEventDisplayId()

int32\_t OH\_Input\_GetTouchEventDisplayId(const struct Input\_TouchEvent\* touchEvent)

**Description**

Obtains the screen ID of a touch event.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Since**: 15

**Parameters**

| Parameter | Description |
| :-- | :-- |
| const struct [Input\_TouchEvent](../../structs/input-touchevent/document.md)\* touchEvent | 
**TouchEvent** object, which can be created through [OH\_Input\_CreateTouchEvent](#oh_input_createtouchevent).

If the **TouchEvent** object is no longer needed, destroy it by calling [OH\_Input\_DestroyTouchEvent](#oh_input_destroytouchevent).

 |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | Screen ID of a touch event. |

#### \[h2\]OH\_Input\_CancelInjection()

void OH\_Input\_CancelInjection()

**Description**

Stops event injection and revokes authorization.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Since**: 12

#### \[h2\]OH\_Input\_RequestInjection()

Input\_Result OH\_Input\_RequestInjection(Input\_InjectAuthorizeCallback callback)

**Description**

Requests the permission for [OH\_Input\_InjectKeyEvent](#oh_input_injectkeyevent), [OH\_Input\_InjectTouchEvent](#oh_input_injecttouchevent), and [OH\_Input\_InjectMouseEvent](#oh_input_injectmouseevent).

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Device behavior differences**: This API takes effect only on PCs/2-in-1 devices. If this API is called on other devices, error code 801 is returned.

**Since**: 20

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [Input\_InjectAuthorizeCallback](#input_injectauthorizecallback) callback | Callback used to return the permission authorization status. For details, see [Input\_InjectAuthorizeCallback](#input_injectauthorizecallback). |

**Return value**

| Type | Description |
| :-- | :-- |
| [Input\_Result](#input_result) | 
Return value. For details, see [Input\_Result](#input_result).

INPUT\_SUCCESS = 0: Operation success. The application waits for the user authorization result and returns the authorization status through a callback.

INPUT\_PARAMETER\_ERROR = 401: Parameter error. The callback parameter is empty.

INPUT\_DEVICE\_NOT\_SUPPORTED = 801: Function not supported.

INPUT\_SERVICE\_EXCEPTION = 3800001: Service error.

INPUT\_INJECTION\_AUTHORIZING = 3900005: Permission being granted.

INPUT\_INJECTION\_OPERATION\_FREQUENT = 3900006: Repeated request. The application continuously requests permission authorization at an interval of no more than 3 seconds.

INPUT\_INJECTION\_AUTHORIZED = 3900007: Permission granted.

INPUT\_INJECTION\_AUTHORIZED\_OTHERS = 3900008: Permission granted to other applications.

 |

#### \[h2\]OH\_Input\_QueryAuthorizedStatus()

Input\_Result OH\_Input\_QueryAuthorizedStatus(Input\_InjectionStatus\* status)

**Description**

Queries the injection permission authorization status of the current application.

**Since**: 20

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [Input\_InjectionStatus](#input_injectionstatus)\* status | Injection permission authorization status of the current application. See [Input\_InjectionStatus](#input_injectionstatus). |

**Return value**

| Type | Description |
| :-- | :-- |
| [Input\_Result](#input_result) | 
Return value. For details, see [Input\_Result](#input_result).

INPUT\_SUCCESS = 0: Operation success.

INPUT\_PARAMETER\_ERROR = 401: Parameter error. The status parameter is empty.

INPUT\_SERVICE\_EXCEPTION = 3800001: Service error.

 |

#### \[h2\]OH\_Input\_CreateAxisEvent()

Input\_AxisEvent\* OH\_Input\_CreateAxisEvent(void)

**Description**

Creates an axis event object. You can call [OH\_Input\_DestroyAxisEvent](#oh_input_destroyaxisevent) to destroy an axis event object.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Since**: 12

**Return value**

| Type | Description |
| :-- | :-- |
| Input\_AxisEvent\* | [Input\_AxisEvent](../../structs/input-axisevent/document.md) object if the operation is successful; **null** otherwise. |

#### \[h2\]OH\_Input\_DestroyAxisEvent()

Input\_Result OH\_Input\_DestroyAxisEvent(Input\_AxisEvent\*\* axisEvent)

**Description**

Destroys an axis event object.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [Input\_AxisEvent](../../structs/input-axisevent/document.md)\*\* axisEvent | Pointer to the axis event object. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Input\_Result](#input_result) | [INPUT\_SUCCESS](#input_result) if the operation is successful; [INPUT\_PARAMETER\_ERROR](#input_result) if **axisEvent** is null. |

#### \[h2\]OH\_Input\_SetAxisEventAction()

Input\_Result OH\_Input\_SetAxisEventAction(Input\_AxisEvent\* axisEvent, InputEvent\_AxisAction action)

**Description**

Sets the action for an axis event.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [Input\_AxisEvent](../../structs/input-axisevent/document.md)\* axisEvent | 
Axis event object. You can call [OH\_Input\_CreateAxisEvent](#oh_input_createaxisevent) to create an axis event object.

If the axis event object is no longer needed, destroy it by calling [OH\_Input\_DestroyAxisEvent](#oh_input_destroyaxisevent).

 |
| [InputEvent\_AxisAction](../oh-axis-type-h/document.md#inputevent_axisaction) action | Axis event action. For details, see [InputEvent\_AxisAction](../oh-axis-type-h/document.md#inputevent_axisaction). |

**Return value**

| Type | Description |
| :-- | :-- |
| [Input\_Result](#input_result) | [INPUT\_SUCCESS](#input_result) if the operation is successful; [INPUT\_PARAMETER\_ERROR](#input_result) if **axisEvent** is null. |

#### \[h2\]OH\_Input\_GetAxisEventAction()

Input\_Result OH\_Input\_GetAxisEventAction(const Input\_AxisEvent\* axisEvent, InputEvent\_AxisAction \*action)

**Description**

Obtains the action of an axis event.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| const [Input\_AxisEvent](../../structs/input-axisevent/document.md)\* axisEvent | 
Axis event object. You can call [OH\_Input\_CreateAxisEvent](#oh_input_createaxisevent) to create an axis event object.

If the axis event object is no longer needed, destroy it by calling [OH\_Input\_DestroyAxisEvent](#oh_input_destroyaxisevent).

 |
| [InputEvent\_AxisAction](../oh-axis-type-h/document.md#inputevent_axisaction) \*action | Axis event action. For details, see [InputEvent\_AxisAction](../oh-axis-type-h/document.md#inputevent_axisaction). |

**Return value**

| Type | Description |
| :-- | :-- |
| [Input\_Result](#input_result) | [INPUT\_SUCCESS](#input_result) if the operation is successful; [INPUT\_PARAMETER\_ERROR](#input_result) if **axisEvent** or **action** is null. |

#### \[h2\]OH\_Input\_SetAxisEventDisplayX()

Input\_Result OH\_Input\_SetAxisEventDisplayX(Input\_AxisEvent\* axisEvent, float displayX)

**Description**

Sets the X coordinate of the axis event in the relative coordinate system with the upper-left corner of the specified screen as the origin.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [Input\_AxisEvent](../../structs/input-axisevent/document.md)\* axisEvent | 
Axis event object. You can call [OH\_Input\_CreateAxisEvent](#oh_input_createaxisevent) to create an axis event object.

If the axis event object is no longer needed, destroy it by calling [OH\_Input\_DestroyAxisEvent](#oh_input_destroyaxisevent).

 |
| float displayX | X coordinate of the axis event in the relative coordinate system with the upper-left corner of the specified screen as the origin. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Input\_Result](#input_result) | [INPUT\_SUCCESS](#input_result) if the operation is successful; [INPUT\_PARAMETER\_ERROR](#input_result) if **axisEvent** is null. |

#### \[h2\]OH\_Input\_GetAxisEventDisplayX()

Input\_Result OH\_Input\_GetAxisEventDisplayX(const Input\_AxisEvent\* axisEvent, float\* displayX)

**Description**

Obtains the X coordinate of the axis event in the relative coordinate system with the upper-left corner of the specified screen as the origin.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| const [Input\_AxisEvent](../../structs/input-axisevent/document.md)\* axisEvent | 
Axis event object. You can call [OH\_Input\_CreateAxisEvent](#oh_input_createaxisevent) to create an axis event object.

If the axis event object is no longer needed, destroy it by calling [OH\_Input\_DestroyAxisEvent](#oh_input_destroyaxisevent).

 |
| float\* displayX | X coordinate of the axis event in the relative coordinate system with the upper-left corner of the specified screen as the origin. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Input\_Result](#input_result) | [INPUT\_SUCCESS](#input_result) if the operation is successful; [INPUT\_PARAMETER\_ERROR](#input_result) if **axisEvent** or **displayX** is null. |

#### \[h2\]OH\_Input\_SetAxisEventDisplayY()

Input\_Result OH\_Input\_SetAxisEventDisplayY(Input\_AxisEvent\* axisEvent, float displayY)

**Description**

Sets the Y coordinate of the axis event in the relative coordinate system with the upper-left corner of the specified screen as the origin.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [Input\_AxisEvent](../../structs/input-axisevent/document.md)\* axisEvent | 
Axis event object. You can call [OH\_Input\_CreateAxisEvent](#oh_input_createaxisevent) to create an axis event object.

If the axis event object is no longer needed, destroy it by calling [OH\_Input\_DestroyAxisEvent](#oh_input_destroyaxisevent).

 |
| float displayY | Y coordinate of the axis event in the relative coordinate system with the upper-left corner of the specified screen as the origin. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Input\_Result](#input_result) | [INPUT\_SUCCESS](#input_result) if the operation is successful; [INPUT\_PARAMETER\_ERROR](#input_result) if **axisEvent** is null. |

#### \[h2\]OH\_Input\_GetAxisEventDisplayY()

Input\_Result OH\_Input\_GetAxisEventDisplayY(const Input\_AxisEvent\* axisEvent, float\* displayY)

**Description**

Obtains the Y coordinate of the axis event in the relative coordinate system with the upper-left corner of the specified screen as the origin.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| const [Input\_AxisEvent](../../structs/input-axisevent/document.md)\* axisEvent | 
Axis event object. You can call [OH\_Input\_CreateAxisEvent](#oh_input_createaxisevent) to create an axis event object.

If the axis event object is no longer needed, destroy it by calling [OH\_Input\_DestroyAxisEvent](#oh_input_destroyaxisevent).

 |
| float\* displayY | Y coordinate of the axis event in the relative coordinate system with the upper-left corner of the specified screen as the origin. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Input\_Result](#input_result) | [INPUT\_SUCCESS](#input_result) if the operation is successful; [INPUT\_PARAMETER\_ERROR](#input_result) if **axisEvent** or **displayY** is null. |

#### \[h2\]OH\_Input\_SetAxisEventAxisValue()

Input\_Result OH\_Input\_SetAxisEventAxisValue(Input\_AxisEvent\* axisEvent,InputEvent\_AxisType axisType, double axisValue)

**Description**

Sets the axis value of the axis type specified by the axis event.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [Input\_AxisEvent](../../structs/input-axisevent/document.md)\* axisEvent | 
Axis event object. You can call [OH\_Input\_CreateAxisEvent](#oh_input_createaxisevent) to create an axis event object.

If the axis event object is no longer needed, destroy it by calling [OH\_Input\_DestroyAxisEvent](#oh_input_destroyaxisevent).

 |
| [InputEvent\_AxisType](../oh-axis-type-h/document.md#inputevent_axistype) axisType | Axis type. For details, see [InputEvent\_AxisType](../oh-axis-type-h/document.md#inputevent_axistype). |
| double axisValue | Axis event value. A positive number means scrolling forward (for example, 1.0 equals one unit forward), and a negative number means scrolling backward (for example, -1.0 equals one unit backward). |

**Return value**

| Type | Description |
| :-- | :-- |
| [Input\_Result](#input_result) | [INPUT\_SUCCESS](#input_result) if the operation is successful; [INPUT\_PARAMETER\_ERROR](#input_result) if **axisEvent** is null. |

#### \[h2\]OH\_Input\_GetAxisEventAxisValue()

Input\_Result OH\_Input\_GetAxisEventAxisValue(const Input\_AxisEvent\* axisEvent,InputEvent\_AxisType axisType, double\* axisValue)

**Description**

Obtains the axis value for the specified axis type of the axis event.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| const [Input\_AxisEvent](../../structs/input-axisevent/document.md)\* axisEvent | 
Axis event object. You can call [OH\_Input\_CreateAxisEvent](#oh_input_createaxisevent) to create an axis event object.

If the axis event object is no longer needed, destroy it by calling [OH\_Input\_DestroyAxisEvent](#oh_input_destroyaxisevent).

 |
| [InputEvent\_AxisType](../oh-axis-type-h/document.md#inputevent_axistype) axisType | Axis type. For details, see [InputEvent\_AxisType](../oh-axis-type-h/document.md#inputevent_axistype). |
| double\* axisValue | Axis event value. A positive number means scrolling forward (for example, 1.0 equals one unit forward), and a negative number means scrolling backward (for example, -1.0 equals one unit backward). |

**Return value**

| Type | Description |
| :-- | :-- |
| [Input\_Result](#input_result) | [INPUT\_SUCCESS](#input_result) if the operation is successful; [INPUT\_PARAMETER\_ERROR](#input_result) if **axisEvent** or **axisValue** is null. |

#### \[h2\]OH\_Input\_SetAxisEventActionTime()

Input\_Result OH\_Input\_SetAxisEventActionTime(Input\_AxisEvent\* axisEvent, int64\_t actionTime)

**Description**

Sets the time when an axis event occurs.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [Input\_AxisEvent](../../structs/input-axisevent/document.md)\* axisEvent | 
Axis event object. You can call [OH\_Input\_CreateAxisEvent](#oh_input_createaxisevent) to create an axis event object.

If the axis event object is no longer needed, destroy it by calling [OH\_Input\_DestroyAxisEvent](#oh_input_destroyaxisevent).

 |
| int64\_t actionTime | Time when an axis event occurs, in microseconds since the system starts. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Input\_Result](#input_result) | [INPUT\_SUCCESS](#input_result) if the operation is successful; [INPUT\_PARAMETER\_ERROR](#input_result) if **axisEvent** is null. |

#### \[h2\]OH\_Input\_GetAxisEventActionTime()

Input\_Result OH\_Input\_GetAxisEventActionTime(const Input\_AxisEvent\* axisEvent, int64\_t\* actionTime)

**Description**

Obtains the time when an axis event occurs.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| const [Input\_AxisEvent](../../structs/input-axisevent/document.md)\* axisEvent | 
Axis event object. You can call [OH\_Input\_CreateAxisEvent](#oh_input_createaxisevent) to create an axis event object.

If the axis event object is no longer needed, destroy it by calling [OH\_Input\_DestroyAxisEvent](#oh_input_destroyaxisevent).

 |
| int64\_t\* actionTime | Time when an axis event occurs, in microseconds since the system starts. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Input\_Result](#input_result) | [INPUT\_SUCCESS](#input_result) if the operation is successful; [INPUT\_PARAMETER\_ERROR](#input_result) if **axisEvent** or **actionTime** is null. |

#### \[h2\]OH\_Input\_SetAxisEventType()

Input\_Result OH\_Input\_SetAxisEventType(Input\_AxisEvent\* axisEvent, InputEvent\_AxisEventType axisEventType)

**Description**

Sets the axis event type.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [Input\_AxisEvent](../../structs/input-axisevent/document.md)\* axisEvent | 
Axis event object. You can call [OH\_Input\_CreateAxisEvent](#oh_input_createaxisevent) to create an axis event object.

If the axis event object is no longer needed, destroy it by calling [OH\_Input\_DestroyAxisEvent](#oh_input_destroyaxisevent).

 |
| [InputEvent\_AxisEventType](../oh-axis-type-h/document.md#inputevent_axiseventtype) axisEventType | Axis event type. For details, see [InputEvent\_AxisEventType](../oh-axis-type-h/document.md#inputevent_axiseventtype). |

**Return value**

| Type | Description |
| :-- | :-- |
| [Input\_Result](#input_result) | [INPUT\_SUCCESS](#input_result) if the operation is successful; [INPUT\_PARAMETER\_ERROR](#input_result) if **axisEvent** is null. |

#### \[h2\]OH\_Input\_GetAxisEventType()

Input\_Result OH\_Input\_GetAxisEventType(const Input\_AxisEvent\* axisEvent, InputEvent\_AxisEventType\* axisEventType)

**Description**

Obtains the axis event type.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| const [Input\_AxisEvent](../../structs/input-axisevent/document.md)\* axisEvent | 
Axis event object. You can call [OH\_Input\_CreateAxisEvent](#oh_input_createaxisevent) to create an axis event object.

If the axis event object is no longer needed, destroy it by calling [OH\_Input\_DestroyAxisEvent](#oh_input_destroyaxisevent).

 |
| [InputEvent\_AxisEventType](../oh-axis-type-h/document.md#inputevent_axiseventtype)\* axisEventType | Axis event type. For details, see [InputEvent\_AxisEventType](../oh-axis-type-h/document.md#inputevent_axiseventtype). |

**Return value**

| Type | Description |
| :-- | :-- |
| [Input\_Result](#input_result) | [INPUT\_SUCCESS](#input_result) if the operation is successful; [INPUT\_PARAMETER\_ERROR](#input_result) if **axisEvent** or **axisEventType** is null. |

#### \[h2\]OH\_Input\_SetAxisEventSourceType()

Input\_Result OH\_Input\_SetAxisEventSourceType(Input\_AxisEvent\* axisEvent, InputEvent\_SourceType sourceType)

**Description**

Sets the axis event source type.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [Input\_AxisEvent](../../structs/input-axisevent/document.md)\* axisEvent | 
Axis event object. You can call [OH\_Input\_CreateAxisEvent](#oh_input_createaxisevent) to create an axis event object.

If the axis event object is no longer needed, destroy it by calling [OH\_Input\_DestroyAxisEvent](#oh_input_destroyaxisevent).

 |
| [InputEvent\_SourceType](#inputevent_sourcetype) sourceType | Axis event source type. For details, see [InputEvent\_SourceType](#inputevent_sourcetype). |

**Return value**

| Type | Description |
| :-- | :-- |
| [Input\_Result](#input_result) | [INPUT\_SUCCESS](#input_result) if the operation is successful; [INPUT\_PARAMETER\_ERROR](#input_result) if **axisEvent** is null. |

#### \[h2\]OH\_Input\_GetAxisEventSourceType()

Input\_Result OH\_Input\_GetAxisEventSourceType(const Input\_AxisEvent\* axisEvent, InputEvent\_SourceType\* sourceType)

**Description**

Obtains the axis event source type.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| const [Input\_AxisEvent](../../structs/input-axisevent/document.md)\* axisEvent | 
Axis event object. You can call [OH\_Input\_CreateAxisEvent](#oh_input_createaxisevent) to create an axis event object.

If the axis event object is no longer needed, destroy it by calling [OH\_Input\_DestroyAxisEvent](#oh_input_destroyaxisevent).

 |
| [InputEvent\_SourceType](#inputevent_sourcetype)\* sourceType | Axis event source type. For details, see [InputEvent\_SourceType](#inputevent_sourcetype). |

**Return value**

| Type | Description |
| :-- | :-- |
| [Input\_Result](#input_result) | [INPUT\_SUCCESS](#input_result) if the operation is successful; [INPUT\_PARAMETER\_ERROR](#input_result) if **axisEvent** or **sourceType** is null. |

#### \[h2\]OH\_Input\_SetAxisEventWindowId()

Input\_Result OH\_Input\_SetAxisEventWindowId(Input\_AxisEvent\* axisEvent, int32\_t windowId)

**Description**

Sets the window ID of an axis event.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Since**: 15

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [Input\_AxisEvent](../../structs/input-axisevent/document.md)\* axisEvent | 
Axis event object. You can call [OH\_Input\_CreateAxisEvent](#oh_input_createaxisevent) to create an axis event object.

If the axis event object is no longer needed, destroy it by calling [OH\_Input\_DestroyAxisEvent](#oh_input_destroyaxisevent).

 |
| int32\_t windowId | Window ID of an axis event. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Input\_Result](#input_result) | [INPUT\_SUCCESS](#input_result) if the operation is successful; [INPUT\_PARAMETER\_ERROR](#input_result) if **axisEvent** is null. |

#### \[h2\]OH\_Input\_GetAxisEventWindowId()

Input\_Result OH\_Input\_GetAxisEventWindowId(const Input\_AxisEvent\* axisEvent, int32\_t\* windowId)

**Description**

Obtains the window ID of an axis event.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Since**: 15

**Parameters**

| Parameter | Description |
| :-- | :-- |
| const [Input\_AxisEvent](../../structs/input-axisevent/document.md)\* axisEvent | 
Axis event object. You can call [OH\_Input\_CreateAxisEvent](#oh_input_createaxisevent) to create an axis event object.

If the axis event object is no longer needed, destroy it by calling [OH\_Input\_DestroyAxisEvent](#oh_input_destroyaxisevent).

 |
| int32\_t\* windowId | Window ID of the axis event. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Input\_Result](#input_result) | [INPUT\_SUCCESS](#input_result) if the operation is successful; [INPUT\_PARAMETER\_ERROR](#input_result) if **axisEvent** or **windowId** is null. |

#### \[h2\]OH\_Input\_SetAxisEventDisplayId()

Input\_Result OH\_Input\_SetAxisEventDisplayId(Input\_AxisEvent\* axisEvent, int32\_t displayId)

**Description**

Sets the screen ID of an axis event.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Since**: 15

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [Input\_AxisEvent](../../structs/input-axisevent/document.md)\* axisEvent | 
Axis event object. You can call [OH\_Input\_CreateAxisEvent](#oh_input_createaxisevent) to create an axis event object.

If the axis event object is no longer needed, destroy it by calling [OH\_Input\_DestroyAxisEvent](#oh_input_destroyaxisevent).

 |
| int32\_t displayId | Screen ID of an axis event. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Input\_Result](#input_result) | [INPUT\_SUCCESS](#input_result) if the operation is successful; [INPUT\_PARAMETER\_ERROR](#input_result) if **axisEvent** is null. |

#### \[h2\]OH\_Input\_GetAxisEventDisplayId()

Input\_Result OH\_Input\_GetAxisEventDisplayId(const Input\_AxisEvent\* axisEvent, int32\_t\* displayId)

**Description**

Obtains the screen ID of an axis event.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Since**: 15

**Parameters**

| Parameter | Description |
| :-- | :-- |
| const [Input\_AxisEvent](../../structs/input-axisevent/document.md)\* axisEvent | 
Axis event object. You can call [OH\_Input\_CreateAxisEvent](#oh_input_createaxisevent) to create an axis event object.

If the axis event object is no longer needed, destroy it by calling [OH\_Input\_DestroyAxisEvent](#oh_input_destroyaxisevent).

 |
| int32\_t\* displayId | Screen ID of the axis event. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Input\_Result](#input_result) | [INPUT\_SUCCESS](#input_result) if the operation is successful; [INPUT\_PARAMETER\_ERROR](#input_result) if **axisEvent** or **displayId** is null. |

#### \[h2\]OH\_Input\_AddKeyEventMonitor()

Input\_Result OH\_Input\_AddKeyEventMonitor(Input\_KeyEventCallback callback)

**Description**

Adds a listener for key events. Only the initial addition takes effect. Subsequent attempts will be ignored.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Required permissions**: ohos.permission.INPUT\_MONITORING

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [Input\_KeyEventCallback](#input_keyeventcallback) callback | Callback used to receive key events. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Input\_Result](#input_result) | 
[INPUT\_SUCCESS](#input_result) if the operation is successful; [INPUT\_PERMISSION\_DENIED](#input_result) if permission verification fails;

[INPUT\_PARAMETER\_ERROR](#input_result) if the callback is empty; [INPUT\_SERVICE\_EXCEPTION](#input_result) if the service is abnormal.

 |

#### \[h2\]OH\_Input\_AddMouseEventMonitor()

Input\_Result OH\_Input\_AddMouseEventMonitor(Input\_MouseEventCallback callback)

**Description**

Adds a listener for mouse events, including mouse click and movement events, but not scroll wheel events. Scroll wheel events are axis events.

This API can be called only when the screen recording scenario is in use. Otherwise, the call does not take effect.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Required permissions**: ohos.permission.INPUT\_MONITORING

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [Input\_MouseEventCallback](#input_mouseeventcallback) callback | Callback used to receive mouse events. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Input\_Result](#input_result) | 
[INPUT\_SUCCESS](#input_result) if the operation is successful; [INPUT\_PERMISSION\_DENIED](#input_result) if permission verification fails;

[INPUT\_PARAMETER\_ERROR](#input_result) if the callback is empty; [INPUT\_SERVICE\_EXCEPTION](#input_result) if the service is abnormal.

 |

#### \[h2\]OH\_Input\_AddTouchEventMonitor()

Input\_Result OH\_Input\_AddTouchEventMonitor(Input\_TouchEventCallback callback)

**Description**

Adds a listener for touch input events.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Required permissions**: ohos.permission.INPUT\_MONITORING

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [Input\_TouchEventCallback](#input_toucheventcallback) callback | Callback used to receive touch events. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Input\_Result](#input_result) | 
[INPUT\_SUCCESS](#input_result) if the operation is successful; [INPUT\_PERMISSION\_DENIED](#input_result) if permission verification fails;

[INPUT\_PARAMETER\_ERROR](#input_result) if the callback is empty; [INPUT\_SERVICE\_EXCEPTION](#input_result) if the service is abnormal.

 |

#### \[h2\]OH\_Input\_AddAxisEventMonitorForAll()

Input\_Result OH\_Input\_AddAxisEventMonitorForAll(Input\_AxisEventCallback callback)

**Description**

Adds a listener for all types of axis events, which are defined in [InputEvent\_AxisEventType](../oh-axis-type-h/document.md#inputevent_axiseventtype).

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Required permissions**: ohos.permission.INPUT\_MONITORING

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [Input\_AxisEventCallback](#input_axiseventcallback) callback | Callback used to receive axis events. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Input\_Result](#input_result) | 
[INPUT\_SUCCESS](#input_result) if the operation is successful; [INPUT\_PERMISSION\_DENIED](#input_result) if permission verification fails;

[INPUT\_PARAMETER\_ERROR](#input_result) if the callback is empty; [INPUT\_SERVICE\_EXCEPTION](#input_result) if the service is abnormal.

 |

#### \[h2\]OH\_Input\_AddAxisEventMonitor()

Input\_Result OH\_Input\_AddAxisEventMonitor(InputEvent\_AxisEventType axisEventType, Input\_AxisEventCallback callback)

**Description**

Adds a listener for the specified type of axis events, which are defined in [InputEvent\_AxisEventType](../oh-axis-type-h/document.md#inputevent_axiseventtype).

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Required permissions**: ohos.permission.INPUT\_MONITORING

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [InputEvent\_AxisEventType](../oh-axis-type-h/document.md#inputevent_axiseventtype) axisEventType | Axis event type, which is defined in [InputEvent\_AxisEventType](../oh-axis-type-h/document.md#inputevent_axiseventtype). |
| [Input\_AxisEventCallback](#input_axiseventcallback) callback | Callback used to receive the specified type of axis events. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Input\_Result](#input_result) | 
[INPUT\_SUCCESS](#input_result) if the operation is successful; [INPUT\_PERMISSION\_DENIED](#input_result) if permission verification fails;

[INPUT\_PARAMETER\_ERROR](#input_result) if the callback is empty; [INPUT\_SERVICE\_EXCEPTION](#input_result) if the service is abnormal.

 |

#### \[h2\]OH\_Input\_RemoveKeyEventMonitor()

Input\_Result OH\_Input\_RemoveKeyEventMonitor(Input\_KeyEventCallback callback)

**Description**

Removes the listener for key events.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Required permissions**: ohos.permission.INPUT\_MONITORING

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [Input\_KeyEventCallback](#input_keyeventcallback) callback | Callback for key events. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Input\_Result](#input_result) | 
[INPUT\_SUCCESS](#input_result) if the operation is successful; [INPUT\_PERMISSION\_DENIED](#input_result) if permission verification fails;

[INPUT\_PARAMETER\_ERROR](#input_result) if the callback is empty or no listener is added; [INPUT\_SERVICE\_EXCEPTION](#input_result) if the service is abnormal.

 |

#### \[h2\]OH\_Input\_RemoveMouseEventMonitor()

Input\_Result OH\_Input\_RemoveMouseEventMonitor(Input\_MouseEventCallback callback)

**Description**

Removes the listener for mouse events.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Required permissions**: ohos.permission.INPUT\_MONITORING

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [Input\_MouseEventCallback](#input_mouseeventcallback) callback | Callback for mouse events. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Input\_Result](#input_result) | 
[INPUT\_SUCCESS](#input_result) if the operation is successful; [INPUT\_PERMISSION\_DENIED](#input_result) if permission verification fails;

[INPUT\_PARAMETER\_ERROR](#input_result) if the callback is empty or no listener is added; [INPUT\_SERVICE\_EXCEPTION](#input_result) if the service is abnormal.

 |

#### \[h2\]OH\_Input\_RemoveTouchEventMonitor()

Input\_Result OH\_Input\_RemoveTouchEventMonitor(Input\_TouchEventCallback callback)

**Description**

Removes the listener for touch events.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Required permissions**: ohos.permission.INPUT\_MONITORING

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [Input\_TouchEventCallback](#input_toucheventcallback) callback | Callback for touch events. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Input\_Result](#input_result) | 
[INPUT\_SUCCESS](#input_result) if the operation is successful; [INPUT\_PERMISSION\_DENIED](#input_result) if permission verification fails;

[INPUT\_PARAMETER\_ERROR](#input_result) if the callback is empty or no listener is added; [INPUT\_SERVICE\_EXCEPTION](#input_result) if the service is abnormal.

 |

#### \[h2\]OH\_Input\_RemoveAxisEventMonitorForAll()

Input\_Result OH\_Input\_RemoveAxisEventMonitorForAll(Input\_AxisEventCallback callback)

**Description**

Removes the listener for all types of axis events.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Required permissions**: ohos.permission.INPUT\_MONITORING

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [Input\_AxisEventCallback](#input_axiseventcallback) callback | Callback for the all types of axis events. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Input\_Result](#input_result) | 
[INPUT\_SUCCESS](#input_result) if the operation is successful; [INPUT\_PERMISSION\_DENIED](#input_result) if permission verification fails;

[INPUT\_PARAMETER\_ERROR](#input_result) if the callback is empty or no listener is added; [INPUT\_SERVICE\_EXCEPTION](#input_result) if the service is abnormal.

 |

#### \[h2\]OH\_Input\_RemoveAxisEventMonitor()

Input\_Result OH\_Input\_RemoveAxisEventMonitor(InputEvent\_AxisEventType axisEventType, Input\_AxisEventCallback callback)

**Description**

Removes the listener for the specified type of axis events, which are defined in [InputEvent\_AxisEventType](../oh-axis-type-h/document.md#inputevent_axiseventtype).

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Required permissions**: ohos.permission.INPUT\_MONITORING

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [InputEvent\_AxisEventType](../oh-axis-type-h/document.md#inputevent_axiseventtype) axisEventType | Axis event type, which is defined in [InputEvent\_AxisEventType](../oh-axis-type-h/document.md#inputevent_axiseventtype). |
| [Input\_AxisEventCallback](#input_axiseventcallback) callback | Callback for the specified type of axis events. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Input\_Result](#input_result) | 
[INPUT\_SUCCESS](#input_result) if the operation is successful; [INPUT\_PERMISSION\_DENIED](#input_result) if permission verification fails;

[INPUT\_PARAMETER\_ERROR](#input_result) if the callback is empty or no listener is added; [INPUT\_SERVICE\_EXCEPTION](#input_result) if the service is abnormal.

 |

#### \[h2\]OH\_Input\_AddKeyEventInterceptor()

Input\_Result OH\_Input\_AddKeyEventInterceptor(Input\_KeyEventCallback callback, Input\_InterceptorOptions \*option)

**Description**

Adds a key event interceptor. Only the first addition takes effect. Subsequent requests will return error code [INPUT\_REPEAT\_INTERCEPTOR](#input_result). Key events are intercepted only when the application gains focus.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Required permission**: ohos.permission.INTERCEPT\_INPUT\_EVENT

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [Input\_KeyEventCallback](#input_keyeventcallback) callback | Callback used to receive key events. |
| [Input\_InterceptorOptions](../../structs/input-interceptoroptions/document.md) \*option | Options for event interception. If **null** is passed, the default value is used. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Input\_Result](#input_result) | 
[INPUT\_SUCCESS](#input_result) if the operation is successful; [INPUT\_PERMISSION\_DENIED](#input_result) if permission verification fails;

[INPUT\_PARAMETER\_ERROR](#input_result) if the callback is empty or no listener is added; [INPUT\_REPEAT\_INTERCEPTOR](#input_result) if an interceptor is repeatedly added;

[INPUT\_SERVICE\_EXCEPTION](#input_result) if the service is abnormal.

 |

#### \[h2\]OH\_Input\_AddInputEventInterceptor()

Input\_Result OH\_Input\_AddInputEventInterceptor(Input\_InterceptorEventCallback \*callback,Input\_InterceptorOptions \*option)

**Description**

Adds an interceptor for input events, including mouse, touch, and axis events. Only the first addition takes effect. Subsequent requests will return error code [INPUT\_REPEAT\_INTERCEPTOR](#input_result). Key events are intercepted only when the application window is hit.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Required permission**: ohos.permission.INTERCEPT\_INPUT\_EVENT

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [Input\_InterceptorEventCallback](../../structs/input-interceptoreventcallback/document.md) \*callback | Pointer to the structure of the interceptor event callback. For details, see [Input\_InterceptorEventCallback](../../structs/input-interceptoreventcallback/document.md). |
| [Input\_InterceptorOptions](../../structs/input-interceptoroptions/document.md) \*option | Options for event interception. If **null** is passed, the default value is used. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Input\_Result](#input_result) | 
[INPUT\_SUCCESS](#input_result) if the operation is successful; [INPUT\_PERMISSION\_DENIED](#input_result) if permission verification fails;

[INPUT\_PARAMETER\_ERROR](#input_result) if the callback is empty or no listener is added; [INPUT\_REPEAT\_INTERCEPTOR](#input_result) if an interceptor is repeatedly added;

[INPUT\_SERVICE\_EXCEPTION](#input_result) if the service is abnormal.

 |

#### \[h2\]OH\_Input\_RemoveKeyEventInterceptor()

Input\_Result OH\_Input\_RemoveKeyEventInterceptor(void)

**Description**

Removes the interceptor for key events.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Required permission**: ohos.permission.INTERCEPT\_INPUT\_EVENT

**Since**: 12

**Return value**

| Type | Description |
| :-- | :-- |
| [Input\_Result](#input_result) | 
[INPUT\_SUCCESS](#input_result) if the operation is successful; [INPUT\_PERMISSION\_DENIED](#input_result) if permission verification fails;

[INPUT\_SERVICE\_EXCEPTION](#input_result) if the service is abnormal.

 |

#### \[h2\]OH\_Input\_RemoveInputEventInterceptor()

Input\_Result OH\_Input\_RemoveInputEventInterceptor(void)

**Description**

Removes the interceptor for input events, including mouse, touch, and axis events.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Required permission**: ohos.permission.INTERCEPT\_INPUT\_EVENT

**Since**: 12

**Return value**

| Type | Description |
| :-- | :-- |
| [Input\_Result](#input_result) | 
[INPUT\_SUCCESS](#input_result) if the operation is successful; [INPUT\_PERMISSION\_DENIED](#input_result) if permission verification fails;

[INPUT\_SERVICE\_EXCEPTION](#input_result) if the service is abnormal.

 |

#### \[h2\]OH\_Input\_GetIntervalSinceLastInput()

Input\_Result OH\_Input\_GetIntervalSinceLastInput(int64\_t \*timeInterval)

**Description**

Obtains the interval since the last system input event.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Since**: 14

**Parameters**

| Parameter | Description |
| :-- | :-- |
| int64\_t \*timeInterval | Time interval, in μs. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Input\_Result](#input_result) | 
Return value of the **OH\_Input\_GetIntervalSinceLastInput** function.

[INPUT\_SUCCESS](#input_result) if the interval is obtained successfully; [INPUT\_SERVICE\_EXCEPTION](#input_result) if the service is abnormal; [INPUT\_PARAMETER\_ERROR](#input_result) if the parameter is incorrect.

 |

#### \[h2\]OH\_Input\_CreateHotkey()

Input\_Hotkey \*OH\_Input\_CreateHotkey(void)

**Description**

Creates a hotkey object. You can call [OH\_Input\_DestroyHotkey](#oh_input_destroyhotkey) to destroy a hotkey object.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Since**: 14

**Return value**

| Type | Description |
| :-- | :-- |
| [Input\_Hotkey](../../structs/input-hotkey/document.md) | [Input\_Hotkey](../../structs/input-hotkey/document.md) pointer if the operation is successful; a null pointer otherwise (possibly because of a memory allocation failure). |

#### \[h2\]OH\_Input\_DestroyHotkey()

void OH\_Input\_DestroyHotkey(Input\_Hotkey \*\*hotkey)

**Description**

Destroys a hotkey object.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Since**: 14

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [Input\_Hotkey](../../structs/input-hotkey/document.md) \*\*hotkey | Hotkey object. |

#### \[h2\]OH\_Input\_SetPreKeys()

void OH\_Input\_SetPreKeys(Input\_Hotkey \*hotkey, int32\_t \*preKeys, int32\_t size)

**Description**

Sets the modifier keys.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Since**: 14

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [Input\_Hotkey](../../structs/input-hotkey/document.md) \*hotkey | Hotkey object. |
| int32\_t \*preKeys | List of modifier keys. |
| int32\_t size | Number of modifier keys. One or two modifier keys are supported. |

#### \[h2\]OH\_Input\_GetPreKeys()

Input\_Result OH\_Input\_GetPreKeys(const Input\_Hotkey \*hotkey, int32\_t \*\*preKeys, int32\_t \*preKeyCount)

**Description**

Obtains the modifier key.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Since**: 14

**Parameters**

| Parameter | Description |
| :-- | :-- |
| const [Input\_Hotkey](../../structs/input-hotkey/document.md) \*hotkey | Hotkey object. |
| int32\_t \*\*preKeys | List of modifier keys. |
| int32\_t \*preKeyCount | Number of modifier keys. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Input\_Result](#input_result) | 
Return value of the **OH\_Input\_GetPreKeys** function.

[INPUT\_SUCCESS](#input_result) if the operation is successful; [INPUT\_PARAMETER\_ERROR](#input_result) otherwise.

 |

#### \[h2\]OH\_Input\_SetFinalKey()

void OH\_Input\_SetFinalKey(Input\_Hotkey\* hotkey, int32\_t finalKey)

**Description**

Sets the modified key.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Since**: 14

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [Input\_Hotkey](../../structs/input-hotkey/document.md)\* hotkey | Hotkey object. |
| int32\_t finalKey | Modifier key value. Only one modifier key value is allowed. |

#### \[h2\]OH\_Input\_GetFinalKey()

Input\_Result OH\_Input\_GetFinalKey(const Input\_Hotkey\* hotkey, int32\_t \*finalKeyCode)

**Description**

Obtains the modified key.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Since**: 14

**Parameters**

| Parameter | Description |
| :-- | :-- |
| const [Input\_Hotkey](../../structs/input-hotkey/document.md)\* hotkey | Hotkey object. |
| int32\_t \*finalKeyCode | Modified key. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Input\_Result](#input_result) | 
Return value of the **OH\_Input\_GetFinalKey** function.

[INPUT\_SUCCESS](#input_result) if the operation is successful;

[INPUT\_PARAMETER\_ERROR](#input_result) otherwise.

 |

#### \[h2\]OH\_Input\_CreateAllSystemHotkeys()

Input\_Hotkey \*\*OH\_Input\_CreateAllSystemHotkeys(int32\_t count)

**Description**

Creates an [Input\_Hotkey](../../structs/input-hotkey/document.md) array. You can call [OH\_Input\_DestroyAllSystemHotkeys](#oh_input_destroyallsystemhotkeys) to destroy the array of the [Input\_Hotkey](../../structs/input-hotkey/document.md) instance and reclaim the memory.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Device behavior differences**: This API has no effect on wearables, but can be properly called on other devices.

**Since**: 14

**Parameters**

| Parameter | Description |
| :-- | :-- |
| int32\_t count | Number of [Input\_Hotkey](../../structs/input-hotkey/document.md) instances. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Input\_Hotkey](../../structs/input-hotkey/document.md) | 
Return value of the **OH\_Input\_CreateAllSystemHotkeys** function.

which is [INPUT\_SUCCESS](#input_result) if the operation is successful.

 |

#### \[h2\]OH\_Input\_DestroyAllSystemHotkeys()

void OH\_Input\_DestroyAllSystemHotkeys(Input\_Hotkey \*\*hotkeys, int32\_t count)

**Description**

Destroys an [Input\_Hotkey](../../structs/input-hotkey/document.md) array and reclaims the memory.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Since**: 14

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [Input\_Hotkey](../../structs/input-hotkey/document.md) \*\*hotkeys | Double pointer to the [Input\_Hotkey](../../structs/input-hotkey/document.md) array. |
| int32\_t count | Number of [Input\_Hotkey](../../structs/input-hotkey/document.md) instances. |

#### \[h2\]OH\_Input\_GetAllSystemHotkeys()

Input\_Result OH\_Input\_GetAllSystemHotkeys(Input\_Hotkey \*\*hotkey, int32\_t \*count)

**Description**

Obtains all configured hotkeys.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Device behavior differences**: This API has no effect on wearables, but can be properly called on other devices.

**Since**: 14

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [Input\_Hotkey](../../structs/input-hotkey/document.md) \*\*hotkey | [Input\_Hotkey](../../structs/input-hotkey/document.md) array. When calling this API for the first time, you can pass **NULL** to obtain the array length. |
| int32\_t \*count | Number of supported hotkeys. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Input\_Result](#input_result) | 
Return value of the **OH\_Input\_GetAllSystemHotkeys** function.

[INPUT\_SUCCESS](#input_result) if the operation is successful;

[INPUT\_PARAMETER\_ERROR](#input_result) otherwise.

 |

#### \[h2\]OH\_Input\_SetRepeat()

void OH\_Input\_SetRepeat(Input\_Hotkey\* hotkey, bool isRepeat)

**Description**

Specifies whether to report repeated key events.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Since**: 14

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [Input\_Hotkey](../../structs/input-hotkey/document.md)\* hotkey | Hotkey object. |
| bool isRepeat | Whether to report repeated key events. The value **true** means to report repeated key events, and the value **false** means the opposite. |

#### \[h2\]OH\_Input\_GetRepeat()

Input\_Result OH\_Input\_GetRepeat(const Input\_Hotkey\* hotkey, bool \*isRepeat)

**Description**

Checks whether to report repeated key events.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Since**: 14

**Parameters**

| Parameter | Description |
| :-- | :-- |
| const [Input\_Hotkey](../../structs/input-hotkey/document.md)\* hotkey | Hotkey object. |
| bool \*isRepeat | Whether the reported key event is repeated. The value **true** indicates that the key event is repeated, and the value **false** indicates that the key event is not repeated. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Input\_Result](#input_result) | 
Return value of the **OH\_Input\_GetRepeat** function.

[INPUT\_SUCCESS](#input_result) if the operation is successful;

[INPUT\_PARAMETER\_ERROR](#input_result) otherwise.

 |

#### \[h2\]OH\_Input\_AddHotkeyMonitor()

Input\_Result OH\_Input\_AddHotkeyMonitor(const Input\_Hotkey\* hotkey, Input\_HotkeyCallback callback)

**Description**

Subscribes to hotkey events.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/4eorMmdDTySQXuid_trb_g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062404Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E366B4B43CE7AF8605E602E0F1A0D14C74C85C67CBF3ADB43FBC3DCDCF9556D6)

When subscribing to hotkey events, pay attention to the following restrictions on **preKeys** and **finalKey**:

1.  **preKeys**: Modifier key set (including Ctrl, Shift, and Alt) containing 1-4 keys. There is no requirement on the key order. For example, in **Ctrl+Shift+Esc**, **Ctrl** and **Shift** are modifier keys.
2.  **finalKey**: Modified key, which can be any key except the modifier keys and Meta key. For details about the keys, see [Key Codes of the Key Devices](../oh-key-code-h/document.md). For example, in **Ctrl+Shift+Esc**, **Esc** is the modifier key.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Device behavior differences**: This API can be properly called on devices other than wearables. If it is called on wearables, error code 801 is returned.

**Since**: 14

**Parameters**

| Parameter | Description |
| :-- | :-- |
| const [Input\_Hotkey](../../structs/input-hotkey/document.md)\* hotkey | Hotkey object. |
| [Input\_HotkeyCallback](#input_hotkeycallback) callback | Defines the callback used to return hotkey events. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Input\_Result](#input_result) | 
Return value of the **OH\_Input\_AddHotkeyMonitor** function.

[INPUT\_SUCCESS](#input_result) if the operation is successful;

[INPUT\_PARAMETER\_ERROR](#input_result) if parameter verification fails;

[INPUT\_OCCUPIED\_BY\_SYSTEM](#input_result) if the hotkey has been occupied by the system (you can use [OH\_Input\_GetAllSystemHotkeys](#oh_input_getallsystemhotkeys) to query allsystem hotkeys);

[INPUT\_OCCUPIED\_BY\_OTHER](#input_result) if the hotkey has been occupied by another application;

[INPUT\_DEVICE\_NOT\_SUPPORTED](#input_result) if the function is not supported.

 |

#### \[h2\]OH\_Input\_RemoveHotkeyMonitor()

Input\_Result OH\_Input\_RemoveHotkeyMonitor(const Input\_Hotkey\* hotkey, Input\_HotkeyCallback callback)

**Description**

Unsubscribes from hotkey events.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Since**: 14

**Parameters**

| Parameter | Description |
| :-- | :-- |
| const [Input\_Hotkey](../../structs/input-hotkey/document.md)\* hotkey | Hotkey object. |
| [Input\_HotkeyCallback](#input_hotkeycallback) callback | Defines the callback used to return hotkey events. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Input\_Result](#input_result) | 
Return value of the **OH\_Input\_RemoveHotkeyMonitor** function.

[INPUT\_SUCCESS](#input_result) if the operation is successful; [INPUT\_PARAMETER\_ERROR](#input_result) if parameter verification fails.

 |

#### \[h2\]OH\_Input\_RegisterDeviceListener()

Input\_Result OH\_Input\_RegisterDeviceListener(Input\_DeviceListener\* listener)

**Description**

Registers a listener for device hot swap events.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Since**: 13

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [Input\_DeviceListener](../../structs/input-devicelistener/document.md)\* listener | Pointer to the [Input\_DeviceListener](../../structs/input-devicelistener/document.md) object. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Input\_Result](#input_result) | 
Return value of the **OH\_Input\_RegisterDeviceListener** function.

[INPUT\_SUCCESS](#input_result) if the operation is successful;

[INPUT\_PARAMETER\_ERROR](#input_result) if the listener is null.

 |

#### \[h2\]OH\_Input\_UnregisterDeviceListener()

Input\_Result OH\_Input\_UnregisterDeviceListener(Input\_DeviceListener\* listener)

**Description**

Unregisters the listener for device hot swap events.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Since**: 13

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [Input\_DeviceListener](../../structs/input-devicelistener/document.md)\* listener | Pointer to the [Input\_DeviceListener](../../structs/input-devicelistener/document.md) object. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Input\_Result](#input_result) | 
Return value of the **OH\_Input\_UnregisterDeviceListener** function.

[INPUT\_SUCCESS](#input_result) if the operation is successful;

[INPUT\_PARAMETER\_ERROR](#input_result) if **listener** is null or the listener is not registered;

[INPUT\_SERVICE\_EXCEPTION](#input_result) if the service is abnormal.

 |

#### \[h2\]OH\_Input\_UnregisterDeviceListeners()

Input\_Result OH\_Input\_UnregisterDeviceListeners()

**Description**

Unregisters the listener for all device hot swap events.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Since**: 13

**Return value**

| Type | Description |
| :-- | :-- |
| [Input\_Result](#input_result) | 
Return value of the **OH\_Input\_UnregisterDeviceListener** function.

[INPUT\_SUCCESS](#input_result) if the operation is successful;

[INPUT\_SERVICE\_EXCEPTION](#input_result) if the service is abnormal.

 |

#### \[h2\]OH\_Input\_GetDeviceIds()

Input\_Result OH\_Input\_GetDeviceIds(int32\_t \*deviceIds, int32\_t inSize, int32\_t \*outSize)

**Description**

Obtains the IDs of all input devices.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Since**: 13

**Parameters**

| Parameter | Description |
| :-- | :-- |
| int32\_t \*deviceIds | List of input device IDs. |
| int32\_t inSize | Size of the input device ID list. |
| int32\_t \*outSize | Length of the output device ID list. The value must be less than or equal to the value of **inSize**. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Input\_Result](#input_result) | 
[INPUT\_SUCCESS](#input_result) if the operation is successful;

[INPUT\_PARAMETER\_ERROR](#input_result) if **deviceIds** or **outSize** is a null pointer or **inSize** is less than **0**.

 |

#### \[h2\]OH\_Input\_GetDevice()

Input\_Result OH\_Input\_GetDevice(int32\_t deviceId, Input\_DeviceInfo \*\*deviceInfo)

**Description**

Obtains information about the input device.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Since**: 13

**Parameters**

| Parameter | Description |
| :-- | :-- |
| int32\_t deviceId | Unique ID of the input device. If a physical device is repeatedly reinstalled or restarted, its ID may change. |
| [Input\_DeviceInfo](../../structs/input-deviceinfo/document.md) \*\*deviceInfo | Pointer to the [Input\_DeviceInfo](../../structs/input-deviceinfo/document.md) object. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Input\_Result](#input_result) | 
[INPUT\_SUCCESS](#input_result) if the operation is successful;

[INPUT\_PARAMETER\_ERROR](#input_result) if **deviceInfo** is a null pointer or **deviceId** is invalid.

You can use [OH\_Input\_GetDeviceIds](#oh_input_getdeviceids) to query the device IDs supported by the system.

 |

#### \[h2\]OH\_Input\_CreateDeviceInfo()

Input\_DeviceInfo\* OH\_Input\_CreateDeviceInfo(void)

**Description**

Creates a **deviceInfo** object. You can call [OH\_Input\_DestroyDeviceInfo](#oh_input_destroydeviceinfo) to destroy an input device information object.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Since**: 13

**Return value**

| Type | Description |
| :-- | :-- |
| Input\_DeviceInfo\* | Pointer to the [Input\_DeviceInfo](../../structs/input-deviceinfo/document.md) object if the operation is successful; a null pointer otherwise (possibly because of a memory allocation failure). |

#### \[h2\]OH\_Input\_DestroyDeviceInfo()

void OH\_Input\_DestroyDeviceInfo(Input\_DeviceInfo \*\*deviceInfo)

**Description**

Destroys a **deviceInfo** object.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Since**: 13

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [Input\_DeviceInfo](../../structs/input-deviceinfo/document.md) \*\*deviceInfo | **deviceInfo** object. |

#### \[h2\]OH\_Input\_GetKeyboardType()

Input\_Result OH\_Input\_GetKeyboardType(int32\_t deviceId, int32\_t \*keyboardType)

**Description**

Obtains the keyboard type of the input device.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Since**: 13

**Parameters**

| Parameter | Description |
| :-- | :-- |
| int32\_t deviceId | Unique ID of the input device. If a physical device is repeatedly reinstalled or restarted, its ID may change. |
| int32\_t \*keyboardType | Pointer to the keyboard type of the input device. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Input\_Result](#input_result) | 
[INPUT\_SUCCESS](#input_result) if the operation is successful;

[INPUT\_PARAMETER\_ERROR](#input_result) if the device ID is invalid or **keyboardType** is a null pointer.

 |

#### \[h2\]OH\_Input\_GetDeviceId()

Input\_Result OH\_Input\_GetDeviceId(Input\_DeviceInfo \*deviceInfo, int32\_t \*id)

**Description**

Obtains the ID of an input device.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Since**: 13

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [Input\_DeviceInfo](../../structs/input-deviceinfo/document.md) \*deviceInfo | Input device information. For details, see [Input\_DeviceInfo](../../structs/input-deviceinfo/document.md). |
| int32\_t \*id | Pointer to the input device ID. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Input\_Result](#input_result) | 
[INPUT\_SUCCESS](#input_result) if the operation is successful;

[INPUT\_PARAMETER\_ERROR](#input_result) if **deviceInfo** or **ID** is a null pointer.

 |

#### \[h2\]OH\_Input\_GetDeviceName()

Input\_Result OH\_Input\_GetDeviceName(Input\_DeviceInfo \*deviceInfo, char \*\*name)

**Description**

Obtains the name of an input device.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Since**: 13

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [Input\_DeviceInfo](../../structs/input-deviceinfo/document.md) \*deviceInfo | Input device information. For details, see [Input\_DeviceInfo](../../structs/input-deviceinfo/document.md). |
| char \*\*name | Pointer to the input device name. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Input\_Result](#input_result) | 
[INPUT\_SUCCESS](#input_result) if the operation is successful;

[INPUT\_PARAMETER\_ERROR](#input_result) if **deviceInfo** or **name** is a null pointer.

 |

#### \[h2\]OH\_Input\_GetCapabilities()

Input\_Result OH\_Input\_GetCapabilities(Input\_DeviceInfo \*deviceInfo, int32\_t \*capabilities)

**Description**

Obtains the capabilities of an input device, for example, a touchscreen, touchpad, or keyboard.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Since**: 13

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [Input\_DeviceInfo](../../structs/input-deviceinfo/document.md) \*deviceInfo | Input device information. For details, see [Input\_DeviceInfo](../../structs/input-deviceinfo/document.md). |
| int32\_t \*capabilities | Pointer to the capability information of the input device. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Input\_Result](#input_result) | 
[INPUT\_SUCCESS](#input_result) if the operation is successful;

[INPUT\_PARAMETER\_ERROR](#input_result) if **deviceInfo** or **capabilities** is a null pointer.

 |

#### \[h2\]OH\_Input\_GetDeviceVersion()

Input\_Result OH\_Input\_GetDeviceVersion(Input\_DeviceInfo \*deviceInfo, int32\_t \*version)

**Description**

Obtains the version information of an input device.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Since**: 13

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [Input\_DeviceInfo](../../structs/input-deviceinfo/document.md) \*deviceInfo | Input device information. For details, see [Input\_DeviceInfo](../../structs/input-deviceinfo/document.md). |
| int32\_t \*version | Pointer to the version information of the input device. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Input\_Result](#input_result) | 
[INPUT\_SUCCESS](#input_result) if the operation is successful;

[INPUT\_PARAMETER\_ERROR](#input_result) if **deviceInfo** or **version** is a null pointer.

 |

#### \[h2\]OH\_Input\_GetDeviceProduct()

Input\_Result OH\_Input\_GetDeviceProduct(Input\_DeviceInfo \*deviceInfo, int32\_t \*product)

**Description**

Obtains the product information of an input device.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Since**: 13

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [Input\_DeviceInfo](../../structs/input-deviceinfo/document.md) \*deviceInfo | Input device information. For details, see [Input\_DeviceInfo](../../structs/input-deviceinfo/document.md). |
| int32\_t \*product | Pointer to the product information of the input device. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Input\_Result](#input_result) | 
[INPUT\_SUCCESS](#input_result) if the operation is successful;

[INPUT\_PARAMETER\_ERROR](#input_result) if **deviceInfo** or **product** is a null pointer.

 |

#### \[h2\]OH\_Input\_GetDeviceVendor()

Input\_Result OH\_Input\_GetDeviceVendor(Input\_DeviceInfo \*deviceInfo, int32\_t \*vendor)

**Description**

Obtains the vendor information of an input device.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Since**: 13

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [Input\_DeviceInfo](../../structs/input-deviceinfo/document.md) \*deviceInfo | Input device information. For details, see [Input\_DeviceInfo](../../structs/input-deviceinfo/document.md). |
| int32\_t \*vendor | Pointer to the vendor information of the input device. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Input\_Result](#input_result) | 
[INPUT\_SUCCESS](#input_result) if the operation is successful;

[INPUT\_PARAMETER\_ERROR](#input_result) if **deviceInfo** or **vendor** is a null pointer.

 |

#### \[h2\]OH\_Input\_GetDeviceAddress()

Input\_Result OH\_Input\_GetDeviceAddress(Input\_DeviceInfo \*deviceInfo, char \*\*address)

**Description**

Obtains the physical address of an input device.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Since**: 13

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [Input\_DeviceInfo](../../structs/input-deviceinfo/document.md) \*deviceInfo | Input device information. For details, see [Input\_DeviceInfo](../../structs/input-deviceinfo/document.md). |
| char \*\*address | Pointer to the physical address of the input device. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Input\_Result](#input_result) | 
[INPUT\_SUCCESS](#input_result) if the operation is successful;

[INPUT\_PARAMETER\_ERROR](#input_result) if **deviceInfo** or **address** is a null pointer.

 |

#### \[h2\]OH\_Input\_GetFunctionKeyState()

Input\_Result OH\_Input\_GetFunctionKeyState(int32\_t keyCode, int32\_t \*state)

**Description**

Obtains the function key status.

**Since**: 15

**Parameters**

| Parameter | Description |
| :-- | :-- |
| int32\_t keyCode | Function key. Currently, only the **CapsLock** key is supported. The key value is **1**. |
| int32\_t \*state | Function key status. The value **0** indicates that the function key is disabled, and the value **1** indicates that the function key is enabled. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Input\_Result](#input_result) | 
Return value of the **OH\_Input\_GetFunctionKeyState** function.

[INPUT\_SUCCESS](#input_result) if the operation is successful;

[INPUT\_PARAMETER\_ERROR](#input_result) if the parameter is incorrect;

[INPUT\_KEYBOARD\_DEVICE\_NOT\_EXIST](#input_result) if the keyboard device does not exist.

 |

#### \[h2\]OH\_Input\_InjectTouchEvent()

int32\_t OH\_Input\_InjectTouchEvent(const struct Input\_TouchEvent\* touchEvent)

**Description**

Injects a touch event by using coordinates in the relative coordinate system with the upper-left corner of the specified screen as the origin.

This API does not take effect if the event injection permission is not granted.

Since API version 20, you are advised to use [OH\_Input\_RequestInjection](#oh_input_requestinjection) to request the required permission before calling this API. If the status returned by [OH\_Input\_QueryAuthorizedStatus](#oh_input_queryauthorizedstatus) is [AUTHORIZED](#input_injectionstatus), then you can call this API.

**Device behavior differences**: This API can be properly called on PCs/2-in-1 devices, but has no effect on other devices.

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| const struct [Input\_TouchEvent](../../structs/input-touchevent/document.md)\* touchEvent | 
**TouchEvent** object, which can be created through [OH\_Input\_CreateTouchEvent](#oh_input_createtouchevent).

If the **TouchEvent** object is no longer needed, destroy it by calling [OH\_Input\_DestroyTouchEvent](#oh_input_destroytouchevent).

 |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Return value of the **OH\_Input\_InjectTouchEvent** function.

[INPUT\_SUCCESS](#input_result) if the operation is successful;

[INPUT\_PARAMETER\_ERROR](#input_result) if the parameter is incorrect;

[INPUT\_PERMISSION\_DENIED](#input_result) if the permission is denied.

 |

#### \[h2\]OH\_Input\_InjectMouseEvent()

int32\_t OH\_Input\_InjectMouseEvent(const struct Input\_MouseEvent\* mouseEvent)

**Description**

Injects a mouse event by using coordinates in the relative coordinate system with the upper-left corner of the specified screen as the origin.

This API does not take effect if the event injection permission is not granted.

Since API version 20, you are advised to use [OH\_Input\_RequestInjection](#oh_input_requestinjection) to request the required permission before calling this API. If the status returned by [OH\_Input\_QueryAuthorizedStatus](#oh_input_queryauthorizedstatus) is [AUTHORIZED](#input_injectionstatus), then you can call this API.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| const struct [Input\_MouseEvent](../../structs/input-mouseevent/document.md)\* mouseEvent | 
Mouse event object. You can call [OH\_Input\_CreateMouseEvent](#oh_input_createmouseevent) to create a mouse event object.

If the mouse event object is no longer needed, destroy it by calling [OH\_Input\_DestroyMouseEvent](#oh_input_destroymouseevent).

 |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Return value of the **OH\_Input\_InjectTouchEvent** function.

[INPUT\_SUCCESS](#input_result) if the operation is successful;

[INPUT\_PARAMETER\_ERROR](#input_result) if the parameter is incorrect;

[INPUT\_PERMISSION\_DENIED](#input_result) if the permission is denied.

 |

#### \[h2\]OH\_Input\_GetMouseEventDisplayId()

int32\_t OH\_Input\_GetMouseEventDisplayId(const struct Input\_MouseEvent\* mouseEvent)

**Description**

Obtains the screen ID of a mouse event.

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Since**: 15

**Parameters**

| Parameter | Description |
| :-- | :-- |
| const struct [Input\_MouseEvent](../../structs/input-mouseevent/document.md)\* mouseEvent | 
Mouse event object. You can call [OH\_Input\_CreateMouseEvent](#oh_input_createmouseevent) to create a mouse event object.

If the mouse event object is no longer needed, destroy it by calling [OH\_Input\_DestroyMouseEvent](#oh_input_destroymouseevent).

 |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | Screen ID if the operation is successful; **\-1** if **mouseEvent** is null. |

#### \[h2\]OH\_Input\_QueryMaxTouchPoints()

Input\_Result OH\_Input\_QueryMaxTouchPoints(int32\_t \*count)

**Description**

Queries the maximum number of touch points supported by the device.

**Since**: 20

**Parameters**

| Parameter | Description |
| :-- | :-- |
| int32\_t \*count | Maximum number of touch points supported by the device. The value range is \[0, 10\]. The value **\-1** indicates that the number of touch points is unknown. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Input\_Result](#input_result) | 
Return value of the **OH\_Input\_QueryMaxTouchPoints** function.

[INPUT\_SUCCESS](#input_result) if the operation is successful;

[INPUT\_PARAMETER\_ERROR](#input_result) if the parameter verification fails.

 |

#### \[h2\]OH\_Input\_InjectMouseEventGlobal()

int32\_t OH\_Input\_InjectMouseEventGlobal(const struct Input\_MouseEvent\* mouseEvent)

**Description**

Injects a mouse event by using coordinates in the global coordinate system with the upper-left corner of the primary screen as the origin.

This API does not take effect if the event injection permission is not granted.

You are advised to use [OH\_Input\_RequestInjection](#oh_input_requestinjection) to request the required permission before calling this API. If the status returned by [OH\_Input\_QueryAuthorizedStatus](#oh_input_queryauthorizedstatus) is [AUTHORIZED](#input_injectionstatus), then you can call this API.

**Since**: 20

**Parameters**

| Parameter | Description |
| :-- | :-- |
| const struct [Input\_MouseEvent](../../structs/input-mouseevent/document.md)\* mouseEvent | 
Mouse event object. You can call [OH\_Input\_CreateMouseEvent](#oh_input_createmouseevent) to create a mouse event object.

If the mouse event object is no longer needed, destroy it by calling [OH\_Input\_DestroyMouseEvent](#oh_input_destroymouseevent).

 |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Return value of the **OH\_Input\_InjectMouseEventGlobal** function.

[INPUT\_SUCCESS](#input_result) if the operation is successful;

[INPUT\_PARAMETER\_ERROR](#input_result) if the parameter is incorrect;

[INPUT\_PERMISSION\_DENIED](#input_result) if the permission is denied.

 |

#### \[h2\]OH\_Input\_SetMouseEventGlobalX()

void OH\_Input\_SetMouseEventGlobalX(struct Input\_MouseEvent\* mouseEvent, int32\_t globalX)

**Description**

Sets the X coordinate of the mouse event in the global coordinate system with the upper-left corner of the primary screen as the origin.

**Since**: 20

**Parameters**

| Parameter | Description |
| :-- | :-- |
| const struct [Input\_MouseEvent](../../structs/input-mouseevent/document.md)\* mouseEvent | 
Mouse event object. You can call [OH\_Input\_CreateMouseEvent](#oh_input_createmouseevent) to create a mouse event object.

If the mouse event object is no longer needed, destroy it by calling [OH\_Input\_DestroyMouseEvent](#oh_input_destroymouseevent).

 |
| int32\_t globalX | X coordinate of the mouse event in the global coordinate system with the upper-left corner of the primary screen as the origin. |

#### \[h2\]OH\_Input\_GetMouseEventGlobalX()

int32\_t OH\_Input\_GetMouseEventGlobalX(const struct Input\_MouseEvent\* mouseEvent)

**Description**

Obtains the X coordinate of the mouse event in the global coordinate system with the upper-left corner of the primary screen as the origin.

**Since**: 20

**Parameters**

| Parameter | Description |
| :-- | :-- |
| const struct [Input\_MouseEvent](../../structs/input-mouseevent/document.md)\* mouseEvent | 
Mouse event object. You can call [OH\_Input\_CreateMouseEvent](#oh_input_createmouseevent) to create a mouse event object.

If the mouse event object is no longer needed, destroy it by calling [OH\_Input\_DestroyMouseEvent](#oh_input_destroymouseevent).

 |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | X coordinate of the mouse event in the global coordinate system with the upper-left corner of the primary screen as the origin. |

#### \[h2\]OH\_Input\_SetMouseEventGlobalY()

void OH\_Input\_SetMouseEventGlobalY(struct Input\_MouseEvent\* mouseEvent, int32\_t globalY)

**Description**

Sets the Y coordinate of the mouse event in the global coordinate system with the upper-left corner of the primary screen as the origin.

**Since**: 20

**Parameters**

| Parameter | Description |
| :-- | :-- |
| const struct [Input\_MouseEvent](../../structs/input-mouseevent/document.md)\* mouseEvent | 
Mouse event object. You can call [OH\_Input\_CreateMouseEvent](#oh_input_createmouseevent) to create a mouse event object.

If the mouse event object is no longer needed, destroy it by calling [OH\_Input\_DestroyMouseEvent](#oh_input_destroymouseevent).

 |
| int32\_t globalY | Y coordinate of the mouse event in the global coordinate system with the upper-left corner of the primary screen as the origin. |

#### \[h2\]OH\_Input\_GetMouseEventGlobalY()

int32\_t OH\_Input\_GetMouseEventGlobalY(const struct Input\_MouseEvent\* mouseEvent)

**Description**

Obtains the Y coordinate of the mouse event in the global coordinate system with the upper-left corner of the primary screen as the origin.

**Since**: 20

**Parameters**

| Parameter | Description |
| :-- | :-- |
| const struct [Input\_MouseEvent](../../structs/input-mouseevent/document.md)\* mouseEvent | 
Mouse event object. You can call [OH\_Input\_CreateMouseEvent](#oh_input_createmouseevent) to create a mouse event object.

If the mouse event object is no longer needed, destroy it by calling [OH\_Input\_DestroyMouseEvent](#oh_input_destroymouseevent).

 |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | Y coordinate of the mouse event in the global coordinate system with the upper-left corner of the primary screen as the origin. |

#### \[h2\]OH\_Input\_InjectTouchEventGlobal()

int32\_t OH\_Input\_InjectTouchEventGlobal(const struct Input\_TouchEvent\* touchEvent)

**Description**

Injects a touch event by using coordinates in the global coordinate system with the upper-left corner of the primary screen as the origin.

This API does not take effect if the event injection permission is not granted.

You are advised to use [OH\_Input\_RequestInjection](#oh_input_requestinjection) to request the required permission before calling this API. If the status returned by [OH\_Input\_QueryAuthorizedStatus](#oh_input_queryauthorizedstatus) is [AUTHORIZED](#input_injectionstatus), then you can call this API.

**Since**: 20

**Parameters**

| Parameter | Description |
| :-- | :-- |
| const struct [Input\_TouchEvent](../../structs/input-touchevent/document.md)\* touchEvent | 
**TouchEvent** object, which can be created through [OH\_Input\_CreateTouchEvent](#oh_input_createtouchevent).

If the **TouchEvent** object is no longer needed, destroy it by calling [OH\_Input\_DestroyTouchEvent](#oh_input_destroytouchevent).

 |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Return value of the **OH\_Input\_InjectTouchEventGlobal** function.

[INPUT\_SUCCESS](#input_result) if the operation is successful;

[INPUT\_PARAMETER\_ERROR](#input_result) if the parameter is incorrect;

[INPUT\_PERMISSION\_DENIED](#input_result) if the permission is denied.

 |

#### \[h2\]OH\_Input\_SetTouchEventGlobalX()

void OH\_Input\_SetTouchEventGlobalX(struct Input\_TouchEvent\* touchEvent, int32\_t globalX)

**Description**

Sets the X coordinate of the touch event in the global coordinate system with the upper-left corner of the primary screen as the origin.

**Since**: 20

**Parameters**

| Parameter | Description |
| :-- | :-- |
| const struct [Input\_TouchEvent](../../structs/input-touchevent/document.md)\* touchEvent | 
**TouchEvent** object, which can be created through [OH\_Input\_CreateTouchEvent](#oh_input_createtouchevent).

If the **TouchEvent** object is no longer needed, destroy it by calling [OH\_Input\_DestroyTouchEvent](#oh_input_destroytouchevent).

 |
| int32\_t globalX | X coordinate of the touch event in the global coordinate system with the upper-left corner of the primary screen as the origin. |

#### \[h2\]OH\_Input\_GetTouchEventGlobalX()

int32\_t OH\_Input\_GetTouchEventGlobalX(const struct Input\_TouchEvent\* touchEvent)

**Description**

Obtains the X coordinate of the touch event in the global coordinate system with the upper-left corner of the primary screen as the origin.

**Since**: 20

**Parameters**

| Parameter | Description |
| :-- | :-- |
| const struct [Input\_TouchEvent](../../structs/input-touchevent/document.md)\* touchEvent | 
**TouchEvent** object, which can be created through [OH\_Input\_CreateTouchEvent](#oh_input_createtouchevent).

If the **TouchEvent** object is no longer needed, destroy it by calling [OH\_Input\_DestroyTouchEvent](#oh_input_destroytouchevent).

 |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | X coordinate of the touch event in the global coordinate system with the upper-left corner of the primary screen as the origin. |

#### \[h2\]OH\_Input\_SetTouchEventGlobalY()

void OH\_Input\_SetTouchEventGlobalY(struct Input\_TouchEvent\* touchEvent, int32\_t globalY)

**Description**

Sets the Y coordinate of the touch event in the global coordinate system with the upper-left corner of the primary screen as the origin.

**Since**: 20

**Parameters**

| Parameter | Description |
| :-- | :-- |
| const struct [Input\_TouchEvent](../../structs/input-touchevent/document.md)\* touchEvent | 
**TouchEvent** object, which can be created through [OH\_Input\_CreateTouchEvent](#oh_input_createtouchevent).

If the **TouchEvent** object is no longer needed, destroy it by calling [OH\_Input\_DestroyTouchEvent](#oh_input_destroytouchevent).

 |
| int32\_t globalY | Y coordinate of the touch event in the global coordinate system with the upper-left corner of the primary screen as the origin. |

#### \[h2\]OH\_Input\_GetTouchEventGlobalY()

int32\_t OH\_Input\_GetTouchEventGlobalY(const struct Input\_TouchEvent\* touchEvent)

**Description**

Obtains the Y coordinate of the touch event in the global coordinate system with the upper-left corner of the primary screen as the origin.

**Since**: 20

**Parameters**

| Parameter | Description |
| :-- | :-- |
| const struct [Input\_TouchEvent](../../structs/input-touchevent/document.md)\* touchEvent | 
**TouchEvent** object, which can be created through [OH\_Input\_CreateTouchEvent](#oh_input_createtouchevent).

If the **TouchEvent** object is no longer needed, destroy it by calling [OH\_Input\_DestroyTouchEvent](#oh_input_destroytouchevent).

 |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | Y coordinate of the touch event in the global coordinate system with the upper-left corner of the primary screen as the origin. |

#### \[h2\]OH\_Input\_SetAxisEventGlobalX()

Input\_Result OH\_Input\_SetAxisEventGlobalX(struct Input\_AxisEvent\* axisEvent, int32\_t globalX)

**Description**

Sets the X coordinate of the axis event in the global coordinate system with the upper-left corner of the primary screen as the origin.

**Since**: 20

**Parameters**

| Parameter | Description |
| :-- | :-- |
| const [Input\_AxisEvent](../../structs/input-axisevent/document.md)\* axisEvent | 
Axis event object. You can call [OH\_Input\_CreateAxisEvent](#oh_input_createaxisevent) to create an axis event object.

If the axis event object is no longer needed, destroy it by calling [OH\_Input\_DestroyAxisEvent](#oh_input_destroyaxisevent).

 |
| int32\_t globalX | X coordinate of the axis event in the global coordinate system with the upper-left corner of the primary screen as the origin. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Input\_Result](#input_result) | 
[INPUT\_SUCCESS](#input_result) if the operation is successful;

[INPUT\_PARAMETER\_ERROR](#input_result) if **axisEvent** is a null pointer.

 |

#### \[h2\]OH\_Input\_GetAxisEventGlobalX()

Input\_Result OH\_Input\_GetAxisEventGlobalX(const Input\_AxisEvent\* axisEvent, int32\_t\* globalX)

**Description**

Obtains the X coordinate of the axis event in the global coordinate system with the upper-left corner of the primary screen as the origin.

**Since**: 20

**Parameters**

| Parameter | Description |
| :-- | :-- |
| const [Input\_AxisEvent](../../structs/input-axisevent/document.md)\* axisEvent | 
Axis event object. You can call [OH\_Input\_CreateAxisEvent](#oh_input_createaxisevent) to create an axis event object.

If the axis event object is no longer needed, destroy it by calling [OH\_Input\_DestroyAxisEvent](#oh_input_destroyaxisevent).

 |
| int32\_t\* globalX | X coordinate of the axis event in the global coordinate system with the upper-left corner of the primary screen as the origin. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Input\_Result](#input_result) | 
[INPUT\_SUCCESS](#input_result) if the operation is successful;

[INPUT\_PARAMETER\_ERROR](#input_result) if **axisEvent** or **globalX** is a null pointer.

 |

#### \[h2\]OH\_Input\_SetAxisEventGlobalY()

Input\_Result OH\_Input\_SetAxisEventGlobalY(struct Input\_AxisEvent\* axisEvent, int32\_t globalY)

**Description**

Sets the Y coordinate of the axis event in the global coordinate system with the upper-left corner of the primary screen as the origin.

**Since**: 20

**Parameters**

| Parameter | Description |
| :-- | :-- |
| const [Input\_AxisEvent](../../structs/input-axisevent/document.md)\* axisEvent | 
Axis event object. You can call [OH\_Input\_CreateAxisEvent](#oh_input_createaxisevent) to create an axis event object.

If the axis event object is no longer needed, destroy it by calling [OH\_Input\_DestroyAxisEvent](#oh_input_destroyaxisevent).

 |
| int32\_t globalY | Y coordinate of the axis event in the global coordinate system with the upper-left corner of the primary screen as the origin. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Input\_Result](#input_result) | 
[INPUT\_SUCCESS](#input_result) if the operation is successful;

[INPUT\_PARAMETER\_ERROR](#input_result) if **axisEvent** is a null pointer.

 |

#### \[h2\]OH\_Input\_GetAxisEventGlobalY()

Input\_Result OH\_Input\_GetAxisEventGlobalY(const Input\_AxisEvent\* axisEvent, int32\_t\* globalY)

**Description**

Obtains the Y coordinate of the axis event in the global coordinate system with the upper-left corner of the primary screen as the origin.

**Since**: 20

**Parameters**

| Parameter | Description |
| :-- | :-- |
| const [Input\_AxisEvent](../../structs/input-axisevent/document.md)\* axisEvent | 
Axis event object. You can call [OH\_Input\_CreateAxisEvent](#oh_input_createaxisevent) to create an axis event object.

If the axis event object is no longer needed, destroy it by calling [OH\_Input\_DestroyAxisEvent](#oh_input_destroyaxisevent).

 |
| int32\_t\* globalY | Y coordinate of the axis event in the global coordinate system with the upper-left corner of the primary screen as the origin. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Input\_Result](#input_result) | 
[INPUT\_SUCCESS](#input_result) if the operation is successful;

[INPUT\_PARAMETER\_ERROR](#input_result) if **axisEvent** or **globalY** is a null pointer.

 |

#### \[h2\]OH\_Input\_GetPointerLocation()

Input\_Result OH\_Input\_GetPointerLocation(int32\_t \*displayId, double \*displayX, double \*displayY)

**Description**

Obtains the coordinates of the mouse pointer on the current screen.

**Device behavior differences**: This API can be properly called on devices other than wearables. If it is called on wearables, error code 3900010 is returned.

**Since**: 20

**Parameters**

| Parameter | Description |
| :-- | :-- |
| int32\_t \*displayId | Screen ID of the current screen. |
| double \*displayX | X coordinate of the mouse pointer on the screen. |
| double \*displayY | Y coordinate of the mouse pointer on the screen. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Input\_Result](#input_result) | 
Return value of the **GetPointerLocation** function.

[INPUT\_SUCCESS](#input_result) if the operation is successful;

[INPUT\_PARAMETER\_ERROR](#input_result) if the parameter is incorrect;

[INPUT\_SERVICE\_EXCEPTION](#input_result) if a service exception occurs;

[INPUT\_APP\_NOT\_FOCUSED](#input_result) if the current application is not in focus;

[INPUT\_DEVICE\_NO\_POINTER](#input_result) if no mouse device is available.

 |

#### \[h2\]OH\_Input\_GetKeyEventId()

Input\_Result OH\_Input\_GetKeyEventId(const struct Input\_KeyEvent\* keyEvent, int32\_t\* eventId)

**Description**

Obtains the ID of a key event.

**Since**: 21

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [Input\_KeyEvent](../../structs/input-keyevent/document.md)\* keyEvent | 
**KeyEvent** object, which can be created through [OH\_Input\_CreateKeyEvent](#oh_input_createkeyevent).

If the key event object is no longer needed, destroy it by calling [OH\_Input\_DestroyKeyEvent](#oh_input_destroykeyevent).

 |
| int32\_t\* eventId | ID of the key event. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Input\_Result](#input_result) | 
Return value of the **OH\_Input\_GetKeyEventId** function.

[INPUT\_SUCCESS](#input_result) if the operation is successful;

[INPUT\_PARAMETER\_ERROR](#input_result) if the parameter verification fails.

 |

#### \[h2\]OH\_Input\_AddKeyEventHook()

Input\_Result OH\_Input\_AddKeyEventHook(Input\_KeyEventCallback callback)

**Description**

Adds a hook function for key event interception.

You can call [OH\_Input\_RemoveKeyEventHook](#oh_input_removekeyeventhook) to remove a hook function that has been added. Multiple hook functions can be set for an application, but only one hook function can be set for a process. The most recently added hook function has a higher priority.

Before using this API, go to Settings > Privacy & security > Permission manager on the device and enable the permission for Input Assistance. This permission is available only for PCs/2-in-1 devices and tablets.

**Required permissions**: ohos.permission.HOOK\_KEY\_EVENT

**Device behavior differences**: This API can be properly called on devices other than wearables. If it is called on wearables, error code 801 is returned.

**Since**: 21

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [Input\_KeyEventCallback](#input_keyeventcallback) callback | Hook function, which is used to intercept all key events to be distributed. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Input\_Result](#input_result) | 
Return value of the **OH\_Input\_AddKeyEventHook** function.

[INPUT\_SUCCESS](#input_result) if the operation is successful;

[INPUT\_PARAMETER\_ERROR](#input_result) if the parameter verification fails;

[INPUT\_DEVICE\_NOT\_SUPPORTED](#input_result) if the function is not supported.

[INPUT\_PERMISSION\_DENIED](#input_result) if the permission verification fails;

[INPUT\_REPEAT\_INTERCEPTOR](#input_result) if the hook function is set repeatedly (only one hook function can be set for a process);

[INPUT\_SERVICE\_EXCEPTION](#input_result) if the service is abnormal.

 |

#### \[h2\]OH\_Input\_RemoveKeyEventHook()

Input\_Result OH\_Input\_RemoveKeyEventHook(Input\_KeyEventCallback callback)

**Description**

Removes the hook function for key event interception.

This API is usually used together with [OH\_Input\_AddKeyEventHook](#oh_input_addkeyeventhook).

**Since**: 21

**Device behavior differences**: This API can be properly called on devices other than wearables. If it is called on wearables, error code 801 is returned.

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [Input\_KeyEventCallback](#input_keyeventcallback) callback | Hook function, which is used to intercept all key events to be distributed. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Input\_Result](#input_result) | 
Return value of the **OH\_Input\_RemoveKeyEventHook** function.

[INPUT\_SUCCESS](#input_result) if the operation is successful; (if a hook is not added, a success message is also returned when the hook is removed);

[INPUT\_PARAMETER\_ERROR](#input_result) if the parameter verification fails;

[INPUT\_SERVICE\_EXCEPTION](#input_result) if the service is abnormal.

 |

#### \[h2\]OH\_Input\_DispatchToNextHandler()

Input\_Result OH\_Input\_DispatchToNextHandler(int32\_t eventId)

**Description**

Redispatches key events.

Only key events intercepted by the hook function can be redispatched, and these events must maintain the original priority sequence.

After this API is called, key events will be redispatched within 3 seconds. If the redispatch is not completed within 3 seconds, [INPUT\_PARAMETER\_ERROR](#input_result) is reported.

Successful redispatch requires correct mapping of events. If one or more [KEY\_ACTION\_DOWN](#input_keyeventaction) events are redispatched, the [KEY\_ACTION\_UP](#input_keyeventaction) or [KEY\_ACTION\_CANCEL](#input_keyeventaction) event can be redispatched.

If only the [KEY\_ACTION\_UP](#input_keyeventaction) or [KEY\_ACTION\_CANCEL](#input_keyeventaction) key events are redispatched, the API call is successful, but the dispatch is not actually performed.

If the redispatched event is not intercepted by the hook function, the API call is successful, but the dispatch is not actually performed.

**Device behavior differences**: This API can be properly called on devices other than wearables. If it is called on wearables, error code 801 is returned.

**Since**: 21

**Parameters**

| Parameter | Description |
| :-- | :-- |
| int32\_t eventId | ID of the key event, which can be obtained through [OH\_Input\_GetKeyEventId](#oh_input_getkeyeventid). |

**Return value**

| Type | Description |
| :-- | :-- |
| [Input\_Result](#input_result) | 
Return value of the **OH\_Input\_DispatchToNextHandler** function.

[INPUT\_SUCCESS](#input_result) if the operation is successful;

[INPUT\_PARAMETER\_ERROR](#input_result) if the parameter verification fails; (you can call [OH\_Input\_GetKeyEventId](#oh_input_getkeyeventid) to check whether the input eventId is correct);

[INPUT\_SERVICE\_EXCEPTION](#input_result) if the service is abnormal.

 |

#### \[h2\]OH\_Input\_SetPointerVisible()

Input\_Result OH\_Input\_SetPointerVisible(bool visible)

**Description**

Sets the visible status of the mouse pointer in the current window.

**Device behavior differences**: This API can be properly called on devices other than wearables. If it is called on wearables, error code 801 is returned.

**Since**: 22

**Parameters**

| Parameter | Description |
| :-- | :-- |
| bool visible | Whether the mouse pointer is visible. The value **true** indicates that the mouse pointer is visible, and the value **false** indicates the opposite. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Input\_Result](#input_result) | 
Return value of the **OH\_Input\_SetPointerVisible** function.

[INPUT\_SUCCESS](#input_result) if the operation is successful;

[INPUT\_DEVICE\_NOT\_SUPPORTED](#input_result) if the device is not supported;

[INPUT\_SERVICE\_EXCEPTION](#input_result) if the service is abnormal.

 |

#### \[h2\]OH\_Input\_GetPointerStyle()

Input\_Result OH\_Input\_GetPointerStyle(int32\_t windowId, int32\_t \*pointerStyle)

**Description**

Obtains the mouse pointer style of the specified window.

**Device behavior differences**: This API has no effect on wearables, but can be properly called on other devices.

**Since**: 22

**Parameters**

| Parameter | Description |
| :-- | :-- |
| int32\_t windowId | 
Window ID. The value is an integer greater than or equal to **\-1**. The value **\-1** indicates the global window.

Only the ID of the current window or global window can be specified. If any other ID is specified, the default pointer style of the global window is returned. You can obtain the ID of the current window through [getWindowProperties](../../../../../../application-framework/arkui/arkts-api/window-manager/ohos-window-window/interface-window/document.md#getwindowproperties9).

 |
| int32\_t\* pointerStyle | Mouse pointer style. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Input\_Result](#input_result) | 
Return value of the **OH\_Input\_GetPointerStyle** function.

[INPUT\_SUCCESS](#input_result) if the operation is successful;

[INPUT\_PARAMETER\_ERROR](#input_result) if the parameter verification fails;

[INPUT\_SERVICE\_EXCEPTION](#input_result) if the service is abnormal.

 |

#### \[h2\]OH\_Input\_SetPointerStyle()

Input\_Result OH\_Input\_SetPointerStyle(int32\_t windowId, int32\_t pointerStyle)

**Description**

Sets the mouse pointer style of the specified window.

**Device behavior differences**: This API has no effect on wearables, but can be properly called on other devices.

**Since**: 22

**Parameters**

| Parameter | Description |
| :-- | :-- |
| int32\_t windowId | 
Window ID. The value is an integer greater than or equal to 0.

Only the ID of the current window can be specified. If any other ID is specified, the API call is successful, but the setting does not take effect. You can obtain the ID of the current window through [getWindowProperties](../../../../../../application-framework/arkui/arkts-api/window-manager/ohos-window-window/interface-window/document.md#getwindowproperties9).

 |
| int32\_t pointerStyle | Mouse pointer style. The value is an enumerated value of [Input\_PointerStyle](../oh-pointer-style-h/document.md#input_pointerstyle). |

**Return value**

| Type | Description |
| :-- | :-- |
| [Input\_Result](#input_result) | 
Return value of the **OH\_Input\_SetPointerStyle** function.

[INPUT\_SUCCESS](#input_result) if the operation is successful;

[INPUT\_PARAMETER\_ERROR](#input_result) if the parameter verification fails;

[INPUT\_SERVICE\_EXCEPTION](#input_result) if the service is abnormal.

 |

#### \[h2\]OH\_Input\_CustomCursor\_Create()

Input\_CustomCursor\* OH\_Input\_CustomCursor\_Create(OH\_PixelmapNative\* pixelMap, int32\_t anchorX, int32\_t anchorY)

**Description**

Creates a custom mouse pointer object. You can call [OH\_Input\_CustomCursor\_Destroy](#oh_input_customcursor_destroy) to destroy a custom mouse pointer resource object.

**Since**: 22

**Parameters**

| Parameter | Description |
| :-- | :-- |
| OH\_PixelmapNative\* pixelMap | Pixel map of the custom mouse pointer object. For details, see [OH\_PixelmapNative](../../../../../../media/image-kit/c-apis/structs/oh-pixelmapnative/document.md). The minimum value is the minimum size of the resource image. The maximum value is 256 x 256 px. |
| int32\_t anchorX | Horizontal coordinate of the mouse pointer's focus. The coordinates are subject to the size of the custom mouse pointer. The minimum value is **0** and the maximum value is the maximum width of the resource image, in px. |
| int32\_t anchorY | Vertical coordinate of the mouse pointer's focus. The coordinates are subject to the size of the custom mouse pointer. The minimum value is **0** and the maximum value is the maximum height of the resource image, in px. |

**Return value**

| Type | Description |
| :-- | :-- |
| Input\_CustomCursor\* | [Input\_CustomCursor](../../structs/input-customcursor/document.md) object. The pointer to the custom mouse pointer object is returned if the operation is successful, and a null pointer is returned if an exception occurs. |

#### \[h2\]OH\_Input\_CustomCursor\_Destroy()

void OH\_Input\_CustomCursor\_Destroy(Input\_CustomCursor\*\* customCursor)

**Description**

Destroys a custom mouse pointer object.

**Since**: 22

**Parameters**

| Parameter | Description |
| :-- | :-- |
| Input\_CustomCursor\*\* customCursor | Custom mouse pointer object. For details, see [Input\_CustomCursor](../../structs/input-customcursor/document.md). |

#### \[h2\]OH\_Input\_CustomCursor\_GetPixelMap()

Input\_Result OH\_Input\_CustomCursor\_GetPixelMap(Input\_CustomCursor\* customCursor, OH\_PixelmapNative\*\* pixelMap)

**Description**

Obtains the pixel map of a custom mouse pointer object.

**Since**: 22

**Parameters**

| Parameter | Description |
| :-- | :-- |
| Input\_CustomCursor\* customCursor | Custom mouse pointer object. For details, see [Input\_CustomCursor](../../structs/input-customcursor/document.md). |
| OH\_PixelmapNative\*\* pixelMap | Pixel map of the custom mouse pointer object. For details, see [OH\_PixelmapNative](../../../../../../media/image-kit/c-apis/structs/oh-pixelmapnative/document.md). |

**Return value**

| Type | Description |
| :-- | :-- |
| [Input\_Result](#input_result) | 
Return value of the **OH\_Input\_CustomCursor\_GetPixelMap** function.

[INPUT\_SUCCESS](#input_result) if the operation is successful;

[INPUT\_PARAMETER\_ERROR](#input_result) if the parameter verification fails.

 |

#### \[h2\]OH\_Input\_CustomCursor\_GetAnchor()

Input\_Result OH\_Input\_CustomCursor\_GetAnchor(Input\_CustomCursor\* customCursor, int32\_t\* anchorX, int32\_t\* anchorY)

**Description**

Obtains the focus coordinates of a custom mouse pointer object.

**Since**: 22

**Parameters**

| Parameter | Description |
| :-- | :-- |
| Input\_CustomCursor\* customCursor | Custom mouse pointer object. For details, see [Input\_CustomCursor](../../structs/input-customcursor/document.md). |
| int32\_t\* anchorX | Horizontal coordinate of the custom mouse pointer object's focus, in px. |
| int32\_t\* anchorY | Vertical coordinate of the custom mouse pointer object's focus, in px. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Input\_Result](#input_result) | 
Return value of the **OH\_Input\_CustomCursor\_GetAnchor** function.

[INPUT\_SUCCESS](#input_result) if the operation is successful;

[INPUT\_PARAMETER\_ERROR](#input_result) if the parameter verification fails.

 |

#### \[h2\]OH\_Input\_CursorConfig\_Create()

Input\_CursorConfig\* OH\_Input\_CursorConfig\_Create(bool followSystem)

**Description**

Creates a custom mouse pointer configuration object. You can call [OH\_Input\_CursorConfig\_Destroy](#oh_input_cursorconfig_destroy) to destroy a custom mouse pointer configuration object.

**Since**: 22

**Parameters**

| Parameter | Description |
| :-- | :-- |
| bool followSystem | Whether to adjust the pointer size based on the system setting. The value **true** means to adjust the pointer size based on the system setting, and the value **false** means to use the size of the custom mouse pointer. The adjustable range is \[size of the pointer image, 256 x 256\]. |

**Return value**

| Type | Description |
| :-- | :-- |
| Input\_CursorConfig\* | Custom mouse pointer configuration object. For details, see [Input\_CursorConfig](../../structs/input-cursorconfig/document.md). |

#### \[h2\]OH\_Input\_CursorConfig\_Destroy()

void OH\_Input\_CursorConfig\_Destroy(Input\_CursorConfig\*\* cursorConfig)

**Description**

Destroys a custom mouse pointer configuration object.

**Since**: 22

**Parameters**

| Parameter | Description |
| :-- | :-- |
| Input\_CursorConfig\*\* cursorConfig | Custom mouse pointer configuration object. For details, see [Input\_CursorConfig](../../structs/input-cursorconfig/document.md). |

#### \[h2\]OH\_Input\_CursorConfig\_IsFollowSystem()

Input\_Result OH\_Input\_CursorConfig\_IsFollowSystem(Input\_CursorConfig \*cursorConfig, bool \*followSystem)

**Description**

Queries whether the custom mouse pointer configuration follows the system setting to adjust the pointer size.

**Since**: 22

**Parameters**

| Parameter | Description |
| :-- | :-- |
| Input\_CursorConfig\* cursorConfig | Custom mouse pointer configuration object. For details, see [Input\_CursorConfig](../../structs/input-cursorconfig/document.md). |
| bool\* followSystem | Whether to adjust the pointer size based on the system setting. The value **true** means to adjust the pointer size based on the system setting, and the value **false** means to use the size of custom mouse pointer. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Input\_Result](#input_result) | 
Return value of the **OH\_Input\_CursorConfig\_IsFollowSystem** function.

[INPUT\_SUCCESS](#input_result) if the operation is successful;

[INPUT\_PARAMETER\_ERROR](#input_result) if the parameter verification fails.

 |

#### \[h2\]OH\_Input\_SetCustomCursor()

Input\_Result OH\_Input\_SetCustomCursor(int32\_t windowId, Input\_CustomCursor\* customCursor, Input\_CursorConfig\* cursorConfig)

**Description**

Sets the custom mouse pointer style.

The cursor may be switched back to the system style in the following cases: application window layout change, hot zone switching, page redirection, moving of the cursor out of the window and then back to the window, or moving of the cursor in different areas of the window. In this case, you need to reset the cursor style.

**Device behavior differences**: This API can be properly called on devices other than wearables. If it is called on wearables, error code 801 is returned.

**Since**: 22

**Parameters**

| Parameter | Description |
| :-- | :-- |
| int32\_t windowId | Window ID. The value must be an integer greater than or equal to **0**. Only the pointer style of the current window can be specified. |
| Input\_CustomCursor\* customCursor | Custom mouse pointer object. For details, see [Input\_CustomCursor](../../structs/input-customcursor/document.md). |
| Input\_CursorConfig\* cursorConfig | Custom mouse pointer configuration object. For details, see [Input\_CursorConfig](../../structs/input-cursorconfig/document.md). |

**Return value**

| Type | Description |
| :-- | :-- |
| [Input\_Result](#input_result) | 
Return value of the **OH\_Input\_SetCustomCursor** function.

[INPUT\_SUCCESS](#input_result) if the operation is successful;

[INPUT\_PARAMETER\_ERROR](#input_result) if the parameter verification fails;

[INPUT\_INVALID\_WINDOWID](#input_result) if the window ID is invalid;

[INPUT\_DEVICE\_NOT\_SUPPORTED](#input_result) if the device is not supported;

[INPUT\_SERVICE\_EXCEPTION](#input_result) if the service is abnormal.

 |

#### \[h2\]OH\_Input\_CursorInfo\_Create()

struct Input\_CursorInfo\* OH\_Input\_CursorInfo\_Create()

**Description**

Creates a mouse pointer information object. You can call [OH\_Input\_CursorInfo\_Destroy](#oh_input_cursorinfo_destroy) to destroy a mouse pointer information object.

**Since**: 22

**Return value**

| Type | Description |
| :-- | :-- |
| struct Input\_CursorInfo\* | An [Input\_CursorInfo](../../structs/input-cursorinfo/document.md) object if the operation is successful; a null pointer otherwise (possibly because of a memory allocation failure). |

#### \[h2\]OH\_Input\_CursorInfo\_Destroy()

void OH\_Input\_CursorInfo\_Destroy(Input\_CursorInfo\*\* cursorInfo)

**Description**

Destroys the mouse pointer information object.

**Since**: 22

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [Input\_CursorInfo](../../structs/input-cursorinfo/document.md)\*\* cursorInfo | Mouse pointer information object. |

#### \[h2\]OH\_Input\_CursorInfo\_IsVisible()

Input\_Result OH\_Input\_CursorInfo\_IsVisible(Input\_CursorInfo\* cursorInfo, bool\* visible)

**Description**

Obtains the pointer visible status of the specified mouse pointer information object.

**Since**: 22

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [Input\_CursorInfo](../../structs/input-cursorinfo/document.md)\* cursorInfo | Mouse pointer information object. You can call [OH\_Input\_GetMouseEventCursorInfo](#oh_input_getmouseeventcursorinfo) to query the mouse pointer information of a specified mouse event, or call [OH\_Input\_GetCursorInfo](#oh_input_getcursorinfo) to query the current mouse pointer information. |
| bool\* visible | Visible status of the mouse pointer. The value **true** indicates that the mouse pointer is visible, and the value **false** indicates the opposite. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Input\_Result](#input_result) | 
Return value of the **OH\_Input\_CursorInfo\_IsVisible** function.

[INPUT\_SUCCESS](#input_result) if the operation is successful;

[INPUT\_PARAMETER\_ERROR](#input_result) if the parameter verification fails.

 |

#### \[h2\]OH\_Input\_CursorInfo\_GetStyle()

Input\_Result OH\_Input\_CursorInfo\_GetStyle(Input\_CursorInfo\* cursorInfo, Input\_PointerStyle\* style)

**Description**

Obtains the pointer style of the specified mouse pointer information object.

**Since**: 22

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [Input\_CursorInfo](../../structs/input-cursorinfo/document.md)\* cursorInfo | Mouse pointer information object. You can call [OH\_Input\_GetMouseEventCursorInfo](#oh_input_getmouseeventcursorinfo) to query the mouse pointer information of a specified mouse event, or call [OH\_Input\_GetCursorInfo](#oh_input_getcursorinfo) to query the current mouse pointer information. |
| [Input\_PointerStyle](../oh-pointer-style-h/document.md) | Pointer style. For details, see [Input\_PointerStyle](../oh-pointer-style-h/document.md#input_pointerstyle). |

**Return value**

| Type | Description |
| :-- | :-- |
| [Input\_Result](#input_result) | 
Return value of the **OH\_Input\_CursorInfo\_GetStyle** function.

[INPUT\_SUCCESS](#input_result) if the operation is successful;

[INPUT\_PARAMETER\_ERROR](#input_result) if the parameter verification fails or the pointer is invisible.

 |

#### \[h2\]OH\_Input\_CursorInfo\_GetSizeLevel()

Input\_Result OH\_Input\_CursorInfo\_GetSizeLevel(Input\_CursorInfo\* cursorInfo, int32\_t\* sizeLevel)

**Description**

Obtains the pointer size level of the specified mouse pointer information object.

**Since**: 22

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [Input\_CursorInfo](../../structs/input-cursorinfo/document.md)\* cursorInfo | Mouse pointer information object. You can call [OH\_Input\_GetMouseEventCursorInfo](#oh_input_getmouseeventcursorinfo) to query the mouse pointer information of a specified mouse event, or call [OH\_Input\_GetCursorInfo](#oh_input_getcursorinfo) to query the current mouse pointer information. |
| int32\_t\* sizeLevel | Pointer size level of the mouse pointer information object. The value is an integer ranging from 1 to 7. A larger value indicates a higher pointer size level. The size of the custom pointer [DEVELOPER\_DEFINED\_ICON](../oh-pointer-style-h/document.md#input_pointerstyle) is subject to the actual bitmap size. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Input\_Result](#input_result) | 
Return value of the **OH\_Input\_CursorInfo\_GetSizeLevel** function.

[INPUT\_SUCCESS](#input_result) if the operation is successful;

[INPUT\_PARAMETER\_ERROR](#input_result) if the parameter verification fails or the pointer is invisible.

 |

#### \[h2\]OH\_Input\_CursorInfo\_GetColor()

Input\_Result OH\_Input\_CursorInfo\_GetColor(Input\_CursorInfo\* cursorInfo, uint32\_t\* color)

**Description**

Obtains the pointer color of the specified mouse pointer information object.

**Since**: 22

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [Input\_CursorInfo](../../structs/input-cursorinfo/document.md)\* cursorInfo | Mouse pointer information object. You can call [OH\_Input\_GetMouseEventCursorInfo](#oh_input_getmouseeventcursorinfo) to query the mouse pointer information of a specified mouse event, or call [OH\_Input\_GetCursorInfo](#oh_input_getcursorinfo) to query the current mouse pointer information. |
| uint32\_t\* color | Pointer color of the mouse pointer information object, which is represented by a 32-bit ARGB integer. The size of the custom pointer [DEVELOPER\_DEFINED\_ICON](../oh-pointer-style-h/document.md#input_pointerstyle) is subject to the actual bitmap color. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Input\_Result](#input_result) | 
Return value of the **OH\_Input\_CursorInfo\_GetColor** function.

[INPUT\_SUCCESS](#input_result) if the operation is successful;

[INPUT\_PARAMETER\_ERROR](#input_result) if the parameter verification fails or the pointer is invisible.

 |

#### \[h2\]OH\_Input\_GetMouseEventCursorInfo()

Input\_Result OH\_Input\_GetMouseEventCursorInfo(const struct Input\_MouseEvent\* mouseEvent, Input\_CursorInfo\* cursorInfo)

**Description**

Obtains the mouse pointer information of the mouse event, including the pointer visible status, pointer style, pointer size level, and pointer color.

**Since**: 22

**Parameters**

| Parameter | Description |
| :-- | :-- |
| const [Input\_MouseEvent](../../structs/input-mouseevent/document.md)\* mouseEvent | Mouse event object. You can obtain the mouse event object from the callback of [OH\_Input\_AddMouseEventMonitor](#oh_input_addmouseeventmonitor) or [OH\_Input\_AddInputEventInterceptor](#oh_input_addinputeventinterceptor). |
| [Input\_CursorInfo](../../structs/input-cursorinfo/document.md)\* cursorInfo | Mouse pointer information object. You can call [OH\_Input\_CursorInfo\_Create](#oh_input_cursorinfo_create) to create a mouse pointer information object. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Input\_Result](#input_result) | 
Return value of the **OH\_Input\_GetMouseEventCursorInfo** function.

[INPUT\_SUCCESS](#input_result) if the operation is successful;

[INPUT\_PARAMETER\_ERROR](#input_result) if the parameter verification fails.

 |

#### \[h2\]OH\_Input\_GetCursorInfo()

Input\_Result OH\_Input\_GetCursorInfo(Input\_CursorInfo\* cursorInfo, OH\_PixelmapNative\*\* pixelmap)

**Description**

Obtains the mouse pointer information, including the pointer visible status, pointer style, pointer size level, and pointer color. If the **pixelmap** parameter is not empty and the pointer style is [DEVELOPER\_DEFINED\_ICON](../oh-pointer-style-h/document.md#input_pointerstyle), the **PixelMap** object of the pointer is returned.

**Device behavior differences**: This API has no effect on wearables, but can be properly called on other devices.

**Since**: 22

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [Input\_CursorInfo](../../structs/input-cursorinfo/document.md)\* cursorInfo | Mouse pointer information object. You can call [OH\_Input\_CursorInfo\_Create](#oh_input_cursorinfo_create) to create a mouse pointer information object. |
| [OH\_PixelmapNative](../../../../../../media/image-kit/c-apis/structs/oh-pixelmapnative/document.md)\*\* pixelmap | 
**PixelMap** object. If this parameter is not empty and the pointer is a custom one, the **PixelMap** object of the pointer is returned. Otherwise, the **PixelMap** object is not returned. Firstly, create an **OH\_PixelmapInitializationOptions** object through [OH\_PixelmapInitializationOptions\_Create](../../../../../../media/image-kit/c-apis/header-files/pixelmap-native-h/document.md#oh_pixelmapinitializationoptions_create). Then, set the width to a value greater than **0** through [OH\_PixelmapInitializationOptions\_SetWidth](../../../../../../media/image-kit/c-apis/header-files/pixelmap-native-h/document.md#oh_pixelmapinitializationoptions_setwidth), set the height to a value greater than **0** through [OH\_PixelmapInitializationOptions\_SetHeight](../../../../../../media/image-kit/c-apis/header-files/pixelmap-native-h/document.md#oh_pixelmapinitializationoptions_setheight). Finally, create a **PixelMap** object by calling [OH\_PixelmapNative\_CreateEmptyPixelmap](../../../../../../media/image-kit/c-apis/header-files/pixelmap-native-h/document.md#oh_pixelmapnative_createemptypixelmap) with the **OH\_PixelmapInitializationOptions** object passed in.

When the **PixelMap** object is no longer needed, you need to call [OH\_PixelmapNative\_Release](../../../../../../media/image-kit/c-apis/header-files/pixelmap-native-h/document.md#oh_pixelmapnative_release) to release the object and then call [OH\_PixelmapNative\_Destroy](../../../../../../media/image-kit/c-apis/header-files/pixelmap-native-h/document.md#oh_pixelmapnative_destroy) to destroy it.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [Input\_Result](#input_result) | 
Return value of the **OH\_Input\_GetCursorInfo** function.

[INPUT\_SUCCESS](#input_result) if the operation is successful;

[INPUT\_PARAMETER\_ERROR](#input_result) if the parameter verification fails;

[INPUT\_SERVICE\_EXCEPTION](#input_result) if the service is abnormal.

 |
