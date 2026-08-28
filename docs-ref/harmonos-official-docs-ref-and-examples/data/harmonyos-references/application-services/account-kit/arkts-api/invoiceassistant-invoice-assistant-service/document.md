# invoiceAssistant (Invoice Assistant Service)

This module provides the invoice assistant capability of Account Kit.

**Start version**: 5.0.0(12)

#### Module Import

import { invoiceAssistant } from '@kit.AccountKit';

#### InvoiceAssistantErrorCode

Enumeration that defines error codes of APIs related to the invoice assistant service of Account Kit.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.HuaweiID.InvoiceAssistant

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

USER\_CANCELED

 | 

[1010060001](../../arkts-error-codes/document.md#section165992015527)

 | 

The user cancels the invoice assistant service.

 |
| 

SYSTEM\_ERROR

 | 

[1010060002](../../arkts-error-codes/document.md#section730115513413)

 | 

Internal system error.

 |
| 

APP\_NOT\_AUTHORIZED

 | 

[1010060003](../../arkts-error-codes/document.md#section717135217914)

 | 

The certificate fingerprint of the app fails to be verified.

 |
| 

FREQUENT\_CALLS

 | 

[1010060004](../../arkts-error-codes/document.md#section12371175713102)

 | 

API calls are too frequent.

 |
| 

NETWORK\_ERROR

 | 

[1010060005](../../arkts-error-codes/document.md#section17507143210121)

 | 

Network connection error.

 |
| 

ACCOUNT\_NOT\_LOGGED\_IN

 | 

[1010060006](../../arkts-error-codes/document.md#section569215704317)

 | 

The user has not signed in with their HUAWEI ID.

 |
| 

INVOICE\_TITLE\_EXISTS

 | 

[1010060007](../../arkts-error-codes/document.md#section670931214512)

 | 

The invoice title already exists.

 |
| 

UNSUPPORTED

 | 

[1010060008](../../arkts-error-codes/document.md#section16845834174215)

 | 

The invoice assistant service is unavailable for the HUAWEI ID signed in.

 |

#### InvoiceTitle

Invoice title data object returned by the invoice assistant service.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.HuaweiID.InvoiceAssistant

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

type

 | 

string

 | 

No

 | 

No

 | 

Title type. The options are **0** (individual) and **1** (enterprise).

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

Title name.

 |
| 

taxNumber

 | 

string

 | 

No

 | 

No

 | 

Taxpayer identification number. For a title of the enterprise type, the actual value is returned. For a title of the individual type, an empty string is returned.

 |
| 

companyAddress

 | 

string

 | 

No

 | 

No

 | 

Address of a company. For a title of the enterprise type, the actual value is returned. For a title of the individual type, an empty string is returned.

 |
| 

telephone

 | 

string

 | 

No

 | 

No

 | 

Phone number of a company. For a title of the enterprise type, the actual value is returned. For a title of the individual type, an empty string is returned.

 |
| 

bankName

 | 

string

 | 

No

 | 

No

 | 

Bank name of a company. For a title of the enterprise type, the actual value is returned. For a title of the individual type, an empty string is returned.

 |
| 

bankAccount

 | 

string

 | 

No

 | 

No

 | 

Bank account of a company. For a title of the enterprise type, the actual value is returned. For a title of the individual type, an empty string is returned.

 |

#### selectInvoiceTitle

selectInvoiceTitle(context: common.Context): Promise<InvoiceTitle>

Shows the invoice title selection screen and returns the invoice title selected by a user. This API returns the result asynchronously through a promise.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.HuaweiID.InvoiceAssistant

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

Promise<[InvoiceTitle](#section9615740103819)\>

 | 

[InvoiceTitle](#section9615740103819) object returned through a promise.

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

[1010060001](../../arkts-error-codes/document.md#section165992015527)

 | 

The operation was canceled by the user.

 |
| 

[1010060002](../../arkts-error-codes/document.md#section730115513413)

 | 

System internal error.

 |
| 

[1010060003](../../arkts-error-codes/document.md#section717135217914)

 | 

Failed to check the fingerprint of the app bundle.

 |
| 

[1010060004](../../arkts-error-codes/document.md#section12371175713102)

 | 

Too frequent API calls.

 |
| 

[1010060005](../../arkts-error-codes/document.md#section17507143210121)

 | 

Network connection error.

 |
| 

[1010060006](../../arkts-error-codes/document.md#section569215704317)

 | 

The HUAWEI ID is not signed in.

 |
| 

[1010060007](../../arkts-error-codes/document.md#section670931214512)

 | 

Failed to create an invoice title because the title already exists.

 |
| 

[1010060008](../../arkts-error-codes/document.md#section16845834174215)

 | 

The invoice service does not support the logged HUAWEI ID.

 |

**Example**:

import { invoiceAssistant } from '@kit.AccountKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Execute the request.
if (canIUse('SystemCapability.HuaweiID.InvoiceAssistant')) {
  try {
    // The following provides only code snippets. Use it in the custom component instance to obtain the **UIContext** object as the input parameter of the function.
    invoiceAssistant.selectInvoiceTitle(this.getUIContext().getHostContext())
      .then((data: invoiceAssistant.InvoiceTitle) => {
        hilog.info(0x0000, 'testTag', 'Succeeded in selecting invoice title');
        const type: string = data.type;
        const title: string = data.title;
        const taxNumber: string = data.taxNumber;
        const companyAddress: string = data.companyAddress;
        const telephone: string = data.telephone;
        const bankName: string = data.bankName;
        const bankAccount: string = data.bankAccount;

      // Process **type**, **title**, **taxNumber**, **companyAddress**, **telephone**, **bankName**, and **bankAccount**.
        // ...

      })
      .catch((error: BusinessError<Object>) => {
        dealAllError(error);
      })
  } catch (error) {
    dealAllError(error);
  }
} else {
  hilog.info(0x0000, 'testTag',
    'The current device does not support the invoking of the selectInvoiceTitle interface.');
}

// Handle the error.
function dealAllError(error: BusinessError<Object>): void {
  hilog.error(0x0000, 'testTag', \`Failed to authorize. Code: ${error.code}, message: ${error.message}\`);
}
