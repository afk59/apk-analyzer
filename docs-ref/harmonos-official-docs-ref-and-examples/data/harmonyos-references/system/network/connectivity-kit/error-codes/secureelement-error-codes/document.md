# SecureElement Error Codes

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/SmnBRi0pRq-t0COSPLQD-g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1BB0877695B2A383C0372E6C0FD89254E6308FB2FD7424970D68D3CF27582DF4)

This topic describes only module-specific error codes. For details about universal error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

#### 3300101 Abnormal SE Service Status

**Error Message**

IllegalStateError, an attempt is made to use an SE session that has been closed.

**Description**

The SecureElement (SE) service is abnormal.

**Possible Causes**

1.  The SE service is disconnected.

**Solution**

1.  Close the SE service.
2.  Set up a connection with the SE service again.

#### 3300102 Failed to Find the Desired SE

**Error Message**

NoSuchElementError, the AID on the SE is not available or cannot be selected.

**Description**

The desired SE is not found.

**Possible Causes**

1.  The **aid** value of the parameter is incorrect.
2.  The SE channel is occupied.

**Solution**

1.  Enter a correct **aid** value.
2.  Close the SE channel and then re-establish a connection.
3.  Restart the device and try again.

#### 3300103 Failed to Obtain the Access Rule

**Error Message**

SecurityError, the calling application cannot be granted access to this AID or the default applet on this session.

**Description**

The access rule cannot be obtained.

**Possible Causes**

1.  There is no access rule for the application on the SE.

**Solution**

1.  Write correct access rules to the SE.
2.  Close the SE service and set up a connection with the SE service again.

#### 3300104 SE Chip I/O Exception

**Error Message**

IOError, there is a communication problem to the reader or the SE.

**Description**

The I/O of the SE chip is abnormal.

**Possible Causes**

1.  The communication with the SE chip is abnormal.
2.  The SE chip is abnormal.

**Solution**

1.  Close the SE service and set up a connection with the SE service again.
2.  Restart the device.
