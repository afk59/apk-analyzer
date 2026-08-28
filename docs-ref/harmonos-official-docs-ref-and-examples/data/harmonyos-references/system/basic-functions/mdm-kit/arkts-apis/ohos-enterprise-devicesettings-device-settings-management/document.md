# @ohos.enterprise.deviceSettings (Device Settings Management)

The **deviceSettings** module provides APIs for setting enterprise devices, including setting and obtaining the screen-off time of a device.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/sTkx2A6tRKCbHHV060WJZQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062406Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FB9DDA3886F0FF7B4F7E28C1C5203CEF10C8CF5CBC361979F81481C49FCF108D)

The initial APIs of this module are supported since API version 12. Newly added APIs will be marked with a superscript to indicate their earliest API version.

The APIs of this module can be used only in the stage model.

The APIs of this module can be called only by a device administrator application that is enabled. For details, see [MDM Kit Development](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/mdm-kit-guide).

#### Modules to Import

import { deviceSettings } from '@kit.MDMKit';

#### deviceSettings.setValue

setValue(admin: Want, item: string, value: string): void

Sets the device policy.

**Required permissions**: ohos.permission.ENTERPRISE\_MANAGE\_SETTINGS

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| item | string | Yes | 
Type of the policy to set.

\- **screenOff**: screen-off policy. For PCs/2-in-1 devices, only the screen-off policy in battery mode can be set.

\- **dateTime**: system time settings.

\- **powerPolicy**: device power policy. For PCs/2-in-1 devices, only the power policy in battery mode can be set.

 |
| value | string | Yes | 

Policy type value.

If **item** is **screenOff**, **value** is the screen-off time, in ms.

If **item** is **dateTime**, **value** is the system time to set, in ms.

If **item** is **powerPolicy**, **value** is a JSON string in {"powerScene":xx,"powerPolicy":{"powerPolicyAction":xx,"delayTime":xx}} format. **powerScene** specifies the power policy scenario; **delayTime** specifies the delay time in ms (it cannot be set to 30000 ms); **powerPolicyAction** specifies the sleep policy.

The value of **powerScene** can be:

\- **0**: timeout.

The value of **powerPolicyAction** can be:

\- **0**: No action is performed.

\- **1**: enter sleep mode automatically.

\- **2**: forcibly enter sleep mode.

\- **3**: enter sleep mode. This policy does not take effect currently.

\- **4**: power off.

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

import { deviceSettings } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  // Replace with actual values.
  deviceSettings.setValue(wantTemp, 'screenOff', '3000');
  console.info(\`Succeeded in setting screen off time.\`);
} catch (err) {
  console.error(\`Failed to set screen off time. Code: ${err.code}, message: ${err.message}\`);
}

#### deviceSettings.getValue

getValue(admin: Want, item: string): string

Obtains a device setting policy.

**Required permissions**: ohos.permission.ENTERPRISE\_MANAGE\_SETTINGS

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| item | string | Yes | 
Type of the policy to set.

\- **screenOff**: screen-off policy of a device. For PCs/2-in-1 devices, only the screen-off policy in battery mode can be obtained.

\- **powerPolicy**: device power policy. For PCs/2-in-1 devices, only the power policy in battery mode can be obtained.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| string | 
Policy type value.

If **item** is **screenOff**, the device screen-off time (in ms) is returned. For PCs/2-in-1 devices, the device screen-off time (in ms) in battery mode is returned.

If **item** is **powerPolicy**, the power policy is returned. For PCs/2-in-1 devices, the power policy in battery mode is returned. The power policy a JSON string in {"powerScene":xx,"powerPolicy":{"powerPolicyAction":xx,"delayTime":xx}} format. **powerScene** indicates the power policy scenario, **delayTime** indicates the delay time (in ms), and **powerPolicyAction** indicates the sleep policy.

The value of **powerScene** can be:

\- **0**: timeout.

The value of **powerPolicyAction** can be:

\- **0**: No action is performed.

\- **1**: enter sleep mode automatically.

\- **2**: forcibly enter sleep mode.

\- **3**: enter sleep mode. This policy does not take effect currently.

\- **4**: power off.

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

import { deviceSettings } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  // Replace parameters with actual values.
  let result: string = deviceSettings.getValue(wantTemp, 'screenOff');
  console.info(\`Succeeded in getting screen off time, result : ${result}\`);
} catch (err) {
  console.error(\`Failed to get screen off time. Code: ${err.code}, message: ${err.message}\`);
}

#### deviceSettings.setHomeWallpaper20+

setHomeWallpaper(admin: Want, fd: number): Promise<void>

Sets the home screen wallpaper. This API uses a promise to return the result.

**Required permissions**: ohos.permission.ENTERPRISE\_SET\_WALLPAPER

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| fd | number | Yes | File descriptor of the image to be set as the home screen wallpaper. The file descriptor of an image in the application's sandbox directory can be obtained via the file.fs.[openSync](../../../../../application-framework/core-file-kit/arkts-apis/ohos-file-fs-file-management/document.md#fsopensync) API. The size of the wallpaper image must not exceed 100 MB. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. An error object is thrown when the home screen wallpaper fails to be set. |

**Error codes**

For details about the error codes, see [Enterprise Device Management Error Codes](../../error-codes/enterprise-device-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9200012 | Parameter verification failed. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**Example**

import { deviceSettings } from '@kit.MDMKit';
import { common, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo as fs }  from '@kit.CoreFileKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
const context = this.getUIContext().getHostContext() as common.UIAbilityContext;
// Replace parameters with actual values.
let filename: string = "homewallpaper.jpg";
let filePath: string = context.filesDir + '/' + filename;
let fd: number = fs.openSync(filePath, fs.OpenMode.READ\_WRITE).fd;
deviceSettings.setHomeWallpaper(wantTemp, fd).then(() => {
  console.info('Succeeded in setting home wallpaper');
}).catch((err: BusinessError) => {
  console.error(\`Failed to set home wallpaper. Code: ${err.code}, message: ${err.message}\`);
}).finally(() => {
  fs.closeSync(fd);
});

#### deviceSettings.setUnlockWallpaper20+

setUnlockWallpaper(admin: Want, fd: number): Promise<void>

Sets the lock screen wallpaper. This API uses a promise to return the result.

**Required permissions**: ohos.permission.ENTERPRISE\_SET\_WALLPAPER

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| fd | number | Yes | File descriptor of the image to be set as the lock screen wallpaper. The file descriptor of an image in the application's sandbox directory can be obtained via the file.fs.[openSync](../../../../../application-framework/core-file-kit/arkts-apis/ohos-file-fs-file-management/document.md#fsopensync) API. The size of the wallpaper image must not exceed 100 MB. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. An error object is thrown when the lock screen wallpaper fails to be set. |

**Error codes**

For details about the error codes, see [Enterprise Device Management Error Codes](../../error-codes/enterprise-device-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9200012 | Parameter verification failed. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**Example**

import { deviceSettings } from '@kit.MDMKit';
import { common, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo as fs }  from '@kit.CoreFileKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
const context = this.getUIContext().getHostContext() as common.UIAbilityContext;
// Replace parameters with actual values.
let filename: string = "lockwallpaper.jpg";
let filePath: string = context.filesDir + '/' + filename;
let fd: number = fs.openSync(filePath, fs.OpenMode.READ\_WRITE).fd;
deviceSettings.setUnlockWallpaper(wantTemp, fd).then(() => {
  console.info('Succeeded in setting lock wallpaper');
}).catch((err: BusinessError) => {
  console.error(\`Failed to set lock wallpaper. Code: ${err.code}, message: ${err.message}\`);
});
