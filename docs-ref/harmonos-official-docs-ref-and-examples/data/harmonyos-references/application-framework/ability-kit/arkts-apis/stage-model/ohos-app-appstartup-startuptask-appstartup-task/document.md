# @ohos.app.appstartup.StartupTask (AppStartup Task)

The module provides capabilities related to startup tasks in [AppStartup](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-startup).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/2VwzQvboTu6OqE0Inuc3Vw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062206Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C19AFA69279ADD84679FF0E11304CC5A1DCC7E07458E58329EA1B451F6ACC34E)

The initial APIs of this module are supported since API version 12. Newly added APIs will be marked with a superscript to indicate their earliest API version.

The APIs of this module can be used only in the stage model.

#### Modules to Import

import { StartupTask } from '@kit.AbilityKit';

#### StartupTask

Provides capabilities related to startup tasks. It is decorated by [@Sendable](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-sendable#sendable-decorator).

**Decorator**: @Sendable

#### \[h2\]onDependencyCompleted

onDependencyCompleted?(dependency: string, result: Object): void

Called when the dependent startup task is complete.

**System capability**: SystemCapability.Ability.AppStartup

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| dependency | string | Yes | Name of the dependent startup task. |
| result | Object | Yes | Execution result of [init](#init) of the dependent startup task. |

**Example**

import { StartupTask, common } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

@Sendable
export default class StartupTask\_001 extends StartupTask {
  constructor() {
    super();
  }

  async init(context: common.AbilityStageContext) {
    // ...
  }

  onDependencyCompleted(dependency: string, result: Object): void {
    hilog.info(0x0000, 'testTag', 'StartupTask\_001 onDependencyCompleted, dependency: %{public}s, result: %{public}s',
      dependency, JSON.stringify(result));
    // ...
  }
}

#### \[h2\]init

init(context: AbilityStageContext): Promise<Object | void>

Called when all the dependent startup tasks are complete. You can initialize the startup task in this callback. This API uses a promise to return the result.

**System capability**: SystemCapability.Ability.AppStartup

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | [AbilityStageContext](../../dependent-elements-and-definitions/application/abilitystagecontext/document.md) | Yes | Context environment of the [AbilityStage](../ohos-app-ability-abilitystage-abilitystage-component-manager/document.md). |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Object | void> | Promise used to return the execution result. |

**Example**

import { StartupTask, common } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

@Sendable
export default class StartupTask\_001 extends StartupTask {
  constructor() {
    super();
  }
  async init(context: common.AbilityStageContext) {
    hilog.info(0x0000, 'testTag', 'StartupTask\_001 init.');
    // ...
    
    return "StartupTask\_001";
  }

  onDependencyCompleted(dependency: string, result: Object): void {
    // ...
  }
}
