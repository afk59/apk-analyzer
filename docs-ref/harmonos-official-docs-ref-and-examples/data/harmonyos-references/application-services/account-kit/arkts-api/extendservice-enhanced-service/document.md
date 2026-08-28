# extendService (Enhanced Service)

This module provides enhanced capabilities of Account Kit, including identity verification and jumping to the account center.

**Start version**: 4.0.0(10)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/bOQAvpaNQ8iavAfev3d3zg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062501Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DC6FF3679AB7F99F519CC1B88D7FF2277B15906AA8349784922523C36976D79F)

This service is available only to system apps currently.

#### Module Import

import { extendService } from '@kit.AccountKit';

#### IdType

Enumeration object of ID types.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.ExtendService

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

#### RiskLevel

Enumeration object of risk levels.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.ExtendService

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

LOW

 | 

1

 | 

Low risk.

 |
| 

HIGH

 | 

2

 | 

High risk.

 |

#### VerifyRequest

Identity verification request object.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.ExtendService

**Start version**: 4.0.0(10)

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

idType

 | 

[IdType](#section816451553012)

 | 

No

 | 

No

 | 

ID type of **idValue**.

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

UnionID or OpenID obtained by a user. The type passed is defined by **idType**. The value contains 1 to 256 characters.

The UnionID and OpenID can be obtained through the [LoginWithHuaweiIDResponse](../authentication-unified-authentication-service/document.md#section15454203811311), [AuthorizationWithHuaweiIDResponse](../authentication-unified-authentication-service/document.md#section10418450161620), [LoginPanel](../../arkts-components/loginpanel-huawei-id-sign-in-panel-component/document.md#section72281234181611), or [LoginWithHuaweiIDButton](../../arkts-components/loginwithhuaweiidbutton-huawei-id-sign-in-button-component/document.md#section1624716107193) API. For details, please refer to the relevant sample code.

 |
| 

sceneId

 | 

string

 | 

No

 | 

No

 | 

Scenario ID for identity verification. This parameter and the **riskLevel** parameter together represent a set of configurations of an app on the Account Kit server, including the number of verification times, first verification mode, and secondary verification mode. The value contains 1 to 10 characters.

 |
| 

riskLevel

 | 

[RiskLevel](#section7913052143518)

 | 

No

 | 

No

 | 

Risk level. This parameter and **sceneId** parameter together represent a set of configurations of an app on the Account Kit server. Generally, secondary verification is required in high-risk scenarios.

 |
| 

nonce

 | 

string

 | 

No

 | 

No

 | 

**nonce** parameter in the request body. The value contains 1 to 64 characters. This parameter is contained in the returned **verifyToken** and can be used to prevent replay attacks through consistency verification.

You are advised to use nonces and perform consistency verification. [util.generateRandomUUID()](../../../../application-framework/arkts/arkts-apis/ohos-util-util/document.md#utilgeneraterandomuuid9) is recommended.

 |

**Example**:

import { extendService } from '@kit.AccountKit';
import { util } from '@kit.ArkTS';

// Create request parameters.
const request: extendService.VerifyRequest = {
  idType: extendService.IdType.UNION\_ID,
  idValue: '_xxx_', // The value can be obtained through the HUAWEI ID sign-in API.
  sceneId: '_xxx_', // ID of a scene that triggers identity verification.
  riskLevel: extendService.RiskLevel.LOW,
  nonce: util.generateRandomUUID() // You are advised to use **generateRandomUUID** to generate a nonce.
  }

#### VerifyResult

Identity verification request result object.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.ExtendService

**Start version**: 4.0.0(10)

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

verifyToken

 | 

string

 | 

Yes

 | 

No

 | 

Token returned for identity verification, which is in JWT format.

 |

**Example**:

import { extendService } from '@kit.AccountKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { util } from '@kit.ArkTS';
import { BusinessError } from '@kit.BasicServicesKit';

// Create request parameters.
const request: extendService.VerifyRequest = {
  idType: extendService.IdType.UNION\_ID,
  idValue: '_xxx_', // The value can be obtained through the HUAWEI ID sign-in or authorization API.
  sceneId: '_xxx_', // ID of a scene that triggers identity verification.
  riskLevel: extendService.RiskLevel.LOW,
  nonce: util.generateRandomUUID() // You are advised to use **generateRandomUUID** to generate a nonce.
}

// Execute the identity verification request and process the result.
try {
  // The following provides only code snippets. Use it in the custom component instance to obtain the **UIContext** object as the input parameter of the function.
  extendService.verifyAccount(this.getUIContext().getHostContext(), request, (error: BusinessError, data) => {
    if (error) {
      dealAllError(error);
      return;
    }
    const verifyResult = data as extendService.VerifyResult;
    hilog.info(0x0000, 'testTag', 'Succeeded in verifying.');
    const verifyToken = verifyResult.verifyToken;
    // Process **verifyToken**.
  });
} catch (error) {
  dealAllError(error);
}

// Handle the error.
function dealAllError(error: BusinessError): void {
  hilog.error(0x0000, 'testTag', \`Failed to verify. Code: ${error.code}, message: ${error.message}\`);
}

#### ExtendErrorCode

Enumeration that defines error codes of the Account Kit extension module.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.ExtendService

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

INVALID\_PARAMETER

 | 

[401](../../../../api-reference-overview/universal-error-codes/document.md#section401-parameter-check-failed)

 | 

Parameter check failed.

 |
| 

NETWORK\_ERROR

 | 

[1001600001](../../arkts-error-codes/document.md#section1211715201154)

 | 

The network is unavailable.

 |
| 

ACCOUNT\_NOT\_LOGGED\_IN

 | 

[1001600002](../../arkts-error-codes/document.md#section174914372610)

 | 

The user has not signed in with their HUAWEI ID.

 |
| 

PACKAGE\_FINGERPRINT\_CHECK\_ERROR

 | 

[1001600003](../../arkts-error-codes/document.md#section176803402816)

 | 

The certificate fingerprint of the app fails to be verified.

 |
| 

PERMISSION\_CHECK\_ERROR

 | 

[1001600004](../../arkts-error-codes/document.md#section1924781781013)

 | 

The app does not have the required permissions.

 |
| 

USER\_CANCELED

 | 

[1001600005](../../arkts-error-codes/document.md#section051982312124)

 | 

The user canceled the current operation.

 |
| 

VERIFICATION\_FACTOR\_UNAVAILABLE

 | 

[1001600006](../../arkts-error-codes/document.md#section1140794171313)

 | 

The verification factor is not supported on the device.

 |
| 

INTERNAL\_ERROR

 | 

[1001600007](../../arkts-error-codes/document.md#section7982145091511)

 | 

Internal error.

 |

#### verifyAccount

verifyAccount(context: common.Context, request: VerifyRequest, callback: AsyncCallback<VerifyResult>): void

Executes an Account Kit-based identity verification request. This API returns the result asynchronously through a callback.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.ExtendService

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

Yes

 | 

Context.

Contexts supported by apps: [UIAbilityContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md) and [UIExtensionContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiextensioncontext/document.md). Apps cannot use [UIExtensionContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiextensioncontext/document.md) in non-full-screen components such as semi-modal, pop-up, and sub-window components.

Contexts supported by atomic services: [UIAbilityContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md)

NOTE:

-   In version 4.0.0(10), the parameter type is [UIAbilityContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md).
-   In 4.1.0(11) and later versions, the parameter type is [Context](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md).

 |
| 

request

 | 

[VerifyRequest](#section9615740103819)

 | 

Yes

 | 

Identity verification request object, containing request parameters.

 |
| 

callback

 | 

AsyncCallback<[VerifyResult](#section155352089012)\>

 | 

Yes

 | 

Callback function.

If the identity verification is successful, **err** is **undefined** and **data** is the obtained [VerifyResult](#section155352089012) object. Otherwise, an error object will be returned.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS Error Codes](../../arkts-error-codes/document.md).

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

[1001600001](../../arkts-error-codes/document.md#section1211715201154)

 | 

The network is unavailable.

 |
| 

[1001600002](../../arkts-error-codes/document.md#section174914372610)

 | 

The user has not logged in with HUAWEI ID.

 |
| 

[1001600003](../../arkts-error-codes/document.md#section176803402816)

 | 

Failed to check the fingerprint of the application bundle.

 |
| 

[1001600004](../../arkts-error-codes/document.md#section1924781781013)

 | 

The application does not have the required permissions.

 |
| 

[1001600005](../../arkts-error-codes/document.md#section051982312124)

 | 

The user canceled the current operation.

 |
| 

[1001600006](../../arkts-error-codes/document.md#section1140794171313)

 | 

The requested verification factors are unavailable on the device.

 |
| 

[1001600007](../../arkts-error-codes/document.md#section7982145091511)

 | 

Internal error.

 |

**Example**:

import { extendService } from '@kit.AccountKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { util } from '@kit.ArkTS';
import { BusinessError } from '@kit.BasicServicesKit';

// Create request parameters.
const request: extendService.VerifyRequest = {
  idType: extendService.IdType.UNION\_ID,
  idValue: '_xxx_', // The value can be obtained through the HUAWEI ID sign-in API.
  sceneId: '_xxx_', // ID of a scene that triggers identity verification, which can be applied for through configuration.
  riskLevel: extendService.RiskLevel.LOW,
  nonce: util.generateRandomUUID() // You are advised to use **generateRandomUUID** to generate a nonce.
}

// Execute the identity verification request and process the result.
try {
  // The following provides only code snippets. Use it in the custom component instance to obtain the **UIContext** object as the input parameter of the function.
  extendService.verifyAccount(this.getUIContext().getHostContext(), request, (error, data) => {
    if (error) {
      dealAllError(error);
      return;
    }
    const verifyResult = data as extendService.VerifyResult;
    hilog.info(0x0000, 'testTag', 'Succeeded in verifying.');
    const verifyToken = verifyResult.verifyToken;
    // Process **verifyToken**.
  });
} catch (error) {
  dealAllError(error);
}

// Handle the error.
function dealAllError(error: BusinessError): void {
  hilog.error(0x0000, 'testTag', \`Failed to verify. Code: ${error.code}, message: ${error.message}\`);
}

#### verifyAccount

verifyAccount(context: common.Context, request: VerifyRequest): Promise<VerifyResult>

Executes an Account Kit-based identity verification request. This API returns the result asynchronously through a promise.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.ExtendService

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

Yes

 | 

Context.

Contexts supported by apps: [UIAbilityContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md) and [UIExtensionContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiextensioncontext/document.md). Apps cannot use [UIExtensionContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiextensioncontext/document.md) in non-full-screen components such as semi-modal, pop-up, and sub-window components.

Contexts supported by atomic services: [UIAbilityContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md)

NOTE:

-   In version 4.0.0(10), the parameter type is [UIAbilityContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md).
-   In 4.1.0(11) and later versions, the parameter type is [Context](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md).

 |
| 

request

 | 

[VerifyRequest](#section9615740103819)

 | 

Yes

 | 

Identity verification request object, containing request parameters.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[VerifyResult](#section155352089012)\>

 | 

[VerifyResult](#section155352089012) object returned through a promise.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS Error Codes](../../arkts-error-codes/document.md).

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

[1001600001](../../arkts-error-codes/document.md#section1211715201154)

 | 

The network is unavailable.

 |
| 

[1001600002](../../arkts-error-codes/document.md#section174914372610)

 | 

The user has not logged in with HUAWEI ID.

 |
| 

[1001600003](../../arkts-error-codes/document.md#section176803402816)

 | 

Failed to check the fingerprint of the application bundle.

 |
| 

[1001600004](../../arkts-error-codes/document.md#section1924781781013)

 | 

The application does not have the required permissions.

 |
| 

[1001600005](../../arkts-error-codes/document.md#section051982312124)

 | 

The user canceled the current operation.

 |
| 

[1001600006](../../arkts-error-codes/document.md#section1140794171313)

 | 

The requested verification factors are unavailable on the device.

 |
| 

[1001600007](../../arkts-error-codes/document.md#section7982145091511)

 | 

Internal error.

 |

**Example**:

import { extendService } from '@kit.AccountKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { util } from '@kit.ArkTS';
import { BusinessError } from '@kit.BasicServicesKit';

// Create request parameters.
const request: extendService.VerifyRequest = {
  idType: extendService.IdType.UNION\_ID,
  idValue: '_xxx_', // The value can be obtained through the HUAWEI ID sign-in API.
  sceneId: '_xxx_', // ID of a scene that triggers identity verification, which can be applied for through configuration.
  riskLevel: extendService.RiskLevel.LOW,
  nonce: util.generateRandomUUID() // You are advised to use **generateRandomUUID** to generate a nonce.
}

// The following provides only code snippets. Use it in the custom component instance to obtain the **UIContext** object as the input parameter of the function.
// Execute the identity verification request and process the result.
extendService.verifyAccount(this.getUIContext().getHostContext(), request).then(data => {
  const verifyResult = data as extendService.VerifyResult;
  hilog.info(0x0000, 'testTag', 'Succeeded in verifying.');
  const verifyToken = verifyResult.verifyToken;
  // Process **verifyToken**.
}).catch((error: BusinessError) => {
  dealAllError(error);
})

// Handle the error.
function dealAllError(error: BusinessError): void {
  hilog.error(0x0000, 'testTag', \`Failed to verify. Code: ${error.code}, message: ${error.message}\`);
}

#### startAccountCenter

startAccountCenter(context: common.Context, callback: AsyncCallback<void>): void

Shows the account center screen to view the basic information of the signed-in HUAWEI ID. The result will be returned asynchronously through a callback.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.ExtendService

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

Yes

 | 

Context.

Contexts supported: [UIAbilityContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md) and [UIExtensionContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiextensioncontext/document.md). Apps cannot use [UIExtensionContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiextensioncontext/document.md) in non-full-screen components such as semi-modal, pop-up, and sub-window components.

NOTE:

-   In version 4.0.0(10), the parameter type is [UIAbilityContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md).
-   In 4.1.0(11) and later versions, the parameter type is [Context](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md).

 |
| 

callback

 | 

AsyncCallback<void>

 | 

Yes

 | 

Callback function.

If the request for showing the account center screen is successfully executed, **err** is **undefined**. Otherwise, an error object will be returned.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS Error Codes](../../arkts-error-codes/document.md).

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

[1001600001](../../arkts-error-codes/document.md#section1211715201154)

 | 

The network is unavailable.

 |
| 

[1001600002](../../arkts-error-codes/document.md#section174914372610)

 | 

The user has not logged in with HUAWEI ID.

 |
| 

[1001600003](../../arkts-error-codes/document.md#section176803402816)

 | 

Failed to check the fingerprint of the application bundle.

 |
| 

[1001600004](../../arkts-error-codes/document.md#section1924781781013)

 | 

The application does not have the required permissions.

 |
| 

[1001600007](../../arkts-error-codes/document.md#section7982145091511)

 | 

Internal error.

 |

**Example**:

import { extendService } from '@kit.AccountKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Execute the request for opening the account center and process the result.
try {
  // The following provides only code snippets. Use it in the custom component instance to obtain the **UIContext** object as the input parameter of the function.
  extendService.startAccountCenter(this.getUIContext().getHostContext(), (error: BusinessError) => {
    if (error) {
      dealAllError(error);
      return;
    }
    hilog.info(0x0000, 'testTag', 'Succeeded in starting account center');
  });
} catch (error) {
  dealAllError(error);
}

// Handle the error.
function dealAllError(error: BusinessError): void {
  hilog.error(0x0000, 'testTag', \`Failed to startAccountCenter. Code: ${error.code}, message: ${error.message}\`);
}

#### startAccountCenter

startAccountCenter(context: common.Context): Promise<void>

Shows the account center screen to view the basic information of the signed-in HUAWEI ID. The result will be returned asynchronously through a promise.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.ExtendService

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

Yes

 | 

Context.

Contexts supported: [UIAbilityContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md) and [UIExtensionContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiextensioncontext/document.md). Apps cannot use [UIExtensionContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiextensioncontext/document.md) in non-full-screen components such as semi-modal, pop-up, and sub-window components.

NOTE:

-   In version 4.0.0(10), the parameter type is [UIAbilityContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md).
-   In 4.1.0(11) and later versions, the parameter type is [Context](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md).

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

For details about the error codes, please refer to [ArkTS Error Codes](../../arkts-error-codes/document.md).

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

[1001600001](../../arkts-error-codes/document.md#section1211715201154)

 | 

The network is unavailable.

 |
| 

[1001600002](../../arkts-error-codes/document.md#section174914372610)

 | 

The user has not logged in with HUAWEI ID.

 |
| 

[1001600003](../../arkts-error-codes/document.md#section176803402816)

 | 

Failed to check the fingerprint of the application bundle.

 |
| 

[1001600004](../../arkts-error-codes/document.md#section1924781781013)

 | 

The application does not have the required permissions.

 |
| 

[1001600007](../../arkts-error-codes/document.md#section7982145091511)

 | 

Internal error.

 |

**Example**:

import { extendService } from '@kit.AccountKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

// The following provides only code snippets. Use it in the custom component instance to obtain the **UIContext** object as the input parameter of the function.
// Execute the request for opening the account center and process the result.
extendService.startAccountCenter(this.getUIContext().getHostContext()).then(() => {
  hilog.info(0x0000, 'testTag', 'Succeeded in starting account center');
}).catch((error: BusinessError<Object>) => {
  dealAllError(error);
})

// Handle the error.
function dealAllError(error: BusinessError<Object>): void {
  hilog.error(0x0000, 'testTag', \`Failed to startAccountCenter. Code: ${error.code}, message: ${error.message}\`);
}
