# Metadata

The module defines a metadata object. An application can obtain the metadata through [bundleManager.getBundleInfoForSelf](../../../both-models-recommended/ohos-bundle-bundlemanager-bundle-management-module/document.md#bundlemanagergetbundleinfoforself), with **GET\_BUNDLE\_INFO\_WITH\_METADATA** passed in for [bundleFlags](../../../both-models-recommended/ohos-bundle-bundlemanager-bundle-management-module/document.md#bundleflag). This object is contained in [ApplicationInfo](../applicationinfo/document.md), [HapModuleInfo](../hapmoduleinfo/document.md), [AbilityInfo](../abilityinfo/document.md), and [ExtensionAbilityInfo](../extensionabilityinfo/document.md).

The module provides the configuration about the module, UIAbility, and ExtensionAbility. The value is of the array type. The configuration is valid only for the current module, UIAbility, or ExtensionAbility.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/-kl0jMowQRmwDVccfaUm3g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062210Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=637D4FA83C5BB39DFCB8F55E88AB96D7226283BA2E2477709F4F92865C7DD958)

The initial APIs of this module are supported since API version 9. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { bundleManager } from '@kit.AbilityKit';

#### Metadata

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.BundleManager.BundleFramework.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| name | string | No | No | Metadata name. |
| value | string | No | No | Metadata value. |
| resource | string | No | No | Metadata resource descriptor. For details, see **$profile:config\_file**, which indicates the **config\_file.json** file configured in the **profile** directory. |
| valueId18+ | number | Yes | Yes | ID of the metadata value. If **valueId** is not set to **0**, the current metadata value is customized, and **valueId** must be used to obtain the corresponding value from the resource manager module. If **valueId** is set to **0**, the current metadata value is a fixed string. |
