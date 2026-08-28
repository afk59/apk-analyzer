# ProcessData

The module defines process data. If a lifecycle change listener is registered by calling [appManager.on('applicationState')](../../../both-models-recommended/ohos-app-ability-appmanager-application-management/document.md#appmanageronapplicationstate14), the [onProcessCreated](../applicationstateobserver/document.md#applicationstateobserveronprocesscreated) callback in [ApplicationStateObserver](../applicationstateobserver/document.md) is invoked when the lifecycle of an application or ability changes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0a/v3/cS750Bl_QrOFjSdyLXOTGw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062210Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A6B8BB9358C8DA9F3E11F747BBE1D92C0C7EDACCCD2E85DBF9DDDAD81FD42C00)

The initial APIs of this module are supported since API version 14. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { appManager } from '@kit.AbilityKit';

#### Properties

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| pid | number | No | No | Process ID. |
| bundleName | string | No | No | Bundle name of the application. |
| uid | number | No | No | UID of the application. |
| isContinuousTask | boolean | No | No | Whether the task is a continuous task. **true** if yes, **false** otherwise. |
| isKeepAlive | boolean | No | No | Whether the process is a resident task. **true** if yes, **false** otherwise. |
| state | number | No | No | 
Application state. The options are as follows:

**0**: The application process is being initialized.

**1**: The application process has been initialized and is ready.

**2**: The application is running in the foreground.

**4**: The application is running in the background.

**5**: The application process is terminated.

 |

**Example**

import { appManager } from '@kit.AbilityKit';

let observerCode = appManager.on('applicationState', {
  onForegroundApplicationChanged(appStateData: appManager.AppStateData) {
    console.info(\`onForegroundApplicationChanged, appStateData: ${JSON.stringify(appStateData)}.\`);
  },
  onAbilityStateChanged(abilityStateData: appManager.AbilityStateData) {
    console.info(\`onAbilityStateChanged, abilityStateData: ${JSON.stringify(abilityStateData)}.\`);
  },
  onProcessCreated(processData: appManager.ProcessData) {
    console.info(\`onProcessCreated, processData: ${JSON.stringify(processData)}.\`);
  },
  onProcessDied(processData: appManager.ProcessData) {
    console.info(\`onProcessDied, processData: ${JSON.stringify(processData)}.\`);
  },
  onProcessStateChanged(processData: appManager.ProcessData) {
    console.info(\`onProcessStateChanged, processData.pid : ${JSON.stringify(processData.pid)}.\`);
    console.info(\`onProcessStateChanged, processData.bundleName : ${JSON.stringify(processData.bundleName)}.\`);
    console.info(\`onProcessStateChanged, processData.uid : ${JSON.stringify(processData.uid)}.\`);
    console.info(\`onProcessStateChanged, processData.isContinuousTask : ${JSON.stringify(processData.isContinuousTask)}.\`);
    console.info(\`onProcessStateChanged, processData.isKeepAlive : ${JSON.stringify(processData.isKeepAlive)}.\`);
  },
  onAppStarted(appStateData: appManager.AppStateData) {
    console.info(\`onAppStarted, appStateData: ${JSON.stringify(appStateData)}.\`);
  },
  onAppStopped(appStateData: appManager.AppStateData) {
    console.info(\`onAppStopped, appStateData: ${JSON.stringify(appStateData)}.\`);
  }
});
