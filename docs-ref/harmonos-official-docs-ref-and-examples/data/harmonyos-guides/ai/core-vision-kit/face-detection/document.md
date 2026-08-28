# Face Detection

#### Application Scenarios

Face detection detects faces in images and returns high-precision bounding box coordinates, facial landmark positions, facial orientation, and confidence scores. By locating faces, this capability enables precise beautification and modification of specific facial features. It is widely used in various facial recognition scenarios, such as face clustering and beauty enhancement.

The following figure shows an example.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/PzpaF94HTSisT0eUJFGTJg/en-us_image_0000002382773153.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062126Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C993FA9B589220E654F61F644171D2D612B70CE99AC64CCCBB099AEACF697D9C)

#### Restrictions

This capability is currently not supported on emulators.

| 
AI Capability

 | 

Restrictions

 |
| :-- | :-- |
| 

Face detection

 | 

-   The input image should have a suitable imaging quality (720p or higher recommended), with a height between 224 px and 15,210 px, a width between 100 px and 10,000 px, and a height-to-width ratio preferably below 10:1 (the height must be less than 10 times of the width), ideally close to the height-to-width ratio of a smartphone screen.
-   It is not suitable for real-time detection because the API call takes a long period of time.
-   Only one thread is allowed per user.

 |

#### World Coordinate System

The following image shows the coordinate system used for representing face orientation.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/BFlirNKAQsyIKfDsjAZkNg/en-us_image_0000002336286446.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062126Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3675ABCF34F3408D4EE52D9BEBD05261457A1F489ED2C0F97C8DF05A0CE5C0A4)

#### Development Procedure

1.  Add the classes for implementing face detection to a project.
    
    import { faceDetector } from '@kit.CoreVisionKit';
    import { image } from '@kit.ImageKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    import { fileIo } from '@kit.CoreFileKit';
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
        hilog.error(0x0000, 'faceDetector', "Failed to get uri.");
      }
      this.loadImage(uri)
    }
    
    private openPhoto(): Promise<string> {
      return new Promise<string>((resolve) => {
        let photoPicker: photoAccessHelper.PhotoViewPicker = new photoAccessHelper.PhotoViewPicker();
        photoPicker.select({
          MIMEType: photoAccessHelper.PhotoViewMIMETypes.IMAGE\_TYPE, 
          maxSelectNumber: 1
        }).then(res => {
          resolve(res.photoUris\[0\])
        }).catch((err: BusinessError) => {
          hilog.error(0x0000, 'faceDetector', \`Failed to get photo image uri.code: ${err.code}, message: ${err.message}\`);
          resolve('');
        })
      })
    }
    
    private loadImage(name: string) {
      setTimeout(async () => {
        let imageSource: image.ImageSource | undefined = undefined;
        let fileSource = await fileIo.open(name, fileIo.OpenMode.READ\_ONLY);
        imageSource = image.createImageSource(fileSource.fd);
        this.chooseImage = await imageSource.createPixelMap();
        this.dataValues = "";
      }, 100
      )
    }
    
4.  Instantiate the [VisionInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/core-vision-face-detector-api#section14488135133518) object and pass [PixelMap](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-image-pixelmap) of the image to be detected to implement face detection.
    
    // Initialize the face detection service and call the face detection API.
    faceDetector.init();
    let visionInfo: faceDetector.VisionInfo = {
      pixelMap: this.chooseImage,
    };
    let data:faceDetector.Face\[\] = await faceDetector.detect(visionInfo);
    
5.  (Optional) To display the result on the UI, use the following code:
    
    let data:faceDetector.Face\[\] = await faceDetector.detect(visionInfo);
    if (data.length === 0) {
      this.dataValues = "No face is detected in the image. Select an image that contains a face.";
    } else {
      let faceString = JSON.stringify(data);
      hilog.info(0x0000, 'testTag', "faceString data is " + faceString);
      this.dataValues = faceString;
    }
    

#### Development Example

## Index.ets

import { faceDetector } from '@kit.CoreVisionKit';
import { image } from '@kit.ImageKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';
import { photoAccessHelper } from '@kit.MediaLibraryKit';

@Entry
@Component
struct Index {
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
      Button('Detect face')
        .type(ButtonType.Capsule)
        .fontColor(Color.White)
        .alignSelf(ItemAlign.Center)
        .width('80%')
        .margin(10)
        .onClick(() => {
          if(!this.chooseImage) {
            hilog.error(0x0000, 'faceDetectorSample', "Failed to detect face.");
            return;
          }
          // Call the face detection API.
          faceDetector.init();
          let visionInfo: faceDetector.VisionInfo = {
            pixelMap: this.chooseImage,
          };
          faceDetector.detect(visionInfo)
            .then((data: faceDetector.Face\[\]) => {
              if (data.length === 0) {
                this.dataValues = "No face is detected in the image. Select an image that contains a face.";
              } else {
                let faceString = JSON.stringify(data);
                hilog.info(0x0000, 'faceDetectorSample', "faceString data is " + faceString);
                this.dataValues = faceString;
              }
            })
            .catch((error: BusinessError) => {
              hilog.error(0x0000, 'faceDetectorSample', \`Face detection failed. Code: ${error.code}, message: ${error.message}\`);
              this.dataValues = \`Error: ${error.message}\`;
            });
          faceDetector.release();
        })
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }

  private async selectImage() {
    let uri = await this.openPhoto()
    if (uri === undefined) {
      hilog.error(0x0000, 'faceDetectorSample', "Failed to get uri.");
    }
    this.loadImage(uri);
  }

  private openPhoto(): Promise<string> {
    return new Promise<string>((resolve) => {
      let photoPicker: photoAccessHelper.PhotoViewPicker = new photoAccessHelper.PhotoViewPicker();
      photoPicker.select({
        MIMEType: photoAccessHelper.PhotoViewMIMETypes.IMAGE\_TYPE,
        maxSelectNumber: 1
      }).then(res => {
        resolve(res.photoUris\[0\])
      }).catch((err: BusinessError) => {
        hilog.error(0x0000, 'faceDetectorSample', \`Failed to get photo image uri.code: ${err.code}, message: ${err.message}\`);
        resolve('');
      })
    })
  }

  private loadImage(name: string) {
    setTimeout(async () => {
      let imageSource: image.ImageSource | undefined = undefined;
      try {
        let fileSource = await fileIo.open(name, fileIo.OpenMode.READ\_ONLY);
        imageSource = image.createImageSource(fileSource.fd);
        this.chooseImage = await imageSource.createPixelMap();
        this.dataValues = "";
        await fileIo.close(fileSource);
      } catch (error) {
        hilog.error(0x0000, 'faceDetectorSample', \`Failed to open file. Error: ${error}\`);
      }
    }, 100
    )
  }
}
