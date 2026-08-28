# TrustedAppService

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/nPvuwFJPR624sSH0SvGt9A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062334Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=47E31A11AF07B57F4EBC17210EB7D9DCE9EEFC489D3E3B9EDC69CA2ED4A331BB)

This section describes only module-specific client error codes and provides the cause analysis. If the error persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/). Huawei will get back to you as soon as possible.

#### 201 Permission Verification Failed

**Description**

Permission verification failed.

**Possible causes**

1.  The app has not enabled TrustedAppService.
2.  The app does not have the required permissions.

**Solution**

1.  Enable TrustedAppService. For details, please refer to [Enabling Device Security Kit](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/devicesecurity-deviceverify-activateservice).
2.  Apply for location permissions. For details, please refer to [Development Procedure](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/devicesecurity-taas-securelocation#section9187179113620) for location security verification in the development guide.

#### 401 Parameter Check Failed

**Description**

Parameter check failed.

**Possible causes**

1.  The passed value is not an enumerated value provided by the kit.
2.  The **userData** length is invalid.

**Solution**

1.  Pass an enumerated value provided by the kit.
2.  Change the value of **userData** to make sure the length is between 16 and 127 bytes.

#### 1011500001 Invalid Algorithm Parameter

**Description**

The key parameter is not supported.

**Possible causes**

The passed attestation key algorithm or key length is not supported.

**Solution**

Pass an enumerated algorithm and key length provided by the kit.

#### 1011500002 Some Parameters Are Missing

**Description**

Some parameters are missing.

**Possible causes**

Not all parameters required by the API are passed.

**Solution**

Pass all the mandatory parameters by referring to the API description.

#### 1011500003 Key Generation Failed

**Description**

Failed to generate the key.

**Possible causes**

The device is not connected to the network.

**Solution**

Connect the device to the network.

#### 1011500004 Certificate Creation Failed

**Description**

Failed to create the certificate file.

**Possible causes**

The certificate file storage path conflicts with another file.

**Solution**

Change the storage path or name of the file that causes the conflict.

#### 1011500005 File Operation Failed

**Description**

The key file operation failed.

**Possible causes**

The file system operation failed.

**Solution**

Send the request again. If the error persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/) for assistance.

#### 1011500006 IPC Failed

**Description**

IPC failed.

**Possible causes**

The SA of TrustedAppService is not started.

**Solution**

Send the request again. If the error persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/) for assistance.

#### 1011500007 The Key Does Not Exist

**Description**

The key does not exist.

**Possible causes**

The attestation key is not created before the attestation session is initialized.

**Solution**

Create an attestation key before initializing the attestation session. For details, please refer to [Enabling Device Security Kit](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/devicesecurity-deviceverify-activateservice).

#### 1011500008 Certificate Verification Failed

**Description**

Certificate verification failed.

**Possible causes**

The certificate file is damaged.

**Solution**

Destroy the attestation key, re-create it, and then initialize the attestation session.

#### 1011500009 Certificate Has Expired

**Description**

The certificate has expired.

**Possible causes**

The certificate is out of the validity period.

**Solution**

Destroy the attestation key, re-create it, and then initialize the attestation session.

#### 1011500010 Unmatching Key

**Description**

The key does not match.

**Possible causes**

The certificate and key do not match.

**Solution**

Destroy the attestation key, re-create it, and then initialize the attestation session.

#### 1011500011 Failed to Initialize the Camera in Secure Mode

**Description**

Failed to initialize the camera in secure mode.

**Possible causes**

The device serial number passed for initializing the attestation session is invalid.

**Solution**

Re-obtain the camera serial number. For details, please refer to [Camera Kit Development Guide](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/camera-kit).

#### 1011500012 Attestation Session Context Is Abnormal

**Description**

The attestation session is abnormal.

**Possible causes**

The attestation session is ended in the process of obtaining the data to verify location security or during secure image compression and cropping.

**Solution**

Re-initialize the attestation session, and then obtain the data to verify location security or compress and crop the secure image.

#### 1011500013 Key Has Expired

**Description**

The key has expired.

**Possible causes**

The key is out of the validity period.

**Solution**

Destroy the attestation key, re-create it, and then initialize the attestation session.

#### 1011500014 Location Service Unavailable

**Description**

The location service is not available.

**Possible causes**

The location service is faulty.

**Solution**

Send the request again. If the error persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/) for assistance.

#### 1011500015 Location Service Is Disabled

**Description**

The location service is disabled.

**Possible causes**

The location service is disabled on the device.

**Solution**

Enable the location service in **Control Center**.

#### 1011500016 Failed to Obtain Location Information

**Description**

Failed to obtain the location information.

**Possible causes**

1.  GPS signals cannot be obtained.
2.  The sensor is faulty.

**Solution**

Send the request again. If the error persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/) for assistance.

#### 1011500017 Signature Verification Failed

**Description**

Signature verification failed.

**Possible causes**

The signature file is damaged.

**Solution**

Obtain the secure image data or secure geographical location data again, and initiate a new processing request.

#### 1011500018 Failed to Process the Secure Image

**Description**

Failed to process the secure image.

**Possible causes**

The image data of the secure image is damaged.

**Solution**

Send the request again. If the error persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/) for assistance.
