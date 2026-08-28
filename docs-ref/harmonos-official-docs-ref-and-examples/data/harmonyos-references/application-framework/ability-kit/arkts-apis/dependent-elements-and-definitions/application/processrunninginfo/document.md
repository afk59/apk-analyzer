# ProcessRunningInfo

The module defines the running information of a process. The information can be obtained through [getProcessRunningInfos](../../../apis-no-longer-maintained/ohos-application-appmanager-appmanager/document.md#appmanagergetprocessrunninginfosdeprecated) of appManager.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/psL6I7VaTre-HMAEkZG3pw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062209Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2ED5C60DC469442FF6BC78DB0789C93099C06CC7ABFFF2A02342AA4E3342B320)

-   The APIs provided by this module are deprecated since API version 9. You are advised to use [ProcessInformation9+](../processinformation/document.md) instead.
-   The initial APIs of this module are supported since API version 8.

#### Modules to Import

import appManager from '@ohos.application.appManager';

#### Attributes

**System capability**: SystemCapability.Ability.AbilityRuntime.Mission

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| pid | number | No | No | Process ID. |
| uid | number | No | No | UID of the application. |
| processName | string | No | No | Process name. |
| bundleNames | Array<string> | No | No | Names of all running bundles in the process. |

**Example**

import appManager from '@ohos.application.appManager';
import { BusinessError } from '@ohos.base';

appManager.getProcessRunningInfos().then((data) => {
    console.info(\`success: ${JSON.stringify(data)}\`);
}).catch((error: BusinessError) => {
    console.error(\`failed: ${JSON.stringify(error)}\`);
});
