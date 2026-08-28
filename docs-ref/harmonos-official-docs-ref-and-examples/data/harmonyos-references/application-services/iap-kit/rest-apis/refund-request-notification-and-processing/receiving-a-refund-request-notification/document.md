# Receiving a Refund Request Notification

#### Function

When a user applies for a refund, the IAP server calls this API to send a refund review notification to your app server.

#### Scenario

If [the address for receiving key event notifications](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/iap-set-necessary-parameters#section22711950153313) is configured when you apply for the IAP service in [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html) and the notification service version is set to **v3**, the IAP server will call this API to send notifications to the address when users initiate refund requests.

If your app server returns a failure response (the HTTP status code in the response is not **200**), the IAP server will periodically resend the notification about the key event to your app server. It is recommended that your app server return a success response immediately after receiving the notification, to avoid constantly receiving messages from the IAP server.

To ensure the reliability of the resending mechanism, the number of notifications resent is likely to be more than expected.

Recommended logic for handling a key event notification:

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/Xp4h2dk-Saeg_8OZZHxeMQ/en-us_image_0000002446613121.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062510Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B736885B89DFF076979D0042035B9AF3918CA2AAE9642C5B371DCA33C88F0575)

1.  The IAP server sends a key event notification about a refund request.
2.  Upon receiving the notification, the app server retrieves the user's refund request information from the notification and determines how to process the refund request.
3.  The app server sends the refund review result to the IAP server.
4.  If the refund request is approved, the IAP server will process the refund. Otherwise, the process ends.
5.  After a successful refund, the IAP server will send a notification to the app server regarding the order refund or subscription revocation.

#### Restrictions

It is recommended that you do not configure an IP address trustlist on your server to restrict Huawei egress IP addresses. Configuring an IP address trustlist is meaningless because it restricts business development without improving security, especially when a more secure JWS signature mechanism is available for the IAP service. You are accountable for any consequence in the case of your breach of this rule.

To receive key event notifications related to refunds, it is necessary to configure the address for receiving key event notifications in [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html#/). The address must support the HTTPS protocol and have a valid commercial certificate. For security purposes, the cipher must support at least one of ECDHE-RSA-AES128-GCM-SHA256, ECDHE-ECDSA-AES128-GCM-SHA256, ECDHE-RSA-AES256-GCM-SHA384, and ECDHE-ECDSA-AES256-GCM-SHA384. Otherwise, notification messages cannot be received properly.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/Nk94nVqISUWCdAWdqwinAQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062510Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E50617F2C405D2F1330C8810075B44594E451572F6C867041F317A7E50328348)

Refund request event notifications are not supported for sandbox orders. After the user submits a refund request, the IAP service skips the refund review process and completes the refund directly. A refund success event notification (NotificationSubtype: **REFUND\_TRANSACTION**) will then be sent to your server.

#### Prototype

<table><tbody><tr><th class="firstcol" id="mcps1.3.4.2.1.3.1.1" valign="top" width="20%"><p>Protocol</p></th><td class="cellrowborder" valign="top" width="80%"><p>HTTPS POST</p></td></tr><tr><th class="firstcol" id="mcps1.3.4.2.1.3.2.1" valign="top" width="20%"><p>Direction</p></th><td class="cellrowborder" valign="top" width="80%"><p>IAP server -&gt; Your server</p></td></tr><tr><th class="firstcol" id="mcps1.3.4.2.1.3.3.1" valign="top" width="20%"><p>URL</p></th><td class="cellrowborder" valign="top" width="80%"><p>The URL is configured when you apply for the IAP service.</p></td></tr><tr><th class="firstcol" id="mcps1.3.4.2.1.3.4.1" valign="top" width="20%"><p>Data Format</p></th><td class="cellrowborder" valign="top" width="80%"><p>Request: Content-Type: application/json; charset=UTF-8</p><p>Response: Content-Type: application/json;charset=UTF-8</p></td></tr></tbody></table>

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

Follow [the instructions](../../verifying-the-signature-in-the-returned-result/document.md) to verify the signature for the **NotificationPayload** message body through the JWS signature method.

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

Notification type.

-   **REFUND\_REQUEST**: refund review event notification

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

refundRequestData

 | 

Yes

 | 

[RefundRequestData](#section16766126101118)

 | 

Refund request details.

 |

## RefundRequestData

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

refundReason

 | 

Yes

 | 

String

 | 

Reason for a user's refund request.

-   **LEGAL**: unauthorized purchase by a minor
-   **UNINTENDED\_PURCHASE**: accidental purchase or subscription
-   **UNSATISFIED\_WITH\_PURCHASE**: purchased product not functioning properly
-   **FULFILLMENT\_ISSUE**: product not received
-   **OTHER**: others

 |
| 

applyAmount

 | 

Yes

 | 

Long

 | 

Requested refund amount, in fen (RMB).

 |
| 

currency

 | 

Yes

 | 

String

 | 

Currency.

-   **CNY**: RMB.

 |
| 

applyType

 | 

Yes

 | 

Integer

 | 

Request type.

-   **1**: initial request

 |
| 

refundBatchNo

 | 

Yes

 | 

String

 | 

Refund batch number.

 |
| 

refundOrders

 | 

Yes

 | 

List<[RefundOrder](#section5541109181116)\>

 | 

Order IDs under a refund request. Multi-order refund requests are currently supported only within game apps.

 |

## RefundOrder

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

Purchase token. The value contains a maximum of 256 characters.

 |
| 

payAmount

 | 

Yes

 | 

Long

 | 

Actual payment amount of an order, in fen (RMB).

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
  "notificationType": "REFUND\_REQUEST",
  "notificationRequestId": "7f67e39aa72d1a55f36293047f9769c0aa47a467ffb110eaeeeb888def9f9713",
  "notificationMetaData": {
    "environment": "NORMAL",
    "applicationId": "\*\*\*",
    "packageName": "\*\*\*",
    "refundRequestData": {
      "refundReason": "UNINTENDED\_PURCHASE",
      "applyAmount": 1,
      "applyType": 1,
      "refundBatchNo": "\*\*\*",
      "currency": "CNY",
      "refundOrders": \[
        {
          "purchaseOrderId": "\*\*\*",
          "purchaseToken": "\*\*\*",
          "payAmount": 1
        }
      \]
    }
  },
  "notificationVersion": "v3",
  "signedTime": 1741073978222
}

#### Response Parameters

The HTTP status code is used to identify whether the IAP server successfully sends a notification to your app server.

-   If the notification is received successfully, your app server will need to give an HTTP 200 OK success status response to the IAP server.
-   Upon a failure to receive the notification, your app server needs to send an HTTP 40X or HTTP 50X message to tell the IAP server to retry. Then, the IAP server will retry multiple times within a period of time.

#### Response Example

HTTP/1.2 200 OK
