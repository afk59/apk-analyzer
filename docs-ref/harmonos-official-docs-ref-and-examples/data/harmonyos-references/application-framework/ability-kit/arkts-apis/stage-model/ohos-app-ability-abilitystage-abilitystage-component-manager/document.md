# @ohos.app.ability.AbilityStage (AbilityStage Component Manager)

AbilityStage is a [module](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/application-package-overview#multi-module-design-mechanism)\-level component manager. It is used for initializing operations such as resource preloading and thread creation at the module level, as well as maintaining the application state under the module. An AbilityStage instance corresponds to a module.

When the [HAP](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/hap-package) or [HSP](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/in-app-hsp) of an application is first loaded, an AbilityStage instance is created. If a module contains both AbilityStage and other components (like UIAbility or ExtensionAbility), the AbilityStage instance is created before the other component instances.

An AbilityStage has the lifecycle callbacks [onCreate()](#oncreate) and [onDestroy()](#ondestroy12), and the event callbacks [onAcceptWant()](#onacceptwant), [onConfigurationUpdate()](#onconfigurationupdate), and [onMemoryLevel()](#onmemorylevel).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/dgdIqLdMRd658UDmdXelYg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062204Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B3A4B443E3149E5B7A830DA33E71340E101023EE430F5090E5E304A7A79D98D8)

The initial APIs of this module are supported since API version 9. Newly added APIs will be marked with a superscript to indicate their earliest API version.

The APIs of this module can be used only in the stage model.

#### Modules to Import

import { AbilityStage } from '@kit.AbilityKit';

#### AbilityStage

#### \[h2\]Properties

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| context | [AbilityStageContext](../../dependent-elements-and-definitions/application/abilitystagecontext/document.md) | No | No | Context of an AbilityStage. |

#### \[h2\]onCreate

onCreate(): void

Called when an AbilityStage instance is created. Such an instance is automatically created by the system before it loads the first Ability instance of the module.

You can initialize the module (for example, preload resources or create threads) in this callback. This API returns the result synchronously and does not support asynchronous callbacks.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Example**

import { AbilityStage } from '@kit.AbilityKit';

export default class MyAbilityStage extends AbilityStage {
  onCreate() {
    console.info('MyAbilityStage.onCreate is called');
  }
}

#### \[h2\]onAcceptWant

onAcceptWant(want: Want): string

Called when a UIAbility with the launch mode set to [specified](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-launch-type#specified) is launched. This API returns a string representing the unique ID of the UIAbility instance. This API returns the result synchronously and does not support asynchronous callbacks.

If a UIAbility instance with the same ID already exists in the system, that instance is reused. Otherwise, a new instance is created.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/oDZorntpSzi9EHA29xaYTA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062204Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7082A71EA7241E8356DEFA29EB94234E6564C8188D2737F8C2D18C028443864F)

Starting from API version 20, this callback is not triggered when [AbilityStage.onAcceptWantAsync](#onacceptwantasync20) is implemented.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| want | [Want](../../both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | Want type parameter that includes the launch parameters provided by the caller, such as the ability name and bundle name. |

**Return value**

| Type | Description |
| :-- | :-- |
| string | ID of the UIAbility. If a UIAbility with the same ID has been launched, that UIAbility is reused. Otherwise, a new instance is created and launched. |

**Example**

import { AbilityStage, Want } from '@kit.AbilityKit';

export default class MyAbilityStage extends AbilityStage {
  onAcceptWant(want: Want) {
    console.info('MyAbilityStage.onAcceptWant called');
    return 'com.example.test';
  }
}

#### \[h2\]onNewProcessRequest11+

onNewProcessRequest(want: Want): string

Called when a UIAbility, which is configured to run in an independent process (with **isolationProcess** set to **true** in the [module.json5](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/module-configuration-file) file), is launched. This API returns a string representing the unique process ID. This API returns the result synchronously and does not support asynchronous callbacks.

If the application already has a process with the same ID, the UIAbility runs in that process. Otherwise, a new process is created.

If you implement both **onNewProcessRequest** and [onAcceptWant](#onacceptwant), the system first invokes the **onNewProcessRequest** callback, and then the **onAcceptWant** callback.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/6FU34NBjQxqgAGlgVmf5gw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062204Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4000E1904EE64371D980C00FE20E9E3D3A05A29E83C23CA3826A14C57B720185)

-   In API version 19 and earlier, only a UIAbility can be launched in the specified process.
-   Starting from API version 20, this callback is not executed when [AbilityStage.onNewProcessRequestAsync](#onnewprocessrequestasync20) is implemented.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Device behavior differences**: This API executes the callback normally only on 2-in-1 devices and tablets. It does not execute the callback on other devices.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| want | [Want](../../both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | Want type parameter that includes the launch parameters provided by the caller, such as the UIAbility name and bundle name. |

**Return value**

| Type | Description |
| :-- | :-- |
| string | Custom process identifier. If the process with this identifier has been created, the ability runs in the process. Otherwise, a new process is created and the ability runs in it. |

**Example**

import { AbilityStage, Want } from '@kit.AbilityKit';

export default class MyAbilityStage extends AbilityStage {
  onNewProcessRequest(want: Want) {
    console.info('MyAbilityStage.onNewProcessRequest called');
    return 'com.example.test';
  }
}

#### \[h2\]onConfigurationUpdate

onConfigurationUpdate(newConfig: Configuration): void

Called when the system global configuration (such as the system language and dark/light color mode) changes. All the configuration items are defined in the [Configuration](../../both-models-recommended/ohos-app-ability-configuration-environment-variables/document.md) class. This API returns the result synchronously and does not support asynchronous callbacks.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/MW-DcEtcQTe_YF4P7MMFxw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062204Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D43D059296E9F6E84A026E62EBF366E833EFB13F0868E51FC8C90D4112D5CA33)

There are certain restrictions when this callback is actually triggered. For example, if you set the application language by calling [setLanguage](../../dependent-elements-and-definitions/application/applicationcontext-application-context/document.md#applicationcontextsetlanguage11), the system does not trigger the **onConfigurationUpdate** callback even if the system language changes. For details, see [When to Use](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/subscribe-system-environment-variable-changes#when-to-use).

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| newConfig | [Configuration](../../both-models-recommended/ohos-app-ability-configuration-environment-variables/document.md) | Yes | Callback invoked when the global configuration is updated. The global configuration indicates the configuration of the environment where the application is running and includes the language and color mode. |

**Example**

import { AbilityStage, Configuration } from '@kit.AbilityKit';

export default class MyAbilityStage extends AbilityStage {
  onConfigurationUpdate(config: Configuration) {
    console.info(\`MyAbilityStage.onConfigurationUpdate, language: ${config.language}\`);
  }
}

#### \[h2\]onMemoryLevel

onMemoryLevel(level: AbilityConstant.MemoryLevel): void

Listens for changes in the system memory level status. Called when the available memory of the entire device changes to a specified level. You can implement this callback to promptly release non-essential resources (such as cached data or temporary objects) upon receiving a memory shortage event, thereby preventing the application process from being forcibly terminated by the system.

This API returns the result synchronously and does not support asynchronous callbacks.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/a5D0eqk9Q9qdAEtrnmpJeg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062204Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D5F77D4DD22037DD05081615BF47B5DA5AEBC88FE5C0CF031C0D380A840C4F7A)

The **onMemoryLevel** callback runs in the main thread of the current process. If time-consuming UI component release is performed in this callback, the main thread task will be blocked. Therefore, you are not advised to release UI components in the callback.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| level | [AbilityConstant.MemoryLevel](../ohos-app-ability-abilityconstant-ability-related-constants/document.md#memorylevel) | Yes | 
Memory level that indicates the memory usage status. When the specified memory level is reached, a callback will be invoked and the system will start adjustment.

**NOTE**

The trigger conditions may differ across various devices. For example, on a standard device with 12 GB of memory:

\- A callback with value 0 is triggered when available memory drops to between 1700 MB and 1800 MB.

\- A callback with value 1 is triggered when available memory drops to between 1600 MB and 1700 MB.

\- A callback with value 2 is triggered when available memory drops to below 1600 MB.

 |

**Example**

import { AbilityStage, AbilityConstant } from '@kit.AbilityKit';

export default class MyAbilityStage extends AbilityStage {
  onMemoryLevel(level: AbilityConstant.MemoryLevel) {
    console.info(\`MyAbilityStage.onMemoryLevel, level: ${JSON.stringify(level)}\`);
  }
}

#### \[h2\]onDestroy12+

onDestroy(): void

Called when the last Ability instance of the corresponding module exits. This API is called during the normal lifecycle. If the application exits abnormally or is terminated, this API is not called. This API returns the result synchronously and does not support asynchronous callbacks.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Example**

import { AbilityStage } from '@kit.AbilityKit';

export default class MyAbilityStage extends AbilityStage {
  onDestroy() {
    console.info('MyAbilityStage.onDestroy is called');
  }
}

#### \[h2\]onPrepareTermination15+

onPrepareTermination(): AbilityConstant.PrepareTermination

Called when the application is closed by the user, allowing the user to choose between immediate termination or cancellation. This API returns the result synchronously and does not support asynchronous callbacks.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/LIYTqd84Sn2wL9l60JYVyg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062204Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=07BD209B4E2210DF78DBB06EFBDAA71E31FA98DDA32C4EE1DB2FB61E28A32604)

-   The API is called only when the application exits under normal circumstances (for example, when the application is closed through the doc bar or tray, or when the application shuts down along with the device). It will not be called if the application is terminated forcibly.
    
-   This API is not executed when [AbilityStage.onPrepareTerminationAsync](#onprepareterminationasync15) is implemented.
    

**Required permissions**: ohos.permission.PREPARE\_APP\_TERMINATE

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Device behavior differences**

-   Starting from API version 15, this API executes the callback normally only on 2-in-1 devices. It does not execute the callback on other devices.
-   Starting from API version 19, this API executes the callback normally only on 2-in-1 devices and tablets. It does not execute the callback on other devices.

**Return value**

| Type | Description |
| :-- | :-- |
| [AbilityConstant.PrepareTermination](../ohos-app-ability-abilityconstant-ability-related-constants/document.md#preparetermination15) | The user's choice. |

**Example**

import { AbilityConstant, AbilityStage } from '@kit.AbilityKit';

export default class MyAbilityStage extends AbilityStage {
  onPrepareTermination(): AbilityConstant.PrepareTermination {
    console.info('MyAbilityStage.onPrepareTermination is called');
    return AbilityConstant.PrepareTermination.CANCEL;
  }
}

#### \[h2\]onPrepareTerminationAsync15+

onPrepareTerminationAsync(): Promise<AbilityConstant.PrepareTermination>

Called when the application is closed by the user, allowing the user to choose between immediate termination or cancellation. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/XahndCmWS8OdGLJs12kmHw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062204Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=99FB9721B4CDCD0661BB0238FB79B48CD16981E98CC3E60D2360BF710179825B)

-   The API is called only when the application exits under normal circumstances (for example, when the application is closed through the doc bar or tray, or when the application shuts down along with the device). It will not be called if the application is terminated forcibly.
    
-   If an asynchronous callback crashes, it will be handled as a timeout. If the application does not respond within 10 seconds, it will be terminated forcibly.
    

**Required permissions**: ohos.permission.PREPARE\_APP\_TERMINATE

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Device behavior differences**

-   Starting from API version 15, this API executes the callback normally only on 2-in-1 devices. It does not execute the callback on other devices.
-   Starting from API version 19, this API executes the callback normally only on 2-in-1 devices and tablets. It does not execute the callback on other devices.

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[AbilityConstant.PrepareTermination](../ohos-app-ability-abilityconstant-ability-related-constants/document.md#preparetermination15)\> | Promise used to return the user's choice. |

**Example**

import { AbilityConstant, AbilityStage } from '@kit.AbilityKit';

export default class MyAbilityStage extends AbilityStage {
  async onPrepareTerminationAsync(): Promise<AbilityConstant.PrepareTermination> {
    await new Promise<AbilityConstant.PrepareTermination>((res, rej) => {
      setTimeout(res, 3000); // Execute the operation after 3 seconds.
    });
    return AbilityConstant.PrepareTermination.CANCEL;
  }
}

#### \[h2\]onAcceptWantAsync20+

onAcceptWantAsync(want: Want): Promise<string>

Called when a UIAbility with the launch mode set to [specified](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-launch-type#specified) is launched. This API returns a string representing the unique ID of the UIAbility instance. This API uses a promise to return the result.

If a UIAbility instance with the same ID already exists in the system, that instance is reused. Otherwise, a new instance is created.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| want | [Want](../../both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | Want information about the target UIAbility, such as the UIAbility name and bundle name. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<string> | Promise used to return a string that uniquely identifies the UIAbility instance launched. If a UIAbility instance with the same ID already exists in the system, that instance is reused. Otherwise, a new instance is created. |

**Example**

import { AbilityStage } from '@kit.AbilityKit';

class MyAbilityStage extends AbilityStage {
  async onAcceptWantAsync(): Promise<string> {
    await new Promise<string>((res, rej) => {
      setTimeout(res, 1000); // Execute the operation after 1 second.
    });
    return 'default';
  }
}

#### \[h2\]onNewProcessRequestAsync20+

onNewProcessRequestAsync(want: Want): Promise<string>

Called when a UIAbility, which is configured to run in an independent process (with **isolationProcess** set to **true** in the [module.json5](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/module-configuration-file) file), is launched. This API returns a string representing the unique process ID. This API uses a promise to return the result.

If the application already has a process with the same ID, the UIAbility runs in that process. Otherwise, a new process is created.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Device behavior differences**: This API executes the callback normally only on 2-in-1 devices and tablets. It does not execute the callback on other devices.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| want | [Want](../../both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | Want type parameter that includes the launch parameters provided by the caller, such as the UIAbility name and bundle name. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<string> | Promise used to return a string representing the process ID. If the application already has a process with the same ID, the UIAbility runs in that process. Otherwise, a new process is created. |

**Example**

import { AbilityStage } from '@kit.AbilityKit';

class MyAbilityStage extends AbilityStage {
  async onNewProcessRequestAsync(): Promise<string> {
    await new Promise<string>((res, rej) => {
      setTimeout(res, 1000); // Execute the operation after 1 second.
    });
    return '';
  }
}
