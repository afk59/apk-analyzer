# AbilityResult

The module defines the result code and data returned to the caller when a started UIAbility is terminated.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/sRKuDG51QjyBi66oKhP-kg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062209Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1AA03D784BCDB13B2BA7BD523DBB859627581E8C4329D689E081EB7FFCB21690)

The initial APIs of this module are supported since API version 7. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

[Stage model](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/ability-terminology#stage-model):

import { common } from '@kit.AbilityKit';

[FA model](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/ability-terminology#fa-model):

import ability from '@ohos.ability.ability';

#### How to Use

In the stage model, you can use [startAbilityForResult](../../application/uiabilitycontext/document.md#startabilityforresult) to obtain the AbilityResult object returned when the started UIAbility is terminated by calling [terminateSelfWithResult](../../application/uiabilitycontext/document.md#terminateselfwithresult).

In the FA model, you can use [startAbilityForResult](../../../fa-model/ohos-ability-featureability-featureability-module/document.md#featureabilitystartabilityforresult7) to obtain the AbilityResult object returned after the started UIAbility is terminated by calling [terminateSelfWithResult](../../../fa-model/ohos-ability-featureability-featureability-module/document.md#featureabilityterminateselfwithresult7).

#### Attributes

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.AbilityBase

| Name | Type | Read-only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| resultCode | number | No | No | 
Result code returned by the target party to the caller after the UIAbility of the target party is started and then terminated.

\- In normal cases, the result code sent by the target party is returned.

\- In abnormal cases, the value **\-1** is returned.

 |
| want | [Want](../../../both-models-recommended/ohos-app-ability-want-want/document.md) | No | Yes | Data returned after the started UIAbility is terminated. |
