# fileGuard (Hierarchical File Management)

The fileGuard service allows mobile device management ([MDM](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/mdm-kit)) apps to identify enterprise key information asset (KIA) files and prevent their unauthorized outflow, ensuring enterprise-level data security. The service provides functions including scanning all directories for files, identifying KIA files, and preventing these files from being transmitted over the network to untrusted segments.

This service is available only for MDM apps that have obtained the service permission.

**Start version**: 4.0.0(10)

#### Module Import

import { fileGuard } from '@kit.EnterpriseDataGuardKit';

#### CommonDirScanType

Enumerates types of common directories that can be scanned.

**System capability**: SystemCapability.PCService.FileGuard

**Start version**: 4.0.0(10)

| 
Enumeration

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

MEDIA\_ONLY

 | 

0

 | 

Media library directory.

 |
| 

MEDIA\_AND\_SANDBOX

 | 

1

 | 

Media library directory and sandbox directory.

 |

#### SecurityLevel

Enumerates file security levels.

**System capability**: SystemCapability.PCService.FileGuard

**Start version**: 4.0.0(10)

| 
Enumeration

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

DEFAULT

 | 

\-1

 | 

File security level not effective.

**Start version**: 5.1.1(19)

 |
| 

EXTERNAL

 | 

0

 | 

Public.

 |
| 

INTERNAL

 | 

1

 | 

Internal.

 |
| 

SECRET

 | 

2

 | 

Secret.

 |
| 

CONFIDENTIAL

 | 

3

 | 

Confidential.

 |
| 

TOP\_SECRET

 | 

4

 | 

Top secret.

 |

#### FilePathInfo

Defines file path information.

**System capability**: SystemCapability.PCService.FileGuard

**Start version**: 4.0.0(10)

| 
Parameter

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

absolutePath

 | 

string

 | 

No

 | 

No

 | 

Absolute file path.

 |
| 

uri

 | 

string

 | 

No

 | 

No

 | 

File URI.

 |

#### FileTagInfo

Defines file tag information.

**System capability**: SystemCapability.PCService.FileGuard

**Start version**: 4.0.0(10)

| 
Parameter

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

securityLevel

 | 

number

 | 

No

 | 

No

 | 

Security level of a file. For details, please refer to [SecurityLevel](#section36136612415).

 |
| 

tag

 | 

string

 | 

No

 | 

No

 | 

File tag information.

 |

#### ScanFileCallback

Provides the callback class of the scanning result.

**System capability**: SystemCapability.PCService.FileGuard

**Start version**: 4.0.0(10)

#### \[h2\]onReceiveFileList

onReceiveFileList(files: Array<string>): void

Defines the callback function of the file directory scanning result.

**System capability**: SystemCapability.PCService.FileGuard

**Start version**: 4.0.0(10)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

files

 | 

Array<string>

 | 

Yes

 | 

List of absolute paths of files to be scanned.

 |

**Example**:

let onReceiveFileList: (files: string\[\]) => void = (files: Array<string>) => {
  files.forEach((value: string, index: number) => {
    console.info(\`Succeeded in getting file: ${value}.\`);
  })
};

#### \[h2\]onTaskCompleted

onTaskCompleted(count: number): void

Callback function triggered when directory scanning is complete.

**System capability**: SystemCapability.PCService.FileGuard

**Start version**: 4.0.0(10)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

count

 | 

number

 | 

Yes

 | 

Number of files that are scanned.

 |

**Example**:

let onTaskCompleted: (count: number) => void = (count: number) => {
  console.info(\`Succeeded in getting count: ${count}.\`);
};

#### FileGuard

Provides APIs for hierarchical file management and control, including scanning file directories, setting file attributes, and delivering file control policies.

**System capability**: SystemCapability.PCService.FileGuard

**Start version**: 4.0.0(10)

#### \[h2\]constructor

constructor()

Creates a **FileGuard** object.

**System capability**: SystemCapability.PCService.FileGuard

**Start version**: 4.0.0(10)

**Example**:

let guard: fileGuard.FileGuard = new fileGuard.FileGuard();

#### \[h2\]startFileScanTask

startFileScanTask(type: CommonDirScanType, callback: ScanFileCallback, batchNum?: number): void

Starts a file scanning task for a common directory.

**Required permission**: ohos.permission.FILE\_GUARD\_MANAGER

**System capability**: SystemCapability.PCService.FileGuard

**Start version**: 4.0.0(10)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

[CommonDirScanType](#section1753862116813)

 | 

Yes

 | 

Common directory to scan. The options are **MEDIA\_ONLY** and **MEDIA\_AND\_SANDBOX**.

 |
| 

callback

 | 

[ScanFileCallback](#section1747318273273)

 | 

Yes

 | 

Callback used to return the file list and scanning completion notification.

 |
| 

batchNum

 | 

number

 | 

No

 | 

Maximum number of files returned by the callback function in each scan batch. The value ranges from 1 to 200. Any out-of-range value is invalid. By default, 100 files are returned in each scan batch, until the scanning of all files is complete.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

201

 | 

Permission denied.

 |
| 

401

 | 

The parameter check failed.

 |

**Example**:

let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
let onReceiveFileList: (files: string\[\]) => void = (files: Array<string>) => {
  console.info(\`Succeeded in getting number of files obtained in each callback: ${files.length}.\`);
  files.forEach((value: string, index: number) => {
    console.info(\`Succeeded in getting file: ${value}.\`);
  })
};
let onCompleteScanTask: (count: number) => void = (count: number) => {
  console.info(\`Succeeded in getting count: ${count}.\`);
};
let scanFileCallback: fileGuard.ScanFileCallback = {
  onReceiveFileList: onReceiveFileList,
  onTaskCompleted: onCompleteScanTask
};
guard.startFileScanTask(fileGuard.CommonDirScanType.MEDIA\_ONLY, scanFileCallback);

#### \[h2\]startFileScanTask

startFileScanTask(path: string, callback: ScanFileCallback, batchNum?: number): void

Starts a file scanning task for a specified directory under the common directory.

**Required permission**: ohos.permission.FILE\_GUARD\_MANAGER

**System capability**: SystemCapability.PCService.FileGuard

**Start version**: 4.0.0(10)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

path

 | 

string

 | 

Yes

 | 

Subset of directories in the [default path range](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/dataguard-introduction#li1475101851010).

 |
| 

callback

 | 

[ScanFileCallback](#section1747318273273)

 | 

Yes

 | 

Callback used to return the file list and scanning completion notification.

 |
| 

batchNum

 | 

number

 | 

No

 | 

Maximum number of files returned by the callback function in each scan batch. The value ranges from 1 to 200. Any out-of-range value is invalid. By default, 100 files are returned in each scan batch, until the scanning of all files is complete.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

201

 | 

Permission denied.

 |
| 

401

 | 

The parameter check failed.

 |

**Example**:

let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
let path: string = '/data/service/el2/test';
let onReceiveFileList: (files: string\[\]) => void = (files: Array<string>) => {
  console.info(\`Succeeded in getting number of files obtained in each callback: ${files.length}.\`);
  files.forEach((value: string, index: number) => {
    console.info(\`Succeeded in getting file: ${value}.\`);
  })
};
let onCompleteScanTask: (count: number) => void = (count: number) => {
  console.info(\`Succeeded in getting count: ${count}.\`);
};
let scanFileCallback: fileGuard.ScanFileCallback = {
  onReceiveFileList: onReceiveFileList,
  onTaskCompleted: onCompleteScanTask
};
guard.startFileScanTask(path, scanFileCallback);

#### \[h2\]openFile

openFile(path: string, callback: AsyncCallback<number>): void

Opens a file. This API returns the result asynchronously through a callback.

**Required permission**: ohos.permission.FILE\_GUARD\_MANAGER

**System capability**: SystemCapability.PCService.FileGuard

**Start version**: 4.0.0(10)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

path

 | 

string

 | 

Yes

 | 

Subset of absolute paths in the [default path range](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/dataguard-introduction#li1475101851010).

 |
| 

callback

 | 

AsyncCallback<number>

 | 

Yes

 | 

Callback function. If the operation is successful, **err** is **undefined** and **data** is the obtained file descriptor (FD); otherwise, **err** is an error object.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

201

 | 

Permission denied.

 |
| 

401

 | 

The parameter check failed.

 |

**Example**:

import { BusinessError } from '@kit.BasicServicesKit';

let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
let path: string = '/data/service/el2/test/test.txt';
guard.openFile(path, (err: BusinessError, fd: number) => {
  if (err) {
    console.error(\`Failed to open file. Code: ${err.code}, message: ${err.message}.\`);
    return;
  }
  console.info(\`Succeeded in opening file. path: ${path}, fd: ${fd}.\`);
});

#### \[h2\]openFile

openFile(path: string): Promise<number>

Opens a file. This API returns the result asynchronously through a promise.

**Required permission**: ohos.permission.FILE\_GUARD\_MANAGER

**System capability**: SystemCapability.PCService.FileGuard

**Start version**: 4.0.0(10)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

path

 | 

string

 | 

Yes

 | 

Subset of absolute paths in the [default path range](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/dataguard-introduction#li1475101851010).

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<number>

 | 

Promise used to return the FD of the file opened.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

201

 | 

Permission denied.

 |
| 

401

 | 

The parameter check failed.

 |

**Example**:

import { BusinessError } from '@kit.BasicServicesKit';

let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
let path: string = '/data/service/el2/test/test.txt';
guard.openFile(path).then((fd: number) => {
  console.info(\`Succeeded in opening file. path: ${path}, fd: ${fd}.\`);
}).catch((err: BusinessError) => {
  console.error(\`Failed to open file. Code: ${err.code}, message: ${err.message}.\`);
});

#### \[h2\]openFileWrite

openFileWrite(path: string, callback: AsyncCallback<number>): void

Opens a file in write-only mode. This API returns the result through a callback.

**Required permission**: ohos.permission.FILE\_GUARD\_MANAGER

**System capability**: SystemCapability.PCService.FileGuard

**Start version**: 5.1.1(19)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

path

 | 

string

 | 

Yes

 | 

Subset of absolute paths in the [personal directory of a user](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/dataguard-introduction#li61091691019).

 |
| 

callback

 | 

AsyncCallback<number>

 | 

Yes

 | 

Callback function. If the operation is successful, **err** is **undefined** and **data** is the obtained file descriptor (FD); otherwise, **err** is an error object.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

201

 | 

Permission denied.

 |
| 

401

 | 

Parameter error. Possible causes:

1\. Mandatory parameters are left unspecified.

2\. Incorrect parameter types.

3\. Parameter verification failed.

 |

**Example**:

import { BusinessError } from '@kit.BasicServicesKit';

let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
let path: string = '/data/service/el2/100/hmdfs/account/files/Docs/Documents/test.txt';
guard.openFileWrite(path, (err: BusinessError, fd: number) => {
  if (err) {
    console.error(\`Failed to open file in write-only mode. Code: ${err.code}, message: ${err.message}.\`);
    return;
  }
  console.info(\`Succeeded in opening file in write-only mode. path: ${path}, fd: ${fd}.\`);
});

#### \[h2\]openFileWrite

openFileWrite(path: string): Promise<number>

Opens a file in write-only mode. This API returns the result asynchronously through a promise.

**Required permission**: ohos.permission.FILE\_GUARD\_MANAGER

**System capability**: SystemCapability.PCService.FileGuard

**Start version**: 5.1.1(19)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

path

 | 

string

 | 

Yes

 | 

Subset of absolute paths in the [personal directory of a user](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/dataguard-introduction#li61091691019).

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<number>

 | 

Promise used to return the FD of the file opened.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

201

 | 

Permission denied.

 |
| 

401

 | 

Parameter error. Possible causes:

1\. Mandatory parameters are left unspecified.

2\. Incorrect parameter types.

3\. Parameter verification failed.

 |

**Example**:

import { BusinessError } from '@kit.BasicServicesKit';

let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
let path: string = '/data/service/el2/100/hmdfs/account/files/Docs/Documents/test.txt';
guard.openFileWrite(path).then((fd: number) => {
  console.info(\`Succeeded in opening file in write-only mode. path: ${path}, fd: ${fd}.\`);
}).catch((err: BusinessError) => {
  console.error(\`Failed to open file in write-only mode. Code: ${err.code}, message: ${err.message}.\`);
});

#### \[h2\]setFileTag

setFileTag(path: string, level: SecurityLevel, tag: string, callback: AsyncCallback<void>): void

Sets file tags. This API returns the result asynchronously through a callback.

**Required permission**: ohos.permission.FILE\_GUARD\_MANAGER

**System capability**: SystemCapability.PCService.FileGuard

**Start version**: 4.0.0(10)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

path

 | 

string

 | 

Yes

 | 

Subset of absolute paths in the [default path range](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/dataguard-introduction#li1475101851010).

 |
| 

level

 | 

[SecurityLevel](#section36136612415)

 | 

Yes

 | 

File security level. The options are **EXTERNAL**, **INTERNAL**, **SECRET**, **CONFIDENTIAL**, and **TOP SECRET**.

 |
| 

tag

 | 

string

 | 

Yes

 | 

File tag, which cannot exceed 65536 bytes.

 |
| 

callback

 | 

AsyncCallback<void>

 | 

Yes

 | 

Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

201

 | 

Permission denied.

 |
| 

401

 | 

The parameter check failed.

 |

**Example**:

import { BusinessError } from '@kit.BasicServicesKit';

let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
let path: string = '/data/service/el2/test/test.txt';
let tag: string = 'test';
guard.setFileTag(path, fileGuard.SecurityLevel.EXTERNAL, tag, (err: BusinessError) => {
  if (err) {
    console.error(\`Failed to set file tag. Code: ${err.code}, message: ${err.message}.\`);
    return;
  }
  console.info(\`Succeeded in setting file tag.\`);
});

#### \[h2\]setFileTag

setFileTag(path: string, level: SecurityLevel, tag: string): Promise<void>

Sets file tags. This API returns the result asynchronously through a promise.

**Required permission**: ohos.permission.FILE\_GUARD\_MANAGER

**System capability**: SystemCapability.PCService.FileGuard

**Start version**: 4.0.0(10)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

path

 | 

string

 | 

Yes

 | 

Subset of absolute paths in the [default path range](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/dataguard-introduction#li1475101851010).

 |
| 

level

 | 

[SecurityLevel](#section36136612415)

 | 

Yes

 | 

File security level. The options are **EXTERNAL**, **INTERNAL**, **SECRET**, **CONFIDENTIAL**, and **TOP SECRET**.

 |
| 

tag

 | 

string

 | 

Yes

 | 

File tag, which cannot exceed 65536 bytes.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<void>

 | 

**Promise** object. No result is returned.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

201

 | 

Permission denied.

 |
| 

401

 | 

The parameter check failed.

 |

**Example**:

import { BusinessError } from '@kit.BasicServicesKit';

let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
let path: string = '/data/service/el2/test/test.txt';
let tag: string = 'test';
guard.setFileTag(path, fileGuard.SecurityLevel.EXTERNAL, tag).then(() => {
  console.info(\`Succeeded in setting file tag.\`);
}).catch((err: BusinessError) => {
  console.error(\`Failed to set file tag. Code: ${err.code}, message: ${err.message}.\`);
});

#### \[h2\]queryFileTag

queryFileTag(path: string, callback: AsyncCallback<FileTagInfo>): void

Obtains the file tags. This API returns the result asynchronously through a callback.

**Required permission**: ohos.permission.FILE\_GUARD\_MANAGER

**System capability**: SystemCapability.PCService.FileGuard

**Start version**: 4.0.0(10)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

path

 | 

string

 | 

Yes

 | 

Subset of absolute paths in the [default path range](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/dataguard-introduction#li1475101851010).

 |
| 

callback

 | 

AsyncCallback<[FileTagInfo](#section118461622113311)\>

 | 

Yes

 | 

Callback used to return the file tag information object.

If the operation is successful, **err** is **undefined** and **data** is the obtained [FileTagInfo](#section118461622113311) object; otherwise, **err** is an error object.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

201

 | 

Permission denied.

 |
| 

401

 | 

The parameter check failed.

 |

**Example**:

import { BusinessError } from '@kit.BasicServicesKit';

let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
let path: string = '/data/service/el2/test/test.txt';
guard.queryFileTag(path, (err: BusinessError, data: fileGuard.FileTagInfo) => {
  if (err) {
    console.error(\`Failed to query file tag. Code: ${err.code}, message: ${err.message}.\`);
    return;
  }
  console.info(\`Succeeded in querying file tag.\`);
});

#### \[h2\]queryFileTag

queryFileTag(path: string): Promise<FileTagInfo>

Obtains the file tags. This API returns the result asynchronously through a promise.

**Required permission**: ohos.permission.FILE\_GUARD\_MANAGER

**System capability**: SystemCapability.PCService.FileGuard

**Start version**: 4.0.0(10)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

path

 | 

string

 | 

Yes

 | 

Subset of absolute paths in the [default path range](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/dataguard-introduction#li1475101851010).

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[FileTagInfo](#section118461622113311)\>

 | 

Promise used to return the file tag information object.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

201

 | 

Permission denied.

 |
| 

401

 | 

The parameter check failed.

 |

**Example**:

import { BusinessError } from '@kit.BasicServicesKit';

let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
let path: string = '/data/service/el2/test/test.txt';
guard.queryFileTag(path).then((data: fileGuard.FileTagInfo) => {
  console.info(\`Succeeded in querying file tag.\`);
}).catch((err: BusinessError) => {
  console.error(\`Failed to query file tag. Code: ${err.code}, message: ${err.message}.\`);
});

#### \[h2\]getFileUri

getFileUri(path: string, callback: AsyncCallback<FilePathInfo>): void

Obtains the URI of a file. This API returns the result asynchronously through a callback.

**Required permission**: ohos.permission.FILE\_GUARD\_MANAGER

**System capability**: SystemCapability.PCService.FileGuard

**Start version**: 4.0.0(10)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

path

 | 

string

 | 

Yes

 | 

Subset of absolute paths in the [personal directory of a user](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/dataguard-introduction#li61091691019).

 |
| 

callback

 | 

AsyncCallback<[FilePathInfo](#section1026911633210)\>

 | 

Yes

 | 

Callback function. If the operation is successful, **err** is **undefined** and **data** is the [FilePathInfo](#section1026911633210) obtained; otherwise, **err** is an error object.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

201

 | 

Permission denied.

 |
| 

401

 | 

The parameter check failed.

 |

**Example**:

import { BusinessError } from '@kit.BasicServicesKit';

let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
let path: string = '/data/service/el2/100/hmdfs/account/files/test/test.txt';
guard.getFileUri(path, (err: BusinessError, data: fileGuard.FilePathInfo) => {
  if (err) {
    console.error(\`Failed to get file uri. Code: ${err.code}, message: ${err.message}.\`);
  }else{
    console.info(\`Succeeded in getting file uri.\`);
  }
});

#### \[h2\]getFileUri

getFileUri(path: string): Promise<FilePathInfo>

Obtains the URI of a file. This API returns the result asynchronously through a promise.

**Required permission**: ohos.permission.FILE\_GUARD\_MANAGER

**System capability**: SystemCapability.PCService.FileGuard

**Start version**: 4.0.0(10)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

path

 | 

string

 | 

Yes

 | 

Subset of absolute paths in the [personal directory of a user](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/dataguard-introduction#li61091691019).

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[FilePathInfo](#section1026911633210)\>

 | 

Promise used to return the absolute path and URI of a file.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

201

 | 

Permission denied.

 |
| 

401

 | 

The parameter check failed.

 |

**Example**:

import { BusinessError } from '@kit.BasicServicesKit';

let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
let path: string = '/data/service/el2/100/hmdfs/account/files/test/test.txt';
guard.getFileUri(path).then((data: fileGuard.FilePathInfo) => {
  console.info(\`Succeeded in getting file uri.\`);
}).catch((err: BusinessError) => {
  console.error(\`Failed to get file uri. Code: ${err.code}, message: ${err.message}.\`);
});

#### \[h2\]deleteFile

deleteFile(path: string, callback: AsyncCallback<void>): void

Deletes files in a specified directory. This API returns the result asynchronously through a callback.

**Required permission**: ohos.permission.FILE\_GUARD\_MANAGER

**System capability**: SystemCapability.PCService.FileGuard

**Start version**: 4.0.0(10)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

path

 | 

string

 | 

Yes

 | 

Subset of absolute paths in the [personal directory of a user](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/dataguard-introduction#li61091691019).

 |
| 

callback

 | 

AsyncCallback<void>

 | 

Yes

 | 

Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

201

 | 

Permission denied.

 |
| 

401

 | 

The parameter check failed.

 |

**Example**:

import { BusinessError } from '@kit.BasicServicesKit';

let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
let path: string = '/data/service/el2/100/hmdfs/account/files/Docs/Documents/test.txt';
guard.deleteFile(path, (err: BusinessError) => {
  if (err) {
    console.error(\`Failed to delete file. Code: ${err.code}, message: ${err.message}.\`);
  }else{
    console.info(\`Succeeded in deleting file.\`);
  }
});

#### \[h2\]deleteFile

deleteFile(path: string): Promise<void>

Deletes files in a specified directory. This API returns the result asynchronously through a promise.

**Required permission**: ohos.permission.FILE\_GUARD\_MANAGER

**System capability**: SystemCapability.PCService.FileGuard

**Start version**: 4.0.0(10)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

path

 | 

string

 | 

Yes

 | 

Subset of absolute paths in the [personal directory of a user](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/dataguard-introduction#li61091691019).

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<void>

 | 

**Promise** object. No result is returned.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

201

 | 

Permission denied.

 |
| 

401

 | 

The parameter check failed.

 |

**Example**:

import { BusinessError } from '@kit.BasicServicesKit';

let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
let path: string = '/data/service/el2/100/hmdfs/account/files/Docs/Documents/test.txt';
guard.deleteFile(path).then(() => {
  console.info(\`Succeeded in deleting file.\`);
}).catch((err: BusinessError) => {
  console.error(\`Failed to delete file. Code: ${err.code}, message: ${err.message}.\`);
});

#### \[h2\]updatePolicy

updatePolicy(policy: string, callback: AsyncCallback<void>): void

Updates the security control policy. This API returns the result asynchronously through a callback.

**Required permission**: ohos.permission.SET\_FILE\_GUARD\_POLICY

**System capability**: SystemCapability.PCService.FileGuard

**Start version**: 4.0.0(10)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

policy

 | 

string

 | 

Yes

 | 

Security control policy.

Fields in the policy are described as follows:

**net\_intercept\_toggle**: indicates whether to block unauthorized transfers. The options are **0** (no) and **1** (yes). The default value is **0**.

**boundary**: list of public network segments.

**netsegment\_trustlist**: list of trusted network segments.

**netsegment\_blocklist:**: list of untrusted network segments.

**default\_policy**: default network segment policy (for network segments other than trusted and untrusted network segments in the public network). The options are **0** (block) and **1** (not block). The default value is **0**.

 |
| 

callback

 | 

AsyncCallback<void>

 | 

Yes

 | 

Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

201

 | 

Permission denied.

 |
| 

401

 | 

The parameter check failed.

 |

**Example**:

import { BusinessError } from '@kit.BasicServicesKit';

let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
let policy: string = '{' +
  '"net\_intercept\_toggle":0,' +
  '"boundary":\["10.10.0.0-10.255.255.255","172.16.0.0-172.31.255.255"\],' +
  '"netsegment\_trustlist":\["10.10.0.0-10.255.255.255"\],' +
  '"netsegment\_blocklist":\["172.16.0.0-172.31.255.255"\],' +
  '"default\_policy":0' +
  '}';
guard.updatePolicy(policy, (err: BusinessError) => {
  if (err) {
    console.error(\`Failed to update policy. Code: ${err.code}, message: ${err.message}.\`);
  } else {
    console.info(\`Succeeded in updating policy.\`);
  }
});

#### \[h2\]updatePolicy

updatePolicy(policy: string): Promise<void>

Updates the security control policy. This API returns the result asynchronously through a promise.

**Required permission**: ohos.permission.SET\_FILE\_GUARD\_POLICY

**System capability**: SystemCapability.PCService.FileGuard

**Start version**: 4.0.0(10)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

policy

 | 

string

 | 

Yes

 | 

Security control policy.

Fields in the policy are described as follows:

**net\_intercept\_toggle**: indicates whether to block unauthorized transfers. The options are **0** (no) and **1** (yes). The default value is **0**.

**boundary**: list of public network segments.

**netsegment\_trustlist**: list of trusted network segments.

**netsegment\_blocklist:**: list of untrusted network segments.

**default\_policy**: default network segment policy (for network segments other than trusted and untrusted network segments in the public network). The options are **0** (block) and **1** (not block). The default value is **0**.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<void>

 | 

**Promise** object. No result is returned.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

201

 | 

Permission denied.

 |
| 

401

 | 

The parameter check failed.

 |

**Example**:

import { BusinessError } from '@kit.BasicServicesKit';

let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
let policy: string = '{' +
  '"net\_intercept\_toggle":0,' +
  '"boundary":\["10.10.0.0-10.255.255.255","172.16.0.0-172.31.255.255"\],' +
  '"netsegment\_trustlist":\["10.10.0.0-10.255.255.255"\],' +
  '"netsegment\_blocklist":\["172.16.0.0-172.31.255.255"\],' +
  '"default\_policy":0' +
  '}';
guard.updatePolicy(policy).then(() => {
  console.info(\`Succeeded in updating policy.\`);
}).catch((err: BusinessError) => {
  console.error(\`Failed to update policy. Code: ${err.code}, message: ${err.message}.\`);
});

#### \[h2\]setKiaFilelist

setKiaFilelist(filelist: string, callback: AsyncCallback<void>): void

Sets the KIA file list. This API returns the result asynchronously through a callback.

**Required permission**: ohos.permission.FILE\_GUARD\_MANAGER

**System capability**: SystemCapability.PCService.FileGuard

**Start version**: 4.0.0(10)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

filelist

 | 

string

 | 

Yes

 | 

List of KIA file absolute paths in the [default path range](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/dataguard-introduction#li1475101851010).

 |
| 

callback

 | 

AsyncCallback<void>

 | 

Yes

 | 

Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

201

 | 

Permission denied.

 |
| 

401

 | 

The parameter check failed.

 |

**Example**:

import { BusinessError } from '@kit.BasicServicesKit';

let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
let fileListStr: string = '{"kia\_filelist":\["/data/service/el2/100/hmdfs/account/files/Documents/Desktop/aaa.docx","/data/service/el2/100/hmdfs/account/files/Documents/Desktop/bbb.docx"\]}';
guard.setKiaFilelist(fileListStr, (err: BusinessError) => {
  if (err) {
    console.error(\`Failed to set the list of KIA file. Code: ${err.code}, message: ${err.message}.\`);
  } else {
    console.info(\`Succeeded in setting the list of KIA file.\`);
  }
});

#### \[h2\]setKiaFilelist

setKiaFilelist(filelist: string): Promise<void>

Sets the KIA file list. This API returns the result asynchronously through a promise.

**Required permission**: ohos.permission.FILE\_GUARD\_MANAGER

**System capability**: SystemCapability.PCService.FileGuard

**Start version**: 4.0.0(10)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

filelist

 | 

string

 | 

Yes

 | 

List of KIA file absolute paths in the [default path range](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/dataguard-introduction#li1475101851010).

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<void>

 | 

**Promise** object. No result is returned.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

201

 | 

Permission denied.

 |
| 

401

 | 

The parameter check failed.

 |

**Example**:

import { BusinessError } from '@kit.BasicServicesKit';

let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
let fileListStr: string = '{"kia\_filelist":\["/data/service/el2/100/hmdfs/account/files/Documents/Desktop/aaa.docx","/data/service/el2/100/hmdfs/account/files/Documents/Desktop/bbb.docx"\]}';
guard.setKiaFilelist(fileListStr).then(() => {
  console.info(\`Succeeded in setting the list of KIA file.\`);
}).catch((err: BusinessError) => {
  console.error(\`Failed to set the list of KIA file. Code: ${err.code}, message: ${err.message}.\`);
});

#### \[h2\]on('kiaCopy')

on(type: 'kiaCopy', callback: Callback<string>): void

Subscribes to KIA file copy events. This API returns the result through a callback.

**Required permission**: ohos.permission.FILE\_GUARD\_MANAGER

**System capability**: SystemCapability.PCService.FileGuard

**Start version**: 5.0.3(15)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

**'kiaCopy'**: KIA file copy event. This parameter is always set to this value.

 |
| 

callback

 | 

Callback<string>

 | 

Yes

 | 

Callback function used to return the KIA file copy event.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

201

 | 

Permission denied.

 |
| 

401

 | 

The parameter check failed.

 |

**Example**:

let guard: fileGuard.FileGuard = new fileGuard.FileGuard();

function onKiaCopyCallback(eventData: string) {
  console.info(\`Succeeded in receiving eventData: ${eventData}.\`);
}
try {
  guard.on('kiaCopy', onKiaCopyCallback);
} catch (e) {
  console.error(\`Failed to listen the kia file copy event. Code: ${e.code}, message: ${e.message}.\`);
}

#### \[h2\]off('kiaCopy')

off(type: 'kiaCopy', callback?: Callback<string>): void

Unsubscribes from KIA file copy events. This API returns the result through a callback.

**Required permission**: ohos.permission.FILE\_GUARD\_MANAGER

**System capability**: SystemCapability.PCService.FileGuard

**Start version**: 5.0.3(15)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

**'kiaCopy'**: KIA file copy event. This parameter is always set to this value.

 |
| 

callback

 | 

Callback<string>

 | 

No

 | 

Callback function used to return the KIA file copy information.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

201

 | 

Permission denied.

 |
| 

401

 | 

The parameter check failed.

 |

**Example**:

let guard: fileGuard.FileGuard = new fileGuard.FileGuard();

function offKiaCopyCallback(eventData: string) {
  console.info(\`Succeeded in receiving eventData: ${eventData}.\`);
}
try {
  guard.off('kiaCopy', offKiaCopyCallback);
} catch (e) {
  console.error(\`Failed to cancel listen the KIA file copy event. Code: ${e.code}, message: ${e.message}.\`);
}

#### \[h2\]on('kiaRename')

on(type: 'kiaRename', callback: Callback<string>): void

Subscribes to KIA file rename events. This API returns the result through a callback.

**Required permission**: ohos.permission.FILE\_GUARD\_MANAGER

**System capability**: SystemCapability.PCService.FileGuard

**Start version**: 5.0.3(15)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

**'kiaRename'**: KIA file rename event. This parameter is always set to this value.

 |
| 

callback

 | 

Callback<string>

 | 

Yes

 | 

Callback function used to return the KIA file rename event.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

201

 | 

Permission denied.

 |
| 

401

 | 

The parameter check failed.

 |

**Example**:

let guard: fileGuard.FileGuard = new fileGuard.FileGuard();

function onKiaRenameCallback(eventData: string) {
  console.info(\`Succeeded in receiving eventData: ${eventData}.\`);
}
try {
  guard.on('kiaRename', onKiaRenameCallback);
} catch (e) {
  console.error(\`Failed to listen the KIA file rename event. Code: ${e.code}, message: ${e.message}.\`);
}

#### \[h2\]off('kiaRename')

off(type: 'kiaRename', callback?: Callback<string>): void

Unsubscribes from KIA file rename events. This API returns the result through a callback.

**Required permission**: ohos.permission.FILE\_GUARD\_MANAGER

**System capability**: SystemCapability.PCService.FileGuard

**Start version**: 5.0.3(15)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

**'kiaRename'**: KIA file rename event. This parameter is always set to this value.

 |
| 

callback

 | 

Callback<string>

 | 

No

 | 

Callback function used to return the KIA file renaming information.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

201

 | 

Permission denied.

 |
| 

401

 | 

The parameter check failed.

 |

**Example**:

let guard: fileGuard.FileGuard = new fileGuard.FileGuard();

function offKiaRenameCallback(eventData: string) {
  console.info(\`Succeeded in receiving eventData: ${eventData}.\`);
}
try {
  guard.off('kiaRename', offKiaRenameCallback);
} catch (e) {
  console.error(\`Failed to cancel listen the KIA file rename event. Code: ${e.code}, message: ${e.message}.\`);
}

#### \[h2\]on('kiaCompress')

on(type: 'kiaCompress', callback: Callback<string>): void

Subscribes to KIA file compress events. This API returns the result through a callback.

**Required permission**: ohos.permission.FILE\_GUARD\_MANAGER

**System capability**: SystemCapability.PCService.FileGuard

**Start version**: 5.0.3(15)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

**'kiaCompress'**: KIA file compress event. This parameter is always set to this value.

 |
| 

callback

 | 

Callback<string>

 | 

Yes

 | 

Callback function used to return the KIA file compress event.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

201

 | 

Permission denied.

 |
| 

401

 | 

The parameter check failed.

 |

**Example**:

let guard: fileGuard.FileGuard = new fileGuard.FileGuard();

function onKiaCompressCallback(eventData: string) {
  console.info(\`Succeeded in receiving eventData: ${eventData}.\`);
}
try {
  guard.on('kiaCompress', onKiaCompressCallback);
} catch (e) {
  console.error(\`Failed to listen the KIA file compress event. Code: ${e.code}, message: ${e.message}.\`);
}

#### \[h2\]off('kiaCompress')

off(type: 'kiaCompress', callback?: Callback<string>): void

Unsubscribes from KIA file compress events. This API returns the result through a callback.

**Required permission**: ohos.permission.FILE\_GUARD\_MANAGER

**System capability**: SystemCapability.PCService.FileGuard

**Start version**: 5.0.3(15)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

**'kiaCompress'**: KIA file compress event. This parameter is always set to this value.

 |
| 

callback

 | 

Callback<string>

 | 

No

 | 

Callback function used to return the KIA file compression information.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

201

 | 

Permission denied.

 |
| 

401

 | 

The parameter check failed.

 |

**Example**:

let guard: fileGuard.FileGuard = new fileGuard.FileGuard();

function offKiaCompressCallback(eventData: string) {
  console.info(\`Succeeded in receiving eventData: ${eventData}.\`);
}
try {
  guard.off('kiaCompress', offKiaCompressCallback);
} catch (e) {
  console.error(\`Failed to cancel listen the KIA file compress event. Code: ${e.code}, message: ${e.message}.\`);
}

#### \[h2\]setKiaWatermarkImage

setKiaWatermarkImage(image: Uint8Array, info: string): Promise<void>

Sets a KIA file watermark image.

**Required permission**: ohos.permission.SET\_FILE\_GUARD\_POLICY

**System capability**: SystemCapability.PCService.FileGuard

**Start version**: 5.0.3(15)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

image

 | 

Uint8Array

 | 

Yes

 | 

Watermark image.

 |
| 

info

 | 

string

 | 

Yes

 | 

Watermark additional information.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<void>

 | 

**Promise** object. No result is returned.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

201

 | 

Permission denied.

 |
| 

401

 | 

The parameter check failed.

 |

**Example**:

import { fileIo as fs } from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';

async function testSetKiaWaterMarkImage() {
  try {
    let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
    let imagePath: string = '/data/service/el2/100/hmdfs/account/files/Docs/Documents/1.png';
    let fd: number = await guard.openFile(imagePath);
    let stat: fs.Stat = fs.statSync(fd);
    let buffer: ArrayBuffer = new ArrayBuffer(stat.size);
    fs.readSync(fd, buffer);

    let image: Uint8Array = new Uint8Array(buffer);
    let info: string = new Date().toLocaleString();
    guard.setKiaWatermarkImage(image, info).then(() => {
      console.info(\`Succeeded in setting the watermark image for Kia file.\`);
    }).catch((err: BusinessError) => {
      console.error(\`Failed to set the watermark image for Kia file. Code: ${err.code}, message: ${err.message}.\`);
    })
  } catch (e) {
    console.error(\`testSetKiaWaterMarkImage Exception, Code: ${e.code}, message: ${e.message}\`);
  }
}

#### \[h2\]setFileCustomTag

setFileCustomTag(path: string, tagList: Array<string>, callback: AsyncCallback<void>): void

Sets custom tags for a file.

**Required permission**: ohos.permission.FILE\_GUARD\_MANAGER

**System capability**: SystemCapability.PCService.FileGuard

**Start version**: 5.1.1(19)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

path

 | 

string

 | 

Yes

 | 

Subset of absolute paths in the [default path range](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/dataguard-introduction#li1475101851010).

 |
| 

tagList

 | 

Array<string>

 | 

Yes

 | 

List of tags. The number of tags cannot exceed 5.

 |
| 

callback

 | 

AsyncCallback<void>

 | 

Yes

 | 

Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

201

 | 

Permission denied.

 |
| 

1001700103

 | 

The path is not exist.

 |
| 

1001700104

 | 

The tag list check failed.

 |

**Example**:

import { BusinessError } from '@kit.BasicServicesKit';

let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
let path: string = '/data/service/el2/100/hmdfs/account/files/Docs/Documents/test.txt';
let tagList: string\[\] = \['tag1', 'tag2'\];
guard.setFileCustomTag(path, tagList, (err: BusinessError) => {
  if (err) {
    console.error(\`Failed to set file custom tag. Code: ${err.code}, message: ${err.message}.\`);
  } else {
    console.info(\`Succeeded in setting file custom tag.\`);
  }
});

#### \[h2\]setFileCustomTag

setFileCustomTag(path: string, tagList: Array<string>): Promise<void>

Sets custom tags for a file.

**Required permission**: ohos.permission.FILE\_GUARD\_MANAGER

**System capability**: SystemCapability.PCService.FileGuard

**Start version**: 5.1.1(19)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

path

 | 

string

 | 

Yes

 | 

Subset of absolute paths in the [default path range](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/dataguard-introduction#li1475101851010).

 |
| 

tagList

 | 

Array<string>

 | 

Yes

 | 

List of tags. The number of tags cannot exceed 5.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<void>

 | 

**Promise** object. No result is returned.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

201

 | 

Permission denied.

 |
| 

1001700103

 | 

The path is not exist.

 |
| 

1001700104

 | 

The tag list check failed.

 |

**Example**:

import { BusinessError } from '@kit.BasicServicesKit';

let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
let path: string = '/data/service/el2/100/hmdfs/account/files/Docs/Documents/test.txt';
let tagList: string\[\] = \['tag1', 'tag2'\];
guard.setFileCustomTag(path, tagList).then(() => {
  console.info(\`Succeeded in setting file custom tag.\`);
}).catch((err: BusinessError) => {
  console.error(\`Failed to set file custom tag. Code: ${err.code}, message: ${err.message}.\`);
});

#### \[h2\]unsetFileCustomTag

unsetFileCustomTag(path: string, tagList: Array<string>, callback: AsyncCallback<void>): void

Cancels custom tag setting for a file.

**Required permission**: ohos.permission.FILE\_GUARD\_MANAGER

**System capability**: SystemCapability.PCService.FileGuard

**Start version**: 5.1.1(19)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

path

 | 

string

 | 

Yes

 | 

Subset of absolute paths in the [default path range](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/dataguard-introduction#li1475101851010).

 |
| 

tagList

 | 

Array<string>

 | 

Yes

 | 

List of tags. The number of tags cannot exceed 5.

 |
| 

callback

 | 

AsyncCallback<void>

 | 

Yes

 | 

Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

201

 | 

Permission denied.

 |
| 

1001700103

 | 

The path is not exist.

 |
| 

1001700104

 | 

The tag list check failed.

 |

**Example**:

import { BusinessError } from '@kit.BasicServicesKit';

let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
let path: string = '/data/service/el2/100/hmdfs/account/files/Docs/Documents/test.txt';
let tagList: string\[\] = \['tag1', 'tag2'\];
guard.unsetFileCustomTag(path, tagList, (err: BusinessError) => {
  if (err) {
    console.error(\`Failed to unset file custom tag. Code: ${err.code}, message: ${err.message}.\`);
  } else {
    console.info(\`Succeeded in unsetting file custom tag.\`);
  }
});

#### \[h2\]unsetFileCustomTag

unsetFileCustomTag(path: string, tagList: Array<string>): Promise<void>

Cancels custom tag setting for a file.

**Required permission**: ohos.permission.FILE\_GUARD\_MANAGER

**System capability**: SystemCapability.PCService.FileGuard

**Start version**: 5.1.1(19)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

path

 | 

string

 | 

Yes

 | 

Subset of absolute paths in the [default path range](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/dataguard-introduction#li1475101851010).

 |
| 

tagList

 | 

Array<string>

 | 

Yes

 | 

List of tags. The number of tags cannot exceed 5.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<void>

 | 

**Promise** object. No result is returned.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

201

 | 

Permission denied.

 |
| 

1001700103

 | 

The path is not exist.

 |
| 

1001700104

 | 

The tag list check failed.

 |

**Example**:

import { BusinessError } from '@kit.BasicServicesKit';

let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
let path: string = '/data/service/el2/100/hmdfs/account/files/Docs/Documents/test.txt';
let tagList: string\[\] = \['tag1', 'tag2'\];
guard.unsetFileCustomTag(path, tagList).then(() => {
  console.info(\`Succeeded in unsetting file custom tag.\`);
}).catch((err: BusinessError) => {
  console.error(\`Failed to unset file custom tag. Code: ${err.code}, message: ${err.message}.\`);
});
