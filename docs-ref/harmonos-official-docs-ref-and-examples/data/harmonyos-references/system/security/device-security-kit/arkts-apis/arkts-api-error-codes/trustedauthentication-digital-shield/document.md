# TrustedAuthentication (Digital Shield)

#### 1019100001 Permission Verification Failed

**Description**

Permission verification failed.

**Possible causes**

The HAP has not obtained the digital shield permission in AppGallery Connect.

**Solution**

Only apps that meet the application scenario requirements can apply for this permission. Enable the digital shield service by referring to [Enabling Device Security Kit](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/devicesecurity-deviceverify-activateservice).

#### 1019100002 Parameter Check Failed

**Description**

Parameter check failed.

**Possible causes**

A mandatory parameter is missing, or the parameter type or specifications are invalid.

**Solution**

Make sure all the mandatory parameters are passed and the parameter types and specifications are valid.

#### 1019100003 Number of Consecutive Password Authentication Failures Reaches Upper Limit

**Description**

The number of consecutive password authentication failures reaches the upper limit allowed by the digital shield service.

**Possible causes**

The user forgets the password, or an attacker attempts to crack the password by brute force.

**Solution**

The digital shield is locked. You can provide a reactivation process for the user based on the service scenario.

#### 1019100004 Password Deletion Failure

**Description**

Internal error.

**Possible causes**

An exception occurred when other system APIs are called in the password deletion process.

**Solution**

Try again first. If the retry fails, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/) for assistance.

#### 1019100005 Password Authentication Failure

**Description**

Internal error.

**Possible causes**

An exception occurred when other system APIs are called in the password authentication process.

**Solution**

Try again first. If the retry fails, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/) for assistance.

#### 1019100006 Input Text Check Failure

**Description**

Internal error.

**Possible causes**

The device does not support TUI or the TUI service is faulty.

**Solution**

Check whether the device supports the digital shield capability. If so, try again. If the retry fails, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/) for assistance.

#### 1019100007 Unsupported Image Format

**Description**

The image format is not supported.

**Possible causes**

The input image format does not meet the requirements. The digital shield service APIs require that the image format be RGBA PNG and the image width and height be within 216.

**Solution**

Ensure that the input image meets the format requirements of the digital shield service.

#### 1019100008 Operation Canceled by User

**Description**

The service operation is canceled by the user.

**Possible causes**

The user cancels the operation on the TUI or the TUI automatically exits after 2 minutes of user inactivity.

**Solution**

This is not an error, as the user proactively ends the process.

#### 1019100009 Backup Data Export Failure

**Description**

Failed to export the backup data.

**Possible causes**

The corresponding backup data is not imported, or the password authentication fails during backup data export.

**Solution**

Ensure that the data has been correctly imported and the user password authentication is successful during data export.

#### 1019100010 Backup Data Import Failure

**Description**

Failed to import the backup data.

**Possible causes**

The backup data can be imported only once. If the backup data is imported repeatedly, an error is reported.

**Solution**

Ensure that the data is correctly imported for the first time. When the digital shield service is disabled, the lifecycle of the imported data ends.

#### 1019100011 Invalid TUI Authentication Information

**Description**

Invalid TUI authentication information.

**Possible causes**

The entered authentication information is in an invalid format or exceeds the allowed length.

**Solution**

Ensure that the entered TUI authentication information meets the requirements.

#### 1019100012 Invalid authID

**Description**

Invalid authID.

**Possible causes**

The password authID passed during the operation is different from that obtained when the password is created.

**Solution**

Ensure that the passed authID is the one obtained when the password is created.

#### 1019100013 Password Creation Failure

**Description**

Internal error.

**Possible causes**

An exception occurred when other system APIs are called in the password creation process.

**Solution**

Try again first. If the retry fails, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/) for assistance.

#### 1019100014 Password Change Failure

**Description**

Internal error.

**Possible causes**

An exception occurred when other system APIs are called in the password change process.

**Solution**

Try again first. If the retry fails, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/) for assistance.

#### 1019100015 Biometric Authentication authToken Issuance Failure

**Description**

Internal error.

**Possible causes**

The input **tuiAuthToken** and **bioAuthToken** are from different sessions, or the ATL level of **bioAuthToken** is not **ATL4**.

**Solution**

Check the possible causes. If neither of them applies, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/) for assistance.

#### 1019100016 Digital Shield Service Disabled

**Description**

The digital shield service is not enabled.

**Possible causes**

The device does not support the digital shield service, or the digital shield service fails to be enabled on the device.

**Solution**

Ensure that the device supports the digital shield service.

#### 1019100017 Failed to Obtain the Number of Remaining Authentication Times

**Description**

Failed to obtain the number of remaining authentication times of the digital shield.

**Possible causes**

An exception occurred when other system APIs are called in the process of obtaining the number of remaining authentication times of the digital shield.

**Solution**

Try again first. If the retry fails, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/) for assistance.

#### 1019100018 Failed to Disable the Authentication Capability of a Specified Biometric Feature

**Description**

Failed to disable the authentication capability of a specified biometric feature.

**Possible causes**

An exception occurred when other system APIs are called in the process of disabling the authentication capability of a specified biometric feature.

**Solution**

Try again first. If the retry fails, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/) for assistance.

#### 1019100019 Not Matching the Bound Biometric Feature

**Description**

The authenticated biometric feature does not match the bound biometric feature.

**Possible causes**

The authenticated biometric feature, for example, fingerprint, does not match the bound biometric feature.

**Solution**

Instruct the user to use the bound biometric feature for authentication.

#### 1019100020 Biometric Feature Already Bound

**Description**

The biometric feature is bound repeatedly.

**Possible causes**

The biometric feature is bound repeatedly.

**Solution**

Notify the user that the biometric feature has been bound.

#### 1019100021 Biometric Feature Not Bound

**Description**

The biometric feature is not bound.

**Possible causes**

During biometric authentication or biometric feature unbinding, it is found that the corresponding biometric feature is not bound.

**Solution**

Ensure that the biometric feature has been bound.
