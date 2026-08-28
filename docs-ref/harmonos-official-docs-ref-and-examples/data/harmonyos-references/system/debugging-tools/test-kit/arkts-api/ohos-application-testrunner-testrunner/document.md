# @ohos.application.testRunner (TestRunner)

The **TestRunner** module provides a test framework. You can use the APIs of this module to prepare the unit test environment and run test cases.

To implement your own unit test framework, extend this class and override its APIs.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/o6Jn4S9IQjSrAXmZXxLRCA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062416Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F664D17504409EDEB8AB6AD91CE8DABB5418A54C3D68322448E6F13F6117F767)

The initial APIs of this module are supported since API version 8. Newly added APIs will be marked with a superscript to indicate their earliest API version.

The APIs of this module can be used only in [unittest](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/unittest-guidelines).

#### Modules to Import

import { TestRunner } from '@kit.TestKit';

#### TestRunner.onPrepare

onPrepare(): void

Prepares the unit test environment to run test cases.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Atomic service API**: This API can be used in atomic services since API version 11.

**Example**

import { TestRunner } from '@kit.TestKit';

export default class UserTestRunner implements TestRunner {
  onPrepare() {
    console.info('Trigger onPrepare');
  }

  onRun() {
  }
}

#### TestRunner.onRun

onRun(): void

Runs test cases.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Atomic service API**: This API can be used in atomic services since API version 11.

**Example**

import { TestRunner } from '@kit.TestKit';

export default class UserTestRunner implements TestRunner {
  onPrepare() {
  }

  onRun() {
    console.info('Trigger onRun');
  }
}
