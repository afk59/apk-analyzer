# @ohos.multimodalInput.keyEvent (Key Event)

The **keyEvent** module provides key events reported by a device. It is inherited from [InputEvent](../ohos-multimodalinput-inputevent-input-event/document.md).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/RXLM4DgWScKD1MKse4Ti7g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062403Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A4BFB6CA72CCCBD06A5C54AD88524AFDC31D41F9AF23D7BCAAB913E8E73CE0F6)

-   The initial APIs of this module are supported since API version 9. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { Action, Key, KeyEvent } from '@kit.InputKit';

#### Action

Key event type.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.MultimodalInput.Input.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| CANCEL | 0 | Cancellation of a key action. |
| DOWN | 1 | Key press. |
| UP | 2 | Key release. |

#### Key

Defines a key.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.MultimodalInput.Input.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| code | [KeyCode](../ohos-multimodalinput-keycode-keycode/document.md#keycode) | No | No | Key code. |
| pressedTime | number | No | No | Key press time, in μs. |
| deviceId | number | No | No | Unique ID of the input device. If a physical device is repeatedly reinstalled or restarted, its ID may change. |

#### KeyEvent

Key event.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.MultimodalInput.Input.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| action | [Action](#action) | No | No | Key event type. |
| key | [Key](#key) | No | No | Defines a key. |
| unicodeChar | number | No | No | Unicode character corresponding to the key. |
| keys | [Key](#key) \[\] | No | No | List of pressed keys. |
| ctrlKey | boolean | No | No | 
Whether ctrlKey is being pressed.

The value **true** indicates that the key is pressed, and the value **false** indicates the opposite.

 |
| altKey | boolean | No | No | 

Whether altKey is being pressed.

The value **true** indicates that the key is pressed, and the value **false** indicates the opposite.

 |
| shiftKey | boolean | No | No | 

Whether shiftKey is being pressed.

The value **true** indicates that the key is pressed, and the value **false** indicates the opposite.

 |
| logoKey | boolean | No | No | 

Whether logoKey is being pressed.

The value **true** indicates that the key is pressed, and the value **false** indicates the opposite.

 |
| fnKey | boolean | No | No | 

Whether fnKey is being pressed.

The value **true** indicates that the key is pressed, and the value **false** indicates the opposite.

 |
| capsLock | boolean | No | No | 

Whether capsLock is enabled.

The value **true** indicates that capsLock is enabled, and the value **false** indicates the opposite.

 |
| numLock | boolean | No | No | 

Whether numLock is enabled.

The value **true** indicates that numLock is enabled, and the value **false** indicates the opposite.

 |
| scrollLock | boolean | No | No | 

Whether scrollLock is enabled.

The value **true** indicates that scrollLock is enabled, and the value **false** indicates the opposite.

 |
