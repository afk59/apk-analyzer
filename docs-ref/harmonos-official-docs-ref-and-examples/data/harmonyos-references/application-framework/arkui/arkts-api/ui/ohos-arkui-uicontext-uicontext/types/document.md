# Types

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/8UteuVUcQreNDO8EDcGNQQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062228Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C3138863D29EEE9471CE047A1104C2D9DD62E496A66BDA7E846F6A01CFCD4420)

The initial APIs of this module are supported since API version 12. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### CustomBuilderWithId18+

type CustomBuilderWithId = (id: number) => void

Defines a type that can be used for component attributes and method parameters to customize the UI description and generate custom components with a specific component ID.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| id | number | Yes | Component ID. |

#### ClickEventListenerCallback12+

type ClickEventListenerCallback = (event: ClickEvent, node?: FrameNode) => void

Defines the callback type for listening for click events in **UIObserver**.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | [ClickEvent](../../../../arkts-components/universal-events/interaction-response-events/click-event/document.md#clickevent) | Yes | Information about the click event that triggers the callback. |
| node | [FrameNode](../../arkui/framenode/document.md) | No | Component bound to the click event. |

#### PanListenerCallback19+

type PanListenerCallback = (event: GestureEvent, current: GestureRecognizer, node?: FrameNode) => void

Defines a callback for pan gesture events.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | [GestureEvent](../../../../arkts-components/gesture-handling/gesture-common-apis/document.md#gestureevent) | Yes | Information about the gesture event that triggers the callback. |
| current | [GestureRecognizer](../../../../arkts-components/gesture-handling/gesture-common-apis/document.md#gesturerecognizer12) | Yes | Information about the gesture recognizer that detects the event. |
| node | [FrameNode](../../arkui/framenode/document.md) | No | Component bound to the gesture event. |

#### GestureEventListenerCallback12+

type GestureEventListenerCallback = (event: GestureEvent, node?: FrameNode) => void

Defines the callback type for gesture event listeners in **UIObserver**.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | [GestureEvent](../../../../arkts-components/gesture-handling/gesture-common-apis/document.md#gestureevent) | Yes | Information about the gesture event that triggers the callback. |
| node | [FrameNode](../../arkui/framenode/document.md) | No | Component bound to the gesture event. |

#### NodeIdentity20+

type NodeIdentity = string | number

Defines the component ID.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Type | Description |
| :-- | :-- |
| string | ID of the target component, set using the universal attributes [id](../../../../arkts-components/universal-attributes/basic-attributes/component-id/document.md#id). |
| number | System-assigned unique node ID, obtainable via [getUniqueId](../../arkui/framenode/document.md#getuniqueid12). |

#### NodeRenderStateChangeCallback20+

type NodeRenderStateChangeCallback = (state: NodeRenderState, node?: FrameNode) => void

Defines the callback type for listening for the rendering state of a specific node in **UIObserver**.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| state | [NodeRenderState](../enums/document.md#noderenderstate20) | Yes | Information about the gesture event that triggers the callback. |
| node | [FrameNode](../../arkui/framenode/document.md) | No | Component bound to the gesture event that triggers the listener; returns **null** if the component has been released. |

#### GestureListenerCallback20+

type GestureListenerCallback = (info: GestureTriggerInfo) => void

Defines the callback type for listening for specific gesture trigger information in **UIObserver**.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| info | [GestureTriggerInfo](../interfaces-others/document.md#gesturetriggerinfo20) | Yes | Details of the gesture triggered by the interaction. |

#### PointerStyle12+

type PointerStyle = pointer.PointerStyle

Defines the pointer style.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.MultimodalInput.Input.Pointer

| Type | Description |
| :-- | :-- |
| [pointer.PointerStyle](../../../../../../system/basic-functions/input-kit/arkts-apis/ohos-multimodalinput-pointer-mouse-pointer/document.md#pointerstyle) | Pointer style. |

#### Context12+

type Context = common.Context

Defines the context of the current ability.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Model restriction**: This API can be used only in the stage model.

| Type | Description |
| :-- | :-- |
| [common.Context](../../../../../ability-kit/arkts-apis/stage-model/ohos-app-ability-common-ability-common-module/document.md#context) | Context object associated with the current ability. |
