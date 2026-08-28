# PushExtensionAbility

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/h6FNscjaRNGFOLRk5ExN0Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062517Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=51CBCF1575226C85B2F1D0A1F58AAB05985BDB324F73AEBE8B02ACB856D66F8B)

**PushExtensionAbility** is currently reserved and not open for use. If your app needs to start a subprocess to process services, please refer to [Pushing Text-to-Speech Messages](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/push-send-extend-noti).

**PushExtensionAbility** provides callbacks for obtaining scenario-specific message data and destroying the lifecycle. The restrictions are as follows:

-   **PushExtensionAbility** is a lightweight, independent subprocess. The main process cannot be woken up.
-   The notification APIs, widget APIs, window APIs, pop-up APIs, and live view APIs cannot be called.
-   The lifecycle is controlled based on scenarios and is less than 10 seconds by default. If the 10-second period expires, the subprocess lifecycle ends.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Push.PushService

**Start version**: 4.0.0(10)

#### Module Import

import { PushExtensionAbility } from '@kit.PushKit';

#### Attributes

**Model restriction**: The attributes can be used only in the stage model.

**System capability**: SystemCapability.Push.PushService

**Device behavior differences**: For versions earlier than 5.1.0(18), this attribute is supported on phones, tablets, and PCs/2-in-1 devices, but does not work on other devices. For version 5.1.0(18), this attribute is supported on phones, tablets, PCs/2-in-1 devices, and wearables, but does not work on other devices. For version 5.1.1(19) or later, this attribute is supported on phones, tablets, PCs/2-in-1 devices, wearables, and TVs.

**Start version**: 4.0.0(10)

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

context

 | 

[PushExtensionContext](../pushextensioncontext/document.md)

 | 

No

 | 

No

 | 

Context of **PushExtensionAbility**, which inherits from [ExtensionContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/extensioncontext/document.md).

 |

#### onReceiveMessage

onReceiveMessage(payload: pushCommon.PushPayload): void

API for receiving scenario-specific messages after an app inherits from **PushExtensionAbility**.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Push.PushService

**Device behavior differences**: For versions earlier than 5.1.0(18), this API is supported on phones, tablets, and PCs/2-in-1 devices, but does not work on other devices. For version 5.1.0(18), this API is supported on phones, tablets, PCs/2-in-1 devices, and wearables, but does not work on other devices. For version 5.1.1(19) or later, this API is supported on phones, tablets, PCs/2-in-1 devices, wearables, and TVs.

**Start version**: 4.0.0(10)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

payload

 | 

pushCommon.[PushPayload](../pushcommon/document.md#section16335431712)

 | 

Yes

 | 

Scenario-specific message data.

 |

**Example**:

import { PushExtensionAbility, pushCommon } from '@kit.PushKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

// In the following example, **TestExtAbility** inherits from **PushExtensionAbility**:
export default class TestExtAbility extends PushExtensionAbility {
  onReceiveMessage(payload: pushCommon.PushPayload): void {
    hilog.info(0x0000, 'testTag', 'TestExtAbility onReceiveMessage');
  }
}

#### onDestroy

onDestroy(): void

This callback is executed when the **PushExtensionAbility** lifecycle ends. You are advised to clear resources in this method.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Push.PushService

**Device behavior differences**: For versions earlier than 5.1.0(18), this API is supported on phones, tablets, and PCs/2-in-1 devices, but does not work on other devices. For version 5.1.0(18), this API is supported on phones, tablets, PCs/2-in-1 devices, and wearables, but does not work on other devices. For version 5.1.1(19) or later, this API is supported on phones, tablets, PCs/2-in-1 devices, wearables, and TVs.

**Start version**: 4.0.0(10)

**Example**:

import { PushExtensionAbility } from '@kit.PushKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

// In the following example, **TestExtAbility** inherits from **PushExtensionAbility**:
export default class TestExtAbility extends PushExtensionAbility {
  onDestroy(): void {
    hilog.info(0x0000, 'testTag', 'TestExtAbility onDestroy');
  }
}
