# Binding Gesture Events

The ArkUI development framework provides tap, pan, swipe, long press, pinch, and rotation gestures through its NDK APIs. By binding different gestures to specified components and setting corresponding callbacks, you can achieve the desired gesture interaction capabilities.

The following is a simple example to illustrate how to implement gesture binding.

1.  Create a **Column** node to which gestures will be bound.
    
    // Create a Column node.
    auto column = nodeAPI->createNode(ARKUI\_NODE\_COLUMN);
    // Set the background color.
    ArkUI\_NumberValue value\[\] = {{.u32 = 0xff112233}};
    ArkUI\_AttributeItem item = {value, 1};
    nodeAPI->setAttribute(column, NODE\_BACKGROUND\_COLOR, &item);
    // Set the width.
    ArkUI\_NumberValue widthValue\[\] = {{400}};
    ArkUI\_AttributeItem width = {widthValue, 1};
    nodeAPI->setAttribute(column, NODE\_WIDTH, &width);
    //Set the height.
    ArkUI\_NumberValue heightValue\[\] = {{400}};
    ArkUI\_AttributeItem height = {heightValue, 1};
    nodeAPI->setAttribute(column, NODE\_HEIGHT, &height);
    
2.  Create a single-finger long-press gesture with a 1-second activation threshold.
    
    // Obtain the set of native gesture APIs.
    auto gestureApi = reinterpret\_cast<ArkUI\_NativeGestureAPI\_1 \*>(
        OH\_ArkUI\_QueryModuleInterfaceByName(ARKUI\_NATIVE\_GESTURE, "ArkUI\_NativeGestureAPI\_1"));
    // Create a long press gesture.
    // DURATION\_NUM\_1000 = 1000
    auto longPressGesture = gestureApi->createLongPressGesture(1, true, DURATION\_NUM\_1000);
    
3.  Bind the created gesture to the **Column** node created in step 1.
    
    auto onActionCallBack = \[\](ArkUI\_GestureEvent \*event, void \*extraParam) {
        // Callback content
        // ···
    };
    
    // Set the gesture to the component.
    gestureApi->setGestureEventTarget(
        longPressGesture, GESTURE\_EVENT\_ACTION\_ACCEPT | GESTURE\_EVENT\_ACTION\_UPDATE | GESTURE\_EVENT\_ACTION\_END, column,
        onActionCallBack);
    
    gestureApi->addGestureToNode(column, longPressGesture, PARALLEL, NORMAL\_GESTURE\_MASK);
    

#### Single Gestures

The following introduces how to create different types of gestures:

-   Tap gesture
    
    Triggers a callback when the component is tapped. You can specify the number of taps required and the number of fingers needed.
    
    // Obtain the set of native gesture APIs.
    auto gestureApi = reinterpret\_cast<ArkUI\_NativeGestureAPI\_1 \*>(
        OH\_ArkUI\_QueryModuleInterfaceByName(ARKUI\_NATIVE\_GESTURE, "ArkUI\_NativeGestureAPI\_1"));
    // Create a tap gesture.
    auto tapGesture = gestureApi->createTapGesture(1, 1);
    
-   Pan gesture
    
    Triggers a callback when the user performs a pan gesture on the component. You can specify the required number of fingers, pan direction, and pan distance (in px).
    
    // Obtain the set of native gesture APIs.
    auto gestureApi = reinterpret\_cast<ArkUI\_NativeGestureAPI\_1 \*>(
        OH\_ArkUI\_QueryModuleInterfaceByName(ARKUI\_NATIVE\_GESTURE, "ArkUI\_NativeGestureAPI\_1"));
    // Create a pan gesture.
    auto panGesture = gestureApi->createPanGesture(1, GESTURE\_DIRECTION\_ALL, 1);
    
-   Long press gesture
    
    Triggers a callback when the user long presses the component. You can specify the number of fingers, hold-down time in milliseconds, and repeatability.
    
    // Obtain the set of native gesture APIs.
    auto gestureApi = reinterpret\_cast<ArkUI\_NativeGestureAPI\_1 \*>(
        OH\_ArkUI\_QueryModuleInterfaceByName(ARKUI\_NATIVE\_GESTURE, "ArkUI\_NativeGestureAPI\_1"));
    // Create a long press gesture.
    // DURATION\_NUM\_1000 = 1000
    auto longPressGesture = gestureApi->createLongPressGesture(1, true, DURATION\_NUM\_1000);
    
-   Pinch gesture
    
    Triggers a callback when the user pinches the component. You can specify the number of fingers (at least 2) and the pinch distance (in px).
    
    // Obtain the set of native gesture APIs.
    auto gestureApi = reinterpret\_cast<ArkUI\_NativeGestureAPI\_1 \*>(
        OH\_ArkUI\_QueryModuleInterfaceByName(ARKUI\_NATIVE\_GESTURE, "ArkUI\_NativeGestureAPI\_1"));
    // Create a pinch gesture.
    // NUMBER\_2 = 2, NUMBER\_10 = 10
    auto pinchGesture = gestureApi->createPinchGesture(NUMBER\_2, NUMBER\_10);
    
-   Rotation gesture
    
    Triggers a callback when the user rotates the component. You can specify the number of fingers (at least 2) and angle.
    
    // Obtain the set of native gesture APIs.
    auto gestureApi = reinterpret\_cast<ArkUI\_NativeGestureAPI\_1 \*>(
        OH\_ArkUI\_QueryModuleInterfaceByName(ARKUI\_NATIVE\_GESTURE, "ArkUI\_NativeGestureAPI\_1"));
    // Create a rotation gesture.
    // NUMBER\_2 = 2, NUMBER\_10 = 10
    auto rotationGesture = gestureApi->createRotationGesture(NUMBER\_2, NUMBER\_10);
    
-   Swipe gesture
    
    Triggers a callback when a swipe gesture is detected on the component. You can specify the required number of fingers (at least 1), swipe direction, and minimum velocity (in px/s).
    
    // Obtain the set of native gesture APIs.
    auto gestureApi = reinterpret\_cast<ArkUI\_NativeGestureAPI\_1 \*>(
        OH\_ArkUI\_QueryModuleInterfaceByName(ARKUI\_NATIVE\_GESTURE, "ArkUI\_NativeGestureAPI\_1"));
    // Create a swipe gesture.
    // SPEED\_NUM\_50 = 50
    auto swipeGesture = gestureApi->createSwipeGesture(1, GESTURE\_DIRECTION\_ALL, SPEED\_NUM\_50);
    

#### Combined Gestures

You can combine multiple gestures of different types into a gesture group, which acts as an integrated recognizer to identify sequences of different user gestures.

The recognition mode of the gesture group (that is, the relationship between gestures in the group) is specified by setting [ArkUI\_GroupGestureMode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-gesture-h#arkui_groupgesturemode), including sequential recognition (**SEQUENTIAL\_GROUP**), parallel recognition (**PARALLEL\_GROUP**), and exclusive recognition (**EXCLUSIVE\_GROUP**).

## Sequential Recognition

For combined gestures with sequential recognition, the value of **ArkUI\_GroupGestureMode** is **SEQUENTIAL\_GROUP**. In this gesture recognition mode, gestures are recognized in the order they were registered until they are all recognized successfully. If any of the registered gestures fails to be recognized, subsequent gestures will also fail. Only the last gesture in a sequential group can respond to the [GESTURE\_EVENT\_ACTION\_END](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-gesture-h#arkui_gestureeventactiontype) event.

The following demonstrates how to create a combined gesture that recognizes a long press followed by a swipe in sequence:

// LongPressAndSwipeGesture.h
#include <arkui/native\_animate.h>
#include <arkui/native\_gesture.h>
#include <arkui/native\_interface.h>
#include <arkui/native\_node.h>
#include <arkui/native\_type.h>
#include <arkui/native\_node\_napi.h>
#include <hilog/log.h>
#include "Common.h"
#include "Function.h"
// ...
ArkUI\_NodeHandle LongPressAndSwipeGesture()
{
    auto column = nodeAPI->createNode(ARKUI\_NODE\_COLUMN);

    // Create a node.
    ArkUI\_NumberValue value\[\] = {{.u32 = 0xff112233}};
    ArkUI\_AttributeItem item = {value, ITEM\_SIZE\_ONE};
    nodeAPI->setAttribute(column, NODE\_BACKGROUND\_COLOR, &item);
    ArkUI\_NumberValue widthValue\[\] = {{WIDTH\_SIZE}};
    ArkUI\_AttributeItem width = {widthValue, ITEM\_SIZE\_ONE};
    nodeAPI->setAttribute(column, NODE\_WIDTH, &width);
    ArkUI\_NumberValue heightValue\[\] = {{HEIGHT\_SIZE}};
    ArkUI\_AttributeItem height = {heightValue, ITEM\_SIZE\_ONE};
    nodeAPI->setAttribute(column, NODE\_HEIGHT, &height);

    // Verify gesture API availability.
    auto gestureApi = reinterpret\_cast<ArkUI\_NativeGestureAPI\_1 \*>(
        OH\_ArkUI\_QueryModuleInterfaceByName(ARKUI\_NATIVE\_GESTURE, "ArkUI\_NativeGestureAPI\_1"));
    if (gestureApi->createGroupGesture) {
        OH\_LOG\_Print(LOG\_APP, LOG\_INFO, LOG\_PRINT\_DOMAIN, "\[Sample\_NdkAddInteractionEvent\]",
                     "NdkAddInteractionEvent\_GestureSampleLog, createGroupGesture api exist");
    } else {
        OH\_LOG\_Print(LOG\_APP, LOG\_INFO, LOG\_PRINT\_DOMAIN, "\[Sample\_NdkAddInteractionEvent\]",
                     "NdkAddInteractionEvent\_GestureSampleLog, createGroupGesture api not exist");
    }
    auto groupGesture = gestureApi->createGroupGesture(ArkUI\_GroupGestureMode::SEQUENTIAL\_GROUP);

    // Create a long press gesture.
    auto longPressGesture = gestureApi->createLongPressGesture(GINGERS\_NUM, true, DURATION\_NUM);
    if (gestureApi->getGestureType) {
        ArkUI\_GestureRecognizerType type = gestureApi->getGestureType(longPressGesture);
        OH\_LOG\_Print(LOG\_APP, LOG\_INFO, LOG\_PRINT\_DOMAIN, "\[Sample\_NdkAddInteractionEvent\]",
                     "NdkAddInteractionEvent\_GestureSampleLog longPressGesture,"
                     "ArkUI\_GestureRecognizerType%{public}d", type);
    }
    // Set a callback for the long press gesture.
    auto onActionCallBackPanLongPress = \[\](ArkUI\_GestureEvent \*event, void \*extraParam) {
        ArkUI\_GestureEventActionType actionType = OH\_ArkUI\_GestureEvent\_GetActionType(event);

        float velocity = OH\_ArkUI\_PanGesture\_GetVelocity(event);
        float velocityX = OH\_ArkUI\_PanGesture\_GetVelocityX(event);
        float velocityY = OH\_ArkUI\_PanGesture\_GetVelocityY(event);
        float offsetX = OH\_ArkUI\_PanGesture\_GetOffsetX(event);
        float offsetY = OH\_ArkUI\_PanGesture\_GetOffsetY(event);
        float scale = OH\_ArkUI\_PinchGesture\_GetScale(event);
        float centerX = OH\_ArkUI\_PinchGesture\_GetCenterX(event);
        float centerY = OH\_ArkUI\_PinchGesture\_GetCenterY(event);
        float angle = OH\_ArkUI\_SwipeGesture\_GetAngle(event);
        float velocityS = OH\_ArkUI\_SwipeGesture\_GetVelocity(event);
        float angleR = OH\_ArkUI\_RotationGesture\_GetAngle(event);
        float repeat = OH\_ArkUI\_LongPress\_GetRepeatCount(event);

        OH\_LOG\_Print(
            LOG\_APP, LOG\_INFO, LOG\_PRINT\_DOMAIN, "\[Sample\_NdkAddInteractionEvent\]",
            "NdkAddInteractionEvent\_GestureSampleLog,longPressGesturecallback actionType:%{public}d,"
            "velocity%{public}f,velocityX%{public}f;"
            "velocityY%{public}f,offsetX%{public}f,offsetY%{public}f,scale%{public}fcenterX"
            "%{public}fcenterY"
            "%{public}fangle%{public}fvelocityS%{public}fangleR%{public}frepeat%{public}f",
            actionType, velocity, velocityX, velocityY, offsetX, offsetY, scale, centerX, centerY, angle, velocityS,
            angleR, repeat);
    };
    gestureApi->setGestureEventTarget(longPressGesture,
                                      GESTURE\_EVENT\_ACTION\_ACCEPT | GESTURE\_EVENT\_ACTION\_UPDATE |
                                      GESTURE\_EVENT\_ACTION\_CANCEL, column, onActionCallBackPanLongPress);

    // Add the long press gesture to the gesture group.
    if (gestureApi->addChildGesture) {
        gestureApi->addChildGesture(groupGesture, longPressGesture);
        OH\_LOG\_Print(LOG\_APP, LOG\_INFO, LOG\_PRINT\_DOMAIN, "\[Sample\_NdkAddInteractionEvent\]",
                     "NdkAddInteractionEvent\_GestureSampleLog, addChildGesture longPressGesture");
    }
    // Create a swipe gesture.
    auto swipeGesture = gestureApi->createSwipeGesture(1, GESTURE\_DIRECTION\_ALL, 100);
    if (gestureApi->getGestureType) {
        ArkUI\_GestureRecognizerType type = gestureApi->getGestureType(swipeGesture);
        OH\_LOG\_Print(LOG\_APP, LOG\_INFO, LOG\_PRINT\_DOMAIN, "\[Sample\_NdkAddInteractionEvent\]",
                     "NdkAddInteractionEvent\_GestureSampleLog, ArkUI\_GestureRecognizerType %{public}d",
                     type);
    }
    // Set a callback for the swipe gesture.
    auto onActionCallBack = \[\](ArkUI\_GestureEvent \*event, void \*extraParam) {
        ArkUI\_GestureEventActionType actionType = OH\_ArkUI\_GestureEvent\_GetActionType(event);

        float velocity = OH\_ArkUI\_PanGesture\_GetVelocity(event);
        float velocityX = OH\_ArkUI\_PanGesture\_GetVelocityX(event);
        float velocityY = OH\_ArkUI\_PanGesture\_GetVelocityY(event);
        float offsetX = OH\_ArkUI\_PanGesture\_GetOffsetX(event);
        float offsetY = OH\_ArkUI\_PanGesture\_GetOffsetY(event);
        float scale = OH\_ArkUI\_PinchGesture\_GetScale(event);
        float centerX = OH\_ArkUI\_PinchGesture\_GetCenterX(event);
        float centerY = OH\_ArkUI\_PinchGesture\_GetCenterY(event);
        float angle = OH\_ArkUI\_SwipeGesture\_GetAngle(event);
        float velocityS = OH\_ArkUI\_SwipeGesture\_GetVelocity(event);
        float angleR = OH\_ArkUI\_RotationGesture\_GetAngle(event);
        float repeat = OH\_ArkUI\_LongPress\_GetRepeatCount(event);
        
        // Print logs.
        OH\_LOG\_Print(LOG\_APP, LOG\_INFO, LOG\_PRINT\_DOMAIN, "\[Sample\_NdkAddInteractionEvent\]",
                     "NdkAddInteractionEvent\_GestureSampleLog, swipeGesture "
                     "callback actionType: %{public}d, velocity %{public}f,velocityX "
                     "%{public}f; "
                     "velocityY %{public}f, offsetX %{public}f, offsetY %{public}f, scale %{public}fcenterX "
                     "%{public}f centerY"
                     " %{public}f angle %{public}f velocityS %{public}f angleR %{public}f repeat %{public}f",
                     actionType, velocity, velocityX, velocityY, offsetX, offsetY, scale, centerX, centerY, angle,
                     velocityS, angleR, repeat);

        ArkUI\_NumberValue value\[\] = {{.f32 = 0}, {.f32 = 0}, {.f32 = 0}, {.f32 = angleR}, {.f32 = 0}};
        ArkUI\_AttributeItem item = {value, ITEM\_SIZE\_FIVE};
        auto column = reinterpret\_cast<ArkUI\_NodeHandle>(extraParam);
        nodeAPI->setAttribute(column, NODE\_ROTATE, &item);
    };

    gestureApi->setGestureEventTarget(
        swipeGesture, GESTURE\_EVENT\_ACTION\_ACCEPT | GESTURE\_EVENT\_ACTION\_UPDATE | GESTURE\_EVENT\_ACTION\_END, column,
        onActionCallBack);

    // Add the swipe gesture to the gesture group.
    if (gestureApi->addChildGesture) {
        gestureApi->addChildGesture(groupGesture, swipeGesture);
        OH\_LOG\_Print(LOG\_APP, LOG\_INFO, LOG\_PRINT\_DOMAIN, "\[Sample\_NdkAddInteractionEvent\]",
                     "NdkAddInteractionEvent\_GestureSampleLog, addChildGesture swipeGesture");
    }
    // Set the gesture group to the component.
    gestureApi->addGestureToNode(column, groupGesture, PRIORITY, NORMAL\_GESTURE\_MASK);
    return column;
}

**Sample**

For details, see [Sample](https://gitcode.com/openharmony/applications_app_samples/blob/master/code/DocsSample/ArkUISample/NdkAddInteractionEvent).

## Parallel Recognition

For combined gestures with parallel recognition, the value of **ArkUI\_GroupGestureMode** is **PARALLEL\_GROUP**. In this gesture recognition mode, gestures registered in the combined gestures will be recognized at the same time until they are all recognized successfully. The gestures are recognized in parallel without affecting each other.

The following demonstrates how to create a combined gesture that recognizes long press and swipe gestures in parallel:

// LongPressAndFlickGesture.h
#include <arkui/native\_animate.h>
#include <arkui/native\_gesture.h>
#include <arkui/native\_interface.h>
#include <arkui/native\_node.h>
#include <arkui/native\_type.h>
#include <arkui/native\_node\_napi.h>
#include <hilog/log.h>
#include "Common.h"
#include "Function.h"
// ...

ArkUI\_NodeHandle LongPressAndFlickGesture()
{
    auto column = nodeAPI->createNode(ARKUI\_NODE\_COLUMN);

    // Create a node.
    ArkUI\_NumberValue value\[\] = {{.u32 = 0xff112233}};
    ArkUI\_AttributeItem item = {value, ITEM\_SIZE\_ONE};
    nodeAPI->setAttribute(column, NODE\_BACKGROUND\_COLOR, &item);
    ArkUI\_NumberValue widthValue\[\] = {{WIDTH\_SIZE}};
    ArkUI\_AttributeItem width = {widthValue, ITEM\_SIZE\_ONE};
    nodeAPI->setAttribute(column, NODE\_WIDTH, &width);
    ArkUI\_NumberValue heightValue\[\] = {{HEIGHT\_SIZE}};
    ArkUI\_AttributeItem height = {heightValue, ITEM\_SIZE\_ONE};
    nodeAPI->setAttribute(column, NODE\_HEIGHT, &height);

    // Verify gesture API availability.
    auto gestureApi = reinterpret\_cast<ArkUI\_NativeGestureAPI\_1 \*>(
        OH\_ArkUI\_QueryModuleInterfaceByName(ARKUI\_NATIVE\_GESTURE, "ArkUI\_NativeGestureAPI\_1"));
    if (gestureApi->createGroupGesture) {
        OH\_LOG\_Print(LOG\_APP, LOG\_INFO, LOG\_PRINT\_DOMAIN, "\[Sample\_NdkAddInteractionEvent\]",
                     "NdkAddInteractionEvent\_GestureSampleLog, createGroupGesture api exist");
    } else {
        OH\_LOG\_Print(LOG\_APP, LOG\_INFO, LOG\_PRINT\_DOMAIN, "\[Sample\_NdkAddInteractionEvent\]",
                     "NdkAddInteractionEvent\_GestureSampleLog, createGroupGesture api not exist");
    }

    // Create a gesture group.
    auto groupGesture = gestureApi->createGroupGesture(ArkUI\_GroupGestureMode::PARALLEL\_GROUP);

    // Create a long press gesture.
    auto longPressGesture = gestureApi->createLongPressGesture(GINGERS\_NUM, true, DURATION\_NUM\_500);
    if (gestureApi->getGestureType) {
        ArkUI\_GestureRecognizerType type = gestureApi->getGestureType(longPressGesture);
        OH\_LOG\_Print(LOG\_APP, LOG\_INFO, LOG\_PRINT\_DOMAIN, "\[Sample\_NdkAddInteractionEvent\]",
                     "NdkAddInteractionEvent\_GestureSampleLog,ArkUI\_GestureRecognizerType%{public}d", type);
    }
    // Set a callback for the long press gesture.
    auto onActionCallBackPanLongPress = \[\](ArkUI\_GestureEvent \*event, void \*extraParam) {
        ArkUI\_GestureEventActionType actionType = OH\_ArkUI\_GestureEvent\_GetActionType(event);

        float velocity = OH\_ArkUI\_PanGesture\_GetVelocity(event);
        float velocityX = OH\_ArkUI\_PanGesture\_GetVelocityX(event);
        float velocityY = OH\_ArkUI\_PanGesture\_GetVelocityY(event);
        float offsetX = OH\_ArkUI\_PanGesture\_GetOffsetX(event);
        float offsetY = OH\_ArkUI\_PanGesture\_GetOffsetY(event);
        float scale = OH\_ArkUI\_PinchGesture\_GetScale(event);
        float centerX = OH\_ArkUI\_PinchGesture\_GetCenterX(event);
        float centerY = OH\_ArkUI\_PinchGesture\_GetCenterY(event);
        float angle = OH\_ArkUI\_SwipeGesture\_GetAngle(event);
        float velocityS = OH\_ArkUI\_SwipeGesture\_GetVelocity(event);
        float angleR = OH\_ArkUI\_RotationGesture\_GetAngle(event);
        float repeat = OH\_ArkUI\_LongPress\_GetRepeatCount(event);

        OH\_LOG\_Print(
            LOG\_APP, LOG\_INFO, LOG\_PRINT\_DOMAIN, "\[Sample\_NdkAddInteractionEvent\]",
            "NdkAddInteractionEvent\_GestureSampleLog,longPressGesturecallback actionType:%{public}d,"
            "velocity%{public}f,velocityX%{public}f;"
            "velocityY%{public}f,offsetX%{public}f,offsetY%{public}f,scale%{public}f, centerX "
            "%{public}fcenterY"
            "%{public}fangle%{public}fvelocityS%{public}fangleR%{public}frepeat%{public}f",
            actionType, velocity, velocityX, velocityY, offsetX, offsetY, scale, centerX, centerY, angle, velocityS,
            angleR, repeat);
    };
    gestureApi->setGestureEventTarget(longPressGesture,
                                      GESTURE\_EVENT\_ACTION\_ACCEPT | GESTURE\_EVENT\_ACTION\_UPDATE |
                                            GESTURE\_EVENT\_ACTION\_CANCEL,
                                      column, onActionCallBackPanLongPress);

    // Add the long press gesture to the gesture group.
    if (gestureApi->addChildGesture) {
        gestureApi->addChildGesture(groupGesture, longPressGesture);
        OH\_LOG\_Print(LOG\_APP, LOG\_INFO, LOG\_PRINT\_DOMAIN, "\[Sample\_NdkAddInteractionEvent\]",
                     "NdkAddInteractionEvent\_GestureSampleLog, addChildGesture longPressGesture");
    }
    // Create a swipe gesture.
    auto swipeGesture = gestureApi->createSwipeGesture(GINGERS\_NUM, GESTURE\_DIRECTION\_ALL, DURATION\_NUM\_100);
    if (gestureApi->getGestureType) {
        ArkUI\_GestureRecognizerType type = gestureApi->getGestureType(swipeGesture);
        OH\_LOG\_Print(LOG\_APP, LOG\_INFO, LOG\_PRINT\_DOMAIN, "\[Sample\_NdkAddInteractionEvent\]",
                     "NdkAddInteractionEvent\_GestureSampleLog, ArkUI\_GestureRecognizerType %{public}d",
                     type);
    }
    // Set a callback for the swipe gesture.
    auto onActionCallBack = \[\](ArkUI\_GestureEvent \*event, void \*extraParam) {
        ArkUI\_GestureEventActionType actionType = OH\_ArkUI\_GestureEvent\_GetActionType(event);

        float velocity = OH\_ArkUI\_PanGesture\_GetVelocity(event);
        float velocityX = OH\_ArkUI\_PanGesture\_GetVelocityX(event);
        float velocityY = OH\_ArkUI\_PanGesture\_GetVelocityY(event);
        float offsetX = OH\_ArkUI\_PanGesture\_GetOffsetX(event);
        float offsetY = OH\_ArkUI\_PanGesture\_GetOffsetY(event);
        float scale = OH\_ArkUI\_PinchGesture\_GetScale(event);
        float centerX = OH\_ArkUI\_PinchGesture\_GetCenterX(event);
        float centerY = OH\_ArkUI\_PinchGesture\_GetCenterY(event);
        float angle = OH\_ArkUI\_SwipeGesture\_GetAngle(event);
        float velocityS = OH\_ArkUI\_SwipeGesture\_GetVelocity(event);
        float angleR = OH\_ArkUI\_RotationGesture\_GetAngle(event);
        float repeat = OH\_ArkUI\_LongPress\_GetRepeatCount(event);
        
        // Print logs.
        OH\_LOG\_Print(LOG\_APP, LOG\_INFO, LOG\_PRINT\_DOMAIN, "\[Sample\_NdkAddInteractionEvent\]",
                     "NdkAddInteractionEvent\_GestureSampleLog, swipeGesture "
                     "callback actionType: %{public}d, velocity%{public}f,velocityX "
                     "%{public}f; "
                     "velocityY %{public}f, offsetX %{public}f, offsetY %{public}f, scale %{public}f, centerX "
                     "%{public}f centerY"
                     " %{public}f angle %{public}f velocityS %{public}f angleR %{public}f repeat %{public}f",
                     actionType, velocity, velocityX, velocityY, offsetX, offsetY, scale, centerX, centerY, angle,
                     velocityS, angleR, repeat);

        ArkUI\_NumberValue value\[\] = {{.f32 = 0}, {.f32 = 0}, {.f32 = 0}, {.f32 = angleR}, {.f32 = 0}};
        ArkUI\_AttributeItem item = {value, ITEM\_SIZE\_FIVE};
        auto column = reinterpret\_cast<ArkUI\_NodeHandle>(extraParam);
        nodeAPI->setAttribute(column, NODE\_ROTATE, &item);
    };

    gestureApi->setGestureEventTarget(
        swipeGesture, GESTURE\_EVENT\_ACTION\_ACCEPT | GESTURE\_EVENT\_ACTION\_UPDATE | GESTURE\_EVENT\_ACTION\_END, column,
        onActionCallBack);

    // Add the swipe gesture to the gesture group.
    if (gestureApi->addChildGesture) {
        gestureApi->addChildGesture(groupGesture, swipeGesture);
        OH\_LOG\_Print(LOG\_APP, LOG\_INFO, LOG\_PRINT\_DOMAIN, "\[Sample\_NdkAddInteractionEvent\]",
                     "NdkAddInteractionEvent\_GestureSampleLog, addChildGesture swipeGesture");
    }
    // Set the gesture group to the component.
    gestureApi->addGestureToNode(column, groupGesture, PRIORITY, NORMAL\_GESTURE\_MASK);
    return column;
}

**Sample**

For details, see [Sample](https://gitcode.com/openharmony/applications_app_samples/blob/master/code/DocsSample/ArkUISample/NdkAddInteractionEvent).

## Exclusive Recognition

For combined gestures with exclusive recognition, the value of **ArkUI\_GroupGestureMode** is **EXCLUSIVE\_GROUP**. In this gesture recognition mode, all registered gestures are recognized at once. Once any of the gestures is recognized successfully, the gesture recognition ends, and recognition for all other gestures fails.

The following example illustrates the exclusive recognition of pan and pinch gestures:

// SwipeAndPinchExclusiveGesture.h
#include <arkui/native\_animate.h>
#include <arkui/native\_gesture.h>
#include <arkui/native\_interface.h>
#include <arkui/native\_node.h>
#include <arkui/native\_type.h>
#include <arkui/native\_node\_napi.h>
#include <hilog/log.h>
#include "Common.h"
#include "Function.h"
// ...

ArkUI\_NodeHandle SwipeAndPinchExclusiveGesture()
{
    OH\_ArkUI\_GetModuleInterface(ARKUI\_NATIVE\_NODE, ArkUI\_NativeNodeAPI\_1, nodeAPI);
    if (nodeAPI == nullptr) {
        return nullptr;
    }
    auto column = nodeAPI->createNode(ARKUI\_NODE\_COLUMN);

    // Create a node.
    ArkUI\_NumberValue value\[\] = {{.u32 = 0xff112233}};
    ArkUI\_AttributeItem item = {value, 1};
    nodeAPI->setAttribute(column, NODE\_BACKGROUND\_COLOR, &item);
    ArkUI\_NumberValue widthValue\[\] = {{WIDTH\_SIZE}};
    ArkUI\_AttributeItem width = {widthValue, ITEM\_SIZE\_ONE};
    nodeAPI->setAttribute(column, NODE\_WIDTH, &width);
    ArkUI\_NumberValue heightValue\[\] = {{HEIGHT\_SIZE}};
    ArkUI\_AttributeItem height = {heightValue, ITEM\_SIZE\_ONE};
    nodeAPI->setAttribute(column, NODE\_HEIGHT, &height);

    // Verify gesture API availability.
    auto gestureApi = reinterpret\_cast<ArkUI\_NativeGestureAPI\_1 \*>(
        OH\_ArkUI\_QueryModuleInterfaceByName(ARKUI\_NATIVE\_GESTURE, "ArkUI\_NativeGestureAPI\_1"));
    if (gestureApi->createGroupGesture) {
        OH\_LOG\_Print(LOG\_APP, LOG\_INFO, LOG\_PRINT\_DOMAIN, "\[Sample\_NdkAddInteractionEvent\]",
                     "NdkAddInteractionEvent\_GestureSampleLog, createGroupGesture api exist");
    } else {
        OH\_LOG\_Print(LOG\_APP, LOG\_INFO, LOG\_PRINT\_DOMAIN, "\[Sample\_NdkAddInteractionEvent\]",
                     "NdkAddInteractionEvent\_GestureSampleLog, createGroupGesture api not exist");
    }
    auto groupGesture = gestureApi->createGroupGesture(ArkUI\_GroupGestureMode::EXCLUSIVE\_GROUP);

    // Create a pan gesture.
    auto panGesture = gestureApi->createPanGesture(GINGERS\_NUM, GESTURE\_DIRECTION\_VERTICAL, DURATION\_NUM);
    if (gestureApi->getGestureType) {
        ArkUI\_GestureRecognizerType type = gestureApi->getGestureType(panGesture);
        OH\_LOG\_Print(LOG\_APP, LOG\_INFO, LOG\_PRINT\_DOMAIN, "\[Sample\_NdkAddInteractionEvent\]",
                     "NdkAddInteractionEvent\_GestureSampleLog panGesture, ArkUI\_GestureRecognizerType %{public}d",
                     type);
    }
    // Set a callback for the swipe gesture.
    auto onActionCallBackPan = \[\](ArkUI\_GestureEvent \*event, void \*extraParam) {
        ArkUI\_GestureEventActionType actionType = OH\_ArkUI\_GestureEvent\_GetActionType(event);

        float velocity = OH\_ArkUI\_PanGesture\_GetVelocity(event);
        float velocityX = OH\_ArkUI\_PanGesture\_GetVelocityX(event);
        float velocityY = OH\_ArkUI\_PanGesture\_GetVelocityY(event);
        float offsetX = OH\_ArkUI\_PanGesture\_GetOffsetX(event);
        float offsetY = OH\_ArkUI\_PanGesture\_GetOffsetY(event);
        float scale = OH\_ArkUI\_PinchGesture\_GetScale(event);
        float centerX = OH\_ArkUI\_PinchGesture\_GetCenterX(event);
        float centerY = OH\_ArkUI\_PinchGesture\_GetCenterY(event);
        float angle = OH\_ArkUI\_SwipeGesture\_GetAngle(event);
        float velocityS = OH\_ArkUI\_SwipeGesture\_GetVelocity(event);
        float angleR = OH\_ArkUI\_RotationGesture\_GetAngle(event);
        float repeat = OH\_ArkUI\_LongPress\_GetRepeatCount(event);

        // Print logs.
        OH\_LOG\_Print(
            LOG\_APP, LOG\_INFO, LOG\_PRINT\_DOMAIN, "\[Sample\_NdkAddInteractionEvent\]",
            "NdkAddInteractionEvent\_GestureSampleLog, panGesture callback actionType: %{public}d, "
            "velocity %{public}f,velocityX %{public}f; "
            "velocityY %{public}f, offsetX %{public}f, offsetY %{public}f, scale %{public}fcenterX "
            "%{public}f centerY"
            " %{public}f angle %{public}f velocityS %{public}f angleR %{public}f repeat %{public}f",
            actionType, velocity, velocityX, velocityY, offsetX, offsetY, scale, centerX, centerY, angle, velocityS,
            angleR, repeat);
    };
    gestureApi->setGestureEventTarget(panGesture,
                                      GESTURE\_EVENT\_ACTION\_ACCEPT | GESTURE\_EVENT\_ACTION\_UPDATE |
                                          GESTURE\_EVENT\_ACTION\_END | GESTURE\_EVENT\_ACTION\_CANCEL,
                                      column, onActionCallBackPan);
    // Add the swipe press gesture to the gesture group.
    if (gestureApi->addChildGesture) {
        gestureApi->addChildGesture(groupGesture, panGesture);
        OH\_LOG\_Print(LOG\_APP, LOG\_INFO, LOG\_PRINT\_DOMAIN, "\[Sample\_NdkAddInteractionEvent\]",
                     "NdkAddInteractionEvent\_GestureSampleLog, addChildGesture panGesture");
    }
    // Create a pinch gesture.
    auto pinchGesture = gestureApi->createPinchGesture(0, 0);
    if (gestureApi->getGestureType) {
        ArkUI\_GestureRecognizerType type = gestureApi->getGestureType(pinchGesture);
        OH\_LOG\_Print(LOG\_APP, LOG\_INFO, LOG\_PRINT\_DOMAIN, "\[Sample\_NdkAddInteractionEvent\]",
                     "NdkAddInteractionEvent\_GestureSampleLog pinchGesture, "
                     "ArkUI\_GestureRecognizerType %{public}d", type);
    }
    // Set a callback for the pinch gesture.
    auto onActionCallBack = \[\](ArkUI\_GestureEvent \*event, void \*extraParam) {
        ArkUI\_GestureEventActionType actionType = OH\_ArkUI\_GestureEvent\_GetActionType(event);

        float velocity = OH\_ArkUI\_PanGesture\_GetVelocity(event);
        float velocityX = OH\_ArkUI\_PanGesture\_GetVelocityX(event);
        float velocityY = OH\_ArkUI\_PanGesture\_GetVelocityY(event);
        float offsetX = OH\_ArkUI\_PanGesture\_GetOffsetX(event);
        float offsetY = OH\_ArkUI\_PanGesture\_GetOffsetY(event);
        float scale = OH\_ArkUI\_PinchGesture\_GetScale(event);
        float centerX = OH\_ArkUI\_PinchGesture\_GetCenterX(event);
        float centerY = OH\_ArkUI\_PinchGesture\_GetCenterY(event);
        float angle = OH\_ArkUI\_SwipeGesture\_GetAngle(event);
        float velocityS = OH\_ArkUI\_SwipeGesture\_GetVelocity(event);
        float angleR = OH\_ArkUI\_RotationGesture\_GetAngle(event);
        float repeat = OH\_ArkUI\_LongPress\_GetRepeatCount(event);
        
        OH\_LOG\_Print(
            LOG\_APP, LOG\_INFO, LOG\_PRINT\_DOMAIN, "\[Sample\_NdkAddInteractionEvent\]",
            "NdkAddInteractionEvent\_GestureSampleLog, pinchGesture callback actionType: %{public}d, "
            "velocity %{public}f,velocityX %{public}f; "
            "velocityY %{public}f, offsetX %{public}f, offsetY %{public}f, scale %{public}fcenterX "
            "%{public}f centerY"
            " %{public}f angle %{public}f velocityS %{public}f angleR %{public}f repeat %{public}f",
            actionType, velocity, velocityX, velocityY, offsetX, offsetY, scale, centerX, centerY, angle, velocityS,
            angleR, repeat);
        ArkUI\_NumberValue value\[\] = {{.f32 = scale}, {.f32 = scale}};
        ArkUI\_AttributeItem item = {value, ITEM\_SIZE\_TWO};
        auto column = reinterpret\_cast<ArkUI\_NodeHandle>(extraParam);
        nodeAPI->setAttribute(column, NODE\_SCALE, &item);
    };
    gestureApi->setGestureEventTarget(pinchGesture,
                                      GESTURE\_EVENT\_ACTION\_ACCEPT | GESTURE\_EVENT\_ACTION\_UPDATE |
                                          GESTURE\_EVENT\_ACTION\_END | GESTURE\_EVENT\_ACTION\_CANCEL,
                                      column, onActionCallBack);
    // Add the pinch press gesture to the gesture group.
    if (gestureApi->addChildGesture) {
        gestureApi->addChildGesture(groupGesture, pinchGesture);
        OH\_LOG\_Print(LOG\_APP, LOG\_INFO, LOG\_PRINT\_DOMAIN, "\[Sample\_NdkAddInteractionEvent\]",
                     "NdkAddInteractionEvent\_GestureSampleLog, addChildGesture pinchGesture");
    }
    // Set the gesture group to the component.
    gestureApi->addGestureToNode(column, groupGesture, PRIORITY, NORMAL\_GESTURE\_MASK);
    return column;
}

**Sample**

For details, see [Sample](https://gitcode.com/openharmony/applications_app_samples/blob/master/code/DocsSample/ArkUISample/NdkAddInteractionEvent).

## Custom Gesture Judgment

Custom gesture judgment allows you to dynamically decide whether a gesture recognizer should be considered successful by the system when a user's action matches a gesture recognizer and the gesture recognizer is about to be triggered successfully. This is achieved by binding a callback to the target component using the **setGestureInterrupterToNode** API. The callback returns **CONTINUE** or **REJECT** to determine whether to allow the gesture recognizer to succeed or to give the opportunity to other gesture recognizers.

To implement custom gesture judgment, adjust the example of binding gesture events as follows:

1.  Create a custom gesture judgment callback.
    
    auto onInterruptCallback = \[\](ArkUI\_GestureInterruptInfo \*info) -> ArkUI\_GestureInterruptResult {
        // Check whether the gesture is a system gesture.
        auto sysTag = OH\_ArkUI\_GestureInterruptInfo\_GetSystemFlag(info);
        // Obtain the gesture recognizer for gesture interception.
        auto recognizer = OH\_ArkUI\_GestureInterruptInfo\_GetRecognizer(info);
        // Obtain the system gesture type.
        auto systemRecognizerType = OH\_ArkUI\_GestureInterruptInfo\_GetSystemRecognizerType(info);
        // Obtain the gesture event.
        auto gestureEvent = OH\_ArkUI\_GestureInterruptInfo\_GetGestureEvent(info);
        auto inputEvent = OH\_ArkUI\_GestureEvent\_GetRawInputEvent(gestureEvent);
        OH\_LOG\_Print(LOG\_APP, LOG\_INFO, LOG\_PRINT\_DOMAIN, "\[Sample\_NdkAddInteractionEvent\]",
            "NdkAddInteractionEvent\_eventInfo longPressGesture");
        if (sysTag) {
            // If the gesture is a system gesture, do not intercept it.
            return GESTURE\_INTERRUPT\_RESULT\_CONTINUE;
        } else {
            // If the gesture is not a system gesture, intercept and reject it.
            return GESTURE\_INTERRUPT\_RESULT\_REJECT;
        }
    };
    
2.  Bind the custom gesture interrupter to the node.
    
    gestureApi->setGestureInterrupterToNode(column, onInterruptCallback);
    

After the aforementioned modifications, the originally effective long press gesture is intercepted. Consequently, long pressing the **Column** node will no longer trigger the long press gesture callback.

#### Obtaining Event Information

After binding gesture events to nodes as previously described, you can use [OH\_ArkUI\_GestureEvent\_GetRawInputEvent()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-gesture-h#oh_arkui_gestureevent_getrawinputevent) to obtain the basic event object from the gesture event when the gesture callback is executed. Then, you can call APIs such as [OH\_ArkUI\_PointerEvent\_GetDisplayX()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-ui-input-event-h#oh_arkui_pointerevent_getdisplayx), [OH\_ArkUI\_PointerEvent\_GetDisplayXByIndex()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-ui-input-event-h#oh_arkui_pointerevent_getdisplayxbyindex), [OH\_ArkUI\_UIInputEvent\_GetAction()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-ui-input-event-h#oh_arkui_uiinputevent_getaction), and [OH\_ArkUI\_UIInputEvent\_GetEventTime()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-ui-input-event-h#oh_arkui_uiinputevent_geteventtime) to obtain more information from the basic event. Applications can implement differentiated interaction logic during gesture event execution based on the obtained information.

// Set a callback to handle gesture events when they are triggered.
auto onActionCallback = \[\](ArkUI\_GestureEvent \*event, void \*extraParams) {
    // Obtain the basic event object from the gesture event.
    auto \*inputEvent = OH\_ArkUI\_GestureEvent\_GetRawInputEvent(event);
    // Obtain event information from the basic event.
    auto x = OH\_ArkUI\_PointerEvent\_GetX(inputEvent);
    auto y = OH\_ArkUI\_PointerEvent\_GetY(inputEvent);
    auto displayX = OH\_ArkUI\_PointerEvent\_GetDisplayX(inputEvent);
    auto displayY = OH\_ArkUI\_PointerEvent\_GetDisplayY(inputEvent);
    auto windowX = OH\_ArkUI\_PointerEvent\_GetWindowX(inputEvent);
    auto windowY = OH\_ArkUI\_PointerEvent\_GetWindowY(inputEvent);
    auto pointerCount = OH\_ArkUI\_PointerEvent\_GetPointerCount(inputEvent);
    auto xByIndex = OH\_ArkUI\_PointerEvent\_GetXByIndex(inputEvent, 0);
    auto yByIndex = OH\_ArkUI\_PointerEvent\_GetYByIndex(inputEvent, 0);
    auto displayXByIndex = OH\_ArkUI\_PointerEvent\_GetDisplayXByIndex(inputEvent, 0);
    auto displayYByIndex = OH\_ArkUI\_PointerEvent\_GetDisplayYByIndex(inputEvent, 0);
    auto windowXByIndex = OH\_ArkUI\_PointerEvent\_GetWindowXByIndex(inputEvent, 0);
    auto windowYByIndex = OH\_ArkUI\_PointerEvent\_GetWindowYByIndex(inputEvent, 0);
    auto pointerId = OH\_ArkUI\_PointerEvent\_GetPointerId(inputEvent, 0);
    auto pressure = OH\_ArkUI\_PointerEvent\_GetPressure(inputEvent, 0);
    auto action = OH\_ArkUI\_UIInputEvent\_GetAction(inputEvent);
    auto eventTime = OH\_ArkUI\_UIInputEvent\_GetEventTime(inputEvent);
    auto sourceType = OH\_ArkUI\_UIInputEvent\_GetSourceType(inputEvent);
    auto type = OH\_ArkUI\_UIInputEvent\_GetType(inputEvent);
    std::string eventInfo =
        "x: " + std::to\_string(x) + ", y: " + std::to\_string(y) +
        ", displayX: " + std::to\_string(displayX) + ", displayY: " + std::to\_string(displayY) +
        ", windowX: " + std::to\_string(windowX) + ", windowY: " + std::to\_string(windowY) + "\\n" +
        ", pointerCount: " + std::to\_string(pointerCount) + ", xByIndex: " + std::to\_string(xByIndex) +
        ", yByIndex: " + std::to\_string(yByIndex) +
        ", displayXByIndex: " + std::to\_string(displayXByIndex) +
        ", displayYByIndex: " + std::to\_string(displayYByIndex) +
        ", windowXByIndex: " + std::to\_string(windowXByIndex) +
        ", windowYByIndex: " + std::to\_string(windowYByIndex) + "\\n" +
        ", pointerId: " + std::to\_string(pointerId) + ", pressure: " + std::to\_string(pressure) +
        ", action: " + std::to\_string(action) + ", eventTime: " + std::to\_string(eventTime) +
        ", sourceType: " + std::to\_string(sourceType) + ", type: " + std::to\_string(type);
    OH\_LOG\_Print(LOG\_APP, LOG\_INFO, LOG\_PRINT\_DOMAIN, "\[Sample\_NdkAddInteractionEvent\]",
                 "NdkAddInteractionEvent\_eventInfoOfCommonEvent eventInfo = %{public}s", eventInfo.c\_str());
};
// Create a single-finger tap gesture.
auto TapGesture = gestureApi->createTapGesture(COUNT\_NUM\_1, GINGERS\_NUM\_1);
// Bind the event callback to TapGesture. After the gesture is triggered, the callback function processes the gesture event.
gestureApi->setGestureEventTarget(TapGesture,
                                  GESTURE\_EVENT\_ACTION\_ACCEPT | GESTURE\_EVENT\_ACTION\_UPDATE |
                                  GESTURE\_EVENT\_ACTION\_END | GESTURE\_EVENT\_ACTION\_CANCEL,
                                  column, onActionCallback);
// Add a gesture to the column component so that the column component can trigger the single-finger tap gesture.
gestureApi->addGestureToNode(column, TapGesture, ArkUI\_GesturePriority::PARALLEL,
                             ArkUI\_GestureMask::NORMAL\_GESTURE\_MASK);
