# NotificationRequest

The **NotificationRequest** module provides APIs for defining the notification request.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/WNyec4jlSZ-gn12l_J4hvQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062515Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C06F314AC6802D238B9005198E329AA5FD213188F1993587D18526FDEE952283)

The initial APIs of this module are supported since API version 7. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### NotificationRequest

**System capability**: SystemCapability.Notification.Notification

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| content | [NotificationContent](../notificationcontent/document.md#notificationcontent-1) | No | No | Notification content. |
| id | number | No | Yes | Notification ID. The default value is **0**. If a notification with the same ID exists, the notification is updated. If no notification with the same ID exists, a new notification is created. |
| updateOnly18+ | boolean | No | Yes | 
Whether to update notifications only. The default value is **false**.

\- **true**: If a notification with the same ID exists, the notification is updated. If no notification with the same ID exists, the update fails and no new notification is created.

\- **false**: If a notification with the same ID exists, the notification is updated. If no notification with the same ID exists, a new notification is created.

 |
| appMessageId12+ | string | No | Yes | Unique ID carried in a notification sent by an application, which is used for notification deduplication. If an application publishes notifications with the same **appMessageId** locally or on the cloud, the device displays only one message. Repeated notifications received later will be silenced and deduplicated, and will not be displayed or notified. The deduplication flag is valid only within 24 hours after the notification is published. After 24 hours or the device is restarted, the deduplication flag becomes invalid. |
| notificationSlotType11+ | [notificationManager.SlotType](../../ohos-notificationmanager-notificationmanager/document.md#slottype) | No | Yes | Notification slot type. The default value is **OTHER\_TYPES**. The notification reminder mode varies depending on the notification slot type. |
| notificationFlags8+ | [NotificationFlags](../notificationflags/document.md) | No | Yes | Notification reminder mode. This parameter is left empty by default. |
| isAlertOnce | boolean | No | Yes | 

Whether to send a notification only once when the notification is published or updated. The default value is **false**.

\- **true**: A notification is sent only when the notification is published for the first time. For subsequent update, the notification mode is changed to [LEVEL\_LOW](../../ohos-notificationmanager-notificationmanager/document.md#slotlevel).

\- **false**: A notification is sent based on the configured notification mode.

 |
| sound12+ | string | No | Yes | Name of the custom ringtone file for application notifications. This parameter is left empty by default. This file must be stored in the **resources/rawfile** directory and supports formats such as M4A, AAC, MP3, OGG, WAV, FLAC, and AMR. |
| badgeNumber9+ | number | No | Yes | 

Number of notifications displayed on the application icon. The value is accumulated. The default value is **0**.

If the value of **badgeNumber** is less than or equal to 0, the badge number is not displayed;

if the value is greater than 99, **99+** is displayed on the badge.

For example, if an application publishes three notifications, and badgeNumber is set to **2**, **0**, and **3** in sequence, the application displays **2**, **2**, and **5** accordingly.

 |
| wantAgent | [WantAgent](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-wantagent-wantagent-module/document.md) | No | Yes | Behavior intent of an application, which is triggered when a notification is clicked. This parameter is left empty by default. |
| actionButtons | Array<[NotificationActionButton](../notificationactionbutton/document.md)\> | No | Yes | Notification button. This parameter is left empty by default. A notification can contain a maximum of two buttons. Since API version 16, this capability is supported on the wearables. A notification can contain a maximum of three buttons for the wearables. |
| removalWantAgent9+ | [WantAgent](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-wantagent-wantagent-module/document.md) | No | Yes | 

Behavior intent of an application, which is triggered when a notification is removed. This parameter is left empty by default.

Currently, redirection to UIAbility is not supported. Only common events can be published (that is, the **actionType** field of [WantAgentInfo](../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/wantagent/wantagentinfo/document.md#wantagentinfo-1) is set to **4**).

 |
| tapDismissed | boolean | No | Yes | 

Whether the notification is automatically cleared when the notification carries **wantAgent** or **actionButtons**. This parameter is valid only when the notification carries **wantAgent** or **actionButtons**. The default value is **true**.

\- **true**: The current notification is automatically cleared after the notification or button is tapped.

\- **false**: The current notification is retained after the notification or button is tapped.

 |
| autoDeletedTime | number | No | Yes | 

Scheduled time for clearing a notification. If this parameter is set, the notification will be automatically cleared after the specified time. The default value is **0**.

Data format: timestamp,

in milliseconds.

For example, if a notification is to be cleared after being displayed for 3 seconds (3000 ms), you can set **new Date().getTime() + 3000** to meet this requirement.

 |
| deliveryTime | number | No | Yes | 

Time when the notification is sent. This API is automatically generated by the system.

Data format: timestamp,

in milliseconds.

 |
| label | string | No | Yes | 

Notification label. This parameter is left empty by default.

The **label** field can be used independently, or used together with ID as a notification identifier. ID is preferentially used.

If the label is not empty when a notification is published, you need to specify the label when updating or deleting the notification.

 |
| smallIcon | [image.PixelMap](../../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md) | No | Yes | Small notification icon. This parameter is left empty by default. The total number of the icon pixel bytes cannot exceed 192 KB (which is obtained through [getPixelBytesNumber](../../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md#getpixelbytesnumber7)). The recommended icon size is 128 × 128 pixels. The display effect depends on the device capability and notification center UI style. |
| largeIcon | [image.PixelMap](../../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md) | No | Yes | Large notification icon. This parameter is left empty by default. The total number of the icon pixel bytes cannot exceed 192 KB (which is obtained through [getPixelBytesNumber](../../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md#getpixelbytesnumber7)). The recommended icon size is 128 × 128 pixels. The display effect depends on the device capability and notification center UI style. |
| groupName8+ | string | No | Yes | Group to which a notification belongs. If the group names of different notifications are the same, these notifications are displayed in a group. This parameter is left blank by default. |
| template8+ | [NotificationTemplate](../notificationtemplate/document.md) | No | Yes | Notification template. This parameter is left empty by default. |
| extraInfo | {\[key: string\]: any} | No | Yes | Extended parameters, used to provide custom services for applications. This parameter is left blank by default. |
| slotType(deprecated) | [notification.SlotType](../../apis-no-longer-maintained/ohos-notification-notification/document.md#slottype) | No | Yes | 

Notification slot type. The default value is **OTHER\_TYPES**.

This attribute is supported since API version 7 and deprecated since API version 11. You are advised to use **notificationSlotType** instead.

 |
| hashCode | string | Yes | Yes | Unique ID of the notification. |
| creatorBundleName | string | Yes | Yes | Name of the application that creates the notification. |
| creatorUid | number | Yes | Yes | UID of the application that creates the notification. |
| creatorPid | number | Yes | Yes | PID used for creating the notification. |
| creatorUserId8+ | number | Yes | Yes | ID of the user who creates the notification. |
| isOngoing | boolean | No | Yes | Not supported currently. |
| isUnremovable | boolean | No | Yes | Not supported currently. |
| color | number | No | Yes | Background color of the notification. Not supported currently. |
| colorEnabled | boolean | No | Yes | Whether the notification background color can be enabled. Not supported currently. |
| isStopwatch | boolean | No | Yes | Whether to display the stopwatch. Not supported currently. |
| isCountDown | boolean | No | Yes | Whether to display the countdown time. Not supported currently. |
| isFloatingIcon | boolean | No | Yes | Whether the notification is displayed as a floating icon in the status bar. Not supported currently. |
| distributedOption8+ | [DistributedOptions](#distributedoptions8) | No | Yes | Distributed notification options. Not supported currently. |
| badgeIconStyle | number | No | Yes | Notification badge type. Not supported currently. |
| showDeliveryTime | boolean | No | Yes | Whether to display the time when the notification is delivered. Not supported currently. |

#### DistributedOptions8+

Describes options for cross-device notifications. Not supported currently.

**System capability**: SystemCapability.Notification.Notification

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| isDistributed | boolean | No | Yes | 
Whether cross-device notifications are supported. The default value is **true**.

\- **true**: cross-device notifications are supported.

\- **false**: cross-device notifications are not supported.

 |
| supportDisplayDevices | Array<string> | No | Yes | List of the devices to which the notification can be synchronized. |
| supportOperateDevices | Array<string> | No | Yes | List of the devices on which the notification can be opened. |
