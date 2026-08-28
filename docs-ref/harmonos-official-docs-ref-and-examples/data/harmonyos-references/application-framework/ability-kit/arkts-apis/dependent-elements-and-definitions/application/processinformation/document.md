# ProcessInformation

The module defines the process information. The information can be obtained through [getRunningProcessInformation](../../../both-models-recommended/ohos-app-ability-appmanager-application-management/document.md#appmanagergetrunningprocessinformation) of appManager.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/UdH_IIDXRLudZESsDQoFpw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062210Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=24903167162F41D2FFF3FA17AF3F1408264B991E752374B89D14AFA698EE0597)

The initial APIs of this module are supported since API version 9. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { appManager } from '@kit.AbilityKit';

#### Properties

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| pid | number | No | No | 
Process ID.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| uid | number | No | No | 

UID of the application.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| processName | string | No | No | 

Process name.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| bundleNames | Array<string> | No | No | 

Names of all running bundles in the process.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| state10+ | [appManager.ProcessState](../../../both-models-recommended/ohos-app-ability-appmanager-application-management/document.md#processstate10) | No | No | 

Running status of the process.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| bundleType12+ | [bundleManager.BundleType](../../../both-models-recommended/ohos-bundle-bundlemanager-bundle-management-module/document.md#bundletype) | No | No | 

Type of the bundle running in the process.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| appCloneIndex12+ | number | No | Yes | 

Index of an application clone.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |

**Example**

import { appManager } from '@kit.AbilityKit';

appManager.getRunningProcessInformation((error, data) => {
  if (error) {
    console.error(\`getRunningProcessInformation fail, error: ${JSON.stringify(error)}\`);
  } else {
    console.info(\`getRunningProcessInformation success, data: ${JSON.stringify(data)}\`);
  }
});
