# LoopObserver

The module defines an observer to listen for event processing timeout. It can be used as an input parameter in [ErrorManager.on](../../../both-models-recommended/ohos-app-ability-errormanager-error-management-module/document.md#errormanageronloopobserver12) to listen for the event processing timeout of the current application's main thread.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/4ZEy8vKjQeiFS9OadH5B9w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062209Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BC20380234DD3C544CAC9122F05468BFD139B214CD85643ECED4515B334AC4CE)

The initial APIs of this module are supported since API version 12. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { errorManager } from '@kit.AbilityKit';

#### LoopObserver.onLoopTimeOut

onLoopTimeOut?(timeout: number): void

Called when a timeout occurs for the main thread to process an event in the JS runtime.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| timeout | number | Yes | Actual execution time of the main thread. |

**Example**

import { errorManager } from '@kit.AbilityKit';

let observer: errorManager.LoopObserver = {
  onLoopTimeOut(timeout: number) {
    console.info('Duration timeout: ' + timeout);
  }
};

errorManager.on("loopObserver", 1, observer);
