# @ohos.multimodalInput.inputEvent (Input Event)

The **inputEvent** module provides the basic events reported by the device.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0c/v3/kblXGQ47SJ6UD8MiSQ0ZCQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062403Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=10D361F5154ED9DFC5D02CF0FC7D62D56CF26647C2F870D5FE77658FE9B82C48)

-   The initial APIs of this module are supported since API version 9. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { InputEvent } from '@kit.InputKit';

#### InputEvent

Represents an input event.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.MultimodalInput.Input.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| id | number | No | No | Event ID. |
| deviceId | number | No | No | Unique ID of the input device. If a physical device is repeatedly reinstalled or restarted, its ID may change. |
| actionTime | number | No | No | Time when the input event is reported. |
| screenId | number | No | No | Target screen ID. |
| windowId | number | No | No | Target window ID. |
