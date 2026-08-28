# Passkeys

#### 801 Device Type Error

**Message**

Device type error.

**Description**

This error code is reported when the device type does not support Online Authentication Kit.

**Possible causes**

The device type is emulator.

**Solution**

Use a device of a supported type.

#### 1021300001 Not Supported by the System

**Message**

The system does not support.

**Description**

This error code is reported when the system does not support the current operation.

**Possible causes**

Parameters related to registration or authentication are incorrect. For example, the authenticator does not support the specified signature algorithm.

**Solution**

Verify that the registration and authentication parameters are correctly set.

#### 1021300002 Invalid State

**Message**

Invalid state.

**Description**

This error code is reported when the authenticator is in an invalid state.

**Possible causes**

The authenticator status is abnormal. For example, after the user consents to register a credential, it is found that the credential ID is listed in **excludeCredentials**, which usually indicates that the device has already been registered.

**Solution**

Check the authenticator status and use the authenticator correctly.

#### 1021300003 System Integrity Check Failed

**Message**

System integrity check failed.

**Description**

This error code is reported when there is a security issue during access.

**Possible causes**

A security issue exists, such as the web page URL not using HTTPS or other conditions that fail to meet security requirements.

**Solution**

Use settings that meet security requirements.

#### 1021300004 Canceled by the User

**Message**

User abort.

**Description**

This error code is reported when the user cancels an operation.

**Possible causes**

The user taps the cancel button.

**Solution**

Try again to use the function.

#### 1021300005 Timeout

**Message**

Time out.

**Description**

This error code is reported when the access times out.

**Possible causes**

The access times out.

**Solution**

Complete the operation within the configured time period.

#### 1021300006 Encoding Error

**Message**

Encoding error.

**Description**

This error code is reported when an encoding error occurs.

**Possible causes**

The registration or authentication parameters are incorrect.

**Solution**

Verify that the registration or authentication parameters are correct.

#### 1021300007 Unknown Error

**Message**

Unknown error.

**Description**

This error code is reported when an unknown error occurs.

**Possible causes**

An unknown error occurs.

**Solution**

If this issue occurs repeatedly, you can [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/) to contact Huawei technical support.

#### 1021300008 Incorrect Constraint Condition

**Message**

The constraint condition is incorrect.

**Description**

This error code is reported when a constraint condition is incorrect.

**Possible causes**

The constraint condition is incorrect. For example, **residentKey** is required, but the authenticator does not support it.

**Solution**

Verify that the registration or authentication parameters are correct.

#### 1021300009 Data Error

**Message**

Data error.

**Description**

This error code is reported when a data error occurs.

**Possible causes**

A data error occurs.

**Solution**

Verify that the registration or authentication parameters are correct.

#### 1021300010 Rejected by the User

**Message**

User Rejects.

**Description**

This error code is reported when the user rejects an operation.

**Possible causes**

The user rejects the operation.

**Solution**

Prompt the user to set a related platform authenticator (face, fingerprint, or PIN) first.

#### 1021300011 Failed to Start the System FIDO Service

**Message**

Failed to connect to the service.

**Description**

This error code is reported when the FIDO system capability fails to be started.

**Possible causes**

The FIDO system capability fails to be started.

**Solution**

Restart the phone or try again.

#### 1021300012 Number of Passkeys Reaches the Maximum

**Message**

The number of credentials has reached the maximum limit.

**Description**

This error code is reported when the number of passkeys reaches the maximum.

**Possible causes**

The number of passkeys reaches the maximum.

**Solution**

Prompt the user to delete unnecessary passkeys from the password vault. The system supports a maximum of 500 passkeys, and each app can store up to 20 passkeys.

#### 1021310001 Invalid CTAP Command

**Message**

Invalid CTAP command.

**Description**

This error code is reported when the CTAP command is invalid.

**Possible causes**

The CTAP command is invalid or not supported.

**Solution**

Use a correct CTAP command by referring to the FIDO2 specifications.

#### 1021310002 Invalid Parameters

**Message**

The command contains invalid parameters.

**Description**

This error code is reported when a command contains invalid parameters.

**Possible causes**

The command contains invalid parameters.

**Solution**

Add necessary extended data.

#### 1021310003 Invalid Message Length

**Message**

Invalid message or attribute length.

**Description**

This error code is reported when the message length is invalid.

**Possible causes**

The data transmission length is incorrect.

**Solution**

Use a message with a correct length.

#### 1021310004 Invalid CBOR

**Message**

Invalid CBOR or unpredictable error.

**Description**

This error code is reported when the Concise Binary Object Representation (CBOR) is invalid or an unpredictable error occurs.

**Possible causes**

The CBOR is invalid or an unpredictable error occurs.

**Solution**

Verify that the input parameters are correct.

#### 1021310005 CBOR Parsing Failed

**Message**

Failed to parse the CBOR.

**Description**

This error code is reported when the CBOR fails to be parsed.

**Possible causes**

An error occurs during CBOR parsing.

**Solution**

Verify that the input parameters are correct.

#### 1021310006 Credential Not Found

**Message**

Not found valid credentials.

**Description**

This error code is reported when no valid credential is found.

**Possible causes**

No credential is available for the user.

**Solution**

[Register a passkey](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/onlineauthentication-passkey-intro#section20979171074710) for the user on the current device.

#### 1021310007 Operation Not Allowed

**Message**

Not allowed.

**Description**

This error code is reported when a command is not allowed.

**Possible causes**

The authenticator does not support operations without user verification.

**Solution**

Verify that the input parameters are correct.

#### 1021310008 User Verification Failed

**Message**

User verification failed.

**Description**

This error code is reported when the user verification fails.

**Possible causes**

The user verification fails.

**Solution**

Verify the fingerprint or face again as prompted.

#### 1021310009 Other Errors

**Message**

Other error.

**Description**

This error code is reported when the key generation or signature fails or when an internal error occurs.

**Possible causes**

The key generation or signature fails or an internal error occurs.

**Solution**

If this issue occurs repeatedly, you can [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/) to contact Huawei technical support.
