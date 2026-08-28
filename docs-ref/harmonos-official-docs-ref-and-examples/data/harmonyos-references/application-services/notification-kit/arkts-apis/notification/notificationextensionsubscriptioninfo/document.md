# NotificationExtensionSubscriptionInfo

The **NotificationExtensionSubscriptionInfo** module describes the information about notification extension subscription.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/-unn9Z66SDSBVU2tPkar_g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062515Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=15352635561D018399897D587E08E605561EBA9E3AFCE4AF668C0569D0500EC7)

The initial APIs of this module are supported since API version 22. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### NotificationExtensionSubscriptionInfo

**System capability**: SystemCapability.Notification.Notification

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| type | [notificationExtensionSubscription.SubscribeType](../../ohos-notificationextensionsubscription-notificationextensionsubscription/document.md#subscribetype) | No | No | Subscription type, including Bluetooth. |
| addr | string | No | No | MAC address, which is a unique identifier of the device. Example: 11:22:33:AA:BB:FF |
