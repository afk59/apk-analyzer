# Message Frequency Control

Push Kit's message frequency control includes scenario-based, device-based, and test message frequency control, as well as the push rate control. Upon the violation of any frequency control rule, a corresponding receipt status code will be returned (see [Receipt Status Codes](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/push-msg-receipt#section19100519195717) for details).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/nMAqSYAXQ3yGsK7HU4G54w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062518Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FF0BE6DD41CFFD08D041D838C7DA8AC7102B590AD8F6264E678DD7E0C6CDB4C9)

The message count used in a frequency control rule is based on the number of push requests sent by an app, regardless of whether the device successfully displays the message. If a message is not displayed as expected, you are advised to [troubleshoot the issue](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/push-faq-2) before sending more push requests.

#### Scenario-Specific Message Frequency Control

To provide better user experience, Push Kit provides different frequency control rules for various [push scenarios](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/push-scenes).

If scenario-specific messages exceed the limits specified by frequency control rules, Push Kit will return result code **256** to your message receipt server. For details, please refer to [Receipt Status Codes](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/push-msg-receipt#section19100519195717).

The following table lists the frequency control rules.

| 
Scenario

 | 

Frequency Control Rule

 |
| :-- | :-- |
| 

Notification message

 | 

1\. Apps are punished for violations based on the number of violations. For details, please refer to [Push Notification Violation Penalty Criteria](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/push-punishment-standards).

2\. When the message [category](../request-body-parameters/document.md#section17371529101117) is set to **MARKETING**, the frequency control rule for marketing messages is applied. For details, please refer to [Notification Message Frequency Control Rules](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/push-apply-right#section1128516504398). If an app has not [enabled message self-classification](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/push-send-alert#section15809122792917), all notification messages are classified into news and marketing messages by default.

 |
| 

Widget update message

 | 

The update frequency is limited for each app per widget.

Default frequency: For a released app, up to two messages can be pushed to each widget per device per day. For an unreleased app, up to five messages can be pushed to each widget per device per day.

 |
| 

Live view message

 | 

The messages of a single live view can be updated for up to 10 times every 5 minutes and 60 times every hour per device.

In the ride hailing and live score scenarios, the messages of a single live view can be updated for up to 30 times every 5 minutes and 180 times every hour per device.

 |

#### Device-based Message Frequency Control

In addition to the scenario-specific message frequency control, Push Kit limits the total number of messages that can be received by a single device per day. The message sending frequency will be regulated according to the service scenario and network traffic. In cases where message sending is unnecessary or unreasonable, frequency limits will be applied and Push Kit will send result code **102** to your receipt server. For details, please refer to [Receipt Status Codes](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/push-msg-receipt#section19100519195717).

#### Test Message Frequency Control

To facilitate message testing, you can set pushOptions.[testMessage](../request-body-parameters/document.md#section418321011212) to **true** to send test messages.

A total of 1000 test messages (shared by all devices) can be pushed for each project per day and are not subject to [scenario-specific message frequency control](#section551882820368). If more than 1000 test messages are sent for a project on a single day, message throttling will be implemented until the next day, and Push Kit will return result code **256** to your message receipt server. For details, please refer to [Receipt Status Codes](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/push-msg-receipt#section19100519195717).

#### Message Push Rate Control

Message push rate refers to the QPS of an app, that is, the number of devices to which an app sends messages per second. If the QPS of an app exceeds the threshold, [HTTP response code](../response-parameters/document.md#section4405122736) 503 is returned. The QPS varies depending on the app type and increases with the number of monthly active users of the app on Huawei devices. To query the QPS threshold of an app, sign in to [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html), go to **Development and services** > **Grow** > **Push Kit** > **Settings**, select the app, and check the QPS threshold.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/Ixr49TdjSJKRa9aJ8KOmaw/en-us_image_0000002368546128.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062518Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B412F95F49CA946DA685C62A81BD600FE36620D4FED3D85278F097AC02FEA890)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/c25ypcr8TPiviCOvaQ2kOw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062518Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0E6E87DA12B64D08DFD83CFCCB4E796032F25E66462869C80BBBD0DE53C798EC)

-   When the network traffic is high, system-level flow control will be implemented, causing requests to be rejected with [HTTP response code](../response-parameters/document.md#section4405122736) 503.
