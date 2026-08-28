# @ohos.notificationManager (NotificationManager)

The **NotificationManager** module provides notification management capabilities, covering notifications, notification slots, notification enabled status, and notification badge status.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/wzBHC-bmRXCOjbWe0N9PqQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062515Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C7B736406E55C121140273CB11354F2F0B9FAF4862A28B8DCF998C92355F79C6)

The initial APIs of this module are supported since API version 9. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { notificationManager } from '@kit.NotificationKit';

#### notificationManager.publish

publish(request: NotificationRequest, callback: AsyncCallback<void>): void

Publishes a notification. This API uses an asynchronous callback to return the result.

If the ID and label of the new notification are the same as that of the previous notification, the new one replaces the previous one.

**System capability**: SystemCapability.Notification.Notification

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| request | [NotificationRequest](../notification/notificationrequest/document.md#notificationrequest-1) | Yes | Content and related configuration of the notification to publish. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md), [Notification Error Codes](../../error-codes/notification-error-codes/document.md), and [HTTP Error Codes](../../../../system/network/network-kit/error-codes/http-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 1600001 | Internal error. |
| 1600002 | Marshalling or unmarshalling error. |
| 1600003 | Failed to connect to the service. |
| 1600004 | Notification disabled. |
| 1600005 | Notification slot disabled. |
| 1600007 | The notification does not exist. |
| 1600009 | The notification sending frequency reaches the upper limit. |
| 1600012 | No memory space. |
| 1600014 | No permission. |
| 1600015 | The current notification status does not support duplicate configurations. |
| 1600016 | The notification version for this update is too low. |
| 1600020 | The application is not allowed to send notifications due to permission settings. |
| 2300007 | Network unreachable. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

// publish callback
let publishCallback = (err: BusinessError): void => {
  if (err) {
    console.error(\`Failed to publish notification. Code is ${err.code}, message is ${err.message}\`);
  } else {
    console.info(\`Succeeded in publishing notification.\`);
  }
}
// NotificationRequest object
let notificationRequest: notificationManager.NotificationRequest = {
  id: 1,
  content: {
    notificationContentType: notificationManager.ContentType.NOTIFICATION\_CONTENT\_BASIC\_TEXT,
    normal: {
      title: "test\_title",
      text: "test\_text",
      additionalText: "test\_additionalText"
    }
  }
};
notificationManager.publish(notificationRequest, publishCallback);

#### notificationManager.publish

publish(request: NotificationRequest): Promise<void>

Publishes a notification. This API uses a promise to return the result.

If the ID and label of the new notification are the same as that of the previous notification, the new one replaces the previous one.

**System capability**: SystemCapability.Notification.Notification

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| request | [NotificationRequest](../notification/notificationrequest/document.md#notificationrequest-1) | Yes | Content and related configuration of the notification to publish. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md), [Notification Error Codes](../../error-codes/notification-error-codes/document.md), and [HTTP Error Codes](../../../../system/network/network-kit/error-codes/http-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 1600001 | Internal error. |
| 1600002 | Marshalling or unmarshalling error. |
| 1600003 | Failed to connect to the service. |
| 1600004 | Notification disabled. |
| 1600005 | Notification slot disabled. |
| 1600007 | The notification does not exist. |
| 1600009 | The notification sending frequency reaches the upper limit. |
| 1600012 | No memory space. |
| 1600014 | No permission. |
| 1600015 | The current notification status does not support duplicate configurations. |
| 1600016 | The notification version for this update is too low. |
| 1600020 | The application is not allowed to send notifications due to permission settings. |
| 2300007 | Network unreachable. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

// NotificationRequest object
let notificationRequest: notificationManager.NotificationRequest = {
  id: 1,
  content: {
    notificationContentType: notificationManager.ContentType.NOTIFICATION\_CONTENT\_BASIC\_TEXT,
    normal: {
      title: "test\_title",
      text: "test\_text",
      additionalText: "test\_additionalText"
    }
  }
};
notificationManager.publish(notificationRequest).then(() => {
  console.info(\`Succeeded in publishing notification.\`);
}).catch((err: BusinessError) => {
  console.error(\`Failed to publish notification. Code is ${err.code}, message is ${err.message}\`);
});

#### notificationManager.cancel

cancel(id: number, label: string, callback: AsyncCallback<void>): void

Cancels a notification with the specified ID and label. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Notification.Notification

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| id | number | Yes | Notification ID. |
| label | string | Yes | Notification label. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Notification Error Codes](../../error-codes/notification-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 1600001 | Internal error. |
| 1600002 | Marshalling or unmarshalling error. |
| 1600003 | Failed to connect to the service. |
| 1600007 | The notification does not exist. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

// cancel callback
let cancelCallback = (err: BusinessError): void => {
  if (err) {
    console.error(\`Failed to cancel notification. Code is ${err.code}, message is ${err.message}\`);
  } else {
    console.info(\`Succeeded in canceling notification.\`);
  }
}
notificationManager.cancel(0, "label", cancelCallback);

#### notificationManager.cancel

cancel(id: number, label?: string): Promise<void>

Cancels a notification with the specified ID and optional label. This API uses a promise to return the result.

**System capability**: SystemCapability.Notification.Notification

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| id | number | Yes | Notification ID. |
| label | string | No | Notification label. This parameter is left empty by default. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Notification Error Codes](../../error-codes/notification-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 1600001 | Internal error. |
| 1600002 | Marshalling or unmarshalling error. |
| 1600003 | Failed to connect to the service. |
| 1600007 | The notification does not exist. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

notificationManager.cancel(0).then(() => {
  console.info(\`Succeeded in canceling notification.\`);
}).catch((err: BusinessError) => {
  console.error(\`Failed to cancel notification. Code is ${err.code}, message is ${err.message}\`);
});

#### notificationManager.cancel

cancel(id: number, callback: AsyncCallback<void>): void

Cancels a notification with the specified ID. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Notification.Notification

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| id | number | Yes | Notification ID. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Notification Error Codes](../../error-codes/notification-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 1600001 | Internal error. |
| 1600002 | Marshalling or unmarshalling error. |
| 1600003 | Failed to connect to the service. |
| 1600007 | The notification does not exist. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

// cancel callback
let cancelCallback = (err: BusinessError): void => {
  if (err) {
    console.error(\`Failed to cancel notification. Code is ${err.code}, message is ${err.message}\`);
  } else {
    console.info(\`Succeeded in canceling notification.\`);
  }
}
notificationManager.cancel(0, cancelCallback);

#### notificationManager.cancelAll

cancelAll(callback: AsyncCallback<void>): void

Cancels all notifications of this application. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Notification.Notification

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Notification Error Codes](../../error-codes/notification-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 1600001 | Internal error. |
| 1600002 | Marshalling or unmarshalling error. |
| 1600003 | Failed to connect to the service. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

// cancel callback
let cancelAllCallback = (err: BusinessError): void => {
  if (err) {
    console.error(\`Failed to cancel all notification. Code is ${err.code}, message is ${err.message}\`);
  } else {
    console.info(\`Succeeded in canceling all notification.\`);
  }
}
notificationManager.cancelAll(cancelAllCallback);

#### notificationManager.cancelAll

cancelAll(): Promise<void>

Cancels all notifications of this application. This API uses a promise to return the result.

**System capability**: SystemCapability.Notification.Notification

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Notification Error Codes](../../error-codes/notification-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 1600001 | Internal error. |
| 1600002 | Marshalling or unmarshalling error. |
| 1600003 | Failed to connect to the service. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

notificationManager.cancelAll().then(() => {
  console.info(\`Succeeded in canceling all notification.\`);
}).catch((err: BusinessError) => {
  console.error(\`Failed to cancel all notification. Code is ${err.code}, message is ${err.message}\`);
});

#### notificationManager.addSlot

addSlot(type: SlotType, callback: AsyncCallback<void>): void

Adds a notification slot of a specified type. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Notification.Notification

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SlotType](#slottype) | Yes | Type of the notification slot to add. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Notification Error Codes](../../error-codes/notification-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 1600001 | Internal error. |
| 1600002 | Marshalling or unmarshalling error. |
| 1600003 | Failed to connect to the service. |
| 1600012 | No memory space. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

// addSlot callback
let addSlotCallBack = (err: BusinessError): void => {
  if (err) {
    console.error(\`Failed to add slot. Code is ${err.code}, message is ${err.message}\`);
  } else {
    console.info(\`Succeeded in adding slot.\`);
  }
}
notificationManager.addSlot(notificationManager.SlotType.SOCIAL\_COMMUNICATION, addSlotCallBack);

#### notificationManager.addSlot

addSlot(type: SlotType): Promise<void>

Adds a notification slot of a specified type. This API uses a promise to return the result.

**System capability**: SystemCapability.Notification.Notification

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SlotType](#slottype) | Yes | Type of the notification slot to add. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Notification Error Codes](../../error-codes/notification-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 1600001 | Internal error. |
| 1600002 | Marshalling or unmarshalling error. |
| 1600003 | Failed to connect to the service. |
| 1600012 | No memory space. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

notificationManager.addSlot(notificationManager.SlotType.SOCIAL\_COMMUNICATION).then(() => {
  console.info(\`Succeeded in adding slot.\`);
}).catch((err: BusinessError) => {
  console.error(\`Failed to add slot. Code is ${err.code}, message is ${err.message}\`);
});

#### notificationManager.getSlot

getSlot(slotType: SlotType, callback: AsyncCallback<NotificationSlot>): void

Obtains a notification slot of a specified type. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Notification.Notification

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| slotType | [SlotType](#slottype) | Yes | Type of a notification slot, such as social communication, service notification, content consultation, and so on. |
| callback | AsyncCallback<[NotificationSlot](../notification/notificationslot/document.md)\> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the obtained **NotificationSlot**; otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Notification Error Codes](../../error-codes/notification-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 1600001 | Internal error. |
| 1600002 | Marshalling or unmarshalling error. |
| 1600003 | Failed to connect to the service. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

// getSlot callback
let getSlotCallback = (err: BusinessError, data: notificationManager.NotificationSlot): void => {
  if (err) {
    console.error(\`Failed to get slot. Code is ${err.code}, message is ${err.message}\`);
  } else {
    console.info(\`Succeeded in getting slot, data is ${JSON.stringify(data)}\`);
  }
}
let slotType: notificationManager.SlotType = notificationManager.SlotType.SOCIAL\_COMMUNICATION;
notificationManager.getSlot(slotType, getSlotCallback);

#### notificationManager.getSlot

getSlot(slotType: SlotType): Promise<NotificationSlot>

Obtains a notification slot of a specified type. This API uses a promise to return the result.

**System capability**: SystemCapability.Notification.Notification

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| slotType | [SlotType](#slottype) | Yes | Type of a notification slot, such as social communication, service notification, content consultation, and so on. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[NotificationSlot](../notification/notificationslot/document.md)\> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Notification Error Codes](../../error-codes/notification-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 1600001 | Internal error. |
| 1600002 | Marshalling or unmarshalling error. |
| 1600003 | Failed to connect to the service. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let slotType: notificationManager.SlotType = notificationManager.SlotType.SOCIAL\_COMMUNICATION;
notificationManager.getSlot(slotType).then((data: notificationManager.NotificationSlot) => {
  console.info(\`Succeeded in getting slot, data is ${JSON.stringify(data)}\`);
}).catch((err: BusinessError) => {
  console.error(\`Failed to get slot. Code is ${err.code}, message is ${err.message}\`);
});

#### notificationManager.getSlots

getSlots(callback: AsyncCallback<Array<NotificationSlot>>): void

Obtains all notification slots of this application. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Notification.Notification

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<Array<[NotificationSlot](../notification/notificationslot/document.md)\>> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the obtained **NotificationSlot** array; otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Notification Error Codes](../../error-codes/notification-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 1600001 | Internal error. |
| 1600002 | Marshalling or unmarshalling error. |
| 1600003 | Failed to connect to the service. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

// getSlots callback
let getSlotsCallback = (err: BusinessError, data: Array<notificationManager.NotificationSlot>): void => {
  if (err) {
    console.error(\`Failed to get slots. Code is ${err.code}, message is ${err.message}\`);
  } else {
    console.info(\`Succeeded in getting slots, data is ${JSON.stringify(data)}\`);
  }
}
notificationManager.getSlots(getSlotsCallback);

#### notificationManager.getSlots

getSlots(): Promise<Array<NotificationSlot>>

Obtains all notification slots of this application. This API uses a promise to return the result.

**System capability**: SystemCapability.Notification.Notification

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<[NotificationSlot](../notification/notificationslot/document.md)\>> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [Notification Error Codes](../../error-codes/notification-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 1600001 | Internal error. |
| 1600002 | Marshalling or unmarshalling error. |
| 1600003 | Failed to connect to the service. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

notificationManager.getSlots().then((data: Array<notificationManager.NotificationSlot>) => {
  console.info(\`Succeeded in getting slots, data is ${JSON.stringify(data)}\`);
}).catch((err: BusinessError) => {
  console.error(\`Failed to get slots. Code is ${err.code}, message is ${err.message}\`);
});

#### notificationManager.removeSlot

removeSlot(slotType: SlotType, callback: AsyncCallback<void>): void

Removes a notification slot of a specified type for this application. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Notification.Notification

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| slotType | [SlotType](#slottype) | Yes | Type of a notification slot, such as social communication, service notification, content consultation, and so on. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Notification Error Codes](../../error-codes/notification-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 1600001 | Internal error. |
| 1600002 | Marshalling or unmarshalling error. |
| 1600003 | Failed to connect to the service. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

// removeSlot callback
let removeSlotCallback = (err: BusinessError): void => {
  if (err) {
    console.error(\`Failed to remove slot. Code is ${err.code}, message is ${err.message}\`);
  } else {
    console.info(\`Succeeded in removing slot.\`);
  }
}
let slotType: notificationManager.SlotType = notificationManager.SlotType.SOCIAL\_COMMUNICATION;
notificationManager.removeSlot(slotType, removeSlotCallback);

#### notificationManager.removeSlot

removeSlot(slotType: SlotType): Promise<void>

Removes a notification slot of a specified type for this application. This API uses a promise to return the result.

**System capability**: SystemCapability.Notification.Notification

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| slotType | [SlotType](#slottype) | Yes | Type of a notification slot, such as social communication, service notification, content consultation, and so on. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Notification Error Codes](../../error-codes/notification-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 1600001 | Internal error. |
| 1600002 | Marshalling or unmarshalling error. |
| 1600003 | Failed to connect to the service. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let slotType: notificationManager.SlotType = notificationManager.SlotType.SOCIAL\_COMMUNICATION;
notificationManager.removeSlot(slotType).then(() => {
  console.info(\`Succeeded in removing slot.\`);
}).catch((err: BusinessError) => {
  console.error(\`Failed to remove slot. Code is ${err.code}, message is ${err.message}\`);
});

#### notificationManager.removeAllSlots

removeAllSlots(callback: AsyncCallback<void>): void

Removes all notification slots for this application. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Notification.Notification

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Notification Error Codes](../../error-codes/notification-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 1600001 | Internal error. |
| 1600002 | Marshalling or unmarshalling error. |
| 1600003 | Failed to connect to the service. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let removeAllSlotsCallback = (err: BusinessError): void => {
  if (err) {
    console.error(\`Failed to remove all slots. Code is ${err.code}, message is ${err.message}\`);
  } else {
    console.info(\`Succeeded in removing all slots.\`);
  }
}
notificationManager.removeAllSlots(removeAllSlotsCallback);

#### notificationManager.removeAllSlots

removeAllSlots(): Promise<void>

Removes all notification slots for this application. This API uses a promise to return the result.

**System capability**: SystemCapability.Notification.Notification

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Notification Error Codes](../../error-codes/notification-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 1600001 | Internal error. |
| 1600002 | Marshalling or unmarshalling error. |
| 1600003 | Failed to connect to the service. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

notificationManager.removeAllSlots().then(() => {
  console.info(\`Succeeded in removing all slots.\`);
}).catch((err: BusinessError) => {
  console.error(\`Failed to remove all slots. Code is ${err.code}, message is ${err.message}\`);
});

#### notificationManager.isNotificationEnabled11+

isNotificationEnabled(callback: AsyncCallback<boolean>): void

Checks whether notification is enabled for the specified application. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Notification.Notification

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<boolean> | Yes | Callback used to return the result. The value **true** means that the notification can be published; **false** means the opposite. If this API call fails, an error object is returned. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md), [Notification Error Codes](../../error-codes/notification-error-codes/document.md), and [Bundle Error Codes](../../../../application-framework/ability-kit/error-codes/bundle-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 1600001 | Internal error. |
| 1600002 | Marshalling or unmarshalling error. |
| 1600003 | Failed to connect to the service. |
| 1600008 | The user does not exist. |
| 17700001 | The specified bundle name was not found. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let isNotificationEnabledCallback = (err: BusinessError, data: boolean): void => {
  if (err) {
    console.error(\`isNotificationEnabled failed, code is ${err.code}, message is ${err.message}\`);
  } else {
    console.info(\`isNotificationEnabled success, data is ${JSON.stringify(data)}\`);
  }
}

notificationManager.isNotificationEnabled(isNotificationEnabledCallback);

#### notificationManager.isNotificationEnabled11+

isNotificationEnabled(): Promise<boolean>

Checks whether notification is enabled for the specified application. This API uses a promise to return the result.

**System capability**: SystemCapability.Notification.Notification

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return the result. The value **true** means that the notification is enabled, and **false** means the opposite. |

**Error codes**

For details about the error codes, see [Notification Error Codes](../../error-codes/notification-error-codes/document.md) and [Bundle Error Codes](../../../../application-framework/ability-kit/error-codes/bundle-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 1600001 | Internal error. |
| 1600002 | Marshalling or unmarshalling error. |
| 1600003 | Failed to connect to the service. |
| 1600008 | The user does not exist. |
| 17700001 | The specified bundle name was not found. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

notificationManager.isNotificationEnabled().then((data: boolean) => {
  console.info(\`isNotificationEnabled success, data: ${JSON.stringify(data)}\`);
}).catch((err: BusinessError) => {
  console.error(\`isNotificationEnabled failed, code is ${err.code}, message is ${err.message}\`);
});

#### notificationManager.isNotificationEnabledSync12+

isNotificationEnabledSync(): boolean

Checks whether notification is enabled for the specified application. This API returns the result synchronously.

**System capability**: SystemCapability.Notification.Notification

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Result of the notification enabling status. The value **true** means that the notification is enabled, and **false** means the opposite. |

**Error codes**

For details about the error codes, see [Notification Error Codes](../../error-codes/notification-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 1600001 | Internal error. |
| 1600002 | Marshalling or unmarshalling error. |
| 1600003 | Failed to connect to the service. |

**Example**

let enabled: boolean = notificationManager.isNotificationEnabledSync();
console.info(\`isNotificationEnabledSync success, data is : ${JSON.stringify(enabled)}\`);

#### notificationManager.setBadgeNumber10+

setBadgeNumber(badgeNumber: number): Promise<void>

Sets the notification badge number. This API uses a promise to return the result.

**System capability**: SystemCapability.Notification.Notification

**Device behavior differences**: This API can be properly called on devices other than wearables. If it is called on wearables, error code 801 is returned.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| badgeNumber | number | Yes | Notification badge number to set. If **badgeNumber** is set to **0**, badges are cleared; if the value is greater than **99**, **99+** is displayed on the badge. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Notification Error Codes](../../error-codes/notification-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 801 | Capability not supported. |
| 1600001 | Internal error. |
| 1600002 | Marshalling or unmarshalling error. |
| 1600003 | Failed to connect to the service. |
| 1600012 | No memory space. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let badgeNumber: number = 10;
notificationManager.setBadgeNumber(badgeNumber).then(() => {
  console.info(\`Succeeded in setting badge number.\`);
}).catch((err: BusinessError) => {
  console.error(\`Failed to set badge number. Code is ${err.code}, message is ${err.message}\`);
});

#### notificationManager.setBadgeNumber10+

setBadgeNumber(badgeNumber: number, callback: AsyncCallback<void>): void

Sets the notification badge number. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Notification.Notification

**Device behavior differences**: This API can be properly called on devices other than wearables. If it is called on wearables, error code 801 is returned.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| badgeNumber | number | Yes | Notification badge number to set. If **badgeNumber** is set to **0**, badges are cleared; if the value is greater than **99**, **99+** is displayed on the badge. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Notification Error Codes](../../error-codes/notification-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 801 | Capability not supported. |
| 1600001 | Internal error. |
| 1600002 | Marshalling or unmarshalling error. |
| 1600003 | Failed to connect to the service. |
| 1600012 | No memory space. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let setBadgeNumberCallback = (err: BusinessError): void => {
  if (err) {
    console.error(\`Failed to set badge number. Code is ${err.code}, message is ${err.message}\`);
  } else {
    console.info(\`Succeeded in setting badge number.\`);
  }
}
let badgeNumber: number = 10;
notificationManager.setBadgeNumber(badgeNumber, setBadgeNumberCallback);

#### notificationManager.getBadgeNumber22+

getBadgeNumber(): Promise<number>

Obtains the badge number of this application. This API uses a promise to return the result.

**System capability**: SystemCapability.Notification.Notification

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the badge number. (The value is irrelevant to whether notifications and home-screen badges of this application are enabled.) |

**Error codes**

For details about the error codes, see [Notification Error Codes](../../error-codes/notification-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 1600001 | Internal error. |
| 1600002 | Marshalling or unmarshalling error. |
| 1600003 | Failed to connect to the service. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

notificationManager.getBadgeNumber().then((badgeNumber) => {
  console.info(\`Succeeded in getting badge number, badgeNumber is ${JSON.stringify(badgeNumber)}\`);
}).catch((err: BusinessError) => {
  console.error(\`Failed to get badge number. Code is ${err.code}, message is ${err.message}\`);
});

#### notificationManager.getActiveNotificationCount

getActiveNotificationCount(callback: AsyncCallback<number>): void

Obtains the number of active notifications of this application. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Notification.Notification

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<number> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and data is the obtained number of active notifications; otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Notification Error Codes](../../error-codes/notification-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 1600001 | Internal error. |
| 1600002 | Marshalling or unmarshalling error. |
| 1600003 | Failed to connect to the service. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let getActiveNotificationCountCallback = (err: BusinessError, data: number): void => {
  if (err) {
    console.error(\`Failed to get active notification count. Code is ${err.code}, message is ${err.message}\`);
  } else {
    console.info(\`Succeeded in getting active notification count, data is ${JSON.stringify(data)}\`);
  }
}

notificationManager.getActiveNotificationCount(getActiveNotificationCountCallback);

#### notificationManager.getActiveNotificationCount

getActiveNotificationCount(): Promise<number>

Obtains the number of active notifications of this application. This API uses a promise to return the result.

**System capability**: SystemCapability.Notification.Notification

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [Notification Error Codes](../../error-codes/notification-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 1600001 | Internal error. |
| 1600002 | Marshalling or unmarshalling error. |
| 1600003 | Failed to connect to the service. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

notificationManager.getActiveNotificationCount().then((data: number) => {
  console.info(\`Succeeded in getting active notification count, data is ${JSON.stringify(data)}\`);
}).catch((err: BusinessError) => {
  console.error(\`Failed to get active notification count. Code is ${err.code}, message is ${err.message}\`);
});

#### notificationManager.getActiveNotifications

getActiveNotifications(callback: AsyncCallback<Array<NotificationRequest>>): void

Obtains the active notifications of this application. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Notification.Notification

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<Array<[NotificationRequest](../notification/notificationrequest/document.md#notificationrequest-1)\>> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and data is the obtained **NotificationRequest** array; otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Notification Error Codes](../../error-codes/notification-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 1600001 | Internal error. |
| 1600002 | Marshalling or unmarshalling error. |
| 1600003 | Failed to connect to the service. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let getActiveNotificationsCallback = (err: BusinessError, data: Array<notificationManager.NotificationRequest>): void => {
  if (err) {
    console.error(\`Failed to get active notifications. Code is ${err.code}, message is ${err.message}\`);
  } else {
    console.info(\`Succeeded in getting active notifications, data is ${JSON.stringify(data)}\`);
  }
}
notificationManager.getActiveNotifications(getActiveNotificationsCallback);

#### notificationManager.getActiveNotifications

getActiveNotifications(): Promise<Array<NotificationRequest>>

Obtains the active notifications of this application. This API uses a promise to return the result.

**System capability**: SystemCapability.Notification.Notification

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<[NotificationRequest](../notification/notificationrequest/document.md#notificationrequest-1)\>> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [Notification Error Codes](../../error-codes/notification-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 1600001 | Internal error. |
| 1600002 | Marshalling or unmarshalling error. |
| 1600003 | Failed to connect to the service. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

notificationManager.getActiveNotifications().then((data: Array<notificationManager.NotificationRequest>) => {
  console.info(\`Succeeded in getting active notifications, data is ${JSON.stringify(data)}\`);
}).catch((err: BusinessError) => {
  console.error(\`Failed to get active notifications. Code is ${err.code}, message is ${err.message}\`);
});

#### notificationManager.cancelGroup

cancelGroup(groupName: string, callback: AsyncCallback<void>): void

Cancels notifications under a notification group of this application. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Notification.Notification

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| groupName | string | Yes | Name of the notification group, which is specified through [NotificationRequest](../notification/notificationrequest/document.md#notificationrequest-1) when the notification is published. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Notification Error Codes](../../error-codes/notification-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 1600001 | Internal error. |
| 1600002 | Marshalling or unmarshalling error. |
| 1600003 | Failed to connect to the service. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let cancelGroupCallback = (err: BusinessError): void => {
  if (err) {
    console.error(\`Failed to cancel group. Code is ${err.code}, message is ${err.message}\`);
  } else {
    console.info(\`Succeeded in canceling group.\`);
  }
}
let groupName: string = "GroupName";
notificationManager.cancelGroup(groupName, cancelGroupCallback);

#### notificationManager.cancelGroup

cancelGroup(groupName: string): Promise<void>

Cancels notifications under a notification group of this application. This API uses a promise to return the result.

**System capability**: SystemCapability.Notification.Notification

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| groupName | string | Yes | Name of the notification group, which is specified through [NotificationRequest](../notification/notificationrequest/document.md#notificationrequest-1) when the notification is published. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Notification Error Codes](../../error-codes/notification-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 1600001 | Internal error. |
| 1600002 | Marshalling or unmarshalling error. |
| 1600003 | Failed to connect to the service. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let groupName: string = "GroupName";
notificationManager.cancelGroup(groupName).then(() => {
  console.info(\`Succeeded in canceling group.\`);
}).catch((err: BusinessError) => {
  console.error(\`Failed to cancel group. Code is ${err.code}, message is ${err.message}\`);
});

#### notificationManager.isSupportTemplate

isSupportTemplate(templateName: string, callback: AsyncCallback<boolean>): void

Checks whether a specified template is supported before using [NotificationTemplate](../notification/notificationtemplate/document.md) to publish a notification. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Notification.Notification

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| templateName | string | Yes | Template name. Currently, only **downloadTemplate** is supported. |
| callback | AsyncCallback<boolean> | Yes | Callback used to return the result. The value **true** indicates that the template is supported, and **false** indicates the opposite. If this API call fails, an error object is returned. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Notification Error Codes](../../error-codes/notification-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 1600001 | Internal error. |
| 1600002 | Marshalling or unmarshalling error. |
| 1600003 | Failed to connect to the service. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let templateName: string = 'downloadTemplate';
let isSupportTemplateCallback = (err: BusinessError, data: boolean): void => {
  if (err) {
    console.error(\`isSupportTemplate failed, code is ${err.code}, message is ${err.message}\`);
  } else {
    console.info(\`isSupportTemplate success, data: ${JSON.stringify(data)}\`);
  }
}
notificationManager.isSupportTemplate(templateName, isSupportTemplateCallback);

#### notificationManager.isSupportTemplate

isSupportTemplate(templateName: string): Promise<boolean>

Checks whether a specified template is supported before using [NotificationTemplate](../notification/notificationtemplate/document.md) to publish a notification. This API uses a promise to return the result.

**System capability**: SystemCapability.Notification.Notification

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| templateName | string | Yes | Template name. Currently, only **downloadTemplate** is supported. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return the result. The value **true** means that the specified template is supported, and **false** means the opposite. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Notification Error Codes](../../error-codes/notification-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 1600001 | Internal error. |
| 1600002 | Marshalling or unmarshalling error. |
| 1600003 | Failed to connect to the service. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let templateName: string = 'downloadTemplate';
notificationManager.isSupportTemplate(templateName).then((data: boolean) => {
  console.info(\`isSupportTemplate success, data: ${JSON.stringify(data)}\`);
}).catch((err: BusinessError) => {
  console.error(\`isSupportTemplate failed, code is ${err.code}, message is ${err.message}\`);
});

#### notificationManager.requestEnableNotification10+

requestEnableNotification(context: UIAbilityContext, callback: AsyncCallback<void>): void

Requests notification to be enabled for this application. You can call this API to display a dialog box prompting the user to enable notification for your application before publishing a notification. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/TXTm3WLGTDaTh2noocmgvQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062515Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5BA3CDEDEC0672ECCF8524D436AC22A7EF1DBA4FF1D614857DB399486F818970)

-   This API can be called only after the application UI is loaded (that is, [loadContent](../../../../application-framework/ability-kit/arkts-apis/stage-model/ohos-app-ability-uiextensioncontentsession-uiextensionability-ui-operation-class/document.md#loadcontent) is successfully called).
-   When an application uses **requestEnableNotification()** to display a dialog box for notification authorization and the user rejects the authorization, the application cannot use this API to open the dialog box again. However, it can call [openNotificationSettings](#notificationmanageropennotificationsettings13) to open the notification management dialog box.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Notification.Notification

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | [UIAbilityContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md) | Yes | Ability context bound to the notification dialog box. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Notification Error Codes](../../error-codes/notification-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 1600001 | Internal error. |
| 1600002 | Marshalling or unmarshalling error. |
| 1600003 | Failed to connect to the service. |
| 1600004 | Notification disabled. |
| 1600013 | A notification dialog box is already displayed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { hilog } from '@kit.PerformanceAnalysisKit';

class MyAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');
    windowStage.loadContent('pages/Index', (err, data) => {
      if (err.code) {
        hilog.error(0x0000, 'testTag', \`Failed to load the content. Cause: ${JSON.stringify(err) ?? ''}\`);
        return;
      }
      hilog.info(0x0000, 'testTag', \`Succeeded in loading the content. Data: ${JSON.stringify(data) ?? ''}\`);
      let requestEnableNotificationCallback = (err: BusinessError): void => {
        if (err) {
          hilog.error(0x0000, 'testTag', \`\[ANS\] requestEnableNotification failed, code is ${err.code}, message is ${err.message}\`);
        } else {
          hilog.info(0x0000, 'testTag', \`\[ANS\] requestEnableNotification success\`);
        }
      };
      notificationManager.requestEnableNotification(this.context, requestEnableNotificationCallback);
    });
  }
}

#### notificationManager.requestEnableNotification10+

requestEnableNotification(context: UIAbilityContext): Promise<void>

Requests notification to be enabled for this application. You can call this API to display a dialog box prompting the user to enable notification for your application before publishing a notification. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/xrKPZJPoRRSyKxDgDWWBzQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062515Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6AA02BB4B2D5BF2671AA05D5396FB405A92AEAD19750CBF49E4CB044E269C429)

-   This API can be called only after the application UI is loaded (that is, [loadContent](../../../../application-framework/ability-kit/arkts-apis/stage-model/ohos-app-ability-uiextensioncontentsession-uiextensionability-ui-operation-class/document.md#loadcontent) is successfully called).
-   When an application uses **requestEnableNotification()** to display a dialog box for notification authorization and the user rejects the authorization, the application cannot use this API to open the dialog box again. However, it can call [openNotificationSettings](#notificationmanageropennotificationsettings13) to open the notification management dialog box.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Notification.Notification

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | [UIAbilityContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md) | Yes | Ability context bound to the notification dialog box. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Notification Error Codes](../../error-codes/notification-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 1600001 | Internal error. |
| 1600002 | Marshalling or unmarshalling error. |
| 1600003 | Failed to connect to the service. |
| 1600004 | Notification disabled. |
| 1600013 | A notification dialog box is already displayed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { hilog } from '@kit.PerformanceAnalysisKit';

class MyAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');
    windowStage.loadContent('pages/Index', (err, data) => {
      if (err.code) {
        hilog.error(0x0000, 'testTag', \`Failed to load the content. Cause: ${JSON.stringify(err) ?? ''}\`);
        return;
      }
      hilog.info(0x0000, 'testTag', \`Succeeded in loading the content. Data: ${JSON.stringify(data) ?? ''}\`);
      notificationManager.requestEnableNotification(this.context).then(() => {
        hilog.info(0x0000, 'testTag', \`\[ANS\] requestEnableNotification success\`);
      }).catch((err: BusinessError) => {
        hilog.error(0x0000, 'testTag', \`\[ANS\] requestEnableNotification failed, code is ${err.code}, message is ${err.message}\`);
      });
    });
  }
}

#### notificationManager.requestEnableNotification(deprecated)

requestEnableNotification(callback: AsyncCallback<void>): void

Requests notification to be enabled for this application. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/bGCYhiAKRHWVxIEzdReLbg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062515Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=495DB6D0D565D1E56E7BD16A05CB2A5F6F742FD12F37EB8CDC7668BB63DC2B5D)

This API is supported since API version 9 and deprecated since API version 12. You are advised to use [requestEnableNotification](#notificationmanagerrequestenablenotification10) with context instead.

**System capability**: SystemCapability.Notification.Notification

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Notification Error Codes](../../error-codes/notification-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 1600001 | Internal error. |
| 1600002 | Marshalling or unmarshalling error. |
| 1600003 | Failed to connect to the service. |
| 1600004 | Notification disabled. |
| 1600013 | A notification dialog box is already displayed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let requestEnableNotificationCallback = (err: BusinessError): void => {
  if (err) {
    console.error(\`requestEnableNotification failed, code is ${err.code}, message is ${err.message}\`);
  } else {
    console.info("requestEnableNotification success");
  }
};
notificationManager.requestEnableNotification(requestEnableNotificationCallback);

#### notificationManager.requestEnableNotification(deprecated)

requestEnableNotification(): Promise<void>

Requests notification to be enabled for this application. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/l5CoUs9PT0CJuFKhkP05jQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062515Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2CEA2F7BBD026CA59F50218BB78491CB655AFB4B528DE3C3F13A9D0C8D8E92A6)

This API is supported since API version 9 and deprecated since API version 12. You are advised to use [requestEnableNotification](#notificationmanagerrequestenablenotification10-1) with context instead.

**System capability**: SystemCapability.Notification.Notification

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Notification Error Codes](../../error-codes/notification-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 1600001 | Internal error. |
| 1600002 | Marshalling or unmarshalling error. |
| 1600003 | Failed to connect to the service. |
| 1600004 | Notification disabled. |
| 1600013 | A notification dialog box is already displayed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

notificationManager.requestEnableNotification().then(() => {
  console.info("requestEnableNotification success");
}).catch((err: BusinessError) => {
  console.error(\`requestEnableNotification failed, code is ${err.code}, message is ${err.message}\`);
});

#### notificationManager.isDistributedEnabled

isDistributedEnabled(callback: AsyncCallback<boolean>): void

Checks whether the device supports cross-device notifications. This API uses an asynchronous callback to return the result.

**Device behavior differences**: This API can be properly called on devices other than wearables and TVs. If it is called on wearables and TVs, **false** is returned.

**System capability**: SystemCapability.Notification.Notification

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<boolean> | Yes | Callback used to return the result. The value **true** means that the cross-device notification is supported; **false** means the opposite. If this API call fails, an error object is returned. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Notification Error Codes](../../error-codes/notification-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 1600001 | Internal error. |
| 1600002 | Marshalling or unmarshalling error. |
| 1600003 | Failed to connect to the service. |
| 1600010 | Distributed operation failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let isDistributedEnabledCallback = (err: BusinessError, data: boolean): void => {
  if (err) {
    console.error(\`isDistributedEnabled failed, code is ${err.code}, message is ${err.message}\`);
  } else {
    console.info(\`isDistributedEnabled success ${JSON.stringify(data)}\`);
  }
};
notificationManager.isDistributedEnabled(isDistributedEnabledCallback);

#### notificationManager.isDistributedEnabled

isDistributedEnabled(): Promise<boolean>

Checks whether the device supports cross-device notifications. This API uses a promise to return the result.

**Device behavior differences**: This API can be properly called on devices other than wearables and TVs. If it is called on wearables and TVs, **false** is returned.

**System capability**: SystemCapability.Notification.Notification

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return the result. The value **true** means that the cross-device notification is supported; **false** means the opposite. |

**Error codes**

For details about the error codes, see [Notification Error Codes](../../error-codes/notification-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 1600001 | Internal error. |
| 1600002 | Marshalling or unmarshalling error. |
| 1600003 | Failed to connect to the service. |
| 1600010 | Distributed operation failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

notificationManager.isDistributedEnabled().then((data: boolean) => {
  console.info(\`isDistributedEnabled success, data: ${JSON.stringify(data)}\`);
}).catch((err: BusinessError) => {
  console.error(\`isDistributedEnabled failed, code is ${err.code}, message is ${err.message}\`);
});

#### notificationManager.openNotificationSettings13+

openNotificationSettings(context: UIAbilityContext): Promise<void>

Opens the notification settings page of the application, which is displayed in semi-modal mode and can be used to set the notification enabling and notification mode. This API uses a promise to return the result.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Notification.NotificationSettings

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | [UIAbilityContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md) | Yes | Ability context bound to the notification settings page. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Notification Error Codes](../../error-codes/notification-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported. |
| 1600001 | Internal error. |
| 1600003 | Failed to connect to the service. |
| 1600018 | The notification settings window is already displayed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { hilog } from '@kit.PerformanceAnalysisKit';

class MyAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');
    windowStage.loadContent('pages/Index', (err, data) => {
      if (err.code) {
        hilog.error(0x0000, 'testTag', \`Failed to load the content. Cause: ${JSON.stringify(err) ?? ''}\`);
        return;
      }
      hilog.info(0x0000, 'testTag', \`Succeeded in loading the content. Data: ${JSON.stringify(data) ?? ''}\`);
      notificationManager.openNotificationSettings(this.context).then(() => {
        hilog.info(0x0000, 'testTag', \`\[ANS\] openNotificationSettings success\`);
      }).catch((err: BusinessError) => {
        hilog.error(0x0000, 'testTag', \`\[ANS\] openNotificationSettings failed, code is ${err.code}, message is ${err.message}\`);
      });
    });
  }
}

#### notificationManager.getNotificationSetting20+

getNotificationSetting(): Promise<NotificationSetting>

Obtains the notification settings of an application. This API uses a promise to return the result.

**System capability**: SystemCapability.Notification.Notification

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[NotificationSetting](#notificationsetting20)\> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [Notification Error Codes](../../error-codes/notification-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 1600001 | Internal error. |
| 1600002 | Marshalling or unmarshalling error. |
| 1600003 | Failed to connect to the service. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

notificationManager.getNotificationSetting().then((data: notificationManager.NotificationSetting) => {
    console.info(\`getNotificationSetting success, data: ${JSON.stringify(data)}\`);
}).catch((err: BusinessError) => {
    console.error(\`getNotificationSetting failed, code is ${err.code}, message is ${err.message}\`);
});

#### ContentType

Enumerates the notification content types.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Notification.Notification

| Name | Value | Description |
| :-- | :-- | :-- |
| NOTIFICATION\_CONTENT\_BASIC\_TEXT | 0 | Normal text notification. |
| NOTIFICATION\_CONTENT\_LONG\_TEXT | 1 | Long text notification. |
| NOTIFICATION\_CONTENT\_PICTURE | 2 | Picture-attached notification. |
| NOTIFICATION\_CONTENT\_CONVERSATION | 3 | Conversation notification. Not supported currently. |
| NOTIFICATION\_CONTENT\_MULTILINE | 4 | Multi-line text notification. |
| NOTIFICATION\_CONTENT\_SYSTEM\_LIVE\_VIEW11+ | 5 | Live view notification. A third-party application cannot directly create a notification of this type. After the system proxy creates a system live view, the third-party application publishes a notification with the same ID to update the specified content. |
| NOTIFICATION\_CONTENT\_LIVE\_VIEW11+ | 6 | Common live view notification. Available only to system applications. |

#### SlotLevel

Enumerates the notification level.

**System capability**: SystemCapability.Notification.Notification

| Name | Value | Description |
| :-- | :-- | :-- |
| LEVEL\_NONE | 0 | Notification is disabled. |
| LEVEL\_MIN | 1 | Notification is enabled, but the notification icon is not displayed in the status bar, with no alert tone and banner. |
| LEVEL\_LOW | 2 | Notification is enabled, and the notification icon is displayed in the status bar, with no alert tone and banner. |
| LEVEL\_DEFAULT | 3 | Notification is enabled, and the notification icon is displayed in the status bar, with an alert tone but no banner. |
| LEVEL\_HIGH | 4 | Notification is enabled, and the notification icon is displayed in the status bar, with an alert tone and banner. |

#### SlotType

Enumerates the notification slot types.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Notification.Notification

| Name | Value | Description |
| :-- | :-- | :-- |
| UNKNOWN\_TYPE | 0 | Unknown type. This type corresponds to [SlotLevel](#slotlevel) being **LEVEL\_MIN**. |
| SOCIAL\_COMMUNICATION | 1 | Notification slot for social communication. This type corresponds to [SlotLevel](#slotlevel) being **LEVEL\_HIGH**. |
| SERVICE\_INFORMATION | 2 | Notification slot for service information. This type corresponds to [SlotLevel](#slotlevel) being **LEVEL\_HIGH**. |
| CONTENT\_INFORMATION | 3 | Notification slot for content consultation. This type corresponds to [SlotLevel](#slotlevel) being **LEVEL\_MIN**. |
| LIVE\_VIEW11+ | 4 | Live view. A third-party application cannot directly create a notification of this slot type. After the system proxy creates a system live view, the third-party application publishes a notification with the same ID to update the specified content. This type corresponds to [SlotLevel](#slotlevel) being **LEVEL\_DEFAULT**. |
| CUSTOMER\_SERVICE11+ | 5 | Notification slot for customer service message. This type is used for messages between users and customer service providers. The messages must be initiated by users. This type corresponds to [SlotLevel](#slotlevel) being **LEVEL\_DEFAULT**. |
| OTHER\_TYPES | 0xFFFF | Notification slot for other purposes. This type corresponds to [SlotLevel](#slotlevel) being **LEVEL\_MIN**. |

#### NotificationSetting20+

Describes notification settings, including whether to enable vibration and ringtone.

**System capability**: SystemCapability.Notification.Notification

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| vibrationEnabled | boolean | No | No | 
Whether to enable vibration.

\- **true**: enabled.

\- **false**: disable.

 |
| soundEnabled | boolean | No | No | 

Whether to enable ringtone.

\- **true**: enabled.

\- **false**: disable.

 |

#### BundleOption

type BundleOption = \_BundleOption

Describes the bundle information of an application.

**System capability**: SystemCapability.Notification.Notification

| Type | Description |
| :-- | :-- |
| [\_BundleOption](../notification/notificationcommondef/document.md#bundleoption) | Bundle information. |

#### NotificationActionButton

type NotificationActionButton = \_NotificationActionButton

Describes the operation button displayed in the notification.

**System capability**: SystemCapability.Notification.Notification

| Type | Description |
| :-- | :-- |
| [\_NotificationActionButton](../notification/notificationactionbutton/document.md) | Operation button. |

#### NotificationBasicContent

type NotificationBasicContent = \_NotificationBasicContent

Describes the normal text notification.

**System capability**: SystemCapability.Notification.Notification

| Type | Description |
| :-- | :-- |
| [\_NotificationBasicContent](../notification/notificationcontent/document.md#notificationbasiccontent) | Normal text notification. |

#### NotificationContent

type NotificationContent = \_NotificationContent

Describes the notification content.

**System capability**: SystemCapability.Notification.Notification

| Type | Description |
| :-- | :-- |
| [\_NotificationContent](../notification/notificationcontent/document.md#notificationcontent-1) | Notification content. |

#### NotificationLongTextContent

type NotificationLongTextContent = \_NotificationLongTextContent

Describes the long text notification.

**System capability**: SystemCapability.Notification.Notification

| Type | Description |
| :-- | :-- |
| [\_NotificationLongTextContent](../notification/notificationcontent/document.md#notificationlongtextcontent) | Long text notification. |

#### NotificationMultiLineContent

type NotificationMultiLineContent = \_NotificationMultiLineContent

Describes the multi-line text notification.

**System capability**: SystemCapability.Notification.Notification

| Type | Description |
| :-- | :-- |
| [\_NotificationMultiLineContent](../notification/notificationcontent/document.md#notificationmultilinecontent) | Multi-line text notification. |

#### NotificationPictureContent

type NotificationPictureContent = \_NotificationPictureContent

Describes the picture-attached notification.

**System capability**: SystemCapability.Notification.Notification

| Type | Description |
| :-- | :-- |
| [\_NotificationPictureContent](../notification/notificationcontent/document.md#notificationpicturecontent) | Picture-attached notification |

#### NotificationSystemLiveViewContent11+

type NotificationSystemLiveViewContent = \_NotificationSystemLiveViewContent

Describes the system live view notification.

**System capability**: SystemCapability.Notification.Notification

| Type | Description |
| :-- | :-- |
| [\_NotificationSystemLiveViewContent](../notification/notificationcontent/document.md#notificationsystemliveviewcontent) | System live view notification. |

#### NotificationRequest

type NotificationRequest = \_NotificationRequest

Describes the notification request.

**System capability**: SystemCapability.Notification.Notification

| Type | Description |
| :-- | :-- |
| [\_NotificationRequest](../notification/notificationrequest/document.md#notificationrequest-1) | Notification request. |

#### DistributedOptions

type DistributedOptions = \_DistributedOptions

Describes distributed notification options.

**System capability**: SystemCapability.Notification.Notification

| Type | Description |
| :-- | :-- |
| [\_DistributedOptions](../notification/notificationrequest/document.md#distributedoptions8) | Distributed notification options. |

#### NotificationSlot

type NotificationSlot = \_NotificationSlot

Describes the notification slot.

**System capability**: SystemCapability.Notification.Notification

| Type | Description |
| :-- | :-- |
| [\_NotificationSlot](../notification/notificationslot/document.md) | Notification slot. |

#### NotificationTemplate

type NotificationTemplate = \_NotificationTemplate

Describes the notification template.

**System capability**: SystemCapability.Notification.Notification

| Type | Description |
| :-- | :-- |
| [\_NotificationTemplate](../notification/notificationtemplate/document.md) | Notification template. |

#### NotificationUserInput

type NotificationUserInput = \_NotificationUserInput

Describes the user input for the notification.

**System capability**: SystemCapability.Notification.Notification

| Type | Description |
| :-- | :-- |
| [\_NotificationUserInput](../notification/notificationuserinput/document.md) | User input. |

#### NotificationCapsule11+

type NotificationCapsule = \_NotificationCapsule

Describes the notification capsule.

**System capability**: SystemCapability.Notification.Notification

| Type | Description |
| :-- | :-- |
| [\_NotificationCapsule](../notification/notificationcontent/document.md#notificationcapsule11) | Notification capsule. |

#### NotificationButton11+

type NotificationButton = \_NotificationButton

Describes the notification button.

**System capability**: SystemCapability.Notification.Notification

| Type | Description |
| :-- | :-- |
| [\_NotificationButton](../notification/notificationcontent/document.md#notificationbutton11) | Notification button. |

#### NotificationTime11+

type NotificationTime = \_NotificationTime

Describes the notification timing information.

**System capability**: SystemCapability.Notification.Notification

| Type | Description |
| :-- | :-- |
| [\_NotificationTime](../notification/notificationcontent/document.md#notificationtime11) | Notification timing information. |

#### NotificationProgress11+

type NotificationProgress = \_NotificationProgress

Describes the notification progress.

**System capability**: SystemCapability.Notification.Notification

| Type | Description |
| :-- | :-- |
| [\_NotificationProgress](../notification/notificationcontent/document.md#notificationprogress11) | Notification progress. |
