# getDeviceStatus

#### Function

Your app server can call this API to query the device marking status.

#### Scenario

After obtaining a device token, you can call this API to query the device marking status. If a device has not been marked, **Notfound** will be returned.

#### Restrictions

None

#### Prototype

<table><tbody><tr><th class="firstcol" id="mcps1.3.4.2.1.3.1.1" valign="top" width="18.34%"><p><strong>Protocol</strong></p></th><td class="cellrowborder" valign="top" width="81.66%"><p>HTTPS POST</p></td></tr><tr><th class="firstcol" id="mcps1.3.4.2.1.3.2.1" valign="top" width="18.34%"><p><strong>Direction</strong></p></th><td class="cellrowborder" valign="top" width="81.66%"><p>Your server -&gt; Device Security server</p></td></tr><tr><th class="firstcol" id="mcps1.3.4.2.1.3.3.1" valign="top" width="18.34%"><p><strong>URL</strong></p></th><td class="cellrowborder" valign="top" width="81.66%"><p>https://connect-api.cloud.huawei.com/api/rms/v1/deviceVerify/getDeviceStatus</p></td></tr><tr><th class="firstcol" id="mcps1.3.4.2.1.3.4.1" valign="top" width="18.34%"><p><strong>Data Format</strong></p></th><td class="cellrowborder" valign="top" width="81.66%"><p>Request header: Content-Type: application/json;charset=utf-8</p><p>Response: Content-Type: application/json;charset=utf-8</p></td></tr></tbody></table>

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/_O6BjHBGSie8J74GFJAOnw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062335Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=46C3C82BBB6474540B6E956841B2D7C0F91300821086B20ADC74548809CED5C1)

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

Note: Device marking statuses at different granularities are independent of each other.

The developer-level device marking status is shared among all apps of the same developer. For example, after app A of a given developer updates the device marking status, the device marking status queried by app B of this developer will also change accordingly.

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/WGUF7NINSoenCx1CZGNO9A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062335Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DD91E70ED9EC8EBA72260E837E75BA39AA06407D92D7546051E7099E9596560D)

When constructing a message body, you need to wrap a data structure around the message body. For details, see the following API call example.

#### Request Example

POST /api/rms/v1/deviceVerify/getDeviceStatus HTTP/1.1
Host: xxx
Authorization: Bearer eyJr\*\*\*\*\*OiIx---\*\*\*\*.eyJh\*\*\*\*\*iJodHR--\*\*\*.QRod\*\*\*\*\*4Gp---\*\*\*\*
bundleName: com.huawei.xxx
Content-Type: application/json;charset=utf-8

{"data":{ "mode":1, "deviceToken":"xxx", "transactionId":"ddc740b9-45bb-424a-bc50-64e8a813acad", "timestamp":1711072205525}}

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

Package name obtained from a device token for your verification.

 |
| 

bit0

 | 

No

 | 

Boolean

 | 

First bit of the device marking status.

 |
| 

bit1

 | 

No

 | 

Boolean

 | 

Second bit of the device marking status.

 |
| 

lastUpdateTime

 | 

No

 | 

Long

 | 

UTC time when the data was last updated, in milliseconds. All updates in a month are standardized to a common timestamp, which is 00:00 on the first day of the month, for example, the UTC timestamp **1722441600000** (which is **2024-08-01 00:00:00** in standard time).

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

{"bundleName":"xxx","bit0":true,"bit1":false,"lastUpdateTime":1711072206323,"errorCodes":"OK"}

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

InvalidDeviceToken

 | 

The device token is missing or invalid.

 |
| 

InvalidMode

 | 

The mode is missing or invalid.

 |
| 

DeviceTokenExpired

 | 

The device token has expired.

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
| 

InvalidBundleName

 | 

The package name is missing or invalid.

 |
