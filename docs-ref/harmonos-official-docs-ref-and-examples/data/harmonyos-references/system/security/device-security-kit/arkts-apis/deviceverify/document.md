# DeviceVerify

This module checks and manages the status of an app on a device, including determining whether the app is installed for the first time on the device or whether the user has obtained a coupon on the device, to support new user acquisition campaigns.

**Start version**: 5.0.0(12)

#### Module Import

import { deviceCertificate } from '@kit.DeviceSecurityKit';

#### \[h2\]getDeviceToken

getDeviceToken(): Promise<string>

Obtains the device token of a device. This API returns the result asynchronously through a promise.

**Atomic service API**: This API can be used in atomic services since API version 5.0.2(14).

**System capability**: SystemCapability.Security.DeviceCertificate

**Start version**: 5.0.0(12)

**Returns:**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<string>

 | 

Promise used to return the device token of a device.

 |

**Error codes:**

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

[201](../arkts-api-error-codes/deviceverify/document.md#section1196513239128)

 | 

has no permission.

 |
| 

[1003300005](../arkts-api-error-codes/deviceverify/document.md#section4523135612196)

 | 

internal error.

 |
| 

[1003300006](../arkts-api-error-codes/deviceverify/document.md#section179661348180)

 | 

access cloud server fail.

 |

**Example:**

import { deviceCertificate } from '@kit.DeviceSecurityKit';
import { BusinessError} from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = "DeviceCertificateJsTest";

// Request the device token and process the result.
try {
  deviceCertificate.getDeviceToken().then((token) => {
      hilog.info(0x0000, TAG, 'Succeeded in executing getDeviceToken');
      // Process the device token.
  }).catch((err: BusinessError) => {
      hilog.error(0x0000, TAG, 'getDeviceToken failed!  %{public}d %{public}s', err.code, err.message);
  });
} catch (err) {
  let error: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'getDeviceToken failed!  %{public}d %{public}s', error.code, error.message);
}
