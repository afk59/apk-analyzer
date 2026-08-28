# Application Preloading

#### Overview

Starting from API version 20, the application preloading feature is provided. This feature preloads applications to a specific stage when system resources are sufficient, based on user usage patterns. When a user launches an application, the startup time is reduced because part of the application has already been loaded, which helps enhance user experience and the competitiveness of the application.

This feature is particularly suitable for applications that take a long time to start due to the loading of large amounts of resources, such as large gaming applications and large office applications.

#### Constraints

-   Currently, this feature is supported only on 2-in-1 devices.
    
-   Preloading is supported only for the AbilityStage and UIAbility of the entry module. Regardless of the preloading stage, the entry module must be configured with an entry UIAbility. For details, see step 2 in [How to Develop](#how-to-develop).
    
-   After an application is configured for preloading, whether preloading actually occurs and the specific timing of preloading are determined by the system based on user habits and other information. You cannot intervene in this process.
    

#### Working Principles

When system resources are sufficient, the system preloads the application to a specific stage to improve startup speed. Currently, three preloading stages are supported. You can choose one based on the time-consuming stages of the application's cold start.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/cKSjC9hlRY2zTq5sJdqlAw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061916Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D2D8B5E0D857EF36C730EAA00A85CEF577262429E8FB93298C8A4C6CD765773B)

During application preloading, no UI is displayed. Therefore, no operations related to UI display, interaction, or user visibility should be included at any preloading stage. It is also essential to ensure that all functions operate normally and user experience is not affected when the user officially launches the application.

-   **processCreated**: preloads the application to the stage where the process is created. When this stage is configured, the preloading feature creates an empty process and initializes the application, but no lifecycle callbacks are triggered.
    
-   **abilityStageCreated**: preloads the application to the stage where the [AbilityStage](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-abilitystage) is created. When this stage is configured, the preloading feature creates an empty process and initializes the application, and then triggers the [onCreate](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-abilitystage#oncreate) callback of the [AbilityStage](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-abilitystage) of the entry module.
    
-   **windowStageCreated**: preloads the application to the stage where the [WindowStage](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-window-windowstage) is created. When this stage is configured, the preloading feature creates an empty process and initializes the application, and then triggers the [onCreate](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-abilitystage#oncreate) callback of the [AbilityStage](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-abilitystage) of the entry module. It then launches the entry UIAbility of the entry module and triggers its [onCreate](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-uiability#oncreate) and [onWindowStageCreate](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-uiability#onwindowstagecreate) callbacks. You can obtain the launch reason in the [onCreate](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-uiability#oncreate) callback of the UIAbility through the enum [launchParam.launchReason](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-abilityconstant#launchreason). The enumerated value **PRELOAD** indicates that the current UIAbility is launched by preloading.
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/lmgFm884SMWbgmpg2R4dvQ/en-us_image_0000002568764083.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061916Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7DCE962F6B365CB079E29878BEBA807748C5577C6CDFF085F966905180362188)

#### How to Develop

1.  Declare the preloading stage supported by the application.
    
    For example, to preload the application to the **windowStageCreated** stage, configure the [appPreloadPhase](../../../../../getting-started/development-fundamentals/application-configuration-files-in-stage-model/app-json5-configuration-file/document.md#tags-in-the-configuration-file) tag in the [app.json5](../../../../../getting-started/development-fundamentals/application-configuration-files-in-stage-model/app-json5-configuration-file/document.md) file.
    
    {
      "app": {
        "bundleName": "com.demo.preloadtest",
        "vendor": "example",
        "versionCode": 1000000,
        "versionName": "1.0.0",
        "icon": "$media:layered\_image",
        "label": "$string:app\_name",
        "appPreloadPhase": "windowStageCreated"
      }
    }
    
2.  Configure the entry UIAbility (automatically configured by default when you create a project).
    
    1.  For example, for an EntryAbility, in the [module.json5](../../../../../getting-started/development-fundamentals/application-configuration-files-in-stage-model/module-json5-configuration-file/document.md) file of the entry module, set **mainElement** to **EntryAbility**, and add **"entity.system.home"** to **entities** and **"ohos.want.action.home"** to **actions** in the **skills** tag of **EntryAbility**.
        
    2.  If [appPreloadPhase](../../../../../getting-started/development-fundamentals/application-configuration-files-in-stage-model/app-json5-configuration-file/document.md#tags-in-the-configuration-file) in the [app.json5](../../../../../getting-started/development-fundamentals/application-configuration-files-in-stage-model/app-json5-configuration-file/document.md) file is set to **windowStageCreated**, set **launchType** of the EntryAbility in the entry module's [module.json5](../../../../../getting-started/development-fundamentals/application-configuration-files-in-stage-model/module-json5-configuration-file/document.md) file to [singleton](../uiability-component/uiability-launch-type/document.md#singleton) or [specified](../uiability-component/uiability-launch-type/document.md#specified).
        
    
    {
      "module": {
        "name": "entry",
        "type": "entry",
        "mainElement": "EntryAbility",
        // ...
        "abilities": \[
          {
            "name": "EntryAbility",
            "srcEntry": "./ets/entryability/EntryAbility.ets",
            "launchType": "singleton",
            "skills": \[
              {
                "entities": \[
                  "entity.system.home"
                \],
                "actions": \[
                  "ohos.want.action.home"
                \]
              }
            \]
            // ...
          }
        \]
      }
    }
    
3.  (Optional) Obtain the launch reason of the UIAbility.
    
    When **appPreloadPhase** is set to **windowStageCreated**, you can obtain the launch reason in the [onCreate](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-uiability#oncreate) lifecycle callback of the UIAbility through the enumerated value of [launchParam.launchReason](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-abilityconstant#launchreason). The enumerated value **PRELOAD** indicates that the current UIAbility is launched by preloading.
    
    import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
    
    export default class EntryAbility extends UIAbility {
      onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
        console.info(\`EntryAbility onCreate, LaunchReason:${launchParam.launchReason}\`);
        // Check whether the UIAbility is started by preloading.
        let isPreloadStart = launchParam.launchReason === AbilityConstant.LaunchReason.PRELOAD;
        // ...
      }
    }
