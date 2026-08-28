# Acknowledging the Delivery for a Consumable, Non-consumable, or Non-renewable Subscription

#### Function

This API is used to acknowledge that a purchased consumable, non-consumable, or non-renewable subscription has been delivered.

#### Scenario

After receiving a key event notification from the IAP server, your app server calls the [API for querying the order status for a consumable, non-consumable, or non-renewable subscription](../querying-the-order-status-for-a-consumable-non-consumable-or-non-renewable-subsc/document.md) to obtain the latest order status and delivers the product accordingly. For details, please refer to [Order Delivery Guarantee](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/iap-delivering-products#section39601828172114).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/QghHSVYOSt2EdyoPdi3Tbg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062509Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EEDB5F853619C91EABF9FFB520CBAD909FBC5FE394F020CFC07BE0AC792F7A10)

Each purchase order ID (**purchaseOrderId**) can be used for delivery only once. Do not attempt to deliver repeatedly.

#### Prototype

<table><tbody><tr><th class="firstcol" id="mcps1.3.3.2.1.3.1.1" valign="top" width="20%"><p>Protocol</p></th><td class="cellrowborder" valign="top" width="80%"><p>HTTPS POST</p></td></tr><tr><th class="firstcol" id="mcps1.3.3.2.1.3.2.1" valign="top" width="20%"><p>Direction</p></th><td class="cellrowborder" valign="top" width="80%"><p>Your server -&gt; IAP server</p></td></tr><tr><th class="firstcol" id="mcps1.3.3.2.1.3.3.1" valign="top" width="20%"><p>URL</p></th><td class="cellrowborder" valign="top" width="80%"><p>{rootUrl}/order/harmony/v1/application/purchase/shipped/confirm</p><div class="note"><span class="notetitle">NOTE:</span><div class="notebody"><p>The value of <strong>rootUrl</strong> varies depending on the site. For details, please refer to <a href="../overview/document.md#section11387155610549">Site Information</a>.</p></div></div></td></tr><tr><th class="firstcol" id="mcps1.3.3.2.1.3.4.1" valign="top" width="20%"><p>Data Format</p></th><td class="cellrowborder" valign="top" width="80%"><p>Request: Content-Type: application/json; charset=UTF-8</p><p>Response: Content-Type: application/json;charset=UTF-8</p></td></tr></tbody></table>

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

POST /order/harmony/v1/application/purchase/shipped/confirm
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

#### Response Example

HTTP/1.2 200 OK
Content-Type: application/json;charset=UTF-8
{
  "responseCode": "0",
  "responseMessage": "consume success"
}
