# OCR

#### Application Scenarios

OCR is a technology that converts printed text from various sources, such as bills, cards, tables, newspapers, and books, into image information through optical input methods like scanning or taking photos. The text information is then extracted from the image information using OCR and transformed into character information that can be processed by computers. OCR has the following features:

-   Detects and recognizes text from images captured from documents, street scenes, and other sources. It can also provide text detection and recognition capabilities, and offer related services such as translation and search based on the detection and recognition results.
-   Processes image information from various sources such as cameras and image galleries by providing an open capability for automatic text detection, locating, and recognition.
-   Supports text recognition in scenarios with text tilt within a specific angle range, shooting angle tilt, complex lighting conditions, and complex text backgrounds.

The following figure shows an example.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/GXRhgFqEQKWbfbUWtgJE1w/en-us_image_0000002349092746.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062126Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=79C21D48E855F0CB97114DC0CF3DCC735B1CB18069A7757E10C9AB44A0D46F05)

#### Restrictions

This capability is currently not supported on emulators.

| 
AI Capability

 | 

Restrictions

 |
| :-- | :-- |
| 

OCR

 | 

-   Supported formats: JPG, JPEG, and PNG
-   Supported languages: simplified Chinese, English, Japanese, Korean, and traditional Chinese
-   Text length: no more than 10,000 characters
-   Supports printed font recognition but has limitations in recognizing handwritten fonts.
-   The input image should have a suitable imaging quality (720p or higher recommended), with a height between 100 px and 15,210 px, a width between 100 px and 10,000 px, and a height-to-width ratio preferably below 10:1 (the height must be less than 10 times of the width), ideally close to the height-to-width ratio of a smartphone screen.
-   The shooting angle should be less than 30 degrees from the vertical direction of the plane where the text is located.

 |

#### Development Procedure

1.  Add the classes for implementing OCR to a project.
    
    import { textRecognition } from '@kit.CoreVisionKit'
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
    
3.  Obtain an image from the gallery, convert the image into [PixelMap](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-image-pixelmap), and add the initialization and release methods.
    
    async aboutToAppear(): Promise<void> {
      const initResult = await textRecognition.init();
      hilog.info(0x0000, 'OCRDemo', \`OCR service initialization result:${initResult}\`);
    }
    
    async aboutToDisappear(): Promise<void> {
      await textRecognition.release();
      hilog.info(0x0000, 'OCRDemo', 'OCR service released successfully');
    }
    
    private async selectImage() {
      let uri = await this.openPhoto();
      if (uri === undefined) {
        hilog.error(0x0000, 'OCRDemo', "Failed to get uri.");
        return;
      }
      this.loadImage(uri);
    }
    
    private openPhoto(): Promise<string> {
      return new Promise<string>((resolve) => {
        let photoPicker: photoAccessHelper.PhotoViewPicker = new photoAccessHelper.PhotoViewPicker();
        photoPicker.select({
          MIMEType: photoAccessHelper.PhotoViewMIMETypes.IMAGE\_TYPE,
          maxSelectNumber: 1
        }).then((res: photoAccessHelper.PhotoSelectResult) => {
          resolve(res.photoUris\[0\]);
        }).catch((err: BusinessError) => {
          hilog.error(0x0000, 'OCRDemo', \`Failed to get photo image uri. code: ${err.code}, message: ${err.message}\`);
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
      }, 100)
    }
    
4.  Instantiate the [VisionInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/core-vision-text-recognition-api#section674171818172) object and pass [PixelMap](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-image-pixelmap) of the image to be detected.
    
    **VisionInfo** is the input parameter of the image to be recognized by OCR. Currently, only the visual information of the [PixelMap](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-image-pixelmap) type is supported.
    
    let visionInfo: textRecognition.VisionInfo = {
      pixelMap: this.chooseImage
    };
    
5.  Configure [TextRecognitionConfiguration](https://developer.huawei.com/consumer/en/doc/harmonyos-references/core-vision-text-recognition-api#section1081123302517) to specify whether text direction detection is supported.
    
    let textConfiguration: textRecognition.TextRecognitionConfiguration = {
      isDirectionDetectionSupported: false
    };
    
6.  Call the [recognizeText](https://developer.huawei.com/consumer/en/doc/harmonyos-references/core-vision-text-recognition-api#section1446761711464) API of **textRecognition** to process the recognition result.
    
    If the API call is successful, the recognition result is returned. If the API call fails, an error code is returned.
    
    The **recognizeText** API can be called in three ways. The following uses one way as an example. For details about other ways, please refer to the [API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/core-vision-text-recognition-api).
    
    textRecognition.recognizeText(visionInfo, textConfiguration)
      .then((data: textRecognition.TextRecognitionResult) => {
        // The recognition is successful. Obtain the corresponding result.
        let recognitionString = JSON.stringify(data);
        hilog.info(0x0000, 'OCRDemo', \`Succeeded in recognizing text: ${recognitionString}\`);
        // Update the result to **Text**.
        this.dataValues = data.value;
      })
      .catch((error: BusinessError) => {
        hilog.error(0x0000, 'OCRDemo', \`Failed to recognize text. Code: ${error.code}, message: ${error.message}\`);
        this.dataValues = \`Error: ${error.message}\`;
      });
    

#### Development Example

After button taps, recognize texts within an image, and print the recognition result to logs.

## Index.ets

import { textRecognition } from '@kit.CoreVisionKit'
import { image } from '@kit.ImageKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';
import { photoAccessHelper } from '@kit.MediaLibraryKit';

@Entry
@Component
struct Index {
  private imageSource: image.ImageSource | undefined = undefined;
  @State chooseImage: PixelMap | undefined = undefined;
  @State dataValues: string = '';

  async aboutToAppear(): Promise<void> {
    const initResult = await textRecognition.init();
    hilog.info(0x0000, 'OCRDemo', \`OCR service initialization result:${initResult}\`);
  }

  async aboutToDisappear(): Promise<void> {
    await textRecognition.release();
    hilog.info(0x0000, 'OCRDemo', 'OCR service released successfully');
  }

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
          // Bring up the gallery to obtain images.
          this.selectImage();
        })

      Button('Start recognition')
        .type(ButtonType.Capsule)
        .fontColor(Color.White)
        .alignSelf(ItemAlign.Center)
        .width('80%')
        .margin(10)
        .onClick(async () => {
          this.textRecognitionTest();
        })
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }

  private textRecognitionTest() {
    if (!this.chooseImage) {
      return;
    }
    // Call the text recognition API.
    let visionInfo: textRecognition.VisionInfo = {
      pixelMap: this.chooseImage
    };
    let textConfiguration: textRecognition.TextRecognitionConfiguration = {
      isDirectionDetectionSupported: false
    };
    textRecognition.recognizeText(visionInfo, textConfiguration)
      .then((data: textRecognition.TextRecognitionResult) => {
        // The recognition is successful. Obtain the corresponding result.
        let recognitionString = JSON.stringify(data);
        hilog.info(0x0000, 'OCRDemo', \`Succeeded in recognizing text: ${recognitionString}\`);
        // Update the result to **Text**.
        this.dataValues = data.value;
      })
      .catch((error: BusinessError) => {
        hilog.error(0x0000, 'OCRDemo', \`Failed to recognize text. Code: ${error.code}, message: ${error.message}\`);
        this.dataValues = \`Error: ${error.message}\`;
      });
  }

  private async selectImage() {
    let uri = await this.openPhoto();
    if (uri === undefined) {
      hilog.error(0x0000, 'OCRDemo', "Failed to get uri.");
      return;
    }
    this.loadImage(uri);
  }

  private openPhoto(): Promise<string> {
    return new Promise<string>((resolve) => {
      let photoPicker: photoAccessHelper.PhotoViewPicker = new photoAccessHelper.PhotoViewPicker();
      photoPicker.select({
        MIMEType: photoAccessHelper.PhotoViewMIMETypes.IMAGE\_TYPE,
        maxSelectNumber: 1
      }).then((res: photoAccessHelper.PhotoSelectResult) => {
        resolve(res.photoUris\[0\]);
      }).catch((err: BusinessError) => {
        hilog.error(0x0000, 'OCRDemo', \`Failed to get photo image uri. code: ${err.code}, message: ${err.message}\`);
        resolve('');
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
        hilog.error(0x0000, 'OCRDemo', \`Failed to open file. Error: ${error}\`);
      }
    }, 100)
  }
}
