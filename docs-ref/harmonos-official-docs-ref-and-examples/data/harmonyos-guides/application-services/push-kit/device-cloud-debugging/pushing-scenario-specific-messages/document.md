# Pushing Scenario-Specific Messages

#### Use Cases

Push Kit allows your app to connect to the cloud side using HTTPS, send scenario-specific messages using scenario-specific messaging V3 APIs, and define different values of **push-type** for different scenarios.

The following table lists different scenario-specific message types.

| 
push-type

 | 

Message Type

 |
| :-- | :-- |
| 

0

 | 

Alert message (notification message)

 |
| 

1

 | 

Widget update message (not supported for wearables and TVs)

 |
| 

2

 | 

Text-to-speech message (not supported for TVs)

 |
| 

6

 | 

Background message

 |
| 

7

 | 

Live view message (not supported for wearables, TVs, and PCs/2-in-1 devices)

 |
| 

9

 | 

Location message (not supported for wearables and TVs)

 |
| 

10

 | 

In-app call messages (not supported for wearables, TVs, and PCs/2-in-1 devices)

 |

For details about scenario-specific messages, please refer to [REST API - Scenario-Specific Message API](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-rest-api-scenes).

#### Development Procedure

1.  Send a request from your server to obtain a JWT. For details, please refer to [Generating a JWT Based on a Service Account](../generating-a-jwt-based-on-a-service-account/document.md).
2.  Call the API provided by Push Kit to push scenario-specific messages from your app server. For details, please refer to [REST API - Scenario-Specific Message API](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-rest-api-scenes).
    
    **URL for calling the API using HTTPS POST:**
    
    POST https://push-api.cloud.huawei.com/v3/**\[projectId\]**/messages:send
    
    **\[projectId\]**: Replace it with your project ID. To obtain the project ID, sign in to [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html), click **Development and services**, find and click your project in the project list, and go to **Project settings**.
    
    **Request header example:**
    
    Content-Type: application/json
    Authorization: Bearer eyJr\*\*\*\*\*OiIx---\*\*\*\*.eyJh\*\*\*\*\*iJodHR--\*\*\*.QRod\*\*\*\*\*4Gp---\*\*\*\*
    **push-type: 0**
    
    -   The value of the **Authorization** parameter in the request header is the value **Bearer** combined with the JWT obtained in the [previous step for generating a JWT from a service account online](../generating-a-jwt-based-on-a-service-account/document.md).
    -   The **push-type** parameter in the request header indicates the scenario-specific message type. The value **0** indicates Alert messages (including notification messages ).
    
    **Message body example:**
    
    {
      "payload": {
        **"notification": {**
          "category": "MARKETING",
          "title": "Common notification title",
          "body": "Common notification body",
          "clickAction": {
            "actionType": 0
          },
          "notifyId": 12345
        **}**
      },
      "target": {
        "token": \["MAMzLg\*\*\*\*\*\*\*\*\*\*lPW"\]
      },
      "pushOptions": {
        "testMessage": true
      }
    }
    
    -   You can check more [request examples of scenario-specific messages](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-scenariozed-api-request-example).
    -   You are advised to test functions before code development using a debugging tool, such as Postman.
    
3.  (Optimal) Receive the message receipt from Push Kit on your app server. For details, please refer to [(Optional) Developing the Message Receipt](../optional-developing-the-message-receipt/document.md).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/DwmRcpA4SIGA_M73dEBdvg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062117Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B298E8C718C81947347B05C9748FCD1C7EC7FF31F3EE404D1F5BC67D662B1315)

Push Kit provides Java-based server-side sample code for your reference (including obtaining a JWT and sending a notification message or widget update message). For details, please refer to [Sample Code](https://gitcode.com/HarmonyOS_Samples/push-kit_-sample-code_-server-demo_-java).

#### Pushing a Notification Message Online in AppGallery Connect

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/31GjDwY2TFiDr-NJvVrCqQ/notice_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062117Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0B30C535852A6BE77A798DC5F87FB1AA536F5938ABB81C0DE569944B87F0B01F)

**Currently, only alert notification messages support this function.**

1.  Sign in to [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html), click **Development and services**, click the desired project, and go to the **Project settings** page.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/1C10dOuhRP6LjGpJMVoGbQ/en-us_image_0000002504927183.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062117Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0EFFF288BEDE96A270C875CFB5BAF4C9D7ED196ED3D108D687E2A98046756CD1 "Click to enlarge")
    
2.  Find and click your project. Then go to **Grow** > **Push Kit** > **Notifications (V3 Beta)**. Click **Add notification** to create a push task.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/d8BDgEQaTHO8WZketkSuRw/en-us_image_0000002402305765.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062117Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0751DC5CCA2C645C292A8CAD7D3C9389F5FA8FED4C09E57EFF35DC693499B71B "Click to enlarge")
    
3.  Set task parameters. The following uses an alert notification message as an example.
    
    -   **Configuring the push task**
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/jn8oqzgFRguKPonlwTFS1w/en-us_image_0000002368705932.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062117Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DA756FBB7D7A0E00ED91BDF89A050021F256B6E0227789506F006AB871214DEB "Click to enlarge")
        
        | 
        Parameter
        
         | 
        
        Description
        
         |
        | :-- | :-- |
        | 
        
        App
        
         | 
        
        Name of the target app. This parameter is mandatory.
        
         |
        | 
        
        Name
        
         | 
        
        Name used to identify the notification. This parameter is mandatory but will not be displayed to users.
        
         |
        | 
        
        Scenario
        
         | 
        
        Scenario-specific message type. Currently, only the **ALERT** option is supported.
        
         |
        
    
    -   **Configuring push content - General parameters**
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/1IvQwbcbTGq47Xxkp0W9_w/en-us_image_0000002402225633.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062117Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B13BD974FF4F30BD0441803A0D2B0B256117B941A37EFFA2291ABD0E8CFF205D "Click to enlarge")
        
        | 
        Parameter
        
         | 
        
        Description
        
         |
        | :-- | :-- |
        | 
        
        Test message (testMessage)
        
         | 
        
        This parameter is mandatory and maps to the **testMessage** parameter in the corresponding scenario-specific message API.
        
        It indicates whether a message is a test message. The options are as follows:
        
        -   **false**: formal message
        -   **true**: test message (default)
        
         |
        | 
        
        Offline message cache mode (collapseKey)
        
         | 
        
        This parameter is optional and maps to the **collapseKey** parameter in the corresponding scenario-specific message API.
        
        It specifies the offline message cache mode. The value ranges from -1 to 100.
        
        -   **\-1** (default): All offline messages are cached.
        -   **0-100**: message cache group ID. Messages are cached by group. In each group, only the latest message can be cached for each app.
        
         |
        | 
        
        Message cache duration (ttl)
        
         | 
        
        This parameter is optional and maps to the **ttl** parameter in the corresponding scenario-specific message API.
        
        It specifies the message cache duration, in seconds. When a user device is offline, the Push Kit server caches messages. If the user device goes online within the message cache duration, the messages are delivered. Otherwise, the messages are discarded. The default value is **86400** (1 day), and the maximum value is **1296000** (15 days).
        
         |
        | 
        
        Batch task message ID (biTag)
        
         | 
        
        This parameter is optional and maps to the **biTag** parameter in the corresponding scenario-specific message API.
        
        It indicates the tag of a message in a batch delivery task. The tag is returned to the app server when Push Kit sends the [message receipt](../optional-developing-the-message-receipt/document.md). The value contains a maximum of 64 bytes.
        
         |
        | 
        
        Receipt ID (receiptId)
        
         | 
        
        This parameter is optional and maps to the **receiptId** parameter in the corresponding scenario-specific message API.
        
        It specifies the receipt ID that associates with the receipt URL and configuration of the downlink message. For details about how to view the receipt ID, please refer to [Setting Receipt Parameters](../optional-developing-the-message-receipt/document.md#section462935643010).
        
         |
        
    
    -   **Configuring push content - Sending messages to target devices**
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/K-wJB2oPQ7CP4oY6UVyBvA/en-us_image_0000002402305769.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062117Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4E09D3B7A682D93D1EBD5B2F31278E5A6BF3C8EF2CAB845356D17A3925005D35 "Click to enlarge")
        
        | 
        Parameter
        
         | 
        
        Description
        
         |
        | :-- | :-- |
        | 
        
        Device token (token)
        
         | 
        
        This parameter is mandatory and maps to the **token** parameter in the corresponding scenario-specific message API.
        
        It specifies the tokens used to push messages to target users.
        
        **Example: MAMzL\*\*\*\*\*\*\***
        
         |
        
    
    -   **Configuring push content - Content**
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/wimEyH1bSw-JUx81JLB7fg/en-us_image_0000002368705936.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062117Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B3F70573A8F353463946B8BA59E7948BEA70711024359A2F89A2767F6AB19D96 "Click to enlarge")
        
        | 
        Parameter
        
         | 
        
        Description
        
         |
        | :-- | :-- |
        | 
        
        Message type (category)
        
         | 
        
        This parameter is mandatory and maps to the **category** parameter in the corresponding scenario-specific message API.
        
        It specifies the notification message type. To use this parameter, you need to [apply for the notification self-classification permission](../../preparations/applying-for-scenario-specific-message-permissions/document.md#section16708911111611) first. The notification message type affects the message display and notification modes. The options are as follows:
        
        -   **IM**: instant messaging
        -   **VOIP**: voice and video call
        -   **SUBSCRIPTION**: subscription
        -   **TRAVEL**: travel
        -   **HEALTH**: health
        -   **WORK**: work reminder
        -   **ACCOUNT**: account updates
        -   **EXPRESS**: order & logistics
        -   **FINANCE**: finance
        -   **DEVICE\_REMINDER**: device reminder
        -   **MAIL**: email
        -   **MARKETING**: news, content recommendation, social media feeds, product promotion, financial news, life news, survey, function recommendation, and operational activities (only the content is marked but message sending will not be accelerated)
        -   **PLAY\_VOICE**: voice broadcast
        
         |
        | 
        
        Title (title)
        
         | 
        
        This parameter is mandatory and maps to the **title** parameter in the corresponding scenario-specific message API.
        
        It specifies the notification message title.
        
         |
        | 
        
        Content (body)
        
         | 
        
        This parameter is mandatory and maps to the **body** parameter in the corresponding scenario-specific message API.
        
        It specifies the notification message content.
        
         |
        | 
        
        Action (actionType)
        
         | 
        
        This parameter is mandatory and maps to the **actionType** parameter in **clickAction** in the scenario-specific message API.
        
        It specifies the action triggered by a message tap, which can be opening the app home page, opening a custom action page, or opening a custom intentUri page.
        
         |
        
4.  Click **Submit** in the upper right corner of the page to send the message.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/mAo4GotNS0Si3DdofP3YvA/en-us_image_0000002368705924.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062117Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=010B4370A3A4BD65BB600D8496C307C1966CB09E799EB8D961D6B1558D02A2C4)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/cSKJmjDET-qrGPy01OZh0A/notice_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062117Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0D5CA78E6373C7FECAD4278BC6432545CDB5ED7EF0FDCB539E966F6CF2BE6A3D)
    
    The preview effect is for reference only.
