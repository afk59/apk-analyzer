# AbilityInfo

The module defines the ability information. An application can obtain its own ability information through [bundleManager.getBundleInfoForSelf](../../../both-models-recommended/ohos-bundle-bundlemanager-bundle-management-module/document.md#bundlemanagergetbundleinfoforself), with **GET\_BUNDLE\_INFO\_WITH\_HAP\_MODULE** and **GET\_BUNDLE\_INFO\_WITH\_ABILITY** passed in to [bundleFlags](../../../both-models-recommended/ohos-bundle-bundlemanager-bundle-management-module/document.md#bundleflag).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/7a8Zln9NRf-uJ1aEc1inEw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062210Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A40567C3EC37ADB1F15198968300FBEBACBB14FBE9E2ADF9D854912452DBD6CD)

The initial APIs of this module are supported since API version 9. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { bundleManager } from '@kit.AbilityKit';

#### AbilityInfo

**System capability**: SystemCapability.BundleManager.BundleFramework.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| bundleName | string | Yes | No | 
Bundle name.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| moduleName | string | Yes | No | 

Module name to which the ability belongs.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| name | string | Yes | No | 

Ability name.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| label | string | Yes | No | 

Resource descriptor of the ability name visible to users. It corresponds to the **label** field under **abilities** in the [module.json5](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/module-configuration-file) file.

Note: Starting from API version 20, if [bundleManager.getAbilityInfo](../../../both-models-recommended/ohos-bundle-bundlemanager-bundle-management-module/document.md#bundlemanagergetabilityinfo20) is used to obtain ability information, this field is the ability name visible to users.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| labelId | number | Yes | No | 

Resource ID of the ability label. It is automatically generated during compilation and build based on the label configured in **abilities** of the application.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| description | string | Yes | No | 

Ability description, which describes the content and functions of the current ability. It corresponds to the **description** field under **abilities** in the [module.json5](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/module-configuration-file) file.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| descriptionId | number | Yes | No | 

Resource ID of the ability description. It is automatically generated during compilation and build based on the description configured in **abilities** of the application.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| icon | string | Yes | No | 

Resource descriptor of the ability icon. It corresponds to the **icon** field under **abilities** in the [module.json5](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/module-configuration-file) file.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| iconId | number | Yes | No | 

Resource ID of the ability icon. It is automatically generated during compilation and build based on the icon configured in **abilities** of the application.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| process | string | Yes | No | 

Process name of the ability.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| exported | boolean | Yes | No | 

Whether the ability can be launched by other applications. **true** if the ability can be launched by other applications, **false** otherwise.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| type | [bundleManager.AbilityType](../../../both-models-recommended/ohos-bundle-bundlemanager-bundle-management-module/document.md#abilitytype) | Yes | No | 

Ability type.

**Model restriction**: This API can be used only in the FA model.

 |
| orientation | [bundleManager.DisplayOrientation](../../../both-models-recommended/ohos-bundle-bundlemanager-bundle-management-module/document.md#displayorientation) | Yes | No | 

Ability display orientation. It is derived from the **orientation** field under **abilities** in the [module.json5](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/module-configuration-file) file. If **orientation** in the file is set to an enumerated value, this property is a non-zero value. For details about the available values, see [displayOrientation](../../../both-models-recommended/ohos-bundle-bundlemanager-bundle-management-module/document.md#displayorientation). If **orientation** in the file is set to a resource index, the value of this property is **0**.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| launchType | [bundleManager.LaunchType](../../../both-models-recommended/ohos-bundle-bundlemanager-bundle-management-module/document.md#launchtype) | Yes | No | 

Ability launch mode, that is, whether it can be started in multiton mode. For details, see [LaunchType](../../../both-models-recommended/ohos-bundle-bundlemanager-bundle-management-module/document.md#launchtype).

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| permissions | Array<string> | Yes | No | 

Array of permissions that other applications must request to start or access this ability. The system checks whether the caller has these permissions only if the **exported** property in **AbilityInfo** is **true** (meaning that the ability allows itself to be started by other applications).

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| readPermission | string | Yes | No | 

Permission required for reading the ability data.

**Model restriction**: This API can be used only in the FA model.

 |
| writePermission | string | Yes | No | 

Permission required for writing data to the ability.

**Model restriction**: This API can be used only in the FA model.

 |
| uri | string | Yes | No | 

URI of the ability.

**Model restriction**: This API can be used only in the FA model.

 |
| deviceTypes | Array<string> | Yes | No | 

Device types supported by the ability. The value is derived from that of [deviceTypes](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/module-configuration-file#devicetypes) in the **module.json5** file.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| applicationInfo | [ApplicationInfo](../applicationinfo/document.md) | Yes | No | 

Application configuration information .

This field is not returned when the [getBundleInfoForSelf](../../../both-models-recommended/ohos-bundle-bundlemanager-bundle-management-module/document.md#bundlemanagergetbundleinfoforself) or [getBundleInfo](../../../both-models-recommended/ohos-bundle-bundlemanager-bundle-management-module/document.md#bundlemanagergetbundleinfo14) is used to obtain ability information. You can obtain the related information by obtaining the [bundleInfo](../bundleinfo/document.md#bundleinfo-1).appInfo object.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| metadata | Array<[Metadata](../metadata/document.md)\> | Yes | No | 

Metadata of the ability. You can configure the system-defined parameters to use the capabilities provided by the system, for example, [shortcuts](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/module-configuration-file#shortcuts) and [window metadata configuration](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/window-config-m). You can also customize the parameters and call [getBundleInfoForSelf](../../../both-models-recommended/ohos-bundle-bundlemanager-bundle-management-module/document.md#bundlemanagergetbundleinfoforself) to obtain the parameters by passing **GET\_BUNDLE\_INFO\_WITH\_HAP\_MODULE**, **GET\_BUNDLE\_INFO\_WITH\_ABILITY**, and **GET\_BUNDLE\_INFO\_WITH\_METADATA** to **bundleFlags**.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| enabled | boolean | Yes | No | 

Whether the ability is available, that is, whether it can be started or queried. **true** if available, **false** otherwise. If the ability is unavailable, you must call [getAbilityInfo](../../../both-models-recommended/ohos-bundle-bundlemanager-bundle-management-module/document.md#bundlemanagergetabilityinfo20) with **AbilityFlag** set to **GET\_ABILITY\_INFO\_WITH\_DISABLE** to query the ability.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| supportWindowModes | Array<[bundleManager.SupportWindowMode](../../../both-models-recommended/ohos-bundle-bundlemanager-bundle-management-module/document.md#supportwindowmode)\> | Yes | No | 

Window modes supported by the ability.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| windowSize | [WindowSize](#windowsize) | Yes | No | 

Window size.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| excludeFromDock12+ | boolean | Yes | No | 

Whether the ability icon can be hidden in the dock area. **true** if the ability icon can be hidden in the dock area, **false** otherwise.

Note: This field does not take effect.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| skills12+ | Array<[Skill](../skill/document.md)\> | Yes | No | 

Skills information of the ability. It represents the feature set of [wants](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/want-overview) that can be received by the UIAbility or ExtensionAbility.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| appIndex12+ | number | Yes | No | Index of an application clone. It takes effect only for [application clones](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-clone). |
| orientationId14+ | number | Yes | No | 

Resource ID of the ability display mode. It is derived from the **orientation** field under **abilities** in the [module.json5](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/module-configuration-file) file. If the **orientation** field in the file is set to an enumerated value, **orientationId** is **0**. If the **orientation** field is set to a resource index, **orientationId** is a non-zero value, which is the resource ID generated during building. If **orientationId** is set to a value other than **0**, the current display mode is customized, and this ID must be used to obtain the corresponding resource from the resource manager module. If **orientationId** is set to **0**, no resource is configured.

**Atomic service API**: This API can be used in atomic services since API version 14.

 |

#### WindowSize

Describes the window size.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.BundleManager.BundleFramework.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| maxWindowRatio | number | Yes | No | Maximum aspect ratio of the window in free window mode. The value ranges from 0 to 1. An example value is 0.12. |
| minWindowRatio | number | Yes | No | Minimum aspect ratio of the window in free window mode. The value ranges from 0 to 1. An example value is 0.5. |
| maxWindowWidth | number | Yes | No | Maximum width of the window in free window mode. The unit is vp. |
| minWindowWidth | number | Yes | No | Minimum width of the window in free window mode. The unit is vp. |
| maxWindowHeight | number | Yes | No | Maximum height of the window in free window mode. The unit is vp. |
| minWindowHeight | number | Yes | No | Minimum height of the window in free window mode. The unit is vp. |
