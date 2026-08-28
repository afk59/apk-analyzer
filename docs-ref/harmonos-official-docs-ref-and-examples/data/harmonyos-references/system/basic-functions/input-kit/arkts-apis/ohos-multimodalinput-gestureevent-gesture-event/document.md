# @ohos.multimodalInput.gestureEvent (Gesture Event)

The **gestureEvent** module provides APIs for gesture events reported by devices.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/Ir_-EMuiSs25CYFBO2lLyg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062404Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=48F7A6F2AC1FD3D55C07693AADFC8880ABD4DFF9F47B29EDC058AA903AF79344)

-   The initial APIs of this module are supported since API version 10. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { Rotate, Pinch, ThreeFingersSwipe, FourFingersSwipe, ActionType } from '@kit.InputKit';

#### Pinch

Defines a pinch event.

**System capability**: SystemCapability.MultimodalInput.Input.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| type | [ActionType](#actiontype) | No | No | Event type, for example, gesture start, gesture update, or gesture end. |
| scale | number | No | No | Pinch scale factor. The value is greater than or equal to 0. |

#### Rotate11+

Defines a rotation gesture event.

**System capability**: SystemCapability.MultimodalInput.Input.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| type | [ActionType](#actiontype) | No | No | Event type, for example, gesture start, gesture update, or gesture end. |
| angle | number | No | No | Angle to rotate. |

#### ThreeFingersSwipe

Defines a three-finger swipe gesture event.

**System capability**: SystemCapability.MultimodalInput.Input.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| type | [ActionType](#actiontype) | No | No | Event type, for example, gesture start, gesture update, or gesture end. |
| x | number | No | No | X coordinate. |
| y | number | No | No | Y coordinate. |

#### FourFingersSwipe

Defines a four-finger swipe gesture event.

**System capability**: SystemCapability.MultimodalInput.Input.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| type | [ActionType](#actiontype) | No | No | Event type, for example, gesture start, gesture update, or gesture end. |
| x | number | No | No | X coordinate. |
| y | number | No | No | Y coordinate. |

#### ThreeFingersTap11+

Defines a three-finger tap gesture event.

**System capability**: SystemCapability.MultimodalInput.Input.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| type | [ActionType](#actiontype) | No | No | Event type, for example, gesture start, gesture update, or gesture end. |

#### ActionType

Enumerates gesture event types.

**System capability**: SystemCapability.MultimodalInput.Input.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| CANCEL | 0 | Canceled. |
| BEGIN | 1 | Started. |
| UPDATE | 2 | Updated. |
| END | 3 | Ended. |
