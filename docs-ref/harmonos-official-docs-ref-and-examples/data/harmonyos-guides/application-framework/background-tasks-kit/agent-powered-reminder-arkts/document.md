# Agent-powered Reminder (ArkTS)

#### Introduction

When an application is backgrounded or closed, the system can still send scheduled notifications on behalf of the application. Currently, the following reminder types are supported: timer, calendar, and alarm.To prevent agent-powered reminders from being abused for advertising and marketing, which may affect user experience, a control mechanism is added to agent-powered reminders on some devices. The application cannot directly use agent-powered reminders. For details about the usage after control, see [Constraints](#constraints).

#### Constraints

-   **Device**: The agent reminder applies to mobile phones, tablets, PCs/2-in-1 devices, and smart wearables.
    
-   **Control**:
    

1.  Mobile phones, tablets, and PCs/2-in-1 devices, are under control, but wearable devices are not.
2.  After the control, Calendar Kit can be used to implement the corresponding reminder functionality. For details, see [Calendar Kit Development](../../../application-services/calendar-kit/about-this-kit/document.md). Alternatively, you can request the agent-powered reminder permission from Huawei by email in the following format. Currently, this operation is available only for pure utility applications.

**Email format**:

Send a request to [hwpush@huawei.com](mailto:hwpush@huawei.com). You will receive a reply within 10 working days with the approval result. Once your request is approved, the permission will take effect the next day. Keep an eye on your inbox. The email format is as follows:

Subject: \[Request for the Agent-Powered Reminder Permission\]

Email body:

Permission name: Agent-powered Reminder

Enterprise name:

Application name: \*\*\*

Application's bundle name: com.**.**

Usage scenario: Provide the reason, purpose, and the necessity of using the agent to send notifications or reminders. Attach pictures (if any).

Notification title: \*\*\*

Notification text: \*\*\*

Notification scenario: \*\*\*

Notification frequency: \*\*\*

-   **Quantity**:

1.  A maximum of 30 valid or unexpired reminders can be set for a regular application.
2.  Since API version 10, the total number of valid and unexpired reminders for all applications cannot exceed 12,000. For API version 9 and earlier versions, the total number of valid and unexpired reminders cannot exceed 2,000.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/eFMDa4DFTSumc7uBtXng-g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061950Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4DA1D074F22F500CFB0D812E3F5B50654BE5DA750C54F25B9AECC9CBA356BA2C)

When the reminder time arrives, the notification center displays the relevant reminder. The reminder remains active and unexpired unless the user touches the CLOSE button, at which point the reminder becomes expired.

For a recurring reminder (for example, a daily reminder), the reminder is always valid regardless of whether the user touches the CLOSE button.

-   **Redirection limit**: The application that is redirected to upon a click on the notification must be the application that requested the agent-powered reminder.

#### Relationship with Other Kits

-   When the preset time arrives, notifications created by Notification Kit will be displayed in the notification center. For details about notification styles, see [Notification Style](../../../application-services/notification-kit/about-this-kit/document.md#notification-style).

#### Emulator Support

This capability is supported by the Emulator since API version 20.

#### Available APIs

The table below uses promise as an example to describe the APIs used for developing agent-powered reminders. For details about more APIs and their usage, see [reminderAgentManager](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-reminderagentmanager).

**Table 1** Main APIs for agent-powered reminders

| API | Description |
| :-- | :-- |
| publishReminder(reminderReq: ReminderRequest): Promise<number> | Publishes a reminder. |
| cancelReminder(reminderId: number): Promise<void> | Cancels a reminder published. |
| getValidReminders(): Promise<Array<ReminderRequest>> | Obtains all [valid (not yet expired) reminders](#constraints) set by the current application. |
| cancelAllReminders(): Promise<void> | Cancels all reminders set by the current application. |
| addNotificationSlot(slot: NotificationSlot): Promise<void> | Adds a notification slot. |
| removeNotificationSlot(slotType: notification.SlotType): Promise<void> | Removes a notification slot. |

#### How to Develop

## Requesting Permissions

Declare the ohos.permission.PUBLISH\_AGENT\_REMINDER permission. For details, see [Declaring Permissions](../../../system/security/application-access-control/application-permission-management/requesting-application-permissions/declaring-permissions/document.md).

## Requesting Notification Authorization

[Request notification authorization](../../../application-services/notification-kit/requesting-notification-authorization/document.md). Agent-powered reminders can be used only after being authorized by the user.

## Developing Functionalities

1.  Import the modules.
    
    import { notificationManager } from '@kit.NotificationKit';
    import { reminderAgentManager } from '@kit.BackgroundTasksKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
2.  Define a reminder. You can define the following types of reminders based on project requirements.
    
    -   Timer
        
        let timer: reminderAgentManager.ReminderRequestTimer = {
          reminderType: reminderAgentManager.ReminderType.REMINDER\_TYPE\_TIMER,  // The reminder type is countdown timer.
          ringDuration: Constant.REMINDER\_DURATION,
          title: context.resourceManager.getStringSync($r('app.string.timer').id),  // Reminder title. The value in the "app.string.timer" resource file is "timer".
          content: context.resourceManager.getStringSync($r('app.string.countdown\_close').id),  // Reminder content. The value in the "app.string.countdown\_close" resource file is "timer ended".
          wantAgent: {  // // Information about the target UIAbility that is displayed after the reminder notification is touched.
            pkgName: 'com.example.reminderagentmanager',
            abilityName: 'EntryAbility'
          },
          notificationId: 100, // Notification ID used by the reminder. If there are reminders with the same notification ID, the later one will overwrite the earlier one.
          slotType: notificationManager.SlotType.CONTENT\_INFORMATION,  // Type of the slot used by the reminder.
          triggerTimeInSeconds: this.countdownTime
        };
        
    -   Calendar
        
        let calendar: reminderAgentManager.ReminderRequestCalendar = {
          reminderType: reminderAgentManager.ReminderType.REMINDER\_TYPE\_CALENDAR,  // The reminder type is calendar event.
          dateTime: {  // Reminder time.
            year: date.getFullYear(),
            month: date.getUTCMonth() + 1,
            day: date.getDate(),
            hour: date.getHours(),
            minute: date.getMinutes(),
          },
          actionButton:  // Set the button type and title displayed for the reminder in the notification panel.
          \[{
            title: context.resourceManager.getStringSync($r('app.string.calendar\_close').id),  // The value in the "app.string.calendar\_close" resource file is "disable calendar reminder".
            type: reminderAgentManager.ActionButtonType.ACTION\_BUTTON\_TYPE\_CLOSE
          }\],
          // Information about the target UIAbility that is displayed after the reminder notification is touched.
          wantAgent: { pkgName: 'com.example.reminderagentmanager', abilityName: 'EntryAbility' },
          ringDuration: Constant.REMINDER\_DURATION,  // Ringing duration, in seconds.
          title: context.resourceManager.getStringSync($r('app.string.calendar').id),  // Reminder title. The value in the "app.string.calendar" resource file is "calendar".
          content: context.resourceManager.getStringSync($r('app.string.calendar\_reach').id),  // Reminder content. The value in the "app.string.calendar\_reach" resource file is "calendar reminder time is up".
          slotType: notificationManager.SlotType.CONTENT\_INFORMATION  // Type of the slot used by the reminder.
        }
        
    -   Alarm
        
        let alarm: reminderAgentManager.ReminderRequestAlarm = {
          reminderType: reminderAgentManager.ReminderType.REMINDER\_TYPE\_ALARM,  // The reminder type is alarm clock.
          hour: time.hour,  // Hour portion of the reminder time.
          minute: time.minute,  // Minute portion of the reminder time.
          actionButton:  // Set the button type and title displayed for the reminder in the notification panel.
          \[
            {
              title: context.resourceManager.getStringSync($r('app.string.alarm\_clock\_close').id),  // The value in the "app.string.alarm\_clock\_close" resource file is "disable alarm clock".
              type: reminderAgentManager.ActionButtonType.ACTION\_BUTTON\_TYPE\_CLOSE
            },
            {
              title: context.resourceManager.getStringSync($r('app.string.alarm\_clock\_postpone').id),  // The value in the "app.string.alarm\_clock\_postpone" resource file is "postpone alarm clock".
              type: reminderAgentManager.ActionButtonType.ACTION\_BUTTON\_TYPE\_SNOOZE
            }
          \],
          slotType: notificationManager.SlotType.CONTENT\_INFORMATION,  // Type of the slot used by the reminder.
          ringDuration: Constant.REMINDER\_DURATION,  // Ringing duration, in seconds.
          wantAgent: {  // Information about the target UIAbility that is displayed after the reminder notification is touched.
            pkgName: 'com.example.reminderagentmanager',
            abilityName: 'EntryAbility'
          },
          title: context.resourceManager.getStringSync($r('app.string.alarm\_clock').id),  // Reminder title. The value in the "app.string.alarm\_clock" resource file is "alarm clock".
          content: context.resourceManager.getStringSync($r('app.string.alarm\_clock\_reach').id),  // Reminder content. The value in the "app.string.alarm\_clock\_reach" resource file is "alarm time is up".
          snoozeTimes: 0,  // Number of reminder snooze times.
          timeInterval: 0,  // Reminder snooze interval, in seconds.
          daysOfWeek: \[\]  // Days of a week when the reminder repeats.
        }
        
3.  Publish the reminder. After the reminder is published, your application can use the agent-powered reminder feature.
    
    let reminderId: number = await reminderAgentManager.publishReminder(
      this.calendarReminders\[index\].reminderRequestCalendar!);
    Logger.info(TAG, \`publish reminder result: id is ${reminderId}\`);
    this.calendarReminders\[index\].reminderId = reminderId;  // Save the ID of the published reminder.
    
4.  Delete the reminder as required.
    
    Logger.info(TAG, \`cancel reminder id is ${this.calendarReminders\[index\].reminderId}\`)
    await reminderAgentManager.cancelReminder(this.calendarReminders\[index\].reminderId);
