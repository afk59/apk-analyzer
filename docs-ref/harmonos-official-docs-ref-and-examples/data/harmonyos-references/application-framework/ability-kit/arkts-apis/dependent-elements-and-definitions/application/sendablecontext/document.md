# SendableContext

SendableContext complies with the [Sendable protocol](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-sendable#sendable-protocol) and inherits from [lang.ISendable](../../../../../arkts/arkts-apis/arkts-lang-arkts-base-capability/document.md#langisendable).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/zaio8T8HR0STlc1QXek8OA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062210Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=08582684F8E1E593633603F571FA29E92512E54155C3AE1DA0925752002C28A0)

-   The initial APIs of this module are supported since API version 12. Newly added APIs will be marked with a superscript to indicate their earliest API version.
-   The APIs of this module can be used only in the stage model.

#### Modules to Import

import { sendableContextManager } from '@kit.AbilityKit';

#### SendableContext

SendableContext, which complies with the [Sendable protocol](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-sendable#sendable-protocol), can be converted to a Context object to implement data transmission between concurrent ArkTS instances (including the main thread and the worker thread of TaskPool or Worker).

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Atomic service API**: This API can be used in atomic services since API version 12.
