# Using Emitter for Inter-Thread Communication

Emitter is an event processing mechanism used in a process. It provides the capabilities of subscribing to, publishing, and unsubscribing from events for applications.

#### When to Use

Emitter is used to process events of the same thread or different threads in the same process in an asynchronous manner. To use this mechanism, you need to subscribe to an event and publish it, after which the Emitter distributes the published event to the subscriber, and the subscriber executes the callback method set during event subscription. Unsubscribe from the event in time to release the Emitter resources when the event does not need to be subscribed to.

#### Working Principles

Emitter distributes tasks by maintaining an internal event queue. An application needs to subscribe to an event and set the callback method of the event. After the application publishes the event, an event is inserted into the queue. The task queue executes the tasks serially, during which the callback method of the task subscriber is called to process the event.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/WNre2jEtQAmkrtFQPnlMrw/en-us_image_0000002568764823.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062020Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D48756BEC840F45EF6E7A7978DBA4519DDC67C73E60C281E5DB42990C8B72CC8)

#### Available APIs

For details, see [@ohos.events.emitter (Emitter)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-emitter).

| API | Capability | Description |
| :-- | :-- | :-- |
| on | Event subscription | Continuously subscribes to an event until the event is unsubscribed from. |
| once | Event subscription | Subscribes to an event once. |
| emit | Event publishing | Publishes an event once. |
| off | Event unsubscription | Unsubscribes from the event and subsequent notifications of this event will not be received. |

#### How to Develop

To enable Emitter's capabilities mentioned above, perform the following steps:

1.  Import the related modules.
    
    import { emitter, Callback } from '@kit.BasicServicesKit';
    
2.  Subscribe to an event.
    
    Use **on()** for continuous subscription or **once()** for one-time subscription. Set the events to subscribe to and the callback function after the events are received.
    
    // Define an event with eventId 1.
    let event: emitter.InnerEvent = {
      eventId: 1
    };
    // Define a callback for an event.
    let callback: Callback<emitter.EventData> = (eventData: emitter.EventData) => {
      this.messageOn = eventData.data!.content
      console.info(\`eventData: ${JSON.stringify(eventData)}\`);
    }
    // ···
    // Execute the callback after receiving the event whose eventId is 1.
    emitter.on(event, callback);
    
    // Execute the callback after receiving the event whose eventId is 1.
    // Note that the event is received only once using once(), while the event is received until the subscription is canceled using on().
    emitter.once(event, callback);
    
3.  Emit the event.
    
    Use **emit()** to emit events and set the events to send and the parameters to pass.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/G7ki7G0sRQKnYO5xDduQWg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062020Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=410DFEADEA38728A75C8A3757EDB5E0E131472AC71C016C13B606AC8C9143FDD)
    
    -   This API can be used to emit data objects across threads. The data objects must meet the specifications specified in [Overview of Inter-Thread Communication Objects](../../../../../application-framework/arkts/arkts-concurrency/inter-thread-communication/inter-thread-communication-objects/overview-of-inter-thread-communication-objects/document.md). Currently, complex data decorated by decorators such as [@State](../../../../../application-framework/arkui/ui-development-arkts-based-declarative-development-paradigm/ui-paradigm-state-management/state-management-v1/component-state-management/state-decorator-state-owned-by-component/document.md) and [@Observed](../../../../../application-framework/arkui/ui-development-arkts-based-declarative-development-paradigm/ui-paradigm-state-management/state-management-v1/component-state-management/observed-and-objectlink-decorators-observing-property-changes-in-nested-class-ob/document.md) is not supported.
    -   After an event is published using the **emit** API, the event may not be executed immediately. When the execution starts depends on the number of events in the event queue and the execution efficiency of each event.
    
    // Define an event with eventId 1 and priority Low.
    let event: emitter.InnerEvent = {
      eventId: 1,
      priority: emitter.EventPriority.LOW
    };
    
    let eventData: emitter.EventData = {
      data: {
        content: 'emitter',
        id: 1,
        isEmpty: false
      }
    };
    
    // Emit the event with eventId 1 and event content eventData.
    emitter.emit(event, eventData);
    
4.  Unsubscribe from the event.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/KJzZNN1URJiBXl1eMnt3Ew/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062020Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D3613982D2E16B5FD4B081A3ADC55F37521D6BBCECF0B5454B1DD427AFD1BD9B)
    
    -   If an event does not need to be subscribed to, cancel the subscription in a timely manner to prevent memory leakage.
    -   After the [off](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-emitter#emitteroff) API is used to unsubscribe from an event, the event that has been published through the [emit](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-emitter#emitteremit) API but has not been executed will be unsubscribed.
    
    // Unsubscribe from the event with eventId 1.
    emitter.off(1);
