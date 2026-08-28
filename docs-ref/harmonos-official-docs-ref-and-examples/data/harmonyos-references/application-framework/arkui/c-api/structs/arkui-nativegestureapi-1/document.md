# ArkUI\_NativeGestureAPI\_1

typedef struct {...} ArkUI\_NativeGestureAPI\_1

#### Overview

Defines the gesture APIs.

**Since**: 12

**Related module**: [ArkUI\_NativeModule](../../modules/arkui-nativemodule/document.md)

**Header file**: [native\_gesture.h](../../header-files/native-gesture-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| int32\_t version | The struct version is 1. |

#### \[h2\]Member Functions

| Name | Description |
| :-- | :-- |
| [ArkUI\_GestureRecognizer\* (\*createTapGesture)(int32\_t countNum, int32\_t fingersNum)](#createtapgesture) | 
Creates a tap gesture.

1\. This API is used to trigger a tap gesture with one, two, or more taps.

2\. If multi-tap is configured, the timeout interval between a lift and the next tap is 300 ms.

3\. If the distance between the last tapped position and the current tapped position exceeds 60 vp, gesture recognition fails.

4\. When multiple fingers are configured for a gesture, the recognition fails if the number of fingers touching the screen within 300 ms of the initial touch is less than the required count, or if the number of fingers lifted from the screen within 300 ms of the first finger's being lifted is less than the required count.

5\. When the number of fingers touching the screen exceeds the set value, the gesture can be recognized.

 |
| [ArkUI\_GestureRecognizer\* (\*createLongPressGesture)(int32\_t fingersNum, bool repeatResult, int32\_t durationNum)](#createlongpressgesture) | 

Creates a long press gesture.

1\. This API is used to trigger a long press gesture, which requires one or more fingers with a minimum 500 ms hold-down time.

2\. In components that support drag actions by default, such as **Text**, **TextInput**, **TextArea**, **HyperLink**, **Image**, and **RichEditor**,

the long press gesture may conflict with the drag action. If this occurs, the event priority is determined as follows:

If the minimum duration of the long press gesture is less than 500 ms, the long press gesture receives a higher response priority than the drag action.

If the minimum duration of the long press gesture is greater than or equal to 500 ms, the drag action receives a higher response priority than the long press gesture.

3\. If a finger moves more than 15 px after being pressed, the gesture recognition fails.

 |
| [ArkUI\_GestureRecognizer\* (\*createPanGesture)(int32\_t fingersNum, ArkUI\_GestureDirectionMask directions, double distanceNum)](#createpangesture) | 

Creates a swipe gesture.

1\. This API is used to trigger a pan gesture when the movement distance of a finger on the screen exceeds the minimum value.

2\. If a pan gesture and a tab swipe occur at the same time, set **distanceNum** to **1** so that the gesture can be more easily recognized.

 |
| [ArkUI\_GestureRecognizer\* (\*createPinchGesture)(int32\_t fingersNum, double distanceNum)](#createpinchgesture) | 

Creates a pinch gesture.

1\. This API is used to trigger a pinch gesture, which requires two to five fingers with a minimum pinch distance of pixels specified by **distanceNum**.

2\. While more fingers than the minimum number can be pressed to trigger the gesture, only the first fingers of the minimum number participate in gesture calculation.

 |
| [ArkUI\_GestureRecognizer\* (\*createRotationGesture)(int32\_t fingersNum, double angleNum)](#createrotationgesture) | 

Creates a rotation gesture.

1\. This API is used to trigger a rotation gesture, which requires two to five fingers with a minimum 1-degree rotation angle.

2\. While more fingers than the minimum number can be pressed to trigger the gesture, only the first two fingers participate in gesture calculation.

 |
| [ArkUI\_GestureRecognizer\* (\*createSwipeGesture)(int32\_t fingersNum, ArkUI\_GestureDirectionMask directions, double speedNum)](#createswipegesture) | 

Creates a swipe gesture. This API is used to implement a swipe gesture, which can be recognized when the swipe speed (px/s) is higher than that specified by **speedNum**.

 |
| [ArkUI\_GestureRecognizer\* (\*createGroupGesture)(ArkUI\_GroupGestureMode gestureMode)](#creategroupgesture) | Creates a gesture group. |
| [void (\*dispose)(ArkUI\_GestureRecognizer\* recognizer)](#dispose) | Disposes of a gesture to release resources. |
| [int32\_t (\*addChildGesture)(ArkUI\_GestureRecognizer\* group, ArkUI\_GestureRecognizer\* child)](#addchildgesture) | Adds a gesture to a gesture group. |
| [int32\_t (\*removeChildGesture)(ArkUI\_GestureRecognizer\* group, ArkUI\_GestureRecognizer\* child)](#removechildgesture) | Removes a gesture from a gesture group. |
| [int32\_t (\*setGestureEventTarget)(ArkUI\_GestureRecognizer\* recognizer, ArkUI\_GestureEventActionTypeMask actionTypeMask, void\* extraParams,void (\*targetReceiver)(ArkUI\_GestureEvent\* event, void\* extraParams))](#setgestureeventtarget) | Registers a callback for gestures. |
| [int32\_t (\*addGestureToNode)(ArkUI\_NodeHandle node, ArkUI\_GestureRecognizer\* recognizer, ArkUI\_GesturePriority mode, ArkUI\_GestureMask mask)](#addgesturetonode) | Adds a gesture to a UI component. |
| [int32\_t (\*removeGestureFromNode)(ArkUI\_NodeHandle node, ArkUI\_GestureRecognizer\* recognizer)](#removegesturefromnode) | Removes a gesture from a node. |
| [int32\_t (\*setGestureInterrupterToNode)(ArkUI\_NodeHandle node, ArkUI\_GestureInterruptResult (\*interrupter)(ArkUI\_GestureInterruptInfo\* info))](#setgestureinterruptertonode) | Sets a gesture interruption callback for a node. |
| [ArkUI\_GestureRecognizerType (\*getGestureType)(ArkUI\_GestureRecognizer\* recognizer)](#getgesturetype) | Obtains the type of a gesture. |
| [int32\_t (\*setInnerGestureParallelTo)(ArkUI\_NodeHandle node, void\* userData, ArkUI\_GestureRecognizer\* (\*parallelInnerGesture)(ArkUI\_ParallelInnerGestureEvent\* event))](#setinnergestureparallelto) | Sets the callback function for the parallel internal gesture event. |
| [ArkUI\_GestureRecognizer\* (\*createTapGestureWithDistanceThreshold)(int32\_t countNum, int32\_t fingersNum, double distanceThreshold)](#createtapgesturewithdistancethreshold) | 

Creates a tap gesture that is subject to distance restrictions.

1\. This API is used to trigger a tap gesture with one, two, or more taps.

2\. If multi-tap is configured, the timeout interval between a lift and the next tap is 300 ms.

3\. If the distance between the last tapped position and the current tapped position exceeds 60 vp, gesture recognition fails.

4\. When multiple fingers are configured for a gesture, the recognition fails if the number of fingers touching the screen within 300 ms of the initial touch is less than the required count, or if the number of fingers lifted from the screen within 300 ms of the first finger's being lifted is less than the required count.

5\. When the number of fingers touching the screen exceeds the set value, the gesture can be recognized.

6\. If the finger moves beyond the preset distance limit, gesture recognition fails.

 |

#### Member Function Description

#### \[h2\]createTapGesture()

ArkUI\_GestureRecognizer\* (\*createTapGesture)(int32\_t countNum, int32\_t fingersNum)

**Description**

Creates a tap gesture.

1.  This API is used to trigger a tap gesture with one, two, or more taps.
2.  If multi-tap is configured, the timeout interval between a lift and the next tap is 300 ms.
3.  If the distance between the last tapped position and the current tapped position exceeds 60 vp, gesture recognition fails.
4.  If the value is greater than 1, the tap gesture will fail to be recognized when the required number of fingers is not pressed within 300 milliseconds after the first finger touches down, or when the required number of fingers is not lifted within 300 milliseconds after the first finger is lifted.
5.  When the number of fingers touching the screen exceeds the set value, the gesture can be recognized.

**Parameters**

| Name | Description |
| :-- | :-- |
| int32\_t countNum | Number of consecutive taps. If the value is less than 1 or is not set, the default value **1** is used. |
| int32\_t fingersNum | Number of fingers required to trigger the tap gesture. The value ranges from 1 to 10. If the value is less than 1 or is not set, the default value **1** is used. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ArkUI\_GestureRecognizer](../arkui-gesturerecognizer/document.md)\* | Returns the pointer to the created gesture. |

#### \[h2\]createLongPressGesture()

ArkUI\_GestureRecognizer\* (\*createLongPressGesture)(int32\_t fingersNum, bool repeatResult, int32\_t durationNum)

**Description**

Creates a long press gesture.

1.  This API is used to trigger a long press gesture, which requires one or more fingers with a minimum 500 ms hold-down time.
    
2.  In components that support drag actions by default, such as **Text**, **TextInput**, **TextArea**, **HyperLink**, **Image**, and **RichEditor**,
    
    the long press gesture may conflict with the drag action. If this occurs, the event priority is determined as follows:
    
    If the minimum duration of the long press gesture is less than 500 ms, the long press gesture receives a higher response priority than the drag action.
    
    If the minimum duration of the long press gesture is greater than or equal to 500 ms, the drag action receives a higher response priority than the long press gesture.
    
3.  If a finger moves more than 15 px after being pressed, the gesture recognition fails.
    

**Parameters**

| Name | Description |
| :-- | :-- |
| int32\_t fingersNum | Minimum number of fingers to trigger a long press gesture. The value ranges from 1 to 10. If the value is out of the range, the default value **1** is used. |
| bool repeatResult | 
Whether to continuously trigger the event callback.

The value **true** means to continuously trigger event callbacks, and **false** means the opposite.

 |
| int32\_t durationNum | Minimum hold-down time, in ms. If the value is less than or equal to 0, the default value **500** is used. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ArkUI\_GestureRecognizer](../arkui-gesturerecognizer/document.md)\* | Returns the pointer to the created gesture. |

#### \[h2\]createPanGesture()

ArkUI\_GestureRecognizer\* (\*createPanGesture)(int32\_t fingersNum, ArkUI\_GestureDirectionMask directions, double distanceNum)

**Description**

Creates a swipe gesture.

1.  This API is used to trigger a pan gesture when the movement distance of a finger on the screen exceeds the minimum value.
2.  If a pan gesture and a tab swipe occur at the same time, set **distanceNum** to **1** so that the gesture can be more easily recognized.

**Parameters**

| Name | Description |
| :-- | :-- |
| int32\_t fingersNum | Minimum number of fingers to trigger a pan gesture. The value ranges from 1 to 10. If the value is less than 1 or is not set, the default value **1** is used. |
| [ArkUI\_GestureDirectionMask](../../header-files/native-gesture-h/document.md#variables) directions | Pan direction. The value supports the AND (&) and OR (|) operations. |
| double distanceNum | Minimum pan distance to trigger the gesture, in px. If this parameter is set to a value less than or equal to 0, the default value **5px** is used. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ArkUI\_GestureRecognizer](../arkui-gesturerecognizer/document.md)\* | Pointer to the created gesture. |

#### \[h2\]createPinchGesture()

ArkUI\_GestureRecognizer\* (\*createPinchGesture)(int32\_t fingersNum, double distanceNum)

**Description**

Creates a pinch gesture.

1.  This API is used to trigger a pinch gesture, which requires two to five fingers with a minimum pinch distance of pixels specified by **distanceNum**.
2.  While more fingers than the minimum number can be pressed to trigger the gesture, only the first fingers of the minimum number participate in gesture calculation.

**Parameters**

| Name | Description |
| :-- | :-- |
| int32\_t fingersNum | Minimum number of fingers required to trigger the pinch gesture. The value ranges from 2 to 5. If the value is out of the range, the default value **2** is used. |
| double distanceNum | Minimum recognition distance, in px. If this parameter is set to a value less than or equal to 0, the default value **5px** is used. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ArkUI\_GestureRecognizer](../arkui-gesturerecognizer/document.md)\* | Returns the pointer to the created gesture. |

#### \[h2\]createRotationGesture()

ArkUI\_GestureRecognizer\* (\*createRotationGesture)(int32\_t fingersNum, double angleNum)

**Description**

Creates a rotation gesture.

1.  This API is used to trigger a rotation gesture, which requires two to five fingers with a minimum 1-degree rotation angle.
2.  While more fingers than the minimum number can be pressed to trigger the gesture, only the first two fingers participate in gesture calculation.

**Parameters**

| Name | Description |
| :-- | :-- |
| int32\_t fingersNum | Minimum number of fingers required to trigger the rotation gesture. The value ranges from 2 to 5. If the value is out of the range, the default value **2** is used. |
| double angleNum | Minimum angle change required to trigger the rotation gesture, in degrees (deg). The default value is **1**. If this parameter is set to a value less than or equal to 0 or greater than 360, the default value **1** is used. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ArkUI\_GestureRecognizer](../arkui-gesturerecognizer/document.md)\* | Returns the pointer to the created gesture. |

#### \[h2\]createSwipeGesture()

ArkUI\_GestureRecognizer\* (\*createSwipeGesture)(int32\_t fingersNum, ArkUI\_GestureDirectionMask directions, double speedNum)

**Description**

Creates a swipe gesture.

This API is used to implement a swipe gesture, which can be recognized when the swipe speed (px/s) is higher than that specified by **speedNum**.

**Parameters**

| Name | Description |
| :-- | :-- |
| int32\_t fingersNum | Minimum number of fingers required to trigger the swipe gesture. The value ranges from 1 to 10. |
| [ArkUI\_GestureDirectionMask](../../header-files/native-gesture-h/document.md#variables) directions | Directions in which the swipe gesture can be recognized. |
| double speedNum | Minimum speed required to recognize the swipe gesture, in px/s. If this parameter is set to a value less than or equal to 0, the default value **100px/s** is used. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ArkUI\_GestureRecognizer](../arkui-gesturerecognizer/document.md)\* | Returns the pointer to the created gesture. |

#### \[h2\]createGroupGesture()

ArkUI\_GestureRecognizer\* (\*createGroupGesture)(ArkUI\_GroupGestureMode gestureMode)

**Description**

Creates a gesture group.

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_GroupGestureMode](../../header-files/native-gesture-h/document.md#arkui_groupgesturemode) gestureMode | Gesture group mode. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ArkUI\_GestureRecognizer](../arkui-gesturerecognizer/document.md)\* | Returns the pointer to the created gesture group. |

#### \[h2\]dispose()

void (\*dispose)(ArkUI\_GestureRecognizer\* recognizer)

**Description**

Disposes of a gesture to release resources.

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_GestureRecognizer](../arkui-gesturerecognizer/document.md)\* recognizer | Pointer to the gesture to be disposed of. |

#### \[h2\]addChildGesture()

int32\_t (\*addChildGesture)(ArkUI\_GestureRecognizer\* group, ArkUI\_GestureRecognizer\* child)

**Description**

Adds a gesture to a gesture group.

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_GestureRecognizer](../arkui-gesturerecognizer/document.md)\* group | Pointer to the target gesture group. |
| [ArkUI\_GestureRecognizer](../arkui-gesturerecognizer/document.md)\* child | Pointer to the target gesture. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Error code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../../header-files/native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../../header-files/native-type-h/document.md#arkui_errorcode) if a parameter error occurs, for example, attempting to add a gesture to an object that is not a gesture group.

 |

#### \[h2\]removeChildGesture()

int32\_t (\*removeChildGesture)(ArkUI\_GestureRecognizer\* group, ArkUI\_GestureRecognizer\* child)

**Description**

Removes a gesture from a gesture group.

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_GestureRecognizer](../arkui-gesturerecognizer/document.md)\* group | Pointer to the target gesture group. |
| [ArkUI\_GestureRecognizer](../arkui-gesturerecognizer/document.md)\* child | Pointer to the target gesture. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Error code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../../header-files/native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../../header-files/native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]setGestureEventTarget()

int32\_t (\*setGestureEventTarget)(ArkUI\_GestureRecognizer\* recognizer, ArkUI\_GestureEventActionTypeMask actionTypeMask, void\* extraParams,void (\*targetReceiver)(ArkUI\_GestureEvent\* event, void\* extraParams))

**Description**

Registers a callback for gestures.

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_GestureRecognizer](../arkui-gesturerecognizer/document.md)\* recognizer | Pointer to a gesture recognizer. |
| [ArkUI\_GestureEventActionTypeMask](../../header-files/native-gesture-h/document.md#variables) actionTypeMask | Gesture event types. Multiple callbacks can be registered at once, with the callback event types distinguished in the callbacks. Example: actionTypeMask = GESTURE\_EVENT\_ACTION\_ACCEPT | GESTURE\_EVENT\_ACTION\_UPDATE; |
| void\* extraParams | Context passed in the **targetReceiver** callback. |
| targetReceiver | Callback to register for processing the gesture event types. **event** indicates the gesture callback data. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Error code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../../header-files/native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../../header-files/native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]addGestureToNode()

int32\_t (\*addGestureToNode)(ArkUI\_NodeHandle node, ArkUI\_GestureRecognizer\* recognizer, ArkUI\_GesturePriority mode, ArkUI\_GestureMask mask)

**Description**

Adds a gesture to a UI component.

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../arkui-node--00020177/document.md) node | Pointer to the ArkUI component node to which you want to add the gesture. |
| [ArkUI\_GestureRecognizer](../arkui-gesturerecognizer/document.md)\* recognizer | Gesture to be added to the UI component. |
| [ArkUI\_GesturePriority](../../header-files/native-gesture-h/document.md#arkui_gesturepriority) mode | Mode of the gesture. |
| [ArkUI\_GestureMask](../../header-files/native-gesture-h/document.md#arkui_gesturemask) mask | Gesture masking mode. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Error code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../../header-files/native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../../header-files/native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]removeGestureFromNode()

int32\_t (\*removeGestureFromNode)(ArkUI\_NodeHandle node, ArkUI\_GestureRecognizer\* recognizer)

**Description**

Removes a gesture from a node.

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../arkui-node--00020177/document.md) node | Pointer to the node from which you want to remove the gesture. |
| [ArkUI\_GestureRecognizer](../arkui-gesturerecognizer/document.md)\* recognizer | Gesture to be removed. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Error code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../../header-files/native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../../header-files/native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]setGestureInterrupterToNode()

int32\_t (\*setGestureInterrupterToNode)(ArkUI\_NodeHandle node, ArkUI\_GestureInterruptResult (\*interrupter)(ArkUI\_GestureInterruptInfo\* info))

**Description**

Sets a gesture interruption callback for a node.

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../arkui-node--00020177/document.md) node | Pointer to the ArkUI node for which you want to set a gesture interruption callback. |
| [ArkUI\_GestureInterruptResult](../../header-files/native-gesture-h/document.md#arkui_gestureinterruptresult) (\*interrupter)([ArkUI\_GestureInterruptInfo](../arkui-gestureinterruptinfo/document.md)\* info) | 
Gesture interruption callback to set. **info** returns the gesture interruption data. If **interrupter** returns **GESTURE\_INTERRUPT\_RESULT\_CONTINUE**, the gesture recognition process continues. If it returns **GESTURE\_INTERRUPT\_RESULT\_REJECT**, the gesture recognition process is paused. If this parameter is set to a null pointer, the callback function is unregistered.

Note: After the event interruption callback is registered, it will be available in subsequent single-gesture processing. That is, even if you use the **setGestureInterrupterToNode** API to reset the gesture interruption callback to undefined or use the [dispose](#dispose) API to dispose of the gesture that is about to be triggered, the callback will still respond when the trigger condition is met. If the object used in the callback has been released before the callback is triggered, you need to protect the object.

 |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Error code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../../header-files/native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../../header-files/native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]getGestureType()

ArkUI\_GestureRecognizerType (\*getGestureType)(ArkUI\_GestureRecognizer\* recognizer)

**Description**

Obtains the type of a gesture.

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_GestureRecognizer](../arkui-gesturerecognizer/document.md)\* recognizer | Pointer to the gesture. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ArkUI\_GestureRecognizerType](../../header-files/native-gesture-h/document.md#arkui_gesturerecognizertype) | Returns the gesture type. |

#### \[h2\]setInnerGestureParallelTo()

int32\_t (\*setInnerGestureParallelTo)(ArkUI\_NodeHandle node, void\* userData, ArkUI\_GestureRecognizer\* (\*parallelInnerGesture)(ArkUI\_ParallelInnerGestureEvent\* event))

**Description**

Sets the callback function for the parallel internal gesture event.

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../arkui-node--00020177/document.md) node | Pointer to the ArkUI node for which you want to set the callback of the parallel internal gesture event. |
| void\* userData | Custom data. |
| parallelInnerGesture | Parallel internal gesture event. **event** returns the data of the parallel internal gesture event. **parallelInnerGesture** returns the pointer to the gesture recognizer that requires parallel recognition. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../../header-files/native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../../header-files/native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]createTapGestureWithDistanceThreshold()

ArkUI\_GestureRecognizer\* (\*createTapGestureWithDistanceThreshold)(int32\_t countNum, int32\_t fingersNum, double distanceThreshold)

**Description**

Creates a tap gesture that is subject to distance restrictions.

1.  This API is used to trigger a tap gesture with one, two, or more taps.
2.  If multi-tap is configured, the timeout interval between a lift and the next tap is 300 ms.
3.  If the distance between the last tapped position and the current tapped position exceeds 60 vp, gesture recognition fails.
4.  If the value is greater than 1, the tap gesture will fail to be recognized when the required number of fingers is not pressed within 300 milliseconds after the first finger touches down, or when the required number of fingers is not lifted within 300 milliseconds after the first finger is lifted.
5.  When the number of fingers touching the screen exceeds the set value, the gesture can be recognized.
6.  If the finger moves beyond the preset distance limit, gesture recognition fails.

**Parameters**

| Name | Description |
| :-- | :-- |
| int32\_t countNum | Number of consecutive taps. If the value is less than 1 or is not set, the default value **1** is used. |
| int32\_t fingersNum | Number of fingers required to trigger the tap gesture. The value ranges from 1 to 10. If the value is less than 1 or is not set, the default value **1** is used. |
| double distanceThreshold | Allowed moving distance of a finger. If the value is less than 0 or is not set, it will be converted to the default value of infinity. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ArkUI\_GestureRecognizer](../arkui-gesturerecognizer/document.md)\* | Returns the pointer to the created gesture. |
