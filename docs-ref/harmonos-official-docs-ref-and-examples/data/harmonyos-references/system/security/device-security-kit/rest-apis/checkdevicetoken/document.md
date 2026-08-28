# checkDeviceToken

#### Function

Your app server can call this API to check the validity of a device token, ensuring that the device is a real Huawei device.

#### Scenario

After obtaining a device token, you can call this API to check the validity of the device token, ensuring that the device is a real Huawei device.

Differences between this capability and device attestation:

| 
Open Capability

 | 

Description

 |
| :-- | :-- |
| 

Device token check

 | 

This capability is a lightweight implementation of device attestation, which has simple requirements on integration.

This capability cannot defend against replay attacks. In addition, it requires interaction with the Device Security server in each verification, which will lead to service processing delay.

 |
| 

[Device attestation](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/device-attestation-intro)

 | 

In this capability, a public/private key pair is created in the trusted execution environment (TEE) on the device side, and the public key is attested and stored on the app server. This requires you to store the attested public key on the app server and maintain the lifecycle of the public key, posing high requirements on integration.

This capability can defend against replay attacks. Subsequent service requests do not need to interact with the device attestation server, which will not cause significant service processing delay.

 |

You are advised to choose a suitable capability based on your actual security requirements and service scenarios.

#### Restrictions

None

#### Prototype

<table><tbody><tr><th class="firstcol" id="mcps1.3.4.2.1.3.1.1" valign="top" width="18.34%"><p><strong>Protocol</strong></p></th><td class="cellrowborder" valign="top" width="81.66%"><p>HTTPS POST</p></td></tr><tr><th class="firstcol" id="mcps1.3.4.2.1.3.2.1" valign="top" width="18.34%"><p><strong>Direction</strong></p></th><td class="cellrowborder" valign="top" width="81.66%"><p>Your server -&gt; Device Security server</p></td></tr><tr><th class="firstcol" id="mcps1.3.4.2.1.3.3.1" valign="top" width="18.34%"><p><strong>URL</strong></p></th><td class="cellrowborder" valign="top" width="81.66%"><p>https://connect-api.cloud.huawei.com/api/rms/v1/deviceVerify/checkDeviceToken</p></td></tr><tr><th class="firstcol" id="mcps1.3.4.2.1.3.4.1" valign="top" width="18.34%"><p><strong>Data Format</strong></p></th><td class="cellrowborder" valign="top" width="81.66%"><p>Request header: Content-Type: application/json;charset=utf-8</p><p>Response: Content-Type: application/json;charset=utf-8</p></td></tr></tbody></table>

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/W0Fy99oOSNu1FkHhTS6grQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062335Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=498438DF738B5169C6B44B5A067A3EA9BDD464E12CD6302E52200DD38DCE2CA3)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/1YQxMCvIQlS8NQyeAcwR3A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062335Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=70240FB3B3E292DB3F72D99EB7113BAE09C7254C46515A0A42727866B142B69F)

When constructing a message body, you need to wrap a data structure around the message body. For details, see the following API call example.

#### Request Example

post /api/rms/v1/deviceVerify/checkDeviceToken HTTP/1.1
Host: xxx
Authorization: Bearer eyJr\*\*\*\*\*OiIx---\*\*\*\*.eyJh\*\*\*\*\*iJodHR--\*\*\*.QRod\*\*\*\*\*4Gp---\*\*\*\*
bundleName: com.huawei.xxx
Content-Type: application/json;charset=utf-8

{"data":{ "deviceToken":"xxx", "transactionId":"xxx", "timestamp":1704038400}}

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
