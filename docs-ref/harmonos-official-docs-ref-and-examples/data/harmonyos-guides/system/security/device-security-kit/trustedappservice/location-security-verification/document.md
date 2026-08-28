# Location Security Verification

#### Use Cases

Geographical location information obtained from the GPS hardware or network location is signed by creating an attestation key and initializing an attestation session, to ensure authenticity and integrity of the geographical location information.

#### Restrictions

This feature requires that the device supports location security verification.

After calling [initializeAttestContext](https://developer.huawei.com/consumer/en/doc/harmonyos-references/devicesecurity-taas-api#section166716269293) to initialize the attestation session for location security verification, you can call [getCurrentSecureLocation](https://developer.huawei.com/consumer/en/doc/harmonyos-references/devicesecurity-taas-api#section1744710293017) to obtain the data to verify location security. If the API call fails with [ATTEST\_ERROR\_LOCATION\_SERVICE\_UNAVAILABLE](https://developer.huawei.com/consumer/en/doc/harmonyos-references/devicesecurity-arktsapi-errcode-taas#section108810541837) returned, the current device does not support location security verification. The following is an example:

import { trustedAppService } from '@kit.DeviceSecurityKit';
import { BusinessError } from '@kit.BasicServicesKit';

// After the attestation session for location security verification is initialized, obtain the data to verify location security. The following uses the "Accuracy first" policy as an example:
const timeout = 5000; // Timeout interval for obtaining the data to verify location security, in milliseconds.
const priority = trustedAppService.LocatingPriority.PRIORITY\_ACCURACY; // The "Accuracy first" policy is used.
let secureLocation: trustedAppService.SecureLocation;
// Obtain the data to verify location security.
try {
  secureLocation = await trustedAppService.getCurrentSecureLocation(timeout, priority);
} catch (err) {
  const error = err as BusinessError;
  if (error.code == trustedAppService.AttestExceptionErrCode.ATTEST\_ERROR\_LOCATION\_SERVICE\_UNAVAILABLE) {
      console.error(\`current device not support secure location\`);
  } else {
      console.error(\`Failed to get current secure location, message:${error.message}, code:${error.code}\`);
  }
}

#### Service Process

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/5y2C9v--QLuVObn4J7gCJQ/en-us_image_0000002482908426.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062006Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=408E376FE2640FD7149D7ED200A1D917188E273A386D3724A3FC1EE5C08C83E1 "Click to enlarge")

There are two priority policies for an app to obtain the data to verify location security: accuracy first and speed first. If the accuracy first policy is used, TrustedAppService returns the GPS location preferentially, and returns the network location if obtaining the GPS location times out. If the speed first policy is used, TrustedAppService returns the GPS or network location whichever is obtained first.

#### API Description

For details about the APIs, please refer to [API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/devicesecurity-taas-api).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[createAttestKey](https://developer.huawei.com/consumer/en/doc/harmonyos-references/devicesecurity-taas-api#section81796536265)(options: AttestOptions): Promise<void>

 | 

Creates an attestation key.

 |
| 

[initializeAttestContext](https://developer.huawei.com/consumer/en/doc/harmonyos-references/devicesecurity-taas-api#section166716269293)(userData: string, options: AttestOptions): Promise<AttestReturnResult>

 | 

Initializes an attestation session.

 |
| 

[finalizeAttestContext](https://developer.huawei.com/consumer/en/doc/harmonyos-references/devicesecurity-taas-api#section18667940102912)(options: AttestOptions): Promise<void>

 | 

Ends an attestation session.

 |
| 

[destroyAttestKey](https://developer.huawei.com/consumer/en/doc/harmonyos-references/devicesecurity-taas-api#section19260221152819)(): Promise<void>

 | 

Destroys an attestation key.

 |
| 

[getCurrentSecureLocation](https://developer.huawei.com/consumer/en/doc/harmonyos-references/devicesecurity-taas-api#section1744710293017)(timeout: number, priority: LocatingPriority): Promise<SecureLocation>

 | 

Obtains the data to verify location security.

 |

#### Development Procedure

1.  Apply for the [ohos.permission.APPROXIMATELY\_LOCATION](https://developer.huawei.com/consumer/en/doc/harmonyos-guides-V13/permissions-for-all-V13#ohospermissionapproximately_location) and [ohos.permission.LOCATION](https://developer.huawei.com/consumer/en/doc/harmonyos-guides-V13/permissions-for-all-V13#ohospermissionlocation) permissions. For details, please refer to [Requesting User Authorization](../../../application-access-control/application-permission-management/requesting-application-permissions/requesting-user-authorization/document.md).
2.  Import the TrustedAppService module.
    
    import { trustedAppService } from '@kit.DeviceSecurityKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
3.  Create an attestation key and initialize an attestation session.
    
    // Parameters for creating an attestation key.
    const createProperties: Array<trustedAppService.AttestParam> = \[
      {
        tag: trustedAppService.AttestTag.ATTEST\_TAG\_ALGORITHM,
        value: trustedAppService.AttestKeyAlg.ATTEST\_ALG\_ECC
      },
      {
        tag: trustedAppService.AttestTag.ATTEST\_TAG\_KEY\_SIZE,
        value: trustedAppService.AttestKeySize.ATTEST\_ECC\_KEY\_SIZE\_256
      }
    \];
    const createOptions: trustedAppService.AttestOptions = {
      properties: createProperties
    };
    // Parameters for initializing an attestation session.
    const userData = "trusted\_app\_service\_demo" // Example value. Generate a value on your own, which contains 16 to 127 bytes.
    const initProperties: Array<trustedAppService.AttestParam> = \[
      {
        tag: trustedAppService.AttestTag.ATTEST\_TAG\_DEVICE\_TYPE,
        value: trustedAppService.AttestType.ATTEST\_TYPE\_LOCATION
      },
      {
        tag: trustedAppService.AttestTag.ATTEST\_TAG\_DEVICE\_ID,
        value: BigInt(0) // This parameter does not take effect in the location security verification scenario.
      }
    \];
    const initOptions: trustedAppService.AttestOptions = {
      properties: initProperties
    };
    // Create an attestation key and initialize an attestation session.
    let certChainList: Array<string>;
    try {
      await trustedAppService.createAttestKey(createOptions);
      const result = await trustedAppService.initializeAttestContext(userData, initOptions);
      certChainList = result.certChains;
    } catch (err) {
      const error = err as BusinessError;
      console.error(\`Failed to initialize attest context, message:${error.message}, code:${error.code}\`);
    }
    
4.  Obtain the data to verify location security. The following uses the "Accuracy first" policy as an example:
    
    const timeout = 5000; // Timeout interval for obtaining the data to verify location security, in milliseconds.
    const priority = trustedAppService.LocatingPriority.PRIORITY\_ACCURACY; // The "Accuracy first" policy is used.
    let secureLocation: trustedAppService.SecureLocation;
    // Obtain the data to verify location security.
    try {
      secureLocation = await trustedAppService.getCurrentSecureLocation(timeout, priority);
    } catch (err) {
      const error = err as BusinessError;
      console.error(\`Failed to get current secure location, message:${error.message}, code:${error.code}\`);
    }
    
5.  End the attestation session.
    
    // Parameters for ending the attestation session.
    const finalProperties: Array<trustedAppService.AttestParam> = \[
      {
        tag: trustedAppService.AttestTag.ATTEST\_TAG\_DEVICE\_TYPE,
        value: trustedAppService.AttestType.ATTEST\_TYPE\_LOCATION
      }
    \];
    const finalOptions: trustedAppService.AttestOptions = {
      properties: finalProperties,
    };
    // End the attestation session.
    try {
      await trustedAppService.finalizeAttestContext(finalOptions);
    } catch (err) {
      const error = err as BusinessError;
      console.error(\`Failed to finalize attest context, message:${error.message}, code:${error.code}\`);
    }
    
    To destroy the attestation key, call the [destroyAttestKey](https://developer.huawei.com/consumer/en/doc/harmonyos-references/devicesecurity-taas-api#section19260221152819) API after the attestation session ends.
