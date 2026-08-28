# RemoteLocationExtensionAbility

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/rQ5EyDvYSDWNSa8958LBIw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062517Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4419930BD612266FC39E22F3A92B357637482B76A80F3616ABD7F18C25FC3B0C)

**RemoteLocationExtensionAbility** is currently reserved and not open for use.

**RemoteLocationExtensionAbility** provides callbacks for obtaining location-specific message data and destroying the lifecycle. After a user grants the location permission, **RemoteLocationExtensionAbility** can query the user's location and push messages based on service requirements. The restrictions are as follows:

-   **RemoteLocationExtensionAbility** is a lightweight, independent subprocess. The main process cannot be woken up.
-   The notification APIs and widget APIs cannot be called.
-   The lifecycle is controlled based on scenarios and is less than 10 seconds by default. If the 10-second period expires, the subprocess lifecycle ends.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Push.PushService

**Start version**: 4.1.0(11)

#### Module Import

import { RemoteLocationExtensionAbility } from '@kit.PushKit';

#### Attributes

**Model restriction**: The attributes can be used only in the stage model.

**System capability**: SystemCapability.Push.PushService

**Device behavior differences**: This attribute is supported on phones, tablets, and PCs/2-in-1 devices, but does not work on other devices.

**Start version**: 4.1.0(11)

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

[RemoteLocationExtensionContext](../remotelocationextensioncontext/document.md)

 | 

No

 | 

No

 | 

Context of **RemoteLocationExtensionAbility**, which inherits from [ExtensionContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/extensioncontext/document.md).

 |

#### onReceiveMessage

onReceiveMessage(payload: pushCommon.PushPayload): Promise<void>

API for receiving scenario-specific messages after an app inherits from **RemoteLocationExtensionAbility**. This API returns the result asynchronously through a promise.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Push.PushService

**Device behavior differences**: This API is supported on phones, tablets, and PCs/2-in-1 devices, but does not work on other devices.

**Start version**: 4.1.0(11)

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

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<void>

 | 

**Promise** object. No result is returned.

 |

**Example**:

import { RemoteLocationExtensionAbility, pushCommon } from '@kit.PushKit'; 
import { hilog } from '@kit.PerformanceAnalysisKit'; 
 
// In the following example, **TestExtAbility** inherits from **RemoteLocationExtensionAbility**:
export default class TestExtAbility extends RemoteLocationExtensionAbility { 
  async onReceiveMessage(payload: pushCommon.PushPayload): Promise<void> { 
    hilog.info(0x0000, 'testTag', 'TestExtAbility onReceiveMessage, payload : %{public}s', JSON.stringify(payload)); 
  } 
}

#### onDestroy

onDestroy(): void

This callback is executed when the **RemoteLocationExtensionAbility** lifecycle ends. You are advised to clear resources in this method.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Push.PushService

**Device behavior differences**: This API is supported on phones, tablets, and PCs/2-in-1 devices, but does not work on other devices.

**Start version**: 4.1.0(11)

**Example**:

import { RemoteLocationExtensionAbility } from '@kit.PushKit'; 
import { hilog } from '@kit.PerformanceAnalysisKit'; 
 
// In the following example, **TestExtAbility** inherits from **RemoteLocationExtensionAbility**:
export default class TestExtAbility extends RemoteLocationExtensionAbility { 
  onDestroy(): void { 
    hilog.info(0x0000, 'testTag', 'TestExtAbility onDestroy'); 
  } 
}
