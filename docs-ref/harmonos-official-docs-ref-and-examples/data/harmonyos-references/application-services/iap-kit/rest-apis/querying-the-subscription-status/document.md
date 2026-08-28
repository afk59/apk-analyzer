# Querying the Subscription Status

#### Function

This API is used to query the latest status of an auto-renewable subscription.

#### Scenario

After receiving a key event notification from the IAP server, your app server calls this API to obtain the latest subscription status.

#### Prototype

<table><tbody><tr><th class="firstcol" id="mcps1.3.3.2.1.3.1.1" valign="top" width="20%"><p>Protocol</p></th><td class="cellrowborder" valign="top" width="80%"><p>HTTPS POST</p></td></tr><tr><th class="firstcol" id="mcps1.3.3.2.1.3.2.1" valign="top" width="20%"><p>Direction</p></th><td class="cellrowborder" valign="top" width="80%"><p>Your server -&gt; IAP server</p></td></tr><tr><th class="firstcol" id="mcps1.3.3.2.1.3.3.1" valign="top" width="20%"><p>URL</p></th><td class="cellrowborder" valign="top" width="80%"><p>{rootUrl}/subscription/harmony/v1/application/subscription/status/query</p><div class="note"><span class="notetitle">NOTE:</span><div class="notebody"><p>The value of <strong>rootUrl</strong> varies depending on the site. For details, please refer to <a href="../overview/document.md#section11387155610549">Site Information</a>.</p></div></div></td></tr><tr><th class="firstcol" id="mcps1.3.3.2.1.3.4.1" valign="top" width="20%"><p>Data Format</p></th><td class="cellrowborder" valign="top" width="80%"><p>Request: Content-Type: application/json; charset=UTF-8</p><p>Response: Content-Type: application/json;charset=UTF-8</p></td></tr></tbody></table>

#### Request Parameters

## Request Header

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

Content-Type

 | 

Yes

 | 

String

 | 

Content type. The value is **application/json;charset=UTF-8**.

 |
| 

Authorization

 | 

Yes

 | 

String

 | 

Authentication information. JWT is used for authentication. For details, please refer to [Authorization Description](../generating-a-token-for-a-server-side-api-call/document.md#section11166125713715).

 |

## Request Body

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

Purchase token of a product, which you can obtain from the information returned after a purchase or an order query. The value contains a maximum of 256 characters.

 |

#### Request Example

For more detailed sample code or sample code in other programming languages, see **[IAP Kit-Sample-ServerDemo](https://gitcode.com/HarmonyOS_Samples/iapkit-sample-serverdemo/blob/Java/README_en.md)**.

POST /subscription/harmony/v1/application/subscription/status/query
Content-Type: application/json;charset=UTF-8
Authorization: Bearer \*\*\*.\*\*\*.\*\*\*
Accept: application/json
{
  "purchaseToken": "\*\*\*.\*.\*\*\*",
  "purchaseOrderId": "\*\*\*.\*\*\*"
}

#### Response Parameters

## Response Header

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

Content-Type

 | 

Yes

 | 

String

 | 

Content type. The value is **application/json;charset=UTF-8**.

 |

## Response Body

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

responseCode

 | 

Yes

 | 

String

 | 

Result code.

-   **0**: success
-   Other values: failure. Please refer to [REST API Result Codes](../rest-api-result-codes/document.md).

 |
| 

responseMessage

 | 

No

 | 

String

 | 

Result message.

 |
| 

jwsSubGroupStatus

 | 

Yes

 | 

String

 | 

Data in JWS format that contains subscription status information. Follow the instructions in [Verifying the Signature in the Returned Result](../verifying-the-signature-in-the-returned-result/document.md) to decode and perform signature verification for the returned result to obtain subscription status information in JSON format. Check the parameters in the JSON string in [SubGroupStatusPayload](#section149821246171719).

 |

## SubGroupStatusPayload

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

applicationId

 | 

Yes

 | 

String

 | 

App ID.

 |
| 

packageName

 | 

Yes

 | 

String

 | 

App package name.

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

lastSubscriptionStatus

 | 

No

 | 

Object

 | 

Final subscription status ([SubscriptionStatus](#section9100101211811)) within a subscription group. For example, if a user switches from subscription A to B and then to C, this parameter indicates the status of subscription C.

 |
| 

historySubscriptionStatusList

 | 

No

 | 

List<Object>

 | 

List of recent active subscription statuses ([SubscriptionStatus](#section9100101211811)) within a subscription group, sorted in ascending order by the time of subscription switching. The list contains up to 10 valid status records.

For example, if subscription A switches to B, and B switches to C, the list will include the three subscription status records for A, B, and C.

 |

## SubscriptionStatus

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

purchaseToken

 | 

Yes

 | 

String

 | 

Purchase token. In a consumable/non-consumable/non-renewable subscription purchase, each purchase token matches a specific order. In a subscription purchase, each purchase token matches a subscription ID. The value contains a maximum of 256 characters.

 |
| 

status

 | 

Yes

 | 

String

 | 

Subscription status.

-   **1**: active
-   **2**: expired
-   **3**: charge attempt
-   **5**: revoked

 |
| 

expiresTime

 | 

Yes

 | 

Long

 | 

Time when a subscription expires. The value is a UTC timestamp, in milliseconds.

 |
| 

lastPurchaseOrder

 | 

No

 | 

Object

 | 

Latest order for a subscription. For details about the included parameters, please refer to [PurchaseOrderPayload](../data-types/document.md#section1950214943118).

 |
| 

recentPurchaseOrderList

 | 

No

 | 

List<Object>

 | 

List of the latest orders for a subscription, including those generated upon renewal balance conversion, and deferral. For details about the included parameters, please refer to [PurchaseOrderPayload](../data-types/document.md#section1950214943118).

 |
| 

renewalInfo

 | 

No

 | 

Object

 | 

Latest future billing plan for a subscription. For details about the included parameters, please refer to [SubRenewalInfo](#section6346140171811).

 |

## SubRenewalInfo

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

nextRenewPeriodProductId

 | 

No

 | 

String

 | 

ID of the product to be purchased on the next billing date.

 |
| 

productId

 | 

Yes

 | 

String

 | 

ID of the product that is currently active.

 |
| 

autoRenewStatusCode

 | 

Yes

 | 

String

 | 

Auto-renewal status.

-   **0**: disabled
-   **1**: enabled

 |
| 

hasInBillingRetryPeriod

 | 

Yes

 | 

Boolean

 | 

Indicates whether the system is still attempting to charge.

-   **true**: yes
-   **false**: no

 |
| 

priceIncreaseStatusCode

 | 

No

 | 

String

 | 

Price increase status code.

-   **1**: A user has not agreed to a price increase.
-   **2**: A user has agreed to a price increase.

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

renewalPrice

 | 

No

 | 

Long

 | 

Price charged on the next billing date, in cents. This parameter is not returned in the subscription cancellation scenario.

 |
| 

currency

 | 

No

 | 

String

 | 

Currency. For details, please refer to the [ISO 4217](https://www.iso.org/iso-4217-currency-codes.html) standard. For example, CNY, USD, and MYR.

 |
| 

renewalTime

 | 

No

 | 

Long

 | 

Time when a renewal happens. The value is a UTC timestamp, in milliseconds.

 |
| 

expirationIntent

 | 

No

 | 

String

 | 

Reason for subscription renewal failure.

-   **1**: canceled by a user
-   **2**: invalid product
-   **3**: invalid contract signing
-   **4**: abnormal fee deduction
-   **5**: price increase rejected by a user
-   **6**: unknown
-   **7**: undelivered subscriptions found

 |

#### Response Example

HTTP/1.2 200 OK
Content-Type: application/json;charset=UTF-8
{
  "responseCode": "0",
  "jwsSubGroupStatus": "\*\*\*"
}

Example of the [SubGroupStatusPayload](#section149821246171719) structure:

{
    "environment": "NORMAL",
    "applicationId": "10\*\*\*58",
    "packageName": "demoApp",
    "subGroupId": "demoSubGroup",
    "lastSubscriptionStatus": {
        "subGroupGenerationId": "c0e5f80732852b92f7111b8b9ed4fbb\*\*\*\*\*\*\*\*\*\*\*\*c842ea854dfa2da67ab9e",
        "subscriptionId": "\*\*\*\*\*\*\*\*\*\*\*\*\*.\*\*\*\*\*\*\*\*.\*\*\*\*",
        "purchaseToken": "\*\*\*.\*.\*\*\*",
        "status": "5",
        "expiresTime": 1721716039363,
        "lastPurchaseOrder": {
            "subGroupGenerationId": "c0e5f80732852b92f7111b8b9ed4fbb\*\*\*\*\*\*\*\*\*\*\*\*c842ea854dfa2da67ab9e",
            "purchaseOrderId": "\*\*\*\*\*\*\*\*\*\*\*\*\*.\*\*\*\*\*\*\*\*.\*\*\*\*",
            "subscriptionId": "\*\*\*\*\*\*\*\*\*\*\*\*\*.\*\*\*\*\*\*\*\*.\*\*\*\*",
            "purchaseToken": "\*\*\*.\*.\*\*\*",
            "applicationId": "10\*\*\*58",
            "productId": "demoProduct",
            "subGroupId": "demoSubGroup",
            "purchaseTime": 1721082441000,
            "duration": "P1W",
            "durationTypeCode": "0",
            "productType": "2",
            "developerPayload": "demoPayload",
            "signedTime": 1721111398533,
            "purchaseOrderRevocationReasonCode": "1",
            "revocationTime": 1721111240720,
            "offerTypeCode": "1",
            "offerId": "12\*\*56",
            "environment": "NORMAL",
            "countryCode": "CN",
            "price": 880,
            "currency": "SGD",
            "finishStatus": "1"
        },
        "recentPurchaseOrderList": \[
            {
                "subGroupGenerationId": "c0e5f80732852b92f7111b8b9ed4fbb\*\*\*\*\*\*\*\*\*\*\*\*c842ea854dfa2da67ab9e",
                "purchaseOrderId": "\*\*\*\*\*\*\*\*\*\*\*\*\*.\*\*\*\*\*\*\*\*.\*\*\*\*",
                "subscriptionId": "\*\*\*\*\*\*\*\*\*\*\*\*\*.\*\*\*\*\*\*\*\*.\*\*\*\*",
                "purchaseToken": "\*\*\*.\*.\*\*\*",
                "applicationId": "10\*\*\*58",
                "productId": "demoProduct",
                "subGroupId": "demoSubGroup",
                "purchaseTime": 1721082441000,
                "duration": "P1W",
                "durationTypeCode": "0",
                "productType": "2",
                "developerPayload": "demoPayload",
                "signedTime": 1721111398533,
                "purchaseOrderRevocationReasonCode": "1",
                "revocationTime": 1721111240720,
                "offerTypeCode": "1",
                "offerId": "12\*\*56",
                "environment": "NORMAL",
                "countryCode": "CN",
                "price": 880,
                "currency": "SGD",
                "finishStatus": "1"
            }
        \],
        "renewalInfo": {
            "subGroupGenerationId": "c0e5f80732852b92f7111b8b9ed4fbb\*\*\*\*\*\*\*\*\*\*\*\*c842ea854dfa2da67ab9e",
            "productId": "demoProduct",
            "autoRenewStatusCode": "0",
            "hasInBillingRetryPeriod": false,
            "environment": "NORMAL"
        }
    },
    "historySubscriptionStatusList": \[
        {
            "subGroupGenerationId": "c0e5f80732852b92f7111b8b9ed4fbb\*\*\*\*\*\*\*\*\*\*\*\*c842ea854dfa2da67ab9e",
            "subscriptionId": "\*\*\*\*\*\*\*\*\*\*\*\*\*.\*\*\*\*\*\*\*\*.\*\*\*\*",
            "purchaseToken": "\*\*\*.\*.\*\*\*",
            "status": "5",
            "expiresTime": 1721716039363,
            "lastPurchaseOrder": {
                "subGroupGenerationId": "c0e5f80732852b92f7111b8b9ed4fbb\*\*\*\*\*\*\*\*\*\*\*\*c842ea854dfa2da67ab9e",
                "purchaseOrderId": "\*\*\*\*\*\*\*\*\*\*\*\*\*.\*\*\*\*\*\*\*\*.\*\*\*\*",
                "subscriptionId": "\*\*\*\*\*\*\*\*\*\*\*\*\*.\*\*\*\*\*\*\*\*.\*\*\*\*",
                "purchaseToken": "\*\*\*.\*.\*\*\*",
                "applicationId": "10\*\*\*58",
                "productId": "demoProduct",
                "subGroupId": "demoSubGroup",
                "purchaseTime": 1721082441000,
                "duration": "P1W",
                "durationTypeCode": "0",
                "productType": "2",
                "developerPayload": "demoPayload",
                "signedTime": 1721111398533,
                "purchaseOrderRevocationReasonCode": "1",
                "revocationTime": 1721111240720,
                "offerTypeCode": "1",
                "offerId": "12\*\*56",
                "environment": "NORMAL",
                "countryCode": "CN",
                "price": 880,
                "currency": "SGD",
                "finishStatus": "1"
            },
            "recentPurchaseOrderList": \[
                {
                    "subGroupGenerationId": "c0e5f80732852b92f7111b8b9ed4fbb\*\*\*\*\*\*\*\*\*\*\*\*c842ea854dfa2da67ab9e",
                    "purchaseOrderId": "\*\*\*\*\*\*\*\*\*\*\*\*\*.\*\*\*\*\*\*\*\*.\*\*\*\*",
                    "subscriptionId": "\*\*\*\*\*\*\*\*\*\*\*\*\*.\*\*\*\*\*\*\*\*.\*\*\*\*",
                    "purchaseToken": "\*\*\*.\*.\*\*\*",
                    "applicationId": "10\*\*\*58",
                    "productId": "demoProduct",
                    "subGroupId": "demoSubGroup",
                    "purchaseTime": 1721082441000,
                    "duration": "P1W",
                    "durationTypeCode": "0",
                    "productType": "2",
                    "developerPayload": "demoPayload",
                    "signedTime": 1721111398533,
                    "purchaseOrderRevocationReasonCode": "1",
                    "revocationTime": 1721111240720,
                    "offerTypeCode": "1",
                    "offerId": "12\*\*56",
                    "environment": "NORMAL",
                    "countryCode": "CN",
                    "price": 880,
                    "currency": "SGD",
                    "finishStatus": "1"
                }
            \],
            "renewalInfo": {
                "subGroupGenerationId": "c0e5f80732852b92f7111b8b9ed4fbb\*\*\*\*\*\*\*\*\*\*\*\*c842ea854dfa2da67ab9e",
                "productId": "demoProduct",
                "autoRenewStatusCode": "0",
                "hasInBillingRetryPeriod": false,
                "environment": "NORMAL"
            }
        }
    \]
}
