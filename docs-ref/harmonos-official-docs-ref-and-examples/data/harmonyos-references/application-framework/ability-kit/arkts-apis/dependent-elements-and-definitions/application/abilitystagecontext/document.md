# AbilityStageContext

The AbilityStageContext module implements the context of an ability stage. It inherits from [Context](../context-context-base-class-of-the-stage-model/document.md).

This module provides APIs for accessing a specific ability stage. You can use the APIs to obtain the ModuleInfo object and environment configuration of an ability stage.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/_s_GTYUCQ_GIDyZaqPVN7Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062209Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=66A7D7F3C67E2B144CE1A6759F56A1F9A37A51B8F1808C9514434D7044759ADA)

The initial APIs of this module are supported since API version 9. Newly added APIs will be marked with a superscript to indicate their earliest API version.

The APIs of this module can be used only in the stage model.

#### Modules to Import

import { common } from '@kit.AbilityKit';

#### Properties

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| currentHapModuleInfo | [HapModuleInfo](../../bundlemanager/hapmoduleinfo/document.md) | No | No | ModuleInfo object corresponding to the ability stage. |
| config | [Configuration](../../../both-models-recommended/ohos-app-ability-configuration-environment-variables/document.md) | No | No | Environment variables. |

**Example**

import { AbilityStage } from '@kit.AbilityKit';

class MyAbilityStage extends AbilityStage {
  onCreate() {
    let abilityStageContext = this.context;
    // Obtain the current module name.
    let name = abilityStageContext.currentHapModuleInfo.name;
    // Obtain the current language.
    let language = abilityStageContext.config.language;
  }
}
