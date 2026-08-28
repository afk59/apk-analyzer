# @ohos.file.statvfs (File System Space Statistics)

This module provides APIs for obtaining file system information, including the total size and free size of a file system, in bytes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/LCD8hsThSwGNgfiLHLr49w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062319Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=516CBF56FCF98BCC6BD592F83A1FBEC1C6E37421A56245C77EF3FD07D83D6D1C)

The initial APIs of this module are supported since API version 9. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { statfs } from '@kit.CoreFileKit';

#### statfs.getFreeSize

getFreeSize(path:string): Promise<number>

Obtains the free size of the specified file system, in bytes. This API uses a promise to return the result.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | File path of the file system. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the free size obtained, in bytes. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

| ID | Error Message |
| :-- | :-- |
| 13900002 | No such file or directory. |
| 13900004 | Interrupted system call. |
| 13900005 | I/O error. |
| 13900008 | Bad file descriptor. |
| 13900011 | Out of memory. |
| 13900012 | Permission denied. |
| 13900013 | Bad address. |
| 13900018 | Not a directory. |
| 13900030 | File name too long. |
| 13900031 | Function not implemented. |
| 13900033 | Too many symbolic links encountered. |
| 13900038 | Value too large for defined data type. |
| 13900042 | Unknown error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let path = context.filesDir;
statfs.getFreeSize(path).then((number: number) => {
  console.info("getFreeSize succeed, Size: " + number);
}).catch((err: BusinessError) => {
  console.error("getFreeSize failed with error message: " + err.message + ", error code: " + err.code);
});

#### statfs.getFreeSize

getFreeSize(path:string, callback:AsyncCallback<number>): void

Obtains the free size of the specified file system, in bytes. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | File path of the file system. |
| callback | AsyncCallback<number> | Yes | Callback used to return the free size obtained, in bytes. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

| ID | Error Message |
| :-- | :-- |
| 13900002 | No such file or directory. |
| 13900004 | Interrupted system call. |
| 13900005 | I/O error. |
| 13900008 | Bad file descriptor. |
| 13900011 | Out of memory. |
| 13900012 | Permission denied. |
| 13900013 | Bad address. |
| 13900018 | Not a directory. |
| 13900030 | File name too long. |
| 13900031 | Function not implemented. |
| 13900033 | Too many symbolic links encountered. |
| 13900038 | Value too large for defined data type. |
| 13900042 | Unknown error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let path = context.filesDir;
statfs.getFreeSize(path, (err: BusinessError, number: number) => {
  if (err) {
    console.error("getFreeSize failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("getFreeSize succeed, Size: " + number);
  }
});

#### statfs.getFreeSizeSync10+

getFreeSizeSync(path:string): number

Obtains the free size of the specified file system, in bytes. This API returns the result synchronously.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | File path of the file system. |

**Return value**

| Type | Description |
| :-- | :-- |
| number | Free size obtained, in bytes. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

| ID | Error Message |
| :-- | :-- |
| 13900002 | No such file or directory. |
| 13900004 | Interrupted system call. |
| 13900005 | I/O error. |
| 13900008 | Bad file descriptor. |
| 13900011 | Out of memory. |
| 13900012 | Permission denied. |
| 13900013 | Bad address. |
| 13900018 | Not a directory. |
| 13900030 | File name too long. |
| 13900031 | Function not implemented. |
| 13900033 | Too many symbolic links encountered. |
| 13900038 | Value too large for defined data type. |
| 13900042 | Unknown error. |

**Example**

import { common } from '@kit.AbilityKit';

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let path = context.filesDir;
let number = statfs.getFreeSizeSync(path);
console.info("getFreeSizeSync succeed, Size: " + number);

#### statfs.getTotalSize

getTotalSize(path: string): Promise<number>

Obtains the total size of the specified file system, in bytes. This API uses a promise to return the result.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | File path of the file system. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the total size obtained, in bytes. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

| ID | Error Message |
| :-- | :-- |
| 13900002 | No such file or directory. |
| 13900004 | Interrupted system call. |
| 13900005 | I/O error. |
| 13900008 | Bad file descriptor. |
| 13900011 | Out of memory. |
| 13900012 | Permission denied. |
| 13900013 | Bad address. |
| 13900018 | Not a directory. |
| 13900030 | File name too long. |
| 13900031 | Function not implemented. |
| 13900033 | Too many symbolic links encountered. |
| 13900038 | Value too large for defined data type. |
| 13900042 | Unknown error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let path = context.filesDir;
statfs.getTotalSize(path).then((number: number) => {
  console.info("getTotalSize succeed, Size: " + number);
}).catch((err: BusinessError) => {
  console.error("getTotalSize failed with error message: " + err.message + ", error code: " + err.code);
});

#### statfs.getTotalSize

getTotalSize(path: string, callback: AsyncCallback<number>): void

Obtains the total size of the specified file system, in bytes. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | File path of the file system. |
| callback | AsyncCallback<number> | Yes | Callback used to return the total size obtained, in bytes. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

| ID | Error Message |
| :-- | :-- |
| 13900002 | No such file or directory. |
| 13900004 | Interrupted system call. |
| 13900005 | I/O error. |
| 13900008 | Bad file descriptor. |
| 13900011 | Out of memory. |
| 13900012 | Permission denied. |
| 13900013 | Bad address. |
| 13900018 | Not a directory. |
| 13900030 | File name too long. |
| 13900031 | Function not implemented. |
| 13900033 | Too many symbolic links encountered. |
| 13900038 | Value too large for defined data type. |
| 13900042 | Unknown error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let path = context.filesDir;
statfs.getTotalSize(path, (err: BusinessError, number: number) => {
  if (err) {
    console.error("getTotalSize failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("getTotalSize succeed, Size: " + number);
  }
});

#### statfs.getTotalSizeSync10+

getTotalSizeSync(path: string): number

Obtains the total size of the specified file system, in bytes. This API returns the result synchronously.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | File path of the file system. |

**Return value**

| Type | Description |
| :-- | :-- |
| number | Total size obtained, in bytes. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

| ID | Error Message |
| :-- | :-- |
| 13900002 | No such file or directory. |
| 13900004 | Interrupted system call. |
| 13900005 | I/O error. |
| 13900008 | Bad file descriptor. |
| 13900011 | Out of memory. |
| 13900012 | Permission denied. |
| 13900013 | Bad address. |
| 13900018 | Not a directory. |
| 13900030 | File name too long. |
| 13900031 | Function not implemented. |
| 13900033 | Too many symbolic links encountered. |
| 13900038 | Value too large for defined data type. |
| 13900042 | Unknown error. |

**Example**

import { common } from '@kit.AbilityKit';

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let path = context.filesDir;
let number = statfs.getTotalSizeSync(path);
console.info("getTotalSizeSync succeed, Size: " + number);
