# ProcessInfo

The module defines process information. You can use [getProcessInfo](../context-context-base-class-of-the-fa-model/document.md#contextgetprocessinfo7) to obtain information about the processes running on the current ability.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/RPJFQ5TDRcK3VluGhGQUIA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062207Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D5467E143B834562BE25A81B20783B52998BA62B15E4DDD8A7CD176618D44DC1)

The initial APIs of this module are supported since API version 7. The APIs of this module can be used only in the FA model. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import featureAbility from '@ohos.ability.featureAbility';

#### Attributes

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| pid | number | No | No | Process ID. |
| processName | string | No | No | Process name. |

**Example**

import featureAbility from '@ohos.ability.featureAbility';

let context = featureAbility.getContext();
context.getProcessInfo((error, data) => {
    if (error && error.code !== 0) {
        console.error(\`getProcessInfo fail, error: ${JSON.stringify(error)}\`);
    } else {
        console.info(\`getProcessInfo success, data: ${JSON.stringify(data)}\`);
        let pid = data.pid;
        let processName = data.processName;
    }
});
