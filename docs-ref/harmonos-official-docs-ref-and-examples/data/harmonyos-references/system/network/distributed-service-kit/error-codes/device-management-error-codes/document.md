# Device Management Error Codes

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/f-p_bzC_S06lcXhUiNTWAA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062344Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FCBD71CBEF6CE81D376460F21606AE4F24F512D930223583FBD645EBB3547686)

This topic describes only module-specific error codes. For details about universal error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

#### 11600101 Service Invoking Exception

**Error Message**

Failed to execute the function.

**Description**

This error code is reported if a service fails to be invoked due to an internal error.

**Possible Causes**

An error occurred during internal invocation.

**Solution**

Call the API again.

#### 11600102 Failed to Obtain the Service

**Error Message**

Failed to obtain the service.

**Description**

This error code is reported if the service fails to start, resulting in a service access failure.

**Possible Causes**

The service is not started or fails to start.

**Solution**

Make sure the service is started and obtain the service again.

#### 11600103 Authentication Unavailable

**Error Message**

Authentication unavailable.

**Description**

This error code is reported if the current service call fails because the previous authentication service is still in progress.

**Possible Causes**

The previous authentication service is still in progress.

**Solution**

Wait until the previous authentication service is complete and call the authentication API again.

#### 11600104 Discovery Unavailable

**Error Message**

Discovery unavailable.

**Description**

This error code is reported if the current service call fails because the previous discovery service is still in progress.

**Possible Causes**

The previous discovery service is still in progress.

**Solution**

Wait until the previous discovery service is complete and call the discovery API again.

#### 11600105 Publish Unavailable

**Error Message**

Publish unavailable.

**Description**

This error code is reported if the current service call fails because the previous published service is still in progress.

**Possible Causes**

The previous publish service is still in progress.

**Solution**

Wait until the previous publish service is complete and call the publish API again.

#### 11600106 Failed to Obtain Data from the Cloud

**Error Message**

Failed to get data from the cloud.

**Description**

This error code is reported if the attempt to retrieve data from the cloud fails because the network is abnormal.

**Possible Causes**

The network connection is abnormal, or the network request returns an error.

**Solution**

Ensure that the network connection is normal and call the API again with correct parameters.

#### 11600107 Login Account Required

**Error Message**

A login account is required.

**Description**

This error code is reported if a login account is required for service invocation.

**Possible Causes**

No login account is available on the device.

**Solution**

Use the correct account to log in to the device and call the API again.

#### 11600108 Unlawful Information in Device Name

**Error Message**

The device name contains non-compliant content.

**Description**

This error code is reported if device name contains illegitimate information.

**Possible Causes**

The new device name contains unlawful information.

**Solution**

Ensure that the device name complies with laws and regulations.

#### 32300001 Transport Stream Repeatedly Created

**Error Message**

Only one stream can be created for the current session.

**Description**

This error code is reported if a session for which a transport stream is created already exists.

**Possible Causes**

This error code is reported if a session for which a transport stream is created already has a transport stream.

**Solution**

Ensure that the task of the previous transport stream is complete. Use **destroyStream** to close the transport stream before creating a new one.

#### 32300002 Stream Receive End Not Started

**Error Message**

The stream at the receive end is not started.

**Description**

This error code is reported if the receive end of transport streams is not started.

**Possible Causes**

The receive end is not started.

**Solution**

Start transmission of transport streams after the receive end is started.

#### 32300003 Bit Rate Not Supported

**Error Message**

Bitrate not supported.

**Description**

This error code is reported if the bit rate is not supported.

**Possible Causes**

This error code is reported if the configured bit rate does not match the bit rate supported by the device.

**Solution**

Select an appropriate bit rate based on network conditions and requirements.

#### 32300004 Color Space Not Supported

**Error Message**

Color space not supported.

**Description**

This error code is reported if the color space is not supported.

**Possible Causes**

This error code is reported if the color space output type is set to **OH\_COLORSPACE\_BT2020\_HLG\_LIMIT** but the actual output type is not the specified type.

**Solution**

Ensure that the color space output type is within the supported range.
