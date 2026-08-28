# @ohos.reminderAgent (Agent-powered Reminder)

The **reminderAgent** module provides APIs for publishing scheduled reminders through the reminder agent.

You can use the APIs to create scheduled reminders for countdown timers, calendar events, and alarm clocks. When the created reminders are published, the timing and pop-up notification functions of your application will be taken over by the reminder agent in the background when your application is frozen or exits.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0c/v3/X4_OvNUpT3W-SCZmBj6LPg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062318Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=168602C3E02E49B7E33298A2B6A5E18E873C38918D5A23DAD5DB9E89A236292B)

This module is supported since API version 7 and deprecated since API version 9. You are advised to use [@ohos.reminderAgentManager (Agent-powered Reminder)](../../ohos-reminderagentmanager-agent-powered-reminder/document.md) instead.

The initial APIs of this module are supported since API version 7. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import reminderAgent from'@ohos.reminderAgent';

#### reminderAgent.publishReminder(deprecated)

publishReminder(reminderReq: ReminderRequest, callback: AsyncCallback<number>): void

Publishes a reminder through the reminder agent. This API uses an asynchronous callback to return the result. It can be called only when notification is enabled for the application through [Notification.requestEnableNotification](../../../../../application-services/notification-kit/arkts-apis/apis-no-longer-maintained/ohos-notification-notification/document.md#notificationrequestenablenotification8).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/GkBJ7PcqSPyLWQMtQ7gYew/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062318Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F2599F1467D0865333DE474BA036F779667FB688ACE36171D206C0DBAA361C26)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [reminderAgentManager.publishReminder](../../ohos-reminderagentmanager-agent-powered-reminder/document.md#reminderagentmanagerpublishreminder).

**Required permissions**: ohos.permission.PUBLISH\_AGENT\_REMINDER

**System capability**: SystemCapability.Notification.ReminderAgent

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| reminderReq | [ReminderRequest](#reminderrequestdeprecated) | Yes | Reminder to be published. |
| callback | AsyncCallback<number> | Yes | Callback used to return the published reminder's ID. |

**Example**

import { BusinessError } from '@ohos.base';

let timer:reminderAgent.ReminderRequestTimer = {
  reminderType: reminderAgent.ReminderType.REMINDER\_TYPE\_TIMER,
  triggerTimeInSeconds: 10
}

reminderAgent.publishReminder(timer, (err: BusinessError, reminderId: number) => {
  console.info("callback, reminderId = " + reminderId);
});

#### reminderAgent.publishReminder(deprecated)

publishReminder(reminderReq: ReminderRequest): Promise<number>

Publishes a reminder through the reminder agent. This API uses a promise to return the result. It can be called only when notification is enabled for the application through [Notification.requestEnableNotification](../../../../../application-services/notification-kit/arkts-apis/apis-no-longer-maintained/ohos-notification-notification/document.md#notificationrequestenablenotification8).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/ndatNNgOQ0mUL4JleZhaSw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062318Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6B51F1407F4F0BB95143DE80A4275F2F031CE61BC15315CA0F9511E45C1F324D)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [reminderAgentManager.publishReminder](../../ohos-reminderagentmanager-agent-powered-reminder/document.md#reminderagentmanagerpublishreminder-1).

**Required permissions**: ohos.permission.PUBLISH\_AGENT\_REMINDER

**System capability**: SystemCapability.Notification.ReminderAgent

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| reminderReq | [ReminderRequest](#reminderrequestdeprecated) | Yes | Reminder to be published. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the published reminder's ID. |

**Example**

let timer:reminderAgent.ReminderRequestTimer = {
  reminderType: reminderAgent.ReminderType.REMINDER\_TYPE\_TIMER,
  triggerTimeInSeconds: 10
}

reminderAgent.publishReminder(timer).then((reminderId: number) => {
  console.info("promise, reminderId = " + reminderId);
});

#### reminderAgent.cancelReminder(deprecated)

cancelReminder(reminderId: number, callback: AsyncCallback<void>): void

Cancels the reminder with the specified ID. This API uses an asynchronous callback to return the cancellation result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/ns9IC3keTACuGq-535dIbg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062318Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9D67FE1EC761F7720D223E100CE8B03F5D138F54034E454CE74BB60CB09E752E)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [reminderAgentManager.cancelReminder](../../ohos-reminderagentmanager-agent-powered-reminder/document.md#reminderagentmanagercancelreminder).

**System capability**: SystemCapability.Notification.ReminderAgent

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| reminderId | number | Yes | ID of the reminder. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Example**

import { BusinessError } from '@ohos.base';

reminderAgent.cancelReminder(1, (err: BusinessError, data: void) => {
  console.info("cancelReminder callback");
});

#### reminderAgent.cancelReminder(deprecated)

cancelReminder(reminderId: number): Promise<void>

Cancels the reminder with the specified ID. This API uses a promise to return the cancellation result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/hcg7trPES6yTgIbl4XdG5w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062318Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FB322F1B0A1688EA030D3E240334BE1A8DFE6380BFE9183ECB2A27FC7DFE8DAC)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [reminderAgentManager.cancelReminder](../../ohos-reminderagentmanager-agent-powered-reminder/document.md#reminderagentmanagercancelreminder-1).

**System capability**: SystemCapability.Notification.ReminderAgent

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| reminderId | number | Yes | ID of the reminder. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise used to return the result. |

**Example**

reminderAgent.cancelReminder(1).then(() => {
    console.info("cancelReminder promise");
});

#### reminderAgent.getValidReminders(deprecated)

getValidReminders(callback: AsyncCallback<Array<ReminderRequest>>): void

Obtains all valid (not yet expired) reminders set by the current application. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e/v3/PP6ye7DvRDWLAr3XkyEOUg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062318Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=425C99C38B983431C1F75102511BBF2CEF11D665C93C4539087370C52361A359)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [reminderAgentManager.getValidReminders](../../ohos-reminderagentmanager-agent-powered-reminder/document.md#reminderagentmanagergetvalidreminders).

**System capability**: SystemCapability.Notification.ReminderAgent

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<Array<[ReminderRequest](#reminderrequestdeprecated)\>> | Yes | Callback used to return an array of all valid reminders set by the current application. |

**Example**

import { BusinessError } from '@ohos.base';

reminderAgent.getValidReminders((err: BusinessError, reminders: Array<reminderAgent.ReminderRequest>) => {
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
})

#### reminderAgent.getValidReminders(deprecated)

getValidReminders(): Promise<Array<ReminderRequest>>

Obtains all valid (not yet expired) reminders set by the current application. This API uses a promise to return the reminders.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/xlZncMzeQkm6kSWpRqhmMQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062318Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0CB016F286DED15CE3D40E2553D09A25942A370E201C23ADC1D76CF0C857A553)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [reminderAgentManager.getValidReminders](../../ohos-reminderagentmanager-agent-powered-reminder/document.md#reminderagentmanagergetvalidreminders-1).

**System capability**: SystemCapability.Notification.ReminderAgent

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<[ReminderRequest](#reminderrequestdeprecated)\>> | Promise used to return an array of all valid reminders set by the current application. |

**Example**

reminderAgent.getValidReminders().then((reminders: Array<reminderAgent.ReminderRequest>) => {
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
})

#### reminderAgent.cancelAllReminders(deprecated)

cancelAllReminders(callback: AsyncCallback<void>): void

Cancels all reminders set by the current application. This API uses an asynchronous callback to return the cancellation result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/N0yFEmc2QSyjUJur_VukMw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062318Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=043CE2001FE88EC9E958DD3303F0E238C1F989CAB1C81EC1AB3FE41BBEB9F2B4)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [reminderAgentManager.cancelAllReminders](../../ohos-reminderagentmanager-agent-powered-reminder/document.md#reminderagentmanagercancelallreminders).

**System capability**: SystemCapability.Notification.ReminderAgent

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Example**

import { BusinessError } from '@ohos.base';

reminderAgent.cancelAllReminders((err: BusinessError, data: void) =>{
  console.info("cancelAllReminders callback")
})

#### reminderAgent.cancelAllReminders(deprecated)

cancelAllReminders(): Promise<void>

Cancels all reminders set by the current application. This API uses a promise to return the cancellation result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/Bp854XoeRuShy-bthSiOww/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062318Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=923EE3879678731AC61A794EDE9BDBE5671C51E79D0E75680D285027ACCBDF4D)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [reminderAgentManager.cancelAllReminders](../../ohos-reminderagentmanager-agent-powered-reminder/document.md#reminderagentmanagercancelallreminders-1).

**System capability**: SystemCapability.Notification.ReminderAgent

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise used to return the result. |

**Example**

reminderAgent.cancelAllReminders().then(() => {
    console.info("cancelAllReminders promise")
})

#### reminderAgent.addNotificationSlot(deprecated)

addNotificationSlot(slot: NotificationSlot, callback: AsyncCallback<void>): void

Adds a notification slot. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/IVOn6DZlTjO8A3BGzNxIZQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062318Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E57AF14171BDB73170C3A6ABA645C4CC8F5CF580FC252BB91EF03651C6CDD609)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [reminderAgentManager.addNotificationSlot](../../ohos-reminderagentmanager-agent-powered-reminder/document.md#reminderagentmanageraddnotificationslot).

**System capability**: SystemCapability.Notification.ReminderAgent

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| slot | [NotificationSlot](../../../../../application-services/notification-kit/arkts-apis/apis-no-longer-maintained/ohos-notification-notification/document.md#notificationslot) | Yes | Notification slot, whose type can be set. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Example**

import notification from '@ohos.notificationManager'
import { BusinessError } from '@ohos.base';

let mySlot:notification.NotificationSlot = {
  type: notification.SlotType.SOCIAL\_COMMUNICATION
}
reminderAgent.addNotificationSlot(mySlot, (err: BusinessError, data: void) => {
  console.info("addNotificationSlot callback");
});

#### reminderAgent.addNotificationSlot(deprecated)

addNotificationSlot(slot: NotificationSlot): Promise<void>

Adds a notification slot. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/1IrX7fHDTs6GHq5fPS4anA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062318Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=45A88838D2CF403EE8B4F64FCAF896FBD6EC3A16F5DE717E5FC21AE0E5B98389)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [reminderAgentManager.addNotificationSlot](../../ohos-reminderagentmanager-agent-powered-reminder/document.md#reminderagentmanageraddnotificationslot-1).

**System capability**: SystemCapability.Notification.ReminderAgent

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| slot | [NotificationSlot](../../../../../application-services/notification-kit/arkts-apis/apis-no-longer-maintained/ohos-notification-notification/document.md#notificationslot) | Yes | Notification slot, whose type can be set. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise used to return the result. |

**Example**

import notification from '@ohos.notificationManager'

let mySlot:notification.NotificationSlot = {
  type: notification.SlotType.SOCIAL\_COMMUNICATION
}
reminderAgent.addNotificationSlot(mySlot).then(() => {
  console.info("addNotificationSlot promise");
});

#### reminderAgent.removeNotificationSlot(deprecated)

removeNotificationSlot(slotType: notification.SlotType, callback: AsyncCallback<void>): void

Removes a notification slot of a specified type. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/HNoXXfU8RBquM6RePUuNGw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062318Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DAF4F4752582A19E6A56F14DC3737B8FEE6223DF4425EA91ABF0216BC754D7FB)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [reminderAgentManager.removeNotificationSlot](../../ohos-reminderagentmanager-agent-powered-reminder/document.md#reminderagentmanagerremovenotificationslot).

**System capability**: SystemCapability.Notification.ReminderAgent

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| slotType | [notification.SlotType](../../../../../application-services/notification-kit/arkts-apis/apis-no-longer-maintained/ohos-notification-notification/document.md#slottype) | Yes | Type of the reminder notification slot to remove. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Example**

import notification from '@ohos.notification'
import { BusinessError } from '@ohos.base';

reminderAgent.removeNotificationSlot(notification.SlotType.CONTENT\_INFORMATION, (err: BusinessError, data: void) => {
  console.info("removeNotificationSlot callback");
});

#### reminderAgent.removeNotificationSlot(deprecated)

removeNotificationSlot(slotType: notification.SlotType): Promise<void>

Removes a notification slot of a specified type. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/n4N07gQPQXOfgdcQn3M7Yw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062318Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=699346B1572AA12CD1DD162AF85D6E3475FBA9B95B69D6D6F0CF78A9B8BB9974)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [reminderAgentManager.removeNotificationSlot](../../ohos-reminderagentmanager-agent-powered-reminder/document.md#reminderagentmanagerremovenotificationslot-1).

**System capability**: SystemCapability.Notification.ReminderAgent

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| slotType | [notification.SlotType](../../../../../application-services/notification-kit/arkts-apis/apis-no-longer-maintained/ohos-notification-notification/document.md#slottype) | Yes | Type of the reminder notification slot to remove. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise used to return the result. |

**Example**

import notification from '@ohos.notification'

reminderAgent.removeNotificationSlot(notification.SlotType.CONTENT\_INFORMATION).then(() => {
    console.info("removeNotificationSlot promise");
});

#### ActionButtonType(deprecated)

Enumerates the button types.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/XQ_t7cMuTZ-oCoK4tu_Veg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062318Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1DE61BAAFA627DEEF940206C268356CBDFC5F3D4A311F12BA49C8A31821FCE4F)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [reminderAgentManager.ActionButtonType](../../ohos-reminderagentmanager-agent-powered-reminder/document.md#actionbuttontype) instead.

**System capability**: SystemCapability.Notification.ReminderAgent

| Name | Value | Description |
| :-- | :-- | :-- |
| ACTION\_BUTTON\_TYPE\_CLOSE | 0 | Button for closing the reminder. |
| ACTION\_BUTTON\_TYPE\_SNOOZE | 1 | Button for snoozing the reminder. |

#### ReminderType(deprecated)

Enumerates reminder types.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/wR4vONA_Q8Cpt9WDi0HW4A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062318Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8C5CF52ABF87B402D81453BE6E0E7CCF23D6EF2DAE7EFA4447862C1270EDAD7E)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [reminderAgentManager.ReminderType](../../ohos-reminderagentmanager-agent-powered-reminder/document.md#remindertype) instead.

**System capability**: SystemCapability.Notification.ReminderAgent

| Name | Value | Description |
| :-- | :-- | :-- |
| REMINDER\_TYPE\_TIMER | 0 | Countdown reminder. |
| REMINDER\_TYPE\_CALENDAR | 1 | Calendar reminder. |
| REMINDER\_TYPE\_ALARM | 2 | Alarm reminder. |

#### ActionButton(deprecated)

Defines a button displayed in the reminder notification.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/pP4yz790QA--TbxmLdFf7Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062318Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C85BF35EFA87D51EEF3458D8CDAE4D0AC8DFB23B6336EE928302497E22C87018)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [reminderAgentManager.ActionButton](../../ohos-reminderagentmanager-agent-powered-reminder/document.md#actionbutton) instead.

**System capability**: SystemCapability.Notification.ReminderAgent

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| title | string | No | No | Text on the button. |
| type | [ActionButtonType](#actionbuttontypedeprecated) | No | No | Button type. |

#### WantAgent(deprecated)

Sets the package and ability that are redirected to when the reminder notification is clicked.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/ZzqX9tImSf26HEGY79FBzg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062318Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C35999B3AF4C3C035AB9D8C3AA19318483837F030BBFBA062D3744EB8BEB8F94)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [reminderAgentManager.WantAgent](../../ohos-reminderagentmanager-agent-powered-reminder/document.md#wantagent) instead.

**System capability**: SystemCapability.Notification.ReminderAgent

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| pkgName | string | No | No | Name of the HAP that is redirected to when the reminder notification is clicked. |
| abilityName | string | No | No | Name of the ability that is redirected to when the reminder notification is clicked. |

#### MaxScreenWantAgent(deprecated)

Provides the information about the target package and ability to start automatically when the reminder is displayed in full-screen mode. This API is reserved.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/1-3dXGHZS6icy3iGAA4vaQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062318Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A3C8375205A204D794BCB27F97623CE72A454F671D609C8F4FDBF55F2D9A6775)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [reminderAgentManager.MaxScreenWantAgent](../../ohos-reminderagentmanager-agent-powered-reminder/document.md#maxscreenwantagent).

**System capability**: SystemCapability.Notification.ReminderAgent

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| pkgName | string | No | No | Name of the HAP that is automatically started when the reminder arrives and the device is not in use. |
| abilityName | string | No | No | Name of the ability that is automatically started when the reminder arrives and the device is not in use. |

#### ReminderRequest(deprecated)

Defines the reminder to publish.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3/v3/VxG7zbu4Rw2G68aHmwkZIw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062318Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=36D124863BF98DA5C21AC85A6AF1214CB8C7628BDE31529DE97207106AD29663)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [reminderAgentManager.ReminderRequest](../../ohos-reminderagentmanager-agent-powered-reminder/document.md#reminderrequest) instead.

**System capability**: SystemCapability.Notification.ReminderAgent

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| reminderType | [ReminderType](#remindertypedeprecated) | No | No | Type of the reminder. |
| actionButton | \[[ActionButton](#actionbuttondeprecated)?, [ActionButton](#actionbuttondeprecated)?\] | No | Yes | Button displayed in the reminder notification. (The parameter is optional. Up to two buttons are supported.) |
| wantAgent | WantAgent | No | Yes | Information about the ability that is redirected to when the notification is clicked. |
| maxScreenWantAgent | [MaxScreenWantAgent](#maxscreenwantagentdeprecated) | No | Yes | Information about the ability that is automatically started when the reminder arrives. If the device is in use, a notification will be displayed. |
| ringDuration | number | No | Yes | Ringing duration, in seconds. The default value is **1**. |
| snoozeTimes | number | No | Yes | Number of reminder snooze times. The default value is **0**. |
| timeInterval | number | No | Yes | Reminder snooze interval, in seconds. The default value is **0**. |
| title | string | No | Yes | Reminder title. |
| content | string | No | Yes | Reminder content. |
| expiredContent | string | No | Yes | Content to be displayed after the reminder expires. |
| snoozeContent | string | No | Yes | Content to be displayed when the reminder is snoozing. |
| notificationId | number | No | Yes | Notification ID used by the reminder. If there are reminders with the same notification ID, the later one will overwrite the earlier one. |
| slotType | [notification.SlotType](../../../../../application-services/notification-kit/arkts-apis/apis-no-longer-maintained/ohos-notification-notification/document.md#slottype) | No | Yes | Type of the slot used by the reminder. |

#### ReminderRequestCalendar(deprecated)

Defines a reminder for a calendar event.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/oGsc_MEzRnqZHa2eRA2IWg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062318Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9C20E2386B41F5CDE9F48D7ABE8689C8ED7194AA4D44568F29FF065EF2D6AB06)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [reminderAgentManager.ReminderRequestCalendar](../../ohos-reminderagentmanager-agent-powered-reminder/document.md#reminderrequestcalendar) instead.

**System capability**: SystemCapability.Notification.ReminderAgent

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| dateTime | [LocalDateTime](#localdatetimedeprecated) | No | No | Reminder time. |
| repeatMonths | Array<number> | No | Yes | Month in which the reminder repeats. |
| repeatDays | Array<number> | No | Yes | Date on which the reminder repeats. |

#### ReminderRequestAlarm(deprecated)

Defines a reminder for an alarm.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/TVkPtz6NTZOqVZaf3vRkyg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062318Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=851E9F9609248D2D2017C7B9DAE8F247236120D09141B76FDBC484D0D4C2BC97)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [reminderAgentManager.ReminderRequestAlarm](../../ohos-reminderagentmanager-agent-powered-reminder/document.md#reminderrequestalarm) instead.

**System capability**: SystemCapability.Notification.ReminderAgent

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| hour | number | No | No | Hour portion of the reminder time. |
| minute | number | No | No | Minute portion of the reminder time. |
| daysOfWeek | Array<number> | No | Yes | Days of a week when the reminder repeats. The value ranges from 1 to 7, corresponding to the data from Monday to Sunday. |

#### ReminderRequestTimer(deprecated)

Defines a reminder for a scheduled timer.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/0gKmUgOUQfmz1_Zla1IbqQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062318Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=29969FDC07DF0884577DCECD62D4955EF4C57F8AA301B8889B3683A142AC50DF)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [reminderAgentManager.ReminderRequestTimer](../../ohos-reminderagentmanager-agent-powered-reminder/document.md#reminderrequesttimer) instead.

**System capability**: SystemCapability.Notification.ReminderAgent

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| triggerTimeInSeconds | number | No | No | Number of seconds in the countdown timer. |

#### LocalDateTime(deprecated)

Sets the time information for a calendar reminder.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/06/v3/WgbTssY6Ro6gupdN1oq93A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062318Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3541349CC3C2EC9ABB265E9CE38B287DB2B6F3C0BFC6D151A88A122A552C870C)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [reminderAgentManager.LocalDateTime](../../ohos-reminderagentmanager-agent-powered-reminder/document.md#localdatetime) instead.

**System capability**: SystemCapability.Notification.ReminderAgent

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| year | number | No | No | Year. |
| month | number | No | No | Month. |
| day | number | No | No | Date. |
| hour | number | No | No | Hour. |
| minute | number | No | No | Minute. |
| second | number | No | Yes | Second. |
