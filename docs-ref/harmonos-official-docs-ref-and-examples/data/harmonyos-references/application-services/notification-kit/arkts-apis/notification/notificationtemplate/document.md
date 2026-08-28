# NotificationTemplate

The **NotificationTemplate** module describes the notification template.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/f58Cts2DQVqZOEDExHGHBA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062515Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4691691DCA12CB4F4411C58A44303A65D66D78C93DDD49B33A73AA28524EC183)

The initial APIs of this module are supported since API version 8. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### NotificationTemplate

**System capability**: SystemCapability.Notification.Notification

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| name | string | No | No | Template name. Currently, only **downloadTemplate** is supported, indicating the progress bar template that displays download progress. |
| data | Record<string, Object> | No | No | 
Template data.

\- **title**: title of the file. This parameter is mandatory, and the value is of the string type.

\- **fileName**: name of the file to be downloaded. This parameter is mandatory, and the value is of the string type.

\- **progressValue**: download progress. The value is a number.

 |
