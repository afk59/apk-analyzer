# Using WindowManager to Manage Multimodal Input Events (C/C++)

#### When to Use

[WindowManager](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-windowmanager) provides the capability to manage application windows and can be used to handle multimodal input events.

Currently, WindowManager supports filtering multimodal input events and injecting multimodal touch events into target windows. The specific development steps are detailed below.

#### Filtering Multimodal Input Events

You can use the capability provided by the WindowManager module to intercept key events so that they are not distributed to internal components of your application.

## Linking the Dynamic Library in the CMake Script

target\_link\_libraries(entry PUBLIC libnative\_window\_manager.so libohinput.so)

## Adding Header Files

#include "multimodalinput/oh\_input\_manager.h"
#include "multimodalinput/oh\_key\_code.h"
#include "window\_manager/oh\_window\_comm.h"
#include "window\_manager/oh\_window\_event\_filter.h"

## Available APIs

| API | Description |
| :-- | :-- |
| OH\_NativeWindowManager\_RegisterKeyEventFilter(int32\_t windowId, OH\_NativeWindowManager\_KeyEventFilter keyEventFilter) | Registers a key event filter for a window. |
| OH\_NativeWindowManager\_UnregisterKeyEventFilter(int32\_t windowId) | Unregisters the key event filter of a window. |

-   After an application window is created, bind a key event filter using the window ID.
-   The key event filter is triggered only when the application window receives a key event.
-   If the callback function returns **true**, the event is intercepted; if it returns **false**, the event is not intercepted.
-   Only one key event filter can be registered for the same window ID. The last registered key event filter overwrites the previously registered one. To filter a multi-key event, you are advised to process the multi-key combination in a filter.

## Example

The following sample code describes how to register and unregister a key event filter. The following uses the Esc key and number keys as an example.

#include "napi/native\_api.h"
#include "window\_manager/oh\_window\_comm.h"
#include "window\_manager/oh\_window\_event\_filter.h"
#include "multimodalinput/oh\_input\_manager.h"
#include "multimodalinput/oh\_key\_code.h"

// Set a filter.
static bool filterFunc(Input\_KeyEvent \*event) {
  auto keyCode = OH\_Input\_GetKeyEventKeyCode(event);
  auto action = OH\_Input\_GetKeyEventAction(event);
  // Case1: Implement the event filter for the Esc key.
  // return keyCode == Input\_KeyCode::KEYCODE\_ESCAPE;

  // Case 2: Implement the event filter for the number keys only when they are pressed.
  // return keyCode >= Input\_KeyCode::KEYCODE\_0 && keyCode <= Input\_KeyCode::KEYCODE\_9
  //  && action == Input\_KeyEventAction::KEY\_ACTION\_DOWN;
  
  // Implement the event filter for the combination of the Esc key and a pressed-down number key. (Case1 || Case2).
  return (keyCode >= Input\_KeyCode::KEYCODE\_0 && keyCode <= Input\_KeyCode::KEYCODE\_9
     && action == Input\_KeyEventAction::KEY\_ACTION\_DOWN) || (keyCode == Input\_KeyCode::KEYCODE\_ESCAPE);
}

static napi\_value registerFilter(napi\_env env, napi\_callback\_info info) {
  size\_t argc = 1;
  napi\_value args\[1\] = {nullptr};
  napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);
  
  int32\_t windowId;
  napi\_get\_value\_int32(env, args\[0\], &windowId);
  
  // Register the filter for the window specified by the window ID.
  auto res = OH\_NativeWindowManager\_RegisterKeyEventFilter(windowId, filterFunc);
  
  napi\_value errCode;
  napi\_create\_int32(env, res, &errCode);
  return errCode;
}

static napi\_value clearFilter(napi\_env env, napi\_callback\_info info) {
  size\_t argc = 1;
  napi\_value args\[1\] = {nullptr};
  napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);

  int32\_t windowId;
  napi\_get\_value\_int32(env, args\[0\], &windowId);

  auto res = OH\_NativeWindowManager\_UnregisterKeyEventFilter(windowId);
  napi\_value errCode;
  napi\_create\_int32(env, res, &errCode);
  return errCode;

}

EXTERN\_C\_START
static napi\_value Init(napi\_env env, napi\_value exports) {
  napi\_property\_descriptor desc\[\] = {
    {"registerFilter", nullptr, registerFilter, nullptr, nullptr, nullptr, napi\_default, nullptr},
    {"clearFilter", nullptr, clearFilter, nullptr, nullptr, nullptr, napi\_default, nullptr}};
  napi\_define\_properties(env, exports, sizeof(desc) / sizeof(desc\[0\]), desc);
  return exports;
}
EXTERN\_C\_END

#### Injecting Multimodal Touch Events

You can use the capability provided by the WindowManager module to inject touch events into a specified window. This operation is supported only for windows within the same process. It does not trigger changes in window focus, z-order, or dragging. Instead, the events are directly sent to ArkUI.

## Linking the Dynamic Library in the CMake Script

target\_link\_libraries(entry PUBLIC libnative\_window\_manager.so libohinput.so)

## Adding Header Files

#include "multimodalinput/oh\_input\_manager.h"
#include "window\_manager/oh\_window.h"
#include "napi/native\_api.h"

## Available APIs

| API | Description |
| :-- | :-- |
| OH\_WindowManager\_InjectTouchEvent(int32\_t windowId, Input\_TouchEvent\* touchEvent, int32\_t windowX, int32\_t windowY) | Injects a touch event into the specified window. |

-   Construct event parameters and inject the event to the window with the specified window ID.
    
-   Only windows within the same process are supported. Injection does not trigger changes in window focus, z-order, or dragging. Events are directly sent to ArkUI.
    
-   The API must be called after the specified window has completed its UI loading.
    
-   Check the window and multimodal touch event to ensure the event parameters are correct before sending the event to ArkUI. The specific parameter descriptions are as follows:
    
    | Name | Description |
    | :-- | :-- |
    | windowId | ID of the target window. Only windows within the same process are supported. Otherwise, error code 1300002 is returned. The window must have completed UI loading. Otherwise, error code 1300003 is returned. |
    | touchEvent | Pointer to the multimodal touch event. For details, see [Input\_TouchEvent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-input-input-touchevent). The event is defined in **oh\_input\_manager.h**. Call [OH\_Input\_CreateTouchEvent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-oh-input-manager-h#oh_input_createtouchevent) to create a touchEvent object, and call [OH\_Input\_DestroyTouchEvent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-oh-input-manager-h#oh_input_destroytouchevent) to destroy the object after use. For specific parameter details, see the table below. |
    | windowX | X coordinate of the event relative to the target window. The parameter must be a non-negative integer; otherwise, error code 1300003 is returned. |
    | windowY | Y coordinate of the event relative to the target window. The parameter must be a non-negative integer; otherwise, error code 1300003 is returned. |
    
    The following table describes the parameters of the **touchEvent** event.
    
    | Name | API | Description |
    | :-- | :-- | :-- |
    | action | [OH\_Input\_SetTouchEventAction](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-oh-input-manager-h#oh_input_settoucheventaction) | 
    Event action. The default value is **0**.
    
    Only the following actions are supported:
    
    \- **0**: cancel, indicating a cancel event.
    
    \- **1**: down, indicating a press-down event.
    
    \- **2**: move, indicating a move event.
    
    \- **3**: up, indicating a lift event.
    
    \- For other actions, error code 1300003 is returned.
    
     |
    | id | [OH\_Input\_SetTouchEventFingerId](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-oh-input-manager-h#oh_input_settoucheventfingerid) | 
    
    Finger ID. The default value is **0**.
    
    The parameter must be a non-negative integer; otherwise, error code 1300003 is returned.
    
     |
    | displayX | [OH\_Input\_SetTouchEventDisplayX](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-oh-input-manager-h#oh_input_settoucheventdisplayx) | 
    
    X coordinate of the event relative to the screen. The default value is **0**.
    
    The parameter must be a non-negative integer; otherwise, error code 1300003 is returned. It is recommended that the value of this parameter be the same as that of **windowX**, although inconsistency will not return an error code. Only the input parameter's range is verified. You are advised to use [getWindowProperties()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-window-window#getwindowproperties9) to obtain the **windowRect** property and calculate the corresponding **windowX** by subtracting the horizontal coordinate of the window's top-left corner in **windowRect** from **displayX**.
    
     |
    | displayY | [OH\_Input\_SetTouchEventDisplayY](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-oh-input-manager-h#oh_input_settoucheventdisplayy) | 
    
    Y coordinate of the event relative to the screen. The default value is **0**.
    
    The parameter must be a non-negative integer; otherwise, error code 1300003 is returned. It is recommended that the value of this parameter be the same as that of **windowY**, although inconsistency will not return an error code. Only the input parameter's range is verified. You are advised to use [getWindowProperties()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-window-window#getwindowproperties9) to obtain the **windowRect** property and calculate the corresponding **windowY** by subtracting the vertical coordinate of the window's top-left corner in **windowRect** from **displayY**.
    
     |
    | actionTime | [OH\_Input\_SetTouchEventActionTime](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-oh-input-manager-h#oh_input_settoucheventactiontime) | Timestamp. The default value is **\-1**. The parameter must be a non-negative integer; otherwise, error code 1300003 is returned. |
    | windowId | [OH\_Input\_SetTouchEventWindowId](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-oh-input-manager-h#oh_input_settoucheventwindowid) | Window ID for event injection. The default value is **\-1**. If the parameter is not the default value and does not match **windowId** in [OH\_WindowManager\_InjectTouchEvent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-oh-window-h#oh_windowmanager_injecttouchevent), the input parameter is considered invalid. |
    | displayId | [OH\_Input\_SetTouchEventDisplayId](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-oh-input-manager-h#oh_input_settoucheventdisplayid) | Display ID for event injection. The default value is **\-1**. There are no restrictions, but you are advised to ensure that the display ID matches the window ID in [OH\_WindowManager\_InjectTouchEvent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-oh-window-h#oh_windowmanager_injecttouchevent). You are advised to call [getWindowProperties()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-window-window#getwindowproperties9) to obtain the **displayId** property. |
    

## Example

The following sample code describes how to inject a multimodal touch event into the target window, using a single event injection as an example.

#include "napi/native\_api.h"
#include "window\_manager/oh\_window.h"
#include "multimodalinput/oh\_input\_manager.h"

static napi\_value injectEvent(napi\_env env, napi\_callback\_info info) {
  size\_t argc = 10;
  napi\_value args\[10\] = {nullptr};
  napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);

  int32\_t windowId;
  napi\_get\_value\_int32(env, args\[0\], &windowId);

  int32\_t displayId;
  napi\_get\_value\_int32(env, args\[1\], &displayId);

  int32\_t windowX;
  napi\_get\_value\_int32(env, args\[2\], &windowX);

  int32\_t windowY;
  napi\_get\_value\_int32(env, args\[3\], &windowY);

  int32\_t action;
  napi\_get\_value\_int32(env, args\[4\], &action);

  int32\_t fingerId;
  napi\_get\_value\_int32(env, args\[5\], &fingerId);

  int32\_t displayX;
  napi\_get\_value\_int32(env, args\[6\], &displayX);

  int32\_t displayY;
  napi\_get\_value\_int32(env, args\[7\], &displayY);

  int32\_t actionTime;
  napi\_get\_value\_int32(env, args\[8\], &actionTime);

  int32\_t TE\_WindowId;
  napi\_get\_value\_int32(env, args\[9\], &TE\_WindowId);
  
  // Construct a multimodal touch event.
  Input\_TouchEvent\* touchEvent = OH\_Input\_CreateTouchEvent();
  OH\_Input\_SetTouchEventAction(touchEvent, action);
  OH\_Input\_SetTouchEventFingerId(touchEvent, fingerId);
  OH\_Input\_SetTouchEventDisplayX(touchEvent, displayX);
  OH\_Input\_SetTouchEventDisplayY(touchEvent, displayY);
  OH\_Input\_SetTouchEventActionTime(touchEvent, actionTime);
  OH\_Input\_SetTouchEventWindowId(touchEvent, TE\_WindowId);
  OH\_Input\_SetTouchEventDisplayId(touchEvent, displayId);

  // Inject the multimodal touch event to the window with the specified windowId.
  auto res = OH\_WindowManager\_InjectTouchEvent(windowId, touchEvent, windowX, windowY);

  // Destroy the touchEvent object after using it.
  OH\_Input\_DestroyTouchEvent(&touchEvent);
  
  napi\_value errCode;
  napi\_create\_int32(env, res, &errCode);
  return errCode;
}

EXTERN\_C\_START
static napi\_value Init(napi\_env env, napi\_value exports) {
  napi\_property\_descriptor desc\[\] = {
    {"injectEvent", nullptr, injectEvent, nullptr, nullptr, nullptr, napi\_default, nullptr}};
  napi\_define\_properties(env, exports, sizeof(desc) / sizeof(desc\[0\]), desc);
  return exports;
}
EXTERN\_C\_END
