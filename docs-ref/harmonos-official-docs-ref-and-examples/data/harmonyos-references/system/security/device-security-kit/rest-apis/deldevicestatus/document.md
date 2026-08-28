# delDeviceStatus

#### Function

Your app server can call this API to delete the device marking status.

#### Scenario

Your app server can call this API to delete the device marking status. After the deletion, the marking becomes invalid on the cloud.

#### Restrictions

None

#### Prototype

<table><tbody><tr><th class="firstcol" id="mcps1.3.4.2.1.3.1.1" valign="top" width="18.740000000000002%"><p><strong>Protocol</strong></p></th><td class="cellrowborder" valign="top" width="81.26%"><p>HTTPS POST</p></td></tr><tr><th class="firstcol" id="mcps1.3.4.2.1.3.2.1" valign="top" width="18.740000000000002%"><p><strong>Direction</strong></p></th><td class="cellrowborder" valign="top" width="81.26%"><p>Your server -&gt; Device Security server</p></td></tr><tr><th class="firstcol" id="mcps1.3.4.2.1.3.3.1" valign="top" width="18.740000000000002%"><p><strong>URL</strong></p></th><td class="cellrowborder" valign="top" width="81.26%"><p>https://connect-api.cloud.huawei.com/api/rms/v1/deviceVerify/delDeviceStatus</p></td></tr><tr><th class="firstcol" id="mcps1.3.4.2.1.3.4.1" valign="top" width="18.740000000000002%"><p><strong>Data Format</strong></p></th><td class="cellrowborder" valign="top" width="81.26%"><p>Request header: Content-Type: application/json;charset=utf-8</p><p>Response: Content-Type: application/json;charset=utf-8</p></td></tr></tbody></table>

#### Request Parameters

**Request Header**

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

No

 | 

String

 | 

Content type. The value is **application/json;charset=utf-8**.

 |
| 

Authorization

 | 

Yes

 | 

String

 | 

Access token generated from a service account.

 |
| 

bundleName

 | 

Yes

 | 

String

 | 

Your app package name.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/QDKpCVXORCGZQpIuoboHhg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062335Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8EAD95F4D9D04B3CC2ACE8CC5B5C5F0D9408D901B0D0BDFBBFD24234AEB2C792)

The value of **Authorization** is **Bearer** followed by a space character and then the obtained authentication information. You can generate a token by referring to [Sample Code](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/devicesecurity-deviceverify-token#section1910053451218).

**Request Body**

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

mode

 | 

Yes

 | 

Int

 | 

Granularity of the device marking status. The options are as follows:

**1**: app-level

**2**: developer-level

 |
| 

deviceToken

 | 

Yes

 | 

String

 | 

Temporary device token obtained through the [getDeviceToken](../../arkts-apis/deviceverify/document.md#section102884586336) API.

 |
| 

transactionId

 | 

No

 | 

String

 | 

Unique transaction ID of an app service, which is used to associate the service context.

 |
| 

timestamp

 | 

Yes

 | 

Long

 | 

UTC time on the app server, in milliseconds.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/8VwmvchFSV2mMOFoyzkUxg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062335Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C583E9AA8C016E922DC0D5403B86197D1C47FC0204E000BE1F6EEC1BB42B6FFB)

When constructing a message body, you need to wrap a data structure around the message body. For details, see the following API call example.

#### Request Example

POST /api/rms/v1/deviceVerify/delDeviceStatus HTTP/1.1
Host: xxx
Authorization: Bearer eyJr\*\*\*\*\*OiIx---\*\*\*\*.eyJh\*\*\*\*\*iJodHR--\*\*\*.QRod\*\*\*\*\*4Gp---\*\*\*\*
bundleName: com.huawei.xxx
Content-Type: application/json;charset=utf-8

{"data":{ "mode":1, "deviceToken":"xxx", "transactionId":"ddc740b9-45bb-424a-bc50-64e8a813acab", "timestamp":1711072205525}}

#### Response Parameters

**Response Body**

| 
**Parameter**

 | 

Mandatory

 | 

Type

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

bundleName

 | 

No

 | 

String

 | 

Package name obtained from a token for your verification.

 |
| 

errorCodes

 | 

Yes

 | 

String

 | 

Result code.

 |

#### Response Example

HTTP/1.1 200 OK
Content-Type: application/json;charset=utf-8

{"bundleName":"xxx","errorCodes":"OK"}

#### Result Codes

For details about the result codes, please refer to [REST API Error Codes](../rest-api-error-codes/document.md).

| 
**Result Code**

 | 

**Description**

 |
| :-- | :-- |
| 

OK

 | 

The request is processed successfully.

 |
| 

NotFound

 | 

No marking record about the device is found. (The device is authenticated successfully but not marked.)

 |
| 

InvalidBundleName

 | 

The package name is missing or invalid.

 |
| 

InvalidDeviceToken

 | 

The device token is missing or invalid.

 |
| 

DeviceTokenExpired

 | 

The device token has expired.

 |
| 

InvalidMode

 | 

The mode is missing or invalid.

 |
| 

InvalidTimeStamp

 | 

The timestamp is missing or invalid.

 |
| 

InternalServerError

 | 

Internal server error.

 |
