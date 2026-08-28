# Canceling a Notification

When a user taps a notification to bring the application to the foreground, the application may cancel one, multiple, or all notifications.

When a user launches the application from the home screen icon and views in-app messages, the application may cancel the notifications associated with those messages.

Examples:

-   Scenario 1: The user receives an instant message from a friend. After they tap the notification to open the application and view the message, the application cancels the corresponding notification.
-   Scenario 2: The user receives an instant message from a friend. After they launch the application from the home screen icon and view the message, the application cancels the corresponding notification.

#### Available APIs

The table below lists some APIs for canceling notifications. For details about the APIs, see [@ohos.notificationManager (NotificationManager)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-notificationmanager).

| **API** | **Description** |
| :-- | :-- |
| cancel(id: number, callback: AsyncCallback<void>): void | Cancels a notification. |
| cancelAll(callback: AsyncCallback<void>): void | Cancels all notifications published by the application. |

#### How to Develop

The following describes how to cancel a text notification. This procedure is applicable for canceling other types of notifications.

1.  Import modules.
    
    import { notificationManager } from '@kit.NotificationKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    
    const TAG: string = '\[PublishOperation\]';
    const DOMAIN\_NUMBER: number = 0xFF00;
    
2.  Publish a notification.
    
    For details, see [Publishing a Text Notification](../publishing-a-notification/publishing-a-text-notification/document.md).
    
3.  Cancel the notification.
    
    // After the application is started in the foreground and the message is viewed, call this API to cancel the notification.
    notificationManager.cancel(1, (err: BusinessError) => {
      if (err) {
        hilog.error(DOMAIN\_NUMBER, TAG,
          \`Failed to cancel notification. Code is ${err.code}, message is ${err.message}\`);
        return;
      }
      hilog.info(DOMAIN\_NUMBER, TAG, 'Succeeded in canceling notification.');
    });
