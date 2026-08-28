# @ohos.app.ability.ChildProcess (Child Process Base Class)

ChildProcess is the base class for you to customize child processes. When starting a child process through [childProcessManager](../ohos-app-ability-childprocessmanager-child-process-management/document.md), you must inherit this class and override the entrypoint method.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/yVaIt_DtTHSwzg1LbGZW3A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062204Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5C248362DCA7F6AA0E28C4C75F2A19D07AD4474464B9F039CE9D28CBE9588D0B)

The initial APIs of this module are supported since API version 11. Newly added APIs will be marked with a superscript to indicate their earliest API version.

The APIs of this module can be used only in the stage model.

#### Modules to Import

import { ChildProcess } from '@kit.AbilityKit';

#### ChildProcess.onStart

onStart(args?: ChildProcessArgs): void

Entrypoint method of the child process. This callback is triggered when the child process is started through [childProcessManager](../ohos-app-ability-childprocessmanager-child-process-management/document.md).

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| args12+ | [ChildProcessArgs](../ohos-app-ability-childprocessargs-child-process-arguments/document.md) | No | Parameters transferred to the child process. |

**Example**

import { ChildProcess, ChildProcessArgs } from '@kit.AbilityKit';

export default class DemoProcess extends ChildProcess {

  onStart(args?: ChildProcessArgs) {
    let entryParams = args?.entryParams;
    let fd = args?.fds?.key1;
    // ..
  }
}
