# VpnExtensionContext

**VpnExtensionContext** represents the context of **VpnExtensionAbility** and is inherited from [ExtensionContext](../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/extensioncontext/document.md).

This module provides the context required for APIs to access the resources of a **VpnExtensionAbility** object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/C6rojlElSz2tpETH5ZvsRA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062346Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7EE0CB9E48B8396EAA46C7BB70DE3CCB25B33D5AFBECA2B450A97A243304E356)

The initial APIs of this module are supported since API version 11. Newly added APIs will be marked with a superscript to indicate their earliest API version.

The APIs of this module can be used only in the stage model.

#### Modules to Import

import { VpnExtensionAbility } from '@kit.NetworkKit';

#### How to Use

You can obtain a **VpnExtensionContext** object through a **VpnExtensionAbility** child class instance.

import { VpnExtensionAbility, vpnExtension } from '@kit.NetworkKit';
import { Want } from '@kit.AbilityKit';

export default class MyVpnExtAbility extends VpnExtensionAbility {
  private vpnServerIp: string = 'xxx.xxx.x.x';
  private tunIp: string = 'x.x.x.x';
  private blockedAppName: string = 'xxxx';

  onCreate(want: Want) {
    let VpnConnection: vpnExtension.VpnConnection = vpnExtension.createVpnConnection(this.context);
    console.info("vpn createVpnConnection: " + JSON.stringify(VpnConnection));
  }
}

#### VpnExtensionAbility

Represents the VPN extension capability.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core.

**Model restriction**: This API can be used only in the stage model.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| context | [VpnExtensionContext](#) | No | No | Specified context. |

## onCreate

onCreate(want: Want): void

Represents the callback triggered when the extended VPN is initialized.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/ZlF4iAEORAyA24XAarn6gg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062346Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B7B3FEAA55064F371BCC2AA74CB39E7CD745C4691762BF472CD77CC1C802B21E)

You are advised to call [onDestroy](#ondestroy) to listen to the destruction of the extended VPN and clear resources in a timely manner.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core.

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| want | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | Want information. |

## onDestroy

onDestroy(): void

Represents the callback triggered when the extended VPN is destroyed.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core.

**Model restriction**: This API can be used only in the stage model.
