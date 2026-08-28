# HapModuleInfo

The module defines the HAP module information. An application can obtain its own HAP module information through [getBundleInfoForSelf](../../../both-models-recommended/ohos-bundle-bundlemanager-bundle-management-module/document.md#bundlemanagergetbundleinfoforself), with **GET\_BUNDLE\_INFO\_WITH\_HAP\_MODULE** passed in for [bundleFlags](../../../both-models-recommended/ohos-bundle-bundlemanager-bundle-management-module/document.md#bundleflag).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/TR3lFRgVT5WjWvSF_2gHJQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062210Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=00B8A6B3DBEB14E51366C8B8A1EE3B700C74242729EC87DFC1477554F67E39C7)

The initial APIs of this module are supported since API version 9. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { bundleManager } from '@kit.AbilityKit';

#### HapModuleInfo

**System capability**: SystemCapability.BundleManager.BundleFramework.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| name | string | Yes | No | 
Module name.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| icon | string | Yes | No | 

[Icon](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/layered-image) for the entry ability of the current module. It is the index of the icon resource file and should match the value of **icon** in the [abilities](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/module-configuration-file#abilities) or [extensionAbilities](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/module-configuration-file#extensionabilities) field in the module configuration file. If no entry ability is configured, this parameter is left empty.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| iconId | number | Yes | No | 

[Resource ID](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/resource-categories-and-access#resource-directories) of the icon for the entry ability of the current module. If no entry ability is configured, this parameter is left empty.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| label | string | Yes | No | 

Label of the entry ability of the current module. It is the index of a string resource and should match the value of **label** in the [abilities](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/module-configuration-file#abilities) or [extensionAbilities](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/module-configuration-file#extensionabilities) field in the module configuration file. If no entry ability is configured, this parameter is left empty.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| labelId | number | Yes | No | 

[Resource ID](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/resource-categories-and-access#resource-directories) of the label for the entry ability of the current module. If no entry ability is configured, this parameter is left empty.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| description | string | Yes | No | 

Module description.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| descriptionId | number | Yes | No | 

ID of the module description.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| mainElementName | string | Yes | No | 

Name of the UIAbility or ExtensionAbility that serves as the entry of the current module.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| abilitiesInfo | Array<[AbilityInfo](../abilityinfo/document.md)\> | Yes | No | 

Information about all ability components of the current module. The information can be obtained by passing in **GET\_BUNDLE\_INFO\_WITH\_HAP\_MODULE** and **GET\_BUNDLE\_INFO\_WITH\_ABILITY** to the **bundleFlags** parameter of [getBundleInfoForSelf](../../../both-models-recommended/ohos-bundle-bundlemanager-bundle-management-module/document.md#bundlemanagergetbundleinfoforself).

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| extensionAbilitiesInfo | Array<[ExtensionAbilityInfo](../extensionabilityinfo/document.md)\> | Yes | No | 

Information about all ExtensionAbility components of the current module. The information can be obtained by passing in **GET\_BUNDLE\_INFO\_WITH\_HAP\_MODULE** and **GET\_BUNDLE\_INFO\_WITH\_EXTENSION\_ABILITY** to the **bundleFlags** parameter of [getBundleInfoForSelf](../../../both-models-recommended/ohos-bundle-bundlemanager-bundle-management-module/document.md#bundlemanagergetbundleinfoforself).

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| metadata | Array<[Metadata](../metadata/document.md)\> | Yes | No | 

Metadata of the current module. The information can be obtained by passing in **GET\_BUNDLE\_INFO\_WITH\_HAP\_MODULE** and **GET\_BUNDLE\_INFO\_WITH\_METADATA** to the **bundleFlags** parameter of [getBundleInfoForSelf](../../../both-models-recommended/ohos-bundle-bundlemanager-bundle-management-module/document.md#bundlemanagergetbundleinfoforself).

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| deviceTypes | Array<string> | Yes | No | 

Array of [device types](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/module-configuration-file#devicetypes) that the module supports for installation and running.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| installationFree | boolean | Yes | No | 

Whether the module supports the installation-free feature. Installation-free means that the module does not need to be explicitly installed through an app market. **true** if the module supports installation-free, **false** otherwise.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| hashValue | string | Yes | No | 

Hash value of the module.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| type | [bundleManager.ModuleType](../../../both-models-recommended/ohos-bundle-bundlemanager-bundle-management-module/document.md#moduletype) | Yes | No | 

Type of the module.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| preloads | Array<[PreloadItem](#preloaditem)\> | Yes | No | 

Preloaded modules in the atomic service.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| dependencies | Array<[Dependency](#dependency)\> | Yes | No | 

Dynamic shared libraries on which the module depends.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| fileContextMenuConfig11+ | string | Yes | No | 

File menu configuration of the module. The information can be obtained by passing in **GET\_BUNDLE\_INFO\_WITH\_HAP\_MODULE** and **GET\_BUNDLE\_INFO\_WITH\_MENU** to the **bundleFlags** parameter of [getBundleInfoForSelf](../../../both-models-recommended/ohos-bundle-bundlemanager-bundle-management-module/document.md#bundlemanagergetbundleinfoforself).

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| routerMap12+ | Array<[RouterItem](#routeritem12)\> | Yes | No | 

[Router table configuration of the module](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/module-configuration-file#routermap). The information can be obtained by passing in **GET\_BUNDLE\_INFO\_WITH\_HAP\_MODULE** and **GET\_BUNDLE\_INFO\_WITH\_ROUTER\_MAP** to the **bundleFlags** parameter of [getBundleInfoForSelf](../../../both-models-recommended/ohos-bundle-bundlemanager-bundle-management-module/document.md#bundlemanagergetbundleinfoforself).

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| codePath12+ | string | Yes | No | 

Installation path of the module.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| nativeLibraryPath12+ | string | Yes | No | Local library file path of the module in the application. |

#### PreloadItem

Describes the preloaded module information in the atomic service.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.BundleManager.BundleFramework.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| moduleName | string | Yes | No | Module name. |

#### Dependency

Describes the information about the dynamic shared library on which the module depends.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.BundleManager.BundleFramework.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| bundleName10+ | string | Yes | No | Name of the shared bundle on which the current module depends. |
| moduleName | string | Yes | No | Module name of the shared bundle on which the current module depends. |
| versionCode10+ | number | Yes | No | Version number of the shared bundle. |

#### RouterItem12+

Describes the router table configuration of the module.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.BundleManager.BundleFramework.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| name | string | Yes | No | Name of the page to be redirected to. |
| pageSourceFile | string | Yes | No | Path of the page in the module. |
| buildFunction | string | Yes | No | Function decorated by @Builder. The function describes the UI of the page. |
| data | Array<[DataItem](#dataitem12)\> | Yes | No | User-defined string in the [routing table configuration file](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/module-configuration-file#routermap), that is, value of the **data** field. This field is parsed by the system. You do not need to parse it. |
| customData | string | Yes | No | Any type of custom data in the [routing table configuration file](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/module-configuration-file#routermap), that is, JSON string of the **customData** field. You need to call **JSON.parse** to parse the field. |

#### DataItem12+

Describes the user-defined data in the routing table configuration of the module.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.BundleManager.BundleFramework.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| key | string | Yes | No | Key of the user-defined data. |
| value | string | Yes | No | Value of the user-defined data. |
