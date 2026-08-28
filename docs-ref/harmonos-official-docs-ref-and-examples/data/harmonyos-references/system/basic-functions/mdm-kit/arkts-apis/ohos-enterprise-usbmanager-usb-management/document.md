# @ohos.enterprise.usbManager (USB Management)

The **usbManager** module provides APIs for USB management.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/zq7cdoPRQVKZwR5-fLFPug/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062406Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CD78DB3514D4940ED554BF8F134FFE8A3EBEA31A7AC7EB220F0B8B25324C0874)

-   The initial APIs of this module are supported since API version 12. Newly added APIs will be marked with a superscript to indicate their earliest API version.
    
-   The APIs of this module can be used only in the stage model.
    
-   The APIs of this module can be called only by a device administrator application that is enabled. For details, see [MDM Kit Development](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/mdm-kit-guide).
    
-   The global restriction policy is provided by **restrictions**. To disable USB globally, see [@ohos.enterprise.restrictions (restriction policy)](../ohos-enterprise-restrictions-restrictions/document.md).
    

#### Modules to Import

import { usbManager } from '@kit.MDMKit';

#### usbManager.addAllowedUsbDevices

addAllowedUsbDevices(admin: Want, usbDeviceIds: Array<UsbDeviceId>): void

Adds allowed USB devices.

A policy conflict is reported when this API is called in the following scenarios:

1.  The USB capability of the device has been disabled using the [setDisallowedPolicy](../ohos-enterprise-restrictions-restrictions/document.md#restrictionssetdisallowedpolicy) API.
2.  The USB storage device access policy has been disabled using the [setUsbStorageDeviceAccessPolicy](#usbmanagersetusbstoragedeviceaccesspolicy) API.
3.  Disallowed USB device types have been added using the [addDisallowedUsbDevices](#usbmanageradddisallowedusbdevices14) API.

**Required permission**: ohos.permission.ENTERPRISE\_MANAGE\_USB

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| usbDeviceIds | Array<[UsbDeviceId](#usbdeviceid)\> | Yes | USB device IDs, which can be obtained through [getDevices](../../../basic-services-kit/arkts-apis/device-management/ohos-usbmanager-usb-manager/document.md#usbmanagergetdevices). The maximum number of USB devices is 1,000. If there are already 300 USB device IDs, only 700 more can be added. |

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

import { usbManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
try {
  let usbDeviceIds: Array<usbManager.UsbDeviceId> = \[{
      vendorId: 1,
      productId: 1
  }\];
  usbManager.addAllowedUsbDevices(wantTemp, usbDeviceIds);
  console.info(\`Succeeded in adding allowed USB devices.\`);
} catch (err) {
  console.error(\`Failed to add allowed USB devices. Code: ${err.code}, message: ${err.message}\`);
}

#### usbManager.removeAllowedUsbDevices

removeAllowedUsbDevices(admin: Want, usbDeviceIds: Array<UsbDeviceId>): void

Removes allowed USB devices.

**Required permission**: ohos.permission.ENTERPRISE\_MANAGE\_USB

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| usbDeviceIds | Array<[UsbDeviceId](#usbdeviceid)\> | Yes | USB device IDs, which can be obtained through [getDevices](../../../basic-services-kit/arkts-apis/device-management/ohos-usbmanager-usb-manager/document.md#usbmanagergetdevices). |

**Error codes**

For details about the error codes, see [Enterprise Device Management Error Codes](../../error-codes/enterprise-device-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { usbManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
try {
  let usbDeviceIds: Array<usbManager.UsbDeviceId> = \[{
      vendorId: 1,
      productId: 1
  }\];
  usbManager.removeAllowedUsbDevices(wantTemp, usbDeviceIds);
  console.info(\`Succeeded in removing allowed USB devices.\`);
} catch (err) {
  console.error(\`Failed to remove allowed USB devices. Code: ${err.code}, message: ${err.message}\`);
}

#### usbManager.getAllowedUsbDevices

getAllowedUsbDevices(admin: Want): Array<UsbDeviceId>

Obtains allowed USB devices.

**Required permission**: ohos.permission.ENTERPRISE\_MANAGE\_USB

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |

**Return value**

| Type | Description |
| :-- | :-- |
| Array<[UsbDeviceId](#usbdeviceid)\> | Allowed USB devices obtained. |

**Error codes**

For details about the error codes, see [Enterprise Device Management Error Codes](../../error-codes/enterprise-device-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { usbManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
try {
  let result: Array<usbManager.UsbDeviceId> = usbManager.getAllowedUsbDevices(wantTemp);
  console.info(\`Succeeded in getting allowed USB devices. Result: ${JSON.stringify(result)}\`);
} catch (err) {
  console.error(\`Failed to get allowed USB devices. Code: ${err.code}, message: ${err.message}\`);
}

#### usbManager.setUsbStorageDeviceAccessPolicy

setUsbStorageDeviceAccessPolicy(admin: Want, usbPolicy: UsbPolicy): void

Sets the access policy of the USB storage device.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/BjQu-c41RWe1bWmevWVljQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062406Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E185AFD1C0F0F41B4E28FEFB8BE4BF25DFF4208FA64A08AEE46DA0A0667AA895)

Before calling the API, read and write operations on the USB storage device should be suspended to ensure operational stability and data integrity. Otherwise, unexpected exceptions may occur.

A policy conflict occurs when you set the USB storage device access policy to read, write, or read-only in the following scenarios:

1.  The USB capability of the device has been disabled using the [setDisallowedPolicy](../ohos-enterprise-restrictions-restrictions/document.md#restrictionssetdisallowedpolicy) API.
2.  The USB storage device has been disallowed to use through [addDisallowedUsbDevices](#usbmanageradddisallowedusbdevices14).
3.  USB storage write access has been disabled for specific users via the [setDisallowedPolicyForAccount](../ohos-enterprise-restrictions-restrictions/document.md#restrictionssetdisallowedpolicyforaccount14) API.

A policy conflict is reported if the USB storage device access policy is disabled by calling this API in the following scenarios:

1.  The USB capability of the device has been disabled using the [setDisallowedPolicy](../ohos-enterprise-restrictions-restrictions/document.md#restrictionssetdisallowedpolicy) API.
2.  The available USB devices have been added through [addAllowedUsbDevices](#usbmanageraddallowedusbdevices).
3.  USB storage write access has been disabled for specific users via the [setDisallowedPolicyForAccount](../ohos-enterprise-restrictions-restrictions/document.md#restrictionssetdisallowedpolicyforaccount14) API.

You can disable a USB storage device by calling this API or [addDisallowedUsbDevices](#usbmanageradddisallowedusbdevices14). The latter is recommended.

**Required permission**: ohos.permission.ENTERPRISE\_MANAGE\_USB

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| usbPolicy | [UsbPolicy](#usbpolicy) | Yes | Access policy of the USB storage device. |

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

import { usbManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
try {
  let policy: usbManager.UsbPolicy = usbManager.UsbPolicy.DISABLED;
  usbManager.setUsbStorageDeviceAccessPolicy(wantTemp, policy);
  console.info(\`Succeeded in setting USB storage device access policy.\`);
} catch (err) {
  console.error(\`Failed to set USB storage device access policy. Code: ${err.code}, message: ${err.message}\`);
}

#### usbManager.getUsbStorageDeviceAccessPolicy

getUsbStorageDeviceAccessPolicy(admin: Want): UsbPolicy

Obtains the access policy of the USB storage device.

**Required permission**: ohos.permission.ENTERPRISE\_MANAGE\_USB

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |

**Return value**

| Type | Description |
| :-- | :-- |
| [UsbPolicy](#usbpolicy) | Access policy of the USB storage device. |

**Error codes**

For details about the error codes, see [Enterprise Device Management Error Codes](../../error-codes/enterprise-device-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { usbManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
try {
  let result: usbManager.UsbPolicy = usbManager.getUsbStorageDeviceAccessPolicy(wantTemp);
  console.info(\`Succeeded in getting USB storage device access policy. Result: ${JSON.stringify(result)}\`);
} catch (err) {
  console.error(\`Failed to get USB storage device access policy. Code: ${err.code}, message: ${err.message}\`);
}

#### usbManager.addDisallowedUsbDevices14+

addDisallowedUsbDevices(admin: Want, usbDevices: Array<UsbDeviceType>): void

Adds disallowed USB device types.

A policy conflict is reported when this API is called in the following scenarios:

1.  The USB capability of the device has been disabled using the [setDisallowedPolicy](../ohos-enterprise-restrictions-restrictions/document.md#restrictionssetdisallowedpolicy) API.
2.  The available USB devices have been added through [addAllowedUsbDevices](#usbmanageraddallowedusbdevices).
3.  USB storage write access has been disabled for specific users via the [setDisallowedPolicyForAccount](../ohos-enterprise-restrictions-restrictions/document.md#restrictionssetdisallowedpolicyforaccount14) API.

**Required permission**: ohos.permission.ENTERPRISE\_MANAGE\_USB

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| usbDevices | Array<[UsbDeviceType](#usbdevicetype14)\> | Yes | Array of the USB devices to be added, which can be obtained through [getDevices](../../../basic-services-kit/arkts-apis/device-management/ohos-usbmanager-usb-manager/document.md#usbmanagergetdevices). The maximum number of USB devices is 200. If there are already 100 USB device IDs, only 100 more can be added. |

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

import { usbManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
try {
  let usbDevices: Array<usbManager.UsbDeviceType> = \[{
      baseClass: 8,
      subClass: 0,
      protocol: 0,
      descriptor: usbManager.Descriptor.INTERFACE
  }\];
  usbManager.addDisallowedUsbDevices(wantTemp, usbDevices);
  console.info(\`Succeeded in adding disallowed USB devices.\`);
} catch (err) {
  console.error(\`Failed to add disallowed USB devices. Code: ${err.code}, message: ${err.message}\`);
}

#### usbManager.removeDisallowedUsbDevices14+

removeDisallowedUsbDevices(admin: Want, usbDevices: Array<UsbDeviceType>): void

Removes the disallowed USB device types.

**Required permission**: ohos.permission.ENTERPRISE\_MANAGE\_USB

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| usbDevices | Array<[UsbDeviceType](#usbdevicetype14)\> | Yes | Array of the USB devices to be removed, which can be obtained through [getDevices](../../../basic-services-kit/arkts-apis/device-management/ohos-usbmanager-usb-manager/document.md#usbmanagergetdevices). |

**Error codes**

For details about the error codes, see [Enterprise Device Management Error Codes](../../error-codes/enterprise-device-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { usbManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
try {
  let usbDevices: Array<usbManager.UsbDeviceType> = \[{
      baseClass: 8,
      subClass: 0,
      protocol: 0,
      descriptor: usbManager.Descriptor.INTERFACE
  }\];
  usbManager.removeDisallowedUsbDevices(wantTemp, usbDevices);
  console.info(\`Succeeded in removing disallowed USB devices.\`);
} catch (err) {
  console.error(\`Failed to remove disallowed USB devices. Code: ${err.code}, message: ${err.message}\`);
}

#### usbManager.getDisallowedUsbDevices14+

getDisallowedUsbDevices(admin: Want): Array<UsbDeviceType>

Obtains the disallowed USB device types.

**Required permission**: ohos.permission.ENTERPRISE\_MANAGE\_USB

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |

**Return value**

| Type | Description |
| :-- | :-- |
| Array<[UsbDeviceType](#usbdevicetype14)\> | Disallowed USB device types obtained. |

**Error codes**

For details about the error codes, see [Enterprise Device Management Error Codes](../../error-codes/enterprise-device-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { usbManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
try {
  let result: Array<usbManager.UsbDeviceType> = usbManager.getDisallowedUsbDevices(wantTemp);
  console.info(\`Succeeded in getting disallowed USB devices. Result: ${JSON.stringify(result)}\`);
} catch (err) {
  console.error(\`Failed to get disallowed USB devices. Code: ${err.code}, message: ${err.message}\`);
}

#### UsbDeviceId

Represents the USB device identity information.

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| vendorId | number | No | No | Vendor ID. |
| productId | number | No | No | Product ID. |

#### UsbDeviceType14+

Represents the USB device type information.

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| baseClass | number | No | No | 
Type code.

You can obtain the list of USB devices connected to the host device through the [getDevices](../../../basic-services-kit/arkts-apis/device-management/ohos-usbmanager-usb-manager/document.md#usbmanagergetdevices) API, find the current device in the returned list, and check its value.

First, determine the type of descriptor to pass in based on this value. If the descriptor is **DEVICE**, this field takes the value of the **USBDevice.clazz** field; if the descriptor is **INTERFACE**, this field takes the value of the **USBDevice.configs.interfaces.clazz** field.

If the field value is 255 (indicating the device's type code is a vendor-defined code), calling the [addDisallowedUsbDevices](#usbmanageradddisallowedusbdevices14) or [removeDisallowedUsbDevices](#usbmanagerremovedisallowedusbdevices14) API to enable or disable the device will not take effect. If the field value is not defined in [defined-class-codes](https://www.usb.org/defined-class-codes), calling the [addDisallowedUsbDevices](#usbmanageradddisallowedusbdevices14) or [removeDisallowedUsbDevices](#usbmanagerremovedisallowedusbdevices14) API to enable or disable the device will also not take effect.

 |
| subClass | number | No | No | 

Subtype code.

You can obtain the list of USB devices connected to the host device through the [getDevices](../../../basic-services-kit/arkts-apis/device-management/ohos-usbmanager-usb-manager/document.md#usbmanagergetdevices) API, find the current device in the returned list, and check its value.

First, determine the type of descriptor to pass in based on the value of baseClass. If the descriptor is **DEVICE**, this field takes the value of the **USBDevice.subClass** field; if the descriptor is **INTERFACE**, this field takes the value of the **USBDevice.configs.interfaces.subClass** field.

If the field value is 255 (indicating that the subtype code of the device is a vendor-defined code), calling the [addDisallowedUsbDevices](#usbmanageradddisallowedusbdevices14) or [removeDisallowedUsbDevices](#usbmanagerremovedisallowedusbdevices14) API to enable or disable the device will not take effect. If the field value is not defined in [defined-class-codes](https://www.usb.org/defined-class-codes), calling the [addDisallowedUsbDevices](#usbmanageradddisallowedusbdevices14) or [removeDisallowedUsbDevices](#usbmanagerremovedisallowedusbdevices14) API to enable or disable the device will also not take effect.

 |
| protocol | number | No | No | 

Protocol code.

You can obtain the list of USB devices connected to the host device through the [getDevices](../../../basic-services-kit/arkts-apis/device-management/ohos-usbmanager-usb-manager/document.md#usbmanagergetdevices) API, find the current device in the returned list, and check its value.

First, determine the type of descriptor to pass in based on the value of baseClass. If the descriptor is **DEVICE**, this field takes the value of the **USBDevice.protocol** field; if the descriptor is **INTERFACE**, this field takes the value of the **USBDevice.configs.interfaces.protocol** field.

If the field value is 255 (indicating the device's protocol code is a vendor-defined code), calling the [addDisallowedUsbDevices](#usbmanageradddisallowedusbdevices14) or [removeDisallowedUsbDevices](#usbmanagerremovedisallowedusbdevices14) API to enable or disable the device will not take effect. If the field value is not defined in [defined-class-codes](https://www.usb.org/defined-class-codes), calling the [addDisallowedUsbDevices](#usbmanageradddisallowedusbdevices14) or [removeDisallowedUsbDevices](#usbmanagerremovedisallowedusbdevices14) API to enable or disable the device will also not take effect.

 |
| descriptor | [Descriptor](#descriptor14) | No | No | 

USB descriptor.

You can obtain the list of USB devices connected to the host device through the [getDevices](../../../basic-services-kit/arkts-apis/device-management/ohos-usbmanager-usb-manager/document.md#usbmanagergetdevices) API, find the current device in the returned list, and check its value.

If the value of **USBDevice.clazz** is **0**, you need to find the value of **USBDevice.configs.interfaces.clazz** in the Base Class column in [defined-class-codes](https://www.usb.org/defined-class-codes). The Descriptor Usage column in the row where the search result is located indicates the descriptor type to be transferred. If the value of Descriptor Usage is **Both**, both types can be transferred. If device-level disabling is required, transfer **DEVICE**. If interface-level disabling is required, transfer **INTERFACE**.

If the value of **USBDevice.clazz** is **255** (indicating the device's type code is a vendor-defined code), calling the [addDisallowedUsbDevices](#usbmanageradddisallowedusbdevices14) or [removeDisallowedUsbDevices](#usbmanagerremovedisallowedusbdevices14) API to enable or disable the device will not take effect. If the value of **USBDevice.clazz** is another value, search for the value in the Base Class column of [defined-class-codes](https://www.usb.org/defined-class-codes). The Descriptor Usage column in the row where the search result is located indicates the descriptor type to be transferred. If the value of Descriptor Usage is **Both**, both types can be transferred. If device-level disabling is required, transfer **DEVICE**. If interface-level disabling is required, transfer **INTERFACE**.

 |

#### UsbPolicy

Enumerates the USB access policies.

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

| Name | Value | Description |
| :-- | :-- | :-- |
| READ\_WRITE | 0 | Read and write. |
| READ\_ONLY | 1 | Read only. |
| DISABLED | 2 | Disabled. |

#### Descriptor14+

Enumerates USB descriptors.

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

| Name | Value | Description |
| :-- | :-- | :-- |
| INTERFACE | 0 | Interface descriptor. |
| DEVICE | 1 | Device descriptor. |
