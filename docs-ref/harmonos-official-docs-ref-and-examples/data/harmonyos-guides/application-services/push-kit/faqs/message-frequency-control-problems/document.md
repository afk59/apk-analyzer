# Message Frequency Control Problems

To provide better notification experience for users and prevent them from being disturbed by frequent messages, Push Kit offers a variety of frequency control rules. If the upper limit is reached, excess messages will be **discarded**. The count is reset the **next day**.

#### Possible Causes of Notification Message Frequency Control

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/dWGPiBnGQcWHT2LEm3l9dg/en-us_image_0000002542156749.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062117Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F5522C086F7BA1B7830D45FC2E9DC6422B8EE8A83C97A76FEE7D8EE42D5D3474 "Click to enlarge")

The specific rules are as follows.

**During app debugging**, a total of 1000 test messages (shared by all devices) can be pushed for each project per day and are not subject to scenario-specific message frequency control, meaning that distinguishment is not made between notification or scenario-specific message types. To send test messages, you need to set [testMessage](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-scenariozed-api-request-param#section418321011212) to **true**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/PZo1jz2PSr6la30FsPyN5Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062117Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=86892429C171C844250C126937D35B557CD67995E4E9A76BA5F2DC1B8E97928E)

If messages pushed exceed the limit (1000 messages), Push Kit will return result code **256** to your receipt server. Please note that the quantity (1000) here indicates the number of requests successfully sent by the REST API, but not necessarily the number of messages that successfully reach the devices.

**Once your app is officially released**, the message sending frequency will be regulated according to the service scenario and network traffic. In cases where message sending is unnecessary or unreasonable, frequency limits will be applied based on [Scenario-Specific Message Frequency Control](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-msg-freq-control#section551882820368). The following table lists the frequency control rules.

| 
Scenario

 | 

Frequency Control

 |
| :-- | :-- |
| 

Notification message

 | 

**If you have not applied for the message self-classification permission, messages pushed by your app are categorized as news and marketing messages by default (category set to MARKETING)**. According to [Notification Message Frequency Control Rules](../../preparations/applying-for-scenario-specific-message-permissions/document.md#section1128516504398), each app can push up to 2 or 5 (depending on the app category) messages to each device on a daily basis. If you need to send only news and marketing messages, you do not need to apply for the message self-classification permission. If you need to send service and communication messages, you need to [apply for the permission](../../preparations/applying-for-scenario-specific-message-permissions/document.md#section16708911111611) first.

 |
| 

Widget update message

 | 

For a released app, up to two messages can be pushed to each widget per device per day. For an unreleased app, up to five messages can be pushed to each widget per device per day.

 |
| 

Live view message

 | 

The messages of a single live view can be updated for up to 10 times every 5 minutes and 60 times every hour per device.

In the ride hailing and live score scenarios, the messages of a single live view can be updated for up to 30 times every 5 minutes and 180 times every hour per device.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/YbEUwrbcTfO3qvosAJpm_g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062117Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A326EEAC7E5C9A84EBAFFCE8D1D410EF1E1A68AED546DFFB9C586E84C0739F4F)

The message sending frequency will be regulated according to the service scenario and network traffic. In cases where message sending is unnecessary or unreasonable, frequency limits will be applied and Push Kit will send result code **102** to your receipt server.

If scenario-specific messages exceed the limits specified by frequency control rules, Push Kit will return result code **256**.

For details about frequency control rules, please refer to [Message Frequency Control](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-msg-freq-control). For details about the receipt status codes, please refer to [Receipt Status Codes](../../device-cloud-debugging/optional-developing-the-message-receipt/document.md#section19100519195717).

#### How many push tokens can I use to send messages through a REST API at a time?

A maximum of 1000 push tokens can be set in a single push. Therefore, the Push Kit server can send a maximum of 1000 messages based on the tokens at a time. If the number of messages to be sent is greater than 1000, error code [80300010](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-scenariozed-api-response#section199581758926) will be returned. In this case, you are advised to send these messages in batches.

#### Will the size of the message containing 1000 target push tokens exceed the size limit of a single push message (4 KB)?

The size limit is for the message body, which does not include carried push tokens.
