# Application Continuation Development

The application continuation feature allows an ongoing task (including the UI component status) of an application to be switched from a device to another and continue on the target device.

The following functionalities can be implemented:

-   Saving and restoring user-defined data (application service content).
-   Saving and restoring page route information and UI component status data.
-   Checking application compatibility.
-   Setting the mission continuation state (**ACTIVE** by default) dynamically.
    
    For example, for an editing application, only the text editing page needs to be migrated to the target device. In this case, you can use [setMissionContinueState](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext#setmissioncontinuestate10) for precise control.
    
-   Determining whether to restore the page stack (restored by default).
    
    If you want to customize the page to be displayed after the application is migrated to the target device, you can use [wantConstant.Params](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-wantconstant#params) for precise control.
    
-   Determining whether to exit the application on the source device after a successful migration (the application exits by default). In this case, [@ohos.app.ability.wantConstant (wantConstant)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-wantconstant) can be used for precise control.
    

#### Constraints

This feature can be used only when the following conditions are met:

-   **Supported devices**
    
    Devices running HarmonyOS NEXT Developer Preview0 or later.
    
-   **Constraints**
    -   The same HUAWEI ID is logged on both devices.
    -   WLAN and Bluetooth must be enabled on both devices, or Enhanced collaboration services is enabled at **Settings** > **More connectivity options** > **Advanced**.
    -   The continuation feature should be enabled on both devices by going to **Settings** > **More connectivity options**.
    -   The application must be installed on both devices.
    -   To ensure optimal user experience, the data transferred by **wantParam** in the **onContinue** callback must be less than 100 KB. If the data to be transferred exceeds 100 KB, use [Distributed Data Object](../../../application-framework/arkdata/distributed-application-data-sync/overview-of-cross-device-application-data-sync/document.md) to synchronize the data.

#### Available APIs

The following table lists the main APIs for implementing application continuation. For details, see [Reference Documents](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-uiability).

| 
**API**

 | 

**Description**

 |
| :-- | :-- |
| 

onContinue(wantParam : {\[key: string\]: Object}): OnContinueResult

 | 

Called by the source application to save the data required for migration and specify whether the migration is allowed.

-   **AGREE**: The migration is allowed.
-   **REJECT**: The migration is rejected, for example, when an application is abnormal in **onContinue()**.
-   **MISMATCH**: The application versions of the source and target devices do not match. The application on the source device can obtain the version of the target application from **onContinue**. If the ability continuation cannot be performed due to version mismatch, this error code is returned.

 |
| 

onCreate(want: Want, param: AbilityConstant.LaunchParam): void;

 | 

Called by the target to restore the data and UI page if the target uses cold start or the target is a multiton application and uses hot start.

 |
| 

onNewWant(want: Want, launchParams: AbilityConstant.LaunchParam): void;

 | 

Called by the target to restore the data and UI page if the target is a singleton application and uses hot start.

 |

#### How to Develop

1.  Enable the application continuation capability.
    
    In the **abilities** field of the **module.json5** file, set **continuable** to **true**, indicating that the UIAbility can be migrated. If this parameter is set to **false** (the default value), the UIAbility cannot be migrated.
    
    {
      "module": {
        ...
        "abilities": \[
          {
            ...
            "continuable": true,
          }
        \]
      }
    }
    
2.  Configure the application launch type. For details, see [UIAbility Component Launch Type](../../../application-framework/ability-kit/stage-model-development/stage-model-application-components/uiability-component/uiability-launch-type/document.md).
3.  Implement [onContinue()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-uiability#oncontinue) in the source UIAbility.
    
    When application data migration is triggered, **onContinue()** is called on the source end. You can implement the following in this callback:
    
    1.  Saving the data to migrate: You can save the data to migrate in KV pairs in **wantParam**.
    2.  (Optional) Checking application compatibility: You can obtain the application version on the target device from **wantParam.version** in **onContinue()** and compare it with the application version on the source device. If the version compatibility check fails, the application should notify users of the cause of the migration failure.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/Wgbrp7hFQ2agzDJaad1F9Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062129Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D25221E7DE80FE227723C09F7264E925F5F386C6EAD904CAFAADD641235F9315)
        
        If the compatibility issues have little or no impact on migration experience, you can skip this check.
        
    3.  Returning the migration result: You can check whether the migration is supported based on the return value of **onContinue()**. For details, see [AbilityConstant.OnContinueResult](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-abilityconstant#oncontinueresult).
    
    -   Certain fields (listed in the table below) in **wantParam** passed in to **onContinue()** are preconfigured in the system. You can use these fields for service processing. When defining custom **wantParam** data, do not use the same keys as the preconfigured ones to prevent data exceptions due to system overwrites. See the following table for more details.
        
        | 
        Field
        
         | 
        
        Description
        
         |
        | :-- | :-- |
        | 
        
        version
        
         | 
        
        Version number of the application on the target device.
        
         |
        | 
        
        targetDevice
        
         | 
        
        Network ID of the target device.
        
         |
        
    
    import { AbilityConstant, UIAbility } from '@kit.AbilityKit';
    import { promptAction } from '@kit.ArkUI';
    
    export default class EntryAbility extends UIAbility {
      onContinue(wantParam: Record<string, Object>) {
        const targetVersion  = wantParam.version;  // Obtain the version number of the target application.
        // The application can set the minimum compatible version based on the source version, which can be obtained from the versionCode field in the app.json5 file. This is to prevent incompatibility caused because the target version is too earlier.
        const versionThreshold: number = 0; // Replace the value with the minimum version number supported by the application.
        // Compatibility verification
        if (targetVersion < versionThreshold) {
          // It is recommended that users be notified of the reason why the migration is rejected if the version compatibility check fails.
          promptAction.showToast({
               message: 'The target application version is too early to continue. Update the application and try again.',
               duration: 2000
          })
          // Return MISMATCH when the compatibility check fails.
          return AbilityConstant.OnContinueResult.MISMATCH;
        }
        console.info(\`onContinue version = ${wantParam.version}, targetDevice: ${wantParam.targetDevice}\`)
        // Save the data to be migrated.
        const continueInput = 'Data to migrate';
        if (continueInput) {
          // Save the data to be migrated in the custom field (for example, data) of wantParam.
          wantParam\["data"\] = continueInput;
        }
         return AbilityConstant.OnContinueResult.AGREE;
      }
    }
    
4.  Restore data and load the UI.
    
    In the stage model, applications with different launch types call different APIs to restore data and load the UI, as shown below.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/TWIgJV4RQcSI9mjYIuYnWw/en-us_image_0000002220910158.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062129Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4D4F29F4202798F3E5D09EAFE2CD955539C1F39CEFC3ED07BDF665A9A336D592 "Click to enlarge")
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/Erh_4YfVQGirYPJGE9UyGA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062129Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AE107A8CEA54CB6F400E5CED4EEEC92C94CA4F535D87078791CA248A381B8126)
    
    1.  When an application is launched as a result of a migration, the **onWindowStageRestore** lifecycle callback, rather than **onWindowStageCreate()**, is triggered following **onCreate()** or **onNewWant()**. This sequence occurs for both cold and hot starts.
    2.  If you have performed some necessary initialization operations during application launch in **onWindowStageCreate()**, you must perform the same initialization operations in **onWindowStageRestore()** after the migration to avoid application exceptions.
    
    Implement **onCreate()** and **onNewWant()** in the UIAbility of the target device to implement data restore.
    
    -   Implementation example of **onCreate**
        
        -   The target device determines whether the startup is **LaunchReason.CONTINUATION** based on **launchReason** in **onCreate**.
            
        -   You can obtain the saved data from the **want** parameter.
            
        -   If a page with a page stack needs to be restored, call **restoreWindowStage()** before **onCreate()** or **onNewWant()** is executed. If the page stack does not need to be migrated, see [Migrating the Page Stack on Demand](#section34254151518).
            
        
        import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
        
        export default class EntryAbility extends UIAbility {
          storage : LocalStorage = new LocalStorage();
          onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
            if (launchParam.launchReason === AbilityConstant.LaunchReason.CONTINUATION) {
              // Obtain the saved data for restore.
              let continueInput = '';
              if (want.parameters !== undefined) {
                continueInput = JSON.stringify(want.parameters.data);
                console.info(\`continue input ${continueInput}\`)
              }
              // Trigger page restore.
              this.context.restoreWindowStage(this.storage);
            }
          }
        }
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/KOMerlagRqGDcRsx76bAkw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062129Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4DD2F220B30B0805525AAF394F8D94F9909B283FCF174AFFAD4C426316FDD9CA)
        
        The **restoreWindowStage(this.storage)** API must be executed in a synchronous API. If it is executed in an asynchronous callback, the page may fail to be loaded after application migration.
        
    -   For a singleton application, you must also implement **onNewWant()**, in the same way as **onCreate()**.
        
        Determine the migration scenario in **onNewWant()**, restore data, and trigger page restore.
        
        import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
        
        export default class EntryAbility extends UIAbility {
          storage : LocalStorage = new LocalStorage();
          onNewWant(want: Want, launchParam: AbilityConstant.LaunchParam): void {
            console.info(\`EntryAbility onNewWant ${AbilityConstant.LaunchReason.CONTINUATION}\`)
            if (launchParam.launchReason === AbilityConstant.LaunchReason.CONTINUATION) {
              // Obtain the saved data for restore.
              let continueInput = '';
              if (want.parameters !== undefined) {
                continueInput = JSON.stringify(want.parameters.data);
                console.info(\`continue input ${continueInput}\`);
              }
              this.context.restoreWindowStage(this.storage);
            }
          }
        }
        
    

#### Configuring Optional Migration Features

## Dynamically Setting the Migration State

The application continuation state can be dynamically set since API version 10. Specifically, the application can enable or disable migration based on the service scenario by calling [setMissionContinueState](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext#setmissioncontinuestate10).

| 
Value

 | 

Description

 |
| :-- | :-- |
| 

AbilityConstant.ContinueState.ACTIVE

 | 

Mission continuation is enabled for the application.

 |
| 

AbilityConstant.ContinueState.INACTIVE

 | 

Mission continuation is disabled for the application.

 |

**Setting the Migration State**

By default, **AbilityConstant.ContinueState.ACTIVE** is set for an application, which indicates that migration is enabled.

In special cases, for example, to enable migration only on a specific page or only when an event occurs, perform the following steps:

1.  Disable migration in the **onCreate** callback of the ability.
    
    // EntryAbility.ets
    import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
    export default class EntryAbility extends UIAbility {
      onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
        // ...
        this.context.setMissionContinueState(AbilityConstant.ContinueState.INACTIVE, (result) => {
          console.info(\`setMissionContinueState: ${JSON.stringify(result)}\`);
        });
        // ...
      }
    }
    

2.  To enable migration on a specific page, set it in the **onPageShow()** function of the page.
    
    // PageName.ets
    import { AbilityConstant, common } from '@kit.AbilityKit';
    @Entry
    @Component
    struct PageName {
      private context = getContext(this) as common.UIAbilityContext;
      build() {
        // ...
      }
      // ...
      onPageShow(){
      // When the page is displayed, set the migration state to ACTIVE.
        this.context.setMissionContinueState(AbilityConstant.ContinueState.ACTIVE, (result) => {
          console.info('setMissionContinueState ACTIVE result: ', JSON.stringify(result));
        });
      }
    }
    

3.  To enable migration for an event of a component, set the migration state in the event. The following uses the **onClick** event of the **Button** component as an example.
    
    // PageName.ets
    import { AbilityConstant, common } from '@kit.AbilityKit';
    @Entry
    @Component
    struct PageName {
      private context = getContext(this) as common.UIAbilityContext;
      build() {
        // ...
        Button() {
          //...
        }.onClick(()=>{
        // When the button is clicked, set the migration state to ACTIVE.
          this.context.setMissionContinueState(AbilityConstant.ContinueState.ACTIVE, (result) => {
            console.info('setMissionContinueState ACTIVE result: ', JSON.stringify(result));
          });
        })
      }
    }
    

**Ensuring Migration Continuity**

When the application on the target device is loaded, the application may have set its own task continuation state (for example, set the state to **INACTIVE** in **onCreate** during cold start or to **INACTIVE** during hot start since the peer has opened a page that cannot be migrated). To ensure a migration back to the source end, you must set the mission continuation state to **ACTIVE** in **onCreate** and **onNewWant**.

// EntryAbility.ets
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
export default class EntryAbility extends UIAbility {
  // ...
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    // ...
    // Set the migration status to migration allowed during cold start.
    this.context.setMissionContinueState(AbilityConstant.ContinueState.ACTIVE, (result) => {
      console.info(\`setMissionContinueState: ${JSON.stringify(result)}\`);
    });
  }
  onNewWant(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    // ...
    // Set the migration status to migration allowed during hot start.
    if (launchParam.launchReason === AbilityConstant.LaunchReason.CONTINUATION) {
      this.context.setMissionContinueState(AbilityConstant.ContinueState.ACTIVE, (result) => {
        console.info('setMissionContinueState ACTIVE result: ', JSON.stringify(result));
      });
    }
  }
  // ...
}

## Migrating the Page Stack on Demand

The application can dynamically determine whether to restore the page stack. By default, the page stack is restored. If the application on the target device does not use the default page stack restored, disable page stack migration and set the page to be displayed in **onWindowStageRestore()**. For details about the configuration, see [SUPPORT\_CONTINUE\_PAGE\_STACK\_KEY](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-wantconstant#params).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/abU5tD-dRZiAQQODmx8xsQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062129Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BE5A3F6782D32F2D6FA2FBDD4F8B58C3C4A11A95BB503BAD8D5E7239F964A7E6)

1.  Currently, only the page stack implemented based on the router module can be automatically restored. The page stack implemented using the **Navigation** component cannot be automatically restored.
2.  If an application uses the **Navigation** component for routing, you can disable page stack migration and save the page (or page stack) to be migrated in **want**, and manually load the specified page on the target device.

The index and second routes exist in the page stack of the application on the source device. In such situation, specify the page to restore, rather than using the page stack of the source device.

Example: Page stack information does not need to be automatically migrated during application migration.

// EntryAbility.ets
import { AbilityConstant, UIAbility, wantConstant } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
export default class EntryAbility extends UIAbility {
  // ...
  onContinue(wantParam: Record<string, Object>) {
    console.info(\`onContinue version = ${wantParam.version}, targetDevice: ${wantParam.targetDevice}\`);
    wantParam\[wantConstant.Params.SUPPORT\_CONTINUE\_PAGE\_STACK\_KEY\] = false;
    return AbilityConstant.OnContinueResult.AGREE;
  }
  // ...
  onWindowStageRestore(windowStage: window.WindowStage) {
      // Set the page to be displayed after the migration.
    windowStage.loadContent('pages/Index', (err, data) => {
      if (err.code) {
        console.info('Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
        return;
      }
      console.info('Succeeded in loading the content. Data: %{public}s', JSON.stringify(data) ?? '');
    });
  }
}

## Exiting the Application on Demand

You can determine whether to exit the application on the source device after a successful migration (the application exits by default). To prevent the application on the source device from automatically exiting after a successful migration, set the [SUPPORT\_CONTINUE\_SOURCE\_EXIT\_KEY](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-wantconstant#params) parameter.

Example: An application on the source device does not exit after a successful migration.

import { AbilityConstant, UIAbility, wantConstant } from '@kit.AbilityKit';
export default class EntryAbility extends UIAbility {
  // ...
  onContinue(wantParam: Record<string, Object>) {
    console.info(\`onContinue version = ${wantParam.version}, targetDevice: ${wantParam.targetDevice}\`);
    wantParam\[wantConstant.Params.SUPPORT\_CONTINUE\_SOURCE\_EXIT\_KEY\] = false;
    return AbilityConstant.OnContinueResult.AGREE;
  }
  // ...
}

## Supporting Cross-Device Migration Between Different Abilities in the Same Application

Generally, the same ability is involved during a cross-device migration. However, different ability names may be configured for the same service on different device types, resulting in different abilities. To support migration in this scenario, you can configure the **continueType** tag under **abilities** in the **module.json5** file for association. The values of the **continueType** tag of the two abilities must be the same. The following is an example:

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/qnhoTW8oQyiynKHfBJps8A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062129Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0A5BEED99E9FB70167405B7E058CCBA8457695402933D7576823891C7205CC7A)

-   The value of **continueType** must be unique in an application. The value is a string of a maximum of 127 bytes consisting of letters, digits, and underscores (\_).
-   The **continueType** tag is a string array. If multiple fields are configured, only the first field takes effect.

 // Device A
   {
     "module": {
       // ...
       "abilities": \[
         {
           // ...
           "name": "Ability-deviceA",
           "continueType": \['continueType1'\], // Configuration of the continueType tag.
         }
       \]
     }
   }

   // Device B
   {
     "module": {
       // ...
       "abilities": \[
         {
           // ...
           "name": "Ability-deviceB",
           "continueType": \['continueType1'\], // Same as the value of continueType on device A.
         }
       \]
     }
   }

## Migrating Abilities with Different Bundle Names in the Same Application Across Devices

An application may use different bundle names on different devices. To support migration in this scenario, configure **abilities** in the **module.json5** file of the application as follows:

-   **continueBundleName**: bundle name of the application on the peer device.
-   **continueType**: The same value must be used.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/F9DWDVAARmSm26O-ydalVg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062129Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4D081E050588C7D300255394E8E45388028DFD110166DF9B7B5238CC73A8D446)
    
    -   The value of **continueType** must be unique in an application. The value is a string of a maximum of 127 bytes consisting of letters, digits, and underscores (\_).
    -   The **continueType** tag is a string array. If multiple fields are configured, only the first field takes effect.
    

Example:

An application with different bundle names is migrated between device A and device B. The bundle name of the application on device A is com.demo.example1, and that on device B is com.demo.example2.

// In the configuration file for device A, set continueBundleName to the bundle name of the application on device B.
{
  "module": {
    // ...
    "abilities": \[
      {
        "name": "EntryAbility"
        // ...
        "continueType": \['continueType'\], 
        "continueBundleName": \["com.demo.example2"\], // continueBundleName is set to com.demo.example2, which is the bundle name of the application on device B.
      }
    \]
  }
}

// In the configuration file for device B, set continueBundleName to the bundle name of the application on device A.
{
  "module": {
    // ...
    "abilities": \[
      {
        "name": "EntryAbility"
        // ...
        "continueType": \['continueType'\], 
        "continueBundleName": \["com.demo.example1"\], // continueBundleName is set to com.demo.example1, which is the bundle name of the application on device A.
      }
    \]
  }
}

## Quickly Launching the Target Application

By default, the application on the target device (target application for short) is not started immediately after the migration is initiated. Instead, it is started only after the data is migrated from the source device to the target device. To start the application immediately after the user initiates the continuation and improve user experience, you can add the suffix **\_ContinueQuickStart** to the **continueType** tag in the **module.json5** file to configure the quick start of the target application. Example:

{
  "module": {
    // ...
    "abilities": \[
      {
        // ...
        "name": "EntryAbility"
        "continueType": \['EntryAbility\_ContinueQuickStart'\], // If continueType is configured, add the suffix '\_ContinueQuickStart' to the tag value. If continueType is not set, set the value in the _AbilityName_ + '\_ContinueQuickStart' format.
      }
    \]
  }
}

If the quick start is configured for an application, the application will receive an **onCreate()** or **onNewWant()** request with **launchReason.PREPARE\_CONTINUATION** when the user initiates the continuation, and then receive an **onNewWant()** request with **launchReason.CONTINUATION**, as shown in the following table.

| 
Scenario

 | 

Lifecycle Function

 | 

launchParam.launchReason

 |
| :-- | :-- | :-- |
| 

First start request

 | 

onCreate (in the case of cold start);

onNewWant (in the case of hot start)

 | 

AbilityConstant.LaunchReason.PREPARE\_CONTINUATION

 |
| 

Second start request

 | 

onNewWant

 | 

AbilityConstant.LaunchReason.CONTINUATION

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/QsZkWXYkSreXF7s90UhHEg/en-us_image_0000002255989845.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062129Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DF16B96C32C9999F23D1383721C326BDB5D14AC70BF711FC01A9D38F6ABCBEFE)

If fast start is not configured, only one start request is received.

| 
Scenario

 | 

Lifecycle Function

 | 

launchParam.launchReason

 |
| :-- | :-- | :-- |
| 

One start request

 | 

onCreate (in the case of cold start);

onNewWant (in the case of hot start)

 | 

AbilityConstant.LaunchReason.CONTINUATION

 |

After quick startup is configured, **onCreate()** or **onNewWant()** can be implemented as follows:

import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG: string = '\[MigrationAbility\]';
const DOMAIN\_NUMBER: number = 0xFF00;

export default class MigrationAbility extends UIAbility {
  storage : LocalStorage = new LocalStorage();

  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    hilog.info(DOMAIN\_NUMBER, TAG, '%{public}s', 'Ability onCreate');

    // 1. Quick start is configured. Trigger the lifecycle callback when the application is launched immediately.
    if (launchParam.launchReason === AbilityConstant.LaunchReason.PREPARE\_CONTINUATION) {
      // If the application data to migrate is large, add a loading screen here (for example, displaying "loading" on the screen).
      // Handle issues related to custom redirection and timing.
      // ...
    }
  }

  onNewWant(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    hilog.info(DOMAIN\_NUMBER, TAG, 'onNewWant');

    // 1. Quick start is configured. Trigger the lifecycle callback when the application is launched immediately.
    if (launchParam.launchReason === AbilityConstant.LaunchReason.PREPARE\_CONTINUATION) {
      // If the application data to migrate is large, add a loading screen here (for example, displaying "loading" on the screen).
      // Handle issues related to custom redirection and timing.
      // ...
    }

    // 2. Trigger the lifecycle callback when the migration data is restored.
    if (launchParam.launchReason === AbilityConstant.LaunchReason.CONTINUATION) {
      // Restore the saved data from want.parameters.
      let continueInput = '';
      if (want.parameters !== undefined) {
        continueInput = JSON.stringify(want.parameters.data);
        hilog.info(DOMAIN\_NUMBER, TAG, \`continue input ${JSON.stringify(continueInput)}\`);
      }
      // Trigger page restore.
      this.context.restoreWindowStage(this.storage);
    }
  }
}

#### Migrating Data Using distributedDataObject

If the size of the data to be migrated is greater than 100 KB or the data to be migrated is stored in files, you can use **distributedDataObject** to implement data migration. For details about the working principles and APIs, see [Cross-Device Sync of Distributed Data Objects](../../../application-framework/arkdata/distributed-application-data-sync/cross-device-sync-of-distributed-data-objects-arkts/document.md).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/08/v3/G8SC8s5iRGSMsDnPbsc3LA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062129Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9F6FE3560A08EBE81090B95F42E57064E0375F3F346D3F52AFC7C12B424CAD35)

It is difficult to obtain the time when file synchronization is complete when file migration is implemented by using cross-device file access. Since API version 12, **distributedDataObject** is recommended to migrate assets instead of cross-device file access. File migration implemented through cross-device file access can still be used.

## Applying for Permission

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/GqCutz6NRc-8dpeHJZvp2A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062129Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=27867A07917550C2200574DE09676057F66813DDB967F4AC5ABC5B7ABE639356)

-   Since API version 12, the ohos.permission.DISTRIBUTED\_DATASYNC permission is not required.
-   In API version 11 and earlier versions, perform the following operations:

1.  Declare the ohos.permission.DISTRIBUTED\_DATASYNC permission. For details, see [Declaring Permissions](../../../system/security/application-access-control/application-permission-management/requesting-application-permissions/declaring-permissions/document.md).
2.  The application needs to request the ohos.permission.DISTRIBUTED\_DATASYNC permission from users when it is started for the first time or proceeds to the continuation page. For details, see [Requesting User Authorization](../../../system/security/application-access-control/application-permission-management/requesting-application-permissions/requesting-user-authorization/document.md).

## Basic Data Migration

The procedure of migrating basic data using **distributedDataObject** is similar to the preceding development procedure. Data is saved using **onContinue()** on the source device and is restored using the **onCreate()** or **onNewWant()** API on the target device.

1.  Create a distributed data object in [onContinue()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-uiability#oncontinue) of the source UIAbility and save the data. The execution process is as follows:
    
    1.  Use **create()** in the **onContinue()** API to create a distributed data object and fill the data to be migrated into the distributed data object.
    2.  Call **genSessionId()** to generate a networking ID for the distributed data object, and call **setSessionId()** with this ID to add the device to the network and activate the distributed data object.
    3.  Use **save()** to persist the activated distributed data object. This allows the target application to still obtain data even if the application on the source device exits.
    4.  Pass the generated **sessionId** to the target application through **want**. The **sessionId** is used to activate the distributed data object of the target application and transfer data to the target application.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/r9OhJRPjSV6wSvNE3bcdGA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062129Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3521C3F299A2298E920D7E9BB5D83618E1F8ED00132F458C5A4E619B59DA393A)
    
    -   The distributed data object needs to be activated and then persisted. Therefore, **save()** must be called after **setSessionId()** is called.
    -   To prevent the application on the source device from exiting before the data migrated to the target device is saved, use **await** to wait until **save()** is complete. Since API version 12, asynchronous **onContinue()** APIs are provided for such scenario.
    -   Currently, the **sessionId** field in **wantParams** is used by the system during migration. You are advised to define other key values in **wantParams** to store the session ID generated for the distributed data object to avoid exceptions.
    
    Sample code:
    
    import { distributedDataObject } from '@kit.ArkData';
    import { UIAbility, AbilityConstant } from '@kit.AbilityKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    const TAG: string = '\[MigrationAbility\]';
    const DOMAIN\_NUMBER: number = 0xFF00;
    
    // Service data definition
    class ParentObject {
      mother: string
      father: string
    
      constructor(mother: string, father: string) {
        this.mother = mother
        this.father = father
      }
    }
    
    // Characters, numbers, Boolean values, and objects can be passed via the distributed data object.
    class SourceObject {
      name: string | undefined
      age: number | undefined
      isVis: boolean | undefined
      parent: ParentObject | undefined
    
      constructor(name: string | undefined, age: number | undefined, isVis: boolean | undefined, parent: ParentObject | undefined) {
        this.name = name
        this.age = age
        this.isVis = isVis
        this.parent = parent
      }
    }
    
    export default class MigrationAbility extends UIAbility {
      d\_object?: distributedDataObject.DataObject;
    
      async onContinue(wantParam: Record<string, Object>): Promise<AbilityConstant.OnContinueResult> {
        // ...
        let parentSource: ParentObject = new ParentObject('jack mom', 'jack Dad');
        let source: SourceObject = new SourceObject("jack", 18, false, parentSource);
    
        // Create a distributed data object.
        this.d\_object = distributedDataObject.create(this.context, source);
    
        // Generate a networking ID for the distributed data object and activate the distributed data object.
        let dataSessionId: string = distributedDataObject.genSessionId();
        this.d\_object.setSessionId(dataSessionId);
    
        // Save the network ID in want and pass it to the target application.
        wantParam\['dataSessionId'\] = dataSessionId;
    
        // Persist the distributed data object to ensure that the data object on the target device can be restored even if the source application exits after migration.
        // Obtain networkId of the target device from wantParam.targetDevice as an input parameter.
        await this.d\_object.save(wantParam.targetDevice as string).then((result:
          distributedDataObject.SaveSuccessResponse) => {
          hilog.info(DOMAIN\_NUMBER, TAG, \`Succeeded in saving. SessionId: ${result.sessionId},
            version:${result.version}, deviceId:${result.deviceId}\`);
        }).catch((err: BusinessError) => {
          hilog.error(DOMAIN\_NUMBER, TAG, 'Failed to save. Error: ', JSON.stringify(err) ?? '');
        });
      }
    }
    
2.  In **onCreate()** or **onNewWant()** of the target UIAbility, add the same networking ID to the distributed data object on the target device to restore data.
    
    1.  Create an empty distributed data object for receiving data to be restored.
    2.  Read the networking ID of the distributed data object from **want**.
    3.  Register **on()** to listen for data changes. In the callback of the event whose status is **restore**, implement the service operation to be performed when the data restore is complete.
    4.  Call **setSessionId()** to connect the target application to the network and activate the distributed data object.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/EyiS9NZIQvG3y0T5b9wcWQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062129Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A1177D7F7624323E96DF4CB101DB04175779FBE22A28737FA957F387E2B11BA5)
    
    -   The distributed data object of the target application connected to the network cannot be a temporary variable. Since **on()** for the distributed data object uses an asynchronous callback and may be executed after **onCreate()** or **onNewWant()** is complete. The temporary variable will be released, which causes a null pointer exception. You can use class member variables to avoid this exception.
    -   Before a distributed data object on the target device is activated, set the attribute of the object used to create the distributed data object to **undefined**. Otherwise, the data on the source end will be overwritten by new data after the distributed data object is connected to the network, and data restore will fail.
    -   Before activating a distributed data object, call **on()** of the object to register listening to prevent data restore failure caused by missing the restore event.
    
    Sample code:
    
    import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
    import { distributedDataObject } from '@kit.ArkData';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    const TAG: string = '\[MigrationAbility\]';
    const DOMAIN\_NUMBER: number = 0xFF00;
    
    // The definition of the sample data object is the same as the preceding definition.
    
    export default class MigrationAbility extends UIAbility {
      d\_object?: distributedDataObject.DataObject;
    
      onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
        if (launchParam.launchReason === AbilityConstant.LaunchReason.CONTINUATION) {
          // ...
          // Invoke the encapsulated distributed data object processing function.
          this.handleDistributedData(want);
        }
      }
    
      onNewWant(want: Want, launchParam: AbilityConstant.LaunchParam): void {
        if (launchParam.launchReason === AbilityConstant.LaunchReason.CONTINUATION) {
          if (want.parameters !== undefined) {
            // ...
          // Invoke the encapsulated distributed data object processing function.
            this.handleDistributedData(want);
          }
        }
      }
    
      handleDistributedData(want: Want) {
        // Create an empty distributed data object.
        let remoteSource: SourceObject = new SourceObject(undefined, undefined, undefined, undefined);
        this.d\_object = distributedDataObject.create(this.context, remoteSource);
    
        // Obtain the networking ID of the distributed data object.
        let dataSessionId = '';
        if (want.parameters !== undefined) {
          dataSessionId = want.parameters.dataSessionId as string;
        }
        // Add a data change listener.
        this.d\_object.on("status", (sessionId: string, networkId: string, status: 'online' | 'offline' | 'restored') => {
          hilog.info(DOMAIN\_NUMBER, TAG, "status changed " + sessionId + " " + status + " " + networkId);
          if (status === 'restored') {
            if (this.d\_object) {
              // When the "restored" status is received, read data from the distributed data object.
              hilog.info(DOMAIN\_NUMBER, TAG, "restored name:" + this.d\_object\['name'\]);
              hilog.info(DOMAIN\_NUMBER, TAG, "restored parents:" + JSON.stringify(this.d\_object\['parent'\]));
            }
          }
        });
        // Activate the distributed data object.
        this.d\_object.setSessionId(dataSessionId);
      }
    }
    

## Migrating File Assets

For file data such as images and documents, you need to convert the data to the **commonType.Asset** type and then encapsulate the data into distributed data objects for migration. The migration implementation is similar to that of common distributed data objects. The following describes only the differences.

-   On the source device, save the file assets to be migrated to the distributed data object **DataObject**. The procedure is as follows:

1.  Copy file assets to the distributed file directory. For details, see **Basic File APIs**.
2.  Create an **Asset** object for the file in the distributed file directory.
3.  Save the **Asset** object as the root attribute of the distributed data object.

Then, the implementation is the same as that of a common data object migration. The data object can be connected to the network and stored persistently.

Example:

// Import modules.
import { UIAbility, AbilityConstant } from '@kit.AbilityKit';
import { distributedDataObject, commonType } from '@kit.ArkData';
import { fileIo, fileUri } from '@kit.CoreFileKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@ohos.base';
const TAG: string = '\[MigrationAbility\]';
const DOMAIN\_NUMBER: number = 0xFF00;

// Define the data object.
class ParentObject {
  mother: string
  father: string

  constructor(mother: string, father: string) {
    this.mother = mother
    this.father = father
  }
}

class SourceObject {
  name: string | undefined
  age: number | undefined
  isVis: boolean | undefined
  parent: ParentObject | undefined
  attachment: commonType.Asset | undefined // Add the Asset attribute.

  constructor(name: string | undefined, age: number | undefined, isVis: boolean | undefined,
    parent: ParentObject | undefined, attachment: commonType.Asset | undefined) {
    this.name = name
    this.age = age
    this.isVis = isVis
    this.parent = parent
    this.attachment = attachment;
  }
}

export default class MigrationAbility extends UIAbility {
  d\_object?: distributedDataObject.DataObject;

  async onContinue(wantParam: Record<string, Object>): Promise<AbilityConstant.OnContinueResult> {
    // ...

    // 1. Write the asset to the distributed file directory.
    let distributedDir: string = this.context.distributedFilesDir;  // Obtain the distributed file path.
    let fileName: string = '/test.txt';                        // File name
    let filePath: string = distributedDir + fileName;          // File path

    try {
      // Create a file in the distributed directory.
      let file = fileIo.openSync(filePath, fileIo.OpenMode.READ\_WRITE | fileIo.OpenMode.CREATE);
      hilog.info(DOMAIN\_NUMBER, TAG, 'Create file success.');
      // Write content to the file. (If the asset is an image, the image can be converted into a buffer and then written.)
      fileIo.writeSync(file.fd, '\[Sample\] Insert file content here.');
      // Close the file.
      fileIo.closeSync(file.fd);
    } catch (error) {
      let err: BusinessError = error as BusinessError;
      hilog.error(DOMAIN\_NUMBER, TAG, \`Failed to openSync / writeSync / closeSync. Code: ${err.code}, message: ${err.message}\`);
    }

    // 2. Create an asset object using the file in the distributed file directory.
    let distributedUri: string = fileUri.getUriFromPath(filePath); // Obtain the URI of the distributed file.

    // Obtain file parameters.
    let ctime: string = '';
    let mtime: string = '';
    let size: string = '';
    await fileIo.stat(filePath).then((stat: fileIo.Stat) => {
      ctime = stat.ctime.toString ();  // Creation time
      mtime = stat.mtime.toString();  // Modification time
      size = stat.size.toString();    // File size
    })

    // Create an Asset object.
    let attachment: commonType.Asset = {
      name: fileName,
      uri: distributedUri,
      path: filePath,
      createTime: ctime,
      modifyTime: mtime,
      size: size,
    }

    // 3. Create a distributed data object with the asset object set as its root attribute.
    let parentSource: ParentObject = new ParentObject('jack mom', 'jack Dad');
    let source: SourceObject = new SourceObject("jack", 18, false, parentSource, attachment);
    this.d\_object = distributedDataObject.create(this.context, source);

    // Generate the network ID, activate the distributed data object, and save the data persistently.
    // ...
}

-   An **Asset** object with attributes of **undefined** needs to be created on the target device, using as the root attribute of the distributed data object. When **on()** returns the event whose status is **restored**, data, including the asset, has been synchronized to the target device.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/wP5iSSvvQs6dSJ_wL3SQWA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062129Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0F3D85DD9B2D79873D9E125F24008CDE596C65E22C6B2E34F172E4486F635624)

When creating a distributed data object on the target device, do not use **undefined** to initialize the asset in **SourceObject**. You need to create an **Asset** object with empty attributes. Otherwise, asset synchronization fails.

Sample code:

import { UIAbility, Want } from '@kit.AbilityKit';
import { distributedDataObject, commonType } from '@kit.ArkData';
import { hilog } from '@kit.PerformanceAnalysisKit';
const TAG: string = '\[MigrationAbility\]';
const DOMAIN\_NUMBER: number = 0xFF00;

export default class MigrationAbility extends UIAbility {
  d\_object?: distributedDataObject.DataObject;

  handleDistributedData(want: Want) {
    // ...
    // Create an Asset object with attributes of undefined.
    let attachment: commonType.Asset = {
      name: '',
      uri: '',
      path: '',
      createTime: '',
      modifyTime: '',
      size: '',
    }

    // Use the Asset object to create a distributed data object. Other basic attributes can be undefined.
    let source: SourceObject = new SourceObject(undefined, undefined, undefined, undefined, attachment);
    this.d\_object = distributedDataObject.create(this.context, source);

    this.d\_object.on("status", (sessionId: string, networkId: string, status: 'online' | 'offline' | 'restored') => {
        if (status === 'restored') {
          // When the callback returns "restored", the distributed asset object synchronization is complete.
          hilog.info(DOMAIN\_NUMBER, TAG, "restored attachment:" + JSON.stringify(this.d\_object\['attachment'\]));
        }
    });
    // ...
  }
}

If multiple assets in an application need to be synchronized, use either of the following methods:

1.  Implement each asset as a root attribute of the distributed data object. Use this method if the number of assets to be migrated is fixed.
2.  Convert an array of assets into an object for transfer. Use this method if the number of assets to be migrated dynamically changes (for example, a user selects an uncertain number of images). Currently, the asset array cannot be directly transferred as a root attribute.

For the implementation of method 1, you can add more assets by referring to the procedure for adding an asset. The following is sample code for implementing method 2:

// Import modules.
import { distributedDataObject, commonType } from '@kit.ArkData';
import { UIAbility } from '@kit.AbilityKit';

// Define the data object.
class SourceObject {
  name: string | undefined
  assets: Object | undefined  // Add an Object attribute to the distributed data object.

  constructor(name: string | undefined, assets: Object | undefined) {
    this.name = name
    this.assets = assets;
  }
}

// This function is used to convert an asset array to a record.
GetAssetsWrapper(assets: commonType.Assets): Record<string, commonType.Asset> {
  let wrapper: Record<string, commonType.Asset> = {}
  let num: number = assets.length;
  for (let i: number = 0; i < num; i++) {
    wrapper\[\`asset${i}\`\] = assets\[i\];
  }
  return wrapper;
}

export default class MigrationAbility extends UIAbility {
  d\_object?: distributedDataObject.DataObject;

  async onContinue(wantParam: Record<string, Object>): AbilityConstant.OnContinueResult {
    // ...

    // Create multiple asset objects.
    let attachment1: commonType.Asset = {
      // ...
    }

    let attachment2: commonType.Asset = {
      // ...
    }

    // Insert the asset objects into an asset array.
    let assets: commonType.Assets = \[\];
    assets.push(attachment1);
    assets.push(attachment2);

    // Convert the asset array to a Record Object and use it to create a distributed data object.
    let assetsWrapper: Object = this.GetAssetsWrapper(assets);
    let source: SourceObject = new SourceObject("jack", assetsWrapper);
    this.d\_object = distributedDataObject.create(this.context, source);

    // ...
}
