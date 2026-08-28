# Uploading a Specified File to the Cloud

You can quickly upload files from your local device to the cloud. After the upload is complete, you can go to the **Cloud Storage** page of AppGallery Connect to view the uploaded files.

#### Restrictions

This kit supports phones and tablets by default. Support for wearables is available starting from 5.1.0(18), and for TVs starting from 5.1.1(19).

#### Prerequisites

You have [initialized a storage instance](../initializing-a-storage-instance/document.md).

#### Procedure

1.  Select the file to be uploaded. In the following sample code, [photoAccessHelper.PhotoViewPicker](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-photoaccesshelper-photoviewpicker) is used to specify the file to be uploaded.
2.  Copy the file to be uploaded to the [context.cacheDir](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-context#properties) directory.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/f1gIr65QRJSpBaZu0CR2Yw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062102Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8E6D4DA84870893C25506419038441F00A3D7E40BD817165F2085B3D29DDE353)
    
    The input parameter **localPath** of the **StorageBucket.uploadFile** API can only be set to a file path in the **context.cacheDir** directory. Therefore, you need to copy the file to the **context.cacheDir** directory before uploading the file.
    
3.  Call the [StorageBucket.uploadFile](https://developer.huawei.com/consumer/en/doc/harmonyos-references/cloudfoundation-cloudstorage#section2105131521913) API to create an upload task and listen to the **progress**, **completed**, and **failed** events of the upload task.
4.  Start the upload task.

The complete sample code is as follows:

import { cloudStorage } from '@kit.CloudFoundationKit';
import { BusinessError, request } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { photoAccessHelper } from '@kit.MediaLibraryKit';
import { fileIo as fs } from '@kit.CoreFileKit';
import { GlobalContext } from '../common/GlobalContext';

let storageBucket: cloudStorage.StorageBucket = cloudStorage.bucket();

@Component
export struct testPage {
  build() {
  }

  // Upload a specified file to the cloud.
  upload() {
    this.selectPhoto().then((photoSelectResult: photoAccessHelper.PhotoSelectResult) => {
      let fileUri = photoSelectResult.photoUris\[0\];
      hilog.info(0x0000, 'testTag', \`pick file ${fileUri}\`);
      let fileName = fileUri.split('/').pop() as string;
      hilog.info(0x0000, 'testTag', \`file name ${fileName}\`);
      let cacheFile = GlobalContext.getContext().cacheDir + '/' + fileName;
      hilog.info(0x0000, 'testTag', \`cacheFile ${cacheFile}\`);
      // Copy the selected file to the **cache** directory.
      this.copyFile(fileUri, cacheFile);
      // Upload the file to the default Cloud Storage instance.
      this.uploadFile(cacheFile, \`screenshot/${fileName}\`);
    }).catch((err: BusinessError) => {
      hilog.error(0x0000, 'testTag', \`Failed to upload file, code: ${err.code}, message: ${err.message}\`);
    })
  }

  /\*\*
   \* @throws photoViewPicker select throws
   \*/
  selectPhoto(): Promise<photoAccessHelper.PhotoSelectResult> {
    // Use **photoAccessHelper** to select the specified file.
    let photoSelectOptions = new photoAccessHelper.PhotoSelectOptions();
    photoSelectOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE\_TYPE; // Set the media file type to **IMAGE**.
    photoSelectOptions.maxSelectNumber = 1; // Set the maximum number of images that can be selected.
    let photoViewPicker = new photoAccessHelper.PhotoViewPicker();
    return photoViewPicker.select(photoSelectOptions);
  }

  copyFile(srcPath: string, dstPath: string) {
    try {
      let srcFile = fs.openSync(srcPath);
      let dstFile = fs.openSync(dstPath, fs.OpenMode.READ\_WRITE | fs.OpenMode.CREATE);
      fs.copyFileSync(srcFile.fd, dstFile.fd);
      fs.closeSync(srcFile);
      fs.closeSync(dstFile);
    } catch (e) {
      hilog.error(0x0000, 'testTag', \`copy file failed ${e.message}\`);
      return;
    }
  }

  uploadFile(localPath: string, cloudPath: string) {
    storageBucket.uploadFile(GlobalContext.getContext(), {
      localPath: localPath, // Local file path, located in the **context.cacheDir** directory.
      cloudPath: cloudPath   // Cloud path. The value can be in format of _File directory/File name_ (for example, **screenshot/demo.jpg**) or _File name_.
    }).then((task: request.agent.Task) => {
      task.on('progress', (progress) => {
        hilog.info(0x0000, 'testTag', \`on progress ${JSON.stringify(progress)}\`);
      });
      task.on('completed', (progress) => {
        hilog.info(0x0000, 'testTag', \`on completed ${JSON.stringify(progress)}\`);
        // Delete temporary files in the **cache** directory.
        fs.unlink(localPath).catch((err: BusinessError) => {
          hilog.error(0x0000, 'testTag', \`Failed to unlink, code: ${err.code}, message: ${err.message}.\`);
        });
      });
      task.on('failed', (progress) => {
        hilog.info(0x0000, 'testTag', \`on failed ${JSON.stringify(progress)}\`);
        // Delete temporary files in the **cache** directory.
        fs.unlink(localPath).catch((err: BusinessError) => {
          hilog.error(0x0000, 'testTag', \`Failed to unlink, code: ${err.code}, message: ${err.message}.\`);
        });
      });
      task.on('response', (response) => {
        hilog.info(0x0000, 'testTag', \`on response ${JSON.stringify(response)}\`);
      });

        // Start the task.
      task.start((err: BusinessError) => {
        if (err) {
          hilog.error(0x0000, 'testTag',
            \`Failed to start a file upload task, code: ${err.code}, message: ${err.message}\`);
        } else {
          hilog.info(0x0000, 'testTag', \`Succeeded in starting a file upload task.\`);
        }
      });
    }).catch((err: BusinessError) => {
      hilog.error(0x0000, 'testTag', \`Failed to upload file, code: ${err.code}, message: ${err.message}\`);
    })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/huHe2HvyRx-o9s8heM802w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062102Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=252294D06EB8D0FCA956A9B043235E106F4D637178C5F11087ADA53F74CC327D)

After the upload is complete, you can sign in to [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html), select a project, and go to the **Cloud Storage** page to view the file list.
