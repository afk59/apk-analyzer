# Message Recall

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/OD1v-YvKRQeoA3noB-Z8NA/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062518Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5FA4E814BE88FAC692C61D648BC8F62691E41B47004D2D91C7320677A6406E72)

To ensure network security, Push Kit disabled the TLS 1.0 and TLS 1.1 protocols and unsupported cipher suites for push-related domains on November 30, 2022. After the date, your app is unable to send push messages using the TLS protocol earlier than version 1.2 or unspecified cipher suites.

If your app uses TLS 1.0 or TLS 1.1 to access push-related domains, ensure that the protocol is updated to TLS 1.2 or later.

#### Function

You can call this API to recall sent messages. **Currently, only notification messages and text-to-speech messages can be recalled.** To avoid misinterpretation, "messages" in this section are referring to notification messages and text-to-speech messages.

#### Restrictions

The message body cannot exceed 4096 bytes (excluding push tokens), and the maximum number of push tokens carried at a time cannot exceed 1000 (current system configuration).

#### Prototype

<table><tbody><tr><th class="firstcol" id="mcps1.3.4.2.1.3.1.1" valign="top" width="20%"><p>Protocol</p></th><td class="cellrowborder" valign="top" width="80%"><p>HTTPS POST</p></td></tr><tr><th class="firstcol" id="mcps1.3.4.2.1.3.2.1" valign="top" width="20%"><p>Direction</p></th><td class="cellrowborder" valign="top" width="80%"><p>Your server -&gt; Push Kit server</p></td></tr><tr><th class="firstcol" id="mcps1.3.4.2.1.3.3.1" valign="top" width="20%"><p>URL</p></th><td class="cellrowborder" valign="top" width="80%"><p>https://push-api.cloud.huawei.com/v1/<strong>[clientId]</strong>/messages:revoke</p><div class="note"><span class="notetitle">NOTE:</span><div class="notebody"><p><strong>[clientId]</strong>: Replace it with the client ID of your app. Refer to the <a href="https://developer.huawei.com/consumer/en/doc/app/agc-help-view-app-info-0000002282674569" target="_blank">guide</a> to obtain the ID.</p></div></div></td></tr><tr><th class="firstcol" id="mcps1.3.4.2.1.3.4.1" valign="top" width="20%"><p>Data Format</p></th><td class="cellrowborder" valign="top" width="80%"><p>Request: Content-Type: application/json</p><p>Response: Content-Type: application/json</p></td></tr></tbody></table>

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

Type of the message to be recalled. The options are as follows:

**0**: notification message

**2**: text-to-speech message

 | 

0

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

notifyId

 | 

Yes

 | 

Integer

 | 

**notifyId** contained in message delivery. For details, please refer to [notifyId](../scenario-specific-message/request-body-parameters/document.md#section17371529101117).

 |
| 

token

 | 

Yes

 | 

Array \[String\]

 | 

Push token of the target user when a message is recalled.

Example: "token": \["\*\*\*\*\*\*\*\*\*\*\*\*"\]

NOTICE:

A maximum of 1000 tokens can be carried each time.

 |

#### Request Example

**// Recall messages based on notifyId** **and token.**
{
    "notifyId": 3114932,
    "token": \[
        "pushToken1",
        "pushToken2",
        "pushToken3"
    \]
}

#### Response Parameters

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

Yes

 | 

String

 | 

Request ID.

 |

#### Response Example

**Success response example**:

{ 
    "code": "80000000", 
    "msg": "Success", 
    "requestId": "157\*\*\*\*\*\*\*006" 
}

**Failure response example**:

{ 
    "code": "80100003", 
    "msg": "Illegal payload, The header does not contain valid push-type",
    "requestId": "1690\*\*\*\*\*\*\*1701" 
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

Check the **Authorization** parameter in the HTTP header.

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
| 

503

 | 

Traffic control.

 | 

-   Distribute the sending speed evenly.
-   Spread out push notification delivery to avoid peak sending times.

 |

#### Service Response Codes

## 80000000 Success

**Message**

Success.

**Description**

Sent successfully.

**Possible causes**

Sent successfully.

**Solution**

None.

## 80100001 Some Request Parameters Are Invalid

**Message**

Check Parameter Error.

**Description**

Some request parameters are invalid.

**Possible causes**

Some request parameters are invalid.

**Solution**

Verify the request [parameters](#section6305192417583) as prompted by the response.

## 80100003 Incorrect Message Structure

**Message**

Illegal payload, {errorTips}.

**Description**

Incorrect message structure.

**Possible causes**

Incorrect message structure.

**Solution**

Verify the [request body structure](#section6305192417583) as prompted by the response.

## 80100020 Some Content in Message Structure Is Incorrect

**Message**

Check Parameter Partial Success.

**Description**

Some content in the message structure is incorrect.

**Possible causes**

Some content in the message structure is incorrect.

**Solution**

Verify the parameters in the message structure as prompted by the response.

## 80200001 Authentication Error

**Message**

Authentication Error.

**Description**

OAuth authentication error.

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

## 80300002 Current App Does Not Have Permission to Send Messages

**Message**

No permission to send message to these tmIDs.

**Description**

The current app does not have the permission to send messages.

**Possible causes**

1.  Push Kit has not been enabled.
2.  The **ClientId** is not an app-level client ID.

**Solution**

1.  Sign in to [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html) and verify that Push Kit has been enabled. For details, please refer to [Enabling Push Kit](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/push-config-setting).
2.  Verify that the **ClientId** is an app-level client ID. For details, please refer to the [guide](https://developer.huawei.com/consumer/en/doc/app/agc-help-view-app-info-0000002282674569).

## 80300007 All Tokens Are Invalid

**Message**

All the tokens are invalid.

**Description**

All tokens are invalid.

**Possible causes**

1.  In principle, the tokens of different apps on the same device are different. However, the same tokens may exist by mistake in practice.
2.  The package name and app ID configured for the app on the device are different from those obtained in [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html).
3.  Devices are upgraded from HarmonyOS 4 or earlier (HarmonyOS for short) to HarmonyOS 5 or later (HarmonyOS NEXT for short). As a result, push tokens need to be re-obtained.

**Solution**

Rectify the fault as prompted by the response:

1.  Ensure that no push token of other apps is passed.
2.  Verify that the package name and app ID configured for the app on the device are the same as those obtained in [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html).
3.  After the device OS is upgraded to HarmonyOS NEXT, regenerate the push token and use [request body parameters of the HarmonyOS NEXT version](../scenario-specific-message/request-body-parameters/document.md) to send the message request.
    
    Use the v3 request URL (**https://push-api.cloud.huawei.com/****v3****/_\[projectId\]_/messages:send**) to send the REST API request.
    
    You are advised to call the **getToken()** API upon app launch to check the push token. If the push token of the device changes, report the change to your app server in a timely manner.
    

## 80300010 Number of Tokens in Message Body Is 0 or Exceeds Default Value

**Message**

token count should within {0} and {1}.

**Description**

The number of tokens in the message body is 0 or exceeds the default value.

**Possible causes**

The number of tokens in the message body is 0 or exceeds the default value (**1000**).

**Solution**

Check the number of tokens as prompted by the response. If the number of tokens exceeds the upper limit, send the message for these tokens in batches.

## 80300017 Tokens in Token List Belong to Multiple Apps

**Message**

Token app count should not exceed 1.

**Description**

Tokens in the token list belong to multiple apps.

**Possible causes**

Tokens in the token list are generated by multiple apps.

**Solution**

Verify that the tokens in the token list are generated by the same app.

## 80300028 App Corresponding to the Token Is Different from That Corresponding to the ClientId

**Message**

Token app mismatch with specify app.

**Description**

The app corresponding to the token is different from that corresponding to the **ClientId**.

**Possible causes**

1.  In principle, the tokens of different apps on the same device are different. However, the same tokens may exist by mistake in practice.
2.  The package name and app ID configured for the app on the device are different from those obtained in [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html).

**Solution**

Rectify the fault as prompted by the response:

1.  Ensure that no push token of other apps is passed.
2.  Verify that the package name and app ID configured for the app on the device are the same as those obtained in [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html).

## 80300032 No Permission to Recall Messages

**Message**

No permission to revoke messages.

**Description**

No permission to recall messages.

**Possible causes**

No permission to recall messages.

**Solution**

Recall messages based on both token and **notifyId**.

## 80000001 System Internal Error

**Message**

CommonService Error.

**Description**

System internal error.

**Possible causes**

An unknown error occurred.

**Solution**

[Submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/) for assistance.
