# @ohos.enterprise.deviceInfo (Device Information Management)

The **deviceInfo** module provides APIs for enterprise device information management, including obtaining device serial numbers and device names.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/IPQi-yADS9ag6ZeY9KR9WQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062406Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=42A0B67BCE27A8FC88D4043864E9A2B6AE967FED26D935748CE163D0DC3A7D95)

-   The initial APIs of this module are supported since API version 12. Newly added APIs will be marked with a superscript to indicate their earliest API version.
    
-   The APIs of this module can be used only in the stage model.
    
-   The APIs of this module can be called only by a device administrator application that is enabled. For details, see [MDM Kit Development](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/mdm-kit-guide).
    

#### Modules to Import

import { deviceInfo } from '@kit.MDMKit';

#### deviceInfo.getDeviceInfo

getDeviceInfo(admin: Want, label: string): string

Obtains device information.

**Required permissions**: ohos.permission.ENTERPRISE\_GET\_DEVICE\_INFO

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| label | string | Yes | 
Device information label that can be obtained.

\- **deviceName**: device name.

\- **deviceSerial**: device serial number.

\- **simInfo**: SIM card information.

\- **disk**: disk information.

\- **memory**: memory information. Currently, it is available only for PCs/2-in-1 devices.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| string | 
Device information obtained.

If **label** is **simInfo**, the return value is the SIM card information in a JSON string. For example, \[{"slotId": 0, "MEID": "", "IMSI": "", "ICCID": "", "IMEI": ""}, {"slotId": 1, "MEID": "", "IMSI": "", "ICCID": "", "IMEI": ""}\], where **slotId:0** indicates card slot 1, and **slotId:1** indicates card slot 2.

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

import { deviceInfo } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  // Replace with actual values.
  let result: string = deviceInfo.getDeviceInfo(wantTemp, 'deviceName');
  console.info(\`Succeeded in getting device name, result : ${result}\`);
} catch (err) {
  console.error(\`Failed to get device name. Code: ${err.code}, message: ${err.message}\`);
}
