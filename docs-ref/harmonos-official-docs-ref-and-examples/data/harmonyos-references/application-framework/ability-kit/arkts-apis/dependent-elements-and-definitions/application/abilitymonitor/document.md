# AbilityMonitor

The module provides the capability of listening for lifecycle state changes of a specified [UIAbility](../../../stage-model/ohos-app-ability-uiability-ability-with-ui/document.md). You can use AbilityMonitor as an input parameter of [abilityDelegator.addAbilityMonitor](../../../../../../system/debugging-tools/test-kit/arkts-api/dependent-elements-and-definitions/abilitydelegator/document.md#addabilitymonitor9) to register a listener.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/1_xzFjpOQoSk3BPI1iGvcg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062209Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8DB23BD13E38E4FA87B872B746B1ED62DB5CA91F0A7124CF9472B85259379DEF)

The initial APIs of this module are supported since API version 9. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { abilityDelegatorRegistry } from '@kit.TestKit';

#### Usage

AbilityMonitor can be used as an input parameter of [addAbilityMonitor](../../../../../../system/debugging-tools/test-kit/arkts-api/dependent-elements-and-definitions/abilitydelegator/document.md#addabilitymonitor9) in **abilityDelegator** to listen for lifecycle changes of an ability.

#### AbilityMonitor

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| abilityName | string | No | No | Name of the UIAbility object to be listened. |
| moduleName | string | No | Yes | Module name of the UIAbility object. |
| onAbilityCreate | (ability: [UIAbility](../../../stage-model/ohos-app-ability-uiability-ability-with-ui/document.md)) => void | No | Yes | Callback invoked when the UIAbility object is created. |
| onAbilityForeground | (ability: [UIAbility](../../../stage-model/ohos-app-ability-uiability-ability-with-ui/document.md)) => void | No | Yes | Callback invoked when the UIAbility object transitions to the foreground. |
| onAbilityBackground | (ability: [UIAbility](../../../stage-model/ohos-app-ability-uiability-ability-with-ui/document.md)) => void | No | Yes | Callback invoked when the UIAbility object transitions to the background. |
| onAbilityDestroy | (ability: [UIAbility](../../../stage-model/ohos-app-ability-uiability-ability-with-ui/document.md)) => void | No | Yes | Callback invoked when the UIAbility object is destroyed. |
| onWindowStageCreate | (ability: [UIAbility](../../../stage-model/ohos-app-ability-uiability-ability-with-ui/document.md)) => void | No | Yes | Callback invoked when a WindowStage instance is created. |
| onWindowStageRestore | (ability: [UIAbility](../../../stage-model/ohos-app-ability-uiability-ability-with-ui/document.md)) => void | No | Yes | Callback invoked when the page stack is restored for the target UIAbility during cross-device migration. |
| onWindowStageDestroy | (ability: [UIAbility](../../../stage-model/ohos-app-ability-uiability-ability-with-ui/document.md)) => void | No | Yes | Callback invoked when the WindowStage instance is destroyed. |

**Example**

import { abilityDelegatorRegistry } from '@kit.TestKit';
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

function onAbilityCreateCallback(data: UIAbility) {
  console.info(\`onAbilityCreateCallback, data: ${JSON.stringify(data)}\`);
}

let monitor: abilityDelegatorRegistry.AbilityMonitor = {
  abilityName: 'abilityname',
  moduleName: "moduleName",
  onAbilityCreate: onAbilityCreateCallback
}

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.addAbilityMonitor(monitor, (error: BusinessError) => {
  if (error) {
    console.error(\`addAbilityMonitor fail, error: ${JSON.stringify(error)}\`);
  }
});
