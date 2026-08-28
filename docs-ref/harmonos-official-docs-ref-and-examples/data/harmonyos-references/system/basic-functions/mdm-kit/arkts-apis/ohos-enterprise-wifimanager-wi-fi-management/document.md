# @ohos.enterprise.wifiManager (Wi-Fi Management)

The **wifiManager** module provides Wi-Fi management capabilities for enterprise devices, including obtaining the Wi-Fi status.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/HfVZPJ4NSemoq5ygnfRP1A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062406Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9A143719294A6DFC9061BAF44CD9C964D1771CA6EE0FACD8A2A315FEDEE01527)

The initial APIs of this module are supported since API version 12. Newly added APIs will be marked with a superscript to indicate their earliest API version.

The APIs of this module can be used only in the stage model.

The APIs of this module can be called only by a device administrator application that is enabled. For details, see [MDM Kit Development](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/mdm-kit-guide).

The global restriction policies are provided by **restrictions**. To disable Wi-Fi globally, see [@ohos.enterprise.restrictions](../ohos-enterprise-restrictions-restrictions/document.md).

#### Modules to Import

import { wifiManager } from '@kit.MDMKit';

#### wifiManager.isWifiActiveSync

isWifiActiveSync(admin: Want): boolean

Queries the Wi-Fi status of the current device.

**Required permissions**: ohos.permission.ENTERPRISE\_MANAGE\_WIFI

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns the Wi-Fi status. The value **true** means Wi-Fi is enabled, and the value **false** means the opposite. |

**Error codes**

For details about the error codes, see [Enterprise Device Management Error Codes](../../error-codes/enterprise-device-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { wifiManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility',
};

try {
  let result: boolean = wifiManager.isWifiActiveSync(wantTemp);
  console.info(\`Succeeded in querying whether the Wi-Fi is active or not, result : ${result}\`);
} catch (err) {
  console.error(\`Failed to query whether the Wi-Fi is active or not. Code: ${err.code}, message: ${err.message}\`);
}

#### wifiManager.setWifiProfileSync

setWifiProfileSync(admin: Want, profile: WifiProfile): void

Configures Wi-Fi for the current device to connect to a specified network.

**Required permissions**: ohos.permission.ENTERPRISE\_MANAGE\_WIFI

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| profile | [WifiProfile](#wifiprofile) | Yes | Wi-Fi configuration information. |

**Error codes**

For details about the error codes, see [Enterprise Device Management Error Codes](../../error-codes/enterprise-device-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

Scenario 1: public Wi-Fi development

import { wifiManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility',
};

let profile: wifiManager.WifiProfile = {
  // Replace with actual values.
  'ssid': 'guest-Wi-Fi',
  'preSharedKey': '',
  'securityType': wifiManager.WifiSecurityType.WIFI\_SEC\_TYPE\_OPEN
};

try {
  wifiManager.setWifiProfileSync(wantTemp, profile);
  console.info(\`Succeeded in setting Wi-Fi profile.\`);
} catch (err) {
  console.error(\`Failed to set Wi-Fi profile. Code: ${err.code}, message: ${err.message}\`);
}

**Multiple Wi-Fi networks with the same name but different BSSIDs**

import { wifiManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility',
};

let profile: wifiManager.WifiProfile = {
  // Replace with actual values.
  'ssid': 'guest-Wi-Fi',
  'bssid': 'AA:BB:CC:DD:EE:FF',
  'preSharedKey': '',
  'securityType': wifiManager.WifiSecurityType.WIFI\_SEC\_TYPE\_OPEN
};

try {
  wifiManager.setWifiProfileSync(wantTemp, profile);
  console.info(\`Succeeded in setting Wi-Fi profile.\`);
} catch (err) {
  console.error(\`Failed to set Wi-Fi profile. Code: ${err.code}, message: ${err.message}\`);
}

Scenario 3: old industrial devices with low security

import { wifiManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility',
};

let profile: wifiManager.WifiProfile = {
  // Replace with actual values.
  'ssid': 'Legacy-Office-Wi-Fi',
  'bssid': 'AA:BB:CC:DD:EE:FF',
  'preSharedKey': '',
  'securityType': wifiManager.WifiSecurityType.WIFI\_SEC\_TYPE\_WEP
};

try {
  wifiManager.setWifiProfileSync(wantTemp, profile);
  console.info(\`Succeeded in setting Wi-Fi profile.\`);
} catch (err) {
  console.error(\`Failed to set Wi-Fi profile. Code: ${err.code}, message: ${err.message}\`);
}

Scenario 4: home networks, small offices, and consumer routers

import { wifiManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility',
};

let profile: wifiManager.WifiProfile = {
  // Replace with actual values.
  'ssid': 'home\_Wi-Fi',
  'preSharedKey': 'passwd',
  'securityType': wifiManager.WifiSecurityType.WIFI\_SEC\_TYPE\_PSK
};

try {
  wifiManager.setWifiProfileSync(wantTemp, profile);
  console.info(\`Succeeded in setting Wi-Fi profile.\`);
} catch (err) {
  console.error(\`Failed to set Wi-Fi profile. Code: ${err.code}, message: ${err.message}\`);
}

Scenario 5: modern IoT device networks

import { wifiManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility',
};

let profile: wifiManager.WifiProfile = {
  // Replace with actual values.
  'ssid': 'iot\_Wi-Fi',
  'preSharedKey': 'passwd',
  'securityType': wifiManager.WifiSecurityType.WIFI\_SEC\_TYPE\_SAE
};

try {
  wifiManager.setWifiProfileSync(wantTemp, profile);
  console.info(\`Succeeded in setting Wi-Fi profile.\`);
} catch (err) {
  console.error(\`Failed to set Wi-Fi profile. Code: ${err.code}, message: ${err.message}\`);
}

Scenario 6: company networks and university campus networks

import { wifiManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility',
};

// EAP-PEAP configuration example
let profile: wifiManager.WifiProfile = {
  // Replace with actual values.
  'ssid': 'company\_Wi-Fi',
  'preSharedKey': '',
  'securityType': wifiManager.WifiSecurityType.WIFI\_SEC\_TYPE\_EAP,
  'eapProfile': {
    eapMethod: wifiManager.EapMethod.EAP\_PEAP,
    phase2Method: wifiManager.Phase2Method.PHASE2\_MSCHAPV2,
    identity: 'zhangsan@company.com',
    password: 'passwd',
    anonymousIdentity: '',
    caPath: '/system/etc/security/caCerts/company-ca.pem',
    caCertAliases:  '',
    clientCertAliases: '',
    certEntry: new Uint8Array(),
    certPassword: '',
    altSubjectMatch: 'CN=radius.company.com,OU=IT Department,O=Company Inc.,C=US',
    domainSuffixMatch: 'company.com',
    realm: '',
    eapSubId: 0,
    plmn: ''
  }
};

try {
  wifiManager.setWifiProfileSync(wantTemp, profile);
  console.info(\`Succeeded in setting Wi-Fi profile.\`);
} catch (err) {
  console.error(\`Failed to set Wi-Fi profile. Code: ${err.code}, message: ${err.message}\`);
}

import { wifiManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility',
};

// EAP-TLS configuration example
let profile: wifiManager.WifiProfile = {
  // Replace with actual values.
  'ssid': 'tls\_Wi-Fi',
  'preSharedKey': '',
  'securityType': wifiManager.WifiSecurityType.WIFI\_SEC\_TYPE\_EAP,
  'eapProfile': {
    eapMethod: wifiManager.EapMethod.EAP\_TLS,
    phase2Method: wifiManager.Phase2Method.PHASE2\_NONE,
    identity: 'zhangsan@company.com',
    password: '',
    anonymousIdentity: '',
    caPath: '/system/etc/security/caCerts/company-ca.pem',
    caCertAliases: '',
    clientCertAliases: 'zhangsan-auth-cert',
    certEntry: new Uint8Array(),
    certPassword: '',
    altSubjectMatch: 'CN=radius.company.com,OU=IT Department,O=Company Inc.,C=US',
    domainSuffixMatch: 'company.com',
    realm: '',
    eapSubId: 0,
    plmn: ''
  }
};

try {
  wifiManager.setWifiProfileSync(wantTemp, profile);
  console.info(\`Succeeded in setting Wi-Fi profile.\`);
} catch (err) {
  console.error(\`Failed to set Wi-Fi profile. Code: ${err.code}, message: ${err.message}\`);
}

import { wifiManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility',
};

// EAP-TTLS configuration example
let profile: wifiManager.WifiProfile = {
  // Replace with actual values.
  'ssid': 'ttls\_Wi-Fi',
  'preSharedKey': '',
  'securityType': wifiManager.WifiSecurityType.WIFI\_SEC\_TYPE\_EAP,
  'eapProfile': {
    eapMethod: wifiManager.EapMethod.EAP\_TTLS,
    phase2Method: wifiManager.Phase2Method.PHASE2\_GTC,
    identity: 'zhangsan@company.com',
    password: '123456', // Dynamic password generated based on the token.
    anonymousIdentity: '',
    caPath: '',
    caCertAliases: 'company-ca',
    clientCertAliases: '',
    certEntry: new Uint8Array(),
    certPassword: '',
    altSubjectMatch: 'CN=radius.company.com,OU=IT Department,O=Company Inc.,C=US',
    domainSuffixMatch: 'company.com',
    realm: 'company.com',
    plmn: '',
    eapSubId: 0,
  }
};

try {
  wifiManager.setWifiProfileSync(wantTemp, profile);
  console.info(\`Succeeded in setting Wi-Fi profile.\`);
} catch (err) {
  console.error(\`Failed to set Wi-Fi profile. Code: ${err.code}, message: ${err.message}\`);
}

import { wifiManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility',
};

// EAP-SIM configuration example
let profile: wifiManager.WifiProfile = {
  // Replace with actual values.
  'ssid': 'eap\_sim\_Wi-Fi',
  'preSharedKey': '',
  'securityType': wifiManager.WifiSecurityType.WIFI\_SEC\_TYPE\_EAP,
  'eapProfile': {
    eapMethod: wifiManager.EapMethod.EAP\_SIM,
    phase2Method: wifiManager.Phase2Method.PHASE2\_NONE,
    identity: '',
    password:'',
    anonymousIdentity: '',
    caPath: '',
    caCertAliases:  'carrier-root-ca',
    clientCertAliases: '',
    certEntry: new Uint8Array(),
    certPassword: '',
    altSubjectMatch: 'CN=radius.company.com,OU=IT Department,O=Company Inc.,C=US',
    domainSuffixMatch: 'company.com',
    realm: 'waln.mnc000.mcc460.3gppnetwork.org',
    eapSubId: 0,
    plmn: '46000'
  }
};

try {
  wifiManager.setWifiProfileSync(wantTemp, profile);
  console.info(\`Succeeded in setting Wi-Fi profile.\`);
} catch (err) {
  console.error(\`Failed to set Wi-Fi profile. Code: ${err.code}, message: ${err.message}\`);
}

Scenario 7: fixed IP address for client access

import { wifiManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility',
};

let profile: wifiManager.WifiProfile = {
  // Replace with actual values.
  'ssid': 'static\_ip\_Wi-Fi',
  'preSharedKey': 'passwd',
  'securityType': wifiManager.WifiSecurityType.WIFI\_SEC\_TYPE\_PSK,
  'ipType': wifiManager.IpType.STATIC,
  'staticIp': {
    ipAddress: 3232235778, // 192.168.1.2
    gateway: 3232235777, // 192.168.1.1
    prefixLength: 24,
    dnsServers: \[3232235777, 3232235777\],
    domains: \[\]
  }
};

try {
  wifiManager.setWifiProfileSync(wantTemp, profile);
  console.info(\`Succeeded in setting Wi-Fi profile.\`);
} catch (err) {
  console.error(\`Failed to set Wi-Fi profile. Code: ${err.code}, message: ${err.message}\`);
}

#### wifiManager.addAllowedWifiList19+

addAllowedWifiList(admin: Want, list: Array<WifiAccessInfo>): void

Adds allowed Wi-Fi networks. The current device can only connect to the allowed Wi-Fi networks.

A policy conflict is reported when this API is called in the following scenarios:

1.  Wi-Fi networks have been disabled by calling [setDisallowedPolicy](../ohos-enterprise-restrictions-restrictions/document.md#restrictionssetdisallowedpolicy). You can resolve the conflict by enabling the Wi-Fi networks through [setDisallowedPolicy](../ohos-enterprise-restrictions-restrictions/document.md#restrictionssetdisallowedpolicy).
2.  Disallowed Wi-Fi networks have been added by calling [addDisallowedWifiList](#wifimanageradddisallowedwifilist19). You can resolve the conflict by removing the disallowed Wi-Fi networks through [removeDisallowedWifiList](#wifimanagerremovedisallowedwifilist19).

**Required permissions**: ohos.permission.ENTERPRISE\_MANAGE\_WIFI

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| list | Array<[WifiAccessInfo](#wifiaccessinfo19)\> | Yes | Array of allowed Wi-Fi networks. The maximum length of the array is 200. For example, if there are already 100 Wi-Fi networks, a maximum of 100 more can be added. |

**Error codes**

For details about the error codes, see [Enterprise Device Management Error Codes](../../error-codes/enterprise-device-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9200010 | A conflict policy has been configured. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**Example**

import { wifiManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.edmtest',
  abilityName: 'com.example.edmtest.EnterpriseAdminAbility'
};
try {
  let wifiIds: Array<wifiManager.WifiAccessInfo> = \[{
    // Replace with actual values.
    ssid: "wifi\_name",
    bssid: "68:77:24:77:A6:D8"
  }\];
  wifiManager.addAllowedWifiList(wantTemp, wifiIds);
  console.info(\`Succeeded in adding allowed Wi-Fi list.\`);
} catch (err) {
  console.error(\`Failed to add allowed Wi-Fi list. Code: ${err.code}, message: ${err.message}\`);
}

#### wifiManager.removeAllowedWifiList19+

removeAllowedWifiList(admin: Want, list: Array<WifiAccessInfo>): void

Removes Wi-Fi networks from the allowed list. If some Wi-Fi networks are removed from the allowed list, the current device can only connect to the remaining ones; if all Wi-Fi networks are removed from the allowed list, the current device can connect to any Wi-Fi network.

**Required permissions**: ohos.permission.ENTERPRISE\_MANAGE\_WIFI

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| list | Array<[WifiAccessInfo](#wifiaccessinfo19)\> | Yes | Array of Wi-Fi networks to be removed from the allowed list. The maximum length of the array is 200. |

**Error codes**

For details about the error codes, see [Enterprise Device Management Error Codes](../../error-codes/enterprise-device-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**Example**

import { wifiManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.edmtest',
  abilityName: 'EnterpriseAdminAbility'
};
try {
  let wifiIds: Array<wifiManager.WifiAccessInfo> = \[{
    // Replace with actual values.
    ssid: "wifi\_name",
    bssid: "68:77:24:77:A6:D8"
  }\];
  wifiManager.removeAllowedWifiList(wantTemp, wifiIds);
  console.info(\`Succeeded in removing allowed Wi-Fi list.\`);
} catch (err) {
  console.error(\`Failed to remove allowed Wi-Fi list. Code: ${err.code}, message: ${err.message}\`);
}

#### wifiManager.getAllowedWifiList19+

getAllowedWifiList(admin: Want): Array<WifiAccessInfo>

Obtains Wi-Fi networks from the allowed list.

**Required permissions**: ohos.permission.ENTERPRISE\_MANAGE\_WIFI

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |

**Return value**

| Type | Description |
| :-- | :-- |
| Array<[WifiAccessInfo](#wifiaccessinfo19)\> | Array of allowed Wi-Fi networks. |

**Error codes**

For details about the error codes, see [Enterprise Device Management Error Codes](../../error-codes/enterprise-device-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**Example**

import { wifiManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.edmtest',
  abilityName: 'EnterpriseAdminAbility'
};
try {
  let result: Array<wifiManager.WifiAccessInfo> = wifiManager.getAllowedWifiList(wantTemp);
  console.info(\`Succeeded in getting allowed Wi-Fi list. Result: ${JSON.stringify(result)}\`);
} catch (err) {
  console.error(\`Failed to get allowed Wi-Fi list. Code: ${err.code}, message: ${err.message}\`);
}

#### wifiManager.addDisallowedWifiList19+

addDisallowedWifiList(admin: Want, list: Array<WifiAccessInfo>): void

Adds disallowed Wi-Fi networks. The current device cannot connect to the disallowed Wi-Fi networks.

A policy conflict is reported when this API is called in the following scenarios:

1.  Wi-Fi networks have been disabled by calling [setDisallowedPolicy](../ohos-enterprise-restrictions-restrictions/document.md#restrictionssetdisallowedpolicy). You can resolve the conflict by enabling the Wi-Fi networks through [setDisallowedPolicy](../ohos-enterprise-restrictions-restrictions/document.md#restrictionssetdisallowedpolicy).
2.  Allowed Wi-Fi networks have been added by calling [addAllowedWifiList](#wifimanageraddallowedwifilist19). You can resolve the conflict by removing the allowed Wi-Fi networks through [removeAllowedWifiList](#wifimanagerremoveallowedwifilist19).

**Required permissions**: ohos.permission.ENTERPRISE\_MANAGE\_WIFI

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| list | Array<[WifiAccessInfo](#wifiaccessinfo19)\> | Yes | Array of disallowed Wi-Fi networks. The maximum length of the array is 200. For example, if there are already 100 Wi-Fi networks, a maximum of 100 more can be added. |

**Error codes**

For details about the error codes, see [Enterprise Device Management Error Codes](../../error-codes/enterprise-device-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9200010 | A conflict policy has been configured. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**Example**

import { wifiManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.edmtest',
  abilityName: 'EnterpriseAdminAbility'
};
try {
  let wifiIds: Array<wifiManager.WifiAccessInfo> = \[{
    // Replace with actual values.
    ssid: "wifi\_name",
    bssid: "68:77:24:77:A6:D8"
  }\];
  wifiManager.addDisallowedWifiList(wantTemp, wifiIds);
  console.info(\`Succeeded in adding disallowed Wi-Fi list.\`);
} catch (err) {
  console.error(\`Failed to add disallowed Wi-Fi list. Code: ${err.code}, message: ${err.message}\`);
}

#### wifiManager.removeDisallowedWifiList19+

removeDisallowedWifiList(admin: Want, list: Array<WifiAccessInfo>): void

Removes disallowed Wi-Fi networks. If some Wi-Fi networks are removed from the disallowed list, the current device cannot connect to the remaining ones; if all Wi-Fi networks are removed from the disallowed list, the current device can connect to any Wi-Fi network.

**Required permissions**: ohos.permission.ENTERPRISE\_MANAGE\_WIFI

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| list | Array<[WifiAccessInfo](#wifiaccessinfo19)\> | Yes | Array of Wi-Fi networks to be removed. The maximum length of the array is 200. |

**Error codes**

For details about the error codes, see [Enterprise Device Management Error Codes](../../error-codes/enterprise-device-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**Example**

import { wifiManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.edmtest',
  abilityName: 'EnterpriseAdminAbility'
};
try {
  let wifiIds: Array<wifiManager.WifiAccessInfo> = \[{
    // Replace with actual values.
    ssid: "wifi\_name",
    bssid: "68:77:24:77:A6:D8"
  }\];
  wifiManager.removeDisallowedWifiList(wantTemp, wifiIds);
  console.info(\`Succeeded in removing disallowed Wi-Fi list.\`);
} catch (err) {
  console.error(\`Failed to remove disallowed Wi-Fi list. Code: ${err.code}, message: ${err.message}\`);
}

#### wifiManager.getDisallowedWifiList19+

getDisallowedWifiList(admin: Want): Array<WifiAccessInfo>

Obtains disallowed Wi-Fi networks.

**Required permissions**: ohos.permission.ENTERPRISE\_MANAGE\_WIFI

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |

**Return value**

| Type | Description |
| :-- | :-- |
| Array<[WifiAccessInfo](#wifiaccessinfo19)\> | Array of disallowed Wi-Fi networks. |

**Error codes**

For details about the error codes, see [Enterprise Device Management Error Codes](../../error-codes/enterprise-device-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**Example**

import { wifiManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.edmtest',
  abilityName: 'EnterpriseAdminAbility'
};
try {
  let result: Array<wifiManager.WifiAccessInfo> = wifiManager.getDisallowedWifiList(wantTemp);
  console.info(\`Succeeded in getting disallowed Wi-Fi list. Result: ${JSON.stringify(result)}\`);
} catch (err) {
  console.error(\`Failed to get disallowed Wi-Fi list. Code: ${err.code}, message: ${err.message}\`);
}

#### wifiManager.turnOnWifi20+

turnOnWifi(admin: Want, isForce: boolean): void

Enables Wi-Fi.

In the following scenario, attempting to enable Wi-Fi using this API will fail, and a message indicating that the system function is disabled will be returned:

​Wi-Fi has been disabled using the [setDisallowedPolicy](../ohos-enterprise-restrictions-restrictions/document.md#restrictionssetdisallowedpolicy) API. In this case, you must call [setDisallowedPolicy](../ohos-enterprise-restrictions-restrictions/document.md#restrictionssetdisallowedpolicy) to enable Wi-Fi.

**Required permissions**: ohos.permission.ENTERPRISE\_MANAGE\_WIFI

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| isForce | boolean | Yes | 
Whether to forcibly enable Wi-Fi.

The value **true** means to forcibly enable Wi-Fi. Once enabled, it cannot be disabled manually. You must call [turnOffWifi](#wifimanagerturnoffwifi20) instead. The value **false** means the opposite and the Wi-Fi can be disabled manually.

 |

**Error codes**

For details about the error codes, see [Enterprise Device Management Error Codes](../../error-codes/enterprise-device-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 203 | This function is prohibited by enterprise management policies. |

**Example**

import { Want } from '@kit.AbilityKit';
import { wifiManager } from '@kit.MDMKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  wifiManager.turnOnWifi(wantTemp, true);
  console.info(\`Succeeded in turning on Wi-Fi.\`);
} catch (err) {
  console.error(\`Failed to turn on Wi-Fi. Code: ${err.code}, message: ${err.message}\`);
}

#### wifiManager.turnOffWifi20+

turnOffWifi(admin: Want): void

Disables Wi-Fi.

In the following scenario, attempting to disable Wi-Fi using this API will fail, and a message indicating that the system function is disabled will be returned:

​Wi-Fi has been disabled using the [setDisallowedPolicy](../ohos-enterprise-restrictions-restrictions/document.md#restrictionssetdisallowedpolicy) API. In this case, you must call [setDisallowedPolicy](../ohos-enterprise-restrictions-restrictions/document.md#restrictionssetdisallowedpolicy) to enable Wi-Fi.

**Required permissions**: ohos.permission.ENTERPRISE\_MANAGE\_WIFI

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

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
| 203 | This function is prohibited by enterprise management policies. |

**Example**

import { Want } from '@kit.AbilityKit';
import { wifiManager } from '@kit.MDMKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  wifiManager.turnOffWifi(wantTemp);
  console.info(\`Succeeded in turning off Wi-Fi.\`);
} catch (err) {
  console.error(\`Failed to turn off Wi-Fi. Code: ${err.code}, message: ${err.message}\`);
}

#### WifiAccessInfo19+

Represents Wi-Fi access information containing Service Set Identifier (SSID) and Basic Service Set Identifier (BSSID).

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| ssid | string | No | No | Name of the Wi-Fi hotspot. The encoding format is UTF-8 and the maximum length is 32 bytes (three bytes for each Chinese character and one byte for each English character). |
| bssid | string | No | Yes | 
MAC address of the Wi-Fi hotspot, for example, **00:11:22:33:44:55**. To obtain the MAC address, enable **Enable Wi-Fi verbose logging** under **Settings** > **System & updates** > **Developer options** first, and then go to the WLAN list to check the MAC address. If a Wi-Fi network has multiple MAC addresses, all of them must be added here.

This property is optional when the [addDisallowedWifiList](#wifimanageradddisallowedwifilist19) and [removeDisallowedWifiList](#wifimanagerremovedisallowedwifilist19) APIs are called. The default value is an empty string.

This property is optional (available since API version 21) when the [addAllowedWifiList](#wifimanageraddallowedwifilist19) and [removeAllowedWifiList](#wifimanagerremoveallowedwifilist19) APIs are called. The default value is an empty string. However, this property is mandatory in API version 20 and earlier versions.

 |

#### WifiProfile

Represents the Wi-Fi configuration information.

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| ssid | string | No | No | Name of the Wi-Fi hotspot, in UTF-8 format. |
| bssid | string | No | Yes | MAC address of the Wi-Fi hotspot. To obtain the MAC address, enable **Enable Wi-Fi verbose logging** under **Settings** > **System & updates** > **Developer options** first, and then go to the WLAN list to check the MAC address. If a Wi-Fi network has multiple MAC addresses, all of them must be added here. |
| preSharedKey | string | No | No | Pre-shared key. |
| isHiddenSsid | boolean | No | Yes | Whether the network is hidden. The value **true** indicates that the network is hidden; the value **false** indicates the opposite. |
| securityType | [WifiSecurityType](#wifisecuritytype) | No | No | Security type. |
| creatorUid | number | No | Yes | ID of the creator. |
| disableReason | number | No | Yes | Reason for disabling Wi-Fi. |
| netId | number | No | Yes | Network ID allocated. |
| randomMacType | number | No | Yes | Random MAC. The value **0** indicates a random MAC address, and the value **1** indicates device MAC address. |
| randomMacAddr | string | No | Yes | MAC address. This field is mandatory when **randomMacType** is set to device MAC address. |
| ipType | [IpType](#iptype) | No | Yes | IP address type. |
| staticIp | [IpProfile](#ipprofile) | No | Yes | Static IP address information. This field is mandatory when **ipType** is set to **STATIC**. |
| eapProfile | [WifiEapProfile](#wifieapprofile) | No | Yes | Extensible Authentication Protocol (EAP) configuration. This field is mandatory only when **securityType** is set to **WIFI\_SEC\_TYPE\_EAP**. |

#### WifiSecurityType

Enumerates the Wi-Fi security types.

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

| Name | Value | Description |
| :-- | :-- | :-- |
| WIFI\_SEC\_TYPE\_INVALID | 0 | Invalid security type. For example, airport public Wi-Fi. |
| WIFI\_SEC\_TYPE\_OPEN | 1 | Open security type. |
| WIFI\_SEC\_TYPE\_WEP | 2 | Wired Equivalent Privacy (WEP). |
| WIFI\_SEC\_TYPE\_PSK | 3 | PSK. For example, home and small office Wi-Fi. |
| WIFI\_SEC\_TYPE\_SAE | 4 | Simultaneous Authentication of Equals (SAE). For example, smart home and small- and medium-sized enterprise networks. |
| WIFI\_SEC\_TYPE\_EAP | 5 | EAP. For example, large enterprise authentication and university campus networks. |
| WIFI\_SEC\_TYPE\_EAP\_SUITE\_B | 6 | Suite B 192-bit encryption. For example, government and high-security organization networks. |
| WIFI\_SEC\_TYPE\_OWE | 7 | Opportunistic Wireless Encryption (OWE). For example, public Wi-Fi in a coffee shop, which does not require a password to provide encryption for connections. |
| WIFI\_SEC\_TYPE\_WAPI\_CERT | 8 | WLAN Authentication and Privacy Infrastructure (WAPI) in certificate-based mode (WAPI-CERT). It is China's own wireless security standard. |
| WIFI\_SEC\_TYPE\_WAPI\_PSK | 9 | WAPI-PSK. |

#### IpType

Enumerates the IP address types.

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

| Name | Value | Description |
| :-- | :-- | :-- |
| STATIC | 0 | Static IP address, which is used in scenarios where a fixed IP address is required, for example, a fixed IP address of an office printer. |
| DHCP | 1 | Dynamic Host Configuration Protocol (DHCP), which is a service that automatically allocates IP addresses and other network configuration information to devices on a network. |
| UNKNOWN | 2 | Not specified. |

#### IpProfile

Represents IP configuration information.

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| ipAddress | number | No | No | IP address, represented in decimal format. For example, the standard dotted decimal notation **192.168.1.1** corresponds to the decimal value **3232235777**. |
| gateway | number | No | No | Default gateway, represented in decimal format, usually the IP address of the router. |
| prefixLength | number | No | No | Subnet mask. |
| dnsServers | number\[\] | No | No | DNS server. The array can contain a maximum of two addresses: the primary DNS server and the secondary DNS server. |
| domains | Array<string> | No | No | Domain information. |

#### WifiEapProfile

Represents EAP profile (configuration) information.

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| eapMethod | [EapMethod](#eapmethod) | No | No | EAP authentication method. |
| phase2Method | [Phase2Method](#phase2method) | No | No | Phase 2 authentication method. This parameter is mandatory only when **eapMethod** is **EAP\_PEAP** or **EAP\_TTLS**. |
| identity | string | No | No | Identity Information. This parameter cannot be empty when **eapMethod** is **TLS**. |
| anonymousIdentity | string | No | No | Anonymous identity. |
| password | string | No | No | Password. When **eapMethod** is **EAP\_PEAP** or **EAP\_PWD**, this parameter cannot be empty. The value contains a maximum of 128 bytes. |
| caCertAliases | string | No | No | CA certificate alias. |
| caPath | string | No | No | CA certificate path. |
| clientCertAliases | string | No | No | Client certificate alias. When the client certificate content is empty, the client certificate must be installed first via the certificate management API before passing in the alias. |
| certEntry | Uint8Array | No | No | Client certificate content. When **eapMethod** is set to **EAP\_TLS**, if this field is empty, the client certificate alias cannot be empty. |
| certPassword | string | No | No | CA certificate password. |
| altSubjectMatch | string | No | No | A string to match the alternate subject. In addition to checking the primary domain name of the certificate, the system checks whether the alternate subject name of the certificate matches the certificate. |
| domainSuffixMatch | string | No | No | A string to match the domain suffix. |
| realm | string | No | No | Realm for the passpoint credential. |
| plmn | string | No | No | Credential provider. |
| eapSubId | number | No | No | Sub-ID of the SIM card. |

#### EapMethod

Enumerates the EAP authentication methods.

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

| Name | Value | Description |
| :-- | :-- | :-- |
| EAP\_NONE | 0 | Not specified. |
| EAP\_PEAP | 1 | Protected Extensible Authentication Protocol (PEAP). It first establishes a secure TLS tunnel, followed by performing simple authentication within the tunnel. |
| EAP\_TLS | 2 | Transport Layer Security (TLS). It implements mutual certificate authentication. |
| EAP\_TTLS | 3 | Tunnel Transport Layer Security (TTLS). It is similar to PEAP, but supports a more diverse set of authentication methods inside the tunnel. |
| EAP\_PWD | 4 | Password Authentication (PWD). It enables password-based authentication and does not require a server certificate. |
| EAP\_SIM | 5 | Subscriber Identity Module (SIM). It performs authentication using the keys and algorithms stored in the SIM card of a smartphone. |
| EAP\_AKA | 6 | Authentication and Key Agreement (AKA). It performs authentication using enhanced keys and algorithms stored in a USIM card (applicable to 3G/4G/5G SIM cards). |
| EAP\_AKA\_PRIME | 7 | AKA Prime. It is an enhanced version of EAP-AKA and binds the network name during key derivation. |
| EAP\_UNAUTH\_TLS | 8 | Unauthenticated TLS (UNAUTH TLS). It implements one-way authentication (client authentication only) while establishing an encrypted communication channel. |

#### Phase2Method

Enumerates the Phase 2 authentication methods.

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

| Name | Value | Description |
| :-- | :-- | :-- |
| PHASE2\_NONE | 0 | Not specified. |
| PHASE2\_PAP | 1 | PAP. |
| PHASE2\_MSCHAP | 2 | MS-CHAP. |
| PHASE2\_MSCHAPV2 | 3 | MS-CHAPv2. |
| PHASE2\_GTC | 4 | GTC. |
| PHASE2\_SIM | 5 | SIM. |
| PHASE2\_AKA | 6 | AKA. |
| PHASE2\_AKA\_PRIME | 7 | AKA Prime. |
