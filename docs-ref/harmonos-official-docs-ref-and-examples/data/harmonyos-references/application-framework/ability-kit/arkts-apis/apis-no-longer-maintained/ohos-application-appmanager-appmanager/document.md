# @ohos.application.appManager (appManager)

The appManager module provides APIs for application management. For example, you can query whether the system is undergoing a stability test, determine whether the device is RAM-constrained, obtain the maximum memory available to the current application, and retrieve information about running processes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/bVkRWss0R2GWIPPHd133pQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062211Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AE943FE3C97CBEE183AD53E5BAF2AA883432A994CA88C51FA25FE7D19720F98F)

The APIs of this module are supported since API version 8 and deprecated since API version 9. You are advised to use [@ohos.app.ability.appManager](../../both-models-recommended/ohos-app-ability-appmanager-application-management/document.md) instead. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import appManager from '@ohos.application.appManager';

#### appManager.isRunningInStabilityTest

isRunningInStabilityTest(callback: AsyncCallback<boolean>): void

Checks whether the system is undergoing a stability test. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/Lsr1SW6pSbqHTuo9y8PpUg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062211Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4EB5CD392F9058E522E89E1F0CCCFE140B1305051808C836A79E4F9CA6838A54)

A stability test scenario refers to a specific testing environment designed to verify application reliability under complex, extreme, or long-term operating conditions.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<boolean> | Yes | Callback used to return the API call result and the result indicating whether the system is undergoing a stability test. You can perform error handling or custom processing in this callback. **true** if the system is undergoing a stability test, **false** otherwise. |

**Example**

import appManager from '@ohos.application.appManager';

appManager.isRunningInStabilityTest((error, flag) => {
  if (error && error.code !== 0) {
    console.error(\`isRunningInStabilityTest fail, error: ${JSON.stringify(error)}\`);
  } else {
    console.info(\`isRunningInStabilityTest success, the result is: ${JSON.stringify(flag)}\`);
  }
});

#### appManager.isRunningInStabilityTest

isRunningInStabilityTest(): Promise<boolean>

Checks whether the system is undergoing a stability test. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/RsdFTHRhRu60HjhBPqO5mg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062211Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=15E150BEF5919E191C200A19386A04CF6928F5895482D1A3F4E9178EACFFDBFD)

A stability test scenario refers to a specific testing environment designed to verify application reliability under complex, extreme, or long-term operating conditions.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return the API call result and the result indicating whether the system is undergoing a stability test. You can perform error handling or custom processing in this callback. **true** if the system is undergoing a stability test, **false** otherwise. |

**Example**

import appManager from '@ohos.application.appManager';
import { BusinessError } from '@ohos.base';

appManager.isRunningInStabilityTest().then((flag) => {
  console.info(\`The result of isRunningInStabilityTest is: ${JSON.stringify(flag)}\`);
}).catch((error: BusinessError) => {
  console.error(\`error: ${JSON.stringify(error)}\`);
});

#### appManager.isRamConstrainedDevice7+

isRamConstrainedDevice(): Promise<boolean>

Checks whether the current device is a RAM-constrained device (a device with severely limited memory resources). This API uses a promise to return the result.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return the API call result and the result indicating whether the device is RAM-constrained. You can perform error handling or custom processing in this callback. **true** if the device is RAM-constrained, **false** otherwise. |

**Example**

import appManager from '@ohos.application.appManager';
import { BusinessError } from '@ohos.base';

appManager.isRamConstrainedDevice().then((data) => {
  console.info(\`The result of isRamConstrainedDevice is: ${JSON.stringify(data)}\`);
}).catch((error: BusinessError) => {
  console.error(\`error: ${JSON.stringify(error)}\`);
});

#### appManager.isRamConstrainedDevice7+

isRamConstrainedDevice(callback: AsyncCallback<boolean>): void

Checks whether the current device is a RAM-constrained device (a device with severely limited memory resources). This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<boolean> | Yes | Callback used to return the API call result and the result indicating whether the device is RAM-constrained. You can perform error handling or custom processing in this callback. **true** if the device is RAM-constrained, **false** otherwise. |

**Example**

import appManager from '@ohos.application.appManager';

appManager.isRamConstrainedDevice((error, data) => {
  if (error && error.code !== 0) {
    console.error(\`isRamConstrainedDevice fail, error: ${JSON.stringify(error)}\`);
  } else {
    console.info(\`The result of isRamConstrainedDevice is: ${JSON.stringify(data)}\`);
  }
});

#### appManager.getAppMemorySize7+

getAppMemorySize(): Promise<number>

Obtains the maximum memory (RAM allocation) available to the current application. This API uses a promise to return the result.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the maximum memory (RAM allocation) size, in MB. You can perform error processing or other custom processing based on the size. |

**Example**

import appManager from '@ohos.application.appManager';
import { BusinessError } from '@ohos.base';

appManager.getAppMemorySize().then((data) => {
  console.info(\`The size of app memory is: ${JSON.stringify(data)}\`);
}).catch((error: BusinessError) => {
  console.error(\`error: ${JSON.stringify(error)}\`);
});

#### appManager.getAppMemorySize7+

getAppMemorySize(callback: AsyncCallback<number>): void

Obtains the maximum memory (RAM allocation) available to the current application. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<number> | Yes | Callback used to return the maximum memory (RAM allocation) size, in MB. You can perform error processing or other custom processing based on the size. |

**Example**

import appManager from '@ohos.application.appManager';

appManager.getAppMemorySize((error, data) => {
  if (error && error.code !== 0) {
    console.error(\`getAppMemorySize fail, error: ${JSON.stringify(error)}\`);
  } else {
    console.info(\`The size of app memory is: ${JSON.stringify(data)}\`);
  }
});

#### appManager.getProcessRunningInfos(deprecated)

getProcessRunningInfos(): Promise<Array<ProcessRunningInfo>>

Obtains information about the running processes. This API uses a promise to return the result.

This API is deprecated since API version 9. You are advised to use [appManager.getRunningProcessInformation](../../both-models-recommended/ohos-app-ability-appmanager-application-management/document.md#appmanagergetrunningprocessinformation) instead.

**Required permissions**: ohos.permission.GET\_RUNNING\_INFO (available only for system applications)

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<[ProcessRunningInfo](../../dependent-elements-and-definitions/application/processrunninginfo/document.md)\>> | Promise used to return the information about the running processes. |

**Example**

import appManager from '@ohos.application.appManager';
import { BusinessError } from '@ohos.base';

appManager.getProcessRunningInfos().then((data) => {
  console.info(\`The process running infos is: ${JSON.stringify(data)}\`);
}).catch((error: BusinessError) => {
  console.error(\`error: ${JSON.stringify(error)}\`);
});

#### appManager.getProcessRunningInfos(deprecated)

getProcessRunningInfos(callback: AsyncCallback<Array<ProcessRunningInfo>>): void

Obtains information about the running processes. This API uses an asynchronous callback to return the result.

This API is deprecated since API version 9. You are advised to use [appManager.getRunningProcessInformation](../../both-models-recommended/ohos-app-ability-appmanager-application-management/document.md#appmanagergetrunningprocessinformation) instead.

**Required permissions**: ohos.permission.GET\_RUNNING\_INFO (available only for system applications)

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<Array<[ProcessRunningInfo](../../dependent-elements-and-definitions/application/processrunninginfo/document.md)\>> | Yes | Callback used to return the information about the running processes. |

**Example**

import appManager from '@ohos.application.appManager';

appManager.getProcessRunningInfos((error, data) => {
  if (error && error.code !== 0) {
    console.error(\`getProcessRunningInfos fail, error: ${JSON.stringify(error)}\`);
  } else {
    console.info(\`getProcessRunningInfos success, data: ${JSON.stringify(data)}\`);
  }
});
