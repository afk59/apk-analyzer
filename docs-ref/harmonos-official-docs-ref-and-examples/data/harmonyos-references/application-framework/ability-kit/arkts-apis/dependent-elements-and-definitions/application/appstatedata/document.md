# AppStateData

The module defines the application state information. Once an application state change listener is registered using [on](../../../both-models-recommended/ohos-app-ability-appmanager-application-management/document.md#appmanageronapplicationstate14), the system triggers the [onForegroundApplicationChanged](../applicationstateobserver/document.md#applicationstateobserveronforegroundapplicationchanged) callback of [ApplicationStateObserver](../applicationstateobserver/document.md) to deliver notifications whenever the state of an application, process, or ability changes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/zQ5P7eUuQ1y2vud71sEalg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062209Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AF9659C29AC16265873CD3AF4B64FEE4A2CFDA0397747BB967BEAC370B7F7A5D)

The initial APIs of this module are supported since API version 14. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { appManager } from '@kit.AbilityKit';

#### Properties

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| bundleName | string | No | No | Bundle name. |
| uid | number | No | No | UID of the application. |
| state | number | No | No | 
Application state.

**0**: The application is being initialized.

**1**: The application has been initialized and is ready.

**2**: The application is running in the foreground.

**3**: The application is having the focus. (This state is reserved.)

**4**: The application is running in the background.

**5**: The application has exited.

 |
| isSplitScreenMode | boolean | No | No | 

Whether the application is in split-screen mode.

**true**: The application is in split-screen mode.

**false**: The application is not in split-screen mode.

 |
| isFloatingWindowMode | boolean | No | No | 

Whether the application is in floating window mode.

**true**: The application is in floating window mode.

**false**: The application is not in floating window mode.

 |

**Example**

import { appManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let applicationStateObserver: appManager.ApplicationStateObserver = {
  onForegroundApplicationChanged(appStateData: appManager.AppStateData) {
    console.info(\`\[appManager\] onForegroundApplicationChanged: ${JSON.stringify(appStateData)}\`);
    console.info(\`appStateData.bundleName: ${appStateData.bundleName}\`);
    console.info(\`appStateData.uid: ${appStateData.uid}\`);
    console.info(\`appStateData.state: ${appStateData.state}\`);
    console.info(\`appStateData.isSplitScreenMode: ${appStateData.isSplitScreenMode}\`);
    console.info(\`appStateData.isFloatingWindowMode: ${appStateData.isFloatingWindowMode}\`);
  },
  onAbilityStateChanged(abilityStateData: appManager.AbilityStateData) {
    console.info(\`\[appManager\] onAbilityStateChanged: ${JSON.stringify(abilityStateData)}\`);
  },
  onProcessCreated(processData: appManager.ProcessData) {
    console.info(\`\[appManager\] onProcessCreated: ${JSON.stringify(processData)}\`);
  },
  onProcessDied(processData: appManager.ProcessData) {
    console.info(\`\[appManager\] onProcessDied: ${JSON.stringify(processData)}\`);
  },
  onProcessStateChanged(processData: appManager.ProcessData) {
    console.info(\`\[appManager\] onProcessStateChanged: ${JSON.stringify(processData)}\`);
  },
  onAppStarted(appStateData: appManager.AppStateData) {
    console.info(\`\[appManager\] onAppStarted: ${JSON.stringify(appStateData)}\`);
  },
  onAppStopped(appStateData: appManager.AppStateData) {
    console.info(\`\[appManager\] onAppStopped: ${JSON.stringify(appStateData)}\`);
  }
};

try {
  const observerId = appManager.on('applicationState', applicationStateObserver);
  console.info(\`\[appManager\] observerCode: ${observerId}\`);
} catch (paramError) {
  let code = (paramError as BusinessError).code;
  let message = (paramError as BusinessError).message;
  console.error(\`\[appManager\] error code: ${code}, error msg: ${message}\`);
}
