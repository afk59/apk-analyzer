# @ohos.net.policy (Network Policy Management)

The **policy** module provides APIs for managing network policies, which allow you to use firewall technology to control and manage the data traffic used.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/VFebAwxKR1qICtluZp6S5Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C43DCCF409D85EED8C819F22F88F1FF9A6FEE2779313DF6A564475CD71CAFDC8)

The initial APIs of this module are supported since API version 10. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { policy } from '@kit.NetworkKit';

#### NetBearType

type NetBearType = connection.NetBearType

Network type.

**System capability**: SystemCapability.Communication.NetManager.Core

| Type | Description |
| :-- | :-- |
| [connection.NetBearType](../ohos-net-connection-network-connection-management/document.md#netbeartype) | Network type. |

#### policy.showAppNetPolicySettings22+

showAppNetPolicySettings(context: Context): Promise<void>

This API is used to set whether the current application can connect to the Wi-Fi or cellular network. You can call this API to open the network connection settings screen of the current app and set the network connection permission of the application. This API uses a promise to return the result.

**System capability**: SystemCapability.Communication.NetManager.Core

**Model restriction**: This API can be used only in the stage model.

**Device behavior differences**: This API can be called on phones, 2-in-1 devices, and tablets, but does not take effect on other devices.

**Parameters**

| **Name** | Type | **Mandatory** | Description |
| :-- | :-- | :-- | :-- |
| context | [Context](../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md) | Yes | Application context of the stage model. (Only UIAbilityContext and ExtensionContext are supported.) |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise used to return the result. Promise that returns no value. |

**Example:**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/azypKEnCQCqQ43LPeVE0IA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4B3CB7530FEF8659313D08980ABBC418A40A087C7A4296A78758551BB884D594)

In the sample code provided in this topic, **this.context** is used to obtain **UIAbilityContext**, where **this** indicates a UIAbility instance inherited from **UIAbility**. To use **UIAbilityContext** APIs on pages, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

import { policy } from '@kit.NetworkKit';
import { common } from '@kit.AbilityKit';

let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
policy.showAppNetPolicySettings(context).then(() => {
    console.info("showAppNetPolicySettings success");
}).catch(() => {
    console.error("showAppNetPolicySettings failed");
    }
)
