# Obtaining Metadata of a Cloud File

File metadata includes common attributes such as the cloud file name, size, and type, as well as custom file attributes.

After a file is uploaded to the cloud, you can obtain the metadata of the file before downloading the file to determine whether to download the file.

#### Restrictions

This kit supports phones and tablets by default. Support for wearables is available starting from 5.1.0(18), and for TVs starting from 5.1.1(19).

#### Prerequisites

-   You have [initialized a storage instance](../initializing-a-storage-instance/document.md).
-   You have [uploaded a specified file to the cloud](../uploading-a-specified-file-to-the-cloud/document.md).

#### Procedure

Call [StorageBucket.getMetadata](https://developer.huawei.com/consumer/en/doc/harmonyos-references/cloudfoundation-cloudstorage#section2031534817364) to obtain metadata of a specified cloud file.

The complete sample code is as follows:

import { cloudStorage } from '@kit.CloudFoundationKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let storageBucket: cloudStorage.StorageBucket = cloudStorage.bucket();

@Component
export struct testPage {
  build() {
  }

  // Obtain metadata.
  getMetaData() {
    // Obtain the metadata of the **screenshot/screenshot\_20250115\_155321.jpg** file from the default Cloud Storage instance.
    storageBucket.getMetadata('screenshot/screenshot\_20250115\_155321.jpg').then((metadata: cloudStorage.Metadata) => {
      hilog.info(0x0000, 'testTag', \`Succeeded in getting metadata: ${JSON.stringify(metadata)}\`);
    }).catch((err: BusinessError) => {
      hilog.error(0x0000, 'testTag', \`Failed to get metadata, code: ${err.code}, message: ${err.message}\`);
    })
  }
}
