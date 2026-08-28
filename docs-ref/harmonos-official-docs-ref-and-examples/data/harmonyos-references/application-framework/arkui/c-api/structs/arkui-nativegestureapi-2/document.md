# ArkUI\_NativeGestureAPI\_2

typedef struct {...} ArkUI\_NativeGestureAPI\_2

#### Overview

Defines a collection of gesture APIs.

**Since**: 18

**Related module**: [ArkUI\_NativeModule](../../modules/arkui-nativemodule/document.md)

**Header file**: [native\_gesture.h](../../header-files/native-gesture-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| [ArkUI\_NativeGestureAPI\_1](../arkui-nativegestureapi-1/document.md)\* gestureApi1 | Pointer to the **ArkUI\_NativeGestureAPI\_1** struct. |

#### \[h2\]Member Functions

| Name | Description |
| :-- | :-- |
| [int32\_t (\*setGestureInterrupterToNode)(ArkUI\_NodeHandle node, void\* userData,ArkUI\_GestureInterruptResult (\*interrupter)(ArkUI\_GestureInterruptInfo\* info))](#setgestureinterruptertonode) | Sets the callback for gesture interruption events. |

#### Member Function Description

#### \[h2\]setGestureInterrupterToNode()

int32\_t (\*setGestureInterrupterToNode)(ArkUI\_NodeHandle node, void\* userData, ArkUI\_GestureInterruptResult (\*interrupter)(ArkUI\_GestureInterruptInfo\* info))

**Description**

Sets the callback for gesture interruption events.

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../arkui-node--00020177/document.md) node | Pointer to the ArkUI node for which you want to set a gesture interruption callback. |
| void\* userData | Pointer to user-defined data. |
| [ArkUI\_GestureInterruptResult](../../header-files/native-gesture-h/document.md#arkui_gestureinterruptresult) (\*interrupter)([ArkUI\_GestureInterruptInfo](../arkui-gestureinterruptinfo/document.md)\* info) | 
Gesture interruption callback to set. **info** returns the gesture interruption data. If **interrupter** returns **GESTURE\_INTERRUPT\_RESULT\_CONTINUE**, the gesture recognition process continues. If it returns **GESTURE\_INTERRUPT\_RESULT\_REJECT**, the gesture recognition process is paused. If this parameter is set to a null pointer, the callback function is unregistered.

Note: After the event interruption callback is registered, it will be available in subsequent single-gesture processing. That is, even if you use the **setGestureInterrupterToNode** API to reset the gesture interruption callback to undefined or use the [dispose](../arkui-nativegestureapi-1/document.md#dispose) API to dispose of the gesture that is about to be triggered, the callback will still respond when the trigger condition is met. If the object used in the callback has been released before the callback is triggered, you need to protect the object.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Error code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../../header-files/native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../../header-files/native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |
