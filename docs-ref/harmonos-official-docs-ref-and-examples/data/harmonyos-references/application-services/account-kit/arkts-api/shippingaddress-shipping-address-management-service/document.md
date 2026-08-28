# shippingAddress (Shipping Address Management Service)

This module provides the shipping address management capability of Account Kit. Your app can use this capability to obtain the shipping address information of a HUAWEI ID, including the detailed address and mobile number.

**Start version**: 5.0.0(12)

#### Module Import

import { shippingAddress } from '@kit.AccountKit';

#### ShippingAddressErrorCode

Enumeration that defines error codes of the Account Kit shipping address management service.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.ShippingAddress

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

INTERNAL\_ERROR

 | 

[1008100001](../../arkts-error-codes/document.md#section2160112171514)

 | 

Internal error.

 |
| 

NETWORK\_ERROR

 | 

[1008100002](../../arkts-error-codes/document.md#section315852115157)

 | 

The network is unavailable.

 |
| 

ACCOUNT\_NOT\_LOGGED\_IN

 | 

[1008100003](../../arkts-error-codes/document.md#section15158192191517)

 | 

The user has not signed in with their HUAWEI ID.

 |
| 

PACKAGE\_FINGERPRINT\_CHECK\_ERROR

 | 

[1008100004](../../arkts-error-codes/document.md#section1415952110158)

 | 

The certificate fingerprint of the app fails to be verified.

 |
| 

PERMISSION\_CHECK\_ERROR

 | 

[1008100005](../../arkts-error-codes/document.md#section515972151510)

 | 

The app does not have the required permissions.

 |
| 

USER\_CANCELED

 | 

[1008100006](../../arkts-error-codes/document.md#section191591621191512)

 | 

A user exits the shipping address management service without completing the current operation.

 |
| 

UNSUPPORTED

 | 

[1008100007](../../arkts-error-codes/document.md#section91601621141512)

 | 

The shipping address management service is unavailable for the HUAWEI ID signed in.

 |

#### AddressInfo

Shipping address data object returned by the shipping address management service. You can obtain the shipping address information based on the actual scenario.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.ShippingAddress

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

userName

 | 

string

 | 

Yes

 | 

No

 | 

User name. The value contains 2 to 20 characters.

 |
| 

mobileNumber

 | 

string

 | 

Yes

 | 

No

 | 

Mobile number. The value contains 2 to 20 characters.

NOTE:

Currently, only mobile numbers registered in the Chinese mainland are supported. The shipping address supports plaintext mobile numbers in three formats: 183\*\*\*\*\*\*58, +86183\*\*\*\*\*\*58, and 0086183\*\*\*\*\*\*58. The format of the mobile number returned by the API is the same as that entered by the user.

 |
| 

telNumber

 | 

string

 | 

Yes

 | 

Yes

 | 

Fixed-line phone number. The value contains 1 to 256 characters. If this parameter is not set by the user, it will not be returned.

 |
| 

zipCode

 | 

string

 | 

Yes

 | 

Yes

 | 

Postal code. The value contains 1 to 256 characters. If this parameter is not set by the user, it will not be returned.

 |
| 

countryCode

 | 

string

 | 

Yes

 | 

No

 | 

Country/region code. The value contains 1 to 256 characters.

 |
| 

provinceName

 | 

string

 | 

Yes

 | 

No

 | 

Province name. The value contains 1 to 50 characters.

 |
| 

cityName

 | 

string

 | 

Yes

 | 

No

 | 

City name. The value contains 1 to 50 characters.

 |
| 

districtName

 | 

string

 | 

Yes

 | 

No

 | 

District name. The value contains 1 to 50 characters.

NOTE:

Currently, this capability is available only in the Chinese mainland.

 |
| 

streetName

 | 

string

 | 

Yes

 | 

No

 | 

Street name. The value contains 1 to 50 characters.

 |
| 

detailedAddress

 | 

string

 | 

Yes

 | 

No

 | 

Detailed address. The value contains 1 to 50 characters.

 |

#### chooseAddress

chooseAddress(context: common.Context): Promise<AddressInfo>

Opens the shipping address management screen. This API returns the user-selected shipping address asynchronously through a promise. It is used to obtain the shipping address information bound to a HUAWEI ID via Account Kit.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.ShippingAddress

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

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[AddressInfo](#section9615740103819)\>

 | 

[AddressInfo](#section9615740103819) object returned through a promise, which contains the shipping address details.

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

[1008100001](../../arkts-error-codes/document.md#section2160112171514)

 | 

Internal error.

 |
| 

[1008100002](../../arkts-error-codes/document.md#section315852115157)

 | 

The network is unavailable.

 |
| 

[1008100003](../../arkts-error-codes/document.md#section15158192191517)

 | 

The user has not signed in with HUAWEI ID.

 |
| 

[1008100004](../../arkts-error-codes/document.md#section1415952110158)

 | 

Failed to check the fingerprint of the app bundle.

 |
| 

[1008100005](../../arkts-error-codes/document.md#section515972151510)

 | 

The app does not have the required permissions.

 |
| 

[1008100006](../../arkts-error-codes/document.md#section191591621191512)

 | 

The user quits the shipping address management service without finishing.

 |
| 

[1008100007](../../arkts-error-codes/document.md#section91601621141512)

 | 

The shipping address management service does not support the HUAWEI ID that is already signed in.

 |

**Example**:

import { shippingAddress } from '@kit.AccountKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Execute the request.
try {
  // The following provides only code snippets. Use it in the custom component instance to obtain the **UIContext** object as the input parameter of the function.
  shippingAddress.chooseAddress(this.getUIContext().getHostContext()).then((data: shippingAddress.AddressInfo) => {
    hilog.info(0x0000, 'testTag', 'Succeeded in choosing address');
    const userName: string = data.userName;
    const mobileNumber: string = data.mobileNumber;
    const countryCode: string = data.countryCode;
    const provinceName: string = data.provinceName;
    const cityName: string = data.cityName;
    const districtName: string = data.districtName;
    const streetName: string = data.streetName;
    const detailedAddress: string = data.detailedAddress;
    // Process the obtained shipping address information.
  }).catch((error: BusinessError) => {
    dealAllError(error);
  })
} catch (error) {
  dealAllError(error);
}

// Handle the error.
function dealAllError(error: BusinessError): void {
  hilog.error(0x0000, 'testTag', \`Failed to chooseAddress. Code: ${error.code}, message: ${error.message}\`);
}
