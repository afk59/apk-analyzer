# ArkTS API Error Codes

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/ZOXKuJ1TSZaAFHwCmvRFVA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062328Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6C62202A77070908D6711F9D29DC7FE1731D45E9F5CEC19E86AB8F07441779C0)

This section describes only module-specific error codes. For details about universal error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

#### 401 Parameter Check Failed

**Message**

Parameter error. The value of bundleName is incorrect.

Parameter error. The value of layeredDrawableDescriptor is incorrect.

Parameter error. The value of size is incorrect.

Parameter error. The value of hasBorder is incorrect.

Parameter error. The value of pixelMap is incorrect.

Parameter error. The value of mask is incorrect.

Parameter error. The value of icons is incorrect.

Parameter error. The value of parallelNumber is incorrect.

Parameter error. The number of parameters is incorrect.

Parameter error. The type of ttf resource is error, the type must be resource.

Parameter error. The type of json resource is error, the type must be resource.

Parameter error. The ttf resource is null.

Parameter error. The json resource is null.

Parameter error. Load ttf resource failed.

Parameter error. Load json resource failed.

Parameter error. The ttf resource size is zero.

Parameter error. The json resource size is zero.

Parameter error. The json resource schema is incorrect.

**Description**

This error code is reported when a parameter error occurs. Regardless of whether the API is synchronous or asynchronous, this type of error is generally thrown in synchronous mode.

**Possible causes**

A mandatory parameter is missing, or the parameter type is invalid.

**Solution**

1\. Make sure all the mandatory parameters are passed and the parameter types are valid.

2\. Make sure that the passed resource is not empty.

3\. Make sure that the input JSON format is correct.

#### 801 Device Type Error

**Message**

Device Type error.

**Description**

Incorrect device type.

**Possible causes**

Incorrect device type.

**Solution**

Use a device of a supported type.

#### 1012600001 Previous Concurrent Tasks Still Running

**Message**

Task is busy.

**Description**

Previous concurrent tasks are still running.

**Possible causes**

The previous task is still running.

**Solution**

1\. Check whether [hdsDrawable.getHdsLayeredIcons](../hdsdrawable/document.md#section712131324710) and [hdsDrawable.getHdsIcons](../hdsdrawable/document.md#section12429174135913) are called after the expected result is returned, or directly call the non-batch processing API.

2\. [Submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/). Huawei will get back to you as soon as possible.

#### 1012600002 Resource Quantity Reached Upper Limit

**Message**

Resource size error. The ttf resource out of size.

Resource size error. The json resource out of size.

**Description**

The resource quantity exceeds the upper limit.

**Possible causes**

The quantity of passed resources has reached the upper limit. You can customize up to 10 icons.

**Solution**

Reduce symbol icons and matching animation parameter resources.

#### 1012600003 Resource Parsing Failure

**Message**

Resource error. Parse the ttf resource failed.

Resource error. Parse the json resource failed.

**Description**

Resource parsing failed.

**Possible causes**

The resource content is invalid.

**Solution**

1\. Make sure that the icon resource is valid.

2\. Make sure that the animation parameter resource is valid.
