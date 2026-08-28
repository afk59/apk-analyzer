# What are the use scenarios of Emitter and EventHub?

Emitter provides APIs for sending and processing events between threads, including the APIs for processing events that are subscribed to in persistent or one-shot manner, unsubscribing from events, and emitting events to the event queue.

1.  Subscribe to an event.
    
    import { emitter } from '@kit.BasicServicesKit'; 
     
    const TAG: string = 'ThreadModel';
    
    // Define an event with an eventId of 1
    let event: emitter.InnerEvent = {
      eventId: 1
    };
    
    // Execute the callback after receiving an event with eventId 1
    let callback = (eventData: emitter.EventData): void => {
      this.getUIContext().getPromptAction().showToast({
        message: JSON.stringify(eventData)
      });
    };
    
    // Subscribe to events with eventId 1
    emitter.on(event,callback);
    this.getUIContext().getPromptAction().showToast({
      message: 'subscribe\_success'
    });
    
2.  Emit the event.
    
    import { emitter } from '@kit.BasicServicesKit';
    
    // Define an event with an eventId of 1 and a priority of Low 
    let event: emitter.InnerEvent = {
      eventId: 1,
      priority: emitter.EventPriority.LOW
    };
    
    let eventData: emitter.EventData = {
      data: {
        content: 'c',
        id: 1,
        isEmpty: false
      }
    };
    
    // Send an event with eventId 1 and the event content is eventData
    emitter.emit(event,eventData);
    
    EventHub provides APIs for sending and processing events in threads, including subscribing to, unsubscribing from, and triggering events. The reference below describes the development procedure by using data synchronization between the UIAbility component and the UI as an example.
    
    **Reference**
    
    [Data Synchronization Between UIAbility and UI Page](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-data-sync-with-ui)
