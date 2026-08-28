# @ohos.file.environment (Directory Environment Capability)

The **Environment** module provides JS APIs for obtaining the root directories of the storage and user files.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/WRchEqFzRCiQqXrkgK8Y2g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062319Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=104B3A5548661799C12117DDFC314418180561A12FBA39A095F15FFDD07C751A)

The initial APIs of this module are supported since API version 11. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { Environment } from '@kit.CoreFileKit';

#### Environment.getUserDownloadDir

getUserDownloadDir(): string

Obtains the sandbox path of the pre-authorized **Download** directory.

**System capability**: SystemCapability.FileManagement.File.Environment.FolderObtain

**Device behavior differences**: This API can be called on 2-in-1 devices. If it is called on other devices, error code 801 is returned.

**Return value**

| Type | Description |
| :-- | :-- |
| string | Sandbox path of the **Download** directory obtained. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported. |
| 13900042 | Unknown error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
function getUserDownloadDirExample() {
  try {
    let path = Environment.getUserDownloadDir();
    console.info(\`Succeeded in getUserDownloadDir, path is ${path}\`);
  } catch (err) {
    console.error(\`Failed to getUserDownloadDir. Code: ${err.code}, message: ${err.message}\`);
  }
}

#### Environment.getUserDesktopDir

getUserDesktopDir(): string

Obtains the sandbox path of the pre-authorized **Desktop** directory.

**System capability**: SystemCapability.FileManagement.File.Environment.FolderObtain

**Device behavior differences**: This API can be called on 2-in-1 devices. If it is called on other devices, error code 801 is returned.

**Return value**

| Type | Description |
| :-- | :-- |
| string | Sandbox path of the **Desktop** directory obtained. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported. |
| 13900042 | Unknown error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
function getUserDesktopDirExample() {
  try {
    let path = Environment.getUserDesktopDir();
    console.info(\`Succeeded in getUserDesktopDir, path is ${path}\`);
  } catch (err) {
    console.error(\`Failed to getUserDesktopDir. Code: ${err.code}, message: ${err.message}\`);
  }
}

#### Environment.getUserDocumentDir

getUserDocumentDir(): string

Obtains the sandbox path of the pre-authorized **Document** directory.

**System capability**: SystemCapability.FileManagement.File.Environment.FolderObtain

**Device behavior differences**: This API can be called on 2-in-1 devices. If it is called on other devices, error code 801 is returned.

**Return value**

| Type | Description |
| :-- | :-- |
| string | Sandbox path of the **Documents** directory obtained. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported. |
| 13900042 | Unknown error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
function getUserDocumentDirExample() {
  try {
    let path = Environment.getUserDocumentDir();
    console.info(\`Succeeded in getUserDocumentDir, path is ${path}\`);
  } catch (err) {
    console.error(\`Failed to getUserDocumentDir. Code: ${err.code}, message: ${err.message}\`);
  }
}
