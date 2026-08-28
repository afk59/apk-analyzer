# @ohos.enterprise.browser (Browser Management)

The **browser** module provides browser management, including setting, canceling, and obtaining browser policies.

Browser policies are a collection of rules and settings that govern how a browser behaves, ensuring security, compliance, performance optimization, and a consistent user experience.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/qBqEqcx-TA6nVfhzlJvOHA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062405Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2BD687F002A2A661CE85A2F53ADC04A67A76CC289EF162459883C84587CB20A4)

-   The initial APIs of this module are supported since API version 12. Newly added APIs will be marked with a superscript to indicate their earliest API version.
    
-   The APIs of this module can be used only in the stage model.
    
-   The APIs of this module can be called only by a device administrator application that is enabled. For details, see [MDM Kit Development](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/mdm-kit-guide).
    

#### Modules to Import

import { browser } from '@kit.MDMKit';

#### browser.setPolicySync

setPolicySync(admin: Want, appId: string, policyName: string, policyValue: string): void

Sets the sub-policy for a specified browser.

**Required permissions**: ohos.permission.ENTERPRISE\_SET\_BROWSER\_POLICY

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| appId | string | Yes | Application ID, which is used to specify the browser. |
| policyName | string | Yes | Name of the browser policy to set. If the value is an empty string, the browser policy corresponding to the application ID is set. |
| policyValue | string | Yes | Browser policy to set. If the value is an empty string, the policy corresponding to the policy name is removed. |

**Error codes**

For details about the error codes, see [Enterprise Device Management Error Codes](../../error-codes/enterprise-device-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { browser } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

// Replace the value of appId with the specified application ID of the browser.
let appId: string = 'com.example.\*\*\*\*\*\*\_\*\*\*\*\*\*/\*\*\*\*\*\*5t5CoBM=';
let policyName: string = 'InsecurePrivateNetworkRequestsAllowed';
let policyValue: string = '{"level":"mandatory","scope":"machine","source":"platform","value":true}';

try {
  browser.setPolicySync(wantTemp, appId, policyName, policyValue);
  console.info('Succeeded in setting browser policies.');
} catch (err) {
  console.error(\`Failed to set browser policies. Code is ${err.code}, message is ${err.message}\`);
}

#### browser.getPoliciesSync

getPoliciesSync(admin: Want, appId: string): string

Obtains the browser policy by app ID.

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| appId | string | Yes | Application ID, which is used to specify the browser. |

**Return value**

| Type | Description |
| :-- | :-- |
| string | Browser policy obtained. |

**Error codes**

For details about the error codes, see [Enterprise Device Management Error Codes](../../error-codes/enterprise-device-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9200001 | The application is not an administrator application of the device. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { browser } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

// Replace the value of appId with the specified application ID of the browser.
let appId: string = 'com.example.\*\*\*\*\*\*\_\*\*\*\*\*\*/\*\*\*\*\*\*5t5CoBM=';

try {
  let result: string = browser.getPoliciesSync(wantTemp, appId);
  console.info(\`Succeeded in getting browser policies, result : ${JSON.stringify(result)}\`);
} catch(err) {
  console.error(\`Failed to get browser policies. Code is ${err.code}, message is ${err.message}\`);
}

#### browser.setManagedBrowserPolicy15+

setManagedBrowserPolicy(admin: Want, bundleName: string, policyName: string, policyValue: string): void

Sets the browser policy. After the setting is successful, the system common event [COMMON\_EVENT\_MANAGED\_BROWSER\_POLICY\_CHANGED](../../../basic-services-kit/arkts-apis/process-and-thread-communication/system-common-events/document.md#common_event_managed_browser_policy_changed) is released.

**Required permissions**: ohos.permission.ENTERPRISE\_SET\_BROWSER\_POLICY

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| bundleName | string | Yes | Application bundle name, which is used to specify the browser. |
| policyName | string | Yes | Browser policy name. |
| policyValue | string | Yes | Browser policy value. If the value is an empty string, the policy corresponding to the policy name is removed. |

**Error codes**

For details about the error codes, see [Enterprise Device Management Error Codes](../../error-codes/enterprise-device-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { browser } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
// Replace with actual values.
let bundleName: string = 'com.example.testbrowser';
let policyName: string = 'InsecurePrivateNetworkRequestsAllowed';
let policyValue: string = '{"level":"mandatory","scope":"machine","source":"platform","value":true}';

try {
  browser.setManagedBrowserPolicy(wantTemp, bundleName, policyName, policyValue);
  console.info('Succeeded in setting managed browser policy.');
} catch (err) {
  console.error(\`Failed to set managed browser policy. Code is ${err.code}, message is ${err.message}\`);
}

#### browser.getManagedBrowserPolicy15+

getManagedBrowserPolicy(admin: Want, bundleName: string): ArrayBuffer

Obtains the browser policy by application bundle name.

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| bundleName | string | Yes | Application bundle name, which is used to specify the browser. |

**Return value**

| Type | Description |
| :-- | :-- |
| ArrayBuffer | Browser policy obtained. |

**Error codes**

For details about the error codes, see [Enterprise Device Management Error Codes](../../error-codes/enterprise-device-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9200001 | The application is not an administrator application of the device. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { browser } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';
import { util } from '@kit.ArkTS';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
// Replace with actual values.
let bundleName: string = 'com.example.testbrowser';

try {
  let buffer: ArrayBuffer = browser.getManagedBrowserPolicy(wantTemp, bundleName);
  let intBuffer: Uint8Array = new Uint8Array(buffer);
  let decoder: util.TextDecoder = util.TextDecoder.create('utf-8');
  let stringData: string = decoder.decodeToString(intBuffer);
  console.info(\`Succeeded in getting managed browser policy, result : ${stringData}\`);
} catch(err) {
  console.error(\`Failed to get managed browser policy. Code is ${err.code}, message is ${err.message}\`);
}

#### browser.getSelfManagedBrowserPolicyVersion15+

getSelfManagedBrowserPolicyVersion(): string

Obtains the policy version of a specified browser.

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Return value**

| Type | Description |
| :-- | :-- |
| string | Browser policy version. |

**Example**

import { browser } from '@kit.MDMKit';

try {
  let version: string = browser.getSelfManagedBrowserPolicyVersion();
  console.info(\`Succeeded in getting self managed browser policy version, result : ${version}\`);
} catch(err) {
  console.error(\`Failed to get self managed browser policy version. Code is ${err.code}, message is ${err.message}\`);
}

#### browser.getSelfManagedBrowserPolicy15+

getSelfManagedBrowserPolicy(): ArrayBuffer

Obtains the browser policy of the current device.

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Return value**

| Type | Description |
| :-- | :-- |
| ArrayBuffer | Browser policy obtained. |

**Example**

import { browser } from '@kit.MDMKit';
import { util } from '@kit.ArkTS';

try {
  let buffer: ArrayBuffer = browser.getSelfManagedBrowserPolicy();
  let intBuffer: Uint8Array = new Uint8Array(buffer);
  let decoder: util.TextDecoder = util.TextDecoder.create('utf-8');
  let stringData: string = decoder.decodeToString(intBuffer);
  console.info(\`Succeeded in getting self managed browser policy, result : ${stringData}\`);
} catch(err) {
  console.error(\`Failed to get self managed browser policy. Code is ${err.code}, message is ${err.message}\`);
}
