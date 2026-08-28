# @system.notification (Notification)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/ty1sErmaQDiO5QLdg-cvuw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062516Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A8E6760AA663A61BA34C3DD83AA1AFE6BC8027B47FF0AF674AE990360FD9C7F1)

-   The APIs of this module are no longer maintained since API version 7. You are advised to use [@ohos.notification](../ohos-notification-notification/document.md).
    
-   The initial APIs of this module are supported since API version 3. Newly added APIs will be marked with a superscript to indicate their earliest API version.
    

#### Modules to Import

import notification from '@system.notification';

#### ActionResult

**System capability**: SystemCapability.Notification.Notification

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| bundleName | string | Yes | Name of the application bundle to which the notification will be redirected after being clicked. |
| abilityName | string | Yes | Name of the application ability to which the notification will be redirected after being clicked. |
| uri | string | No | URI of the page to be redirected to. |

#### ShowNotificationOptions

**System capability**: SystemCapability.Notification.Notification

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| contentTitle | string | No | Notification title. |
| contentText | string | No | Notification content. |
| clickAction(deprecated) | [ActionResult](#actionresult) | No | 
Action triggered when the notification is clicked.

This API is deprecated since API version 7.

 |

#### notification.show

show(options?: ShowNotificationOptions): void

Displays a notification.

**System capability**: SystemCapability.Notification.Notification

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | ShowNotificationOptions | No | Notification title. |

**Example**

let notificationObj: notification = {
  show() {
    notification.show({
      contentTitle: 'title info',
      contentText: 'text',
      clickAction: {
        bundleName: 'com.example.testapp',
        abilityName: 'notificationDemo',
        uri: '/path/to/notification'
      }
    });
  }
}
