# Interfaces (Others)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/VsPJfIYoTaOew_sLuPdpPA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062228Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D089CD3C8972BA465A88A8303A858603452F30F2ABFF131B2A13BA5A9F4B1E5F)

The initial APIs of this module are supported since API version 10. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### TargetInfo18+

Specifies the target node for component binding.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| id | string | number | No | No | 
Target node for binding popups or menus.

**NOTE**

1\. When **id** is a number, it corresponds to the component's **UniqueID**, whose uniqueness is guaranteed by the system.

2\. When **id** is a string, it corresponds to the component specified by the universal attribute [id](../../../../arkts-components/universal-attributes/basic-attributes/component-id/document.md#id). You must ensure the uniqueness of this ID, although there may be multiple instances.

 |
| componentId | number | No | Yes | Unique ID of the custom component where the target node is located. When the above **id** is specified as a string, this property can be used to narrow down the scope, helping you ensure the uniqueness of **id: string** within a certain range. |

#### PageInfo12+

Represents the page information of the router or navigation destination. If there is no related page information, **undefined** is returned.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| routerPageInfo | observer.[RouterPageInfo](../../ohos-arkui-observer-observer/document.md#routerpageinfo) | No | Yes | Router information. |
| navDestinationInfo | observer.[NavDestinationInfo](../../ohos-arkui-observer-observer/document.md#navdestinationinfo) | No | Yes | Navigation destination information. |

#### OverlayManagerOptions15+

Provides the parameters used for initializing [OverlayManager](../class-overlaymanager/document.md).

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| renderRootOverlay | boolean | No | Yes | 
Whether to render the overlay root node. The value **true** means to render the overlay root node, and **false** means the opposite. The default value is **true**.

**Atomic service API**: This API can be used in atomic services since API version 15.

 |
| enableBackPressedEvent19+ | boolean | No | Yes | 

Whether to enable the swipe-to-dismiss gesture for **ComponentContent** under **OverlayManager**. The value **true** means to enable the swipe-to-dismiss gesture, and **false** means the opposite. Default value: **false**.

**Atomic service API**: This API can be used in atomic services since API version 19.

 |

#### GestureTriggerInfo20+

Defines the information provided when a specific gesture callback is triggered.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| event | [GestureEvent](../../../../arkts-components/gesture-handling/gesture-common-apis/document.md#gestureevent) | No | No | Gesture event object. |
| current | [GestureRecognizer](../../../../arkts-components/gesture-handling/gesture-common-apis/document.md#gesturerecognizer12) | No | No | Gesture recognizer object. Detailed gesture information can be obtained from this object. However, avoid retaining this object locally as it may become invalid after the node is released. |
| currentPhase | [GestureActionPhase](../enums/document.md#gestureactionphase20) | No | No | Phase of the gesture action callback. |
| node | [FrameNode](../../arkui/framenode/document.md) | No | Yes | Node that triggers the gesture. The default value is **null**, indicating that no specific node triggers the gesture. |

#### GestureObserverConfigs20+

Specifies the gesture callback phases to listen for (passing an empty array will be ineffective). Notifications are sent only when the gesture triggers the specified phases.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| actionPhases | Array<[GestureActionPhase](../enums/document.md#gestureactionphase20)\> | No | No | Gesture event object. |

#### SwiperContentInfo22+

Provides content area information of the **Swiper** component.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| id | string | No | No | ID of the **Swiper** component. |
| uniqueId | number | No | No | Unique ID of the **Swiper** component. |
| swiperItemInfos | Array<[SwiperItemInfo](#swiperiteminfo22)\> | No | No | Information about the currently visible child components within the **Swiper** container. |

#### SwiperItemInfo22+

Provides information about **Swiper** child components.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| uniqueId | number | No | No | Unique ID of the **Swiper** child component. |
| index | number | No | No | Index of the child component in the **Swiper** container. |
