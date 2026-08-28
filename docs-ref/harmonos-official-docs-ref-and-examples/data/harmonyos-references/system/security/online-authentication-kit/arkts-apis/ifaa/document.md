# IFAA

IFAA provides the passwordless identity authentication capability for mobile devices to implement passwordless sign-in, passwordless payment, and other IIFAA-compliant services. (Note: In this document, we use "IFAA" to refer to the passwordless authentication module of the HarmonyOS system, and "IIFAA" to refer to the International Internet Finance Authentication Alliance and related technical specifications.)

The supported device types are phones, 2-in-1 devices, and tablets.

**Start version**: 4.1.0(11)

#### Module Import

import { ifaa } from '@kit.OnlineAuthenticationKit'

#### getVersionSync

getVersionSync(): number

Obtains the version number of the IFAA passwordless authentication API and returns the result synchronously.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Security.Ifaa

**Start version**: 4.1.0(11)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

number

 | 

Version number of the IFAA passwordless authentication API.

 |

**Error codes**:

For details about the error codes, please refer to [IFAA](../arkts-api-error-codes/ifaa/document.md).

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

**Example**:

let res: number = ifaa.getVersionSync();
// Process **res**.

#### getAnonymousIdSync

getAnonymousIdSync(userToken: Uint8Array): Uint8Array

Obtains the anonymous ID for IFAA passwordless authentication and returns the result synchronously.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Security.Ifaa

**Start version**: 4.1.0(11)

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

userToken

 | 

Uint8Array

 | 

Yes

 | 

ID that uniquely identifies a user.

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

Anonymous ID for IFAA passwordless authentication.

 |

**Error codes**:

For details about the error codes, please refer to [IFAA](../arkts-api-error-codes/ifaa/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Parameter error.

 |
| 

801

 | 

Device type error.

 |
| 

1006100001

 | 

System Interruption.

 |
| 

1006100002

 | 

The service is abnormal.

 |

**Example**:

// Construct an input parameter based on the TLV format of IIFAA and convert it into a Uint8Array parameter. Here, the **arg** value needs to be replaced with the actual input parameter.
let arg = new Uint8Array(\[0\]);
let getAnonIdResult: Uint8Array = ifaa.getAnonymousIdSync(arg);
// Process **getAnonIdResult**.

#### getAnonymousId

getAnonymousId(userToken: Uint8Array): Promise<Uint8Array>

Obtains the anonymous ID for IFAA passwordless authentication. This API returns the result asynchronously through a promise.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Security.Ifaa

**Start version**: 4.1.0(11)

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

userToken

 | 

Uint8Array

 | 

Yes

 | 

ID that uniquely identifies a user.

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

Anonymous ID returned through a promise.

 |

**Error codes**:

For details about the error codes, please refer to [IFAA](../arkts-api-error-codes/ifaa/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Parameter error.

 |
| 

801

 | 

Device type error.

 |
| 

1006100001

 | 

System Interruption.

 |
| 

1006100002

 | 

The service is abnormal.

 |

**Example**:

import { BusinessError } from '@kit.BasicServicesKit';

// Construct an input parameter based on the TLV format of IIFAA and convert it into a Uint8Array parameter. Here, the **arg** value needs to be replaced with the actual input parameter.
let arg = new Uint8Array(\[0\]);
let getAnonIdPromise: Promise<Uint8Array> = ifaa.getAnonymousId(arg);
getAnonIdPromise.then(result => {
  console.info("Succeeded in doing getAnonymousId.");
  // Process **result**.
}).catch((err: BusinessError) => {
  console.error(\`Failed to call getAnonymousId. Code: ${err.code}, message: ${err.message}\`);
 });

#### getAnonymousId

getAnonymousId(userToken: Uint8Array, callback: AsyncCallback<Uint8Array>): void

Obtains the anonymous ID for IFAA passwordless authentication. This API returns the result asynchronously through a callback.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Security.Ifaa

**Start version**: 4.1.0(11)

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

userToken

 | 

Uint8Array

 | 

Yes

 | 

ID that uniquely identifies a user.

 |
| 

callback

 | 

AsyncCallback<Uint8Array>

 | 

Yes

 | 

Callback function used to obtain returned data.

 |

**Error codes**:

For details about the error codes, please refer to [IFAA](../arkts-api-error-codes/ifaa/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Parameter error.

 |
| 

801

 | 

Device type error.

 |
| 

1006100001

 | 

System Interruption.

 |
| 

1006100002

 | 

The service is abnormal.

 |

**Example**:

import { BusinessError } from '@kit.BasicServicesKit';

// Construct an input parameter based on the TLV format of IIFAA and convert it into a Uint8Array parameter. Here, the **arg** value needs to be replaced with the actual input parameter.
let arg = new Uint8Array(\[0\]);
ifaa.getAnonymousId(arg,
  (err: BusinessError, result: Uint8Array) => {
    if (err) {
      console.error(\`Failed to call getAnonymousId. Code: ${err.code}, message: ${err.message}\`);
    } else {
      console.info("Succeeded in doing getAnonymousId.");
      // Process **result**.
    }
  });

#### queryStatusSync

queryStatusSync(userToken: Uint8Array): boolean

Obtains the status of IFAA passwordless authentication and returns the result synchronously.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Security.Ifaa

**Start version**: 4.1.0(11)

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

userToken

 | 

Uint8Array

 | 

Yes

 | 

ID that uniquely identifies a user.

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

Indicates whether IFAA passwordless authentication is enabled. The value **true** indicates yes, and the value **false** indicates no.

 |

**Error codes**:

For details about the error codes, please refer to [IFAA](../arkts-api-error-codes/ifaa/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Parameter error.

 |
| 

801

 | 

Device type error.

 |
| 

1006100001

 | 

System Interruption.

 |
| 

1006100002

 | 

The service is abnormal.

 |

**Example**:

// Construct an input parameter based on the TLV format of IIFAA and convert it into a Uint8Array parameter. Here, the **arg** value needs to be replaced with the actual input parameter.
let arg = new Uint8Array(\[0\]);
let status: boolean = ifaa.queryStatusSync(arg);
if (status) {
  console.info("ifaa registered");
} else {
  console.info("ifaa deregistered");
}

#### queryStatus

queryStatus(userToken: Uint8Array): Promise<boolean>

Obtains the status of IFAA passwordless authentication. This API returns the result asynchronously through a promise.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Security.Ifaa

**Start version**: 4.1.0(11)

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

userToken

 | 

Uint8Array

 | 

Yes

 | 

ID that uniquely identifies a user.

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

Promise object, which indicates whether IFAA passwordless authentication is enabled. The value **true** indicates yes, and the value **false** indicates no.

 |

**Error codes**:

For details about the error codes, please refer to [IFAA](../arkts-api-error-codes/ifaa/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Parameter error.

 |
| 

801

 | 

Device type error.

 |
| 

1006100001

 | 

System Interruption.

 |
| 

1006100002

 | 

The service is abnormal.

 |

**Example**:

import { BusinessError } from '@kit.BasicServicesKit';

// Construct an input parameter based on the TLV format of IIFAA and convert it into a Uint8Array parameter. Here, the **arg** value needs to be replaced with the actual input parameter.
let arg = new Uint8Array(\[0\]);
let promise: Promise<boolean> = ifaa.queryStatus(arg);
promise.then(result => {
  console.info("Succeeded in doing queryStatus.");
  // Process **result**.
}).catch((err: BusinessError) => {
  console.error(\`Failed to call queryStatus. Code: ${err.code}, message: ${err.message}\`);
});

#### queryStatus

queryStatus(userToken: Uint8Array, callback: AsyncCallback<boolean>): void

Obtains the status of IFAA passwordless authentication. This API returns the result asynchronously through a callback.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Security.Ifaa

**Start version**: 4.1.0(11)

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

userToken

 | 

Uint8Array

 | 

Yes

 | 

ID that uniquely identifies a user.

 |
| 

callback

 | 

AsyncCallback<boolean>

 | 

Yes

 | 

Callback function used to obtain the status of IFAA passwordless authentication. The value **true** indicates yes, and the value **false** indicates no.

 |

**Error codes**:

For details about the error codes, please refer to [IFAA](../arkts-api-error-codes/ifaa/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Parameter error.

 |
| 

801

 | 

Device type error.

 |
| 

1006100001

 | 

System Interruption.

 |
| 

1006100002

 | 

The service is abnormal.

 |

**Example**:

import { BusinessError } from '@kit.BasicServicesKit';

// Construct an input parameter based on the TLV format of IIFAA and convert it into a Uint8Array parameter. Here, the **arg** value needs to be replaced with the actual input parameter.
let arg = new Uint8Array(\[0\]);
ifaa.queryStatus(arg,
  (err: BusinessError, result: boolean) => {
    if (err) {
      console.error(\`Failed to call queryStatus. Code: ${err.code}, message: ${err.message}\`);
    } else {
      console.info("Succeeded in doing queryStatus.");
      // Process **result**.
    }
  });

#### register

register(registerData: Uint8Array): Promise<Uint8Array>

Enables IFAA passwordless authentication. This API returns the result asynchronously through a promise.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Security.Ifaa

**Start version**: 4.1.0(11)

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

registerData

 | 

Uint8Array

 | 

Yes

 | 

Registration data in TLV format, which is delivered by the IIFAA server.

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

Registration data returned through a promise.

 |

**Error codes**:

For details about the error codes, please refer to [IFAA](../arkts-api-error-codes/ifaa/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Parameter error.

 |
| 

801

 | 

Device type error.

 |
| 

1006100001

 | 

System Interruption.

 |
| 

1006100002

 | 

The service is abnormal.

 |

**Example**:

import { BusinessError } from '@kit.BasicServicesKit';

// Construct an input parameter based on the TLV format of IIFAA and convert it into a Uint8Array parameter. Here, the **arg** value needs to be replaced with the actual input parameter.
let arg = new Uint8Array(\[0\]);
let registerPromise: Promise<Uint8Array> = ifaa.register(arg);
registerPromise.then(registerResult => {
  console.info("Succeeded in doing register.");
  // Process **registerResult**.
}).catch((err: BusinessError) =>{
  console.error(\`Failed to call register. Code: ${err.code}, message: ${err.message}\`);
});

#### register

register(registerData: Uint8Array, callback: AsyncCallback<Uint8Array>): void

Enables IFAA passwordless authentication. This API returns the result asynchronously through a callback.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Security.Ifaa

**Start version**: 4.1.0(11)

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

registerData

 | 

Uint8Array

 | 

Yes

 | 

Registration data in TLV format, which is delivered by the IIFAA server.

 |
| 

callback

 | 

AsyncCallback<Uint8Array>

 | 

Yes

 | 

Callback function used to obtain returned data.

 |

**Error codes**:

For details about the error codes, please refer to [IFAA](../arkts-api-error-codes/ifaa/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Parameter error.

 |
| 

801

 | 

Device type error.

 |
| 

1006100001

 | 

System Interruption.

 |
| 

1006100002

 | 

The service is abnormal.

 |

**Example**:

import { BusinessError } from '@kit.BasicServicesKit';

// Construct an input parameter based on the TLV format of IIFAA and convert it into a Uint8Array parameter. Here, the **arg** value needs to be replaced with the actual input parameter.
let arg = new Uint8Array(\[0\]);
ifaa.register(arg, (err: BusinessError, registerResult: Uint8Array) => {
  if (err) {
    console.error(\`Failed to call register. Code: ${err.code}, message: ${err.message}\`);
  } else {
    console.info("Succeeded in doing register.");
    // Process **registerResult**.
  }
});

#### preAuthSync

preAuthSync(): Uint8Array

Obtains the pre-authentication parameters for IFAA passwordless authentication and returns the result synchronously.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Security.Ifaa

**Start version**: 4.1.0(11)

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

Pre-authentication parameters for IFAA passwordless authentication, including the challenge value required for subsequent biometric authentication.

 |

**Error codes**:

For details about the error codes, please refer to [IFAA](../arkts-api-error-codes/ifaa/document.md).

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

1006100001

 | 

System Interruption.

 |
| 

1006100002

 | 

The service is abnormal.

 |

**Example**:

let preAuthResult: Uint8Array = ifaa.preAuthSync();
// Process **preAuthResult**.

#### preAuth

preAuth(): Promise<Uint8Array>

Obtains the pre-authentication parameters for IFAA passwordless authentication. This API returns the result asynchronously through a promise.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Security.Ifaa

**Start version**: 4.1.0(11)

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

Pre-authentication data returned through a promise.

 |

**Error codes**:

For details about the error codes, please refer to [IFAA](../arkts-api-error-codes/ifaa/document.md).

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

1006100001

 | 

System Interruption.

 |
| 

1006100002

 | 

The service is abnormal.

 |

**Example**:

import { BusinessError } from '@kit.BasicServicesKit';

let preAuthPromise: Promise<Uint8Array> = ifaa.preAuth();
preAuthPromise.then(preAuthResult => {
  console.info("Succeeded in doing preAuth.");
  // Process **preAuthResult**.
}).catch((err: BusinessError) =>{
  console.error(\`Failed to call preAuth. Code: ${err.code}, message: ${err.message}\`);
});

#### preAuth

preAuth(callback: AsyncCallback<Uint8Array>): void

Obtains the pre-authentication parameters for IFAA passwordless authentication. This API returns the result asynchronously through a callback.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Security.Ifaa

**Start version**: 4.1.0(11)

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

callback

 | 

AsyncCallback<Uint8Array>

 | 

Yes

 | 

Callback function used to obtain returned pre-authentication data.

 |

**Error codes**:

For details about the error codes, please refer to [IFAA](../arkts-api-error-codes/ifaa/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Parameter error.

 |
| 

801

 | 

Device type error.

 |
| 

1006100001

 | 

System Interruption.

 |
| 

1006100002

 | 

The service is abnormal.

 |

**Example**:

import { BusinessError } from '@kit.BasicServicesKit';

ifaa.preAuth(
  (err: BusinessError, preAuthResult:Uint8Array) => {
    if (err) {
      console.error(\`Failed to call preAuth. Code: ${err.code}, message: ${err.message}\`);
    } else {
      console.info("Succeeded in doing preAuth.");
      // Process **preAuthResult**.
    }
  });

#### authSync

authSync(authToken: Uint8Array, authData: Uint8Array): Uint8Array

Performs IFAA passwordless authentication and returns the result synchronously.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Security.Ifaa

**Start version**: 4.1.0(11)

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

authToken

 | 

Uint8Array

 | 

Yes

 | 

Credential proving that a user passes the authentication. (Obtain this credential by calling the **getUserAuthInstance** API of the **@ohos.userIAM.userAuth** module.)

 |
| 

authData

 | 

Uint8Array

 | 

Yes

 | 

Authentication data in TLV format, which is delivered by the IIFAA server.

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

Authentication result in TLV format.

 |

**Error codes**:

For details about the error codes, please refer to [IFAA](../arkts-api-error-codes/ifaa/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Parameter error.

 |
| 

801

 | 

Device type error.

 |
| 

1006100001

 | 

System Interruption.

 |
| 

1006100002

 | 

The service is abnormal.

 |

**Example**:

// Call **getUserAuthInstance** of **@ohos.userIAM.userAuth** to obtain the token. Here, the **token** value needs to be replaced with actual input parameters.
let token = new Uint8Array(\[0\]);
// Construct input parameters based on the TLV format of IIFAA and convert them into Uint8Array parameters. Here, the **arg** value needs to be replaced with actual input parameters.
let arg = new Uint8Array(\[0\]);
let authResult: Uint8Array = ifaa.authSync(token, arg);
// Process **authResult**.

#### auth

auth(authToken: Uint8Array, authData: Uint8Array): Promise<Uint8Array>

Performs IFAA passwordless authentication. This API returns the result asynchronously through a promise.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Security.Ifaa

**Start version**: 4.1.0(11)

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

authToken

 | 

Uint8Array

 | 

Yes

 | 

Credential proving that a user passes the authentication. (Obtain this credential by calling the **getUserAuthInstance** API of the **@ohos.userIAM.userAuth** module.)

 |
| 

authData

 | 

Uint8Array

 | 

Yes

 | 

Authentication data in TLV format, which is delivered by the IIFAA server.

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

Authentication result in TLV format, which is returned through a promise.

 |

**Error codes**:

For details about the error codes, please refer to [IFAA](../arkts-api-error-codes/ifaa/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Parameter error.

 |
| 

801

 | 

Device type error.

 |
| 

1006100001

 | 

System Interruption.

 |
| 

1006100002

 | 

The service is abnormal.

 |

**Example**:

import { BusinessError } from '@kit.BasicServicesKit';

// Call **getUserAuthInstance** of **@ohos.userIAM.userAuth** to obtain the token. Here, the **token** value needs to be replaced with actual input parameters.
let token = new Uint8Array(\[0\]);
// Construct input parameters based on the TLV format of IIFAA and convert them into Uint8Array parameters. Here, the **arg** value needs to be replaced with actual input parameters.
let arg = new Uint8Array(\[0\]);
let authPromise: Promise<Uint8Array> = ifaa.auth(token, arg);
authPromise.then(authResult => {
  console.info("Succeeded in doing auth.");
  // Process **authResult**.
}).catch((err: BusinessError) =>{
  console.error(\`Failed to call auth. Code: ${err.code}, message: ${err.message}\`);
});

#### auth

auth(authToken: Uint8Array, authData: Uint8Array, callback: AsyncCallback<Uint8Array>): void

Performs IFAA passwordless authentication. This API returns the result asynchronously through a callback.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Security.Ifaa

**Start version**: 4.1.0(11)

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

authToken

 | 

Uint8Array

 | 

Yes

 | 

Credential proving that a user passes the authentication. (Obtain this credential by calling the **getUserAuthInstance** API of the **@ohos.userIAM.userAuth** module.)

 |
| 

authData

 | 

Uint8Array

 | 

Yes

 | 

Authentication data in TLV format, which is delivered by the IIFAA server.

 |
| 

callback

 | 

AsyncCallback<Uint8Array>

 | 

Yes

 | 

Callback function used to obtain returned data.

 |

**Error codes**:

For details about the error codes, please refer to [IFAA](../arkts-api-error-codes/ifaa/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Parameter error.

 |
| 

801

 | 

Device type error.

 |
| 

1006100001

 | 

System Interruption.

 |
| 

1006100002

 | 

The service is abnormal.

 |

**Example**:

import { BusinessError } from '@kit.BasicServicesKit';

// Call **getUserAuthInstance** of **@ohos.userIAM.userAuth** to obtain the token. Here, the **token** value needs to be replaced with actual input parameters.
let token = new Uint8Array(\[0\]);
// Construct input parameters based on the TLV format of IIFAA and convert them into Uint8Array parameters. Here, the **arg** value needs to be replaced with actual input parameters.
let arg = new Uint8Array(\[0\]);
ifaa.auth(token, arg,
  (err: BusinessError, authResult: Uint8Array) => {
    if (err) {
      console.error(\`Failed to call auth. Code: ${err.code}, message: ${err.message}\`);
    } else {
      console.info("Succeeded in doing auth.");
      // Process **authResult**.
    }
  });

#### deregisterSync

deregisterSync(deregisterData: Uint8Array): void

Disables IFAA passwordless authentication and returns the result synchronously.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Security.Ifaa

**Start version**: 4.1.0(11)

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

deregisterData

 | 

Uint8Array

 | 

Yes

 | 

Deregistration data in TLV format, which is delivered by the IIFAA server.

 |

**Error codes**:

For details about the error codes, please refer to [IFAA](../arkts-api-error-codes/ifaa/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Parameter error.

 |
| 

801

 | 

Device type error.

 |
| 

1006100001

 | 

System Interruption.

 |
| 

1006100002

 | 

The service is abnormal.

 |

**Example**:

// Construct an input parameter based on the TLV format of IIFAA and convert it into a Uint8Array parameter. Here, the **arg** value needs to be replaced with the actual input parameter.
let arg = new Uint8Array(\[0\]);
ifaa.deregisterSync(arg);

#### deregister

deregister(deregisterData: Uint8Array): Promise<void>

Disables IFAA passwordless authentication. This API returns the result asynchronously through a promise.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Security.Ifaa

**Start version**: 4.1.0(11)

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

deregisterData

 | 

Uint8Array

 | 

Yes

 | 

Deregistration data in TLV format, which is delivered by the IIFAA server.

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

For details about the error codes, please refer to [IFAA](../arkts-api-error-codes/ifaa/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Parameter error.

 |
| 

801

 | 

Device type error.

 |
| 

1006100001

 | 

System Interruption.

 |
| 

1006100002

 | 

The service is abnormal.

 |

**Example**:

import { BusinessError } from '@kit.BasicServicesKit';

// Construct an input parameter based on the TLV format of IIFAA and convert it into a Uint8Array parameter. Here, the **arg** value needs to be replaced with the actual input parameter.
let arg = new Uint8Array(\[0\]);
let promise: Promise<void> = ifaa.deregister(arg);
promise.then(()=> {
  console.info("Succeeded in doing deregister.");
}).catch((err: BusinessError) => {
  console.error(\`Failed to call deregister. Code: ${err.code}, message: ${err.message}\`);
});

#### deregister

deregister(deregisterData: Uint8Array, callback: AsyncCallback<void>): void

Disables IFAA passwordless authentication. This API returns the result asynchronously through a callback.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Security.Ifaa

**Start version**: 4.1.0(11)

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

deregisterData

 | 

Uint8Array

 | 

Yes

 | 

Deregistration data in TLV format, which is delivered by the IIFAA server.

 |
| 

callback

 | 

AsyncCallback<void>

 | 

Yes

 | 

Callback function.

 |

**Error codes**:

For details about the error codes, please refer to [IFAA](../arkts-api-error-codes/ifaa/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Parameter error.

 |
| 

801

 | 

Device type error.

 |
| 

1006100001

 | 

System Interruption.

 |
| 

1006100002

 | 

The service is abnormal.

 |

**Example**:

import { BusinessError } from '@kit.BasicServicesKit';

// Construct an input parameter based on the TLV format of IIFAA and convert it into a Uint8Array parameter. Here, the **arg** value needs to be replaced with the actual input parameter.
let arg = new Uint8Array(\[0\]);
ifaa.deregister(arg,
  (err: BusinessError) => {
    if (err) {
      console.error(\`Failed to call deregister. Code: ${err.code}, message: ${err.message}\`);
    } else {
      console.info("Succeeded in doing deregister.");
    }
});

#### getProtocolVersionSync

getProtocolVersionSync(): Uint8Array

Obtains the protocol version number for IFAA passwordless authentication and returns the result synchronously.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Security.Ifaa

**Start version**: 4.1.0(11)

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

Protocol version number for IFAA passwordless authentication.

 |

**Error codes**:

For details about the error codes, please refer to [IFAA](../arkts-api-error-codes/ifaa/document.md).

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

1006100001

 | 

System Interruption.

 |
| 

1006100002

 | 

The service is abnormal.

 |

**Example**:

let res: Uint8Array = ifaa.getProtocolVersionSync();

#### getProtocolVersion

getProtocolVersion(): Promise<Uint8Array>

Obtains the protocol version number for IFAA passwordless authentication. This API returns the result asynchronously through a promise.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Security.Ifaa

**Start version**: 4.1.0(11)

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

Protocol version number returned through a promise.

 |

**Error codes**:

For details about the error codes, please refer to [IFAA](../arkts-api-error-codes/ifaa/document.md).

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

1006100001

 | 

System Interruption.

 |
| 

1006100002

 | 

The service is abnormal.

 |

**Example**:

import { BusinessError } from '@kit.BasicServicesKit';

let promise: Promise<Uint8Array> = ifaa.getProtocolVersion();
promise.then(result => {
  console.info("Succeeded in doing getProtocolVersion.");
  // Process **result**.
}).catch((err: BusinessError) => {
  console.error(\`Failed to call getProtocolVersion. Code: ${err.code}, message: ${err.message}\`);
});

#### getProtocolVersion

getProtocolVersion(callback: AsyncCallback<Uint8Array>): void

Obtains the protocol version number for IFAA passwordless authentication. This API returns the result asynchronously through a callback.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Security.Ifaa

**Start version**: 4.1.0(11)

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

callback

 | 

AsyncCallback<Uint8Array>

 | 

Yes

 | 

Callback function used to obtain returned data.

 |

**Error codes**:

For details about the error codes, please refer to [IFAA](../arkts-api-error-codes/ifaa/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Parameter error.

 |
| 

801

 | 

Device type error.

 |
| 

1006100001

 | 

System Interruption.

 |
| 

1006100002

 | 

The service is abnormal.

 |

**Example**:

import { BusinessError } from '@kit.BasicServicesKit';

ifaa.getProtocolVersion(
  (err: BusinessError, result: Uint8Array) => {
    if (err) {
      console.error(\`Failed to call getProtocolVersion. Code: ${err.code}, message: ${err.message}\`);
    } else {
      console.info("Succeeded in doing getProtocolVersion.");
      // Process **result**.
    }
  });

#### getSupportedCertTypesSync

getSupportedCertTypesSync(): Uint8Array

Obtains the certificate format supported by IFAA passwordless authentication and returns the result synchronously.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Security.Ifaa

**Start version**: 4.1.0(11)

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

Certificate format supported by IFAA passwordless authentication.

 |

**Error codes**:

For details about the error codes, please refer to [IFAA](../arkts-api-error-codes/ifaa/document.md).

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

1006100001

 | 

System Interruption.

 |
| 

1006100002

 | 

The service is abnormal.

 |

**Example**:

let result: Uint8Array = ifaa.getSupportedCertTypesSync();
// Process **result**.

#### getSupportedCertTypes

getSupportedCertTypes(): Promise<Uint8Array>

Obtains the certificate format supported by IFAA passwordless authentication. This API returns the result asynchronously through a promise.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Security.Ifaa

**Start version**: 4.1.0(11)

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

Supported certificate format, which is returned through a promise.

 |

**Error codes**:

For details about the error codes, please refer to [IFAA](../arkts-api-error-codes/ifaa/document.md).

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

1006100001

 | 

System Interruption.

 |
| 

1006100002

 | 

The service is abnormal.

 |

**Example**:

import { BusinessError } from '@kit.BasicServicesKit';

let promise: Promise<Uint8Array> = ifaa.getSupportedCertTypes();
promise.then(result => {
  console.info("Succeeded in doing getSupportedCertTypes.");
  // Process **result**.
}).catch((err: BusinessError) => {
  console.error(\`Failed to call getSupportedCertTypes. Code: ${err.code}, message: ${err.message}\`);
});

#### getSupportedCertTypes

getSupportedCertTypes(callback: AsyncCallback<Uint8Array>): void

Obtains the certificate format supported by IFAA passwordless authentication. This API returns the result asynchronously through a callback.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Security.Ifaa

**Start version**: 4.1.0(11)

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

callback

 | 

AsyncCallback<Uint8Array>

 | 

Yes

 | 

Callback function used to obtain returned data.

 |

**Error codes**:

For details about the error codes, please refer to [IFAA](../arkts-api-error-codes/ifaa/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Parameter error.

 |
| 

801

 | 

Device type error.

 |
| 

1006100001

 | 

System Interruption.

 |
| 

1006100002

 | 

The service is abnormal.

 |

**Example**:

import { BusinessError } from '@kit.BasicServicesKit';

ifaa.getSupportedCertTypes(
  (err: BusinessError, result: Uint8Array) => {
    if (err) {
      console.error(\`Failed to call getSupportedCertTypes. Code: ${err.code}, message: ${err.message}\`);
    } else {
      console.info("Succeeded in doing getSupportedCertTypes.");
      // Process **result**.
    }
  });
