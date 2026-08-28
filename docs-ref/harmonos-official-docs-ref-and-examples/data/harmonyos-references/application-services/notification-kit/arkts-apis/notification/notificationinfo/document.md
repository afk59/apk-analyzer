# NotificationInfo

Notification information delivered to the [onReceiveMessage](../../ohos-application-notificationsubscriberextensionability-extensionability-for-not/document.md#onreceivemessage) callback of ExtensionAbility for notification subscriptions.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/CLrdHkm2Q96L-FTFBF-8nA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062515Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7183EF5FA240BAB6D704697519514FE8B3760E7512070400801AF7C7738A6429)

The initial APIs of this module are supported since API version 22. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### NotificationInfo

**System capability**: SystemCapability.Notification.Notification

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| hashCode | string | Yes | No | Unique identifier of the notification. |
| notificationSlotType | [notificationManager.SlotType](../../ohos-notificationmanager-notificationmanager/document.md#slottype) | Yes | No | Notification slot type. |
| content | [NotificationExtensionContent](../notificationextensioncontent/document.md) | Yes | No | Notification content. |
| bundleName | string | Yes | No | Name of the bundle that creates the notification. |
| appIndex | number | Yes | No | Index of the application clone that creates the notification. It takes effect only for application clones. |
| appName | string | Yes | Yes | Name of the application that creates the notification. |
| deliveryTime | number | Yes | Yes | Timestamp (in milliseconds) when the notification is published. |
| groupName | string | Yes | Yes | Notification group name, which is left empty by default. |
