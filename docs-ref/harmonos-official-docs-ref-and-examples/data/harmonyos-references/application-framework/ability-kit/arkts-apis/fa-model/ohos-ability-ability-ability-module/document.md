# @ohos.ability.ability (Ability Module)

The module provides all level-2 module APIs for developers to export.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/rKH1wzszSEqL4SUZ-nxAtQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062207Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C900A8D3CC50A2D6751EDA675B68931917E1AA5E84AA7D667CD0FD9C1C326979)

The initial APIs of this module are supported since API version 9. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { ability } from '@kit.AbilityKit';

#### DataAbilityHelper

type DataAbilityHelper = \_DataAbilityHelper

Defines the level-2 module DataAbilityHelper.

**System capability**: SystemCapability.Ability.AbilityRuntime.FAModel

**Model restriction**: This API can be used only in the FA model.

| Type | Description |
| :-- | :-- |
| [\_DataAbilityHelper](../../dependent-elements-and-definitions/ability/dataabilityhelper/document.md) | Level-2 module DataAbilityHelper. |

#### PacMap

type PacMap = \_PacMap

Defines the level-2 module PacMap.

**System capability**: SystemCapability.Ability.AbilityRuntime.FAModel

| Type | Description |
| :-- | :-- |
| [\_PacMap](../../dependent-elements-and-definitions/ability/dataabilityhelper/document.md#pacmap) | Level-2 module DataAbilityHelper. |

#### DataAbilityOperation

type DataAbilityOperation = \_DataAbilityOperation

Defines the level-2 module DataAbilityOperation.

**System capability**: SystemCapability.Ability.AbilityRuntime.FAModel

**Model restriction**: This API can be used only in the FA model.

| Type | Description |
| :-- | :-- |
| [\_DataAbilityOperation](../ability/dataabilityoperation/document.md) | Level-2 module DataAbilityOperation. |

#### DataAbilityResult

type DataAbilityResult = \_DataAbilityResult

Defines the level-2 module DataAbilityResult.

**System capability**: SystemCapability.Ability.AbilityRuntime.FAModel

**Model restriction**: This API can be used only in the FA model.

| Type | Description |
| :-- | :-- |
| [\_DataAbilityResult](../ability/dataabilityresult/document.md) | Level-2 module DataAbilityResult. |

#### AbilityResult

type AbilityResult = \_AbilityResult

Defines the level-2 module AbilityResult.

**System capability**: SystemCapability.Ability.AbilityBase

**Model restriction**: This API can be used only in the FA model.

| Type | Description |
| :-- | :-- |
| [\_AbilityResult](../../dependent-elements-and-definitions/ability/abilityresult/document.md) | Level-2 module AbilityResult. |

#### ConnectOptions

type ConnectOptions = \_ConnectOptions

Defines the level-2 module ConnectOptions.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Model restriction**: This API can be used only in the FA model.

| Type | Description |
| :-- | :-- |
| [\_ConnectOptions](../../dependent-elements-and-definitions/ability/connectoptions/document.md) | Level-2 module ConnectOptions. |

#### StartAbilityParameter

type StartAbilityParameter = \_StartAbilityParameter

Defines the level-2 module StartAbilityParameter.

**System capability**: SystemCapability.Ability.AbilityRuntime.FAModel

**Model restriction**: This API can be used only in the FA model.

| Type | Description |
| :-- | :-- |
| [\_StartAbilityParameter](../ability/startabilityparameter/document.md) | Level-2 module StartAbilityParameter. |

**Example**

import { ability } from '@kit.AbilityKit';

let dataAbilityHelper: ability.DataAbilityHelper;
let pacMap: ability.PacMap;
let dataAbilityOperation: ability.DataAbilityOperation;
let dataAbilityResult: ability.DataAbilityResult;
let abilityResult: ability.AbilityResult;
let connectOptions: ability.ConnectOptions;
let startAbilityParameter: ability.StartAbilityParameter;
