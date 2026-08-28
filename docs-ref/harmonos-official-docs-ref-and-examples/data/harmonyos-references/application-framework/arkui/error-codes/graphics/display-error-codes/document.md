# Display Error Codes

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/ZBcAMOx1TkuzJBVTYguOLg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062312Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=71DE9860F61E051B5CA258ADF875A56A4521B6C42864C77B1421265C829050AC)

This topic describes only module-specific error codes. For details about universal error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

#### 1400001 Invalid Display or Screen

**Error Message**

Invalid display or screen.

**Description**

This error code is reported when an invalid display, including a virtual screen, is operated.

**Possible Causes**

1.  The virtual screen has not been created.
2.  The virtual screen has been destroyed.

**Solution**

1.  Before operating the virtual screen, check whether the virtual screen has been created.
2.  Check whether the virtual screen has been destroyed.

#### 1400003 Abnormal Display Manager Service

**Error Message**

This display manager service works abnormally.

**Description**

This error code is reported when the display manager service is abnormal.

**Possible Causes**

1.  The display manager service is not started normally.
2.  The bottom-layer graphics synthesis and rendering are abnormal.

**Solution**

Try again later or restart the device.

#### 1400004 Parameter Error

**Error Message**

Parameter error.

**Description**

This error code is reported when an input parameter is incorrect.

**Possible Causes**

The parameter value is out of range.

**Solution**

Correct the parameters.
