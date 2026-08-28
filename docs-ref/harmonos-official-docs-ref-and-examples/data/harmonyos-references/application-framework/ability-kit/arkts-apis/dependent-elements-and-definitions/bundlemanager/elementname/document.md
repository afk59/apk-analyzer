# ElementName

A structured identifier for an application component, containing fields such as **bundleName**, **moduleName**, and **abilityName**. It is usually used in [AbilityRunningInfo.ability](../../application/abilityrunninginfo/document.md) for component launch information and in the [connectOptions.onConnect](../../ability/connectoptions/document.md#onconnect) callback for component connection.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/DE9UtvGhT-WftZbs8RI7rg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062210Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FB936F9114B496FF5481EFA31EF10499C2D41946CA2380CA54BF41C2580649B4)

The initial APIs of this module are supported since API version 9. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { bundleManager } from '@kit.AbilityKit';

#### ElementName

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.BundleManager.BundleFramework.Core

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| deviceId | string | No | Yes | Device ID. |
| bundleName | string | No | No | Bundle name. |
| abilityName | string | No | No | Name of the ability. |
| uri | string | No | Yes | Resource ID. |
| shortName | string | No | Yes | Short name of the ability. It is a string starting with a period (.). |
| moduleName | string | No | Yes | Module name of the HAP file to which the ability belongs. |
