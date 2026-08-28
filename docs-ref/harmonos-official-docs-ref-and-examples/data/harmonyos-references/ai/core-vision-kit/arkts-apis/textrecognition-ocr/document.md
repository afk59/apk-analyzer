# textRecognition (OCR)

The OCR service provides the capability of converting image information into character information. After printed materials such as bills, cards, tables, newspapers, and books are converted into image information through optical input methods like scanning or taking photos, OCR technologies are used to convert the image information into character information that can be processed by computers. This facilitates the extraction of characters, screen coordinates, and bounding boxes for users. Currently, this service can recognize simplified Chinese, English, Japanese, Korean, and traditional Chinese.

**Start version**: 4.0.0(10)

#### Module Import

import { textRecognition } from '@kit.CoreVisionKit';

#### TextRecognitionConfiguration

OCR configuration, which is used to specify whether text direction detection is supported.

**System capability**: SystemCapability.AI.OCR.TextRecognition

**Start version**: 4.0.0(10)

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

isDirectionDetectionSupported

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether text direction detection is supported.

The value **true** indicates yes, and the value **false** indicates no.

The default value is **true**. If you can determine that the current image is correct, you can set this parameter to **false** to improve performance.

 |

#### VisionInfo

Visual information to be recognized. Currently, only the visual information of the [PixelMap](../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md) type in color data format RGBA\_8888 is supported.

**System capability**: SystemCapability.AI.OCR.TextRecognition

**Start version**: 4.0.0(10)

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

pixelMap

 | 

[image.PixelMap](../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md)

 | 

Yes

 | 

No

 | 

Image to be recognized.

For details about the specifications, please refer to [Restrictions](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/core-vision-introduction#section625292610522).

 |

#### PixelPoint

Pixel point position.

**System capability**: SystemCapability.AI.OCR.TextRecognition

**Start version**: 4.0.0(10)

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

x

 | 

number

 | 

Yes

 | 

No

 | 

Horizontal (X) coordinate of a pixel point.

 |
| 

y

 | 

number

 | 

Yes

 | 

No

 | 

Vertical (Y) coordinate of a pixel point.

 |

#### TextWord

Information about a word, including the content and the coordinates of its bounding box.

**System capability**: SystemCapability.AI.OCR.TextRecognition

**Start version**: 4.0.0(10)

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

value

 | 

string

 | 

Yes

 | 

No

 | 

Text content of a word.

 |
| 

cornerPoints

 | 

Array<[PixelPoint](#section3420112419175)\>

 | 

Yes

 | 

No

 | 

List of bounding box points of a word, which is returned clockwise.

 |

#### TextLine

Information about a line of text.

**System capability**: SystemCapability.AI.OCR.TextRecognition

**Start version**: 4.0.0(10)

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

value

 | 

string

 | 

Yes

 | 

No

 | 

Text content of a line.

 |
| 

cornerPoints

 | 

Array<[PixelPoint](#section3420112419175)\>

 | 

Yes

 | 

No

 | 

List of bounding box points of a line, which is returned clockwise.

 |
| 

words

 | 

Array<[TextWord](#section102702025111712)\>

 | 

Yes

 | 

No

 | 

Words contained in a line.

 |

#### TextBlock

Information about a block of text.

**System capability**: SystemCapability.AI.OCR.TextRecognition

**Start version**: 4.0.0(10)

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

value

 | 

string

 | 

Yes

 | 

No

 | 

Text content of a block.

 |
| 

lines

 | 

Array<[TextLine](#section12801726161718)\>

 | 

Yes

 | 

No

 | 

Lines contained in a block.

 |

#### TextRecognitionResult

OCR result, including the text content and coordinate information.

**System capability**: SystemCapability.AI.OCR.TextRecognition

**Start version**: 4.0.0(10)

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

value

 | 

string

 | 

Yes

 | 

No

 | 

Recognized text content.

 |
| 

blocks

 | 

Array<[TextBlock](#section1889182651713)\>

 | 

Yes

 | 

No

 | 

Specific block information in the text content.

 |

#### textRecognition.init

init(): Promise<boolean>

Initializes the OCR service. This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.AI.OCR.TextRecognition

**Start version**: 5.0.0(12)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<boolean>

 | 

Indicates whether the initialization is successful, which is returned through a promise.

The value **true** indicates yes, and the value **false** indicates no.

 |

**Example**:

import { textRecognition } from '@kit.CoreVisionKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

async function initAndReleaseOCR() {
  // Initialize the OCR service.
  const initResult = await textRecognition.init();
  hilog.info(0x0000, 'textRecognitionSample', \`OCR service initialization result:${initResult}\`);

  if (initResult) {
    hilog.info(0x0000, 'textRecognitionSample', 'OCR service initialized successfully');

    // Add the code for using the OCR service.
    // Example: await textRecognition.recognizeText(...);

    // Release the OCR service after the usage is complete.
    await textRecognition.release();
    hilog.info(0x0000, 'textRecognitionSample', 'OCR service released successfully');
  } else {
    hilog.error(0x0000, 'textRecognitionSample', 'Failed to initialize OCR service');
  }
}

@Entry
@Component
struct Page {

  build() {
    Column(){
      Button('initAndReleaseOCR').onClick(() => {
        // Call the function.
        initAndReleaseOCR();
      })
    }
  }
}

#### textRecognition.release

release(): Promise<void>

Releases the OCR service. This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.AI.OCR.TextRecognition

**Start version**: 5.0.0(12)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<void>

 | 

Promise object. This API does not return any value.

 |

**Example**:

import { textRecognition } from '@kit.CoreVisionKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

async function initAndReleaseOCR() {
  // Initialize the OCR service.
  const initResult = await textRecognition.init();
  hilog.info(0x0000, 'textRecognitionSample', \`OCR service initialization result:${initResult}\`);

  if (initResult) {
    hilog.info(0x0000, 'textRecognitionSample', 'OCR service initialized successfully');

    // Add the code for using the OCR service.
    // Example: await textRecognition.recognizeText(...);

    // Release the OCR service after the usage is complete.
    await textRecognition.release();
    hilog.info(0x0000, 'textRecognitionSample', 'OCR service released successfully');
  } else {
    hilog.error(0x0000, 'textRecognitionSample', 'Failed to initialize OCR service');
  }
}

@Entry
@Component
struct Page {

  build() {
    Column(){
      Button('initAndReleaseOCR').onClick(() => {
        // Call the function.
        initAndReleaseOCR();
      })
    }
  }
}

#### textRecognition.recognizeText

recognizeText(visionInfo: VisionInfo, callback: AsyncCallback<TextRecognitionResult>): void

Recognizes text contained in visual information. This API returns the result asynchronously through a callback.

**System capability**: SystemCapability.AI.OCR.TextRecognition

**Start version**: 4.0.0(10)

**Parameters**:

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

visionInfo

 | 

[VisionInfo](#section674171818172)

 | 

Yes

 | 

Visual information to be recognized.

 |
| 

callback

 | 

[AsyncCallback](../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#asynccallback)<[TextRecognitionResult](#section17548123419204)\>

 | 

Yes

 | 

Callback function, which returns the OCR object.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

200

 | 

Run timed out, please try again later.

 |
| 

401

 | 

The parameter check failed.

 |
| 

1001400001

 | 

Failed to run, please try again.

 |
| 

1001400002

 | 

The service is abnormal.

 |

**Example**:

import { textRecognition } from '@kit.CoreVisionKit'
import { image } from '@kit.ImageKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';
import { photoAccessHelper } from '@kit.MediaLibraryKit';

let imageSource: image.ImageSource | undefined = undefined;
let chooseImage: PixelMap | undefined = undefined;
// Convert the image into **PixelMap**. The image can be obtained from the gallery.
let photoPicker: photoAccessHelper.PhotoViewPicker = new photoAccessHelper.PhotoViewPicker();
photoPicker.select({
  MIMEType: photoAccessHelper.PhotoViewMIMETypes.IMAGE\_TYPE, maxSelectNumber: 1
}).then((res: photoAccessHelper.PhotoSelectResult) => {
  let uri = res.photoUris\[0\];
  if (uri === undefined) {
    hilog.error(0x0000, 'OCRDemo', 'Failed to get uri.');
    return;
  }
  setTimeout(async () => {
    let fileSource = await fileIo.open(uri, fileIo.OpenMode.READ\_ONLY);
    imageSource = image.createImageSource(fileSource.fd);
    chooseImage = await imageSource.createPixelMap();
    if (!chooseImage) {
      return;
    }

    // Call the OCR API.
    let visionInfo: textRecognition.VisionInfo = {
      pixelMap: chooseImage
    };
    textRecognition.recognizeText(visionInfo, (error: BusinessError, data: textRecognition.TextRecognitionResult) => {
      if (error.code !== 0) {
        hilog.error(0x0000, 'OCRDemo', \`Failed to recognize text. Code: ${error.code}, message: ${error.message}\`);
        return;
      }
      // The recognition is successful. Obtain the corresponding result.
      let recognitionString = JSON.stringify(data);
      hilog.info(0x0000, 'OCRDemo', \`Succeeded in recognizing text: ${recognitionString}\`);

      if(chooseImage && imageSource) {
        chooseImage.release();
        imageSource.release();
      }
    });
    if (fileSource) {
      try {
        await fileIo.close(fileSource);
      } catch (err) {
        hilog.error(0x0000, 'OCRDemo', \`Failed to close fileSource. Code: ${err.code}, message: ${err.message}\`);
      }
    }
  }, 100)
}).catch((err: BusinessError) => {
  hilog.error(0x0000, 'OCRDemo', \`Failed to get photo image uri. Code: ${err.code}, message: ${err.message}\`);
})

@Entry
@Component
struct Page {

  build() {
    Column(){
    }
  }
}

#### textRecognition.recognizeText

recognizeText(visionInfo: VisionInfo, configuration ?: TextRecognitionConfiguration): Promise<TextRecognitionResult>

Recognizes text contained in visual information. You can customize the configuration for more detailed settings. This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.AI.OCR.TextRecognition

**Start version**: 4.0.0(10)

**Parameters**:

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

visionInfo

 | 

[VisionInfo](#section674171818172)

 | 

Yes

 | 

Visual information to be recognized.

 |
| 

configuration

 | 

[TextRecognitionConfiguration](#section1081123302517)

 | 

No

 | 

Recognition configuration.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[TextRecognitionResult](#section17548123419204)\>

 | 

OCR result returned through a promise.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

200

 | 

Run timed out, please try again later.

 |
| 

401

 | 

The parameter check failed.

 |
| 

1001400001

 | 

Failed to run, please try again.

 |
| 

1001400002

 | 

The service is abnormal.

 |

**Example**:

import { textRecognition } from '@kit.CoreVisionKit'
import { image } from '@kit.ImageKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';
import { photoAccessHelper } from '@kit.MediaLibraryKit';

let imageSource: image.ImageSource | undefined = undefined;
let chooseImage: PixelMap | undefined = undefined;
// Convert the image into **PixelMap**. The image can be obtained from the gallery.
let photoPicker: photoAccessHelper.PhotoViewPicker = new photoAccessHelper.PhotoViewPicker();
photoPicker.select({
  MIMEType: photoAccessHelper.PhotoViewMIMETypes.IMAGE\_TYPE, maxSelectNumber: 1
}).then((res: photoAccessHelper.PhotoSelectResult) => {
  let uri = res.photoUris\[0\];
  if (uri === undefined) {
    hilog.error(0x0000, 'OCRDemo', 'Failed to get uri.');
    return;
  }
  setTimeout(async () => {
    let fileSource = await fileIo.open(uri, fileIo.OpenMode.READ\_ONLY);
    imageSource = image.createImageSource(fileSource.fd);
    chooseImage = await imageSource.createPixelMap();
    if (!chooseImage) {
      return;
    }

    // Call the OCR API.
    let visionInfo: textRecognition.VisionInfo = {
      pixelMap: chooseImage
    };
    let recognitionResult = await textRecognition.recognizeText(visionInfo);

    // The recognition is successful. Obtain the corresponding result.
    let recognitionString = JSON.stringify(recognitionResult);
    hilog.info(0x0000, 'OCRDemo', \`Succeeded in recognizing text: ${recognitionString}\`);

    if(chooseImage && imageSource) {
      chooseImage.release();
      imageSource.release();
    }
    if (fileSource) {
      try {
        await fileIo.close(fileSource);
      } catch (err) {
        hilog.error(0x0000, 'OCRDemo', \`Failed to close fileSource. Code: ${err.code}, message: ${err.message}\`);
      }
    }
  }, 100)
}).catch((err: BusinessError) => {
  hilog.error(0x0000, 'OCRDemo', \`Failed to get photo image uri. Code: ${err.code}, message: ${err.message}\`);
})

@Entry
@Component
struct Page {

  build() {
    Column(){
    }
  }
}

#### textRecognition.recognizeText

recognizeText(visionInfo: VisionInfo, configuration: TextRecognitionConfiguration, callback: AsyncCallback<TextRecognitionResult>): void

Recognizes text contained in visual information. You can customize the configuration for more detailed settings. This API returns the result asynchronously through a callback.

**System capability**: SystemCapability.AI.OCR.TextRecognition

**Start version**: 4.0.0(10)

**Parameters**:

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

visionInfo

 | 

[VisionInfo](#section674171818172)

 | 

Yes

 | 

Visual information to be recognized.

 |
| 

configuration

 | 

[TextRecognitionConfiguration](#section1081123302517)

 | 

Yes

 | 

Recognition configuration.

 |
| 

callback

 | 

[AsyncCallback](../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#asynccallback)<[TextRecognitionResult](#section17548123419204)\>

 | 

Yes

 | 

Callback of the recognition result, which can be used for UI display or interaction.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

200

 | 

Run timed out, please try again later.

 |
| 

401

 | 

The parameter check failed.

 |
| 

1001400001

 | 

Failed to run, please try again.

 |
| 

1001400002

 | 

The service is abnormal.

 |

**Example**:

import { textRecognition } from '@kit.CoreVisionKit'
import { image } from '@kit.ImageKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';
import { photoAccessHelper } from '@kit.MediaLibraryKit';

let imageSource: image.ImageSource | undefined = undefined;
let chooseImage: PixelMap | undefined = undefined;
// Convert the image into **PixelMap**. The image can be obtained from the gallery.
let photoPicker: photoAccessHelper.PhotoViewPicker = new photoAccessHelper.PhotoViewPicker();
photoPicker.select({
  MIMEType: photoAccessHelper.PhotoViewMIMETypes.IMAGE\_TYPE, maxSelectNumber: 1
}).then((res: photoAccessHelper.PhotoSelectResult) => {
  let uri = res.photoUris\[0\];
  if (uri === undefined) {
    hilog.error(0x0000, 'OCRDemo', 'Failed to get uri.');
    return;
  }
  setTimeout(async () => {
    let fileSource = await fileIo.open(uri, fileIo.OpenMode.READ\_ONLY);
    imageSource = image.createImageSource(fileSource.fd);
    chooseImage = await imageSource.createPixelMap();
    if (!chooseImage) {
      return;
    }

    // Call the OCR API.
    let visionInfo: textRecognition.VisionInfo = {
      pixelMap: chooseImage
    };
    let textConfiguration: textRecognition.TextRecognitionConfiguration = {
      isDirectionDetectionSupported: false
    };
    textRecognition.recognizeText(visionInfo, textConfiguration, (error: BusinessError, data: textRecognition.TextRecognitionResult) => {
      if (error.code !== 0) {
        hilog.error(0x0000, 'OCRDemo', \`Failed to recognize text. Code: ${error.code}, message: ${error.message}\`);
        return;
      }
      // The recognition is successful. Obtain the corresponding result.
      let recognitionString = JSON.stringify(data);
      hilog.info(0x0000, 'OCRDemo', \`Succeeded in recognizing text: ${recognitionString}\`);

      if(chooseImage && imageSource) {
        chooseImage.release();
        imageSource.release();
      }
    });
    if (fileSource) {
      try {
        await fileIo.close(fileSource);
      } catch (err) {
        hilog.error(0x0000, 'OCRDemo', \`Failed to close fileSource. Code: ${err.code}, message: ${err.message}\`);
      }
    }
  }, 100)
}).catch((err: BusinessError) => {
  hilog.error(0x0000, 'OCRDemo', \`Failed to get photo image uri. Code: ${err.code}, message: ${err.message}\`);
})

@Entry
@Component
struct Page {

  build() {
    Column(){
    }
  }
}

#### textRecognition.getSupportedLanguages

getSupportedLanguages(): Promise<Array<string>>

Obtains the list of languages supported by OCR. This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.AI.OCR.TextRecognition

**Start version**: 4.0.0(10)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<Array<string>>

 | 

[List of supported languages](#section133729715453), which is returned through a promise.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

1001400001

 | 

Failed to run, please try again.

 |
| 

1001400002

 | 

The service is abnormal.

 |

**Example**:

import { textRecognition } from '@kit.CoreVisionKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

textRecognition.getSupportedLanguages().then((data: Array<string>) => {
  let languageString = data.join(', ');
  hilog.info(0x0000, 'OCRDemo', \`Succeeded in obtaining the language: ${languageString}\`);
}, (err: BusinessError) => {
  hilog.error(0x0000, 'OCRDemo', \`Failed to obtain the language. Code: ${err.code}, message: ${err.message}\`);
});

@Entry
@Component
struct Page {

  build() {
    Column(){
    }
  }
}

#### textRecognition.getSupportedLanguages

getSupportedLanguages(callback: AsyncCallback<Array<string>>): void

Obtains the list of languages supported by OCR. This API returns the result asynchronously through a callback.

**System capability**: SystemCapability.AI.OCR.TextRecognition

**Start version**: 4.0.0(10)

**Parameters**:

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

callback

 | 

[AsyncCallback](../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#asynccallback)<Array<string>>

 | 

Yes

 | 

[List of supported languages](#section133729715453).

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

1001400001

 | 

Failed to run, please try again.

 |
| 

1001400002

 | 

The service is abnormal.

 |

**Example**:

import { textRecognition } from '@kit.CoreVisionKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

textRecognition.getSupportedLanguages((error: BusinessError, data: Array<string>) => {
  if (!error) {
    hilog.info(0x0000, 'OCRDemo', \`Succeeded in obtaining the language: ${data}\`);
  } else {
    hilog.error(0x0000, 'OCRDemo', \`Failed to obtain the language. Code: ${error.code}, message: ${error.message}\`);
  }
});

@Entry
@Component
struct Page {

  build() {
    Column(){
    }
  }
}

#### List of Supported Languages

| 
Language

 | 

Description

 |
| :-- | :-- |
| 

zh-CN

 | 

Simplified Chinese.

 |
| 

en

 | 

English.

 |
| 

ja

 | 

Japanese.

 |
| 

ko

 | 

Korean.

 |
| 

zh-TW

 | 

Traditional Chinese.

 |
