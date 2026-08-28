# Getting Started

#### Sample Code

You can refer to the **server-side** [sample code](https://gitcode.com/harmonyos_samples/push-kit_-sample-code_-server-demo_-java) to learn about the process of pushing scenario-specific messages, and refer to the **client-side** [sample code](https://gitcode.com/harmonyos_samples/push-kit-sample-code-clientdemo-arkts) to learn about the functions and processes of generating a push token and receiving a scenario-specific message from Push Kit.

#### Development Process

Follow the steps below (**using [notification message](../pushing-scenario-specific-messages/pushing-a-notification-message/sending-a-notification-message/document.md) as an example**) to develop your app.

| 
No.

 | 

Step

 | 

Description

 |
| :-- | :-- | :-- |
| 

1

 | 

[Enable Push Kit](../preparations/enabling-push-kit/document.md)

 | 

Before developing an app, [enable Push Kit](../preparations/enabling-push-kit/document.md#section13206419341) first. When **configuring the signing information**, use the **manual signing** mode.

[Automatic signing](../../../coding-and-debugging/configuring-a-debug-signature/document.md#section18815157237) is available since DevEco Studio 6.0.0 Beta5.

 |
| 

2

 | 

[Apply for the message self-classification permission](../preparations/applying-for-scenario-specific-message-permissions/document.md#section16708911111611)

 | 

-   Apply for the required scenario-specific message permission according to the [message classification standards](../preparations/applying-for-scenario-specific-message-permissions/document.md#section1924971516101). Each message type has its own message classification standards, notification mode, and [frequency control rules](../preparations/applying-for-scenario-specific-message-permissions/document.md#section1128516504398). If you encounter any problems during the permission application, send an email to [hwpush@huawei.com](mailto:hwpush@huawei.com) to contact us.
-   If you have not enabled the required permission or the permission you have enabled does not match the [category](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-scenariozed-api-request-param#section17371529101117) field contained in the request body of your [REST API call to push scenario-specific messages](../device-cloud-debugging/pushing-scenario-specific-messages/document.md), notification messages are classified into **news and marketing messages** by default. In this case, you are subject to the [restriction](../preparations/applying-for-scenario-specific-message-permissions/document.md#section1128516504398) that each app can push up to 2 or 5 (depending on the app category) messages to each device on a daily basis. When the limit is reached, the device will no longer receive messages from that app on that day.
-   You are advised to set [testMessage](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-scenariozed-api-request-param#section418321011212) to **true** during debugging, so your test messages will not be limited due to [frequency control](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-msg-freq-control).
-   If frequency control is triggered, rectify the fault by referring to the [frequency control FAQ](../faqs/message-frequency-control-problems/document.md).

 |
| 

3

 | 

Obtain a push token on the **client side**

 | 

When calling the [REST API of Push Kit](../device-cloud-debugging/generating-a-jwt-based-on-a-service-account/document.md#section33041381718), you need to set the **token** parameter. For details about the parameter setting, please refer to [Obtaining a Push Token](../preparations/obtaining-a-push-token/document.md#section85173618105). You should pay attention to the [push token change scenario](../preparations/obtaining-a-push-token/document.md#section123091617105820). If the push token of a device changes but the server still uses the outdated push token to call the REST API of Push Kit, the device will not receive the pushed message.

 |
| 

4

 | 

Request notification authorization on the **client side**

 | 

To ensure that devices can receive messages properly, you need to call the [requestEnableNotification](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-notificationmanager#notificationmanagerrequestenablenotification10-1)() method to prompt users to allow notifications before sending messages. For details about the sample code, please refer to step 2 in [Development Procedure](../pushing-scenario-specific-messages/pushing-a-notification-message/sending-a-notification-message/document.md#section17790171616598).

 |
| 

5

 | 

Configure the **skills** section on the **client side**

 | 

Configure the **skills** section to ensure proper redirection upon tapping the message. For details, please refer to [Actions to Be Triggered upon Message Tapping](../pushing-scenario-specific-messages/pushing-a-notification-message/sending-a-notification-message/document.md#section697519219136).

 |
| 

6

 | 

Generate a JWT based on a service account on the **server side**

 | 

When [calling the REST API of Push Kit](../device-cloud-debugging/generating-a-jwt-based-on-a-service-account/document.md#section33041381718) to push scenario-specific messages, you need to set the **Authorization** parameter in the request header. For details about the parameter setting, please refer to [Generating a JWT Based on a Service Account](../device-cloud-debugging/generating-a-jwt-based-on-a-service-account/document.md).

 |
| 

7

 | 

[Call the REST API to push scenario-specific messages](../device-cloud-debugging/pushing-scenario-specific-messages/document.md) on the **server side**

 | 

To call REST APIs from your app server, refer to the [Request Body Structure](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-scenariozed-api-request-struct) and [Request Body Parameters](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-scenariozed-api-request-param) of the HarmonyOS NEXT version. If an API call request fails, rectify the fault by referring to [Response Parameters](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-scenariozed-api-response). If an API call is successful but the device does not receive the message, rectify the fault by referring to [Why Does the Target Device Fail to Receive a Push Message After the Push API Is Successfully Called on the Cloud?](../faqs/why-does-the-target-device-fail-to-receive-a-push-message-after-the-push-api-is-/document.md).

 |
| 

8

 | 

(Optional) Develop the message receipt

 | 

The Push Kit server will send the message delivery status to your app receipt server in a message receipt, so you can learn about the status of the delivered message and rectify any possible errors. For details, please refer to [(Optional) Developing the Message Receipt](../device-cloud-debugging/optional-developing-the-message-receipt/document.md).

 |
| 

9

 | 

(Optional) Receive and process messages on the **client side**

 | 

Server-client [data transfer](../pushing-scenario-specific-messages/pushing-a-notification-message/sending-a-notification-message/document.md#section108252081117) can be achieved in the process of passing parameters on the server side and receiving data on the client side.

 |

#### (Optional) Other Message Types

For details about all message types supported by Push Kit and their application scenarios, please refer to [Message Types](../about-this-kit/document.md#section121512516176).

For example, your app can leverage in-app call messages for making voice and video calls, utilize text-to-speech messages for service implementation of voice broadcasting, and employ background messages to update app configurations.

-   Some types of scenario-specific messages require specific permissions to reach users. For details, please refer to [Overview of Scenario-Specific Message Permissions](../preparations/applying-for-scenario-specific-message-permissions/document.md#section1937015602710).
-   After a permission is approved, complete development based on the development guide section of the corresponding message type.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/tLJnt8RGQ3uikjq0RcURzA/notice_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062116Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D16475E30687122100819B7B7A612DCBF52330DED1A927F3112B6E588496D04F)

If your project has integrated Push Kit for HarmonyOS 3.x/4.x and now your app also needs to push notifications to devices running HarmonyOS Next/5.x or later, you need to complete the above development process again for the client and server sides.
