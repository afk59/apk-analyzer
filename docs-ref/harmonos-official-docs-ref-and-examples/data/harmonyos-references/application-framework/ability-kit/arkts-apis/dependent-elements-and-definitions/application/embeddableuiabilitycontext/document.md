# EmbeddableUIAbilityContext

EmbeddableUIAbilityContext provides the context environment for the [EmbeddableUIAbility](../../../stage-model/ohos-app-ability-embeddableuiability-embeddable-uiability/document.md). It inherits from [UIAbilityContext](../uiabilitycontext/document.md).

When an EmbeddableUIAbility component is instantiated, the system automatically creates the corresponding EmbeddableUIAbilityContext.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/wiQk7WSoSn6Wq45_Q7jq4A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062209Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2373AC740342E10F0511F0028D44F69351B4FB1D5AB5665C71046C7605D04E25)

-   The initial APIs of this module are supported since API version 12. Newly added APIs will be marked with a superscript to indicate their earliest API version.
-   The APIs of this module can be used only in the stage model.
-   The APIs of this module must be used in the main thread, but not in child threads such as Worker and TaskPool.

#### Modules to Import

import { common } from '@kit.AbilityKit';

#### EmbeddableUIAbilityContext

Through the EmbeddableUIAbilityContext, you can obtain the EmbeddableUIAbility-related configuration and APIs for operating EmbeddableUIAbility and ServiceExtensionAbility components. For example, you can use the APIs to start an EmbeddableUIAbility, terminate an EmbeddableUIAbility to which the EmbeddableUIAbilityContext belongs, and start, terminate, connect to, or disconnect from a ServiceExtensionAbility.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Atomic service API**: This API can be used in atomic services since API version 12.
