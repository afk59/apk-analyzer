# Integration Specifications

In an effort to maintain order within the Huawei notification ecosystem, protect users' legitimate rights, and ensure a positive user experience, this collection of specifications is hereby established in accordance with applicable laws and regulations, as well as the [HUAWEI Developers Service Agreement](https://developer.huawei.com/consumer/en/doc/start/agreement-0000001052728169), [Agreement on Use of Huawei APIs](https://developer.huawei.com/consumer/en/doc/20209), [HUAWEI Push Service Agreement](https://developer.huawei.com/consumer/en/doc/app/10134), [AppGallery Review Guidelines](https://developer.huawei.com/consumer/en/doc/app/50104), and [Atomic Service Review Guidelines](https://developer.huawei.com/consumer/en/doc/app/50129).

All HarmonyOS apps, joint operations apps, and atomic services (hereinafter referred to as "apps") that are to be released on HUAWEI AppGallery and use Push Kit must adhere to the specifications. Besides, all app developers should comply with the specifications and [HUAWEI AppGallery Connect Distribution Service Agreement For Paid Apps](https://developer.huawei.com/consumer/cn/doc/app/20204).

#### Usage Principles

-   Push messages of HarmonyOS apps must be delivered through Push Kit (Huawei's official push channel).
-   The [standard message layouts](#section178791211154912) must be used to ensure consistent notification experience.
-   Message push requires user consent and an app needs to ask users whether to allow notifications upon the first app launch.
-   Forcing changes to notification attributes for commercial purposes (for example, forcibly pin a notification to the top for a running app) is prohibited to safeguard user experience.
-   Comply with the [Notification Content Management Rules](../../appendixes/notification-content-management-rules/document.md).

#### Notification Content

To maintain legal, accurate, consistent, and readable push notification content, and to enhance user experience, please follow the [Notification Content Management Rules](../../appendixes/notification-content-management-rules/document.md).

#### Notification Layout

## Overview of Notification Layout Specifications

| 
General Principle

 | 

Exception Scenario

 |
| :-- | :-- |
| 

Do not forge push messages of other apps, including app icons and message content.

 | 

\-

 |
| 

Do not hide your app icon in a notification.

 | 

\-

 |
| 

Do not use a notification layout that is inconsistent with the design specifications.

 | 

\-

 |
| 

Do not forcibly pin a specific notification on the top for a running app.

 | 

Voice call, video call, media playback, progress notification (such as download, update, and upload), voice recording, navigation, screen projection, workout timer, and step count.

 |
| 

Do not modify the one-tap deletion button.

 | 

\-

 |
| 

Do not forge banner notifications or lock screen notifications.

 | 

\-

 |
| 

Do not send a same notification repeatedly to disturb users.

 | 

\-

 |
| 

Ensure that the notification title is different from the notification body.

 | 

\-

 |

## Text Format

| 
Description

 | 

Image Display

 |
| :-- | :-- |
| 

A maximum of three lines can be displayed for the notification content. If the content is too long, it is truncated by an ellipsis (...).

 | 

For details, please refer to [Styles for Common Notifications](https://developer.huawei.com/consumer/en/doc/design-guides/system-features-notification-0000001793074217#section4182426382).

 |

## Notification Badge

An app needs to display a numerical badge on their icon to indicate unread notification messages.

| 
Description

 | 

Image Display

 |
| :-- | :-- |
| 

The numerical badge is displayed in the upper right corner of the app icon.

 | 

For details, please refer to [Application Icon Badges](https://developer.huawei.com/consumer/en/doc/design-guides/system-features-notification-0000001793074217#section20838133494210).

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/5mrGzD1nQFGF8lyh1w7Vpw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062116Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=95D5A354CF6CB98F0860588E5C7A15B939682EC398D873B09E38F79565DB06A6)

Wearables and TVs do not support this notification format.

## Large Notification Icon

| 
Description

 | 

Image Display

 |
| :-- | :-- |
| 

This icon applies to notifications with image preview.

 | 

For details, please refer to [Styles for Notifications with Image Previews](https://developer.huawei.com/consumer/en/doc/design-guides/system-features-notification-0000001793074217#section16214134103817).

 |

A large notification icon must meet the following requirements:

-   Use a JPG, JPEG, PNG, or BMP image as the icon. The image width x height must be less than 128 x 128 pixels. Images larger than 49,152 pixels will not be displayed.
-   Avoid highly saturated or solid colors (such as black or red). Maintain color saturation and brightness within a 10%-90% range.
-   Use an image that is clear and easily understandable. Avoid elements that obstruct image comprehension, such as QR codes, pixelation, obvious noises, or dense text and symbols.
-   Ensure that the image quality matches the overall notification quality. Avoid complex, cluttered images with multiple elements that detract from the visual appeal.
-   Ensure that the image does not obstruct critical notification text.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/duEa-ffAQnGu1PDcWzXN8w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062116Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9FE9E5537703B83C027986FF801D53950D733549038E10D5526DBF996E0C9F5E)

Wearables do not support this notification format.

## Multi-Line Text Format

If a notification contains a significant amount of content, display the content in a clear and organized manner.

| 
Description

 | 

Image Display

 |
| :-- | :-- |
| 

A maximum of three separate lines of content can be displayed. For each line, overlong text will be truncated by an ellipsis (...).

 | 

For details, please refer to [Style for Multi-line Text Notifications](https://developer.huawei.com/consumer/en/doc/design-guides/system-features-notification-0000001793074217#section148485300395).

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0b/v3/U_UOiwEqRqakjr1_xpXmFg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062116Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4EEF54F01B1E6A34E53DD843C8C498E9F3B7EBCF1E24C0DBDB0CA738AE9003A0)

Wearables do not support this notification format.

#### Notification Redirection

-   A notification should not launch another app.
-   A notification should not link to an illegal website.
-   A notification should not trick users into downloading a third-party app.

#### Notification Switch Authorization

-   When your app is launched for the first time, ask the user whether to allow notifications.
-   Disable the notification switch by default until explicit user consent is obtained.

#### Other Rules

-   Do not tamper with, damage, or decompile functions provided by Push Kit or modify the basic functions of Push Kit.
-   Avoid any other behavior that may compromise user experience.
