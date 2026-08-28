# About This Kit

Push Kit is a messaging service provided for you to establish a cloud-to-device messaging channel. With Push Kit integrated, HarmonyOS apps can reach the right users at the right time, boosting user engagement and stickiness.

#### Quick Start

For details about how to integrate Push Kit, please refer to [Getting Started](../getting-started/document.md).

#### Highlights

-   **Stable messaging channel**
    
    Push Kit offers system-level long links that can be used to push messages in real time, even when your app isn't running.
    
-   **Tailored message styles**
    
    Push Kit offers a variety of message display options, including text styles, large message icons, multi-line text, and badges, to cater to your diverse and personalized messaging needs.
    
-   **Flexible scenario-specific messages**
    
    You can leverage scenario-specific messages to reach users flexibly in a wide range of scenarios. For example, your app can leverage in-app call messages for making voice and video calls, utilize text-to-speech messages for service implementation of voice broadcasting, and employ background messages to update app configurations.
    

#### Notification Scenarios of Push Messages

Push messages are notifications sent from an app to Huawei devices via **Push Kit**. Users will receive notifications through the notification panel, banners, lock screen, app icon badges, and notification icons.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/kqTrxronTFGerLsaAnvC6g/en-us_image_0000002520398629.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062116Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B29A6A8E9D9F85C32ED2E7E8F19268A05F8DDD292040474A9C8EE5AE00204E31 "Click to enlarge")

For details about each scenario, please refer to [Notification Scenarios](https://developer.huawei.com/consumer/en/doc/design-guides/system-features-notification-0000001793074217#section162699204401).

#### Message Types

Push Kit supports the following message types.

| 
Message Type

 | 

Description

 |
| :-- | :-- |
| 

[Notification message](../pushing-scenario-specific-messages/pushing-a-notification-message/document.md)

 | 

A notification message is directly sent by Push Kit and displayed in the notification panel, on the lock screen, or as a banner. Users can tap the message to launch the corresponding app.

You can leverage [various notification message layouts](../pushing-scenario-specific-messages/pushing-a-notification-message/sending-a-notification-message/document.md#section5164103925811) to attract users.

Common application scenarios: travel reminder and account status

 |
| 

[Text-to-speech message](../pushing-scenario-specific-messages/pushing-text-to-speech-messages/document.md)

 | 

When a user device receives a text-to-speech message from your app, Push Kit will start a subprocess of your app to handle the relevant service logic.

Common application scenarios: voice broadcast

 |
| 

[Widget update message](../pushing-scenario-specific-messages/pushing-a-widget-update-message/document.md)

 | 

Your app can push updated widget content via widget update messages at the right moment to engage users.

Common application scenarios: ride hailing and package delivery tracking

 |
| 

[Background messages](../pushing-scenario-specific-messages/pushing-a-background-message/document.md)

 | 

Upon receiving a background message, the device will transfer the message to the app if the app is currently running in the foreground. Otherwise, the message will be cached for later delivery after the app is launched.

Common application scenarios: notifications of app configuration updates

 |
| 

[Live view messages](../pushing-scenario-specific-messages/pushing-a-live-view-message/document.md)

 | 

Your app can request the Push Kit server to create or update a live view.

Common application scenarios: live score and ride hailing status updates

 |
| 

[In-app call messages](../pushing-scenario-specific-messages/pushing-an-in-app-call-message/document.md)

 | 

This type of messages empower your app with voice and video call capabilities.

Common application scenarios: voice and video call

 |

#### Service Process

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/yvslvlD-TJSCKSVb-s_BUQ/en-us_image_0000002488158806.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062116Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C815AA56944CBC1277C975F865302EC0229FB22374420000F8EEB194FAB910FB "Click to enlarge")

The service process of Push Kit is as follows:

1.  An app calls Push Kit to obtain a push token.
2.  The app reports information including the push token to the app server.
3.  The app server sends a push message request to the Push Kit server. The notification function of an app is disabled by default. Before requesting message push, request user authorization for sending notifications. For details, please refer to [Requesting Notification Authorization](../../notification-kit/requesting-notification-authorization/document.md).
4.  The Push Kit server delivers the message to Push Kit.
5.  Push Kit processes the message.

#### Restrictions

## Factors Affecting the Delivery Rate

Push Kit functions as a secure and reliable system-level messaging channel to ensure successful message delivery. The message delivery may be affected by the following factors:

-   Whether the target device is connected to the network. Push Kit caches a message if its target device is offline, and delivers the message after the device goes online.
-   Whether the app has been uninstalled from the device
-   Whether the network status of the target device is stable
-   Security control policies of the target device

## Message Timeliness

When the device network is in good conditions and not congested, Push Kit utilizes intelligent push policies to reduce the messaging latency.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e/v3/dT2gmM5XSoGXC6kduaWxGg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062116Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F06A72B2F0923131BCFE26033634E095D8D8867729B30B1A6AA0377C3E0F9E21)

To reduce disturbance to users, the OS will learn their behavioral habits, predict their sleep time, and implement message control during their sleep. Push Kit will cache messages pushed during this period (excluding in-app call messages or VoIP messages with **category** set to **VoIP**). Push Kit will redeliver the messages to the user device until the user wakes up.

## Message Length and Quantity Limits

-   The message body cannot exceed 4096 bytes (excluding the token).
-   For each project, all apps can send a maximum of 1000 test messages altogether (see **pushOptions.[testMessage](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-scenariozed-api-request-param#section418321011212)**) per day. The service quota for formal messages varies depending on the scenario. For details, please refer to [Message Frequency Control](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-msg-freq-control).

## Network Restrictions

If the network where a device is located has a firewall or is restricted, ensure that the following port numbers are enabled to allow traffic, so that your message delivery rate will not be affected:

Port numbers:

-   5223
-   443

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/gKKhheaATBKeer7EkaqAvw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062116Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=48DAD3848A55AFC72326279294ADC0B033404CE8FF7C218164731FFFD59E3523)

The IP address of the push server is allocated dynamically and its access cannot be allowed just by adding the server IP address to the trustlist. You are advised to use a device on an unrestricted network or allow the port numbers above.

## Supported Devices

Push Kit supports phones, tablets, PCs/2-in-1 devices, wearables, and TVs.

## Emulator Version and Remote Real Device Description

Push Kit supports the Emulator, but there are some differences in feature support between real devices and the Emulator. For details, please refer to [Differences Between the Emulator and the Real Device](../../../coding-and-debugging/running-your-app-on-the-emulator/overview/differences-between-the-emulator-and-the-real-device/document.md#section38231424133213). Push Kit does not support debugging on remote real devices.

#### Relationship with Other Kits

-   Push Kit establishes a messaging channel from the cloud side to devices, enabling real-time message delivery from the cloud side. If you want to push notifications directly from devices, leverage capabilities of [Notification Kit](../../notification-kit/about-this-kit/document.md).
-   To [push a widget update message](../pushing-scenario-specific-messages/pushing-a-widget-update-message/document.md), use [Form Kit](../../../application-framework/form-kit/about-this-kit/document.md) to create a widget for your app first.
-   To [push a live view update message](../pushing-scenario-specific-messages/pushing-a-live-view-message/document.md), use [Live View Kit](../../live-view-kit/about-this-kit/document.md) to create a local live view first.
-   To [push an in-app call message](../pushing-scenario-specific-messages/pushing-an-in-app-call-message/document.md), use [Call Service Kit](../../call-service-kit/about-this-kit/document.md) to manage app calls.

#### Sample Code

Refer to the [sample code](https://gitcode.com/harmonyos_samples/push-kit-sample-code-clientdemo-arkts) of Push Kit for details.
