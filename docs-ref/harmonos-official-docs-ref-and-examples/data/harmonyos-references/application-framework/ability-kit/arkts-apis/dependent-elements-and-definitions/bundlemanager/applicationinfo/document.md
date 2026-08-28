# ApplicationInfo

The module defines the application information. An application can obtain its own application information through [bundleManager.getBundleInfoForSelf](../../../both-models-recommended/ohos-bundle-bundlemanager-bundle-management-module/document.md#bundlemanagergetbundleinfoforself), with **GET\_BUNDLE\_INFO\_WITH\_APPLICATION** passed in to [bundleFlags](../../../both-models-recommended/ohos-bundle-bundlemanager-bundle-management-module/document.md#bundleflag).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/DvIfqo6fQdKDheds4ZLduw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062210Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0F9E8EE081872F4A84E6517D96EC54F48E27B75B04EA9FFF8200BDC979AE147C)

The initial APIs of this module are supported since API version 9. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { bundleManager } from '@kit.AbilityKit';

#### ApplicationInfo

**System capability**: SystemCapability.BundleManager.BundleFramework.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| name | string | Yes | No | 
Name of the application bundle. It corresponds to the **bundleName** field in the [app.json5](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-configuration-file) file.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| description | string | Yes | No | 

Description of the application. It corresponds to the **description** field in the [app.json5](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-configuration-file). For details about **description**, see the **descriptionResource** field in this table.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| descriptionId | number | Yes | No | 

Resource ID of the application description. It is automatically generated during compilation and build based on the description configured for the application.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| enabled | boolean | Yes | No | 

Whether the application is enabled. **true** if enabled, **false** otherwise.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| label | string | Yes | No | 

Application label. It corresponds to the **label** field in the [app.json5](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-configuration-file) file. For details about **label**, see the **labelResource** field in this table. Starting from API version 20, if [bundleManager.getAbilityInfo](../../../both-models-recommended/ohos-bundle-bundlemanager-bundle-management-module/document.md#bundlemanagergetabilityinfo20) is used to obtain application information, this field is the application name visible to users, instead of the resource descriptor.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| labelId | number | Yes | No | 

Resource ID of the application label. It is automatically generated during compilation and build based on the label configured for the application.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| icon | string | Yes | No | 

Application icon. It corresponds to the **icon** field in the [app.json5](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-configuration-file) file. For details about **icon**, see the **iconResource** field in this table.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| iconId | number | Yes | No | 

Resource ID of the application icon. It is automatically generated during compilation and build based on the icon configured for the application.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| process | string | Yes | No | 

Process name.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| permissions | Array<string> | Yes | No | 

Permission list required for accessing the application.

This field is not returned when the [getBundleInfoForSelf](../../../both-models-recommended/ohos-bundle-bundlemanager-bundle-management-module/document.md#bundlemanagergetbundleinfoforself) or [getBundleInfo](../../../both-models-recommended/ohos-bundle-bundlemanager-bundle-management-module/document.md#bundlemanagergetbundleinfo14) is used to obtain application information. You can obtain the permission list by obtaining the [bundleInfo](../bundleinfo/document.md#bundleinfo-1).reqPermissionDetails.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| codePath | string | Yes | No | 

Installation directory of the application.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| metadata(deprecated) | Map<string, Array<[Metadata](../metadata/document.md)\>> | Yes | No | 

Metadata of the application. The information can be obtained by passing in **GET\_BUNDLE\_INFO\_WITH\_APPLICATION** and **GET\_BUNDLE\_INFO\_WITH\_METADATA** to the **bundleFlags** parameter of [getBundleInfoForSelf](../../../both-models-recommended/ohos-bundle-bundlemanager-bundle-management-module/document.md#bundlemanagergetbundleinfoforself).

Note: Supported since API version 9 and deprecated since API version 10. You are advised to use **metadataArray** instead.

 |
| metadataArray10+ | Array<[ModuleMetadata](#modulemetadata10)\> | Yes | No | 

Metadata of the application. The information can be obtained by passing in **GET\_BUNDLE\_INFO\_WITH\_APPLICATION** and **GET\_BUNDLE\_INFO\_WITH\_METADATA** to the **bundleFlags** parameter of [getBundleInfoForSelf](../../../both-models-recommended/ohos-bundle-bundlemanager-bundle-management-module/document.md#bundlemanagergetbundleinfoforself).

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| removable | boolean | Yes | No | 

Whether the application is removable. **true** if removable, **false** otherwise.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| accessTokenId | number | Yes | No | 

Access token ID of the application, which is used in the [application access control verification API](../../../both-models-recommended/ohos-abilityaccessctrl-application-access-control/document.md#checkaccesstoken9).

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| uid | number | Yes | No | 

UID of the application.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| iconResource | [Resource](../../../../../localization-kit/arkts-apis/ohos-resourcemanager-resource-management/document.md#resource9) | Yes | No | 

Resource information of the application icon. The resource information obtained contains the bundle name, module name, and ID of the resource. You can call [getMediaContent](../../../../../localization-kit/arkts-apis/ohos-resourcemanager-resource-management/document.md#getmediacontent9) to obtain the resource details.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| labelResource | [Resource](../../../../../localization-kit/arkts-apis/ohos-resourcemanager-resource-management/document.md#resource9) | Yes | No | 

Resource information of the application label. The resource information obtained contains the bundle name, module name, and ID of the resource. You can call [getMediaContent](../../../../../localization-kit/arkts-apis/ohos-resourcemanager-resource-management/document.md#getmediacontent9) to obtain the resource details.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| descriptionResource | [Resource](../../../../../localization-kit/arkts-apis/ohos-resourcemanager-resource-management/document.md#resource9) | Yes | No | 

Resource information of the application description. The resource information obtained contains the bundle name, module name, and ID of the resource. You can call [getMediaContent](../../../../../localization-kit/arkts-apis/ohos-resourcemanager-resource-management/document.md#getmediacontent9) to obtain the resource details.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| appDistributionType | string | Yes | No | Distribution type of the application signing certificate. The options are as follows:-   **app\_gallery**: application installed from AppGallery. For details about how to apply for a signing certificate, see [Requesting a Release Profile](https://developer.huawei.com/consumer/en/doc/app/agc-help-release-profile-0000002248341090).
-   **enterprise**: enterprise internal application. These are applications developed by an enterprise for its internal use by employees only. They are not distributed through public channels like AppGallery but are distributed internally via the enterprise's own channels. For details about how to apply for a signing certificate, see [Requesting an In-House Release Profile](https://developer.huawei.com/consumer/en/doc/app/agc-help-inhouse-profile-0000002283340021).
-   **enterprise\_mdm**: enterprise [Mobile Device Management (MDM) application](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/mdm-kit-term#mdm-application-device-administrator-application).
-   **enterprise\_normal**: standard enterprise application. These applications do not need to be released to AppGallery. Instead, they can be distributed and installed through an enterprise [MDM application](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/mdm-kit-term#mdm-application-device-administrator-application) and offline installer.
-   **os\_integration**: pre-installed application. They are not available for third-party applications.
-   crowdtesting: application under crowdtesting, which is distributed by AppGallery to a limited number of users and come with a set expiration date. When the system detects that the validity period of the application expires, it prompts the user to update to the release version available on AppGallery. This API is deprecated since API version 11.
-   **internaltesting**: application under internal testing of AppGallery.
-   none: others.
    
    **Atomic service API**: This API can be used in atomic services since API version 11.
     |
| appProvisionType | string | Yes | No | 

Type of the application signing certificate file. The options are **debug** and **release**.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| systemApp | boolean | Yes | No | 

Whether the application is a system application. **true** if it is a system application, **false** otherwise.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| bundleType | [bundleManager.BundleType](../../../both-models-recommended/ohos-bundle-bundlemanager-bundle-management-module/document.md#bundletype) | Yes | No | 

Bundle type, which can be **APP** (application) or **ATOMIC\_SERVICE** (atomic service).

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| debug10+ | boolean | Yes | No | 

Whether the application is running in debug mode. **true** if in debug mode, **false** otherwise.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| dataUnclearable11+ | boolean | Yes | No | 

Whether the application data is unclearable. **true** if unclearable, **false** otherwise.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| nativeLibraryPath12+ | string | Yes | No | Local library file path of the application. |
| multiAppMode12+ | [MultiAppMode](#multiappmode12) | Yes | No | Multi-app mode. |
| appIndex12+ | number | Yes | No | Index of an application clone. It takes effect only for cloned applications. |
| installSource12+ | string | Yes | No | 

Installation source of an application. The options are as follows:

\- **pre-installed**: pre-installed application installed during the first boot.

\- **ota**: pre-installed application added during system upgrade.

\- **recovery**: pre-installed application manually restored by the user after uninstallation.

\- **bundleName**: installation by the application corresponding to this bundle name. **bundleName** represents a variable, subject to the actual value.

\- **unknown**: unknown application installation source.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| releaseType12+ | string | Yes | No | 

Release type of the SDK used for application packing. Currently, the SDK release types include Canary, Beta, and Release. Each of the Canary and Beta releases can be distinguished by a sequential number, such as Canary1, Canary2, Beta1, and Beta2. You can compare the SDK release type on which application packaging depends and the OS release type (specified by [deviceInfo.distributionOSReleaseType](../../../../../../system/basic-functions/basic-services-kit/arkts-apis/device-management/ohos-deviceinfo-device-information/document.md)) to determine the compatibility.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| cloudFileSyncEnabled12+ | boolean | Yes | No | 

Whether device-cloud file synchronization is enabled for the application. **true** if enabled, **false** otherwise.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| cloudStructuredDataSyncEnabled20+ | boolean | Yes | Yes | 

Whether device-cloud structured data synchronization is enabled for the application. **true** if enabled, **false** otherwise.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |

#### MultiAppMode12+

Defines the [multi-app mode](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/multiinstance).

**System capability**: SystemCapability.BundleManager.BundleFramework.Core

**Parameters**

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| multiAppModeType | [bundleManager.MultiAppModeType](../../../both-models-recommended/ohos-bundle-bundlemanager-bundle-management-module/document.md#multiappmodetype12) | Yes | No | Type of the multi-app mode. |
| maxCount | number | Yes | No | Maximum number of accounts that can log in to the application at the same time. |

#### ModuleMetadata10+

Describes the metadata of a module.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.BundleManager.BundleFramework.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| moduleName | string | Yes | No | Module name. |
| metadata | Array<[Metadata](../metadata/document.md)\> | Yes | No | Metadata list of the module. |
