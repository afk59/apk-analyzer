# Event Interception Development (C/C++)

#### Introduction

Since API version 12, the multimodal module provides applications with the ability to create and delete keys and intercept input events (including mouse, touch, and axis events). For example, you can intercept key, mouse, touch, and axis events.

#### Available APIs

The following table lists the APIs for event interception. For details, see [Input](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-input).

| API | Description |
| :-- | :-- |
| Input\_Result OH\_Input\_AddKeyEventInterceptor(Input\_KeyEventCallback callback, Input\_InterceptorOptions \*option) | Creates a key event interceptor. |
| Input\_Result OH\_Input\_AddInputEventInterceptor(Input\_InterceptorEventCallback \*callback, Input\_InterceptorOptions \*option) | Creates an input event interceptor. Input events include mouse, touch, and axis events. |
| Input\_Result OH\_Input\_RemoveKeyEventInterceptor() | Removes a key event interceptor. |
| Input\_Result OH\_Input\_RemoveInputEventInterceptor() | Removes an input event interceptor. |

#### How to Develop

## Linking a Dynamic Library

Before calling interception-related APIs, you need to link the related dynamic library. You can do this by editing the **CMakeList.txt** file as follows:

target\_link\_libraries(entry PUBLIC libohinput.so)

## Applying for Required Permissions

Declare the required permission in the **module.json5** file. For details, see [Declaring Permissions in the Configuration File](../../../security/application-access-control/application-permission-management/requesting-application-permissions/declaring-permissions/document.md).

"requestPermissions": \[
    {
        "name": "ohos.permission.INTERCEPT\_INPUT\_EVENT"
    }
\]

## Creating an Event Interceptor

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
    // ···
}

static napi\_value AddKeyEventInterceptor(napi\_env env, napi\_callback\_info info)
{
    Input\_Result ret = OH\_Input\_AddKeyEventInterceptor(OnKeyEventCallback, nullptr);
    // ···
}

static napi\_value RemoveKeyEventInterceptor(napi\_env env, napi\_callback\_info info)
{
    Input\_Result ret = OH\_Input\_RemoveKeyEventInterceptor();
    // ···
}

-   **Input Events (Mouse, Touch, and Axis Events)**

struct MouseEvent {
    int32\_t action;
    int32\_t displayX;
    int32\_t displayY;
    int32\_t button { -1 };
    int32\_t axisType { -1 };
    float axisValue { 0.0f };
    int64\_t actionTime { -1 };
};

struct TouchEvent {
    int32\_t action;
    int32\_t id;
    int32\_t displayX;
    int32\_t displayY;
    int64\_t actionTime { -1 };
};

struct AxisEvent {
    int32\_t axisAction;
    float displayX;
    float displayY;
    std::map<int32\_t, double> axisValues;
    int64\_t actionTime { -1 };
    int32\_t sourceType;
    int32\_t axisEventType { -1 };
};

// Define the mouse event callback function.
void OnMouseEventCallback(const Input\_MouseEvent\* mouseEvent)
{
    MouseEvent event;
    // The lifecycle of Input\_MouseEvent is limited to the callback function. Input\_MouseEvent will be destroyed if it is called outside of the callback function.
    event.action = OH\_Input\_GetMouseEventAction(mouseEvent);
    event.displayX = OH\_Input\_GetMouseEventDisplayX(mouseEvent);
    event.displayY = OH\_Input\_GetMouseEventDisplayY(mouseEvent);
    event.button = OH\_Input\_GetMouseEventButton(mouseEvent);
    event.axisType = OH\_Input\_GetMouseEventAxisType(mouseEvent);
    event.axisValue = OH\_Input\_GetMouseEventAxisValue(mouseEvent);
    event.actionTime = OH\_Input\_GetMouseEventActionTime(mouseEvent);
    // ···
}

// Define the touch event callback function.
void OnTouchEventCallback(const Input\_TouchEvent\* touchEvent)
{
    TouchEvent event;
    // The lifecycle of Input\_TouchEvent is limited to the callback function. Input\_TouchEvent will be destroyed if it is called outside of the callback function.
    event.action = OH\_Input\_GetTouchEventAction(touchEvent);
    event.id = OH\_Input\_GetTouchEventFingerId(touchEvent);
    event.displayX = OH\_Input\_GetTouchEventDisplayX(touchEvent);
    event.displayY = OH\_Input\_GetTouchEventDisplayY(touchEvent);
    event.actionTime = OH\_Input\_GetTouchEventActionTime(touchEvent);
    // ···
}

// Define the axis event callback function.
void OnAxisEventCallback(const Input\_AxisEvent\* axisEvent)
{
    AxisEvent event;
    
    // The lifecycle of Input\_AxisEvent is limited to the callback function. Input\_AxisEvent will be destroyed if it is called outside of the callback function.
    InputEvent\_AxisAction action;
    Input\_Result ret = OH\_Input\_GetAxisEventAction(axisEvent, &action);
    event.axisAction = action;
    ret = OH\_Input\_GetAxisEventDisplayX(axisEvent, &event.displayX);
    ret = OH\_Input\_GetAxisEventDisplayY(axisEvent, &event.displayY);
    ret = OH\_Input\_GetAxisEventActionTime(axisEvent, &event.actionTime);
    InputEvent\_SourceType sourceType;
    ret = OH\_Input\_GetAxisEventSourceType(axisEvent, &sourceType);
    event.sourceType = sourceType;
    InputEvent\_AxisEventType axisEventType;
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
    // ···
}

// Structure of the input event callback function
Input\_InterceptorEventCallback g\_eventCallback;

static napi\_value AddEventInterceptor(napi\_env env, napi\_callback\_info info)
{
    // Set the mouse event callback function.
    g\_eventCallback.mouseCallback = OnMouseEventCallback;
    // Set the touch event callback function.
    g\_eventCallback.touchCallback = OnTouchEventCallback;
    // Set the axis event callback function.
    g\_eventCallback.axisCallback = OnAxisEventCallback;
    Input\_Result ret = OH\_Input\_AddInputEventInterceptor(&g\_eventCallback, nullptr);
    // ···
}

static napi\_value RemoveEventInterceptor(napi\_env env, napi\_callback\_info info)
{
    Input\_Result ret = OH\_Input\_RemoveInputEventInterceptor();
    // ···
}
