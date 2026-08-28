# @ohos.file.cloudSync (Device-Cloud Sync)

The **cloudSync** module provides the device-cloud synchronization capabilities for applications. You can use the APIs to start or stop device-cloud synchronization and start or stop the download of images.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/_dXKxB2EQXCgoVYMPuL8Ow/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062319Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=43DD910DA8A40E0653C34CED0931995FFC98D185C7B917BFB1F4CEC76086B686)

The initial APIs of this module are supported since API version 10. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { cloudSync } from '@kit.CoreFileKit';

#### SyncState12+

Enumerates the device-cloud sync states.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/MI7N6x2dQRC3cgRXRRKkGw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062319Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9788546D267BA81FD0AF305DC061A36086C12463D1994D01434BBF609FE4EE60)

If a sync progress event listener is registered for an application, a callback will be invoked to notify the application when the device-cloud sync state is changed.

**System capability**: SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| UPLOADING | 0 | The file is being uploaded. |
| UPLOAD\_FAILED | 1 | Upload failed. |
| DOWNLOADING | 2 | The file is being downloaded. |
| DOWNLOAD\_FAILED | 3 | Download failed. |
| COMPLETED | 4 | Sync completed. |
| STOPPED | 5 | Sync stopped. |

#### ErrorType12+

Enumerates the device-cloud sync errors.

-   In the current phase, **NETWORK\_UNAVAILABLE** is returned only when the mobile data network and Wi-Fi are unavailable. If the mobile data network is available, the synchronization can be performed normally.
-   During the sync process, if the battery level is lower than 10% in non-charging scenarios, **BATTERY\_LEVEL\_LOW** will be return when the current upload is complete.
-   When sync is being triggered, if the battery level is lower than 10% in non-charging scenarios, sync is not allowed and an error code will be returned by **start()**.
-   If the cloud space is insufficient when a file is uploaded, the upload will fail and there is no such a file in the cloud.

**System capability**: SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| NO\_ERROR | 0 | No error. |
| NETWORK\_UNAVAILABLE | 1 | No network is available. |
| WIFI\_UNAVAILABLE | 2 | Wi-Fi is unavailable. |
| BATTERY\_LEVEL\_LOW | 3 | The battery level is lower than 10%. |
| BATTERY\_LEVEL\_WARNING | 4 | The battery level is lower than 15%. |
| CLOUD\_STORAGE\_FULL | 5 | The cloud space is insufficient. |
| LOCAL\_STORAGE\_FULL | 6 | The local space is insufficient. |
| DEVICE\_TEMPERATURE\_TOO\_HIGH | 7 | The device temperature is too high. |
| REMOTE\_SERVER\_ABNORMAL20+ | 8 | The remote service is unavailable. |

#### SyncProgress12+

Represents information about the device-cloud sync progress.

#### \[h2\]Property

**System capability**: SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| state | [SyncState](#syncstate12) | No | No | Device-cloud sync state. |
| error | [ErrorType](#errortype12) | No | No | Sync error. |

#### State11+

Enumerates the download states of a cloud file.

**System capability**: SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| RUNNING | 0 | The cloud file is being downloaded. |
| COMPLETED | 1 | The cloud file download is complete. |
| FAILED | 2 | The cloud file download failed. |
| STOPPED | 3 | The cloud file download is stopped. |

#### DownloadProgress11+

Represents information about the download progress of a cloud file.

#### \[h2\]Property

**System capability**: SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| state | [State](#state11) | No | No | File download state. |
| processed | number | No | No | Size of the downloaded data, in bytes. The value range is \[0, 9223372036854775807\]. |
| size | number | No | No | Size of the cloud file, in bytes. The value range is \[0, 9223372036854775807\]. |
| uri | string | No | No | URI of the cloud file. |
| error | [DownloadErrorType](#downloaderrortype11) | No | No | Download error type. |

#### FileSync12+

Provides APIs for the file manager application to perform device-cloud sync of the files stored in the Drive Kit. Before using the APIs of this class, you need to create a **FileSync** instance.

**System capability**: SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

#### \[h2\]constructor12+

constructor()

A constructor used to create a **FileSync** instance.

**System capability**: SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | The input parameter is invalid. Possible causes:Incorrect parameter types. |

**Example**

let fileSync = new cloudSync.FileSync()

#### \[h2\]on12+

on(event: 'progress', callback: Callback<SyncProgress>): void

Registers a listener for the device-cloud sync progress.

**System capability**: SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | string | Yes | Event type. The value is **progress**, which indicates the sync progress event. |
| callback | Callback<[SyncProgress](#syncprogress12)\> | Yes | Callback used to return the sync progress information. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [File Management Error Codes](../../error-codes/file-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | The input parameter is invalid. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 13600001 | IPC error. |

**Example**

let fileSync = new cloudSync.FileSync();
let callback = (pg: cloudSync.SyncProgress) => {
  console.info("file sync state: " + pg.state + "error type:" + pg.error);
}

fileSync.on('progress', callback);

#### \[h2\]off12+

off(event: 'progress', callback?: Callback<SyncProgress>): void

Removes the specified callback from the device-cloud sync progress.

**System capability**: SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | string | Yes | Event type. The value is **progress**, which indicates the sync progress event. |
| callback | Callback<[SyncProgress](#syncprogress12)\> | No | Callback used to return the sync progress. The default value is null. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [File Management Error Codes](../../error-codes/file-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | The input parameter is invalid. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 13600001 | IPC error. |

**Example**

let fileSync = new cloudSync.FileSync();

let callback = (pg: cloudSync.SyncProgress) => {
  console.info("file sync state: " + pg.state + "error type:" + pg.error);
}

fileSync.on('progress', callback);

fileSync.off('progress', callback);

#### \[h2\]start12+

start(): Promise<void>

Starts device-cloud sync of a file. This API uses a promise to return the result.

**System capability**: SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [File Management Error Codes](../../error-codes/file-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | The input parameter is invalid. Possible causes:Incorrect parameter types. |
| 13600001 | IPC error. |
| 22400001 | Cloud status not ready. |
| 22400002 | Network unavailable. |
| 22400003 | Low battery level. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let fileSync = new cloudSync.FileSync();

let callback = (pg: cloudSync.SyncProgress) => {
  console.info("file sync state: " + pg.state + "error type:" + pg.error);
}

fileSync.on('progress', callback);

fileSync.start().then(() => {
  console.info("start sync successfully");
}).catch((err: BusinessError) => {
  console.error("start sync failed with error message: " + err.message + ", error code: " + err.code);
});

#### \[h2\]start12+

start(callback: AsyncCallback<void>): void

Starts device-cloud sync of a file. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [File Management Error Codes](../../error-codes/file-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | The input parameter is invalid. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 13600001 | IPC error. |
| 22400001 | Cloud status not ready. |
| 22400002 | Network unavailable. |
| 22400003 | Low battery level. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let fileSync = new cloudSync.FileSync();

fileSync.start((err: BusinessError) => {
  if (err) {
    console.error("start sync failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("start sync successfully");
  }
});

#### \[h2\]stop12+

stop(): Promise<void>

Stops device-cloud sync of a file. This API uses a promise to return the result.

Calling **stop** will stop the sync process. To resume the sync, call [start](#start12).

**System capability**: SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [File Management Error Codes](../../error-codes/file-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | The input parameter is invalid. Possible causes:Incorrect parameter types. |
| 13600001 | IPC error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let fileSync = new cloudSync.FileSync();

fileSync.stop().then(() => {
  console.info("stop sync successfully");
}).catch((err: BusinessError) => {
  console.error("stop sync failed with error message: " + err.message + ", error code: " + err.code);
});

#### \[h2\]stop12+

stop(callback: AsyncCallback<void>): void

Stops device-cloud sync of a file. This API uses an asynchronous callback to return the result.

Calling **stop** will stop the sync process. To resume the sync, call [start](#start12).

**System capability**: SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [File Management Error Codes](../../error-codes/file-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | The input parameter is invalid. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 13600001 | IPC error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let fileSync = new cloudSync.FileSync();

fileSync.stop((err: BusinessError) => {
  if (err) {
    console.error("stop sync failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("stop sync successfully");
  }
});

#### \[h2\]getLastSyncTime12+

getLastSyncTime(): Promise<number>

Obtains the last sync time. This API uses a promise to return the result.

**System capability**: SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the last sync time obtained. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [File Management Error Codes](../../error-codes/file-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | The input parameter is invalid. Possible causes:Incorrect parameter types. |
| 13600001 | IPC error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let fileSync = new cloudSync.FileSync();

fileSync.getLastSyncTime().then((timeStamp: number) => {
  let date = new Date(timeStamp);
  console.info("get last sync time successfully:"+ date);
}).catch((err: BusinessError) => {
  console.error("get last sync time failed with error message: " + err.message + ", error code: " + err.code);
});

#### \[h2\]getLastSyncTime12+

getLastSyncTime(callback: AsyncCallback<number>): void

Obtains the last sync time. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<number> | Yes | Callback used to return the last sync time obtained. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [File Management Error Codes](../../error-codes/file-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | The input parameter is invalid. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 13600001 | IPC error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let fileSync = new cloudSync.FileSync();

fileSync.getLastSyncTime((err: BusinessError, timeStamp: number) => {
  if (err) {
    console.error("get last sync time with error message: " + err.message + ", error code: " + err.code);
  } else {
    let date = new Date(timeStamp);
    console.info("get last sync time successfully:"+ date);
  }
});

#### CloudFileCache11+

Provides APIs for the file manager application to download files from the Drive Kit to a local device.

**System capability**: SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

#### \[h2\]construct11+

constructor()

A constructor used to create a **CloudFileCache** instance. Data is not shared between multiple instances.

**System capability**: SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | The input parameter is invalid. Possible causes:Incorrect parameter types. |

**Example**

let fileCache = new cloudSync.CloudFileCache();

#### \[h2\]on11+

on(event: 'progress', callback: Callback<DownloadProgress>): void

Registers a listener for the download progress of a file from the Drive Kit.

**System capability**: SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | string | Yes | Event. The value is **progress**, which indicates the download progress event of a cloud file. |
| callback | Callback<[DownloadProgress](#downloadprogress11)\> | Yes | Callback for the download progress event of a file from the Drive Kit. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [File Management Error Codes](../../error-codes/file-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | The input parameter is invalid. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 13600001 | IPC error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let fileCache = new cloudSync.CloudFileCache();
let callback = (pg: cloudSync.DownloadProgress) => {
  console.info("download state: " + pg.state);
};

try {
  fileCache.on('progress', callback);
} catch (e) {
  const error = e as BusinessError;
  console.error(\`Error code: ${error.code}, message: ${error.message}\`);
}

#### \[h2\]on20+

on(event: 'batchDownload', callback: Callback<MultiDownloadProgress>): void

Registers a listener for the batch download of a file from the Drive Kit.

**System capability**: SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | string | Yes | Event type. The value is **'batchDownload'**, indicating the batch download event. |
| callback | Callback<[MultiDownloadProgress](#multidownloadprogress20)\> | Yes | Callback for the batch download event of a file from the Drive Kit. |

**Error codes**

For details about the error codes, see [File Management Error Codes](../../error-codes/file-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 13900020 | Invalid argument. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 22400005 | Inner error. Possible causes: 1.Failed to access the database or execute the SQL statement. 2.System error, such as a null pointer, insufficient memory or a JS engine exception. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let fileCache = new cloudSync.CloudFileCache();
let callback = (data: cloudSync.MultiDownloadProgress) => {
  console.info(\`Batch download progress: downloadedSize: ${data.downloadedSize}, totalSize: ${data.totalSize}\`);
  if (data.state == cloudSync.State.COMPLETED) {
    console.info('Batch download finished.');
  } else if (data.state == cloudSync.State.FAILED) {
    console.info(\`Batch download stopped, error type: ${data.errType}.\`);
  }
};

try {
  fileCache.on('batchDownload', callback);
} catch (e) {
  let error = e as BusinessError;
  console.error(\`Failed to register download callback, error code: ${error.code}, message: ${error.message}\`);
}

#### \[h2\]off11+

off(event: 'progress', callback?: Callback<DownloadProgress>): void

Removes the specified callback from the device-cloud file cache progress.

**System capability**: SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | string | Yes | Event type. The value is **progress**, which indicates the sync progress event. |
| callback | Callback<[DownloadProgress](#downloadprogress11)\> | No | Callback for the download progress event of a file from the Drive Kit. If this parameter is not specified, this API unregisters all callbacks for the download progress event. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [File Management Error Codes](../../error-codes/file-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | The input parameter is invalid. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 13600001 | IPC error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let fileCache = new cloudSync.CloudFileCache();

let callback = (pg: cloudSync.DownloadProgress) => {
  console.info("download state: " + pg.state);
}

try {
  fileCache.on('progress', callback);
  fileCache.off('progress', callback);
} catch (e) {
  const error = e as BusinessError;
  console.error(\`Error code: ${error.code}, message: ${error.message}\`);
}

#### \[h2\]off20+

off(event: 'batchDownload', callback?: Callback<MultiDownloadProgress>): void

Removes the listener added via the [on](#on20) API for file batch downloads.

**System capability**: SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | string | Yes | Event type. The value is **'batchDownload'**, indicating the batch download event. |
| callback | Callback<[MultiDownloadProgress](#multidownloadprogress20)\> | No | Callback for the batch download of a file from the Drive Kit. If this parameter is set, the specified callback will be canceled; otherwise, all currently subscribed callbacks of the same event type will be canceled. |

**Error codes**

For details about the error codes, see [File Management Error Codes](../../error-codes/file-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 13900020 | Invalid argument. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 22400005 | Inner error. Possible causes: 1.Failed to access the database or execute the SQL statement. 2.System error, such as a null pointer, insufficient memory or a JS engine exception. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let fileCache = new cloudSync.CloudFileCache();
let callback = (pg: cloudSync.MultiDownloadProgress) => {
  console.info("download state: " + pg.state);
}

try {
  fileCache.on('batchDownload', callback);
  fileCache.off('batchDownload', callback);
} catch (e) {
  let error = e as BusinessError;
  console.error(\`Failed to unregister download callback, error code: ${error.code}, message: ${error.message}\`);
}

#### \[h2\]start11+

start(uri: string): Promise<void>

Starts to download a file from the Drive Kit to the local device. This API uses a promise to return the result.

**System capability**: SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| uri | string | Yes | URI of the file to download. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [File Management Error Codes](../../error-codes/file-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | The input parameter is invalid. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 13600001 | IPC error. |
| 13900002 | No such file or directory. |
| 13900025 | No space left on device. |
| 14000002 | Invalid URI. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { fileUri } from '@kit.CoreFileKit';

let fileCache = new cloudSync.CloudFileCache();
let path = "/data/storage/el2/cloud/1.txt";
let uri = fileUri.getUriFromPath(path);

try {
  fileCache.on('progress', (pg: cloudSync.DownloadProgress) => {
    console.info("download state:" + pg.state);
  });
} catch (e) {
  const error = e as BusinessError;
  console.error(\`Error code: ${error.code}, message: ${error.message}\`);
}

fileCache.start(uri).then(() => {
  console.info("start download successfully");
}).catch((err: BusinessError) => {
  console.error("start download failed with error message: " + err.message + ", error code: " + err.code);
});

#### \[h2\]start11+

start(uri: string, callback: AsyncCallback<void>): void

Starts to download a file from the Drive Kit to the local device. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| uri | string | Yes | URI of the file to download. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [File Management Error Codes](../../error-codes/file-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | The input parameter is invalid. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 13600001 | IPC error. |
| 13900002 | No such file or directory. |
| 13900025 | No space left on device. |
| 14000002 | Invalid URI. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { fileUri } from '@kit.CoreFileKit';

let fileCache = new cloudSync.CloudFileCache();
let path = "/data/storage/el2/cloud/1.txt";
let uri = fileUri.getUriFromPath(path);

fileCache.start(uri, (err: BusinessError) => {
  if (err) {
    console.error("start download failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("start download successfully");
  }
});

#### \[h2\]startBatch20+

startBatch(uris: Array<string>, fileType?: DownloadFileType): Promise<number>

Starts the batch download of a file from the Drive Kit. This API uses a promise to return the result.

Different batch download tasks can be distinguished by the task ID returned.

**System capability**: SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| uris | Array<string> | Yes | URI list. A maximum of 400 URIs can be transferred at a time. An error (22400004) will be thrown if the number of URIs exceeds 400. |
| fileType | [DownloadFileType](#downloadfiletype20) | No | File type. The default value is **CONTENT**. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the ID of the batch download task. |

**Error codes**

For details about the error codes, see [File Management Error Codes](../../error-codes/file-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 13600001 | IPC error. Possible causes: 1.IPC failed or timed out. 2.Failed to load the service. |
| 13900020 | Invalid argument. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 14000002 | Invalid uri. |
| 22400004 | Exceed the maximum limit. |
| 22400005 | Inner error. Possible causes: 1.Failed to access the database or execute the SQL statement. 2.System error, such as a null pointer, insufficient memory or a JS engine exception. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let fileCache = new cloudSync.CloudFileCache();
try {
  fileCache.on('batchDownload', (pg: cloudSync.MultiDownloadProgress) => {
    console.info(\`batch download state: ${pg.state}\`);
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(\`Failed to unregister download callback, error code: ${error.code}, message: ${error.message}\`);
}

let uriList: Array<string> = \[\];
fileCache.startBatch(uriList, cloudSync.DownloadFileType.CONTENT).then((downloadId: number) => {
  console.info(\`start batch download successfully, taskId: ${downloadId}\`);
}).catch((err: BusinessError) => {
  console.error(\`start download failed with error message: ${err.message}, error code: ${err.code}\`);
});

#### \[h2\]stop11+

stop(uri: string, needClean?: boolean): Promise<void>

Stops downloading a file from the Drive Kit to the local device. This API uses a promise to return the result.

When **stop()** is called, the current file download process terminates, and downloaded files are retained by default. You can call **start()** to resume the download.

**System capability**: SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| uri | string | Yes | URI of the file to download. |
| needClean12+ | boolean | No | 
Whether to delete the downloaded files. The default value **false** means not to delete the downloaded files; the value **true** means the opposite.

This parameter is available since API version 12.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [File Management Error Codes](../../error-codes/file-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | The input parameter is invalid. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 13600001 | IPC error. |
| 13900002 | No such file or directory. |
| 14000002 | Invalid URI. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { fileUri } from '@kit.CoreFileKit';

let fileCache = new cloudSync.CloudFileCache();
let path = "/data/storage/el2/cloud/1.txt";
let uri = fileUri.getUriFromPath(path);

fileCache.stop(uri, true).then(() => {
  console.info("stop download successfully");
}).catch((err: BusinessError) => {
  console.error("stop download failed with error message: " + err.message + ", error code: " + err.code);
});

#### \[h2\]stop11+

stop(uri: string, callback: AsyncCallback<void>): void

Stops downloading a file from the Drive Kit to the local device. This API uses an asynchronous callback to return the result.

When **stop()** is called, the current file download process terminates, and downloaded files are retained. You can call **start()** to resume the download.

**System capability**: SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| uri | string | Yes | URI of the file to download. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [File Management Error Codes](../../error-codes/file-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | The input parameter is invalid. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 13600001 | IPC error. |
| 13900002 | No such file or directory. |
| 14000002 | Invalid URI. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { fileUri } from '@kit.CoreFileKit';

let fileCache = new cloudSync.CloudFileCache();
let path = "/data/storage/el2/cloud/1.txt";
let uri = fileUri.getUriFromPath(path);

fileCache.stop(uri, (err: BusinessError) => {
  if (err) {
    console.error("stop download failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("stop download successfully");
  }
});

#### \[h2\]stopBatch20+

stopBatch(downloadId: number, needClean?: boolean): Promise<void>

Stops the batch download task enabled by [startBatch](#startbatch20) of a file from the Drive Kit. This API uses a promise to return the result.

When **stopBatch()** is called, the batch download terminates. The **needClean** parameter determines whether to delete incompletely downloaded files.

**System capability**: SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| downloadId | number | Yes | ID of the download task to be stopped. |
| needClean | boolean | No | Whether to delete incompletely downloaded files. The default value **false** means not to delete the files; the value **true** means the opposite. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [File Management Error Codes](../../error-codes/file-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 13600001 | IPC error. Possible causes: 1.IPC failed or timed out. 2.Failed to load the service. |
| 13900020 | Invalid argument. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 22400005 | Inner error. Possible causes: 1.Failed to access the database or execute the SQL statement. 2.System error, such as a null pointer, insufficient memory or a JS engine exception. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let taskId = -1;
let uriList: Array<string> = \[\];
let fileCache = new cloudSync.CloudFileCache();
fileCache.startBatch(uriList, cloudSync.DownloadFileType.CONTENT).then((downloadId: number) => {
  taskId = downloadId;
  console.info("start batch download successfully");
}).catch((err: BusinessError) => {
  console.error(\`start batch download failed with error message: ${err.message}, error code: ${err.code}\`);
});

let needStop = true;
if (needStop && taskId > 0) {
  fileCache.stopBatch(taskId, true).then(() => {
    console.info("stop batch download successfully");
  }).catch((err: BusinessError) => {
    console.error(\`stop batch download failed with error message: ${err.message}, error code: ${err.code}\`);
  });
}

#### \[h2\]cleanFileCache20+

cleanFileCache(uri: string): void

Deletes a cache file. This API returns the result synchronously.

**System capability**: SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| uri | string | Yes | URI of the cache file to delete. |

**Error codes**

For details about the error codes, see [File Management Error Codes](../../error-codes/file-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 13600001 | IPC error. Possible causes:1.IPC failed or timed out. 2.Failed to load the service. |
| 13900002 | No such file or directory. |
| 13900010 | Try again. |
| 13900012 | Permission denied by the file system. |
| 13900020 | Parameter error. Possible causes:1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 14000002 | Invalid URI. |
| 22400005 | Inner error. Possible causes:1.Failed to access the database or execute the SQL statement. 2.System error, such as a null pointer, insufficient memory or a JS engine exception. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { fileUri } from '@kit.CoreFileKit';

let fileCache = new cloudSync.CloudFileCache();
let path = "/data/storage/el2/cloud/1.txt";
let uri = fileUri.getUriFromPath(path);

try {
  fileCache.cleanFileCache(uri);
} catch (err) {
  let error:BusinessError = err as BusinessError;
  console.error("clean file cache failed with error message: " + err.message + ", error code: " + err.code);
}

#### DownloadErrorType11+

Enumerates the device-cloud download error types.

**System capability**: SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| NO\_ERROR | 0 | No error. |
| UNKNOWN\_ERROR | 1 | Unknown error. |
| NETWORK\_UNAVAILABLE | 2 | The network is unavailable. |
| LOCAL\_STORAGE\_FULL | 3 | The local space is insufficient. |
| CONTENT\_NOT\_FOUND | 4 | The file is not found in the cloud space. |
| FREQUENT\_USER\_REQUESTS | 5 | The user requests are too frequent to respond. |

#### DownloadFileType20+

Enumerates the download file types from the Drive Kit.

**System capability**: SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| CONTENT | 0 | Content file. |
| THUMBNAIL | 1 | Thumbnail file. |
| LCD | 2 | LCD file. |

#### FailedFileInfo20+

Represents a list of files that fail to be downloaded from the Drive Kit and failure causes.

**System capability**: SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| uri | string | No | No | URI of the file that fails to be downloaded. |
| error | [DownloadErrorType](#downloaderrortype11) | No | No | Error type of the file download failure. |

#### MultiDownloadProgress20+

Represents the batch download progress of a file from the Drive Kit.

#### \[h2\]Property

**System capability**: SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| state | [State](#state11) | No | No | Execution state of the batch download. |
| taskId | number | No | No | ID of a batch download task. The value ranges from 0 to INT64\_MAX. If the progress is abnormal, the value **\-1** is returned. |
| successfulCount | number | No | No | Number of successfully downloaded files. The value ranges from 0 to 400. If the progress is abnormal, the value **\-1** is returned. |
| failedCount | number | No | No | Number of files that fail to be downloaded. The value ranges from 0 to 400. If the progress is abnormal, the value **\-1** is returned. |
| totalCount | number | No | No | Total number of files. The value ranges from 0 to 400. If the progress is abnormal, the value **\-1** is returned. |
| downloadedSize | number | No | No | Size of the downloaded file, in bytes. The value range is \[0, INT64\_MAX). If the progress is abnormal, the value **INT64\_MAX** is returned. |
| totalSize | number | No | No | Total size of the files to be downloaded, in bytes. The value range is \[0, INT64\_MAX). If the progress is abnormal, the value **INT64\_MAX** is returned. |
| errType | [DownloadErrorType](#downloaderrortype11) | No | No | Type of the error returned when the batch download fails. |

#### \[h2\]getFailedFiles20+

getFailedFiles(): Array<FailedFileInfo>

Obtains the list of files that fail to be downloaded in batches.

**System capability**: SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Array<[FailedFileInfo](#failedfileinfo20)\> | List of file URIs that fail to be downloaded and the corresponding error types. |

**Error codes**

For details about the error codes, see [File Management Error Codes](../../error-codes/file-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 22400005 | Inner error. Possible causes: 1.Failed to access the database or execute the SQL statement. 2.System error, such as a null pointer, insufficient memory or a JS engine exception. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let taskId = -1;
let failedList: Array<cloudSync.FailedFileInfo> = \[\];
let fileCache = new cloudSync.CloudFileCache();
let callback = (data: cloudSync.MultiDownloadProgress) => {
  console.info(\`Batch download progress: downloadedSize: ${data.downloadedSize}, totalSize: ${data.totalSize}\`);
  if (data.state == cloudSync.State.FAILED) {
    console.info(\`Batch download stopped, error type: ${data.errType}.\`);
    failedList = data.getFailedFiles();
  }
};

try {
  fileCache.on('batchDownload', callback);
} catch (e) {
  let error = e as BusinessError;
  console.error(\`Failed to register download callback, error code: ${error.code}, message: ${error.message}\`);
}

let uriList: Array<string> = \[\];
fileCache.startBatch(uriList, cloudSync.DownloadFileType.CONTENT).then((downloadId: number) => {
  taskId = downloadId;
  console.info("start batch download successfully");
}).catch((err: BusinessError) => {
  console.error(\`start batch download failed with error message: ${err.message}, error code: ${err.code}\`);
});

#### \[h2\]getSuccessfulFiles20+

getSuccessfulFiles(): Array<string>

Obtains the list of files that are successfully downloaded in batches.

**System capability**: SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Array<string> | List of URIs of the files that are successfully downloaded. The value is an array. |

**Error codes**

For details about the error codes, see [File Management Error Codes](../../error-codes/file-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 22400005 | Inner error. Possible causes: 1.Failed to access the database or execute the SQL statement. 2.System error, such as a null pointer, insufficient memory or a JS engine exception. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let finishedList: Array<string> = \[\];
let fileCache = new cloudSync.CloudFileCache();
let callback = (data: cloudSync.MultiDownloadProgress) => {
  console.info(\`Batch download progress: downloadedSize: ${data.downloadedSize}, totalSize: ${data.totalSize}\`);
  if (data.state == cloudSync.State.COMPLETED) {
    console.info(\`Batch download stopped, error type: ${data.errType}.\`);
    finishedList = data.getSuccessfulFiles();
  }
};

try {
  fileCache.on('batchDownload', callback);
} catch (e) {
  const error = e as BusinessError;
  console.error(\`Failed to register download callback, error code: ${error.code}, message: ${error.message}\`);
}

let uriList: Array<string> = \[\];
fileCache.startBatch(uriList, cloudSync.DownloadFileType.CONTENT).then((downloadId: number) => {
  console.info(\`start batch download successfully, taskId: ${downloadId}\`);
}).catch((err: BusinessError) => {
  console.error(\`start batch download failed with error message: ${err.message}, error code: ${err.code}\`);
});

#### cloudSync.registerChange12+

registerChange(uri: string, recursion: boolean, callback: Callback<ChangeData>): void

Subscribes to the change of a file.

**System capability**: SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| uri | string | Yes | URI of the file to download. |
| recursion | boolean | Yes | Whether to listen for the change of the URI, subfiles, and subdirectories. The value **true** means to listen for the change of the URI, subfiles, and subdirectories; the value **false** means to only listen for the change of the URI. |
| callback | Callback<[ChangeData](#changedata12)\> | Yes | Callback used to return the changed data. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [File Management Error Codes](../../error-codes/file-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | The input parameter is invalid. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 13900001 | Operation not permitted. |
| 13900002 | No such file or directory. |
| 13900012 | Permission denied. |
| 14000002 | Invalid URI. |

**Example**

import { fileUri } from '@kit.CoreFileKit';

let path = "/data/storage/el2/cloud/1.txt";
let uri = fileUri.getUriFromPath(path);
let onCallback1 = (changeData: cloudSync.ChangeData) => {
  if (changeData.type == cloudSync.NotifyType.NOTIFY\_ADDED) {
    // file had added, do something
  } else if (changeData.type== cloudSync.NotifyType.NOTIFY\_DELETED) {
    // file had removed, do something
  }
}
cloudSync.registerChange(uri, false, onCallback1);
// Unregister the listener.
cloudSync.unregisterChange(uri);

#### cloudSync.unregisterChange12+

unregisterChange(uri: string): void

Unsubscribes from the change of a file.

**System capability**: SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| uri | string | Yes | URI of the file to download. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [File Management Error Codes](../../error-codes/file-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | The input parameter is invalid. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 13900001 | Operation not permitted. |
| 13900002 | No such file or directory. |
| 13900012 | Permission denied. |
| 14000002 | Invalid URI. |

**Example**

import { fileUri } from '@kit.CoreFileKit';

let path = "/data/storage/el2/cloud/1.txt";
let uri = fileUri.getUriFromPath(path);
let onCallback1 = (changeData: cloudSync.ChangeData) => {
  if (changeData.type == cloudSync.NotifyType.NOTIFY\_ADDED) {
    // file had added, do something
  } else if (changeData.type== cloudSync.NotifyType.NOTIFY\_DELETED) {
    // file had removed, do something
  }
}
cloudSync.registerChange(uri, false, onCallback1);
// Unregister the listener.
cloudSync.unregisterChange(uri);

#### NotifyType12+

Enumerates the data change types.

**System capability**: SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| NOTIFY\_ADDED | 0 | A file is created. |
| NOTIFY\_MODIFIED | 1 | The file is modified. |
| NOTIFY\_DELETED | 2 | The file is deleted. |
| NOTIFY\_RENAMED | 3 | The file is renamed or moved. |

#### ChangeData12+

Represents the data change information.

**System capability**: SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| type | [NotifyType](#notifytype12) | No | No | Type of the data change. |
| isDirectory | Array<boolean> | No | No | Whether the URIs with data changed are of directories. The value **true** means the URIs are of directories; the value **false** means the opposite. |
| uris | Array<string> | No | No | List of URIs whose data needs to be changed. |

#### HistoryVersion20+

Represents the historical version information of the device-cloud file when the [gethistoryversionlist](#gethistoryversionlist20) method of the [FileVersion](#fileversion20) class is called.

#### \[h2\]Property

**System capability**: SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| editedTime | number | No | No | Time when the file content is modified. |
| fileSize | number | No | No | File size in bytes. |
| versionId | string | No | No | File version. |
| originalFileName | string | No | No | File name of the current version. |
| sha256 | string | No | No | Hash value of the file content of the current version. |
| autoResolved | boolean | No | No | 
Whether the current version is the one where conflicts were automatically resolved.

When the application is set to manually resolve conflicts, **false** is returned by default, which is meaningless.

When the application is set to automatically resolve conflicts, the device side automatically resolves conflicts. The value **true** means conflicts exist in the current version and have been automatically resolved by the device-cloud service; the value **false** means no conflict exists and conflicts are not automatically resolved.

 |

**NOTE**

The current device-cloud sync provides an automatic conflict resolution mechanism for cases where a file is modified simultaneously on both the local device and another device. To enable users to manually resolve the conflict, add the **cloudkit\_config.json** file to the **/entry/src/main/resources/base/profile** directory of the project and set **manualConflictResolutionEnable** to **true**. Otherwise, skip this step or set **manualConflictResolutionEnable** to **false**.

Example of configuring the **cloudkit\_config.json** file:

{
  "cloudKitConfig": {
    "cloudFileSyncConfig": {
      "manualConflictResolutionEnable": "true"
    }
  }
}

#### VersionDownloadProgress20+

Represents the download state and progress information of historical version files when the [downloadHistoryVersion](#downloadhistoryversion20) method of the [FileVersion](#fileversion20) class is called.

#### \[h2\]Property

**System capability**: SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| state | [State](#state11) | No | No | Download state of the cloud file of the selected version. |
| progress | number | No | No | Download progress. |
| errType | [DownloadErrorType](#downloaderrortype11) | No | No | Type of the error that occurs when the download fails. |

#### FileVersion20+

Represents the device-cloud file version management class. It allows you to manage historical versions of client-cloud files, obtain the list of historical versions, download historical versions to the local device, replace the current local file with a historical version file, and query and remove conflict flags for version conflicts.

#### \[h2\]construct20+

constructor()

A constructor used to create a **FileVersion** instance.

**System capability**: SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**Error codes**

For details about the error codes, see [File Management Error Codes](../../error-codes/file-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 22400005 | Inner error. Possible causes: 1.Failed to access the database or execute the SQL statement. 2.System error, such as a null pointer, insufficient memory or a JS engine exception. |

**Example**

let fileVersion = new cloudSync.FileVersion();

#### \[h2\]getHistoryVersionList20+

getHistoryVersionList(uri: string, versionNumLimit: number): Promise<Array<HistoryVersion>>

Obtains the list of historical versions. The returned versions are sorted by modification time. The earlier the modification time, the later the version. This API uses a promise to return the result.

If the number of cloud versions is less than the length limit, the list will be returned with the actual number of versions.

If the number of cloud versions is greater than or equal to the length limit, the number of the latest versions (specified by **versionNumLimit**) will be returned.

**System capability**: SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| uri | string | Yes | File URI. |
| versionNumLimit | number | Yes | Length limit of the historical version list. The value range is \[0, 100000\] (unit: number). If the input value is greater than 100,000, the list is returned according to the maximum value. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<[HistoryVersion](#historyversion20)\>> | Promise used to return the list of historical versions. |

**Error codes**

For details about the error codes, see [File Management Error Codes](../../error-codes/file-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 13600001 | IPC error. Possible causes: 1.IPC failed or timed out. 2.Failed to load the service. |
| 13900002 | No such file or directory. |
| 13900010 | Try again. |
| 13900012 | Permission denied by the file system. |
| 13900020 | Invalid argument. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 14000002 | Invalid URI. |
| 22400002 | Network unavailable. |
| 22400005 | Inner error. Possible causes: 1.Failed to access the database or execute the SQL statement. 2.System error, such as a null pointer, insufficient memory or a JS engine exception. |

**Example**

import { fileUri } from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';

let fileVersion = new cloudSync.FileVersion();

let path = "/data/storage/el2/cloud/1.txt";
let uri = fileUri.getUriFromPath(path);
let limit = 10;

fileVersion.getHistoryVersionList(uri, limit).then((versionList: Array<cloudSync.HistoryVersion>) => {
  for(let i = 0, len = versionList.length; i < len; i++) {
    console.info("get history versionId: " + versionList\[i\].versionId);
  }
}).catch((err: BusinessError) => {
  console.error("get history version failed with error message: " + err.message + ", error code: " + err.code);
});

#### \[h2\]downloadHistoryVersion20+

downloadHistoryVersion(uri: string, versionId: string, callback: Callback<[VersionDownloadProgress](#versiondownloadprogress20)\>): Promise<string>

Obtains the content of a file of a specified version based on the version number. You can download a file of a specified version from the cloud to a temporary local path. The application determines whether to replace the original file with the temporary file, or retain or delete the temporary file. This API uses a promise to return the result.

**System capability**: SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| uri | string | Yes | File URI. |
| versionId | string | Yes | Version ID of a file. The format is returned by the [gethistoryversionlist](#gethistoryversionlist20) API. |
| callback | Callback<[VersionDownloadProgress](#versiondownloadprogress20)\> | Yes | Callback for download progress. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<string> | Promise used to return the URI of the temporary file of a historical version. |

**Error codes**

For details about the error codes, see [File Management Error Codes](../../error-codes/file-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 13600001 | IPC error. Possible causes: 1.IPC failed or timed out. 2.Failed to load the service. |
| 13900002 | No such file or directory. |
| 13900010 | Try again. |
| 13900012 | Permission denied by the file system. |
| 13900020 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 14000002 | Invalid URI. |
| 22400002 | Network unavailable. |
| 22400005 | Inner error. Possible causes: 1.Failed to access the database or execute the SQL statement. 2.System error, such as a null pointer, insufficient memory or a JS engine exception. |

**Example**

import { fileUri } from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';

let fileVersion = new cloudSync.FileVersion();

let path = "/data/storage/el2/cloud/1.txt";
let uri = fileUri.getUriFromPath(path);
let versionId = '123456'; // The format returned by the getHistoryVersionList method is used as an example.

let callback = (data: cloudSync.VersionDownloadProgress) => {
  if (data.state == cloudSync.State.RUNNING) {
    console.info("download progress: " + data.progress);
  } else if (data.state == cloudSync.State.FAILED) {
    console.info("download failed errType: " + data.errType);
  } else if (data.state == cloudSync.State.COMPLETED) {
    console.info("download version file success");
  }
};

fileVersion.downloadHistoryVersion(uri, versionId, callback).then((fileUri: string) => {
  console.info("success to begin download, downloadFileUri: " + fileUri);
}).catch((err: BusinessError) => {
  console.error("download history version file failed with error message: " + err.message + ", error code: " + err.code);
});

#### \[h2\]replaceFileWithHistoryVersion20+

replaceFileWithHistoryVersion(originalUri: string, versionUri: string): Promise<void>

Replaces the local file with the file of a historical version. Before replacement, call the [downloadHistoryVersion](#downloadhistoryversion20) method to download the selected historical version and obtain its version URI. If this API is called directly without prior download or the version URI is invalid, an exception will be thrown. Once replacement is complete, the temporary file will be automatically deleted. This API uses a promise to return the result.

**System capability**: SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| originalUri | string | Yes | URI of the local file. |
| versionUri | string | Yes | URI of the historical file. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [File Management Error Codes](../../error-codes/file-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 13600001 | IPC error. Possible causes: 1.IPC failed or timed out. 2.Failed to load the service. |
| 13900002 | No such file or directory. |
| 13900005 | I/O error. |
| 13900008 | Bad file descriptor. |
| 13900010 | Try again. |
| 13900012 | Permission denied by the file system. |
| 13900020 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 14000002 | Invalid URI. |
| 22400005 | Inner error. Possible causes: 1.Failed to access the database or execute the SQL statement. 2.System error, such as a null pointer, insufficient memory or a JS engine exception. |
| 22400007 | The version file specified to replace the original file does not exist. |

**Example**

import { fileUri } from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';

let fileVersion = new cloudSync.FileVersion();

let path = "/data/storage/el2/cloud/1.txt";
let uri = fileUri.getUriFromPath(path);
let versionId = '123456'; // The format returned by the getHistoryVersionList method is used as an example.

let callback = (data: cloudSync.VersionDownloadProgress) => {
  if (data.state == cloudSync.State.RUNNING) {
    console.info("download progress: " + data.progress);
  } else if (data.state == cloudSync.State.FAILED) {
    console.info("download failed errType: " + data.errType);
  } else if (data.state == cloudSync.State.COMPLETED) {
    console.info("download version file success");
  }
};

let versionUri = "";
fileVersion.downloadHistoryVersion(uri, versionId, callback).then((fileUri: string) => {
  versionUri = fileUri;
  console.info("success to begin download, downloadFileUri: " + fileUri);
}).catch((err: BusinessError) => {
  console.error(\`download history version file failed with error message: ${err.message}, error code: ${err.code}\`);
});
fileVersion.replaceFileWithHistoryVersion(uri, versionUri).then(() => {
  console.info("replace file with history version success.");
}).catch((err: BusinessError) => {
  console.error("replace file with history version filed with error message: " + err.message + ", error code: " + err.code);
});

#### \[h2\]isFileConflict20+

isFileConflict(uri: string): Promise<boolean>

Obtains the version conflict flag of a local file. This API uses a promise to return the result. This API takes effect only when the application is configured for manual conflict resolution. Otherwise, conflicts are automatically resolved during synchronization, and the return value will be **false**.

Once the application is configured for manual conflict resolution, calling this API returns whether the current local file conflicts with the cloud file. The application then prompts the user to handle the conflict. After the conflict is resolved, you need to call the [clearFileConflict](#clearfileconflict20) method to clear the conflict flag and synchronize the file to the cloud.

**System capability**: SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| uri | string | Yes | File URI. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return the conflict flag between the local file and the cloud file. The value **true** indicates that the local file conflicts with the cloud file, and the value **false** indicates the opposite. |

**Error codes**

For details about the error codes, see [File Management Error Codes](../../error-codes/file-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 13600001 | IPC error. Possible causes: 1.IPC failed or timed out. 2.Failed to load the service. |
| 13900002 | No such file or directory. |
| 13900010 | Try again. |
| 13900012 | Permission denied by the file system. |
| 13900020 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 14000002 | Invalid URI. |
| 22400005 | Inner error. Possible causes: 1.Failed to access the database or execute the SQL statement. 2.System error, such as a null pointer, insufficient memory or a JS engine exception. |

**Example**

import { fileUri } from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';

let fileVersion = new cloudSync.FileVersion();

let path = "/data/storage/el2/cloud/1.txt";
let uri = fileUri.getUriFromPath(path);

fileVersion.isFileConflict(uri).then((isConflict: boolean) => {
  console.info("current file is conflict: " + isConflict);
}).catch((err: BusinessError) => {
  console.error("get current file conflict flag failed with error message: " + err.message + ", error code: " + err.code);
});

#### \[h2\]clearFileConflict20+

clearFileConflict(uri: string): Promise<void>

Clears the version conflict flag of the local file. If a conflict occurs, you need to call this API to clear the conflict flag after the conflict is resolved locally and trigger automatic synchronization. This API uses a promise to return the result.

**System capability**: SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| uri | string | Yes | URI of the file for which the conflict flag is to be cleared. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [File Management Error Codes](../../error-codes/file-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 13600001 | IPC error. Possible causes: 1.IPC failed or timed out. 2.Failed to load the service. |
| 13900002 | No such file or directory. |
| 13900010 | Try again. |
| 13900012 | Permission denied by the file system. |
| 13900020 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 14000002 | Invalid URI. |
| 22400005 | Inner error. Possible causes: 1.Failed to access the database or execute the SQL statement. 2.System error, such as a null pointer, insufficient memory or a JS engine exception. |

**Example**

import { fileUri } from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';

let fileVersion = new cloudSync.FileVersion();

let path = "/data/storage/el2/cloud/1.txt";
let uri = fileUri.getUriFromPath(path);

let isConflict = false;
fileVersion.isFileConflict(uri).then((isConflictRet: boolean) => {
  isConflict = isConflictRet;
  console.info("current file is conflict: " + isConflictRet);
}).catch((err: BusinessError) => {
  console.error(\`get current file conflict flag failed with error message: ${err.message}, error code: ${err.code}\`);
});
fileVersion.clearFileConflict(uri).then(() => {
  console.info("clean file conflict flag success");
}).catch((err: BusinessError) => {
  console.error("clean file conflict flag failed with error message: " + err.message + ", error code: " + err.code);
});

#### cloudSync.getCoreFileSyncState20+

getCoreFileSyncState(uri: string): FileState

Obtains the upload sync state of a cloud file. This API returns the result synchronously.

**System capability**: SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| uri | string | Yes | URI of the file whose sync state is to be obtained. |

**Return value**

| Type | Description |
| :-- | :-- |
| [FileState](#filestate20) | Upload sync state of the given cloud file. |

**Error codes**

For details about the error codes, see [File Management Error Codes](../../error-codes/file-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 13600001 | IPC error. Possible causes:1.IPC failed or timed out. 2.Failed to load the service. |
| 13900002 | No such file or directory. |
| 13900004 | Interrupted system call. |
| 13900010 | Try again. |
| 13900012 | Permission denied by the file system. |
| 13900020 | Invalid argument. Possible causes:1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 13900031 | Function not implemented. |
| 14000002 | Invalid URI. |
| 22400005 | Inner error. Possible causes:1.Failed to access the database or execute the SQL statement. 2.System error, such as a null pointer, insufficient memory or a JS engine exception. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { fileUri } from '@kit.CoreFileKit';

let path = "/data/storage/el2/cloud/1.txt";
let uri = fileUri.getUriFromPath(path);
try {
  let state = cloudSync.getCoreFileSyncState(uri);
} catch (err) {
  let error:BusinessError = err as BusinessError;
  console.error(\`getCoreFileSyncState failed with error ${error.code}, message is ${error.message}\`);
}

#### FileState20+

Enumerates the device-cloud file sync states.

**System capability**: SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| INITIAL\_AFTER\_DOWNLOAD | 0 | Initial state after the first download. |
| UPLOADING | 1 | The file is being uploaded. |
| STOPPED | 2 | The upload has been stopped. |
| TO\_BE\_UPLOADED | 3 | The file is going to be uploaded. |
| UPLOAD\_SUCCESS | 4 | The file has been successfully uploaded. |
| UPLOAD\_FAILURE | 5 | The file fails to be uploaded. |
