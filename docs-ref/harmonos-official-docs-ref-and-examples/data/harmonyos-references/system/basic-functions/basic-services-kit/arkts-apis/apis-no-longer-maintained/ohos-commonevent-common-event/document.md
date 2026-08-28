# @ohos.commonEvent (Common Event)

The **CommonEvent** module provides capabilities to publish, subscribe to, and unsubscribe from common events, as well as obtain and modify the common event result code and result data.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/3ZXzx_HgTfqFtG6RtS9Cqw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=747D5B627C63ABFB2190909046FFEF75ED3247B9E282E6512A6BCA2E33DFBCBF)

-   The APIs provided by this module are no longer maintained since API version 9. You are advised to use [@ohos.commonEventManager](../../process-and-thread-communication/ohos-commoneventmanager-common-event/document.md).
    
-   The initial APIs of this module are supported since API version 7. Newly added APIs will be marked with a superscript to indicate their earliest API version.
    

#### Modules to Import

import commonEvent from '@ohos.commonEvent';

#### Support

A system common event is an event that is published by a system service or system application and requires specific permissions to subscribe to. To publish or subscribe to this type of event, you must follow the event-specific definitions.

For details about the definitions of all system common events, see [System Common Events](../system-common-events-to-be-deprecated-soon/document.md).

#### commonEvent.publish(deprecated)

publish(event: string, callback: AsyncCallback<void>): void

Publishes a common event. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/p1Xuu7WKR7mgrz9p_l6LCw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8F1A50D0ED8D1AF3C2DCF5E18F9D895E8E35F0B1EBE125B51D395DF050DD9CF8)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [commonEventManager.publish](../../process-and-thread-communication/ohos-commoneventmanager-common-event/document.md#commoneventmanagerpublish) instead.

**System capability**: SystemCapability.Notification.CommonEvent

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | string | Yes | Name of the common event to publish. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Example**

import Base from '@ohos.base';

// Callback for common event publication
function publishCB(err:Base.BusinessError) {
    if (err.code) {
        console.error(\`publish failed, code is ${err.code}\`);
    } else {
        console.info("publish");
    }
}

// Publish a common event.
commonEvent.publish("event", publishCB);

#### commonEvent.publish(deprecated)

publish(event: string, options: CommonEventPublishData, callback: AsyncCallback<void>): void

Publishes a common event with given properties. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/BQquuIpPRoy-deQ_JqFEVg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EEC35DB854563C4879A9C543F1335BE1899FDFA303494C052A97A7B3B6775ADC)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [commonEventManager.publish](../../process-and-thread-communication/ohos-commoneventmanager-common-event/document.md#commoneventmanagerpublish-1) instead.

**System capability**: SystemCapability.Notification.CommonEvent

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | string | Yes | Name of the common event to publish. |
| options | [CommonEventPublishData](../../process-and-thread-communication/commonevent/commoneventpublishdata/document.md) | Yes | Properties of the common event to publish. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Example**

import Base from '@ohos.base';
import CommonEventManager from '@ohos.commonEventManager';

// Information of a common event.
let options:CommonEventManager.CommonEventPublishData = {
    code: 0,             // Initial code of the common event.
    data: "initial data",// Initial data of the common event.
    isOrdered: true  // The common event is an ordered one.
}

// Callback for common event publication
function publishCB(err:Base.BusinessError) {
    if (err.code) {
        console.error(\`publish failed, code is ${err.code}\`);
    } else {
        console.info("publish");
    }
}

// Publish a common event.
commonEvent.publish("event", options, publishCB);

#### commonEvent.createSubscriber(deprecated)

createSubscriber(subscribeInfo: CommonEventSubscribeInfo, callback: AsyncCallback<CommonEventSubscriber>): void

Creates a subscriber. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/7TuA1lXsQjm6IwWOkMTUvQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BFD72A4E49D42D1AA34C53D554E5EF2D2A7CB720C41003E0C25D313AAD07A982)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [commonEventManager.createSubscriber](../../process-and-thread-communication/ohos-commoneventmanager-common-event/document.md#commoneventmanagercreatesubscriber) instead.

**System capability**: SystemCapability.Notification.CommonEvent

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| subscribeInfo | [CommonEventSubscribeInfo](../../process-and-thread-communication/commonevent/commoneventsubscribeinfo/document.md) | Yes | Subscriber information. |
| callback | AsyncCallback<[CommonEventSubscriber](../../process-and-thread-communication/commonevent/commoneventsubscriber/document.md)\> | Yes | Callback used to return the result. |

**Example**

import Base from '@ohos.base';
import CommonEventManager from '@ohos.commonEventManager';

let subscriber:CommonEventManager.CommonEventSubscriber; // Used to save the created subscriber object for subsequent subscription and unsubscription.

// Subscriber information.
let subscribeInfo:CommonEventManager.CommonEventSubscribeInfo = {
    events: \["event"\]
};

// Callback for subscriber creation.
function createCB(err:Base.BusinessError, commonEventSubscriber:CommonEventManager.CommonEventSubscriber) {
    if (err.code) {
        console.error(\`createSubscriber failed, code is ${err.code}\`);
    } else {
        console.info("createSubscriber");
        subscriber = commonEventSubscriber;
    }
}

// Create a subscriber.
commonEvent.createSubscriber(subscribeInfo, createCB);

#### commonEvent.createSubscriber(deprecated)

createSubscriber(subscribeInfo: CommonEventSubscribeInfo): Promise<CommonEventSubscriber>

Creates a subscriber. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/dGgcyzq3Tfqk0SSjZ8wT2w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A7A484F6FEEFE699762EDA167A353FBD2E143153FC8E7AB02C788EA19AA74B7F)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [commonEventManager.createSubscriber](../../process-and-thread-communication/ohos-commoneventmanager-common-event/document.md#commoneventmanagercreatesubscriber-1) instead.

**System capability**: SystemCapability.Notification.CommonEvent

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| subscribeInfo | [CommonEventSubscribeInfo](../../process-and-thread-communication/commonevent/commoneventsubscribeinfo/document.md) | Yes | Subscriber information. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[CommonEventSubscriber](../../process-and-thread-communication/commonevent/commoneventsubscriber/document.md)\> | Promise used to return the subscriber object. |

**Example**

import Base from '@ohos.base';
import CommonEventManager from '@ohos.commonEventManager';

let subscriber:CommonEventManager.CommonEventSubscriber; // Used to save the created subscriber object for subsequent subscription and unsubscription.

// Subscriber information.
let subscribeInfo:CommonEventManager.CommonEventSubscribeInfo = {
    events: \["event"\]
};

// Create a subscriber.
commonEvent.createSubscriber(subscribeInfo).then((commonEventSubscriber:CommonEventManager.CommonEventSubscriber) => {
    console.info("createSubscriber");
    subscriber = commonEventSubscriber;
}).catch((err:Base.BusinessError) => {
    console.error(\`createSubscriber failed, code is ${err.code}\`);
});

#### commonEvent.subscribe(deprecated)

subscribe(subscriber: CommonEventSubscriber, callback: AsyncCallback<CommonEventData>): void

Subscribes to common events. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/fXNvryV5RLWCR9OHbQzG0Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=51B3AB93964764B9CDC195E40B01465E33AF0C025354DE474E737261CAC6DA04)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [commonEventManager.subscribe](../../process-and-thread-communication/ohos-commoneventmanager-common-event/document.md#commoneventmanagersubscribe) instead.

**System capability**: SystemCapability.Notification.CommonEvent

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| subscriber | [CommonEventSubscriber](../../process-and-thread-communication/commonevent/commoneventsubscriber/document.md) | Yes | Subscriber object. |
| callback | AsyncCallback<[CommonEventData](../../process-and-thread-communication/commonevent/commoneventdata/document.md)\> | Yes | Callback used to return the result. |

**Example**

import Base from '@ohos.base';
import CommonEventManager from '@ohos.commonEventManager';

let subscriber:CommonEventManager.CommonEventSubscriber;// Used to save the created subscriber object for subsequent subscription and unsubscription.

// Subscriber information.
let subscribeInfo:CommonEventManager.CommonEventSubscribeInfo = {
    events: \["event"\]
};

// Callback for common event subscription.
function subscribeCB(err:Base.BusinessError, data:CommonEventManager.CommonEventData) {
    if (err.code) {
        console.error(\`subscribe failed, code is ${err.code}\`);
    } else {
        console.info("subscribe " + JSON.stringify(data));
    }
}

// Callback for subscriber creation.
function createCB(err:Base.BusinessError, commonEventSubscriber:CommonEventManager.CommonEventSubscriber) {
    if (err.code) {
        console.error(\`createSubscriber failed, code is ${err.code}\`);
    } else {
        console.info("createSubscriber");
        subscriber = commonEventSubscriber;
        // Subscribe to a common event.
        commonEvent.subscribe(subscriber, subscribeCB);
    }
}

// Create a subscriber.
commonEvent.createSubscriber(subscribeInfo, createCB);

#### commonEvent.unsubscribe(deprecated)

unsubscribe(subscriber: CommonEventSubscriber, callback?: AsyncCallback<void>): void

Unsubscribes from common events. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/a3rrGTrATCO-t0d-S64BXg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=935E870BE7BF509E30B8D24F9FFF1AC31759B1628859350E2A3851A274E30B01)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [commonEventManager.unsubscribe](../../process-and-thread-communication/ohos-commoneventmanager-common-event/document.md#commoneventmanagerunsubscribe) instead.

**System capability**: SystemCapability.Notification.CommonEvent

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| subscriber | [CommonEventSubscriber](../../process-and-thread-communication/commonevent/commoneventsubscriber/document.md) | Yes | Subscriber object. |
| callback | AsyncCallback<void> | No | Callback used to return the result. |

**Example**

import Base from '@ohos.base';
import CommonEventManager from '@ohos.commonEventManager';

let subscriber:CommonEventManager.CommonEventSubscriber;    // Used to save the created subscriber object for subsequent subscription and unsubscription.

// Subscriber information.
let subscribeInfo:CommonEventManager.CommonEventSubscribeInfo = {
    events: \["event"\]
};

// Callback for common event subscription.
function subscribeCB(err:Base.BusinessError, data:CommonEventManager.CommonEventData) {
    if (err.code) {
        console.error(\`subscribe failed, code is ${err.code}\`);
    } else {
        console.info("subscribe " + JSON.stringify(data));
    }
}

// Callback for subscriber creation.
function createCB(err:Base.BusinessError, commonEventSubscriber:CommonEventManager.CommonEventSubscriber) {
    if (err.code) {
        console.error(\`createSubscriber failed, code is ${err.code}\`);
    } else {
        console.info("createSubscriber");
        subscriber = commonEventSubscriber;
        // Subscribe to a common event.
        commonEvent.subscribe(subscriber, subscribeCB);
    }
}

// Callback for common event unsubscription.
function unsubscribeCB(err:Base.BusinessError) {
    if (err.code) {
        console.error(\`unsubscribe failed, code is ${err.code}\`);
    } else {
        console.info("unsubscribe");
    }
}

// Create a subscriber.
commonEvent.createSubscriber(subscribeInfo, createCB);

// Unsubscribe from the common event.
commonEvent.unsubscribe(subscriber, unsubscribeCB);
