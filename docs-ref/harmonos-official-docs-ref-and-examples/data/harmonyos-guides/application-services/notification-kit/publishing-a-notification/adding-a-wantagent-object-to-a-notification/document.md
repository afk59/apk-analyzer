# Adding a WantAgent Object to a Notification

An application requests [WantAgent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-wantagent) from Ability Kit and encapsulates it into the notification. When a notification is published, the user may tap a message or a button in the notification panel to start the target application or publish a common event.

The following figure shows a notification carrying action buttons.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/nvZlwKnCQYmx9EoWYP-GyQ/en-us_image_0000002568684989.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062114Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=81258964016BCEE4DBAB7AFBCBCB2A565293D2D3EA50FF68BA20C49FBD69C1A7)

#### Working Principles

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/I52rjzOuSB60PMMpoQTcag/en-us_image_0000002568764999.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062114Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9E70D85319E0DDC1CF56325A25332899EB19426F3475291B7E33ABF8907D60D8)

#### Available APIs

| **API** | **Description** |
| :-- | :-- |
| [publish](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-notificationmanager#notificationmanagerpublish-1)(request: NotificationRequest): Promise<void> | Publishes a notification. |
| [getWantAgent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-wantagent#wantagentgetwantagent)(info: WantAgentInfo, callback: AsyncCallback<WantAgent>): void | Creates a **WantAgent** object. |

#### How to Develop

1.  Import the modules.
    
    import { notificationManager } from '@kit.NotificationKit';
    import { wantAgent, WantAgent } from '@kit.AbilityKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    
    const TAG: string = '\[PublishOperation\]';
    const DOMAIN\_NUMBER: number = 0xFF00;
    
2.  Create a **WantAgentInfo** object.
    
    Scenario 1: Create a [WantAgentInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-wantagent-wantagentinfo) object for starting a UIAbility.
    
    let wantAgentObj: WantAgent | null = null; // Store the created WantAgent object for subsequent trigger actions.
    
    // Set the action type through operationType of WantAgentInfo.
    let wantAgentInfo: wantAgent.WantAgentInfo = {
      wants: \[
        {
          deviceId: '',
          bundleName: 'com.sample.eventnotification', // Use the actual bundle name.
          abilityName: 'EntryAbility', // Use the actual ability name.
          action: '',
          entities: \[\],
          uri: '',
          parameters: {}
        }
      \],
      actionType: wantAgent.OperationType.START\_ABILITY,
      requestCode: 0,
      actionFlags: \[wantAgent.WantAgentFlags.CONSTANT\_FLAG\]
    };
    
    Scenario 2: Create a [WantAgentInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-wantagent-wantagentinfo) object for publishing a [common event](../../../../system/basic-functions/basic-services-kit/process-and-thread-communication/using-common-events-for-ipc/introduction-to-common-events/document.md).
    
    let wantAgentObj: WantAgent | null = null; // Store the created WantAgent object for subsequent trigger actions.
    
    // Set the action type through operationType of WantAgentInfo.
    let wantAgentInfo: wantAgent.WantAgentInfo = {
      wants: \[
        {
          action: 'event\_name', // Set the action name.
          parameters: {},
        }
      \],
      actionType: wantAgent.OperationType.SEND\_COMMON\_EVENT,
      requestCode: 0,
      actionFlags: \[wantAgent.WantAgentFlags.CONSTANT\_FLAG\],
    };
    
3.  Call [getWantAgent()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-wantagent#wantagentgetwantagent) to create a **WantAgent** object.
    
    // Create a WantAgent object.
    wantAgent.getWantAgent(wantAgentInfo, (err: BusinessError, data: WantAgent) => {
      if (err) {
        hilog.error(DOMAIN\_NUMBER, TAG,
          \`Failed to get want agent. Code is ${err.code}, message is ${err.message}\`);
        return;
      }
      hilog.info(DOMAIN\_NUMBER, TAG, 'Succeeded in getting want agent.');
      wantAgentObj = data;
    
      // ...
    });
    
4.  Create a **NotificationRequest** object and publish a notification carrying **WantAgent**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/HBdpHCrgSp-ptRiaKIiHjQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062114Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=28CC78E920E080F3AB31122ACF065CD20E03C5E31201AFC12D7F8E8D5B0BF99E)
    
    -   If **WantAgent** is encapsulated in a notification, **WantAgent** is triggered when the notification is tapped. If a notification contains action buttons, the buttons are displayed when the notification is tapped and **WantAgent** is triggered when the notification is tapped again.
        
    -   If **WantAgent** is encapsulated in the action buttons, the buttons are displayed under the notification when the notification is tapped and **WantAgent** is triggered when a button is tapped.
        
    
    // Create the NotificationActionButton object.
    let actionButton: notificationManager.NotificationActionButton = {
      title: 'open\_the\_app',
      // Before using wantAgentObj, ensure that a value has been assigned to it (that is, step 3 is performed).
      // WantAgent of the notification buttons
      wantAgent: wantAgentObj!
    };
    
    // Create a NotificationRequest object.
    let notificationRequest: notificationManager.NotificationRequest = {
      content: {
        notificationContentType: notificationManager.ContentType.NOTIFICATION\_CONTENT\_BASIC\_TEXT,
        normal: {
          title: 'one\_button\_notify',
          text: 'Click on this notification twice to open the app',
          additionalText: 'Test\_AdditionalText',
        },
      },
      id: 6,
      // WantAgent of the notification
      wantAgent: wantAgentObj!,
      // Action buttons
      actionButtons: \[actionButton\],
    };
    
    notificationManager.publish(notificationRequest, (err: BusinessError) => {
      if (err) {
        hilog.error(DOMAIN\_NUMBER, TAG,
          \`Failed to publish notification. Code is ${err.code}, message is ${err.message}\`);
        return;
      }
      hilog.info(DOMAIN\_NUMBER, TAG, 'Succeeded in publishing notification.');
    });
    

#### Sample Code

-   [Custom Notification](https://gitcode.com/openharmony/applications_app_samples/blob/master/code/BasicFeature/Notification/CustomNotification/README.md)
