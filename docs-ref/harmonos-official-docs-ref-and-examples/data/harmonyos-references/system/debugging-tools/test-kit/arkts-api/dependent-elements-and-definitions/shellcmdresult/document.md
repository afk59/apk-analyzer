# ShellCmdResult

The **ShellCmdResult** module provides the shell command execution result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/ScZ1nUqEQiKKKomh5e8YOg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062416Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0600DC326DCEAEA7106580CB37B80C5F38FC140E9A499DD33B0F9350E68556B1)

The initial APIs of this module are supported since API version 8. Newly added APIs will be marked with a superscript to indicate their earliest API version.

The APIs of this module can be used only in [unittest](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/unittest-guidelines).

#### Modules to Import

import { abilityDelegatorRegistry } from '@kit.TestKit';

#### ShellCmdResult

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| stdResult | string | No | No | Standard output of the shell command. |
| exitCode | number | No | No | Result code of the shell command. |

#### Usage

The result is obtained by calling [executeShellCommand](../abilitydelegator/document.md#executeshellcommand) in **abilityDelegator**.

**Example**

import { abilityDelegatorRegistry } from '@kit.TestKit';
import { BusinessError } from '@kit.BasicServicesKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;
let cmd = 'cmd';

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.executeShellCommand(cmd, (error: BusinessError, data) => {
  if (error) {
    console.error(\`executeShellCommand fail, error: ${JSON.stringify(error)}\`);
  } else {
    console.info(\`executeShellCommand success, data: ${JSON.stringify(data)}\`);
  }
});
