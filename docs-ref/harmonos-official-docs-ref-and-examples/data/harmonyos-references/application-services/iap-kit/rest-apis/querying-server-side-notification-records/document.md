# Querying Server-Side Notification Records

#### Function

This API is used to query server-side notification records.

#### Scenario

You can use this API to query server-side notification records, ensuring that no notifications are missed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/pXXGQQanSfSZrAQ9kUppsQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062509Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A2490F2E434A5079BC3647006132FBAC4AACB54F452B5721D44A22DEB654D024)

1.  You can query notification records within the past 30 days.
2.  Notification records in the sandbox cannot be queried.
3.  Only one API call is allowed per second.

#### Prototype

<table><tbody><tr><th class="firstcol" id="mcps1.3.4.1.3.1.1" valign="top" width="20%"><p>Protocol</p></th><td class="cellrowborder" valign="top" width="80%"><p>HTTPS POST</p></td></tr><tr><th class="firstcol" id="mcps1.3.4.1.3.2.1" valign="top" width="20%"><p>Direction</p></th><td class="cellrowborder" valign="top" width="80%"><p>Your server -&gt; IAP server</p></td></tr><tr><th class="firstcol" id="mcps1.3.4.1.3.3.1" valign="top" width="20%"><p>URL</p></th><td class="cellrowborder" valign="top" width="80%"><p>{rootUrl}/harmony/v1/application/notifications/query</p><div class="note"><span class="notetitle">NOTE:</span><div class="notebody"><p>The value of <strong>rootUrl</strong> varies depending on the site. For details, please refer to <a href="../overview/document.md#section11387155610549">Site Information</a>.</p></div></div></td></tr><tr><th class="firstcol" id="mcps1.3.4.1.3.4.1" valign="top" width="20%"><p>Data Format</p></th><td class="cellrowborder" valign="top" width="80%"><p>Request: Content-Type: application/json; charset=UTF-8</p><p>Response: Content-Type: application/json;charset=UTF-8</p></td></tr></tbody></table>

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

startTime

 | 

Yes

 | 

Long

 | 

Start time of the query range. The value is a UTC timestamp, in milliseconds.

NOTE:

-   The start time cannot be later than the current time.
-   The query time range must not exceed the past 30 days.

 |
| 

endTime

 | 

Yes

 | 

Long

 | 

End time of the query range. The value is a UTC timestamp, in milliseconds.

-   The end time cannot be later than the current time.
-   The end time must be later than the start time.

 |
| 

notificationType

 | 

No

 | 

String

 | 

Notification type. If not specified, all notification types will be queried. For details about notification types, please refer to [NotificationType](../key-event-notifications/document.md#section161113819282).

 |
| 

sendResult

 | 

No

 | 

Integer

 | 

Notification sending result. If not specified, both successful and failed records will be queried.

-   **0**: successful
-   **1**: failed

 |
| 

purchaseOrderIdList

 | 

No

 | 

List<String>

 | 

List of purchase order IDs.

 |
| 

continuationToken

 | 

No

 | 

String

 | 

Data location flag for a query in pagination mode.

This parameter is not required for the initial request. If a response includes a **continuationToken**, use the **continuationToken** in the next query to retrieve the next page of data.

 |

#### Request Example

POST /harmony/v1/application/notifications/query
Content-Type: application/json;charset=UTF-8
Authorization: Bearer \*\*\*.\*\*\*.\*\*\*
Accept: application/json
{
  "startTime": 1751299200000,
  "endTime": 1751472000000
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

-   **0**: successful
-   Other values: failed. Please refer to [REST API Result Codes](../rest-api-result-codes/document.md).

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

notificationHistory

 | 

No

 | 

List<Object>

 | 

Notification record. For details, please refer to [NotificationHistory](#section213857922).

 |
| 

continuationToken

 | 

No

 | 

String

 | 

Data location flag for a query in pagination mode. If a **continuationToken** is returned, pass it in the next query to retrieve the next page of data.

 |

#### NotificationHistory

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

Notification content, which is a character string generated after **NotificationPayload** is signed. For details, please refer to [NotificationPayload](../key-event-notifications/document.md#section6960203212276).

Follow [the instructions](../verifying-the-signature-in-the-returned-result/document.md) to verify the signature for the **NotificationPayload** message body through the JWS signature method.

 |
| 

sendResult

 | 

Yes

 | 

Integer

 | 

Notification sending result.

-   **0**: successful
-   **1**: failed

 |

#### Response Example

HTTP/1.2 200 OK
Content-Type: application/json;charset=UTF-8
{
  "responseCode": "0",
  "notificationHistory": \[
    {
      "jwsNotification": "\*\*\*\*",
      "sendResult": 0
    },
    {
      "jwsNotification": "\*\*\*\*",
      "sendResult": 1
    }
  \],
  "continuationToken": "\*\*\*"
}
