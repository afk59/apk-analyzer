# @ohos.notification (Notification)

The **Notification** module provides notification management capabilities, covering notifications, notification slots, notification subscription, notification enabled status, and notification badge status.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/5C5H6WaBRZGoroUk5cF_7Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062516Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=52640415029F6D6689FD9D8191F61EA0BA37EBD886697AAA2ED4FF5799EE408D)

The APIs of this module are deprecated since API version 9. You are advised to use [@ohos.notificationManager](../../ohos-notificationmanager-notificationmanager/document.md) instead.

The initial APIs of this module are supported since API version 7. Newly added APIs will be marked with a superscript to indicate their earliest API version.

Notification subscription and unsubscription APIs are available only to system applications.

#### Modules to Import

import Notification from '@ohos.notification';

#### Notification.publish

publish(request: NotificationRequest, callback: AsyncCallback<void>): void

Publishes a notification. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Notification.Notification

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| request | [NotificationRequest](#notificationrequest) | Yes | Content and related configuration of the notification to publish. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Example**

import NotificationManager from '@ohos.notificationManager';
import Base from '@ohos.base';

// publish callback
let publishCallback = (err: Base.BusinessError) => {
  if (err) {
    console.error(\`publish failed, code is ${err}\`);
  } else {
    console.info("publish success");
  }
}
// NotificationRequest object
let notificationRequest: NotificationManager.NotificationRequest = {
  id: 1,
  content: {
    contentType: Notification.ContentType.NOTIFICATION\_CONTENT\_BASIC\_TEXT,
    normal: {
      title: "test\_title",
      text: "test\_text",
      additionalText: "test\_additionalText"
    }
  }
};
Notification.publish(notificationRequest, publishCallback);

#### Notification.publish

publish(request: NotificationRequest): Promise<void>

Publishes a notification. This API uses a promise to return the result.

**System capability**: SystemCapability.Notification.Notification

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| request | [NotificationRequest](#notificationrequest) | Yes | Content and related configuration of the notification to publish. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

import NotificationManager from '@ohos.notificationManager';
import Base from '@ohos.base';

// NotificationRequest object
let notificationRequest: NotificationManager.NotificationRequest = {
  id: 1,
  content: {
    contentType: Notification.ContentType.NOTIFICATION\_CONTENT\_BASIC\_TEXT,
    normal: {
      title: "test\_title",
      text: "test\_text",
      additionalText: "test\_additionalText"
    }
  }
};
Notification.publish(notificationRequest).then(() => {
  console.info("publish success");
}).catch((err: Base.BusinessError) => {
  console.error(\`publish failed, code is ${err}\`);
});

#### Notification.cancel

cancel(id: number, label: string, callback: AsyncCallback<void>): void

Cancels a notification with the specified ID and label. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Notification.Notification

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| id | number | Yes | Notification ID. |
| label | string | Yes | Notification label. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Example**

import Base from '@ohos.base';

// cancel callback
let cancelCallback = (err: Base.BusinessError) => {
  if (err) {
    console.info("cancel failed " + JSON.stringify(err));
  } else {
    console.info("cancel success");
  }
}
Notification.cancel(0, "label", cancelCallback);

#### Notification.cancel

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

**Example**

import Base from '@ohos.base';

Notification.cancel(0).then(() => {
  console.info("cancel success");
}).catch((err: Base.BusinessError) => {
  console.error(\`cancel failed, code is ${err}\`);
});

#### Notification.cancel

cancel(id: number, callback: AsyncCallback<void>): void

Cancels a notification with the specified ID. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Notification.Notification

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| id | number | Yes | Notification ID. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Example**

import Base from '@ohos.base';

// cancel callback
let cancelCallback = (err: Base.BusinessError) => {
  if (err) {
    console.info("cancel failed " + JSON.stringify(err));
  } else {
    console.info("cancel success");
  }
}
Notification.cancel(0, cancelCallback);

#### Notification.cancelAll

cancelAll(callback: AsyncCallback<void>): void

Cancels all notifications. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Notification.Notification

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Example**

import Base from '@ohos.base';

// cancel callback
let cancelAllCallback = (err: Base.BusinessError) => {
  if (err) {
    console.info("cancelAll failed " + JSON.stringify(err));
  } else {
    console.info("cancelAll success");
  }
}
Notification.cancelAll(cancelAllCallback);

#### Notification.cancelAll

cancelAll(): Promise<void>

Cancels all notifications. This API uses a promise to return the result.

**System capability**: SystemCapability.Notification.Notification

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

import Base from '@ohos.base';

Notification.cancelAll().then(() => {
  console.info("cancelAll success");
}).catch((err: Base.BusinessError) => {
  console.error(\`cancelAll failed, code is ${err}\`);
});

#### Notification.addSlot

addSlot(type: SlotType, callback: AsyncCallback<void>): void

Adds a notification slot of a specified type. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Notification.Notification

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SlotType](#slottype) | Yes | Type of the notification slot to add. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Example**

import Base from '@ohos.base';

// addSlot callback
let addSlotCallBack = (err: Base.BusinessError) => {
  if (err) {
    console.info("addSlot failed " + JSON.stringify(err));
  } else {
    console.info("addSlot success");
  }
}
Notification.addSlot(Notification.SlotType.SOCIAL\_COMMUNICATION, addSlotCallBack);

#### Notification.addSlot

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

**Example**

import Base from '@ohos.base';

Notification.addSlot(Notification.SlotType.SOCIAL\_COMMUNICATION).then(() => {
  console.info("addSlot success");
}).catch((err: Base.BusinessError) => {
  console.error(\`addSlot failed, code is ${err}\`);
});

#### Notification.getSlot

getSlot(slotType: SlotType, callback: AsyncCallback<NotificationSlot>): void

Obtains a notification slot of a specified type. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Notification.Notification

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| slotType | [SlotType](#slottype) | Yes | Type of the notification slot, which can be used for social communication, service information, content consultation, and other purposes. |
| callback | AsyncCallback<[NotificationSlot](#notificationslot)\> | Yes | Callback used to return the result. |

**Example**

import Base from '@ohos.base';

// getSlot callback
let getSlotCallback = (err: Base.BusinessError) => {
  if (err) {
    console.info("getSlot failed " + JSON.stringify(err));
  } else {
    console.info("getSlot success");
  }
}
let slotType: Notification.SlotType = Notification.SlotType.SOCIAL\_COMMUNICATION;
Notification.getSlot(slotType, getSlotCallback);

#### Notification.getSlot

getSlot(slotType: SlotType): Promise<NotificationSlot>

Obtains a notification slot of a specified type. This API uses a promise to return the result.

**System capability**: SystemCapability.Notification.Notification

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| slotType | [SlotType](#slottype) | Yes | Type of the notification slot, which can be used for social communication, service information, content consultation, and other purposes. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<NotificationSlot> | Promise used to return the result. |

**Example**

import Base from '@ohos.base';

let slotType: Notification.SlotType = Notification.SlotType.SOCIAL\_COMMUNICATION;
Notification.getSlot(slotType).then((data) => {
  console.info("getSlot success, data: " + JSON.stringify(data));
}).catch((err: Base.BusinessError) => {
  console.error(\`getSlot failed, code is ${err}\`);
});

#### Notification.getSlots

getSlots(callback: AsyncCallback<Array<NotificationSlot>>): void

Obtains all notification slots. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Notification.Notification

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<Array<[NotificationSlot](#notificationslot)\>> | Yes | Callback used to return the result. |

**Example**

import Base from '@ohos.base';

// getSlots callback
function getSlotsCallback(err: Base.BusinessError) {
  if (err) {
    console.info("getSlots failed " + JSON.stringify(err));
  } else {
    console.info("getSlots success");
  }
}
Notification.getSlots(getSlotsCallback);

#### Notification.getSlots

getSlots(): Promise<Array<NotificationSlot>>

Obtains all notification slots of this application. This API uses a promise to return the result.

**System capability**: SystemCapability.Notification.Notification

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<[NotificationSlot](#notificationslot)\>> | Promise used to return the result. |

**Example**

import Base from '@ohos.base';

Notification.getSlots().then((data) => {
  console.info("getSlots success, data: " + JSON.stringify(data));
}).catch((err: Base.BusinessError) => {
  console.error(\`getSlots failed, code is ${err}\`);
});

#### Notification.removeSlot

removeSlot(slotType: SlotType, callback: AsyncCallback<void>): void

Removes a notification slot of a specified type. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Notification.Notification

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| slotType | [SlotType](#slottype) | Yes | Type of the notification slot, which can be used for social communication, service information, content consultation, and other purposes. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Example**

import Base from '@ohos.base';

// removeSlot callback
let removeSlotCallback = (err: Base.BusinessError) => {
  if (err) {
    console.info("removeSlot failed " + JSON.stringify(err));
  } else {
    console.info("removeSlot success");
  }
}
let slotType: Notification.SlotType = Notification.SlotType.SOCIAL\_COMMUNICATION;
Notification.removeSlot(slotType, removeSlotCallback);

#### Notification.removeSlot

removeSlot(slotType: SlotType): Promise<void>

Removes a notification slot of a specified type. This API uses a promise to return the result.

**System capability**: SystemCapability.Notification.Notification

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| slotType | [SlotType](#slottype) | Yes | Type of the notification slot, which can be used for social communication, service information, content consultation, and other purposes. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

import Base from '@ohos.base';

let slotType: Notification.SlotType = Notification.SlotType.SOCIAL\_COMMUNICATION;
Notification.removeSlot(slotType).then(() => {
  console.info("removeSlot success");
}).catch((err: Base.BusinessError) => {
  console.error(\`removeSlot failed, code is ${err}\`);
});

#### Notification.removeAllSlots

removeAllSlots(callback: AsyncCallback<void>): void

Removes all notification slots. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Notification.Notification

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Example**

import Base from '@ohos.base';

let removeAllCallBack = (err: Base.BusinessError) => {
  if (err) {
    console.info("removeAllSlots failed " + JSON.stringify(err));
  } else {
    console.info("removeAllSlots success");
  }
}
Notification.removeAllSlots(removeAllCallBack);

#### Notification.removeAllSlots

removeAllSlots(): Promise<void>

Removes all notification slots. This API uses a promise to return the result.

**System capability**: SystemCapability.Notification.Notification

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

import Base from '@ohos.base';

Notification.removeAllSlots().then(() => {
  console.info("removeAllSlots success");
}).catch((err: Base.BusinessError) => {
  console.error(\`removeAllSlots failed, code is ${err}\`);
});

#### Notification.getActiveNotificationCount

getActiveNotificationCount(callback: AsyncCallback<number>): void

Obtains the number of active notifications of this application. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Notification.Notification

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<number> | Yes | Callback used to return the result. |

**Example**

import Base from '@ohos.base';

let getActiveNotificationCountCallback = (err: Base.BusinessError, data: number) => {
  if (err) {
    console.info("getActiveNotificationCount failed " + JSON.stringify(err));
  } else {
    console.info("getActiveNotificationCount success");
  }
}

Notification.getActiveNotificationCount(getActiveNotificationCountCallback);

#### Notification.getActiveNotificationCount

getActiveNotificationCount(): Promise<number>

Obtains the number of active notifications of this application. This API uses a promise to return the result.

**System capability**: SystemCapability.Notification.Notification

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the result. |

**Example**

import Base from '@ohos.base';

Notification.getActiveNotificationCount().then((data: number) => {
  console.info("getActiveNotificationCount success, data: " + JSON.stringify(data));
}).catch((err: Base.BusinessError) => {
  console.error(\`getAllActiveNotifications failed, code is ${err}\`);
});

#### Notification.getActiveNotifications

getActiveNotifications(callback: AsyncCallback<Array<NotificationRequest>>): void

Obtains active notifications of this application. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Notification.Notification

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<Array<[NotificationRequest](#notificationrequest)\>> | Yes | Callback used to return the result. |

**Example**

import Base from '@ohos.base';
import NotificationManager from '@ohos.notificationManager';

let getActiveNotificationsCallback = (err: Base.BusinessError, data: NotificationManager.NotificationRequest\[\]) => {
  if (err) {
    console.info("getActiveNotifications failed " + JSON.stringify(err));
  } else {
    console.info("getActiveNotifications success");
  }
}

Notification.getActiveNotifications(getActiveNotificationsCallback);

#### Notification.getActiveNotifications

getActiveNotifications(): Promise<Array<[NotificationRequest](#notificationrequest)\>>

Obtains active notifications of this application. This API uses a promise to return the result.

**System capability**: SystemCapability.Notification.Notification

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<[NotificationRequest](#notificationrequest)\>> | Promise used to return the result. |

**Example**

import Base from '@ohos.base';
import NotificationManager from '@ohos.notificationManager';

Notification.getActiveNotifications().then((data: NotificationManager.NotificationRequest\[\]) => {
  console.info("removeGroupByBundle success, data: " + JSON.stringify(data));
}).catch((err: Base.BusinessError) => {
  console.error(\`removeGroupByBundle failed, code is ${err}\`);
});

#### Notification.cancelGroup8+

cancelGroup(groupName: string, callback: AsyncCallback<void>): void

Cancels notifications under a notification group of this application. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Notification.Notification

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| groupName | string | Yes | Name of the notification group, which is specified through [NotificationRequest](#notificationrequest) when the notification is published. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Example**

import Base from '@ohos.base';

let cancelGroupCallback = (err: Base.BusinessError) => {
  if (err) {
    console.info("cancelGroup failed " + JSON.stringify(err));
  } else {
    console.info("cancelGroup success");
  }
}

let groupName: string = "GroupName";

Notification.cancelGroup(groupName, cancelGroupCallback);

#### Notification.cancelGroup8+

cancelGroup(groupName: string): Promise<void>

Cancels notifications under a notification group of this application. This API uses a promise to return the result.

**System capability**: SystemCapability.Notification.Notification

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| groupName | string | Yes | Name of the notification group. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

import Base from '@ohos.base';

let groupName: string = "GroupName";
Notification.cancelGroup(groupName).then(() => {
  console.info("cancelGroup success");
}).catch((err: Base.BusinessError) => {
  console.error(\`cancelGroup failed, code is ${err}\`);
});

#### Notification.isSupportTemplate8+

isSupportTemplate(templateName: string, callback: AsyncCallback<boolean>): void

Checks whether a specified template exists. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Notification.Notification

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| templateName | string | Yes | Template name. |
| callback | AsyncCallback<boolean> | Yes | Callback used to return the result. |

**Example**

import Base from '@ohos.base';

let templateName: string = 'process';
function isSupportTemplateCallback(err: Base.BusinessError, data: boolean) {
  if (err) {
    console.info("isSupportTemplate failed " + JSON.stringify(err));
  } else {
    console.info("isSupportTemplate success");
  }
}

Notification.isSupportTemplate(templateName, isSupportTemplateCallback);

#### Notification.isSupportTemplate8+

isSupportTemplate(templateName: string): Promise<boolean>

Checks whether a specified template exists. This API uses a promise to return the result.

**System capability**: SystemCapability.Notification.Notification

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| templateName | string | Yes | Template name. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return the result. |

**Example**

import Base from '@ohos.base';

let templateName: string = 'process';
Notification.isSupportTemplate(templateName).then((data: boolean) => {
  console.info("isSupportTemplate success, data: " + JSON.stringify(data));
}).catch((err: Base.BusinessError) => {
  console.error(\`isSupportTemplate failed, code is ${err}\`);
});

#### Notification.requestEnableNotification8+

requestEnableNotification(callback: AsyncCallback<void>): void

Requests notification to be enabled for this application. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Notification.Notification

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Example**

import Base from '@ohos.base';

let requestEnableNotificationCallback = (err: Base.BusinessError) => {
  if (err) {
    console.info("requestEnableNotification failed " + JSON.stringify(err));
  } else {
    console.info("requestEnableNotification success");
  }
};

Notification.requestEnableNotification(requestEnableNotificationCallback);

#### Notification.requestEnableNotification8+

requestEnableNotification(): Promise<void>

Requests notification to be enabled for this application. This API uses a promise to return the result.

**System capability**: SystemCapability.Notification.Notification

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

import Base from '@ohos.base';

Notification.requestEnableNotification().then(() => {
  console.info("requestEnableNotification success");
}).catch((err: Base.BusinessError) => {
  console.error(\`requestEnableNotification failed, code is ${err}\`);
});

#### Notification.isDistributedEnabled8+

isDistributedEnabled(callback: AsyncCallback<boolean>): void

Checks whether this device supports distributed notifications. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Notification.Notification

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<boolean> | Yes | Callback used to return the result. |

**Example**

import Base from '@ohos.base';

let isDistributedEnabledCallback = (err: Base.BusinessError, data: boolean) => {
  if (err) {
    console.info("isDistributedEnabled failed " + JSON.stringify(err));
  } else {
    console.info("isDistributedEnabled success " + JSON.stringify(data));
  }
};

Notification.isDistributedEnabled(isDistributedEnabledCallback);

#### Notification.isDistributedEnabled8+

isDistributedEnabled(): Promise<boolean>

Checks whether this device supports distributed notifications. This API uses a promise to return the result.

**System capability**: SystemCapability.Notification.Notification

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return the result. |

**Example**

import Base from '@ohos.base';

Notification.isDistributedEnabled().then((data: boolean) => {
    console.info("isDistributedEnabled success, data: " + JSON.stringify(data));
}).catch((err: Base.BusinessError) => {
  console.error(\`isDistributedEnabled failed, code is ${err}\`);
});

#### ContentType

**System capability**: SystemCapability.Notification.Notification

| Name | Value | Description |
| :-- | :-- | :-- |
| NOTIFICATION\_CONTENT\_BASIC\_TEXT | NOTIFICATION\_CONTENT\_BASIC\_TEXT | Normal text notification. |
| NOTIFICATION\_CONTENT\_LONG\_TEXT | NOTIFICATION\_CONTENT\_LONG\_TEXT | Long text notification. |
| NOTIFICATION\_CONTENT\_PICTURE | NOTIFICATION\_CONTENT\_PICTURE | Picture-attached notification. |
| NOTIFICATION\_CONTENT\_CONVERSATION | NOTIFICATION\_CONTENT\_CONVERSATION | Conversation notification. |
| NOTIFICATION\_CONTENT\_MULTILINE | NOTIFICATION\_CONTENT\_MULTILINE | Multi-line text notification. |

#### SlotLevel

**System capability**: SystemCapability.Notification.Notification

| Name | Value | Description |
| :-- | :-- | :-- |
| LEVEL\_NONE | 0 | The notification function is disabled. |
| LEVEL\_MIN | 1 | The notification function is enabled, but the notification icon is not displayed in the status bar, with no banner or alert tone. |
| LEVEL\_LOW | 2 | The notification function is enabled, and the notification icon is displayed in the status bar, with no banner or alert tone. |
| LEVEL\_DEFAULT | 3 | The notification feature is enabled, and the notification icon is displayed in the status bar, with an alert tone but no banner. |
| LEVEL\_HIGH | 4 | The notification feature is enabled, and the notification icon is displayed in the status bar, with an alert tone and banner. |

#### BundleOptiondeprecated

**System capability**: SystemCapability.Notification.Notification

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/tILkUycGSRScxrOKGCIYyw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062516Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BB888DE9791649B8A788E7A727C323E66A7C8DC63422E17D0795C6D34799307E)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [notificationManager.BundleOption](../../notification/notificationcommondef/document.md#bundleoption) instead.

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| bundle | string | Yes | Bundle information of the application. |
| uid | number | No | User ID. The default value is 0. |

#### NotificationKeydeprecated

**System capability**: SystemCapability.Notification.Notification

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/B7FqQVzSTQK6-8eJivU2Ew/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062516Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=095F75A21185CA4C6DC9F8AB120B5DA2A187419C73A28C512A034FB2183D8EAA)

This API is supported since API version 7 and deprecated since API version 9.

| Name | Type | Readable | Writable | Description |
| :-- | :-- | :-- | :-- | :-- |
| id | number | Yes | Yes | Notification ID. |
| label | string | Yes | Yes | Notification label. |

#### SlotType

**System capability**: SystemCapability.Notification.Notification

| Name | Value | Description |
| :-- | :-- | :-- |
| UNKNOWN\_TYPE | 0 | Unknown type. |
| SOCIAL\_COMMUNICATION | 1 | Notification slot for social communication. |
| SERVICE\_INFORMATION | 2 | Notification slot for service information. |
| CONTENT\_INFORMATION | 3 | Notification slot for content consultation. |
| OTHER\_TYPES | 0xFFFF | Notification slot for other purposes. |

#### NotificationActionButton

Describes the button displayed in the notification.

**System capability**: SystemCapability.Notification.Notification

| Name | Type | Readable | Writable | Description |
| :-- | :-- | :-- | :-- | :-- |
| title | string | Yes | Yes | Button title. |
| wantAgent | [WantAgent](../../../../../application-framework/ability-kit/arkts-apis/apis-no-longer-maintained/ohos-wantagent-wantagent-module/document.md) | Yes | Yes | **WantAgent** of the button. |
| extras | { \[key: string\]: any } | Yes | Yes | Extra information of the button. |
| userInput8+ | [NotificationUserInput](#notificationuserinput8) | Yes | Yes | User input object. |

#### NotificationBasicContent

Describes the normal text notification.

**System capability**: SystemCapability.Notification.Notification

| Name | Type | Readable | Writable | Description |
| :-- | :-- | :-- | :-- | :-- |
| title | string | Yes | Yes | Notification title. |
| text | string | Yes | Yes | Notification content. |
| additionalText | string | Yes | Yes | Additional information of the notification. |

#### NotificationLongTextContent

Describes the long text notification.

**System capability**: SystemCapability.Notification.Notification

| Name | Type | Readable | Writable | Description |
| :-- | :-- | :-- | :-- | :-- |
| title | string | Yes | Yes | Notification title. |
| text | string | Yes | Yes | Notification content. |
| additionalText | string | Yes | Yes | Additional information of the notification. |
| longText | string | Yes | Yes | Long text of the notification. |
| briefText | string | Yes | Yes | Brief text of the notification. |
| expandedTitle | string | Yes | Yes | Title of the notification in the expanded state. |

#### NotificationMultiLineContent

Describes the multi-line text notification.

**System capability**: SystemCapability.Notification.Notification

| Name | Type | Readable | Writable | Description |
| :-- | :-- | :-- | :-- | :-- |
| title | string | Yes | Yes | Notification title. |
| text | string | Yes | Yes | Notification content. |
| additionalText | string | Yes | Yes | Additional information of the notification. |
| briefText | string | Yes | Yes | Brief text of the notification. |
| longTitle | string | Yes | Yes | Title of the notification in the expanded state. |
| lines | Array<string> | Yes | Yes | Multi-line text of the notification. |

#### NotificationPictureContent

Describes the picture-attached notification.

**System capability**: SystemCapability.Notification.Notification

| Name | Type | Readable | Writable | Description |
| :-- | :-- | :-- | :-- | :-- |
| title | string | Yes | Yes | Notification title. |
| text | string | Yes | Yes | Notification content. |
| additionalText | string | Yes | Yes | Additional information of the notification. |
| briefText | string | Yes | Yes | Brief text of the notification. |
| expandedTitle | string | Yes | Yes | Title of the notification in the expanded state. |
| picture | [image.PixelMap](../../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md) | Yes | Yes | Picture attached to the notification. |

#### NotificationContent

Describes the notification content.

**System capability**: SystemCapability.Notification.Notification

| Name | Type | Readable | Writable | Description |
| :-- | :-- | :-- | :-- | :-- |
| contentType | [notification.ContentType](#contenttype) | Yes | Yes | Notification content type. |
| normal | [NotificationBasicContent](#notificationbasiccontent) | Yes | Yes | Normal text. |
| longText | [NotificationLongTextContent](#notificationlongtextcontent) | Yes | Yes | Long text. |
| multiLine | [NotificationMultiLineContent](#notificationmultilinecontent) | Yes | Yes | Multi-line text. |
| picture | [NotificationPictureContent](#notificationpicturecontent) | Yes | Yes | Picture-attached. |

#### NotificationRequest

Describes the notification request.

**System capability**: SystemCapability.Notification.Notification

| Name | Type | Readable | Writable | Description |
| :-- | :-- | :-- | :-- | :-- |
| content | [NotificationContent](#notificationcontent) | Yes | Yes | Notification content. |
| id | number | Yes | Yes | Notification ID. |
| slotType | [notification.SlotType](#slottype) | Yes | Yes | Slot type. |
| isOngoing | boolean | Yes | Yes | Whether the notification is an ongoing notification. |
| isUnremovable | boolean | Yes | Yes | Whether the notification can be removed. |
| deliveryTime | number | Yes | Yes | Time when the notification is sent. |
| tapDismissed | boolean | Yes | Yes | Whether the notification is automatically cleared. |
| autoDeletedTime | number | Yes | Yes | Time when the notification is automatically cleared. |
| wantAgent | [WantAgent](../../../../../application-framework/ability-kit/arkts-apis/apis-no-longer-maintained/ohos-wantagent-wantagent-module/document.md) | Yes | Yes | **WantAgent** instance to which the notification will be redirected after being clicked. |
| extraInfo | {\[key: string\]: any} | Yes | Yes | Extended parameters. |
| color | number | Yes | Yes | Background color of the notification. Not supported currently. |
| colorEnabled | boolean | Yes | Yes | Whether the notification background color is enabled. Not supported currently. |
| isAlertOnce | boolean | Yes | Yes | Whether the notification triggers an alert only once. |
| isStopwatch | boolean | Yes | Yes | Whether to display the stopwatch. |
| isCountDown | boolean | Yes | Yes | Whether to display the countdown time. |
| isFloatingIcon | boolean | Yes | Yes | Whether the notification is displayed as a floating icon in the status bar. |
| label | string | Yes | Yes | Notification label. |
| badgeIconStyle | number | Yes | Yes | Notification badge type. |
| showDeliveryTime | boolean | Yes | Yes | Whether to display the time when the notification is delivered. |
| actionButtons | Array<[NotificationActionButton](#notificationactionbutton)\> | Yes | Yes | Buttons in the notification. Up to two buttons are allowed. |
| smallIcon | [image.PixelMap](../../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md) | Yes | Yes | Small notification icon. This field is optional, and the icon size cannot exceed 30 KB. |
| largeIcon | [image.PixelMap](../../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md) | Yes | Yes | Large notification icon. This field is optional, and the icon size cannot exceed 30 KB. |
| creatorBundleName | string | Yes | No | Name of the bundle that creates the notification. |
| creatorUid | number | Yes | No | UID used for creating the notification. |
| creatorPid | number | Yes | No | PID used for creating the notification. |
| creatorUserId8+ | number | Yes | No | ID of the user who creates the notification. |
| hashCode | string | Yes | No | Unique ID of the notification. |
| groupName8+ | string | Yes | Yes | Notification group name. |
| template8+ | [NotificationTemplate](#notificationtemplate8) | Yes | Yes | Notification template. |
| distributedOption8+ | [DistributedOptions](#distributedoptions8) | Yes | Yes | Distributed notification options. |
| notificationFlags8+ | [NotificationFlags](../../notification/notificationflags/document.md) | Yes | No | Notification flags. |
| removalWantAgent9+ | [WantAgent](../../../../../application-framework/ability-kit/arkts-apis/apis-no-longer-maintained/ohos-wantagent-wantagent-module/document.md) | Yes | Yes | **WantAgent** instance to which the notification will be redirected when it is removed. |
| badgeNumber9+ | number | Yes | Yes | Number of notifications displayed on the application icon. |

#### DistributedOptions8+

Describes distributed notifications options.

**System capability**: SystemCapability.Notification.Notification

| Name | Type | Readable | Writable | Description |
| :-- | :-- | :-- | :-- | :-- |
| isDistributed | boolean | Yes | Yes | Whether the notification is a distributed notification. |
| supportDisplayDevices | Array<string> | Yes | Yes | List of the devices to which the notification can be synchronized. |
| supportOperateDevices | Array<string> | Yes | Yes | List of the devices on which the notification can be opened. |

#### NotificationSlot

Describes the notification slot.

**System capability**: SystemCapability.Notification.Notification

| Name | Type | Readable | Writable | Description |
| :-- | :-- | :-- | :-- | :-- |
| type | [notification.SlotType](#slottype) | Yes | Yes | Slot type. |
| level | [notification.SlotLevel](#slotlevel) | Yes | Yes | Notification level. If this parameter is not set, the default value is used based on the notification slot type. |
| desc | string | Yes | Yes | Notification slot description. |
| badgeFlag | boolean | Yes | Yes | Whether to display the badge. |
| bypassDnd | boolean | Yes | Yes | Whether to bypass DND mode in the system. |
| lockscreenVisibility | number | Yes | Yes | Mode for displaying the notification on the lock screen. |
| vibrationEnabled | boolean | Yes | Yes | Whether vibration is enabled for the notification. |
| sound | string | Yes | Yes | Notification alert tone. |
| lightEnabled | boolean | Yes | Yes | Whether the indicator blinks for the notification. |
| lightColor | number | Yes | Yes | Indicator color of the notification. |
| vibrationValues | Array<number> | Yes | Yes | Vibration mode of the notification. |
| enabled9+ | boolean | Yes | No | Whether the notification slot is enabled. |

#### NotificationTemplate8+

Describes the notification template.

**System capability**: SystemCapability.Notification.Notification

| Name | Type | Readable | Writable | Description |
| :-- | :-- | :-- | :-- | :-- |
| name | string | Yes | Yes | Template name. |
| data | Record<string, Object> | Yes | Yes | Template data. |

#### NotificationUserInput8+

Provides the notification user input.

**System capability**: SystemCapability.Notification.Notification

| Name | Type | Readable | Writable | Description |
| :-- | :-- | :-- | :-- | :-- |
| inputKey | string | Yes | Yes | Key to identify the user input. |
