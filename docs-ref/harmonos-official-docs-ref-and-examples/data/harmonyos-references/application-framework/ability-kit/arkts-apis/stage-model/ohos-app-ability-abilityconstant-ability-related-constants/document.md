# @ohos.app.ability.AbilityConstant (Ability-related Constants)

AbilityConstant provides enums related to abilities, including application launch reasons ([LaunchReason](#launchreason)), last exit reasons ([LastExitReason](#lastexitreason)), and migration results ([OnContinueResult](#oncontinueresult)).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/lIGGrmaoQ1-v-OuYLq-hLQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062204Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E8B46562F97DB703A20C85423D7B05848D4F2F4F90A26F3E3A692FBFE0289361)

-   The initial APIs of this module are supported since API version 9. Newly added APIs will be marked with a superscript to indicate their earliest API version.
    
-   The APIs of this module can be used only in the stage model.
    

#### Modules to Import

import { AbilityConstant } from '@kit.AbilityKit';

#### Constants

**System capability**: SystemCapability.Ability.AbilityBase

**Atomic service API**: This API can be used in atomic services since API version 20.

| Name | Type | Value | Description |
| :-- | :-- | :-- | :-- |
| REASON\_MESSAGE\_DESKTOP\_SHORTCUT20+ | string | "ReasonMessage\_DesktopShortcut" | The UIAbility is launched via a home screen shortcut. If this string is obtained from the **launchReasonMessage** property in [LaunchParam](#launchparam), the UIAbility is initiated by touching a shortcut on the home screen. |

#### LaunchParam

Describes the launch parameters, which mainly include the ability launch reasons and reasons for the last exit. The parameter values are automatically passed in by the system when the ability is launched. You do not need to change the values.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

| Name | Type | Read-only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| launchReason | [LaunchReason](#launchreason) | No | No | 
An enumerated value indicating the reason for ability launch (for example, recovery from a fault, intent invocation, or atomic service sharing). For details, see [LaunchReason](#launchreason).

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| launchReasonMessage18+ | string | No | Yes | 

Detailed message that describes the reason for the ability launch.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| lastExitReason | [LastExitReason](#lastexitreason) | No | No | 

An enumerated value indicating the reason for the last exit of the ability.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| lastExitMessage12+ | string | No | No | 

Detailed message that describes the reason for the last exit of the ability.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| lastExitDetailInfo18+ | [LastExitDetailInfo](#lastexitdetailinfo18) | No | Yes | 

Key runtime information for the last exit of the ability (including process ID, exit timestamp, and RSS memory value).

**Atomic service API**: This API can be used in atomic services since API version 18.

 |

#### LaunchReason

Enumerates the ability launch reasons. You can use it together with the value of **launchParam.launchReason** in [onCreate(want, launchParam)](../ohos-app-ability-uiability-ability-with-ui/document.md#oncreate) of the UIAbility to complete different operations.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| UNKNOWN | 0 | 
Unknown reason.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| START\_ABILITY | 1 | 

The ability is started by calling [startAbility](../../dependent-elements-and-definitions/application/uiabilitycontext/document.md#startability).

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| CALL | 2 | 

The ability is started by calling [startAbilityByCall](../../dependent-elements-and-definitions/application/uiabilitycontext/document.md#startabilitybycall).

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| CONTINUATION | 3 | 

The ability is started by means of cross-device migration.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| APP\_RECOVERY | 4 | 

The ability is automatically started when the application is restored from a fault.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| SHARE10+ | 5 | 

The ability is started by means of atomic service sharing.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| AUTO\_STARTUP11+ | 8 | The ability is automatically started upon system boot. |
| INSIGHT\_INTENT11+ | 9 | 

The ability is started by the InsightIntent framework.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| PREPARE\_CONTINUATION12+ | 10 | 

The ability is started in advance during cross-device migration.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| PRELOAD20+ | 11 | 

The ability is started through preloading.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |

**Example**

import { UIAbility, Want, AbilityConstant } from '@kit.AbilityKit';

export default class MyAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    if (launchParam.launchReason === AbilityConstant.LaunchReason.START\_ABILITY) {
      console.info('The ability has been started by the way of startAbility.');
    }
  }
}

#### LastExitReason

Enumerates the reasons for the last exit of the ability. You can use it together with the value of **launchParam.lastExitReason** in [onCreate()](../ohos-app-ability-uiability-ability-with-ui/document.md#oncreate) of the UIAbility to complete different operations.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| UNKNOWN | 0 | 
Unknown reason.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| ABILITY\_NOT\_RESPONDING(deprecated) | 1 | 

The Ability component does not respond.

Note: This enum is supported since API version 9 and deprecated since API version 10. You are advised to use **APP\_FREEZE**.

 |
| NORMAL | 2 | 

The user closes the application, and the application exits normally.

**Atomic service API**: This API can be used in atomic services since API version 11.

Note: If the application process is forcibly terminated using methods not provided by Ability Kit, such as calling [process.exit()](../../../../arkts/arkts-apis/ohos-process-obtaining-process-information/document.md#processexitdeprecated) or using the kernel **kill** command, the reason for the last exit is also reported as **NORMAL**.

 |
| CPP\_CRASH10+ | 3 | 

The ability exits due to [process crash](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/cppcrash-guidelines).

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| JS\_ERROR10+ | 4 | 

The ability exits due to a JS\_ERROR fault triggered when an application has a JS syntax error that is not captured by developers.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| APP\_FREEZE10+ | 5 | 

The ability exits due to [application freeze](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/appfreeze-guidelines).

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| PERFORMANCE\_CONTROL10+ | 6 | 

The ability exits due to system performance problems, for example, insufficient device memory.

**Atomic service API**: This API can be used in atomic services since API version 11.

Note: This API will be deprecated. You are advised to use **RESOURCE\_CONTROL** instead.

 |
| RESOURCE\_CONTROL10+ | 7 | 

The ability exits due to improper use of system resources. The specific error cause can be obtained through [LaunchParam.lastExitMessage](#launchparam). The possible causes are as follows:

\- **CPU Highload**: The CPU load is high.

\- **CPU\_EXT Highload**: A fast CPU load detection is carried out.

\- **IO Manage Control**: An I/O management and control operation is carried out.

\- **App Memory Deterioration**: The application memory usage exceeds the threshold.

\- **Temperature Control**: The temperature is too high or too low.

\- **Memory Pressure**: The system is low on memory, triggering process termination in ascending order of priority.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| UPGRADE10+ | 8 | 

The application exits due to an upgrade.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| USER\_REQUEST18+ | 9 | 

The ability exits because it receives a request from the multitasking center.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| SIGNAL18+ | 10 | 

The ability exits because it receives a kill signal from the system.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |

**Example**

import { UIAbility, Want, AbilityConstant } from '@kit.AbilityKit';

export default class MyAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    if (launchParam.lastExitReason === AbilityConstant.LastExitReason.APP\_FREEZE) {
      console.info('The ability has exit last because the ability was not responding.');
    }
    if (launchParam.lastExitReason === AbilityConstant.LastExitReason.RESOURCE\_CONTROL) {
      console.info(\`The ability has exited last because the rss control, the lastExitReason is ${launchParam.lastExitReason}, the lastExitMessage is ${launchParam.lastExitMessage}.\`);
    }
  }
}

#### LastExitDetailInfo18+

Describes the key runtime information of the process where the ability last exited.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

| Name | Type | Read-only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| pid | number | No | No | 
ID of the process where the ability last exited.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| processName | string | No | No | 

Name of the process.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| uid | number | No | No | 

UID of the application.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| exitSubReason | number | No | No | 

Specific reason for the last exit of the ability.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| exitMsg | string | No | No | 

Reason why the process was killed.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| rss | number | No | No | 

Actual memory usage of the process, in KB.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| pss | number | No | No | 

Actual physical memory usage of the process, in KB.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| timestamp | number | No | No | 

Exact time when the ability last exited.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| processState20+ | [appManager.ProcessState](../../both-models-recommended/ohos-app-ability-appmanager-application-management/document.md#processstate10) | No | Yes | 

Process status of the ability when it last exited.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |

**Example**

import { UIAbility, Want, AbilityConstant } from '@kit.AbilityKit';

export default class MyAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    if (launchParam.lastExitDetailInfo) {
      console.info(\`pid: ${launchParam.lastExitDetailInfo.pid}
      \\n processName: ${launchParam.lastExitDetailInfo.processName}
      \\n uid: ${launchParam.lastExitDetailInfo.uid}
      \\n exitSubReason: ${launchParam.lastExitDetailInfo.exitSubReason}
      \\n exitMsg: ${launchParam.lastExitDetailInfo.exitMsg}
      \\n rss: ${launchParam.lastExitDetailInfo.rss}
      \\n pss: ${launchParam.lastExitDetailInfo.pss}
      \\n timestamp: ${launchParam.lastExitDetailInfo.timestamp}
      \\n processState: ${launchParam.lastExitDetailInfo.processState}.\`
      );
    }
  }
}

#### OnContinueResult

Enumerates the ability continuation results. You can use it in [onContinue()](../ohos-app-ability-uiability-ability-with-ui/document.md#oncontinue) of the UIAbility to complete different operations.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| AGREE | 0 | The ability continuation is accepted. |
| REJECT | 1 | The ability continuation is rejected. If the application is abnormal in [onContinue](../ohos-app-ability-uiability-ability-with-ui/document.md#oncontinue), which results in abnormal display during data restoration, this result is returned. |
| MISMATCH | 2 | The version does not match. The application on the initiator can obtain the version of the target application from [onContinue](../ohos-app-ability-uiability-ability-with-ui/document.md#oncontinue). If the ability continuation cannot be performed due to version mismatch, this result is returned. |

**Example**

import { UIAbility, AbilityConstant } from '@kit.AbilityKit';

export default class MyAbility extends UIAbility {
  onContinue(wantParam: Record<string, Object>) {
    return AbilityConstant.OnContinueResult.AGREE;
  }
}

#### MemoryLevel

Enumerates the memory levels of the entire device. You can use it in [onMemoryLevel()](../ohos-app-ability-ability-ability-base-class/document.md#abilityonmemorylevel) of the UIAbility to complete different operations.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| MEMORY\_LEVEL\_MODERATE | 0 | The available memory of the entire device is moderate. |
| MEMORY\_LEVEL\_LOW | 1 | The available memory of the entire device is low. |
| MEMORY\_LEVEL\_CRITICAL | 2 | The available memory of the entire device is critically low. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/aMS0tzvSRM6okLSJ8ardOQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062204Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=70FBAA99FB51028AFAA491F390FEEFD7D511899FC1F8AE88393098C8939AE89A)

The trigger conditions may differ across various devices. For example, on a standard device with 12 GB of memory:

-   When the available memory of the entire device drops to 1700 MB to 1800 MB, the **onMemoryLevel** callback with a value of **0** is triggered, indicating that the available memory is moderate.
-   When the available memory of the entire device drops to 1600 MB to 1700 MB, the **onMemoryLevel** callback with a value of **1** is triggered, indicating that the available memory is low.
-   When the available memory of the entire device drops below 1600 MB, the **onMemoryLevel** callback with a value of **2** is triggered, indicating that the available memory is critically low.

**Example**

import { UIAbility, AbilityConstant } from '@kit.AbilityKit';

export default class MyAbility extends UIAbility {
  onMemoryLevel(level: AbilityConstant.MemoryLevel) {
    if (level === AbilityConstant.MemoryLevel.MEMORY\_LEVEL\_CRITICAL) {
      console.info('The memory of device is critical, please release some memory.');
    }
  }
}

#### WindowMode12+

Enumerates the window modes in which a UIAbility can be displayed at startup. You can use it in [startAbility](../../dependent-elements-and-definitions/application/uiabilitycontext/document.md#startability-2).

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| WINDOW\_MODE\_FULLSCREEN | 1 | Full-screen mode. It takes effect only on 2-in-1 devices and tablets. |
| WINDOW\_MODE\_SPLIT\_PRIMARY | 100 | Primary screen (left screen in the case of horizontal orientation) in split-screen mode. It is valid only in intra-app redirection scenarios. It takes effect only on foldable devices and tablets. |
| WINDOW\_MODE\_SPLIT\_SECONDARY | 101 | Secondary screen (right screen in the case of horizontal orientation) in split-screen mode. It is valid only in intra-app redirection scenarios. It takes effect only on foldable devices and tablets. |

**Example**

import { UIAbility, StartOptions, Want, AbilityConstant } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let want: Want = {
  bundleName: 'com.example.myapplication',
  abilityName: 'EntryAbility'
};
let option: StartOptions = {
  windowMode: AbilityConstant.WindowMode.WINDOW\_MODE\_SPLIT\_PRIMARY
};

// Ensure that the context is obtained.
export default class MyAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    this.context.startAbility(want, option).then(() => {
      console.info('Succeed to start ability.');
    }).catch((error: BusinessError) => {
      console.error(\`Failed to start ability with error: ${JSON.stringify(error)}\`);
    });
  }
}

#### OnSaveResult

Enumerates the result types for the operation of saving application data. You can use it in [onSaveState()](../ohos-app-ability-uiability-ability-with-ui/document.md#onsavestate) of the UIAbility to complete [UIAbility backup and restore](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/ability-recover-guideline).

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| ALL\_AGREE | 0 | Always agreed to save the status. |
| CONTINUATION\_REJECT | 1 | Rejected to save the status in continuation. |
| CONTINUATION\_MISMATCH | 2 | Continuation mismatch. |
| RECOVERY\_AGREE | 3 | Agreed to restore the saved status. |
| RECOVERY\_REJECT | 4 | Rejected to restore the saved status. |
| ALL\_REJECT | 5 | Always rejected to save the status. |

**Example**

import { UIAbility, AbilityConstant } from '@kit.AbilityKit';

export default class MyAbility extends UIAbility {
  onSaveState(reason: AbilityConstant.StateType, wantParam: Record<string, Object>) {
    return AbilityConstant.OnSaveResult.ALL\_AGREE;
  }
}

#### StateType

Enumerates the scenarios for saving application data. You can use it in [onSaveState()](../ohos-app-ability-uiability-ability-with-ui/document.md#onsavestate) of the UIAbility to complete [UIAbility backup and restore](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/ability-recover-guideline).

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| CONTINUATION | 0 | Application migration scenario. |
| APP\_RECOVERY | 1 | Application recovery scenario. |

**Example**

import { UIAbility, AbilityConstant } from '@kit.AbilityKit';

export default class MyAbility extends UIAbility {
  onSaveState(reason: AbilityConstant.StateType, wantParam: Record<string, Object>) {
    if (reason === AbilityConstant.StateType.CONTINUATION) {
      console.info('Save the ability data when the ability continuation.');
    }
    return AbilityConstant.OnSaveResult.ALL\_AGREE;
  }
}

#### ContinueState10+

Enumerates the mission continuation states of the application. It is used in the [setMissionContinueState](../../dependent-elements-and-definitions/application/uiabilitycontext/document.md#setmissioncontinuestate10) API of [UIAbilityContext](../../dependent-elements-and-definitions/application/uiabilitycontext/document.md).

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| ACTIVE | 0 | Mission continuation is activated for the current application. |
| INACTIVE | 1 | Mission continuation is not activated for the current application. |

**Example**

import { UIAbility, Want, AbilityConstant } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class MyAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    this.context.setMissionContinueState(AbilityConstant.ContinueState.INACTIVE, (result: BusinessError) => {
      console.info(\`setMissionContinueState: ${JSON.stringify(result)}\`);
    });
  }
}

#### CollaborateResult18+

Enumerates the collaboration request results. You can use it in multi-device collaboration scenarios to specify whether the target application accepts the collaboration request from the caller application. You can use it in [onCollaborate()](../ohos-app-ability-uiability-ability-with-ui/document.md#oncollaborate18) of the UIAbility.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| ACCEPT | 0 | Accepts the collaboration request. |
| REJECT | 1 | Rejects the collaboration request. |

**Example**

import { UIAbility, AbilityConstant } from '@kit.AbilityKit';

export default class MyAbility extends UIAbility {
  onCollaborate(wantParam: Record<string, Object>) {
    return AbilityConstant.CollaborateResult.ACCEPT;
  }
}

#### PrepareTermination15+

Enumerates the actions triggered when an application is closed by the user. You can use it in [onPrepareTermination](../ohos-app-ability-abilitystage-abilitystage-component-manager/document.md#onpreparetermination15) or [onPrepareTerminationAsync](../ohos-app-ability-abilitystage-abilitystage-component-manager/document.md#onprepareterminationasync15) of [AbilityStage](../ohos-app-ability-abilitystage-abilitystage-component-manager/document.md).

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| TERMINATE\_IMMEDIATELY | 0 | Executes the termination action immediately. This is the default behavior. |
| CANCEL | 1 | Cancels the termination action. |

**Example**

import { AbilityConstant, AbilityStage } from '@kit.AbilityKit';

export default class MyAbilityStage extends AbilityStage {
  onPrepareTermination(): AbilityConstant.PrepareTermination {
    console.info('MyAbilityStage.onPrepareTermination is called');
    return AbilityConstant.PrepareTermination.CANCEL;
  }
}
