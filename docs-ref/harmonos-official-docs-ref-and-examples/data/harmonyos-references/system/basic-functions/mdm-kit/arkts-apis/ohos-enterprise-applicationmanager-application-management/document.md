# @ohos.enterprise.applicationManager (Application Management)

The **applicationManager** module provides application management capabilities, including adding, removing, and obtaining the applications that are forbidden to run.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/YwVOqWvHQLG3smeU9GVtZg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062405Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=233F0C8D251371E9E8F41812FEF98CF8AFBDA1E7B090B4639FC8287054ECE9A8)

The initial APIs of this module are supported since API version 12. Newly added APIs will be marked with a superscript to indicate their earliest API version.

The APIs of this module can be used only in the stage model.

The APIs of this module can be called only by a device administrator application that is enabled. For details, see [MDM Kit Development](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/mdm-kit-guide). The [applicationManager.isAppKioskAllowed](#applicationmanagerisappkioskallowed20) API is available to all applications.

#### Modules to Import

import { applicationManager } from '@kit.MDMKit';

#### applicationManager.addDisallowedRunningBundlesSync

addDisallowedRunningBundlesSync(admin: Want, appIds: Array<string>, accountId?: number): void

Adds the applications that are not allowed to run by the current or specified user. From API version 21, if the allowed application list [addallowedRunningBundles](#applicationmanageraddallowedrunningbundles21) is not empty, the prohibited application list cannot be added using this API. Otherwise, the error code 9200010 is reported.

**Required permissions**: ohos.permission.ENTERPRISE\_MANAGE\_APPLICATION

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| appIds | Array<string> | Yes | 
IDs of the applications to add.

Note: From API version 21 onwards, the **appId** and **appIdentifier** of the app can be passed. **appIdentifier** is recommended. In API version 20 and earlier versions, only **appId** can be passed.

 |
| accountId | number | No | 

Account ID, which must be greater than or equal to 0.

You can call [getOsAccountLocalId](../../../basic-services-kit/arkts-apis/account-management/ohos-account-osaccount-system-account-management/document.md#getosaccountlocalid9-1) of @ohos.account.osAccount to obtain the ID.

\- If **accountId** is passed in, this API applies to the specified user.

\- If **accountId** is not passed in, this API applies to the current user.

 |

**Error codes**

For details about the error codes, see [Enterprise Device Management Error Codes](../../error-codes/enterprise-device-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9200010 | A conflict policy has been configured. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { applicationManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace it as required.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
// Replace it as required.
let appIds: Array<string> = \['com.example.\*\*\*\*\*\*\_\*\*\*\*\*\*/\*\*\*\*\*\*5t5CoBM='\];

try {
  applicationManager.addDisallowedRunningBundlesSync(wantTemp, appIds);
  console.info('Succeeded in adding disallowed running bundles.');
} catch (err) {
  console.error(\`Failed to add disallowed running bundles. Code is ${err.code}, message is ${err.message}\`);
}

#### applicationManager.removeDisallowedRunningBundlesSync

removeDisallowedRunningBundlesSync(admin: Want, appIds: Array<string>, accountId?: number): void

Removes the applications that are not allowed to run by the current user or specified user.

**Required permissions**: ohos.permission.ENTERPRISE\_MANAGE\_APPLICATION

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| appIds | Array<string> | Yes | 
IDs of the applications to add.

Note: Since API version 21, elements in the array can use [appId](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/common-problem-of-application#what-is-appid) and [appIdentifier](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/common-problem-of-application#what-is-appidentifier). Only the input **appId** or **appIdentifier** is removed. **appIdentifier** or **appId** of the same app will not be removed. In API version 20 and earlier versions, only **appId** can be transferred.

 |
| accountId | number | No | 

Account ID, which must be greater than or equal to 0.

You can call [getOsAccountLocalId](../../../basic-services-kit/arkts-apis/account-management/ohos-account-osaccount-system-account-management/document.md#getosaccountlocalid9-1) of @ohos.account.osAccount to obtain the ID.

\- If **accountId** is passed in, this API applies to the specified user.

\- If **accountId** is not passed in, this API applies to the current user.

 |

**Error codes**

For details about the error codes, see [Enterprise Device Management Error Codes](../../error-codes/enterprise-device-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { applicationManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace it as required.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
// Replace it as required.
let appIds: Array<string> = \['com.example.\*\*\*\*\*\*\_\*\*\*\*\*\*/\*\*\*\*\*\*5t5CoBM='\];

try {
  applicationManager.removeDisallowedRunningBundlesSync(wantTemp, appIds);
  console.info('Succeeded in removing disallowed running bundles.');
} catch (err) {
  console.error(\`Failed to remove disallowed running bundles. Code is ${err.code}, message is ${err.message}\`);
}

#### applicationManager.getDisallowedRunningBundlesSync

getDisallowedRunningBundlesSync(admin: Want, accountId?: number): Array<string>

Obtains applications that are not allowed to run by the current user or specified user.

**Required permissions**: ohos.permission.ENTERPRISE\_MANAGE\_APPLICATION

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| accountId | number | No | 
Account ID, which must be greater than or equal to 0.

You can call [getOsAccountLocalId](../../../basic-services-kit/arkts-apis/account-management/ohos-account-osaccount-system-account-management/document.md#getosaccountlocalid9-1) of @ohos.account.osAccount to obtain the ID.

\- If **accountId** is passed in, this API applies to the specified user.

\- If **accountId** is not passed in, this API applies to the current user.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Array<string> | 
Applications that are not allowed to run by the current user or specified user.

Note: For API version 20 and earlier versions, the return value is the **appId** list. In API version 21 and later versions, the return value is the **appId** or **appIdentifier** list.

 |

**Error codes**

For details about the error codes, see [Enterprise Device Management Error Codes](../../error-codes/enterprise-device-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { applicationManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace it as required.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  let result: Array<string> = applicationManager.getDisallowedRunningBundlesSync(wantTemp);
  console.info(\`Succeeded in getting disallowed running bundles, result : ${JSON.stringify(result)}\`);
} catch (err) {
  console.error(\`Failed to get disallowed running bundles. Code is ${err.code}, message is ${err.message}\`);
}

#### applicationManager.addAllowedRunningBundles21+

addAllowedRunningBundles(admin: Want, appIdentifiers: Array<string>, accountId: number): void

Adds the applications that are allowed to run under specified users.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/obcECPr-RQi1uQwqbHeVsQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062405Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A6FFF2C4F85DFEE478752AA86C1A9704A5F73CFA50C616AEAF510198BEC99AFA)

1.  Most APIs provided by MDM Kit are available only to MDM applications. When using this API, add the MDM application to the application running trustlist. Otherwise, the MDM application will be prohibited from running, blocking the API call. For details about whether the API is open only to MDM applications, see the module description.
    
2.  If the application running blocklist is not empty, this API cannot be used to add applications to the running trustlist. Otherwise, the error code 9200010 is reported. APIs related to the application running blocklist include [addDisallowedRunningBundlesSync](#applicationmanageradddisallowedrunningbundlessync).
    
3.  This API only takes effect for third-party applications. System applications are not subject to this list and are allowed to run by default.
    

**Required permissions**: ohos.permission.ENTERPRISE\_MANAGE\_APPLICATION

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| appIdentifiers | Array<string> | Yes | 
Array of app unique identifiers. You can obtain **bundleInfo.signatureInfo.appIdentifier** through the [bundleManager.getinstalledbundlelist](../ohos-enterprise-bundlemanager-bundle-management/document.md#bundlemanagergetinstalledbundlelist20) API.

Value range:

\- The total number of entries in this list for a single user must not exceed 200. For example, if 50 entries have been set for user 100 and none for user 101, user 100 can add 150 more entries, while user 101 can add up to 200 entries.

 |
| accountId | number | Yes | 

Account ID, which must be greater than or equal to 0.

You can call [getOsAccountLocalId](../../../basic-services-kit/arkts-apis/account-management/ohos-account-osaccount-system-account-management/document.md#getosaccountlocalid9-1) of @ohos.account.osAccount to obtain the ID.

 |

**Error codes**

For details about the error codes, see [Enterprise Device Management Error Codes](../../error-codes/enterprise-device-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9200010 | A conflict policy has been configured. |
| 9200012 | Parameter verification failed. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**Example**

import { applicationManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace it as required.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
// Replace it as required.
let appIdentifiers: Array<string> = \['0123456789123456789'\];

try {
  applicationManager.addAllowedRunningBundles(wantTemp, appIdentifiers, 100);
  console.info('Succeeded in adding allowed running bundles.');
} catch (err) {
  console.error(\`Failed to add allowed running bundles. Code is ${err.code}, message is ${err.message}\`);
}

#### applicationManager.removeAllowedRunningBundles21+

removeAllowedRunningBundles(admin: Want, appIdentifiers: Array<string>, accountId: number): void

Removes the applications that are allowed to run by the specified user.

**Required permissions**: ohos.permission.ENTERPRISE\_MANAGE\_APPLICATION

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| appIdentifiers | Array<string> | Yes | Array of unique identifiers of an app. You can obtain the **bundleInfo.signatureInfo.appIdentifier** by calling the [bundleManager.getinstalledbundlelist](../ohos-enterprise-bundlemanager-bundle-management/document.md#bundlemanagergetinstalledbundlelist20) API. Value range: The array length cannot exceed 200. |
| accountId | number | Yes | 
Account ID, which must be greater than or equal to 0.

You can call [getOsAccountLocalId](../../../basic-services-kit/arkts-apis/account-management/ohos-account-osaccount-system-account-management/document.md#getosaccountlocalid9-1) of @ohos.account.osAccount to obtain the ID.

 |

**Error codes**

For details about the error codes, see [Enterprise Device Management Error Codes](../../error-codes/enterprise-device-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9200012 | Parameter verification failed. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**Example**

import { applicationManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace it as required.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
// Replace it as required.
let appIdentifiers: Array<string> = \['0123456789123456789'\];

try {
  applicationManager.removeAllowedRunningBundles(wantTemp, appIdentifiers, 100);
  console.info('Succeeded in removing allowed running bundles.');
} catch (err) {
  console.error(\`Failed to remove allowed running bundles. Code is ${err.code}, message is ${err.message}\`);
}

#### applicationManager.getAllowedRunningBundles21+

getAllowedRunningBundles(admin: Want, accountId: number): Array<string>

Obtains the list of applications allowed to run by a specified user.

**Required permissions**: ohos.permission.ENTERPRISE\_MANAGE\_APPLICATION

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| accountId | number | Yes | 
Account ID, which must be greater than or equal to 0.

You can call [getOsAccountLocalId](../../../basic-services-kit/arkts-apis/account-management/ohos-account-osaccount-system-account-management/document.md#getosaccountlocalid9-1) of @ohos.account.osAccount to obtain the ID.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Array<string> | List of applications allowed to run by a specified user. |

**Error codes**

For details about the error codes, see [Enterprise Device Management Error Codes](../../error-codes/enterprise-device-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**Example**

import { applicationManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace it as required.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  let result: Array<string> = applicationManager.getAllowedRunningBundles(wantTemp, 100);
  console.info(\`Succeeded in getting allowed running bundles, result : ${JSON.stringify(result)}\`);
} catch (err) {
  console.error(\`Failed to get allowed running bundles. Code is ${err.code}, message is ${err.message}\`);
}

#### applicationManager.addAutoStartApps

addAutoStartApps(admin: Want, autoStartApps: Array<Want>): void

Adds the auto-start applications for the current user. Applications added to the auto-start list via this API cannot be manually disabled for auto-start by users on the device(users can disable automatic application launch by choosing Settings > Apps & services > Launch manager). However, they can be removed from the auto-start list using the [removeAutoStartApps](#applicationmanagerremoveautostartapps) API.

**Required permissions**: ohos.permission.ENTERPRISE\_MANAGE\_APPLICATION

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Device behavior differences**: For API version 20 and earlier versions, this API can be properly called on PCs/2-in-1 devices and does not work on other devices. This API can be used on phones, tablets, PCs/2-in-1 devices since API version 21.

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| autoStartApps | Array<[Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md)\> | Yes | Array of auto-start applications. The maximum array length is 10. For example, if there are already 5 applications in the list, a maximum of 5 more can be added via this API. **Want** must contain **bundleName** and **abilityName**. The ability can be UIAbility or ServiceExtensionAbility. If the value of **exported** in the [abilities](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/module-configuration-file#abilities) tag is **false**, the ability cannot be started. |

**Error codes**

For details about the error codes, see [Enterprise Device Management Error Codes](../../error-codes/enterprise-device-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { applicationManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace it as required.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
let autoStartApps: Array<Want> = \[
  {
    // Replace it as required.
    bundleName: 'com.example.autoStartApplication',
    abilityName: 'EntryAbility'
  }
\];

try {
  applicationManager.addAutoStartApps(wantTemp, autoStartApps);
  console.info('Succeeded in adding auto start applications.');
} catch(err) {
  console.error(\`Failed to add auto start applications. Code: ${err.code}, message: ${err.message}\`);
}

#### applicationManager.removeAutoStartApps

removeAutoStartApps(admin: Want, autoStartApps: Array<Want>): void

Removes the auto-start applications for the current user.

**Required permissions**: ohos.permission.ENTERPRISE\_MANAGE\_APPLICATION

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Device behavior differences**: For API version 20 and earlier versions, this API can be properly called on PCs/2-in-1 devices and does not work on other devices. This API can be used on phones, tablets, PCs/2-in-1 devices since API version 21.

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| autoStartApps | Array<[Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md)\> | Yes | Array of auto-start applications. **Want** must contain **bundleName** and **abilityName**. The ability can be UIAbility or ServiceExtensionAbility. If the value of **exported** in the [abilities](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/module-configuration-file#abilities) tag is **false**, the ability cannot be started. |

**Error codes**

For details about the error codes, see [Enterprise Device Management Error Codes](../../error-codes/enterprise-device-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { applicationManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace it as required.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
let autoStartApps: Array<Want> = \[
  {
    // Replace it as required.
    bundleName: 'com.example.autoStartApplication',
    abilityName: 'EntryAbility'
  }
\];

try {
  applicationManager.removeAutoStartApps(wantTemp, autoStartApps);
  console.info('Succeeded in removing auto start applications.');
} catch(err) {
  console.error(\`Failed to remove auto start applications. Code: ${err.code}, message: ${err.message}\`);
}

#### applicationManager.removeAutoStartApps20+

removeAutoStartApps(admin: Want, autoStartApps: Array<Want>, accountId: number): void

Removes the specified application from the auto-start application list of a specified user.

**Required permissions**: ohos.permission.ENTERPRISE\_MANAGE\_APPLICATION

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Device behavior differences**: For API version 20 and earlier versions, this API can be properly called on PCs/2-in-1 devices and does not work on other devices. This API can be used on phones, tablets, PCs/2-in-1 devices since API version 21.

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| autoStartApps | Array<[Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md)\> | Yes | Array of auto-start applications. **Want** must contain **bundleName** and **abilityName**. |
| accountId | number | Yes | 
Account ID, which must be greater than or equal to 0.

You can call [getOsAccountLocalId](../../../basic-services-kit/arkts-apis/account-management/ohos-account-osaccount-system-account-management/document.md#getosaccountlocalid9-1) of @ohos.account.osAccount to obtain the ID.

 |

**Error codes**

For details about the error codes, see [Enterprise Device Management Error Codes](../../error-codes/enterprise-device-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**Example**

import { applicationManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';
 
let wantTemp: Want = {
  // Replace it as required.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

let autoStartApps: Array<Want> = \[
  // Replace it as required.
  {
    bundleName: 'com.example.autoStartApplication',
    abilityName: 'EntryAbility'
  }
\];

try {
  applicationManager.removeAutoStartApps(wantTemp, autoStartApps, 100);
  console.info('Succeeded in removing auto start applications.');
} catch(err) {
  console.error(\`Failed to remove auto start applications. Code: ${err.code}, message: ${err.message}\`);
}

#### applicationManager.getAutoStartApps

getAutoStartApps(admin: Want): Array<Want>

Checks the auto-start applications for the current user.

**Required permissions**: ohos.permission.ENTERPRISE\_MANAGE\_APPLICATION

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Device behavior differences**: For API version 20 and earlier versions, this API can be properly called on PCs/2-in-1 devices and does not work on other devices. This API can be used on phones, tablets, PCs/2-in-1 devices since API version 21.

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |

**Return value**

| Type | Description |
| :-- | :-- |
| Array<[Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md)\> | List of the auto-start applications obtained. |

**Error codes**

For details about the error codes, see [Enterprise Device Management Error Codes](../../error-codes/enterprise-device-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { applicationManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace it as required.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  let res: Array<Want> = applicationManager.getAutoStartApps(wantTemp);
  console.info(\`Succeeded in adding auto start apps: ${JSON.stringify(res)}\`);
} catch(err) {
  console.error(\`Failed to auto start apps. Code: ${err.code}, message: ${err.message}\`);
}

#### applicationManager.addAutoStartApps20+

addAutoStartApps(admin: Want, autoStartApps: Array<Want>, accountId: number, disallowModify: boolean): void

Adds a list of applications that automatically start upon system startup for a specified user, and sets whether to forbid the user to manually cancel the automatic startup of applications(users can disable automatic application launch by choosing Settings > Apps & services > Launch manager).

Applications can be added to the auto-start list via this API and the [addAutoStartApps](#applicationmanageraddautostartapps) API. Settings from both APIs can take effect simultaneously. For a single user, the auto-start list supports a maximum of 10 applications. For example, if there are already 3 applications in the current list, a maximum of 7 more can be added for the user via this API.

**Required permissions**: ohos.permission.ENTERPRISE\_MANAGE\_APPLICATION

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Device behavior differences**: For API version 20 and earlier versions, this API can be properly called on PCs/2-in-1 devices and does not work on other devices. This API can be used on phones, tablets, PCs/2-in-1 devices since API version 21.

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| autoStartApps | Array<[Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md)\> | Yes | Array of auto-start applications. The array can contain a maximum of 10 applications. **Want** must contain **bundleName** and **abilityName**. The ability can be UIAbility or ServiceExtensionAbility. If the value of **exported** in the [abilities](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/module-configuration-file#abilities) tag is **false**, the ability cannot be started. |
| accountId | number | Yes | 
Account ID, which must be greater than or equal to 0.

You can call [getOsAccountLocalId](../../../basic-services-kit/arkts-apis/account-management/ohos-account-osaccount-system-account-management/document.md#getosaccountlocalid9-1) of @ohos.account.osAccount to obtain the ID.

 |
| disallowModify | boolean | Yes | Whether to disable the user from manually disabling automatic application startup. The value **true** indicates that auto-start is disabled, and the value **false** indicates the opposite.If the value is set to false, users can disable automatic application launch by choosing Settings > Apps & services > Launch manager. |

**Error codes**

For details about the error codes, see [Enterprise Device Management Error Codes](../../error-codes/enterprise-device-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**Example**

import { applicationManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace it as required.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

let autoStartApps: Array<Want> = \[
  // Replace it as required.
  {
    bundleName: 'com.example.autoStartApplication',
    abilityName: 'EntryAbility'
  }
\];

try {
  applicationManager.addAutoStartApps(wantTemp, autoStartApps, 100, true);
  console.info('Succeeded in adding auto start applications and set disllowModify.');
} catch(err) {
  console.error(\`Failed to add auto start applications and set disallowModify. Code: ${err.code}, message: ${err.message}\`);
}

#### applicationManager.getAutoStartApps20+

getAutoStartApps(admin: Want, accountId: number): Array<Want>

Checks the auto-start applications for the specified user.

**Required permissions**: ohos.permission.ENTERPRISE\_MANAGE\_APPLICATION

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Device behavior differences**: For API version 20 and earlier versions, this API can be properly called on PCs/2-in-1 devices and does not work on other devices. This API can be used on phones, tablets, PCs/2-in-1 devices since API version 21.

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| accountId | number | Yes | 
Account ID, which must be greater than or equal to 0.

You can call [getOsAccountLocalId](../../../basic-services-kit/arkts-apis/account-management/ohos-account-osaccount-system-account-management/document.md#getosaccountlocalid9-1) of @ohos.account.osAccount to obtain the ID.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Array<[Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md)\> | List of the auto-start applications obtained. |

**Error codes**

For details about the error codes, see [Enterprise Device Management Error Codes](../../error-codes/enterprise-device-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**Example**

import { applicationManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace it as required.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  let res: Array<Want> = applicationManager.getAutoStartApps(wantTemp, 100);
  console.info(\`Succeeded in getting auto start apps: ${JSON.stringify(res)}\`);
} catch(err) {
  console.error(\`Failed to get auto start apps. Code: ${err.code}, message: ${err.message}\`);
}

#### applicationManager.isModifyAutoStartAppsDisallowed20+

isModifyAutoStartAppsDisallowed(admin: Want, autoStartApp: Want, accountId: number): boolean

Checks whether the auto-start of an application is disabled for the specified user.

**Required permissions**: ohos.permission.ENTERPRISE\_MANAGE\_APPLICATION

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Device behavior differences**: For API version 20 and earlier versions, this API can be properly called on PCs/2-in-1 devices and does not work on other devices. This API can be used on phones, tablets, PCs/2-in-1 devices since API version 21.

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| autoStartApp | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | Auto-start applications to add. **Want** must contain **bundleName** and **abilityName**. |
| accountId | number | Yes | 
Account ID, which must be greater than or equal to 0.

You can call [getOsAccountLocalId](../../../basic-services-kit/arkts-apis/account-management/ohos-account-osaccount-system-account-management/document.md#getosaccountlocalid9-1) of @ohos.account.osAccount to obtain the ID.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Whether to disable the user from disabling automatic application startup. The value **true** indicates that auto-start is disabled, and the value **false** indicates the opposite. |

**Error codes**

For details about the error codes, see [Enterprise Device Management Error Codes](../../error-codes/enterprise-device-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**Example**

import { applicationManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace it as required.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

let autoStartApp: Want = {
  // Replace it as required.
  bundleName: 'com.example.autoStartApplication',
  abilityName: 'EntryAbility'
};

try {
  let res: boolean = applicationManager.isModifyAutoStartAppsDisallowed(wantTemp, autoStartApp, 100);
  console.info(\`Succeeded in getting disallow modify auto start app: ${JSON.stringify(res)}\`);
} catch(err) {
  console.error(\`Failed to get disallow modify auto start app. Code: ${err.code}, message: ${err.message}\`);
}

#### applicationManager.addKeepAliveApps14+

addKeepAliveApps(admin: Want, bundleNames: Array<string>, accountId: number): void

Adds applications to the keep-alive list; once added, the application processes will be kept alive automatically. After the device is powered on or the application is killed, the system will proactively restart these application processes. The keep-alive status takes effect only after the application has accessed the [Status Bar Extension Kit](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/statusbar-extension-guide). Applications added to the keep-alive list via this API cannot be manually removed from keep-alive status by users on the device(users can cancel the keep-alive status by choosing Settings > Apps & services > Background apps). However, they can be removed from the keep-alive list using the [removeKeepAliveApps](#applicationmanagerremovekeepaliveapps14) API. If applications are disallowed to run by calling [addDisallowedRunningBundlesSync](#applicationmanageradddisallowedrunningbundlessync), they cannot be kept alive. Otherwise, error code 9200010 will be reported.

**Required permissions**: ohos.permission.ENTERPRISE\_MANAGE\_APPLICATION

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Device behavior differences**: This API can be properly called on PCs/2-in-1 devices. If it is called on other device types, error code 801 is returned.

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| bundleNames | Array<string> | Yes | Array of application bundle names, which specifies the applications to be kept alive. A maximum of 5 applications are supported.The application must be installed under a common user and has accessed the [Status Bar Extension Kit](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/statusbar-extension-guide). Otherwise, error code 9201005 is reported. |
| accountId | number | Yes | 
Account ID, which must be greater than or equal to 0.

You can call [getOsAccountLocalId](../../../basic-services-kit/arkts-apis/account-management/ohos-account-osaccount-system-account-management/document.md#getosaccountlocalid9-1) of @ohos.account.osAccount to obtain the ID.

 |

**Error codes**

For details about the error codes, see [Enterprise Device Management Error Codes](../../error-codes/enterprise-device-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9200010 | A conflict policy has been configured. |
| 9201005 | Add keep alive applications failed. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |

**Example**

import { applicationManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace it as required.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
// Replace it as required.
let bundleNames: Array<string> = \['com.example.myapplication'\];

try {
  applicationManager.addKeepAliveApps(wantTemp, bundleNames, 100);
  console.info('Succeeded in adding keep alive apps.');
} catch (err) {
  console.error(\`Failed to add keep alive apps. Code is ${err.code}, message is ${err.message}\`);
}

#### applicationManager.addKeepAliveApps20+

addKeepAliveApps(admin: Want, bundleNames: Array<string>, accountId: number, disallowModify: boolean): void

Adds applications to the keep-alive list; once added, the application processes will be kept alive automatically. You can also set whether to disable manual keep-alive cancellation. After the device is powered on or the application is killed, the system will proactively restart these application processes.

Applications can be added to the keep-alive list via this API and the [addKeepAliveApps](#applicationmanageraddkeepaliveapps14) API. Settings from both APIs can take effect simultaneously. For a single user, the keep-alive list supports a maximum of 5 applications. For example, if there are already 3 applications in the current list, a maximum of 2 more can be added for the user via this API.

If applications are disallowed to run by calling [addDisallowedRunningBundlesSync](#applicationmanageradddisallowedrunningbundlessync), they cannot be kept alive. Otherwise, error code 9200010 will be reported.

**Required permissions**: ohos.permission.ENTERPRISE\_MANAGE\_APPLICATION

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Device behavior differences**: This API can be properly called on PCs/2-in-1 devices. If it is called on other device types, error code 801 is returned.

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| bundleNames | Array<string> | Yes | 
Array of application bundle names, which specifies the applications to be kept alive. A maximum of 5 applications are supported.

Applications must be installed under user 1 (a user who supports single-instance running of third-party applications) and have integrated [background services](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-service-extension-ability#implementing-a-background-service); or the application is installed under a common user and has accessed the [Status Bar Extension Kit](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/statusbar-extension-guide). Otherwise, the error code 9201005 will be reported.

 |
| accountId | number | Yes | 

Account ID, which must be greater than or equal to 0.

You can call [getOsAccountLocalId](../../../basic-services-kit/arkts-apis/account-management/ohos-account-osaccount-system-account-management/document.md#getosaccountlocalid9-1) of @ohos.account.osAccount to obtain the ID.

 |
| disallowModify | boolean | Yes | Whether to forbid users to manually cancel the keep-alive status. The value **true** indicates that users are not allowed to manually cancel the keep-alive status, and the value **false** indicates the opposite.If the value is set to false, users can cancel the keep-alive status by choosing Settings > Apps & services > Background apps. |

**Error codes**

For details about the error codes, see [Enterprise Device Management Error Codes](../../error-codes/enterprise-device-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9200010 | A conflict policy has been configured. |
| 9201005 | Add keep alive applications failed. |
| 201 | Permission verification failed.The application does not have the permission required to call the API. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |

**Example**

import { applicationManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace it as required.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

// Replace it as required.
let bundleNames: Array<string> = \['com.example.myapplication'\];

try {
  applicationManager.addKeepAliveApps(wantTemp, bundleNames, 100, true);
  console.info('Succeeded in adding keep alive apps and set disallowModify.');
} catch (err) {
  console.error(\`Failed to add keep alive apps and set disallowModify. Code is ${err.code}, message is ${err.message}\`);
}

#### applicationManager.removeKeepAliveApps14+

removeKeepAliveApps(admin: Want, bundleNames: Array<string>, accountId: number): void

Removes a specified application from the keep-alive list.

**Required permissions**: ohos.permission.ENTERPRISE\_MANAGE\_APPLICATION

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Device behavior differences**: This API takes effect only on PCs/2-in-1 devices and does not work on other devices.

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| bundleNames | Array<string> | Yes | Application bundle name array, which specifies the applications to be kept alive. A maximum of five applications are supported. |
| accountId | number | Yes | 
Account ID, which must be greater than or equal to 0.

You can call [getOsAccountLocalId](../../../basic-services-kit/arkts-apis/account-management/ohos-account-osaccount-system-account-management/document.md#getosaccountlocalid9-1) of @ohos.account.osAccount to obtain the ID.

 |

**Error codes**

For details about the error codes, see [Enterprise Device Management Error Codes](../../error-codes/enterprise-device-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { applicationManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace it as required.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
// Replace it as required.
let bundleNames: Array<string> = \['com.example.myapplication'\];

try {
  applicationManager.removeKeepAliveApps(wantTemp, bundleNames, 100);
  console.info('Succeeded in removing keep alive apps.');
} catch (err) {
  console.error(\`Failed to remove keep alive apps. Code is ${err.code}, message is ${err.message}\`);
}

#### applicationManager.getKeepAliveApps14+

getKeepAliveApps(admin: Want, accountId: number): Array<string>

Obtains the bundle name of the keep-alive application.

**Required permissions**: ohos.permission.ENTERPRISE\_MANAGE\_APPLICATION

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Device behavior differences**: This API takes effect only on PCs/2-in-1 devices and does not work on other devices.

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| accountId | number | Yes | 
Account ID, which must be greater than or equal to 0.

You can call [getOsAccountLocalId](../../../basic-services-kit/arkts-apis/account-management/ohos-account-osaccount-system-account-management/document.md#getosaccountlocalid9-1) of @ohos.account.osAccount to obtain the ID.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Array<string> | Bundle name of the application kept alive for the specified user. |

**Error codes**

For details about the error codes, see [Enterprise Device Management Error Codes](../../error-codes/enterprise-device-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { applicationManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace it as required.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  let result: Array<string> = applicationManager.getKeepAliveApps(wantTemp, 100);
  console.info('Succeeded in getting keep alive apps.');
} catch (err) {
  console.error(\`Failed to get keep alive apps. Code is ${err.code}, message is ${err.message}\`);
}

#### applicationManager.isModifyKeepAliveAppsDisallowed20+

isModifyKeepAliveAppsDisallowed(admin: Want, accountId: number, bundleName: string): boolean

Checks whether the application is forbidden to cancel the keep-alive status.

**Required permissions**: ohos.permission.ENTERPRISE\_MANAGE\_APPLICATION

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Device behavior differences**: This API takes effect only on PCs/2-in-1 devices and does not work on other devices.

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| accountId | number | Yes | 
Account ID, which must be greater than or equal to 0.

You can call [getOsAccountLocalId](../../../basic-services-kit/arkts-apis/account-management/ohos-account-osaccount-system-account-management/document.md#getosaccountlocalid9-1) of @ohos.account.osAccount to obtain the ID.

 |
| bundleName | string | Yes | Bundle name. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Whether to forbid users to manually cancel the keep-alive status. The value **true** indicates that users are not allowed to manually cancel the keep-alive status, and the value **false** indicates the opposite.If the value is set to false, users can cancel the keep-alive status by choosing Settings > Apps & services > Background apps. |

**Error codes**

For details about the error codes, see [Enterprise Device Management Error Codes](../../error-codes/enterprise-device-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**Example**

import { applicationManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace it as required.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

// Replace it as required.
let keepAliveApp: string = 'com.example.keepAliveApplication';

try {
  let res: boolean = applicationManager.isModifyKeepAliveAppsDisallowed(wantTemp, 100, keepAliveApp);
  console.info(\`Succeeded in getting disallow modify keep alive app: ${JSON.stringify(res)}\`);
} catch(err) {
  console.error(\`Failed to get disallow modify keep alive app. Code: ${err.code}, message: ${err.message}\`);
}

#### applicationManager.clearUpApplicationData20+

clearUpApplicationData(admin: Want, bundleName: string, appIndex: number, accountId: number): void

Clears all application data.

**Required permissions**: ohos.permission.ENTERPRISE\_MANAGE\_APPLICATION

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| bundleName | string | Yes | Bundle name of the application whose data needs to be cleared. |
| appIndex | number | Yes | 
Index of the application clone. The value is an integer greater than or equal to 0.

You can call [getAppCloneIdentity](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-bundle-bundlemanager-bundle-management-module/document.md#bundlemanagergetappcloneidentity14) of @ohos.bundle.bundleManager to obtain the index.

 |
| accountId | number | Yes | 

Account ID. The value is an integer greater than or equal to 0.

You can call [getOsAccountLocalId](../../../basic-services-kit/arkts-apis/account-management/ohos-account-osaccount-system-account-management/document.md#getosaccountlocalid9-1) of @ohos.account.osAccount to obtain the ID.

 |

**Error codes**

For details about the error codes, see [Enterprise Device Management Error Codes](../../error-codes/enterprise-device-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**Example**

import { Want } from '@kit.AbilityKit';
import { applicationManager } from '@kit.MDMKit';

let wantTemp: Want = {
  // Replace it as required.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
// Replace it as required.
let bundleName: string = 'com.example.exampleapplication';

try {
  // Replace it as required.
  applicationManager.clearUpApplicationData(wantTemp, bundleName, 0, 100);
  console.info('Succeeded in clearing up application data.');
} catch (err) {
  console.error(\`Failed to clear up application data. Code is ${err.code}, message is ${err.message}\`);
}

#### applicationManager.setAllowedKioskApps20+

setAllowedKioskApps(admin: Want, appIdentifiers: Array<string>): void

Sets applications allowed to run in kiosk mode.

Kiosk mode is a system-level runtime mode that restricts a device to a single application or a set of applications. It controls the lock screen, status bar, gestures, and key features to prevent users from launching other applications or performing other operations on the device.

**Required permissions**: ohos.permission.ENTERPRISE\_SET\_KIOSK

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| appIdentifiers | Array<string> | Yes | Array of [unique identifiers](../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/bundlemanager/bundleinfo/document.md#signatureinfo) of an application. You can call the [bundleManager.getBundleInfo](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-bundle-bundlemanager-bundle-management-module/document.md#bundlemanagergetbundleinfo14-2) API to obtain the **bundleInfo.signatureInfo.appIdentifier**. In case of repeated configuration, the newly configured array will overwrite the old one, with a maximum limit of 200 entries. |

**Error codes**

For details about the error codes, see [Enterprise Device Management Error Codes](../../error-codes/enterprise-device-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**Example**

import { Want } from '@kit.AbilityKit';
import { applicationManager } from '@kit.MDMKit';

let wantTemp: Want = {
  // Replace it as required.
  bundleName: 'com.example.edmtest',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  // Replace it as required.
  let appIdentifiers: Array<string> = \['6917\*\*\*\*3569'\];
  applicationManager.setAllowedKioskApps(wantTemp, appIdentifiers);
  console.info('Succeeded in setting allowed kiosk apps.');
} catch (err) {
  console.error(\`Failed to set allowed kiosk apps. Code is ${err.code}, message is ${err.message}\`);
}

#### applicationManager.getAllowedKioskApps20+

getAllowedKioskApps(admin: Want): Array<string>

Obtains the applications allowed to run in kiosk mode.

**Required permissions**: ohos.permission.ENTERPRISE\_SET\_KIOSK

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |

**Return value**

| Type | Description |
| :-- | :-- |
| Array<string> | List of [unique identifiers](../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/bundlemanager/bundleinfo/document.md#signatureinfo) of an application that can run in kiosk mode. |

**Error codes**

For details about the error codes, see [Enterprise Device Management Error Codes](../../error-codes/enterprise-device-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**Example**

import { Want } from '@kit.AbilityKit';
import { applicationManager } from '@kit.MDMKit';

let wantTemp: Want = {
  // Replace it as required.
  bundleName: 'com.example.edmtest',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  let appIdentifiers: Array<string> = applicationManager.getAllowedKioskApps(wantTemp);
  console.info(\`Succeeded in getting allowed kiosk apps, appIdentifiers: ${JSON.stringify(appIdentifiers)}\`);
} catch (err) {
  console.error(\`Failed to get allowed kiosk apps. Code is ${err.code}, message is ${err.message}\`);
}

#### applicationManager.isAppKioskAllowed20+

isAppKioskAllowed(appIdentifier: string): boolean

Checks whether an application is allowed to run in kiosk mode.

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| appIdentifier | string | Yes | [Unique identifiers](../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/bundlemanager/bundleinfo/document.md#signatureinfo) of an application. You can call the [bundleManager.getBundleInfo](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-bundle-bundlemanager-bundle-management-module/document.md#bundlemanagergetbundleinfo14-2) API to obtain the **bundleInfo.signatureInfo.appIdentifier**. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | The value **true** means the application can run in kiosk mode; the value **false** means the opposite. |

**Example**

import { applicationManager } from '@kit.MDMKit';

try {
  // Replace it as required.
  let isAllowed: boolean = applicationManager.isAppKioskAllowed('6917\*\*\*\*3569');
  console.info(\`Succeeded in querying if the app is allowed kiosk, isAllowed: ${isAllowed}\`);
} catch (err) {
  console.error(\`Failed to query if the app is allowed kiosk. Code is ${err.code}, message is ${err.message}\`);
}

#### applicationManager.setKioskFeatures20+

setKioskFeatures(admin: Want, features: Array<KioskFeature>): void

Sets the features of the kiosk mode. This API is used to control whether the notification center and control panel can be accessed [in kiosk mode](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-kioskmanager-kiosk-mode-management/document.md#kioskmanagerenterkioskmode). In non-kiosk mode, this API can be called normally but does not take effect. It will take effect after kiosk mode is enabled.

**Required permissions**: ohos.permission.ENTERPRISE\_SET\_KIOSK

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Device behavior differences**: This API has no effect on PCs/2-in-1 devices, but can be properly called on phones and tablets.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| features | Array<[KioskFeature](#kioskfeature20)\> | Yes | 
Features of the kiosk mode.

If an empty array is passed, the system will clear all previously configured features and restore kiosk mode to its default state, where capabilities such as the notification center, control panel, and recent tasks panel are disabled.

 |

**Error codes**

For details about the error codes, see [Enterprise Device Management Error Codes](../../error-codes/enterprise-device-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9200012 | Parameter verification failed. |
| 201 | Permission verification failed.The application does not have the permission required to call the API. |

**Example**

import { Want } from '@kit.AbilityKit';
import { applicationManager } from '@kit.MDMKit';

let wantTemp: Want = {
  // Replace it as required.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
let kioskFeatures: Array<applicationManager.KioskFeature> = \[\];
kioskFeatures.push(applicationManager.KioskFeature.ALLOW\_NOTIFICATION\_CENTER);
kioskFeatures.push(applicationManager.KioskFeature.ALLOW\_CONTROL\_CENTER);
try {
  applicationManager.setKioskFeatures(wantTemp, kioskFeatures);
  console.info('Succeeded in setting kiosk feature.');
} catch (err) {
  console.error(\`Failed to set kiosk feature. Code is ${err.code}, message is ${err.message}\`);
}

#### KioskFeature20+

Defines the features of the kiosk mode.

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

| Name | Value | Description |
| :-- | :-- | :-- |
| ALLOW\_NOTIFICATION\_CENTER | 1 | Allow access to the notification center. |
| ALLOW\_CONTROL\_CENTER | 2 | Allow access to the control panel. |

#### applicationManager.addUserNonStopApps22+

addUserNonStopApps(admin: Want, applicationInstances: Array<common.ApplicationInstance>): void

Adds applications to the non-stoppable application list for a specified user. This policy only applies to installed applications. If the parameter list contains uninstalled applications, error code 9200012 will be returned. If an application in the list is uninstalled after the policy is set, the uninstalled application will be removed from the list. Adding an application that already exists in the list will return success, but the application will not be added repeatedly to the policy list.

Non-stoppable applications cannot be closed by swiping up in the task center. After a user taps the application name in **Settings** > **Apps & services** to go to the details page, the forcible stop button is unavailable.

**Required permissions**: ohos.permission.ENTERPRISE\_MANAGE\_APPLICATION

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Device behavior differences**: This API can be called on phones and tablets but has no effect on other devices.

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| applicationInstances | Array<[common.ApplicationInstance](../ohos-enterprise-common-common-module/document.md#applicationinstance)\> | Yes | Array of non-stoppable applications. A maximum of 10 applications can be added to the non-stoppable application list. This limit is not divided among users. Specifically, the total number of such applications added by all users cannot exceed 10. For example, if there are already 3 applications in the current list, a maximum of 7 more can be added for a specified user via this API. |

**Error codes**

For details about the error codes, see [Enterprise Device Management Error Codes](../../error-codes/enterprise-device-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9200012 | Parameter verification failed. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**Example**

import { applicationManager, common } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace it as required.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

let applicationInstances: Array<common.ApplicationInstance> = \[
  // Replace it as required.
  {
    appIdentifier: '0123456789123456789',
    accountId: 100,
    appIndex: 0
  }
\];

try {
  applicationManager.addUserNonStopApps(wantTemp, applicationInstances);
  console.info('Succeeded in adding UserNonStop applications.');
} catch(err) {
  console.error(\`Failed to add UserNonStop applications. Code: ${err.code}, message: ${err.message}\`);
}

#### applicationManager.removeUserNonStopApps22+

removeUserNonStopApps(admin: Want, applicationInstances: Array<common.ApplicationInstance>): void

Removes the non-stoppable application list for a specified user. If the parameter list includes uninstalled applications, the removal will still succeed. Installed applications will be removed from the list, while uninstalled ones will not impact the removal process.

**Required permissions**: ohos.permission.ENTERPRISE\_MANAGE\_APPLICATION

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Device behavior differences**: This API can be called on phones and tablets but has no effect on other devices.

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| applicationInstances | Array<[common.ApplicationInstance](../ohos-enterprise-common-common-module/document.md#applicationinstance)\> | Yes | Array of non-stoppable applications. |

**Error codes**

For details about the error codes, see [Enterprise Device Management Error Codes](../../error-codes/enterprise-device-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9200012 | Parameter verification failed. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**Example**

import { applicationManager, common } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace it as required.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

let applicationInstances: Array<common.ApplicationInstance> = \[
  // Replace it as required.
  {
    appIdentifier: '0123456789123456789',
    accountId: 100,
    appIndex: 0
  }
\];

try {
  applicationManager.removeUserNonStopApps(wantTemp, applicationInstances);
  console.info('Succeeded in removing UserNonStop applications.');
} catch(err) {
  console.error(\`Failed to remove UserNonStop applications. Code: ${err.code}, message: ${err.message}\`);
}

#### applicationManager.getUserNonStopApps22+

getUserNonStopApps(admin: Want): Array<common.ApplicationInstance>

Obtains the non-stoppable application list of all users on the current device.

**Required permissions**: ohos.permission.ENTERPRISE\_MANAGE\_APPLICATION

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Device behavior differences**: This API can be called on phones and tablets but has no effect on other devices.

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |

**Return value**

| Type | Description |
| :-- | :-- |
| Array<[common.ApplicationInstance](../ohos-enterprise-common-common-module/document.md#applicationinstance)\> | Array of non-stoppable applications. |

**Error codes**

For details about the error codes, see [Enterprise Device Management Error Codes](../../error-codes/enterprise-device-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**Example**

import { applicationManager, common } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace it as required.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  let result: Array<common.ApplicationInstance> = applicationManager.getUserNonStopApps(wantTemp);
  console.info(\`Succeeded in getting UserNonStop applications, result : ${JSON.stringify(result)}\`);
} catch(err) {
  console.error(\`Failed to get UserNonStop applications. Code: ${err.code}, message: ${err.message}\`);
}

#### applicationManager.addFreezeExemptedApps22+

addFreezeExemptedApps(admin: Want, applicationInstances: Array<common.ApplicationInstance>): void

Adds applications to the background freeze-exempt application list for a specified user. This policy applies only to installed applications and becomes invalid after the device is restarted. If the parameter list contains uninstalled applications, error code 9200012 will be returned. If an application in the list is uninstalled after the policy is set, the uninstalled application will be removed from the list. Adding an application that already exists in the list will return success, but the application will not be added repeatedly to the policy list.

Freezing operations include suspending the target application, and managing software resource agents, hardware resource agents, and high-power consumption.

**Required permissions**: ohos.permission.ENTERPRISE\_MANAGE\_APPLICATION

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Device behavior differences**: This API can be called on phones and tablets but has no effect on other devices.

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| applicationInstances | Array<[common.ApplicationInstance](../ohos-enterprise-common-common-module/document.md#applicationinstance)\> | Yes | Array of the background freeze-exempt application list. A maximum of 10 applications can be added to the list. This limit is not divided among users. Specifically, the total number of such applications added by all users cannot exceed 10. For example, if there are already 3 applications in the current list, a maximum of 7 more can be added for a specified user via this API. |

**Error codes**

For details about the error codes, see [Enterprise Device Management Error Codes](../../error-codes/enterprise-device-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9200012 | Parameter verification failed. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**Example**

import { applicationManager, common } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace it as required.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

let applicationInstances: Array<common.ApplicationInstance> = \[
  // Replace it as required.
  {
    appIdentifier: '0123456789123456789',
    accountId: 100,
    appIndex: 0
  }
\];

try {
  applicationManager.addFreezeExemptedApps(wantTemp, applicationInstances);
  console.info('Succeeded in adding FreezeExempted applications.');
} catch(err) {
  console.error(\`Failed to add FreezeExempted applications. Code: ${err.code}, message: ${err.message}\`);
}

#### applicationManager.removeFreezeExemptedApps22+

removeFreezeExemptedApps(admin: Want, applicationInstances: Array<common.ApplicationInstance>): void

Removes the background freeze-exempt application list for a specified user. If the parameter list includes uninstalled applications, the removal will still succeed. Installed applications will be removed from the list, while uninstalled ones will not impact the removal process.

**Required permissions**: ohos.permission.ENTERPRISE\_MANAGE\_APPLICATION

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Device behavior differences**: This API can be called on phones and tablets but has no effect on other devices.

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| applicationInstances | Array<[common.ApplicationInstance](../ohos-enterprise-common-common-module/document.md#applicationinstance)\> | Yes | Array of the background freeze-exempt application list. |

**Error codes**

For details about the error codes, see [Enterprise Device Management Error Codes](../../error-codes/enterprise-device-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9200012 | Parameter verification failed. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**Example**

import { applicationManager, common } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace it as required.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

let applicationInstances: Array<common.ApplicationInstance> = \[
  // Replace it as required.
  {
    appIdentifier: '0123456789123456789',
    accountId: 100,
    appIndex: 0
  }
\];

try {
  applicationManager.removeFreezeExemptedApps(wantTemp, applicationInstances);
  console.info('Succeeded in removing FreezeExempted applications.');
} catch(err) {
  console.error(\`Failed to remove FreezeExempted applications. Code: ${err.code}, message: ${err.message}\`);
}

#### applicationManager.getFreezeExemptedApps22+

getFreezeExemptedApps(admin: Want): Array<common.ApplicationInstance>

Obtains the background freeze-exempt application list of all users on the current device.

**Required permissions**: ohos.permission.ENTERPRISE\_MANAGE\_APPLICATION

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Device behavior differences**: This API can be called on phones and tablets but has no effect on other devices.

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |

**Return value**

| Type | Description |
| :-- | :-- |
| Array<[common.ApplicationInstance](../ohos-enterprise-common-common-module/document.md#applicationinstance)\> | Array of the background freeze-exempt application list. |

**Error codes**

For details about the error codes, see [Enterprise Device Management Error Codes](../../error-codes/enterprise-device-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**Example**

import { applicationManager, common } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace it as required.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  let result: Array<common.ApplicationInstance> = applicationManager.getFreezeExemptedApps(wantTemp);
  console.info(\`Succeeded in getting FreezeExempted applications, result : ${JSON.stringify(result)}\`);
} catch(err) {
  console.error(\`Failed to get FreezeExempted applications. Code: ${err.code}, message: ${err.message}\`);
}
