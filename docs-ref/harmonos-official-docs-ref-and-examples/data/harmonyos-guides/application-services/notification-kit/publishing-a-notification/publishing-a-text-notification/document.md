# Publishing a Text Notification

You can publish text notifications to send SMS messages, alert messages, and more. There are two types of text notifications: normal text and multi-line text.

**Table 1** Basic notification content types

| Type | Description |
| :-- | :-- |
| NOTIFICATION\_CONTENT\_BASIC\_TEXT | Normal text notification. |
| NOTIFICATION\_CONTENT\_MULTILINE | Multi-line text notification. |

#### Available APIs

The following table describes the APIs for notification publishing. You specify the notification information – content, ID, slot type, and publish time – by setting the [NotificationRequest](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-notification-notificationrequest#notificationrequest-1) parameter in the APIs.

| Name | Description |
| :-- | :-- |
| publish(request: NotificationRequest, callback: AsyncCallback<void>): void | Publishes a notification. |

#### How to Develop

1.  Import the module.
    
    import { notificationManager } from '@kit.NotificationKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    
    const TAG: string = '\[PublishOperation\]';
    const DOMAIN\_NUMBER: number = 0xFF00;
    
2.  Create a **NotificationRequest** object and publish a progress notification.
    
    -   A normal text notification consists of the **title**, **text**, and **additionalText** fields. For details, see [NotificationBasicContent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-notification-notificationcontent#notificationbasiccontent).
        
        let notificationRequest: notificationManager.NotificationRequest = {
          id: 1,
          content: {
            notificationContentType: notificationManager.ContentType.NOTIFICATION\_CONTENT\_BASIC\_TEXT, // Basic notification
            normal: {
              title: 'test\_title',
              text: 'test\_text',
              additionalText: 'test\_additionalText',
            }
          }
        };
        notificationManager.publish(notificationRequest, (err: BusinessError) => {
          if (err) {
            hilog.error(DOMAIN\_NUMBER, TAG,
              \`Failed to publish notification. Code is ${err.code}, message is ${err.message}\`);
            return;
          }
          hilog.info(DOMAIN\_NUMBER, TAG, 'Succeeded in publishing notification.');
        });
        
    -   In addition to the fields in the normal text notification, the multi-line text notification provides the **lines**, **briefText**, and **longTitle** fields. For details, see [NotificationMultiLineContent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-notification-notificationcontent#notificationmultilinecontent).
        
        let notificationRequest: notificationManager.NotificationRequest = {
          id: 3,
          content: {
            notificationContentType: notificationManager.ContentType.NOTIFICATION\_CONTENT\_MULTILINE, // Multi-line text notification
            multiLine: {
              title: 'test\_multi\_line\_title',
              text: 'test\_text',
              briefText: 'test\_briefText',
              longTitle: 'test\_longTitle',
              lines: \['line\_01', 'line\_02', 'line\_03'\],
            }
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
