# @ohos.enterprise.deviceControl (Device Control Management)

The **deviceControl** module provides APIs for device control.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/H7k6Pm1sRwyEWWJoXKaJsg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062406Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7E2323F1DDE59E15E037DF2F8F861E866DD1B343EDDA1FE67A90752997F03594)

The initial APIs of this module are supported since API version 12. Newly added APIs will be marked with a superscript to indicate their earliest API version.

The APIs of this module can be used only in the stage model.

The APIs of this module can be called only by a device administrator application that is enabled. For details, see [MDM Kit Development](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/mdm-kit-guide).

#### Modules to Import

import { deviceControl } from '@kit.MDMKit';

#### deviceControl.operateDevice

operateDevice(admin: Want, operate: string, addition?: string): void

Allows the specified device administrator application to operate devices.

**Required permissions**: ohos.permission.ENTERPRISE\_OPERATE\_DEVICE

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| operate | string | Yes | 
Operation to be performed, which can be any of the following:

\- **resetFactory**: restore device factory settings. After this API is called, the device will be restored to factory settings immediately. Once the restoration is complete, all device data will be erased and cannot be restored. To protect against data loss caused by potential application attacks, enterprises should implement robust security measures for their applications.

\- **reboot**: restart devices.

\- **shutDown**: shut down devices.

\- **lockScreen**: lock device screens.

\- **lockDevice**: lock devices. After a device is locked, its screen is unusable and buttons are unresponsive. During development, an "emergency escape route" must be reserved and verified before deploying device lock policies. You are advised to maintain the hdc and remote communication capabilities during development to allow for device unlocking via hdc commands or remote push capability.

\- **unlockDevice**: unlock devices.

Prior to API version 21, device lock and unlock are available only on PCs/2-in-1 devices. Since API version 21, support has been extended to phones and tablets.

 |
| addition | string | No | Additional parameter for the operation. If **operate** is set to **lockDevice**, this parameter indicates the description displayed after the screen is locked. |

**Error codes**

For details about the error codes, see [Enterprise Device Management Error Codes](../../error-codes/enterprise-device-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { deviceControl } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace it as required.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  // Replace the parameters as required.
  deviceControl.operateDevice(wantTemp, 'resetFactory');
} catch (err) {
  console.error(\`Failed to reset factory. Code is ${err.code}, message is ${err.message}\`);
}
