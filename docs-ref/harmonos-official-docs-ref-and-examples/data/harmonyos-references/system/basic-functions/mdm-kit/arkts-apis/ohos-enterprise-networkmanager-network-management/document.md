# @ohos.enterprise.networkManager (Network Management)

The **networkManager** module provides APIs for network management of enterprise devices, including obtaining the device IP address and MAC address.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/Onx0hSfnRWuo5n-crAhWaA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062406Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=87C2CB7D959C99CFD5BE3C8360245351E62F135D592619092A797E5C0735EE70)

The initial APIs of this module are supported since API version 12. Newly added APIs will be marked with a superscript to indicate their earliest API version.

The APIs of this module can be used only in the stage model.

The APIs of this module can be called only by a device administrator application that is enabled. For details, see [MDM Kit Development](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/mdm-kit-guide).

#### Modules to Import

import { networkManager } from '@kit.MDMKit';

#### networkManager.getAllNetworkInterfacesSync

getAllNetworkInterfacesSync(admin: Want): Array<string>

Obtains all activated wired network interfaces.

**Required permissions**: ohos.permission.ENTERPRISE\_MANAGE\_NETWORK

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |

**Return value**

| Type | Description |
| :-- | :-- |
| Array<string> | Names of all activated wired network interfaces. |

**Error codes**

For details about the error codes, see [Enterprise Device Management Error Codes](../../error-codes/enterprise-device-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { networkManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  let result: Array<string> = networkManager.getAllNetworkInterfacesSync(wantTemp);
  console.info(\`Succeeded in getting all network interfaces, result : ${JSON.stringify(result)}\`);
} catch (err) {
  console.error(\`Failed to get all network interfaces. Code: ${err.code}, message: ${err.message}\`);
}

#### networkManager.getIpAddressSync

getIpAddressSync(admin: Want, networkInterface: string): string

Obtains the device IP address based on the network interface.

**Required permissions**: ohos.permission.ENTERPRISE\_MANAGE\_NETWORK

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| networkInterface | string | Yes | Network port. |

**Return value**

| Type | Description |
| :-- | :-- |
| string | IP address of the network interface specified by the device. |

**Error codes**

For details about the error codes, see [Enterprise Device Management Error Codes](../../error-codes/enterprise-device-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { networkManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  // Replace parameters with actual values.
  let result: string = networkManager.getIpAddressSync(wantTemp, 'eth0');
  console.info(\`Succeeded in getting ip address, result : ${result}\`);
} catch (err) {
  console.error(\`Failed to get ip address. Code: ${err.code}, message: ${err.message}\`);
}

#### networkManager.getMacSync

getMacSync(admin: Want, networkInterface: string): string

Obtains the MAC address of a device based on the network interface.

**Required permissions**: ohos.permission.ENTERPRISE\_MANAGE\_NETWORK

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| networkInterface | string | Yes | Network port. |

**Return value**

| Type | Description |
| :-- | :-- |
| string | MAC address of the network interface specified by the device. |

**Error codes**

For details about the error codes, see [Enterprise Device Management Error Codes](../../error-codes/enterprise-device-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { networkManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  // Replace parameters with actual values.
  let result: string = networkManager.getMacSync(wantTemp, 'eth0');
  console.info(\`Succeeded in getting mac, result : ${result}\`);
} catch (err) {
  console.error(\`Failed to get mac. Code: ${err.code}, message: ${err.message}\`);
}

#### networkManager.isNetworkInterfaceDisabledSync

isNetworkInterfaceDisabledSync(admin: Want, networkInterface: string): boolean

Queries whether a specified network interface is disabled.

**Required permissions**: ohos.permission.ENTERPRISE\_MANAGE\_NETWORK

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| networkInterface | string | Yes | Network port. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the network port is disabled; returns **false** otherwise. |

**Error codes**

For details about the error codes, see [Enterprise Device Management Error Codes](../../error-codes/enterprise-device-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { networkManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  // Replace parameters with actual values.
  let result: boolean = networkManager.isNetworkInterfaceDisabledSync(wantTemp, 'eth0');
  console.info(\`Succeeded in querying network interface is disabled or not, result : ${result}\`);
} catch (err) {
  console.error(\`Failed to query network interface is disabled or not. Code: ${err.code}, message: ${err.message}\`);
}

#### networkManager.setNetworkInterfaceDisabledSync

setNetworkInterfaceDisabledSync(admin: Want, networkInterface: string, isDisabled: boolean): void

Disables the device from using the specified network interface.

**Required permissions**: ohos.permission.ENTERPRISE\_MANAGE\_NETWORK

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| networkInterface | string | Yes | Network port. |
| isDisabled | boolean | Yes | Network port status to set. The value **true** means to disable the network port, and **false** means to enable the network port. |

**Error codes**

For details about the error codes, see [Enterprise Device Management Error Codes](../../error-codes/enterprise-device-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { networkManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  // Replace parameters with actual values.
  networkManager.setNetworkInterfaceDisabledSync(wantTemp, 'eth0', true);
  console.info(\`Succeeded in setting network interface disabled\`);
} catch (err) {
  console.error(\`Failed to set network interface disabled. Code: ${err.code}, message: ${err.message}\`);
}

#### networkManager.setGlobalProxySync

setGlobalProxySync(admin: Want, httpProxy: connection.HttpProxy): void

Sets the global network proxy.

**Required permissions**: ohos.permission.ENTERPRISE\_MANAGE\_NETWORK

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| httpProxy | [connection.HttpProxy](../../../../network/network-kit/arkts-apis/ohos-net-connection-network-connection-management/document.md#httpproxy10) | Yes | Global HTTP proxy to set. |

**Error codes**

For details about the error codes, see [Enterprise Device Management Error Codes](../../error-codes/enterprise-device-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { networkManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';
import { connection } from '@kit.NetworkKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

// Replace with actual values.
let exclusionStr: string = "192.168,baidu.com";
let exclusionArray: Array<string> = exclusionStr.split(',');
let httpProxy: connection.HttpProxy = {
  host: "192.168.xx.xxx",
  port: 8080,
  exclusionList: exclusionArray
};

try {
  networkManager.setGlobalProxySync(wantTemp, httpProxy);
  console.info(\`Succeeded in setting network global proxy.\`);
} catch (err) {
  console.error(\`Failed to set network global proxy. Code: ${err.code}, message: ${err.message}\`);
}

#### networkManager.setGlobalProxyForAccount15+

setGlobalProxyForAccount(admin: Want, httpProxy: connection.HttpProxy, accountId: number): void

Sets the network proxy for a specified user.

**Required permissions**: ohos.permission.ENTERPRISE\_MANAGE\_NETWORK

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Device behavior differences**: This API can be properly called on PCs/2-in-1 devices. If it is called on other device types, error code 801 is returned.

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| httpProxy | [connection.HttpProxy](../../../../network/network-kit/arkts-apis/ohos-net-connection-network-connection-management/document.md#httpproxy10) | Yes | HTTP proxy configuration of the network. |
| accountId | number | Yes | 
User ID, which must be greater than or equal to 0.

You can call [getOsAccountLocalId](../../../basic-services-kit/arkts-apis/account-management/ohos-account-osaccount-system-account-management/document.md#getosaccountlocalid9-1) of **@ohos.account.osAccount** to obtain the user ID.

 |

**Error codes**

For details about the error codes, see [Enterprise Device Management Error Codes](../../error-codes/enterprise-device-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |

**Example**

import { networkManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';
import { connection } from '@kit.NetworkKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

let httpProxy: connection.HttpProxy = {
  // Replace with actual values.
  host: '192.168.xx.xxx',
  port: 8080,
  exclusionList: \['192.168', 'baidu.com'\]
};

try {
  // Replace parameters with actual values.
  networkManager.setGlobalProxyForAccount(wantTemp, httpProxy, 100);
  console.info(\`Succeeded in setting network global proxy.\`);
} catch (err) {
  console.error(\`Failed to set network global proxy. Code: ${err.code}, message: ${err.message}\`);
}

#### networkManager.getGlobalProxySync

getGlobalProxySync(admin: Want): connection.HttpProxy

Obtains the global network proxy.

**Required permissions**: ohos.permission.ENTERPRISE\_MANAGE\_NETWORK

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |

**Return value**

| Type | Description |
| :-- | :-- |
| [connection.HttpProxy](../../../../network/network-kit/arkts-apis/ohos-net-connection-network-connection-management/document.md#httpproxy10) | Global HTTP proxy configuration obtained. |

**Error codes**

For details about the error codes, see [Enterprise Device Management Error Codes](../../error-codes/enterprise-device-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { networkManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';
import { connection } from '@kit.NetworkKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  let result: connection.HttpProxy = networkManager.getGlobalProxySync(wantTemp);
  console.info(\`Succeeded in getting network global proxy, result : ${JSON.stringify(result)}\`);
} catch (err) {
  console.error(\`Failed to get network global proxy. Code: ${err.code}, message: ${err.message}\`);
}

#### networkManager.getGlobalProxyForAccount15+

getGlobalProxyForAccount(admin: Want | null, accountId: number): connection.HttpProxy

Obtains the network proxy for a specified user.

**Required permissions**: ohos.permission.ENTERPRISE\_MANAGE\_NETWORK

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Device behavior differences**: This API can be properly called on PCs/2-in-1 devices. If it is called on other device types, error code 801 is returned.

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | null | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| accountId | number | Yes | 
User ID, which must be greater than or equal to 0.

You can call [getOsAccountLocalId](../../../basic-services-kit/arkts-apis/account-management/ohos-account-osaccount-system-account-management/document.md#getosaccountlocalid9-1) of **@ohos.account.osAccount** to obtain the user ID.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [connection.HttpProxy](../../../../network/network-kit/arkts-apis/ohos-net-connection-network-connection-management/document.md#httpproxy10) | HTTP proxy configuration of the network. |

**Error codes**

For details about the error codes, see [Enterprise Device Management Error Codes](../../error-codes/enterprise-device-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |

**Example**

import { networkManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';
import { connection } from '@kit.NetworkKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  // Replace parameters with actual values.
  let result: connection.HttpProxy = networkManager.getGlobalProxyForAccount(wantTemp, 100);
  console.info(\`Succeeded in getting network global proxy, result : ${JSON.stringify(result)}\`);
} catch (err) {
  console.error(\`Failed to get network global proxy. Code: ${err.code}, message: ${err.message}\`);
}

#### networkManager.addFirewallRule

addFirewallRule(admin: Want, firewallRule: FirewallRule): void

Adds firewall rules for the device. IPv4 and IPv6 are supported since API version 22. In API version 21 and earlier versions, only IPv4 is supported.

After a rule with [Action](#action) set to **ALLOW** is added, a rule with **Action** set to **DENY** is added by default to discard or intercept all network data packets that do not meet the **ALLOW** rule.

After the device is restarted, the firewall rules are cleared.

**Required permissions**: ohos.permission.ENTERPRISE\_MANAGE\_NETWORK

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| firewallRule | [FirewallRule](#firewallrule) | Yes | Firewall rule to add. |

**Error codes**

For details about the error codes, see [Enterprise Device Management Error Codes](../../error-codes/enterprise-device-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { networkManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
let firewallRule: networkManager.FirewallRule = {
  // Replace with actual values.
  "srcAddr": "192.168.1.1-192.168.22.66",
  "destAddr": "10.1.1.1",
  "srcPort": "8080",
  "destPort": "8080",
  "appUid": "9696",
  "direction": networkManager.Direction.OUTPUT,
  "action": networkManager.Action.DENY,
  "protocol": networkManager.Protocol.UDP,
  "family": 1
};

try {
  networkManager.addFirewallRule(wantTemp, firewallRule);
  console.info('Succeeded in adding firewall rule.');
} catch (err) {
  console.error(\`Failed to add firewall rule. Code: ${err.code}, message: ${err.message}\`);
}

#### networkManager.removeFirewallRule

removeFirewallRule(admin: Want, firewallRule?: FirewallRule): void

Removes firewall rules of the device. IPv4 and IPv6 are supported since API version 22. In API version 21 and earlier versions, only IPv4 is supported.

If there is no rule with [Action](#action) being **ALLOW** after the rule is removed, the **DENY** rules that are added by default with [addFirewallRule](#networkmanageraddfirewallrule) will be removed.

**Required permissions**: ohos.permission.ENTERPRISE\_MANAGE\_NETWORK

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| firewallRule | [FirewallRule](#firewallrule) | No | Firewall rule to remove. If the value is empty, all firewall rules will be removed. |

**Error codes**

For details about the error codes, see [Enterprise Device Management Error Codes](../../error-codes/enterprise-device-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { networkManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

let firewallRule: networkManager.FirewallRule = {
  // Replace with actual values.
  "srcAddr": "192.168.1.1-192.168.22.66",
  "destAddr": "10.1.1.1",
  "srcPort": "8080",
  "destPort": "8080",
  "appUid": "9696",
  "direction": networkManager.Direction.OUTPUT,
  "action": networkManager.Action.DENY,
  "protocol": networkManager.Protocol.UDP,
  "family": 1
};

// Remove the specified firewall rule.
try {
  networkManager.removeFirewallRule(wantTemp, firewallRule);
  console.info('Succeeded in removing firewall rule.');
} catch (err) {
  console.error(\`Failed to remove firewall rule. Code: ${err.code}, message: ${err.message}\`);
}

// Remove all firewall rules.
try {
  networkManager.removeFirewallRule(wantTemp);
  console.info('Succeeded in removing all firewall rule.');
} catch (err) {
  console.error(\`Failed to remove all firewall rule. Code: ${err.code}, message: ${err.message}\`);
}

#### networkManager.getFirewallRules

getFirewallRules(admin: Want): Array<FirewallRule>

Checks firewall rules of the device. IPv4 and IPv6 are supported since API version 22. In API version 21 and earlier versions, only IPv4 is supported.

**Required permissions**: ohos.permission.ENTERPRISE\_MANAGE\_NETWORK

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |

**Return value**

| Type | Description |
| :-- | :-- |
| Array<[FirewallRule](#firewallrule)\> | A list of firewall rules configured for the device is returned. If the operation fails, an exception will be thrown. |

**Error codes**

For details about the error codes, see [Enterprise Device Management Error Codes](../../error-codes/enterprise-device-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { networkManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
let firewallRule: Array<networkManager.FirewallRule>;
try {
  firewallRule = networkManager.getFirewallRules(wantTemp);
  console.info('Succeeded in getting firewall rules');
} catch (err) {
  console.error(\`Failed to get firewall rules. Code: ${err.code}, message: ${err.message}\`);
}

#### networkManager.addDomainFilterRule

addDomainFilterRule(admin: Want, domainFilterRule: DomainFilterRule): void

Adds domain name filtering rules for the device. IPv4 and IPv6 are supported since API version 22. In API version 21 and earlier versions, only IPv4 is supported.

After a rule with [Action](#action) set to **ALLOW** is added, a rule with **Action** set to **DENY** is added by default to discard or intercept all packets for domain name resolution that do not meet the **ALLOW** rule.

After the device is restarted, the domain name filtering rules are cleared.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/K4mZ3yecQYeaC_ZIaC7WKQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062406Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A0ADC6F59842988CC39C1F919DF8511EE3C1979543E20C9593C2FF1D804D8B23)

To prevent interception rules from becoming ineffective due to DNS caching, it is recommended that you configure domain name filtering rules immediately after the system starts up. If interception fails because of DNS caching, restart the system to clear the cache and restore the interception function.

**Required permissions**: ohos.permission.ENTERPRISE\_MANAGE\_NETWORK

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| domainFilterRule | [DomainFilterRule](#domainfilterrule) | Yes | Domain name filtering rule to add. |

**Error codes**

For details about the error codes, see [Enterprise Device Management Error Codes](../../error-codes/enterprise-device-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { networkManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
let domainFilterRule: networkManager.DomainFilterRule = {
  // Replace with actual values.
  "domainName": "www.example.com",
  "appUid": "9696",
  "action": networkManager.Action.DENY,
  "family": 1
};

try {
  networkManager.addDomainFilterRule(wantTemp, domainFilterRule);
  console.info('Succeeded in adding domain filter rules');
} catch (err) {
  console.error(\`Failed to add domain filter rules. Code: ${err.code}, message: ${err.message}\`);
}

#### networkManager.removeDomainFilterRule

removeDomainFilterRule(admin: Want, domainFilterRule?: DomainFilterRule): void

Removes domain name filtering rules for the device. IPv4 and IPv6 are supported since API version 22. In API version 21 and earlier versions, only IPv4 is supported.

If there is no rule with [Action](#action) being **ALLOW** after the rule is removed, the **DENY** rules that are added by default with [addDomainFilterRule](#networkmanageradddomainfilterrule) will be removed.

**Required permissions**: ohos.permission.ENTERPRISE\_MANAGE\_NETWORK

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| domainFilterRule | [DomainFilterRule](#domainfilterrule) | No | Domain name filtering rule to remove. If the value is empty, all domain name filtering rules will be removed. |

**Error codes**

For details about the error codes, see [Enterprise Device Management Error Codes](../../error-codes/enterprise-device-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { networkManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

let domainFilterRule: networkManager.DomainFilterRule = {
  // Replace with actual values.
  "domainName": "www.example.com",
  "appUid": "9696",
  "action": networkManager.Action.DENY,
  "family": 1
};

// Remove the specified firewall rule.
try {
  networkManager.removeDomainFilterRule(wantTemp, domainFilterRule);
  console.info('Succeeded in removing domain filter rules');
} catch (err) {
  console.error(\`Failed to remove domain filter rules. Code: ${err.code}, message: ${err.message}\`);
}

// Remove all firewall rules.
try {
  networkManager.removeDomainFilterRule(wantTemp);
  console.info('Succeeded in removing all domain filter rules');
} catch (err) {
  console.error(\`Failed to remove all domain filter rules. Code: ${err.code}, message: ${err.message}\`);
}

#### networkManager.getDomainFilterRules

getDomainFilterRules(admin: Want): Array<DomainFilterRule>

Checks domain name filtering rules of the device. IPv4 and IPv6 are supported since API version 22. In API version 21 and earlier versions, only IPv4 is supported.

**Required permissions**: ohos.permission.ENTERPRISE\_MANAGE\_NETWORK

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |

**Return value**

| Type | Description |
| :-- | :-- |
| Array<[DomainFilterRule](#domainfilterrule)\> | A list of domain name filtering rules configured for the device is returned. If the operation fails, an exception will be thrown. |

**Error codes**

For details about the error codes, see [Enterprise Device Management Error Codes](../../error-codes/enterprise-device-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { networkManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
let domainFilterRule: Array<networkManager.DomainFilterRule>;
try {
  domainFilterRule = networkManager.getDomainFilterRules(wantTemp);
  console.info('Succeeded in getting  domain filter rules');
} catch (err) {
  console.error(\`Failed to get domain filter rules. Code: ${err.code}, message: ${err.message}\`);
}

#### networkManager.turnOnMobileData20+

turnOnMobileData(admin: Want, isForce: boolean): void

Turns on mobile data.

**Required permissions**: ohos.permission.ENTERPRISE\_MANAGE\_NETWORK

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| isForce | boolean | Yes | 
Whether to forcibly enable mobile data.

The value **true** means to forcibly enable mobile data. Once enabled, it cannot be turned off manually; it can only be disabled via the [turnOffMobileData](#networkmanagerturnoffmobiledata20) API. The value **false** means not to forcibly enable mobile data. It can be turned off manually.

 |

**Error codes**

For details about the error codes, see [Enterprise Device Management Error Codes](../../error-codes/enterprise-device-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**Example**

import { networkManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
try {
  networkManager.turnOnMobileData(wantTemp, true);
  console.info(\`Turn on mobile data succeeded\`);
} catch (err) {
  console.error(\`Failed to turn on mobile data. Code: ${err.code}, message: ${err.message}\`);
}

#### networkManager.turnOffMobileData20+

turnOffMobileData(admin: Want): void

Turns off mobile data.

**Required permissions**: ohos.permission.ENTERPRISE\_MANAGE\_NETWORK

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |

**Error codes**

For details about the error codes, see [Enterprise Device Management Error Codes](../../error-codes/enterprise-device-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**Example**

import { networkManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
try {
  networkManager.turnOffMobileData(wantTemp);
  console.info(\`Turn off mobile data succeeded\`);
} catch (err) {
  console.error(\`Failed to turn off mobile data. Code: ${err.code}, message: ${err.message}\`);
}

#### networkManager.addApn20+

addApn(admin: Want, apnInfo: Record<string, string>): void

Adds an access point name (APN).

**Required permissions**: ohos.permission.ENTERPRISE\_MANAGE\_APN

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| apnInfo | Record<string, string> | Yes | 
APN information to be added.

\- **apnName**: APN identifier, which is mandatory.

\- **mcc**: 3-digit mobile country code (MCC), which is mandatory.

\- **mnc**: 2-digit or 3-digit mobile network code (MNC), which is mandatory.

\- **apn**: access point name, which is mandatory.

\- **type**: APN service type, which is optional.

\- **user**: user name for APN authentication, which is optional.

\- **password**: password for APN authentication, which is optional.

\- **proxy**: address of the proxy server for a common data connection, which is optional.

\- **mmsproxy**: dedicated proxy address of the MMS service, which is optional.

\- **authType**: authentication protocol type of the APN, which is optional.

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
import { networkManager } from '@kit.MDMKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility',
};
let apnInfo: Record<string, string> = {
  // Replace with actual values.
  "apnName": "CTNET",
  "apn": "CTNET",
  "mnc": "11",
  "mcc": "460",
};
try {
  networkManager.addApn(wantTemp, apnInfo);
  console.info(\`Succeeded in adding apn.\`);
} catch (err) {
  console.error(\`Failed to add apn. Code: ${err.code}, message: ${err.message}\`);
}

#### networkManager.deleteApn20+

deleteApn(admin: Want, apnId: string): void

Deletes the APN.

**Required permissions**: ohos.permission.ENTERPRISE\_MANAGE\_APN

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| apnId | string | Yes | APN ID to be deleted. You can obtain device information using [networkManager.queryApn](#networkmanagerqueryapn20). |

**Error codes**

For details about the error codes, see [Enterprise Device Management Error Codes](../../error-codes/enterprise-device-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**Example**

import { Want } from '@kit.AbilityKit';
import { networkManager } from '@kit.MDMKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility',
};
let apnId: string = "1"; // Replace it as required.
try {
  networkManager.deleteApn(wantTemp, apnId);
  console.info(\`Succeeded in deleting apn.\`);
} catch (err) {
  console.error(\`Failed to delete apn. Code: ${err.code}, message: ${err.message}\`);
}

#### networkManager.updateApn20+

updateApn(admin: Want, apnInfo: Record<string, string>, apnId: string): void

Updates the APN.

**Required permissions**: ohos.permission.ENTERPRISE\_MANAGE\_APN

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| apnInfo | Record<string, string> | Yes | 
APN information to be updated.

\- **apnName**: APN identifier, which is optional.

\- **mcc**: 3-digit mobile country code (MCC), which is optional.

\- **mnc**: 2-digit or 3-digit mobile network code (MNC), which is optional.

\- **APN**: access point name, which is optional.

\- **type**: APN service type, which is optional.

\- **user**: user name for APN authentication, which is optional.

\- **password**: password for APN authentication, which is optional.

\- **proxy**: address of the proxy server for a common data connection, which is optional.

\- **mmsproxy**: dedicated proxy address of the MMS service, which is optional.

\- **authType**: authentication protocol type of the APN, which is optional.

 |
| apnId | string | Yes | APN ID to be updated. You can obtain device information using [networkManager.queryApn](#networkmanagerqueryapn20). |

**Error codes**

For details about the error codes, see [Enterprise Device Management Error Codes](../../error-codes/enterprise-device-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**Example**

import { Want } from '@kit.AbilityKit';
import { networkManager } from '@kit.MDMKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility',
};
let apnInfo: Record<string, string> = {
  // Replace with actual values.
  "apnName": "CTNET",
  "apn": "CTNET",
  "mnc": "11",
  "mcc": "460",
};
let apnId: string = "1"; // Replace it as required.
try {
  networkManager.updateApn(wantTemp, apnInfo, apnId);
  console.info(\`Succeeded in updating apn.\`);
} catch (err) {
  console.error(\`Failed to update apn. Code: ${err.code}, message: ${err.message}\`);
}

#### networkManager.setPreferredApn20+

setPreferredApn(admin: Want, apnId: string): void

Sets the preferred APN.

**Required permissions**: ohos.permission.ENTERPRISE\_MANAGE\_APN

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| apnId | string | Yes | Preferred APN ID to be set. You can obtain device information using [networkManager.queryApn](#networkmanagerqueryapn20). |

**Error codes**

For details about the error codes, see [Enterprise Device Management Error Codes](../../error-codes/enterprise-device-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**Example**

import { Want } from '@kit.AbilityKit';
import { networkManager } from '@kit.MDMKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility',
};
let apnId: string = "1"; // Replace it as required.
try {
  networkManager.setPreferredApn(wantTemp, apnId);
  console.info(\`Succeeded in setting preferred apn.\`);
} catch (err) {
  console.error(\`Failed to set preferred apn. Code: ${err.code}, message: ${err.message}\`);
}

#### networkManager.queryApn20+

queryApn(admin: Want, apnInfo: Record<string, string>): Array<string>

Queries the APN ID.

**Required permissions**: ohos.permission.ENTERPRISE\_MANAGE\_APN

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| apnInfo | Record<string, string> | Yes | 
APN information.

\- **apnName**: APN identifier, which is optional.

\- **mcc**: 3-digit mobile country code (MCC), which is optional.

\- **mnc**: 2-digit or 3-digit mobile network code (MNC), which is optional.

\- **apn**: access point name, which is optional.

\- **type**: APN service type, which is optional.

\- **user**: user name for APN authentication, which is optional.

\- **proxy**: address of the proxy server for a common data connection, which is optional.

\- **mmsproxy**: dedicated proxy address of the MMS service, which is optional.

\- **authType**: authentication protocol type of the APN, which is optional.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Array<string> | APN ID obtained. |

**Error codes**

For details about the error codes, see [Enterprise Device Management Error Codes](../../error-codes/enterprise-device-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**Example**

import { Want } from '@kit.AbilityKit';
import { networkManager } from '@kit.MDMKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility',
};
let apnInfo: Record<string, string> = {
  // Replace with actual values.
  "apnName": "CTNET",
  "apn": "CTNET",
  "mnc": "11",
  "mcc": "460",
};
try {
  let queryResult: Array<string> = networkManager.queryApn(wantTemp, apnInfo);
  console.info(\`Succeeded in querying apn, result : ${JSON.stringify(queryResult)}\`);
} catch (err) {
  console.error(\`Failed to query apn. Code: ${err.code}, message: ${err.message}\`);
}

#### networkManager.queryApn20+

queryApn(admin: Want, apnId: string): Record<string, string>

Queries the APN parameter information.

**Required permissions**: ohos.permission.ENTERPRISE\_MANAGE\_APN

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| apnId | string | Yes | Specified APN ID. You can obtain device information using [networkManager.queryApn](#networkmanagerqueryapn20). |

**Return value**

| Type | Description |
| :-- | :-- |
| Record<string, string> | 
APN parameter information of the specified APN ID.

\- **apnName**: APN identifier.

\- **mcc**: 3-digit mobile country code (MCC).

\- **mnc**: 2-digit or 3-digit mobile network code (MNC).

\- **apn**: access point name.

\- **type**: APN service type.

\- **user**: user name for APN authentication.

\- **proxy**: address of the proxy server for a common data connection.

\- **mmsproxy**: dedicated proxy address of the MMS service.

\- **authType**: authentication protocol type of the APN.

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
import { networkManager } from '@kit.MDMKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility',
};
let apnId: string = "1"; // Replace it as required.
try {
  let queryResult: Record<string, string> = networkManager.queryApn(wantTemp, apnId);
  console.info(\`Succeeded in querying apn, result : ${JSON.stringify(queryResult)}\`);
} catch (err) {
  console.error(\`Failed to query apn. Code: ${err.code}, message: ${err.message}\`);
}

#### FirewallRule

Represents a firewall rule. IPv4 and IPv6 are supported since API version 22. In API version 21 and earlier versions, only IPv4 is supported.

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

| Name | Type | Read-only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| srcAddr | string | No | Yes | Source IP address. An IP address segment, for example, **192.168.0.0/22** or **192.168.1.100-192.168.1.200** is supported. |
| destAddr | string | No | Yes | Destination IP address. An IP address segment, for example, **192.168.0.0/22** or **192.168.1.100-192.168.1.200** is supported. |
| srcPort | string | No | Yes | Source port. |
| destPort | string | No | Yes | Destination port. |
| appUid | string | No | Yes | UID of the application. |
| direction | [Direction](#direction) | No | Yes | 
Direction chains to which the rule applies.

This parameter is mandatory when a firewall filtering rule is added.

This parameter is optional when a firewall is removed. If this parameter is left empty, all [Direction](#direction) chains are cleared, and **srcAddr**, **destAddr**, **srcPort**, **destPort**, and **appUid** must be also left empty.

 |
| action | [Action](#action) | No | Yes | 

Action to take, that is, receive or discard the data packets.

This parameter is mandatory when a firewall filtering rule is added.

This parameter is optional when a firewall is removed. If this parameter is left empty, all [Action](#action) chains are cleared, and **srcAddr**, **destAddr**, **srcPort**, **destPort**, and **appUid** must be also left empty.

 |
| protocol | [Protocol](#protocol) | No | Yes | Network protocol. If the value is **ALL** or **ICMP**, the settings of **srcPort** and **destPort** are invalid. |
| family22+ | number | No | Yes | IP protocol version. The value can be **1** (IPv4) or **2** (IPv6). |

#### DomainFilterRule

Represents a domain name filtering rule. IPv4 and IPv6 are supported since API version 22. In API version 21 and earlier versions, only IPv4 is supported.

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

| Name | Type | Read-only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| domainName | string | No | Yes | Domain name. This parameter is mandatory when a domain name filtering rule is added. Segment matching is supported. For example, if **domainName** is set to **example.com**, **example.com**, **[www.example.com](http://www.example.com)**, and **[www.test.example.com](http://www.test.example.com)** will be matched, while **linkexample.com** will not be matched. |
| appUid | string | No | Yes | UID of the application. |
| action | [Action](#action) | No | Yes | 
Action to take, that is, receive or discard the data packets.

This parameter is mandatory when a domain name filtering rule is added.

This parameter is optional when a domain name filtering rule is removed. If this parameter is left empty, all [Action](#action) chains are cleared, and **domainName** and **appUid** must be also left empty.

 |
| direction15+ | [Direction](#direction) | No | Yes | 

Direction chains to which the rule applies.

This parameter is optional when a domain name filtering rule is added. If this parameter is set to output chain or input chain, the output chain takes effect. If this parameter is set to a forward chain, **appUid** must be empty. Otherwise, error code 401 will be returned.

This parameter is optional when a domain name filtering rule is removed. If the value is empty, all [Direction](#direction) chains are cleared, and **domainName** and **appUid** must be empty.

 |
| family22+ | number | No | Yes | IP protocol version. The value can be **1** (IPv4) or **2** (IPv6). |

#### Direction

Enumerates the direction chains to which the rule applies.

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

| Name | Value | Description |
| :-- | :-- | :-- |
| INPUT | 0 | Input chain. |
| OUTPUT | 1 | Output chain. |
| FORWARD15+ | 2 | Forward chain. |

#### Action

Enumerates the actions that can be taken for data packets.

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

| Name | Value | Description |
| :-- | :-- | :-- |
| ALLOW | 0 | Receive data packets. |
| DENY | 1 | Discard data packets. |
| REJECT15+ | 2 | Reject data packets. |

#### Protocol

Enumerates network protocols.

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

| Name | Value | Description |
| :-- | :-- | :-- |
| ALL | 0 | All network protocols. |
| TCP | 1 | TCP. |
| UDP | 2 | UDP. |
| ICMP | 3 | ICMP. |
