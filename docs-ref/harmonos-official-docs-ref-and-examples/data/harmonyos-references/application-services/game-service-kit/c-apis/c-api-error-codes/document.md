# C API Error Codes

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/o2SlL_tlSDSHyqHwNYeDiA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062507Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BE1D4AC78B07634C523B1F11814DFCBE544D8A7395A42CD09F11D3EEB1233BB1)

This section describes only the error codes related to Game Service Kit. For details about universal error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

#### 1010300001 Internal System Error

**Message**

System internal error.

**Description**

Internal system error.

**Possible causes**

An internal error occurs in the Game Service Kit system.

**Solution**

[Submit a ticket online](<https://developer.huawei.com/consumer/en/support/feedback/#/add/101704353566310877?level2=101704353626565886&amp;level3=101704354579010004&amp;keyWord=Game Service Kit>). Huawei technical support will handle the problem in time.

#### 1010300002 Authentication Failure

**Message**

Invalid caller.

**Description**

Authentication failure.

**Possible causes**

The network connection is abnormal, or a passed parameter is incorrect.

**Solution**

1.  For the first sign-in on a device, check whether the network is properly connected.
2.  Check whether the parameters passed to the [HMS\_GamePerformance\_Init](../modules/gameperformance/document.md#ga1045d9d8f4e7972b44ff95571afca8f9) API are correct.

#### 1010300003 Invalid Request

**Message**

Invalid request.

**Description**

Invalid request.

**Possible causes**

Other APIs are called when the initialization is not performed or fails.

**Solution**

Call the [HMS\_GamePerformance\_Init](../modules/gameperformance/document.md#ga1045d9d8f4e7972b44ff95571afca8f9) API first and ensure that the API is successfully called.

#### 1010300004 Invalid Parameter

**Message**

Parameter error.

**Description**

Invalid parameter.

**Possible causes**

-   A mandatory parameter was left empty.
-   Parameter verification failed.

**Solution**

Ensure that all mandatory parameters are passed and that the input parameters conform to the specifications.
