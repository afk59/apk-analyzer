# @ohos.bundle.bundleManager (Bundle Management Module)

The module provides APIs for obtaining application information, including [bundle information](../../dependent-elements-and-definitions/bundlemanager/bundleinfo/document.md), [application information](../../dependent-elements-and-definitions/bundlemanager/applicationinfo/document.md), [ability information](../../dependent-elements-and-definitions/bundlemanager/abilityinfo/document.md) (information about a UIAbility), and [ExtensionAbility information](../../dependent-elements-and-definitions/bundlemanager/extensionabilityinfo/document.md).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/KUS7jrw5TKGrx0CIWk0uFw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062208Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CE36CABCDEB79BE38723E91B07F6F0517F28C45A6960C4BEA4491A06A1A659BD)

The initial APIs of this module are supported since API version 9. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { bundleManager } from '@kit.AbilityKit';

#### BundleFlag

Enumerates the bundle flags, which indicate the type of bundle information to obtain.

**System capability**: SystemCapability.BundleManager.BundleFramework.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| GET\_BUNDLE\_INFO\_DEFAULT | 0x00000000 | 
Used to obtain the default bundle information. The obtained information does not contain information about the signature, application, HAP module, ability, ExtensionAbility, or permission.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| GET\_BUNDLE\_INFO\_WITH\_APPLICATION | 0x00000001 | 

Used to obtain the bundle information with application information. The obtained information does not contain information about the signature, HAP module, ability, ExtensionAbility, or permission.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| GET\_BUNDLE\_INFO\_WITH\_HAP\_MODULE | 0x00000002 | 

Used to obtain the bundle information with HAP module information. The obtained information does not contain information about the signature, application, ability, ExtensionAbility, or permission.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| GET\_BUNDLE\_INFO\_WITH\_ABILITY | 0x00000004 | 

Used to obtain the bundle information with ability information. The obtained information does not contain information about the signature, application, ExtensionAbility, or permission. It must be used together with **GET\_BUNDLE\_INFO\_WITH\_HAP\_MODULE**.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| GET\_BUNDLE\_INFO\_WITH\_EXTENSION\_ABILITY | 0x00000008 | 

Used to obtain the bundle information with ExtensionAbility information. The obtained information does not contain information about the signature, application, ability, or permission. It must be used together with **GET\_BUNDLE\_INFO\_WITH\_HAP\_MODULE**.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| GET\_BUNDLE\_INFO\_WITH\_REQUESTED\_PERMISSION | 0x00000010 | 

Used to obtain the bundle information with permission information. The obtained information does not contain information about the signature, application, HAP module, ability, or ExtensionAbility.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| GET\_BUNDLE\_INFO\_WITH\_METADATA | 0x00000020 | 

Used to obtain the metadata contained in the application, module, ability, or ExtensionAbility information. It must be used together with **GET\_BUNDLE\_INFO\_WITH\_APPLICATION**, **GET\_BUNDLE\_INFO\_WITH\_HAP\_MODULE**, **GET\_BUNDLE\_INFO\_WITH\_ABILITY**, and **GET\_BUNDLE\_INFO\_WITH\_EXTENSION\_ABILITY**.

\- To obtain the metadata contained in the application information, it must be used together with **GET\_BUNDLE\_INFO\_WITH\_APPLICATION**.

\- To obtain the metadata contained in the module information, it must be used together with **GET\_BUNDLE\_INFO\_WITH\_HAP\_MODULE**.

\- To obtain the metadata contained in the ability information, it must be used together with **GET\_BUNDLE\_INFO\_WITH\_HAP\_MODULE** and **GET\_BUNDLE\_INFO\_WITH\_ABILITY**.

\- To obtain the metadata contained in the ExtensionAbility information, it must be used together with **GET\_BUNDLE\_INFO\_WITH\_HAP\_MODULE** and **GET\_BUNDLE\_INFO\_WITH\_EXTENSION\_ABILITY**.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| GET\_BUNDLE\_INFO\_WITH\_DISABLE | 0x00000040 | 

Used to obtain the information about disabled bundles and abilities of a bundle. The obtained information does not contain information about the signature, application, HAP module, ability, ExtensionAbility, or permission.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| GET\_BUNDLE\_INFO\_WITH\_SIGNATURE\_INFO | 0x00000080 | 

Used to obtain the bundle information with signature information. The obtained information does not contain information about the application, HAP module, ability, ExtensionAbility, or permission.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| GET\_BUNDLE\_INFO\_WITH\_MENU11+ | 0x00000100 | 

Used to obtain the bundle information with the file context menu configuration. It must be used together with **GET\_BUNDLE\_INFO\_WITH\_HAP\_MODULE**.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| GET\_BUNDLE\_INFO\_WITH\_ROUTER\_MAP12+ | 0x00000200 | 

Used to obtain the bundle information with the router map. It must be used together with **GET\_BUNDLE\_INFO\_WITH\_HAP\_MODULE**.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| GET\_BUNDLE\_INFO\_WITH\_SKILL12+ | 0x00000800 | 

Used to obtain the bundle information with the skills. It must be used together with **GET\_BUNDLE\_INFO\_WITH\_HAP\_MODULE**, **GET\_BUNDLE\_INFO\_WITH\_ABILITY**, and **GET\_BUNDLE\_INFO\_WITH\_EXTENSION\_ABILITY**.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |

#### ExtensionAbilityType

Enumerates the types of ExtensionAbility components.

**System capability**: SystemCapability.BundleManager.BundleFramework.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| FORM | 0 | 
[FormExtensionAbility](../../../../form-kit/arkts-apis/ohos-app-form-formextensionability-formextensionability/document.md): provides APIs for widget development.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| WORK\_SCHEDULER | 1 | [WorkSchedulerExtensionAbility](../../../../background-tasks-kit/arkts-apis/ohos-workschedulerextensionability-deferred-task-scheduling-callbacks/document.md): provides extended capabilities related to deferred tasks, enabling applications to execute non-real-time tasks when the system is idle. |
| INPUT\_METHOD | 2 | [InputMethodExtensionAbility](../../../../ime-kit/arkts-apis/ohos-inputmethodextensionability-inputmethodextensionability/document.md): provides extended capabilities related to input method applications. |
| ACCESSIBILITY | 4 | [AccessibilityExtensionAbility](../../../../accessibility-kit/arkts-apis/ohos-application-accessibilityextensionability-accessibilityextensionability/document.md): provides extended capabilities related to accessibility services, supporting access and operation of the foreground UI. |
| BACKUP | 9 | [BackupExtensionAbility](../../../../core-file-kit/arkts-apis/ohos-application-backupextensionability-backupextensionability/document.md): provides extended capabilities for data backup and restore. |
| ENTERPRISE\_ADMIN | 11 | [EnterpriseAdminExtensionAbility](../../../../../system/basic-functions/mdm-kit/arkts-apis/ohos-enterprise-enterpriseadminextensionability-enterpriseadminextensionability/document.md): provides extended capabilities for processing enterprise management events, such as application installation events on devices and events indicating too many incorrect screen-lock password attempts. |
| SHARE10+ | 16 | [ShareExtensionAbility](../../stage-model/ohos-app-ability-shareextensionability-extensionability-for-share-detail-page-in/document.md): provides sharing service templates based on the UIExtensionAbility. |
| DRIVER10+ | 18 | [DriverExtensionAbility](../../../../../system/hardware/driver-development-kit/arkts-api/ohos-app-ability-driverextensionability-driver-extension-ability/document.md): provides extended capabilities for the peripheral driver. When an application configures an ExtensionAbility of the driver type, it is recognized as a driver application. Driver applications do not differentiate between users during installation, uninstall, and recovery. Moreover, when a new user account is created, the existing driver applications on the device are installed for that user. For example, when a sub-user is created, the driver applications already installed by the primary user is automatically installed for the sub-user. If a driver application is uninstalled for a sub-user, it is also removed for the primary user. |
| ACTION10+ | 19 | [ActionExtensionAbility](../../stage-model/ohos-app-ability-actionextensionability-extensionability-for-custom-actions/document.md): provides custom action service templates based on the UIExtensionAbility. |
| EMBEDDED\_UI12+ | 21 | [EmbeddedUIExtensionAbility](../../stage-model/ohos-app-ability-embeddeduiextensionability-extensionability-for-cross-process-u/document.md): provides extended capabilities for the embeddable UI across process. |
| INSIGHT\_INTENT\_UI12+ | 22 | InsightIntentUIExtensionAbility: provides extended capabilities that enable applications to be called by Celia intents so as to be displayed in windows. |
| FENCE18+ | 24 | [FenceExtensionAbility](../../../../../application-services/location-kit/arkts-apis/ohos-app-ability-fenceextensionability-fenceextensionability/document.md): provides geofence-related capabilities. It inherits from ExtensionAbility. |
| ASSET\_ACCELERATION18+ | 26 | AssetAccelerationExtensionAbility: provides extended capabilities of pre-downloading background resources when the device is idle. |
| FORM\_EDIT18+ | 27 | [FormEditExtensionAbility](../../../../form-kit/arkts-apis/ohos-app-form-formeditextensionability-formeditextensionability/document.md): provides extended capabilities related to widget editing. It inherits from UIExtensionAbility. |
| DISTRIBUTED20+ | 28 | [DistributedExtensionAbility](../../../../../system/network/distributed-service-kit/arkts-apis/ohos-application-distributedextensionability-distributed-extension/document.md): provides extended capabilities for distributed services and lifecycle callbacks for creation, destruction, and connection of the DistributedExtensionAbility. |
| APP\_SERVICE20+ | 29 | [AppServiceExtensionAbility](../../stage-model/ohos-app-ability-appserviceextensionability-extensionability-for-application-bac/document.md): provides backend service capabilities for enterprise common applications. |
| LIVE\_FORM20+ | 30 | 

[LiveFormExtensionAbility](../../../../form-kit/arkts-apis/ohos-app-form-liveformextensionability-liveformextensionability/document.md): provides extended capabilities for interactive widgets, and provides lifecycle callbacks for creating and destroying interactive widgets.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |
| WEB\_NATIVE\_MESSAGING21+ | 32 | [WebNativeMessagingExtensionAbility](../../../../arkweb/arkts-api/ohos-web-webnativemessagingextensionability-web-native-messaging-extension-abili/document.md): provides extended capabilities for web native message communication. |
| FAULT\_LOG21+ | 33 | [FaultLogExtensionAbility](../../../../../system/debugging-tools/performance-analysis-kit/arkts-api/ohos-hiviewdfx-faultlogextensionability-delayed-fault-notification/document.md): provides extended capabilities for delayed fault notifications. |
| NOTIFICATION\_SUBSCRIBER22+ | 34 | [NotificationSubscriberExtensionAbility](../../../../../application-services/notification-kit/arkts-apis/ohos-application-notificationsubscriberextensionability-extensionability-for-not/document.md): provides extended capabilities for notification subscription. |
| CRYPTO22+ | 35 | [CryptoExtensionAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/huks-extension-ability-support-dev): provides extended capabilities for external key management. |
| UNSPECIFIED | 255 | The ability type is not specified. |
| CALLER\_INFO\_QUERY19+ | 25 | [CallerInfoQueryExtensionAbility](../../../../../application-services/call-service-kit/arkts-api/callerinfoqueryextensionability-extended-ability-for-querying-incoming-and-outgo/document.md): provides the capability of querying incoming and outgoing call information. |

#### PermissionGrantState

Enumerates the permission grant states.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.BundleManager.BundleFramework.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| PERMISSION\_DENIED | \-1 | Permission denied. |
| PERMISSION\_GRANTED | 0 | Permission granted. |

#### SupportWindowMode

Enumerates the window modes supported by the ability.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.BundleManager.BundleFramework.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| FULL\_SCREEN | 0 | A window in full-screen mode is supported. |
| SPLIT | 1 | A window in split-screen mode is supported. |
| FLOATING | 2 | A floating window is supported. |

#### LaunchType

Enumerates the [launch types](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-launch-type) of the UIAbility.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.BundleManager.BundleFramework.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| SINGLETON | 0 | The UIAbility can have only one instance. |
| MULTITON | 1 | The UIAbility can have multiple instances. |
| SPECIFIED | 2 | The UIAbility can have one or multiple instances, depending on the internal service of the ability. |

#### AbilityType

Enumerates the types of ability components.

**Model restriction**: This API can be used only in the FA model.

**System capability**: SystemCapability.BundleManager.BundleFramework.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| PAGE | 1 | Ability that has the UI. FA developed using the Page template to provide the capability of interacting with users. |
| SERVICE | 2 | Ability of the background service type, without the UI. [PA (ParticleAbility)](../../fa-model/ohos-ability-particleability-particleability-module/document.md) developed using the Service template to provide the capability of running tasks in the background, such as downloading files or playing music in the background. |
| DATA | 3 | [PA (ParticleAbility)](../../fa-model/ohos-ability-particleability-particleability-module/document.md) developed using the Data template to provide unified data access for external systems. |

#### DisplayOrientation

Enumerates the display orientations of the ability. It is applicable only to [PageAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/pageability-overview) in the FA model.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.BundleManager.BundleFramework.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| UNSPECIFIED | 0 | 
Unspecified. The orientation is determined by the system.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| LANDSCAPE | 1 | 

Landscape.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| PORTRAIT | 2 | 

Portrait.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| FOLLOW\_RECENT | 3 | 

The last display orientation is used.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| LANDSCAPE\_INVERTED | 4 | 

Reverse landscape.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| PORTRAIT\_INVERTED | 5 | 

Reverse portrait.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| AUTO\_ROTATION | 6 | 

Automatically rotates when the sensor changes to landscape or portrait mode.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| AUTO\_ROTATION\_LANDSCAPE | 7 | 

Automatically rotates when the sensor changes to landscape mode.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| AUTO\_ROTATION\_PORTRAIT | 8 | 

Automatically rotates when the sensor changes to portrait mode.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| AUTO\_ROTATION\_RESTRICTED | 9 | 

Switched-determined auto rotation.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| AUTO\_ROTATION\_LANDSCAPE\_RESTRICTED | 10 | 

Switched-determined auto rotation in the horizontal direction.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| AUTO\_ROTATION\_PORTRAIT\_RESTRICTED | 11 | 

Switched-determined auto rotation in the vertical direction.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| LOCKED | 12 | 

Locked.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| AUTO\_ROTATION\_UNSPECIFIED12+ | 13 | 

Auto rotation controlled by the switch and determined by the system.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| FOLLOW\_DESKTOP12+ | 14 | 

Following the orientation of the home screen.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |

#### CompatiblePolicy10+

Defines the version compatibility type of the dynamic shared library.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.BundleManager.BundleFramework.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| BACKWARD\_COMPATIBILITY | 1 | The shared library is backward compatible. |

#### ModuleType

Enumerates the module types.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.BundleManager.BundleFramework.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| ENTRY | 1 | Main module of and entry to the application, providing the basic application functionality. |
| FEATURE | 2 | Dynamic feature module of the application, extending the application functionality. This type of HAP can be installed based on user needs and device types. |
| SHARED | 3 | [Dynamic shared library](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/in-app-hsp) of the application. |

#### BundleType

Enumerates the bundle types.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.BundleManager.BundleFramework.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| APP | 0 | The bundle is an application. |
| ATOMIC\_SERVICE | 1 | The bundle is an atomic service. |

#### MultiAppModeType12+

Enumerates the types of the multi-app mode.

**System capability**: SystemCapability.BundleManager.BundleFramework.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| UNSPECIFIED | 0 | Unspecified. It is the default value of [multiAppMode](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-configuration-file#multiappmode). |
| MULTI\_INSTANCE | 1 | [Multi-instance mode](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/multiinstance). A resident process does not support this value. |
| APP\_CLONE | 2 | [App clone mode](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-clone) |

#### AbilityFlag20+

Enumerates the ability flags, which indicate the type of ability information to obtain.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.BundleManager.BundleFramework.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| GET\_ABILITY\_INFO\_DEFAULT | 0x00000000 | Used to obtain the default [ability information](../../dependent-elements-and-definitions/bundlemanager/abilityinfo/document.md), which does not contain permissions, metadata, or ability information of disabled abilities. |
| GET\_ABILITY\_INFO\_WITH\_PERMISSION | 0x00000001 | Used to obtain the ability information containing permissions. |
| GET\_ABILITY\_INFO\_WITH\_APPLICATION | 0x00000002 | Used to obtain the ability information containing application information. |
| GET\_ABILITY\_INFO\_WITH\_METADATA | 0x00000004 | Used to obtain the ability information containing metadata. |
| GET\_ABILITY\_INFO\_WITH\_DISABLE | 0x00000008 | Used to obtain the ability information of disabled abilities. |
| GET\_ABILITY\_INFO\_ONLY\_SYSTEM\_APP | 0x00000010 | Used to obtain the ability information of system applications. |
| GET\_ABILITY\_INFO\_WITH\_APP\_LINKING | 0x00000040 | Used to obtain the ability information that passes [domain name verification](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-linking-startup#section4452103365213). |
| GET\_ABILITY\_INFO\_WITH\_SKILL | 0x00000080 | Used to obtain the ability information containing skills. |

#### bundleManager.getBundleInfoForSelf

getBundleInfoForSelf(bundleFlags: number): Promise<BundleInfo>

Obtains the bundle information of the current application based on the given bundle flags. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.BundleManager.BundleFramework.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| [bundleFlags](#bundleflag) | number | Yes | Type of the bundle information to obtain. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[BundleInfo](../../dependent-elements-and-definitions/bundlemanager/bundleinfo/document.md)\> | Promise used to return the bundle information. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**Example**

// Obtain the bundle information, which contains the application information including a metadata array.
import { bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let bundleFlags =
  bundleManager.BundleFlag.GET\_BUNDLE\_INFO\_WITH\_APPLICATION | bundleManager.BundleFlag.GET\_BUNDLE\_INFO\_WITH\_METADATA;

try {
  bundleManager.getBundleInfoForSelf(bundleFlags).then((data) => {
    hilog.info(0x0000, 'testTag', 'getBundleInfoForSelf successfully. Data: %{public}s', JSON.stringify(data));
  }).catch((err: BusinessError) => {
    hilog.error(0x0000, 'testTag', 'getBundleInfoForSelf failed. Cause: %{public}s', err.message);
  });
} catch (err) {
  let message = (err as BusinessError).message;
  hilog.error(0x0000, 'testTag', 'getBundleInfoForSelf failed: %{public}s', message);
}

#### bundleManager.getBundleInfoForSelf

getBundleInfoForSelf(bundleFlags: number, callback: AsyncCallback<BundleInfo>): void

Obtains the bundle information of the current application based on the given bundle flags. This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.BundleManager.BundleFramework.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| [bundleFlags](#bundleflag) | number | Yes | Type of the bundle information to obtain. |
| callback | AsyncCallback<[BundleInfo](../../dependent-elements-and-definitions/bundlemanager/bundleinfo/document.md)\> | Yes | [Callback](../../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#asynccallback) used to return the result. If the information is successfully obtained, **err** is **null** and **data** is the bundle information of the current application. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**Example**

// Obtain the bundle information, which contains the ability information including permissions.
import { bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let bundleFlags =
  bundleManager.BundleFlag.GET\_BUNDLE\_INFO\_WITH\_HAP\_MODULE | bundleManager.BundleFlag.GET\_BUNDLE\_INFO\_WITH\_ABILITY |
  bundleManager.BundleFlag.GET\_BUNDLE\_INFO\_WITH\_REQUESTED\_PERMISSION;

try {
  bundleManager.getBundleInfoForSelf(bundleFlags, (err, data) => {
    if (err) {
      hilog.error(0x0000, 'testTag', 'getBundleInfoForSelf failed: %{public}s', err.message);
    } else {
      hilog.info(0x0000, 'testTag', 'getBundleInfoForSelf successfully: %{public}s', JSON.stringify(data));
    }
  });
} catch (err) {
  let message = (err as BusinessError).message;
  hilog.error(0x0000, 'testTag', 'getBundleInfoForSelf failed: %{public}s', message);
}

#### bundleManager.getProfileByAbility

getProfileByAbility(moduleName: string, abilityName: string, metadataName: string, callback: AsyncCallback<Array<string>>): void

Obtains the JSON string array of the current application's configuration file based on the given module name, ability name, and metadata name (name configured under **metadata** in [abilities](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/module-configuration-file#abilities) of the **module.json5** file). This API uses an asynchronous callback to return the result.

NOTE

If the profile uses the resource reference format, the return value retains this format (for example, **$string:res\_id**). You can obtain the referenced resources through related APIs of the [resource manager module](../../../../localization-kit/arkts-apis/ohos-resourcemanager-resource-management/document.md).

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.BundleManager.BundleFramework.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| moduleName | string | Yes | Module name. |
| abilityName | string | Yes | Name of the UIAbility component. |
| metadataName | string | Yes | [Metadata name](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/module-configuration-file#metadata) of the UIAbility component, that is, **name** of the **metadata** tag under [abilities](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/module-configuration-file#abilities) in the **module.json5** file. |
| callback | AsyncCallback<Array<string>> | Yes | [Callback](../../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#asynccallback) used to return the result. If the information is successfully obtained, **err** is **null** and **data** is **Array<string>**. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Bundle Error Codes](../../../error-codes/bundle-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 17700002 | The specified moduleName is not existed. |
| 17700003 | The specified abilityName is not existed. |
| 17700024 | Failed to get the profile because there is no profile in the HAP. |
| 17700029 | The specified ability is disabled. |

**Example**

import { bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let moduleName = 'entry';
let abilityName = 'EntryAbility';
let metadataName = 'ability\_metadata';

try {
  bundleManager.getProfileByAbility(moduleName, abilityName, metadataName, (err, data) => {
    if (err) {
      hilog.error(0x0000, 'testTag', 'getProfileByAbility failed. Cause: %{public}s', err.message);
    } else {
      hilog.info(0x0000, 'testTag', 'getProfileByAbility successfully: %{public}s', JSON.stringify(data));
    }
  });
} catch (err) {
  let message = (err as BusinessError).message;
  hilog.error(0x0000, 'testTag', 'getProfileByAbility failed. Cause: %{public}s', message);
}

#### bundleManager.getProfileByAbility

getProfileByAbility(moduleName: string, abilityName: string, metadataName?: string): Promise<Array<string>>

Obtains the JSON string array of the current application's configuration file based on the given module name, ability name, and metadata name (name configured under **metadata** in [abilities](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/module-configuration-file#abilities) of the **module.json5** file). This API uses a promise to return the result.

NOTE

If the profile uses the resource reference format, the return value retains this format (for example, **$string:res\_id**). You can obtain the referenced resources through related APIs of the [resource manager module](../../../../localization-kit/arkts-apis/ohos-resourcemanager-resource-management/document.md).

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.BundleManager.BundleFramework.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| moduleName | string | Yes | Module name. |
| abilityName | string | Yes | Name of the UIAbility component. |
| metadataName | string | No | Metadata name of the UIAbility component, that is, **name** of the **metadata** tag under [abilities](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/module-configuration-file#abilities) in the **module.json5** file. The default value is null. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<string>> | Promise used to return the array of JSON strings obtained. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Bundle Error Codes](../../../error-codes/bundle-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 17700002 | The specified moduleName is not existed. |
| 17700003 | The specified abilityName is not existed. |
| 17700024 | Failed to get the profile because there is no profile in the HAP. |
| 17700029 | The specified ability is disabled. |

**Example**

import { bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let moduleName = 'entry';
let abilityName = 'EntryAbility';

try {
  // Obtain the JSON string array of the configuration file based on the module name and ability name.
  bundleManager.getProfileByAbility(moduleName, abilityName).then((data) => {
    hilog.info(0x0000, 'testTag', 'getProfileByAbility successfully. Data: %{public}s', JSON.stringify(data));
  }).catch((err: BusinessError) => {
    hilog.error(0x0000, 'testTag', 'getProfileByAbility failed. Cause: %{public}s', err.message);
  });
} catch (err) {
  let message = (err as BusinessError).message;
  hilog.error(0x0000, 'testTag', 'getProfileByAbility failed. Cause: %{public}s', message);
}

import { bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let moduleName = 'entry';
let abilityName = 'EntryAbility';
let metadataName = 'ability\_metadata';

try {
  // Obtain the JSON string array of the current application's configuration file based on the module name, ability name, and metadata name.
  bundleManager.getProfileByAbility(moduleName, abilityName, metadataName).then((data) => {
    hilog.info(0x0000, 'testTag', 'getProfileByAbility successfully. Data: %{public}s', JSON.stringify(data));
  }).catch((err: BusinessError) => {
    hilog.error(0x0000, 'testTag', 'getProfileByAbility failed. Cause: %{public}s', err.message);
  });
} catch (err) {
  let message = (err as BusinessError).message;
  hilog.error(0x0000, 'testTag', 'getProfileByAbility failed. Cause: %{public}s', message);
}

#### bundleManager.getProfileByAbilitySync10+

getProfileByAbilitySync(moduleName: string, abilityName: string, metadataName?: string): Array<string>

Obtains the JSON string array of the current application's configuration file based on the given module name, ability name, and metadata name (name configured in [metadata](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/module-configuration-file#metadata) of the **module.json5** file). This API returns the result synchronously. The result value is a string array.

If the profile uses the resource reference format, the return value retains this format (for example, **$string:res\_id**). You can obtain the referenced resources through related APIs of the [resource manager module](../../../../localization-kit/arkts-apis/ohos-resourcemanager-resource-management/document.md).

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.BundleManager.BundleFramework.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| moduleName | string | Yes | Module name. |
| abilityName | string | Yes | Name of the UIAbility component. |
| metadataName | string | No | Metadata name of the UIAbility component, that is, **name** of the **metadata** tag under [abilities](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/module-configuration-file#abilities) in the **module.json5** file. The default value is null. |

**Return value**

| Type | Description |
| :-- | :-- |
| Array<string> | An array of JSON strings. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Bundle Error Codes](../../../error-codes/bundle-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 17700002 | The specified moduleName is not existed. |
| 17700003 | The specified abilityName is not existed. |
| 17700024 | Failed to get the profile because there is no profile in the HAP. |
| 17700029 | The specified ability is disabled. |

**Example**

import { bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let moduleName = 'entry';
let abilityName = 'EntryAbility';

try {
  // Obtain the JSON string array of the configuration file based on the module name and ability name.
  let data = bundleManager.getProfileByAbilitySync(moduleName, abilityName);
  hilog.info(0x0000, 'testTag', 'getProfileByAbilitySync successfully. Data: %{public}s', JSON.stringify(data));
} catch (err) {
  let message = (err as BusinessError).message;
  hilog.error(0x0000, 'testTag', 'getProfileByAbilitySync failed. Cause: %{public}s', message);
}

import { bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let moduleName: string = 'entry';
let abilityName: string = 'EntryAbility';
let metadataName: string = 'ability\_metadata';

try {
  // Obtain the JSON string array of the configuration file based on the module name, ability name, and metadata name.
  let data = bundleManager.getProfileByAbilitySync(moduleName, abilityName, metadataName);
  hilog.info(0x0000, 'testTag', 'getProfileByAbilitySync successfully. Data: %{public}s', JSON.stringify(data));
} catch (err) {
  let message = (err as BusinessError).message;
  hilog.error(0x0000, 'testTag', 'getProfileByAbilitySync failed. Cause: %{public}s', message);
}

#### bundleManager.getProfileByExtensionAbility

getProfileByExtensionAbility(moduleName: string, extensionAbilityName: string, metadataName: string, callback: AsyncCallback<Array<string>>): void

Obtains the JSON string array of the current application's configuration file based on the given module name, ExtensionAbility name, and metadata name (name configured in [metadata](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/module-configuration-file#metadata) of the **module.json5** file). This API uses an asynchronous callback to return the result.

If the profile uses the resource reference format, the return value retains this format (for example, **$string:res\_id**). You can obtain the referenced resources through related APIs of the [resource manager module](../../../../localization-kit/arkts-apis/ohos-resourcemanager-resource-management/document.md).

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.BundleManager.BundleFramework.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| moduleName | string | Yes | Module name. |
| extensionAbilityName | string | Yes | Name of the ExtensionAbility component. |
| metadataName | string | Yes | Metadata name of the ExtensionAbility component, that is, **name** of the **metadata** tag under [extensionAbilities](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/module-configuration-file#extensionabilities) in the **module.json5** file. |
| callback | AsyncCallback<Array<string>> | Yes | [Callback](../../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#asynccallback) used to return the result. If the information is successfully obtained, **err** is **null** and **data** is **Array<string>**. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Bundle Error Codes](../../../error-codes/bundle-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 17700002 | The specified moduleName is not existed. |
| 17700003 | The specified extensionAbilityName not existed. |
| 17700024 | Failed to get the profile because there is no profile in the HAP. |

**Example**

import { bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let moduleName = 'entry';
let extensionAbilityName = 'com.example.myapplication.extension';
let metadataName = 'ability\_metadata';

try {
  bundleManager.getProfileByExtensionAbility(moduleName, extensionAbilityName, metadataName, (err, data) => {
    if (err) {
      hilog.error(0x0000, 'testTag', 'getProfileByExtensionAbility failed: %{public}s', err.message);
    } else {
      hilog.info(0x0000, 'testTag', 'getProfileByExtensionAbility successfully: %{public}s', JSON.stringify(data));
    }
  });
} catch (err) {
  let message = (err as BusinessError).message;
  hilog.error(0x0000, 'testTag', 'getProfileByExtensionAbility failed: %{public}s', message);
}

#### bundleManager.getProfileByExtensionAbility

getProfileByExtensionAbility(moduleName: string, extensionAbilityName: string, metadataName?: string): Promise<Array<string>>

Obtains the JSON string array of the current application's configuration file based on the given module name, ExtensionAbility name, and metadata name (name configured in [metadata](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/module-configuration-file#metadata) of the **module.json5** file). This API uses a promise to return the result.

If the profile uses the resource reference format, the return value retains this format (for example, **$string:res\_id**). You can obtain the referenced resources through related APIs of the [resource manager module](../../../../localization-kit/arkts-apis/ohos-resourcemanager-resource-management/document.md).

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.BundleManager.BundleFramework.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| moduleName | string | Yes | Module name. |
| extensionAbilityName | string | Yes | Name of the ExtensionAbility component. |
| metadataName | string | No | Metadata name of the ExtensionAbility component, that is, **name** of the **metadata** tag under [extensionAbilities](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/module-configuration-file#extensionabilities) in the **module.json5** file. The default value is null. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<string>> | Promise used to return the array of JSON strings obtained. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Bundle Error Codes](../../../error-codes/bundle-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 17700002 | The specified moduleName is not existed. |
| 17700003 | The specified extensionAbilityName not existed. |
| 17700024 | Failed to get the profile because there is no profile in the HAP. |

**Example**

import { bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let moduleName = 'entry';
let extensionAbilityName = 'com.example.myapplication.extension';
let metadataName = 'ability\_metadata';

try {
  bundleManager.getProfileByExtensionAbility(moduleName, extensionAbilityName).then((data) => {
    hilog.info(0x0000, 'testTag', 'getProfileByExtensionAbility successfully. Data: %{public}s', JSON.stringify(data));
  }).catch((err: BusinessError) => {
    hilog.error(0x0000, 'testTag', 'getProfileByExtensionAbility failed. Cause: %{public}s', err.message);
  });
} catch (err) {
  let message = (err as BusinessError).message;
  hilog.error(0x0000, 'testTag', 'getProfileByExtensionAbility failed. Cause: %{public}s', message);
}

try {
  bundleManager.getProfileByExtensionAbility(moduleName, extensionAbilityName, metadataName).then((data) => {
    hilog.info(0x0000, 'testTag', 'getProfileByExtensionAbility successfully. Data: %{public}s', JSON.stringify(data));
  }).catch((err: BusinessError) => {
    hilog.error(0x0000, 'testTag', 'getProfileByExtensionAbility failed. Cause: %{public}s', err.message);
  });
} catch (err) {
  let message = (err as BusinessError).message;
  hilog.error(0x0000, 'testTag', 'getProfileByExtensionAbility failed. Cause: %{public}s', message);
}

#### bundleManager.getProfileByExtensionAbilitySync10+

getProfileByExtensionAbilitySync(moduleName: string, extensionAbilityName: string, metadataName?: string): Array<string>

Obtains the JSON string array of the current application's configuration file based on the given module name, ExtensionAbility name, and metadata name (name configured in [metadata](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/module-configuration-file#metadata) of the **module.json5** file). This API returns the result synchronously. The result value is a string array.

If the profile uses the resource reference format, the return value retains this format (for example, **$string:res\_id**). You can obtain the referenced resources through related APIs of the [resource manager module](../../../../localization-kit/arkts-apis/ohos-resourcemanager-resource-management/document.md).

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.BundleManager.BundleFramework.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| moduleName | string | Yes | Module name. |
| extensionAbilityName | string | Yes | Name of the ExtensionAbility component. |
| metadataName | string | No | Metadata name of the ExtensionAbility component, that is, **name** of the **metadata** tag under [extensionAbilities](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/module-configuration-file#extensionabilities) in the **module.json5** file. The default value is null. |

**Return value**

| Type | Description |
| :-- | :-- |
| Array<string> | An array of JSON strings. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Bundle Error Codes](../../../error-codes/bundle-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 17700002 | The specified moduleName is not existed. |
| 17700003 | The specified extensionAbilityName not existed. |
| 17700024 | Failed to get the profile because there is no profile in the HAP. |

**Example**

import { bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let moduleName = 'entry';
let extensionAbilityName = 'com.example.myapplication.extension';
let metadataName = 'ability\_metadata';

try {
  let data = bundleManager.getProfileByExtensionAbilitySync(moduleName, extensionAbilityName);
  hilog.info(0x0000, 'testTag', 'getProfileByExtensionAbilitySync successfully. Data: %{public}s',
    JSON.stringify(data));
} catch (err) {
  let message = (err as BusinessError).message;
  hilog.error(0x0000, 'testTag', 'getProfileByExtensionAbilitySync failed. Cause: %{public}s', message);
}

try {
  let data = bundleManager.getProfileByExtensionAbilitySync(moduleName, extensionAbilityName, metadataName);
  hilog.info(0x0000, 'testTag', 'getProfileByExtensionAbilitySync successfully. Data: %{public}s',
    JSON.stringify(data));
} catch (err) {
  let message = (err as BusinessError).message;
  hilog.error(0x0000, 'testTag', 'getProfileByExtensionAbilitySync failed. Cause: %{public}s', message);
}

#### bundleManager.getBundleInfoForSelfSync10+

getBundleInfoForSelfSync(bundleFlags: number): BundleInfo

Obtains the bundle information of the current application based on the given bundle flags. This API returns the result synchronously.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.BundleManager.BundleFramework.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| [bundleFlags](#bundleflag) | number | Yes | Type of the bundle information to obtain. |

**Return value**

| Type | Description |
| :-- | :-- |
| [BundleInfo](../../dependent-elements-and-definitions/bundlemanager/bundleinfo/document.md) | Bundle information obtained. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**Example**

import { bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let bundleFlags = bundleManager.BundleFlag.GET\_BUNDLE\_INFO\_WITH\_REQUESTED\_PERMISSION;

try {
  let data = bundleManager.getBundleInfoForSelfSync(bundleFlags);
  hilog.info(0x0000, 'testTag', 'getBundleInfoForSelfSync successfully: %{public}s', JSON.stringify(data));
} catch (err) {
  let message = (err as BusinessError).message;
  hilog.error(0x0000, 'testTag', 'getBundleInfoForSelfSync failed: %{public}s', message);
}

#### bundleManager.canOpenLink12+

canOpenLink(link: string): boolean

Checks whether the target application can be accessed based on the provided link. The scheme specified in the link must be configured in the **querySchemes** field of the [module.json5](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/module-configuration-file) file.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.BundleManager.BundleFramework.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| link | string | Yes | Link to check. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result for whether the link can be opened. **true** if it can be opened, **false** otherwise. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Bundle Error Codes](../../../error-codes/bundle-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 17700055 | The specified link is invalid. |
| 17700056 | The scheme of the specified link is not in the querySchemes. |

**Example**

import { bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let link = 'welink://';
  let data = bundleManager.canOpenLink(link);
  hilog.info(0x0000, 'testTag', 'canOpenLink successfully: %{public}s', JSON.stringify(data));
} catch (err) {
  let message = (err as BusinessError).message;
  hilog.error(0x0000, 'testTag', 'canOpenLink failed: %{public}s', message);
}

#### bundleManager.getLaunchWant13+

getLaunchWant(): Want

Obtains the **Want** parameters of the [entry UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/application-package-glossary#uiability) of the current application.

**Atomic service API**: This API can be used in atomic services since API version 13.

**System capability**: SystemCapability.BundleManager.BundleFramework.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [Want](../ohos-app-ability-want-want/document.md) | Want object that contains only the bundle name and ability name. |

**Error codes**

For details about the error codes, see [Bundle Error Codes](../../../error-codes/bundle-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17700072 | The launch want is not found. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { bundleManager } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let want = bundleManager.getLaunchWant();
  hilog.info(0x0000, 'testTag', 'getLaunchWant ability name: %{public}s', want.abilityName);
  hilog.info(0x0000, 'testTag', 'getLaunchWant bundle name: %{public}s', want.bundleName);
} catch (error) {
  let message = (error as BusinessError).message;
  hilog.error(0x0000, 'testTag', 'getLaunchWant failed: %{public}s', message);
}

#### bundleManager.getBundleInfo14+

getBundleInfo(bundleName: string, bundleFlags: number, userId: number, callback: AsyncCallback<BundleInfo>): void

Obtains the [BundleInfo](../../dependent-elements-and-definitions/bundlemanager/bundleinfo/document.md) based on the given bundle name, bundle flags, and user ID. This API uses an asynchronous callback to return the result.

No permission is required for obtaining the caller's own information.

**Required permissions**: ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED

**System capability**: SystemCapability.BundleManager.BundleFramework.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| bundleName | string | Yes | Bundle name. |
| [bundleFlags](#bundleflag) | number | Yes | Type of the bundle information to obtain. |
| userId | number | Yes | User ID, which can be obtained by calling [getOsAccountLocalId](../../../../../system/basic-functions/basic-services-kit/arkts-apis/account-management/ohos-account-osaccount-system-account-management/document.md#getosaccountlocalid9). |
| callback | AsyncCallback<[BundleInfo](../../dependent-elements-and-definitions/bundlemanager/bundleinfo/document.md)\> | Yes | [Callback](../../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#asynccallback) used to return the result. If the information is successfully obtained, **err** is **null** and **data** is the bundle information. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Bundle Error Codes](../../../error-codes/bundle-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 17700001 | The specified bundleName is not found. |
| 17700004 | The specified user ID is not found. |
| 17700026 | The specified bundle is disabled. |

**Example**

// Obtain the bundle information, which contains the ability information.
import { bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let bundleName = 'com.example.myapplication';
let bundleFlags =
  bundleManager.BundleFlag.GET\_BUNDLE\_INFO\_WITH\_HAP\_MODULE | bundleManager.BundleFlag.GET\_BUNDLE\_INFO\_WITH\_ABILITY;
let userId = 100;

try {
  bundleManager.getBundleInfo(bundleName, bundleFlags, userId, (err, data) => {
    if (err) {
      hilog.error(0x0000, 'testTag', 'getBundleInfo failed: %{public}s', err.message);
    } else {
      hilog.info(0x0000, 'testTag', 'getBundleInfo successfully: %{public}s', JSON.stringify(data));
    }
  });
} catch (err) {
  let message = (err as BusinessError).message;
  hilog.error(0x0000, 'testTag', 'getBundleInfo failed: %{public}s', message);
}

// Obtain the bundle information, which contains the application information including metadata.
import { bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let bundleName = 'com.example.myapplication';
let bundleFlags =
  bundleManager.BundleFlag.GET\_BUNDLE\_INFO\_WITH\_APPLICATION | bundleManager.BundleFlag.GET\_BUNDLE\_INFO\_WITH\_METADATA;
let userId = 100;

try {
  bundleManager.getBundleInfo(bundleName, bundleFlags, userId, (err, data) => {
    if (err) {
      hilog.error(0x0000, 'testTag', 'getBundleInfo failed: %{public}s', err.message);
    } else {
      hilog.info(0x0000, 'testTag', 'getBundleInfo successfully: %{public}s', JSON.stringify(data));
    }
  });
} catch (err) {
  let message = (err as BusinessError).message;
  hilog.error(0x0000, 'testTag', 'getBundleInfo failed: %{public}s', message);
}

#### bundleManager.getBundleInfo14+

getBundleInfo(bundleName: string, bundleFlags: number, callback: AsyncCallback<BundleInfo>): void

Obtains the bundle information based on the given bundle name and bundle flags. This API uses an asynchronous callback to return the result.

No permission is required for obtaining the caller's own information.

**Required permissions**: ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED

**System capability**: SystemCapability.BundleManager.BundleFramework.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| bundleName | string | Yes | Bundle name. |
| [bundleFlags](#bundleflag) | number | Yes | Type of the bundle information to obtain. |
| callback | AsyncCallback<[BundleInfo](../../dependent-elements-and-definitions/bundlemanager/bundleinfo/document.md)\> | Yes | [Callback](../../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#asynccallback) used to return the result. If the information is successfully obtained, **err** is **null** and **data** is the bundle information. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Bundle Error Codes](../../../error-codes/bundle-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 17700001 | The specified bundleName is not found. |
| 17700026 | The specified bundle is disabled. |

**Example**

// Obtain the bundle information with the ExtensionAbility information.
import { bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let bundleName = 'com.example.myapplication';
let bundleFlags = bundleManager.BundleFlag.GET\_BUNDLE\_INFO\_WITH\_HAP\_MODULE |
bundleManager.BundleFlag.GET\_BUNDLE\_INFO\_WITH\_EXTENSION\_ABILITY;

try {
  bundleManager.getBundleInfo(bundleName, bundleFlags, (err, data) => {
    if (err) {
      hilog.error(0x0000, 'testTag', 'getBundleInfo failed: %{public}s', err.message);
    } else {
      hilog.info(0x0000, 'testTag', 'getBundleInfo successfully: %{public}s', JSON.stringify(data));
    }
  });
} catch (err) {
  let message = (err as BusinessError).message;
  hilog.error(0x0000, 'testTag', 'getBundleInfo failed: %{public}s', message);
}

#### bundleManager.getBundleInfo14+

getBundleInfo(bundleName: string, bundleFlags: number, userId?: number): Promise<BundleInfo>

Obtains the bundle information based on the given bundle name, bundle flags, and user ID. This API uses a promise to return the result.

No permission is required for obtaining the caller's own information.

**Required permissions**: ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED

**System capability**: SystemCapability.BundleManager.BundleFramework.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| bundleName | string | Yes | Bundle name. |
| [bundleFlags](#bundleflag) | number | Yes | Type of the bundle information to obtain. |
| userId | number | No | User ID, which can be obtained by calling [getOsAccountLocalId](../../../../../system/basic-functions/basic-services-kit/arkts-apis/account-management/ohos-account-osaccount-system-account-management/document.md#getosaccountlocalid9). The default value is the user ID of the caller. The value must be greater than or equal to 0. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[BundleInfo](../../dependent-elements-and-definitions/bundlemanager/bundleinfo/document.md)\> | Promise used to return the bundle information obtained. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Bundle Error Codes](../../../error-codes/bundle-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 17700001 | The specified bundleName is not found. |
| 17700004 | The specified user ID is not found. |
| 17700026 | The specified bundle is disabled. |

**Example**

// Obtain the bundle information with the application and signature information.
import { bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let bundleName = 'com.example.myapplication';
let bundleFlags = bundleManager.BundleFlag.GET\_BUNDLE\_INFO\_WITH\_APPLICATION |
bundleManager.BundleFlag.GET\_BUNDLE\_INFO\_WITH\_SIGNATURE\_INFO;
let userId = 100;

try {
  bundleManager.getBundleInfo(bundleName, bundleFlags, userId).then((data) => {
    hilog.info(0x0000, 'testTag', 'getBundleInfo successfully. Data: %{public}s', JSON.stringify(data));
  }).catch((err: BusinessError) => {
    hilog.error(0x0000, 'testTag', 'getBundleInfo failed. Cause: %{public}s', err.message);
  });
} catch (err) {
  let message = (err as BusinessError).message;
  hilog.error(0x0000, 'testTag', 'getBundleInfo failed. Cause: %{public}s', message);
}

import { bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let bundleName = 'com.example.myapplication';
let bundleFlags = bundleManager.BundleFlag.GET\_BUNDLE\_INFO\_DEFAULT;

try {
  bundleManager.getBundleInfo(bundleName, bundleFlags).then((data) => {
    hilog.info(0x0000, 'testTag', 'getBundleInfo successfully. Data: %{public}s', JSON.stringify(data));
  }).catch((err: BusinessError) => {
    hilog.error(0x0000, 'testTag', 'getBundleInfo failed. Cause: %{public}s', err.message);
  });
} catch (err) {
  let message = (err as BusinessError).message;
  hilog.error(0x0000, 'testTag', 'getBundleInfo failed. Cause: %{public}s', message);
}

#### bundleManager.getBundleInfoSync14+

getBundleInfoSync(bundleName: string, bundleFlags: number, userId: number): BundleInfo

Obtains the bundle information based on the given bundle name, bundle flags, and user ID. This API returns the result synchronously.

No permission is required for obtaining the caller's own information.

**Required permissions**: ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED

**System capability**: SystemCapability.BundleManager.BundleFramework.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| bundleName | string | Yes | Bundle name. |
| [bundleFlags](#bundleflag) | number | Yes | Type of the bundle information to obtain. |
| userId | number | Yes | User ID, which can be obtained by calling [getOsAccountLocalId](../../../../../system/basic-functions/basic-services-kit/arkts-apis/account-management/ohos-account-osaccount-system-account-management/document.md#getosaccountlocalid9). |

**Return value**

| Type | Description |
| :-- | :-- |
| [BundleInfo](../../dependent-elements-and-definitions/bundlemanager/bundleinfo/document.md) | Bundle information obtained. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Bundle Error Codes](../../../error-codes/bundle-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 17700001 | The specified bundleName is not found. |
| 17700004 | The specified user ID is not found. |
| 17700026 | The specified bundle is disabled. |

**Example**

import { bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let bundleName = 'com.example.myapplication';
let bundleFlags = bundleManager.BundleFlag.GET\_BUNDLE\_INFO\_WITH\_REQUESTED\_PERMISSION;
let userId = 100;

try {
  let data = bundleManager.getBundleInfoSync(bundleName, bundleFlags, userId);
  hilog.info(0x0000, 'testTag', 'getBundleInfoSync successfully: %{public}s', JSON.stringify(data));
} catch (err) {
  let message = (err as BusinessError).message;
  hilog.error(0x0000, 'testTag', 'getBundleInfoSync failed: %{public}s', message);
}

#### bundleManager.getBundleInfoSync14+

getBundleInfoSync(bundleName: string, bundleFlags: number): BundleInfo

Obtains the bundle information for the caller's user based on the given bundle name and bundle flags. This API returns the result synchronously.

No permission is required for obtaining the caller's own information.

**Required permissions**: ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED

**System capability**: SystemCapability.BundleManager.BundleFramework.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| bundleName | string | Yes | Bundle name. |
| [bundleFlags](#bundleflag) | number | Yes | Type of the bundle information to obtain. |

**Return value**

| Type | Description |
| :-- | :-- |
| [BundleInfo](../../dependent-elements-and-definitions/bundlemanager/bundleinfo/document.md) | Bundle information obtained. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Bundle Error Codes](../../../error-codes/bundle-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 17700001 | The specified bundleName is not found. |
| 17700026 | The specified bundle is disabled. |

**Example**

import { bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let bundleName = 'com.example.myapplication';
let bundleFlags = bundleManager.BundleFlag.GET\_BUNDLE\_INFO\_WITH\_REQUESTED\_PERMISSION;
try {
  let data = bundleManager.getBundleInfoSync(bundleName, bundleFlags);
  hilog.info(0x0000, 'testTag', 'getBundleInfoSync successfully: %{public}s', JSON.stringify(data));
} catch (err) {
  let message = (err as BusinessError).message;
  hilog.error(0x0000, 'testTag', 'getBundleInfoSync failed: %{public}s', message);
}

#### bundleManager.getBundleNameByUid14+

getBundleNameByUid(uid: number, callback: AsyncCallback<string>): void

Obtains the bundle name based on the given UID. This API uses an asynchronous callback to return the result.

**Required permissions**: ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED

**System capability**: SystemCapability.BundleManager.BundleFramework.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| uid | number | Yes | UID of the application. |
| callback | AsyncCallback<string> | Yes | [Callback](../../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#asynccallback) used to return the result. If the information is successfully obtained, **err** is **null** and **data** is the bundle name. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Bundle Error Codes](../../../error-codes/bundle-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 17700021 | The uid is not found. |

**Example**

import { bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let uid = 20010005;
try {
  bundleManager.getBundleNameByUid(uid, (err, data) => {
    if (err) {
      hilog.error(0x0000, 'testTag', 'getBundleNameByUid failed: %{public}s', err.message);
    } else {
      hilog.info(0x0000, 'testTag', 'getBundleNameByUid successfully: %{public}s', JSON.stringify(data));
    }
  });
} catch (err) {
  let message = (err as BusinessError).message;
  hilog.error(0x0000, 'testTag', 'getBundleNameByUid failed: %{public}s', message);
}

#### bundleManager.getBundleNameByUid14+

getBundleNameByUid(uid: number): Promise<string>

Obtains the bundle name based on the given UID. This API uses a promise to return the result.

**Required permissions**: ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED

**System capability**: SystemCapability.BundleManager.BundleFramework.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| uid | number | Yes | UID of the application. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<string> | Promise used to return the bundle name obtained. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Bundle Error Codes](../../../error-codes/bundle-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 17700021 | The uid is not found. |

**Example**

import { bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let uid = 20010005;
try {
  bundleManager.getBundleNameByUid(uid).then((data) => {
    hilog.info(0x0000, 'testTag', 'getBundleNameByUid successfully. Data: %{public}s', JSON.stringify(data));
  }).catch((err: BusinessError) => {
    hilog.error(0x0000, 'testTag', 'getBundleNameByUid failed. Cause: %{public}s', err.message);
  });
} catch (err) {
  let message = (err as BusinessError).message;
  hilog.error(0x0000, 'testTag', 'getBundleNameByUid failed. Cause: %{public}s', message);
}

#### bundleManager.getBundleNameByUidSync14+

getBundleNameByUidSync(uid: number): string

Obtains the bundle name based on the given UID. This API returns the result synchronously.

**Required permissions**: ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED

**System capability**: SystemCapability.BundleManager.BundleFramework.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| uid | number | Yes | UID of the application. |

**Return value**

| Type | Description |
| :-- | :-- |
| string | Bundle name obtained. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Bundle Error Codes](../../../error-codes/bundle-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 17700021 | The uid is not found. |

**Example**

import { bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let uid = 20010005;
try {
  let data = bundleManager.getBundleNameByUidSync(uid);
  hilog.info(0x0000, 'testTag', 'getBundleNameByUidSync successfully. Data: %{public}s', JSON.stringify(data));
} catch (err) {
  let message = (err as BusinessError).message;
  hilog.error(0x0000, 'testTag', 'getBundleNameByUidSync failed. Cause: %{public}s', message);
}

#### bundleManager.getAppCloneIdentity14+

getAppCloneIdentity(uid: number): Promise<AppCloneIdentity>;

Obtains the bundle name and clone index of a cloned application based on the given UID. This API uses a promise to return the result.

**Required permissions**: ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED

**System capability**: SystemCapability.BundleManager.BundleFramework.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| uid | number | Yes | UID of the application. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[AppCloneIdentity](../../dependent-elements-and-definitions/bundlemanager/bundleinfo/document.md#appcloneidentity14)\> | Promise used to return the application clone index. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Bundle Error Codes](../../../error-codes/bundle-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 17700021 | The uid is not found. |

**Example**

import { bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let uid = 20010005;

try {
  bundleManager.getAppCloneIdentity(uid).then((res) => {
    hilog.info(0x0000, 'testTag', 'getAppCloneIdentity res = %{public}s', JSON.stringify(res));
  }).catch((err: BusinessError) => {
    hilog.error(0x0000, 'testTag', 'getAppCloneIdentity failed. Cause: %{public}s', err.message);
  });
} catch (err) {
  let message = (err as BusinessError).message;
  hilog.error(0x0000, 'testTag', 'getAppCloneIdentity failed. Cause: %{public}s', message);
}

#### bundleManager.getSignatureInfo18+

getSignatureInfo(uid: number): SignatureInfo

Obtains the [signature information](../../dependent-elements-and-definitions/bundlemanager/bundleinfo/document.md#signatureinfo) of an application based on the given UID.

**Required permissions**: ohos.permission.GET\_SIGNATURE\_INFO

**System capability**: SystemCapability.BundleManager.BundleFramework.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| uid | number | Yes | UID of the application. |

**Return value**

| Type | Description |
| :-- | :-- |
| [SignatureInfo](../../dependent-elements-and-definitions/bundlemanager/bundleinfo/document.md#signatureinfo) | SignatureInfo object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Bundle Error Codes](../../../error-codes/bundle-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 17700021 | The uid is not found. |

**Example**

import { bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let uid = 20010005; // Replace uid with the UID of the corresponding application.
try {
  let data = bundleManager.getSignatureInfo(uid);
  hilog.info(0x0000, 'testTag', 'getSignatureInfo successfully. Data: %{public}s', JSON.stringify(data));
} catch (err) {
  let message = (err as BusinessError).message;
  hilog.error(0x0000, 'testTag', 'getSignatureInfo failed. Cause: %{public}s', message);
}

#### bundleManager.getAbilityInfo20+

getAbilityInfo(uri: string, abilityFlags: number): Promise<Array<AbilityInfo>>

Obtains the ability information based on the given resource identifier and ability flag. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 20.

**Required permissions**: ohos.permission.GET\_ABILITY\_INFO

**System capability**: SystemCapability.BundleManager.BundleFramework.Core

**Device behavior differences**: This API can be properly called only on PCs/2-in-1 devices. If it is called on other device types, error code 201 is returned.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| uri | string | Yes | URI of the resource. The value is the same as that of the [uris field under skills in the module.json5 file](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/module-configuration-file#skills). |
| abilityFlags | number | Yes | [Ability flag](#abilityflag20), indicating the ability information to be obtained. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<[AbilityInfo](../../dependent-elements-and-definitions/bundlemanager/abilityinfo/document.md)\>> | Promise used to return an array of ability information. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Bundle Error Codes](../../../error-codes/bundle-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 17700003 | The ability is not found. |

**Example**

import { bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let abilityFlags = bundleManager.AbilityFlag.GET\_ABILITY\_INFO\_WITH\_APPLICATION;
let uri = "https://www.example.com";

try {
  bundleManager.getAbilityInfo(uri, abilityFlags).then((data) => {
    console.info('getAbilityInfo successfully. Data: ' + JSON.stringify(data));
  }).catch((err: BusinessError) => {
    let message = (err as BusinessError).message;
    console.error('getAbilityInfo failed. Cause: ' + message);
  });
} catch (err) {
  let message = (err as BusinessError).message;
  console.error('getAbilityInfo failed. Cause: ' + message);
}

#### bundleManager.cleanBundleCacheFilesForSelf21+

cleanBundleCacheFilesForSelf(): Promise<void>

Clears the application cache. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 21.

**System capability**: SystemCapability.BundleManager.BundleFramework.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

import { bundleManager } from '@kit.AbilityKit';

bundleManager.cleanBundleCacheFilesForSelf().then(() => {
  console.info('cleanBundleCacheFilesForSelf complete.');
});

#### bundleManager.getPluginBundlePathForSelf22+

getPluginBundlePathForSelf(pluginBundleName: string): string

Obtains the installation path of a specified plugin in the current [application sandbox](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-sandbox-directory).

**System capability**: SystemCapability.BundleManager.BundleFramework.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| pluginBundleName | string | Yes | Bundle name of the target plugin. |

**Return value**

| Type | Description |
| :-- | :-- |
| string | Installation path of the target plugin in the current application sandbox. |

**Error codes**

For details about the error codes, see [Bundle Error Codes](../../../error-codes/bundle-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17700001 | The specified bundleName is not found. |

**Example**

import { bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

// Use the actual bundle name of the plugin.
let pluginBundleName = 'com.ohos.pluginDemo';
try {
  let path = bundleManager.getPluginBundlePathForSelf(pluginBundleName);
  hilog.info(0x0000, 'testTag', 'getPluginBundlePathForSelf successfully. path: %{public}s', path);
} catch (err) {
  let message = (err as BusinessError).message;
  hilog.error(0x0000, 'testTag', 'getPluginBundlePathForSelf failed. Cause: %{public}s', message);
}

#### ApplicationInfo

type ApplicationInfo = \_ApplicationInfo

Defines the application information.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.BundleManager.BundleFramework.Core

| Type | Description |
| :-- | :-- |
| [\_ApplicationInfo](../../dependent-elements-and-definitions/bundlemanager/applicationinfo/document.md#applicationinfo-1) | Application information. |

#### ModuleMetadata10+

type ModuleMetadata = \_ModuleMetadata

Defines the metadata of a module.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.BundleManager.BundleFramework.Core

| Type | Description |
| :-- | :-- |
| [\_ModuleMetadata](../../dependent-elements-and-definitions/bundlemanager/applicationinfo/document.md#modulemetadata10) | Metadata of the module. |

#### Metadata

type Metadata = \_Metadata

Defines the metadata.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.BundleManager.BundleFramework.Core

| Type | Description |
| :-- | :-- |
| [\_Metadata](../../dependent-elements-and-definitions/bundlemanager/metadata/document.md#metadata-1) | Metadata. |

#### BundleInfo

type BundleInfo = \_BundleInfo.BundleInfo

Defines the bundle information.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.BundleManager.BundleFramework.Core

| Type | Description |
| :-- | :-- |
| [\_BundleInfo.BundleInfo](../../dependent-elements-and-definitions/bundlemanager/bundleinfo/document.md#bundleinfo-1) | Bundle information. |

#### UsedScene

type UsedScene = \_BundleInfo.UsedScene

Defines the use scenario and timing for using the permission.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.BundleManager.BundleFramework.Core

| Type | Description |
| :-- | :-- |
| [\_BundleInfo.UsedScene](../../dependent-elements-and-definitions/bundlemanager/bundleinfo/document.md#usedscene) | Use scenario and timing for using the permission. |

#### ReqPermissionDetail

type ReqPermissionDetail = \_BundleInfo.ReqPermissionDetail

Defines the detailed information of the permissions to request from the system.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.BundleManager.BundleFramework.Core

| Type | Description |
| :-- | :-- |
| [\_BundleInfo.ReqPermissionDetail](../../dependent-elements-and-definitions/bundlemanager/bundleinfo/document.md#reqpermissiondetail) | Detailed information of the permissions to request from the system. |

#### SignatureInfo

type SignatureInfo = \_BundleInfo.SignatureInfo

Defines the signature information of the bundle.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.BundleManager.BundleFramework.Core

| Type | Description |
| :-- | :-- |
| [\_BundleInfo.SignatureInfo](../../dependent-elements-and-definitions/bundlemanager/bundleinfo/document.md#signatureinfo) | Signature information of the bundle. |

#### HapModuleInfo

type HapModuleInfo = \_HapModuleInfo.HapModuleInfo

Defines the module information.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.BundleManager.BundleFramework.Core

| Type | Description |
| :-- | :-- |
| [\_HapModuleInfo.HapModuleInfo](../../dependent-elements-and-definitions/bundlemanager/hapmoduleinfo/document.md#hapmoduleinfo-1) | Module information. |

#### PreloadItem

type PreloadItem = \_HapModuleInfo.PreloadItem

Defines the preloaded module information in the atomic service.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.BundleManager.BundleFramework.Core

| Type | Description |
| :-- | :-- |
| [\_HapModuleInfo.PreloadItem](../../dependent-elements-and-definitions/bundlemanager/hapmoduleinfo/document.md#preloaditem) | Preloaded module information in the atomic service. |

#### Dependency

type Dependency = \_HapModuleInfo.Dependency

Defines the information about the dynamic shared libraries on which the module depends.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.BundleManager.BundleFramework.Core

| Type | Description |
| :-- | :-- |
| [\_HapModuleInfo.Dependency](../../dependent-elements-and-definitions/bundlemanager/hapmoduleinfo/document.md#dependency) | Information about the dynamic shared libraries on which the module depends. |

#### RouterItem12+

type RouterItem = \_HapModuleInfo.RouterItem

Defines the router table configuration of the module.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.BundleManager.BundleFramework.Core

| Type | Description |
| :-- | :-- |
| [\_HapModuleInfo.RouterItem](../../dependent-elements-and-definitions/bundlemanager/hapmoduleinfo/document.md#routeritem12) | Router table configuration of the module. |

#### DataItem12+

type DataItem = \_HapModuleInfo.DataItem

Defines the user-defined data in the routing table configuration of the module.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.BundleManager.BundleFramework.Core

| Type | Description |
| :-- | :-- |
| [\_HapModuleInfo.DataItem](../../dependent-elements-and-definitions/bundlemanager/hapmoduleinfo/document.md#dataitem12) | User-defined data in the routing table configuration of the module. |

#### AbilityInfo

type AbilityInfo = \_AbilityInfo.AbilityInfo

Defines the ability information.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.BundleManager.BundleFramework.Core

| Type | Description |
| :-- | :-- |
| [\_AbilityInfo.AbilityInfo](../../dependent-elements-and-definitions/bundlemanager/abilityinfo/document.md#abilityinfo-1) | Ability information. |

#### WindowSize

type WindowSize = \_AbilityInfo.WindowSize

Defines the window size.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.BundleManager.BundleFramework.Core

| Type | Description |
| :-- | :-- |
| [\_AbilityInfo.WindowSize](../../dependent-elements-and-definitions/bundlemanager/abilityinfo/document.md#windowsize) | Window size. |

#### ExtensionAbilityInfo

type ExtensionAbilityInfo = \_ExtensionAbilityInfo.ExtensionAbilityInfo

Defines the ExtensionAbility information.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.BundleManager.BundleFramework.Core

| Type | Description |
| :-- | :-- |
| [\_ExtensionAbilityInfo.ExtensionAbilityInfo](../../dependent-elements-and-definitions/bundlemanager/extensionabilityinfo/document.md#extensionabilityinfo-1) | ExtensionAbility information. |

#### ElementName

type ElementName = \_ElementName

Defines the element name.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.BundleManager.BundleFramework.Core

| Type | Description |
| :-- | :-- |
| [\_ElementName](../../dependent-elements-and-definitions/bundlemanager/elementname/document.md#elementname-1) | Element name. |

#### Skill12+

type Skill = \_Skill.Skill

Defines the skill information.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.BundleManager.BundleFramework.Core

| Type | Description |
| :-- | :-- |
| [\_Skill.Skill](../../dependent-elements-and-definitions/bundlemanager/skill/document.md#skill-1) | Skill information. |

#### SkillUrl12+

type SkillUrl = \_Skill.SkillUri

Defines the SkillUri information.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.BundleManager.BundleFramework.Core

| Type | Description |
| :-- | :-- |
| [\_Skill.SkillUri](../../dependent-elements-and-definitions/bundlemanager/skill/document.md#skilluri) | SkillUri information. |

#### AppCloneIdentity15+

type AppCloneIdentity = \_BundleInfo.AppCloneIdentity

Describes the identity information of an application clone.

**System capability**: SystemCapability.BundleManager.BundleFramework.Core

| Type | Description |
| :-- | :-- |
| [\_BundleInfo.AppCloneIdentity](../../dependent-elements-and-definitions/bundlemanager/bundleinfo/document.md#appcloneidentity14) | Identity information of an application clone. |
