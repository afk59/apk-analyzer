# Returning the Refund Review Result

#### Function

This API is used to return the refund review result to the IAP server.

#### Scenario

After a user requests a refund, the IAP server will send a refund review notification to your app server. After processing the refund based on the review information, your app server calls this API to inform the IAP server of the refund review result.

#### Prototype

<table><tbody><tr><th class="firstcol" id="mcps1.3.3.2.1.3.1.1" valign="top" width="20%"><p>Protocol</p></th><td class="cellrowborder" valign="top" width="80%"><p>HTTPS POST</p></td></tr><tr><th class="firstcol" id="mcps1.3.3.2.1.3.2.1" valign="top" width="20%"><p>Direction</p></th><td class="cellrowborder" valign="top" width="80%"><p>Your server -&gt; IAP server</p></td></tr><tr><th class="firstcol" id="mcps1.3.3.2.1.3.3.1" valign="top" width="20%"><p>URL</p></th><td class="cellrowborder" valign="top" width="80%"><p>{rootUrl}/post-sales/harmony/v1/transactions/refund/result</p><div class="note"><span class="notetitle">NOTE:</span><div class="notebody"><p>The value of <strong>rootUrl</strong> varies depending on the site. For details, please refer to <a href="../../overview/document.md#section11387155610549">Site Information</a>.</p></div></div></td></tr><tr><th class="firstcol" id="mcps1.3.3.2.1.3.4.1" valign="top" width="20%"><p>Data Format</p></th><td class="cellrowborder" valign="top" width="80%"><p>Request: Content-Type: application/json; charset=UTF-8</p><p>Response: Content-Type: application/json;charset=UTF-8</p></td></tr></tbody></table>

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

Authentication information. JWT is used for authentication. For details, please refer to [Authorization Description](../../generating-a-token-for-a-server-side-api-call/document.md#section11166125713715).

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

reviewType

 | 

Yes

 | 

Integer

 | 

Review result.

-   **1**: approved
-   **2**: rejected

 |
| 

refundBatchNo

 | 

Yes

 | 

String

 | 

Refund work order number or batch number.

 |
| 

remark

 | 

No

 | 

String

 | 

Review result remarks. When the value of **reviewType** is **2**, the rejection reason needs to be returned.

 |
| 

notifyTime

 | 

Yes

 | 

Long

 | 

Notification time, which is a UTC timestamp in milliseconds, representing the number of milliseconds elapsed since January 1, 1970, 00:00 UTC.

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

totalRefundAmount

 | 

No

 | 

Long

 | 

Total refund amount approved, in fen (RMB). This parameter is mandatory when **reviewType** is set to **1**.

 |
| 

currency

 | 

No

 | 

String

 | 

Currency. This parameter is mandatory when **reviewType** is set to **1**.

-   **CNY**: RMB.

 |
| 

reviewResultList

 | 

Yes

 | 

List<[ReviewResult](#section149821246171719)\>

 | 

Order refund details: When you approve a multi-order refund request, the refund amount for each order must be clearly returned. **If the refund of any order is denied, the refund amount for that order should be returned as 0.**

 |

## ReviewResult

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

Order ID, transmitted transparently as provided in the system notification. The value contains a maximum of 256 characters.

 |
| 

payMoney

 | 

Yes

 | 

Long

 | 

Actual payment amount of an order, in fen (RMB).

 |
| 

refundMoney

 | 

Yes

 | 

Long

 | 

Refund amount approved, in fen (RMB).

 |

#### Request Example

POST /post-sales/harmony/v1/transactions/refund/result
Content-Type: application/json;charset=UTF-8
Authorization: Bearer \*\*\*.\*\*\*.\*\*\*
Accept: application/json
{
  "refundBatchNo": "\*\*\*",
  "reviewType": 1,
  "notifyTime": 1741085489609,
  "applicationId": "\*\*\*",
  "totalRefundAmount": 1290,
  "currency": "CNY",
  "reviewResultList": \[
    {
      "purchaseOrderId": "\*\*\*",
      "payMoney": 1290,
      "refundMoney": 1290
    }
  \]
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

returnCode

 | 

Yes

 | 

String

 | 

Result code.

-   **0**: Succeeded.
-   **1**: Incorrect parameter.
-   **990106**: Invalid review type.
-   **990107**: The order ID in the review result does not match that in the refund request.
-   **990109**: For a refund order that exceeds its processing time, review results cannot be sent through the API.
-   **990110**: The refund status is no longer eligible for review.

 |
| 

returnDesc

 | 

Yes

 | 

String

 | 

Result message.

 |
| 

subErrCode

 | 

No

 | 

String

 | 

If **returnCode** is not **0**, this parameter indicates the specific error reason.

-   **211**: Incorrect JWT format.

 |

#### Response Example

HTTP/1.2 200 OK
Content-Type: application/json;charset=UTF-8
{
  "returnCode": "0",
  "returnDesc": "success"
}
