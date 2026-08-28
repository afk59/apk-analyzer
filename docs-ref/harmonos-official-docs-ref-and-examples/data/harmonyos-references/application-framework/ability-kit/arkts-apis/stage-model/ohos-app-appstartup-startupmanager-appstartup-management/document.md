# @ohos.app.appstartup.startupManager (AppStartup Management)

The module provides the capability to manage startup tasks in [AppStartup](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-startup). The APIs of this module can be called only on the main thread.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/qT0GWIa5QYqZSSsoLak_1w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062206Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=712E762ED5272EA3B93D838E42A87CB87F81BAAAF5C525F8C319C3220C7FBD11)

The initial APIs of this module are supported since API version 12. Newly added APIs will be marked with a superscript to indicate their earliest API version.

This module supports .so file preloading since API version 18.

The APIs of this module can be used only in the stage model.

#### Modules to Import

import { startupManager }  from '@kit.AbilityKit';

#### startupManager.run

run(startupTasks: Array<string>, config?: StartupConfig): Promise<void>

Runs startup tasks or loads .so files.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/H9V_G05QQPm9wUlCrEmDWQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062206Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=083B2993C4AB515F112FC0B05BDB7F4DEEC4BD3DE63DD404A0344C7567206F2A)

This API cannot be used to run startup tasks defined in a feature-type HAP. To run those tasks, use [startupManager.run](#startupmanagerrun20).

**System capability**: SystemCapability.Ability.AppStartup

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| startupTasks | Array<string> | Yes | Array of [StartupTask](../ohos-app-appstartup-startuptask-appstartup-task/document.md) names or names of .so files to be preloaded. |
| config | [StartupConfig](../ohos-app-appstartup-startupconfig-appstartup-configuration/document.md) | No | Configuration for the timeout duration and listener of startup tasks in AppStartup. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Ability Error Codes](../../../error-codes/ability-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 16000050 | Internal error. |
| 28800001 | Startup task or its dependency not found. |
| 28800002 | The startup tasks have circular dependencies. |
| 28800003 | An error occurred while running the startup tasks. |
| 28800004 | Running startup tasks timeout. |

**Example**

import { AbilityConstant, UIAbility, Want, startupManager } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');
    let startParams = \['StartupTask\_001', 'libentry\_001'\];
    try {
      // Manually call the run method.
      startupManager.run(startParams).then(() => {
        console.info(\`StartupTest startupManager run then, startParams = ${startParams}.\`);
      }).catch((error: BusinessError) => {
        console.error(\`StartupTest promise catch failed, error code: ${error.code}, error msg: ${error.message}.\`);
      });
    } catch (error) {
      let errMsg = (error as BusinessError).message;
      let errCode = (error as BusinessError).code;
      console.error(\`Startup.run failed, err code: ${errCode}, err msg: ${errMsg}.\`);
    }
  }

  // ...
}

#### startupManager.run20+

run(startupTasks: Array<string>, context: common.AbilityStageContext, config: StartupConfig): Promise<void>

Runs startup tasks or loads .so files. You can specify [AbilityStageContext](../../dependent-elements-and-definitions/application/abilitystagecontext/document.md) for loading startup tasks. This API uses a promise to return the result.

**System capability**: SystemCapability.Ability.AppStartup

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| startupTasks | Array<string> | Yes | Array of [StartupTask](../ohos-app-appstartup-startuptask-appstartup-task/document.md) names or names of .so files to be preloaded. |
| context | [common.AbilityStageContext](../../dependent-elements-and-definitions/application/abilitystagecontext/document.md) | Yes | AbilityStage context that executes the [StartupTask](../ohos-app-appstartup-startuptask-appstartup-task/document.md). It is passed as an input parameter to [init](../ohos-app-appstartup-startuptask-appstartup-task/document.md#init) of the task. |
| config | [StartupConfig](../ohos-app-appstartup-startupconfig-appstartup-configuration/document.md) | Yes | Configuration for the timeout duration and listener of startup tasks in AppStartup. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Ability Error Codes](../../../error-codes/ability-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 16000050 | Internal error. |
| 28800001 | Startup task or its dependency not found. |
| 28800002 | The startup tasks have circular dependencies. |
| 28800003 | An error occurred while running the startup tasks. |
| 28800004 | Running startup tasks timeout. |

**Example**

import { AbilityStage, startupManager, StartupListener, StartupConfig } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class MyAbilityStage extends AbilityStage {
  onCreate(): void {
    hilog.info(0x0000, 'testTag', 'AbilityStage onCreate');
    let onCompletedCallback = (error: BusinessError<void>) => {
      if (error) {
        hilog.error(0x0000, 'testTag', 'onCompletedCallback error: %{public}s', JSON.stringify(error));
      } else {
        hilog.info(0x0000, 'testTag', 'onCompletedCallback: success.');
      }
    };
    let startupListener: StartupListener = {
      'onCompleted': onCompletedCallback
    };
    let config: StartupConfig = {
      'timeoutMs': 10000,
      'startupListener': startupListener
    };

    try {
      // Manually call the run method.
      startupManager.run(\['StartupTask\_001', 'libentry\_001'\], this.context, config).then(() => {
        hilog.info(0x0000, 'testTag', '%{public}s', 'startupManager.run success');
      }).catch((error: BusinessError<void>) => {
        hilog.error(0x0000, 'testTag', 'startupManager.run promise catch error: %{public}s', JSON.stringify(error));
      })
    } catch (error) {
      hilog.error(0x0000, 'testTag', 'startupManager.run catch error: %{public}s', JSON.stringify(error));
    }
  }
  // ...
}

#### startupManager.removeAllStartupTaskResults

removeAllStartupTaskResults(): void

Removes all startup task results.

If there are preloading tasks for .so files, the corresponding .so files is set to the unloaded state. However, .so files that have already been loaded in the cache will not be removed.

**System capability**: SystemCapability.Ability.AppStartup

**Example**

import { AbilityConstant, UIAbility, Want, startupManager } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');
    try {
      startupManager.run(\['StartupTask\_001', 'libentry\_001'\]).then(() => {
        hilog.info(0x0000, 'testTag', 'StartupTask\_001 init successful');
      }).catch((error: BusinessError) => {
        hilog.error(0x0000, 'testTag', \`StartupTask\_001 promise catch failed, error: %{public}s\`,
          JSON.stringify(error) ?? '');
      });
    } catch (error) {
      hilog.error(0x0000, 'testTag', \`StartupTask\_001.run failed, error: %{public}s\`, JSON.stringify(error) ?? '');
    }
  }

  onWindowStageCreate(windowStage: window.WindowStage) {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');
    startupManager.removeAllStartupTaskResults(); // Remove all startup task results.

    windowStage.loadContent('pages/Index', (err, data) => {
      if (err.code) {
        hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
        return;
      }
      hilog.info(0x0000, 'testTag', 'Succeeded in loading the content. Data: %{public}s', JSON.stringify(data) ?? '');
    });
  }
}

#### startupManager.getStartupTaskResult

getStartupTaskResult(startupTask: string): Object

Obtains the execution result of a startup task or .so file preloading task.

**System capability**: SystemCapability.Ability.AppStartup

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| startupTask | string | Yes | Name of the [StartupTask](../ohos-app-appstartup-startuptask-appstartup-task/document.md) or name of the .so file to be preloaded. |

**Return value**

| Type | Description |
| :-- | :-- |
| Object | 
Execution result of [init](../ohos-app-appstartup-startuptask-appstartup-task/document.md#init) of the startup task if a startup task name is passed.

undefined if a .so file name is passed.

 |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**Example**

import { AbilityConstant, UIAbility, Want, startupManager } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');
    try {
      startupManager.run(\['StartupTask\_001'\]).then(() => {
        hilog.info(0x0000, 'testTag', 'StartupTask\_001 init successful');
      }).catch((error: BusinessError) => {
        hilog.error(0x0000, 'testTag', \`StartupTask\_001 promise catch failed, error: %{public}s\`,
          JSON.stringify(error) ?? '');
      });
    } catch (error) {
      hilog.error(0x0000, 'testTag', \`StartupTask\_001.run failed, error: %{public}s\`, JSON.stringify(error) ?? '');
    }
  }

  onWindowStageCreate(windowStage: window.WindowStage) {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');
    let result = startupManager.getStartupTaskResult('StartupTask\_001'); // Manually obtain the startup task result.
    hilog.info(0x0000, 'testTag', 'getStartupTaskResult result = %{public}s', result);
    windowStage.loadContent('pages/Index', (err, data) => {
      if (err.code) {
        hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
        return;
      }
      hilog.info(0x0000, 'testTag', 'Succeeded in loading the content. Data: %{public}s', JSON.stringify(data) ?? '');
    });
  }
}

#### startupManager.isStartupTaskInitialized

isStartupTaskInitialized(startupTask: string): boolean

Checks whether a startup task or .so file preloading task is initialized.

**System capability**: SystemCapability.Ability.AppStartup

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| startupTask | string | Yes | Name of the [StartupTask](../ohos-app-appstartup-startuptask-appstartup-task/document.md) or name of the .so file to be preloaded. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result for whether the task is initialized. **true** if initialized, **false** otherwise. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**Example**

import { AbilityConstant, UIAbility, Want, startupManager } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');
    try {
      startupManager.run(\['StartupTask\_001', 'libentry\_001'\]).then(() => {
      hilog.info(0x0000, 'testTag', 'StartupTask\_001 init successful');
      }).catch((error: BusinessError) => {
        hilog.error(0x0000, 'testTag', \`StartupTask\_001 promise catch failed, error: %{public}s\`,
          JSON.stringify(error) ?? '');
      });
    } catch (error) {
      hilog.error(0x0000, 'testTag', \`StartupTask\_001.run failed, error: %{public}s\`, JSON.stringify(error) ?? '');
    }
  }

  onWindowStageCreate(windowStage: window.WindowStage) {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');
    let result1 = startupManager.isStartupTaskInitialized('StartupTask\_001');
    let result2 = startupManager.isStartupTaskInitialized('libentry\_001');
    if (result1) {
      console.info('StartupTask\_001 init successful');
    } else {
      console.info('StartupTask\_001 uninitialized');
    }
    if (result2) {
      console.info('libentry\_001 init successful');
    } else {
      console.info('libentry\_001 uninitialized');
    }

    windowStage.loadContent('pages/Index', (err, data) => {
      if (err.code) {
        hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
        return;
      }
      hilog.info(0x0000, 'testTag', 'Succeeded in loading the content. Data: %{public}s', JSON.stringify(data) ?? '');
    });
  }
}

#### startupManager.removeStartupTaskResult

removeStartupTaskResult(startupTask: string): void

Removes the initialization result of a startup task or .so file preloading task.

-   If a startup task name is passed, the initialization result of that startup task is removed.
    
-   If a .so file is passed, the .so file is set to the unloaded state, but the loaded .so file in the cache is not removed.
    

**System capability**: SystemCapability.Ability.AppStartup

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| startupTask | string | Yes | Name of the [StartupTask](../ohos-app-appstartup-startuptask-appstartup-task/document.md) or name of the .so file to be preloaded. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**Example**

import { AbilityConstant, UIAbility, Want, startupManager } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');
    try{
      startupManager.run(\['StartupTask\_001', 'libentry\_001'\]).then(() => {
        hilog.info(0x0000, 'testTag', 'StartupTask\_001 init successful');
      }).catch((error: BusinessError) => {
        hilog.error(0x0000, 'testTag', \`StartupTask\_001 promise catch failed, error: %{public}s\`,
          JSON.stringify(error) ?? '');
      });
    } catch (error) {
      hilog.error(0x0000, 'testTag', \`StartupTask\_001.run failed, error: %{public}s\`, JSON.stringify(error) ?? '');
    }
  }

  onWindowStageCreate(windowStage: window.WindowStage) {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');
    startupManager.removeStartupTaskResult('StartupTask\_001');
    startupManager.removeStartupTaskResult('libentry\_001');

    windowStage.loadContent('pages/Index', (err, data) => {
      if (err.code) {
        hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
        return;
      }
      hilog.info(0x0000, 'testTag', 'Succeeded in loading the content. Data: %{public}s', JSON.stringify(data) ?? '');
    });
  }
}
