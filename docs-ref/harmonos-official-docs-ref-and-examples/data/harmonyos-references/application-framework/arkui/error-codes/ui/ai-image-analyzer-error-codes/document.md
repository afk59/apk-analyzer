# AI Image Analyzer Error Codes

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/VrlpWmQQQ4GZL557brnjhg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062311Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=56C5B556BD1B135AAD91B33F5FDEF681F7D30DB57F08BAB44F72A7BE423A8722)

This topic describes only module-specific error codes. For details about universal error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

#### 110001 AI Image Analysis Not Supported

**Error Message**

Image analysis feature is unsupported.

**Description**

This error code is reported when **startImageAnalyzer()** is called while AI image analysis is not supported.

**Possible Causes**

An unsupported API is called.

**Solution**

N/A

#### 110002 AI Image Analysis Already in Progress

**Error Message**

Image analysis is currently being executed.

**Description**

This error code is reported when **startImageAnalyzer()** is called while the previous analysis session is still ongoing.

**Possible Causes**

The API is called at an incorrect time.

**Solution**

N/A

#### 110003 AI Image Analysis Terminated

**Error Message**

Image analysis is stopped.

**Description**

This error code is reported when **stopImageAnalyzer()** interrupts an ongoing analysis operation initiated by **startImageAnalyzer()**.

**Possible Causes**

The API is called at an incorrect time.

**Solution**

N/A
