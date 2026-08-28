# Multi-object Detection

#### Application Scenarios

Multi-object detection detects various objects in a given image (including landscapes, animals, plants, buildings, faces, tables, and texts) and highlights the positions of these objects using boxes.

The following figure shows an example.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/5tmPO7aLQP6wC_z1UgQQMA/en-us_image_0000002349092750.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062126Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FF75C815B7AEC94477FC8AAC8474340F8055A2C84A3EC33E8E6124CA7BA37818)

#### Restrictions

This capability is currently not supported on emulators.

| 
AI Capability

 | 

Restrictions

 |
| :-- | :-- |
| 

Multi-object detection

 | 

-   The input image should have a suitable imaging quality (720p or higher recommended), with a height between 100 px and 10,000 px, a width between 100 px and 10,000 px, and a height-to-width ratio preferably below 5:1 (the height must be less than 5 times of the width), ideally close to the height-to-width ratio of a smartphone screen.
-   The object's size must account for more than 0.1% of the total image area.

 |

#### Development Procedure

1.  Add the classes for implementing multi-object detection to a project.
    
    import { image } from '@kit.ImageKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    import { fileIo } from '@kit.CoreFileKit';
    import { objectDetection, visionBase } from '@kit.CoreVisionKit';
    import { photoAccessHelper } from '@kit.MediaLibraryKit';
    
2.  Configure a simple UI layout and add a tap event to the **Button** component to bring up the gallery for selecting images.
    
    Button('Select image')
      .type(ButtonType.Capsule)
      .fontColor(Color.White)
      .alignSelf(ItemAlign.Center)
      .width('80%')
      .margin(10)
      .onClick(() => {
        // Bring up the gallery to obtain images.
        this.selectImage();
      })
    
3.  Obtain an image from the gallery and convert the image into [PixelMap](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-image-pixelmap).
    
    private async selectImage() {
      let uri = await this.openPhoto()
      if (uri === undefined) {
        hilog.error(0x0000, 'objectDetectSample', "Failed to define uri.");
      }
      this.loadImage(uri)
    }
    
    private openPhoto(): Promise<string> {
      return new Promise<string>((resolve, reject) => {
        let photoPicker: photoAccessHelper.PhotoViewPicker = new photoAccessHelper.PhotoViewPicker();
        photoPicker.select({
          MIMEType: photoAccessHelper.PhotoViewMIMETypes.IMAGE\_TYPE, maxSelectNumber: 1
        }).then(res => {
          resolve(res.photoUris\[0\])
        }).catch((err: BusinessError) => {
          hilog.error(0x0000, 'objectDetectSample', \`Failed to get photo image uri. code: ${err.code}, message: ${err.message}\`);
          reject('')
        })
      })
    }
    
    private loadImage(name: string) {
      setTimeout(async () => {
        let fileSource = await fileIo.open(name, fileIo.OpenMode.READ\_ONLY);
        this.imageSource = image.createImageSource(fileSource.fd);
        this.chooseImage = await this.imageSource.createPixelMap();
      }, 100)
    }
    
4.  Instantiate the **Request** object and pass [PixelMap](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-image-pixelmap) of the image to be detected to implement multi-object detection.
    
    // Call the multi-object detection API.
    let request: visionBase.Request = {
      inputData: { pixelMap: this.chooseImage }
    };
    let data: objectDetection.ObjectDetectionResponse = await (await objectDetection.ObjectDetector.create()).process(request);
    
5.  (Optional) To display the result on the UI, use the following code:
    
    let objectJson = JSON.stringify(data);
    hilog.info(0x0000, 'objectDetectSample', \`Succeeded in object detection: ${objectJson}\`);
    this.dataValues = objectJson;
    

#### Development Example

## Index.ets

import { image } from '@kit.ImageKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';
import { objectDetection, visionBase } from '@kit.CoreVisionKit';
import { photoAccessHelper } from '@kit.MediaLibraryKit';

@Entry
@Component
struct Index {
  private imageSource: image.ImageSource | undefined = undefined;
  @State chooseImage: PixelMap | undefined = undefined
  @State dataValues: string = ''

  build() {
    Column() {
      Image(this.chooseImage)
        .objectFit(ImageFit.Fill)
        .height('60%')

      Text(this.dataValues)
        .copyOption(CopyOptions.LocalDevice)
        .height('15%')
        .margin(10)
        .width('60%')

      Button('Select image')
        .type(ButtonType.Capsule)
        .fontColor(Color.White)
        .alignSelf(ItemAlign.Center)
        .width('80%')
        .margin(10)
        .onClick(() => {
          // Bring up the gallery.
          this.selectImage()
        })

      Button('Start multi-object detection')
        .type(ButtonType.Capsule)
        .fontColor(Color.White)
        .alignSelf(ItemAlign.Center)
        .width('80%')
        .margin(10)
        .onClick(async () => {
          if(!this.chooseImage) {
            hilog.error(0x0000, 'objectDetectSample', \`Failed to choose image.\`);
            return;
          }
          let request: visionBase.Request = {
            inputData: { pixelMap: this.chooseImage }
          };
          try {
            let data: objectDetection.ObjectDetectionResponse =
              await (await objectDetection.ObjectDetector.create()).process(request);
            let objectJson = JSON.stringify(data);
            hilog.info(0x0000, 'objectDetectSample', \`Succeeded in object detection: ${objectJson}\`);
            this.dataValues = objectJson;
          } catch (error) {
            hilog.error(0x0000, 'objectDetectSample', \`Failed to get result. Error: ${error}\`);
          }
        })
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }

  private async selectImage() {
    try {
      let uri = await this.openPhoto();
      if (uri === undefined) {
        hilog.error(0x0000, 'objectDetectSample', "Failed to define uri.");
        return;
      }
      this.loadImage(uri);
    } catch (err) {
      hilog.error(0x0000, 'objectDetectSample', \`Failed to get photo image uri. code: ${err.code}, message: ${err.message}\`);
    }
  }

  private openPhoto(): Promise<string> {
    return new Promise<string>((resolve, reject) => {
      let photoPicker: photoAccessHelper.PhotoViewPicker = new photoAccessHelper.PhotoViewPicker();
      photoPicker.select({
        MIMEType: photoAccessHelper.PhotoViewMIMETypes.IMAGE\_TYPE, maxSelectNumber: 1
      }).then(res => {
        resolve(res.photoUris\[0\]);
      }).catch((err: BusinessError) => {
        hilog.error(0x0000, 'objectDetectSample', \`Failed to get photo image uri. code: ${err.code}, message: ${err.message}\`);
        reject(err);
      })
    })
  }

  private loadImage(name: string) {
    setTimeout(async () => {
      try {
        let fileSource = await fileIo.open(name, fileIo.OpenMode.READ\_ONLY);
        this.imageSource = image.createImageSource(fileSource.fd);
        this.chooseImage = await this.imageSource.createPixelMap();
        await fileIo.close(fileSource);
      } catch (error) {
        hilog.error(0x0000, 'objectDetectSample', \`Failed to open file. Error: ${error}\`);
      }
    }, 100)
  }
}
