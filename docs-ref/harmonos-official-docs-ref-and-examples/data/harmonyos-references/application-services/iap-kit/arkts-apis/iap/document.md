# IAP

This module provides the capabilities for IAP.

**Model restriction**: APIs of this module can be used only in the stage model.

**Start version**: 4.0.0(10)

#### Module Import

import { iap } from '@kit.IAPKit';

#### ProductType

Product type.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Payment.IAP

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

CONSUMABLE

 | 

0

 | 

Consumable.

 |
| 

NONCONSUMABLE

 | 

1

 | 

Non-consumable.

 |
| 

AUTORENEWABLE

 | 

2

 | 

Auto-renewable subscription.

**Start version**: 4.1.0(11)

 |
| 

NONRENEWABLE

 | 

3

 | 

Non-renewable subscription.

**Atomic service API**: This API can be used in atomic services since API version 5.0.2(14).

**Start version**: 5.0.2 (14)

 |

#### PurchaseQueryType

Queries the type of purchase data.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Payment.IAP

**Start version**: 4.1.0(11)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

ALL

 | 

0

 | 

All purchase records, including consumables, non-consumables, auto-renewable subscriptions, and non-renewable subscriptions.

 |
| 

UNFINISHED

 | 

1

 | 

Consumables, non-consumables, auto-renewable subscriptions, and non-renewable subscriptions that have been purchased but not delivered.

 |
| 

CURRENT\_ENTITLEMENT

 | 

2

 | 

Non-consumables that have been purchased and subscriptions that are currently active.

 |

#### PeriodUnit

Billing cycle unit of a subscription.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Payment.IAP

**Start version**: 4.1.0(11)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

DAY

 | 

0

 | 

Day.

 |
| 

WEEK

 | 

1

 | 

Week.

 |
| 

MONTH

 | 

2

 | 

Month.

 |
| 

YEAR

 | 

3

 | 

Year.

 |
| 

MINUTE

 | 

4

 | 

Minute. (Reserved parameter, which is not supported currently.)

 |

#### OfferPaymentMode

Payment method of a promotion.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Payment.IAP

**Start version**: 4.1.0(11)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

FREE\_TRIAL

 | 

1

 | 

Free trial.

 |
| 

PAY\_AS\_YOU\_GO

 | 

2

 | 

Pay-as-you-go.

 |
| 

PAY\_UP\_FRONT

 | 

3

 | 

Prepayment.

 |
| 

SINGLE\_PROMOTION

 | 

5

 | 

One-off special offer (not supported currently), which is applicable only to consumables, non-consumables, and non-renewable subscriptions.

This product type is not supported for wearables or TVs.

**Atomic service API**: This API can be used in atomic services since API version 5.0.5(17).

**Start version**: 5.0.5(17)

 |

#### OfferType

Promotion type.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Payment.IAP

**Start version**: 4.1.0(11)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

INTRODUCTORY

 | 

0

 | 

Introductory offers for new users.

 |
| 

PROMOTIONAL

 | 

1

 | 

Promotional offers for specific user groups.

 |

#### IAPErrorCode

Enumeration of error codes.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Payment.IAP

**Start version**: 4.1.0(11)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

USER\_CANCELED

 | 

1001860000

 | 

The user cancels the current operation.

 |
| 

SYSTEM\_ERROR

 | 

1001860001

 | 

Common error code upon a failure.

 |
| 

APP\_NOT\_AUTHORIZED

 | 

1001860002

 | 

The app is not authorized to call the API.

 |
| 

INVALID\_PRODUCT

 | 

1001860003

 | 

Invalid product information.

 |
| 

FREQUENT\_CALLS

 | 

1001860004

 | 

API calls are too frequent.

 |
| 

NETWORK\_ERROR

 | 

1001860005

 | 

Network connection error.

 |
| 

PRODUCT\_TERRITORY\_NOT\_SUPPORTED

 | 

1001860007

 | 

The app to which the product belongs is not released in a specified location.

 |
| 

ACCOUNT\_NOT\_LOGGED\_IN

 | 

1001860050

 | 

The HUAWEI ID is not signed in.

 |
| 

PRODUCT\_OWNED

 | 

1001860051

 | 

The purchase failed because the user already owns the product.

 |
| 

PURCHASE\_NOT\_PAID

 | 

1001860052

 | 

The delivery failed because the user does not own the product.

 |
| 

PURCHASE\_FINISHED

 | 

1001860053

 | 

The product has been delivered. No more delivery is needed.

 |
| 

ACCOUNT\_TERRITORY\_NOT\_SUPPORTED

 | 

1001860054

 | 

The country or region of the signed-in HUAWEI ID does not support IAP.

 |
| 

USER\_NOT\_ALLOWED

 | 

1001860056

 | 

The transaction is rejected.

 |
| 

APP\_NOT\_DEBUG

 | 

1001860057

 | 

The app does not have a debug signature.

**Start version**: 5.0.0(12)

 |
| 

ACCOUNT\_NOT\_TEST

 | 

1001860058

 | 

The HUAWEI ID is not a test account in the sandbox environment.

**Start version**: 5.0.0(12)

 |
| 

INVALID\_PROMOTIONAL\_OFFER

 | 

1001860059

 | 

Invalid special offer information.

**Start version**: 5.0.0(12)

 |
| 

INVALID\_PURCHASE\_SIGNATURE

 | 

1001860060

 | 

Invalid signature information.

**Start version**: 5.0.0(12)

 |
| 

PURCHASE\_ALREADY\_REFUNDED

 | 

1001860061

 | 

The product has been refunded or is in the process of being refunded.

**Atomic service API**: This API can be used in atomic services since API version 5.0.3(15).

**Start version**: 5.0.3(15)

 |
| 

REFUND\_NOT\_ALLOWED

 | 

1001860062

 | 

Refund is not allowed.

**Atomic service API**: This API can be used in atomic services since API version 5.0.3(15).

**Start version**: 5.0.3(15)

 |

#### WindowScreenMode

UI mode.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Payment.IAP

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

DIALOG\_BOX

 | 

1

 | 

Pop-up.

 |
| 

FULLSCREEN

 | 

2

 | 

Full-screen.

 |

#### ProductStatus

Enumeration of product statuses.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Payment.IAP

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

VALID

 | 

0

 | 

Valid.

 |
| 

CANCELED

 | 

1

 | 

Canceled, that is, deleted. Products in this status cannot be renewed or subscribed to.

 |
| 

OFFLINE

 | 

3

 | 

Offline. Offline subscriptions cannot be purchased by new users, but existing subscribers can still renew their plans.

 |

#### iap.queryEnvironmentStatus

queryEnvironmentStatus(context: common.Context): Promise<void>

Checks whether the currently signed-in HUAWEI ID is located in a country or region where IAP Kit is available. Currently, this API is available only in the Chinese mainland.

The called API returns the result asynchronously through a promise.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Payment.IAP

**Start version**: 4.0.0(10)

**Parameters**:

| 
**Parameter**

 | 

**Type**

 | 

Mandatory

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

context

 | 

common.[Context](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md)

 | 

Yes

 | 

Context. [UIAbilityContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md) is recommended.

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

**Promise** object. **Promise** object without a return value.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
**Error Code**

 | 

**Error Message**

 |
| :-- | :-- |
| 

401

 | 

Parameter error.

 |
| 

1001860000

 | 

The operation was canceled by the user.

 |
| 

1001860001

 | 

System internal error.

 |
| 

1001860002

 | 

The application is not authorized.

 |
| 

1001860004

 | 

Too frequent API calls.

 |
| 

1001860005

 | 

Network connection error.

 |
| 

1001860050

 | 

The HUAWEI ID is not signed in.

 |
| 

1001860054

 | 

The country or region of the signed-in HUAWEI ID does not support IAP.

 |

**Example**:

import { iap } from '@kit.IAPKit';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

iap.queryEnvironmentStatus(this.getUIContext().getHostContext() as common.UIAbilityContext).then(() => {
  // The request succeeded.
  console.info('Succeeded in querying environment status.');
}).catch((err: BusinessError) => {
  // The request failed.
  console.error(\`Failed to query environment status. Code is ${err.code}, message is ${err.message}\`);
});

#### iap.queryEnvironmentStatus

queryEnvironmentStatus(context: common.Context, callback: AsyncCallback<void>): void

Checks whether the currently signed-in HUAWEI ID is located in a country or region where IAP Kit is available. Currently, this API is available only in the Chinese mainland.

This API returns the result asynchronously through a callback.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Payment.IAP

**Start version**: 4.0.0(10)

**Parameters**:

| 
**Parameter**

 | 

**Type**

 | 

Mandatory

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

context

 | 

common.[Context](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md)

 | 

Yes

 | 

Context. [UIAbilityContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md) is recommended.

 |
| 

callback

 | 

AsyncCallback<void>

 | 

Yes

 | 

Callback function. If the signed-in HUAWEI ID is from a country or region supported by IAP Kit, **err** will be **undefined**; otherwise, an error object will be returned.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
**Error Code**

 | 

**Error Message**

 |
| :-- | :-- |
| 

401

 | 

Parameter error.

 |
| 

1001860000

 | 

The operation was canceled by the user.

 |
| 

1001860001

 | 

System internal error.

 |
| 

1001860004

 | 

Too frequent API calls.

 |
| 

1001860005

 | 

Network connection error.

 |
| 

1001860050

 | 

The HUAWEI ID is not signed in.

 |
| 

1001860054

 | 

The country or region of the signed-in HUAWEI ID does not support IAP.

 |

**Example**:

import { iap } from '@kit.IAPKit';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

iap.queryEnvironmentStatus(this.getUIContext().getHostContext() as common.UIAbilityContext, (err: BusinessError) => {
  if (err) {
    // The request failed.
    console.error(\`Failed to query environment status. Code is ${err.code}, message is ${err.message}\`);
    return;
  }
  // The request succeeded.
  console.info('Succeeded in querying environment status.');
});

#### iap.queryProducts

queryProducts(context: common.UIAbilityContext, parameter: QueryProductsParameter): Promise<Array<Product>>

Obtains product details configured in [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html#/). The called API returns the result asynchronously through a promise.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Payment.IAP

**Start version**: 4.0.0(10)

**Parameters**:

| 
**Parameter**

 | 

**Type**

 | 

Mandatory

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

context

 | 

common.[UIAbilityContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md)

 | 

Yes

 | 

[UIAbility](../../../../application-framework/ability-kit/arkts-apis/stage-model/ohos-app-ability-uiability-ability-with-ui/document.md) context.

 |
| 

parameter

 | 

[QueryProductsParameter](#section1033653365917)

 | 

Yes

 | 

[QueryProductsParameter](#section1033653365917) object, which contains request information.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<Array<[Product](#section346874219313)\>>

 | 

**Promise** object, which contains product details.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
**Error Code**

 | 

**Error Message**

 |
| :-- | :-- |
| 

401

 | 

Parameter error.

 |
| 

1001860001

 | 

System internal error.

 |
| 

1001860002

 | 

The application is not authorized.

 |
| 

1001860003

 | 

Invalid product information.

 |
| 

1001860004

 | 

Too frequent API calls.

 |
| 

1001860005

 | 

Network connection error.

 |
| 

1001860007

 | 

The app to which the product belongs is not released in a specified location.

 |
| 

1001860050

 | 

The HUAWEI ID is not signed in.

 |
| 

1001860054

 | 

The country or region of the signed-in HUAWEI ID does not support IAP.

 |

**Example**:

import { iap } from '@kit.IAPKit';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

const parameter: iap.QueryProductsParameter = {
  // iap.ProductType.CONSUMABLE: consumable
  // iap.ProductType.NONCONSUMABLE: non-consumable
  // iap.ProductType.AUTORENEWABLE: auto-renewable subscription
  // iap.ProductType.NONRENEWABLE: non-renewable subscription
  productType: iap.ProductType.CONSUMABLE,
    // Use IDs of the products you configured in AppGallery Connect as the values of **productIds**.
  productIds: \['testConsumeProduct01', 'testConsumeProduct02'\]
}
iap.queryProducts(this.getUIContext().getHostContext() as common.UIAbilityContext, parameter).then((data: Array<iap.Product>) => {
  // The request succeeded.
  console.info(\`Succeeded in querying products. data length: ${data?.length}\`);
}).catch((err: BusinessError) => {
  // The request failed.
  console.error(\`Failed to query products. Code is ${err.code}, message is ${err.message}\`);
});

#### iap.queryProducts

queryProducts(context: common.UIAbilityContext, parameter: QueryProductsParameter, callback: AsyncCallback<Array<Product>>): void

Obtains product details configured in [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html#/). This API returns the result asynchronously through a callback.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Payment.IAP

**Start version**: 4.0.0(10)

**Parameters**:

| 
**Parameter**

 | 

**Type**

 | 

Mandatory

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

context

 | 

common.[UIAbilityContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md)

 | 

Yes

 | 

[UIAbility](../../../../application-framework/ability-kit/arkts-apis/stage-model/ohos-app-ability-uiability-ability-with-ui/document.md) context.

 |
| 

parameter

 | 

[QueryProductsParameter](#section1033653365917)

 | 

Yes

 | 

[QueryProductsParameter](#section1033653365917) object, which contains request information.

 |
| 

callback

 | 

AsyncCallback<Array<[Product](#section346874219313)\>>

 | 

Yes

 | 

Callback function. If the query is successful, **err** is **undefined** and **data** is the obtained Array<[Product](#section346874219313)\>; otherwise, an error object will be returned.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
**Error Code**

 | 

**Error Message**

 |
| :-- | :-- |
| 

401

 | 

Parameter error.

 |
| 

1001860001

 | 

System internal error.

 |
| 

1001860002

 | 

The application is not authorized.

 |
| 

1001860003

 | 

Invalid product information.

 |
| 

1001860004

 | 

Too frequent API calls.

 |
| 

1001860005

 | 

Network connection error.

 |
| 

1001860007

 | 

The app to which the product belongs is not released in a specified location.

 |
| 

1001860050

 | 

The HUAWEI ID is not signed in.

 |
| 

1001860054

 | 

The country or region of the signed-in HUAWEI ID does not support IAP.

 |

**Example**:

import { iap } from '@kit.IAPKit';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

const parameter: iap.QueryProductsParameter = {
  // iap.ProductType.CONSUMABLE: consumable
  // iap.ProductType.NONCONSUMABLE: non-consumable
  // iap.ProductType.AUTORENEWABLE: auto-renewable subscription
  // iap.ProductType.NONRENEWABLE: non-renewable subscription
  productType: iap.ProductType.CONSUMABLE,
    // Use IDs of the products you configured in AppGallery Connect as the values of **productIds**.
  productIds: \['testConsumeProduct01', 'testConsumeProduct02'\]
}
iap.queryProducts(this.getUIContext().getHostContext() as common.UIAbilityContext, parameter, (err: BusinessError, data: Array<iap.Product>) => {
  if (err) {
    // The request failed.
    console.error(\`Failed to query products. Code is ${err.code}, message is ${err.message}\`);
    return;
  }
  // The request succeeded.
  console.info(\`Succeeded in querying products. data length: ${data?.length}\`);
});

#### iap.queryProducts

queryProducts(context: common.UIAbilityContext, productIds: string\[\]): Promise<Array<Product>>

Obtains product details configured in [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html#/). The called API returns the result asynchronously through a promise.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 6.0.0(20).

**System capability**: SystemCapability.Payment.IAP

**Start version**: 6.0.0(20)

**Parameters**:

| 
**Parameter**

 | 

**Type**

 | 

Mandatory

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

context

 | 

common.[UIAbilityContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md)

 | 

Yes

 | 

[UIAbility](../../../../application-framework/ability-kit/arkts-apis/stage-model/ohos-app-ability-uiability-ability-with-ui/document.md) context.

 |
| 

productIds

 | 

string\[\]

 | 

Yes

 | 

ID list of products to be queried. Each product ID must exist and be unique in your app.

Product IDs are specified when you configure products in [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html#/). For details, please refer to [Configuring Products](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/iap-config-product).

NOTE:

A maximum of 200 product IDs can be queried at a time. For a large number of products, it is advised to query their IDs in batches.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<Array<[Product](#section346874219313)\>>

 | 

**Promise** object, which contains product details.

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

1001860001

 | 

System internal error.

 |
| 

1001860002

 | 

The application is not authorized.

 |
| 

1001860003

 | 

Invalid product information.

 |
| 

1001860004

 | 

Too frequent API calls.

 |
| 

1001860005

 | 

Network connection error.

 |
| 

1001860007

 | 

The app to which the product belongs is not released in a specified location.

 |
| 

1001860050

 | 

The HUAWEI ID is not signed in.

 |
| 

1001860054

 | 

The country or region of the signed-in HUAWEI ID does not support IAP.

 |

**Example**:

import { iap } from '@kit.IAPKit';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Use IDs of the products you configured in AppGallery Connect as the values of **productIds**.
const productIds: string\[\] = \['testConsumeProduct01', 'testConsumeProduct02'\];
iap.queryProducts(this.getUIContext().getHostContext() as common.UIAbilityContext, productIds).then((data: Array<iap.Product>) => {
  // The request succeeded.
 console.info(\`Succeeded in querying products. data length: ${data?.length}\`);
}).catch((err: BusinessError) => {
  // The request failed.
  console.error(\`Failed to query products. Code is ${err.code}, message is ${err.message}\`);
})

#### iap.purchase(deprecated)

purchase(context: common.UIAbilityContext, parameter: PurchaseParameter): Promise<PurchaseResult>

Creates an order. Both consumables and non-consumables are supported. After a user initiates a purchase for a product already configured in [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html#/), this API brings up the checkout screen of IAP Kit to show the product name, price, and payment methods.

The called API returns the result asynchronously through a promise.

**Deprecation description**: This API is deprecated since API version 4.1.0(11). You are advised to use [createPurchase](#section18798154545516) instead.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Payment.IAP

**Device behavior differences**: This API is supported on phones, PCs/2-in-1 devices, and tablets. On other devices, it returns error code 1001860001.

**Start version**: 4.0.0(10)

**Parameters**:

| 
**Parameter**

 | 

**Type**

 | 

Mandatory

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

context

 | 

common.[UIAbilityContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md)

 | 

Yes

 | 

[UIAbility](../../../../application-framework/ability-kit/arkts-apis/stage-model/ohos-app-ability-uiability-ability-with-ui/document.md) context.

 |
| 

parameter

 | 

[PurchaseParameter](#section1340120344598)

 | 

Yes

 | 

[PurchaseParameter](#section1340120344598) object, which contains request information.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[PurchaseResult](#section111613541391)\>

 | 

**Promise** object, which contains the purchase result.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
**Error Code**

 | 

**Error Message**

 |
| :-- | :-- |
| 

401

 | 

Parameter error.

 |
| 

1001860000

 | 

The operation was canceled by the user.

 |
| 

1001860001

 | 

System internal error.

 |
| 

1001860002

 | 

The application is not authorized.

 |
| 

1001860003

 | 

Invalid product information.

 |
| 

1001860004

 | 

Too frequent API calls.

 |
| 

1001860005

 | 

Network connection error.

 |
| 

1001860007

 | 

The app to which the product belongs is not released in a specified location.

 |
| 

1001860051

 | 

Failed to purchase a product because the user already owns the product.

 |
| 

1001860054

 | 

The country or region of the signed-in HUAWEI ID does not support IAP.

 |
| 

1001860056

 | 

The user is not allowed to make purchase.

 |

**Example**:

import { iap } from '@kit.IAPKit';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

const parameter: iap.PurchaseParameter = {
  // iap.ProductType.CONSUMABLE: consumable
  // iap.ProductType.NONCONSUMABLE: non-consumable
  productType: iap.ProductType.CONSUMABLE,
  // Use the product ID set by you when configuring product information in AppGallery Connect as the value of **productId**.
  productId: 'testConsumeProduct01',
  developerPayload: 'test developer payload string.'
}
iap.purchase(this.getUIContext().getHostContext() as common.UIAbilityContext, parameter).then((data: iap.PurchaseResult) => {
  // The request succeeded.
  console.info('Succeeded in purchasing.');
}).catch((err: BusinessError) => {
  // The request failed.
  console.error(\`Failed to purchase. Code is ${err.code}, message is ${err.message}\`);
});

#### iap.purchase(deprecated)

purchase(context: common.UIAbilityContext, parameter: PurchaseParameter, callback: AsyncCallback<PurchaseResult>): void

Creates an order. Both consumables and non-consumables are supported. After a user initiates a purchase for a product already configured in [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html#/), this API brings up the checkout screen of IAP Kit to show the product name, price, and payment methods.

This API returns the result asynchronously through a callback.

**Deprecation description**: This API is deprecated since API version 4.1.0(11). You are advised to use [createPurchase](#section19694203910585) instead.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Payment.IAP

**Device behavior differences**: This API is supported on phones, PCs/2-in-1 devices, and tablets. On other devices, it returns error code 1001860001.

**Start version**: 4.0.0(10)

**Parameters**:

| 
**Parameter**

 | 

**Type**

 | 

Mandatory

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

context

 | 

common.[UIAbilityContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md)

 | 

Yes

 | 

[UIAbility](../../../../application-framework/ability-kit/arkts-apis/stage-model/ohos-app-ability-uiability-ability-with-ui/document.md) context.

 |
| 

parameter

 | 

[PurchaseParameter](#section1340120344598)

 | 

Yes

 | 

[PurchaseParameter](#section1340120344598) object, which contains request information.

 |
| 

callback

 | 

AsyncCallback<[PurchaseResult](#section111613541391)\>

 | 

Yes

 | 

Callback function. If the purchase is successful, **err** is **undefined** and **data** is the obtained [PurchaseResult](#section111613541391) object; otherwise, an error object will be returned.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
**Error Code**

 | 

**Error Message**

 |
| :-- | :-- |
| 

401

 | 

Parameter error.

 |
| 

1001860000

 | 

The operation was canceled by the user.

 |
| 

1001860001

 | 

System internal error.

 |
| 

1001860002

 | 

The application is not authorized.

 |
| 

1001860003

 | 

Invalid product information.

 |
| 

1001860004

 | 

Too frequent API calls.

 |
| 

1001860005

 | 

Network connection error.

 |
| 

1001860007

 | 

The app to which the product belongs is not released in a specified location.

 |
| 

1001860051

 | 

Failed to purchase a product because the user already owns the product.

 |
| 

1001860054

 | 

The country or region of the signed-in HUAWEI ID does not support IAP.

 |
| 

1001860056

 | 

The user is not allowed to make purchase.

 |

**Example**:

import { iap } from '@kit.IAPKit';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

const parameter: iap.PurchaseParameter = {
  // iap.ProductType.CONSUMABLE: consumable
  // iap.ProductType.NONCONSUMABLE: non-consumable
  productType: iap.ProductType.CONSUMABLE,
  // Use the product ID set by you when configuring product information in AppGallery Connect as the value of **productId**.
  productId: 'testConsumeProduct01',
  developerPayload: 'test developer payload string.'
}
iap.purchase(this.getUIContext().getHostContext() as common.UIAbilityContext, parameter, (err: BusinessError, data: iap.PurchaseResult) => {
  if (err) {
    // The request failed.
    console.error(\`Failed to purchase. Code is ${err.code}, message is ${err.message}\`);
    return;
  }
  // The request succeeded.
  console.info('Succeeded in purchasing.');
});

#### iap.createPurchase

createPurchase(context: common.UIAbilityContext, parameter: PurchaseParameter): Promise<CreatePurchaseResult>

Initiates a purchase. Consumables, non-consumables, auto-renewable subscriptions, and non-renewable subscriptions are supported. After a user initiates a purchase for a product already configured in [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html#/), this API brings up the checkout screen of IAP Kit to show the product name, price, and more.

The called API returns the result asynchronously through a promise.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Payment.IAP

**Start version**: 4.1.0(11)

**Parameters**:

| 
**Parameter**

 | 

**Type**

 | 

Mandatory

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

context

 | 

common.[UIAbilityContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md)

 | 

Yes

 | 

[UIAbility](../../../../application-framework/ability-kit/arkts-apis/stage-model/ohos-app-ability-uiability-ability-with-ui/document.md) context.

 |
| 

parameter

 | 

[PurchaseParameter](#section1340120344598)

 | 

Yes

 | 

[PurchaseParameter](#section1340120344598) object, which contains request information.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[CreatePurchaseResult](#section193852021105111)\>

 | 

**Promise** object, which contains the purchase result.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
**Error Code**

 | 

**Error Message**

 |
| :-- | :-- |
| 

401

 | 

Parameter error.

 |
| 

1001860000

 | 

The operation was canceled by the user.

 |
| 

1001860001

 | 

System internal error.

 |
| 

1001860002

 | 

The application is not authorized.

 |
| 

1001860003

 | 

Invalid product information.

 |
| 

1001860004

 | 

Too frequent API calls.

 |
| 

1001860005

 | 

Network connection error.

 |
| 

1001860007

 | 

The app to which the product belongs is not released in a specified location.

 |
| 

1001860051

 | 

Failed to purchase a product because the user already owns the product.

 |
| 

1001860054

 | 

The country or region of the signed-in HUAWEI ID does not support IAP.

 |
| 

1001860056

 | 

The user is not allowed to make purchase.

 |
| 

1001860059

 | 

Invalid promotional offer id.

 |
| 

1001860060

 | 

Invalid purchase signature.

 |

**Example**:

import { iap } from '@kit.IAPKit';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

const parameter: iap.PurchaseParameter = {
  // iap.ProductType.CONSUMABLE: consumable
  // iap.ProductType.NONCONSUMABLE: non-consumable
  // iap.ProductType.AUTORENEWABLE: auto-renewable subscription
  // iap.ProductType.NONRENEWABLE: non-renewable subscription
  productType: iap.ProductType.AUTORENEWABLE,
  // Use the product ID set by you when configuring product information in AppGallery Connect as the value of **productId**.
  productId: 'testProduct01',
  developerPayload: 'test developer payload string.'
}
iap.createPurchase(this.getUIContext().getHostContext() as common.UIAbilityContext, parameter).then((data: iap.CreatePurchaseResult) => {
  // The request succeeded.
  console.info(\`Succeeded in creating purchase. data: ${data.purchaseData}\`);
}).catch((err: BusinessError) => {
  // The request failed.
  console.error(\`Failed to create purchase. Code is ${err.code}, message is ${err.message}\`);
});

#### iap.createPurchase

createPurchase(context: common.UIAbilityContext, parameter: PurchaseParameter, callback: AsyncCallback<CreatePurchaseResult>): void

Initiates a purchase. Consumables, non-consumables, auto-renewable subscriptions, and non-renewable subscriptions are supported. After a user initiates a purchase for a product already configured in [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html#/), this API brings up the checkout screen of IAP Kit to show the product name, price, and more.

This API returns the result asynchronously through a callback.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Payment.IAP

**Start version**: 4.1.0(11)

**Parameters**:

| 
**Parameter**

 | 

**Type**

 | 

Mandatory

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

context

 | 

common.[UIAbilityContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md)

 | 

Yes

 | 

[UIAbility](../../../../application-framework/ability-kit/arkts-apis/stage-model/ohos-app-ability-uiability-ability-with-ui/document.md) context.

 |
| 

parameter

 | 

[PurchaseParameter](#section1340120344598)

 | 

Yes

 | 

[PurchaseParameter](#section1340120344598) object, which contains request information.

 |
| 

callback

 | 

AsyncCallback<[CreatePurchaseResult](#section193852021105111)\>

 | 

Yes

 | 

Callback function. If the purchase is successful, **err** is **undefined** and **data** is the obtained [CreatePurchaseResult](#section193852021105111) object; otherwise, an error object will be returned.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
**Error Code**

 | 

**Error Message**

 |
| :-- | :-- |
| 

401

 | 

Parameter error.

 |
| 

1001860000

 | 

The operation was canceled by the user.

 |
| 

1001860001

 | 

System internal error.

 |
| 

1001860002

 | 

The application is not authorized.

 |
| 

1001860003

 | 

Invalid product information.

 |
| 

1001860004

 | 

Too frequent API calls.

 |
| 

1001860005

 | 

Network connection error.

 |
| 

1001860007

 | 

The app to which the product belongs is not released in a specified location.

 |
| 

1001860051

 | 

Failed to purchase a product because the user already owns the product.

 |
| 

1001860054

 | 

The country or region of the signed-in HUAWEI ID does not support IAP.

 |
| 

1001860056

 | 

The user is not allowed to make purchase.

 |
| 

1001860059

 | 

Invalid promotional offer id.

 |
| 

1001860060

 | 

Invalid purchase signature.

 |

**Example**:

import { iap } from '@kit.IAPKit';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

const parameter: iap.PurchaseParameter = {
  // iap.ProductType.CONSUMABLE: consumable
  // iap.ProductType.NONCONSUMABLE: non-consumable
  // iap.ProductType.AUTORENEWABLE: auto-renewable subscription
  // iap.ProductType.NONRENEWABLE: non-renewable subscription
  productType: iap.ProductType.AUTORENEWABLE,
  // Use the product ID set by you when configuring product information in AppGallery Connect as the value of **productId**.
  productId: 'testProduct01',
  developerPayload: 'test developer payload string.'
}
iap.createPurchase(this.getUIContext().getHostContext() as common.UIAbilityContext, parameter, (err: BusinessError, data: iap.CreatePurchaseResult) => {
  if (err) {
    // The request failed.
    console.error(\`Failed to create purchase. Code is ${err.code}, message is ${err.message}\`);
    return;
  }
  // The request succeeded.
  console.info(\`Succeeded in creating purchase. data: ${data.purchaseData}\`);
});

#### iap.consumePurchase(deprecated)

consumePurchase(context: common.UIAbilityContext, parameter: ConsumePurchaseParameter): Promise<ConsumeResult>

Consumes a consumable after it is successfully delivered. The called API returns the result asynchronously through a promise.

**Deprecation description**: This API is deprecated since API version 4.1.0(11). You are advised to use [finishPurchase](#section124751324135814) instead.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Payment.IAP

**Device behavior differences**: This API is supported on phones, PCs/2-in-1 devices, and tablets. On other devices, it returns error code 1001860001.

**Start version**: 4.0.0(10)

**Parameters**:

| 
**Parameter**

 | 

**Type**

 | 

Mandatory

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

context

 | 

common.[UIAbilityContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md)

 | 

Yes

 | 

[UIAbility](../../../../application-framework/ability-kit/arkts-apis/stage-model/ohos-app-ability-uiability-ability-with-ui/document.md) context.

 |
| 

parameter

 | 

[ConsumePurchaseParameter](#section659703618597)

 | 

Yes

 | 

[ConsumePurchaseParameter](#section659703618597) object, which contains request information.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[ConsumeResult](#section1343816549919)\>

 | 

**Promise** object, which contains the consumption result.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
**Error Code**

 | 

**Error Message**

 |
| :-- | :-- |
| 

401

 | 

Parameter error.

 |
| 

1001860001

 | 

System internal error.

 |
| 

1001860002

 | 

The application is not authorized.

 |
| 

1001860004

 | 

Too frequent API calls.

 |
| 

1001860005

 | 

Network connection error.

 |
| 

1001860007

 | 

The app to which the product belongs is not released in a specified location.

 |
| 

1001860050

 | 

The HUAWEI ID is not signed in.

 |
| 

1001860052

 | 

The purchase cannot be finished because the user has not paid for it.

 |
| 

1001860053

 | 

The purchase has been finished and cannot be finished again.

 |
| 

1001860054

 | 

The country or region of the signed-in HUAWEI ID does not support IAP.

 |

**Example**:

import { iap } from '@kit.IAPKit';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

const parameter: iap.ConsumePurchaseParameter = {
  purchaseToken: '\*\*\*',
  developerChallenge: 'developerChallenge'
}
iap.consumePurchase(this.getUIContext().getHostContext() as common.UIAbilityContext, parameter).then((data: iap.ConsumeResult) => {
  // The request succeeded.
  console.info('Succeeded in consuming purchase.');
}).catch((err: BusinessError) => {
  // The request failed.
  console.error(\`Failed to consume purchase. Code is ${err.code}, message is ${err.message}\`);
});

#### iap.consumePurchase(deprecated)

consumePurchase(context: common.UIAbilityContext, parameter: ConsumePurchaseParameter, callback: AsyncCallback<ConsumeResult>): void

Consumes a consumable after it is successfully delivered. This API returns the result asynchronously through a callback.

**Deprecation description**: This API is deprecated since API version 4.1.0(11). You are advised to use [finishPurchase](#section2045683917408) instead.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Payment.IAP

**Device behavior differences**: This API is supported on phones, PCs/2-in-1 devices, and tablets. On other devices, it returns error code 1001860001.

**Start version**: 4.0.0(10)

**Parameters**:

| 
**Parameter**

 | 

**Type**

 | 

Mandatory

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

context

 | 

common.[UIAbilityContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md)

 | 

Yes

 | 

[UIAbility](../../../../application-framework/ability-kit/arkts-apis/stage-model/ohos-app-ability-uiability-ability-with-ui/document.md) context.

 |
| 

parameter

 | 

[ConsumePurchaseParameter](#section659703618597)

 | 

Yes

 | 

[ConsumePurchaseParameter](#section659703618597) object, which contains request information.

 |
| 

callback

 | 

AsyncCallback<[ConsumeResult](#section1343816549919)\>

 | 

Yes

 | 

Callback function. If the consumption is successful, **err** is **undefined** and **data** is the obtained [ConsumeResult](#section1343816549919) object; otherwise, an error object will be returned.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
**Error Code**

 | 

**Error Message**

 |
| :-- | :-- |
| 

401

 | 

Parameter error.

 |
| 

1001860001

 | 

System internal error.

 |
| 

1001860002

 | 

The application is not authorized.

 |
| 

1001860004

 | 

Too frequent API calls.

 |
| 

1001860005

 | 

Network connection error.

 |
| 

1001860007

 | 

The app to which the product belongs is not released in a specified location.

 |
| 

1001860050

 | 

The HUAWEI ID is not signed in.

 |
| 

1001860052

 | 

The purchase cannot be finished because the user has not paid for it.

 |
| 

1001860053

 | 

The purchase has been finished and cannot be finished again.

 |
| 

1001860054

 | 

The country or region of the signed-in HUAWEI ID does not support IAP.

 |

**Example**:

import { iap } from '@kit.IAPKit';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

const parameter: iap.ConsumePurchaseParameter = {
  purchaseToken: '\*\*\*',
  developerChallenge: 'developerChallenge'
}
iap.consumePurchase(this.getUIContext().getHostContext() as common.UIAbilityContext, parameter, (err: BusinessError, data: iap.ConsumeResult) => {
  if (err) {
    // The request failed.
    console.error(\`Failed to consume purchase. Code is ${err.code}, message is ${err.message}\`);
    return;
  }
  // The request succeeded.
  console.info('Succeeded in consuming purchase.');
});

#### iap.finishPurchase

finishPurchase(context: common.UIAbilityContext, parameter: FinishPurchaseParameter): Promise<void>

Acknowledges the delivery of a product to complete the purchase after the product is delivered. The called API returns the result asynchronously through a promise.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Payment.IAP

**Start version**: 4.1.0(11)

**Parameters**:

| 
**Parameter**

 | 

**Type**

 | 

Mandatory

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

context

 | 

common.[UIAbilityContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md)

 | 

Yes

 | 

[UIAbility](../../../../application-framework/ability-kit/arkts-apis/stage-model/ohos-app-ability-uiability-ability-with-ui/document.md) context.

 |
| 

parameter

 | 

[FinishPurchaseParameter](#section103714142118)

 | 

Yes

 | 

[FinishPurchaseParameter](#section103714142118) object, which contains request information.

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

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
**Error Code**

 | 

**Error Message**

 |
| :-- | :-- |
| 

401

 | 

Parameter error.

 |
| 

1001860001

 | 

System internal error.

 |
| 

1001860002

 | 

The application is not authorized.

 |
| 

1001860004

 | 

Too frequent API calls.

 |
| 

1001860005

 | 

Network connection error.

 |
| 

1001860050

 | 

The HUAWEI ID is not signed in.

 |
| 

1001860052

 | 

The purchase cannot be finished because the user has not paid for it.

 |
| 

1001860053

 | 

The purchase has been finished and cannot be finished again.

 |
| 

1001860054

 | 

The country or region of the signed-in HUAWEI ID does not support IAP.

 |

**Example**:

import { iap } from '@kit.IAPKit';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

const finishPurchaseParam: iap.FinishPurchaseParameter = {
  // iap.ProductType.CONSUMABLE: consumable
  // iap.ProductType.NONCONSUMABLE: non-consumable
  // iap.ProductType.AUTORENEWABLE: auto-renewable subscription
  // iap.ProductType.NONRENEWABLE: non-renewable subscription
  productType: iap.ProductType.CONSUMABLE,
  purchaseToken: '\*\*\*',
  purchaseOrderId: '\*\*\*'
};
iap.finishPurchase(this.getUIContext().getHostContext() as common.UIAbilityContext, finishPurchaseParam).then(() => {
  // The request succeeded.
  console.info('Succeeded in finishing purchase.');
}).catch((err: BusinessError) => {
  // The request failed.
  console.error(\`Failed to finish purchase. Code is ${err.code}, message is ${err.message}\`);
});

#### iap.finishPurchase

finishPurchase(context: common.UIAbilityContext, parameter: FinishPurchaseParameter, callback: AsyncCallback<void>): void

Acknowledges the delivery of a product to complete the purchase after the product is delivered. This API returns the result asynchronously through a callback.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Payment.IAP

**Start version**: 4.1.0(11)

**Parameters**:

| 
**Parameter**

 | 

**Type**

 | 

Mandatory

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

context

 | 

common.[UIAbilityContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md)

 | 

Yes

 | 

[UIAbility](../../../../application-framework/ability-kit/arkts-apis/stage-model/ohos-app-ability-uiability-ability-with-ui/document.md) context.

 |
| 

parameter

 | 

[FinishPurchaseParameter](#section103714142118)

 | 

Yes

 | 

[FinishPurchaseParameter](#section103714142118) object, which contains request information.

 |
| 

callback

 | 

AsyncCallback<void>

 | 

Yes

 | 

Callback function. If the delivery acknowledgement is complete, **err** is **undefined**; otherwise, an error object will be returned.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
**Error Code**

 | 

**Error Message**

 |
| :-- | :-- |
| 

401

 | 

Parameter error.

 |
| 

1001860001

 | 

System internal error.

 |
| 

1001860002

 | 

The application is not authorized.

 |
| 

1001860004

 | 

Too frequent API calls.

 |
| 

1001860005

 | 

Network connection error.

 |
| 

1001860050

 | 

The HUAWEI ID is not signed in.

 |
| 

1001860052

 | 

The purchase cannot be finished because the user has not paid for it.

 |
| 

1001860053

 | 

The purchase has been finished and cannot be finished again.

 |
| 

1001860054

 | 

The country or region of the signed-in HUAWEI ID does not support IAP.

 |

**Example**:

import { iap } from '@kit.IAPKit';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

const finishPurchaseParam: iap.FinishPurchaseParameter = {
  // iap.ProductType.CONSUMABLE: consumable
  // iap.ProductType.NONCONSUMABLE: non-consumable
  // iap.ProductType.AUTORENEWABLE: auto-renewable subscription
  // iap.ProductType.NONRENEWABLE: non-renewable subscription
  productType: iap.ProductType.CONSUMABLE,
  purchaseToken: '\*\*\*',
  purchaseOrderId: '\*\*\*'
};
iap.finishPurchase(this.getUIContext().getHostContext() as common.UIAbilityContext, finishPurchaseParam, (err: BusinessError) => {
  if (err) {
    // The request failed.
    console.error(\`Failed to finish purchase. Code is ${err.code}, message is ${err.message}\`);
    return;
  }
  // The request succeeded.
  console.info('Succeeded in finishing purchase.');
});

#### iap.queryOwnedPurchases(deprecated)

queryOwnedPurchases(context: common.UIAbilityContext, parameter: QueryPurchasesParameter): Promise<QueryPurchasesResult>

Queries purchase data of the products that a user has bought, including consumables and non-consumables. Only one type of products can be queried per API call.

-   For consumables, this API returns purchase data of those already bought but not consumed. If some purchase data is returned, relevant products may not be delivered due to some issues. Your app should check whether these products have been delivered, and if not, redeliver them. For a successfully delivered product, the app calls the [consumePurchase](#section754232910168) API to consume it. To obtain order information of those successfully consumed products, call [queryPurchaseRecords](#section69451529105019).

-   For non-consumables, this API returns purchase data of all the products that have been bought.

The called API returns the result asynchronously through a promise.

**Deprecation description**: This API is deprecated since API version 4.1.0(11). You are advised to use [queryPurchases](#section1147122418532) instead.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Payment.IAP

**Device behavior differences**: This API is supported on phones, PCs/2-in-1 devices, and tablets. On other devices, it returns error code 1001860001.

**Start version**: 4.0.0(10)

**Parameters**:

| 
**Parameter**

 | 

**Type**

 | 

Mandatory

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

context

 | 

common.[UIAbilityContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md)

 | 

Yes

 | 

[UIAbility](../../../../application-framework/ability-kit/arkts-apis/stage-model/ohos-app-ability-uiability-ability-with-ui/document.md) context.

 |
| 

parameter

 | 

[QueryPurchasesParameter](#section555872993213)

 | 

Yes

 | 

[QueryPurchasesParameter](#section555872993213) object, which contains request information.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[QueryPurchasesResult](#section7249204210514)\>

 | 

**Promise** object, which contains the queried purchase data.

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

401

 | 

Parameter error.

 |
| 

1001860001

 | 

System internal error.

 |
| 

1001860002

 | 

The application is not authorized.

 |
| 

1001860003

 | 

Invalid product information.

 |
| 

1001860004

 | 

Too frequent API calls.

 |
| 

1001860005

 | 

Network connection error.

 |
| 

1001860007

 | 

The app to which the product belongs is not released in a specified location.

 |
| 

1001860050

 | 

The HUAWEI ID is not signed in.

 |
| 

1001860053

 | 

The purchase has been finished and cannot be finished again.

 |
| 

1001860054

 | 

The country or region of the signed-in HUAWEI ID does not support IAP.

 |

**Example**:

import { iap } from '@kit.IAPKit';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

const parameter: iap.QueryPurchasesParameter = {
  productType: iap.ProductType.CONSUMABLE
}
iap.queryOwnedPurchases(this.getUIContext().getHostContext() as common.UIAbilityContext, parameter).then((data: iap.QueryPurchasesResult) => {
  // The request succeeded.
  console.info('Succeeded in querying owned purchases.');
}).catch((err: BusinessError) => {
  // The request failed.
  console.error(\`Failed to query owned purchases. Code is ${err.code}, message is ${err.message}\`);
});

#### iap.queryOwnedPurchases(deprecated)

queryOwnedPurchases(context: common.UIAbilityContext, parameter: QueryPurchasesParameter, callback: AsyncCallback<QueryPurchasesResult>): void

Queries purchase data of the products that a user has bought, including consumables and non-consumables. Only one type of products can be queried per API call.

-   For consumables, this API returns purchase data of those already bought but not consumed. If some purchase data is returned, relevant products may not be delivered due to some issues. Your app should check whether these products have been delivered, and if not, redeliver them. For a successfully delivered product, the app calls the [consumePurchase](#section754232910168) API to consume it. To obtain order information of those successfully consumed products, call [queryPurchaseRecords](#section1495292925012).

-   For non-consumables, this API returns purchase data of all the products that have been bought.

This API returns the result asynchronously through a callback.

**Deprecation description**: This API is deprecated since API version 4.1.0(11). You are advised to use [queryPurchases](#section11799839122114) instead.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Payment.IAP

**Device behavior differences**: This API is supported on phones, PCs/2-in-1 devices, and tablets. On other devices, it returns error code 1001860001.

**Start version**: 4.0.0(10)

**Parameters**:

| 
**Parameter**

 | 

**Type**

 | 

Mandatory

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

context

 | 

common.[UIAbilityContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md)

 | 

Yes

 | 

[UIAbility](../../../../application-framework/ability-kit/arkts-apis/stage-model/ohos-app-ability-uiability-ability-with-ui/document.md) context.

 |
| 

parameter

 | 

[QueryPurchasesParameter](#section555872993213)

 | 

Yes

 | 

[QueryPurchasesParameter](#section555872993213) object, which contains request information.

 |
| 

callback

 | 

AsyncCallback<[QueryPurchasesResult](#section7249204210514)\>

 | 

Yes

 | 

Callback function. If the query is successful, **err** is **undefined** and **data** is the obtained [QueryPurchasesResult](#section7249204210514) object; otherwise, an error object will be returned.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
**Error Code**

 | 

**Error Message**

 |
| :-- | :-- |
| 

401

 | 

Parameter error.

 |
| 

1001860001

 | 

System internal error.

 |
| 

1001860002

 | 

The application is not authorized.

 |
| 

1001860003

 | 

Invalid product information.

 |
| 

1001860004

 | 

Too frequent API calls.

 |
| 

1001860005

 | 

Network connection error.

 |
| 

1001860007

 | 

The app to which the product belongs is not released in a specified location.

 |
| 

1001860050

 | 

The HUAWEI ID is not signed in.

 |
| 

1001860053

 | 

The purchase has been finished and cannot be finished again.

 |
| 

1001860054

 | 

The country or region of the signed-in HUAWEI ID does not support IAP.

 |

**Example**:

import { iap } from '@kit.IAPKit';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

const parameter: iap.QueryPurchasesParameter = {
  productType: iap.ProductType.CONSUMABLE
}
iap.queryOwnedPurchases(this.getUIContext().getHostContext() as common.UIAbilityContext, parameter, (err: BusinessError, data: iap.QueryPurchasesResult) => {
  if (err) {
    // The request failed.
    console.error(\`Failed to query owned purchases. Code is ${err.code}, message is ${err.message}\`);
    return;
  }
  // The request succeeded.
  console.info('Succeeded in querying owned purchases.');
});

#### iap.queryPurchaseRecords(deprecated)

queryPurchaseRecords(context: common.UIAbilityContext, parameter: QueryPurchasesParameter): Promise<QueryPurchasesResult>

Obtains the purchase data of consumables that have been consumed. The called API returns the result asynchronously through a promise.

**Deprecation description**: This API is deprecated since API version 4.1.0(11). You are advised to use [queryPurchases](#section1147122418532) instead.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Payment.IAP

**Device behavior differences**: This API is supported on phones, PCs/2-in-1 devices, and tablets. On other devices, it returns error code 1001860001.

**Start version**: 4.0.0(10)

**Parameters**:

| 
**Parameter**

 | 

**Type**

 | 

Mandatory

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

context

 | 

common.[UIAbilityContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md)

 | 

Yes

 | 

[UIAbility](../../../../application-framework/ability-kit/arkts-apis/stage-model/ohos-app-ability-uiability-ability-with-ui/document.md) context.

 |
| 

parameter

 | 

[QueryPurchasesParameter](#section555872993213)

 | 

Yes

 | 

[QueryPurchasesParameter](#section555872993213) object, which contains request information.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[QueryPurchasesResult](#section7249204210514)\>

 | 

**Promise** object, which contains the purchase data of consumables that have been consumed.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
**Error Code**

 | 

**Error Message**

 |
| :-- | :-- |
| 

401

 | 

Parameter error.

 |
| 

1001860001

 | 

System internal error.

 |
| 

1001860002

 | 

The application is not authorized.

 |
| 

1001860004

 | 

Too frequent API calls.

 |
| 

1001860005

 | 

Network connection error.

 |
| 

1001860050

 | 

The HUAWEI ID is not signed in.

 |

**Example**:

import { iap } from '@kit.IAPKit';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

const parameter: iap.QueryPurchasesParameter = {
  productType: iap.ProductType.CONSUMABLE
}
iap.queryPurchaseRecords(this.getUIContext().getHostContext() as common.UIAbilityContext, parameter).then((data: iap.QueryPurchasesResult) => {
  // The request succeeded.
  console.info('Succeeded in querying purchase records.');  
}).catch((err: BusinessError) => {
  // The request failed.
  console.error(\`Failed to query purchase records. Code is ${err.code}, message is ${err.message}\`);
});

#### iap.queryPurchaseRecords(deprecated)

queryPurchaseRecords(context: common.UIAbilityContext, parameter: QueryPurchasesParameter, callback: AsyncCallback<QueryPurchasesResult>): void

Obtains the purchase data of consumables that have been consumed. This API returns the result asynchronously through a callback.

**Deprecation description**: This API is deprecated since API version 4.1.0(11). You are advised to use [queryPurchases](#section11799839122114) instead.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Payment.IAP

**Device behavior differences**: This API is supported on phones, PCs/2-in-1 devices, and tablets. On other devices, it returns error code 1001860001.

**Start version**: 4.0.0(10)

**Parameters**:

| 
**Parameter**

 | 

**Type**

 | 

Mandatory

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

context

 | 

common.[UIAbilityContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md)

 | 

Yes

 | 

[UIAbility](../../../../application-framework/ability-kit/arkts-apis/stage-model/ohos-app-ability-uiability-ability-with-ui/document.md) context.

 |
| 

parameter

 | 

[QueryPurchasesParameter](#section555872993213)

 | 

Yes

 | 

[QueryPurchasesParameter](#section555872993213) object, which contains request information.

 |
| 

callback

 | 

AsyncCallback<[QueryPurchasesResult](#section7249204210514)\>

 | 

Yes

 | 

Callback function. If the query is successful, **err** is **undefined** and **data** is the obtained [QueryPurchasesResult](#section7249204210514) object; otherwise, an error object will be returned.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
**Error Code**

 | 

**Error Message**

 |
| :-- | :-- |
| 

401

 | 

Parameter error.

 |
| 

1001860001

 | 

System internal error.

 |
| 

1001860002

 | 

The application is not authorized.

 |
| 

1001860004

 | 

Too frequent API calls.

 |
| 

1001860005

 | 

Network connection error.

 |
| 

1001860050

 | 

The HUAWEI ID is not signed in.

 |

**Example**:

import { iap } from '@kit.IAPKit';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

const parameter: iap.QueryPurchasesParameter = {
  productType: iap.ProductType.CONSUMABLE
}
iap.queryPurchaseRecords(this.getUIContext().getHostContext() as common.UIAbilityContext, parameter, (err: BusinessError, data: iap.QueryPurchasesResult) => {
  if (err) {
    // The request failed.
    console.error(\`Failed to query purchase records. Code is ${err.code}, message is ${err.message}\`);
    return;
  }
  // The request succeeded.
  console.info('Succeeded in querying purchase records.');
});

#### iap.queryPurchases

queryPurchases(context: common.UIAbilityContext, parameter: QueryPurchasesParameter): Promise<QueryPurchaseResult>

Queries the order information of purchased products, including:

-   Purchased products for which the delivery is not acknowledged.
-   Non-consumables, auto-renewable subscriptions, and non-renewable subscriptions that are currently active.

The called API returns the result asynchronously through a promise.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Payment.IAP

**Start version**: 4.1.0(11)

**Parameters**:

| 
**Parameter**

 | 

**Type**

 | 

Mandatory

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

context

 | 

common.[UIAbilityContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md)

 | 

Yes

 | 

[UIAbility](../../../../application-framework/ability-kit/arkts-apis/stage-model/ohos-app-ability-uiability-ability-with-ui/document.md) context.

 |
| 

parameter

 | 

[QueryPurchasesParameter](#section555872993213)

 | 

Yes

 | 

[QueryPurchasesParameter](#section555872993213) object, which contains request information.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[QueryPurchaseResult](#section820381425513)\>

 | 

**Promise** object, which contains the order information of purchased products. In the sandbox environment, the order information of delivered non-consumables is not returned.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
**Error Code**

 | 

**Error Message**

 |
| :-- | :-- |
| 

401

 | 

Parameter error.

 |
| 

1001860001

 | 

System internal error.

 |
| 

1001860002

 | 

The application is not authorized.

 |
| 

1001860004

 | 

Too frequent API calls.

 |
| 

1001860005

 | 

Network connection error.

 |
| 

1001860050

 | 

The HUAWEI ID is not signed in.

 |
| 

1001860054

 | 

The country or region of the signed-in HUAWEI ID does not support IAP.

 |

**Example**:

import { iap } from '@kit.IAPKit';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

const parameter: iap.QueryPurchasesParameter = {
  productType: iap.ProductType.CONSUMABLE,
  queryType: iap.PurchaseQueryType.UNFINISHED
}
iap.queryPurchases(this.getUIContext().getHostContext() as common.UIAbilityContext, parameter).then((data: iap.QueryPurchaseResult) => {
  // The request succeeded.
  console.info(\`Succeeded in querying purchases. data len: ${data.purchaseDataList?.length}\`);
}).catch((err: BusinessError) => {
  // The request failed.
  console.error(\`Failed to query purchases. Code is ${err.code}, message is ${err.message}\`);
});

#### iap.queryPurchases

queryPurchases(context: common.UIAbilityContext, parameter: QueryPurchasesParameter, callback: AsyncCallback<QueryPurchaseResult>): void

Queries the order information of purchased products, including:

-   Purchased products for which the delivery is not acknowledged.
-   Non-consumables, auto-renewable subscriptions, and non-renewable subscriptions that are currently active.

This API returns the result asynchronously through a callback.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Payment.IAP

**Start version**: 4.1.0(11)

**Parameters**:

| 
**Parameter**

 | 

**Type**

 | 

Mandatory

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

context

 | 

common.[UIAbilityContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md)

 | 

Yes

 | 

[UIAbility](../../../../application-framework/ability-kit/arkts-apis/stage-model/ohos-app-ability-uiability-ability-with-ui/document.md) context.

 |
| 

parameter

 | 

[QueryPurchasesParameter](#section555872993213)

 | 

Yes

 | 

[QueryPurchasesParameter](#section555872993213) object, which contains request information.

 |
| 

callback

 | 

AsyncCallback<[QueryPurchaseResult](#section820381425513)\>

 | 

Yes

 | 

Callback function. If the query is successful, **err** is **undefined** and **data** is the obtained [QueryPurchaseResult](#section820381425513) object; otherwise, an error object will be returned. In the sandbox environment, the order information of delivered non-consumables is not returned.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
**Error Code**

 | 

**Error Message**

 |
| :-- | :-- |
| 

401

 | 

Parameter error.

 |
| 

1001860001

 | 

System internal error.

 |
| 

1001860002

 | 

The application is not authorized.

 |
| 

1001860004

 | 

Too frequent API calls.

 |
| 

1001860005

 | 

Network connection error.

 |
| 

1001860050

 | 

The HUAWEI ID is not signed in.

 |
| 

1001860054

 | 

The country or region of the signed-in HUAWEI ID does not support IAP.

 |

**Example**:

import { iap } from '@kit.IAPKit';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

const parameter: iap.QueryPurchasesParameter = {
  productType: iap.ProductType.CONSUMABLE,
  queryType: iap.PurchaseQueryType.UNFINISHED
}
iap.queryPurchases(this.getUIContext().getHostContext() as common.UIAbilityContext, parameter, (err: BusinessError, data: iap.QueryPurchaseResult) => {
  if (err) {
    // The request failed.
    console.error(\`Failed to query purchases. Code is ${err.code}, message is ${err.message}\`);
    return;
  }
  // The request succeeded.
  console.info(\`Succeeded in querying purchases. data len: ${data.purchaseDataList?.length}\`);
});

#### iap.showManagedSubscriptions

showManagedSubscriptions(context: common.Context, uiParameter: UIWindowParameter, groupId?: string): Promise<void>

Redirects to the subscription status screen or the subscription details screen. The called API returns the result asynchronously through a promise.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Payment.IAP

**Device behavior differences**: This API is supported on phones, tablets, 2-in-1 devices, and TVs. On other devices, it returns error code 801.

**Start version**: 5.0.0(12)

**Parameters**:

| 
**Parameter**

 | 

**Type**

 | 

Mandatory

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

context

 | 

common.[Context](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md)

 | 

Yes

 | 

Context. [UIAbilityContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md) is recommended.

 |
| 

uiParameter

 | 

[UIWindowParameter](#section12131915171317)

 | 

Yes

 | 

[UIWindowParameter](#section12131915171317) object, which contains the UI display mode.

 |
| 

groupId

 | 

string

 | 

No

 | 

Subscription group ID, which comes from the subscription group configured in [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html#/). For details, please refer to [Auto-renewable Subscriptions](https://developer.huawei.com/consumer/en/doc/app/non-subscription-0000001958955109).

NOTE:

-   If **groupId** is passed, the subscription details screen will be displayed.
-   If **groupId** is not passed, the subscription status screen will be displayed. If a user has only one subscription data record in an app, the screen for showing the details of this subscription will be displayed.

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

**Promise** object. **Promise** object without a return value.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
**Error Code**

 | 

**Error Message**

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

Capability not supported. Failed to call the API due to limited device capabilities.

 |
| 

1001860001

 | 

System internal error.

 |
| 

1001860002

 | 

The application is not authorized.

 |
| 

1001860004

 | 

Too frequent API calls.

 |
| 

1001860005

 | 

Network connection error.

 |
| 

1001860050

 | 

The HUAWEI ID is not signed in.

 |
| 

1001860054

 | 

The country or region of the signed-in HUAWEI ID does not support IAP.

 |

**Example**:

import { iap } from '@kit.IAPKit';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

const uiWindowParameter: iap.UIWindowParameter = {
  windowScreenMode: iap.WindowScreenMode.DIALOG\_BOX
}
const groupId = '\*\*\*';
iap.showManagedSubscriptions(this.getUIContext().getHostContext() as common.UIAbilityContext, uiWindowParameter, groupId).then(() => {
  // The request succeeded.
  console.info('Succeeded in showing subscription page.');
}).catch((err: BusinessError) => {
  // The request failed.
  console.error(\`Failed to show subscription page. Code is ${err.code}, message is ${err.message}\`);
});

#### iap.isSandboxActivated

isSandboxActivated(context: common.Context): Promise<boolean>

Checks whether the sandbox environment is available. The called API returns the result asynchronously through a promise.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Payment.IAP

**Start version**: 5.0.0(12)

**Parameters**:

| 
**Parameter**

 | 

**Type**

 | 

Mandatory

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

context

 | 

common.[Context](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md)

 | 

Yes

 | 

Context. [UIAbilityContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md) is recommended.

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

**Promise** object. If **true** is returned, the sandbox environment is available. If **false** is returned, the sandbox environment is unavailable. You can check the reason based on the returned error code.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
**Error Code**

 | 

**Error Message**

 |
| :-- | :-- |
| 

401

 | 

Parameter error.

 |
| 

1001860001

 | 

System internal error.

 |
| 

1001860002

 | 

The application is not authorized.

 |
| 

1001860004

 | 

Too frequent API calls.

 |
| 

1001860005

 | 

Network connection error.

 |
| 

1001860050

 | 

The HUAWEI ID is not signed in.

 |
| 

1001860054

 | 

The country or region of the signed-in HUAWEI ID does not support IAP.

 |
| 

1001860057

 | 

The app provision type is not debug.

 |
| 

1001860058

 | 

The HUAWEI ID is not test account.

 |

**Example**:

import { iap } from '@kit.IAPKit';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

iap.isSandboxActivated(this.getUIContext().getHostContext() as common.UIAbilityContext).then((isActivated: boolean) => {
  // The request succeeded.
  console.info(\`Succeeded in checking the sandbox status. is activate: ${isActivated}\`);
}).catch((err: BusinessError) => {
  // The request failed.
  console.error(\`Failed to check the sandbox status. Code is ${err.code}, message is ${err.message}\`);
});

#### iap.createRefundRequest

createRefundRequest(context: common.Context, purchaseOrderId: string): Promise<void>

Refund API, which is called to start the refund process. This API applies only to non-game apps. The called API returns the result asynchronously through a promise.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.3(15).

**System capability**: SystemCapability.Payment.IAP

**Device behavior differences**: This API is supported on phones, tablets, and 2-in-1 devices. On other devices, it returns error code 801.

**Start version**: 5.0.3(15)

**Parameters**:

| 
**Parameter**

 | 

**Type**

 | 

Mandatory

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

context

 | 

common.[Context](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md)

 | 

Yes

 | 

Context.

 |
| 

purchaseOrderId

 | 

string

 | 

Yes

 | 

Order ID of a purchase. The value contains a maximum of 256 characters.

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

Promise object. Promise object without a return value.

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

401

 | 

Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.

 |
| 

801

 | 

Capability not supported. Failed to call the API due to limited device capabilities.

 |
| 

1001860000

 | 

The operation was canceled by the user.

 |
| 

1001860001

 | 

System internal error.

 |
| 

1001860002

 | 

The application is not authorized.

 |
| 

1001860004

 | 

Too frequent API calls.

 |
| 

1001860005

 | 

Network connection error.

 |
| 

1001860054

 | 

The country or region of the signed-in HUAWEI ID does not support IAP.

 |
| 

1001860061

 | 

The purchase has been refunded or in refund.

 |
| 

1001860062

 | 

Refund is not allowed.

 |

**Example**:

import { iap } from '@kit.IAPKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct IapTest {
  /\*\*
 \* Show the refund screen.
   \*/
  createRefundRequest() {
    const context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
  // Call **iap.createRefundRequest** to process the refund. Pass **context** and **purchaseOrderId** in the call request.
    let purchaseOrderId = '';
    iap.createRefundRequest(context, purchaseOrderId).then(() => {
    // Refund succeeded.
      console.info('Succeeded in create refund request.');
      // ...
    }).catch((err: BusinessError) => {
    // Refund failed.
      console.error(\`Failed to create refund request. Code is ${err.code}, message is ${err.message}\`);
      // ...
    });
  }
  build() {
  }
}

#### QueryProductsParameter

Request parameters for the [queryProducts](#section55531442102518) API.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Payment.IAP

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

productType

 | 

[ProductType](#section59035422210)

 | 

No

 | 

No

 | 

Product type. The options are as follows:

-   **CONSUMABLE**: consumable
-   **NONCONSUMABLE**: non-consumable
-   **AUTORENEWABLE**: auto-renewable subscription
-   NONRENEWABLE: non-renewable subscription

 |
| 

productIds

 | 

string\[\]

 | 

No

 | 

No

 | 

ID list of products to be queried. Each product ID must exist and be unique in your app.

Product IDs are specified when you configure products in [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html#/). For details, please refer to [Configuring Products](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/iap-config-product).

NOTE:

A maximum of 200 product IDs can be queried at a time. For a large number of products, it is advised to query their IDs in batches.

 |

#### Product

Details of a product.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Payment.IAP

**Start version**: 4.0.0(10)

| 
Name

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

id

 | 

string

 | 

No

 | 

No

 | 

Product ID.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

 |
| 

type

 | 

[ProductType](#section59035422210)

 | 

No

 | 

No

 | 

Product type.

-   **CONSUMABLE**: consumable
-   **NONCONSUMABLE**: non-consumable
-   **AUTORENEWABLE**: auto-renewable subscription
-   NONRENEWABLE: non-renewable subscription

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

 |
| 

name

 | 

string

 | 

No

 | 

No

 | 

Product name, which you set when adding the product. The name is displayed on the IAP checkout screen.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

 |
| 

description

 | 

string

 | 

No

 | 

No

 | 

Product description, which you set when adding the product.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

 |
| 

price(deprecated)

 | 

string

 | 

No

 | 

No

 | 

Displayed price of a product, in the format of **Currency+Price**, for example, **EUR 0.15**. In some countries and regions, the value of this parameter is in the format of a currency symbol together with a price, for example, **¥0.15** in the Chinese mainland. The price includes the tax.

-   For a consumable or non-consumable with a [promotional price](https://developer.huawei.com/consumer/en/doc/app/promotion-non-subscription-0000001931836332), this parameter indicates the promotional price. If the product has no promotional price, this parameter indicates its original price.
-   For an auto-renewable subscription, this parameter indicates its original price.

NOTE:

This parameter is deprecated since 4.1.0(11). You are advised to use **localPrice** instead.

 |
| 

localPrice

 | 

string

 | 

No

 | 

Yes

 | 

Displayed price of a product, in the format of **Currency+Price**, for example, **EUR 0.15**. In some countries and regions, the value of this parameter is in the format of a currency symbol together with a price, for example, **¥0.15** in the Chinese mainland. The price includes the tax. Optional.

-   For a consumable, non-consumable, or non-renewable subscription with a promotional price, this parameter indicates the promotional price. If the product has no promotional price, this parameter indicates its original price. (The promotional price capability has been adjusted to [temporary price adjustment](https://developer.huawei.com/consumer/en/doc/app/revise-non-subscription-0000001931836328). In the temporary price adjustment scenario, this parameter indicates the original price of a product.)
-   For an auto-renewable subscription, this parameter indicates its original price.

**Start version**: 4.1.0(11)

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

 |
| 

microPrice

 | 

number

 | 

No

 | 

No

 | 

Product price in micro unit, which equals the actual product price multiplied by 1,000,000. For example, if the actual price of a product is US$1.99, the product price in micro unit is 1,990,000 (1.99 x 1,000,000).

-   For a consumable, non-consumable, or non-renewable subscription with a promotional price, this parameter indicates the promotional price in micro unit. If the product has no promotional price, this parameter indicates its original price in micro unit. (The promotional price capability has been adjusted to [temporary price adjustment](https://developer.huawei.com/consumer/en/doc/app/revise-non-subscription-0000001931836328). In the temporary price adjustment scenario, this parameter indicates the original price of a product.)
-   For an auto-renewable subscription, this parameter indicates its original price in micro unit.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

 |
| 

originalLocalPrice

 | 

string

 | 

No

 | 

No

 | 

Original price of a product, in the format of **Currency+Price**, for example, **EUR 0.15**. In some countries and regions, the value of this parameter is in the format of a currency symbol together with a price, for example, **¥0.15** in the Chinese mainland. The price includes the tax.

-   For a consumable, non-consumable, or non-renewable subscription, this parameter only indicates its original price, regardless of whether a [promotional price](https://developer.huawei.com/consumer/en/doc/app/promotion-non-subscription-0000001931836332) is set.
-   For an auto-renewable subscription, this parameter will not be returned.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

 |
| 

originalMicroPrice

 | 

number

 | 

No

 | 

No

 | 

Original price in micro unit of a product, which equals the original product price multiplied by 1,000,000. For example, if the original price of a product is US$1.99, the product price in micro unit is 1,990,000 (1.99 x 1,000,000).

-   For a consumable, non-consumable, or non-renewable subscription, this parameter only indicates its original price in micro unit, regardless of whether a [promotional price](https://developer.huawei.com/consumer/en/doc/app/promotion-non-subscription-0000001931836332) is set.
-   For an auto-renewable subscription, this parameter will not be returned.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

 |
| 

currency

 | 

string

 | 

No

 | 

No

 | 

Currency used to pay for a product, for example, CNY.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

 |
| 

status

 | 

[ProductStatus](#section2762171942710)

 | 

No

 | 

Yes

 | 

Product status.

**Start version**: 5.0.0(12)

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

 |
| 

subscriptionInfo

 | 

[SubscriptionInfo](#section151973366473)

 | 

No

 | 

Yes

 | 

Information about an auto-renewable subscription. Optional.

**Start version**: 4.1.0(11)

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

 |
| 

promotionalOffers

 | 

[PromotionalOffer](#section446812293465)\[\]

 | 

No

 | 

Yes

 | 

List of promotional offers for specific user groups.

**Start version**: 5.0.0(12)

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

 |
| 

jsonRepresentation

 | 

string

 | 

No

 | 

Yes

 | 

Original JSON character string of product details.

**Start version**: 4.1.0(11)

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

 |

#### PromotionalOffer

Custom special offers supported by a subscription.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Payment.IAP

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

offerId

 | 

string

 | 

No

 | 

No

 | 

Offer ID.

 |
| 

paymentMode

 | 

[OfferPaymentMode](#section23427243315)

 | 

No

 | 

No

 | 

Payment method of a promotion.

 |
| 

periodUnit

 | 

[PeriodUnit](#section3468210113210)

 | 

No

 | 

Yes

 | 

Unit of the subscription billing cycle.

 |
| 

periodCount

 | 

number

 | 

No

 | 

Yes

 | 

Number of billing cycles for a subscription.

 |
| 

localPrice

 | 

string

 | 

No

 | 

No

 | 

Discounted price of a product, in the format of **Currency+Price**, for example, **EUR 0.15**. In some countries and regions, the value of this parameter is in the format of a currency symbol together with a price, for example, **¥0.15** in the Chinese mainland.

 |
| 

microPrice

 | 

number

 | 

No

 | 

No

 | 

Discounted price in micro unit, which equals the actual product price multiplied by 1,000,000. For example, if the actual price of a product is US$1.99, the product price in micro unit is 1,990,000 (1.99 x 1,000,000).

 |

#### SubscriptionInfo

Subscription information.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Payment.IAP

**Start version**: 4.1.0(11)

| 
**Name**

 | 

**Type**

 | 

Read-Only

 | 

**Optional**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

periodUnit

 | 

[PeriodUnit](#section3468210113210)

 | 

No

 | 

No

 | 

Unit of the subscription billing cycle.

 |
| 

periodCount

 | 

number

 | 

No

 | 

No

 | 

Number of billing cycles for a subscription.

 |
| 

groupId

 | 

string

 | 

No

 | 

No

 | 

Subscription group ID.

 |
| 

groupLevel

 | 

number

 | 

No

 | 

No

 | 

Subscription level.

 |
| 

hasEligibilityForIntroOffer

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether a user has enjoyed an introductory offer. The options are as follows:

-   **true**: yes
-   **false**: no
-   Other values: No relevant information is obtained.

 |
| 

introductoryOffer

 | 

[SubscriptionOffer](#section16479185319413)

 | 

No

 | 

Yes

 | 

Promotion information.

 |

#### SubscriptionOffer

Promotion information.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Payment.IAP

**Start version**: 4.1.0(11)

| 
**Name**

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

paymentMode

 | 

[OfferPaymentMode](#section23427243315)

 | 

No

 | 

No

 | 

Payment method of a promotion.

 |
| 

periodUnit

 | 

[PeriodUnit](#section3468210113210)

 | 

No

 | 

No

 | 

Unit of the subscription billing cycle.

 |
| 

periodCount

 | 

number

 | 

No

 | 

No

 | 

Duration of a promotional activity, in the same unit as the billing cycle of a subscription. For example, if a promotional activity covers two billing cycles and the billing cycle is two weeks, the value of this parameter is four weeks (that is, two billing cycles multiplied by two weeks.)

 |
| 

localPrice

 | 

string

 | 

No

 | 

No

 | 

Promotional price of a product, in the format of **Currency+Price**, for example, **EUR 0.15**. In some countries and regions, the value of this parameter is in the format of a currency symbol together with a price, for example, **¥0.15** in the Chinese mainland.

 |
| 

microPrice

 | 

number

 | 

No

 | 

No

 | 

Promotional price in micro unit. Promotional price in micro unit, which equals the product price multiplied by 1,000,000.

 |
| 

offerType

 | 

[OfferType](#section131398372313)

 | 

No

 | 

No

 | 

Promotion type.

 |

#### PurchaseParameter

Request parameters of the [purchase](#section107784425446) and [createPurchase](#section18798154545516) APIs.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Payment.IAP

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

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

productId

 | 

string

 | 

No

 | 

No

 | 

ID of a product to be paid. Product IDs are specified when you configure products in [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html#/). For details, please refer to [Configuring Products](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/iap-config-product).

 |
| 

productType

 | 

[ProductType](#section59035422210)

 | 

No

 | 

No

 | 

Product type. The options are as follows:

-   **CONSUMABLE**: consumable
-   **NONCONSUMABLE**: non-consumable
-   **AUTORENEWABLE**: auto-renewable subscription
-   NONRENEWABLE: non-renewable subscription

 |
| 

developerPayload

 | 

string

 | 

No

 | 

Yes

 | 

Information stored on the merchant side.

If a value exists, the value will be returned in the callback result to the app after successful payment.

NOTE:

The value length range is \[0, 256\]. If the length limit is exceeded, the truncated data will be returned after the payment is successful. You are advised to verify the value length before a purchase request is made to avoid truncation.

 |
| 

reservedInfo

 | 

string

 | 

No

 | 

Yes

 | 

Additional information passed via a JSON string in **key-value** format.

Example:

let reservedInfo = "{\\"key1\\":\\"value1\\",\\"key2\\":\\"value2\\"}";

NOTE:

This parameter is reserved for you to pass additional information. You can choose to set it or not.

 |
| 

promotionalOfferId

 | 

string

 | 

No

 | 

Yes

 | 

Offer ID. This ID is the same as the promotional offer ID set by you when [configuring a promotional offer](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/iap-subscription-functions#li1264912560544) for a product. To pass this parameter and make sure it takes effect, pass the special offer information in the **jwsRepresentation** parameter.

**Start version**: 5.0.0(12)

 |
| 

applicationUserName

 | 

string

 | 

No

 | 

Yes

 | 

Obfuscated string that serves as a unique identifier for each user account. This parameter can be passed in the scenario where the offer ID is passed.

**Start version**: 5.0.0(12)

 |
| 

jwsRepresentation

 | 

string

 | 

No

 | 

Yes

 | 

JWS signature data that contains purchase parameters, such as special offer information. For details, please refer to [Generating a Signed Purchase Parameter for a Promotion](../../rest-apis/generating-a-signed-purchase-parameter-for-a-promotion/document.md).

**Start version**: 5.0.0(12)

 |
| 

quantity

 | 

number

 | 

No

 | 

Yes

 | 

Quantity of the purchased consumables or non-renewable subscriptions.

-   The **quantity** parameter applies to one product type only. It does not support a mix of different product types.
-   The maximum quantity is **10**.

CAUTION:

If the **quantity** parameter is used to support bulk purchases of products, your app needs to verify that the ordered quantity matches the final delivered quantity to prevent under-deliveries or over-deliveries.

**Atomic service API**: This API can be used in atomic services since API version 5.0.3(15).

**Start version**: 5.0.3(15)

 |

#### PurchaseResult(deprecated)

Result returned by the [purchase](#section107784425446) API.

**Deprecation description**: This API is deprecated since API version 4.1.0(11).

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Payment.IAP

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

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

inAppPurchaseData

 | 

string

 | 

No

 | 

No

 | 

JSON string of order data. Check the parameters in the string in [InAppPurchaseData](../data-types/document.md#section494862084917).

 |
| 

signature

 | 

string

 | 

No

 | 

No

 | 

Signature string generated after the **paymentData** string is signed using the IAP private key.

 |
| 

signatureAlgorithm

 | 

string

 | 

No

 | 

No

 | 

Signature algorithm. The value is fixed at **SHA256WithRSA/PSS**.

 |

#### CreatePurchaseResult

Result returned by the [createPurchase](#section18798154545516) API.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Payment.IAP

**Start version**: 4.1.0(11)

| 
**Name**

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

purchaseData

 | 

string

 | 

No

 | 

No

 | 

JSON string containing the payment result. Check the parameters in the string in [PurchaseData](../data-types/document.md#section650794012482).

 |

#### ConsumePurchaseParameter(deprecated)

Request parameters for the [consumePurchase](#section754232910168) API.

**Deprecation description**: This API is deprecated since API version 4.1.0(11).

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Payment.IAP

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

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

purchaseToken

 | 

string

 | 

No

 | 

No

 | 

Purchase token, which is generated by the IAP server when the payment for a product is complete.

NOTE:

**purchaseToken** is obtained from [InAppPurchaseData](../data-types/document.md#section494862084917). When the payment is successful or the [queryOwnedPurchases](#section78016131463) API is called, [InAppPurchaseData](../data-types/document.md#section494862084917) in JSON format will be returned.

 |
| 

developerChallenge

 | 

string

 | 

No

 | 

Yes

 | 

Custom challenge, which uniquely identifies a consumption request. After the consumption is successful, the challenge is recorded in the purchase data and returned.

NOTE:

The value length range is \[0, 64\].

 |

#### ConsumeResult(deprecated)

Result returned by the [consumePurchase](#section754232910168) API.

**Deprecation description**: This API is deprecated since API version 4.1.0(11).

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Payment.IAP

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

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

consumedPurchaseData

 | 

string

 | 

No

 | 

No

 | 

JSON string that contains consumption result data. Check the parameters in the string in [InAppPurchaseData](../data-types/document.md#section494862084917).

 |
| 

signature

 | 

string

 | 

No

 | 

No

 | 

Signature string generated after the consumption data (**consumedPurchaseData**) is signed using the IAP private key. The signature algorithm is specified by the **signatureAlgorithm** field.

After receiving the signature string, the app needs to perform signature verification on the JSON string of **consumedPurchaseData**. For details, please refer to [Verifying the Signature in the Returned Result](../../rest-apis/verifying-the-signature-in-the-returned-result/document.md).

 |
| 

signatureAlgorithm

 | 

string

 | 

No

 | 

No

 | 

Signature algorithm. The value is fixed at **SHA256WithRSA/PSS**.

 |

#### FinishPurchaseParameter

Request parameters for the [finishPurchase](#section124751324135814) API.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Payment.IAP

**Start version**: 4.1.0(11)

| 
**Name**

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

productType

 | 

[ProductType](#section59035422210)

 | 

No

 | 

No

 | 

Product type.

-   **CONSUMABLE**: consumable
-   **NONCONSUMABLE**: non-consumable
-   **AUTORENEWABLE**: auto-renewable subscription
-   NONRENEWABLE: non-renewable subscription

 |
| 

purchaseToken

 | 

string

 | 

No

 | 

No

 | 

Purchase token returned in the purchase order.

In a consumable/non-consumable purchase, each purchase token matches a specific order. In a subscription purchase, each purchase token matches a subscription ID.

NOTE:

**purchaseToken** is obtained from [PurchaseOrderPayload](../data-types/document.md#section260562820380). [PurchaseOrderPayload](../data-types/document.md#section260562820380) is returned after the [createPurchase](#section18798154545516) or [queryPurchases](#section1147122418532) API is called.

 |
| 

purchaseOrderId

 | 

string

 | 

No

 | 

No

 | 

Order ID returned after a purchase. The value contains a maximum of 256 characters.

NOTE:

**purchaseOrderId** is obtained from [PurchaseOrderPayload](../data-types/document.md#section260562820380). [PurchaseOrderPayload](../data-types/document.md#section260562820380) is returned after the [createPurchase](#section18798154545516) or [queryPurchases](#section1147122418532) API is called.

 |

#### QueryPurchasesParameter

Request parameters of the [queryOwnedPurchases](#section78016131463), [queryPurchaseRecords](#section69451529105019), and [queryPurchases](#section1147122418532) APIs.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Payment.IAP

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

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

productType

 | 

[ProductType](#section59035422210)

 | 

No

 | 

No

 | 

Product type. The options are as follows:

-   **CONSUMABLE**: consumable
-   **NONCONSUMABLE**: non-consumable
-   **AUTORENEWABLE**: auto-renewable subscription
-   NONRENEWABLE: non-renewable subscription

 |
| 

continuationToken

 | 

string

 | 

No

 | 

Yes

 | 

Data location flag for a query in pagination mode.

This parameter is optional for the first query. If a user has a large number of products and the response contains **continuationToken**, the app must initiate another call on the current API and pass the already received **continuationToken**. If product query is still incomplete, the app needs to call the API again until no **continuationToken** is returned, indicating that all products are returned.

 |
| 

queryType

 | 

[PurchaseQueryType](#section1389262216514)

 | 

No

 | 

Yes

 | 

Query type. The options are as follows:

-   **ALL**: All purchase records, including consumables, non-consumables, auto-renewable subscriptions, and non-renewable subscriptions.
-   **UNFINISHED** (default value): Consumables, non-consumables, auto-renewable subscriptions, and non-renewable subscriptions that have been purchased but not delivered.
-   **CURRENT\_ENTITLEMENT**: Non-consumables that have been purchased and subscriptions that are currently active.

NOTE:

Regardless of the value you set, this parameter has no effect for [queryOwnedPurchases](#section78016131463) and [queryPurchaseRecords](#section69451529105019).

**Start version**: 4.1.0(11)

 |

#### QueryPurchasesResult(deprecated)

Result returned by the [queryOwnedPurchases](#section78016131463) or [queryPurchaseRecords](#section69451529105019) API.

**Deprecation description**: This API is deprecated since API version 4.1.0(11).

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Payment.IAP

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

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

productList

 | 

string\[\]

 | 

No

 | 

No

 | 

Product ID array.

 |
| 

inAppPurchaseDataList

 | 

string\[\]

 | 

No

 | 

No

 | 

[InAppPurchaseData](../data-types/document.md#section494862084917) in JSON format, which is used together with **inAppSignatureList** for signature verification. For details about the parameters contained in each JSON string, please refer to [InAppPurchaseData](../data-types/document.md#section494862084917)

 |
| 

inAppSignatureList

 | 

string\[\]

 | 

No

 | 

No

 | 

Signature string of each JSON string in **inAppPurchaseDataList**. The IAP private key is used for signing through the signature algorithm specified by the **signatureAlgorithm** field.

The app needs to verify each JSON string in **inAppPurchaseDataList**. For details about the verification method, please refer to [Verifying the Signature in the Returned Result](../../rest-apis/verifying-the-signature-in-the-returned-result/document.md).

 |
| 

continuationToken

 | 

string

 | 

No

 | 

Yes

 | 

Data location flag for a query in pagination mode.

If a user has a large number of products and the response contains **continuationToken**, the app must initiate another call on the current API and pass the already received **continuationToken**. If product query is still incomplete, the app needs to call the API again until no **continuationToken** is returned, indicating that all products are returned.

 |
| 

signatureAlgorithm

 | 

string

 | 

No

 | 

No

 | 

Signature algorithm. The value is fixed at **SHA256WithRSA/PSS**.

 |

#### QueryPurchaseResult

Result returned by the [queryPurchases](#section1147122418532) API.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Payment.IAP

**Start version**: 4.1.0(11)

| 
**Name**

 | 

**Type**

 | 

Read-Only

 | 

**Optional**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

purchaseDataList

 | 

string\[\]

 | 

No

 | 

No

 | 

Array of [PurchaseData](../data-types/document.md#section650794012482) character strings.

 |
| 

continuationToken

 | 

string

 | 

No

 | 

Yes

 | 

Data location flag for a query in pagination mode.

If a user has a large number of products and the response contains **continuationToken**, the app must initiate another call on the current API and pass the already received **continuationToken**. If product query is still incomplete, the app needs to call the API again until no **continuationToken** is returned, indicating that all products are returned.

 |

#### UIWindowParameter

UI parameters of the [iap.showManagedSubscriptions](#section39973360502) API.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Payment.IAP

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

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

windowScreenMode

 | 

[WindowScreenMode](#section15231134814464)

 | 

No

 | 

No

 | 

UI mode.

-   **DIALOG\_BOX**: pop-up.
-   **FULLSCREEN**: full-screen.

 |
