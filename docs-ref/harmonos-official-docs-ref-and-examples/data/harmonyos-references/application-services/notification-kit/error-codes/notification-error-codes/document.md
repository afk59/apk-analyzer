# Notification Error Codes

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/ODHkLp0fS1KaoI8meLnMtw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062516Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EA93E45321E07D5D4D822C00366FAE043749E8D46D18803A665544421C92D476)

This topic describes only module-specific error codes. For details about universal error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

#### 1600001 Internal Error

**Error Message**

Internal error.

**Description**

This error code is reported when an error occurs during internal processing, such as multi-thread processing or internal pointer checks.

**Possible Causes**

Common kernel errors such as multi-thread processing and internal processing errors occur.

**Solution**

Make sure the system resources are sufficient.

#### 1600002 Marshalling or Unmarshalling Error

**Error Message**

Marshalling or unmarshalling error.

**Description**

This error code is reported when a marshalling or unmarshalling error occurs before data transmission.

**Possible Causes**

A parameter mismatch is detected between the application and the notification service.

**Solution**

Make sure the application SDK version matches the system version.

#### 1600003 Failed to Connect to the Notification Service

**Error Message**

Failed to connect to the service.

**Description**

This error code is reported when the application fails to connect to the notification service.

**Possible Causes**

The notification service is busy or abnormal.

**Solution**

Restart the system.

#### 1600004 Notification Disabled

**Error Message**

Notification disabled.

**Description**

This error code is reported when notification is disabled.

**Possible Causes**

The notification feature is not enabled for the application.

**Solution**

Enable notification for the application in notification settings.

#### 1600005 Notification Slot Disabled

**Error Message**

Notification slot disabled.

**Description**

This error code is reported when the notification slot is not available.

**Possible Causes**

The notification slot is disabled or has not been added.

**Solution**

1.  Access notification settings and check whether the application has the notification slot. If no, add it.
    
2.  Make sure the notification slot is enabled.
    

#### 1600007 Notification Not Found

**Error Message**

The notification does not exist.

**Description**

This error code is reported when the notification service could not find the notification.

**Possible Causes**

The notification has been canceled or deleted.

**Solution**

None.

#### 1600008 User Not Found

**Error Message**

The user does not exist.

**Description**

This error code is reported when the specified user is not found in the information system.

**Possible Causes**

The user information passed is incorrect.

**Solution**

Verify the user information.

#### 1600009 Notification Sending Limit Reached

**Error Message**

The notification sending frequency reaches the upper limit.

**Description**

This error code is reported when the notification sending frequency reaches the upper limit.

**Possible Causes**

More than 10 notifications are sent per second, or more than 20 notifications are updated per second.

**Solution**

Reduce the notification sending frequency to no more than 10 per second.

#### 1600010 Distributed Operation Failed

**Error Message**

Distributed operation failed.

**Description**

This error code is reported when an error occurs with the distributed database operation or distributed API invoking.

**Possible Causes**

The distributed database could not be operated or the distributed API could not be invoked.

**Solution**

Verify the distributed connection.

#### 1600012 Insufficient Memory Space

**Error Message**

No memory space.

**Description**

This error code is reported when a memory allocation error occurs.

**Possible Causes**

A memory allocation error occurs.

**Solution**

Ensure sufficient system memory.

#### 1600013 Notification Pop-up Window Displayed

**Error Message**

A notification dialog box is already displayed.

**Description**

This error code is reported when the notification pop-up window is displayed.

**Possible Causes**

The notification pop-up window is displayed.

**Solution**

Check whether the notification pop-up window is displayed.

#### 1600014 No Related Permission

**Error Message**

No permission.

**Description**

This error code is reported when you do not have the related permission.

**Possible Causes**

You do not have the related permission.

**Solution**

Check whether you have the related permission.

#### 1600015 Duplicate Configurations not Allowed for the Current Notification Status

**Error Message**

The current notification status does not support duplicate configurations.

**Description**

This error code is reported when the current notification status does not support duplicate configurations.

**Possible Causes**

The current notification status does not support duplicate configurations.

**Solution**

Check whether the notification status is duplicately configured.

#### 1600016 Updated Notification Version Outdated

**Error Message**

The notification version for this update is too low.

**Description**

This error code is reported when the notification version for this update is outdated.

**Possible Causes**

The notification version for this update is outdated.

**Solution**

Check the notification version.

#### 1600018 Notification Settings Page Already Displayed

**Error Message**

The notification settings window is already displayed.

**Description**

This error code is reported when the notification settings page has been displayed.

**Possible Causes**

The notification settings page has been displayed.

**Solution**

Check whether the notification settings page is displayed.

#### 1600020 Applications in the Permission Control List Is Not Allowed to Publish Notifications

**Error Message**

The application is not allowed to send notifications due to permission settings.

**Description**

This error code is reported when an application under the permission control list publishes a notification.

**Possible Causes**

The application is restricted by the enterprise-customized devices.

**Solution**

The application is under permission control of [Enterprise Device Manager](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/mdm-kit-intro) and it cannot exit the permission control list automatically.

#### 1600023 NotificationSubscriberExtensionAbility Not Implemented

**Error Message**

The application does not implement the NotificationSubscriberExtensionAbility.

**Description**

This error code is reported when the application does not implement the NotificationSubscriberExtensionAbility.

**Possible Causes**

The [NotificationSubscriberExtensionAbility](../../arkts-apis/ohos-application-notificationsubscriberextensionability-extensionability-for-not/document.md) is not set or is incorrectly set for the application.

**Solution**

Create a NotificationSubscriberExtensionAbility for the application. For details about how to configure the extension ability, see [NotificationSubscriberExtensionAbility](../../arkts-apis/ohos-application-notificationsubscriberextensionability-extensionability-for-not/document.md) in [ExtensionAbility Component](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/extensionability-overview).
