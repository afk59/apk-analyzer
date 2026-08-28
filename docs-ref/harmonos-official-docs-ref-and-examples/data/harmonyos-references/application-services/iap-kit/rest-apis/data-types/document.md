# Data Types

#### PurchaseOrderPayload

Purchase data model, which supports consumables, non-consumables, auto-renewable subscriptions, and non-renewable subscriptions.

| 
Parameter

 | 

Mandatory

 | 

Type

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

environment

 | 

Yes

 | 

String

 | 

Environment type.

-   **NORMAL**: production environment
-   **SANDBOX**: sandbox environment

 |
| 

purchaseOrderId

 | 

Yes

 | 

String

 | 

Order ID of a purchase. The value contains a maximum of 256 characters.

 |
| 

purchaseToken

 | 

Yes

 | 

String

 | 

Purchase token. In a consumable/non-consumable/non-renewable subscription purchase, each purchase token matches a specific order. In an auto-renewable subscription purchase, each purchase token matches a subscription ID. Each purchase token is valid for only one delivery. To avoid duplicate deliveries to the same user, it is necessary to restrict the number of times a purchase token can be used for delivery. The value contains a maximum of 256 characters.

 |
| 

applicationId

 | 

Yes

 | 

String

 | 

App ID. For details about how to obtain the app ID, please refer to [Configuring App Identity Information](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/iap-config-app-identity-info).

 |
| 

productId

 | 

Yes

 | 

String

 | 

Product ID.

 |
| 

productType

 | 

Yes

 | 

String

 | 

Product type. The options are as follows:

-   **0**: consumable
-   **1**: non-consumable

-   **2**: auto-renewable subscription
-   **3**: non-renewable subscription

 |
| 

quantity

 | 

No

 | 

Long

 | 

Number of purchased products. This parameter applies only to batch purchase of consumables and non-renewable subscriptions.

CAUTION:

If the **quantity** parameter is used to support bulk purchases of products, your app needs to verify that the ordered quantity matches the final delivered quantity to prevent under-deliveries or over-deliveries.

**Atomic service API**: This API can be used in atomic services since API version 5.0.3(15).

**Start version**: 5.0.3(15)

 |
| 

purchaseTime

 | 

Yes

 | 

Long

 | 

Time when a product is purchased. The value is a UTC timestamp, in milliseconds.

If the purchase is not complete, this parameter is left empty.

 |
| 

finishStatus

 | 

No

 | 

String

 | 

Delivery status. The options are as follows:

-   **1**: delivered
-   **2**: not delivered

 |
| 

needFinish

 | 

No

 | 

Boolean

 | 

Indicates whether it is a must to acknowledge the delivery to complete the purchase. The options are as follows:

-   **true**: The delivery must be acknowledged to complete the purchase.
-   **false**: Acknowledging the delivery to complete the purchase is optional.

 |
| 

price

 | 

Yes

 | 

Long

 | 

Price, in cents.

 |
| 

currency

 | 

Yes

 | 

String

 | 

Currency. For details, please refer to the [ISO 4217](https://www.iso.org/iso-4217-currency-codes.html) standard. For example, CNY, USD, and MYR.

 |
| 

developerPayload

 | 

No

 | 

String

 | 

Information stored on the merchant side, which an app passes when calling the payment API.

 |
| 

purchaseOrderRevocationReasonCode

 | 

No

 | 

String

 | 

Reason for revoking an order.

-   **0**: other reasons
-   **1**: refund when a user encounters a problem

 |
| 

revocationTime

 | 

No

 | 

Long

 | 

Time when an order is revoked. The value is a UTC timestamp, in milliseconds.

 |
| 

offerTypeCode

 | 

No

 | 

String

 | 

Offer type.

-   **1**: introductory offers for new users
-   **2**: promotional offers for specific user groups
-   **4**: win-back offers for at-risk users

 |
| 

offerId

 | 

No

 | 

String

 | 

Offer ID.

 |
| 

countryCode

 | 

Yes

 | 

String

 | 

Country or region code, which is used to identify a country or region. The value must comply with the [ISO 3166](https://www.iso.org/iso-3166-country-codes.html) standard.

 |
| 

signedTime

 | 

Yes

 | 

Long

 | 

Time when signing is performed. The value is a UTC timestamp, in milliseconds.

 |
| 

**Parameters returned only for subscriptions:**

 |
| 

subGroupGenerationId

 | 

Yes

 | 

String

 | 

Subscription group generation ID.

-   When a user switches from one subscription to another, the ID remains unchanged.
-   If a subscription expires and exceeds the [account hold period](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/iap-subscription-functions#section1656191811315), the ID will change when the user repurchases the product.

 |
| 

subscriptionId

 | 

Yes

 | 

String

 | 

Subscription ID. The ID will change when:

-   A user switches from one subscription to another.
-   A user re-purchases a subscription when it expires and exceeds the [account hold period](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/iap-subscription-functions#section1656191811315).

 |
| 

subGroupId

 | 

Yes

 | 

String

 | 

Subscription group ID.

 |
| 

duration

 | 

Yes

 | 

String

 | 

Validity period after a purchase. The value is in ISO 8601 format. For example, **P1W** indicates a week and **P1M** indicates a month.

 |
| 

durationTypeCode

 | 

Yes

 | 

String

 | 

Type of a subscription cycle.

-   **0**: normal
-   **1**: extended

 |

#### PurchaseReservedInfo

Additional information for a purchase promotion.

| 
Parameter

 | 

Mandatory

 | 

Type

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

productItem

 | 

Yes

 | 

ProductItem

 | 

Product information.

 |
| 

offerInfo

 | 

Yes

 | 

OfferInfo

 | 

Offer parameters.

 |

#### ProductItem

Product information.

| 
Parameter

 | 

Mandatory

 | 

Type

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

applicationId

 | 

Yes

 | 

String

 | 

App ID. For details about how to obtain the app ID, please refer to [Configuring App Identity Information](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/iap-config-app-identity-info).

 |
| 

productId

 | 

Yes

 | 

String

 | 

Product ID.

 |

#### OfferInfo

Offer parameters.

| 
Parameter

 | 

Mandatory

 | 

Type

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

offerId

 | 

Yes

 | 

String

 | 

Offer ID. This ID is the same as that specified during promotion settings when you configure product information in AppGallery Connect. For details, please refer to [Setting Promotional Prices](https://developer.huawei.com/consumer/en/doc/app/set-0000001931995712).

 |
| 

applicationUserName

 | 

No

 | 

String

 | 

Obfuscated string that serves as a unique identifier for each user account. This parameter can be passed in the scenario where the offer ID is passed.

 |
| 

nonce

 | 

Yes

 | 

String

 | 

A unique, lowercase UUID generated by yourself and guaranteed to be system-wide unique.

 |
