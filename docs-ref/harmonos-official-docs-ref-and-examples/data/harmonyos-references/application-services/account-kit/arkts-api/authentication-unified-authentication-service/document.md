# authentication (Unified Authentication Service)

This module provides the authentication capabilities of Account Kit, including account sign-in, authorization, and authorization revoking. You can use these capabilities to implement account sign-in and registration, obtain the sign-in status of a HUAWEI ID, verify the mobile number consistency status, obtain user authorization information, and so on.

**Start version**: 4.0.0(10)

#### Module Import

import { authentication } from '@kit.AccountKit';

#### HuaweiIDProvider

Provides methods for implementing the authentication service. This API is used to create sign-in, authorization, and authorization revoking request objects.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.Auth

**Start version**: 4.0.0(10)

**Inheritance**: **HuaweiIDProvider** inherits from [AuthenticationProvider](#section1860064133610).

#### \[h2\]createLoginWithHuaweiIDRequest

createLoginWithHuaweiIDRequest(): LoginWithHuaweiIDRequest

Creates a sign-in request object with default scopes and permissions. You can set properties in this object to specify the request parameter for the HUAWEI ID sign-in scenario.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.Auth

**Start version**: 4.0.0(10)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[LoginWithHuaweiIDRequest](#section42261825935)

 | 

Object for requesting data such as the UnionID and OpenID via Account Kit during app sign-in. Set request parameters for this object according to your actual needs.

 |

**Example**:

import { authentication } from '@kit.AccountKit';

const huaweiIdProvider = new authentication.HuaweiIDProvider();
const loginWithHuaweiIDRequest = huaweiIdProvider.createLoginWithHuaweiIDRequest();

#### \[h2\]createAuthorizationWithHuaweiIDRequest

createAuthorizationWithHuaweiIDRequest(): AuthorizationWithHuaweiIDRequest

Creates an object for requesting authorization via Account Kit. You can set properties in this object to specify the request parameter for the HUAWEI ID sign-in scenario.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.Auth

**Start version**: 4.0.0(10)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[AuthorizationWithHuaweiIDRequest](#section12940173017165)

 | 

Object for requesting authorization for obtaining user information.

 |

**Example**:

import { authentication } from '@kit.AccountKit';

const huaweiIdProvider = new authentication.HuaweiIDProvider();
const request = huaweiIdProvider.createAuthorizationWithHuaweiIDRequest();

#### \[h2\]createCancelAuthorizationRequest

createCancelAuthorizationRequest(): CancelAuthorizationRequest

Creates an object for requesting to revoke authorization via Account Kit. You can set properties in this object to specify the request parameter for revoking authorization from a HUAWEI ID.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.Auth

**Start version**: 4.0.0(10)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[CancelAuthorizationRequest](#section17720275174)

 | 

Object for requesting to revoke authorization.

 |

**Example**:

import { authentication } from '@kit.AccountKit';

const huaweiIdProvider = new authentication.HuaweiIDProvider();
const cancelAuthorizationRequest = huaweiIdProvider.createCancelAuthorizationRequest();

#### \[h2\]getHuaweiIDState

getHuaweiIDState(request: StateRequest): Promise<StateResult>

Obtains the sign-in status of a HUAWEI ID. This API returns the result asynchronously through a promise. It can be used to check whether a HUAWEI ID is signed in, without relying on network connection.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.Auth

**Start version**: 5.0.0(12)

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

request

 | 

[StateRequest](#section9615740103819)

 | 

Yes

 | 

Request object for obtaining the sign-in status of a HUAWEI ID. The object includes request parameters.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[StateResult](#section18875010506)\>

 | 

[StateResult](#section18875010506) object returned through a promise.

 |

**Error codes**:

For details about the error codes, please refer to [Account Management Error Codes](../../../../system/basic-functions/basic-services-kit/error-codes/account-management-error-codes/document.md) and [ArkTS Error Codes](../../arkts-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

[12300001](../../../../system/basic-functions/basic-services-kit/error-codes/account-management-error-codes/document.md#section12300001-system-service-abnormal)

 | 

System service works abnormally.

 |
| 

[1001502003](../../arkts-error-codes/document.md#section289120911112)

 | 

Invalid input parameter value.

 |

**Example**:

import { authentication } from '@kit.AccountKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Create request parameters.
const stateRequest: authentication.StateRequest = {
  idType: authentication.IdType.UNION\_ID,
  idValue: '_xxx_' // The value can be obtained through the HUAWEI ID sign-in API.
}
try {
  // Execute the request for obtaining the HUAWEI ID sign-in status and process the result.
  new authentication.HuaweiIDProvider().getHuaweiIDState(stateRequest).then((data: authentication.StateResult) => {
    hilog.info(0x0000, 'testTag', 'Succeeded in getting huaweiIdState result.');
    const state = data.state;
    // Process the state.
  }).catch((error: BusinessError) => {
    dealAllError(error);
  })
} catch (error) {
  dealAllError(error);
}

// Handle the error.
function dealAllError(error: BusinessError): void {
  hilog.error(0x0000, 'testTag', \`Failed to get huaweiIdState, errorCode=${error.code}, errorMsg=${error.message}\`);
}

#### \[h2\]getMobileNumberConsistency

getMobileNumberConsistency(request: ConsistencyRequest): Promise<ConsistencyResult>

Obtains the mobile number consistency status. This API returns the result asynchronously through a promise. It is used to check whether the mobile number bound to the HUAWEI ID is the same as that of the SIM card in the device.

Before using the API for obtaining the mobile number consistency status, request the **quickLoginMobilePhone** scope first. For details, please refer to [Prerequisites](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/account-phone-unionid-login#section95093591227). If the scope/permission application fails, error [1001502014](../../arkts-error-codes/document.md#section78953611814) will be returned, indicating that the app has not got necessary scopes/permissions.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.Auth

**Device behavior differences**: This API works on phones, PCs/2-in-1 devices, and tablets. On other devices, it returns error code 801.

**Start version**: 5.0.0(12)

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

request

 | 

[ConsistencyRequest](#section168131411512)

 | 

Yes

 | 

Request object for obtaining the mobile number consistency status, including request parameters.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[ConsistencyResult](#section155352089012)\>

 | 

[ConsistencyResult](#section155352089012) object returned through a promise.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS Error Codes](../../arkts-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

[401](../../../../api-reference-overview/universal-error-codes/document.md#section401-parameter-check-failed)

 | 

Parameter error. Possible causes:

1\. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

 |
| 

[801](../../../../api-reference-overview/universal-error-codes/document.md#section801-api-not-supported)

 | 

Capability not supported. Function getMobileNumberConsistency can not work correctly due to limited device capabilities.

 |
| 

[1001500001](../../arkts-error-codes/document.md#section1581681312511)

 | 

Failed to check the fingerprint of the app bundle.

 |
| 

[1001500004](../../arkts-error-codes/document.md#section13107132603718)

 | 

The account does not support this function.

 |
| 

[1001500005](../../arkts-error-codes/document.md#section612754419379)

 | 

This function is restricted from being called.

 |
| 

[1001502001](../../arkts-error-codes/document.md#section539558125020)

 | 

The user has not logged in with HUAWEI ID.

 |
| 

[1001502002](../../arkts-error-codes/document.md#section1393125918588)

 | 

The application is not authorized.

 |
| 

[1001502005](../../arkts-error-codes/document.md#section1281526328)

 | 

Network error.

 |
| 

[1001502009](../../arkts-error-codes/document.md#section17561151616317)

 | 

Internal error.

 |
| 

[1001502014](../../arkts-error-codes/document.md#section78953611814)

 | 

The app does not have the required scopes or permissions.

 |

**Example**:

import { authentication } from '@kit.AccountKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Create request parameters.
const consistencyRequest: authentication.ConsistencyRequest = {
  idType: authentication.IdType.UNION\_ID,
  idValue: '_xxx_', // The value can be obtained through the HUAWEI ID sign-in API.
  mobileNumber: '+86xxxxxxxxxxx' // Mobile number in plaintext obtained through the one-tap HUAWEI ID sign-in function.
}
try {
  // Execute the request for obtaining the mobile number consistency status and process the result.
  new authentication.HuaweiIDProvider().getMobileNumberConsistency(consistencyRequest)
    .then((data: authentication.ConsistencyResult) => {
      hilog.info(0x0000, 'testTag', \`Succeeded in getting getMobileNumberConsistency result = ${data.state}\`);
      const state = data.state;
      // Process the state.
    })
    .catch((err: BusinessError) => {
      dealAllError(err);
    })
} catch (error) {
  dealAllError(error);
}

// Handle the error.
function dealAllError(error: BusinessError): void {
  hilog.error(0x0000, 'testTag',
    \`Failed to get mobileNumberConsistency, errorCode=${error.code}, errorMsg=${error.message}\`);
}

#### LoginWithHuaweiIDRequest

Object for requesting data such as the UnionID and OpenID via Account Kit during app sign-in. Set request parameters for this object according to your actual needs.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.Auth

**Start version**: 4.0.0(10)

**Inheritance**: **LoginWithHuaweiIDRequest** inherits from [AuthenticationRequest](#section3118182610348).

| 
**Name**

 | 

**Type**

 | 

**Read-Only**

 | 

**Optional**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

forceLogin

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether to forcibly show the HUAWEI ID sign-in screen.

If the value is **true** but no HUAWEI ID has signed in, the HUAWEI ID sign-in screen will be displayed.

If the value is **false** and no HUAWEI ID has signed in, error [1001502001 User Has Not Signed In to HUAWEI ID](../../arkts-error-codes/document.md#section539558125020) will be returned when you call [executeRequest](#section3975181884311).

Default value: **true**

 |
| 

state

 | 

string

 | 

No

 | 

Yes

 | 

**state** parameter in the request body. This parameter will be compared with the **state** parameter in the response body to prevent cross-site attacks.

The value can contain digits (0–9), letters (a–z or A–Z), dots (.), colons (:), slashes (/), and underscores (\_). The length limit is 1 to 255 characters. The verification rule is ^\[0-9a-zA-Z:/\\.\\-\_\]{1,255}$.

You are advised to use nonces and perform consistency verification. [util.generateRandomUUID()](../../../../application-framework/arkts/arkts-apis/ohos-util-util/document.md#utilgeneraterandomuuid9) is recommended.

 |
| 

nonce

 | 

string

 | 

No

 | 

Yes

 | 

**nonce** parameter in the request body. This parameter is contained in the returned ID token and can be used to prevent replay attacks through consistency verification.

The value can contain digits (0–9), letters (a–z or A–Z), dots (.), colons (:), slashes (/), and underscores (\_). The length limit is 1 to 255 characters. The verification rule is ^\[0-9a-zA-Z:/\\.\\-\_\]{1,255}$.

If this parameter is not passed or is left empty, the default value of **nonce** in the ID token is **default**.

You are advised to use nonces and perform consistency verification. [util.generateRandomUUID()](../../../../application-framework/arkts/arkts-apis/ohos-util-util/document.md#utilgeneraterandomuuid9) is recommended.

 |
| 

idTokenSignAlgorithm

 | 

[IdTokenSignAlgorithm](#section3339031310)

 | 

No

 | 

Yes

 | 

ID token signing algorithm. Select an algorithm for your app based on the security, performance, and system compatibility requirements.

The default value is **PS256**.

 |

**Example**:

import { authentication } from '@kit.AccountKit';
import { util } from '@kit.ArkTS';

const loginRequest = new authentication.HuaweiIDProvider().createLoginWithHuaweiIDRequest();
// The default value is **true**. If no HUAWEI ID has signed in, the HUAWEI ID sign-in screen will be forcibly shown.
loginRequest.forceLogin = true;
loginRequest.idTokenSignAlgorithm = authentication.IdTokenSignAlgorithm.PS256; // The default value is **PS256**.
loginRequest.state = util.generateRandomUUID(); // You are advised to use **generateRandomUUID** to generate a state.

#### IdTokenSignAlgorithm

ID token signing algorithm, which has enumerated values. ID tokens are encrypted according to the value of **IdTokenSignAlgorithm**. Select an algorithm for your app based on the security, performance, and system compatibility requirements.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.Auth

**Start version**: 4.0.0(10)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

PS256

 | 

1

 | 

RSASSA-PSS uses SHA-256 and SHA-256-based MGF1. For security purposes, PS256 is recommended.

 |
| 

RS256

 | 

2

 | 

RSASSA-PKCS1-v1\_5 uses SHA-256.

 |

**Example**:

import { authentication } from '@kit.AccountKit';

const loginRequest = new authentication.HuaweiIDProvider().createLoginWithHuaweiIDRequest();
// The default value is **true**. If no HUAWEI ID has signed in, the HUAWEI ID sign-in screen will be forcibly shown.
loginRequest.forceLogin = true;
loginRequest.idTokenSignAlgorithm = authentication.IdTokenSignAlgorithm.PS256;

#### LoginWithHuaweiIDResponse

Object for responding to the sign-in request via Account Kit, which can be parsed to obtain data such as the OpenID, UnionID, authorization code, and ID token. It is used as a return result after successful HUAWEI ID sign-in and can be parsed to obtain HUAWEI ID-related information.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.Auth

**Start version**: 4.0.0(10)

**Inheritance**: **LoginWithHuaweiIDResponse** inherits from [AuthenticationResponse](#section2697164193515).

| 
**Name**

 | 

**Type**

 | 

**Read-Only**

 | 

**Optional**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

data

 | 

[LoginWithHuaweiIDCredential](#section17820155561513)

 | 

Yes

 | 

Yes

 | 

Sign-in result data, which is used to obtain or associate with HUAWEI ID-related information. **openID**, **unionID**, **authorizationCode**, and **idToken** parameters are contained in the result data.

 |
| 

state

 | 

string

 | 

Yes

 | 

Yes

 | 

**state** parameter returned in the response body. Account Kit compares this parameter with the **state** parameter passed in the request body to prevent cross-site attacks. The value can contain digits (0–9), letters (a–z or A–Z), dots (.), colons (:), slashes (/), and underscores (\_). The length limit is 1 to 255 characters. The verification rule is ^\[0-9a-zA-Z:/\\.\\-\_\]{1,255}$.

 |

**Example**:

import { authentication } from '@kit.AccountKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { util } from '@kit.ArkTS';
import { BusinessError } from '@kit.BasicServicesKit';

// Create a sign-in request and set parameters.
const loginRequest = new authentication.HuaweiIDProvider().createLoginWithHuaweiIDRequest();
// The default value is **true**. If no HUAWEI ID has signed in, the HUAWEI ID sign-in screen will be forcibly shown.
loginRequest.forceLogin = true;
loginRequest.idTokenSignAlgorithm = authentication.IdTokenSignAlgorithm.PS256;
loginRequest.state = util.generateRandomUUID(); // You are advised to use **generateRandomUUID** to generate a state.

// Execute the sign-in request and process the result.
try {
  // The following provides only code snippets. Use it in the custom component instance to obtain the **UIContext** object as the input parameter of the function.
  const controller = new authentication.AuthenticationController(this.getUIContext().getHostContext());
  controller.executeRequest(loginRequest, (error: BusinessError<Object>, data) => {
    if (error) {
      dealAllError(error);
      return;
    }
    const loginWithHuaweiIDResponse = data as authentication.LoginWithHuaweiIDResponse;
    const state = loginWithHuaweiIDResponse.state;
    if (state && loginRequest.state !== state) {
      hilog.error(0x0000, 'testTag', \`Failed to login. The state is different, response state: ${state}\`);
      return;
    }
    hilog.info(0x0000, 'testTag', 'Succeeded in login.');
    const loginWithHuaweiIDCredential = loginWithHuaweiIDResponse?.data;
    const code = loginWithHuaweiIDCredential?.authorizationCode;
    const idToken = loginWithHuaweiIDCredential?.idToken;
    // Process the authorization code and ID token.
  });
} catch (error) {
  dealAllError(error);
}

// Handle the error.
function dealAllError(error: BusinessError<Object>): void {
  hilog.error(0x0000, 'testTag', \`Failed to login. Code: ${error.code}, message: ${error.message}\`);
  // In sign-in scenarios involving UI interactions, it is advised to guide users with the following error code prompts:
  if (error.code === ErrorCode.ERROR\_CODE\_LOGIN\_OUT) {
    // HUAWEI ID not signed in. Use a HUAWEI ID to sign in and try again, or sign in to the app in another way.
  } else if (error.code === ErrorCode.ERROR\_CODE\_NETWORK\_ERROR) {
    // A network exception occurs. Check the current network status and try again, or sign in to the app in another way.
  } else if (error.code === ErrorCode.ERROR\_CODE\_INTERNAL\_ERROR) {
    // Failed to sign in. Try another way.
  } else if (error.code === ErrorCode.ERROR\_CODE\_USER\_CANCEL) {
    // Authorization canceled.
  } else if (error.code === ErrorCode.ERROR\_CODE\_SYSTEM\_SERVICE) {
    // System service exception. Try again later or sign in to the app in another way.
  } else if (error.code === ErrorCode.ERROR\_CODE\_REQUEST\_REFUSE) {
    // Repeated request. No further action is needed.
  } else {
    // Failed to sign in. Try another way.
  }
}

export enum ErrorCode {
  // The HUAWEI ID is not signed in.
  ERROR\_CODE\_LOGIN\_OUT = 1001502001,
  // Network error.
  ERROR\_CODE\_NETWORK\_ERROR = 1001502005,
  // Internal error.
  ERROR\_CODE\_INTERNAL\_ERROR = 1001502009,
  // Authorization canceled.
  ERROR\_CODE\_USER\_CANCEL = 1001502012,
  // System service error.
  ERROR\_CODE\_SYSTEM\_SERVICE = 12300001,
  // Repeated request.
  ERROR\_CODE\_REQUEST\_REFUSE = 1001500002
}

#### LoginWithHuaweiIDCredential

Credential returned after successful sign-in via Account Kit, which is used to obtain user information and associate with a HUAWEI ID (through OpenID/UnionID).

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.Auth

**Start version**: 4.0.0(10)

| 
**Name**

 | 

**Type**

 | 

**Read-Only**

 | 

**Optional**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

authorizationCode

 | 

string

 | 

Yes

 | 

Yes

 | 

Authorization code. It is a temporary credential used to obtain an access token. The obtained token is valid for 5 minutes and can be used only once. The value contains 1 to 1024 characters.

 |
| 

idToken

 | 

string

 | 

Yes

 | 

Yes

 | 

ID token. It is a JWT character string that contains user information, which can be used to obtain some user information and verify signatures. The value contains 1 to 2048 characters.

 |
| 

openID

 | 

string

 | 

Yes

 | 

No

 | 

OpenID, which represents the identity of a HUAWEI ID user when using different types of products. The same user has different OpenIDs for different apps. For details about the format requirements, please refer to [Formats of OpenID and UnionID](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/account-faq-9).

 |
| 

unionID

 | 

string

 | 

Yes

 | 

No

 | 

UnionID, which represents the identity of a HUAWEI ID user when using different products of the same developer. The same user has the same UnionID for different apps of the same developer. For details about the format requirements, please refer to [Formats of OpenID and UnionID](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/account-faq-9).

 |

**Example**:

import { authentication } from '@kit.AccountKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { util } from '@kit.ArkTS';
import { BusinessError } from '@kit.BasicServicesKit';

// Create a sign-in request and set parameters.
const loginRequest = new authentication.HuaweiIDProvider().createLoginWithHuaweiIDRequest();
// The default value is **true**. If no HUAWEI ID has signed in, the HUAWEI ID sign-in screen will be forcibly shown.
loginRequest.forceLogin = true;
loginRequest.idTokenSignAlgorithm = authentication.IdTokenSignAlgorithm.PS256;
loginRequest.state = util.generateRandomUUID(); // You are advised to use **generateRandomUUID** to generate a state.

// Execute the sign-in request and process the result.
try {
  // The following provides only code snippets. Use it in the custom component instance to obtain the **UIContext** object as the input parameter of the function.
  const controller = new authentication.AuthenticationController(this.getUIContext().getHostContext());
  controller.executeRequest(loginRequest, (error: BusinessError<Object>, data) => {
    if (error) {
      dealAllError(error);
      return;
    }
    const loginWithHuaweiIDResponse = data as authentication.LoginWithHuaweiIDResponse;
    const state = loginWithHuaweiIDResponse.state;
    if (state && loginRequest.state !== state) {
      hilog.error(0x0000,
        'testTag', \`Failed to login. The state is different, response state: ${state}\`);
      return;
    }
    hilog.info(0x0000, 'testTag', 'Succeeded in login.');

    const loginWithHuaweiIDCredential = loginWithHuaweiIDResponse?.data;
    const code = loginWithHuaweiIDCredential?.authorizationCode;
    const idToken = loginWithHuaweiIDCredential?.idToken;
    // Process the authorization code and ID token.
  });
} catch (error) {
  dealAllError(error);
}

// Handle the error.
function dealAllError(error: BusinessError<Object>): void {
  hilog.error(0x0000, 'testTag', \`Failed to login. Code: ${error.code}, message: ${error.message}\`);
  // In sign-in scenarios involving UI interactions, it is advised to guide users with the following error code prompts:
  if (error.code === ErrorCode.ERROR\_CODE\_LOGIN\_OUT) {
    // HUAWEI ID not signed in. Use a HUAWEI ID to sign in and try again, or sign in to the app in another way.
  } else if (error.code === ErrorCode.ERROR\_CODE\_NETWORK\_ERROR) {
    // A network exception occurs. Check the current network status and try again, or sign in to the app in another way.
  } else if (error.code === ErrorCode.ERROR\_CODE\_INTERNAL\_ERROR) {
    // Failed to sign in. Try another way.
  } else if (error.code === ErrorCode.ERROR\_CODE\_USER\_CANCEL) {
    // Authorization canceled.
  } else if (error.code === ErrorCode.ERROR\_CODE\_SYSTEM\_SERVICE) {
    // System service exception. Try again later or sign in to the app in another way.
  } else if (error.code === ErrorCode.ERROR\_CODE\_REQUEST\_REFUSE) {
    // Repeated request. No further action is needed.
  } else {
    // Failed to sign in. Try another way.
  }
}

export enum ErrorCode {
  // The HUAWEI ID is not signed in.
  ERROR\_CODE\_LOGIN\_OUT = 1001502001,
  // Network error.
  ERROR\_CODE\_NETWORK\_ERROR = 1001502005,
  // Internal error.
  ERROR\_CODE\_INTERNAL\_ERROR = 1001502009,
  // Authorization canceled.
  ERROR\_CODE\_USER\_CANCEL = 1001502012,
  // System service error.
  ERROR\_CODE\_SYSTEM\_SERVICE = 12300001,
  // Repeated request.
  ERROR\_CODE\_REQUEST\_REFUSE = 1001500002
}

#### AuthorizationWithHuaweiIDRequest

Object for requesting authorization via Account Kit to obtain more user information, which contains parameters such as **scopes** and **permissions**. It is used as an object for requesting authorization from a HUAWEI ID. You can pass parameters as needed.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.Auth

**Start version**: 4.0.0(10)

**Inheritance**: **AuthorizationWithHuaweiIDRequest** inherits from [AuthenticationRequest](#section3118182610348).

| 
**Name**

 | 

**Type**

 | 

**Read-Only**

 | 

**Optional**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

scopes

 | 

string\[\]

 | 

No

 | 

Yes

 | 

List of scopes used to obtain user data. The **scopes** and **permissions** parameters cannot be empty at the same time. Otherwise, error [1001502003](../../arkts-error-codes/document.md#section289120911112) will be returned. If an invalid scope (for example, **null**) is passed, the OpenID and UnionID are directly returned.

Default value: **\['openid'\]**

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

The options of **scopes** are as follows:

-   **profile**: scope for obtaining the basic information about a HUAWEI ID user, such as the nickname and avatar. (Atomic service version 5.1.1(19) and later support this scope. Additionally, you need to specify the **supportAtomicService** parameter.)
-   **openid**: scope for obtaining the OpenID and UnionID of a HUAWEI ID user. For details about the format requirements, please refer to [Formats of OpenID and UnionID](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/account-faq-9).
-   **phone**: scope for obtaining the mobile number bound to a HUAWEI ID for quick verification. (Atomic services do not support this scope, but the [quick mobile number verification button](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/scenario-fusion-button-getphonenumber) of Scenario Fusion Kit can be used for the atomic services to obtain mobile numbers. The mobile number of a child account cannot be obtained using this scope.) Before calling this scope, you need to request it. For details, please refer to [Prerequisites](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/account-get-phonenumber#section2011736191112).
-   **quickLoginAnonymousPhone**: scope for obtaining the anonymous mobile number bound to a HUAWEI ID. (This scope can only be used with **openid**. Anonymous mobile numbers cannot be obtained for wearables or user accounts registered outside the Chinese mainland. In this case, error [1001500003 Unsupported Scopes or Permissions](../../arkts-error-codes/document.md#section116574197436) will be reported). You need to request account permissions before using this scope. For details, please refer to [Prerequisites](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/account-phone-unionid-login#section95093591227).
    
    NOTE:
    
    **For HUAWEI ID registered in the Chinese mainland using mobile numbers also in the Chinese mainland, anonymous mobile numbers are returned without the country/region codes. For HUAWEI IDs registered in the Chinese mainland using mobile numbers from all other countries or regions, the returned anonymous mobile numbers include the country/region codes by default.**
    
-   **riskLevel**: scope for obtaining the risk level of a HUAWEI ID. (This scope can only be used together with **openid**, **phone**, or **profile**. For this API, atomic services do not support using the **riskLevel** scope in combination with **phone**. If an atomic service truly needs to use these two scopes together, refer to the [button for obtaining the mobile number and risk level](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/scenario-fusion-button-get-risklevel) of Scenario Fusion Kit. Accounts outside the Chinese mainland do not support this scope.) Before using this scope, you need to request it. For details, please refer to [Prerequisites](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/account-get-risklevel-on-demand-acquisition#section13750142919492).

 |
| 

permissions

 | 

string\[\]

 | 

No

 | 

Yes

 | 

Permission list, which is used to obtain a temporary credential for user authorization and identity verification information. The **scopes** and **permissions** parameters cannot be empty at the same time. Otherwise, error [1001502003](../../arkts-error-codes/document.md#section289120911112) will be returned. If an invalid permission (for example, **null**) is passed, the OpenID and UnionID are directly returned.

The parameter is left empty by default, indicating that the temporary credential and real-name information will not be returned.

The options of **permissions** are as follows:

-   **serviceauthcode**: temporary credentials for user authorization.
-   **idtoken**: user identity verification information.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

 |
| 

forceAuthorization

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether to forcibly show the HUAWEI ID sign-in screen when no HUAWEI ID has signed in.

Default value: **true**

If the value is **true** but the user has not signed in or given authorization, the user sign-in or authorization screen will be displayed.

If the value is **false** and the user has not signed in, error [1001502001 User Has Not Signed In to HUAWEI ID](../../arkts-error-codes/document.md#section539558125020) will be returned.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

 |
| 

state

 | 

string

 | 

No

 | 

Yes

 | 

**state** parameter in the request body. The value can contain digits (0–9), letters (a–z or A–Z), dots (.), colons (:), slashes (/), and underscores (\_). The length limit is 1 to 255 characters. The verification rule is ^\[0-9a-zA-Z:/\\.\\-\_\]{1,255}$. This parameter will be compared with the **state** parameter in the response body to prevent cross-site attacks.

You are advised to use nonces and perform consistency verification. [util.generateRandomUUID()](../../../../application-framework/arkts/arkts-apis/ohos-util-util/document.md#utilgeneraterandomuuid9) is recommended.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

 |
| 

nonce

 | 

string

 | 

No

 | 

Yes

 | 

**nonce** parameter in the request body. The value can contain digits (0–9), letters (a–z or A–Z), dots (.), colons (:), slashes (/), and underscores (\_). The length limit is 1 to 255 characters. The verification rule is ^\[0-9a-zA-Z:/\\.\\-\_\]{1,255}$. This parameter is contained in the returned ID token and can be used to prevent replay attacks through consistency verification. If this parameter is not passed or is left empty, the default value of **nonce** in the ID token is **default**.

You are advised to use nonces and perform consistency verification. [util.generateRandomUUID()](../../../../application-framework/arkts/arkts-apis/ohos-util-util/document.md#utilgeneraterandomuuid9) is recommended.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

 |
| 

idTokenSignAlgorithm

 | 

[IdTokenSignAlgorithm](#section3339031310)

 | 

No

 | 

Yes

 | 

Signing algorithm of ID tokens. The default value is **PS256**. Select an algorithm for your app based on the security, performance, and system compatibility requirements.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

 |
| 

supportAtomicService

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether obtaining the avatar and nickname is supported for an atomic service in the context that **profile** is passed to **scopes**.

The default value is **false**.

If this parameter is set to **true**, the avatar and nickname can be obtained.

If this parameter is set to **false**, error [1001500003 Unsupported Scopes or Permissions](../../arkts-error-codes/document.md#section116574197436) will be returned.

**Start version**: 5.1.1(19)

**Atomic service API**: This API can be used in atomic services since API version 5.1.1(19).

NOTE:

It is used for atomic services.

 |

**Example**:

import { authentication } from '@kit.AccountKit';
import { util } from '@kit.ArkTS';

const authRequest = new authentication.HuaweiIDProvider().createAuthorizationWithHuaweiIDRequest();
authRequest.scopes = \['profile'\]; // The atomic service can set **supportAtomicService** to **true** to use the **profile** scope.
authRequest.permissions = \['idtoken'\];
authRequest.forceAuthorization = true;
authRequest.state = util.generateRandomUUID(); // You are advised to use **generateRandomUUID** to generate a state.
authRequest.idTokenSignAlgorithm = authentication.IdTokenSignAlgorithm.PS256;

#### AuthorizationWithHuaweiIDResponse

Encapsulates user information returned in the [AuthorizationWithHuaweiIDRequest](#section12940173017165) object (used to request authorization). It is used as a return result after successful authorization of a HUAWEI ID and can be parsed to obtain HUAWEI ID-related information.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.Auth

**Start version**: 4.0.0(10)

**Inheritance**: **AuthorizationWithHuaweiIDResponse** inherits from [AuthenticationResponse](#section2697164193515).

| 
**Name**

 | 

**Type**

 | 

**Read-Only**

 | 

**Optional**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

data

 | 

[AuthorizationWithHuaweiIDCredential](#section1846111631718)

 | 

Yes

 | 

Yes

 | 

User authorization result data, which is used to obtain or associate with HUAWEI ID-related information.

 |
| 

state

 | 

string

 | 

Yes

 | 

Yes

 | 

**state** parameter returned in the response body. The value can contain digits (0–9), letters (a–z or A–Z), dots (.), colons (:), slashes (/), and underscores (\_). The length limit is 1 to 255 characters. The verification rule is ^\[0-9a-zA-Z:/\\.\\-\_\]{1,255}$. This parameter will be compared with the **state** parameter in the request body to prevent cross-site attacks.

 |

**Example**:

import { authentication } from '@kit.AccountKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { util } from '@kit.ArkTS';
import { BusinessError } from '@kit.BasicServicesKit';

// Create an authorization request and set parameters.
const authRequest = new authentication.HuaweiIDProvider().createAuthorizationWithHuaweiIDRequest();
// **openid** is the default value and cannot be modified. To obtain other user information, pass the relevant scope. For details, please refer to the documentation of the **AuthorizationWithHuaweiIDRequest** class.
authRequest.scopes = \['openid'\];
authRequest.permissions = \['idtoken', 'serviceauthcode'\];
authRequest.forceAuthorization = true;
authRequest.state = util.generateRandomUUID(); // You are advised to use **generateRandomUUID** to generate a state.
authRequest.idTokenSignAlgorithm = authentication.IdTokenSignAlgorithm.PS256;

// Execute the authorization request and process the result.
try {
  // The following provides only code snippets. Use it in the custom component instance to obtain the **UIContext** object as the input parameter of the function.
  const controller = new authentication.AuthenticationController(this.getUIContext().getHostContext());
  controller.executeRequest(authRequest, (error: BusinessError<Object>, data) => {
    if (error) {
      dealAllError(error);
      return;
    }
    const authorizationWithHuaweiIDResponse = data as authentication.AuthorizationWithHuaweiIDResponse;
    const state = authorizationWithHuaweiIDResponse.state;
    if (state && authRequest.state !== state) {
      hilog.error(0x0000, 'testTag', \`Failed to authorize. The state is different, response state: ${state}\`);
      return;
    }
    hilog.info(0x0000, 'testTag', 'Succeeded in authentication.');
    const authorizationWithHuaweiIDCredential = authorizationWithHuaweiIDResponse?.data;
    const idToken = authorizationWithHuaweiIDCredential?.idToken;
    const code = authorizationWithHuaweiIDCredential?.authorizationCode;
    // Process the ID token and authorization code.
  });
} catch (error) {
  dealAllError(error);
}

// Handle the error.
function dealAllError(error: BusinessError<Object>): void {
  hilog.error(0x0000, 'testTag', \`Failed to obtain userInfo. Code: ${error.code}, message: ${error.message}\`);
  // In scenarios involving UI interactions, it is advised to guide users with the following error code prompts.
  if (error.code === ErrorCode.ERROR\_CODE\_LOGIN\_OUT) {
    // Not signed in with a HUAWEI ID. Sign in with a HUAWEI ID and try again.
  } else if (error.code === ErrorCode.ERROR\_CODE\_NETWORK\_ERROR) {
    // Network error. Check your network connection and try again.
  } else if (error.code === ErrorCode.ERROR\_CODE\_USER\_CANCEL) {
    // Authorization canceled.
  } else if (error.code === ErrorCode.ERROR\_CODE\_SYSTEM\_SERVICE) {
    // System error. Try again later.
  } else if (error.code === ErrorCode.ERROR\_CODE\_REQUEST\_REFUSE) {
    // Repeated request. No further action is needed.
  } else {
    // Failed to obtain your information. Please try again later.
  }
}

export enum ErrorCode {
  // The HUAWEI ID is not signed in.
  ERROR\_CODE\_LOGIN\_OUT = 1001502001,
  // Network error.
  ERROR\_CODE\_NETWORK\_ERROR = 1001502005,
  // Authorization canceled.
  ERROR\_CODE\_USER\_CANCEL = 1001502012,
  // System service error.
  ERROR\_CODE\_SYSTEM\_SERVICE = 12300001,
  // Repeated request.
  ERROR\_CODE\_REQUEST\_REFUSE = 1001500002
}

#### AuthorizationWithHuaweiIDCredential

Credential returned after successful authorization via Account Kit, which is used to obtain user information (avatar, nickname, anonymous mobile number, and others) and associate with a HUAWEI ID (through OpenID/UnionID).

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.Auth

**Start version**: 4.0.0(10)

| 
**Name**

 | 

**Type**

 | 

**Read-Only**

 | 

**Optional**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

authorizationCode

 | 

string

 | 

Yes

 | 

Yes

 | 

Authorization code. Temporary credential, which is used to obtain an access token. The temporary credential is valid for 5 minutes and can be used only once. The value contains 1 to 1024 characters.

**Return scenario**: This parameter is returned when the **serviceauthcode** parameter is passed to **permissions** of the [AuthorizationWithHuaweiIDRequest](#section12940173017165) API.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

 |
| 

idToken

 | 

string

 | 

Yes

 | 

Yes

 | 

ID token. It is a JWT character string that contains user information, which can be used to obtain some user information and verify signatures. The value contains 1 to 2048 characters.

**Return scenario**: This parameter is returned when the **idtoken** parameter is passed to **permissions** of the [AuthorizationWithHuaweiIDRequest](#section12940173017165) API.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

 |
| 

openID

 | 

string

 | 

Yes

 | 

Yes

 | 

OpenID, which represents the identity of a HUAWEI ID user when using different types of products. The same user has different OpenIDs for different apps. For details about the format requirements, please refer to [Formats of OpenID and UnionID](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/account-faq-9).

**Return scenario**: This parameter is returned by default.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

 |
| 

unionID

 | 

string

 | 

Yes

 | 

Yes

 | 

UnionID, which represents the identity of a HUAWEI ID user when using different products of the same developer. The same user has the same UnionID for different apps of the same developer. For details about the format requirements, please refer to [Formats of OpenID and UnionID](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/account-faq-9).

**Return scenario**: This parameter is returned by default.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

 |
| 

avatarUri

 | 

string

 | 

Yes

 | 

Yes

 | 

Avatar URL, which has a short validity period. You are advised to download and save the avatar before using it.

The value is not subject to length restrictions. Example: **https://_xxx/xxx_**

**Return scenario**: This parameter is returned when the **profile** parameter is passed to **scopes** of the [AuthorizationWithHuaweiIDRequest](#section12940173017165) API.

**Atomic service API**: This API can be used in atomic services since API version 6.0.0(20).

 |
| 

nickName

 | 

string

 | 

Yes

 | 

Yes

 | 

User nickname. The value contains 2 to 20 characters.

**Return scenario**: This parameter is returned when the **profile** parameter is passed to **scopes** of the [AuthorizationWithHuaweiIDRequest](#section12940173017165) API.

**Atomic service API**: This API can be used in atomic services since API version 6.0.0(20).

 |
| 

email

 | 

string

 | 

Yes

 | 

Yes

 | 

Email address of a user. The value contains 4 to 254 characters.

**Return scenario**: This parameter is returned when the **email** parameter is passed to **scopes** of the [AuthorizationWithHuaweiIDRequest](#section12940173017165) API.

NOTICE:

Atomic services do not support this parameter.

 |
| 

authorizedScopes

 | 

string\[\]

 | 

Yes

 | 

Yes

 | 

List of scopes that are successfully authorized. Upon successful authorization of the scopes, an authorization code will be returned, which can then be used to retrieve the corresponding user information.

**Return scenario**: **openid** is returned by default.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

 |
| 

extraInfo

 | 

Record<string, Object>

 | 

Yes

 | 

Yes

 | 

Extended information. The key can be **quickLoginAnonymousPhone** or **localNumberConsistency**.

If [code obfuscation](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/source-obfuscation-guide) has been enabled, the obfuscation trustlist needs to be configured to exclude the properties within it from being obfuscated.

**Return scenario**: This parameter is returned when extended request parameters (such as **quickLoginAnonymousPhone**) are passed to **scopes** of the [AuthorizationWithHuaweiIDRequest](#section12940173017165) API.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**Note**: In the one-tap sign-in scenario of a HUAWEI ID, you can use the **localNumberConsistency** parameter to obtain the comparison result between the mobile number bound to the HUAWEI ID and the mobile number of the local SIM card.

**true**: yes

**false**: no

NOTE:

If the user's device has no SIM cards, **false** will be returned.

As long as the mobile number of one of the device's SIM cards is the same as the passed one, **true** will be returned. Otherwise, **false** will be returned.

 |

**Example**:

import { authentication } from '@kit.AccountKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { util } from '@kit.ArkTS';
import { BusinessError } from '@kit.BasicServicesKit';

// Create an authorization request and set parameters.
const authRequest = new authentication.HuaweiIDProvider().createAuthorizationWithHuaweiIDRequest();
// **openid** is the default value and cannot be modified. To obtain other user information, pass the relevant scope. For details, please refer to the documentation of the **AuthorizationWithHuaweiIDRequest** class.
authRequest.scopes = \['openid'\];
authRequest.permissions = \['idtoken', 'serviceauthcode'\];
authRequest.forceAuthorization = true;
authRequest.state = util.generateRandomUUID(); // You are advised to use **generateRandomUUID** to generate a state.
authRequest.idTokenSignAlgorithm = authentication.IdTokenSignAlgorithm.PS256;

// Execute the authorization request and process the result.
try {
  // The following provides only code snippets. Use it in the custom component instance to obtain the **UIContext** object as the input parameter of the function.
  const controller = new authentication.AuthenticationController(this.getUIContext().getHostContext());
  controller.executeRequest(authRequest, (error: BusinessError<Object>, data) => {
    if (error) {
      dealAllError(error);
      return;
    }
    const authorizationWithHuaweiIDResponse = data as authentication.AuthorizationWithHuaweiIDResponse;
    const state = authorizationWithHuaweiIDResponse.state;
    if (state && authRequest.state !== state) {
      hilog.error(0x0000, 'testTag', \`Failed to authorize. The state is different, response state: ${state}\`);
      return;
    }
    hilog.info(0x0000, 'testTag', 'Succeeded in authentication.');
    const authorizationWithHuaweiIDCredential = authorizationWithHuaweiIDResponse?.data;
    const idToken = authorizationWithHuaweiIDCredential?.idToken;
    const code = authorizationWithHuaweiIDCredential?.authorizationCode;
    // Process the ID token and authorization code.
  });
} catch (error) {
  dealAllError(error);
}

// Handle the error.
function dealAllError(error: BusinessError<Object>): void {
  hilog.error(0x0000, 'testTag', \`Failed to obtain userInfo. Code: ${error.code}, message: ${error.message}\`);
  // In scenarios involving UI interactions, it is advised to guide users with the following error code prompts.
  if (error.code === ErrorCode.ERROR\_CODE\_LOGIN\_OUT) {
    // Not signed in with a HUAWEI ID. Sign in with a HUAWEI ID and try again.
  } else if (error.code === ErrorCode.ERROR\_CODE\_NETWORK\_ERROR) {
    // Network error. Check your network connection and try again.
  } else if (error.code === ErrorCode.ERROR\_CODE\_USER\_CANCEL) {
    // Authorization canceled.
  } else if (error.code === ErrorCode.ERROR\_CODE\_SYSTEM\_SERVICE) {
    // System error. Try again later.
  } else if (error.code === ErrorCode.ERROR\_CODE\_REQUEST\_REFUSE) {
    // Repeated request. No further action is needed.
  } else {
    // Failed to obtain your information. Please try again later.
  }
}

export enum ErrorCode {
  // The HUAWEI ID is not signed in.
  ERROR\_CODE\_LOGIN\_OUT = 1001502001,
  // Network error.
  ERROR\_CODE\_NETWORK\_ERROR = 1001502005,
  // Authorization canceled.
  ERROR\_CODE\_USER\_CANCEL = 1001502012,
  // System service error.
  ERROR\_CODE\_SYSTEM\_SERVICE = 12300001,
  // Repeated request.
  ERROR\_CODE\_REQUEST\_REFUSE = 1001500002
}

#### CancelAuthorizationRequest

Object for requesting to revoke authorization via Account Kit. It is used as a parameter for requesting to revoke HUAWEI ID authorization.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.Auth

**Start version**: 4.0.0(10)

**Inheritance**: **CancelAuthorizationRequest** inherits from [AuthenticationRequest](#section3118182610348).

| 
**Name**

 | 

**Type**

 | 

**Read-Only**

 | 

**Optional**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

state

 | 

string

 | 

No

 | 

Yes

 | 

**state** parameter in the request body. The value can contain digits (0–9), letters (a–z or A–Z), dots (.), colons (:), slashes (/), and underscores (\_). The length limit is 1 to 255 characters. The verification rule is ^\[0-9a-zA-Z:/\\.\\-\_\]{1,255}$.

This parameter will be compared with the **state** parameter in the response body to prevent cross-site attacks.

You are advised to use nonces and perform consistency verification. [util.generateRandomUUID()](../../../../application-framework/arkts/arkts-apis/ohos-util-util/document.md#utilgeneraterandomuuid9) is recommended.

 |

**Example**:

import { authentication } from '@kit.AccountKit';
import { util } from '@kit.ArkTS';

const cancelRequest = new authentication.HuaweiIDProvider().createCancelAuthorizationRequest();
cancelRequest.state = util.generateRandomUUID(); // You are advised to use **generateRandomUUID** to generate a state.

#### CancelAuthorizationResponse

Response result of revoking a HUAWEI ID authorization request.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.Auth

**Start version**: 4.0.0(10)

**Inheritance**: **CancelAuthorizationResponse** inherits from [AuthenticationResponse](#section2697164193515).

**Parameters**:

| 
**Name**

 | 

**Type**

 | 

**Read-Only**

 | 

**Optional**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

state

 | 

string

 | 

Yes

 | 

Yes

 | 

**state** parameter returned in the response body. The value can contain digits (0–9), letters (a–z or A–Z), dots (.), colons (:), slashes (/), and underscores (\_). The length limit is 1 to 255 characters. The verification rule is ^\[0-9a-zA-Z:/\\.\\-\_\]{1,255}$.

This parameter will be compared with the **state** parameter in the request body to prevent cross-site attacks.

 |

**Example**:

import { authentication } from '@kit.AccountKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { util } from '@kit.ArkTS';
import { BusinessError } from '@kit.BasicServicesKit';

// Create an authorization revoking request and set parameters.
const cancelRequest = new authentication.HuaweiIDProvider().createCancelAuthorizationRequest();
cancelRequest.state = util.generateRandomUUID(); // You are advised to use **generateRandomUUID** to generate a state.

// Execute the authorization revoking request and process the result.
try {
  // The following provides only code snippets. Use it in the custom component instance to obtain the **UIContext** object as the input parameter of the function.
  const controller = new authentication.AuthenticationController(this.getUIContext().getHostContext());
  controller.executeRequest(cancelRequest, (error: BusinessError<Object>, data) => {
    if (error) {
      dealAllError(error);
      return;
    }
    const cancelAuthorizationResponse = data as authentication.CancelAuthorizationResponse;
    const state = cancelAuthorizationResponse.state;
    if (state && cancelRequest.state !== state) {
      hilog.error(0x0000, 'testTag', \`Failed to cancel. The state is different, response state: ${state}\`);
      return;
    }
    hilog.info(0x0000, 'testTag', 'Succeeded in canceling.');
  });
} catch (error) {
  dealAllError(error);
}

// Handle the error.
function dealAllError(error: BusinessError<Object>): void {
  hilog.error(0x0000, 'testTag', \`Failed to cancel. Code: ${error.code}, message: ${error.message}\`);
  // In sign-in scenarios involving UI interactions, it is advised to guide users with the following error code prompts:
  if (error.code === ErrorCode.ERROR\_CODE\_LOGIN\_OUT) {
    // HUAWEI ID not signed in. Use a HUAWEI ID to sign in and try again, or sign in to the app in another way.
  } else if (error.code === ErrorCode.ERROR\_CODE\_NETWORK\_ERROR) {
    // A network exception occurs. Check the current network status and try again, or sign in to the app in another way.
  } else if (error.code === ErrorCode.ERROR\_CODE\_INTERNAL\_ERROR) {
    // Failed to sign in. Try another way.
  } else if (error.code === ErrorCode.ERROR\_CODE\_USER\_CANCEL) {
    // Authorization canceled.
  } else if (error.code === ErrorCode.ERROR\_CODE\_SYSTEM\_SERVICE) {
    // System service exception. Try again later or sign in to the app in another way.
  } else if (error.code === ErrorCode.ERROR\_CODE\_REQUEST\_REFUSE) {
    // Repeated request. No further action is needed.
  } else {
    // Failed to sign in. Try another way.
  }
}

export enum ErrorCode {
  // The HUAWEI ID is not signed in.
  ERROR\_CODE\_LOGIN\_OUT = 1001502001,
  // Network error.
  ERROR\_CODE\_NETWORK\_ERROR = 1001502005,
  // Internal error.
  ERROR\_CODE\_INTERNAL\_ERROR = 1001502009,
  // Authorization canceled.
  ERROR\_CODE\_USER\_CANCEL = 1001502012,
  // System service error.
  ERROR\_CODE\_SYSTEM\_SERVICE = 12300001,
  // Repeated request.
  ERROR\_CODE\_REQUEST\_REFUSE = 1001500002
}

#### AuthenticationErrorCode

Error codes for the sign-in, authorization, and authorization revoking APIs. Process errors according to the error codes listed in the table below.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.Auth

**Start version**: 4.0.0(10)

| 
**Name**

 | 

**Value**

 | 

**Description**

 |
| :-- | :-- | :-- |
| 

PACKAGE\_FINGERPRINT\_CHECK\_ERROR

 | 

[1001500001](../../arkts-error-codes/document.md#section1581681312511)

 | 

The certificate fingerprint of the app fails to be verified.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

 |
| 

DUPLICATE\_REQUEST\_REJECTED

 | 

[1001500002](../../arkts-error-codes/document.md#section134761318124311)

 | 

Repeated request. No operation is needed to address this error code. Your app needs to implement tap control to prevent consecutive taps from initiating the same request.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

 |
| 

SCOPE\_OR\_PERRMISSION\_UNSUPPORTED

 | 

[1001500003](../../arkts-error-codes/document.md#section116574197436)

 | 

The scopes or permissions are not supported.

**Start version**: 5.0.0(12)

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

 |
| 

UNSUPPORTED

 | 

[1001500004](../../arkts-error-codes/document.md#section13107132603718)

 | 

This function is unavailable for the HUAWEI ID already signed in.

**Start version**: 5.0.0(12)

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

 |
| 

REQUEST\_RESTRICTED

 | 

[1001500005](../../arkts-error-codes/document.md#section612754419379)

 | 

This function is restricted.

**Start version**: 5.0.0(12)

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

 |
| 

ACCOUNT\_NOT\_LOGGED\_IN

 | 

[1001502001](../../arkts-error-codes/document.md#section539558125020)

 | 

The user has not signed in with their HUAWEI ID.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

 |
| 

APP\_NOT\_AUTHORIZED

 | 

[1001502002](../../arkts-error-codes/document.md#section1393125918588)

 | 

The app is not authorized.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

 |
| 

PARAMETER\_INVALID

 | 

[1001502003](../../arkts-error-codes/document.md#section289120911112)

 | 

Invalid input parameter value.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

 |
| 

NETWORK\_ERROR

 | 

[1001502005](../../arkts-error-codes/document.md#section1281526328)

 | 

Network error.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

 |
| 

INTERNAL\_ERROR

 | 

[1001502009](../../arkts-error-codes/document.md#section17561151616317)

 | 

Internal errors, such as Account Kit server errors.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

 |
| 

USER\_CANCELED

 | 

[1001502012](../../arkts-error-codes/document.md#section223413481361)

 | 

The user revokes authorization.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

 |
| 

SCOPE\_OR\_PERMISSION\_NOT\_REQUESTED

 | 

[1001502014](../../arkts-error-codes/document.md#section78953611814)

 | 

The app does not have the required scopes or permissions.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

 |

#### AuthenticationController

Controller for Account Kit-based sign-in, authorization, and authorization revoking requests. It is used to execute the method for requesting sign-in authorization.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.Auth

**Start version**: 4.0.0(10)

#### \[h2\]constructor

constructor(context?: common.Context)

Constructor, which constructs the **Controller** instance for Account Kit-based sign-in, authorization, and other requests.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.Auth

**Start version**: 4.0.0(10)

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

context

 | 

[common.Context](../../../../application-framework/ability-kit/arkts-apis/stage-model/ohos-app-ability-common-ability-common-module/document.md#context)

 | 

No

 | 

Context. This parameter is mandatory when the HUAWEI ID sign-in and authorization screens need to be started. Otherwise, error [401](../../../../api-reference-overview/universal-error-codes/document.md#section401-parameter-check-failed) will be returned.

Contexts supported by apps: [UIAbilityContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md) and [UIExtensionContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiextensioncontext/document.md). Apps cannot use [UIExtensionContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiextensioncontext/document.md) in non-full-screen components such as semi-modal, pop-up, and sub-window components.

Contexts supported by atomic services: [UIAbilityContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md)

NOTE:

-   In version 4.0.0(10), the parameter type is [UIAbilityContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md).
-   In 4.1.0(11) and later versions, the parameter type is [Context](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md).

 |

**Example**:

import { authentication } from '@kit.AccountKit';

// The following provides only code snippets. Use it in the custom component instance to obtain the **UIContext** object as the input parameter of the function.
const controller = new authentication.AuthenticationController(this.getUIContext().getHostContext());

#### \[h2\]executeRequest

executeRequest(request: AuthenticationRequest, callback: AsyncCallback<AuthenticationResponse, Record<string, Object>>): void

Executes requests (such as sign-in and authorization) of Account Kit. This API returns the result asynchronously through a callback. It is used to request sign-in and authorization, or revoke authorization from a HUAWEI ID.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.Auth

**Start version**: 4.0.0(10)

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

request

 | 

[AuthenticationRequest](#section3118182610348)

 | 

Yes

 | 

Request body for sign-in authorization and verification.

If this parameter is not passed as expected, error [401](../../../../api-reference-overview/universal-error-codes/document.md#section401-parameter-check-failed) will be returned, indicating a parameter error.

 |
| 

callback

 | 

AsyncCallback<[AuthenticationResponse](#section2697164193515), Record<string, Object>>

 | 

Yes

 | 

Sign-in authorization callback.

If the response data is successfully retrieved, **err** is **undefined** and **data** is the obtained [AuthenticationResponse](#section2697164193515) object. Otherwise, an error object will be returned.

If this parameter is not passed as expected, error [401](../../../../api-reference-overview/universal-error-codes/document.md#section401-parameter-check-failed) will be returned, indicating a parameter error.

 |

**Error codes**:

For details about the error codes, please refer to [Account Management Error Codes](../../../../system/basic-functions/basic-services-kit/error-codes/account-management-error-codes/document.md) and [ArkTS Error Codes](../../arkts-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

[401](../../../../api-reference-overview/universal-error-codes/document.md#section401-parameter-check-failed)

 | 

Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.

 |
| 

[12300001](../../../../system/basic-functions/basic-services-kit/error-codes/account-management-error-codes/document.md#section12300001-system-service-abnormal)

 | 

System service works abnormally.

 |
| 

[1001502001](../../arkts-error-codes/document.md#section539558125020)

 | 

The user has not logged in with HUAWEI ID.

 |
| 

[1001502002](../../arkts-error-codes/document.md#section1393125918588)

 | 

The application is not authorized.

 |
| 

[1001502003](../../arkts-error-codes/document.md#section289120911112)

 | 

Invalid input parameter value.

 |
| 

[1001502005](../../arkts-error-codes/document.md#section1281526328)

 | 

Network error.

 |
| 

[1001502009](../../arkts-error-codes/document.md#section17561151616317)

 | 

Internal error.

 |
| 

[1001500001](../../arkts-error-codes/document.md#section1581681312511)

 | 

Failed to check the fingerprint of the app bundle.

 |
| 

[1001502012](../../arkts-error-codes/document.md#section223413481361)

 | 

The user canceled the authorization.

 |
| 

[1001502014](../../arkts-error-codes/document.md#section78953611814)

 | 

The app does not have the required scopes or permissions.

 |
| 

[1001500002](../../arkts-error-codes/document.md#section134761318124311)

 | 

This error code is reported when a request is already being processed.

 |
| 

[1001500003](../../arkts-error-codes/document.md#section116574197436)

 | 

The scopes or permissions are not supported.

 |

**Example**:

import { authentication } from '@kit.AccountKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { util } from '@kit.ArkTS';
import { BusinessError } from '@kit.BasicServicesKit';

// Create an authorization request and set parameters.
const authRequest = new authentication.HuaweiIDProvider().createAuthorizationWithHuaweiIDRequest();
// **openid** is the default value and cannot be modified. To obtain other user information, pass the relevant scope. For details, please refer to the documentation of the **AuthorizationWithHuaweiIDRequest** class.
authRequest.scopes = \['openid'\];
authRequest.permissions = \['idtoken', 'serviceauthcode'\];
authRequest.forceAuthorization = true;
authRequest.state = util.generateRandomUUID(); // You are advised to use **generateRandomUUID** to generate a state.
authRequest.idTokenSignAlgorithm = authentication.IdTokenSignAlgorithm.PS256;

// Execute the authorization request and process the result.
try {
  // The following provides only code snippets. Use it in the custom component instance to obtain the **UIContext** object as the input parameter of the function.
  const controller = new authentication.AuthenticationController(this.getUIContext().getHostContext());
  controller.executeRequest(authRequest, (error: BusinessError<Object>, data) => {
    if (error) {
      dealAllError(error);
      return;
    }
    const authorizationWithHuaweiIDResponse = data as authentication.AuthorizationWithHuaweiIDResponse;
    const state = authorizationWithHuaweiIDResponse.state;
    if (state && authRequest.state !== state) {
      hilog.error(0x0000, 'testTag', \`Failed to authorize. The state is different, response state: ${state}\`);
      return;
    }
    hilog.info(0x0000, 'testTag', 'Succeeded in authentication.');
    const authorizationWithHuaweiIDCredential = authorizationWithHuaweiIDResponse?.data;
    const idToken = authorizationWithHuaweiIDCredential?.idToken;
    const code = authorizationWithHuaweiIDCredential?.authorizationCode;
    // Process the ID token and authorization code.
  });
} catch (error) {
  dealAllError(error);
}

// Handle the error.
function dealAllError(error: BusinessError<Object>): void {
  hilog.error(0x0000, 'testTag', \`Failed to obtain userInfo. Code: ${error.code}, message: ${error.message}\`);
  // In scenarios involving UI interactions, it is advised to guide users with the following error code prompts.
  if (error.code === ErrorCode.ERROR\_CODE\_LOGIN\_OUT) {
    // Not signed in with a HUAWEI ID. Sign in with a HUAWEI ID and try again.
  } else if (error.code === ErrorCode.ERROR\_CODE\_NETWORK\_ERROR) {
    // Network error. Check your network connection and try again.
  } else if (error.code === ErrorCode.ERROR\_CODE\_USER\_CANCEL) {
    // Authorization canceled.
  } else if (error.code === ErrorCode.ERROR\_CODE\_SYSTEM\_SERVICE) {
    // System error. Try again later.
  } else if (error.code === ErrorCode.ERROR\_CODE\_REQUEST\_REFUSE) {
    // Repeated request. No further action is needed.
  } else {
    // Failed to obtain your information. Please try again later.
  }
}

export enum ErrorCode {
  // The HUAWEI ID is not signed in.
  ERROR\_CODE\_LOGIN\_OUT = 1001502001,
  // Network error.
  ERROR\_CODE\_NETWORK\_ERROR = 1001502005,
  // Authorization canceled.
  ERROR\_CODE\_USER\_CANCEL = 1001502012,
  // System service error.
  ERROR\_CODE\_SYSTEM\_SERVICE = 12300001,
  // Repeated request.
  ERROR\_CODE\_REQUEST\_REFUSE = 1001500002
}

#### \[h2\]executeRequest

executeRequest(request: AuthenticationRequest): Promise<AuthenticationResponse>

Executes Account Kit-based sign-in, authorization, and other requests. This API returns the result asynchronously through a promise. It is used to request sign-in and authorization, or revoke authorization from a HUAWEI ID.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.Auth

**Start version**: 4.0.0(10)

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

request

 | 

[AuthenticationRequest](#section3118182610348)

 | 

Yes

 | 

Request body for sign-in authorization and verification. If this parameter is not passed as expected, error [401](../../../../api-reference-overview/universal-error-codes/document.md#section401-parameter-check-failed) will be returned, indicating a parameter error.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[AuthenticationResponse](#section2697164193515)\>

 | 

**Promise** object for sign-in authorization. It is used to return the [AuthenticationResponse](#section2697164193515) object.

 |

**Error codes**:

For details about the error codes, please refer to [Account Management Error Codes](../../../../system/basic-functions/basic-services-kit/error-codes/account-management-error-codes/document.md) and [ArkTS Error Codes](../../arkts-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

[401](../../../../api-reference-overview/universal-error-codes/document.md#section401-parameter-check-failed)

 | 

Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.

 |
| 

[12300001](../../../../system/basic-functions/basic-services-kit/error-codes/account-management-error-codes/document.md#section12300001-system-service-abnormal)

 | 

System service works abnormally.

 |
| 

[1001502001](../../arkts-error-codes/document.md#section539558125020)

 | 

The user has not logged in with HUAWEI ID.

 |
| 

[1001502002](../../arkts-error-codes/document.md#section1393125918588)

 | 

The application is not authorized.

 |
| 

[1001502003](../../arkts-error-codes/document.md#section289120911112)

 | 

Invalid input parameter value.

 |
| 

[1001502005](../../arkts-error-codes/document.md#section1281526328)

 | 

Network error.

 |
| 

[1001502009](../../arkts-error-codes/document.md#section17561151616317)

 | 

Internal error.

 |
| 

[1001500001](../../arkts-error-codes/document.md#section1581681312511)

 | 

Failed to check the fingerprint of the app bundle.

 |
| 

[1001502012](../../arkts-error-codes/document.md#section223413481361)

 | 

The user canceled the authorization.

 |
| 

[1001502014](../../arkts-error-codes/document.md#section78953611814)

 | 

The app does not have the required scopes or permissions.

 |
| 

[1001500002](../../arkts-error-codes/document.md#section134761318124311)

 | 

This error code is reported when a request is already being processed.

 |
| 

[1001500003](../../arkts-error-codes/document.md#section116574197436)

 | 

The scopes or permissions are not supported.

 |

**Example**:

import { authentication } from '@kit.AccountKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { util } from '@kit.ArkTS';
import { BusinessError } from '@kit.BasicServicesKit';

// Create an authorization request and set parameters.
const authRequest = new authentication.HuaweiIDProvider().createAuthorizationWithHuaweiIDRequest();
// **openid** is the default value and cannot be modified. To obtain other user information, pass the relevant scope. For details, please refer to the documentation of the **AuthorizationWithHuaweiIDRequest** class.
authRequest.scopes = \['openid'\];
authRequest.permissions = \['idtoken', 'serviceauthcode'\];
authRequest.forceAuthorization = true;
authRequest.state = util.generateRandomUUID(); // You are advised to use **generateRandomUUID** to generate a state.
authRequest.idTokenSignAlgorithm = authentication.IdTokenSignAlgorithm.PS256;

// Execute the authorization request and process the result.
try {
  // The following provides only code snippets. Use it in the custom component instance to obtain the **UIContext** object as the input parameter of the function.
  const controller = new authentication.AuthenticationController(this.getUIContext().getHostContext());
  controller.executeRequest(authRequest).then((data) => {
    const authorizationWithHuaweiIDResponse = data as authentication.AuthorizationWithHuaweiIDResponse;
    const state = authorizationWithHuaweiIDResponse.state;
    if (state && authRequest.state !== state) {
      hilog.error(0x0000, 'testTag', \`Failed to authorize. The state is different, response state: ${state}\`);
      return;
    }
    hilog.info(0x0000, 'testTag', 'Succeeded in authentication.');
    const authorizationWithHuaweiIDCredential = authorizationWithHuaweiIDResponse?.data;
    const idToken = authorizationWithHuaweiIDCredential?.idToken;
    const code = authorizationWithHuaweiIDCredential?.authorizationCode;
    // Process the ID token and authorization code.
  }).catch((err: BusinessError) => {
    dealAllError(err);
  });
} catch (error) {
  dealAllError(error);
}

// Handle the error.
function dealAllError(error: BusinessError): void {
  hilog.error(0x0000, 'testTag', \`Failed to obtain userInfo. Code: ${error.code}, message: ${error.message}\`);
  // In scenarios involving UI interactions, it is advised to guide users with the following error code prompts.
  if (error.code === ErrorCode.ERROR\_CODE\_LOGIN\_OUT) {
    // Not signed in with a HUAWEI ID. Sign in with a HUAWEI ID and try again.
  } else if (error.code === ErrorCode.ERROR\_CODE\_NETWORK\_ERROR) {
    // Network error. Check your network connection and try again.
  } else if (error.code === ErrorCode.ERROR\_CODE\_USER\_CANCEL) {
    // Authorization canceled.
  } else if (error.code === ErrorCode.ERROR\_CODE\_SYSTEM\_SERVICE) {
    // System error. Try again later.
  } else if (error.code === ErrorCode.ERROR\_CODE\_REQUEST\_REFUSE) {
    // Repeated request. No further action is needed.
  } else {
    // Failed to obtain your information. Please try again later.
  }
}

export enum ErrorCode {
  // The HUAWEI ID is not signed in.
  ERROR\_CODE\_LOGIN\_OUT = 1001502001,
  // Network error.
  ERROR\_CODE\_NETWORK\_ERROR = 1001502005,
  // Authorization canceled.
  ERROR\_CODE\_USER\_CANCEL = 1001502012,
  // System service error.
  ERROR\_CODE\_SYSTEM\_SERVICE = 12300001,
  // Repeated request.
  ERROR\_CODE\_REQUEST\_REFUSE = 1001500002
}

#### AuthenticationRequest

Parent object for requesting HUAWEI ID sign-in authorization and verification.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.Auth

**Start version**: 4.0.0(10)

#### AuthenticationResponse

Parent object for responding to the HUAWEI ID sign-in authorization and verification request.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.Auth

**Start version**: 4.0.0(10)

#### AuthenticationProvider

Parent provider object for requesting HUAWEI ID sign-in authorization and verification.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.Auth

**Start version**: 4.0.0(10)

#### IdType

Enumeration object of ID types. It is used as the parameter for requesting the HUAWEI ID sign-in status.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.Auth

**Start version**: 5.0.0(12)

| 
**Name**

 | 

**Value**

 | 

**Description**

 |
| :-- | :-- | :-- |
| 

USER\_ID

 | 

1

 | 

UID of a HUAWEI ID user.

NOTE:

This parameter is available only to system apps.

 |
| 

OPEN\_ID

 | 

2

 | 

OpenID of a HUAWEI ID user. For details about the format requirements, please refer to [Formats of OpenID and UnionID](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/account-faq-9).

 |
| 

UNION\_ID

 | 

3

 | 

UnionID of a HUAWEI ID user. For details about the format requirements, please refer to [Formats of OpenID and UnionID](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/account-faq-9).

 |

#### State

Enumeration object of HUAWEI ID sign-in statuses. It is used to save the sign-in status of a HUAWEI ID.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.Auth

**Start version**: 5.0.0(12)

| 
**Name**

 | 

**Value**

 | 

**Description**

 |
| :-- | :-- | :-- |
| 

UNLOGGED\_IN

 | 

0

 | 

No HUAWEI ID is signed in.

 |
| 

AUTHORIZED

 | 

1

 | 

A HUAWEI ID has signed in, and the UnionID/OpenID of the passed HUAWEI ID is the same as those of the current HUAWEI ID.

 |
| 

UNAUTHORIZED

 | 

2

 | 

A HUAWEI ID has signed in, but the UnionID/OpenID of the passed HUAWEI ID is different from those of the current HUAWEI ID.

 |

#### StateRequest

Object for requesting the HUAWEI ID sign-in status. It is used as a parameter passed to [getHuaweiIDState](#section102884586336).

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.Auth

**Start version**: 5.0.0(12)

| 
**Name**

 | 

**Type**

 | 

**Read-Only**

 | 

**Optional**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

idType

 | 

[IdType](#section13891254145017)

 | 

No

 | 

No

 | 

ID type of **idValue**. Currently, non-system apps can only pass a UnionID or an OpenID.

 |
| 

idValue

 | 

string

 | 

No

 | 

No

 | 

UnionID or OpenID obtained by a user. The type passed is defined by **idType**. The parameter cannot be empty. Otherwise, error [1001502003 Invalid Input Parameter Value](../../arkts-error-codes/document.md#section289120911112) will be reported. The value contains 1 to 256 characters.

The UnionID and OpenID can be obtained through the [LoginWithHuaweiIDResponse](#section15454203811311), [AuthorizationWithHuaweiIDResponse](#section10418450161620), [LoginPanel](../../arkts-components/loginpanel-huawei-id-sign-in-panel-component/document.md#section72281234181611), or [LoginWithHuaweiIDButton](../../arkts-components/loginwithhuaweiidbutton-huawei-id-sign-in-button-component/document.md#section1624716107193) API. For details, please refer to the relevant sample code.

 |

**Example**:

import { authentication } from '@kit.AccountKit';

// Create request parameters.
const request: authentication.StateRequest = {
  idType: authentication.IdType.UNION\_ID,
  idValue: '_xxx_' // The value can be obtained through the HUAWEI ID sign-in API.
}

#### StateResult

Result object for obtaining the HUAWEI ID sign-in status.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.Auth

**Start version**: 5.0.0(12)

| 
**Name**

 | 

**Type**

 | 

**Read-Only**

 | 

**Optional**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

state

 | 

[State](#section1687013712515)

 | 

No

 | 

No

 | 

Enumeration object of HUAWEI ID sign-in statuses. It is used to save the sign-in status of a HUAWEI ID.

 |

**Example**:

import { authentication } from '@kit.AccountKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Create request parameters.
const stateRequest: authentication.StateRequest = {
  idType: authentication.IdType.UNION\_ID,
  idValue: '_xxx_' // The value can be obtained through the HUAWEI ID sign-in API.
}
try {
  // Execute the request for obtaining the HUAWEI ID sign-in status and process the result.
  new authentication.HuaweiIDProvider().getHuaweiIDState(stateRequest).then((data: authentication.StateResult) => {
    hilog.info(0x0000, 'testTag', 'Succeeded in getting huaweiIdState result.');
    const state = data.state;
    // Process the state.
  }).catch((err: BusinessError) => {
    dealAllError(err);
  })
} catch (error) {
  dealAllError(error);
}

// Handle the error.
function dealAllError(error: BusinessError): void {
  hilog.error(0x0000, 'testTag', \`Failed to getHuaweiIdState, errorCode=${error.code}, errorMsg=${error.message}\`);
}

#### ConsistencyState

Enumeration object of mobile number consistency statuses. You can perform risk control based on the result.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.Auth

**Start version**: 5.0.0(12)

| 
**Name**

 | 

**Value**

 | 

**Description**

 |
| :-- | :-- | :-- |
| 

CONSISTENT

 | 

0

 | 

A HUAWEI ID has signed in, and the passed mobile number is the same as that bound to the HUAWEI ID and also the same as the mobile number of any SIM card in the current device.

 |
| 

INCONSISTENT\_WITH\_DEVICES

 | 

1

 | 

A HUAWEI ID has signed in, and the passed mobile number is the same as that bound to the HUAWEI ID but different from the mobile number of the device's SIM card, or the current device does not have a SIM card.

 |
| 

INCONSISTENT

 | 

2

 | 

A HUAWEI ID has signed in, but the passed mobile number is different from that bound to the HUAWEI ID.

 |

#### ConsistencyRequest

Request object for obtaining the mobile number consistency status.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.Auth

**Start version**: 5.0.0(12)

| 
**Name**

 | 

**Type**

 | 

**Read-Only**

 | 

**Optional**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

idType

 | 

[IdType](#section13891254145017)

 | 

No

 | 

No

 | 

ID type of **idValue**. Currently, non-system apps can only pass a UnionID or an OpenID.

 |
| 

idValue

 | 

string

 | 

No

 | 

No

 | 

UnionID or OpenID of a user. The value is mandatory and contains 1 to 256 characters. The type of **idValue** is defined by **idType**.

The UnionID and OpenID can be obtained through the [LoginWithHuaweiIDResponse](#section15454203811311), [AuthorizationWithHuaweiIDResponse](#section10418450161620), [LoginPanel](../../arkts-components/loginpanel-huawei-id-sign-in-panel-component/document.md#section72281234181611), or [LoginWithHuaweiIDButton](../../arkts-components/loginwithhuaweiidbutton-huawei-id-sign-in-button-component/document.md#section1624716107193) API. For details, please refer to the relevant sample code.

 |
| 

mobileNumber

 | 

string

 | 

No

 | 

No

 | 

Mobile number obtained through the one-tap sign-in function of the [LoginWithHuaweiIDButton](../../arkts-components/loginwithhuaweiidbutton-huawei-id-sign-in-button-component/document.md#section1624716107193) component. The country/region code must be added to the passed mobile number (for example, "+86" for mobile numbers registered in the Chinese mainland). The value is mandatory and contains 1 to 256 characters.

Example: +86xxxxxxxxxxx (plaintext mobile number)

 |

**Example**:

import { authentication } from '@kit.AccountKit';

// Create request parameters.
const request: authentication.ConsistencyRequest = {
  idType: authentication.IdType.UNION\_ID,
  idValue: '_xxx_', // The value can be obtained through the HUAWEI ID sign-in API.
  mobileNumber: '+86xxxxxxxxxxx' // Mobile number in plaintext obtained through the one-tap HUAWEI ID sign-in function.
}

#### ConsistencyResult

Result object for obtaining the mobile number consistency status. You can perform risk control based on the result.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.Auth

**Start version**: 5.0.0(12)

| 
**Name**

 | 

**Type**

 | 

**Read-Only**

 | 

**Optional**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

state

 | 

[ConsistencyState](#section1271024585118)

 | 

No

 | 

No

 | 

Enumeration object of mobile number consistency statuses.

 |

**Example**:

import { authentication } from '@kit.AccountKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Create request parameters.
const consistencyRequest: authentication.ConsistencyRequest = {
  idType: authentication.IdType.UNION\_ID,
  idValue: ''_xxx_', // The value can be obtained through the HUAWEI ID sign-in API.
  mobileNumber: '+86xxxxxxxxxxx' // Mobile number in plaintext obtained through the one-tap HUAWEI ID sign-in function.
}
try {
  // Execute the request for obtaining the mobile number consistency status and process the result.
  new authentication.HuaweiIDProvider().getMobileNumberConsistency(consistencyRequest)
    .then((data: authentication.ConsistencyResult) => {
      hilog.info(0x0000, 'testTag', \`Succeeded in getting getMobileNumberConsistency result = ${data.state}\`);
      const state = data.state;
      // Process the state.
    })
    .catch((err: BusinessError) => {
      dealAllError(err);
    })
} catch (error) {
  dealAllError(error);
}

// Handle the error.
function dealAllError(error: BusinessError): void {
  hilog.error(0x0000, 'testTag',
    \`Failed to get mobileNumberConsistency, errorCode=${error.code}, errorMsg=${error.message}\`);
}
