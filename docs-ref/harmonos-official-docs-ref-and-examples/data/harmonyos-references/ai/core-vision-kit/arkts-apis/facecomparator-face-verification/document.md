# faceComparator (Face Verification)

The face verification service recognizes faces, performs high-precision comparison of human faces, and provides confidence scores to determine whether the faces belong to the same person. This cutting-edge technology can be used to intelligently categorize and manage photos. The on-device intelligent image recognition algorithm ensures accurate face recognition, enabling your app to provide better user experience.

**Start version**: 5.0.0(12)

#### Module Import

import { faceComparator } from '@kit.CoreVisionKit';

#### VisionInfo

Visual information to be recognized. Currently, only the visual information of the PixelMap type in color data format RGBA\_8888 is supported.

**System capability**: SystemCapability.AI.Face.Comparator

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

Yes

 | 

No

 | 

Image to be recognized.

For details about the specifications, please refer to [Restrictions](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/core-vision-introduction#section625292610522).

 |

#### FaceCompareResult

Face verification result.

**System capability**: SystemCapability.AI.Face.Comparator

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

isSamePerson

 | 

boolean

 | 

Yes

 | 

No

 | 

Indicates whether the faces belong to the same person. The value **true** indicates yes, and the value **false** indicates no.

 |
| 

similarity

 | 

number

 | 

Yes

 | 

No

 | 

Similarity. The value is a floating point number ranging from 0 to 1. A larger value indicates a higher similarity.

 |

#### faceComparator.init

init(): Promise<boolean>

Initializes the face verification service. This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.AI.Face.Comparator

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

import { faceComparator } from '@kit.CoreVisionKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

async function initAndReleaseFaceComparator() {
  // Initialize the face verification service.
  const initResult = await faceComparator.init();
  hilog.info(0x0000, 'faceComparatorSample', \`Face comparator initialization result:${initResult}\`);

  if (initResult) {
    hilog.info(0x0000, 'faceComparatorSample', 'Face comparator initialized successfully');

    // Add the code for using the face verification service.

    // Release the face verification service after the usage is complete.
    await faceComparator.release();
    hilog.info(0x0000, 'faceComparatorSample', 'Face comparator released successfully');
  } else {
    hilog.error(0x0000, 'faceComparatorSample', 'Failed to initialize face comparator');
  }
}

@Entry
@Component
struct Page {

  build() {
    Column(){
      Button('initAndReleaseFaceComparator').onClick(() => {
        // Call the function.
        initAndReleaseFaceComparator();
      })
    }
  }
}

#### faceComparator.release

release(): Promise<void>

Releases the face verification service. This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.AI.Face.Comparator

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

import { faceComparator } from '@kit.CoreVisionKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

async function initAndReleaseFaceComparator() {
  // Initialize the face verification service.
  const initResult = await faceComparator.init();
  hilog.info(0x0000, 'faceComparatorSample', \`Face comparator initialization result:${initResult}\`);

  if (initResult) {
    hilog.info(0x0000, 'faceComparatorSample', 'Face comparator initialized successfully');

    // Add the code for using the face verification service.

    // Release the face verification service after the usage is complete.
    await faceComparator.release();
    hilog.info(0x0000, 'faceComparatorSample', 'Face comparator released successfully');
  } else {
    hilog.error(0x0000, 'faceComparatorSample', 'Failed to initialize face comparator');
  }
}

@Entry
@Component
struct Page {

  build() {
    Column(){
      Button('initAndReleaseFaceComparator').onClick(() => {
        // Call the function.
        initAndReleaseFaceComparator();
      })
    }
  }
}

#### faceComparator.compareFaces

compareFaces(visionInfo1: VisionInfo, visionInfo2: VisionInfo): Promise<FaceCompareResult>

Creates a face verification instance. This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.AI.Face.Comparator

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

visionInfo1

 | 

[VisionInfo](#section674171818172)

 | 

Yes

 | 

First image that contains a face.

 |
| 

visionInfo2

 | 

[VisionInfo](#section674171818172)

 | 

Yes

 | 

Second image that contains a face.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[FaceCompareResult](#section1518613358392)\>

 | 

Face verification result returned through a promise.

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

1008400001

 | 

Failed to run, please try again.

 |
| 

1008400002

 | 

The service is abnormal.

 |

**Example**:

import { faceComparator } from '@kit.CoreVisionKit';
import { image } from '@kit.ImageKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';
import { photoAccessHelper } from '@kit.MediaLibraryKit';

async function faceCompareTest() {
  let chooseImage: PixelMap | undefined = undefined;
  let chooseImage1: PixelMap | undefined = undefined;

  // Select two images from the gallery.
  let PhotoSelectOptions = new photoAccessHelper.PhotoSelectOptions();
  PhotoSelectOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE\_TYPE;
  PhotoSelectOptions.maxSelectNumber = 2;
  let photoPicker: photoAccessHelper.PhotoViewPicker = new photoAccessHelper.PhotoViewPicker();
  let PhotoSelectResult = await photoPicker.select(PhotoSelectOptions);
  let uris = PhotoSelectResult.photoUris;

  if (uris.length !== 2) {
    hilog.info(0x0000, 'testTag', 'selected uris length is not 2');
    return;
  }

  // Convert the selected images into **PixelMap**.
  let fileSource = await fileIo.open(uris\[0\], fileIo.OpenMode.READ\_ONLY);
  let imageSource = image.createImageSource(fileSource.fd);
  chooseImage = await imageSource.createPixelMap();

  fileSource = await fileIo.open(uris\[1\], fileIo.OpenMode.READ\_ONLY);
  imageSource = image.createImageSource(fileSource.fd);
  chooseImage1 = await imageSource.createPixelMap();

  if (!chooseImage || !chooseImage1) {
    hilog.info(0x0000, 'testTag', 'chooseImage or chooseImage1 is undefined');
    return;
  }

  // Call the face verification API.
  let visionInfo: faceComparator.VisionInfo = {
    pixelMap: chooseImage
  };
  let visionInfo1: faceComparator.VisionInfo = {
    pixelMap: chooseImage1
  };

  let data: faceComparator.FaceCompareResult = await faceComparator.compareFaces(visionInfo, visionInfo1);
  let similarity = (data.similarity \* 100).toFixed(2);
  let isSamePerson = data.isSamePerson ? 'is' : 'is not';
  let faceString = \`Similarity: ${similarity}%. ${isSamePerson} the same person\`;
  hilog.info(0x0000, 'testTag', 'faceString data is ' + faceString);

  // Release resources.
  if (chooseImage && chooseImage1) {
    chooseImage.release();
    chooseImage1.release();
  }
  if (fileSource) {
    try {
      await fileIo.close(fileSource);
    } catch (err) {
      hilog.error(0x0000, 'testTag', \`Failed to close fileSource. Code: ${err.code}, message: ${err.message}\`);
    }
  }
}

@Entry
@Component
struct Page {

  build() {
    Column(){
      Button('faceCompareTest').onClick(() => {
        faceCompareTest().catch((err: BusinessError) => {
          hilog.error(0x0000, 'faceCompareSample', \`Failed to compare faces. code: ${err.code}, message: ${err.message}\`);
        });
      })
    }
  }
}
