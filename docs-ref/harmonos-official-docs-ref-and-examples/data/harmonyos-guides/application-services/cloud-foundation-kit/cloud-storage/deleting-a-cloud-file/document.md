# Deleting a Cloud File

A cloud file that is no longer needed can be deleted through the app client.

#### Restrictions

This kit supports phones and tablets by default. Support for wearables is available starting from 5.1.0(18), and for TVs starting from 5.1.1(19).

#### Prerequisites

-   You have [initialized a storage instance](../initializing-a-storage-instance/document.md).
-   You have [uploaded a specified file to the cloud](../uploading-a-specified-file-to-the-cloud/document.md).

#### Procedure

Call [StorageBucket.deleteFile](https://developer.huawei.com/consumer/en/doc/harmonyos-references/cloudfoundation-cloudstorage#section1290422653419) to delete a file from the cloud.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/4lQ3qV2US0i2ie9XS0Zv6g/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062102Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=ACB13EA35A4BBB65DCDE41245DEF4288CFFF204AF63851BB5EB43AAAC8BCAEFC)

Deletion is irreversible. Once deleted, the file will be physically deleted and cannot be retrieved.

The complete sample code is as follows:

import { cloudStorage } from '@kit.CloudFoundationKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let storageBucket: cloudStorage.StorageBucket = cloudStorage.bucket();

@Component
export struct testPage {
  build() {
  }

  // Delete a cloud file.
  deleteFile() {
    // Delete the **screenshot/screenshot\_20250115\_155321.jpg** file from the default Cloud Storage instance.
    storageBucket.deleteFile('screenshot/screenshot\_20250115\_155321.jpg').then(() => {
      hilog.info(0x0000, 'testTag', \`Succeeded in deleting file.\`);
    }).catch((err: BusinessError) => {
      hilog.error(0x0000, 'testTag', \`Failed to delete file, code: ${err.code}, message: ${err.message}\`);
    })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/jvlJYBPGTvuaBq3lo0WpsQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062102Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0DD6AC3102B9200784B7AEB28FF701FCE6B00FAA9DA1FC2B7F76CCDF32C1D275)

After the file is deleted, you can sign in to [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html), select a project, and go to the **Cloud Storage** page to view the file list.
