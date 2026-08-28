# @ohos.userIAM.userAuth (User Authentication)

The **userAuth** module provides APIs for user authentication, which applies to scenarios such as device unlocking, payment, and application login.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/x6D2Czo8RGqtOf5mAAPLgA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062340Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=98AA1336FB828E36C3D785829AF1DE461D6E8FF04112A70D868727ADB3B3F364)

The initial APIs of this module are supported since API version 6. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { userAuth } from '@kit.UserAuthenticationKit';

#### Constant

**System capability**: SystemCapability.UserIAM.UserAuth.Core

| Name | Type | Value | Description |
| :-- | :-- | :-- | :-- |
| MAX\_ALLOWABLE\_REUSE\_DURATION12+ | number | 300000 | 
Maximum reuse duration of the unlock authentication result, in milliseconds. The value is **300000**.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| PERMANENT\_LOCKOUT\_DURATION22+ | number | 0x7fffffff | 

Permanent lockout duration, in milliseconds. The value is **0x7fffffff**.

**Atomic service API**: This API can be used in atomic services since API version 22.

 |

#### AuthLockState22+

Enumerates the lockout status of an identity authentication type.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.UserIAM.UserAuth.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| isLocked | boolean | No | No | Whether the authentication is locked. **true** means yes; **false** otherwise. |
| remainingAuthAttempts | number | No | No | Number of remaining attempts before the authentication is locked. The maximum value is **5**. |
| lockoutDuration | number | No | No | 
Remaining lockout duration, in milliseconds.

If the authentication is permanently locked, the value is **PERMANENT\_LOCKOUT\_DURATION**. You need to unlock it using the PIN.

 |

#### UserAuthTipCode20+

Enumerates the intermediate states of identity authentication.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.UserIAM.UserAuth.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| COMPARE\_FAILURE | 1 | The authentication failed. |
| TIMEOUT | 2 | The authentication has timed out. |
| TEMPORARILY\_LOCKED | 3 | The authentication is temporarily locked. |
| PERMANENTLY\_LOCKED | 4 | The authentication is permanently locked. |
| WIDGET\_LOADED | 5 | The identity authentication page is loaded. |
| WIDGET\_RELEASED | 6 | The current identity authentication page is switched to another authentication page or the identity authentication component is closed. |
| COMPARE\_FAILURE\_WITH\_FROZEN | 7 | Authentication is locked after a failed attempt. |

#### EnrolledState12+

Represents the state of a credential enrolled.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.UserIAM.UserAuth.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| credentialDigest | number | No | No | Credential digest, which is randomly generated when a credential is added. |
| credentialCount | number | No | No | Number of enrolled credentials. |

#### ReuseMode12+

Enumerates the modes for reusing authentication results.

**System capability**: SystemCapability.UserIAM.UserAuth.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| AUTH\_TYPE\_RELEVANT | 1 | 
The device unlock authentication result can be reused within the validity period if the authentication type matches any of the authentication types specified for this authentication.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| AUTH\_TYPE\_IRRELEVANT | 2 | 

The device unlock authentication result can be reused within the validity period regardless of the authentication type.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| CALLER\_IRRELEVANT\_AUTH\_TYPE\_RELEVANT14+ | 3 | 

Any identity authentication result (including device unlock authentication result) can be reused within the validity period if the authentication type matches any of the authentication types specified for this authentication.

**Atomic service API**: This API can be used in atomic services since API version 14.

 |
| CALLER\_IRRELEVANT\_AUTH\_TYPE\_IRRELEVANT14+ | 4 | 

Any identity authentication result (including device unlock authentication result) can be reused within the validity period regardless of the authentication type.

**Atomic service API**: This API can be used in atomic services since API version 14.

 |

#### ReuseUnlockResult12+

Represents information about the authentication result reuse.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/cmGIJfdDQLiAp63XmqQpKw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062340Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C6522497F606B6B545932CE98246A4AA8019E0650D4D1895D8E55F7C18165CB5)

If the credential changes within the reuse duration after a successful identity authentication (including device unlock authentication), the authentication result can still be reused and the actual **EnrolledState** is returned in the authentication result. If the credential used for the previous authentication has been deleted when the authentication result is used:

\- If the deleted credential is face or fingerprint, the authentication result can still be reused, but **credentialCount** and **credentialDigest** in the **EnrolledState** returned are both **0**.

\- If the deleted credential is a lock screen password, the reuse will fail.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.UserIAM.UserAuth.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| reuseMode | [ReuseMode](#reusemode12) | No | No | Authentication result reuse mode. |
| reuseDuration | number | No | No | Reuse duration of the authentication result, in milliseconds. The value must be greater than 0 and the maximum value is [MAX\_ALLOWABLE\_REUSE\_DURATION](#constant). |

#### userAuth.getAuthLockState22+

getAuthLockState(authType: UserAuthType): Promise<AuthLockState>

Queries the lockout state of the specified authentication type. This API uses a promise to return the result.

**Required permissions**: ohos.permission.ACCESS\_BIOMETRIC

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.UserIAM.UserAuth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| authType | [UserAuthType](#userauthtype8) | Yes | Authentication type. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[AuthLockState](#authlockstate22)\> | Promise used to return the result. An error is reported when the operation fails. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [User Authentication Error Codes](../../error-codes/user-authentication-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 12500002 | General operation error. |
| 12500005 | The authentication type is not supported. |
| 12500008 | The parameter is out of range. |
| 12500010 | The type of credential has not been enrolled. |

**Example**

import { userAuth } from '@kit.UserAuthenticationKit';
import { BusinessError } from '@kit.BasicServicesKit';

let queryType = userAuth.UserAuthType.PIN;
let authLockState : userAuth.AuthLockState = {
  isLocked : false,
  remainingAuthAttempts : 0,
  lockoutDuration : 0
}

userAuth.getAuthLockState(queryType)
  .then((result : userAuth.AuthLockState) => {
    authLockState = result;
    console.info(\`get auth lock state success, authLockState is: ${JSON.stringify(authLockState)}\`);
  })
  .catch((err : BusinessError) => {
    console.info(\`get auth lock state failed, err code is : ${err?.code}, err message is : ${err?.message}\`);
  })

#### userAuth.getEnrolledState12+

getEnrolledState(authType: UserAuthType): EnrolledState

Obtains the credential state.

**Required permissions**: ohos.permission.ACCESS\_BIOMETRIC

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.UserIAM.UserAuth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| authType | [UserAuthType](#userauthtype8) | Yes | Authentication type. |

**Return value**

| Type | Description |
| :-- | :-- |
| [EnrolledState](#enrolledstate12) | Credential state obtained if the operation is successful. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [User Authentication Error Codes](../../error-codes/user-authentication-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | 
Parameter error. Possible causes:

1.Mandatory parameters are left unspecified.

 |
| 12500002 | General operation error. |
| 12500005 | The authentication type is not supported. |
| 12500010 | The type of credential has not been enrolled. |

**Example**

import { userAuth } from '@kit.UserAuthenticationKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let enrolledState = userAuth.getEnrolledState(userAuth.UserAuthType.FACE);
  console.info(\`get current enrolled state success, enrolledState = ${JSON.stringify(enrolledState)}\`);
} catch (error) {
  const err: BusinessError = error as BusinessError;
  console.error(\`get current enrolled state failed, Code is ${err?.code}, message is ${err?.message}\`);
}

#### AuthParam10+

Defines the user authentication parameters.

**System capability**: SystemCapability.UserIAM.UserAuth.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| challenge | Uint8Array | No | No | 
Random challenge value, which can be used to prevent replay attacks. It cannot exceed 32 bytes and can be passed in **Uint8Array(\[\])** format.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| authType | [UserAuthType](#userauthtype8)\[\] | No | No | 

Authentication type list, which specifies the types of authentication provided on the user authentication page.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| authTrustLevel | [AuthTrustLevel](#authtrustlevel8) | No | No | 

Authentication trust level. For details, see [Principles for Classifying Biometric Authentication Trust Levels](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/user-authentication-overview#principles-for-classifying-biometric-authentication-trust-levels).

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| reuseUnlockResult12+ | [ReuseUnlockResult](#reuseunlockresult12) | No | Yes | 

Information about the authentication result reuse. By default, the result cannot be reused.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| skipLockedBiometricAuth20+ | boolean | No | Yes | 

Whether to skip the authentication mode that has been locked and automatically switch to another authentication mode. If no authentication mode can be switched to, the component is disabled and an authentication freezing error code is returned.

**true**: When biometric authentication is frozen, the system skips the countdown page and directly switches to another authentication mode.

**false** (default): The countdown page is not skipped.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |

#### WidgetParam10+

Represents the information presented on the user authentication page.

**System capability**: SystemCapability.UserIAM.UserAuth.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| title | string | No | No | 
Title of the user authentication page, which cannot be empty or exceed 500 characters. You are advised to set it to the authentication purpose, such as payment or application login.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| navigationButtonText | string | No | Yes | 

Text on the navigation button. It cannot exceed 60 characters. It is supported in single fingerprint or facial authentication before API version 18. Since API version 18, it is also supported in combined facial and fingerprint authentication. By default, the custom navigation button is not displayed.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| uiContext18+ | Context | No | Yes | 

Whether to display the authentication dialog box in modal application mode. This mode is applicable only to 2-in-1 devices. If this mode is not used or other types of devices are used, the authentication dialog box is displayed in modal system mode. By default, the identity authentication dialog box is displayed in modal system mode.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |

#### UserAuthResult10+

Represents the user authentication result. If the authentication is successful, the authentication type and token information are returned.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.UserIAM.UserAuth.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| result | number | No | No | User authentication result. If the authentication is successful, **SUCCESS** is returned. Otherwise, an error code is returned. For details, see [UserAuthResultCode](#userauthresultcode9). |
| token | Uint8Array | No | Yes | Authentication token information. The value can contain a maximum of 1024 bytes. |
| authType | [UserAuthType](#userauthtype8) | No | Yes | Authentication type. |
| enrolledState12+ | [EnrolledState](#enrolledstate12) | No | Yes | Credential state. |

#### IAuthCallback10+

Provides callbacks to return the authentication result.

#### \[h2\]onResult10+

onResult(result: UserAuthResult): void

Called to return the authentication result. If the authentication is successful, **UserAuthResult** contains the token information.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.UserIAM.UserAuth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| result | [UserAuthResult](#userauthresult10) | Yes | Authentication result. |

**Example 1**

Initiate a lock screen password authentication request at ATL3 or higher.

import { BusinessError } from '@kit.BasicServicesKit';
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { userAuth } from '@kit.UserAuthenticationKit';

try {
  const rand = cryptoFramework.createRandom();
  const len: number = 16;
  let randData: Uint8Array | null = null;
  let retryCount = 0;
  while(retryCount < 3){
    randData = rand?.generateRandomSync(len)?.data;
    if(randData){
      break;
    }
    retryCount++;
  }
  if(!randData){
    return;
  }
  const authParam: userAuth.AuthParam = {
    challenge: randData,
    authType: \[userAuth.UserAuthType.PIN\],
    authTrustLevel: userAuth.AuthTrustLevel.ATL3,
  };
  const widgetParam: userAuth.WidgetParam = {
    title: 'Enter password',
  };

  const userAuthInstance = userAuth.getUserAuthInstance(authParam, widgetParam);
  console.info('get userAuth instance success');
  // The authentication result is returned by onResult only after the authentication is started by start() of UserAuthInstance.
  userAuthInstance.on('result', {
    onResult (result) {
      console.info(\`userAuthInstance callback result = ${JSON.stringify(result)}\`);
    }
  });
  console.info('auth on success');
  userAuthInstance.start();
  console.info('auth start success');
} catch (error) {
  const err: BusinessError = error as BusinessError;
  console.error(\`auth catch error. Code is ${err?.code}, message is ${err?.message}\`);
}

**Example 2**

Initiate a lock screen password authentication request at ATL3 or higher, and enable the authentication result to be reused for the same type of authentication within the maximum reuse duration of device unlocking.

import { BusinessError } from '@kit.BasicServicesKit';
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { userAuth } from '@kit.UserAuthenticationKit';

let reuseUnlockResult: userAuth.ReuseUnlockResult = {
  reuseMode: userAuth.ReuseMode.AUTH\_TYPE\_RELEVANT,
  reuseDuration: userAuth.MAX\_ALLOWABLE\_REUSE\_DURATION,
}
try {
  const rand = cryptoFramework.createRandom();
  const len: number = 16;
  let randData: Uint8Array | null = null;
  let retryCount = 0;
  while(retryCount < 3){
    randData = rand?.generateRandomSync(len)?.data;
    if(randData){
      break;
    }
    retryCount++;
  }
  if(!randData){
    return;
  }
  const authParam: userAuth.AuthParam = {
    challenge: randData,
    authType: \[userAuth.UserAuthType.PIN\],
    authTrustLevel: userAuth.AuthTrustLevel.ATL3,
    reuseUnlockResult: reuseUnlockResult,
  };
  const widgetParam: userAuth.WidgetParam = {
    title: 'Enter password',
  };
  const userAuthInstance = userAuth.getUserAuthInstance(authParam, widgetParam);
  console.info('get userAuth instance success');
  // The authentication result is returned by onResult only after the authentication is started by start() of UserAuthInstance.
  userAuthInstance.on('result', {
    onResult (result) {
      console.info(\`userAuthInstance callback result = ${JSON.stringify(result)}\`);
    }
  });
  console.info('auth on success');
  userAuthInstance.start();
  console.info('auth start success');
} catch (error) {
  const err: BusinessError = error as BusinessError;
  console.error(\`auth catch error. Code is ${err?.code}, message is ${err?.message}\`);
}

**Example 3**

Initiate a lock screen password authentication request at ATL3 or higher, and enable the authentication result to be reused for any type of authentication within the maximum reuse duration of any application.

import { BusinessError } from '@kit.BasicServicesKit';
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { userAuth } from '@kit.UserAuthenticationKit';

let reuseUnlockResult: userAuth.ReuseUnlockResult = {
  reuseMode: userAuth.ReuseMode.CALLER\_IRRELEVANT\_AUTH\_TYPE\_RELEVANT,
  reuseDuration: userAuth.MAX\_ALLOWABLE\_REUSE\_DURATION,
}
try {
  const rand = cryptoFramework.createRandom();
  const len: number = 16;
  let randData: Uint8Array | null = null;
  let retryCount = 0;
  while(retryCount < 3){
    randData = rand?.generateRandomSync(len)?.data;
    if(randData){
      break;
    }
    retryCount++;
  }
  if(!randData){
    return;
  }
  const authParam: userAuth.AuthParam = {
    challenge: randData,
    authType: \[userAuth.UserAuthType.PIN\],
    authTrustLevel: userAuth.AuthTrustLevel.ATL3,
    reuseUnlockResult: reuseUnlockResult,
  };
  const widgetParam: userAuth.WidgetParam = {
    title: 'Enter password',
  };
  const userAuthInstance = userAuth.getUserAuthInstance(authParam, widgetParam);
  console.info('get userAuth instance success');
  // The authentication result is returned by onResult only after the authentication is started by start() of UserAuthInstance.
  userAuthInstance.on('result', {
    onResult (result) {
      console.info(\`userAuthInstance callback result = ${JSON.stringify(result)}\`);
    }
  });
  console.info('auth on success');
  userAuthInstance.start();
  console.info('auth start success');
} catch (error) {
  const err: BusinessError = error as BusinessError;
  console.error(\`auth catch error. Code is ${err?.code}, message is ${err?.message}\`);
}

#### AuthTipInfo20+

Represents the intermediate authentication status.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.UserIAM.UserAuth.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| tipType | [UserAuthType](#userauthtype8) | No | No | Authentication type of the intermediate status. |
| tipCode | [UserAuthTipCode](#userauthtipcode20) | No | No | Intermediate status. |

#### AuthTipCallback20+

type AuthTipCallback = (authTipInfo: AuthTipInfo) => void

Defines the callback to return the intermediate authentication status.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.UserIAM.UserAuth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| authTipInfo | [AuthTipInfo](#authtipinfo20) | Yes | Intermediate authentication status. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { userAuth } from '@kit.UserAuthenticationKit';

try {
  const rand = cryptoFramework.createRandom();
  const len: number = 16;
  let randData: Uint8Array | null = null;
  let retryCount = 0;
  while(retryCount < 3){
    randData = rand?.generateRandomSync(len)?.data;
    if(randData){
      break;
    }
    retryCount++;
  }
  if(!randData){
    return;
  }
  const authParam: userAuth.AuthParam = {
    challenge: randData,
    authType: \[userAuth.UserAuthType.PIN\],
    authTrustLevel: userAuth.AuthTrustLevel.ATL3,
  };
  const widgetParam: userAuth.WidgetParam = {
    title: 'Enter password',
  };

  const userAuthInstance = userAuth.getUserAuthInstance(authParam, widgetParam);
  console.info('get userAuth instance success');
  // The intermediate authentication status is returned by onAuthTip only after the authentication is started by start() of UserAuthInstance.
  userAuthInstance.on('authTip', (authTipInfo: userAuth.AuthTipInfo) => {
    console.info(\`userAuthInstance callback authTipInfo = ${JSON.stringify(authTipInfo)}\`);
  });
  console.info('auth on success');
  userAuthInstance.start();
  console.info('auth start success');
} catch (error) {
  const err: BusinessError = error as BusinessError;
  console.error(\`auth catch error. Code is ${err?.code}, message is ${err?.message}\`);
}

#### UserAuthInstance10+

Provides APIs for user authentication. The user authentication widget is supported.

Before using the APIs of **UserAuthInstance**, you must obtain a **UserAuthInstance** instance by using [getUserAuthInstance](#userauthgetuserauthinstance10).

#### \[h2\]on10+

on(type: 'result', callback: IAuthCallback): void

Subscribes to the user authentication result. This API is used to obtain the final identity authentication result after the user completes identity authentication interaction with the authentication component. Before the authentication component disappears, the authentication failure attempts are not returned through this API. To perceive each authentication failure, use the [on('authTip')](#on20) API for subscription.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/HLt-pc8_QuGkjOldfLNhJg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062340Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2197FA3971B6950DA702BF13D50201F24CB39C967258198AB25CF0F1BE228E08)

On PCs/2-in-1 devices, if an application initiates authentication in modal application mode (that is, a valid **uiContext** is passed when the user API parameter [widgetParam](#widgetparam10) is configured) and receives the authentication result, and if other windows need to be displayed, the application needs to obtain the flag message released by the component pop-up window and subscribe to the component release message (**authTipInfo.tipCode = UserAuthTipCode.WIDGET\_RELEASED**) through the [on('authTip')](#on20) API.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.UserIAM.UserAuth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | 'result' | Yes | Event type. The value is **result**, which indicates the authentication result. |
| callback | [IAuthCallback](#iauthcallback10) | Yes | Callback used to return the user authentication result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [User Authentication Error Codes](../../error-codes/user-authentication-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.Mandatory parameters are left unspecified.

2.Incorrect parameter types.

3.Parameter verification failed.

 |
| 12500002 | General operation error. |

**Example 1**

Perform user identity authentication in modal system mode.

import { BusinessError } from '@kit.BasicServicesKit';
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { userAuth } from '@kit.UserAuthenticationKit';

try {
  const rand = cryptoFramework.createRandom();
  const len: number = 16;
  let randData: Uint8Array | null = null;
  let retryCount = 0;
  while(retryCount < 3){
    randData = rand?.generateRandomSync(len)?.data;
    if(randData){
      break;
    }
    retryCount++;
  }
  if(!randData){
    return;
  }
  const authParam: userAuth.AuthParam = {
    challenge: randData,
    authType: \[userAuth.UserAuthType.PIN\],
    authTrustLevel: userAuth.AuthTrustLevel.ATL3,
  };
  const widgetParam: userAuth.WidgetParam = {
    title: 'Enter password',
  };
  const userAuthInstance = userAuth.getUserAuthInstance(authParam, widgetParam);
  console.info('get userAuth instance success');
  // The authentication result is returned by onResult only after the authentication is started by start() of UserAuthInstance.
  userAuthInstance.on('result', {
    onResult (result) {
      console.info(\`userAuthInstance callback result = ${JSON.stringify(result)}\`);
    }
  });
  console.info('auth on success');
  userAuthInstance.start();
  console.info('auth start success');
} catch (error) {
  const err: BusinessError = error as BusinessError;
  console.error(\`auth catch error. Code is ${err?.code}, message is ${err?.message}\`);
}

**Example 2**

Perform user identity authentication in modal application mode.

import { BusinessError } from '@kit.BasicServicesKit';
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { userAuth } from '@kit.UserAuthenticationKit';

@Entry
@Component
struct Index {
  modelApplicationAuth(): void {
    try {
      const rand = cryptoFramework.createRandom();
      const len: number = 16;
      let randData: Uint8Array | null = null;
      let retryCount = 0;
      while(retryCount < 3){
        randData = rand?.generateRandomSync(len)?.data;
        if(randData){
          break;
        }
        retryCount++;
      }
      if(!randData){
        return;
      }
      const authParam: userAuth.AuthParam = {
        challenge: randData,
        authType: \[userAuth.UserAuthType.PIN\],
        authTrustLevel: userAuth.AuthTrustLevel.ATL3,
      };
      const uiContext: UIContext = this.getUIContext();
      const context: Context | undefined = uiContext.getHostContext();
      const widgetParam: userAuth.WidgetParam = {
        title: 'Enter password',
        uiContext: context,
      };
      const userAuthInstance = userAuth.getUserAuthInstance(authParam, widgetParam);
      console.info('get userAuth instance success');
      // The authentication result is returned by onResult only after the authentication is started by start() of UserAuthInstance.
      userAuthInstance.on('result', {
        onResult (result) {
          console.info(\`userAuthInstance callback result = ${JSON.stringify(result)}\`);
        }
      });
      console.info('auth on success');
      userAuthInstance.start();
      console.info('auth start success');
    } catch (error) {
      const err: BusinessError = error as BusinessError;
      console.error(\`auth catch error. Code is ${err?.code}, message is ${err?.message}\`);
    }
  }

  build() {
    Column() {
      Button('start auth')
        .onClick(() => {
          this.modelApplicationAuth();
        })
    }
  }
}

#### \[h2\]off10+

off(type: 'result', callback?: IAuthCallback): void

Unsubscribes from the user authentication result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/yPjowAgeS1GhCHiRXNKBgQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062340Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6B037F5C71D252125F6D7198B93B63C66F6317D5C27DB721189BE91FA382D85B)

The [UserAuthInstance](#userauthinstance10) instance used to invoke this API must be the one used to subscribe to the event.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.UserIAM.UserAuth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | 'result' | Yes | Event type. The value is **result**, which indicates the authentication result. |
| callback | [IAuthCallback](#iauthcallback10) | No | Callback used to return the user authentication result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [User Authentication Error Codes](../../error-codes/user-authentication-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.Mandatory parameters are left unspecified.

2.Incorrect parameter types.

3.Parameter verification failed.

 |
| 12500002 | General operation error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { userAuth } from '@kit.UserAuthenticationKit';

try {
  const rand = cryptoFramework.createRandom();
  const len: number = 16;
  let randData: Uint8Array | null = null;
  let retryCount = 0;
  while(retryCount < 3){
    randData = rand?.generateRandomSync(len)?.data;
    if(randData){
      break;
    }
    retryCount++;
  }
  if(!randData){
    return;
  }
  const authParam: userAuth.AuthParam = {
    challenge: randData,
    authType: \[userAuth.UserAuthType.PIN\],
    authTrustLevel: userAuth.AuthTrustLevel.ATL3,
  };
  const widgetParam: userAuth.WidgetParam = {
    title: 'Enter password',
  };
  const userAuthInstance = userAuth.getUserAuthInstance(authParam, widgetParam);
  console.info('get userAuth instance success');
  userAuthInstance.off('result', {
    onResult (result) {
      console.info(\`auth off result = ${JSON.stringify(result)}\`);
    }
  });
  console.info('auth off success');
} catch (error) {
  const err: BusinessError = error as BusinessError;
  console.error(\`auth catch error. Code is ${err?.code}, message is ${err?.message}\`);
}

#### \[h2\]start10+

start(): void

Starts authentication.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/09/v3/dhZWF9JRTnKsiNv3PYS-KQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062340Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=11E05733754C129BBE93E9335B2E684F7B3F93FE57EB08AEC816037ECA3B8E5D)

Each **UserAuthInstance** can be used for authentication only once.

**Required permissions**: ohos.permission.ACCESS\_BIOMETRIC or ohos.permission.USER\_AUTH\_FROM\_BACKGROUND (available only for system applications)

Starting from API version 20, only system applications can apply for the ohos.permission.USER\_AUTH\_FROM\_BACKGROUND permission.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.UserIAM.UserAuth.Core

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [User Authentication Error Codes](../../error-codes/user-authentication-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | 
Permission denied. Possible causes:

1.No permission to access biometric.

2.No permission to start authentication from background.

 |
| 401 | 

Parameter error. Possible causes:

1.Incorrect parameter types.

 |
| 12500002 | General operation error. |
| 12500003 | Authentication canceled. |
| 12500005 | The authentication type is not supported. |
| 12500006 | The authentication trust level is not supported. |
| 12500009 | Authentication is locked out. |
| 12500010 | The type of credential has not been enrolled. |
| 12500011 | Switched to the customized authentication process. |
| 12500013 | Operation failed because of PIN expired. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { userAuth } from '@kit.UserAuthenticationKit';

try {
  const rand = cryptoFramework.createRandom();
  const len: number = 16;
  let randData: Uint8Array | null = null;
  let retryCount = 0;
  while(retryCount < 3){
    randData = rand?.generateRandomSync(len)?.data;
    if(randData){
      break;
    }
    retryCount++;
  }
  if(!randData){
    return;
  }
  const authParam: userAuth.AuthParam = {
    challenge: randData,
    authType: \[userAuth.UserAuthType.PIN\],
    authTrustLevel: userAuth.AuthTrustLevel.ATL3,
  };
  const widgetParam: userAuth.WidgetParam = {
    title: 'Enter password',
  };
  const userAuthInstance = userAuth.getUserAuthInstance(authParam, widgetParam);
  console.info('get userAuth instance success');
  userAuthInstance.start();
  console.info('auth start success');
} catch (error) {
  const err: BusinessError = error as BusinessError;
  console.error(\`auth catch error. Code is ${err?.code}, message is ${err?.message}\`);
}

#### \[h2\]cancel10+

cancel(): void

Cancels this authentication.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/piWnNJfqQDSLxbf3XFUcng/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062340Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=364C82FDC17DA7F334A70FB0BF6DA3E403AE12917EEAB704FA91FFE3F5C6791F)

**UserAuthInstance** must be the instance being authenticated.

**Required permissions**: ohos.permission.ACCESS\_BIOMETRIC

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.UserIAM.UserAuth.Core

**Error codes**

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | 
Parameter error. Possible causes:

1.Incorrect parameter types.

 |
| 12500002 | General operation error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { userAuth } from '@kit.UserAuthenticationKit';

try {
  const rand = cryptoFramework.createRandom();
  const len: number = 16;
  let randData: Uint8Array | null = null;
  let retryCount = 0;
  while(retryCount < 3){
    randData = rand?.generateRandomSync(len)?.data;
    if(randData){
      break;
    }
    retryCount++;
  }
  if(!randData){
    return;
  }
  const authParam : userAuth.AuthParam = {
    challenge: randData,
    authType: \[userAuth.UserAuthType.PIN\],
    authTrustLevel: userAuth.AuthTrustLevel.ATL3,
  };
  const widgetParam: userAuth.WidgetParam = {
    title: 'Enter password',
  };
  const userAuthInstance = userAuth.getUserAuthInstance(authParam, widgetParam);
  console.info('get userAuth instance success');
  // The cancel() API can be called only after the authentication is started by start() of UserAuthInstance.
  userAuthInstance.start();
  console.info('auth start success');
  userAuthInstance.cancel();
  console.info('auth cancel success');
} catch (error) {
  const err: BusinessError = error as BusinessError;
  console.error(\`auth catch error. Code is ${err?.code}, message is ${err?.message}\`);
}

#### \[h2\]on20+

on(type: 'authTip', callback: AuthTipCallback): void

Subscribes to authentication tip information. This API is used to obtain the component startup and exit messages and each authentication failure. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/lQbHFS3DTDK3aoyAytLZrg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062340Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BB1A0D9E87DD11DAA0F333397BA81595CC005DD8AC8EC2EE6F25C983F5409116)

On PCs/2-in-1 devices, if an application initiates authentication in modal application mode (that is, a valid **uiContext** is passed when the user API parameter [widgetParam](#widgetparam10) is configured) and receives the authentication result, and if other windows need to be displayed, the application needs to obtain the flag message released by the component pop-up window and subscribe to the component release message (**authTipInfo.tipCode = UserAuthTipCode.WIDGET\_RELEASED**) through the [on('authTip')](#on20) API.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.UserIAM.UserAuth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The supported event is **'authTip'**. This event is triggered when [start()](#start10) is called and authentication is initiated. |
| callback | [AuthTipCallback](#authtipcallback20) | Yes | Callback used to return the intermediate authentication status. |

**Error codes**

For details about the error codes, see [User Authentication Error Codes](../../error-codes/user-authentication-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 12500002 | General operation error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { userAuth } from '@kit.UserAuthenticationKit';

try {
  const rand = cryptoFramework.createRandom();
  const len: number = 16;
  let randData: Uint8Array | null = null;
  let retryCount = 0;
  while(retryCount < 3){
    randData = rand?.generateRandomSync(len)?.data;
    if(randData){
      break;
    }
    retryCount++;
  }
  if(!randData){
    return;
  }
  const authParam: userAuth.AuthParam = {
    challenge: randData,
    authType: \[userAuth.UserAuthType.PIN\],
    authTrustLevel: userAuth.AuthTrustLevel.ATL3,
  };
  const widgetParam: userAuth.WidgetParam = {
    title: 'Enter password',
  };
  const userAuthInstance = userAuth.getUserAuthInstance(authParam, widgetParam);
  console.info('get userAuth instance success');
  // The intermediate authentication status is returned by onAuthTip only after the authentication is started by start() of UserAuthInstance.
  userAuthInstance.on('authTip', (authTipInfo: userAuth.AuthTipInfo) => {
    console.info(\`userAuthInstance callback authTipInfo = ${JSON.stringify(authTipInfo)}\`);
  });
  console.info('auth on success');
  userAuthInstance.start();
  console.info('auth start success');
} catch (error) {
  const err: BusinessError = error as BusinessError;
  console.error(\`auth catch error. Code is ${err?.code}, message is ${err?.message}\`);
}

#### \[h2\]off20+

off(type: 'authTip', callback?: AuthTipCallback): void

Unsubscribes from the event for intermediate authentication status.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/okDNxDLCQNaQ3Y4CKZhqKw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062340Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=770647E2060D0E240EFFE447D42731FB75089095399F077BBD01BFBD14D7B38C)

The [UserAuthInstance](#userauthinstance10) instance used to invoke this API must be the one used to subscribe to the event.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.UserIAM.UserAuth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The supported event is **'authTip'**. This API unsubscribes from the event triggered by [on()](#on20) after the [start()](#start10) call and the initiation of authentication. |
| callback | [AuthTipCallback](#authtipcallback20) | No | Callback used to return the intermediate authentication status. If this parameter is not passed, the value passed when the [on()](#on20) API is called is used by default. |

**Error codes**

For details about the error codes, see [User Authentication Error Codes](../../error-codes/user-authentication-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 12500002 | General operation error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { userAuth } from '@kit.UserAuthenticationKit';

try {
  const rand = cryptoFramework.createRandom();
  const len: number = 16;
  let randData: Uint8Array | null = null;
  let retryCount = 0;
  while(retryCount < 3){
    randData = rand?.generateRandomSync(len)?.data;
    if(randData){
      break;
    }
    retryCount++;
  }
  if(!randData){
    return;
  }
  const authParam: userAuth.AuthParam = {
    challenge: randData,
    authType: \[userAuth.UserAuthType.PIN\],
    authTrustLevel: userAuth.AuthTrustLevel.ATL3,
  };
  const widgetParam: userAuth.WidgetParam = {
    title: 'Enter password',
  };
  const userAuthInstance = userAuth.getUserAuthInstance(authParam, widgetParam);
  console.info('get userAuth instance success');
  userAuthInstance.off('authTip', (authTipInfo: userAuth.AuthTipInfo) => {
    console.info(\`userAuthInstance callback authTipInfo = ${JSON.stringify(authTipInfo)}\`);
  });
  console.info('auth off success');
} catch (error) {
  const err: BusinessError = error as BusinessError;
  console.error(\`auth catch error. Code is ${err?.code}, message is ${err?.message}\`);
}

#### userAuth.getUserAuthInstance10+

getUserAuthInstance(authParam: AuthParam, widgetParam: WidgetParam): UserAuthInstance

Obtains a [UserAuthInstance](#userauthinstance10) instance for user authentication. The user authentication widget is also supported.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/HuEjJDYrShKdSMd06Nk9XA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062340Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7AFFCA6E06618D26E0AB679127F71819A2C6D4A8EDF7C344FDB9A9EE205B7ADD)

Each **UserAuthInstance** can be used for authentication only once.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.UserIAM.UserAuth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| authParam | [AuthParam](#authparam10) | Yes | User authentication parameters. |
| widgetParam | [WidgetParam](#widgetparam10) | Yes | Parameters on the user authentication page. |

**Return value**

| Type | Description |
| :-- | :-- |
| [UserAuthInstance](#userauthinstance10) | **UserAuthInstance** instance that supports UI. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [User Authentication Error Codes](../../error-codes/user-authentication-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.Mandatory parameters are left unspecified.

2.Incorrect parameter types.

3.Parameter verification failed.

 |
| 12500002 | General operation error. |
| 12500005 | The authentication type is not supported. |
| 12500006 | The authentication trust level is not supported. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { userAuth } from '@kit.UserAuthenticationKit';

try {
  const rand = cryptoFramework.createRandom();
  const len: number = 16;
  let randData: Uint8Array | null = null;
  let retryCount = 0;
  while(retryCount < 3){
    randData = rand?.generateRandomSync(len)?.data;
    if(randData){
      break;
    }
    retryCount++;
  }
  if(!randData){
    return;
  }
  const authParam: userAuth.AuthParam = {
    challenge: randData,
    authType: \[userAuth.UserAuthType.PIN\],
    authTrustLevel: userAuth.AuthTrustLevel.ATL3,
  };
  const widgetParam: userAuth.WidgetParam = {
    title: 'Enter password',
  };
  let userAuthInstance = userAuth.getUserAuthInstance(authParam, widgetParam);
  console.info('get userAuth instance success');
} catch (error) {
  const err: BusinessError = error as BusinessError;
  console.error(\`auth catch error. Code is ${err?.code}, message is ${err?.message}\`);
}

#### AuthResultInfo(deprecated)

Represents the authentication result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/pegg1AHgTO2ul_FLuFFJjQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062340Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0E96FB8804E63837DEBA22DB8877E75BED08D85D666DE26335279F2EA273FE8F)

This parameter is supported since API version 9 and deprecated since API version 11. Use [UserAuthResult](#userauthresult10) instead.

**System capability**: SystemCapability.UserIAM.UserAuth.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| result | number | No | No | Authentication result. |
| token | Uint8Array | No | Yes | Token that has passed the user identity authentication. |
| remainAttempts | number | No | Yes | Number of remaining authentication attempts. |
| lockoutDuration | number | No | Yes | Lock duration of the authentication operation, in ms. |

#### TipInfo(deprecated)

Represents the tip information displayed during the authentication, which is used to provide feedback during the authentication process.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/oQyvKduaR22jg_b9uwmvuQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062340Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=52F253EC014E337543904B5B1F579824B9D69A032C4E555A18BEB493649836B5)

This API is supported since API version 9 and deprecated since API version 11. Use [AuthTipInfo](#authtipinfo20) instead.

**System capability**: SystemCapability.UserIAM.UserAuth.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| module | number | No | No | ID of the module that sends the tip information. |
| tip | number | No | No | Tip to be given during the authentication process. |

#### EventInfo(deprecated)

type EventInfo = AuthResultInfo | TipInfo

Enumerates the authentication event information types.

It consists of the fields in **Type** in the following table.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/oWbH-89YR16-pKTA45Ep1Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062340Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=87A728AE8E8DCB12D50359F08B6C1D6B2205BFE0F9ABF021ECD98415B7D629F1)

This parameter is supported since API version 9 and deprecated since API version 11. Use [UserAuthResult](#userauthresult10) instead.

**System capability**: SystemCapability.UserIAM.UserAuth.Core

| Type | Description |
| :-- | :-- |
| [AuthResultInfo](#authresultinfodeprecated) | Authentication result. |
| [TipInfo](#tipinfodeprecated) | Authentication tip information. |

#### AuthEventKey(deprecated)

type AuthEventKey = 'result' | 'tip'

Defines the keyword of the authentication event type. It is used as a parameter of [on](#ondeprecated).

It consists of the fields in **Type** in the following table.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/julwya5iQp-LpA-0LzInKg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062340Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=62DB4AFFFB43CFED2644FB6529AAA7DAFF6C5FCC8DC66624574403E9976E3957)

This API is supported since API version 9 and deprecated since API version 11.

**System capability**: SystemCapability.UserIAM.UserAuth.Core

| Type | Description |
| :-- | :-- |
| 'result' | If the first parameter of [on](#ondeprecated) is **result**, the [callback](#callbackdeprecated) returns the authentication result. |
| 'tip' | If the first parameter of [on](#ondeprecated) is **tip**, the [callback](#callbackdeprecated) returns the authentication tip information. |

#### AuthEvent(deprecated)

Provides an asynchronous callback to return the authentication event information.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/L1f80g-YTBCk_TBtWA5LyQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062340Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C9FBF81C13766A4D2A2FC104C8E87FA1635684A4AB180C067BC4F9D70A588B4F)

This API is supported since API version 9 and deprecated since API version 11. Use [IAuthCallback](#iauthcallback10) instead.

#### \[h2\]callback(deprecated)

callback(result : EventInfo) : void

Called to return the authentication result or authentication tip information.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/8CAtG0VNROumAA9LLsfKPQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062340Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FF3676CD243FC194E171E9880325D45A0B90E9247CBCC6FAFE3BBB0BEF824A11)

This API is supported since API version 9 and deprecated since API version 11. Use [onResult](#onresult10) instead.

**System capability**: SystemCapability.UserIAM.UserAuth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| result | [EventInfo](#eventinfodeprecated) | Yes | Authentication result or tip information. |

**Example**

import { userAuth } from '@kit.UserAuthenticationKit';

let challenge = new Uint8Array(\[1, 2, 3, 4, 5, 6, 7, 8\]);
let authType = userAuth.UserAuthType.FACE;
let authTrustLevel = userAuth.AuthTrustLevel.ATL1;
// Obtain the authentication result via a callback.
try {
  let auth = userAuth.getAuthInstance(challenge, authType, authTrustLevel);
  auth.on('result', {
    callback: (result: userAuth.AuthResultInfo) => {
      console.info(\`authV9 result ${result.result}\`);
      console.info(\`authV9 token ${result.token}\`);
      console.info(\`authV9 remainAttempts ${result.remainAttempts}\`);
      console.info(\`authV9 lockoutDuration ${result.lockoutDuration}\`);
    }
  } as userAuth.AuthEvent);
  auth.start();
  console.info('authV9 start success');
} catch (error) {
  console.error(\`authV9 error = ${error}\`);
  // do error.
}
// Obtain the authentication tip information via a callback.
try {
  let auth = userAuth.getAuthInstance(challenge, authType, authTrustLevel);
  auth.on('tip', {
    callback : (result : userAuth.TipInfo) => {
      switch (result.tip) {
        case userAuth.FaceTips.FACE\_AUTH\_TIP\_TOO\_BRIGHT:
          // Do something.
          break;
        case userAuth.FaceTips.FACE\_AUTH\_TIP\_TOO\_DARK:
          // Do something.
          break;
        default:
          // do others.
      }
    }
  } as userAuth.AuthEvent);
  auth.start();
  console.info('authV9 start success');
} catch (error) {
  console.error(\`authV9 error = ${error}\`);
  // do error.
}

#### AuthInstance(deprecated)

Implements user authentication.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/0F8iqiV9TyO0j03iJyKuoA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062340Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5A20F328E2A89F79BB6BBD63632B8E2EF24077295102E311E4FDE12FB888B5F9)

This API is supported since API version 9 and deprecated since API version 10. Use [UserAuthInstance](#userauthinstance10) instead.

#### \[h2\]on(deprecated)

on : (name : AuthEventKey, callback : AuthEvent) => void

Subscribes to the user authentication events of the specified type.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/4lVYKc5oQmyFBAhTbQQbeA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062340Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7524F92958167638CEEC4E9B37DF2890CC0D0558A7B227719D0E73C7C90829F1)

This API is supported since API version 9 and deprecated since API version 10. Use [on](#on10) instead.

Use the [AuthInstance](#authinstancedeprecated) instance obtained to call this API.

**System capability**: SystemCapability.UserIAM.UserAuth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| name | [AuthEventKey](#autheventkeydeprecated) | Yes | Authentication event type. If the value is **result**, the callback returns the authentication result. If the value is **tip**, the callback returns the authentication tip information. |
| callback | [AuthEvent](#autheventdeprecated) | Yes | Callback used to return the authentication result or tip information. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [User Authentication Error Codes](../../error-codes/user-authentication-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |
| 12500002 | General operation error. |

**Example**

import { userAuth } from '@kit.UserAuthenticationKit';

let challenge = new Uint8Array(\[1, 2, 3, 4, 5, 6, 7, 8\]);
let authType = userAuth.UserAuthType.FACE;
let authTrustLevel = userAuth.AuthTrustLevel.ATL1;
try {
  let auth = userAuth.getAuthInstance(challenge, authType, authTrustLevel);
  // Subscribe to the authentication result.
  auth.on('result', {
    callback: (result: userAuth.AuthResultInfo) => {
      console.info(\`authV9 result ${result.result}\`);
      console.info(\`authV9 token ${result.token}\`);
      console.info(\`authV9 remainAttempts ${result.remainAttempts}\`);
      console.info(\`authV9 lockoutDuration ${result.lockoutDuration}\`);
    }
  });
  // Subscribe to authentication tip information.
  auth.on('tip', {
    callback : (result : userAuth.TipInfo) => {
      switch (result.tip) {
        case userAuth.FaceTips.FACE\_AUTH\_TIP\_TOO\_BRIGHT:
          // Do something.
          break;
        case userAuth.FaceTips.FACE\_AUTH\_TIP\_TOO\_DARK:
          // Do something.
          break;
        default:
          // do others.
      }
    }
  } as userAuth.AuthEvent);
  auth.start();
  console.info('authV9 start success');
} catch (error) {
  console.error(\`authV9 error = ${error}\`);
  // do error.
}

#### \[h2\]off(deprecated)

off : (name : AuthEventKey) => void

Unsubscribes from the user authentication events of the specified type.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/5XW261M9RE6oSInTr2u7gQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062340Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1BCDE815BF5D146948C438B8B0043D5B978DED8CB228B6263794E62E3E70E146)

This API is supported since API version 9 and deprecated since API version 10. Use [off](#off10) instead.

The [AuthInstance](#authinstancedeprecated) instance used to invoke this API must be the one used to subscribe to the event.

**System capability**: SystemCapability.UserIAM.UserAuth.Core

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| name | [AuthEventKey](#autheventkeydeprecated) | Yes | Authentication event type. If the value is **result**, the authentication result is unsubscribed from. If the value is **tip**, the authentication tip information is unsubscribed from. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [User Authentication Error Codes](../../error-codes/user-authentication-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |
| 12500002 | General operation error. |

**Example**

import { userAuth } from '@kit.UserAuthenticationKit';

let challenge = new Uint8Array(\[1, 2, 3, 4, 5, 6, 7, 8\]);
let authType = userAuth.UserAuthType.FACE;
let authTrustLevel = userAuth.AuthTrustLevel.ATL1;
try {
  let auth = userAuth.getAuthInstance(challenge, authType, authTrustLevel);
  // Subscribe to the authentication result.
  auth.on('result', {
    callback: (result: userAuth.AuthResultInfo) => {
      console.info(\`authV9 result ${result.result}\`);
      console.info(\`authV9 token ${result.token}\`);
      console.info(\`authV9 remainAttempts ${result.remainAttempts}\`);
      console.info(\`authV9 lockoutDuration ${result.lockoutDuration}\`);
    }
  });
  // Unsubscribe from the authentication result.
  auth.off('result');
  console.info('cancel subscribe authentication event success');
} catch (error) {
  console.error(\`cancel subscribe authentication event failed, error = ${error}\`);
  // do error.
}

#### \[h2\]start(deprecated)

start : () => void

Starts authentication.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/ziVja7xRQPuipt0Hymx_tg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062340Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8F969327A7894FC0E2B8EEBCC4BC492153DFB055A4126FC703399D072D3E0BA6)

This API is supported since API version 9 and deprecated since API version 10. Use [start](#start10) instead.

Use the [AuthInstance](#authinstancedeprecated) instance obtained to call this API.

**Required permissions**: ohos.permission.ACCESS\_BIOMETRIC

**System capability**: SystemCapability.UserIAM.UserAuth.Core

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [User Authentication Error Codes](../../error-codes/user-authentication-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. |
| 12500001 | Authentication failed. |
| 12500002 | General operation error. |
| 12500003 | The operation is canceled. |
| 12500004 | The operation is time-out. |
| 12500005 | The authentication type is not supported. |
| 12500006 | The authentication trust level is not supported. |
| 12500007 | The authentication task is busy. |
| 12500009 | The authenticator is locked. |
| 12500010 | The type of credential has not been enrolled. |

**Example**

import { userAuth } from '@kit.UserAuthenticationKit';

let challenge = new Uint8Array(\[1, 2, 3, 4, 5, 6, 7, 8\]);
let authType = userAuth.UserAuthType.FACE;
let authTrustLevel = userAuth.AuthTrustLevel.ATL1;

try {
  let auth = userAuth.getAuthInstance(challenge, authType, authTrustLevel);
  auth.start();
  console.info('authV9 start auth success');
} catch (error) {
  console.error(\`authV9 start auth failed, error = ${error}\`);
}

#### \[h2\]cancel(deprecated)

cancel : () => void

Cancels this authentication.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/4HcTykyFQYqJqc1IDn-doA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062340Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=348E5D4D3BD465784D197AC37D025765CD0B90EF6172A200026CA45507CE5448)

This API is supported since API version 9 and deprecated since API version 10. Use [cancel](#cancel10) instead.

Use the [AuthInstance](#authinstancedeprecated) instance obtained to call this API. The [AuthInstance](#authinstancedeprecated) instance must be the instance being authenticated.

**Required permissions**: ohos.permission.ACCESS\_BIOMETRIC

**System capability**: SystemCapability.UserIAM.UserAuth.Core

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [User Authentication Error Codes](../../error-codes/user-authentication-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. |
| 12500002 | General operation error. |

**Example**

import { userAuth } from '@kit.UserAuthenticationKit';

let challenge = new Uint8Array(\[1, 2, 3, 4, 5, 6, 7, 8\]);
let authType = userAuth.UserAuthType.FACE;
let authTrustLevel = userAuth.AuthTrustLevel.ATL1;

try {
  let auth = userAuth.getAuthInstance(challenge, authType, authTrustLevel);
  auth.cancel();
  console.info('cancel auth success');
} catch (error) {
  console.error(\`cancel auth failed, error = ${error}\`);
}

#### userAuth.getAuthInstance(deprecated)

getAuthInstance(challenge : Uint8Array, authType : UserAuthType, authTrustLevel : AuthTrustLevel): AuthInstance

Obtains an **AuthInstance** instance for user authentication.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/SSzv3vt-SJmHKNcER2mobg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062340Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B287022EA6D482B36D2C7F7F21C4A8D20E65F7D06B4DF38DAF0388199670B852)

This API is supported since API version 9 and deprecated since API version 10. Use [getUserAuthInstance](#userauthgetuserauthinstance10) instead.

An **AuthInstance** instance can be used for authentication only once.

**System capability**: SystemCapability.UserIAM.UserAuth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| challenge | Uint8Array | Yes | Challenge value. It cannot exceed 32 bytes and can be passed in Uint8Array(\[\]) format. |
| authType | [UserAuthType](#userauthtype8) | Yes | Authentication type. Currently, **FACE** and **FINGERPRINT** are supported. |
| authTrustLevel | [AuthTrustLevel](#authtrustlevel8) | Yes | Authentication trust level. |

**Return value**

| Type | Description |
| :-- | :-- |
| [AuthInstance](#authinstancedeprecated) | **AuthInstance** instance obtained. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [User Authentication Error Codes](../../error-codes/user-authentication-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |
| 12500002 | General operation error. |
| 12500005 | The authentication type is not supported. |
| 12500006 | The authentication trust level is not supported. |

**Example**

import { userAuth } from '@kit.UserAuthenticationKit';

let challenge = new Uint8Array(\[1, 2, 3, 4, 5, 6, 7, 8\]);
let authType = userAuth.UserAuthType.FACE;
let authTrustLevel = userAuth.AuthTrustLevel.ATL1;

try {
  let auth = userAuth.getAuthInstance(challenge, authType, authTrustLevel);
  console.info('let auth instance success');
} catch (error) {
  console.error(\`get auth instance success failed, error = ${error}\`);
}

#### userAuth.getAvailableStatus9+

getAvailableStatus(authType : UserAuthType, authTrustLevel : AuthTrustLevel): void

Checks whether the specified authentication capability is supported.

**Required permissions**: ohos.permission.ACCESS\_BIOMETRIC

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.UserIAM.UserAuth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| authType | [UserAuthType](#userauthtype8) | Yes | Authentication type. PIN is supported since API version 11. |
| authTrustLevel | [AuthTrustLevel](#authtrustlevel8) | Yes | Authentication trust level. |

The mechanism for returning the error code is as follows:

Error code 12500005 is returned if the authentication executor is not registered and the specified authentication capability is not supported.

Error code 12500006 is returned if the authentication executor has been registered, the authentication functionality is not disabled, but the authentication trust level is lower than that specified by the service.

Error code 12500010 is returned if the authentication executor has been registered, the authentication functionality is not disabled, but the user has not enrolled credential.

Error code 12500013 is returned if the authentication executor has been registered, the authentication functionality is not disabled, but the password has expired.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/03/v3/xf-LHXZRTF-__w_c2DLF5w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062340Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=34D776D679798E49CC3D7C29E3823186C9B277E65B5DC06DB15B98DDAA9F67CB)

If **getAvailableStatus** is called to check whether lock screen password authentication at ATL4 is supported for a user who has enrolled a 4-digit PIN as the lock screen password (the authentication trust level is ATL3), error code 12500010 will be returned.

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [User Authentication Error Codes](../../error-codes/user-authentication-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | 
Parameter error. Possible causes:

1.Mandatory parameters are left unspecified.

 |
| 12500002 | General operation error. |
| 12500005 | The authentication type is not supported. |
| 12500006 | The authentication trust level is not supported. |
| 12500010 | The type of credential has not been enrolled. |
| 12500013 | Operation failed because of PIN expired. |

**Example**

import { userAuth } from '@kit.UserAuthenticationKit';

try {
  userAuth.getAvailableStatus(userAuth.UserAuthType.FACE, userAuth.AuthTrustLevel.ATL3);
  console.info('current auth trust level is supported');
} catch (error) {
  console.error(\`current auth trust level is not supported, error = ${error}\`);
}

#### UserAuthResultCode9+

Enumerates the authentication result codes.

**System capability**: SystemCapability.UserIAM.UserAuth.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| SUCCESS | 12500000 | 
The operation is successful.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| FAIL | 12500001 | 

The authentication failed.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| GENERAL\_ERROR | 12500002 | 

A general operation error occurred.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| CANCELED | 12500003 | 

The authentication is canceled.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| TIMEOUT | 12500004 | 

The authentication has timed out.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| TYPE\_NOT\_SUPPORT | 12500005 | 

The authentication type is not supported.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| TRUST\_LEVEL\_NOT\_SUPPORT | 12500006 | 

The authentication trust level is not supported.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| BUSY | 12500007 | 

The system does not respond.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| INVALID\_PARAMETERS20+ | 12500008 | 

Parameter verification failed.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |
| LOCKED | 12500009 | 

The authentication executor is locked.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| NOT\_ENROLLED | 12500010 | 

The user has not enrolled the specified system identity authentication credential.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| CANCELED\_FROM\_WIDGET10+ | 12500011 | 

The user cancels the system authentication and selects a custom authentication of the application. The caller needs to launch the custom authentication page.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| PIN\_EXPIRED12+ | 12500013 | 

The authentication failed because the lock screen password has expired.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |

#### UserAuth(deprecated)

Provides APIs for managing the **UserAuth** object.

#### \[h2\]constructor(deprecated)

constructor()

A constructor used to create a **UserAuth** instance.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/S6G2CxGvRIeVAOVjG2AglA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062340Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=05DCB8DB43C16B57403F236FBBB13EC1762ED7C512C075989B090FB31E8054ED)

This API is supported since API version 8 and deprecated since API version 9. Use [getAuthInstance](#userauthgetauthinstancedeprecated) instead.

**System capability**: SystemCapability.UserIAM.UserAuth.Core

**Example**

import { userAuth } from '@kit.UserAuthenticationKit';

let auth = new userAuth.UserAuth();

#### \[h2\]getVersion(deprecated)

getVersion() : number

Obtains the version of this authenticator.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/03/v3/fVMxmtE7SQmQIEhHzQToBA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062340Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=88021F433BA85839481988A7F4C51935A54C8006635A41A1320809298BC9B5B4)

This API is supported since API version 8 and deprecated since API version 9.

**Required permissions**: ohos.permission.ACCESS\_BIOMETRIC

**System capability**: SystemCapability.UserIAM.UserAuth.Core

**Return value**

| Type | Description |
| :-- | :-- |
| number | Authenticator version obtained. |

**Example**

import { userAuth } from '@kit.UserAuthenticationKit';

let auth = new userAuth.UserAuth();
let version = auth.getVersion();
console.info(\`auth version = ${version}\`);

#### \[h2\]getAvailableStatus(deprecated)

getAvailableStatus(authType : UserAuthType, authTrustLevel : AuthTrustLevel) : number

Checks whether the specified authentication capability is supported.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/wO5_AC3uS4ap4w_P88pwUA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062340Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A9F092F252974DC668A9782AAB1BB4254E7F835310850CFE69BCCF13798E17D0)

This API is supported since API version 8 and deprecated since API version 9. Use [getAvailableStatus](#userauthgetavailablestatus9) instead.

**Required permissions**: ohos.permission.ACCESS\_BIOMETRIC

**System capability**: SystemCapability.UserIAM.UserAuth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| authType | [UserAuthType](#userauthtype8) | Yes | Authentication type. Currently, **FACE** and **FINGERPRINT** are supported. |
| authTrustLevel | [AuthTrustLevel](#authtrustlevel8) | Yes | Authentication trust level. |

**Return value**

| Type | Description |
| :-- | :-- |
| number | Query result. If the authentication capability is supported, **SUCCESS** is returned. Otherwise, a [ResultCode](#resultcodedeprecated) is returned. |

**Example**

import { userAuth } from '@kit.UserAuthenticationKit';

let auth = new userAuth.UserAuth();
let checkCode = auth.getAvailableStatus(userAuth.UserAuthType.FACE, userAuth.AuthTrustLevel.ATL1);
if (checkCode == userAuth.ResultCode.SUCCESS) {
  console.info('check auth support success');
} else {
  console.error(\`check auth support fail, code = ${checkCode}\`);
}

#### \[h2\]auth(deprecated)

auth(challenge: Uint8Array, authType: UserAuthType, authTrustLevel: AuthTrustLevel, callback: IUserAuthCallback): Uint8Array

Starts user authentication. This API uses a callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/sWqF9YI9TqWfRrwQli-79Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062340Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F7406DFC5CFBF9FE5479440BE6D71ABAE9CDD2571E568AD3D8AAF9A1C6E234B2)

This API is supported since API version 8 and deprecated since API version 9. Use [start](#startdeprecated) instead.

**Required permissions**: ohos.permission.ACCESS\_BIOMETRIC

**System capability**: SystemCapability.UserIAM.UserAuth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| challenge | Uint8Array | Yes | Challenge value, which can be passed in Uint8Array(\[\]) format. |
| authType | [UserAuthType](#userauthtype8) | Yes | Authentication type. Currently, **FACE** and **FINGERPRINT** are supported. |
| authTrustLevel | [AuthTrustLevel](#authtrustlevel8) | Yes | Authentication trust level. |
| callback | [IUserAuthCallback](#iuserauthcallbackdeprecated) | Yes | Callback used to return the result. |

**Return value**

| Type | Description |
| :-- | :-- |
| Uint8Array | Context ID, which is used as the input parameter of [cancelAuth](#cancelauthdeprecated). |

**Example**

import { userAuth } from '@kit.UserAuthenticationKit';

let auth = new userAuth.UserAuth();
let challenge = new Uint8Array(\[\]);
auth.auth(challenge, userAuth.UserAuthType.FACE, userAuth.AuthTrustLevel.ATL1, {
  onResult: (result, extraInfo) => {
    try {
      console.info(\`auth onResult result = ${result}\`);
      console.info(\`auth onResult extraInfo = ${JSON.stringify(extraInfo)}\`);
      if (result == userAuth.ResultCode.SUCCESS) {
        // Add the logic to be executed when the authentication is successful.
      } else {
        // Add the logic to be executed when the authentication fails.
      }
    } catch (error) {
      console.error(\`auth onResult error = ${error}\`);
    }
  }
});

#### \[h2\]cancelAuth(deprecated)

cancelAuth(contextID : Uint8Array) : number

Cancels the authentication based on the context ID.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/Tk5cPe2zTvOVPOSFPwIwTQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062340Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=57187C801DAF971BB4EA50F8251C4C907AB6ABE1F25BB9E52BB26F4FEF2FFF15)

This API is supported since API version 8 and deprecated since API version 9. Use [cancel](#canceldeprecated) instead.

**Required permissions**: ohos.permission.ACCESS\_BIOMETRIC

**System capability**: SystemCapability.UserIAM.UserAuth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| contextID | Uint8Array | Yes | Context ID, which is obtained by [auth](#authdeprecated). |

**Return value**

| Type | Description |
| :-- | :-- |
| number | Returns **SUCCESS** if the cancellation is successful. Returns a [ResultCode](#resultcodedeprecated) otherwise. |

**Example**

import { userAuth } from '@kit.UserAuthenticationKit';

// contextId can be obtained via auth(). In this example, it is defined here.
let contextId = new Uint8Array(\[0, 1, 2, 3, 4, 5, 6, 7\]);
let auth = new userAuth.UserAuth();
let cancelCode = auth.cancelAuth(contextId);
if (cancelCode == userAuth.ResultCode.SUCCESS) {
  console.info('cancel auth success');
} else {
  console.error('cancel auth fail');
}

#### IUserAuthCallback(deprecated)

Provides callbacks to return the authentication result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/UdLwtsmiTKOHnGzEcDWG_w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062340Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=509BB42CE517279A8974FCF6FAD643878D9F00AA00D883CCBD07817AEC2429D7)

This API is supported since API version 8 and deprecated since API version 9. Use [AuthEvent](#autheventdeprecated) instead.

#### \[h2\]onResult(deprecated)

onResult: (result : number, extraInfo : AuthResult) => void

Called to return the authentication result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/ucQfJgzxSb67FxZlTGRuJg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062340Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A974124E791C110A2819BA19BA6CE7788FF9C05F3819F4BF71BB895A3E70DC88)

This API is supported since API version 8 and deprecated since API version 9. Use [callback](#callbackdeprecated) instead.

**System capability**: SystemCapability.UserIAM.UserAuth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| result | number | Yes | Authentication result. For details, see [ResultCode](#resultcodedeprecated). |
| extraInfo | [AuthResult](#authresultdeprecated) | Yes | 
Extended information, which varies depending on the authentication result.

If the authentication is successful, the user authentication token will be returned in **extraInfo**.

If the authentication fails, the remaining number of authentication times will be returned in **extraInfo**.

If the authentication executor is locked, the freeze time will be returned in **extraInfo**.

 |

**Example**

import { userAuth } from '@kit.UserAuthenticationKit';

let auth = new userAuth.UserAuth();
let challenge = new Uint8Array(\[\]);
auth.auth(challenge, userAuth.UserAuthType.FACE, userAuth.AuthTrustLevel.ATL1, {
  onResult: (result, extraInfo) => {
    try {
      console.info(\`auth onResult result = ${result}\`);
      console.info(\`auth onResult extraInfo = ${JSON.stringify(extraInfo)}\`);
      if (result == userAuth.ResultCode.SUCCESS) {
        // Add the logic to be executed when the authentication is successful.
      }  else {
        // Add the logic to be executed when the authentication fails.
      }
    } catch (error) {
      console.error(\`auth onResult error = ${error}\`);
    }
  }
});

#### \[h2\]onAcquireInfo(deprecated)

onAcquireInfo ?: (module : number, acquire : number, extraInfo : any) => void

Called to acquire authentication tip information. This API is optional.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7/v3/zT-KNpbeRZuksp_kqsXpXA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062340Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1597C27770D58909B58A848183235F14D8734339982DE185FCE97B62065D7163)

This API is supported since API version 8 and deprecated since API version 9. Use [callback](#callbackdeprecated) instead.

**System capability**: SystemCapability.UserIAM.UserAuth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| module | number | Yes | ID of the module that sends the tip information. |
| acquire | number | Yes | Authentication tip information. |
| extraInfo | any | Yes | Reserved field. |

**Example**

import { userAuth } from '@kit.UserAuthenticationKit';

let auth = new userAuth.UserAuth();
let challenge = new Uint8Array(\[\]);
auth.auth(challenge, userAuth.UserAuthType.FACE, userAuth.AuthTrustLevel.ATL1, {
  onResult: (result, extraInfo) => {
    try {
      console.info(\`auth onResult result = ${result}\`);
      console.info(\`auth onResult extraInfo = ${JSON.stringify(extraInfo)}\`);
      if (result == userAuth.ResultCode.SUCCESS) {
        // Add the logic to be executed when the authentication is successful.
      }  else {
        // Add the logic to be executed when the authentication fails.
      }
    } catch (error) {
      console.error(\`auth onResult error = ${error}\`);
    }
  },
  onAcquireInfo: (module, acquire, extraInfo : userAuth.AuthResult) => {
    try {
      console.info(\`auth onAcquireInfo module = ${module}\`);
      console.info(\`auth onAcquireInfo acquire = ${acquire}\`);
      console.info(\`auth onAcquireInfo extraInfo = ${JSON.stringify(extraInfo)}\`);
    } catch (error) {
      console.error(\`auth onAcquireInfo error = ${error}\`);
    }
  }
});

#### AuthResult(deprecated)

Represents the authentication result object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/B6P1EdpoSa6IXMbyqDDVYA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062340Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=278DB3C45F418E422E4015D5EDF7A69CB31787EA578E14E0BBDC1E9171396AE4)

This API is supported since API version 8 and deprecated since API version 9. Use [AuthResultInfo](#authresultinfodeprecated) instead.

**System capability**: SystemCapability.UserIAM.UserAuth.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| token | Uint8Array | No | Yes | Authentication token information. |
| remainTimes | number | No | Yes | Number of remaining authentication operations. |
| freezingTime | number | No | Yes | Time for which the authentication operation is frozen. The unit is milliseconds. |

#### ResultCode(deprecated)

Enumerates the authentication result codes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/4E3BzQFCSMepz9oz9ofwQw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062340Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CE1243BDC5E66709DF35D5479C1EA8C170714716FD60704656D5F176C2A5E3E6)

This API is supported since API version 8 and deprecated since API version 9. Use [UserAuthResultCode](#userauthresultcode9) instead.

**System capability**: SystemCapability.UserIAM.UserAuth.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| SUCCESS | 0 | The operation is successful. |
| FAIL | 1 | The authentication failed. |
| GENERAL\_ERROR | 2 | A general operation error occurred. |
| CANCELED | 3 | The authentication is canceled. |
| TIMEOUT | 4 | The authentication timed out. |
| TYPE\_NOT\_SUPPORT | 5 | The authentication type is not supported. |
| TRUST\_LEVEL\_NOT\_SUPPORT | 6 | The authentication trust level is not supported. |
| BUSY | 7 | Indicates the busy state. |
| INVALID\_PARAMETERS | 8 | Invalid parameters are detected. |
| LOCKED | 9 | The authentication executor is locked. |
| NOT\_ENROLLED | 10 | The user has not enrolled the authentication information. |

#### FaceTips(deprecated)

Enumerates the tip codes used during the facial authentication process.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/xhVVIhtOSsKgG_bdSMsXkg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062340Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=626D36D4DA4921AA4EE27A048B96422077EB786415B6759274F1EB276E22A775)

This API is supported since API version 8 and deprecated since API version 11.

**System capability**: SystemCapability.UserIAM.UserAuth.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| FACE\_AUTH\_TIP\_TOO\_BRIGHT | 1 | The obtained facial image is too bright due to high illumination. |
| FACE\_AUTH\_TIP\_TOO\_DARK | 2 | The obtained facial image is too dark due to low illumination. |
| FACE\_AUTH\_TIP\_TOO\_CLOSE | 3 | The face is too close to the device. |
| FACE\_AUTH\_TIP\_TOO\_FAR | 4 | The face is too far away from the device. |
| FACE\_AUTH\_TIP\_TOO\_HIGH | 5 | Only the upper part of the face is captured because the device is angled too high. |
| FACE\_AUTH\_TIP\_TOO\_LOW | 6 | Only the lower part of the face is captured because the device is angled too low. |
| FACE\_AUTH\_TIP\_TOO\_RIGHT | 7 | Only the right part of the face is captured because the device is deviated to the right. |
| FACE\_AUTH\_TIP\_TOO\_LEFT | 8 | Only the left part of the face is captured because the device is deviated to the left. |
| FACE\_AUTH\_TIP\_TOO\_MUCH\_MOTION | 9 | The face moves too fast during facial information collection. |
| FACE\_AUTH\_TIP\_POOR\_GAZE | 10 | The face is not facing the camera. |
| FACE\_AUTH\_TIP\_NOT\_DETECTED | 11 | No face is detected. |

#### FingerprintTips(deprecated)

Enumerates the tip codes used during the fingerprint authentication process.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/wcRmfUPuQQC2Y2EEegpeRg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062340Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=ED129336CA00BCD854FC8C211367D274B4A33CEF30032D2FF82F809857DCD78E)

This API is supported since API version 8 and deprecated since API version 11.

**System capability**: SystemCapability.UserIAM.UserAuth.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| FINGERPRINT\_AUTH\_TIP\_GOOD | 0 | The obtained fingerprint image is in good condition. |
| FINGERPRINT\_AUTH\_TIP\_DIRTY | 1 | Large fingerprint image noise is detected due to suspicious or detected dirt on the sensor. |
| FINGERPRINT\_AUTH\_TIP\_INSUFFICIENT | 2 | The noise of the fingerprint image is too large to be processed. |
| FINGERPRINT\_AUTH\_TIP\_PARTIAL | 3 | Incomplete fingerprint image is detected. |
| FINGERPRINT\_AUTH\_TIP\_TOO\_FAST | 4 | The fingerprint image is incomplete due to fast movement. |
| FINGERPRINT\_AUTH\_TIP\_TOO\_SLOW | 5 | Failed to obtain the fingerprint image because the finger seldom moves. |

#### UserAuthType8+

Enumerates the identity authentication types.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.UserIAM.UserAuth.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| PIN10+ | 1 | PIN authentication. |
| FACE | 2 | Facial authentication. |
| FINGERPRINT | 4 | Fingerprint authentication. |

#### AuthTrustLevel8+

Enumerates the trust levels of the authentication result.

For typical use cases, see [Principles for Classifying Biometric Authentication Trust Levels](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/user-authentication-overview#principles-for-classifying-biometric-authentication-trust-levels).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.UserIAM.UserAuth.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| ATL1 | 10000 | Authentication trust level 1. The authentication of this level can identify individual users and provides limited liveness detection capabilities. It is applicable to scenarios such as service risk control and access to common personal data. |
| ATL2 | 20000 | Authentication trust level 2. The authentication of this level can accurately identify individual users and provides regular liveness detection capabilities. It is applicable to scenarios such as device unlocking and application login. |
| ATL3 | 30000 | Authentication trust level 3. The authentication of this level can accurately identify individual users and provides strong liveness detection capabilities. It is applicable to scenarios such as device unlocking. |
| ATL4 | 40000 | Authentication trust level 4. The authentication of this level can accurately identify individual users and provides powerful liveness detection capabilities. It is applicable to scenarios such as small-amount payment. |

#### SecureLevel(deprecated)

type SecureLevel = string

Enumerates the authentication security levels.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/2u7U0VR-QKW1ZYUCnVUifA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062340Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=19421B0CE0F7A8426845C77D6F6E04F81A8EDE6390FA3715513FA3E0B8E36FA2)

This API is supported since API version 6 and deprecated since API version 8. Use [AuthTrustLevel](#authtrustlevel8) instead.

**System capability**: SystemCapability.UserIAM.UserAuth.Core

| Type | Description |
| :-- | :-- |
| string | Authentication security level, which can be any of the following: |

#### AuthType(deprecated)

type AuthType = string

Enumerates the authentication types.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/Pn-rIno3RaGurP71s92CgQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062340Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8DF936E77C910AB1FF18105A2AA013B358D02ADC8C3963EFB06543873D3FEBF1)

This API is supported since API version 6 and deprecated since API version 8. Use [UserAuthType](#userauthtype8) instead.

**System capability**: SystemCapability.UserIAM.UserAuth.Core

| Type | Description |
| :-- | :-- |
| string | Authentication type, which can be any of the following: |

#### userAuth.getAuthenticator(deprecated)

getAuthenticator(): Authenticator

Obtains an **Authenticator** instance for user authentication.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/esJ3fEnqRaq3efo41aBKew/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062340Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A1638AC601E20E987E3502E297AA54D5261C5A3F09381579621258FE4EC477FE)

This API is supported since API version 6 and deprecated since API version 8. Use [getAuthInstance](#userauthgetauthinstancedeprecated) instead.

**System capability**: SystemCapability.UserIAM.UserAuth.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [Authenticator](#authenticatordeprecated) | **Authenticator** instance obtained. |

**Example**

import { userAuth } from '@kit.UserAuthenticationKit';

let authenticator = userAuth.getAuthenticator();

#### Authenticator(deprecated)

Provides APIs for managing the **Authenticator** object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/eepDgOmbRdKYYgVQgzYDYg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062340Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9E292F6CCE0C3CE4BB942684EBFCAB140ACC25F2494DC3EE6D0A117EE694E188)

This API is supported since API version 6 and deprecated since API version 8. Use [AuthInstance](#authinstancedeprecated) instead.

#### \[h2\]execute(deprecated)

execute(type: AuthType, level: SecureLevel, callback: AsyncCallback<number>): void

Starts user authentication. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/07/v3/jxNDuvl3Ray8BhhZun5XXQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062340Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D628DB85806643AC36C5BADE48F5ABC415BFAEF8BF36DB9A03E0388D21FC5B66)

This API is supported since API version 6 and deprecated since API version 8. Use [start](#startdeprecated) instead.

**Required permissions**: ohos.permission.ACCESS\_BIOMETRIC

**System capability**: SystemCapability.UserIAM.UserAuth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | AuthType | Yes | 
Authentication type. Currently, only **FACE\_ONLY** is supported.

**ALL** is reserved and not supported by the current version.

 |
| level | SecureLevel | Yes | 

Security level of the authentication. It can be **S1** (lowest), **S2**, **S3**, or **S4** (highest).

Devices capable of 3D facial recognition support S3 and lower-level authentication.

Devices capable of 2D facial recognition support S2 and lower-level authentication.

 |
| callback | AsyncCallback<number> | Yes | Callback used to return the result. **number** indicates the [AuthenticationResult](#authenticationresultdeprecated). |

**Example**

import { userAuth } from '@kit.UserAuthenticationKit';

let authenticator = userAuth.getAuthenticator();
authenticator.execute('FACE\_ONLY', 'S2', (error, code)=>{
  if (code === userAuth.ResultCode.SUCCESS) {
    console.info('auth success');
    return;
  }
  console.error(\`auth fail, code = ${code}\`);
});

#### \[h2\]execute(deprecated)

execute(type : AuthType, level : SecureLevel): Promise<number>

Starts user authentication. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/TKdkA-6XR0Kp9OYyjDrr0A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062340Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=91253412747ECA45E67546DDADEB0560676A1FA0FC520136A7346DBDC675C532)

This API is supported since API version 6 and deprecated since API version 8. Use [start](#startdeprecated) instead.

**Required permissions**: ohos.permission.ACCESS\_BIOMETRIC

**System capability**: SystemCapability.UserIAM.UserAuth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | AuthType | Yes | 
Authentication type. Currently, only **FACE\_ONLY** is supported.

**ALL** is reserved and not supported by the current version.

 |
| level | SecureLevel | Yes | 

Security level of the authentication. It can be **S1** (lowest), **S2**, **S3**, or **S4** (highest).

Devices capable of 3D facial recognition support S3 and lower-level authentication.

Devices capable of 2D facial recognition support S2 and lower-level authentication.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the authentication result, which is a number. For details, see [AuthenticationResult](#authenticationresultdeprecated). |

**Example**

import { userAuth } from '@kit.UserAuthenticationKit';

try {
  let authenticator = userAuth.getAuthenticator();
  authenticator.execute('FACE\_ONLY', 'S2').then((code)=>{
    console.info('auth success');
  })
} catch (error) {
  console.error(\`auth fail, code = ${error}\`);
}

#### AuthenticationResult(deprecated)

Enumerates the authentication results.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/px87gieBQqOo0MOo1GpHjA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062340Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0280DAEF3D8225136EC1DBD5268A704F4261BDBD173432282E943FCF6DF58EA1)

This API is supported since API version 6 and deprecated since API version 8. Use [ResultCode](#resultcodedeprecated) instead.

**System capability**: SystemCapability.UserIAM.UserAuth.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| NO\_SUPPORT | \-1 | The device does not support the current authentication mode. |
| SUCCESS | 0 | The authentication is successful. |
| COMPARE\_FAILURE | 1 | The feature comparison failed. |
| CANCELED | 2 | The authentication was canceled by the user. |
| TIMEOUT | 3 | The authentication has timed out. |
| CAMERA\_FAIL | 4 | The camera failed to start. |
| BUSY | 5 | The authentication service is not available. Try again later. |
| INVALID\_PARAMETERS | 6 | The authentication parameters are invalid. |
| LOCKED | 7 | The user account is locked because the number of authentication failures has reached the threshold. |
| NOT\_ENROLLED | 8 | No authentication credential is registered. |
| GENERAL\_ERROR | 100 | Other errors. |
