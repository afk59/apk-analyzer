# fileManagerService

This module provides the capability of moving files to the recycle bin and obtaining file icons.

**Start version**: 5.0.5(17)

#### Module Import

import { fileManagerService } from '@kit.FileManagerServiceKit';

#### fileManagerService.deleteToTrash

deleteToTrash(uri: string): Promise<string>

Asynchronously moves a file to the recycle bin and returns the path of the file after being moved to the recycle bin. This API returns the result asynchronously through a promise.

**Note**: For details about how to use the **uri** parameter in this API, please refer to [Document URI](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/user-file-uri-intro#document-uri).

**System capability**: SystemCapability.FileManagement.FileManagerService.Core

**Start version**: 5.0.5(17)

**Parameters:**

| 
**Parameter**

 | 

**Type**

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

uri

 | 

string

 | 

Yes

 | 

URI of the file to be deleted.

 |

**Returns:**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<string>

 | 

URI of the file after it is moved to the recycle bin. This API returns the result asynchronously through a promise.

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

401

 | 

Parameter error.

 |
| 

1014000001

 | 

Operation not permitted.

 |
| 

1014000002

 | 

No such file or directory.

 |
| 

1014000003

 | 

No space left on device.

 |
| 

1014000004

 | 

System inner fail.

 |

**Sample code**:

import { fileManagerService } from '@kit.FileManagerServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

async function deleteFile() {
  // A built-in storage directory is used as an example.
  // **targetUri** in the sample code indicates the URI of the file in the **Download** directory.
  // Perform development based on the obtained URI and ensure that the read and write permissions on the file are obtained.
  let targetUri: string = "file://docs/storage/Users/currentUser/Download/1.txt";
  try {
    let trashUri: string = await fileManagerService.deleteToTrash(targetUri);
    console.info("trashUri: " + trashUri);
  } catch (err) {
    let error: BusinessError = err as BusinessError;
    console.error("delete failed, errCode:" + error.code + ", errMessage:" + error.message);
  }
}

#### fileManagerService.getFileIconSync

getFileIconSync(fileType: string): string | Resource

Obtains a file icon based on the file type.

**Required permission**: ohos.permission.GET\_FILE\_ICON

**System capability**: SystemCapability.FileManagement.FileManagerService.Core

**Start version**: 5.0.5(17)

**Parameters:**

| 
**Parameter**

 | 

**Type**

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

fileType

 | 

string

 | 

Yes

 | 

[UTD-ID corresponding to the file type](../../icon-format-description/document.md).

 |

**Returns:**

| 
**Type**

 | 

Description

 |
| :-- | :-- |
| 

string | [Resource](../../../../application-framework/arkui/arkts-components/common-definitions/basic-types/document.md#resource)

 | 

Base64-encoded file icon or its resource object.

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

Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed.

 |
| 

1014000004

 | 

System inner fail.

 |

**Sample code**:

import { fileManagerService } from '@kit.FileManagerServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { uniformTypeDescriptor } from '@kit.ArkData';

@Entry
@Component
struct Index {
  @State fileIcon: string | Resource = '';

  private getFileIconByFileExtension(filenameExtension: string): void {
    try {
      let typeId: string = uniformTypeDescriptor.getUniformDataTypeByFilenameExtension(filenameExtension);
      this.fileIcon = fileManagerService.getFileIconSync(typeId);
    } catch (error) {
      let err: BusinessError = error as BusinessError;
      console.error('getFileIconByFileExtension failed with err: ' + JSON.stringify(err));
    }
  }

  build() {
    RelativeContainer() {
      Column() {
        Image(this.fileIcon)
          .height(88)
          .border({ width: 1, radius: 6 })
        Button('Update FileIcon')
          .onClick(() => {
            // The TXT format is used as an example.
            this.getFileIconByFileExtension('.txt');
          })
      }
    }
    .height('100%')
    .width('100%')
  }
}

#### fileManagerService.getFileIcon

getFileIcon(fileType: string): Promise<string | Resource>

Obtains a file icon based on the file type. This API returns the result asynchronously through a promise.

**Required permission**: ohos.permission.GET\_FILE\_ICON

**System capability**: SystemCapability.FileManagement.FileManagerService.Core

**Start version**: 5.0.5(17)

**Parameters:**

| 
**Parameter**

 | 

**Type**

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

fileType

 | 

string

 | 

Yes

 | 

[UTD-ID corresponding to the file type](../../icon-format-description/document.md).

 |

**Returns:**

| 
**Type**

 | 

Description

 |
| :-- | :-- |
| 

Promise<string | [Resource](../../../../application-framework/arkui/arkts-components/common-definitions/basic-types/document.md#resource)\>

 | 

Base64-encoded file icon or its resource object. This API returns the result asynchronously through a promise.

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

Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed.

 |
| 

1014000004

 | 

System inner fail.

 |

**Sample code**:

import { fileManagerService } from '@kit.FileManagerServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { uniformTypeDescriptor } from '@kit.ArkData';

@Entry
@Component
struct Index {
  @State fileIcon: string | Resource = '';

  private getFileIconByFileExtension(filenameExtension: string): void {
    try {
      console.error('getFileIconByFileExtension');
      let typeId: string = uniformTypeDescriptor.getUniformDataTypeByFilenameExtension(filenameExtension);
      fileManagerService.getFileIcon(typeId).then((retIcon: string | Resource) => {
        this.fileIcon = retIcon;
      });
    } catch (error) {
      let err: BusinessError = error as BusinessError;
      console.error('getFileIconByFileExtension failed with err: ' + JSON.stringify(err));
    }
  }

  build() {
    RelativeContainer() {
      Column() {
        Image(this.fileIcon)
          .height(88)
          .border({ width: 1, radius: 6 })
        Button('Update FileIcon')
          .onClick(() => {
            // The TXT format is used as an example.
            this.getFileIconByFileExtension('.txt');
          })
      }
    }
    .height('100%')
    .width('100%')
  }
}
