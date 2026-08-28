# Setting Metadata of a Cloud File

File metadata includes common attributes such as the cloud file name, size, and type, as well as custom file attributes.

You can set custom file attributes after saving a file on the cloud.

#### Restrictions

This kit supports phones and tablets by default. Support for wearables is available starting from 5.1.0(18), and for TVs starting from 5.1.1(19).

#### Prerequisites

-   You have [initialized a storage instance](../initializing-a-storage-instance/document.md).
-   You have [uploaded a specified file to the cloud](../uploading-a-specified-file-to-the-cloud/document.md).

#### Procedure

Call [StorageBucket.setMetadata](https://developer.huawei.com/consumer/en/doc/harmonyos-references/cloudfoundation-cloudstorage#section1924314716387) to set metadata of a cloud file.

import { cloudStorage } from '@kit.CloudFoundationKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let storageBucket: cloudStorage.StorageBucket = cloudStorage.bucket();

@Component
export struct testPage {
  build() {
  }

  // Set metadata.
  setMetaData() {
    // Set the metadata of the **screenshot/screenshot\_20250115\_155321.jpg** file in the default Cloud Storage instance.
    storageBucket.setMetadata('screenshot/screenshot\_20250115\_155321.jpg', {
      customMetadata: {
        key1: "value1",
        key2: "value2"
      }
    }).then((metadata: cloudStorage.Metadata) => {
      hilog.info(0x0000, 'testTag', \`Succeeded in setting metadata: ${JSON.stringify(metadata)}\`);
    }).catch((err: BusinessError) => {
      hilog.error(0x0000, 'testTag', \`Failed to set metadata, code: ${err.code}, message: ${err.message}\`);
    })
  }
}
