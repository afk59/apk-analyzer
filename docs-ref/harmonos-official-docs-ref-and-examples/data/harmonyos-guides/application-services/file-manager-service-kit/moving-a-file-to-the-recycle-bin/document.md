# Moving a File to the Recycle Bin

#### Use Cases

Move a file in the public directory to the recycle bin.

#### API Description

| 
API Name

 | 

Description

 |
| :-- | :-- |
| 

[deleteToTrash](https://developer.huawei.com/consumer/en/doc/harmonyos-references/filemanagerservice-arkts-filemanagerservice#section439917413536)(uri: string): Promise<string>

 | 

Moves a specified file to the recycle bin and returns the URI of the file in the recycle bin. This API returns the result asynchronously through a promise.

 |

#### Sample Code

1\. Import the File Manager Service Kit module and other related modules.

import { fileManagerService } from '@kit.FileManagerServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

2\. Move a specified file to the recycle bin.

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
