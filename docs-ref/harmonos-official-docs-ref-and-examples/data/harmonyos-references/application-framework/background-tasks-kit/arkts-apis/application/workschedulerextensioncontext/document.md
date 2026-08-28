# WorkSchedulerExtensionContext

The **WorkSchedulerExtensionContext** module, inherited from [ExtensionContext](../../../../ability-kit/arkts-apis/dependent-elements-and-definitions/application/extensioncontext/document.md), provides a context environment for the **WorkSchedulerExtensionAbility**.

This module provides APIs for accessing the resources of a **WorkSchedulerExtensionAbility**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/4GHhBp8tQV-JFn9Fri_oxw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062318Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=13DF0F34E4B94D3612FBDABED5E9F51C6C2772A264159AA222135A9FC0A2F12E)

-   The initial APIs of this module are supported since API version 10. Newly added APIs will be marked with a superscript to indicate their earliest API version.
-   The APIs of this module can be used only in the stage model.

#### How to Use

Obtain the context through a **WorkSchedulerExtensionAbility** child class instance.

import { WorkSchedulerExtensionAbility, workScheduler } from '@kit.BackgroundTasksKit';

class MyWorkSchedulerExtensionAbility extends WorkSchedulerExtensionAbility {
    onWorkStart(workInfo: workScheduler.WorkInfo) {
        let WorkSchedulerExtensionContext = this.context; // Obtain the WorkSchedulerExtensionContext.
    }
}

#### WorkSchedulerExtensionContext

Provides a context environment for the **WorkSchedulerExtensionAbility**.

**System capability**: SystemCapability.ResourceSchedule.WorkScheduler

**Model restriction**: This API can be used only in the stage model.
