# recoveryKey (Enterprise Recovery Key)

Ensures the robustness of user data while guaranteeing its security, facilitating the secure decryption of encrypted hard drive data.

This service is available only for MDM apps that have obtained the service permission.

**Start version**: 5.0.3(15)

#### Module Import

import { recoveryKey } from '@kit.EnterpriseDataGuardKit';

#### EnterpriseRecoveryKeyInfo

Defines the enterprise recovery key and related encryption parameters.

**System capability**: SystemCapability.PCService.RecoveryKeyService

**Start version**: 5.0.3(15)

| 
Parameter

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

enterpriseRecoveryKey

 | 

Uint8Array

 | 

No

 | 

No

 | 

Enterprise recovery key encrypted using AES-GCM-256.

 |
| 

exportPublicKey

 | 

Uint8Array

 | 

No

 | 

No

 | 

Temporary public key used for AES-GCM-256 encryption.

 |
| 

iv

 | 

Uint8Array

 | 

No

 | 

No

 | 

IV used for AES-GCM-256 encryption.

 |
| 

tag

 | 

Uint8Array

 | 

No

 | 

No

 | 

Tag used for AES-GCM-256 encryption.

 |

#### getEnterpriseRecoveryKey

getEnterpriseRecoveryKey(userId: number): Promise<EnterpriseRecoveryKeyInfo>

Obtains an enterprise recovery key.

**Required permission**: ohos.permission.ENTERPRISE\_RECOVERY\_KEY

**System capability**: SystemCapability.PCService.RecoveryKeyService

**Start version**: 5.0.3(15)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

userId

 | 

number

 | 

Yes

 | 

ID of the user for whom an enterprise recovery key needs to be obtained.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[EnterpriseRecoveryKeyInfo](#en-us_topic_0000001983615174_section35870815206)\>

 | 

Promise object used to return the enterprise recovery key and related encryption parameters.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

201

 | 

Permission denied.

 |
| 

401

 | 

The parameter check failed.

 |
| 

1014400001

 | 

System service exception.

 |
| 

1014400201

 | 

Invalid device type, current device is not enterprise device.

 |
| 

1014400202

 | 

Invalid userId.

 |
| 

1014400203

 | 

Enterprise recovery key is already existed.

 |

**Example**:

import { buffer } from '@kit.ArkTS';
import { BusinessError, osAccount } from '@kit.BasicServicesKit';

async function getEnterpriseRecoveryKey() {
  try {
    let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
    let userId: number = await accountManager.getOsAccountLocalId();
    recoveryKey.getEnterpriseRecoveryKey(userId).then((info: recoveryKey.EnterpriseRecoveryKeyInfo) => {
      console.info(\`Succeeded in getting enterprise recovery key.\`);
      console.info(\`EnterpriseRecoveryKeyInfo enterpriseRecoveryKey: ${buffer.from(info.enterpriseRecoveryKey).toString('hex')}\`);
      console.info(\`EnterpriseRecoveryKeyInfo exportPublicKey: ${buffer.from(info.exportPublicKey).toString('hex')}\`);
      console.info(\`EnterpriseRecoveryKeyInfo iv: ${buffer.from(info.iv).toString('hex')}\`);
      console.info(\`EnterpriseRecoveryKeyInfo tag: ${buffer.from(info.tag).toString('hex')}\`);
    }).catch((error: BusinessError) => {
      console.error(\`Failed to get enterprise recovery key. Code: ${error.code}, message: ${error.message}\`);
    });
  } catch (e) {
    console.error(\`Failed to testGetEnterpriseRecoveryKey. Code: ${e.code}, message: ${e.message}\`);
  }
}

#### getAuthChallenge

getAuthChallenge(): Promise<Uint8Array>

Obtains a challenge before initiating the process of updating the enterprise public key certificate or deleting enterprise recovery key data.

**Required permission**: ohos.permission.ENTERPRISE\_RECOVERY\_KEY

**System capability**: SystemCapability.PCService.RecoveryKeyService

**Start version**: 5.0.3(15)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<Uint8Array>

 | 

Challenge obtained before initiating the process of updating the enterprise public key certificate or deleting enterprise recovery key data.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

201

 | 

Permission denied.

 |
| 

1014400001

 | 

System service exception.

 |
| 

1014400201

 | 

Invalid device type, current device is not enterprise device.

 |

**Example**:

import { buffer } from '@kit.ArkTS';
import { BusinessError } from '@kit.BasicServicesKit';

recoveryKey.getAuthChallenge().then((challenge: Uint8Array) => {
  console.info(\`Succeeded in getting challenge. challenge is: ${buffer.from(challenge).toString('hex')}\`);
}).catch((error: BusinessError) => {
  console.error(\`Failed to get challenge. Code: ${error.code}, message: ${error.message}\`);
});

#### updateEnterpriseCertificate

updateEnterpriseCertificate(signature: Uint8Array, cert: Uint8Array): Promise<number>

Updates the enterprise public key certificate. Before this, you need to call the [getAuthChallenge](#en-us_topic_0000001983615174_section41041418113717) API to obtain a challenge and [sign it](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/recoverykey-signature).

**Required permission**: ohos.permission.ENTERPRISE\_RECOVERY\_KEY

**System capability**: SystemCapability.PCService.RecoveryKeyService

**Start version**: 5.0.3(15)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

signature

 | 

Uint8Array

 | 

Yes

 | 

[Signature](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/recoverykey-signature) of the challenge.

 |
| 

cert

 | 

Uint8Array

 | 

Yes

 | 

Public key certificate in PEM format, which needs to be passed in binary format.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<number>

 | 

**Promise** object. If the request is successful, **0** is returned; otherwise, no result is returned.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

201

 | 

Permission denied.

 |
| 

401

 | 

The parameter check failed.

 |
| 

1014400001

 | 

System service exception.

 |
| 

1014400201

 | 

Invalid device type, current device is not enterprise device.

 |
| 

1014400204

 | 

Invalid signature.

 |
| 

1014400205

 | 

Invalid cert.

 |

**Example**:

import { BusinessError } from '@kit.BasicServicesKit';

let signature: Uint8Array = new Uint8Array(\[0\]);
let cert: Uint8Array = new Uint8Array(\[0\]);
recoveryKey.updateEnterpriseCertificate(signature, cert).then((ret: number)=>{
  console.info(\`Succeeded in updating certificate. result is: ${ret}\`);
}).catch((error: BusinessError) => {
  console.error(\`Failed to update certificate. Code: ${error.code}, message: ${error.message}\`);
});

#### deleteEnterpriseRecoveryKey

deleteEnterpriseRecoveryKey(userId: number, signature: Uint8Array): Promise<number>

Deletes data related to the enterprise recovery key. Before this, you need to call the [getAuthChallenge](#en-us_topic_0000001983615174_section41041418113717) API to obtain a challenge and [sign it](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/recoverykey-signature).

**Required permission**: ohos.permission.ENTERPRISE\_RECOVERY\_KEY

**System capability**: SystemCapability.PCService.RecoveryKeyService

**Start version**: 5.0.3(15)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

userId

 | 

number

 | 

Yes

 | 

ID of the user for whom an enterprise recovery key needs to be deleted.

 |
| 

signature

 | 

Uint8Array

 | 

Yes

 | 

[Signature](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/recoverykey-signature) of the challenge.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<number>

 | 

**Promise** object. If the request is successful, **0** is returned; otherwise, no result is returned.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

201

 | 

Permission denied.

 |
| 

401

 | 

The parameter check failed.

 |
| 

1014400001

 | 

System service exception.

 |
| 

1014400201

 | 

Invalid device type, current device is not enterprise device.

 |
| 

1014400202

 | 

Invalid userId.

 |
| 

1014400204

 | 

Invalid signature.

 |

**Example**:

import { BusinessError, osAccount } from '@kit.BasicServicesKit';

async function deleteEnterpriseRecoveryKey() {
  try {
    let signature: Uint8Array = new Uint8Array(\[0\]);
    let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
    let userId: number = await accountManager.getOsAccountLocalId();
    recoveryKey.deleteEnterpriseRecoveryKey(userId, signature).then((ret: number)=>{
      console.info(\`Succeeded in deleting enterprise recovery key. result is: ${ret}\`);
    }).catch((error: BusinessError)=>{
      console.error(\`Failed to delete enterprise recovery key. Code: ${error.code}, message: ${error.message}\`);
    });
  } catch (e) {
    console.error(\`Failed to deleteEnterpriseRecoveryKey. Code: ${e.code}, message: ${e.message}\`);
  }
}

#### verifyUserIdentityEnterprise

verifyUserIdentityEnterprise(userId: number, userType: number, pinCode: string): Promise<void>

Verifies the identity of an enterprise user. Before exporting the enterprise recovery key to reset the lock screen password, verify the lock screen password first.

**Required permission**: ohos.permission.ENTERPRISE\_RECOVERY\_KEY

**System capability**: SystemCapability.PCService.RecoveryKeyService

**Start version**: 6.0.0(20)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

userId

 | 

number

 | 

Yes

 | 

ID of the user for whom an enterprise recovery key needs to be exported.

 |
| 

userType

 | 

number

 | 

Yes

 | 

[User type](../../../../basic-functions/basic-services-kit/arkts-apis/account-management/ohos-account-osaccount-system-account-management/document.md#osaccounttype). You can call [getOsAccountType](../../../../basic-functions/basic-services-kit/arkts-apis/account-management/ohos-account-osaccount-system-account-management/document.md#getosaccounttype9) to obtain the user type.

 |
| 

pinCode

 | 

string

 | 

Yes

 | 

Lock screen password, which contains a maximum of 64 characters.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<void>

 | 

**Promise** object. No result is returned.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

201

 | 

Permission denied.

 |
| 

1014400001

 | 

System service exception.

 |
| 

1014400103

 | 

Authentication is failed.

 |
| 

1014400201

 | 

Invalid device type, current device is not enterprise device.

 |
| 

1014400202

 | 

Invalid userId.

 |

**Example**:

import { BusinessError, osAccount } from '@kit.BasicServicesKit';

/\*\*
 \* @param pinCode Lock screen password entered by the user.
 \*/
async function verifyUserIdentityEnterprise(pinCode: string) {
  try {
    let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
    let accountType: osAccount.OsAccountType = await accountManager.getOsAccountType();

    let userId: number = await accountManager.getOsAccountLocalId();
    let userType: number = accountType.valueOf();
    recoveryKey.verifyUserIdentityEnterprise(userId, userType, pinCode).then(() => {
      console.info(\`Succeeded in verifying user identity.\`);
    }).catch((error: BusinessError) => {
      console.error(\`Failed to verified user identity. Code: ${error.code}, message: ${error.message}\`);
    })
  } catch (e) {
    console.error(\`Failed to verifyUserIdentityEnterprise. Code: ${e.code}, message: ${e.message}\`);
  }
}

#### getEnterpriseRecoveryKeyForResettingPin

getEnterpriseRecoveryKeyForResettingPin(userId: number, userType: number): Promise<EnterpriseRecoveryKeyInfo>

Exports the enterprise recovery key used to reset the lock screen password. You need to call the [verifyUserIdentityEnterprise](#section1894251193414) API first to verify the user identity and call this API within 30 seconds.

**Required permission**: ohos.permission.ENTERPRISE\_RECOVERY\_KEY

**System capability**: SystemCapability.PCService.RecoveryKeyService

**Start version**: 6.0.0(20)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

userId

 | 

number

 | 

Yes

 | 

ID of the user for whom an enterprise recovery key needs to be exported.

 |
| 

userType

 | 

number

 | 

Yes

 | 

[User type](../../../../basic-functions/basic-services-kit/arkts-apis/account-management/ohos-account-osaccount-system-account-management/document.md#osaccounttype). You can call [getOsAccountType](../../../../basic-functions/basic-services-kit/arkts-apis/account-management/ohos-account-osaccount-system-account-management/document.md#getosaccounttype9) to obtain the user type.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[EnterpriseRecoveryKeyInfo](#en-us_topic_0000001983615174_section35870815206)\>

 | 

Promise object used to return the enterprise recovery key and related encryption parameters.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

201

 | 

Permission denied.

 |
| 

1014400001

 | 

System service exception.

 |
| 

1014400201

 | 

Invalid device type, current device is not enterprise device.

 |
| 

1014400202

 | 

Invalid userId.

 |

**Example**:

import { buffer } from '@kit.ArkTS';
import { BusinessError, osAccount } from '@kit.BasicServicesKit';

async function getEnterpriseRecoveryKeyForResettingPin() {
  try {
    let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
    let accountType: osAccount.OsAccountType = await accountManager.getOsAccountType();

    let userId: number = await accountManager.getOsAccountLocalId();
    let userType: number = accountType.valueOf();
    recoveryKey.getEnterpriseRecoveryKeyForResettingPin(userId, userType)
      .then((info: recoveryKey.EnterpriseRecoveryKeyInfo) => {
        console.info(\`Succeeded in getting enterprise recovery key for resetting pin.\`);
        console.info(\`EnterpriseRecoveryKeyInfo enterpriseRecoveryKey: ${buffer.from(info.enterpriseRecoveryKey)
          .toString('hex')}\`);
        console.info(\`EnterpriseRecoveryKeyInfo exportPublicKey: ${buffer.from(info.exportPublicKey)
          .toString('hex')}\`);
        console.info(\`EnterpriseRecoveryKeyInfo iv: ${buffer.from(info.iv).toString('hex')}\`);
        console.info(\`EnterpriseRecoveryKeyInfo tag: ${buffer.from(info.tag).toString('hex')}\`);
      }).catch((err: BusinessError) => {
      console.error(\`Failed to get enterprise recovery key for resetting pin. Code: ${err.code}, message: ${err.message}\`);
    })
  } catch (e) {
    console.error(\`Failed to getEnterpriseRecoveryKeyForResettingPin. Code: ${e.code}, message: ${e.message}\`);
  }
}
