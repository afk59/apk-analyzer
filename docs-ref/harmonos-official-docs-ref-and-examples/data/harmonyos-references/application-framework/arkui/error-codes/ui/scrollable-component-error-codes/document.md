# Scrollable Component Error Codes

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/d9BnCw48RaeGbTQvmnbggQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062311Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=45846B3F3E115B8BB2A990201F55A90A7217B791297B6064896B9AFAD0385F88)

This topic describes only module-specific error codes. For details about universal error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

#### 100004 Controller Not Bound to Component

**Error Message**

Controller not bound to component.

**Description**

This error code is reported when an API is called through a controller but no controller is bound to the component. The error code is a string.

**Possible Causes**

The API called requires a controller, but the component is not bound to one.

**Solution**

Verify that the controller is properly bound to a component and that the component has not been released.
