# Settings Error Codes

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/6nF_ZSyQRE2ZohkeLBvZ1Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062401Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=02626473358124B59D94222B64D7FE78491866A6A2EE14A31E04296B3865C449)

This topic describes only module-specific error codes. For details about universal error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

#### 14800000 Parameter Check Failed

**Error Message**

Parameter error. Possible causes: 1. Parameter verification failed.

**Description**

1.  This error code is reported when the null parameter is incorrect.
    
2.  This error code is reported when the parameter parsing fails.
    

**Possible Causes**

1.  A null parameter is incorrect (Null Argument Error).
    
2.  A value range is incorrect (Value Range Error).
    

**Solution**

Make sure all the mandatory parameters are passed. If parameter verification fails, read the parameter specifications and locate the fault based on the possible causes.

#### 14800010 UIAbility Required

**Error Message**

Original service error.

**Description**

This error code is reported when the original service throws an error.

**Possible Causes**

The current context is not the UIAbility.

**Solution**

Perform the operation on UIAbility.
