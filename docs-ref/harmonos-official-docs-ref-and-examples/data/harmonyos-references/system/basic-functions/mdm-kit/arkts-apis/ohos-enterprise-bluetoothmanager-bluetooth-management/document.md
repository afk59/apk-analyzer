# @ohos.enterprise.bluetoothManager (Bluetooth Management)

The **bluetoothManager** module provides Bluetooth management capabilities, including setting and obtaining Bluetooth information.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7/v3/RwXhLG6wSP-GhMa1PA2LHg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062405Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B7B2C43762DB90F90A085F6E047CA30A84D3FAE16EF8B2758F8DA1473C134BA0)

The initial APIs of this module are supported since API version 12. Newly added APIs will be marked with a superscript to indicate their earliest API version.

The APIs of this module can be used only in the stage model.

The APIs of this module can be called only by a device administrator application that is enabled. For details, see [MDM Kit Development](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/mdm-kit-guide).

The global restriction policies are provided by **restrictions**. To disable Bluetooth globally, see [@ohos.enterprise.restrictions](../ohos-enterprise-restrictions-restrictions/document.md).

#### Modules to Import

import { bluetoothManager } from '@kit.MDMKit';

#### bluetoothManager.getBluetoothInfo

getBluetoothInfo(admin: Want): BluetoothInfo

Obtains device Bluetooth information.

**Required permissions**: ohos.permission.ENTERPRISE\_MANAGE\_BLUETOOTH

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |

**Return value**

| Type | Description |
| :-- | :-- |
| [BluetoothInfo](#bluetoothinfo) | Bluetooth information, including the Bluetooth name, state, and profile connection state. |

**Error codes**

For details about the error codes, see [Enterprise Device Management Error Codes](../../error-codes/enterprise-device-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { bluetoothManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace it as required.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
    let result: bluetoothManager.BluetoothInfo = bluetoothManager.getBluetoothInfo(wantTemp);
    console.info(\`Succeeded in getting bluetooth info: ${JSON.stringify(result)}\`);
} catch(err) {
    console.error(\`Failed to get bluetooth info. Code: ${err.code}, message: ${err.message}\`);
}

#### bluetoothManager.addAllowedBluetoothDevices

addAllowedBluetoothDevices(admin: Want, deviceIds: Array<string>): void

Adds Bluetooth devices to the trustlist. After adding devices to this list, the current device will only be allowed to connect to Bluetooth devices in the list. Since API version 22, the MAC addresses in the array must comply with the Bluetooth MAC address specifications (for example, 00:1A:2B:3C:4D:5E). Invalid MAC addresses will be removed and only valid MAC addresses will be added.

A policy conflict is reported when this API is called in the following scenarios:

1.  Bluetooth has been disabled by calling [setDisallowedPolicy](../ohos-enterprise-restrictions-restrictions/document.md#restrictionssetdisallowedpolicy). You can resolve the conflict by enabling the Bluetooth through [setDisallowedPolicy](../ohos-enterprise-restrictions-restrictions/document.md#restrictionssetdisallowedpolicy).
2.  Disallowed Bluetooth devices have been added by calling [addDisallowedBluetoothDevices](#bluetoothmanageradddisallowedbluetoothdevices20). You can resolve the conflict by removing disallowed Bluetooth devices through [removeDisallowedBluetoothDevices](#bluetoothmanagerremovedisallowedbluetoothdevices20).

**Required permissions**: ohos.permission.ENTERPRISE\_MANAGE\_BLUETOOTH

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| deviceIds | Array<string> | Yes | MAC addresses of the Bluetooth devices to add. The maximum number of allowed Bluetooth devices is 1,000. If there are already 300 MAC addresses of the devices, only 700 more can be added. |

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

import { bluetoothManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace it as required.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
// Replace it as required.
let deviceIds: Array<string> = \["00:1A:2B:3C:4D:5E","AA:BB:CC:DD:EE:FF"\];
try {
    bluetoothManager.addAllowedBluetoothDevices(wantTemp,deviceIds);
    console.info(\`Succeeded in adding allowed bluetooth devices.\`);
} catch(err) {
    console.error(\`Failed to add allowed bluetooth devices. Code: ${err.code}, message: ${err.message}\`);
}

#### bluetoothManager.removeAllowedBluetoothDevices

removeAllowedBluetoothDevices(admin: Want, deviceIds: Array<string>): void

Removes allowed Bluetooth devices.

**Required permissions**: ohos.permission.ENTERPRISE\_MANAGE\_BLUETOOTH

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| deviceIds | Array<string> | Yes | MAC addresses of the Bluetooth devices to remove. |

**Error codes**

For details about the error codes, see [Enterprise Device Management Error Codes](../../error-codes/enterprise-device-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { bluetoothManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace it as required.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
// Replace it as required.
let deviceIds: Array<string> = \["00:1A:2B:3C:4D:5E","AA:BB:CC:DD:EE:FF"\];
try {
    bluetoothManager.removeAllowedBluetoothDevices(wantTemp,deviceIds);
    console.info(\`Succeeded in removing allowed bluetooth devices.\`);
} catch(err) {
    console.error(\`Failed to remove allowed bluetooth devices. Code: ${err.code}, message: ${err.message}\`);
}

#### bluetoothManager.getAllowedBluetoothDevices

getAllowedBluetoothDevices(admin: Want): Array<string>

Obtains allowed Bluetooth devices.

**Required permissions**: ohos.permission.ENTERPRISE\_MANAGE\_BLUETOOTH

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |

**Return value**

| Type | Description |
| :-- | :-- |
| Array<string> | MAC addresses of allowed Bluetooth devices obtained. |

**Error codes**

For details about the error codes, see [Enterprise Device Management Error Codes](../../error-codes/enterprise-device-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { bluetoothManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace it as required.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
try {
    let result: Array<string> = bluetoothManager.getAllowedBluetoothDevices(wantTemp);
    console.info(\`Succeeded in getting allowed bluetooth devices. Result: ${JSON.stringify(result)}\`);
} catch(err) {
    console.error(\`Failed to get allowed bluetooth devices. Code: ${err.code}, message: ${err.message}\`);
}

#### bluetoothManager.addDisallowedBluetoothDevices20+

addDisallowedBluetoothDevices(admin: Want, deviceIds: Array<string>): void

Adds Bluetooth devices to the blocklist. The current device cannot connect to the disallowed Bluetooth devices. Since API version 22, the MAC addresses in the array must comply with the Bluetooth MAC address specifications (for example, 00:1A:2B:3C:4D:5E). Invalid MAC addresses will be removed and only valid MAC addresses will be added.

A policy conflict is reported when this API is called in the following scenarios:

1.  Bluetooth has been disabled by calling [setDisallowedPolicy](../ohos-enterprise-restrictions-restrictions/document.md#restrictionssetdisallowedpolicy). You can resolve the conflict by enabling the Bluetooth through [setDisallowedPolicy](../ohos-enterprise-restrictions-restrictions/document.md#restrictionssetdisallowedpolicy).
2.  Allowed Bluetooth devices have been added by calling [addAllowedBluetoothDevices](#bluetoothmanageraddallowedbluetoothdevices). You can resolve the conflict by removing allowed Bluetooth devices through [removeAllowedBluetoothDevices](#bluetoothmanagerremoveallowedbluetoothdevices).

**Required permissions**: ohos.permission.ENTERPRISE\_MANAGE\_BLUETOOTH

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| deviceIds | Array<string> | Yes | MAC addresses of the Bluetooth devices to add. The maximum number of disallowed Bluetooth devices is 1,000. If there are already 300 MAC addresses of the devices, only 700 more can be added. |

**Error codes**

For details about the error codes, see [Enterprise Device Management Error Codes](../../error-codes/enterprise-device-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9200010 | A conflict policy has been configured. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**Example**

import { bluetoothManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace it as required.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
// Replace it as required.
let deviceIds: Array<string> = \["00:1A:2B:3C:4D:5E","AA:BB:CC:DD:EE:FF"\];
try {
    bluetoothManager.addDisallowedBluetoothDevices(wantTemp,deviceIds);
    console.info(\`Succeeded in adding disallowed bluetooth devices.\`);
} catch(err) {
    console.error(\`Failed to add disallowed bluetooth devices. Code: ${err.code}, message: ${err.message}\`);
}

#### bluetoothManager.removeDisallowedBluetoothDevices20+

removeDisallowedBluetoothDevices(admin: Want, deviceIds: Array<string>): void

Removes disallowed Bluetooth devices. If some Bluetooth devices are removed from the disallowed list, the current device cannot connect to the remaining ones; if all Bluetooth devices are removed, the current device can connect to any Bluetooth device.

**Required permissions**: ohos.permission.ENTERPRISE\_MANAGE\_BLUETOOTH

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| deviceIds | Array<string> | Yes | MAC addresses of the Bluetooth devices to remove. |

**Error codes**

For details about the error codes, see [Enterprise Device Management Error Codes](../../error-codes/enterprise-device-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**Example**

import { bluetoothManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace it as required.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
// Replace it as required.
let deviceIds: Array<string> = \["00:1A:2B:3C:4D:5E","AA:BB:CC:DD:EE:FF"\];
try {
    bluetoothManager.removeDisallowedBluetoothDevices(wantTemp,deviceIds);
    console.info(\`Succeeded in removing disallowed bluetooth devices.\`);
} catch(err) {
    console.error(\`Failed to remove disallowed bluetooth devices. Code: ${err.code}, message: ${err.message}\`);
}

#### bluetoothManager.getDisallowedBluetoothDevices20+

getDisallowedBluetoothDevices(admin: Want): Array<string>

Obtains disallowed Bluetooth devices.

**Required permissions**: ohos.permission.ENTERPRISE\_MANAGE\_BLUETOOTH

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |

**Return value**

| Type | Description |
| :-- | :-- |
| Array<string> | MAC addresses of disallowed Bluetooth devices obtained. |

**Error codes**

For details about the error codes, see [Enterprise Device Management Error Codes](../../error-codes/enterprise-device-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**Example**

import { bluetoothManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace it as required.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
try {
    let result: Array<string> = bluetoothManager.getDisallowedBluetoothDevices(wantTemp);
    console.info(\`Succeeded in getting disallowed bluetooth devices. Result: ${JSON.stringify(result)}\`);
} catch(err) {
    console.error(\`Failed to get disallowed bluetooth devices. Code: ${err.code}, message: ${err.message}\`);
}

#### bluetoothManager.turnOnBluetooth20+

turnOnBluetooth(admin: Want): void

Enables Bluetooth. After Bluetooth is enabled, the user can manually disable it.

**Required permissions**: ohos.permission.ENTERPRISE\_MANAGE\_BLUETOOTH

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
| 203 | This function is prohibited by enterprise management policies. |

**Example**

import { Want } from '@kit.AbilityKit';
import { bluetoothManager } from '@kit.MDMKit';

let wantTemp: Want = {
  // Replace it as required.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
try {
    bluetoothManager.turnOnBluetooth(wantTemp);
    console.info(\`Succeeded in turning on bluetooth.\`);
} catch(err) {
    console.error(\`Failed to turn on bluetooth. Code: ${err.code}, message: ${err.message}\`);
}

#### bluetoothManager.turnOffBluetooth20+

turnOffBluetooth(admin: Want): void

Disables Bluetooth. After Bluetooth is disabled, the user can manually enable it.

**Required permissions**: ohos.permission.ENTERPRISE\_MANAGE\_BLUETOOTH

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
| 203 | This function is prohibited by enterprise management policies. |

**Example**

import { Want } from '@kit.AbilityKit';
import { bluetoothManager } from '@kit.MDMKit';

let wantTemp: Want = {
  // Replace it as required.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
try {
    bluetoothManager.turnOffBluetooth(wantTemp);
    console.info('Succeeded in turning off bluetooth.');
} catch(err) {
    console.error(\`Failed to turn off bluetooth. Code: ${err.code}, message: ${err.message}\`);
}

#### bluetoothManager.addDisallowedBluetoothProtocols20+

addDisallowedBluetoothProtocols(admin: Want, accountId: number, protocols: Array<Protocol>): void

Adds disallowed Bluetooth protocols. Specified users cannot use the disallowed Bluetooth protocols to send files to other devices. This API is used to disable the GATT or SPP protocol, which does not take effect for system services and system applications.

**Required permissions**: ohos.permission.ENTERPRISE\_MANAGE\_BLUETOOTH

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| accountId | number | Yes | 
User ID, which must be greater than or equal to 0.

You can call [getOsAccountLocalId](../../../basic-services-kit/arkts-apis/account-management/ohos-account-osaccount-system-account-management/document.md#getosaccountlocalid9-1) of @ohos.account.osAccount to obtain the ID.

 |
| protocols | Array<[Protocol](#protocol20)\> | Yes | Bluetooth protocol array, which has a maximum length of 10,000. |

**Error codes**

For details about the error codes, see [Enterprise Device Management Error Codes](../../error-codes/enterprise-device-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**Example**

import { Want } from '@kit.AbilityKit';
import { bluetoothManager } from '@kit.MDMKit';

let wantTemp: Want = {
  // Replace it as required.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
// Replace it as required.
let accountId: number = 100;
let protocols: Array<bluetoothManager.Protocol> = \[bluetoothManager.Protocol.GATT, bluetoothManager.Protocol.SPP\];
try{
    bluetoothManager.addDisallowedBluetoothProtocols(wantTemp, accountId, protocols);
    console.info('Succeeded in adding disallowed bluetooth protocols policy.');
} catch (err) {
    console.error(\`Failed to add disallowed bluetooth protocols. Code: ${err.code}, message: ${err.message}\`);
}

#### bluetoothManager.removeDisallowedBluetoothProtocols20+

removeDisallowedBluetoothProtocols(admin: Want, accountId: number, protocols: Array<Protocol>): void

Removes disallowed Bluetooth protocols. After removing some protocols, the user is still restricted by the remaining disallowed protocols; after removing all protocols, the user can use any protocol; removing non-existent protocols results in a successful API call but no actual change.

**Required permissions**: ohos.permission.ENTERPRISE\_MANAGE\_BLUETOOTH

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| accountId | number | Yes | 
User ID, which must be greater than or equal to 0.

You can call [getOsAccountLocalId](../../../basic-services-kit/arkts-apis/account-management/ohos-account-osaccount-system-account-management/document.md#getosaccountlocalid9-1) of @ohos.account.osAccount to obtain the ID.

 |
| protocols | Array<[Protocol](#protocol20)\> | Yes | Bluetooth protocol array. |

**Error codes**

For details about the error codes, see [Enterprise Device Management Error Codes](../../error-codes/enterprise-device-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**Example**

import { Want } from '@kit.AbilityKit';
import { bluetoothManager } from '@kit.MDMKit';

let wantTemp: Want = {
  // Replace it as required.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
// Replace it as required.
let accountId: number = 100;
let protocols: Array<bluetoothManager.Protocol> = \[bluetoothManager.Protocol.GATT, bluetoothManager.Protocol.SPP\];
try{
    bluetoothManager.removeDisallowedBluetoothProtocols(wantTemp, accountId, protocols);
    console.info('Succeeded in removing disallowed bluetooth protocols policy.');
} catch (err) {
    console.error(\`Failed to remove disallowed bluetooth protocols. Code: ${err.code}, message: ${err.message}\`);
}

#### bluetoothManager.getDisallowedBluetoothProtocols20+

getDisallowedBluetoothProtocols(admin: Want, accountId: number): Array<Protocol>

Obtains the disallowed Bluetooth protocols of a specified user.

**Required permissions**: ohos.permission.ENTERPRISE\_MANAGE\_BLUETOOTH

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| accountId | number | Yes | 
User ID, which must be greater than or equal to 0.

You can call [getOsAccountLocalId](../../../basic-services-kit/arkts-apis/account-management/ohos-account-osaccount-system-account-management/document.md#getosaccountlocalid9-1) of @ohos.account.osAccount to obtain the ID.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Array<[Protocol](#protocol20)\> | Array of disallowed Bluetooth protocols. |

**Error codes**

For details about the error codes, see [Enterprise Device Management Error Codes](../../error-codes/enterprise-device-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**Example**

import { Want } from '@kit.AbilityKit';
import { bluetoothManager } from '@kit.MDMKit';

let wantTemp: Want = {
  // Replace it as required.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
// Replace it as required.
let accountId: number = 100;
try{
    let result: Array<bluetoothManager.Protocol> = bluetoothManager.getDisallowedBluetoothProtocols(wantTemp, accountId);
    console.info(\`Succeeded in getting disallowed bluetooth protocols. Result: ${JSON.stringify(result)}\`);
} catch (err) {
    console.error(\`Failed to get disallowed bluetooth protocols. Code: ${err.code}, message: ${err.message}\`);
}

#### BluetoothInfo

Represents the device Bluetooth information.

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| name | string | No | No | Bluetooth name of the device. |
| state | [access.BluetoothState](../../../../network/connectivity-kit/arkts-apis/ohos-bluetooth-access-bluetooth-access-module/document.md#bluetoothstate) | No | No | Bluetooth state of the device. |
| connectionState | [constant.ProfileConnectionState](../../../../network/connectivity-kit/arkts-apis/ohos-bluetooth-constant-bluetooth-constant-module/document.md#profileconnectionstate) | No | No | Bluetooth profile connection state of the device. |

#### Protocol20+

Represents the Bluetooth protocol type.

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

| Name | Value | Description |
| :-- | :-- | :-- |
| GATT | 0 | [Generic Attribute Profile (GATT)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/terminology#gatt) |
| SPP | 1 | [Serial Port Profile (SPP)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/terminology#spp) |
| OPP | 2 | [Object Push Profile (OPP)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/terminology#opp) |
