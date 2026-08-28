# ApplicationStateObserver

The module defines an observer to listen for application state changes. It can be used as an input parameter in [on('applicationState')](../../../both-models-recommended/ohos-app-ability-appmanager-application-management/document.md#appmanageronapplicationstate14) to listen for lifecycle changes of the application.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/01/v3/kCHUo3MkRtSGRumpYa4Vsg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062209Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=956B5FD2C929B601378F3401711C8D4739C102A3511242C77AD51DC920818ED0)

The initial APIs of this module are supported since API version 14. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { appManager } from '@kit.AbilityKit';

#### ApplicationStateObserver.onForegroundApplicationChanged

onForegroundApplicationChanged(appStateData: AppStateData): void

Called when the foreground or background state of an application changes.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| appStateData | [AppStateData](../appstatedata/document.md) | Yes | Application state data. |

#### ApplicationStateObserver.onAbilityStateChanged

onAbilityStateChanged(abilityStateData: AbilityStateData): void

Called when the ability state changes.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| abilityStateData | [AbilityStateData](../abilitystatedata/document.md) | Yes | Ability state data. |

#### ApplicationStateObserver.onProcessCreated

onProcessCreated(processData: ProcessData): void

Called when a process is created.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| processData | [ProcessData](../processdata/document.md) | Yes | Process data. |

#### ApplicationStateObserver.onProcessDied

onProcessDied(processData: ProcessData): void

Called when a process is destroyed.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| processData | [ProcessData](../processdata/document.md) | Yes | Process data. |

#### ApplicationStateObserver.onProcessStateChanged

onProcessStateChanged(processData: ProcessData): void

Called when the process state is changed.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| processData | [ProcessData](../processdata/document.md) | Yes | Process data. |

#### ApplicationStateObserver.onAppStarted

onAppStarted(appStateData: AppStateData): void

Called when the first process of the application is created.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| appStateData | [AppStateData](../appstatedata/document.md) | Yes | Application state data. |

#### ApplicationStateObserver.onAppStopped

onAppStopped(appStateData: AppStateData): void

Called when the last process of the application is destroyed.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| appStateData | [AppStateData](../appstatedata/document.md) | Yes | Application state data. |

#### ProcessData

type ProcessData = \_ProcessData.default

Defines the process data.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

| Type | Description |
| :-- | :-- |
| [\_ProcessData.default](../processdata/document.md) | Process data. |

**Example**

import { appManager } from '@kit.AbilityKit';

let applicationStateObserver: appManager.ApplicationStateObserver = {
  onForegroundApplicationChanged(appStateData) {
    console.info(\`onForegroundApplicationChanged, appStateData: ${JSON.stringify(appStateData)}.\`);
  },
  onAbilityStateChanged(abilityStateData) {
    console.info(\`onAbilityStateChanged, abilityStateData: ${JSON.stringify(abilityStateData)}.\`);
  },
  onProcessCreated(processData) {
    console.info(\`onProcessCreated, processData: ${JSON.stringify(processData)}.\`);
  },
  onProcessDied(processData) {
    console.info(\`onProcessDied, processData: ${JSON.stringify(processData)}.\`);
  },
  onProcessStateChanged(processData) {
    console.info(\`onProcessStateChanged, processData: ${JSON.stringify(processData)}.\`);
  },
  onAppStarted(appStateData) {
    console.info(\`onAppStarted, appStateData: ${JSON.stringify(appStateData)}.\`);
  },
  onAppStopped(appStateData) {
    console.info(\`onAppStopped, appStateData: ${JSON.stringify(appStateData)}.\`);
  }
};
let observerCode = appManager.on('applicationState', applicationStateObserver);
