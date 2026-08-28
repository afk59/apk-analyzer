# VoIPExtensionAbility

**VoIPExtensionAbility** is the in-app call message extension ability. It inherits from [UIExtensionAbility](../../../../application-framework/ability-kit/arkts-apis/stage-model/ohos-app-ability-uiextensionability-extensionability-with-ui/document.md) and adds a callback for obtaining scenario-specific message data. The restrictions are as follows:

-   **VoIPExtensionAbility** is a lightweight, independent subprocess.
-   The widget APIs cannot be called.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Push.PushService

**Start version**: 4.1.0(11)

#### Module Import

import { VoIPExtensionAbility } from '@kit.PushKit';

#### Attributes

**Model restriction**: The attributes can be used only in the stage model.

**System capability**: SystemCapability.Push.PushService

**Device behavior differences**: This attribute is supported on phones and tablets, but does not work on other devices.

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

[VoIPExtensionContext](../voipextensioncontext/document.md#section4636115714125)

 | 

No

 | 

No

 | 

Context of **VoIPExtensionAbility**, which inherits from [UIExtensionContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiextensioncontext/document.md).

 |

#### onReceiveMessage

onReceiveMessage(voipInfo: pushCommon.VoIPInfo): void

API for receiving in-app call messages after an app inherits from **VoIPExtensionAbility**.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Push.PushService

**Device behavior differences**: This API is supported on phones and tablets, but does not work on other devices.

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

voipInfo

 | 

pushCommon.[VoIPInfo](../pushcommon/document.md#section3437161814585)

 | 

Yes

 | 

VoIP call message data.

 |

**Example**:

import { VoIPExtensionAbility, pushCommon } from '@kit.PushKit'; 
import { hilog } from '@kit.PerformanceAnalysisKit';

export default class VoipExtAbility extends VoIPExtensionAbility { 
  onReceiveMessage(voipInfo: pushCommon.VoIPInfo): void { 
    hilog.info(0x0000, 'testTag', 'TestExtAbility onReceiveMessage'); 
  } 
}
