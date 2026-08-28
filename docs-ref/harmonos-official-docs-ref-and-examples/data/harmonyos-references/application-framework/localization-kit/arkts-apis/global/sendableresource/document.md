# SendableResource

The **SendableResource** module provides sendable resource information, such as the application bundle name, application module name, and resource ID.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/G6hyUlvxQCGRrJWdCkaWgQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062327Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E7B716DE163D0A7FF125A75ED5F19253798695B58B6DFCB6443B97C611F1FA38)

The initial APIs of this module are supported since API version 12. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Import a module.

import { resourceManager } from '@kit.LocalizationKit';

#### SendableResource

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.ResourceManager

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| bundleName | string | No | No | Bundle name of the application. |
| moduleName | string | No | No | Module name of the application. |
| id | number | No | No | Resource ID. |
| params | collections.Array<string | number> | No | Yes | Other resource parameters, including the resource name, substitution value for the formatting API, and quantifier for the singular-plural formatting API. |
| type | number | No | Yes | Resource type. |
