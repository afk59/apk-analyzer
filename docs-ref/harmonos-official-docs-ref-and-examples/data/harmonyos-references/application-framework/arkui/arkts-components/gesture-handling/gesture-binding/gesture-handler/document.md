# Gesture Handler

You can set the gestures that are bound to a component. You can use the [UIGestureEvent](../bound-gesture-configuration/document.md#uigestureevent) object to add or remove gestures.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/kICnaBrGSBmoWITMU_0weQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062237Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0F0D6D41EECE7AC52D3BFDF560AF99D0397D28CD7818C405BE832F3F41EED84C)

The initial APIs of this module are supported since API version 12. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### GestureHandler<T>

Represents the base type for gesture handlers.

#### \[h2\]tag

tag(tag: string): T

Sets the tag for the gesture handler.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| tag | string | Yes | Gesture handler tag. |

**Return values**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### \[h2\]allowedTypes14+

allowedTypes(types: Array<SourceTool>): T

Sets the event input sources supported by the gesture handler.

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| types | Array<[SourceTool](../gesture-binding/document.md#sourcetool9)\> | Yes | Supported input source types. |

**Return values**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### BaseHandlerOptions15+

Provides the parameters of the basic gesture handler.

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| isFingerCountLimited | boolean | No | Yes | 
Whether to enforce the exact number of fingers touching the screen. **true**: Enforce the exact number of fingers touching the screen. **false**: Do not enforce the exact number of fingers touching the screen.

Default value: **false**

 |

#### TapGestureHandler

Defines a type of gesture handler object for tap gestures.

#### \[h2\]constructor

constructor(options?: TapGestureHandlerOptions)

Constructor used to create a tap gesture handler instance.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [TapGestureHandlerOptions](#tapgesturehandleroptions) | No | Parameters of the tap gesture handler. |

#### \[h2\]onAction

onAction(event: Callback<GestureEvent>): TapGestureHandler

Sets the callback for successful tap gesture recognition.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | [Callback](../../../common-definitions/basic-types/document.md#callback12)<[GestureEvent](../../gesture-common-apis/document.md#gestureevent)\> | Yes | Callback invoked upon successful tap gesture recognition. |

**Return values**

| Type | Description |
| :-- | :-- |
| [TapGestureHandler](#tapgesturehandler) | Tap gesture handler object. |

#### TapGestureHandlerOptions

Provides the parameters of the tap gesture handler. Inherits from [BaseHandlerOptions](#basehandleroptions15).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| count | number | No | Yes | 
Number of consecutive taps. If the value is less than 1 or is not set, the default value is used.

Default value: **1**

Value range: \[0, +∞)

**NOTE**

1\. If multi-tap is configured, the timeout interval between a lift and the next tap is 300 ms.

2\. If the distance between the last tapped position and the current tapped position exceeds 60 vp, gesture recognition fails.

 |
| fingers | number | No | Yes | 

Number of fingers required to trigger a tap. The value ranges from 1 to 10. If the value is less than 1 or is not set, the default value is used.

Default value: **1**

**NOTE**

1\. If the value is greater than 1, the tap gesture will fail to be recognized when the required number of fingers is not pressed within 300 milliseconds after the first finger touches down, or when the required number of fingers is not lifted within 300 milliseconds after the first finger is lifted.

2\. When the number of fingers touching the screen exceeds the set value, the gesture can be recognized.

 |
| isFingerCountLimited15+ | boolean | No | Yes | 

Whether to enforce the exact number of fingers touching the screen. **true**: Enforce the exact number of fingers touching the screen. **false**: Do not enforce the exact number of fingers touching the screen. With the value **true**, the gesture recognition fails if the number of fingers touching the screen does not match the configured value of **fingers**.

In multi-tap events (where the **count** parameter is greater than 1), each tap must have the same number of fingers as the configured value; otherwise, the gesture recognition fails.

Default value: **false**

**Atomic service API**: This API can be used in atomic services since API version 15.

 |

#### LongPressGestureHandler

Defines a long press gesture handler object.

#### \[h2\]constructor

constructor(options?: LongPressGestureHandlerOptions)

Constructor used to create a long press gesture handler instance.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [LongPressGestureHandlerOptions](#longpressgesturehandleroptions) | No | Parameters of the long press gesture handler. |

#### \[h2\]onAction

onAction(event: Callback<GestureEvent>): LongPressGestureHandler

Sets the callback for successful long press gesture recognition.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | [Callback](../../../common-definitions/basic-types/document.md#callback12)<[GestureEvent](../../gesture-common-apis/document.md#gestureevent)\> | Yes | Callback invoked upon successful long press gesture recognition. |

**Return values**

| Type | Description |
| :-- | :-- |
| [LongPressGestureHandler](#longpressgesturehandler) | Long press gesture handler object. |

#### \[h2\]onActionEnd

onActionEnd(event: Callback<GestureEvent>): LongPressGestureHandler

Sets the callback for long press gesture recognition completion. This callback is triggered when all fingers are lifted after successful recognition.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | [Callback](../../../common-definitions/basic-types/document.md#callback12)<[GestureEvent](../../gesture-common-apis/document.md#gestureevent)\> | Yes | Callback invoked when long press gesture recognition completes. |

**Return values**

| Type | Description |
| :-- | :-- |
| [LongPressGestureHandler](#longpressgesturehandler) | Long press gesture handler object. |

#### \[h2\]onActionCancel

onActionCancel(event: Callback<void>): LongPressGestureHandler

Sets the callback for long press gesture cancellation. This callback is triggered when a touch cancellation event occurs after successful recognition. No gesture event information is returned.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | [Callback](../../../common-definitions/basic-types/document.md#callback12)<void> | Yes | Callback invoked when the long press gesture is cancelled. |

**Return values**

| Type | Description |
| :-- | :-- |
| [LongPressGestureHandler](#longpressgesturehandler) | Long press gesture handler object. |

#### \[h2\]onActionCancel18+

onActionCancel(event: Callback<GestureEvent>): LongPressGestureHandler

Sets the callback for long press gesture cancellation. This callback is triggered when a touch cancellation event occurs after successful recognition. Compared with [onActionCancel](#onactioncancel), this API returns gesture event information.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | [Callback](../../../common-definitions/basic-types/document.md#callback12)<[GestureEvent](../../gesture-common-apis/document.md#gestureevent)\> | Yes | Callback invoked when the long press gesture is cancelled. This callback returns gesture event information. |

**Return values**

| Type | Description |
| :-- | :-- |
| [LongPressGestureHandler](#longpressgesturehandler) | Long press gesture handler object. |

#### LongPressGestureHandlerOptions

Provides the parameters of the long press gesture handler. Inherits from [BaseHandlerOptions](#basehandleroptions15).

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| fingers | number | No | Yes | 
Minimum number of fingers to trigger a long press gesture. The value ranges from 1 to 10.

Default value: **1**

Value range: \[1, 10\]

**NOTE**

If a finger moves more than 15 px after being pressed, the gesture recognition fails.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| repeat | boolean | No | Yes | 

Whether to continuously trigger the event callback. The value **true** means to continuously trigger the event callback, and **false** means the opposite.

Default value: **false**

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| duration | number | No | Yes | 

Minimum hold-down time, in ms.

Default value: **500**

**NOTE**

Value range: \[0, +∞)

If the value is less than or equal to 0, the default value **500** is used.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| isFingerCountLimited15+ | boolean | No | Yes | 

Whether to enforce the exact number of fingers touching the screen. **true**: Enforce the exact number of fingers touching the screen. **false**: Do not enforce the exact number of fingers touching the screen. With the value **true**, the gesture recognition fails if the number of fingers touching the screen does not match the configured value of **fingers**.

For gestures that have already been successfully recognized, changes in the number of fingers touching the screen will not trigger the **repeat** event. However, if the number of fingers touching the screen returns to the configured minimum number, the [onAction](../../basic-gestures/longpressgesture/document.md#onaction) event can be triggered. The [onActionEnd](../../basic-gestures/longpressgesture/document.md#onactionend) event can also be triggered regardless of the finger count.

Default value: **false**

**Atomic service API**: This API can be used in atomic services since API version 15.

 |
| allowableMovement22+ | number | No | Yes | 

Maximum movement distance recognized by the long press gesture recognizer, in px.

Default value: **15**

Value range: (0, +∞). If the value is less than or equal to 0, the default value **15** is used.

**Atomic service API**: This API can be used in atomic services since API version 22.

 |

#### PanGestureHandler

Defines a pan gesture handler object.

#### \[h2\]constructor

constructor(options?: PanGestureHandlerOptions)

Constructor used to create a pan gesture handler instance.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [PanGestureHandlerOptions](#pangesturehandleroptions) | No | Parameters of the pan gesture handler. |

#### \[h2\]onActionStart

onActionStart(event: Callback<GestureEvent>): PanGestureHandler

Sets the callback for successful pan gesture recognition.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | [Callback](../../../common-definitions/basic-types/document.md#callback12)<[GestureEvent](../../gesture-common-apis/document.md#gestureevent)\> | Yes | Callback invoked upon successful pan gesture recognition. |

**Return values**

| Type | Description |
| :-- | :-- |
| [PanGestureHandler](#pangesturehandler) | Pan gesture handler object. |

#### \[h2\]onActionUpdate

onActionUpdate(event: Callback<GestureEvent>): PanGestureHandler

Sets the callback for pan gesture movement updates. The callback is triggered when the pan gesture moves.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | [Callback](../../../common-definitions/basic-types/document.md#callback12)<[GestureEvent](../../gesture-common-apis/document.md#gestureevent)\> | Yes | 
Callback invoked during pan gesture movement.

If **fingerList** contains multiple fingers, this callback updates the location information of only one finger each time.

 |

**Return values**

| Type | Description |
| :-- | :-- |
| [PanGestureHandler](#pangesturehandler) | Pan gesture handler object. |

#### \[h2\]onActionEnd

onActionEnd(event: Callback<GestureEvent>): PanGestureHandler

Sets the callback for pan gesture recognition completion. This callback is triggered when all fingers are lifted after successful recognition.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | [Callback](../../../common-definitions/basic-types/document.md#callback12)<[GestureEvent](../../gesture-common-apis/document.md#gestureevent)\> | Yes | Callback invoked when pan gesture recognition completes. |

**Return values**

| Type | Description |
| :-- | :-- |
| [PanGestureHandler](#pangesturehandler) | Pan gesture handler object. |

#### \[h2\]onActionCancel

onActionCancel(event: Callback<void>): PanGestureHandler

Sets the callback for pan gesture cancellation. This callback is triggered when a touch cancellation event occurs after successful recognition. No gesture event information is returned.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | [Callback](../../../common-definitions/basic-types/document.md#callback12)<void> | Yes | Callback invoked when the pan gesture is cancelled. |

**Return values**

| Type | Description |
| :-- | :-- |
| [PanGestureHandler](#pangesturehandler) | Pan gesture handler object. |

#### \[h2\]onActionCancel18+

onActionCancel(event: Callback<GestureEvent>): PanGestureHandler

Sets the callback for pan gesture cancellation. This callback is triggered when a touch cancellation event occurs after successful recognition. Compared with [onActionCancel](#onactioncancel-1), this API returns gesture event information.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | [Callback](../../../common-definitions/basic-types/document.md#callback12)<[GestureEvent](../../gesture-common-apis/document.md#gestureevent)\> | Yes | Callback invoked when the pan gesture is cancelled. Gesture event information is returned. |

**Return values**

| Type | Description |
| :-- | :-- |
| [PanGestureHandler](#pangesturehandler) | Pan gesture handler object. |

#### PanGestureHandlerOptions

Provides the parameters of the pan gesture handler. Inherits from [BaseHandlerOptions](#basehandleroptions15).

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| fingers | number | No | Yes | 
Minimum number of fingers to trigger a pan gesture. The value ranges from 1 to 10.

Default value: **1**

Value range: \[1, 10\]

**NOTE**

If the value is less than 1 or is not set, the default value is used.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| direction | [PanDirection](../../basic-gestures/pangesture/document.md#pandirection) | No | Yes | 

Pan direction. The value supports the AND (&) and OR (|) operations.

Default value: **PanDirection.All**

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| distance | number | No | Yes | 

Minimum pan distance to trigger the gesture, in vp.

Default value: **8** for the stylus and **5** for other input sources

**NOTE**

If a pan gesture and a [tab](../../../navigation-and-switching/tabs/document.md) swipe occur at the same time, set **distance** to **1** to make the gesture more easily recognizable.

Value range: \[0, +∞)

If the value specified is less than 0, the default value is used.

Since API version 19, the default value is **8**, in vp, for the stylus.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| distanceMap19+ | Map<[SourceTool](../gesture-binding/document.md#sourcetool9), number> | No | Yes | 

Minimum pan distance for different input sources to trigger the gesture, in vp.

Default value: **8** for the stylus and **5** for other input sources

Value range: \[0, +∞)

If the value specified is less than 0, the default value is used.

**Atomic service API**: This API can be used in atomic services since API version 19.

 |

#### SwipeGestureHandler

Defines a swipe gesture handler object.

#### \[h2\]constructor

constructor(options?: SwipeGestureHandlerOptions)

Constructor used to create a swipe gesture handler instance.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [SwipeGestureHandlerOptions](#swipegesturehandleroptions) | No | Parameters of the swipe gesture handler. |

#### \[h2\]onAction

onAction(event: Callback<GestureEvent>): SwipeGestureHandler

Sets the callback for successful swipe gesture recognition.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | [Callback](../../../common-definitions/basic-types/document.md#callback12)<[GestureEvent](../../gesture-common-apis/document.md#gestureevent)\> | Yes | Callback invoked upon successful swipe gesture recognition. |

**Return values**

| Type | Description |
| :-- | :-- |
| [SwipeGestureHandler](#swipegesturehandler) | Swipe gesture handler object. |

#### SwipeGestureHandlerOptions

Provides the parameters of the swipe gesture handler. Inherits from [BaseHandlerOptions](#basehandleroptions15).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| fingers | number | No | Yes | 
Minimum number of fingers to trigger a swipe gesture. The value ranges from 1 to 10.

Default value: **1**

Value range: \[1, 10\]

 |
| direction | [SwipeDirection](../../basic-gestures/swipegesture/document.md#swipedirection) | No | Yes | 

Directions in which the swipe gesture can be recognized.

Default value: **SwipeDirection.All**

 |
| speed | number | No | Yes | 

Minimum speed of the swipe gesture.

Default value: 100 vp/s

**NOTE**

If the value is less than or equal to 0, it will be converted to the default value.

 |
| isFingerCountLimited15+ | boolean | No | Yes | 

Whether to enforce the exact number of fingers touching the screen. **true**: Enforce the exact number of fingers touching the screen. **false**: Do not enforce the exact number of fingers touching the screen. With the value **true**, the gesture recognition fails if the number of fingers touching the screen does not match the configured value of **fingers**.

Default value: **false**

**Atomic service API**: This API can be used in atomic services since API version 15.

 |

#### PinchGestureHandler

Defines a type of gesture handler object for pinch gestures.

#### \[h2\]constructor

constructor(options?: PinchGestureHandlerOptions)

Constructor used to create a pinch gesture handler instance.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [PinchGestureHandlerOptions](#pinchgesturehandleroptions) | No | Parameters of the pinch gesture handler. |

#### \[h2\]onActionStart

onActionStart(event: Callback<GestureEvent>): PinchGestureHandler

Sets the callback for successful pinch gesture recognition.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | [Callback](../../../common-definitions/basic-types/document.md#callback12)<[GestureEvent](../../gesture-common-apis/document.md#gestureevent)\> | Yes | Callback invoked upon successful pinch gesture recognition. |

**Return values**

| Type | Description |
| :-- | :-- |
| [PinchGestureHandler](#pinchgesturehandler) | Pinch gesture handler object. |

#### \[h2\]onActionUpdate

onActionUpdate(event: Callback<GestureEvent>): PinchGestureHandler

Sets the callback for pinch gesture movement updates. The callback is triggered when the pinch gesture moves.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | [Callback](../../../common-definitions/basic-types/document.md#callback12)<[GestureEvent](../../gesture-common-apis/document.md#gestureevent)\> | Yes | Callback invoked during pinch gesture movement. |

**Return values**

| Type | Description |
| :-- | :-- |
| [PinchGestureHandler](#pinchgesturehandler) | Pinch gesture handler object. |

#### \[h2\]onActionEnd

onActionEnd(event: Callback<GestureEvent>): PinchGestureHandler

Sets the callback for pinch gesture recognition completion. This callback is triggered when all fingers are lifted after successful recognition.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | [Callback](../../../common-definitions/basic-types/document.md#callback12)<[GestureEvent](../../gesture-common-apis/document.md#gestureevent)\> | Yes | Callback invoked when pinch gesture recognition completes. |

**Return values**

| Type | Description |
| :-- | :-- |
| [PinchGestureHandler](#pinchgesturehandler) | Pinch gesture handler object. |

#### \[h2\]onActionCancel

onActionCancel(event: Callback<void>): PinchGestureHandler

Sets the callback for pinch gesture cancellation. This callback is triggered when a touch cancellation event occurs after successful recognition. No gesture event information is returned.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | [Callback](../../../common-definitions/basic-types/document.md#callback12)<void> | Yes | Callback invoked when the pinch gesture is cancelled. No gesture event information is returned. |

**Return values**

| Type | Description |
| :-- | :-- |
| [PinchGestureHandler](#pinchgesturehandler) | Pinch gesture handler object. |

#### \[h2\]onActionCancel18+

onActionCancel(event: Callback<GestureEvent>): PinchGestureHandler

Sets the callback for pinch gesture cancellation. This callback is triggered when a touch cancellation event occurs after successful recognition. Compared with [onActionCancel](#onactioncancel-2), this API returns gesture event information.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | [Callback](../../../common-definitions/basic-types/document.md#callback12)<[GestureEvent](../../gesture-common-apis/document.md#gestureevent)\> | Yes | Callback invoked when the pinch gesture is cancelled. Gesture event information is returned. |

**Return values**

| Type | Description |
| :-- | :-- |
| [PinchGestureHandler](#pinchgesturehandler) | Pinch gesture handler object. |

#### PinchGestureHandlerOptions

Provides the parameters of the pinch gesture handler. Inherits from [BaseHandlerOptions](#basehandleroptions15).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| fingers | number | No | Yes | 
Minimum number of fingers to trigger a pinch. The value ranges from 2 to 5.

Default value: **2**

Value range: \[2, 5\]

While more fingers than the minimum number can be pressed to trigger the gesture, only the first fingers of the minimum number participate in gesture calculation.

 |
| distance | number | No | Yes | 

Minimum recognition distance, in vp.

Default value: **5**

**NOTE**

If the value is less than or equal to 0, it will be converted to the default value.

 |
| isFingerCountLimited15+ | boolean | No | Yes | 

Whether to enforce the exact number of fingers touching the screen. **true**: Enforce the exact number of fingers touching the screen. **false**: Do not enforce the exact number of fingers touching the screen. With the value **true**, the gesture recognition fails if the number of fingers touching the screen does not match the configured value of **fingers**. The gesture can only be successfully recognized if the number of fingers equals the configured minimum and the swipe distance meets the threshold. Note that only the first two fingers that touch the screen are considered for the gesture. If one of these fingers is lifted, the gesture recognition fails. For gestures that have already been successfully recognized, changing the number of fingers touching the screen will not trigger the [onActionUpdate](../../basic-gestures/pinchgesture/document.md#onactionupdate) event, but the [onActionEnd](../../basic-gestures/pinchgesture/document.md#onactionend) event can still be triggered.

Default value: **false**

**Atomic service API**: This API can be used in atomic services since API version 15.

 |

#### RotationGestureHandler

Defines a rotation gesture handler object.

#### \[h2\]constructor

constructor(options?: RotationGestureHandlerOptions)

Constructor used to create a rotation gesture handler instance.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [RotationGestureHandlerOptions](#rotationgesturehandleroptions) | No | Parameters of the rotation gesture handler. |

#### \[h2\]onActionStart

onActionStart(event: Callback<GestureEvent>): RotationGestureHandler

Sets the callback for successful rotation gesture recognition.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | [Callback](../../../common-definitions/basic-types/document.md#callback12)<[GestureEvent](../../gesture-common-apis/document.md#gestureevent)\> | Yes | Callback invoked upon successful rotation gesture recognition. |

**Return values**

| Type | Description |
| :-- | :-- |
| [RotationGestureHandler](#rotationgesturehandler) | Rotation gesture handler object. |

#### \[h2\]onActionUpdate

onActionUpdate(event: Callback<GestureEvent>): RotationGestureHandler

Sets the callback for rotation gesture movement updates. The callback is triggered when the rotation gesture moves.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | [Callback](../../../common-definitions/basic-types/document.md#callback12)<[GestureEvent](../../gesture-common-apis/document.md#gestureevent)\> | Yes | Callback invoked during rotation gesture movement. |

**Return values**

| Type | Description |
| :-- | :-- |
| [RotationGestureHandler](#rotationgesturehandler) | Rotation gesture handler object. |

#### \[h2\]onActionEnd

onActionEnd(event: Callback<GestureEvent>): RotationGestureHandler

Sets the callback for rotation gesture recognition completion. This callback is triggered when all fingers are lifted after successful recognition.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | [Callback](../../../common-definitions/basic-types/document.md#callback12)<[GestureEvent](../../gesture-common-apis/document.md#gestureevent)\> | Yes | Callback invoked when rotation gesture recognition completes. |

**Return values**

| Type | Description |
| :-- | :-- |
| [RotationGestureHandler](#rotationgesturehandler) | Rotation gesture handler object. |

#### \[h2\]onActionCancel

onActionCancel(event: Callback<void>): RotationGestureHandler

Sets the callback for rotation gesture cancellation. This callback is triggered when a touch cancellation event occurs after successful recognition. No gesture event information is returned.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | [Callback](../../../common-definitions/basic-types/document.md#callback12)<void> | Yes | Callback invoked when the rotation gesture is cancelled. No gesture event information is returned. |

**Return values**

| Type | Description |
| :-- | :-- |
| [RotationGestureHandler](#rotationgesturehandler) | Rotation gesture handler object. |

#### \[h2\]onActionCancel18+

onActionCancel(event: Callback<GestureEvent>): RotationGestureHandler

Sets the callback for rotation gesture cancellation. This callback is triggered when a touch cancellation event occurs after successful recognition. Compared with [onActionCancel](#onactioncancel-3), this API returns gesture event information.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | [Callback](../../../common-definitions/basic-types/document.md#callback12)<[GestureEvent](../../gesture-common-apis/document.md#gestureevent)\> | Yes | Callback invoked when the rotation gesture is cancelled. Gesture event information is returned. |

**Return values**

| Type | Description |
| :-- | :-- |
| [RotationGestureHandler](#rotationgesturehandler) | Rotation gesture handler object. |

#### RotationGestureHandlerOptions

Provides the parameters of the rotation gesture handler. Inherits from [BaseHandlerOptions](#basehandleroptions15).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| fingers | number | No | Yes | 
Minimum number of fingers to trigger a rotation. The value ranges from 2 to 5.

Default value: **2**

Value range: \[2, 5\]

While more fingers than the minimum number can be pressed to trigger the gesture, only the first two fingers participate in gesture calculation.

 |
| angle | number | No | Yes | 

Minimum angle change required to trigger the rotation gesture, in degrees (deg).

Default value: **1**

**NOTE**

If the value is less than or equal to 0 or greater than 360, it will be converted to the default value.

 |
| isFingerCountLimited15+ | boolean | No | Yes | 

Whether to enforce the exact number of fingers touching the screen. **true**: Enforce the exact number of fingers touching the screen. **false**: Do not enforce the exact number of fingers touching the screen. With the value **true**, the gesture recognition fails if the number of fingers touching the screen does not match the configured value of **fingers**. The gesture can only be successfully recognized if the number of fingers equals the configured minimum and the swipe distance meets the threshold. Note that only the first two fingers that touch the screen are considered for the gesture. If one of these fingers is lifted, the gesture recognition fails.

For gestures that have already been successfully recognized, changing the number of fingers touching the screen will not trigger the [onActionUpdate](../../basic-gestures/rotationgesture/document.md#onactionupdate) event, but the [onActionEnd](../../basic-gestures/rotationgesture/document.md#onactionend) event can still be triggered.

Default value: **false**

**Atomic service API**: This API can be used in atomic services since API version 15.

 |

#### GestureGroupHandler

Defines a gesture group handler object.

#### \[h2\]constructor

constructor(options?: GestureGroupGestureHandlerOptions)

Constructor used to create a gesture group handler instance.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [GestureGroupGestureHandlerOptions](#gesturegroupgesturehandleroptions) | No | Parameters of the gesture group handler. |

#### \[h2\]onCancel

onCancel(event: Callback<void>): GestureGroupHandler

Sets the cancellation callback for the gesture group handler. The callback is triggered when a sequence gesture ([GestureMode](../../combined-gestures/document.md#gesturemode).Sequence) is cancelled.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | [Callback](../../../common-definitions/basic-types/document.md#callback12)<void> | Yes | Callback invoked when the gesture group is cancelled. |

**Return values**

| Type | Description |
| :-- | :-- |
| [GestureGroupHandler](#gesturegrouphandler) | Current gesture group handler object. |

#### GestureGroupGestureHandlerOptions

Provides the parameters of the gesture group handler.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| mode | [GestureMode](../../combined-gestures/document.md#gesturemode) | No | No | 
Recognition mode of [combined gestures](../../combined-gestures/document.md).

Default value: **GestureMode.Sequence**

 |
| gestures | [GestureHandler](#gesturehandlert)<[TapGestureHandler](#tapgesturehandler) | [LongPressGestureHandler](#longpressgesturehandler) | [PanGestureHandler](#pangesturehandler) | [SwipeGestureHandler](#swipegesturehandler) | [PinchGestureHandler](#pinchgesturehandler) | [RotationGestureHandler](#rotationgesturehandler) | [GestureGroupHandler](#gesturegrouphandler)\>\[\] | No | No | 

Gesture group.

**NOTE**

To add both single-tap and double-tap gestures for a component, add two [TapGesture](../../basic-gestures/tapgesture/document.md) instances as the [combined gestures](../../combined-gestures/document.md), with the double-tap gesture preceding the single-tap gesture. The gestures will not work correctly if this order is reversed.

 |

#### GesturePriority

Enumerates gesture priority levels.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| NORMAL | 0 | Normal priority. |
| PRIORITY | 1 | High priority. |
