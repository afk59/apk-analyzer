# @ohos.reminderAgentManager (Agent-powered Reminder)

The **reminderAgentManager** module provides APIs related to agent-powered reminders. When your application is frozen or exits, the application's scheduled notification capability will be taken over by a system service running in the background. You can use the APIs to create scheduled reminders for countdown timers, calendar events, and alarm clocks. For details, see [Agent-powered Reminder](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/agent-powered-reminder).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/UCD29dcJQa-BC_aSvStIXA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062318Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D5944E53AABBBBC07F28FBEA0D95DB845259E6EE6B87C5F57339437A3CEAB288)

The initial APIs of this module are supported since API version 9. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { reminderAgentManager } from '@kit.BackgroundTasksKit';

#### reminderAgentManager.publishReminder

publishReminder(reminderReq: ReminderRequest, callback: AsyncCallback<number>): void

Publishes a reminder. This API uses an asynchronous callback to return the result.

Once an agent-powered reminder is published, the notification center will display the reminder when the scheduled time arrives. If the value of [ReminderRequest.ringDuration](#reminderrequest) is greater than 0, a custom ringtone will be played on the alarm channel by default. If the value is less than or equal to 0, no ringtone will be played.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/0LhJwakpQzWMcFpOetIzlg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062318Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=510C9809F47F319312B512ABB2B8727143655316569FDCF68D947A31B513F7E9)

This API can be called only after the [notificationManager.requestEnableNotification](../../../../application-services/notification-kit/arkts-apis/ohos-notificationmanager-notificationmanager/document.md#notificationmanagerrequestenablenotification10) permission is obtained.

To prevent agent-powered reminders from being abused for advertising and marketing purposes, a control mechanism is added. For details about how to use agent-powered reminders after the control, see [Development Guide](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/agent-powered-reminder#constraints).

**Required permissions**: ohos.permission.PUBLISH\_AGENT\_REMINDER

**System capability**: SystemCapability.Notification.ReminderAgent

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| reminderReq | [ReminderRequest](#reminderrequest) | Yes | Request used for publishing the reminder. |
| callback | AsyncCallback<number> | Yes | Callback used to return the published reminder's ID. |

**Error codes**

For details about the error codes, see [reminderAgentManager Error Codes](../../error-codes/reminderagentmanager-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter is not valid parameter. |
| 1700001 | Notification is not enabled. |
| 1700002 | The number of reminders exceeds the limit. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { reminderAgentManager } from '@kit.BackgroundTasksKit';

let timer: reminderAgentManager.ReminderRequestTimer = {
  reminderType: reminderAgentManager.ReminderType.REMINDER\_TYPE\_TIMER,
  triggerTimeInSeconds: 10
}

reminderAgentManager.publishReminder(timer, (err: BusinessError, reminderId: number) => {
  if (err.code) {
    console.error("callback err code:" + err.code + " message:" + err.message);
  } else {
    console.info("callback, reminderId = " + reminderId);
  }
});

#### reminderAgentManager.publishReminder

publishReminder(reminderReq: ReminderRequest): Promise<number>

Publishes a reminder. This API uses a promise to return the result.

If the value of [ReminderRequest.ringDuration](#reminderrequest) is greater than 0, the custom ringtone is played on the alarm channel by default. If the value is less than or equal to 0, no ringtone is played.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/JRRYAKgtRLyMXCZsrVwgOg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062318Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=199CAFDA5523A2900066E3CBC3BEA3CF446A91D87CD94499AA9873778E02DDB4)

This API can be called only after the [notificationManager.requestEnableNotification](../../../../application-services/notification-kit/arkts-apis/ohos-notificationmanager-notificationmanager/document.md#notificationmanagerrequestenablenotification10) permission is obtained.

To prevent agent-powered reminders from being abused for advertising and marketing purposes, a control mechanism is added. For details about how to use agent-powered reminders after the control, see [Development Guide](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/agent-powered-reminder#constraints).

**Required permissions**: ohos.permission.PUBLISH\_AGENT\_REMINDER

**System capability**: SystemCapability.Notification.ReminderAgent

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| reminderReq | [ReminderRequest](#reminderrequest) | Yes | Request used for publishing the reminder. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the published reminder ID. |

**Error codes**

For details about the error codes, see [reminderAgentManager Error Codes](../../error-codes/reminderagentmanager-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter is not valid parameter. |
| 1700001 | Notification is not enabled. |
| 1700002 | The number of reminders exceeds the limit. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { reminderAgentManager } from '@kit.BackgroundTasksKit';

let timer: reminderAgentManager.ReminderRequestTimer = {
  reminderType: reminderAgentManager.ReminderType.REMINDER\_TYPE\_TIMER,
  triggerTimeInSeconds: 10
}

reminderAgentManager.publishReminder(timer).then((reminderId: number) => {
  console.info("promise, reminderId = " + reminderId);
}).catch((err: BusinessError) => {
  console.error("promise err code:" + err.code + " message:" + err.message);
});

#### reminderAgentManager.cancelReminder

cancelReminder(reminderId: number, callback: AsyncCallback<void>): void

Cancels a reminder published. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Notification.ReminderAgent

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| reminderId | number | Yes | ID of the agent-powered reminder to be canceled. The reminder ID is returned when the [publishReminder](#reminderagentmanagerpublishreminder) API is called. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If all the reminders are canceled, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [reminderAgentManager Error Codes](../../error-codes/reminderagentmanager-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter is not valid parameter. |
| 1700003 | The reminder does not exist. |
| 1700004 | The bundle name does not exist. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { reminderAgentManager } from '@kit.BackgroundTasksKit';

let reminderId: number = 1;
reminderAgentManager.cancelReminder(reminderId, (err: BusinessError) => {
  if (err.code) {
    console.error("callback err code:" + err.code + " message:" + err.message);
  } else {
    console.info("cancelReminder callback");
  }
});

#### reminderAgentManager.cancelReminder

cancelReminder(reminderId: number): Promise<void>

Cancels a reminder published. This API uses a promise to return the result.

**System capability**: SystemCapability.Notification.ReminderAgent

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| reminderId | number | Yes | ID of the agent-powered reminder to be canceled. The reminder ID is returned when the [publishReminder](#reminderagentmanagerpublishreminder) API is called. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [reminderAgentManager Error Codes](../../error-codes/reminderagentmanager-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter is not valid parameter. |
| 1700003 | The reminder does not exist. |
| 1700004 | The bundle name does not exist. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { reminderAgentManager } from '@kit.BackgroundTasksKit';

let reminderId: number = 1;
reminderAgentManager.cancelReminder(reminderId).then(() => {
  console.info("cancelReminder promise");
}).catch((err: BusinessError) => {
  console.error("promise err code:" + err.code + " message:" + err.message);
});

#### reminderAgentManager.getValidReminders

getValidReminders(callback: AsyncCallback<Array<ReminderRequest>>): void

Obtains all [valid (not yet expired) reminders](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/agent-powered-reminder#constraints) set by the current application. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Notification.ReminderAgent

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<Array<[ReminderRequest](#reminderrequest)\>> | Yes | Callback used to return all the valid reminders. |

**Error codes**

For details about the error codes, see [reminderAgentManager Error Codes](../../error-codes/reminderagentmanager-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter is not valid parameter. |
| 1700004 | The bundle name does not exist. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { reminderAgentManager } from '@kit.BackgroundTasksKit';

reminderAgentManager.getValidReminders((err: BusinessError, reminders: Array<reminderAgentManager.ReminderRequest>) => {
  if (err.code) {
    console.error("callback err code:" + err.code + " message:" + err.message);
  } else {
    console.info("callback, getValidReminders length = " + reminders.length);
    for (let i = 0; i < reminders.length; i++) {
      console.info("getValidReminders = " + reminders\[i\]);
      console.info("getValidReminders, reminderType = " + reminders\[i\].reminderType);
      const actionButton = reminders\[i\].actionButton || \[\];
      for (let j = 0; j < actionButton.length; j++) {
        console.info("getValidReminders, actionButton.title = " + actionButton\[j\]?.title);
        console.info("getValidReminders, actionButton.type = " + actionButton\[j\]?.type);
      }
      console.info("getValidReminders, wantAgent.pkgName = " + reminders\[i\].wantAgent?.pkgName);
      console.info("getValidReminders, wantAgent.abilityName = " + reminders\[i\].wantAgent?.abilityName);
      console.info("getValidReminders, ringDuration = " + reminders\[i\].ringDuration);
      console.info("getValidReminders, snoozeTimes = " + reminders\[i\].snoozeTimes);
      console.info("getValidReminders, timeInterval = " + reminders\[i\].timeInterval);
      console.info("getValidReminders, title = " + reminders\[i\].title);
      console.info("getValidReminders, content = " + reminders\[i\].content);
      console.info("getValidReminders, expiredContent = " + reminders\[i\].expiredContent);
      console.info("getValidReminders, snoozeContent = " + reminders\[i\].snoozeContent);
      console.info("getValidReminders, notificationId = " + reminders\[i\].notificationId);
      console.info("getValidReminders, slotType = " + reminders\[i\].slotType);
    }
  }
});

#### reminderAgentManager.getValidReminders

getValidReminders(): Promise<Array<ReminderRequest>>

Obtains all [valid (not yet expired) reminders](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/agent-powered-reminder#constraints) set by the current application. This API uses a promise to return the result.

**System capability**: SystemCapability.Notification.ReminderAgent

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<[ReminderRequest](#reminderrequest)\>> | Promise used to return all the valid reminders. |

**Error codes**

For details about the error codes, see [reminderAgentManager Error Codes](../../error-codes/reminderagentmanager-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter is not valid parameter. |
| 1700004 | The bundle name does not exist. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { reminderAgentManager } from '@kit.BackgroundTasksKit';

reminderAgentManager.getValidReminders().then((reminders: Array<reminderAgentManager.ReminderRequest>) => {
  console.info("promise, getValidReminders length = " + reminders.length);
  for (let i = 0; i < reminders.length; i++) {
    console.info("getValidReminders = " + reminders\[i\]);
    console.info("getValidReminders, reminderType = " + reminders\[i\].reminderType);
    const actionButton = reminders\[i\].actionButton || \[\];
    for (let j = 0; j < actionButton.length; j++) {
      console.info("getValidReminders, actionButton.title = " + actionButton\[j\]?.title);
      console.info("getValidReminders, actionButton.type = " + actionButton\[j\]?.type);
    }
    console.info("getValidReminders, wantAgent.pkgName = " + reminders\[i\].wantAgent?.pkgName);
    console.info("getValidReminders, wantAgent.abilityName = " + reminders\[i\].wantAgent?.abilityName);
    console.info("getValidReminders, ringDuration = " + reminders\[i\].ringDuration);
    console.info("getValidReminders, snoozeTimes = " + reminders\[i\].snoozeTimes);
    console.info("getValidReminders, timeInterval = " + reminders\[i\].timeInterval);
    console.info("getValidReminders, title = " + reminders\[i\].title);
    console.info("getValidReminders, content = " + reminders\[i\].content);
    console.info("getValidReminders, expiredContent = " + reminders\[i\].expiredContent);
    console.info("getValidReminders, snoozeContent = " + reminders\[i\].snoozeContent);
    console.info("getValidReminders, notificationId = " + reminders\[i\].notificationId);
    console.info("getValidReminders, slotType = " + reminders\[i\].slotType);
  }
}).catch((err: BusinessError) => {
  console.error("promise err code:" + err.code + " message:" + err.message);
});

#### reminderAgentManager.cancelAllReminders

cancelAllReminders(callback: AsyncCallback<void>): void

Cancels all reminders set by the current application. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Notification.ReminderAgent

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If all the reminders are canceled, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [reminderAgentManager Error Codes](../../error-codes/reminderagentmanager-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter is not valid parameter. |
| 1700004 | The bundle name does not exist. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { reminderAgentManager } from '@kit.BackgroundTasksKit';

reminderAgentManager.cancelAllReminders((err: BusinessError) =>{
  if (err.code) {
    console.error("callback err code:" + err.code + " message:" + err.message);
  } else {
    console.info("cancelAllReminders callback")
  }
});

#### reminderAgentManager.cancelAllReminders

cancelAllReminders(): Promise<void>

Cancels all reminders set by the current application. This API uses a promise to return the result.

**System capability**: SystemCapability.Notification.ReminderAgent

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [reminderAgentManager Error Codes](../../error-codes/reminderagentmanager-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter is not valid parameter. |
| 1700004 | The bundle name does not exist. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { reminderAgentManager } from '@kit.BackgroundTasksKit';

reminderAgentManager.cancelAllReminders().then(() => {
  console.info("cancelAllReminders promise")
}).catch((err: BusinessError) => {
  console.error("promise err code:" + err.code + " message:" + err.message);
});

#### reminderAgentManager.addNotificationSlot

addNotificationSlot(slot: NotificationSlot, callback: AsyncCallback<void>): void

Adds a notification slot. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Notification.ReminderAgent

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| slot | [NotificationSlot](../../../../application-services/notification-kit/arkts-apis/notification/notificationslot/document.md#notificationslot-1) | Yes | Notification slot instance. Only the **notificationType** property can be set. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the notification slot is added, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter is not valid parameter. |

**Example**

import { notificationManager } from '@kit.NotificationKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { reminderAgentManager } from '@kit.BackgroundTasksKit';

let mySlot: notificationManager.NotificationSlot = {
  notificationType: notificationManager.SlotType.SOCIAL\_COMMUNICATION
}

reminderAgentManager.addNotificationSlot(mySlot, (err: BusinessError) => {
  if (err.code) {
    console.error("callback err code:" + err.code + " message:" + err.message);
  } else {
    console.info("addNotificationSlot callback");
  }
});

#### reminderAgentManager.addNotificationSlot

addNotificationSlot(slot: NotificationSlot): Promise<void>

Adds a notification slot. This API uses a promise to return the result.

**System capability**: SystemCapability.Notification.ReminderAgent

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| slot | [NotificationSlot](../../../../application-services/notification-kit/arkts-apis/notification/notificationslot/document.md#notificationslot-1) | Yes | Notification slot instance. Only the **notificationType** property can be set. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter is not valid parameter. |

**Example**

import { notificationManager } from '@kit.NotificationKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { reminderAgentManager } from '@kit.BackgroundTasksKit';

let mySlot: notificationManager.NotificationSlot = {
  notificationType: notificationManager.SlotType.SOCIAL\_COMMUNICATION
}
reminderAgentManager.addNotificationSlot(mySlot).then(() => {
  console.info("addNotificationSlot promise");
}).catch((err: BusinessError) => {
  console.error("promise err code:" + err.code + " message:" + err.message);
});

#### reminderAgentManager.removeNotificationSlot

removeNotificationSlot(slotType: notification.SlotType, callback: AsyncCallback<void>): void

Removes a specified notification slot. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Notification.ReminderAgent

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| slotType | [notification.SlotType](../../../../application-services/notification-kit/arkts-apis/apis-no-longer-maintained/ohos-notification-notification/document.md#slottype) | Yes | Type of the notification slot. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the notification slot is removed, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter is not valid parameter. |

**Example**

import { notificationManager } from '@kit.NotificationKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { reminderAgentManager } from '@kit.BackgroundTasksKit';

reminderAgentManager.removeNotificationSlot(notificationManager.SlotType.CONTENT\_INFORMATION,
  (err: BusinessError) => {
  if (err.code) {
    console.error("callback err code:" + err.code + " message:" + err.message);
  } else {
    console.info("removeNotificationSlot callback");
  }
});

#### reminderAgentManager.removeNotificationSlot

removeNotificationSlot(slotType: notification.SlotType): Promise<void>

Removes a specified notification slot. This API uses a promise to return the result.

**System capability**: SystemCapability.Notification.ReminderAgent

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| slotType | [notification.SlotType](../../../../application-services/notification-kit/arkts-apis/apis-no-longer-maintained/ohos-notification-notification/document.md#slottype) | Yes | Type of the notification slot. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter is not valid parameter. |

**Example**

import { notificationManager } from '@kit.NotificationKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { reminderAgentManager } from '@kit.BackgroundTasksKit';

reminderAgentManager.removeNotificationSlot(notificationManager.SlotType.CONTENT\_INFORMATION).then(() => {
  console.info("removeNotificationSlot promise");
}).catch((err: BusinessError) => {
  console.error("promise err code:" + err.code + " message:" + err.message);
});

#### reminderAgentManager.getAllValidReminders12+

getAllValidReminders(): Promise<Array<ReminderInfo>>

Obtains all [valid (not yet expired) reminders](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/agent-powered-reminder#constraints) set by the current application. This API uses a promise to return the result. To call this API, you need to request the ohos.permission.PUBLISH\_AGENT\_REMINDER permission.

**System capability**: SystemCapability.Notification.ReminderAgent

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<[ReminderInfo](#reminderinfo12)\>> | Promise used to return all the valid reminders. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { reminderAgentManager } from '@kit.BackgroundTasksKit';

reminderAgentManager.getAllValidReminders().then((reminders: Array<reminderAgentManager.ReminderInfo>) => {
  console.info("promise, getAllValidReminders length = " + reminders.length);
  for (let i = 0; i < reminders.length; i++) {
    console.info("getAllValidReminders, reminderId = " + reminders\[i\].reminderId);
    console.info("getAllValidReminders, reminderType = " + reminders\[i\].reminderReq.reminderType);
    const actionButton = reminders\[i\].reminderReq.actionButton || \[\];
    for (let j = 0; j < actionButton.length; j++) {
      console.info("getAllValidReminders, actionButton.title = " + actionButton\[j\]?.title);
      console.info("getAllValidReminders, actionButton.type = " + actionButton\[j\]?.type);
    }
    console.info("getAllValidReminders, wantAgent.pkgName = " + reminders\[i\].reminderReq.wantAgent?.pkgName);
    console.info("getAllValidReminders, wantAgent.abilityName = " + reminders\[i\].reminderReq.wantAgent?.abilityName);
    console.info("getAllValidReminders, ringDuration = " + reminders\[i\].reminderReq.ringDuration);
    console.info("getAllValidReminders, snoozeTimes = " + reminders\[i\].reminderReq.snoozeTimes);
    console.info("getAllValidReminders, timeInterval = " + reminders\[i\].reminderReq.timeInterval);
    console.info("getAllValidReminders, title = " + reminders\[i\].reminderReq.title);
    console.info("getAllValidReminders, content = " + reminders\[i\].reminderReq.content);
    console.info("getAllValidReminders, expiredContent = " + reminders\[i\].reminderReq.expiredContent);
    console.info("getAllValidReminders, snoozeContent = " + reminders\[i\].reminderReq.snoozeContent);
    console.info("getAllValidReminders, notificationId = " + reminders\[i\].reminderReq.notificationId);
    console.info("getAllValidReminders, slotType = " + reminders\[i\].reminderReq.slotType);
  }
}).catch((err: BusinessError) => {
  console.error("promise err code:" + err.code + " message:" + err.message);
});

#### reminderAgentManager.addExcludeDate12+

addExcludeDate(reminderId: number, date: Date): Promise<void>

Adds a non-reminder date for a recurring calendar reminder with a specific ID. For example, configure a daily reminder to skip notifications on Tuesdays. This API uses a promise to return the result.

**System capability**: SystemCapability.Notification.ReminderAgent

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| reminderId | number | Yes | ID of the agent-powered reminder to be added. The reminder ID is returned when the [publishReminder](#reminderagentmanagerpublishreminder) API is called. |
| date | Date | Yes | Non-reminder date. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [reminderAgentManager Error Codes](../../error-codes/reminderagentmanager-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | If the input parameter is not valid parameter. |
| 1700003 | The reminder does not exist. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { reminderAgentManager } from '@kit.BackgroundTasksKit';

let reminderId: number = 1;
let date = new Date();
reminderAgentManager.addExcludeDate(reminderId, date).then(() => {
  console.info("addExcludeDate promise");
}).catch((err: BusinessError) => {
  console.error("promise err code:" + err.code + " message:" + err.message);
});

#### reminderAgentManager.deleteExcludeDates12+

deleteExcludeDates(reminderId: number): Promise<void>

Deletes all non-reminder dates for a recurring calendar reminder with a specific ID. This API uses a promise to return the result.

**System capability**: SystemCapability.Notification.ReminderAgent

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| reminderId | number | Yes | ID of the agent-powered reminder to be removed. The reminder ID is returned when the [publishReminder](#reminderagentmanagerpublishreminder) API is called. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [reminderAgentManager Error Codes](../../error-codes/reminderagentmanager-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 1700003 | The reminder does not exist. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { reminderAgentManager } from '@kit.BackgroundTasksKit';

let reminderId: number = 1;
reminderAgentManager.deleteExcludeDates(reminderId).then(() => {
  console.info("deleteExcludeDates promise");
}).catch((err: BusinessError) => {
  console.error("promise err code:" + err.code + " message:" + err.message);
});

#### reminderAgentManager.getExcludeDates12+

getExcludeDates(reminderId: number): Promise<Array<Date>>

Obtains all non-reminder dates for a recurring calendar reminder with a specific ID. This API uses a promise to return the result.

**System capability**: SystemCapability.Notification.ReminderAgent

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| reminderId | number | Yes | ID of the agent-powered reminder to be queried. The reminder ID is returned when the [publishReminder](#reminderagentmanagerpublishreminder) API is called. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<Date>> | Promise used to return all the non-reminder dates. |

**Error codes**

For details about the error codes, see [reminderAgentManager Error Codes](../../error-codes/reminderagentmanager-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 1700003 | The reminder does not exist. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { reminderAgentManager } from '@kit.BackgroundTasksKit';

let reminderId: number = 1;
reminderAgentManager.getExcludeDates(reminderId).then((dates) => {
  console.info("getExcludeDates promise length: " + dates.length);
  for (let i = 0; i < dates.length; i++) {
    console.info("getExcludeDates promise date is: " + dates\[i\].toString());
  }
}).catch((err: BusinessError) => {
  console.error("promise err code:" + err.code + " message:" + err.message);
});

#### reminderAgentManager.updateReminder20+

updateReminder(reminderId: number, reminderReq: ReminderRequest): Promise<void>

Updates the agent-powered reminder with the specified ID. This API uses a promise to return the result. Only [valid (not yet expired) reminders](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/agent-powered-reminder#constraints) that are not displayed in the notification panel can be updated.

**Required permissions**: ohos.permission.PUBLISH\_AGENT\_REMINDER

**System capability**: SystemCapability.Notification.ReminderAgent

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| reminderId | number | Yes | ID of the agent-powered reminder to be updated. The reminder ID is returned when the [publishReminder](#reminderagentmanagerpublishreminder) API is called. |
| reminderReq | [ReminderRequest](#reminderrequest) | Yes | Request instance used to set detailed information such as the reminder type and ringing duration. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [reminderAgentManager Error Codes](../../error-codes/reminderagentmanager-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 1700003 | The reminder does not exist. |
| 1700007 | If the input parameter is not valid parameter. |

**Example**

import { reminderAgentManager } from '@kit.BackgroundTasksKit';
import { BusinessError } from '@kit.BasicServicesKit';

let timer: reminderAgentManager.ReminderRequestTimer = {
  reminderType: reminderAgentManager.ReminderType.REMINDER\_TYPE\_TIMER,
  triggerTimeInSeconds: 10
}

let reminderId: number = 1;
reminderAgentManager.updateReminder(reminderId, timer).then(() => {
  console.info("update reminder succeed");
}).catch((err: BusinessError) => {
  console.error("promise err code:" + err.code + " message:" + err.message);
});

#### ActionButtonType

Enumerates the types of buttons displayed for a reminder.

**System capability**: SystemCapability.Notification.ReminderAgent

| Name | Value | Description |
| :-- | :-- | :-- |
| ACTION\_BUTTON\_TYPE\_CLOSE | 0 | Button for closing the reminder. |
| ACTION\_BUTTON\_TYPE\_SNOOZE | 1 | Button for snoozing the reminder, with the frequency and timing configured via **snoozeTimes** and **timeInterval** in the [ReminderRequest](#reminderrequest) struct. |

#### ReminderType

Enumerates the reminder types.

**System capability**: SystemCapability.Notification.ReminderAgent

| Name | Value | Description |
| :-- | :-- | :-- |
| REMINDER\_TYPE\_TIMER | 0 | Countdown reminder. |
| REMINDER\_TYPE\_CALENDAR | 1 | Calendar reminder. |
| REMINDER\_TYPE\_ALARM | 2 | Alarm reminder. |

#### RingChannel20+

Enumerates the audio playback channels for the custom prompt tone.

**System capability**: SystemCapability.Notification.ReminderAgent

| Name | Value | Description |
| :-- | :-- | :-- |
| RING\_CHANNEL\_ALARM | 0 | Alarm channel. |
| RING\_CHANNEL\_MEDIA | 1 | Media channel. |

#### ActionButton

Describes the button displayed for a reminder.

**System capability**: SystemCapability.Notification.ReminderAgent

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| title | string | No | No | Text on the button. |
| titleResource11+ | string | No | Yes | Resource ID of the title. This parameter is used to read the title information after the system language is switched. |
| type | [ActionButtonType](#actionbuttontype) | No | No | Button type. |

#### WantAgent

Defines the information about the redirected-to ability.

**System capability**: SystemCapability.Notification.ReminderAgent

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| pkgName | string | No | No | Name of the target package. |
| abilityName | string | No | No | Name of the target ability. |
| parameters12+ | Record<string, Object> | No | Yes | Parameters to be transferred to the target. |
| uri12+ | string | No | Yes | URI of the target ability. |

#### MaxScreenWantAgent

Describes the information about the ability that is started automatically and displayed in full-screen mode when a reminder is displayed in the notification center. This API is reserved.

**System capability**: SystemCapability.Notification.ReminderAgent

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| pkgName | string | No | No | Name of the target package. (If the device is in use, only a notification banner is displayed.) |
| abilityName | string | No | No | Name of the target ability. (If the device is in use, only a notification banner is displayed.) |

#### ReminderRequest

Defines the request for publishing a reminder.

**System capability**: SystemCapability.Notification.ReminderAgent

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| reminderType | [ReminderType](#remindertype) | No | No | Type of the reminder. |
| actionButton | [\[ActionButton?, ActionButton?, ActionButton?\]](#actionbutton) | No | Yes | 
Buttons displayed for the reminder notification.

For third-party applications, a maximum of two buttons are supported.

For system applications, a maximum of three buttons are supported in API version 10 and later versions, and a maximum of two buttons are supported in versions earlier than API version 10.

 |
| wantAgent | [WantAgent](#wantagent) | No | Yes | Information about the ability that is redirected to when the reminder is clicked. |
| maxScreenWantAgent | [MaxScreenWantAgent](#maxscreenwantagent) | No | Yes | 

Information about the ability that is started automatically and displayed in full-screen mode when the reminder arrives. If the device is in use, only a notification banner is displayed.

This API is reserved.

 |
| ringDuration | number | No | Yes | Ringing duration, in seconds. The default value is 1 second, and the maximum value is 30 minutes. |
| snoozeTimes | number | No | Yes | Number of reminder snooze times. The default value is **0**. (It is not applicable to countdown reminders.) |
| timeInterval | number | No | Yes | Reminder snooze interval, in seconds. The minimum value is 30 seconds. (It is not applicable to countdown reminders.) |
| title | string | No | Yes | Reminder title. |
| titleResourceId18+ | number | No | Yes | Resource ID of the reminder title. |
| content | string | No | Yes | Reminder content. |
| contentResourceId18+ | number | No | Yes | Resource ID of the reminder content. |
| expiredContent | string | No | Yes | Content to be displayed after the reminder expires. |
| expiredContentResourceId18+ | number | No | Yes | Resource ID of the content to be displayed after the reminder expires. |
| snoozeContent | string | No | Yes | Content to be displayed when the reminder is snoozing. (It is not applicable to countdown reminders.) |
| snoozeContentResourceId18+ | number | No | Yes | Resource ID of the content to be displayed when the reminder is snoozing. |
| notificationId | number | No | Yes | Notification ID used by the reminder. You must pass in a notification ID. If there are reminders with the same notification ID, the later one will overwrite the earlier one. |
| groupId11+ | string | No | Yes | Group ID used for the reminder. If "Don't ask again" or similar information is selected for the reminder, other reminders with the same group ID are also canceled. |
| slotType | [notification.SlotType](../../../../application-services/notification-kit/arkts-apis/ohos-notificationmanager-notificationmanager/document.md#slottype) | No | Yes | Type of the slot used by the reminder. |
| tapDismissed10+ | boolean | No | Yes | 

Whether the reminder is automatically cleared. For details, see [NotificationRequest.tapDismissed](../../../../application-services/notification-kit/arkts-apis/notification/notificationrequest/document.md#notificationrequest-1).

\- **true** (default): The reminder is automatically cleared after the notification or button is tapped.

\- **false**: The reminder is retained after the notification or button is tapped.

 |
| autoDeletedTime10+ | number | No | Yes | Time when the reminder is automatically cleared. For details, see [NotificationRequest.autoDeletedTime](../../../../application-services/notification-kit/arkts-apis/notification/notificationrequest/document.md#notificationrequest-1). |
| snoozeSlotType11+ | [notification.SlotType](../../../../application-services/notification-kit/arkts-apis/ohos-notificationmanager-notificationmanager/document.md#slottype) | No | Yes | Type of the slot used by the snoozed reminder. (It is not applicable to countdown reminders.) |
| customRingUri11+ | string | No | Yes | URI of the custom prompt tone. The prompt tone file must be stored in the **resources/rawfile** directory and supports formats such as M4A, AAC, MP3, OGG, WAV, FLAC, and AMR. |
| ringChannel20+ | [RingChannel](#ringchannel20) | No | Yes | Audio channel of the custom prompt tone. The default channel is the alarm channel. |

#### ReminderRequestCalendar

ReminderRequestCalendar extends ReminderRequest

Defines a reminder for a calendar event.

**System capability**: SystemCapability.Notification.ReminderAgent

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| dateTime | [LocalDateTime](#localdatetime) | No | No | Reminder time. |
| repeatMonths | Array<number> | No | Yes | Month in which the reminder repeats. The value range is \[1, 12\]. This parameter must be used together with **repeatDays**. |
| repeatDays | Array<number> | No | Yes | Day in which the reminder repeats. The value range is \[1, 31\]. This parameter must be used together with **repeatMonths**. |
| daysOfWeek11+ | Array<number> | No | Yes | Days of a week when the reminder repeats. The value ranges from 1 to 7, corresponding to the data from Monday to Sunday. |
| endDateTime12+ | [LocalDateTime](#localdatetime) | No | Yes | End time of the reminder. |

#### ReminderRequestAlarm

ReminderRequestAlarm extends ReminderRequest

Defines a reminder for an alarm.

**System capability**: SystemCapability.Notification.ReminderAgent

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| hour | number | No | No | Hour portion of the reminder time. The value range is \[0, 23\]. |
| minute | number | No | No | Minute portion of the reminder time. The value range is \[0, 59\]. |
| daysOfWeek | Array<number> | No | Yes | Days of a week when the reminder repeats. The value ranges from 1 to 7, corresponding to the data from Monday to Sunday. |

#### ReminderRequestTimer

ReminderRequestTimer extends ReminderRequest

Defines a reminder for a scheduled timer.

**System capability**: SystemCapability.Notification.ReminderAgent

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| triggerTimeInSeconds | number | No | No | Number of seconds in the countdown timer. |

#### LocalDateTime

Defines the time information for a calendar reminder.

**System capability**: SystemCapability.Notification.ReminderAgent

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| year | number | No | No | Year. |
| month | number | No | No | Month. The value ranges from 1 to 12. |
| day | number | No | No | Day. The value ranges from 1 to 31. |
| hour | number | No | No | Hour. The value ranges from 0 to 23. |
| minute | number | No | No | Minute. The value ranges from 0 to 59. |
| second | number | No | Yes | Second. The value ranges from 0 to 59. |

#### ReminderInfo12+

Defines the reminder information.

**System capability**: SystemCapability.Notification.ReminderAgent

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| reminderId | number | No | No | Reminder ID. |
| reminderReq | [ReminderRequest](#reminderrequest) | No | No | Request used for publishing the reminder. |
