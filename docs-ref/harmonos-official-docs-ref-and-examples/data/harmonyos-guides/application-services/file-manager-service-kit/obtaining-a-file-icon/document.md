# Obtaining a File Icon

#### Use Cases

Obtain a file icon based on the file type.

#### API Description

| 
API Name

 | 

Description

 |
| :-- | :-- |
| 

function [getFileIconSync](https://developer.huawei.com/consumer/en/doc/harmonyos-references/filemanagerservice-arkts-filemanagerservice#section4895194412545)(fileType: string): string | Resource

 | 

Obtains a file icon based on the file type.

 |
| 

function [getFileIcon](https://developer.huawei.com/consumer/en/doc/harmonyos-references/filemanagerservice-arkts-filemanagerservice#section370910404112)(fileType: string): Promise<string | Resource>

 | 

Obtains a file icon based on the file type. This API returns the result asynchronously through a promise.

 |

#### Sample Code

1\. Import the File Manager Service Kit module and other related modules.

import { fileManagerService } from '@kit.FileManagerServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { uniformTypeDescriptor } from '@kit.ArkData';

2\. Request permissions. To use the API for obtaining file icons, you need to declare the required permission **ohos.permission.GET\_FILE\_ICON** in **module.json5**. For details, please refer to [Declaring Permissions](../../../system/security/application-access-control/application-permission-management/requesting-application-permissions/declaring-permissions/document.md).

3\. Obtain a file icon.

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
