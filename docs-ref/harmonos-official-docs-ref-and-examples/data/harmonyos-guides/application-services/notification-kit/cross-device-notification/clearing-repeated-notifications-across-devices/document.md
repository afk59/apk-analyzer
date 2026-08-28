# Clearing Repeated Notifications Across Devices

Since API version 20, you can clear repeated notifications across devices to prevent users from being disturbed by notifications published through different ways (for example, notifications sent from a mobile phone to the current device are the same as those published by Push Kit).

#### Implementation Principles

When an application publishes a notification, the notification carries the [appMessageId](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-notification-notificationrequest#notificationrequest-1) field, which is a unique identifier. After receiving notifications from multiple ways, the cross-device notification service checks the notification based on this field to clear duplicate notifications.

Only the first notification is displayed on the device. Duplicate notifications received later will be silently cleared and will not be displayed or notified.

**Figure 1** Process of notification deduplication in all scenarios

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/skLFEQRwS8SJqu71JS1dnw/en-us_image_0000002537925214.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062114Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B31A2B48B2601A2041066CEE296B54C79F493EF0186DF4CF92B6A5B611F9586E)

#### Constraints

-   The uniqueness of the [appMessageId](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-notification-notificationrequest#notificationrequest-1) field must be ensured. This field for the same notification must stay consistent on all devices.
-   The [appMessageId](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-notification-notificationrequest#notificationrequest-1) field is valid only within 24 hours after the notification is published. If the notification is published beyond 24 hours or the device is restarted, this field becomes invalid.

#### Available APIs

| **API** | **Description** | **Description** |
| :-- | :-- | :-- |
| [publish](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-notificationmanager#notificationmanagerpublish-1)(request: NotificationRequest): Promise<void> | Publishes a notification. | For details, see the description of the **appMessageId** field in the [NotificationRequest](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-notification-notificationrequest) object. |

#### How to Develop

1.  Import the related modules.
    
    import { notificationManager } from '@kit.NotificationKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
2.  Publish a notification that contains the **appMessageId** field.
    
    // publish callback
    let publishCallback = (err: BusinessError): void => {
      if (err) {
        console.error(\`Failed to publish notification. Code is ${err.code}, message is ${err.message}\`);
      } else {
        console.info(\`Succeeded in publishing notification.\`);
      }
    };
    // NotificationRequest object
    let notificationRequest: notificationManager.NotificationRequest = {
      id: 1,
      content: {
        notificationContentType: notificationManager.ContentType.NOTIFICATION\_CONTENT\_BASIC\_TEXT,
        normal: {
          title: 'test\_title',
          text: 'test\_text',
          additionalText: 'test\_additionalText'
        }
      },
      appMessageId: 'test\_appMessageId\_1'
    };
    notificationManager.publish(notificationRequest, publishCallback);
