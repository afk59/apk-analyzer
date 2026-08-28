# Downloading a File from the Cloud to a Local Path

After a file is uploaded to the cloud, you can download the file from the cloud to a local path.

#### Restrictions

This kit supports phones and tablets by default. Support for wearables is available starting from 5.1.0(18), and for TVs starting from 5.1.1(19).

#### Prerequisites

-   You have [initialized a storage instance](../initializing-a-storage-instance/document.md).
-   You have [uploaded a specified file to the cloud](../uploading-a-specified-file-to-the-cloud/document.md).

#### Procedure

1.  Call the [StorageBucket.downloadFile](https://developer.huawei.com/consumer/en/doc/harmonyos-references/cloudfoundation-cloudstorage#section02263293319) API to create a download task and listen to the **progress**, **completed**, and **failed** events of the download task.
2.  Start the download task.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/ABCNSRhYRnuNZvmS7qwjDA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062102Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4101F860D82ED9F55ADDFB0B869D36A409AA8678BE8F6DFF15791C9A89D92C9A)
    
    After the download is successful, the file will be saved in the [context.cacheDir](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-context#properties) directory.
    

The complete sample code is as follows:

import { cloudStorage } from '@kit.CloudFoundationKit';
import { BusinessError, request } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { GlobalContext } from '../common/GlobalContext';

let storageBucket: cloudStorage.StorageBucket = cloudStorage.bucket();

@Component
export struct testPage {
  build() {
  }

  // Download a file from the cloud to a local path.
  download() {
    // Obtain the file specified by **fileName** from the default Cloud Storage instance and save it locally.
    storageBucket.downloadFile(GlobalContext.getContext(), {
      localPath: \`screenshot.jpg\`, // The file will be stored in the **context.cacheDir** directory.
      cloudPath: \`screenshot/screenshot\_20250115\_155321.jpg\`  // Cloud file path. The value can be in format of _File directory/File name_ or _File name_.
    }).then((task: request.agent.Task) => {
      task.on('progress', (progress) => {
        hilog.info(0x0000, 'testTag', \`on progress ${JSON.stringify(progress)} \`);
      });
      task.on('completed', (progress) => {
        hilog.info(0x0000, 'testTag', \`on completed ${JSON.stringify(progress)} \`);
      });
      task.on('failed', (progress) => {
        hilog.info(0x0000, 'testTag', \`on failed ${JSON.stringify(progress)} \`);
      });
      task.on('response', (response) => {
        hilog.info(0x0000, 'testTag', \`on response ${JSON.stringify(response)} \`);
      });
      task.start((err: BusinessError) => {
        if (err) {
          hilog.error(0x0000, 'testTag',
            \`Failed to start a file download task, code: ${err.code}, message: ${err.message}\`);
        } else {
          hilog.info(0x0000, 'testTag', \`Succeeded in starting a file download task. result: ${task.tid}\`);
        }
      });
    }).catch((err: BusinessError) => {
      hilog.error(0x0000, 'testTag', \`Failed to download file, code: ${err.code}, message: ${err.message}\`);
    })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/OAi62hoaQfyo5wKXKm07jQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062102Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AED1743B8C353D0F9EF0C78A00A93913B1E3CAFEA183D078751AD0F2E26FB454)

If a file with the same name already exists locally, an error will occur during the download. You can set [DownloadParams.overwrite](https://developer.huawei.com/consumer/en/doc/harmonyos-references/cloudfoundation-cloudstorage#section14137913019) to determine whether to overwrite the local file.
