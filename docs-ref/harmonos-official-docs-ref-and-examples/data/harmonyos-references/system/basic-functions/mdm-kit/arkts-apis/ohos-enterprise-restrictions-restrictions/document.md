# @ohos.enterprise.restrictions (Restrictions)

This **restrictions** module provides APIs for disallowing general features of devices. You can globally disable or enable the features such as Bluetooth, HDC, USB, and Wi-Fi.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/VUWteiBuR5-gbEeb9WbzBA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062406Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=55548AD7941B082AE9001B06C75FA1B849BFA0A03935DA0436D96E5A83BA8F91)

The initial APIs of this module are supported since API version 12. Newly added APIs will be marked with a superscript to indicate their earliest API version.

The APIs of this module can be used only in the stage model.

The APIs of this module can be called only by a device administrator application that is enabled. For details, see [MDM Kit Development](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/mdm-kit-guide).

#### Modules to Import

import { restrictions } from '@kit.MDMKit';

#### restrictions.setDisallowedPolicy

setDisallowedPolicy(admin: Want, feature: string, disallow: boolean): void

Disallows a feature.

**Required permissions**: ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS, ohos.permission.PERSONAL\_MANAGE\_RESTRICTIONS15+, or ohos.permission.ENTERPRISE\_MANAGE\_NETWORK (The required permissions vary depending on the feature to be set. For details, see Table 1.)

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| feature | string | Yes | 
For features that can be set, see Table 1.

**NOTE**

Since API version 15, applications granted with the ohos.permission.PERSONAL\_MANAGE\_RESTRICTIONS permission and [activated as device administrator applications](../ohos-enterprise-adminmanager-administrator-permission-management/document.md#adminmanagerstartadminprovision15) can set the following features: **bluetooth**, **hdc**, **microphone**, **usb**, **wifi**, **tethering**, and **camera**, screenshot, screenRecord, nearLink, resetFactory.

 |
| disallow | boolean | Yes | Whether to disallow the feature. The value **true** means to disallow the feature; the value **false** means the opposite. |

**Table 1 Supported features**

| Feature | Description | Required Permission |
| :-- | :-- | :-- |
| bluetooth | Device Bluetooth capability. If a Bluetooth device blocklist or trustlist is configured via [addDisallowedBluetoothDevices](../ohos-enterprise-bluetoothmanager-bluetooth-management/document.md#bluetoothmanageradddisallowedbluetoothdevices20) or [addAllowedBluetoothDevices](../ohos-enterprise-bluetoothmanager-bluetooth-management/document.md#bluetoothmanageraddallowedbluetoothdevices), disabling Bluetooth via this API takes priority. The blocklist or trustlist will only take effect after Bluetooth is re-enabled. | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS or ohos.permission.PERSONAL\_MANAGE\_RESTRICTIONS |
| modifyDateTime | Device capability to modify system time. | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS |
| printer | Device printing capability. Currently, this feature is available only for PCs/2-in-1 devices. Disabling printing via this API overrides the [setDisallowedPolicyForAccount](#restrictionssetdisallowedpolicyforaccount14) setting for specific users. | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS |
| hdc | Capability for other devices to connect to and debug this device via HDC. Disabling this capability prevents external devices from connecting or debugging via HDC. | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS or ohos.permission.PERSONAL\_MANAGE\_RESTRICTIONS |
| microphone | Device microphone capability. | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS or ohos.permission.PERSONAL\_MANAGE\_RESTRICTIONS |
| fingerprint | Device fingerprint authentication capability. Calling this API will trigger a policy conflict if fingerprint authentication has already been disabled for a user via [setDisallowedPolicyForAccount](#restrictionssetdisallowedpolicyforaccount14). | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS |
| usb | 
Device USB capability. Disabling this capability prohibits the use of external USB devices (the device cannot act as a USB host to connect external devices).

A policy conflict occurs in the following scenarios:

1\. A list of allowed USB devices has been configured via the [addAllowedUsbDevices](../ohos-enterprise-usbmanager-usb-management/document.md#usbmanageraddallowedusbdevices) API.

2\. USB storage device access policy has been set to read-only or disabled via the [setUsbStorageDeviceAccessPolicy](../ohos-enterprise-usbmanager-usb-management/document.md#usbmanagersetusbstoragedeviceaccesspolicy) API.

3\. Specific USB device types have been blocked via the [addDisallowedUsbDevices](../ohos-enterprise-usbmanager-usb-management/document.md#usbmanageradddisallowedusbdevices14) API.

4\. USB storage write access has been disabled for specific users via the [setDisallowedPolicyForAccount](#restrictionssetdisallowedpolicyforaccount14) API.

 | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS or ohos.permission.PERSONAL\_MANAGE\_RESTRICTIONS |
| wifi | Device Wi-Fi capability. | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS or ohos.permission.PERSONAL\_MANAGE\_RESTRICTIONS |
| tethering14+ | Network tethering capability (the ability to share the device's internet connection with other devices, that is, hotspot sharing). | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS or ohos.permission.PERSONAL\_MANAGE\_RESTRICTIONS |
| inactiveUserFreeze14+ | Capability of freezing inactive users. When this capability is disabled, non-**UIAbility** processes will generally not be frozen, and background tasks requested by **UIAbility** (such as transient tasks, continuous tasks, deferred tasks, or energy efficiency resources) will also not be frozen. Currently, this capability is supported only on PCs/2-in-1 devices. When the system switches to the enterprise space user, the personal space users are inactive users. | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS |
| camera14+ | Device camera capability. | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS or ohos.permission.PERSONAL\_MANAGE\_RESTRICTIONS |
| mtpClient18+ | Media Transfer Protocol (MTP) client capability (including read and write capabilities), currently supported only on PC/2-in-1 devices. MTP allows users to linearly access media files on mobile devices. A policy conflict occurs if this API is used to disable MTP client capability after MTP client write access has been disabled for specific users via [setDisallowedPolicyForAccount](#restrictionssetdisallowedpolicyforaccount14). | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS |
| mtpServer18+ | MTP server capability, currently supported only on phone and tablets. | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS |
| sambaClient20+ | 

Samba client capability, currently supported only on PC/2-in-1 devices.

Samba is a free software that implements the SMB protocol on Linux and UNIX systems, consisting of both server and client programs.

Server Messages Block (SMB) is a communication protocol for sharing files and printers over the local area network (LAN), enabling access to shared file systems, printers, and other resources between devices on the same LAN. As a client/server protocol, SMB allows clients to access shared resources hosted on servers.

 | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS |
| sambaServer20+ | Samba server capability, currently supported only on PC/2-in-1 devices. | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS |
| backupAndRestore20+ | Backup and restore capability. If this feature is disabled, the **Settings** > **System** > **Backup & Restore** and **Settings** > **Cloud** options will be dimmed. Currently, this feature is supported only on phones and tablets. To completely disable the backup and restore capability, you are advised to call [applicationManager.addDisallowedRunningBundlesSync](../ohos-enterprise-applicationmanager-application-management/document.md#applicationmanageradddisallowedrunningbundlessync) to disable applications with this feature, such as Backup & Restore, HiSuite, and Cloud. | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS |
| maintenanceMode20+ | Device maintenance mode capability. | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS |
| mms20+ | Multimedia Messaging Service (MMS) capability to receive and send multimedia messages. Currently, this feature is supported only on smartphones and tablets. | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS |
| sms20+ | Short Messaging Service (SMS) capability to receive and send SMS messages. Currently, this feature is supported only on smartphones and tablets. | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS |
| mobileData20+ | Cellular data capability, which is supported only on smartphones and tablets. | ohos.permission.ENTERPRISE\_MANAGE\_NETWORK |
| airplaneMode20+ | Airplane mode capability, which is supported only on smartphones and tablets. | ohos.permission.ENTERPRISE\_MANAGE\_NETWORK |
| vpn20+ | Virtual Private Network (VPN) capability. | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS |
| notification20+ | Device notification capability. Disabling this feature prevents system applications and third-party applications from displaying notifications. The notification capability of system services is not affected. | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS |
| nfc20+ | Near Field Communication (NFC) capability, which is supported only on phones and tablets. | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS |
| privateSpace20+ | Privacy space creation capability, which is supported only on smartphones and tablets. This setting does not affect existing private spaces. | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS |
| telephoneCall20+ | Call capability. Disabling this feature blocks incoming or outgoing calls. Currently, this feature is supported only on smartphones and tablets. | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS |
| appClone21+ | [Application clone capability](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-clone). When this feature is disabled, new application clones cannot be created. This feature is invalid for the application clone that has been created. | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS |
| externalStorageCard21+ | 

External storage capability. Disabling this feature prohibits the use of external storage and unmounts currently connected external storage. If files are in use during unmounting, unmounting may fail with error code 9200013.

After external storage is disabled and then enabled again, you need to manually reconnect the external storage.

 | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS |
| randomMac21+ | Random MAC address capability for Wi-Fi connections. When this feature is disabled, only the device's physical MAC address can be used for Wi-Fi connections. | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS |
| unmuteDevice22+ | Device audio playback capability. When this feature is disabled, media playback will be muted, while [cellular calls](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/audio-call-overview) remain unaffected. | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS |
| hdcRemote22+ | Capability of the device to debug other devices through HDC. Currently, this feature can be set only for PCs/2-in-1 devices. Disabling this capability prevents debugging smartphones, tablets, PCs, smart watches, and other devices via HDC. | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS |
| screenshot | Device screen capture capability. | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS or ohos.permission.PERSONAL\_MANAGE\_RESTRICTIONS |
| screenRecord | Device screen recording capability. | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS or ohos.permission.PERSONAL\_MANAGE\_RESTRICTIONS |
| diskRecoveryKey | Recovery key export capability. | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS |
| nearLink | Device NearLink capability. | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS or ohos.permission.PERSONAL\_MANAGE\_RESTRICTIONS |
| developerMode14+ | Developer mode, which takes effect after the device is restarted. Currently, this mode is supported only on PCs and 2-in-1 devices. | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS |
| resetFactory18+ | Factory reset capability. | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS or ohos.permission.PERSONAL\_MANAGE\_RESTRICTIONS |
| remoteDesk20+ | Remote desktop capability. You can go to **My HUAWEI** > **Services** > **Quick services** > **Smart Diagnosis**, tap the icon in the upper right corner, and select **Remote Service** to check it. Currently, this feature is available only for mobile phones, tablets, and PCs/2-in-1 devices. | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS |
| remoteDiagnosis20+ | Remote diagnosis capability. You can go to **My HUAWEI** > **Services** > **Quick services** > **Smart Diagnosis**, tap the icon in the upper right corner, and select **Diagnostic Analysis** to check it. Currently, this feature is available only for mobile phones, tablets, and PCs/2-in-1 devices. | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS |
| otaUpdate20+ | System upgrade capability on public networks. | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS |

**Error codes**

For details about the error codes, see [Enterprise Device Management Error Codes](../../error-codes/enterprise-device-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9200013 | The enterprise management policy has been successfully set, but the function has not taken effect in real time. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**Example**

import { restrictions } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  // Replace parameters with actual values.
  restrictions.setDisallowedPolicy(wantTemp, 'printer', true);
  console.info('Succeeded in setting printer disabled');
} catch (err) {
  console.error(\`Failed to set printer disabled. Code is ${err.code}, message is ${err.message}\`);
}

#### restrictions.getDisallowedPolicy

getDisallowedPolicy(admin: Want | null, feature: string): boolean

Queries whether a feature is disabled.

**Required permissions**: ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS, ohos.permission.PERSONAL\_MANAGE\_RESTRICTIONS15+, or ohos.permission.ENTERPRISE\_MANAGE\_NETWORK (The required permissions vary depending on the feature to be queried. For details, see Table 2.)

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | null | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| feature | string | Yes | 
For features that can be queried, see Table 2.

**NOTE**

Since API version 15, applications granted with the ohos.permission.PERSONAL\_MANAGE\_RESTRICTIONS permission and [activated as device administrator applications](../ohos-enterprise-adminmanager-administrator-permission-management/document.md#adminmanagerstartadminprovision15) can obtain the following features: **bluetooth**, **hdc**, **microphone**, **usb**, **wifi**, **tethering**, and **camera**, screenshot, screenRecord, nearLink, resetFactory.

 |

**Table 2** Features that can be queried

| Feature | Description | Required Permission |
| :-- | :-- | :-- |
| bluetooth | Device Bluetooth capability. | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS or ohos.permission.PERSONAL\_MANAGE\_RESTRICTIONS |
| modifyDateTime | Device capability to modify system time. | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS |
| printer | Device printing capability. Currently, this feature is available only for PCs/2-in-1 devices. | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS |
| hdc | Capability for other devices to connect to and debug this device via HDC. | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS or ohos.permission.PERSONAL\_MANAGE\_RESTRICTIONS |
| microphone | Device microphone capability. | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS or ohos.permission.PERSONAL\_MANAGE\_RESTRICTIONS |
| fingerprint | Device fingerprint authentication capability. | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS |
| usb | Device USB capability. Disabling this capability prohibits the use of external USB devices (the device cannot act as a USB host to connect external devices). | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS or ohos.permission.PERSONAL\_MANAGE\_RESTRICTIONS |
| wifi | Device Wi-Fi capability. | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS or ohos.permission.PERSONAL\_MANAGE\_RESTRICTIONS |
| tethering14+ | Network tethering capability (the ability to share the device's internet connection with other devices, that is, hotspot sharing). | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS or ohos.permission.PERSONAL\_MANAGE\_RESTRICTIONS |
| inactiveUserFreeze14+ | Capability of freezing inactive users. When this capability is disabled, non-**UIAbility** processes will generally not be frozen, and background tasks requested by **UIAbility** (such as transient tasks, continuous tasks, deferred tasks, or energy efficiency resources) will also not be frozen. Currently, this capability is supported only on PCs/2-in-1 devices. When the system switches to the enterprise space user, the personal space users are inactive users. | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS |
| camera14+ | Device camera capability. | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS or ohos.permission.PERSONAL\_MANAGE\_RESTRICTIONS |
| mtpClient18+ | Media Transfer Protocol (MTP) client capability (including read and write capabilities), currently supported only on PC/2-in-1 devices. MTP allows users to linearly access media files on mobile devices. | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS |
| mtpServer18+ | MTP server capability, currently supported only on phone and tablets. | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS |
| sambaClient20+ | 
Samba client capability, currently supported only on PC/2-in-1 devices.

Samba is a free software that implements the SMB protocol on Linux and UNIX systems, consisting of both server and client programs.

Server Messages Block (SMB) is a communication protocol for sharing files and printers over the local area network (LAN), enabling access to shared file systems, printers, and other resources between devices on the same LAN. As a client/server protocol, SMB allows clients to access shared resources hosted on servers.

 | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS |
| sambaServer20+ | Samba server capability, currently supported only on PC/2-in-1 devices. | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS |
| backupAndRestore20+ | Backup and restore capability. If this feature is disabled, the **Settings** > **System** > **Backup & Restore** and **Settings** > **Cloud** options will be dimmed. Currently, this feature is supported only on phones and tablets. | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS |
| maintenanceMode20+ | Device maintenance mode capability. | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS |
| mms20+ | Multimedia Messaging Service (MMS) capability to receive and send multimedia messages. Currently, this feature is supported only on smartphones and tablets. | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS |
| sms20+ | Short Messaging Service (SMS) capability to receive and send SMS messages. Currently, this feature is supported only on smartphones and tablets. | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS |
| mobileData20+ | Cellular data capability, which is supported only on smartphones and tablets. | ohos.permission.ENTERPRISE\_MANAGE\_NETWORK |
| airplaneMode20+ | Airplane mode capability, which is supported only on smartphones and tablets. | ohos.permission.ENTERPRISE\_MANAGE\_NETWORK |
| vpn20+ | Virtual Private Network (VPN) capability. | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS |
| notification20+ | Device notification capability. | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS |
| nfc20+ | Near Field Communication (NFC) capability, which is supported only on phones and tablets. | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS |
| privateSpace20+ | Privacy space creation capability, which is supported only on smartphones and tablets. | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS |
| telephoneCall20+ | Call capability. Disabling this feature blocks incoming or outgoing calls. Currently, this feature is supported only on smartphones and tablets. | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS |
| appClone21+ | [Application clone capability](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-clone). When this feature is disabled, new application clones cannot be created. | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS |
| externalStorageCard21+ | External storage capability. | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS |
| randomMac21+ | Random MAC address capability for Wi-Fi connections. | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS |
| unmuteDevice22+ | Device audio playback capability. When this feature is disabled, media playback will be muted, while [cellular calls](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/audio-call-overview) remain unaffected. | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS |
| hdcRemote22+ | Capability of the device to debug other devices through HDC. Currently, this feature can be set only for PCs/2-in-1 devices. | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS |
| screenshot | Device screen capture capability. | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS or ohos.permission.PERSONAL\_MANAGE\_RESTRICTIONS |
| screenRecord | Device screen recording capability. | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS or ohos.permission.PERSONAL\_MANAGE\_RESTRICTIONS |
| diskRecoveryKey | Recovery key export capability. | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS |
| nearLink | Device NearLink capability. | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS or ohos.permission.PERSONAL\_MANAGE\_RESTRICTIONS |
| developerMode14+ | Developer mode, which takes effect after the device is restarted. Currently, this mode is supported only on PCs and 2-in-1 devices. | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS |
| resetFactory18+ | Factory reset capability. | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS or ohos.permission.PERSONAL\_MANAGE\_RESTRICTIONS |
| remoteDesk20+ | Remote desktop capability. You can go to **My HUAWEI** > **Services** > **Quick services** > **Smart Diagnosis**, tap the icon in the upper right corner, and select **Remote Service** to check it. Currently, this feature is available only for mobile phones, tablets, and PCs/2-in-1 devices. | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS |
| remoteDiagnosis20+ | Remote diagnosis capability. You can go to **My HUAWEI** > **Services** > **Quick services** > **Smart Diagnosis**, tap the icon in the upper right corner, and select **Diagnostic Analysis** to check it. Currently, this feature is available only for mobile phones, tablets, and PCs/2-in-1 devices. | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS |
| otaUpdate20+ | System upgrade capability on public networks. | ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | The value **true** means the feature is disallowed; the value **false** means the opposite. |

**Error codes**

For details about the error codes, see [Enterprise Device Management Error Codes](../../error-codes/enterprise-device-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**Example**

import { restrictions } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  // Replace parameters with actual values.
  let result: boolean = restrictions.getDisallowedPolicy(wantTemp, 'printer');
  console.info(\`Succeeded in querying whether the printing function is disabled. Disabled status: ${result}\`);
} catch (err) {
  console.error(\`Failed to get printer disabled status. Code is ${err.code}, message is ${err.message}\`);
}

#### restrictions.setDisallowedPolicyForAccount14+

setDisallowedPolicyForAccount(admin: Want, feature: string, disallow: boolean, accountId: number): void

Disallows a feature for a specified user.

**Required permissions**: ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| feature | string | Yes | 
Feature to set.

\- **fingerprint**: device fingerprint authentication capability. Currently, this feature is supported only on PCs/2-in-1 devices. The rules for using this parameter are as follows:

1\. If this capability has been disabled through the [setDisallowedPolicy](#restrictionssetdisallowedpolicy) API, using **setDisallowedPolicyForAccount** will throw a policy conflict.

2\. When **setDisallowedPolicyForAccount** is used to disable or enable the device fingerprint authentication capability for a specified user, any subsequent action via the [setDisallowedPolicy](#restrictionssetdisallowedpolicy) API will override the previous setting. If [setDisallowedPolicy](#restrictionssetdisallowedpolicy) enables the capability, all users gain access to the device fingerprint authentication.

\- **print**20+: device printing capability, which is supported only on PCs/2-in-1 devices. If printing is disabled via this API, it remains disabled for specific users even if the [setDisallowedPolicy](#restrictionssetdisallowedpolicy) API is used to enable it for those users.

\- **mtpClient**20+: Media Transfer Protocol (MTP) client capability (write only). Currently, this feature is supported only on PCs/2-in-1 devices. MTP allows users to linearly access media files on mobile devices. A policy conflict error will occur if this API is used to disable MTP client capability after MTP client write access has been disabled for specific users via the [setDisallowedPolicy](#restrictionssetdisallowedpolicy) API.

\- **usbStorageDeviceWrite**20+: USB storage device write capability. Currently, this feature is supported only on enterprise PCs/2-in-1 devices.

If the USB storage device write permission of a user is disabled via this API in any of the following situations, a policy conflict will be reported:

1\. The device USB capability has been disabled via the [setDisallowedPolicy](#restrictionssetdisallowedpolicy) API.

2\. USB storage device access policy has been set to read-only or disabled via the [setUsbStorageDeviceAccessPolicy](../ohos-enterprise-usbmanager-usb-management/document.md#usbmanagersetusbstoragedeviceaccesspolicy) API.

3\. Storage USB devices have been disabled via the [addDisallowedUsbDevices](../ohos-enterprise-usbmanager-usb-management/document.md#usbmanageradddisallowedusbdevices14) API.

\- **diskRecoveryKey**20+: recovery [key export](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/huks-export-key-arkts) capability. Currently, this feature is supported only on PCs/2-in-1 devices.

\- **sudo**20+: superuser do (execution with superuser privileges). Currently, this feature is supported only on PCs/2-in-1 devices. If this feature is disabled, neither enterprise spaces nor personal spaces can perform operations with superuser privileges.

\- **distributedTransmissionOutgoing**20+: one-way data transmission between devices (only data transmission to other devices is supported).

 |
| disallow | boolean | Yes | Whether to disallow the feature. The value **true** means to disallow the feature; the value **false** means the opposite. |
| accountId | number | Yes | 

User ID, which must be greater than or equal to 0.

You can call [getOsAccountLocalId](../../../basic-services-kit/arkts-apis/account-management/ohos-account-osaccount-system-account-management/document.md#getosaccountlocalid9) to obtain the user ID.

 |

**Error codes**

For details about the error codes, see [Enterprise Device Management Error Codes](../../error-codes/enterprise-device-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | the administrator application does not have permission to manage the device. |
| 9200010 | A conflict policy has been configured. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**Example**

import { restrictions } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  // Replace parameters with actual values.
  restrictions.setDisallowedPolicyForAccount(wantTemp, 'fingerprint', true, 100);
  console.info('Succeeded in setting fingerprint disabled');
} catch (err) {
  console.error(\`Failed to set fingerprint disabled. Code is ${err.code}, message is ${err.message}\`);
}

#### restrictions.getDisallowedPolicyForAccount14+

getDisallowedPolicyForAccount(admin: Want | null, feature: string, accountId: number): boolean

Obtains the status of a feature for a specified user.

**Required permissions**: ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | null | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| feature | string | Yes | 
Feature to set.

\- **fingerprint**: device fingerprint authentication capability. Currently, this feature is supported only on PCs/2-in-1 devices. Note that when [setDisallowedPolicyForAccount](#restrictionssetdisallowedpolicyforaccount14) is used to disable or enable the device fingerprint authentication capability for a specified user, any subsequent action via the [setDisallowedPolicy](#restrictionssetdisallowedpolicy) API will override the previous setting. The value **false** will be returned.

\- **mtpClient**20+: Media Transfer Protocol (MTP) client capability (write only). Currently, this feature is supported only on PCs/2-in-1 devices. MTP allows users to linearly access media files on mobile devices.

\- **usbStorageDeviceWrite**20+: USB storage device write capability. Currently, this feature is supported only on enterprise PCs/2-in-1 devices.

\- **diskRecoveryKey**20+: recovery [key export](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/huks-export-key-arkts) capability. Currently, this feature is supported only on PCs/2-in-1 devices.

\- **sudo**20+: superuser do (execution with superuser privileges). Currently, this feature is supported only on PCs/2-in-1 devices. If this feature is disabled, neither enterprise spaces nor personal spaces can perform operations with superuser privileges.

\- **distributedTransmissionOutgoing**20+: one-way data transmission between devices (only data transmission to other devices is supported).

\- **print**20+: device printing capability, which is supported only on PCs/2-in-1 devices. If printing is disabled via the [setDisallowedPolicy](#restrictionssetdisallowedpolicy) API, it remains disabled even if the [setDisallowedPolicyForAccount](#restrictionssetdisallowedpolicyforaccount14) API is used to enable it for specific users.

 |
| accountId | number | Yes | 

User ID, which must be greater than or equal to 0.

You can call [getOsAccountLocalId](../../../basic-services-kit/arkts-apis/account-management/ohos-account-osaccount-system-account-management/document.md#getosaccountlocalid9) to obtain the user ID.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | The value **true** means the feature is disabled; the value **false** means the opposite. |

**Error codes**

For details about the error codes, see [Enterprise Device Management Error Codes](../../error-codes/enterprise-device-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | the administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**Example**

import { restrictions } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  // Replace parameters with actual values.
  let result: boolean = restrictions.getDisallowedPolicyForAccount(wantTemp, 'fingerprint', 100);
  console.info(\`Succeeded in querying is the fingerprint function disabled : ${result}\`);
} catch (err) {
  console.error(\`Failed to set fingerprint disabled. Code is ${err.code}, message is ${err.message}\`);
}

#### restrictions.addDisallowedListForAccount14+

addDisallowedListForAccount(admin: Want, feature: string, list: Array<string>, accountId: number): void

Adds a list of applications that are not allowed to use a feature for a specified user.

**Required permissions**: ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| feature | string | Yes | 
Feature to set.

\- **snapshotSkip**: screen snapshot capability.

 |
| list | Array<string> | Yes | List of content such as the bundle names. |
| accountId | number | Yes | 

User ID, which must be greater than or equal to 0.

You can call [getOsAccountLocalId](../../../basic-services-kit/arkts-apis/account-management/ohos-account-osaccount-system-account-management/document.md#getosaccountlocalid9) to obtain the user ID.

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

import { restrictions } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
// Replace with actual values.
let valueList:Array<string> = \["com.xx.aa.", "com.xx.bb"\];
try {
  // Replace parameters with actual values.
  restrictions.addDisallowedListForAccount(wantTemp, 'snapshotSkip', valueList, 100);
  console.info('Succeeded in adding disallowed snapshotSkip feature');
} catch (err) {
  console.error(\`Failed to add disallowed snapshotSkip feature. Code is ${err.code}, message is ${err.message}\`);
}

#### restrictions.removeDisallowedListForAccount14+

removeDisallowedListForAccount(admin: Want, feature: string, list: Array<string>, accountId: number): void

Removes the list of applications that are not allowed to use a feature for a specified user.

**Required permissions**: ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| feature | string | Yes | 
Feature to set.

\- **snapshotSkip**: screen snapshot capability.

 |
| list | Array<string> | Yes | List of content such as the bundle names. |
| accountId | number | Yes | 

User ID, which must be greater than or equal to 0.

You can call [getOsAccountLocalId](../../../basic-services-kit/arkts-apis/account-management/ohos-account-osaccount-system-account-management/document.md#getosaccountlocalid9) to obtain the user ID.

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

import { restrictions } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
// Replace with actual values.
let valueList:Array<string> = \["com.xx.aa.", "com.xx.bb"\];
try {
  // Replace parameters with actual values.
  restrictions.removeDisallowedListForAccount(wantTemp, 'snapshotSkip', valueList, 100);
  console.info('Succeeded in removing disallowed snapshotSkip feature');
} catch (err) {
  console.error(\`Failed to remove disallowed snapshotSkip feature. Code is ${err.code}, message is ${err.message}\`);
}

#### restrictions.getDisallowedListForAccount14+

getDisallowedListForAccount(admin: Want, feature: string, accountId: number): Array<string>

Obtains the list of applications that are not allowed to use a feature for a specified user.

**Required permissions**: ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| feature | string | Yes | 
Feature to set.

\- **snapshotSkip**: screen snapshot capability.

 |
| accountId | number | Yes | 

User ID, which must be greater than or equal to 0.

You can call [getOsAccountLocalId](../../../basic-services-kit/arkts-apis/account-management/ohos-account-osaccount-system-account-management/document.md#getosaccountlocalid9) to obtain the user ID.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Array<string> | List of applications that have been added by the user and for which a certain feature is disabled. |

**Error codes**

For details about the error codes, see [Enterprise Device Management Error Codes](../../error-codes/enterprise-device-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { restrictions } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  // Replace parameters with actual values.
  let result: Array<string> = restrictions.getDisallowedListForAccount(wantTemp, 'snapshotSkip', 100);
  console.info('Succeeded in querying disallowed list for account');
} catch (err) {
  console.error(\`Failed to query disallowed list for account. Code is ${err.code}, message is ${err.message}\`);
}

#### restrictions.setUserRestriction20+

setUserRestriction(admin: Want, settingsItem: string, restricted: boolean): void

Sets restrictions on user behaviors.

**Required permissions**: ohos.permission.ENTERPRISE\_SET\_USER\_RESTRICTION

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| settingsItem | string | Yes | 
User behavior.

\- **setApn**: APN configuration, currently supported only on smartphones and tablets.

\- **powerLongPress**: capability to open the power menu by long-pressing the power button. Currently, only smartphones and tablets are supported.

\- **setEthernetIp**: Ethernet IP address configuration, currently supported only on PCs/2-in-1 devices.

\- **setDeviceName**: device name configuration, currently supported only on PCs/2-in-1 devices, smartphones, and tablets. When it is disabled, the device name cannot be modified in the following settings: **About**, **Bluetooth**, and **More connectivity options** > **NearLink** on PCs/2-in-1 devices, and **About**, **Bluetooth**, and **Personal hotspot** on smartphones and tablets.

\- **setBiometricsAndScreenLock**: screen lock password configuration, currently supported only on PCs/2-in-1 devices, smartphones, and tablets.

 |
| restricted | boolean | Yes | Whether to disable the action. The value **true** means to disable the action, and **false** means the opposite. |

**Error codes**

For details about the error codes, see [Enterprise Device Management Error Codes](../../error-codes/enterprise-device-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**Example**

import { Want } from '@kit.AbilityKit';
import { restrictions } from '@kit.MDMKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  // Replace parameters with actual values.
  restrictions.setUserRestriction(wantTemp, 'setApn', true);
  console.info('Succeeded in restricting from setting apn');
} catch (err) {
  console.error(\`Failed to restrict from setting apn. Code is ${err.code}, message is ${err.message}\`);
}

#### restrictions.getUserRestricted20+

getUserRestricted(admin: Want, settingsItem: string): boolean

Obtains the disabled status of a setting item.

**Required permissions**: ohos.permission.ENTERPRISE\_SET\_USER\_RESTRICTION

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| settingsItem | string | Yes | 
Setting item.

\- **setEthernetIp**: Ethernet IP address configuration, currently supported only on PCs/2-in-1 devices.

\- **setDeviceName**: device name configuration, currently supported only on PCs/2-in-1 devices, smartphones, and tablets. When it is disabled, the device name cannot be modified in the following settings: **About**, **Bluetooth**, and **More connectivity options** > **NearLink** on PCs/2-in-1 devices, and **About**, **Bluetooth**, and **Personal hotspot** on smartphones and tablets.

\- **setBiometricsAndScreenLock**: screen lock password configuration, currently supported only on PCs/2-in-1 devices, smartphones, and tablets.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Disabled status of the specified setting item. The value **true** means the item is disabled; the value **false** means the opposite. |

**Error codes**

For details about the error codes, see [Enterprise Device Management Error Codes](../../error-codes/enterprise-device-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**Example**

import { Want } from '@kit.AbilityKit';
import { restrictions } from '@kit.MDMKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  // Replace input parameters with actual values.
  let result: boolean = restrictions.getUserRestricted(wantTemp, 'setEthernetIp');
  console.info('Succeeded in getting user restricted');
} catch (err) {
  console.error(\`Failed to get user restricted. Code is ${err.code}, message is ${err.message}\`);
}
