# ArkTS API Error Codes

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/zRUjJ6DFRn6iATB4QaDNmQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062518Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=012CC90A5879BFED04E5603EEAFFAD61AA6FE75D9176600A96F0D07ADAFD991B)

This section describes only module-specific error codes. For details about universal error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

#### 1000900001 System Error

**Message**

System internal error.

**Description**

This error code is reported when a system internal error occurs.

**Possible causes**

An unknown error occurred.

**Solution**

1.  Try again.
2.  If the error persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).
3.  If the [pushService.on('tokenUpdate')](../pushservice/document.md#section1730794845210) API returns error code 1000900001, check for repeated registrations.

#### 1000900002 Extension Does Not Exist

**Message**

Extension does not exist.

**Description**

This error code is reported when the ExtensionAbility does not exist.

**Possible causes**

The ExtensionAbility to be started does not exist in the system.

**Solution**

Verify that the extensionAbilities module is correctly configured in the **src/main/module.json5** file of the project based on the scenario-specific message type.

#### 1000900003 Extension Callback Execution Failure

**Message**

Extension callback execution failed.

**Description**

This error code is reported when the ExtensionAbility callback execution fails.

**Possible causes**

An exception occurred when the [onReceiveMessage](../remotenotificationextensionability/document.md#section455013322919)() callback of the ExtensionAbility is executed.

**Solution**

Verify the code execution logic in the [onReceiveMessage](../remotenotificationextensionability/document.md#section455013322919)() callback of the ExtensionAbility.

#### 1000900004 ExtensionAbility Callback Execution Timeout

**Message**

Extension callback execution timed out.

**Description**

This error code is reported when the ExtensionAbility callback execution times out.

**Possible causes**

Executing the [onReceiveMessage](../remotenotificationextensionability/document.md#section455013322919)() callback of the ExtensionAbility timed out.

**Solution**

Verify the code execution logic in the [onReceiveMessage](../remotenotificationextensionability/document.md#section455013322919)() callback of the ExtensionAbility.

#### 1000900005 Repeated Registration of the Same Scenario-Specific Message Is Not Allowed

**Message**

Messages of the same push type cannot be received repeatedly.

**Description**

This error code is reported when a same type of scenario-specific messages is repeatedly registered.

**Possible causes**

pushService.[receiveMessage](../pushservice/document.md#section125883044911)() is called repeatedly to register a same type of scenario-specific messages.

**Solution**

Delete unnecessary pushService.[receiveMessage](../pushservice/document.md#section125883044911)() calls, and process the received scenario-specific message in the same callback.

#### 1000900006 AAID Service Connection Failure

**Message**

Failed to connect to the AAID service.

**Description**

This error code is reported when an error occurs in the PushService connection.

**Possible causes**

The PushService is faulty.

**Solution**

1.  Try again.
2.  If the error persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

#### 1000900007 AAID Service Internal Error

**Message**

Internal error of the AAID service.

**Description**

This error code is reported when an exception occurs in the internal task processing of the PushService.

**Possible causes**

The internal processing of the PushService timed out or is faulty.

**Solution**

1.  Try again.
2.  If the error persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

#### 1000900008 Push Kit Connection Failure

**Message**

Failed to connect to the push service.

**Description**

This error code is reported when an error occurs in the PushService connection.

**Possible causes**

The PushService is faulty.

**Solution**

1.  Try again.
2.  If the error persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

#### 1000900009 Push Service Internal Error

**Message**

Internal error of the push service.

**Description**

This error code is reported when an exception occurs in the internal task processing of the PushService.

**Possible causes**

1.  Failed to send a request to the Push Kit server.
2.  The network is unavailable.
3.  The internal processing of the PushService timed out or is faulty.

**Solution**

1.  Restart the device.
2.  Switch to a new network or your hotspot and try again.
3.  If the error persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

#### 1000900010 App Authentication Failure

**Message**

Illegal application identity.

**Description**

This error code is reported if the app identity is invalid.

**Possible causes**

-   The app is configured incorrectly:
    -   The app type specified during its creation in [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html) is not HarmonyOS app.
    -   Push Kit is not enabled under **Project settings** > **Manage open capabilities** in [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html). Please refer to step 5 and step 6 in [Enabling Push Kit](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/push-config-setting#section13206419341) to complete manual signing for the corresponding phase.
    -   Push Kit is enabled under **Project settings** > **Manage open capabilities** in [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html), but the profile is not requested again. Please refer to step 5 and step 6 in [Enabling Push Kit](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/push-config-setting#section13206419341) to complete manual signing for the corresponding phase.
-   The network is unavailable.
-   The Huawei server is faulty.
-   Push Kit does not support debugging on remote real devices.

**Solution**

1.  Verify that the app configuration is correct.
2.  Check your network to ensure that it is working properly.
3.  If the error persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

#### 1000900011 Network Unavailable

**Message**

The network is unavailable.

**Description**

This error code is reported when the network is abnormal.

**Possible causes**

The network is unavailable.

**Solution**

1.  Try again later or reconnect to the network.
2.  The IP address of the push server is allocated dynamically and its access cannot be allowed just by adding the server IP address to the trustlist. You are advised to use a device on an unrestricted network or allow ports 5223 and 443, and then try again.
3.  If the error persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

#### 1000900012 Push Kit Not Enabled

**Message**

Push rights are not activated.

**Description**

This error code is reported when Push Kit is not enabled for the app in AppGallery Connect.

**Possible causes**

Push Kit is not enabled for the app in AppGallery Connect.

**Solution**

Sign in to [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html), find and click the desired project, go to **Grow** > **Push Kit**, and enable Push Kit. For details, please refer to step 3 in [Procedure](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/push-config-setting#section13206419341).

#### 1000900013 Cross-Location Token Application Is Not Allowed

**Message**

Cross-location application is not allowed to obtain the token.

**Description**

This error code is reported when an app obtains a push token across data storage locations.

**Possible causes**

The app obtains a push token across data storage locations

**Solution**

Verify that the device location matches the [data processing location](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/push-config-setting#section18206161914419) set in AppGallery Connect.

#### 1000900014 Token Application Not Supported by Device

**Message**

The device does not support getting token.

**Description**

This error code is reported when the device does not support token application.

**Possible causes**

The device does not support token application.

**Solution**

Use a phone, tablet, or PC/2-in-1 device for debugging. Support for wearables is available starting from 5.1.0(18), and for TVs starting from 5.1.1(19).

#### 1000900015 Bound App Accounts Reached Upper Limit

**Message**

The number of bound profile-app relationships exceeds the maximum.

**Description**

This error code is reported when the number of bound app accounts, specifically, accounts in the app's own account system, has reached the upper limit.

**Possible causes**

The number of bound app accounts exceeds the upper limit (10).

**Solution**

Call **pushService.**[unbindAppProfileId](../pushservice/document.md#section915174525214)() to unbind some accounts and try again. For details about the recommended binding and unbinding time, please refer to [Developing Account Authentication for Notification Messages](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/push-send-alert#section1677618118810).

#### 1000900016 HUAWEI ID Not Signed In

**Message**

The os distributed account is not logged in.

**Description**

This error code is reported when the HUAWEI ID is not signed in.

**Possible causes**

The HUAWEI ID to be bound is not signed in.

**Solution**

Go to **Settings** on the device and check whether the HUAWEI ID is signed in. If not, sign in with the HUAWEI ID and try again.

#### 1000900018 API Calls Too Frequent

**Message**

Number of calls exceeded.

**Description**

This error code is reported when API calls are too frequent.

**Possible causes**

The number of requests to this API in a short period of time exceeds the limit.

**Solution**

Decrease the API call frequency.

#### 1000900020 Empty Push Token

**Message**

App token is empty.

**Description**

This error code is reported when the push token of an app is empty.

**Possible causes**

The app does not obtain a push token before calling this API.

**Solution**

[Obtain a push token](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/push-get-token) before calling this API.

#### 1000900021 App Not Registered in AppGallery Connect

**Message**

App is not available or not registered.

**Description**

This error code is reported when the app or atomic service is not found in AppGallery Connect.

**Possible causes**

1\. The app or atomic service is not registered in AppGallery Connect.

2\. The subscription [type](../servicenotification/document.md#section11384539111610) does not match the app type.

**Solution**

1\. Verify that the app or atomic service has completed registration in AppGallery Connect. For details, please refer to [Application Development Preparations](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/application-dev-overview).

2\. Verify that the subscription [type](../servicenotification/document.md#section11384539111610) matches the app type. Currently, only atomic services support subscription through a HUAWEI ID.

#### 1000900022 Notification Disabled

**Message**

Notification switch off.

**Description**

This error code is reported when the app's notification function is disabled.

**Possible causes**

The app's notification function is disabled.

**Solution**

Go to **Settings** > **Notifications & status bar** and enable the notification function for the app.

#### 1000900023 Number of Template IDs Exceeds Upper Limit

**Message**

Number of entity ids exceed the upper limit.

**Description**

This error code is reported when the number of passed template IDs exceeds the upper limit.

**Possible causes**

The number of passed template IDs exceeds the upper limit.

**Solution**

Verify that the number of passed template IDs does not exceed 3.

#### 1000900024 Failure to Display the Notification Subscription Authorization Pop-up

**Message**

Failed to display subscription UI.

**Description**

This error code is reported when the notification subscription authorization pop-up fails to be displayed.

**Possible causes**

The notification subscription authorization pop-up has been displayed in the foreground.

**Solution**

Verify that no notification subscription authorization pop-up is displayed in the foreground.

#### 1000900030 User Has Not Signed in to HUAWEI ID

**Message**

The user has not logged in with HUAWEI ID.

**Description**

This error code is reported when a user has not signed in to the HUAWEI ID during subscription through a HUAWEI ID.

**Possible causes**

The user has not signed in to the HUAWEI ID.

**Solution**

Go to **Settings**, verify that the HUAWEI ID is signed in, and subscribe again.

#### 1000900031 Same Type of Callback Can Be Registered Only Once

**Message**

The same type of callback can be registered only once.

**Description**

The same type of callback can be registered only once.

**Possible causes**

The **pushService.on('distributedMessageReceive')** API is called repeatedly for registration.

**Solution**

Verify that the [pushService.on('distributedMessageReceive')](../pushservice/document.md#section679412149361) API is not called repeatedly.
