# Publishing a Progress Notification

The progress notification is a commonly used notification type, mainly used to display the progress of an ongoing operation, such as file downloading. When publishing a progress notification through the notification subsystem, you can use the readily available template by specifying the related attributes, such as the template name and template data.

In the [NotificationTemplate](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-notification-notificationtemplate), which only supports the progress type, **data** indicates custom template data.

#### Available APIs

[isSupportTemplate()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-notificationmanager#notificationmanagerissupporttemplate) is used to check whether a specific template is supported. Currently, only the progress bar template is supported.

| Name | Description |
| :-- | :-- |
| isSupportTemplate(templateName: string): Promise<boolean> | Checks whether a specific template is supported. |

#### How to Develop

1.  Import the module.
    
    import { notificationManager } from '@kit.NotificationKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    
    const TAG: string = '\[PublishOperation\]';
    const DOMAIN\_NUMBER: number = 0xFF00;
    
2.  Check whether a specific template is supported. In this example, the template of the **downloadTemplate** type is checked.
    
    notificationManager.isSupportTemplate('downloadTemplate').then((data: boolean) => {
      let isSupportTemplate: boolean = data; // The value true means that the template of the downloadTemplate type is supported, and false means the opposite.
      hilog.info(DOMAIN\_NUMBER, TAG,
        \`Succeeded in supporting download template notification. data is ${isSupportTemplate}\`);
    }).catch((err: BusinessError) => {
      hilog.error(DOMAIN\_NUMBER, TAG,
        \`Failed to support download template notification. Code is ${err.code}, message is ${err.message}\`);
    });
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/OGAtWFoWSb6m5fVzgWLV3g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062114Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BA59EF3EFF2871350512C1BE39A5F05452C0D201C931EB0F65E4D368570E4556)
    
    Proceed with the step below only when the specified template is supported.
    
3.  Create a **NotificationRequest** object and publish a progress notification.
    
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
        data: { title: 'File Title', fileName: 'music.mp4', progressValue: 45 }
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
