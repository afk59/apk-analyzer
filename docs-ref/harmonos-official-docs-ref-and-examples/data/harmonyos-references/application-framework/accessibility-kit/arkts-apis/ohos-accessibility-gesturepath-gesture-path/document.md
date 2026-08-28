# @ohos.accessibility.GesturePath (Gesture Path)

The **GesturePath** module provides APIs for creating gesture path information required for an accessibility application to inject gestures.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/0p6rOfZ_T6W8g72ixz_xZw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062214Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B86FDDDF7615A8390B79DC034A6F331A0AF5D4FA4DA0C3095EDE7CE959E9185B)

-   The initial APIs of this module are supported since API version 9. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { GesturePath } from '@kit.AccessibilityKit';

#### GesturePath

Defines a gesture path.

**System capability**: SystemCapability.BarrierFree.Accessibility.Core

## Properties

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| points | Array<[GesturePoint](../ohos-accessibility-gesturepoint-gesture-point/document.md#gesturepoint)\> | No | No | Gesture touch point. |
| durationTime | number | No | No | Total gesture duration, in milliseconds. |

#### \[h2\]constructor(deprecated)

constructor(durationTime: number);

Defines a constructor used to create a **GesturePath** instance.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/oIT2VmEATOauLxQ5OK-D9Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062214Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3D5AE4ED716914FE4356C41DF6135C338850A586DF2C46F7A2BF9EFC351277AB)

This API is supported since API version 9 and deprecated since API version 12. Related capabilities are no longer available in the system.

**System capability**: SystemCapability.BarrierFree.Accessibility.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| durationTime | number | Yes | Total gesture duration, in milliseconds. |

**Example**

import { GesturePath } from '@kit.AccessibilityKit';

let gesturePath = new GesturePath(20);
