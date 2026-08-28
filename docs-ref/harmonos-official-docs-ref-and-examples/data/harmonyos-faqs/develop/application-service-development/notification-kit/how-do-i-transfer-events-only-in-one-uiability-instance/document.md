# How Do I transfer events only in one UIAbility instance?

You can call the EventHub module in UIAbility to subscribe to events. EventHub provides an event center with the capabilities for subscribing to, unsubscribing from, and triggering events.

The code snippet is as follows:

import { UIAbility } from '@kit.AbilityKit';

export default class EntryAbility extends UIAbility {
  onForeground() {
    this.context.eventHub.on('myEvent', this.eventFunc);
    // result:
    // eventFunc is called,undefined,undefined
    this.context.eventHub.emit('myEvent');
    // result:
    // eventFunc is called,1,undefined
    this.context.eventHub.emit('myEvent', 1);
    // result:
    // eventFunc is called,1,2
    this.context.eventHub.emit('myEvent', 1, 2);
  }

  eventFunc(argOne: number, argTwo: number) {
    console.log(\`eventFunc is called, ${argOne}, ${argTwo}\`);
  }
}

**Reference**

[Using EventHub for Data Synchronization](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-data-sync-with-ui#using-eventhub-for-data-synchronization)
