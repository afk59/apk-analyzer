# Image Risk Control

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9/v3/R1lSPc9xSm2LMlLUi1FrFg/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062518Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E4C94520917C57C2B1DC370568CBC9184597A8A6C7D7E81B942A8C1860A54EBB)

To ensure network security, Push Kit disabled the TLS 1.0 and TLS 1.1 protocols and unsupported cipher suites for push-related domains on November 30, 2022. After the date, your app is unable to send push messages using the TLS protocol earlier than version 1.2 or unspecified cipher suites.

If your app uses TLS 1.0 or TLS 1.1 to access push-related domains, ensure that the protocol is updated to TLS 1.2 or later.

#### Function

This API is used to check for risks of an image that is to be sent.

#### Restrictions

Each app can make a maximum of 60 API calls per minute.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/3iNd4Vw5Rguw5yT70fxgIQ/notice_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062518Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C6059B4EFBF3B9FA2E630F2E18EDB62397021C8F4974CE1AD6880D8F4CBB4166)

This API is used only for pushing messages. Do not modify images that have passed the image risk check, as this may prevent notification messages from being displayed properly.

#### Prototype

<table><tbody><tr><th align="left" class="firstcol" id="mcps1.3.4.2.1.3.1.1" valign="top" width="17.330000000000002%"><p>Protocol</p></th><td class="cellrowborder" valign="top" width="82.67%"><p>HTTPS POST</p></td></tr><tr><th align="left" class="firstcol" id="mcps1.3.4.2.1.3.2.1" valign="top" width="17.330000000000002%"><p>Direction</p></th><td class="cellrowborder" valign="top" width="82.67%"><p>Your server -&gt; Push Kit server</p></td></tr><tr><th class="firstcol" id="mcps1.3.4.2.1.3.3.1" valign="top" width="17.330000000000002%"><p>URL</p></th><td class="cellrowborder" valign="top" width="82.67%"><p>https://push-api.cloud.huawei.com/v1/<strong>[clientId]</strong>/images:verify</p></td></tr><tr><th class="firstcol" id="mcps1.3.4.2.1.3.4.1" valign="top" width="17.330000000000002%"><p>URL</p></th><td class="cellrowborder" valign="top" width="82.67%"><p>https://push-api.cloud.huawei.com/v2/<strong>[projectId]</strong>/images:verify</p></td></tr><tr><th class="firstcol" id="mcps1.3.4.2.1.3.5.1" valign="top" width="17.330000000000002%"><p>Data Format</p></th><td class="cellrowborder" valign="top" width="82.67%"><p>Request: Content-Type: application/json</p><p>Response: Content-Type: application/json</p></td></tr></tbody></table>

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/8VEcGhidSBOcOyFTZBky4g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062518Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CB80DD66F99AC70DE4F44D4EBE0BA8679FE45A1041F1FFE6A7510249766B5787)

-   In the URL, **\[clientId\]** indicates the OAuth 2.0 client ID (credential). To obtain the client ID, sign in to [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html), click **Development and services**, click the desired project, and go to the **Project settings** page.
-   In the URL, **\[projectId\]** indicates the project ID. To obtain the project ID, sign in to [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html), click **Development and services**, click the desired project, and go to the **Project settings** page.
-   The two URLs point to the same API, but only differ in the authentication mode. You can use either of them.

#### Request Parameters

**Request Header**

| 
Parameter

 | 

Description

 | 

Example

 |
| :-- | :-- | :-- |
| 

Authorization

 | 

Authentication mode:

**JWT**

For details, please refer to [Generating a JWT Based on a Service Account](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/push-jwt-token).

NOTE:

You are advised to set the JWT validity period to 3600 seconds, within which a JWT can be reused.

This parameter value is **Bearer** followed by a space character and then the obtained authentication information.

 | 

Bearer eyJraWQiOiIx---xxx.eyJhdWQiOiJodHR---xxx.QRodgXa2xeXSt4Gp---xxx

 |
| 

push-type

 | 

Message type. The options are as follows:

**0**: sends a notification containing a large icon

**1**: updates the image on a service widget

**2**: sends a text-to-speech message containing a large icon

 | 

1

 |

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

imageUrl

 | 

Yes

 | 

String

 | 

Public URL of an image to be verified. The protocol must be HTTPS.

 |

#### Request Example

{
    "imageUrl": "https://example.com/image.png"
}

#### Response Parameters

**Response Body**

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

Response code.

 |
| 

msg

 | 

Yes

 | 

String

 | 

Response message.

 |
| 

requestId

 | 

No

 | 

String

 | 

Request ID.

 |
| 

downloadUrl

 | 

No

 | 

String

 | 

URL of the image that passes the risk check. (This parameter is returned only when the API call is successful.)

 |
| 

expireTime

 | 

No

 | 

String

 | 

Expiration time of the image risk check, which is a Unix timestamp in seconds. (This parameter is returned only when the API call is successful.)

 |

#### Response Examples

**Success response example**:

{
    "code": "83010000",
    "msg": "Verify success",
    "requestId": "1631\*\*\*\*\*\*\*\*\*\*\*0101",
    "downloadUrl": "https://\*\*.png?verifyKey=MEUCIQDzfYMReU\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*fdCOX9KToGq7o%3D",
    "expireTime": "1689911616"
}

**Failure response example**:

{
    "code": "83010005",
    "msg": "Download picture failed",
    "requestId": "1691\*\*\*\*\*\*\*\*\*\*\*1501"
}

#### HTTP Response Codes

| 
HTTP Response Code

 | 

Description

 | 

Solution

 |
| :-- | :-- | :-- |
| 

200

 | 

Success.

 | 

\-

 |
| 

400

 | 

Invalid parameter.

 | 

Check the service response code and locate the fault accordingly.

 |
| 

401

 | 

Authentication failed.

 | 

Verify the JSON Web Token (JWT) in the **Authorization** parameter in the HTTP request header.

 |
| 

404

 | 

Service not found.

 | 

Verify that the request URI is correct.

 |
| 

500

 | 

Internal service error.

 | 

[Submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/) for assistance.

 |
| 

502

 | 

The connection request is abnormal, generally because the network is unstable.

 | 

Try again later or [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

 |

#### Service Response Codes

## 80100001 Invalid Parameter

**Message**

Check Parameter Error.

**Description**

Invalid parameter.

**Possible causes**

Invalid parameter.

**Solution**

Verify the [request parameters](#section13271045101216) as prompted by the response.

## 80100003 Invalid URL Format

**Message**

only https allow.

**Description**

Invalid URL format.

**Possible causes**

Invalid URL format.

**Solution**

Verify that the setting of **imageUrl** uses the HTTPS protocol as prompted by the response.

## 80200001 Authentication Error

**Message**

Authentication Error.

**Description**

Authentication error.

**Possible causes**

1.  The message does not contain the **Authorization** parameter, or the **Authorization** parameter is left empty.
2.  The project ID used for JWT application is different from that used for sending the message.
3.  The JWT in the **Authorization** parameter does not match the app.
4.  The REST API request is not sent using the v3 request URL.

**Solution**

Rectify the authentication failure of the **Authorization** parameter in the request header as prompted by the response.

1.  Verify that the message contains the **Authorization** parameter, and the **Authorization** parameter is not empty.
2.  Verify that the value of **projectId** in the push request URL (**https://push-api.cloud.huawei.com/****v3****/_\[projectId\]_/messages:send**) is the same as the ID of the project to which your app belongs. For details, please refer to step 2 in [Generating a JWT Based on a Service Account](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/push-jwt-token#section16173145352).
3.  Verify that the JWT in the **Authorization** parameter matches the app. For details, please refer to [Generating a JWT Based on a Service Account](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/push-jwt-token).
4.  Use the v3 request URL (**https://push-api.cloud.huawei.com/****v3****/_\[projectId\]_/messages:send**) to send the REST API request.

Generate a new JWT and then send the message.

## 80200003 OAuth Token Expired

**Message**

Access token expired.

**Description**

OAuth token expired.

**Possible causes**

The access token expired.

**Solution**

Generate a new JWT and then send the message as prompted by the response. For details, please refer to [Generating a JWT Based on a Service Account](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/push-jwt-token).

## 80200005 JWT Expired

**Message**

Jwt token expired.

**Description**

JWT expired.

**Possible causes**

JWT expired.

**Solution**

Generate a new JWT and then send the message as prompted by the response. For details, please refer to [Generating a JWT Based on a Service Account](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/push-jwt-token).

## 80300002 No Permission

**Message**

No permission to send message to these tmIDs.

**Description**

No permission.

**Possible causes**

Push Kit has not been enabled for the project.

**Solution**

[Enable Push Kit](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/push-config-setting) in [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html).

## 83010000 Image Passes Risk Check

**Message**

Verify success.

**Description**

The image passes the risk check.

**Possible causes**

The image passes the risk check.

**Solution**

None.

## 83010001 Image Failed Risk Check

**Message**

Verify failed.

**Description**

The image failed the risk check.

**Possible causes**

The image contains sensitive information.

**Solution**

Modify the image as prompted by the response and perform risk check on the image again.

## 83010002 Traffic Control Threshold Exceeded

**Message**

The number of sent messages exceeds the limit.

**Description**

The request frequency exceeds the traffic control threshold.

**Possible causes**

The request frequency exceeds the traffic control threshold (60 requests per minute per app).

**Solution**

Reduce the request frequency and try again.

## 83010003 Empty Message Body

**Message**

Request body is empty.

**Description**

Empty message body.

**Possible causes**

Empty message body.

**Solution**

Verify the [message body](#section13271045101216) content as prompted by the response.

## 83010004 Risk Check Not Supported

**Message**

Send control is not supported.

**Description**

Risk check is not supported.

**Possible causes**

No risk check policy is matched.

**Solution**

[Submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/) for assistance.

## 83010005 Image Download Failure

**Message**

Download picture failed.

**Description**

Failed to download the image.

**Possible causes**

The image URL in the request body is incorrect.

**Solution**

Verify the image URL in the request body as prompted by the response.

## 83010007 Incorrect Message Type

**Message**

The header does not contain valid push-type.

**Description**

Incorrect message type.

**Possible causes**

Incorrect message type.

**Solution**

Verify [push-type](#section13271045101216) as prompted by the response.
