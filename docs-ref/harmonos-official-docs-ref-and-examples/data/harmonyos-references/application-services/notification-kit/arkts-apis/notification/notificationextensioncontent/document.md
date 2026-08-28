# NotificationExtensionContent

The **NotificationExtensionContent** module describes the notification extension content.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/NymH4q5NRqiax60zQxmWuQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062515Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=173DBAAED12B6B1ED414AB2668C936E90CD593311A3FC0B4F5F3937E349F648F)

The initial APIs of this module are supported since API version 22. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### NotificationExtensionContent

**System capability**: SystemCapability.Notification.Notification

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| title | string | No | No | Notification title. It cannot be empty or exceed 1024 bytes. Excess content will be truncated. |
| text | string | No | No | Notification content. It cannot be empty or exceed 3072 bytes. Excess content will be truncated. |
