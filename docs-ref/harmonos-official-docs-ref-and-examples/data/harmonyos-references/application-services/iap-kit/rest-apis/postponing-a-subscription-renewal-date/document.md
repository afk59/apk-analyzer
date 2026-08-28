# Postponing a Subscription Renewal Date

#### Function

This API is used to postpone the next renewal date of an auto-renewable subscription.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/66pBMo3aSi6B5Vr87qjbLQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062509Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0F670EE397336D0F920C147C07C733DF43689404D625FE2DB0E7395607EE23A7)

After you postpone a user's subscription renewal date, it is recommended that you send out emails or in-app notifications to notify the user of the change.

#### Scenario

When you launch some preferential activities within your app, for example, rewarding users with product use duration, you can call this API to postpone the users' next subscription renewal dates. After the renewal date is successfully postponed:

-   The IAP server sends a postponement success notification to your app server.
-   The user can continue to use the paid service and content and will not be charged during the extended period.
-   The system updates the subscription renewal date, and the next billing cycle will begin on the new, postponed expiration date.

#### Restrictions

Subscription renewal date postponements are subject to the following restrictions:

1.  Only subscriptions in active state can be extended. Delaying the renewal date for expired subscriptions is not supported.
2.  Renewal date postponement is not supported for subscriptions during the free trial period.
3.  Each subscription can be postponed a maximum of two times within a 365-day period.
4.  Each API call can postpone the subscription renewal date by 1 to 90 days.

#### Prototype

<table><tbody><tr><th class="firstcol" id="mcps1.3.4.2.1.3.1.1" valign="top" width="20%"><p>Protocol</p></th><td class="cellrowborder" valign="top" width="80%"><p>HTTPS POST</p></td></tr><tr><th class="firstcol" id="mcps1.3.4.2.1.3.2.1" valign="top" width="20%"><p>Direction</p></th><td class="cellrowborder" valign="top" width="80%"><p>Your server -&gt; IAP server</p></td></tr><tr><th class="firstcol" id="mcps1.3.4.2.1.3.3.1" valign="top" width="20%"><p>URL</p></th><td class="cellrowborder" valign="top" width="80%"><p>{rootUrl}/subscription/harmony/v1/application/subscription/renewal/modify</p><div class="note"><span class="notetitle">NOTE:</span><div class="notebody"><p>The value of <strong>rootUrl</strong> varies depending on the site. For details, please refer to <a href="../overview/document.md#section11387155610549">Site Information</a>.</p></div></div></td></tr><tr><th class="firstcol" id="mcps1.3.4.2.1.3.4.1" valign="top" width="20%"><p>Data Format</p></th><td class="cellrowborder" valign="top" width="80%"><p>Request: Content-Type: application/json; charset=UTF-8</p><p>Response: Content-Type: application/json;charset=UTF-8</p></td></tr></tbody></table>

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
| 

requestId

 | 

Yes

 | 

String

 | 

Request ID. It is a unique identifier generated on your side to track each subscription renewal date postponement request.

 |
| 

modifyReason

 | 

Yes

 | 

Integer

 | 

Reasons for subscription date postponement:

-   **0**: free gift
-   **1**: purchase
-   **2**: in-app service issue or service interruptions

 |
| 

extendByDays

 | 

Yes

 | 

Integer

 | 

Number of days the subscription renewal date can be postponed. The value ranges from 1 to 90.

 |

#### Request Example

POST /subscription/harmony/v1/application/subscription/renewal/modify
Content-Type: application/json;charset=UTF-8
Authorization: Bearer \*\*\*.\*\*\*.\*\*\*
Accept: application/json
{
  "purchaseToken": "\*\*\*.\*.\*\*\*",
  "purchaseOrderId": "\*\*\*.\*\*\*",
  "requestId": "\*\*\*\*\*\*",
  "modifyReason": 0,
  "extendByDays": 10
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

newExpirationTime

 | 

Yes

 | 

Long

 | 

Expiration time of the subscription period after the postponement. It is a standard timestamp, for example, 1737354632136.

 |

#### Response Example

HTTP/1.2 200 OK
Content-Type: application/json; charset=UTF-8
Content-Length: 68
{
  "responseCode": "0",
  "newExpirationTime": 1597679570777
}
