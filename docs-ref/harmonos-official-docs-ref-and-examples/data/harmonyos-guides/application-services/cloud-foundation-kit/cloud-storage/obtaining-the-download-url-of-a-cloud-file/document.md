# Obtaining the Download URL of a Cloud File

After uploading a file to the cloud, you can obtain the download URL and provide it on your website for users to download the file.

#### Restrictions

This kit supports phones and tablets by default. Support for wearables is available starting from 5.1.0(18), and for TVs starting from 5.1.1(19).

#### Prerequisites

-   You have [initialized a storage instance](../initializing-a-storage-instance/document.md).
-   You have [uploaded a specified file to the cloud](../uploading-a-specified-file-to-the-cloud/document.md).

#### Procedure

Call the [StorageBucket.getDownloadURL](https://developer.huawei.com/consumer/en/doc/harmonyos-references/cloudfoundation-cloudstorage#section9969145143317) API to obtain the cloud file download URL.

The complete sample code is as follows:

import { cloudStorage } from '@kit.CloudFoundationKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let storageBucket: cloudStorage.StorageBucket = cloudStorage.bucket();

@Component
export struct testPage {
  build() {
  }

  // Obtain the download URL of a cloud file.
  getUrl() {
    // Obtain the download URL of the **screenshot/screenshot\_20250115\_155321.jpg** file from the default Cloud Storage instance.
    storageBucket.getDownloadURL('screenshot/screenshot\_20250115\_155321.jpg').then((downloadURL: string) => {
      hilog.info(0x0000, 'testTag', \`Succeeded in getting download URL: ${downloadURL}\`);
    }).catch((err: BusinessError) => {
      hilog.error(0x0000, 'testTag', \`Failed to get download URL, code: ${err.code}, message: ${err.message}\`);
    })
  }
}
