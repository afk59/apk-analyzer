# Gesture Common APIs

Provides common APIs related to gestures.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/KzvZFf-RStSWKUmnVeDzfA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062237Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=091CA6777C5FAE1401C599C5C0991B46B6BCC66EB6605364CE08A83EFDFC8837)

The initial APIs of this module are supported since API version 7. Updates will be marked with a superscript to indicate their earliest API version.

#### GestureInterface<T>11+

Defines the gesture API.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### \[h2\]tag11+

tag(tag: string): T

Sets a gesture tag.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| tag | string | Yes | Gesture tag. |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### \[h2\]allowedTypes14+

allowedTypes(types: Array<SourceTool>): T

Sets the input types that can trigger the gesture response.

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| types | Array<[SourceTool](../gesture-binding/gesture-binding/document.md#sourcetool9)\> | Yes | Input types that can trigger the gesture response. |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### ScrollableTargetInfo12+

Provides the information about the scrollable container component corresponding to the gesture recognizer. It inherits from [EventTargetInfo](#eventtargetinfo12).

#### \[h2\]isBegin12+

isBegin(): boolean

Checks whether this scrollable container component is scrolled to the top. If it is a **Swiper** component in loop mode, **false** is returned.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Whether the current scrollable container component is scrolled to the top. The value **true** means that the component is scrolled to the top, and **false** means the opposite. |

#### \[h2\]isEnd12+

isEnd(): boolean

Checks whether the current scroll container is scrolled to the bottom. If the container is a **Swiper** component and is in loop mode, **false** is returned.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Whether the current scrollable container component is scrolled to the bottom. The value **true** means that the component is scrolled to the bottom, and **false** means the opposite. |

#### EventTargetInfo12+

Provides the information about the component corresponding to the gesture recognizer.

#### \[h2\]getId12+

getId(): string

Obtains the ID of this component.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| string | [ID](../../universal-attributes/basic-attributes/component-id/document.md#id) of the current component. |

#### TouchRecognizer20+

Represents a touch gesture recognizer.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### \[h2\]getEventTargetInfo20+

getEventTargetInfo(): EventTargetInfo

Obtains the information about the component corresponding to this touch gesture recognizer.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| [EventTargetInfo](#eventtargetinfo12) | Information about the component corresponding to the current touch gesture recognizer. |

#### \[h2\]cancelTouch20+

cancelTouch(): void

Sends a touch cancellation event to this touch gesture recognizer.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### GestureRecognizer12+

Gesture recognizer object.

#### \[h2\]getTag12+

getTag(): string

Obtains the tag of this gesture recognizer.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| string | Tag of the current gesture recognizer. |

#### \[h2\]getType12+

getType(): GestureControl.GestureType

Obtains the type of this gesture recognizer.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| [GestureControl.GestureType](#gesturetype11) | Type of the current gesture recognizer. |

#### \[h2\]isBuiltIn12+

isBuiltIn(): boolean

Obtains whether this gesture recognizer is a built-in gesture.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Whether the current gesture recognizer is a built-in gesture. The value **true** means that the gesture recognizer is a built-in gesture, and **false** means the opposite. |

#### \[h2\]setEnabled12+

setEnabled(isEnabled: boolean): void

Sets the enabled state of this gesture recognizer.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| isEnabled | boolean | Yes | Enabled state to set. The value **true** means that the gesture recognizer is enabled and will trigger events, and **false** means the opposite. |

#### \[h2\]isEnabled12+

isEnabled(): boolean

Obtains the enabled state of this gesture recognizer.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Enabled state of the gesture recognizer. The value **true** means that the gesture recognizer is enabled and will trigger events, and **false** means the opposite. |

#### \[h2\]getState12+

getState(): GestureRecognizerState

Obtains the state of this gesture recognizer.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| [GestureRecognizerState](#gesturerecognizerstate12) | State of the gesture recognizer. |

#### \[h2\]getEventTargetInfo12+

getEventTargetInfo(): EventTargetInfo

Obtains the information about the component corresponding to this gesture recognizer.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| [EventTargetInfo](#eventtargetinfo12) | Information about the component corresponding to the current gesture recognizer. |

#### \[h2\]isValid12+

isValid(): boolean;

Whether the current gesture recognizer is valid.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | 
Whether the current gesture recognizer is valid.

Returns **false** if the component bound to this recognizer is destroyed or if the recognizer is not on the response chain.

Returns **true** if the bound component exists and the recognizer is in the response chain.

 |

#### \[h2\]getFingerCount18+

getFingerCount(): number

Obtains the number of fingers required to trigger the preset gesture.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| number | 
Number of fingers required to trigger the preset gesture.

Value range: an integer from 1 to 10.

 |

#### \[h2\]isFingerCountLimit18+

isFingerCountLimit(): boolean

Checks whether the preset gesture detects the number of fingers on the screen.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Whether the preset gesture will detect the number of fingers on the screen. **true** if the gesture event is bound and detects the number of fingers; **false** otherwise. |

#### \[h2\]preventBegin20+

preventBegin(): void

Prevents a gesture recognizer from participating in the current gesture recognition before all fingers are lifted. If the system has already determined the result of the gesture recognizer (regardless of success or failure), calling this API will be ineffective. Unlike GestureRecognizer.[setEnabled](#setenabled12)(isEnabled: boolean), which only affects callback execution, this API prevents the recognizer from participating in the recognition process entirely.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### TapRecognizer18+

Implements a tap gesture recognizer object. Inherits from [GestureRecognizer](#gesturerecognizer12).

#### \[h2\]getTapCount18+

getTapCount(): number

Obtains the number of consecutive taps required for the tap gesture to be recognized.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| number | 
Number of consecutive taps required for the tap gesture to be recognized.

Value range: \[0, +∞)

 |

#### LongPressRecognizer18+

Implements a long press gesture recognizer. Inherits from [GestureRecognizer](#gesturerecognizer12).

#### \[h2\]isRepeat18+

isRepeat(): boolean

Checks whether the long press gesture recognizer is set to trigger repeated callbacks.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Whether the long press gesture recognizer is set to trigger repeated callbacks. **false**: Repeated callbacks are not triggered. **true**: Repeated callbacks are triggered. |

#### \[h2\]getDuration18+

getDuration(): number

Obtains the minimum duration required for the long press gesture to be recognized.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| number | 
Minimum duration, in ms.

Value range: \[0, +∞)

 |

#### \[h2\]getAllowableMovement22+

getAllowableMovement(): number

Obtains the maximum movement distance allowed for gesture recognition by the long press gesture recognizer.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| number | 
Maximum movement distance recognized by the long press gesture recognizer, in px.

Value range: (0, +∞)

 |

#### SwipeRecognizer18+

Implements a swipe gesture recognizer. Inherits from [GestureRecognizer](#gesturerecognizer12).

#### \[h2\]getVelocityThreshold18+

getVelocityThreshold(): number

Obtains the minimum velocity required for the swipe gesture to be recognized.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| number | 
Minimum velocity required for the swipe gesture to be recognized, in vp/s.

Value range: \[0, +∞)

 |

#### \[h2\]getDirection18+

getDirection(): SwipeDirection

Obtains the direction for recognizing swipe gestures.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| [SwipeDirection](../basic-gestures/swipegesture/document.md#swipedirection) | Direction for recognizing swipe gestures. |

#### PinchRecognizer18+

Implements a pinch gesture recognizer. Inherits from [GestureRecognizer](#gesturerecognizer12).

#### \[h2\]getDistance18+

getDistance(): number

Obtains the minimum distance required for the pinch gesture to be recognized.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| number | 
Minimum distance required for the pinch gesture to be recognized, in vp.

Value range: \[0, +∞)

 |

#### RotationRecognizer18+

Implements a rotation gesture recognizer. Inherits from [GestureRecognizer](#gesturerecognizer12).

#### \[h2\]getAngle18+

getAngle(): number

Obtains the minimum angle change required for the rotation gesture to be recognized.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| number | 
Minimum angle change required for the rotation gesture to be recognized, in degrees (deg).

Value range: \[0, +∞)

**NOTE**

If the provided angle is less than or equal to 0 or greater than 360, it is converted to the default value **1**.

 |

#### PanRecognizer12+

Implements a pan gesture recognizer. Inherits from [GestureRecognizer](#gesturerecognizer12).

#### \[h2\]getPanGestureOptions12+

getPanGestureOptions(): PanGestureOptions

Obtains the properties of this pan gesture recognizer.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| [PanGestureOptions](../basic-gestures/pangesture/document.md#pangestureoptions) | Properties of the current pan gesture recognizer. |

#### \[h2\]getDirection19+

getDirection(): PanDirection

Obtains the recognized direction of the current pan gesture recognizer.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| [PanDirection](../basic-gestures/pangesture/document.md#pandirection) | Recognized direction of the current pan gesture recognizer. |

#### \[h2\]getDistance19+

getDistance(): number

Obtains the minimum pan distance required to trigger this pan gesture recognizer.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| number | Minimum swipe distance. Unit: vp. |

#### \[h2\]getDistanceMap19+

getDistanceMap(): Map<SourceTool, number>

Obtains the minimum pan distances required for different input sources to trigger this pan gesture recognizer.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/Oem1kGNPTcyiiK8xzfSqHg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062237Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4C4CB8B07859F5460A762FDFB4179DA17B2AE16D9B5E6AB3BD928120B17B1A34)

This API only returns thresholds for input sources that have been explicitly configured during pan gesture initialization. The default threshold can be queried using the [SourceTool](../gesture-binding/gesture-binding/document.md#sourcetool9).Unknown type. Thresholds for unconfigured device types are not available.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| Map<[SourceTool](../gesture-binding/gesture-binding/document.md#sourcetool9), number> | Minimum pan distances required for different input sources to trigger the pan gesture recognizer. Unit: vp. |

#### GestureRecognizerState12+

Enumerates the gesture recognizer states.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| READY | 0 | Ready. |
| DETECTING | 1 | Detecting. |
| PENDING | 2 | Pending. |
| BLOCKED | 3 | Blocked. |
| SUCCESSFUL | 4 | Successful. |
| FAILED | 5 | Failed. |

#### GestureEvent

Defines the gesture event information. Inherits from [BaseEvent](../gesture-control/custom-gesture-judgment/document.md#baseevent8).

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| repeat | boolean | No | No | 
Whether the event is a repeated trigger event, used in the **LongPressGesture** scenarios. The value **true** means that the event is a repeated trigger event, and **false** means the opposite.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| offsetX | number | No | No | 

X-axis offset of the gesture event relative to the finger press position, in vp. Used in **PanGesture** scenarios. A positive value means to pan from left to right, and a negative value means the opposite.

**Atomic service API**: This API can be used in atomic services since API version 11.

Value range: (-∞, +∞)

 |
| offsetY | number | No | No | 

Y-axis offset of the gesture event relative to the finger press position, in vp. Used in **PanGesture** scenarios. A positive value means to pan from top to bottom, and a negative value means the opposite.

**Atomic service API**: This API can be used in atomic services since API version 11.

Value range: (-∞, +∞)

 |
| angle | number | No | No | 

Rotation angle for the **RotationGesture** event.

Angle of the swipe gesture for the **SwipeGesture** event, that is, the change in the included angle between the line segment created by the two fingers and the horizontal direction.

**NOTE**

Angle calculation method: After a swipe gesture is recognized, a line connecting the two fingers is identified as the initial line. As the fingers swipe, the line between the fingers rotates. Based on the coordinates of the initial line's and current line's end points, the arc tangent function is used to calculate the respective included angle of the points relative to the horizontal direction by using the following formula: Rotation angle = arctan2(cy2-cy1,cx2-cx1) - arctan2(y2-y1,x2-x1). The initial line is used as the coordinate system. The clockwise rotation is 0 to 180 degrees, and the counter-clockwise rotation is -180 to 0 degrees.

Value range: \[-180, +180\]

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| scale | number | No | No | 

Scale ratio. This attribute is used for the pinch gesture.

Value range: \[0, +∞)

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| pinchCenterX | number | No | No | 

X-coordinate of the center of the pinch gesture, in vp, relative to the original area of the current component. This attribute is used for the **PinchGesture** event.

Value range: \[0, +∞)

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| pinchCenterY | number | No | No | 

Y-coordinate of the center of the pinch gesture, in vp, relative to the original area of the current component. This attribute is used for the **PinchGesture** event.

Value range: \[0, +∞)

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| speed8+ | number | No | No | 

Swipe gesture speed, that is, the average swipe speed of all fingers relative to the original area of the current component, in vp/s. Used for the **SwipeGesture** event.

Value range: \[0, +∞)

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| fingerList8+ | [FingerInfo](#fingerinfo8)\[\] | No | No | 

List of touch points of the gesture event. If the event input device is touchscreen, the list includes all touch points. If the event input device is mouse or touchpad, the list contains only one touch point.

**NOTE**

1\. The index of a finger corresponds to its position, that is, the ID of a finger in **fingerList\[index\]** refers to its index. If a finger is pressed first and does not participate in triggering of the current gesture, its position in **fingerList** is left empty.

2\. **fingerList** is empty when gestures are triggered using a keyboard or game controller and no finger information exists.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| fingerInfos20+ | [FingerInfo](#fingerinfo8)\[\] | No | Yes | 

Information about touch points of the gesture event. For gesture events initiated by a touchscreen, **fingerInfos** includes information about all touch points. For gesture events initiated by a mouse or touchpad, **fingerInfos** contains only one touch point.

**NOTE**

**fingerInfos** only records information about effective fingers that participate in the touch. Fingers that are pressed first but do not participate in triggering of the current gesture will not be shown in **fingerInfos**. The default value is an empty array **\[\]**, and an empty array indicates no effective touch point information.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |
| velocityX10+ | number | No | No | 

Velocity along the x-axis. This parameter is used in [PanGesture](../basic-gestures/pangesture/document.md). The origin of the coordinate axis is the upper left corner of the screen. The velocity is positive if the movement is from left to right, and it is negative if the movement is from right to left. The unit is vp/s.

Value range: (-∞, +∞)

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| velocityY10+ | number | No | No | 

Velocity along the y-axis. This parameter is used in [PanGesture](../basic-gestures/pangesture/document.md). The origin of the coordinate axis is the upper left corner of the screen. The velocity is positive if the movement is from top to bottom, and it is negative if the movement is from bottom to top. The unit is vp/s.

Value range: (-∞, +∞)

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| velocity10+ | number | No | No | 

Velocity along the main axis. This parameter is used in [PanGesture](../basic-gestures/pangesture/document.md). The value is the arithmetic square root of the sum of squares of the velocity along the x- and y-axis. The unit is vp/s.

Value range: \[0, +∞)

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| tapLocation20+ | [EventLocationInfo](../basic-gestures/tapgesture/document.md#eventlocationinfo20) | No | Yes | 

Coordinate information of the current tap gesture. For non-tap gestures, the return value of **tapLocation** is **undefined**.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |

#### GestureMask

Enumerates masking modes of child component gestures.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| Normal | \- | The gestures of child components are enabled and recognized based on the default gesture recognition sequence. |
| IgnoreInternal | \- | The gestures of child components are disabled, including the built-in gestures, such as the built-in swipe gesture for a **List** component. If the areas of the parent and child components are partly overlapped, only gestures in the overlapped areas are disabled. |

#### GestureJudgeResult11+

Enumerates gesture competition results.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| CONTINUE | 0 | The system gesture recognition process continues. |
| REJECT | 1 | Gesture recognition fails. |

#### GestureType11+

Enumerates gesture recognizer types.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| TAP\_GESTURE | 0 | Tap. |
| LONG\_PRESS\_GESTURE | 1 | Long press gesture. |
| PAN\_GESTURE | 2 | Pan. |
| PINCH\_GESTURE | 3 | Pinch gesture. |
| SWIPE\_GESTURE | 4 | Swipe. |
| ROTATION\_GESTURE | 5 | Rotation gesture. |
| DRAG | 6 | Drag and drop. |
| CLICK | 7 | Click. |

#### GestureInfo11+

Defines the gesture information type.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| tag | string | No | Yes | 
Gesture tag.

**NOTE**

Returns **undefined** if the gesture's **tag** attribute was not set.

 |
| type | [GestureControl.GestureType](#gesturetype11) | No | No | 

Gesture type.

**NOTE**

Returns **\-1** for built-in gestures of unexposed types.

 |
| isSystemGesture | boolean | No | No | 

Whether the gesture is a system/component gesture. **true** if the gesture is a system/component gesture, **false** otherwise.

Default value: **false**

 |

#### FingerInfo8+

Defines the finger information type.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| id | number | No | No | 
Index of the finger, determined by the number of fingers pressed. The first pressed finger is assigned 0, with the index incrementing by one for each subsequent finger.

**NOTE**

Indexes for other input sources (mouse: 1001, stylus: 102, mouse wheel: 0, two-finger trackpad slide: 0) are also converted to finger indexes.

Value range: \[0, 9)

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| globalX | number | No | No | 

X-coordinate relative to the upper left corner of the application window, in vp.

Value range: \[0, +∞)

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| globalY | number | No | No | 

Y-coordinate relative to the upper left corner of the application window, in vp.

Value range: \[0, +∞)

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| localX | number | No | No | 

X-coordinate relative to the upper left corner of the current component's original area, in vp.

Value range: \[0, +∞)

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| localY | number | No | No | 

Y-coordinate relative to the upper left corner of the current component's original area, in vp.

Value range: \[0, +∞)

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| displayX12+ | number | No | No | 

X-coordinate relative to the upper left corner of the screen, in vp.

Value range: \[0, +∞)

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| displayY12+ | number | No | No | 

Y-coordinate relative to the upper left corner of the screen, in vp.

Value range: \[0, +∞)

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| hand15+ | [InteractionHand](../../common-definitions/enums/document.md#interactionhand15) | No | Yes | 

Whether the event is triggered by a left-hand or right-hand tap.

**Atomic service API**: This API can be used in atomic services since API version 15.

 |
| globalDisplayX20+ | number | No | Yes | 

X-coordinate relative to the upper left corner of the global display, in vp.

Value range: \[0, +∞)

**Atomic service API**: This API can be used in atomic services since API version 20.

 |
| globalDisplayY20+ | number | No | Yes | 

Y-coordinate relative to the upper left corner of the global display, in vp.

Value range: \[0, +∞)

**Atomic service API**: This API can be used in atomic services since API version 20.

 |

#### GestureType

type GestureType = TapGesture | LongPressGesture | PanGesture | PinchGesture | SwipeGesture | RotationGesture | GestureGroup

Enumerates gesture recognizer types. The value type is a union of the types listed in the table below.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Type | Description |
| :-- | :-- |
| [TapGesture](../basic-gestures/tapgesture/document.md) | Tap gesture, which can be a single-tap or multi-tap gesture. |
| [LongPressGesture](../basic-gestures/longpressgesture/document.md) | Long press. |
| [PanGesture](../basic-gestures/pangesture/document.md) | Pan gesture (triggered when the movement distance of a finger on the screen reaches the minimum value, which is 5 vp by default). |
| [PinchGesture](../basic-gestures/pinchgesture/document.md) | Pinch gesture. |
| [RotationGesture](../basic-gestures/rotationgesture/document.md) | Rotation gesture. |
| [SwipeGesture](../basic-gestures/swipegesture/document.md) | Swipe gesture (triggered when the swipe speed exceeds the specified threshold, which is 100 vp/s by default). |
| [GestureGroup](../combined-gestures/document.md) | A group of gestures. Continuous recognition, parallel recognition, and exclusive recognition are supported. |

#### BaseGestureEvent11+

Defines the basic gesture event type. Inherits from [BaseEvent](../gesture-control/custom-gesture-judgment/document.md#baseevent8).

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| fingerList | [FingerInfo](#fingerinfo8)\[\] | No | No | 
Information about all fingers triggering the event.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| fingerInfos20+ | [FingerInfo](#fingerinfo8)\[\] | No | Yes | 

Information about all valid touch points. The default value is an empty array **\[\]**, and an empty array indicates no effective touch point information.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |

#### TapGestureEvent11+

Inherits from [BaseGestureEvent](#basegestureevent11). This object can be passed as the **event** parameter of [onGestureJudgeBegin](../gesture-control/custom-gesture-judgment/document.md#ongesturejudgebegin).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| tapLocation20+ | [EventLocationInfo](../basic-gestures/tapgesture/document.md#eventlocationinfo20) | No | Yes | 
Coordinates of the tap gesture.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |

#### LongPressGestureEvent11+

Inherits from [BaseGestureEvent](#basegestureevent11). This object can be passed as the **event** parameter of [onGestureJudgeBegin](../gesture-control/custom-gesture-judgment/document.md#ongesturejudgebegin).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| repeat | boolean | No | No | Whether the event is a repeated trigger event. **true**: The event is repeated. **false**: The event is not repeated. |

#### PanGestureEvent11+

Inherits from [BaseGestureEvent](#basegestureevent11). This object can be passed as the **event** parameter of [onGestureJudgeBegin](../gesture-control/custom-gesture-judgment/document.md#ongesturejudgebegin).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| offsetX | number | No | No | Offset of the gesture event on the x-axis relative to the original area of the current component, in vp. A positive value means to pan from left to right, and a negative value means the opposite. |
| offsetY | number | No | No | Offset of the gesture event on the y-axis relative to the original area of the current component, in vp. A positive value means to pan from top to bottom, and a negative value means the opposite. |
| velocityX | number | No | No | Velocity along the x-axis. The origin of the coordinate axis is the upper left corner of the screen. The velocity is positive if the movement is from left to right, and it is negative if the movement is from right to left. The unit is vp/s. |
| velocityY | number | No | No | Velocity along the y-axis. The origin of the coordinate axis is the upper left corner of the screen. The velocity is positive if the movement is from top to bottom, and it is negative if the movement is from bottom to top. The unit is vp/s. |
| velocity | number | No | No | Velocity along the main axis. The value is the arithmetic square root of the sum of squares of the velocity along the x- and y-axis. The unit is vp/s. |

#### PinchGestureEvent11+

Inherits from [BaseGestureEvent](#basegestureevent11). This object can be passed as the **event** parameter of [onGestureJudgeBegin](../gesture-control/custom-gesture-judgment/document.md#ongesturejudgebegin).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| scale | number | No | No | Scale factor. |
| pinchCenterX | number | No | No | X-coordinate of the center of the pinch gesture, in vp, relative to the original area of the current component. |
| pinchCenterY | number | No | No | Y-coordinate of the center of the pinch gesture, in vp, relative to the original area of the current component. |

#### RotationGestureEvent11+

Inherits from [BaseGestureEvent](#basegestureevent11). This object can be passed as the **event** parameter of [onGestureJudgeBegin](../gesture-control/custom-gesture-judgment/document.md#ongesturejudgebegin).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| angle | number | No | No | 
Rotation angle, in deg.

**NOTE**

Angle calculation: Once a rotation gesture is detected, the line connecting two fingers is considered the start line. As the fingers move, the line between them rotates. Based on the coordinates of the start line and the current line, the included angle relative to the horizontal axis is computed using the arctangent function.

The final angle is calculated as follows: arctan2(cy2 - cy1, cx2 - cx1) - arctan2(y2 - y1, x2 - x1).

If the start line is taken as the reference axis, clockwise rotation produces values from 0 to 180 degrees, and counterclockwise rotation produces values from –180 to 0 degrees.

 |

#### SwipeGestureEvent11+

Inherits from [BaseGestureEvent](#basegestureevent11). This object can be passed as the **event** parameter of [onGestureJudgeBegin](../gesture-control/custom-gesture-judgment/document.md#ongesturejudgebegin).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| angle | number | No | No | 
Angle of the swipe gesture, that is, the change in the included angle between the line segment created by the two fingers and the horizontal direction. The unit is deg.

**NOTE**

Angle calculation: Once a swipe gesture is detected, the line connecting two fingers is considered the start line. As the fingers move, the line between them rotates. Based on the coordinates of the start line and the current line, the included angle relative to the horizontal axis is computed using the arctangent function.

The final angle is calculated as follows: arctan2(cy2 - cy1, cx2 - cx1) - arctan2(y2 - y1, x2 - x1).

If the start line is taken as the reference axis, clockwise rotation produces values from 0 to 180 degrees, and counterclockwise rotation produces values from –180 to 0 degrees.

 |
| speed | number | No | No | Swipe gesture speed, defined as the average swipe speed of all fingers relative to the original area of the current component. The unit is vp/s. |
