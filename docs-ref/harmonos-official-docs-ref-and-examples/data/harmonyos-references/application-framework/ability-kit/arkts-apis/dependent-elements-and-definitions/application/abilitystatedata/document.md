# AbilityStateData

The AbilityStateData module defines a struct for ability state information. Once a lifecycle change listener is registered using [on](../../../both-models-recommended/ohos-app-ability-appmanager-application-management/document.md#appmanageronapplicationstate14), you can obtain an instance of this struct from the input parameter of the **onAbilityStateChanged** callback of [ApplicationStateObserver](../applicationstateobserver/document.md).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/XysZjCkxRk2jECKif1oryg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062209Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=201461BA7DA6E0B158DC0629DF3131753E10D0967DDCE6F3CA6402670AE3E23C)

The initial APIs of this module are supported since API version 14. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { appManager } from '@kit.AbilityKit';

#### AbilityStateData

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| pid | number | No | No | Process ID. |
| bundleName | string | No | No | Bundle name. |
| abilityName | string | No | No | Ability name. |
| uid | number | No | No | UID of the application. |
| state | number | No | No | 
Ability state.

\- [Stage model](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/ability-terminology#stage-model): For the [UIAbility](../../../stage-model/ohos-app-ability-uiability-ability-with-ui/document.md), see [UIAbility States](#uiability-states). For the [ExtensionAbility](../../../stage-model/ohos-app-ability-extensionability-extensionability-base-class/document.md), see [ExtensionAbility States](#extensionability-states).

\- [FA model](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/ability-terminology#fa-model): For the ability, see [Ability States](#ability-states).

 |
| moduleName | string | No | No | Module name to which the ability belongs. |
| abilityType | number | No | No | [Ability type](#ability-types), which can be [UIAbility](../../../stage-model/ohos-app-ability-uiability-ability-with-ui/document.md) or [ExtensionAbility](../../../stage-model/ohos-app-ability-extensionability-extensionability-base-class/document.md). |
| isAtomicService | boolean | No | No | 

Whether the ability belongs to an atomic service.

**true**: The ability belongs to an atomic service.

**false**: The ability does not belong to an atomic service.

 |
| appCloneIndex | number | No | Yes | Index of an [application clone](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-clone). |

## UIAbility States

| Value | State | Description |
| :-- | :-- | :-- |
| 0 | ABILITY\_STATE\_CREATE | The UIAbility is being created. |
| 1 | ABILITY\_STATE\_READY | The UIAbility has been created. |
| 2 | ABILITY\_STATE\_FOREGROUND | The UIAbility is running in the foreground. |
| 3 | ABILITY\_STATE\_FOCUS | The UIAbility has gained focus. |
| 4 | ABILITY\_STATE\_BACKGROUND | The UIAbility is running in the background. |
| 5 | ABILITY\_STATE\_TERMINATED | The UIAbility is terminated. |

## ExtensionAbility States

| Value | State | Description |
| :-- | :-- | :-- |
| 0 | EXTENSION\_STATE\_CREATE | The ExtensionAbility is being created. |
| 1 | EXTENSION\_STATE\_READY | The ExtensionAbility has been created. |
| 2 | EXTENSION\_STATE\_CONNECTED | The ExtensionAbility is connected to the client. |
| 3 | EXTENSION\_STATE\_DISCONNECTED | The ExtensionAbility is disconnected from the client. |
| 4 | EXTENSION\_STATE\_TERMINATED | The ExtensionAbility is terminated. |

## Ability States

| Value | State | Description |
| :-- | :-- | :-- |
| 0 | ABILITY\_STATE\_CREATE | The ability is being created. |
| 1 | ABILITY\_STATE\_READY | The ability has been created. |
| 2 | ABILITY\_STATE\_FOREGROUND | The ability is running in the foreground. |
| 3 | ABILITY\_STATE\_FOCUS | The ability has gained focus. |
| 4 | ABILITY\_STATE\_BACKGROUND | The ability is running in the background. |
| 5 | ABILITY\_STATE\_TERMINATED | The ability is terminated. |
| 7 | ABILITY\_STATE\_CONNECTED | The background service is connected to the client. |
| 8 | ABILITY\_STATE\_DISCONNECTED | The background service is disconnected from the client. |

## Ability Types

| Value | State | Description |
| :-- | :-- | :-- |
| 0 | UNKNOWN | Unknown type. (System error.) |
| 1 | PAGE | Ability that provides the UI, that is, [UIAbility](../../../stage-model/ohos-app-ability-uiability-ability-with-ui/document.md). |
| 2 | SERVICE | Ability that provides the background service. (FA model.) |
| 3 | DATA | Ability that provides the data service. (FA model.) |
| 4 | FORM | Ability that provides the widget service. (FA model.) |
| 5 | EXTENSION | Ability that provides the extension service. (stage model.) |
