# AppVersionInfo

The module defines the application version information. You can use [getAppVersionInfo](../context-context-base-class-of-the-fa-model/document.md#contextgetappversioninfo7) to obtain the version information of the current application.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/LDv2C9FwT32bOKAE3N8RuA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062207Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=29E67D56522259EEB2C8A14D9533D03A7E5001C60E08563694CE145510992523)

The initial APIs of this module are supported since API version 7. Newly added APIs will be marked with a superscript to indicate their earliest API version.

The APIs of this module can be used only in the FA model.

#### Modules to Import

import featureAbility from '@ohos.ability.featureAbility';

#### Attributes

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| appName | string | Yes | No | Application name. |
| versionCode | number | Yes | No | Application version code. |
| versionName | string | Yes | No | Application version name. |
