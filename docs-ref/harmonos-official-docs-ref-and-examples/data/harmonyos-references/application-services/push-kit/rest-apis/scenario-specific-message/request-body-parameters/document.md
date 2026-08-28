# Request Body Parameters

#### pushOptions

| 
Parameter

 | 

Mandatory

 | 

Type

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

testMessage

 | 

No

 | 

Boolean

 | 

Indicates whether a message is a test message. The options are as follows:

-   **false** (default): formal message
-   **true**: test message

NOTE:

When **testMessage** is set to **true**, a maximum of 1000 test messages can be pushed for a single project, and a maximum of 10 tokens can be carried in each push message. Please note that the quantity (1000) here indicates the number of requests successfully sent by the REST API, but not necessarily the number of messages that successfully reach the devices.

Only one token can be carried each time a widget update message is pushed.

 |
| 

ttl

 | 

No

 | 

Integer

 | 

Message cache duration, in seconds. When a user device is offline, the Push Kit server caches messages. If the user device goes online within the message cache duration, the messages are delivered. Otherwise, the messages are discarded. The default value is **86400** (1 day), and the maximum value is **1296000** (15 days).

NOTE:

When pushing an in-app call message or pushing a notification message or text-to-speech message for a VoIP call, you are advised to set **ttl** to a duration within 30 to 60 seconds.

 |
| 

biTag

 | 

No

 | 

String

 | 

Tag of a message in a batch delivery task. The tag is returned to the app server when Push Kit sends the [message receipt](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/push-msg-receipt). The value contains a maximum of 64 bytes.

 |
| 

receiptId

 | 

No

 | 

String

 | 

Unique receipt ID that associates with the receipt URL and configuration of the downlink message. You can find the receipt ID in [Setting Receipt Parameters](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/push-msg-receipt#section462935643010).

 |
| 

collapseKey

 | 

No

 | 

Integer

 | 

Mode for the Push Kit server to cache messages sent to an offline device. These cached messages will be delivered once the device goes online again. The options are as follows:

-   **\-1** (default): All messages are cached.
-   **0-100**: message cache group ID. Messages are cached by group. In each group, only the latest message can be cached for each app.

For example, if you send 10 messages and set **collapseKey** to **1** for the first five messages and to **2** for the rest, the latest message whose value of **collapseKey** is **1** and the latest message whose value of **collapseKey** is **2** are sent to the user after the user's device goes online.

NOTICE:

The **collapseKey** parameter is valid only for messages whose **push-type** is set to one of the following values:

**0**: notification message

**2**: text-to-speech message

 |

#### target

| 
Parameter

 | 

Mandatory

 | 

Type

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

token

 | 

Yes

 | 

Array \[String\]

 | 

Token used to push messages to target users.

**Example**:

{
  "token": \["MAMzL\*\*\*\*\*\*\*"\]
}

NOTICE:

Only one token can be carried each time a widget update message is sent. In other scenarios, a maximum of 1000 tokens can be carried each time a message is sent.

 |

#### AlertPayload (Notification Message)

For details about the request body example, please refer to [Notification Message](../request-examples/document.md#section146950125107).

| 
Parameter

 | 

Mandatory

 | 

Type

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

notification

 | 

Yes

 | 

[Notification](#section17371529101117) Object

 | 

Notification message structure. For details, please refer to [Notification](#section17371529101117).

 |

## Notification

| 
Parameter

 | 

Mandatory

 | 

Type

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

category

 | 

Yes

 | 

String

 | 

Notification message type. To use this parameter, you need to apply for the message self-classification permission by referring to [Message Self-Classification](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/push-apply-right#section16708911111611). The notification message type affects the message display and notification modes. The options are as follows:

**Service and communication**

-   **IM**: instant messaging
-   **VoIP**: voice or video call invitation
-   **MISS\_CALL**: missed call notification
-   **SUBSCRIPTION**: subscription
-   **TRAVEL**: travel
-   **HEALTH**: health
-   **WORK**: work reminder
-   **ACCOUNT**: account change
-   **EXPRESS**: order & logistics
-   **FINANCE**: finance
-   **DEVICE\_REMINDER**: device reminder
-   **MAIL**: email
-   **PLAY\_VOICE**: voice broadcast

NOTICE:

The **PLAY\_VOICE** type can be used for sending only text-to-speech messages whose **push-type** is **2**.

The option **2** of **push-type** indicates a text-to-speech message.

**News and marketing**

-   **MARKETING**: news, content recommendation, social media feeds, product promotion, financial news, life news, survey, function recommendation, and operational activities (the content is only marked but message sending will not be accelerated).

NOTE:

-   If you need to send only MARKETING messages, you do not need to apply for the message self-classification permission. The frequency control policy for MARKETING messages is different from that for other types of notification messages. For details, please refer to [Notification Message Frequency Control Rules](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/push-apply-right#section1128516504398). If frequency control is triggered, rectify the fault by referring to the [frequency control FAQ](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/push-faq-5).

 |
| 

title

 | 

Yes

 | 

String

 | 

Notification message title. (Note the message body size limits. For details, please refer to [Restrictions](../function/document.md#section114731924131418).)

 |
| 

body

 | 

Yes

 | 

String

 | 

Notification message content. (Note the message body size limits. For details, please refer to [Restrictions](../function/document.md#section114731924131418).)

 |
| 

image

 | 

No

 | 

String

 | 

URL of the large icon on the right of a notification. The URL must use the HTTPS protocol. (Note the message body size limits. For details, please refer to [Restrictions](../function/document.md#section114731924131418).)

NOTE:

-   Wearables do not support the large icon style on the right.
-   The supported image formats are PNG, JPG, JPEG, and BMP. It is recommended that the image width x height be less than 128 x 128 pixels. Images larger than 49,152 pixels will not be displayed.

 |
| 

style

 | 

No

 | 

Integer

 | 

Style of a notification message. The options are as follows:

-   **0** (default): common notification
-   **1**: large text
-   **3**: multi-line text (For details about the application scenario, see the [guide](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/push-send-alert#section77234163220).)

NOTICE:

-   The large text style (**style=1**) will be discarded. You are advised to use the common notification style (**style=0**).
-   Wearables do not support the large text style or multi-line text style.

 |
| 

bigTitle

 | 

No

 | 

String

 | 

Title of a notification in the large text style. This parameter is mandatory when **style** is set to **1**. After **bigTitle** is specified, the value of **bigTitle** instead of that of **title** will be displayed in the notification panel. (Note the message body size limits. For details, please refer to [Restrictions](../function/document.md#section114731924131418).)

NOTICE:

-   This parameter will be discarded. You are advised to use the **title** parameter.
-   Wearables do not support the large text style.

 |
| 

bigBody

 | 

No

 | 

String

 | 

Content of a notification in the large text style. This parameter is mandatory when **style** is set to **1**. After **bigBody** is specified, the value of **bigBody** instead of that of **body** will be displayed in the notification panel. (Note the message body size limits. For details, please refer to [Restrictions](../function/document.md#section114731924131418).)

NOTICE:

-   This parameter will be discarded. You are advised to use the **body** parameter.
-   Wearables do not support the large text style.

 |
| 

notifyId

 | 

No

 | 

Integer

 | 

Unique notification ID of a message. If a message does not contain the ID or the ID is **\-1**, Push Kit will generate a unique ID for the message. Different notification messages can use the same notification ID, so that new messages can overwrite old messages. This parameter is mandatory if the message may need to be recalled later, and the value range is \[0, 2147483647\]. For details, please refer to [Message Recall](../../message-recall/document.md).

 |
| 

appMessageId

 | 

No

 | 

String

 | 

Unique ID of an app message. If a message does not contain the ID, no value will be assigned to **appMessageId** by default. The value is a string of 1–64 characters, including uppercase letters, lowercase letters, digits, spaces, and the following special characters: + / = - \_

NOTICE:

-   When multiple app messages with the same **appMessageId** are received through multiple channels (Push Kit, Near Field Communications, app-initiated data fetch from the cloud, or local notification sending), the target device displays only the earliest message within the validity period (24 hours by default).
-   **notifyId** is used as the basis for overwriting old messages with new messages. However, if two messages have the same **notifyId** and same **appMessageId**, the old message will be displayed.

 |
| 

profileId

 | 

No

 | 

String

 | 

Anonymous identifier of an account in the app's account system. The value contains a maximum of 64 characters.

 |
| 

inboxContent

 | 

No

 | 

Array \[String\]

 | 

Content of a notification in the multi-line text style. This parameter is mandatory when **style** is set to **3**. A message supports a maximum of three lines of text, and each line can contain up to 1024 characters, with an ellipsis (...) indicating truncated content.

**Example**:

"inboxContent": \[
  "1. Message styles",
  "2. Message reminder and display modes",
  "3. Support notification message localization"
\]

NOTICE:

Wearables do not support the multi-line text style.

 |
| 

clickAction

 | 

Yes

 | 

[ClickAction](#section152462191216) Object

 | 

Action to be triggered upon message tapping. For details, please refer to [ClickAction](#section152462191216).

 |
| 

badge

 | 

No

 | 

[Badge](#section266310382145) Object

 | 

Badge of a notification message. For details, please refer to [Badge](#section266310382145). If this parameter is not set, the app will not display the badge if no badge exists before, and the badge number remains unchanged if a badge exists.

**Example**:

{
  "badge": { "addNum": 1 }
}

NOTICE:

Wearables and TVs do not support the notification badge style.

 |
| 

sound

 | 

No

 | 

String

 | 

Custom ringtone. The ringtone file specified here must be stored in the **/resources/rawfile** path of the app. For example, the value **alert.mp3** corresponds to the **/resources/rawfile/alert.mp3** file of the app on the device. The ringtone file format can be MP3, WAV, or MPEG. If you do not set this parameter, the default ringtone will be used.

If a request does not contain the **soundDuration** parameter, it is recommended that the ringtone duration not exceed 30 seconds. Any portion exceeding 30 seconds will be truncated. If a request contains the **soundDuration** parameter, see the description of the **soundDuration** parameter for details.

NOTICE:

Wearables, TVs, and PCs/2-in-1 devices do not support custom ringtones.

 |
| 

soundDuration

 | 

No

 | 

Integer

 | 

Custom ringtone duration. The **soundDuration** parameter must be used together with the **sound** parameter, and takes effect only when a request contains the **sound** parameter. The value can contain only digits. The value range is \[1, 60\], in seconds.

The custom ringtone specified by the **sound** parameter will be played until the duration reaches the value of **soundDuration**. If the duration of the custom ringtone is shorter than the value of **soundDuration**, it will loop until the specified duration is reached.

 |
| 

foregroundShow

 | 

No

 | 

Boolean

 | 

Indicates whether to display notification messages when an app is running in the foreground. The options are as follows:

-   **true** (default value): Notification messages are displayed no matter whether the app is running in the foreground or background. In this case, [receiveMessage](../../../arkts-apis/pushservice/document.md#section125883044911) will not be triggered to receive messages.
-   **false**: Notification messages are displayed only when the app is running in the background. When the app is running in the foreground, even though notification messages are not displayed, the app can receive notification messages through [receiveMessage](../../../arkts-apis/pushservice/document.md#section125883044911) and complete service processing accordingly. For details, please refer to [notification message processing when the app is running in the foreground](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/push-send-alert#section99251359545).

 |

## ClickAction

| 
Parameter

 | 

Mandatory

 | 

Type

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

actionType

 | 

Yes

 | 

Integer

 | 

Action to be triggered upon message tapping. The options are as follows:

**0**: open the app home page

**1**: open a custom app page

**3**: delete a notification message

**5**: open the dialer screen

The value of **actionType** varies depending on the scenario. For details, please refer to [Actions Upon Message Tapping in Different Scenarios](#section1513717610141).

 |
| 

action

 | 

No

 | 

String

 | 

Action corresponding to the ability of an in-app page. When **actionType** is set to **1**, either **uri** or **action** must be set. If the page path corresponding to **action** does not exist, the app home page is displayed by default.

For details about how to set **action**, please refer to [Opening an In-app Page upon Message Tapping](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/push-send-alert#section8794131614597).

 |
| 

uri

 | 

No

 | 

String

 | 

URI corresponding to the ability of an in-app page. For details about the internal structure of a **uri** object, please refer to [skills](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/module-configuration-file#skills). When **actionType** is set to **1**, either **uri** or **action** must be set. If there are multiple abilities, set **action** or **uri** for each ability. The **action** parameter is preferentially used to search for the corresponding in-app page.

For details about how to set **uri**, please refer to [Opening an In-app Page upon Message Tapping](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/push-send-alert#section8794131614597).

 |
| 

data

 | 

No

 | 

Object

 | 

Data transferred to an app upon message tapping. The value is a JSON object. (Note the message body size limits. For details, please refer to [Restrictions](../function/document.md#section114731924131418).)

When **actionType** is set to **5**, **data** is mandatory. The value is in **{"tel": "_xxx_"}** format, where _xxx_ is a phone number which contains a maximum of 20 characters, including the following:

-   \+ (can only be the first character)
-   \-
-   Space character
-   0–9
-   #

**Example**:

{
  "data": {
    "key1": "value1",
    "key2": "value2"
  }
}

NOTICE:

When **actionType** is set to **5**, the first character must be the plus sign (+) or a digit ranging from 0 to 9.

 |

## Actions Upon Message Tapping in Different Scenarios

| 
push-type

 | 

Parameter

 | 

Enumerated Value of **actionType**

 |
| :-- | :-- | :-- |
| 

**0** (alert message)

 | 

notification.clickAction

 | 

**0**: open the app home page

**1**: open a custom app page

 |
| 

**2** (text-to-speech message)

 | 

notification.clickAction

 | 

**0**: open the app home page

**1**: open a custom app page

 |
| 

**7** (live view)

 | 

notificationData.clickAction

 | 

**0**: open the app home page

**1**: open a custom app page

 |
| 

notificationData.extend.clickAction

 | 

**0**: open the app home page

**1**: open a custom app page

**3**: delete a notification message

**5**: open the dialer screen

NOTICE:

If a device does not support the dialer function, no live view can be created even if **actionType** is set to **5**.

 |

## Badge

| 
Parameter

 | 

Mandatory

 | 

Type

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

addNum

 | 

No

 | 

Integer

 | 

Increment to the badge number, which is an integer ranging from 1 to 99.

NOTE:

-   Suppose an app currently has _N_ unread messages. If **addNum** is set to **3**, the number displayed on the app badge increases by 3 each time a message that contains **addNum** is received, that is, the number equals _N_ + 3. (If the sum of _N_ + 3 is greater than 99, **99+** will be displayed on the app badge.)
-   If **addNum** is not set, the default value **0** is used, and the number displayed in the app badge does not increase.

 |
| 

setNum

 | 

No

 | 

Integer

 | 

Badge number, which is an integer ranging from 0 to 99. This is the actual number displayed in the app badge.

NOTE:

The priority of **setNum** is higher than that of **addNum**.

-   If **setNum** is not passed, **addNum** will be used.
-   If **setNum** is greater than or equal to 0, **setNum** is passed and will be used. The notification will not contain the **addNum** parameter.

 |

#### ExtensionPayload (Text-to-Speech Message)

For details about the request body example, please refer to [Text-to-Speech Message](../request-examples/document.md#section127381221110).

| 
Parameter

 | 

Mandatory

 | 

Type

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

notification

 | 

Yes

 | 

[Notification](#section17371529101117) Object

 | 

Notification message structure. For details, please refer to [Notification](#section17371529101117).

NOTICE:

The **notification.category** parameter is mandatory and must be set to **PLAY\_VOICE**. Before sending a text-to-speech message, [apply for the text-to-speech message permission](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/push-apply-right#section159981112245).

 |
| 

extraData

 | 

Yes

 | 

String

 | 

Extra data of the text-to-speech message. (Note the message body size limits. For details, please refer to [Restrictions](../function/document.md#section114731924131418).)

For details about how to obtain **extraData**, please refer to [Sample Code](https://gitcode.com/harmonyos_samples/push-kit-sample-code-clientdemo-arkts/blob/master/entry/src/main/ets/abilities/RemoteNotificationExtAbility.ets).

 |

#### FormUpdatePayload (Widget Update Message)

For details about the request body example, please refer to [Widget Update Message](../request-examples/document.md#section27613181115).

| 
Parameter

 | 

Mandatory

 | 

Type

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

formId

 | 

Yes

 | 

Long

 | 

Instance ID of a service widget, which is obtained when [onAddForm](../../../../../application-framework/form-kit/arkts-apis/ohos-app-form-formextensionability-formextensionability/document.md#formextensionabilityonaddform) is called (a user adds the widget to the home screen). Note that the maximum value of **formId** generated by a device is **2^31-1**, and the maximum value of **formId** you can set is **2^63-1**.

 |
| 

version

 | 

Yes

 | 

Integer

 | 

Version number of a widget update message. The value ranges from **0** to **2^31-1**.

-   The version number of a new widget update message must be greater than that of the current widget update message. Otherwise, the update fails.
-   If the version number of a new widget update message is **0**, the widget update version number is reset and this widget update is still valid. The version number of the next widget update message must be greater than 0.

 |
| 

images

 | 

No

 | 

Array \[[FormImage](#section13251213192210) Object\]

 | 

Image data of a service widget, which is an array of objects. For details, please refer to [FormImage](#section13251213192210). Currently, the array can contain only one object.

**Example**:

{
  "images": \[{
    "keyName": "icon",
    "url": "https://xxx.png",
    "require": 1
  }\]
}

 |
| 

moduleName

 | 

Yes

 | 

String

 | 

Module name of a service widget.

Value of [name](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/module-configuration-file#tags-in-the-configuration-file) in the **module** section in **src/main/module.json5** at the module level.

 |
| 

formName

 | 

Yes

 | 

String

 | 

Name of a service widget.

The data comes from the value of **name** in the configuration of a widget under the **forms** section in the widget configuration file in **src/main/resources/base/profile** at the module level. For details, please refer to the [guide](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/push-form-update#li29441751145417).

 |
| 

abilityName

 | 

Yes

 | 

String

 | 

Ability name of a service widget.

Ability name of the service widget in the [extensionAbilities](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/module-configuration-file#extensionabilities) section in **src/main/module.json5** at the module level.

 |
| 

formData

 | 

Yes

 | 

Object

 | 

Service data of the service widget to be updated, in key-value format.

**Example**:

{
  "formData": {
    "content": "newContent"
  }
}

The data comes from the declarative paradigm component name in the widget page file in **src/main/ets/widgets** at the module level. For details, please refer to the [guide](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/push-form-update#li29441751145417).

NOTICE:

-   The key in **formData** cannot start with **datashareproxy://**.
-   If the value in **formData** is of the numeric type, the value cannot exceed **2^53-1**.
-   The value in **formData** cannot be **null**.

 |

## FormImage

| 
Parameter

 | 

Mandatory

 | 

Type

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

keyName

 | 

No

 | 

String

 | 

Image key. The value must be different from the key of the custom variable data in **formData**.

The data comes from the image component name in the widget page file in **src/main/ets/widgets** at the module level. For details, please refer to the [guide](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/push-form-update#li29441751145417).

 |
| 

url

 | 

No

 | 

String

 | 

Image download URL. The URL must use the HTTPS protocol. (Note the message body size limits. For details, please refer to [Restrictions](../function/document.md#section114731924131418).)

NOTICE:

The supported image formats are PNG, JPG, and JPEG. The image size cannot exceed 512 KB. The image width x height must be less than 12,800 pixels.

 |
| 

require

 | 

No

 | 

Integer

 | 

Image-based widget update policy. The options are as follows:

-   **1** (default): If an image fails to be downloaded, the widget will not be updated.
-   **0**: If an image fails to be downloaded, only the text of the service widget will be updated.

 |

#### BackgroundPayload (Background Message)

For details about the request body example, please refer to [Background Message](../request-examples/document.md#section17319203139).

| 
Parameter

 | 

Mandatory

 | 

Type

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

extraData

 | 

Yes

 | 

String

 | 

Data transferred to an app. (Note the message body size limits. For details, please refer to [Restrictions](../function/document.md#section114731924131418).)

Push Kit checks whether the app is in the foreground. If so, Push Kit transfers the data to the target app. If not, Push Kit caches the data or silently writes the data to the app cache.

For details about how to obtain **extraData**, please refer to [Sample Code](https://gitcode.com/harmonyos_samples/push-kit-sample-code-clientdemo-arkts/blob/master/entry/src/main/ets/abilities/RemoteNotificationExtAbility.ets).

 |
| 

proxyData

 | 

No

 | 

String

 | 

Indicates whether to use the data proxy to silently write data to the app cache when the app process is not in the foreground. To use the data proxy, you must pass **ENABLE**. If you do not want to enable the proxy to write data, do not set this parameter in the message body.

 |

#### LiveViewPayload (Live View Message)

For details about the live view request example, please refer to [Live View Creation Message](../request-examples/document.md#section818119510482) and [Live View Update Message](../request-examples/document.md#section771432213146).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/2ssuQHKATaytP_2e9o91Qw/notice_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062518Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0A6546B8366FD56759FA2AC903A5EFAE5ED85DA492425F1D558AA7AA1C437F24)

To ensure the timeliness of live view messages, be sure to update the live view content promptly. If a live view is not updated for more than 2 hours, the system will hide the live view display on the status bar and lock screen, but retain its display in the notification panel. If a live view is not updated for more than 4 hours, the system considers that the live view ends and clears the live view from all display entrances.

| 
Parameter

 | 

Mandatory

 | 

Type

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

activityId

 | 

Yes

 | 

Integer

 | 

Unique ID of a live view, which is generated by you. The value range is \[-2147483648, 2147483647\]. This parameter corresponds to the [id](https://developer.huawei.com/consumer/en/doc/harmonyos-references/liveveiw-liveviewmanager#section411410371767) parameter in Live View Kit.

NOTICE:

If the live view corresponding to a specific **activityId** does not exist in the scenario of updating or ending a live view, the use of this **activityId** to send live view messages will be banned for 24 hours.

 |
| 

operation

 | 

Yes

 | 

Integer

 | 

Live view message operation type. The options are as follows:

-   **0**: live view creation message. A live view can be created only when **event** is set to **FLIGHT**, **TAXI**, or **TRAIN**. For details, please refer to [Restrictions on Live View Creation](#section441214411235).
-   **1**: live view update message. (Ensure that the live view corresponding to a specific **activityId** exists.)
-   **2**: live view ending message. (Ensure that the live view corresponding to a specific **activityId** exists.)

If optional parameters are not set, do not have default values, and are not otherwise specified during live view update or ending, their previously set values are inherited by default.

 |
| 

event

 | 

Yes

 | 

String

 | 

Service scenario. The options are as follows:

-   **TAXI**: ride hailing
-   **DELIVERY**: instant delivery (takeout and fresh food)
-   **FLIGHT**: flight
-   **TRAIN**: high-speed rail/common train
-   **QUEUE**: queueing
-   **PICK\_UP**: meal pickup
-   **SCORE**: live scores
-   **RENT**: shared leasing
-   **TIMER**: timing
-   **WORKOUT**: workout
-   **NAVIGATION**: navigation

To use specific scenarios, you need to apply for corresponding permissions. For details, please refer to [Applying for the Formal Permission on Live View Kit](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/liveview-formal-authority).

NOTICE:

For a live view creation message (**operation** is set to **0**), the value of **event** must be **FLIGHT**, **TAXI**, or **TRAIN**.

 |
| 

status

 | 

No

 | 

String

 | 

Status of a live view message.

This parameter is mandatory when **operation** is set to **0** or **1** and the live view to be updated is created through the REST API.

The value range of **status** depends on the scenario. For details, please refer to [Status Value Range](#section1251014198565).

For details about how to use the placeholder **{{status}}** in the message body, please refer to [Parameters That Support Placeholders](#section111894703518). If the requirements are met, the placeholder in the parameter will be replaced with the [target value](#section1251014198565).

 |
| 

title

 | 

No

 | 

String

 | 

(Optional) Title displayed in the notification panel when the system does not support live view notifications. (Note the message body size limits. For details, please refer to [Restrictions](../function/document.md#section114731924131418).)

 |
| 

content

 | 

No

 | 

String

 | 

(Optional) Content displayed in the notification panel when the system does not support live view notifications. (Note the message body size limits. For details, please refer to [Restrictions](../function/document.md#section114731924131418).)

 |
| 

mute

 | 

No

 | 

Boolean

 | 

Indicates whether to use silent reminder for message update. The options are as follows:

-   **true** (default): silent
-   **false**: ringtone or vibration

 |
| 

version

 | 

No

 | 

Integer

 | 

Version number of a live view update notification, which is greater than or equal to 0. The version number of the live view update notification must be greater than that of the current live view notification. Otherwise, the update fails.

 |
| 

activityData

 | 

Yes

 | 

[ActivityData](#section93901138192612) Object

 | 

Detailed data of a live view notification. For details, please refer to [ActivityData](#section93901138192612).

 |

## Restrictions on Live View Creation

For details about the sample request for creating a live view, please refer to [Live View Creation Message](../request-examples/document.md#section818119510482).

1.  You can use the REST API to create live views for the following events: **FLIGHT**, **TAXI**, and **TRAIN**.
2.  Only one live view can be created for a same **activityId** value through the REST API within 12 hours.
3.  The restrictions on the layout type (**activityData.notificationData.**[type](#section7742121916279)) and mandatory parameters during live view creation for different events are as follows.
    
    | 
    Event
    
     | 
    
    Supported Layout During Creation
    
     | 
    
    Mandatory Parameters During Creation
    
     | 
    
    Mandatory Parameters for Update of a Live View Created Through the REST API
    
     |
    | :-- | :-- | :-- | :-- |
    | 
    
    FLIGHT
    
     | 
    
    Left-right text template
    
     | 
    
    [status](#section66881469306)
    
    activityData.notificationData.[keywords](#section7742121916279)
    
     | 
    
    [status](#section66881469306)
    
     |
    | 
    
    TAXI
    
     | 
    
    Progress visualization
    
    Emphasized text template
    
    Left-right text template
    
    Live scores
    
     | 
    
    [status](#section66881469306)
    
     | 
    
    [status](#section66881469306)
    
     |
    | 
    
    TRAIN
    
     | 
    
    Left-right text template
    
     | 
    
    [status](#section66881469306)
    
    activityData.notificationData.[keywords](#section7742121916279)
    
     | 
    
    [status](#section66881469306)
    
     |
    
4.  No matter which layout (specified by activityData.notificationData.[type](#section7742121916279)) is used, you need to add the placeholder **{{status}}** of **[status](#section66881469306)** in the [parameters that support placeholders](#section111894703518) at least once. If the [keywords](#section7742121916279) parameter in the event is mandatory, you also need to add the corresponding placeholder (see the description of [keywords](#section7742121916279)) in the [parameters that support placeholders](#section111894703518) at least once.
5.  The update of live views created through the REST API must meet the requirements of both **status** and **keywords**. For live views created using Live View Kit, the **status** and **keywords** parameters are optional when you update the live views through the REST API. However, if you choose to set the parameters, ensure that the settings meet their requirements.

## Parameters That Support Placeholders

| 
Layout

 | 

Parameter

 |
| :-- | :-- |
| 

Progress visualization

Live scores

 | 

activityData.notificationData.[contentTitle](#section7742121916279)

activityData.notificationData.[contentText](#section7742121916279).[text](#section33109121415)

activityData.notificationData.[extend](#section7742121916279).[text](#section15169131522812)

 |
| 

Emphasized text template

 | 

activityData.notificationData.[contentTitle](#section7742121916279)

activityData.notificationData.[contentText](#section7742121916279).[text](#section33109121415)

activityData.notificationData.[extend](#section7742121916279).[text](#section15169131522812)

activityData.notificationData.[singleTextBlock](#section7742121916279).[firstLine](#section4853202219519)

activityData.notificationData.[singleTextBlock](#section7742121916279).[secondLine](#section4853202219519)

 |
| 

Left-right text template

 | 

activityData.notificationData.[contentTitle](#section7742121916279)

activityData.notificationData.[contentText](#section7742121916279).[text](#section33109121415)

activityData.notificationData.[extend](#section7742121916279).[text](#section15169131522812)

activityData.notificationData.[firstTextBlock](#section7742121916279).[firstLine](#section194733293615)

activityData.notificationData.[firstTextBlock](#section7742121916279).[secondLine](#section194733293615)

activityData.notificationData.[lastTextBlock](#section7742121916279).[firstLine](#section1714025575)

activityData.notificationData.[lastTextBlock](#section7742121916279).[secondLine](#section1714025575)

 |

## Value Range of Status

| 
Event

 | 

Value of status

 | 

Content to Replace the {{status}} Placeholder in the Message Body

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

**FLIGHT**

 | 

DEPART

 | 

Scheduled departure

 | 

A reminder will be sent a certain time prior to the scheduled flight departure.

 |
| 

WAITING\_FOR\_CHECK\_IN

 | 

Not checked in

 | 

The user has not checked in for the flight.

 |
| 

CHECKED\_IN

 | 

Checked in

 | 

The flight is checked in.

 |
| 

PASSED\_SECURITY\_CHECK

 | 

Security check completed

 | 

The user has completed security check.

 |
| 

START\_BOARDING

 | 

Boarding started

 | 

Boarding has started for the flight.

 |
| 

URGE\_BOARDING

 | 

Last boarding call

 | 

This is the last boarding call for the flight.

 |
| 

BOARDED

 | 

Aboard

 | 

The user is aboard the plane.

 |
| 

END\_BOARDING

 | 

Boarding finished

 | 

The flight has finished boarding.

 |
| 

ABOUT\_TO\_TAKE\_OFF

 | 

About to take off

 | 

The flight is about to take off.

 |
| 

TAKEN\_OFF

 | 

Taken off

 | 

Users who have followed a flight are notified that the flight has taken off.

 |
| 

ARRIVED

 | 

Arrived

 | 

The flight has arrived.

 |
| 

TRANSFER

 | 

Connecting flight reminder

 | 

Reminder to notify the user of the next flight's information upon arrival at their transfer airport.

You are advised to create a new live view for a different flight.

 |
| 

NEW\_ITINERARY

 | 

Next flight started

 | 

Reminder to notify the user that the next flight has started.

 |
| 

GATE\_CHANGE

 | 

Boarding gate change

 | 

The boarding gate has changed.

 |
| 

FLIGHT\_DELAY

 | 

Delay

 | 

The flight is delayed.

 |
| 

FLIGHT\_CANCEL

 | 

Cancellation

 | 

The flight is canceled.

 |
| 

FLIGHT\_DIVERSION

 | 

Diversion

 | 

The flight is diverted to another airport.

 |
| 

FLIGHT\_RETURN

 | 

Return

 | 

The flight has returned.

 |
| 

**TAXI**

 | 

CALLING

 | 

Searching for a driver

 | 

The system is searching for a driver.

 |
| 

ABOUT\_TO\_BEGIN

 | 

Ride about to start

 | 

The ride is about to start. This status is used in scheduled ride-hailing and hitchhiking scenarios to remind the user a certain time before the ride starts.

 |
| 

DRIVER\_ON\_THE\_WAY

 | 

Driver on the way

 | 

The driver is on the way.

 |
| 

DRIVER\_ARRIVE

 | 

Driver arrived

 | 

The driver has arrived at the pickup point.

 |
| 

HEADING\_TO\_DESTINATION

 | 

Heading to the destination

 | 

The vehicle is heading to the destination. If an order has multiple waypoints, this status can be used continuously until the trip is completed.

 |
| 

COMPLETED

 | 

Trip completed

 | 

The trip is completed.

 |
| 

RE\_CALLING

 | 

Searching for a new driver

 | 

The system is searching for a new driver. This status is used when the order is reassigned or the driver cancels the order.

 |
| 

CANCELED

 | 

Order canceled

 | 

The order is canceled. Orders canceled by users or due to insufficient driver availability in the area are both categorized as canceled orders.

 |
| 

**TRAIN**

 | 

DEPART

 | 

Scheduled departure

 | 

A reminder will be sent to the user a certain period of time before the scheduled train departure.

 |
| 

PASSED\_SECURITY\_CHECK

 | 

Security check completed

 | 

The user has completed security check.

 |
| 

TICKET\_CHECK

 | 

Boarding reminder

 | 

The train has started boarding.

 |
| 

CHECKED

 | 

Boarding completed

 | 

The user is aboard the train.

 |
| 

CHECK\_IN\_CLOSED

 | 

Boarding finished

 | 

The train has finished boarding.

 |
| 

SET\_OFF

 | 

Departed

 | 

The train has departed.

 |
| 

HEADING\_TO\_DESTINATION

 | 

Train on the move

 | 

As the train is moving, the system can provide real-time updates on the upcoming stations and how long it will take to get there.

 |
| 

ARRIVED

 | 

Arrived

 | 

The train has arrived at the destination.

 |
| 

GATE\_CHANGE

 | 

Boarding gate change

 | 

The boarding gate has changed.

 |
| 

TRAIN\_DELAY

 | 

Train delayed

 | 

The train is delayed.

 |
| 

TRAIN\_CANCEL

 | 

Train canceled

 | 

The train is canceled.

 |

## ActivityData

| 
Parameter

 | 

Mandatory

 | 

Type

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

notificationData

 | 

Yes

 | 

[NotificationData](#section7742121916279) Object

 | 

Notification layout data. For details, please refer to [NotificationData](#section7742121916279).

 |
| 

capsuleData

 | 

No

 | 

[CapsuleData](#section12786224738) Object

 | 

Capsule layout data. For details, please refer to [CapsuleData](#section12786224738).

 |
| 

externalData

 | 

No

 | 

[ExternalData](#section1565314801014) Object

 | 

Data displayed on the cover screen of small-size foldable devices. For details, please refer to [ExternalData](#section1565314801014).

 |

## NotificationData

| 
Parameter

 | 

Mandatory

 | 

Type

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

Yes

 | 

Integer

 | 

Layout type. The options are as follows:

-   **3**: progress visualization, which is applicable to activities involving progress updates, such as takeout delivery, fresh food delivery, and ride hailing.
-   **4**: emphasized text template, which is applicable to activities that display key information such as meal pickup codes, delivery pickup codes, and license plate numbers.
-   **5**: left-right text template, which is applicable to activities involving the display of departure and arrival points, such as high-speed rail, trains, and flights.
-   **7**: live scores, which is applicable to sports and game events.

NOTICE:

When you create a live view, each [event](#section66881469306) can only use a specific layout type. For details, please refer to [Restrictions on Live View Creation](#section441214411235). When you update a live view, each [event](#section66881469306) can use any layout type.

 |
| 

keywords

 | 

No

 | 

Map<String, String>

 | 

Live view keywords. This parameter is mandatory when **operation** is set to **0** and **event** is set to one of the following values:

-   **FLIGHT**: There is only one keyword **flightNo**, indicating the flight number. The placeholder format is **{{flightNo}}**.
    
    Example:
    
    {
      "flightNo": "XX1234"
    }
    
-   **TRAIN**: There is only one keyword **trainNo**, indicating the train number. The placeholder format is **{{trainNo}}**.
    
    Example:
    
    {
      "trainNo": "GXXXX"
    }
    

For details about how to use placeholders in the message body, please refer to [Parameters That Support Placeholders](#section111894703518).

 |
| 

additionalText

 | 

No

 | 

String

 | 

Prompt information or disclaimer. This parameter is available only when **NotificationData.type** is set to **5**. (Note the message body size limits. For details, please refer to [Restrictions](../function/document.md#section114731924131418).)

 |
| 

keepTime

 | 

No

 | 

Long

 | 

Duration for storing live view notifications in the notification panel after a live view ends. The default value is **0**, indicating that the notifications are not stored. The maximum value is 3600, in seconds.

The storage period is subject to the value of this parameter carried in the live view ending message. The live view cannot be updated or ended again during the storage period.

 |
| 

contentTitle

 | 

No

 | 

String

 | 

Notification title. The value contains a maximum of 1024 characters.

When **operation** is set to **0**, this parameter is mandatory and cannot be an empty string.

 |
| 

contentText

 | 

No

 | 

Array \[[RichText](#section33109121415) Object\]

 | 

Notification content, which consists of multiple rich text sections. The total text length cannot exceed 1024 characters. If you set the text color, only one color can be specified.

When **operation** is set to **0**, this parameter is mandatory and cannot be an empty array.

 |
| 

richProgress

 | 

No

 | 

[RichProgress](#section3869231875) Object

 | 

Rich progress information. This parameter is mandatory when **type** is set to **3**. For details, please refer to [RichProgress](#section3869231875).

 |
| 

singleTextBlock

 | 

No

 | 

[SingleTextBlock](#section4853202219519) Object

 | 

Text block to be emphasized in the emphasized text template style. This parameter is mandatory when **type** is set to **4**. The text block occupies the left part of an extension area by default. For details, please refer to [SingleTextBlock](#section4853202219519).

 |
| 

firstTextBlock

 | 

No

 | 

[FirstTextBlock](#section194733293615) Object

 | 

Left text block in the multi-text-block layout. This parameter is mandatory when **type** is set to **5**. For details, please refer to [FirstTextBlock](#section194733293615).

 |
| 

lastTextBlock

 | 

No

 | 

[LastTextBlock](#section1714025575) Object

 | 

Right text block in the multi-text-block layout. This parameter is mandatory when **type** is set to **5**. For details, please refer to [LastTextBlock](#section1714025575).

 |
| 

displayHorizontalLine

 | 

No

 | 

Boolean

 | 

Indicates whether to display the dividing line of an extension area. If this parameter is not set, the dividing line is displayed by default. The options are as follows:

-   **true**: yes
-   **false**: no

NOTE:

The dividing line is displayed only when **type** is set to **5** or **7**.

 |
| 

spaceIcon

 | 

No

 | 

String

 | 

Spacing icon, which is a local resource. When **type** is set to **5**, the icon occupies the middle of an extension area.

When **operation** is set to **0**, **type** is set to **5**, and **spaceType** is not specified or is set to **0**, this parameter is mandatory and cannot be an empty string.

The value is a file name in the specified path.

Example: For the icon file **icon.png** stored in **/resources/rawfile** of the app, the value is **icon.png**.

 |
| 

spaceText

 | 

No

 | 

String

 | 

Spacing text. When **type** is set to **5**, the text occupies the middle of an extension area.

When **operation** is set to **0**, **type** is set to **5**, and **spaceType** is set to **1**, this parameter is mandatory and cannot be an empty string. (Note the message body size limits. For details, please refer to [Restrictions](../function/document.md#section114731924131418).)

 |
| 

style

 | 

No

 | 

Integer

 | 

Left-right text style type. The options are as follows:

**0**: emphasized

**1**: balanced

NOTE:

If the **style** parameter is not passed during message creation, the emphasized style will be used by default.

 |
| 

spaceType

 | 

No

 | 

Integer

 | 

Spacing type. The options are as follows:

**0**: icon

**1**: text

NOTE:

If the **spaceType** parameter is not passed during message creation, the spacing icon will be used by default.

 |
| 

extend

 | 

No

 | 

[Extend](#section15169131522812) Object

 | 

Style of an auxiliary area. This parameter is optional when there is no update. For details, please refer to [Extend](#section15169131522812).

NOTE:

-   When **type** is updated to a new layout, this parameter must be set.
-   During the live view update, if the display type of the auxiliary area is image but the image path is incorrect, the update may fail.

 |
| 

game

 | 

No

 | 

[Game](#section1134158205816) Object

 | 

Extension area of live scores. This parameter is mandatory when **type** is set to **7**. For details, please refer to [Game](#section1134158205816).

 |
| 

descPic

 | 

No

 | 

String

 | 

Description image in an extension area, which is not displayed by default. When **type** is set to **4** and the parameter is set, the image will occupy the right part of the extension area. If this parameter is not specified, the system uses the last updated image.

When **operation** is set to **0** and **type** is set to **4**, this parameter is mandatory and cannot be an empty string.

The value is a file name in the specified path.

Example: For the icon file **icon.png** stored in **/resources/rawfile** of the app, the value is **icon.png**.

 |
| 

clickAction

 | 

Yes

 | 

[ClickAction](#section152462191216) Object

 | 

Action to be triggered upon message tapping. For details, please refer to [ClickAction](#section152462191216).

 |
| 

lockScreen

 | 

No

 | 

[LiveViewLockScreen](#section1786105519115) Object

 | 

Parameters related to the lock screen immersive live view. For details, please refer to [LiveViewLockScreen](#section1786105519115).

 |
| 

weather

 | 

No

 | 

[Weather](#section831712212426) Object

 | 

Passed weather information struct. The weather will be displayed on the widget only when the weather type, weather location type, and highest and lowest temperatures are all passed. Only the left-right text template (**type** = **5**) is supported.

When a special weather type such as rain or snow is passed and the value of **backgroundType** passed to the live view widget indicates the moon-viewing flight or sunset flight, the weather background is preferentially displayed on the widget. (For details about the valid values of **backgroundType**, please refer to the enumerated values of [BackgroundType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/liveveiw-liveviewmanager#section15834105743213) in Live View Kit.) For other non-special weather types, the moon-viewing flight or sunset flight background is preferentially displayed on the widget.

 |
| 

backgroundType

 | 

No

 | 

Integer

 | 

Background type of the live view widget. Only the left-right text template (**type** = **5**) is supported. For details about the valid values, please refer to the enumerated values of [BackgroundType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/liveveiw-liveviewmanager#section15834105743213) in Live View Kit.

When the background type passed to the live view widget is the moon-viewing flight or sunset flight and a special weather type such as rain or snow (defined in [Weather](#section831712212426)) is passed, the weather background is preferentially displayed on the widget. For other non-special weather types, the moon-viewing flight or sunset flight background is preferentially displayed on the widget.

 |

## Extend

| 
Parameter

 | 

Mandatory

 | 

Type

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

No

 | 

Integer

 | 

Display type of an auxiliary area. The options are as follows:

-   **0** (default): Do not display the auxiliary area.
-   **1**: Display common text.
-   **2**: Display text in capsule mode.
-   **3**: Display an image. (The size of an auxiliary area is 44 x 44 vp. The image is scaled with its aspect ratio retained for the content to be completely displayed within the boundaries of the auxiliary area.)
-   **4**: Display an icon. (The size of an auxiliary area is 44 x 44 vp. The image is displayed with its aspect ratio retained, in a size less than or equal to the original size.)

 |
| 

text

 | 

No

 | 

String

 | 

Text information in an auxiliary area. When **type** is set to **1** or **2**, this parameter is mandatory and cannot be an empty string. (Note the message body size limits. For details, please refer to [Restrictions](../function/document.md#section114731924131418).)

 |
| 

pic

 | 

No

 | 

String

 | 

Image information in an auxiliary area. When **type** is set to **3** or **4**, this parameter is mandatory and cannot be an empty string.

The value is a file name in the specified path.

Example: For the icon file **icon.png** stored in **/resources/rawfile** of the app, the value is **icon.png**.

CAUTION:

This parameter will no longer be maintained in the near future. Please switch to the **image** parameter promptly.

 |
| 

image

 | 

No

 | 

String

 | 

Image information in an auxiliary area. When **type** is set to **3** or **4**, this parameter is mandatory and cannot be an empty string.

The value is a file name in the specified path.

Example: For the icon file **icon.png** stored in **/resources/rawfile** of the app, the value is **icon.png**.

 |
| 

clickAction

 | 

No

 | 

[ClickAction](#section152462191216) Object

 | 

Action to be triggered upon auxiliary area tapping. For details, please refer to [ClickAction](#section152462191216).

If this parameter is not specified, the auxiliary area does not support redirection.

 |

## Game

| 
Parameter

 | 

Mandatory

 | 

Type

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

host

 | 

Yes

 | 

[Team](#section169951247145919) Object

 | 

Left style of an extension area. For details, please refer to [Team](#section169951247145919).

 |
| 

guest

 | 

Yes

 | 

[Team](#section169951247145919) Object

 | 

Right style of an extension area. For details, please refer to [Team](#section169951247145919).

 |
| 

competition

 | 

Yes

 | 

[Competition](#section1797918449016) Object

 | 

Middle style of an extension area. For details, please refer to [Competition](#section1797918449016).

 |

## Team

| 
Parameter

 | 

Mandatory

 | 

Type

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

icon

 | 

No

 | 

String

 | 

Team icon in the display area. When **operation** is set to **0**, this parameter is mandatory and cannot be an empty string.

The value is a file name in the specified path.

Example: For the icon file **icon.png** stored in **/resources/rawfile** of the app, the value is **icon.png**.

 |
| 

name

 | 

No

 | 

String

 | 

Team name. When **operation** is set to **0**, this parameter is mandatory and cannot be an empty string. (Note the message body size limits. For details, please refer to [Restrictions](../function/document.md#section114731924131418).)

 |
| 

score

 | 

No

 | 

String

 | 

Live score. When **operation** is set to **0**, this parameter is mandatory and cannot be an empty string. (Note the message body size limits. For details, please refer to [Restrictions](../function/document.md#section114731924131418).)

 |

## Competition

| 
Parameter

 | 

Mandatory

 | 

Type

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

desc

 | 

No

 | 

String

 | 

Text description in the upper-middle part of an extension area. When **operation** is set to **0**, either this parameter or **richDesc** must be set. If this parameter is set, its value cannot be an empty string. (Note the message body size limits. For details, please refer to [Restrictions](../function/document.md#section114731924131418).)

 |
| 

richDesc

 | 

No

 | 

Array \[[RichText](#section33109121415) Object\]

 | 

Rich text description in the upper-middle part of an extension area. When **operation** is set to **0**, either this parameter or **desc** must be set. If this parameter is set, its value cannot be an empty array, and the concatenated result of all text in the array cannot be an empty string. (Note the message body size limits. For details, please refer to [Restrictions](../function/document.md#section114731924131418).)

 |
| 

time

 | 

No

 | 

String

 | 

Competition time in the lower-middle part of an extension area. When **operation** is set to **0**, this parameter is mandatory and cannot be an empty string. (Note the message body size limits. For details, please refer to [Restrictions](../function/document.md#section114731924131418).)

 |

## LiveViewLockScreen

| 
Parameter

 | 

Mandatory

 | 

Type

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

picture

 | 

No

 | 

String

 | 

Image displayed in a lock screen immersive live view.

The value is a file name in the specified path.

Example: For the icon file **icon.png** stored in **/resources/rawfile** of the app, the value is **icon.png**.

 |

## CapsuleData

| 
Parameter

 | 

Mandatory

 | 

Type

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

Yes

 | 

Integer

 | 

Capsule layout type. The options are as follows:

-   **1**: icon + text. The capsule displays the icon on the left and text on the right.
-   **2**: timer. The capsule displays the icon on the left and the timing text on the right.
-   **3**: progress. The capsule displays the overall progress with the icon on the left and the percentage or ratio on the right.

 |
| 

status

 | 

Yes

 | 

Integer

 | 

Display status of a live view capsule on the status bar. The options are as follows:

-   **1**: The capsule is displayed.
-   **\-1**: The capsule is not displayed.

 |
| 

icon

 | 

Yes

 | 

String

 | 

Status icon, which is a local resource. You are advised to use an 18 x 18 vp solid-color vector icon.

Example: For the icon file **icon.svg** stored in **/resources/rawfile** of the app, the value is **icon.svg**.

 |
| 

bgColor

 | 

Yes

 | 

String

 | 

Background color of a capsule. The value is in #ARGB format, with a number sign (#) and 8 hexadecimal digits.

The following colors are not supported:

-   #FF000000
-   #FFFFFFFF
-   #FFF1F3F5

 |
| 

remind

 | 

No

 | 

String

 | 

Dynamic effect of a capsule on the status bar. If this parameter is not specified, there is no special effect by default.

-   **DEFAULT**: There is no special effect.
-   **FLIP**: Preempts the capsule position. This effect can be displayed for five times at most per activity.
-   **EXPAND**: The capsule is automatically expanded into a floating card. This effect can be displayed twice at most per activity.

 |
| 

title

 | 

No

 | 

String

 | 

Main text of the capsule. The value contains a maximum of 128 characters.

This parameter is mandatory when **operation** is set to **0** and **type** is set to **1**.

When **type** is set to **1**, this parameter specifies the capsule title.

 |
| 

content

 | 

No

 | 

String

 | 

Capsule content. The value contains a maximum of 128 characters. The extended text specified by this parameter is displayed when a device has a widescreen or is in landscape orientation.

This parameter is mandatory when **operation** is set to **0** and **type** is set to **1** or **2**.

 |
| 

capsuleTimer

 | 

No

 | 

[CapsuleTimer](#section771411404914) Object

 | 

Capsule timer. For details, please refer to [CapsuleTimer](#section771411404914).

When **type** is set to **2**, this parameter is mandatory and specifies the capsule timer information.

 |
| 

progress

 | 

No

 | 

[Progress](#section16961132420417) Object

 | 

Progress information in a capsule. For details, please refer to [Progress](#section16961132420417).

When **type** is set to **3**, this parameter specifies the progress information in a capsule.

 |

## Progress

| 
Parameter

 | 

Mandatory

 | 

Type

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

max

 | 

No

 | 

Integer

 | 

Maximum progress value. The default value is **1**. The value range is \[1, 2147483647\].

 |
| 

progress

 | 

Yes

 | 

Integer

 | 

Current progress value. The value range is \[0, 2147483647\]. The value of this parameter must be less than or equal to the maximum progress value.

 |
| 

indeterminate

 | 

No

 | 

Boolean

 | 

Progress display type. The progress is displayed as a ratio by default.

-   **true**: percentage
-   **false**: ratio

 |

## SingleTextBlock

| 
Parameter

 | 

Mandatory

 | 

Type

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

firstLine

 | 

Yes

 | 

String

 | 

Text in the first line. The value contains a maximum of 128 characters and cannot be an empty string.

 |
| 

secondLine

 | 

Yes

 | 

String

 | 

Text in the second line. The value contains a maximum of 128 characters and cannot be an empty string.

 |
| 

underlineColor

 | 

No

 | 

String

 | 

Underline color of the text in the second line. The value is in #ARGB format, with a number sign (#) and 8 hexadecimal digits. If this parameter is not specified, the underline will not be displayed.

 |

## FirstTextBlock

| 
Parameter

 | 

Mandatory

 | 

Type

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

firstLine

 | 

Yes

 | 

String

 | 

Text in the first line. The value contains a maximum of 128 characters and cannot be an empty string.

 |
| 

secondLine

 | 

Yes

 | 

String

 | 

Text in the second line. The value contains a maximum of 128 characters and cannot be an empty string.

 |

## LastTextBlock

| 
Parameter

 | 

Mandatory

 | 

Type

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

firstLine

 | 

Yes

 | 

String

 | 

Text in the first line. The value contains a maximum of 128 characters and cannot be an empty string.

 |
| 

secondLine

 | 

Yes

 | 

String

 | 

Text in the second line. The value contains a maximum of 128 characters and cannot be an empty string.

 |
| 

firstLineSuperscript

 | 

No

 | 

String

 | 

Superscript in the upper right corner of the first-line text. The value is in +_x_ format, where _x_ ranges from 1 to 9. Values out of this range will not be displayed.

 |
| 

secondLineSuperscript

 | 

No

 | 

String

 | 

Superscript in the upper right corner of the second-line text. The value is in +_x_ format, where _x_ ranges from 1 to 9. Values out of this range will not be displayed.

 |

## RichProgress

| 
Parameter

 | 

Mandatory

 | 

Type

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

indicatorIcon

 | 

No

 | 

String

 | 

Progress indicator icon, which is a local resource. If this parameter is not specified, the system displays the last updated image.

When **operation** is set to **0** and **indicatorType** is set to **1** or **2**, this parameter is mandatory and cannot be an empty string.

The value is a file name in the specified path.

Example: For the icon file **icon.png** stored in **/resources/rawfile** of the app, the value is **icon.png**.

 |
| 

progress

 | 

Yes

 | 

Integer

 | 

Progress percentage. The value ranges from 0 to 100. It determines the position of the indicator in the progress bar.

 |
| 

color

 | 

No

 | 

String

 | 

Color of the progress points and node icons on the left of the progress indicator. The value is in #ARGB format, with a number sign (#) and 8 hexadecimal digits. The default color is blue.

 |
| 

bgColor

 | 

No

 | 

String

 | 

Color of the progress points and node icons on the right of the progress indicator. The value is in #ARGB format, with a number sign (#) and 8 hexadecimal digits. The default color is gray.

 |
| 

nodeIcons

 | 

No

 | 

Array \[String\]

 | 

Icon of each node in the progress bar, which is a local resource. The array length range is \[2, 5\]. If this parameter is not specified, the system uses the last updated image.

When **operation** is set to **0**, this parameter is mandatory and cannot be an empty array.

The value is a file name in the specified path.

Example: For the icon file **icon.png** stored in **/resources/rawfile** of the app, the value is **icon.png**.

 |
| 

type

 | 

No

 | 

Integer

 | 

Progress display type in an extension area. The options are as follows:

-   **0** (default): dotted line
-   **1**: common solid line
-   **2**: thick solid line

 |
| 

indicatorType

 | 

No

 | 

Integer

 | 

Display type of a small indicator icon in an extension area. The options are as follows:

-   **0** (default): The small indicator icon is not displayed.
-   **1**: The small indicator icon is displayed above the progress line.
-   **2**: The small indicator icon is displayed on the progress line.

 |

## CapsuleTimer

| 
Parameter

 | 

Mandatory

 | 

Type

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

time

 | 

No

 | 

Long

 | 

Initial value of the capsule timer, which is updated every second. The unit is millisecond (ms) and the default value is **0**.

 |
| 

countDown

 | 

No

 | 

Boolean

 | 

Indicates whether a timer is a countdown timer. The default value is **false**.

-   **false**: no
-   **true**: yes

 |
| 

pause

 | 

No

 | 

Boolean

 | 

Indicates whether a capsule timer is paused. The default value is **false**.

-   **false**: no
-   **true**: yes. A paused timer displays the time when it is paused.

 |

## ExternalData

| 
Parameter

 | 

Mandatory

 | 

Type

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

No

 | 

Integer

 | 

Template type for a cover screen. The options are as follows:

-   **0** (default): default type
-   **1**: background image

 |
| 

bgColor

 | 

No

 | 

String

 | 

Background color of a cover screen. The value is in #RGB format, with a number sign (#) and 6 hexadecimal digits. If this parameter is not specified, the default color is used.

 |
| 

bgImage

 | 

No

 | 

String

 | 

Background image of a cover screen, which is a local resource. When **type** is set to **1**, this parameter is mandatory when a live view is created and does not need to be set when the live view is not updated.

When **operation** is set to **0** and **type** is set to **1**, this parameter is mandatory and cannot be an empty string.

The value is a file name in the specified path.

Example: For the icon file **icon.png** stored in **/resources/rawfile** of the app, the value is **icon.png**.

 |
| 

title

 | 

No

 | 

String

 | 

Custom notification title on a cover screen. The value contains a maximum of 128 characters.

When **operation** is set to **0**, this parameter is mandatory and cannot be an empty string.

 |
| 

body

 | 

No

 | 

Array \[[RichText](#section33109121415) Object\]

 | 

Custom notification content on a cover screen, which consists of multiple rich text sections. The total text length cannot exceed 128 characters. If you set the text color, only one color can be specified.

When **operation** is set to **0**, this parameter is mandatory and cannot be an empty array.

 |

## RichText

| 
Parameter

 | 

Mandatory

 | 

Type

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

text

 | 

Yes

 | 

String

 | 

Text. (Note the message body size limits. For details, please refer to [Restrictions](../function/document.md#section114731924131418).)

 |
| 

foregroundColor

 | 

No

 | 

String

 | 

Text color. The value is in #ARGB format, with a number sign (#) and 8 hexadecimal digits. If **foregroundColor** is not set, the default text color **#FF000000** will be used. If **foregroundColor** is set, its values for all objects in the array must be the same.

 |

## Weather

| 
Parameter

 | 

Mandatory

 | 

Type

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

weatherType

 | 

No

 | 

Integer

 | 

Weather type. If **weatherType** is not passed or an invalid value is passed, the weather will not be displayed. For details about the valid values, please refer to the enumerated values of [WeatherType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/liveveiw-liveviewmanager#section2062895313473) in Live View Kit.

 |
| 

locationType

 | 

No

 | 

Integer

 | 

Weather location type. If **locationType** is not passed or an invalid value is passed, the weather will not be displayed. For details about the valid values, please refer to the enumerated values of [WeatherLocationType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/liveveiw-liveviewmanager#section1597237195618) in Live View Kit.

 |
| 

highTemperature

 | 

No

 | 

Integer

 | 

Highest temperature. Only Celsius is supported. The highest temperature must be less than or equal to 58°C and greater than the lowest temperature (specified by **lowTemperature**). If this parameter is not passed or an invalid value is passed, the weather will not be displayed.

 |
| 

lowTemperature

 | 

No

 | 

Integer

 | 

Lowest temperature. Only Celsius is supported. The lowest temperature must be greater than or equal to –95°C and less than the highest temperature (specified by **highTemperature**). If this parameter is not passed or an invalid value is passed, the weather will not be displayed.

 |

#### VoIPCallPayload (In-App Call Message)

For details about the request body example, please refer to [In-App Call Message](../request-examples/document.md#section299111610344).

| 
Parameter

 | 

Mandatory

 | 

Type

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

extraData

 | 

Yes

 | 

String

 | 

Data transferred to an app. The app processes related logic based on the data and displays in-app call message information. (Note the message body size limits. For details, please refer to [Restrictions](../function/document.md#section114731924131418).)

For details about how to obtain **extraData**, please refer to [Sample Code](https://gitcode.com/harmonyos_samples/push-kit-sample-code-clientdemo-arkts/blob/master/entry/src/main/ets/service/VoipCallService.ets).

 |
