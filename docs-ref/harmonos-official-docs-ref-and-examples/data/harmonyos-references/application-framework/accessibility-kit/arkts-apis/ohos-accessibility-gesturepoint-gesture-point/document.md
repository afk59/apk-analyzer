# @ohos.accessibility.GesturePoint (Gesture Point)

The **GesturePoint** module provides APIs for creating gesture touch point information required for an accessibility application to inject gestures.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/03rxGOhhS3GaqpkuM-g0uw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062214Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2B5512F3ABAFEFC903102FFBBF96763E2652759BE702CB6AC342B745D3B2E943)

-   The initial APIs of this module are supported since API version 9. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { GesturePoint } from '@kit.AccessibilityKit';

#### GesturePoint

Defines a gesture touch point.

**System capability**: SystemCapability.BarrierFree.Accessibility.Core

## Attributes

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| positionX | number | No | No | X coordinate of the touch point. |
| positionY | number | No | No | Y coordinate of the touch point. |

#### \[h2\]constructor(deprecated)

constructor(positionX: number, positionY: number);

Defines a constructor used to create a **GesturePoint** instance.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/cjZuUltVToqBjPDwQ_GYKw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062214Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F2C71F0C81CAAD981FB53305604A350C0684776C6874F0BF160F133306A6F20D)

This API is supported since API version 9 and deprecated since API version 12. Related capabilities are no longer available in the system.

**System capability**: SystemCapability.BarrierFree.Accessibility.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| positionX | number | Yes | X coordinate of the touch point. |
| positionY | number | Yes | Y coordinate of the touch point. |

**Example**

import { GesturePoint } from '@kit.AccessibilityKit';

let gesturePoint = new GesturePoint(1, 2);
