# Bound Gesture Configuration

You can set the gestures that are bound to a component. Specifically, you can add or remove gestures by calling the APIs of the **UIGestureEvent** object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/-sdUB2CoQgmo9K2Nu7NIVw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062237Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C9B1DC830749EB124F5124E9B9F7DE963DB434E7DC568D0D2EF9431DCF6498F4)

The initial APIs of this module are supported since API version 12. Newly added APIs will be marked with a superscript to indicate their earliest API version.

In **fingerList** of [GestureEvent](../../gesture-common-apis/document.md#gestureevent), the index of a finger corresponds to its position, that is, the ID of a finger in **fingerList\[index\]** refers to its index. If a finger is pressed first and does not participate in triggering of the current gesture, its position in **fingerList** is left empty. You are advised to use **fingerInfos** when possible.

#### UIGestureEvent

Provides APIs for configuring gestures bound to a component.

#### \[h2\]addGesture

addGesture<T>(gesture: GestureHandler<T>, priority?: GesturePriority, mask?: GestureMask): void

Adds a gesture.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| gesture | [GestureHandler<T>](../gesture-handler/document.md#gesturehandlert) | Yes | Gesture handler object. |
| priority | [GesturePriority](../gesture-handler/document.md#gesturepriority) | No | 
Priority of the bound gesture.

Default value: **GesturePriority.NORMAL**.

 |
| mask | [GestureMask](../../gesture-common-apis/document.md#gesturemask) | No | 

Mask for gesture events.

Default value: **GestureMask.Normal**.

 |

#### \[h2\]addParallelGesture

addParallelGesture<T>(gesture: GestureHandler<T>, mask?: GestureMask): void

Adds a gesture that can be recognized at once by the component and its child component.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| gesture | [GestureHandler<T>](../gesture-handler/document.md#gesturehandlert) | Yes | Gesture handler object. |
| mask | [GestureMask](../../gesture-common-apis/document.md#gesturemask) | No | 
Mask for gesture events.

Default value: **GestureMask.Normal**.

 |

#### \[h2\]removeGestureByTag

removeGestureByTag(tag: string): void

Remove a gesture from a component that has been bound with a specific tag through a modifier.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| tag | string | Yes | Gesture handler flag. |

#### \[h2\]clearGestures

clearGestures(): void

Clears all gestures that have been bound to the component through a modifier.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### Example

See the example in [Gesture Modifier](../../../universal-attributes/modifiers-and-custom-property/gesture-modifier/document.md).
