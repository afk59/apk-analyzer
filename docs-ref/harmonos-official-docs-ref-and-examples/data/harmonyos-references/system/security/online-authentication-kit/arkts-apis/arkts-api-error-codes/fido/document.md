# FIDO

#### 401 Input Parameter Error

**Message**

Parameter error.

**Description**

This error code is reported when the input parameter does not meet the requirements.

**Possible causes**

The input parameter does not meet the requirements.

**Solution**

Check the input parameter based on the API definition.

#### 801 Device Type Error

**Message**

Device type error.

**Description**

This error code is reported when the device type does not support Online Authentication Kit.

**Possible causes**

The device type is emulator.

**Solution**

Use a device of a supported type.

#### 1005900003 Operation Canceled by User

**Message**

User cancels.

**Description**

This error code is reported when a user cancels an operation.

**Possible causes**

A user taps the close button during biometric feature authentication.

**Solution**

Initiate the authentication again.

#### 1005900005 No Authenticator Available

**Message**

No authenticator matching the authenticator policy specified is available.

**Description**

This error code is reported when there is no authenticator available.

**Possible causes**

1\. **checkPolicy**: User data exists on the server but does not exist on the client, for example, because the user data has been deleted after FIDO authentication is enabled.

2\. **processUAFOperation**:

Enabling: FIDO authentication has been enabled for a user, but FIDO authentication is to be enabled for the user again.

Authentication: Authentication is performed on a user for whom FIDO authentication is not enabled.

**Solution**

1\. **checkPolicy**: Re-enable FIDO authentication.

2\. **processUAFOperation**:

Enabling: FIDO authentication does not need to be enabled again. Perform authentication directly.

Authentication: Enable FIDO authentication for the user and then perform authentication. For details, please refer to [Use Cases](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/onlineauthentication-fido#section2960852143012).

#### 1005900006 Protocol Error

**Message**

A violation of the UAF protocol occurred.

**Description**

This error code is reported when there is a UAF protocol error.

**Possible causes**

The message format or data is incorrect.

**Solution**

Ensure that the passed message is correct.

#### 1005900007 Facet ID Does Not Match

**Message**

No Facet\_ID is registered.

**Description**

This error code is reported when the facet ID does not match.

**Possible causes**

The facet ID calculated by the client is different from that configured on the FIDO server. (The facet ID is the signature value in the certificate for packaging your app. Obtain it in advance and then configure it on the FIDO server.)

**Solution**

Check whether the facet ID configured on the server is correct. The format of a facet ID for HarmonyOS is ohos:app-id:<_App signature value_\>.

The app signature value can be obtained through the [getBundleInfoForSelf](../../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-bundle-bundlemanager-bundle-management-module/document.md#bundlemanagergetbundleinfoforself) API. Set [BundleFlag](../../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-bundle-bundlemanager-bundle-management-module/document.md#bundleflag) to **GET\_BUNDLE\_INFO\_WITH\_SIGNATURE\_INFO**, obtain the **appId** parameter in **signatureInfo**, and delete the package name prefix and all equal signs (=) at the end of the **appId** parameter value.

Example:

1\. Obtain **appId** through the [getBundleInfoForSelf](../../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-bundle-bundlemanager-bundle-management-module/document.md#bundlemanagergetbundleinfoforself) API.

"com.huawei.hmos.test\_6ea5b1b7d51b857cb46d570eb79f7b1c8936a18c5f9bd6b9592ccc75e3406863=="

2\. Delete the package name prefix and all equal signs (=) at the end. The remaining part is the signature value.

"6ea5b1b7d51b857cb4d50e79f7b1c8936a18c5f9bd6b9592ccc75e3406863"

3\. Obtain the facet ID by adding a prefix **ohos:app-id:**.

"ohos:app-id:6ea5b1b7d51b857cb46d570eb79f7b1c8936a18c5f9bd6b9592ccc75e3406863"

#### 1005900009 Current Request Denied

**Message**

The authenticator denies access to the generated request.

**Description**

This error code is reported when the authenticator denies a request.

**Possible causes**

The **KHAccessToken** value obtained after **KeyHandle** read from the database is decrypted during authentication does not match the dynamically calculated **KHAccessToken** value.

**Solution**

Disable the current FIDO fingerprint/facial authentication and enable it again.

#### 1005900014 No Biometric Feature Information Recorded for Users

**Message**

The user does not record biometric features or the authentication module is abnormal.

**Description**

This error code is reported when a user's biometric features are not recorded or the authentication module is abnormal.

**Possible causes**

The user's biometric features are not recorded.

**Solution**

1.  Check whether the mobile device has registered biometric feature information.
2.  Enter the biometric feature information in settings.

#### 1005900015 System Interruption

**Message**

System Interruption.

**Description**

This error code is reported when the system is interrupted.

**Possible causes**

The running environment is abnormal.

**Solution**

Restart the mobile device.

#### 1005900016 Unknown Error

**Message**

Unknown error.

**Description**

This error code is reported when an unknown error occurs.

**Possible causes**

An unknown error occurs in the FIDO service.

**Solution**

1.  Try again.
2.  Restart the device and try again.

#### 1005900017 Switching to the Custom Authentication Mode

**Message**

Switched to the custom authentication process.

**Description**

This error code is reported when the user cancels the current authentication upon UAF authentication failure in the scenario where the button text for switching to another authentication mode is passed.

**Possible causes**

The user cancels the current authentication upon UAF authentication failure.

**Solution**

Initiate UAF authentication again or start the custom authentication mode.
