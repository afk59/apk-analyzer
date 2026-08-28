# @ohos.app.ability.VpnExtensionAbility (Enhanced VPN Management)

This module provides lifecycle callbacks for third-party VPNs, including VPN creation and destruction.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/JitoxErXSMC9j4nCRsjuJw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062346Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A75FEC5DC4FA2D348ADF7E520A8A3AC54778AEDC0BDF48EEE4CB25AA44189BE9)

-   The initial APIs of this module are supported since API version 11. Newly added APIs will be marked with a superscript to indicate their earliest API version.
    
-   The APIs of this module can be used only in the stage model.
    

#### Modules to Import

import { VpnExtensionAbility } from '@kit.NetworkKit';

#### Attributes

**System capability**: SystemCapability.Ability.AbilityRuntime.Core.

| Name | Type | Read-only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| context | [VpnExtensionContext](../vpnextensioncontext/document.md) | No | No | Context of the **VpnExtension**. This context is inherited from **ExtensionContext**. |

#### VpnExtensionAbility.onCreate

onCreate(want: Want): void

Called when the third-party VPN is initialized upon startup.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/UiAvUMVcTpiJvMukvO-u6Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062346Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F70AA3A144E89760509BA19DB0F4D5D73423B8C58C4780DB6A9D75CE333DC06A)

You are advised to call [onDestroy](#vpnextensionabilityondestroy) to listen to the destruction of the third-party VPN and clear resources in a timely manner.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| want | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | Want information. |

**Example**

import { VpnExtensionAbility } from '@kit.NetworkKit';
import { Want } from '@kit.AbilityKit';

class MyVpnExtAbility extends VpnExtensionAbility {
    onCreate(want: Want) {
       console.info('MyVpnExtAbility onCreate');
    }
}

#### VpnExtensionAbility.onDestroy

onDestroy(): void

Called when the third-party VPN is destroyed to clear resources.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Example**

import { VpnExtensionAbility } from '@kit.NetworkKit';

class MyVpnExtAbility extends VpnExtensionAbility {
    onDestroy() {
       console.info('MyVpnExtAbility onDestroy');
    }
}
