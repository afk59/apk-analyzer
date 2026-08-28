# Querying Orders Related to Specific Purchase Records

#### Function

This API is used to query payment and refund orders within a specified time range.

#### Scenario

For example, if you want to check the payment and refund orders of the previous day, you can set the start time to 00:00 of the previous day and the end time to 00:00 of the current day, and then call this API to query related order records.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/Cgky4AxcT0Kd0z3MTQ49Hw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062509Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2478CC40DB4444D2854DFFD7AA68D0831DD4E3C44035A16CF0F9910E6A5F0971)

-   As daily order information may still be subject to change, it is not recommended to use this API to query real-time order data for the current day. It is recommended to query with a one-day delay.
-   Currently, only order data within 180 days can be queried.
-   Currently, sandbox orders and zero-amount orders cannot be queried.

#### Prototype

<table><tbody><tr><th class="firstcol" id="mcps1.3.3.2.1.3.1.1" valign="top" width="20%"><p>Protocol</p></th><td class="cellrowborder" valign="top" width="80%"><p>HTTPS POST</p></td></tr><tr><th class="firstcol" id="mcps1.3.3.2.1.3.2.1" valign="top" width="20%"><p>Direction</p></th><td class="cellrowborder" valign="top" width="80%"><p>Your server -&gt; IAP server</p></td></tr><tr><th class="firstcol" id="mcps1.3.3.2.1.3.3.1" valign="top" width="20%"><p>URL</p></th><td class="cellrowborder" valign="top" width="80%"><p>{rootUrl}/order/harmony/v1/application/trade/orders/query</p><div class="note"><span class="notetitle">NOTE:</span><div class="notebody"><p>The value of <strong>rootUrl</strong> varies depending on the site. For details, please refer to <a href="../overview/document.md#section11387155610549">Site Information</a>.</p></div></div></td></tr><tr><th class="firstcol" id="mcps1.3.3.2.1.3.4.1" valign="top" width="20%"><p>Data Format</p></th><td class="cellrowborder" valign="top" width="80%"><p>Request: Content-Type: application/json; charset=UTF-8</p><p>Response: Content-Type: application/json;charset=UTF-8</p></td></tr></tbody></table>

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

-   The start time cannot be later than the current time.

 |
| 

endTime

 | 

Yes

 | 

Long

 | 

End time of the query range. The value is a UTC timestamp, in milliseconds.

-   The difference between the start time and end time must be less than or equal to 48 hours.
-   The end time must be later than the start time.

 |
| 

continuationToken

 | 

No

 | 

String

 | 

Data location flag for a query in pagination mode.

-   This parameter is not required for the initial request. If a response includes a **continuationToken**, use the **continuationToken** in the next query to retrieve the next page of data.

 |

#### Request Example

POST /order/harmony/v1/application/trade/orders/query
Content-Type: application/json; charset=UTF-8
Authorization: Bearer \*\*\*.\*\*\*.\*\*\*
Accept: application/json
{
  "startTime": 1739548800000,
  "endTime": 1739721600000
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

orderInfoList

 | 

No

 | 

List<Object>

 | 

List of order information, in JSON format. Each **JSONObject** indicates the information of an order. For details about the order information format, please refer to [OrderInfo](#section58501102185).

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

#### Response Example

HTTP/1.2 200 OK
Content-Type: application/json; charset=UTF-8
{
  "responseCode": "0",
  "orderInfoList": \[
    {
      "requestId": "\*\*\*",
      "country": "CN",
      "merchantId": "\*\*\*",
      "applicationId": "\*\*\*",
      "orderTime": 1739602800000,
      "tradeTime": 1739602800000,
      "productId": "\*\*\*",
      "productName": "test",
      "payMoney": "10.00",
      "couponAmt": "0.10",
      "currency": "CNY",
      "tradeState": 0,
      "tradeType": "REFUND",
      "refundTime": 1739620800000,
      "refundMoney": "0.02"
    },
    {
      "requestId": "\*\*\*",
      "country": "CN",
      "merchantId": "\*\*\*",
      "applicationId": "\*\*\*",
      "orderTime": 1739602800000,
      "tradeTime": 1739602800000,
      "productId": "\*\*\*",
      "productName": "Tested product,"
      "payMoney": "0.01",
      "currency": "CNY",
      "tradeState": 0,
      "tradeType": "PURCHASE"
    },
    // ...
  \],
  "continuationToken": "\*\*\*"
}

## OrderInfo

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

requestId

 | 

Yes

 | 

String

 | 

Purchase order ID associated with a specific transaction, equivalent to **purchaseOrderId**. The value contains a maximum of 256 characters.

 |
| 

country

 | 

Yes

 | 

String

 | 

Country or region code, which is used to identify a country or region. The value must comply with the [ISO 3166](https://www.iso.org/iso-3166-country-codes.html) standard.

 |
| 

merchantId

 | 

Yes

 | 

String

 | 

Merchant ID.

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

orderTime

 | 

Yes

 | 

Long

 | 

Time when an order is placed. The value is a UTC timestamp, in milliseconds.

 |
| 

tradeTime

 | 

Yes

 | 

Long

 | 

Payment time. The value is a UTC timestamp, in milliseconds.

NOTE:

Orders whose **(tradeTime)** is in the range **\[startTime,endTime)** are returned.

 |
| 

productId

 | 

Yes

 | 

String

 | 

Product ID.

 |
| 

productName

 | 

Yes

 | 

String

 | 

Product name.

 |
| 

payMoney

 | 

Yes

 | 

String

 | 

Payment amount, with the currency unit varying based on the user's ordering country.

 |
| 

couponAmt

 | 

No

 | 

String

 | 

Coupon amount, with the currency unit varying based on the user's ordering country.

 |
| 

currency

 | 

Yes

 | 

String

 | 

Currency.

 |
| 

tradeState

 | 

Yes

 | 

Integer

 | 

Order status.

-   **0**: success

 |
| 

tradeType

 | 

Yes

 | 

String

 | 

Transaction type.

-   **PURCHASE**: payment
-   **REFUND**: refund

 |
| 

refundTime

 | 

No

 | 

Long

 | 

Refund time. The value is a UTC timestamp, in milliseconds.

 |
| 

refundMoney

 | 

No

 | 

String

 | 

Refund amount, with the currency unit varying based on the user's ordering country.

 |
