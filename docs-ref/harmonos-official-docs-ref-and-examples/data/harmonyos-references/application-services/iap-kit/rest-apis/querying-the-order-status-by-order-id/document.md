# Querying the Order Status by Order ID

#### Function

This API is used to query the order status information based on an order ID.

#### Scenario

When users have questions about an order, they can seek technical support from the developer using the order ID. The developer can then use this API to query the corresponding order status information.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/ZnULlNyhRUax_3ZPQ4-3uQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062509Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CD45DC647D922B3BC69A16AFF7FF283B27D09E520262E22F07D9E7932608C15A)

This API can be used to query only orders within one year.

This API does not support querying sandbox test orders.

#### Prototype

<table><tbody><tr><th class="firstcol" id="mcps1.3.3.2.1.3.1.1" valign="top" width="20%"><p>Protocol</p></th><td class="cellrowborder" valign="top" width="80%"><p>HTTPS POST</p></td></tr><tr><th class="firstcol" id="mcps1.3.3.2.1.3.2.1" valign="top" width="20%"><p>Direction</p></th><td class="cellrowborder" valign="top" width="80%"><p>Your server -&gt; IAP server</p></td></tr><tr><th class="firstcol" id="mcps1.3.3.2.1.3.3.1" valign="top" width="20%"><p>URL</p></th><td class="cellrowborder" valign="top" width="80%"><p>{rootUrl}/harmony/v1/application/order/lookup</p><div class="note"><span class="notetitle">NOTE:</span><div class="notebody"><p>The value of <strong>rootUrl</strong> varies depending on the site. For details, please refer to <a href="../overview/document.md#section11387155610549">Site Information</a>.</p></div></div></td></tr><tr><th class="firstcol" id="mcps1.3.3.2.1.3.4.1" valign="top" width="20%"><p>Data Format</p></th><td class="cellrowborder" valign="top" width="80%"><p>Request: Content-Type: application/json; charset=UTF-8</p><p>Response: Content-Type: application/json;charset=UTF-8</p></td></tr></tbody></table>

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

orderNo

 | 

Yes

 | 

String

 | 

Order number associated with a specific transaction. Users can find this number on their device by navigating to **Settings** > **HUAWEI ID** > **Payment and purchases** > **Purchase history** and viewing the details of the corresponding order.

 |

#### Request Example

POST /harmony/v1/application/order/lookup
Content-Type: application/json;charset=UTF-8
Authorization: Bearer \*\*\*.\*\*\*.\*\*\*
Accept: application/json
{
  "orderNo": "\*\*\*\*\*\*"
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

orderStatus

 | 

Yes

 | 

Integer

 | 

Indicates whether the order ID in the request is valid.

-   **1**: The order ID is valid and the corresponding order exists.
-   **0**: The order ID is invalid.

 |
| 

jwsPurchaseOrder

 | 

No

 | 

String

 | 

Order status information in JWS format.

Refer to [here](../verifying-the-signature-in-the-returned-result/document.md) to verify the signature. After a successful verification, decode the string to obtain the order status information. To learn more, see [PurchaseOrderPayload](../data-types/document.md#section1950214943118).

 |

#### Response Example

HTTP/1.2 200 OK
Content-Type: application/json;charset=UTF-8
{
  "responseCode": "0",
  "responseMessage": "success",
  "orderStatus": 1,
  "jwsPurchaseOrder": "\*\*\*"
}
