# ArkTS API Error Codes

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/7QkjJoywSU-fm6pvVrpJAA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062456Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1A33239311B3F56ED76806399BAD2D7E1712A0652E0E75B486DC2E9F546B619E)

This section describes only the error codes related to Graphics Accelerate Kit. For details about universal error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

#### 1016600000 The Current API Cannot Be Called in the Resource Acceleration ExtensionAbility

**Message**

The API call from an ExtensionAbility is not allowed.

**Description**

This API cannot be called in the resource acceleration ExtensionAbility.

**Possible causes**

It is not allowed to call this API in the resource acceleration ExtensionAbility.

**Solution**

Check whether this API is in the range of APIs allowed by the resource acceleration ExtensionAbility. Only the following APIs provided by **assetDownloadManager** can be called:

-   [assetDownloadManager.fetchManifestUrl](../assetdownloadmanager-resource-package-download-management/document.md#en-us_topic_0000002214513333_en-us_topic_0000002137922672_section81101219425)
-   [assetDownloadManager.removeAssetDownloadTask](../assetdownloadmanager-resource-package-download-management/document.md#en-us_topic_0000002214513333_en-us_topic_0000002137922672_section222042984419)
-   [assetDownloadManager.fetchAllAssetDownloadTasks](../assetdownloadmanager-resource-package-download-management/document.md#en-us_topic_0000002214513333_en-us_topic_0000002137922672_section918114094718)
-   [assetDownloadManager.removeAllAssetDownloadTasks](../assetdownloadmanager-resource-package-download-management/document.md#en-us_topic_0000002214513333_en-us_topic_0000002137922672_section2809432393)
-   [assetDownloadManager.fetchGroupAssetDownloadTasks](../assetdownloadmanager-resource-package-download-management/document.md#en-us_topic_0000002214513333_en-us_topic_0000002137922672_section93791016111111)
-   [assetDownloadManager.removeGroupAssetDownloadTasks](../assetdownloadmanager-resource-package-download-management/document.md#en-us_topic_0000002214513333_en-us_topic_0000002137922672_section641613495177)
-   [assetDownloadManager.limitDownloadTaskSpeed](../assetdownloadmanager-resource-package-download-management/document.md#en-us_topic_0000002214513333_en-us_topic_0000002137922672_section17279143882113)
-   [assetDownloadManager.reportDownloadProgress](../assetdownloadmanager-resource-package-download-management/document.md#section1492357144916)

#### 1016600001 The Domain Name of the Download Task Is Not in the Trustlist

**Message**

The domain name of the download task is not in the domain name trustlist.

**Description**

The domain name of the download task is not in the trustlist.

**Possible causes**

The domain name of the download task is not in the trustlist.

**Solution**

-   Third-party CDN: View the domain name trustlist in AppGallery Connect. For details, please refer to [Creating a Download Task](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/graphics-accelerate-assetdownload-release#en-us_topic_0000002179265860_en-us_topic_0000002177341213_section1494105011355).
-   Huawei CDN: The domain name trustlist is automatically set based on resource package download tasks.

#### 1016600002 The Task ID or Group ID Does Not Exist During Download Task Pausing, Resuming, or Obtaining

**Message**

The task ID or group ID entered during operations such as pause, resume, and fetch does not exist.

**Description**

The task ID or group ID does not exist during download task pausing, resuming, or obtaining.

**Possible causes**

No operable task ID or group ID is found.

**Solution**

The task ID or group ID does not exist. Ensure that the task ID or group ID is correct.

#### 1016600003 The Current Task Status Does Not Support the Current Operation

**Message**

The current task status does not support the current operator.

**Description**

The current task status does not support the current operation.

**Possible causes**

The current task status does not match the current operation. For example, to resume a download task that is not paused, or to pause a download task which has already been paused.

**Solution**

Before performing an operation on a task, check the current status of the task and ensure that the task operation matches the task status. For example, call the [fetchAllAssetDownloadTasks](../assetdownloadmanager-resource-package-download-management/document.md#en-us_topic_0000002214513333_en-us_topic_0000002137922672_section918114094718) method to view the task status.

#### 1016600004 The Task Queue Is Full

**Message**

The application task queue is full.

**Description**

The task queue is full.

**Possible causes**

The number of resource package download tasks in the queue exceeds 200.

**Solution**

Submit tasks only when there is space available in the task queue.

#### 1016600005 Execution of a Resource Acceleration ExtensionAbility Method Times Out

**Message**

Extension life cycle callback execution timed out.

**Description**

The execution of a resource acceleration ExtensionAbility method times out.

**Possible causes**

The execution of the resource acceleration ExtensionAbility method is not finished within its lifecycle.

**Solution**

[Submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/add/101704353566310877?level2=201704444384569052&amp;level3=601723606112598571). Huawei technical support will get back to you as soon as possible.

#### 1016600006 Abnormal Method Within the Resource Acceleration ExtensionAbility Lifecycle

**Message**

An exception occurs in the callback extension js.

**Description**

There is an abnormal method within the resource acceleration ExtensionAbility lifecycle.

**Possible causes**

The internal processing logic of the resource acceleration ExtensionAbility times out.

**Solution**

Check whether there are uncaught exceptions in the methods within the resource acceleration ExtensionAbility lifecycle.

#### 1016600094 Service Error

**Message**

Task service ability error.

**Description**

A service error occurs.

**Possible causes**

The game resource acceleration service is abnormal.

**Solution**

[Submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/add/101704353566310877?level2=201704444384569052&amp;level3=601723606112598571). Huawei technical support will get back to you as soon as possible.

#### 1016600401 Parameter Error

**Message**

Parameter error.

**Description**

Parameter error.

**Possible causes**

The type or value of an input parameter is incorrect.

**Solution**

Ensure that the input parameters are correct and try again.
