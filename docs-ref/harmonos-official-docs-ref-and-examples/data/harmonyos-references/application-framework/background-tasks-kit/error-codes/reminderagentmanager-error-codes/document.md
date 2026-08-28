# reminderAgentManager Error Codes

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/9HF7QctcSVuG7HNZGvEtxA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062319Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A8E204511FEAB11B463586C2D415CE2B190CAB385CA58BDFC675451177F6FA32)

This topic describes only module-specific error codes. For details about universal error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

#### 1700001 Notification Disabled

**Error Message**

Notification is not enabled.

**Description**

The application is not allowed to send notifications when **publishReminder()** is called.

**Possible Causes**

1.  The application has not requested the notification to be enabled.
2.  The notification feature is not enabled for the application.

**Solution**

1.  Use [notificationManager.requestEnableNotification](../../../../application-services/notification-kit/arkts-apis/ohos-notificationmanager-notificationmanager/document.md#notificationmanagerrequestenablenotification10) to request the notification to be enabled.
2.  Enable notification for the application in the notification settings.

#### 1700002 Too Many Reminders

**Error Message**

The number of reminders exceeds the limit.

**Description**

The number of reminders exceeds the limit when **publishReminder()** is called.

**Possible Causes**

1.  Regular applications lack permission to use agent-powered reminders, with the total number of reminders set to 0.
2.  The number of reminders for a regular application exceeds 30.
3.  In API version 10 and later versions, the total number of reminders across all applications exceeds 12,000. In API version 9 and earlier versions, the total number of reminders across all applications exceeds 2,000.

Solution

1.  First, check if you have [requested permission to use the agent-powered reminder](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/agent-powered-reminder#constraints).
2.  If the request is approved, check whether the number of reminders exceeds the limit and delete any unnecessary reminders promptly.

#### 1700003 Nonexistent Reminder

**Error Message**

The reminder does not exist.

**Description**

The reminder passed in **cancelReminder()** does not exist.

**Possible Causes**

1.  The reminder has expired.
2.  The reminder has been deleted.

**Solution**

1.  Check whether the reminder is valid.
2.  Check whether the reminder has been deleted.

#### 1700004 Nonexistent Bundle Name

**Error Message**

The bundle name does not exist.

**Description**

The bundle name passed is not found.

**Possible Causes**

1.  The bundle name is incorrect.
2.  The application is not installed.

**Solution**

Check whether the bundle name exists.

#### 1700007 Invalid Parameter

**Error Message**

If the input parameter is not valid parameter.

**Description**

The input parameter is invalid.

**Possible Causes**

The parameter does not comply with the rules.

**Solution**

Make sure all the mandatory parameters are passed in and the parameter types are valid. If parameter verification fails, read the parameter specifications and locate the fault based on the possible causes.
