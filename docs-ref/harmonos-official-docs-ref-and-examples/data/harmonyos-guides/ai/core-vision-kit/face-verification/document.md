# Face Verification

#### Application Scenarios

Face verification compares two input images and determines whether the two faces in the images are of the same person. If so, the system shows that they are the same person, with a high confidence score. If not, the system shows that they are different people, with a low confidence score. This can be used in app scenarios that require face comparison, such as comparing the similarity between two people or the similarity between a person and a celebrity in entertainment apps.

The following figure shows an example.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/xk1MvbbDSeKa9cDYjy-kBQ/en-us_image_0000002348932986.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062126Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3C5899E98F3A7783A1C4056E7FB9070D595ED74891DC432C52CB0924B3647563)

#### Restrictions

This capability is currently not supported on emulators.

| 
AI Capability

 | 

Restrictions

 |
| :-- | :-- |
| 

Face verification

 | 

-   Currently, only one-to-one face comparison is supported.
-   Both input images should have a suitable imaging quality (720p or higher recommended), with a height between 224 px and 15,210 px, a width between 100 px and 10,000 px, and a height-to-width ratio preferably below 10:1 (the height must be less than 10 times of the width), ideally close to the height-to-width ratio of a smartphone screen.

 |

#### Development Procedure

1.  Add the classes for implementing face verification to a project.
    
    import { faceComparator } from '@kit.CoreVisionKit';
    import { image } from '@kit.ImageKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    import { fileIo } from '@kit.CoreFileKit';
    import { photoAccessHelper } from '@kit.MediaLibraryKit';
    
2.  Configure a simple UI layout and add a tap event to the **Button** component to bring up the gallery for selecting images.
    
    Button('Select images')
      .type(ButtonType.Capsule)
      .fontColor(Color.White)
      .alignSelf(ItemAlign.Center)
      .width('80%')
      .margin(10)
      .onClick(() => {
        // Bring up the gallery to obtain images.
        this.selectImage();
      })
    
3.  Obtain images from the gallery, convert the images into [PixelMap](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-image-pixelmap), and add the initialization and release methods.
    
    async aboutToAppear(): Promise<void> {
      const initResult = await faceComparator.init();
      hilog.info(0x0000, TAG, \`Face comparator initialization result:${initResult}\`);
    }
    
    async aboutToDisappear(): Promise<void> {
      await faceComparator.release();
      hilog.info(0x0000, TAG, 'Face comparator released successfully');
    }
    
    private async selectImage() {
      let uri = await this.openPhoto()
      if (uri === undefined) {
        hilog.error(0x0000, 'faceCompare', "Failed to get two image uris.");
      }
      this.loadImage(uri);
    }
    
    private openPhoto(): Promise<string\[\]> {
      return new Promise<string\[\]>((resolve, reject) => {
        let photoPicker: photoAccessHelper.PhotoViewPicker = new photoAccessHelper.PhotoViewPicker();
        photoPicker.select({
          MIMEType: photoAccessHelper.PhotoViewMIMETypes.IMAGE\_TYPE,
          maxSelectNumber: 2
        }).then(res => {
          resolve(res.photoUris);
        }).catch((err: BusinessError) => {
          hilog.error(0x0000, TAG, \`Failed to get photo image uris. code: ${err.code}, message: ${err.message}\`);
          reject();
        });
      });
    }
    
    private loadImage(names: string\[\]) {
      setTimeout(async () => {
        let imageSource: image.ImageSource | undefined = undefined;
        let fileSource = await fileIo.open(names\[0\], fileIo.OpenMode.READ\_ONLY);
        imageSource = image.createImageSource(fileSource.fd);
        this.chooseImage = await imageSource.createPixelMap();
        fileSource = await fileIo.open(names\[1\], fileIo.OpenMode.READ\_ONLY);
        imageSource = image.createImageSource(fileSource.fd);
        this.chooseImage1 = await imageSource.createPixelMap();
      }, 100
      )
    }
    
4.  Implement the face verification function. Instantiate the [VisionInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/core-vision-facecomparator-api#section674171818172) objects, pass [PixelMap](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-image-pixelmap) of the two images, and call the [faceComparator.compareFaces](https://developer.huawei.com/consumer/en/doc/harmonyos-references/core-vision-facecomparator-api#section16178105410532) method to compare faces.
    
    // Call the face verification API.
    let visionInfo: faceComparator.VisionInfo = {
      pixelMap: this.chooseImage,
    };
    let visionInfo1: faceComparator.VisionInfo = {
      pixelMap: this.chooseImage1,
    };
    let data:faceComparator.FaceCompareResult = await faceComparator.compareFaces(visionInfo, visionInfo1);
    
5.  (Optional) To display the result on the UI, use the following code:
    
    let data:faceComparator.FaceCompareResult = await faceComparator.compareFaces(visionInfo, visionInfo1);
    let faceString = "degree of similarity: "+ this.toPercentage(data.similarity)+((data.isSamePerson)?". is":". no")+ " same person";
    hilog.info(0x0000, 'testTag', "faceString data is " + faceString);
    this.dataValues = faceString;
    

#### Development Example

## Index.ets

import { faceComparator } from '@kit.CoreVisionKit';
import { image } from '@kit.ImageKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';
import { photoAccessHelper } from '@kit.MediaLibraryKit';

const TAG: string = "FaceCompareSample";

@Entry
@Component
struct Index {
  @State chooseImage: PixelMap | undefined = undefined
  @State chooseImage1: PixelMap | undefined = undefined
  @State dataValues: string = ''

  async aboutToAppear(): Promise<void> {
    const initResult = await faceComparator.init();
    hilog.info(0x0000, TAG, \`Face comparator initialization result:${initResult}\`);
  }

  async aboutToDisappear(): Promise<void> {
    await faceComparator.release();
    hilog.info(0x0000, TAG, 'Face comparator released successfully');
  }

  build() {
    Column() {
      Image(this.chooseImage)
        .objectFit(ImageFit.Fill)
        .height('30%')
        .accessibilityDescription("Default image 1")
      Image(this.chooseImage1)
        .objectFit(ImageFit.Fill)
        .height('30%')
        .accessibilityDescription("Default image 2")
      Text(this.dataValues)
        .copyOption(CopyOptions.LocalDevice)
        .height('15%')
        .margin(10)
        .width('60%')
      Button('Select images')
        .type(ButtonType.Capsule)
        .fontColor(Color.White)
        .alignSelf(ItemAlign.Center)
        .width('80%')
        .margin(10)
        .onClick(() => {
          // Bring up the gallery.
          this.selectImage()
        })
      Button('Compare faces')
        .type(ButtonType.Capsule)
        .fontColor(Color.White)
        .alignSelf(ItemAlign.Center)
        .width('80%')
        .margin(10)
        .onClick(() => {
          if(!this.chooseImage || !this.chooseImage1) {
            hilog.error(0x0000, TAG, "Failed to choose image");
            return;
          }
          // Call the face verification API.
          let visionInfo: faceComparator.VisionInfo = {
            pixelMap: this.chooseImage,
          };
          let visionInfo1: faceComparator.VisionInfo = {
            pixelMap: this.chooseImage1,
          };
          faceComparator.compareFaces(visionInfo, visionInfo1)
            .then((data: faceComparator.FaceCompareResult) => {
              let faceString = "degree of similarity: "+ this.toPercentage(data.similarity)+((data.isSamePerson)?". is":". no")+ " same person";
              hilog.info(0x0000, TAG, "faceString data is " + faceString);
              this.dataValues = faceString;
            })
            .catch((error: BusinessError) => {
              hilog.error(0x0000, TAG, \`Face comparison failed. Code: ${error.code}, message: ${error.message}\`);
              this.dataValues = \`Error: ${error.message}\`;
            });
        })
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }

  private toPercentage(num: number): string {
    return \`${(num \* 100).toFixed(2)}%\`;
  }

  private async selectImage() {
    let uri = await this.openPhoto()
    if (uri === undefined) {
      hilog.error(0x0000, TAG, "Failed to get two image uris.");
    }
    this.loadImage(uri);
  }

  private openPhoto(): Promise<string\[\]> {
    return new Promise<string\[\]>((resolve, reject) => {
      let photoPicker: photoAccessHelper.PhotoViewPicker = new photoAccessHelper.PhotoViewPicker();
      photoPicker.select({
        MIMEType: photoAccessHelper.PhotoViewMIMETypes.IMAGE\_TYPE,
        maxSelectNumber: 2
      }).then(res => {
        resolve(res.photoUris);
      }).catch((err: BusinessError) => {
        hilog.error(0x0000, TAG, \`Failed to get photo image uris. code: ${err.code}, message: ${err.message}\`);
        reject();
      });
    });
  }

  private loadImage(names: string\[\]) {
    setTimeout(async () => {
      let imageSource: image.ImageSource | undefined = undefined;
      let fileSource: fileIo.File
      try {
        fileSource = await fileIo.open(names\[0\], fileIo.OpenMode.READ\_ONLY);
        imageSource = image.createImageSource(fileSource.fd);
        this.chooseImage = await imageSource.createPixelMap();
      } catch (error) {
        hilog.error(0x0000, TAG, \`Failed to open file. Error: ${error}\`);
      }
      try {
        fileSource = await fileIo.open(names\[1\], fileIo.OpenMode.READ\_ONLY);
        imageSource = image.createImageSource(fileSource.fd);
        this.chooseImage1 = await imageSource.createPixelMap();
        await fileIo.close(fileSource);
      } catch (error) {
        hilog.error(0x0000, TAG, \`Failed to open the second file. Error: ${error}\`);
      }
    }, 100
    )
  }
}
