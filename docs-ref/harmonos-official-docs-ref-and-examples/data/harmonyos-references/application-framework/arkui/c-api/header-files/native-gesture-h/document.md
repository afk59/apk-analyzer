# native\_gesture.h

#### Overview

Declares the APIs of **NativeGesture**.

**File to include**: <arkui/native\_gesture.h>

**Library**: libace\_ndk.z.so

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Since**: 12

**Related module**: [ArkUI\_NativeModule](../../modules/arkui-nativemodule/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [ArkUI\_NativeGestureAPI\_1](../../structs/arkui-nativegestureapi-1/document.md) | ArkUI\_NativeGestureAPI\_1 | Defines a struct for the gesture APIs. |
| [ArkUI\_NativeGestureAPI\_2](../../structs/arkui-nativegestureapi-2/document.md) | \- | Defines the gesture APIs. |
| [ArkUI\_GestureRecognizer](../../structs/arkui-gesturerecognizer/document.md) | ArkUI\_GestureRecognizer | Defines a gesture recognizer. |
| [ArkUI\_GestureInterruptInfo](../../structs/arkui-gestureinterruptinfo/document.md) | ArkUI\_GestureInterruptInfo | Defines the gesture interruption information. |
| [ArkUI\_GestureEvent](../../structs/arkui-gestureevent/document.md) | ArkUI\_GestureEvent | Defines the gesture event. |
| [ArkUI\_GestureEventTargetInfo](../../structs/arkui-gestureeventtargetinfo/document.md) | ArkUI\_GestureEventTargetInfo | Defines a **GestureEventTargetInfo** object that provides information about a gesture event target. |
| [ArkUI\_ParallelInnerGestureEvent](../../structs/arkui-parallelinnergestureevent/document.md) | ArkUI\_ParallelInnerGestureEvent | Defines a parallel built-in gesture event. |
| [ArkUI\_TouchRecognizer](../../structs/arkui-touchrecognizer/document.md) | ArkUI\_TouchRecognizer | Defines a touch recognizer. |
| [ArkUI\_TouchRecognizer\*](../../structs/arkui-touchrecognizer--00020177/document.md) | ArkUI\_TouchRecognizerHandle | Defines a touch recognizer handle. |
| [ArkUI\_TouchRecognizerHandle\*](../../structs/arkui-touchrecognizerhandle/document.md) | ArkUI\_TouchRecognizerHandleArray | Defines an array of touch recognizer handles. |
| [ArkUI\_GestureRecognizer\*](../../structs/arkui-gesturerecognizer--00020177/document.md) | ArkUI\_GestureRecognizerHandle | Defines the gesture recognizer handle. |
| [ArkUI\_GestureRecognizerHandle\*](../../structs/arkui-gesturerecognizerhandle/document.md) | ArkUI\_GestureRecognizerHandleArray | Defines the gesture recognizer handle array. |

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [ArkUI\_GestureEventActionType](#arkui_gestureeventactiontype) | ArkUI\_GestureEventActionType | Enumerates gesture event types. |
| [ArkUI\_GesturePriority](#arkui_gesturepriority) | ArkUI\_GesturePriority | Enumerates gesture event modes. |
| [ArkUI\_GroupGestureMode](#arkui_groupgesturemode) | ArkUI\_GroupGestureMode | Enumerates gesture group modes. |
| [ArkUI\_GestureDirection](#arkui_gesturedirection) | ArkUI\_GestureDirection | Enumerates gesture directions. |
| [ArkUI\_GestureMask](#arkui_gesturemask) | ArkUI\_GestureMask | Enumerates gesture masking modes. |
| [ArkUI\_GestureRecognizerType](#arkui_gesturerecognizertype) | ArkUI\_GestureRecognizerType | Enumerates gesture recognizer types. |
| [ArkUI\_GestureInterruptResult](#arkui_gestureinterruptresult) | ArkUI\_GestureInterruptResult | Enumerates gesture interruption results. |
| [ArkUI\_GestureRecognizerState](#arkui_gesturerecognizerstate) | ArkUI\_GestureRecognizerState | Enumerates the gesture recognizer states. |

#### \[h2\]Functions

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [typedef void (\*ArkUI\_GestureRecognizerDisposeNotifyCallback)(ArkUI\_GestureRecognizer\* recognizer, void\* userData)](#arkui_gesturerecognizerdisposenotifycallback) | ArkUI\_GestureRecognizerDisposeNotifyCallback | Defines a callback function for notifying gesture recognizer destruction. |
| [bool OH\_ArkUI\_GestureInterruptInfo\_GetSystemFlag(const ArkUI\_GestureInterruptInfo\* event)](#oh_arkui_gestureinterruptinfo_getsystemflag) | \- | Checks whether a gesture is a system built-in gesture. |
| [ArkUI\_GestureRecognizer\* OH\_ArkUI\_GestureInterruptInfo\_GetRecognizer(const ArkUI\_GestureInterruptInfo\* event)](#oh_arkui_gestureinterruptinfo_getrecognizer) | \- | Obtains the pointer to the interrupted gesture recognizer. |
| [ArkUI\_GestureEvent\* OH\_ArkUI\_GestureInterruptInfo\_GetGestureEvent(const ArkUI\_GestureInterruptInfo\* event)](#oh_arkui_gestureinterruptinfo_getgestureevent) | \- | Obtains the pointer to the interrupted gesture event. |
| [int32\_t OH\_ArkUI\_GestureInterruptInfo\_GetSystemRecognizerType(const ArkUI\_GestureInterruptInfo\* event)](#oh_arkui_gestureinterruptinfo_getsystemrecognizertype) | \- | Obtains the type of the system built-in gesture to trigger. |
| [int32\_t OH\_ArkUI\_GestureInterruptInfo\_GetTouchRecognizers(const ArkUI\_GestureInterruptInfo\* info,ArkUI\_TouchRecognizerHandleArray\* recognizers, int32\_t\* size)](#oh_arkui_gestureinterruptinfo_gettouchrecognizers) | \- | Obtains touch recognizers from gesture interruption information. |
| [ArkUI\_NodeHandle OH\_ArkUI\_TouchRecognizer\_GetNodeHandle(const ArkUI\_TouchRecognizerHandle recognizer)](#oh_arkui_touchrecognizer_getnodehandle) | \- | Obtains the component handle corresponding to a touch recognizer. |
| [int32\_t OH\_ArkUI\_TouchRecognizer\_CancelTouch(ArkUI\_TouchRecognizerHandle recognizer, ArkUI\_GestureInterruptInfo\* info)](#oh_arkui_touchrecognizer_canceltouch) | \- | Sends a cancel touch event to a touch recognizer in a gesture interruption callback. |
| [ArkUI\_GestureEventActionType OH\_ArkUI\_GestureEvent\_GetActionType(const ArkUI\_GestureEvent\* event)](#oh_arkui_gestureevent_getactiontype) | \- | Obtains the gesture event type. |
| [const ArkUI\_UIInputEvent\* OH\_ArkUI\_GestureEvent\_GetRawInputEvent(const ArkUI\_GestureEvent\* event)](#oh_arkui_gestureevent_getrawinputevent) | \- | Obtains gesture input. |
| [int32\_t OH\_ArkUI\_LongPress\_GetRepeatCount(const ArkUI\_GestureEvent\* event)](#oh_arkui_longpress_getrepeatcount) | \- | Checks whether the event is a repeated trigger event. |
| [float OH\_ArkUI\_PanGesture\_GetVelocity(const ArkUI\_GestureEvent\* event)](#oh_arkui_pangesture_getvelocity) | \- | Obtains the velocity of a pan gesture along the main axis. |
| [float OH\_ArkUI\_PanGesture\_GetVelocityX(const ArkUI\_GestureEvent\* event)](#oh_arkui_pangesture_getvelocityx) | \- | Obtains the velocity of a pan gesture along the x-axis. |
| [float OH\_ArkUI\_PanGesture\_GetVelocityY(const ArkUI\_GestureEvent\* event)](#oh_arkui_pangesture_getvelocityy) | \- | Obtains the velocity of a pan gesture along the y-axis. |
| [float OH\_ArkUI\_PanGesture\_GetOffsetX(const ArkUI\_GestureEvent\* event)](#oh_arkui_pangesture_getoffsetx) | \- | Obtains the relative offset of a pan gesture along the x-axis. |
| [float OH\_ArkUI\_PanGesture\_GetOffsetY(const ArkUI\_GestureEvent\* event)](#oh_arkui_pangesture_getoffsety) | \- | Obtains the relative offset of a pan gesture along the y-axis. |
| [float OH\_ArkUI\_SwipeGesture\_GetAngle(const ArkUI\_GestureEvent\* event)](#oh_arkui_swipegesture_getangle) | \- | 
Obtains the angle information of the swipe gesture. After a swipe gesture is recognized, a line connecting the two fingers is identified as the initial line. As the fingers swipe, the line between the fingers rotates.

Based on the coordinates of the initial line's and current line's end points, the arc tangent function is used to calculate the respective included angle of the points relative to the horizontal direction

by using the following formula: Rotation angle = arctan2(cy2-cy1,cx2-cx1) - arctan2(y2-y1,x2-x1).

The initial line is used as the coordinate system. The clockwise rotation is 0 to 180 degrees, and the counter-clockwise rotation is -180 to 0 degrees.

 |
| [float OH\_ArkUI\_SwipeGesture\_GetVelocity(const ArkUI\_GestureEvent\* event)](#oh_arkui_swipegesture_getvelocity) | \- | Obtains the average velocity of all fingers used in the swipe gesture. |
| [float OH\_ArkUI\_RotationGesture\_GetAngle(const ArkUI\_GestureEvent\* event)](#oh_arkui_rotationgesture_getangle) | \- | Obtains the angle information of a rotation gesture. |
| [float OH\_ArkUI\_PinchGesture\_GetScale(const ArkUI\_GestureEvent\* event)](#oh_arkui_pinchgesture_getscale) | \- | Obtains the scale ratio of a pinch gesture. |
| [float OH\_ArkUI\_PinchGesture\_GetCenterX(const ArkUI\_GestureEvent\* event)](#oh_arkui_pinchgesture_getcenterx) | \- | Obtains the x-coordinate of the center of the pinch gesture, in vp, relative to the upper left corner of the current component. |
| [float OH\_ArkUI\_PinchGesture\_GetCenterY(const ArkUI\_GestureEvent\* event)](#oh_arkui_pinchgesture_getcentery) | \- | Obtains the y-coordinate of the center of the pinch gesture, in vp, relative to the upper left corner of the current component. |
| [ArkUI\_NodeHandle OH\_ArkUI\_GestureEvent\_GetNode(const ArkUI\_GestureEvent\* event)](#oh_arkui_gestureevent_getnode) | \- | Obtains the ArkUI component to which the gesture is bound. |
| [int32\_t OH\_ArkUI\_GetResponseRecognizersFromInterruptInfo(const ArkUI\_GestureInterruptInfo\* event,ArkUI\_GestureRecognizerHandleArray\* responseChain, int32\_t\* count)](#oh_arkui_getresponserecognizersfrominterruptinfo) | \- | Obtains information about a gesture response chain. |
| [int32\_t OH\_ArkUI\_SetGestureRecognizerEnabled(ArkUI\_GestureRecognizer\* recognizer, bool enabled)](#oh_arkui_setgesturerecognizerenabled) | \- | Sets the enabled state of a gesture recognizer. |
| [int32\_t OH\_ArkUI\_SetGestureRecognizerLimitFingerCount(ArkUI\_GestureRecognizer\* recognizer, bool limitFingerCount)](#oh_arkui_setgesturerecognizerlimitfingercount) | \- | Sets whether to enable strict finger count checking. If this feature is enabled and the actual number of touch fingers does not match the set number, the gesture recognition fails. |
| [bool OH\_ArkUI\_GetGestureRecognizerEnabled(ArkUI\_GestureRecognizer\* recognizer)](#oh_arkui_getgesturerecognizerenabled) | \- | Obtains the enabled state of a gesture recognizer. |
| [int32\_t OH\_ArkUI\_GetGestureRecognizerState(ArkUI\_GestureRecognizer\* recognizer, ArkUI\_GestureRecognizerState\* state)](#oh_arkui_getgesturerecognizerstate) | \- | Obtains the state of a gesture recognizer. |
| [int32\_t OH\_ArkUI\_GetGestureEventTargetInfo(ArkUI\_GestureRecognizer\* recognizer, ArkUI\_GestureEventTargetInfo\*\* info)](#oh_arkui_getgestureeventtargetinfo) | \- | Obtains the information about a gesture event target. |
| [int32\_t OH\_ArkUI\_GestureEventTargetInfo\_IsScrollBegin(ArkUI\_GestureEventTargetInfo\* info, bool\* ret)](#oh_arkui_gestureeventtargetinfo_isscrollbegin) | \- | Obtains whether this scrollable container component is scrolled to the top. |
| [int32\_t OH\_ArkUI\_GestureEventTargetInfo\_IsScrollEnd(ArkUI\_GestureEventTargetInfo\* info, bool\* ret)](#oh_arkui_gestureeventtargetinfo_isscrollend) | \- | Obtains whether this scrollable container component is scrolled to the bottom. |
| [int32\_t OH\_ArkUI\_GetPanGestureDirectionMask(ArkUI\_GestureRecognizer\* recognizer,ArkUI\_GestureDirectionMask\* directionMask)](#oh_arkui_getpangesturedirectionmask) | \- | Obtains the direction of a pan gesture. |
| [bool OH\_ArkUI\_IsBuiltInGesture(ArkUI\_GestureRecognizer\* recognizer)](#oh_arkui_isbuiltingesture) | \- | Obtains whether a gesture is a system built-in gesture. |
| [int32\_t OH\_ArkUI\_GetGestureTag(ArkUI\_GestureRecognizer\* recognizer, char\* buffer, int32\_t bufferSize, int32\_t\* result)](#oh_arkui_getgesturetag) | \- | Obtains the tag of a gesture recognizer. |
| [int32\_t OH\_ArkUI\_GetGestureBindNodeId(ArkUI\_GestureRecognizer\* recognizer, char\* nodeId, int32\_t size,int32\_t\* result)](#oh_arkui_getgesturebindnodeid) | \- | Obtains the ID of the component linked to a gesture recognizer. |
| [bool OH\_ArkUI\_IsGestureRecognizerValid(ArkUI\_GestureRecognizer\* recognizer)](#oh_arkui_isgesturerecognizervalid) | \- | Obtains whether a gesture recognizer is valid. |
| [void\* OH\_ArkUI\_ParallelInnerGestureEvent\_GetUserData(ArkUI\_ParallelInnerGestureEvent\* event)](#oh_arkui_parallelinnergestureevent_getuserdata) | \- | Obtains custom data in the parallel built-in gesture event. |
| [ArkUI\_GestureRecognizer\* OH\_ArkUI\_ParallelInnerGestureEvent\_GetCurrentRecognizer(ArkUI\_ParallelInnerGestureEvent\* event)](#oh_arkui_parallelinnergestureevent_getcurrentrecognizer) | \- | Obtains the current gesture recognizer in a parallel built-in gesture event. |
| [int32\_t OH\_ArkUI\_ParallelInnerGestureEvent\_GetConflictRecognizers(ArkUI\_ParallelInnerGestureEvent\* event,ArkUI\_GestureRecognizerHandleArray\* array, int32\_t\* size)](#oh_arkui_parallelinnergestureevent_getconflictrecognizers) | \- | Obtains the conflicting gesture recognizers in a parallel built-in gesture event. |
| [int32\_t OH\_ArkUI\_SetArkUIGestureRecognizerDisposeNotify(ArkUI\_GestureRecognizer\* recognizer,ArkUI\_GestureRecognizerDisposeNotifyCallback callback, void\* userData)](#oh_arkui_setarkuigesturerecognizerdisposenotify) | \- | Sets a callback function for notifying gesture recognizer destruction. |
| [int32\_t OH\_ArkUI\_GetGestureParam\_DirectMask(ArkUI\_GestureRecognizer\* recognizer, ArkUI\_GestureDirectionMask\* directMask)](#oh_arkui_getgestureparam_directmask) | \- | Obtains the swipe direction of a gesture recognizer. |
| [int32\_t OH\_ArkUI\_GetGestureParam\_FingerCount(ArkUI\_GestureRecognizer\* recognizer, int\* finger)](#oh_arkui_getgestureparam_fingercount) | \- | Obtains the number of fingers used by a gesture recognizer. |
| [int32\_t OH\_ArkUI\_GetGestureParam\_limitFingerCount(ArkUI\_GestureRecognizer\* recognizer, bool\* isLimited)](#oh_arkui_getgestureparam_limitfingercount) | \- | Checks whether a gesture recognizer has a finger count limit. |
| [int32\_t OH\_ArkUI\_GetGestureParam\_repeat(ArkUI\_GestureRecognizer\* recognizer, bool\* isRepeat)](#oh_arkui_getgestureparam_repeat) | \- | Checks whether a gesture recognizer continuously triggers event callbacks. |
| [int32\_t OH\_ArkUI\_GetGestureParam\_distance(ArkUI\_GestureRecognizer\* recognizer, double\* distance)](#oh_arkui_getgestureparam_distance) | \- | Obtains the allowed movement distance range for a gesture recognizer. |
| [int32\_t OH\_ArkUI\_GetGestureParam\_speed(ArkUI\_GestureRecognizer\* recognizer, double\* speed)](#oh_arkui_getgestureparam_speed) | \- | Obtains the minimum swipe speed recognized by a gesture recognizer. |
| [int32\_t OH\_ArkUI\_GetGestureParam\_duration(ArkUI\_GestureRecognizer\* recognizer, int\* duration)](#oh_arkui_getgestureparam_duration) | \- | Obtains the minimum duration required to trigger a long press by a gesture recognizer. |
| [int32\_t OH\_ArkUI\_GetGestureParam\_angle(ArkUI\_GestureRecognizer\* recognizer, double\* angle)](#oh_arkui_getgestureparam_angle) | \- | Obtains the minimum angle change required for a rotation gesture to be recognized by a gesture recognizer. |
| [int32\_t OH\_ArkUI\_GetGestureParam\_distanceThreshold(ArkUI\_GestureRecognizer\* recognizer, double\* distanceThreshold)](#oh_arkui_getgestureparam_distancethreshold) | \- | Obtains the movement threshold distance for gesture recognition. |
| [ArkUI\_ErrorCode OH\_ArkUI\_PanGesture\_SetDistanceMap(ArkUI\_GestureRecognizer\* recognizer, int size, int\* toolTypeArray, double\* distanceArray)](#oh_arkui_pangesture_setdistancemap) | \- | Sets the minimum sliding distance threshold mapping for gesture recognition. |
| [ArkUI\_ErrorCode OH\_ArkUI\_PanGesture\_GetDistanceByToolType(ArkUI\_GestureRecognizer\* recognizer, int toolType, double\* distance)](#oh_arkui_pangesture_getdistancebytooltype) | \- | Obtains the movement distance threshold for gesture recognition for a specific input device type. This API only returns values for device types previously set using **OH\_ArkUI\_PanGesture\_SetDistanceMap**. The default pan gesture activation threshold can be obtained using **UI\_INPUT\_EVENT\_TOOL\_TYPE\_UNKNOWN**. This API returns no value for unconfigured device types. |
| [ArkUI\_ErrorCode OH\_ArkUI\_SetTouchTestDoneCallback(ArkUI\_NodeHandle node,void\* userData,void (\*touchTestDone)(ArkUI\_GestureEvent\* event,ArkUI\_GestureRecognizerHandleArray recognizers,int32\_t count,void\* userData))](#oh_arkui_settouchtestdonecallback) | \- | Registers a callback that is executed after all gesture recognizers are collected. When the user begins touching the screen, the system performs hit testing and collects gesture recognizers based on the touch location. Subsequently, before processing any move events, the component can use this API to determine the gesture recognizers that will participate in and compete for recognition. |
| [void\* OH\_ArkUI\_GestureInterrupter\_GetUserData(ArkUI\_GestureInterruptInfo\* event)](#oh_arkui_gestureinterrupter_getuserdata) | \- | Obtains the custom data from a gesture interruption event. |
| [ArkUI\_ErrorCode OH\_ArkUI\_PreventGestureRecognizerBegin(ArkUI\_GestureRecognizer\* recognizer)](#oh_arkui_preventgesturerecognizerbegin) | \- | Prevents a gesture recognizer from participating in the current gesture recognition before all fingers are lifted. If the system has already determined the result of the gesture recognizer (regardless of success or failure), calling this API will be ineffective. |
| [ArkUI\_ErrorCode OH\_ArkUI\_LongPressGesture\_SetAllowableMovement(ArkUI\_GestureRecognizer\* recognizer, double allowableMovement)](#oh_arkui_longpressgesture_setallowablemovement) | \- | Sets the maximum movement distance allowed for gesture recognition by the long press gesture recognizer. |
| [ArkUI\_ErrorCode OH\_ArkUI\_LongPressGesture\_GetAllowableMovement(ArkUI\_GestureRecognizer\* recognizer, double\* allowableMovement)](#oh_arkui_longpressgesture_getallowablemovement) | \- | Obtains the maximum movement distance allowed for gesture recognition by the long press gesture recognizer. |

#### \[h2\]Variables

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| uint32\_t | ArkUI\_GestureDirectionMask | 
Defines a set of gesture directions.

Example: **ArkUI\_GestureDirectionMask directions = GESTURE\_DIRECTION\_LEFT | GESTURE\_DIRECTION\_RIGHT**.

This example indicates that the leftward and rightward directions are supported.

 |
| uint32\_t | ArkUI\_GestureEventActionTypeMask | Defines a set of gesture event types. Example: \*\*ArkUI\_GestureEventActionTypeMask actions = GESTURE\_EVENT\_ACTION\_ACCEPT | GESTURE\_EVENT\_ACTION\_UPDATE |

#### \[h2\]Example

| Name | Description |
| :-- | :-- |
| [NdkGestureSetting](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/ArkUISample/NdkGestureSetting) | Examples demonstrating gesture binding, gesture removal, and custom gesture detection are added since API version 20. |
| [NdkGestureNestScroll](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/ArkUISample/NdkGestureNestScroll) | Examples demonstrating nested scrolling through gesture APIs are added since API version 20. |
| [NdkGestureBlocking](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/ArkUISample/NdkGestureBlocking) | Examples demonstrating gesture interception are added since API version 20. |

#### Enum Description

#### \[h2\]ArkUI\_GestureEventActionType

enum ArkUI\_GestureEventActionType

**Description**

Enumerates gesture event types.

**Since**: 12

| Value | Description |
| :-- | :-- |
| GESTURE\_EVENT\_ACTION\_ACCEPT = 0x01 | Triggered. |
| GESTURE\_EVENT\_ACTION\_UPDATE = 0x02 | Updated. |
| GESTURE\_EVENT\_ACTION\_END = 0x04 | Ended. |
| GESTURE\_EVENT\_ACTION\_CANCEL = 0x08 | Canceled. |

#### \[h2\]ArkUI\_GesturePriority

enum ArkUI\_GesturePriority

**Description**

Enumerates gesture event modes.

**Since**: 12

| Value | Description |
| :-- | :-- |
| NORMAL = 0 | Normal. |
| PRIORITY = 1 | High priority. |
| PARALLEL = 2 | Parallel. |

#### \[h2\]ArkUI\_GroupGestureMode

enum ArkUI\_GroupGestureMode

**Description**

Enumerates gesture group modes.

**Since**: 12

| Value | Description |
| :-- | :-- |
| SEQUENTIAL\_GROUP = 0 | Sequential recognition. Gestures are recognized in the registration sequence until all gestures are recognized successfully. Once one gesture fails to be recognized, all subsequent gestures fail to be recognized. Only the last gesture in the gesture group can respond to the end event. |
| PARALLEL\_GROUP = 1 | Parallel recognition. Registered gestures are recognized concurrently until all gestures are recognized. The recognition result of each gesture does not affect each other. |
| EXCLUSIVE\_GROUP = 2 | Exclusive recognition. Registered gestures are identified concurrently. If one gesture is successfully recognized, gesture recognition ends. |

#### \[h2\]ArkUI\_GestureDirection

enum ArkUI\_GestureDirection

**Description**

Enumerates gesture directions.

**Since**: 12

| Value | Description |
| :-- | :-- |
| GESTURE\_DIRECTION\_ALL = 0b1111 | All directions. |
| GESTURE\_DIRECTION\_HORIZONTAL = 0b0011 | Horizontal direction. |
| GESTURE\_DIRECTION\_VERTICAL = 0b1100 | Vertical direction. |
| GESTURE\_DIRECTION\_LEFT = 0b0001 | Leftward. |
| GESTURE\_DIRECTION\_RIGHT = 0b0010 | Rightward. |
| GESTURE\_DIRECTION\_UP = 0b0100 | Upward. |
| GESTURE\_DIRECTION\_DOWN = 0b1000 | Downward. |
| GESTURE\_DIRECTION\_NONE = 0 | None. |

#### \[h2\]ArkUI\_GestureMask

enum ArkUI\_GestureMask

**Description**

Enumerates gesture masking modes.

**Since**: 12

| Value | Description |
| :-- | :-- |
| NORMAL\_GESTURE\_MASK = 0 | The gestures of child components are enabled and recognized based on the default gesture recognition sequence. |
| IGNORE\_INTERNAL\_GESTURE\_MASK = 1 | The gestures of child components are disabled, including the built-in gestures. |

#### \[h2\]ArkUI\_GestureRecognizerType

enum ArkUI\_GestureRecognizerType

**Description**

Enumerates gesture recognizer types.

**Since**: 12

| Value | Description |
| :-- | :-- |
| TAP\_GESTURE = 0 | Tap. |
| LONG\_PRESS\_GESTURE = 1 | Long press. |
| PAN\_GESTURE = 2 | Pan. |
| PINCH\_GESTURE = 3 | Pinch. |
| ROTATION\_GESTURE = 4 | Rotate. |
| SWIPE\_GESTURE = 5 | Swipe. |
| GROUP\_GESTURE = 6 | A group of gestures. |
| CLICK\_GESTURE = 7 | 
Click gesture registered with **onClick**.

**Since**: 20

 |
| DRAG\_DROP = 8 | 

Drag-and-drop gesture.

**Since**: 20

 |

#### \[h2\]ArkUI\_GestureInterruptResult

enum ArkUI\_GestureInterruptResult

**Description**

Enumerates gesture interruption results.

**Since**: 12

| Value | Description |
| :-- | :-- |
| GESTURE\_INTERRUPT\_RESULT\_CONTINUE = 0 | The gesture recognition process continues. |
| GESTURE\_INTERRUPT\_RESULT\_REJECT = 1 | The gesture recognition process is paused. |

#### \[h2\]ArkUI\_GestureRecognizerState

enum ArkUI\_GestureRecognizerState

**Description**

Enumerates the gesture recognizer states.

**Since**: 12

| Value | Description |
| :-- | :-- |
| ARKUI\_GESTURE\_RECOGNIZER\_STATE\_READY = 0 | Ready. |
| ARKUI\_GESTURE\_RECOGNIZER\_STATE\_DETECTING = 1 | Detecting. |
| ARKUI\_GESTURE\_RECOGNIZER\_STATE\_PENDING = 2 | Pending. |
| ARKUI\_GESTURE\_RECOGNIZER\_STATE\_BLOCKED = 3 | Blocked. |
| ARKUI\_GESTURE\_RECOGNIZER\_STATE\_SUCCESSFUL = 4 | Successful. |
| ARKUI\_GESTURE\_RECOGNIZER\_STATE\_FAILED = 5 | Failed. |

#### Function Description

#### \[h2\]ArkUI\_GestureRecognizerDisposeNotifyCallback()

typedef void (\*ArkUI\_GestureRecognizerDisposeNotifyCallback)(ArkUI\_GestureRecognizer\* recognizer, void\* userData)

**Description**

Defines a callback function for notifying gesture recognizer destruction.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_GestureRecognizer](../../structs/arkui-gesturerecognizer/document.md)\* recognizer | Pointer to the gesture recognizer instance. |
| void\* userData | Pointer to user-defined data. |

#### \[h2\]OH\_ArkUI\_GestureInterruptInfo\_GetSystemFlag()

bool OH\_ArkUI\_GestureInterruptInfo\_GetSystemFlag(const ArkUI\_GestureInterruptInfo\* event)

**Description**

Checks whether a gesture is a system built-in gesture.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [ArkUI\_GestureInterruptInfo](../../structs/arkui-gestureinterruptinfo/document.md)\* event | Pointer to the gesture interruption callback event. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | 
**true**: built-in gesture.

**false**: non-built-in gesture.

 |

#### \[h2\]OH\_ArkUI\_GestureInterruptInfo\_GetRecognizer()

ArkUI\_GestureRecognizer\* OH\_ArkUI\_GestureInterruptInfo\_GetRecognizer(const ArkUI\_GestureInterruptInfo\* event)

**Description**

Obtains the pointer to the interrupted gesture recognizer.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [ArkUI\_GestureInterruptInfo](../../structs/arkui-gestureinterruptinfo/document.md)\* event | Pointer to the gesture interruption callback event. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ArkUI\_GestureRecognizer](../../structs/arkui-gesturerecognizer/document.md)\* | Pointer to the interrupted gesture recognizer. |

#### \[h2\]OH\_ArkUI\_GestureInterruptInfo\_GetGestureEvent()

ArkUI\_GestureEvent\* OH\_ArkUI\_GestureInterruptInfo\_GetGestureEvent(const ArkUI\_GestureInterruptInfo\* event)

**Description**

Obtains the pointer to the interrupted gesture event.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [ArkUI\_GestureInterruptInfo](../../structs/arkui-gestureinterruptinfo/document.md)\* event | Pointer to the gesture interruption callback event. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ArkUI\_GestureEvent](../../structs/arkui-gestureevent/document.md)\* | Pointer to the interrupted gesture event. |

#### \[h2\]OH\_ArkUI\_GestureInterruptInfo\_GetSystemRecognizerType()

int32\_t OH\_ArkUI\_GestureInterruptInfo\_GetSystemRecognizerType(const ArkUI\_GestureInterruptInfo\* event)

**Description**

Obtains the type of the system built-in gesture to trigger.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [ArkUI\_GestureInterruptInfo](../../structs/arkui-gestureinterruptinfo/document.md)\* event | Pointer to the gesture interruption callback event. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | Type of the system built-in gesture to trigger. The value is defined in [ArkUI\_GestureRecognizerType](#arkui_gesturerecognizertype). If the triggered gesture is not a built-in gesture, **\-1** is returned. |

#### \[h2\]OH\_ArkUI\_GestureInterruptInfo\_GetTouchRecognizers()

int32\_t OH\_ArkUI\_GestureInterruptInfo\_GetTouchRecognizers(const ArkUI\_GestureInterruptInfo\* info,ArkUI\_TouchRecognizerHandleArray\* recognizers, int32\_t\* size)

**Description**

Obtains touch recognizers from gesture interruption information.

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| const [ArkUI\_GestureInterruptInfo](../../structs/arkui-gestureinterruptinfo/document.md)\* info | Pointer to the gesture interruption information. |
| [ArkUI\_TouchRecognizerHandleArray](../../structs/arkui-touchrecognizerhandle/document.md)\* recognizers | Pointer to the array of touch recognizers. |
| int32\_t\* size | Pointer to the size of the touch recognizer array. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_TouchRecognizer\_GetNodeHandle()

ArkUI\_NodeHandle OH\_ArkUI\_TouchRecognizer\_GetNodeHandle(const ArkUI\_TouchRecognizerHandle recognizer)

**Description**

Obtains the component handle corresponding to a touch recognizer.

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| const [ArkUI\_TouchRecognizerHandle](../../structs/arkui-touchrecognizerhandle/document.md) recognizer | Handle to the touch recognizer. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) | Component handle corresponding to the touch recognizer. |

#### \[h2\]OH\_ArkUI\_TouchRecognizer\_CancelTouch()

int32\_t OH\_ArkUI\_TouchRecognizer\_CancelTouch(ArkUI\_TouchRecognizerHandle recognizer, ArkUI\_GestureInterruptInfo\* info)

**Description**

Sends a cancel touch event to a touch recognizer in a gesture interruption callback.

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_TouchRecognizerHandle](../../structs/arkui-touchrecognizerhandle/document.md) recognizer | Handle to the touch recognizer. |
| [ArkUI\_GestureInterruptInfo](../../structs/arkui-gestureinterruptinfo/document.md)\* info | Pointer to the gesture interruption information. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_GestureEvent\_GetActionType()

ArkUI\_GestureEventActionType OH\_ArkUI\_GestureEvent\_GetActionType(const ArkUI\_GestureEvent\* event)

**Description**

Obtains the gesture event type.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [ArkUI\_GestureEvent](../../structs/arkui-gestureevent/document.md)\* event | Pointer to the gesture event. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ArkUI\_GestureEventActionType](#arkui_gestureeventactiontype) | Type of the gesture event. |

#### \[h2\]OH\_ArkUI\_GestureEvent\_GetRawInputEvent()

const ArkUI\_UIInputEvent\* OH\_ArkUI\_GestureEvent\_GetRawInputEvent(const ArkUI\_GestureEvent\* event)

**Description**

Obtains gesture input.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [ArkUI\_GestureEvent](../../structs/arkui-gestureevent/document.md)\* event | Pointer to the gesture event. |

**Returns**

| Type | Description |
| :-- | :-- |
| const [ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md)\* | Pointer to the input event of the gesture event. |

#### \[h2\]OH\_ArkUI\_LongPress\_GetRepeatCount()

int32\_t OH\_ArkUI\_LongPress\_GetRepeatCount(const ArkUI\_GestureEvent\* event)

**Description**

Checks whether the event is a repeated trigger event.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [ArkUI\_GestureEvent](../../structs/arkui-gestureevent/document.md)\* event | Pointer to the gesture event. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | Whether the event is a repeated trigger event. The value **1** means that the event is a repeated trigger event, and **0** means the opposite. |

#### \[h2\]OH\_ArkUI\_PanGesture\_GetVelocity()

float OH\_ArkUI\_PanGesture\_GetVelocity(const ArkUI\_GestureEvent\* event)

**Description**

Obtains the velocity of a pan gesture along the main axis.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [ArkUI\_GestureEvent](../../structs/arkui-gestureevent/document.md)\* event | Pointer to the gesture event. |

**Returns**

| Type | Description |
| :-- | :-- |
| float | Velocity of the pan gesture along the main axis, in px/s. The value is the square root of the sum of the squares of the velocity on the x-axis and y-axis. |

#### \[h2\]OH\_ArkUI\_PanGesture\_GetVelocityX()

float OH\_ArkUI\_PanGesture\_GetVelocityX(const ArkUI\_GestureEvent\* event)

**Description**

Obtains the velocity of a pan gesture along the x-axis.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [ArkUI\_GestureEvent](../../structs/arkui-gestureevent/document.md)\* event | Pointer to the gesture event. |

**Returns**

| Type | Description |
| :-- | :-- |
| float | Velocity of the pan gesture along the x-axis, in px/s. |

#### \[h2\]OH\_ArkUI\_PanGesture\_GetVelocityY()

float OH\_ArkUI\_PanGesture\_GetVelocityY(const ArkUI\_GestureEvent\* event)

**Description**

Obtains the velocity of a pan gesture along the y-axis.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [ArkUI\_GestureEvent](../../structs/arkui-gestureevent/document.md)\* event | Pointer to the gesture event. |

**Returns**

| Type | Description |
| :-- | :-- |
| float | Velocity of the pan gesture along the y-axis, in px/s. |

#### \[h2\]OH\_ArkUI\_PanGesture\_GetOffsetX()

float OH\_ArkUI\_PanGesture\_GetOffsetX(const ArkUI\_GestureEvent\* event)

**Description**

Obtains the relative offset of a pan gesture along the x-axis.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [ArkUI\_GestureEvent](../../structs/arkui-gestureevent/document.md)\* event | Pointer to the gesture event. |

**Returns**

| Type | Description |
| :-- | :-- |
| float | Relative offset of the gesture along the x-axis, in px. |

#### \[h2\]OH\_ArkUI\_PanGesture\_GetOffsetY()

float OH\_ArkUI\_PanGesture\_GetOffsetY(const ArkUI\_GestureEvent\* event)

**Description**

Obtains the relative offset of a pan gesture along the y-axis.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [ArkUI\_GestureEvent](../../structs/arkui-gestureevent/document.md)\* event | Pointer to the gesture event. |

**Returns**

| Type | Description |
| :-- | :-- |
| float | Relative offset of the gesture along the y-axis, in px. |

#### \[h2\]OH\_ArkUI\_SwipeGesture\_GetAngle()

float OH\_ArkUI\_SwipeGesture\_GetAngle(const ArkUI\_GestureEvent\* event)

**Description**

Obtains the angle information of the swipe gesture. After a swipe gesture is recognized, a line connecting the two fingers is identified as the initial line. As the fingers swipe, the line between the fingers rotates.

Based on the coordinates of the initial line's and current line's end points, the arc tangent function is used to calculate the respective included angle of the points relative to the horizontal direction

by using the following formula: Rotation angle = arctan2(cy2-cy1,cx2-cx1) - arctan2(y2-y1,x2-x1).

The initial line is used as the coordinate system. The clockwise rotation is 0 to 180 degrees, and the counter-clockwise rotation is -180 to 0 degrees.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [ArkUI\_GestureEvent](../../structs/arkui-gestureevent/document.md)\* event | Pointer to the gesture event. |

**Returns**

| Type | Description |
| :-- | :-- |
| float | Angle of the swipe gesture, which is the result obtained based on the aforementioned formula. The unit is deg. |

#### \[h2\]OH\_ArkUI\_SwipeGesture\_GetVelocity()

float OH\_ArkUI\_SwipeGesture\_GetVelocity(const ArkUI\_GestureEvent\* event)

**Description**

Obtains the average velocity of all fingers used in the swipe gesture.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [ArkUI\_GestureEvent](../../structs/arkui-gestureevent/document.md)\* event | Pointer to the gesture event. |

**Returns**

| Type | Description |
| :-- | :-- |
| float | Average velocity of all fingers used in the swipe gesture, in px/s. |

#### \[h2\]OH\_ArkUI\_RotationGesture\_GetAngle()

float OH\_ArkUI\_RotationGesture\_GetAngle(const ArkUI\_GestureEvent\* event)

**Description**

Obtains the angle information of a rotation gesture.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [ArkUI\_GestureEvent](../../structs/arkui-gestureevent/document.md)\* event | Pointer to the gesture event. |

**Returns**

| Type | Description |
| :-- | :-- |
| float | Rotation angle. The unit is deg. |

#### \[h2\]OH\_ArkUI\_PinchGesture\_GetScale()

float OH\_ArkUI\_PinchGesture\_GetScale(const ArkUI\_GestureEvent\* event)

**Description**

Obtains the scale ratio of a pinch gesture.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [ArkUI\_GestureEvent](../../structs/arkui-gestureevent/document.md)\* event | Pointer to the gesture event. |

**Returns**

| Type | Description |
| :-- | :-- |
| float | Scale factor. |

#### \[h2\]OH\_ArkUI\_PinchGesture\_GetCenterX()

float OH\_ArkUI\_PinchGesture\_GetCenterX(const ArkUI\_GestureEvent\* event)

**Description**

Obtains the x-coordinate of the center of the pinch gesture, in vp, relative to the upper left corner of the current component.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [ArkUI\_GestureEvent](../../structs/arkui-gestureevent/document.md)\* event | Pointer to the gesture event. |

**Returns**

| Type | Description |
| :-- | :-- |
| float | X-coordinate of the center of the pinch gesture, in px, relative to the upper left corner of the current component. |

#### \[h2\]OH\_ArkUI\_PinchGesture\_GetCenterY()

float OH\_ArkUI\_PinchGesture\_GetCenterY(const ArkUI\_GestureEvent\* event)

**Description**

Obtains the y-coordinate of the center of the pinch gesture, in vp, relative to the upper left corner of the current component.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [ArkUI\_GestureEvent](../../structs/arkui-gestureevent/document.md)\* event | Pointer to the gesture event. |

**Returns**

| Type | Description |
| :-- | :-- |
| float | Y-coordinate of the center of the pinch gesture, in px, relative to the upper left corner of the current component. |

#### \[h2\]OH\_ArkUI\_GestureEvent\_GetNode()

ArkUI\_NodeHandle OH\_ArkUI\_GestureEvent\_GetNode(const ArkUI\_GestureEvent\* event)

**Description**

Obtains the ArkUI component to which the gesture is bound.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [ArkUI\_GestureEvent](../../structs/arkui-gestureevent/document.md)\* event | Pointer to the gesture event. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) | ArkUI component to which the gesture is bound. Returns **NULL** if the event is invalid. |

#### \[h2\]OH\_ArkUI\_GetResponseRecognizersFromInterruptInfo()

int32\_t OH\_ArkUI\_GetResponseRecognizersFromInterruptInfo(const ArkUI\_GestureInterruptInfo\* event,ArkUI\_GestureRecognizerHandleArray\* responseChain, int32\_t\* count)

**Description**

Obtains information about a gesture response chain.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [ArkUI\_GestureInterruptInfo](../../structs/arkui-gestureinterruptinfo/document.md)\* event | Pointer to the gesture interruption callback event. |
| [ArkUI\_GestureRecognizerHandleArray](../../structs/arkui-gesturerecognizerhandle/document.md)\* responseChain | Pointer to an array of gesture recognizers on the response chain. |
| int32\_t\* count | Pointer to the number of gesture recognizers on the response chain. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_SetGestureRecognizerEnabled()

int32\_t OH\_ArkUI\_SetGestureRecognizerEnabled(ArkUI\_GestureRecognizer\* recognizer, bool enabled)

**Description**

Sets the enabled state of a gesture recognizer.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_GestureRecognizer](../../structs/arkui-gesturerecognizer/document.md)\* recognizer | Pointer to the gesture recognizer instance. |
| bool enabled | Enabled state. The value **true** means that the gesture recognizer is enabled, and **false** means the opposite. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_SetGestureRecognizerLimitFingerCount()

int32\_t OH\_ArkUI\_SetGestureRecognizerLimitFingerCount(ArkUI\_GestureRecognizer\* recognizer, bool limitFingerCount)

**Description**

Sets whether to enable strict finger count checking. If this feature is enabled and the actual number of touch fingers does not match the set number, the gesture recognition fails.

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_GestureRecognizer](../../structs/arkui-gesturerecognizer/document.md)\* recognizer | Pointer to the gesture recognizer instance. |
| bool limitFingerCount | 
Whether to enable strict finger count checking.

**true**: Enforce the exact number of fingers touching the screen.

**false**: Do not enforce the exact number of fingers touching the screen.

 |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_GetGestureRecognizerEnabled()

bool OH\_ArkUI\_GetGestureRecognizerEnabled(ArkUI\_GestureRecognizer\* recognizer)

**Description**

Obtains the enabled state of a gesture recognizer.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_GestureRecognizer](../../structs/arkui-gesturerecognizer/document.md)\* recognizer | Pointer to the gesture recognizer instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | 
**true**: enabled.

**false**: disabled.

 |

#### \[h2\]OH\_ArkUI\_GetGestureRecognizerState()

int32\_t OH\_ArkUI\_GetGestureRecognizerState(ArkUI\_GestureRecognizer\* recognizer, ArkUI\_GestureRecognizerState\* state)

**Description**

Obtains the state of a gesture recognizer.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_GestureRecognizer](../../structs/arkui-gesturerecognizer/document.md)\* recognizer | Pointer to the gesture recognizer instance. |
| [ArkUI\_GestureRecognizerState](#arkui_gesturerecognizerstate)\* state | Pointer to the state of the gesture recognizer. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_GetGestureEventTargetInfo()

int32\_t OH\_ArkUI\_GetGestureEventTargetInfo(ArkUI\_GestureRecognizer\* recognizer, ArkUI\_GestureEventTargetInfo\*\* info)

**Description**

Obtains the information about a gesture event target.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_GestureRecognizer](../../structs/arkui-gesturerecognizer/document.md)\* recognizer | Pointer to the gesture recognizer instance. |
| [ArkUI\_GestureEventTargetInfo](../../structs/arkui-gestureeventtargetinfo/document.md)\*\* info | Pointer to the information about a gesture event target. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_GestureEventTargetInfo\_IsScrollBegin()

int32\_t OH\_ArkUI\_GestureEventTargetInfo\_IsScrollBegin(ArkUI\_GestureEventTargetInfo\* info, bool\* ret)

**Description**

Obtains whether this scrollable container component is scrolled to the top.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_GestureEventTargetInfo](../../structs/arkui-gestureeventtargetinfo/document.md)\* info | Pointer to the information about a gesture event target. |
| bool\* ret | Pointer to the parameter indicating whether this scrollable container component is scrolled to the top. The value **true** means that the component is scrolled to the top, and **false** means the opposite. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_NON\_SCROLLABLE\_CONTAINER](../native-type-h/document.md#arkui_errorcode) if the component is not a scrollable container.

 |

#### \[h2\]OH\_ArkUI\_GestureEventTargetInfo\_IsScrollEnd()

int32\_t OH\_ArkUI\_GestureEventTargetInfo\_IsScrollEnd(ArkUI\_GestureEventTargetInfo\* info, bool\* ret)

**Description**

Obtains whether this scrollable container component is scrolled to the bottom.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_GestureEventTargetInfo](../../structs/arkui-gestureeventtargetinfo/document.md)\* info | Pointer to the information about a gesture event target. |
| bool\* ret | Pointer to the parameter indicating whether this scrollable container component is scrolled to the bottom. The value **true** means that the component is scrolled to the bottom, and **false** means the opposite. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_NON\_SCROLLABLE\_CONTAINER](../native-type-h/document.md#arkui_errorcode) if the component is not a scrollable container.

 |

#### \[h2\]OH\_ArkUI\_GetPanGestureDirectionMask()

int32\_t OH\_ArkUI\_GetPanGestureDirectionMask(ArkUI\_GestureRecognizer\* recognizer,ArkUI\_GestureDirectionMask\* directionMask)

**Description**

Obtains the direction of a pan gesture.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_GestureRecognizer](../../structs/arkui-gesturerecognizer/document.md)\* recognizer | Pointer to the gesture recognizer instance. |
| [ArkUI\_GestureDirectionMask](#variables)\* directionMask | Pointer to the pan direction. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_IsBuiltInGesture()

bool OH\_ArkUI\_IsBuiltInGesture(ArkUI\_GestureRecognizer\* recognizer)

**Description**

Obtains whether a gesture is a system built-in gesture.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_GestureRecognizer](../../structs/arkui-gesturerecognizer/document.md)\* recognizer | Pointer to the gesture recognizer instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | 
**true**: built-in gesture.

**false**: non-built-in gesture.

 |

#### \[h2\]OH\_ArkUI\_GetGestureTag()

int32\_t OH\_ArkUI\_GetGestureTag(ArkUI\_GestureRecognizer\* recognizer, char\* buffer, int32\_t bufferSize, int32\_t\* result)

**Description**

Obtains the tag of a gesture recognizer.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_GestureRecognizer](../../structs/arkui-gesturerecognizer/document.md)\* recognizer | Pointer to the gesture recognizer instance. |
| char\* buffer | Pointer to the output buffer. |
| int32\_t bufferSize | Size of the output buffer. |
| int32\_t\* result | Pointer to the length of the copied string. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_BUFFER\_SIZE\_NOT\_ENOUGH](../native-type-h/document.md#arkui_errorcode) if the buffer is not large enough.

 |

#### \[h2\]OH\_ArkUI\_GetGestureBindNodeId()

int32\_t OH\_ArkUI\_GetGestureBindNodeId(ArkUI\_GestureRecognizer\* recognizer, char\* nodeId, int32\_t size,int32\_t\* result)

**Description**

Obtains the ID of the component linked to a gesture recognizer.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_GestureRecognizer](../../structs/arkui-gesturerecognizer/document.md)\* recognizer | Pointer to the gesture recognizer instance. |
| char\* nodeId | Pointer to the component ID. |
| int32\_t size | Size of the output buffer. |
| int32\_t\* result | Pointer to the length of the copied string. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_BUFFER\_SIZE\_NOT\_ENOUGH](../native-type-h/document.md#arkui_errorcode) if the buffer is not large enough.

 |

#### \[h2\]OH\_ArkUI\_IsGestureRecognizerValid()

bool OH\_ArkUI\_IsGestureRecognizerValid(ArkUI\_GestureRecognizer\* recognizer)

**Description**

Obtains whether a gesture recognizer is valid.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_GestureRecognizer](../../structs/arkui-gesturerecognizer/document.md)\* recognizer | Pointer to the gesture recognizer instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | 
**true**: The gesture recognizer is valid.

**false**: The gesture recognizer is invalid.

 |

#### \[h2\]OH\_ArkUI\_ParallelInnerGestureEvent\_GetUserData()

void\* OH\_ArkUI\_ParallelInnerGestureEvent\_GetUserData(ArkUI\_ParallelInnerGestureEvent\* event)

**Description**

Obtains custom data in the parallel built-in gesture event.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_ParallelInnerGestureEvent](../../structs/arkui-parallelinnergestureevent/document.md)\* event | Pointer to the parallel built-in gesture event. |

**Returns**

| Type | Description |
| :-- | :-- |
| void\* | Pointer to user-defined data. |

#### \[h2\]OH\_ArkUI\_ParallelInnerGestureEvent\_GetCurrentRecognizer()

ArkUI\_GestureRecognizer\* OH\_ArkUI\_ParallelInnerGestureEvent\_GetCurrentRecognizer(ArkUI\_ParallelInnerGestureEvent\* event)

**Description**

Obtains the current gesture recognizer in a parallel built-in gesture event.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_ParallelInnerGestureEvent](../../structs/arkui-parallelinnergestureevent/document.md)\* event | Pointer to the parallel built-in gesture event. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ArkUI\_GestureRecognizer](../../structs/arkui-gesturerecognizer/document.md)\* | Pointer to the current gesture recognizer. |

#### \[h2\]OH\_ArkUI\_ParallelInnerGestureEvent\_GetConflictRecognizers()

int32\_t OH\_ArkUI\_ParallelInnerGestureEvent\_GetConflictRecognizers(ArkUI\_ParallelInnerGestureEvent\* event,ArkUI\_GestureRecognizerHandleArray\* array, int32\_t\* size)

**Description**

Obtains the conflicting gesture recognizers in a parallel built-in gesture event.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_ParallelInnerGestureEvent](../../structs/arkui-parallelinnergestureevent/document.md)\* event | Pointer to the parallel built-in gesture event. |
| [ArkUI\_GestureRecognizerHandleArray](../../structs/arkui-gesturerecognizerhandle/document.md)\* array | Pointer to the array of conflicting gesture recognizers. |
| int32\_t\* size | Pointer to the size of the array of conflicting gesture recognizers. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_SetArkUIGestureRecognizerDisposeNotify()

int32\_t OH\_ArkUI\_SetArkUIGestureRecognizerDisposeNotify(ArkUI\_GestureRecognizer\* recognizer,ArkUI\_GestureRecognizerDisposeNotifyCallback callback, void\* userData)

**Description**

Sets a callback function for notifying gesture recognizer destruction.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_GestureRecognizer](../../structs/arkui-gesturerecognizer/document.md)\* recognizer | Pointer to the gesture recognizer instance. |
| [ArkUI\_GestureRecognizerDisposeNotifyCallback](#arkui_gesturerecognizerdisposenotifycallback) callback | Callback function for notifying gesture recognizer destruction. |
| void\* userData | Pointer to user-defined data. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_GetGestureParam\_DirectMask()

int32\_t OH\_ArkUI\_GetGestureParam\_DirectMask(ArkUI\_GestureRecognizer\* recognizer, ArkUI\_GestureDirectionMask\* directMask)

**Description**

Obtains the swipe direction of a gesture recognizer.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_GestureRecognizer](../../structs/arkui-gesturerecognizer/document.md)\* recognizer | Pointer to the gesture recognizer instance. |
| [ArkUI\_GestureDirectionMask](#variables)\* directMask | Pointer to the swipe direction of the gesture recognizer. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_GetGestureParam\_FingerCount()

int32\_t OH\_ArkUI\_GetGestureParam\_FingerCount(ArkUI\_GestureRecognizer\* recognizer, int\* finger)

**Description**

Obtains the number of fingers used by a gesture recognizer.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_GestureRecognizer](../../structs/arkui-gesturerecognizer/document.md)\* recognizer | Pointer to the gesture recognizer instance. |
| int\* finger | Pointer to the number of fingers used by the gesture recognizer. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_GetGestureParam\_limitFingerCount()

int32\_t OH\_ArkUI\_GetGestureParam\_limitFingerCount(ArkUI\_GestureRecognizer\* recognizer, bool\* isLimited)

**Description**

Checks whether a gesture recognizer has a finger count limit.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_GestureRecognizer](../../structs/arkui-gesturerecognizer/document.md)\* recognizer | Pointer to the gesture recognizer instance. |
| bool\* isLimited | Pointer to the parameter indicating whether the gesture recognizer has a finger count limit. **true** indicates that the gesture recognizer has a finger count limit. **false** indicates that the gesture recognizer does not have a finger count limit. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_GetGestureParam\_repeat()

int32\_t OH\_ArkUI\_GetGestureParam\_repeat(ArkUI\_GestureRecognizer\* recognizer, bool\* isRepeat)

**Description**

Checks whether a gesture recognizer continuously triggers event callbacks.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_GestureRecognizer](../../structs/arkui-gesturerecognizer/document.md)\* recognizer | Pointer to the gesture recognizer instance. |
| bool\* isRepeat | Pointer to the parameter indicating whether the gesture recognizer continuously triggers event callbacks. The value **true** means to continuously trigger event callbacks, and false means the opposite. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_RECOGNIZER\_TYPE\_NOT\_SUPPORTED](../native-type-h/document.md#arkui_errorcode) if the gesture recognizer type is not supported.

 |

#### \[h2\]OH\_ArkUI\_GetGestureParam\_distance()

int32\_t OH\_ArkUI\_GetGestureParam\_distance(ArkUI\_GestureRecognizer\* recognizer, double\* distance)

**Description**

Obtains the allowed movement distance range for a gesture recognizer.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_GestureRecognizer](../../structs/arkui-gesturerecognizer/document.md)\* recognizer | Pointer to the gesture recognizer instance. |
| double\* distance | Pointer to the allowed movement distance range of the gesture recognizer. The unit is px. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_RECOGNIZER\_TYPE\_NOT\_SUPPORTED](../native-type-h/document.md#arkui_errorcode) if the gesture recognizer type is not supported.

 |

#### \[h2\]OH\_ArkUI\_GetGestureParam\_speed()

int32\_t OH\_ArkUI\_GetGestureParam\_speed(ArkUI\_GestureRecognizer\* recognizer, double\* speed)

**Description**

Obtains the minimum swipe speed recognized by a gesture recognizer.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_GestureRecognizer](../../structs/arkui-gesturerecognizer/document.md)\* recognizer | Pointer to the gesture recognizer instance. |
| double\* speed | Pointer to the minimum swipe speed recognized by the gesture recognizer. The unit is px/s. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_RECOGNIZER\_TYPE\_NOT\_SUPPORTED](../native-type-h/document.md#arkui_errorcode) if the gesture recognizer type is not supported.

 |

#### \[h2\]OH\_ArkUI\_GetGestureParam\_duration()

int32\_t OH\_ArkUI\_GetGestureParam\_duration(ArkUI\_GestureRecognizer\* recognizer, int\* duration)

**Description**

Obtains the minimum duration required to trigger a long press by a gesture recognizer.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_GestureRecognizer](../../structs/arkui-gesturerecognizer/document.md)\* recognizer | Pointer to the gesture recognizer instance. |
| int\* duration | Pointer to the minimum duration for a long press. The unit is ms. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_RECOGNIZER\_TYPE\_NOT\_SUPPORTED](../native-type-h/document.md#arkui_errorcode) if the gesture recognizer type is not supported.

 |

#### \[h2\]OH\_ArkUI\_GetGestureParam\_angle()

int32\_t OH\_ArkUI\_GetGestureParam\_angle(ArkUI\_GestureRecognizer\* recognizer, double\* angle)

**Description**

Obtains the minimum angle change required for a rotation gesture to be recognized by a gesture recognizer.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_GestureRecognizer](../../structs/arkui-gesturerecognizer/document.md)\* recognizer | Pointer to the gesture recognizer instance. |
| double\* angle | Pointer to the minimum angle change. The unit is deg. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_RECOGNIZER\_TYPE\_NOT\_SUPPORTED](../native-type-h/document.md#arkui_errorcode) if the gesture recognizer type is not supported.

 |

#### \[h2\]OH\_ArkUI\_GetGestureParam\_distanceThreshold()

int32\_t OH\_ArkUI\_GetGestureParam\_distanceThreshold(ArkUI\_GestureRecognizer\* recognizer, double\* distanceThreshold)

**Description**

Obtains the movement threshold distance for gesture recognition.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_GestureRecognizer](../../structs/arkui-gesturerecognizer/document.md)\* recognizer | Pointer to the gesture recognizer instance. |
| double\* distanceThreshold | Pointer to the movement distance threshold of the gesture recognizer. The unit is px. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_RECOGNIZER\_TYPE\_NOT\_SUPPORTED](../native-type-h/document.md#arkui_errorcode) if the gesture recognizer type is not supported.

 |

#### \[h2\]OH\_ArkUI\_PanGesture\_SetDistanceMap()

ArkUI\_ErrorCode OH\_ArkUI\_PanGesture\_SetDistanceMap(ArkUI\_GestureRecognizer\* recognizer, int size, int\* toolTypeArray, double\* distanceArray)

**Description**

Sets the minimum sliding distance threshold mapping for gesture recognition.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_GestureRecognizer](../../structs/arkui-gesturerecognizer/document.md)\* recognizer | Pointer to the gesture recognizer instance. |
| int size | Size of the array of minimum sliding distance thresholds. |
| int\* toolTypeArray | Pointer to the array of tool types for which thresholds are set. If a value other than [UI\_INPUT\_EVENT\_TOOL\_TYPE\_XXX](../ui-input-event-h/document.md#anonymous2) is set, the setting does not take effect. |
| double\* distanceArray | Pointer to the array of minimum sliding distances. The unit is px. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ArkUI\_ErrorCode](../native-type-h/document.md#arkui_errorcode) | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_RECOGNIZER\_TYPE\_NOT\_SUPPORTED](../native-type-h/document.md#arkui_errorcode) if the gesture recognizer type is not supported.

 |

#### \[h2\]OH\_ArkUI\_PanGesture\_GetDistanceByToolType()

ArkUI\_ErrorCode OH\_ArkUI\_PanGesture\_GetDistanceByToolType(ArkUI\_GestureRecognizer\* recognizer, int toolType, double\* distance)

**Description**

Obtains the movement distance threshold for gesture recognition for a specific input device type. This API only returns values for device types previously set using **OH\_ArkUI\_PanGesture\_SetDistanceMap**. The default movement distance threshold can be obtained by querying the [UI\_INPUT\_EVENT\_TOOL\_TYPE\_UNKNOWN](../ui-input-event-h/document.md#anonymous2) type. Other types that have not been set are not returned.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_GestureRecognizer](../../structs/arkui-gesturerecognizer/document.md)\* recognizer | Pointer to the gesture recognizer instance. |
| int toolType | Tool type for which you want to obtain the threshold. |
| double\* distance | Pointer to the movement distance threshold of the gesture recognizer. The unit is px. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ArkUI\_ErrorCode](../native-type-h/document.md#arkui_errorcode) | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_RECOGNIZER\_TYPE\_NOT\_SUPPORTED](../native-type-h/document.md#arkui_errorcode) if the gesture recognizer type is not supported.

 |

#### \[h2\]OH\_ArkUI\_SetTouchTestDoneCallback()

ArkUI\_ErrorCode OH\_ArkUI\_SetTouchTestDoneCallback(ArkUI\_NodeHandle node, void\* userData, void (\*touchTestDone)(ArkUI\_GestureEvent\* event, ArkUI\_GestureRecognizerHandleArray recognizers, int32\_t count, void\* userData))

**Description**

Registers a callback that is executed after all gesture recognizers are collected. When the user begins touching the screen, the system performs hit testing and collects gesture recognizers based on the touch location. Subsequently, before processing any move events, the component can use this API to determine the gesture recognizers that will participate in and compete for recognition.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) node | Handle to the node on which the callback is to be set. |
| void\* userData | Pointer to user-defined data. |
| void (\*touchTestDone)([ArkUI\_GestureEvent](../../structs/arkui-gestureevent/document.md)\* event, [ArkUI\_GestureRecognizerHandleArray](../../structs/arkui-gesturerecognizerhandle/document.md) recognizers, int32\_t count, void\* userData) | Callback for completion of gesture recognizer collection. **event** indicates the basic information about the gesture, **recognizers** indicates the gesture recognizer array, **count** indicates the number of gesture recognizers, and **userData** indicates the user-defined data. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ArkUI\_ErrorCode](../native-type-h/document.md#arkui_errorcode) | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_GestureInterrupter\_GetUserData()

void\* OH\_ArkUI\_GestureInterrupter\_GetUserData(ArkUI\_GestureInterruptInfo\* event)

**Description**

Obtains the custom data from a gesture interruption event.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_GestureInterruptInfo](../../structs/arkui-gestureinterruptinfo/document.md)\* event | Pointer to the gesture interruption information. |

**Returns**

| Type | Description |
| :-- | :-- |
| void\* | Pointer to user-defined data. |

#### \[h2\]OH\_ArkUI\_PreventGestureRecognizerBegin()

ArkUI\_ErrorCode OH\_ArkUI\_PreventGestureRecognizerBegin(ArkUI\_GestureRecognizer\* recognizer)

**Description**

Prevents a gesture recognizer from participating in the current gesture recognition before all fingers are lifted. If the system has already determined the result of the gesture recognizer (regardless of success or failure), calling this API will be ineffective.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_GestureRecognizer](../../structs/arkui-gesturerecognizer/document.md)\* recognizer | Pointer to the gesture recognizer instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ArkUI\_ErrorCode](../native-type-h/document.md#arkui_errorcode) | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_LongPressGesture\_SetAllowableMovement()

ArkUI\_ErrorCode OH\_ArkUI\_LongPressGesture\_SetAllowableMovement(ArkUI\_GestureRecognizer\* recognizer, double allowableMovement)

**Description**

Sets the maximum movement distance allowed for gesture recognition by the long press gesture recognizer.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_GestureRecognizer](../../structs/arkui-gesturerecognizer/document.md)\* recognizer | Pointer to the gesture recognizer instance. |
| double allowableMovement | 
Maximum movement distance allowed for gesture recognition by the long press gesture recognizer.

The unit is px.

Value range: (0, +∞). If the value is less than or equal to 0, the default value **15** is used.

 |

**Returns**

| Type | Description |
| :-- | :-- |
| [ArkUI\_ErrorCode](../native-type-h/document.md#arkui_errorcode) | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_RECOGNIZER\_TYPE\_NOT\_SUPPORTED](../native-type-h/document.md#arkui_errorcode) if the gesture recognizer type is not supported.

 |

#### \[h2\]OH\_ArkUI\_LongPressGesture\_GetAllowableMovement()

ArkUI\_ErrorCode OH\_ArkUI\_LongPressGesture\_GetAllowableMovement(ArkUI\_GestureRecognizer\* recognizer, double\* allowableMovement)

**Description**

Obtains the maximum movement distance allowed for gesture recognition by the long press gesture recognizer.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_GestureRecognizer](../../structs/arkui-gesturerecognizer/document.md)\* recognizer | Pointer to the gesture recognizer instance. |
| double\* allowableMovement | Pointer to the maximum movement distance allowed for gesture recognition by the long press gesture recognizer. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ArkUI\_ErrorCode](../native-type-h/document.md#arkui_errorcode) | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_RECOGNIZER\_TYPE\_NOT\_SUPPORTED](../native-type-h/document.md#arkui_errorcode) if the gesture recognizer type is not supported.

 |
