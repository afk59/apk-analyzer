# Function

The V3 scenario-specific message API divides typical push scenarios into multiple types and defines a unique **push-type** value for each scenario. The API provides message sending, governance, and other capabilities tailored for each scenario to better reach and engage users.

#### Use Cases

| 
push-type

 | 

Name

 | 

Scenario

 | 

Remarks

 |
| :-- | :-- | :-- | :-- |
| 

0

 | 

Alert message

 | 

Notification message.

 | 

You need to apply for the message self-classification permission. For details, please refer to [Message Self-Classification](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/push-apply-right#section16708911111611).

 |
| 

1

 | 

Widget update message

 | 

Widget update.

 | 

\-

 |
| 

2

 | 

Text-to-speech message

 | 

After Push Kit starts the notification extension subprocess, you can process the voice broadcast service in the subprocess.

 | 

You need to [apply for the text-to-speech message permission](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/push-apply-right#section159981112245).

 |
| 

6

 | 

Background message

 | 

Push Kit checks whether an app is started. If the app is started, a background message is sent to the target app. If the app is not started, the background message is cached.

 | 

\-

 |
| 

7

 | 

Live view message

 | 

Creates, updates, or ends a live view.

 | 

You need to [apply for the Live View Kit permission](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/liveview-rights).

 |
| 

10

 | 

In-app call message

 | 

In-app call message.

 | 

You need to [apply for the in-app call message permission](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/push-apply-right#section7291115452410).

 |

#### Restrictions

-   The message body cannot exceed 4096 bytes (excluding push tokens).
-   For each project, all apps can send a maximum of 1000 test messages (see pushOptions.[testMessage](../request-body-parameters/document.md#section418321011212)) per day. The service quota for formal messages varies depending on the scenario. For details, please refer to [Message Frequency Control](../message-frequency-control/document.md).
