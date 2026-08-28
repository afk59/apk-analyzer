# BundleInfo

The module defines the bundle information. An application can obtain its own bundle information through [bundleManager.getBundleInfoForSelf](../../../both-models-recommended/ohos-bundle-bundlemanager-bundle-management-module/document.md#bundlemanagergetbundleinfoforself), with [bundleFlags](../../../both-models-recommended/ohos-bundle-bundlemanager-bundle-management-module/document.md#bundleflag) set to the information to be contained in the returned [BundleInfo](#).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/JmVEc2rjTvGxmSiKoze3cA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062210Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=338402AE1B1C31E7BDCE7F3E732F55AC61464C93B43D5125BF278F5D9AB9A305)

The initial APIs of this module are supported since API version 9. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { bundleManager } from '@kit.AbilityKit';

#### BundleInfo

**System capability**: SystemCapability.BundleManager.BundleFramework.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| name | string | Yes | No | 
Name of the application package. It corresponds to the **bundleName** field in the [app.json5](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-configuration-file) file.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| vendor | string | Yes | No | 

Vendor of the application package. It corresponds to the **vendor** field in the [app.json5](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-configuration-file) file.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| versionCode | number | Yes | No | 

Version code of the application package. It corresponds to the **versionCode** field in the [app.json5](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-configuration-file) file.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| versionName | string | Yes | No | 

Version description of the application package. It corresponds to the **versionName** field in the [app.json5](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-configuration-file) file.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| minCompatibleVersionCode | number | Yes | No | 

Minimum compatible version of the application package in the distributed scenario. It corresponds to the **minCompatibleVersionCode** field in the [app.json5](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-configuration-file) file.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| targetVersion | number | Yes | No | 

Target version of the application. It corresponds to the **targetAPIVersion** field in the [app.json5](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-configuration-file) file.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| appInfo | [ApplicationInfo](../applicationinfo/document.md) | Yes | No | 

Application information. The information can be obtained by passing in **GET\_BUNDLE\_INFO\_WITH\_APPLICATION** to the **bundleFlags** parameter of [getBundleInfoForSelf](../../../both-models-recommended/ohos-bundle-bundlemanager-bundle-management-module/document.md#bundlemanagergetbundleinfoforself).

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| hapModulesInfo | Array<[HapModuleInfo](../hapmoduleinfo/document.md)\> | Yes | No | 

Module configuration information. The information can be obtained by passing in **GET\_BUNDLE\_INFO\_WITH\_HAP\_MODULE** to the **bundleFlags** parameter of [getBundleInfoForSelf](../../../both-models-recommended/ohos-bundle-bundlemanager-bundle-management-module/document.md#bundlemanagergetbundleinfoforself).

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| reqPermissionDetails | Array<[ReqPermissionDetail](#reqpermissiondetail)\> | Yes | No | 

Detailed information of the permissions to request from the system. The information can be obtained by passing in **GET\_BUNDLE\_INFO\_WITH\_REQUESTED\_PERMISSION** to the **bundleFlags** parameter of [getBundleInfoForSelf](../../../both-models-recommended/ohos-bundle-bundlemanager-bundle-management-module/document.md#bundlemanagergetbundleinfoforself). The indices of the **reqPermissionDetails** array and the **permissionGrantStates** array are in one-to-one correspondence, meaning that the authorization status of **reqPermissionDetails\[2\]** is **permissionGrantStates\[2\]**.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| permissionGrantStates | Array<[bundleManager.PermissionGrantState](../../../both-models-recommended/ohos-bundle-bundlemanager-bundle-management-module/document.md#permissiongrantstate)\> | Yes | No | 

Permission grant state. The information can be obtained by passing in **GET\_BUNDLE\_INFO\_WITH\_REQUESTED\_PERMISSION** to the **bundleFlags** parameter of [getBundleInfoForSelf](../../../both-models-recommended/ohos-bundle-bundlemanager-bundle-management-module/document.md#bundlemanagergetbundleinfoforself). The indices of the **reqPermissionDetails** array and the **permissionGrantStates** array are in one-to-one correspondence, meaning that the authorization status of **reqPermissionDetails\[2\]** is **permissionGrantStates\[2\]**.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| signatureInfo | [SignatureInfo](#signatureinfo) | Yes | No | 

Signature information of the bundle. The information can be obtained by passing in **GET\_BUNDLE\_INFO\_WITH\_SIGNATURE\_INFO** to the **bundleFlags** parameter of [getBundleInfoForSelf](../../../both-models-recommended/ohos-bundle-bundlemanager-bundle-management-module/document.md#bundlemanagergetbundleinfoforself).

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| installTime | number | Yes | No | 

Timestamp for the installation of the application package. It measures the milliseconds that have passed since the Unix epoch (January 1, 1970, 08:00:00 UTC+8), in milliseconds.

**Atomic service API**: This API can be used in atomic services since API version 11.

**NOTE**

If the current time is not obtained when the device is powered on for the first time from the factory, the Unix epoch (1970-01-01 08:00:00 UTC+8) is used as the start time of the current system. For example, if the time is not obtained after startup and the installation succeeds after a 32-second wait, the application package installation timestamp is 32000.

 |
| updateTime | number | Yes | No | 

Timestamp for the last update of the application package. It measures the milliseconds that have passed since the Unix epoch (January 1, 1970, 08:00:00 UTC+8), in milliseconds.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| routerMap12+ | Array<[RouterItem](../hapmoduleinfo/document.md#routeritem12)\> | Yes | No | 

Router table of the application. The table is obtained by deduplicating and combining the **routerMap** information under **hapModulesInfo** based on the **name** field in **RouterItem**. The information can be obtained by passing in **GET\_BUNDLE\_INFO\_WITH\_HAP\_MODULE** and **GET\_BUNDLE\_INFO\_WITH\_ROUTER\_MAP** to the **bundleFlags** parameter of [getBundleInfoForSelf](../../../both-models-recommended/ohos-bundle-bundlemanager-bundle-management-module/document.md#bundlemanagergetbundleinfoforself).

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| appIndex12+ | number | Yes | No | Index of an application clone. It takes effect only for application clones. |
| firstInstallTime18+ | number | Yes | Yes | 

Timestamp for the initial installation of the application package. It measures the milliseconds that have passed since the Unix epoch (January 1, 1970, 08:00:00 UTC+8), in milliseconds. For preinstalled applications, the initial installation timestamp is 1533657660000.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |

#### ReqPermissionDetail

Provides the detailed information of the permissions to request from the system.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/c6pTsbbPTSaNPV1CnKyVlw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062210Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EC0F3CBF393B08D341130CA5A132C900CDBF92386EB33931103D1F8A61CD3AAE)

-   If multiple packages of an application have requested the same permission but with different reasons, the system returns only one reason based on a descending priority order: entry HAP > feature HAP > in-app HSP.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.BundleManager.BundleFramework.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| name | string | No | No | [Name of the permission](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-permissions) to request. |
| moduleName10+ | string | No | No | Name of the module that requests the permission. |
| reason | string | No | No | Reason for requesting the permission. |
| reasonId | number | No | No | ID of the reason for requesting the permission. |
| usedScene | [UsedScene](#usedscene) | No | No | Use scenario and timing for using the permission. |

#### UsedScene

Describes the use scenario and timing for using the permission.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.BundleManager.BundleFramework.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| abilities | Array<string> | No | No | Abilities that use the permission. |
| when | string | No | No | Time when the permission is used. The value can be **inuse** or **always**. |

#### SignatureInfo

Describes the signature information of the bundle.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.BundleManager.BundleFramework.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| appId | string | Yes | No | 
App ID, which uniquely identifies an app. For details, see [What Is appId?](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/common-problem-of-application#what-is-appid).

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| fingerprint | string | Yes | No | 

Fingerprint information of the application package. It is generated by calculating the hash value of the signing certificate using the SHA-256 algorithm. This field changes when the used signing certificate changes.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| appIdentifier11+ | string | Yes | No | 

Unique ID of the application. For details, see [What is appIdentifier?](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/common-problem-of-application#what-is-appidentifier).

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| certificate14+ | string | Yes | Yes | 

Public key of the application certificate.

**Atomic service API**: This API can be used in atomic services since API version 14.

 |

#### AppCloneIdentity14+

Describes the identity information of an application clone.

**System capability**: SystemCapability.BundleManager.BundleFramework.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| bundleName | string | Yes | No | Bundle name of the application. |
| appIndex | number | Yes | No | Index of the application clone. |
