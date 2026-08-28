# subjectSegmentation (Subject Segmentation)

Core Vision Kit can segment objects in a common image based on parameter settings (such as the maximum number of objects to be detected and whether to output detailed information about each object). The segmentation information includes the overall segmentation result of the image and detailed information about each prominent object.

**Start version**: 5.0.0(12)

#### Module Import

import { subjectSegmentation } from '@kit.CoreVisionKit';

#### VisionInfo

Visual information to be recognized. Currently, only the visual information of the PixelMap type in color data format RGBA\_8888 is supported.

**System capability**: SystemCapability.AI.Vision.SubjectSegmentation

**Start version**: 5.0.0(12)

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

No

 | 

No

 | 

Image to be recognized.

For details about the specifications, please refer to [Restrictions](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/core-vision-introduction#section625292610522).

 |

#### SegmentationConfig

Optional configuration for salient subject segmentation, including the maximum number of output subjects, whether to output detailed segmentation information about each subject, and whether to output the foreground image.

**System capability**: SystemCapability.AI.Vision.SubjectSegmentation

**Start version**: 5.0.0(12)

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

maxCount

 | 

number

 | 

No

 | 

Yes

 | 

Maximum number of subjects to be output. The value ranges from 1 to 20. The subjects are sorted in descending order based on their proportion of occupied area in the input image. The default value is **6**.

 |
| 

enableSubjectDetails

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether to output the foreground information (**subjectDetails**) about each subject. The value **true** indicates yes, and the value **false** indicates no. The default value is **false**.

 |
| 

enableSubjectForegroundImage

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether to output foreground images. The value **true** indicates yes, and the value **false** indicates no. The default value is **false**.

 |

#### Rectangle

Bounding box after salient subject segmentation.

**System capability**: SystemCapability.AI.Vision.SubjectSegmentation

**Start version**: 5.0.0(12)

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

left

 | 

number

 | 

No

 | 

No

 | 

X coordinate of the upper left corner of a bounding box.

 |
| 

top

 | 

number

 | 

No

 | 

No

 | 

Y coordinate of the upper left corner of a bounding box.

 |
| 

height

 | 

number

 | 

No

 | 

No

 | 

Height of a bounding box, in pixels.

 |
| 

width

 | 

number

 | 

No

 | 

No

 | 

Width of a bounding box, in pixels.

 |

#### SubjectResult

Detailed result after segmentation.

**System capability**: SystemCapability.AI.Vision.SubjectSegmentation

**Start version**: 5.0.0(12)

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

foregroundImage

 | 

[image.PixelMap](../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md)

 | 

No

 | 

No

 | 

Foreground image of a salient subject.

 |
| 

mattingList

 | 

Int32Array

 | 

No

 | 

No

 | 

1D array based on the original image size, which represents the subject mask. The value ranges from 0 to 255. The value **0** indicates the background, the value **255** indicates a subject, and the values between **0** and **255** indicate the probability of a salient subject.

 |
| 

subjectRectangle

 | 

[Rectangle](#section789716171126)

 | 

No

 | 

No

 | 

Bounding box of a subject.

 |

#### SegmentationResult

Overall output results after segmentation, including the number of subjects, segmentation information about all subjects in the entire image, and detailed information about each subject.

**System capability**: SystemCapability.AI.Vision.SubjectSegmentation

**Start version**: 5.0.0(12)

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

subjectCount

 | 

number

 | 

No

 | 

No

 | 

Number of subjects, which is restricted by the value of **maxCount** in [SegmentationConfig](#section1268211401742).

 |
| 

fullSubject

 | 

[SubjectResult](#section19644831362)

 | 

No

 | 

No

 | 

Information about all salient subjects output from an entire image by default.

 |
| 

subjectDetails

 | 

Array<[SubjectResult](#section19644831362)\>

 | 

No

 | 

Yes

 | 

Detailed information about each salient subject.

 |

#### subjectSegmentation.init

init(): Promise<boolean>

Initializes the subject segmentation service. This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.AI.Vision.SubjectSegmentation

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

import { subjectSegmentation } from '@kit.CoreVisionKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

async function initAndReleaseSubjectSegmentation() {
  // Initialize the subject segmentation service.
  const initResult = await subjectSegmentation.init();
  hilog.info(0x0000, 'subjectSegmentationSample', \`Subject segmentation initialization result:${initResult}\`);

  if (initResult) {
    hilog.info(0x0000, 'subjectSegmentationSample', 'Subject segmentation initialized successfully');

    // Add the code for using the subject segmentation service.

    // Release the subject segmentation service after the usage is complete.
    await subjectSegmentation.release();
    hilog.info(0x0000, 'subjectSegmentationSample', 'Subject segmentation released successfully');
  } else {
    hilog.error(0x0000, 'subjectSegmentationSample', 'Failed to initialize subject segmentation');
  }
}

@Entry
@Component
struct Page {

  build() {
    Column(){
      Button('initAndReleaseSubjectSegmentation').onClick(() => {
        // Call the function.
        initAndReleaseSubjectSegmentation();
      })
    }
  }
}

#### subjectSegmentation.release

release(): Promise<void>

Releases the subject segmentation service. This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.AI.Vision.SubjectSegmentation

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

import { subjectSegmentation } from '@kit.CoreVisionKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

async function initAndReleaseSubjectSegmentation() {
  // Initialize the subject segmentation service.
  const initResult = await subjectSegmentation.init();
  hilog.info(0x0000, 'subjectSegmentationSample', \`Subject segmentation initialization result:${initResult}\`);

  if (initResult) {
    hilog.info(0x0000, 'subjectSegmentationSample', 'Subject segmentation initialized successfully');

    // Add the code for using the subject segmentation service.

    // Release the subject segmentation service after the usage is complete.
    await subjectSegmentation.release();
    hilog.info(0x0000, 'subjectSegmentationSample', 'Subject segmentation released successfully');
  } else {
    hilog.error(0x0000, 'subjectSegmentationSample', 'Failed to initialize subject segmentation');
  }
}

@Entry
@Component
struct Page {

  build() {
    Column(){
      Button('initAndReleaseSubjectSegmentation').onClick(() => {
        // Call the function.
        initAndReleaseSubjectSegmentation();
      })
    }
  }
}

#### subjectSegmentation.doSegmentation

doSegmentation(visionInfo: VisionInfo, config?: SegmentationConfig): Promise<SegmentationResult>

Creates a salient subject segmentation instance and initializes the engine. This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.AI.Vision.SubjectSegmentation

**Start version**: 5.0.0(12)

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

Image instance.

 |
| 

config

 | 

[SegmentationConfig](#section1268211401742)

 | 

No

 | 

Optional configuration for salient subject segmentation, including the maximum number of subjects and whether to output detailed information about each subject.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[SegmentationResult](#section747541297)\>

 | 

Salient subject result.

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

1011000001

 | 

Failed to run, please try again.

 |
| 

1011000002

 | 

The service is abnormal.

 |

**Example**:

import { subjectSegmentation } from '@kit.CoreVisionKit';
import { image } from '@kit.ImageKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';
import { photoAccessHelper } from '@kit.MediaLibraryKit';

const TAG: string = 'ImageSegmentationSample';

async function subjectSegmentationTest() {
  let chooseImage: image.PixelMap | undefined = undefined;
  let maxNum: string = '20';

  // Select an image from the gallery.
  let PhotoSelectOptions = new photoAccessHelper.PhotoSelectOptions();
  PhotoSelectOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE\_TYPE;
  PhotoSelectOptions.maxSelectNumber = 1;
  let photoPicker: photoAccessHelper.PhotoViewPicker = new photoAccessHelper.PhotoViewPicker();
  let PhotoSelectResult = await photoPicker.select(PhotoSelectOptions);
  let uris = PhotoSelectResult.photoUris;

  if (uris.length !== 1) {
    hilog.info(0x0000, TAG, 'Selected uris length is not 1');
    return;
  }

  // Convert the selected image into **PixelMap**.
  let fileSource = await fileIo.open(uris\[0\], fileIo.OpenMode.READ\_ONLY);
  let imageSource = image.createImageSource(fileSource.fd);
  chooseImage = await imageSource.createPixelMap();

  if (!chooseImage) {
    hilog.info(0x0000, TAG, 'chooseImage is undefined');
    return;
  }
  if (fileSource) {
    try {
      await fileIo.close(fileSource);
    } catch (err) {
      hilog.error(0x0000, TAG, \`Failed to close fileSource. Code: ${err.code}, message: ${err.message}\`);
    }
  }

  // Call the image segmentation API.
  let visionInfo: subjectSegmentation.VisionInfo = {
    pixelMap: chooseImage
  };
  let config: subjectSegmentation.SegmentationConfig = {
    maxCount: parseInt(maxNum),
    enableSubjectDetails: true,
    enableSubjectForegroundImage: true
  };
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

  hilog.info(0x0000, TAG, 'Segmentation result: ' + outputString);
}

@Entry
@Component
struct Page {

  build() {
    Column(){
      Button('subjectSegmentationTest').onClick(() => {
        subjectSegmentationTest().catch((err: BusinessError) => {
          hilog.error(0x0000, TAG, \`Failed to segment a photo. code: ${err.code}, message: ${err.message}\`);
        });
      })
    }
  }
}
