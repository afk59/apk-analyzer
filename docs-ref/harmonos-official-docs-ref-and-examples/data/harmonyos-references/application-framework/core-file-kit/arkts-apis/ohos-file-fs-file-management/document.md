# @ohos.file.fs (File Management)

The **fs** module provides APIs for file operations, including accessing and managing files and directories, obtaining file information statistics, and reading and writing data using a stream.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0d/v3/PUsM3qrpThezcquY8qXmXA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062319Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B772331EE8B80B8C35715382823B93788CC1474B97CB8E87EC3710069ED8FC0B)

The initial APIs of this module are supported since API version 9. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { fileIo as fs } from '@kit.CoreFileKit';

#### How to Use

Before using the APIs provided by this module to perform operations on a file or directory, obtain the application sandbox path of the file or directory as follows:

import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    let context = this.context;
    let pathDir = context.filesDir;
  }
}

For details about how to obtain the sandbox path and how to use the related APIs, see [Obtaining Application File Paths](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/application-context-stage#obtaining-application-file-paths).

A uniform resource identifier (URI) is a string pointing to a resource. For APIs that support only the sandbox path as the input parameter, you can construct a **fileUri** object and obtain the sandbox path property to convert the URI to the sandbox path, and then use the APIs. For details about the URI definition and how to convert a URI to a path, see [File URI](../ohos-file-fileuri-file-uri/document.md).

#### fs.stat

stat(file: string | number): Promise<Stat>

Obtains detailed attribute information of a file or directory. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| file | string | number | Yes | 
Application sandbox path, URI, or FD of the file or directory.

**Note**: URIs can be passed since API version 22.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[Stat](#stat)\> | Promise used to return the file or directory information. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
fs.stat(filePath).then((stat: fs.Stat) => {
  console.info("get file info succeed, the size of file is " + stat.size);
}).catch((err: BusinessError) => {
  console.error("get file info failed with error message: " + err.message + ", error code: " + err.code);
});

#### fs.stat

stat(file: string | number, callback: AsyncCallback<Stat>): void

Obtains detailed attribute information of a file or directory. This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| file | string | number | Yes | 
Application sandbox path, URI, or FD of the file or directory.

**Note**: URIs can be passed since API version 22.

 |
| callback | AsyncCallback<[Stat](#stat)\> | Yes | Callback used to return the file or directory information obtained. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
fs.stat(pathDir, (err: BusinessError, stat: fs.Stat) => {
  if (err) {
    console.error("get file info failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("get file info succeed, the size of file is " + stat.size);
  }
});

#### fs.statSync

statSync(file: string | number): Stat

Obtains detailed attribute information of a file or directory. This API returns the result synchronously.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| file | string | number | Yes | 
Application sandbox path, URI, or FD of the file or directory.

**Note**: URIs can be passed since API version 22.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [Stat](#stat) | Detailed information of a file or directory. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

let stat = fs.statSync(pathDir);
console.info("get file info succeed, the size of file is " + stat.size);

#### fs.access

access(path: string, mode?: AccessModeType): Promise<boolean>

Checks whether the file or directory exists or has the operation permission. This API uses a promise to return the result.

If the read, write, or read and write permission verification fails, the error code 13900012 (Permission denied) will be thrown.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | Application sandbox path of the file or directory. |
| mode12+ | [AccessModeType](#accessmodetype12) | No | Permission on the file or directory to check. If this parameter is left blank, the system checks whether the file exists. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return a Boolean value. The value **true** means the file exists; the value **false** means the opposite. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
fs.access(filePath).then((res: boolean) => {
  if (res) {
    console.info("file exists");
  } else {
    console.info("file not exists");
  }
}).catch((err: BusinessError) => {
  console.error("access failed with error message: " + err.message + ", error code: " + err.code);
});

#### fs.access12+

access(path: string, mode: AccessModeType, flag: AccessFlagType): Promise<boolean>

Checks whether the file or directory is stored locally or has the operation permission. This API uses a promise to return the result.

If the read, write, or read and write permission verification fails, the error code 13900012 (Permission denied) will be thrown.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | Application sandbox path of the file or directory. |
| mode | [AccessModeType](#accessmodetype12) | Yes | Permission on the file or directory to check. |
| flag | [AccessFlagType](#accessflagtype12) | Yes | Position of the file or directory to check. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return a Boolean value. The value **true** means the file or directory is a local one and has the related permission. The value **false** means the file or directory does not exist or is on the cloud or a distributed device. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
fs.access(filePath, fs.AccessModeType.EXIST, fs.AccessFlagType.LOCAL).then((res: boolean) => {
  if (res) {
    console.info("file exists");
  } else {
    console.info("file not exists");
  }
}).catch((err: BusinessError) => {
  console.error("access failed with error message: " + err.message + ", error code: " + err.code);
});

#### fs.access

access(path: string, callback: AsyncCallback<boolean>): void

Checks whether a file or directory exists. This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | Application sandbox path of the file or directory. |
| callback | AsyncCallback<boolean> | Yes | Callback used to return the result. The value **true** means the file exists; the value **false** means the opposite. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
fs.access(filePath, (err: BusinessError, res: boolean) => {
  if (err) {
    console.error("access failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    if (res) {
      console.info("file exists");
    } else {
      console.info("file not exists");
    }
  }
});

#### fs.accessSync

accessSync(path: string, mode?: AccessModeType): boolean

Checks whether a file or directory exists or has the operation permission. This API returns the result synchronously.

If the read, write, or read and write permission verification fails, the error code 13900012 (Permission denied) will be thrown.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | Application sandbox path of the file or directory. |
| mode12+ | [AccessModeType](#accessmodetype12) | No | Permission on the file or directory to check. If this parameter is left blank, the system checks whether the file or directory exists. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | The value **true** means the file exists; the value **false** means the opposite. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
try {
  let res = fs.accessSync(filePath);
  if (res) {
    console.info("file exists");
  } else {
    console.info("file not exists");
  }
} catch(error) {
  let err: BusinessError = error as BusinessError;
  console.error("accessSync failed with error message: " + err.message + ", error code: " + err.code);
}

#### fs.accessSync12+

accessSync(path: string, mode: AccessModeType, flag: AccessFlagType): boolean

Checks whether a file or directory is stored locally or has the operation permission. This API returns the result synchronously.

If the read, write, or read and write permission verification fails, the error code 13900012 (Permission denied) will be thrown.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | Application sandbox path of the file to check. |
| mode | [AccessModeType](#accessmodetype12) | Yes | Permission on the file or directory to check. |
| flag | [AccessFlagType](#accessflagtype12) | Yes | Position of the file or directory to check. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | The value **true** means the file is a local file and has the related permission. The value **false** means the file does not exist or is on the cloud or a distributed device. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
try {
  let res = fs.accessSync(filePath, fs.AccessModeType.EXIST, fs.AccessFlagType.LOCAL);
  if (res) {
    console.info("file exists");
  } else {
    console.info("file not exists");
  }
} catch(error) {
  let err: BusinessError = error as BusinessError;
  console.error("accessSync failed with error message: " + err.message + ", error code: " + err.code);
}

#### fs.close

close(file: number | File): Promise<void>

Closes a file or directory. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| file | number | [File](#file) | Yes | **File** object or FD of the file to close. Once closed, the **File** object or FD cannot be used for read or write operations. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
let file = fs.openSync(filePath);
fs.close(file).then(() => {
  console.info("close file succeed");
}).catch((err: BusinessError) => {
  console.error("close file failed with error message: " + err.message + ", error code: " + err.code);
});

#### fs.close

close(file: number | File, callback: AsyncCallback<void>): void

Closes a file or directory. This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| file | number | [File](#file) | Yes | **File** object or FD of the file to close. Once closed, the **File** object or FD cannot be used for read or write operations. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
let file = fs.openSync(filePath);
fs.close(file, (err: BusinessError) => {
  if (err) {
    console.error("close file failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("close file succeed");
  }
});

#### fs.closeSync

closeSync(file: number | File): void

Closes a file or directory. This API returns the result synchronously.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| file | number | [File](#file) | Yes | **File** object or FD of the file to close. Once closed, the **File** object or FD cannot be used for read or write operations. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

let filePath = pathDir + "/test.txt";
let file = fs.openSync(filePath);
fs.closeSync(file);

#### fs.copy11+

copy(srcUri: string, destUri: string, options?: CopyOptions): Promise<void>

Copies a file or directory. This API uses a promise to return the result.

File copy across devices is supported. This API forcibly overwrites the file or directory. The input parameter can be the URI of the file or directory.

A maximum of 10 cross-device copy tasks are allowed at the same time, and the number of files to be copied at a time cannot exceed 500.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| srcUri | string | Yes | URI of the file or directory to copy. |
| destUri | string | Yes | URI of the destination file or directory. |
| options | [CopyOptions](#copyoptions11) | No | Callback invoked to provide the copy progress. If this parameter is not set, the callback will not be invoked. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

**Example**

import { fileIo as fs } from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileUri } from '@kit.CoreFileKit';

let srcDirPathLocal: string = pathDir + "/src";
let dstDirPathLocal: string = pathDir + "/dest";

let srcDirUriLocal: string = fileUri.getUriFromPath(srcDirPathLocal);
let dstDirUriLocal: string = fileUri.getUriFromPath(dstDirPathLocal);

let progressListener: fs.ProgressListener = (progress: fs.Progress) => {
  console.info(\`progressSize: ${progress.processedSize}, totalSize: ${progress.totalSize}\`);
};
let copyOption: fs.CopyOptions = {
  "progressListener" : progressListener
}
try {
  fs.copy(srcDirUriLocal, dstDirUriLocal, copyOption).then(()=>{
    console.info("Succeeded in copying.");
  }).catch((err: BusinessError)=>{
    console.error(\`Failed to copy. Code: ${err.code}, message: ${err.message}\`);
  })
} catch(err) {
  console.error(\`Failed to copy.Code: ${err.code}, message: ${err.message}\`);
}

#### fs.copy11+

copy(srcUri: string, destUri: string, callback: AsyncCallback<void>): void

Copies a file or directory. This API uses an asynchronous callback to return the result.

File copy across devices is supported. This API forcibly overwrites the file or directory. The input parameter can be the URI of the file or directory.

A maximum of 10 cross-device copy tasks are allowed at the same time, and the number of files to be copied at a time cannot exceed 500.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| srcUri | string | Yes | URI of the file or directory to copy. |
| destUri | string | Yes | URI of the destination file or directory. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { fileUri } from '@kit.CoreFileKit';

let srcDirPathLocal: string = pathDir + "/src";
let dstDirPathLocal: string = pathDir + "/dest";

let srcDirUriLocal: string = fileUri.getUriFromPath(srcDirPathLocal);
let dstDirUriLocal: string = fileUri.getUriFromPath(dstDirPathLocal);

try {
  fs.copy(srcDirUriLocal, dstDirUriLocal, (err: BusinessError) => {
    if (err) {
      console.error(\`Failed to copy. Code: ${err.code}, message: ${err.message}\`);
      return;
    }
    console.info("Succeeded in copying.");
  })
} catch(err) {
  console.error(\`Failed to copy. Code: ${err.code}, message: ${err.message}\`);
}

#### fs.copy11+

copy(srcUri: string, destUri: string, options: CopyOptions, callback: AsyncCallback<void>): void

Copies a file or directory. This API uses an asynchronous callback to return the result.

File copy across devices is supported. This API forcibly overwrites the file or directory. The input parameter can be the URI of the file or directory.

A maximum of 10 cross-device copy tasks are allowed at the same time, and the number of files to be copied at a time cannot exceed 500.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| srcUri | string | Yes | URI of the file or directory to copy. |
| destUri | string | Yes | URI of the destination file or directory. |
| options | [CopyOptions](#copyoptions11) | Yes | Callback used to return the copy progress. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

**Example**

import { fileIo as fs } from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileUri } from '@kit.CoreFileKit';

let srcDirPathLocal: string = pathDir + "/src";
let dstDirPathLocal: string = pathDir + "/dest";

let srcDirUriLocal: string = fileUri.getUriFromPath(srcDirPathLocal);
let dstDirUriLocal: string = fileUri.getUriFromPath(dstDirPathLocal);

try {
  let progressListener: fs.ProgressListener = (progress: fs.Progress) => {
    console.info(\`progressSize: ${progress.processedSize}, totalSize: ${progress.totalSize}\`);
  };
  let copyOption: fs.CopyOptions = {
    "progressListener" : progressListener
  }
  fs.copy(srcDirUriLocal, dstDirUriLocal, copyOption, (err: BusinessError) => {
    if (err) {
      console.error(\`Failed to copy. Code: ${err.code}, message: ${err.message}\`);
      return;
    }
    console.info("Succeeded in copying.");
  })
} catch(err) {
  console.error(\`Failed to copy. Code: ${err.code}, message: ${err.message}\`);
}

#### fs.copyFile

copyFile(src: string | number, dest: string | number, mode?: number): Promise<void>

Copies a file. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| src | string | number | Yes | Path or FD of the file to copy. |
| dest | string | number | Yes | Destination path of the file or FD of the file created. |
| mode | number | No | 
Whether to overwrite the file with the same name in the destination directory. The default value is **0**, which is the only value supported.

**0**: overwrite the file with the same name and truncate the part that is not overwritten.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
let srcPath = pathDir + "/srcDir/test.txt";
let dstPath = pathDir + "/dstDir/test.txt";
fs.copyFile(srcPath, dstPath, 0).then(() => {
  console.info("copy file succeed");
}).catch((err: BusinessError) => {
  console.error("copy file failed with error message: " + err.message + ", error code: " + err.code);
});

#### fs.copyFile

copyFile(src: string | number, dest: string | number, mode: number, callback: AsyncCallback<void>): void

Copies a file with the specified mode. This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| src | string | number | Yes | Path or FD of the file to copy. |
| dest | string | number | Yes | Destination path of the file or FD of the file created. |
| mode | number | Yes | 
Whether to overwrite the file with the same name in the destination directory. The default value is **0**, which is the only value supported.

**0**: overwrite the file with the same name and truncate the part that is not overwritten.

 |
| callback | AsyncCallback<void> | Yes | Callback invoked immediately after the file is copied. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
let srcPath = pathDir + "/srcDir/test.txt";
let dstPath = pathDir + "/dstDir/test.txt";
fs.copyFile(srcPath, dstPath, 0, (err: BusinessError) => {
  if (err) {
    console.error("copy file failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("copy file succeed");
  }
});

#### fs.copyFile

copyFile(src: string | number, dest: string | number, callback: AsyncCallback<void>): void

Copies a file. This API overwrites the file with the same name in the destination directory and truncates the part that is not overwritten. This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| src | string | number | Yes | Path or FD of the file to copy. |
| dest | string | number | Yes | Destination path of the file or FD of the file created. |
| callback | AsyncCallback<void> | Yes | Callback invoked immediately after the file is copied. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
let srcPath = pathDir + "/srcDir/test.txt";
let dstPath = pathDir + "/dstDir/test.txt";
fs.copyFile(srcPath, dstPath, (err: BusinessError) => {
  if (err) {
    console.error("copy file failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("copy file succeed");
  }
});

#### fs.copyFileSync

copyFileSync(src: string | number, dest: string | number, mode?: number): void

Copies a file. This API returns the result synchronously.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| src | string | number | Yes | Path or FD of the file to copy. |
| dest | string | number | Yes | Destination path of the file or FD of the file created. |
| mode | number | No | 
Whether to overwrite the file with the same name in the destination directory. The default value is **0**, which is the only value supported.

**0**: overwrite the file with the same name and truncate the part that is not overwritten.

 |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

let srcPath = pathDir + "/srcDir/test.txt";
let dstPath = pathDir + "/dstDir/test.txt";
fs.copyFileSync(srcPath, dstPath);

#### fs.copyDir10+

copyDir(src: string, dest: string, mode?: number): Promise<void>

Copies the source directory to the destination path. This API uses a promise to return the result.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| src | string | Yes | Application sandbox path of the source directory. |
| dest | string | Yes | Application sandbox path of the destination directory. |
| mode | number | No | 
Copy mode. The default value is **0**.

\- **0**: Throw an exception if a file conflict occurs.

An exception will be thrown if the destination directory contains a directory with the same name as the source directory, and a file with the same name exists in the conflict directory. All the non-conflicting files in the source directory will be moved to the destination directory, and the non-conflicting files in the destination directory will be retained. The data attribute in the error returned provides information about the conflicting files in the Array<[ConflictFiles](#conflictfiles10)\> format.

\- **1**: Forcibly overwrite the files with the same name in the destination directory.

When the destination directory contains a directory with the same name as the source directory, the files with the same names in the destination directory are overwritten forcibly; the files without conflicts in the destination directory are retained.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
// Copy srcPath to destPath.
let srcPath = pathDir + "/srcDir/";
let destPath = pathDir + "/destDir/";
fs.copyDir(srcPath, destPath, 0).then(() => {
  console.info("copy directory succeed");
}).catch((err: BusinessError) => {
  console.error("copy directory failed with error message: " + err.message + ", error code: " + err.code);
});

#### fs.copyDir10+

copyDir(src: string, dest: string, mode: number, callback: AsyncCallback<void, Array<ConflictFiles>>): void

Copies the source directory to the destination path. You can set the copy mode. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| src | string | Yes | Application sandbox path of the source directory. |
| dest | string | Yes | Application sandbox path of the destination directory. |
| mode | number | Yes | 
Copy mode. The default value is **0**.

\- **0**: Throw an exception if a file conflict occurs.

An exception will be thrown if the destination directory contains a directory with the same name as the source directory, and a file with the same name exists in the conflict directory. All the non-conflicting files in the source directory will be moved to the destination directory, and the non-conflicting files in the destination directory will be retained. The data attribute in the error returned provides information about the conflicting files in the Array<[ConflictFiles](#conflictfiles10)\> format.

\- **1**: Forcibly overwrite the files with the same name in the destination directory.

When the destination directory contains a directory with the same name as the source directory, the files with the same names in the destination directory are overwritten forcibly; the files without conflicts in the destination directory are retained.

 |
| callback | AsyncCallback<void, Array<[ConflictFiles](#conflictfiles10)\>> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo as fs, ConflictFiles } from '@kit.CoreFileKit';
// Copy srcPath to destPath.
let srcPath = pathDir + "/srcDir/";
let destPath = pathDir + "/destDir/";
fs.copyDir(srcPath, destPath, 0, (err: BusinessError<Array<ConflictFiles>>) => {
  if (err && err.code == 13900015 && err.data?.length !== undefined) {
    for (let i = 0; i < err.data.length; i++) {
      console.error("copy directory failed with conflicting files: " + err.data\[i\].srcFile + " " + err.data\[i\].destFile);
    }
  } else if (err) {
    console.error("copy directory failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("copy directory succeed");
  }
});

#### fs.copyDir10+

copyDir(src: string, dest: string, callback: AsyncCallback<void, Array<ConflictFiles>>): void

Copies the source directory to the destination path. This API uses an asynchronous callback to return the result.

An exception will be thrown if the destination directory contains a directory with the same name as the source directory and there are files with the same name in the conflicting directory. All the non-conflicting files in the source directory will be moved to the destination directory, and the non-conflicting files in the destination directory will be retained. The data attribute in the error returned provides information about the conflicting files in the Array<[ConflictFiles](#conflictfiles10)\> format.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| src | string | Yes | Application sandbox path of the source directory. |
| dest | string | Yes | Application sandbox path of the destination directory. |
| callback | AsyncCallback<void, Array<[ConflictFiles](#conflictfiles10)\>> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo as fs, ConflictFiles } from '@kit.CoreFileKit';
// Copy srcPath to destPath.
let srcPath = pathDir + "/srcDir/";
let destPath = pathDir + "/destDir/";
fs.copyDir(srcPath, destPath, (err: BusinessError<Array<ConflictFiles>>) => {
  if (err && err.code == 13900015 && err.data?.length !== undefined) {
    for (let i = 0; i < err.data.length; i++) {
      console.error("copy directory failed with conflicting files: " + err.data\[i\].srcFile + " " + err.data\[i\].destFile);
    }
  } else if (err) {
    console.error("copy directory failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("copy directory succeed");
  }
});

#### fs.copyDirSync10+

copyDirSync(src: string, dest: string, mode?: number): void

Copies the source directory to the destination path. This API returns the result synchronously.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| src | string | Yes | Application sandbox path of the source directory. |
| dest | string | Yes | Application sandbox path of the destination directory. |
| mode | number | No | 
Copy mode. The default value is **0**.

\- **0**: Throw an exception if a file conflict occurs.

An exception will be thrown if the destination directory contains a directory with the same name as the source directory, and a file with the same name exists in the conflict directory. All the non-conflicting files in the source directory will be moved to the destination directory, and the non-conflicting files in the destination directory will be retained. The data attribute in the error returned provides information about the conflicting files in the Array<[ConflictFiles](#conflictfiles10)\> format.

\- **1**: Forcibly overwrite the files with the same name in the destination directory.

When the destination directory contains a directory with the same name as the source directory, the files with the same names in the destination directory are overwritten forcibly; the files without conflicts in the destination directory are retained.

 |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
// Copy srcPath to destPath.
let srcPath = pathDir + "/srcDir/";
let destPath = pathDir + "/destDir/";
try {
  fs.copyDirSync(srcPath, destPath, 0);
  console.info("copy directory succeed");
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error("copy directory failed with error message: " + err.message + ", error code: " + err.code);
}

#### fs.dup10+

dup(fd: number): File

Duplicates the file descriptor and returns the corresponding **File** object.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| fd | number | Yes | File descriptor. |

**Return value**

| Type | Description |
| :-- | :-- |
| [File](#file) | File object opened. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

let filePath = pathDir + "/test.txt";
let file1 = fs.openSync(filePath, fs.OpenMode.READ\_WRITE);
let fd: number = file1.fd;
let file2 = fs.dup(fd);
console.info("The name of the file2 is " + file2.name);
fs.closeSync(file1);
fs.closeSync(file2);

#### fs.connectDfs12+

connectDfs(networkId: string, listeners: DfsListeners): Promise<void>

Triggers connection. If the peer device is abnormal, [onStatus](#onstatus12) in **DfsListeners** will be called to notify the application.

**Required permissions**: ohos.permission.DISTRIBUTED\_DATASYNC

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| networkId | string | Yes | Network ID of the device. The device network ID can be obtained from [DeviceBasicInfo](../../../../system/network/distributed-service-kit/arkts-apis/ohos-distributeddevicemanager-device-management/document.md#devicebasicinfo) using the related [distributedDeviceManager](../../../../system/network/distributed-service-kit/arkts-apis/ohos-distributeddevicemanager-device-management/document.md) API. |
| listeners | [DfsListeners](#fsdfslisteners12) | Yes | Listeners for distributed file system status. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo as fs } from '@kit.CoreFileKit';
import { distributedDeviceManager } from '@kit.DistributedServiceKit';
let dmInstance = distributedDeviceManager.createDeviceManager("com.example.filesync");
let deviceInfoList: Array<distributedDeviceManager.DeviceBasicInfo> = dmInstance.getAvailableDeviceListSync();
if (deviceInfoList && deviceInfoList.length > 0) {
  console.info(\`Success to get available device list\`);
  let networkId = deviceInfoList\[0\].networkId;
  let listeners: fs.DfsListeners = {
    onStatus(networkId, status) {
      console.info('onStatus');
    }
  };
  fs.connectDfs(networkId, listeners).then(() => {
    console.info("Success to connectDfs");
  }).catch((err: BusinessError) => {
    console.error(\`Failed to connectDfs. Code: ${err.code}, message: ${err.message}\`);
  });
}

#### fs.disconnectDfs12+

disconnectDfs(networkId: string): Promise<void>

Triggers disconnection.

**Required permissions**: ohos.permission.DISTRIBUTED\_DATASYNC

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| networkId | string | Yes | Network ID of the device. The device network ID can be obtained from [DeviceBasicInfo](../../../../system/network/distributed-service-kit/arkts-apis/ohos-distributeddevicemanager-device-management/document.md#devicebasicinfo) using the related [distributedDeviceManager](../../../../system/network/distributed-service-kit/arkts-apis/ohos-distributeddevicemanager-device-management/document.md) API. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Space Statistics Error Codes](../../error-codes/file-management-error-codes/document.md#space-statistics-error-codes) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo as fs } from '@kit.CoreFileKit';
import { distributedDeviceManager } from '@kit.DistributedServiceKit';
let dmInstance = distributedDeviceManager.createDeviceManager("com.example.filesync");
let deviceInfoList: Array<distributedDeviceManager.DeviceBasicInfo> = dmInstance.getAvailableDeviceListSync();
if (deviceInfoList && deviceInfoList.length > 0) {
  console.info(\`Success to get available device list\`);
  let networkId = deviceInfoList\[0\].networkId;
  fs.disconnectDfs(networkId).then(() => {
    console.info("Success to disconnect dfs");
  }).catch((err: BusinessError) => {
    console.error(\`Failed to disconnect dfs. Code: ${err.code}, message: ${err.message}\`);
  })
}

#### fs.setxattr12+

setxattr(path: string, key: string, value: string): Promise<void>

Sets an extended attribute of a file or directory. This API uses a promise to return the result.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | Application sandbox path of the file or directory. |
| key | string | Yes | Key of the extended attribute to obtain. The value is a string of less than 256 bytes and can contain only the **user.** prefix. |
| value | string | Yes | Value of the extended attribute to set. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/test.txt";
let attrKey = "user.comment";
let attrValue = "Test file.";

fs.setxattr(filePath, attrKey, attrValue).then(() => {
  console.info("Set extended attribute successfully.");
}).catch((err: BusinessError) => {
  console.error("Failed to set extended attribute with error message: " + err.message + ", error code: " + err.code);
});

#### fs.setxattrSync12+

setxattrSync(path: string, key: string, value: string): void

Sets an extended attribute of a file or directory.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | Application sandbox path of the file or directory. |
| key | string | Yes | Key of the extended attribute to obtain. The value is a string of less than 256 bytes and can contain only the **user.** prefix. |
| value | string | Yes | Value of the extended attribute to set. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/test.txt";
let attrKey = "user.comment";
let attrValue = "Test file.";

try {
  fs.setxattrSync(filePath, attrKey, attrValue);
  console.info("Set extended attribute successfully.");
} catch (err) {
  console.error("Failed to set extended attribute with error message: " + err.message + ", error code: " + err.code);
}

#### fs.getxattr12+

getxattr(path: string, key: string): Promise<string>

Obtains an extended attribute of a file or directory. This API uses a promise to return the result.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | Application sandbox path of the file or directory. |
| key | string | Yes | Key of the extended attribute to obtain. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<string> | Promise used to return the value of the extended attribute obtained. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/test.txt";
let attrKey = "user.comment";

fs.getxattr(filePath, attrKey).then((attrValue: string) => {
  console.info("Get extended attribute succeed, the value is: " + attrValue);
}).catch((err: BusinessError) => {
  console.error("Failed to get extended attribute with error message: " + err.message + ", error code: " + err.code);
});

#### fs.getxattrSync12+

getxattrSync(path: string, key: string): string

Obtains an extended attribute of a file. This API returns the result synchronously.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | Application sandbox path of the file or directory. |
| key | string | Yes | Key of the extended attribute to obtain. |

**Return value**

| Type | Description |
| :-- | :-- |
| string | Value of the extended attribute obtained. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/test.txt";
let attrKey = "user.comment";

try {
  let attrValue = fs.getxattrSync(filePath, attrKey);
  console.info("Get extended attribute succeed, the value is: " + attrValue);
} catch (err) {
  console.error("Failed to get extended attribute with error message: " + err.message + ", error code: " + err.code);
}

#### fs.mkdir

mkdir(path: string): Promise<void>

Creates a directory. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | Application sandbox path of the directory. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
let dirPath = pathDir + "/testDir";
fs.mkdir(dirPath).then(() => {
  console.info("mkdir succeed");
}).catch((err: BusinessError) => {
  console.error("mkdir failed with error message: " + err.message + ", error code: " + err.code);
});

#### fs.mkdir11+

mkdir(path: string, recursion: boolean): Promise<void>

Creates a directory. This API uses a promise to return the result. The value **true** means to create a directory recursively.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | Application sandbox path of the directory. |
| recursion | boolean | Yes | 
Whether to create a directory recursively.

The value **true** means to create a directory recursively. The value **false** means to create a single-level directory.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
let dirPath = pathDir + "/testDir1/testDir2/testDir3";
fs.mkdir(dirPath, true).then(() => {
  console.info("mkdir succeed");
}).catch((err: BusinessError) => {
  console.error("mkdir failed with error message: " + err.message + ", error code: " + err.code);
});

#### fs.mkdir

mkdir(path: string, callback: AsyncCallback<void>): void

Creates a directory. This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | Application sandbox path of the directory. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
let dirPath = pathDir + "/testDir";
fs.mkdir(dirPath, (err: BusinessError) => {
  if (err) {
    console.error("mkdir failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("mkdir succeed");
  }
});

#### fs.mkdir11+

mkdir(path: string, recursion: boolean, callback: AsyncCallback<void>): void

Creates a directory. This API uses an asynchronous callback to return the result. The value **true** means to create a directory recursively.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | Application sandbox path of the directory. |
| recursion | boolean | Yes | 
Whether to create a directory recursively.

The value **true** means to create a directory recursively. The value **false** means to create a single-level directory.

 |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
let dirPath = pathDir + "/testDir1/testDir2/testDir3";
fs.mkdir(dirPath, true, (err: BusinessError) => {
  if (err) {
    console.error("mkdir failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("mkdir succeed");
  }
});

#### fs.mkdirSync

mkdirSync(path: string): void

Creates a directory. This API returns the result synchronously.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | Application sandbox path of the directory. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

let dirPath = pathDir + "/testDir";
fs.mkdirSync(dirPath);

#### fs.mkdirSync11+

mkdirSync(path: string, recursion: boolean): void

Creates a directory. This API returns the result synchronously. The value **true** means to create a directory recursively.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | Application sandbox path of the directory. |
| recursion | boolean | Yes | 
Whether to create a directory recursively.

The value **true** means to create a directory recursively. The value **false** means to create a single-level directory.

 |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

let dirPath = pathDir + "/testDir1/testDir2/testDir3";
fs.mkdirSync(dirPath, true);

#### fs.open

open(path: string, mode?: number): Promise<File>

Opens a file or directory. This API uses a promise to return the result. This API supports the use of a URI.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | Application sandbox path or URI of the file or directory. |
| mode | number | No | 
[Mode](#openmode) for opening the file or directory. You must specify one of the following options. By default, the file is opened in read-only mode.

\- **OpenMode.READ\_ONLY(0o0)**: Open the file in read-only mode.

\- **OpenMode.WRITE\_ONLY(0o1)**: Open the file in write-only mode.

\- **OpenMode.READ\_WRITE(0o2)**: Open the file in read/write mode.

You can add the following function options in bitwise OR mode. By default, no additional option is added.

\- **OpenMode.CREATE(0o100)**: Create a file if the file does not exist.

\- **OpenMode.TRUNC(0o1000)**: If the file exists and is opened in write mode, truncate the file length to 0.

\- **OpenMode.APPEND(0o2000)**: Open the file in append mode. New data will be added to the end of the file.

\- **OpenMode.NONBLOCK(0o4000)**: If **path** points to a named pipe (also known as a FIFO), block special file, or character special file, perform non-blocking operations on the opened file and in subsequent I/Os.

\- **OpenMode.DIR(0o200000)**: If **path** does not point to a directory, throw an exception. The write permission is not allowed.

\- **OpenMode.NOFOLLOW(0o400000)**: If **path** points to a symbolic link, throw an exception.

\- **OpenMode.SYNC(0o4010000)**: Open the file in synchronous I/O mode.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[File](#file)\> | Promise used to return the **File** object. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
fs.open(filePath, fs.OpenMode.READ\_WRITE | fs.OpenMode.CREATE).then((file: fs.File) => {
  console.info("file fd: " + file.fd);
  fs.closeSync(file);
}).catch((err: BusinessError) => {
  console.error("open file failed with error message: " + err.message + ", error code: " + err.code);
});

#### fs.open

open(path: string, mode: number, callback: AsyncCallback<File>): void

Opens a file or directory with the specified mode. This API uses an asynchronous callback to return the result.

This API supports the use of a URI.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | Application sandbox path or URI of a file or directory. |
| mode | number | Yes | 
[Mode](#openmode) for opening the file or directory. You must specify one of the following options. By default, the file is opened in read-only mode.

\- **OpenMode.READ\_ONLY(0o0)**: Open the file in read-only mode.

\- **OpenMode.WRITE\_ONLY(0o1)**: Open the file in write-only mode.

\- **OpenMode.READ\_WRITE(0o2)**: Open the file in read/write mode.

You can also specify the following options, separated by a bitwise OR operator (|). By default, no additional options are given.

\- **OpenMode.CREATE(0o100)**: If the file does not exist, create it.

\- **OpenMode.TRUNC(0o1000)**: If the file exists and is opened in write mode, truncate the file length to 0.

\- **OpenMode.APPEND(0o2000)**: Open the file in append mode. New data will be added to the end of the file.

\- **OpenMode.NONBLOCK(0o4000)**: If **path** points to a named pipe (also known as a FIFO), block special file, or character special file, perform non-blocking operations on the opened file and in subsequent I/Os.

\- **OpenMode.DIR(0o200000)**: If **path** does not point to a directory, throw an exception. The write permission is not allowed.

\- **OpenMode.NOFOLLOW(0o400000)**: If **path** points to a symbolic link, throw an exception.

\- **OpenMode.SYNC(0o4010000)**: Open the file in synchronous I/O mode.

 |
| callback | AsyncCallback<[File](#file)\> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
fs.open(filePath, fs.OpenMode.READ\_WRITE | fs.OpenMode.CREATE, (err: BusinessError, file: fs.File) => {
  if (err) {
    console.error("open failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("file fd: " + file.fd);
    fs.closeSync(file);
  }
});

#### fs.open

open(path: string, callback: AsyncCallback<File>): void

Opens a file or directory. This API uses an asynchronous callback to return the result. This API supports the use of a URI.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | Application sandbox path or URI of a file or directory. |
| callback | AsyncCallback<[File](#file)\> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
fs.open(filePath, (err: BusinessError, file: fs.File) => {
  if (err) {
    console.error("open failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("file fd: " + file.fd);
    fs.closeSync(file);
  }
});

#### fs.openSync

openSync(path: string, mode?: number): File

Opens a file or directory. This API returns the result synchronously. This API supports the use of a URI.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | Application sandbox path or URI of a file or directory to open. |
| mode | number | No | 
[Mode](#openmode) for opening the file or directory. You must specify one of the following options. By default, the file is opened in read-only mode.

\- **OpenMode.READ\_ONLY(0o0)**: Open the file in read-only mode.

\- **OpenMode.WRITE\_ONLY(0o1)**: Open the file in write-only mode.

\- **OpenMode.READ\_WRITE(0o2)**: Open the file in read/write mode.

You can also specify the following options, separated by a bitwise OR operator (|). By default, no additional options are given.

\- **OpenMode.CREATE(0o100)**: If the file does not exist, create it.

\- **OpenMode.TRUNC(0o1000)**: If the file exists and is opened in write mode, truncate the file length to 0.

\- **OpenMode.APPEND(0o2000)**: Open the file in append mode. New data will be added to the end of the file.

\- **OpenMode.NONBLOCK(0o4000)**: If **path** points to a named pipe (also known as a FIFO), block special file, or character special file, perform non-blocking operations on the opened file and in subsequent I/Os.

\- **OpenMode.DIR(0o200000)**: If **path** does not point to a directory, throw an exception. The write permission is not allowed.

\- **OpenMode.NOFOLLOW(0o400000)**: If **path** points to a symbolic link, throw an exception.

\- **OpenMode.SYNC(0o4010000)**: Open the file in synchronous I/O mode.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [File](#file) | File object opened. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

let filePath = pathDir + "/test.txt";
let file = fs.openSync(filePath, fs.OpenMode.READ\_WRITE | fs.OpenMode.CREATE);
console.info("file fd: " + file.fd);
fs.closeSync(file);

#### fs.read

read(fd: number, buffer: ArrayBuffer, options?: ReadOptions): Promise<number>

Reads file data. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| fd | number | Yes | FD of the file. |
| buffer | ArrayBuffer | Yes | Buffer used to store the file data read. |
| options | [ReadOptions](#readoptions11) | No | 
The options are as follows:

\- **offset** (number): start position to read the data. This parameter is optional. By default, data is read from the current position.

\- **length** (number): length of the data to read. This parameter is optional. The default value is the buffer length.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the length of the data read, in bytes. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { buffer } from '@kit.ArkTS';
let filePath = pathDir + "/test.txt";
let file = fs.openSync(filePath, fs.OpenMode.READ\_WRITE);
let arrayBuffer = new ArrayBuffer(4096);
fs.read(file.fd, arrayBuffer).then((readLen: number) => {
  console.info("read file data succeed");
  let buf = buffer.from(arrayBuffer, 0, readLen);
  console.info(\`The content of file: ${buf.toString()}\`);
}).catch((err: BusinessError) => {
  console.error("read file data failed with error message: " + err.message + ", error code: " + err.code);
}).finally(() => {
  fs.closeSync(file);
});

#### fs.read

read(fd: number, buffer: ArrayBuffer, options?: ReadOptions, callback: AsyncCallback<number>): void

Reads data from a file. This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| fd | number | Yes | FD of the file. |
| buffer | ArrayBuffer | Yes | Buffer used to store the file data read. |
| options | [ReadOptions](#readoptions11) | No | 
The options are as follows:

\- **offset** (number): start position to read the data. This parameter is optional. By default, data is read from the current position.

\- **length** (number): length of the data to read. This parameter is optional. The default value is the buffer length.

 |
| callback | AsyncCallback<number> | Yes | Callback used to return the length of the data read, in bytes. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { buffer } from '@kit.ArkTS';
let filePath = pathDir + "/test.txt";
let file = fs.openSync(filePath, fs.OpenMode.READ\_WRITE);
let arrayBuffer = new ArrayBuffer(4096);
fs.read(file.fd, arrayBuffer, (err: BusinessError, readLen: number) => {
  if (err) {
    console.error("read failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("read file data succeed");
    let buf = buffer.from(arrayBuffer, 0, readLen);
    console.info(\`The content of file: ${buf.toString()}\`);
  }
  fs.closeSync(file);
});

#### fs.readSync

readSync(fd: number, buffer: ArrayBuffer, options?: ReadOptions): number

Reads data from a file. This API returns the result synchronously.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| fd | number | Yes | FD of the file. |
| buffer | ArrayBuffer | Yes | Buffer used to store the file data read. |
| options | [ReadOptions](#readoptions11) | No | 
The options are as follows:

\- **offset** (number): start position to read the data. This parameter is optional. By default, data is read from the current position.

\- **length** (number): length of the data to read. This parameter is optional. The default value is the buffer length.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| number | Length of the data read, in bytes. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

let filePath = pathDir + "/test.txt";
let file = fs.openSync(filePath, fs.OpenMode.READ\_WRITE);
let buf = new ArrayBuffer(4096);
fs.readSync(file.fd, buf);
fs.closeSync(file);

#### fs.rmdir

rmdir(path: string): Promise<void>

Removes a directory and all its subdirectories and files. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/dvt1RoNLQUOwqR2WIwPXKw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062319Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=33DEB37DA931B83F571CBB5F041EEC71D8591BF0725E352DE266C8C9152CC0F3)

This API can be used to remove a single file. However, you are advised to use **unlink()** instead.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | Application sandbox path of the directory. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
let dirPath = pathDir + "/testDir";
fs.rmdir(dirPath).then(() => {
  console.info("rmdir succeed");
}).catch((err: BusinessError) => {
  console.error("rmdir failed with error message: " + err.message + ", error code: " + err.code);
});

#### fs.rmdir

rmdir(path: string, callback: AsyncCallback<void>): void

Removes a directory and all its subdirectories and files. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/7TSe1--URcShcS4d1_iHsQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062319Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9EE30D2E11202D275D8C1F8A24364B7FF0B46B6CD6FC10BF01AFD5D1E6E6FC71)

This API can be used to remove a single file. However, you are advised to use **unlink()** instead.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | Application sandbox path of the directory. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
let dirPath = pathDir + "/testDir";
fs.rmdir(dirPath, (err: BusinessError) => {
  if (err) {
    console.error("rmdir failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("rmdir succeed");
  }
});

#### fs.rmdirSync

rmdirSync(path: string): void

Removes a directory and all its subdirectories and files synchronously.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/JqKthjLwRGWogjP240D-Kg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062319Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E60FEACCDBD1C0A3005D1D553887FB4A9E38E8010BAE3502B04F7D07B8895BC9)

This API can be used to remove a single file. However, you are advised to use **unlinkSync** instead.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | Application sandbox path of the directory. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

let dirPath = pathDir + "/testDir";
fs.rmdirSync(dirPath);

#### fs.unlink

unlink(path: string): Promise<void>

Removes a file. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | Application sandbox path of the file. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
fs.unlink(filePath).then(() => {
  console.info("remove file succeed");
}).catch((err: BusinessError) => {
  console.error("remove file failed with error message: " + err.message + ", error code: " + err.code);
});

#### fs.unlink

unlink(path: string, callback: AsyncCallback<void>): void

Removes a file. This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | Application sandbox path of the file. |
| callback | AsyncCallback<void> | Yes | Callback invoked immediately after the file is removed. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
fs.unlink(filePath, (err: BusinessError) => {
  if (err) {
    console.error("remove file failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("remove file succeed");
  }
});

#### fs.unlinkSync

unlinkSync(path: string): void

Removes a file. This API returns the result synchronously.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | Application sandbox path of the file. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

let filePath = pathDir + "/test.txt";
fs.unlinkSync(filePath);

#### fs.write

write(fd: number, buffer: ArrayBuffer | string, options?: WriteOptions): Promise<number>

Writes data into a file. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| fd | number | Yes | FD of the file. |
| buffer | ArrayBuffer | string | Yes | Data to write. It can be a string or data from a buffer. |
| options | [WriteOptions](#writeoptions11) | No | 
The options are as follows:

\- **offset** (number): start position to write the data in the file. This parameter is optional. By default, data is written from the current position.

\- **length** (number): length of the data to write. This parameter is optional. The default value is the buffer length.

\- **encoding** (string): format of the data to be encoded when the data is a string. The default value is **'utf-8'**, which is the only value supported currently.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the length of the data written, in bytes. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
let file = fs.openSync(filePath, fs.OpenMode.READ\_WRITE | fs.OpenMode.CREATE);
let str: string = "hello, world";
fs.write(file.fd, str).then((writeLen: number) => {
  console.info("write data to file succeed and size is:" + writeLen);
}).catch((err: BusinessError) => {
  console.error("write data to file failed with error message: " + err.message + ", error code: " + err.code);
}).finally(() => {
  fs.closeSync(file);
});

#### fs.write

write(fd: number, buffer: ArrayBuffer | string, options?: WriteOptions, callback: AsyncCallback<number>): void

Writes data to a file. This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| fd | number | Yes | FD of the file. |
| buffer | ArrayBuffer | string | Yes | Data to write. It can be a string or data from a buffer. |
| options | [WriteOptions](#writeoptions11) | No | 
The options are as follows:

\- **offset** (number): start position to write the data in the file. This parameter is optional. By default, data is written from the current position.

\- **length** (number): length of the data to write. This parameter is optional. The default value is the buffer length.

\- **encoding** (string): format of the data to be encoded when the data is a string. The default value is **'utf-8'**, which is the only value supported currently.

 |
| callback | AsyncCallback<number> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
let file = fs.openSync(filePath, fs.OpenMode.READ\_WRITE | fs.OpenMode.CREATE);
let str: string = "hello, world";
fs.write(file.fd, str, (err: BusinessError, writeLen: number) => {
  if (err) {
    console.error("write data to file failed with error message:" + err.message + ", error code: " + err.code);
  } else {
    console.info("write data to file succeed and size is:" + writeLen);
  }
  fs.closeSync(file);
});

#### fs.writeSync

writeSync(fd: number, buffer: ArrayBuffer | string, options?: WriteOptions): number

Writes data to a file. This API returns the result synchronously.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| fd | number | Yes | FD of the file. |
| buffer | ArrayBuffer | string | Yes | Data to write. It can be a string or data from a buffer. |
| options | [WriteOptions](#writeoptions11) | No | 
The options are as follows:

\- **offset** (number): start position to write the data in the file. This parameter is optional. By default, data is written from the current position.

\- **length** (number): length of the data to write. This parameter is optional. The default value is the buffer length.

\- **encoding** (string): format of the data to be encoded when the data is a string. The default value is **'utf-8'**, which is the only value supported currently.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| number | Length of the data written, in bytes. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

let filePath = pathDir + "/test.txt";
let file = fs.openSync(filePath, fs.OpenMode.READ\_WRITE | fs.OpenMode.CREATE);
let str: string = "hello, world";
let writeLen = fs.writeSync(file.fd, str);
console.info("write data to file succeed and size is:" + writeLen);
fs.closeSync(file);

#### fs.truncate

truncate(file: string | number, len?: number): Promise<void>

Truncates a file. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| file | string | number | Yes | Application sandbox path or FD of the file. |
| len | number | No | File length, in bytes, after truncation. The default value is **0**. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
let len: number = 5;
fs.truncate(filePath, len).then(() => {
  console.info("truncate file succeed");
}).catch((err: BusinessError) => {
  console.error("truncate file failed with error message: " + err.message + ", error code: " + err.code);
});

#### fs.truncate

truncate(file: string | number, len?: number, callback: AsyncCallback<void>): void

Truncates a file. This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| file | string | number | Yes | Application sandbox path or FD of the file. |
| len | number | No | File length, in bytes, after truncation. The default value is **0**. |
| callback | AsyncCallback<void> | Yes | Callback that returns no value. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
let len: number = 5;
fs.truncate(filePath, len, (err: BusinessError) => {
  if (err) {
    console.error("truncate failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("truncate succeed");
  }
});

#### fs.truncateSync

truncateSync(file: string | number, len?: number): void

Truncates the file content. This API returns the result synchronously.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| file | string | number | Yes | Application sandbox path or FD of the file. |
| len | number | No | File length, in bytes, after truncation. The default value is **0**. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

let filePath = pathDir + "/test.txt";
let len: number = 5;
fs.truncateSync(filePath, len);

#### fs.readLines11+

readLines(filePath: string, options?: Options): Promise<ReaderIterator>

Reads the text content of a file line by line. This API uses a promise to return the result. Only the files in UTF-8 format are supported.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| filePath | string | Yes | Application sandbox path of the file. |
| options | [Options](#options11) | No | 
Options for reading the text. The options are as follows:

\- **encoding** (string): format of the data to be encoded.

It is valid only when the data is of the string type.

The default value is **'utf-8'**, which is the only value supported.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[ReaderIterator](#readeriterator11)\> | Promise used to return a **ReaderIterator** object. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo as fs, Options } from '@kit.CoreFileKit';
let filePath = pathDir + "/test.txt";
let options: Options = {
  encoding: 'utf-8'
};
fs.readLines(filePath, options).then((readerIterator: fs.ReaderIterator) => {
  for (let it = readerIterator.next(); !it.done; it = readerIterator.next()) {
    console.info("content: " + it.value);
  }
}).catch((err: BusinessError) => {
  console.error("readLines failed with error message: " + err.message + ", error code: " + err.code);
});

#### fs.readLines11+

readLines(filePath: string, options?: Options, callback: AsyncCallback<ReaderIterator>): void

Reads a file text line by line. This API uses an asynchronous callback to return the result. Only the files in UTF-8 format are supported.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| filePath | string | Yes | Application sandbox path of the file. |
| options | [Options](#options11) | No | 
Options for reading the text. The options are as follows:

\- **encoding** (string): format of the data to be encoded.

It is valid only when the data is of the string type.

The default value is **'utf-8'**, which is the only value supported.

 |
| callback | AsyncCallback<[ReaderIterator](#readeriterator11)\> | Yes | Callback used to return a **ReaderIterator** object. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo as fs, Options } from '@kit.CoreFileKit';
let filePath = pathDir + "/test.txt";
let options: Options = {
  encoding: 'utf-8'
};
fs.readLines(filePath, options, (err: BusinessError, readerIterator: fs.ReaderIterator) => {
  if (err) {
    console.error("readLines failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    for (let it = readerIterator.next(); !it.done; it = readerIterator.next()) {
      console.info("content: " + it.value);
    }
  }
});

#### fs.readLinesSync11+

readLinesSync(filePath: string, options?: Options): ReaderIterator

Reads the text content of a file line by line. This API returns the result synchronously.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| filePath | string | Yes | Application sandbox path of the file. |
| options | [Options](#options11) | No | 
Options for reading the text. The options are as follows:

\- **encoding** (string): format of the data to be encoded.

It is valid only when the data is of the string type.

The default value is **'utf-8'**, which is the only value supported.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [ReaderIterator](#readeriterator11) | **ReaderIterator** object. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

import { fileIo as fs, Options } from '@kit.CoreFileKit';
let filePath = pathDir + "/test.txt";
let options: Options = {
  encoding: 'utf-8'
};
let readerIterator = fs.readLinesSync(filePath, options);
for (let it = readerIterator.next(); !it.done; it = readerIterator.next()) {
  console.info("content: " + it.value);
}

#### ReaderIterator11+

Provides a **ReaderIterator** object. Before calling APIs of **ReaderIterator**, you need to use **readLines()** to create a **ReaderIterator** instance.

#### \[h2\]next11+

next(): ReaderIteratorResult

Obtains the **ReaderIterator** result.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Return value**

| Type | Description |
| :-- | :-- |
| [ReaderIteratorResult](#readeriteratorresult11) | **ReaderIteratorResult** object obtained. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/lupBRYM0QkSDudS1jf1dnA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062319Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CE25189D319A41596091FD4BE9037A40A4565634A3FB629E81AC03AD5154709D)

If the line read by **ReaderIterator** is not in UTF-8 format, error code 13900037 will be returned.

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo as fs, Options } from '@kit.CoreFileKit';
let filePath = pathDir + "/test.txt";
let options: Options = {
  encoding: 'utf-8'
};
fs.readLines(filePath, options).then((readerIterator: fs.ReaderIterator) => {
  for (let it = readerIterator.next(); !it.done; it = readerIterator.next()) {
    console.info("content: " + it.value);
  }
}).catch((err: BusinessError) => {
  console.error("readLines failed with error message: " + err.message + ", error code: " + err.code);
});

#### ReaderIteratorResult11+

Represents the information obtained by the **ReaderIterator** object.

**System capability**: SystemCapability.FileManagement.File.FileIO

| Name | Type | Description |
| :-- | :-- | :-- |
| done | boolean | Whether the iteration is complete. The value **true** means the iteration is complete; the value **false** means the opposite. |
| value | string | File text content read line by line. |

#### fs.readText

readText(filePath: string, options?: ReadTextOptions): Promise<string>

Reads the text content of a file. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| filePath | string | Yes | Application sandbox path of the file. |
| options | [ReadTextOptions](#readtextoptions11) | No | 
The options are as follows:

\- **offset** (number): start position to read the data. This parameter is optional. By default, data is read from the current position.

\- **length** (number): length of the data to read. This parameter is optional. The default value is the file length.

\- **encoding** (string): format of the data to be encoded.

It is valid only when the data is of the string type. The default value is **'utf-8'**, which is the only value supported.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<string> | Promise used to return the file content read. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
fs.readText(filePath).then((str: string) => {
  console.info("readText succeed:" + str);
}).catch((err: BusinessError) => {
  console.error("readText failed with error message: " + err.message + ", error code: " + err.code);
});

#### fs.readText

readText(filePath: string, options?: ReadTextOptions, callback: AsyncCallback<string>): void

Reads the text content of a file. This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| filePath | string | Yes | Application sandbox path of the file. |
| options | [ReadTextOptions](#readtextoptions11) | No | 
The options are as follows:

\- **offset** (number): start position to read the data. This parameter is optional. By default, data is read from the current position.

\- **length** (number): length of the data to read. This parameter is optional. The default value is the file length.

\- **encoding** (string): format of the data to be encoded. The default value is **'utf-8'**, which is the only value supported.

 |
| callback | AsyncCallback<string> | Yes | Callback used to return the content read. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo as fs, ReadTextOptions } from '@kit.CoreFileKit';
let filePath = pathDir + "/test.txt";
let stat = fs.statSync(filePath);
let readTextOption: ReadTextOptions = {
    offset: 1,
    length: stat.size,
    encoding: 'utf-8'
};
fs.readText(filePath, readTextOption, (err: BusinessError, str: string) => {
  if (err) {
    console.error("readText failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("readText succeed:" + str);
  }
});

#### fs.readTextSync

readTextSync(filePath: string, options?: ReadTextOptions): string

Reads the text content of a file. This API returns the result synchronously.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| filePath | string | Yes | Application sandbox path of the file. |
| options | [ReadTextOptions](#readtextoptions11) | No | 
The options are as follows:

\- **offset** (number): start position to read the data. This parameter is optional. By default, data is read from the current position.

\- **length** (number): length of the data to read. This parameter is optional. The default value is the file length.

\- **encoding** (string): format of the data to be encoded.

It is valid only when the data is of the string type. The default value is **'utf-8'**, which is the only value supported.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| string | Content of the file read. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

import { fileIo as fs, ReadTextOptions } from '@kit.CoreFileKit';
let filePath = pathDir + "/test.txt";
let readTextOptions: ReadTextOptions = {
  offset: 1,
  length: 0,
  encoding: 'utf-8'
};
let stat = fs.statSync(filePath);
readTextOptions.length = stat.size;
let str = fs.readTextSync(filePath, readTextOptions);
console.info("readText succeed:" + str);

#### fs.lstat

lstat(path: string): Promise<Stat>

Obtains information about a symbolic link that is used to refer to a file or directory. This API uses a promise to return the result.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | 
Application sandbox path or URI of the file.

**Note**: URIs can be passed since API version 22.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[Stat](#stat)\> | Promise used to return the symbolic link information obtained. For details, see **Stat**. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/linkToFile";
fs.lstat(filePath).then((stat: fs.Stat) => {
  console.info("lstat succeed, the size of file is " + stat.size);
}).catch((err: BusinessError) => {
  console.error("lstat failed with error message: " + err.message + ", error code: " + err.code);
});

#### fs.lstat

lstat(path: string, callback: AsyncCallback<Stat>): void

Obtains information about a symbolic link that is used to refer to a file or directory. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | 
Application sandbox path or URI of the file.

**Note**: URIs can be passed since API version 22.

 |
| callback | AsyncCallback<[Stat](#stat)\> | Yes | Callback used to return the symbolic link information obtained. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/linkToFile";
fs.lstat(filePath, (err: BusinessError, stat: fs.Stat) => {
  if (err) {
    console.error("lstat failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("lstat succeed, the size of file is " + stat.size);
  }
});

#### fs.lstatSync

lstatSync(path: string): Stat

Obtains information about a symbolic link that is used to refer to a file or directory. This API returns the result synchronously.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | 
Application sandbox path or URI of the file.

**Note**: URIs can be passed since API version 22.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [Stat](#stat) | File information obtained. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

let filePath = pathDir + "/linkToFile";
let fileStat = fs.lstatSync(filePath);
console.info("lstat succeed, the size of file is " + fileStat.size);

#### fs.rename

rename(oldPath: string, newPath: string): Promise<void>

Renames a file or directory. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/WMBu9LhYRAyktbLtofHuAA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062319Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=56DD7B53F7341B9CB8B03FEE2CAF9E20D5F4AB97A21F0CCA656FCB15AB2DB196)

This API is not supported in a distributed directory.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| oldPath | string | Yes | Application sandbox path of the file or directory to rename. |
| newPath | string | Yes | Application sandbox path of the renamed file or directory. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
let srcFile = pathDir + "/test.txt";
let dstFile = pathDir + "/new.txt";
fs.rename(srcFile, dstFile).then(() => {
  console.info("rename succeed");
}).catch((err: BusinessError) => {
  console.error("rename failed with error message: " + err.message + ", error code: " + err.code);
});

#### fs.rename

rename(oldPath: string, newPath: string, callback: AsyncCallback<void>): void

Renames a file or directory. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/Sb5-XGKHRaa96ufsESsEjQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062319Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=854DBC2F22F9CA342BDE8AC2E33C4B08BFB7EFBD611C2E2C346E84AEC28DC206)

This API is not supported in a distributed directory.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| oldPath | string | Yes | Application sandbox path of the file or directory to rename. |
| newPath | string | Yes | Application sandbox path of the renamed file or directory. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
let srcFile = pathDir + "/test.txt";
let dstFile = pathDir + "/new.txt";
fs.rename(srcFile, dstFile, (err: BusinessError) => {
  if (err) {
    console.error("rename failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("rename succeed");
  }
});

#### fs.renameSync

renameSync(oldPath: string, newPath: string): void

Renames a file or directory. This API returns the result synchronously.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/iCGsm_xYRGyagyoqOXRCaw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062319Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A321A6A91E41DA907247033C229DBCA4EDA5E6A04E199FE3684E574F2FA9226F)

This API is not supported in a distributed directory.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| oldPath | string | Yes | Application sandbox path of the file or directory to rename. |
| newPath | string | Yes | Application sandbox path of the renamed file or directory. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

let srcFile = pathDir + "/test.txt";
let dstFile = pathDir + "/new.txt";
fs.renameSync(srcFile, dstFile);

#### fs.fsync

fsync(fd: number): Promise<void>

Synchronizes the cached data of a file to storage. This API uses a promise to return the result.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| fd | number | Yes | FD of the file. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
let file = fs.openSync(filePath);
fs.fsync(file.fd).then(() => {
  console.info("sync data succeed");
}).catch((err: BusinessError) => {
  console.error("sync data failed with error message: " + err.message + ", error code: " + err.code);
}).finally(() => {
  fs.closeSync(file);
});

#### fs.fsync

fsync(fd: number, callback: AsyncCallback<void>): void

Synchronizes the cached data of a file to storage. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| fd | number | Yes | FD of the file. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
let file = fs.openSync(filePath);
fs.fsync(file.fd, (err: BusinessError) => {
  if (err) {
    console.error("fsync failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("fsync succeed");
  }
  fs.closeSync(file);
});

#### fs.fsyncSync

fsyncSync(fd: number): void

Synchronizes the cached data of a file to storage. This API returns the result synchronously.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| fd | number | Yes | FD of the file. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

let filePath = pathDir + "/test.txt";
let file = fs.openSync(filePath);
fs.fsyncSync(file.fd);
fs.closeSync(file);

#### fs.fdatasync

fdatasync(fd: number): Promise<void>

Synchronizes the data of a file. This API uses a promise to return the result.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| fd | number | Yes | FD of the file. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
let file = fs.openSync(filePath);
fs.fdatasync(file.fd).then(() => {
  console.info("sync data succeed");
}).catch((err: BusinessError) => {
  console.error("sync data failed with error message: " + err.message + ", error code: " + err.code);
}).finally(() => {
  fs.closeSync(file);
});

#### fs.fdatasync

fdatasync(fd: number, callback: AsyncCallback<void>): void

Synchronizes the data of a file. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| fd | number | Yes | FD of the file. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
let file = fs.openSync(filePath);
fs.fdatasync(file.fd, (err: BusinessError) => {
  if (err) {
    console.error("fdatasync failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("fdatasync succeed");
  }
  fs.closeSync(file);
});

#### fs.fdatasyncSync

fdatasyncSync(fd: number): void

Synchronizes the data of a file. This API returns the result synchronously.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| fd | number | Yes | FD of the file. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

let filePath = pathDir + "/test.txt";
let file = fs.openSync(filePath);
fs.fdatasyncSync(file.fd);
fs.closeSync(file);

#### fs.symlink

symlink(target: string, srcPath: string): Promise<void>

Creates a symbolic link based on a file path. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/_YRvGgQbSnyYOJ4BbGZ3uA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062319Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EE20B633C73F9DCE7C1783FF1FE2AC6D139796C2C837246E619344511C0DE22F)

Since API version 11, this API cannot be used by third-party applications.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| target | string | Yes | Application sandbox path of the target file. |
| srcPath | string | Yes | Application sandbox path of the symbolic link. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
let srcFile = pathDir + "/test.txt";
let dstFile = pathDir + "/test";
fs.symlink(srcFile, dstFile).then(() => {
  console.info("symlink succeed");
}).catch((err: BusinessError) => {
  console.error("symlink failed with error message: " + err.message + ", error code: " + err.code);
});

#### fs.symlink

symlink(target: string, srcPath: string, callback: AsyncCallback<void>): void

Creates a symbolic link based on the file path. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/kJcQXdPHTM6YNVO4gEBvMg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062319Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=719DA41504BEDE1C861DFC1ED5F62B8E7FD065DE9ED074BC74506DFBBCC26B43)

Since API version 11, this API cannot be used by third-party applications.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| target | string | Yes | Application sandbox path of the target file. |
| srcPath | string | Yes | Application sandbox path of the symbolic link. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
let srcFile = pathDir + "/test.txt";
let dstFile = pathDir + "/test";
fs.symlink(srcFile, dstFile, (err: BusinessError) => {
  if (err) {
    console.error("symlink failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("symlink succeed");
  }
});

#### fs.symlinkSync

symlinkSync(target: string, srcPath: string): void

Creates a symbolic link based on the file path. This API returns the result synchronously.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/GseWTqcHQYquYblAKUPT9A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062319Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=80100932E9B49AEF0D171FFF959AE95EBA7A70AC6191328389F53F985C968DBB)

Since API version 11, this API cannot be used by third-party applications.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| target | string | Yes | Application sandbox path of the target file. |
| srcPath | string | Yes | Application sandbox path of the symbolic link. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

let srcFile = pathDir + "/test.txt";
let dstFile = pathDir + "/test";
fs.symlinkSync(srcFile, dstFile);

#### fs.listFile

listFile(path: string, options?: ListFileOptions): Promise<string\[\]>

Lists the names of all files and directories in the current path. Filtering is supported. This API uses a promise to return the result.

You can configure the **recursion** parameter in **options** to recursively list the relative paths of all files. The relative path starts with a slash (/).

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | Application sandbox path of the directory. |
| options | [ListFileOptions](#listfileoptions11) | No | Options for filtering files. The files are not filtered by default. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<string\[\]> | Promise used to return the file name array, which is encoded in UTF-8 format by default. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo as fs, Filter, ListFileOptions } from '@kit.CoreFileKit';
let listFileOption: ListFileOptions = {
  recursion: false,
  listNum: 0,
  filter: {
    suffix: \[".png", ".jpg", ".jpeg"\],
    displayName: \["\*abc", "efg\*"\],
    fileSizeOver: 1024
  }
}
fs.listFile(pathDir, listFileOption).then((filenames: Array<string>) => {
  console.info("listFile succeed");
  for (let i = 0; i < filenames.length; i++) {
    console.info("fileName: %s", filenames\[i\]);
  }
}).catch((err: BusinessError) => {
  console.error("list file failed with error message: " + err.message + ", error code: " + err.code);
});

#### fs.listFile

listFile(path: string, options?: ListFileOptions, callback: AsyncCallback<string\[\]>): void

Lists the names of all files and directories in the current path. Filtering is supported. This API uses an asynchronous callback to return the result.

You can configure the **recursion** parameter in **options** to recursively list the relative paths of all files. The relative path starts with a slash (/).

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | Application sandbox path of the directory. |
| options | [ListFileOptions](#listfileoptions11) | No | Options for filtering files. The files are not filtered by default. |
| callback | AsyncCallback<string\[\]> | Yes | Callback used to return the file names listed. The files are encoded in UTF-8 by default. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo as fs, Filter, ListFileOptions } from '@kit.CoreFileKit';
let listFileOption: ListFileOptions = {
  recursion: false,
  listNum: 0,
  filter: {
    suffix: \[".png", ".jpg", ".jpeg"\],
    displayName: \["\*abc", "efg\*"\],
    fileSizeOver: 1024
  }
};
fs.listFile(pathDir, listFileOption, (err: BusinessError, filenames: Array<string>) => {
  if (err) {
    console.error("list file failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("listFile succeed");
    for (let i = 0; i < filenames.length; i++) {
      console.info("filename: %s", filenames\[i\]);
    }
  }
});

#### fs.listFileSync

listFileSync(path: string, options?: ListFileOptions): string\[\]

Lists the names of all files and directories in the current directory. This API returns the result synchronously. Filtering is supported.

You can configure the **recursion** parameter in **options** to recursively list the relative paths of all files. The relative path starts with a slash (/).

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | Application sandbox path of the directory. |
| options | [ListFileOptions](#listfileoptions11) | No | Options for filtering files. The files are not filtered by default. |

**Return value**

| Type | Description |
| :-- | :-- |
| string\[\] | File name array, which is encoded in UTF-8 format by default. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

import { fileIo as fs, Filter, ListFileOptions} from '@kit.CoreFileKit';
let listFileOption: ListFileOptions = {
  recursion: false,
  listNum: 0,
  filter: {
    suffix: \[".png", ".jpg", ".jpeg"\],
    displayName: \["\*abc", "efg\*"\],
    fileSizeOver: 1024
  }
};
let filenames = fs.listFileSync(pathDir, listFileOption);
console.info("listFile succeed");
for (let i = 0; i < filenames.length; i++) {
  console.info("filename: %s", filenames\[i\]);
}

#### fs.lseek11+

lseek(fd: number, offset: number, whence?: WhenceType): number

Adjusts the position of the file offset pointer.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| fd | number | Yes | File descriptor. |
| offset | number | Yes | Relative offset, in bytes. |
| whence | [WhenceType](#whencetype11) | No | Where to start the offset. If this parameter is not specified, the file start position is used by default. |

**Return value**

| Type | Description |
| :-- | :-- |
| number | Position of the current offset as measured from the beginning of the file, in bytes. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

let filePath = pathDir + "/test.txt";
let file = fs.openSync(filePath, fs.OpenMode.CREATE | fs.OpenMode.READ\_WRITE);
console.info('The current offset is at ' + fs.lseek(file.fd, 5, fs.WhenceType.SEEK\_SET));
fs.closeSync(file);

#### fs.moveDir10+

moveDir(src: string, dest: string, mode?: number): Promise<void>

Moves the source directory to the destination directory. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1/v3/KpClxFJKS0a7JoWTWt44Ug/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062319Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=65D41915CA166A4ED3A2810C34F1F96F125D4ECAD930EBEC74A1723A804350F2)

This API is not supported in a distributed directory.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| src | string | Yes | Application sandbox path of the source directory. |
| dest | string | Yes | Application sandbox path of the destination directory. |
| mode | number | No | 
Move mode. The default value is **0**.

\- **0**: Throw an exception if a directory conflict occurs.

An exception will be thrown if the destination directory contains a non-empty directory with the same name as the source directory.

\- **1**: Throw an exception if a file conflict occurs.

An exception will be thrown if the destination directory contains a directory with the same name as the source directory, and a file with the same name exists in the conflict directory. All the non-conflicting files in the source directory will be moved to the destination directory, and the non-conflicting files in the destination directory will be retained. The data attribute in the error returned provides information about the conflicting files in the Array<[ConflictFiles](#conflictfiles10)\> format.

\- **2**: Forcibly overwrite the conflicting files in the destination directory.

When the destination directory contains a directory with the same name as the source directory, the files with the same names in the destination directory are overwritten forcibly; the files without conflicts in the destination directory are retained.

\- **3**: Forcibly overwrite the conflicting directory.

The source directory is moved to the destination directory, and the content of the moved directory is the same as that of the source directory. If the destination directory contains a directory with the same name as the source directory, all original files in the directory will be deleted.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
let srcPath = pathDir + "/srcDir";
let destPath = pathDir + "/destDir";
fs.moveDir(srcPath, destPath, 1).then(() => {
  console.info("move directory succeed");
}).catch((err: BusinessError) => {
  console.error("move directory failed with error message: " + err.message + ", error code: " + err.code);
});

#### fs.moveDir10+

moveDir(src: string, dest: string, mode: number, callback: AsyncCallback<void, Array<ConflictFiles>>): void

Moves the source directory to the destination directory. You can set the move mode. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/Amb-xyzrQHu37daE8drvQQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062319Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5BC82AD42D3EE2A8E9E08BD8C806FDBADFEBDA9473E62A043F93669CCEAE80CF)

This API is not supported in a distributed directory.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| src | string | Yes | Application sandbox path of the source directory. |
| dest | string | Yes | Application sandbox path of the destination directory. |
| mode | number | Yes | 
Move mode. The default value is **0**.

\- **0**: Throw an exception if a directory conflict occurs.

An exception will be thrown if the destination directory contains a directory with the same name as the source directory.

\- **1**: Throw an exception if a file conflict occurs.

An exception will be thrown if the destination directory contains a directory with the same name as the source directory, and a file with the same name exists in the conflict directory. All the non-conflicting files in the source directory will be moved to the destination directory, and the non-conflicting files in the destination directory will be retained. The data attribute in the error returned provides information about the conflicting files in the Array<[ConflictFiles](#conflictfiles10)\> format.

\- **2**: Forcibly overwrite the conflicting files in the destination directory.

When the destination directory contains a directory with the same name as the source directory, the files with the same names in the destination directory are overwritten forcibly; the files without conflicts in the destination directory are retained.

\- **3**: Forcibly overwrite the conflicting directory.

The source directory is moved to the destination directory, and the content of the moved directory is the same as that of the source directory. If the destination directory contains a directory with the same name as the source directory, all original files in the directory will be deleted.

 |
| callback | AsyncCallback<void, Array<[ConflictFiles](#conflictfiles10)\>> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo as fs, ConflictFiles } from '@kit.CoreFileKit';
let srcPath = pathDir + "/srcDir";
let destPath = pathDir + "/destDir";
fs.moveDir(srcPath, destPath, 1, (err: BusinessError<Array<ConflictFiles>>) => {
  if (err && err.code == 13900015 && err.data?.length !== undefined) {
    for (let i = 0; i < err.data.length; i++) {
      console.error("move directory failed with conflicting files: " + err.data\[i\].srcFile + " " + err.data\[i\].destFile);
    }
  } else if (err) {
    console.error("move directory failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("move directory succeed");
  }
});

#### fs.moveDir10+

moveDir(src: string, dest: string, callback: AsyncCallback<void, Array<ConflictFiles>>): void

Moves the source directory to the destination directory. This API uses an asynchronous callback to return the result.

An exception will be thrown if a directory conflict occurs, that is, the destination directory contains a directory with the same name as the source directory.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/I004taxiSqK83KkP7AFKlg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062319Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=48D8D0A780391B5F3FF9D063B4024EE7C21E3D667E32EDCA7B36581D590C3B7F)

This API is not supported in a distributed directory.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| src | string | Yes | Application sandbox path of the source directory. |
| dest | string | Yes | Application sandbox path of the destination directory. |
| callback | AsyncCallback<void, Array<[ConflictFiles](#conflictfiles10)\>> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo as fs, ConflictFiles } from '@kit.CoreFileKit';
let srcPath = pathDir + "/srcDir";
let destPath = pathDir + "/destDir";
fs.moveDir(srcPath, destPath, (err: BusinessError<Array<ConflictFiles>>) => {
  if (err && err.code == 13900015 && err.data?.length !== undefined) {
    for (let i = 0; i < err.data.length; i++) {
      console.error("move directory failed with conflicting files: " + err.data\[i\].srcFile + " " + err.data\[i\].destFile);
    }
  } else if (err) {
    console.error("move directory failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("move directory succeed");
  }
});

#### fs.moveDirSync10+

moveDirSync(src: string, dest: string, mode?: number): void

Moves the source directory to the destination directory. This API returns the result synchronously.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/VJ5Eq9fZQw6-zbESxqMhCg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062319Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=58A7B8E8F584E83024792BC3964929A740DD65060E7C1B584E72F439E98B9C00)

This API is not supported in a distributed directory.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| src | string | Yes | Application sandbox path of the source directory. |
| dest | string | Yes | Application sandbox path of the destination directory. |
| mode | number | No | 
Move mode. The default value is **0**.

\- **0**: Throw an exception if a directory conflict occurs.

An exception will be thrown if the destination directory contains a directory with the same name as the source directory.

\- **1**: Throw an exception if a file conflict occurs.

An exception will be thrown if the destination directory contains a directory with the same name as the source directory, and a file with the same name exists in the conflict directory. All the non-conflicting files in the source directory will be moved to the destination directory, and the non-conflicting files in the destination directory will be retained. The data attribute in the error returned provides information about the conflicting files in the Array<[ConflictFiles](#conflictfiles10)\> format.

\- **2**: Forcibly overwrite the conflicting files in the destination directory.

When the destination directory contains a directory with the same name as the source directory, the files with the same names in the destination directory are overwritten forcibly; the files without conflicts in the destination directory are retained.

\- **3**: Forcibly overwrite the conflicting directory.

The source directory is moved to the destination directory, and the content of the moved directory is the same as that of the source directory. If the destination directory contains a directory with the same name as the source directory, all original files in the directory will be deleted.

 |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo as fs, ConflictFiles } from '@kit.CoreFileKit';
let srcPath = pathDir + "/srcDir";
let destPath = pathDir + "/destDir";
try {
  fs.moveDirSync(srcPath, destPath, 1);
  console.info("move directory succeed");
} catch (error) {
  let err: BusinessError<Array<ConflictFiles>> = error as BusinessError<Array<ConflictFiles>>;
  if (err.code == 13900015 && err.data?.length !== undefined) {
    for (let i = 0; i < err.data.length; i++) {
      console.error("move directory failed with conflicting files: " + err.data\[i\].srcFile + " " + err.data\[i\].destFile);
    }
  } else {
    console.error("move directory failed with error message: " + err.message + ", error code: " + err.code);
  }
}

#### fs.moveFile

moveFile(src: string, dest: string, mode?: number): Promise<void>

Moves a file. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/u0YUS9j8SDuMyJYPSGC6jw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062319Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A2A64961EA3DDE44495D63E574416F3D1C8A3B4951E5011090FB6D3DAB9E1CD1)

This API is not supported in a distributed directory.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| src | string | Yes | Application sandbox path of the file to move. |
| dest | string | Yes | Application sandbox path of the destination file. |
| mode | number | No | 
Move mode.

The value **0** means to overwrite the file with the same name in the destination directory; the value **1** means to throw an exception. The default value is **0**.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
let srcPath = pathDir + "/source.txt";
let destPath = pathDir + "/dest.txt";
fs.moveFile(srcPath, destPath, 0).then(() => {
  console.info("move file succeed");
}).catch((err: BusinessError) => {
  console.error("move file failed with error message: " + err.message + ", error code: " + err.code);
});

#### fs.moveFile

moveFile(src: string, dest: string, mode: number, callback: AsyncCallback<void>): void

Moves a file with the specified mode. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/dkc9tQDDQYmVabTQn-jP4w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062319Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5CC84EB717260CAFDBC80FA5E84E8C0FE98DB5814961698943B91C581E1250BA)

This API is not supported in a distributed directory.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| src | string | Yes | Application sandbox path of the file to move. |
| dest | string | Yes | Application sandbox path of the destination file. |
| mode | number | Yes | 
Move mode.

The value **0** means to overwrite the file with the same name in the destination directory; the value **1** means to throw an exception. The default value is **0**.

 |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
let srcPath = pathDir + "/source.txt";
let destPath = pathDir + "/dest.txt";
fs.moveFile(srcPath, destPath, 0, (err: BusinessError) => {
  if (err) {
    console.error("move file failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("move file succeed");
  }
});

#### fs.moveFile

moveFile(src: string, dest: string, callback: AsyncCallback<void>): void

Moves a file and forcibly overwrites the file with the same name in the destination directory. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/Ajj5r7jeQQuAKFghn-IYnQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062319Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D2C8F10F95A9B6D44AC27C2D1D7B8D8918CBBA930F38B04FB5ADC3F92C214C8C)

This API is not supported in a distributed directory.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| src | string | Yes | Application sandbox path of the file to move. |
| dest | string | Yes | Application sandbox path of the destination file. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
let srcPath = pathDir + "/source.txt";
let destPath = pathDir + "/dest.txt";
fs.moveFile(srcPath, destPath, (err: BusinessError) => {
  if (err) {
    console.error("move file failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("move file succeed");
  }
});

#### fs.moveFileSync

moveFileSync(src: string, dest: string, mode?: number): void

Moves a file. This API returns the result synchronously.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/tDIgWoyTQZ-oCFW-rWgRHg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062319Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=60F3C0669667603BDDD83E926D067942479EC545C4E3E8681471CF9144FC726B)

This API is not supported in a distributed directory.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| src | string | Yes | Application sandbox path of the file to move. |
| dest | string | Yes | Application sandbox path of the destination file. |
| mode | number | No | 
Move mode.

The value **0** means to overwrite the file with the same name in the destination directory; the value **1** means to throw an exception. The default value is **0**.

 |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

let srcPath = pathDir + "/source.txt";
let destPath = pathDir + "/dest.txt";
fs.moveFileSync(srcPath, destPath, 0);
console.info("move file succeed");

#### fs.mkdtemp

mkdtemp(prefix: string): Promise<string>

Creates a temporary directory. This API uses a promise to return the result.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| prefix | string | Yes | String to be replaced with six randomly generated characters to create a unique temporary directory. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<string> | Promise used to return the directory created. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
fs.mkdtemp(pathDir + "/XXXXXX").then((dir: string) => {
  console.info("mkdtemp succeed:" + dir);
}).catch((err: BusinessError) => {
  console.error("mkdtemp failed with error message: " + err.message + ", error code: " + err.code);
});

#### fs.mkdtemp

mkdtemp(prefix: string, callback: AsyncCallback<string>): void

Creates a temporary directory. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| prefix | string | Yes | String to be replaced with six randomly generated characters to create a unique temporary directory. |
| callback | AsyncCallback<string> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
fs.mkdtemp(pathDir + "/XXXXXX", (err: BusinessError, res: string) => {
  if (err) {
    console.error("mkdtemp failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("mkdtemp succeed");
  }
});

#### fs.mkdtempSync

mkdtempSync(prefix: string): string

Creates a temporary directory. This API returns the result synchronously.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| prefix | string | Yes | String to be replaced with six randomly generated characters to create a unique temporary directory. |

**Return value**

| Type | Description |
| :-- | :-- |
| string | Unique directory generated. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

let res = fs.mkdtempSync(pathDir + "/XXXXXX");

#### fs.utimes11+

utimes(path: string, mtime: number): void

Changes the time when the file was last modified.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | Application sandbox path of the file. |
| mtime | number | Yes | New timestamp. The value is the number of milliseconds elapsed since the Epoch time (00:00:00 UTC on January 1, 1970). Only the time when the file was last modified can be changed. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

let filePath = pathDir + "/test.txt";
let file = fs.openSync(filePath, fs.OpenMode.CREATE | fs.OpenMode.READ\_WRITE);
fs.writeSync(file.fd, 'test data');
fs.closeSync(file);
fs.utimes(filePath, new Date().getTime());

#### fs.createRandomAccessFile10+

createRandomAccessFile(file: string | File, mode?: number): Promise<RandomAccessFile>

Creates a **RandomAccessFile** instance based on the specified file path or file object. This API uses a promise to return the result.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| file | string | [File](#file) | Yes | Application sandbox path of the file or an opened file object. |
| mode | number | No | 
[Mode](#openmode) for creating the **RandomAccessFile** instance. This parameter is valid only when the application sandbox path of the file is passed in. One of the following options must be specified:

\- **OpenMode.READ\_ONLY(0o0)**: Create the file in read-only mode. This is the default value.

\- **OpenMode.WRITE\_ONLY(0o1)**: Create the file in write-only mode.

\- **OpenMode.READ\_WRITE(0o2)**: Create the file in read/write mode.

You can also specify the following options, separated by a bitwise OR operator (|). By default, no additional options are given.

\- **OpenMode.CREATE(0o100)**: If the file does not exist, create it.

\- **OpenMode.TRUNC(0o1000)**: If the **RandomAccessFile** object already exists and is created in write mode, truncate the file length to 0.

\- **OpenMode.APPEND(0o2000)**: Create the file in append mode. New data will be added to the end of the **RandomAccessFile** object.

\- **OpenMode.NONBLOCK(0o4000)**: If **path** points to a named pipe (also known as a FIFO), block special file, or character special file, perform non-blocking operations on the created file and in subsequent I/Os.

\- **OpenMode.DIR(0o200000)**: If **path** does not point to a directory, throw an exception. The write permission is not allowed.

\- **OpenMode.NOFOLLOW(0o400000)**: If **path** points to a symbolic link, throw an exception.

\- **OpenMode.SYNC(0o4010000)**: Create a **RandomAccessFile** instance in synchronous I/O mode.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[RandomAccessFile](#randomaccessfile10)\> | Promise used to return the **RandomAccessFile** instance created. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
let file = fs.openSync(filePath, fs.OpenMode.CREATE | fs.OpenMode.READ\_WRITE);
fs.createRandomAccessFile(file).then((randomAccessFile: fs.RandomAccessFile) => {
  console.info("randomAccessFile fd: " + randomAccessFile.fd);
  randomAccessFile.close();
}).catch((err: BusinessError) => {
  console.error("create randomAccessFile failed with error message: " + err.message + ", error code: " + err.code);
}).finally(() => {
  fs.closeSync(file);
});

#### fs.createRandomAccessFile10+

createRandomAccessFile(file: string | File, callback: AsyncCallback<RandomAccessFile>): void

Creates a **RandomAccessFile** object in read-only mode based on a file path or file object. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| file | string | [File](#file) | Yes | Application sandbox path of the file or an opened file object. |
| callback | AsyncCallback<[RandomAccessFile](#randomaccessfile10)\> | Yes | Callback used to return the **RandomAccessFile** instance created. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
let file = fs.openSync(filePath, fs.OpenMode.CREATE | fs.OpenMode.READ\_WRITE);
fs.createRandomAccessFile(file, (err: BusinessError, randomAccessFile: fs.RandomAccessFile) => {
  if (err) {
    console.error("create randomAccessFile failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("randomAccessFile fd: " + randomAccessFile.fd);
    randomAccessFile.close();
  }
  fs.closeSync(file);
});

#### fs.createRandomAccessFile10+

createRandomAccessFile(file: string | File, mode: number, callback: AsyncCallback<RandomAccessFile>): void

Creates a **RandomAccessFile** instance based on a file path or file object. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| file | string | [File](#file) | Yes | Application sandbox path of the file or an opened file object. |
| mode | number | Yes | 
[Mode](#openmode) for creating the **RandomAccessFile** instance. This parameter is valid only when the application sandbox path of the file is passed in. One of the following options must be specified:

\- **OpenMode.READ\_ONLY(0o0)**: Create the file in read-only mode. This is the default value.

\- **OpenMode.WRITE\_ONLY(0o1)**: Create the file in write-only mode.

\- **OpenMode.READ\_WRITE(0o2)**: Create the file in read/write mode.

You can also specify the following options, separated by a bitwise OR operator (|). By default, no additional options are given.

\- **OpenMode.CREATE(0o100)**: If the file does not exist, create it.

\- **OpenMode.TRUNC(0o1000)**: If the **RandomAccessFile** object already exists and is created in write mode, truncate the file length to 0.

\- **OpenMode.APPEND(0o2000)**: Create the file in append mode. New data will be added to the end of the **RandomAccessFile** object.

\- **OpenMode.NONBLOCK(0o4000)**: If **path** points to a named pipe (also known as a FIFO), block special file, or character special file, perform non-blocking operations on the created file and in subsequent I/Os.

\- **OpenMode.DIR(0o200000)**: If **path** does not point to a directory, throw an exception. The write permission is not allowed.

\- **OpenMode.NOFOLLOW(0o400000)**: If **path** points to a symbolic link, throw an exception.

\- **OpenMode.SYNC(0o4010000)**: Create a **RandomAccessFile** instance in synchronous I/O mode.

 |
| callback | AsyncCallback<[RandomAccessFile](#randomaccessfile10)\> | Yes | Callback used to return the **RandomAccessFile** instance created. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
let file = fs.openSync(filePath, fs.OpenMode.CREATE | fs.OpenMode.READ\_WRITE);
fs.createRandomAccessFile(file, fs.OpenMode.READ\_ONLY, (err: BusinessError, randomAccessFile: fs.RandomAccessFile) => {
  if (err) {
    console.error("create randomAccessFile failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("randomAccessFile fd: " + randomAccessFile.fd);
    randomAccessFile.close();
  }
  fs.closeSync(file);
});

#### fs.createRandomAccessFile12+

createRandomAccessFile(file: string | File, mode?: number, options?: RandomAccessFileOptions): Promise<RandomAccessFile>

Creates a **RandomAccessFile** instance based on the specified file path or file object. This API uses a promise to return the result.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| file | string | [File](#file) | Yes | Application sandbox path of the file or an opened file object. |
| mode | number | No | 
[Mode](#openmode) for creating the **RandomAccessFile** instance. This parameter is valid only when the application sandbox path of the file is passed in. One of the following options must be specified:

\- **OpenMode.READ\_ONLY(0o0)**: Create the file in read-only mode. This is the default value.

\- **OpenMode.WRITE\_ONLY(0o1)**: Create the file in write-only mode.

\- **OpenMode.READ\_WRITE(0o2)**: Create the file in read/write mode.

You can also specify the following options, separated by a bitwise OR operator (|). By default, no additional options are given.

\- **OpenMode.CREATE(0o100)**: If the file does not exist, create it.

\- **OpenMode.TRUNC(0o1000)**: If the **RandomAccessFile** object already exists and is created in write mode, truncate the file length to 0.

\- **OpenMode.APPEND(0o2000)**: Create the file in append mode. New data will be added to the end of the **RandomAccessFile** object.

\- **OpenMode.NONBLOCK(0o4000)**: If **path** points to a named pipe (also known as a FIFO), block special file, or character special file, perform non-blocking operations on the created file and in subsequent I/Os.

\- **OpenMode.DIR(0o200000)**: If **path** does not point to a directory, throw an exception. The write permission is not allowed.

\- **OpenMode.NOFOLLOW(0o400000)**: If **path** points to a symbolic link, throw an exception.

\- **OpenMode.SYNC(0o4010000)**: Create a **RandomAccessFile** instance in synchronous I/O mode.

 |
| options | [RandomAccessFileOptions](#randomaccessfileoptions12) | No | 

The options are as follows:

\- **start** (number): start position of the data to read in the file. This parameter is optional. By default, data is read from the current position.

\- **end** (number): end position of the data to read in the file. This parameter is optional. The default value is the end of the file.

This parameter takes effect only for file stream objects obtained by [getreadstream](#getreadstream12) and [getwritestream](#getwritestream12).

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[RandomAccessFile](#randomaccessfile10)\> | Promise used to return the **RandomAccessFile** instance created. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
fs.createRandomAccessFile(filePath, fs.OpenMode.CREATE | fs.OpenMode.READ\_WRITE, { start: 10, end: 100 })
  .then((randomAccessFile: fs.RandomAccessFile) => {
    console.info("randomAccessFile fd: " + randomAccessFile.fd);
    randomAccessFile.close();
  })
  .catch((err: BusinessError) => {
    console.error("create randomAccessFile failed with error message: " + err.message + ", error code: " + err.code);
  });

#### fs.createRandomAccessFileSync10+

createRandomAccessFileSync(file: string | File, mode?: number): RandomAccessFile

Creates a **RandomAccessFile** instance based on a file path or file object.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| file | string | [File](#file) | Yes | Application sandbox path of the file or an opened file object. |
| mode | number | No | 
[Mode](#openmode) for creating the **RandomAccessFile** instance. This parameter is valid only when the application sandbox path of the file is passed in. One of the following options must be specified:

\- **OpenMode.READ\_ONLY(0o0)**: Create the file in read-only mode. This is the default value.

\- **OpenMode.WRITE\_ONLY(0o1)**: Create the file in write-only mode.

\- **OpenMode.READ\_WRITE(0o2)**: Create the file in read/write mode.

You can also specify the following options, separated by a bitwise OR operator (|). By default, no additional options are given.

\- **OpenMode.CREATE(0o100)**: If the file does not exist, create it.

\- **OpenMode.TRUNC(0o1000)**: If the **RandomAccessFile** object already exists and is created in write mode, truncate the file length to 0.

\- **OpenMode.APPEND(0o2000)**: Create the file in append mode. New data will be added to the end of the **RandomAccessFile** object.

\- **OpenMode.NONBLOCK(0o4000)**: If **path** points to a named pipe (also known as a FIFO), block special file, or character special file, perform non-blocking operations on the created file and in subsequent I/Os.

\- **OpenMode.DIR(0o200000)**: If **path** does not point to a directory, throw an exception. The write permission is not allowed.

\- **OpenMode.NOFOLLOW(0o400000)**: If **path** points to a symbolic link, throw an exception.

\- **OpenMode.SYNC(0o4010000)**: Create a **RandomAccessFile** instance in synchronous I/O mode.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [RandomAccessFile](#randomaccessfile10) | **RandomAccessFile** instance created. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

let filePath = pathDir + "/test.txt";
let file = fs.openSync(filePath, fs.OpenMode.CREATE | fs.OpenMode.READ\_WRITE);
let randomAccessFile = fs.createRandomAccessFileSync(file);
randomAccessFile.close();

#### fs.createRandomAccessFileSync12+

createRandomAccessFileSync(file: string | File, mode?: number, options?: RandomAccessFileOptions): RandomAccessFile

Creates a **RandomAccessFile** instance based on a file path or file object.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| file | string | [File](#file) | Yes | Application sandbox path of the file or an opened file object. |
| mode | number | No | 
[Mode](#openmode) for creating the **RandomAccessFile** instance. This parameter is valid only when the application sandbox path of the file is passed in. One of the following options must be specified:

\- **OpenMode.READ\_ONLY(0o0)**: Create the file in read-only mode. This is the default value.

\- **OpenMode.WRITE\_ONLY(0o1)**: Create the file in write-only mode.

\- **OpenMode.READ\_WRITE(0o2)**: Create the file in read/write mode.

You can also specify the following options, separated by a bitwise OR operator (|). By default, no additional options are given.

\- **OpenMode.CREATE(0o100)**: If the file does not exist, create it.

\- **OpenMode.TRUNC(0o1000)**: If the **RandomAccessFile** object already exists and is created in write mode, truncate the file length to 0.

\- **OpenMode.APPEND(0o2000)**: Create the file in append mode. New data will be added to the end of the **RandomAccessFile** object.

\- **OpenMode.NONBLOCK(0o4000)**: If **path** points to a named pipe (also known as a FIFO), block special file, or character special file, perform non-blocking operations on the created file and in subsequent I/Os.

\- **OpenMode.DIR(0o200000)**: If **path** does not point to a directory, throw an exception. The write permission is not allowed.

\- **OpenMode.NOFOLLOW(0o400000)**: If **path** points to a symbolic link, throw an exception.

\- **OpenMode.SYNC(0o4010000)**: Create a **RandomAccessFile** instance in synchronous I/O mode.

 |
| options | [RandomAccessFileOptions](#randomaccessfileoptions12) | No | 

The options are as follows:

\- **start** (number): start position of the data to read in the file. This parameter is optional. By default, data is read from the current position.

\- **end** (number): end position of the data to read in the file. This parameter is optional. The default value is the end of the file.

This parameter takes effect only for file stream objects obtained by [getreadstream](#getreadstream12) and [getwritestream](#getwritestream12).

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [RandomAccessFile](#randomaccessfile10) | **RandomAccessFile** instance created. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

let filePath = pathDir + "/test.txt";
let randomAccessFile = fs.createRandomAccessFileSync(filePath, fs.OpenMode.CREATE | fs.OpenMode.READ\_WRITE,
  { start: 10, end: 100 });
randomAccessFile.close();

#### fs.createStream

createStream(path: string, mode: string): Promise<Stream>

Creates a stream based on a file path. This API uses a promise to return the result. To close the stream, use **close()** of [Stream](#stream).

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | Application sandbox path of the file. |
| mode | string | Yes | 
\- **r**: Open a file for reading. The file must exist.

\- **r+**: Open a file for both reading and writing. The file must exist.

\- **w**: Open a file for writing. If the file exists, clear its content. If the file does not exist, create a file.

\- **w+**: Open a file for both reading and writing. If the file exists, clear its content. If the file does not exist, create a file.

\- **a**: Open a file in append mode for writing at the end of the file. If the file does not exist, create a file. If the file exists, write data to the end of the file (the original content of the file is reserved).

\- **a+**: Open a file in append mode for reading or updating at the end of the file. If the file does not exist, create a file. If the file exists, write data to the end of the file (the original content of the file is reserved).

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[Stream](#stream)\> | Promise used to return the stream opened. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
fs.createStream(filePath, "a+").then((stream: fs.Stream) => {
  stream.closeSync();
  console.info("createStream succeed");
}).catch((err: BusinessError) => {
  console.error("createStream failed with error message: " + err.message + ", error code: " + err.code);
});

#### fs.createStream

createStream(path: string, mode: string, callback: AsyncCallback<Stream>): void

Creates a stream based on a file path. This API uses an asynchronous callback to return the result. To close the stream, use **close()** of [Stream](#stream).

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | Application sandbox path of the file. |
| mode | string | Yes | 
\- **r**: Open a file for reading. The file must exist.

\- **r+**: Open a file for both reading and writing. The file must exist.

\- **w**: Open a file for writing. If the file exists, clear its content. If the file does not exist, create a file.

\- **w+**: Open a file for both reading and writing. If the file exists, clear its content. If the file does not exist, create a file.

\- **a**: Open a file in append mode for writing at the end of the file. If the file does not exist, create a file. If the file exists, write data to the end of the file (the original content of the file is reserved).

\- **a+**: Open a file in append mode for reading or updating at the end of the file. If the file does not exist, create a file. If the file exists, write data to the end of the file (the original content of the file is reserved).

 |
| callback | AsyncCallback<[Stream](#stream)\> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
fs.createStream(filePath, "r+", (err: BusinessError, stream: fs.Stream) => {
  if (err) {
    console.error("create stream failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    stream.closeSync();
    console.info("createStream succeed");
  }
})

#### fs.createStreamSync

createStreamSync(path: string, mode: string): Stream

Creates a stream based on a file path. This API returns the result synchronously. To close the stream, use **close()** of [Stream](#stream).

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | Application sandbox path of the file. |
| mode | string | Yes | 
\- **r**: Open a file for reading. The file must exist.

\- **r+**: Open a file for both reading and writing. The file must exist.

\- **w**: Open a file for writing. If the file exists, clear its content. If the file does not exist, create a file.

\- **w+**: Open a file for both reading and writing. If the file exists, clear its content. If the file does not exist, create a file.

\- **a**: Open a file in append mode for writing at the end of the file. If the file does not exist, create a file. If the file exists, write data to the end of the file (the original content of the file is reserved).

\- **a+**: Open a file in append mode for reading or updating at the end of the file. If the file does not exist, create a file. If the file exists, write data to the end of the file (the original content of the file is reserved).

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [Stream](#stream) | Stream opened. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

let filePath = pathDir + "/test.txt";
let stream = fs.createStreamSync(filePath, "r+");
console.info("createStream succeed");
stream.closeSync();

#### fs.fdopenStream

fdopenStream(fd: number, mode: string): Promise<Stream>

Opens a stream based on an FD. This API uses a promise to return the result. To close the stream, use **close()** of [Stream](#stream).

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| fd | number | Yes | FD of the file. |
| mode | string | Yes | 
\- **r**: Open a file for reading. The file must exist.

\- **r+**: Open a file for both reading and writing. The file must exist.

\- **w**: Open a file for writing. If the file exists, clear its content. If the file does not exist, create a file.

\- **w+**: Open a file for both reading and writing. If the file exists, clear its content. If the file does not exist, create a file.

\- **a**: Open a file in append mode for writing at the end of the file. If the file does not exist, create a file. If the file exists, write data to the end of the file (the original content of the file is reserved).

\- **a+**: Open a file in append mode for reading or updating at the end of the file. If the file does not exist, create a file. If the file exists, write data to the end of the file (the original content of the file is reserved).

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[Stream](#stream)\> | Promise used to return the stream opened. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
let file = fs.openSync(filePath);
fs.fdopenStream(file.fd, "r+").then((stream: fs.Stream) => {
  console.info("openStream succeed");
  stream.closeSync();
}).catch((err: BusinessError) => {
  console.error("openStream failed with error message: " + err.message + ", error code: " + err.code);
  // If the file stream fails to be opened, the FD must be manually closed.
  fs.closeSync(file);
});

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/ARUvkbo9Q8OWfxd7OtNgaQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062319Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1FFBF7CE911C9F733BBA6CF204BD638C7210443E78541E99487BC98B23564E19)

When a file stream created with an FD is used, the lifecycle of the FD will be managed by the file stream object. When **close()** is called to close the file stream, the FD is also closed.

#### fs.fdopenStream

fdopenStream(fd: number, mode: string, callback: AsyncCallback<Stream>): void

Opens a stream based on an FD. This API uses an asynchronous callback to return the result. To close the stream, use **close()** of [Stream](#stream).

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| fd | number | Yes | FD of the file. |
| mode | string | Yes | 
\- **r**: Open a file for reading. The file must exist.

\- **r+**: Open a file for both reading and writing. The file must exist.

\- **w**: Open a file for writing. If the file exists, clear its content. If the file does not exist, create a file.

\- **w+**: Open a file for both reading and writing. If the file exists, clear its content. If the file does not exist, create a file.

\- **a**: Open a file in append mode for writing at the end of the file. If the file does not exist, create a file. If the file exists, write data to the end of the file (the original content of the file is reserved).

\- **a+**: Open a file in append mode for reading or updating at the end of the file. If the file does not exist, create a file. If the file exists, write data to the end of the file (the original content of the file is reserved).

 |
| callback | AsyncCallback<[Stream](#stream)\> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
let file = fs.openSync(filePath, fs.OpenMode.READ\_ONLY);
fs.fdopenStream(file.fd, "r+", (err: BusinessError, stream: fs.Stream) => {
  if (err) {
    console.error("fdopen stream failed with error message: " + err.message + ", error code: " + err.code);
    // If the file stream fails to be opened, the FD must be manually closed.
    fs.closeSync(file);
  } else {
    console.info("fdopen stream succeed");
    stream.closeSync();
  }
});

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/DEv1WPUmSHiHmMytR9EvzA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062319Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=040B0F72D70DC9AD5839DECAC65E414F7798E3B0E251D2ED70C0B4BE5D7491E9)

If a file stream is created with an FD, the lifecycle of the FD is also transferred to the file stream object. When **close()** is called to close the file stream, the FD is also closed.

#### fs.fdopenStreamSync

fdopenStreamSync(fd: number, mode: string): Stream

Opens a stream based on an FD. This API returns the result synchronously. To close the stream, use **close()** of [Stream](#stream).

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| fd | number | Yes | FD of the file. |
| mode | string | Yes | 
\- **r**: Open a file for reading. The file must exist.

\- **r+**: Open a file for both reading and writing. The file must exist.

\- **w**: Open a file for writing. If the file exists, clear its content. If the file does not exist, create a file.

\- **w+**: Open a file for both reading and writing. If the file exists, clear its content. If the file does not exist, create a file.

\- **a**: Open a file in append mode for writing at the end of the file. If the file does not exist, create a file. If the file exists, write data to the end of the file (the original content of the file is reserved).

\- **a+**: Open a file in append mode for reading or updating at the end of the file. If the file does not exist, create a file. If the file exists, write data to the end of the file (the original content of the file is reserved).

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [Stream](#stream) | Stream opened. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

let filePath = pathDir + "/test.txt";
let file = fs.openSync(filePath, fs.OpenMode.READ\_ONLY | fs.OpenMode.CREATE);
let stream = fs.fdopenStreamSync(file.fd, "r+");
stream.closeSync();

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/g82MPEYaSpqjXSO6hhygKw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062319Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=14899688D5AE80E521BBACFE2FCF0B43B79DB21C3819D69506214A47D91A9C26)

If a file stream is created with an FD, the lifecycle of the FD is also transferred to the file stream object. When **close()** is called to close the file stream, the FD is also closed.

#### fs.createReadStream12+

createReadStream(path: string, options?: ReadStreamOptions ): ReadStream

Creates a readable stream. This API returns the result synchronously.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | Path of the file. |
| options | [ReadStreamOptions](#readstreamoptions12) | No | 
The options are as follows:

\- **start** (number): start position of the data to read in the file. This parameter is optional. By default, data is read from the current position.

\- **end** (number): end position of the data to read in the file. This parameter is optional. The default value is the end of the file.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [ReadStream](#readstream12) | **ReadStream** instance obtained. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

**Example**

// Create a readable stream.
const rs = fs.createReadStream(\`${pathDir}/read.txt\`);
// Create a writeable stream.
const ws = fs.createWriteStream(\`${pathDir}/write.txt\`);
// Copy files in paused mode.
rs.on('readable', () => {
  const data = rs.read();
  if (!data) {
    return;
  }
  ws.write(data);
});

#### fs.createWriteStream12+

createWriteStream(path: string, options?: WriteStreamOptions): WriteStream

Creates a writeable stream. This API returns the result synchronously.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | Path of the file. |
| options | [WriteStreamOptions](#writestreamoptions12) | No | 
The options are as follows:

\- **start** (number): start position to write the data in the file. This parameter is optional. By default, data is written from the current position.

\- **mode** (number): [mode](#openmode) for creating the writeable stream. This parameter is optional. The default value is the write-only mode.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [WriteStream](#writestream12) | **WriteStream** instance obtained. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

**Example**

// Create a readable stream.
const rs = fs.createReadStream(\`${pathDir}/read.txt\`);
// Create a writeable stream.
const ws = fs.createWriteStream(\`${pathDir}/write.txt\`);
// Copy files in paused mode.
rs.on('readable', () => {
  const data = rs.read();
  if (!data) {
    return;
  }
  ws.write(data);
});

#### AtomicFile15+

AtomicFile is a class used to perform atomic read and write operations on files.

A temporary file is written and renamed to the original file location, which ensures file integrity. If the write operation fails, the temporary file is deleted without modifying the original file content.

You can call **finishWrite()** or **failWrite()** to write or roll back file content.

**System capability**: SystemCapability.FileManagement.File.FileIO

#### \[h2\]constructor15+

constructor(path: string)

Creates an **AtomicFile** class for a file in a specified path.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | Application sandbox path of the file. |

#### \[h2\]getBaseFile15+

getBaseFile(): File

Obtains the file object through the **AtomicFile** object.

The FD needs to be closed by calling **close()**.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Return value**

| Type | Description |
| :-- | :-- |
| [File](#file) | File object opened. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

import { common } from '@kit.AbilityKit';
import { fileIo as fs} from '@kit.CoreFileKit';

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let pathDir = context.filesDir;

try {
  let atomicFile = new fs.AtomicFile(\`${pathDir}/write.txt\`);
  let writeStream = atomicFile.startWrite();
  writeStream.write("hello, world", "utf-8", ()=> {
    atomicFile.finishWrite();
    let File = atomicFile.getBaseFile();
    console.info('AtomicFile getBaseFile File.fd is: ' + File.fd + ' path: ' + File.path + ' name: ' + File.name);
  })
} catch (err) {
  console.error(\`Failed to get baseFile. Code: ${err.code}, message: ${err.message}\`);
}

#### \[h2\]openRead15+

openRead(): ReadStream

Creates a **ReadStream** instance.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Return value**

| Type | Description |
| :-- | :-- |
| [ReadStream](#readstream12) | **ReadStream** instance obtained. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

import { common } from '@kit.AbilityKit';
import { fileIo as fs} from '@kit.CoreFileKit';

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let pathDir = context.filesDir;

try {
  let file = new fs.AtomicFile(\`${pathDir}/read.txt\`);
  let writeStream = file.startWrite();
  writeStream.write("hello, world", "utf-8", ()=> {
    file.finishWrite();
    setTimeout(()=>{
      let readStream = file.openRead();
      readStream.on('readable', () => {
        const data = readStream.read();
        if (!data) {
          console.error('AtomicFile read data is null.');
          return;
        }
        console.info('AtomicFile read data is: ' + data);
      });
    },1000);
  })
} catch (err) {
  console.error(\`Failed to AtomicFile. Code: ${err.code}, message: ${err.message}\`);
}

#### \[h2\]readFully15+

readFully(): ArrayBuffer

Reads all content of a file.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Return value**

| Type | Description |
| :-- | :-- |
| ArrayBuffer | Full content of a file. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

import { common } from '@kit.AbilityKit';
import { fileIo as fs} from '@kit.CoreFileKit';
import { util, buffer } from '@kit.ArkTS';

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let pathDir = context.filesDir;

try {
  let file = new fs.AtomicFile(\`${pathDir}/read.txt\`);
  let writeStream = file.startWrite();
  writeStream.write("hello, world", "utf-8", ()=> {
    file.finishWrite();
    setTimeout(()=>{
      let data = file.readFully();
      let decoder = util.TextDecoder.create('utf-8');
      let str = decoder.decodeToString(new Uint8Array(data));
      console.info('AtomicFile readFully str is: ' + str);
    },1000);
  })
} catch (err) {
  console.error(\`Failed to AtomicFile. Code: ${err.code}, message: ${err.message}\`);
}

#### \[h2\]startWrite15+

startWrite(): WriteStream

Starts to write new file data in the **WriteStream** object returned.

If the file does not exist, create a file.

Call **finishWrite()** if the write operation is successful; call **failWrite()** if the write operation fails.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Return value**

| Type | Description |
| :-- | :-- |
| [WriteStream](#writestream12) | **WriteStream** instance obtained. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

import { common } from '@kit.AbilityKit';
import { fileIo as fs} from '@kit.CoreFileKit';

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let pathDir = context.filesDir;

try {
  let file = new fs.AtomicFile(\`${pathDir}/write.txt\`);
  let writeStream = file.startWrite();
  writeStream.write("hello, world", "utf-8", ()=> {
    file.finishWrite();
    console.info('AtomicFile write finished!');
  })
} catch (err) {
  console.error(\`Failed to AtomicFile. Code: ${err.code}, message: ${err.message}\`);
}

#### \[h2\]finishWrite15+

finishWrite(): void

Finishes writing file data when the write operation is complete.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

import { common } from '@kit.AbilityKit';
import { fileIo as fs} from '@kit.CoreFileKit';

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let pathDir = context.filesDir;

try {
  let file = new fs.AtomicFile(\`${pathDir}/write.txt\`);
  let writeStream = file.startWrite();
  writeStream.write("hello, world", "utf-8", ()=> {
    file.finishWrite();
  })
} catch (err) {
  console.error(\`Failed to AtomicFile. Code: ${err.code}, message: ${err.message}\`);
}

#### \[h2\]failWrite15+

failWrite(): void

Rolls back the file after the file fails to be written.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

import { common } from '@kit.AbilityKit';
import { fileIo as fs} from '@kit.CoreFileKit';

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let pathDir = context.filesDir;

let file = new fs.AtomicFile(\`${pathDir}/write.txt\`);
try {
  let writeStream = file.startWrite();
  writeStream.write("hello, world", "utf-8", ()=> {
    console.info('AtomicFile write succeed!');
  })
} catch (err) {
  file.failWrite();
  console.error(\`Failed to AtomicFile. Code: ${err.code}, message: ${err.message}\`);
}

#### \[h2\]delete15+

delete(): void

Deletes the **AtomicFile** class, including the original files and temporary files.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

import { common } from '@kit.AbilityKit';
import { fileIo as fs} from '@kit.CoreFileKit';
import { util } from '@kit.ArkTS';

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let pathDir = context.filesDir;

try {
  let file = new fs.AtomicFile(\`${pathDir}/read.txt\`);
  let writeStream = file.startWrite();
  writeStream.write("hello, world", "utf-8", ()=> {
    file.finishWrite();
    setTimeout(()=>{
      let data = file.readFully();
      let decoder = util.TextDecoder.create('utf-8');
      let str = decoder.decodeToString(new Uint8Array(data));
      console.info('AtomicFile readFully str is: ' + str);
      file.delete();
    },1000);
  })
} catch (err) {
  console.error(\`Failed to AtomicFile. Code: ${err.code}, message: ${err.message}\`);
}

#### fs.createWatcher10+

createWatcher(path: string, events: number, listener: WatchEventListener): Watcher

Creates a **Watcher** object to listen for file or directory changes.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | Application sandbox path of the file or directory to observe. |
| events | number | Yes | 
Events to observe. Multiple events can be separated by a bitwise OR operator (|).

\- **0x1: IN\_ACCESS**: A file is accessed.

\- **0x2: IN\_MODIFY**: The file content is modified.

\- **0x4: IN\_ATTRIB**: The file metadata is modified.

\- **0x8: IN\_CLOSE\_WRITE**: A file is opened, written with data, and then closed.

\- **0x10: IN\_CLOSE\_NOWRITE**: A file or directory is opened and then closed without data written.

\- **0x20: IN\_OPEN**: A file or directory is opened.

\- **0x40: IN\_MOVED\_FROM**: A file in the observed directory is moved.

\- **0x80: IN\_MOVED\_TO**: A file is moved to the observed directory.

\- **0x100: IN\_CREATE**: A file or directory is created in the observed directory.

\- **0x200: IN\_DELETE**: A file or directory is deleted from the observed directory.

\- **0x400: IN\_DELETE\_SELF**: The observed directory is deleted. After the directory is deleted, the listening stops.

\- **0x800: IN\_MOVE\_SELF**: The observed file or directory is moved. After the file or directory is moved, the listening continues.

\- **0xfff: IN\_ALL\_EVENTS**: All events.

 |
| listener | [WatchEventListener](#watcheventlistener10) | Yes | Callback invoked when an observed event occurs. The callback will be invoked each time an observed event occurs. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Watcher](#watcher10) | **Watcher** object created. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

import { common } from '@kit.AbilityKit';
import { fileIo as fs, WatchEvent } from '@kit.CoreFileKit';

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let pathDir = context.filesDir;
let filePath = pathDir + "/test.txt";
let file = fs.openSync(filePath, fs.OpenMode.READ\_WRITE | fs.OpenMode.CREATE);
let watcher = fs.createWatcher(filePath, 0x2 | 0x10, (watchEvent: WatchEvent) => {
  if (watchEvent.event == 0x2) {
    console.info(watchEvent.fileName + 'was modified');
  } else if (watchEvent.event == 0x10) {
    console.info(watchEvent.fileName + 'was closed');
  }
});
watcher.start();
fs.writeSync(file.fd, 'test');
fs.closeSync(file);
watcher.stop();

#### WatchEventListener10+

(event: WatchEvent): void

Provides APIs for observing events.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | [WatchEvent](#watchevent10) | Yes | Event for the callback to invoke. |

#### WatchEvent10+

Defines the event to observe.

#### \[h2\]Properties

**System capability**: SystemCapability.FileManagement.File.FileIO

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| fileName | string | Yes | No | Sandbox path of the file to observe. The sandbox path contains the file name. |
| event | number | Yes | No | 
Events to observe. Multiple events can be separated by a bitwise OR operator (|).

\- **0x1: IN\_ACCESS**: A file is accessed.

\- **0x2: IN\_MODIFY**: The file content is modified.

\- **0x4: IN\_ATTRIB**: The file metadata is modified.

\- **0x8: IN\_CLOSE\_WRITE**: A file is opened, written with data, and then closed.

\- **0x10: IN\_CLOSE\_NOWRITE**: A file or directory is opened and then closed without data written.

\- **0x20: IN\_OPEN**: A file or directory is opened.

\- **0x40: IN\_MOVED\_FROM**: A file in the observed directory is moved.

\- **0x80: IN\_MOVED\_TO**: A file is moved to the observed directory.

\- **0x100: IN\_CREATE**: A file or directory is created in the observed directory.

\- **0x200: IN\_DELETE**: A file or directory is deleted from the observed directory.

\- **0x400: IN\_DELETE\_SELF**: The observed directory is deleted. After the directory is deleted, the listening stops.

\- **0x800: IN\_MOVE\_SELF**: The observed file or directory is moved. After the file or directory is moved, the listening continues.

\- **0xfff: IN\_ALL\_EVENTS**: All events.

 |
| cookie | number | Yes | No | 

Cookie bound with the event.

Currently, only the **IN\_MOVED\_FROM** and **IN\_MOVED\_TO** events are supported. The **IN\_MOVED\_FROM** and **IN\_MOVED\_TO** events of the same file have the same **cookie** value.

 |

#### Progress11+

Defines the copy progress information.

**System capability**: SystemCapability.FileManagement.File.FileIO

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| processedSize | number | Yes | No | Size of the copied data. |
| totalSize | number | Yes | No | Total size of the data to be copied. |

#### TaskSignal12+

Provides APIs for interrupting a copy task.

**System capability**: SystemCapability.FileManagement.File.FileIO

#### \[h2\]cancel12+

cancel(): void

Cancels a copy task.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo as fs } from '@kit.CoreFileKit';
import { fileUri } from '@kit.CoreFileKit';
import { common } from '@kit.AbilityKit';

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let pathDir = context.filesDir;

let srcDirPathLocal: string = pathDir + "/src";
let dstDirPathLocal: string = pathDir + "/dest";
let srcDirUriLocal: string = fileUri.getUriFromPath(srcDirPathLocal);
let dstDirUriLocal: string = fileUri.getUriFromPath(dstDirPathLocal);
let copySignal = new fs.TaskSignal;
let progressListener: fs.ProgressListener = (progress: fs.Progress) => {
  console.info(\`progressSize: ${progress.processedSize}, totalSize: ${progress.totalSize}\`);
  if (progress.processedSize / progress.totalSize > 0.5) {
    copySignal.cancel();
    console.info("copy cancel.");
  }
};
let options: fs.CopyOptions = {
  "progressListener" : progressListener,
  "copySignal" : copySignal,
}

try {
  fs.copy(srcDirUriLocal, dstDirUriLocal, options, (err: BusinessError) => {
    if (err) {
      console.error("copy fail, err: ", err.message);
      return;
    }
    console.info("copy success.");
  })
} catch (err) {
  console.error("copyFileWithCancel failed, err: ", err.message);
}

#### \[h2\]onCancel12+

onCancel(): Promise<string>

Subscribes to the event reported when a copy task is canceled.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<string> | Promise used to return the path of the last file copied. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

import { fileIo as fs } from '@kit.CoreFileKit';
import { TaskSignal } from '@kit.CoreFileKit';
let copySignal: fs.TaskSignal = new TaskSignal();
copySignal.onCancel();

#### CopyOptions11+

Defines the callback for listening for the copy progress.

**System capability**: SystemCapability.FileManagement.File.FileIO

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| progressListener | [ProgressListener](#progresslistener11) | No | Yes | Listener used to observe the copy progress. |
| copySignal | [TaskSignal](#tasksignal12) | No | Yes | Signal used to cancel a copy task. |

#### ProgressListener11+

Listener used to observe the copy progress.

**System capability**: SystemCapability.FileManagement.File.FileIO

| Type | Description |
| :-- | :-- |
| (progress: [Progress](#progress11)) => void | Listener used to observe the copy progress. |

**Example**

import { TaskSignal } from '@kit.CoreFileKit';
let copySignal: fs.TaskSignal = new TaskSignal();
let progressListener: fs.ProgressListener = (progress: fs.Progress) => {
  console.info(\`processedSize: ${progress.processedSize}, totalSize: ${progress.totalSize}\`);
};
let copyOption: fs.CopyOptions = {
  "progressListener" : progressListener,
  "copySignal" : copySignal,
}

#### Stat

Represents detailed file information. Before calling any API of the **Stat()** class, use [stat()](#fsstat) to create a **Stat** instance.

#### \[h2\]Properties

**System capability**: SystemCapability.FileManagement.File.FileIO

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| ino | bigint | Yes | No | File ID. Different files on the same device have different **ino**s. |
| mode | number | Yes | No | 
File permissions. The meaning of each bit is as follows:

Note: The following values are in octal format. The return values are in decimal format. You need to convert the values.

\- **0o400**: The user has the read permission on a regular file or a directory entry.

\- **0o200**: The user has the permission to write a regular file or create and delete a directory entry.

\- **0o100**: The user has the permission to execute a regular file or search for the specified path in a directory.

\- **0o040**: The user group has the read permission on a regular file or a directory entry.

\- **0o020**: The user group has the permission to write a regular file or create and delete a directory entry.

\- **0o010**: The user group has the permission to execute a regular file or search for the specified path in a directory.

\- **0o004**: Other users have the permission to read a regular file or read a directory entry.

\- **0o002**: Other users have the permission to write a regular file or create and delete a directory entry.

\- **0o001**: Other users have the permission to execute a regular file or search for the specified path in a directory.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| uid | number | Yes | No | ID of the file owner. |
| gid | number | Yes | No | ID of the user group of the file. |
| size | number | Yes | No | 

File size, in bytes. This parameter is valid only for regular files.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| atime | number | Yes | No | 

Time when the file was last accessed. The value is the number of seconds elapsed since 00:00:00 on January 1, 1970.

**Note**: Currently, user data partitions are mounted in **noatime** mode by default, and **atime** update is disabled.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| mtime | number | Yes | No | 

Time when the file content was last modified. The value is the number of seconds elapsed since 00:00:00 on January 1, 1970.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| ctime | number | Yes | No | Time when the file metadata was last modified. The value is the number of seconds elapsed since 00:00:00 on January 1, 1970. |
| atimeNs15+ | bigint | Yes | Yes | 

Time of the last access to the file. The value is the number of nanoseconds elapsed since 00:00:00 on January 1, 1970.

**Note**: Currently, user data partitions are mounted in **noatime** mode by default, and **atime** update is disabled.

 |
| mtimeNs15+ | bigint | Yes | Yes | Time of the last modification to the file. The value is the number of nanoseconds elapsed since 00:00:00 on January 1, 1970. |
| ctimeNs15+ | bigint | Yes | Yes | Time of the last status change of the file. The value is the number of nanoseconds elapsed since 00:00:00 on January 1, 1970. |
| location11+ | [LocationType](#locationtype11) | Yes | No | File location, which indicates whether the file is stored in a local device or in the cloud. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/pnFrChomTvqrq_Ame--JtQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062319Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DD4B8CD4B3F5E4E6B69E0A966B1A61C7F5C5E8ECBC51713E4BB92D9A25D8FFDC)

Some properties in **Stat** are only supported for common files. You can use the [isFile()](#isfile) API to check whether a file is a common file.

#### \[h2\]isBlockDevice

isBlockDevice(): boolean

Checks whether this file is a block special file. A block special file supports access by block only, and it is cached when accessed.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Whether the file is a block special file. The value **true** means the file is a block special file; the value **false** means the file is not a block special file. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

let filePath = pathDir + "/test.txt";
let isBLockDevice = fs.statSync(filePath).isBlockDevice();

#### \[h2\]isCharacterDevice

isCharacterDevice(): boolean

Checks whether this file is a character special file. A character special device supports random access, and it is not cached when accessed.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Whether the file is a character special device. The value **true** means the file is a character special device; the value **false** means the opposite. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

let filePath = pathDir + "/test.txt";
let isCharacterDevice = fs.statSync(filePath).isCharacterDevice();

#### \[h2\]isDirectory

isDirectory(): boolean

Checks whether this file is a directory.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Whether the file is a directory. The value **true** means the file is a directory; the value **false** means the opposite. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

let dirPath = pathDir + "/test";
let isDirectory = fs.statSync(dirPath).isDirectory();

#### \[h2\]isFIFO

isFIFO(): boolean

Checks whether this file is a named pipe (or FIFO). Named pipes are used for inter-process communication.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Whether the file is an FIFO. The value **true** means the file is an FIFO; the value **false** means the opposite. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

let filePath = pathDir + "/test.txt";
let isFIFO = fs.statSync(filePath).isFIFO();

#### \[h2\]isFile

isFile(): boolean

Checks whether this file is a regular file.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Whether the file is a regular file. The value **true** means that the file is a regular file; the value **false** means the opposite. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

let filePath = pathDir + "/test.txt";
let isFile = fs.statSync(filePath).isFile();

#### \[h2\]isSocket

isSocket(): boolean

Checks whether this file is a socket.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Whether the file is a socket. The value **true** means that the file is a socket; the value **false** means the opposite. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

let filePath = pathDir + "/test.txt";
let isSocket = fs.statSync(filePath).isSocket();

#### \[h2\]isSymbolicLink

isSymbolicLink(): boolean

Checks whether this file is a symbolic link.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Whether the file is a symbolic link. The value **true** means that the file is a symbolic link; the value **false** means the opposite. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

let filePath = pathDir + "/test.txt";
let isSymbolicLink = fs.statSync(filePath).isSymbolicLink();

#### Stream

Provides API for stream operations. Before calling any API of **Stream**, you need to create a **Stream** instance by using [fs.createStream](#fscreatestream) or [fs.fdopenStream](#fsfdopenstream).

#### \[h2\]close

close(): Promise<void>

Closes the file stream. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
let stream = fs.createStreamSync(filePath, "r+");
stream.close().then(() => {
  console.info("close fileStream succeed");
}).catch((err: BusinessError) => {
  console.error("close fileStream  failed with error message: " + err.message + ", error code: " + err.code);
});

#### \[h2\]close

close(callback: AsyncCallback<void>): void

Closes the file stream. This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback invoked immediately after the stream is closed. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
let stream = fs.createStreamSync(filePath, "r+");
stream.close((err: BusinessError) => {
  if (err) {
    console.error("close stream failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("close stream succeed");
  }
});

#### \[h2\]closeSync

closeSync(): void

Closes the file stream. This API returns the result synchronously.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

let filePath = pathDir + "/test.txt";
let stream = fs.createStreamSync(filePath, "r+");
stream.closeSync();

#### \[h2\]flush

flush(): Promise<void>

Flushes the file stream. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
let stream = fs.createStreamSync(filePath, "r+");
stream.flush().then(() => {
  console.info("flush succeed");
  stream.close();
}).catch((err: BusinessError) => {
  console.error("flush failed with error message: " + err.message + ", error code: " + err.code);
});

#### \[h2\]flush

flush(callback: AsyncCallback<void>): void

Flushes the file stream. This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
let stream = fs.createStreamSync(filePath, "r+");
stream.flush((err: BusinessError) => {
  if (err) {
    console.error("flush stream failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("flush succeed");
    stream.close();
  }
});

#### \[h2\]flushSync

flushSync(): void

Flushes the file stream. This API returns the result synchronously.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

let filePath = pathDir + "/test.txt";
let stream = fs.createStreamSync(filePath, "r+");
stream.flushSync();
stream.close();

#### \[h2\]write

write(buffer: ArrayBuffer | string, options?: WriteOptions): Promise<number>

Writes data to a stream file. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| buffer | ArrayBuffer | string | Yes | Data to write. It can be a string or data from a buffer. |
| options | [WriteOptions](#writeoptions11) | No | 
The options are as follows:

\- **length** (number): length of the data to write. The default value is the buffer length.

\- **offset** (number): start position to write the data in the file. This parameter is optional. By default, data is written from the current position.

\- **encoding** (string): format of the data to be encoded when the data is a string. The default value is **'utf-8'**, which is the only value supported.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the length of the data written. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo as fs, WriteOptions } from '@kit.CoreFileKit';
let filePath = pathDir + "/test.txt";
let stream = fs.createStreamSync(filePath, "r+");
let writeOption: WriteOptions = {
  offset: 5,
  length: 5,
  encoding: 'utf-8'
};
stream.write("hello, world", writeOption).then((number: number) => {
  console.info("write succeed and size is:" + number);
  stream.close();
}).catch((err: BusinessError) => {
  console.error("write failed with error message: " + err.message + ", error code: " + err.code);
});

#### \[h2\]write

write(buffer: ArrayBuffer | string, options?: WriteOptions, callback: AsyncCallback<number>): void

Writes data to a stream file. This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| buffer | ArrayBuffer | string | Yes | Data to write. It can be a string or data from a buffer. |
| options | [WriteOptions](#writeoptions11) | No | 
The options are as follows:

\- **length** (number): length of the data to write. This parameter is optional. The default value is the buffer length.

\- **offset** (number): start position to write the data in the file. This parameter is optional. By default, data is written from the current position.

\- **encoding** (string): format of the data to be encoded when the data is a string. The default value is **'utf-8'**, which is the only value supported.

 |
| callback | AsyncCallback<number> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo as fs, WriteOptions } from '@kit.CoreFileKit';
let filePath = pathDir + "/test.txt";
let stream = fs.createStreamSync(filePath, "r+");
let writeOption: WriteOptions = {
  offset: 5,
  length: 5,
  encoding: 'utf-8'
};
stream.write("hello, world", writeOption, (err: BusinessError, bytesWritten: number) => {
  if (err) {
    console.error("write stream failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    if (bytesWritten) {
      console.info("write succeed and size is:" + bytesWritten);
    }
  }
  stream.close();
});

#### \[h2\]writeSync

writeSync(buffer: ArrayBuffer | string, options?: WriteOptions): number

Writes data to a stream file. This API returns the result synchronously.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| buffer | ArrayBuffer | string | Yes | Data to write. It can be a string or data from a buffer. |
| options | [WriteOptions](#writeoptions11) | No | 
The options are as follows:

\- **length** (number): length of the data to write. This parameter is optional. The default value is the buffer length.

\- **offset** (number): start position to write the data in the file. This parameter is optional. By default, data is written from the current position.

\- **encoding** (string): format of the data to be encoded when the data is a string. The default value is **'utf-8'**, which is the only value supported.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| number | Length of the data written in the file. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

import { fileIo as fs, WriteOptions } from '@kit.CoreFileKit';
let filePath = pathDir + "/test.txt";
let stream = fs.createStreamSync(filePath,"r+");
let writeOption: WriteOptions = {
  offset: 5,
  length: 5,
  encoding: 'utf-8'
};
let num = stream.writeSync("hello, world", writeOption);
stream.close();

#### \[h2\]read

read(buffer: ArrayBuffer, options?: ReadOptions): Promise<number>

Reads data from a stream file. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| buffer | ArrayBuffer | Yes | Buffer used to store the file read. |
| options | [ReadOptions](#readoptions11) | No | 
The options are as follows:

\- **length** (number): length of the data to read. This parameter is optional. The default value is the buffer length.

\- **offset** (number): start position to read the data. This parameter is optional. By default, data is read from the current position.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the data read. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { buffer } from '@kit.ArkTS';
import { fileIo as fs, ReadOptions } from '@kit.CoreFileKit';
let filePath = pathDir + "/test.txt";
let stream = fs.createStreamSync(filePath, "r+");
let arrayBuffer = new ArrayBuffer(4096);
let readOption: ReadOptions = {
  offset: 5,
  length: 5
};
stream.read(arrayBuffer, readOption).then((readLen: number) => {
  console.info("read data succeed");
  let buf = buffer.from(arrayBuffer, 0, readLen);
  console.info(\`The content of file: ${buf.toString()}\`);
  stream.close();
}).catch((err: BusinessError) => {
  console.error("read data failed with error message: " + err.message + ", error code: " + err.code);
});

#### \[h2\]read

read(buffer: ArrayBuffer, options?: ReadOptions, callback: AsyncCallback<number>): void

Reads data from a stream file. This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| buffer | ArrayBuffer | Yes | Buffer used to store the file read. |
| options | [ReadOptions](#readoptions11) | No | 
The options are as follows:

\- **length** (number): length of the data to read. This parameter is optional. The default value is the buffer length.

\- **offset** (number): start position to read the data. This parameter is optional. By default, data is read from the current position.

 |
| callback | AsyncCallback<number> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { buffer } from '@kit.ArkTS';
import { fileIo as fs, ReadOptions } from '@kit.CoreFileKit';
let filePath = pathDir + "/test.txt";
let stream = fs.createStreamSync(filePath, "r+");
let arrayBuffer = new ArrayBuffer(4096);
let readOption: ReadOptions = {
  offset: 5,
  length: 5
};
stream.read(arrayBuffer, readOption, (err: BusinessError, readLen: number) => {
  if (err) {
    console.error("read stream failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("read data succeed");
    let buf = buffer.from(arrayBuffer, 0, readLen);
    console.info(\`The content of file: ${buf.toString()}\`);
    stream.close();
  }
});

#### \[h2\]readSync

readSync(buffer: ArrayBuffer, options?: ReadOptions): number

Reads data from a stream file. This API returns the result synchronously.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| buffer | ArrayBuffer | Yes | Buffer used to store the file read. |
| options | [ReadOptions](#readoptions11) | No | 
The options are as follows:

\- **length** (number): length of the data to read. This parameter is optional. The default value is the buffer length.

\- **offset** (number): start position to read the data. This parameter is optional. By default, data is read from the current position.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| number | Length of the data read. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

import { fileIo as fs, ReadOptions } from '@kit.CoreFileKit';
let filePath = pathDir + "/test.txt";
let stream = fs.createStreamSync(filePath, "r+");
let readOption: ReadOptions = {
  offset: 5,
  length: 5
};
let buf = new ArrayBuffer(4096);
let num = stream.readSync(buf, readOption);
stream.close();

#### File

Represents a **File** object opened by **open()**.

#### \[h2\]Properties

**System capability**: SystemCapability.FileManagement.File.FileIO

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| fd | number | Yes | No | 
FD of the file.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| path10+ | string | Yes | No | Path of the file. |
| name10+ | string | Yes | No | Name of the file. |

#### \[h2\]getParent11+

getParent(): string

Obtains the parent directory of this file object.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Return value**

| Type | Description |
| :-- | :-- |
| string | Parent directory obtained. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
let file = fs.openSync(filePath, fs.OpenMode.READ\_WRITE | fs.OpenMode.CREATE);
console.info('The parent path is: ' + file.getParent());
fs.closeSync(file);

#### \[h2\]lock

lock(exclusive?: boolean): Promise<void>

Applies an exclusive lock or a shared lock on this file in blocking mode. This API uses a promise to return the result.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| exclusive | boolean | No | 
Lock to apply.

The value **true** means an exclusive lock, and the value **false** (default) means a shared lock.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
let file = fs.openSync(filePath, fs.OpenMode.READ\_WRITE | fs.OpenMode.CREATE);
file.lock(true).then(() => {
  console.info("lock file succeed");
}).catch((err: BusinessError) => {
  console.error("lock file failed with error message: " + err.message + ", error code: " + err.code);
}).finally(() => {
  fs.closeSync(file);
});

#### \[h2\]lock

lock(exclusive?: boolean, callback: AsyncCallback<void>): void

Applies an exclusive lock or a shared lock on this file in blocking mode. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| exclusive | boolean | No | 
Lock to apply.

The value **true** means an exclusive lock, and the value **false** (default) means a shared lock.

 |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
let file = fs.openSync(filePath, fs.OpenMode.READ\_WRITE | fs.OpenMode.CREATE);
file.lock(true, (err: BusinessError) => {
  if (err) {
    console.error("lock file failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("lock file succeed");
  }
  fs.closeSync(file);
});

#### \[h2\]tryLock

tryLock(exclusive?: boolean): void

Applies an exclusive lock or a shared lock on this file in non-blocking mode.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| exclusive | boolean | No | 
Lock to apply.

The value **true** means an exclusive lock, and the value **false** (default) means a shared lock.

 |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

let filePath = pathDir + "/test.txt";
let file = fs.openSync(filePath, fs.OpenMode.READ\_WRITE | fs.OpenMode.CREATE);
file.tryLock(true);
console.info("lock file succeed");
fs.closeSync(file);

#### \[h2\]unlock

unlock(): void

Unlocks a file. This API returns the result synchronously.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

let filePath = pathDir + "/test.txt";
let file = fs.openSync(filePath, fs.OpenMode.READ\_WRITE | fs.OpenMode.CREATE);
file.tryLock(true);
file.unlock();
console.info("unlock file succeed");
fs.closeSync(file);

#### fs.DfsListeners12+

Provides APIs for listening for the distributed file system status.

**System capability**: SystemCapability.FileManagement.File.FileIO

#### \[h2\]onStatus12+

onStatus(networkId: string, status: number): void;

Called to return the specified status. Its parameters are passed in by [connectDfs](#fsconnectdfs12).

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| networkId | string | Yes | Network ID of the device. |
| status | number | Yes | 
Status code of the distributed file system. The status code is the error code returned by **onStatus** invoked by **connectDfs**. If the device is abnormal when **connectDfs()** is called, **onStatus** will be called to return the error code:

\- [13900046](../../error-codes/file-management-error-codes/document.md#section13900046-connection-interrupted-by-software): The connection is interrupted by software.

 |

#### RandomAccessFile10+

Provides APIs for randomly reading and writing a stream. Before invoking any API of **RandomAccessFile**, you need to use **createRandomAccessFile()** to create a **RandomAccessFile** instance synchronously or asynchronously.

#### \[h2\]Properties

**System capability**: SystemCapability.FileManagement.File.FileIO

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| fd | number | Yes | No | FD of the file. |
| filePointer | number | Yes | No | Offset pointer to the **RandomAccessFile** instance. |

#### \[h2\]setFilePointer10+

setFilePointer(filePointer:number): void

Sets the file offset pointer.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| filePointer | number | Yes | Offset pointer to the **RandomAccessFile** instance. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

let filePath = pathDir + "/test.txt";
let randomAccessFile = fs.createRandomAccessFileSync(filePath, fs.OpenMode.READ\_WRITE | fs.OpenMode.CREATE);
randomAccessFile.setFilePointer(1);
randomAccessFile.close();

#### \[h2\]close10+

close(): void

Closes the **RandomAccessFile** instance. This API returns the result synchronously.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

let filePath = pathDir + "/test.txt";
let randomAccessFile = fs.createRandomAccessFileSync(filePath, fs.OpenMode.READ\_WRITE | fs.OpenMode.CREATE);
randomAccessFile.close();

#### \[h2\]write10+

write(buffer: ArrayBuffer | string, options?: WriteOptions): Promise<number>

Writes data into a file. This API uses a promise to return the result.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| buffer | ArrayBuffer | string | Yes | Data to write. It can be a string or data from a buffer. |
| options | [WriteOptions](#writeoptions11) | No | 
The options are as follows:

\- **length** (number): length of the data to write. The default value is the buffer length.

\- **offset** (number): start position to write the data (it is determined by **filePointer** plus **offset**). This parameter is optional. By default, data is written from the **filePointer**.

\- **encoding** (string): format of the data to be encoded when the data is a string. The default value is **'utf-8'**, which is the only value supported.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the length of the data written. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo as fs, WriteOptions } from '@kit.CoreFileKit';
let filePath = pathDir + "/test.txt";
let file = fs.openSync(filePath, fs.OpenMode.CREATE | fs.OpenMode.READ\_WRITE);
let randomAccessFile = fs.createRandomAccessFileSync(file);
let bufferLength: number = 4096;
let writeOption: WriteOptions = {
  offset: 1,
  length: 5,
  encoding: 'utf-8'
};
let arrayBuffer = new ArrayBuffer(bufferLength);
randomAccessFile.write(arrayBuffer, writeOption).then((bytesWritten: number) => {
  console.info("randomAccessFile bytesWritten: " + bytesWritten);
}).catch((err: BusinessError) => {
  console.error("create randomAccessFile failed with error message: " + err.message + ", error code: " + err.code);
}).finally(() => {
  randomAccessFile.close();
  fs.closeSync(file);
});

#### \[h2\]write10+

write(buffer: ArrayBuffer | string, options?: WriteOptions, callback: AsyncCallback<number>): void

Writes data to a file. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| buffer | ArrayBuffer | string | Yes | Data to write. It can be a string or data from a buffer. |
| options | [WriteOptions](#writeoptions11) | No | 
The options are as follows:

\- **length** (number): length of the data to write. This parameter is optional. The default value is the buffer length.

\- **offset** (number): start position to write the data (it is determined by **filePointer** plus **offset**). This parameter is optional. By default, data is written from the **filePointer**.

\- **encoding** (string): format of the data to be encoded when the data is a string. The default value is **'utf-8'**, which is the only value supported.

 |
| callback | AsyncCallback<number> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo as fs, WriteOptions } from '@kit.CoreFileKit';
let filePath = pathDir + "/test.txt";
let file = fs.openSync(filePath, fs.OpenMode.CREATE | fs.OpenMode.READ\_WRITE);
let randomAccessFile = fs.createRandomAccessFileSync(file);
let bufferLength: number = 4096;
let writeOption: WriteOptions = {
  offset: 1,
  length: bufferLength,
  encoding: 'utf-8'
};
let arrayBuffer = new ArrayBuffer(bufferLength);
randomAccessFile.write(arrayBuffer, writeOption, (err: BusinessError, bytesWritten: number) => {
  if (err) {
    console.error("write failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    if (bytesWritten) {
      console.info("write succeed and size is:" + bytesWritten);
    }
  }
  randomAccessFile.close();
  fs.closeSync(file);
});

#### \[h2\]writeSync10+

writeSync(buffer: ArrayBuffer | string, options?: WriteOptions): number

Writes data to a file. This API returns the result synchronously.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| buffer | ArrayBuffer | string | Yes | Data to write. It can be a string or data from a buffer. |
| options | [WriteOptions](#writeoptions11) | No | 
The options are as follows:

\- **length** (number): length of the data to write. This parameter is optional. The default value is the buffer length.

\- **offset** (number): start position to write the data (it is determined by **filePointer** plus **offset**). This parameter is optional. By default, data is written from the **filePointer**.

\- **encoding** (string): format of the data to be encoded when the data is a string. The default value is **'utf-8'**, which is the only value supported.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| number | Length of the data written in the file. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

import { fileIo as fs, WriteOptions } from '@kit.CoreFileKit';
let filePath = pathDir + "/test.txt";
let randomAccessFile = fs.createRandomAccessFileSync(filePath, fs.OpenMode.CREATE | fs.OpenMode.READ\_WRITE);
let writeOption: WriteOptions = {
  offset: 5,
  length: 5,
  encoding: 'utf-8'
};
let bytesWritten = randomAccessFile.writeSync("hello, world", writeOption);
randomAccessFile.close();

#### \[h2\]read10+

read(buffer: ArrayBuffer, options?: ReadOptions): Promise<number>

Reads data from a file. This API uses a promise to return the result.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| buffer | ArrayBuffer | Yes | Buffer used to store the file read. |
| options | [ReadOptions](#readoptions11) | No | 
The options are as follows:

\- **length** (number): length of the data to read. This parameter is optional. The default value is the buffer length.

\- **offset** (number): start position to read the data (it is determined by **filePointer** plus **offset**). This parameter is optional. By default, data is read from the **filePointer**.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the data read. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo as fs, ReadOptions } from '@kit.CoreFileKit';
let filePath = pathDir + "/test.txt";
let file = fs.openSync(filePath, fs.OpenMode.CREATE | fs.OpenMode.READ\_WRITE);
let randomAccessFile = fs.createRandomAccessFileSync(file);
let bufferLength: number = 4096;
let readOption: ReadOptions = {
  offset: 1,
  length: 5
};
let arrayBuffer = new ArrayBuffer(bufferLength);
randomAccessFile.read(arrayBuffer, readOption).then((readLength: number) => {
  console.info("randomAccessFile readLength: " + readLength);
}).catch((err: BusinessError) => {
  console.error("create randomAccessFile failed with error message: " + err.message + ", error code: " + err.code);
}).finally(() => {
  randomAccessFile.close();
  fs.closeSync(file);
});

#### \[h2\]read10+

read(buffer: ArrayBuffer, options?: ReadOptions, callback: AsyncCallback<number>): void

Reads data from a file. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| buffer | ArrayBuffer | Yes | Buffer used to store the file read. |
| options | [ReadOptions](#readoptions11) | No | 
The options are as follows:

\- **length** (number): length of the data to read. This parameter is optional. The default value is the buffer length.

\- **offset** (number): start position to read the data (it is determined by **filePointer** plus **offset**). This parameter is optional. By default, data is read from the **filePointer**.

 |
| callback | AsyncCallback<number> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo as fs, ReadOptions } from '@kit.CoreFileKit';
let filePath = pathDir + "/test.txt";
let file = fs.openSync(filePath, fs.OpenMode.CREATE | fs.OpenMode.READ\_WRITE);
let randomAccessFile = fs.createRandomAccessFileSync(file);
let length: number = 20;
let readOption: ReadOptions = {
  offset: 1,
  length: 5
};
let arrayBuffer = new ArrayBuffer(length);
randomAccessFile.read(arrayBuffer, readOption, (err: BusinessError, readLength: number) => {
  if (err) {
    console.error("read failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    if (readLength) {
      console.info("read succeed and size is:" + readLength);
    }
  }
  randomAccessFile.close();
  fs.closeSync(file);
});

#### \[h2\]readSync10+

readSync(buffer: ArrayBuffer, options?: ReadOptions): number

Reads data from a file. This API returns the result synchronously.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| buffer | ArrayBuffer | Yes | Buffer used to store the file read. |
| options | [ReadOptions](#readoptions11) | No | 
The options are as follows:

\- **length** (number): length of the data to read. This parameter is optional. The default value is the buffer length.

\- **offset** (number): start position to read the data (it is determined by **filePointer** plus **offset**). This parameter is optional. By default, data is read from the **filePointer**.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| number | Length of the data read. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

let filePath = pathDir + "/test.txt";
let file = fs.openSync(filePath, fs.OpenMode.CREATE | fs.OpenMode.READ\_WRITE);
let randomAccessFile = fs.createRandomAccessFileSync(file);
let length: number = 4096;
let arrayBuffer = new ArrayBuffer(length);
let readLength = randomAccessFile.readSync(arrayBuffer);
randomAccessFile.close();
fs.closeSync(file);

#### \[h2\]getReadStream12+

getReadStream(): ReadStream

Obtains a **ReadStream** instance of this **RandomAccessFile**.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Return value**

| Type | Description |
| :-- | :-- |
| [ReadStream](#readstream12) | **ReadStream** instance obtained. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

**Example**

const filePath = pathDir + "/test.txt";
const randomAccessFile = fs.createRandomAccessFileSync(filePath, fs.OpenMode.CREATE | fs.OpenMode.READ\_WRITE);
const rs = randomAccessFile.getReadStream();
rs.close();
randomAccessFile.close();

#### \[h2\]getWriteStream12+

getWriteStream(): WriteStream

Obtains a **WriteStream** instance of this **RandomAccessFile**.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Return value**

| Type | Description |
| :-- | :-- |
| [WriteStream](#writestream12) | **WriteStream** instance obtained. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

**Example**

const filePath = pathDir + "/test.txt";
const randomAccessFile = fs.createRandomAccessFileSync(filePath, fs.OpenMode.CREATE | fs.OpenMode.READ\_WRITE);
const ws = randomAccessFile.getWriteStream();
ws.close();
randomAccessFile.close();

#### Watcher10+

Provides APIs for observing the changes of files or directories. Before using the APIs of **Watcher**, call **createWatcher()** to create a **Watcher** object.

#### \[h2\]start10+

start(): void

Starts listening.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

let filePath = pathDir + "/test.txt";
let watcher = fs.createWatcher(filePath, 0xfff, () => {});
watcher.start();
watcher.stop();

#### \[h2\]stop10+

stop(): void

Stops listening and removes the **Watcher** object.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

let filePath = pathDir + "/test.txt";
let watcher = fs.createWatcher(filePath, 0xfff, () => {});
watcher.start();
watcher.stop();

#### OpenMode

Defines the constants of the **mode** parameter used in **open()**. It specifies the mode for opening a file.

**System capability**: SystemCapability.FileManagement.File.FileIO

| Name | Type | Value | Description |
| :-- | :-- | :-- | :-- |
| READ\_ONLY | number | 0o0 | 
Open the file in read-only mode.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| WRITE\_ONLY | number | 0o1 | 

Open the file in write-only mode.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| READ\_WRITE | number | 0o2 | 

Open the file in read/write mode.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| CREATE | number | 0o100 | 

Create a file if the specified file does not exist.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| TRUNC | number | 0o1000 | 

If the file exists and is opened in write-only or read/write mode, truncate the file length to 0.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| APPEND | number | 0o2000 | 

Open the file in append mode. New data will be written to the end of the file.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| NONBLOCK | number | 0o4000 | If **path** points to a named pipe (FIFO), block special file, or character special file, perform non-blocking operations on the open file and in subsequent I/Os. |
| DIR | number | 0o200000 | If **path** does not point to a directory, throw an exception. |
| NOFOLLOW | number | 0o400000 | If **path** points to a symbolic link, throw an exception. |
| SYNC | number | 0o4010000 | Open the file in synchronous I/O mode. |

#### Filter10+

Defines the file filtering configuration used by **listFile()**.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.FileManagement.File.FileIO

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| suffix | Array<string> | No | Yes | Locate files that fully match the specified file name extensions, which are of the OR relationship. |
| displayName | Array<string> | No | Yes | Locate files that fuzzy match the specified file names, which are of the OR relationship. Currently, only the wildcard \* is supported. |
| mimeType | Array<string> | No | Yes | Locate files that fully match the specified MIME types, which are of the OR relationship. This parameter is reserved. |
| fileSizeOver | number | No | Yes | Locate files that are greater than the specified size. |
| lastModifiedAfter | number | No | Yes | Locate files whose last modification time is the same or later than the specified time. |
| excludeMedia | boolean | No | Yes | 
Whether to exclude the files already in **Media**.

The value **true** means to exclude the files already in **Media**; the value **false** means not to exclude the files already in **Media**.

 |

#### ConflictFiles10+

Defines conflicting file information used in **copyDir()** or **moveDir()**.

**System capability**: SystemCapability.FileManagement.File.FileIO

| Name | Type | Description |
| :-- | :-- | :-- |
| srcFile | string | Path of the source file. |
| destFile | string | Path of the destination file. |

#### Options11+

Defines the options used in **readLines()**.

**System capability**: SystemCapability.FileManagement.File.FileIO

| Name | Type | Description |
| :-- | :-- | :-- |
| encoding | string | File encoding format. It is optional. |

#### WhenceType11+

Enumerates the types of the relative offset position used in **lseek()**.

**System capability**: SystemCapability.FileManagement.File.FileIO

| Name | Value | Description |
| :-- | :-- | :-- |
| SEEK\_SET | 0 | Beginning of the file. |
| SEEK\_CUR | 1 | Current offset position. |
| SEEK\_END | 2 | End of the file. |

#### LocationType11+

Enumerates the file locations.

**System capability**: SystemCapability.FileManagement.File.FileIO

| Name | Value | Description |
| :-- | :-- | :-- |
| LOCAL | 1 | The file is stored in a local device. |
| CLOUD | 2 | The file is stored in the cloud. |

#### AccessModeType12+

Enumerates the access modes to verify. If this parameter is left blank, the system checks whether the file exists.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.FileManagement.File.FileIO

| Name | Value | Description |
| :-- | :-- | :-- |
| EXIST | 0 | Whether the file exists. |
| WRITE | 2 | Verify the write permission on the file. |
| READ | 4 | Verify the read permission on the file. |
| READ\_WRITE | 6 | Verify the read/write permission on the file. |

#### AccessFlagType12+

Enumerates the locations of the file to verify.

**System capability**: SystemCapability.FileManagement.File.FileIO

| Name | Value | Description |
| :-- | :-- | :-- |
| LOCAL | 0 | The file is stored locally. |

#### ReadOptions11+

Defines the options used in **read()**.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.FileManagement.File.FileIO

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| offset | number | No | Yes | Start position of the file to read (current **filePointer** plus **offset**), in bytes. This parameter is optional. By default, data is read from the **filePointer**. |
| length | number | No | Yes | Length of the data to read, in bytes. This parameter is optional. The default value is the buffer length. |

#### ReadTextOptions11+

Defines the options used in **readText()**. It inherits from [ReadOptions](#readoptions11).

**System capability**: SystemCapability.FileManagement.File.FileIO

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| offset | number | No | Yes | Start position of the file to read, in bytes. This parameter is optional. By default, data is read from the current position. |
| length | number | No | Yes | Length of the data to read, in bytes. This parameter is optional. The default value is the file length. |
| encoding | string | No | Yes | 
Format of the data to be encoded. This parameter is valid only when the data type is string. The default value is **'utf-8'**, which is the only value supported.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |

#### WriteOptions11+

Defines the options used in **write()**. It inherits from [Options](#options11).

**System capability**: SystemCapability.FileManagement.File.FileIO

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| offset | number | No | Yes | 
Start position of the file to write (current **filePointer** plus **offset**), in bytes. This parameter is optional. By default, data is written from the **filePointer**.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| length | number | No | Yes | 

Length of the data to write, in bytes. This parameter is optional. The default value is the buffer length.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| encoding | string | No | Yes | Format of the data to be encoded. This parameter is valid only when the data type is string. The default value is **'utf-8'**, which is the only value supported. |

#### ListFileOptions11+

Defines the options used in **listFile()**.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.FileManagement.File.FileIO

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| recursion | boolean | No | Yes | Whether to list all files in the subdirectories recursively. This parameter is optional. The default value is **false**. If **recursion** is **false**, the names of files and directories that meet the filtering requirements in the current directory are returned. If **recursion** is **true**, relative paths (starting with /) of all files that meet the specified conditions in the current directory are returned. |
| listNum | number | No | Yes | Number of file names to list. This parameter is optional. The default value is **0**, which means to list all files. |
| filter | [Filter](#filter10) | No | Yes | File filtering configuration. This parameter is optional. It specifies the file filtering conditions. |

#### ReadStream12+

Defines a readable stream. You need to use [fs.createReadStream](#fscreatereadstream12) to create a **ReadStream** instance, which is inherited from [stream.Readable](../../../arkts/arkts-apis/ohos-util-stream-stream-base-class/document.md#readable).

The data obtained by **ReadStream** is a decoded string. Currently, only the UTF-8 format is supported.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| bytesRead | number | Yes | No | Number of bytes read by the readable stream. |
| path | string | Yes | No | Path of the file corresponding to the readable stream. |

#### \[h2\]seek12+

seek(offset: number, whence?: WhenceType): number

Adjusts the position of the readable stream offset pointer.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| offset | number | Yes | Relative offset, in bytes. |
| whence | [WhenceType](#whencetype11) | No | Where to start the offset. The default value is **SEEK\_SET**, which indicates the beginning of the file. |

**Return value**

| Type | Description |
| :-- | :-- |
| number | Position of the current offset pointer (offset relative to the file header, in bytes). |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

**Example**

const filePath = pathDir + "/test.txt";
const rs = fs.createReadStream(filePath);
const curOff = rs.seek(5, fs.WhenceType.SEEK\_SET);
console.info(\`current offset is ${curOff}\`);
rs.close();

#### \[h2\]close12+

close(): void

Closes this readable stream.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

const filePath = pathDir + "/test.txt";
const rs = fs.createReadStream(filePath);
rs.close();

#### WriteStream12+

Defines a writeable stream. You need to use [fs.createWriteStream](#fscreatewritestream12) to create a **WriteStream** instance, which is inherited from [stream.Writable](../../../arkts/arkts-apis/ohos-util-stream-stream-base-class/document.md#writable).

#### \[h2\]Properties

**System capability**: SystemCapability.FileManagement.File.FileIO

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| bytesWritten | number | Yes | No | Number of bytes written to the writable stream. |
| path | string | Yes | No | Path of the file corresponding to the writeable stream. |

#### \[h2\]seek12+

seek(offset: number, whence?: WhenceType): number;

Adjusts the position of the writeable stream offset pointer.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| offset | number | Yes | Relative offset, in bytes. |
| whence | [WhenceType](#whencetype11) | No | Where to start the offset. The default value is **SEEK\_SET**, which indicates the beginning of the file. |

**Return value**

| Type | Description |
| :-- | :-- |
| number | Position of the current offset pointer (offset relative to the file header, in bytes). |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

**Example**

const filePath = pathDir + "/test.txt";
const ws = fs.createWriteStream(filePath);
const curOff = ws.seek(5, fs.WhenceType.SEEK\_SET);
console.info(\`current offset is ${curOff}\`);
ws.close();

#### \[h2\]close12+

close(): void

Closes this writeable stream.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

**Example**

const filePath = pathDir + "/test.txt";
const ws = fs.createWriteStream(filePath);
ws.close();

#### RandomAccessFileOptions12+

Defines the options used in **createRandomAccessFile()**.

**System capability**: SystemCapability.FileManagement.File.FileIO

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| start | number | No | Yes | Start position to read the data, in bytes. This parameter is optional. By default, data is read from the current position. |
| end | number | No | Yes | End position to read the data, in bytes. This parameter is optional. The default value is the end of the file. |

#### ReadStreamOptions12+

Defines the options used in **createReadStream()**.

**System capability**: SystemCapability.FileManagement.File.FileIO

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| start | number | No | Yes | Start position to read the data, in bytes. This parameter is optional. By default, data is read from the current position. |
| end | number | No | Yes | End position to read the data, in bytes. This parameter is optional. The default value is the end of the file. |

#### WriteStreamOptions12+

Defines the options used in **createWriteStream()**.

**System capability**: SystemCapability.FileManagement.File.FileIO

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| start | number | No | Yes | Start position to write the data, in bytes. This parameter is optional. By default, data is written from the current position. |
| mode | number | No | Yes | 
[Option](#openmode) for creating the writeable stream. You must specify one of the following options.

\- **OpenMode.READ\_ONLY(0o0)**: read-only, which is the default value.

\- **OpenMode.WRITE\_ONLY(0o1)**: write-only.

\- **OpenMode.READ\_WRITE(0o2)**: read/write.

You can also specify the following options, separated by a bitwise OR operator (|). By default, no additional options are given.

\- **OpenMode.CREATE(0o100)**: If the file does not exist, create it.

\- **OpenMode.TRUNC(0o1000)**: If the file exists and is opened in write mode, truncate the file length to 0.

\- **OpenMode.APPEND(0o2000)**: Open the file in append mode. New data will be added to the end of the file.

\- **OpenMode.NONBLOCK(0o4000)**: If **path** points to a named pipe (also known as a FIFO), block special file, or character special file, perform non-blocking operations on the opened file and in subsequent I/Os.

\- **OpenMode.DIR(0o200000)**: If **path** does not point to a directory, throw an exception. The write permission is not allowed.

\- **OpenMode.NOFOLLOW(0o400000)**: If **path** points to a symbolic link, throw an exception.

\- **OpenMode.SYNC(0o4010000)**: Open the file in synchronous I/O mode.

 |
