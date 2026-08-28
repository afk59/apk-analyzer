# (Optional) Developing the Message Receipt

#### Use Cases

After the Push Kit server sends a message to a device, the device will report the message status to the Push Kit server, and the Push Kit server will send the result to your app's receipt server in a message receipt, so you can learn about the status of the delivered message and rectify any possible errors.

Due to the network status and message quantity, the message receipt sending may be delayed after the Push Kit server receives a response from the user device. If the delay is too long, the user device may be offline.

#### Message Receipt Service Development

Develop your receipt server code by referring to [Message Receipt](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-api-msg-receipt). The service API address will be used as the callback address in [Setting Receipt Parameters](#section462935643010).

#### Enabling the Receipt Permission

1.  Sign in to [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html), click **Development and services**, click the desired project, and go to the **Project settings** page.
    
2.  Find and click the desired project in the project list. Then, go to **Grow** > **Push Kit** > **Settings**. On the **Settings** page that is displayed, choose to set the project-level message receipt or app-level message receipt. Note that the URL for receiving the project-level message receipt is valid for all apps in the project. If you set both the project-level and app-level message receipt receiving URLs, the app-level message receipt receiving URL is used first.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/aUOa58BLQBeYeRwAUejNQw/en-us_image_0000002368705916.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062117Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=07019E7E09C420AAEEBBDDE439A3164E39E775861790014C01659B462CC921BC "Click to enlarge")
    
3.  Taking the app-level message receipt configuration as an example. Select an app for which the receipt needs to be set and click **Enable**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/R2sSsMVjT0uR4u4aWC75hQ/en-us_image_0000002402305773.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062117Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AEABEE9F041B176F11A2FE74D4F5FEF9D67490E1DF883B5890E44905F90E29D7 "Click to enlarge")
    
4.  On the **Select receipt** page that is displayed, select an existing receipt or create a receipt.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/XN6XqshLSZ6U9VIHvcTRFA/en-us_image_0000002368546024.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062117Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2C3AF9D1F4138052DC402E9B93DC6D174F75BB73EA4835D7EB41F5FA79FAA8F2 "Click to enlarge")
    

#### Setting Receipt Parameters

Create a receipt and set the parameters in the following figure.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/RmFAbw0dSFekkcrMZiFqJg/en-us_image_0000002368546036.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062117Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3DEE07AFCBCC2465A0A1590B4517862BC2CFDBE34B9446B64261B8D6BB415719)

1.  Set the message receipt name and callback address.
    
    After the callback address is configured, the Push Kit server will check whether the certificate provided by the message receipt server (app server for receiving the message receipt) is issued by a commercial CA.
    
    -   Commercial CA prompt information
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/LpI9AX1kTSSt3I4YqLs6YA/en-us_image_0000002368705908.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062117Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7C2C0DB8E743365E3C7B3ED32C5D681C575162C05B70C968A5A2B1BC6B018579)
        
    -   Self-signed CA prompt information
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/AOsxDX9MQnG-TLUX_8xQoQ/en-us_image_0000002402305753.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062117Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=85CE4442A987BC0F394948DCF66801A5BC8986D0E13F2F251CF8265750495731 "Click to enlarge")
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/wr90FibIRf-Gj6N3moR_SQ/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062117Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A652DBC72D62454862BBA56A4EAE4D3911E486E2785EF689E18FF15F4B1CA327)
        
        If the certificate expires, you will be unable to receive message receipts. So replace the certificate of your message receipt server in time.
        
2.  Configure the callback user name (**userName**, which is optional) and callback key (**secret**, which is optional) for identity verification. The callback key can be automatically generated.
    1.  Obtain **X-HUAWEI-CALLBACK-ID** from the header of the receipt message. An example is as follows:
        
        X-HUAWEI-CALLBACK-ID: 
        timestamp=1563\*\*\*\*\*1261;nonce=a07bfa17-6d82-4b53-a9a2-07c\*\*\*\*\*eef1;value=E4YeO\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*QXF+c=
        
        In the example, **timestamp** indicates the millisecond-level timestamp of the receipt message, **nonce** indicates a random UUID, **value** indicates the signature information, and the signature method is **Base64(HMAC-SHA256(secret, timestamp+nonce+userName))**.
        
    2.  Generate a signature based on **timestamp**, **nonce**, **userName**, and **secret** and compare the signature with the content of **value** for signature verification. You can also click **Generate key** in AppGallery Connect to automatically generate a callback key.
        
        The Java sample code for generating a signature is as follows:
        
        StringBuilder buf = new StringBuilder(); 
        buf.append(timestamp); 
        buf.append(nonce); 
        // Callback user name configured for the message receipt.
        buf.append(userName); 
        // Callback key configured for the message receipt.
        String secret = "your secret"; 
        String signature = ""; 
        try { 
          Mac mac = Mac._getInstance_("HmacSHA256");
          // The receipt key of the earlier version is encrypted using **secret.getBytes(UTF\_8)**, and the receipt key of the new version is encoded using **Base64**.
          SecretKeySpec key = new SecretKeySpec(Base64.getDecoder().decode(secret), "HmacSHA256"); 
          mac.init(key); 
          byte\[\] encodeV = mac.doFinal(buf.toString().getBytes(UTF\_8));  
          signature = Base64._getEncoder_().encodeToString(encodeV); 
        } catch (NoSuchAlgorithmException | InvalidKeyException e) {  
          // Generate error logs.
          ...
        }
        
3.  Set the supported receipt version.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/ZArsmmevSO-wRAl2X-kV-Q/en-us_image_0000002402305761.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062117Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0DB89E11B2DD10D43A207B0704BE0E0315960AEDEED9AB539AFAFAE991CF63D2)
    
    The V1 receipt does not support scenario-specific messages. Use the V2 receipt.
    
4.  Click **Test Receipt** to test the receipt callback address. After completing the test, click **Submit**. The receipt is created.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/dzaS5XVRRQ6Z-QjRh91DlA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062117Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=30372120281FCF50E1B3B6A14B5C49DCB5243864FFF0F84561BBE35B8E768DDD)
    
    -   The Push Kit server interacts with the app server that receives message receipts using HTTPS. The Push Kit server will verify the certificate provided by the app server. Therefore, it is recommended that your app server use a commercial CA-issued HTTPS certificate.
    -   If you have configured the receipt correctly, after you click **Test Receipt**, your receipt server will receive a test message sent by the Push Kit server. The message content is fixed for a receipt version and is used only for test.
    
    **Sample message:**
    
    Message delivery receipt:
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/QczwrE_aRYuqpSiLERvfaQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062117Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=156D3466DE99E1CF7FA97B449D6F9CEC99002B2591E2B5ACE384DDB7A5F0DE55)
    
    All scenario-specific messages except widget update messages support the message delivery receipt.
    
     {
      "statuses": \[
        {
          "biTag": "bi\*\*62",
          "pushType": 0,
          "token": "MsDZmCSyuS+Gd\*\*\*\*\*\*\*\*\*\*\*ZLs8Es",
          "requestId": "169802\*\*1701",
          "appPackageName": "com.\*\*.\*\*",
          "deliveryStatus": {
            "result": 0,
            "timestamp": 1697741455082
          }
        }
      \]
    }
    
    Widget update receipt:
    
    {
      "statuses": \[
        {
          "biTag": "bi\*\*62",
          "pushType": 1,
          "token": "MsDZmCSyuS+Gd\*\*\*\*\*\*\*\*\*\*\*ZLs8Es",
          "requestId": "169802\*\*1701",
          "appPackageName": "com.\*\*.\*\*",
          "formStatus": {
            "formId": 10086,
            "result": 0,
            "timestamp": 1698027152082
          }
        }
      \]
    }
    
    The test is passed only when your message receipt server returns a success response. Then, click **Submit** to complete message receipt creation.
    
    Success response:
    
    { 
         "code": "0", 
         "message": "success" 
     }
    

#### Receipt Status Codes

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/8pumKXxyQPGrY8MQ4x-L5w/notice_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062117Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=60C10E2A3EE5561574CD3716EE47A7B68583C13A9EEE7BF7D8329B4748D3A60B)

Before locating faults based on receipt status codes, check whether the URL of the [message push API](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-scenariozed-api-request-struct) (https://push-api.cloud.huawei.com/**v3**/**\[projectId\]**/messages:send) is correct.

-   Use the message push API URL of the V3 version but not the V1 or V2 version. For details, please refer to [Request URL Version Problem in a Scenario-specific Message](../../faqs/request-url-version-problem-in-a-scenario-specific-message/document.md).
-   Check whether the **projectId** in the push API URL is the same as that of the project to which the current app belongs. If not, update **projectId** in the push API URL, [regenerate a JWT](../generating-a-jwt-based-on-a-service-account/document.md), complete operations in [Obtaining a Push Token](../../preparations/obtaining-a-push-token/document.md) again, and send the message again.

You can collect statistics on received message receipt status codes and make analysis. The following table lists the receipt status codes.

| 
Receipt Status Code

 | 

Description

 | 

Cause and Handling Suggestion

 |
| :-- | :-- | :-- |
| 

0

 | 

The message is delivered successfully.

 | 

N/A

 |
| 

2

 | 

The token is invalid as the app has been uninstalled.

 | 

The app does not exist after the message is successfully sent to the device. The app has been uninstalled in most cases.

 |
| 

5

 | 

The token is not matched.

 | 

The token in the received message is different from the local token. Possible causes are as follows:

-   The user has cleared the local app data.
-   The user has updated the app by uninstallation and reinstallation.
-   You have deleted the local token by calling the pushService.[deleteToken](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-pushservice#section108761115154914)() method from your app.
-   You have called [deleteAAID](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-aaid-api#section4466259194220)() from your app, which deletes the local token together with the AAID.
-   After the device is restored to factory settings, the user relaunches the preloaded app, or reinstalls and launches the non-preloaded app.

The token does not exist in local data storage when the device receives the message. Possible causes are as follows:

-   App not activated.

If the error persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

 |
| 

6

 | 

The notification message is not displayed.

 | 

Possible causes are as follows:

-   The user has disabled the notification function on the device.
-   The user has disabled the notification function of this app.
-   The user has enabled the minor mode.

 |
| 

10

 | 

Inactive device.

 | 

If a device is inactive (that is, the device has been connected to the network for less than 30 days), no message is sent to the device.

 |
| 

14

 | 

Other errors.

 | 

Internal network error.

 |
| 

15

 | 

The message of the offline user is controlled.

 | 

1.  An offline user's message overwriting policy has been set through **collapseKey** in the server API. Based on this policy, the message is overwritten and therefore not delivered to the device.
2.  A maximum of 120 offline messages can be cached. When the upper limit is reached, an upcoming offline message will overwrite the one cached the earliest.

 |
| 

22

 | 

Target users do not match.

 | 

The user to which the push token belongs does not match the local user on the current device. Ensure that the push token used for messaging is the same as that requested for the local user.

NOTICE:

If the local user before accessing PrivateSpace is user A, after PrivateSpace access, the system switches the local user to user B. At this time, if you use the push token requested for user A to send a message, this receipt status code will be returned.

 |
| 

27

 | 

The app process does not exist, and the background message is cached.

 | 

The target app process does not exist on the device. As a result, the background message is cached.

 |
| 

31

 | 

The target app does not have the page that is pointed to.

 | 

Check the **skills** section configuration and the setting of the **clickAction** field in the request body by referring to [Actions to Be Triggered upon Message Tapping](../../pushing-scenario-specific-messages/pushing-a-notification-message/sending-a-notification-message/document.md#section697519219136).

 |
| 

51

 | 

The device is powered on but locked.

 | 

The user restarted the device but did not unlock the screen.

 |
| 

102

 | 

The message is discarded due to frequency control.

 | 

For an app, a maximum of 3000 messages can be pushed to a single device on a daily basis. When the upper limit is reached, no messages can be sent on the same calendar day.

 |
| 

144

 | 

The **profileId** parameter does not exist.

 | 

Check the [profileId](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-scenariozed-api-request-param#section17371529101117) field in the payload of the downlink scenario-specific message.

 |
| 

151

 | 

The push message is not displayed or **formId** of the widget does not exist.

 | 

1.  Ensure that the widget has been added to the home screen of the user device.
2.  Ensure that the [formId](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-scenariozed-api-request-param#section6471174713249) specified in the widget update message exists.

 |
| 

155

 | 

Failed to update the live view.

 | 

Verify that your notification has been created or has not expired.

 |
| 

156

 | 

The live view update messages are out of order.

 | 

The [version](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-scenariozed-api-request-param#section66881469306) field carried in the live view notification message is earlier than the current version. As a result, update fails.

 |
| 

158

 | 

The live view to be created already exists.

 | 

A live view with the same [activityId](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-scenariozed-api-request-param#section66881469306) created using Live View Kit already exists on the device.

 |
| 

188

 | 

Failed to launch the app.

 | 

Please try again later.

 |
| 

191

 | 

Failed to update the badge number.

 | 

The badge number is incorrectly set in the OS.

 |
| 

256

 | 

The message upper limit is reached.

 | 

You can check the details of the [frequency control policy](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-msg-freq-control#section551882820368).

 |
| 

259

 | 

The message is rejected.

 | 

1.  The message contains inappropriate content.
2.  The message contains an insecure URL.

Change the message content or URL.

 |
| 

261

 | 

The widget does not exist.

 | 

The widget update message is not delivered due to control by the Push Kit server (control period: 30 days). Filter out invalid messages. Cause: The widget corresponding to the [formId](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-scenariozed-api-request-param#section6471174713249) in the widget update message does not exist.

Enter an allocated **formId** to avoid that the widget update message cannot be delivered in the control period.

 |
| 

262

 | 

The number of widget updates has reached the upper limit.

 | 

The widget update message is not delivered due to control by the Push Kit server (control period: one day). Filter out invalid messages. Cause: The number of widget update times on the user device has reached the upper limit. (The frequency control limit on the server side is not reached.)

 |
| 

264

 | 

Message not subscribed to.

 | 

A user has not agreed to a subscription, but the subscription message is sent.

 |
| 

265

 | 

The live view update is restricted.

 | 

The live view notification corresponding to an [activityId](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-scenariozed-api-request-param#section66881469306) value does not exist, so live view messages with this **activityId** value are banned from sending for 24 hours.

 |
| 

268

 | 

The **status** field is not passed.

 | 

The [status](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-scenariozed-api-request-param#section66881469306) field is not passed when a live view created through Push Kit is updated.

 |
| 

269

 | 

The live view already exists.

 | 

A live view with the same [activityId](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-scenariozed-api-request-param#section66881469306) created by Push Kit already exists.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/u5r8UBc-RCGgFfuCNe6wbQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062117Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F71921C5732C15823233990E9E0018ABC1F5019656DC75842055D9695E8F605C)

Filter out tokens whose message status is 2, 5, 6, or 10 to reduce messages sent to devices corresponding to these tokens.
