# @ohos.enterprise.securityManager (Security Management)

The **securityManager** module provides device security management capabilities, including obtaining the security patch status and file system encryption status.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/dS3O5uyPT2mK30GYYXSe4A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062406Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E33B9FAB983BB7E36D89ECD4CA3CB0913DDF88B79988D869DED63890990E09FF)

The initial APIs of this module are supported since API version 12. Newly added APIs will be marked with a superscript to indicate their earliest API version.

The APIs of this module can be used only in the stage model.

The APIs of this module can be called only by a device administrator application that is enabled. For details, see [MDM Kit Development](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/mdm-kit-guide).

#### Modules to Import

import { securityManager } from '@kit.MDMKit';

#### securityManager.uninstallUserCertificate

uninstallUserCertificate(admin: Want, certUri: string): Promise<void>

Uninstalls a user certificate. This API uses a promise to return the result.

**Required permissions**: ohos.permission.ENTERPRISE\_MANAGE\_CERTIFICATE

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| certUri | string | Yes | Certificate URI, which is set and returned by the [installUserCertificate](#securitymanagerinstallusercertificate) API for installing a user certificate. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. An error object is thrown when a user certificate fails to be uninstalled. |

**Error codes**

For details about the error codes, see [Enterprise Device Management Error Codes](../../error-codes/enterprise-device-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9201001 | Failed to manage the certificate. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { securityManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
// Replace with actual values.
let aliasStr = "certName";
securityManager.uninstallUserCertificate(wantTemp, aliasStr).then(() => {
  console.info(\`Succeeded in uninstalling user certificate.\`);
}).catch((err: BusinessError) => {
  console.error(\`Failed to uninstall user certificate. Code is ${err.code}, message is ${err.message}\`);
});

#### securityManager.installUserCertificate

installUserCertificate(admin: Want, certificate: CertBlob): Promise<string>

Installs a user certificate. This API uses a promise to return the result.

**Required permissions**: ohos.permission.ENTERPRISE\_MANAGE\_CERTIFICATE

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| certificate | [CertBlob](#certblob) | Yes | Certificate information. The certificate file must be stored in the path that the app has the permission to access, such as the app sandbox path. For details about the mapping between the app sandbox path and the actual physical path, see [Mappings Between App Sandbox Paths and Physical Paths](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-sandbox-directory#mappings-between-application-sandbox-paths-and-physical-paths). |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<string> | Promise used to return the URI of the installed certificate. This URI can be used to uninstall the certificate. |

**Error codes**

For details about the error codes, see [Enterprise Device Management Error Codes](../../error-codes/enterprise-device-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9201001 | Failed to manage the certificate. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { securityManager } from '@kit.MDMKit';
import { common, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
let certFileArray: Uint8Array = new Uint8Array();
// Initialize the context variable in the onCreate callback function of the MainAbility.
// Store test.cer in the rawfile directory.
// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
const context = this.getUIContext().getHostContext() as common.UIAbilityContext;
context.resourceManager.getRawFileContent("test.cer").then((value) => {
  certFileArray = value;
  securityManager.installUserCertificate(wantTemp, { inData: certFileArray, alias: "cert\_alias\_xts" })
    .then((result) => {
      console.info(\`Succeeded in installing user certificate, result : ${JSON.stringify(result)}\`);
    }).catch((err: BusinessError) => {
    console.error(\`Failed to install user certificate. Code: ${err.code}, message: ${err.message}\`);
  })
}).catch((err: BusinessError) => {
  console.error(\`Failed to get raw file content. message: ${err.message}\`);
  return;
});

#### securityManager.installUserCertificate18+

installUserCertificate(admin: Want, certificate: CertBlob, accountId: number): string

Installs a user certificate based on the system account.

**Required permissions**: ohos.permission.ENTERPRISE\_MANAGE\_CERTIFICATE

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| certificate | [CertBlob](#certblob) | Yes | Certificate information. The certificate file must be stored in the path that the app has the permission to access, such as the app sandbox path. For details about the mapping between the app sandbox path and the actual physical path, see [Mappings Between App Sandbox Paths and Physical Paths](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-sandbox-directory#mappings-between-application-sandbox-paths-and-physical-paths). |
| accountId | number | Yes | User ID, which must be greater than or equal to 0. You can call [getOsAccountLocalId](../../../basic-services-kit/arkts-apis/account-management/ohos-account-osaccount-system-account-management/document.md#getosaccountlocalid9-1) of **@ohos.account.osAccount** to obtain the user ID. |

**Return value**

| Type | Description |
| :-- | :-- |
| string | URI of the installed certificate, which is used to uninstall the certificate. |

**Error codes**

For details about the error codes, see [Enterprise Device Management Error Codes](../../error-codes/enterprise-device-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9201001 | Failed to manage the certificate. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**Example**

import { securityManager } from '@kit.MDMKit';
import { common, Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
let certFileArray: Uint8Array = new Uint8Array();
let accountId: number = 100;
// Initialize the context variable in the onCreate callback function of the MainAbility.
// Store test.cer in the rawfile directory.
// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
const context = this.getUIContext().getHostContext() as common.UIAbilityContext;
context.resourceManager.getRawFileContent("test.cer").then((value) => {
  certFileArray = value;
  try {
    let result: string = securityManager.installUserCertificate(wantTemp, { inData: certFileArray, alias: "cert\_alias\_xts" }, accountId);
    console.info(\`Succeeded in installing user certificate. result: ${result}\`);
  } catch (err) {
    console.error(\`Failed to install user certificate. Code: ${err.code}, message: ${err.message}\`);
  }
});

#### securityManager.getUserCertificates18+

getUserCertificates(admin: Want, accountId: number): Array<string>

Obtains the user certificate of a specified system account.

**Required permissions**: ohos.permission.ENTERPRISE\_MANAGE\_CERTIFICATE

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| accountId | number | Yes | User ID, which must be greater than or equal to 0. You can call [getOsAccountLocalId](../../../basic-services-kit/arkts-apis/account-management/ohos-account-osaccount-system-account-management/document.md#getosaccountlocalid9-1) of **@ohos.account.osAccount** to obtain the user ID. |

**Return value**

| Type | Description |
| :-- | :-- |
| Array<string> | All user certificates installed under the specified user ID. |

**Error codes**

For details about the error codes, see [Enterprise Device Management Error Codes](../../error-codes/enterprise-device-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**Example**

import { securityManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
// Replace with actual values.
let accountId: number = 100;
try {
  let result: Array<string> = securityManager.getUserCertificates(wantTemp, accountId);
  console.info(\`Succeeded in getting the uri list of user Certificates. result: ${JSON.stringify(result)}\`);
} catch (err) {
  console.error(\`Failed to get the uri list of user Certificates. Code: ${err.code}, message: ${err.message}\`);
}

#### securityManager.getSecurityStatus

getSecurityStatus(admin: Want, item: string): string

Obtains the security status of the current device.

**Required permissions**: ohos.permission.ENTERPRISE\_MANAGE\_SECURITY

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| item | string | Yes | 
Type of the security status to obtain.

\- **patch**: device security patch.

\- **encryption**: device file system encryption.

\- **root:** root status of the device.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| string | Security status obtained. |

**Error codes**

For details about the error codes, see [Enterprise Device Management Error Codes](../../error-codes/enterprise-device-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { securityManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  let result: string = securityManager.getSecurityStatus(wantTemp, 'patch');
  console.info(\`Succeeded in getting security patch tag. tag: ${result}\`);
} catch (err) {
  console.error(\`Failed to get security patch tag. Code: ${err.code}, message: ${err.message}\`);
}

#### securityManager.setPasswordPolicy

setPasswordPolicy(admin: Want, policy: PasswordPolicy): void

Sets the device screen lock password policy. During screen lock password setting, if the current screen lock password does not meet the requirements, a security message will be displayed, prompting the user to reset the screen lock password.

**Required permissions**: ohos.permission.ENTERPRISE\_MANAGE\_SECURITY

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| policy | [PasswordPolicy](#passwordpolicy) | Yes | Device screen lock password policy. |

**Error codes**

For details about the error codes, see [Enterprise Device Management Error Codes](../../error-codes/enterprise-device-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { securityManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

let policy: securityManager.PasswordPolicy = {
  complexityRegex: '^(?=.\*\[a-z\])(?=.\*\[A-Z\])(?=.\*\\\\d)(?=.\*\[!@#$%^&\*\])\[a-zA-Z\\\\d!@#$%^&\*\]{8,}$',
  validityPeriod: 1,
  additionalDescription: 'The password must contain at least eight characters, including at least one uppercase letter, one lowercase letter, one digit, and one special character.',
};
try {
    securityManager.setPasswordPolicy(wantTemp, policy);
    console.info(\`Succeeded in setting password policy.\`);
} catch(err) {
    console.error(\`Failed to set password policy. Code: ${err.code}, message: ${err.message}\`);
}

#### securityManager.getPasswordPolicy

getPasswordPolicy(admin: Want): PasswordPolicy

Obtains the device screen lock password policy.

**Required permissions**: ohos.permission.ENTERPRISE\_MANAGE\_SECURITY

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |

**Return value**

| Type | Description |
| :-- | :-- |
| [PasswordPolicy](#passwordpolicy) | Device screen lock password policy. |

**Error codes**

For details about the error codes, see [Enterprise Device Management Error Codes](../../error-codes/enterprise-device-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { securityManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
    let result: securityManager.PasswordPolicy = securityManager.getPasswordPolicy(wantTemp);
    console.info(\`Succeeded in getting password policy, result : ${JSON.stringify(result)}\`);
} catch(err) {
    console.error(\`Failed to get password policy. Code: ${err.code}, message: ${err.message}\`);
}

#### securityManager.setAppClipboardPolicy

setAppClipboardPolicy(admin: Want, tokenId: number, policy: ClipboardPolicy): void

Sets the device clipboard policy.

**Required permissions**: ohos.permission.ENTERPRISE\_MANAGE\_SECURITY

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| tokenId | number | Yes | Application token ID, which can be obtained using [bundleManager.getApplicationInfo](../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/bundlemanager/applicationinfo/document.md). Currently, a maximum of 100 token IDs can be saved. |
| policy | [ClipboardPolicy](#clipboardpolicy) | Yes | Clipboard policy to set. |

**Error codes**

For details about the error codes, see [Enterprise Device Management Error Codes](../../error-codes/enterprise-device-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { securityManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
// Replace with actual values.
let tokenId: number = 586874394;
try {
    securityManager.setAppClipboardPolicy(wantTemp, tokenId, securityManager.ClipboardPolicy.IN\_APP);
    console.info(\`Succeeded in setting clipboard policy.\`);
} catch(err) {
    console.error(\`Failed to set clipboard policy. Code: ${err.code}, message: ${err.message}\`);
}

#### securityManager.getAppClipboardPolicy

getAppClipboardPolicy(admin: Want, tokenId?: number): string

Obtains the device clipboard policy.

**Required permissions**: ohos.permission.ENTERPRISE\_MANAGE\_SECURITY

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| tokenId | number | No | Application token ID, which can be obtained using [bundleManager.getApplicationInfo](../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/bundlemanager/applicationinfo/document.md). Currently, a maximum of 100 token IDs can be saved. |

**Return value**

| Type | Description |
| :-- | :-- |
| string | Device clipboard policy in JSON format. |

**Error codes**

For details about the error codes, see [Enterprise Device Management Error Codes](../../error-codes/enterprise-device-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { securityManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
// Replace with actual values.
let tokenId: number = 586874394;
try {
    let result: string = securityManager.getAppClipboardPolicy(wantTemp, tokenId);
    console.info(\`Succeeded in getting password policy, result : ${result}\`);
} catch(err) {
    console.error(\`Failed to set clipboard policy. Code: ${err.code}, message: ${err.message}\`);
}

#### securityManager.setAppClipboardPolicy18+

setAppClipboardPolicy(admin: Want, bundleName: string, accountId: number, policy: ClipboardPolicy): void

Sets the device clipboard policy of a specified application for a specified user. Currently, a maximum of 100 policies can be saved.

**Required permissions**: ohos.permission.ENTERPRISE\_MANAGE\_SECURITY

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| bundleName | string | Yes | Bundle name of the application for which the device clipboard policy is set. |
| accountId | number | Yes | User ID, which must be greater than or equal to 0. You can call [getOsAccountLocalId](../../../basic-services-kit/arkts-apis/account-management/ohos-account-osaccount-system-account-management/document.md#getosaccountlocalid9-1) of **@ohos.account.osAccount** to obtain the user ID. |
| policy | [ClipboardPolicy](#clipboardpolicy) | Yes | Clipboard policy to set. |

**Error codes**

For details about the error codes, see [Enterprise Device Management Error Codes](../../error-codes/enterprise-device-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**Example**

import { securityManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
// Replace with actual values.
let bundleName: string = 'com.example.myapplication';
let accountId: number = 100;
try {
    securityManager.setAppClipboardPolicy(wantTemp, bundleName, accountId, securityManager.ClipboardPolicy.IN\_APP);
    console.info(\`Succeeded in setting clipboard policy.\`);
} catch(err) {
    console.error(\`Failed to set clipboard policy. Code: ${err.code}, message: ${err.message}\`);
}

#### securityManager.getAppClipboardPolicy18+

getAppClipboardPolicy(admin: Want, bundleName: string, accountId: number): string

Obtains the device clipboard policy of a specified application for a specified user.

**Required permissions**: ohos.permission.ENTERPRISE\_MANAGE\_SECURITY

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| bundleName | string | Yes | Bundle name of the application for which the device clipboard policy is set. |
| accountId | number | Yes | User ID, which must be greater than or equal to 0. You can call [getOsAccountLocalId](../../../basic-services-kit/arkts-apis/account-management/ohos-account-osaccount-system-account-management/document.md#getosaccountlocalid9-1) of **@ohos.account.osAccount** to obtain the user ID. |

**Return value**

| Type | Description |
| :-- | :-- |
| string | Device clipboard policy in JSON format. |

**Error codes**

For details about the error codes, see [Enterprise Device Management Error Codes](../../error-codes/enterprise-device-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**Example**

import { securityManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
// Replace with actual values.
let bundleName: string = 'com.example.myapplication';
let accountId: number = 100;
try {
    let result: string = securityManager.getAppClipboardPolicy(wantTemp, bundleName, accountId);
    console.info(\`Succeeded in getting password policy, result : ${result}\`);
} catch(err) {
    console.error(\`Failed to set clipboard policy. Code: ${err.code}, message: ${err.message}\`);
}

#### securityManager.setWatermarkImage14+

setWatermarkImage(admin: Want, bundleName: string, source: string | image.PixelMap, accountId: number): void

Sets a watermark policy for a specified application of a specified user. Currently, a maximum of 100 policies can be saved.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/uAfwkbYzTAmVzOtQJ77vjQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062406Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3E4BBF4CD6C94FA4878247C1A12AC91F297EFAF86479962F198E51FD23AF1951)

This API is applicable to setting watermarks for third-party applications in enterprise scenarios to reduce the risk of enterprise information leakage. You are not advised to set watermarks for system applications (such as the home screen application), as unknown exceptions may occur.

**Required permissions**: ohos.permission.ENTERPRISE\_MANAGE\_SECURITY

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| bundleName | string | Yes | Bundle name of the application for which the watermark is set. |
| source | string | [image.PixelMap](../../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md) | Yes | 
**string** indicates the image path, which is the path that the app has the permission to access, such as the app sandbox path. For details about the mapping between the app sandbox path and the actual physical path, see [Mappings Between App Sandbox Paths and Physical Paths](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-sandbox-directory#mappings-between-application-sandbox-paths-and-physical-paths).

**image.PixelMap** indicates an image object. The size of an image pixel cannot exceed 500 KB.

The size of an image pixel is calculated as follows: Image width (pixels) × Image height (pixels) × Number of bytes per pixel (typically 4). For example, the size of a 100 × 100 image is 100 × 100 × 4 = 40,000 bytes.

 |
| accountId | number | Yes | User ID. You can call [getOsAccountLocalId](../../../basic-services-kit/arkts-apis/account-management/ohos-account-osaccount-system-account-management/document.md#getosaccountlocalid9-1) of **@ohos.account.osAccount** to obtain the user ID. |

**Error codes**

For details about the error codes, see [Enterprise Device Management Error Codes](../../error-codes/enterprise-device-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { securityManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
// Replace with actual values.
let bundleName: string = 'com.example.myapplication';
let source: string = '/data/storage/el1/base/test.png';
let accountId: number = 100;
try {
    securityManager.setWatermarkImage(wantTemp, bundleName, source, accountId);
    console.info(\`Succeeded in setting set watermarkImage policy.\`);
} catch(err) {
    console.error(\`Failed to set watermarkImage policy. Code: ${err.code}, message: ${err.message}\`);
}

#### securityManager.cancelWatermarkImage14+

cancelWatermarkImage(admin: Want, bundleName: string, accountId: number): void

Cancels the watermark policy for a specified user.

**Required permissions**: ohos.permission.ENTERPRISE\_MANAGE\_SECURITY

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| bundleName | string | Yes | Bundle name of the application for which the watermark is removed. |
| accountId | number | Yes | User ID. You can call [getOsAccountLocalId](../../../basic-services-kit/arkts-apis/account-management/ohos-account-osaccount-system-account-management/document.md#getosaccountlocalid9-1) of **@ohos.account.osAccount** to obtain the user ID. |

**Error codes**

For details about the error codes, see [Enterprise Device Management Error Codes](../../error-codes/enterprise-device-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { securityManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
// Replace with actual values.
let bundleName: string = 'com.example.myapplication';
let accountId: number = 100;
try {
    securityManager.cancelWatermarkImage(wantTemp, bundleName, accountId);
    console.info(\`Succeeded in setting cancel watermarkImage policy.\`);
} catch(err) {
    console.error(\`Failed to cancel watermarkImage policy. Code: ${err.code}, message: ${err.message}\`);
}

#### securityManager.setPermissionManagedState20+

setPermissionManagedState(admin: Want, applicationInstance: ApplicationInstance, permissions: Array<string>, managedState: PermissionManagedState): void

Sets the management policy for the [user\_grant permission](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/permissions-for-all-user) of a specified application.

**Required permissions**: ohos.permission.ENTERPRISE\_MANAGE\_USER\_GRANT\_PERMISSION

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| applicationInstance | [ApplicationInstance](#applicationinstance20) | Yes | Application instance. |
| permissions | Array<string> | Yes | List of permissions to be managed. Only [user\_grant permission](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/permissions-for-all-user) is supported. The list is grouped by [application permission groups](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-permission-group-list) and must include all permissions in the same permission group declared by the application in [module.json5](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/module-configuration-file). For example, if an application declares ohos.permission.READ\_CALENDAR and ohos.permission.WRITE\_CALENDAR in **module.json5**, the input permission list must contain both ohos.permission.READ\_CALENDAR and ohos.permission.WRITE\_CALENDAR. |
| managedState | [PermissionManagedState](#permissionmanagedstate20) | Yes | Management policy for application permissions. |

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

import { Want } from '@kit.AbilityKit';
import { securityManager } from '@kit.MDMKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
let appInstanceTemp: securityManager.ApplicationInstance = {
      // Replace with actual values.
      appIdentifier: '736498586',
      appIndex: 0,
      accountId: 100
};
let permissionsTemp: Array<string> = \['ohos.permission.CAMERA', 'ohos.permission.LOCATION'\];
try {
    securityManager.setPermissionManagedState(wantTemp, appInstanceTemp, permissionsTemp, securityManager.PermissionManagedState.GRANTED);
    console.info('Succeeded in setting permission managed state.');
} catch(err) {
    console.error(\`Failed to set permission managed state.  Code: ${err.code}, message: ${err.message}\`);
}

#### securityManager.getPermissionManagedState20+

getPermissionManagedState(admin: Want, applicationInstance: ApplicationInstance, permission: string): PermissionManagedState

Obtains the management policy for the [user\_grant permission](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/permissions-for-all-user) of a specified application.

**Required permissions**: ohos.permission.ENTERPRISE\_MANAGE\_USER\_GRANT\_PERMISSION

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| applicationInstance | [ApplicationInstance](#applicationinstance20) | Yes | Application instance. |
| permission | string | Yes | Name of the permission required for obtaining the management policy. Only the **user\_grant** permission is supported. |

**Return value**

| Type | Description |
| :-- | :-- |
| [PermissionManagedState](#permissionmanagedstate20) | Management policy for application permissions. |

**Error codes**

For details about the error codes, see [Enterprise Device Management Error Codes](../../error-codes/enterprise-device-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9200012 | Parameter verification failed. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**Example**

import { Want } from '@kit.AbilityKit';
import { securityManager } from '@kit.MDMKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
let appInstanceTemp: securityManager.ApplicationInstance = {
      // Replace with actual values.
      appIdentifier: '736498586',
      appIndex: 0,
      accountId: 100
};
let permissionTemp: string = 'ohos.permission.ENTERPRISE\_MANAGE\_USER\_GRANT\_PERMISSION';
try {
    let result: securityManager.PermissionManagedState = securityManager.getPermissionManagedState(wantTemp, appInstanceTemp, permissionTemp);
    console.info(\`Succeeded in getting permission managed state, result : ${result}\`);
} catch(err) {
    console.error(\`Failed to get permission managed state. Code: ${err.code}, message: ${err.message}\`);
}

#### securityManager.setExternalSourceExtensionsPolicy22+

setExternalSourceExtensionsPolicy(admin: Want, policy: common.ManagedPolicy): void

Sets the management policy for extensions from external sources.

-   DEFAULT:
    
    Default policy with no restrictions applied. Users can enable or disable **Run extensions from external sources** in **Settings** > **Privacy & security** > **Advanced option**.
    
-   DISALLOW:
    
    Policy that disallows extensions from external sources to run. With this policy, currently running extensions can continue, but cannot be started after being closed. Users cannot enable **Run extensions from external sources**.
    
-   FORCE\_OPEN:
    
    Policy that forcibly enables extensions from external sources to run. Users cannot disable **Run extensions from external sources**.
    

**Required permissions**: ohos.permission.ENTERPRISE\_MANAGE\_SECURITY

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Device behavior differences**: This API can be properly called on PCs/2-in-1 devices. If it is called on other device types, error code 801 is returned.

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md#want) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| policy | [common.ManagedPolicy](../ohos-enterprise-common-common-module/document.md#managedpolicy) | Yes | Management policy. |

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

import { common, securityManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
try {
    securityManager.setExternalSourceExtensionsPolicy(wantTemp, common.ManagedPolicy.FORCE\_OPEN);
    console.info(\`Succeeded in setting managed policy.\`);
} catch(err) {
    console.error(\`Failed to set managed policy. Code: ${err.code}, message: ${err.message}\`);
}

#### securityManager.getExternalSourceExtensionsPolicy22+

getExternalSourceExtensionsPolicy(admin: Want): common.ManagedPolicy

Obtains the management policy for extensions from external sources.

**Required permissions**: ohos.permission.ENTERPRISE\_MANAGE\_SECURITY

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Device behavior differences**: This API can be properly called on PCs/2-in-1 devices. If it is called on other device types, error code 801 is returned.

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md#want) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |

**Return value**

| Type | Description |
| :-- | :-- |
| [common.ManagedPolicy](../ohos-enterprise-common-common-module/document.md#managedpolicy) | Management policy obtained. |

**Error codes**

For details about the error codes, see [Enterprise Device Management Error Codes](../../error-codes/enterprise-device-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**Example**

import { common, securityManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
    let result: common.ManagedPolicy = securityManager.getExternalSourceExtensionsPolicy(wantTemp);
    console.info(\`Succeeded in getting managed policy, result : ${result}\`);
} catch(err) {
    console.error(\`Failed to get managed policy. Code: ${err.code}, message: ${err.message}\`);
}

#### CertBlob

Represents the certificate information.

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| inData | Uint8Array | No | No | Binary content of the certificate. |
| alias | string | No | No | Certificate alias. The value length must be less than 40 characters. |

#### PasswordPolicy

Represents a device screen lock password policy.

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| complexityRegex | string | No | Yes | Regular expression for password complexity. |
| validityPeriod | number | No | Yes | Password validity period, in ms. |
| additionalDescription | string | No | Yes | Password complexity description, for example, "The password must contain 8 to 30 characters consisting of letters, digits, and special characters". |

#### ClipboardPolicy

Represents a device clipboard policy.

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

| Name | Value | Description |
| :-- | :-- | :-- |
| DEFAULT | 0 | Default policy, which indicates no policy. |
| IN\_APP | 1 | Allow the clipboard to be used in the same application. |
| LOCAL\_DEVICE | 2 | Allow the clipboard to be used on the same device. |
| CROSS\_DEVICE | 3 | Allow the clipboard to be used across devices. |

#### ApplicationInstance20+

Application instance

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| appIdentifier | string | No | No | The [unique identifier](../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/bundlemanager/bundleinfo/document.md#signatureinfo) of an application. If an application does not have **appIdentifier**, **appId** can be used instead. Both **bundleInfo.signatureInfo.appIdentifier** and **bundleInfo.signatureInfo.appId** can be obtained via the [bundleManager.getBundleInfo](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-bundle-bundlemanager-bundle-management-module/document.md#bundlemanagergetbundleinfo14-2) API. |
| accountId | number | No | No | User ID, which must be greater than or equal to 0. You can call [getOsAccountLocalId](../../../basic-services-kit/arkts-apis/account-management/ohos-account-osaccount-system-account-management/document.md#getosaccountlocalid9-1) of **@ohos.account.osAccount** to obtain the user ID. |
| appIndex | number | No | No | 
Index of the application clone. The default value is **0**.

If **appIndex** is set to **0**, the main application is used. If **appIndex** is set to a value greater than 0, the application clone with the specified index is used.

 |

#### PermissionManagedState20+

Represents the management status of application permissions.

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

| Name | Value | Description |
| :-- | :-- | :-- |
| DEFAULT | 1 | The permission is granted by the user by default. |
| GRANTED | 0 | This permission is granted silently. |
| DENIED | \-1 | This permission is denied silently. |
