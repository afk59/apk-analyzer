# Why Does the Target Device Fail to Receive a Push Message After the Push API Is Successfully Called on the Cloud?

After a message is successfully delivered from the cloud, the target device may fail to display the message due to reasons such as frequency control and disabled notification switch.

#### Possible Causes of Message Receiving Failure

-   Frequency control occurs for the messages. Please check whether you have [enabled the message self-classification permission](../../pushing-scenario-specific-messages/pushing-a-notification-message/sending-a-notification-message/document.md#section15809122792917). You are advised to send test messages during debugging. For details, please refer to [Message Frequency Control Problems](../message-frequency-control-problems/document.md).
-   The network connection of the device is abnormal, for example the device is in the test environment or is not connected to the external network.
-   The notification switch on the device is disabled.
-   The push token has expired. A push token will expire in scenarios such as: the app has not been installed or has been uninstalled (for details, please refer to [Use Cases](../../preparations/obtaining-a-push-token/document.md#section123091617105820)). In this case, regenerate a push token.
-   The app is running in the foreground, but a text-to-speech message ([push-type](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-scenariozed-api-request-struct#section20573634202313) set to **2**) is pushed. In this case, switch the app to the background and then push the text-to-speech message again, or just push a common notification message instead (with **push-type** set to **0**).
-   The **skills** section is incorrectly configured. For details about how to configure the section, please refer to [Actions to Be Triggered upon Message Tapping](../../pushing-scenario-specific-messages/pushing-a-notification-message/sending-a-notification-message/document.md#section697519219136).
-   The message is sent in gentle notification mode. Messages categorized as news and marketing messages or without the self-classification permission are sent in gentle notification mode. Such notifications are displayed only in the notification panel without banner, lock screen, ringtone, or vibration alerts. Users need to check such notifications in the notification panel.

#### Troubleshooting

1.  You are advised to [develop the message receipt](../../device-cloud-debugging/optional-developing-the-message-receipt/document.md). Then the Push Kit server will send the message delivery status to your app receipt server in a message receipt, so you can rectify any possible errors based on the [receipt status code](../../device-cloud-debugging/optional-developing-the-message-receipt/document.md#section19100519195717).
2.  You can sign in to [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html), open your project, go to **Development and services** > **Push Kit** > **Self-service analysis (beta)**, and trace messages and query push token information.
