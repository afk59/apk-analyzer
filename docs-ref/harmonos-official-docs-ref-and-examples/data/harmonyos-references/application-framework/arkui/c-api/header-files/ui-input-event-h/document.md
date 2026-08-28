# ui\_input\_event.h

#### Overview

Provides ArkUI event definitions on the native side.

**File to include**: <arkui/ui\_input\_event.h>

**Library**: libace\_ndk.z.so

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Since**: 12

**Related module**: [ArkUI\_EventModule](../../modules/arkui-eventmodule/document.md)

**Sample**: [NdkInputEvent](https://gitcode.com/openharmony/applications_app_samples/blob/master/code/DocsSample/ArkUISample/NdkInputEvent), [CoastingAxisEventNDK](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/ArkUISample/CoastingAxisEventNDK)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md) | ArkUI\_UIInputEvent | Defines the UI input event. |
| [ArkUI\_CoastingAxisEvent](../../structs/arkui-coastingaxisevent/document.md) | ArkUI\_CoastingAxisEvent | Defines the coasting axis event. |
| [ArkUI\_TouchTestInfo](../../structs/arkui-touchtestinfo/document.md) | ArkUI\_TouchTestInfo | Defines touch test information. |
| [ArkUI\_TouchTestInfoItem](../../structs/arkui-touchtestinfoitem/document.md) | ArkUI\_TouchTestInfoItem | Defines touch test information items. |
| [ArkUI\_TouchTestInfoItem\*](../../structs/arkui-touchtestinfoitem--00020177/document.md) | ArkUI\_TouchTestInfoItemHandle | Defines the handle of touch test information items. |
| [ArkUI\_TouchTestInfoItemHandle\*](../../structs/arkui-touchtestinfoitemhandle/document.md) | ArkUI\_TouchTestInfoItemArray | Defines the handle array of touch test information items. |

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [ArkUI\_UIInputEvent\_Type](#arkui_uiinputevent_type) | ArkUI\_UIInputEvent\_Type | Enumerates the UI input event types. |
| [anonymous1](#anonymous1) | \- | Enumerates the action types of the input event. |
| [anonymous2](#anonymous2) | \- | Enumerates the tool types of the input event. |
| [anonymous3](#anonymous3) | \- | Enumerates the source types of the input event. |
| [HitTestMode](#hittestmode) | HitTestMode | Enumerates the hit test modes. |
| [anonymous4](#anonymous4) | \- | Enumerates the action types of the mouse event. |
| [anonymous5](#anonymous5) | \- | Enumerates the button types of the mouse event. |
| [ArkUI\_ModifierKeyName](#arkui_modifierkeyname) | ArkUI\_ModifierKeyName | Enumerates the modifier keys. |
| [anonymous6](#anonymous6) | \- | Enumerates the axis types for focus axis events. |
| [ArkUI\_InteractionHand](#arkui_interactionhand) | ArkUI\_InteractionHand | Defines whether the touch event is from the left or right hand. |
| [anonymous7](#anonymous7) | \- | Enumerates the action types for axis events. |
| [anonymous8](#anonymous8) | \- | Enumerates the axis types for axis events. |
| [ArkUI\_CoastingAxisEventPhase](#arkui_coastingaxiseventphase) | ArkUI\_CoastingAxisEventPhase | Enumerates the phases of coasting axis events. |
| [ArkUI\_TouchTestStrategy](#arkui_touchteststrategy) | ArkUI\_TouchTestStrategy | Defines the touch test policy. |

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [int32\_t OH\_ArkUI\_UIInputEvent\_GetType(const ArkUI\_UIInputEvent\* event)](#oh_arkui_uiinputevent_gettype) | Obtains the type of a UI input event. Before accessing an **ArkUI\_UIInputEvent** pointer, use this API to determine the type of the input event. This API returns a value from the [ArkUI\_UIInputEvent\_Type](#arkui_uiinputevent_type) enum. It helps ensure compatibility with subsequent accessors. For example, if the event is a touch event, which is directional, you can use OH\_ArkUI\_UIInputEvent\_GetXXX or OH\_ArkUI\_PointerEvent\_GetXXX for access. Using OH\_ArkUI\_KeyEvent\_GetXXX to access the event may produce undefined behavior. For unsupported event types, this API returns the default value **0**. |
| [int32\_t OH\_ArkUI\_UIInputEvent\_GetAction(const ArkUI\_UIInputEvent\* event)](#oh_arkui_uiinputevent_getaction) | Obtains the action type of an input event. The action type defines the phase of a basic event (for example, start or end) and characterizes its behavior, such as touch down or touch up. Action types are specific to the event category: UI\_TOUCH\_EVENT\_ACTION\_XXX for touch events and UI\_MOUSE\_EVENT\_ACTION\_XXX for mouse events. |
| [int32\_t OH\_ArkUI\_UIInputEvent\_GetSourceType(const ArkUI\_UIInputEvent\* event)](#oh_arkui_uiinputevent_getsourcetype) | Obtains the source type of a UI input event. The source represents the physical device, such as a touchscreen or mouse device, that generates the event. It is defined by the UI\_INPUT\_EVENT\_SOURCE\_TYPE\_XXX enum. This is different from the input tool, which is the device used to interact with the source, for example, a finger or stylus. However, in certain cases, the input source and the input tool can be the same. For example, a mouse device acts as both the source and tool for click events. |
| [int32\_t OH\_ArkUI\_UIInputEvent\_GetToolType(const ArkUI\_UIInputEvent\* event)](#oh_arkui_uiinputevent_gettooltype) | Obtains the tool type of a UI input event. The input tool is the device used to interact with the input source, such as a finger or stylus. These tools themselves do not generate events but can drive the input source device to continuously generate events. The returned type is defined by the enumerated value of UI\_INPUT\_EVENT\_TOOL\_TYPE\_XXX. |
| [int64\_t OH\_ArkUI\_UIInputEvent\_GetEventTime(const ArkUI\_UIInputEvent\* event)](#oh_arkui_uiinputevent_geteventtime) | Obtains the time when a specified UI input event occurs. The unit is ns. |
| [uint32\_t OH\_ArkUI\_PointerEvent\_GetPointerCount(const ArkUI\_UIInputEvent\* event)](#oh_arkui_pointerevent_getpointercount) | Obtains the number of touch points from a pointer event (such as a touch, mouse, or axis event). Pointer events are typically events that carry position information, such as touch events, where the location of the event can be determined. Non-pointer events, such as key events, do not have position information and do not involve touch points, so this API is not applicable to key events. For touch events, this API returns the number of active touch points, for example, fingers on the screen. For mouse and axis events, this API always returns **1**, as they are single-pointer interactions. |
| [int32\_t OH\_ArkUI\_PointerEvent\_GetPointerId(const ArkUI\_UIInputEvent\* event, uint32\_t pointerIndex)](#oh_arkui_pointerevent_getpointerid) | Obtains the unique ID of a touch point from a pointer event (such as a touch, mouse, or axis event). The ID distinguishes between multiple touch points from the same input device. The return value itself does not have any other meaning beyond identifying the touch point. |
| [int32\_t OH\_ArkUI\_PointerEvent\_GetChangedPointerId(const ArkUI\_UIInputEvent\* event, uint32\_t\* pointerIndex)](#oh_arkui_pointerevent_getchangedpointerid) | Obtains the ID of the touch pointer that triggers the current touch event. |
| [float OH\_ArkUI\_PointerEvent\_GetX(const ArkUI\_UIInputEvent\* event)](#oh_arkui_pointerevent_getx) | Obtains the x-coordinate relative to the upper left corner of the current component from a pointer event (such as a touch, mouse, or axis event). |
| [float OH\_ArkUI\_PointerEvent\_GetXByIndex(const ArkUI\_UIInputEvent\* event, uint32\_t pointerIndex)](#oh_arkui_pointerevent_getxbyindex) | Obtains the x-coordinate of a specific touch point relative to the upper left corner of the current component from a pointer event (such as a touch, mouse, or axis event). For mouse and axis events, this API returns the default value of **0.0f** if the given index is greater than 0. |
| [float OH\_ArkUI\_PointerEvent\_GetY(const ArkUI\_UIInputEvent\* event)](#oh_arkui_pointerevent_gety) | Obtains the y-coordinate relative to the upper left corner of the current component from a pointer event (such as a touch, mouse, or axis event). |
| [float OH\_ArkUI\_PointerEvent\_GetYByIndex(const ArkUI\_UIInputEvent\* event, uint32\_t pointerIndex)](#oh_arkui_pointerevent_getybyindex) | Obtains the y-coordinate of a specific touch point relative to the upper left corner of the current component from a pointer event (such as a touch, mouse, or axis event). For mouse and axis events, this API returns the default value of **0.0f** if the given index is greater than 0. |
| [float OH\_ArkUI\_PointerEvent\_GetWindowX(const ArkUI\_UIInputEvent\* event)](#oh_arkui_pointerevent_getwindowx) | Obtains the x-coordinate relative to the upper left corner of the current application window from a pointer event (such as a touch, mouse, or axis event). |
| [float OH\_ArkUI\_PointerEvent\_GetWindowXByIndex(const ArkUI\_UIInputEvent\* event, uint32\_t pointerIndex)](#oh_arkui_pointerevent_getwindowxbyindex) | Obtains the x-coordinate of a specific touch point relative to the upper left corner of the current application window from a pointer event (such as a touch, mouse, or axis event). For mouse and axis events, this API returns the default value of **0.0f** if the given index is greater than 0. |
| [float OH\_ArkUI\_PointerEvent\_GetWindowY(const ArkUI\_UIInputEvent\* event)](#oh_arkui_pointerevent_getwindowy) | Obtains the y-coordinate relative to the upper left corner of the current application window from a pointer event (such as a touch, mouse, or axis event). |
| [float OH\_ArkUI\_PointerEvent\_GetWindowYByIndex(const ArkUI\_UIInputEvent\* event, uint32\_t pointerIndex)](#oh_arkui_pointerevent_getwindowybyindex) | Obtains the y-coordinate of a specific touch point relative to the upper left corner of the current application window from a pointer event (such as a touch, mouse, or axis event). For mouse and axis events, this API returns the default value of **0.0f** if the given index is greater than 0. |
| [float OH\_ArkUI\_PointerEvent\_GetDisplayX(const ArkUI\_UIInputEvent\* event)](#oh_arkui_pointerevent_getdisplayx) | Obtains the x-coordinate relative to the upper left corner of the current screen from a pointer event (such as a touch, mouse, or axis event). |
| [float OH\_ArkUI\_PointerEvent\_GetDisplayXByIndex(const ArkUI\_UIInputEvent\* event, uint32\_t pointerIndex)](#oh_arkui_pointerevent_getdisplayxbyindex) | Obtains the x-coordinate of a specific touch point relative to the upper left corner of the current screen from a pointer event (such as a touch, mouse, or axis event). For mouse and axis events, this API returns the default value of **0.0f** if the given index is greater than 0. |
| [float OH\_ArkUI\_PointerEvent\_GetDisplayY(const ArkUI\_UIInputEvent\* event)](#oh_arkui_pointerevent_getdisplayy) | Obtains the y-coordinate relative to the upper left corner of the current screen from a pointer event (such as a touch, mouse, or axis event). |
| [float OH\_ArkUI\_PointerEvent\_GetDisplayYByIndex(const ArkUI\_UIInputEvent\* event, uint32\_t pointerIndex)](#oh_arkui_pointerevent_getdisplayybyindex) | Obtains the y-coordinate of a specific touch point relative to the upper left corner of the current screen from a pointer event (such as a touch, mouse, or axis event). For mouse and axis events, this API returns the default value of **0.0f** if the given index is greater than 0. |
| [float OH\_ArkUI\_PointerEvent\_GetGlobalDisplayX(const ArkUI\_UIInputEvent\* event)](#oh_arkui_pointerevent_getglobaldisplayx) | Obtains the x-coordinate relative to the global display from a pointer event (such as a touch, mouse, or axis event). The position information can be obtained only from a [ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md) event. |
| [float OH\_ArkUI\_PointerEvent\_GetGlobalDisplayXByIndex(const ArkUI\_UIInputEvent\* event, uint32\_t pointerIndex)](#oh_arkui_pointerevent_getglobaldisplayxbyindex) | Obtains the x-coordinate relative to the global display from a pointer event (such as a touch, mouse, or axis event). Position information can only be obtained from UI input events. For mouse and axis events, if the provided **pointerIndex** is greater than 0, this API always returns the default value **0.0f**. |
| [float OH\_ArkUI\_PointerEvent\_GetGlobalDisplayY(const ArkUI\_UIInputEvent\* event)](#oh_arkui_pointerevent_getglobaldisplayy) | Obtains the y-coordinate relative to the global display from a pointer event (such as a touch, mouse, or axis event). The position information can be obtained only from a [ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md) event. |
| [float OH\_ArkUI\_PointerEvent\_GetGlobalDisplayYByIndex(const ArkUI\_UIInputEvent\* event, uint32\_t pointerIndex)](#oh_arkui_pointerevent_getglobaldisplayybyindex) | Obtains the y-coordinate relative to the global display from a pointer event (such as a touch, mouse, or axis event). Position information can only be obtained from UI input events. For mouse and axis events, if the provided **pointerIndex** is greater than 0, this API always returns the default value **0.0f**. |
| [float OH\_ArkUI\_PointerEvent\_GetPressure(const ArkUI\_UIInputEvent\* event, uint32\_t pointerIndex)](#oh_arkui_pointerevent_getpressure) | Obtains the pressure applied to the touchscreen from a pointer event (such as a touch event). |
| [float OH\_ArkUI\_PointerEvent\_GetTiltX(const ArkUI\_UIInputEvent\* event, uint32\_t pointerIndex)](#oh_arkui_pointerevent_gettiltx) | Obtains the angle relative to the YZ plane from a pointer event (for example, a touch event). The value range is \[-90, 90\], in deg. A positive value indicates a rightward tilt. This API is applicable only to stylus-based touch events from devices that support tilt angle reporting. |
| [float OH\_ArkUI\_PointerEvent\_GetTiltY(const ArkUI\_UIInputEvent\* event, uint32\_t pointerIndex)](#oh_arkui_pointerevent_gettilty) | Obtains the angle relative to the XZ plane from a pointer event (for example, a touch event). The value range is \[-90, 90\], in deg. A positive value indicates a downward tilt. This API is applicable only to stylus-based touch events from devices that support tilt angle reporting. |
| [int32\_t OH\_ArkUI\_PointerEvent\_GetRollAngle(const ArkUI\_UIInputEvent\* event, double\* rollAngle)](#oh_arkui_pointerevent_getrollangle) | Obtains the rotation angle of the stylus around the z-axis from a UI input event. |
| [float OH\_ArkUI\_PointerEvent\_GetTouchAreaWidth(const ArkUI\_UIInputEvent\* event, uint32\_t pointerIndex)](#oh_arkui_pointerevent_gettouchareawidth) | Obtains the width of the touch area for a pointer event. This API is applicable only to finger-based touch events, and the return value typically represents the radius of a circular touch area. |
| [float OH\_ArkUI\_PointerEvent\_GetTouchAreaHeight(const ArkUI\_UIInputEvent\* event, uint32\_t pointerIndex)](#oh_arkui_pointerevent_gettouchareaheight) | Obtains the height of the touch area for a pointer event. This API is applicable only to finger-based touch events, and the return value typically represents the radius of a circular touch area. |
| [int32\_t OH\_ArkUI\_PointerEvent\_GetInteractionHand(const ArkUI\_UIInputEvent \*event, ArkUI\_InteractionHand \*hand)](#oh_arkui_pointerevent_getinteractionhand) | Checks whether an event is triggered by a left-hand or right-hand tap. This API is only effective on some touch devices. |
| [int32\_t OH\_ArkUI\_PointerEvent\_GetInteractionHandByIndex(const ArkUI\_UIInputEvent \*event, int32\_t pointerIndex, ArkUI\_InteractionHand \*hand)](#oh_arkui_pointerevent_getinteractionhandbyindex) | Checks whether an event is triggered by a left-hand or right-hand tap. This API is only effective on some touch devices. |
| [uint32\_t OH\_ArkUI\_PointerEvent\_GetHistorySize(const ArkUI\_UIInputEvent\* event)](#oh_arkui_pointerevent_gethistorysize) | Obtains the number of historical events from a pointer event (such as a touch event). A historical event is the raw event that occurs between the current event and the previous event. This API is applicable only to the move phase (touch or mouse movement) of a pointer event. If this API is called in other states, the default value **0** is returned. |
| [int64\_t OH\_ArkUI\_PointerEvent\_GetHistoryEventTime(const ArkUI\_UIInputEvent\* event, uint32\_t historyIndex)](#oh_arkui_pointerevent_gethistoryeventtime) | Obtains the occurrence time of a historical event from a pointer event (such as a touch, mouse, or axis event). |
| [uint32\_t OH\_ArkUI\_PointerEvent\_GetHistoryPointerCount(const ArkUI\_UIInputEvent\* event, uint32\_t historyIndex)](#oh_arkui_pointerevent_gethistorypointercount) | Obtains the number of touch points in a specific historical event from a pointer event (such as a touch, mouse, or axis event). |
| [int32\_t OH\_ArkUI\_PointerEvent\_GetHistoryPointerId(const ArkUI\_UIInputEvent\* event, uint32\_t pointerIndex, uint32\_t historyIndex)](#oh_arkui_pointerevent_gethistorypointerid) | Obtains the unique ID of a touch point from a historical event of a pointer event (such as a touch event). The ID distinguishes between multiple touch points from the same input device. The return value itself does not have any other meaning beyond identifying the touch point. |
| [float OH\_ArkUI\_PointerEvent\_GetHistoryX(const ArkUI\_UIInputEvent\* event, uint32\_t pointerIndex, uint32\_t historyIndex)](#oh_arkui_pointerevent_gethistoryx) | Obtains the x-coordinate of a specific touch point in a specific historical event relative to the upper left corner of the current component from a pointer event (such as a touch, mouse, or axis event). |
| [float OH\_ArkUI\_PointerEvent\_GetHistoryY(const ArkUI\_UIInputEvent\* event, uint32\_t pointerIndex, uint32\_t historyIndex)](#oh_arkui_pointerevent_gethistoryy) | Obtains the y-coordinate of a specific touch point in a specific historical event relative to the upper left corner of the current component from a pointer event (such as a touch, mouse, or axis event). |
| [float OH\_ArkUI\_PointerEvent\_GetHistoryWindowX(const ArkUI\_UIInputEvent\* event, uint32\_t pointerIndex, uint32\_t historyIndex)](#oh_arkui_pointerevent_gethistorywindowx) | Obtains the x-coordinate of a specific touch point in a specific historical event relative to the upper left corner of the current application window from a pointer event (such as a touch, mouse, or axis event). |
| [float OH\_ArkUI\_PointerEvent\_GetHistoryWindowY(const ArkUI\_UIInputEvent\* event, uint32\_t pointerIndex, uint32\_t historyIndex)](#oh_arkui_pointerevent_gethistorywindowy) | Obtains the y-coordinate of a specific touch point in a specific historical event relative to the upper left corner of the current application window from a pointer event (such as a touch, mouse, or axis event). |
| [float OH\_ArkUI\_PointerEvent\_GetHistoryDisplayX(const ArkUI\_UIInputEvent\* event, uint32\_t pointerIndex, uint32\_t historyIndex)](#oh_arkui_pointerevent_gethistorydisplayx) | Obtains the x-coordinate of a specific touch point in a specific historical event relative to the upper left corner of the current screen from a pointer event (such as a touch, mouse, or axis event). |
| [float OH\_ArkUI\_PointerEvent\_GetHistoryDisplayY(const ArkUI\_UIInputEvent\* event, uint32\_t pointerIndex, uint32\_t historyIndex)](#oh_arkui_pointerevent_gethistorydisplayy) | Obtains the y-coordinate of a specific touch point in a specific historical event relative to the upper left corner of the current screen from a pointer event (such as a touch, mouse, or axis event). |
| [float OH\_ArkUI\_PointerEvent\_GetHistoryGlobalDisplayX(const ArkUI\_UIInputEvent\* event, uint32\_t pointerIndex, uint32\_t historyIndex)](#oh_arkui_pointerevent_gethistoryglobaldisplayx) | Obtains the x-coordinate relative to the global display for a specific touch point from historical events, based on the given pointer index and history index of an input event (such as a touch, mouse, or axis event). Position information can only be obtained from UI input events. For mouse and axis events, if the provided **pointerIndex** is greater than 0, this API always returns the default value **0.0f**. |
| [float OH\_ArkUI\_PointerEvent\_GetHistoryGlobalDisplayY(const ArkUI\_UIInputEvent\* event, uint32\_t pointerIndex, uint32\_t historyIndex)](#oh_arkui_pointerevent_gethistoryglobaldisplayy) | Obtains the y-coordinate relative to the global display for a specific touch point from historical events, based on the given pointer index and history index of an input event (such as a touch, mouse, or axis event). Position information can only be obtained from UI input events. For mouse and axis events, if the provided **pointerIndex** is greater than 0, this API always returns the default value **0.0f**. |
| [float OH\_ArkUI\_PointerEvent\_GetHistoryPressure(const ArkUI\_UIInputEvent\* event, uint32\_t pointerIndex, uint32\_t historyIndex)](#oh_arkui_pointerevent_gethistorypressure) | Obtains the pressure applied to the touchscreen in a specific historical event from a pointer event (such as a touch event). |
| [float OH\_ArkUI\_PointerEvent\_GetHistoryTiltX(const ArkUI\_UIInputEvent\* event, uint32\_t pointerIndex, uint32\_t historyIndex)](#oh_arkui_pointerevent_gethistorytiltx) | Obtains the angle relative to the YZ plane in a specific historical event from a pointer event (such as a touch event). The value range is \[-90, 90\], in deg. A positive value indicates a rightward tilt. |
| [float OH\_ArkUI\_PointerEvent\_GetHistoryTiltY(const ArkUI\_UIInputEvent\* event, uint32\_t pointerIndex, uint32\_t historyIndex)](#oh_arkui_pointerevent_gethistorytilty) | Obtains the angle relative to the XZ plane in a specific historical event from a pointer event (such as a touch event). The value range is \[-90, 90\], in deg. A positive value indicates a downward tilt. |
| [float OH\_ArkUI\_PointerEvent\_GetHistoryTouchAreaWidth(const ArkUI\_UIInputEvent\* event, uint32\_t pointerIndex, uint32\_t historyIndex)](#oh_arkui_pointerevent_gethistorytouchareawidth) | Obtains the width of the touch area in a specific historical event from a pointer event (such as a touch event). |
| [float OH\_ArkUI\_PointerEvent\_GetHistoryTouchAreaHeight(const ArkUI\_UIInputEvent\* event, uint32\_t pointerIndex, uint32\_t historyIndex)](#oh_arkui_pointerevent_gethistorytouchareaheight) | Obtains the height of the touch area in a specific historical event from a pointer event (such as a touch event). |
| [double OH\_ArkUI\_AxisEvent\_GetVerticalAxisValue(const ArkUI\_UIInputEvent\* event)](#oh_arkui_axisevent_getverticalaxisvalue) | Obtains the value of the vertical scroll axis for this axis event. This value is typically generated by mouse wheel scrolling or two-finger vertical swiping on a touchpad. If the value is generated by mouse wheel scrolling: 1. The reported value is in degrees and represents the angular increment of a single scroll, not the total accumulation. 2. The reported value includes the user's scroll step configuration (see [OH\_ArkUI\_AxisEvent\_GetScrollStep](#oh_arkui_axisevent_getscrollstep)). 3. The sign of the value indicates the direction: positive for forward scrolling and negative for backward scrolling. If the value is generated by two-finger vertical swiping on a touchpad: 1. The reported value is in px and represents the scroll increment, not the total accumulation. 2. The reported value does not include the user's scroll step configuration [OH\_ArkUI\_AxisEvent\_GetScrollStep](#oh_arkui_axisevent_getscrollstep). 3. The sign of the value indicates the direction: positive for swiping up and negative for swiping down. 4. The direction is affected by the system settings for natural scrolling. Under normal circumstances, vertical scroll axis events only drive vertical swipe gestures. However, if the mouse pointer is over a scrollable area where the scrollable directions are consistent, the vertical scroll axis event can drive the swipe gestures in this scrollable area, even if they are defined as horizontal. |
| [double OH\_ArkUI\_AxisEvent\_GetHorizontalAxisValue(const ArkUI\_UIInputEvent\* event)](#oh_arkui_axisevent_gethorizontalaxisvalue) | Obtains the value of the horizontal scroll axis for this axis event. This value is generated by two-finger horizontal swiping on a touchpad. |
| [double OH\_ArkUI\_AxisEvent\_GetPinchAxisScaleValue(const ArkUI\_UIInputEvent\* event)](#oh_arkui_axisevent_getpinchaxisscalevalue) | Obtains the scale value of the pinch axis for this axis event. This value is generated by a two-finger pinch gesture on a touchpad. The reported scale value is relative to the initial state when the system first detects the pinch gesture, with an initial scale value of 1.0. During the pinch operation, the scale value decreases from 1.0 towards 0.0 when the user pinches inward and increases from 1.0 when the user spreads fingers outward. |
| [int32\_t OH\_ArkUI\_AxisEvent\_GetAxisAction(const ArkUI\_UIInputEvent\* event)](#oh_arkui_axisevent_getaxisaction) | Obtains the action type of this axis event. |
| [int32\_t OH\_ArkUI\_AxisEvent\_HasAxis(const ArkUI\_UIInputEvent\* event, int32\_t axis)](#oh_arkui_axisevent_hasaxis) | Checks whether this axis event contains the specified axis type. |
| [int32\_t OH\_ArkUI\_PointerEvent\_SetInterceptHitTestMode(const ArkUI\_UIInputEvent\* event, HitTestMode mode)](#oh_arkui_pointerevent_setintercepthittestmode) | Sets the touch test mode. This API only applies to scenarios raw input events are received, such as when **NODE\_ON\_TOUCH** is used for touch event handling. It cannot be used with **ArkUI\_UIInputEvent** objects obtained from gesture events through [OH\_ArkUI\_GestureEvent\_GetRawInputEvent](../native-gesture-h/document.md#oh_arkui_gestureevent_getrawinputevent). |
| [int32\_t OH\_ArkUI\_MouseEvent\_GetMouseButton(const ArkUI\_UIInputEvent\* event)](#oh_arkui_mouseevent_getmousebutton) | Obtains the button type of a mouse event. |
| [int32\_t OH\_ArkUI\_MouseEvent\_GetMouseAction(const ArkUI\_UIInputEvent\* event)](#oh_arkui_mouseevent_getmouseaction) | Obtains the action type of a mouse event. |
| [int32\_t OH\_ArkUI\_PointerEvent\_SetStopPropagation(const ArkUI\_UIInputEvent\* event, bool stopPropagation)](#oh_arkui_pointerevent_setstoppropagation) | Sets whether to stop event propagation. This API only applies to scenarios raw input events are received, such as when **NODE\_ON\_TOUCH** is used for touch event handling. It cannot be used with **ArkUI\_UIInputEvent** objects obtained from gesture events through [OH\_ArkUI\_GestureEvent\_GetRawInputEvent](../native-gesture-h/document.md#oh_arkui_gestureevent_getrawinputevent). |
| [int32\_t OH\_ArkUI\_UIInputEvent\_GetDeviceId(const ArkUI\_UIInputEvent\* event)](#oh_arkui_uiinputevent_getdeviceid) | Obtains the ID of the input device that triggers a key event. |
| [int32\_t OH\_ArkUI\_UIInputEvent\_GetPressedKeys(const ArkUI\_UIInputEvent\* event, int32\_t\* pressedKeyCodes, int32\_t\* length)](#oh_arkui_uiinputevent_getpressedkeys) | Obtains all pressed keys. Currently, only key events are supported. |
| [double OH\_ArkUI\_FocusAxisEvent\_GetAxisValue(const ArkUI\_UIInputEvent\* event, int32\_t axis)](#oh_arkui_focusaxisevent_getaxisvalue) | Obtains the axis value of a focus axis event. |
| [int32\_t OH\_ArkUI\_FocusAxisEvent\_SetStopPropagation(const ArkUI\_UIInputEvent\* event, bool stopPropagation)](#oh_arkui_focusaxisevent_setstoppropagation) | Sets whether to prevent a focus axis event from bubbling up. |
| [int32\_t OH\_ArkUI\_UIInputEvent\_GetModifierKeyStates(const ArkUI\_UIInputEvent\* event, uint64\_t\* keys)](#oh_arkui_uiinputevent_getmodifierkeystates) | Obtains the modifier key states for a UI input event. This API outputs the state of all modifier keys at the time of the event through the **keys** parameter. You can determine which keys are pressed by performing bitwise operations with the modifier key types defined in [ArkUI\_ModifierKeyName](#arkui_modifierkeyname). |
| [int32\_t OH\_ArkUI\_AxisEvent\_SetPropagation(const ArkUI\_UIInputEvent\* event, bool propagation)](#oh_arkui_axisevent_setpropagation) | Sets whether to enable axis event propagation (bubbling). By default, axis events do not bubble and are only sent to the first component that can respond to axis events. You can enable axis event bubbling when an axis event is received to allow the event to be passed to the next ancestor component in the response chain that can handle axis events. This API cannot be used on axis events obtained from gesture events. |
| [int32\_t OH\_ArkUI\_AxisEvent\_GetScrollStep(const ArkUI\_UIInputEvent\* event)](#oh_arkui_axisevent_getscrollstep) | Obtains the scroll step coefficient for a wheel-based axis event. This API returns the user-configured scroll scale factor. |
| [float OH\_ArkUI\_UIInputEvent\_GetEventTargetWidth(const ArkUI\_UIInputEvent\* event)](#oh_arkui_uiinputevent_geteventtargetwidth) | Obtains the width of the component hit by an event. |
| [float OH\_ArkUI\_UIInputEvent\_GetEventTargetHeight(const ArkUI\_UIInputEvent\* event)](#oh_arkui_uiinputevent_geteventtargetheight) | Obtains the height of the component hit by an event. |
| [float OH\_ArkUI\_UIInputEvent\_GetEventTargetPositionX(const ArkUI\_UIInputEvent\* event)](#oh_arkui_uiinputevent_geteventtargetpositionx) | Obtains the x-coordinate of the component hit by an event. |
| [float OH\_ArkUI\_UIInputEvent\_GetEventTargetPositionY(const ArkUI\_UIInputEvent\* event)](#oh_arkui_uiinputevent_geteventtargetpositiony) | Obtains the y-coordinate of the component hit by an event. |
| [float OH\_ArkUI\_UIInputEvent\_GetEventTargetGlobalPositionX(const ArkUI\_UIInputEvent\* event)](#oh_arkui_uiinputevent_geteventtargetglobalpositionx) | Obtains the global x-coordinate of the component hit by an event. |
| [float OH\_ArkUI\_UIInputEvent\_GetEventTargetGlobalPositionY(const ArkUI\_UIInputEvent\* event)](#oh_arkui_uiinputevent_geteventtargetglobalpositiony) | Obtains the global y-coordinate of the component hit by an event. |
| [int64\_t OH\_ArkUI\_PointerEvent\_GetPressedTimeByIndex(const ArkUI\_UIInputEvent\* event, uint32\_t pointerIndex)](#oh_arkui_pointerevent_getpressedtimebyindex) | Obtains the press time of a specified touch point. This API is effective only for touch events. |
| [float OH\_ArkUI\_MouseEvent\_GetRawDeltaX(const ArkUI\_UIInputEvent\* event)](#oh_arkui_mouseevent_getrawdeltax) | Obtains the movement increment of the mouse along the X axis in a two-dimensional plane. The value is the original movement data of the mouse hardware, which is expressed in the unit of the mouse movement distance in the physical world. The reported value is determined by the hardware, not the physical or logical pixels of the screen. |
| [float OH\_ArkUI\_MouseEvent\_GetRawDeltaY(const ArkUI\_UIInputEvent\* event)](#oh_arkui_mouseevent_getrawdeltay) | Obtains the movement increment of the mouse along the Y axis in a two-dimensional plane. The value is the original movement data of the mouse hardware, which is expressed in the unit of the mouse movement distance in the physical world. The reported value is determined by the hardware, not the physical or logical pixels of the screen. |
| [int32\_t OH\_ArkUI\_MouseEvent\_GetPressedButtons(const ArkUI\_UIInputEvent\* event, int32\_t\* pressedButtons, int32\_t\* length)](#oh_arkui_mouseevent_getpressedbuttons) | Obtains the pressed buttons from a mouse event. |
| [int32\_t OH\_ArkUI\_UIInputEvent\_GetTargetDisplayId(const ArkUI\_UIInputEvent\* event)](#oh_arkui_uiinputevent_gettargetdisplayid) | Obtains the ID of the screen where the UI input event occurs. |
| [bool OH\_ArkUI\_HoverEvent\_IsHovered(const ArkUI\_UIInputEvent\* event)](#oh_arkui_hoverevent_ishovered) | Checks whether the cursor is hovering over this component. |
| [int32\_t OH\_ArkUI\_PointerEvent\_CreateClonedEvent(const ArkUI\_UIInputEvent\* event, ArkUI\_UIInputEvent\*\* clonedEvent)](#oh_arkui_pointerevent_createclonedevent) | Creates a cloned event pointer based on an event pointer. This API is effective only for touch events. |
| [int32\_t OH\_ArkUI\_PointerEvent\_DestroyClonedEvent(const ArkUI\_UIInputEvent\* event)](#oh_arkui_pointerevent_destroyclonedevent) | Destroys a cloned event pointer. |
| [int32\_t OH\_ArkUI\_PointerEvent\_SetClonedEventLocalPosition(const ArkUI\_UIInputEvent\* event, float x, float y)](#oh_arkui_pointerevent_setclonedeventlocalposition) | Sets the x-coordinate and y-coordinate of a cloned event relative to the upper left corner of the current component. |
| [int32\_t OH\_ArkUI\_PointerEvent\_SetClonedEventLocalPositionByIndex(const ArkUI\_UIInputEvent\* event, float x, float y, int32\_t pointerIndex)](#oh_arkui_pointerevent_setclonedeventlocalpositionbyindex) | Sets the x-coordinate and y-coordinate of a specific touch point of a cloned event relative to the upper left corner of the current component. |
| [int32\_t OH\_ArkUI\_PointerEvent\_SetClonedEventActionType(const ArkUI\_UIInputEvent\* event, int32\_t actionType)](#oh_arkui_pointerevent_setclonedeventactiontype) | Sets the action type of a cloned event. |
| [int32\_t OH\_ArkUI\_PointerEvent\_SetClonedEventChangedFingerId(const ArkUI\_UIInputEvent\* event, int32\_t fingerId)](#oh_arkui_pointerevent_setclonedeventchangedfingerid) | Sets the touch point ID of a cloned pointer event. |
| [int32\_t OH\_ArkUI\_PointerEvent\_SetClonedEventFingerIdByIndex(const ArkUI\_UIInputEvent\* event, int32\_t fingerId, int32\_t pointerIndex)](#oh_arkui_pointerevent_setclonedeventfingeridbyindex) | Sets the touch point ID of a specific touch point of a cloned event. |
| [int32\_t OH\_ArkUI\_PointerEvent\_PostClonedEvent(ArkUI\_NodeHandle node, const ArkUI\_UIInputEvent\* event)](#oh_arkui_pointerevent_postclonedevent) | Posts a cloned event to a specific node. |
| [ArkUI\_ErrorCode OH\_ArkUI\_UIInputEvent\_GetLatestStatus()](#oh_arkui_uiinputevent_getlateststatus) | Obtains the result code of the most recent API call related to an **ArkUI\_UIInputEvent** object. This API is typically unnecessary for normal operations, but can be used to verify ambiguous return values |
| [ArkUI\_CoastingAxisEvent OH\_ArkUI\_UIInputEvent\_GetCoastingAxisEvent(ArkUI\_UIInputEvent\* event)](#oh_arkui_uiinputevent_getcoastingaxisevent) | Obtains the pointer to a coasting axis event. |
| [int64\_t OH\_ArkUI\_CoastingAxisEvent\_GetEventTime(ArkUI\_CoastingAxisEvent event)](#oh_arkui_coastingaxisevent_geteventtime) | Obtains the time when a coasting axis event occurs. |
| [ArkUI\_CoastingAxisEventPhase OH\_ArkUI\_CoastingAxisEvent\_GetPhase(ArkUI\_CoastingAxisEvent event)](#oh_arkui_coastingaxisevent_getphase) | Obtains the scroll phase of the specified coasting axis event. |
| [float OH\_ArkUI\_CoastingAxisEvent\_GetDeltaY(ArkUI\_CoastingAxisEvent event)](#oh_arkui_coastingaxisevent_getdeltay) | Obtains the vertical delta value of the specified coasting axis event. Unit: px, representing the single scroll increment (not the total scroll amount). Negative values indicate a downward direction (fingers swiping from top to bottom), and positive values indicate an upward direction (fingers swiping from bottom to top). |
| [float OH\_ArkUI\_CoastingAxisEvent\_GetDeltaX(ArkUI\_CoastingAxisEvent event)](#oh_arkui_coastingaxisevent_getdeltax) | Obtains the horizontal delta value of the specified coasting axis event. Unit: px, representing the single scroll increment (not the total scroll amount). Positive values indicate a rightward direction (fingers swiping from right to left), and negative values indicate a leftward direction (fingers swiping from left to right). |
| [int32\_t OH\_ArkUI\_CoastingAxisEvent\_SetPropagation(ArkUI\_CoastingAxisEvent event, bool propagation)](#oh_arkui_coastingaxisevent_setpropagation) | Sets whether to enable event propagation for the specified coasting axis event. By default, event propagation is disabled. |
| [ArkUI\_ErrorCode OH\_ArkUI\_TouchTestInfo\_GetTouchTestInfoList(ArkUI\_TouchTestInfo\* info, ArkUI\_TouchTestInfoItemArray\* array, int32\_t\* size)](#oh_arkui_touchtestinfo_gettouchtestinfolist) | Obtains the array of touch test information items from the touch test information. |
| [float OH\_ArkUI\_TouchTestInfoItem\_GetX(const ArkUI\_TouchTestInfoItem\* info)](#oh_arkui_touchtestinfoitem_getx) | Obtains the X coordinate relative to the upper left corner of the child component from the touch test information item, in px. |
| [float OH\_ArkUI\_TouchTestInfoItem\_GetY(const ArkUI\_TouchTestInfoItem\* info)](#oh_arkui_touchtestinfoitem_gety) | Obtains the Y coordinate relative to the upper left corner of the child component from the touch test information item, in px. |
| [float OH\_ArkUI\_TouchTestInfoItem\_GetWindowX(const ArkUI\_TouchTestInfoItem\* info)](#oh_arkui_touchtestinfoitem_getwindowx) | Obtains the X coordinate relative to the upper left corner of the current application window from the touch test information item, in px. |
| [float OH\_ArkUI\_TouchTestInfoItem\_GetWindowY(const ArkUI\_TouchTestInfoItem\* info)](#oh_arkui_touchtestinfoitem_getwindowy) | Obtains the Y coordinate relative to the upper left corner of the current application window from the touch test information item, in px. |
| [float OH\_ArkUI\_TouchTestInfoItem\_GetXRelativeToParent(const ArkUI\_TouchTestInfoItem\* info)](#oh_arkui_touchtestinfoitem_getxrelativetoparent) | Obtains the X coordinate relative to the upper left corner of the parent component from the touch test information item, in px. |
| [float OH\_ArkUI\_TouchTestInfoItem\_GetYRelativeToParent(const ArkUI\_TouchTestInfoItem\* info)](#oh_arkui_touchtestinfoitem_getyrelativetoparent) | Obtains the Y coordinate relative to the upper left corner of the parent component from the touch test information item, in px. |
| [ArkUI\_ErrorCode OH\_ArkUI\_TouchTestInfoItem\_GetChildRect(const ArkUI\_TouchTestInfoItem\* info, ArkUI\_Rect\* childRect)](#oh_arkui_touchtestinfoitem_getchildrect) | Obtains the boundary rectangle information of the child component from the touch test information item. |
| [ArkUI\_ErrorCode OH\_ArkUI\_TouchTestInfoItem\_GetChildId(const ArkUI\_TouchTestInfoItem\* info, char\* buffer, int32\_t bufferSize)](#oh_arkui_touchtestinfoitem_getchildid) | Obtains the ID of the child component from the touch test information item. |
| [ArkUI\_ErrorCode OH\_ArkUI\_TouchTestInfo\_SetTouchResultStrategy(ArkUI\_TouchTestInfo\* info, ArkUI\_TouchTestStrategy strategy)](#oh_arkui_touchtestinfo_settouchresultstrategy) | Sets the touch test policy, that is, the behavior of a component and its child components in a hit test. |
| [ArkUI\_ErrorCode OH\_ArkUI\_TouchTestInfo\_SetTouchResultId(ArkUI\_TouchTestInfo\* info, const char\* id)](#oh_arkui_touchtestinfo_settouchresultid) | Sets the ID of a child component involved in a hit test. |

#### Enum Description

#### \[h2\]ArkUI\_UIInputEvent\_Type

enum ArkUI\_UIInputEvent\_Type

**Description**

Enumerates the UI input event types.

**Since**: 12

| Value | Description |
| :-- | :-- |
| ARKUI\_UIINPUTEVENT\_TYPE\_UNKNOWN = 0 | Unknown. |
| ARKUI\_UIINPUTEVENT\_TYPE\_TOUCH = 1 | Touch event. |
| ARKUI\_UIINPUTEVENT\_TYPE\_AXIS = 2 | Axis event. |
| ARKUI\_UIINPUTEVENT\_TYPE\_MOUSE = 3 | Mouse event. |
| ARKUI\_UIINPUTEVENT\_TYPE\_KEY = 4 | 
Key event.

**Since**: 20

 |

#### \[h2\]anonymous1

enum anonymous1

**Description**

Enumerates the action types of the input event.

**Since**: 12

| Value | Description |
| :-- | :-- |
| UI\_TOUCH\_EVENT\_ACTION\_CANCEL = 0 | Cancellation of touch. |
| UI\_TOUCH\_EVENT\_ACTION\_DOWN = 1 | Pressing of touch. |
| UI\_TOUCH\_EVENT\_ACTION\_MOVE = 2 | Moving of touch. |
| UI\_TOUCH\_EVENT\_ACTION\_UP = 3 | Lifting of touch. |

#### \[h2\]anonymous2

enum anonymous2

**Description**

Enumerates the tool types of the input event.

**Since**: 12

| Value | Description |
| :-- | :-- |
| UI\_INPUT\_EVENT\_TOOL\_TYPE\_UNKNOWN = 0 | Unknown tool type. |
| UI\_INPUT\_EVENT\_TOOL\_TYPE\_FINGER = 1 | Finger. |
| UI\_INPUT\_EVENT\_TOOL\_TYPE\_PEN = 2 | Stylus. |
| UI\_INPUT\_EVENT\_TOOL\_TYPE\_MOUSE = 3 | Mouse. |
| UI\_INPUT\_EVENT\_TOOL\_TYPE\_TOUCHPAD = 4 | Touchpad. |
| UI\_INPUT\_EVENT\_TOOL\_TYPE\_JOYSTICK = 5 | Joystick. |

#### \[h2\]anonymous3

enum anonymous3

**Description**

Enumerates the source types of the input event.

**Since**: 12

| Value | Description |
| :-- | :-- |
| UI\_INPUT\_EVENT\_SOURCE\_TYPE\_UNKNOWN = 0 | Unknown input source. |
| UI\_INPUT\_EVENT\_SOURCE\_TYPE\_MOUSE = 1 | Mouse. |
| UI\_INPUT\_EVENT\_SOURCE\_TYPE\_TOUCH\_SCREEN = 2 | Touchscreen. |
| UI\_INPUT\_EVENT\_SOURCE\_TYPE\_KEY = 4 | 
Key.

**Since**: 22

 |
| UI\_INPUT\_EVENT\_SOURCE\_TYPE\_JOYSTICK = 5 | 

Joystick.

**Since**: 22

 |

#### \[h2\]HitTestMode

enum HitTestMode

**Description**

Enumerates the hit test modes.

**Since**: 12

| Value | Description |
| :-- | :-- |
| HTM\_DEFAULT = 0 | Default hit test mode. The node itself and its child nodes respond to the hit test, but block the hit test of sibling nodes. It does not affect the hit test of ancestor nodes. |
| HTM\_BLOCK = 1 | The node itself responds to the hit test and blocks the hit test of child nodes, sibling nodes, and ancestor nodes. |
| HTM\_TRANSPARENT = 2 | Both the node itself and its child nodes respond to the hit test and do not block the hit test of sibling nodes and ancestor nodes. |
| HTM\_NONE = 3 | The node itself does not respond to the hit test and does not block the hit test of child nodes, sibling nodes, and ancestor nodes. |
| HTM\_BLOCK\_HIERARCHY = 4 | 
The node itself and its child nodes respond to the hit test, preventing all sibling nodes and parent nodes with lower priority from participating in the hit test.

**Since**: 20

 |
| HTM\_BLOCK\_DESCENDANTS = 5 | 

The node itself does not respond to the hit test, and all its descendants (children, grandchildren, and more) also do not respond to the hit test. It does not affect the hit test of ancestor nodes.

**Since**: 20

 |

#### \[h2\]anonymous4

enum anonymous4

**Description**

Enumerates the action types of the mouse event.

**Since**: 12

| Value | Description |
| :-- | :-- |
| UI\_MOUSE\_EVENT\_ACTION\_UNKNOWN = 0 | Unknown action. |
| UI\_MOUSE\_EVENT\_ACTION\_PRESS = 1 | The mouse button is pressed. |
| UI\_MOUSE\_EVENT\_ACTION\_RELEASE = 2 | The mouse button is released. |
| UI\_MOUSE\_EVENT\_ACTION\_MOVE = 3 | The mouse cursor moves. |
| UI\_MOUSE\_EVENT\_ACTION\_CANCEL = 13 | 
The mouse button action is canceled.

**Since**: 18

 |

#### \[h2\]anonymous5

enum anonymous5

**Description**

Enumerates the button types of the mouse event.

**Since**: 12

| Value | Description |
| :-- | :-- |
| UI\_MOUSE\_EVENT\_BUTTON\_NONE = 0 | No button. |
| UI\_MOUSE\_EVENT\_BUTTON\_LEFT = 1 | Left button. |
| UI\_MOUSE\_EVENT\_BUTTON\_RIGHT = 2 | Right button. |
| UI\_MOUSE\_EVENT\_BUTTON\_MIDDLE = 3 | Middle button. |
| UI\_MOUSE\_EVENT\_BUTTON\_BACK = 4 | Back button on the left of the mouse. |
| UI\_MOUSE\_EVENT\_BUTTON\_FORWARD = 5 | Forward button on the left of the mouse. |

#### \[h2\]ArkUI\_ModifierKeyName

enum ArkUI\_ModifierKeyName

**Description**

Enumerates the modifier keys.

**Since**: 12

| Value | Description |
| :-- | :-- |
| ARKUI\_MODIFIER\_KEY\_CTRL = 1 << 0 | Ctrl. |
| ARKUI\_MODIFIER\_KEY\_SHIFT = 1 << 1 | Shift. |
| ARKUI\_MODIFIER\_KEY\_ALT = 1 << 2 | Alt. |
| ARKUI\_MODIFIER\_KEY\_FN = 1 << 3 | Fn (for debugging purposes only; typically, the Fn key state is not reported) |

#### \[h2\]anonymous6

enum anonymous6

**Description**

Defines the axis types of the [focus axis event](../../../arkts-components/universal-events/basic-input-events/focus-axis-event/document.md).

**Since**: 15

| Value | Description |
| :-- | :-- |
| UI\_FOCUS\_AXIS\_EVENT\_ABS\_X = 0 | Game controller x-axis. |
| UI\_FOCUS\_AXIS\_EVENT\_ABS\_Y = 1 | Game controller y-axis. |
| UI\_FOCUS\_AXIS\_EVENT\_ABS\_Z = 2 | Game controller z-axis. |
| UI\_FOCUS\_AXIS\_EVENT\_ABS\_RZ = 3 | Game controller rz-axis. |
| UI\_FOCUS\_AXIS\_EVENT\_ABS\_GAS = 4 | Game controller GAS-axis. |
| UI\_FOCUS\_AXIS\_EVENT\_ABS\_BRAKE = 5 | Game controller BRAKE-axis. |
| UI\_FOCUS\_AXIS\_EVENT\_ABS\_HAT0X = 6 | Game controller HAT0X-axis. |
| UI\_FOCUS\_AXIS\_EVENT\_ABS\_HAT0Y = 7 | Game controller HAT0Y-axis. |

#### \[h2\]ArkUI\_InteractionHand

enum ArkUI\_InteractionHand

**Description**

Defines whether the touch event is from the left or right hand.

**Since**: 15

| Value | Description |
| :-- | :-- |
| ARKUI\_EVENT\_HAND\_NONE = 0 | Unknown. |
| ARKUI\_EVENT\_HAND\_LEFT = 1 | Left hand. |
| ARKUI\_EVENT\_HAND\_RIGHT = 2 | Right hand. |

#### \[h2\]anonymous7

enum anonymous7

**Description**

Defines the operation types of the [axis event](../../../arkts-components/universal-events/basic-input-events/axis-event/document.md).

**Since**: 15

| Value | Description |
| :-- | :-- |
| UI\_AXIS\_EVENT\_ACTION\_NONE = 0 | The axis event is abnormal. |
| UI\_AXIS\_EVENT\_ACTION\_BEGIN = 1 | The axis event begins. |
| UI\_AXIS\_EVENT\_ACTION\_UPDATE = 2 | The axis event is updated. |
| UI\_AXIS\_EVENT\_ACTION\_END = 3 | The axis event ends. |
| UI\_AXIS\_EVENT\_ACTION\_CANCEL = 4 | The axis event is canceled. |

#### \[h2\]anonymous8

enum anonymous8

**Description**

Enumerates the axis types for axis events.

**Since**: 22

| Value | Description |
| :-- | :-- |
| UI\_AXIS\_TYPE\_VERTICAL\_AXIS = 0 | Vertical axis. |
| UI\_AXIS\_TYPE\_HORIZONTAL\_AXIS = 1 | Horizontal axis. |
| UI\_AXIS\_TYPE\_PINCH\_AXIS = 2 | Pinch axis. |

#### \[h2\]ArkUI\_CoastingAxisEventPhase

enum ArkUI\_CoastingAxisEventPhase

**Description**

Enumerates the phases of coasting axis events.

**Since**: 22

| Value | Description |
| :-- | :-- |
| ARKUI\_COASTING\_AXIS\_EVENT\_PHASE\_NONE = 0 | Invalid coasting axis event phase, serving as an abnormal default value. You can verify that the coasting axis phase is not this value to confirm event validity. |
| ARKUI\_COASTING\_AXIS\_EVENT\_PHASE\_BEGIN = 1 | The coasting axis event begins. This is the initial event in the coasting phase. |
| ARKUI\_COASTING\_AXIS\_EVENT\_PHASE\_UPDATE = 2 | The coasting axis event updates. In this phase, you can obtain the coasting axis delta value to handle scroll offset calculations. |
| ARKUI\_COASTING\_AXIS\_EVENT\_PHASE\_END = 3 | The coasting axis event ends. This phase is triggered when coasting stops due to braking (for example, the user re-engages the touchpad during coasting, or interacts via a mouse or touchscreen) or natural decay to rest. Upon reaching this phase, immediately terminate the coasting scroll effect. |

#### \[h2\]ArkUI\_TouchTestStrategy

enum ArkUI\_TouchTestStrategy

**Description**

Defines the touch test policy.

**Since**: 22

| Value | Description |
| :-- | :-- |
| ARKUI\_TOUCH\_TEST\_STRATEGY\_DEFAULT = 0 | Custom dispatch has no effect. The system dispatches events based on the hit status of the current node. |
| ARKUI\_TOUCH\_TEST\_STRATEGY\_FORWARD\_COMPETITION = 1 | The event is dispatched to a specified child node, and the system determines whether to dispatch events to other sibling nodes. |
| ARKUI\_TOUCH\_TEST\_STRATEGY\_FORWARD = 2 | The event is dispatched to a specified child node, and the system will not dispatch events to other sibling nodes. |

#### Function Description

#### \[h2\]OH\_ArkUI\_UIInputEvent\_GetType()

int32\_t OH\_ArkUI\_UIInputEvent\_GetType(const ArkUI\_UIInputEvent\* event)

**Description**

Obtains the type of a UI input event. Before accessing an **ArkUI\_UIInputEvent** pointer, use this API to determine the type of the input event. This API returns a value from the [ArkUI\_UIInputEvent\_Type](#arkui_uiinputevent_type) enum. It helps ensure compatibility with subsequent accessors. For example, if the event is a touch event, which is directional, you can use OH\_ArkUI\_UIInputEvent\_GetXXX or OH\_ArkUI\_PointerEvent\_GetXXX for access. Using OH\_ArkUI\_KeyEvent\_GetXXX to access the event may produce undefined behavior. For unsupported event types, this API returns the default value **0**.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [const ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md)\* event | Pointer to the UI input event. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | Type of the UI input event. Returns **0** if any parameter error occurs. |

#### \[h2\]OH\_ArkUI\_UIInputEvent\_GetAction()

int32\_t OH\_ArkUI\_UIInputEvent\_GetAction(const ArkUI\_UIInputEvent\* event)

**Description**

Obtains the action type of an input event. The action type defines the phase of a basic event (for example, start or end) and characterizes its behavior, such as touch down or touch up. Action types are specific to the event category: [UI\_TOUCH\_EVENT\_ACTION\_XXX](#anonymous1) for touch events and [UI\_MOUSE\_EVENT\_ACTION\_XXX](#anonymous4) for mouse events. For an axis event, use [OH\_ArkUI\_AxisEvent\_GetAxisAction](#oh_arkui_axisevent_getaxisaction) to obtain the action types, which returns [UI\_AXIS\_EVENT\_ACTION\_XXX](#anonymous7). For a key event, use [OH\_ArkUI\_KeyEvent\_GetType](../native-key-event-h/document.md#oh_arkui_keyevent_gettype) to obtain the action types, which returns [ArkUI\_KeyEventType](../native-key-event-h/document.md#arkui_keyeventtype).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [const ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md)\* event | Pointer to the UI input event. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | Action type of the UI input event. Returns **\-1** if any parameter error occurs. |

#### \[h2\]OH\_ArkUI\_UIInputEvent\_GetSourceType()

int32\_t OH\_ArkUI\_UIInputEvent\_GetSourceType(const ArkUI\_UIInputEvent\* event)

**Description**

Obtains the source type of a UI input event. The source represents the physical device, such as a touchscreen or mouse device, that generates the input event. It is defined by [UI\_INPUT\_EVENT\_SOURCE\_TYPE\_XXX](#anonymous3). This is different from the input tool, which is the device used to interact with the source, for example, a finger or stylus. However, in certain cases, the input source and the input tool can be the same. For example, a mouse device acts as both the source and tool for click events. For key events, obtaining the source type is not supported, and in such cases, the API will return an **unknown** value.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [const ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md)\* event | Pointer to the UI input event. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | Source type of the UI input event. |

#### \[h2\]OH\_ArkUI\_UIInputEvent\_GetToolType()

int32\_t OH\_ArkUI\_UIInputEvent\_GetToolType(const ArkUI\_UIInputEvent\* event)

**Description**

Obtains the tool type of a UI input event. The input tool is the device used to interact with the input source, such as a finger or stylus. These tools themselves do not generate events but can drive the input source device to continuously generate events. The returned type is defined by the enumerated value of [UI\_INPUT\_EVENT\_TOOL\_TYPE\_XXX](#anonymous2). For key events, obtaining the tool type is not supported, and in such cases, the API will return an **unknown** value.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [const ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md)\* event | Pointer to the UI input event. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | Tool type of the UI input event. |

#### \[h2\]OH\_ArkUI\_UIInputEvent\_GetEventTime()

int64\_t OH\_ArkUI\_UIInputEvent\_GetEventTime(const ArkUI\_UIInputEvent\* event)

**Description**

Obtains the time when a specified UI input event occurs. The unit is ns.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [const ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md)\* event | Pointer to the UI input event. |

**Return value**

| Type | Description |
| :-- | :-- |
| int64\_t | Time when the UI input event occurs. Returns **0** if any parameter error occurs. |

#### \[h2\]OH\_ArkUI\_PointerEvent\_GetPointerCount()

uint32\_t OH\_ArkUI\_PointerEvent\_GetPointerCount(const ArkUI\_UIInputEvent\* event)

**Description**

Obtains the number of touch points from a pointer event (such as a touch, mouse, or axis event). Pointer events are typically events that carry position information, such as touch events, where the location of the event can be determined. Non-pointer events, such as key events, do not have position information and do not involve points, so this API always returns **0**. For touch events, this API returns the number of active touch points, for example, fingers on the screen. For mouse and axis events, this API always returns **1**, as they are single-pointer interactions.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [const ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md)\* event | Pointer to the UI input event. |

**Return value**

| Type | Description |
| :-- | :-- |
| uint32\_t | Number of touch points in the pointer event. |

#### \[h2\]OH\_ArkUI\_PointerEvent\_GetPointerId()

int32\_t OH\_ArkUI\_PointerEvent\_GetPointerId(const ArkUI\_UIInputEvent\* event, uint32\_t pointerIndex)

**Description**

Obtains the unique ID of a touch point from a pointer event (such as a touch, mouse, or axis event). The ID distinguishes between multiple touch points from the same input device. The return value itself does not have any other meaning beyond identifying the touch point.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [const ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md)\* event | Pointer to the UI input event. |
| uint32\_t pointerIndex | Index of the target touch point in the multi-touch data list. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | Unique ID of the specified touch point. |

#### \[h2\]OH\_ArkUI\_PointerEvent\_GetChangedPointerId()

int32\_t OH\_ArkUI\_PointerEvent\_GetChangedPointerId(const ArkUI\_UIInputEvent\* event, uint32\_t\* pointerIndex)

**Description**

Obtains the ID of the touch pointer that triggers the current touch event.

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| [const ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md)\* event | Pointer to the UI input event. |
| uint32\_t\* pointerIndex | Index of the target touch point in the multi-touch data list. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_PointerEvent\_GetX()

float OH\_ArkUI\_PointerEvent\_GetX(const ArkUI\_UIInputEvent\* event)

**Description**

Obtains the x-coordinate relative to the upper left corner of the current component from a pointer event (such as a touch, mouse, or axis event).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [const ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md)\* event | Pointer to the UI input event. |

**Return value**

| Type | Description |
| :-- | :-- |
| float | X-coordinate relative to the upper left corner of the current component, in px. Returns **0.0f** if a parameter error occurs. |

#### \[h2\]OH\_ArkUI\_PointerEvent\_GetXByIndex()

float OH\_ArkUI\_PointerEvent\_GetXByIndex(const ArkUI\_UIInputEvent\* event, uint32\_t pointerIndex)

**Description**

Obtains the x-coordinate of a specific touch point relative to the upper left corner of the current component from a pointer event (such as a touch, mouse, or axis event). For mouse and axis events, this API returns the default value of **0.0f** if the given index is greater than 0.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [const ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md)\* event | Pointer to the UI input event. |
| uint32\_t pointerIndex | Index of the target touch point in the multi-touch data list. |

**Return value**

| Type | Description |
| :-- | :-- |
| float | X-coordinate of the specific touch point relative to the upper left corner of the current component, in px. Returns **0.0f** if a parameter error occurs. |

#### \[h2\]OH\_ArkUI\_PointerEvent\_GetY()

float OH\_ArkUI\_PointerEvent\_GetY(const ArkUI\_UIInputEvent\* event)

**Description**

Obtains the y-coordinate relative to the upper left corner of the current component from a pointer event (such as a touch, mouse, or axis event).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [const ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md)\* event | Pointer to the UI input event. |

**Return value**

| Type | Description |
| :-- | :-- |
| float | Y-coordinate relative to the upper left corner of the current component, in px. Returns **0.0f** if a parameter error occurs. |

#### \[h2\]OH\_ArkUI\_PointerEvent\_GetYByIndex()

float OH\_ArkUI\_PointerEvent\_GetYByIndex(const ArkUI\_UIInputEvent\* event, uint32\_t pointerIndex)

**Description**

Obtains the y-coordinate of a specific touch point relative to the upper left corner of the current component from a pointer event (such as a touch, mouse, or axis event). For mouse and axis events, this API returns the default value of **0.0f** if the given index is greater than 0.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [const ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md)\* event | Pointer to the UI input event. |
| uint32\_t pointerIndex | Index of the target touch point in the multi-touch data list. |

**Return value**

| Type | Description |
| :-- | :-- |
| float | Y-coordinate of the specific touch point relative to the upper left corner of the current component, in px. Returns **0.0f** if a parameter error occurs. |

#### \[h2\]OH\_ArkUI\_PointerEvent\_GetWindowX()

float OH\_ArkUI\_PointerEvent\_GetWindowX(const ArkUI\_UIInputEvent\* event)

**Description**

Obtains the x-coordinate relative to the upper left corner of the current application window from a pointer event (such as a touch, mouse, or axis event).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [const ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md)\* event | Pointer to the UI input event. |

**Return value**

| Type | Description |
| :-- | :-- |
| float | X-coordinate relative to the upper left corner of the current application window, in px. Returns **0.0f** if a parameter error occurs. |

#### \[h2\]OH\_ArkUI\_PointerEvent\_GetWindowXByIndex()

float OH\_ArkUI\_PointerEvent\_GetWindowXByIndex(const ArkUI\_UIInputEvent\* event, uint32\_t pointerIndex)

**Description**

Obtains the x-coordinate of a specific touch point relative to the upper left corner of the current application window from a pointer event (such as a touch, mouse, or axis event). For mouse and axis events, this API returns the default value of **0.0f** if the given index is greater than 0.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [const ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md)\* event | Pointer to the UI input event. |
| uint32\_t pointerIndex | Index of the target touch point in the multi-touch data list. |

**Return value**

| Type | Description |
| :-- | :-- |
| float | X-coordinate of the specific touch point relative to the upper left corner of the current application window, in px. Returns **0.0f** if a parameter error occurs. |

#### \[h2\]OH\_ArkUI\_PointerEvent\_GetWindowY()

float OH\_ArkUI\_PointerEvent\_GetWindowY(const ArkUI\_UIInputEvent\* event)

**Description**

Obtains the y-coordinate relative to the upper left corner of the current application window from a pointer event (such as a touch, mouse, or axis event).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [const ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md)\* event | Pointer to the UI input event. |

**Return value**

| Type | Description |
| :-- | :-- |
| float | Y-coordinate relative to the upper left corner of the current application window, in px. Returns **0.0f** if a parameter error occurs. |

#### \[h2\]OH\_ArkUI\_PointerEvent\_GetWindowYByIndex()

float OH\_ArkUI\_PointerEvent\_GetWindowYByIndex(const ArkUI\_UIInputEvent\* event, uint32\_t pointerIndex)

**Description**

Obtains the y-coordinate of a specific touch point relative to the upper left corner of the current application window from a pointer event (such as a touch, mouse, or axis event). For mouse and axis events, this API returns the default value of **0.0f** if the given index is greater than 0.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [const ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md)\* event | Pointer to the UI input event. |
| uint32\_t pointerIndex | Index of the target touch point in the multi-touch data list. |

**Return value**

| Type | Description |
| :-- | :-- |
| float | Y-coordinate of the specific touch point relative to the upper left corner of the current application window, in px. Returns **0.0f** if a parameter error occurs. |

#### \[h2\]OH\_ArkUI\_PointerEvent\_GetDisplayX()

float OH\_ArkUI\_PointerEvent\_GetDisplayX(const ArkUI\_UIInputEvent\* event)

**Description**

Obtains the x-coordinate relative to the upper left corner of the current screen from a pointer event (such as a touch, mouse, or axis event).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [const ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md)\* event | Pointer to the UI input event. |

**Return value**

| Type | Description |
| :-- | :-- |
| float | X-coordinate relative to the upper left corner of the current screen, in px. Returns **0.0f** if a parameter error occurs. |

#### \[h2\]OH\_ArkUI\_PointerEvent\_GetDisplayXByIndex()

float OH\_ArkUI\_PointerEvent\_GetDisplayXByIndex(const ArkUI\_UIInputEvent\* event, uint32\_t pointerIndex)

**Description**

Obtains the x-coordinate of a specific touch point relative to the upper left corner of the current screen from a pointer event (such as a touch, mouse, or axis event). For mouse and axis events, this API returns the default value of **0.0f** if the given index is greater than 0.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [const ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md)\* event | Pointer to the UI input event. |
| uint32\_t pointerIndex | Index of the target touch point in the multi-touch data list. |

**Return value**

| Type | Description |
| :-- | :-- |
| float | X-coordinate of the specific touch point relative to the upper left corner of the current screen, in px. Returns **0.0f** if a parameter error occurs. |

#### \[h2\]OH\_ArkUI\_PointerEvent\_GetDisplayY()

float OH\_ArkUI\_PointerEvent\_GetDisplayY(const ArkUI\_UIInputEvent\* event)

**Description**

Obtains the y-coordinate relative to the upper left corner of the current screen from a pointer event (such as a touch, mouse, or axis event).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [const ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md)\* event | Pointer to the UI input event. |

**Return value**

| Type | Description |
| :-- | :-- |
| float | Y-coordinate relative to the upper left corner of the current screen, in px. Returns **0.0f** if a parameter error occurs. |

#### \[h2\]OH\_ArkUI\_PointerEvent\_GetDisplayYByIndex()

float OH\_ArkUI\_PointerEvent\_GetDisplayYByIndex(const ArkUI\_UIInputEvent\* event, uint32\_t pointerIndex)

**Description**

Obtains the y-coordinate of a specific touch point relative to the upper left corner of the current screen from a pointer event (such as a touch, mouse, or axis event). For mouse and axis events, this API returns the default value of **0.0f** if the given index is greater than 0.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [const ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md)\* event | Pointer to the UI input event. |
| uint32\_t pointerIndex | Index of the target touch point in the multi-touch data list. |

**Return value**

| Type | Description |
| :-- | :-- |
| float | Y-coordinate of the specific touch point relative to the upper left corner of the current screen, in px. Returns **0.0f** if a parameter error occurs. |

#### \[h2\]OH\_ArkUI\_PointerEvent\_GetGlobalDisplayX()

float OH\_ArkUI\_PointerEvent\_GetGlobalDisplayX(const ArkUI\_UIInputEvent\* event)

**Description**

Obtains the x-coordinate relative to the global display from a pointer event (such as a touch, mouse, or axis event). The position information can be obtained only from a [ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md) event.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [const ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md)\* event | Pointer to the UI input event. |

**Return value**

| Type | Description |
| :-- | :-- |
| float | X-coordinate relative to the global display, in px. **0.0f** is returned if any parameter error occurs (for example, if the event does not contain position information). |

#### \[h2\]OH\_ArkUI\_PointerEvent\_GetGlobalDisplayXByIndex()

float OH\_ArkUI\_PointerEvent\_GetGlobalDisplayXByIndex(const ArkUI\_UIInputEvent\* event, uint32\_t pointerIndex)

**Description**

Obtains the x-coordinate relative to the global display from a pointer event (such as a touch, mouse, or axis event). Position information can only be obtained from UI input events. For mouse and axis events, if the provided **pointerIndex** is greater than 0, this API always returns the default value **0.0f**.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [const ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md)\* event | Pointer to the UI input event. |
| uint32\_t pointerIndex | Index of the target touch point in the multi-touch data list. Valid value range: \[0, [OH\_ArkUI\_PointerEvent\_GetPointerCount()](#oh_arkui_pointerevent_getpointercount) – 1\] |

**Return value**

| Type | Description |
| :-- | :-- |
| float | X-coordinate of the specific touch point relative to the global display, in px. Returns **0.0f** if any parameter error occurs. |

#### \[h2\]OH\_ArkUI\_PointerEvent\_GetGlobalDisplayY()

float OH\_ArkUI\_PointerEvent\_GetGlobalDisplayY(const ArkUI\_UIInputEvent\* event)

**Description**

Obtains the y-coordinate relative to the global display from a pointer event (such as a touch, mouse, or axis event). The position information can be obtained only from a [ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md) event.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [const ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md)\* event | Pointer to the UI input event. |

**Return value**

| Type | Description |
| :-- | :-- |
| float | Y-coordinate relative to the global display, in px. **0.0f** is returned if any parameter error occurs (for example, if the event does not contain position information). |

#### \[h2\]OH\_ArkUI\_PointerEvent\_GetGlobalDisplayYByIndex()

float OH\_ArkUI\_PointerEvent\_GetGlobalDisplayYByIndex(const ArkUI\_UIInputEvent\* event, uint32\_t pointerIndex)

**Description**

Obtains the y-coordinate relative to the global display from a pointer event (such as a touch, mouse, or axis event). Position information can only be obtained from UI input events. For mouse and axis events, if the provided **pointerIndex** is greater than 0, this API always returns the default value **0.0f**.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [const ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md)\* event | Pointer to the UI input event. |
| uint32\_t pointerIndex | Index of the target touch point in the multi-touch data list. Valid value range: \[0, [OH\_ArkUI\_PointerEvent\_GetPointerCount()](#oh_arkui_pointerevent_getpointercount) – 1\] |

**Return value**

| Type | Description |
| :-- | :-- |
| float | Y-coordinate relative to the global display, in px. Returns **0.0f** if any parameter error occurs. |

#### \[h2\]OH\_ArkUI\_PointerEvent\_GetPressure()

float OH\_ArkUI\_PointerEvent\_GetPressure(const ArkUI\_UIInputEvent\* event, uint32\_t pointerIndex)

**Description**

Obtains the pressure applied to the touchscreen from a pointer event (such as a touch event).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [const ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md)\* event | Pointer to the UI input event. |
| uint32\_t pointerIndex | Index of the target touch point in the multi-touch data list. |

**Return value**

| Type | Description |
| :-- | :-- |
| float | Touch pressure generated by the current pointer event. The value range is \[0, 1\]. The pressure is positively correlated with the value. If the parameter is abnormal, the default value **0.0f** is returned. On some devices, the return value may be greater than 1 due to different hardware parameter configurations. |

#### \[h2\]OH\_ArkUI\_PointerEvent\_GetTiltX()

float OH\_ArkUI\_PointerEvent\_GetTiltX(const ArkUI\_UIInputEvent\* event, uint32\_t pointerIndex)

**Description**

Obtains the angle relative to the YZ plane from a pointer event (for example, a touch event). The value range is \[-90, 90\], in deg. A positive value indicates a rightward tilt. This API is applicable only to stylus-based touch events from devices that support tilt angle reporting.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [const ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md)\* event | Pointer to the UI input event. |
| uint32\_t pointerIndex | Index of the target touch point in the multi-touch data list. |

**Return value**

| Type | Description |
| :-- | :-- |
| float | Angle relative to the YZ plane. |

#### \[h2\]OH\_ArkUI\_PointerEvent\_GetTiltY()

float OH\_ArkUI\_PointerEvent\_GetTiltY(const ArkUI\_UIInputEvent\* event, uint32\_t pointerIndex)

**Description**

Obtains the angle relative to the XZ plane from a pointer event (for example, a touch event). The value range is \[-90, 90\], in deg. A positive value indicates a downward tilt. This API is applicable only to stylus-based touch events from devices that support tilt angle reporting.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [const ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md)\* event | Pointer to the UI input event. |
| uint32\_t pointerIndex | Index of the target touch point in the multi-touch data list. |

**Return value**

| Type | Description |
| :-- | :-- |
| float | Angle relative to the XZ plane. |

#### \[h2\]OH\_ArkUI\_PointerEvent\_GetRollAngle()

int32\_t OH\_ArkUI\_PointerEvent\_GetRollAngle(const ArkUI\_UIInputEvent\* event, double\* rollAngle)

**Description**

Obtains the rotation angle of the stylus around the z-axis from a UI input event.

**Since**: 17

**Parameters**

| Name | Description |
| :-- | :-- |
| [const ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md)\* event | Pointer to the current UI input event. |
| double\* rollAngle | Rotation angle of the stylus around the z-axis, in deg. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_PointerEvent\_GetTouchAreaWidth()

float OH\_ArkUI\_PointerEvent\_GetTouchAreaWidth(const ArkUI\_UIInputEvent\* event, uint32\_t pointerIndex)

**Description**

Obtains the width of the touch area for a pointer event. This API is applicable only to finger-based touch events, and the return value typically represents the radius of a circular touch area.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [const ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md)\* event | Pointer to the UI input event. |
| uint32\_t pointerIndex | Index of the target touch point in the multi-touch data list. |

**Return value**

| Type | Description |
| :-- | :-- |
| float | Width of the touch area, in px. |

#### \[h2\]OH\_ArkUI\_PointerEvent\_GetTouchAreaHeight()

float OH\_ArkUI\_PointerEvent\_GetTouchAreaHeight(const ArkUI\_UIInputEvent\* event, uint32\_t pointerIndex)

**Description**

Obtains the height of the touch area for a pointer event. This API is applicable only to finger-based touch events, and the return value typically represents the radius of a circular touch area.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [const ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md)\* event | Pointer to the UI input event. |
| uint32\_t pointerIndex | Index of the target touch point in the multi-touch data list. |

**Return value**

| Type | Description |
| :-- | :-- |
| float | Height of the touch area, in px. |

#### \[h2\]OH\_ArkUI\_PointerEvent\_GetInteractionHand()

int32\_t OH\_ArkUI\_PointerEvent\_GetInteractionHand(const ArkUI\_UIInputEvent \*event, ArkUI\_InteractionHand \*hand)

**Description**

Checks whether an event is triggered by a left-hand or right-hand tap. This API is only effective on some touch devices. The value is not available immediately upon press. Until the system infers the result, this API will return **NONE**. Do not rely on the return value for critical functionality.

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| [const ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md) \*event | Pointer to the UI input event. |
| [ArkUI\_InteractionHand](#arkui_interactionhand) \*hand | Whether the touch point is from the left or right hand. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_PointerEvent\_GetInteractionHandByIndex()

int32\_t OH\_ArkUI\_PointerEvent\_GetInteractionHandByIndex(const ArkUI\_UIInputEvent \*event, int32\_t pointerIndex, ArkUI\_InteractionHand \*hand)

**Description**

Checks whether an event is triggered by a left-hand or right-hand tap. This API is only effective on some touch devices. The value is not available immediately upon press. Until the system infers the result, this API will return **NONE**. Do not rely on the return value for critical functionality.

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| [const ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md) \*event | Pointer to the UI input event. |
| int32\_t pointerIndex | Index of the target touch point in the multi-touch data list. |
| [ArkUI\_InteractionHand](#arkui_interactionhand) \*hand | Whether the touch point is from the left or right hand. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_PointerEvent\_GetHistorySize()

uint32\_t OH\_ArkUI\_PointerEvent\_GetHistorySize(const ArkUI\_UIInputEvent\* event)

**Description**

Obtains the number of historical events from a pointer event (such as a touch event). A historical event is the raw event that occurs between the current event and the previous event. This API is applicable only to the move phase (touch or mouse movement) of a pointer event. If this API is called in other states, the default value **0** is returned.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [const ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md)\* event | Pointer to the UI input event. |

**Return value**

| Type | Description |
| :-- | :-- |
| uint32\_t | Number of historical events. |

#### \[h2\]OH\_ArkUI\_PointerEvent\_GetHistoryEventTime()

int64\_t OH\_ArkUI\_PointerEvent\_GetHistoryEventTime(const ArkUI\_UIInputEvent\* event, uint32\_t historyIndex)

**Description**

Obtains the occurrence time of a historical event from a pointer event (such as a touch, mouse, or axis event).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [const ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md)\* event | Pointer to the UI input event. |
| uint32\_t historyIndex | Index of the target historical event. |

**Return value**

| Type | Description |
| :-- | :-- |
| int64\_t | Time when the UI input event occurs, in ns. Returns **0** if a parameter error occurs. |

#### \[h2\]OH\_ArkUI\_PointerEvent\_GetHistoryPointerCount()

uint32\_t OH\_ArkUI\_PointerEvent\_GetHistoryPointerCount(const ArkUI\_UIInputEvent\* event, uint32\_t historyIndex)

**Description**

Obtains the number of touch points in a specific historical event from a pointer event (such as a touch, mouse, or axis event).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [const ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md)\* event | Pointer to the UI input event. |
| uint32\_t historyIndex | Index of the target historical event. |

**Return value**

| Type | Description |
| :-- | :-- |
| uint32\_t | Number of touch points in the specified historical event. |

#### \[h2\]OH\_ArkUI\_PointerEvent\_GetHistoryPointerId()

int32\_t OH\_ArkUI\_PointerEvent\_GetHistoryPointerId(const ArkUI\_UIInputEvent\* event, uint32\_t pointerIndex, uint32\_t historyIndex)

**Description**

Obtains the unique ID of a touch point from a historical event of a pointer event (such as a touch event). The ID distinguishes between multiple touch points from the same input device. The return value itself does not have any other meaning beyond identifying the touch point.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [const ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md)\* event | Pointer to the UI input event. |
| uint32\_t pointerIndex | Index of the target touch point in the multi-touch data list. |
| uint32\_t historyIndex | Index of the target historical event. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | ID of the corresponding touch point in the specified historical event. |

#### \[h2\]OH\_ArkUI\_PointerEvent\_GetHistoryX()

float OH\_ArkUI\_PointerEvent\_GetHistoryX(const ArkUI\_UIInputEvent\* event, uint32\_t pointerIndex, uint32\_t historyIndex)

**Description**

Obtains the x-coordinate of a specific touch point in a specific historical event relative to the upper left corner of the current component from a pointer event (such as a touch, mouse, or axis event).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [const ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md)\* event | Pointer to the UI input event. |
| uint32\_t pointerIndex | Index of the target touch point in the multi-touch data list. |
| uint32\_t historyIndex | Index of the target historical event. |

**Return value**

| Type | Description |
| :-- | :-- |
| float | X-coordinate of the specific touch point in the specific historical event relative to the upper left corner of the current component, in px. Returns **0.0f** if a parameter error occurs. |

#### \[h2\]OH\_ArkUI\_PointerEvent\_GetHistoryY()

float OH\_ArkUI\_PointerEvent\_GetHistoryY(const ArkUI\_UIInputEvent\* event, uint32\_t pointerIndex, uint32\_t historyIndex)

**Description**

Obtains the y-coordinate of a specific touch point in a specific historical event relative to the upper left corner of the current component from a pointer event (such as a touch, mouse, or axis event).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [const ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md)\* event | Pointer to the UI input event. |
| uint32\_t pointerIndex | Index of the target touch point in the multi-touch data list. |
| uint32\_t historyIndex | Index of the target historical event. |

**Return value**

| Type | Description |
| :-- | :-- |
| float | Y-coordinate of the specific touch point in the specific historical event relative to the upper left corner of the current component, in px. Returns **0.0f** if a parameter error occurs. |

#### \[h2\]OH\_ArkUI\_PointerEvent\_GetHistoryWindowX()

float OH\_ArkUI\_PointerEvent\_GetHistoryWindowX(const ArkUI\_UIInputEvent\* event, uint32\_t pointerIndex, uint32\_t historyIndex)

**Description**

Obtains the x-coordinate of a specific touch point in a specific historical event relative to the upper left corner of the current application window from a pointer event (such as a touch, mouse, or axis event).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [const ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md)\* event | Pointer to the UI input event. |
| uint32\_t pointerIndex | Index of the target touch point in the multi-touch data list. |
| uint32\_t historyIndex | Index of the target historical event. |

**Return value**

| Type | Description |
| :-- | :-- |
| float | X-coordinate of the specific touch point in the specific historical event relative to the upper left corner of the current application window, in px. Returns **0.0f** if a parameter error occurs. |

#### \[h2\]OH\_ArkUI\_PointerEvent\_GetHistoryWindowY()

float OH\_ArkUI\_PointerEvent\_GetHistoryWindowY(const ArkUI\_UIInputEvent\* event, uint32\_t pointerIndex, uint32\_t historyIndex)

**Description**

Obtains the y-coordinate of a specific touch point in a specific historical event relative to the upper left corner of the current application window from a pointer event (such as a touch, mouse, or axis event).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [const ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md)\* event | Pointer to the UI input event. |
| uint32\_t pointerIndex | Index of the target touch point in the multi-touch data list. |
| uint32\_t historyIndex | Index of the target historical event. |

**Return value**

| Type | Description |
| :-- | :-- |
| float | Y-coordinate of the specific touch point in the specific historical event relative to the upper left corner of the current application window, in px. Returns **0.0f** if a parameter error occurs. |

#### \[h2\]OH\_ArkUI\_PointerEvent\_GetHistoryDisplayX()

float OH\_ArkUI\_PointerEvent\_GetHistoryDisplayX(const ArkUI\_UIInputEvent\* event, uint32\_t pointerIndex, uint32\_t historyIndex)

**Description**

Obtains the x-coordinate of a specific touch point in a specific historical event relative to the upper left corner of the current screen from a pointer event (such as a touch, mouse, or axis event).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [const ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md)\* event | Pointer to the UI input event. |
| uint32\_t pointerIndex | Index of the target touch point in the multi-touch data list. |
| uint32\_t historyIndex | Index of the target historical event. |

**Return value**

| Type | Description |
| :-- | :-- |
| float | X-coordinate of the specific touch point in the specific historical event relative to the upper left corner of the current screen, in px. Returns **0.0f** if a parameter error occurs. |

#### \[h2\]OH\_ArkUI\_PointerEvent\_GetHistoryDisplayY()

float OH\_ArkUI\_PointerEvent\_GetHistoryDisplayY(const ArkUI\_UIInputEvent\* event, uint32\_t pointerIndex, uint32\_t historyIndex)

**Description**

Obtains the y-coordinate of a specific touch point in a specific historical event relative to the upper left corner of the current screen from a pointer event (such as a touch, mouse, or axis event).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [const ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md)\* event | Pointer to the UI input event. |
| uint32\_t pointerIndex | Index of the target touch point in the multi-touch data list. |
| uint32\_t historyIndex | Index of the target historical event. |

**Return value**

| Type | Description |
| :-- | :-- |
| float | Y-coordinate of the specific touch point in the specific historical event relative to the upper left corner of the current screen, in px. Returns **0.0f** if a parameter error occurs. |

#### \[h2\]OH\_ArkUI\_PointerEvent\_GetHistoryGlobalDisplayX()

float OH\_ArkUI\_PointerEvent\_GetHistoryGlobalDisplayX(const ArkUI\_UIInputEvent\* event, uint32\_t pointerIndex, uint32\_t historyIndex)

**Description**

Obtains the x-coordinate relative to the global display for a specific touch point from historical events, based on the given pointer index and history index of an input event (such as a touch, mouse, or axis event). Position information can only be obtained from UI input events. For mouse and axis events, if the provided **pointerIndex** is greater than 0, this API always returns the default value **0.0f**.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [const ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md)\* event | Pointer to the UI input event. |
| uint32\_t pointerIndex | Index of the target touch point in the multi-touch data list. Valid value range: \[0, [OH\_ArkUI\_PointerEvent\_GetPointerCount()](#oh_arkui_pointerevent_getpointercount) – 1\] |
| uint32\_t historyIndex | Historical value to be returned. The value must be less than [OH\_ArkUI\_PointerEvent\_GetHistorySize](#oh_arkui_pointerevent_gethistorysize). |

**Return value**

| Type | Description |
| :-- | :-- |
| float | X-coordinate of the specific touch point in the specific historical event relative to the global display, in px. Returns **0.0f** if any parameter error occurs. |

#### \[h2\]OH\_ArkUI\_PointerEvent\_GetHistoryGlobalDisplayY()

float OH\_ArkUI\_PointerEvent\_GetHistoryGlobalDisplayY(const ArkUI\_UIInputEvent\* event, uint32\_t pointerIndex, uint32\_t historyIndex)

**Description**

Obtains the y-coordinate relative to the global display for a specific touch point from historical events, based on the given pointer index and history index of an input event (such as a touch, mouse, or axis event). Position information can only be obtained from UI input events. For mouse and axis events, if the provided **pointerIndex** is greater than 0, this API always returns the default value **0.0f**.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [const ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md)\* event | Pointer to the UI input event. |
| uint32\_t pointerIndex | Index of the target touch point in the multi-touch data list. Valid value range: \[0, [OH\_ArkUI\_PointerEvent\_GetPointerCount()](#oh_arkui_pointerevent_getpointercount) – 1\] |
| uint32\_t historyIndex | Historical value to be returned. The value must be less than [OH\_ArkUI\_PointerEvent\_GetHistorySize](#oh_arkui_pointerevent_gethistorysize). |

**Return value**

| Type | Description |
| :-- | :-- |
| float | Y-coordinate of the specific touch point in the specific historical event relative to the global display, in px. Returns **0.0f** if any parameter error occurs. |

#### \[h2\]OH\_ArkUI\_PointerEvent\_GetHistoryPressure()

float OH\_ArkUI\_PointerEvent\_GetHistoryPressure(const ArkUI\_UIInputEvent\* event, uint32\_t pointerIndex, uint32\_t historyIndex)

**Description**

Obtains the pressure applied to the touchscreen in a specific historical event from a pointer event (such as a touch event).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [const ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md)\* event | Pointer to the UI input event. |
| uint32\_t pointerIndex | Index of the target touch point in the multi-touch data list. |
| uint32\_t historyIndex | Index of the target historical event. |

**Return value**

| Type | Description |
| :-- | :-- |
| float | Touch pressure generated by the current pointer event. The value range is \[0, 1\]. The pressure is positively correlated with the value. If the parameter is abnormal, the default value **0.0f** is returned. On some devices, the return value may be greater than 1 due to different hardware parameter configurations. |

#### \[h2\]OH\_ArkUI\_PointerEvent\_GetHistoryTiltX()

float OH\_ArkUI\_PointerEvent\_GetHistoryTiltX(const ArkUI\_UIInputEvent\* event, uint32\_t pointerIndex, uint32\_t historyIndex)

**Description**

Obtains the angle relative to the YZ plane in a specific historical event from a pointer event (such as a touch event). The value range is \[-90, 90\], in deg. A positive value indicates a rightward tilt.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [const ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md)\* event | Pointer to the UI input event. |
| uint32\_t pointerIndex | Index of the target touch point in the multi-touch data list. |
| uint32\_t historyIndex | Index of the target historical event. |

**Return value**

| Type | Description |
| :-- | :-- |
| float | Angle relative to the YZ plane. |

#### \[h2\]OH\_ArkUI\_PointerEvent\_GetHistoryTiltY()

float OH\_ArkUI\_PointerEvent\_GetHistoryTiltY(const ArkUI\_UIInputEvent\* event, uint32\_t pointerIndex, uint32\_t historyIndex)

**Description**

Obtains the angle relative to the XZ plane in a specific historical event from a pointer event (such as a touch event). The value range is \[-90, 90\], in deg. A positive value indicates a downward tilt.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [const ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md)\* event | Pointer to the UI input event. |
| uint32\_t pointerIndex | Index of the target touch point in the multi-touch data list. |
| uint32\_t historyIndex | Index of the target historical event. |

**Return value**

| Type | Description |
| :-- | :-- |
| float | Angle relative to the XZ plane. |

#### \[h2\]OH\_ArkUI\_PointerEvent\_GetHistoryTouchAreaWidth()

float OH\_ArkUI\_PointerEvent\_GetHistoryTouchAreaWidth(const ArkUI\_UIInputEvent\* event, uint32\_t pointerIndex, uint32\_t historyIndex)

**Description**

Obtains the width of the touch area in a specific historical event from a pointer event (such as a touch event).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [const ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md)\* event | Pointer to the UI input event. |
| uint32\_t pointerIndex | Index of the target touch point in the multi-touch data list. |
| uint32\_t historyIndex | Index of the target historical event. |

**Return value**

| Type | Description |
| :-- | :-- |
| float | Width of the touch area, in px. |

#### \[h2\]OH\_ArkUI\_PointerEvent\_GetHistoryTouchAreaHeight()

float OH\_ArkUI\_PointerEvent\_GetHistoryTouchAreaHeight(const ArkUI\_UIInputEvent\* event, uint32\_t pointerIndex, uint32\_t historyIndex)

**Description**

Obtains the height of the touch area in a specific historical event from a pointer event (such as a touch event).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [const ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md)\* event | Pointer to the UI input event. |
| uint32\_t pointerIndex | Index of the target touch point in the multi-touch data list. |
| uint32\_t historyIndex | Index of the target historical event. |

**Return value**

| Type | Description |
| :-- | :-- |
| float | Height of the touch area, in px. |

#### \[h2\]OH\_ArkUI\_AxisEvent\_GetVerticalAxisValue()

double OH\_ArkUI\_AxisEvent\_GetVerticalAxisValue(const ArkUI\_UIInputEvent\* event)

**Description**

Obtains the value of the vertical scroll axis for this axis event. This value is typically generated by mouse wheel scrolling or two-finger vertical swiping on a touchpad. If the value is generated by mouse wheel scrolling: 1. The reported value is in degrees and represents the angular increment of a single scroll, not the total accumulation. 2. The reported value includes the user's scroll step configuration (see [OH\_ArkUI\_AxisEvent\_GetScrollStep](#oh_arkui_axisevent_getscrollstep)). 3. The sign of the value indicates the direction: positive for backward scrolling and negative for forward scrolling. If the value is generated by two-finger vertical swiping on a touchpad: 1. The reported value is in px and represents the scroll increment, not the total accumulation. 2. The reported value does not include the user's scroll step configuration [OH\_ArkUI\_AxisEvent\_GetScrollStep](#oh_arkui_axisevent_getscrollstep). 3. The sign of the value indicates the direction: positive for swiping up and negative for swiping down. 4. The direction is affected by the system settings for natural scrolling. Under normal circumstances, vertical scroll axis events only drive vertical swipe gestures. However, if the mouse pointer is over a scrollable area where the scrollable directions are consistent, the vertical scroll axis event can drive the swipe gestures in this scrollable area, even if they are defined as horizontal.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [const ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md)\* event | Pointer to the UI input event. |

**Return value**

| Type | Description |
| :-- | :-- |
| double | Value of the vertical scroll axis of the current axis event. Returns **0.0** if any parameter error occurs. |

#### \[h2\]OH\_ArkUI\_AxisEvent\_GetHorizontalAxisValue()

double OH\_ArkUI\_AxisEvent\_GetHorizontalAxisValue(const ArkUI\_UIInputEvent\* event)

**Description**

Obtains the value of the horizontal scroll axis for this axis event. This value is generated by two-finger horizontal swiping on a touchpad. Note: 1. The reported value is in px and represents the incremental scroll amount, not the total scroll amount. 2. The reported value does not include the user's scroll step configuration [OH\_ArkUI\_AxisEvent\_GetScrollStep](#oh_arkui_axisevent_getscrollstep). 3. The sign of the value indicates the direction: positive for swiping left and negative for swiping right. 4. The direction is affected by the system settings for natural scrolling.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [const ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md)\* event | Pointer to the UI input event. |

**Return value**

| Type | Description |
| :-- | :-- |
| double | Value of the horizontal scroll axis of the current axis event. Returns **0.0** if any parameter error occurs. |

#### \[h2\]OH\_ArkUI\_AxisEvent\_GetPinchAxisScaleValue()

double OH\_ArkUI\_AxisEvent\_GetPinchAxisScaleValue(const ArkUI\_UIInputEvent\* event)

**Description**

Obtains the scale value of the pinch axis for this axis event. This value is generated by a two-finger pinch gesture on a touchpad. The reported scale value is relative to the initial state when the system first detects the pinch gesture, with an initial scale value of 1.0. During the pinch operation, the scale value decreases from 1.0 towards 0.0 when the user pinches inward and increases from 1.0 when the user spreads fingers outward.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [const ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md)\* event | Pointer to the UI input event. |

**Return value**

| Type | Description |
| :-- | :-- |
| double | Scale value of the pinch axis of the current axis event. Returns **0.0** if any parameter error occurs. |

#### \[h2\]OH\_ArkUI\_AxisEvent\_GetAxisAction()

int32\_t OH\_ArkUI\_AxisEvent\_GetAxisAction(const ArkUI\_UIInputEvent\* event)

**Description**

Obtains the action type of this axis event.

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| [const ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md)\* event | Pointer to the UI input event. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | Action type of the current axis event. For details, see [anonymous7](#anonymous7). If a non-axis event is input, **0** is returned by default. |

#### \[h2\]OH\_ArkUI\_AxisEvent\_HasAxis()

int32\_t OH\_ArkUI\_AxisEvent\_HasAxis(const ArkUI\_UIInputEvent\* event, int32\_t axis)

**Description**

Checks whether this axis event contains the specified axis type.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [const ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md)\* event | Pointer to the UI input event. |
| int32\_t axis | Axis type of the axis event, specified using [UI\_AXIS\_TYPE\_XXX](#anonymous8). |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | Whether the current axis event contains the specified axis type. Returns **true** if the axis event contains the specified axis type, and **false** otherwise. |

#### \[h2\]OH\_ArkUI\_PointerEvent\_SetInterceptHitTestMode()

int32\_t OH\_ArkUI\_PointerEvent\_SetInterceptHitTestMode(const ArkUI\_UIInputEvent\* event, HitTestMode mode)

**Description**

Sets the touch test mode. This API only applies to scenarios raw input events are received, such as when **NODE\_ON\_TOUCH** is used for touch event handling. It cannot be used with **ArkUI\_UIInputEvent** objects obtained from gesture events through [OH\_ArkUI\_GestureEvent\_GetRawInputEvent](../native-gesture-h/document.md#oh_arkui_gestureevent_getrawinputevent).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [const ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md)\* event | Pointer to the UI input event. |
| [HitTestMode](#hittestmode) mode | Touch test mode. The parameter type is [HitTestMode](#hittestmode). |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | Result code. |

#### \[h2\]OH\_ArkUI\_MouseEvent\_GetMouseButton()

int32\_t OH\_ArkUI\_MouseEvent\_GetMouseButton(const ArkUI\_UIInputEvent\* event)

**Description**

Obtains the button type of a mouse event.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [const ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md)\* event | Pointer to the UI input event. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | Mouse button type. The value is defined by the [anonymous5](#anonymous5) enumeration. If the API is called in a non-mouse event, the return value is **\-1**. |

#### \[h2\]OH\_ArkUI\_MouseEvent\_GetMouseAction()

int32\_t OH\_ArkUI\_MouseEvent\_GetMouseAction(const ArkUI\_UIInputEvent\* event)

**Description**

Obtains the action type of a mouse event.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [const ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md)\* event | Pointer to the UI input event. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | Mouse action type. The value is defined by the [anonymous4](#anonymous4) enumeration. If the API is called in a non-mouse event, the return value is **\-1**. |

#### \[h2\]OH\_ArkUI\_PointerEvent\_SetStopPropagation()

int32\_t OH\_ArkUI\_PointerEvent\_SetStopPropagation(const ArkUI\_UIInputEvent\* event, bool stopPropagation)

**Description**

Sets whether to stop event propagation. This API only applies to scenarios raw input events are received, such as when **NODE\_ON\_TOUCH** is used for touch event handling, and does not apply to axis events. It cannot be used with **ArkUI\_UIInputEvent** objects obtained from gesture events through [OH\_ArkUI\_GestureEvent\_GetRawInputEvent](../native-gesture-h/document.md#oh_arkui_gestureevent_getrawinputevent).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [const ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md)\* event | Pointer to the UI input event. |
| bool stopPropagation | Whether to stop event propagation. The value **true** means to stop event propagation, and **false** means the opposite. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | Result code. Returns **0** if the operation is successful; returns **401** if the operation fails, possibly because a parameter error, for example, null pointer for the **event** parameter, occurs. |

#### \[h2\]OH\_ArkUI\_UIInputEvent\_GetDeviceId()

int32\_t OH\_ArkUI\_UIInputEvent\_GetDeviceId(const ArkUI\_UIInputEvent\* event)

**Description**

Obtains the device ID of the current UI input event.

**Since**: 14

**Parameters**

| Name | Description |
| :-- | :-- |
| [const ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md)\* event | Pointer to the target **ArkUI\_UIInputEvent** object. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | Device ID of the current UI input event. |

#### \[h2\]OH\_ArkUI\_UIInputEvent\_GetPressedKeys()

int32\_t OH\_ArkUI\_UIInputEvent\_GetPressedKeys(const ArkUI\_UIInputEvent\* event, int32\_t\* pressedKeyCodes, int32\_t\* length)

**Description**

Obtains all pressed keys. Currently, only key events are supported.

**Since**: 14

**Parameters**

| Name | Description |
| :-- | :-- |
| [const ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md)\* event | Pointer to the target **ArkUI\_UIInputEvent** object. |
| int32\_t\* pressedKeyCodes | Array of all pressed keys. The caller is responsible for allocating the memory space to which the array points. |
| int32\_t\* length | Dual-purpose parameter: As input, it indicates the length of the provided **pressedKeyCodes** array; as output, it indicates the number of pressed keys. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_BUFFER\_SIZE\_NOT\_ENOUGH](../native-type-h/document.md#arkui_errorcode) if the memory is insufficient.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_FocusAxisEvent\_GetAxisValue()

double OH\_ArkUI\_FocusAxisEvent\_GetAxisValue(const ArkUI\_UIInputEvent\* event, int32\_t axis)

**Description**

Obtains the axis value of a focus axis event.

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| [const ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md)\* event | Pointer to the target **ArkUI\_UIInputEvent** object. |
| int32\_t axis | Axis type of the focus axis event. For details, see [anonymous6](#anonymous6). |

**Return value**

| Type | Description |
| :-- | :-- |
| double | Axis value of the focus axis event. Returns **0.0** if any parameter error occurs. |

#### \[h2\]OH\_ArkUI\_FocusAxisEvent\_SetStopPropagation()

int32\_t OH\_ArkUI\_FocusAxisEvent\_SetStopPropagation(const ArkUI\_UIInputEvent\* event, bool stopPropagation)

**Description**

Sets whether to prevent a focus axis event from bubbling up.

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| [const ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md)\* event | Pointer to the UI input event. |
| bool stopPropagation | Whether to stop event propagation. The value **true** means to stop event propagation, and **false** means the opposite. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_UIInputEvent\_GetModifierKeyStates()

int32\_t OH\_ArkUI\_UIInputEvent\_GetModifierKeyStates(const ArkUI\_UIInputEvent\* event, uint64\_t\* keys)

**Description**

Obtains the modifier key states for a UI input event. This API outputs the state of all modifier keys at the time of the event through the **keys** parameter. You can determine which keys are pressed by performing bitwise operations with the modifier key types defined in [ArkUI\_ModifierKeyName](#arkui_modifierkeyname).

**Since**: 17

**Parameters**

| Name | Description |
| :-- | :-- |
| [const ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md)\* event | Pointer to the target **ArkUI\_UIInputEvent** object. |
| uint64\_t\* keys | Pointer to the combination of pressed modifier keys. The application can use bitwise operations to determine which keys are pressed. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_AxisEvent\_SetPropagation()

int32\_t OH\_ArkUI\_AxisEvent\_SetPropagation(const ArkUI\_UIInputEvent\* event, bool propagation)

**Description**

Sets whether to enable axis event propagation (bubbling). By default, axis events do not bubble and are only sent to the first component that can respond to axis events. You can enable axis event bubbling when an axis event is received to allow the event to be passed to the next ancestor component in the response chain that can handle axis events. This API cannot be used on axis events obtained from gesture events.

**Since**: 17

**Parameters**

| Name | Description |
| :-- | :-- |
| [const ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md)\* event | Pointer to the UI input event. |
| bool propagation | Whether to enable event propagation. The value **true** means to enable event propagation, and **false** means the opposite. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_AxisEvent\_GetScrollStep()

int32\_t OH\_ArkUI\_AxisEvent\_GetScrollStep(const ArkUI\_UIInputEvent\* event)

**Description**

Obtains the scroll step coefficient for a wheel-based axis event. This API returns the user-configured scroll scale factor.

**Since**: 17

**Parameters**

| Name | Description |
| :-- | :-- |
| [const ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md)\* event | Pointer to the **ArkUI\_UIInputEvent** object. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | Scroll step configuration of the mouse wheel axis event. For non-mouse events, the default value **0** is returned. |

#### \[h2\]OH\_ArkUI\_UIInputEvent\_GetEventTargetWidth()

float OH\_ArkUI\_UIInputEvent\_GetEventTargetWidth(const ArkUI\_UIInputEvent\* event)

**Description**

Obtains the width of the component hit by an event.

**Since**: 17

**Parameters**

| Name | Description |
| :-- | :-- |
| [const ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md)\* event | Pointer to the **ArkUI\_UIInputEvent** object. |

**Return value**

| Type | Description |
| :-- | :-- |
| float | Width of the component hit by an event, in pixels. If any parameter error occurs, **0.0f** is returned. |

#### \[h2\]OH\_ArkUI\_UIInputEvent\_GetEventTargetHeight()

float OH\_ArkUI\_UIInputEvent\_GetEventTargetHeight(const ArkUI\_UIInputEvent\* event)

**Description**

Obtains the height of the component hit by an event.

**Since**: 17

**Parameters**

| Name | Description |
| :-- | :-- |
| [const ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md)\* event | Pointer to the **ArkUI\_UIInputEvent** object. |

**Return value**

| Type | Description |
| :-- | :-- |
| float | Height of the component hit by an event, in pixels. If any parameter error occurs, **0.0f** is returned. |

#### \[h2\]OH\_ArkUI\_UIInputEvent\_GetEventTargetPositionX()

float OH\_ArkUI\_UIInputEvent\_GetEventTargetPositionX(const ArkUI\_UIInputEvent\* event)

**Description**

Obtains the x-coordinate of the component hit by an event.

**Since**: 17

**Parameters**

| Name | Description |
| :-- | :-- |
| [const ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md)\* event | Pointer to the **ArkUI\_UIInputEvent** object. |

**Return value**

| Type | Description |
| :-- | :-- |
| float | X-coordinate of the component hit by an event, in pixels. If any parameter error occurs, **0.0f** is returned. |

#### \[h2\]OH\_ArkUI\_UIInputEvent\_GetEventTargetPositionY()

float OH\_ArkUI\_UIInputEvent\_GetEventTargetPositionY(const ArkUI\_UIInputEvent\* event)

**Description**

Obtains the y-coordinate of the component hit by an event.

**Since**: 17

**Parameters**

| Name | Description |
| :-- | :-- |
| [const ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md)\* event | Pointer to the **ArkUI\_UIInputEvent** object. |

**Return value**

| Type | Description |
| :-- | :-- |
| float | Y-coordinate of the component hit by an event, in pixels. If any parameter error occurs, **0.0f** is returned. |

#### \[h2\]OH\_ArkUI\_UIInputEvent\_GetEventTargetGlobalPositionX()

float OH\_ArkUI\_UIInputEvent\_GetEventTargetGlobalPositionX(const ArkUI\_UIInputEvent\* event)

**Description**

Obtains the global x-coordinate of the component hit by an event.

**Since**: 17

**Parameters**

| Name | Description |
| :-- | :-- |
| [const ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md)\* event | Pointer to the **ArkUI\_UIInputEvent** object. |

**Return value**

| Type | Description |
| :-- | :-- |
| float | Global x-coordinate of the component hit by an event, in pixels. If any parameter error occurs, **0.0f** is returned. |

#### \[h2\]OH\_ArkUI\_UIInputEvent\_GetEventTargetGlobalPositionY()

float OH\_ArkUI\_UIInputEvent\_GetEventTargetGlobalPositionY(const ArkUI\_UIInputEvent\* event)

**Description**

Obtains the global y-coordinate of the component hit by an event.

**Since**: 17

**Parameters**

| Name | Description |
| :-- | :-- |
| [const ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md)\* event | Pointer to the **ArkUI\_UIInputEvent** object. |

**Return value**

| Type | Description |
| :-- | :-- |
| float | Global y-coordinate of the component hit by an event, in pixels. If any parameter error occurs, **0.0f** is returned. |

#### \[h2\]OH\_ArkUI\_PointerEvent\_GetPressedTimeByIndex()

int64\_t OH\_ArkUI\_PointerEvent\_GetPressedTimeByIndex(const ArkUI\_UIInputEvent\* event, uint32\_t pointerIndex)

**Description**

Obtains the press time of a specified touch point. This API is effective only for touch events.

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| [const ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md)\* event | Pointer to the target **ArkUI\_UIInputEvent** object. |
| uint32\_t pointerIndex | Index of the target touch point in the multi-touch data list. |

**Return value**

| Type | Description |
| :-- | :-- |
| int64\_t | Press time of the specific touch point, in ns. Returns **0** if any parameter error occurs. |

#### \[h2\]OH\_ArkUI\_MouseEvent\_GetRawDeltaX()

float OH\_ArkUI\_MouseEvent\_GetRawDeltaX(const ArkUI\_UIInputEvent\* event)

**Description**

Obtains the movement increment of the mouse along the X axis in a two-dimensional plane. The value is the original movement data of the mouse hardware, which is expressed in the unit of the mouse movement distance in the physical world. The reported value is determined by the hardware, not the physical or logical pixels of the screen.

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| [const ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md)\* event | Pointer to the target **ArkUI\_UIInputEvent** object. |

**Return value**

| Type | Description |
| :-- | :-- |
| float | Returns the movement increment of the mouse device along the X axis in the two-dimensional plane, which is expressed in the unit of the mouse movement distance in the physical world. If any parameter error occurs, **0.0f** is returned. |

#### \[h2\]OH\_ArkUI\_MouseEvent\_GetRawDeltaY()

float OH\_ArkUI\_MouseEvent\_GetRawDeltaY(const ArkUI\_UIInputEvent\* event)

**Description**

Obtains the movement increment of the mouse along the Y axis in a two-dimensional plane. The value is the original movement data of the mouse hardware, which is expressed in the unit of the mouse movement distance in the physical world. The reported value is determined by the hardware, not the physical or logical pixels of the screen.

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| [const ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md)\* event | Pointer to the target **ArkUI\_UIInputEvent** object. |

**Return value**

| Type | Description |
| :-- | :-- |
| float | Returns the movement increment of the mouse device along the Y axis in the two-dimensional plane, which is expressed in the unit of the mouse movement distance in the physical world. If any parameter error occurs, **0.0f** is returned. |

#### \[h2\]OH\_ArkUI\_MouseEvent\_GetPressedButtons()

int32\_t OH\_ArkUI\_MouseEvent\_GetPressedButtons(const ArkUI\_UIInputEvent\* event, int32\_t\* pressedButtons, int32\_t\* length)

**Description**

Obtains the pressed buttons from a mouse event.

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| [const ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md)\* event | Pointer to the target **ArkUI\_UIInputEvent** object. |
| int32\_t\* pressedButtons | Array of the pressed buttons. Create an integer array to store the button values. For button code definitions, see [anonymous5](#anonymous5). |
| int32\_t\* length | Total length of the array. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_BUFFER\_SIZE\_ERROR](../native-type-h/document.md#arkui_errorcode) if the input buffer size is invalid.

 |

#### \[h2\]OH\_ArkUI\_UIInputEvent\_GetTargetDisplayId()

int32\_t OH\_ArkUI\_UIInputEvent\_GetTargetDisplayId(const ArkUI\_UIInputEvent\* event)

**Description**

Obtains the ID of the screen where the UI input event occurs.

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| [const ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md)\* event | Pointer to the target **ArkUI\_UIInputEvent** object. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | Screen ID. Returns **0** if any parameter error occurs. |

#### \[h2\]OH\_ArkUI\_HoverEvent\_IsHovered()

bool OH\_ArkUI\_HoverEvent\_IsHovered(const ArkUI\_UIInputEvent\* event)

**Description**

Checks whether the cursor is hovering over this component.

**Since**: 17

**Parameters**

| Name | Description |
| :-- | :-- |
| [const ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md)\* event | Pointer to the target **ArkUI\_UIInputEvent** object. |

**Return value**

| Type | Description |
| :-- | :-- |
| bool | 
Returns **true** if the cursor is hovering over the current component.

Returns **false** if the cursor is not hovering over the current component.

 |

#### \[h2\]OH\_ArkUI\_PointerEvent\_CreateClonedEvent()

int32\_t OH\_ArkUI\_PointerEvent\_CreateClonedEvent(const ArkUI\_UIInputEvent\* event, ArkUI\_UIInputEvent\*\* clonedEvent)

**Description**

Creates a cloned event pointer based on an event pointer. This API is effective only for touch events.

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| [const ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md)\* event | Pointer to the target **ArkUI\_UIInputEvent** object. |
| [ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md)\*\* clonedEvent | Pointer to the target **ArkUI\_UIInputEvent** object. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_PointerEvent\_DestroyClonedEvent()

int32\_t OH\_ArkUI\_PointerEvent\_DestroyClonedEvent(const ArkUI\_UIInputEvent\* event)

**Description**

Destroys a cloned event pointer.

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| [const ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md)\* event | Pointer to the target **ArkUI\_UIInputEvent** object. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_NOT\_CLONED\_POINTER\_EVENT](../native-type-h/document.md#arkui_errorcode) if the input event pointer is not a cloned event pointer.

 |

#### \[h2\]OH\_ArkUI\_PointerEvent\_SetClonedEventLocalPosition()

int32\_t OH\_ArkUI\_PointerEvent\_SetClonedEventLocalPosition(const ArkUI\_UIInputEvent\* event, float x, float y)

**Description**

Sets the x-coordinate and y-coordinate of a cloned event relative to the upper left corner of the current component.

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| [const ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md)\* event | Pointer to the target **ArkUI\_UIInputEvent** object. |
| float x | X-coordinate relative to the upper left corner of the current component, in px. |
| float y | Y-coordinate relative to the upper left corner of the current component, in px. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_NOT\_CLONED\_POINTER\_EVENT](../native-type-h/document.md#arkui_errorcode) if the input event pointer is not a cloned event pointer.

 |

#### \[h2\]OH\_ArkUI\_PointerEvent\_SetClonedEventLocalPositionByIndex()

int32\_t OH\_ArkUI\_PointerEvent\_SetClonedEventLocalPositionByIndex(const ArkUI\_UIInputEvent\* event, float x, float y, int32\_t pointerIndex)

**Description**

Sets the x-coordinate and y-coordinate of a specific touch point of a cloned event relative to the upper left corner of the current component.

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| [const ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md)\* event | Pointer to the target **ArkUI\_UIInputEvent** object. |
| float x | X-coordinate relative to the upper left corner of the current component, in px. |
| float y | Y-coordinate relative to the upper left corner of the current component, in px. |
| int32\_t pointerIndex | Index of the target touch point in the multi-touch data list. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_NOT\_CLONED\_POINTER\_EVENT](../native-type-h/document.md#arkui_errorcode) if the input event pointer is not a cloned event pointer.

 |

#### \[h2\]OH\_ArkUI\_PointerEvent\_SetClonedEventActionType()

int32\_t OH\_ArkUI\_PointerEvent\_SetClonedEventActionType(const ArkUI\_UIInputEvent\* event, int32\_t actionType)

**Description**

Sets the action type of a cloned event.

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| [const ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md)\* event | Pointer to the target **ArkUI\_UIInputEvent** object. |
| int32\_t actionType | Action type of the cloned event. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_NOT\_CLONED\_POINTER\_EVENT](../native-type-h/document.md#arkui_errorcode) if the input event pointer is not a cloned event pointer.

 |

#### \[h2\]OH\_ArkUI\_PointerEvent\_SetClonedEventChangedFingerId()

int32\_t OH\_ArkUI\_PointerEvent\_SetClonedEventChangedFingerId(const ArkUI\_UIInputEvent\* event, int32\_t fingerId)

**Description**

Sets the touch point ID of a cloned pointer event.

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| [const ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md)\* event | Pointer to the target **ArkUI\_UIInputEvent** object. |
| int32\_t fingerId | ID of the touch point that triggers the event. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_NOT\_CLONED\_POINTER\_EVENT](../native-type-h/document.md#arkui_errorcode) if the input event pointer is not a cloned event pointer.

 |

#### \[h2\]OH\_ArkUI\_PointerEvent\_SetClonedEventFingerIdByIndex()

int32\_t OH\_ArkUI\_PointerEvent\_SetClonedEventFingerIdByIndex(const ArkUI\_UIInputEvent\* event, int32\_t fingerId, int32\_t pointerIndex)

**Description**

Sets the touch point ID of a specific touch point of a cloned event.

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| [const ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md)\* event | Pointer to the target **ArkUI\_UIInputEvent** object. |
| int32\_t fingerId | Touch point ID of the specific touch point. |
| int32\_t pointerIndex | Index of the target touch point in the multi-touch data list. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_NOT\_CLONED\_POINTER\_EVENT](../native-type-h/document.md#arkui_errorcode) if the input event pointer is not a cloned event pointer.

 |

#### \[h2\]OH\_ArkUI\_PointerEvent\_PostClonedEvent()

int32\_t OH\_ArkUI\_PointerEvent\_PostClonedEvent(ArkUI\_NodeHandle node, const ArkUI\_UIInputEvent\* event)

**Description**

Posts a cloned event to a specific node.

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) node | Target node. |
| [const ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md)\* event | Pointer to the target **ArkUI\_UIInputEvent** object. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_NOT\_CLONED\_POINTER\_EVENT](../native-type-h/document.md#arkui_errorcode) if the input event pointer is not a cloned event pointer.

Returns [ARKUI\_ERROR\_CODE\_POST\_CLONED\_COMPONENT\_STATUS\_ABNORMAL](../native-type-h/document.md#arkui_errorcode) if the component status is abnormal.

Returns [ARKUI\_ERROR\_CODE\_POST\_CLONED\_NO\_COMPONENT\_HIT\_TO\_RESPOND\_TO\_THE\_EVENT](../native-type-h/document.md#arkui_errorcode) if no component is hit to respond to the event.

 |

#### \[h2\]OH\_ArkUI\_UIInputEvent\_GetLatestStatus()

ArkUI\_ErrorCode OH\_ArkUI\_UIInputEvent\_GetLatestStatus()

**Description**

Obtains the result code of the most recent API call related to an **ArkUI\_UIInputEvent** object. This API is typically unnecessary for normal operations, but can be used to verify ambiguous return values

**Since**: 20

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_ErrorCode](../native-type-h/document.md#arkui_errorcode) | Result code of the most recent API call related to the **ArkUI\_UIInputEvent** object. |

#### \[h2\]OH\_ArkUI\_UIInputEvent\_GetCoastingAxisEvent()

ArkUI\_CoastingAxisEvent\* OH\_ArkUI\_UIInputEvent\_GetCoastingAxisEvent(ArkUI\_UIInputEvent\* event)

**Description**

Obtains the coasting axis event from the specified component event. A valid event is available only when the user slides two fingers a certain distance on the touchpad and quickly releases them, and a component registered with the [NODE\_ON\_COASTING\_AXIS\_EVENT](../native-node-h/document.md#arkui_nodeeventtype) event exists at the pointer position. This API must be called after the [ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md) object is obtained from the [ArkUI\_NodeEvent](../../structs/arkui-nodeevent/document.md) object.

The coasting axis event is triggered only when the user performs a two-finger swipe and releases on the touchpad, so it is exclusive to touchpad devices. This event generates axis values that gradually attenuate based on the initial swipe velocity after finger release. Due to factors such as refresh rate and performance constraints, the axis value of the current event may be higher or lower than the previous one. The following behavior will interrupt the coasting axis event and immediately trigger [ARKUI\_COASTING\_AXIS\_EVENT\_PHASE\_END](#arkui_coastingaxiseventphase):

1.  Touching the touchpad
    
2.  Scrolling the mouse wheel
    
3.  Clicking a node registered for coasting axis events (clicking unregistered nodes has no effect). For example, if node A registers the event and node B is being scrolled during coasting, clicking node B will not interrupt the event. Click event interruption is affected by the [HitTest mode](#oh_arkui_pointerevent_setintercepthittestmode). If the tapped area contains any nodes that can respond to coasting axis events, the coasting axis event will be forcibly terminated.
    
4.  Application hibernation (such as minimization and screen lock)
    

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md)\* event | Pointer to the target **ArkUI\_UIInputEvent** object. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_CoastingAxisEvent](../../structs/arkui-coastingaxisevent/document.md) | Pointer to the coasting axis event. Returns a null pointer if no coasting axis event occurs or if parameters are invalid. |

#### \[h2\]OH\_ArkUI\_CoastingAxisEvent\_GetEventTime()

int64\_t OH\_ArkUI\_CoastingAxisEvent\_GetEventTime(ArkUI\_CoastingAxisEvent\* event)

**Description**

Obtains the time when a coasting axis event occurs.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_CoastingAxisEvent](../../structs/arkui-coastingaxisevent/document.md)\* event | Pointer to the coasting axis event. |

**Return value**

| Type | Description |
| :-- | :-- |
| int64\_t | Time when the UI input event occurs, in ns. If any parameter error occurs, **0** is returned. |

#### \[h2\]OH\_ArkUI\_CoastingAxisEvent\_GetPhase()

ArkUI\_CoastingAxisEventPhase OH\_ArkUI\_CoastingAxisEvent\_GetPhase(ArkUI\_CoastingAxisEvent\* event)

**Description**

Obtains the scroll phase of the specified coasting axis event.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_CoastingAxisEvent](../../structs/arkui-coastingaxisevent/document.md)\* event | Pointer to the coasting axis event. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_CoastingAxisEventPhase](#arkui_coastingaxiseventphase) | 
Event phase. For details, see [ArkUI\_CoastingAxisEventPhase](#arkui_coastingaxiseventphase).

Returns **ARKUI\_COASTING\_AXIS\_EVENT\_PHASE\_NONE** if any parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_CoastingAxisEvent\_GetDeltaY

float OH\_ArkUI\_CoastingAxisEvent\_GetDeltaY(ArkUI\_CoastingAxisEvent\* event)

**Description**

Obtains the vertical delta value of the specified coasting axis event. Unit: px, representing the single scroll increment (not the total scroll amount). Negative values indicate a downward direction (fingers swiping from top to bottom), and positive values indicate an upward direction (fingers swiping from bottom to top).

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_CoastingAxisEvent](../../structs/arkui-coastingaxisevent/document.md)\* event | Pointer to the coasting axis event. |

**Return value**

| Type | Description |
| :-- | :-- |
| float | Y-axis delta value, in px. Returns **0.0f** if any parameter error occurs. |

#### \[h2\]OH\_ArkUI\_CoastingAxisEvent\_GetDeltaX

float OH\_ArkUI\_CoastingAxisEvent\_GetDeltaX(ArkUI\_CoastingAxisEvent\* event)

**Description**

Obtains the horizontal delta value of the specified coasting axis event. Unit: px, representing the single scroll increment (not the total scroll amount). Positive values indicate a rightward direction (fingers swiping from right to left), and negative values indicate a leftward direction (fingers swiping from left to right).

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_CoastingAxisEvent](../../structs/arkui-coastingaxisevent/document.md)\* event | Pointer to the coasting axis event. |

**Return value**

| Type | Description |
| :-- | :-- |
| float | X-axis delta value, in px. Returns **0.0f** if any parameter error occurs. |

#### \[h2\]OH\_ArkUI\_CoastingAxisEvent\_SetPropagation()

int32\_t OH\_ArkUI\_CoastingAxisEvent\_SetPropagation(ArkUI\_CoastingAxisEvent\* event, bool propagation)

**Description**

Sets whether to enable event propagation for the specified coasting axis event. By default, event propagation is disabled.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_CoastingAxisEvent](../../structs/arkui-coastingaxisevent/document.md)\* event | Pointer to the coasting axis event. |
| bool propagation | Whether to enable event propagation. **true**: enable; **false**: disable. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_TouchTestInfo\_GetTouchTestInfoList

ArkUI\_ErrorCode OH\_ArkUI\_TouchTestInfo\_GetTouchTestInfoList(ArkUI\_TouchTestInfo\* info,
    ArkUI\_TouchTestInfoItemArray\* array, int32\_t\* size);

**Description**

Obtains the array of touch test information items.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_TouchTestInfo](../../structs/arkui-touchtestinfo/document.md)\* info | Pointer to the touch test information. |
| [ArkUI\_TouchTestInfoItemArray](../../structs/arkui-touchtestinfoitemhandle/document.md)\* array | Pointer to the array of touch test information items. |
| int32\_t\* size | Size of the array of touch test information items. |

**Return value**

| Type | Description |
| :-- | :-- |
| ArkUI\_ErrorCode | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_TouchTestInfoItem\_GetX

float OH\_ArkUI\_TouchTestInfoItem\_GetX(const ArkUI\_TouchTestInfoItem\* info);

**Description**

Obtains the X coordinate relative to the upper left corner of the child component from the touch test information item, in px.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| const [ArkUI\_TouchTestInfoItem](../../structs/arkui-touchtestinfoitem/document.md)\* info | Pointer to a touch test information item. |

**Return value**

| Type | Description |
| :-- | :-- |
| float | X coordinate relative to the upper left corner of the child component, in px. If the parameter value is incorrect, **0.0f** is returned. |

#### \[h2\]OH\_ArkUI\_TouchTestInfoItem\_GetY

float OH\_ArkUI\_TouchTestInfoItem\_GetY(const ArkUI\_TouchTestInfoItem\* info);

**Description**

Obtains the Y coordinate relative to the upper left corner of the child component from the touch test information item, in px.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| const [ArkUI\_TouchTestInfoItem](../../structs/arkui-touchtestinfoitem/document.md)\* info | Pointer to a touch test information item. |

**Return value**

| Type | Description |
| :-- | :-- |
| float | Y coordinate relative to the upper left corner of the child component, in px. If the parameter value is incorrect, **0.0f** is returned. |

#### \[h2\]OH\_ArkUI\_TouchTestInfoItem\_GetWindowX

float OH\_ArkUI\_TouchTestInfoItem\_GetWindowX(const ArkUI\_TouchTestInfoItem\* info);

**Description**

Obtains the X coordinate relative to the upper left corner of the current application window from the touch test information item, in px.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| const [ArkUI\_TouchTestInfoItem](../../structs/arkui-touchtestinfoitem/document.md)\* info | Pointer to a touch test information item. |

**Return value**

| Type | Description |
| :-- | :-- |
| float | X coordinate relative to the upper left corner of the current application window, in px. If the parameter value is incorrect, **0.0f** is returned. |

#### \[h2\]OH\_ArkUI\_TouchTestInfoItem\_GetWindowY

float OH\_ArkUI\_TouchTestInfoItem\_GetWindowY(const ArkUI\_TouchTestInfoItem\* info);

**Description**

Obtains the Y coordinate relative to the upper left corner of the current application window from the touch test information item, in px.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| const [ArkUI\_TouchTestInfoItem](../../structs/arkui-touchtestinfoitem/document.md)\* info | Pointer to a touch test information item. |

**Return value**

| Type | Description |
| :-- | :-- |
| float | Y coordinate relative to the upper left corner of the current application window, in px. If the parameter value is incorrect, **0.0f** is returned. |

#### \[h2\]OH\_ArkUI\_TouchTestInfoItem\_GetXRelativeToParent

float OH\_ArkUI\_TouchTestInfoItem\_GetXRelativeToParent(const ArkUI\_TouchTestInfoItem\* info);

**Description**

Obtains the X coordinate relative to the upper left corner of the parent component from the touch test information item, in px.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| const [ArkUI\_TouchTestInfoItem](../../structs/arkui-touchtestinfoitem/document.md)\* info | Pointer to a touch test information item. |

**Return value**

| Type | Description |
| :-- | :-- |
| float | X coordinate relative to the upper left corner of the parent component, in px. If the parameter value is incorrect, **0.0f** is returned. |

#### \[h2\]OH\_ArkUI\_TouchTestInfoItem\_GetYRelativeToParent

float OH\_ArkUI\_TouchTestInfoItem\_GetYRelativeToParent(const ArkUI\_TouchTestInfoItem\* info);

**Description**

Obtains the Y coordinate relative to the upper left corner of the parent component from the touch test information item, in px.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| const [ArkUI\_TouchTestInfoItem](../../structs/arkui-touchtestinfoitem/document.md)\* info | Pointer to a touch test information item. |

**Return value**

| Type | Description |
| :-- | :-- |
| float | Y coordinate relative to the upper left corner of the parent component, in px. If the parameter value is incorrect, **0.0f** is returned. |

#### \[h2\]OH\_ArkUI\_TouchTestInfoItem\_GetChildRect

ArkUI\_ErrorCode OH\_ArkUI\_TouchTestInfoItem\_GetChildRect(const ArkUI\_TouchTestInfoItem\* info, ArkUI\_Rect\* childRect);

**Description**

Obtains the boundary rectangle information of the child component from the touch test information item.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| const [ArkUI\_TouchTestInfoItem](../../structs/arkui-touchtestinfoitem/document.md)\* info | Pointer to a touch test information item. |
| [ArkUI\_Rect](../../structs/arkui-rect/document.md)\* childRect | Pointer to the boundary rectangle of the child component, which is used to store the obtained boundary rectangle information. |

**Return value**

| Type | Description |
| :-- | :-- |
| ArkUI\_ErrorCode | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_TouchTestInfoItem\_GetChildId

ArkUI\_ErrorCode OH\_ArkUI\_TouchTestInfoItem\_GetChildId(const ArkUI\_TouchTestInfoItem\* info, char\* buffer,
    int32\_t bufferSize);

**Description**

Obtains the ID of the child component from the touch test information item.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| const [ArkUI\_TouchTestInfoItem](../../structs/arkui-touchtestinfoitem/document.md)\* info | Pointer to a touch test information item. |
| char\* buffer | Storage buffer. |
| int32\_t bufferSize | Buffer size. |

**Return value**

| Type | Description |
| :-- | :-- |
| ArkUI\_ErrorCode | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_BUFFER\_SIZE\_NOT\_ENOUGH](../native-type-h/document.md#arkui_errorcode) if the buffer space is insufficient.

 |

#### \[h2\]OH\_ArkUI\_TouchTestInfo\_SetTouchResultStrategy

ArkUI\_ErrorCode OH\_ArkUI\_TouchTestInfo\_SetTouchResultStrategy(ArkUI\_TouchTestInfo\* info, ArkUI\_TouchTestStrategy strategy);

**Description**

Sets the touch test policy, that is, the behavior of a component and its child components in a hit test.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_TouchTestInfo](../../structs/arkui-touchtestinfo/document.md)\* info | Pointer to the touch test information. |
| [ArkUI\_TouchTestStrategy](#arkui_touchteststrategy) strategy | Touch test policy, defining the behavior rules of a component and its child components in a hit test. |

**Return value**

| Type | Description |
| :-- | :-- |
| ArkUI\_ErrorCode | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_TouchTestInfo\_SetTouchResultId

ArkUI\_ErrorCode OH\_ArkUI\_TouchTestInfo\_SetTouchResultId(ArkUI\_TouchTestInfo\* info, const char\* id);

**Description**

Sets the ID of a child component involved in a hit test.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_TouchTestInfo](../../structs/arkui-touchtestinfo/document.md)\* info | Pointer to the touch test information. |
| const char\* id | ID of a child component, which specifies the target child component involved in a hit test. |

**Return value**

| Type | Description |
| :-- | :-- |
| ArkUI\_ErrorCode | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |
