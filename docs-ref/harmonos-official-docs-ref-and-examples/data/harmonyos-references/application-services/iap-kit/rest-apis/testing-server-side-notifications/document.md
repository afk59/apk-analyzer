# Testing Server-Side Notifications

#### Function

This API is used to test server-side notifications.

#### Scenario

When this API is called, the IAP server sends a test notification to your server.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/8NqeOnlsQPSlEubVXIhBNw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062509Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5FFD338AEB5ACCF4AB4AD0AC0116CBE21EE9776C05A0CCF9161FA8F28A4ADF1D)

1.  Only one call is allowed within a 5-minute window. Once your server receives the test notification, it is not recommended to call this API again.
2.  Test notifications can only be sent to a server in the production environment.
3.  The type for test notifications is TEST, with no sub-type. For details, please refer to [NotificationType](../key-event-notifications/document.md#section161113819282).

#### Prototype

<table><tbody><tr><th class="firstcol" id="mcps1.3.4.1.3.1.1" valign="top" width="20%"><p>Protocol</p></th><td class="cellrowborder" valign="top" width="80%"><p>HTTPS POST</p></td></tr><tr><th class="firstcol" id="mcps1.3.4.1.3.2.1" valign="top" width="20%"><p>Direction</p></th><td class="cellrowborder" valign="top" width="80%"><p>Your server -&gt; IAP server</p></td></tr><tr><th class="firstcol" id="mcps1.3.4.1.3.3.1" valign="top" width="20%"><p>URL</p></th><td class="cellrowborder" valign="top" width="80%"><p>{rootUrl}/harmony/v1/application/notifications/test</p><div class="note"><span class="notetitle">NOTE:</span><div class="notebody"><p>The value of <strong>rootUrl</strong> varies depending on the site. For details, please refer to <a href="../overview/document.md#section11387155610549">Site Information</a>.</p></div></div></td></tr><tr><th class="firstcol" id="mcps1.3.4.1.3.4.1" valign="top" width="20%"><p>Data Format</p></th><td class="cellrowborder" valign="top" width="80%"><p>Request: Content-Type: application/json; charset=UTF-8</p><p>Response: Content-Type: application/json;charset=UTF-8</p></td></tr></tbody></table>

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

#### Request Example

POST /harmony/v1/application/notifications/test
Content-Type: application/json;charset=UTF-8
Authorization: Bearer \*\*\*.\*\*\*.\*\*\*
Accept: application/json

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

testNotificationId

 | 

Yes

 | 

String

 | 

Test notification ID.

 |

#### Response Example

HTTP/1.2 200 OK
Content-Type: application/json;charset=UTF-8
{
  "responseCode": "0",
  "testNotificationId": "\*\*\*"
}

#### Sample Code

{
  "notificationType": "TEST", // The value is fixed at **TEST**.
  "notificationRequestId": "xxx",
  "notificationMetaData": {
    "environment": "NORMAL", // The value is fixed at **NORMAL**.
    "applicationId": "xxx", // App ID.
    "packageName": "testPackageName", // The value is fixed at **testPackageName**.
    "type": 0, // The value is fixed at **0**.
    "purchaseToken": "xxx", // The prefix is fixed at **testPurchaseToken**, followed by the app ID.
    "purchaseOrderId": "xxx" // The prefix is fixed at **testPurchaseOrderId**, followed by the app ID.
  },
  "notificationVersion": "v3", // The value is fixed at **v3**.
  "signedTime": 1747445946282
}
