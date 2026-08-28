# Extended Authentication Error Codes

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/Xjfr2o6-SQOeBtkpwdaJkQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062349Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=988807B18848E92F96C538501F302A0105D5F6A85333D6F5D84EC67FF0349AFE)

This topic describes only module-specific error codes. For details about universal error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

#### 33200001 Invalid netId

**Error Message**

Invalid netId.

**Description**

This error code is reported if **netId** is invalid.

**Possible causes**

The specified **netId** does not exist.

**Solution**

Enter a valid **netId**.

#### 33200002 Failed to Exit Extended Authentication of the Specified NIC

**Error Message**

log off fail.

**Description**

This error code is reported if the attempt to exit extended authentication of the NIC identified by the specified **netId** fails.

**Possible causes**

The specified **netId** does not exist.

**Solution**

Enter a valid **netId**.

#### 33200003 Invalid eth eap Configuration

**Error Message**

Invalid profile.

**Description**

This error code is reported if the **eth eap** configuration in **profile** is invalid.

**Possible causes**

The **profile** field value is incorrect.

**Solution**

Configure the **profile** field correctly.

#### 33200004 Invalid eap Result Value

**Error Message**

Invalid result.

**Description**

This error code is reported if the **result** value is invalid.

**Possible causes**

The input **result** value is not within the range of **CustomResult**.

**Solution**

Set **result** to a value within the range of **CustomResult**.

#### 33200005 Invalid Data Length

**Error Message**

Invalid size of eap data.

**Description**

This error code is reported if the EAP data length is invalid.

**Possible causes**

The input EAP data length is different from the value of **bufferLen** in **EapData**.

**Solution**

Ensure that the value of **bufferLen** is the same as the EAP data length.

#### 33200006 Invalid Network Type

**Error Message**

Invalid net type.

**Description**

This error code is reported if the network type is invalid.

**Possible causes**

The input network type is not supported.

**Solution**

Set the input network type to **1** (WLAN) or **2** (ETH).

#### 33200007 Invalid eapCode Value

**Error Message**

Invalid eap code.

**Description**

This error code is reported if **eapCode** is invalid.

**Possible causes**

The input **eapCode** is not within the valid value range.

**Solution**

Enter a valid **eapCode** value, which can be **1**, **2**, **3**, or **4**.

#### 33200008 Invalid eapType Value

**Error Message**

Invalid eap type.

**Description**

This error code is reported if **eapType** is invalid.

**Possible causes**

The input **eapCode** is not within the valid value range.

**Solution**

Set **eapType** to a value within the range of \[1, 255\].

#### 33200009 netmanager Not Exist

**Error Message**

netmanager stop.

**Description**

The netmanager process does not exist.

**Possible causes**

This error code is reported if the netmanager process is abnormal.

**Solution**

Reboot the system.

#### 33200010 Invalid eap Status

**Error Message**

Invalid eth state.

**Description**

This error code is reported if the eth status is invalid.

**Possible causes**

The Ethernet adapter is not working properly.

**Solution**

Remove and insert the network cable and try again.

#### 33200099 Internal Program Error

**Error Message**

internal error.

**Description**

This error code is reported if a program fails to operate properly.

**Possible causes**

The program encounters an internal error.

**Solution**

Reboot the system.
