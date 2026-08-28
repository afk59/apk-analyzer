# ArkTS API Result Codes

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/fKNgmWjPTP6HRjtxyfmSmA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062353Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=095184E7AC98F4FE9869D2514FE3EA801026AFF93DB39BA5C6D29CD9C16B0688)

This section describes only module-specific result codes. For details about universal error codes, please refer to [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

#### 1001202001 Process Canceled on the Remote Device

**Message**

Canceled on the remote device.

**Description**

The calling of a Device Interconnectivity API is canceled by the callee.

**Possible cause**

The calling is canceled by the remote device after the app on the remote device is started.

**Solution**

Perform function tests based on the correct process of using Device Interconnectivity.

#### 1001202002 Internal Error in the Collaboration Framework

**Message**

An internal error occurs in the collaboration framework.

**Description**

The calling of a Device Interconnectivity API is canceled by the callee.

**Possible cause**

The calling is canceled after the app on the remote device is started.

**Solution**

[Submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/). Huawei will get back to you as soon as possible.

#### 1001202003 Process Canceled on the Local Device

**Message**

Canceled on the local device.

**Description**

The calling of a Device Interconnectivity API is canceled by the caller.

**Possible cause**

The calling is canceled by the local device after the app on the remote device is started.

**Solution**

Perform function tests based on the correct process of using Device Interconnectivity.

#### 1001202004 Capability of Device Interconnectivity Started

**Message**

The capability of Device Interconnectivity is started.

**Description**

The capability of Device Interconnectivity is started.

**Possible cause**

The capability of Device Interconnectivity is started.

**Solution**

This is a normal status code, and no operation is required.

#### 1001202005 All Images Have Been Sent Back

**Message**

All images have been sent back.

**Description**

All images have been sent back.

**Possible cause**

All images have been sent back.

**Solution**

This is a normal status code, indicating that all images have been sent back.

#### 1001202006 Returned File Name

**Message**

Returned file name.

**Description**

Returned file name.

**Possible cause**

The returned information is a file name.

**Solution**

This is a normal status code, indicating that the returned information is a file name.

#### 1001202007 Passed Custom Image Number Is Less Than or Equal to 0

**Message**

The passed custom image number is less than or equal to 0.

**Description**

The passed custom image number is less than or equal to 0.

**Possible cause**

The value of **canReceiveNumber** passed using [createCollaborationServiceMenuItems](../collaborationservice-device-interconnectivity-component/document.md#section149271552154711) is less than or equal to 0.

**Solution**

When using [createCollaborationServiceMenuItems](../collaborationservice-device-interconnectivity-component/document.md#section149271552154711), set **canReceiveNumber** to a value ranging from 1 to 50.
