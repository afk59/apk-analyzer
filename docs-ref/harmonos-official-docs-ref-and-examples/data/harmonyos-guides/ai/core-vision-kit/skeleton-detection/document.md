# Skeleton Detection

#### Application Scenarios

Skeleton detection detects skeleton keypoints on the human body to describe skeletal information. It is primarily used in applications such as intelligent video surveillance, patient monitoring systems, human-computer interaction, virtual reality, human animation, smart home, intelligent security, and athlete training assistance.

The supported 17 keypoints include the nose, left and right eyes, left and right ears, left and right shoulders, left and right elbows, left and right wrists, left and right hips, left and right knees, and left and right ankles.

The following figure shows an example.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/ykCcgIQVRZSj2iXKbioqMA/en-us_image_0000002382773157.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062126Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8B9B59BE6A2263FFE115C098F09A62F47E85AFB16E5B2F3039132D5578DD768B)

#### Restrictions

This capability is currently not supported on emulators.

| 
AI Capability

 | 

Restrictions

 |
| :-- | :-- |
| 

Skeleton detection

 | 

-   The input image should have a suitable imaging quality (720p or higher recommended), with a height between 100 px and 10,000 px, a width between 100 px and 10,000 px, and a height-to-width ratio preferably below 5:1 (the height must be less than 5 times of the width), ideally close to the height-to-width ratio of a smartphone screen.

 |

#### Development Procedure

1.  Add the classes for implementing skeleton detection to a project.
    
    import { image } from '@kit.ImageKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    import { fileIo } from '@kit.CoreFileKit';
    import { skeletonDetection, visionBase } from '@kit.CoreVisionKit';
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
        hilog.error(0x0000, 'skeletonDetectSample', "Failed to define uri.");
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
          hilog.error(0x0000, 'skeletonDetectSample', \`Failed to get photo image uri. code: ${err.code}, message: ${err.message}\`);
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
    
4.  Instantiate the **Request** object and pass [PixelMap](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-image-pixelmap) of the image to be detected to implement skeleton detection.
    
    // Call the skeleton detection API.
    let request: visionBase.Request = {
      inputData: { pixelMap: this.chooseImage }
    };
    let data: skeletonDetection.SkeletonDetectionResponse = await (await skeletonDetection.SkeletonDetector.create()).process(request);
    
5.  (Optional) To display the result on the UI, use the following code:
    
    let data: skeletonDetection.SkeletonDetectionResponse = await (await skeletonDetection.SkeletonDetector.create()).process(request);
    let poseJson = JSON.stringify(data);
    hilog.info(0x0000, 'skeletonDetectSample', \`Succeeded in skeleton detection: ${poseJson}\`);
    this.dataValues = poseJson;
    

#### Development Example

## Index.ets

import { image } from '@kit.ImageKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';
import { skeletonDetection, visionBase } from '@kit.CoreVisionKit';
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

      Button('Start skeleton detection')
        .type(ButtonType.Capsule)
        .fontColor(Color.White)
        .alignSelf(ItemAlign.Center)
        .width('80%')
        .margin(10)
        .onClick(async () => {
          if(!this.chooseImage) {
            hilog.error(0x0000, 'skeletonDetectSample', \`Failed to choose image.\`);
            return;
          }
          // Call the skeleton detection API.
          let request: visionBase.Request = {
            inputData: { pixelMap: this.chooseImage }
          };
          try {
            let data: skeletonDetection.SkeletonDetectionResponse =
              await (await skeletonDetection.SkeletonDetector.create()).process(request);
            let poseJson = JSON.stringify(data);
            hilog.info(0x0000, 'skeletonDetectSample', \`Succeeded in skeleton detection: ${poseJson}\`);
            this.dataValues = poseJson;
          } catch (error) {
            hilog.error(0x0000, 'skeletonDetectSample', \`Failed to get result. Error: ${error}\`);
          }
        })
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }

  private async selectImage() {
    let uri = await this.openPhoto()
    if (uri === undefined) {
      hilog.error(0x0000, 'skeletonDetectSample', "Failed to define uri.");
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
        hilog.error(0x0000, 'skeletonDetectSample', \`Failed to get photo image uri. code: ${err.code}, message: ${err.message}\`);
        reject('')
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
        hilog.error(0x0000, 'skeletonDetectSample', \`Failed to open file. Error: ${error}\`);
      }
    }, 100)
  }
}
