# Obtaining the Cloud File List

You can obtain information about all files in a specified cloud directory, including the file storage directory and file name.

#### Restrictions

This kit supports phones and tablets by default. Support for wearables is available starting from 5.1.0(18), and for TVs starting from 5.1.1(19).

#### Prerequisites

-   You have [initialized a storage instance](../initializing-a-storage-instance/document.md).
-   You have [uploaded a specified file to the cloud](../uploading-a-specified-file-to-the-cloud/document.md).

#### Procedure

Call [StorageBucket.list](https://developer.huawei.com/consumer/en/doc/harmonyos-references/cloudfoundation-cloudstorage#section420475053513) to obtain the list of files in a specified directory on the cloud.

The complete sample code is as follows:

import { cloudStorage } from '@kit.CloudFoundationKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let storageBucket: cloudStorage.StorageBucket = cloudStorage.bucket();

@Component
export struct testPage {
  build() {
  }

  // Obtain the file list.
  getList() {
    // Obtain the list of files in the root path of the default Cloud Storage instance.
    storageBucket.list('').then((result: cloudStorage.ListResults) => {
      hilog.info(0x0000, 'testTag', \`Succeeded in listing files, result: ${JSON.stringify(result)}\`);
    }).catch((err: BusinessError) => {
      hilog.error(0x0000, 'testTag', \`Failed to list files, code: ${err.code}, message: ${err.message}\`);
    })
  }
}

The structure of the obtained file list is as follows:

{
  directories: \["empty-dir1\\/", "screenshot\\/"\],
  files: \["IMG\_20240229\_103118.jpg", "IMG\_20240318\_093732.jpg"\]
}
