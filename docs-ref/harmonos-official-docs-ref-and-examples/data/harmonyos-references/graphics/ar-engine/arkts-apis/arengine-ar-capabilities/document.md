# arEngine (AR Capabilities)

This module provides APIs related to arEngine (AR capabilities) of AR Engine.

**System capability**: SystemCapability.AREngine.Core

**Start version**: 5.1.0(18)

#### Modules to Import

import { arEngine } from '@kit.AREngine';

#### ARAddAugmentedImageMode

Enumerates the image adding modes.

**System capability**: SystemCapability.AREngine.Core

**Start version**: 5.1.0(18)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

NORMAL

 | 

0

 | 

Normal mode.

If the number of images added exceeds the default maximum number (50), AR Engine reports an error. For details, please refer to [1009200011](../../ar-engine-error-codes/document.md#section4676153191213).

 |
| 

UPDATE

 | 

1

 | 

Update mode.

If the number of images added exceeds the default maximum number (50), AR Engine deletes the earliest data to add new images.

 |

#### ARAddAugmentedImageReason

Enumerates the causes of image adding failures.

**System capability**: SystemCapability.AREngine.Core

**Start version**: 5.1.0(18)

| 
**Name**

 | 

**Value**

 | 

**Description**

 |
| :-- | :-- | :-- |
| 

NONE

 | 

0

 | 

No failure cause is reported, and the image is added successfully.

 |
| 

SIZE\_NOT\_MATCH

 | 

1

 | 

The image dimensions are incorrect.

NOTE:

The image dimensions are evaluated from the aspect ratio and resolution. It is recommended that the image aspect ratio and resolution have a minimum rating of **Fit**.

 |
| 

LIGHT\_ANOMALY

 | 

2

 | 

The image is too bright or too dark.

 |
| 

FEATURE\_LIMIT

 | 

3

 | 

The image color is monotonous. For example, the image is a pure color image.

 |
| 

OTHER

 | 

4

 | 

Other reasons, such as light reflection, light spot, and repetitive content.

 |

-   Aspect ratio
    
    Ratio of the image width to the height. For example, for an image with the resolution of 640 × 480 pixels, the aspect ratio is 1.33, which corresponds to a rating of **Excellent**.
    
    | 
    Image Aspect Ratio
    
     | 
    
    Rating
    
     |
    | :-- | :-- |
    | 
    
    \[6, ∞)
    
     | 
    
    Invalid
    
     |
    | 
    
    \[4, 6)
    
     | 
    
    Bad
    
     |
    | 
    
    \[2.5, 4)
    
     | 
    
    Unfit
    
     |
    | 
    
    \[2, 2.5)
    
     | 
    
    Fit
    
     |
    | 
    
    \[1.5, 2)
    
     | 
    
    Good
    
     |
    | 
    
    \[1, 1.5)
    
     | 
    
    Excellent
    
     |
    
-   Resolution
    
    The image resolution ratio is calculated based on the reference resolution 640 × 480 pixels. For example, if an image's resolution is 320 × 240 pixels, its ratio is 0.5, which corresponds to a rating of **Fit**.
    
    | 
    Image Resolution Ratio
    
     | 
    
    Rating
    
     |
    | :-- | :-- |
    | 
    
    \[0, 0.2\]
    
     | 
    
    Invalid
    
     |
    | 
    
    (0.2, 0.3\]
    
     | 
    
    Bad
    
     |
    | 
    
    (0.35, 0.45\]
    
     | 
    
    Unfit
    
     |
    | 
    
    (0.45, 0.7\]
    
     | 
    
    Fit
    
     |
    | 
    
    (0.7, 0.9\]
    
     | 
    
    Good
    
     |
    | 
    
    (0.9, ∞)
    
     | 
    
    Excellent
    
     |
    

#### ARDepthMode

Enumerates the depth modes.

**System capability**: SystemCapability.AREngine.Core

**Start version**: 5.1.0(18)

| 
**Name**

 | 

Value

 | 

**Description**

 |
| :-- | :-- | :-- |
| 

DISABLED

 | 

0

 | 

The depth mode is disabled.

 |
| 

AUTOMATIC

 | 

1

 | 

The depth mode is enabled.

AR Engine automatically attempts to obtain depth information from various depth sources.

NOTE:

Typically, there are two types of depth sources: motion algorithms and Time of Flight (ToF) sensors.

Currently, only motion algorithms are supported.

 |

#### ARFocusMode

Enumerates the focus modes.

**System capability**: SystemCapability.AREngine.Core

**Start version**: 5.1.0(18)

| 
**Name**

 | 

Value

 | 

**Description**

 |
| :-- | :-- | :-- |
| 

FIXED

 | 

0

 | 

Fixed focus mode.

 |
| 

AUTO

 | 

1

 | 

Auto focus mode.

 |

#### ARImageFormat

Enumerates the image data formats.

**System capability**: SystemCapability.AREngine.Core

**Start version**: 5.1.0(18)

| 
**Name**

 | 

Value

 | 

**Description**

 |
| :-- | :-- | :-- |
| 

UNKNOWN

 | 

0

 | 

Invalid image format.

 |
| 

YUV\_420\_888

 | 

2

 | 

YUV\_420\_888 format, which is suitable for processing high-resolution image data.

 |
| 

Y\_8

 | 

3

 | 

Y\_8 format, which is suitable for scenarios requiring lower precision or smaller storage for image data.

 |
| 

Y\_16

 | 

4

 | 

Y\_16 format, which is suitable for scenarios requiring higher precision for image data.

 |

#### ARMeshMode

Enumerates the mesh modes.

**System capability**: SystemCapability.AREngine.Core

**Start version**: 5.1.0(18)

| 
**Name**

 | 

Value

 | 

**Description**

 |
| :-- | :-- | :-- |
| 

DISABLED

 | 

0

 | 

The mesh mode is disabled.

AR Engine does not process or display mesh data.

 |
| 

ENABLE

 | 

1

 | 

The mesh mode is enabled.

AR Engine attempts to process and display mesh data.

 |

#### ARPlaneFindingMode

Enumerates the plane finding modes.

**System capability**: SystemCapability.AREngine.Core

**Start version**: 5.1.0(18)

| 
**Name**

 | 

Value

 | 

**Description**

 |
| :-- | :-- | :-- |
| 

DISABLED

 | 

0

 | 

Plane finding is disabled.

 |
| 

HORIZONTAL

 | 

1

 | 

Only horizontal planes, such as floors and tables, are detected.

 |
| 

VERTICAL

 | 

2

 | 

Only vertical planes, such as walls, are detected.

 |
| 

HORIZONTAL\_AND\_VERTICAL

 | 

3

 | 

Both horizontal and vertical planes are detected.

 |

#### ARPlaneType

Enumerates the plane types.

**System capability**: SystemCapability.AREngine.Core

**Start version**: 5.1.0(18)

| 
**Name**

 | 

Value

 | 

**Description**

 |
| :-- | :-- | :-- |
| 

FACING\_HORIZONTAL\_UPWARD

 | 

0

 | 

Upward-facing horizontal plane, such as ground and table platforms.

 |
| 

FACING\_HORIZONTAL\_DOWNWARD

 | 

1

 | 

Downward-facing horizontal plane, such as the ceiling.

 |
| 

FACING\_VERTICAL

 | 

2

 | 

Vertical plane, such as the wall.

 |
| 

FACING\_INVALID

 | 

3

 | 

Invalid or unsupported plane type.

This may occur due to changes in the environment, lighting conditions, or other factors.

 |

#### ARPointOrientationMode

Enumerates the orientation modes.

**System capability**: SystemCapability.AREngine.Core

**Start version**: 5.1.0(18)

| 
**Name**

 | 

Value

 | 

**Description**

 |
| :-- | :-- | :-- |
| 

INITIALIZED\_TO\_IDENTITY

 | 

0

 | 

The orientation is consistent with that of the world coordinate system, but with minor adjustments.

 |
| 

ESTIMATED\_SURFACE\_NORMAL

 | 

1

 | 

The orientation is determined by the estimated plane's normal vector.

The orientation of the point is the same as that of the plane. This mode is applicable to the application scenario where the orientation of the point needs to be determined based on the plane characteristics.

 |

#### ARPoseMode

Enumerates the ways to create a world coordinate system.

**System capability**: SystemCapability.AREngine.Core

**Start version**: 5.1.0(18)

| 
**Name**

 | 

Value

 | 

**Description**

 |
| :-- | :-- | :-- |
| 

GRAVITY

 | 

0

 | 

Determined by gravity.

The Y axis of the world coordinate system is consistent with the gravity direction, and the origin is the original location of the device. For details, please refer to [AR Engine Gravity Aligned with World Coordinate System](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arengine-coordinate#section51232054151614).

 |
| 

GRAVITY\_AND\_HEADING

 | 

1

 | 

Determined by gravity and compass.

The Y axis of the world coordinate system is consistent with the gravity direction, the X axis points to the north of the compass, and the origin is the original location of the device. For details, please refer to [AR Engine Gravity Aligned with Northward Coordinate System](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arengine-coordinate#section1786771621711).

CAUTION:

This option is supported only in power saving mode. Set [ARPowerMode](#section9223439153519) to **POWER\_SAVING** to enable this option.

 |

#### ARPoseType

Enumerates the pose types.

**System capability**: SystemCapability.AREngine.Core

**Start version**: 5.1.0(18)

| 
**Name**

 | 

Value

 | 

**Description**

 |
| :-- | :-- | :-- |
| 

IDENTITY

 | 

0

 | 

Default state, that is, no rotation or translation.

 |
| 

ROTATE\_90

 | 

1

 | 

Rotated by 90 degrees in clockwise direction.

 |
| 

ROTATE\_180

 | 

2

 | 

Rotated by 180 degrees in clockwise direction.

 |
| 

ROTATE\_270

 | 

3

 | 

Rotated by 270 degrees in clockwise direction.

 |

#### ARPowerMode

Enumerates the power consumption modes.

**System capability**: SystemCapability.AREngine.Core

**Start version**: 5.1.0(18)

| 
**Name**

 | 

Value

 | 

**Description**

 |
| :-- | :-- | :-- |
| 

NORMAL

 | 

0

 | 

Normal mode.

AR Engine maintains a counterbalance between performance and power consumption.

 |
| 

POWER\_SAVING

 | 

1

 | 

Energy saving mode.

AR Engine prioritizes reducing power consumption, which may result in lower performance in exchange for extended battery life.

 |
| 

PERFORMANCE\_FIRST

 | 

2

 | 

Performance-preferred mode.

AR Engine prioritizes performance, offering higher processing capabilities and faster response times. However, this may lead to increased power consumption.

 |
| 

BOOST

 | 

3

 | 

Mode of outputting the device pose information only.

AR Engine only outputs the device pose information, and the power consumption is lower than that in normal mode. In this mode, plane-related settings such as [ARPlaneFindingMode](#section764515681310) do not take effect.

 |
| 

ULTRA\_POWER\_SAVING

 | 

11

 | 

Ultra power-saving mode.

AR Engine further reduces power consumption, which is lower than that in power-saving mode. This may result in more significant performance trade-offs.

 |

#### ARSemanticDenseMode

Enumerates the recognition modes of high-precision geometric reconstruction.

**System capability**: SystemCapability.AREngine.Core

**Start version**: 6.0.0(20)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

DISABLED

 | 

0

 | 

The high-precision geometric reconstruction recognition mode is disabled.

 |
| 

NORMAL

 | 

1

 | 

Normal mode, where only dense point cloud recognition is enabled.

 |
| 

CUBE\_VOLUME

 | 

2

 | 

Cube volume measurement mode.

 |
| 

CUBE\_SPACE

 | 

3

 | 

Cube space volume measurement mode.

 |

#### ARSemanticMode

Enumerates the semantic modes.

**System capability**: SystemCapability.AREngine.Core

**Start version**: 5.1.0(18)

| 
**Name**

 | 

Value

 | 

**Description**

 |
| :-- | :-- | :-- |
| 

NONE

 | 

0

 | 

Semantics not used.

 |
| 

PLANE

 | 

1

 | 

Plane semantic mode used.

 |

#### ARSemanticPlaneLabel

Enumerates the semantic types detected by the current plane.

**System capability**: SystemCapability.AREngine.Core

**Start version**: 5.1.0(18)

| 
**Name**

 | 

Value

 | 

**Description**

 |
| :-- | :-- | :-- |
| 

UNKNOWN

 | 

0

 | 

Unknown plane type.

 |
| 

WALL

 | 

1

 | 

Wall.

 |
| 

FLOOR

 | 

2

 | 

Floor.

 |
| 

SEAT

 | 

3

 | 

A seat, such as a chair or stool.

 |
| 

TABLE

 | 

4

 | 

Table.

 |
| 

CEILING

 | 

5

 | 

Ceiling.

 |
| 

DOOR

 | 

6

 | 

Door.

 |
| 

WINDOW

 | 

7

 | 

Window.

 |
| 

BED

 | 

8

 | 

Bed.

 |
| 

PLANE\_SPACE

 | 

9

 | 

Plane space.

**Start version**: 6.0.0(20)

 |
| 

CUBE\_VOLUME

 | 

10

 | 

Cube volume.

**Start version**: 6.0.0(20)

 |
| 

CUBE\_SPACE

 | 

11

 | 

Cube space volume.

**Start version**: 6.0.0(20)

 |

#### ARTrackingState

Enumerates the tracking states of trackable objects.

**System capability**: SystemCapability.AREngine.Core

**Start version**: 5.1.0(18)

| 
**Name**

 | 

Value

 | 

**Description**

 |
| :-- | :-- | :-- |
| 

TRACKING

 | 

0

 | 

Tracking.

 |
| 

PAUSED

 | 

1

 | 

Tracking paused.

 |
| 

STOPPED

 | 

2

 | 

Tracking stopped.

 |

#### ARTrackingStateReason

Enumerates the tracking failure causes.

**System capability**: SystemCapability.AREngine.Core

**Start version**: 5.1.0(18)

| 
**Name**

 | 

Value

 | 

**Description**

 |
| :-- | :-- | :-- |
| 

NONE

 | 

0

 | 

Unknown cause.

This may occur because the system is temporarily unable to recognize trackable objects but is still attempting to track them.

 |
| 

EXCESSIVE\_MOTION

 | 

1

 | 

Target moving too fast.

The trackable object (such as a plane, point, or image) is moving too quickly, making it difficult for AR Engine to accurately identify and track it.

 |
| 

INSUFFICIENT\_FEATURES

 | 

2

 | 

Insufficient visual features.

The visual features of the trackable object are not rich enough, such as having unclear textures or overly uniform colors, preventing AR Engine from accurately identifying and tracking it.

 |

#### ARTrackableType

Enumerates the types of trackable objects, such as planes and points.

**System capability**: SystemCapability.AREngine.Core

**Start version**: 5.1.0(18)

| 
**Name**

 | 

Value

 | 

**Description**

 |
| :-- | :-- | :-- |
| 

BASE

 | 

0 × 41520100

 | 

Basic trackable object type, which is the default type of AR Engine.

 |
| 

PLANE

 | 

0 × 41520101

 | 

Trackable object of the plane type.

 |
| 

POINT

 | 

0 × 41520102

 | 

Trackable object of the point type.

 |
| 

AUGMENTED\_IMAGE

 | 

0 × 41520104

 | 

Trackable object of the augmented image type.

 |
| 

INVALID

 | 

0

 | 

Invalid trackable object type.

 |

#### ARType

Enumerates the AR capability types.

**System capability**: SystemCapability.AREngine.Core

**Start version**: 5.1.0(18)

| 
**Name**

 | 

Value

 | 

**Description**

 |
| :-- | :-- | :-- |
| 

WORLD

 | 

0 × 01

 | 

Environment tracking capability.

 |
| 

IMAGE

 | 

0 × 80

 | 

Image recognition capability.

 |

#### Distortion

type Distortion = \[number, number, number, number, number\]

Type alias, which is used to represent an array containing five digits and is the distortion coefficient of the camera.

**System capability**: SystemCapability.AREngine.Core

**Start version**: 5.1.0(18)

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

number

 | 

The value type is number. The data is intrinsic camera parameters. The value range is not limited.

**Distortion \[0\]** to **Distortion \[2\]** indicate k1, k2, and k3 (radial distortion coefficients), and **Distortion \[3\]** to **Distortion \[4\]** indicate tangential distortion coefficients.

 |

#### ARAugmentedImageDatabase

Augmented image database object.

Represents related operations on the augmented image database, such as serialization, deserialization, image adding, and image quantity obtaining.

**System capability**: SystemCapability.AREngine.Core

**Start version**: 5.1.0(18)

#### \[h2\]ARAugmentedImageDatabase.deserialize

deserialize(buffer: ArrayBuffer): Promise<void>

Deserializes the data of the augmented image database to a new augmented image database object.

This API returns the result asynchronously through a promise.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/aDsQNwtQQgOLB4GoiNglIg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062445Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=87D7A1E2A3D630BA56BF1F98A8E5AF171F8CCE2B6EE0672508F5BBCF14BCADCF)

This operation is time-consuming. You are advised to run it in the background thread.

**System capability**: SystemCapability.AREngine.Core

**Start version**: 5.1.0(18)

**Parameters**:

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

buffer

 | 

ArrayBuffer

 | 

Yes

 | 

**ArrayBuffer** data of the augmented image database.

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

Promise<void>

 | 

Promise object that returns no value.

 |

**Error codes**:

For details about the error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [AR Engine Error Codes](../../ar-engine-error-codes/document.md).

| 
**Error Code**

 | 

**Error Message**

 |
| :-- | :-- |
| 

401

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |
| 

1009200001

 | 

Failure.

 |
| 

1009200008

 | 

Resource exhausted.

 |

**Example**:

import { arEngine } from '@kit.AREngine';

async function deserialize(): Promise<void> {
  let buffer: ArrayBuffer = new ArrayBuffer(0);
  let imageDatabase: arEngine.ARAugmentedImageDatabase = await arEngine.createARAugmentedImageDatabase();
  await imageDatabase.deserialize(buffer);
}

#### \[h2\]ARAugmentedImageDatabase.serialize

serialize(): Promise<ArrayBuffer>

Serializes the data of the augmented image database into a buffer.

This API returns the **ArrayBuffer** object asynchronously through a promise.

**System capability**: SystemCapability.AREngine.Core

**Start version**: 5.1.0(18)

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

Promise<ArrayBuffer>

 | 

Promise object, which returns an **ArrayBuffer** object.

ArrayBuffer is a buffer that stores the serialized data of the augmented image database.

 |

**Error codes**:

For details about the error codes, please refer to [AR Engine Error Codes](../../ar-engine-error-codes/document.md).

| 
**Error Code**

 | 

**Error Message**

 |
| :-- | :-- |
| 

1009200001

 | 

Failure.

 |

**Example**:

import { arEngine } from '@kit.AREngine';

async function serialize(): Promise<void> {
  let imageDatabase: arEngine.ARAugmentedImageDatabase = await arEngine.createARAugmentedImageDatabase();
  let buffer: ArrayBuffer = await imageDatabase.serialize();
}

#### \[h2\]ARAugmentedImageDatabase.addImage

addImage(name: string, pixelMap: image.PixelMap, widthInMeters: number): Promise<ARAddAugmentedImageResult>

Adds an image to the image database and outputs the index of the image.

This API returns the **ARAddAugmentedImageResult** object asynchronously through a promise.

**System capability**: SystemCapability.AREngine.Core

**Start version**: 5.1.0(18)

**Parameters**:

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

name

 | 

string

 | 

Yes

 | 

Image name.

The value cannot be empty and can contain a maximum of 255 characters. If the value contains more than 255 characters, the excess characters will be discarded.

 |
| 

pixelMap

 | 

[image.PixelMap](../../../../media/image-kit/arkts-apis/ohos-multimedia-sendableimage-image-processing-based-on-sendable-objects/document.md#pixelmap)

 | 

Yes

 | 

Image information.

 |
| 

widthInMeters

 | 

number

 | 

Yes

 | 

Actual physical width of an object in an image.

The width is not limited, in meters. The default value is the size of an A4 paper.

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

Promise<[ARAddAugmentedImageResult](#section67121231105218)\>

 | 

Promise object, which returns the **ARAddAugmentedImageResult** object.

**ARAddAugmentedImageResult** is a data object that indicates the result of adding an augmented image.

 |

**Error codes**:

For details about the error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [AR Engine Error Codes](../../ar-engine-error-codes/document.md).

| 
**Error Code**

 | 

**Error Message**

 |
| :-- | :-- |
| 

401

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |
| 

1009200001

 | 

Failure.

 |
| 

1009200008

 | 

Resource exhausted.

 |
| 

1009200011

 | 

The number of images added exceeds the maximum.

 |
| 

1009200012

 | 

Attempted to add an image with insufficient quality to the image database.

 |

**Example**:

import { image } from '@kit.ImageKit';
import { arEngine } from '@kit.AREngine';

async function addImage(): Promise<void> {
  let color: ArrayBuffer = new ArrayBuffer(96); // 96 is the size of the pixel buffer to create. The value is calculated as follows: height \* width \*4.
  let opts: image.InitializationOptions = {
    editable: true,
    pixelFormat: image.PixelMapFormat.RGBA\_8888,
    size: { height: 4, width: 6 }
  }
  let pixelMap: image.PixelMap = image.createPixelMapSync(color, opts);
  let imageDatabase: arEngine.ARAugmentedImageDatabase = await arEngine.createARAugmentedImageDatabase();
  let addImageResult: arEngine.ARAddAugmentedImageResult = await imageDatabase.addImage('xx', pixelMap, 0.3);
}

#### \[h2\]ARAugmentedImageDatabase.getImageCount

getImageCount(): number

Obtains the number of images in the image database.

**System capability**: SystemCapability.AREngine.Core

**Start version**: 5.1.0(18)

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

number

 | 

Number of images.

 |

**Error codes**:

For details about the error codes, please refer to [AR Engine Error Codes](../../ar-engine-error-codes/document.md).

| 
**Error Code**

 | 

**Error Message**

 |
| :-- | :-- |
| 

1009200001

 | 

Failure.

 |

**Example**:

import { arEngine } from '@kit.AREngine';

async function getImageCount(): Promise<void> {
  let imageDatabase: arEngine.ARAugmentedImageDatabase = await arEngine.createARAugmentedImageDatabase();
  let imageCount: number = imageDatabase.getImageCount();
}

#### \[h2\]ARAugmentedImageDatabase.getCapacity

getCapacity(): number

Obtains the maximum number of images that can be added.

**System capability**: SystemCapability.AREngine.Core

**Start version**: 5.1.0(18)

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

number

 | 

Maximum number of images that can be added.

 |

**Error codes**:

For details about the error codes, please refer to [AR Engine Error Codes](../../ar-engine-error-codes/document.md).

| 
**Error Code**

 | 

**Error Message**

 |
| :-- | :-- |
| 

1009200001

 | 

Failure.

 |

**Example**:

import { arEngine } from '@kit.AREngine';

async function getCapacity(): Promise<void> {
  let imageDatabase: arEngine.ARAugmentedImageDatabase = await arEngine.createARAugmentedImageDatabase();
  let imageCapacity: number = imageDatabase.getCapacity();
}

#### \[h2\]ARAugmentedImageDatabase.getImageAddMode

getImageAddMode(): ARAddAugmentedImageMode

Obtains the image adding mode.

**System capability**: SystemCapability.AREngine.Core

**Start version**: 5.1.0(18)

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[ARAddAugmentedImageMode](#section913918490464)

 | 

Image adding mode.

 |

**Error codes**:

For details about the error codes, please refer to [AR Engine Error Codes](../../ar-engine-error-codes/document.md).

| 
**Error Code**

 | 

**Error Message**

 |
| :-- | :-- |
| 

1009200001

 | 

Failure.

 |

**Example**:

import { arEngine } from '@kit.AREngine';

async function getImageAddMode(): Promise<void> {
  let imageDatabase: arEngine.ARAugmentedImageDatabase = await arEngine.createARAugmentedImageDatabase();
  let addImageMode: arEngine.ARAddAugmentedImageMode = imageDatabase.getImageAddMode();
}

#### \[h2\]ARAugmentedImageDatabase.setImageAddMode

setImageAddMode(mode: ARAddAugmentedImageMode): void

Sets the image adding mode.

**System capability**: SystemCapability.AREngine.Core

**Start version**: 5.1.0(18)

**Parameters**:

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

mode

 | 

[ARAddAugmentedImageMode](#section913918490464)

 | 

Yes

 | 

Image adding mode.

 |

**Error codes**:

For details about the error codes, please refer to [AR Engine Error Codes](../../ar-engine-error-codes/document.md).

| 
**Error Code**

 | 

**Error Message**

 |
| :-- | :-- |
| 

1009200001

 | 

Failure.

 |

**Example**:

import { arEngine } from '@kit.AREngine';

async function setImageAddMode(): Promise<void> {
  let imageDatabase: arEngine.ARAugmentedImageDatabase = await arEngine.createARAugmentedImageDatabase();
  imageDatabase.setImageAddMode(arEngine.ARAddAugmentedImageMode.UPDATE);
}

#### \[h2\]ARAugmentedImageDatabase.release

release(): Promise<void>

Releases the memory occupied by the [ARAugmentedImageDatabase](#section1410345414514) object.

This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.AREngine.Core

**Start version**: 5.1.0(18)

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

Promise<void>

 | 

Promise object that returns no value.

 |

**Error codes**:

For details about the error codes, please refer to [AR Engine Error Codes](../../ar-engine-error-codes/document.md).

| 
**Error Code**

 | 

**Error Message**

 |
| :-- | :-- |
| 

1009200001

 | 

Failure.

 |

**Example**:

import { arEngine } from '@kit.AREngine';

async function release(): Promise<void> {
  let imageDatabase: arEngine.ARAugmentedImageDatabase = await arEngine.createARAugmentedImageDatabase();
  await imageDatabase.release();
}

#### ARCameraIntrinsics

Defines intrinsic camera parameters.

Includes **fx**, **fy**, **cx**, **cy**, and distortion parameters.

**System capability**: SystemCapability.AREngine.Core

**Start version**: 5.1.0(18)

| 
Name

 | 

**Type**

 | 

**Read-Only**

 | 

**Optional**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

fx

 | 

number

 | 

Yes

 | 

No

 | 

Focal length of the camera on the X axis.

Any value is acceptable.

 |
| 

fy

 | 

number

 | 

Yes

 | 

No

 | 

Focal length of the camera on the Y axis.

Any value is acceptable.

 |
| 

cx

 | 

number

 | 

Yes

 | 

No

 | 

Principal point of the camera on the X axis.

Any value is acceptable.

 |
| 

cy

 | 

number

 | 

Yes

 | 

No

 | 

Principal point of the camera on the Y axis.

Any value is acceptable.

 |
| 

distortion

 | 

[Distortion](#section4381141123516)

 | 

Yes

 | 

No

 | 

Distortion parameter of the camera.

 |

#### ARConfig

Defines the configuration parameters of [ARSession](#section19193165314510).

**System capability**: SystemCapability.AREngine.Core

**Start version**: 5.1.0(18)

| 
Name

 | 

**Type**

 | 

**Read-Only**

 | 

**Optional**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

type

 | 

[ARType](#section1712356171319)

 | 

No

 | 

No

 | 

AR capability type.

 |
| 

planeFindingMode

 | 

[ARPlaneFindingMode](#section764515681310)

 | 

No

 | 

Yes

 | 

Plane finding mode.

The default value is **HORIZONTAL\_AND\_VERTICAL**.

 |
| 

powerMode

 | 

[ARPowerMode](#section9223439153519)

 | 

No

 | 

Yes

 | 

Power consumption mode.

The default value is **NORMAL**.

 |
| 

focusMode

 | 

[ARFocusMode](#section6848111619409)

 | 

No

 | 

Yes

 | 

Focus mode.

The default value is **FIXED**.

 |
| 

semanticMode

 | 

[ARSemanticMode](#section19325205718138)

 | 

No

 | 

Yes

 | 

Semantic mode.

The default value is **NONE**.

 |
| 

maxMapSize

 | 

number

 | 

No

 | 

Yes

 | 

Maximum memory size (MB) for storing map data. The value ranges from 100 MB to 16 GB. The default value is **800 MB**.

You are advised to set the memory size based on the memory capacity of the device. If the memory size exceeds the hardware limit, unexpected errors may occur.

 |
| 

poseMode

 | 

[ARPoseMode](#section342619402359)

 | 

No

 | 

Yes

 | 

World coordinate system creation mode.

The default value is **GRAVITY**.

 |
| 

depthMode

 | 

[ARDepthMode](#section947895524619)

 | 

No

 | 

Yes

 | 

Depth mode.

The default value is **DISABLED**.

 |
| 

meshMode

 | 

[ARMeshMode](#section111790505464)

 | 

No

 | 

Yes

 | 

Mesh mode.

The default value is **DISABLED**.

 |
| 

addAugmentedImageMode

 | 

[ARAddAugmentedImageMode](#section913918490464)

 | 

No

 | 

Yes

 | 

Image adding mode.

The default value is **NORMAL**.

 |
| 

semanticDenseMode

 | 

[ARSemanticDenseMode](#section162053411246)

 | 

No

 | 

Yes

 | 

Recognition mode of high-precision geometric reconstruction.

The default value is **DISABLED**.

**Start version**: 6.0.0(20)

 |

#### ARPointCloud

Defines a collection of trackable 3D point clouds.

**System capability**: SystemCapability.AREngine.Core

**Start version**: 5.1.0(18)

| 
Name

 | 

**Type**

 | 

**Read-Only**

 | 

**Optional**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

timestamp

 | 

number

 | 

Yes

 | 

No

 | 

Timestamp of the current feature point cloud detection.

The unit is ns.

 |
| 

points

 | 

Array<number>

 | 

Yes

 | 

No

 | 

Coordinates of all points in the point cloud and the confidence array corresponding to the coordinates.

 |

#### ARSemanticDenseCubeData

Cube data of a high-precision geometric reconstruction object.

**System capability**: SystemCapability.AREngine.Core

**Start version**: 6.0.0(20)

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

id

 | 

number

 | 

Yes

 | 

No

 | 

ID of the current cube.

 |
| 

vertexSize

 | 

number

 | 

Yes

 | 

No

 | 

Number of vertices of the current cube.

 |
| 

vertexData

 | 

Array<number>

 | 

Yes

 | 

No

 | 

Vertex data of the current cube.

8 vertices corresponding to the cube. The index starts from the back surface of the cube and is arranged counterclockwise.

 |
| 

confidence

 | 

number

 | 

Yes

 | 

No

 | 

Confidence of the current cube. The value can be **0**, **1**, or **2**.

 |
| 

label

 | 

[ARSemanticPlaneLabel](#section5137195514137)

 | 

Yes

 | 

No

 | 

Semantic label of the current cube.

 |

#### ARSemanticDensePointData

Dense point cloud data of a high-precision geometric reconstruction object.

**System capability**: SystemCapability.AREngine.Core

**Start version**: 6.0.0(20)

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

id

 | 

ArrayBuffer

 | 

Yes

 | 

No

 | 

ID array of all points in the dense point cloud data.

NOTE:

If this parameter needs to be converted from the ArrayBuffer type to the int32 type, refer to [Data Type Conversion](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arengine-arraybuffer-info) to perform the conversion.

 |
| 

position

 | 

ArrayBuffer

 | 

Yes

 | 

No

 | 

Coordinates of all points in the dense point cloud data and their confidence arrays, in the format of \[x0, y0, z0, c0, x1, y1, z1, c1, x2, ...\].

NOTE:

If this parameter needs to be converted from the ArrayBuffer type to the float32 type, refer to [Data Type Conversion](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arengine-arraybuffer-info) to perform the conversion.

 |
| 

color

 | 

ArrayBuffer

 | 

Yes

 | 

No

 | 

Colors of all points in the dense point cloud data, in RGBA format. The format is \[r0, g0, b0, a0, r1, g1, b1, a1, r2, ...\].

NOTE:

If this parameter needs to be converted from the ArrayBuffer type to the int32 type, refer to [Data Type Conversion](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arengine-arraybuffer-info) to perform the conversion.

 |

#### ARSession

Manages the system status of AR Engine.

**System capability**: SystemCapability.AREngine.Core

**Start version**: 5.1.0(18)

#### \[h2\]ARSession.getFrame

getFrame(): ARFrame

Obtains a frame of data after AR Engine processing.

**System capability**: SystemCapability.AREngine.Core

**Start version**: 5.1.0(18)

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[ARFrame](#section83421523123819)

 | 

Returns a frame of data after AR Engine processing.

 |

**Error codes**:

For details about the error codes, please refer to [AR Engine Error Codes](../../ar-engine-error-codes/document.md).

| 
**Error Code**

 | 

**Error Message**

 |
| :-- | :-- |
| 

1009200001

 | 

Failure.

 |

**Example**:

import { arEngine, arViewController } from '@kit.AREngine';
import { Node } from '@kit.ArkGraphics3D';

class ARViewCallbackImpl extends arViewController.ARViewCallback {
  onAnchorAdd(ctx: arViewController.ARViewContext, node: Node, anchor: arEngine.ARAnchor): void {
    // ...
  }

  onAnchorUpdate(ctx: arViewController.ARViewContext, node: Node, anchor: arEngine.ARAnchor): void {
    // ...
  }

  async onFrameUpdate(ctx: arViewController.ARViewContext, sysBootTs: number): Promise<void> {
    if (!ctx.session) {
      // Exit if no session is created. For details about how to create a session, see the development guide.
      return;
    }

    let arSession: arEngine.ARSession = ctx.session;
    let frame: arEngine.ARFrame = arSession.getFrame();
    await frame.release();
  }
}

#### \[h2\]ARSession.createAnchor

createAnchor(pose: ARPose): ARAnchor

Creates an anchor for continuous tracking.

**System capability**: SystemCapability.AREngine.Core

**Start version**: 5.1.0(18)

**Parameters**:

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

pose

 | 

[ARPose](#section19274193834913)

 | 

Yes

 | 

Creates an anchor pose object.

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[ARAnchor](#section106411242143016)

 | 

Returns an anchor object.

 |

**Error codes**:

For details about the error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [AR Engine Error Codes](../../ar-engine-error-codes/document.md).

| 
**Error Code**

 | 

**Error Message**

 |
| :-- | :-- |
| 

401

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |
| 

1009200001

 | 

Failure.

 |

**Example**:

import { Quaternion, Vec3 } from '@kit.ArkGraphics3D';
import { arEngine } from '@kit.AREngine';

let r: Quaternion = {
  x: 0,
  y: 0,
  z: 0,
  w: 0
}
let t: Vec3 = { x: 0, y: 0, z: 0 };
let pose: arEngine.ARPose = arEngine.createARPose(r, t);
// Refer to the sample code of the ARSession.getFrame API for details about arSession creation.
let anchor: arEngine.ARAnchor= arSession.createAnchor(pose);

#### \[h2\]ARSession.detachAnchor

detachAnchor(anchor: ARAnchor): void

Stops tracking and unbinds the anchor.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/8IhfzxgHRmS58ioMy3-cQA/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062445Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BAAB60AFADA00D335B81B7F41FBFD0B3CDB6EF822EF97BB0FE73C5F5A1AD6C29)

This function does not release the anchor [ARAnchor](#section106411242143016). You need to call [ARAnchor.release](#section63641154194411) to release the anchor.

**System capability**: SystemCapability.AREngine.Core

**Start version**: 5.1.0(18)

**Parameters**:

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

anchor

 | 

[ARAnchor](#section106411242143016)

 | 

Yes

 | 

Anchor object to be unbound.

 |

**Error codes**:

For details about the error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [AR Engine Error Codes](../../ar-engine-error-codes/document.md).

| 
**Error Code**

 | 

**Error Message**

 |
| :-- | :-- |
| 

401

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |
| 

1009200001

 | 

Failure.

 |

**Example**:

import { arEngine } from '@kit.AREngine';

// Refer to the sample code of the ARSession.getFrame API for details about arSession creation.
let pose: arEngine.ARPose = arSession.getFrame().getCamera().getPose();
let anchor: arEngine.ARAnchor = arSession.createAnchor(pose);
arSession.detachAnchor(anchor);

#### \[h2\]ARSession.getAllAnchors

getAllAnchors(): Array<ARAnchor>

Obtains anchors in all states.

**System capability**: SystemCapability.AREngine.Core

**Start version**: 5.1.0(18)

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

Array<[ARAnchor](#section106411242143016)\>

 | 

Returns an array of anchor objects.

 |

**Error codes**:

For details about the error codes, please refer to [AR Engine Error Codes](../../ar-engine-error-codes/document.md).

| 
**Error Code**

 | 

**Error Message**

 |
| :-- | :-- |
| 

1009200001

 | 

Failure.

 |
| 

1009200008

 | 

Resource exhausted.

 |

**Example**:

import { arEngine } from '@kit.AREngine';

// Refer to the sample code of the ARSession.getFrame API for details about arSession creation.
let anchors: Array<arEngine.ARAnchor> = arSession.getAllAnchors();

#### \[h2\]ARSession.getAllTrackables

getAllTrackables(type: ARTrackableType): Array<ARTrackable>

Obtains all trackable objects of a specified type.

**System capability**: SystemCapability.AREngine.Core

**Start version**: 5.1.0(18)

**Parameters**:

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

[ARTrackableType](#section1725585684613)

 | 

Yes

 | 

Type of the trackable object.

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

Array<[ARTrackable](#section1710323720204)\>

 | 

Array of trackable objects.

 |

**Error codes**:

For details about the error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [AR Engine Error Codes](../../ar-engine-error-codes/document.md).

| 
**Error Code**

 | 

**Error Message**

 |
| :-- | :-- |
| 

401

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |
| 

1009200001

 | 

Failure.

 |
| 

1009200008

 | 

Resource exhausted.

 |

**Example**:

import { arEngine } from '@kit.AREngine';

// Refer to the sample code of the ARSession.getFrame API for details about arSession creation.
let allTrackables: Array<arEngine.ARTrackable> = arSession.getAllTrackables(arEngine.ARTrackableType.BASE);

#### \[h2\]ARSession.openFlash

openFlash(): Promise<boolean>

Enables the flash of the device.

This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.AREngine.Core

**Start version**: 5.1.0(18)

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

Promise<boolean>

 | 

Promise object. If **true** is returned, the flash function is enabled. If **false** is returned, the flash function is disabled.

 |

**Error codes**:

For details about the error codes, please refer to [AR Engine Error Codes](../../ar-engine-error-codes/document.md).

| 
**Error Code**

 | 

**Error Message**

 |
| :-- | :-- |
| 

1009200001

 | 

Failure.

 |

**Example**:

import { arEngine } from '@kit.AREngine';

async function openFlash(): Promise<void> {
  // Refer to the sample code of the ARSession.getFrame API for details about arSession creation.
  let result: boolean = await arSession.openFlash();
}

#### \[h2\]ARSession.closeFlash

closeFlash(): Promise<boolean>

Disables the flash of the device.

This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.AREngine.Core

**Start version**: 5.1.0(18)

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

Promise<boolean>

 | 

Promise object. If **true** is returned, the flash of the device is disabled. If **false** is returned, the flash of the device is enabled.

 |

**Error codes**:

For details about the error codes, please refer to [AR Engine Error Codes](../../ar-engine-error-codes/document.md).

| 
**Error Code**

 | 

**Error Message**

 |
| :-- | :-- |
| 

1009200001

 | 

Failure.

 |

**Example**:

import { arEngine } from '@kit.AREngine';

async function closeFlash(): Promise<void> {
  // Refer to the sample code of the ARSession.getFrame API for details about arSession creation.
  let result: boolean = await arSession.closeFlash();
}

#### \[h2\]ARSession.release

release(): Promise<void>

Releases the memory occupied by the [ARSession](#section19193165314510) object, which manages the AR Engine system status.

This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.AREngine.Core

**Start version**: 5.1.0(18)

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

Promise<void>

 | 

Promise object that returns no value.

 |

**Error codes**:

For details about the error codes, please refer to [AR Engine Error Codes](../../ar-engine-error-codes/document.md).

| 
**Error Code**

 | 

**Error Message**

 |
| :-- | :-- |
| 

1009200001

 | 

Failure.

 |

**Example**:

import { arEngine } from '@kit.AREngine';

async function release(): Promise<void> {
  // Refer to the sample code of the ARSession.getFrame API for details about arSession creation.
  await arSession.release();
}

#### ImageComponent

Basic structure parameters of an image component.

**System capability**: SystemCapability.AREngine.Core

**Start version**: 5.1.0(18)

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

rowStride

 | 

number

 | 

Yes

 | 

No

 | 

Number of bytes between the start positions of two consecutive pixel rows in an image. The line spacing is always greater than 0.

 |
| 

pixelStride

 | 

number

 | 

Yes

 | 

No

 | 

Number of bytes between the start points of two consecutive pixels in an image. The pixel pitch is always greater than 0.

 |
| 

buffer

 | 

ArrayBuffer

 | 

Yes

 | 

No

 | 

Buffer object of the planar data of the current frame.

NOTE:

If this type needs to be converted to the int32 type, refer to [Data Type Conversion](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arengine-arraybuffer-info) to perform the conversion.

 |

#### ARAddAugmentedImageResult

Adds augmented image results.

**System capability**: SystemCapability.AREngine.Core

**Start version**: 5.1.0(18)

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

index

 | 

number

 | 

No

 | 

No

 | 

Unique image index. The value ranges from 0 to 49.

 |
| 

state

 | 

number

 | 

No

 | 

No

 | 

Result status of adding an augmented image. If the operation is successful, the value is **0**. Otherwise, the value is an error code.

 |
| 

stateReason

 | 

[ARAddAugmentedImageReason](#section7453144131020)

 | 

No

 | 

No

 | 

Cause of the image adding failure.

 |

#### ARAnchor

Defines an anchor object.

An anchor, which describes the spatial location associated with a trackable object.

**System capability**: SystemCapability.AREngine.Core

**Start version**: 5.1.0(18)

**Parameters**:

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

id

 | 

number

 | 

Yes

 | 

No

 | 

Anchor index. The value ranges from 0 to 49.

 |
| 

trackingState

 | 

[ARTrackingState](#section16656547114620)

 | 

Yes

 | 

No

 | 

Tracking state of the trackable object.

 |

#### \[h2\]ARAnchor.getPose

getPose(): ARPose

Obtains the pose of the anchor in the world coordinate system.

**System capability**: SystemCapability.AREngine.Core

**Start version**: 5.1.0(18)

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[ARPose](#section19274193834913)

 | 

Pose object.

 |

**Error codes**:

For details about the error codes, please refer to [AR Engine Error Codes](../../ar-engine-error-codes/document.md).

| 
**Error Code**

 | 

**Error Message**

 |
| :-- | :-- |
| 

1009200001

 | 

Failure.

 |

**Example**:

import { arEngine } from '@kit.AREngine';

// Refer to the sample code of the ARSession.getFrame API for details about arSession creation.
let anchors: Array<arEngine.ARAnchor> = arSession.getAllAnchors();
let pose: arEngine.ARPose = anchors\[0\].getPose();

#### \[h2\]ARAnchor.detach

detach(): void

Stops tracking and unbinds the anchor.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/wC2w8Z4KSniTrKpOKnaihg/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062445Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=86A7CE4C6DE17B64E031790ECC20A6582D5CFD7CF840550835940CF8D20C4389)

This function does not release the anchor. You need to call [ARAnchor.release](#section63641154194411) to release the anchor.

**System capability**: SystemCapability.AREngine.Core

**Start version**: 5.1.0(18)

**Error codes**:

For details about the error codes, please refer to [AR Engine Error Codes](../../ar-engine-error-codes/document.md).

| 
**Error Code**

 | 

**Error Message**

 |
| :-- | :-- |
| 

1009200001

 | 

Failure.

 |

**Example**:

import { arEngine } from '@kit.AREngine';

// Refer to the sample code of the ARSession.getFrame API for details about arSession creation.
let anchors: Array<arEngine.ARAnchor> = arSession.getAllAnchors();
anchors\[0\].detach();

#### \[h2\]ARAnchor.release

release(): Promise<void>

Releases the memory occupied by the [ARAnchor](#section106411242143016) object.

This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.AREngine.Core

**Start version**: 5.1.0(18)

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

Promise<void>

 | 

Promise object that returns no value.

 |

**Error codes**:

For details about the error codes, please refer to [AR Engine Error Codes](../../ar-engine-error-codes/document.md).

| 
**Error Code**

 | 

**Error Message**

 |
| :-- | :-- |
| 

1009200001

 | 

Failure.

 |

**Example**:

import { arEngine } from '@kit.AREngine';

async function release(): Promise<void> {
  // Refer to the sample code of the ARSession.getFrame API for details about arSession creation.
  let anchors: Array<arEngine.ARAnchor> = arSession.getAllAnchors();
  await anchors\[0\].release();
}

#### ARAugmentedImage

Defines an augmented image object.

This class is inherited from the [ARTrackable](#section1710323720204) class.

**System capability**: SystemCapability.AREngine.Core

**Start version**: 5.1.0(18)

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

extendX

 | 

number

 | 

Yes

 | 

No

 | 

Estimated physical image width on the X axis, in meters. If the tracking state of the image is **PAUSED** or **STOPPED**, the returned width information is the width of the last tracking. If the image is not tracked, **0** is returned.

 |
| 

extendZ

 | 

number

 | 

Yes

 | 

No

 | 

Estimated physical image width on the Z axis, in meters. If the tracking state of the image is **PAUSED** or **STOPPED**, the returned width information is the width of the last tracking. If the image is not tracked, **0** is returned.

 |
| 

index

 | 

number

 | 

Yes

 | 

No

 | 

Index of an augmented image in the augmented image database. The value is a numeric value ranging from 1 to 50. It is the unique identifier of an image in the database.

 |
| 

name

 | 

string

 | 

Yes

 | 

No

 | 

Name of an augmented image. The value contains a maximum of 255 bytes and may not be unique.

 |

#### ARCamera

Camera information for the current frame.

**System capability**: SystemCapability.AREngine.Core

**Start version**: 5.1.0(18)

**Parameters**:

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

state

 | 

[ARTrackingState](#section16656547114620)

 | 

Yes

 | 

No

 | 

Tracking state of the trackable object.

 |
| 

stateReason

 | 

[ARTrackingStateReason](#section93821938193519)

 | 

Yes

 | 

No

 | 

Tracking failure cause.

 |
| 

viewMatrix

 | 

[Matrix4](../../../../application-framework/arkui/arkts-api/ui/arkui/graphics/document.md#matrix4)

 | 

Yes

 | 

No

 | 

View matrix of the camera in the latest frame.

 |

#### \[h2\]ARCamera.getPose

getPose(): ARPose

Obtains the pose of the camera in the world space.

For details about the pose information, please refer to [Coordinate System](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arengine-coordinate).

The pose information is available only when the status is **TRACKING**.

**System capability**: SystemCapability.AREngine.Core

**Start version**: 5.1.0(18)

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[ARPose](#section19274193834913)

 | 

Pose object.

 |

**Error codes**:

For details about the error codes, please refer to [AR Engine Error Codes](../../ar-engine-error-codes/document.md).

| 
**Error Code**

 | 

**Error Message**

 |
| :-- | :-- |
| 

1009200001

 | 

Failure.

 |

**Example**:

import { arEngine } from '@kit.AREngine';

// Refer to the sample code of the ARSession.getFrame API for details about arSession creation.
let frame: arEngine.ARFrame = arSession.getFrame();
let camera: arEngine.ARCamera = frame.getCamera();
let cameraPose: arEngine.ARPose = camera.getPose();

#### \[h2\]ARCamera.getDisplayOrientedPose

getDisplayOrientedPose(): ARPose

Obtains the pose of the virtual camera that faces the display in the world space.

For details about the pose information, please refer to [Coordinate System](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arengine-coordinate).

The pose information is available only when the status is **TRACKING**.

**System capability**: SystemCapability.AREngine.Core

**Start version**: 5.1.0(18)

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[ARPose](#section19274193834913)

 | 

Pose object.

 |

**Error codes**:

For details about the error codes, please refer to [AR Engine Error Codes](../../ar-engine-error-codes/document.md).

| 
**Error Code**

 | 

**Error Message**

 |
| :-- | :-- |
| 

1009200001

 | 

Failure.

 |

**Example**:

import { arEngine } from '@kit.AREngine';

// Refer to the sample code of the ARSession.getFrame API for details about arSession creation.
let frame: arEngine.ARFrame = arSession.getFrame();
let camera: arEngine.ARCamera = frame.getCamera();
let displayOrientedPose: arEngine.ARPose = camera.getDisplayOrientedPose();

#### \[h2\]ARCamera.getProjectionMatrix

getProjectionMatrix(near: number, far: number): Matrix4

Obtains the projection matrix used to render the virtual content on the camera image.

**System capability**: SystemCapability.AREngine.Core

**Start version**: 5.1.0(18)

**Parameters**:

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

near

 | 

number

 | 

Yes

 | 

Distance of the near clipping plane from the camera in the coordinate system, in meters. The value must be greater than 0.

 |
| 

far

 | 

number

 | 

Yes

 | 

Distance of the far clipping plane from the camera in the coordinate system, in meters. The value must be greater than 0 and greater than that of the near clipping plane from the camera in the coordinate system.

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[Matrix4](../../../../application-framework/arkui/arkts-api/ui/arkui/graphics/document.md#matrix4)

 | 

Returns a **Matrix4** object.

A **Matrix4** object is an array that contains 16 floating-point numbers, which is used to represent the column-major rotation transformation matrix in OpenGL.

 |

**Error codes**:

For details about the error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [AR Engine Error Codes](../../ar-engine-error-codes/document.md).

| 
**Error Code**

 | 

**Error Message**

 |
| :-- | :-- |
| 

401

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |
| 

1009200001

 | 

Failure.

 |

**Example**:

import { Matrix4 } from '@kit.ArkUI';
import { arEngine } from '@kit.AREngine';

// Refer to the sample code of the ARSession.getFrame API for details about arSession creation.
let frame: arEngine.ARFrame = arSession.getFrame();
let camera: arEngine.ARCamera = frame.getCamera();
let matrix: Matrix4 = camera.getProjectionMatrix(0, 1);

#### \[h2\]ARCamera.getImageIntrinsics

getImageIntrinsics(): ARCameraIntrinsics

Obtains the intrinsic parameter object of an offline camera.

This object can be used to obtain the intrinsic parameters such as the focal length, image dimensions, principal point, and distortion parameters of the camera.

**System capability**: SystemCapability.AREngine.Core

**Start version**: 5.1.0(18)

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[ARCameraIntrinsics](#section1472734105519)

 | 

Returns an intrinsic parameter object of the camera.

 |

**Error codes**:

For details about the error codes, please refer to [AR Engine Error Codes](../../ar-engine-error-codes/document.md).

| 
**Error Code**

 | 

**Error Message**

 |
| :-- | :-- |
| 

1009200001

 | 

Failure.

 |

**Example**:

import { arEngine } from '@kit.AREngine';

// Refer to the sample code of the ARSession.getFrame API for details about arSession creation.
let frame: arEngine.ARFrame = arSession.getFrame();
let camera: arEngine.ARCamera = frame.getCamera();
let imageIntrinsics: arEngine.ARCameraIntrinsics = camera.getImageIntrinsics();

#### ARFrame

A frame of data processed by AR Engine.

**System capability**: SystemCapability.AREngine.Core

**Start version**: 5.1.0(18)

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

timestamp

 | 

number

 | 

Yes

 | 

No

 | 

Timestamp of the current frame.

The unit is ns.

 |
| 

pointCloud

 | 

[ARPointCloud](#section1941316821)

 | 

Yes

 | 

No

 | 

Set of trackable 3D point clouds in the current frame.

 |

#### \[h2\]ARFrame.getCamera

getCamera(): ARCamera

Obtains the camera object of the current frame.

**System capability**: SystemCapability.AREngine.Core

**Start version**: 5.1.0(18)

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[ARCamera](#section176984261612)

 | 

Camera object of the current frame.

 |

**Error codes**:

For details about the error codes, please refer to [AR Engine Error Codes](../../ar-engine-error-codes/document.md).

| 
**Error Code**

 | 

**Error Message**

 |
| :-- | :-- |
| 

1009200001

 | 

Failure.

 |

**Example**:

import { arEngine } from '@kit.AREngine';

// Refer to the sample code of the ARSession.getFrame API for details about arSession creation.
let frame: arEngine.ARFrame = arSession.getFrame();
let camera: arEngine.ARCamera = frame.getCamera();

#### \[h2\]ARFrame.getUpdatedTrackables

getUpdatedTrackables(type: ARTrackableType): Array<ARTrackable>

Obtains the updated trackable object of a specified type.

**System capability**: SystemCapability.AREngine.Core

**Start version**: 5.1.0(18)

**Parameters**:

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

[ARTrackableType](#section1725585684613)

 | 

Yes

 | 

Type of the trackable object.

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

Array<[ARTrackable](#section1710323720204)\>

 | 

Array of trackable objects.

 |

**Error codes**:

For details about the error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [AR Engine Error Codes](../../ar-engine-error-codes/document.md).

| 
**Error Code**

 | 

**Error Message**

 |
| :-- | :-- |
| 

401

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |
| 

1009200001

 | 

Failure.

 |

**Example**:

import { arEngine } from '@kit.AREngine';

// Refer to the sample code of the ARSession.getFrame API for details about arSession creation.
let frame: arEngine.ARFrame = arSession.getFrame();
let trackables: arEngine.ARTrackable\[\] = frame.getUpdatedTrackables(arEngine.ARTrackableType.BASE);

#### \[h2\]ARFrame.hitTest

hitTest(x: number, y: number): Array<ARHitResult>

Obtains the pixel coordinates (**pixelX** and **pixelY**) in the preview area based on the light projected by the camera to determine the ray direction, and then checks whether the ray has an intersection on the plane, mesh, or point cloud.

**System capability**: SystemCapability.AREngine.Core

**Start version**: 5.1.0(18)

**Parameters**:

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

x

 | 

number

 | 

Yes

 | 

X coordinate of a pixel in the preview area.

The value is determined by the display resolution of the device.

 |
| 

y

 | 

number

 | 

Yes

 | 

Y coordinate of a pixel in the preview area.

The value is determined by the display resolution of the device.

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

Array<[ARHitResult](#section14725141314593)\>

 | 

Array of hit detection result objects.

 |

**Error codes**:

For details about the error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [AR Engine Error Codes](../../ar-engine-error-codes/document.md).

| 
**Error Code**

 | 

**Error Message**

 |
| :-- | :-- |
| 

401

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |
| 

1009200001

 | 

Failure.

 |
| 

1009200008

 | 

Resource exhausted.

 |

**Example**:

import { arEngine } from '@kit.AREngine';

// Refer to the sample code of the ARSession.getFrame API for details about arSession creation.
let frame: arEngine.ARFrame = arSession.getFrame();
let hitResult: arEngine.ARHitResult\[\] = frame.hitTest(0, 0);

#### \[h2\]ARFrame.acquireSceneMesh

acquireSceneMesh(): ARSceneMesh

Obtains the scene mesh data of the current frame.

**System capability**: SystemCapability.AREngine.Core

**Start version**: 5.1.0(18)

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[ARSceneMesh](#section81184417712)

 | 

Set of environmental mesh data.

 |

**Error codes**:

For details about the error codes, please refer to [AR Engine Error Codes](../../ar-engine-error-codes/document.md).

| 
**Error Code**

 | 

**Error Message**

 |
| :-- | :-- |
| 

1009200001

 | 

Failure.

 |
| 

1009200008

 | 

Resource exhausted.

 |

**Example**:

import { arEngine } from '@kit.AREngine';

// Refer to the sample code of the ARSession.getFrame API for details about arSession creation.
let frame: arEngine.ARFrame = arSession.getFrame();
let sceneMesh: arEngine.ARSceneMesh = frame.acquireSceneMesh();

#### \[h2\]ARFrame.acquireDepthImage16Bits

acquireDepthImage16Bits(): ARImage

Obtains the depth image object corresponding to the current frame.

The depth image is a single 16-bit plane at index 0. Each pixel contains the distance to the camera plane, in mm. The depth range is from 0 mm to 65,535 mm, that is, about 65 m.

**System capability**: SystemCapability.AREngine.Core

**Start version**: 5.1.0(18)

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[ARImage](#section3211104815419)

 | 

Returns the camera video stream frame object.

 |

**Error codes**:

For details about the error codes, please refer to [AR Engine Error Codes](../../ar-engine-error-codes/document.md).

| 
**Error Code**

 | 

**Error Message**

 |
| :-- | :-- |
| 

1009200001

 | 

Failure.

 |

**Example**:

import { arEngine } from '@kit.AREngine';

// Refer to the sample code of the ARSession.getFrame API for details about arSession creation.
let frame: arEngine.ARFrame = arSession.getFrame();
let arImage: arEngine.ARImage = frame.acquireDepthImage16Bits();

#### \[h2\]ARFrame.acquireDepthConfidenceImage

acquireDepthConfidenceImage(): ARImage

Obtains the depth confidence map of the current frame.

The confidence value can be 0, 1, or 2. **0** indicates the lowest confidence of the estimated depth value, **1** indicates medium confidence of the estimated depth value, and **2** indicates the highest confidence of the estimated depth value. The width and height of the depth confidence map are the same as those of the depth map.

**System capability**: SystemCapability.AREngine.Core

**Start version**: 5.1.0(18)

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[ARImage](#section3211104815419)

 | 

Returns the camera video stream frame object.

 |

**Error codes**:

For details about the error codes, please refer to [AR Engine Error Codes](../../ar-engine-error-codes/document.md).

| 
**Error Code**

 | 

**Error Message**

 |
| :-- | :-- |
| 

1009200001

 | 

Failure.

 |

**Example**:

import { arEngine } from '@kit.AREngine';

// Refer to the sample code of the ARSession.getFrame API for details about arSession creation.
let frame: arEngine.ARFrame = arSession.getFrame();
let depthConfidenceImage: arEngine.ARImage = frame.acquireDepthConfidenceImage();

#### \[h2\]ARFrame.acquireSemanticDense

acquireSemanticDense(): ARSemanticDenseData

Obtains the high-precision geometric reconstruction object data.

**System capability**: SystemCapability.AREngine.Core

**Start version**: 6.0.0(20)

**Returns**:

| 
**Type**

 | 

Description

 |
| :-- | :-- |
| 

[ARSemanticDenseData](#section137161158185414)

 | 

High-precision geometric reconstruction object data of the current frame.

 |

**Error codes**:

For details about the error codes, please refer to [AR Engine Error Codes](../../ar-engine-error-codes/document.md).

| 
**Error Code**

 | 

**Error Message**

 |
| :-- | :-- |
| 

1009200001

 | 

Failure.

 |

**Example**:

import { arEngine } from '@kit.AREngine';

// Refer to the sample code of the ARSession.getFrame API for details about arSession creation.
let frame: arEngine.ARFrame = arSession.getFrame();
let semanticData: arEngine.ARSemanticDenseData = frame.acquireSemanticDense();

#### \[h2\]ARFrame.release

release(): Promise<void>

Releases the memory occupied by the [ARFrame](#section83421523123819) object.

This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.AREngine.Core

**Start version**: 5.1.0(18)

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

Promise<void>

 | 

Promise object that returns no value.

 |

**Error codes**:

For details about the error codes, please refer to [AR Engine Error Codes](../../ar-engine-error-codes/document.md).

| 
**Error Code**

 | 

**Error Message**

 |
| :-- | :-- |
| 

1009200001

 | 

Failure.

 |

**Example**:

import { arEngine } from '@kit.AREngine';

async function release(): Promise<void> {
  // Refer to the sample code of the ARSession.getFrame API for details about arSession creation.
  let frame: arEngine.ARFrame = arSession.getFrame();
  await frame.release();
}

#### ARHitResult

Hit testing result object, which describes the hit testing result of a single trackable object.

**System capability**: SystemCapability.AREngine.Core

**Start version**: 5.1.0(18)

**Parameters**:

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

distance

 | 

number

 | 

Yes

 | 

No

 | 

Distance from the camera to the hit position, in meters. The value ranges from 0 to 65535.

 |

#### \[h2\]ARHitResult.getHitPose

getHitPose(): ARPose

Obtains the pose of an intersection.

For details about the pose information, please refer to [Coordinate System](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arengine-coordinate).

If [ARPointOrientationMode](#section188141239153515) is **ESTIMATED\_SURFACE\_NORMAL**, X+ is the vertical vector of the ray, that is, the parallel vector of the plane, Y+ is the normal vector of the plane, and Z+ is the parallel vector of the plane, roughly pointing to the camera.

If [ARPointOrientationMode](#section188141239153515) is **INITIALIZED\_TO\_IDENTITY**, the rotation of the coordinates does not change with the angle of the plane. X+ is the vertical vector of the ray, pointing to the right (from the perspective of the device). Y+ points upwards, and Z+ roughly points to the camera.

**System capability**: SystemCapability.AREngine.Core

**Start version**: 5.1.0(18)

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[ARPose](#section19274193834913)

 | 

Pose object.

 |

**Error codes**:

For details about the error codes, please refer to [AR Engine Error Codes](../../ar-engine-error-codes/document.md).

| 
**Error Code**

 | 

**Error Message**

 |
| :-- | :-- |
| 

1009200001

 | 

Failure.

 |

**Example**:

import { arEngine } from '@kit.AREngine';

// Refer to the sample code of the ARSession.getFrame API for details about arSession creation.
let frame: arEngine.ARFrame = arSession.getFrame();
let hitResult: Array<arEngine.ARHitResult> = frame.hitTest(0, 0);
let hitPose: arEngine.ARPose = hitResult\[0\].getHitPose();

#### \[h2\]ARHitResult.getTrackable

getTrackable(): ARTrackable

Obtains the trackable object that is hit.

**System capability**: SystemCapability.AREngine.Core

**Start version**: 5.1.0(18)

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[ARTrackable](#section1710323720204)

 | 

Returns the object that can be tracked.

 |

**Error codes**:

For details about the error codes, please refer to [AR Engine Error Codes](../../ar-engine-error-codes/document.md).

| 
**Error Code**

 | 

**Error Message**

 |
| :-- | :-- |
| 

1009200001

 | 

Failure.

 |

**Example**:

import { arEngine } from '@kit.AREngine';

// Refer to the sample code of the ARSession.getFrame API for details about arSession creation.
let frame: arEngine.ARFrame = arSession.getFrame();
let hitResult: Array<arEngine.ARHitResult> = frame.hitTest(0, 0);
let trackable: arEngine.ARTrackable = hitResult\[0\].getTrackable();

#### \[h2\]ARHitResult.createAnchor

createAnchor(): ARAnchor

Creates an anchor at the intersection.

**System capability**: SystemCapability.AREngine.Core

**Start version**: 5.1.0(18)

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[ARAnchor](#section106411242143016)

 | 

Anchor object.

 |

**Error codes**:

For details about the error codes, please refer to [AR Engine Error Codes](../../ar-engine-error-codes/document.md).

| 
**Error Code**

 | 

**Error Message**

 |
| :-- | :-- |
| 

1009200001

 | 

Failure.

 |

**Example**:

import { arEngine } from '@kit.AREngine';

// Refer to the sample code of the ARSession.getFrame API for details about arSession creation.
let frame: arEngine.ARFrame = arSession.getFrame();
let hitResult: Array<arEngine.ARHitResult> = frame.hitTest(0, 0);
let anchor: arEngine.ARAnchor = hitResult\[0\].createAnchor();

#### \[h2\]ARHitResult.release

release(): Promise<void>

Releases the memory occupied by the [ARHitResult](#section14725141314593) object.

This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.AREngine.Core

**Start version**: 5.1.0(18)

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

Promise<void>

 | 

Promise object that returns no value.

 |

**Error codes**:

For details about the error codes, please refer to [AR Engine Error Codes](../../ar-engine-error-codes/document.md).

| 
**Error Code**

 | 

**Error Message**

 |
| :-- | :-- |
| 

1009200001

 | 

Failure.

 |

**Example**:

import { arEngine } from '@kit.AREngine';

// Refer to the sample code of the ARSession.getFrame API for details about arSession creation.
let frame: arEngine.ARFrame = arSession.getFrame();
let hitResult: Array<arEngine.ARHitResult> = frame.hitTest(0, 0);
await hitResult\[0\].release();

#### ARImage

Defines the camera video stream frame object.

**System capability**: SystemCapability.AREngine.Core

**Start version**: 5.1.0(18)

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

format

 | 

[ARImageFormat](#section183476224713)

 | 

Yes

 | 

No

 | 

Image format.

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

Image width of the current frame, in pixels. The numeric value range is related to the camera pixel of the device.

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

Image height of the current frame, in pixels. The numeric value range is related to the camera pixel of the device.

 |
| 

imageTimestamp

 | 

number

 | 

Yes

 | 

No

 | 

Image timestamp, in nanoseconds.

 |
| 

planes

 | 

Array<[ImageComponent](#section175993235012)\>

 | 

Yes

 | 

No

 | 

Basic structure parameters of an image component.

 |

#### \[h2\]ARImage.release

release(): Promise<void>

Releases the memory occupied by the [ARImage](#section3211104815419) camera video stream frame object.

This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.AREngine.Core

**Start version**: 5.1.0(18)

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

Promise<void>

 | 

Promise object that returns no value.

 |

**Error codes**:

For details about the error codes, please refer to [AR Engine Error Codes](../../ar-engine-error-codes/document.md).

| 
**Error Code**

 | 

**Error Message**

 |
| :-- | :-- |
| 

1009200001

 | 

Failure.

 |

**Example**:

import { arEngine } from '@kit.AREngine';

async function release(): Promise<void> {
  // Refer to the sample code of the ARSession.getFrame API for details about arSession creation.
  let frame: arEngine.ARFrame = arSession.getFrame();
  let image: arEngine.ARImage = frame.acquireDepthImage16Bits();
  await image.release();
}

#### ARPlane

Defines a plane object, which describes the detected trackable plane information.

This class is inherited from the [ARTrackable](#section1710323720204) class.

**System capability**: SystemCapability.AREngine.Core

**Start version**: 5.1.0(18)

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

planeType

 | 

[ARPlaneType](#section766818120479)

 | 

No

 | 

No

 | 

Plane type.

 |
| 

extendX

 | 

number

 | 

No

 | 

No

 | 

Length of the boundary rectangle along the X axis of the plane local coordinate system, in meters. The numeric value range is not limited.

 |
| 

extendZ

 | 

number

 | 

No

 | 

No

 | 

Length of the boundary rectangle along the Z axis of the plane local coordinate system, in meters. The numeric value range is not limited.

 |
| 

label

 | 

[ARSemanticPlaneLabel](#section5137195514137)

 | 

No

 | 

No

 | 

Semantic type of the current plane.

 |

#### \[h2\]ARPlane.getPolygonXZ

getPolygonXZ(): ArrayBuffer

Obtains the 2D vertex array of the detected plane.

**System capability**: SystemCapability.AREngine.Core

**Start version**: 5.1.0(18)

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

ArrayBuffer

 | 

Returns an **ArrayBuffer** buffer object that contains the vertex coordinate array. Coordinates of the X-Z plane in the local coordinate system.

NOTE:

If this type needs to be converted to the float32 type, refer to [Data Type Conversion](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arengine-arraybuffer-info) to perform the conversion.

 |

**Error codes**:

For details about the error codes, please refer to [AR Engine Error Codes](../../ar-engine-error-codes/document.md).

| 
**Error Code**

 | 

**Error Message**

 |
| :-- | :-- |
| 

1009200001

 | 

Failure.

 |

**Example**:

import { arEngine } from '@kit.AREngine';

// Refer to the sample code of the ARSession.getFrame API for details about arSession creation.
let trackables: Array<arEngine.ARTrackable> = arSession.getAllTrackables(arEngine.ARTrackableType.PLANE);
let plane = trackables\[0\] as arEngine.ARPlane;
let buffer: ArrayBuffer = plane.getPolygonXZ();

#### \[h2\]ARPlane.getSubsumedBy

getSubsumedBy(): ARPlane

Obtains the parent plane of a plane (a parent plane is generated when a plane is merged with another one).

**System capability**: SystemCapability.AREngine.Core

**Start version**: 5.1.0(18)

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[ARPlane](#section3392194311417)

 | 

Returns a plane object, which indicates the parent plane. If no parent plane is available, **undefined** is returned.

 |

**Error codes**:

For details about the error codes, please refer to [AR Engine Error Codes](../../ar-engine-error-codes/document.md).

| 
**Error Code**

 | 

**Error Message**

 |
| :-- | :-- |
| 

1009200001

 | 

Failure.

 |

**Example**:

import { arEngine } from '@kit.AREngine';

// Refer to the sample code of the ARSession.getFrame API for details about arSession creation.
let trackables: Array<arEngine.ARTrackable> = arSession.getAllTrackables(arEngine.ARTrackableType.PLANE);
let plane = trackables\[0\] as arEngine.ARPlane;
let subsumedPlane: arEngine.ARPlane = plane.getSubsumedBy();

#### \[h2\]ARPlane.isPoseInExtents

isPoseInExtents(pose: ARPose): boolean

Checks whether a given pose is within the boundary rectangle of the plane.

**System capability**: SystemCapability.AREngine.Core

**Start version**: 5.1.0(18)

**Parameters**:

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

pose

 | 

[ARPose](#section19274193834913)

 | 

Yes

 | 

Pose object.

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

boolean

 | 

If **true** is returned, the pose is in the boundary rectangle of the plane. If **false** is returned, the pose is not in the boundary rectangle of the plane.

 |

**Error codes**:

For details about the error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [AR Engine Error Codes](../../ar-engine-error-codes/document.md).

| 
**Error Code**

 | 

**Error Message**

 |
| :-- | :-- |
| 

401

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |
| 

1009200001

 | 

Failure.

 |

**Example**:

import { arEngine } from '@kit.AREngine';

// Refer to the sample code of the ARSession.getFrame API for details about arSession creation.
let trackables: Array<arEngine.ARTrackable> = arSession.getAllTrackables(arEngine.ARTrackableType.PLANE);
let pose: arEngine.ARPose = trackables\[0\].getPose();
let plane = trackables\[0\] as arEngine.ARPlane;
let result: boolean = plane.isPoseInExtents(pose);

#### \[h2\]ARPlane.isPoseInPolygon

isPoseInPolygon(pose: ARPose): boolean

Checks whether a given pose is within the boundary polygon of the plane.

**System capability**: SystemCapability.AREngine.Core

**Start version**: 5.1.0(18)

**Parameters**:

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

pose

 | 

[ARPose](#section19274193834913)

 | 

Yes

 | 

Pose object.

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

boolean

 | 

If **true** is returned, the pose is in the boundary polygon of the plane. If **false** is returned, the pose is not in the boundary polygon of the plane.

 |

**Error codes**:

For details about the error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [AR Engine Error Codes](../../ar-engine-error-codes/document.md).

| 
**Error Code**

 | 

**Error Message**

 |
| :-- | :-- |
| 

401

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |
| 

1009200001

 | 

Failure.

 |

**Example**:

import { arEngine } from '@kit.AREngine';

// Refer to the sample code of the ARSession.getFrame API for details about arSession creation.
let trackables: Array<arEngine.ARTrackable> = arSession.getAllTrackables(arEngine.ARTrackableType.PLANE);
let pose: arEngine.ARPose = trackables\[0\].getPose();
let plane = trackables\[0\] as arEngine.ARPlane;
let result: boolean = plane.isPoseInPolygon(pose);

#### ARPlaneAnchor

Anchor object of the plane type.

This class is inherited from the [ARAnchor](#section106411242143016) class.

**System capability**: SystemCapability.AREngine.Core

**Start version**: 5.1.0(18)

#### \[h2\]ARPlaneAnchor.getPlane

getPlane(): ARPlane

Obtains the plane.

**System capability**: SystemCapability.AREngine.Core

**Start version**: 5.1.0(18)

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[ARPlane](#section3392194311417)

 | 

Plane object, which describes the detected trackable plane information.

 |

**Error codes**:

For details about the error codes, please refer to [AR Engine Error Codes](../../ar-engine-error-codes/document.md).

| 
**Error Code**

 | 

**Error Message**

 |
| :-- | :-- |
| 

1009200001

 | 

Failure.

 |

**Example**:

import { arEngine, ARView, arViewController } from '@kit.AREngine';
import { Node } from '@kit.ArkGraphics3D'; 
// This method is used in ARViewCallback.
onAnchorAdd(ctx: arViewController.ARViewContext, node: Node, anchor: arEngine.ARAnchor): void {
  let planeAnchor: arEngine.ARPlaneAnchor = anchor as arEngine.ARPlaneAnchor;
  let plane: arEngine.ARPlane = planeAnchor.getPlane();
  plane.release();
}

#### ARPoint

3D point cloud object that can be tracked.

This class is inherited from the [ARTrackable](#section1710323720204) class.

**System capability**: SystemCapability.AREngine.Core

**Start version**: 5.1.0(18)

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

orientationMode

 | 

[ARPointOrientationMode](#section188141239153515)

 | 

Yes

 | 

No

 | 

Orientation mode.

 |

#### ARPose

Pose object.

Represents an immutable rigid transformation from one coordinate system to another, such as translation or rotation.

**System capability**: SystemCapability.AREngine.Core

**Start version**: 5.1.0(18)

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

rotation

 | 

[Quaternion](../../../arkgraphics-3d/arkts-apis/graphics3d/scenetype/document.md#quaternion)

 | 

Yes

 | 

No

 | 

Posture data from the pose object, including the rotation component.

 |
| 

translation

 | 

[Vec3](../../../arkgraphics-3d/arkts-apis/graphics3d/scenetype/document.md#vec3)

 | 

Yes

 | 

No

 | 

Posture data from the pose object, including the translation component.

 |

#### \[h2\]ARPose.getMatrix

getMatrix(): Matrix4

Converts the pose data into a 4 × 4 matrix.

**System capability**: SystemCapability.AREngine.Core

**Start version**: 5.1.0(18)

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[Matrix4](../../../../application-framework/arkui/arkts-api/ui/arkui/graphics/document.md#matrix4)

 | 

Array of 16 floating-point numbers stored in column-major order.

 |

**Error codes**:

For details about the error codes, please refer to [AR Engine Error Codes](../../ar-engine-error-codes/document.md).

| 
**Error Code**

 | 

**Error Message**

 |
| :-- | :-- |
| 

1009200001

 | 

Failure.

 |

**Example**:

import { Matrix4 } from '@kit.ArkUI';
import { arEngine } from '@kit.AREngine';

// Refer to the sample code of the ARSession.getFrame API for details about arSession creation.
let frame: arEngine.ARFrame = arSession.getFrame();
let camera: arEngine.ARCamera = frame.getCamera();
let pose: arEngine.ARPose = camera.getPose();
let matrix: Matrix4 = pose.getMatrix();

#### \[h2\]ARPose.release

release(): Promise<void>

Releases the memory occupied by the [ARPose](#section19274193834913) object.

This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.AREngine.Core

**Start version**: 5.1.0(18)

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

Promise<void>

 | 

Promise object that returns no value.

 |

**Error codes**:

For details about the error codes, please refer to [AR Engine Error Codes](../../ar-engine-error-codes/document.md).

| 
**Error Code**

 | 

**Error Message**

 |
| :-- | :-- |
| 

1009200001

 | 

Failure.

 |

**Example**:

import { arEngine } from '@kit.AREngine';

async function release(): Promise<void> {
  // Refer to the sample code of the ARSession.getFrame API for details about arSession creation.
  let frame: arEngine.ARFrame = arSession.getFrame();
  let camera: arEngine.ARCamera = frame.getCamera();
  let pose: arEngine.ARPose = camera.getPose();
  await pose.release();
}

#### ARSceneMesh

Defines a set of the environment mesh data.

**System capability**: SystemCapability.AREngine.Core

**Start version**: 5.1.0(18)

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

verticesSize

 | 

number

 | 

Yes

 | 

No

 | 

Number of vertices in a scene mesh.

The minimum value is 0, and there is no upper limit.

 |
| 

triangleIndicesSize

 | 

number

 | 

Yes

 | 

No

 | 

Number of triangle indexes in a scene mesh. The minimum value is 0, and there is no upper limit.

 |

#### \[h2\]ARSceneMesh.getVertices

getVertices(): ArrayBuffer

Obtains vertex coordinate data in a scene mesh.

**System capability**: SystemCapability.AREngine.Core

**Start version**: 5.1.0(18)

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

ArrayBuffer

 | 

**ArrayBuffer** buffer object. This buffer contains the coordinates of vertices on the X-Z plane in the local coordinate system.

NOTE:

If this type needs to be converted to the float32 type, refer to [Data Type Conversion](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arengine-arraybuffer-info) to perform the conversion.

 |

**Error codes**:

For details about the error codes, please refer to [AR Engine Error Codes](../../ar-engine-error-codes/document.md).

| 
**Error Code**

 | 

**Error Message**

 |
| :-- | :-- |
| 

1009200001

 | 

Failure.

 |

**Example**:

import { arEngine } from '@kit.AREngine';

// Refer to the sample code of the ARSession.getFrame API for details about arSession creation.
let frame: arEngine.ARFrame = arSession.getFrame();
let sceneMesh: arEngine.ARSceneMesh = frame.acquireSceneMesh();
let buffer: ArrayBuffer = sceneMesh.getVertices();

#### \[h2\]ARSceneMesh.getVertexNormals

**getVertexNormals** (): **ArrayBuffer**

Obtains the vertex normal coordinate data in a scene mesh.

**System capability**: SystemCapability.AREngine.Core

**Start version**: 5.1.0(18)

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

ArrayBuffer

 | 

**ArrayBuffer** buffer object. This buffer contains the coordinates of vertices on the X-Z plane in the local coordinate system.

NOTE:

If this type needs to be converted to the float32 type, refer to [Data Type Conversion](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arengine-arraybuffer-info) to perform the conversion.

 |

**Error codes**:

For details about the error codes, please refer to [AR Engine Error Codes](../../ar-engine-error-codes/document.md).

| 
**Error Code**

 | 

**Error Message**

 |
| :-- | :-- |
| 

1009200001

 | 

Failure.

 |

**Example**:

import { arEngine } from '@kit.AREngine';

// Refer to the sample code of the ARSession.getFrame API for details about arSession creation.
let frame: arEngine.ARFrame = arSession.getFrame();
let sceneMesh: arEngine.ARSceneMesh = frame.acquireSceneMesh();
let buffer: ArrayBuffer = sceneMesh.getVertexNormals();

#### \[h2\]ARSceneMesh.getTriangleIndices

getTriangleIndices(): ArrayBuffer

Obtains the triangle index data in a scene mesh.

**System capability**: SystemCapability.AREngine.Core

**Start version**: 5.1.0(18)

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

ArrayBuffer

 | 

**ArrayBuffer** buffer object. This buffer contains the coordinates of vertices on the X-Z plane in the local coordinate system.

NOTE:

If this type needs to be converted to the int32 type, refer to [Data Type Conversion](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arengine-arraybuffer-info) to perform the conversion.

 |

**Error codes**:

For details about the error codes, please refer to [AR Engine Error Codes](../../ar-engine-error-codes/document.md).

| 
**Error Code**

 | 

**Error Message**

 |
| :-- | :-- |
| 

1009200001

 | 

Failure.

 |

**Example**:

import { arEngine } from '@kit.AREngine';

// Refer to the sample code of the **ARSession.getFrame** API for details about **arSession** creation.
let frame: arEngine.ARFrame = arSession.getFrame();
let sceneMesh: arEngine.ARSceneMesh = frame.acquireSceneMesh();
let buffer: ArrayBuffer = sceneMesh.getTriangleIndices();

#### \[h2\]ARSceneMesh.release

release(): Promise<void>

Releases the memory occupied by the [ARSceneMesh](#section81184417712) environment mesh data object.

This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.AREngine.Core

**Start version**: 5.1.0(18)

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

Promise<void>

 | 

Promise object that returns no value.

 |

**Error codes**:

For details about the error codes, please refer to [AR Engine Error Codes](../../ar-engine-error-codes/document.md).

| 
**Error Code**

 | 

**Error Message**

 |
| :-- | :-- |
| 

1009200001

 | 

Failure.

 |

**Example**:

import { arEngine } from '@kit.AREngine';

async function release(): Promise<void> {
  // Refer to the sample code of the ARSession.getFrame API for details about arSession creation.
  let frame: arEngine.ARFrame = arSession.getFrame();
  let sceneMesh: arEngine.ARSceneMesh = frame.acquireSceneMesh();
  await sceneMesh.release();
}

#### ARSemanticDenseData

Defines the high-precision geometric reconstruction object data set.

**System capability**: SystemCapability.AREngine.Core

**Start version**: 6.0.0(20)

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

timestamp

 | 

number

 | 

Yes

 | 

No

 | 

Timestamp of the high-precision geometric reconstruction object data, in nanoseconds.

 |
| 

pointDataSize

 | 

number

 | 

Yes

 | 

No

 | 

Dense point cloud size in the high-precision geometric reconstruction object data. The minimum value is **0**, and the maximum value is **10000**.

 |
| 

cubeDataSize

 | 

number

 | 

Yes

 | 

No

 | 

Cube count in the high-precision geometric reconstruction object data. The minimum value is **0**, and the maximum value is **1**.

 |

#### \[h2\]ARSemanticDenseData.acquirePointData

acquirePointData(): ARSemanticDensePointData

Dense point cloud data in the high-precision geometric reconstruction object data.

**System capability**: SystemCapability.AREngine.Core

**Start version**: 6.0.0(20)

**Returns**:

| 
**Type**

 | 

Description

 |
| :-- | :-- |
| 

[ARSemanticDensePointData](#section1031071863714)

 | 

Dense point cloud data in all high-precision geometric reconstruction object data.

 |

**Error codes**:

For details about the error codes, please refer to [AR Engine Error Codes](../../ar-engine-error-codes/document.md).

| 
**Error Code**

 | 

**Error Message**

 |
| :-- | :-- |
| 

1009200001

 | 

Failure.

 |

**Example**:

import { arEngine } from '@kit.AREngine';

// Refer to the sample code of the ARSession.getFrame API for details about arSession creation.
let frame: arEngine.ARFrame = arSession.getFrame();
let semanticData: arEngine.ARSemanticDenseData = frame.acquireSemanticDense();
let semanticPointData: arEngine.ARSemanticDensePointData = semanticData.acquirePointData();

#### \[h2\]ARSemanticDenseData.acquireCubeData

acquireCubeData(): Array<ARSemanticDenseCubeData>

Cube data in the high-precision geometric reconstruction object data.

**System capability**: SystemCapability.AREngine.Core

**Start version**: 6.0.0(20)

**Returns**:

| 
**Type**

 | 

Description

 |
| :-- | :-- |
| 

Array<[ARSemanticDenseCubeData](#section1516742919422)\>

 | 

List of cube data in the high-precision geometric reconstruction object data.

 |

**Error codes**:

For details about the error codes, please refer to [AR Engine Error Codes](../../ar-engine-error-codes/document.md).

| 
**Error Code**

 | 

**Error Message**

 |
| :-- | :-- |
| 

1009200001

 | 

Failure.

 |

**Example**:

import { arEngine } from '@kit.AREngine';

// Refer to the sample code of the ARSession.getFrame API for details about arSession creation.
let frame: arEngine.ARFrame = arSession.getFrame();
let semanticData: arEngine.ARSemanticDenseData = frame.acquireSemanticDense();
let semanticCubeData: arEngine.ARSemanticDenseCubeData = semanticData.acquireCubeData()\[0\];

#### \[h2\]ARSemanticDenseData.release

release(): Promise<void>

Releases the memory occupied by the high-precision geometric reconstruction object data [ARSemanticDenseData](#section137161158185414).

This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.AREngine.Core

**Start version**: 6.0.0(20)

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

Promise<void>

 | 

Promise object that returns no value.

 |

**Error codes**:

For details about the error codes, please refer to [AR Engine Error Codes](../../ar-engine-error-codes/document.md).

| 
**Error Code**

 | 

**Error Message**

 |
| :-- | :-- |
| 

1009200001

 | 

Failure.

 |

**Example**:

import { arEngine } from '@kit.AREngine';

// Refer to the sample code of the ARSession.getFrame API for details about arSession creation.
let frame: arEngine.ARFrame = arSession.getFrame();
let semanticData: arEngine.ARSemanticDenseData = frame.acquireSemanticDense();
await semanticData.release();

#### ARTrackable

Defines a trackable object.

**System capability**: SystemCapability.AREngine.Core

**Start version**: 5.1.0(18)

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

type

 | 

[ARTrackableType](#section1725585684613)

 | 

Yes

 | 

No

 | 

Type of the trackable object.

 |
| 

state

 | 

[ARTrackingState](#section16656547114620)

 | 

Yes

 | 

No

 | 

Tracking state of the trackable object.

 |

#### \[h2\]ARTrackable.getPose

getPose(): ARPose

Obtains the pose information of a trackable object.

**System capability**: SystemCapability.AREngine.Core

**Start version**: 5.1.0(18)

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[ARPose](#section19274193834913)

 | 

Pose information of the trackable object.

 |

**Error codes**:

For details about the error codes, please refer to [AR Engine Error Codes](../../ar-engine-error-codes/document.md).

| 
**Error Code**

 | 

**Error Message**

 |
| :-- | :-- |
| 

1009200001

 | 

Failure.

 |

**Example**:

import { arEngine } from '@kit.AREngine';

// Refer to the sample code of the ARSession.getFrame API for details about arSession creation.
let trackables: Array<arEngine.ARTrackable> = arSession.getAllTrackables(arEngine.ARTrackableType.BASE);
let trackablePose: arEngine.ARPose = trackables\[0\].getPose();

#### \[h2\]ARTrackable.getAnchors

getAnchors(): Array<ARAnchor>

Obtains anchor information of a trackable object.

**System capability**: SystemCapability.AREngine.Core

**Start version**: 5.1.0(18)

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

Array<[ARAnchor](#section106411242143016)\>

 | 

Array of anchor objects.

 |

**Error codes**:

For details about the error codes, please refer to [AR Engine Error Codes](../../ar-engine-error-codes/document.md).

| 
**Error Code**

 | 

**Error Message**

 |
| :-- | :-- |
| 

1009200001

 | 

Failure.

 |

**Example**:

import { arEngine } from '@kit.AREngine';

// Refer to the sample code of the ARSession.getFrame API for details about arSession creation.
let trackables: Array<arEngine.ARTrackable> = arSession.getAllTrackables(arEngine.ARTrackableType.BASE);
let anchors: Array<arEngine.ARAnchor> = trackables\[0\].getAnchors();

#### \[h2\]ARTrackable.createAnchor

createAnchor(pose: ARPose): ARAnchor

Creates an anchor object using the pose information of the trackable object. The anchor is bound to the current trackable object.

**System capability**: SystemCapability.AREngine.Core

**Start version**: 5.1.0(18)

**Parameters**:

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

pose

 | 

[ARPose](#section19274193834913)

 | 

Yes

 | 

Pose object.

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[ARAnchor](#section106411242143016)

 | 

Anchor object.

 |

**Error codes**:

For details about the error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [AR Engine Error Codes](../../ar-engine-error-codes/document.md).

| 
**Error Code**

 | 

**Error Message**

 |
| :-- | :-- |
| 

401

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |
| 

1009200001

 | 

Failure.

 |

**Example**:

import { arEngine } from '@kit.AREngine';

// Refer to the sample code of the ARSession.getFrame API for details about arSession creation.
let trackables: Array<arEngine.ARTrackable> = arSession.getAllTrackables(arEngine.ARTrackableType.BASE);
let pose: arEngine.ARPose = trackables\[0\].getPose();
let anchor: arEngine.ARAnchor = trackables\[0\].createAnchor(pose);

#### \[h2\]ARTrackable.release

release(): Promise<void>

Releases the memory occupied by the tracked object [ARTrackable](#section1710323720204).

This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.AREngine.Core

**Start version**: 5.1.0(18)

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

Promise<void>

 | 

Promise object that returns no value.

 |

**Error codes**:

For details about the error codes, please refer to [AR Engine Error Codes](../../ar-engine-error-codes/document.md).

| 
**Error Code**

 | 

**Error Message**

 |
| :-- | :-- |
| 

1009200001

 | 

Failure.

 |

**Example**:

import { arEngine } from '@kit.AREngine';

// Refer to the sample code of the ARSession.getFrame API for details about arSession creation.
let trackables: Array<arEngine.ARTrackable> = arSession.getAllTrackables(arEngine.ARTrackableType.BASE);
await trackables\[0\].release();

#### arEngine.createARAugmentedImageDatabase

createARAugmentedImageDatabase(): Promise<ARAugmentedImageDatabase>

Creates an augmented image database.

This API returns the [ARAugmentedImageDatabase](#section1410345414514) object asynchronously through a promise.

**System capability**: SystemCapability.AREngine.Core

**Start version**: 5.1.0(18)

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

Promise<[ARAugmentedImageDatabase](#section1410345414514)\>

 | 

Promise object, which returns an **ARAugmentedImageDatabase** object.

 |

**Error codes**:

For details about the error codes, please refer to [AR Engine Error Codes](../../ar-engine-error-codes/document.md).

| 
**Error Code**

 | 

**Error Message**

 |
| :-- | :-- |
| 

1009200001

 | 

Failure.

 |

**Example**:

import { arEngine } from '@kit.AREngine';

async function createARAugmentedImageDatabase(): Promise<void> {
  let imageDatabase: arEngine.ARAugmentedImageDatabase = await arEngine.createARAugmentedImageDatabase();
}

#### arEngine.createARPose

createARPose(rotation: Quaternion, translation: Vec3): ARPose

Creates and initializes an [ARPose](#section19274193834913) object in AR Engine and returns the object.

**System capability**: SystemCapability.AREngine.Core

**Start version**: 5.1.0(18)

**Parameters**:

| 
**Parameter**

 | 

Type

 | 

**Mandatory**

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

rotation

 | 

[Quaternion](../../../arkgraphics-3d/arkts-apis/graphics3d/scenetype/document.md#quaternion)

 | 

Yes

 | 

Data of the rotation component. This parameter is of the quaternion type. It is usually an array containing four elements, that is, a quaternion, which is used to represent and operate 3D rotation.

 |
| 

translation

 | 

[Vec3](../../../arkgraphics-3d/arkts-apis/graphics3d/scenetype/document.md#vec3)

 | 

Yes

 | 

Data of the translation component. This parameter is of the Vec3 type. It is usually an array that contains three elements, indicating the x, y, and z components of a 3D vector, and is used to indicate the translation position of an object.

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[ARPose](#section19274193834913)

 | 

Created pose object.

 |

**Error codes**:

For details about the error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [AR Engine Error Codes](../../ar-engine-error-codes/document.md).

| 
**Error Code**

 | 

**Error Message**

 |
| :-- | :-- |
| 

401

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |
| 

1009200001

 | 

Failure.

 |

**Example**:

import { Quaternion, Vec3 } from '@kit.ArkGraphics3D';
import { arEngine } from '@kit.AREngine';

let r: Quaternion = {
  x: 0,
  y: 0,
  z: 0,
  w: 0
};
let t: Vec3 = { x: 0, y: 0, z: 0 };
let pose: arEngine.ARPose = arEngine.createARPose(r, t);
