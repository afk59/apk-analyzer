# @ohos.app.appstartup.StartupConfig (AppStartup Configuration)

The module defines the configuration of [AppStartup](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-startup).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/47R8U8UKSdmHP53JQFm5vA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062206Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0063D647A17E6B579450B1BED8AC7DC8DAACF90E6E8390B26B15E951C398020C)

The initial APIs of this module are supported since API version 12. Newly added APIs will be marked with a superscript to indicate their earliest API version.

The APIs of this module can be used only in the stage model.

#### Modules to Import

import { StartupConfig } from '@kit.AbilityKit';

#### StartupConfig

Describes the timeout duration and listener of startup tasks in AppStartup. For details, see [Setting Startup Parameters](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-startup#setting-startup-parameters).

**System capability**: SystemCapability.Ability.AppStartup

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| timeoutMs | number | No | Yes | Timeout for executing all startup tasks, measured in ms. The default value is 10000 ms. |
| startupListener | [StartupListener](../ohos-app-appstartup-startuplistener-appstartup-task-listener/document.md) | No | Yes | AppStartup listener, which is called when all the startup tasks are complete. |

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
