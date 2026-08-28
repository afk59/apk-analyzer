# Updating a Notification

You can use this API to update published notifications, such as the upload/download progress and IMs.

#### Available APIs

The table below lists the API for updating notifications. You can use the **updateOnly** field in [NotificationRequest](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-notification-notificationrequest#notificationrequest-1) to specify the notification to update. The value is set to **false** if no notification is specified.

-   Set **updateOnly** to **true**, the notification is updated if the notification with the same ID exists; the notification fails to update if the notification with the same ID does not exist and no notification is created.
    
-   Set **updateOnly** to **false**, the notification is updated if the notification with the same ID exists; a notification is created if the notification with the same ID does not exist.
    

| **API** | **Description** |
| :-- | :-- |
| [publish](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-notificationmanager#notificationmanagerpublish)(request: NotificationRequest, callback: AsyncCallback<void>): void | Publishes an updated notification. |

#### How to Develop

The following uses the progress bar notification as an example.

1.  Import modules.
    
    import { notificationManager } from '@kit.NotificationKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    
    const TAG: string = '\[PublishOperation\]';
    const DOMAIN\_NUMBER: number = 0xFF00;
    
2.  Publish the progress bar notification.
    
    let notificationRequest: notificationManager.NotificationRequest = {
      id: 5,
      content: {
        notificationContentType: notificationManager.ContentType.NOTIFICATION\_CONTENT\_BASIC\_TEXT,
        normal: {
          title: 'test\_title',
          text: 'test\_text',
          additionalText: 'test\_additionalText'
        }
      },
      // Create a progress template. The name field has a fixed value of downloadTemplate.
      template: {
        name: 'downloadTemplate',
        data: { title: 'File Title', fileName: 'music.mp4', progressValue: 50 }
      }
    };
    
    // Publish the notification.
    notificationManager.publish(notificationRequest, (err: BusinessError) => {
      if (err) {
        hilog.error(DOMAIN\_NUMBER, TAG,
          \`Failed to publish notification. Code is ${err.code}, message is ${err.message}\`);
        return;
      }
      hilog.info(DOMAIN\_NUMBER, TAG, 'Succeeded in publishing notification.');
    });
    
3.  Update the progress bar notification using the **updateOnly** field in the [NotificationRequest](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-notification-notificationrequest#notificationrequest-1) API.
    
    let notificationRequest: notificationManager.NotificationRequest = {
      id: 5,
      updateOnly: true,
      content: {
        notificationContentType: notificationManager.ContentType.NOTIFICATION\_CONTENT\_BASIC\_TEXT,
        normal: {
          title: 'test\_title',
          text: 'test\_text',
          additionalText: 'test\_additionalText'
        }
      },
      // Create a progress template. The name field has a fixed value of downloadTemplate.
      template: {
        name: 'downloadTemplate',
        data: { title: 'File Title', fileName: 'music.mp4', progressValue: 99 }
      }
    };
    
    // Update the published notification.
    notificationManager.publish(notificationRequest, (err: BusinessError) => {
      if (err) {
        hilog.error(DOMAIN\_NUMBER, TAG,
          \`Failed to update notification. Code is ${err.code}, message is ${err.message}\`);
        return;
      }
      hilog.info(DOMAIN\_NUMBER, TAG, 'Succeeded in updating notification.');
    });
