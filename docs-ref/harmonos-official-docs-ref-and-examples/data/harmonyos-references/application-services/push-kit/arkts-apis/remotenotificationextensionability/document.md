# RemoteNotificationExtensionAbility

**RemoteNotificationExtensionAbility** provides callbacks for obtaining scenario-specific message data and ending the lifecycle. The restrictions are as follows:

-   **RemoteNotificationExtensionAbility** is a lightweight, independent subprocess. The main process cannot be woken up.
-   The notification APIs, widget APIs, window APIs, pop-up APIs, and live view APIs cannot be called.
-   The lifecycle is controlled based on scenarios and is less than 10 seconds by default. If the 10-second period expires, the subprocess lifecycle ends.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Push.PushService

**Start version**: 4.1.0(11)

#### Module Import

import { RemoteNotificationExtensionAbility } from '@kit.PushKit';

#### Attributes

**Model restriction**: The attributes can be used only in the stage model.

**System capability**: SystemCapability.Push.PushService

**Device behavior differences**: For versions earlier than 5.1.0(18), this attribute is supported on phones, tablets, and PCs/2-in-1 devices, but does not work on other devices. For version 5.1.0(18) or later, this attribute is supported on phones, tablets, PCs/2-in-1 devices, and wearables, but does not work on other devices.

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

[RemoteNotificationExtensionContext](../remotenotificationextensioncontext/document.md)

 | 

No

 | 

No

 | 

Context of **RemoteNotificationExtensionAbility**, which inherits from [ExtensionContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/extensioncontext/document.md).

 |

#### onReceiveMessage

onReceiveMessage(remoteNotificationInfo: pushCommon.RemoteNotificationInfo): Promise<pushCommon.RemoteNotificationContent>

Receives notification extension data after an app inherits from **RemoteNotificationExtensionAbility**. This API returns the result asynchronously through a promise.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Push.PushService

**Device behavior differences**: For versions earlier than 5.1.0(18), this API is supported on phones, tablets, and PCs/2-in-1 devices, but does not work on other devices. For version 5.1.0(18) or later, this API is supported on phones, tablets, PCs/2-in-1 devices, and wearables, but does not work on other devices.

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

remoteNotificationInfo

 | 

pushCommon.[RemoteNotificationInfo](../pushcommon/document.md#section5154112615120)

 | 

Yes

 | 

Notification extension data.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<pushCommon.[RemoteNotificationContent](../pushcommon/document.md#section155703491918)\>

 | 

Promise object, which returns the new content of an extended notification.

 |

**Example**:

import { RemoteNotificationExtensionAbility, pushCommon } from '@kit.PushKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

// In the following example, **RemoteNotificationExtAbility** inherits from **RemoteNotificationExtensionAbility**:
export default class RemoteNotificationExtAbility extends RemoteNotificationExtensionAbility {
  async onReceiveMessage(remoteNotificationInfo: pushCommon.RemoteNotificationInfo): Promise<pushCommon.RemoteNotificationContent> {
    hilog.info(0x0000, 'testTag', 'TestExtAbility onReceiveMessage');
    return {
      title: 'Default replace title.',
      text: 'Default replace text.',
      badgeNumber: 1,
      wantAgent: {
        abilityName: 'DemoAbility',
        parameters: {
          key: 'Default value'
        }
      }
    }
  }  
}

#### onDestroy

onDestroy(): void

This callback is executed when the **RemoteNotificationExtensionAbility** lifecycle ends. You are advised to clear resources in this method.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Push.PushService

**Device behavior differences**: For versions earlier than 5.1.0(18), this API is supported on phones, tablets, and PCs/2-in-1 devices, but does not work on other devices. For version 5.1.0(18) or later, this API is supported on phones, tablets, PCs/2-in-1 devices, and wearables, but does not work on other devices.

**Start version**: 4.1.0(11)

**Example**:

import { RemoteNotificationExtensionAbility } from '@kit.PushKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
 
// In the following example, **RemoteNotificationExtAbility** inherits from **RemoteNotificationExtensionAbility**:
export default class RemoteNotificationExtAbility extends RemoteNotificationExtensionAbility {
  onDestroy(): void { 
    hilog.info(0x0000, 'testTag', 'RemoteNotificationExtAbility onDestroy.'); 
  } 
}
