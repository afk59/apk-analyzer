# Applying for Scenario-Specific Message Permissions

#### Overview of Scenario-Specific Message Permissions

Push Kit supports a wide range of scenario-specific message types. Some of the types require specific permissions to reach users. The following table describes the permissions required by each message type.

| 
Scenario-Specific Message Permission

 | 

Description

 | 

Application Scope

 |
| :-- | :-- | :-- |
| 

Message self-classification

 | 

Allows you to classify notification messages by yourself to improve user experience. Messages can still be sent without this permission. In this case, Push Kit classifies these messages as **[news and marketing](#section1924971516101)** messages by default.

NOTICE:

**If you have not applied for the message self-classification permission, messages pushed by your app are categorized as news and marketing messages by default**. The maximum number of news and marketing messages that can be pushed by an app to each device on a daily basis is either **2** or **5**, depending on your app category. If your upper limit is reached, send test messages or apply for the self-classification permission.

 | 

All apps can apply for this permission. However, some message categories are available only for specific app categories.

 |
| 

Text-to-speech message

 | 

Pushes a notification message when it arrives at a device and activates the app to perform actions such as voice broadcast. An app can push text-to-speech messages only after gaining this permission.

 | 

This permission is available only for apps that send new order notifications to merchants and support merchant payment reception.

 |
| 

In-app call message

 | 

This permission allows your app to display the call screen and start the voice or video call when an in-app call message arrives at a device. An app can push in-app call messages only after gaining this permission.

 | 

This permission is available only for communication and alarm apps that provide the in-app video and voice call function.

This permission applies only to call scenarios within an enterprise or organization itself.

 |

The following sections will detail the specific permissions of scenario-specific messages and how to apply for them.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/IRhpfN4ITomJQRtKsQw0lA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062116Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9FCC28605C9F4C2782143495B093DBBD05C77664E6333C234D3320DF10B9DF7B)

If you encounter any problems during the permission application, send an email to [hwpush@huawei.com](mailto:hwpush@huawei.com) to contact us.

#### Message Self-Classification

## Message Classification Mode

To improve user experience and build a sound sustainable messaging ecosystem, Push Kit classifies [notification messages](../../pushing-scenario-specific-messages/pushing-a-notification-message/document.md) into the following categories based on the message content for easier management: **service and communication** and **news and marketing**. To tailor notification messages more precisely to your business requirements, you can classify messages by yourself based on the [Message Classification Standards](#section1924971516101).

If an app has not enabled message self-classification, all notification messages are classified into **news and marketing** messages by default.

The following flowchart demonstrates the message classification logic.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/az7x3tSTRsS9mUVj1Iry9w/en-us_image_0000002493423430.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062116Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=79F6E03B7CBFB8F1A449132F9E7E081BEF8F3206AEFE2651EEB914D601DE406F "Click to enlarge")

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/6qqfaj9IT_i8Jq3zozrI0g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062116Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3513FF9C54EA6C4A1D7BEC0D68CAC75D265CCD6C93D3A0A46C62ADCA9E5E70F2)

-   If your app has the self-classification permission and the message to be pushed carries the [category](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-scenariozed-api-request-param#section17371529101117) field with an approved value, Push Kit will trust your self-classification. Note that, if your app only needs to push news and marketing messages, you do not need to apply for the self-classification permission.
-   If the message to be pushed for your app contains an unapproved value of the [category](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-scenariozed-api-request-param#section17371529101117) field (for example, the value **IM** that has not been approved for your app is passed to **category**), the message is automatically classified into a news and marketing message instead of your defined category.

The standards for classifying notification messages apply only to [push notification messages](../../pushing-scenario-specific-messages/pushing-a-notification-message/sending-a-notification-message/document.md) and also must be applied for such messages. For details, please refer to [Message Classification Standards and Notification Modes](#section1924971516101). Other scenario-specific messages can be developed and adapted according to relevant guides.

## Message Classification Standards and Notification Modes

Push Kit classifies notification messages into the following types based on message content and messaging scenarios: **service and communication messages**, as well as **news and marketing messages**. Push Kit also tailors notification management based on message classification. This includes adjusting reminder modes, display positions, and push frequency for different message types.

| 
**Message Type**

 | 

**Scenario Description**

 | 

**Notification Mode and Display Location**

 | 

Frequency Control

 |
| :-- | :-- | :-- | :-- |
| 

Service and communication

 | 

Provides timely updates to users through the notification panel, including social communication and service reminder messages. These messages are usually expected by users.

 | 

Lock screen, ringtone, vibration, etc.

NOTE:

**Service reminder messages** can only be displayed in the notification panel on wearables in silent mode.

TVs do not support ringtones or vibration.

 | 

The message sending frequency will be regulated according to the service scenario and network traffic. In cases where message sending is unnecessary or unreasonable, frequency limits will be applied.

 |
| 

News and marketing

 | 

Provides information such as activity notices, recommendations, and news, including news messages and marketing messages. These messages are sent from operations personnel to users.

 | 

Gentle notification, which will display a notification only in the notification panel

NOTE:

**News and marketing messages** are delivered in the lock screen, ringtone, or vibration notification mode on wearables.

TVs do not support ringtones or vibration.

 | 

Each app can push up to 2 or 5 (depending on the app category) messages to each device on a daily basis.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/-TyXyfXoQ0-tB2nilRqOrA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062116Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DA7B727C39EF2C61A4323D183A37A99EBA8F9067AA4FF9D47A6BDCC865FCA282)

Push Kit's message classification standards are subject to change as app messaging evolves. Please refer to this document for the most current classification guidelines.

**Service and Communication - Social**

| 
**Message Type**

 | 

Value of category on Cloud

 | 

**Scenario Description**

 | 

**Notification Mode**

 |
| :-- | :-- | :-- | :-- |
| 

Instant messaging

 | 

IM

 | 

Point-to-point or group chatting messages (or private message) between users.

**Note: You need to declare that such messages do not include private messages from unfollowed users, official account messages, or batch messages or ads sent by merchants.**

 | 

Social messages under the **service and communication** category. The default notification mode is lock screen + ringtone + vibration. Users can change the notification mode for an app in **Notifications**.

 |
| 

Voice and video call

 | 

VOIP

 | 

Notifications for voice call invitation, video call invitation, and incoming calls.

**Note: These messages serve as notifications only and do not initiate app launch or call connection.**

 |
| 

MISS\_CALL

 | 

Missed call notifications.

 |

**Service and Communication - Service Reminder**

| 
**Message Type**

 | 

Value of category on Cloud

 | 

**Scenario Description**

 | 

**Notification Mode**

 |
| :-- | :-- | :-- | :-- |
| 

Travel

 | 

TRAVEL

 | 

Notification messages relevant to travel that are pushed to consumers, including:

-   Trip reminder
-   Flight/Train change notification
-   Reminder before hotel check-in
-   Bus arrival

 | 

Service reminder messages under the **service and communication** category. The default notification mode is lock screen + ringtone + vibration. Users can change the notification mode for an app in **Notifications**.

NOTE:

Gentle notification is used for wearables, which will display a notification only in the notification panel.

 |
| 

Health

 | 

HEALTH

 | 

Notifications about health data that users proactively request measurement. This type is available only for sports and health apps.

-   Workout data (such as steps, cycling mileage, and swimming distance)
-   Body data (such as the heart rate, weight, body fat, and calories burned)

 |
| 

Work reminder

 | 

WORK

 | 

Notifications that remind users of future events and to-do items, including:

-   Event reminder: such as meeting reminder, to-do reminder, schedule reminder, and teaching task/course reminder.
-   To-do items for service providers: such as review progress reminder, certification progress reminder, work order notification, new order notification, after-sales notification, delivery urging notification, and ride hailing order notification.
-   Merchant operations occasions: such as insufficient inventory, sellout, product removal, restricted money withdrawal, customer complaint, store restrictions, product blocklist, transaction violation, and counterfeit/fraudulent shipment.

 |
| 

Account change

 | 

ACCOUNT

 | 

Notifications sent when a user account or assets under an account change.

-   Account change: such as account sign-in/-out, account status change, and account information authentication.
-   Account asset change: such as membership expiration, membership renewal, and balance change (real asset change, but not changes of bonus points, gold coins, or leaderboard rankings).

 |
| 

Order & Logistics

 | 

EXPRESS

 | 

Notifications that contain order information or logistics information of ongoing or completed orders.

-   Order notifications: These notifications are sent to notify consumers of successful order placement, order details, order status, order complaint handling progress, and invoice generation.
-   Logistics notifications: These notifications contain logistics status, including shipped, being delivered, accepted, and picked up.

 |
| 

Finance

 | 

FINANCE

 | 

Notifications about transaction amount changes and wealth management/investment information. This type is available only for financial, banking, and payment apps and can be triggered in the following scenarios:

-   Payment and payment reception, bank deposit and deduction, transaction, collection and refund, top-up, unpaid bills, loan application status, repayment/overdue payment, account freezing, amount limit, and security deposit payment.
-   Wealth management product purchase success, wealth management product maturity/redemption availability, dividend distribution/income update, and risk level adjustment.
-   Conditional order triggering, entrusted trade, successful allocation, auto-renewal or redemption, net asset value notification, rights offering/bond allotment, new share application, and stock trade.

 |
| 

Device reminder

 | 

DEVICE\_REMINDER

 | 

Notifications sent to inform users of any device status change, warning, and alarm from IoT devices.

 |
| 

Email

 | 

MAIL

 | 

Notifications sent to inform users of new emails. This type is available only for email and office software apps.

 |
| 

Voice broadcast

 | 

PLAY\_VOICE

 | 

Voice broadcast played by the app to remind users. This mode is specially suitable for merchant operations to broadcast user payment amounts, user payment cancellations, and order placement by users.

 | 

Service reminder messages under the **service and communication** category. The default notification mode is lock screen + vibration. Users can change the notification mode for an app in **Notifications**. To avoid conflicts with other in-app voice notifications, the ringtone notification mode is not available to this type of messages.

NOTE:

Gentle notification is used for wearables, which will display a notification only in the notification panel.

 |
| 

Subscription

 | 

SUBSCRIPTION

 | 

Subscription messages sent to users if they proactively subscribe to content and allow notifications. This type is available only in the following scenarios:

-   A user proactively sets a reminder for a live streaming program or a reminder for a reserved activity.
-   A user proactively sets a check-in reminder.
-   A user proactively sets a price reduction reminder.
-   A reminder is sent when a followed account releases a new post or an author updates their book.
-   A user proactively sets a market dynamics reminder (price fluctuation and prediction).
-   A reminder is sent for a paid subscription.
-   A reminder is sent for a topic proactively subscribed by a user (such as news, financial updates, weather, or industry-specific insights).
-   Notifications about social interactions are sent: such as friend activities, new followers, added friends, being liked, being mentioned, being added to favorites, comments, messages, follows, replies, and reposts.

 | 

Service reminder messages under the **service and communication** category. The default notification mode is lock screen + ringtone + vibration. Users can change the notification mode for an app in **Notifications**.

NOTE:

-   Gentle notification is used for wearables, which will display a notification only in the notification panel.
-   Subscription messages are applicable for a specific scenario only when the corresponding process requirements listed in the table below are met.
-   You are advised to [set a quick entry for enabling app notifications](../../../notification-kit/setting-quick-entry-for-enabling-application-notifications/document.md) in your app. This will allow users to easily locate the notification categorization switch, thereby enhancing their notification management experience and helping to reduce the app notification disabling rate.

 |

**Subscription process requirements for requesting subscription messages**

| 
Subscription Type

 | 

Subscription Scenario

 | 

Subscription Process Requirements (Submit a Diagram Illustrating Your Subscription Process)

 |
| :-- | :-- | :-- |
| 

Common subscription messages

 | 

Live streaming program reminder

Reserved activity reminder

Check-in reminder

Price reduction reminder

Reminder sent when a followed account/author releases a new post

Book update reminder

Market dynamics reminder

Paid subscription reminder

Reminder of a proactively subscribed topic

 | 

-   The subscription page must include both a subscribe/follow button and a corresponding unsubscribe/unfollow option.
-   The option for sending notifications about subscription/following is disabled by default.
-   Upon subscription, your app must display a separate pop-up asking users whether they want to receive push notifications related to this subscription.
-   Push notifications must clearly indicate that they are subscription messages. (For example, the notification title or body should include explicit words like "subscription"/"reserved activity"/"following"/friend"/"follower".
-   The subscription content topic scope should not be overly broad or vague (incorrect examples: information subscription; interest tag subscription).

 |
| 

Social updates

 | 

Notifications about social interactions

 | 

-   Your app must provide a separate notification switch for each type of social interaction, including comments, replies, favorites, and likes.
-   Push notifications must clearly indicate that they are subscription messages. (For example, the notification title or body should include explicit words like "subscription"/"reserved activity"/"following"/friend"/"follower".

 |

**News and Marketing - Content & News**

| 
**Message Type**

 | 

Value of category on Cloud

 | 

**Scenario Description**

 | 

**Notification Mode**

 |
| :-- | :-- | :-- | :-- |
| 

Financial dynamics

 | 

MARKETING

 | 

Notifications about stock, lottery, futures, options, and foreign exchange, including transaction notices and industry announcements.

 | 

**News and marketing** notification messages. These messages will be displayed only in the notification panel in gentle notification mode.

NOTE:

The notification mode for wearables is lock screen + ringtone + vibration. Users can change the notification mode for an app in **Notifications**.

 |
| 

Lifestyle & Information

 | 

Navigation notifications: including route display, route planning based on real-time traffic conditions, traffic conditions (congestion alerts), location services, and map app launch for location.

 |
| 

Surveys

 | 

Notifications to gather user feedback on product usage habits, product satisfaction, and service quality.

 |
| 

Others

 | 

Messages that communicate for feature recommendations, platform announcements, and app updates.

 |
| 

Content recommendation

 | 

Messages for recommending content to users, without their proactive subscription.

Such content includes comments, books, ads, videos, audios, programs, courses, live streaming channels, community topics, and game publicity.

 |
| 

News

 | 

Notifications highlighting newsworthy, recent events.

News topics include politics, economics, law, military, technology, education, culture, sports, and society.

 |
| 

Social updates

 | 

Notifications that recommend users: including people nearby, influencers, streamers, potential matches, and people you might know.

 |

**News and Marketing - Campaigns**

| 
**Message Type**

 | 

Value of category on Cloud

 | 

**Scenario Description**

 | 

**Notification Mode**

 |
| :-- | :-- | :-- | :-- |
| 

Function recommendation

 | 

MARKETING

 | 

Notifications that recommend a certain function of the app to users.

 | 

**News and marketing** notification messages. These messages will be displayed only in the notification panel in gentle notification mode.

NOTE:

The notification mode for wearables is lock screen + ringtone + vibration. Users can change the notification mode for an app in **Notifications**.

 |
| 

User engagement activities

 | 

Notifications sent by an app but not set by user, including user-involved activity notifications, reminders, game prompts, and service messages.

 |
| 

Product promotions

 | 

Notifications used to promote products, including discounts, lowest prices, sales, buy-one-get-one-free offers, rebates, coupons, vouchers, and red envelope giveaways.

 |

## Notification Message Frequency Control Rules

Based on the [message classification standards](#section1924971516101), Push Kit classifies notification messages into the following categories: **service and communication** and **news and marketing**. Push Kit provides different frequency control rules for the two types of notification messages.

-   Service and communication messages are subject to frequency control. The message sending frequency will be regulated according to the service scenario and network traffic. In cases where message sending is unnecessary or unreasonable, frequency limits will be applied For details about frequency control, please refer to [Message Frequency Control](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-msg-freq-control).
-   The daily push upper limit of news and marketing messages is controlled by app category. The following table lists the details.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/IEmLiRTXRcqK-XVUh6oZxQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062116Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=47231EB34091542B8A82572043DE3CCC24BA0C99AC729533136E1DFDDBAAF94F)

-   For details about app categories, please refer to [Categorization](https://developer.huawei.com/consumer/en/doc/50103).
-   The daily limit is defined on a natural day basis.
-   If your app does not belong to any category below or you have not applied for the self-classification permission, the daily push limit of your app per device is 2 messages by default.
-   To prevent frequency control on messages during debugging, you are advised to send test messages in this phase. For details, please refer to [Message Frequency Control](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-msg-freq-control).

| 
**Level-2 Category**

 | 

**Level-3 Category**

 | 

**Daily Push Upper Limit per App per Day (Unit: Messages)**

 |
| :-- | :-- | :-- |
| 

News & reading

 | 

News (These apps need to obtain the _Internet News Information Service License_ in advance.)

 | 

5

 |
| 

Books, magazines, audiobooks, anime & comics, humor, sports, and Classification Information

 | 

2

 |
| 

Puzzle & casual

 | 

All

 | 

2

 |
| 

Strategy

 | 

All

 | 

2

 |
| 

Sports

 | 

All

 | 

2

 |
| 

Card & board games

 | 

All

 | 

2

 |
| 

Action

 | 

All

 | 

2

 |
| 

Role-playing

 | 

All

 | 

2

 |
| 

Entertainment

 | 

All

 | 

2

 |
| 

Tools

 | 

All

 | 

2

 |
| 

Social

 | 

All

 | 

2

 |
| 

Education

 | 

All

 | 

2

 |
| 

Photo & video

 | 

All

 | 

2

 |
| 

Food & drink

 | 

All

 | 

2

 |
| 

Navigation & transport

 | 

All

 | 

2

 |
| 

Travel

 | 

All

 | 

2

 |
| 

Shopping

 | 

All

 | 

2

 |
| 

Business

 | 

All

 | 

2

 |
| 

Kids

 | 

All

 | 

2

 |
| 

Finance

 | 

All

 | 

2

 |
| 

Health & fitness

 | 

All

 | 

2

 |
| 

Lifestyle

 | 

All

 | 

2

 |
| 

Cars

 | 

All

 | 

2

 |
| 

Personalized themes

 | 

All

 | 

2

 |

## Application Procedure

**Application Principles**

Before applying for notification message self-classification, please ensure a thorough understanding of the [Message Classification Mode](#section12819174063215) and verify that your app meets the following requirements:

1.  Push messages of your app are classified based on criteria that align with the [Message Classification Standards](#section1924971516101).
2.  Your app complies with the [HUAWEI Push Service Agreement](https://developer.huawei.com/consumer/en/doc/app/10134) and other related regulations, and has no violation record.
3.  Your message types align with the classification rules, and the message content example is consistent with the message type description.

**Application Process**

1.  Sign in to [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html) and click **Development and services**. Find and click the desired project in the project list. Then, go to **Grow** > **Push Kit** > **Settings**. Select the desired app, and click **Apply** next to **Self-classification**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/wT_hq3W4RcqxncBkDZMnUA/en-us_image_0000002489360544.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062116Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=21894B783D19D36C3DFD84591D7BB88539F1555146F5FAD9C84E82961357C8D9 "Click to enlarge")
    
2.  Select message types as required and click **Next**. Then provide message examples (for subscription messages, you must also include a scenario description and screenshots) and submit the application. You can click **View progress** to check the review progress.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/1wS2ALsfQWi9BzaT6PwMkw/notice_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062116Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=60F6725CEE7BDEB8952EF952039D394ADA0C8F09B0B45DFE8B80C21F061EDF11)
    
    -   If a message type has already been approved, subsequent messages within the scope of this type do not need to be applied for again.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/9u9pf4uaS1KVWE4jIt4JYw/en-us_image_0000002489360552.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062116Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=23A3B3094725DEC3B1900A0FF3C836794B81B52FF8FF616647AAC45C2406DA46 "Click to enlarge")
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/pPN9WBjdSIKBYbq5ogLmuQ/notice_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062116Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0D53E2E3065DBEE4DA5D998553FB43AD03347380D1B2811FAD5C63452D28966C)
    
    -   The message content example must match the scenario of the message category and must not contain any marketing or advertising content. If the submitted content does not match the scenario or contains such content, penalties will be imposed in accordance with the _Push Kit Push Notification Violation Penalty Criteria_.
    -   To ensure that the reviewer fully understands your application and expedite the approval process, describe the message example and scenario in the message content example as comprehensively as possible.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/e9jyCB8FRui2zbWjurXtmQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062116Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BF429605F4AB06ABBBE155990C26D5CCF37845AD6205990DEB9A5085FB209EAA)
    
    The following message content examples are for reference only.
    
    Order & logistics message content example:
    
    Your order has been successfully placed. You can check the order details.
    
    Subscription message content example:
    
    Updates available for topic/author/event XX you have subscribed to/followed. Click to view.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/u55b-CbsTaWDNMUxIHHGgA/en-us_image_0000002489200592.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062116Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1936122A8CA1D74EC0E5D10CB735C9418F6379524884AC03BE94D4B552388C1B "Click to enlarge")
    
3.  If this is not your first application, click **New application** to apply for a new message type.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/1HaxHmwnTpmSuBIE8aiq1Q/en-us_image_0000002489360560.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062116Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=92A40F3964E1A41C20CEF785F9D13C4E8A9ADA6B28CFF114F062210D63EBF7A0 "Click to enlarge")
    
4.  The message type application review takes about five working days. You can click **Details** next to **Self-classification** to view the approved message types. You can also click **Application records** to view message types you have applied for.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/JcE6qYP7RVWQ8vYjpfPH6Q/en-us_image_0000002489200596.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062116Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4E63264BDABF545B59B78704E7BC8BA3FBFDCE87C57D26353F12AD8C4B49075A "Click to enlarge")
    
    You can click **Application records** to view the message types you have applied for, and view, edit, and delete these application records.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/05/v3/soa9PAs3SFqOgxvQmAApaA/en-us_image_0000002489360574.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062116Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A7829105F11812E4815D00661D53B1F5310D2A393944F874F1FF1F2F73703FA3 "Click to enlarge")
    
5.  Adapt the **category** field on the cloud based on the self-classification information after your application is approved. Your self-classification permission takes effect five minutes after approval.
    
    After the self-classification permission takes effect, notification messages pushed by your app will be classified based on the [category](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-scenariozed-api-request-param#section17371529101117) field that you have defined on the cloud.
    
    The value of the **category** field must contain an approved, capitalized English value of **category** defined in AppGallery Connect. An incorrect category or a category that does not comply with the classification standards will result in a violation.
    
    For details about the violations and penalties, please refer to [Push Notification Violation Penalty Criteria](../../appendixes/push-notification-violation-penalty-criteria/document.md).
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/Heskfhl4Q4yYB7wfFBSL7g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062116Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DEBA0751ED5A0CBA0C644450B67B1CAE8A98C0D1169AAD5CC264D73E3D16D728)
    
    If you have any questions about the above rules, please send an email to [hwpush@huawei.com](mailto:hwpush@huawei.com) to contact us.
    

#### Applying for the In-App Call Message Permission

This permission allows your app to display the call screen and start the voice or video call when an in-app call message arrives at a device.

This scenario is available only for communication and alarm apps that provide the in-app video and voice call function.

**Procedure**

1.  Sign in to [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html) and click **Development and services**.
2.  Find and click your project on the project list, go to **Project settings**, select your app, and go to **Manage open capabilities**. Click **Request** next to the permission for pushing in-app call messages.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/saarMrb-Sa-SPUZv7CaDtg/en-us_image_0000002507401354.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062116Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C22C614FF386AEC54C24101D6D14B269BA62629EE791A4DA7D9C250164037DF6 "Click to enlarge")
    
    In the permission application dialog box, configure your app information and upload an attachment as prompted, and click **Submit**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/J76HGN3gR5WtWGXnXBfYkg/en-us_image_0000002525422599.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062116Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C870F65711D2E49E2CCF27B383E9811F8C462D193F728F315B4025B794382DD2 "Click to enlarge")
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/OoJ3h5duQ0CdnOfUU7t2mA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062116Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C8B30E1C6493A198D54FB67DC9FE1B3F5767FA606A1CD8FA7E109C329243211E)
    
    -   When applying for the permission, upload relevant materials. For an enterprise internal app, provide a stamped proof letter issued by the served entity. For a non-internal app, provide a Value-added Telecom Business License (for B22 multi-party communication service business in China).
    -   Wearables, TVs, and PCs/2-in-1 devices do not support this permission.
    
    **Proof letter for applying for the in-app call message permission**:
    
    App name: \*\*\*
    
    App package name and app ID: \*\*\* & \*\*\*
    
    Your commitment:
    
    1\. _\*\*\* (app name)_ will use in-app call messages only in the applied scenario (video and audio call scenario).
    
    2\. The app does not prevent OS hibernation after service completion.
    
    3\. The requested in-app call message permission is used only in this app and is intended exclusively for internal use by employees of your company or organization. It will not be transferred or made available to external parties or non-affiliated employees.
    
    4\. If there are any other acts that violate the above item 1, 2, or 3, I agree that Push Kit can revoke this permission.
    
    Company XXX
    
    _YYYY-MM-DD_
    
3.  You will be redirected to the **Interaction center** page after submitting the application. Our intelligent assistant will inform you of the review progress. Usually, the review takes no more than eight working days. After exiting **Interaction center**, you can click the bubble icon in the upper right corner of AppGallery Connect to access it again.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/DA0KKXjoRoauE_fKgi5A2g/en-us_image_0000002539333149.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062116Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0F9AD23403ACCABB96D2A64C3A2036F2FC8EA068DE2AFC078171A96EBF6721DD "Click to enlarge")
    
4.  Wait for the review to complete. The permission will take effect once it is approved and you can see the permission selected for Push Kit.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/mJrCVBG6RBCKQlprDOPzwA/en-us_image_0000002507571846.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062116Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=57A0333B9ADB1FA2EE62CB55A0C6797F1375B62AF6E3FADD1CA4AB130560BF8F "Click to enlarge")
    

#### Applying for the Text-to-Speech Message Permission

When a user device receives a text-to-speech message from your app, Push Kit will start a subprocess of your app to handle the relevant service logic, for example, voice broadcast. The subprocess will be running for 10 seconds by default, within which you need to complete your service handling.

The following limitations apply to applications for text-to-speech messages:

-   This message type is available only for apps that send new order notifications to merchants and support merchant payment reception.
-   Apps cannot use text-to-speech messages to start the main app process.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/928ED9g-TkicHO98lA1nHQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062116Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2F59B4ECC0A20B60C9BDA0350B1B9C3F3173B7D71C1099F2FEEFB4075A48F68F)

-   To streamline the text-to-speech message experience, the extended notification message permission will be renamed to text-to-speech message permission starting in early January 2026. This update simplifies the integration process: you will only need to request this single permission, eliminating the previous requirement to apply for both the extended notification permission and the PLAY\_VOICE (text-to-speech message) category separately.
-   Existing services that have already obtained the extended notification permission and the PLAY\_VOICE category will continue to function without interruption. No adjustments to your code or service workflows are required.

**Procedure**

1.  Sign in to [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html) and click **Development and services**.
2.  Find and click your project on the project list, go to **Project settings**, select your app, and go to **Manage open capabilities**. Click **Request** next to the permission for pushing text-to-speech messages.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/sbVdLQmzQZS4e25BrELE3g/en-us_image_0000002533783903.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062116Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B9B15AF72A8CC917F2BF0F73EE47C9DE3671552CB3D3316721E8E94BFD9E8152 "Click to enlarge")
    
    In the permission application dialog box, configure your app information and upload an attachment as prompted, and click **Submit**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/2x-uMZ17S3u_ZRa2T8lLzA/en-us_image_0000002510912740.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062116Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8E6C5EC8391F96A3F3336AFAFE6F2F01A5D3EB0629158E75F21CAB872C291E9A "Click to enlarge")
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/pd3mMpDlT2qbiTsR4HfMYg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062116Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D5353BFD2193B75272C4AE27DCE1327CBDDB1AE6586461F1CB6DE687ADB53CC4)
    
    -   You need to upload screenshots or schematic diagrams of the voice notification UI or video recordings of voice playback.
    -   TVs do not support this permission.
    
3.  You will be redirected to the **Interaction center** page after submitting the application. Our intelligent assistant will inform you of the review progress. Usually, the review takes no more than eight working days. After exiting **Interaction center**, you can click the bubble icon in the upper right corner of AppGallery Connect to access it again.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/HS_5rzMeSkKn5juNJkTpmg/en-us_image_0000002533625721.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062116Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C81A417135FF5DDF5BC819064ECC7722F4A032D773F14A9B778031B5CE2B91EF "Click to enlarge")
    
4.  Wait for the review to complete. The permission will take effect once it is approved and you can see the permission selected for Push Kit.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/NgM7TzHtQ4OIpZNlljoQeQ/en-us_image_0000002533802489.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062116Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=519C77001841034439A5F477DEB2A482CB1101108DD8A8152E2C3C76939B231F "Click to enlarge")
    

#### Applying for the Custom Message Notification Ringtone Permission

The custom ringtone is played only when a user device receives a [notification message](../../pushing-scenario-specific-messages/pushing-a-notification-message/document.md) that carries the [sound](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-scenariozed-api-request-param#section17371529101117) field. Otherwise, the default ringtone is played. If the [soundDuration](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-scenariozed-api-request-param#section17371529101117) field also exists, the duration of the custom ringtone is subject to the parameter setting.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/gB7EQdIUSXG0EkzHIhNujQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062116Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8439A8CDE07C75D9AFB30576FBA3CCEE0FB488C91DD8C0900D5DC7AA98256ED0)

To further optimize the user experience, the custom ringtone function in Push Kit will no longer be managed as a permission control item since November 2025. You can now use this function without applying for explicit permission.

Services that have already applied for the custom ringtone permission can continue to use the function. No code or service process adjustments are required.
