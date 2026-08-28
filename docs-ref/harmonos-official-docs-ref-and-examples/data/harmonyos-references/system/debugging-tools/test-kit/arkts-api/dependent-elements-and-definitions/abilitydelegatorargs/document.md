# AbilityDelegatorArgs

The **AbilityDelegatorArgs** module provides APIs to obtain an **AbilityDelegatorArgs** object during the execution of test cases.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/sj_enO-qTLC58Qi6oA0JNQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062416Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C79E134393C6658E4B6BC75945EF80E62942AC33ECFC69B4EEDC8EB6F4FCAF31)

The initial APIs of this module are supported since API version 8. Newly added APIs will be marked with a superscript to indicate their earliest API version.

The APIs of this module can be used only in [unittest](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/unittest-guidelines).

#### Modules to Import

import { abilityDelegatorRegistry } from '@kit.TestKit';

#### Usage

An **AbilityDelegatorArgs** object is obtained by calling [getArguments](../../ohos-app-ability-abilitydelegatorregistry-abilitydelegatorregistry/document.md#abilitydelegatorregistrygetarguments) in **AbilityDelegatorRegistry**.

#### AbilityDelegatorArgs

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| bundleName | string | No | No | Bundle name of the application to test. |
| parameters | Record<string, string> | No | No | Parameters of the unit test that is started currently. |
| testCaseNames | string | No | No | Test case name. |
| testRunnerClassName | string | No | No | Names of the test case executors. |

**Example**

import { abilityDelegatorRegistry } from '@kit.TestKit';

let args: abilityDelegatorRegistry.AbilityDelegatorArgs = abilityDelegatorRegistry.getArguments();
