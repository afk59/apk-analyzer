# About This Kit

With Notification Kit, you can publish local notifications from your application and push them to users on the client. Local notifications can be displayed by ringtones, vibrations, banners, lock screen, screen off, Always On Display (AOD), and notification panel based on the notification type and publishing scenario.

#### When to Use

When an application is running, you can use Notification Kit to publish notifications to users. When the application is switched to the background, you cannot publish local notifications. Instead, you need to access the [Push Kit](../../push-kit/about-this-kit/document.md) to publish offline notifications on the cloud.

You can use the local notification capability in multiple scenarios. For example, synchronize the upload and download progress of the user, send instant customer service payment notifications, and update the number of steps.

#### Capability Scope

Notification Kit supports the following capabilities:

-   Publishes notifications in the form of text or progress bar.
-   Carries or updates the application notification badge.
-   Cancels one or all published notifications.
-   Queries the list of published notifications.
-   Queries the status of the notification function of an application.
-   Enables notification publishing (disabled by default) by triggering an authorization dialog to request user consent for sending notifications.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/eIhbI9ivRe25rQiEMhRwhg/en-us_image_0000002537765270.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062114Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=24FA7FF9A9E6C41E8A04BE0D28616D16103D2FB8FF5A3E046F85AF7C83C67584)

#### Service Flow

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/awCguz2JREOjrdTsMM1jNQ/en-us_image_0000002537925210.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062114Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AE0F80F8299F4D43A7A9C912F6FAEE5AB278FC84229959552EAE52FC4FC984E4)

The main service flow of using Notification Kit is as follows:

1.  Request notification authorization.
    
2.  Publish a notification to Notification Kit.
    
3.  Display the notification in the notification center.
    

#### Notification Style

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/fnfc-eTzTIqZbMGHbhDdDw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062114Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5DAD30EBDF372BBF3579BA3ABC749F3D34EBD6138F07F7B4EBEA891F685A4EFA)

The display effect depends on the device capability and notification center UI style.

Common notification styles in Notification Kit are as follows.

| Type | Notification Style | Description |
| :-- | :-- | :-- |
| [Text](../publishing-a-notification/publishing-a-text-notification/document.md) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/NbvlLoTDQJSJrkxomtjmMw/en-us_image_0000002568684987.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062114Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=86CBA598BB3EB0B2D90B45EDD9C9DF7FDABED75C5686A5B14D9E3A4FE34FBEBB) | A maximum of three lines can be displayed in the notification text. Excess content is truncated by an ellipsis (...). |
| [Multi-line text](../publishing-a-notification/publishing-a-text-notification/document.md) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/zwwjPLR4RD-_7-YUgrXU-w/en-us_image_0000002568764997.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062114Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DDFF0C8DF897125FD5D8004F4A220226AD93099FED37947DA1D5A8C7C10B0300) | A maximum of three lines of content can be displayed. Excess content of each line is truncated by an ellipsis (...). |
| [Notification badge](../managing-the-notification-badge/document.md) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/kwSIWXUaTuKsayJODXYBng/en-us_image_0000002537765272.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062114Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C94F8908E4BAA7F0A89986EE66227F06B9E45DCE57362301E13F1680D344F353) | Displayed as a number in the upper right corner. |
| [Progress bar](../publishing-a-notification/publishing-a-progress-notification/document.md) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/InpeqmlwTBGu3uP8rEKfcw/en-us_image_0000002537925212.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062114Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=689FC924185A48FD0643C171A163BD243168B93810EA17F754662FA571EAB122) | Progress notification. |

#### Constraints

-   There is a limit on the number of notifications per application in the system windows. The current limit is 24.
-   The notification cannot exceed 200 KB (due to cross-process serialization).
-   The publication and update frequencies for notifications must meet the following requirements. Otherwise, the publication or update fails and the corresponding error code is returned.
    -   The total number of notifications published by an application cannot exceed 10 per second, and that of notifications updated cannot exceed 20 per second.
    -   The total number of notifications published by all third-party applications cannot exceed 15 per second, and that of notifications updated cannot exceed 30 per second.

#### Relationship with Related Kits

-   Notifications created by Notification Kit are displayed in the notification center or other system entries in real time. To display some scheduled notifications to remind users after the application is switched to the background or the process is terminated, for example, reminders for flash sales in shopping applications, you can use [Background Tasks Kit](../../../application-framework/background-tasks-kit/about-this-kit/document.md) to create notifications. Currently, notifications based on countdown, calendar, and alarm clocks are supported.
-   You can use the [getWantAgent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-wantagent#wantagentgetwantagent) API of [Ability Kit](../../../application-framework/ability-kit/about-this-kit/document.md) to set the **WantAgent** triggered when a user taps a notification.
-   You can use [Push Kit](../../push-kit/about-this-kit/document.md) to push remote notifications to the local device.
