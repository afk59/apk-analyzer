# @ohos.WorkSchedulerExtensionAbility (Deferred Task Scheduling Callbacks)

The **WorkSchedulerExtensionAbility** module provides callbacks for deferred task scheduling. You can override the APIs provided by this module. When a deferred task is triggered, the system calls back the application through the APIs and processes the task logic in the callback.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/S35SlbdzQBOyeTlFTnK0-A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062318Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DEEDFB6EE1C64C1557E6FD9D12296CC38837040473C1844490732B5324E5670E)

-   The initial APIs of this module are supported since API version 9. Newly added APIs will be marked with a superscript to indicate their earliest API version.
    
-   The APIs of this module can be used only in the stage model.
    

#### Modules to Import

import { WorkSchedulerExtensionAbility } from '@kit.BackgroundTasksKit';

#### WorkSchedulerExtensionContext10+

type WorkSchedulerExtensionContext = \_WorkSchedulerExtensionContext

**WorkSchedulerExtensionContext** represents the context of **WorkSchedulerExtensionAbility** and is inherited from [ExtensionContext](../../../ability-kit/arkts-apis/dependent-elements-and-definitions/application/extensioncontext/document.md).

**System capability**: SystemCapability.ResourceSchedule.WorkScheduler

| Type | Description |
| :-- | :-- |
| [\_WorkSchedulerExtensionContext](../application/workschedulerextensioncontext/document.md) | Context of the **WorkSchedulerExtension**. |

#### WorkSchedulerExtensionAbility

Provides callbacks to be invoked when the scheduling conditions are met or the scheduling ends, for example, [onWorkStart()](#onworkstart) or [onWorkStop()](#onworkstop) in **WorkSchedulerExtensionAbility**.

#### \[h2\]Properties

**System capability**: SystemCapability.ResourceSchedule.WorkScheduler

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| context10+ | [WorkSchedulerExtensionContext](../application/workschedulerextensioncontext/document.md) | No | No | Context of the **WorkSchedulerExtensionAbility**. This context inherits from **ExtensionContext**. |

#### \[h2\]onWorkStart

onWorkStart(work: workScheduler.WorkInfo): void

Called when the system starts scheduling the deferred task.

**System capability**: SystemCapability.ResourceSchedule.WorkScheduler

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| work | [workScheduler.WorkInfo](../ohos-resourceschedule-workscheduler-deferred-task-scheduling/document.md#workinfo) | Yes | Deferred task that starts. |

**Example**

import { workScheduler } from '@kit.BackgroundTasksKit';
import { WorkSchedulerExtensionAbility } from '@kit.BackgroundTasksKit';

export default class MyWorkSchedulerExtensionAbility extends WorkSchedulerExtensionAbility {
  onWorkStart(workInfo: workScheduler.WorkInfo) {
      console.info(\`MyWorkSchedulerExtensionAbility onWorkStart, workId: ${workInfo.workId},
          bundleName: ${workInfo.bundleName}, abilityName: ${workInfo.abilityName}.\`);
  }
}

#### \[h2\]onWorkStop

onWorkStop(work: workScheduler.WorkInfo): void

Called when the system stops scheduling the deferred task. This callback is triggered when the deferred task times out for 2 minutes or the [stopWork](../ohos-resourceschedule-workscheduler-deferred-task-scheduling/document.md#workschedulerstopwork) API is called to cancel the task.

**System capability**: SystemCapability.ResourceSchedule.WorkScheduler

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| work | [workScheduler.WorkInfo](../ohos-resourceschedule-workscheduler-deferred-task-scheduling/document.md#workinfo) | Yes | Deferred task that stops. |

**Example**

import { workScheduler } from '@kit.BackgroundTasksKit';
import { WorkSchedulerExtensionAbility } from '@kit.BackgroundTasksKit';

export default class MyWorkSchedulerExtensionAbility extends WorkSchedulerExtensionAbility {
  onWorkStop(workInfo: workScheduler.WorkInfo) {
      console.info(\`MyWorkSchedulerExtensionAbility onWorkStop, workId: ${workInfo.workId},
          bundleName: ${workInfo.bundleName}, abilityName: ${workInfo.abilityName}.\`);
  }
}
