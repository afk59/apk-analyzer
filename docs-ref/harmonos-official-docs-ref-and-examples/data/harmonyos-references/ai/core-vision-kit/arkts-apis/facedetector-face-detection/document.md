# faceDetector (Face Detection)

The face detection service supports the capability of detecting 2D faces. It detects the number of faces, facial position, feature points (left and right eye centers, nose, and mouth corners), and posture (pitch, roll, and yaw) in a specified image. Bounding boxes of detected faces are sorted by size.

Compared with the Vision Kit face liveness detection service used for videos, this face detection service is used for images.

**Start version**: 5.0.0(12)

#### Module Import

import { faceDetector } from '@kit.CoreVisionKit';

#### VisionInfo

Visual information to be recognized. Currently, only the visual information of the **PixelMap** type in color data format RGBA\_8888 is supported.

**Atomic service API**: This API can be used in atomic services since API version 5.0.2(14).

**System capability**: SystemCapability.AI.Face.Detector

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

#### FaceRecognitionConfiguration

Configuration of face occlusion detection.

**System capability**: SystemCapability.AI.Face.Detector

**Start version**: 5.0.2(14)

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

faceBlock

 | 

boolean

 | 

Yes

 | 

No

 | 

Indicates whether to enable face occlusion detection.

The value **true** indicates yes, and the value **false** indicates no. The default value is **false**.

 |

#### FaceBlock

Enumeration of face occlusion detection results.

**System capability**: SystemCapability.AI.Face.Detector

**Start version**: 5.0.2(14)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

UNINITIALIZED

 | 

\-1

 | 

Face occlusion detection is not enabled.

 |
| 

UNBLOCKED

 | 

0

 | 

Not occluded.

 |
| 

BLOCKED

 | 

1

 | 

Occluded.

 |

#### FacePoint

Pixel point position.

**Atomic service API**: This API can be used in atomic services since API version 5.0.2(14).

**System capability**: SystemCapability.AI.Face.Detector

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

#### FacePose

Direction of a face in 3D space. For details about the coordinate system, please refer to the [world coordinate system](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/core-vision-face-detector#section17390143819516).

**Atomic service API**: This API can be used in atomic services since API version 5.0.2(14).

**System capability**: SystemCapability.AI.Face.Detector

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

yaw

 | 

number

 | 

Yes

 | 

No

 | 

Angle of moving a head left and right, that is, rotating around the vertical Y axis (**localRotationY**). Value range: \[–180, 180\]

 |
| 

pitch

 | 

number

 | 

Yes

 | 

No

 | 

Angle of moving a head up and down, that is, rotating around the transverse X axis (**localRotationX**). Value range: \[–180, 180\]

 |
| 

roll

 | 

number

 | 

Yes

 | 

No

 | 

Angle of tilting a head from side to side, that is, rotating around the sagittal Z axis (**localRotationZ**). Value range: \[–180, 180\]

 |

#### FaceRectangle

Bounding box of a face.

**Atomic service API**: This API can be used in atomic services since API version 5.0.2(14).

**System capability**: SystemCapability.AI.Face.Detector

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

Yes

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

Yes

 | 

No

 | 

Y coordinate of the upper left corner of a bounding box.

 |
| 

width

 | 

number

 | 

Yes

 | 

No

 | 

Width of a bounding box, in pixels.

 |
| 

height

 | 

number

 | 

Yes

 | 

No

 | 

Height of a bounding box, in pixels.

 |

#### Face

Face information list.

**System capability**: SystemCapability.AI.Face.Detector

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

probability

 | 

number

 | 

Yes

 | 

No

 | 

Confidence of the face detection result. The value is a floating point number ranging from 0 to 1. A larger value indicates a higher confidence.

**Atomic service API**: This API can be used in atomic services since API version 5.0.2(14).

 |
| 

block

 | 

[FaceBlock](#section13470323960)

 | 

Yes

 | 

Yes

 | 

Face occlusion result.

**Start version**: 5.0.2(14)

 |
| 

pose

 | 

[FacePose](#section1268211401742)

 | 

Yes

 | 

No

 | 

Face pose.

**Atomic service API**: This API can be used in atomic services since API version 5.0.2(14).

 |
| 

rect

 | 

[FaceRectangle](#section19644831362)

 | 

Yes

 | 

No

 | 

Face bounding box list.

**Atomic service API**: This API can be used in atomic services since API version 5.0.2(14).

 |
| 

points

 | 

Array<[FacePoint](#section789716171126)\>

 | 

Yes

 | 

No

 | 

Array of facial landmarks, including the left and right eye centers, nose, as well as left and right mouth corners. The sequence is as follows: left eye center, right eye center, nose, left mouth corner, and right mouth corner.

**Atomic service API**: This API can be used in atomic services since API version 5.0.2(14).

 |

#### faceDetector.init

init(): Promise<boolean>

Initializes the face detection service. This API returns the result asynchronously through a promise.

**Atomic service API**: This API can be used in atomic services since API version 5.0.2(14).

**System capability**: SystemCapability.AI.Face.Detector

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

import { faceDetector } from '@kit.CoreVisionKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

async function initAndReleaseFaceDetector() {
  // Initialize the face detection service.
  const initResult = await faceDetector.init();
  hilog.info(0x0000, 'faceDetectorSample', \`Face detector initialization result:${initResult}\`);

  if (initResult) {
    hilog.info(0x0000, 'faceDetectorSample', 'Face detector initialized successfully');

    // Add the code for using the face detection service.

    // Release the face detection service after the usage is complete.
    await faceDetector.release();
    hilog.info(0x0000, 'faceDetectorSample', 'Face detector released successfully');
  } else {
    hilog.error(0x0000, 'faceDetectorSample', 'Failed to initialize face detector');
  }
}

@Entry
@Component
struct Page {

  build() {
    Column(){
      Button('initAndReleaseFaceDetector').onClick(() => {
        // Call the function.
        initAndReleaseFaceDetector();
      })
    }
  }
}

#### faceDetector.init

init(faceRecognitionConfiguration: FaceRecognitionConfiguration): Promise<boolean>

Initializes the face occlusion detection service. In the same process, as long as one face detection service has occlusion detection enabled and this service has not been released, all other face detection services within that process will also have occlusion detection enabled. This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.AI.Face.Detector

**Start version**: 5.0.2(14)

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

faceRecognitionConfiguration

 | 

[FaceRecognitionConfiguration](#section1821372213619)

 | 

Yes

 | 

Configuration of face occlusion detection.

 |

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

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

The parameter check failed.

 |

**Example**:

import { faceDetector } from '@kit.CoreVisionKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

async function initAndReleaseFaceDetector() {
  let config: faceDetector.FaceRecognitionConfiguration = {
    faceBlock: true
  }
  // Initialize the face occlusion detection service.
  const initResult = await faceDetector.init(config);
  hilog.info(0x0000, 'faceDetectorSample', \`Face detector initialization result:${initResult}\`);

  if (initResult) {
    hilog.info(0x0000, 'faceDetectorSample', 'Face detector initialized successfully');

    // Add the code for using the face detection service.

    // Release the face detection service after the usage is complete.
    await faceDetector.release();
    hilog.info(0x0000, 'faceDetectorSample', 'Face detector released successfully');
  } else {
    hilog.error(0x0000, 'faceDetectorSample', 'Failed to initialize face detector');
  }
}

@Entry
@Component
struct Page {

  build() {
    Column(){
      Button('initAndReleaseFaceDetector').onClick(() => {
        // Call the function.
        initAndReleaseFaceDetector();
      })
    }
  }
}

#### faceDetector.release

release(): Promise<void>

Releases the face detection service. This API returns the result asynchronously through a promise.

**Atomic service API**: This API can be used in atomic services since API version 5.0.2(14).

**System capability**: SystemCapability.AI.Face.Detector

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

import { faceDetector } from '@kit.CoreVisionKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

async function initAndReleaseFaceDetector() {
  // Initialize the face detection service.
  const initResult = await faceDetector.init();
  hilog.info(0x0000, 'faceDetectorSample', \`Face detector initialization result:${initResult}\`);

  if (initResult) {
    hilog.info(0x0000, 'faceDetectorSample', 'Face detector initialized successfully');

    // Add the code for using the face detection service.

    // Release the face detection service after the usage is complete.
    await faceDetector.release();
    hilog.info(0x0000, 'faceDetectorSample', 'Face detector released successfully');
  } else {
    hilog.error(0x0000, 'faceDetectorSample', 'Failed to initialize face detector');
  }
}

@Entry
@Component
struct Page {

  build() {
    Column(){
      Button('initAndReleaseFaceDetector').onClick(() => {
        // Call the function.
        initAndReleaseFaceDetector();
      })
    }
  }
}

#### faceDetector.detect

detect(visionInfo: VisionInfo): Promise<Array<Face>>

Detects face information in an image. This API returns the result asynchronously through a promise.

**Atomic service API**: This API can be used in atomic services since API version 5.0.2(14).

**System capability**: SystemCapability.AI.Face.Detector

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

[VisionInfo](#section14488135133518)

 | 

Yes

 | 

Image instance (including faces).

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<Array<[Face](#section747541297)\>>

 | 

Face detection result returned through a promise.

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

1008800001

 | 

Failed to run, please try again.

 |
| 

1008800002

 | 

The service is abnormal.

 |

**Example**:

import { faceDetector } from '@kit.CoreVisionKit';
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
  MIMEType: photoAccessHelper.PhotoViewMIMETypes.IMAGE\_TYPE,
  maxSelectNumber: 1
}).then((res: photoAccessHelper.PhotoSelectResult) => {
  let uri = res.photoUris\[0\];
  if (uri === undefined) {
    hilog.info(0x0000, 'faceDetectorSample', 'uri is undefined');
    return
  }
  setTimeout(async () => {
    let file = await fileIo.open(uri, fileIo.OpenMode.READ\_ONLY);
    imageSource = image.createImageSource(file.fd);
    chooseImage = await imageSource.createPixelMap();
    hilog.info(0x0000, 'faceDetectorSample', 'chooseImage:', chooseImage);
    if (!chooseImage) {
      return
    }
    // Call the face detection API.
    let visionInfo: faceDetector.VisionInfo = {
      pixelMap: chooseImage
    };
    let data: faceDetector.Face\[\] = await faceDetector.detect(visionInfo);
    if (data.length === 0) {
      hilog.info(0x0000, 'faceDetectorSample', 'No face is detected in the image.');
    } else {
      let faceString = JSON.stringify(data);
      hilog.info(0x0000, 'faceDetectorSample', 'faceString data is ' + faceString);
    }

    if (chooseImage && imageSource) {
      chooseImage.release();
      imageSource.release();
    }
    if (file) {
      try {
        await fileIo.close(file);
      } catch (err) {
        hilog.error(0x0000, 'faceDetectorSample', \`Failed to close fileSource. Code: ${err.code}, message: ${err.message}\`);
      }
    }
  }, 100);
}).catch((err: BusinessError) => {
  hilog.error(0x0000, 'faceDetectorSample', \`Failed to get photo image uri. code: ${err.code}, message: ${err.message}\`);
});

@Entry
@Component
struct Page {

  build() {
    Column(){
    }
  }
}
