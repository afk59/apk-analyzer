# @ohos.app.ability.abilityDelegatorRegistry (AbilityDelegatorRegistry)

**AbilityDelegatorRegistry**, a module of the automatic test framework, is used to obtain [AbilityDelegator](../dependent-elements-and-definitions/abilitydelegator/document.md) and [AbilityDelegatorArgs](../dependent-elements-and-definitions/abilitydelegatorargs/document.md) objects. **AbilityDelegator** provides APIs for creating [AbilityMonitor](../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/abilitymonitor/document.md#abilitymonitor-1) objects, which can be used to listen for ability lifecycle changes. **AbilityDelegatorArgs** provides APIs for obtaining test parameters.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/GoiCX5S6QhmBzKLS9OQF4w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062416Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EAE51DFC388E005F1564D8E4928BCBA03D8657774F1399C77E570F8DEB3E5A01)

The initial APIs of this module are supported since API version 9. Newly added APIs will be marked with a superscript to indicate their earliest API version.

The APIs of this module can be used only in [unittest](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/unittest-guidelines).

#### Modules to Import

import { abilityDelegatorRegistry } from '@kit.TestKit';

#### AbilityLifecycleState

Enumerates the ability lifecycle states. It can be used in [getAbilityState(ability)](../dependent-elements-and-definitions/abilitydelegator/document.md#getabilitystate9) of [AbilityDelegator](../dependent-elements-and-definitions/abilitydelegator/document.md) to return different ability lifecycle states.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| UNINITIALIZED | 0 | The ability is in an invalid state. |
| CREATE | 1 | The ability is created. |
| FOREGROUND | 2 | The ability is running in the foreground. |
| BACKGROUND | 3 | The ability is running in the background. |
| DESTROY | 4 | The ability is destroyed. |

#### abilityDelegatorRegistry.getAbilityDelegator

getAbilityDelegator(): AbilityDelegator

Obtains an [AbilityDelegator](../dependent-elements-and-definitions/abilitydelegator/document.md) object.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [AbilityDelegator](../dependent-elements-and-definitions/abilitydelegator/document.md) | [AbilityDelegator](../dependent-elements-and-definitions/abilitydelegator/document.md) object, which can be used to schedule the functionalities of the test framework. |

**Example**

import { abilityDelegatorRegistry } from '@kit.TestKit';
import { Want } from '@kit.AbilityKit';

let abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
let want: Want = {
  bundleName: 'com.example.myapplication',
  abilityName: 'EntryAbility'
};

abilityDelegator.startAbility(want, (err) => {
  if (err) {
    console.error(\`Failed start ability, error: ${JSON.stringify(err)}\`);
  } else {
    console.info('Success start ability.');
  }
});

#### abilityDelegatorRegistry.getArguments

getArguments(): AbilityDelegatorArgs

Obtains an [AbilityDelegatorArgs](../dependent-elements-and-definitions/abilitydelegatorargs/document.md) object.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [AbilityDelegatorArgs](../dependent-elements-and-definitions/abilitydelegatorargs/document.md) | [AbilityDelegatorArgs](../dependent-elements-and-definitions/abilitydelegatorargs/document.md) object, which can be used to obtain test parameters. |

**Example**

import { abilityDelegatorRegistry } from '@kit.TestKit';

let args = abilityDelegatorRegistry.getArguments();
console.info(\`getArguments bundleName: ${args.bundleName}\`);
console.info(\`getArguments parameters: ${JSON.stringify(args.parameters)}\`);
console.info(\`getArguments testCaseNames: ${args.testCaseNames}\`);
console.info(\`getArguments testRunnerClassName: ${args.testRunnerClassName}\`);

#### AbilityDelegator

type AbilityDelegator = \_AbilityDelegator

Represents the **AbilityDelegator** module.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

| Type | Description |
| :-- | :-- |
| [\_AbilityDelegator](../dependent-elements-and-definitions/abilitydelegator/document.md) | The **AbilityDelegator** module. |

#### AbilityDelegatorArgs

type AbilityDelegatorArgs = \_AbilityDelegatorArgs

Represents the **AbilityDelegatorArgs** module.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

| Type | Description |
| :-- | :-- |
| [\_AbilityDelegatorArgs](../dependent-elements-and-definitions/abilitydelegatorargs/document.md) | The **AbilityDelegatorArgs** module. |

#### AbilityMonitor

type AbilityMonitor = \_AbilityMonitor

Represents the **AbilityMonitor** module.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

| Type | Description |
| :-- | :-- |
| [\_AbilityMonitor](../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/abilitymonitor/document.md) | The **AbilityMonitor** module. |

#### ShellCmdResult

type ShellCmdResult = \_ShellCmdResult

Represents the **ShellCmdResult** module.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

| Type | Description |
| :-- | :-- |
| [\_ShellCmdResult](../dependent-elements-and-definitions/shellcmdresult/document.md) | The **ShellCmdResult** module. |

#### AbilityStageMonitor14+

type AbilityStageMonitor = \_AbilityStageMonitor

Represents the **AbilityStageMonitor** module.

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

| Type | Description |
| :-- | :-- |
| [\_AbilityStageMonitor](../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/abilitystagemonitor/document.md) | The **AbilityStageMonitor** module. |
