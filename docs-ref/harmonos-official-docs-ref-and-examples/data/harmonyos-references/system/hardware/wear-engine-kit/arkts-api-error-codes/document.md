# ArkTS API Error Codes

#### 401 Parameter Error

**Error message**

Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

**Description**

Invalid parameters.

**Possible causes**

A mandatory parameter is missing, or the parameter type is invalid.

**Solution**

1.  Make sure that all the mandatory parameters are passed and the parameter types are valid.
2.  [Submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/). Huawei technical support will get back to you as soon as possible.

#### 801 API Not Supported

**Error message**

Capability not supported.

**Description**

This error code is reported when the device supports the target SysCap but does not support a specific API.

**Possible causes**

The device does not support this API.

**Solution**

Check whether the device supports this API.

#### 1008500001 Network Error

**Error message**

Network error. The network is unavailable.

**Description**

Network error.

**Possible causes**

No network connection.

**Solution**

1.  Check the network configurations.
2.  [Submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/). Huawei technical support will get back to you as soon as possible.

#### 1008500002 No Linked Devices

**Error message**

No device is bound.

**Description**

No linked devices.

**Possible causes**

No wearable device is connected to the phone.

**Solution**

1.  Check whether the device is correctly connected to the phone.
2.  [Submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/). Huawei technical support will get back to you as soon as possible.

#### 1008500003 Device Not Connected

**Error message**

Device disconnected.

**Description**

Device not connected.

**Possible causes**

1.  The Bluetooth connection between the phone and the device is disconnected.
2.  The device disconnects from the Huawei Health app.

**Solution**

1.  Check whether Bluetooth is enabled on both the phone and the device.
2.  Check whether the device has been linked and connected via the Huawei Health app.
3.  [Submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/). Huawei technical support will get back to you as soon as possible.

#### 1008500004 Wear Engine Service Not Applied For

**Error message**

App has not applied for the Wear Engine service.

**Description**

The phone-side app has not applied for the Wear Engine service.

**Possible causes**

1.  The compatibility option was not enabled during the Wear Engine service application process.
2.  You have not applied for the Wear Engine service on HUAWEI Developers.

**Solution**

1.  Check the compatibility option when applying for the Wear Engine service.
2.  [Submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/). Huawei technical support will get back to you as soon as possible.

#### 1008500005 User Authorization Not Granted

**Error message**

The HUAWEI ID is not authorized.

**Description**

The HUAWEI ID fails to be authenticated.

**Possible causes**

The permission required by the API is not granted by the user.

**Solution**

[Request user authorization](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/request_user_authorization) and make sure that the user has granted required permissions.

#### 1008500006 Privacy Statement Not Agreed To

**Error message**

User privacy is not agreed.

**Description**

The user does not agree to the privacy statement of the Huawei Health app.

**Possible causes**

The user has never started the Huawei Health app.

**Solution**

Instruct the user to start the Huawei Health app and agree to the privacy statement.

#### 1008500007 Capability Not Supported on the Wearable Device

**Error message**

The device capability is not supported.

**Description**

Capability not supported on the wearable device.

**Possible causes**

The wearable device does not support the capabilities required to successfully call the current API.

**Solution**

Check the supported device capabilities.

#### 1008500008 Account Not Signed In

**Error message**

Account error. The user has not logged in with HUAWEI ID.

**Description**

Account not signed in.

**Possible causes**

The account is not signed in.

**Solution**

Call the API again after the user signs in to their HUAWEI ID.

#### 1008500009 Account Error

**Error message**

Account error. Failed to obtain account information with HUAWEI ID.

**Description**

Account error.

**Possible causes**

The HUAWEI ID is not registered in the Chinese mainland (excluding Hong Kong, Macao, and Taiwan).

**Solution**

Sign in using a HUAWEI ID registered in the Chinese mainland (excluding Hong Kong, Macao, and Taiwan) and try again.

#### 1008500010 Invalid Device ID

**Error message**

Device ID is invalid.

**Description**

Invalid device ID.

**Possible causes**

1.  An incorrect device ID is passed.
2.  An expired device ID is passed.

**Solution**

Call [getConnectedDevices](../arkts-apis/wearengine-wearable-capabilities/document.md#section1828213119411) to obtain the device ID again.

#### 1008500011 Invalid File

**Error message**

File is invalid.

**Description**

Invalid file.

**Possible causes**

The input file is invalid.

**Solution**

1.  Check whether the file path is valid.
2.  Check whether the file exists.

#### 1008500012 Too Many Callback Functions

**Error message**

Too many callbacks of the same type.

**Description**

Too many callback functions.

**Possible causes**

Too many callback functions of the same type are registered.

**Solution**

Unsubscribe from events that you no longer need to subscribe to.

#### 1008509999 Internal Error

**Error message**

Internal error.

**Description**

Internal error.

**Possible causes**

1.  The app information, such as the signature certificate, does not match that on the cloud.
2.  **randomId** is invalid.
3.  **clientId** has not been configured in the app's metadata.
4.  An unknown error has occurred in the WearEngine service.

**Solution**

1.  Verify that the app information such as the signature certificate matches that on HUAWEI Developers.
2.  Disconnect and then reconnect the device.
3.  [Configure clientId](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/configuration_client_id) in the **metadata** field.
4.  [Submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/). Huawei technical support will get back to you as soon as possible.
