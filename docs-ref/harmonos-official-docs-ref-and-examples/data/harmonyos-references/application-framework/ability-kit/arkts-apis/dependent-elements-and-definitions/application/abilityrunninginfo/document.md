# AbilityRunningInfo

AbilityRunningInfo is a struct that records the running information and state of an ability. It is obtained through [getAbilityRunningInfos](../../../both-models-recommended/ohos-app-ability-abilitymanager-ability-information-management/document.md#abilitymanagergetabilityrunninginfos14).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/OnYFx8IzSuqJQhTRfy41Tw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062209Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=95364FD69CA8F5FC3592EF8622717971086832C05D8DEEBD2C06E6BF1AC3477A)

The initial APIs of this module are supported since API version 14. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { abilityManager } from '@kit.AbilityKit';

#### AbilityRunningInfo

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| ability | [ElementName](../../bundlemanager/elementname/document.md) | No | No | Element name of the ability. |
| pid | number | No | No | Process ID. |
| uid | number | No | No | UID of the application. |
| processName | string | No | No | Process name. |
| startTime | number | No | No | Ability start time. |
| abilityState | [abilityManager.AbilityState](../../../both-models-recommended/ohos-app-ability-abilitymanager-ability-information-management/document.md#abilitystate14) | No | No | Ability state. |

**Example**

import { abilityManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  abilityManager.getAbilityRunningInfos()
    .then((data: abilityManager.AbilityRunningInfo\[\]) => {
      for (let i = 0; i < data.length; i++) {
        let abilityInfo = data\[i\];
        console.info(\`getAbilityRunningInfos success, data: ${JSON.stringify(abilityInfo)}\`);
      }
    })
    .catch((error: BusinessError) => {
      console.error(\`getAbilityRunningInfos fail, error code: ${JSON.stringify(error.code)}, error msg: ${JSON.stringify(error.message)}\`);
    })
} catch (e) {
  let code = (e as BusinessError).code;
  let msg = (e as BusinessError).message;
  console.error(\`getAbilityRunningInfos fail, error code: ${JSON.stringify(code)}, error msg: ${JSON.stringify(msg)}\`);
}
