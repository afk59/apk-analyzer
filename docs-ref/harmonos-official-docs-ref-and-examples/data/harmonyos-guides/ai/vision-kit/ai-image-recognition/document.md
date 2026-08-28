# AI Image Recognition

#### Use Cases

AI image recognition provides scenario-based text recognition, subject segmentation, and image search functions by aggregating AI capabilities such as Optical Character Recognition (OCR), subject segmentation, entity recognition, and multi-object recognition. To use these functions, you need to first enable the AI image recognition control by calling related APIs provided by basic controls (for details, please refer to [Image](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-image#enableanalyzer11), [Video](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-media-components-video#enableanalyzer12), and [XComponent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-xcomponent#enableanalyzer12)). Furthermore, you can customize the functions based on your own needs through the APIs provided in the API reference of Vision Kit. Your customization requires collaboration of the basic controls. For example, to recognize static images, use the **Image** control; to recognize frames displayed when videos are paused, use the **Video** control; to recognize images in scenarios such as customized rendering, use the **XComponent** control.

AI image recognition provides the following functions:

-   Text recognition
    
    A user can press and hold text to select it or continuously press and hold an entity such as a phone number, email address, URL, physical address, or time in the text to trigger a quick operation on the corresponding entity. For example, a user can continuously press and hold a time in the text to trigger the quick operation entry for creating an event.
    
-   Image search
    
    A user can perform image search based on a clipped object. Alternatively, the user can proactively trigger the identification of objects, such as animals, plants, or buildings in an image, mark them with corresponding icons, and tap the icons to perform image search. The search result will be displayed in a modal window.
    
-   Subject segmentation
    
    A user can press and hold one or multiple subjects to perform subject segmentation. Then, the user can copy or share a subject, select all subjects, or use the subjects for image search.
    
-   AIButton
    
    AIButton can be used to achieve the following functions: explicit underlining of entities such as a phone number, email address, URL, physical address, and time (showing a quick operation menu after a user taps the entity), image translation (from the image text language to the system language if the two languages are different), and table extraction (if there is a table in an image). When AIButton is set to visible, images are pre-analyzed. AIButton is displayed only when the images contain text and the text region occupies more than 5% of space in the image region.
    

Here are some suggestions for using AI image recognition:

-   AI image recognition can help users obtain more information from images (for example, long-pressing an image to clip content, select text, or recognize entities). In large image preview scenarios, users tend to be more interested in the content of images. Therefore, you are advised to enable this capability in such scenarios to provide users with the optimal interactive experience.
-   AIButton is used for explicitly reminding users to interact with text on images. Enabling AIButton will trigger image pre-analysis, which causes certain power consumption. It is essential to fully understand your service scenarios, estimate the target users' image content distribution, and balance the image browsing experience with advanced AI image recognition experience. For example, if your service aims to help users efficiently extract text from images, enabling AIButton will enhance users' text extraction experience. However, if your service is more focused on image editing, consider disabling AIButton.

**Figure 1** AI image recognition example  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/EUIIWXaaSoqrGp-gSHFtbw/en-us_image_0000002236392776.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062129Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D6798A573D78895B543C32AA4A1008D8C5B30B255DF6446D4F83F80EA129E634 "Click to enlarge")

#### Restrictions

-   Languages supported for text: simplified Chinese, traditional Chinese, English, Uyghur, and Tibetan
-   The minimum image resolution is 100 x 100.
-   Image analysis supports only static non-vector images, which means that SVG and GIF images cannot be analyzed. The image [PixelMap](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-image-pixelmap) can be passed for analysis. Currently, only [RGBA\_8888](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-image-e#pixelmapformat7) images are supported.
-   The minimum aspect ratio is 1:3 (the height must be less than 3 times of the width) for images to be translated and 1:7 (the height must be less than 7 times of the width) for images to have their text recognized.
-   You can use [getImageAnalyzerSupportTypes](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-image-common#getimageanalyzersupporttypes12) to check whether the current device supports AI image recognition.
    
    The return format is **SupportTypes: \[_Enumerated value for subject recognition_, _Enumerated value for text recognition_, _Enumerated value for object lookup_\]**. For details about the enumerated values, please refer to [ImageAnalyzerType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-image-common#imageanalyzertype12).
    
    If **SupportTypes: \[\]** is returned, the current device does not support AI image recognition. If other values are returned, the current device supports AI image recognition.
    
    import { visionImageAnalyzer } from '@kit.VisionKit';
    
    @Entry
    @Component
    struct Index {
      private aiController: visionImageAnalyzer.VisionImageAnalyzerController = new visionImageAnalyzer.VisionImageAnalyzerController()
    
      build() {
        Row() {
          Button('getTypes')
            .onClick(() => {
              let SupportTypes = this.aiController.getImageAnalyzerSupportTypes()
              console.info(\`SupportTypes: ${JSON.stringify(SupportTypes)}\`)
            })
        }
      }
    }
    

#### Development Procedure

1.  Add classes related to the AI image recognition control.
    
    import { visionImageAnalyzer } from '@kit.VisionKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
2.  Initialize the [VisionImageAnalyzerController](https://developer.huawei.com/consumer/en/doc/harmonyos-references/vision-image-analyzer#section37192953318) object.
    
    private visionImageAnalyzerController: visionImageAnalyzer.VisionImageAnalyzerController = new visionImageAnalyzer.VisionImageAnalyzerController();
    private isSupportImageAnalyzer: boolean = false;
    
3.  Check whether the device supports AI image recognition. If yes, subscribe to related events.
    
    aboutToAppear(): void {
      let supportTypes = this.visionImageAnalyzerController.getImageAnalyzerSupportTypes(); 
      if (supportTypes.length > 0) {
         this.isSupportImageAnalyzer = true;
         this.registerListener();
      }
    }
    
    registerListener(){
       this.visionImageAnalyzerController.on('imageAnalyzerVisibilityChange', (visibility: visionImageAnalyzer.ImageAnalyzerVisibility) => {
         console.info("DEMO\_TAG", \`imageAnalyzerVisibilityChange result: ${JSON.stringify(visibility)}\`)
       })
       this.visionImageAnalyzerController.on('textAnalysis', (text: string) => {
          console.info("DEMO\_TAG", \`textAnalysis result: ${JSON.stringify(text)}\`)
       })
       this.visionImageAnalyzerController.on('selectedTextChange', (selectedText: string) => {
         console.info("DEMO\_TAG", \`selectedTextChange result: ${JSON.stringify(selectedText)}\`)
       })
       this.visionImageAnalyzerController.on('subjectAnalysis', (subjects: visionImageAnalyzer.Subject\[\]) => {
         console.info("DEMO\_TAG", \`subjectAnalysis result: ${JSON.stringify(subjects)}\`)
       })
       this.visionImageAnalyzerController.on('selectedSubjectsChange', (subjects: visionImageAnalyzer.Subject\[\]) => {
         console.info("DEMO\_TAG", \`selectedSubjectsChange result: ${JSON.stringify(subjects)}\`)
       })
       this.visionImageAnalyzerController.on('analyzerFailed', (error: BusinessError) => {
         console.error("DEMO\_TAG", \`analyzerFailed result: ${JSON.stringify(error)}\`)
       })
    }
    
4.  Bind the [VisionImageAnalyzerController](https://developer.huawei.com/consumer/en/doc/harmonyos-references/vision-image-analyzer#section37192953318) object to control interactions related to image recognition.
    
    build() {
      Stack() {
        // Replace the image with your own one stored in the **resources/base/media** directory. The values of **types** must be a subset of **supportTypes** defined in the previous step.
        Image($r('app.media.img'), {
          types: \[ImageAnalyzerType.TEXT, ImageAnalyzerType.SUBJECT, ImageAnalyzerType.OBJECT\_LOOKUP\],
          aiController: this.visionImageAnalyzerController
        })
          .width('100%')
          .height('100%')
          .enableAnalyzer(this.isSupportImageAnalyzer ? true: false)
          .objectFit(ImageFit.Contain)
      }.width('100%').height('100%')
    }
    
5.  Unsubscribe from events.
    
    aboutToDisappear(): void {
      this.visionImageAnalyzerController.off('imageAnalyzerVisibilityChange')
      this.visionImageAnalyzerController.off('textAnalysis')
      this.visionImageAnalyzerController.off('selectedTextChange')
      this.visionImageAnalyzerController.off('subjectAnalysis')
      this.visionImageAnalyzerController.off('selectedSubjectsChange')
      this.visionImageAnalyzerController.off('analyzerFailed')
    }
    

#### Development Example

## Index.ets

import { visionImageAnalyzer } from '@kit.VisionKit';
import { BusinessError } from '@kit.BasicServicesKit'
@Entry
@Component
struct ImageDemo {
  private visionImageAnalyzerController: visionImageAnalyzer.VisionImageAnalyzerController = new visionImageAnalyzer.VisionImageAnalyzerController()
  private isSupportImageAnalyzer: boolean = false;
  aboutToAppear(): void {
    let supportTypes = this.visionImageAnalyzerController.getImageAnalyzerSupportTypes(); 
    if (supportTypes.length > 0) {
      this.isSupportImageAnalyzer = true;
      this.registerListener();
    }
  }

  registerListener(){
    this.visionImageAnalyzerController.on('imageAnalyzerVisibilityChange', (visibility: visionImageAnalyzer.ImageAnalyzerVisibility) => {
      console.info("DEMO\_TAG", \`imageAnalyzerVisibilityChange result: ${JSON.stringify(visibility)}\`)
    })
    this.visionImageAnalyzerController.on('textAnalysis', (text: string) => {
      console.info("DEMO\_TAG", \`textAnalysis result: ${JSON.stringify(text)}\`)
    })
    this.visionImageAnalyzerController.on('selectedTextChange', (selectedText: string) => {
      console.info("DEMO\_TAG", \`selectedTextChange result: ${JSON.stringify(selectedText)}\`)
    })
    this.visionImageAnalyzerController.on('subjectAnalysis', (subjects: visionImageAnalyzer.Subject\[\]) => {
      console.info("DEMO\_TAG", \`subjectAnalysis result: ${JSON.stringify(subjects)}\`)
    })
    this.visionImageAnalyzerController.on('selectedSubjectsChange', (subjects: visionImageAnalyzer.Subject\[\]) => {
      console.info("DEMO\_TAG", \`selectedSubjectsChange result: ${JSON.stringify(subjects)}\`)
    })
    this.visionImageAnalyzerController.on('analyzerFailed', (error: BusinessError) => {
      console.error("DEMO\_TAG", \`analyzerFailed result: ${JSON.stringify(error)}\`)
    })
  }
  build() {
    Stack() {
      Image($r('app.media.img'), {
        types: \[ImageAnalyzerType.TEXT, ImageAnalyzerType.SUBJECT, ImageAnalyzerType.OBJECT\_LOOKUP\],
        aiController: this.visionImageAnalyzerController
      })
        .width('100%')
        .height('100%')
        .enableAnalyzer(this.isSupportImageAnalyzer ? true : false)
        .objectFit(ImageFit.Contain)
    }.width('100%').height('100%')
  }
    aboutToDisappear(): void {
      this.visionImageAnalyzerController.off('imageAnalyzerVisibilityChange')
      this.visionImageAnalyzerController.off('textAnalysis')
      this.visionImageAnalyzerController.off('selectedTextChange')
      this.visionImageAnalyzerController.off('subjectAnalysis')
      this.visionImageAnalyzerController.off('selectedSubjectsChange')
      this.visionImageAnalyzerController.off('analyzerFailed')
    }
}
