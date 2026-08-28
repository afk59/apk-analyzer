# Resource

Provides resource information, such as the application bundle name, application module name, and resource ID.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/IO_EFVd9RHiSFUf_grdu-g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062326Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DD72768FE8D476CA9DFB7CF49B9370D88030804E7B7CC92C7EAAD3BAF6A76FE8)

The initial APIs of this module are supported since API version 9. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Import a module.

import { resourceManager } from '@kit.LocalizationKit'

#### Resource

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Global.ResourceManager

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| bundleName | string | No | No | Bundle name of the application. |
| moduleName | string | No | No | Module name of the application. |
| id | number | No | No | Resource ID. |
| params | any\[\] | No | Yes | Other resource parameters, including the resource name, substitution value for the formatting API, and quantifier for the singular-plural formatting API. |
| type | number | No | Yes | Resource type. |
