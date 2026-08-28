# Mouse Pointer Error Codes

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/n_b4oQ9tSr2BjF5TS_d7IA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062405Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=28D9763DA2F68E1F31B516C5BD143F42F7F38B5DF232484A20541C0018C447F3)

-   This topic describes only module-specific error codes. For details about universal error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

#### 26500001 Invalid Window ID

**Error Message**

Invalid windowId. Possible causes: The window id does not belong to the current process.

**Description**

Invalid window ID.

**Possible Causes**

The window ID does not belong to the current process.

**Solution**

Pass in the window ID of the current process. You can obtain the attributes of the current window by calling [getWindowProperties()](../../../../../application-framework/arkui/arkts-api/window-manager/ohos-window-window/interface-window/document.md#getwindowproperties9). The window ID is contained in the returned window attributes.

#### 3800001 Multimodal input internal error

**Error Message**

Input service exception. Possible causes: 1. Memory allocation failure. 2. Thread busy. 3. Service terminated abnormally. 4. Other unexpected errors. Try again later.

**Description**

Internal error of the multimodal input service.

**Possible Causes**

Unexpected errors, such as memory allocation failure, busy thread, and abnormal service exit, occur.

**Solution**

Try again later.
