# @ohos.app.ability.ChildProcessOptions (Child Process Startup Options)

The module describes the startup configuration of a child process. When starting a child process through [childProcessManager](../ohos-app-ability-childprocessmanager-child-process-management/document.md), you can configure the startup configuration of the child process through **ChildProcessOptions**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/LewFKnA6SEivZizP79_VLg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062205Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C57FCE006436A745B6BFEE843E6ABE850A7B7997E73479AC3AACE86BC932664F)

The initial APIs of this module are supported since API version 12. Newly added APIs will be marked with a superscript to indicate their earliest API version.

The APIs of this module can be used only in the stage model.

#### Modules to Import

import { ChildProcessOptions } from '@kit.AbilityKit';

#### ChildProcessOptions

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| isolationMode | boolean | No | Yes | Controls the sandbox isolation level and network access permissions of the child process. **true** if the child process runs in an independent sandbox environment and cannot access the network; **false** if the child process shares the sandbox and network environment with the main process. The default value is **false**. |
| isolationUid21+ | boolean | No | Yes | Whether the child process uses an independent UID. **true** if the child process uses an independent UID; **false** if the child process and the main process share the same UID. The default value is **false**. This parameter is valid only when **isolationMode** is set to **true**. |

**Example**

Sample code for the child process:

// Create the child process class DemoProcess.ets in src/main/ets/process of the entry module.
// entry/src/main/ets/process/DemoProcess.ets
import { ChildProcess, ChildProcessArgs } from '@kit.AbilityKit';

export default class DemoProcess extends ChildProcess {
  onStart(args?: ChildProcessArgs) {
    let entryParams = args?.entryParams;
    let fd = args?.fds?.key1;
    // Child process code logic
  }
}

Sample code for the main process:

// Call childProcessManager.startArkChildProcess to start the child process.
// entry/src/main/ets/pages/Index.ets
import { ChildProcessArgs, ChildProcessOptions, childProcessManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import DemoProcess from '../process/DemoProcess';

@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        Text('Click')
          .fontSize(30)
          .fontWeight(FontWeight.Bold)
          .onClick(() => {
            try {
              DemoProcess.toString(); // Call any API of the DemoProcess class to prevent the code from being directly optimized by the compiler because it is not being referenced.
              let options: ChildProcessOptions = {
                isolationMode: false,
                isolationUid: false
              };
              let args: ChildProcessArgs = {
                entryParams: "testParam",
              };
              childProcessManager.startArkChildProcess("entry/ets/process/DemoProcess.ets", args, options)
                .then((pid) => {
                  console.info(\`startChildProcess success, pid: ${pid}\`);
                })
                .catch((err: BusinessError) => {
                  console.error(\`startChildProcess business error, errorCode: ${err.code}, errorMsg:${err.message}\`);
                });
            } catch (err) {
              console.error(\`startChildProcess error, errorCode: ${err.code}, errorMsg:${err.message}\`);
            }
          });
      }
      .width('100%')
    }
    .height('100%')
  }
}
