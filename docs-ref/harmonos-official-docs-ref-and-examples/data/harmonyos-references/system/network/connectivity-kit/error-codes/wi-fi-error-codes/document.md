# Wi-Fi Error Codes

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f/v3/sLE9ZyYwSJq13CmF0HAI2w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0EFD62250C5406A8ED597A27C57D6CAAC9253D9532D5A1FB8F7BE249B4C158A9)

This topic describes only module-specific error codes. For details about universal error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

#### 2401000 STA Internal Error

**Error Message**

Operation failed.

**Description**

An error occurs when the Wi-Fi service performs an operation related to the station (STA).

**Possible Causes**

1.  Communication between the Wi-Fi service and the STA failed.
2.  The Wi-Fi chip communication is abnormal.
3.  An unknown error has occurred.

**Solution**

1.  Disable and then enable the Wi-Fi function again.
2.  If the error persists, restart the device.

#### 2501000 STA Internal Error

**Error Message**

Operation failed.

**Description**

An error occurs when the Wi-Fi service performs an operation related to the station (STA).

**Possible Causes**

1.  Communication between the Wi-Fi service and the STA failed.
2.  The Wi-Fi chip communication is abnormal.
3.  An unknown error has occurred.

**Solution**

1.  Disable and then enable the Wi-Fi function again.
2.  If the error persists, restart the device.

#### 2501001 STA Disabled

**Error Message**

Wi-Fi STA disabled.

**Description**

The Wi-Fi STA function is disabled.

**Possible Causes**

The Wi-Fi function is disabled.

**Solution**

Enable the Wi-Fi function.

#### 2501005 No User Response to the Connection Request

**Error Message**

The user does not respond.

**Description**

When an application connects to a candidate network, the application prompts the user whether to trust and establish the connection. The user does not respond to the connection request.

**Possible Causes**

1.  The user swipes up to close the dialog box.
2.  The user does not click **OK** or **Cancel** within 10 seconds.

**Solution**

The user needs to agree to the request for connecting to the candidate network.

#### 2501006 Connection Request Rejected

**Error Message**

The user refused the action.

**Description**

When an application connects to a candidate network, the application prompts the user whether to trust and establish the connection. The user cancels the connection request.

**Possible Causes**

The user clicks **Cancel** to reject the connection.

**Solution**

The user needs to agree to the request for connecting to the candidate network.

#### 2501007 Parameter Verification Failed

**Error Message**

Parameter validation failed.

**Description**

An error occurs during parameter verification.

**Possible Causes**

The parameter value range is incorrect.

**Solution**

Rectify the fault according to the parameter restrictions of the API.

#### 2601000 Hotspot Module Error

**Error Message**

Operation failed.

**Description**

An error occurs when the Wi-Fi service performs a hotspot-related operation.

**Possible Causes**

1.  Communication between the Wi-Fi service and the STA failed.
2.  The Wi-Fi chip communication is abnormal.
3.  An unknown error has occurred.

**Solution**

1.  Disable and then enable the hotspot again.
2.  If the error persists, restart the device.

#### 2701000 AP Extension Module Error

**Error Message**

Operation failed.

**Description**

An error occurs when the Wi-Fi service performs a hotspot-related operation.

**Possible Causes**

1.  Communication between the Wi-Fi service and the STA failed.
2.  The Wi-Fi chip communication is abnormal.
3.  An unknown error has occurred.

**Solution**

1.  Disable and then enable the hotspot again.
2.  If the error persists, restart the device.

#### 2801000 P2P Module Error

**Error Message**

Operation failed.

**Description**

An error occurs when the Wi-Fi service performs a P2P-related operation.

**Possible Causes**

1.  Communication between the Wi-Fi service and the STA failed.
2.  The Wi-Fi chip communication is abnormal.
3.  An unknown error has occurred.

**Solution**

1.  Disable and then enable the Wi-Fi function again.
2.  If the error persists, restart the device.

#### 2501003 Failed to Open the Service

**Error Message**

Operation failed because the service is being closed.

**Description**

The operation for opening the service failed because the service is being closed.

**Possible Causes**

The service is being closed.

**Solution**

Open the service again later.

#### 2501004 Failed to Close the Service

**Error Message**

Operation failed because the service is being opened.

**Description**

The operation for closing the service failed because the service is being opened.

**Possible Causes**

The service is being opened.

**Solution**

Close the service again later.
