# Enums

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3/v3/horwBHy_Tde9uxZ1bSX96Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062228Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=78416DE17EF892EB1EC1EC079314F5B3CA92ED31AD1D3FD205B757736CED0EFB)

The initial APIs of this module are supported since API version 10. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### KeyboardAvoidMode11+

Enumerates the modes in which the layout responds when the keyboard is displayed.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| OFFSET | 0 | 
The layout moves up.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| RESIZE | 1 | 

The layout is resized.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| OFFSET\_WITH\_CARET14+ | 2 | 

The layout moves up, and this adjustment also occurs if the caret position in the text box changes.

**Atomic service API**: This API can be used in atomic services since API version 14.

 |
| RESIZE\_WITH\_CARET14+ | 3 | 

The layout is resized, and this adjustment also occurs if the caret position in the text box changes.

**Atomic service API**: This API can be used in atomic services since API version 14.

 |
| NONE14+ | 4 | 

The layout is not adjusted to avoid the keyboard.

**Atomic service API**: This API can be used in atomic services since API version 14.

 |

#### SwiperDynamicSyncSceneType12+

Enumerates the dynamic sync scene types.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| GESTURE | 0 | Gesture operation. |
| ANIMATION | 1 | Animation transition. |

#### MarqueeDynamicSyncSceneType14+

Enumerates the dynamic sync scene types for the **Marquee** component.

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| ANIMATION | 1 | Animation transition. |

#### NodeRenderState20+

Enumerates component rendering states.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| ABOUT\_TO\_RENDER\_IN | 0 | The node has been attached to the render tree and will generally be rendered in the next frame. Under normal cases, it may be visible, but "being scheduled for rendering" does not equate to "guaranteed visibility". |
| ABOUT\_TO\_RENDER\_OUT | 1 | The node has been removed from the render tree and will generally not be rendered in the next frame. Users will no longer see this node. |

#### GestureActionPhase20+

Enumerates triggering phases of gesture callbacks, corresponding to the action callbacks defined in **gesture.d.ts**. However, different gesture types support different phases (for example, **SwipeGesture** only includes the **WILL\_START** enumerated value).

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| WILL\_START | 0 | The gesture has been successfully recognized by the system, and the **onActionStart** or **onAction** callback will be triggered immediately. If the gesture is bound to **onActionStart**, the callback is triggered at **onActionStart**. If the gesture is bound to **onAction**, the callback is triggered at **onAction**. If both are bound, the callback is triggered at **onActionStart** with priority. If neither is bound, no callback will be triggered. Some containers (for example, scrollable containers) have built-in gestures bound to callbacks, which support the above callback triggering mechanism by default. For these containers, callbacks can be triggered without explicit binding. |
| WILL\_END | 1 | The gesture has been determined to be in an ended state (typically occurring when the user lifts their finger to terminate the interaction). The **onActionEnd** callback will be triggered immediately, but the gesture must be explicitly bound to **onActionEnd**. Some containers (for example, scrollable containers) have built-in gestures bound to callbacks, which support this end-state determination by default. For these containers, the **onActionEnd** callback can be triggered without explicit binding. |

#### GestureListenerType20+

Enumerates the types of gestures to be listened for.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| TAP | 0 | Tap gesture. |
| LONG\_PRESS | 1 | Long press gesture. |
| PAN | 2 | Pan gesture. |
| PINCH | 3 | Pinch gesture. |
| SWIPE | 4 | Swipe gesture. |
| ROTATION | 5 | Rotation gesture. |

#### ResolveStrategy22+

Enumerates resolution strategies for **UIContext** objects.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| CALLING\_SCOPE | 0 | Obtain the UIContext of the current calling scope. |
| LAST\_FOCUS | 1 | Obtain the UIContext of the instance that most recently switched to the focused state. |
| MAX\_INSTANCE\_ID | 2 | Obtain the UIContext of the instance with the largest instance ID. |
| UNIQUE | 3 | Obtain the UIContext of the unique UI instance (when only one UI instance exists). |
| LAST\_FOREGROUND | 4 | Obtain the UIContext of the instance that most recently switched to the foreground. |
| UNDEFINED | 5 | Obtain a UIContext with an ambiguous calling scope. |
