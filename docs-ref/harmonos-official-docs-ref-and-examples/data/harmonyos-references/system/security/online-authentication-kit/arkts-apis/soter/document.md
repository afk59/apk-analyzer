# SOTER

SOTER enables passwordless identity authentication on mobile devices, so that apps complying with the SOTER standard can support service scenarios such as passwordless sign-in and payment.

The supported device types are phones, 2-in-1 devices, and tablets.

**Start version**: 5.0.0(12)

#### Module Import

import { soter } from '@kit.OnlineAuthenticationKit'

#### KeyType

Key type. The value is an enumerated value.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Security.SOTER

**Start version**: 5.0.0(12)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

ECC\_P256

 | 

0

 | 

The key type is ECC P256.

 |

#### SignedResult

Signature result.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Security.SOTER

**Start version**: 5.0.0(12)

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

message

 | 

Uint8Array

 | 

Yes

 | 

Original message.

 |
| 

signature

 | 

Uint8Array

 | 

Yes

 | 

Signature of the original message.

 |
| 

saltLength

 | 

number

 | 

Yes

 | 

Salt length, which is less than the maximum value of the U32 type.

 |

#### getVersionSync

getVersionSync(): string

Obtains the version number of the SOTER passwordless authentication API and returns the result synchronously.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Security.SOTER

**Start version**: 5.0.0(12)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

string

 | 

Version number of the SOTER passwordless authentication API. The value contains a maximum of 64 characters.

 |

**Error codes**:

For details about the error codes, please refer to [SOTER](../arkts-api-error-codes/soter/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

801

 | 

Device type error.

 |
| 

1014500001

 | 

The service is abnormal.

 |

**Example**:

let res: string = soter.getVersionSync();// Process the result.

#### getVersion

getVersion(): Promise<string>

Obtains the version number of the SOTER passwordless authentication API and returns the result asynchronously through a promise.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Security.SOTER

**Start version**: 5.0.0(12)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<string>

 | 

Version number of the SOTER passwordless authentication API, which is returned through a promise. The value contains a maximum of 64 characters.

 |

**Error codes**:

For details about the error codes, please refer to [SOTER](../arkts-api-error-codes/soter/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

801

 | 

Device type error.

 |
| 

1014500001

 | 

The service is abnormal.

 |

**Example**:

import { BusinessError } from '@kit.BasicServicesKit';

let resPromise: Promise<string> = soter.getVersion();
resPromise.then(result => {
  console.info('Succeeded in doing getVersion.');
  // Process the result.
}).catch((error: BusinessError) => {
  console.error(\`Failed to call getVersion. Code: ${error.code}, message: ${error.message}\`);
});

#### hasAppSecureKeySync

hasAppSecureKeySync(keyType: KeyType): boolean

Queries the app secure key generation status and returns the result synchronously.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Security.SOTER

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

keyType

 | 

[KeyType](#section186410451429)

 | 

Yes

 | 

Key type. Currently, only **soter.KeyType.ECC\_P256** is supported.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

boolean

 | 

Indicates whether an app secure key is generated, which is returned synchronously. The value **true** indicates yes, and the value **false** indicates no.

 |

**Error codes**:

For details about the error codes, please refer to [SOTER](../arkts-api-error-codes/soter/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Parameter error. Possible causes:

1\. Mandatory parameters are left unspecified.

2\. Parameter verification failed.

 |
| 

801

 | 

Device type error.

 |
| 

1014500001

 | 

The service is abnormal.

 |

**Example**:

let keyType: soter.KeyType = soter.KeyType.ECC\_P256; // Key type. Currently, only ECC\_P256 is supported.

// Query the app secure key generation status. The result is returned synchronously.
let hasAppSecureKey: boolean = soter.hasAppSecureKeySync(keyType);

#### hasAppSecureKey

hasAppSecureKey(keyType: KeyType): Promise<boolean>

Queries the app secure key generation status. This API returns the result asynchronously through a promise.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Security.SOTER

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

keyType

 | 

[KeyType](#section186410451429)

 | 

Yes

 | 

Key type. Currently, only **soter.KeyType.ECC\_P256** is supported.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<boolean>

 | 

Indicates whether an app secure key is generated. The result is returned through a promise. The value **true** indicates yes, and the value **false** indicates no.

 |

**Error codes**:

For details about the error codes, please refer to [SOTER](../arkts-api-error-codes/soter/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Parameter error. Possible causes:

1\. Mandatory parameters are left unspecified.

2\. Parameter verification failed.

 |
| 

801

 | 

Device type error.

 |
| 

1014500001

 | 

The service is abnormal.

 |

**Example**:

import { BusinessError } from '@kit.BasicServicesKit';

let keyType: soter.KeyType = soter.KeyType.ECC\_P256; // Key type. Currently, only ECC\_P256 is supported.

// Query the app secure key generation status. The result is returned asynchronously.
let hasAppSecureKeyPromise: Promise<boolean> = soter.hasAppSecureKey(keyType);
hasAppSecureKeyPromise.then(result => {
  console.info('Succeeded in doing hasAppSecureKey.');
  // Process the result.
}).catch((error: BusinessError) => {
  console.error(\`Failed to call hasAppSecureKey. Code: ${error.code}, message: ${error.message}\`);
});

#### generateAppSecureKeySync

generateAppSecureKeySync(keyType: KeyType): Uint8Array

Generates an app secure key and returns the result synchronously.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Security.SOTER

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

keyType

 | 

[KeyType](#section186410451429)

 | 

Yes

 | 

Key type. Currently, only **soter.KeyType.ECC\_P256** is supported.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Uint8Array

 | 

App secret.

 |

**Error codes**:

For details about the error codes, please refer to [SOTER](../arkts-api-error-codes/soter/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Parameter error. Possible causes:

1\. Mandatory parameters are left unspecified.

2\. Parameter verification failed.

 |
| 

801

 | 

Device type error.

 |
| 

1014500001

 | 

The service is abnormal.

 |

**Example**:

let keyType: soter.KeyType = soter.KeyType.ECC\_P256; // Key type. Currently, only ECC\_P256 is supported.

// Generate an app secure key.
let appSecureKey: Uint8Array = soter.generateAppSecureKeySync(keyType);

#### generateAppSecureKey

generateAppSecureKey(keyType: KeyType): Promise<Uint8Array>

Generates an app secure key. This API returns the result asynchronously through a promise.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Security.SOTER

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

keyType

 | 

[KeyType](#section186410451429)

 | 

Yes

 | 

Key type. Currently, only **soter.KeyType.ECC\_P256** is supported. An error will be reported if other enumerated values are used.

 |

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

App secure key, which is returned through a promise.

 |

**Error codes**:

For details about the error codes, please refer to [SOTER](../arkts-api-error-codes/soter/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Parameter error. Possible causes:

1\. Mandatory parameters are left unspecified.

2\. Parameter verification failed.

 |
| 

801

 | 

Device type error.

 |
| 

1014500001

 | 

The service is abnormal.

 |

**Example**:

import { BusinessError } from '@kit.BasicServicesKit';

let keyType: soter.KeyType = soter.KeyType.ECC\_P256; // Key type. Currently, only ECC\_P256 is supported.

// Generate an app secure key.
let appSecureKeyPromise: Promise<Uint8Array> = soter.generateAppSecureKey(keyType);
appSecureKeyPromise.then(result => {
  console.info('Succeeded in doing generateAppSecureKey.');
  // Process the result.
}).catch((error: BusinessError) => {
  console.error(\`Failed to call generateAppSecureKey. Code: ${error.code}, message: ${error.message}\`);
});

#### getAppSecureKeySync

getAppSecureKeySync(keyType: KeyType): Uint8Array

Obtains an app secure key and returns the result synchronously.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Security.SOTER

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

keyType

 | 

[KeyType](#section186410451429)

 | 

Yes

 | 

Key type. Currently, only **soter.KeyType.ECC\_P256** is supported.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Uint8Array

 | 

App secret.

 |

**Error codes**:

For details about the error codes, please refer to [SOTER](../arkts-api-error-codes/soter/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Parameter error. Possible causes:

1\. Mandatory parameters are left unspecified.

2\. Parameter verification failed.

 |
| 

801

 | 

Device type error.

 |
| 

1014500001

 | 

The service is abnormal.

 |

**Example**:

let keyType: soter.KeyType = soter.KeyType.ECC\_P256; // Key type. Currently, only ECC\_P256 is supported.

// Obtain the app secure key. The result is returned synchronously.
let appSecureKey: Uint8Array = soter.getAppSecureKeySync(keyType);

#### getAppSecureKey

getAppSecureKey(keyType: KeyType): Promise<Uint8Array>

Obtains an app secure key. This API returns the result asynchronously through a promise.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Security.SOTER

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

keyType

 | 

[KeyType](#section186410451429)

 | 

Yes

 | 

Key type. Currently, only **soter.KeyType.ECC\_P256** is supported.

 |

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

App secure key, which is returned through a promise.

 |

**Error codes**:

For details about the error codes, please refer to [SOTER](../arkts-api-error-codes/soter/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Parameter error. Possible causes:

1\. Mandatory parameters are left unspecified.

2\. Parameter verification failed.

 |
| 

801

 | 

Device type error.

 |
| 

1014500001

 | 

The service is abnormal.

 |

**Example**:

import { BusinessError } from '@kit.BasicServicesKit';

let keyType: soter.KeyType = soter.KeyType.ECC\_P256; // Key type. Currently, only ECC\_P256 is supported.

// Obtain the app secure key. The result is returned through a promise.
let appSecureKeyPromise: Promise<Uint8Array> = soter.getAppSecureKey(keyType);
appSecureKeyPromise.then(result => {
  console.info('Succeeded in doing getAppSecureKey.');
  // Process the result.
}).catch((error: BusinessError) => {
  console.error(\`Failed to call getAppSecureKey. Code: ${error.code}, message: ${error.message}\`);
});

#### hasAuthKeySync

hasAuthKeySync(keyAlias: string, keyType: KeyType): boolean

Queries the authentication key generation status and returns the result synchronously.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Security.SOTER

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

keyAlias

 | 

string

 | 

Yes

 | 

Key alias, which can contain 1 to 31 characters. You can customize this parameter by yourself. The value can contain characters a-z, A-Z, 0-9, hyphens (-), and underlines (\_). The hyphen or underline cannot be the first character in the value.

 |
| 

keyType

 | 

[KeyType](#section186410451429)

 | 

Yes

 | 

Key type. Currently, only **soter.KeyType.ECC\_P256** is supported.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

boolean

 | 

Indicates whether an authentication key is generated, which is returned synchronously. The value **true** indicates yes, and the value **false** indicates no.

 |

**Error codes**:

For details about the error codes, please refer to [SOTER](../arkts-api-error-codes/soter/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Parameter error. Possible causes:

1\. Mandatory parameters are left unspecified.

2\. Parameter verification failed.

 |
| 

801

 | 

Device type error.

 |
| 

1014500001

 | 

The service is abnormal.

 |

**Example**:

let keyType: soter.KeyType = soter.KeyType.ECC\_P256; // Key type. Currently, only ECC\_P256 is supported.
let keyAlias: string = 'keyAlias'; // Key alias. Customize this parameter by yourself.

// Query the authentication key generation status. The result is returned synchronously.
let hasAuthKey: boolean = soter.hasAuthKeySync(keyAlias, keyType);

#### hasAuthKey

hasAuthKey(keyAlias: string, keyType: KeyType): Promise<boolean>

Queries the authentication key generation status. This API returns the result asynchronously through a promise.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Security.SOTER

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

keyAlias

 | 

string

 | 

Yes

 | 

Key alias, which can contain 1 to 31 characters. You can customize this parameter by yourself. The value can contain characters a-z, A-Z, 0-9, hyphens (-), and underlines (\_). The hyphen or underline cannot be the first character in the value.

 |
| 

keyType

 | 

[KeyType](#section186410451429)

 | 

Yes

 | 

Key type. Currently, only **soter.KeyType.ECC\_P256** is supported.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<boolean>

 | 

Indicates whether an authentication key is generated, which is returned through a promise. The value **true** indicates yes, and the value **false** indicates no.

 |

**Error codes**:

For details about the error codes, please refer to [SOTER](../arkts-api-error-codes/soter/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Parameter error. Possible causes:

1\. Mandatory parameters are left unspecified.

2\. Parameter verification failed.

 |
| 

801

 | 

Device type error.

 |
| 

1014500001

 | 

The service is abnormal.

 |

**Example**:

import { BusinessError } from '@kit.BasicServicesKit';

let keyType: soter.KeyType = soter.KeyType.ECC\_P256; // Key type. Currently, only ECC\_P256 is supported.
let keyAlias: string = 'keyAlias';

// Query the authentication key generation status. The result is returned through a promise.
let hasAuthKeyPromise: Promise<boolean> = soter.hasAuthKey(keyAlias, keyType);
hasAuthKeyPromise.then(result => {
  console.info('Succeeded in doing hasAuthKey.');
  // Process the result.
}).catch((error: BusinessError) => {
  console.error(\`Failed to call hasAuthKey. Code: ${error.code}, message: ${error.message}\`);
});

#### generateAuthKeySync

generateAuthKeySync(keyAlias: string, keyType: KeyType): SignedResult

Generates an authentication key and returns the result synchronously.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Security.SOTER

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

keyAlias

 | 

string

 | 

Yes

 | 

Key alias, which can contain 1 to 31 characters. You can customize this parameter by yourself. The value can contain characters a-z, A-Z, 0-9, hyphens (-), and underlines (\_). The hyphen or underline cannot be the first character in the value.

 |
| 

keyType

 | 

[KeyType](#section186410451429)

 | 

Yes

 | 

Key type. Currently, only **soter.KeyType.ECC\_P256** is supported.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[SignedResult](#section13572542154913)

 | 

**SignedResult** object. In the object, **signature** indicates the signature of the message, **message** indicates the original content of the message, and **saltLength** indicates the length of the cryptographic salt used.

 |

**Error codes**:

For details about the error codes, please refer to [SOTER](../arkts-api-error-codes/soter/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Parameter error. Possible causes:

1\. Mandatory parameters are left unspecified.

2\. Parameter verification failed.

 |
| 

801

 | 

Device type error.

 |
| 

1014500001

 | 

The service is abnormal.

 |

**Example**:

let keyType: soter.KeyType = soter.KeyType.ECC\_P256; // Key type. Currently, only ECC\_P256 is supported.
let keyAlias: string = 'keyAlias';

// Generate an authentication key.
let signedResult: soter.SignedResult = soter.generateAuthKeySync(keyAlias, keyType);
let authKey: Uint8Array = signedResult?.signature; // Use the result.

#### generateAuthKey

generateAuthKey(keyAlias: string, keyType: KeyType): Promise<SignedResult>

Generates an authentication key. This API returns the result asynchronously through a promise.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Security.SOTER

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

keyAlias

 | 

string

 | 

Yes

 | 

Key alias, which can contain 1 to 31 characters. You can customize this parameter by yourself. The value can contain characters a-z, A-Z, 0-9, hyphens (-), and underlines (\_). The hyphen or underline cannot be the first character in the value.

 |
| 

keyType

 | 

[KeyType](#section186410451429)

 | 

Yes

 | 

Key type. Currently, only **soter.KeyType.ECC\_P256** is supported.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[SignedResult](#section13572542154913)\>

 | 

**SignedResult** object returned through a promise. In the object, **signature** indicates the signature of the message, **message** indicates the original content of the message, and **saltLength** indicates the length of the cryptographic salt used.

 |

**Error codes**:

For details about the error codes, please refer to [SOTER](../arkts-api-error-codes/soter/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Parameter error. Possible causes:

1\. Mandatory parameters are left unspecified.

2\. Parameter verification failed.

 |
| 

801

 | 

Device type error.

 |
| 

1014500001

 | 

The service is abnormal.

 |

**Example**:

import { BusinessError } from '@kit.BasicServicesKit';

let keyType: soter.KeyType = soter.KeyType.ECC\_P256; // Key type. Currently, only ECC\_P256 is supported.
let keyAlias: string = 'keyAlias';

// Generate an authentication key.
let authKeyPromise: Promise<soter.SignedResult> = soter.generateAuthKey(keyAlias, keyType);
authKeyPromise.then(result => {
  console.info('Succeeded in doing generateAuthKey.');
  // Process the result.
}).catch((error: BusinessError) => {
   console.error(\`Failed to call generateAuthKey. Code: ${error.code}, message: ${error.message}\`);
});

#### getAuthKeySync

getAuthKeySync(keyAlias: string, keyType: KeyType): SignedResult

Obtains an authentication key and returns the result synchronously.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Security.SOTER

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

keyAlias

 | 

string

 | 

Yes

 | 

Key alias, which can contain 1 to 31 characters. You can customize this parameter by yourself. The value can contain characters a-z, A-Z, 0-9, hyphens (-), and underlines (\_). The hyphen or underline cannot be the first character in the value.

 |
| 

keyType

 | 

[KeyType](#section186410451429)

 | 

Yes

 | 

Key type. Currently, only **soter.KeyType.ECC\_P256** is supported.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[SignedResult](#section13572542154913)

 | 

**SignedResult** object. In the object, **signature** indicates the signature of the message, **message** indicates the original content of the message, and **saltLength** indicates the length of the cryptographic salt used.

 |

**Error codes**:

For details about the error codes, please refer to [SOTER](../arkts-api-error-codes/soter/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Parameter error. Possible causes:

1\. Mandatory parameters are left unspecified.

2\. Parameter verification failed.

 |
| 

801

 | 

Device type error.

 |
| 

1014500001

 | 

The service is abnormal.

 |

**Example**:

let keyType: soter.KeyType = soter.KeyType.ECC\_P256; // Key type. Currently, only ECC\_P256 is supported.
let keyAlias: string = 'keyAlias';

// Obtain the authentication key. The result is returned synchronously.
let signedResult: soter.SignedResult = soter.getAuthKeySync(keyAlias, keyType);
let authKey: Uint8Array = signedResult.message; // Use the result.

#### getAuthKey

getAuthKey(keyAlias: string, keyType: KeyType): Promise<SignedResult>

Obtains an authentication key. This API returns the result asynchronously through a promise.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Security.SOTER

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

keyAlias

 | 

string

 | 

Yes

 | 

Key alias, which can contain 1 to 31 characters. You can customize this parameter by yourself. The value can contain characters a-z, A-Z, 0-9, hyphens (-), and underlines (\_). The hyphen or underline cannot be the first character in the value.

 |
| 

keyType

 | 

[KeyType](#section186410451429)

 | 

Yes

 | 

Key type. Currently, only **soter.KeyType.ECC\_P256** is supported.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[SignedResult](#section13572542154913)\>

 | 

**SignedResult** object returned through a promise. In the object, **signature** indicates the signature of the message, **message** indicates the original content of the message, and **saltLength** indicates the length of the cryptographic salt used.

 |

**Error codes**:

For details about the error codes, please refer to [SOTER](../arkts-api-error-codes/soter/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Parameter error. Possible causes:

1\. Mandatory parameters are left unspecified.

2\. Parameter verification failed.

 |
| 

801

 | 

Device type error.

 |
| 

1014500001

 | 

The service is abnormal.

 |

**Example**:

import { BusinessError } from '@kit.BasicServicesKit';

let keyType: soter.KeyType = soter.KeyType.ECC\_P256; // Key type. Currently, only ECC\_P256 is supported.
let keyAlias: string = 'keyAlias';

// Obtain the authentication key. The result is returned through a promise.
let authKeyPromise: Promise<soter.SignedResult> = soter.getAuthKey(keyAlias, keyType);
authKeyPromise.then(result => {
  console.info('Succeeded in doing getAuthKey.');
  // Process the result.
}).catch((error: BusinessError) => {
  console.error(\`Failed to call getAuthKey. Code: ${error.code}, message: ${error.message}\`);
});

#### generateChallengeSync

generateChallengeSync(keyAlias: string): Uint8Array

Generates a challenge and returns the result synchronously.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Security.SOTER

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

keyAlias

 | 

string

 | 

Yes

 | 

Key alias, which can contain 1 to 31 characters. You can customize this parameter by yourself. The value can contain characters a-z, A-Z, 0-9, hyphens (-), and underlines (\_). The hyphen or underline cannot be the first character in the value.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Uint8Array

 | 

Generated challenge.

 |

**Error codes**:

For details about the error codes, please refer to [SOTER](../arkts-api-error-codes/soter/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Parameter error. Possible causes:

1\. Mandatory parameters are left unspecified.

2\. Parameter verification failed.

 |
| 

801

 | 

Device type error.

 |
| 

1014500001

 | 

The service is abnormal.

 |

**Example**:

let keyAlias: string = 'keyAlias';

// Generate a challenge.
let challenge: Uint8Array = soter.generateChallengeSync(keyAlias);

#### generateChallenge

generateChallenge(keyAlias: string): Promise<Uint8Array>

Generates a challenge. This API returns the result asynchronously through a promise.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Security.SOTER

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

keyAlias

 | 

string

 | 

Yes

 | 

Key alias, which can contain 1 to 31 characters. You can customize this parameter by yourself. The value can contain characters a-z, A-Z, 0-9, hyphens (-), and underlines (\_). The hyphen or underline cannot be the first character in the value.

 |

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

Generated challenge, which is returned through a promise.

 |

**Error codes**:

For details about the error codes, please refer to [SOTER](../arkts-api-error-codes/soter/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Parameter error. Possible causes:

1\. Mandatory parameters are left unspecified.

2\. Parameter verification failed.

 |
| 

801

 | 

Device type error.

 |
| 

1014500001

 | 

The service is abnormal.

 |

**Example**:

import { BusinessError } from '@kit.BasicServicesKit';

let keyAlias: string = 'keyAlias';

// Generate a challenge.
let challengePromise: Promise<Uint8Array> = soter.generateChallenge(keyAlias);
challengePromise.then(result => {
  console.info('Succeeded in doing generateChallenge.');
  // Process the result.
}).catch((error: BusinessError) => {
  console.error(\`Failed to call generateChallenge. Code: ${error.code}, message: ${error.message}\`);
});

#### signWithAuthKeySync

signWithAuthKeySync(keyAlias: string, authToken: Uint8Array, info: string): SignedResult

Performs SOTER passwordless authentication and returns the signed message synchronously.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Security.SOTER

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

keyAlias

 | 

string

 | 

Yes

 | 

Key alias, which can contain 1 to 31 characters. You can customize this parameter by yourself. The value can contain characters a-z, A-Z, 0-9, hyphens (-), and underlines (\_). The hyphen or underline cannot be the first character in the value.

 |
| 

authToken

 | 

Uint8Array

 | 

Yes

 | 

Credential proving that a user passes the authentication. (Obtain this credential by calling the **getUserAuthInstance** API of the **@ohos.userIAM.userAuth** module.)

 |
| 

info

 | 

string

 | 

Yes

 | 

Customized information, which can contain a maximum of 511 characters.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[SignedResult](#section13572542154913)

 | 

**SignedResult** object. In the object, **signature** indicates the signature of the message, **message** indicates the original content of the message, and **saltLength** indicates the length of the cryptographic salt used.

 |

**Error codes**:

For details about the error codes, please refer to [SOTER](../arkts-api-error-codes/soter/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Parameter error. Possible causes:

1\. Mandatory parameters are left unspecified.

2\. Parameter verification failed.

 |
| 

801

 | 

Device type error.

 |
| 

1014500001

 | 

The service is abnormal.

 |

**Example**:

let keyAlias: string = 'keyAlias';
// Call **getUserAuthInstance** of **@ohos.userIAM.userAuth** to obtain the value of **authToken**. Replace the **authToken** value here with an actual value.
let authToken = new Uint8Array(\[0\]);
let info = '';
let authResult: soter.SignedResult = soter.signWithAuthKeySync(keyAlias, authToken, info)

#### signWithAuthKey

signWithAuthKey(keyAlias: string, authToken: Uint8Array, info: string): Promise<SignedResult>

Performs SOTER passwordless authentication and returns the signed message asynchronously through a promise.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Security.SOTER

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

keyAlias

 | 

string

 | 

Yes

 | 

Key alias, which can contain 1 to 31 characters. You can customize this parameter by yourself. The value can contain characters a-z, A-Z, 0-9, hyphens (-), and underlines (\_). The hyphen or underline cannot be the first character in the value.

 |
| 

authToken

 | 

Uint8Array

 | 

Yes

 | 

Credential proving that a user passes the authentication. (Obtain this credential by calling the **getUserAuthInstance** API of the **@ohos.userIAM.userAuth** module.)

 |
| 

info

 | 

string

 | 

Yes

 | 

Customized information, which can contain a maximum of 511 characters.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[SignedResult](#section13572542154913)\>

 | 

**SignedResult** object returned through a promise. In the object, **signature** indicates the signature of the message, **message** indicates the original content of the message, and **saltLength** indicates the length of the cryptographic salt used.

 |

**Error codes**:

For details about the error codes, please refer to [SOTER](../arkts-api-error-codes/soter/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Parameter error. Possible causes:

1\. Mandatory parameters are left unspecified.

2\. Parameter verification failed.

 |
| 

801

 | 

Device type error.

 |
| 

1014500001

 | 

The service is abnormal.

 |

**Example**:

import { BusinessError } from '@kit.BasicServicesKit';

let keyAlias: string = 'keyAlias';
// Call **getUserAuthInstance** of **@ohos.userIAM.userAuth** to obtain the value of **authToken**. Replace the **authToken** value here with an actual value.
let authToken = new Uint8Array(\[0\]);
let info = '';
let authResultPromise: Promise<soter.SignedResult> = soter.signWithAuthKey(keyAlias, authToken, info);
authResultPromise.then(result => {
  console.info('Succeeded in doing signWithAuthKey.');
  // Process the result.
}).catch((error: BusinessError) => {
  console.error(\`Failed to call signWithAuthKey. Code: ${error.code}, message: ${error.message}\`);
});

#### deleteAuthKeySync

deleteAuthKeySync(keyAlias: string): void

Deletes an authentication key.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Security.SOTER

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

keyAlias

 | 

string

 | 

Yes

 | 

Key alias, which can contain 1 to 31 characters. You can customize this parameter by yourself. The value can contain characters a-z, A-Z, 0-9, hyphens (-), and underlines (\_). The hyphen or underline cannot be the first character in the value.

 |

**Error codes**:

For details about the error codes, please refer to [SOTER](../arkts-api-error-codes/soter/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Parameter error. Possible causes:

1\. Mandatory parameters are left unspecified.

2\. Parameter verification failed.

 |
| 

801

 | 

Device type error.

 |
| 

1014500001

 | 

The service is abnormal.

 |

**Example**:

// Delete an authentication key.
let keyAlias: string = 'keyAlias';
soter.deleteAuthKeySync(keyAlias);

#### deleteAuthKey

deleteAuthKey(keyAlias: string): Promise<void>

Deletes an authentication key. This API returns the result asynchronously through a promise.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Security.SOTER

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

keyAlias

 | 

string

 | 

Yes

 | 

Key alias, which can contain 1 to 31 characters. You can customize this parameter by yourself. The value can contain characters a-z, A-Z, 0-9, hyphens (-), and underlines (\_). The hyphen or underline cannot be the first character in the value.

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

Promise that returns no value.

 |

**Error codes**:

For details about the error codes, please refer to [SOTER](../arkts-api-error-codes/soter/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Parameter error. Possible causes:

1\. Mandatory parameters are left unspecified.

2\. Parameter verification failed.

 |
| 

801

 | 

Device type error.

 |
| 

1014500001

 | 

The service is abnormal.

 |

**Example**:

import { BusinessError } from '@kit.BasicServicesKit';

let keyAlias: string = 'keyAlias';
// Delete an authentication key.
let delPromise: Promise<void> = soter.deleteAuthKey(keyAlias);
delPromise.then(() => {
  console.info('Succeeded in doing deleteAuthKey.');
}).catch((error: BusinessError) => {
  console.error(\`Failed to call deleteAuthKey. Code: ${error.code}, message: ${error.message}\`);
});

#### deleteAppSecureKeySync

deleteAppSecureKeySync(): void

Deletes an app secure key and returns the result synchronously.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Security.SOTER

**Start version**: 5.0.0(12)

**Error codes**:

For details about the error codes, please refer to [SOTER](../arkts-api-error-codes/soter/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

801

 | 

Device type error.

 |
| 

1014500001

 | 

The service is abnormal.

 |

**Example**:

// Delete an app secure key.
soter.deleteAppSecureKeySync();

#### deleteAppSecureKey

deleteAppSecureKey(): Promise<void>

Deletes an app secure key. This API returns the result asynchronously through a promise.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Security.SOTER

**Start version**: 5.0.0(12)

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

For details about the error codes, please refer to [SOTER](../arkts-api-error-codes/soter/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

801

 | 

Device type error.

 |
| 

1014500001

 | 

The service is abnormal.

 |

**Example**:

import { BusinessError } from '@kit.BasicServicesKit';

// Delete an app secure key.
let delAppSecureKeyPromise: Promise<void> = soter.deleteAppSecureKey();
delAppSecureKeyPromise.then(() => {
  console.info('Succeeded in doing deleteAppSecureKey.');
}).catch((error: BusinessError) => {
  console.error(\`Failed to call deleteAppSecureKey. Code: ${error.code}, message: ${error.message}\`);
});
