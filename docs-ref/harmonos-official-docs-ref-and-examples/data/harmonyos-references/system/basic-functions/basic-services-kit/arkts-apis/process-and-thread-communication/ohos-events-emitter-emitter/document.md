# @ohos.events.emitter (Emitter)

The **Emitter** module provides the capabilities of sending and processing inter- or intra-thread events in a process. You can use the APIs of this module to subscribe to an event in persistent or one-shot manner, unsubscribe from an event, or emit an event to the event queue.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/pZcliBaSRze7fDD9Gxi1Dg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062357Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1560C6ACAA5CA1F3E9D531F641D751E3FC1D6A56C4B6F09B20D879A737B06407)

The initial APIs of this module are supported since API version 7. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { emitter } from '@kit.BasicServicesKit';

#### emitter.on

on(event: InnerEvent, callback: Callback<EventData>): void

Subscribes to an event in persistent manner and executes a callback after the event is received.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Notification.Emitter

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | [InnerEvent](#innerevent) | Yes | Event to subscribe to in persistent manner. The [EventPriority](#eventpriority) parameter is not required and does not take effect. |
| callback | Callback<[EventData](#eventdata)\> | Yes | Callback to be invoked when the event is received. |

**Example**

import { Callback } from '@kit.BasicServicesKit';

let innerEvent: emitter.InnerEvent = {
  eventId: 1
};

let callback: Callback<emitter.EventData> = (eventData: emitter.EventData) => {
  console.info(\`eventData: ${JSON.stringify(eventData)}\`);
}

// Execute the callback after receiving the event whose eventId is 1.
emitter.on(innerEvent, callback);

#### emitter.on11+

on(eventId: string, callback: Callback<EventData>): void

Subscribes to an event in persistent manner and executes a callback after the event is received.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Notification.Emitter

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| eventId | string | Yes | Event ID, which is a custom string with a maximum of 10240 bytes. The value cannot be empty. |
| callback | Callback<[EventData](#eventdata)\> | Yes | Callback to be invoked when the event is received. |

**Example**

import { Callback } from '@kit.BasicServicesKit';

let callback: Callback<emitter.EventData> = (eventData: emitter.EventData) => {
  console.info(\`eventData: ${JSON.stringify(eventData)}\`);
}
// Execute the callback after receiving the event whose event ID is eventId.
emitter.on(\`eventId\`, callback);

#### emitter.on12+

on<T>(eventId: string, callback: Callback<GenericEventData<T>>): void

Subscribes to an event in persistent manner and executes a callback after the event is received.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Notification.Emitter

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| eventId | string | Yes | Event ID, which is a custom string with a maximum of 10240 bytes. The value cannot be empty. |
| callback | Callback<[GenericEventData<T>](#genericeventdatat12)\> | Yes | Callback to be invoked when the event is received. |

**Example**

import { Callback } from '@kit.BasicServicesKit';

@Sendable
class Sample {
  constructor() {
    this.count = 100;
  }
  printCount() {
    console.info('Print count : ' + this.count);
  }
  count: number;
}

let callback: Callback<emitter.GenericEventData<Sample>> = (eventData: emitter.GenericEventData<Sample>): void => {
  console.info(\`eventData: ${JSON.stringify(eventData?.data)}\`);
  if (eventData?.data instanceof Sample) {
    eventData?.data?.printCount();
  }
}
// Execute the callback after receiving the event whose event ID is eventId.
emitter.on("eventId", callback);

#### emitter.once

once(event: InnerEvent, callback: Callback<EventData>): void

Subscribes to an event in one-shot manner and unsubscribes from it after the event callback is executed.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Notification.Emitter

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | [InnerEvent](#innerevent) | Yes | Event to subscribe to in one-shot manner. The [EventPriority](#eventpriority) parameter is not required and does not take effect. |
| callback | Callback<[EventData](#eventdata)\> | Yes | Callback to be invoked when the event is received. |

**Example**

import { Callback } from '@kit.BasicServicesKit';

let innerEvent: emitter.InnerEvent = {
  eventId: 1
};

let callback: Callback<emitter.EventData> = (eventData: emitter.EventData) => {
  console.info(\`eventData: ${JSON.stringify(eventData)}\`);
}
// Execute the callback after receiving the event whose eventId is 1.
emitter.once(innerEvent, callback);

#### emitter.once11+

once(eventId: string, callback: Callback<EventData>): void

Subscribes to an event in one-shot manner and unsubscribes from it after the event callback is executed.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Notification.Emitter

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| eventId | string | Yes | Event ID, which is a custom string with a maximum of 10240 bytes. The value cannot be empty. |
| callback | Callback<[EventData](#eventdata)\> | Yes | Callback to be invoked when the event is received. |

**Example**

import { Callback } from '@kit.BasicServicesKit';

let callback: Callback<emitter.EventData> = (eventData: emitter.EventData) => {
  console.info(\`eventData: ${JSON.stringify(eventData)}\`);
}
// Execute the callback after receiving the event whose event ID is eventId.
emitter.once("eventId", callback);

#### emitter.once12+

once<T>(eventId: string, callback: Callback<GenericEventData<T>>): void

Subscribes to an event in one-shot manner and unsubscribes from it after the event callback is executed.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Notification.Emitter

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| eventId | string | Yes | Event ID, which is a custom string with a maximum of 10240 bytes. The value cannot be empty. |
| callback | Callback<[GenericEventData<T>](#genericeventdatat12)\> | Yes | Callback to be invoked when the event is received. |

**Example**

import { Callback } from '@kit.BasicServicesKit';

@Sendable
class Sample {
  constructor() {
    this.count = 100;
  }
  printCount() {
    console.info('Print count : ' + this.count);
  }
  count: number;
}

let callback: Callback<emitter.GenericEventData<Sample>> = (eventData: emitter.GenericEventData<Sample>): void => {
  console.info(\`eventData: ${JSON.stringify(eventData?.data)}\`);
  if (eventData?.data instanceof Sample) {
    eventData?.data?.printCount();
  }
}
// Execute the callback after receiving the event whose event ID is eventId.
emitter.once("eventId", callback);

#### emitter.off

off(eventId: number): void

Unsubscribes from all events with the specified event ID.

After this API is used to unsubscribe from an event, the event that has been published through the [emit](#emitteremit) API but has not been executed will be unsubscribed.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Notification.Emitter

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| eventId | number | Yes | Event ID. |

**Example**

// Unregister the callbacks of all events whose eventID is 1.
emitter.off(1);

#### emitter.off11+

off(eventId: string): void

Unsubscribes from all events with the specified event ID.

After this API is used to unsubscribe from an event, the event that has been published through the [emit](#emitteremit11) API but has not been executed will be unsubscribed.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Notification.Emitter

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| eventId | string | Yes | Event ID, which is a custom string with a maximum of 10240 bytes. The value cannot be empty. |

**Example**

// Unregister the callbacks of all events whose event ID is eventId.
emitter.off("eventId");

#### emitter.off10+

off(eventId: number, callback: Callback<EventData>): void

Unsubscribes from an event with the specified event ID and processed by the specified callback. This API takes effect only when **Callback<EventData>** has been registered through the [on](#emitteron) or [once](#emitteronce) API. Otherwise, no processing is performed.

After this API is used to unsubscribe from an event, the event that has been published through the [emit](#emitteremit) API but has not been executed will be unsubscribed.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Notification.Emitter

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| eventId | number | Yes | Event ID. |
| callback | Callback<[EventData](#eventdata)\> | Yes | Callback to unregister. |

**Example**

import { Callback } from '@kit.BasicServicesKit';

let callback: Callback<emitter.EventData> = (eventData: emitter.EventData) => {
  console.info(\`eventData: ${JSON.stringify(eventData)}\`);
}
// Unregister the callback of the event whose eventID is 1. The callback object must be the registered object.
// If the callback has not been registered, no processing is performed.
emitter.off(1, callback);

#### emitter.off11+

off(eventId: string, callback: Callback<EventData>): void

Unsubscribes from an event with the specified event ID and processed by the specified callback. This API takes effect only when **Callback<EventData>** has been registered through the [on](#emitteron11) or [once](#emitteronce11) API. Otherwise, no processing is performed.

After this API is used to unsubscribe from an event, the event that has been published through the [emit](#emitteremit11) API but has not been executed will be unsubscribed.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Notification.Emitter

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| eventId | string | Yes | Event ID, which is a custom string with a maximum of 10240 bytes. The value cannot be empty. |
| callback | Callback<[EventData](#eventdata)\> | Yes | Callback to unregister. |

**Example**

import { Callback } from '@kit.BasicServicesKit';

let callback: Callback<emitter.EventData> = (eventData: emitter.EventData) => {
  console.info(\`eventData: ${JSON.stringify(eventData)}\`);
}
// Unregister the callback of the event whose event ID is eventId. The callback object must be the registered object.
// If the callback has not been registered, no processing is performed.
emitter.off("eventId", callback);

#### emitter.off12+

off<T>(eventId: string, callback: Callback<GenericEventData<T>>): void

Unsubscribes from an event with the specified event ID and processed by the specified callback. This API takes effect only when **Callback<EventData>** has been registered through the [on](#emitteron12) or [once](#emitteronce12) API. Otherwise, no processing is performed.

After this API is used to unsubscribe from an event, the event that has been published through the [emit](#emitteremit12) API but has not been executed will be unsubscribed.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Notification.Emitter

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| eventId | string | Yes | Event ID, which is a custom string with a maximum of 10240 bytes. The value cannot be empty. |
| callback | Callback<[GenericEventData<T>](#genericeventdatat12)\> | Yes | Callback to unregister. |

**Example**

import { Callback } from '@kit.BasicServicesKit';

@Sendable
class Sample {
  constructor() {
    this.count = 100;
  }
  printCount() {
    console.info('Print count : ' + this.count);
  }
  count: number;
}

let callback: Callback<emitter.GenericEventData<Sample>> = (eventData: emitter.GenericEventData<Sample>): void => {
  console.info(\`eventData: ${JSON.stringify(eventData?.data)}\`);
  if (eventData?.data instanceof Sample) {
    eventData?.data?.printCount();
  }
}
// Unregister the callback of the event whose event ID is eventId. The callback object must be the registered object.
// If the callback has not been registered, no processing is performed.
emitter.off("eventId", callback);

#### emitter.emit

emit(event: InnerEvent, data?: EventData): void

Emits a specified event.

This API can be used to emit data objects across threads. The data objects must meet the specifications specified in [Overview of Inter-Thread Communication Objects](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/serializable-overview). Currently, complex data decorated by decorators such as [@State](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-state) and [@Observed](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-observed-and-objectlink) is not supported.

After an event is published using this API, the event may not be executed immediately. When the execution starts depends on the number of events in the event queue and the execution efficiency of each event.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Notification.Emitter

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | [InnerEvent](#innerevent) | Yes | Event to emit, where [EventPriority](#eventpriority) specifies the emit priority of the event. |
| data | [EventData](#eventdata) | No | Data carried by the event. This parameter is left empty by default. |

**Example**

let eventData: emitter.EventData = {
  data: {
    "content": "content",
    "id": 1,
  }
};

let innerEvent: emitter.InnerEvent = {
  eventId: 1,
  priority: emitter.EventPriority.HIGH
};

emitter.emit(innerEvent, eventData);

#### emitter.emit11+

emit(eventId: string, data?: EventData): void

Emits a specified event.

This API can be used to emit data objects across threads. The data objects must meet the specifications specified in [Overview of Inter-Thread Communication Objects](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/serializable-overview). Currently, complex data decorated by decorators such as [@State](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-state) and [@Observed](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-observed-and-objectlink) is not supported.

After an event is published using this API, the event may not be executed immediately. When the execution starts depends on the number of events in the event queue and the execution efficiency of each event.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Notification.Emitter

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| eventId | string | Yes | Event ID, which is a custom string with a maximum of 10240 bytes. The value cannot be empty. |
| data | [EventData](#eventdata) | No | Data carried by the event. This parameter is left empty by default. |

**Example**

let eventData: emitter.EventData = {
  data: {
  "content": "content",
  "id": 1,
  }
};

emitter.emit("eventId", eventData);

#### emitter.emit12+

emit<T>(eventId: string, data?: GenericEventData<T>): void

Emits a specified event.

This API can be used to emit data objects across threads. The data objects must meet the specifications specified in [Overview of Inter-Thread Communication Objects](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/serializable-overview). Currently, complex data decorated by decorators such as [@State](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-state) and [@Observed](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-observed-and-objectlink) is not supported.

After an event is published using this API, the event may not be executed immediately. When the execution starts depends on the number of events in the event queue and the execution efficiency of each event.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Notification.Emitter

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| eventId | string | Yes | Event ID, which is a custom string with a maximum of 10240 bytes. The value cannot be empty. |
| data | [GenericEventData<T>](#genericeventdatat12) | No | Data carried by the event. This parameter is left empty by default. |

**Example**

@Sendable
class Sample {
  constructor() {
    this.count = 100;
  }
  printCount() {
    console.info('Print count : ' + this.count);
  }
  count: number;
}

let eventData: emitter.GenericEventData<Sample> = {
  data: new Sample()
};
emitter.emit("eventId", eventData);

#### emitter.emit11+

emit(eventId: string, options: Options, data?: EventData): void

Emits an event of a specified priority.

This API can be used to emit data objects across threads. The data objects must meet the specifications specified in [Overview of Inter-Thread Communication Objects](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/serializable-overview). Currently, complex data decorated by decorators such as [@State](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-state) and [@Observed](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-observed-and-objectlink) is not supported.

After an event is published using this API, the event may not be executed immediately. When the execution starts depends on the number of events in the event queue and the execution efficiency of each event.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Notification.Emitter

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| eventId | string | Yes | Event ID, which is a custom string with a maximum of 10240 bytes. The value cannot be empty. |
| options | [Options](#options11) | Yes | Event emit priority. |
| data | [EventData](#eventdata) | No | Data carried by the event. This parameter is left empty by default. |

**Example**

let eventData: emitter.EventData = {
  data: {
    "content": "content",
    "id": 1,
  }
};

let options: emitter.Options = {
  priority: emitter.EventPriority.HIGH
};

emitter.emit("eventId", options, eventData);

#### emitter.emit12+

emit<T>(eventId: string, options: Options, data?: GenericEventData<T>): void

Emits an event of a specified priority.

This API can be used to emit data objects across threads. The data objects must meet the specifications specified in [Overview of Inter-Thread Communication Objects](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/serializable-overview). Currently, complex data decorated by decorators such as [@State](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-state) and [@Observed](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-observed-and-objectlink) is not supported.

After an event is published using this API, the event may not be executed immediately. When the execution starts depends on the number of events in the event queue and the execution efficiency of each event.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Notification.Emitter

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| eventId | string | Yes | Event ID, which is a custom string with a maximum of 10240 bytes. The value cannot be empty. |
| options | [Options](#options11) | Yes | Event emit priority. |
| data | [GenericEventData<T>](#genericeventdatat12) | No | Data carried by the event. This parameter is left empty by default. |

**Example**

@Sendable
class Sample {
  constructor() {
    this.count = 100;
  }
  printCount() {
    console.info('Print count : ' + this.count);
  }
  count: number;
}

let options: emitter.Options = {
  priority: emitter.EventPriority.HIGH
};
let eventData: emitter.GenericEventData<Sample> = {
  data: new Sample()
};

emitter.emit("eventId", options, eventData);

#### emitter.getListenerCount11+

getListenerCount(eventId: number | string): number

Obtains the number of subscriptions to a specified event.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Notification.Emitter

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| eventId | number | string | Yes | Event ID, which is a custom string with a maximum of 10240 bytes. The value cannot be empty. |

**Returns**

| Type | Description |
| :-- | :-- |
| number | Number of subscriptions to a specified event. |

**Example**

let count: number = emitter.getListenerCount("eventId");

#### EventPriority

Enumerates the event priorities.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Notification.Emitter

| Name | Value | Description |
| :-- | :-- | :-- |
| IMMEDIATE | 0 | The event will be emitted before high-priority events. |
| HIGH | 1 | The event will be emitted before low-priority events. |
| LOW | 2 | The event will be emitted before idle-priority events. By default, an event is in LOW priority. |
| IDLE | 3 | The event will be emitted after all the other events. |

#### InnerEvent

Describes an event to subscribe to or emit. The **EventPriority** settings do not take effect under event subscription.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Notification.Emitter

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| eventId | number | No | No | Event ID. |
| priority | [EventPriority](#eventpriority) | No | Yes | Event priority. The default value is **EventPriority.LOW**. |

#### EventData

Describes the data carried by the emitted event.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Notification.Emitter

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| data | { \[key: string\]: any } | No | Yes | Data carried by the emitted event. The value can be in any of the following types: Array, ArrayBuffer, Boolean, DataView, Date, Error, Map, Number, Object, Primitive (except symbol), RegExp, Set, String, and TypedArray. The maximum data size is 16 MB. |

#### Options11+

Describes the event emit priority.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Notification.Emitter

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| priority | [EventPriority](#eventpriority) | No | Yes | Event priority. The default value is **EventPriority.LOW**. |

#### GenericEventData<T>12+

Describes the generic data carried by the emitted event.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Notification.Emitter

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| data | T | No | Yes | Data carried by the emitted event. **T**: generic type. |

#### Emitter22+

This module provides the capabilities of sending and processing inter- or intra-thread events in a process of the same Emitter instance. You can use the following APIs to subscribe to an event in persistent or one-shot manner, unsubscribe from an event, or emit an event to the event queue.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.Notification.Emitter

#### \[h2\]constructor22+

constructor()

Defines a constructor.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.Notification.Emitter

**Example**

let emitter1: emitter.Emitter = new emitter.Emitter();

#### \[h2\]on22+

on(eventId: string, callback: Callback<EventData>): void

Subscribes to an event specified by the Emitter instance in persistent manner and executes a callback after the event is received.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.Notification.Emitter

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| eventId | string | Yes | Event ID, which is a custom string with a maximum of 10240 bytes. The value cannot be empty. |
| callback | Callback<[EventData](#eventdata)\> | Yes | Callback to be invoked when the event is received. |

**Example**

import { Callback } from '@kit.BasicServicesKit';

let emitter1: emitter.Emitter = new emitter.Emitter();

let callback: Callback<emitter.EventData> = (eventData: emitter.EventData) => {
  console.info(\`eventData: ${JSON.stringify(eventData)}\`);
}

emitter1.on(\`eventId\`, callback);

#### \[h2\]on22+

on<T>(eventId: string, callback: Callback<GenericEventData<T>>): void

Subscribes to an event specified by the Emitter instance in persistent manner and executes a callback after the event is received.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.Notification.Emitter

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| eventId | string | Yes | Event ID, which is a custom string with a maximum of 10240 bytes. The value cannot be empty. |
| callback | Callback<[GenericEventData<T>](#genericeventdatat12)\> | Yes | Callback to be invoked when the event is received. |

**Example**

import { Callback } from '@kit.BasicServicesKit';

let emitter1: emitter.Emitter = new emitter.Emitter();

@Sendable
class Sample {
  constructor() {
    this.count = 100;
  }
  printCount() {
    console.info('Print count : ' + this.count);
  }
  count: number;
}

let callback: Callback<emitter.GenericEventData<Sample>> = (eventData: emitter.GenericEventData<Sample>): void => {
  console.info(\`eventData: ${JSON.stringify(eventData?.data)}\`);
  if (eventData?.data instanceof Sample) {
    eventData?.data?.printCount();
  }
}

emitter1.on("eventId", callback);

#### \[h2\]once22+

once(eventId: string, callback: Callback<EventData>): void

Subscribes to an event specified by the Emitter instance in one-shot manner and unsubscribes from it after the event callback is executed. This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.Notification.Emitter

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| eventId | string | Yes | Event ID, which is a custom string with a maximum of 10240 bytes. The value cannot be empty. |
| callback | Callback<[EventData](#eventdata)\> | Yes | Callback to be invoked when the event is received. |

**Example**

import { Callback } from '@kit.BasicServicesKit';

let emitter1: emitter.Emitter = new emitter.Emitter();

let callback: Callback<emitter.EventData> = (eventData: emitter.EventData) => {
  console.info(\`eventData: ${JSON.stringify(eventData)}\`);
}

emitter1.once("eventId", callback);

#### \[h2\]once22+

once<T>(eventId: string, callback: Callback<GenericEventData<T>>): void

Subscribes to an event specified by the Emitter instance in one-shot manner and unsubscribes from it after the event callback is executed. This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.Notification.Emitter

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| eventId | string | Yes | Event ID, which is a custom string with a maximum of 10240 bytes. The value cannot be empty. |
| callback | Callback<[GenericEventData<T>](#genericeventdatat12)\> | Yes | Callback to be invoked when the event is received. |

**Example**

import { Callback } from '@kit.BasicServicesKit';

let emitter1: emitter.Emitter = new emitter.Emitter();

@Sendable
class Sample {
  constructor() {
    this.count = 100;
  }
  printCount() {
    console.info('Print count : ' + this.count);
  }
  count: number;
}

let callback: Callback<emitter.GenericEventData<Sample>> = (eventData: emitter.GenericEventData<Sample>): void => {
  console.info(\`eventData: ${JSON.stringify(eventData?.data)}\`);
  if (eventData?.data instanceof Sample) {
    eventData?.data?.printCount();
  }
}

emitter1.once("eventId", callback);

#### \[h2\]off22+

off(eventId: string): void

Unsubscribes from all events with the specified event ID of the Emitter instance.

After this API is used to unsubscribe from an event, the event that has been published through the [emit](#emit22) API but has not been executed will be unsubscribed.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.Notification.Emitter

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| eventId | string | Yes | Event ID, which is a custom string with a maximum of 10240 bytes. The value cannot be empty. |

**Example**

let emitter1: emitter.Emitter = new emitter.Emitter();

emitter1.off("eventId");

#### \[h2\]off22+

off(eventId: string, callback: Callback<EventData>): void

Unsubscribes from an event of the Emitter instance. This API takes effect only when the [on](#on22) or [once](#once22) API is used to subscribe to the event with specified event ID and a callback is used to process the event.

After this API is used to unsubscribe from an event, the event that has been published through the [emit](#emit22) API but has not been executed will be unsubscribed.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.Notification.Emitter

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| eventId | string | Yes | Event ID, which is a custom string with a maximum of 10240 bytes. The value cannot be empty. |
| callback | Callback<[EventData](#eventdata)\> | Yes | Callback to unregister. |

**Example**

import { Callback } from '@kit.BasicServicesKit';

let emitter1: emitter.Emitter = new emitter.Emitter();

let callback: Callback<emitter.EventData> = (eventData: emitter.EventData) => {
  console.info(\`eventData: ${JSON.stringify(eventData)}\`);
}

emitter1.off("eventId", callback);

#### \[h2\]off22+

off<T>(eventId: string, callback: Callback<GenericEventData<T>>): void

Unsubscribes from an event of the Emitter instance. This API takes effect only when the [on](#on22-1) or [once](#once22-1) API is used to subscribe to the event with specified event ID and a callback is used to process the event.

After this API is used to unsubscribe from an event, the event that has been published through the [emit](#emit22-1) API but has not been executed will be unsubscribed.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.Notification.Emitter

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| eventId | string | Yes | Event ID, which is a custom string with a maximum of 10240 bytes. The value cannot be empty. |
| callback | Callback<[GenericEventData<T>](#genericeventdatat12)\> | Yes | Callback to unregister. |

**Example**

import { Callback } from '@kit.BasicServicesKit';

@Sendable
class Sample {
  constructor() {
    this.count = 100;
  }
  printCount() {
    console.info('Print count : ' + this.count);
  }
  count: number;
}

let emitter1: emitter.Emitter = new emitter.Emitter();

let callback: Callback<emitter.GenericEventData<Sample>> = (eventData: emitter.GenericEventData<Sample>): void => {
  console.info(\`eventData: ${JSON.stringify(eventData?.data)}\`);
  if (eventData?.data instanceof Sample) {
    eventData?.data?.printCount();
  }
}

emitter1.off("eventId", callback);

#### \[h2\]emit22+

emit(eventId: string, data?: EventData): void

Emits a specified event to the Emitter class instance.

This API can be used to emit data objects across threads. The data objects must meet the specifications specified in [Overview of Inter-Thread Communication Objects](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/serializable-overview). Currently, complex data decorated by decorators such as [@State](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-state) and [@Observed](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-observed-and-objectlink) is not supported.

After an event is published using this API, the event may not be executed immediately. When the execution starts depends on the number of events in the event queue and the execution efficiency of each event.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.Notification.Emitter

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| eventId | string | Yes | Event ID, which is a custom string with a maximum of 10240 bytes. The value cannot be empty. |
| data | [EventData](#eventdata) | No | Data carried by the event. This parameter is left empty by default. |

**Example**

let emitter1: emitter.Emitter = new emitter.Emitter();
let eventData: emitter.EventData = {
  data: {
  "content": "content",
  "id": 1,
  }
};

emitter1.emit("eventId", eventData);

#### \[h2\]emit22+

emit<T>(eventId: string, data?: GenericEventData<T>): void

Emits a specified event to the Emitter class instance.

This API can be used to emit data objects across threads. The data objects must meet the specifications specified in [Overview of Inter-Thread Communication Objects](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/serializable-overview). Currently, complex data decorated by decorators such as [@State](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-state) and [@Observed](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-observed-and-objectlink) is not supported.

After an event is published using this API, the event may not be executed immediately. When the execution starts depends on the number of events in the event queue and the execution efficiency of each event.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.Notification.Emitter

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| eventId | string | Yes | Event ID, which is a custom string with a maximum of 10240 bytes. The value cannot be empty. |
| data | [GenericEventData<T>](#genericeventdatat12) | No | Data carried by the event. This parameter is left empty by default. |

**Example**

@Sendable
class Sample {
  constructor() {
    this.count = 100;
  }
  printCount() {
    console.info('Print count : ' + this.count);
  }
  count: number;
}

let emitter1: emitter.Emitter = new emitter.Emitter();

let eventData: emitter.GenericEventData<Sample> = {
  data: new Sample()
};

emitter1.emit("eventId", eventData);

#### \[h2\]emit22+

emit(eventId: string, options: Options, data?: EventData): void

Emits a specified event to the Emitter class instance.

This API can be used to emit data objects across threads. The data objects must meet the specifications specified in [Overview of Inter-Thread Communication Objects](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/serializable-overview). Currently, complex data decorated by decorators such as [@State](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-state) and [@Observed](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-observed-and-objectlink) is not supported.

After an event is published using this API, the event may not be executed immediately. When the execution starts depends on the number of events in the event queue and the execution efficiency of each event.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.Notification.Emitter

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| eventId | string | Yes | Event ID, which is a custom string with a maximum of 10240 bytes. The value cannot be empty. |
| options | [Options](#options11) | Yes | Event emit priority. |
| data | [EventData](#eventdata) | No | Data carried by the event. This parameter is left empty by default. |

**Example**

let emitter1: emitter.Emitter = new emitter.Emitter();

let options: emitter.Options = {
  priority: emitter.EventPriority.HIGH
};
let eventData: emitter.EventData = {
  data: {
  "content": "content",
  "id": 1,
  }
};

emitter1.emit("eventId", options, eventData);

#### \[h2\]emit22+

emit<T>(eventId: string, options: Options, data?: GenericEventData<T>): void

Emits an event of a specified priority to the Emitter instance.

This API can be used to emit data objects across threads. The data objects must meet the specifications specified in [Overview of Inter-Thread Communication Objects](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/serializable-overview). Currently, complex data decorated by decorators such as [@State](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-state) and [@Observed](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-observed-and-objectlink) is not supported.

After an event is published using this API, the event may not be executed immediately. When the execution starts depends on the number of events in the event queue and the execution efficiency of each event.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.Notification.Emitter

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| eventId | string | Yes | Event ID, which is a custom string with a maximum of 10240 bytes. The value cannot be empty. |
| options | [Options](#options11) | Yes | Event emit priority. |
| data | [GenericEventData<T>](#genericeventdatat12) | No | Data carried by the event. This parameter is left empty by default. |

**Example**

@Sendable
class Sample {
  constructor() {
    this.count = 100;
  }
  printCount() {
    console.info('Print count : ' + this.count);
  }
  count: number;
}

let emitter1: emitter.Emitter = new emitter.Emitter();

let options: emitter.Options = {
  priority: emitter.EventPriority.HIGH
};
let eventData: emitter.GenericEventData<Sample> = {
  data: new Sample()
};

emitter1.emit("eventId", options, eventData);

#### \[h2\]getListenerCount22+

getListenerCount(eventId: string): number

Obtains the number of subscriptions to a specified event of the Emitter instance.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.Notification.Emitter

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| eventId | string | Yes | Event ID, which is a custom string with a maximum of 10240 bytes. The value cannot be empty. |

**Returns**

| Type | Description |
| :-- | :-- |
| number | Number of subscriptions to a specified event. |

**Example**

let emitter1: emitter.Emitter = new emitter.Emitter();
let count = emitter1.getListenerCount("eventId");
