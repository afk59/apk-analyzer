# BaseContext

BaseContext is an abstract class that specifies whether a child class Context is used for the stage model or FA model. It is the parent class for all types of Context.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/ut-KpdwQTW-sElWMcQZZUg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062209Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BBAD5FAD47690D2679259AB9679B3D5FED67E8AB4F6157EB5071FDFE4436DB7A)

The initial APIs of this module are supported since API version 8. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { common } from '@kit.AbilityKit';

#### Attributes

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| stageMode | boolean | No | No | 
Whether the child class Context is used for the stage model.

**true**: [Stage model](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/ability-terminology#stage-model).

**false**: [FA model](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/ability-terminology#fa-model).

 |

**Example**

Take the stage model as an example. You can access the **stageMode** field through UIAbilityContext.

import { UIAbility, AbilityConstant, Want } from '@kit.AbilityKit';

class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    // EntryAbility onCreate, isStageMode: true
    console.info(\`EntryAbility onCreate, isStageMode: ${this.context.stageMode}\`);
  }
}
