# AppStartup

#### Overview

During application launch, a series of startup tasks are often required. If all these tasks are placed within the [onCreate](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-uiability#oncreate) lifecycle of the [UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-uiability) in the [HAP](../../../../../getting-started/development-fundamentals/application-package-fundamentals/application-package-development-and-usage/hap/document.md), they can only be executed sequentially on the main thread, which significantly affects the application launch speed. In addition, when there are too many tasks, complex dependencies between them make the code difficult to maintain.

AppStartup offers an efficient approach to application launch. By supporting asynchronous initiation of startup tasks, it ensures a smoother startup process. The centralized configuration of execution order and dependencies of multiple startup tasks in a single file simplifies and clarifies the startup codebase, enhancing maintainability.

#### Working Mechanism

AppStartup supports startup tasks in automatic or manual mode. By default, automatic mode is used. During the creation of an [AbilityStage](../../../ability-kit-terminology/document.md#abilitystage), the configured startup tasks are loaded and executed in automatic mode. You can also call [startupManager.run](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-appstartup-startupmanager#startupmanagerrun) to execute the startup tasks in manual mode after an AbilityStage is created.

**Figure 1** Startup procedure

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d/v3/lSKM_uyWRTe6-5tIeI-JXw/en-us_image_0000002568764081.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061916Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8D36095F43D37E50949837C923EC73BD898A11A1FE2ED117652EB6F3EBA87B09)

#### Supported Scope

-   An entry-type HAP can be started in automatic or manual mode. Starting from API version 20, a feature-type HAP can be started in automatic or manual mode.
    
-   Starting from API version 18, startup tasks can be configured in the [HSP](../../../../../getting-started/development-fundamentals/application-package-fundamentals/application-package-development-and-usage/hsp/document.md) and [HAR](../../../../../getting-started/development-fundamentals/application-package-fundamentals/application-package-development-and-usage/har/document.md). However, startup tasks and .so file preloading tasks in the HSP and HAR cannot be set to automatic mode. Instead, they can be initiated by the automatic startup tasks and .so file preloading tasks in the HAP.
    
-   Starting from API version 18, AppStartup supports the configuration of .so file preloading tasks. For details about how to develop .so files, refer to [Node-API](../../../../../ndk-development/code-development/using-node-api/node-api-development-process/document.md) to create a native C++ project.
    

#### Constraints

-   AppStartup must be enabled in the [module.json5](../../../../../getting-started/development-fundamentals/application-configuration-files-in-stage-model/module-json5-configuration-file/document.md) file of the [HAP](../../../../../getting-started/development-fundamentals/application-package-fundamentals/application-package-development-and-usage/hap/document.md).
    
-   Given that the ExtensionAbility have a single launch scenario and using AppStartup will add unnecessary overhead, it is not supported to trigger AppStartup when starting the ExtensionAbility.
    
-   Circular dependencies between startup tasks or .so file preloading tasks are not allowed.
    

#### Development Process

1.  [Defining an AppStartup Configuration File](#defining-an-appstartup-configuration-file): Create and define an AppStartup configuration file in the resource file directory.
    
    1.  [Creating an AppStartup Configuration File](#creating-an-appstartup-configuration-file): Create an AppStartup configuration file in the resource file directory, and reference this configuration file in [module.json5](../../../../../getting-started/development-fundamentals/application-configuration-files-in-stage-model/module-json5-configuration-file/document.md).
    2.  [Defining Startup Parameter Configuration](#defining-startup-parameter-configuration): Add startup parameter configuration information to the AppStartup configuration file.
    3.  [Defining Startup Task Configuration](#defining-startup-task-configuration): Add startup task configuration information to the AppStartup configuration file.
    4.  [Defining .so File Preloading Task Configuration](#defining-so-file-preloading-task-configuration): Add configuration information of .so file preloading tasks to the AppStartup configuration file.
2.  [Setting Startup Parameters](#setting-startup-parameters): In the startup parameter file, set parameters such as the timeout interval and startup task listener.
    
3.  [Adding a Startup Task for Each Component to Be Initialized](#adding-a-startup-task-for-each-component-to-be-initialized): Implement the [StartupTask](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-appstartup-startuptask) interface.
    
4.  [Optional Operations](#optional-operations): You can finely control the behavior of AppStartup in complex scenarios.
    
    -   [Using AppStartup in the HSP and HAR](#using-appstartup-in-the-hsp-and-har): Configure startup tasks and .so file preloading tasks in the HSP and HAR to manage dependencies across modules, making large applications start faster and be easier to maintain.
    -   [Changing Startup Mode](#changing-startup-mode): Switch the startup task and .so file preloading task to manual mode to decide exactly when they run, cutting down on startup time.
    -   [Adding Task Matching Rules](#adding-task-matching-rules): Use rules to filter which tasks run, ensuring only relevant tasks load based on the situation.
    -   [Setting the Startup Task Scheduling Phase](#setting-the-startup-task-scheduling-phase): Set the scheduling phase of startup tasks to execute them earlier, thereby reducing startup time.

#### Defining an AppStartup Configuration File

## Creating an AppStartup Configuration File

1.  Create an AppStartup configuration file in **resources/base/profile** of the [HAP](../../../../../getting-started/development-fundamentals/application-package-fundamentals/application-package-development-and-usage/hap/document.md). The file name can be customized. The following uses **startup\_config.json** as an example.
    
2.  Add the index of the AppStartup configuration file to the **appStartup** tag in the [module.json5 file](../../../../../getting-started/development-fundamentals/application-configuration-files-in-stage-model/module-json5-configuration-file/document.md).
    
    The following is an example of the **module.json5** file:
    
    {
      "module": {
        "name": "entry",
        "type": "entry",
        // ···
        "appStartup": "$profile:startup\_config," // AppStartup configuration file
        // ···
      }
    }
    

## Defining Startup Parameter Configuration

In the **startup\_config.json** file, add the configuration for the startup parameters.

1.  Create the startup parameter configuration file in the **ets/startup** directory. In this example, the file name is **StartupConfig.ets**.
    
2.  Add the information about the startup parameter configuration file to the **startup\_config.json** file.
    
    The following is an example of the **startup\_config.json** file:
    
    {
      "startupTasks": \[
        // A startup task.
      \],
      "appPreloadHintStartupTasks": \[
        // A .so file preloading task.
      \],
      "configEntry": "./ets/startup/StartupConfig.ets" // Startup parameter configuration
    }
    

**Table 1** Fields in the startup\_config.json file

| Field | Description | Data Type | Optional |
| :-- | :-- | :-- | :-- |
| startupTasks | Configuration information about a startup task. For details, see [Defining Startup Task Configuration](#defining-startup-task-configuration). | Object array | Optional, defaults to an empty array |
| appPreloadHintStartupTasks | Configuration information about a .so file preloading task configuration. For details, see [Defining .so File Preloading Task Configuration](#defining-so-file-preloading-task-configuration). | Object array | Optional, defaults to an empty array |
| configEntry | 
Path of the startup parameter file. For details, see [Setting Startup Parameters](#setting-startup-parameters).

**NOTE**

\- Do not configure this field for the HSP and HAR.

\- If [file name obfuscation](../../../../arkts/arkts-compilation-toolchain/arkguard-for-source-code-obfuscation/arkguard-principles-and-capabilities-for-source-code-obfuscation/document.md#section-enable-filename-obfuscation) is enabled, the file path must be added to the trustlist. For details, see [\-keep-file-name](../../../../arkts/arkts-compilation-toolchain/arkguard-for-source-code-obfuscation/arkguard-principles-and-capabilities-for-source-code-obfuscation/document.md#section-keep-file-name).

 | String | Mandatory |

## Defining Startup Task Configuration

It is assumed that the application has six startup tasks. The dependencies between the tasks are shown in the figure below. To facilitate concurrent execution of startup tasks, a startup task file should contain only one startup task. In this example, each startup task corresponds to a startup task file.

**Figure 2** Dependencies between startup tasks

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/knvVjVDqRxOUL99hqdVebw/en-us_image_0000002537764356.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061916Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F3CEB351A9D26D5379724E11E629E6CE0F5A05E17921DD4F50F19933F47FC02A)

1.  Create six startup task files in the **ets/startup** directory. The file names must be unique. In this example, the six files are named from **StartupTask\_001.ets** to **StartupTask\_006.ets**.
    
2.  Add the startup task configuration information to the **startup\_config.json** file.
    
    The following is an example of the **startup\_config.json** file:
    
    {
      "startupTasks": \[
        {
          "name": "StartupTask\_001",
          "srcEntry": "./ets/startup/StartupTask\_001.ets",
          "dependencies": \[
            "StartupTask\_002",
            "StartupTask\_003"
          \],
          "runOnThread": "taskPool",
          "waitOnMainThread": false
        },
        {
          "name": "StartupTask\_002",
          "srcEntry": "./ets/startup/StartupTask\_002.ets",
          "dependencies": \[
            "StartupTask\_003",
            "StartupTask\_004"
          \],
          "runOnThread": "taskPool",
          "waitOnMainThread": false
        },
        {
          "name": "StartupTask\_003",
          "srcEntry": "./ets/startup/StartupTask\_003.ets",
          "dependencies": \[
            "StartupTask\_004"
          \],
          "runOnThread": "taskPool",
          "waitOnMainThread": false
        },
        {
          "name": "StartupTask\_004",
          "srcEntry": "./ets/startup/StartupTask\_004.ets",
          "runOnThread": "taskPool",
          "waitOnMainThread": false
        },
        {
          "name": "StartupTask\_005",
          "srcEntry": "./ets/startup/StartupTask\_005.ets",
          "dependencies": \[
            "StartupTask\_006"
          \],
          "runOnThread": "mainThread",
          "waitOnMainThread": true,
          "excludeFromAutoStart": true
        },
        {
          "name": "StartupTask\_006",
          "srcEntry": "./ets/startup/StartupTask\_006.ets",
          "runOnThread": "mainThread",
          "waitOnMainThread": false,
          "excludeFromAutoStart": true
        }
      \],
      "appPreloadHintStartupTasks": \[
        // A .so file preloading task.
      \],
      "configEntry": "./ets/startup/StartupConfig.ets"
    }
    

**Table 2** Description of startupTasks

| Field | Description | Data Type | Optional |
| :-- | :-- | :-- | :-- |
| name | Name of the startup task, which can be customized. It is recommended that the name be the same as the class name. | String | Mandatory |
| srcEntry | 
Path of the file corresponding to the startup task.

**NOTE**

If [file name obfuscation](../../../../arkts/arkts-compilation-toolchain/arkguard-for-source-code-obfuscation/arkguard-principles-and-capabilities-for-source-code-obfuscation/document.md#section-enable-filename-obfuscation) is enabled, the file path must be added to the trustlist. For details, see [\-keep-file-name](../../../../arkts/arkts-compilation-toolchain/arkguard-for-source-code-obfuscation/arkguard-principles-and-capabilities-for-source-code-obfuscation/document.md#section-keep-file-name).

 | String | Mandatory |
| dependencies | Array holding the class names of other startup tasks on which this task depends. | Object array | Optional, defaults to an empty array |
| excludeFromAutoStart | 

Whether to exclude automatic mode. For details, see [Changing Startup Mode](#changing-startup-mode).

\- **true**: manual mode.

\- **false**: automatic mode.

**NOTE**

This field must be set to **true** for the HSP and HAR.

 | Boolean | Optional, defaults to **false** |
| runOnThread | 

Thread where the startup task is executed.

\- **mainThread**: executed in the main thread.

\- **taskPool**: executed in an asynchronous thread.

 | String | Optional, defaults to **mainThread** |
| waitOnMainThread | 

Whether the main thread needs to wait until the startup task finishes execution. This parameter is valid only when **runOnThread** is set to **taskPool**.

\- **true**: The main thread loads the application home page only the startup task finishes execution.

\- **false**: The main thread does not wait for the startup task to finish execution.

 | Boolean | Optional, defaults to **true** |
| matchRules | 

Used to filter startup tasks that should be initiated in automatic mode to expedite the application launch process. It is ideal for scenarios where you need to quickly pull up a particular page, such as transitions triggered by home screen widgets, notifications, or intent calls, to provide a seamless one-step experience for accessing functional services. For details, see [Adding Task Matching Rules](#adding-task-matching-rules).

**NOTE**

\- This field is supported since API version 20 and can be configured only in HAPs.

\- This field takes precedence over **excludeFromAutoStart**. If none of the startup tasks match, the tasks are processed according to their **excludeFromAutoStart** settings.

 | Object | Optional |
| schedulerPhase | 

Scheduling phase for startup tasks. For details about the setting procedure, see [Setting the Startup Task Scheduling Phase](#setting-the-startup-task-scheduling-phase).

\- **preAbilityStageLoad**: The startup task and its dependent tasks are scheduled and executed before the AbilityStage module is loaded.

\- **postAbilityStageLoad**: The startup task and its dependent tasks are scheduled and executed after the AbilityStage module is loaded.

**NOTE**

\- This field is supported since API version 21 and can be configured only in HAPs.

\- "AbilityStage module loading" here refers to the loading of the **AbilityStage.ets** file and its dependent modules. For details, see [Loading Process of Modular Operation](../../../../arkts/arkts-runtime/arkts-modularization/overview-of-modular-operation/document.md#loading-process-of-modular-operation).

 | String | Optional, defaults to **postAbilityStageLoad** |

## Defining .so File Preloading Task Configuration

It is assumed that AppStartup has six .so file preloading tasks. The dependencies between the tasks are shown in the figure below. You are not advised to run code logic in the loading callback of .so files, as prolonged .so file loading can adversely affect the main thread's operation.

**Figure 3** Dependencies between .so file preloading tasks

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/LL6GImxJTue2H5V720zMIQ/en-us_image_0000002537924296.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061916Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BF4DEA1CE0098B2827A485197F25FA74D55224FC56AB1C11FCF6EFB778490E95)

1.  Create.so files by referring to [Node-API](../../../../../ndk-development/code-development/using-node-api/node-api-development-process/document.md). In this example, the six files are named from **libentry\_001.so** to **libentry\_006.so**.
    
2.  Add the configuration information of the .so file preloading tasks to the **startup\_config.json** file.
    
    The following is an example of the **startup\_config.json** file:
    
    {
      "startupTasks": \[
        // A startup task.
      \],
      "appPreloadHintStartupTasks": \[
        {
          "name": "libentry\_001",
          "srcEntry": "libentry\_001.so",
          "dependencies": \[
            "libentry\_002",
            "libentry\_003"
          \],
          "runOnThread": "taskPool"
        },
        {
          "name": "libentry\_002",
          "srcEntry": "libentry\_002.so",
          "dependencies": \[
            "libentry\_003",
            "libentry\_004"
          \],
          "runOnThread": "taskPool"
        },
        {
          "name": "libentry\_003",
          "srcEntry": "libentry\_003.so",
          "dependencies": \[
            "libentry\_004"
          \],
          "runOnThread": "taskPool"
        },
        {
          "name": "libentry\_004",
          "srcEntry": "libentry\_004.so",
          "runOnThread": "taskPool"
        },
        {
          "name": "libentry\_005",
          "srcEntry": "libentry\_005.so",
          "dependencies": \[
            "libentry\_006"
          \],
          "runOnThread": "taskPool",
          "excludeFromAutoStart": true
        },
        {
          "name": "libentry\_006",
          "srcEntry": "libentry\_006.so",
          "runOnThread": "taskPool",
          "excludeFromAutoStart": true
        }
      \],
      "configEntry": "./ets/startup/StartupConfig.ets"
    }
    

**Table 3** appPreloadHintStartupTasks

| Field | Description | Data Type | Optional |
| :-- | :-- | :-- | :-- |
| name | Name of the .so file to preload. | String | Mandatory |
| srcEntry | File name of the .so file, including the extension. | String | Mandatory |
| dependencies | Array holding the .so file names of other preloading tasks on which this task depends. | Object array | Optional, defaults to an empty array |
| excludeFromAutoStart | 
Whether to exclude automatic mode. For details, see [Changing Startup Mode](#changing-startup-mode).

\- **true**: manual mode.

\- **false**: automatic mode.

**NOTE**

This field must be set to **true** for the HSP and HAR.

 | Boolean | Optional, defaults to **false** |
| runOnThread | 

Thread where preloading is performed.

\- **taskPool**: executed in an asynchronous thread.

**NOTE**

Preloading of .so files can be executed only in TaskPool threads.

 | String | Mandatory |
| matchRules | 

Used to filter the .so file preloading tasks that should be initiated in automatic mode to expedite the application launch process. It is ideal for scenarios where you need to quickly pull up a particular page, such as transitions triggered by home screen widgets, notifications, or intent calls, to provide a seamless one-step experience for accessing functional services. For details, see [Adding Task Matching Rules](#adding-task-matching-rules).

**NOTE**

\- This field is supported since API version 20 and can be configured only in HAPs.

\- This field takes precedence over **excludeFromAutoStart**. If none of the .so file preloading tasks match, the tasks are processed according to their **excludeFromAutoStart** settings.

 | Object | Optional |

#### Setting Startup Parameters

In the startup parameter file (**ets/startup/StartupConfig.ets** in this example), call [StartupConfigEntry](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-appstartup-startupconfigentry) to set the common AppStartup parameters, including the timeout interval and listener.

-   [StartupConfig](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-appstartup-startupconfig): sets the task timeout interval and AppStartup listener.
-   [StartupListener](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-appstartup-startuplistener): listens for the execution result of the startup task.

import { StartupConfig, StartupConfigEntry, StartupListener } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class MyStartupConfigEntry extends StartupConfigEntry {
  onConfig() {
    hilog.info(0x0000, 'testTag', \`onConfig\`);
    let onCompletedCallback = (error: BusinessError<void>) => {
      hilog.info(0x0000, 'testTag', \`onCompletedCallback\`);
      if (error) {
        hilog.error(0x0000, 'testTag', 'onCompletedCallback: %{public}d, message: %{public}s', error.code,
          error.message);
      } else {
        hilog.info(0x0000, 'testTag', \`onCompletedCallback: success.\`);
      }
    };
    let startupListener: StartupListener = {
      'onCompleted': onCompletedCallback
    };
    let config: StartupConfig = {
      'timeoutMs': 10000,
      'startupListener': startupListener
    };
    return config;
  }
// ···
}

#### Adding a Startup Task for Each Component to Be Initialized

Through the preceding operations, you have configured the AppStartup configuration file and startup parameters. Now you need to implement [StartupTask](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-appstartup-startuptask) in each startup task file by calling the following two APIs:

-   [init](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-appstartup-startuptask#init): starts task initialization. Call **init** to initialize a task only after all startup tasks on which the task depends are executed, that is, after **onDependencyCompleted** is invoked.
-   [onDependencyCompleted](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-appstartup-startuptask#ondependencycompleted): invoked when the startup task on which the current task depends is complete.

The following uses the **StartupTask\_001.ets** file in [startup\_config.json](#defining-startup-task-configuration) as an example. You must add a startup task for each component to be initialized.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/-g7syFXdQhGZ8ppwYKD_5A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061916Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B99ECEC01CA2AC3E4EF64283B703E9E5C69C4B641A927A977B77D63963EAC1BB)

**StartupTask** follows the [Sendable protocol](../../../../arkts/arkts-concurrency/inter-thread-communication/inter-thread-communication-objects/sendable-object/overview-of-sendable-objects/document.md#sendable-protocol). Therefore, the Sendable annotation must be added when this API is inherited.

import { StartupTask, common } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

@Sendable
export default class StartupTask\_001 extends StartupTask {
  constructor() {
    super();
  }

  async init(context: common.AbilityStageContext) {
    hilog.info(0x0000, 'testTag', 'StartupTask\_001 init.');
    return 'StartupTask\_001';
  }

  onDependencyCompleted(dependence: string, result: Object): void {
    hilog.info(0x0000, 'testTag', 'StartupTask\_001 onDependencyCompleted, dependence: %{public}s, result: %{public}s',
      dependence, JSON.stringify(result));
  }
}

#### Optional Operations

## Using AppStartup in the HSP and HAR

Large applications often consist of multiple [HSP](../../../../../getting-started/development-fundamentals/application-package-fundamentals/application-package-development-and-usage/hsp/document.md) and [HAR](../../../../../getting-started/development-fundamentals/application-package-fundamentals/application-package-development-and-usage/har/document.md) modules. This section provides an example to demonstrate how to use AppStartup in HSP and HAR packages. This example application includes two HSP packages (hsp1, hsp2) and one HAR package (har1), with startup tasks and .so file preloading tasks.

Perform the following steps:

1.  Create an AppStartup configuration file under the **resources/base/profile** directory for each HSP and HAR, in addition to the [HAP](../../../../../getting-started/development-fundamentals/application-package-fundamentals/application-package-development-and-usage/hap/document.md). Different modules can use the same file name. The following uses **startup\_config.json** as an example.
    
2.  Configure the **startup\_config.json** file for each module.
    
    The table below lists the startup tasks and .so file preloading tasks available for the application.
    
    **Table 4** Startup tasks and .so file preloading tasks
    
    | Module | Startup Task | .so File Preloading Task |
    | :-- | :-- | :-- |
    | entry | HAP\_Task\_01 | libentry\_01 |
    | hsp1 | 
    HSP1\_Task\_01
    
    HSP1\_Task\_02
    
     | 
    
    libhsp1\_01
    
    libhsp1\_02
    
     |
    | hsp2 | HSP2\_Task\_01 | libhsp2\_01 |
    | har | HAR1\_Task\_01 | libhar1\_01 |
    
    **Figure 4** Dependencies between the startup tasks and .so file preloading tasks
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/feHOhYI1RTKwsN7fTJoXQQ/en-us_image_0000002568684073.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061916Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2E268A5BCC5B135ED1435663F34E8EE5EA58D98A44FADBBB8A86837E65BD9EA2)
    
    For details about the **startup\_config.json** file of the [HAP](../../../../../getting-started/development-fundamentals/application-package-fundamentals/application-package-development-and-usage/hap/document.md), see [Defining Startup Task Configuration](#defining-startup-task-configuration). For the HSP and HAR, do not configure the **configEntry** field in the **startup\_config.json** file. The following uses the configuration file of **hsp1** as an example:
    
    {
      "startupTasks": \[
        {
          "name": "HSP1\_Task\_01",
          "srcEntry": "./ets/startup/HSP1\_Task\_01.ets",
          "dependencies": \[
            "HSP1\_Task\_02",
            "HAR1\_Task\_01"
          \],
          "runOnThread": "taskPool",
          "waitOnMainThread": false,
          "excludeFromAutoStart": true
        }
      \],
      "appPreloadHintStartupTasks": \[
        {
          "name": "libhsp1\_01",
          "srcEntry": "libhsp1\_01.so",
          "dependencies": \[
            "libhsp1\_02",
            "libhar1\_01"
          \],
          "runOnThread": "taskPool",
          "excludeFromAutoStart": true
        }
      \]
    }
    
3.  Add the index of the AppStartup configuration file to the **appStartup** tag in the [module.json5 file](../../../../../getting-started/development-fundamentals/application-configuration-files-in-stage-model/module-json5-configuration-file/document.md) of each module.
    
    The following are examples of **module.json5** for **hsp1**, **hsp2**, and **har1**:
    
    {
      "module": {
        "name": "hsp1",
        "type": "shared",
        // ···
        "appStartup": "$profile:startup\_config," // AppStartup configuration file
        // ···
      }
    }
    
    {
      "module": {
        "name": "hsp2",
        "type": "shared",
        // ···
        "appStartup": "$profile:startup\_config," // AppStartup configuration file
        // ···
      }
    }
    
    {
      "module": {
        "name": "har1",
        "type": "har",
        // ···
        "appStartup": "$profile:startup\_config," // AppStartup configuration file
      }
    }
    

For details about other steps, see [Setting Startup Parameters](#setting-startup-parameters) and [Adding a Startup Task for Each Component to Be Initialized](#adding-a-startup-task-for-each-component-to-be-initialized).

## Changing Startup Mode

AppStartup provides two modes for executing startup tasks: automatic and manual. The entry module defaults to automatic mode, but you can change it to manual mode if needed. The HSP and HAR support the configuration of manual mode only.

-   Automatic mode: After an AbilityStage is created, startup tasks are automatically executed.
-   Manual mode: After a UIAbility is created, you need to manually call the API to execute the startup tasks and .so file preloading tasks. Modules that are infrequently used do not need to be initialized when the application is launched. You can change the startup mode of these modules to manual. After the application finishes launching, you can call [startupManager.run](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-appstartup-startupmanager#startupmanagerrun) to execute the startup tasks and .so file preloading tasks.

The following uses the **onCreate** lifecycle of the UIAbility as an example to describe how to manually trigger a startup task. The sample code is as follows:

import { AbilityConstant, UIAbility, Want, startupManager } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';
// ···

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');
    let startParams = \['StartupTask\_005', 'StartupTask\_006'\];
    try {
      startupManager.run(startParams).then(() => {
        console.info(\`StartupTest startupManager run then, startParams = ${JSON.stringify(startParams)}.\`);
      }).catch((error: BusinessError) => {
        console.error(\`StartupTest promise catch error, error = ${JSON.stringify(error)}.\`);
        console.error(\`StartupTest promise catch error, startParams = ${JSON.stringify(startParams)}.\`);
      })
    } catch (error) {
      let errMsg = (error as BusinessError).message;
      let errCode = (error as BusinessError).code;
      console.error(\`Startup catch error, errCode= ${errCode}.\`);
      console.error(\`Startup catch error, errMsg= ${errMsg}.\`);
    }
  }

// ···
}

You can also call the API to trigger the manual mode after a page is loaded. The sample code is as follows:

import { startupManager } from '@kit.AbilityKit';

@Entry
@Component
struct Index {
  @State message: ResourceStr = $r('app.string.manual\_mode'); // $r('app.string.manual\_mode') is a custom resource.
  @State startParams1: Array<string> = \['StartupTask\_006'\];
  @State startParams2: Array<string> = \['libentry\_006'\];

  build() {
    RelativeContainer() {
      Button(this.message)
        .id('AppStartup')
        .fontSize(20)
        .fontWeight(FontWeight.Bold)
        .onClick(() => {
          if (!startupManager.isStartupTaskInitialized('StartupTask\_006')) { // Check whether the startup task finishes execution.
            startupManager.run(this.startParams1);
          }
          if (!startupManager.isStartupTaskInitialized('libentry\_006')) {
            startupManager.run(this.startParams2);
          }
        })
        .alignRules({
          center: { anchor: '\_\_container\_\_', align: VerticalAlign.Center },
          middle: { anchor: '\_\_container\_\_', align: HorizontalAlign.Center }
        })
    }
    .height('100%')
    .width('100%')
  }
}

## Adding Task Matching Rules

To achieve a one-step direct experience for functional services when launching a specific page via methods such as widgets, notifications, or intent calls, you can use **matchRules** to load only the relevant startup tasks for the current scenario, instead of loading all default auto-start tasks. This approach enhances startup performance.

You can add match rules in either of the following ways:

-   Using **uris**, **actions**, and **insightIntents** fields in **matchRules**: Match different startup tasks and .so file preloading tasks based on the URI, action, or intent name when the UIAbility is launched.
    
-   Using **customization** in **matchRules**: If the above methods do not meet your needs, you can define custom matching rule.
    
    **Table 5** Description of matchRules fields
    
    | Field | Description | Data Type | Optional | Scenario |
    | :-- | :-- | :-- | :-- | :-- |
    | uris | Range of URIs for tasks executed in automatic mode. When the UIAbility is launched, **uri** in the [Want](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-want) is matched against the configured **uris** array. The format is scheme://host/path, and other parts of the URI (such as port and fragment) are ignored. | String array | Optional, defaults to empty | The UIAbility is started through a specific URI. |
    | actions | Range of actions for tasks executed in automatic mode. When the UIAbility is launched, **action** in the [Want](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-want) is matched against the configured **actions** array. | String array | Optional, defaults to empty | The UIAbility is started through a specific action. |
    | insightIntents | Range of intent names for tasks executed in automatic mode. When the UIAbility is launched, **intentName** is matched against the configured **insightIntents** array. | String array | Optional, defaults to empty | The UIAbility is started through a specific intent name. |
    | customization | 
    Range of custom rules for tasks executed in automatic mode. Custom rules are returned by [onRequestCustomMatchRule](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-appstartup-startupconfigentry#onrequestcustommatchrule20) of StartupConfigEntry. When the UIAbility is started, the custom rule is matched against the configured **customization** array.
    
    **NOTE**
    
    Only tasks in **startupTasks** are supported.
    
     | String array | Optional, defaults to empty | If the **uris**, **actions**, and **insightIntents** fields do not meet your needs, you can use **customization** to customize rules. |
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/-e6eUTaKSiObCmS2tKzShw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061916Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C1B53AC05FDA7FABABE93468BB0500CA3C1BA7651B00DB52D47A40CC0FD0506F)
    
    -   If any of **uris**, **actions**, **insightIntents**, or **customization** match, the task is considered matched.
    -   If any task matches, the task and its dependent tasks will be executed in automatic mode.
    -   If all tasks fail to match, they are handled according to their **excludeFromAutoStart** configuration.
    

The following uses URI matching (similar to action and intent name matching) and customization matching as examples to describe how to add task matching rules to filter tasks.

**Scenario 1: URI Matching**

Suppose you want to automatically execute StartupTask\_004 and libentry\_006 tasks when a user taps a notification to jump to the notification details page. If **uri** in the Want when launching the notification details UIAbility is test://com.example.startupdemo/notification, you can match it via URI. Here is an example:

1.  Modify the **startup\_config.json** file in [Defining Startup Task Configuration](#defining-startup-task-configuration) to add **matchRules** for StartupTask\_004 and libentry\_006.
    
    {
      "startupTasks": \[
        {
          "name": "StartupTask\_004",
          "srcEntry": "./ets/startup/StartupTask\_004.ets",
          "runOnThread": "taskPool",
          "waitOnMainThread": false,
          "matchRules": {
            "uris": \[
              "test://com.example.startupdemo/notification"
            \]
          }
        },
      \],
      "appPreloadHintStartupTasks": \[
        {
          "name": "libentry\_006",
          "srcEntry": "libentry\_006.so",
          "runOnThread": "taskPool",
          "excludeFromAutoStart": true,
          "matchRules": {
            "uris": \[
              "test://com.example.startupdemo/notification"
            \]
          }
        }
      \],
      "configEntry": "./ets/startup/StartupConfig.ets"
    }
    

**Scenario 2: Customization Matching**

Suppose you want to automatically execute StartupTask\_006 and .so file preloading tasks with **excludeFromAutoStart=false** when a user taps a weather widget to jump to the weather screen. If the custom parameter **fromType** in the Want when launching the weather UIAbility is **card**, you can match it via customization. Here is an example:

1.  Modify the **MyStartupConfigEntry.ets** file in [Setting Startup Parameters](#setting-startup-parameters) and add [onRequestCustomMatchRule](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-appstartup-startupconfigentry#onrequestcustommatchrule20).
    
    import { StartupConfigEntry, Want } from '@kit.AbilityKit';
    // ···
    
    export default class MyStartupConfigEntry extends StartupConfigEntry {
    // ···
      onRequestCustomMatchRule(want: Want): string {
        if (want?.parameters?.fromType == 'card') {
          return 'ruleCard';
        }
        return '';
      }
    
    }
    
2.  Modify the **startup\_config.json** file in [Defining Startup Task Configuration](#defining-startup-task-configuration) to add **matchRules** for StartupTask\_006. The .so file preloading task does not support the **customization** field and is handled according to the **excludeFromAutoStart** configuration.
    
    {
      "startupTasks": \[
        {
          "name": "StartupTask\_006",
          "srcEntry": "./ets/startup/StartupTask\_006.ets",
          "runOnThread": "mainThread",
          "waitOnMainThread": false,
          "excludeFromAutoStart": true,
          "matchRules": {
            "customization": \[
              "ruleCard"
            \]
          }
        }
      \],
      "configEntry": "./ets/startup/StartupConfig.ets"
    }
    

## Setting the Startup Task Scheduling Phase

Starting from API version 21, configuring the startup task scheduling phase is supported. By default, startup tasks begin execution after the AbilityStage module is loaded but before the [AbilityStage.onCreate](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-abilitystage#oncreate) lifecycle callback. For large applications, loading the AbilityStage module can be time-consuming. You can set the **schedulerPhase** field of a startup task to **preAbilityStageLoad**. This schedules the task before the AbilityStage module loads, allowing it to execute concurrently with the module loading on an asynchronous thread, thereby reducing application startup time.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/9iuAcxIBRW-ls6pH9l7bgw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061916Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4A9BFEC9F490B4691D3CF24860CE9D18CD9C2DF562C89D7872C544B2BBCA4C89)

Scheduling the startup task before the AbilityStage module loads changes the original execution order. If the startup task has dependencies on the AbilityStage module being loaded, unexpected results may occur. You can follow the instructions provided in [Side Effects and Optimization of Module Loading](../../../../arkts/arkts-runtime/arkts-modularization/side-effects-and-optimization-of-module-loading/document.md) to adapt any dependent parts.

For example, the home page of an application needs to obtain feed stream data through network requests, and you want this task to run concurrently with the AbilityStage module loading on an asynchronous thread. Assuming the network request task is StartupTask\_004 defined in [Defining Startup Task Configuration](#defining-startup-task-configuration), the development procedure is as follows:

1.  Configure the task to be scheduled before the AbilityStage module loads. In the **startup\_config.json** file, set the **schedulerPhase** field of StartupTask\_004 to **preAbilityStageLoad**.
2.  Configure the task to execute concurrently with AbilityStage module loading on an asynchronous thread. Set the **runOnThread** field of StartupTask\_004 to **taskPool** and the **waitOnMainThread** field to **false**.

{
  "startupTasks": \[
    {
      "name": "StartupTask\_004",
      "srcEntry": "./ets/startup/StartupTask\_004.ets",
      "runOnThread": "taskPool",
      "waitOnMainThread": false,
      "schedulerPhase": "preAbilityStageLoad"
    }
  \],
  "configEntry": "./ets/startup/StartupConfig.ets"
}
