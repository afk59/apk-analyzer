# ExtensionAbilityInfo

The module defines the ExtensionAbility information. An application can obtain its own ExtensionAbility information through [bundleManager.getBundleInfoForSelf](../../../both-models-recommended/ohos-bundle-bundlemanager-bundle-management-module/document.md#bundlemanagergetbundleinfoforself), with **GET\_BUNDLE\_INFO\_WITH\_HAP\_MODULE** and **GET\_BUNDLE\_INFO\_WITH\_EXTENSION\_ABILITY** passed in to [bundleFlags](../../../both-models-recommended/ohos-bundle-bundlemanager-bundle-management-module/document.md#bundleflag).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1/v3/qD-vFT7fSYKd-kQ9WcV-Ww/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062210Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2B9076A031E3741440E5C991139F0BC0DF8B82F2FC5485C8B2B84C28A07FFBB6)

The initial APIs of this module are supported since API version 9. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { bundleManager } from '@kit.AbilityKit';

#### ExtensionAbilityInfo

**System capability**: SystemCapability.BundleManager.BundleFramework.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| bundleName | string | Yes | No | 
Bundle name.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| moduleName | string | Yes | No | 

Name of the HAP file to which the ExtensionAbility belongs.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| name | string | Yes | No | 

Name of the ExtensionAbility.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| labelId | number | Yes | No | 

ID of the ExtensionAbility label.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| descriptionId | number | Yes | No | 

ID of the ExtensionAbility description.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| iconId | number | Yes | No | 

ID of the ExtensionAbility icon.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| exported | boolean | Yes | No | 

Whether the ExtensionAbility can be called by other applications. **true** if the ExtensionAbility can be called by other applications, **false** otherwise.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| extensionAbilityType | [bundleManager.ExtensionAbilityType](../../../both-models-recommended/ohos-bundle-bundlemanager-bundle-management-module/document.md#extensionabilitytype) | Yes | No | 

Type of the ExtensionAbility.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| permissions | Array<string> | Yes | No | 

Permissions required for other bundles to call the ExtensionAbility.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| applicationInfo | [ApplicationInfo](../applicationinfo/document.md) | Yes | No | 

Application configuration information .

This field is not returned when the [getBundleInfoForSelf](../../../both-models-recommended/ohos-bundle-bundlemanager-bundle-management-module/document.md#bundlemanagergetbundleinfoforself) or [getBundleInfo](../../../both-models-recommended/ohos-bundle-bundlemanager-bundle-management-module/document.md#bundlemanagergetbundleinfo14) is used to obtain ExtensionAbilityInfo information. You can obtain the related information by obtaining the [bundleInfo](../bundleinfo/document.md#bundleinfo-1).appInfo object.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| metadata | Array<[Metadata](../metadata/document.md)\> | Yes | No | 

Metadata of the ExtensionAbility. The information can be obtained by passing in **GET\_BUNDLE\_INFO\_WITH\_HAP\_MODULE**, **GET\_BUNDLE\_INFO\_WITH\_EXTENSION\_ABILITY**, and **GET\_BUNDLE\_INFO\_WITH\_METADATA** to the **bundleFlags** parameter of [getBundleInfoForSelf](../../../both-models-recommended/ohos-bundle-bundlemanager-bundle-management-module/document.md#bundlemanagergetbundleinfoforself).

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| enabled | boolean | Yes | No | 

Whether the ExtensionAbility is enabled. **true** if enabled, **false** otherwise.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| readPermission | string | Yes | No | 

Permission required for reading data from the ExtensionAbility.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| writePermission | string | Yes | No | 

Permission required for writing data to the ExtensionAbility.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| extensionAbilityTypeName11+ | string | Yes | No | 

Type of the ExtensionAbility. For details about available values, see [the type field under the extensionabilities tag](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/module-configuration-file#extensionabilities).

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| skills12+ | Array<[Skill](../skill/document.md)\> | Yes | No | 

Skills of the ExtensionAbility.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| appIndex12+ | number | Yes | No | Index of an application clone. It takes effect only for cloned applications. |
