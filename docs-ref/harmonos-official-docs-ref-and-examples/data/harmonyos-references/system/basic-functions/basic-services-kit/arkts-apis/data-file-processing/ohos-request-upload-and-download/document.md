# @ohos.request (Upload and Download)

The **request** module provides applications with basic upload, download, and background transmission agent capabilities.

-   Currently, the **request** module cannot be called in extensions.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/oyE0gRicRTedVDbBft6W_w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B44CE7135AF82D5F0B24D1F09FC11D7351E749B8CD2C80C31EFD59A00D3AB680)

The initial APIs of this module are supported since API version 6. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { request } from '@kit.BasicServicesKit';

#### Constants

**System capability**: SystemCapability.MiscServices.Download

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/NJ5QuDOmRSmvVLpS79oK9Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=26A564BCEFC2CA3C290796F11558E4F8F4AF008A5AF7F067B15D53474E8B1F10)

**Network type**: custom network type specified by **networkType** in [DownloadConfig](#downloadconfig).

**Download error codes**: values of **err** in the [on('fail')](#onfail7) callback and the values of the **failedReason** field returned by [getTaskInfo](#gettaskinfo9).

**Causes of download pause**: values of **pausedReason** returned by [getTaskInfo](#gettaskinfo9).

**Download status code**: values of **status** returned by [getTaskInfo](#gettaskinfo9).

| Name | Type | Value | Description |
| :-- | :-- | :-- | :-- |
| EXCEPTION\_PERMISSION9+ | number | 201 | (Universal error codes) Permission verification failed. |
| EXCEPTION\_PARAMCHECK9+ | number | 401 | (Universal error codes) Parameter check failed. |
| EXCEPTION\_UNSUPPORTED9+ | number | 801 | (Universal error codes) The device does not support this API. |
| EXCEPTION\_FILEIO9+ | number | 13400001 | (Specific error codes) Abnormal file operation. |
| EXCEPTION\_FILEPATH9+ | number | 13400002 | (Specific error codes) Abnormal file path. |
| EXCEPTION\_SERVICE9+ | number | 13400003 | (Specific error codes) Abnormal service. |
| EXCEPTION\_OTHERS9+ | number | 13499999 | (Specific error codes) Other errors. |
| NETWORK\_MOBILE | number | 0x00000001 | (Network type) Bit flag download allowed on a mobile network. |
| NETWORK\_WIFI | number | 0x00010000 | (Network type) Bit flag download allowed on a WLAN. |
| ERROR\_CANNOT\_RESUME7+ | number | 0 | (Download error codes) Failure to resume the download due to network errors. |
| ERROR\_DEVICE\_NOT\_FOUND7+ | number | 1 | (Download error codes) Failure to find a storage device such as a memory card. |
| ERROR\_FILE\_ALREADY\_EXISTS7+ | number | 2 | (Download error codes) Failure to download the file because it already exists. |
| ERROR\_FILE\_ERROR7+ | number | 3 | (Download error codes) File operation failed. |
| ERROR\_HTTP\_DATA\_ERROR7+ | number | 4 | (Download error codes) HTTP transmission failed. |
| ERROR\_INSUFFICIENT\_SPACE7+ | number | 5 | (Download error codes) Insufficient storage space. |
| ERROR\_TOO\_MANY\_REDIRECTS7+ | number | 6 | (Download error codes) Error caused by too many network redirections. |
| ERROR\_UNHANDLED\_HTTP\_CODE7+ | number | 7 | (Download error codes) Unidentified HTTP code. |
| ERROR\_UNKNOWN7+ | number | 8 | 
(Download error codes) Unknown error.

In API version 12 or earlier, only serial connection to the IP addresses associated with the specified domain name is supported, and the connection time for a single IP address is not controllable. If the first IP address returned by the DNS is blocked, a handshake timeout may occur, leading to an ERROR\_UNKNOWN error.

 |
| ERROR\_OFFLINE9+ | number | 9 | (Download error codes) No network connection. |
| ERROR\_UNSUPPORTED\_NETWORK\_TYPE9+ | number | 10 | (Download error codes) Network type mismatch. |
| PAUSED\_QUEUED\_FOR\_WIFI7+ | number | 0 | (Causes of download pause) Download paused and queuing for a WLAN connection because the file size exceeds the maximum value allowed for a mobile network session. |
| PAUSED\_WAITING\_FOR\_NETWORK7+ | number | 1 | 

(Causes of download pause) Download paused due to a network connection problem.

Example: network disconnection

 |
| PAUSED\_WAITING\_TO\_RETRY7+ | number | 2 | (Causes of download pause) Download paused due to network error and then retried. |
| PAUSED\_BY\_USER9+ | number | 3 | (Causes of download pause) The user paused the session. |
| PAUSED\_UNKNOWN7+ | number | 4 | (Causes of download pause) Download paused due to unknown reasons. |
| SESSION\_SUCCESSFUL7+ | number | 0 | (Download task status codes) Successful download. |
| SESSION\_RUNNING7+ | number | 1 | (Download task status codes) Download in progress. |
| SESSION\_PENDING7+ | number | 2 | (Download task status codes) Download pending. |
| SESSION\_PAUSED7+ | number | 3 | (Download task status codes) Download paused. |
| SESSION\_FAILED7+ | number | 4 | (Download task status codes) Download failure without retry. |

#### request.uploadFile9+

uploadFile(context: BaseContext, config: UploadConfig): Promise<UploadTask>

Uploads a file. This API uses a promise to return the result. HTTP is supported. You can use [on('complete'|'fail')](#oncomplete--fail9) to obtain the upload success or error information.

**Required permissions**: ohos.permission.INTERNET

**System capability**: SystemCapability.MiscServices.Upload

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/yrjOqpvhQyarsKXRlmSR4w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2DA38DF2930653A18D7A8D00AC04A007EA914D4FF75A0666A31EDA64E01AF328)

For details about how to obtain the context in the example, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | [BaseContext](../../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/basecontext/document.md) | Yes | Application-based context. |
| config | [UploadConfig](#uploadconfig) | Yes | Upload configurations. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[UploadTask](#uploadtask)\> | Promise used to return the **UploadTask** object. |

**Error codes**

For details about the error codes, see [Upload and Download Error Codes](../../../error-codes/upload-and-download-error-codes/document.md) and [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | The permissions check fails. |
| 401 | The parameters check fails. Possible causes: 1. Missing mandatory parameters. 2. Incorrect parameter type. 3. Parameter verification failed. |
| 13400002 | File path not supported or invalid. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let uploadTask: request.UploadTask;
let uploadConfig: request.UploadConfig = {
  url: 'http://www.example.com', // Replace the URL with the HTTP address of the real server.
  header: { 'Accept': '\*/\*' },
  method: "POST",
  files: \[{ filename: "test", name: "test", uri: "internal://cache/test.jpg", type: "image/jpeg" }\], // Set type to the MIME type specified by the HTTP.
  data: \[{ name: "name123", value: "123" }\],
};
try {
  request.uploadFile(context, uploadConfig).then((data: request.UploadTask) => {
    uploadTask = data;
  }).catch((err: BusinessError) => {
    console.error(\`Failed to request the upload. Code: ${err.code}, message: ${err.message}\`);
  });
} catch (err) {
  console.error(\`Failed to request the upload. Code: ${err.code}, message: ${err.message}\`);
}

#### request.uploadFile9+

uploadFile(context: BaseContext, config: UploadConfig, callback: AsyncCallback<UploadTask>): void

Uploads a file. This API uses an asynchronous callback to return the result. HTTP is supported. You can use [on('complete'|'fail')](#oncomplete--fail9) to obtain the upload success or error information.

**Required permissions**: ohos.permission.INTERNET

**System capability**: SystemCapability.MiscServices.Upload

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/JtaRnP44R7ioepBD8mzM1g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B61EC3F2BCCF469260714ECE94C057BC95ECFF843AF33888B10885691C5B3D6A)

For details about how to obtain the context in the example, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | [BaseContext](../../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/basecontext/document.md) | Yes | Application-based context. |
| config | [UploadConfig](#uploadconfig) | Yes | Upload configurations. |
| callback | AsyncCallback<[UploadTask](#uploadtask)\> | Yes | Callback used to return the **UploadTask** object. If the operation is successful, **err** is **undefined**, and **data** is the **UploadTask** object obtained. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Upload and Download Error Codes](../../../error-codes/upload-and-download-error-codes/document.md) and [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | The permissions check fails. |
| 401 | The parameters check fails. Possible causes: 1. Missing mandatory parameters. 2. Incorrect parameter type. 3. Parameter verification failed. |
| 13400002 | File path not supported or invalid. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let uploadTask: request.UploadTask;
let uploadConfig: request.UploadConfig = {
  url: 'http://www.example.com', // Replace the URL with the HTTP address of the real server.
  header: { 'Accept': '\*/\*' },
  method: "POST",
  files: \[{ filename: "test", name: "test", uri: "internal://cache/test.jpg", type: "image/jpeg" }\], // Set type to the MIME type specified by the HTTP.
  data: \[{ name: "name123", value: "123" }\],
};
try {
  request.uploadFile(context, uploadConfig, (err: BusinessError, data: request.UploadTask) => {
    if (err) {
      console.error(\`Failed to request the upload. Code: ${err.code}, message: ${err.message}\`);
      return;
    }
    uploadTask = data;
  });
} catch (err) {
  console.error(\`Failed to request the upload. Code: ${err.code}, message: ${err.message}\`);
}

#### request.upload(deprecated)

upload(config: UploadConfig): Promise<UploadTask>

Uploads files. This API uses a promise to return the result.

**Model restriction**: This API can be used only in the FA model.

**Required permissions**: ohos.permission.INTERNET

**System capability**: SystemCapability.MiscServices.Upload

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/qeuWeZc3Tv6cKQAnpu_Zfg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9798C9AD2F31A02B1EF114BA429364A6DBD902F6276E29C891808E312CA9A91F)

This API is supported since API version 6 and deprecated since API version 9. You are advised to use [request.uploadFile](#requestuploadfile9) instead.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| config | [UploadConfig](#uploadconfig) | Yes | Upload configurations. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[UploadTask](#uploadtask)\> | Promise used to return the **UploadTask** object. |

**Error codes**

For details about the error codes, see [Upload and Download Error Codes](../../../error-codes/upload-and-download-error-codes/document.md) and [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | The permissions check fails. |

**Example**

let uploadTask: request.UploadTask;
let uploadConfig: request.UploadConfig = {
  url: 'http://www.example.com', // Replace the URL with the HTTP address of the real server.
  header: { 'Accept': '\*/\*' },
  method: "POST",
  files: \[{ filename: "test", name: "test", uri: "internal://cache/test.jpg", type: "image/jpeg" }\], // Set type to the MIME type specified by the HTTP.
  data: \[{ name: "name123", value: "123" }\],
};
request.upload(uploadConfig).then((data: request.UploadTask) => {
  uploadTask = data;
}).catch((err: BusinessError) => {
  console.error(\`Failed to request the upload. Code: ${err.code}, message: ${err.message}\`);
})

#### request.upload(deprecated)

upload(config: UploadConfig, callback: AsyncCallback<UploadTask>): void

Uploads files. This API uses an asynchronous callback to return the result.

**Model restriction**: This API can be used only in the FA model.

**Required permissions**: ohos.permission.INTERNET

**System capability**: SystemCapability.MiscServices.Upload

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/xKEDWiG_RzqLGg-QzDldDQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3BF19BD455E967DDF12B04DD8298BE5C1F08AF81DE7CAFB6E1EDD4E28A8176DC)

This API is supported since API version 6 and deprecated since API version 9. You are advised to use [request.uploadFile](#requestuploadfile9) instead.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| config | [UploadConfig](#uploadconfig) | Yes | Upload configurations. |
| callback | AsyncCallback<[UploadTask](#uploadtask)\> | Yes | Callback used to return the **UploadTask** object. If the operation is successful, **err** is **undefined**, and **data** is the **UploadTask** object obtained. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Upload and Download Error Codes](../../../error-codes/upload-and-download-error-codes/document.md) and [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | The permissions check fails. |

**Example**

let uploadTask: request.UploadTask;
let uploadConfig: request.UploadConfig = {
  url: 'http://www.example.com', // Replace the URL with the HTTP address of the real server.
  header: { 'Accept': '\*/\*' },
  method: "POST",
  files: \[{ filename: "test", name: "test", uri: "internal://cache/test.jpg", type: "image/jpeg" }\], // Set type to the MIME type specified by the HTTP.
  data: \[{ name: "name123", value: "123" }\],
};
request.upload(uploadConfig, (err: BusinessError, data: request.UploadTask) => {
  if (err) {
    console.error(\`Failed to request the upload. Code: ${err.code}, message: ${err.message}\`);
    return;
  }
  uploadTask = data;
});

#### UploadTask

Implements file uploads. Before using any APIs of this class, you must obtain an **UploadTask** object, from a promise through [request.uploadFile](#requestuploadfile9) or from a callback through [request.uploadFile](#requestuploadfile9-1).

#### \[h2\]on('progress')

on(type: 'progress', callback: (uploadedSize: number, totalSize: number) => void): void

Subscribes to upload progress events. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.MiscServices.Upload

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/B2qogdLFTwyUZanEWne6gg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EFCCFCCDDFCBEEA7BC037B3F49D0931F09DC8B553DD568D84B4019D82F9A96C1)

To maintain a balance between power consumption and performance, this API cannot be called when the application is running in the background.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'progress'**, indicating upload progress. |
| callback | function | Yes | Callback used to return the size of the uploaded file and the total size of the file to upload. |

Parameters of the callback function

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| uploadedSize | number | Yes | Size of the uploaded files, in bytes. |
| totalSize | number | Yes | Total size of the files to upload, in bytes. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | The parameters check fails. Possible causes: 1. Missing mandatory parameters. 2. Incorrect parameter type. 3. Parameter verification failed. |

**Example**

let upProgressCallback = (uploadedSize: number, totalSize: number) => {
  console.info("upload totalSize:" + totalSize + "  uploadedSize:" + uploadedSize);
};
uploadTask.on('progress', upProgressCallback);

#### \[h2\]on('headerReceive')7+

on(type: 'headerReceive', callback: (header: object) => void): void

Subscribes to HTTP response events for the upload task.This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.MiscServices.Upload

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type.

\- **'headerReceive'**: The HTTP request receives a response.

 |
| callback | function | Yes | Callback used to return the response content. |

Parameters of the callback function

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| header | object | Yes | HTTP response. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | The parameters check fails. Possible causes: 1. Missing mandatory parameters. 2. Incorrect parameter type. 3. Parameter verification failed. |

**Example**

let headerCallback = (headers: object) => {
  console.info("upOnHeader headers:" + JSON.stringify(headers));
};
uploadTask.on('headerReceive', headerCallback);

#### \[h2\]on('complete' | 'fail')9+

on(type: 'complete' | 'fail', callback: Callback<Array<TaskState>>): void

Subscribes to upload completion or failure events. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.MiscServices.Upload

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Type of the event to subscribe to. |
| callback | Callback<Array<[TaskState](#taskstate9)\>> | Yes | Callback used to return the state of the upload task. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | The parameters check fails. Possible causes: 1. Missing mandatory parameters. 2. Incorrect parameter type. 3. Parameter verification failed. |

**Example**

let upCompleteCallback = (taskStates: Array<request.TaskState>) => {
  for (let i = 0; i < taskStates.length; i++) {
    console.info("upOnComplete taskState:" + JSON.stringify(taskStates\[i\]));
  }
};
uploadTask.on('complete', upCompleteCallback);

let upFailCallback = (taskStates: Array<request.TaskState>) => {
  for (let i = 0; i < taskStates.length; i++) {
    console.info("upOnFail taskState:" + JSON.stringify(taskStates\[i\]));
  }
};
uploadTask.on('fail', upFailCallback);

#### \[h2\]off('progress')

off(type: 'progress', callback?: (uploadedSize: number, totalSize: number) => void): void

Unsubscribes from upload progress events.

**System capability**: SystemCapability.MiscServices.Upload

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type.

\- **'progress'**: upload progress.

 |
| callback | function | No | Callback to unregister. If this parameter is not specified, all callbacks of the current type will be unregistered. |

Parameters of the callback function

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| uploadedSize | number | Yes | Size of the uploaded files, in bytes. |
| totalSize | number | Yes | Total size of the files to upload, in bytes. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | The parameters check fails. Possible causes: 1. Missing mandatory parameters. 2. Incorrect parameter type. 3. Parameter verification failed. |

**Example**

let upProgressCallback1 = (uploadedSize: number, totalSize: number) => {
  console.info('Upload delete progress notification.' + 'totalSize:' + totalSize + 'uploadedSize:' + uploadedSize);
};
let upProgressCallback2 = (uploadedSize: number, totalSize: number) => {
  console.info('Upload delete progress notification.' + 'totalSize:' + totalSize + 'uploadedSize:' + uploadedSize);
};
uploadTask.on('progress', upProgressCallback1);
uploadTask.on('progress', upProgressCallback2);
// Unsubscribe from upProgressCallback1.
uploadTask.off('progress', upProgressCallback1);
// Unsubscribe from all callbacks of upload progress events.
uploadTask.off('progress');

#### \[h2\]off('headerReceive')7+

off(type: 'headerReceive', callback?: (header: object) => void): void

Unsubscribes from HTTP response events for the upload task.

**System capability**: SystemCapability.MiscServices.Upload

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type.

\- **'headerReceive'**: The HTTP request receives a response.

 |
| callback | function | No | Callback to unregister. If this parameter is not specified, all callbacks of the current type will be unregistered. |

Parameters of the callback function

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| header | object | Yes | HTTP response. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | The parameters check fails. Possible causes: 1. Missing mandatory parameters. 2. Incorrect parameter type. 3. Parameter verification failed. |

**Example**

let headerCallback1 = (header: object) => {
  console.info(\`Upload delete headerReceive notification. header: ${JSON.stringify(header)}\`);
};
let headerCallback2 = (header: object) => {
  console.info(\`Upload delete headerReceive notification. header: ${JSON.stringify(header)}\`);
};
uploadTask.on('headerReceive', headerCallback1);
uploadTask.on('headerReceive', headerCallback2);
// Unsubscribe from headerCallback1.
uploadTask.off('headerReceive', headerCallback1);
// Unsubscribe from all callbacks of the HTTP header events for the upload task.
uploadTask.off('headerReceive');

#### \[h2\]off('complete' | 'fail')9+

off(type: 'complete' | 'fail', callback?: Callback<Array<TaskState>>): void

Unsubscribes from upload completion or failure events.

**System capability**: SystemCapability.MiscServices.Upload

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type.

\- **'complete'**: upload task completion.

\- **'fail'**: upload task failure.

 |
| callback | Callback<Array<[TaskState](#taskstate9)\>> | No | Callback to unregister. If this parameter is not specified, all callbacks of the current type will be unregistered. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | the parameters check fails. Possible causes: 1. Missing mandatory parameters. 2. Incorrect parameter type. 3. Parameter verification failed. |

**Example**

let upCompleteCallback1 = (taskStates: Array<request.TaskState>) => {
  console.info('Upload delete complete notification.');
  for (let i = 0; i < taskStates.length; i++) {
    console.info('taskState:' + JSON.stringify(taskStates\[i\]));
  }
};
let upCompleteCallback2 = (taskStates: Array<request.TaskState>) => {
  console.info('Upload delete complete notification.');
  for (let i = 0; i < taskStates.length; i++) {
    console.info('taskState:' + JSON.stringify(taskStates\[i\]));
  }
};
uploadTask.on('complete', upCompleteCallback1);
uploadTask.on('complete', upCompleteCallback2);
// Unsubscribe from headerCallback1.
uploadTask.off('complete', upCompleteCallback1);
// Unsubscribe from all callbacks of the upload completion events.
uploadTask.off('complete');

let upFailCallback1 = (taskStates: Array<request.TaskState>) => {
  console.info('Upload delete fail notification.');
  for (let i = 0; i < taskStates.length; i++) {
    console.info('taskState:' + JSON.stringify(taskStates\[i\]));
  }
};
let upFailCallback2 = (taskStates: Array<request.TaskState>) => {
  console.info('Upload delete fail notification.');
  for (let i = 0; i < taskStates.length; i++) {
    console.info('taskState:' + JSON.stringify(taskStates\[i\]));
  }
};
uploadTask.on('fail', upFailCallback1);
uploadTask.on('fail', upFailCallback2);
// Unsubscribe from headerCallback1.
uploadTask.off('fail', upFailCallback1);
// Unsubscribe from all callbacks of the upload failure events.
uploadTask.off('fail');

#### \[h2\]delete9+

delete(): Promise<boolean>

Deletes this upload task. This API uses a promise to return the result.

**Required permissions**: ohos.permission.INTERNET

**System capability**: SystemCapability.MiscServices.Upload

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/hzOXRu9-SLO3Ke8w6uR3nA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8FF43AB7CC424AA7F627EAB1CC74C127740845F8616C308AF4C7CB0655D010E6)

The scenarios for triggering error code **401 the parameters check fails** do not exist. Therefore, this error code is removed from API version 12.

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return the result. The value **true** indicates that the operation is successful; **false** indicates the opposite. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | The permissions check fails. |

**Example**

uploadTask.delete().then((result: boolean) => {
  console.info('Succeeded in deleting the upload task.');
}).catch((err: BusinessError) => {
  console.error(\`Failed to delete the upload task. Code: ${err.code}, message: ${err.message}\`);
});

#### \[h2\]delete9+

delete(callback: AsyncCallback<boolean>): void

Deletes an upload task. This API uses an asynchronous callback to return the result.

**Required permissions**: ohos.permission.INTERNET

**System capability**: SystemCapability.MiscServices.Upload

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/zl1MnSfYQtOYxVpl_8e9ug/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A219957CCB07538C094552AB9B9333A8782F5D09FFBED079316190F54DECF995)

The scenarios for triggering error code **401 the parameters check fails** do not exist. Therefore, this error code is removed from API version 12.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<boolean> | Yes | Callback used to return the result. The value **true** indicates that the operation is successful; **false** indicates the opposite. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | The permissions check fails. |

**Example**

uploadTask.delete((err: BusinessError, result: boolean) => {
  if (err) {
    console.error(\`Failed to delete the upload task. Code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info('Succeeded in deleting the upload task.');
});

#### \[h2\]remove(deprecated)

remove(): Promise<boolean>

Removes this upload task. This API uses a promise to return the result.

**Required permissions**: ohos.permission.INTERNET

**System capability**: SystemCapability.MiscServices.Upload

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/oCk7umy-TzeOogyhIoUijA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BC633391720D79067643F4371B2765AAC0FA6397625943DC43DE15CA4B70A456)

This API is supported since API version 6 and deprecated since API version 9. You are advised to use [delete](#delete9) instead.

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return the result. The value **true** indicates that the operation is successful; **false** indicates the opposite. |

**Error codes**

For details about the error codes, see [Upload and Download Error Codes](../../../error-codes/upload-and-download-error-codes/document.md) and [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | The permissions check fails. |

**Example**

uploadTask.remove().then((result: boolean) => {
  console.info('Succeeded in removing the upload task.');
}).catch((err: BusinessError) => {
  console.error(\`Failed to remove the upload task. Code: ${err.code}, message: ${err.message}\`);
});

#### \[h2\]remove(deprecated)

remove(callback: AsyncCallback<boolean>): void

Removes an upload task. This API uses an asynchronous callback to return the result.

**Required permissions**: ohos.permission.INTERNET

**System capability**: SystemCapability.MiscServices.Upload

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/L4DLrCrJTu6aDmDot8nMaA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0392E53EE7FCD23EA93248447A1D1B4380615B5ECE8E06AD325BA597BBC06F94)

This API is supported since API version 6 and deprecated since API version 9. You are advised to use [delete](#delete9-1) instead.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<boolean> | Yes | Callback used to return the result. The value **true** indicates that the operation is successful; **false** indicates the opposite. |

**Error codes**

For details about the error codes, see [Upload and Download Error Codes](../../../error-codes/upload-and-download-error-codes/document.md) and [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | The permissions check fails. |

**Example**

uploadTask.remove((err: BusinessError, result: boolean) => {
  if (err) {
    console.error(\`Failed to remove the upload task. Code: ${err.code}, message: ${err.message}\`);
    return;
  }
  if (result) {
    console.info('Succeeded in removing the upload task.');
  }
});

#### UploadConfig

Describes the configuration of an upload task.

**System capability**: SystemCapability.MiscServices.Upload

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| url | string | No | No | Resource URL. From API version 6 to 14, the value contains a maximum of 2048 characters; since API version 15, the value contains a maximum of 8192 characters. [Intercepting HTTP](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-file-upload-download#intercepting-http) is supported. |
| header | Object | No | No | HTTP or HTTPS header added to an upload request. |
| method | string | No | No | HTTP request method. The value can be **POST** or **PUT**. The default value is **POST**. Use **POST** to add resources and **PUT** to modify resources. |
| index11+ | number | No | Yes | Path index of the task. The default value is **0**. |
| begins11+ | number | No | Yes | Start point of the file read when the upload task begins. The default value is **0**. The value is a closed interval, indicating that the file is read from the beginning. |
| ends11+ | number | No | Yes | End point of the file read when the upload task is complete. The default value is **\-1**. The value is a closed interval, indicating that the file is read till the end. |
| files | Array<[File](#file)\> | No | No | List of files to upload. The files are submitted in multipart/form-data format. |
| data | Array<[RequestData](#requestdata)\> | No | No | Form data in the request body. |

#### TaskState9+

Implements a **TaskState** object, which is the callback parameter of the [on('complete' | 'fail')](#oncomplete--fail9) and [off('complete' | 'fail')](#offcomplete--fail9) APIs.

**System capability**: SystemCapability.MiscServices.Upload

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| path | string | No | No | File path. |
| responseCode | number | No | No | 
Return value of an upload task. The value **0** means that the task is successful, and other values means that the task fails. For details about the task result, see **message**.

You are advised to create an upload task by using [request.agent.create](#requestagentcreate10-1) and handle exceptions based on standard error codes.

 |
| message | string | No | No | Description of the upload task result. |

The following table describes the enum values of **responseCode**.

| Result Code | Description |
| :-- | :-- |
| 0 | uploaded success. |
| 5 | Task suspended or stopped. |
| 6 | Foreground task stopped. The reason is that the application, to which the task belongs, is switched to the background or terminated. Check the application status. |
| 7 | No network connection. Check whether the device is connected to the network. |
| 8 | Network mismatch. Check whether the current network type matches the network type required by the task. |
| 10 | Failed to create the HTTP request. Verify the parameters or try again. |
| 12 | Request timeout. Verify the parameter configuration or the network connection, or try again. |
| 13 | Connection failed. Verify the parameter configuration or the network connection, or try again. |
| 14 | Request failed. Verify the parameter configuration or the network connection, or try again. |
| 15 | Upload failed. Verify the parameter configuration or the network connection, or try again. |
| 16 | Redirection failed. Verify the parameter configuration or the network connection, or try again. |
| 17 | Protocol error. The server returns a 4XX or 5XX status code. Verify the parameter configuration and try again. |
| 20 | Other errors. Verify the parameter configuration or the network connection, or try again. |

#### File

Describes the list of files in [UploadConfig](#uploadconfig).

**System capability**: SystemCapability.MiscServices.Download

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| filename | string | No | No | File name in the header when **multipart** is used. |
| name | string | No | No | Name of a form item when **multipart** is used. The default value is **file**. |
| uri | string | No | No | 
Local path for storing files.

Only **internal://cache/** is supported, that is, **context.cacheDir** of the caller (namely, cache directory of the input **context**).

Example: **internal://cache/path/to/file.txt**.

 |
| type | string | No | No | Type of the file content. By default, the type is obtained based on the extension of the file name or URI. |

#### RequestData

Describes the form data in [UploadConfig](#uploadconfig).

**System capability**: SystemCapability.MiscServices.Download

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| name | string | No | No | Name of a form element. |
| value | string | No | No | Value of a form element. |

#### request.downloadFile9+

downloadFile(context: BaseContext, config: DownloadConfig): Promise<DownloadTask>

Downloads a file. This API uses a promise to return the result. HTTP is supported. You can use [on('complete'|'pause'|'remove')](#oncompletepauseremove7) to obtain the download task state, including task completion, pause, and removal. You can also use [on('fail')](#onfail7) to obtain the task download error information.

**Required permissions**: ohos.permission.INTERNET

**System capability**: SystemCapability.MiscServices.Download

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/pYnxvNzSQPKcJhBn5jnyqQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A183918ECEE97AACD55484C3018EC63DB4B05C35D73E209B69476288EF514F73)

For details about how to obtain the context in the example, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | [BaseContext](../../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/basecontext/document.md) | Yes | Application-based context. |
| config | [DownloadConfig](#downloadconfig) | Yes | Download configuration. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[DownloadTask](#downloadtask)\> | Promise used to return the **DownloadTask** object. |

**Error codes**

For details about the error codes, see [Upload and Download Error Codes](../../../error-codes/upload-and-download-error-codes/document.md) and [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | The permissions check fails. |
| 401 | The parameters check fails. Possible causes: 1. Missing mandatory parameters. 2. Incorrect parameter type. 3. Parameter verification failed. |
| 13400001 | Invalid file or file system error. |
| 13400002 | File path not supported or invalid. |
| 13400003 | Task service ability error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
try {
  // Replace the URL with the HTTP address of the real server.
  request.downloadFile(context, { url: 'https://xxxx/xxxx.hap' }).then((data: request.DownloadTask) => {
     let downloadTask: request.DownloadTask = data;
  }).catch((err: BusinessError) => {
    console.error(\`Failed to request the download. Code: ${err.code}, message: ${err.message}\`);
  })
} catch (err) {
  console.error(\`Failed to request the download. Code: ${err.code}, message: ${err.message}\`);
}

#### request.downloadFile9+

downloadFile(context: BaseContext, config: DownloadConfig, callback: AsyncCallback<DownloadTask>): void

Downloads a file. This API uses an asynchronous callback to return the result. HTTP is supported. You can use [on('complete'|'pause'|'remove')](#oncompletepauseremove7) to obtain the download task state, including task completion, pause, and removal. You can also use [on('fail')](#onfail7) to obtain the task download error information.

**Required permissions**: ohos.permission.INTERNET

**System capability**: SystemCapability.MiscServices.Download

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/yX7lvaWqSBeG_j12NI5PCQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EE31351CD813805014912FB5BC5C2EB273CAEFD2CAB2D323C286608B2B1D7101)

For details about how to obtain the context in the example, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | [BaseContext](../../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/basecontext/document.md) | Yes | Application-based context. |
| config | [DownloadConfig](#downloadconfig) | Yes | Download configuration. |
| callback | AsyncCallback<[DownloadTask](#downloadtask)\> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the **DownloadTask** object obtained. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Upload and Download Error Codes](../../../error-codes/upload-and-download-error-codes/document.md) and [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | The permissions check fails. |
| 401 | The parameters check fails. Possible causes: 1. Missing mandatory parameters. 2. Incorrect parameter type. 3. Parameter verification failed. |
| 13400001 | Invalid file or file system error. |
| 13400002 | File path not supported or invalid. |
| 13400003 | Task service ability error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
try {
  // Replace the URL with the HTTP address of the real server.
  request.downloadFile(context, {
    url: 'https://xxxx/xxxxx.hap',
    filePath: 'xxx/xxxxx.hap'
  }, (err: BusinessError, data: request.DownloadTask) => {
    if (err) {
      console.error(\`Failed to request the download. Code: ${err.code}, message: ${err.message}\`);
      return;
    }
  });
} catch (err) {
  console.error(\`Failed to request the download. Code: ${err.code}, message: ${err.message}\`);
}

#### request.download(deprecated)

download(config: DownloadConfig): Promise<DownloadTask>

Download files. This API uses a promise to return the result.

**Model restriction**: This API can be used only in the FA model.

**Required permissions**: ohos.permission.INTERNET

**System capability**: SystemCapability.MiscServices.Download

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/0Knlipf6RjevBSsthsptHA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=27D87E997388264D2E08DA301786B8D79D2C9E3662256AC47B02112FE4A5FD3E)

This API is supported since API version 6 and deprecated since API version 9. You are advised to use [request.downloadFile](#requestdownloadfile9) instead.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| config | [DownloadConfig](#downloadconfig) | Yes | Download configuration. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[DownloadTask](#downloadtask)\> | Promise used to return the **DownloadTask** object. |

**Error codes**

For details about the error codes, see [Upload and Download Error Codes](../../../error-codes/upload-and-download-error-codes/document.md) and [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | The permissions check fails. |

**Example**

let downloadTask: request.DownloadTask;
// Replace the URL with the HTTP address of the real server.
request.download({ url: 'https://xxxx/xxxx.hap' }).then((data: request.DownloadTask) => {
  downloadTask = data;
}).catch((err: BusinessError) => {
  console.error(\`Failed to request the download. Code: ${err.code}, message: ${err.message}\`);
})

#### request.download(deprecated)

download(config: DownloadConfig, callback: AsyncCallback<DownloadTask>): void

Downloads files. This API uses an asynchronous callback to return the result.

**Model restriction**: This API can be used only in the FA model.

**Required permissions**: ohos.permission.INTERNET

**System capability**: SystemCapability.MiscServices.Download

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/SeseD4AQQby3pFQsqCLU6g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=34A14994DB1E3145D4950194C8FD452466196216663BD843B1409943F1311BAA)

This API is supported since API version 6 and deprecated since API version 9. You are advised to use [request.downloadFile](#requestdownloadfile9-1) instead.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| config | [DownloadConfig](#downloadconfig) | Yes | Download configuration. |
| callback | AsyncCallback<[DownloadTask](#downloadtask)\> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the **DownloadTask** object obtained. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Upload and Download Error Codes](../../../error-codes/upload-and-download-error-codes/document.md) and [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | The permissions check fails. |

**Example**

let downloadTask: request.DownloadTask;
// Replace the URL with the HTTP address of the real server.
request.download({ url: 'https://xxxx/xxxxx.hap',
filePath: 'xxx/xxxxx.hap'}, (err: BusinessError, data: request.DownloadTask) => {
  if (err) {
    console.error(\`Failed to request the download. Code: ${err.code}, message: ${err.message}\`);
    return;
  }
  downloadTask = data;
});

#### DownloadTask

Implements file downloads. Before using any APIs of this class, you must obtain a **DownloadTask** object, from a promise through [request.downloadFile](#requestdownloadfile9) or from a callback through [request.downloadFile](#requestdownloadfile9-1).

#### \[h2\]on('progress')

on(type: 'progress', callback: (receivedSize: number, totalSize: number) => void): void

Subscribes to download progress events. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.MiscServices.Download

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/5q7V8ojTR06X-eO09WsMJQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=57BB8E03B867A2A3CCD97982DAA39F60A1030DD7796F0F0E828BA03A6252F575)

To maintain a balance between power consumption and performance, this API cannot be called when the application is running in the background.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type.

\- **'progress'**: download progress.

 |
| callback | function | Yes | Callback used to return the size of the uploaded file and the total size of the file to upload. |

Parameters of the callback function

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| receivedSize | number | Yes | Current download progress, in bytes. |
| totalSize | number | Yes | Total size of the files to download, in bytes. If the server uses the chunk mode for data transmission and the total file size cannot be obtained from the request header, the value of **totalSize** is treated as **\-1**. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | The parameters check fails. Possible causes: 1. Missing mandatory parameters. 2. Incorrect parameter type. 3. Parameter verification failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
try {
  // Replace the URL with the HTTP address of the real server.
  request.downloadFile(context, { url: 'https://xxxx/xxxx.hap' }).then((data: request.DownloadTask) => {
    let downloadTask: request.DownloadTask = data;
    let progressCallback = (receivedSize: number, totalSize: number) => {
      console.info("download receivedSize:" + receivedSize + " totalSize:" + totalSize);
    };
    downloadTask.on('progress', progressCallback);
  }).catch((err: BusinessError) => {
    console.error(\`Failed to request the download. Code: ${err.code}, message: ${err.message}\`);
  })
} catch (err) {
  console.error(\`Failed to request the download. Code: ${err.code}, message: ${err.message}\`);
}

#### \[h2\]off('progress')

off(type: 'progress', callback?: (receivedSize: number, totalSize: number) => void): void

Unsubscribes from download progress events.

**System capability**: SystemCapability.MiscServices.Download

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type.

\- **'progress'**: download progress.

 |
| callback | function | No | Callback to unregister. If this parameter is not specified, all callbacks of the current type will be unregistered. |

Parameters of the callback function

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| receivedSize | number | Yes | Current download progress, in bytes. |
| totalSize | number | Yes | Total size of the files to download, in bytes. If the server uses the chunk mode for data transmission and the total file size cannot be obtained from the request header, the value of **totalSize** is treated as **\-1**. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | The parameters check fails. Possible causes: 1. Missing mandatory parameters. 2. Incorrect parameter type. 3. Parameter verification failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
try {
  // Replace the URL with the HTTP address of the real server.
  request.downloadFile(context, { url: 'https://xxxx/xxxx.hap' }).then((data: request.DownloadTask) => {
    let downloadTask: request.DownloadTask = data;
    let progressCallback1 = (receivedSize: number, totalSize: number) => {
      console.info('Download delete progress notification.' + 'receivedSize:' + receivedSize + 'totalSize:' + totalSize);
    };
    let progressCallback2 = (receivedSize: number, totalSize: number) => {
      console.info('Download delete progress notification.' + 'receivedSize:' + receivedSize + 'totalSize:' + totalSize);
    };
    downloadTask.on('progress', progressCallback1);
    downloadTask.on('progress', progressCallback2);
    // Unsubscribe from progressCallback1.
    downloadTask.off('progress', progressCallback1);
    // Unsubscribe from all callbacks of download progress events.
    downloadTask.off('progress');
  }).catch((err: BusinessError) => {
    console.error(\`Failed to request the download. Code: ${err.code}, message: ${err.message}\`);
  })
} catch (err) {
  console.error(\`Failed to request the download. Code: ${err.code}, message: ${err.message}\`);
}

#### \[h2\]on('complete'|'pause'|'remove')7+

on(type: 'complete'|'pause'|'remove', callback: () => void): void

Subscribes to download events. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.MiscServices.Download

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type.

\- **'complete'**: download task completion.

\- **'pause'**: download task pause.

\- **'remove'**: download task removal.

 |
| callback | function | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | The parameters check fails. Possible causes: 1. Missing mandatory parameters. 2. Incorrect parameter type. 3. Parameter verification failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
try {
  // Replace the URL with the HTTP address of the real server.
  request.downloadFile(context, { url: 'https://xxxx/xxxx.hap' }).then((data: request.DownloadTask) => {
    let downloadTask: request.DownloadTask = data;
    let completeCallback = () => {
      console.info('Download task completed.');
    };
    downloadTask.on('complete', completeCallback);

    let pauseCallback = () => {
      console.info('Download task pause.');
    };
    downloadTask.on('pause', pauseCallback);

    let removeCallback = () => {
      console.info('Download task remove.');
    };
    downloadTask.on('remove', removeCallback);
  }).catch((err: BusinessError) => {
    console.error(\`Failed to request the download. Code: ${err.code}, message: ${err.message}\`);
  })
} catch (err) {
  console.error(\`Failed to request the download. Code: ${err.code}, message: ${err.message}\`);
}

#### \[h2\]off('complete'|'pause'|'remove')7+

off(type: 'complete'|'pause'|'remove', callback?: () => void): void

Unsubscribes from download events.

**System capability**: SystemCapability.MiscServices.Download

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type.

\- **'complete'**: download task completion.

\- **'pause'**: download task pause.

\- **'remove'**: download task removal.

 |
| callback | function | No | Callback to unregister. If this parameter is not specified, all callbacks of the current type will be unregistered. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | The parameters check fails. Possible causes: 1. Missing mandatory parameters. 2. Incorrect parameter type. 3. Parameter verification failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
try {
  // Replace the URL with the HTTP address of the real server.
  request.downloadFile(context, { url: 'https://xxxx/xxxx.hap' }).then((data: request.DownloadTask) => {
    let downloadTask: request.DownloadTask = data;
    let completeCallback1 = () => {
      console.info('Download delete complete notification.');
    };
    let completeCallback2 = () => {
      console.info('Download delete complete notification.');
    };
    downloadTask.on('complete', completeCallback1);
    downloadTask.on('complete', completeCallback2);
    // Unsubscribe from completeCallback1.
    downloadTask.off('complete', completeCallback1);
    // Unsubscribe from all callbacks of the download completion events.
    downloadTask.off('complete');

    let pauseCallback1 = () => {
      console.info('Download delete pause notification.');
    };
    let pauseCallback2 = () => {
      console.info('Download delete pause notification.');
    };
    downloadTask.on('pause', pauseCallback1);
    downloadTask.on('pause', pauseCallback2);
    // Unsubscribe from pauseCallback1.
    downloadTask.off('pause', pauseCallback1);
    // Unsubscribe from all callbacks of the download pause events.
    downloadTask.off('pause');

    let removeCallback1 = () => {
      console.info('Download delete remove notification.');
    };
    let removeCallback2 = () => {
      console.info('Download delete remove notification.');
    };
    downloadTask.on('remove', removeCallback1);
    downloadTask.on('remove', removeCallback2);
    // Unsubscribe from removeCallback1.
    downloadTask.off('remove', removeCallback1);
    // Unsubscribe from all callbacks of the download removal events.
    downloadTask.off('remove');
  }).catch((err: BusinessError) => {
    console.error(\`Failed to request the download. Code: ${err.code}, message: ${err.message}\`);
  })
} catch (err) {
  console.error(\`Failed to request the download. Code: ${err.code}, message: ${err.message}\`);
}

#### \[h2\]on('fail')7+

on(type: 'fail', callback: (err: number) => void): void

Subscribes to download failure events. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.MiscServices.Download

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type.

\- **'fail'**: download task failure.

 |
| callback | function | Yes | Callback for the download task failure event. |

Parameters of the callback function

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| err | number | Yes | Error code of the download failure. For details about the error codes, see [Download Error Codes](#constants). |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | The parameters check fails. Possible causes: 1. Missing mandatory parameters. 2. Incorrect parameter type. 3. Parameter verification failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
try {
  // Replace the URL with the HTTP address of the real server.
  request.downloadFile(context, { url: 'https://xxxx/xxxx.hap' }).then((data: request.DownloadTask) => {
    let downloadTask: request.DownloadTask = data;
    let failCallback = (err: number) => {
      console.error(\`Failed to download the task. Code: ${err}\`);
    };
    downloadTask.on('fail', failCallback);
  }).catch((err: BusinessError) => {
    console.error(\`Failed to request the download. Code: ${err.code}, message: ${err.message}\`);
  })
} catch (err) {
  console.error(\`Failed to request the download. Code: ${err.code}, message: ${err.message}\`);
}

#### \[h2\]off('fail')7+

off(type: 'fail', callback?: (err: number) => void): void

Unsubscribes from download failure events.

**System capability**: SystemCapability.MiscServices.Download

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type.

\- **'fail'**: download task failure.

 |
| callback | function | No | Callback to unregister. If this parameter is not specified, all callbacks of the current type will be unregistered. |

Parameters of the callback function

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| err | number | Yes | Error code of the download failure. For details about the error codes, see [Download Error Codes](#constants). |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | The parameters check fails. Possible causes: 1. Missing mandatory parameters. 2. Incorrect parameter type. 3. Parameter verification failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
try {
  // Replace the URL with the HTTP address of the real server.
  request.downloadFile(context, { url: 'https://xxxx/xxxx.hap' }).then((data: request.DownloadTask) => {
    let downloadTask: request.DownloadTask = data;
    let failCallback1 = (err: number) => {
      console.error(\`Failed to download the task. Code: ${err}\`);
    };
    let failCallback2 = (err: number) => {
      console.error(\`Failed to download the task. Code: ${err}\`);
    };
    downloadTask.on('fail', failCallback1);
    downloadTask.on('fail', failCallback2);
    // Unsubscribe from failCallback1.
    downloadTask.off('fail', failCallback1);
    // Unsubscribe from all callbacks of the download failure events.
    downloadTask.off('fail');
  }).catch((err: BusinessError) => {
    console.error(\`Failed to request the download. Code: ${err.code}, message: ${err.message}\`);
  })
} catch (err) {
  console.error(\`Failed to request the download. Code: ${err.code}, message: ${err.message}\`);
}

#### \[h2\]delete9+

delete(): Promise<boolean>

Deletes this download task. This API uses a promise to return the result.

**Required permissions**: ohos.permission.INTERNET

**System capability**: SystemCapability.MiscServices.Download

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/JON7nMtKRKK1JfEuS2dgQw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7F959B04CE72E571F5B3BD48C625969AB3694BA8203637322474A1184009388F)

The scenarios for triggering error code **401 the parameters check fails** do not exist. Therefore, this error code is removed from API version 12.

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return the result. The value **true** indicates that the operation is successful; **false** indicates the opposite. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | The permissions check fails. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
try {
  // Replace the URL with the HTTP address of the real server.
  request.downloadFile(context, { url: 'https://xxxx/xxxx.hap' }).then((data: request.DownloadTask) => {
    data.delete().then((result: boolean) => {
      console.info('Succeeded in removing the download task.');
    }).catch((err: BusinessError) => {
      console.error(\`Failed to remove the download task. Code: ${err.code}, message: ${err.message}\`);
    });
  }).catch((err: BusinessError) => {
    console.error(\`Failed to request the download. Code: ${err.code}, message: ${err.message}\`);
  })
} catch (err) {
  console.error(\`Failed to request the download. Code: ${err.code}, message: ${err.message}\`);
}

#### \[h2\]delete9+

delete(callback: AsyncCallback<boolean>): void

Deletes a download task. This API uses an asynchronous callback to return the result.

**Required permissions**: ohos.permission.INTERNET

**System capability**: SystemCapability.MiscServices.Download

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/War4c3lrQHaAg5IU7O6yyA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7010757AC7BE8E91C94DEB8EF6329295EA28921FA5A73370ABC1C4731F9F5B01)

The scenarios for triggering error code **401 the parameters check fails** do not exist. Therefore, this error code is removed from API version 12.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<boolean> | Yes | Callback used to return the result. The value **true** indicates that the operation is successful; **false** indicates the opposite. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | The permissions check fails. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
try {
  // Replace the URL with the HTTP address of the real server.
  request.downloadFile(context, { url: 'https://xxxx/xxxx.hap' }).then((data: request.DownloadTask) => {
    let downloadTask: request.DownloadTask = data;
    downloadTask.delete((err: BusinessError, result: boolean) => {
      if (err) {
        console.error(\`Failed to remove the download task. Code: ${err.code}, message: ${err.message}\`);
        return;
      }
      console.info('Succeeded in removing the download task.');
    });
  }).catch((err: BusinessError) => {
    console.error(\`Failed to request the download. Code: ${err.code}, message: ${err.message}\`);
  })
} catch (err) {
  console.error(\`Failed to request the download. Code: ${err.code}, message: ${err.message}\`);
}

#### \[h2\]getTaskInfo9+

getTaskInfo(): Promise<DownloadInfo>

Obtains the information about this download task. This API uses a promise to return the result.

**Required permissions**: ohos.permission.INTERNET

**System capability**: SystemCapability.MiscServices.Download

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/vUFi8reTSL-JJOWfGy-7BA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=ECB94DFB03F2FEE77279DA7239751D556B1FF1E5502D3EDE8F2B9AF199FD44FB)

The scenarios for triggering error code **401 the parameters check fails** do not exist. Therefore, this error code is removed from API version 12.

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[DownloadInfo](#downloadinfo7)\> | Promise used to return a **DownloadInfo** object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | The permissions check fails. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
try {
  // Replace the URL with the HTTP address of the real server.
  request.downloadFile(context, { url: 'https://xxxx/xxxx.hap' }).then((data: request.DownloadTask) => {
    let downloadTask: request.DownloadTask = data;
    downloadTask.getTaskInfo().then((downloadInfo: request.DownloadInfo) => {
      console.info('Succeeded in querying the download task')
    }).catch((err: BusinessError) => {
      console.error(\`Failed to query the download task. Code: ${err.code}, message: ${err.message}\`)
    });
  }).catch((err: BusinessError) => {
    console.error(\`Failed to request the download. Code: ${err.code}, message: ${err.message}\`);
  })
} catch (err) {
  console.error(\`Failed to request the download. Code: ${err.code}, message: ${err.message}\`);
}

#### \[h2\]getTaskInfo9+

getTaskInfo(callback: AsyncCallback<DownloadInfo>): void

Obtains the information about this download task. This API uses an asynchronous callback to return the result.

**Required permissions**: ohos.permission.INTERNET

**System capability**: SystemCapability.MiscServices.Download

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/eA-_mn33QCK1yM6B3_Gw6A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2D5F829CC4D54725F752955DB5DBFC5A3986EBE32BA8DCA7246BFCBD9329E4E0)

The scenarios for triggering error code **401 the parameters check fails** do not exist. Therefore, this error code is removed from API version 12.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[DownloadInfo](#downloadinfo7)\> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the **DownloadInfo** object obtained. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | The permissions check fails. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
try {
  // Replace the URL with the HTTP address of the real server.
  request.downloadFile(context, { url: 'https://xxxx/xxxx.hap' }).then((data: request.DownloadTask) => {
    let downloadTask: request.DownloadTask = data;
    downloadTask.getTaskInfo((err: BusinessError, downloadInfo: request.DownloadInfo) => {
      if (err) {
        console.error(\`Failed to query the download mimeType. Code: ${err.code}, message: ${err.message}\`);
      } else {
        console.info('Succeeded in querying the download mimeType');
      }
    });
  }).catch((err: BusinessError) => {
    console.error(\`Failed to request the download. Code: ${err.code}, message: ${err.message}\`);
  })
} catch (err) {
  console.error(\`Failed to request the download. Code: ${err.code}, message: ${err.message}\`);
}

#### \[h2\]getTaskMimeType9+

getTaskMimeType(): Promise<string>

Obtains the MIME type (that is, media type of resources in HTTP) of a download task. This API uses a promise to return the result.

**Required permissions**: ohos.permission.INTERNET

**System capability**: SystemCapability.MiscServices.Download

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/U54q5ZotQFKGEqT9XzCTbQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A2947B450230EED0603733386BDA742DC59546A741012CD096CFA778380CC12D)

The scenarios for triggering error code **401 the parameters check fails** do not exist. Therefore, this error code is removed from API version 12.

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<string> | Promise used to return the MIME type of a download task. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | The permissions check fails. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
try {
  // Replace the URL with the HTTP address of the real server.
  request.downloadFile(context, { url: 'https://xxxx/xxxx.hap' }).then((data: request.DownloadTask) => {
    let downloadTask: request.DownloadTask = data;
    downloadTask.getTaskMimeType().then((data: string) => {
      console.info('Succeeded in querying the download MimeType');
    }).catch((err: BusinessError) => {
      console.error(\`Failed to query the download MimeType. Code: ${err.code}, message: ${err.message}\`)
    });
  }).catch((err: BusinessError) => {
    console.error(\`Failed to request the download. Code: ${err.code}, message: ${err.message}\`);
  })
} catch (err) {
  console.error(\`Failed to request the download. Code: ${err.code}, message: ${err.message}\`);
}

#### \[h2\]getTaskMimeType9+

getTaskMimeType(callback: AsyncCallback<string>): void

Obtains the MIME type (that is, media type of resources in HTTP) of a download task. This API uses an asynchronous callback to return the result.

**Required permissions**: ohos.permission.INTERNET

**System capability**: SystemCapability.MiscServices.Download

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/vwuhJa1GTZu_zp-gkh3CsQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0671540A7675A7FF5F558A337A9520E727EDAF0B78FD367FD522A11A5CD17C72)

The scenarios for triggering error code **401 the parameters check fails** do not exist. Therefore, this error code is removed from API version 12.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<string> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and data is the **MimeType** object obtained. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | The permissions check fails. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
try {
  // Replace the URL with the HTTP address of the real server.
  request.downloadFile(context, { url: 'https://xxxx/xxxx.hap' }).then((data: request.DownloadTask) => {
    let downloadTask: request.DownloadTask = data;
    downloadTask.getTaskMimeType((err: BusinessError, data: string) => {
      if (err) {
        console.error(\`Failed to query the download mimeType. Code: ${err.code}, message: ${err.message}\`);
      } else {
        console.info('Succeeded in querying the download mimeType');
      }
    });
  }).catch((err: BusinessError) => {
    console.error(\`Failed to request the download. Code: ${err.code}, message: ${err.message}\`);
  })
} catch (err) {
  console.error(\`Failed to request the download. Code: ${err.code}, message: ${err.message}\`);
}

#### \[h2\]suspend9+

suspend(): Promise<boolean>

Suspends this download task. You can use [restore](#restore9) to restore the download. This API uses a promise to return the result.

**Required permissions**: ohos.permission.INTERNET

**System capability**: SystemCapability.MiscServices.Download

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/eJZyAMHgRea9HxprtLn62A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8327F0388A1398A9F837A6D83BD9223B67B0543CDC2C5F4CA58C2FD763EE7413)

The scenarios for triggering error code **401 the parameters check fails** do not exist. Therefore, this error code is removed from API version 12.

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return the result. The value **true** indicates that the operation is successful; **false** indicates the opposite. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | The permissions check fails. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
try {
  // Replace the URL with the HTTP address of the real server.
  request.downloadFile(context, { url: 'https://xxxx/xxxx.hap' }).then((data: request.DownloadTask) => {
    let downloadTask: request.DownloadTask = data;
    downloadTask.suspend().then((result: boolean) => {
      console.info('Succeeded in pausing the download task.');
    }).catch((err: BusinessError) => {
      console.error(\`Failed to pause the download task. Code: ${err.code}, message: ${err.message}\`);
    });
  }).catch((err: BusinessError) => {
    console.error(\`Failed to request the download. Code: ${err.code}, message: ${err.message}\`);
  })
} catch (err) {
  console.error(\`Failed to request the download. Code: ${err.code}, message: ${err.message}\`);
}

#### \[h2\]suspend9+

suspend(callback: AsyncCallback<boolean>): void

Suspends this download task. You can use [restore](#restore9) to restore the download. This API uses an asynchronous callback to return the result.

**Required permissions**: ohos.permission.INTERNET

**System capability**: SystemCapability.MiscServices.Download

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/-2E1TbYPR4-r85hq7YTjhg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5309EE31C233C00F9AD8BD60850158723F879D17A6425AD4FA7A116BD0373746)

The scenarios for triggering error code **401 the parameters check fails** do not exist. Therefore, this error code is removed from API version 12.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<boolean> | Yes | Callback used to return the result. The value **true** indicates that the operation is successful; **false** indicates the opposite. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | The permissions check fails. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
try {
  // Replace the URL with the HTTP address of the real server.
  request.downloadFile(context, { url: 'https://xxxx/xxxx.hap' }).then((data: request.DownloadTask) => {
    let downloadTask: request.DownloadTask = data;
    downloadTask.suspend((err: BusinessError, result: boolean) => {
      if (err) {
        console.error(\`Failed to pause the download task. Code: ${err.code}, message: ${err.message}\`);
        return;
      }
      console.info('Succeeded in pausing the download task.');
    });
  }).catch((err: BusinessError) => {
    console.error(\`Failed to request the download. Code: ${err.code}, message: ${err.message}\`);
  })
} catch (err) {
  console.error(\`Failed to request the download. Code: ${err.code}, message: ${err.message}\`);
}

#### \[h2\]restore9+

restore(): Promise<boolean>

Restores this download task. This API uses a promise to return the result.

**Required permissions**: ohos.permission.INTERNET

**System capability**: SystemCapability.MiscServices.Download

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/tlBwXL0lTC229E4LZxI-cw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FD561ED9DB556C703B94704CF6BCFABBA4D90112B653F8787CFDA9CEFE9E2534)

The scenarios for triggering error code **401 the parameters check fails** do not exist. Therefore, this error code is removed from API version 12.

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return the result. The value **true** indicates that the operation is successful; **false** indicates the opposite. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | The permissions check fails. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
try {
  // Replace the URL with the HTTP address of the real server.
  request.downloadFile(context, { url: 'https://xxxx/xxxx.hap' }).then((data: request.DownloadTask) => {
    let downloadTask: request.DownloadTask = data;
    downloadTask.restore().then((result: boolean) => {
      console.info('Succeeded in resuming the download task.')
    }).catch((err: BusinessError) => {
      console.error(\`Failed to resume the download task. Code: ${err.code}, message: ${err.message}\`);
    });
  }).catch((err: BusinessError) => {
    console.error(\`Failed to request the download. Code: ${err.code}, message: ${err.message}\`);
  })
} catch (err) {
  console.error(\`Failed to request the download. Code: ${err.code}, message: ${err.message}\`);
}

#### \[h2\]restore9+

restore(callback: AsyncCallback<boolean>): void

Restores a download task. This API uses an asynchronous callback to return the result.

**Required permissions**: ohos.permission.INTERNET

**System capability**: SystemCapability.MiscServices.Download

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/ICMNHupiTzip_mQRSljWuA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=582DC9B1EDFADF284B9DBE5C3083C9B59ADC22A4D9779344FC3EEF73FBF9EC1A)

The scenarios for triggering error code **401 the parameters check fails** do not exist. Therefore, this error code is removed from API version 12.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<boolean> | Yes | Callback used to return the result. The value **true** indicates that the operation is successful; **false** indicates the opposite. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | The permissions check fails. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
try {
  // Replace the URL with the HTTP address of the real server.
  request.downloadFile(context, { url: 'https://xxxx/xxxx.hap' }).then((data: request.DownloadTask) => {
    let downloadTask: request.DownloadTask = data;
    downloadTask.restore((err: BusinessError, result: boolean) => {
      if (err) {
        console.error(\`Failed to resume the download task. Code: ${err.code}, message: ${err.message}\`);
        return;
      }
      console.info('Succeeded in resuming the download task.');
    });
  }).catch((err: BusinessError) => {
    console.error(\`Failed to request the download. Code: ${err.code}, message: ${err.message}\`);
  })
} catch (err) {
  console.error(\`Failed to request the download. Code: ${err.code}, message: ${err.message}\`);
}

#### \[h2\]remove(deprecated)

remove(): Promise<boolean>

Removes this download task. This API uses a promise to return the result.

**Required permissions**: ohos.permission.INTERNET

**System capability**: SystemCapability.MiscServices.Download

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/-bCqq3gKRHyy5-Nndxps6Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7C09A0F918D98AD115348F8F289CB74CF2076EA6D7FC8AC2A6C27AEC0A2AEC47)

This API is supported since API version 6 and deprecated since API version 9. You are advised to use [delete](#delete9-2) instead.

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return the result. The value **true** indicates that the operation is successful; **false** indicates the opposite. |

**Error codes**

For details about the error codes, see [Upload and Download Error Codes](../../../error-codes/upload-and-download-error-codes/document.md) and [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | The permissions check fails. |

**Example**

downloadTask.remove().then((result) => {
  console.info('Succeeded in removing the download task.');
}).catch ((err: BusinessError) => {
  console.error(\`Failed to remove the download task. Code: ${err.code}, message: ${err.message}\`);
});

#### \[h2\]remove(deprecated)

remove(callback: AsyncCallback<boolean>): void

Removes a download task. This API uses an asynchronous callback to return the result.

**Required permissions**: ohos.permission.INTERNET

**System capability**: SystemCapability.MiscServices.Download

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/LSvWpHwrRKGP1DHNBwo8dQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=182289D7B849810D695469D93F15DC15D38E90B932EF3586A65B8A37903541C5)

This API is supported since API version 6 and deprecated since API version 9. You are advised to use [delete](#delete9-3) instead.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<boolean> | Yes | Callback used to return the result. The value **true** indicates that the operation is successful; **false** indicates the opposite. |

**Error codes**

For details about the error codes, see [Upload and Download Error Codes](../../../error-codes/upload-and-download-error-codes/document.md) and [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | The permissions check fails. |

**Example**

downloadTask.remove((err, result)=>{
  if(err) {
    console.error(\`Failed to remove the download task. Code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info('Succeeded in removing the download task.');
});

#### \[h2\]query(deprecated)

query(): Promise<DownloadInfo>

Queries this download task. This API uses a promise to return the result.

**Required permissions**: ohos.permission.INTERNET

**System capability**: SystemCapability.MiscServices.Download

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/dA9_mPcKRLqQx1KUwEq4vg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BCB5ECCC47D69448D3F37686770C3E70D4C09DEE02FCFBBB6B91C8CC166469BC)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [getTaskInfo](#gettaskinfo9) instead.

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[DownloadInfo](#downloadinfo7)\> | Promise used to return the **DownloadInfo** object. |

**Error codes**

For details about the error codes, see [Upload and Download Error Codes](../../../error-codes/upload-and-download-error-codes/document.md) and [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | The permissions check fails. |

**Example**

downloadTask.query().then((downloadInfo) => {
  console.info('Succeeded in querying the download task.')
}).catch((err: BusinessError) => {
  console.error(\`Failed to query the download task. Code: ${err.code}, message: ${err.message}\`)
});

#### \[h2\]query(deprecated)

query(callback: AsyncCallback<DownloadInfo>): void

Queries this download task. This API uses an asynchronous callback to return the result.

**Required permissions**: ohos.permission.INTERNET

**System capability**: SystemCapability.MiscServices.Download

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/3Q_uzyONRkqk3GGAQiZGpw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E2DFD0A3F07033DF3C884B9BB693122CCA02E0C1667700A1F1F8E51591D96207)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [getTaskInfo](#gettaskinfo9-1) instead.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[DownloadInfo](#downloadinfo7)\> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the **DownloadInfo** object obtained. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Upload and Download Error Codes](../../../error-codes/upload-and-download-error-codes/document.md) and [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | The permissions check fails. |

**Example**

downloadTask.query((err: BusinessError, downloadInfo: request.DownloadInfo)=>{
  if(err) {
    console.error(\`Failed to query the download mimeType. Code: ${err.code}, message: ${err.message}\`);
  } else {
    console.info('Succeeded in querying the download task.');
  }
});

#### \[h2\]queryMimeType(deprecated)

queryMimeType(): Promise<string>

Queries the MIME type of this download task. This API uses a promise to return the result.

**Required permissions**: ohos.permission.INTERNET

**System capability**: SystemCapability.MiscServices.Download

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/NvgGbFufRpiH0QcHwmk4Dw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B91025D50E932E10DFBFD055A4454E9E3794E9702BF3F0AFD5DB64F8FA239BE2)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [getTaskMimeType](#gettaskmimetype9) instead.

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<string> | Promise used to return the MIME type of a download task. |

**Error codes**

For details about the error codes, see [Upload and Download Error Codes](../../../error-codes/upload-and-download-error-codes/document.md) and [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | The permissions check fails. |

**Example**

downloadTask.queryMimeType().then((data: string) => {
  console.info('Succeeded in querying the download MimeType.');
}).catch((err: BusinessError) => {
  console.error(\`Failed to query the download MimeType. Code: ${err.code}, message: ${err.message}\`)
});

#### \[h2\]queryMimeType(deprecated)

queryMimeType(callback: AsyncCallback<string>): void

Queries the MIME type of this download task. This API uses an asynchronous callback to return the result.

**Required permissions**: ohos.permission.INTERNET

**System capability**: SystemCapability.MiscServices.Download

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/XLnh7UXjQuKKnwiAFYN2Pw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6478018762B8CF4149612EA2EAA90A77DEC317264160CE23AF37A468BD76E9FE)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [getTaskMimeType](#gettaskmimetype9-1) instead.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<string> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and data is the **MimeType** object obtained. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Upload and Download Error Codes](../../../error-codes/upload-and-download-error-codes/document.md) and [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | The permissions check fails. |

**Example**

downloadTask.queryMimeType((err: BusinessError, data: string)=>{
  if(err) {
    console.error(\`Failed to query the download mimeType. Code: ${err.code}, message: ${err.message}\`);
  } else {
    console.info('Succeeded in querying the download mimeType.');
  }
});

#### \[h2\]pause(deprecated)

pause(): Promise<void>

Pauses this download task. This API uses a promise to return the result.

**Required permissions**: ohos.permission.INTERNET

**System capability**: SystemCapability.MiscServices.Download

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/rePpQhS0TRq0-utKp_iVPA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F451E9732C6BDD5AF54E44C464638F56CFF8EDF0381D735EF32848FBAB445EB6)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [suspend](#suspend9) instead.

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Upload and Download Error Codes](../../../error-codes/upload-and-download-error-codes/document.md) and [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | The permissions check fails. |

**Example**

downloadTask.pause().then(() => {
  console.info('Succeeded in pausing the download task.');
}).catch((err: BusinessError) => {
  console.error(\`Failed to pause the download task. Code: ${err.code}, message: ${err.message}\`);
});

#### \[h2\]pause(deprecated)

pause(callback: AsyncCallback<void>): void

Pauses this download task. This API uses an asynchronous callback to return the result.

**Required permissions**: ohos.permission.INTERNET

**System capability**: SystemCapability.MiscServices.Download

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/vIKFBC-8QT2yJ5HOt18-JA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=633586A7BE4DB57BE0B71A822A382D45D6395B8228A86D4E429AE7D9E35699D8)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [suspend](#suspend9-1) instead.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Upload and Download Error Codes](../../../error-codes/upload-and-download-error-codes/document.md) and [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | The permissions check fails. |

**Example**

downloadTask.pause((err: BusinessError) => {
  if(err) {
    console.error(\`Failed to pause the download task. Code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info('Succeeded in pausing the download task.');
});

#### \[h2\]resume(deprecated)

resume(): Promise<void>

Resumes this download task. This API uses a promise to return the result.

**Required permissions**: ohos.permission.INTERNET

**System capability**: SystemCapability.MiscServices.Download

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/bpH1XRb2RD-jC10vcQVm1g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7CDCD66033DA5EC5B878EC5ED68295EEC5BE8857435DBC2755C7E103F84194A0)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [restore](#restore9) instead.

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Upload and Download Error Codes](../../../error-codes/upload-and-download-error-codes/document.md) and [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | The permissions check fails. |

**Example**

downloadTask.resume().then(() => {
  console.info('Succeeded in resuming the download task.')
}).catch((err: BusinessError) => {
  console.error(\`Failed to resume the download task. Code: ${err.code}, message: ${err.message}\`);
});

#### \[h2\]resume(deprecated)

resume(callback: AsyncCallback<void>): void

Resumes a download task. This API uses an asynchronous callback to return the result.

**Required permissions**: ohos.permission.INTERNET

**System capability**: SystemCapability.MiscServices.Download

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/9xCBSrUoQWCxR1W29xN7_A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=72CDDC06635898484DAFABB8F1B644EB44E5E9C5D5682958DC7864D49999C27E)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [restore](#restore9-1) instead.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Upload and Download Error Codes](../../../error-codes/upload-and-download-error-codes/document.md) and [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | The permissions check fails. |

**Example**

downloadTask.resume((err: BusinessError) => {
  if (err) {
    console.error(\`Failed to resume the download task. Code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info('Succeeded in resuming the download task.');
});

#### DownloadConfig

Defines the download task configuration.

**System capability**: SystemCapability.MiscServices.Download

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| url | string | No | No | Resource URL. From API version 6 to 14, the value contains a maximum of 2048 characters; since API version 15, the value contains a maximum of 8192 characters. [Intercepting HTTP](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-file-upload-download#intercepting-http) is supported. |
| header | Object | No | Yes | HTTPS flag header to be included in the download request. The default value is empty. |
| enableMetered | boolean | No | Yes | 
Whether download is allowed on a metered connection. The value **true** means the download is allowed, and **false** means the opposite. The default value is **false**.

**NOTE**

In general cases, a mobile data connection is metered, while a Wi-Fi connection is not.

 |
| enableRoaming | boolean | No | Yes | Whether download is allowed on a roaming network. The value **true** means the download is allowed, and **false** means the opposite. The default value is **false**. |
| description | string | No | Yes | Description of the download session. The default value is an empty string. |
| filePath7+ | string | No | Yes | 

Path where the downloaded file is stored. The default value is the cache directory of the caller (that is, the input **context**). The default file name is the part truncated from the last slash (/) in the URL.

\- In the FA model, use the [Context.getCacheDir](../../../../../../application-framework/ability-kit/arkts-apis/fa-model/app/context-context-base-class-of-the-fa-model/document.md#contextgetcachedir) method to obtain the application storage path.

\- In the Stage model, use the **AbilityContext** class in [Context (Context Base Class of the Stage Model)](../../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md) to obtain the file path.

 |
| networkType | number | No | Yes | 

Network type that can be used for download. The allowed network type is determined by bitwise operation of [network type constants](#constants). The following settings are supported:

\- Only the cellular network is supported. The parameter is **NETWORK\_MOBILE** or **0x00000001**.

\- Only WLAN is supported. The parameter is **NETWORK\_WIFI** or **0x00010000**.

\- Both cellular network and WLAN are supported, which is the default settings. The parameter is \*\*NETWORK\_MOBILE | **NETWORK\_WIFI** or **0x00010001**.

When the parameter is \*\*NETWORK\_MOBILE | **NETWORK\_WIFI**, the **enableMetered** and **enableRoaming** parameters do not take effect.

 |
| title | string | No | Yes | Download task name. The default value is **download**. |
| background9+ | boolean | No | Yes | Whether to enable the background task notification. When this parameter is enabled, the download status is displayed in the notification panel. The value **true** means the parameter is enabled, and **false** means the opposite. The default value is **false**. |

#### DownloadInfo7+

Defines the download task information, which is the callback parameter of the [getTaskInfo](#gettaskinfo9) API.

**System capability**: SystemCapability.MiscServices.Download

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| downloadId | number | No | No | Download task ID. |
| failedReason | number | No | No | Cause of the download failure. The value can be any constant in [Download Error Codes](#constants). |
| fileName | string | No | No | Name of the downloaded file. |
| filePath | string | No | No | URI of the saved file. |
| pausedReason | number | No | No | Cause of download pause. The value can be any constant in [Causes of Download Pause](#constants). |
| status | number | No | No | Download task status code. The value can be any constant in [Download Task Status Codes](#constants). |
| targetURI | string | No | No | URI of the downloaded file. |
| downloadTitle | string | No | No | Name of the download task. |
| downloadTotalBytes | number | No | No | Total size of the files to download, in bytes. |
| description | string | No | No | Description of the download task. |
| downloadedBytes | number | No | No | Real-time download size, in bytes. |

#### request.agent10+

#### \[h2\]Constants

**System capability**: SystemCapability.Request.FileTransferAgent

| Name | Type | Value | Description |
| :-- | :-- | :-- | :-- |
| VISIBILITY\_COMPLETION21+ | number | 1 | ([Notification](#requestagentnotification15) visibility type) Displays completion notifications. |
| VISIBILITY\_PROGRESS21+ | number | 2 | ([Notification](#requestagentnotification15) visibility type) Displays progress notifications. |

#### request.agent.Action10+

Defines action options.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Request.FileTransferAgent

| Name | Value | Description |
| :-- | :-- | :-- |
| DOWNLOAD | 0 | Download. |
| UPLOAD | 1 | Upload. |

#### request.agent.Mode10+

Defines mode options.

After foreground tasks of an application are switched to the background for a period of time, background tasks are not affected but foreground tasks will fail or pause.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Request.FileTransferAgent

| Name | Value | Description |
| :-- | :-- | :-- |
| BACKGROUND | 0 | Background task. |
| FOREGROUND | 1 | Foreground task. |

#### request.agent.Network10+

Defines network options.

If the network does not meet the preset conditions, the tasks that have not been executed will await for execution, and the tasks that are being executed will fail or pause.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Request.FileTransferAgent

| Name | Value | Description |
| :-- | :-- | :-- |
| ANY | 0 | Network of any type. |
| WIFI | 1 | Wi-Fi network. |
| CELLULAR | 2 | Cellular data network. |

#### request.agent.BroadcastEvent11+

Defines a custom system event. You can use a common event API to obtain the event.

The upload and download SA has the **ohos.permission.SEND\_TASK\_COMPLETE\_EVENT** permission. You can configure the level-2 configuration file to which the metadata of an event points to intercept other event senders.

Use the **CommonEventData** type to transmit data related to common events. The members in **CommonEventData** are different from those described in [CommonEventData](../../process-and-thread-communication/commonevent/commoneventdata/document.md). Specifically, **CommonEventData.code** indicates the task status, which is **0x40 COMPLETE** or **0x41 FAILED**, and **CommonEventData.data** indicates the task ID.

**System capability**: SystemCapability.Request.FileTransferAgent

| Name | Value | Description |
| :-- | :-- | :-- |
| COMPLETE | ohos.request.event.COMPLETE | Task completion event. The returned event code can be **0x40** or **0x41**, depending on whether the task is successful or fails. |

#### request.agent.FileSpec10+

Provides the file information of a table item.

**System capability**: SystemCapability.Request.FileTransferAgent

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| path | string | No | No | 
File path.

\- Relative path, which is in the cache directory of the caller.

Example: **./xxx/yyy/zzz.html** or **xxx/yyy/zzz.html**

\- Internal protocol path, which can be **internal://** or its subdirectory. **internal** indicates the cache directory of the caller (that is, the input **context**), and **internal://cache** corresponds to **context.cacheDir**.

Example: **internal://cache/path/to/file.txt**

\- Application sandbox directory. Only the **base** directory and its subdirectories are supported.

Example: **/data/storage/el1/base/path/to/file.txt**

\- File protocol path, which must match the application bundle name. Only the **base** directory and its subdirectories are supported.

Example: **file://com.example.test/data/storage/el2/base/file.txt**

\- Public files of users. Only upload tasks are supported.

Example: **file://media/Photo/path/to/file.img**. Only foreground tasks are supported.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| mimeType(deprecated) | string | No | Yes | 

MIME type of the file, which is obtained from the file name. The default value is the file name extension.

**Atomic service API**: This API can be used in atomic services since API version 11.

This API is deprecated since API version 18. You are advised to use **contentType** instead.

 |
| contentType18+ | string | No | Yes | Content type of the file. The default value is the file name extension. This option is filled in the **Content-Type** field specified in the HTTP form. |
| filename | string | No | Yes | 

File name. The default value is obtained from the file path.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| extras | object | No | Yes | 

Additional information. This parameter is not included in HTTP requests. The default value is empty.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |

#### request.agent.FormItem10+

Describes the form item of a task.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Request.FileTransferAgent

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| name | string | No | No | Form parameter name. |
| value | string | [FileSpec](#requestagentfilespec10) | Array<[FileSpec](#requestagentfilespec10)\> | No | No | Form parameter value. |

#### request.agent.Config10+

Provides the configuration information of an upload or download task.

**System capability**: SystemCapability.Request.FileTransferAgent

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| action | [Action](#requestagentaction10) | No | No | 
Task action.

\- **UPLOAD**: Upload tasks.

\- **DOWNLOAD**: Download tasks.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| url | string | No | No | 

Resource URL. From API version 6 to 14, the value contains a maximum of 2048 characters; since API version 15, the value contains a maximum of 8192 characters. [Intercepting HTTP](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-file-upload-download#intercepting-http) is supported.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| title | string | No | Yes | 

Task title. The value contains a maximum of 256 characters. The default value is **upload** or **download** in lowercase. Set the value to that of **action**.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| description | string | No | Yes | 

Task description. The value contains a maximum of 1024 characters. The default value is a null string.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| mode | [Mode](#requestagentmode10) | No | Yes | 

Task mode. The default mode is background. Since API version 20, the task mode for downloading files to the user file folder must be set to **request.agent.Mode.FOREGROUND**.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| overwrite | boolean | No | Yes | 

Whether to overwrite an existing file during the download. The default value is **false**.

\- **true**: Overwrite the existing file.

\- **false**: Do not overwrite the existing file. In this case, the download fails.

Since API version 20, the overwrite mode for downloading files to the user file folder must be set to **true**.

In this case, do not create multiple tasks to download content to the same file at a time. Otherwise, the file content will be disordered.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| method | string | No | Yes | 

Standard HTTP method for the task. The value can be **GET**, **POST**, or **PUT**, which is case-insensitive.

\- For the upload task, use **PUT** or **POST**. The default value is **PUT**.

\- For the download task, use **GET** or **POST**. The default value is **GET**.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| headers | object | No | Yes | 

HTTP headers to be included in the task.

\- For the upload task, the default **Content-Type** is **multipart/form-data**.

\- For the download task, the default **Content-Type** is **application/json**.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| data | string | Array<[FormItem](#requestagentformitem10)\> | No | Yes | 

\- For the download task, the value is a string, typically in JSON format (an object will be converted to a JSON string); the default value is null.

\- For the upload task, the value is Array<[FormItem](#requestagentformitem10)\>. Since API version 15, a maximum of 100 files can be uploaded in a single task. This parameter is left empty by default.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| saveas | string | No | Yes | 

Path for storing downloaded files. The options are as follows:

\- Relative path, which is in the cache directory of the caller, for example, **./xxx/yyy/zzz.html** or **xxx/yyy/zzz.html**.

\- Internal protocol path, which can be **internal://** or its subdirectory. **internal** indicates the cache directory of the caller (that is, the input **context**), and **internal://cache** corresponds to **context.cacheDir**, for example, **internal://cache/path/to/file.txt**.

\- Application sandbox path. Only the **base** directory and its subdirectories are supported, for example, **/data/storage/el1/base/path/to/file.txt**.

\- File protocol path, which can be the path of an application file or a user file. For the application file, the application bundle name must be matched and only the **base** directory and its subdirectories are supported, for example, **file://com.example.test/data/storage/el2/base/file.txt**. For the user file, its path must be the user file URI created by the caller.

Since API version 20, the default file path can be the cache path of the caller (that is, the passed context), except for [downloading network resource files to the user file](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-file-upload-download#downloading-network-resource-files-to-the-user-file). The default file name is the part truncated from the last slash (/) in the URL.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| network | [Network](#requestagentnetwork10) | No | Yes | 

Network used for the task. The default value is **ANY** (Wi-Fi or cellular).

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| metered | boolean | No | Yes | 

Whether the task is allowed on a metered network. The default value is **false**.

\- **true**: The task is allowed on a metered network.

\- **false**: The task is not allowed on a metered network.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| roaming | boolean | No | Yes | 

Whether the task is allowed on a roaming network. The default value is **true**.

\- **true**: The task is allowed on a roaming network.

\- **false**: The task is not allowed on a roaming network.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| retry | boolean | No | Yes | 

Whether automatic retry is enabled for the task. This parameter is only applicable to background tasks. The default value is **true**.

\- **true**: The automatic retry is enabled.

\- **false**: The automatic retry is disabled.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| redirect | boolean | No | Yes | 

Whether redirection is allowed. The default value is **true**.

\- **true**: The redirection is allowed.

\- **false**: The redirection is not allowed.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| proxy12+ | string | No | Yes | 

Proxy address. The value contains a maximum of 512 characters.

It is in the format of **http://<\*domain or address\*>:<port>**. By default, this parameter is left empty.

 |
| index | number | No | Yes | 

Path index of the task. It is usually used for resumable transfers. The default value is **0**.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| begins | number | No | Yes | 

File start point of the task. It is usually used for resumable transfers. The default value is **0**. The value is a closed interval.

\- For the download task, the value is obtained by sending an HTTP range request to read the start position when the server starts to download files.

\- For the upload task, the value is obtained at the start position of the upload.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| ends | number | No | Yes | 

File end point of the task. It is usually used for resumable transfers. The default value is **\-1**. The value is a closed interval.

\- For the download task, the value is obtained by sending an HTTP range request to read the end position when the server starts to download files.

\- For the upload task, the value is obtained at the end position of the upload.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| gauge | boolean | No | Yes | 

Whether to send progress notifications. This parameter applies only to background tasks. The default value is **false**.

\- **false**: Progress notifications are not sent. This means that a notification is sent only to indicate the result of the total task.

\- **true**: Progress notifications are sent to indicate the result of each file.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| precise | boolean | No | Yes | 

\- If this parameter is set to **true**, the task fails when the file size cannot be obtained.

\- If this parameter is set to **false**, the task continues when the file size is set to **\-1**.

The default value is **false**.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| token | string | No | Yes | 

Task token. To query a task with a token, you need to provide the token and use [request.agent.touch](#requestagenttouch10). Otherwise, the specified task cannot be queried. The value contains 8 to 2048 bytes. This parameter is left empty by default.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| priority11+ | number | No | Yes | 

Priority of the task. The priority of a foreground task is higher than that of a background task. For tasks in the same mode, a smaller value indicates a higher priority.

Default value: **0**

 |
| extras | object | No | Yes | 

Additional information of the task. This parameter is left empty by default.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| multipart15+ | boolean | No | Yes | 

Whether to use a single request to upload multiple files. If yes, **multipart/form-data** must be used.

\- **false**: A single request is used to upload one file.

\- **true**: A single request is used to upload multiple files.

The default value is **false**.

 |
| notification15+ | [Notification](#requestagentnotification15) | No | Yes | Custom settings for the notification bar. The default value is **{}**. |
| minSpeed20+ | [MinSpeed](#requestagentminspeed20) | No | Yes | Minimum speed, which is disabled by default. |
| timeout20+ | [Timeout](#requestagenttimeout20) | No | Yes | Custom timeout interval. The default connection timeout interval is 60 seconds, and the default total timeout interval is 604800 seconds (one week). If retry is set to **true**, the [timeout](#requestagenttimeout20) event triggers immediate retry, which will obscure the timeout event itself. As a result, the internal [timeout](#requestagenttimeout20) condition has been triggered but the [timeout](#requestagenttimeout20) event is not observable. Set **retry** to **false** to explicitly observe the [timeout](#requestagenttimeout20) event. |

#### request.agent.State10+

Defines the current task status.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Request.FileTransferAgent

| Name | Value | Description |
| :-- | :-- | :-- |
| INITIALIZED | 0x00 | The task is initialized based on the configuration specified in [Config](#requestagentconfig10). |
| WAITING | 0x10 | The task lacks resources for running or the resources for retries, or does not match the network status. |
| RUNNING | 0x20 | The task is being executed. |
| RETRYING | 0x21 | The task has failed at least once and is being executed again. |
| PAUSED | 0x30 | The task is suspended and will be resumed later. |
| STOPPED | 0x31 | The task is stopped. |
| COMPLETED | 0x40 | The task is complete. |
| FAILED | 0x41 | The task fails. |
| REMOVED | 0x50 | The task is removed. |

#### request.agent.Progress10+

Describes the data structure of the task progress.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Request.FileTransferAgent

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| state | [State](#requestagentstate10) | Yes | No | Current task status. |
| index | number | Yes | No | Index of the file that is being processed in the task. |
| processed | number | Yes | No | Size of processed data in the current file in the task, in bytes. |
| sizes | Array<number> | Yes | No | Size of a file in a task, in bytes. If the server uses the chunk mode for data transmission and the total file size cannot be obtained from the request header, the value of **sizes** is treated as **\-1**. |
| extras | object | Yes | Yes | Extra information of the task, for example, the header and body of the response from the server. The default value is empty. |

#### request.agent.Faults10+

Defines the cause of a task failure.

**System capability**: SystemCapability.Request.FileTransferAgent

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/KaR3z2JkRcKrsNO5LDSDYA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8B5C7F6EE9C8C51214C12382816EAFDA6E3D5304ED45518BE9A37698B99CE96A)

In API version 12 or earlier, only serial connection to the IP addresses associated with the specified domain name is supported, and the connection time for a single IP address is not controllable. If the first IP address returned by the DNS is blocked, a handshake timeout may occur, leading to a **TIMEOUT** error.

| Name | Value | Description |
| :-- | :-- | :-- |
| OTHERS | 0xFF | 
Other fault.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| DISCONNECTED | 0x00 | 

Network disconnection.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| TIMEOUT | 0x10 | 

Timeout.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| PROTOCOL | 0x20 | 

Protocol error, for example, an internal server error (500) or a data range that cannot be processed (416).

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| PARAM12+ | 0x30 | 

Parameter error, for example, incorrect URL format.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| FSIO | 0x40 | 

File system I/O error, for example, an error that occurs during the open, search, read, write, or close operation.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| DNS12+ | 0x50 | 

DNS resolution error.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| TCP12+ | 0x60 | 

TCP connection error.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| SSL12+ | 0x70 | 

SSL connection error, for example, a certificate error or certificate verification failure.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| REDIRECT12+ | 0x80 | 

Redirection error.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| LOW\_SPEED20+ | 0x90 | Low speed. |

#### request.agent.Filter10+

Defines the filter criteria.

**System capability**: SystemCapability.Request.FileTransferAgent

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| before | number | No | Yes | Unix timestamp of the end time, in milliseconds. The default value is the invoking time. |
| after | number | No | Yes | Unix timestamp of the start time, in milliseconds. The default value is the invoking time minus 24 hours. |
| state | [State](#requestagentstate10) | No | Yes | Task state. If this parameter is not set, all tasks are queried. |
| action | [Action](#requestagentaction10) | No | Yes | 
Task action.

\- **UPLOAD**: Upload tasks.

\- **DOWNLOAD**: Download tasks.

\- If this parameter is not set, all tasks are queried.

 |
| mode | [Mode](#requestagentmode10) | No | Yes | 

Task mode.

\- **FOREGROUND**: foreground task.

\- **BACKGROUND**: background task.

\- If this parameter is not set, all tasks are queried.

 |

#### request.agent.TaskInfo10+

Defines the data structure of the task information for query. The fields available vary depending on the query type.

**System capability**: SystemCapability.Request.FileTransferAgent

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| saveas | string | Yes | Yes | Path for storing downloaded files. |
| url | string | Yes | Yes | 
Task URL.

\- Use [request.agent.show](#requestagentshow10-1) and [request.agent.touch](#requestagenttouch10-1) to query the value.

 |
| data | string | Array<[FormItem](#requestagentformitem10)\> | Yes | Yes | 

Task value.

\- Use [request.agent.show](#requestagentshow10-1) and [request.agent.touch](#requestagenttouch10-1) to query the value.

 |
| tid | string | Yes | No | Task ID. |
| title | string | Yes | No | Task title. |
| description | string | Yes | No | Task description. |
| action | [Action](#requestagentaction10) | Yes | No | 

Task action.

\- **UPLOAD**: Upload tasks.

\- **DOWNLOAD**: Download tasks.

 |
| mode | [Mode](#requestagentmode10) | Yes | No | 

Task mode.

\- **FOREGROUND**: foreground task.

\- **BACKGROUND**: background task.

 |
| priority11+ | number | Yes | No | Task priority. The priority of a foreground task is higher than that of a background task. For tasks in the same mode, a smaller value indicates a higher priority. |
| mimeType | string | Yes | No | MIME type in the task configuration. |
| progress | [Progress](#requestagentprogress10) | Yes | No | Task progress. |
| gauge | boolean | Yes | No | 

Whether to send progress notifications. This parameter applies only to background tasks.

\- **false**: Progress notifications are not sent. This means that a notification is sent only to indicate the result of the total task.

\- **true**: Progress notifications are sent to indicate the result of each file.

 |
| ctime | number | Yes | No | 

Unix timestamp when the task is created, in milliseconds. The value is generated by the system of the current device.

Note: When [request.agent.search](#requestagentsearch10-1) is used for query, this value must be within the range of \[after,before\] for the task ID to be obtained. For details about **before** and **after**, see [Filter](#requestagentfilter10).

 |
| mtime | number | Yes | No | Unix timestamp when the task state changes, in milliseconds. The value is generated by the system of the current device. |
| retry | boolean | Yes | No | 

Whether automatic retry is enabled for the task. This parameter applies only to background tasks.

\- **true**: The automatic retry is enabled.

\- **false**: The automatic retry is disabled.

 |
| tries | number | Yes | No | Number of retries of the task. |
| faults | [Faults](#requestagentfaults10) | Yes | No | Failure cause of the task. |
| reason | string | Yes | No | Reason why the task is waiting, failed, stopped, or paused. |
| extras | object | Yes | Yes | Extra information of the task. |

#### request.agent.HttpResponse12+

Describes the data structure of the task response header.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Request.FileTransferAgent

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| version | string | Yes | No | HTTP version. |
| statusCode | number | Yes | No | HTTP response status code. |
| reason | string | Yes | No | HTTP response cause. |
| headers | Map<string, Array<string>> | Yes | No | HTTP response header. |

#### request.agent.Notification15+

Describes the custom information of the notification bar.

**System capability**: SystemCapability.Request.FileTransferAgent

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| title | string | No | Yes | Custom title, with a maximum of 1024 bytes. The default title is used if this parameter is not set. |
| text | string | No | Yes | Custom body text, with a maximum of 3072 bytes. The default text is used if this parameter is not set. |
| visibility21+ | number | No | Yes | 
Task visibility mode for the notification bar, which is determined by bitwise operations on the [VISIBILITY constant](#constants-1). The options are as follows:

\- Only the completion notification is displayed. The parameter is **VISIBILITY\_COMPLETION** or **1**. The corresponding notification is displayed after the task is complete or fails.

\- Only the progress notification is displayed when the task is in progress. The parameter is **VISIBILITY\_PROGRESS** or **2**. Completion notification is not displayed when the download task is complete or fails.

\- The progress notification and completion notification are displayed. The parameter is **VISIBILITY\_COMPLETION | VISIBILITY\_PROGRESS** or **3**. The progress notification is displayed when the task is in progress. When the download task is complete or fails, the completion notification is displayed as well.

If this parameter is not set, the **gauge** field is used for determination. If there is no **gauge** field, only the completion notification is displayed.

 |
| wantAgent22+ | [WantAgent](../../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-wantagent-wantagent-module/document.md) | No | Yes | Notification parameter, which is used to implement redirection after a task notification is tapped. The default value is empty. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { common, wantAgent, WantAgent } from '@kit.AbilityKit';

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let wantAgentInfo: wantAgent.WantAgentInfo = {
  wants: \[
    {
      deviceId: '',
      bundleName: 'com.example.request',
      abilityName: 'EntryAbility',
      action: '',
      entities: \[\],
      uri: '',
      parameters: {}
    }
  \],
  actionType: wantAgent.OperationType.START\_ABILITY,
  requestCode: 0,
  wantAgentFlags:\[wantAgent.WantAgentFlags.CONSTANT\_FLAG\]
};
let config: request.agent.Config = {
  action: request.agent.Action.DOWNLOAD,
  url: 'http://127.0.0.1', // Replace the URL with the HTTP address of the real server.
  title: 'taskOnNotification',
  description: 'Sample code for event listening',
  mode: request.agent.Mode.BACKGROUND,
  overwrite: true,
  method: "PUT",
  saveas: "./",
  network: request.agent.Network.ANY,
  gauge: true,
  notification: {
    visibility: request.agent.VISIBILITY\_COMPLETION | request.agent.VISIBILITY\_PROGRESS,
    wantAgent: await wantAgent.getWantAgent(wantAgentInfo),
  }
};
let createOnCallback = (progress: request.agent.Progress) => {
  console.info('download task progress.');
};
request.agent.create(context, config).then((task: request.agent.Task) => {
  task.on('progress', createOnCallback);
  console.info(\`Succeeded in creating a download task. result: ${task.tid}\`);
  task.start();
}).catch((err: BusinessError) => {
  console.error(\`Failed to create a download task, Code: ${err.code}, message: ${err.message}\`);
});

#### request.agent.GroupConfig15+

Describes group configuration options for download tasks.

**System capability**: SystemCapability.Request.FileTransferAgent

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| gauge | boolean | No | Yes | 
Whether to send progress notifications. This parameter applies only to background tasks.

\- **true**: The progress, success, and failure notifications are displayed.

\- **false**: Only success and failure notifications are displayed.

The default value is **false**.

 |
| notification15+ | [Notification](#requestagentnotification15) | No | No | Custom settings for the notification bar. The default value is **{}**. |

#### request.agent.WaitingReason20+

Enumerates the reasons why a task is waiting.

**System capability**: SystemCapability.Request.FileTransferAgent

| Name | Value | Description |
| :-- | :-- | :-- |
| TASK\_QUEUE\_FULL | 0x00 | The task queue is full. |
| NETWORK\_NOT\_MATCH | 0x01 | The required network conditions are not met. |
| APP\_BACKGROUND | 0x02 | The application has been running in the background for a long time. |
| USER\_INACTIVATED | 0x03 | The user is inactive. |

#### request.agent.MinSpeed20+

Defines the minimum speed of a task. If the task speed is lower than the preset value for a specified period of time, the task fails. The failure cause is [LOW\_SPEED](#requestagentfaults10).

**System capability**: SystemCapability.Request.FileTransferAgent

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| speed | number | No | No | Minimum speed of a task, in byte/s. If the task speed is lower than this value for a specified period of time, the task fails. If the value is set to **0**, there is no minimum speed limit. |
| duration | number | No | No | Duration during which the task speed can be lower than the minimum speed, in seconds. If the task speed is lower than the preset value for a specified period of time, the task fails. If the value is set to **0**, there is no minimum speed limit. |

#### request.agent.Timeout20+

Defines the timeout configuration of a task. The task waiting duration is not counted. For details about the waiting reasons, see [WaitingReason20+](#requestagentwaitingreason20).

**System capability**: SystemCapability.Request.FileTransferAgent

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| connectionTimeout | number | No | Yes | Task connection timeout interval, in seconds. The connection timeout interval indicates the maximum time required for establishing a connection between the client and server. If this parameter is not set, the default value **60** is used. The minimum value is **1**. |
| totalTimeout | number | No | Yes | Total timeout interval of a task, in seconds. The total timeout interval includes the time required for establishing a connection, sending a request, and receiving a response. If this parameter is not set, the default value **604800** is used. The minimum value is **1**, and the maximum value is **604800** (that is, one week). |

#### request.agent.Task10+

Implements an upload or download task. Before using this API, you must obtain a **Task** object, from a promise through [request.agent.create](#requestagentcreate10-1) or from a callback through [request.agent.create](#requestagentcreate10).

#### \[h2\]Properties

Task properties include the task ID and task configuration.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Request.FileTransferAgent

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/mDg-WRc-RBaNnvN__SXj9Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4B12030D71F1058826CC69D0B9A4EDD3007DB610AABCC94E388E748C459D00E4)

The **Task** object and its mounting callback function are released and automatically reclaimed by the system after the **remove** method is called.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| tid | string | Yes | No | Task ID, which is unique and automatically generated by the system. |
| config | [Config](#requestagentconfig10) | No | No | Task configuration. |

#### \[h2\]on('progress')10+

on(event: 'progress', callback: (progress: [Progress](#requestagentprogress10)) => void): void

Subscribes to task progress changes. This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Request.FileTransferAgent

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/s1xe1ot_Sv61139eQe5gXQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=09E85D01AB6E3FC21A1A21FED77CBEDA57BAB1E4ECBF9D5F57CC6041078BE4DE)

For details about how to obtain the context in the example, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | string | Yes | 
Event type.

\- **'progress'**: task progress.

 |
| callback | function | Yes | Callback to be invoked when the specified event occurs. |

Parameters of the callback function

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| progress | [Progress](#requestagentprogress10) | Yes | Task progress. |

**Error codes**

For details about the error codes, see [Upload and Download Error Codes](../../../error-codes/upload-and-download-error-codes/document.md) and [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Missing mandatory parameters. 2. Incorrect parameter type. 3. Parameter verification failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let attachments: Array<request.agent.FormItem> = \[{
  name: "taskOnTest",
  value: {
    filename: "taskOnTest.avi",
    path: "./taskOnTest.avi",
  }
}\];
let config: request.agent.Config = {
  action: request.agent.Action.UPLOAD,
  url: 'http://127.0.0.1', // Replace the URL with the HTTP address of the real server.
  title: 'taskOnTest',
  description: 'Sample code for event listening',
  mode: request.agent.Mode.FOREGROUND,
  overwrite: false,
  method: "PUT",
  data: attachments,
  saveas: "./",
  network: request.agent.Network.CELLULAR,
  metered: false,
  roaming: true,
  retry: true,
  redirect: true,
  index: 0,
  begins: 0,
  ends: -1,
  gauge: false,
  precise: false,
  token: "it is a secret"
};
let createOnCallback = (progress: request.agent.Progress) => {
  console.info('upload task progress.');
};
request.agent.create(context, config).then((task: request.agent.Task) => {
  task.on('progress', createOnCallback);
  console.info(\`Succeeded in creating a upload task. result: ${task.tid}\`);
  task.start();
}).catch((err: BusinessError) => {
  console.error(\`Failed to create a upload task, Code: ${err.code}, message: ${err.message}\`);
});

#### \[h2\]on('completed')10+

on(event: 'completed', callback: (progress: [Progress](#requestagentprogress10)) => void): void

Subscribes to task completion events. This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Request.FileTransferAgent

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/KG3-nWDeTmWR62ZUHHsglg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B336DAB415B03FD483788BDCAF7D0FC5AADF624CFCFEF78845507C72A57C81C7)

For details about how to obtain the context in the example, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | string | Yes | 
Event type.

\- **'completed'**: task completion.

 |
| callback | function | Yes | Callback to be invoked when the specified event occurs. |

Parameters of the callback function

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| progress | [Progress](#requestagentprogress10) | Yes | Task progress. |

**Error codes**

For details about the error codes, see [Upload and Download Error Codes](../../../error-codes/upload-and-download-error-codes/document.md) and [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Missing mandatory parameters. 2. Incorrect parameter type. 3. Parameter verification failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let attachments: Array<request.agent.FormItem> = \[{
  name: "taskOnTest",
  value: {
    filename: "taskOnTest.avi",
    path: "./taskOnTest.avi",
  }
}\];
let config: request.agent.Config = {
  action: request.agent.Action.UPLOAD,
  url: 'http://127.0.0.1', // Replace the URL with the HTTP address of the real server.
  title: 'taskOnTest',
  description: 'Sample code for event listening',
  mode: request.agent.Mode.FOREGROUND,
  overwrite: false,
  method: "PUT",
  data: attachments,
  saveas: "./",
  network: request.agent.Network.CELLULAR,
  metered: false,
  roaming: true,
  retry: true,
  redirect: true,
  index: 0,
  begins: 0,
  ends: -1,
  gauge: false,
  precise: false,
  token: "it is a secret"
};
let createOnCallback = (progress: request.agent.Progress) => {
  console.info('upload task completed.');
};
request.agent.create(context, config).then((task: request.agent.Task) => {
  task.on('completed', createOnCallback);
  console.info(\`Succeeded in creating a upload task. result: ${task.tid}\`);
  task.start();
}).catch((err: BusinessError) => {
  console.error(\`Failed to create a upload task, Code: ${err.code}, message: ${err.message}\`);
});

#### \[h2\]on('failed')10+

on(event: 'failed', callback: (progress: [Progress](#requestagentprogress10)) => void): void

Subscribes to task failure events. This API uses an asynchronous callback to return the result. You can call [request.agent.show](#requestagentshow10-1) to view the error cause.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Request.FileTransferAgent

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/J5yIRp2UQ8CWMjR0LqBHhw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=69ED78F6E6B5DAB3034B943E8C54F233F00C9437DC73AD0D690783914A1176CE)

For details about how to obtain the context in the example, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | string | Yes | 
Event type.

\- **'failed'**: task failure.

 |
| callback | function | Yes | Callback to be invoked when the specified event occurs. |

Parameters of the callback function

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| progress | [Progress](#requestagentprogress10) | Yes | Task progress. |

**Error codes**

For details about the error codes, see [Upload and Download Error Codes](../../../error-codes/upload-and-download-error-codes/document.md) and [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Missing mandatory parameters. 2. Incorrect parameter type. 3. Parameter verification failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let attachments: Array<request.agent.FormItem> = \[{
  name: "taskOnTest",
  value: {
    filename: "taskOnTest.avi",
    path: "./taskOnTest.avi",
  }
}\];
let config: request.agent.Config = {
  action: request.agent.Action.UPLOAD,
  url: 'http://127.0.0.1', // Replace the URL with the HTTP address of the real server.
  title: 'taskOnTest',
  description: 'Sample code for event listening',
  mode: request.agent.Mode.FOREGROUND,
  overwrite: false,
  method: "PUT",
  data: attachments,
  saveas: "./",
  network: request.agent.Network.CELLULAR,
  metered: false,
  roaming: true,
  retry: true,
  redirect: true,
  index: 0,
  begins: 0,
  ends: -1,
  gauge: false,
  precise: false,
  token: "it is a secret"
};
let createOnCallback = (progress: request.agent.Progress) => {
  console.info('upload task failed.');
};
request.agent.create(context, config).then((task: request.agent.Task) => {
  task.on('failed', createOnCallback);
  console.info(\`Succeeded in creating a upload task. result: ${task.tid}\`);
  task.start();
}).catch((err: BusinessError) => {
  console.error(\`Failed to create a upload task, Code: ${err.code}, message: ${err.message}\`);
});

#### \[h2\]on('pause')11+

on(event: 'pause', callback: (progress: [Progress](#requestagentprogress10)) => void): void

Subscribes to task pause events. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Request.FileTransferAgent

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/QTXID6-PQoWiatPTs_Lw2w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=66AE2EBEDE61BA05C9B97DD2527A86C198253BB7CCCA752E84F9F0B0910F96B6)

For details about how to obtain the context in the example, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | string | Yes | 
Event type.

\- **'pause'**: task pause.

 |
| callback | function | Yes | Callback to be invoked when the specified event occurs. |

Parameters of the callback function

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| progress | [Progress](#requestagentprogress10) | Yes | Task progress. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Missing mandatory parameters. 2. Incorrect parameter type. 3. Parameter verification failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let attachments: Array<request.agent.FormItem> = \[{
  name: "taskOnTest",
  value: {
    filename: "taskOnTest.avi",
    path: "./taskOnTest.avi",
  }
}\];
let config: request.agent.Config = {
  action: request.agent.Action.UPLOAD,
  url: 'http://127.0.0.1', // Replace the URL with the HTTP address of the real server.
  title: 'taskOnTest',
  description: 'Sample code for event listening',
  mode: request.agent.Mode.FOREGROUND,
  overwrite: false,
  method: "POST",
  data: attachments,
  saveas: "./",
  network: request.agent.Network.CELLULAR,
  metered: false,
  roaming: true,
  retry: true,
  redirect: true,
  index: 0,
  begins: 0,
  ends: -1,
  gauge: false,
  precise: false,
  token: "it is a secret"
};
let createOnCallback = (progress: request.agent.Progress) => {
  console.info('upload task pause.');
};
request.agent.create(context, config).then(async (task: request.agent.Task) => {
  task.on('pause', createOnCallback);
  console.info(\`Succeeded in creating a upload task. result: ${task.tid}\`);
  task.start();
  // Wait for 1 second before executing the next step to prevent asynchronous out-of-order.
  await new Promise<void>((resolve) => {
    setTimeout(() => resolve(),1000)
  })
  task.pause();
}).catch((err: BusinessError) => {
  console.error(\`Failed to create a upload task, Code: ${err.code}, message: ${err.message}\`);
});

#### \[h2\]on('resume')11+

on(event: 'resume', callback: (progress: [Progress](#requestagentprogress10)) => void): void

Subscribes to task resume events. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Request.FileTransferAgent

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/fpJZ839qQ5yB-W9EIwIO_Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=51A85C2C5CD6A34F7570C83E6FD4D367254CC774692382935D5019D09E29BC73)

For details about how to obtain the context in the example, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | string | Yes | 
Event type.

\- **'resume'**: task resume.

 |
| callback | function | Yes | Callback to be invoked when the specified event occurs. |

Parameters of the callback function

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| progress | [Progress](#requestagentprogress10) | Yes | Task progress. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Missing mandatory parameters. 2. Incorrect parameter type. 3. Parameter verification failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let attachments: Array<request.agent.FormItem> = \[{
  name: "taskOnTest",
  value: {
    filename: "taskOnTest.avi",
    path: "./taskOnTest.avi",
  }
}\];
let config: request.agent.Config = {
  action: request.agent.Action.UPLOAD,
  url: 'http://127.0.0.1', // Replace the URL with the HTTP address of the real server.
  title: 'taskOnTest',
  description: 'Sample code for event listening',
  mode: request.agent.Mode.FOREGROUND,
  overwrite: false,
  method: "PUT",
  data: attachments,
  saveas: "./",
  network: request.agent.Network.CELLULAR,
  metered: false,
  roaming: true,
  retry: true,
  redirect: true,
  index: 0,
  begins: 0,
  ends: -1,
  gauge: false,
  precise: false,
  token: "it is a secret"
};
let createOnCallback = (progress: request.agent.Progress) => {
  console.info('upload task resume.');
};
request.agent.create(context, config).then(async (task: request.agent.Task) => {
  task.on('resume', createOnCallback);
  console.info(\`Succeeded in creating a upload task. result: ${task.tid}\`);
  task.start();
  // Wait for 1 second before executing the next step to prevent asynchronous out-of-order.
  await new Promise<void>((resolve) => {
    setTimeout(() => resolve(),1000)
  })
  task.pause();
  // Wait for 1 second before executing the next step to prevent asynchronous out-of-order.
  await new Promise<void>((resolve) => {
    setTimeout(() => resolve(),1000)
  })
  task.resume();
}).catch((err: BusinessError) => {
  console.error(\`Failed to create a upload task, Code: ${err.code}, message: ${err.message}\`);
});

#### \[h2\]on('remove')11+

on(event: 'remove', callback: (progress: [Progress](#requestagentprogress10)) => void): void

Subscribes to task removal events. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Request.FileTransferAgent

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/cFbJPbQnQUeRGCwSQUviAw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BCD2D6282CE7EC53B2335D0112999C4B29BEF4DFB44B3BBF7F6091A4799590E0)

For details about how to obtain the context in the example, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | string | Yes | 
Event type.

\- **'remove'**: task removal.

 |
| callback | function | Yes | Callback to be invoked when the specified event occurs. |

Parameters of the callback function

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| progress | [Progress](#requestagentprogress10) | Yes | Task progress. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Missing mandatory parameters. 2. Incorrect parameter type. 3. Parameter verification failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let attachments: Array<request.agent.FormItem> = \[{
  name: "taskOnTest",
  value: {
    filename: "taskOnTest.avi",
    path: "./taskOnTest.avi",
  }
}\];
let config: request.agent.Config = {
  action: request.agent.Action.UPLOAD,
  url: 'http://127.0.0.1', // Replace the URL with the HTTP address of the real server.
  title: 'taskOnTest',
  description: 'Sample code for event listening',
  mode: request.agent.Mode.FOREGROUND,
  overwrite: false,
  method: "PUT",
  data: attachments,
  saveas: "./",
  network: request.agent.Network.CELLULAR,
  metered: false,
  roaming: true,
  retry: true,
  redirect: true,
  index: 0,
  begins: 0,
  ends: -1,
  gauge: false,
  precise: false,
  token: "it is a secret"
};
let createOnCallback = (progress: request.agent.Progress) => {
  console.info('upload task remove.');
};
request.agent.create(context, config).then(async (task: request.agent.Task) => {
  task.on('remove', createOnCallback);
  console.info(\`Succeeded in creating a upload task. result: ${task.tid}\`);
  task.start();
  // Wait for 1 second before executing the next step to prevent asynchronous out-of-order.
  await new Promise<void>((resolve) => {
    setTimeout(() => resolve(),1000)
  })
  request.agent.remove(task.tid);
}).catch((err: BusinessError) => {
  console.error(\`Failed to create a upload task, Code: ${err.code}, message: ${err.message}\`);
});

#### \[h2\]on('response')12+

on(event: 'response', callback: Callback<HttpResponse>): void

Subscribes to task response headers. This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Request.FileTransferAgent

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/ohMgBmbxQlaoEJilS_wFpw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=49DD51A43CD7E83345D595B2C4EE60225D7531A633D1648D0AD5725014928222)

For details about how to obtain the context in the example, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | string | Yes | 
Event type.

\- **'response'**: task response.

 |
| callback | Callback<[HttpResponse](#requestagenthttpresponse12)\> | Yes | Callback used to return the data structure of the task response header. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Missing mandatory parameters. 2. Incorrect parameter type. 3. Parameter verification failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let attachments: Array<request.agent.FormItem> = \[{
  name: "taskOnTest",
  value: {
    filename: "taskOnTest.avi",
    path: "./taskOnTest.avi",
  }
}\];
let config: request.agent.Config = {
  action: request.agent.Action.UPLOAD,
  url: 'http://127.0.0.1', // Replace the URL with the HTTP address of the real server.
  title: 'taskOnTest',
  description: 'Sample code for event listening',
  mode: request.agent.Mode.FOREGROUND,
  overwrite: false,
  method: "PUT",
  data: attachments,
  saveas: "./",
  network: request.agent.Network.CELLULAR,
  metered: false,
  roaming: true,
  retry: true,
  redirect: true,
  index: 0,
  begins: 0,
  ends: -1,
  gauge: false,
  precise: false,
  token: "it is a secret"
};
let createOnCallback = (response: request.agent.HttpResponse) => {
  console.info('upload task response.');
};
request.agent.create(context, config).then((task: request.agent.Task) => {
  task.on('response', createOnCallback);
  console.info(\`Succeeded in creating a upload task. result: ${task.tid}\`);
  task.start();
}).catch((err: BusinessError) => {
  console.error(\`Failed to create a upload task, Code: ${err.code}, message: ${err.message}\`);
});

#### \[h2\]on('faultOccur')20+

on(event: 'faultOccur', callback: Callback<Faults>): void

Subscribes to task failure events. This API uses a callback to return the result.

**System capability**: SystemCapability.Request.FileTransferAgent

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/dpLJo1QqSsaKnHgUW5usUg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4932993670384383F42B8D0899EE5360B834E38550CF447499A2DD26B243FD87)

For details about how to obtain the context in the example, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | string | Yes | 
Event type.

\- **'faultOccur'**: task failure.

 |
| callback | Callback<[Faults](#requestagentfaults10)\> | Yes | Callback used to return the failure cause of the task. |

**Error codes**

For details about the error codes, see [Upload and Download Error Codes](../../../error-codes/upload-and-download-error-codes/document.md) and [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Missing mandatory parameters. 2. Incorrect parameter type. 3. Parameter verification failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let attachments: Array<request.agent.FormItem> = \[{
  name: "taskOnTest",
  value: {
    filename: "taskOnTest.avi",
    mimeType: "application/octet-stream",
    path: "./taskOnTest.avi",
  }
}\];
let config: request.agent.Config = {
  action: request.agent.Action.UPLOAD,
  url: 'http://127.0.0.1', // Replace the URL with the HTTP address of the real server.
  title: 'taskOnTest',
  description: 'Sample code for event listening',
  mode: request.agent.Mode.FOREGROUND,
  overwrite: false,
  method: "PUT",
  data: attachments,
  saveas: "./",
  network: request.agent.Network.CELLULAR,
  metered: false,
  roaming: true,
  retry: true,
  redirect: true,
  index: 0,
  begins: 0,
  ends: -1,
  gauge: false,
  precise: false,
  token: "it is a secret"
};
let faultOnCallback = (faults: request.agent.Faults) => {
  console.info('upload task failed.');
};
request.agent.create(context, config).then((task: request.agent.Task) => {
  task.on('faultOccur', faultOnCallback);
  console.info(\`Succeeded in creating a upload task. result: ${task.tid}\`);
  task.start();
}).catch((err: BusinessError) => {
  console.error(\`Failed to create a upload task, Code: ${err.code}, message: ${err.message}\`);
});

#### \[h2\]on('wait')20+

on(event: 'wait', callback: Callback<WaitingReason>): void

Subscribes to task wait events. This API uses a callback to return the result.

**System capability**: SystemCapability.Request.FileTransferAgent

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/Tk3aUEIqR-2Rtkedo_v3_g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3017E52480513E6654679E30CE335F9A96948DFD85929BFBBD47ABD63C42AD31)

For details about how to obtain the context in the example, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | string | Yes | 
Event type.

\- 'wait': The task is waiting.

 |
| callback | Callback<[WaitingReason](#requestagentwaitingreason20)\> | Yes | Callback used to return the waiting reason of the task. |

**Error codes**

For details about the error codes, see [Upload and Download Error Codes](../../../error-codes/upload-and-download-error-codes/document.md) and [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Missing mandatory parameters. 2. Incorrect parameter type. 3. Parameter verification failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let attachments: Array<request.agent.FormItem> = \[{
  name: "taskOnTest",
  value: {
    filename: "taskOnTest.avi",
    mimeType: "application/octet-stream",
    path: "./taskOnTest.avi",
  }
}\];
let config: request.agent.Config = {
  action: request.agent.Action.UPLOAD,
  url: 'http://127.0.0.1', // Replace the URL with the HTTP address of the real server.
  title: 'taskOnTest',
  description: 'Sample code for event listening',
  mode: request.agent.Mode.FOREGROUND,
  overwrite: false,
  method: "PUT",
  data: attachments,
  saveas: "./",
  network: request.agent.Network.CELLULAR,
  metered: false,
  roaming: true,
  retry: true,
  redirect: true,
  index: 0,
  begins: 0,
  ends: -1,
  gauge: false,
  precise: false,
  token: "it is a secret"
};
let waitOnCallback = (reason: request.agent.WaitingReason) => {
  console.info('upload task waiting.');
};
request.agent.create(context, config).then((task: request.agent.Task) => {
  task.on('wait', waitOnCallback);
  console.info(\`Succeeded in creating a upload task. result: ${task.tid}\`);
  task.start();
}).catch((err: BusinessError) => {
  console.error(\`Failed to create a upload task, Code: ${err.code}, message: ${err.message}\`);
});

#### \[h2\]off('progress')10+

off(event: 'progress', callback?: (progress: [Progress](#requestagentprogress10)) => void): void

Unsubscribes from task progress events.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Request.FileTransferAgent

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/RvmwV9DCQ4q9SQ6inIYy-w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CB6F5934BA258A015B704F404E798D9AE00DFF85207D54E4F83BBD7F57E0FF1F)

For details about how to obtain the context in the example, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | string | Yes | 
Event type.

\- **'progress'**: task progress.

 |
| callback | function | No | Callback to be invoked when the specified event occurs. If this parameter is not specified, all callbacks of the task progress events are unregistered. |

Parameters of the callback function

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| progress | [Progress](#requestagentprogress10) | Yes | Task progress. |

**Error codes**

For details about the error codes, see [Upload and Download Error Codes](../../../error-codes/upload-and-download-error-codes/document.md) and [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Missing mandatory parameters. 2. Incorrect parameter type. 3. Parameter verification failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let attachments: Array<request.agent.FormItem> = \[{
  name: "taskOffTest",
  value: {
    filename: "taskOffTest.avi",
    path: "./taskOffTest.avi",
  }
}\];
let config: request.agent.Config = {
  action: request.agent.Action.UPLOAD,
  url: 'http://127.0.0.1', // Replace the URL with the HTTP address of the real server.
  title: 'taskOffTest',
  description: 'Sample code for event listening',
  mode: request.agent.Mode.FOREGROUND,
  overwrite: false,
  method: "PUT",
  data: attachments,
  saveas: "./",
  network: request.agent.Network.CELLULAR,
  metered: false,
  roaming: true,
  retry: true,
  redirect: true,
  index: 0,
  begins: 0,
  ends: -1,
  gauge: false,
  precise: false,
  token: "it is a secret"
};
let createOffCallback1 = (progress: request.agent.Progress) => {
  console.info('upload task progress.');
};
let createOffCallback2 = (progress: request.agent.Progress) => {
  console.info('upload task progress.');
};
request.agent.create(context, config).then((task: request.agent.Task) => {
  task.on('progress', createOffCallback1);
  task.on('progress', createOffCallback2);
  // Unsubscribe from createOffCallback1.
  task.off('progress', createOffCallback1);
  // Unsubscribe from all callbacks of task progress changes.
  task.off('progress');
  console.info(\`Succeeded in creating a upload task. result: ${task.tid}\`);
  task.start();
}).catch((err: BusinessError) => {
  console.error(\`Failed to create a upload task, Code: ${err.code}, message: ${err.message}\`);
});

#### \[h2\]off('completed')10+

off(event: 'completed', callback?: (progress: [Progress](#requestagentprogress10)) => void): void

Unsubscribes from task completion events.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Request.FileTransferAgent

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/CvPpbhcHROOVd5MyA5AuSw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=18A98F214D959B252454DAB73B51373F4C0CAAA9051E27D795534EA2182C878B)

For details about how to obtain the context in the example, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | string | Yes | 
Event type.

\- **'completed'**: task completion.

 |
| callback | function | No | Callback to be invoked when the specified event occurs. If this parameter is not specified, all callbacks of the task completion events are unregistered. |

Parameters of the callback function

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| progress | [Progress](#requestagentprogress10) | Yes | Task progress. |

**Error codes**

For details about the error codes, see [Upload and Download Error Codes](../../../error-codes/upload-and-download-error-codes/document.md) and [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Missing mandatory parameters. 2. Incorrect parameter type. 3. Parameter verification failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let attachments: Array<request.agent.FormItem> = \[{
  name: "taskOffTest",
  value: {
    filename: "taskOffTest.avi",
    path: "./taskOffTest.avi",
  }
}\];
let config: request.agent.Config = {
  action: request.agent.Action.UPLOAD,
  url: 'http://127.0.0.1', // Replace the URL with the HTTP address of the real server.
  title: 'taskOffTest',
  description: 'Sample code for event listening',
  mode: request.agent.Mode.FOREGROUND,
  overwrite: false,
  method: "PUT",
  data: attachments,
  saveas: "./",
  network: request.agent.Network.CELLULAR,
  metered: false,
  roaming: true,
  retry: true,
  redirect: true,
  index: 0,
  begins: 0,
  ends: -1,
  gauge: false,
  precise: false,
  token: "it is a secret"
};
let createOffCallback1 = (progress: request.agent.Progress) => {
  console.info('upload task completed.');
};
let createOffCallback2 = (progress: request.agent.Progress) => {
  console.info('upload task completed.');
};
request.agent.create(context, config).then((task: request.agent.Task) => {
  task.on('completed', createOffCallback1);
  task.on('completed', createOffCallback2);
  // Unsubscribe from createOffCallback1.
  task.off('completed', createOffCallback1);
  // Unsubscribe from all callbacks of the task completion events.
  task.off('completed');
  console.info(\`Succeeded in creating a upload task. result: ${task.tid}\`);
  task.start();
}).catch((err: BusinessError) => {
  console.error(\`Failed to create a upload task, Code: ${err.code}, message: ${err.message}\`);
});

#### \[h2\]off('failed')10+

off(event: 'failed', callback?: (progress: [Progress](#requestagentprogress10)) => void): void

Unsubscribes from task failure events.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Request.FileTransferAgent

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/4Kmk5JKrR_SCbul7_sQ_gQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6517C0EAF8B0E18BA4F5DDDFBB6492C04BE0E481586D6D587479F216DCBEBB98)

For details about how to obtain the context in the example, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | string | Yes | 
Event type.

\- **'failed'**: task failure.

 |
| callback | function | No | Callback to be invoked when the specified event occurs. If this parameter is not specified, all callbacks of the task failure events are unregistered. |

Parameters of the callback function

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| progress | [Progress](#requestagentprogress10) | Yes | Task progress. |

**Error codes**

For details about the error codes, see [Upload and Download Error Codes](../../../error-codes/upload-and-download-error-codes/document.md) and [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Missing mandatory parameters. 2. Incorrect parameter type. 3. Parameter verification failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let attachments: Array<request.agent.FormItem> = \[{
  name: "taskOffTest",
  value: {
    filename: "taskOffTest.avi",
    path: "./taskOffTest.avi",
  }
}\];
let config: request.agent.Config = {
  action: request.agent.Action.UPLOAD,
  url: 'http://127.0.0.1', // Replace the URL with the HTTP address of the real server.
  title: 'taskOffTest',
  description: 'Sample code for event listening',
  mode: request.agent.Mode.FOREGROUND,
  overwrite: false,
  method: "PUT",
  data: attachments,
  saveas: "./",
  network: request.agent.Network.CELLULAR,
  metered: false,
  roaming: true,
  retry: true,
  redirect: true,
  index: 0,
  begins: 0,
  ends: -1,
  gauge: false,
  precise: false,
  token: "it is a secret"
};
let createOffCallback1 = (progress: request.agent.Progress) => {
  console.info('upload task failed.');
};
let createOffCallback2 = (progress: request.agent.Progress) => {
  console.info('upload task failed.');
};
request.agent.create(context, config).then((task: request.agent.Task) => {
  task.on('failed', createOffCallback1);
  task.on('failed', createOffCallback2);
  // Unsubscribe from createOffCallback1.
  task.off('failed', createOffCallback1);
  // Unsubscribe from all callbacks of the task failure events.
  task.off('failed');
  console.info(\`Succeeded in creating a upload task. result: ${task.tid}\`);
  task.start();
}).catch((err: BusinessError) => {
  console.error(\`Failed to create a upload task, Code: ${err.code}, message: ${err.message}\`);
});

#### \[h2\]off('pause')11+

off(event: 'pause', callback?: (progress: [Progress](#requestagentprogress10)) => void): void

Unsubscribes from the foreground task pause event.

**System capability**: SystemCapability.Request.FileTransferAgent

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/rqskcG5MQjazbXH5qT_0wA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C3B7107133EAC9741284022F6635C4EAD0B77BCA9324823C22C3EDD94BBB671B)

For details about how to obtain the context in the example, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | string | Yes | 
Event type.

\- **'pause'**: task pause.

 |
| callback | function | No | Callback to be invoked when the specified event occurs. If this parameter is not specified, all callbacks of the task pause events are unregistered. |

Parameters of the callback function

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| progress | [Progress](#requestagentprogress10) | Yes | Task progress. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Missing mandatory parameters. 2. Incorrect parameter type. 3. Parameter verification failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let attachments: Array<request.agent.FormItem> = \[{
  name: "taskOffTest",
  value: {
    filename: "taskOffTest.avi",
    path: "./taskOffTest.avi",
  }
}\];
let config: request.agent.Config = {
  action: request.agent.Action.UPLOAD,
  url: 'http://127.0.0.1', // Replace the URL with the HTTP address of the real server.
  title: 'taskOffTest',
  description: 'Sample code for event listening',
  mode: request.agent.Mode.FOREGROUND,
  overwrite: false,
  method: "PUT",
  data: attachments,
  saveas: "./",
  network: request.agent.Network.CELLULAR,
  metered: false,
  roaming: true,
  retry: true,
  redirect: true,
  index: 0,
  begins: 0,
  ends: -1,
  gauge: false,
  precise: false,
  token: "it is a secret"
};
let createOffCallback1 = (progress: request.agent.Progress) => {
  console.info('upload task pause.');
};
let createOffCallback2 = (progress: request.agent.Progress) => {
  console.info('upload task pause.');
};
request.agent.create(context, config).then((task: request.agent.Task) => {
  task.on('pause', createOffCallback1);
  task.on('pause', createOffCallback2);
  // Unsubscribe from createOffCallback1.
  task.off('pause', createOffCallback1);
  // Unsubscribe from all callbacks of the task pause event.
  task.off('pause');
  console.info(\`Succeeded in creating a upload task. result: ${task.tid}\`);
  task.start();
}).catch((err: BusinessError) => {
  console.error(\`Failed to create a upload task, Code: ${err.code}, message: ${err.message}\`);
});

#### \[h2\]off('resume')11+

off(event: 'resume', callback?: (progress: [Progress](#requestagentprogress10)) => void): void

Unsubscribes from foreground task resume events.

**System capability**: SystemCapability.Request.FileTransferAgent

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/7vEmIK9jS4uq78IdIoDC5w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=96316B2BD1FC268EA84757336B877B41A9A3AC59F64E488C65DE4FB3D8D6578D)

For details about how to obtain the context in the example, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | string | Yes | 
Event type.

\- **'resume'**: task resume.

 |
| callback | function | No | Callback to be invoked when the specified event occurs. If this parameter is not specified, all callbacks of the task resume events are unregistered. |

Parameters of the callback function

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| progress | [Progress](#requestagentprogress10) | Yes | Task progress. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Missing mandatory parameters. 2. Incorrect parameter type. 3. Parameter verification failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let attachments: Array<request.agent.FormItem> = \[{
  name: "taskOffTest",
  value: {
    filename: "taskOffTest.avi",
    path: "./taskOffTest.avi",
  }
}\];
let config: request.agent.Config = {
  action: request.agent.Action.UPLOAD,
  url: 'http://127.0.0.1', // Replace the URL with the HTTP address of the real server.
  title: 'taskOffTest',
  description: 'Sample code for event listening',
  mode: request.agent.Mode.FOREGROUND,
  overwrite: false,
  method: "PUT",
  data: attachments,
  saveas: "./",
  network: request.agent.Network.CELLULAR,
  metered: false,
  roaming: true,
  retry: true,
  redirect: true,
  index: 0,
  begins: 0,
  ends: -1,
  gauge: false,
  precise: false,
  token: "it is a secret"
};
let createOffCallback1 = (progress: request.agent.Progress) => {
  console.info('upload task resume.');
};
let createOffCallback2 = (progress: request.agent.Progress) => {
  console.info('upload task resume.');
};
request.agent.create(context, config).then((task: request.agent.Task) => {
  task.on('resume', createOffCallback1);
  task.on('resume', createOffCallback2);
  // Unsubscribe from createOffCallback1.
  task.off('resume', createOffCallback1);
  // Unsubscribe from all callbacks of the task resume event.
  task.off('resume');
  console.info(\`Succeeded in creating a upload task. result: ${task.tid}\`);
  task.start();
}).catch((err: BusinessError) => {
  console.error(\`Failed to create a upload task, Code: ${err.code}, message: ${err.message}\`);
});

#### \[h2\]off('remove')11+

off(event: 'remove', callback?: (progress: [Progress](#requestagentprogress10)) => void): void

Unsubscribes from the task removal event.

**System capability**: SystemCapability.Request.FileTransferAgent

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/LZ_je0mpQwixg5nLcKmcZA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=43063BAAF89908047A4A945CC5703F41E752DF53498D06D4A2391E033FA6A221)

For details about how to obtain the context in the example, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | string | Yes | 
Event type.

\- **'remove'**: task removal.

 |
| callback | function | No | Callback to be invoked when the specified event occurs. If this parameter is not specified, all callbacks of the task removal events are unregistered. |

Parameters of the callback function

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| progress | [Progress](#requestagentprogress10) | Yes | Task progress. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Missing mandatory parameters. 2. Incorrect parameter type. 3. Parameter verification failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let attachments: Array<request.agent.FormItem> = \[{
  name: "taskOffTest",
  value: {
    filename: "taskOffTest.avi",
    path: "./taskOffTest.avi",
  }
}\];
let config: request.agent.Config = {
  action: request.agent.Action.UPLOAD,
  url: 'http://127.0.0.1', // Replace the URL with the HTTP address of the real server.
  title: 'taskOffTest',
  description: 'Sample code for event listening',
  mode: request.agent.Mode.FOREGROUND,
  overwrite: false,
  method: "PUT",
  data: attachments,
  saveas: "./",
  network: request.agent.Network.CELLULAR,
  metered: false,
  roaming: true,
  retry: true,
  redirect: true,
  index: 0,
  begins: 0,
  ends: -1,
  gauge: false,
  precise: false,
  token: "it is a secret"
};
let createOffCallback1 = (progress: request.agent.Progress) => {
  console.info('upload task remove.');
};
let createOffCallback2 = (progress: request.agent.Progress) => {
  console.info('upload task remove.');
};
request.agent.create(context, config).then((task: request.agent.Task) => {
  task.on('remove', createOffCallback1);
  task.on('remove', createOffCallback2);
  // Unsubscribe from createOffCallback1.
  task.off('remove', createOffCallback1);
  // Unsubscribe from all callbacks of the task failure event.
  task.off('remove');
  console.info(\`Succeeded in creating a upload task. result: ${task.tid}\`);
  task.start();
}).catch((err: BusinessError) => {
  console.error(\`Failed to create a upload task, Code: ${err.code}, message: ${err.message}\`);
});

#### \[h2\]off('response')12+

off(event: 'response', callback?: Callback<HttpResponse>): void

Unsubscribes from task response headers.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Request.FileTransferAgent

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/kn2a19KLRZyI3RvtfkjehQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D6BA2B6FA314B5372B4949616662B2907BB06877CA07478056F4394C6C779E52)

For details about how to obtain the context in the example, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | string | Yes | 
Event type.

\- **response**: task response.

 |
| callback | Callback<[HttpResponse](#requestagenthttpresponse12)\> | No | Callback to unregister. If this parameter is not specified, all callbacks of the current type will be unregistered. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Missing mandatory parameters. 2. Incorrect parameter type. 3. Parameter verification failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let attachments: Array<request.agent.FormItem> = \[{
  name: "taskOffTest",
  value: {
    filename: "taskOffTest.avi",
    path: "./taskOffTest.avi",
  }
}\];
let config: request.agent.Config = {
  action: request.agent.Action.UPLOAD,
  url: 'http://127.0.0.1', // Replace the URL with the HTTP address of the real server.
  title: 'taskOffTest',
  description: 'Sample code for event listening',
  mode: request.agent.Mode.FOREGROUND,
  overwrite: false,
  method: "PUT",
  data: attachments,
  saveas: "./",
  network: request.agent.Network.CELLULAR,
  metered: false,
  roaming: true,
  retry: true,
  redirect: true,
  index: 0,
  begins: 0,
  ends: -1,
  gauge: false,
  precise: false,
  token: "it is a secret"
};
let createOffCallback1 = (progress: request.agent.HttpResponse) => {
  console.info('upload task response.');
};
let createOffCallback2 = (progress: request.agent.HttpResponse) => {
  console.info('upload task response.');
};
request.agent.create(context, config).then((task: request.agent.Task) => {
  task.on('response', createOffCallback1);
  task.on('response', createOffCallback2);
  // Unsubscribe from createOffCallback1.
  task.off('response', createOffCallback1);
  // Unsubscribe from all callbacks of the task failure event.
  task.off('response');
  console.info(\`Succeeded in creating a upload task. result: ${task.tid}\`);
  task.start();
}).catch((err: BusinessError) => {
  console.error(\`Failed to create a upload task, Code: ${err.code}, message: ${err.message}\`);
});

#### \[h2\]off('faultOccur')20+

off(event: 'faultOccur', callback?: Callback<Faults>): void

Unsubscribes from task failure events.

**System capability**: SystemCapability.Request.FileTransferAgent

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/QdQv_vrRT0yRQVIoTfD6cw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C7C2A7AA35767D6F83B964B7AD98B0A324D497B593B733E2A87435362A717E38)

For details about how to obtain the context in the example, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | string | Yes | 
Event type.

\- **'faultOccur'**: task failure.

 |
| callback | Callback<[Faults](#requestagentfaults10)\> | No | Callback to unregister. If this parameter is not specified, all callbacks of the current type will be unregistered. |

**Error codes**

For details about the error codes, see [Upload and Download Error Codes](../../../error-codes/upload-and-download-error-codes/document.md) and [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Missing mandatory parameters. 2. Incorrect parameter type. 3. Parameter verification failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let attachments: Array<request.agent.FormItem> = \[{
  name: "taskOffTest",
  value: {
    filename: "taskOffTest.avi",
    mimeType: "application/octet-stream",
    path: "./taskOffTest.avi",
  }
}\];
let config: request.agent.Config = {
  action: request.agent.Action.UPLOAD,
  url: 'http://127.0.0.1', // Replace the URL with the HTTP address of the real server.
  title: 'taskOffTest',
  description: 'Sample code for event listening',
  mode: request.agent.Mode.FOREGROUND,
  overwrite: false,
  method: "PUT",
  data: attachments,
  saveas: "./",
  network: request.agent.Network.CELLULAR,
  metered: false,
  roaming: true,
  retry: true,
  redirect: true,
  index: 0,
  begins: 0,
  ends: -1,
  gauge: false,
  precise: false,
  token: "it is a secret"
};
let faultOffCallback1 = (faults: request.agent.Faults) => {
  console.info('upload task failed.');
};
let faultOffCallback2 = (faults: request.agent.Faults) => {
  console.info('upload task failed.');
};
request.agent.create(context, config).then((task: request.agent.Task) => {
  task.on('faultOccur', faultOffCallback1);
  task.on('faultOccur', faultOffCallback2);
  // Unsubscribe from faultOffCallback1.
  task.off('faultOccur', faultOffCallback1);
  // Unsubscribe from all callbacks of the task failure event.
  task.off('faultOccur');
  console.info(\`Succeeded in creating a upload task. result: ${task.tid}\`);
  task.start();
}).catch((err: BusinessError) => {
  console.error(\`Failed to create a upload task, Code: ${err.code}, message: ${err.message}\`);
});

#### \[h2\]off('wait')20+

off(event: 'wait', callback?: Callback<WaitingReason>): void

Unsubscribes from task waiting events.

**System capability**: SystemCapability.Request.FileTransferAgent

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/5ZRPemtUSquglycy6VQrlQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=815DB50395BA97E1DA3D2CF6BF58212D453650592CC3C645A959F4CE88B8B942)

For details about how to obtain the context in the example, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | string | Yes | 
Event type.

\- 'wait': The task is waiting.

 |
| callback | Callback<[WaitingReason](#requestagentwaitingreason20)\> | No | Callback to unregister. If this parameter is not specified, all callbacks of the current type will be unregistered. |

**Error codes**

For details about the error codes, see [Upload and Download Error Codes](../../../error-codes/upload-and-download-error-codes/document.md) and [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Missing mandatory parameters. 2. Incorrect parameter type. 3. Parameter verification failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let attachments: Array<request.agent.FormItem> = \[{
  name: "taskOffTest",
  value: {
    filename: "taskOffTest.avi",
    mimeType: "application/octet-stream",
    path: "./taskOffTest.avi",
  }
}\];
let config: request.agent.Config = {
  action: request.agent.Action.UPLOAD,
  url: 'http://127.0.0.1', // Replace the URL with the HTTP address of the real server.
  title: 'taskOffTest',
  description: 'Sample code for event listening',
  mode: request.agent.Mode.FOREGROUND,
  overwrite: false,
  method: "PUT",
  data: attachments,
  saveas: "./",
  network: request.agent.Network.CELLULAR,
  metered: false,
  roaming: true,
  retry: true,
  redirect: true,
  index: 0,
  begins: 0,
  ends: -1,
  gauge: false,
  precise: false,
  token: "it is a secret"
};
let waitOffCallback1 = (reason: request.agent.WaitingReason) => {
  console.info('upload task waiting.');
};
let waitOffCallback2 = (reason: request.agent.WaitingReason) => {
  console.info('upload task waiting.');
};
request.agent.create(context, config).then((task: request.agent.Task) => {
  task.on('wait', waitOffCallback1);
  task.on('wait', waitOffCallback2);
  // Unsubscribe from waitOffCallback1.
  task.off('wait', waitOffCallback1);
  // Unsubscribe from all callbacks of the task failure event.
  task.off('wait');
  console.info(\`Succeeded in creating a upload task. result: ${task.tid}\`);
  task.start();
}).catch((err: BusinessError) => {
  console.error(\`Failed to create a upload task, Code: ${err.code}, message: ${err.message}\`);
});

#### \[h2\]start10+

start(callback: AsyncCallback<void>): void

Starts a task. This API uses an asynchronous callback to return the result.

Tasks in the following states can be started:

1.  Task created by **request.agent.create**.
2.  Download tasks that are created by **request.agent.create** but have failed or paused.

**Required permissions**: ohos.permission.INTERNET

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Request.FileTransferAgent

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/1kSZvR7iSOm4rRkvzAFQuA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BDC068516AB55056DE4DD866406C3FCFFF2146DF2268460F720FAFA90849F292)

For details about how to obtain the context in the example, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Upload and Download Error Codes](../../../error-codes/upload-and-download-error-codes/document.md) and [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 13400003 | Task service ability error. |
| 21900007 | Operation with wrong task state. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let config: request.agent.Config = {
  action: request.agent.Action.DOWNLOAD,
  url: 'http://127.0.0.1', // Replace the URL with the HTTP address of the real server.
  title: 'taskStartTest',
  description: 'Sample code for start the download task',
  mode: request.agent.Mode.BACKGROUND,
  overwrite: false,
  method: "GET",
  data: "",
  saveas: "./",
  network: request.agent.Network.CELLULAR,
  metered: false,
  roaming: true,
  retry: true,
  redirect: true,
  index: 0,
  begins: 0,
  ends: -1,
  gauge: false,
  precise: false,
  token: "it is a secret"
};
request.agent.create(context, config).then((task: request.agent.Task) => {
  task.start((err: BusinessError) => {
    if (err) {
      console.error(\`Failed to start the download task, Code: ${err.code}, message: ${err.message}\`);
      return;
    }
    console.info(\`Succeeded in starting a download task.\`);
  });
  console.info(\`Succeeded in creating a download task. result: ${task.tid}\`);
}).catch((err: BusinessError) => {
  console.error(\`Failed to create a download task, Code: ${err.code}, message: ${err.message}\`);
});

#### \[h2\]start10+

start(): Promise<void>

Starts this task. This API uses a promise to return the result.

Tasks in the following states can be started:

1.  Task created by **request.agent.create**.
2.  Download tasks that are created by **request.agent.create** but have failed or paused.

**Required permissions**: ohos.permission.INTERNET

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Request.FileTransferAgent

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/q9MIcrSoTYakovOdbB1lng/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3615CAC6772260420B80F158FD555B2C78397828A197D6DEC7C9765A31AEA63C)

For details about how to obtain the context in the example, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Upload and Download Error Codes](../../../error-codes/upload-and-download-error-codes/document.md) and [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 13400003 | Task service ability error. |
| 21900007 | Operation with wrong task state. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let config: request.agent.Config = {
  action: request.agent.Action.DOWNLOAD,
  url: 'http://127.0.0.1', // Replace the URL with the HTTP address of the real server.
  title: 'taskStartTest',
  description: 'Sample code for start the download task',
  mode: request.agent.Mode.BACKGROUND,
  overwrite: false,
  method: "GET",
  data: "",
  saveas: "./",
  network: request.agent.Network.CELLULAR,
  metered: false,
  roaming: true,
  retry: true,
  redirect: true,
  index: 0,
  begins: 0,
  ends: -1,
  gauge: false,
  precise: false,
  token: "it is a secret"
};
request.agent.create(context, config).then((task: request.agent.Task) => {
  task.start().then(() => {
    console.info(\`Succeeded in starting a download task.\`);
  }).catch((err: BusinessError) => {
    console.error(\`Failed to start the download task, Code: ${err.code}, message: ${err.message}\`);
  });
  console.info(\`Succeeded in creating a download task. result: ${task.tid}\`);
}).catch((err: BusinessError) => {
  console.error(\`Failed to create a download task, Code: ${err.code}, message: ${err.message}\`);
});

#### \[h2\]pause10+

pause(callback: AsyncCallback<void>): void

Pauses a task that is waiting, running, or retrying. A paused task can be resumed by [resume](#resume10). This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Request.FileTransferAgent

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Upload and Download Error Codes](../../../error-codes/upload-and-download-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 13400003 | Task service ability error. |
| 21900007 | Operation with wrong task state. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let config: request.agent.Config = {
  action: request.agent.Action.DOWNLOAD,
  url: 'http://127.0.0.1', // Replace the URL with the HTTP address of the real server.
  title: 'taskPauseTest',
  description: 'Sample code for pause the download task',
  mode: request.agent.Mode.BACKGROUND,
  overwrite: false,
  method: "GET",
  data: "",
  saveas: "./",
  network: request.agent.Network.CELLULAR,
  metered: false,
  roaming: true,
  retry: true,
  redirect: true,
  index: 0,
  begins: 0,
  ends: -1,
  gauge: false,
  precise: false,
  token: "it is a secret"
};
request.agent.create(context, config).then(async (task: request.agent.Task) => {
  task.start();
  // Wait for 1 second before executing the next step to prevent asynchronous out-of-order.
  await new Promise<void>((resolve) => {
    setTimeout(() => resolve(),1000)
  })
  task.pause((err: BusinessError) => {
    if (err) {
      console.error(\`Failed to pause the download task, Code: ${err.code}, message: ${err.message}\`);
      return;
    }
    console.info(\`Succeeded in pausing a download task. \`);
  });
  console.info(\`Succeeded in creating a download task. result: ${task.tid}\`);
}).catch((err: BusinessError) => {
  console.error(\`Failed to create a download task, Code: ${err.code}, message: ${err.message}\`);
});

#### \[h2\]pause10+

pause(): Promise<void>

Pauses a task that is waiting, running, or retrying. A paused task can be resumed by [resume](#resume10). This API uses a promise to return the result.

**System capability**: SystemCapability.Request.FileTransferAgent

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Upload and Download Error Codes](../../../error-codes/upload-and-download-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 13400003 | Task service ability error. |
| 21900007 | Operation with wrong task state. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let config: request.agent.Config = {
  action: request.agent.Action.DOWNLOAD,
  url: 'http://127.0.0.1', // Replace the URL with the HTTP address of the real server.
  title: 'taskPauseTest',
  description: 'Sample code for pause the download task',
  mode: request.agent.Mode.BACKGROUND,
  overwrite: false,
  method: "GET",
  data: "",
  saveas: "./",
  network: request.agent.Network.CELLULAR,
  metered: false,
  roaming: true,
  retry: true,
  redirect: true,
  index: 0,
  begins: 0,
  ends: -1,
  gauge: false,
  precise: false,
  token: "it is a secret"
};
request.agent.create(context, config).then(async (task: request.agent.Task) => {
  task.start();
  // Wait for 1 second before executing the next step to prevent asynchronous out-of-order.
  await new Promise<void>((resolve) => {
    setTimeout(() => resolve(),1000)
  })
  task.pause().then(() => {
    console.info(\`Succeeded in pausing a download task. \`);
  }).catch((err: BusinessError) => {
    console.error(\`Failed to pause the download task, Code: ${err.code}, message: ${err.message}\`);
  });
  console.info(\`Succeeded in creating a download task. result: ${task.tid}\`);
}).catch((err: BusinessError) => {
  console.error(\`Failed to create a download task, Code: ${err.code}, message: ${err.message}\`);
});

#### \[h2\]resume10+

resume(callback: AsyncCallback<void>): void

Resumes a paused task. This API uses an asynchronous callback to return the result.

**Required permissions**: ohos.permission.INTERNET

**System capability**: SystemCapability.Request.FileTransferAgent

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Upload and Download Error Codes](../../../error-codes/upload-and-download-error-codes/document.md) and [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 13400003 | Task service ability error. |
| 21900007 | Operation with wrong task state. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let config: request.agent.Config = {
  action: request.agent.Action.DOWNLOAD,
  url: 'http://127.0.0.1', // Replace the URL with the HTTP address of the real server.
  title: 'taskResumeTest',
  description: 'Sample code for resume the download task',
  mode: request.agent.Mode.BACKGROUND,
  overwrite: false,
  method: "GET",
  data: "",
  saveas: "./",
  network: request.agent.Network.CELLULAR,
  metered: false,
  roaming: true,
  retry: true,
  redirect: true,
  index: 0,
  begins: 0,
  ends: -1,
  gauge: false,
  precise: false,
  token: "it is a secret"
};
request.agent.create(context, config).then(async (task: request.agent.Task) => {
  task.start();
  // Wait for 1 second before executing the next step to prevent asynchronous out-of-order.
  await new Promise<void>((resolve) => {
    setTimeout(() => resolve(),1000)
  })
  task.pause();
  // Wait for 1 second before executing the next step to prevent asynchronous out-of-order.
  await new Promise<void>((resolve) => {
    setTimeout(() => resolve(),1000)
  })
  task.resume((err: BusinessError) => {
    if (err) {
      console.error(\`Failed to resume the download task, Code: ${err.code}, message: ${err.message}\`);
      return;
    }
    console.info(\`Succeeded in resuming a download task. \`);
  });
  console.info(\`Succeeded in creating a download task. result: ${task.tid}\`);
}).catch((err: BusinessError) => {
  console.error(\`Failed to create a download task, Code: ${err.code}, message: ${err.message}\`);
});

#### \[h2\]resume10+

resume(): Promise<void>

Resumes a paused task. This API uses a promise to return the result.

**Required permissions**: ohos.permission.INTERNET

**System capability**: SystemCapability.Request.FileTransferAgent

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Upload and Download Error Codes](../../../error-codes/upload-and-download-error-codes/document.md) and [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 13400003 | Task service ability error. |
| 21900007 | Operation with wrong task state. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let config: request.agent.Config = {
  action: request.agent.Action.DOWNLOAD,
  url: 'http://127.0.0.1', // Replace the URL with the HTTP address of the real server.
  title: 'taskResumeTest',
  description: 'Sample code for resume the download task',
  mode: request.agent.Mode.BACKGROUND,
  overwrite: false,
  method: "GET",
  data: "",
  saveas: "./",
  network: request.agent.Network.CELLULAR,
  metered: false,
  roaming: true,
  retry: true,
  redirect: true,
  index: 0,
  begins: 0,
  ends: -1,
  gauge: false,
  precise: false,
  token: "it is a secret"
};
request.agent.create(context, config).then(async (task: request.agent.Task) => {
  task.start();
  // Wait for 1 second before executing the next step to prevent asynchronous out-of-order.
  await new Promise<void>((resolve) => {
    setTimeout(() => resolve(),1000)
  })
  task.pause();
  // Wait for 1 second before executing the next step to prevent asynchronous out-of-order.
  await new Promise<void>((resolve) => {
    setTimeout(() => resolve(),1000)
  })
  task.resume().then(() => {
    console.info(\`Succeeded in resuming a download task. \`);
  }).catch((err: BusinessError) => {
    console.error(\`Failed to resume the download task, Code: ${err.code}, message: ${err.message}\`);
  });
  console.info(\`Succeeded in creating a download task. result: ${task.tid}\`);
}).catch((err: BusinessError) => {
  console.error(\`Failed to create a download task, Code: ${err.code}, message: ${err.message}\`);
});

#### \[h2\]stop10+

stop(callback: AsyncCallback<void>): void

Stops a task that is running, waiting, or retrying. A paused task can be resumed by [start](#start10). This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Request.FileTransferAgent

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Upload and Download Error Codes](../../../error-codes/upload-and-download-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 13400003 | Task service ability error. |
| 21900007 | Operation with wrong task state. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let config: request.agent.Config = {
  action: request.agent.Action.DOWNLOAD,
  url: 'http://127.0.0.1', // Replace the URL with the HTTP address of the real server.
  title: 'taskStopTest',
  description: 'Sample code for stop the download task',
  mode: request.agent.Mode.BACKGROUND,
  overwrite: false,
  method: "GET",
  data: "",
  saveas: "./",
  network: request.agent.Network.CELLULAR,
  metered: false,
  roaming: true,
  retry: true,
  redirect: true,
  index: 0,
  begins: 0,
  ends: -1,
  gauge: false,
  precise: false,
  token: "it is a secret"
};
request.agent.create(context, config).then(async (task: request.agent.Task) => {
  task.start();
  // Wait for 1 second before executing the next step to prevent asynchronous out-of-order.
  await new Promise<void>((resolve) => {
    setTimeout(() => resolve(),1000)
  })
  task.stop((err: BusinessError) => {
    if (err) {
      console.error(\`Failed to stop the download task, Code: ${err.code}, message: ${err.message}\`);
      return;
    }
    console.info(\`Succeeded in stopping a download task. \`);
  });
  console.info(\`Succeeded in creating a download task. result: ${task.tid}\`);
}).catch((err: BusinessError) => {
  console.error(\`Failed to create a download task, Code: ${err.code}, message: ${err.message}\`);
});

#### \[h2\]stop10+

stop(): Promise<void>

Stops a task that is running, waiting, or retrying. A paused task can be resumed by [start](#start10). This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Request.FileTransferAgent

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Upload and Download Error Codes](../../../error-codes/upload-and-download-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 13400003 | Task service ability error. |
| 21900007 | Operation with wrong task state. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let config: request.agent.Config = {
  action: request.agent.Action.DOWNLOAD,
  url: 'http://127.0.0.1', // Replace the URL with the HTTP address of the real server.
  title: 'taskStopTest',
  description: 'Sample code for stop the download task',
  mode: request.agent.Mode.BACKGROUND,
  overwrite: false,
  method: "GET",
  data: "",
  saveas: "./",
  network: request.agent.Network.CELLULAR,
  metered: false,
  roaming: true,
  retry: true,
  redirect: true,
  index: 0,
  begins: 0,
  ends: -1,
  gauge: false,
  precise: false,
  token: "it is a secret"
};
request.agent.create(context, config).then(async (task: request.agent.Task) => {
  task.start();
  // Wait for 1 second before executing the next step to prevent asynchronous out-of-order.
  await new Promise<void>((resolve) => {
    setTimeout(() => resolve(),1000)
  })
  task.stop().then(() => {
    console.info(\`Succeeded in stopping a download task. \`);
  }).catch((err: BusinessError) => {
    console.error(\`Failed to stop the download task, Code: ${err.code}, message: ${err.message}\`);
  });
  console.info(\`Succeeded in creating a download task. result: ${task.tid}\`);
}).catch((err: BusinessError) => {
  console.error(\`Failed to create a download task, Code: ${err.code}, message: ${err.message}\`);
});

#### \[h2\]setMaxSpeed18+

setMaxSpeed(speed: number): Promise<void>

Sets the maximum number of bytes that can be transmitted by a task per second. This API uses a promise to return the result.

**System capability**: SystemCapability.Request.FileTransferAgent

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| speed | number | Yes | Maximum number of bytes that can be transmitted by a task per second, with a minimum of 16384 bytes. The value cannot be less than the minimum speed value specified by [MinSpeed](#requestagentminspeed20). |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Upload and Download Error Codes](../../../error-codes/upload-and-download-error-codes/document.md) and [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Missing mandatory parameters. 2. Incorrect parameter type. 3. Parameter verification failed. |
| 13400003 | Task service ability error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let config: request.agent.Config = {
  action: request.agent.Action.DOWNLOAD,
  url: 'http://127.0.0.1', // Replace the URL with the HTTP address of the real server.
  saveas: "./",
};
request.agent.create(context, config).then((task: request.agent.Task) => {
  // Set the maximum transmission speed.
  task.setMaxSpeed(10 \* 1024 \* 1024).then(() => {
    console.info(\`Succeeded in setting the max speed of the task. result: ${task.tid}\`);
  }).catch((err: BusinessError) => {
    console.error(\`Failed to set the max speed of the task. result: ${task.tid}\`);
  });
}).catch((err: BusinessError) => {
  console.error(\`Failed to create a download task, Code: ${err.code}, message: ${err.message}\`);
});

#### request.agent.create10+

create(context: BaseContext, config: Config, callback: AsyncCallback<Task>): void

Creates an upload or download task and adds it to the queue. This API uses an asynchronous callback to return the result. HTTP/HTTPS is supported.

**Required permissions**: ohos.permission.INTERNET

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Request.FileTransferAgent

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/sjn043uGQZmU9VugIQ2e_g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=397CEE43C53131681A19ED3FCC7A9798FBF28E8E859C65171409DB9854F720AD)

For details about how to obtain the context in the example, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | [BaseContext](../../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/basecontext/document.md) | Yes | Application-based context. |
| config | [Config](#requestagentconfig10) | Yes | Task configuration. |
| callback | AsyncCallback<[Task](#requestagenttask10)\> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the **Task** object obtained. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Upload and Download Error Codes](../../../error-codes/upload-and-download-error-codes/document.md) and [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Missing mandatory parameters. 2. Incorrect parameter type. 3. Parameter verification failed. |
| 13400001 | Invalid file or file system error. |
| 13400003 | Task service ability error. |
| 21900004 | The application task queue is full. |
| 21900005 | Operation with wrong task mode. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let attachments: Array<request.agent.FormItem> = \[{
  name: "createTest",
  value: {
    filename: "createTest.avi",
    path: "./createTest.avi",
  }
}\];
let config: request.agent.Config = {
  action: request.agent.Action.UPLOAD,
  url: 'http://127.0.0.1', // Replace the URL with the HTTP address of the real server.
  title: 'createTest',
  description: 'Sample code for create task',
  mode: request.agent.Mode.BACKGROUND,
  overwrite: false,
  method: "PUT",
  data: attachments,
  saveas: "./",
  network: request.agent.Network.CELLULAR,
  metered: false,
  roaming: true,
  retry: true,
  redirect: true,
  index: 0,
  begins: 0,
  ends: -1,
  gauge: false,
  precise: false,
  token: "it is a secret"
};
request.agent.create(context, config, async (err: BusinessError, task: request.agent.Task) => {
  if (err) {
    console.error(\`Failed to create a download task, Code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info(\`Succeeded in creating a download task. result: ${task.config}\`);
  await task.start();
  // You need to manually call remove() to end the lifecycle of the task object.
  request.agent.remove(task.tid);
});

#### request.agent.create10+

create(context: BaseContext, config: Config): Promise<Task>

Creates an upload or download task and adds it to the queue. This API uses a promise to return the result. HTTP/HTTPS is supported.

**Required permissions**: ohos.permission.INTERNET

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Request.FileTransferAgent

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/RlxIVcuzSYy0jO4T5m3H6g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=26A697B735CEB5DCDEBA139E484A3656E00C10A713C8EB1B64282B77BBDAEDA2)

For details about how to obtain the context in the example, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | [BaseContext](../../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/basecontext/document.md) | Yes | Application-based context. |
| config | [Config](#requestagentconfig10) | Yes | Task configuration. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[Task](#requestagenttask10)\> | Promise used to return the created task. |

**Error codes**

For details about the error codes, see [Upload and Download Error Codes](../../../error-codes/upload-and-download-error-codes/document.md) and [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Missing mandatory parameters. 2. Incorrect parameter type. 3. Parameter verification failed. |
| 13400001 | Invalid file or file system error. |
| 13400003 | Task service ability error. |
| 21900004 | The application task queue is full. |
| 21900005 | Operation with wrong task mode. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let attachments: Array<request.agent.FormItem> = \[{
  name: "createTest",
  value: {
    filename: "createTest.avi",
    path: "./createTest.avi",
  }
}\];
let config: request.agent.Config = {
  action: request.agent.Action.UPLOAD,
  url: 'http://127.0.0.1', // Replace the URL with the HTTP address of the real server.
  title: 'createTest',
  description: 'Sample code for create task',
  mode: request.agent.Mode.BACKGROUND,
  overwrite: false,
  method: "PUT",
  data: attachments,
  saveas: "./",
  network: request.agent.Network.CELLULAR,
  metered: false,
  roaming: true,
  retry: true,
  redirect: true,
  index: 0,
  begins: 0,
  ends: -1,
  gauge: false,
  precise: false,
  token: "it is a secret"
};
request.agent.create(context, config).then(async (task: request.agent.Task) => {
  console.info(\`Succeeded in creating a download task. result: ${task.config}\`);
  await task.start();
  // You need to manually call remove() to end the lifecycle of the task object.
  request.agent.remove(task.tid);
}).catch((err: BusinessError) => {
  console.error(\`Failed to create a download task, Code: ${err.code}, message: ${err.message}\`);
});

#### request.agent.getTask11+

getTask(context: BaseContext, id: string, token?: string): Promise<Task>

Obtains task information based on the task ID. This API uses a promise to return the result.

**System capability**: SystemCapability.Request.FileTransferAgent

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | [BaseContext](../../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/basecontext/document.md) | Yes | Application-based context. |
| id | string | Yes | Task ID. |
| token | string | No | Token for task query. The default value is empty. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[Task](#requestagenttask10)\> | Promise used to return the task information. |

**Error codes**

For details about the error codes, see [Upload and Download Error Codes](../../../error-codes/upload-and-download-error-codes/document.md) and [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Missing mandatory parameters. 2. Incorrect parameter type. 3. Parameter verification failed. |
| 13400003 | Task service ability error. |
| 21900006 | Task removed or not found. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
request.agent.getTask(context, "123456").then((task: request.agent.Task) => {
  console.info(\`Succeeded in querying a task. result: ${task.tid}\`);
}).catch((err: BusinessError) => {
  console.error(\`Failed to query a task, Code: ${err.code}, message: ${err.message}\`);
});

#### request.agent.remove10+

remove(id: string, callback: AsyncCallback<void>): void

Removes a specified task of the invoker. If the task is being executed, the task is forced to stop. This API uses an asynchronous callback to return the result. After this API is called, the **task** object and its callback function are released.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Request.FileTransferAgent

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| id | string | Yes | Task ID. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Upload and Download Error Codes](../../../error-codes/upload-and-download-error-codes/document.md) and [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Missing mandatory parameters. 2. Incorrect parameter type. |
| 13400003 | Task service ability error. |
| 21900006 | Task removed or not found. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

request.agent.remove("123456", (err: BusinessError) => {
  if (err) {
    console.error(\`Failed to remove a download task, Code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info(\`Succeeded in removing a download task.\`);
});

#### request.agent.remove10+

remove(id: string): Promise<void>

Removes a specified task of the invoker. If the task is being executed, the task is forced to stop. This API uses a promise to return the result. After this API is called, the **task** object and its callback function are released.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Request.FileTransferAgent

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| id | string | Yes | Task ID. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Upload and Download Error Codes](../../../error-codes/upload-and-download-error-codes/document.md) and [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Missing mandatory parameters. 2. Incorrect parameter type. |
| 13400003 | Task service ability error. |
| 21900006 | Task removed or not found. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

request.agent.remove("123456").then(() => {
  console.info(\`Succeeded in removing a download task. \`);
}).catch((err: BusinessError) => {
  console.error(\`Failed to remove a download task, Code: ${err.code}, message: ${err.message}\`);
});

#### request.agent.show10+

show(id: string, callback: AsyncCallback<TaskInfo>): void

Queries a task details based on the task ID. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Request.FileTransferAgent

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| id | string | Yes | Task ID. |
| callback | AsyncCallback<[TaskInfo](#requestagenttaskinfo10)\> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the **TaskInfo** object obtained. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Upload and Download Error Codes](../../../error-codes/upload-and-download-error-codes/document.md) and [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Missing mandatory parameters. 2. Incorrect parameter type. |
| 13400003 | Task service ability error. |
| 21900006 | Task removed or not found. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

request.agent.show("123456", (err: BusinessError, taskInfo: request.agent.TaskInfo) => {
  if (err) {
    console.error(\`Failed to show a upload task, Code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info(\`Succeeded in showing a upload task.\`);
});

#### request.agent.show10+

show(id: string): Promise<TaskInfo>

Queries a task details based on the task ID. This API uses a promise to return the result.

**System capability**: SystemCapability.Request.FileTransferAgent

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| id | string | Yes | Task ID. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[TaskInfo](#requestagenttaskinfo10)\> | Promise used to return the **TaskInfo** object. |

**Error codes**

For details about the error codes, see [Upload and Download Error Codes](../../../error-codes/upload-and-download-error-codes/document.md) and [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Missing mandatory parameters. 2. Incorrect parameter type. |
| 13400003 | Task service ability error. |
| 21900006 | Task removed or not found. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

request.agent.show("123456").then((taskInfo: request.agent.TaskInfo) => {
  console.info(\`Succeeded in showing a upload task.\`);
}).catch((err: BusinessError) => {
  console.error(\`Failed to show a upload task, Code: ${err.code}, message: ${err.message}\`);
});

#### request.agent.touch10+

touch(id: string, token: string, callback: AsyncCallback<TaskInfo>): void

Queries the task details based on the task ID and token. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Request.FileTransferAgent

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| id | string | Yes | Task ID. |
| token | string | Yes | Token for task query. |
| callback | AsyncCallback<[TaskInfo](#requestagenttaskinfo10)\> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the **TaskInfo** object obtained. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Upload and Download Error Codes](../../../error-codes/upload-and-download-error-codes/document.md) and [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Missing mandatory parameters. 2. Incorrect parameter type. 3. Parameter verification failed. |
| 13400003 | Task service ability error. |
| 21900006 | Task removed or not found. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

request.agent.touch("123456", "token", (err: BusinessError, taskInfo: request.agent.TaskInfo) => {
  if (err) {
    console.error(\`Failed to touch a upload task, Code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info(\`Succeeded in touching a upload task.\`);
});

#### request.agent.touch10+

touch(id: string, token: string): Promise<TaskInfo>

Queries the task details based on the task ID and token. This API uses a promise to return the result.

**System capability**: SystemCapability.Request.FileTransferAgent

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| id | string | Yes | Task ID. |
| token | string | Yes | Token for task query. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[TaskInfo](#requestagenttaskinfo10)\> | Promise used to return the **TaskInfo** object. |

**Error codes**

For details about the error codes, see [Upload and Download Error Codes](../../../error-codes/upload-and-download-error-codes/document.md) and [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Missing mandatory parameters. 2. Incorrect parameter type. 3. Parameter verification failed. |
| 13400003 | Task service ability error. |
| 21900006 | Task removed or not found. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

request.agent.touch("123456", "token").then((taskInfo: request.agent.TaskInfo) => {
  console.info(\`Succeeded in touching a upload task. \`);
}).catch((err: BusinessError) => {
  console.error(\`Failed to touch a upload task, Code: ${err.code}, message: ${err.message}\`);
});

#### request.agent.search10+

search(callback: AsyncCallback<Array<string>>): void

Searches for task IDs based on [Filter](#requestagentfilter10). The IDs of all tasks from the invoking time to 24 hours ago are searched. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Request.FileTransferAgent

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<Array<string>> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the task ID. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Upload and Download Error Codes](../../../error-codes/upload-and-download-error-codes/document.md) and [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter type. 2. Parameter verification failed. |
| 13400003 | Task service ability error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

request.agent.search((err: BusinessError, data: Array<string>) => {
  if (err) {
    console.error(\`Failed to search a upload task, Code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info(\`Succeeded in searching a upload task. \`);
});

#### request.agent.search10+

search(filter: Filter, callback: AsyncCallback<Array<string>>): void

Searches for task IDs based on [Filter](#requestagentfilter10). This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Request.FileTransferAgent

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| filter | [Filter](#requestagentfilter10) | Yes | Filter criteria. |
| callback | AsyncCallback<Array<string>> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the task ID. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Upload and Download Error Codes](../../../error-codes/upload-and-download-error-codes/document.md) and [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter type. 2. Parameter verification failed. |
| 13400003 | Task service ability error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let filter: request.agent.Filter = {
  action: request.agent.Action.UPLOAD,
  mode: request.agent.Mode.BACKGROUND
}
request.agent.search(filter, (err: BusinessError, data: Array<string>) => {
  if (err) {
    console.error(\`Failed to search a upload task, Code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info(\`Succeeded in searching a upload task. \`);
});

#### request.agent.search10+

search(filter?: Filter): Promise<Array<string>>

Searches for task IDs based on [Filter](#requestagentfilter10). This API uses a promise to return the result.

**System capability**: SystemCapability.Request.FileTransferAgent

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| filter | [Filter](#requestagentfilter10) | No | Filter criteria. The default value is empty. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<string>> | Promise used to return the task IDs that meet the filter criteria. |

**Error codes**

For details about the error codes, see [Upload and Download Error Codes](../../../error-codes/upload-and-download-error-codes/document.md) and [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter type. 2. Parameter verification failed. |
| 13400003 | Task service ability error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let filter: request.agent.Filter = {
  action: request.agent.Action.UPLOAD,
  mode: request.agent.Mode.BACKGROUND
}
request.agent.search(filter).then((data: Array<string>) => {
  console.info(\`Succeeded in searching a upload task. \`);
}).catch((err: BusinessError) => {
  console.error(\`Failed to search a upload task, Code: ${err.code}, message: ${err.message}\`);
});

#### request.agent.createGroup15+

createGroup(config: GroupConfig): Promise<string>

Creates a group based on [GroupConfig](#requestagentgroupconfig15). This API uses a promise to return the result.

**System capability**: SystemCapability.Request.FileTransferAgent

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| config | [GroupConfig15+](#requestagentgroupconfig15) | Yes | Group options for a download task. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<string> | Promise used to return the ID of the created group. |

**Error codes**

For details about the error codes, see [Upload and Download Error Codes](../../../error-codes/upload-and-download-error-codes/document.md) and [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Missing mandatory parameters. 2. Incorrect parameter type. 3. Parameter verification failed. |
| 13400003 | Task service ability error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

// Prepare the GroupConfig object.
let config: request.agent.GroupConfig = {
    notification: {},
};
// Call the createGroup API to create a group.
request.agent.createGroup(config).then((gid: string) => {
  console.info(\`Succeeded in creating a download task group. \`);
}).catch((err: BusinessError) => {
  console.error(\`Failed to create a download group, Code: ${err.code}, message: ${err.message}\`);
});

#### request.agent.attachGroup15+

attachGroup(gid: string, tids: string\[\]): Promise<void>

Attaches multiple download task IDs to a specified group ID. This API uses a promise to return the result.

If any task ID does not meet the attachment conditions, all tasks in the list will not be added to the group.

**System capability**: SystemCapability.Request.FileTransferAgent

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| gid | string | Yes | Target group ID. |
| tids | string\[\] | Yes | List of task IDs to attach. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Upload and Download Error Codes](../../../error-codes/upload-and-download-error-codes/document.md) and [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Missing mandatory parameters. 2. Incorrect parameter type. 3. Parameter verification failed. |
| 13400003 | Task service ability error. |
| 21900005 | Operation with wrong task mode. |
| 21900006 | Task removed or not found. |
| 21900007 | Operation with wrong task state. |
| 21900008 | Group deleted or not found. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

// Prepare the group ID and task ID list.
let groupId: string = "123456789";
let taskIds: string\[\] = \["1111", "2222", "3333", "4444"\];
// Call the attachGroup API to add a task ID list to the group.
request.agent.attachGroup(groupId, taskIds).then(() => {
  console.info(\`Succeeded in attaching tasks to the download task group.\`);
}).catch((err: BusinessError) => {
  console.error(\`Failed to attach tasks to the download group, Code: ${err.code}, message: ${err.message}\`);
});

#### request.agent.deleteGroup15+

deleteGroup(gid: string): Promise<void>

Deletes a specified group. No task ID can be added to the group. This API uses a promise to return the result.

When all tasks in a group are succeeded, failed, or removed and the group is deleted, the completion and failure notifications of this group are displayed.

**System capability**: SystemCapability.Request.FileTransferAgent

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| gid | string | Yes | Target group ID. The value must be the same as the ID of the created task group, that is, the return value of the task group created using the [request.agent.createGroup](#requestagentcreategroup15) API. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Upload and Download Error Codes](../../../error-codes/upload-and-download-error-codes/document.md) and [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Missing mandatory parameters. 2. Incorrect parameter type. 3. Parameter verification failed. |
| 13400003 | Task service ability error. |
| 21900008 | Group deleted or not found. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

// Prepare the group ID.
let groupId: string = "123456789";

// Call the deleteGroup API to delete a group.
request.agent.deleteGroup(groupId).then(() => {
  console.info(\`Succeeded in deleting the download task group.\`);
}).catch((err: BusinessError) => {
  console.error(\`Failed to delete the download group, Code: ${err.code}, message: ${err.message}\`);
});
