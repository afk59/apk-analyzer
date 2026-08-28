# @ohos.app.ability.application (Application Utility Class)

You can use this module to manage and obtain the application [context](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/application-context-stage) and control the application process state.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/Hcxlfvb7QkOyyRyacRvdkQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062204Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=71861B4D1F2D673AED49121822F14CC0D4221409F75922E8970D16B90923C2C2)

The initial APIs of this module are supported since API version 12. Newly added APIs will be marked with a superscript to indicate their earliest API version.

The APIs of this module can be used only in the stage model.

#### Modules to Import

import { application } from '@kit.AbilityKit';

#### AppPreloadType22+

Enumerates the preloading types of the current application process.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| UNSPECIFIED | 0 | No preloading has taken place, or the preloaded data has been cleared. |
| TYPE\_CREATE\_PROCESS | 1 | Preloads the process up to the point of process creation completion. |
| TYPE\_CREATE\_ABILITY\_STAGE | 2 | Preloads the process up to the point of [AbilityStage](../ohos-app-ability-abilitystage-abilitystage-component-manager/document.md) creation completion. |
| TYPE\_CREATE\_WINDOW\_STAGE | 3 | Preloads the process up to the point of [WindowStage](../../../../arkui/arkts-api/window-manager/ohos-window-window/interface-windowstage/document.md) creation completion. |

#### application.createModuleContext

createModuleContext(context: Context, moduleName: string): Promise<Context>

Creates the context for a module. The [resourceManager.Configuration](../../../../localization-kit/arkts-apis/ohos-resourcemanager-resource-management/document.md#configuration) in the created module context inherits from the input context, making it convenient for you to access [application resources across HAP/HSP packages](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/resource-categories-and-access#cross-haphsp-resources). This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/LOZkSAl1RQmftptyys5YIA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062204Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2204C39A131D8C1D24ACBAC48293C6550D3A2B990DFB15209BAAE7C197001C92)

Creating a module context involves resource querying and initialization, which can be time-consuming. In scenarios where application fluidity is critical, avoid frequently or repeatedly calling the **createModuleContext** API to create multiple context instances, as this may negatively impact user experience.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | [Context](../../dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md) | Yes | Application context. |
| moduleName | string | Yes | Module name. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[Context](../../dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md)\> | Promise used to return the context created. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |

**Example**

import { AbilityConstant, UIAbility, application, common, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    let moduleContext: common.Context;
    try {
      application.createModuleContext(this.context, 'entry').then((data: Context) => {
        moduleContext = data;
        console.info('createModuleContext success!');
      }).catch((error: BusinessError) => {
        let code: number = (error as BusinessError).code;
        let message: string = (error as BusinessError).message;
        console.error(\`createModuleContext failed, error.code: ${code}, error.message: ${message}\`);
      });
    } catch (error) {
      let code: number = (error as BusinessError).code;
      let message: string = (error as BusinessError).message;
      console.error(\`createModuleContext failed, error.code: ${code}, error.message: ${message}\`);
    }
  }
}

#### application.getApplicationContext14+

getApplicationContext(): ApplicationContext

Obtains the application context. This API provides context access independent of the base class **Context**.

Repeated calls to this API generate a new ApplicationContext object.

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [ApplicationContext](../../dependent-elements-and-definitions/application/applicationcontext-application-context/document.md) | Application context. |

**Error codes**

For details about the error codes, see [Ability Error Codes](../../../error-codes/ability-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 16000050 | Internal error. |

**Example**

import { AbilityConstant, UIAbility, application, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    try {
      let applicationContext = application.getApplicationContext();
    } catch (error) {
      let code: number = (error as BusinessError).code;
      let message: string = (error as BusinessError).message;
      console.error(\`getApplicationContext failed, error.code: ${code}, error.message: ${message}\`);
    }
  }
}

#### application.createPluginModuleContext19+

createPluginModuleContext(context: Context, pluginBundleName: string, pluginModuleName: string): Promise<Context>

Creates the context of a plugin under the current application based on the context, plugin bundle name, and plugin module name, so as to obtain the basic information about the plugin. This API uses a promise to return the result.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | [Context](../../dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md) | Yes | Application context. |
| pluginBundleName | string | Yes | Bundle name of the plugin. |
| pluginModuleName | string | Yes | Module name of the plugin. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[Context](../../dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md)\> | Promise used to return the context created. |

**Example**

import { AbilityConstant, UIAbility, application, common, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    let moduleContext: common.Context;
    try {
      application.createPluginModuleContext(this.context, 'com.example.pluginBundleName', 'pluginModuleName')
        .then((data: Context) => {
          moduleContext = data;
          console.info('createPluginModuleContext success!');
        })
        .catch((error: BusinessError) => {
          let code: number = (error as BusinessError).code;
          let message: string = (error as BusinessError).message;
          console.error(\`createPluginModuleContext failed, error.code: ${code}, error.message: ${message}\`);
        });
    } catch (error) {
      let code: number = (error as BusinessError).code;
      let message: string = (error as BusinessError).message;
      console.error(\`createPluginModuleContext failed, error.code: ${code}, error.message: ${message}\`);
    }
  }
}

#### application.promoteCurrentToCandidateMasterProcess20+

promoteCurrentToCandidateMasterProcess(insertToHead: boolean): Promise<void>

Adds the current process into the [candidate master process](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/ability-terminology#candidate-master-process) list. This API uses a promise to return the result.

When the [master process](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/ability-terminology#master-process) is destroyed and a UIAbility or UIExtensionAbility with **isolationProcess** set to **true** is restarted, the system takes corresponding actions based on whether there is a candidate master process.

-   If a candidate master process exists, the system sets the process at the head of the candidate master process list as the new master process and triggers the [onNewProcessRequest](../ohos-app-ability-abilitystage-abilitystage-component-manager/document.md#onnewprocessrequest11) callback.
-   If no candidate master process exists, the system performs the following operations based on the component type:
    -   For a UIAbility, the system creates an empty process as the master process.
    -   For a UIExtensionAbility, the system first tries to reuse an existing UIExtensionAbility process as the new master process. If no available process exists, it creates an empty process as the master process.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/c9P0MrxVTuaJ4s2Hk6PWrA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062204Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=712AD8128686C26B21E2D7C7B39DB9F6F56DFFB130B01B11933C9EF2C25D6123)

If the current process is already the [master process](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/ability-terminology#master-process), calling this API has no effect and does not generate an error code.

A process can be set as a candidate master process only if it is currently running a component with **isolationProcess** set to **true** or has previously as the main process.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Device behavior differences**: This API can be properly called on PCs/2-in-1 devices and tablets. If it is called on other devices, error code 801 is returned.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| insertToHead | boolean | Yes | Whether to add the current process to the head of the candidate master process list. **true** to add the current process to the head of the list, **false** to add the current process to the tail of the list. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Ability Error Codes](../../../error-codes/ability-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported. |
| 16000115 | The current process cannot be set as a candidate master process. |

**Example**

import { AbilityConstant, UIAbility, application, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    try {
      application.promoteCurrentToCandidateMasterProcess(true)
        .then(() => {
          console.info('promote succeed');
        })
        .catch((err: BusinessError) => {
          console.error(\`promote failed, code is ${err.code}, message is ${err.message}\`);
        });
    } catch (error) {
      let code: number = (error as BusinessError).code;
      let message: string = (error as BusinessError).message;
      console.error(\`promoteCurrentToCandidateMasterProcess failed, error.code: ${code}, error.message: ${message}\`);
    }
  }
}

#### application.demoteCurrentFromCandidateMasterProcess20+

demoteCurrentFromCandidateMasterProcess(): Promise<void>

Removes the current process from the candidate master process list. This API uses a promise to return the result.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Device behavior differences**: This API can be properly called on PCs/2-in-1 devices and tablets. If it is called on other devices, error code 801 is returned.

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Ability Error Codes](../../../error-codes/ability-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported. |
| 16000116 | The current process is already a master process and does not support cancellation. |
| 16000117 | The current process is not a candidate master process and does not support cancellation. |

**Example**

import { AbilityConstant, UIAbility, application, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    try {
      application.demoteCurrentFromCandidateMasterProcess()
        .then(() => {
          console.info('demote succeed');
        })
        .catch((err: BusinessError) => {
          console.error(\`demote failed, code is ${err.code}, message is ${err.message}\`);
        });
    } catch (error) {
      let code: number = (error as BusinessError).code;
      let message: string = (error as BusinessError).message;
      console.error(\`demoteCurrentFromCandidateMasterProcess failed, error.code: ${code}, error.message: ${message}\`);
    }
  }
}

#### application.exitMasterProcessRole21+

exitMasterProcessRole(): Promise<void>

Relinquishes the [master-process](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/ability-terminology#master-process) role from the current process. This API uses a promise to return the result.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Device behavior differences**: This API can be properly called only on 2-in-1 devices and tablets. If it is called on other device types, error code 801 is returned.

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Ability Error Codes](../../../error-codes/ability-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported. |
| 16000118 | Not a master process. |
| 16000119 | Cannot exit because there is an unfinished request. |

**Example**

import { AbilityConstant, UIAbility, application, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    try {
      application.exitMasterProcessRole()
        .then(() => {
          console.info('exitMasterProcessRole succeed');
        })
        .catch((err: BusinessError) => {
          console.error(\`exitMasterProcessRole failed, code is ${err.code}, message is ${err.message}\`);
        });
    } catch (error) {
      let code: number = (error as BusinessError).code;
      let message: string = (error as BusinessError).message;
      console.error(\`exitMasterProcessRole failed, error.code: ${code}, error.message: ${message}\`);
    }
  }
}

#### application.getAppPreloadType22+

getAppPreloadType(): AppPreloadType

Obtains the preloading type of the current application process.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/Rg0ICCSeQ7CYWg1R24ZxTA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062204Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2524A9EEB4B09084E6F76BF2DEFAF8F88BB2EADD270C3B9A57641085B6DB5FE6)

-   This API can return the actual preloading type only if it is called before the first execution of [AbilityStage.onCreate](../ohos-app-ability-abilitystage-abilitystage-component-manager/document.md#oncreate).
-   Once the AbilityStage creation finishes, the preloaded data of the application is cleared. Any subsequent calls will return **UNSPECIFIED** instead of the original preloading type.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [AppPreloadType](#apppreloadtype22) | Obtains the preloading type of the current application process. |

**Example**

import { AbilityStage, application } from '@kit.AbilityKit';

export default class MyAbilityStage extends AbilityStage{
  onCreate() {
    let appPreloadType = application.getAppPreloadType();
  }
}
