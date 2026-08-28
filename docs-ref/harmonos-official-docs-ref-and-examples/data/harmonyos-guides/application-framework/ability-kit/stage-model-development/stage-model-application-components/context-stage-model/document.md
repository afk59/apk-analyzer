# Context (Stage Model)

#### Overview

[Context](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-context) serves as the context environment for objects within an application. It provides basic information about the application, for example, [resourceManager](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-resource-manager) (resource management), [applicationInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-bundlemanager-applicationinfo) (current application information), and [area](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-contextconstant#areamode) (file partitions).

#### Comparison of Different Context Types

Both [UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-uiability) components and various derived classes of [ExtensionAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-extensionability) components have their own context classes. These include the base class Context, [ApplicationContext](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-applicationcontext), [AbilityStageContext](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-abilitystagecontext), [UIAbilityContext](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext), and [ExtensionContext](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-extensioncontext). For details about their relationships, see [Inheritance and Holding Relationships of Different Context Types](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-context#inheritance-and-holding-relationships-of-different-context-types).

The following table describes how to obtain different types of context and their usage scenarios.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0c/v3/OynsTiNjRP-T5WyugTCxJQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061915Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1915EDC8E15ADC23AC46DB8952A3126C8B1C07C5FA3264B753B4640913261EA5)

Different types of context possess distinct capabilities and cannot be substituted for or forcibly converted into one another. For example, [ApplicationContext](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-applicationcontext) is bound to the [setFontSizeScale](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-applicationcontext#applicationcontextsetfontsizescale13) API, which is not available in [UIAbilityContext](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext). Therefore, even if you forcibly convert UIAbilityContext to ApplicationContext, you will not be able to call the **setFontSizeScale** API.

**Table 1** Different context types

| Context Type | Description | Acquisition Method | Usage Scenario |
| :-- | :-- | :-- | :-- |
| [ApplicationContext](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-applicationcontext) | Global context of an application, providing application-level information and capabilities. | 
\- From API version 14 onwards, you can directly call [getApplicationContext](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-application#applicationgetapplicationcontext14) to obtain it.

\- In versions earlier than API version 14, you can obtain it by calling [getApplicationContext](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-context#getapplicationcontext) of a Context instance.

 | 

\- [Obtain basic information about the current application](#obtaining-basic-information).

\- [Obtain application file paths](#obtaining-application-file-paths).

\- [Obtain and modifying encryption levels](#obtaining-and-modifying-encryption-levels).

\- [Listen for application foreground/background changes](#listening-for-application-foregroundbackground-changes).

 |
| [AbilityStageContext](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-abilitystagecontext) | Context of a module, providing module-level information and capabilities. | 

\- To obtain the context of the current AbilityStage, you can directly access the [context](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-abilitystage#properties) property of the AbilityStage instance.

\- To obtain the context of another module in the same application, you can call [createModuleContext](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-application#applicationcreatemodulecontext).

 | 

\- Obtain basic information about the current module.

\- [Obtain module-level file paths](#obtaining-application-file-paths).

 |
| [UIAbilityContext](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext) | Context of a UIAbility, providing external information and capabilities of the UIAbility. | 

\- You can directly access the [context](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-uiability#properties) property through a UIAbility instance.

\- To load a UI component instance in the window of a UIAbility, call [getHostContext](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-uicontext-uicontext#gethostcontext12).

 | 

\- Obtain basic information about the current UIAbility.

\- Start other applications or atomic services, and connect to or disconnect from ServiceExtensionAbility components created by system applications.

\- Destroy the current UIAbility.

 |
| [ExtensionContext](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-extensioncontext) | Context of an ExtensionAbility. Each type of ExtensionContext provides different information and capabilities. | Directly access the context property through an ExtensionAbility instance. | 

The capabilities provided by the context corresponding to different types of ExtensionAbility vary. For example, [InputMethodExtensionContext](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inputmethod-extension-context) mainly provides the following capabilities:

\- Obtain the basic information about the InputMethodExtensionAbility.

\- Destroy the current input method.

 |
| [UIContext](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-uicontext-uicontext) | Context of a UI instance of ArkUI, providing capabilities related to UI operations. It is not directly related to the other types of context mentioned above. | 

\- To obtain the UI context within a UI component, directly call [getUIContext](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-custom-component-api#getuicontext).

\- If a Window instance exists, call [getUIContext](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-window-window#getuicontext10).

 | 

Use it for UI-related operations in the UI instance, for example:

\- Obtain the font of the current UI instance.

\- Display different types of dialog boxes.

\- Set the UI avoid mode when the soft keyboard is displayed.

 |

#### Acquisition of Context

If you need to obtain application resources, application paths, or use the methods provided by Context to implement operations such as application redirection, environment variable setting, data clearing, and permission obtaining, you need to obtain the corresponding context. This section describes how to obtain different types of context and where to use it.

## Obtaining ApplicationContext (Global Application Context)

[ApplicationContext](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-applicationcontext) provides capabilities such as listening for lifecycle changes of application components within the application, system memory changes, system environment changes, setting application language, setting application color mode, clearing application data, and revoking permissions granted by the user. It can be obtained in [UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-uiability), [ExtensionAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-extensionability), and [AbilityStage](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-abilitystage).

import { UIAbility, AbilityConstant, Want } from '@kit.AbilityKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    let applicationContext = this.context.getApplicationContext();
  }
}

## Obtains AbilityStageContext (Module-Level Context)

Compared with the base class Context, [AbilityStageContext](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-abilitystagecontext) additionally provides information such as [HapModuleInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-bundlemanager-hapmoduleinfo) and [Configuration](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-configuration).

import { AbilityStage } from '@kit.AbilityKit';

export default class MyAbilityStage extends AbilityStage {
  onCreate(): void {
    let abilityStageContext = this.context;
    // ...
  }
}

## Obtaining Context of Another Module in the Current Application (Module-Level Context)

Call [createModuleContext](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-application#applicationcreatemodulecontext) to obtain the context of another module in the current application. After obtaining the context, you can obtain the resource information of that module.

import { common, application } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = '\[CreateModuleContext\]';
const DOMAIN = 0xF811;

let storageEventCall = new LocalStorage();

@Entry(storageEventCall)
@Component
struct CreateModuleContext {
  private context = this.getUIContext().getHostContext() as common.UIAbilityContext;

  build() {
    Column() {
    // ···
      List({ initialIndex: 0 }) {
        ListItem() {
          Row() {
            // ···
          }
          .onClick(() => {
            let moduleName2: string = 'entry';
            application.createModuleContext(this.context, moduleName2)
              .then((data: common.Context) => {
                hilog.info(DOMAIN, TAG, \`CreateModuleContext success, data: ${JSON.stringify(data)}\`);
                if (data !== null) {
                  this.getUIContext().getPromptAction().showToast({
                    // Replace $r('app.string.success\_message') with the resource file you use.
                    message: $r('app.string.success\_message')
                  });
                }
              })
              .catch((err: BusinessError) => {
                hilog.error(DOMAIN, TAG, \`CreateModuleContext failed, err code:${err.code}, err msg: ${err.message}\`);
              });
          })
        }
        // ···
      }
    // ···
    }
    // ···
  }
}

## Obtaining UIAbilityContext (Context for the UIAbility)

Compared with the base class [Context](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-context), [UIAbilityContext](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext) additionally provides information such as **abilityInfo** and **currentHapModuleInfo**. UIAbilityContext can be used to obtain the UIAbility configuration information, such as the code path, bundle name, ability name, and environment status required by the application. It can also be used to obtain methods to operate the UIAbility instance, such as [startAbility()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext#startability), [connectServiceExtensionAbility()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext#connectserviceextensionability), and [terminateSelf()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext#terminateself).

-   You can use **this.context** to obtain the context of a UIAbility instance.
    
    import { UIAbility, AbilityConstant, Want } from '@kit.AbilityKit';
    
    export default class EntryAbility extends UIAbility {
      onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
        // Obtain the context of the UIAbility instance.
        let context = this.context;
      }
    }
    
-   Obtain the context of the UIAbility instance on the page.
    
    import { common, Want } from '@kit.AbilityKit'; // Import the context module.
    
    @Entry
    @Component
    struct EventHub {
      // Define context variables.
      private context = this.getUIContext().getHostContext() as common.UIAbilityContext;
    
      startAbilityTest(): void {
        let want: Want = {
          // Want parameter information.
        };
        this.context.startAbility(want);
      }
    
      // UI page display.
      build() {
        // ···
      }
    }
    
    You can also define variables after importing the context module but before using [UIAbilityContext](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext).
    
    import { common, Want } from '@kit.AbilityKit';
    
    @Entry
    @Component
    struct UIAbilityComponentsBasicUsage {
      startAbilityTest(): void {
        let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
        let want: Want = {
          // Want parameter information.
        };
        context.startAbility(want);
      }
    
      // UI page display.
      build() {
        // ···
      }
    }
    
-   To stop the [UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-uiability) instance after the service is not needed, call [terminateSelf()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext#terminateself).
    
    import { common } from '@kit.AbilityKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    
    const TAG = '\[UIAbilityComponentsUsage\]';
    const DOMAIN = 0xF811;
    @Entry
    @Component
    struct UIAbilityComponentsUsage {
      // UI page display.
      build() {
        Column() {
        // ···
          Button('FuncAbilityB')
            .onClick(() => {
              let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
              try {
                context.terminateSelf((err: BusinessError) => {
                  if (err.code) {
                    // Process service logic errors.
                    hilog.error(DOMAIN, TAG, \`terminateSelf failed, code is ${err.code}, message is ${err.message}.\`);
                    return;
                  }
                  // Carry out normal service processing.
                  hilog.info(DOMAIN, TAG, \`terminateSelf succeed.\`);
                });
              } catch (err) {
                // Capture the synchronization parameter error.
                let code = (err as BusinessError).code;
                let message = (err as BusinessError).message;
                hilog.error(DOMAIN, TAG, \`terminateSelf failed, code is ${code}, message is ${message}.\`);
              }
            })
        }
      }
    }
    

## Obtaining ExtensionAbilityContext (Context for the ExtensionAbility)

Obtain a scenario-specific [ExtensionContext](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-extensioncontext). For example, FormExtensionContext, which inherits from ExtensionContext, provides APIs related to widget services.

import { FormExtensionAbility, formBindingData } from '@kit.FormKit';
import { Want } from '@kit.AbilityKit';

export default class MyFormExtensionAbility extends FormExtensionAbility {
  onAddForm(want: Want) {
    let formExtensionContext = this.context;
    let dataObj1: Record<string, string> = {
      'temperature': '11c',
      'time': '11:00'
    };
    let obj1: formBindingData.FormBindingData = formBindingData.createFormBindingData(dataObj1);
    return obj1;
  }
}

#### Typical Usage Scenarios of Context

This topic describes how to use the context in the following scenarios:

-   [Obtaining Basic Information](#obtaining-basic-information)
-   [Obtaining Application File Paths](#obtaining-application-file-paths)
-   [Obtaining and Modifying Encryption Levels](#obtaining-and-modifying-encryption-levels)
-   [Listening for Application Foreground/Background Changes](#listening-for-application-foregroundbackground-changes)
-   [Listening for UIAbility Lifecycle Changes](#listening-for-uiability-lifecycle-changes)

## Obtaining Basic Information

Different types of Context classes, which inherit from [Context](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-context), default to inheriting the parent class's methods and properties, as well as having their own independent methods and properties.

You can obtain basic information about the current application, module, UIAbility, or ExtensionAbility through the context property (such as the resource manager object and application information). Below is an example of acquiring information for the UIAbility.

If you need to obtain resource objects across packages, see [Accessing Resources](../../../../../getting-started/resource-categories-and-access/document.md#accessing-resources).

import { UIAbility, AbilityConstant, Want } from '@kit.AbilityKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    // Obtain a resource manager.
    let resourceManager = this.context.getApplicationContext().resourceManager;
    // Obtain application information.
    let applicationInfo = this.context.getApplicationContext().applicationInfo;
  }
}

## Obtaining Application File Paths

The [base class Context](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-context) provides the capability of obtaining application file paths. [ApplicationContext](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-applicationcontext), [AbilityStageContext](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-abilitystagecontext), [UIAbilityContext](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext), and [ExtensionContext](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-extensioncontext) inherit this capability. However, the specific paths retrieved can differ based on the type of the context used.

-   [ApplicationContext](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-applicationcontext): This context provides access to the application-level file path, which is used to store global application information. Files in this path are removed when the application is uninstalled.
    
-   [AbilityStageContext](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-abilitystagecontext), [UIAbilityContext](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext), and [ExtensionContext](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-extensioncontext): These contexts provide access to [module-level](../../../../../getting-started/development-fundamentals/application-package-fundamentals/application-package-overview/document.md) file paths. Files in these paths are removed when the corresponding [HAP](../../../../../getting-started/development-fundamentals/application-package-fundamentals/application-package-development-and-usage/hap/document.md) or [HSP](../../../../../getting-started/development-fundamentals/application-package-fundamentals/application-package-development-and-usage/hsp/document.md) module is uninstalled. Uninstalling an HAP or HSP module does not affect files under the application-level path unless all HAP and HSP modules of the application are uninstalled.
    
    -   UIAbilityContext: This context can be used to obtain the file paths of the module containing the UIAbility.
    -   ExtensionContext: This context can be used to obtain the file paths of the module containing the ExtensionAbility.
    -   AbilityStageContext: Given that AbilityStageContext is initialized earlier than UIAbilityContext and ExtensionContext, it is typically used to obtain file paths within the AbilityStage.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/9v6AoPtmQ1au0JltpJC5fg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061915Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DA4C04B9558B9D0F74CDAA6059F2226E2EB6136816D2DAAB9FA95B75F6992A81)

The application file paths are a type of application sandbox paths. For details, see [Application Sandbox Directory](../../../../core-file-kit/application-files/application-sandbox/document.md).

**Table 1** Description of application file paths obtained by different types of contexts

| Name | Description | Path Obtained by ApplicationContext | Path Obtained by AbilityStageContext, UIAbilityContext, and ExtensionContext |
| :-- | :-- | :-- | :-- |
| bundleCodeDir | Bundle code directory. | <Path prefix>/el1/bundle | <Path prefix>/el1/bundle |
| cacheDir | Cache directory. | <Path prefix>/<Encryption level>/base/cache | <Path prefix>/<Encryption level>/base/**haps/<module-name>**/cache |
| filesDir | File directory. | <Path prefix>/<Encryption level>/base/files | <Path prefix>/<Encryption level>/base/**haps/<module-name>**/files |
| preferencesDir | Preferences directory. | <Path prefix>/<Encryption level>/base/preferences | <Path prefix>/<Encryption level>/base/**haps/<module-name>**/preferences |
| tempDir | Temporary directory. | <Path prefix>/<Encryption level>/base/temp | <Path prefix>/<Encryption level>/base/**haps/<module-name>**/temp |
| databaseDir | Database directory. | <Path prefix>/<Encryption level>/database | <Path prefix>/<Encryption level>/database/**<module-name>** |
| distributedFilesDir | Distributed file directory. | <Path prefix>/el2/distributedFiles | <Path prefix>/el2/distributedFiles/ |
| resourceDir11+ | 
Resource directory.

**NOTE**

You are required to manually create the **resfile** directory in **<module-name>\\resources**.

 | N/A | <Path prefix>/el1/bundle/**<module-name>**/resources/resfile |
| cloudFileDir12+ | Cloud file directory. | <Path prefix>/el2/cloud | <Path prefix>/el2/cloud/ |
| logFileDir22+ | Directory for storing log files. | <Path prefix>/el2/log | <Path prefix>/el2/log/ |

This section uses ApplicationContext to obtain **cacheDir** and **filesDir** as an example to describe how to obtain the application cache directory and application file directory, and how to use these paths to create and read/write files.

-   **Obtaining the Application Cache Directory**
    
    import { common } from '@kit.AbilityKit';
    
    @Entry
    @Component
    struct ApplicationContextCache {
      @State message: string = 'Hello World';
      private context = this.getUIContext().getHostContext() as common.UIAbilityContext;
    
      build() {
        Row() {
          Column() {
            Text(this.message)
            // ···
            Button() {
              Text('create file')
            // ···
                .onClick(() => {
                  let applicationContext = this.context.getApplicationContext();
                  // Obtain the application cache directory.
                  let cacheDir = applicationContext.cacheDir;
                })
            }
            // ···
          }
        // ···
        }
        // ···
      }
    }
    
-   **Obtaining the Application File Directory**
    
    import { common } from '@kit.AbilityKit';
    import { buffer } from '@kit.ArkTS';
    import { fileIo, ReadOptions } from '@kit.CoreFileKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    
    const TAG: string = '\[ApplicationContextFile\]';
    const DOMAIN\_NUMBER: number = 0xFF00;
    
    @Entry
    @Component
    struct ApplicationContextFile {
      @State message: string = 'Hello World';
      private context = this.getUIContext().getHostContext() as common.UIAbilityContext;
    
      build() {
        Row() {
          Column() {
            Text(this.message)
            // ···
            Button() {
              Text('create file')
                  // ···
                .onClick(() => {
                  let applicationContext = this.context.getApplicationContext();
                  // Obtain the application file path.
                  let filesDir = applicationContext.filesDir;
                  hilog.info(DOMAIN\_NUMBER, TAG, \`filePath: ${filesDir}\`);
                  // Create and open the file if it does not exist. Open the file if it already exists.
                  let file = fileIo.openSync(filesDir + '/test.txt', fileIo.OpenMode.READ\_WRITE | fileIo.OpenMode.CREATE);
                  // Write data to the file.
                  let writeLen = fileIo.writeSync(file.fd, 'Try to write str.');
                  hilog.info(DOMAIN\_NUMBER, TAG, \`The length of str is: ${writeLen}\`);
                  // Create an ArrayBuffer object with a size of 1024 bytes to store the data read from the file.
                  let arrayBuffer = new ArrayBuffer(1024);
                  // Set the offset and length to read.
                  let readOptions: ReadOptions = {
                    offset: 0,
                    length: arrayBuffer.byteLength
                  };
                  // Read the file content to the ArrayBuffer object and return the number of bytes that are actually read.
                  let readLen = fileIo.readSync(file.fd, arrayBuffer, readOptions);
                  // Convert the ArrayBuffer object into a Buffer object and output it as a string.
                  let buf = buffer.from(arrayBuffer, 0, readLen);
                  hilog.info(DOMAIN\_NUMBER, TAG, \`the content of file: ${buf.toString()}\`);
                  // Close the file.
                  fileIo.closeSync(file);
                })
            }
            // ···
          }
        // ···
        }
        // ···
      }
    }
    

## Obtaining and Modifying Encryption Levels

Encrypting application files enhances data security by preventing files from unauthorized access. Different application files require different levels of protection.

In practice, you need to select a proper encryption level based on scenario-specific requirements to protect application data security. The proper use of EL1 and the EL2 can efficiently improve the security. For details about the permissions required for a specific encryption level, see [AreaMode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-contextconstant#areamode) in [ContextConstant](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-contextconstant).

-   EL1: For private files, such as alarms and wallpapers, the application can place them in a directory with the device-level encryption (EL1) to ensure that they can be accessed before the user enters the password.
-   EL2: For sensitive files, such as personal privacy data, the application can place them in a directory with the user-level encryption (EL2).
-   EL3: For step recording, file download, or music playback that needs to read, write, and create files when the screen is locked, the application can place these files in EL3.
-   EL4: For files that are related to user security information and do not need to be read, written, or created when the screen is locked, the application can place them in EL4.
-   EL5: By default, sensitive user privacy files cannot be read or written on the lock screen. If such files need to be read or written on the lock screen, you can call [acquireAccess](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-screenlockfilemanager#screenlockfilemanageracquireaccess) to apply for reading or writing files before the screen is locked or create new files that can be read and written after the screen is locked. It is more appropriate to place these files in EL5.

You can obtain and set the encryption level by reading and writing the **area** attribute in [Context](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-context).

import { UIAbility, contextConstant, AbilityConstant, Want } from '@kit.AbilityKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    // Before storing common information, switch the encryption level to EL1.
    this.context.area = contextConstant.AreaMode.EL1; // Change the encryption level.
    // Store common information.

    // Before storing sensitive information, switch the encryption level to EL2.
    this.context.area = contextConstant.AreaMode.EL2; // Change the encryption level.
    // Store sensitive information.

    // Before storing sensitive information, switch the encryption level to EL3.
    this.context.area = contextConstant.AreaMode.EL3; // Change the encryption level.
    // Store sensitive information.

    // Before storing sensitive information, switch the encryption level to EL4.
    this.context.area = contextConstant.AreaMode.EL4; // Change the encryption level.
    // Store sensitive information.

    // Before storing sensitive information, switch the encryption level to EL5.
    this.context.area = contextConstant.AreaMode.EL5; // Change the encryption level.
    // Store sensitive information.
  }
}

// AreaContext.ets
import { contextConstant, common } from '@kit.AbilityKit';

@Entry
@Component
struct AreaContext {
  private context = this.getUIContext().getHostContext() as common.UIAbilityContext;

  build() {
    Column() {
    // ···
      List({ initialIndex: 0 }) {
        // ···
        ListItem() {
          Row() {
            // ···
          }
          .onClick(() => {
            // Before storing common information, switch the encryption level to EL1.
            if (this.context.area === contextConstant.AreaMode.EL2) { // Obtain the encryption level.
              this.context.area = contextConstant.AreaMode.EL1; // Change the encryption level.
              this.getUIContext().getPromptAction().showToast({
                message: 'SwitchToEL1'
              });
            }
            // Store common information.
          })
        }
        // ···
        ListItem() {
          Row() {
            // ···
          }
          .onClick(() => {
            // Before storing sensitive information, switch the encryption level to EL2.
            if (this.context.area === contextConstant.AreaMode.EL1) { // Obtain the encryption level.
              this.context.area = contextConstant.AreaMode.EL2; // Change the encryption level.
              this.getUIContext().getPromptAction().showToast({
                message: 'SwitchToEL2'
              });
            }
            // Store sensitive information.
          })
        }
        // ···
      }
    // ···
    }
    // ···
  }
}

## Listening for Application Foreground/Background Changes

You can use the capabilities of [ApplicationContext](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-applicationcontext) to listen for changes in the application's foreground and background state. When the application switches between foreground and background, corresponding callback functions can be triggered to execute methods that depend on the foreground/background state or to collect data on the frequency of application state changes.

The following uses [UIAbilityContext](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext) as an example.

import { UIAbility, ApplicationStateChangeCallback } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
  
const TAG = '\[LifecycleAbility\]';
const DOMAIN = 0xF811;

export default class LifecycleAbility extends UIAbility {
  onCreate() {
    let applicationStateChangeCallback: ApplicationStateChangeCallback = {
      onApplicationForeground() {
        hilog.info(DOMAIN, TAG, 'applicationStateChangeCallback onApplicationForeground');
      },
      onApplicationBackground() {
        hilog.info(DOMAIN, TAG, 'applicationStateChangeCallback onApplicationBackground');
      }
    }

    // 1. Obtain an applicationContext object.
    let applicationContext = this.context.getApplicationContext();
    try {
      // 2. Use applicationContext.on() to subscribe to the 'applicationStateChange' event.
      applicationContext.on('applicationStateChange', applicationStateChangeCallback);
    } catch (paramError) {
      hilog.error(DOMAIN, TAG, \`error: ${(paramError as BusinessError).code}, ${(paramError as BusinessError).message}\`);
    }
    hilog.info(DOMAIN, TAG, 'Register applicationStateChangeCallback');
  }
}

## Listening for UIAbility Lifecycle Changes

You can use [ApplicationContext](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-applicationcontext) to listen for lifecycle changes of a UIAbility. When the lifecycle of a [UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-uiability) changes, for example, a UIAbility is created, switched between the foreground and background, or destroyed, corresponding callback functions are invoked. In this way, the methods that depend on the UIAbility lifecycle can be executed, and the dwell time and access frequency of a specified page can be collected.

Each time the callback is registered, a listener lifecycle ID is returned, with the value incremented by 1 each time. The following uses [UIAbilityContext](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext) as an example.

import { AbilityConstant, AbilityLifecycleCallback, UIAbility, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { window } from '@kit.ArkUI';
import  { BusinessError } from '@kit.BasicServicesKit';

const TAG: string = '\[EntryLifecycleAbility\]';
const DOMAIN\_NUMBER: number = 0xFF00;

export default class EntryLifecycleAbility extends UIAbility {
  // Define a lifecycle ID.
  private lifecycleId: number = -1;

  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    // Define a lifecycle callback object.
    let abilityLifecycleCallback: AbilityLifecycleCallback = {
      // Called when a UIAbility is created.
      onAbilityCreate(uiAbility) {
        hilog.info(DOMAIN\_NUMBER, TAG, \`onAbilityCreate uiAbility.launchWant: ${JSON.stringify(uiAbility.launchWant)}\`);
      },
      // Called when a window is created.
      onWindowStageCreate(uiAbility, windowStage: window.WindowStage) {
        hilog.info(DOMAIN\_NUMBER, TAG, \`onWindowStageCreate uiAbility.launchWant: ${JSON.stringify(uiAbility.launchWant)}\`);
        hilog.info(DOMAIN\_NUMBER, TAG, \`onWindowStageCreate windowStage: ${JSON.stringify(windowStage)}\`);
      },
      // Called when the window becomes active.
      onWindowStageActive(uiAbility, windowStage: window.WindowStage) {
        hilog.info(DOMAIN\_NUMBER, TAG, \`onWindowStageActive uiAbility.launchWant: ${JSON.stringify(uiAbility.launchWant)}\`);
        hilog.info(DOMAIN\_NUMBER, TAG, \`onWindowStageActive windowStage: ${JSON.stringify(windowStage)}\`);
      },
      // Called when the window becomes inactive.
      onWindowStageInactive(uiAbility, windowStage: window.WindowStage) {
        hilog.info(DOMAIN\_NUMBER, TAG, \`onWindowStageInactive uiAbility.launchWant: ${JSON.stringify(uiAbility.launchWant)}\`);
        hilog.info(DOMAIN\_NUMBER, TAG, \`onWindowStageInactive windowStage: ${JSON.stringify(windowStage)}\`);
      },
      // Called when the window is destroyed.
      onWindowStageDestroy(uiAbility, windowStage: window.WindowStage) {
        hilog.info(DOMAIN\_NUMBER, TAG, \`onWindowStageDestroy uiAbility.launchWant: ${JSON.stringify(uiAbility.launchWant)}\`);
        hilog.info(DOMAIN\_NUMBER, TAG, \`onWindowStageDestroy windowStage: ${JSON.stringify(windowStage)}\`);
      },
      // Called when the UIAbility is destroyed.
      onAbilityDestroy(uiAbility) {
        hilog.info(DOMAIN\_NUMBER, TAG, \`onAbilityDestroy uiAbility.launchWant: ${JSON.stringify(uiAbility.launchWant)}\`);
      },
      // Called when the UIAbility is switched from the background to the foreground.
      onAbilityForeground(uiAbility) {
        hilog.info(DOMAIN\_NUMBER, TAG, \`onAbilityForeground uiAbility.launchWant: ${JSON.stringify(uiAbility.launchWant)}\`);
      },
      // Called when the UIAbility is switched from the foreground to the background.
      onAbilityBackground(uiAbility) {
        hilog.info(DOMAIN\_NUMBER, TAG, \`onAbilityBackground uiAbility.launchWant: ${JSON.stringify(uiAbility.launchWant)}\`);
      },
      // Called when UIAbility is continued on another device.
      onAbilityContinue(uiAbility) {
        hilog.info(DOMAIN\_NUMBER, TAG, \`onAbilityContinue uiAbility.launchWant: ${JSON.stringify(uiAbility.launchWant)}\`);
      }
    };
    // Obtain the application context.
    let applicationContext = this.context.getApplicationContext();
    try {
      // Register the application lifecycle callback.
      this.lifecycleId = applicationContext.on('abilityLifecycle', abilityLifecycleCallback);
    } catch (err) {
      let code = (err as BusinessError).code;
      let message = (err as BusinessError).message;
      hilog.error(DOMAIN\_NUMBER, TAG, \`Failed to register applicationContext. Code is ${code}, message is ${message}\`);
    }

    hilog.info(DOMAIN\_NUMBER, TAG, \`register callback number: ${this.lifecycleId}\`);
  }
  onDestroy(): void {
    // Obtain the application context.
    let applicationContext = this.context.getApplicationContext();
    try {
      // Deregister the application lifecycle callback.
      applicationContext.off('abilityLifecycle', this.lifecycleId);
    } catch (err) {
      let code = (err as BusinessError).code;
      let message = (err as BusinessError).message;
      hilog.error(DOMAIN\_NUMBER, TAG, \`Failed to unregister applicationContext. Code is ${code}, message is ${message}\`);
    }
  }
}
