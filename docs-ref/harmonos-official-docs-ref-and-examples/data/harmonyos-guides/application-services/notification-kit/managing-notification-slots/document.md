# Managing Notification Slots

The system supports a range of notification slots. Different notification slots are assigned different reminder modes. You can choose notification slots for your application and manage them as required, such as creating, querying, and deleting notification slots.

#### Notification Slots

The following table lists the notification slots and their reminder modes. **Y** indicates that the feature is supported, and **N** indicates that the feature is not supported.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/mjiHtF27Rt2gvqsz_ukBcA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062114Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=577AB3A0A0C5C809AA11B96F5393C4A0FD53AF308BD7EDC1C1CF961E75B65CBC)

Users can manage notification slots of the specified application in **Settings** > **Notifications & status bar**. If **Allow notifications** is enabled, banners are disabled (they can be enabled by users but not applications), and the lock screen notifications, application icon badges, notification sounds, and vibration are enabled by default.

| SlotType | Value | Category | Notification Panel | Banner | Lock Screen | Alert Tone/Vibration | Status Bar Icon | Automatic Screen-on |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| UNKNOWN\_TYPE | 0 | Unknown | Y | N | N | N | N | N |
| SOCIAL\_COMMUNICATION | 1 | Social communication | Y | Y | Y | Y | Y | Y |
| SERVICE\_INFORMATION | 2 | Service notification | Y | Y | Y | Y | Y | Y |
| CONTENT\_INFORMATION | 3 | Content and news | Y | N | N | N | N | N |
| CUSTOMER\_SERVICE | 5 | Customer service | Y | N | N | Y | Y | N |
| OTHER\_TYPES | 0xFFFF | Other | Y | N | N | N | N | N |

#### Available APIs

The main notification slot APIs are as follows. For details about other APIs, see [@ohos.notificationManager (NotificationManager)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-notificationmanager).

| **API** | **Description** |
| :-- | :-- |
| addSlot(type: SlotType): Promise<void> | Adds a notification slot. |
| getSlot(slotType: SlotType): Promise<NotificationSlot> | Obtains a notification slot. |
| removeSlot(slotType: SlotType): Promise<void> | Removes a notification slot for this application. |

In addition to using **addSlot()**, you can also create a notification slot by passing **notificationSlotType** in the [NotificationRequest](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-notification-notificationrequest#notificationrequest-1). If the specified notification slot does not exist, it is automatically created.

#### How to Develop

1.  Import the **notificationManager** module.
    
    import { notificationManager } from '@kit.NotificationKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    
    const TAG: string = '\[PublishOperation\]';
    const DOMAIN\_NUMBER: number = 0xFF00;
    
2.  Add a notification slot.
    
    // addSlot callback
    let addSlotCallBack = (err: BusinessError): void => {
      if (err) {
        hilog.error(DOMAIN\_NUMBER, TAG, \`addSlot failed, code is ${err.code}, message is ${err.message}\`);
      } else {
        hilog.info(DOMAIN\_NUMBER, TAG, \`addSlot success\`);
      }
    };
    notificationManager.addSlot(notificationManager.SlotType.SOCIAL\_COMMUNICATION, addSlotCallBack);
    
3.  Obtain a notification slot.
    
    Retrieve the slot's creation status and supported notification modes—for example, whether there is an alert tone, vibration, and lock screen visibility.
    
    // getSlot callback
    let getSlotCallback = (err: BusinessError, data: notificationManager.NotificationSlot): void => {
      if (err) {
        hilog.error(DOMAIN\_NUMBER, TAG, \`Failed to get slot. Code is ${err.code}, message is ${err.message}\`);
      } else {
        hilog.info(DOMAIN\_NUMBER, TAG, \`Succeeded in getting slot.\`);
        if (data != null) {
          hilog.info(DOMAIN\_NUMBER, TAG, \`slot enable status is ${JSON.stringify(data.enabled)}\`);
          hilog.info(DOMAIN\_NUMBER, TAG, \`vibrationEnabled status is ${JSON.stringify(data.vibrationEnabled)}\`);
          hilog.info(DOMAIN\_NUMBER, TAG, \`lightEnabled status is ${JSON.stringify(data.lightEnabled)}\`);
        }
      }
    };
    let slotType: notificationManager.SlotType = notificationManager.SlotType.SOCIAL\_COMMUNICATION;
    notificationManager.getSlot(slotType, getSlotCallback);
    
4.  Remove a notification slot.
    
    // removeSlot callback
    let removeSlotCallback = (err: BusinessError): void => {
      if (err) {
        hilog.error(DOMAIN\_NUMBER, TAG,
          \`removeSlot failed, code is ${JSON.stringify(err.code)}, message is ${JSON.stringify(err.message)}\`);
      } else {
        hilog.info(DOMAIN\_NUMBER, TAG, 'removeSlot success');
      }
    };
    let slotType: notificationManager.SlotType = notificationManager.SlotType.SOCIAL\_COMMUNICATION;
    notificationManager.removeSlot(slotType, removeSlotCallback);
