# @ohos.app.ability.EmbeddableUIAbility (Embeddable UIAbility)

EmbeddableUIAbility is an embeddable UIAbility component provided for atomic services. It inherits from [UIAbility](../ohos-app-ability-uiability-ability-with-ui/document.md).

You can implement EmbeddableUIAbility to enable atomic services to be launched by other applications either as a standalone window or embedded within the host application's UI.

For details about the inheritance relationship of each ability, see [Inheritance Relationship](../ohos-app-ability-ability-ability-base-class/document.md#ability-inheritance-relationship).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/LdIezF_LRgec5XvHEc_lQA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062205Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B2C45DF3423F0560AF4DE2A1D86B7C7A763DB0C70435DE0382BE56D31EACAF5D)

The initial APIs of this module are supported since API version 12. Newly added APIs will be marked with a superscript to indicate their earliest API version.

The APIs of this module can be used only in the stage model.

#### Modules to Import

import { EmbeddableUIAbility } from '@kit.AbilityKit';

#### EmbeddableUIAbility

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Atomic service API**: This API can be used in atomic services since API version 12.

| Name | Type | Read-only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| context | [EmbeddableUIAbilityContext](../../dependent-elements-and-definitions/application/embeddableuiabilitycontext/document.md) | No | No | Context of the EmbeddableUIAbility. |
