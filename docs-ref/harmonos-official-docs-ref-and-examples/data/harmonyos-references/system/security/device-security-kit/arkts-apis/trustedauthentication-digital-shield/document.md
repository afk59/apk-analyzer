# TrustedAuthentication (Digital Shield)

This module provides APIs for creating, changing, and deleting digital shield passwords, API for executing transaction authentication, API for enabling biometric (3D face/fingerprint) transaction authentication, API for executing biometric transaction authentication, and APIs importing and exporting key information. Finance apps can use these APIs to support digital shield service development.

**Start version**: 6.0.0(20)

#### Module Import

import { trustedAuthentication } from '@kit.DeviceSecurityKit';

#### enableTrustedAuthentication

enableTrustedAuthentication(challenge: Uint8Array, pwdInfo: PasswordInfo, label: TUILable): Promise<AuthInfo>

Starts the trusted user interface (TUI) and instructs the user to create a digital shield password. This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.Security.TrustedAuthentication

**Start version**: 6.0.0(20)

**Parameters:**

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

challenge

 | 

Uint8Array

 | 

Yes

 | 

Challenge value obtained from [Universal Keystore Kit during session initialization](../../../universal-keystore-kit/arkts-apis/ohos-security-huks-universal-keystore/document.md#huksinitsession9) before a request is initiated. The value is a 32-byte random number.

 |
| 

pwdInfo

 | 

[PasswordInfo](#section1550072910133)

 | 

Yes

 | 

Custom password information. For details, please refer to **PasswordInfo**.

 |
| 

label

 | 

[TUILable](#section125211933134315)

 | 

Yes

 | 

Custom information for TUI display. For details, please refer to **TUILable**.

 |

**Returns:**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[AuthInfo](#section1214193712473)\>

 | 

Promise used to return the **authID** and **authToken** parameters corresponding to digital shield password enabling.

 |

**Error codes:**

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/trustedauthentication-digital-shield/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

1019100001

 | 

The interface invoker does not have the corresponding permission.

 |
| 

1019100002

 | 

Parameter error.

Possible causes:

1\. Mandatory parameters are left unspecified.

2\. Incorrect parameter types.

3\. Parameter verification failed.

 |
| 

1019100007

 | 

Unsupported custom image.

 |
| 

1019100008

 | 

The user canceled the operation.

 |
| 

1019100011

 | 

The title text cannot be displayed.

 |
| 

1019100013

 | 

Failed to set the password.

 |

**Example:**

import { trustedAuthentication} from '@kit.DeviceSecurityKit';
import { BusinessError} from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { resourceManager } from '@kit.LocalizationKit';
import { common } from '@kit.AbilityKit';

const TAG = "TrustedAuthenticationJsTest";
try {
  const rand = cryptoFramework.createRandom();
  const len: number = 32;
  const challenge: Uint8Array = rand?.generateRandomSync(len)?.data;
  const passwordInfo: trustedAuthentication.PasswordInfo = {
    pwdType: trustedAuthentication.PasswordType.PASSWORD\_TYPE\_MIXED,
    pwdMaxLength: 10,
    pwdMinLength: 6,
    maxAuthFailCount: 6
  };
  let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  const resourceMgr: resourceManager.ResourceManager = context.resourceManager;
  const fileData : Uint8Array = await resourceMgr.getRawFileContent('test\_logo\_rgba.png');
  const buffer = fileData.buffer;
  const label:trustedAuthentication.TUILable = {
    image: buffer as ArrayBuffer,
    title: "Enable Digital Shield",
  }
  const authToken = await trustedAuthentication.enableTrustedAuthentication(challenge, passwordInfo, label);
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'enableTrustedAuthentication failed: %{public}d %{public}s', e.code, e.message);
}

#### modifyTrustedAuthenticationPwd

modifyTrustedAuthenticationPwd(challenge: Uint8Array, pwdInfo: PasswordInfo, authID: bigint, label: TUILable): Promise<AuthToken>

Starts the TUI and instructs the user to change the digital shield password. The password will be authenticated based on **authID** before the change. This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.Security.TrustedAuthentication

**Start version**: 6.0.0(20)

**Parameters:**

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

challenge

 | 

Uint8Array

 | 

Yes

 | 

Challenge value obtained from [Universal Keystore Kit during session initialization](../../../universal-keystore-kit/arkts-apis/ohos-security-huks-universal-keystore/document.md#huksinitsession9) before a request is initiated. The value is a 32-byte random number.

 |
| 

pwdInfo

 | 

[PasswordInfo](#section1550072910133)

 | 

Yes

 | 

Custom password information.

 |
| 

authID

 | 

bigint

 | 

Yes

 | 

**authID** obtained during password creation.

 |
| 

label

 | 

[TUILable](#section125211933134315)

 | 

Yes

 | 

Custom information for TUI display.

 |

**Returns:**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[AuthToken](#section20919104010476)\>

 | 

Promise used to return the **authToken** corresponding to digital shield password change.

 |

**Error codes:**

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/trustedauthentication-digital-shield/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

1019100001

 | 

The interface invoker does not have the corresponding permission.

 |
| 

1019100002

 | 

Parameter error.

Possible causes:

1\. Mandatory parameters are left unspecified.

2\. Incorrect parameter types.

3\. Parameter verification failed.

 |
| 

1019100003

 | 

The maximum number of password authentication attempts has been reached.

 |
| 

1019100005

 | 

Face/Fingerprint/Password authentication failed.

 |
| 

1019100007

 | 

Unsupported custom image.

 |
| 

1019100008

 | 

The user canceled the operation.

 |
| 

1019100011

 | 

The title text cannot be displayed.

 |
| 

1019100012

 | 

Invalid authentication ID.

 |
| 

1019100014

 | 

Failed to change the password.

 |

**Example:**

import { trustedAuthentication} from '@kit.DeviceSecurityKit';
import { BusinessError} from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { resourceManager } from '@kit.LocalizationKit';
import { common } from '@kit.AbilityKit';

const TAG = "TrustedAuthenticationJsTest";

try {
 const rand = cryptoFramework.createRandom();
 const len: number = 32;
 const challenge: Uint8Array = rand?.generateRandomSync(len)?.data;
 const passwordInfo: trustedAuthentication.PasswordInfo = {
   pwdType: trustedAuthentication.PasswordType.PASSWORD\_TYPE\_DIGITAL,
   pwdMaxLength: 10,
   pwdMinLength: 6,
   maxAuthFailCount: 6,
 };
 const authID: bigint = 1687413472599354502n;
 let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
 const resourceMgr: resourceManager.ResourceManager = context.resourceManager;
 const fileData : Uint8Array = await resourceMgr.getRawFileContent('test\_logo\_rgba.png');
 const buffer = fileData.buffer;
 const label:trustedAuthentication.TUILable = {
   image: buffer as ArrayBuffer,
   title: "Change Password",
 }
 const authToken = await trustedAuthentication.modifyTrustedAuthenticationPwd(challenge, passwordInfo, authID, label);
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'modifyTrustedAuthenticationPwd failed: %{public}d %{public}s', e.code, e.message);
}

#### disableTrustedAuthentication

disableTrustedAuthentication(challenge: Uint8Array, needAuth: boolean, authID: bigint, label: TUILable): Promise<AuthToken>

Disables the digital shield service. You can use the **needAuth** parameter to specify whether password authentication is required for digital shield disabling. This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.Security.TrustedAuthentication

**Start version**: 6.0.0(20)

**Parameters:**

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

challenge

 | 

Uint8Array

 | 

Yes

 | 

When the value of **needAuth** is **true**, the challenge value is a 32-byte random number obtained from [Universal Keystore Kit during session initialization](../../../universal-keystore-kit/arkts-apis/ohos-security-huks-universal-keystore/document.md#huksinitsession9) before a request is initiated.

When the value of **needAuth** is **false**, the challenge value can be any 32-byte number and does not need to be obtained from Universal Keystore Kit.

 |
| 

needAuth

 | 

boolean

 | 

Yes

 | 

Indicates whether password authentication is required for disabling the digital shield service.

When the value is **false**, password authentication is not required.

When the value is **true**, password authentication is required. The digital shield service can be disabled only after password authentication succeeds.

 |
| 

authID

 | 

bigint

 | 

Yes

 | 

**authID** obtained during password creation.

 |
| 

label

 | 

[TUILable](#section125211933134315)

 | 

Yes

 | 

Custom information for TUI display.

 |

**Returns:**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[AuthToken](#section20919104010476)\>

 | 

Promise used to return the **authToken** corresponding to digital shield password deletion. When **needAuth** is set to **false**, the returned **authToken** is an invalid value with all zeros.

 |

**Error codes:**

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/trustedauthentication-digital-shield/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

1019100001

 | 

The interface invoker does not have the corresponding permission.

 |
| 

1019100002

 | 

Parameter error.

Possible causes:

1\. Mandatory parameters are left unspecified.

2\. Incorrect parameter types.

3\. Parameter verification failed.

 |
| 

1019100003

 | 

The maximum number of password authentication attempts has been reached.

 |
| 

1019100004

 | 

Failed to delete the password.

 |
| 

1019100005

 | 

Face/Fingerprint/Password authentication failed.

 |
| 

1019100007

 | 

Unsupported custom image.

 |
| 

1019100008

 | 

The user canceled the operation.

 |
| 

1019100011

 | 

The title text cannot be displayed.

 |
| 

1019100012

 | 

Invalid authentication ID.

 |

**Example:**

import { trustedAuthentication} from '@kit.DeviceSecurityKit';
import { BusinessError} from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { resourceManager } from '@kit.LocalizationKit';
import { common } from '@kit.AbilityKit';

const TAG = "TrustedAuthenticationJsTest";

try {
 const rand = cryptoFramework.createRandom();
 const len: number = 32;
 const challenge: Uint8Array = rand?.generateRandomSync(len)?.data;
 const authID: bigint = 1687413472599354502n;
 let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
 const resourceMgr: resourceManager.ResourceManager = context.resourceManager;
 const fileData : Uint8Array = await resourceMgr.getRawFileContent('test\_logo\_rgba.png');
 const buffer = fileData.buffer;
 const label:trustedAuthentication.TUILable = {
   image: buffer as ArrayBuffer,
   title: "Disable Digital Shield",
 }
 const authToken = await trustedAuthentication.disableTrustedAuthentication(challenge, true, authID, label);
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'disableTrustedAuthentication failed: %{public}d %{public}s', e.code, e.message);
}

#### trustedAuthentication

trustedAuthentication(challenge: Uint8Array, authID: bigint, label: TUILable): Promise<AuthToken>

Provides the digital shield password authentication capability. You can call this API to complete password authentication before binding biometric information for payment authentication. This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.Security.TrustedAuthentication

**Start version**: 6.0.0(20)

**Parameters:**

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

challenge

 | 

Uint8Array

 | 

Yes

 | 

Challenge value obtained from [Universal Keystore Kit during session initialization](../../../universal-keystore-kit/arkts-apis/ohos-security-huks-universal-keystore/document.md#huksinitsession9) before a request is initiated. The value is a 32-byte random number.

 |
| 

authID

 | 

bigint

 | 

Yes

 | 

**authID** obtained during password creation.

 |
| 

label

 | 

[TUILable](#section125211933134315)

 | 

Yes

 | 

Custom information for TUI display.

 |

**Returns:**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[AuthToken](#section20919104010476)\>

 | 

Promise used to return the **authToken** corresponding to digital shield password authentication.

 |

**Error codes:**

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/trustedauthentication-digital-shield/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

1019100001

 | 

The interface invoker does not have the corresponding permission.

 |
| 

1019100002

 | 

Parameter error.

Possible causes:

1\. Mandatory parameters are left unspecified.

2\. Incorrect parameter types.

3\. Parameter verification failed.

 |
| 

1019100003

 | 

The maximum number of password authentication attempts has been reached.

 |
| 

1019100005

 | 

Face/Fingerprint/Password authentication failed.

 |
| 

1019100007

 | 

Unsupported custom image.

 |
| 

1019100008

 | 

The user canceled the operation.

 |
| 

1019100012

 | 

Invalid authentication ID.

 |

**Example:**

import { trustedAuthentication} from '@kit.DeviceSecurityKit';
import { BusinessError} from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { resourceManager } from '@kit.LocalizationKit';
import { common } from '@kit.AbilityKit';

const TAG = "TrustedAuthenticationJsTest";

try {
 const rand = cryptoFramework.createRandom();
 const len: number = 32;
 const challenge: Uint8Array = rand?.generateRandomSync(len)?.data;
 const authID: bigint = 1687413472599354502n;
 let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
 const resourceMgr: resourceManager.ResourceManager = context.resourceManager;
 const fileData : Uint8Array = await resourceMgr.getRawFileContent('test\_logo\_rgba.png');
 const buffer = fileData.buffer;
 const label:trustedAuthentication.TUILable = {
   image: buffer as ArrayBuffer,
   title: "Password Authentication",
 }
 const authToken = await trustedAuthentication.trustedAuthentication(challenge, authID, label);
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'trustedAuthentication failed: %{public}d %{public}s', e.code, e.message);
}

#### procContentAuthentication

procContentAuthentication(challenge: Uint8Array, authID: bigint, authMsg: AuthReqParams, label: TUILable): Promise<AuthToken>

Authenticates a transaction. This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.Security.TrustedAuthentication

**Start version**: 6.0.0(20)

**Parameters:**

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

challenge

 | 

Uint8Array

 | 

Yes

 | 

Challenge value obtained from [Universal Keystore Kit during session initialization](../../../universal-keystore-kit/arkts-apis/ohos-security-huks-universal-keystore/document.md#huksinitsession9) before a request is initiated. The value is a 32-byte random number.

 |
| 

authID

 | 

bigint

 | 

Yes

 | 

**authID** obtained during password creation.

 |
| 

authMsg

 | 

[AuthReqParams](#section3989356115014)

 | 

Yes

 | 

Transaction authentication request parameters.

 |
| 

label

 | 

[TUILable](#section125211933134315)

 | 

Yes

 | 

Custom information for TUI display.

 |

**Returns:**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[AuthToken](#section20919104010476)\>

 | 

Promise object.

When password authentication is used, the returned result includes the **authToken** of the transaction data.

During biometric authentication, the returned result is a temporary **authToken**. After biometric authentication is successful, [getBiometricAuthToken](#section627215120542) must be called to obtain the officially issued **authToken** containing transaction information.

 |

**Error codes:**

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/trustedauthentication-digital-shield/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

1019100001

 | 

The interface invoker does not have the corresponding permission.

 |
| 

1019100002

 | 

Parameter error.

Possible causes:

1\. Mandatory parameters are left unspecified.

2\. Incorrect parameter types.

3\. Parameter verification failed.

 |
| 

1019100005

 | 

Face/Fingerprint/Password authentication failed.

 |
| 

1019100008

 | 

The user canceled the operation.

 |
| 

1019100011

 | 

The text content cannot be displayed.

 |
| 

1019100012

 | 

Invalid authentication ID.

 |
| 

1019100021

 | 

The corresponding biometric data has not been bound.

 |

**Example:**

import { trustedAuthentication} from '@kit.DeviceSecurityKit';
import { BusinessError} from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { resourceManager } from '@kit.LocalizationKit';
import { common } from '@kit.AbilityKit';

const TAG = "TrustedAuthenticationJsTest";

try {
 const rand = cryptoFramework.createRandom();
 const len: number = 32;
 const challenge: Uint8Array = rand?.generateRandomSync(len)?.data;
 const authID: bigint = 1687413472599354502n;
 let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
 const resourceMgr: resourceManager.ResourceManager = context.resourceManager;
 const fileData : Uint8Array = await resourceMgr.getRawFileContent('test\_logo\_rgba.png');
 const reqParams:trustedAuthentication.AuthReqParams = {
  reqType: trustedAuthentication.AuthType.AUTH\_TYPE\_TUI\_PIN,
  authContent: \["User: John xx", "Account: 95588180804408xxxx", "Transaction amount: 1000000000"\],
 }
 const buffer = fileData.buffer;
 const label:trustedAuthentication.TUILable = {
  image: buffer as ArrayBuffer,
  title: "Password-based Transaction Authentication",
 }
 const result = await trustedAuthentication.procContentAuthentication(challenge, authID, reqParams, label);
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'procContentAuthentication failed: %{public}d %{public}s', e.code, e.message);
}

#### getBiometricAuthToken

getBiometricAuthToken(operType: OperateType, tuiAuthToken: Uint8Array, bioAuthToken: Uint8Array): Promise<AuthToken>

Obtains the **authToken** corresponding to biometric binding or biometric transaction authentication. This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.Security.TrustedAuthentication

**Start version**: 6.0.0(20)

**Parameters:**

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

operType

 | 

[OperateType](#section14617053498)

 | 

Yes

 | 

Operation type for obtaining the **authToken**. For details, please refer to [OperateType](#section14617053498).

 |
| 

tuiAuthToken

 | 

Uint8Array

 | 

Yes

 | 

When the operation type is **OPERATE\_TYPE\_BIOMETRIC\_AUTH**, **tuiAuthToken** indicates the **authToken** information obtained through password authentication ([trustedAuthentication](#section6763105845111)).

When the operation type is **OPERATE\_TYPE\_CONTENT\_AUTH**, **tuiAuthToken** indicates the **authToken** information obtained through temporary transaction information confirmation ([procContentAuthentication](#section1381398185415)).

 |
| 

bioAuthToken

 | 

Uint8Array

 | 

Yes

 | 

**authToken** obtained through biometric authentication. The **tuiAuthToken** and **bioAuthToken** must be obtained using the same challenge, that is, the two **authToken**s must be obtained using the same session.

 |

**Returns:**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[AuthToken](#section20919104010476)\>

 | 

Promise object.

In the biometric binding process, the obtained **authToken** contains the biometric feature ID and is issued after being authenticated by the digital shield service.

In the biometric transaction authentication process, the obtained **authToken** contains the transaction information and biometric feature ID, but has not been authenticated by the digital shield service.

 |

**Error codes:**

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/trustedauthentication-digital-shield/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

1019100001

 | 

The interface invoker does not have the corresponding permission.

 |
| 

1019100002

 | 

Parameter error.

Possible causes:

1\. Mandatory parameters are left unspecified.

2\. Incorrect parameter types.

3\. Parameter verification failed.

 |
| 

1019100005

 | 

Face/Fingerprint/Password authentication failed.

 |
| 

1019100015

 | 

Failed to get the biometric authToken.

 |
| 

1019100019

 | 

The biometric data for authentication does not match the bound biometric feature.

 |
| 

1019100020

 | 

The biometric data has already been bound.

 |

**Example:**

import { userAuth } from '@kit.UserAuthenticationKit';
import { trustedAuthentication} from '@kit.DeviceSecurityKit';
import { BusinessError} from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { resourceManager } from '@kit.LocalizationKit';
import { common } from '@kit.AbilityKit';

const TAG = "TrustedAuthenticationJsTest";

function async PwdVerify(challenge: Uint8Array):Promise<trustedAuthentication.AuthToken> {
  try {
    const authID: bigint = 11842183505170721246n;// In actual use, replace the value with the authID of the account obtained from the server.
    let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
    const resourceMgr: resourceManager.ResourceManager = context.resourceManager;
    const fileData : Uint8Array = await resourceMgr.getRawFileContent('test\_logo\_rgba.png'); // In actual use, replace the value with the name of the app logo image to be displayed on the TUI.
    const buffer = fileData.buffer;
    const label:trustedAuthentication.TUILable = {
      image: buffer as ArrayBuffer,
      title: "Digital Shield Password Authentication",
    }
    const result = await trustedAuthentication.trustedAuthentication(challenge, authID, label);
    return result;
  } catch (err) {  
    hilog.error(0x0000, 'testTag', \`Failed to trustedAuthentication, code:${err.code}, message:${err.message}\`);
    throw new Error('Password verify failed:' + (err as BusinessError).message);
  }
}

const rand = cryptoFramework.createRandom();
const len: number = 32;
let challenge: Uint8Array = rand?.generateRandomSync(len)?.data;
const TuiAuthToken: trustedAuthentication.AuthToken = await PwdVerify(challenge);
let authTypeList :number\[\] = new Array();
authTypeList\[0\] = userAuth.UserAuthType.FINGERPRINT;
authTypeList\[1\] = userAuth.UserAuthType.FACE;

const authParam : userAuth.AuthParam = {
  challenge:  session.challenge as Uint8Array,
  authType: authTypeList,
  authTrustLevel: userAuth.AuthTrustLevel.ATL4
};
const widgetParam: userAuth.WidgetParam = {
  title: 'Enter Digital Shield Password',
  navigationButtonText: 'Enter Digital Shield Password',
};

try {
  const userAuthInstance = await userAuth.getUserAuthInstance(authParam, widgetParam);
  userAuthInstance.on('result', {
	onResult (result) {
	  authTokenData = result.token;
	  let operType = trustedAuthentication.OperateType.OPERATE\_TYPE\_BIOMETRIC\_AUTH;
	  trustedAuthentication.getBiometricAuthToken(operType, TuiAuthToken.authToken, authTokenData).then((newAuthToken) => {
	    let authToken = newAuthToken.authToken as Uint8Array;
		hilog.info("---authToken---" + authToken);
	  });
	}
  })
  userAuthInstance.start();
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'getUserAuthInstance failed: %{public}d %{public}s', e.code, e.message);
}

#### importData

importData(data: ArrayBuffer, authID: bigint): Promise<void>

Imports backup data (the encryption key information used during HUKS signing and signature verification). This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.Security.TrustedAuthentication

**Start version**: 6.0.0(20)

**Parameters:**

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

data

 | 

ArrayBuffer

 | 

Yes

 | 

Generally, this parameter is set to the **wrapkey** data obtained from Universal Keystore Kit. The imported data cannot exceed 2048 bytes. The data cannot be imported repeatedly.

 |
| 

authID

 | 

bigint

 | 

Yes

 | 

**authID** obtained during password creation.

 |

**Returns:**

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

**Error codes:**

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/trustedauthentication-digital-shield/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

1019100001

 | 

The interface invoker does not have the corresponding permission.

 |
| 

1019100002

 | 

Parameter error.

Possible causes:

1\. Mandatory parameters are left unspecified.

2\. Incorrect parameter types.

3\. Parameter verification failed.

 |
| 

1019100010

 | 

Failed to import data.

 |
| 

1019100012

 | 

Invalid authentication ID.

 |

**Example:**

import { trustedAuthentication} from '@kit.DeviceSecurityKit';
import { BusinessError} from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = "TrustedAuthenticationJsTest";

try {
 const authID: bigint = 1687413472599354502n;
 const buffer = new ArrayBuffer(8);
 const bufferArray = new Uint8Array(buffer);
 bufferArray.set(\[1, 2, 3, 4, 5, 6, 7, 8\]);
 const result = await trustedAuthentication.importData(buffer, authID);
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'importData failed: %{public}d %{public}s', e.code, e.message);
}

#### exportData

exportData(authID: bigint, label: TUILable): Promise<ArrayBuffer>

Exports backup data (the encryption key information used during HUKS signing and signature verification). The backup data can be exported only after the password authentication is successful. This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.Security.TrustedAuthentication

**Start version**: 6.0.0(20)

**Parameters:**

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

authID

 | 

bigint

 | 

Yes

 | 

**authID** obtained during password creation.

 |
| 

label

 | 

[TUILable](#section125211933134315)

 | 

Yes

 | 

Custom information for TUI display. For details, please refer to [TUILable](#section125211933134315).

 |

**Returns:**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<ArrayBuffer>

 | 

Promise used to return the backup data.

 |

**Error codes:**

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/trustedauthentication-digital-shield/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

1019100001

 | 

The interface invoker does not have the corresponding permission.

 |
| 

1019100002

 | 

Parameter error.

Possible causes:

1\. Mandatory parameters are left unspecified.

2\. Incorrect parameter types.

3\. Parameter verification failed.

 |
| 

1019100009

 | 

Failed to export data.

 |
| 

1019100012

 | 

Invalid authentication ID.

 |

**Example:**

import { trustedAuthentication} from '@kit.DeviceSecurityKit';
import { BusinessError} from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { resourceManager } from '@kit.LocalizationKit';
import { common } from '@kit.AbilityKit';

const TAG = "TrustedAuthenticationJsTest";

try {
 const credentialID: bigint = 1687413472599354502n;
 let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
 const resourceMgr: resourceManager.ResourceManager = context.resourceManager;
 const fileData : Uint8Array = await resourceMgr.getRawFileContent('test\_logo\_rgba.png');
 const buffer = fileData.buffer;
 const label:trustedAuthentication.TUILable = {
  image: buffer as ArrayBuffer,
  title: "Export Backup Data",
 }
 const result = await trustedAuthentication.exportData(credentialID, label);
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'exportData failed: %{public}d %{public}s', e.code, e.message);
}

#### checkConfirmUITextFormat

checkConfirmUITextFormat(text: string): Promise<TextCheckResult>

Checks whether the content to be displayed on the TUI can be completely displayed in a single line on the screen. This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.Security.TrustedAuthentication

**Start version**: 6.0.0(20)

**Parameters:**

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

text

 | 

string

 | 

Yes

 | 

Authentication information to be displayed on the TUI. Before transaction authentication, you can use this API to check whether the transaction information can be completely displayed in a single line on the screen. The length of the transaction information ranges from 1 to 200 bytes.

 |

**Returns:**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[TextCheckResult](#section27021232135111)\>

 | 

Promise used to return the check result about the display of the specified text on the TUI.

 |

**Error codes:**

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/trustedauthentication-digital-shield/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

1019100001

 | 

The interface invoker does not have the corresponding permission.

 |
| 

1019100002

 | 

Parameter error.

Possible causes:

1\. Mandatory parameters are left unspecified.

2\. Incorrect parameter types.

3\. Parameter verification failed.

 |
| 

1019100006

 | 

Check input confirm text failed.

 |

**Example:**

import { trustedAuthentication} from '@kit.DeviceSecurityKit';
import { BusinessError} from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = "TrustedAuthenticationJsTest";

try {
 const text: string = "Check whether the text to be displayed on the TUI can be properly displayed.";
 const result = await trustedAuthentication.checkConfirmUITextFormat(text);
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'checkConfirmUITextFormat failed: %{public}d %{public}s', e.code, e.message);
}

#### getRemainAuthTimes

getRemainAuthTimes(authID: bigint): Promise<number>

Obtains the number of remaining authentication times of the digital shield. This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.Security.TrustedAuthentication

**Start version**: 6.0.0(20)

**Parameters:**

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

authID

 | 

bigint

 | 

Yes

 | 

**authID** obtained during password creation.

 |

**Returns:**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<number>

 | 

Promise used to return the number of remaining authentication times of the digital shield.

 |

**Error codes:**

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/trustedauthentication-digital-shield/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

1019100001

 | 

The interface invoker does not have the corresponding permission.

 |
| 

1019100002

 | 

Parameter error.

Possible causes:

1\. Mandatory parameters are left unspecified.

2\. Incorrect parameter types.

3\. Parameter verification failed.

 |
| 

1019100012

 | 

Invalid authentication ID.

 |
| 

1019100017

 | 

Failed to get the remaining number of authentication attempts.

 |

**Example:**

import { trustedAuthentication} from '@kit.DeviceSecurityKit';
import { BusinessError} from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = "TrustedAuthenticationJsTest";

try {
 const authID: bigint = 1687413472599354502n;
 const remainTimes = await trustedAuthentication.getRemainAuthTimes(authID);
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'getRemainAuthTimesfailed: %{public}d %{public}s', e.code, e.message);
}

#### disableTrustedBioAuthentication

disableTrustedBioAuthentication(authID: bigint, authType: AuthType): Promise<void>

Disables the authentication capability of a specified biometric feature. This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.Security.TrustedAuthentication

**Start version**: 6.0.0(20)

**Parameters:**

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

authID

 | 

bigint

 | 

Yes

 | 

**authID** obtained during password creation.

 |
| 

authType

 | 

AuthType

 | 

Yes

 | 

The value can only be **AUTH\_TYPE\_FACE** or **AUTH\_TYPE\_FINGERPRINT**.

 |

**Returns:**

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

**Error codes:**

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/trustedauthentication-digital-shield/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

1019100001

 | 

The interface invoker does not have the corresponding permission.

 |
| 

1019100002

 | 

Parameter error.

Possible causes:

1\. Mandatory parameters are left unspecified.

2\. Incorrect parameter types.

3\. Parameter verification failed.

 |
| 

1019100012

 | 

Invalid authentication ID.

 |
| 

1019100018

 | 

Failed to unbind the corresponding biometric data.

 |
| 

1019100021

 | 

The corresponding biometric data has not been bound.

 |

**Example:**

import { trustedAuthentication} from '@kit.DeviceSecurityKit';
import { BusinessError} from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = "TrustedAuthenticationJsTest";

try {
 const authID: bigint = 1687413472599354502n;
 const remainTimes = await trustedAuthentication.disableTrustedBioAuthentication(authID, trustedAuthentication.AuthType.AUTH\_TYPE\_FACE);
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'disableTrustedBioAuthentication: %{public}d %{public}s', e.code, e.message);
}

#### PasswordInfo

Specifies the requirements on the password parameters during password setup.

**System capability**: SystemCapability.Security.TrustedAuthentication

**Start version**: 6.0.0(20)

| 
**Name**

 | 

**Type**

 | 

**Read-Only**

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

pwdType

 | 

[PasswordType](#section1365374114910)

 | 

No

 | 

No

 | 

Password type. For details about the value range, please refer to [PasswordType](#section1365374114910).

 |
| 

pwdMaxLength

 | 

number

 | 

No

 | 

No

 | 

Maximum password length. The value ranges from 6 to 18.

 |
| 

pwdMinLength

 | 

number

 | 

No

 | 

No

 | 

Minimum password length. The value ranges from 6 to 18 and must be less than or equal to the value of **pwdMaxLength**.

 |
| 

maxAuthFailCount

 | 

number

 | 

No

 | 

No

 | 

Maximum number of consecutive password authentication failures. The value ranges from 1 to 10.

 |

#### TUILable

Custom information on the TUI, including the logo and page title.

**System capability**: SystemCapability.Security.TrustedAuthentication

**Start version**: 6.0.0(20)

| 
**Name**

 | 

**Type**

 | 

**Read-Only**

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

image

 | 

ArrayBuffer

 | 

No

 | 

No

 | 

Custom logo information. The image must be in PNG RGBA format, and the maximum width and height must be 216 px.

 |
| 

title

 | 

string

 | 

No

 | 

No

 | 

Custom TUI page title. The maximum length is 31 bytes.

 |

#### AuthInfo

Parameters for enabling the digital shield service.

**System capability**: SystemCapability.Security.TrustedAuthentication

**Start version**: 6.0.0(20)

| 
**Name**

 | 

**Type**

 | 

**Read-Only**

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

authToken

 | 

Uint8Array

 | 

No

 | 

No

 | 

**authToken** information, including the password **authID**.

 |
| 

authID

 | 

bigint

 | 

No

 | 

No

 | 

**authID** of the digital shield password, which is an index for password authentication, deletion, and change.

 |

#### AuthToken

**authToken** obtained after a specified digital shield operation. The encrypted information contained in the **authToken** varies depending on the operation process. For details, please refer to the parameter description of each API.

**System capability**: SystemCapability.Security.TrustedAuthentication

**Start version**: 6.0.0(20)

| 
**Name**

 | 

**Type**

 | 

**Read-Only**

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

authToken

 | 

Uint8Array

 | 

No

 | 

No

 | 

**authToken** in an operation process.

 |

#### AuthType

Defines the transaction authentication type.

**System capability**: SystemCapability.Security.TrustedAuthentication

**Start version**: 6.0.0(20)

| 
**Name**

 | 

Value

 | 

**Description**

 |
| :-- | :-- | :-- |
| 

AUTH\_TYPE\_FACE

 | 

2

 | 

Facial authentication.

 |
| 

AUTH\_TYPE\_FINGERPRINT

 | 

4

 | 

Fingerprint authentication.

 |
| 

AUTH\_TYPE\_TUI\_PIN

 | 

32

 | 

TUI password authentication.

 |

#### PasswordType

Defines the password type. The secure keyboard displayed on the TUI varies depending on the password type.

**System capability**: SystemCapability.Security.TrustedAuthentication

**Start version**: 6.0.0(20)

| 
**Name**

 | 

Value

 | 

**Description**

 |
| :-- | :-- | :-- |
| 

PASSWORD\_TYPE\_DIGITAL

 | 

0

 | 

Numeric password containing only digits.

 |
| 

PASSWORD\_TYPE\_MIXED

 | 

1

 | 

Alphanumeric password containing digits and other characters.

 |

#### OperateType

Defines the operation type.

**System capability**: SystemCapability.Security.TrustedAuthentication

**Start version**: 6.0.0(20)

| 
**Name**

 | 

Value

 | 

**Description**

 |
| :-- | :-- | :-- |
| 

OPERATE\_TYPE\_BIOMETRIC\_AUTH

 | 

1

 | 

Binds biometric features to password authentication.

 |
| 

OPERATE\_TYPE\_CONTENT\_AUTH

 | 

2

 | 

Uses biometric features for transaction authentication.

 |

#### AuthReqParams

Defines transaction authentication request parameters.

**System capability**: SystemCapability.Security.TrustedAuthentication

**Start version**: 6.0.0(20)

| 
**Name**

 | 

**Type**

 | 

**Read-Only**

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

reqType

 | 

[AuthType](#section58527274920)

 | 

No

 | 

No

 | 

Authentication type. For details about the value range, please refer to [AuthType](#section58527274920).

 |
| 

authContent

 | 

Array<string>

 | 

No

 | 

No

 | 

Authentication data, that is, transaction data in the transaction scenario. The size of a single data record cannot exceed 200 bytes.

 |

#### TextCheckResult

Defines the check result of whether text information can be displayed in a single line on the TUI.

**System capability**: SystemCapability.Security.TrustedAuthentication

**Start version**: 6.0.0(20)

| 
**Name**

 | 

**Type**

 | 

**Read-Only**

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

result

 | 

number

 | 

No

 | 

No

 | 

Check result of the input text. If the text can be properly displayed, **0** is returned. Otherwise, [1019100011 Invalid TUI Authentication Information](../arkts-api-error-codes/trustedauthentication-digital-shield/document.md#section19615182019615) is returned.

 |
| 

lastIndex

 | 

number

 | 

No

 | 

No

 | 

Index of the last character that can be properly displayed in the input string.

 |

#### TrustedAuthErrorCode

Error code indicating the execution failure of a digital shield open API.

**System capability**: SystemCapability.Security.TrustedAuthentication

**Start version**: 6.0.0(20)

| 
**Name**

 | 

Value

 | 

**Description**

 |
| :-- | :-- | :-- |
| 

TRUSTED\_AUTH\_ERROR\_NO\_PERMISSION

 | 

1019100001

 | 

Permission verification failed.

 |
| 

TRUSTED\_AUTH\_ERROR\_ILLEGAL\_ARGUMENT

 | 

1019100002

 | 

Parameter check failed.

 |
| 

TRUSTED\_AUTH\_ERROR\_PWD\_LIMIT\_REACHED

 | 

1019100003

 | 

The number of consecutive password authentication failures reaches the upper limit defined by the app.

 |
| 

TRUSTED\_AUTH\_ERROR\_PWD\_DELETE\_FAILED

 | 

1019100004

 | 

Failed to delete the password.

 |
| 

TRUSTED\_AUTH\_ERROR\_VERIFY\_FAILED

 | 

1019100005

 | 

Password authentication failed.

 |
| 

TRUSTED\_AUTH\_ERROR\_CHECK\_CONFIRM\_TEXT\_FAILED

 | 

1019100006

 | 

Input text check failed.

 |
| 

TRUSTED\_AUTH\_ERROR\_NOT\_SUPPORT\_IMAGE

 | 

1019100007

 | 

Unsupported image format.

 |
| 

TRUSTED\_AUTH\_ERROR\_USER\_REQ\_CANCEL

 | 

1019100008

 | 

The user canceled the operation.

 |
| 

TRUSTED\_AUTH\_ERROR\_EXPORT\_DATA\_FAILED

 | 

1019100009

 | 

Failed to export the backup data.

 |
| 

TRUSTED\_AUTH\_ERROR\_IMPORT\_DATA\_FAILED

 | 

1019100010

 | 

Failed to import the backup data.

 |
| 

TRUSTED\_AUTH\_ERROR\_INVALID\_CONTENT

 | 

1019100011

 | 

Invalid TUI authentication information.

 |
| 

TRUSTED\_AUTH\_ERROR\_INVALID\_AUTH\_ID

 | 

1019100012

 | 

Invalid authID.

 |
| 

TRUSTED\_AUTH\_ERROR\_SET\_PWD\_FAILED

 | 

1019100013

 | 

Failed to create the password.

 |
| 

TRUSTED\_AUTH\_ERROR\_MODIFY\_PWD\_FAILED

 | 

1019100014

 | 

Failed to change the password.

 |
| 

TRUSTED\_AUTH\_ERROR\_BIO\_RESIGN\_FAILED

 | 

1019100015

 | 

Failed to issue the authToken for biometric authentication.

 |
| 

TRUSTED\_AUTH\_FEATURE\_INITIALIZATION\_FAILED

 | 

1019100016

 | 

The digital shield service is not enabled.

 |
| 

TRUSTED\_AUTH\_ERROR\_GET\_REMAIN\_TIME

 | 

1019100017

 | 

Failed to obtain the number of remaining authentication times of the digital shield.

 |
| 

TRUSTED\_AUTH\_ERROR\_DISABLE\_BIO\_AUTH

 | 

1019100018

 | 

Failed to disable the authentication capability of a specified biometric feature.

 |
| 

TRUSTED\_AUTH\_ERROR\_BIO\_MISMATCH

 | 

1019100019

 | 

The authenticated biometric feature does not match the bound biometric feature.

 |
| 

TRUSTED\_AUTH\_ERROR\_BIO\_REPEATED\_BIND

 | 

1019100020

 | 

The biometric feature has been bound.

 |
| 

TRUSTED\_AUTH\_ERROR\_NOT\_BIND\_BIO

 | 

1019100021

 | 

The biometric feature is not bound.

 |
