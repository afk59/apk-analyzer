# NotificationSlot

The **NotificationSlot** module provides APIs for defining the notification slots. The notification reminder modes vary according to notification slots.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/BGOi814DR7ymLe-ZAAro0g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062515Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8B6C0E8E18BA5F61216FE1E19E35E70D3AA087ABE69146AC88DD0805CB4F0A0E)

The initial APIs of this module are supported since API version 7. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### NotificationSlot

**System capability**: SystemCapability.Notification.Notification

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| type(deprecated) | [notification.SlotType](../../apis-no-longer-maintained/ohos-notification-notification/document.md#slottype) | No | Yes | 
Notification slot type.

This attribute is supported since API version 7 and deprecated since API version 11. You are advised to use **notificationType** instead.

 |
| notificationType11+ | [notificationManager.SlotType](../../ohos-notificationmanager-notificationmanager/document.md#slottype) | No | Yes | Notification slot type. |
| level(deprecated) | [notification.SlotLevel](../../ohos-notificationmanager-notificationmanager/document.md#slotlevel) | No | Yes | 

Notification level.

This attribute is supported since API version 7 and deprecated since API version 20. You are advised to use **notificationLevel** instead.

 |
| notificationLevel20+ | [notificationManager.SlotLevel](../../ohos-notificationmanager-notificationmanager/document.md#slotlevel) | No | Yes | Notification level. |
| desc | string | No | Yes | Notification slot description. |
| badgeFlag | boolean | No | Yes | 

Whether to display the badge.

\- **true**: Yes.

\- **false**: No.

 |
| bypassDnd | boolean | No | Yes | 

Whether to bypass DND mode in the system.

\- **true**: Yes.

\- **false**: No.

 |
| lockscreenVisibility | number | No | Yes | Mode for displaying the notification on the lock screen. Not supported currently. |
| vibrationEnabled | boolean | No | Yes | 

Whether to enable vibration for the notification.

\- **true**: Yes.

\- **false**: No.

 |
| sound | string | No | Yes | Name of the custom ringtone file for notifications. This file is stored in the **resources/rawfile** directory and supports formats such as M4A, AAC, MP3, OGG, WAV, FLAC, and AMR. |
| lightEnabled | boolean | No | Yes | 

Whether the indicator blinks for the notification.

\- **true**: Yes.

\- **false**: No.

 |
| lightColor | number | No | Yes | Indicator color of the notification. Not supported currently. |
| vibrationValues | Array<number> | No | Yes | Vibration mode of the notification. Not supported currently. |
| enabled9+ | boolean | Yes | Yes | 

Whether the notification is enabled.

\- **true**: enabled.

\- **false**: disabled.

 |
