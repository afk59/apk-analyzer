# On-Demand Feature Distribution (ArkTS)

#### Use Cases

As HarmonyOS apps continue to evolve, their features are becoming increasingly diverse. 80% of users tend to use just 20% of app features, while the remaining features are tailored to specific users. To prevent first-time app downloads from taking too long and using too much users' device space, AppGallery Kit offers on-demand distribution, which allows users to dynamically download enhanced features as needed.

#### Basic Concepts

On-demand distribution: An app is packaged into multiple installation packages, which contain all app code and static resources. The app downloaded from AppGallery contains only basic features. When a user needs to use enhanced features, they can download the corresponding installation packages from the server to their devices. (For details about app release, please refer to [Releasing a HarmonyOS App](https://developer.huawei.com/consumer/en/doc/app/agc-help-release-app-0000002271695230).)

#### Service Process

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/3NN89scvQbGjgiuWMe_0pA/en-us_image_0000002371732673.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062058Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2B11C1F01DF0ABDA1786E78716D56CEC895BB3ACABD3B745C890A16C4B3A6C08 "Click to enlarge")

1.  A user downloads the basic package of app A.
2.  The user requests enhanced features from the app.
3.  The app downloads the dynamic installation package through the API.
4.  The dynamic installation package is downloaded.
5.  The app notifies the user of the download result through the **on** API.

#### Restrictions

-   The app must be released on AppGallery.
-   On-demand feature distribution supports phones, tablets, and PCs/2-in-1 devices. Starting from 5.1.1(19), it also supports TVs.
-   On-demand feature distribution supports debugging using the Emulator for the Arm and x86 architectures.

#### API Description

On-demand feature distribution provides the following ArkTS APIs. For details, please refer to the [API reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-moduleinstallmanager).

| 
API

 | 

**Description**

 |
| :-- | :-- |
| 

[getInstalledModule](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-moduleinstallmanager#section9621184365412)(moduleName: string): [InstalledModule](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-moduleinstallmanager#section1518175355911)

 | 

Queries module installation information.

 |
| 

[createModuleInstallRequest](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-moduleinstallmanager#section0529646101115)(context: [common.UIAbilityContext](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext) | [common.ExtensionContext](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-extensioncontext)): [ModuleInstallRequest](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-moduleinstallmanager#section5451648162618)

 | 

Creates a request object for on-demand loading.

 |
| 

[addModule](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-moduleinstallmanager#section84452138473)(moduleName: string): [ReturnCode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-moduleinstallmanager#section44479181311)

 | 

Adds the name of the module to be loaded.

 |
| 

[fetchModules](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-moduleinstallmanager#section1375123411137)(moduleInstallRequest: [ModuleInstallRequest](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-moduleinstallmanager#section5451648162618)): Promise<[ModuleInstallSessionState](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-moduleinstallmanager#section1535385414136)\>

 | 

Requests on-demand loading and returns the result asynchronously.

 |
| 

[cancelTask](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-moduleinstallmanager#section48442523152)(taskId: string): [ReturnCode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-moduleinstallmanager#section44479181311)

 | 

Cancels a download task.

 |
| 

[showCellularDataConfirmation](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-moduleinstallmanager#section104451223191616)(context: [common.UIAbilityContext](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext) | [common.ExtensionContext](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-extensioncontext), taskId: string): [ReturnCode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-moduleinstallmanager#section44479181311)

 | 

Displays a mobile data reminder pop-up.

 |
| 

[on](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-moduleinstallmanager#section18484105013164)(type: 'moduleInstallStatus', callback: Callback<[ModuleInstallSessionState](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-moduleinstallmanager#section1535385414136)\>, timeout: number): void

 | 

Monitors the progress of the current app download task.

 |
| 

[off](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-moduleinstallmanager#section721141416172)(type: 'moduleInstallStatus', callback?: Callback<[ModuleInstallSessionState](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-moduleinstallmanager#section1535385414136)\>): void

 | 

Cancels monitoring the progress of the current app download task.

 |

#### Development Procedure

## Obtaining Module Installation Information

1.  Import the **moduleInstallManager** module and related common modules.
    
    //LoadInstallService.ets
    import { moduleInstallManager } from '@kit.AppGalleryKit';
    
2.  Construct an input parameter.
    
    The input parameter is the name of the module to be queried.
    
    const moduleName: string = 'AModule';
    
3.  Call [getInstalledModule](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-moduleinstallmanager#section9621184365412) by passing the parameter constructed in step 2.
    
    const moduleInfo: moduleInstallManager.InstalledModule = moduleInstallManager.getInstalledModule(moduleName);
    

## Creating a Request Object for On-Demand Loading

1.  Import the **moduleInstallManager** module and related common modules.
    
    //LoadInstallService.ets
    import { moduleInstallManager } from '@kit.AppGalleryKit';
    import type { common } from '@kit.AbilityKit';
    
2.  Construct an input parameter.
    
    The input parameter is the context of the current app. Only contexts of the [UIAbilityContext](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext) and [ExtensionContext](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-extensioncontext) types are supported. The context of the **UIAbilityContext** type is used to check whether the current app is running in the foreground. If the current app is not running in the foreground, the call will be rejected.
    
    const context: common.UIAbilityContext | common.ExtensionContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
    
3.  Call [createModuleInstallRequest](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-moduleinstallmanager#section0529646101115) by passing the parameter constructed in step 2.
    
    const myModuleInstallProvider: moduleInstallManager.ModuleInstallProvider = new moduleInstallManager.ModuleInstallProvider();
    const myModuleInstallRequest: moduleInstallManager.ModuleInstallRequest = myModuleInstallProvider.createModuleInstallRequest(context);
    

## Requesting On-Demand Loading

1.  Import the **moduleInstallManager** module and related common modules.
    
    //LoadInstallService.ets
    import type { common } from '@kit.AbilityKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    import { moduleInstallManager } from '@kit.AppGalleryKit';
    
2.  Construct an input parameter.
    
    The input parameter is the name of the module to be loaded on demand.
    
    const moduleNameA: string = 'AModule';
    const moduleNameB: string = 'BModule';
    
3.  Call [addModule](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-moduleinstallmanager#section84452138473) of [ModuleInstallRequest](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-moduleinstallmanager#section5451648162618) by passing the parameter constructed in step 2.
    
    let myModuleInstallRequest: moduleInstallManager.ModuleInstallRequest;
    try {
      const myModuleInstallProvider: moduleInstallManager.ModuleInstallProvider = new moduleInstallManager.ModuleInstallProvider();
      const context: common.UIAbilityContext | common.ExtensionContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
      myModuleInstallRequest = myModuleInstallProvider.createModuleInstallRequest(context);
      const aResult: moduleInstallManager.ReturnCode = myModuleInstallRequest.addModule(moduleNameA);
      const bResult: moduleInstallManager.ReturnCode = myModuleInstallRequest.addModule(moduleNameB);
      hilog.info(0, 'TAG', 'aResult:' + aResult + ' bResult:' + bResult);
    } catch (error) {
      hilog.error(0, 'TAG', \`addModule onError.code is ${error.code}, message is ${error.message}\`);
    }
    
4.  Call [fetchModules](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-moduleinstallmanager#section1375123411137) by passing **myModuleInstallRequest** constructed in step 3.
    
    try {
      moduleInstallManager.fetchModules(myModuleInstallRequest)
        .then(() => {
          hilog.info(0, 'TAG', 'Succeeded in fetching Modules data.');
        })
    } catch (error) {
      hilog.error(0, 'TAG', \`fetching Modules onError.code is ${error.code}, message is ${error.message}\`);
    }
    

## Using Dynamic Modules

Assume that app A consists of two packages: **entry.hap** and **AModulelib.hsp**. The **entry** package provides basic features, and the **AModulelib** package provides enhanced features. (For details about how to create a package, please click [here](../../../../getting-started/development-fundamentals/application-package-fundamentals/application-package-development-and-usage/document.md).) AppGallery provides only the **entry** package for users to download and install, while the **AModulelib** package can be dynamically downloaded through the [fetchModules](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-moduleinstallmanager#section1375123411137) API in the **entry** package. Methods and components in **AModulelib** are called using the [dynamic import](../../../../application-framework/arkts/arkts-runtime/arkts-modularization/dynamic-import/document.md) technology.

The implementation in **AModulelib** is as follows:

-   Set **deliveryWithInstall** to **false** in **module.json5** of the dynamic module **AModulelib** to indicate that **AModulelib** will not be downloaded for installation when a user proactively installs app A.
    
    {
      "module": {
        "name": "AModulelib",
        "deliveryWithInstall": false
      }
    }
    

-   Define the **add** method and **DateComponent** component in **AModulelib**. The **add** method is used for addition calculation, and **DateComponent** is used to display text.
    
    **Calc.ets** defines the **add** method as follows:
    
    export function add(a:number, b:number) {
      return a + b;
    }
    
    **DateComponent.ets** defines **DateComponent** as follows:
    
    @Component
    struct DateComponent {
      build() {
        Column() {
          Text('I am a component in **AModulelib**')
            .margin(10);
        }
        .width(300).backgroundColor(Color.Yellow);
      }
    }
    
    @Builder
    export function showDateComponent() {
      DateComponent()
    }
    

-   Export the **add** and **showDateComponent** methods from **AModulelib/Index.ets** of **AModulelib**.
    
    export { add } from './src/main/ets/utils/Calc';
    export { showDateComponent } from './src/main/ets/components/DateComponent';
    

The implementation in **entry** is as follows:

-   Add the dynamic dependency configuration to the basic **entry** module. **oh-package.json5** in **entry** uses **dynamicDependencies** to dynamically depend on the **AModulelib** module.
    
    {
      "dynamicDependencies": {
        "AModulelib": "file:../AModulelib"
      }
    }
    
-   Use the methods and components in the dynamic module **AModulelib** in **entry**. Before calling the functions of **AModulelib**, check whether **AModulelib** has been loaded. If **AModulelib** has not been loaded, load it by referring to [Requesting On-Demand Loading](#section1256946193314).
    
    import { moduleInstallManager } from '@kit.AppGalleryKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    import { BusinessError, Callback } from '@kit.BasicServicesKit';
    import { common } from '@kit.AbilityKit';
    
    @Entry
    @Component
    struct Index {
      @BuilderParam AModulelibComponent: Function;
      @State countTotal: number = 0;
      @State isShow: boolean = false;
    
      build() {
        Row() {
          Column() {
            Button(\`Call the **add** function in **AModulelib** to calculate 3+6\`)
              .onClick(() => {
                this.initAModulelib(() => {
                  import('AModulelib').then((ns: ESObject) => {
                    this.countTotal = ns.add(3, 6);
                  }).catch((error: BusinessError) => {
                    hilog.error(0, 'TAG', \`add onError.code is ${error.code}, message is ${error.message}\`);
                  })
                })
              });
            Text('Calculation result:' + this.countTotal)
              .margin(10);
            Button(\`Call the **showDateComponent** function in **AModulelib**\`)
              .onClick(() => {
                this.initAModulelib(() => {
                  import('AModulelib').then((ns: ESObject) => {
                    this.AModulelibComponent = ns.showDateComponent;
                    this.isShow = true;
                  }).catch((error: BusinessError) => {
                    hilog.error(0, 'TAG', \`showDateComponent onError.code is ${error.code}, message is ${error.message}\`);
                  })
                })
              }).margin({
              top: 10, bottom: 10
            });
            if (this.isShow) {
              this.AModulelibComponent()
            }
          }
          .width('100%')
        }
        .height('100%')
      }
    
      private showToastInfo(msg: string) {
        this.getUIContext().getPromptAction().showToast({
          message: msg,
          duration: 2000
        });
      }
    
      /\*\*
       \* Check whether the **AModulelib** package has been loaded.
       \*
       \* @param successCallBack Callback.
       \*/
      private initAModulelib(successCallBack: Callback<void>): void {
        try {
          const result: moduleInstallManager.InstalledModule = moduleInstallManager.getInstalledModule('AModulelib');
          if (result?.installStatus === moduleInstallManager.InstallStatus.INSTALLED) {
            hilog.info(0, 'TAG', 'AModulelib installed');
            successCallBack && successCallBack();
          } else {
            // If the **AModulelib** module has not been installed, call **fetchModules** to download it.
            hilog.info(0, 'TAG', 'AModulelib not installed');
            this.fetchModule('AModulelib', successCallBack)
          }
        } catch (error) {
          hilog.error(0, 'TAG', \`getInstalledModule onError.code is ${error.code}, message is ${error.message}\`);
        }
      }
    
      /\*\*
       \* Add an event listener.
       \*
       \* @param successCallBack Callback.
       \*/
      private onListenEvents(successCallBack: Callback<void>): void {
        const timeout = 3 \* 60; // Timeout interval, in seconds. The default maximum listening duration is 30 minutes (30 x 60 seconds).
        moduleInstallManager.on('moduleInstallStatus', (data: moduleInstallManager.ModuleInstallSessionState) => {
          // Return success.
          if (data.taskStatus === moduleInstallManager.TaskStatus.INSTALL\_SUCCESSFUL) {
            successCallBack && successCallBack();
            this.showToastInfo('install success');
          }
        }, timeout)
      }
    
      /\*\*
       \* Load a specified package.
       \*
       \* @param moduleName Name of the installation package to be loaded.
       \* @param successCallBack Callback.
       \*/
      private fetchModule(moduleName: string, successCallBack: Callback<void>) {
        try {
          hilog.info(0, 'TAG', 'handleFetchModules start');
          const context = this.getUIContext().getHostContext() as common.UIAbilityContext;
          const moduleInstallProvider: moduleInstallManager.ModuleInstallProvider =
            new moduleInstallManager.ModuleInstallProvider();
          const moduleInstallRequest: moduleInstallManager.ModuleInstallRequest =
            moduleInstallProvider.createModuleInstallRequest(context);
          if (!moduleInstallRequest) {
            hilog.warn(0, 'TAG', 'moduleInstallRequest is empty');
            return;
          }
          moduleInstallRequest.addModule(moduleName);
          moduleInstallManager.fetchModules(moduleInstallRequest)
            .then((data: moduleInstallManager.ModuleInstallSessionState) => {
              hilog.info(0, 'TAG', 'Succeeded in fetching Modules result.');
              if (data.code === moduleInstallManager.RequestErrorCode.SUCCESS) {
                this.onListenEvents(successCallBack)
              } else {
                hilog.info(0, 'TAG', 'fetchModules failure');
              }
            })
            .catch((error: BusinessError) => {
              hilog.error(0, 'TAG', \`fetchModules onError.code is ${error.code}, message is ${error.message}\`);
            })
        } catch (error) {
          hilog.error(0, 'TAG', \`handleFetchModules onError.code is ${error.code}, message is ${error.message}\`);
        }
      }
    }
    

## Performing Debugging

On-demand feature distribution provides you with access to the debug function, allowing you to debug your app during the integration process without the need to release your app on AppGallery. Assume that app A consists of two packages: **entry.hap** and **AModulelib.hsp**. The **entry** package provides basic features, and the **AModulelib** package provides enhanced features. (For details about how to create a package, please click [here](../../../../getting-started/development-fundamentals/application-package-fundamentals/application-package-development-and-usage/hap/document.md).)

1.  Use the [debug certificate](../../../../coding-and-debugging/configuring-a-debug-signature/document.md) to sign your app or atomic service. Compile locally to generate **entry.hap** and **AModulelib.hsp**. You can install the basic package either using [HDC commands](../../../../system/debugging-tools/performance-analysis-kit/command-line-tools/hdc/document.md#hdc-commands) or directly through DevEco Studio.
    
    hdc install entry.hap
    
2.  Enable the [developer debug mode](../../../../coding-and-debugging/debugging-your-app/developer-options/document.md#section530763213432): Go to **Settings**, tap the device model, tap the software version for seven consecutive times on the **About** screen, and tap **Enable** when the "Enable Developer options?" message is displayed.
    
3.  [Access the device sandbox path](../../../../coding-and-debugging/debugging-your-app/device-file-access/document.md#section48216711204) and, within the [app's encrypted data directory el2](../../../../application-framework/core-file-kit/application-files/application-sandbox/document.md#mappings-between-application-sandbox-paths-and-physical-paths), create the **cache/moduleinstall/<_ModuleName_\>** directory (where **<_ModuleName_\>** is **AModulelib** here). Then, upload the module's debug package **AModulelib.hsp** to the corresponding module directory.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/NT6qUpplQda15Xq_dAZA1w/en-us_image_0000002337734712.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062058Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=08E8C45D0291030FB73A691A6A53AE0A504D8B6672202428228F8BC309815BAC)
    
4.  Install the module's debug package by referring to [Creating a Request Object for On-Demand Loading](#section205574623317), [Requesting On-Demand Loading](#section1256946193314), or [Using Dynamic Modules](#section112161336173714), without the need of modifying parameters. Once the installation is successful, the files in the corresponding module directory will be automatically deleted.
