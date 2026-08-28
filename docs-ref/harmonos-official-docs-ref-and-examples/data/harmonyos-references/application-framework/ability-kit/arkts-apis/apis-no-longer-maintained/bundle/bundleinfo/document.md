# BundleInfo

The module defines the bundle information, which can be obtained through [bundle.getBundleInfo](../../ohos-bundle-bundle-module/document.md#bundlegetbundleinfodeprecated).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/0jguBNWWR-i7rLBZRuX2Qg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062212Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=65FDDA60BB63C21DF202B578CDCCEC9CA1974FC5C1A01E92E49CF07A1DB10836)

The initial APIs of this module are supported since API version 7. Newly added APIs will be marked with a superscript to indicate their earliest API version.

The APIs of this module have been deprecated since API version 9. You are advised to use [bundleManager-BundleInfo](../../../dependent-elements-and-definitions/bundlemanager/bundleinfo/document.md) instead.

#### BundleInfo(deprecated)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/MVssLxciTtuMKI1dYFImKg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062212Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6644B25719EAC61000071F477E5349AF09099BB9B58C96709DA796D03D352F6F)

This API has been supported since API version 7 and deprecated since API version 9. You are advised to use [bundleManager-BundleInfo](../../../dependent-elements-and-definitions/bundlemanager/bundleinfo/document.md#bundleinfo-1) instead.

**System capability**: SystemCapability.BundleManager.BundleFramework

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| name | string | Yes | No | Bundle name. |
| type | string | Yes | No | Bundle type. |
| appId | string | Yes | No | ID of the application to which the bundle belongs. |
| uid | number | Yes | No | UID of the application to which the bundle belongs. |
| installTime | number | Yes | No | Time when the HAP file was installed. |
| updateTime | number | Yes | No | Time when the HAP file was updated. |
| appInfo | [ApplicationInfo](../applicationinfo/document.md) | Yes | No | Application configuration information. |
| abilityInfos | Array<[AbilityInfo](../abilityinfo/document.md)\> | Yes | No | 
Ability configuration information.

The value is obtained by passing in GET\_BUNDLE\_WITH\_ABILITIES to [bundle.getBundleInfo](../../ohos-bundle-bundle-module/document.md#bundlegetbundleinfodeprecated).

 |
| reqPermissions | Array<string> | Yes | No | 

Permissions to request from the system for running the application.

The value is obtained by passing in GET\_BUNDLE\_WITH\_REQUESTED\_PERMISSION to [bundle.getBundleInfo](../../ohos-bundle-bundle-module/document.md#bundlegetbundleinfodeprecated).

 |
| reqPermissionDetails | Array<[ReqPermissionDetail](#reqpermissiondetaildeprecated)\> | Yes | No | 

Detailed information of the permissions to request from the system.

The value is obtained by passing in GET\_BUNDLE\_WITH\_REQUESTED\_PERMISSION to [bundle.getBundleInfo](../../ohos-bundle-bundle-module/document.md#bundlegetbundleinfodeprecated).

 |
| vendor | string | Yes | No | Vendor of the bundle. |
| versionCode | number | Yes | No | Version number of the bundle. |
| versionName | string | Yes | No | Version description of the bundle. |
| compatibleVersion | number | Yes | No | Earliest SDK version required for running the bundle. |
| targetVersion | number | Yes | No | Latest SDK version required for running the bundle. |
| isCompressNativeLibs | boolean | Yes | No | Whether the native libraries in the bundle are compressed. **true** if compressed, **false** otherwise. |
| hapModuleInfos | Array<[HapModuleInfo](../hapmoduleinfo/document.md)\> | Yes | No | Module configuration information. |
| entryModuleName | string | Yes | No | Name of the entry module. |
| cpuAbi | string | Yes | No | CPU and ABI information of the bundle. |
| isSilentInstallation | string | Yes | No | Whether the application can be installed in silent mode. |
| minCompatibleVersionCode | number | Yes | No | Earliest version compatible with the bundle in the distributed scenario. |
| entryInstallationFree | boolean | Yes | No | Whether installation-free is supported for the entry module. **true** if supported, **false** otherwise. |
| reqPermissionStates8+ | Array<number> | Yes | No | Permission grant state. The value **0** means that the request is successful, and **\-1** means the opposite. |

#### ReqPermissionDetail(deprecated)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/GTJA_0_URyCh0IApoadktg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062212Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A44373D660EF05B6EBB776774DB90FE2DE07920882F9357CD5E679AB7CE2705B)

This API has been supported since API version 7 and deprecated since API version 9. You are advised to use [ReqPermissionDetail](../../../dependent-elements-and-definitions/bundlemanager/bundleinfo/document.md) instead.

Provides the detailed information of the permissions to request from the system.

**System capability**: SystemCapability.BundleManager.BundleFramework

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| name | string | No | No | Name of the permission to request. |
| reason | string | No | No | Reason for requesting the permission. |
| usedScene | [UsedScene](#usedscenedeprecated) | No | No | Application scenario and timing for using the permission. |

#### UsedScene(deprecated)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/f6rd43DRThudhaa2Fe-1Hg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062212Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8402E1CC9F0CAF01C3E9F6D51E4EE7F4C32B9AE629AE16944D0369FFF67AFCFF)

This API has been supported since API version 7 and deprecated since API version 9. You are advised to use [UsedScene](../../../dependent-elements-and-definitions/bundlemanager/bundleinfo/document.md#usedscene) instead.

Describes the application scenario and timing for using the permission.

**System capability**: SystemCapability.BundleManager.BundleFramework

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| abilities | Array<string> | No | No | Abilities that use the permission. |
| when | string | No | No | Time when the permission is used. |
