# NotificationActionButton

The **NotificationActionButton** module provides APIs for describing the button displayed in the notification.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/mKpY3dKiQxyP8428QvX0Cg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062515Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AAFFCB0181D200B48E1094D4FDF9F3C2DDED123C7473E58914E25BFBCAD2FFB0)

The initial APIs of this module are supported since API version 7. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### NotificationActionButton

**System capability**: SystemCapability.Notification.Notification

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| title | string | No | No | Button title. It cannot be an empty string or exceed 200 bytes. Excess content will be truncated. |
| wantAgent | [WantAgent](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-wantagent-wantagent-module/document.md) | No | No | **WantAgent** of the button. |
| extras | { \[key: string\]: any } | No | Yes | Extra information of the button. Not supported currently. |
| userInput8+ | [NotificationUserInput](../notificationuserinput/document.md) | No | Yes | User input object. This parameter is left empty by default. ID entered by a subscriber. |
