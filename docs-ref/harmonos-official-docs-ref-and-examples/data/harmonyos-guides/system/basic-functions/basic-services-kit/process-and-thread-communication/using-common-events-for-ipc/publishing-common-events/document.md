# Publishing Common Events

#### When to Use

You can use [publish()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-commoneventmanager#commoneventmanagerpublish) to publish a common event, which can carry data for subscribers to parse and process.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/L6GMqD2kSHaSsSvoZmRkvg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062019Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9D72DD36C3A7CA99C6A156FCE8F00B656F0FBF156B5B58793065E67B39776356)

Subscribers can receive sticky common events that have been sent. However, they must subscribe to common events of other types before receiving them. For details about subscription, see [Subscribing to Common Events](../subscribing-to-common-events-in-dynamic-mode/document.md).

#### Available APIs

For details about the APIs, see [commonEventManager.publish](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-commoneventmanager#commoneventmanagerpublish).

| API | Description |
| :-- | :-- |
| publish(event: string, callback: AsyncCallback<void>) | Publishes a common event. |
| publish(event: string, options: [CommonEventPublishData](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-commonevent-commoneventpublishdata), callback: AsyncCallback<void>) | Publishes a common event with given properties. |

#### Publishing a Common Event That Does Not Carry Information

Common events that do not carry information can be published only as unordered common events.

1.  Import the related modules.
    
    import { BusinessError, commonEventManager } from '@kit.BasicServicesKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    
    const TAG: string = 'ProcessModel';
    const DOMAIN\_NUMBER: number = 0xFF00;
    
2.  Pass in the common event name and callback, and publish the event.
    
    // Publish the common event. Replace the event field with the actual event name.
    commonEventManager.publish('event', (err: BusinessError) => {
      if (err) {
        hilog.error(DOMAIN\_NUMBER, TAG,
          \`Publish failed, code is ${JSON.stringify(err.code)}, message is ${JSON.stringify(err.message)}\`);
      } else {
        // ...
        hilog.info(DOMAIN\_NUMBER, TAG, \`Publish success\`);
      }
    });
    

#### Publishing a Common Event That Carries Information

Common events that carry information can be published as unordered, ordered, and sticky common events, which are specified by the **isOrdered** and **isSticky** fields of [CommonEventPublishData](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-commonevent-commoneventpublishdata).

1.  Import the related modules.
    
    import { BusinessError, commonEventManager } from '@kit.BasicServicesKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    
    const TAG: string = 'ProcessModel';
    const DOMAIN\_NUMBER: number = 0xFF00;
    
2.  Create the public event information to publish.
    
    // Information of a common event.
    let options: commonEventManager.CommonEventPublishData = {
      code: 1, // Initial code of the common event.
      data: 'initial data', // Initial data of the common event.
    };
    
3.  Pass in the common event name, information of the common event, and callback, and publish the event.
    
    // Publish the common event. Replace the event field with the actual event name.
    commonEventManager.publish('event', options, (err: BusinessError) => {
      if (err) {
        hilog.error(DOMAIN\_NUMBER, TAG,
          \`Failed to publish common event. Code is ${err.code}, message is ${err.message}\`);
      } else {
        // ...
        hilog.info(DOMAIN\_NUMBER, TAG, \`Succeeded in publishing common event.\`);
      }
    });
