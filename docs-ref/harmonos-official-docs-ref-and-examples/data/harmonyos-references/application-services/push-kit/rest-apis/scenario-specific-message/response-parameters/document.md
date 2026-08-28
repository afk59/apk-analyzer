# Response Parameters

#### Response Body

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

#### Response Examples

**Success response example**:

{ 
    "code": "80000000", 
    "msg": "Success", 
    "requestId": "157\*\*\*\*\*\*\*006" 
}

**Failure response example**:

{ 
    "code": "80100003", 
    "msg": "Illegal payload, badge addNum value ranges from 1 to 99", 
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d/v3/f9x_yFJiTZ66Q5Hg_x0suw/notice_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062518Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5A88F178BC3640471A3F7D1828D66C523401EFF667438CCF7E95E785A6BEFE0E)

Before locating faults based on service response codes, check whether the URL of the [message push API](../request-body-structure/document.md) (https://push-api.cloud.huawei.com/**v3**/**\[projectId\]**/messages:send) is correct.

-   Use the URL of the message push API of the v3 version but not the v1 or v2 version. For details, please refer to [Request URL Version Problem in a Scenario-specific Message](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/push-faq-8).
-   Check whether the **projectId** in the push API URL is the same as that of the project to which the current app belongs. If not, update **projectId** in the push API URL, [regenerate an access token](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/push-jwt-token), [re-obtain the push token](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/push-get-token), and send the message again.

## 80000000 Success

**Message**

Success.

**Description**

Sent successfully.

**Possible causes**

Sent successfully.

**Solution**

None.

## 80100000 Message Failed to Be Sent for Some Tokens

**Message**

Check Parameter Partial Success.

**Description**

The message failed to be sent for some tokens.

**Possible causes**

1.  **noPushTypeRight**: There is no permission on the **push-type** specified in the request header.
2.  **noRight**: The app for which the push token is generated does not belong to the project corresponding to the **projectId** in the request URL.
3.  **atomicUnableSendUnsubscribedMsg**: The atomic service does not support the requested message scenario.
4.  **tokenFormatError**: The token format is incorrect.
5.  **countryNotSupport**: The country/region is not supported.
6.  **tokenPlatformNotSupport**: Third-party proxy tokens are not supported.
7.  **disableSendHuaweiMsgBecauseOfPenalty**: The app is punished for violations.
8.  **differentImgVerifyPolicy**: The value of [push-type](../../image-risk-control/document.md#section13271045101216) used for image risk control is different from that of [push-type](../request-body-structure/document.md#section20573634202313) used in message sending.
9.  **appinfoError**: The app has not been created.
10.  **noRightToSendThisLiveNotificationEvent**: No permission to apply for the required live view scenario.

**Solution**

Rectify the sending failure based on the response, which might be one of the following:

1.  **noPushTypeRight**: Enable the permission on the **push-type** specified in the request header. For details about how to apply for the permission on text-to-speech messages (**push-type** = **2**), please refer to [Applying for the Text-to-Speech Message Permission](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/push-apply-right#section159981112245). For details about how to apply for the permission on in-app call messages (**push-type** = **10**), please refer to [Applying for the In-App Call Message Permission](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/push-apply-right#section7291115452410).
2.  **noRight**: Verify that the app for which the push token is generated belongs to the project corresponding to **projectId** in the request URL. That is, ensure that the value of **projectId** in the request URL (**https://push-api.cloud.huawei.com/v3/_\[projectId\]_/messages:send**) is the same as the project ID of the app in [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html).
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/p95N7Ub-TNOOgvhjJT4U0Q/en-us_image_0000002492833770.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062518Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1EAA73E30ADC3034D3A8DAA58DB92795239E75668D1B30F4BB6574678CA9C3D6 "Click to enlarge")
    
3.  **atomicUnableSendUnsubscribedMsg**: The atomic service can send **only** authorized subscription messages and widget update messages. Verify the message body content.
4.  **tokenFormatError**: Check whether the push token format is correct. If not, [obtain push tokens](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/push-get-token) again.
5.  **countryNotSupport**: [Submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/) for assistance.
6.  **tokenPlatformNotSupport**: [Obtain push tokens](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/push-get-token) again.
7.  **disableSendHuaweiMsgBecauseOfPenalty**: Handle the violations in [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html) and send the message again.
8.  **differentImgVerifyPolicy**: Verify that the value of [push-type](../../image-risk-control/document.md#section13271045101216) used for image risk control is the same as that of [push-type](../request-body-structure/document.md#section20573634202313) used in message sending.
9.  **appinfoError**: Check whether the app has been created in [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html). If so, try again later.
10.  **noRightToSendThisLiveNotificationEvent**: Apply for the required permission by referring to [Applying for the Formal Permission on Live View Kit](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/liveview-formal-authority).

Response example:

{ 
    "code": "80100000", 
    "msg": "{\\"illegalTokens\\":{\\"**tokenFormatError**\\":\[\\"MAAALgE4G98BAAAAst\*\*\*\*\*\*\*jg\\"\]},\\"success\\":1,\\"failure\\":1}", 
    "requestId": "1690\*\*\*\*\*\*\*1701" 
}

## 80100001 Some Request Parameters Are Invalid

**Message**

Check Parameter Error.

**Description**

Some request parameters are invalid.

**Possible causes**

Some request parameters are invalid.

**Solution**

Verify the request [parameters](../request-body-parameters/document.md) as prompted by the response.

## 80100003 Incorrect Message Structure

**Message**

Illegal payload, {errorTips}.

**Description**

Incorrect message structure.

**Possible causes**

Incorrect message structure.

**Solution**

Verify the [request body structure](../request-body-structure/document.md) as prompted by the response.

## 80100004 Message Expiration Time Earlier Than Current Time

**Message**

Illegal expire time.

**Description**

The message expiration time is earlier than the current time.

**Possible causes**

The message expiration time is earlier than the current time.

**Solution**

Verify the setting of the message parameter [ttl](../request-body-parameters/document.md#section418321011212) as prompted by the response.

## 80100022 Signature Verification Not Performed for Images in the Message

**Message**

Anti-Spam: image not verify.

**Description**

Signature verification is not performed for images in the message.

**Possible causes**

Risk check is not performed for images in the message.

**Solution**

Verify that images in the message have passed [risk check](../../image-risk-control/document.md) as prompted by the response.

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
5.  HarmonyOS 5 and later versions no longer support OAuth 2.0-based authentication. Use [JSON Web Tokens (JWTs)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/push-jwt-token) for authentication.

**Solution**

Rectify the authentication failure of the **Authorization** parameter in the request header as prompted by the response.

1.  Verify that the message contains the **Authorization** parameter, and the **Authorization** parameter is not empty.
2.  Verify that the value of **projectId** in the push request URL (**https://push-api.cloud.huawei.com/****v3****/_\[projectId\]_/messages:send**) is the same as the ID of the project to which your app belongs. For details, please refer to step 2 in [Generating a JWT Based on a Service Account](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/push-jwt-token#section16173145352).
3.  Verify that the JWT in the **Authorization** parameter matches the app. For details, please refer to [Generating a JWT Based on a Service Account](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/push-jwt-token).
4.  Use the v3 request URL (**https://push-api.cloud.huawei.com/****v3****/_\[projectId\]_/messages:send**) to send the REST API request.
5.  Generate a [JWT](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/push-jwt-token) and then push the message.

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
2.  Push Kit has been enabled, but the value of **projectId** in the push request URL is different from the ID of the project to which the current app belongs.

**Solution**

1.  Sign in to [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html) and verify that Push Kit has been enabled. For details, please refer to [Enabling Push Kit](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/push-config-setting).
2.  Verify that the value of **projectId** in the push request URL (**https://push-api.cloud.huawei.com/****v3****/_\[projectId\]_/messages:send**) is the same as the ID of the project to which your app belongs. For details, please refer to step 2 in [Generating a JWT Based on a Service Account](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/push-jwt-token#section16173145352).

Ensure that Push Kit has been enabled for the project to which the app belongs, [regenerate an access token](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/push-jwt-token) based on the project, and send the message again.

## 80300007 All Tokens Are Invalid

**Message**

All the tokens are invalid.

**Description**

All tokens are invalid.

**Possible causes**

1.  **noPushTypeRight**: There is no permission on the **push-type** specified in the request header.
2.  **noRight**: The app for which the push token is generated does not belong to the project corresponding to the **projectId** in the request URL. Or the push token is not re-obtained or the request URL version is not updated to V3 after the device OS is upgraded from HarmonyOS 4 or earlier (HarmonyOS for short) to HarmonyOS 5 or later (HarmonyOS NEXT for short).
3.  **atomicUnableSendUnsubscribedMsg**: The atomic service does not support the requested message scenario.
4.  **tokenFormatError**: The token format is incorrect.
5.  **countryNotSupport**: The country/region is not supported.
6.  **tokenPlatformNotSupport**: Third-party proxy tokens are not supported.
7.  **disableSendHuaweiMsgBecauseOfPenalty**: The app is punished for violations.
8.  **differentImgVerifyPolicy**: The value of [push-type](../../image-risk-control/document.md#section13271045101216) used for image risk control is different from that of [push-type](../request-body-structure/document.md#section20573634202313) used in message sending.
9.  **appinfoError**: The app has not been created.
10.  **notSupportPlayVoice**: When a text-to-speech message of the **PLAY\_VOICE** category is pushed, the value of **push-type** in the request header is incorrect.
11.  **noRightToSendThisLiveNotificationEvent**: No permission to apply for the required live view scenario.

**Solution**

Rectify the fault as prompted by the response:

1.  **noPushTypeRight**: Enable the permission on the **push-type** specified in the request header. For details about how to apply for the permission on text-to-speech messages (**push-type** = **2**), please refer to [Applying for the Text-to-Speech Message Permission](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/push-apply-right#section159981112245). For details about how to apply for the permission on in-app call messages (**push-type** = **10**), please refer to [Applying for the In-App Call Message Permission](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/push-apply-right#section7291115452410).
2.  **noRight**: Verify that the app for which the push token is generated belongs to the project corresponding to **projectId** in the request URL. That is, ensure that the value of **projectId** in the request URL (**https://push-api.cloud.huawei.com/v3/_\[projectId\]_/messages:send**) is the same as the project ID of the app in [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html).
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/RCvOp7smS52JFpsdrvt96A/en-us_image_0000002524953707.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062518Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CE98CBCC59FC6F1C5BB7A711D3E89CA1273E1C9328E9D33681A1391C54791EA1 "Click to enlarge")
    
    After the device OS is upgraded to HarmonyOS NEXT, regenerate the push token. (You are advised to call the **getToken()** API upon app launch to check the push token. If the push token of the device changes, report the change to your app server in a timely manner.) Then pass the required [request body parameters](../request-body-parameters/document.md) and use the request URL (**https://push-api.cloud.huawei.com/****v3****/_\[projectId\]_/messages:send**) of the V3 version to send a REST API request.
    
3.  **atomicUnableSendUnsubscribedMsg**: The atomic service can send **only** authorized subscription messages and widget update messages. Verify the message body content.
4.  **tokenFormatError**: Check whether the push token format is correct. If not, [obtain push tokens](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/push-get-token) again.
5.  **countryNotSupport**: [Submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/) for assistance.
6.  **tokenPlatformNotSupport**: [Obtain push tokens](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/push-get-token) again.
7.  **disableSendHuaweiMsgBecauseOfPenalty**: Handle the violations in [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html) and send the message again.
8.  **differentImgVerifyPolicy**: Verify that the value of [push-type](../../image-risk-control/document.md#section13271045101216) used for image risk control is the same as that of [push-type](../request-body-structure/document.md#section20573634202313) used in message sending.
9.  **appinfoError**: Check whether the app has been created in [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html). If so, try again later.
10.  **notSupportPlayVoice**: If an app needs to send a message of the **PLAY\_VOICE** category, the value of **push-type** in the request header must be set to **2**, indicating a text-to-speech message.
11.  **noRightToSendThisLiveNotificationEvent**: Apply for the required permission by referring to [Applying for the Formal Permission on Live View Kit](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/liveview-formal-authority).

Response example:

{
    "code": "80300007",
    "msg": "{\\"failure\\":2,\\"illegalTokens\\":{\\"noRight\\":\[\\"MAAALgE4G98BAAAAst\*\*\*\*\*\*\*jg\\",\\"MAAALgE4G98BAAAAst\*\*\*\*\*\*\*re\\"\]}}",
    "requestId": "1690\*\*\*\*\*\*\*1701"
}

## 80300008 Message Body Size Exceeds 4096 Bytes (Excluding Push Tokens)

**Message**

Push message size is too long.

**Description**

The message body size exceeds 4096 bytes (excluding push tokens).

**Possible causes**

The request message body size exceeds 4096 bytes (excluding push tokens).

**Solution**

Reduce the message body size and send the message again as prompted by the response.

## 80300010 Number of Tokens in Message Body Exceeds Default Value

**Message**

token count should within {0} and {1}.

**Description**

The number of tokens in the message body exceeds the default value.

**Possible causes**

1.  Only one token can be carried each time a widget update message is sent.
2.  In other scenarios, a maximum of 1000 tokens can be carried each time a message is sent.

**Solution**

Reduce the number of tokens each time a message is sent and send the message in different batches, as prompted by the response.

## 80300029 Test Message Sending Frequency Reaches Limit

**Message**

When send test message, the api request exceed limit.

**Description**

The test message sending frequency reaches the limit.

**Possible causes**

Test messages are sent too frequently.

**Solution**

Send test messages again later as prompted by the response.

## 80300030 Number of Tokens Contained in Test Message Exceeds Default Value

**Message**

When send test message, token count exceed limit.

**Description**

The number of tokens contained in a test message exceeds the default value.

**Possible causes**

1.  Only one token can be carried each time a widget update test message is sent.
2.  In other scenarios, a maximum of 10 tokens can be carried each time a test message is sent.

**Solution**

Reduce the number of tokens each time a test message is sent, as prompted by the response.

## 80300036 JWT Validity Period Exceeds One Day

**Message**

JWT expire period over threshold.

**Description**

The validity period of the JWT exceeds one day.

**Possible causes**

The validity period of the JWT exceeds one day.

**Solution**

Regenerate a JWT whose validity period is less than one day as prompted by the response and push the message again.

## 80300037 Message Cannot Be Sent Due to Penalties for Violations

**Message**

Disable send huawei msg because of penalty.

**Description**

The message cannot be sent due to penalties for violations.

**Possible causes**

The message cannot be sent due to penalties for violations.

**Solution**

Handle the violation in [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html) as prompted by the response and then send the message again.

## 81000001 System Internal Error

**Message**

Inner Error.

**Description**

System internal error.

**Possible causes**

An unknown error occurred.

**Solution**

[Submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/) for assistance.
