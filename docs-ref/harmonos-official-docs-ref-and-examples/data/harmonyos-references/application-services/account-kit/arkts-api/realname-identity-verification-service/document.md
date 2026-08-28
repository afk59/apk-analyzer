# realName (Identity Verification Service)

This module provides the identity verification capabilities of Account Kit, including face-based identity verification. In scenarios where identity verification is required, you need to verify the user's identity information to ensure its accuracy.

**Start version**: 5.0.0(12)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/MLlUTaS9QFmhvDbFxxw7nA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062500Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=933F4AB191C28D9117B520B6DDE7DE668DFAEF816EE650BDB4C779EC56B51511)

This API is temporarily unavailable.

#### Module Import

import { realName } from '@kit.AccountKit';

#### FacialRecognitionVerificationRequest

Request object for face-based identity verification, which defines request parameters.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.RealNameVerify

**Start version**: 5.0.0(12)

| 
**Name**

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

verificationToken

 | 

string

 | 

No

 | 

No

 | 

Identity verification token, which is obtained by calling the [Verifying Real-Name Information](../../rest-apis/completing-real-name-verification/verifying-real-name-information/document.md) API of the OpenRealName service. The value contains 1 to 2048 characters.

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

The default value is **undefined**.

You are advised to use nonces and perform consistency verification. [util.generateRandomUUID()](../../../../application-framework/arkts/arkts-apis/ohos-util-util/document.md#utilgeneraterandomuuid9) is recommended.

 |

**Example**:

import { realName } from '@kit.AccountKit';
import { util } from '@kit.ArkTS';

const request: realName.FacialRecognitionVerificationRequest = {
  verificationToken: "_xxx_", // Call the real-name information verification API of the OpenRealName service to obtain this token.
  state: util.generateRandomUUID() // You are advised to use **generateRandomUUID** to generate a state.
}

#### FacialRecognitionVerificationResult

Request result object for face-based identity verification, which defines result parameters. If this object is returned, face-based identity verification is successful.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.RealNameVerify

**Start version**: 5.0.0(12)

| 
**Name**

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

facialRecognitionVerificationToken

 | 

string

 | 

Yes

 | 

No

 | 

Face-based identity verification token, which is returned after successful verification. The value contains 1 to 2048 characters.

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

You are advised to use nonces and perform consistency verification. [util.generateRandomUUID()](../../../../application-framework/arkts/arkts-apis/ohos-util-util/document.md#utilgeneraterandomuuid9) is recommended.

 |

#### RealNameErrorCode

Enumerates error codes of the identity verification service provided by Account Kit.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.RealNameVerify

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

NETWORK\_ERROR

 | 

[1002500001](../../arkts-error-codes/document.md#section126501952132317)

 | 

The network is unavailable.

 |
| 

ACCOUNT\_NOT\_LOGGED\_IN

 | 

[1002500002](../../arkts-error-codes/document.md#section1651105232319)

 | 

The user has not signed in with their HUAWEI ID.

 |
| 

PACKAGE\_FINGERPRINT\_CHECK\_ERROR

 | 

[1002500003](../../arkts-error-codes/document.md#section665175210236)

 | 

The certificate fingerprint of the app fails to be verified.

 |
| 

PERMISSION\_CHECK\_ERROR

 | 

[1002500004](../../arkts-error-codes/document.md#section17651105272310)

 | 

The app does not have the required permissions.

 |
| 

USER\_CANCELED

 | 

[1002500005](../../arkts-error-codes/document.md#section1995615923313)

 | 

The user cancels verification.

 |
| 

INTERNAL\_ERROR

 | 

[1002500006](../../arkts-error-codes/document.md#section10196176171810)

 | 

Internal error.

 |
| 

REAL\_NAME\_UNSUPPORTED

 | 

[1002500008](../../arkts-error-codes/document.md#section177525511359)

 | 

The HUAWEI ID does not support real-name information verification.

 |
| 

REAL\_NAME\_VERIFICATION\_ERROR

 | 

[1002500009](../../arkts-error-codes/document.md#section1055112416269)

 | 

Failed to verify the real-name channel.

 |
| 

FACE\_NOT\_MATCH

 | 

[1002500011](../../arkts-error-codes/document.md#section12860126792)

 | 

The user's face does not match the facial image used as proof of identity.

 |
| 

REAL\_NAME\_NOT\_EXIST

 | 

[1002500012](../../arkts-error-codes/document.md#section1235141017912)

 | 

The real-name information about the HUAWEI ID is not found.

 |
| 

NAME\_AND\_ID\_NUMBER\_NOT\_MATCH

 | 

[1002500013](../../arkts-error-codes/document.md#section1792982614911)

 | 

The name does not match the ID card number.

 |
| 

TOO\_MANY\_ATTEMPTS

 | 

[1002500014](../../arkts-error-codes/document.md#section13455833098)

 | 

Too many real-name information verification attempts. Try again 24 hours later.

 |
| 

VERIFICATION\_TOKEN\_INCORRECT

 | 

[1002500015](../../arkts-error-codes/document.md#section1377413361998)

 | 

The **verificationToken** parameter is invalid.

 |
| 

DEVICE\_NOT\_SUPPORTED

 | 

[1002500016](../../arkts-error-codes/document.md#section1239413431916)

 | 

The device does not support this API.

 |

#### startFacialRecognitionVerification

startFacialRecognitionVerification(context: common.Context, request: FacialRecognitionVerificationRequest): Promise<FacialRecognitionVerificationResult>

Executes face-based identity verification for a HUAWEI ID by showing the verification screen. This API returns the result asynchronously through a promise.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/K0haU69iRcGQqqW6BtjUOg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062500Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9C5FE8668E047D7BC60CFC4291A691FF76D752ECD8DA08B1F6FD7C35CDCE787E)

This API is currently not available for child accounts.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.RealNameVerify

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

context

 | 

[common.Context](../../../../application-framework/ability-kit/arkts-apis/stage-model/ohos-app-ability-common-ability-common-module/document.md#context)

 | 

Yes

 | 

Context.

Contexts supported by apps: [UIAbilityContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md) and [UIExtensionContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiextensioncontext/document.md). Apps cannot use [UIExtensionContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiextensioncontext/document.md) in non-full-screen components such as semi-modal, pop-up, and sub-window components.

Contexts supported by atomic services: [UIAbilityContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md)

 |
| 

request

 | 

[FacialRecognitionVerificationRequest](#section10967755141115)

 | 

Yes

 | 

Object for requesting face-based identity verification, which must contain information such as the token.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[FacialRecognitionVerificationResult](#section19699554110)\>

 | 

[FacialRecognitionVerificationResult](#section19699554110) object returned through a promise. If this object is returned, face-based identity verification is successful. You can compare the **state** values in this object and request object to confirm the current request, preventing cross-site attacks.

 |

**Error codes**:

For details about the error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [ArkTS Error Codes](../../arkts-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

[401](../../../../api-reference-overview/universal-error-codes/document.md#section401-parameter-check-failed)

 | 

Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

 |
| 

[801](../../../../api-reference-overview/universal-error-codes/document.md#section801-api-not-supported)

 | 

Capability not supported. Function startFacialRecognitionVerification can not work correctly due to limited device capabilities.

 |
| 

[1002500001](../../arkts-error-codes/document.md#section126501952132317)

 | 

The network is unavailable.

 |
| 

[1002500002](../../arkts-error-codes/document.md#section1651105232319)

 | 

The user has not logged in with HUAWEI ID.

 |
| 

[1002500003](../../arkts-error-codes/document.md#section665175210236)

 | 

Failed to check the fingerprint of the application bundle.

 |
| 

[1002500004](../../arkts-error-codes/document.md#section17651105272310)

 | 

The application does not have the required permissions.

 |
| 

[1002500005](../../arkts-error-codes/document.md#section1995615923313)

 | 

The user canceled the verification of the HUAWEI ID.

 |
| 

[1002500006](../../arkts-error-codes/document.md#section10196176171810)

 | 

Internal error.

 |
| 

[1002500008](../../arkts-error-codes/document.md#section177525511359)

 | 

Real-name verification is not supported for the HUAWEI ID.

 |
| 

[1002500011](../../arkts-error-codes/document.md#section12860126792)

 | 

Your face does not match your facial image as proof of identity.

 |
| 

[1002500012](../../arkts-error-codes/document.md#section1235141017912)

 | 

No real-name information is found for the HUAWEI ID.

 |
| 

[1002500013](../../arkts-error-codes/document.md#section1792982614911)

 | 

Your name and ID number do not match.

 |
| 

[1002500014](../../arkts-error-codes/document.md#section13455833098)

 | 

Too many real-name verification attempts.

 |
| 

[1002500015](../../arkts-error-codes/document.md#section1377413361998)

 | 

The verificationToken parameter is incorrectly set.

 |
| 

[1002500016](../../arkts-error-codes/document.md#section1239413431916)

 | 

This device does not support this API.

 |

**Example**:

import { realName } from '@kit.AccountKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { util } from '@kit.ArkTS';

const request: realName.FacialRecognitionVerificationRequest = {
  verificationToken: "_xxx_", // Call the real-name information verification API of the OpenRealName service to obtain this token.
  state: util.generateRandomUUID() // You are advised to use **generateRandomUUID** to generate a state.
}
hilog.info(0x0000, 'testTag', \`verifyFacialRecognitionWithPromise params ${request}\`);
// The following provides only code snippets. Use it in the custom component instance to obtain the **UIContext** object as the input parameter of the function.
realName.startFacialRecognitionVerification(this.getUIContext().getHostContext(), request).then(data => {
  const verifyResult = data as realName.FacialRecognitionVerificationResult;
  // Process **verifyResult**.
  hilog.info(0x0000, 'testTag', 'Succeeded in verifying facial recognition.');
}).catch((error: BusinessError<Object>) => {
  dealAllError(error);
})

// Handle the error.
function dealAllError(error: BusinessError<Object>): void {
  hilog.error(0x0000, 'testTag', \`Failed to authorize. Code: ${error.code}, message: ${error.message}\`);
}
