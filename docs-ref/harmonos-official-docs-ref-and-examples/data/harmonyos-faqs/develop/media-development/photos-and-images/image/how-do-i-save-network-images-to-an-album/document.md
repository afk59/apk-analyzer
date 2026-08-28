# How do I save network images to an album?

Use the **SaveButton** component to obtain temporary permission to save the image without requesting the related permission for the application. However, you must request the ohos.permission.INTERNET permission to save network images. Refer to the code snippet below.

import { http } from '@kit.NetworkKit';
import { image } from '@kit.ImageKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { photoAccessHelper } from '@kit.MediaLibraryKit';
import { fileIo as fs } from '@kit.CoreFileKit';

@Entry
@Component
struct SaveImage {
  @State pixelMap: PixelMap | undefined = undefined;

  loadImageWithUrl(url: string) {
    let responseCode = http.ResponseCode;
    let OutData: http.HttpResponse;
    let imagePackerApi = image.createImagePacker();
    let packOpts: image.PackingOption = { format: 'image/jpeg', quality: 98 };
    // Ensure that the network connection is normal.
    http.createHttp().request(url, {
      method: http.RequestMethod.GET,
      connectTimeout: 60000,
      readTimeout: 60000
    },
      async (error: BusinessError, data: http.HttpResponse) => {
        if (error) {
          console.error(\`http request failed with. Code: ${error.code}, message: ${error.message}\`);
        } else {
          OutData = data;
          let code: http.ResponseCode | number = OutData.responseCode;
          if (responseCode.OK === code) {
            let imageData: ArrayBuffer = OutData.result as ArrayBuffer;
            let imageSource: image.ImageSource = image.createImageSource(imageData);

            class tmp {
              height: number = 100
              width: number = 100
            };

            let options: Record<string, number | boolean | tmp> = {
              'alphaType': 0, // Transparency
              'editable': false, // Is it editable
              'pixelFormat': 3, // Pixel Format
              'scaleMode': 1, // Abbreviation
              'size': { height: 100, width: 100 }
            }; // Create Image Size
            imageSource.createPixelMap(options).then((pixelMap: PixelMap) => {
              this.pixelMap = pixelMap;
              this.pixelMap.getImageInfo().then((info: image.ImageInfo) => {
                console.info('info.width = ' + info.size.width);
              }).catch((err: BusinessError) => {
                console.error('Failed ' + err);
              })
              imagePackerApi.packToData(pixelMap, packOpts).then(async (buffer: ArrayBuffer) => {
                try {
                  const context = this.getUIContext().getHostContext()!;
                  let helper = photoAccessHelper.getPhotoAccessHelper(context);
                  let uri = await helper.createAsset(photoAccessHelper.PhotoType.IMAGE, 'png');
                  let file = await fs.open(uri, fs.OpenMode.READ\_WRITE | fs.OpenMode.CREATE);
                  // Write to file
                  await fs.write(file.fd, buffer);
                  this.getUIContext().getPromptAction().showToast({ message: 'Saved to album!' });
                  // Close the file
                  await fs.close(file.fd);
                } catch (error) {
                  console.error('error is ' + JSON.stringify(error));
                }
              }).catch((error: BusinessError) => {
                console.error('Failed to pack the image. And the error is: ' + error);
              }).finally(()=>{
                pixelMap.release();
              })

            })
          }
        }
      }
    )
  }

  build() {
    Row() {
      Column({ space: 10 }) {
        Image('https://agc-storage-drcn.platform.dbankcloud.cn/v0/test-rqcjj/test.png')
          .width('80%')

        SaveButton().onClick(async (event: ClickEvent, result: SaveButtonOnClickResult) => {
          if (result === SaveButtonOnClickResult.SUCCESS) {
            this.loadImageWithUrl('https://agc-storage-drcn.platform.dbankcloud.cn/v0/test-rqcjj/test.png');
          } else {
            this.getUIContext().getPromptAction().showToast({ message: 'Failed to set the permission!' });
          }
        })
      }
      .width('100%')
    }
    .height('100%')
    .backgroundColor(0xF1F3F5)
  }
}

**Reference**

[Using SaveButton](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/savebutton)

[Archived Type Data Sources](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-graphics-display#archived-type-data-sources)
