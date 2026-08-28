# skeletonDetection (Skeleton Detection)

The skeleton detection service identifies key points of the human body from an image, such as the head, shoulders, elbows, wrists, hips, knees, and ankles, and provides their location coordinates along with confidence scores. Skeleton detection is an underlying AI capability and can be used together with other AI capabilities in Core Vision Kit, such as facial recognition and text recognition, to develop more intelligent apps.

**Start version**: 5.0.0(12)

#### Module Import

import { visionBase, skeletonDetection } from '@kit.CoreVisionKit';

#### SkeletonPointType

Enumeration of skeleton point types.

**System capability**: SystemCapability.AI.Vision.SkeletonDetection

**Start version**: 5.0.0(12)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

NOSE

 | 

0

 | 

Nose.

 |
| 

LEFT\_EYE

 | 

1

 | 

Left eye.

 |
| 

RIGHT\_EYE

 | 

2

 | 

Right eye.

 |
| 

LEFT\_EAR

 | 

3

 | 

Left ear.

 |
| 

RIGHT\_EAR

 | 

4

 | 

Right ear.

 |
| 

LEFT\_SHOULDER

 | 

5

 | 

Left shoulder.

 |
| 

RIGHT\_SHOULDER

 | 

6

 | 

Right shoulder.

 |
| 

LEFT\_ELBOW

 | 

7

 | 

Left elbow.

 |
| 

RIGHT\_ELBOW

 | 

8

 | 

Right elbow.

 |
| 

LEFT\_WRIST

 | 

9

 | 

Left wrist.

 |
| 

RIGHT\_WRIST

 | 

10

 | 

Right wrist.

 |
| 

LEFT\_HIP

 | 

11

 | 

Left hip.

 |
| 

RIGHT\_HIP

 | 

12

 | 

Right hip.

 |
| 

LEFT\_KNEE

 | 

13

 | 

Left knee.

 |
| 

RIGHT\_KNEE

 | 

14

 | 

Right knee.

 |
| 

LEFT\_ANKLE

 | 

15

 | 

Left ankle.

 |
| 

RIGHT\_ANKLE

 | 

16

 | 

Right ankle.

 |

#### SkeletonPoint

Detailed skeleton point information.

**System capability**: SystemCapability.AI.Vision.SkeletonDetection

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

point

 | 

visionBase.[Point](../visionbase-core-vision-kit-base-class/document.md#section1465431712919)

 | 

No

 | 

No

 | 

Coordinates of a skeleton point in an image.

 |
| 

score

 | 

number

 | 

No

 | 

No

 | 

Confidence score of a skeleton point. The value range is (0,1). The value **0** indicates the lowest confidence, and the value **1** indicates the highest confidence. A higher confidence score indicates a more reliable location of a point.

 |
| 

type

 | 

[SkeletonPointType](#section4298938144913)

 | 

No

 | 

No

 | 

Type of a skeleton point, that is, the position of a skeleton point in the human skeleton model.

 |

#### Skeleton

Describes a complete skeleton detection result, including the overall confidence score, the approximate position of the human body in an image, as well as the position and type of each key point in detail.

**System capability**: SystemCapability.AI.Vision.SkeletonDetection

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

boundingBox

 | 

visionBase.[BoundingBox](../visionbase-core-vision-kit-base-class/document.md#section789716171126)

 | 

No

 | 

No

 | 

Skeleton bounding box, which is a rectangular box containing all skeleton points.

 |
| 

score

 | 

number

 | 

No

 | 

No

 | 

Overall confidence score. The value ranges from 0 to 1. The value **0** indicates the lowest confidence, and the value **1** indicates the highest confidence. It reflects the overall credibility of the skeleton.

 |
| 

points

 | 

Array<[SkeletonPoint](#section674171818172)\>

 | 

No

 | 

No

 | 

Object array containing skeleton point details.

 |

#### SkeletonDetectionResponse

Complete results of a skeleton detection. As the top-level output of skeleton detection, all the results of a detection are encapsulated in it. It inherits from [Response](../visionbase-core-vision-kit-base-class/document.md#section13793135121418) of **visionBase**.

**System capability**: SystemCapability.AI.Vision.SkeletonDetection

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

skeletons

 | 

Array<[Skeleton](#section49341529125412)\>

 | 

No

 | 

No

 | 

Result set of the skeleton points for all people in an image.

 |

#### SkeletonDetector

Defines the APIs and basic structures of skeleton detection. It inherits from the [visionBase.Analyzer](../visionbase-core-vision-kit-base-class/document.md#section6867321337) class. It has the following functions:

-   **private constructor()**: This is a private constructor. It means that **SkeletonDetector** cannot be directly instantiated by using the **new** keyword. Instead, an instance must be created by using the **create()** static method.
-   **static create(): Promise<SkeletonDetector>**: This is a static method used to create a **SkeletonDetector** instance. It returns the result asynchronously through a promise.
-   **process(request: visionBase.Request): Promise<SkeletonDetectionResponse>**: This is an instance method used to process skeleton detection requests. It returns the result asynchronously through a promise.
-   **destroy(): Promise<void>**: This is an instance method used to destroy the skeleton detection process. It returns the result asynchronously through a promise.

**System capability**: SystemCapability.AI.Vision.SkeletonDetection

**Start version**: 5.0.0(12)

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

constructor

 | 

You must use the **static create()** method to create a **SkeletonDetector** instance.

 |
| 

create

 | 

API for initializing skeleton detection.

 |
| 

process

 | 

API for executing skeleton detection.

 |
| 

destroy

 | 

API for destroying a skeleton detection process.

 |

#### \[h2\]create

static create(): Promise<SkeletonDetector>

Initializes skeleton detection. This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.AI.Vision.SkeletonDetection

**Start version**: 5.0.0(12)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[SkeletonDetector](#section1372216360530)\>

 | 

[SkeletonDetector](#section1372216360530) instance, which is returned through a promise.

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

import { skeletonDetection } from '@kit.CoreVisionKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

async function createAndDestroyDetector() {
  const detector = await skeletonDetection.SkeletonDetector.create();
  if (detector) {
    hilog.info(0x0000, 'skeletonDetectionSample', 'Skeleton detector created successfully');
  } else {
    hilog.error(0x0000,'skeletonDetectionSample','Failed to create Skeleton detector');
    return;
  }
  // Use the detector to perform some operations.
  // ...

  // Destroy the detector.
  if (detector) {
    await detector.destroy();
    hilog.info(0x0000, 'skeletonDetectionSample', 'Skeleton detector destroyed successfully');
  } else {
    hilog.error(0x0000,'skeletonDetectionSample','Failed to destroy Skeleton detector');
  }
}

@Entry
@Component
struct Page {

  build() {
    Column(){
      Button('createAndDestroyDetector').onClick(() => {
        createAndDestroyDetector()
      })
    }
  }
}

#### \[h2\]destroy

destroy(): Promise<void>

Destroys a skeleton detection process. This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.AI.Vision.SkeletonDetection

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

**Promise** object without a return value.

 |

**Example**:

import { skeletonDetection } from '@kit.CoreVisionKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

async function createAndDestroyDetector() {
  const detector = await skeletonDetection.SkeletonDetector.create();
  if (detector) {
    hilog.info(0x0000, 'skeletonDetectionSample', 'Skeleton detector created successfully');
  } else {
    hilog.error(0x0000,'skeletonDetectionSample','Failed to create Skeleton detector');
    return;
  }
  // Use the detector to perform some operations.
  // ...

  // Destroy the detector.
  if (detector) {
    await detector.destroy();
    hilog.info(0x0000, 'skeletonDetectionSample', 'Skeleton detector destroyed successfully');
  } else {
    hilog.error(0x0000,'skeletonDetectionSample','Failed to destroy Skeleton detector');
  }
}

@Entry
@Component
struct Page {

  build() {
    Column(){
      Button('createAndDestroyDetector').onClick(() => {
        createAndDestroyDetector()
      })
    }
  }
}

#### \[h2\]process

process(request: visionBase.Request): Promise<SkeletonDetectionResponse>

Creates a skeleton detection instance and performs skeleton detection. This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.AI.Vision.SkeletonDetection

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

request

 | 

visionBase.[Request](../visionbase-core-vision-kit-base-class/document.md#section6430105121211)

 | 

Yes

 | 

Image instance. Only one image can be passed for skeleton detection.

For details about the specifications, please refer to [Restrictions](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/core-vision-introduction#section625292610522).

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[SkeletonDetectionResponse](#section1565918285820)\>

 | 

Skeleton detection result.

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
| 

1011000001

 | 

Failed to run, please try again.

 |
| 

1011000003

 | 

Failed to run the model, please try again.

 |
| 

1011000004

 | 

Running the model timed out. Try again later.

 |

**Example**:

import { skeletonDetection, visionBase } from '@kit.CoreVisionKit';
import { image } from '@kit.ImageKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';
import { photoAccessHelper } from '@kit.MediaLibraryKit';

let imageSource: image.ImageSource | undefined = undefined;
let chooseImage: image.PixelMap | undefined = undefined;

// Create a skeleton detector.
let detector: skeletonDetection.SkeletonDetector | undefined = undefined;

async function createDetector() {
  detector = await skeletonDetection.SkeletonDetector.create();
  hilog.info(0x0000, 'skeletonDetectionSample', 'Skeleton detector created successfully');
}

@Entry
@Component
struct Page {

  build() {
    Column(){
      Button('Button').onClick(() => {
        // Convert the image into **PixelMap**. The image can be obtained from the gallery.
        let photoPicker: photoAccessHelper.PhotoViewPicker = new photoAccessHelper.PhotoViewPicker();
        photoPicker.select({
          MIMEType: photoAccessHelper.PhotoViewMIMETypes.IMAGE\_TYPE,
          maxSelectNumber: 1
        }).then((res: photoAccessHelper.PhotoSelectResult) => {
          let uri = res.photoUris\[0\];
          if (uri === undefined) {
            hilog.info(0x0000, 'skeletonDetectionSample', 'uri is undefined');
            return
          }
          setTimeout(async () => {
            let file = await fileIo.open(uri, fileIo.OpenMode.READ\_ONLY);
            imageSource = image.createImageSource(file.fd);
            chooseImage = await imageSource.createPixelMap();
            hilog.info(0x0000, 'skeletonDetectionSample', 'chooseImage:', chooseImage);
            if (!chooseImage) {
              return
            }

            // Create a detector.
            await createDetector();

            if (!detector) {
              hilog.error(0x0000, 'skeletonDetectionSample', 'Detector is not initialized');
              return;
            }

            // Call the skeleton detection API.
            let request: visionBase.Request = {
              inputData: { pixelMap: chooseImage },
              scene: visionBase.SceneMode.FOREGROUND
            };

            let response: skeletonDetection.SkeletonDetectionResponse = await detector.process(request);

            if (response.skeletons.length === 0) {
              hilog.info(0x0000, 'skeletonDetectionSample', 'No skeletons detected in the image.');
            } else {
              hilog.info(0x0000, 'skeletonDetectionSample', \`Detected ${response.skeletons.length} skeletons.\`);
              response.skeletons.forEach((skeleton, index) => {
                hilog.info(0x0000, 'skeletonDetectionSample', \`  Score: ${skeleton.score}\`);
                hilog.info(0x0000, 'skeletonDetectionSample', \`  Number of points: ${skeleton.points.length}\`);
                skeleton.points.forEach(point => {
                  hilog.info(0x0000, 'skeletonDetectionSample', \`    ${skeletonDetection.SkeletonPointType\[point.type\]}: (${point.point.x}, ${point.point.y}), Score: ${point.score}\`);
                });
              });
            }

            // Clear resources.
            if (chooseImage && imageSource) {
              chooseImage.release();
              imageSource.release();
            }
            if (file) {
              try {
                await fileIo.close(file);
              } catch (err) {
                hilog.error(0x0000, 'skeletonDetectionSample', \`Failed to close fileSource. Code: ${err.code}, message: ${err.message}\`);
              }
            }
            if (detector) {
              await detector.destroy();
              hilog.info(0x0000, 'skeletonDetectionSample', 'Skeleton detector destroyed successfully');
            }
          }, 100);
        }).catch((err: BusinessError) => {
          hilog.error(0x0000, 'skeletonDetectionSample', \`Failed to get photo image uri. code: ${err.code}, message: ${err.message}\`);
        });
      })
    }
  }
}
