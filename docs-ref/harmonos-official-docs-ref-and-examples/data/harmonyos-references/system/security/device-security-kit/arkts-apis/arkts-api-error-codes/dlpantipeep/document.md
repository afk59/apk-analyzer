# DlpAntiPeep

#### 201 Permission Verification Failed

**Description**

Permission verification failed.

**Possible causes**

The HAP has not obtained the **ohos.permission.DLP\_GET\_HIDE\_STATUS** permission.

**Solution**

Only apps in the list can apply for this permission. For details about how to apply for this permission, please refer to [Requesting Restricted Permissions](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/declare-permissions-in-acl).

#### 801 Capability Not Supported by Device

**Description**

This API is not supported on the current device.

**Possible causes**

The current device does not support this function.

**Solution**

Do not call this API on devices that do not support this API.

#### 1020600001 Internal Error

**Description**

An internal error occurs in the DlpAntiPeep API.

**Possible causes**

An internal function error occurs. The global screen privacy switch is not enabled.

**Solution**

1\. Try again in the service scenario.

2\. Submit a ticket online for assistance.

#### 1020600002 Screen Privacy Not Enabled

**Description**

The screen privacy switch is not enabled.

**Possible causes**

The global screen privacy switch or the app-level switch is not enabled under system settings.

**Solution**

Enable the screen privacy switch and try again.

Step 1: Go to **Settings** > **Privacy & security** > **Screen Privacy**, and enable the global screen privacy switch. Then enable the screen privacy switch for the desired app.

Step 2: Go to the lock screen and perform face unlock.

#### 1020600003 App Not in the Foreground

**Description**

The app failed to call the screen privacy API because it was not in the foreground.

**Possible causes**

The app was in the background when it called the screen privacy API.

**Solution**

Try again when the app is in the foreground.
