# AbilityStageMonitor

The module provides the capability to listen for a specified [AbilityStage](../../../stage-model/ohos-app-ability-abilitystage-abilitystage-component-manager/document.md) object. You can use AbilityStageMonitor as an input parameter of [abilityDelegator.waitAbilityStageMonitor](../../../../../../system/debugging-tools/test-kit/arkts-api/dependent-elements-and-definitions/abilitydelegator/document.md#waitabilitystagemonitor9) to register a listener.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/XynKGpyUTM2ls8tuxoMTNA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062209Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=58EFE7AD61A9C7B57B27798AC01CDE34220E9F1BA19665073A13E1B5436087A6)

The initial APIs of this module are supported since API version 9. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### AbilityStageMonitor

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| moduleName | string | No | No | Module name of the AbilityStage object. |
| srcEntrance | string | No | No | Source path of the AbilityStage object. |

**Example**

import { abilityDelegatorRegistry } from '@kit.TestKit';

let monitor: abilityDelegatorRegistry.AbilityStageMonitor = {
  moduleName: 'feature\_as1',
  srcEntrance: './ets/Application/MyAbilityStage.ts',
}

let abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.waitAbilityStageMonitor(monitor, (error, data) => {
  if (error) {
    console.error(\`waitAbilityStageMonitor fail, error: ${JSON.stringify(error)}\`);
  } else {
    console.info(\`waitAbilityStageMonitor success, data: ${JSON.stringify(data)}\`);
  }
});
