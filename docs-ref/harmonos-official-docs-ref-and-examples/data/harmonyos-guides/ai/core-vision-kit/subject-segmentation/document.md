# Subject Segmentation

#### Application Scenarios

Subject segmentation identifies and isolates foreground objects or regions (that is, salient subjects) that are distinct from the background in an image. It is suitable for scenarios requiring the recognition and extraction of the main information within an image and is widely used in foreground object detection and foreground subject separation tasks. Here are some examples:

-   Sticker creation: Extracts salient foreground objects from an image by removing the background.
-   Background replacement: Replaces the background of an image with a new one while preserving foreground objects.
-   Saliency detection: Quickly locates the most visually prominent regions in an image.
-   Assisted image editing: Facilitates image editing tasks, such as beautifying a foreground object separately.

The following figure shows an example.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/XgZBsyWHT4e6qPPv4nuDYQ/en-us_image_0000002382653433.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062126Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9E13914229462D5A787DCEC8CCD41E6B37D3B0320B01AF1B5C0873C4777F1F45)

#### Restrictions

This capability is currently not supported on emulators.

| 
AI Capability

 | 

Restrictions

 |
| :-- | :-- |
| 

Subject segmentation

 | 

-   An object will only be recognized as a "subject" and segmented from an image if it occupies at least 0.5% of the original image area.
-   It is not recommended to use this capability for images containing a large amount of text.
-   The input image should have a suitable imaging quality (720p or higher recommended), with a height between 20 px and 9000 px, a width between 20 px and 9000 px, and a height-to-width ratio preferably below 3:1 (the height must be less than 3 times of the width), ideally close to the height-to-width ratio of a smartphone screen.

 |

#### Development Procedure

1.  Reference related classes and add them to a project.
    
    import { subjectSegmentation } from '@kit.CoreVisionKit';
    import { image } from '@kit.ImageKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    import { fileIo } from '@kit.CoreFileKit';
    import { photoAccessHelper } from '@kit.MediaLibraryKit';
    
2.  Prepare an image, convert the image into [PixelMap](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-image-pixelmap), and add the initialization and release methods.
    
    async aboutToAppear(): Promise<void> {
      const initResult = await subjectSegmentation.init();
      hilog.info(0x0000, 'subjectSegmentationSample', \`Subject segmentation initialization result:${initResult}\`);
    }
    
    async aboutToDisappear(): Promise<void> {
      await subjectSegmentation.release();
      hilog.info(0x0000, 'subjectSegmentationSample', 'Subject segmentation released successfully');
    }
    
    private async selectImage() {
      let uri = await this.openPhoto()
      if (uri === undefined) {
        hilog.error(0x0000, TAG, "uri is undefined");
      }
      this.loadImage(uri);
    }
    
    private openPhoto(): Promise<Array<string>> {
      return new Promise<Array<string>>((resolve, reject) => {
        let PhotoSelectOptions = new photoAccessHelper.PhotoSelectOptions();
        PhotoSelectOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE\_TYPE;
        PhotoSelectOptions.maxSelectNumber = 1;
        let photoPicker: photoAccessHelper.PhotoViewPicker = new photoAccessHelper.PhotoViewPicker();
        hilog.info(0x0000, TAG, 'PhotoViewPicker.select successfully, PhotoSelectResult uri: ');
        photoPicker.select(PhotoSelectOptions).then((PhotoSelectResult) => {
          hilog.info(0x0000, TAG, \`PhotoViewPicker.select successfully, PhotoSelectResult uri: ${PhotoSelectResult.photoUris}\`);
          resolve(PhotoSelectResult.photoUris)
        }).catch((err: BusinessError) => {
          hilog.error(0x0000, TAG, \`PhotoViewPicker.select failed with errCode: ${err.code}, errMessage: ${err.message}\`);
          reject();
        });
      })
    }
    
    private loadImage(names: string\[\]) {
      setTimeout(async () => {
        let imageSource: image.ImageSource | undefined = undefined
        let fileSource = await fileIo.open(names\[0\], fileIo.OpenMode.READ\_ONLY)
        imageSource = image.createImageSource(fileSource.fd)
        this.chooseImage = await imageSource.createPixelMap()
      }, 100
      )
    }
    
3.  Instantiate the input parameter [VisionInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/core-vision-subjectsegmentation-api#section674171818172) of the image for subject segmentation and pass [PixelMap](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-image-pixelmap) of the image.
    
    let visionInfo: subjectSegmentation.VisionInfo = {
      pixelMap: this.chooseImage,
    };
    
4.  Set [SegmentationConfig](https://developer.huawei.com/consumer/en/doc/harmonyos-references/core-vision-subjectsegmentation-api#section1268211401742) for subject segmentation, including the maximum number of segmented subjects, whether to output the segmentation information about each subject, and whether to output the segmented foreground image.
    
    let config: subjectSegmentation.SegmentationConfig = {
      maxCount: parseInt(this.maxNum),
      enableSubjectDetails: true,
      enableSubjectForegroundImage: true,
    };
    
5.  Call the [subjectSegmentation.doSegmentation](https://developer.huawei.com/consumer/en/doc/harmonyos-references/core-vision-subjectsegmentation-api#section3410243584) API of **subjectSegmentation** to implement subject segmentation.
    
    let data: subjectSegmentation.SegmentationResult = await subjectSegmentation.doSegmentation(visionInfo, config);
    let outputString = \`Subject count: ${data.subjectCount}\\n\`;
    outputString += \`Max subject count: ${config.maxCount}\\n\`;
    outputString += \`Enable subject details: ${config.enableSubjectDetails ? 'Yes' : 'No'}\\n\\n\`;
    let segBox : subjectSegmentation.Rectangle = data.fullSubject.subjectRectangle;
    let segBoxString = \`Full subject box:\\nLeft: ${segBox.left}, Top: ${segBox.top}, Width: ${segBox.width}, Height: ${segBox.height}\\n\\n\`;
    outputString += segBoxString;
    
    if (config.enableSubjectDetails) {
      outputString += 'Individual subject boxes:\\n';
      if (data.subjectDetails) {
        for (let i = 0; i < data.subjectDetails.length; i++) {
          let detailSegBox: subjectSegmentation.Rectangle = data.subjectDetails\[i\].subjectRectangle;
          outputString += \`Subject ${i + 1}:\\nLeft: ${detailSegBox.left}, Top: ${detailSegBox.top}, Width: ${detailSegBox.width}, Height: ${detailSegBox.height}\\n\\n\`;
        }
      }
    }
    

#### Development Example

## Index.ets

import { subjectSegmentation } from '@kit.CoreVisionKit';
import { image } from '@kit.ImageKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';
import { photoAccessHelper } from '@kit.MediaLibraryKit';

const TAG: string = "ImageSegmentationSample";

@Entry
@Component
struct Index {
  @State chooseImage: PixelMap | undefined = undefined
  @State dataValues: string = ''
  @State segmentedImage: PixelMap | undefined = undefined
  @State maxNum: string = '20'

  build() {
    Column() {
      Image(this.chooseImage)
        .objectFit(ImageFit.Fill)
        .height('30%')
        .accessibilityDescription("Image to be segmented")

      Scroll() {
        Text(this.dataValues)
          .copyOption(CopyOptions.LocalDevice)
          .margin(10)
          .width('100%')
      }
      .height('20%')

      Image(this.segmentedImage)
        .objectFit(ImageFit.Fill)
        .height('30%')
        .accessibilityDescription("Segmented subject image")

      Row() {
        Text('Max subject count:')
          .fontSize(16)
        TextInput({ placeholder: 'Enter max subject count', text: this.maxNum })
          .type(InputType.Number)
          .placeholderColor(Color.Gray)
          .fontSize(16)
          .backgroundColor(Color.White)
          .onChange((value: string) => {
            this.maxNum = value
          })
      }
      .width('80%')
      .margin(10)

      Button('Select image')
        .type(ButtonType.Capsule)
        .fontColor(Color.White)
        .alignSelf(ItemAlign.Center)
        .width('80%')
        .margin(10)
        .onClick(() => {
          this.selectImage()
        })

      Button('Image Segmentation')
        .type(ButtonType.Capsule)
        .fontColor(Color.White)
        .alignSelf(ItemAlign.Center)
        .width('80%')
        .margin(10)
        .onClick(() => {
          if (!this.chooseImage) {
            hilog.error(0x0000, TAG, "imageSegmentation not have chooseImage");
            return
          }
          let visionInfo: subjectSegmentation.VisionInfo = {
            pixelMap: this.chooseImage,
          };
          let config: subjectSegmentation.SegmentationConfig = {
            maxCount: parseInt(this.maxNum),
            enableSubjectDetails: true,
            enableSubjectForegroundImage: true,
          };
          subjectSegmentation.doSegmentation(visionInfo, config)
            .then((data: subjectSegmentation.SegmentationResult) => {
              let outputString = \`Subject count: ${data.subjectCount}\\n\`;
              outputString += \`Max subject count: ${config.maxCount}\\n\`;
              outputString += \`Enable subject details: ${config.enableSubjectDetails ? 'Yes' : 'No'}\\n\\n\`;
              let segBox : subjectSegmentation.Rectangle = data.fullSubject.subjectRectangle;
              let segBoxString = \`Full subject box:\\nLeft: ${segBox.left}, Top: ${segBox.top}, Width: ${segBox.width}, Height: ${segBox.height}\\n\\n\`;
              outputString += segBoxString;

              if (config.enableSubjectDetails) {
                outputString += 'Individual subject boxes:\\n';
                if (data.subjectDetails) {
                  for (let i = 0; i < data.subjectDetails.length; i++) {
                    let detailSegBox: subjectSegmentation.Rectangle = data.subjectDetails\[i\].subjectRectangle;
                    outputString += \`Subject ${i + 1}:\\nLeft: ${detailSegBox.left}, Top: ${detailSegBox.top}, Width: ${detailSegBox.width}, Height: ${detailSegBox.height}\\n\\n\`;
                  }
                }
              }

              hilog.info(0x0000, TAG, "Segmentation result: " + outputString);
              this.dataValues = outputString;

              if (data.fullSubject && data.fullSubject.foregroundImage) {
                this.segmentedImage = data.fullSubject.foregroundImage;
              } else {
                hilog.warn(0x0000, TAG, "No foreground image in segmentation result");
              }
            })
            .catch((error: BusinessError) => {
              hilog.error(0x0000, TAG, \`Image segmentation failed errCode: ${error.code}, errMessage: ${error.message}\`);
              this.dataValues = \`Error: ${error.message}\`;
              this.segmentedImage = undefined;
            });
        })
    }
    .width('100%')
    .height('80%')
    .justifyContent(FlexAlign.Center)
  }

  private async selectImage() {
    let uri = await this.openPhoto()
    if (uri === undefined) {
      hilog.error(0x0000, TAG, "uri is undefined");
    }
    this.loadImage(uri);
  }

  private openPhoto(): Promise<Array<string>> {
    return new Promise<Array<string>>((resolve, reject) => {
      let PhotoSelectOptions = new photoAccessHelper.PhotoSelectOptions();
      PhotoSelectOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE\_TYPE;
      PhotoSelectOptions.maxSelectNumber = 1;
      let photoPicker: photoAccessHelper.PhotoViewPicker = new photoAccessHelper.PhotoViewPicker();
      photoPicker.select(PhotoSelectOptions).then((PhotoSelectResult) => {
        hilog.info(0x0000, TAG, \`PhotoViewPicker.select successfully, PhotoSelectResult uri: ${PhotoSelectResult.photoUris}\`);
        resolve(PhotoSelectResult.photoUris)
      }).catch((err: BusinessError) => {
        hilog.error(0x0000, TAG, \`PhotoViewPicker.select failed with errCode: ${err.code}, errMessage: ${err.message}\`);
        reject();
      });
    })
  }

  private loadImage(names: string\[\]) {
    setTimeout(async () => {
      let imageSource: image.ImageSource | undefined = undefined
      try {
        let fileSource = await fileIo.open(names\[0\], fileIo.OpenMode.READ\_ONLY)
        imageSource = image.createImageSource(fileSource.fd)
        this.chooseImage = await imageSource.createPixelMap()
        await fileIo.close(fileSource);
      } catch (error) {
        hilog.error(0x0000, TAG, \`Failed to open file. Error: ${error}\`);
      }
    }, 100
    )
  }
}
