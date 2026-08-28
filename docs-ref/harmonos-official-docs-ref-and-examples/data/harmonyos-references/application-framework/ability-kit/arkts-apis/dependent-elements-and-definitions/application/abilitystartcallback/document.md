# AbilityStartCallback

The module describes the callback invoked to return the UIExtensionAbility startup result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/8S8JwgvCQ8y2K6oeamph-g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062209Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AD8FF6AFE38A5B9A678B0706C0A5C40B4F19DD454B93C244918F1922755C84C0)

The initial APIs of this module are supported since API version 11. Newly added APIs will be marked with a superscript to indicate their earliest API version.

The APIs of this module can be used only in the stage model.

Since API version 11, the APIs of this module are supported in atomic services.

#### Modules to Import

import { common } from '@kit.AbilityKit';

#### AbilityStartCallback

#### \[h2\]Properties

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| completionHandler21+ | [CompletionHandlerForAbilityStartCallback](../../../stage-model/ohos-app-ability-completionhandlerforabilitystartcallback-application-launch-res/document.md) | No | Yes | 
Callback invoked when the ability of a specified type is started.

**Atomic service API**: This API can be used in atomic services since API version 21.

 |

#### \[h2\]onError

onError(code: number, name: string, message: string): void

Called when the UIExtensionAbility fails to start.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| code | number | Yes | Result code returned when the UIExtensionAbility fails to start. |
| name | string | Yes | Name returned when the UIExtensionAbility fails to start. |
| message | string | Yes | Error information returned when the UIExtensionAbility fails to start. |

**Example**

import { UIAbility, common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onForeground() {
    let wantParam: Record<string, Object> = {
      'time': '2023-10-23 20:45',
    };
    let abilityStartCallback: common.AbilityStartCallback = {
      onError: (code: number, name: string, message: string) => {
        console.info(\`code: ${code}, name: ${name}, message: ${message}\`);
      },
      onResult: (abilityResult: common.AbilityResult) => {
        console.info(\`resultCode: ${abilityResult.resultCode}, bundleName: ${abilityResult.want?.bundleName}\`);
      }
    };

    this.context.startAbilityByType('photoEditor', wantParam, abilityStartCallback, (err: BusinessError) => {
      if (err) {
        console.error(\`startAbilityByType fail, err: ${JSON.stringify(err)}\`);
      } else {
        console.info(\`success\`);
      }
    });
  }
}

#### \[h2\]onResult12+

onResult?(parameter: AbilityResult): void

Called when the UIExtensionAbility is terminated.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| parameter | [AbilityResult](../../ability/abilityresult/document.md) | Yes | Result returned when [terminateSelfWithResult](../uiextensioncontext/document.md#terminateselfwithresult12) is called to terminate the UIExtensionAbility. |

**Example**

import { UIAbility, common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onForeground() {
    let wantParam: Record<string, Object> = {
      'time': '2023-10-23 20:45',
    };
    let abilityStartCallback: common.AbilityStartCallback = {
      onError: (code: number, name: string, message: string) => {
        console.info(\`code:\` + code + \`name:\` + name + \`message:\` + message);
      },
      onResult: (abilityResult: common.AbilityResult) => {
        console.info(\`resultCode:\` + abilityResult.resultCode + \`bundleName:\` + abilityResult.want?.bundleName);
      }
    };

    this.context.startAbilityByType('photoEditor', wantParam, abilityStartCallback, (err: BusinessError) => {
      if (err) {
        console.error(\`startAbilityByType fail, err: ${JSON.stringify(err)}\`);
      } else {
        console.info(\`success\`);
      }
    });
  }
}
