# Message Receipt

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/jMlGkrZnRPmhlR3-o_ZiGQ/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062518Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D058B9FD965B3F118F2EAE923504CB3DEBAD9A827176CFBAEEDF615A32BF7664)

To ensure network security, Push Kit disabled the TLS 1.0 and TLS 1.1 protocols and unsupported cipher suites for push-related domains on November 30, 2022. After the date, your app is unable to send push messages using the TLS protocol earlier than version 1.2 or unspecified cipher suites.

If your app uses TLS 1.0 or TLS 1.1 to access push-related domains, ensure that the protocol is updated to TLS 1.2 or later.

#### Function

This API is used by the Push Kit server to send receipts to your server.

#### Restrictions

You need to enable the message receipt function in AppGallery Connect. For details about how to enable the function, please refer to [Enabling the Receipt Permission](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/push-msg-receipt#section86338111648).

The message receipt API has versions V1 and V2. **Only the V2 message receipt API** supports the receipt function for scenario-specific messages.

The scenario-specific message API supported by the **V2 message receipt API** is as follows:

https://push-api.cloud.huawei.com/v3/\[projectId\]/messages:send

#### Prototype

| 
Protocol

 | 

Direction

 | 

URL

 | 

Data Format

 |
| :-- | :-- | :-- | :-- |
| 

HTTPS POST

 | 

Push Kit server -> Your server for receiving receipts

 | 

URL of your server for receiving receipts, which is the same as that you defined in [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html).

 | 

Request: Content-Type: application/json

Response: Content-Type: application/json

 |

#### Request Parameters

## Request Header

| 
Parameter

 | 

Description

 | 

Example

 |
| :-- | :-- | :-- |
| 

X-HUAWEI-CALLBACK-ID

 | 

Message header authentication parameter, which is optional. This parameter is mandatory when both the callback user name and key have been set in the receipt configuration.

 | 

timestamp=1563\*\*\*\*\*1261; nonce=a07bfa17-6d82-4b53-a9a2-07c\*\*\*\*\*eef1; value=E4Ye\*\*\*\*\*HZ6592U8B9S37238E+Hwtjfrmpf8AQXF+c=

-   **timestamp**: timestamp in milliseconds
-   **nonce**: random UUID
-   **value**: Base64-encoded string that has been HMAC-SHA256 encrypted using the callback key. The string before encryption consists of the value of **timestamp**, value of **nonce**, and callback user name, without plus signs (+). For details, please refer to the [sample code](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/push-msg-receipt#li6429181516577).

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

statuses

 | 

Yes

 | 

Array \[[statuses](#section1667405472412) Object \]

 | 

Receipt message content, which is an array of up to 100 [statuses](#section1667405472412) structures. This parameter has versions V1 and V2. Only V2 is supported currently.

 |

#### statuses of V2

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

token

 | 

Yes

 | 

String

 | 

Token of the user to which a message is sent. The token is sent to your app server.

 |
| 

pushType

 | 

Yes

 | 

Integer

 | 

Message type. For details, please refer to [push-type](../scenario-specific-message/request-body-structure/document.md#section20573634202313).

 |
| 

appPackageName

 | 

Yes

 | 

String

 | 

App package name of the message sender.

 |
| 

biTag

 | 

No

 | 

String

 | 

The value is the same as that of **biTag** contained in the message you send. If [biTag](../scenario-specific-message/request-body-parameters/document.md#section418321011212) is not set for sending a notification message, this parameter will be left empty.

 |
| 

requestId

 | 

Yes

 | 

String

 | 

Request ID, which is returned by the message sending API.

 |
| 

deliveryStatus

 | 

No

 | 

[deliveryStatus](#section19136204192210) Object

 | 

Message delivery status ([deliveryStatus](#section19136204192210) structure). This parameter is applicable to receipts for non-widget update messages.

 |
| 

formStatus

 | 

No

 | 

[formStatus](#section72022214244) Object

 | 

Widget update message delivery status ([formStatus](#section72022214244) structure). This parameter is applicable to receipts for widget update messages.

 |

#### deliveryStatus

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

result

 | 

Yes

 | 

Integer

 | 

Receipt status code indicating the message delivery status. For details, please refer to [receipt status codes](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/push-msg-receipt#section19100519195717).

 |
| 

timestamp

 | 

Yes

 | 

Long

 | 

Timestamp when the message successfully arrives at the client, in milliseconds. If the message fails to arrive at the client, the value of this parameter is the timestamp when the receipt message is generated.

 |

#### formStatus

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

formId

 | 

Yes

 | 

Long

 | 

Instance ID of a service widget, which is obtained when [onAddForm](../../../../application-framework/form-kit/arkts-apis/ohos-app-form-formextensionability-formextensionability/document.md#formextensionabilityonaddform) is called (a user adds the widget to the home screen). The maximum value is **2^31-1**.

 |
| 

result

 | 

Yes

 | 

Integer

 | 

Receipt status code indicating the message delivery status. For details, please refer to [receipt status codes](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/push-msg-receipt#section19100519195717).

 |
| 

timestamp

 | 

Yes

 | 

Long

 | 

Timestamp when the message successfully arrives at the client, in milliseconds. If the message fails to arrive at the client, the value of this parameter is the timestamp when the receipt message is generated.

 |

#### Request Example

{
  "statuses": \[
    {
      "biTag": "131415",
      "pushType": 0,
      "appPackageName": "com.\*\*\*\*",
      "token": "148896\*\*\*\*\*\*\*000001",
      "requestId": "1\*\*\*\*\*\*\*0",
      "deliveryStatus":{
        "result": 0,
        "timestamp": 1607832761768
      }
    }
  \]
}

#### Response Parameters

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

code

 | 

Yes

 | 

String

 | 

Processing result code returned by your server.

 |
| 

message

 | 

Yes

 | 

String

 | 

Description of the processing result code returned by your server.

 |

#### Response Example

{
  "code": "0",
  "message": "success"
}
