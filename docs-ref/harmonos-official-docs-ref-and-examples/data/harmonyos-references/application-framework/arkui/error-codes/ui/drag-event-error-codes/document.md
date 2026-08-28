# Drag Event Error Codes

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/SjIfFH_MTiquo_Zeen5JGQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062311Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E766C4B95F1E9D8230E9E9C44207A679D8FC1D216771CC70CB084C758739569D)

This topic describes only module-specific error codes. For details about universal error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

#### 190001 Data Not Found

**Error Message**

Data not found.

**Description**

This error code is reported when no data has been obtained using the [getData](../../../arkts-components/universal-events/interaction-response-events/drag-event/document.md#getdata10) API of **DragEvent**.

**Possible Causes**

The **DragEvent** data has not been obtained.

**Solution**

N/A

#### 190002 Data Retrieval Error

**Error Message**

Data error.

**Description**

This error code is reported when the data obtained via the [getData](../../../arkts-components/universal-events/interaction-response-events/drag-event/document.md#getdata10) API of **DragEvent** is incorrect.

**Possible Causes**

The obtained data is incorrect.

**Solution**

N/A

#### 190003 Operation Not Allowed in the Current Phase

**Error Message**

Operation not allowed for current phase.

**Description**

This error code is reported when you call an API that is only supported during the [onDrop](../../../arkts-components/universal-events/interaction-response-events/drag-event/document.md#ondrop) phase outside of that phase.

**Possible Causes**

The operation is not allowed in the current phase.

**Solution**

Call the corresponding API in the [onDrop](../../../arkts-components/universal-events/interaction-response-events/drag-event/document.md#ondrop) phase.

#### 190004 Operation Failed

**Error Message**

Operation failed.

**Description**

This error code is reported if the [cancelDataLoading](../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-dragcontroller/document.md#canceldataloading15) API is called when data has not been loaded or loading is complete.

**Possible Causes**

The API is called at a wrong time.

**Solution**

Call the [cancelDataLoading](../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-dragcontroller/document.md#canceldataloading15) API during data loading.
