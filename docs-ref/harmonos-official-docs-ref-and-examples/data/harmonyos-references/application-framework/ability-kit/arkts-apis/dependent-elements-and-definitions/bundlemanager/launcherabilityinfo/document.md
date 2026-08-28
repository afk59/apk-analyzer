# LauncherAbilityInfo

The module describes the ability information of the launcher application. The information can be obtained by calling [getLauncherAbilityInfoSync](../../../both-models-recommended/ohos-bundle-launcherbundlemanager-launcherbundlemanager-module/document.md#launcherbundlemanagergetlauncherabilityinfosync).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/KmmKp2mrT8uVqv05ATVa9w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062211Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D862221570A6BC241A0E658512B05EAACEB4D32445BAA270BC68C6297658FEB2)

The initial APIs of this module are supported since API version 18. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { launcherBundleManager } from '@kit.AbilityKit';

#### LauncherAbilityInfo

**System capability**: SystemCapability.BundleManager.BundleFramework.Launcher

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| applicationInfo | [ApplicationInfo](../applicationinfo/document.md) | Yes | No | Application information of the launcher ability. |
| elementName | [ElementName](../elementname/document.md) | Yes | No | Element name of the launcher ability. |
| labelId | number | Yes | No | Label ID of the launcher ability. |
| iconId | number | Yes | No | Icon ID of the launcher ability. |
| userId | number | Yes | No | User ID of the launcher ability. |
| installTime | number | Yes | No | Timestamp when the launcher ability was installed, in milliseconds. |
