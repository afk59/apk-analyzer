# How do I select an image from Gallery and upload it to the server?

You need to apply for the **ohos.permission.INTERNET** permission to upload images to the server.

The sample code is as follows:

import { request } from '@kit.BasicServicesKit';
import { fileIo as fs } from '@kit.CoreFileKit';
import { photoAccessHelper } from '@kit.MediaLibraryKit';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct Index {
  private openPhotoPicker() {
    // Obtain the application file path 
    let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
    let cacheDir = context.cacheDir;
    let photoPicker = new photoAccessHelper.PhotoViewPicker();
    photoPicker.select({
      MIMEType: photoAccessHelper.PhotoViewMIMETypes.IMAGE\_TYPE,
      maxSelectNumber: 1
    }, (\_, result) => {
      if (result) {
        result.photoUris.forEach((uri) => {
          let file = fs.openSync(uri, fs.OpenMode.CREATE);
          // Copy the file to the cache directory
          fs.copyFileSync(file.fd, cacheDir + '/test.jpeg');
          this.uploadImage(\['internal://cache/test.jpeg'\]);
        })
      }
    })
  }

  private uploadImage(paths: string\[\]) {
    let allFiles = Array<request.File>();
    let header = new Map<Object, string>();
    header.set('Content-Type', 'multipart/form-data');
    header.set('key2', 'value2');
    for (let i = 0; i < paths.length; i++) {
      allFiles\[i\] = {
        name: 'image' + i + '.jpeg',
        filename: 'image' + i + '.jpeg',
        uri: paths\[i\],
        type: 'image'
      }
    }
    let data: Array<request.RequestData> = \[{ name: 'name', value: 'value' }\];
    let uploadConfig: request.UploadConfig = {
      url: 'http://XXX&#34',
      header: header,
      method: 'POST',
      files: allFiles,
      data: data
    }
    try {
      request.uploadFile(this.getUIContext().getHostContext(), uploadConfig, (error, uploadTask) => {
        if (uploadTask) {
          uploadTask.on('progress', (uploadSize: number, totalSize: number) => {
            console.info('progress,uploadedSize:' + uploadSize + ',totalSize:' + totalSize);
          })
        } else {
          console.info('upload failure:' + error);
        }
      })
    } catch (error) {
      console.info('upload failure:' + error);
    }
  }

  build() {
    Column() {
      Button ('Select an image for uploading')
        .width('100%')
        .onClick(() => {
          this.openPhotoPicker();
        })
    }
    .width('100%')
    .height('100%')
    .padding(16)
    .justifyContent(FlexAlign.End)
  }
}
