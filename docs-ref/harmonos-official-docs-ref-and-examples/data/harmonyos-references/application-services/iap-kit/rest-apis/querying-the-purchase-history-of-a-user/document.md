# Querying the Purchase History of a User

#### Function

This API is used to query the purchase history of a user.

#### Scenario

You can call this API to query a user's purchase history to determine whether to display the promotional price to the user, whether the purchased product has been delivered, and more.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/fpeRhedtTi6L0YHshtGyTw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062509Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6DEBDF9A1EB77032DB3C57969D437D776AA59BD1C0E305F2592B27537530DED2)

1.  The purchase history for the past seven years can be queried.
2.  The purchase history in the sandbox cannot be queried.

#### Prototype

<table><tbody><tr><th class="firstcol" id="mcps1.3.3.2.1.3.1.1" valign="top" width="20%"><p>Protocol</p></th><td class="cellrowborder" valign="top" width="80%"><p>HTTPS POST</p></td></tr><tr><th class="firstcol" id="mcps1.3.3.2.1.3.2.1" valign="top" width="20%"><p>Direction</p></th><td class="cellrowborder" valign="top" width="80%"><p>Your server -&gt; IAP server</p></td></tr><tr><th class="firstcol" id="mcps1.3.3.2.1.3.3.1" valign="top" width="20%"><p>URL</p></th><td class="cellrowborder" valign="top" width="80%"><p>{rootUrl}/harmony/v1/application/user/orders/query</p><div class="note"><span class="notetitle">NOTE:</span><div class="notebody"><p>The value of <strong>rootUrl</strong> varies depending on the site. For details, please refer to <a href="../overview/document.md#section11387155610549">Site Information</a>.</p></div></div></td></tr><tr><th class="firstcol" id="mcps1.3.3.2.1.3.4.1" valign="top" width="20%"><p>Data Format</p></th><td class="cellrowborder" valign="top" width="80%"><p>Request: Content-Type: application/json; charset=UTF-8</p><p>Response: Content-Type: application/json;charset=UTF-8</p></td></tr></tbody></table>

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

ID of a purchase order to be queried. The value contains a maximum of 256 characters.

 |
| 

productType

 | 

No

 | 

Integer

 | 

Product type for which the purchase history is queried. The options are as follows:

-   **0**: consumable
-   **1**: non-consumable

-   **2**: auto-renewable subscription
-   **3**: non-renewable subscription

 |
| 

startTime

 | 

No

 | 

Long

 | 

Query start time. The value is a UTC timestamp in milliseconds. If **startTime** is not specified, its value is as follows:

-   If **endTime** is specified, **startTime** is **endTime** minus 365 days.
-   If **endTime** is not specified, **startTime** is the current time minus 365 days.

 |
| 

endTime

 | 

No

 | 

Long

 | 

Query end time. The value is a UTC timestamp in milliseconds. If **endTime** is not specified, its value is as follows:

-   If **startTime** is specified, **endTime** is **startTime** plus 365 days, but not earlier than the current time.
-   If **startTime** is not specified, **endTime** is the current time.

NOTE:

The query time range cannot exceed 365 days.

 |
| 

productIdList

 | 

No

 | 

List<String>

 | 

Product ID for which the purchase history is queried. You can specify a maximum of 10 product IDs.

 |
| 

subGroupIdList

 | 

No

 | 

List<String>

 | 

Subscription group ID for which the purchase history is queried. You can specify a maximum of 10 subscription group IDs.

 |
| 

refunded

 | 

No

 | 

Boolean

 | 

Indicates whether purchase records with refunds are queried. The options are as follows:

-   **true**: Query only purchase records with refunds.
-   **false**: Query only purchase records without refunds.

 |
| 

sort

 | 

No

 | 

String

 | 

Order in which purchase records are returned. The options are as follows:

-   **ASCENDING** (default): Purchase records are returned in ascending order of purchase time, and the earliest record is returned first.
-   **DESCENDING**: Purchase records are returned in descending order of purchase time, and the latest record is returned first.

 |
| 

continuationToken

 | 

No

 | 

String

 | 

Data location flag for a query in pagination mode. A maximum of 10 purchase records can be contained on each page.

-   This parameter is not required for the initial request. If a response includes a **continuationToken**, use the **continuationToken** in the next query to retrieve the next page of data.

 |

#### Request Example

POST /harmony/v1/application/user/orders/query
Content-Type: application/json;charset=UTF-8
Authorization: Bearer \*\*\*.\*\*\*.\*\*\*
Accept: application/json
{
  "purchaseOrderId": "\*\*\*\*\*\*"
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

jwsPurchaseOrderList

 | 

No

 | 

List<String>

 | 

Array of order status information in JWS format.

Refer to [here](../verifying-the-signature-in-the-returned-result/document.md) to verify the signature. After a successful verification, decode the string to obtain the order status information. To learn more, see [PurchaseOrderPayload](../data-types/document.md#section1950214943118).

 |
| 

continuationToken

 | 

No

 | 

String

 | 

Data location flag for a query in pagination mode. If a **continuationToken** is returned, pass the **continuationToken** in the next query to retrieve the next page of data.

 |

#### Response Example

HTTP/1.2 200 OK
Content-Type: application/json;charset=UTF-8
{
  "responseCode": "0",
  "jwsPurchaseOrderList": \["\*\*\*\*","\*\*\*\*","\*\*\*\*","\*\*\*\*"\],
  "continuationToken": "\*\*\*"
}
