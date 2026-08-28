# @ohos.file.storageStatistics (Application Storage Statistics)

The **storageStatistics** module provides APIs for obtaining storage space information, including the space of built-in and plug-in memory cards, space occupied by different types of data, and space of application data.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7/v3/uYN-_Q1_Q5ismFh7w22hzw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062319Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C9B765F0351B845866AFA4C27918138EBC4DC840D92A3C15A030E0C79D818B73)

The initial APIs of this module are supported since API version 8. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { storageStatistics } from '@kit.CoreFileKit';

#### storageStatistics.getCurrentBundleStats9+

getCurrentBundleStats(): Promise<BundleStats>

Obtains the storage space (in bytes) of this application. This API uses a promise to return the result.

**System capability**: SystemCapability.FileManagement.StorageService.SpatialStatistics

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[BundleStats](#bundlestats9)\> | Promise used to return the application storage space obtained. |

**Error codes**

For details about the error codes, see [File Management Error Codes](../../error-codes/file-management-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | The input parameter is invalid. Possible causes: Mandatory parameters are left unspecified. |
| 13600001 | IPC error. |
| 13900042 | Unknown error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
storageStatistics.getCurrentBundleStats().then((BundleStats: storageStatistics.BundleStats) => {
  console.info("getCurrentBundleStats successfully:" + JSON.stringify(BundleStats));
}).catch((err: BusinessError) => {
  console.error("getCurrentBundleStats failed with error:"+ JSON.stringify(err));
});

#### storageStatistics.getCurrentBundleStats9+

getCurrentBundleStats(callback: AsyncCallback<BundleStats>): void

Obtains the storage space (in bytes) of this application. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.FileManagement.StorageService.SpatialStatistics

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[BundleStats](#bundlestats9)\> | Yes | Callback used to return the application space obtained. |

**Error codes**

For details about the error codes, see [File Management Error Codes](../../error-codes/file-management-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | The input parameter is invalid. Possible causes: Mandatory parameters are left unspecified. |
| 13600001 | IPC error. |
| 13900042 | Unknown error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
storageStatistics.getCurrentBundleStats((error: BusinessError, bundleStats: storageStatistics.BundleStats) => {
  if (error) {
    console.error("getCurrentBundleStats failed with error:" + JSON.stringify(error));
  } else {
    // Do something.
    console.info("getCurrentBundleStats successfully:" + JSON.stringify(bundleStats));
  }
});

#### storageStatistics.getTotalSize15+

getTotalSize(): Promise<number>

Obtains the total size (in bytes) of the built-in storage. This API uses a promise to return the result.

**System capability**: SystemCapability.FileManagement.StorageService.SpatialStatistics

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the total built-in storage space obtained. |

**Error codes**

For details about the error codes, see [File Management Error Codes](../../error-codes/file-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 13600001 | IPC error. |
| 13900042 | Unknown error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
storageStatistics.getTotalSize().then((number: number) => {
  console.info("getTotalSize successfully:" + JSON.stringify(number));
}).catch((err: BusinessError) => {
  console.error("getTotalSize failed with error:"+ JSON.stringify(err));
});

#### storageStatistics.getTotalSize15+

getTotalSize(callback: AsyncCallback<number>): void

Obtains the total size (in bytes) of the built-in storage. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.FileManagement.StorageService.SpatialStatistics

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<number> | Yes | Callback used to return the built-in storage space obtained. |

**Error codes**

For details about the error codes, see [File Management Error Codes](../../error-codes/file-management-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | The input parameter is invalid. Possible causes: Mandatory parameters are left unspecified. |
| 13600001 | IPC error. |
| 13900042 | Unknown error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
storageStatistics.getTotalSize((error: BusinessError, number: number) => {
  if (error) {
    console.error("getTotalSize failed with error:" + JSON.stringify(error));
  } else {
    // Do something.
    console.info("getTotalSize successfully:" + number);
  }
});

#### storageStatistics.getTotalSizeSync15+

getTotalSizeSync(): number

Obtains the total space of the built-in storage, in bytes. This API returns the result synchronously.

**System capability**: SystemCapability.FileManagement.StorageService.SpatialStatistics

**Return value**

| Type | Description |
| :-- | :-- |
| number | Built-in storage space obtained. |

**Error codes**

For details about the error codes, see [File Management Error Codes](../../error-codes/file-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 13600001 | IPC error. |
| 13900042 | Unknown error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
try {
  let number = storageStatistics.getTotalSizeSync();
  console.info("getTotalSizeSync successfully:" + JSON.stringify(number));
} catch (err) {
  let error: BusinessError = err as BusinessError;
  console.error("getTotalSizeSync failed with error:" + JSON.stringify(error));
}

#### storageStatistics.getFreeSize15+

getFreeSize(): Promise<number>

Obtains the available space (in bytes) of the built-in storage. This API uses a promise to return the result.

**System capability**: SystemCapability.FileManagement.StorageService.SpatialStatistics

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the available space of the built-in storage obtained. |

**Error codes**

For details about the error codes, see [File Management Error Codes](../../error-codes/file-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 13600001 | IPC error. |
| 13900042 | Unknown error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
storageStatistics.getFreeSize().then((number: number) => {
  console.info("getFreeSize successfully:" + JSON.stringify(number));
}).catch((err: BusinessError) => {
  console.error("getFreeSize failed with error:" + JSON.stringify(err));
});

#### storageStatistics.getFreeSize15+

getFreeSize(callback: AsyncCallback<number>): void

Obtains the available space (in bytes) of the built-in storage. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.FileManagement.StorageService.SpatialStatistics

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<number> | Yes | Callback used to return the available space of the built-in storage obtained. |

**Error codes**

For details about the error codes, see [File Management Error Codes](../../error-codes/file-management-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | The input parameter is invalid. Possible causes: Mandatory parameters are left unspecified. |
| 13600001 | IPC error. |
| 13900042 | Unknown error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
storageStatistics.getFreeSize((error: BusinessError, number: number) => {
  if (error) {
    console.error("getFreeSize failed with error:" + JSON.stringify(error));
  } else {
    // Do something.
    console.info("getFreeSize successfully:" + number);
  }
});

#### storageStatistics.getFreeSizeSync15+

getFreeSizeSync(): number

Obtains the available space of the built-in storage, in bytes. This API returns the result synchronously.

**System capability**: SystemCapability.FileManagement.StorageService.SpatialStatistics

**Return value**

| Type | Description |
| :-- | :-- |
| number | Available space of the built-in storage obtained. |

**Error codes**

For details about the error codes, see [File Management Error Codes](../../error-codes/file-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 13600001 | IPC error. |
| 13900042 | Unknown error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
try {
  let number = storageStatistics.getFreeSizeSync();
  console.info("getFreeSizeSync successfully:" + JSON.stringify(number));
} catch (err) {
  let error: BusinessError = err as BusinessError;
  console.error("getFreeSizeSync failed with error:" + JSON.stringify(error));
}

#### BundleStats9+

**System capability**: SystemCapability.FileManagement.StorageService.SpatialStatistics

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| appSize | number | No | No | Size of the application installation files, in bytes. |
| cacheSize | number | No | No | Size of the application cache files, in bytes. |
| dataSize | number | No | No | Size of application files (excluding application installation files), in bytes. |
