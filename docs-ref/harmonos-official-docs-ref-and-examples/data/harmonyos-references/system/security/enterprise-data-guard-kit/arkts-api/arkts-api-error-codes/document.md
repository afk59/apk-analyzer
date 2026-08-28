# ArkTS API Error Codes

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/T249UTxvTVyngHUvsQIfnQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062335Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=00A37339A96584AE7B7D1CDD36D32E3C6BC5D859065A3E66B498BC9668CE8189)

This section describes only module-specific error codes. For details, please refer to [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md). If the error persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/). Huawei will get back to you as soon as possible.

#### 1014400001 System Internal Error

**Message**

System service exception.

**Description**

Internal system error.

**Possible causes**

The system is in an insecure state, or there is a hardware failure.

**Solution**

Try again or [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

#### 1014400103 User Authentication Failure

**Message**

Authentication is failed.

**Description**

User authentication failed.

**Possible causes**

The lock screen password is incorrect.

**Solution**

Prompt the user to enter the correct lock screen password.

#### 1014400201 Invalid Device Type

**Message**

Invalid device type, current device is not enterprise device.

**Description**

The current device is not an enterprise device.

**Possible causes**

The current device is not an enterprise device.

**Solution**

Check whether the device is an enterprise device. For details, please refer to [MDM Kit development guide](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/mdm-kit-guide).

#### 1014400202 Invalid userId

**Message**

Invalid userId.

**Description**

Invalid userId.

**Possible causes**

Invalid enterprise user ID.

**Solution**

Check whether the enterprise user ID is valid.

#### 1014400203 Enterprise Recovery Key Already Exists

**Message**

Enterprise recovery key is already existed.

**Description**

The enterprise recovery key already exists.

**Possible causes**

The enterprise recovery key has been obtained and cannot be obtained again.

**Solution**

Call the [getAuthChallenge](../recoverykey-enterprise-recovery-key/document.md#en-us_topic_0000001983615174_section41041418113717) API to obtain a challenge and sign it. Then call the [deleteEnterpriseRecoveryKey](../recoverykey-enterprise-recovery-key/document.md#en-us_topic_0000001983615174_section1927015514386) API to delete the enterprise recovery key.

#### 1014400204 Signature Verification Failure

**Message**

Invalid signature.

**Description**

Failed to verify the signature of the challenge.

**Possible causes**

1.  The same challenge is used to initiate two requests.
2.  The API request timed out.
3.  An incorrect enterprise private key is used for signing.

**Solution**

1.  Call the [getAuthChallenge](../recoverykey-enterprise-recovery-key/document.md#en-us_topic_0000001983615174_section41041418113717) API to obtain a new challenge and [sign it](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/recoverykey-signature).
2.  Ensure that the enterprise private key is correct.

#### 1014400205 Certificate Verification Failure

**Message**

Invalid cert.

**Description**

Invalid certificate.

**Possible causes**

1.  Invalid certificate format.
2.  The format of the public key in the certificate is incorrect.

**Solution**

1.  Ensure that the certificate is in PEM format.
2.  Ensure that the public key in the certificate is an ECC public key.
3.  Ensure that the certificate carries a valid signature from the enterprise root certificate.

#### 1001700103 Target File Does Not Exist

**Message**

The path is not exist.

**Description**

The file for which tags need to set does not exist.

**Possible causes**

The file for which tags need to set does not exist.

**Solution**

Check whether the file corresponding to the [default path range](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/dataguard-introduction#li1475101851010) exists.

#### 1001700104 Tag List Check Failure

**Message**

The tag list check failed.

**Description**

Failed to check the tag list.

**Possible causes**

1.  A tag in the tag list contains a semicolon (;).
2.  The length of a single tag in the list exceeds 255 characters.
3.  The number of tags exceeds 5.

**Solution**

1.  Ensure that no tag in the tag list contains semicolons (;).
2.  Ensure that the length of each tag in the list does not exceed 255 characters.
3.  Ensure that the number of tags does not exceed 5.
