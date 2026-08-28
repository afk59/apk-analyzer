# Cross-Device Notification Overview

The cross-device notification is designed to implement collaborative interaction of notifications between a smartphone and another devices such as a watch. Typical scenarios are as follows:

-   [Clearing Repeated Notifications Across Devices](../clearing-repeated-notifications-across-devices/document.md): Clear repeated notifications published across devices and by the local device to prevent multiple notifications from disturbing users.

#### Constraints

-   Cross-device notification is supported between phones and watches since API version 18, and between phones and tablets or 2-in-1 devices since API version 20.
-   [Notification slot types](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-notificationmanager#slottype) supported for cross-device notification:
    -   Watch: **SOCIAL\_COMMUNICATION** and **LIVE\_VIEW**.
    -   Tablet: **SOCIAL\_COMMUNICATION**, **SERVICE\_INFORMATION**, **LIVE\_VIEW**, and **CUSTOMER\_SERVICE**.
    -   2-in-1 device: **SOCIAL\_COMMUNICATION**, **SERVICE\_INFORMATION**, and **CUSTOMER\_SERVICE**.

#### Working Principles

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/JlMg5Eu_R7Kl3AwAgpsWQQ/en-us_image_0000002537765274.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062114Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A73F016A6625F02181858C68DD5FA326E71FBD1B4CD0D8F262CC8CC9559E4153)
