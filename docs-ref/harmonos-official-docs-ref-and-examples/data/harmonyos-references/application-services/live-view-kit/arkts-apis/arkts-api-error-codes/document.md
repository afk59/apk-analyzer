# ArkTS API Error Codes

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/Kz34EyPkSQWMb-4qjKeXtg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062510Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5BD48614F0695BE4DD31DABE91EF703998CFB14FED35E7B848277D8DD894A1A8)

This topic describes only module-specific error codes. For details about universal error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

#### 1003500001 System Error

**Message**

Internal error.

**Description**

This error code is reported when a system error occurs.

**Possible causes**

An internal system error occurs.

**Solution**

Retry or [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

#### 1003500002 Marshalling or Unmarshalling Error

**Message**

Marshalling or unmarshalling error.

**Description**

This error code is reported when a marshalling or unmarshalling error occurs.

**Possible causes**

Live View Kit is abnormal.

**Solution**

Retry or [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

#### 1003500003 Failed to Connect to the Service

**Message**

Failed to connect service.

**Description**

This error code is reported when an error occurs in connecting to Live View Kit.

**Possible causes**

Live View Kit is busy or abnormal.

**Solution**

Retry or [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

#### 1003500004 Live View Notification Is Disabled

**Message**

LiveView is not enabled.

**Description**

This error code is reported when live view notification is disabled.

**Possible causes**

Live view notification is not enabled for the app.

**Solution**

Go to **Settings** > **Apps & services** on the device, select your app, and enable live view notification.

#### 1003500005 The Live View Permission of a Specific Scenario Has Not Been Applied for

**Message**

The right of liveView is not enabled.

**Description**

This error code is reported when the live view permission of a specific scenario has not been applied for.

**Possible causes**

Your app has not applied for the live view permission of a specific scenario.

**Solution**

If you have applied for the live view permission of a specific scenario, ensure that the **event** parameter value matches the scenario. If you have not applied for the live view permission of a specific scenario, go to AppGallery Connect and apply for the permission.

#### 1003500006 The Live View Already Exists

**Message**

The liveView already exists.

**Description**

This error code is reported when a live view ID already exists during live view creation.

**Possible causes**

The ID of a live view to be created is the same as that of an existing live view.

**Solution**

Change the [live view ID](../liveviewmanager/document.md#section411410371767).

#### 1003500007 Failed to Connect to the Server

**Message**

Couldn't connect to server.

**Description**

This error code is reported when the network is unreachable.

**Possible causes**

The device is not connected to the network.

**Solution**

Check the network.

#### 1003500008 The Live View Operation Frequency Exceeds the Upper Limit

**Message**

Over max number liveViews per second.

**Description**

This error code is reported when the live view operation frequency exceeds the upper limit.

**Possible causes**

For the same app, the live view creation frequency exceeds 10 per second or the live view update frequency exceeds 20 per second.

**Solution**

Reduce the live view operation frequency.

#### 1003500009 The Live View ID Does Not Exist

**Message**

The liveView does not exist.

**Description**

This error code is reported when a live view ID does not exist.

**Possible causes**

The live view ID does not exist or the live view has been deleted.

**Solution**

1.  Check whether the operation of [creating a live view](../liveviewmanager/document.md#section195321751104612) is successful.
2.  If the creation is successful, check whether the live view exists in the notification panel on the device. If the live view does not exist, stop calling APIs for this [live view ID](../liveviewmanager/document.md#section411410371767).

#### 1003500010 The Live View Has Ended

**Message**

The liveView has ended.

**Description**

This error code is reported when you try to update or end a live view that has been ended.

**Possible causes**

After a live view is ended by [liveViewManager.stopLiveView](../liveviewmanager/document.md#section929145112243), it is still stored in the notification panel within the duration specified by **keepTime**. As a result, this error code is reported when [liveViewManager.updateLiveView](../liveviewmanager/document.md#section1310319579406) or [liveViewManager.stopLiveView](../liveviewmanager/document.md#section929145112243) is called to update or end the live view with the same ID.

**Solution**

Do not call the live view update or ending API for this [live view ID](../liveviewmanager/document.md#section411410371767) before the live view disappears from the notification panel.

#### 1003500011 Incorrect Live View Sequence

**Message**

The liveView sequence is incorrect.

**Description**

This error code is reported when the new sequence number for updating or ending a live view is less than or equal to the current sequence number.

**Possible causes**

The new sequence number for updating or ending a live view is less than or equal to the current sequence number.

**Solution**

Change the [sequence](../liveviewmanager/document.md#section411410371767) parameter value and try to update or end the live view again.

#### 1003500012 The Number of Subscriptions Exceeds the Upper Limit

**Message**

The number of subscription times exceeds the upper limit of 2000.

**Description**

The number of subscriptions exceeds the upper limit.

**Possible causes**

Each user can have a maximum of 2000 subscriptions for each app.

**Solution**

Adjust the number of subscriptions.

#### 1003500013 Invalid Live View Subscription Scenario

**Message**

Invalid event type.

**Description**

Invalid live view subscription scenario.

**Possible causes**

The value of **event** is incorrect.

**Solution**

Verify the **event** parameter setting.

#### 1003500014 The Period Between the Current Time and Live View Alert Time Is Too Long

**Message**

Time exceeds valid period.

**Description**

The period between the current time and live view alert time is too long.

**Possible causes**

The period between the current time and the time specified by **alertTime** exceeds 30 days.

**Solution**

Verify the **alertTime** and **startTime** parameter settings.

#### 1003500015 Live View Subscription Failed

**Message**

Subscribe failed.

**Description**

Live view subscription failed.

**Possible causes**

There is an internal error on the cloud.

**Solution**

Retry or [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

#### 1003500016 The Request Frequency Exceeds the Limit

**Message**

Request subscribe liveView exceed.

**Description**

The request frequency exceeds the limit.

**Possible causes**

The number of subscriptions is too large within a short period of time.

**Solution**

Adjust the subscription frequency.
