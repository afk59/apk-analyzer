# Drawing and Display Error Codes

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/keR8zpt-R3-Bjc8IznfxVg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062456Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=53388ACC572EEC984E3127EEEBD045464C936EC0043EC9C4CE324B447C23DBD7)

This topic describes only module-specific error codes. For details about universal error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

#### 25900001 Abnormal Parameter Value

**Error Message**

Parameter error. Possible causes: Incorrect parameter range.

**Description**

This error code is reported when the parameter value exceeds the allowable range.

**Possible Causes**

The parameter value exceeds the valid range. For example, an enumerated value exceeds the defined range.

**Solution**

Pass parameter values that meet the requirements in the API.
