# NotificationFlags

The **NotificationFlags** module implements a **NotificationFlags** instance.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/04/v3/2zqqWSOyRAidLAtEw4smxg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062515Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=00B87794F8ADAAEBDC737347ED58A0A35D67040CB0DB2C42DC8E26F8E5C7C895)

The initial APIs of this module are supported since API version 8. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### NotificationFlags

Defines the notification flags.

**System capability**: SystemCapability.Notification.Notification

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| soundEnabled | [NotificationFlagStatus](#notificationflagstatus11) | Yes | Yes | Settings of the sound alert for the notification. |
| vibrationEnabled | [NotificationFlagStatus](#notificationflagstatus11) | Yes | Yes | Settings of vibration for the notification. |

#### NotificationFlagStatus11+

Enumerates the notification flag states.

**System capability**: SystemCapability.Notification.Notification

| Name | Value | Description |
| :-- | :-- | :-- |
| TYPE\_NONE | 0 | The default flag is used. The effect is the same as that of **TYPE\_OPEN**. |
| TYPE\_OPEN | 1 | The notification flag is enabled. |
| TYPE\_CLOSE | 2 | The notification flag is disabled. |
