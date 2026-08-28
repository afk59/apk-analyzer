# @ohos.enterprise.adminManager (Administrator Permission Management)

The **adminManager** module provides administrator permission management capabilities for enterprise MDM applications, including enabling or disabling administrator permissions, subscribing to events, delegating applications, and granting permissions.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/8MlYIAkbRgudt7LoyfMixg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062405Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EF4C889646EFE908675CA6024E6E51FF0089B793A9F956BDFB52081DB833CB68)

The initial APIs of this module are supported since API version 12. Newly added APIs will be marked with a superscript to indicate their earliest API version.

The APIs of this module can be called only by a device administrator application. For details, see [MDM Kit Development](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/mdm-kit-guide).

#### Modules to Import

import { adminManager } from '@kit.MDMKit';

#### adminManager.disableAdmin

disableAdmin(admin: Want, userId?: number): Promise<void>

Disables a device administrator application for the specified user. This API uses a promise to return the result.

**Required permissions**: ohos.permission.MANAGE\_ENTERPRISE\_DEVICE\_ADMIN (available only for system applications) or ohos.permission.START\_PROVISIONING\_MESSAGE

\- **ohos.permission.START\_PROVISIONING\_MESSAGE** is supported since API version 20. This permission can be requested only when the BYOD device administrator application is disabled.

\- **ohos.permission.MANAGE\_ENTERPRISE\_DEVICE\_ADMIN** is required for API version 19 and earlier. (This permission can be requested only by system applications.)

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. When deactivating the BYOD device administrator application, you can pass only the **EnterpriseAdminExtensionAbility** component of the current application. |
| userId | number | No | 
User ID, which must be greater than or equal to 0.

\- If **userId** is passed in, this API applies to the specified user.

\- If **userId** is not passed in, this API applies to the current user.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. If the operation fails, an error object will be thrown. |

**Error codes**

For details about the error codes, see [Enterprise Device Management Error Codes](../../error-codes/enterprise-device-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9200005 | Failed to deactivate the administrator application of the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**Example**

import { adminManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

adminManager.disableAdmin(wantTemp, 100).catch((err: BusinessError) => {
  console.error(\`Failed to disable admin. Code: ${err.code}, message: ${err.message}\`);
});

#### adminManager.isByodAdmin20+

isByodAdmin(admin: Want): boolean

Checks whether the current application is activated as a BYOD device administrator application based on the **EnterpriseAdminExtensionAbility** component.

**Required permission**: ohos.permission.START\_PROVISIONING\_MESSAGE

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. Only the **EnterpriseAdminExtensionAbility** component of the current application can be passed. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | The value **true** indicates the application is activated as a BYOD device administrator application, and the value **false** indicates the opposite. |

**Error codes**

For details about the error codes, see [Enterprise Device Management Error Codes](../../error-codes/enterprise-device-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 9200012 | Parameter verification failed. |

**Example**

import { Want } from '@kit.AbilityKit';
import { adminManager } from '@kit.MDMKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  let result: boolean = adminManager.isByodAdmin(wantTemp);
  console.info(\`Succeeded in querying admin is byod admin or not : ${result}\`);
} catch (error) {
  console.error(\`Failed to query admin is byod admin or not. Code is ${error.code}, message is ${error.message}\`);
}

#### adminManager.subscribeManagedEventSync

subscribeManagedEventSync(admin: Want, managedEvents: Array<ManagedEvent>): void

Subscribes to system management events.

**Required permissions**: ohos.permission.ENTERPRISE\_SUBSCRIBE\_MANAGED\_EVENT

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| managedEvents | Array<[ManagedEvent](#managedevent)\> | Yes | Array of events to subscribe to. |

**Error codes**

For details about the error codes, see [Enterprise Device Management Error Codes](../../error-codes/enterprise-device-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9200001 | The application is not an administrator application of the device. |
| 9200008 | The specified system event is invalid. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { adminManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
let events: Array<adminManager.ManagedEvent> = \[adminManager.ManagedEvent.MANAGED\_EVENT\_BUNDLE\_ADDED, adminManager.ManagedEvent.MANAGED\_EVENT\_BUNDLE\_REMOVED\];

try {
  adminManager.subscribeManagedEventSync(wantTemp, events);
  console.info('Succeeded in subscribing managed event.');
} catch (err) {
  console.error(\`Failed to subscribe managed event. Code: ${err.code}, message: ${err.message}\`);
}

#### adminManager.unsubscribeManagedEventSync

unsubscribeManagedEventSync(admin: Want, managedEvents: Array<ManagedEvent>): void

Unsubscribes from system management events.

**Required permissions**: ohos.permission.ENTERPRISE\_SUBSCRIBE\_MANAGED\_EVENT

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| managedEvents | Array<[ManagedEvent](#managedevent)\> | Yes | Array of events to unsubscribe from. |

**Error codes**

For details about the error codes, see [Enterprise Device Management Error Codes](../../error-codes/enterprise-device-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9200001 | The application is not an administrator application of the device. |
| 9200008 | The specified system event is invalid. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { adminManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
let events: Array<adminManager.ManagedEvent> = \[adminManager.ManagedEvent.MANAGED\_EVENT\_BUNDLE\_ADDED, adminManager.ManagedEvent.MANAGED\_EVENT\_BUNDLE\_REMOVED\];

try {
  adminManager.unsubscribeManagedEventSync(wantTemp, events);
  console.info('Succeeded in unsubscribing managed event.');
} catch (err) {
  console.error(\`Failed to unsubscribe managed event. Code: ${err.code}, message: ${err.message}\`);
}

#### adminManager.setDelegatedPolicies14+

setDelegatedPolicies(admin: Want, bundleName: string, policies: Array<string>): void

Delegates other applications to set device management policies. The applications must request the permissions required.

**Required permission**: ohos.permission.ENTERPRISE\_MANAGE\_DELEGATED\_POLICY

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| bundleName | string | Yes | Bundle name of the delegated application. The distribution type of the delegated application must be **enterprise\_normal** or **enterprise\_mdm**. You can call the [getBundleInfoForSelf](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-bundle-bundlemanager-bundle-management-module/document.md#bundlemanagergetbundleinfoforself) API to query the [BundleInfo](../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/bundlemanager/bundleinfo/document.md) of the application, where **BundleInfo.appInfo.appDistributionType** indicates the distribution type. |
| policies | Array<string> | Yes | [Delegation Policy List](#delegation-policy-list) |

**Error codes**

For details about the error codes, see [Enterprise Device Management Error Codes](../../error-codes/enterprise-device-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9200009 | Failed to grant the permission to the application. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { adminManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let admin: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
// Replace with actual values.
let policies: Array<string> = \["disabled\_hdc"\];

try {
  // Replace parameters with actual values.
  adminManager.setDelegatedPolicies(admin, "com.example.enterprise.xxx", policies);
  console.info('Succeeded in setting delegated policies.');
} catch (err) {
  console.error(\`Failed to set delegated policies. Code: ${err.code}, message: ${err.message}\`);
}

#### adminManager.getDelegatedPolicies14+

getDelegatedPolicies(admin: Want, bundleName: string): Array<string>

Queries the list of policies that can be accessed by the delegated application.

**Required permission**: ohos.permission.ENTERPRISE\_MANAGE\_DELEGATED\_POLICY

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| bundleName | string | Yes | Bundle name of the delegated application. The distribution type of the delegated application must be **enterprise\_normal** or **enterprise\_mdm**. You can call the [getBundleInfoForSelf](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-bundle-bundlemanager-bundle-management-module/document.md#bundlemanagergetbundleinfoforself) API to query the [BundleInfo](../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/bundlemanager/bundleinfo/document.md) of the application, where **BundleInfo.appInfo.appDistributionType** indicates the distribution type. |

**Return value**

| Type | Description |
| :-- | :-- |
| Array<string> | Delegation policy list. |

**Error codes**

For details about the error codes, see [Enterprise Device Management Error Codes](../../error-codes/enterprise-device-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { adminManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let admin: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  // Replace parameters with actual values.
  let policies: Array<string> = adminManager.getDelegatedPolicies(admin, "com.example.enterprise.xxx");
  console.info(\`Succeeded in getting delegated policies.${JSON.stringify(policies)}\`);
} catch (err) {
  console.error(\`Failed to get delegated policies. Code: ${err.code}, message: ${err.message}\`);
}

#### adminManager.getDelegatedBundleNames14+

getDelegatedBundleNames(admin: Want, policy: string): Array<string>

Queries the delegated applications that can access a delegation policy and output the list of delegated applications.

**Required permission**: ohos.permission.ENTERPRISE\_MANAGE\_DELEGATED\_POLICY

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| policy | string | Yes | Delegation policy. |

**Return value**

| Type | Description |
| :-- | :-- |
| Array<string> | List of delegated applications. |

**Error codes**

For details about the error codes, see [Enterprise Device Management Error Codes](../../error-codes/enterprise-device-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { adminManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let admin: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  // Replace parameters with actual values.
  let bundleNames: Array<string> = adminManager.getDelegatedBundleNames(admin, "disabled\_hdc");
  console.info(\`Succeeded in getting delegated bundles.${JSON.stringify(bundleNames)}\`);
} catch (err) {
  console.error(\`Failed to get delegated bundles. Code: ${err.code}, message: ${err.message}\`);
}

#### adminManager.startAdminProvision15+

startAdminProvision(admin: Want, type: AdminType, context: common.Context, parameters: Record<string, string>): void

Enables the device administrator application to open a page for the BYOD administrator to perform activation.

**Required permission**: ohos.permission.START\_PROVISIONING\_MESSAGE

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Device behavior differences**: This API can be properly called on phones and tablets but does not take effect on other devices.

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| type | [AdminType](#admintype15) | Yes | Type of the activated device administrator application. Only the **ADMIN\_TYPE\_BYOD** type is supported. |
| context | [common.Context](../../../../../application-framework/ability-kit/arkts-apis/stage-model/ohos-app-ability-common-ability-common-module/document.md#context) | Yes | Context information of the administrator application. |
| parameters | Record<string, string> | Yes | 
Custom parameters. The key value must contain **activateId** and may optionally include **customizedInfo** and **localDeactivationPolicy**.

\- **activateId**: project activation ID.

\- **customizedInfo**: enterprise-defined information.

\- **localDeactivationPolicy**: local deactivation delay (unit: hour). This parameter is supported since API version 22.

 |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { adminManager } from '@kit.MDMKit';
import { common, Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
let recordParameters: Record<string, string> = {
  // Replace with actual values.
  "activateId": "activateId testValue",
  "customizedInfo": "customizedInfo testValue"
};
// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
const context = this.getUIContext().getHostContext() as common.UIAbilityContext;
try {
  console.info('context:' + JSON.stringify(context));
  adminManager.startAdminProvision(wantTemp, adminManager.AdminType.ADMIN\_TYPE\_BYOD, context, recordParameters);
  console.info('startAdminProvision::success');
} catch (error) {
  console.error('startAdminProvision::errorCode: ' + error.code + ' errorMessage: ' + error.message);
}

#### ManagedEvent

Enumerates the system management events that can be subscribed to.

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

| Name | Value | Description |
| :-- | :-- | :-- |
| MANAGED\_EVENT\_BUNDLE\_ADDED | 0 | An application is installed. |
| MANAGED\_EVENT\_BUNDLE\_REMOVED | 1 | An application is uninstalled. |
| MANAGED\_EVENT\_APP\_START | 2 | An application is started. |
| MANAGED\_EVENT\_APP\_STOP | 3 | An application is stopped. |
| MANAGED\_EVENT\_SYSTEM\_UPDATE | 4 | The system is updated. |
| MANAGED\_EVENT\_ACCOUNT\_ADDED18+ | 5 | An account is created. |
| MANAGED\_EVENT\_ACCOUNT\_SWITCHED18+ | 6 | An account is switched. |
| MANAGED\_EVENT\_ACCOUNT\_REMOVED18+ | 7 | An account is removed. |

#### AdminType15+

Enumerates the types of device administrator applications.

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

| Name | Value | Description |
| :-- | :-- | :-- |
| ADMIN\_TYPE\_BYOD | 0x02 | BYOD device administrator application. |

#### Policy20+

Defines the policy type for the trustlist or blocklist.

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

| Name | Value | Description |
| :-- | :-- | :-- |
| BLOCK\_LIST | 0 | Blocklist. |
| TRUST\_LIST | 1 | Trustlist. |

#### Appendix

## Delegation Policy List

| Policy Name | API | Description |
| :-- | :-- | :-- |
| disallow\_add\_local\_account | 
[accountManager.disallowOsAccountAddition](../ohos-enterprise-accountmanager-account-management/document.md#accountmanagerdisallowosaccountaddition)

[accountManager.isOsAccountAdditionDisallowed](../ohos-enterprise-accountmanager-account-management/document.md#accountmanagerisosaccountadditiondisallowed)

 | 

Prevents the device from creating a local user, without needing the **accountId** parameter.

Checks whether the device is prevented from creating a local user, without needing the **accountId** parameter.

 |
| disallow\_add\_os\_account\_by\_user | 

[accountManager.disallowOsAccountAddition](../ohos-enterprise-accountmanager-account-management/document.md#accountmanagerdisallowosaccountaddition)

[accountManager.isOsAccountAdditionDisallowed](../ohos-enterprise-accountmanager-account-management/document.md#accountmanagerisosaccountadditiondisallowed)

 | 

Prevents the specified user from adding accounts, with the **accountId** parameter passed.

Checks whether the specified user is prevented from adding accounts, with the **accountId** parameter passed.

 |
| disallow\_running\_bundles | 

[applicationManager.addDisallowedRunningBundlesSync](../ohos-enterprise-applicationmanager-application-management/document.md#applicationmanageradddisallowedrunningbundlessync)

[applicationManager.removeDisallowedRunningBundlesSync](../ohos-enterprise-applicationmanager-application-management/document.md#applicationmanagerremovedisallowedrunningbundlessync)

[applicationManager.getDisallowedRunningBundlesSync](../ohos-enterprise-applicationmanager-application-management/document.md#applicationmanagergetdisallowedrunningbundlessync)

 | 

Adds the applications that are not allowed to run by the current or specified user.

Removes applications that are not allowed to run.

Obtains applications that are not allowed to run by the current user or specified user.

 |
| manage\_auto\_start\_apps | 

[applicationManager.addAutoStartApps](../ohos-enterprise-applicationmanager-application-management/document.md#applicationmanageraddautostartapps)

[applicationManager.removeAutoStartApps](../ohos-enterprise-applicationmanager-application-management/document.md#applicationmanagerremoveautostartapps)

[applicationManager.getAutoStartApps](../ohos-enterprise-applicationmanager-application-management/document.md#applicationmanagergetautostartapps)

 | 

Adds the auto-start applications.

Removes the auto-start applications.

Obtains the auto-start applications.

 |
| allowed\_bluetooth\_devices | 

[bluetoothManager.addAllowedBluetoothDevices](../ohos-enterprise-bluetoothmanager-bluetooth-management/document.md#bluetoothmanageraddallowedbluetoothdevices)

[bluetoothManager.removeAllowedBluetoothDevices](../ohos-enterprise-bluetoothmanager-bluetooth-management/document.md#bluetoothmanagerremoveallowedbluetoothdevices)

[bluetoothManager.getAllowedBluetoothDevices](../ohos-enterprise-bluetoothmanager-bluetooth-management/document.md#bluetoothmanagergetallowedbluetoothdevices)

 | 

Adds allowed Bluetooth devices.

Removes allowed Bluetooth devices.

Obtains allowed Bluetooth devices.

 |
| set\_browser\_policies | 

[browser.setPolicySync](../ohos-enterprise-browser-browser-management/document.md#browsersetpolicysync)

[browser.getPoliciesSync](../ohos-enterprise-browser-browser-management/document.md#browsergetpoliciessync)

 | 

Sets the sub-policy for a specified browser.

Obtains the policy of a specified browser.

 |
| allowed\_install\_bundles | 

[bundleManager.addAllowedInstallBundlesSync](../ohos-enterprise-bundlemanager-bundle-management/document.md#bundlemanageraddallowedinstallbundlessync)

[bundleManager.removeAllowedInstallBundlesSync](../ohos-enterprise-bundlemanager-bundle-management/document.md#bundlemanagerremoveallowedinstallbundlessync)

[bundleManager.getAllowedInstallBundlesSync](../ohos-enterprise-bundlemanager-bundle-management/document.md#bundlemanagergetallowedinstallbundlessync)

 | 

Adds the applications that can be installed by the current or specified user.

Removes the applications that can be installed.

Obtains the applications that can be installed by the current or specified user.

 |
| disallowed\_install\_bundles | 

[bundleManager.addDisallowedInstallBundlesSync](../ohos-enterprise-bundlemanager-bundle-management/document.md#bundlemanageradddisallowedinstallbundlessync)

[bundleManager.removeDisallowedInstallBundlesSync](../ohos-enterprise-bundlemanager-bundle-management/document.md#bundlemanagerremovedisallowedinstallbundlessync)

[bundleManager.getDisallowedInstallBundlesSync](../ohos-enterprise-bundlemanager-bundle-management/document.md#bundlemanagergetdisallowedinstallbundlessync)

 | 

Adds the applications that are not allowed to be installed by the current or specified user.

Removes the applications that are not allowed to be installed.

Obtains the applications that cannot be installed by the current or specified user.

 |
| disallowed\_uninstall\_bundles | 

[bundleManager.addDisallowedUninstallBundlesSync](../ohos-enterprise-bundlemanager-bundle-management/document.md#bundlemanageradddisalloweduninstallbundlessync)

[bundleManager.removeDisallowedUninstallBundlesSync](../ohos-enterprise-bundlemanager-bundle-management/document.md#bundlemanagerremovedisalloweduninstallbundlessync)

[bundleManager.getDisallowedUninstallBundlesSync](../ohos-enterprise-bundlemanager-bundle-management/document.md#bundlemanagergetdisalloweduninstallbundlessync)

 | 

Adds the applications that cannot be uninstalled by the current or specified user.

Removes the applications that cannot be uninstalled.

Obtains the applications that cannot be uninstalled by the current or specified user.

 |
| get\_device\_info | [deviceInfo.getDeviceInfo](../ohos-enterprise-deviceinfo-device-information-management/document.md#deviceinfogetdeviceinfo) | Obtains device information. |
| location\_policy | 

[locationManager.setLocationPolicy](../ohos-enterprise-locationmanager-location-service-management/document.md#locationmanagersetlocationpolicy)

[locationManager.getLocationPolicy](../ohos-enterprise-locationmanager-location-service-management/document.md#locationmanagergetlocationpolicy)

 | 

Sets the location service policy.

Obtains the location service policy.

 |
| disabled\_network\_interface | 

[networkManager.setNetworkInterfaceDisabledSync](../ohos-enterprise-networkmanager-network-management/document.md#networkmanagersetnetworkinterfacedisabledsync)

[networkManager.isNetworkInterfaceDisabledSync](../ohos-enterprise-networkmanager-network-management/document.md#networkmanagerisnetworkinterfacedisabledsync)

 | 

Disables a network interface.

Checks whether the network interface is disabled.

 |
| global\_proxy | 

[networkManager.setGlobalProxySync](../ohos-enterprise-networkmanager-network-management/document.md#networkmanagersetglobalproxysync)

[networkManager.getGlobalProxySync](../ohos-enterprise-networkmanager-network-management/document.md#networkmanagergetglobalproxysync)

 | 

Sets the global network proxy.

Obtains the global network proxy.

 |
| disabled\_bluetooth | 

[restrictions.setDisallowedPolicy](../ohos-enterprise-restrictions-restrictions/document.md#restrictionssetdisallowedpolicy)

[restrictions.getDisallowedPolicy](../ohos-enterprise-restrictions-restrictions/document.md#restrictionsgetdisallowedpolicy)

 | 

Accepts **bluetooth** as the parameter to disable or enable the Bluetooth capability.

Accepts **bluetooth** as the parameter to query whether the Bluetooth capability is disabled.

 |
| disallow\_modify\_datetime | 

[restrictions.setDisallowedPolicy](../ohos-enterprise-restrictions-restrictions/document.md#restrictionssetdisallowedpolicy)

[restrictions.getDisallowedPolicy](../ohos-enterprise-restrictions-restrictions/document.md#restrictionsgetdisallowedpolicy)

 | 

Accepts **modifyDateTime** as the parameter to disable or enable the system time setting capability.

Accepts **modifyDateTime** as the parameter to query whether the system time modification capability is disabled.

 |
| disabled\_printer | 

[restrictions.setDisallowedPolicy](../ohos-enterprise-restrictions-restrictions/document.md#restrictionssetdisallowedpolicy)

[restrictions.getDisallowedPolicy](../ohos-enterprise-restrictions-restrictions/document.md#restrictionsgetdisallowedpolicy)

 | 

Accepts **printer** as the parameter to disable or enable the printing capability.

Accepts **printer** as the parameter to query whether the printing capability is disabled.

 |
| disabled\_hdc | 

[restrictions.setDisallowedPolicy](../ohos-enterprise-restrictions-restrictions/document.md#restrictionssetdisallowedpolicy)

[restrictions.getDisallowedPolicy](../ohos-enterprise-restrictions-restrictions/document.md#restrictionsgetdisallowedpolicy)

 | 

Accepts **hdc** as the parameter to disable or enable the capability of connecting to and debugging the device through hdc.

Accepts **hdc** as the parameter to query whether the capability of connecting and debugging the device through hdc is disabled.

 |
| disable\_microphone | 

[restrictions.setDisallowedPolicy](../ohos-enterprise-restrictions-restrictions/document.md#restrictionssetdisallowedpolicy)

[restrictions.getDisallowedPolicy](../ohos-enterprise-restrictions-restrictions/document.md#restrictionsgetdisallowedpolicy)

 | 

Accepts **microphone** as the parameter to disable or enable the microphone capability.

Accepts **microphone** as the parameter to query whether the microphone is disabled.

 |
| fingerprint\_auth | 

[restrictions.setDisallowedPolicy](../ohos-enterprise-restrictions-restrictions/document.md#restrictionssetdisallowedpolicy)

[restrictions.getDisallowedPolicy](../ohos-enterprise-restrictions-restrictions/document.md#restrictionsgetdisallowedpolicy)

[restrictions.setDisallowedPolicyForAccount](../ohos-enterprise-restrictions-restrictions/document.md#restrictionssetdisallowedpolicyforaccount14)

[restrictions.getDisallowedPolicyForAccount](../ohos-enterprise-restrictions-restrictions/document.md#restrictionsgetdisallowedpolicyforaccount14)

 | 

Accepts **fingerprint** as the parameter to disable or enable fingerprint authentication.

Accepts **fingerprint** as the parameter to query whether fingerprint authentication is disabled.

Accepts **fingerprint** as the parameter to disable or enable fingerprint authentication for a specified user.

Accepts **fingerprint** as the parameter to query whether fingerprint authentication is disabled for a specified user.

 |
| disable\_usb | 

[restrictions.setDisallowedPolicy](../ohos-enterprise-restrictions-restrictions/document.md#restrictionssetdisallowedpolicy)

[restrictions.getDisallowedPolicy](../ohos-enterprise-restrictions-restrictions/document.md#restrictionsgetdisallowedpolicy)

 | 

Accepts **usb** as the parameter to disable or enable the USB capability.

Accepts **usb** as the parameter to query whether the USB capability is disabled.

 |
| disable\_wifi | 

[restrictions.setDisallowedPolicy](../ohos-enterprise-restrictions-restrictions/document.md#restrictionssetdisallowedpolicy)

[restrictions.getDisallowedPolicy](../ohos-enterprise-restrictions-restrictions/document.md#restrictionsgetdisallowedpolicy)

 | 

Accepts **wifi** as the parameter to disable or enable the Wi-Fi capability.

Accepts **wifi** as the parameter to query whether Wi-Fi is disabled.

 |
| disallowed\_tethering | 

[restrictions.setDisallowedPolicy](../ohos-enterprise-restrictions-restrictions/document.md#restrictionssetdisallowedpolicy)

[restrictions.getDisallowedPolicy](../ohos-enterprise-restrictions-restrictions/document.md#restrictionsgetdisallowedpolicy)

 | 

Accepts **tethering** as the parameter to disable or enable network sharing.

Accepts **tethering** as the parameter to query whether the network sharing capability is disabled.

 |
| inactive\_user\_freeze | 

[restrictions.setDisallowedPolicy](../ohos-enterprise-restrictions-restrictions/document.md#restrictionssetdisallowedpolicy)

[restrictions.getDisallowedPolicy](../ohos-enterprise-restrictions-restrictions/document.md#restrictionsgetdisallowedpolicy)

 | 

Accepts **inactiveUserFreeze** as the parameter to freeze or unfreeze inactive users.

Accepts **inactiveUserFreeze** as the parameter to query whether inactive users are frozen.

 |
| snapshot\_skip | 

[restrictions.addDisallowedListForAccount](../ohos-enterprise-restrictions-restrictions/document.md#restrictionsadddisallowedlistforaccount14)

[restrictions.removeDisallowedListForAccount](../ohos-enterprise-restrictions-restrictions/document.md#restrictionsremovedisallowedlistforaccount14)

[restrictions.getDisallowedListForAccount](../ohos-enterprise-restrictions-restrictions/document.md#restrictionsgetdisallowedlistforaccount14)

 | 

Accepts **snapshotSkip** as the parameter to add applications with screen snapshot disabled.

Accepts **snapshotSkip** as the parameter to remove the applications with screen snapshot disabled.

Accepts **snapshotSkip** as the parameter to obtain the applications with screen snapshot disabled.

 |
| password\_policy | 

[securityManager.setPasswordPolicy](../ohos-enterprise-securitymanager-security-management/document.md#securitymanagersetpasswordpolicy)

[securityManager.getPasswordPolicy](../ohos-enterprise-securitymanager-security-management/document.md#securitymanagergetpasswordpolicy)

 | 

Sets the device screen lock password policy.

Obtains the device screen lock password policy.

 |
| clipboard\_policy | 

[securityManager.setAppClipboardPolicy](../ohos-enterprise-securitymanager-security-management/document.md#securitymanagersetappclipboardpolicy)

[securityManager.getAppClipboardPolicy](../ohos-enterprise-securitymanager-security-management/document.md#securitymanagergetappclipboardpolicy)

 | 

Sets the device clipboard policy.

Obtains the device clipboard policy.

 |
| watermark\_image\_policy | 

[securityManager.setWatermarkImage](../ohos-enterprise-securitymanager-security-management/document.md#securitymanagersetwatermarkimage14)

[securityManager.cancelWatermarkImage](../ohos-enterprise-securitymanager-security-management/document.md#securitymanagercancelwatermarkimage14)

 | 

Sets the watermark policy. Currently, this feature is available only for PCs/2-in-1 devices.

Cancels the watermark policy. Currently, this feature is available only for PCs/2-in-1 devices.

 |
| ntp\_server | 

[systemManager.setNTPServer](../ohos-enterprise-systemmanager-system-management/document.md#systemmanagersetntpserver)

[systemManager.getNTPServer](../ohos-enterprise-systemmanager-system-management/document.md#systemmanagergetntpserver)

 | 

Sets the NTP server policy.

Obtains the NTP server information.

 |
| set\_update\_policy | 

[systemManager.setOtaUpdatePolicy](../ohos-enterprise-systemmanager-system-management/document.md#systemmanagersetotaupdatepolicy)

[systemManager.getOtaUpdatePolicy](../ohos-enterprise-systemmanager-system-management/document.md#systemmanagergetotaupdatepolicy)

 | 

Sets the update policy.

Obtains the update policy.

 |
| notify\_upgrade\_packages | 

[systemManager.notifyUpdatePackages](../ohos-enterprise-systemmanager-system-management/document.md#systemmanagernotifyupdatepackages)

[systemManager.getUpdateResult](../ohos-enterprise-systemmanager-system-management/document.md#systemmanagergetupdateresult)

 | 

Notifies the system of the update packages.

Obtains the system update result.

 |
| allowed\_usb\_devices | 

[usbManager.addAllowedUsbDevices](../ohos-enterprise-usbmanager-usb-management/document.md#usbmanageraddallowedusbdevices)

[usbManager.removeAllowedUsbDevices](../ohos-enterprise-usbmanager-usb-management/document.md#usbmanagerremoveallowedusbdevices)

[usbManager.getAllowedUsbDevices](../ohos-enterprise-usbmanager-usb-management/document.md#usbmanagergetallowedusbdevices)

 | 

Adds allowed USB devices.

Removes allowed USB devices.

Obtains allowed USB devices.

 |
| usb\_read\_only | 

[usbManager.setUsbStorageDeviceAccessPolicy](../ohos-enterprise-usbmanager-usb-management/document.md#usbmanagersetusbstoragedeviceaccesspolicy)

[usbManager.getUsbStorageDeviceAccessPolicy](../ohos-enterprise-usbmanager-usb-management/document.md#usbmanagergetusbstoragedeviceaccesspolicy)

 | 

Sets the USB storage device access policy.

Obtains the USB storage device access policy.

 |
| disallowed\_usb\_devices | 

[usbManager.addDisallowedUsbDevices](../ohos-enterprise-usbmanager-usb-management/document.md#usbmanageradddisallowedusbdevices14)

[usbManager.removeDisallowedUsbDevices](../ohos-enterprise-usbmanager-usb-management/document.md#usbmanagerremovedisallowedusbdevices14)

[usbManager.getDisallowedUsbDevices](../ohos-enterprise-usbmanager-usb-management/document.md#usbmanagergetdisallowedusbdevices14)

 | 

Adds disallowed USB device types.

Removes disallowed USB device types.

Obtains disallowed USB device types.

 |
| disallowed\_sms | 

[restrictions.setDisallowedPolicy](../ohos-enterprise-restrictions-restrictions/document.md#restrictionssetdisallowedpolicy)

[restrictions.getDisallowedPolicy](../ohos-enterprise-restrictions-restrictions/document.md#restrictionsgetdisallowedpolicy)

 | 

Accepts **sms** as the parameter to disable or enable the capability to receive and send SMS messages. Currently, this feature is supported only on smartphones and tablets.

Accepts **sms** as the parameter to check whether the capability to receive and send SMS messages is disabled. Currently, this feature is supported only on smartphones and tablets.

 |
| disallowed\_mms | 

[restrictions.setDisallowedPolicy](../ohos-enterprise-restrictions-restrictions/document.md#restrictionssetdisallowedpolicy)

[restrictions.getDisallowedPolicy](../ohos-enterprise-restrictions-restrictions/document.md#restrictionsgetdisallowedpolicy)

 | 

Accepts **mms** as the parameter to disable or enable the capability to receive and send MMS messages. Currently, this feature is supported only on smartphones and tablets.

Accepts **mms** as the parameter to check whether the capability to receive and send MMS messages is disabled. Currently, this feature is supported only on smartphones and tablets.

 |
| disable\_backup\_and\_restore | 

[restrictions.setDisallowedPolicy](../ohos-enterprise-restrictions-restrictions/document.md#restrictionssetdisallowedpolicy)

[restrictions.getDisallowedPolicy](../ohos-enterprise-restrictions-restrictions/document.md#restrictionsgetdisallowedpolicy)

 | 

Accepts **backupAndRestore** as the parameter to disable or enable the backup and restore capability. Currently, this feature is supported only on smartphones and tablets.

Accepts **backupAndRestore** as the parameter to check whether the backup and restore capability is disabled. Currently, this feature is supported only on smartphones and tablets.

 |
| installed\_bundle\_info\_list | [bundleManager.getInstalledBundleList](../ohos-enterprise-bundlemanager-bundle-management/document.md#bundlemanagergetinstalledbundlelist20) | Obtains the applications installed by a specified user on a device. |
| clear\_up\_application\_data | [applicationManager.clearUpApplicationData](../ohos-enterprise-applicationmanager-application-management/document.md#applicationmanagerclearupapplicationdata20) | Clears all application data. |
| disallow\_unmute\_device | 

[restrictions.setDisallowedPolicy](../ohos-enterprise-restrictions-restrictions/document.md#restrictionssetdisallowedpolicy)

[restrictions.getDisallowedPolicy](../ohos-enterprise-restrictions-restrictions/document.md#restrictionsgetdisallowedpolicy)

 | 

Accepts **unmuteDevice** as the parameter to disable or enable audio playback of the device.

Accepts **unmuteDevice** as the parameter to check whether audio playback of the device is disabled.

 |
| disabled\_hdc\_remote | 

[restrictions.setDisallowedPolicy](../ohos-enterprise-restrictions-restrictions/document.md#restrictionssetdisallowedpolicy)

[restrictions.getDisallowedPolicy](../ohos-enterprise-restrictions-restrictions/document.md#restrictionsgetdisallowedpolicy)

 | 

Accepts **hdcRemote** as the parameter to disable or enable the device's capability of debugging other devices through hdc.

Accepts **hdcRemote** as the parameter to check whether the device's capability of debugging other devices through hdc is disabled.

 |
