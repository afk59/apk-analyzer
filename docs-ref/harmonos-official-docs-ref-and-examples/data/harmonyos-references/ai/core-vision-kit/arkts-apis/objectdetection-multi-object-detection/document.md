# objectDetection (Multi-object Detection)

The multi-object detection service identifies multiple objects from an image. Images in various scenarios are converted into digital images through optical input methods such as photographing and video recording. Then, the images are analyzed using underlying AI capabilities to locate and identify multiple objects of interest, such as faces, animals, and plants, so that users can extract information such as the object type, bounding box position, and confidence score.

Currently, this service can recognize the following types of objects: landscapes, animals, plants, buildings, faces, tables, texts, human heads, cat heads, dog heads, food, cars, human bodies, documents, and cards.

**Start version**: 5.0.0(12)

#### Module Import

import { visionBase, objectDetection } from '@kit.CoreVisionKit';

#### VisionObject

Visual information object.

**System capability**: SystemCapability.AI.Vision.ObjectDetection

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

Bounding box of **visionObject**.

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

Confidence score of **visionObject**. The value range is (0,1). The value **0** indicates the lowest confidence, and the value **1** indicates the highest confidence. A higher confidence score indicates a more reliable location of an object.

 |
| 

labels

 | 

Array<number>

 | 

No

 | 

No

 | 

Object label, which indicates the type of an object.

-   **0**: landscape
-   **1**: animal
-   **2**: plant
-   **3**: building
-   **5**: face
-   **6**: form
-   **7**: text
-   **8**: human head
-   **9**: cat head
-   **10**: dog head
-   **11**: food
-   **12**: vehicle
-   **13**: human body
-   **21**: document
-   **22**: card

 |
| 

id

 | 

number

 | 

No

 | 

No

 | 

Unique identifier of **visionObject**. The ID is an integer starting from 0 and incrementing sequentially.

 |

#### ObjectDetectionResponse

Multi-object detection result class. It inherits from [Response](../visionbase-core-vision-kit-base-class/document.md#section13793135121418) of the base class **visionBase**.

**System capability**: SystemCapability.AI.Vision.ObjectDetection

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

objects

 | 

Array<[VisionObject](#section674171818172)\>

 | 

No

 | 

No

 | 

Multi-object detection result. The value can be an object or an object array.

 |

#### ObjectDetector

Defines the APIs and basic structures of multi-object detection. It inherits from the [visionBase.Analyzer](../visionbase-core-vision-kit-base-class/document.md#section6867321337) class. It has the following functions:

-   **private constructor()**: This is a private constructor. It means that **ObjectDetector** cannot be directly instantiated by using the **new** keyword. Instead, an instance must be created by using the **create()** static method.
-   **static create(): Promise<ObjectDetector>**: This is a static method used to create an **ObjectDetector** instance. It returns the result asynchronously through a promise.
-   **process(request: visionBase.Request): Promise<ObjectDetectionResponse>**: This is an instance method used to process multi-object detection requests. It returns the result asynchronously through a promise.
-   **destroy(): Promise<void>**: This is an instance method used to destroy a multi-object detection process. It returns the result asynchronously through a promise.

**System capability**: SystemCapability.AI.Vision.ObjectDetection

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

You must use the **static create()** method to create an **ObjectDetector** instance.

 |
| 

create

 | 

API for initializing multi-object detection.

 |
| 

process

 | 

API for executing multi-object detection.

 |
| 

destroy

 | 

API for destroying a multi-object detection process.

 |

#### \[h2\]create

static create(): Promise<ObjectDetector>

Initializes multi-object detection. This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.AI.Vision.ObjectDetection

**Start version**: 5.0.0(12)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[ObjectDetector](#section1372216360530)\>

 | 

**ObjectDetector** instance, which is returned through a promise.

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

import { objectDetection } from '@kit.CoreVisionKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

async function createAndDestroyDetector() {
  const detector = await objectDetection.ObjectDetector.create();
  if (detector) {
    hilog.info(0x0000, 'objectDetectionSample', 'Object detector created successfully');
  } else {
    hilog.error(0x0000,'objectDetectionSample','Failed to create object detector');
    return;
  }
  // Use the detector to perform some operations.
  // ...

  // Destroy the detector.
  if (detector) {
    await detector.destroy();
    hilog.info(0x0000, 'objectDetectionSample', 'Object detector destroyed successfully');
  } else {
    hilog.error(0x0000,'objectDetectionSample','Failed to destroy object detector');
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

Destroys a multi-object detection process. This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.AI.Vision.ObjectDetection

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

import { objectDetection } from '@kit.CoreVisionKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

async function createAndDestroyDetector() {
  const detector = await objectDetection.ObjectDetector.create();
  if (detector) {
    hilog.info(0x0000, 'objectDetectionSample', 'Object detector created successfully');
  } else {
    hilog.error(0x0000,'objectDetectionSample','Failed to create object detector');
    return;
  }
  // Use the detector to perform some operations.
  // ...

  // Destroy the detector.
  if (detector) {
    await detector.destroy();
    hilog.info(0x0000, 'objectDetectionSample', 'Object detector destroyed successfully');
  } else {
    hilog.error(0x0000,'objectDetectionSample','Failed to destroy object detector');
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

process(request: visionBase.Request): Promise<ObjectDetectionResponse>

Creates a multi-object detection instance and performs multi-object detection. This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.AI.Vision.ObjectDetection

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

Image instance. Only one image can be passed for multi-object detection.

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

Promise<[ObjectDetectionResponse](#section6430105121211)\>

 | 

Multi-object detection result.

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

import { objectDetection, visionBase } from '@kit.CoreVisionKit';
import { image } from '@kit.ImageKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';
import { photoAccessHelper } from '@kit.MediaLibraryKit';

let imageSource: image.ImageSource | undefined = undefined;
let chooseImage: image.PixelMap | undefined = undefined;

// Create an object detector.
let detector: objectDetection.ObjectDetector | undefined = undefined;

async function createDetector() {
  detector = await objectDetection.ObjectDetector.create();
  hilog.info(0x0000, 'objectDetectionSample', 'Object detector created successfully');
}

@Entry
@Component
struct Page {

  build() {
    Column(){
      Button('Start').onClick(() => {
        // Convert the image into **PixelMap**. The image can be obtained from the gallery.
        let photoPicker: photoAccessHelper.PhotoViewPicker = new photoAccessHelper.PhotoViewPicker();
        photoPicker.select({
          MIMEType: photoAccessHelper.PhotoViewMIMETypes.IMAGE\_TYPE,
          maxSelectNumber: 1
        }).then((res: photoAccessHelper.PhotoSelectResult) => {
          let uri = res.photoUris\[0\];
          if (uri === undefined) {
            hilog.info(0x0000, 'objectDetectionSample', 'uri is undefined');
            return
          }
          setTimeout(async () => {
            let file = await fileIo.open(uri, fileIo.OpenMode.READ\_ONLY);
            imageSource = image.createImageSource(file.fd);
            chooseImage = await imageSource.createPixelMap();
            hilog.info(0x0000, 'objectDetectionSample', 'chooseImage:', chooseImage);
            if (!chooseImage) {
              return
            }

            // Create a detector.
            await createDetector();

            if (!detector) {
              hilog.error(0x0000, 'objectDetectionSample', 'Detector is not initialized');
              return;
            }

            // Call the object detection API.
            let request: visionBase.Request = {
              inputData: { pixelMap: chooseImage },
              scene: visionBase.SceneMode.FOREGROUND
            };

            let response: objectDetection.ObjectDetectionResponse = await detector.process(request);

            if (response.objects.length === 0) {
              hilog.info(0x0000, 'objectDetectionSample', 'No objects detected in the image.');
            } else {
              let objectString = JSON.stringify(response.objects);
              hilog.info(0x0000, 'objectDetectionSample', 'Detected objects: ' + objectString);
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
                hilog.error(0x0000, 'objectDetectionSample', \`Failed to close fileSource. Code: ${err.code}, message: ${err.message}\`);
              }
            }
            if (detector) {
              await detector.destroy();
              hilog.info(0x0000, 'objectDetectionSample', 'Object detector destroyed successfully');
            }
          }, 100);
        }).catch((err: BusinessError) => {
          hilog.error(0x0000, 'objectDetectionSample', \`Failed to get photo image uri. code: ${err.code}, message: ${err.message}\`);
        });
      })
    }
  }
}
