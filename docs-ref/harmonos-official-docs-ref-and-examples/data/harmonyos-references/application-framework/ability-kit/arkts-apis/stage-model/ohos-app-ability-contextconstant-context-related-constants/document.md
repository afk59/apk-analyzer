# @ohos.app.ability.contextConstant (Context-related Constants)

The ContextConstant module defines context-related enums, including the file encryption partition level and process mode of the UIAbility after it is started.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/JMhzDEIAQnaoiRgW_kqnjw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062205Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BCAFE9E090EA01F02A44F11522F6D4BAD470E9FC3904BDA54E0373598AC8339C)

The initial APIs of this module are supported since API version 9. Newly added APIs will be marked with a superscript to indicate their earliest API version.

The APIs of this module can be used only in the stage model.

#### Modules to Import

import { contextConstant } from '@kit.AbilityKit';

#### AreaMode

Enumerates the file encryption levels, which are used to ensure data security for applications across different scenarios. You can select the appropriate encryption level based on the application requirements to protect user data.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| EL1 | 0 | 
Device-level encryption. Directories with this encryption level are accessible after the device is powered on.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| EL2 | 1 | 

User-level encryption. Directories with this encryption level are accessible only after the device is powered on and the password is entered (for the first time).

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| EL311+ | 2 | 

User-level encryption. The file permissions vary according to their scenarios.

\- An open file is always readable and writable regardless of whether the screen is locked.

\- When the screen is locked, a closed file cannot be opened, read, or written. When the screen is unlocked, such a file can be opened, read, and written.

\- When the screen is locked, a file can be created and then opened and written but not read. When the screen is unlocked, a file can be created and then opened, read, and written.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| EL411+ | 3 | 

User-level encryption. The file permissions vary according to their scenarios.

\- When the screen is locked, an open file is not readable or writable. When the screen is unlocked, such a file is readable and writable.

\- When the screen is locked, a closed file cannot be opened, read, or written. When the screen is unlocked, such a file can be opened, read, and written.

\- When the screen is locked, a file cannot be created. When the screen is unlocked, a file can be created and then opened, read, and written.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| EL512+ | 4 | 

Application-level encryption. The file permissions vary according to their scenarios.

\- An open file is always readable and writable regardless of whether the screen is locked.

When the screen is locked, a closed file can be opened, read, and written only if the reserved key is obtained by calling [Access](../../both-models-recommended/ohos-ability-screenlockfilemanager-sensitive-data-access-management-under-lock-s/document.md#screenlockfilemanageracquireaccess). When the screen is unlocked, such a file can be opened, read, and written.

A file can be created and then opened, read, and written regardless of whether the screen is locked.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |

#### ProcessMode12+

Enumerates the process modes of the UIAbility after it is started.

As a property of [StartOptions](../ohos-app-ability-startoptions-optional-parameters-of-startability/document.md), **ProcessMode** takes effect only in [UIAbilityContext.startAbility](../../dependent-elements-and-definitions/application/uiabilitycontext/document.md#startability-1) and is used to specify the process mode of the target UIAbility.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Device behavior differences**: This value takes effect only on 2-in-1 devices and tablets. If it is used on other devices, error code 801 is returned.

| Name | Value | Description |
| :-- | :-- | :-- |
| NEW\_PROCESS\_ATTACH\_TO\_PARENT | 1 | 
A new process is created, the UIAbility is started on the process, and the process exits along with the parent process.

**Constraints**:

In this mode, the target UIAbility and caller must be in the same application.

 |
| NEW\_PROCESS\_ATTACH\_TO\_STATUS\_BAR\_ITEM | 2 | 

A new process is created, the UIAbility is started on the process, and the process is bound to the status bar icon.

**Constraints**:

In this mode, the target UIAbility and caller must be in the same application, and the application must have an icon in the status bar.

 |
| ATTACH\_TO\_STATUS\_BAR\_ITEM | 3 | 

The UIAbility is started, and the process of the UIAbility is bound to the status bar icon.

**Constraints**:

In this mode, the target UIAbility and caller must be in the same application, and the application must have an icon in the status bar.

 |

**Example**

import { UIAbility, Want, StartOptions, contextConstant } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onForeground() {
    let want: Want = {
      deviceId: '',
      bundleName: 'com.example.myapplication',
      abilityName: 'MainAbility2'
    };
    let options: StartOptions = {
      processMode: contextConstant.ProcessMode.NEW\_PROCESS\_ATTACH\_TO\_STATUS\_BAR\_ITEM,
      startupVisibility: contextConstant.StartupVisibility.STARTUP\_HIDE
    };

    try {
      this.context.startAbility(want, options, (err: BusinessError) => {
        if (err.code) {
          // Process service logic errors.
          console.error(\`startAbility failed, code is ${err.code}, message is ${err.message}\`);
          return;
        }
        // Carry out normal service processing.
        console.info('startAbility succeed');
      });
    } catch (err) {
      // Process input parameter errors.
      let code = (err as BusinessError).code;
      let message = (err as BusinessError).message;
      console.error(\`startAbility failed, code is ${code}, message is ${message}\`);
    }
  }
}

#### StartupVisibility12+

Enumerates the visibility statuses of the UIAbility after it is started.

If the target UIAbility is set to invisible, the window of the target UIAbility is not displayed in the foreground, there is no icon in the dock, and the **onForeground** lifecycle of the target UIAbility is not triggered.

As a property of [StartOptions](../ohos-app-ability-startoptions-optional-parameters-of-startability/document.md), **StartupVisibility** takes effect only in [UIAbilityContext.startAbility](../../dependent-elements-and-definitions/application/uiabilitycontext/document.md#startability-1) and specifies the visibility of the target UIAbility after it is started.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Device behavior differences**: This value takes effect only on 2-in-1 devices and tablets. If it is used on other devices, error code 801 is returned.

| Name | Value | Description |
| :-- | :-- | :-- |
| STARTUP\_HIDE | 0 | The target UIAbility is hidden after it is started in the new process. The **onForeground** lifecycle of the UIAbility is not invoked. |
| STARTUP\_SHOW | 1 | The target UIAbility is displayed normally after it is started in the new process. |

**Example**

See [ContextConstant.ProcessMode](#processmode12).

#### Scenarios20+

Enumerates the scenarios where the [onNewWant](../ohos-app-ability-uiability-ability-with-ui/document.md#onnewwant) lifecycle callback is not triggered. It is used in the [setOnNewWantSkipScenarios](../../dependent-elements-and-definitions/application/uiabilitycontext/document.md#setonnewwantskipscenarios20) API.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| SCENARIO\_MOVE\_MISSION\_TO\_FRONT | 0x00000001 | When sharing the screen, the system brings the UIAbility selected by the user to the foreground. |
| SCENARIO\_SHOW\_ABILITY | 0x00000002 | A scenario where the [showAbility](../../dependent-elements-and-definitions/application/uiabilitycontext/document.md#showability12) API is called to move the UIAbility to the foreground. |
| SCENARIO\_BACK\_TO\_CALLER\_ABILITY\_WITH\_RESULT | 0x00000004 | A scenario where the [backToCallerAbilityWithResult](../../dependent-elements-and-definitions/application/uiabilitycontext/document.md#backtocallerabilitywithresult12) API is called to move the UIAbility to the foreground. |

**Example**

import { AbilityConstant, contextConstant, UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    let scenarios: number = contextConstant.Scenarios.SCENARIO\_MOVE\_MISSION\_TO\_FRONT |
      contextConstant.Scenarios.SCENARIO\_SHOW\_ABILITY |
      contextConstant.Scenarios.SCENARIO\_BACK\_TO\_CALLER\_ABILITY\_WITH\_RESULT;

    try {
      this.context.setOnNewWantSkipScenarios(scenarios).then(() => {
        // Carry out normal service processing.
        console.info('setOnNewWantSkipScenarios succeed');
      }).catch((err: BusinessError) => {
        // Process service logic errors.
        console.error(\`setOnNewWantSkipScenarios failed, code is ${err.code}, message is ${err.message}\`);
      });
    } catch (err) {
      // Process input parameter errors.
      let code = (err as BusinessError).code;
      let message = (err as BusinessError).message;
      console.error(\`setOnNewWantSkipScenarios failed, code is ${code}, message is ${message}\`);
    }
  }
}
