# @ohos.application.Configuration (Configuration)

The module defines environment change information. Configuration is an interface definition and is used only for field declaration.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/LG3MY-ZTQY2TptOJOtq6dA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062211Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FF902BA593FA54C1CDB5E6358EC8BC8D5C79B6B124FF8692733BEACACEA25539)

The initial APIs of this module are supported since API version 8. Newly added APIs will be marked with a superscript to indicate their earliest API version.

This module is deprecated since API version 9. You are advised to use [@ohos.app.ability.Configuration](../../both-models-recommended/ohos-app-ability-configuration-environment-variables/document.md) instead.

#### Modules to Import

import Configuration from '@ohos.application.Configuration';

#### Configuration

**System capability**: SystemCapability.Ability.AbilityBase

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| language8+ | string | No | Yes | Language of the application, for example, **zh**. |
| colorMode8+ | [ConfigurationConstant.ColorMode](../ohos-application-configurationconstant-configurationconstant/document.md#colormode) | No | Yes | Color mode, which can be **COLOR\_MODE\_LIGHT** or **COLOR\_MODE\_DARK**. The default value is **COLOR\_MODE\_LIGHT**. |

For details about the fields, see the **ohos.application.Configuration.d.ts** file.

**Example**

import UIAbility from '@ohos.app.ability.UIAbility';
import AbilityConstant from '@ohos.app.ability.AbilityConstant';
import EnvironmentCallback from '@ohos.app.ability.EnvironmentCallback';
import Want from '@ohos.app.ability.Want';
import Window from '@ohos.window';
import { BusinessError } from '@ohos.base';

export default class EntryAbility extends UIAbility {
onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
}

onDestroy() {
}

onWindowStageCreate(windowStage: Window.WindowStage) {
  let envCallback: EnvironmentCallback = {
    onConfigurationUpdated(config) {
      console.info(\`envCallback onConfigurationUpdated success: ${JSON.stringify(config)}\`);
      let language = config.language;
      let colorMode = config.colorMode;
    },
    onMemoryLevel(level) {
      console.info(\`onMemoryLevel level: ${JSON.stringify(level)}\`);
    }
  };

  let applicationContext = this.context.getApplicationContext();
  try {
    applicationContext.on('environment', envCallback);
  } catch (paramError) {
    console.error(\`error: ${(paramError as BusinessError).code}, ${(paramError as BusinessError).message}\`);
  }

  windowStage.loadContent('pages/index', (err, data) => {
    if (err.code) {
      console.error(\`failed to load the content, error: ${JSON.stringify(err)}\`);
      return;
    }
    console.info(\`Succeeded in loading the content, data: ${JSON.stringify(data)}\`);
  });
}
}
