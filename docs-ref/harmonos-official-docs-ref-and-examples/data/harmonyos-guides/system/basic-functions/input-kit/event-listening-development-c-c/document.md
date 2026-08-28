# Event Listening Development (C/C++)

#### When to Use

Since API version 12, the multimodal module provides applications with the ability to listen for key and input events (including mouse, touch, and axis events). Currently, event listening is available only for screen recording applications. For example, when a user starts screen recording, your application can listen for key, mouse, touch, and axis events of the device.

#### Available APIs

The following table lists the APIs for event listening. For details, see [Input](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-input).

| API | Description |
| :-- | :-- |
| Input\_Result OH\_Input\_AddKeyEventMonitor(Input\_KeyEventCallback callback) | Creates a key event listener. |
| Input\_Result OH\_Input\_AddMouseEventMonitor(Input\_MouseEventCallback callback) | Creates a mouse event listener. |
| Input\_Result OH\_Input\_AddTouchEventMonitor(Input\_TouchEventCallback callback) | Creates a touch event listener. |
| Input\_Result OH\_Input\_AddAxisEventMonitorForAll(Input\_AxisEventCallback callback) | Creates a listener for all axis events. |
| Input\_Result OH\_Input\_AddAxisEventMonitor(InputEvent\_AxisEventType axisEventType, Input\_AxisEventCallback callback) | Creates a listener for the specified type of axis events. |
| Input\_Result OH\_Input\_RemoveKeyEventMonitor(Input\_KeyEventCallback callback) | Removes a key event listener. |
| Input\_Result OH\_Input\_RemoveMouseEventMonitor(Input\_MouseEventCallback callback) | Removes a mouse event listener. |
| Input\_Result OH\_Input\_RemoveTouchEventMonitor(Input\_TouchEventCallback callback) | Removes a touch event listener. |
| Input\_Result OH\_Input\_RemoveAxisEventMonitorForAll(Input\_AxisEventCallback callback) | Removes a listener for all axis events. |
| Input\_Result OH\_Input\_RemoveAxisEventMonitor(InputEvent\_AxisEventType axisEventType, Input\_AxisEventCallback callback) | Removes a listener for the specified type of axis events. |

#### How to Develop

## Linking Dynamic Libraries

Before calling listener-related APIs, you need to link the related dynamic libraries. To link dynamic libraries, add the following configuration to the **CMakeList.txt** file:

target\_link\_libraries(entry PUBLIC libohinput.so)

## Applying for Required Permissions

Declare the required permission in the **module.json5** file. For details, see [Declaring Permissions](../../../security/application-access-control/application-permission-management/requesting-application-permissions/declaring-permissions/document.md).

"requestPermissions": \[
    {
        "name": "ohos.permission.INPUT\_MONITORING"
    }
\]

## Creating an Event Listener

-   **Key event**

struct KeyEvent {
    int32\_t action;
    int32\_t keyCode;
    int64\_t actionTime { -1 };
};

// Define the key event callback function.
void OnKeyEventCallback(const Input\_KeyEvent\* keyEvent)
{
    KeyEvent event;
    // The lifecycle of Input\_KeyEvent is limited to the callback function. After the callback function is executed, Input\_KeyEvent is automatically destroyed.
    event.action = OH\_Input\_GetKeyEventAction(keyEvent);
    event.keyCode = OH\_Input\_GetKeyEventKeyCode(keyEvent);
    event.actionTime = OH\_Input\_GetKeyEventActionTime(keyEvent);
    // ...
}

static napi\_value AddKeyEventMonitor(napi\_env env, napi\_callback\_info info)
{
    Input\_Result ret = OH\_Input\_AddKeyEventMonitor(OnKeyEventCallback);
    // ...
}

static napi\_value RemoveKeyEventMonitor(napi\_env env, napi\_callback\_info info)
{
    Input\_Result ret = OH\_Input\_RemoveKeyEventMonitor(OnKeyEventCallback);
    // ...
}

-   **Mouse event**

struct MouseEvent {
    int32\_t action;
    int32\_t displayX;
    int32\_t displayY;
    int32\_t button { -1 };
    int32\_t axisType { -1 };
    float axisValue { 0.0f };
    int64\_t actionTime { -1 };
};

// Define the mouse event callback function.
void OnMouseEventCallback(const Input\_MouseEvent\* mouseEvent)
{
    MouseEvent event;
    // The lifecycle of Input\_MouseEvent is limited to the callback function. After the callback function is executed, Input\_MouseEvent is automatically destroyed.
    event.action = OH\_Input\_GetMouseEventAction(mouseEvent);
    event.displayX = OH\_Input\_GetMouseEventDisplayX(mouseEvent);
    event.displayY = OH\_Input\_GetMouseEventDisplayY(mouseEvent);
    event.button = OH\_Input\_GetMouseEventButton(mouseEvent);
    event.axisType = OH\_Input\_GetMouseEventAxisType(mouseEvent);
    event.axisValue = OH\_Input\_GetMouseEventAxisValue(mouseEvent);
    event.actionTime = OH\_Input\_GetMouseEventActionTime(mouseEvent);
    // ...
}

static napi\_value AddMouseEventMonitor(napi\_env env, napi\_callback\_info info)
{
    Input\_Result ret = OH\_Input\_AddMouseEventMonitor(OnMouseEventCallback);
    // ...
}

static napi\_value RemoveMouseEventMonitor(napi\_env env, napi\_callback\_info info)
{
    Input\_Result ret = OH\_Input\_RemoveMouseEventMonitor(OnMouseEventCallback);
    // ...
}

-   **Touch event**

struct TouchEvent {
    int32\_t action;
    int32\_t id;
    int32\_t displayX;
    int32\_t displayY;
    int64\_t actionTime { -1 };
};

void OnTouchEventCallback(const Input\_TouchEvent\* touchEvent)
{
    TouchEvent event;
    // The lifecycle of Input\_TouchEvent is limited to the callback function. After the callback function is executed, Input\_TouchEvent is automatically destroyed.
    event.action = OH\_Input\_GetTouchEventAction(touchEvent);
    event.id = OH\_Input\_GetTouchEventFingerId(touchEvent);
    event.displayX = OH\_Input\_GetTouchEventDisplayX(touchEvent);
    event.displayY = OH\_Input\_GetTouchEventDisplayY(touchEvent);
    event.actionTime = OH\_Input\_GetTouchEventActionTime(touchEvent);
    // ...
}

static napi\_value AddTouchEventMonitor(napi\_env env, napi\_callback\_info info)
{
    Input\_Result ret = OH\_Input\_AddTouchEventMonitor(OnTouchEventCallback);
    // ...
}

static napi\_value RemoveTouchEventMonitor(napi\_env env, napi\_callback\_info info)
{
    Input\_Result ret = OH\_Input\_RemoveTouchEventMonitor(OnTouchEventCallback);
    // ...
}

-   **Axis event**

struct AxisEvent {
    int32\_t axisAction;
    float displayX;
    float displayY;
    std::map<int32\_t, double> axisValues;
    int64\_t actionTime { -1 };
    int32\_t sourceType;
    int32\_t axisEventType { -1 };
};

void OnAllAxisEventCallback(const Input\_AxisEvent\* axisEvent)
{
    AxisEvent event;
    // The lifecycle of Input\_AxisEvent is limited to the callback function. After the callback function is executed, Input\_AxisEvent is automatically destroyed.
    InputEvent\_AxisAction action = static\_cast<InputEvent\_AxisAction>(0);
    Input\_Result ret = OH\_Input\_GetAxisEventAction(axisEvent, &action);
    event.axisAction = action;
    ret = OH\_Input\_GetAxisEventDisplayX(axisEvent, &event.displayX);
    ret = OH\_Input\_GetAxisEventDisplayY(axisEvent, &event.displayY);
    ret = OH\_Input\_GetAxisEventActionTime(axisEvent, &event.actionTime);
    InputEvent\_SourceType sourceType = static\_cast<InputEvent\_SourceType>(0);
    ret = OH\_Input\_GetAxisEventSourceType(axisEvent, &sourceType);
    event.sourceType = sourceType;
    InputEvent\_AxisEventType axisEventType = static\_cast<InputEvent\_AxisEventType>(-1);
    ret = OH\_Input\_GetAxisEventType(axisEvent, &axisEventType);
    event.axisEventType = axisEventType;
    if (event.axisEventType == AXIS\_EVENT\_TYPE\_PINCH) {
        double value = 0;
        ret = OH\_Input\_GetAxisEventAxisValue(axisEvent, AXIS\_TYPE\_PINCH, &value);
        event.axisValues.insert(std::make\_pair(AXIS\_TYPE\_PINCH, value));
        ret = OH\_Input\_GetAxisEventAxisValue(axisEvent, AXIS\_TYPE\_ROTATE, &value);
        event.axisValues.insert(std::make\_pair(AXIS\_TYPE\_ROTATE, value));
    } else if (event.axisEventType == AXIS\_EVENT\_TYPE\_SCROLL) {
        double value = 0;
        ret = OH\_Input\_GetAxisEventAxisValue(axisEvent, AXIS\_TYPE\_SCROLL\_VERTICAL, &value);
        event.axisValues.insert(std::make\_pair(AXIS\_TYPE\_SCROLL\_VERTICAL, value));
        ret = OH\_Input\_GetAxisEventAxisValue(axisEvent, AXIS\_TYPE\_SCROLL\_HORIZONTAL, &value);
        event.axisValues.insert(std::make\_pair(AXIS\_TYPE\_SCROLL\_HORIZONTAL, value));
    }
    // ...
}

// Define the callback function for pinch-type axis events.
void OnPinchAxisEventCallback(const Input\_AxisEvent\* axisEvent)
{
    AxisEvent event;
    // The lifecycle of Input\_AxisEvent is limited to the callback function. After the callback function is executed, Input\_AxisEvent is automatically destroyed.
    InputEvent\_AxisAction action = static\_cast<InputEvent\_AxisAction>(0);
    Input\_Result ret = OH\_Input\_GetAxisEventAction(axisEvent, &action);
    event.axisAction = action;
    ret = OH\_Input\_GetAxisEventDisplayX(axisEvent, &event.displayX);
    ret = OH\_Input\_GetAxisEventDisplayY(axisEvent, &event.displayY);
    ret = OH\_Input\_GetAxisEventActionTime(axisEvent, &event.actionTime);
    InputEvent\_SourceType sourceType = static\_cast<InputEvent\_SourceType>(0);
    ret = OH\_Input\_GetAxisEventSourceType(axisEvent, &sourceType);
    event.sourceType = sourceType;
    InputEvent\_AxisEventType axisEventType = static\_cast<InputEvent\_AxisEventType>(-1);
    ret = OH\_Input\_GetAxisEventType(axisEvent, &axisEventType);
    event.axisEventType = axisEventType;
    double value = 0;
    ret = OH\_Input\_GetAxisEventAxisValue(axisEvent, AXIS\_TYPE\_PINCH, &value);
    event.axisValues.insert(std::make\_pair(AXIS\_TYPE\_PINCH, value));
    ret = OH\_Input\_GetAxisEventAxisValue(axisEvent, AXIS\_TYPE\_ROTATE, &value);
    event.axisValues.insert(std::make\_pair(AXIS\_TYPE\_ROTATE, value));
    // ...
}

void OnScrollAxisEventCallback(const Input\_AxisEvent\* axisEvent)
{
    AxisEvent event;
    // The lifecycle of Input\_AxisEvent is limited to the callback function. After the callback function is executed, Input\_AxisEvent is automatically destroyed.
    InputEvent\_AxisAction action = static\_cast<InputEvent\_AxisAction>(0);
    Input\_Result ret = OH\_Input\_GetAxisEventAction(axisEvent, &action);
    event.axisAction = action;
    ret = OH\_Input\_GetAxisEventDisplayX(axisEvent, &event.displayX);
    ret = OH\_Input\_GetAxisEventDisplayY(axisEvent, &event.displayY);
    ret = OH\_Input\_GetAxisEventActionTime(axisEvent, &event.actionTime);
    InputEvent\_SourceType sourceType = static\_cast<InputEvent\_SourceType>(0);
    ret = OH\_Input\_GetAxisEventSourceType(axisEvent, &sourceType);
    event.sourceType = sourceType;
    InputEvent\_AxisEventType axisEventType = static\_cast<InputEvent\_AxisEventType>(-1);
    ret = OH\_Input\_GetAxisEventType(axisEvent, &axisEventType);
    event.axisEventType = axisEventType;
    double value = 0;
    ret = OH\_Input\_GetAxisEventAxisValue(axisEvent, AXIS\_TYPE\_SCROLL\_VERTICAL, &value);
    event.axisValues.insert(std::make\_pair(AXIS\_TYPE\_SCROLL\_VERTICAL, value));
    ret = OH\_Input\_GetAxisEventAxisValue(axisEvent, AXIS\_TYPE\_SCROLL\_HORIZONTAL, &value);
    event.axisValues.insert(std::make\_pair(AXIS\_TYPE\_SCROLL\_HORIZONTAL, value));
    // ...
}

static napi\_value AddAxisEventMonitorForAll(napi\_env env, napi\_callback\_info info)
{
    Input\_Result ret = OH\_Input\_AddAxisEventMonitorForAll(OnAllAxisEventCallback);
    // ...
}

static napi\_value RemoveAxisEventMonitorForAll(napi\_env env, napi\_callback\_info info)
{
    Input\_Result ret = OH\_Input\_RemoveAxisEventMonitorForAll(OnAllAxisEventCallback);
    // ...
}

static napi\_value AddPinchAxisEventMonitor(napi\_env env, napi\_callback\_info info)
{
    Input\_Result ret = OH\_Input\_AddAxisEventMonitor(AXIS\_EVENT\_TYPE\_PINCH, OnPinchAxisEventCallback);
    // ...
}

static napi\_value RemovePinchAxisEventMonitor(napi\_env env, napi\_callback\_info info)
{
    Input\_Result ret = OH\_Input\_RemoveAxisEventMonitor(AXIS\_EVENT\_TYPE\_PINCH, OnPinchAxisEventCallback);
    // ...
}

static napi\_value AddScrollAxisEventMonitor(napi\_env env, napi\_callback\_info info)
{
    Input\_Result ret = OH\_Input\_AddAxisEventMonitor(AXIS\_EVENT\_TYPE\_SCROLL, OnScrollAxisEventCallback);
    // ...
}

static napi\_value RemoveScrollAxisEventMonitor(napi\_env env, napi\_callback\_info info)
{
    Input\_Result ret =  OH\_Input\_RemoveAxisEventMonitor(AXIS\_EVENT\_TYPE\_SCROLL, OnScrollAxisEventCallback);
    // ...
}
