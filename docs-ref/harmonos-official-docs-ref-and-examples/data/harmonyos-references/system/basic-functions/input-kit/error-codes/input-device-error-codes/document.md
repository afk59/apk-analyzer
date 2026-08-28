# Input Device Error Codes

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/pWkCdobGS5SOP6xC6a-bOA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062405Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=34AE11757EF4616A0D34E900AF0D40751FABDD5CEA5B79BAD359D8D8ED3E944A)

-   This topic describes only module-specific error codes. For details about universal error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

#### 3900002 Keyboard Not Connected

**Error Message**

There is currently no keyboard device connected.

**Description**

This error code is reported if no connected keyboard is detected.

**Possible Causes**

The physical connection of the input device is disconnected.

**Procedure**

Check whether the keyboard cable is disconnected.

#### 3900003 API Call Failed for a Non-Input Application

**Error Message**

It is prohibited for non-input applications.

**Description**

This error code is reported if the API is called by a non-input application.

**Possible Causes**

Non-input applications call this API.

**Procedure**

Use an input application to call this API.

#### 3800001 Multimodal input internal error

**Error Message**

Input service exception. Possible causes: 1. Memory allocation failure. 2. Thread busy. 3. Service terminated abnormally. 4. Other unexpected errors. Try again later.

**Description**

Internal error of the multimodal input service.

**Possible Causes**

Unexpected errors, such as memory allocation failure, busy thread, and abnormal service exit, occur.

**Procedure**

Try again later.
