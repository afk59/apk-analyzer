# Snapshot Error Codes

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/03/v3/KIe0Hpf9RyCOyYxWxpF1mw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062311Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DDAF8B9578F24813909C4AD924C11EFB38DD11512E79F5E89AEFB50E29079681)

This topic describes only module-specific error codes. For details about universal error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

#### 160001 Image Loading Error

**Error Message**

An image component in builder is not ready for taking a snapshot. The check for the ready state is required when the checkImageStatus option is enabled.

**Symptom**

This error code is reported when image loading fails.

**Possible Cause**

The **Image** component fails to decode the image properly or the node fails to load the image before the snapshot API is called.

**Solution**

Set the **delay** parameter of a snapshot API to ensure that the image is loaded successfully.

#### 160002 Snapshot Timeout

**Error Message**

Timeout.

**Symptom**

This error code is reported when image loading timeout occurs.

**Possible Cause**

The required system task is not executed.

**Solution**

Use the asynchronous API corresponding to the current snapshot API.
