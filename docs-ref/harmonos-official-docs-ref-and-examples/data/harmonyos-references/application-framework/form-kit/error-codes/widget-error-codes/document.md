# Widget Error Codes

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/ED44widkRF-bZLGWhEF9mA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062323Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AACBAEC7B030DE34306347AF4AB1F9CBF24533DA0CE5E487ABEC83352B137402)

This topic describes only module-specific error codes. For details about universal error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

#### 16500050 IPC Failure

**Error Message**

IPC connection error.

**Description**

An error occurs when the system initiates inter-process communications (IPC) to complete the request.

**Possible Causes**

The parameter value passed in the API is too large, causing IPC data verification failure.

**Solution**

Pass appropriate parameter values.

#### 16500060 Service Connection Failure

**Error Message**

Service connection error.

**Description**

An error occurs when the system attempts to connect to a service to complete the request.

**Possible Causes**

1.  The widget is in the initialization state.
2.  The system is busy.

**Solution**

1.  Reconnect to the service.
2.  Restart the device.

#### 16500100 Failed to Obtain Widget Configuration Information

**Error Message**

Failed to obtain configuration information.

**Description**

An error occurs when the system attempts to obtain widget configuration information to complete the request.

**Possible Causes**

The widget configuration information field is missing or invalid.

**Solution**

Use the correct configuration information.

#### 16501000 Internal Function Error

**Error Message**

An internal functional error occurred.

**Description**

An internal error occurs when the system executes the request.

**Possible Causes**

An internal service execution exception occurs.

**Solution**

Try again after the system is restarted.

#### 16501001 Widget ID Not Exist

**Error Message**

The ID of the form to be operated does not exist.

**Description**

The specified widget in the request is not found.

**Possible Causes**

The widget ID passed in the API does not exist or is invalid.

**Solution**

Use a valid widget ID.

#### 16501002 Too Many Widgets

**Error Message**

The number of forms exceeds the maximum allowed.

**Description**

The application attempts to add more widgets when the number of widgets has reached the upper limit.

**Possible Causes**

The number of widgets has reached the upper limit.

**Solution**

Delete unnecessary widgets and then add the required widgets.

#### 16501003 Widget Not Operatable

**Error Message**

The form cannot be operated by the current application.

**Description**

The application cannot perform operations on a widget.

**Possible Causes**

The widget does not belong to the application.

**Solution**

Check whether the widget ID belongs to the application.

#### 16501006 Failed to Connect to the Widget Rendering Service

**Error Message**

FormRenderService is stopped. Connect to the service again.

**Description**

This error code is reported when the widget rendering service fails to be connected.

**Possible Causes**

The service is busy.

**Solution**

Try again later.

#### 16501007 Untrusted Widget

**Error Message**

Form is not trust.

**Description**

The widget is not trusted.

**Possible Causes**

The widget code has problems such as infinite loop and memory leakage, causing system exceptions.

**Solution**

Check whether the widget code has an infinite loop or memory leakage.

#### 16501010 Failed to Set the Background Image of the Interactive Widget

**Error Message**

Failed to set the live form background image.

**Description**

This error code is reported when the background image resource is invalid.

**Possible Causes**

The background image resource is invalid.

**Solution**

Check whether the background image resource is valid.

#### 16501011 API Not Supported

**Error Message**

The form can not support this operation.

**Description**

This error code is reported when the widget does not support the current API.

**Possible Causes**

The interactive widget animation is requested by a common widget, or the current interactive widget is incorrectly configured.

**Solution**

Check whether the configured [sceneAnimationParams](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-ui-widget-configuration#sceneanimationparams-field) of the current widget is correct.

#### 16501012 Incorrect Widget Dimension

**Error Message**

The form host uses an incorrect dimension.

**Description**

This error code is reported when the widget dimension is incorrect.

**Possible Causes**

The specified widget dimension is not configured, or the transferred widget dimension is invalid.

**Solution**

Check whether the input widget dimension is in the [FormDimension](../../arkts-apis/ohos-app-form-forminfo-forminfo/document.md#formdimension) and [supportDimensions](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-ui-widget-configuration#fields-in-configuration-file) configuration list.

#### 16501013 Operation Not Supported

**Error Message**

Some internal server error occurs.

**Description**

An internal error occurs when the system executes the current request.

**Possible Causes**

1.  The system is busy.
2.  The internal data of the system is abnormal.

**Solution**

1.  Restart the system and try again.
2.  If the restart still fails, submit an [online ticket](https://developer.huawei.com/consumer/en/support/feedback/#) to obtain help.

#### 2293766 Requested Bundle Name Not Exist

**Error Message**

The requested bundle name does not exist.

**Description**

The requested bundle name does not exist. This is an internal error.

**Possible Causes**

An error occurs when the bundle management module obtains the bundle name of the requester. This is an internal service execution exception.

**Solution**

1.  Restart the system and try again.
2.  If the restart still fails, submit an [online ticket](https://developer.huawei.com/consumer/en/support/feedback/#) to obtain help.

#### 2293767 Invalid Parameter

**Error Message**

Invalid params received on operating form.

**Description**

Invalid input parameters are passed when the API is called.

**Possible Causes**

1.  Mandatory parameters are not transferred.
2.  The parameter type is incorrect.
3.  The number of parameters is incorrect.
4.  The input parameter is empty, for example, an empty string ('').
5.  Incorrect parameter format.
6.  Invalid parameter value. The input parameters must be the same as those in [app.json5](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-configuration-file) and [Configuring ArkTS Widget Configuration Files](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-ui-widget-configuration).

**Solution**

Check the possible causes to determine whether mandatory parameters are transferred and whether the transferred parameter types are correct.

#### 2293795 Failed to Obtain the Bundle Manager Service

**Error Message**

Get bms rpc failed.

**Description**

Failed to obtain the Bundle Manager service.

**Possible Causes**

An internal service execution exception occurs.

**Solution**

1.  Restart the system and try again.
2.  If the restart still fails, submit an [online ticket](https://developer.huawei.com/consumer/en/support/feedback/#) to obtain help.

#### 2293798 Failed to Obtain the Widget Manager Service

**Error Message**

Get fms rpc failed.

**Description**

Failed to obtain the Widget Manager service.

**Possible Causes**

An internal service execution exception occurs.

**Solution**

1.  Restart the system and try again.
2.  If the restart still fails, submit an [online ticket](https://developer.huawei.com/consumer/en/support/feedback/#) to obtain help.

#### 2293802 Failed to Obtain the System Manager Service

**Error Message**

Get system manager service failed.

**Description**

Failed to obtain the System Manager service.

**Possible Causes**

An internal service execution exception occurs.

**Solution**

1.  Restart the system and try again.
2.  If the restart still fails, submit an [online ticket](https://developer.huawei.com/consumer/en/support/feedback/#) to obtain help.
