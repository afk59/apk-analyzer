# @ohos.app.ability.autoStartupManager (Auto-Startup Management)

The autoStartupManager module provides APIs for an application to query whether it is configured to start automatically at boot time.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/afK2Tt7EQruT9Hyiwu7TDw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062206Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=275D35107EBDBED2918188A5A36D3D2C4EB4CD353CE8ECCAC2924EC2F12BFDCF)

The initial APIs of this module are supported since API version 21. Newly added APIs will be marked with a superscript to indicate their earliest API version.

The APIs of this module can be used only in the stage model.

#### Modules to Import

import { autoStartupManager } from '@kit.AbilityKit';

#### autoStartupManager.getAutoStartupStatusForSelf

getAutoStartupStatusForSelf(): Promise<boolean>

Checks whether the current application is enabled for automatic startup at boot time. This API uses a promise to return the result.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Device behavior differences**: This API can be properly called only on phones, PC/2-in-1 devices, tablets, and wearables. On other devices, it returns the error code 801.

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return the auto-startup status. **true** if enabled for automatic startup at boot time, **false** otherwise. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Ability Error Codes](../../../error-codes/ability-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported. |
| 16000050 | Internal error. Possible causes: 1. Connect to system service failed; 2.System service failed to communicate with dependency module. |

**Example**

import { autoStartupManager, UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onForeground() {
    try {
      autoStartupManager.getAutoStartupStatusForSelf().then((isAutoStartup: boolean) => {
        console.info(\`getAutoStartupStatusForSelf success, isAutoStartup: ${JSON.stringify(isAutoStartup)}.\`);
      }).catch((err: BusinessError) => {
        console.error(\`getAutoStartupStatusForSelf failed, err code: ${err.code}, err msg: ${err.message}.\`);
      });
    } catch (err) {
      let code = (err as BusinessError).code;
      let msg = (err as BusinessError).message;
      console.error(\`getAutoStartupStatusForSelf failed, err code: ${code}, err msg: ${msg}.\`);
    }
  }
}
