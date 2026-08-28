# UI Context Error Codes

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/gfmkqT0hQam5slmIr1fq1w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062311Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=67D1DFA7BB531BB9EF344F7CFD810B76E24E9C3AF14811E85CDC851F76A48C2E)

This topic describes only module-specific error codes. For details about universal error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

#### 190001 Invalid UIContext Object

**Error Message**

The uiContext is invalid.

**Description**

This error code is reported when an invalid UIContext object is detected.

**Possible Causes**

The provided UIContext object is invalid.

**Solution**

Provide a valid UIContext object.

#### 190002 Invalid Callback Function

**Error Message**

The callback function is invalid.

**Description**

This error code is reported when an invalid callback function is detected.

**Possible Causes**

The type of callback function is incorrect.

**Solution**

Pass a callback function of the correct type.

#### 100101 Invalid Negative Parameter Value

**Error Message**

The parameter value cannot be less than 0.

**Description**

This error code is reported when the provided parameter value falls below the minimum allowed threshold of 0.

**Possible Causes**

An invalid negative parameter value is provided.

**Solution**

Ensure all parameter values meet minimum value requirements.

#### 100102 Incorrect Parameter Type

**Error Message**

The parameter value cannot be a floating-point number.

**Description**

This error code is reported when the API expects integer values but receives floating-point input.

**Possible Causes**

An integer is required, but a floating-point value is passed.

**Solution**

Pass integers as required.

#### 100103 Invalid Thread Context

**Error Message**

The function cannot be called from a non-main thread.

**Description**

This error code is reported when the function is incorrectly called from a non-main thread.

**Possible Causes**

The function must be called from the main thread.

**Solution**

Call the function from the main thread.
