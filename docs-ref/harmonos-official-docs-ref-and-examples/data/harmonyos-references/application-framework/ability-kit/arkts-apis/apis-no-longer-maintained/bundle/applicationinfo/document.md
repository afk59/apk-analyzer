# ApplicationInfo

The module provides application information. Unless otherwise specified, the information is obtained through [bundle.getApplicationInfo](../../ohos-bundle-bundle-module/document.md#bundlegetapplicationinfodeprecated).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/kxdmN9evSEmWdOzYaLbXCw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062212Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7497EC4C91E6786D3ED6C41CB2925E809C7266264A68B603D6DC13A6DEE7106E)

The initial APIs of this module are supported since API version 7. Newly added APIs will be marked with a superscript to indicate their earliest API version.

The APIs of this module have been deprecated since API version 9. You are advised to use [bundleManager-ApplicationInfo](../../../dependent-elements-and-definitions/bundlemanager/applicationinfo/document.md) instead.

#### ApplicationInfo(deprecated)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/NCw7lThPSICyYE7iqZ4-hw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062212Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EFBB188384FEF1C032062C529FA8CD8AECB331CE3E16D398583ECEF7F4879A8D)

This API has been supported since API version 7 and deprecated since API version 9. You are advised to use [bundleManager-ApplicationInfo](../../../dependent-elements-and-definitions/bundlemanager/applicationinfo/document.md#applicationinfo-1) instead.

**System capability**: SystemCapability.BundleManager.BundleFramework

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| name | string | Yes | No | Application name. |
| description | string | Yes | No | Application description. |
| descriptionId | number | Yes | No | ID of the application description. |
| systemApp | boolean | Yes | No | Whether the application is a system application. **true** if yes, **false** otherwise. |
| enabled | boolean | Yes | No | Whether the application is enabled. **true** if enabled, **false** otherwise. |
| label | string | Yes | No | Application label. |
| labelId | string | Yes | No | ID of the application label. |
| icon | string | Yes | No | Application icon. |
| iconId | string | Yes | No | ID of the application icon. |
| process | string | Yes | No | Process name. |
| supportedModes | number | Yes | No | Modes supported by the application. Currently, only the **drive** mode is defined. This attribute applies only to telematics devices. |
| moduleSourceDirs | Array<string> | Yes | No | Relative paths for storing application resources. Do not access resource files using concatenated paths. Use [@ohos.resourceManager](../../../../../localization-kit/arkts-apis/ohos-resourcemanager-resource-management/document.md) instead. |
| permissions | Array<string> | Yes | No | 
Permissions required for accessing the application.

The value is obtained by passing in GET\_APPLICATION\_INFO\_WITH\_PERMISSION to [bundle.getApplicationInfo](../../ohos-bundle-bundle-module/document.md#bundlegetapplicationinfodeprecated).

 |
| moduleInfos | Array<[ModuleInfo](../moduleinfo/document.md)\> | Yes | No | Application module information. |
| entryDir | string | Yes | No | Path for storing application files. Do not access resource files using concatenated paths. Use [@ohos.resourceManager](../../../../../localization-kit/arkts-apis/ohos-resourcemanager-resource-management/document.md) instead. |
| codePath8+ | string | Yes | No | Installation directory of the application. Do not access resource files using concatenated paths. Use [@ohos.resourceManager](../../../../../localization-kit/arkts-apis/ohos-resourcemanager-resource-management/document.md) instead. |
| metaData8+ | Map<string, Array<[CustomizeData](../customizedata/document.md)\>> | Yes | No | 

Custom metadata of the application.

The value is obtained by passing in GET\_APPLICATION\_INFO\_WITH\_METADATA to [bundle.getApplicationInfo](../../ohos-bundle-bundle-module/document.md#bundlegetapplicationinfodeprecated).

 |
| removable8+ | boolean | Yes | No | Whether the application is removable. **true** if removable, **false** otherwise. |
| accessTokenId8+ | number | Yes | No | Access token ID of the application. |
| uid8+ | number | Yes | No | UID of the application. |
| entityType | string | Yes | No | Type of the application, for example, gaming, social networking, movies, and news. |
