# Key Event Notifications

If you have integrated IAP Kit's order or subscription functionality into your app, you are advised to [configure an address](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/iap-set-necessary-parameters#section22711950153313) in [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html#/) to receive key event notifications from the IAP server. The notification service version can only be v3.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/I_y8DTI1SxSFhccVm-xe3Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062509Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1E0805580639A7C889350C6CFC19E086B4C0C716E9ED187F0C92009F12F8E348)

It is recommended that the address for receiving key event notifications be configured for all apps that provide consumables, non-consumables, auto-renewable subscriptions, and non-renewable subscriptions, in order to deliver better and more timely services for users. Besides, the address must be HTTPS-compliant and have a valid commercial certificate.

#### Function

After a user purchases a consumable, non-consumable, auto-renewable subscription, or non-renewable subscription, the IAP server calls this API to send a key event notification to your app server.

#### Scenario

If [the address for receiving key event notifications](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/iap-set-necessary-parameters#section22711950153313) is configured when you apply for the IAP service in [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html#/) and the notification service version is set to **v3**, the IAP server will call this API to send notifications to the address upon key events that occur when a user purchases a consumable, non-consumable, auto-renewable subscription, or non-renewable subscription.

Key event notifications are sent for consumables/non-consumables/non-renewable subscriptions in the following scenarios:

-   Payment successful.
-   Refund successful.

Scenarios related to auto-renewable subscriptions are as follows:

-   A user successfully purchases an auto-renewable subscription for the first time.
-   An expired subscription is resumed after a successful auto-renewal.
-   A user proactively renews an expired auto-renewable subscription.
-   A user switches from one auto-renewable subscription to another at the same level. If the two subscriptions have the same billing cycle, the new subscription will take effect immediately.
-   A user switches from one auto-renewable subscription to another at the same level. If the two subscriptions have different billing cycles, the new subscription will take effect on the next billing date.
-   A user switches from one auto-renewable subscription to another at a higher level. The subscription takes effect immediately. The remaining balance of the original subscription will be converted into days for the new subscription, extending its validity period.
-   A user switches from one auto-renewable subscription to another at a lower level. The new subscription will take effect on the next billing date.
-   A user proactively cancels an auto-renewable subscription or your app cancels an auto-renewable subscription. In this scenario, the user can still access the services, but no more renewal will happen after this cycle ends.
-   An auto-renewable subscription is successfully renewed.
-   An expired auto-renewable subscription enters the account hold period.

If your app server returns a failure response (the HTTP status code in the response is not **200**), the IAP server will periodically resend the notification about the key event to your app server. It is recommended that your app server return a success response immediately after receiving the notification, to avoid constantly receiving messages from the IAP server.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/6X5iogOjSzKes0euUh-7Nw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062509Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D69B84258EDB4145B89056936BA1962E7DEFCD7CF9B3FE566A8F241DAD4C13A3)

To ensure the reliability of the resending mechanism, the number of notifications resent is likely to be more than expected.

#### Suggestions on Handling Notifications of Key Events

1.  When your app server receives a key event notification from the IAP server, it is recommended that your app server get the purchase token from the notification, request the IAP server to verify the token, get the latest status of the order or subscription associated with the token if the verification is successful, and finally determine whether to entitle the user to the requested product.
2.  A key event notification is triggered when the order or subscription has a status change, and may be delayed due to network latency or other problems. As a result, the order or subscription status obtained according to the notification received by your app server may not be the latest order or subscription status on the IAP server, so it is recommended that your app server take the actual latest order or subscription status obtained from the IAP server, but not just receiving a notification, as the prerequisite for granting entitlements to the user.
3.  After receiving a notification of the **DID\_NEW\_TRANSACTION** type, you are advised to process the service logic according to the flowchart below to deliver requested services.

Recommended logic for handling a key event notification:

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/AaRbicyUTfqHmsLhhyl7AA/en-us_image_0000002446733029.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062509Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2D73341102AD8728641EDFB7DF79542E77C388D40697BB742513182C1DDB4AF4)

1.  The IAP server sends a key order or subscription event notification to your app server.
2.  Your app server gets the purchase token from the received notification.
3.  Your app server calls the [order status query API](../querying-the-order-status-for-a-consumable-non-consumable-or-non-renewable-subsc/document.md) or [subscription status query API](../querying-the-subscription-status/document.md) provided by the IAP server to query the purchase data and signature data.
4.  The IAP server returns the purchase data and its signature data.
5.  Your app server verifies the order or subscription status, and if the status is as expected, requested services will be offered. For consumables, non-consumables, and non-renewable subscriptions, obtain the latest status through the [order status query API](../querying-the-order-status-for-a-consumable-non-consumable-or-non-renewable-subsc/document.md), and then call the [order delivery acknowledgement API](../acknowledging-the-delivery-for-a-consumable-non-consumable-or-non-renewable-subs/document.md) to deliver the product accordingly. Whether to offer a subscription depends on the **status** field in **SubGroupStatusPayload** obtained after the response of the [subscription status query API](../querying-the-subscription-status/document.md) is decoded via JWS. If the value of **status** is **1**, call the [subscription delivery acknowledgement API](../acknowledging-the-delivery-for-a-subscription/document.md) to offer requested services.
6.  Your app server returns the notification handling result to the IAP server.

#### Restrictions

Do not configure an IP address trustlist on your server to restrict Huawei egress IP addresses. Configuring an IP address trustlist is meaningless because it restricts business development without improving security, especially when a more secure JWS signature mechanism is available for the IAP service. You are accountable for any consequence in the case of your breach of this rule.

The callback address of your app server must be configured in [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html#/) before development. The address must support the HTTPS protocol and have a valid commercial certificate. For security purposes, the cipher must support at least one of ECDHE-RSA-AES128-GCM-SHA256, ECDHE-ECDSA-AES128-GCM-SHA256, ECDHE-RSA-AES256-GCM-SHA384, and ECDHE-ECDSA-AES256-GCM-SHA384. Otherwise, notification messages cannot be received properly.

#### Prototype

<table><tbody><tr><th class="firstcol" id="mcps1.3.7.2.1.3.1.1" valign="top" width="20%"><p>Protocol</p></th><td class="cellrowborder" valign="top" width="80%"><p>HTTPS POST</p></td></tr><tr><th class="firstcol" id="mcps1.3.7.2.1.3.2.1" valign="top" width="20%"><p>Direction</p></th><td class="cellrowborder" valign="top" width="80%"><p>IAP server -&gt; Your server</p></td></tr><tr><th class="firstcol" id="mcps1.3.7.2.1.3.3.1" valign="top" width="20%"><p>URL</p></th><td class="cellrowborder" valign="top" width="80%"><p>The URL is configured when you apply for the IAP service.</p></td></tr><tr><th class="firstcol" id="mcps1.3.7.2.1.3.4.1" valign="top" width="20%"><p>Data Format</p></th><td class="cellrowborder" valign="top" width="80%"><p>Request: Content-Type: application/json; charset=UTF-8</p><p>Response: Content-Type: application/json;charset=UTF-8</p></td></tr></tbody></table>

#### Request Parameters

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

jwsNotification

 | 

Yes

 | 

String

 | 

Notification content, which is a character string generated after **NotificationPayload** is signed. For details, please refer to [NotificationPayload](#section6960203212276).

Follow [the instructions](../verifying-the-signature-in-the-returned-result/document.md) to verify the signature for the **NotificationPayload** message body through the JWS signature method.

 |

## NotificationPayload

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

notificationType

 | 

Yes

 | 

String

 | 

Notification type. For details, please refer to [NotificationType](#section161113819282).

 |
| 

notificationSubtype

 | 

No

 | 

String

 | 

Notification subtype. For details, please refer to [NotificationSubtype](#section16254133782813).

 |
| 

notificationRequestId

 | 

Yes

 | 

String

 | 

Unique ID of a notification request.

 |
| 

notificationMetaData

 | 

Yes

 | 

Object

 | 

Notification metadata. For details, please refer to [NotificationMetaData](#section526717832913).

 |
| 

notificationVersion

 | 

Yes

 | 

String

 | 

Notification service version, which is set to **v3**.

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

## NotificationType

| 
Value

 | 

Description

 |
| :-- | :-- |
| 

DID\_NEW\_TRANSACTION

 | 

The order has been purchased, the subscription has been purchased, or the subscription renewal is successful.

 |
| 

DID\_CHANGE\_RENEWAL\_STATUS

 | 

The subscription status changes.

 |
| 

REVOKE

 | 

The order has been refunded, or the subscription has been revoked.

 |
| 

RENEWAL\_TIME\_MODIFIED

 | 

The subscription expiration time is adjusted.

 |
| 

EXPIRE

 | 

The subscription has expired.

 |
| 

TEST

 | 

Server-side test notification, which is sent only when the API for [testing server-side notifications](../testing-server-side-notifications/document.md) is called.

There is no **notificationSubtype** in this scenario.

 |

## NotificationSubtype

| 
Value

 | 

Description

 |
| :-- | :-- |
| 

INITIAL\_BUY

 | 

The consumable/non-consumable/non-renewable subscription purchase is successful.

The first purchase of an auto-renewable subscription is successful.

Notification type: DID\_NEW\_TRANSACTION

 |
| 

DID\_RENEW

 | 

The renewal is successful.

Notification type: DID\_NEW\_TRANSACTION

 |
| 

RESTORE

 | 

A user proactively resumes a subscription, which can renew as expected.

Notification type: DID\_NEW\_TRANSACTION

 |
| 

AUTO\_RENEW\_ENABLED

 | 

The auto-renewal function is enabled.

Notification type: DID\_CHANGE\_RENEWAL\_STATUS

 |
| 

AUTO\_RENEW\_DISABLED

 | 

The auto-renewal function is disabled.

Notification type: DID\_CHANGE\_RENEWAL\_STATUS

 |
| 

DOWNGRADE

 | 

A user chooses to switch to a new subscription at the same level or at a lower level, which takes effect on the next renewal date.

Notification type: DID\_CHANGE\_RENEWAL\_STATUS or DID\_NEW\_TRANSACTION

 |
| 

UPGRADE

 | 

A user chooses to switch to a new subscription at the same level or at a higher level, which takes effect immediately.

Notification type: DID\_NEW\_TRANSACTION

 |
| 

REFUND\_TRANSACTION

 | 

The consumable/non-consumable/non-renewable subscription order is refunded successfully.

The subscription order is refunded successfully.

Notification type: REVOKE

 |
| 

BILLING\_RETRY

 | 

An expired auto-renewable subscription enters the account hold period.

Notification type: EXPIRE

 |
| 

PRICE\_INCREASE

 | 

A user has agreed to a price increase.

Notification type: DID\_CHANGE\_RENEWAL\_STATUS

 |
| 

BILLING\_RECOVERY

 | 

Subscription payment is successful after a retry.

Notification type: DID\_NEW\_TRANSACTION

 |
| 

PRODUCT\_NOT\_FOR\_SALE

 | 

The product does not exist.

Notification type: EXPIRE

 |
| 

APPLICATION\_DELETE\_SUBSCRIPTION\_HOSTING

 | 

If the subscription is revoked successfully, access to its services will be unavailable immediately.

Notification type: REVOKE

 |
| 

RENEWAL\_EXTENDED

 | 

The next subscription renewal date has been successfully postponed.

Notification type: RENEWAL\_TIME\_MODIFIED

 |

## NotificationMetaData

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

type

 | 

Yes

 | 

Integer

 | 

Product type.

-   **0**: consumable
-   **1**: non-consumable
-   **2**: auto-renewable subscription
-   **3**: non-renewable subscription

 |
| 

currentProductId

 | 

No

 | 

String

 | 

ID of the latest valid subscription. This parameter is available only for subscriptions.

 |
| 

subGroupId

 | 

No

 | 

String

 | 

Subscription group ID. This parameter is available only for subscriptions.

 |
| 

subGroupGenerationId

 | 

No

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

No

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

Purchase token of a product, which you can obtain from the information returned after a purchase or a subscription query. The value contains a maximum of 256 characters.

 |
| 

purchaseOrderId

 | 

No

 | 

String

 | 

Order ID of a purchase. When **NotificationType** is set to **DID\_CHANGE\_RENEWAL\_STATUS** and **NotificationSubtype** is set to **DOWNGRADE**, **purchaseOrderId** is not returned.

The value contains a maximum of 256 characters.

 |

#### Request Example

POST /notify/address
Content-Type: application/json;charset=UTF-8
Accept: application/json
{
  "jwsNotification": "\*\*\*"
}

NotificationPayload Example (Consumable/Non-consumable)

{
  "notificationType": "DID\_NEW\_TRANSACTION",
  "notificationSubtype": "INITIAL\_BUY",
  "notificationRequestId": "7f67e39aa72d1a55f36293047f9769c0aa47a467ffb110eaeeeb888def9f9713",
  "notificationMetaData": {
    "environment": "NORMAL",
    "applicationId": "\*\*\*",
    "packageName": "\*\*\*",
    "type": 0,
    "purchaseToken": "\*\*\*.\*.\*\*\*",
    "purchaseOrderId": "\*\*\*.\*\*\*"
  },
  "notificationVersion": "v3",
  "signedTime": 1702607152698
}

NotificationPayload Example (Non-renewable Subscription)

{
  "notificationType": "DID\_NEW\_TRANSACTION",
  "notificationSubtype": "INITIAL\_BUY",
  "notificationRequestId": "7f67e39aa72d1a55f36293047f9769c0aa47a467ffb110eaeeeb888def9f9713",
  "notificationMetaData": {
    "environment": "NORMAL",
    "applicationId": "\*\*\*",
    "packageName": "\*\*\*",
    "type": 3,
    "purchaseToken": "\*\*\*.\*.\*\*\*",
    "purchaseOrderId": "\*\*\*.\*\*\*"
  },
  "notificationVersion": "v3",
  "signedTime": 1702607152698
}

NotificationPayload Example (Auto-renewable Subscription)

{
  "notificationType": "DID\_NEW\_TRANSACTION",
  "notificationSubtype": "INITIAL\_BUY",
  "notificationRequestId": "6d5882d55c8e5136f2348b8e13b4aaad6d0938898b7e5efdc13f7c7130286f8c",
  "notificationMetaData": {
    "environment": "NORMAL",
    "applicationId": "\*\*\*",
    "packageName": "\*\*\*",
    "type": 2,
    "currentProductId": "1701072721154732",
    "subGroupId": "1701072721154732",
    "subGroupGenerationId": "f7967e2439769fbb3c155a50d2cdd6a8cc8f7750cac7bf78b6f5d65c97c34deb",
    "subscriptionId": "1701072722814.ADE66B39.4732",
    "purchaseToken": "\*\*\*.\*.\*\*\*",
    "purchaseOrderId": "\*\*\*.\*\*\*"
  },
  "notificationVersion": "v3",
  "signedTime": 1701072726860
}

#### Response Parameters

The HTTP status code is used to identify whether the IAP server successfully sends a notification to your app server.

-   If the notification is received successfully, your app server will need to give an HTTP 200 OK success status response to the IAP server.
-   Upon a failure to receive the notification, your app server needs to send an HTTP 40X or HTTP 50X message to tell the IAP server to retry. Then, the IAP server will retry multiple times within a period of time.

#### Response Example

HTTP/1.2 200 OK
