# @ohos.enterprise.locationManager (Location Service Management)

The **locationManager** module provides location service management capabilities for devices, including setting and obtaining the location service policy.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/zy8_ayvWQXyrMHFt2ocmJA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062406Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AC19D70A38182FCE091342298336A7A86AEB4515822ADB638225E0B11F8C1F45)

-   The initial APIs of this module are supported since API version 12. Newly added APIs will be marked with a superscript to indicate their earliest API version.
    
-   The APIs of this module can be used only in the stage model.
    
-   The APIs of this module can be called only by a device administrator application that is enabled. For details, see [MDM Kit Development](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/mdm-kit-guide).
    

#### Modules to Import

import { locationManager } from '@kit.MDMKit';

#### locationManager.setLocationPolicy

setLocationPolicy(admin: Want, policy: LocationPolicy): void

Sets a location service policy.

**Required permissions**: ohos.permission.ENTERPRISE\_MANAGE\_LOCATION

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| policy | [LocationPolicy](#locationpolicy) | Yes | 
Location service policy to set. The value can be any of the following:

\- **0**: The default policy is used.

\- **1**: The location service is disabled.

\- **2**: The location service is forcibly enabled.

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

import { locationManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
    locationManager.setLocationPolicy(wantTemp, locationManager.LocationPolicy.DISALLOW\_LOCATION\_SERVICE);
    console.info(\`Succeeded in setting location patch tag.\`);
} catch(err) {
    console.error(\`Failed to get location patch tag. Code: ${err.code}, message: ${err.message}\`);
}

#### locationManager.getLocationPolicy

getLocationPolicy(admin: Want): LocationPolicy

Queries the location service policy.

**Required permissions**: ohos.permission.ENTERPRISE\_MANAGE\_LOCATION

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| admin | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |

**Return value**

| Type | Description |
| :-- | :-- |
| [LocationPolicy](#locationpolicy) | Enumerated value of the location service policy. **0**: The default policy is used. **1**: The location service is disabled. **2**: The location service is forcibly enabled. |

**Error codes**

For details about the error codes, see [Enterprise Device Management Error Codes](../../error-codes/enterprise-device-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { locationManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
    let result: locationManager.LocationPolicy = locationManager.getLocationPolicy(wantTemp);
    console.info(\`Succeeded in getting location policy. policy: ${result}\`);
} catch(err) {
    console.error(\`Failed to get location policy. Code: ${err.code}, message: ${err.message}\`);
}

#### LocationPolicy

Enumerates the location service policies.

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

| Name | Value | Description |
| :-- | :-- | :-- |
| DEFAULT\_LOCATION\_SERVICE | 0 | Default policy. |
| DISALLOW\_LOCATION\_SERVICE | 1 | The location service is disabled. |
| FORCE\_OPEN\_LOCATION\_SERVICE | 2 | The location service is forcibly enabled. |
