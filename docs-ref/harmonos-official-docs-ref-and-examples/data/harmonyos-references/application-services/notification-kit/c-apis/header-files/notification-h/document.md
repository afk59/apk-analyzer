# notification.h

#### Overview

Defines APIs for notification services.

**File to include**: <NotificationKit/notification.h>

**Library**: libohnotification.so

**System capability**: SystemCapability.Notification.Notification

**Since**: 13

**Related module**: [NOTIFICATION](../../modules/notification/document.md)

#### Summary

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [bool OH\_Notification\_IsNotificationEnabled(void)](#oh_notification_isnotificationenabled) | Checks whether the notification of the specified application is enabled. |

#### Function Description

#### \[h2\]OH\_Notification\_IsNotificationEnabled()

bool OH\_Notification\_IsNotificationEnabled(void)

**Description**

Checks whether the notification of the specified application is enabled.

**Since**: 13

**Returns**

| Type | Description |
| :-- | :-- |
| bool | 
**true** - Notification is enabled for the specified application.

**false** - Notification is not enabled for the specified application.

 |
