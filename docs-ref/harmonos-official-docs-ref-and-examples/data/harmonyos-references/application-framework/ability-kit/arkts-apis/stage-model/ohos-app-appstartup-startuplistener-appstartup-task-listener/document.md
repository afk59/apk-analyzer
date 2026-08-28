# @ohos.app.appstartup.StartupListener (AppStartup Task Listener)

The module defines the task listener used in [App Startup](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-startup).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/_LNXW5B7SbqK-g-00Onp9g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062206Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5A2127F666A160403F28F0C35E1AD7FE419D21E2B1AED34947F4F29A37D8CD97)

The initial APIs of this module are supported since API version 12. Newly added APIs will be marked with a superscript to indicate their earliest API version.

The APIs of this module can be used only in the stage model.

#### Modules to Import

import { StartupListener } from '@kit.AbilityKit';

#### StartupListener.onCompleted

onCompleted?(error: BusinessError<void>): void

Called when all startup tasks are complete.

**System capability**: SystemCapability.Ability.AppStartup

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| error | [BusinessError<void>](../../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#businesserror) | Yes | Error message. |

**Example**

import { StartupConfig, StartupConfigEntry, StartupListener } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

export default class MyStartupConfigEntry extends StartupConfigEntry {
  onConfig() {
    hilog.info(0x0000, 'testTag', \`onConfig\`);
    let onCompletedCallback = (error: BusinessError<void>) => {
      hilog.info(0x0000, 'testTag', \`onCompletedCallback\`);
      if (error) {
        hilog.error(0x0000, 'testTag', 'onCompletedCallback: %{public}d, message: %{public}s', error.code,
          error.message);
      } else {
        hilog.info(0x0000, 'testTag', \`onCompletedCallback: success.\`);
      }
    };
    let startupListener: StartupListener = {
      'onCompleted': onCompletedCallback
    };
    let config: StartupConfig = {
      'timeoutMs': 10000,
      'startupListener': startupListener
    };
    return config;
  }
}
