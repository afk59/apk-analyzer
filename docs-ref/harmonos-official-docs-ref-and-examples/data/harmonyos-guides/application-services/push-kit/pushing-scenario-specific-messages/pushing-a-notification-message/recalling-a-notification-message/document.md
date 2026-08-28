# Recalling a Notification Message

If the content of a push notification is incorrect or violates regulations, it may lead to negative consequences such as user complaints or penalties from regulatory authorities. Push Kit offers a message recall function to help reduce the negative effects in such scenarios.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/p6DAsONbRp-hfltGKAeJCA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062116Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=85E8B10A5411D5EC57B6410E81B06DC98F33C88E3A3B0FCB8FAC5F4006E474CB)

-   A push token and the **notifyId** field are required for message recalling.
-   To use the message recall function, ensure that you have set the **notifyId** field when pushing messages.
-   A message can be recalled only in the following status: the message has arrived at the device, or the message has been displayed on the device but the user has not tapped it.
-   Message recall does not change the number displayed on the notification badge.

#### Restrictions

The function of recalling notification messages supports phones, tablets, PCs, 2-in-1 devices, (since 5.1.0(18)) wearables, and (since 5.1.1(19)) TVs.

#### Development Procedure

1.  Push a message by referring to [Development Procedure](../sending-a-notification-message/document.md#section17790171616598) and ensure that the app can receive the message properly.
2.  Call the REST API on your app server to recall the notification message. For details, please refer to [Message Recall](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-msg-revoke). The request example is as follows:
    
    // Request URL 
    POST https://push-api.cloud.huawei.com/v1/**\[clientId\]**/messages:revoke
     
    // Request Header 
    Content-Type:application/json
    Authorization:Bearer eyJr\*\*\*\*\*OiIx---\*\*\*\*.eyJh\*\*\*\*\*iJodHR--\*\*\*.QRod\*\*\*\*\*4Gp---\*\*\*\*
    **push-type: 0** 
     
    // Request Body 
    {
      "notifyId": 1234567,
      "token": \[
        "pushToken1",
        "pushToken2",
        "pushToken3"
      \]
    }
    
    -   **\[clientId\]**: Replace it with the client ID of your app. Refer to the [guide](https://developer.huawei.com/consumer/en/doc/app/agc-help-view-app-info-0000002282674569) to obtain the ID.
    -   **Authorization**: a character string in JWT format. Obtain the value by referring to [Authorization](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-msg-revoke#section7551144075816).
    -   **push-type**: The value **0** indicates the notification message scenario.
    -   **notifyId**: message ID, which uniquely identifies a message. For details, please refer to [notifyId](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-msg-revoke#section166472121113).
    -   **token**: push token. Obtain the token by referring to [Obtaining a Push Token](../../../preparations/obtaining-a-push-token/document.md).
