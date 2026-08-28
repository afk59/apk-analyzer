# AR Engine

#### Overview

This module provides APIs related to the AR capabilities of AR Engine. AR Engine provides three basic capabilities at its core: motion tracking, environment tracking, and hit testing.

**Start version**: 5.0.0(12)

#### Summary

#### \[h2\]File

| 
**Name**

 | 

**Description**

 |
| :-- | :-- |
| 

[ar\_engine\_core.h](../../header-files-and-structs/header-files/ar-engine-core-h/document.md)

 | 

Declares the APIs for accessing AR Engine; provides APIs related to the AR capabilities; covers basic AR capabilities at its core, including motion tracking, environment tracking, and hit testing.

 |

#### \[h2\]Structs

| 
**Name**

 | 

**Description**

 |
| :-- | :-- |
| 

struct [AREngine\_ARAugmentedImageSource](../../header-files-and-structs/structs/arengine-araugmentedimagesource/document.md)

 | 

Image data.

 |
| 

struct [AREngine\_ClipPlaneDistance](../../header-files-and-structs/structs/arengine-clipplanedistance/document.md)

 | 

Distance to the clipping planes.

 |
| 

struct [AREngine\_ARSemanticDensePointData](../../header-files-and-structs/structs/arengine-arsemanticdensepointdata/document.md)

 | 

Dense point cloud data of a high-precision geometric reconstruction object.

 |
| 

struct [AREngine\_ARSemanticDenseCubeData](../../header-files-and-structs/structs/arengine-arsemanticdensecubedata/document.md)

 | 

Cube data of a high-precision geometric reconstruction object.

 |

#### \[h2\]Macro Definitions

| 
**Name**

 | 

**Description**

 |
| :-- | :-- |
| 

[ARENGINE\_AABB\_POINT\_SIZE](#section1046854145717) = 6

 | 

Size of the bounding box coordinate array.

 |
| 

[ARENGINE\_DISTORTION\_COUNT](#section2059093619593) = 5

 | 

Number of camera distortion parameters.

 |
| 

[ARENGINE\_POSE\_RAW\_SIZE](#section14280842115815) = 7

 | 

Size of the pose data array.

 |
| 

[ARENGINE\_VIEW\_MATRIX\_SIZE](#section02261581599) = 16

 | 

Size of the transformation matrix array.

 |

#### \[h2\]Type Definitions

| 
**Name**

 | 

**Description**

 |
| :-- | :-- |
| 

typedef struct [AREngine\_ARAnchor](#ga76c16c9d68ba9a3b76f1869c60d8ca1d) [AREngine\_ARAnchor](#ga76c16c9d68ba9a3b76f1869c60d8ca1d)

 | 

Anchor object.

 |
| 

typedef struct [AREngine\_ARAnchorList](#ga516a7f0954dcfda438799aa9e7c6e872) [AREngine\_ARAnchorList](#ga516a7f0954dcfda438799aa9e7c6e872)

 | 

Anchor object list.

 |
| 

typedef struct [AREngine\_ARAugmentedImage](#section68491824155217) [AREngine\_ARAugmentedImage](#section68491824155217)

 | 

Trackable image object.

 |
| 

typedef struct [AREngine\_ARAugmentedImageDatabase](#section152051642330) [AREngine\_ARAugmentedImageDatabase](#section152051642330)

 | 

Trackable image database object.

 |
| 

typedef struct [AREngine\_ARCamera](#ga7bdcf1fb36c404d36e09ad70d2545d92) [AREngine\_ARCamera](#ga7bdcf1fb36c404d36e09ad70d2545d92)

 | 

Camera information for the current frame.

 |
| 

typedef struct [AREngine\_ARCameraConfig](#ga9b7a5a2082a4127f85a1c9a95cb9acba) [AREngine\_ARCameraConfig](#ga9b7a5a2082a4127f85a1c9a95cb9acba)

 | 

Camera configuration information.

 |
| 

typedef struct [AREngine\_ARCameraIntrinsics](#ga17948eef3aa7ff7f2fa8aff6a63b4b51) [AREngine\_ARCameraIntrinsics](#ga17948eef3aa7ff7f2fa8aff6a63b4b51)

 | 

Intrinsic camera parameters.

 |
| 

typedef struct [AREngine\_ARConfig](#gab0b32ef6018535fd30000f4b6d65f619) [AREngine\_ARConfig](#gab0b32ef6018535fd30000f4b6d65f619)

 | 

Used for configuring [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) capabilities (that is, capabilities and modes to use).

 |
| 

typedef struct [AREngine\_ARFrame](#gaf35f728a1179ef54a3eba9f1cf021719) [AREngine\_ARFrame](#gaf35f728a1179ef54a3eba9f1cf021719)

 | 

A frame of data processed by AR Engine.

 |
| 

typedef struct [AREngine\_ARHitResult](#gaeb304c8b21122eb7ffda7403316a3507) [AREngine\_ARHitResult](#gaeb304c8b21122eb7ffda7403316a3507)

 | 

Hit testing result object.

 |
| 

typedef struct [AREngine\_ARHitResultList](#ga1f2369453412bd4d77ab8f5aa2d52bb3) [AREngine\_ARHitResultList](#ga1f2369453412bd4d77ab8f5aa2d52bb3)

 | 

Hit testing result list.

 |
| 

typedef struct [AREngine\_ARImage](#gabfee13b0076f2f00b7efdef2717add59) [AREngine\_ARImage](#gabfee13b0076f2f00b7efdef2717add59)

 | 

Camera video stream frame object.

 |
| 

typedef struct [AREngine\_ARPlane](#ga76f9bdb23634312b8488fcbaff4aa9b5) [AREngine\_ARPlane](#ga76f9bdb23634312b8488fcbaff4aa9b5)

 | 

Plane object.

 |
| 

typedef struct [AREngine\_ARPoint](#gac7b6923d92487d68e77543dd223364d6) [AREngine\_ARPoint](#gac7b6923d92487d68e77543dd223364d6)

 | 

Point object.

 |
| 

typedef struct [AREngine\_ARPointCloud](#gacc054cea4851be61b160f32b433737fc) [AREngine\_ARPointCloud](#gacc054cea4851be61b160f32b433737fc)

 | 

Collection of trackable 3D point clouds.

 |
| 

typedef struct [AREngine\_ARPose](#gab2fa63142ebfb09f0c2ddf88cdb86604) [AREngine\_ARPose](#gab2fa63142ebfb09f0c2ddf88cdb86604)

 | 

Pose object.

 |
| 

typedef struct [AREngine\_ARSceneMesh](#section543212520614) [AREngine\_ARSceneMesh](#section543212520614)

 | 

Environment mesh data set.

 |
| 

typedef struct [AREngine\_ARSemanticDenseData](#section1410813229144) [AREngine\_ARSemanticDenseData](#section1410813229144)

 | 

High-precision geometric reconstruction object data set.

 |
| 

typedef struct [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650)

 | 

Used to manage the system status of AR Engine.

 |
| 

typedef struct [AREngine\_ARTarget](#ga9af9c1d51ed065f80b373824e0425fa0) [AREngine\_ARTarget](#ga9af9c1d51ed065f80b373824e0425fa0)

 | 

Object.

 |
| 

typedef struct [AREngine\_ARTrackable](#ga54808ebd1a6ed026494acdd945c4f970) [AREngine\_ARTrackable](#ga54808ebd1a6ed026494acdd945c4f970)

 | 

Trackable object, such as a point or a plane.

 |
| 

typedef struct [AREngine\_ARTrackableList](#gae69e4963b595036fc5e6119a055bb205) [AREngine\_ARTrackableList](#gae69e4963b595036fc5e6119a055bb205)

 | 

Trackable object list.

 |
| 

typedef void (\*[HMS\_AREngine\_PhotoAvailableCallback](#section430673420224))([OH\_NativeBuffer](../../../../../standard-libraries/vulkan/vulkan-extensions/oh-nativebuffer/document.md) \*photoBuffer)

 | 

Callback triggered when a photo stream image is output.

 |

#### \[h2\]Enumerations

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

[AREngine\_ARAddAugmentedImageReason](#section2441053595) {

ARENGINE\_ADD\_AUGMENTED\_IMAGE\_REASON\_NONE = 0,

ARENGINE\_ADD\_AUGMENTED\_IMAGE\_REASON\_SIZE\_NOT\_MATCH = 1,

ARENGINE\_ADD\_AUGMENTED\_IMAGE\_REASON\_LIGHT\_ANOMALY = 2,

ARENGINE\_ADD\_AUGMENTED\_IMAGE\_REASON\_FEATURE\_LIMIT = 3,

ARENGINE\_ADD\_AUGMENTED\_IMAGE\_REASON\_OTHER = 4

}

 | 

Possible cause of the tracking failure.

 |
| 

[AREngine\_ARConfidenceLevel](#section959011484610) {

ARENGINE\_DEPTH\_CONFIDENCE\_LOW = 0,

ARENGINE\_DEPTH\_CONFIDENCE\_MEDIUM = 1,

ARENGINE\_DEPTH\_CONFIDENCE\_HIGH = 2

}

 | 

Depth confidence.

 |
| 

[AREngine\_ARDepthMode](#section12321429115215) {

ARENGINE\_DEPTH\_MODE\_DISABLED = 0,

ARENGINE\_DEPTH\_MODE\_AUTOMATIC = 1

}

 | 

Depth mode.

 |
| 

[AREngine\_ARFocusMode](#gaf50530faa0d094182a0db0c73b75d875) {

ARENGINE\_FOCUS\_MODE\_FIXED = 0,

ARENGINE\_FOCUS\_MODE\_AUTO = 1

}

 | 

Focus mode.

 |
| 

[AREngine\_ARImageDatabaseMode](#section683253471219) {

ARENGINE\_ADD\_NORMAL = 0,

ARENGINE\_ADD\_AUTO = 1

}

 | 

Mode of adding images to the feature database for tracking.

 |
| 

[AREngine\_ARImageFormat](#gadfcf7a1211ed12a90f377610d0f838ac) {

ARENGINE\_IMAGE\_UNKNOWN = 0,

ARENGINE\_IMAGE\_YUV\_420\_888 = 2,

ARENGINE\_IMAGE\_Y\_8 = 3,

ARENGINE\_IMAGE\_Y\_16 = 4

}

 | 

Image format.

 |
| 

[AREngine\_ARImageStreamMode](#section184201559356) {

ARENGINE\_IMAGE\_STREAM\_MODE\_PREVIEW = 0,

ARENGINE\_IMAGE\_STREAM\_MODE\_PREVIEW\_AND\_PHOTO = 1

}

 | 

Image data stream mode. By default, **ARENGINE\_IMAGE\_STREAM\_MODE\_PREVIEW** is used.

 |
| 

[AREngine\_ARMeshMode](#section19436658201620) {

ARENGINE\_MESH\_MODE\_DISABLED = 0,

ARENGINE\_MESH\_MODE\_ENABLE=1

}

 | 

Mesh enabling mode.

 |
| 

[AREngine\_ARPlaneFindingMode](#gab8e7db52d819359026fc4a82815d3fff) {

ARENGINE\_PLANE\_FINDING\_MODE\_DISABLED = 0,

ARENGINE\_PLANE\_FINDING\_MODE\_HORIZONTAL = 1,

ARENGINE\_PLANE\_FINDING\_MODE\_VERTICAL = 2,

ARENGINE\_PLANE\_FINDING\_MODE\_HORIZONTAL\_AND\_VERTICAL = 3

}

 | 

Plane finding mode.

 |
| 

[AREngine\_ARPlaneType](#ga895db37a92155584c5448bee30a8beab) {

ARENGINE\_PLANE\_FACING\_HORIZONTAL\_UPWARD = 0,

ARENGINE\_PLANE\_FACING\_HORIZONTAL\_DOWNWARD = 1,

ARENGINE\_PLANE\_FACING\_VERTICAL = 2,

ARENGINE\_PLANE\_FACING\_INVALID = 3

}

 | 

Plane type.

 |
| 

[AREngine\_ARPointOrientationMode](#ga0e2893593f4372954fd97519e0a63855) {

ARENGINE\_POINT\_ORIENTATION\_INITIALIZED\_TO\_IDENTITY = 0,

ARENGINE\_POINT\_ORIENTATION\_ESTIMATED\_SURFACE\_NORMAL = 1

}

 | 

Orientation mode.

 |
| 

[AREngine\_ARPoseMode](#section1249515330198) {

ARENGINE\_POSE\_MODE\_GRAVITY = 0,

ARENGINE\_POSE\_MODE\_GRAVITY\_HEADING = 1

}

 | 

Output camera pose alignment format of AR Engine.

 |
| 

[AREngine\_ARPoseType](#gae551da7b220b8b38140c3c28882e5010) {

ARENGINE\_POSE\_TYPE\_IDENTITY = 0,

ARENGINE\_POSE\_TYPE\_ROTATE\_90 = 1,

ARENGINE\_POSE\_TYPE\_ROTATE\_180 = 2,

ARENGINE\_POSE\_TYPE\_ROTATE\_270 = 3

}

 | 

Pose type.

 |
| 

[AREngine\_ARPowerMode](#ga3d925e007e2847e69f22af68ec922507) {

ARENGINE\_POWER\_MODE\_NORMAL = 0,

ARENGINE\_POWER\_MODE\_POWER\_SAVING = 1,

ARENGINE\_POWER\_MODE\_PERFORMANCE\_FIRST = 2,

ARENGINE\_POWER\_MODE\_BOOST = 3,

ARENGINE\_POWER\_MODE\_ULTRA\_POWER\_SAVING = 11

}

 | 

Power consumption mode.

 |
| 

[AREngine\_ARPreviewMode](#gadef0f2099b106b872a014ef6551906ae) {

ARENGINE\_PREVIEW\_MODE\_ENABLED = 0,

ARENGINE\_PREVIEW\_MODE\_DISABLED = 1

}

 | 

Preview mode.

 |
| 

[AREngine\_ARSemanticDenseMode](#section09971756142213) {

ARENGINE\_SEMANTIC\_DENSE\_MODE\_DISABLED = 0,

ARENGINE\_SEMANTIC\_DENSE\_MODE\_NORMAL = 1,

ARENGINE\_SEMANTIC\_DENSE\_MODE\_CUBE\_VOLUME = 2,

ARENGINE\_SEMANTIC\_DENSE\_MODE\_CUBE\_SPACE = 3

}

 | 

Recognition mode of high-precision geometric reconstruction.

 |
| 

[AREngine\_ARSemanticMode](#ga34d3000de29454b99d89406d288d6ed5) {

ARENGINE\_SEMANTIC\_MODE\_NONE = 0,

ARENGINE\_SEMANTIC\_MODE\_PLANE = 1,

ARENGINE\_SEMANTIC\_MODE\_TARGET = 2

}

 | 

Semantic mode.

 |
| 

[AREngine\_ARSemanticPlaneLabel](#gafbb6b69fefdc417ba6437ce2fe587cb1) {

ARENGINE\_PLANE\_UNKNOWN = 0,

ARENGINE\_PLANE\_WALL = 1,

ARENGINE\_PLANE\_FLOOR = 2,

ARENGINE\_PLANE\_SEAT = 3,

ARENGINE\_PLANE\_TABLE = 4,

ARENGINE\_PLANE\_CEILING = 5,

ARENGINE\_PLANE\_DOOR = 6,

ARENGINE\_PLANE\_WINDOW = 7,

ARENGINE\_PLANE\_BED = 8,

ARENGINE\_PLANE\_SPACE = 9,

ARENGINE\_CUBE\_VOLUME = 10,

ARENGINE\_CUBE\_SPACE = 11

}

 | 

Semantic type of the current plane.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) {

ARENGINE\_SUCCESS = 0,

ARENGINE\_ERROR\_PERMISSION\_NOT\_GRANTED = 201,

ARENGINE\_ERROR\_INVALID\_ARGUMENT = 401,

ARENGINE\_ERROR\_DEVICE\_NOT\_SUPPORTED = 801,

ARENGINE\_ERROR\_FATAL = 1009200001,

ARENGINE\_ERROR\_SESSION\_PAUSED = 1009200002,

ARENGINE\_ERROR\_SESSION\_NOT\_PAUSED = 1009200003,

ARENGINE\_ERROR\_NOT\_TRACKING = 1009200004,

ARENGINE\_ERROR\_TEXTURE\_NOT\_SET = 1009200005,

ARENGINE\_ERROR\_MISSING\_GL\_CONTEXT = 1009200006,

ARENGINE\_ERROR\_UNSUPPORTED\_CONFIGURATION = 1009200007,

ARENGINE\_ERROR\_RESOURCE\_EXHAUSTED = 1009200008,

ARENGINE\_ERROR\_NOT\_AVAILABLE = 1009200009,

ARENGINE\_ERROR\_CAMERA\_NOT\_AVAILABLE = 1009200010,

ARENGINE\_ERROR\_IMAGE\_EXCEED\_NUM\_LIMIT = 1009200011,

ARENGINE\_ERROR\_IMAGE\_INSUFFICIENT\_QUALITY = 1009200012,

ARENGINE\_ERROR\_IMAGE\_INVALID\_DATABASE = 1009200013,

ARENGINE\_ERROR\_IMAGE\_ADD\_IMAGE\_TRACKING\_STATE = 1009200014,

ARENGINE\_ERROR\_NATIVEBUFFER\_CREATE\_FAILED = 1009200015,

ARENGINE\_ERROR\_NATIVEBUFFER\_WRITE\_FAILED = 1009200016,

ARENGINE\_CAMERA\_SERVICE\_FATAL\_ERROR = 1009200017

}

 | 

Error code returned by the API.

 |
| 

[AREngine\_ARTargetShapeLabel](#gaed68dc13cc314da98d79c88b12d3ae49) {

ARENGINE\_TARGET\_SHAPE\_UNKNOWN = 0,

ARENGINE\_TARGET\_SHAPE\_CUBE = 1,

ARENGINE\_TARGET\_SHAPE\_CIRCLE = 2,

ARENGINE\_TARGET\_SHAPE\_RECTANGLE = 3

}

 | 

Shape of the recognized object.

 |
| 

[AREngine\_ARTrackableType](#ga993948a19fd2bdfa5b946e13a8d4fe3d) {

ARENGINE\_TRACKABLE\_BASE = 0x41520100,

ARENGINE\_TRACKABLE\_PLANE = 0x41520101,

ARENGINE\_TRACKABLE\_POINT = 0x41520102,

ARENGINE\_TRACKABLE\_AUGMENTED\_IMAGE = 0x41520104,

ARENGINE\_TRACKABLE\_TARGET = 0x50000008,

ARENGINE\_TRACKABLE\_INVALID = 0

}

 | 

Type of a trackable object, such as a plane or a point.

 |
| 

[AREngine\_ARTrackingState](#gaae57d2f58331e1033b60cdb2d506a382) {

ARENGINE\_TRACKING\_STATE\_TRACKING = 0,

ARENGINE\_TRACKING\_STATE\_PAUSED = 1,

ARENGINE\_TRACKING\_STATE\_STOPPED = 2

}

 | 

Tracking state of the trackable object.

 |
| 

[AREngine\_ARTrackingStateReason](#ga67774b71935ef2f8a2ae5e5822c3dcdb) {

ARENGINE\_TRACKING\_STATE\_REASON\_NONE = 0,

ARENGINE\_TRACKING\_STATE\_REASON\_EXCESSIVE\_MOTION = 1,

ARENGINE\_TRACKING\_STATE\_REASON\_INSUFFICIENT\_FEATURES = 2

}

 | 

Possible causes of tracking failures.

 |
| 

[AREngine\_ARType](#ga987888aea7dcaa9abcdb64581c850bf5) {

ARENGINE\_TYPE\_WORLD = 0x01,

ARENGINE\_TYPE\_IMAGE = 0x80

}

 | 

AR capability type.

 |
| 

[AREngine\_ARUpdateMode](#gabd21cc975ee97b7fb2133af0068ebb5e) {

ARENGINE\_UPDATE\_MODE\_BLOCKING = 0,

ARENGINE\_UPDATE\_MODE\_LATEST = 1

}

 | 

Data update mode specified by [HMS\_AREngine\_ARSession\_Update](#ga1d1cacf372a8011a439f0e4e76994259).

 |

#### \[h2\]Functions

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARAnchor\_Detach](#ga6b731c00cc038f62d21ccb280067114b) ([AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, [AREngine\_ARAnchor](#ga76c16c9d68ba9a3b76f1869c60d8ca1d) \*anchor)

 | 

Instructs AR Engine to stop tracking and unbind an anchor.

CAUTION:

This function does not release [AREngine\_ARAnchor](#ga76c16c9d68ba9a3b76f1869c60d8ca1d). You need to call [HMS\_AREngine\_ARAnchor\_Release](#gad04b12f9a2b0415789de5d6e1692f51c) to release this anchor.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARAnchor\_GetPose](#gad937acfc5d49f0909bdd84677bb0731a) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARAnchor](#ga76c16c9d68ba9a3b76f1869c60d8ca1d) \*anchor, [AREngine\_ARPose](#gab2fa63142ebfb09f0c2ddf88cdb86604) \*outPose)

 | 

Obtains the pose of a specific anchor in the world coordinate system.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARAnchor\_GetTrackingState](#ga6d8c173cc1ef3888f1bedfd6adb2efb3) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARAnchor](#ga76c16c9d68ba9a3b76f1869c60d8ca1d) \*anchor, [AREngine\_ARTrackingState](#gaae57d2f58331e1033b60cdb2d506a382) \*outTrackingState)

 | 

Obtains the tracking state of the pose of a specific anchor.

 |
| 

void [HMS\_AREngine\_ARAnchor\_Release](#gad04b12f9a2b0415789de5d6e1692f51c) ([AREngine\_ARAnchor](#ga76c16c9d68ba9a3b76f1869c60d8ca1d) \*anchor)

 | 

Releases the memory used by a specific anchor object.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARAnchorList\_AcquireItem](#ga1f520dddd96c9918163bff8b68f428fc) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARAnchorList](#ga516a7f0954dcfda438799aa9e7c6e872) \*anchorList, int32\_t index, [AREngine\_ARAnchor](#ga76c16c9d68ba9a3b76f1869c60d8ca1d) \*\*outAnchor)

 | 

Obtains the anchor at a specific location from the anchor object list.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARAnchorList\_Create](#ga30492334f7a06b98ef0ad5831d33b198) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, [AREngine\_ARAnchorList](#ga516a7f0954dcfda438799aa9e7c6e872) \*\*outAnchorList)

 | 

Creates a list of anchor objects.

 |
| 

void [HMS\_AREngine\_ARAnchorList\_Destroy](#ga5b1078469a123466245f65524c9c33be) ([AREngine\_ARAnchorList](#ga516a7f0954dcfda438799aa9e7c6e872) \*anchorList)

 | 

Releases a list of anchor objects.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARAnchorList\_GetSize](#ga9e96df41cdb973d7e45c714b1bd31fd1) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARAnchorList](#ga516a7f0954dcfda438799aa9e7c6e872) \*anchorList, int32\_t \*outSize)

 | 

Obtains the number of anchors in the anchor object list.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARAugmentedImage\_AcquireName](#section110712352334) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARAugmentedImage](#section68491824155217) \*augmentedImage, char \*augmentedImageName, uint32\_t \*outNameLength)

 | 

Returns the name of the tracking image.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARAugmentedImage\_GetCenterPose](#section498975343520) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARAugmentedImage](#section68491824155217) \*augmentedImage, [AREngine\_ARPose](#gab2fa63142ebfb09f0c2ddf88cdb86604) \*outPose)

 | 

Obtains the pose information of the center point of a tracking image in the world coordinate system.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARAugmentedImage\_GetExtendX](#section917593011382) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARAugmentedImage](#section68491824155217) \*augmentedImage, float \*outExtendX)

 | 

Obtains the estimated value on the X axis based on the center point of the image as the coordinate origin.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARAugmentedImage\_GetExtendZ](#section9630192711390) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARAugmentedImage](#section68491824155217) \*augmentedImage, float \*outExtendZ)

 | 

Obtains the estimated value on the Z axis based on the center point of the image as the coordinate origin.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARAugmentedImage\_GetIndex](#section27041685401) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARAugmentedImage](#section68491824155217) \*augmentedImage, uint32\_t \*outIndex)

 | 

Obtains the index of a tracking image in the tracking image database.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARAugmentedImageDatabase\_AddImage](#section0315115618403) ([AREngine\_ARAugmentedImageDatabase](#section152051642330) \*database, const [AREngine\_ARAugmentedImageSource](../../header-files-and-structs/structs/arengine-araugmentedimagesource/document.md) \*image, uint32\_t \*outIndex, [AREngine\_ARAddAugmentedImageReason](#section2441053595) \*outReason)

 | 

Adds an image to the image database and outputs the index of the image.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARAugmentedImageDatabase\_Create](#section4108822184411) ([AREngine\_ARAugmentedImageDatabase](#section152051642330) \*\*outDatabase)

 | 

Creates an empty tracking image database.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARAugmentedImageDatabase\_Deserialize](#section1619582764511) (const uint8\_t \*buffer, const uint64\_t bufSize, [AREngine\_ARAugmentedImageDatabase](#section152051642330) \*\*outDatabase)

 | 

Deserializes the feature database.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARAugmentedImageDatabase\_Destroy](#section14702121818469) ([AREngine\_ARAugmentedImageDatabase](#section152051642330) \*database)

 | 

Releases an image database object.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARAugmentedImageDatabase\_GetAddMode](#section1731662218476) (const [AREngine\_ARAugmentedImageDatabase](#section152051642330) \*database, [AREngine\_ARImageDatabaseMode](#section683253471219) \*outAddMode)

 | 

Obtains the mode of adding a tracking image.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARAugmentedImageDatabase\_SetAddMode](#section2579104674818) (const [AREngine\_ARAugmentedImageDatabase](#section152051642330) \*database, [AREngine\_ARImageDatabaseMode](#section683253471219) addMode)

 | 

Sets the mode of adding a tracking image.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARAugmentedImageDatabase\_GetCapacity](#section650873916491) (const [AREngine\_ARAugmentedImageDatabase](#section152051642330) \*database, uint32\_t \*outCapacity)

 | 

Obtains the maximum number of images that can be added.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARAugmentedImageDatabase\_GetImageCount](#section6183812506) (const [AREngine\_ARAugmentedImageDatabase](#section152051642330) \*database, uint32\_t \*outImageCount)

 | 

Obtains the number of images stored in the database.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARAugmentedImageDatabase\_Serialize](#section6536162875117) (const [AREngine\_ARAugmentedImageDatabase](#section152051642330) \*database, uint8\_t \*\*outBuffer, uint64\_t \*outBufSize)

 | 

Serializes the feature database.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARCamera\_GetDisplayOrientedPose](#ga088648130f3a91cdf8d7b95f5ee1faf2) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARCamera](#ga7bdcf1fb36c404d36e09ad70d2545d92) \*camera, [AREngine\_ARPose](#gab2fa63142ebfb09f0c2ddf88cdb86604) \*outPose)

 | 

Sets **outPose** to the pose of the virtual camera (facing the display) in the world space, in order to render AR content into the latest frame.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARCamera\_GetImageIntrinsics](#ga8e6f32adc3bd59504042d4e18bfb3432) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARCamera](#ga7bdcf1fb36c404d36e09ad70d2545d92) \*camera, [AREngine\_ARCameraIntrinsics](#ga17948eef3aa7ff7f2fa8aff6a63b4b51) \*outIntrinsics)

 | 

Obtains the object of the offline intrinsic camera parameters. This object can be used to obtain the camera's focal length, image dimensions, principal point, and distortion parameters.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARCamera\_GetPose](#ga00df108c4ba187967a10e9c4d2e27d3a) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARCamera](#ga7bdcf1fb36c404d36e09ad70d2545d92) \*camera, [AREngine\_ARPose](#gab2fa63142ebfb09f0c2ddf88cdb86604) \*outPose)

 | 

Sets **outPose** to the pose of the physical camera in the world space in the latest frame. The pose is the pose of the OpenGL camera.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARCamera\_GetProjectionMatrix](#ga01feacf9cd393a0598e2ac5cf7b61693) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARCamera](#ga7bdcf1fb36c404d36e09ad70d2545d92) \*camera, [AREngine\_ClipPlaneDistance](../../header-files-and-structs/structs/arengine-clipplanedistance/document.md) clipPlaneDistance, float \*outDestColMajor4x4, int32\_t destColMajor4x4Num)

 | 

Obtains the projection matrix used for rendering virtual content on top of the camera image. This matrix can be used for converting from the camera coordinate system to the clip coordinate system.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARCamera\_GetTrackingState](#ga2dc931eee56ae5ea899f8acc08eb3f36) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARCamera](#ga7bdcf1fb36c404d36e09ad70d2545d92) \*camera, [AREngine\_ARTrackingState](#gaae57d2f58331e1033b60cdb2d506a382) \*outTrackingState)

 | 

Obtains the current tracking state of the camera.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARCamera\_GetTrackingStateReason](#gab5411813f2e4ac6de4ebbccfc1bbbd35) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARCamera](#ga7bdcf1fb36c404d36e09ad70d2545d92) \*camera, [AREngine\_ARTrackingStateReason](#ga67774b71935ef2f8a2ae5e5822c3dcdb) \*outTrackingStateReason)

 | 

Obtains the reason when the current tracking state of the camera is [ARENGINE\_TRACKING\_STATE\_PAUSED](#gaae57d2f58331e1033b60cdb2d506a382).

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARCamera\_GetViewMatrix](#ga130b4689d7d967e812d24fc2be071d68) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARCamera](#ga7bdcf1fb36c404d36e09ad70d2545d92) \*camera, float \*outColMajor4x4, int32\_t colMajor4x4Num)

 | 

Obtains the view matrix of the camera in the latest frame.

 |
| 

void [HMS\_AREngine\_ARCamera\_Release](#ga16909b4002b9c6250dad88bb8397adc9) ([AREngine\_ARCamera](#ga7bdcf1fb36c404d36e09ad70d2545d92) \*camera)

 | 

Releases the reference to the camera.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARCameraConfig\_Create](#gac6402425c6c6390da3c4e57d328da443) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, [AREngine\_ARCameraConfig](#ga9b7a5a2082a4127f85a1c9a95cb9acba) \*\*outCameraConfig)

 | 

Creates a camera configuration object.

 |
| 

void [HMS\_AREngine\_ARCameraConfig\_Destroy](#ga2540153f0404799943470c41dff3b5f4) ([AREngine\_ARCameraConfig](#ga9b7a5a2082a4127f85a1c9a95cb9acba) \*cameraConfig)

 | 

Releases a camera configuration object.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARCameraConfig\_GetImageDimensions](#gac3dc81c1c9e6945dd4a3de30e45ccc8f) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARCameraConfig](#ga9b7a5a2082a4127f85a1c9a95cb9acba) \*cameraConfig, int32\_t \*outWidth, int32\_t \*outHeight)

 | 

Obtains the size of the image sent by the camera to the CPU for processing from a camera configuration object.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARCameraConfig\_GetTextureDimensions](#ga19ade172d2e2dcd67495f6be1bcc2706) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARCameraConfig](#ga9b7a5a2082a4127f85a1c9a95cb9acba) \*cameraConfig, int32\_t \*outWidth, int32\_t \*outHeight)

 | 

Obtains the size of the image texture sent by the camera to the GPU for processing from a camera configuration object.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARCameraIntrinsics\_Create](#ga027e92d8f7b25e6e577a9658545e2c2a) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, [AREngine\_ARCameraIntrinsics](#ga17948eef3aa7ff7f2fa8aff6a63b4b51) \*\*outIntrinsics)

 | 

Creates an object of the intrinsic camera parameters.

 |
| 

void [HMS\_AREngine\_ARCameraIntrinsics\_Destroy](#ga09323e31d8bd08e5c1d60bccb118b68b) ([AREngine\_ARCameraIntrinsics](#ga17948eef3aa7ff7f2fa8aff6a63b4b51) \*intrinsics)

 | 

Releases a specific object of intrinsic camera parameters.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARCameraIntrinsics\_GetDistortion](#ga7caab88bb0e859921004ab1121ee2b5d) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARCameraIntrinsics](#ga17948eef3aa7ff7f2fa8aff6a63b4b51) \*intrinsics, float \*outDistortion, int32\_t distortionNum)

 | 

Obtains the distortion parameters of a camera.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARCameraIntrinsics\_GetFocalLength](#gab57c6586ac4d2da1b87f1c0394ffc1b3) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARCameraIntrinsics](#ga17948eef3aa7ff7f2fa8aff6a63b4b51) \*intrinsics, float \*outFocalX, float \*outFocalY)

 | 

Obtains the focal length of a camera (in pixels).

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARCameraIntrinsics\_GetImageDimensions](#gaab99bc9ba5b9b734ef11888fe2bb3f86) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARCameraIntrinsics](#ga17948eef3aa7ff7f2fa8aff6a63b4b51) \*intrinsics, int32\_t \*outWidth, int32\_t \*outHeight)

 | 

Obtains the camera image dimensions, including the width and height (in pixels).

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARCameraIntrinsics\_GetPrincipalPoint](#gaeb38c1df26e1af9d993574c7f13b8f5c) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARCameraIntrinsics](#ga17948eef3aa7ff7f2fa8aff6a63b4b51) \*intrinsics, float \*outPrincipalX, float \*outPrincipalY)

 | 

Obtains the principal point of a camera, with the location of the point expressed in pixels.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARConfig\_Create](#ga97376432184fe702f2451e32b52298fb) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, [AREngine\_ARConfig](#gab0b32ef6018535fd30000f4b6d65f619) \*\*outConfig)

 | 

Creates a configuration object with a proper default configuration.

 |
| 

void [HMS\_AREngine\_ARConfig\_Destroy](#gac86d0db69e8658f2f6bd267d7b288c0a) ([AREngine\_ARConfig](#gab0b32ef6018535fd30000f4b6d65f619) \*config)

 | 

Releases the memory used by a specific configuration object.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARConfig\_GetARType](#ga827ca7c2c2f288338f781e87e28ef996) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARConfig](#gab0b32ef6018535fd30000f4b6d65f619) \*config, [AREngine\_ARType](#ga987888aea7dcaa9abcdb64581c850bf5) \*type)

 | 

Obtains the AR capability type in use.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARConfig\_SetARType](#gaf12b21d8591c5265f8a0e847b716d65c) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, [AREngine\_ARConfig](#gab0b32ef6018535fd30000f4b6d65f619) \*config, [AREngine\_ARType](#ga987888aea7dcaa9abcdb64581c850bf5) type)

 | 

Sets the AR capability type to use.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARConfig\_GetCameraPreviewMode](#gaf4746b3377bd69a52d0587a582cc4679) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, [AREngine\_ARConfig](#gab0b32ef6018535fd30000f4b6d65f619) \*config, [AREngine\_ARPreviewMode](#gadef0f2099b106b872a014ef6551906ae) \*outMode)

 | 

Obtains the current preview mode.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARConfig\_SetCameraPreviewMode](#gac5e6992e38516f75cc6faf1a34047f5d) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, [AREngine\_ARConfig](#gab0b32ef6018535fd30000f4b6d65f619) \*config, [AREngine\_ARPreviewMode](#gadef0f2099b106b872a014ef6551906ae) mode)

 | 

Sets the preview mode.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARConfig\_GetDepthMode](#section6878812194715) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARConfig](#gab0b32ef6018535fd30000f4b6d65f619) \*config, [AREngine\_ARDepthMode](#section12321429115215) \*outDepthMode)

 | 

Obtains the current depth mode.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARConfig\_SetDepthMode](#section12608229155413) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, [AREngine\_ARConfig](#gab0b32ef6018535fd30000f4b6d65f619) \*config, [AREngine\_ARDepthMode](#section12321429115215) depthMode)

 | 

Sets the depth mode.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARConfig\_GetFocusMode](#gae92d8207f54468354ed52ad132e172f9) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARConfig](#gab0b32ef6018535fd30000f4b6d65f619) \*config, [AREngine\_ARFocusMode](#gaf50530faa0d094182a0db0c73b75d875) \*focusMode)

 | 

Obtains the current camera focus mode.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARConfig\_SetFocusMode](#ga7bcf745a74196cb21dca5e4feec18325) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, [AREngine\_ARConfig](#gab0b32ef6018535fd30000f4b6d65f619) \*config, [AREngine\_ARFocusMode](#gaf50530faa0d094182a0db0c73b75d875) focusMode)

 | 

Sets the required camera focus mode.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARConfig\_GetMaxMapSize](#ga65bae175f2ac6da6dca71988c3ac37df) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARConfig](#gab0b32ef6018535fd30000f4b6d65f619) \*config, uint64\_t \*maxMapSize)

 | 

Obtains the maximum memory size for storing map data.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARConfig\_SetMaxMapSize](#ga82fd530a4377b0c0e01c9031aa238372) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, [AREngine\_ARConfig](#gab0b32ef6018535fd30000f4b6d65f619) \*config, uint64\_t maxMapSize)

 | 

Sets the maximum memory size for storing map data.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARConfig\_GetMeshMode](#section5607016063) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, [AREngine\_ARConfig](#gab0b32ef6018535fd30000f4b6d65f619) \*config, [AREngine\_ARMeshMode](#section19436658201620) \*outMeshMode)

 | 

Obtains the current mesh mode.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARConfig\_SetMeshMode](#section53081741287) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, [AREngine\_ARConfig](#gab0b32ef6018535fd30000f4b6d65f619) \*config, [AREngine\_ARMeshMode](#section19436658201620) meshMode)

 | 

Sets the mesh mode.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARConfig\_GetPlaneFindingMode](#ga8aa9412802c98ece87d140b063f50839) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARConfig](#gab0b32ef6018535fd30000f4b6d65f619) \*config, [AREngine\_ARPlaneFindingMode](#gab8e7db52d819359026fc4a82815d3fff) \*planeFindingMode)

 | 

Obtains the current plane finding mode.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARConfig\_SetPlaneFindingMode](#ga884a7db93778e24eef0dfaa794c45674) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, [AREngine\_ARConfig](#gab0b32ef6018535fd30000f4b6d65f619) \*config, [AREngine\_ARPlaneFindingMode](#gab8e7db52d819359026fc4a82815d3fff) planeFindingMode)

 | 

Sets the required plane finding mode.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARConfig\_GetPoseMode](#section7289861874) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARConfig](#gab0b32ef6018535fd30000f4b6d65f619) \*config, [AREngine\_ARPoseMode](#section1249515330198) \*poseMode)

 | 

Obtains the alignment mode of the pose coordinate system output by the camera.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARConfig\_SetPoseMode](#section53221628698) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, [AREngine\_ARConfig](#gab0b32ef6018535fd30000f4b6d65f619) \*config, [AREngine\_ARPoseMode](#section1249515330198) poseMode)

 | 

Sets the alignment mode of the pose coordinate system output by the camera.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARConfig\_GetPowerMode](#ga3c02b15907c21a20e6efcd018750a29f) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARConfig](#gab0b32ef6018535fd30000f4b6d65f619) \*config, [AREngine\_ARPowerMode](#ga3d925e007e2847e69f22af68ec922507) \*powerMode)

 | 

Obtains the current power consumption mode.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARConfig\_SetPowerMode](#gac5048a3977d04d75ba622a0411b03774) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, [AREngine\_ARConfig](#gab0b32ef6018535fd30000f4b6d65f619) \*config, [AREngine\_ARPowerMode](#ga3d925e007e2847e69f22af68ec922507) powerMode)

 | 

Sets the power consumption mode.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARConfig\_SetPreviewSize](#ga8e9f74ef162604dc9bf07204237b45ab) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, [AREngine\_ARConfig](#gab0b32ef6018535fd30000f4b6d65f619) \*config, uint32\_t width, uint32\_t height)

 | 

Sets preview image dimensions. Only a 4:3 aspect ratio is supported. An image exceeding this ratio will default to 1440 x 1080 px.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARConfig\_GetSemanticDenseMode](#section1099254315514) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARConfig](#gab0b32ef6018535fd30000f4b6d65f619) \*config, [AREngine\_ARSemanticDenseMode](#section09971756142213) \*outSemanticDenseMode)

 | 

Obtains the set high-precision geometric reconstruction mode.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARConfig\_SetSemanticDenseMode](#section1569718841012) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, [AREngine\_ARConfig](#gab0b32ef6018535fd30000f4b6d65f619) \*config, [AREngine\_ARSemanticDenseMode](#section09971756142213) semanticDenseMode)

 | 

Sets the high-precision geometric reconstruction mode.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARConfig\_GetSemanticMode](#ga61325a1e0157e477c2ff95c1c0030567) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARConfig](#gab0b32ef6018535fd30000f4b6d65f619) \*config, [AREngine\_ARSemanticMode](#ga34d3000de29454b99d89406d288d6ed5) \*mode)

 | 

Obtains the configured semantic recognition mode.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARConfig\_SetSemanticMode](#gaae87c1ef02b6e9bab123fae2086da248) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, [AREngine\_ARConfig](#gab0b32ef6018535fd30000f4b6d65f619) \*config, [AREngine\_ARSemanticMode](#ga34d3000de29454b99d89406d288d6ed5) mode)

 | 

Sets the required semantic recognition mode.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARConfig\_GetUpdateMode](#gaf32a3cb1f345cd5a243683ecdec63cef) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARConfig](#gab0b32ef6018535fd30000f4b6d65f619) \*config, [AREngine\_ARUpdateMode](#gabd21cc975ee97b7fb2133af0068ebb5e) \*updateMode)

 | 

Obtains the current preview update mode.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARConfig\_SetUpdateMode](#ga871c8aebc084cbba41220d255c46803b) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, [AREngine\_ARConfig](#gab0b32ef6018535fd30000f4b6d65f619) \*config, [AREngine\_ARUpdateMode](#gabd21cc975ee97b7fb2133af0068ebb5e) updateMode)

 | 

Sets the preview update mode.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARConfig\_SetPhotoStreamSize](#section21861035164816)(const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, [AREngine\_ARConfig](#gab0b32ef6018535fd30000f4b6d65f619) \*config, uint32\_t width, uint32\_t height)

 | 

Sets the resolution of an image captured from the photo stream when [AREngine\_ARImageStreamMode](#section184201559356) is set to **ARENGINE\_IMAGE\_STREAM\_MODE\_PREVIEW\_AND\_PHOTO**. Only resolutions at the aspect ratio 4:3 are supported. If the aspect ratio is not 4:3, the device's maximum resolution at the aspect ratio 4:3 will be automatically used.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARConfig\_SetImageStreamMode](#section10809428846)(const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, [AREngine\_ARConfig](#gab0b32ef6018535fd30000f4b6d65f619) \*config, [AREngine\_ARImageStreamMode](#section184201559356) mode)

 | 

Sets the image stream mode.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARConfig\_GetImageStreamMode](#section387103819713)(const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, [AREngine\_ARConfig](#gab0b32ef6018535fd30000f4b6d65f619) \*config, [AREngine\_ARImageStreamMode](#section184201559356) \*outMode)

 | 

Obtains the image stream mode.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARFrame\_AcquireCamera](#ga5295c975a0ff3d633a1dde5a8eb70863) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARFrame](#gaf35f728a1179ef54a3eba9f1cf021719) \*frame, [AREngine\_ARCamera](#ga7bdcf1fb36c404d36e09ad70d2545d92) \*\*outCamera)

 | 

Obtains the camera parameter object of the current frame.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARFrame\_AcquireCameraImage](#gad5619c3cbd2b9ea0cfeff22b72f8d81d) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARFrame](#gaf35f728a1179ef54a3eba9f1cf021719) \*frame, [AREngine\_ARImage](#gabfee13b0076f2f00b7efdef2717add59) \*\*outImage)

 | 

Obtains the image of the current frame of the camera.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARFrame\_AcquireCameraPhotoImage](#section18751333994)(const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARFrame](#gaf35f728a1179ef54a3eba9f1cf021719)\*frame, [HMS\_AREngine\_PhotoAvailableCallback](#section430673420224) photoCallback)

 | 

Obtains the photo stream image of the current frame.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARFrame\_AcquireDepthConfidenceImage](#section4424501286) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARFrame](#gaf35f728a1179ef54a3eba9f1cf021719) \*frame, [AREngine\_ARImage](#gabfee13b0076f2f00b7efdef2717add59) \*\*outConfidenceImage)

 | 

Obtains the depth confidence map of the current frame.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARFrame\_AcquireDepthImage16Bits](#section138574584154) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARFrame](#gaf35f728a1179ef54a3eba9f1cf021719) \*frame, [AREngine\_ARImage](#gabfee13b0076f2f00b7efdef2717add59) \*\*outDepthImage);

 | 

Obtains the depth image of the current frame.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARFrame\_AcquirePointCloud](#ga877f7fc9d9c303f1fd8efb00ec383b34) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARFrame](#gaf35f728a1179ef54a3eba9f1cf021719) \*frame, [AREngine\_ARPointCloud](#gacc054cea4851be61b160f32b433737fc) \*\*outPointCloud)

 | 

Returns the point cloud data of the current frame.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARFrame\_AcquireSceneMesh](#section25711548111020) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARFrame](#gaf35f728a1179ef54a3eba9f1cf021719) \*frame, [AREngine\_ARSceneMesh](#section543212520614) \*\*outSceneMesh)

 | 

Obtains the mesh information of the current frame.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARFrame\_AcquireSemanticDenseData](#section17136162216547) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARFrame](#gaf35f728a1179ef54a3eba9f1cf021719) \*frame, [AREngine\_ARSemanticDenseData](#section1410813229144) \*\*outSemanticDenseData);

 | 

Obtains the high-precision geometric reconstruction object data of the current frame.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARFrame\_Create](#gadfcb9589137a39c5afcb217e18853a9d) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, [AREngine\_ARFrame](#gaf35f728a1179ef54a3eba9f1cf021719) \*\*outFrame)

 | 

Creates an [AREngine\_ARFrame](#gaf35f728a1179ef54a3eba9f1cf021719) object and stores the pointer in _\*_**outFrame**.

 |
| 

void [HMS\_AREngine\_ARFrame\_Destroy](#ga0ca6a470025dbccb44b4fdefc26513f6) ([AREngine\_ARFrame](#gaf35f728a1179ef54a3eba9f1cf021719) \*frame)

 | 

Deletes the current [AREngine\_ARFrame](#gaf35f728a1179ef54a3eba9f1cf021719) object.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARFrame\_GetDisplayGeometryChanged](#ga4fb55932c19ef9c49523a0a5385a9242) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARFrame](#gaf35f728a1179ef54a3eba9f1cf021719) \*frame, int32\_t \*outGeometryChangeState)

 | 

Obtains whether the display (length, width, and rotation) changes.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARFrame\_GetTimestamp](#ga266c2e5c80a961163d3422b96b079701) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARFrame](#gaf35f728a1179ef54a3eba9f1cf021719) \*frame, int64\_t \*outTimestampNs)

 | 

Obtains the timestamp information (in nanoseconds) of the current frame.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARFrame\_GetUpdatedTrackables](#ga0fc74148f836093108b85ab4c7ecdd1c) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARFrame](#gaf35f728a1179ef54a3eba9f1cf021719) \*frame, [AREngine\_ARTrackableType](#ga993948a19fd2bdfa5b946e13a8d4fe3d) filterType, [AREngine\_ARTrackableList](#gae69e4963b595036fc5e6119a055bb205) \*outTrackableList)

 | 

Obtains the updated trackable object of the specified type after [HMS\_AREngine\_ARSession\_Update](#ga1d1cacf372a8011a439f0e4e76994259) is called.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARFrame\_HitTest](#gad9377f19261d5bbc2044497729b4e0df) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARFrame](#gaf35f728a1179ef54a3eba9f1cf021719) \*frame, float pixelX, float pixelY, [AREngine\_ARHitResultList](#ga1f2369453412bd4d77ab8f5aa2d52bb3) \*hitResultList)

 | 

Casts a ray from the camera, with the direction of the ray determined by the points (**pixelX**, **pixelY**) in the preview area. **pixelX** and **pixelY** can be obtained through the XComponent's [DispatchTouchEvent](../../../../../application-framework/arkui/c-api/structs/oh-nativexcomponent-callback/document.md#dispatchtouchevent) event.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARFrame\_TransformDisplayUvCoords](#ga4c7699abab9b82369c0d42b496667fc7) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARFrame](#gaf35f728a1179ef54a3eba9f1cf021719) \*frame, int32\_t elementSize, const float \*uvsIn, float \*uvsOut)

 | 

Converts the texture coordinates so that the background image captured by the camera can be correctly displayed.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARHitResult\_AcquireNewAnchor](#ga30abe7b3457c991815dd79fcfaf26018) ([AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, [AREngine\_ARHitResult](#gaeb304c8b21122eb7ffda7403316a3507) \*hitResult, [AREngine\_ARAnchor](#ga76c16c9d68ba9a3b76f1869c60d8ca1d) \*\*outAnchor)

 | 

Creates an anchor at the hit position.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARHitResult\_AcquireTrackable](#gac3a02e30bb7706d87c4c29d38b363840) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARHitResult](#gaeb304c8b21122eb7ffda7403316a3507) \*hitResult, [AREngine\_ARTrackable](#ga54808ebd1a6ed026494acdd945c4f970) \*\*outTrackable)

 | 

Obtains the trackable object that is hit.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARHitResult\_Create](#ga4b06bcca0f6fc0b081ef8210765d9c91) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, [AREngine\_ARHitResult](#gaeb304c8b21122eb7ffda7403316a3507) \*\*outHitResult)

 | 

Creates an empty hit testing result object.

 |
| 

void [HMS\_AREngine\_ARHitResult\_Destroy](#ga3b3796d7186cb09c4861ebabe2d5b654) ([AREngine\_ARHitResult](#gaeb304c8b21122eb7ffda7403316a3507) \*hitResult)

 | 

Releases the memory used by the hit testing result object.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARHitResult\_GetDistance](#ga6929e52bb352622806d2298497c6b4c8) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARHitResult](#gaeb304c8b21122eb7ffda7403316a3507) \*hitResult, float \*outDistance)

 | 

Returns the distance from the camera to the hit location, in meters.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARHitResult\_GetHitPose](#ga8beaa085410712425041e81f9bc6aa09) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARHitResult](#gaeb304c8b21122eb7ffda7403316a3507) \*hitResult, [AREngine\_ARPose](#gab2fa63142ebfb09f0c2ddf88cdb86604) \*outPose)

 | 

Obtains the pose of an intersection.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARHitResultList\_Create](#gad5dfe929e7952954764d05b8d69abace) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, [AREngine\_ARHitResultList](#ga1f2369453412bd4d77ab8f5aa2d52bb3) \*\*outHitResultList)

 | 

Creates a list of hit testing result objects.

 |
| 

void [HMS\_AREngine\_ARHitResultList\_Destroy](#gaae065ef9a28168b420c96b72ca80c892) ([AREngine\_ARHitResultList](#ga1f2369453412bd4d77ab8f5aa2d52bb3) \*hitResultList)

 | 

Releases the list of hit testing result objects, as well as all hit testing result objects in the list.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARHitResultList\_GetItem](#gaf165c7a1c9ae003cac2a1c2ac2e5e5c4) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARHitResultList](#ga1f2369453412bd4d77ab8f5aa2d52bb3) \*hitResultList, int32\_t index, [AREngine\_ARHitResult](#gaeb304c8b21122eb7ffda7403316a3507) \*outHitResult)

 | 

Obtains the hit testing result object at a specific index from the list of hit testing results.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARHitResultList\_GetSize](#ga131d081663d457c594664c977bd9033c) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARHitResultList](#ga1f2369453412bd4d77ab8f5aa2d52bb3) \*hitResultList, int32\_t \*outSize)

 | 

Obtains the number of objects in the list of hit testing result objects.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARImage\_GetFormat](#ga852b211c7e285ccc154295eb1c604f37) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARImage](#gabfee13b0076f2f00b7efdef2717add59) \*image, [AREngine\_ARImageFormat](#gadfcf7a1211ed12a90f377610d0f838ac) \*outFormat)

 | 

Obtains the image format of the current frame.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARImage\_GetHeight](#ga34c21703e40868ce0fe5795fa82a08fa) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARImage](#gabfee13b0076f2f00b7efdef2717add59) \*image, int32\_t \*outHeight)

 | 

Obtains the image height of the current frame.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARImage\_GetWidth](#ga2c2454e9611dc68e26b8fefb39021597) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARImage](#gabfee13b0076f2f00b7efdef2717add59) \*image, int32\_t \*outWidth)

 | 

Obtains the image width of the current frame.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARImage\_GetNativeBuffer](#section367418528228) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARImage](#gabfee13b0076f2f00b7efdef2717add59) \*image, [OH\_NativeBuffer](../../../../arkgraphics-2d/c-apis/modules/oh-nativebuffer/document.md) \*\*outNativeBuffer);

 | 

Obtains the NativeBuffer data of the current frame's image object.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARImage\_GetPlaneCount](#ga107fbf6737b499aea941fbbfeab1b3e9) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARImage](#gabfee13b0076f2f00b7efdef2717add59) \*image, int32\_t \*outCount)

 | 

Obtains the number of planes in the current frame.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARImage\_GetPlaneData](#gaedc5247eb982443c3f8a2dc8cfd5fdee) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARImage](#gabfee13b0076f2f00b7efdef2717add59) \*image, int32\_t planeIndex, const uint8\_t \*\*outData, int32\_t \*outLength)

 | 

Obtains the plane data in the current frame.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARImage\_GetPlanePixelStride](#gac31f741115e6936f7b8e3ef94579d270) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARImage](#gabfee13b0076f2f00b7efdef2717add59) \*image, int32\_t planeIndex, int32\_t \*outPixelStride)

 | 

Obtains the distance between the start points of two consecutive pixels in an image, in bytes. The pixel stride is always greater than 0.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARImage\_GetPlaneRowStride](#ga35e66d4a869539d2261e41df17730691) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARImage](#gabfee13b0076f2f00b7efdef2717add59) \*image, int32\_t planeIndex, int32\_t \*outRowStride)

 | 

Obtains the number of bytes between the start positions of two consecutive pixel lines in an image. The line spacing is always greater than 0.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARImage\_GetTimestamp](#ga7d2c7f1d596d41bfe1c181057283b740) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARImage](#gabfee13b0076f2f00b7efdef2717add59) \*image, int64\_t \*outTimestamp)

 | 

Obtains the timestamp of an image.

 |
| 

void [HMS\_AREngine\_ARImage\_Release](#ga42fd222576edf6507f6d319a3374cd94) ([AREngine\_ARImage](#gabfee13b0076f2f00b7efdef2717add59) \*image)

 | 

Releases the image object of the current frame, that is, the object created by [HMS\_AREngine\_ARFrame\_AcquireCameraImage](#gad5619c3cbd2b9ea0cfeff22b72f8d81d).

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARPlane\_AcquireSubsumedBy](#ga56686d6a5ff45fcb04812538aa807ac3) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARPlane](#ga76f9bdb23634312b8488fcbaff4aa9b5) \*plane, [AREngine\_ARPlane](#ga76f9bdb23634312b8488fcbaff4aa9b5) \*\*outSubsumedBy)

 | 

Obtains the parent plane of a plane (a parent plane is generated when a plane is merged with another one). If there is no parent plane, **NULL** is returned.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARPlane\_GetCenterPose](#gabbb03027afb984be8542d00d2eebd063) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARPlane](#ga76f9bdb23634312b8488fcbaff4aa9b5) \*plane, [AREngine\_ARPose](#gab2fa63142ebfb09f0c2ddf88cdb86604) \*outPose)

 | 

Obtains the pose information for the conversion from the local coordinate system of a plane to the world coordinate system.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARPlane\_GetExtentX](#ga49db45eb6072384247a057c403a69c8d) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARPlane](#ga76f9bdb23634312b8488fcbaff4aa9b5) \*plane, float \*outExtentX)

 | 

Obtains the length of the plane's bounding rectangle along the X axis of the plane's local coordinate system, such as the width of the rectangle.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARPlane\_GetExtentZ](#ga4daf6a365f1107f146c5d264dfee292c) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARPlane](#ga76f9bdb23634312b8488fcbaff4aa9b5) \*plane, float \*outExtentZ)

 | 

Obtains the length of the plane's bounding rectangle along the Z axis of the plane's local coordinate system, such as the height of the rectangle.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARPlane\_GetLabel](#ga913456f9586c82adcdbcae291ec8e17c) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARPlane](#ga76f9bdb23634312b8488fcbaff4aa9b5) \*plane, [AREngine\_ARSemanticPlaneLabel](#gafbb6b69fefdc417ba6437ce2fe587cb1) \*label)

 | 

Obtains the semantic type of a plane, such as desktop and floor.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARPlane\_GetPolygon](#ga3537ce62e6a92dcdbddff0f39de0fae3) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARPlane](#ga76f9bdb23634312b8488fcbaff4aa9b5) \*plane, float \*outPolygonXz, int32\_t polygonSize)

 | 

Obtains the 2D vertex array of the detected plane, in the format of \[x1, z1, x2, z2, ...\].

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARPlane\_GetPolygonSize](#ga98760556eee2a4a69c33699b7ce3edc6) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARPlane](#ga76f9bdb23634312b8488fcbaff4aa9b5) \*plane, int32\_t \*outPolygonSize)

 | 

Obtains the size of the 2D vertex array of the detected plane.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARPlane\_GetType](#ga8aa35ca398b38eee8c53bd1db8d6ab88) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARPlane](#ga76f9bdb23634312b8488fcbaff4aa9b5) \*plane, [AREngine\_ARPlaneType](#ga895db37a92155584c5448bee30a8beab) \*outPlaneType)

 | 

Obtains the plane type.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARPlane\_IsPoseInExtents](#ga8ded2552569a9e89c1befe8f15123af6) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARPlane](#ga76f9bdb23634312b8488fcbaff4aa9b5) \*plane, const [AREngine\_ARPose](#gab2fa63142ebfb09f0c2ddf88cdb86604) \*pose, int32\_t \*outPoseInExtents)

 | 

Checks whether a pose is within the plane's bounding rectangle.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARPlane\_IsPoseInPolygon](#gab00d22a9c927a2745821023e8e72a8d0) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARPlane](#ga76f9bdb23634312b8488fcbaff4aa9b5) \*plane, const [AREngine\_ARPose](#gab2fa63142ebfb09f0c2ddf88cdb86604) \*pose, int32\_t \*outPoseInPolygon)

 | 

Checks whether a pose is within the plane's bounding polygon.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARPoint\_GetOrientationMode](#gad869ed2a4ac6409bf94c768d9d1d8127) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARPoint](#gac7b6923d92487d68e77543dd223364d6) \*point, [AREngine\_ARPointOrientationMode](#ga0e2893593f4372954fd97519e0a63855) \*outOrientationMode)

 | 

Obtains the orientation mode of an input point.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARPoint\_GetPose](#ga8255eece88d8dc76c554eed360fb7c7b) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARPoint](#gac7b6923d92487d68e77543dd223364d6) \*point, [AREngine\_ARPose](#gab2fa63142ebfb09f0c2ddf88cdb86604) \*outPose)

 | 

Obtains the pose information of an input point.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARPointCloud\_GetData](#ga4061cacb3f3ce45e529acb9afbcdc5ce) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARPointCloud](#gacc054cea4851be61b160f32b433737fc) \*pointCloud, const float \*\*outPointCloudData)

 | 

Obtains the coordinates of all points in a point cloud, as well as their confidence array.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARPointCloud\_GetNumberOfPoints](#gad9701fe82b6468f33f6741cc7f347d45) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARPointCloud](#gacc054cea4851be61b160f32b433737fc) \*pointCloud, int32\_t \*outNumberOfPoints)

 | 

Obtains the coordinates of all points in a point cloud, as well as their confidence array size.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARPointCloud\_GetTimestamp](#ga9e430d52fa372903bcbe40ca5f6a9d9d) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARPointCloud](#gacc054cea4851be61b160f32b433737fc) \*pointCloud, int64\_t \*outTimestampNs)

 | 

Obtains the timestamp when the current feature point cloud is detected, in nanoseconds.

 |
| 

void [HMS\_AREngine\_ARPointCloud\_Release](#ga3751c56632f7f6d383cf9409ec6769bc) ([AREngine\_ARPointCloud](#gacc054cea4851be61b160f32b433737fc) \*pointCloud)

 | 

Releases the memory used by the point cloud object.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARPose\_Create](#gafb471f39563ca1a4947d4f87c77e24e2) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, const float \*poseRaw, const uint32\_t poseRawSize, [AREngine\_ARPose](#gab2fa63142ebfb09f0c2ddf88cdb86604) \*\*outPose)

 | 

Allocates and initializes a new pose object.

 |
| 

void [HMS\_AREngine\_ARPose\_Destroy](#gab988254f4654c8aaadb5740061846057) ([AREngine\_ARPose](#gab2fa63142ebfb09f0c2ddf88cdb86604) \*pose)

 | 

Releases the memory used by the pose object.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARPose\_GetMatrix](#ga787f4daf9efd13c79737ef18cef6d7c7) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARPose](#gab2fa63142ebfb09f0c2ddf88cdb86604) \*pose, float \*outMatrixColMajor4x4, int32\_t matrixColMajor4x4Size)

 | 

Converts the pose data into a 4 × 4 matrix.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARPose\_GetPoseRaw](#ga1ee66c006ffe8255cc04f2a24c277709) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARPose](#gab2fa63142ebfb09f0c2ddf88cdb86604) \*pose, float \*outPoseRaw, int32\_t poseRawSize)

 | 

Extracts pose data from a pose object.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARSceneMesh\_AcquireIndexList](#section7629354145) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARSceneMesh](#section543212520614) \*sceneMesh, int32\_t \*outData, int32\_t dataSize)

 | 

Obtains the index set of mesh faces.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARSceneMesh\_AcquireIndexListSize](#section12621161917152) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARSceneMesh](#section543212520614) \*sceneMesh, int32\_t \*outSize)

 | 

Obtains the number of indexes of the mesh faces.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARSceneMesh\_AcquireVertexList](#section2126723166) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARSceneMesh](#section543212520614) \*sceneMesh, float \*outData, int32\_t dataSize)

 | 

Obtains the vertex set of a mesh.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARSceneMesh\_AcquireVertexNormalList](#section115249588168) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARSceneMesh](#section543212520614) \*sceneMesh, float \*outData, int32\_t dataSize)

 | 

Obtains the normal vector set of the mesh faces.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARSceneMesh\_AcquireVerticesSize](#section1860218429179) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARSceneMesh](#section543212520614) \*sceneMesh, int32\_t \*outSize)

 | 

Obtains the number of vertices of a mesh.

 |
| 

void [HMS\_AREngine\_ARSceneMesh\_Release](#section446832931813) ([AREngine\_ARSceneMesh](#section543212520614) \*SceneMesh)

 | 

Releases the mesh information of the current frame.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARSemanticDense\_AcquireCubeData](#section7554459949) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARSemanticDenseData](#section1410813229144) \*semanticDenseData, [AREngine\_ARSemanticDenseCubeData](../../header-files-and-structs/structs/arengine-arsemanticdensecubedata/document.md) \*\*outCubeData)

 | 

Obtains the cube data from the recognized high-precision geometric reconstruction object data.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARSemanticDense\_AcquireCubeDataSize](#section383013458212) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARSemanticDenseData](#section1410813229144) \*semanticDenseData, int64\_t \*outSize)

 | 

Obtains the cube count from the recognized high-precision geometric reconstruction object data.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARSemanticDense\_AcquirePointData](#section288942515910) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARSemanticDenseData](#section1410813229144) \*semanticDenseData, [AREngine\_ARSemanticDensePointData](../../header-files-and-structs/structs/arengine-arsemanticdensepointdata/document.md) \*\*outPointData)

 | 

Obtains the dense point cloud data from the recognized high-precision geometric reconstruction object data.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARSemanticDense\_AcquirePointDataSize](#section6669112114532) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARSemanticDenseData](#section1410813229144) \*semanticDenseData, int64\_t \*outSize)

 | 

Obtains the dense point cloud size from the recognized high-precision geometric reconstruction object data.

 |
| 

void [HMS\_AREngine\_ARSemanticDense\_Release](#section390280482) ([AREngine\_ARSemanticDenseData](#section1410813229144) \*semanticDenseData)

 | 

Releases a high-precision geometric reconstruction object.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARSession\_AcquireNewAnchor](#ga2ae6dee4baab7cf2c5d0cdd1c845cf0c) ([AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARPose](#gab2fa63142ebfb09f0c2ddf88cdb86604) \*pose, [AREngine\_ARAnchor](#ga76c16c9d68ba9a3b76f1869c60d8ca1d) \*\*outAnchor)

 | 

Creates an anchor for continuous tracking.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARSession\_Configure](#ga6394ae995148abbe3d00082817bf320a) ([AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARConfig](#gab0b32ef6018535fd30000f4b6d65f619) \*config)

 | 

Configures an [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) session.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARSession\_Create](#ga47713cb18234569e03b5216b6c8442d3) (void \*env, void \*applicationContext, [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*\*outSessionPointer)

 | 

Creates an [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) session.

 |
| 

void [HMS\_AREngine\_ARSession\_Destroy](#ga3a2be9998c9cd6373ff1f5209b645a95) ([AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session)

 | 

Releases the resources used by the [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) session.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARSession\_GetCameraConfig](#ga31b28b049ac25b94c02fb27ca56c497d) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, [AREngine\_ARCameraConfig](#ga9b7a5a2082a4127f85a1c9a95cb9acba) \*outCameraConfig)

 | 

Obtains the camera configuration information.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARSession\_GetAllAnchors](#ga4828823e5f3cc1067dbd6a2c8b9c9635) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, [AREngine\_ARAnchorList](#ga516a7f0954dcfda438799aa9e7c6e872) \*outAnchorList)

 | 

Obtains all anchors, including anchors in all states contained in [AREngine\_ARTrackingState](#gaae57d2f58331e1033b60cdb2d506a382).

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARSession\_GetAllTrackables](#gac5b39338f95317671d8de6d4f409cf9c) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, [AREngine\_ARTrackableType](#ga993948a19fd2bdfa5b946e13a8d4fe3d) filterType, [AREngine\_ARTrackableList](#gae69e4963b595036fc5e6119a055bb205) \*outTrackableList)

 | 

Obtains the list of all trackable objects of the specified type.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARSession\_Pause](#ga09dedb5c633141321591db0981629de1) ([AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session)

 | 

Pauses the session, stops the camera preview stream, and releases the camera (otherwise, other apps will not be able to use the camera service), without clearing the plane and anchor data.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARSession\_Resume](#ga7138d56b767738b8aadcbc74f4c328db) ([AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session)

 | 

Starts [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650), or restores [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) after [HMS\_AREngine\_ARSession\_Pause](#ga09dedb5c633141321591db0981629de1) is called.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARSession\_SetCameraGLTexture](#gac697e4be36db63ed6098f154aa9ac01c) ([AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, uint32\_t textureId)

 | 

Sets the OpenGL texture for storing the camera preview stream data.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARSession\_SetDisplayGeometry](#ga3f23bf747def8303c3fb261a9e9a2286) ([AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, [AREngine\_ARPoseType](#gae551da7b220b8b38140c3c28882e5010) rotation, int32\_t width, int32\_t height)

 | 

Sets the display height and width (in pixels).

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARSession\_Stop](#ga0b7405ae0fc1e1257103192a2b7b48d3) ([AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session)

 | 

Stops AR Engine and the camera preview stream, clears the plane and anchor data, releases the camera, and terminates the session.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARSession\_Update](#ga1d1cacf372a8011a439f0e4e76994259) ([AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, [AREngine\_ARFrame](#gaf35f728a1179ef54a3eba9f1cf021719) \*outFrame)

 | 

Updates the computation result of AR Engine.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARTarget\_GetAxisAlignedBoundingBox](#gaaf54fe7a3c38dbb4c0bcaa3c83dd0d76)(const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARTarget](#ga9af9c1d51ed065f80b373824e0425fa0) \*target, float \*outAabb, int32\_t aabbSize)

 | 

Obtains the coordinates of the minimum bounding box of a semantic object, in the format of (xmin, ymin, zmin, xmax, ymax, zmax).

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARTarget\_GetCenterPose](#gaa9a304640d54942be238a7ddd2c13276) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARTarget](#ga9af9c1d51ed065f80b373824e0425fa0) \*target, [AREngine\_ARPose](#gab2fa63142ebfb09f0c2ddf88cdb86604) \*outARPose)

 | 

Obtains the pose object for the conversion from the local coordinate system of the target semantic object to the world coordinate system.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARTarget\_GetRadius](#ga0fb23a8217c7191f765b0d656160ffa1) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARTarget](#ga9af9c1d51ed065f80b373824e0425fa0) \*target, float \*radius)

 | 

Obtains the sphere radius of a semantic object.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARTarget\_GetShapeType](#ga6c702efd6c4fdc3eeb8f5dc38968ec65) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARTarget](#ga9af9c1d51ed065f80b373824e0425fa0) \*target, [AREngine\_ARTargetShapeLabel](#gaed68dc13cc314da98d79c88b12d3ae49) \*shape)

 | 

Obtains the shape type of a semantic object.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARTrackable\_AcquireNewAnchor](#gacf03897f0ac28d338143f3fa350c1491) ([AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, [AREngine\_ARTrackable](#ga54808ebd1a6ed026494acdd945c4f970) \*trackable, [AREngine\_ARPose](#gab2fa63142ebfb09f0c2ddf88cdb86604) \*pose, [AREngine\_ARAnchor](#ga76c16c9d68ba9a3b76f1869c60d8ca1d) \*\*outAnchor)

 | 

Creates an anchor object using the pose information of the trackable object. This anchor will be bound to the current trackable object.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARTrackable\_GetAnchors](#gac7a3b98b0281f2e31ac3d9c47b0dffab) ([AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARTrackable](#ga54808ebd1a6ed026494acdd945c4f970) \*trackable, [AREngine\_ARAnchorList](#ga516a7f0954dcfda438799aa9e7c6e872) \*outAnchorList)

 | 

Obtains a list of anchor objects bound to the input trackable objects.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARTrackable\_GetTrackingState](#ga7805739b2dbeae0d3b04242538a4a840) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARTrackable](#ga54808ebd1a6ed026494acdd945c4f970) \*trackable, [AREngine\_ARTrackingState](#gaae57d2f58331e1033b60cdb2d506a382) \*outTrackingState)

 | 

Obtains the tracking state of the current trackable object.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARTrackable\_GetType](#ga72c800291d0df799fa795db3d3485e4f) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARTrackable](#ga54808ebd1a6ed026494acdd945c4f970) \*trackable, [AREngine\_ARTrackableType](#ga993948a19fd2bdfa5b946e13a8d4fe3d) \*outTrackableType)

 | 

Obtains the type of a trackable object.

 |
| 

void [HMS\_AREngine\_ARTrackable\_Release](#ga6ec735cd18e955442f29416ff58ddd64) ([AREngine\_ARTrackable](#ga54808ebd1a6ed026494acdd945c4f970) \*trackable)

 | 

Releases a trackable object.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARTrackableList\_AcquireItem](#gab1782eeeeddc01b77a140af915cb351c) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARTrackableList](#gae69e4963b595036fc5e6119a055bb205) \*trackableList, int32\_t index, [AREngine\_ARTrackable](#ga54808ebd1a6ed026494acdd945c4f970) \*\*outTrackable)

 | 

Obtains the object at a specific index from the trackable object list.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARTrackableList\_Create](#ga7860d63545ab862e9f3b1fe0a8a83d42) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, [AREngine\_ARTrackableList](#gae69e4963b595036fc5e6119a055bb205) \*\*outTrackableList)

 | 

Creates a list of trackable objects.

 |
| 

void [HMS\_AREngine\_ARTrackableList\_Destroy](#gad6e2ffd71d7cdaa3ae553937437b37c8) ([AREngine\_ARTrackableList](#gae69e4963b595036fc5e6119a055bb205) \*trackableList)

 | 

Releases the list of trackable objects, along with all the anchor references it holds.

 |
| 

[AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARTrackableList\_GetSize](#gad9729d4436f3d969286f31b33d07513e) (const [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARTrackableList](#gae69e4963b595036fc5e6119a055bb205) \*trackableList, int32\_t \*outSize)

 | 

Obtains the number of trackable objects in the list.

 |

#### Macro Description

#### \[h2\]ARENGINE\_AABB\_POINT\_SIZE

const static int32\_t ARENGINE\_AABB\_POINT\_SIZE = 6

**Description**

Size of the bounding box coordinate array.

**Start version**: 5.0.0(12)

#### \[h2\]ARENGINE\_DISTORTION\_COUNT

const static int32\_t ARENGINE\_DISTORTION\_COUNT = 5

**Description**

Number of camera distortion parameters.

**Start version**: 5.0.0(12)

#### \[h2\]ARENGINE\_POSE\_RAW\_SIZE

const static int32\_t ARENGINE\_POSE\_RAW\_SIZE = 7

**Description**

Size of the pose data array.

**Start version**: 5.0.0(12)

#### \[h2\]ARENGINE\_VIEW\_MATRIX\_SIZE

const static int32\_t ARENGINE\_VIEW\_MATRIX\_SIZE = 16

**Description**

Size of the transformation matrix array.

**Start version**: 5.0.0(12)

#### Type Description

#### \[h2\]AREngine\_ARAnchor

typedef struct AREngine\_ARAnchor AREngine\_ARAnchor

**Description**

Anchor object.

Defines the spatial location associated with a trackable object.

**Start version**: 5.0.0(12)

#### \[h2\]AREngine\_ARAnchorList

typedef struct AREngine\_ARAnchorList AREngine\_ARAnchorList

**Description**

Anchor object list.

Contains a series of anchor objects.

**Start version**: 5.0.0(12)

#### \[h2\]AREngine\_ARAugmentedImage

typedef struct AREngine\_ARAugmentedImage AREngine\_ARAugmentedImage

**Description**

Trackable image object.

**Start version**: 5.1.0(18)

#### \[h2\]AREngine\_ARAugmentedImageDatabase

typedef struct AREngine\_ARAugmentedImageDatabase AREngine\_ARAugmentedImageDatabase

**Description**

Trackable image database object.

**Start version**: 5.1.0(18)

#### \[h2\]AREngine\_ARCamera

typedef struct AREngine\_ARCamera AREngine\_ARCamera

**Description**

Camera information for the current frame.

**Start version**: 5.0.0(12)

#### \[h2\]AREngine\_ARCameraConfig

typedef struct AREngine\_ARCameraConfig AREngine\_ARCameraConfig

**Description**

Camera configuration information.

Example: dimensions of the CPU image and GPU texture.

**Start version**: 5.0.0(12)

#### \[h2\]AREngine\_ARCameraIntrinsics

typedef struct AREngine\_ARCameraIntrinsics AREngine\_ARCameraIntrinsics

**Description**

Intrinsic camera parameters.

Includes **fx**, **fy**, **cx**, **cy**, and camera distortion parameters.

**Start version**: 5.0.0(12)

#### \[h2\]AREngine\_ARConfig

typedef struct AREngine\_ARConfig AREngine\_ARConfig

**Description**

Used for configuring [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) capabilities (that is, capabilities and modes to use).

**Start version**: 5.0.0(12)

#### \[h2\]AREngine\_ARFrame

typedef struct AREngine\_ARFrame AREngine\_ARFrame

**Description**

A frame of data processed by AR Engine.

**Start version**: 5.0.0(12)

#### \[h2\]AREngine\_ARHitResult

typedef struct AREngine\_ARHitResult AREngine\_ARHitResult

**Description**

Hit testing result object.

Describes the hit testing result of a single trackable object.

**Start version**: 5.0.0(12)

#### \[h2\]AREngine\_ARHitResultList

typedef struct AREngine\_ARHitResultList AREngine\_ARHitResultList

**Description**

Hit testing result list.

Contains a series of hit testing results.

**Start version**: 5.0.0(12)

#### \[h2\]AREngine\_ARImage

typedef struct AREngine\_ARImage AREngine\_ARImage

**Description**

Camera video stream frame object.

**Start version**: 5.0.0(12)

#### \[h2\]AREngine\_ARPlane

typedef struct AREngine\_ARPlane AREngine\_ARPlane

**Description**

Plane object.

Describes the detected trackable plane information.

**Start version**: 5.0.0(12)

#### \[h2\]AREngine\_ARPoint

typedef struct AREngine\_ARPoint AREngine\_ARPoint

**Description**

Point object.

Describes the detected trackable point data.

**Start version**: 5.0.0(12)

#### \[h2\]AREngine\_ARPointCloud

typedef struct AREngine\_ARPointCloud AREngine\_ARPointCloud

**Description**

Collection of trackable 3D point clouds.

**Start version**: 5.0.0(12)

#### \[h2\]AREngine\_ARPose

typedef struct AREngine\_ARPose AREngine\_ARPose

**Description**

Pose object.

Defines an immutable rigidbody transformation from one coordinate system to another, for example, translation or rotation.

For details, please refer to [en-us\_topic\_0000002500426084.html#EN-US\_TOPIC\_0000002500426084\_\_section134071231142820](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arengine-c-get-pose#section134071231142820).

**Start version**: 5.0.0(12)

#### \[h2\]AREngine\_ARSceneMesh

typedef struct AREngine\_ARSceneMesh AREngine\_ARSceneMesh

**Description**

Environment mesh data set.

**Start version**: 5.1.0(18)

#### \[h2\]AREngine\_ARSemanticDenseData

typedef struct AREngine\_ARSemanticDenseData AREngine\_ARSemanticDenseData

**Description**

High-precision geometric reconstruction object data set.

**Start version**: 6.0.0(20)

#### \[h2\]AREngine\_ARSession

typedef struct AREngine\_ARSession AREngine\_ARSession

**Description**

Used to manage the system status of AR Engine.

**Start version**: 5.0.0(12)

#### \[h2\]AREngine\_ARTarget

typedef struct AREngine\_ARTarget AREngine\_ARTarget

**Description**

Object.

Describes the detected trackable semantic object information, such as a semantic plane.

**Start version**: 5.0.0(12)

#### \[h2\]AREngine\_ARTrackable

typedef struct AREngine\_ARTrackable AREngine\_ARTrackable

**Description**

Trackable object, such as a point or a plane.

After obtaining the object, if you need to obtain the center point position of the plane (by calling [HMS\_AREngine\_ARPlane\_GetCenterPose](#gabbb03027afb984be8542d00d2eebd063)), obtain the pose information of the point (by calling [HMS\_AREngine\_ARPoint\_GetPose](#ga8255eece88d8dc76c554eed360fb7c7b)), or perform any other operations on this object, convert this object into another one (such as [AREngine\_ARPlane](#ga76f9bdb23634312b8488fcbaff4aa9b5) or [AREngine\_ARPoint](#gac7b6923d92487d68e77543dd223364d6)) according to the type of this trackable object (obtained through [HMS\_AREngine\_ARTrackable\_GetType](#ga72c800291d0df799fa795db3d3485e4f)), by referring to [AREngine\_ARPlane](#ga76f9bdb23634312b8488fcbaff4aa9b5) \*arPlane = reinterpret\_cast<[AREngine\_ARPlane](#ga76f9bdb23634312b8488fcbaff4aa9b5) \*>(trackable).

**Start version**: 5.0.0(12)

#### \[h2\]AREngine\_ARTrackableList

typedef struct AREngine\_ARTrackableList AREngine\_ARTrackableList

**Description**

Trackable object list.

**Start version**: 5.0.0(12)

#### \[h2\]HMS\_AREngine\_PhotoAvailableCallback

typedef void (\*HMS\_AREngine\_PhotoAvailableCallback)(OH\_NativeBuffer \*photoBuffer)

**Description**

Callback triggered when a photo stream image is output.

**Start version**: 6.0.2(22)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

photoBuffer

 | 

Image data of the photo stream.

 |

#### Enum Description

#### \[h2\]AREngine\_ARAddAugmentedImageReason

enum AREngine\_ARAddAugmentedImageReason

**Description**

Possible cause of the tracking failure.

**Start version**: 5.1.0(18)

| 
Enumerated Value

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_ADD\_AUGMENTED\_IMAGE\_REASON\_NONE

 | 

The added image meets the quality requirements.

 |
| 

ARENGINE\_ADD\_AUGMENTED\_IMAGE\_REASON\_SIZE\_NOT\_MATCH

 | 

Attempts are made to add an image with insufficient quality (dimensions do not match) to the image database.

NOTE:

The image dimensions are evaluated from the aspect ratio and resolution. It is recommended that the image aspect ratio and resolution have a minimum rating of **Fit**.

 |
| 

ARENGINE\_ADD\_AUGMENTED\_IMAGE\_REASON\_LIGHT\_ANOMALY

 | 

Attempts are made to add an image with insufficient quality (too bright or too dark) to the image database.

 |
| 

ARENGINE\_ADD\_AUGMENTED\_IMAGE\_REASON\_FEATURE\_LIMIT

 | 

Attempts are made to add an image with insufficient quality (the image color is relatively simple) to the image database.

 |
| 

ARENGINE\_ADD\_AUGMENTED\_IMAGE\_REASON\_OTHER

 | 

Attempts are made to add poor quality (other scenarios, such as reflection, light spot, and repetitive content) to the image database.

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
    

#### \[h2\]AREngine\_ARConfidenceLevel

enum AREngine\_ARConfidenceLevel

**Description**

Depth confidence.

**Start version**: 5.0.5(17)

| 
Enumerated Value

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_DEPTH\_CONFIDENCE\_LOW

 | 

The confidence of the depth image is low.

 |
| 

ARENGINE\_DEPTH\_CONFIDENCE\_MEDIUM

 | 

The confidence of the depth image is medium.

 |
| 

ARENGINE\_DEPTH\_CONFIDENCE\_HIGH

 | 

The confidence of the depth image is high.

 |

#### \[h2\]AREngine\_ARDepthMode

enum AREngine\_ARDepthMode

**Description**

Depth mode.

**Start version**: 5.0.5(17)

| 
Enumerated Value

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_DEPTH\_MODE\_DISABLED

 | 

No depth image information is provided.

 |
| 

ARENGINE\_DEPTH\_MODE\_AUTOMATIC

 | 

AR Engine automatically attempts to obtain depth information from various depth sources.

NOTE:

Typically, there are two types of depth sources: motion algorithms and Time of Flight (ToF) sensors.

Currently, only motion algorithms are supported.

 |

#### \[h2\]AREngine\_ARFocusMode

enum AREngine\_ARFocusMode

**Description**

Focus mode.

**Start version**: 5.0.0(12)

| 
Enumerated Value

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_FOCUS\_MODE\_FIXED

 | 

Fixed focus mode.

 |
| 

ARENGINE\_FOCUS\_MODE\_AUTO

 | 

Auto focus mode.

 |

#### \[h2\]AREngine\_ARImageDatabaseMode

enum AREngine\_ARImageDatabaseMode

**Description**

Mode of adding images to the feature database for tracking.

**Start version**: 5.1.0(18)

| 
Enumerated Value

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_ADD\_NORMAL

 | 

Normal adding mode.

 |
| 

ARENGINE\_ADD\_AUTO

 | 

Cyclic deletion mode.

 |

#### \[h2\]AREngine\_ARImageFormat

enum AREngine\_ARImageFormat

**Description**

Image format.

**Start version**: 5.0.0(12)

| 
Enumerated Value

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_IMAGE\_UNKNOWN

 | 

Unknown image format.

 |
| 

ARENGINE\_IMAGE\_YUV\_420\_888

 | 

YUV\_420\_888 format, which is suitable for processing high-resolution image data.

 |
| 

ARENGINE\_IMAGE\_Y\_8

 | 

Y\_8 format, which is suitable for scenarios requiring lower precision or smaller storage for image data.

**Start version**: 5.0.5(17)

 |
| 

ARENGINE\_IMAGE\_Y\_16

 | 

Y\_16 format, which is suitable for scenarios requiring higher precision for image data.

**Start version**: 5.0.5(17)

 |

#### \[h2\]AREngine\_ARImageStreamMode

enum AREngine\_ARImageStreamMode

**Description**

Image data stream mode. By default, **ARENGINE\_IMAGE\_STREAM\_MODE\_PREVIEW** is used.

**Start version**: 6.0.2(22)

| 
Enumerated Value

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_IMAGE\_STREAM\_MODE\_PREVIEW

 | 

Preview stream mode. You can call the [HMS\_AREngine\_ARFrame\_AcquireCameraImage](#gad5619c3cbd2b9ea0cfeff22b72f8d81d) API to obtain the preview stream image.

 |
| 

ARENGINE\_IMAGE\_STREAM\_MODE\_PREVIEW\_AND\_PHOTO

 | 

Preview and photo stream mode. You can call the [HMS\_AREngine\_ARFrame\_AcquireCameraPhotoImage](#section18751333994) API to obtain the photo stream image.

 |

#### \[h2\]AREngine\_ARMeshMode

enum AREngine\_ARMeshMode

**Description**

Mesh enabling mode.

**Start version**: 5.1.0(18)

| 
Enumerated Value

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_MESH\_MODE\_DISABLED

 | 

Mesh mode disabled.

AR Engine does not process or display mesh data.

 |
| 

ARENGINE\_MESH\_MODE\_ENABLE

 | 

Mesh mode enabled.

AR Engine attempts to process or display mesh data.

 |

#### \[h2\]AREngine\_ARPlaneFindingMode

enum AREngine\_ARPlaneFindingMode

**Description**

Plane finding mode.

**Start version**: 5.0.0(12)

| 
Enumerated Value

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_PLANE\_FINDING\_MODE\_DISABLED

 | 

Disables the plane finding.

 |
| 

ARENGINE\_PLANE\_FINDING\_MODE\_HORIZONTAL

 | 

Detects only horizontal planes, such as floors and tables.

 |
| 

ARENGINE\_PLANE\_FINDING\_MODE\_VERTICAL

 | 

Detects only vertical planes, such as walls.

 |
| 

ARENGINE\_PLANE\_FINDING\_MODE\_HORIZONTAL\_AND\_VERTICAL

 | 

Detects both horizontal and vertical planes.

 |

#### \[h2\]AREngine\_ARPlaneType

enum AREngine\_ARPlaneType

**Description**

Plane type.

**Start version**: 5.0.0(12)

| 
Enumerated Value

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_PLANE\_FACING\_HORIZONTAL\_UPWARD

 | 

Upward-facing horizontal plane, such as ground and table platforms.

 |
| 

ARENGINE\_PLANE\_FACING\_HORIZONTAL\_DOWNWARD

 | 

Downward-facing horizontal plane, such as the ceiling.

 |
| 

ARENGINE\_PLANE\_FACING\_VERTICAL

 | 

Vertical plane, such as the wall.

 |
| 

ARENGINE\_PLANE\_FACING\_INVALID

 | 

Invalid or unsupported plane type. This may occur due to changes in the environment, lighting conditions, or other factors.

 |

#### \[h2\]AREngine\_ARPointOrientationMode

enum AREngine\_ARPointOrientationMode

**Description**

Orientation mode.

**Start version**: 5.0.0(12)

| 
Enumerated Value

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_POINT\_ORIENTATION\_INITIALIZED\_TO\_IDENTITY

 | 

The orientation is consistent with that of the world coordinate system, but with minor adjustments.

 |
| 

ARENGINE\_POINT\_ORIENTATION\_ESTIMATED\_SURFACE\_NORMAL

 | 

The orientation is determined by the estimated plane's normal vector.

 |

#### \[h2\]AREngine\_ARPoseMode

enum AREngine\_ARPoseMode

**Description**

Output camera pose alignment format of AR Engine.

**Start version**: 5.1.0(18)

| 
Enumerated Value

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_POSE\_MODE\_GRAVITY

 | 

The output pose information (returned by [HMS\_AREngine\_ARCamera\_GetDisplayOrientedPose](#ga088648130f3a91cdf8d7b95f5ee1faf2) and [HMS\_AREngine\_ARCamera\_GetPose](#ga00df108c4ba187967a10e9c4d2e27d3a)) is the data aligned with the gravity coordinate system. For details, please refer to [AR Engine Gravity Aligned with World Coordinate System](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arengine-coordinate#section51232054151614).

 |
| 

ARENGINE\_POSE\_MODE\_GRAVITY\_HEADING

 | 

The output pose information (returned by [HMS\_AREngine\_ARCamera\_GetDisplayOrientedPose](#ga088648130f3a91cdf8d7b95f5ee1faf2) and [HMS\_AREngine\_ARCamera\_GetPose](#ga00df108c4ba187967a10e9c4d2e27d3a)) is the data aligned with the northbound ENU coordinate system. For details, please refer to [AR Engine Gravity Aligned with Northward Coordinate System](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arengine-coordinate#section1786771621711).

 |

#### \[h2\]AREngine\_ARPoseType

enum AREngine\_ARPoseType

**Description**

Pose type.

**Start version**: 5.0.0(12)

| 
Enumerated Value

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_POSE\_TYPE\_IDENTITY

 | 

Default state, that is, no rotation or translation.

 |
| 

ARENGINE\_POSE\_TYPE\_ROTATE\_90

 | 

Rotated by 90 degrees in clockwise direction.

 |
| 

ARENGINE\_POSE\_TYPE\_ROTATE\_180

 | 

Rotated by 180 degrees in clockwise direction.

 |
| 

ARENGINE\_POSE\_TYPE\_ROTATE\_270

 | 

Rotated by 270 degrees in clockwise direction.

 |

#### \[h2\]AREngine\_ARPowerMode

enum AREngine\_ARPowerMode

**Description**

Power consumption mode.

**Start version**: 5.0.0(12)

| 
Enumerated Value

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_POWER\_MODE\_NORMAL

 | 

Normal mode. AR Engine maintains a counterbalance between performance and power consumption.

 |
| 

ARENGINE\_POWER\_MODE\_POWER\_SAVING

 | 

Power-saving mode. AR Engine prioritizes reducing power consumption, which may result in lower performance in exchange for extended battery life.

 |
| 

ARENGINE\_POWER\_MODE\_PERFORMANCE\_FIRST

 | 

Performance-first mode. AR Engine prioritizes performance, offering higher processing capabilities and faster response times. However, this may lead to increased power consumption.

 |
| 

ARENGINE\_POWER\_MODE\_BOOST

 | 

Mode that outputs the device pose information only. The power consumption in this mode is lower than that in **ARENGINE\_POWER\_MODE\_NORMAL** mode. In this mode, plane-related settings such as [HMS\_AREngine\_ARConfig\_SetPlaneFindingMode](#ga884a7db93778e24eef0dfaa794c45674) do not take effect.

 |
| 

ARENGINE\_POWER\_MODE\_ULTRA\_POWER\_SAVING

 | 

Ultra power-saving mode. AR Engine further optimizes power consumption, reducing it beyond what is achieved in power-saving mode. This may result in more significant performance trade-offs.

 |

#### \[h2\]AREngine\_ARPreviewMode

enum AREngine\_ARPreviewMode

**Description**

Preview mode.

**Start version**: 5.0.0(12)

| 
Enumerated Value

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_PREVIEW\_MODE\_ENABLED

 | 

Enables camera preview.

 |
| 

ARENGINE\_PREVIEW\_MODE\_DISABLED

 | 

Disables camera preview, for example, when in VR mode and the preview stream is not required. In this mode, OpenGL textures set through [HMS\_AREngine\_ARSession\_SetCameraGLTexture](#gac697e4be36db63ed6098f154aa9ac01c) will not be updated.

 |

#### \[h2\]AREngine\_ARSemanticDenseMode

enum AREngine\_ARSemanticDenseMode

**Description**

Recognition mode of high-precision geometric reconstruction.

**Start version**: 6.0.0(20)

| 
Enumerated Value

 | 

**Description**

 |
| :-- | :-- |
| 

ARENGINE\_SEMANTIC\_DENSE\_MODE\_DISABLED

 | 

The high-precision geometric reconstruction recognition mode is disabled.

 |
| 

ARENGINE\_SEMANTIC\_DENSE\_MODE\_NORMAL

 | 

Normal mode, where only dense point cloud recognition is enabled.

 |
| 

ARENGINE\_SEMANTIC\_DENSE\_MODE\_CUBE\_VOLUME

 | 

Cube volume measurement mode.

 |
| 

ARENGINE\_SEMANTIC\_DENSE\_MODE\_CUBE\_SPACE

 | 

Cube space volume measurement mode.

 |

#### \[h2\]AREngine\_ARSemanticMode

enum AREngine\_ARSemanticMode

**Description**

Semantic mode.

**Start version**: 5.0.0(12)

| 
Enumerated Value

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SEMANTIC\_MODE\_NONE

 | 

Semantics not used.

 |
| 

ARENGINE\_SEMANTIC\_MODE\_PLANE

 | 

Plane semantics used.

 |
| 

ARENGINE\_SEMANTIC\_MODE\_TARGET

 | 

Object semantics used.

 |

#### \[h2\]AREngine\_ARSemanticPlaneLabel

enum AREngine\_ARSemanticPlaneLabel

**Description**

Semantic type of the current plane.

**Start version**: 5.0.0(12)

| 
Enumerated Value

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_PLANE\_UNKNOWN

 | 

Unknown type.

 |
| 

ARENGINE\_PLANE\_WALL

 | 

Wall.

 |
| 

ARENGINE\_PLANE\_FLOOR

 | 

Floor.

 |
| 

ARENGINE\_PLANE\_SEAT

 | 

Seat.

 |
| 

ARENGINE\_PLANE\_TABLE

 | 

Table.

 |
| 

ARENGINE\_PLANE\_CEILING

 | 

Ceiling.

 |
| 

ARENGINE\_PLANE\_DOOR

 | 

Door.

 |
| 

ARENGINE\_PLANE\_WINDOW

 | 

Window.

 |
| 

ARENGINE\_PLANE\_BED

 | 

Bed.

 |
| 

ARENGINE\_PLANE\_SPACE

 | 

Plane space.

**Start version**: 6.0.0(20)

 |
| 

ARENGINE\_CUBE\_VOLUME

 | 

Cube volume.

**Start version**: 6.0.0(20)

 |
| 

ARENGINE\_CUBE\_SPACE

 | 

Cube space.

**Start version**: 6.0.0(20)

 |

#### \[h2\]AREngine\_ARStatus

enum AREngine\_ARStatus

**Description**:

Error code returned by the API.

Defines the call status of an API.

**Start version**: 5.0.0(12)

| 
Enumerated Value

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_PERMISSION\_NOT\_GRANTED

 | 

Permissions not granted, such as the camera permission.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |
| 

ARENGINE\_ERROR\_DEVICE\_NOT\_SUPPORTED

 | 

Device not compatible.

 |
| 

ARENGINE\_ERROR\_FATAL

 | 

Failure.

 |
| 

ARENGINE\_ERROR\_SESSION\_PAUSED

 | 

Session paused.

 |
| 

ARENGINE\_ERROR\_SESSION\_NOT\_PAUSED

 | 

Session not paused.

 |
| 

ARENGINE\_ERROR\_NOT\_TRACKING

 | 

Not tracking.

 |
| 

ARENGINE\_ERROR\_TEXTURE\_NOT\_SET

 | 

Texture not set.

 |
| 

ARENGINE\_ERROR\_MISSING\_GL\_CONTEXT

 | 

GL context missing.

 |
| 

ARENGINE\_ERROR\_UNSUPPORTED\_CONFIGURATION

 | 

Configuration not supported.

 |
| 

ARENGINE\_ERROR\_RESOURCE\_EXHAUSTED

 | 

Resource exhausted.

 |
| 

ARENGINE\_ERROR\_NOT\_AVAILABLE

 | 

Service unavailable.

 |
| 

ARENGINE\_ERROR\_CAMERA\_NOT\_AVAILABLE

 | 

Camera unavailable.

 |
| 

ARENGINE\_ERROR\_IMAGE\_EXCEED\_NUM\_LIMIT

 | 

The number of images added exceeds the maximum.

**Start version**: 5.1.0(18)

 |
| 

ARENGINE\_ERROR\_IMAGE\_INSUFFICIENT\_QUALITY

 | 

The image with insufficient quality is added to the image database.

**Start version**: 5.1.0(18)

 |
| 

ARENGINE\_ERROR\_IMAGE\_INVALID\_DATABASE

 | 

No valid image database exists.

**Start version**: 5.1.0(18)

 |
| 

ARENGINE\_ERROR\_IMAGE\_ADD\_IMAGE\_TRACKING\_STATE

 | 

The pictures cannot be added when the tracking state is running.

**Start version**: 5.1.0(18)

 |
| 

ARENGINE\_ERROR\_NATIVEBUFFER\_CREATE\_FAILED

 | 

Failed to create NativeBuffer.

**Start version**: 6.0.0(20)

 |
| 

ARENGINE\_ERROR\_NATIVEBUFFER\_WRITE\_FAILED

 | 

Failed to write to NativeBuffer.

**Start version**: 6.0.0(20)

 |
| 

ARENGINE\_CAMERA\_SERVICE\_FATAL\_ERROR

 | 

The camera service is abnormal.

**Start version**: 6.0.2(22)

 |

#### \[h2\]AREngine\_ARTargetShapeLabel

enum AREngine\_ARTargetShapeLabel

**Description**

Shape of the recognized object.

**Start version**: 5.0.0(12)

| 
Enumerated Value

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_TARGET\_SHAPE\_UNKNOWN

 | 

Unknown shape.

 |
| 

ARENGINE\_TARGET\_SHAPE\_CUBE

 | 

Cube. The bounding box of regular objects can be recognized as a cube.

 |
| 

ARENGINE\_TARGET\_SHAPE\_CIRCLE

 | 

Circle.

 |
| 

ARENGINE\_TARGET\_SHAPE\_RECTANGLE

 | 

Rectangle.

 |

#### \[h2\]AREngine\_ARTrackableType

enum AREngine\_ARTrackableType

**Description**:

Type of a trackable object, such as a plane or a point.

**Start version**: 5.0.0(12)

| 
Enumerated Value

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_TRACKABLE\_BASE

 | 

Basic trackable object type, which can be used as the default [AREngine\_ARTrackableType](#ga993948a19fd2bdfa5b946e13a8d4fe3d).

 |
| 

ARENGINE\_TRACKABLE\_PLANE

 | 

Trackable object of the plane type.

 |
| 

ARENGINE\_TRACKABLE\_POINT

 | 

Trackable object of the point type.

 |
| 

ARENGINE\_TRACKABLE\_AUGMENTED\_IMAGE

 | 

Trackable object of the augmented image type.

**Start version**: 5.1.0(18)

 |
| 

ARENGINE\_TRACKABLE\_TARGET

 | 

Trackable object of the object type.

 |
| 

ARENGINE\_TRACKABLE\_INVALID

 | 

Invalid trackable object type.

 |

#### \[h2\]AREngine\_ARTrackingState

enum AREngine\_ARTrackingState

**Description**

Tracking state of the trackable object.

**Start version**: 5.0.0(12)

| 
Enumerated Value

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_TRACKING\_STATE\_TRACKING

 | 

Tracking.

 |
| 

ARENGINE\_TRACKING\_STATE\_PAUSED

 | 

Tracking paused.

 |
| 

ARENGINE\_TRACKING\_STATE\_STOPPED

 | 

Tracking stopped.

 |

#### \[h2\]AREngine\_ARTrackingStateReason

enum AREngine\_ARTrackingStateReason

**Description**

Possible causes of tracking failures.

**Start version**: 5.0.0(12)

| 
Enumerated Value

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_TRACKING\_STATE\_REASON\_NONE

 | 

Unknown cause. This may occur because the system is temporarily unable to recognize trackable objects but is still attempting to track them.

 |
| 

ARENGINE\_TRACKING\_STATE\_REASON\_EXCESSIVE\_MOTION

 | 

Target moving too fast. The trackable object (such as a plane, point, or image) is moving too quickly, making it difficult for AR Engine to accurately identify and track it.

 |
| 

ARENGINE\_TRACKING\_STATE\_REASON\_INSUFFICIENT\_FEATURES

 | 

Insufficient visual features (such as weak textures). The visual features of the trackable object are not rich enough, such as having unclear textures or overly uniform colors, preventing AR Engine from accurately identifying and tracking it.

 |

#### \[h2\]AREngine\_ARType

enum AREngine\_ARType

**Description**

AR capability type.

**Start version**: 5.0.0(12)

| 
Enumerated Value

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_TYPE\_WORLD

 | 

Environment tracking capability.

 |
| 

ARENGINE\_TYPE\_IMAGE

 | 

Image feature tracking capability.

**Start version**: 5.1.0(18)

 |

#### \[h2\]AREngine\_ARUpdateMode

enum AREngine\_ARUpdateMode

**Description**

Data update mode specified by [HMS\_AREngine\_ARSession\_Update](#ga1d1cacf372a8011a439f0e4e76994259).

**Start version**: 5.0.0(12)

| 
Enumerated Value

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_UPDATE\_MODE\_BLOCKING

 | 

[HMS\_AREngine\_ARSession\_Update](#ga1d1cacf372a8011a439f0e4e76994259) returns results only when new frames are available.

 |
| 

ARENGINE\_UPDATE\_MODE\_LATEST

 | 

[HMS\_AREngine\_ARSession\_Update](#ga1d1cacf372a8011a439f0e4e76994259) returns results immediately (returns the previous frame when no new frame is available).

 |

#### Function Description

#### \[h2\]HMS\_AREngine\_ARAnchor\_Detach

AREngine\_ARStatus HMS\_AREngine\_ARAnchor\_Detach(AREngine\_ARSession \*session, AREngine\_ARAnchor \*anchor)

**Description**

Instructs AR Engine to stop tracking and unbind an anchor.

However, this function does not release the anchor. You need to call [HMS\_AREngine\_ARAnchor\_Release](#gad04b12f9a2b0415789de5d6e1692f51c) to release the anchor.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

anchor

 | 

Anchor object to be unbound. For details, please refer to [AREngine\_ARAnchor](#ga76c16c9d68ba9a3b76f1869c60d8ca1d).

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |
| 

ARENGINE\_ERROR\_FATAL

 | 

Failure.

 |

#### \[h2\]HMS\_AREngine\_ARAnchor\_GetPose

AREngine\_ARStatus HMS\_AREngine\_ARAnchor\_GetPose(const AREngine\_ARSession \*session, const AREngine\_ARAnchor \*anchor, AREngine\_ARPose \*outPose)

**Description**

Obtains the pose of a specific anchor in the world coordinate system.

Each time [HMS\_AREngine\_ARSession\_Update](#ga1d1cacf372a8011a439f0e4e76994259) is called, the pose information returned by [HMS\_AREngine\_ARAnchor\_GetPose](#gad937acfc5d49f0909bdd84677bb0731a) may change.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

anchor

 | 

Anchor whose pose needs to be obtained. For details, please refer to [AREngine\_ARAnchor](#ga76c16c9d68ba9a3b76f1869c60d8ca1d).

 |
| 

outPose

 | 

Pose object of the anchor. For details, please refer to [AREngine\_ARPose](#gab2fa63142ebfb09f0c2ddf88cdb86604).

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |
| 

ARENGINE\_ERROR\_FATAL

 | 

Failure.

 |

#### \[h2\]HMS\_AREngine\_ARAnchor\_GetTrackingState

AREngine\_ARStatus HMS\_AREngine\_ARAnchor\_GetTrackingState(const AREngine\_ARSession \*session, const AREngine\_ARAnchor \*anchor, AREngine\_ARTrackingState \*outTrackingState)

**Description**

Obtains the tracking state of the pose of a specific anchor.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

anchor

 | 

Anchor whose tracking state is to be obtained. For details, please refer to [AREngine\_ARAnchor](#ga76c16c9d68ba9a3b76f1869c60d8ca1d).

 |
| 

outTrackingState

 | 

Tracking state of the anchor's current pose. For details, please refer to [AREngine\_ARTrackingState](#gaae57d2f58331e1033b60cdb2d506a382).

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |
| 

ARENGINE\_ERROR\_FATAL

 | 

Failure.

 |

#### \[h2\]HMS\_AREngine\_ARAnchor\_Release

void HMS\_AREngine\_ARAnchor\_Release(AREngine\_ARAnchor \*anchor)

**Description**

Releases the memory used by a specific anchor object.

Before releasing the memory, instruct AR Engine to stop tracking and unbind the anchor. For details, please refer to [HMS\_AREngine\_ARAnchor\_Detach](#ga6b731c00cc038f62d21ccb280067114b).

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

anchor

 | 

Anchor object to be released. For details, please refer to [AREngine\_ARAnchor](#ga76c16c9d68ba9a3b76f1869c60d8ca1d).

 |

#### \[h2\]HMS\_AREngine\_ARAnchorList\_AcquireItem

AREngine\_ARStatus HMS\_AREngine\_ARAnchorList\_AcquireItem(const AREngine\_ARSession \*session, const AREngine\_ARAnchorList \*anchorList, int32\_t index, AREngine\_ARAnchor \*\*outAnchor)

**Description**

Obtains the anchor at a specific location from the anchor object list.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

anchorList

 | 

List of anchor objects. For details, please refer to [AREngine\_ARAnchorList](#ga516a7f0954dcfda438799aa9e7c6e872).

 |
| 

index

 | 

Position of the anchor to be obtained in the anchor object list. The value ranges from 0 to 49.

 |
| 

outAnchor

 | 

Anchor information to be returned. For details, please refer to [AREngine\_ARAnchor](#ga76c16c9d68ba9a3b76f1869c60d8ca1d).

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |

#### \[h2\]HMS\_AREngine\_ARAnchorList\_Create

AREngine\_ARStatus HMS\_AREngine\_ARAnchorList\_Create(const AREngine\_ARSession \*session, AREngine\_ARAnchorList \*\*outAnchorList)

**Description**

Creates a list of anchor objects.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

outAnchorList

 | 

Reference to the anchor object list to be created. For details, please refer to [AREngine\_ARAnchorList](#ga516a7f0954dcfda438799aa9e7c6e872).

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |
| 

ARENGINE\_ERROR\_RESOURCE\_EXHAUSTED

 | 

Resource exhausted.

 |

#### \[h2\]HMS\_AREngine\_ARAnchorList\_Destroy

void HMS\_AREngine\_ARAnchorList\_Destroy(AREngine\_ARAnchorList \*anchorList)

**Description**

Releases a list of anchor objects.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

anchorList

 | 

List of anchors to be released. For details, please refer to [AREngine\_ARAnchorList](#ga516a7f0954dcfda438799aa9e7c6e872).

 |

#### \[h2\]HMS\_AREngine\_ARAnchorList\_GetSize

AREngine\_ARStatus HMS\_AREngine\_ARAnchorList\_GetSize(const AREngine\_ARSession \*session, const AREngine\_ARAnchorList \*anchorList, int32\_t \*outSize)

**Description**

Obtains the number of anchors in the anchor object list.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

anchorList

 | 

List of anchor objects. For details, please refer to [AREngine\_ARAnchorList](#ga516a7f0954dcfda438799aa9e7c6e872).

 |
| 

outSize

 | 

Number of anchors in the anchor object list.

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |

#### \[h2\]HMS\_AREngine\_ARAugmentedImage\_AcquireName

AREngine\_ARStatus HMS\_AREngine\_ARAugmentedImage\_AcquireName(const AREngine\_ARSession \*session, const AREngine\_ARAugmentedImage \*augmentedImage, char \*augmentedImageName, uint32\_t \*outNameLength)

**Description**

Returns the name of the tracking image.

**Start version**: 5.1.0(18)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

augmentedImage

 | 

Trackable object of the image type. For details, please refer to [AREngine\_ARAugmentedImage](#section68491824155217).

 |
| 

augmentedImageName

 | 

Image name, which cannot exceed 255 bytes.

 |
| 

outNameLength

 | 

Length of the image name.

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |

#### \[h2\]HMS\_AREngine\_ARAugmentedImage\_GetCenterPose

AREngine\_ARStatus HMS\_AREngine\_ARAugmentedImage\_GetCenterPose(const AREngine\_ARSession \*session, const AREngine\_ARAugmentedImage \*augmentedImage, AREngine\_ARPose \*outPose)

**Description**

Obtains the pose information of the center point of a tracking image in the world coordinate system.

**Start version**: 5.1.0(18)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

augmentedImage

 | 

Trackable object of the image type. For details, please refer to [AREngine\_ARAugmentedImage](#section68491824155217).

 |
| 

outPose

 | 

Pose of the tracking image. For details, please refer to [AREngine\_ARPose](#gab2fa63142ebfb09f0c2ddf88cdb86604).

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |

#### \[h2\]HMS\_AREngine\_ARAugmentedImage\_GetExtendX

AREngine\_ARStatus HMS\_AREngine\_ARAugmentedImage\_GetExtendX(const AREngine\_ARSession \*session, const AREngine\_ARAugmentedImage \*augmentedImage, float \*outExtendX)

**Description**

Obtains the estimated value on the X axis based on the center point of the image as the coordinate origin.

Returns the length of a physical image, in meters.

**Start version**: 5.1.0(18)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

augmentedImage

 | 

Trackable object of the image type. For details, please refer to [AREngine\_ARAugmentedImage](#section68491824155217).

 |
| 

outExtendX

 | 

Estimated length of the physical image on the X axis, in meters.

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |

#### \[h2\]HMS\_AREngine\_ARAugmentedImage\_GetExtendZ

AREngine\_ARStatus HMS\_AREngine\_ARAugmentedImage\_GetExtendZ(const AREngine\_ARSession \*session, const AREngine\_ARAugmentedImage \*augmentedImage, float \*outExtendZ)

**Description**

Obtains the estimated value on the Z axis based on the center point of the image as the coordinate origin.

Returns the width of a physical image, in meters.

**Start version**: 5.1.0(18)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

augmentedImage

 | 

Trackable object of the image type. For details, please refer to [AREngine\_ARAugmentedImage](#section68491824155217).

 |
| 

outExtendZ

 | 

Estimated width of the physical image on the Z axis, in meters.

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |

#### \[h2\]HMS\_AREngine\_ARAugmentedImage\_GetIndex

AREngine\_ARStatus HMS\_AREngine\_ARAugmentedImage\_GetIndex(const AREngine\_ARSession \*session, const AREngine\_ARAugmentedImage \*augmentedImage, uint32\_t \*outIndex)

**Description**

Obtains the index of a tracking image in the tracking image database.

**Start version**: 5.1.0(18)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

augmentedImage

 | 

Trackable object of the image type. For details, please refer to [AREngine\_ARAugmentedImage](#section68491824155217).

 |
| 

outIndex

 | 

Index of the image.

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |

#### \[h2\]HMS\_AREngine\_ARAugmentedImageDatabase\_AddImage

AREngine\_ARStatus HMS\_AREngine\_ARAugmentedImageDatabase\_AddImage(AREngine\_ARAugmentedImageDatabase \*database, const AREngine\_ARAugmentedImageSource \*image, uint32\_t \*outIndex, AREngine\_ARAddAugmentedImageReason \*outReason)

**Description**

Adds an image to the image database and outputs the index of the image.

**Start version**: 5.1.0(18)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

database

 | 

Tracking image database. For details, please refer to [AREngine\_ARAugmentedImageDatabase](#section152051642330).

 |
| 

image

 | 

Image information. For details, please refer to [AREngine\_ARAugmentedImageSource](../../header-files-and-structs/structs/arengine-araugmentedimagesource/document.md).

 |
| 

outIndex

 | 

Index of the added image.

 |
| 

outReason

 | 

Reason why the image fails to be added. For details, please refer to [AREngine\_ARAddAugmentedImageReason](#section2441053595).

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |
| 

ARENGINE\_ERROR\_FATAL

 | 

Failure.

 |
| 

ARENGINE\_ERROR\_RESOURCE\_EXHAUSTED

 | 

Resource exhausted.

 |
| 

ARENGINE\_ERROR\_IMAGE\_EXCEED\_NUM\_LIMIT

 | 

The number of images added exceeds the maximum.

**Start version**: 5.1.0(18)

 |
| 

ARENGINE\_ERROR\_IMAGE\_INSUFFICIENT\_QUALITY

 | 

The image with insufficient quality is added to the image database.

**Start version**: 5.1.0(18)

 |

#### \[h2\]HMS\_AREngine\_ARAugmentedImageDatabase\_Create

AREngine\_ARStatus HMS\_AREngine\_ARAugmentedImageDatabase\_Create(AREngine\_ARAugmentedImageDatabase \*\*outDatabase)

**Description**

Creates an empty tracking image database.

**Start version**: 5.1.0(18)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

outDatabase

 | 

Pointer to the image library to be created. For details, please refer to [AREngine\_ARAugmentedImageDatabase](#section152051642330).

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |
| 

ARENGINE\_ERROR\_FATAL

 | 

Failure.

 |
| 

ARENGINE\_ERROR\_RESOURCE\_EXHAUSTED

 | 

Resource exhausted.

 |

#### \[h2\]HMS\_AREngine\_ARAugmentedImageDatabase\_Deserialize

AREngine\_ARStatus HMS\_AREngine\_ARAugmentedImageDatabase\_Deserialize(const uint8\_t \*buffer, const uint64\_t bufSize, AREngine\_ARAugmentedImageDatabase \*\*outDatabase)

**Description**

Deserializes the feature database.

You can deserialize the buffer data generated or saved last time into the feature database and use the feature database directly.

**Start version**: 5.1.0(18)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

buffer

 | 

Tracking image database buffer.

 |
| 

bufSize

 | 

Size of the tracking image database buffer. The maximum value cannot exceed the length of the Int64 type.

 |
| 

outDatabase

 | 

Tracking image database. For details, please refer to [AREngine\_ARAugmentedImageDatabase](#section152051642330).

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |
| 

ARENGINE\_ERROR\_FATAL

 | 

Failure.

 |
| 

ARENGINE\_ERROR\_RESOURCE\_EXHAUSTED

 | 

Resource exhausted.

 |

#### \[h2\]HMS\_AREngine\_ARAugmentedImageDatabase\_Destroy

AREngine\_ARStatus HMS\_AREngine\_ARAugmentedImageDatabase\_Destroy(AREngine\_ARAugmentedImageDatabase \*database)

**Description**

Releases an image database object.

**Start version**: 5.1.0(18)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

database

 | 

Tracking image database. For details, please refer to [AREngine\_ARAugmentedImageDatabase](#section152051642330).

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |

#### \[h2\]HMS\_AREngine\_ARAugmentedImageDatabase\_GetAddMode

AREngine\_ARStatus HMS\_AREngine\_ARAugmentedImageDatabase\_GetAddMode(const AREngine\_ARAugmentedImageDatabase \*database, AREngine\_ARImageDatabaseMode \*outAddMode)

**Description**

Obtains the mode of adding a tracking image.

**Start version**: 5.1.0(18)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

database

 | 

Tracking image database. For details, please refer to [AREngine\_ARAugmentedImageDatabase](#section152051642330).

 |
| 

outAddMode

 | 

Mode of adding a tracking image. For details, please refer to [AREngine\_ARImageDatabaseMode](#section683253471219).

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |

#### \[h2\]HMS\_AREngine\_ARAugmentedImageDatabase\_SetAddMode

AREngine\_ARStatus HMS\_AREngine\_ARAugmentedImageDatabase\_SetAddMode(const AREngine\_ARAugmentedImageDatabase \*database, AREngine\_ARImageDatabaseMode addMode)

**Description**

Sets the mode of adding a tracking image.

**Start version**: 5.1.0(18)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

database

 | 

Tracking image database. For details, please refer to [AREngine\_ARAugmentedImageDatabase](#section152051642330).

 |
| 

addMode

 | 

Mode of adding a tracking image. For details, please refer to [AREngine\_ARImageDatabaseMode](#section683253471219).

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |

#### \[h2\]HMS\_AREngine\_ARAugmentedImageDatabase\_GetCapacity

AREngine\_ARStatus HMS\_AREngine\_ARAugmentedImageDatabase\_GetCapacity(const AREngine\_ARAugmentedImageDatabase \*database, uint32\_t \*outCapacity)

**Description**

Obtains the maximum number of images that can be added.

**Start version**: 5.1.0(18)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

database

 | 

Tracking image database. For details, please refer to [AREngine\_ARAugmentedImageDatabase](#section152051642330).

 |
| 

outCapacity

 | 

Maximum number of images. The default value is **50**.

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |

#### \[h2\]HMS\_AREngine\_ARAugmentedImageDatabase\_GetImageCount

AREngine\_ARStatus HMS\_AREngine\_ARAugmentedImageDatabase\_GetImageCount(const AREngine\_ARAugmentedImageDatabase \*database, uint32\_t \*outImageCount)

**Description**

Obtains the number of images stored in the database.

**Start version**: 5.1.0(18)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

database

 | 

Tracking image database. For details, please refer to [AREngine\_ARAugmentedImageDatabase](#section152051642330).

 |
| 

outImageCount

 | 

Number of returned images.

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |
| 

ARENGINE\_ERROR\_FATAL

 | 

Failure.

 |

#### \[h2\]HMS\_AREngine\_ARAugmentedImageDatabase\_Serialize

AREngine\_ARStatus HMS\_AREngine\_ARAugmentedImageDatabase\_Serialize(const AREngine\_ARAugmentedImageDatabase \*database, uint8\_t \*\*outBuffer, uint64\_t \*outBufSize)

**Description**

Serializes the feature database.

After images are added, the feature database can be serialized into a buffer. You can save the buffer for future use.

**Start version**: 5.1.0(18)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

database

 | 

Tracking image database. For details, please refer to [AREngine\_ARAugmentedImageDatabase](#section152051642330).

 |
| 

outBuffer

 | 

Tracking image database buffer.

 |
| 

outBufSize

 | 

Size of the tracking image database buffer.

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |
| 

ARENGINE\_ERROR\_FATAL

 | 

Failure.

 |

#### \[h2\]HMS\_AREngine\_ARCamera\_GetDisplayOrientedPose

AREngine\_ARStatus HMS\_AREngine\_ARCamera\_GetDisplayOrientedPose(const AREngine\_ARSession \*session, const AREngine\_ARCamera \*camera, AREngine\_ARPose \*outPose)

**Description**

Sets **outPose** to the pose of the virtual camera (facing the display) in the world space, in order to render AR content into the latest frame.

The pose is that of the OpenGL camera, where the positive direction of the X axis is right, the positive direction of the Y axis is upwards, and the negative direction of the Z axis is the look-at direction of the camera. The camera position refers to the physical camera position, and the orientation of the camera's X axis and Y axis is affected by the screen orientation (taking display rotation into account).

The pose information can be used only when [ARENGINE\_TRACKING\_STATE\_TRACKING](#gaae57d2f58331e1033b60cdb2d506a382) is returned by [HMS\_AREngine\_ARCamera\_GetTrackingState](#ga2dc931eee56ae5ea899f8acc08eb3f36).

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

camera

 | 

Camera corresponding to the session. For details, please refer to [AREngine\_ARCamera](#ga7bdcf1fb36c404d36e09ad70d2545d92).

 |
| 

outPose

 | 

Pose of the virtual camera in the world space. For details, please refer to [AREngine\_ARPose](#gab2fa63142ebfb09f0c2ddf88cdb86604).

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |

#### \[h2\]HMS\_AREngine\_ARCamera\_GetImageIntrinsics

AREngine\_ARStatus HMS\_AREngine\_ARCamera\_GetImageIntrinsics(const AREngine\_ARSession \*session, const AREngine\_ARCamera \*camera, AREngine\_ARCameraIntrinsics \*outIntrinsics)

**Description**

Obtains the object of the offline intrinsic camera parameters. This object can be used to obtain the camera's focal length, image dimensions, principal point, and distortion parameters.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

camera

 | 

Camera corresponding to the session. For details, please refer to [AREngine\_ARCamera](#ga7bdcf1fb36c404d36e09ad70d2545d92).

 |
| 

outIntrinsics

 | 

Object of the intrinsic camera parameters. For details, please refer to [AREngine\_ARCameraIntrinsics](#ga17948eef3aa7ff7f2fa8aff6a63b4b51).

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |
| 

ARENGINE\_ERROR\_FATAL

 | 

Failure.

 |

#### \[h2\]HMS\_AREngine\_ARCamera\_GetPose

AREngine\_ARStatus HMS\_AREngine\_ARCamera\_GetPose(const AREngine\_ARSession \*session, const AREngine\_ARCamera \*camera, AREngine\_ARPose \*outPose)

**Description**

Sets **outPose** to the pose of the physical camera in the world space in the latest frame. The pose is the pose of the OpenGL camera.

The positive direction of the X axis is right, the positive direction of the Y axis is up, and the negative direction of the Z axis is the gaze direction of the camera. The camera position refers to the physical camera position, and the orientation of the camera's X axis and Y axis is not affected by the screen orientation (taking display rotation into account).

The pose information can be used only when [ARENGINE\_TRACKING\_STATE\_TRACKING](#gaae57d2f58331e1033b60cdb2d506a382) is returned by [HMS\_AREngine\_ARCamera\_GetTrackingState](#ga2dc931eee56ae5ea899f8acc08eb3f36).

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

camera

 | 

Camera corresponding to the session. For details, please refer to [AREngine\_ARCamera](#ga7bdcf1fb36c404d36e09ad70d2545d92).

 |
| 

outPose

 | 

Pose of the physical camera in the world space. For details, please refer to [AREngine\_ARPose](#gab2fa63142ebfb09f0c2ddf88cdb86604).

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |

#### \[h2\]HMS\_AREngine\_ARCamera\_GetProjectionMatrix

AREngine\_ARStatus HMS\_AREngine\_ARCamera\_GetProjectionMatrix(const AREngine\_ARSession \*session, const AREngine\_ARCamera \*camera, AREngine\_ClipPlaneDistance clipPlaneDistance, float \*outDestColMajor4x4, int32\_t destColMajor4x4Num)

**Description**

Obtains the projection matrix used for rendering virtual content on top of the camera image. This matrix can be used for converting from the camera coordinate system to the clip coordinate system.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

camera

 | 

Camera corresponding to the session. For details, please refer to [AREngine\_ARCamera](#ga7bdcf1fb36c404d36e09ad70d2545d92).

 |
| 

clipPlaneDistance

 | 

Distance to the OpenGL clipping plane. For details, please refer to [AREngine\_ClipPlaneDistance](../../header-files-and-structs/structs/arengine-clipplanedistance/document.md).

 |
| 

outDestColMajor4x4

 | 

Array consisting of 16 floating-point numbers, indicating a column-major uniform transformation matrix in OpenGL.

 |
| 

destColMajor4x4Num

 | 

Array size: [ARENGINE\_VIEW\_MATRIX\_SIZE](#section02261581599).

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |
| 

ARENGINE\_ERROR\_FATAL

 | 

Failure.

 |

#### \[h2\]HMS\_AREngine\_ARCamera\_GetTrackingState

AREngine\_ARStatus HMS\_AREngine\_ARCamera\_GetTrackingState(const AREngine\_ARSession \*session, const AREngine\_ARCamera \*camera, AREngine\_ARTrackingState \*outTrackingState)

**Description**

Obtains the current tracking state of the camera.

The camera pose is available only when the tracking state is [ARENGINE\_TRACKING\_STATE\_TRACKING](#gaae57d2f58331e1033b60cdb2d506a382).

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

camera

 | 

Camera corresponding to the session. For details, please refer to [AREngine\_ARCamera](#ga7bdcf1fb36c404d36e09ad70d2545d92).

 |
| 

outTrackingState

 | 

Current tracking state of the camera. For details, please refer to [AREngine\_ARTrackingState](#gaae57d2f58331e1033b60cdb2d506a382).

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |

#### \[h2\]HMS\_AREngine\_ARCamera\_GetTrackingStateReason

AREngine\_ARStatus HMS\_AREngine\_ARCamera\_GetTrackingStateReason(const AREngine\_ARSession \*session, const AREngine\_ARCamera \*camera, AREngine\_ARTrackingStateReason \*outTrackingStateReason)

**Description**

Obtains the reason when the current tracking state of the camera is [ARENGINE\_TRACKING\_STATE\_PAUSED](#gaae57d2f58331e1033b60cdb2d506a382).

When the current tracking state of the camera is [ARENGINE\_TRACKING\_STATE\_TRACKING](#gaae57d2f58331e1033b60cdb2d506a382), the function returns [ARENGINE\_TRACKING\_STATE\_REASON\_NONE](#ga67774b71935ef2f8a2ae5e5822c3dcdb).

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

camera

 | 

Camera corresponding to the session. For details, please refer to [AREngine\_ARCamera](#ga7bdcf1fb36c404d36e09ad70d2545d92).

 |
| 

outTrackingStateReason

 | 

Cause of the tracking failure. For details, please refer to [AREngine\_ARTrackingStateReason](#ga67774b71935ef2f8a2ae5e5822c3dcdb).

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |

#### \[h2\]HMS\_AREngine\_ARCamera\_GetViewMatrix

AREngine\_ARStatus HMS\_AREngine\_ARCamera\_GetViewMatrix(const AREngine\_ARSession \*session, const AREngine\_ARCamera \*camera, float \*outColMajor4x4, int32\_t colMajor4x4Num)

**Description**

Obtains the view matrix of the camera in the latest frame.

This matrix performs the inverse transformation of the pose provided by [HMS\_AREngine\_ARCamera\_GetDisplayOrientedPose](#ga088648130f3a91cdf8d7b95f5ee1faf2). That is, it transforms the world coordinate system to the camera coordinate system.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

camera

 | 

Camera corresponding to the session. For details, please refer to [AREngine\_ARCamera](#ga7bdcf1fb36c404d36e09ad70d2545d92).

 |
| 

outColMajor4x4

 | 

Array consisting of 16 floating-point numbers, indicating a column-major uniform transformation matrix in OpenGL.

 |
| 

colMajor4x4Num

 | 

Array size. The array size must be greater than or equal to [ARENGINE\_VIEW\_MATRIX\_SIZE](#section02261581599).

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |

#### \[h2\]HMS\_AREngine\_ARCamera\_Release

void HMS\_AREngine\_ARCamera\_Release(AREngine\_ARCamera \*camera)

**Description**

Releases the reference to the camera.

You need to call [HMS\_AREngine\_ARCamera\_Release](#ga16909b4002b9c6250dad88bb8397adc9) if you have called [HMS\_AREngine\_ARFrame\_AcquireCamera](#ga5295c975a0ff3d633a1dde5a8eb70863).

This method is ineffective before [HMS\_AREngine\_ARFrame\_AcquireCamera](#ga5295c975a0ff3d633a1dde5a8eb70863) is called.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

camera

 | 

Camera reference to be released. For details, please refer to [AREngine\_ARCamera](#ga7bdcf1fb36c404d36e09ad70d2545d92).

 |

#### \[h2\]HMS\_AREngine\_ARCameraConfig\_Create

AREngine\_ARStatus HMS\_AREngine\_ARCameraConfig\_Create(const AREngine\_ARSession \*session, AREngine\_ARCameraConfig \*\*outCameraConfig)

**Description**

Creates a camera configuration object.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

outCameraConfig

 | 

Pointer to the newly allocated address of the camera configuration object. For details, please refer to [AREngine\_ARCameraConfig](#ga9b7a5a2082a4127f85a1c9a95cb9acba).

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |
| 

ARENGINE\_ERROR\_RESOURCE\_EXHAUSTED

 | 

Resource exhausted.

 |

#### \[h2\]HMS\_AREngine\_ARCameraConfig\_Destroy

void HMS\_AREngine\_ARCameraConfig\_Destroy(AREngine\_ARCameraConfig \*cameraConfig)

**Description**

Releases a camera configuration object.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

cameraConfig

 | 

Pointer to the camera configuration object to be released. For details, please refer to [AREngine\_ARCameraConfig](#ga9b7a5a2082a4127f85a1c9a95cb9acba).

 |

#### \[h2\]HMS\_AREngine\_ARCameraConfig\_GetImageDimensions

AREngine\_ARStatus HMS\_AREngine\_ARCameraConfig\_GetImageDimensions(const AREngine\_ARSession \*session, const AREngine\_ARCameraConfig \*cameraConfig, int32\_t \*outWidth, int32\_t \*outHeight)

**Description**

Obtains the size of the image sent by the camera to the CPU for processing from a camera configuration object.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

cameraConfig

 | 

Pointer to the camera configuration object. For details, please refer to [AREngine\_ARCameraConfig](#ga9b7a5a2082a4127f85a1c9a95cb9acba).

 |
| 

outWidth

 | 

Width of the image, in pixels.

 |
| 

outHeight

 | 

Height of the image, in pixels.

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |

#### \[h2\]HMS\_AREngine\_ARCameraConfig\_GetTextureDimensions

AREngine\_ARStatus HMS\_AREngine\_ARCameraConfig\_GetTextureDimensions(const AREngine\_ARSession \*session, const AREngine\_ARCameraConfig \*cameraConfig, int32\_t \*outWidth, int32\_t \*outHeight)

**Description**

Obtains the size of the image texture sent by the camera to the GPU for processing from a camera configuration object.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

cameraConfig

 | 

Pointer to the camera configuration object. For details, please refer to [AREngine\_ARCameraConfig](#ga9b7a5a2082a4127f85a1c9a95cb9acba).

 |
| 

outWidth

 | 

Width of the image texture, in pixels.

 |
| 

outHeight

 | 

Height of the image texture, in pixels.

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |

#### \[h2\]HMS\_AREngine\_ARCameraIntrinsics\_Create

AREngine\_ARStatus HMS\_AREngine\_ARCameraIntrinsics\_Create(const AREngine\_ARSession \*session, AREngine\_ARCameraIntrinsics \*\*outIntrinsics)

**Description**

Creates an object of the intrinsic camera parameters.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

outIntrinsics

 | 

Pointer to the newly allocated address of the object of intrinsic camera parameters. For details, please refer to [AREngine\_ARCameraIntrinsics](#ga17948eef3aa7ff7f2fa8aff6a63b4b51).

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |
| 

ARENGINE\_ERROR\_RESOURCE\_EXHAUSTED

 | 

Resource exhausted.

 |

#### \[h2\]HMS\_AREngine\_ARCameraIntrinsics\_Destroy

void HMS\_AREngine\_ARCameraIntrinsics\_Destroy(AREngine\_ARCameraIntrinsics \*intrinsics)

**Description**

Releases a specific object of intrinsic camera parameters.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

intrinsics

 | 

Object of intrinsic camera parameters to be released. For details, please refer to [AREngine\_ARCameraIntrinsics](#ga17948eef3aa7ff7f2fa8aff6a63b4b51).

 |

#### \[h2\]HMS\_AREngine\_ARCameraIntrinsics\_GetDistortion

AREngine\_ARStatus HMS\_AREngine\_ARCameraIntrinsics\_GetDistortion(const AREngine\_ARSession \*session, const AREngine\_ARCameraIntrinsics \*intrinsics, float \*outDistortion, int32\_t distortionNum)

**Description**

Obtains the distortion parameters of a camera.

It includes 5 components: **outDistortion\[0\]** to **outDistortion \[2\]** represent k1, k2, and k3 (radial distortion coefficients), and **outDistortion \[3\]** to **outDistortion \[4\]** are the tangential distortion coefficients.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

intrinsics

 | 

Pointer to the object of intrinsic camera parameters. For details, please refer to [AREngine\_ARCameraIntrinsics](#ga17948eef3aa7ff7f2fa8aff6a63b4b51).

 |
| 

outDistortion

 | 

Returns an array of camera distortion parameters.

 |
| 

distortionNum

 | 

Number of camera distortion parameters. For details, please refer to [ARENGINE\_DISTORTION\_COUNT](#section2059093619593).

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |

#### \[h2\]HMS\_AREngine\_ARCameraIntrinsics\_GetFocalLength

AREngine\_ARStatus HMS\_AREngine\_ARCameraIntrinsics\_GetFocalLength(const AREngine\_ARSession \*session, const AREngine\_ARCameraIntrinsics \*intrinsics, float \*outFocalX, float \*outFocalY)

**Description**

Obtains the focal length of a camera (in pixels).

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

intrinsics

 | 

Pointer to the object of intrinsic camera parameters. For details, please refer to [AREngine\_ARCameraIntrinsics](#ga17948eef3aa7ff7f2fa8aff6a63b4b51).

 |
| 

outFocalX

 | 

Pixel focal length in the x(u) direction of the intrinsic camera parameter matrix.

 |
| 

outFocalY

 | 

Pixel focal length in the y(v) direction of the intrinsic camera parameter matrix.

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |

#### \[h2\]HMS\_AREngine\_ARCameraIntrinsics\_GetImageDimensions

AREngine\_ARStatus HMS\_AREngine\_ARCameraIntrinsics\_GetImageDimensions(const AREngine\_ARSession \*session, const AREngine\_ARCameraIntrinsics \*intrinsics, int32\_t \*outWidth, int32\_t \*outHeight)

**Description**

Obtains the camera image dimensions, including the width and height (in pixels).

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

intrinsics

 | 

Pointer to the object of intrinsic camera parameters. For details, please refer to [AREngine\_ARCameraIntrinsics](#ga17948eef3aa7ff7f2fa8aff6a63b4b51).

 |
| 

outWidth

 | 

Width of the camera image, in pixels.

 |
| 

outHeight

 | 

Height of the camera image, in pixels.

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |

#### \[h2\]HMS\_AREngine\_ARCameraIntrinsics\_GetPrincipalPoint

AREngine\_ARStatus HMS\_AREngine\_ARCameraIntrinsics\_GetPrincipalPoint(const AREngine\_ARSession \*session, const AREngine\_ARCameraIntrinsics \*intrinsics, float \*outPrincipalX, float \*outPrincipalY)

**Description**

Obtains the principal point of a camera, with the location of the point expressed in pixels.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

intrinsics

 | 

Pointer to the object of intrinsic camera parameters. For details, please refer to [AREngine\_ARCameraIntrinsics](#ga17948eef3aa7ff7f2fa8aff6a63b4b51).

 |
| 

outPrincipalX

 | 

X-axis coordinate of the camera's principal point.

 |
| 

outPrincipalY

 | 

Y-axis coordinate of the camera's principal point.

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |

#### \[h2\]HMS\_AREngine\_ARConfig\_Create

AREngine\_ARStatus HMS\_AREngine\_ARConfig\_Create(const AREngine\_ARSession \*session, AREngine\_ARConfig \*\*outConfig)

**Description**

Creates a configuration object with a proper default configuration.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

outConfig

 | 

Pointer to the newly allocated address of the configuration object. For details, please refer to [AREngine\_ARConfig](#gab0b32ef6018535fd30000f4b6d65f619).

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |
| 

ARENGINE\_ERROR\_RESOURCE\_EXHAUSTED

 | 

Resource exhausted.

 |

#### \[h2\]HMS\_AREngine\_ARConfig\_Destroy

void HMS\_AREngine\_ARConfig\_Destroy(AREngine\_ARConfig \*config)

**Description**

Releases the memory used by a specific configuration object.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

config

 | 

Configuration object to be released. For details, please refer to [AREngine\_ARConfig](#gab0b32ef6018535fd30000f4b6d65f619).

 |

#### \[h2\]HMS\_AREngine\_ARConfig\_GetARType

AREngine\_ARStatus HMS\_AREngine\_ARConfig\_GetARType(const AREngine\_ARSession \*session, const AREngine\_ARConfig \*config, AREngine\_ARType \*type)

**Description**

Obtains the AR capability type in use.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

config

 | 

Pointer to the configuration object with the target configuration information. For details, please refer to [AREngine\_ARConfig](#gab0b32ef6018535fd30000f4b6d65f619).

 |
| 

type

 | 

Type of the AR Engine capability in use. For details, please refer to [AREngine\_ARType](#ga987888aea7dcaa9abcdb64581c850bf5).

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |

#### \[h2\]HMS\_AREngine\_ARConfig\_GetCameraPreviewMode

AREngine\_ARStatus HMS\_AREngine\_ARConfig\_GetCameraPreviewMode(const AREngine\_ARSession \*session, AREngine\_ARConfig \*config, AREngine\_ARPreviewMode \*outMode)

**Description**

Obtains the current preview mode.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

config

 | 

Pointer to the configuration object with the target configuration information. For details, please refer to [AREngine\_ARConfig](#gab0b32ef6018535fd30000f4b6d65f619).

 |
| 

outMode

 | 

Camera preview mode. For details, please refer to [AREngine\_ARPreviewMode](#gadef0f2099b106b872a014ef6551906ae).

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |

#### \[h2\]HMS\_AREngine\_ARConfig\_GetDepthMode

AREngine\_ARStatus HMS\_AREngine\_ARConfig\_GetDepthMode(const AREngine\_ARSession \*session, const AREngine\_ARConfig \*config, AREngine\_ARDepthMode \*outDepthMode)

**Description**

Obtains the current depth mode.

**Start version**: 5.0.5(17)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

config

 | 

Pointer to the configuration object with the target configuration information. For details, please refer to [AREngine\_ARConfig](#gab0b32ef6018535fd30000f4b6d65f619).

 |
| 

outDepthMode

 | 

Current depth mode. For details, please refer to [AREngine\_ARDepthMode](#section12321429115215).

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |

#### \[h2\]HMS\_AREngine\_ARConfig\_GetFocusMode

AREngine\_ARStatus HMS\_AREngine\_ARConfig\_GetFocusMode(const AREngine\_ARSession \*session, const AREngine\_ARConfig \*config, AREngine\_ARFocusMode \*focusMode)

**Description**

Obtains the current camera focus mode.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

config

 | 

Pointer to the configuration object with the target configuration information. For details, please refer to [AREngine\_ARConfig](#gab0b32ef6018535fd30000f4b6d65f619).

 |
| 

focusMode

 | 

Current focus mode. For details, please refer to [AREngine\_ARFocusMode](#gaf50530faa0d094182a0db0c73b75d875).

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |

#### \[h2\]HMS\_AREngine\_ARConfig\_GetMaxMapSize

AREngine\_ARStatus HMS\_AREngine\_ARConfig\_GetMaxMapSize(const AREngine\_ARSession \*session, const AREngine\_ARConfig \*config, uint64\_t \*maxMapSize)

**Description**

Obtains the maximum memory size for storing map data.

You can call this API to obtain the maximum memory size for storing map data after [HMS\_AREngine\_ARSession\_Configure](#ga6394ae995148abbe3d00082817bf320a) is executed.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

config

 | 

Pointer to the configuration object with the target configuration information. For details, please refer to [AREngine\_ARConfig](#gab0b32ef6018535fd30000f4b6d65f619).

 |
| 

maxMapSize

 | 

Maximum memory size for storing map data, in MB.

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |

#### \[h2\]HMS\_AREngine\_ARConfig\_GetMeshMode

AREngine\_ARStatus HMS\_AREngine\_ARConfig\_GetMeshMode(const AREngine\_ARSession \*session, const AREngine\_ARConfig \*config, AREngine\_ARMeshMode \*outMeshMode)

**Description**

Obtains the current mesh mode.

**Start version**: 5.1.0(18)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

config

 | 

Pointer to the configuration object with the target configuration information. For details, please refer to [AREngine\_ARConfig](#gab0b32ef6018535fd30000f4b6d65f619).

 |
| 

outMeshMode

 | 

Mesh mode. For details, please refer to [AREngine\_ARMeshMode](#section19436658201620).

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |

#### \[h2\]HMS\_AREngine\_ARConfig\_GetPlaneFindingMode

AREngine\_ARStatus HMS\_AREngine\_ARConfig\_GetPlaneFindingMode(const AREngine\_ARSession \*session, const AREngine\_ARConfig \*config, AREngine\_ARPlaneFindingMode \*planeFindingMode)

**Description**

Obtains the current plane finding mode.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

config

 | 

Pointer to the configuration object with the target configuration information. For details, please refer to [AREngine\_ARConfig](#gab0b32ef6018535fd30000f4b6d65f619).

 |
| 

planeFindingMode

 | 

Current plane finding mode. For details, please refer to [AREngine\_ARPlaneFindingMode](#gab8e7db52d819359026fc4a82815d3fff).

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |

#### \[h2\]HMS\_AREngine\_ARConfig\_GetPoseMode

AREngine\_ARStatus HMS\_AREngine\_ARConfig\_GetPoseMode(const AREngine\_ARSession \*session, const AREngine\_ARConfig \*config, AREngine\_ARPoseMode \*poseMode)

**Description**

Obtains the alignment mode of the pose coordinate system output by the camera.

**Start version**: 5.1.0(18)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

config

 | 

Pointer to the configuration object with the target configuration information. For details, please refer to [AREngine\_ARConfig](#gab0b32ef6018535fd30000f4b6d65f619).

 |
| 

poseMode

 | 

Camera pose mode. For details, please refer to [AREngine\_ARPoseMode](#section1249515330198).

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |

#### \[h2\]HMS\_AREngine\_ARConfig\_GetPowerMode

AREngine\_ARStatus HMS\_AREngine\_ARConfig\_GetPowerMode(const AREngine\_ARSession \*session, const AREngine\_ARConfig \*config, AREngine\_ARPowerMode \*powerMode)

**Description**

Obtains the current power consumption mode.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

config

 | 

Pointer to the configuration object with the target configuration information. For details, please refer to [AREngine\_ARConfig](#gab0b32ef6018535fd30000f4b6d65f619).

 |
| 

powerMode

 | 

Current power consumption mode. For details, please refer to [AREngine\_ARPowerMode](#ga3d925e007e2847e69f22af68ec922507).

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |

#### \[h2\]HMS\_AREngine\_ARConfig\_GetSemanticDenseMode

AREngine\_ARStatus HMS\_AREngine\_ARConfig\_GetSemanticDenseMode(const AREngine\_ARSession \*session, const AREngine\_ARConfig \*config, AREngine\_ARSemanticDenseMode \*outSemanticDenseMode)

**Description**

Obtains the set high-precision geometric reconstruction mode.

**Start version**: 6.0.0(20)

**Parameters**:

| 
Name

 | 

**Description**

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

config

 | 

Pointer to the configuration object with the target configuration information. For details, please refer to [AREngine\_ARConfig](#gab0b32ef6018535fd30000f4b6d65f619).

 |
| 

outSemanticDenseMode

 | 

Current high-precision geometric reconstruction mode. For details, please refer to [AREngine\_ARSemanticDenseMode](#section09971756142213).

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |

#### \[h2\]HMS\_AREngine\_ARConfig\_GetSemanticMode

AREngine\_ARStatus HMS\_AREngine\_ARConfig\_GetSemanticMode(const AREngine\_ARSession \*session, const AREngine\_ARConfig \*config, AREngine\_ARSemanticMode \*mode)

**Description**

Obtains the configured semantic recognition mode.

This method becomes effective after [HMS\_AREngine\_ARConfig\_SetSemanticMode](#gaae87c1ef02b6e9bab123fae2086da248) is called.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

config

 | 

Pointer to the configuration object with the target configuration information. For details, please refer to [AREngine\_ARConfig](#gab0b32ef6018535fd30000f4b6d65f619).

 |
| 

mode

 | 

Current semantic mode. For details, please refer to [AREngine\_ARSemanticMode](#ga34d3000de29454b99d89406d288d6ed5).

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |

#### \[h2\]HMS\_AREngine\_ARConfig\_GetUpdateMode

AREngine\_ARStatus HMS\_AREngine\_ARConfig\_GetUpdateMode(const AREngine\_ARSession \*session, const AREngine\_ARConfig \*config, AREngine\_ARUpdateMode \*updateMode)

**Description**

Obtains the current preview update mode.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

config

 | 

Pointer to the configuration object with the target configuration information. For details, please refer to [AREngine\_ARConfig](#gab0b32ef6018535fd30000f4b6d65f619).

 |
| 

updateMode

 | 

Current preview update mode. For details, please refer to [AREngine\_ARUpdateMode](#gabd21cc975ee97b7fb2133af0068ebb5e).

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |

#### \[h2\]HMS\_AREngine\_ARConfig\_SetARType

AREngine\_ARStatus HMS\_AREngine\_ARConfig\_SetARType(const AREngine\_ARSession \*session, AREngine\_ARConfig \*config, AREngine\_ARType type)

**Description**

Sets the AR capability type to use.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

config

 | 

Pointer to the configuration object with the target configuration information. For details, please refer to [AREngine\_ARConfig](#gab0b32ef6018535fd30000f4b6d65f619).

 |
| 

type

 | 

Type of capabilities supported by AR Engine. For details, please refer to [AREngine\_ARType](#ga987888aea7dcaa9abcdb64581c850bf5).

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |
| 

ARENGINE\_ERROR\_UNSUPPORTED\_CONFIGURATION

 | 

Configuration not supported.

 |

#### \[h2\]HMS\_AREngine\_ARConfig\_SetCameraPreviewMode

AREngine\_ARStatus HMS\_AREngine\_ARConfig\_SetCameraPreviewMode(const AREngine\_ARSession \*session, AREngine\_ARConfig \*config, AREngine\_ARPreviewMode mode)

**Description**

Sets the preview mode.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

config

 | 

Pointer to the configuration object with the target configuration information. For details, please refer to [AREngine\_ARConfig](#gab0b32ef6018535fd30000f4b6d65f619).

 |
| 

mode

 | 

Camera preview mode. For details, please refer to [AREngine\_ARPreviewMode](#gadef0f2099b106b872a014ef6551906ae).

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |

#### \[h2\]HMS\_AREngine\_ARConfig\_SetDepthMode

AREngine\_ARStatus HMS\_AREngine\_ARConfig\_SetDepthMode(const AREngine\_ARSession \*session, AREngine\_ARConfig \*config, AREngine\_ARDepthMode depthMode)

**Description**

Sets the depth mode.

**Start version**: 5.0.5(17)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

config

 | 

Pointer to the configuration object with the target configuration information. For details, please refer to [AREngine\_ARConfig](#gab0b32ef6018535fd30000f4b6d65f619).

 |
| 

depthMode

 | 

Depth image mode. For details, please refer to [AREngine\_ARDepthMode](#section12321429115215).

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |

#### \[h2\]HMS\_AREngine\_ARConfig\_SetFocusMode

AREngine\_ARStatus HMS\_AREngine\_ARConfig\_SetFocusMode(const AREngine\_ARSession \*session, AREngine\_ARConfig \*config, AREngine\_ARFocusMode focusMode)

**Description**

Sets the required camera focus mode.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

config

 | 

Pointer to the configuration object with the target configuration information. For details, please refer to [AREngine\_ARConfig](#gab0b32ef6018535fd30000f4b6d65f619).

 |
| 

focusMode

 | 

Focus mode. For details, please refer to [AREngine\_ARFocusMode](#gaf50530faa0d094182a0db0c73b75d875).

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |

#### \[h2\]HMS\_AREngine\_ARConfig\_SetMaxMapSize

AREngine\_ARStatus HMS\_AREngine\_ARConfig\_SetMaxMapSize(const AREngine\_ARSession \*session, AREngine\_ARConfig \*config, uint64\_t maxMapSize)

**Description**

Sets the maximum memory size for storing map data.

If the value you set is indicated as invalid, a valid size closest to the value you set will take effect. The default value of the maximum memory size is 800 MB.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

config

 | 

Pointer to the configuration object with the target configuration information. For details, please refer to [AREngine\_ARConfig](#gab0b32ef6018535fd30000f4b6d65f619).

 |
| 

maxMapSize

 | 

Maximum memory size for storing map data, in MB. The value ranges from 100 MB to 16 GB. You are advised to set the memory size according to the device's memory capacity. Exceeding the hardware limits may result in unexpected errors.

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |

#### \[h2\]HMS\_AREngine\_ARConfig\_SetMeshMode

AREngine\_ARStatus HMS\_AREngine\_ARConfig\_SetMeshMode(const AREngine\_ARSession \*session, AREngine\_ARConfig \*config, AREngine\_ARMeshMode meshMode)

**Description**

Sets the mesh mode.

**Start version**: 5.1.0(18)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

config

 | 

Pointer to the configuration object with the target configuration information. For details, please refer to [AREngine\_ARConfig](#gab0b32ef6018535fd30000f4b6d65f619).

 |
| 

meshMode

 | 

Mesh mode. For details, please refer to [AREngine\_ARMeshMode](#section19436658201620).

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |

#### \[h2\]HMS\_AREngine\_ARConfig\_SetPlaneFindingMode

AREngine\_ARStatus HMS\_AREngine\_ARConfig\_SetPlaneFindingMode(const AREngine\_ARSession \*session, AREngine\_ARConfig \*config, AREngine\_ARPlaneFindingMode planeFindingMode)

**Description**

Sets the required plane finding mode.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

config

 | 

Pointer to the configuration object with the target configuration information. For details, please refer to [AREngine\_ARConfig](#gab0b32ef6018535fd30000f4b6d65f619).

 |
| 

planeFindingMode

 | 

Plane finding mode. For details, please refer to [AREngine\_ARPlaneFindingMode](#gab8e7db52d819359026fc4a82815d3fff).

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |

#### \[h2\]HMS\_AREngine\_ARConfig\_SetPoseMode

AREngine\_ARStatus HMS\_AREngine\_ARConfig\_SetPoseMode(const AREngine\_ARSession \*session, AREngine\_ARConfig \*config, AREngine\_ARPoseMode poseMode)

**Description**

Sets the alignment mode of the pose coordinate system output by the camera.

**Start version**: 5.1.0(18)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

config

 | 

Pointer to the configuration object with the target configuration information. For details, please refer to [AREngine\_ARConfig](#gab0b32ef6018535fd30000f4b6d65f619).

 |
| 

poseMode

 | 

Camera pose mode. For details, please refer to [AREngine\_ARPoseMode](#section1249515330198).

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |

#### \[h2\]HMS\_AREngine\_ARConfig\_SetPowerMode

AREngine\_ARStatus HMS\_AREngine\_ARConfig\_SetPowerMode(const AREngine\_ARSession \*session, AREngine\_ARConfig \*config, AREngine\_ARPowerMode powerMode)

**Description**

Sets the power consumption mode.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

config

 | 

Pointer to the configuration object with the target configuration information. For details, please refer to [AREngine\_ARConfig](#gab0b32ef6018535fd30000f4b6d65f619).

 |
| 

powerMode

 | 

Power consumption mode. For details, please refer to [AREngine\_ARPowerMode](#ga3d925e007e2847e69f22af68ec922507).

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |

#### \[h2\]HMS\_AREngine\_ARConfig\_SetPreviewSize

AREngine\_ARStatus HMS\_AREngine\_ARConfig\_SetPreviewSize(const AREngine\_ARSession \*session, AREngine\_ARConfig \*config, uint32\_t width, uint32\_t height)

**Description**

Sets preview image dimensions. Only a 4:3 aspect ratio is supported. An image exceeding this ratio will default to 1440 x 1080 px.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

config

 | 

Pointer to the configuration object with the target configuration information. For details, please refer to [AREngine\_ARConfig](#gab0b32ef6018535fd30000f4b6d65f619).

 |
| 

width

 | 

Width of the preview image, in pixels. You can call [OH\_CameraManager\_GetSupportedCameraOutputCapability](../../../../../media/camera-kit/c-apis/header-files/camera-manager-h/document.md#oh_cameramanager_getsupportedcameraoutputcapability) to query the dimensions supported by the device.

 |
| 

height

 | 

Height of the preview image, in pixels. You can call [OH\_CameraManager\_GetSupportedCameraOutputCapability](../../../../../media/camera-kit/c-apis/header-files/camera-manager-h/document.md#oh_cameramanager_getsupportedcameraoutputcapability) to query the dimensions supported by the device.

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |

#### \[h2\]HMS\_AREngine\_ARConfig\_SetSemanticDenseMode

AREngine\_ARStatus HMS\_AREngine\_ARConfig\_SetSemanticDenseMode(const AREngine\_ARSession \*session, AREngine\_ARConfig \*config, AREngine\_ARSemanticDenseMode semanticDenseMode)

**Description**

Sets the high-precision geometric reconstruction mode.

**Start version**: 6.0.0(20)

**Parameters**:

| 
Name

 | 

**Description**

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

config

 | 

Pointer to the configuration object with the target configuration information. For details, please refer to [AREngine\_ARConfig](#gab0b32ef6018535fd30000f4b6d65f619).

 |
| 

semanticDenseMode

 | 

High-precision geometric reconstruction mode. For details, please refer to [AREngine\_ARSemanticDenseMode](#section09971756142213).

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |

#### \[h2\]HMS\_AREngine\_ARConfig\_SetSemanticMode

AREngine\_ARStatus HMS\_AREngine\_ARConfig\_SetSemanticMode(const AREngine\_ARSession \*session, AREngine\_ARConfig \*config, AREngine\_ARSemanticMode mode)

**Description**

Sets the required semantic recognition mode.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

config

 | 

Pointer to the configuration object with the target configuration information. For details, please refer to [AREngine\_ARConfig](#gab0b32ef6018535fd30000f4b6d65f619).

 |
| 

mode

 | 

Semantic mode. For details, please refer to [AREngine\_ARSemanticMode](#ga34d3000de29454b99d89406d288d6ed5).

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |

#### \[h2\]HMS\_AREngine\_ARConfig\_SetUpdateMode

AREngine\_ARStatus HMS\_AREngine\_ARConfig\_SetUpdateMode(const AREngine\_ARSession \*session, AREngine\_ARConfig \*config, AREngine\_ARUpdateMode updateMode)

**Description**

Sets the preview update mode.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

config

 | 

Pointer to the configuration object with the target configuration information. For details, please refer to [AREngine\_ARConfig](#gab0b32ef6018535fd30000f4b6d65f619).

 |
| 

updateMode

 | 

Preview update mode. For details, please refer to [AREngine\_ARUpdateMode](#gabd21cc975ee97b7fb2133af0068ebb5e).

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |

#### \[h2\]HMS\_AREngine\_ARConfig\_SetPhotoStreamSize

AREngine\_ARStatus HMS\_AREngine\_ARConfig\_SetPhotoStreamSize(const AREngine\_ARSession \*session, AREngine\_ARConfig \*config, uint32\_t width, uint32\_t height)

**Description**

Sets the resolution of an image captured from the photo stream when [AREngine\_ARImageStreamMode](#section184201559356) is set to **ARENGINE\_IMAGE\_STREAM\_MODE\_PREVIEW\_AND\_PHOTO**. Only resolutions at the aspect ratio 4:3 are supported. If the aspect ratio is not 4:3, the device's maximum resolution at the aspect ratio 4:3 will be automatically used.

**Start version**: 6.0.2(22)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

config

 | 

Pointer to the configuration object with the target configuration information. For details, please refer to [AREngine\_ARConfig](#gab0b32ef6018535fd30000f4b6d65f619).

 |
| 

width

 | 

Width of the photo stream image, in pixels. You can call [OH\_CameraManager\_GetSupportedCameraOutputCapability](../../../../../media/camera-kit/c-apis/header-files/camera-manager-h/document.md#oh_cameramanager_getsupportedcameraoutputcapability) to query the values supported by the device.

 |
| 

height

 | 

Height of the photo stream image, in pixels. You can call [OH\_CameraManager\_GetSupportedCameraOutputCapability](../../../../../media/camera-kit/c-apis/header-files/camera-manager-h/document.md#oh_cameramanager_getsupportedcameraoutputcapability) to query the values supported by the device.

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |

#### \[h2\]HMS\_AREngine\_ARConfig\_SetImageStreamMode

AREngine\_ARStatus HMS\_AREngine\_ARConfig\_SetImageStreamMode(const AREngine\_ARSession \*session, AREngine\_ARConfig \*config, AREngine\_ARImageStreamMode mode)

**Description**

Sets the image stream mode.

**Start version**: 6.0.2(22)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

config

 | 

Pointer to the configuration object with the target configuration information. For details, please refer to [AREngine\_ARConfig](#gab0b32ef6018535fd30000f4b6d65f619).

 |
| 

mode

 | 

Image stream mode. For details, please refer to [AREngine\_ARImageStreamMode](#section184201559356).

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |

#### \[h2\]HMS\_AREngine\_ARConfig\_GetImageStreamMode

AREngine\_ARStatus HMS\_AREngine\_ARConfig\_GetImageStreamMode(const AREngine\_ARSession \*session, AREngine\_ARConfig \*config, AREngine\_ARImageStreamMode \*outMode)

**Description**

Obtains the image stream mode.

**Start version**: 6.0.2(22)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

config

 | 

Pointer to the configuration object with the target configuration information. For details, please refer to [AREngine\_ARConfig](#gab0b32ef6018535fd30000f4b6d65f619).

 |
| 

outMode

 | 

Image stream mode. For details, please refer to [AREngine\_ARImageStreamMode](#section184201559356).

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |

#### \[h2\]HMS\_AREngine\_ARFrame\_AcquireCamera

AREngine\_ARStatus HMS\_AREngine\_ARFrame\_AcquireCamera(const AREngine\_ARSession \*session, const AREngine\_ARFrame \*frame, AREngine\_ARCamera \*\*outCamera)

**Description**

Obtains the camera parameter object of the current frame.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

frame

 | 

Current frame object. For details, please refer to [AREngine\_ARFrame](#gaf35f728a1179ef54a3eba9f1cf021719).

 |
| 

outCamera

 | 

Camera parameter object of the current frame. For details, please refer to [AREngine\_ARCamera](#ga7bdcf1fb36c404d36e09ad70d2545d92).

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |
| 

ARENGINE\_ERROR\_RESOURCE\_EXHAUSTED

 | 

Resource exhausted.

 |

#### \[h2\]HMS\_AREngine\_ARFrame\_AcquireCameraImage

AREngine\_ARStatus HMS\_AREngine\_ARFrame\_AcquireCameraImage(const AREngine\_ARSession \*session, const AREngine\_ARFrame \*frame, AREngine\_ARImage \*\*outImage)

**Description**

Obtains the image of the current frame of the camera.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

frame

 | 

Current frame object. For details, please refer to [AREngine\_ARFrame](#gaf35f728a1179ef54a3eba9f1cf021719).

 |
| 

outImage

 | 

Image object of the current frame. For details, please refer to [AREngine\_ARImage](#gabfee13b0076f2f00b7efdef2717add59).

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |
| 

ARENGINE\_ERROR\_UNSUPPORTED\_CONFIGURATION

 | 

Configuration not supported.

 |

#### \[h2\]HMS\_AREngine\_ARFrame\_AcquireCameraPhotoImage

AREngine\_ARStatus HMS\_AREngine\_ARFrame\_AcquireCameraPhotoImage(const AREngine\_ARSession \*session, const AREngine\_ARFrame \*frame, HMS\_AREngine\_PhotoAvailableCallback photoCallback)

**Description**

Obtains the photo stream image of the current frame.

**Start version**: 6.0.2(22)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

frame

 | 

Current frame object. For details, please refer to [AREngine\_ARFrame](#gaf35f728a1179ef54a3eba9f1cf021719).

 |
| 

photoCallback

 | 

Callback triggered when a photo stream image is output. For details, please refer to [HMS\_AREngine\_PhotoAvailableCallback](#section430673420224).

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |
| 

ARENGINE\_ERROR\_UNSUPPORTED\_CONFIGURATION

 | 

Configuration not supported.

 |
| 

ARENGINE\_ERROR\_FATAL

 | 

Failure.

 |
| 

ARENGINE\_ERROR\_CAMERA\_NOT\_AVAILABLE

 | 

The camera is unavailable.

 |
| 

ARENGINE\_CAMERA\_SERVICE\_FATAL\_ERROR

 | 

The camera service is abnormal.

 |

#### \[h2\]HMS\_AREngine\_ARFrame\_AcquireDepthConfidenceImage

AREngine\_ARStatus HMS\_AREngine\_ARFrame\_AcquireDepthConfidenceImage(const AREngine\_ARSession \*session, const AREngine\_ARFrame \*frame, AREngine\_ARImage \*\*outConfidenceImage)

**Description**

Obtains the depth confidence map of the current frame.

**Start version**: 5.0.5(17)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

frame

 | 

Current frame object. For details, please refer to [AREngine\_ARFrame](#gaf35f728a1179ef54a3eba9f1cf021719).

 |
| 

outConfidenceImage

 | 

Depth confidence map object of the current frame. For details, please refer to [AREngine\_ARImage](#gabfee13b0076f2f00b7efdef2717add59).

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |

#### \[h2\]HMS\_AREngine\_ARFrame\_AcquireDepthImage16Bits

AREngine\_ARStatus HMS\_AREngine\_ARFrame\_AcquireDepthImage16Bits(const AREngine\_ARSession \*session, const AREngine\_ARFrame \*frame, AREngine\_ARImage \*\*outDepthImage)

**Description**

Obtains the depth image of the current frame.

**Start version**: 5.0.5(17)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

frame

 | 

Current frame object. For details, please refer to [AREngine\_ARFrame](#gaf35f728a1179ef54a3eba9f1cf021719).

 |
| 

outDepthImage

 | 

Depth image object of the current frame. For details, please refer to [AREngine\_ARImage](#gabfee13b0076f2f00b7efdef2717add59).

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |

#### \[h2\]HMS\_AREngine\_ARFrame\_AcquirePointCloud

AREngine\_ARStatus HMS\_AREngine\_ARFrame\_AcquirePointCloud(const AREngine\_ARSession \*session, const AREngine\_ARFrame \*frame, AREngine\_ARPointCloud \*\*outPointCloud)

**Description**

Returns the point cloud data of the current frame.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

frame

 | 

Current frame object. For details, please refer to [AREngine\_ARFrame](#gaf35f728a1179ef54a3eba9f1cf021719).

 |
| 

outPointCloud

 | 

Point cloud object of the current frame. For details, please refer to [AREngine\_ARPointCloud](#gacc054cea4851be61b160f32b433737fc).

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |
| 

ARENGINE\_ERROR\_RESOURCE\_EXHAUSTED

 | 

Resource exhausted.

 |

#### \[h2\]HMS\_AREngine\_ARFrame\_AcquireSceneMesh

AREngine\_ARStatus HMS\_AREngine\_ARFrame\_AcquireSceneMesh(const AREngine\_ARSession \*session, const AREngine\_ARFrame \*frame, AREngine\_ARSceneMesh \*\*outSceneMesh)

**Description**

Obtains the mesh information of the current frame.

**Start version**: 5.1.0(18)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

frame

 | 

Current frame object. For details, please refer to [AREngine\_ARFrame](#gaf35f728a1179ef54a3eba9f1cf021719).

 |
| 

outSceneMesh

 | 

Mesh information of the current frame. For details, please refer to [AREngine\_ARSceneMesh](#section543212520614).

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |
| 

ARENGINE\_ERROR\_RESOURCE\_EXHAUSTED

 | 

Resource exhausted.

 |

#### \[h2\]HMS\_AREngine\_ARFrame\_AcquireSemanticDenseData

AREngine\_ARStatus HMS\_AREngine\_ARFrame\_AcquireSemanticDenseData(const AREngine\_ARSession \*session, const AREngine\_ARFrame \*frame, AREngine\_ARSemanticDenseData \*\*outSemanticDenseData)

**Description**

Obtains the high-precision geometric reconstruction object data of the current frame.

**Start version**: 6.0.0(20)

**Parameters**:

| 
Name

 | 

**Description**

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

frame

 | 

Current frame object. For details, please refer to [AREngine\_ARFrame](#gaf35f728a1179ef54a3eba9f1cf021719).

 |
| 

outSemanticDenseData

 | 

High-precision geometric reconstruction object data of the current frame. For details, please refer to [AREngine\_ARSemanticDenseData](#section1410813229144).

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |
| 

ARENGINE\_ERROR\_RESOURCE\_EXHAUSTED

 | 

Resource exhausted.

 |

#### \[h2\]HMS\_AREngine\_ARFrame\_Create

AREngine\_ARStatus HMS\_AREngine\_ARFrame\_Create(const AREngine\_ARSession \*session, AREngine\_ARFrame \*\*outFrame)

**Description**

Creates an [AREngine\_ARFrame](#gaf35f728a1179ef54a3eba9f1cf021719) object and stores the pointer in _\*_**outFrame**.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

outFrame

 | 

Current frame object. For details, please refer to [AREngine\_ARFrame](#gaf35f728a1179ef54a3eba9f1cf021719).

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |
| 

ARENGINE\_ERROR\_RESOURCE\_EXHAUSTED

 | 

Resource exhausted.

 |

#### \[h2\]HMS\_AREngine\_ARFrame\_Destroy

void HMS\_AREngine\_ARFrame\_Destroy(AREngine\_ARFrame \*frame)

**Description**

Deletes the current [AREngine\_ARFrame](#gaf35f728a1179ef54a3eba9f1cf021719) object.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

frame

 | 

Current frame object to be destroyed. For details, please refer to [AREngine\_ARFrame](#gaf35f728a1179ef54a3eba9f1cf021719).

 |

#### \[h2\]HMS\_AREngine\_ARFrame\_GetDisplayGeometryChanged

AREngine\_ARStatus HMS\_AREngine\_ARFrame\_GetDisplayGeometryChanged(const AREngine\_ARSession \*session, const AREngine\_ARFrame \*frame, int32\_t \*outGeometryChangeState)

**Description**

Obtains whether the display (length, width, and rotation) changes.

If so, you need to call [HMS\_AREngine\_ARFrame\_TransformDisplayUvCoords](#ga4c7699abab9b82369c0d42b496667fc7) again to obtain the correct coordinates of the texture map. If the return value of **outGeometryChangeState** is **0**, no changes have occurred. Otherwise, changes have occurred.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

frame

 | 

Current frame object. For details, please refer to [AREngine\_ARFrame](#gaf35f728a1179ef54a3eba9f1cf021719).

 |
| 

outGeometryChangeState

 | 

Result indicating whether the display (length, width, and rotation) changes. Value **0** indicates that no change has occurred. Other values indicate that changes have occurred.

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |

#### \[h2\]HMS\_AREngine\_ARFrame\_GetTimestamp

AREngine\_ARStatus HMS\_AREngine\_ARFrame\_GetTimestamp(const AREngine\_ARSession \*session, const AREngine\_ARFrame \*frame, int64\_t \*outTimestampNs)

**Description**

Obtains the timestamp information (in nanoseconds) of the current frame.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

frame

 | 

Current frame object. For details, please refer to [AREngine\_ARFrame](#gaf35f728a1179ef54a3eba9f1cf021719).

 |
| 

outTimestampNs

 | 

Timestamp information.

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |

#### \[h2\]HMS\_AREngine\_ARFrame\_GetUpdatedTrackables

AREngine\_ARStatus HMS\_AREngine\_ARFrame\_GetUpdatedTrackables(const AREngine\_ARSession \*session, const AREngine\_ARFrame \*frame, AREngine\_ARTrackableType filterType, AREngine\_ARTrackableList \* outTrackableList)

**Description**

Obtains the updated trackable object of the specified type after [HMS\_AREngine\_ARSession\_Update](#ga1d1cacf372a8011a439f0e4e76994259) is called.

For details about trackable object types, please refer to [AREngine\_ARTrackableType](#ga993948a19fd2bdfa5b946e13a8d4fe3d).

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

frame

 | 

Current frame object. For details, please refer to [AREngine\_ARFrame](#gaf35f728a1179ef54a3eba9f1cf021719).

 |
| 

filterType

 | 

Type of the trackable object to be returned. For details, please refer to [AREngine\_ARTrackableType](#ga993948a19fd2bdfa5b946e13a8d4fe3d).

 |
| 

outTrackableList

 | 

List of trackable objects. For details, please refer to [AREngine\_ARTrackableList](#gae69e4963b595036fc5e6119a055bb205).

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |

#### \[h2\]HMS\_AREngine\_ARFrame\_HitTest

AREngine\_ARStatus HMS\_AREngine\_ARFrame\_HitTest(const AREngine\_ARSession \*session, const AREngine\_ARFrame \*frame, float pixelX, float pixelY, AREngine\_ARHitResultList \*hitResultList)

**Description**

Casts a ray from the camera, with the direction of the ray determined by the points (**pixelX**, **pixelY**) in the preview area. **pixelX** and **pixelY** can be obtained through the XComponent's [DispatchTouchEvent](../../../../../application-framework/arkui/c-api/structs/oh-nativexcomponent-callback/document.md#dispatchtouchevent) event.

The ray collides with the plane, mesh, or the points in the point cloud tracked by the system (if the point cloud is recognized), resulting in intersections and hit results. The intersections are sorted by their distance from the device, from closest to farthest, and stored in a list. (pixelX, pixelY) indicate the coordinates of a pixel in the preview area.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

frame

 | 

Current frame object. For details, please refer to [AREngine\_ARFrame](#gaf35f728a1179ef54a3eba9f1cf021719).

 |
| 

pixelX

 | 

X-axis coordinate, which is obtained via [XComponent](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/napi-xcomponent-guidelines).

 |
| 

pixelY

 | 

Y-axis coordinate, which is obtained via [XComponent](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/napi-xcomponent-guidelines).

 |
| 

hitResultList

 | 

Hit result list. For details, please refer to [AREngine\_ARHitResultList](#ga1f2369453412bd4d77ab8f5aa2d52bb3).

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |
| 

ARENGINE\_ERROR\_FATAL

 | 

Failure.

 |

#### \[h2\]HMS\_AREngine\_ARFrame\_TransformDisplayUvCoords

AREngine\_ARStatus HMS\_AREngine\_ARFrame\_TransformDisplayUvCoords(const AREngine\_ARSession \*session, const AREngine\_ARFrame \*frame, int32\_t elementSize, const float \*uvsIn, float \*uvsOut)

**Description**

Converts the texture coordinates so that the background image captured by the camera can be correctly displayed.

You need to call this method to convert the texture coordinates only when **outGeometryChangeState** returned by [HMS\_AREngine\_ARFrame\_GetDisplayGeometryChanged](#ga4fb55932c19ef9c49523a0a5385a9242) is not 0, or when you have set a new display size by calling [HMS\_AREngine\_ARSession\_SetDisplayGeometry](#ga3f23bf747def8303c3fb261a9e9a2286).

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

frame

 | 

Current frame object. For details, please refer to [AREngine\_ARFrame](#gaf35f728a1179ef54a3eba9f1cf021719).

 |
| 

elementSize

 | 

Number of texture coordinates to be converted. The value must be a multiple of 2 (uv coordinates). The minimum value is 0.

 |
| 

uvsIn

 | 

Original input uv coordinate. The array size is **elementSize** and cannot be **nullptr**.

 |
| 

uvsOut

 | 

Converted uv coordinate. The array size is **elementSize** and cannot be **nullptr**.

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |
| 

ARENGINE\_ERROR\_FATAL

 | 

Failure.

 |

#### \[h2\]HMS\_AREngine\_ARHitResult\_AcquireNewAnchor

AREngine\_ARStatus HMS\_AREngine\_ARHitResult\_AcquireNewAnchor(AREngine\_ARSession \*session, AREngine\_ARHitResult \*hitResult, AREngine\_ARAnchor \*\*outAnchor)

**Description**

Creates an anchor at the hit position.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

hitResult

 | 

Hit testing result object. For details, please refer to [AREngine\_ARHitResult](#gaeb304c8b21122eb7ffda7403316a3507).

 |
| 

outAnchor

 | 

Newly created anchor object. For details, please refer to [AREngine\_ARAnchor](#ga76c16c9d68ba9a3b76f1869c60d8ca1d).

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |
| 

ARENGINE\_ERROR\_RESOURCE\_EXHAUSTED

 | 

Resource exhausted.

 |

#### \[h2\]HMS\_AREngine\_ARHitResult\_AcquireTrackable

AREngine\_ARStatus HMS\_AREngine\_ARHitResult\_AcquireTrackable(const AREngine\_ARSession \*session, const AREngine\_ARHitResult \*hitResult, AREngine\_ARTrackable \*\*outTrackable)

**Description**

Obtains the trackable object that is hit.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

hitResult

 | 

Hit testing result object. For details, please refer to [AREngine\_ARHitResult](#gaeb304c8b21122eb7ffda7403316a3507).

 |
| 

outTrackable

 | 

Trackable object that is hit. For details, please refer to [AREngine\_ARTrackable](#ga54808ebd1a6ed026494acdd945c4f970).

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |

#### \[h2\]HMS\_AREngine\_ARHitResult\_Create

AREngine\_ARStatus HMS\_AREngine\_ARHitResult\_Create(const AREngine\_ARSession \*session, AREngine\_ARHitResult \*\*outHitResult)

**Description**

Creates an empty hit testing result object.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

outHitResult

 | 

Hit testing result object to be created. For details, please refer to [AREngine\_ARHitResult](#gaeb304c8b21122eb7ffda7403316a3507).

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |
| 

ARENGINE\_ERROR\_RESOURCE\_EXHAUSTED

 | 

Resource exhausted.

 |

#### \[h2\]HMS\_AREngine\_ARHitResult\_Destroy

void HMS\_AREngine\_ARHitResult\_Destroy(AREngine\_ARHitResult \*hitResult)

**Description**

Releases the list of hit testing result objects, as well as all hit testing result objects in the list.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

hitResult

 | 

Hit testing result object to be released. For details, please refer to [AREngine\_ARHitResult](#gaeb304c8b21122eb7ffda7403316a3507).

 |

#### \[h2\]HMS\_AREngine\_ARHitResult\_GetDistance

AREngine\_ARStatus HMS\_AREngine\_ARHitResult\_GetDistance(const AREngine\_ARSession \*session, const AREngine\_ARHitResult \*hitResult, float \*outDistance)

**Description**

Returns the distance from the camera to the hit location, in meters.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

hitResult

 | 

Hit testing result object. For details, please refer to [AREngine\_ARHitResult](#gaeb304c8b21122eb7ffda7403316a3507).

 |
| 

outDistance

 | 

Returns the distance from the camera to the hit object, in meters.

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |

#### \[h2\]HMS\_AREngine\_ARHitResult\_GetHitPose

AREngine\_ARStatus HMS\_AREngine\_ARHitResult\_GetHitPose(const AREngine\_ARSession \*session, const AREngine\_ARHitResult \*hitResult, AREngine\_ARPose \*outPose)

**Description**

Obtains the pose of an intersection.

The pose's translation component corresponds to the intersection's coordinates in the world coordinate system, while its rotation component varies according to the type of the intersection (such as the intersection with a plane or a point cloud).

1.  When a ray collides with the plane, in the local coordinate system: X+ is perpendicular to the ray and parallel to the tracked plane; Y+ is the normal vector of the tracked plane; Z+ is parallel to the plane and roughly points to the camera.
2.  When a ray collides with points in a point cloud, the system attempts to estimate a plane with the point cloud of the hit area.
    1.  If [HMS\_AREngine\_ARPoint\_GetOrientationMode](#gad869ed2a4ac6409bf94c768d9d1d8127) returns [ARENGINE\_POINT\_ORIENTATION\_ESTIMATED\_SURFACE\_NORMAL](#ga0e2893593f4372954fd97519e0a63855), X+ is perpendicular to the ray and parallel to the tracked plane, Y+ is the normal vector of the tracked plane, and Z+ is parallel to the plane and roughly points to the camera.
    2.  If [ARENGINE\_POINT\_ORIENTATION\_INITIALIZED\_TO\_IDENTITY](#ga0e2893593f4372954fd97519e0a63855) is returned, the orientation of the coordinates will not change with the plane's angle. X+ is perpendicular to the ray and points to the right (from the device's perspective), Y+ points upward, and Z+ roughly points to the camera. For details, please refer to the orientation mode definition.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

hitResult

 | 

Hit testing result object. For details, please refer to [AREngine\_ARHitResult](#gaeb304c8b21122eb7ffda7403316a3507).

 |
| 

outPose

 | 

Intersection pose. For details, please refer to [AREngine\_ARPose](#gab2fa63142ebfb09f0c2ddf88cdb86604).

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |

#### \[h2\]HMS\_AREngine\_ARHitResultList\_Create

AREngine\_ARStatus HMS\_AREngine\_ARHitResultList\_Create(const AREngine\_ARSession \*session, AREngine\_ARHitResultList \*\*outHitResultList)

**Description**

Creates a list of hit testing result objects.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

outHitResultList

 | 

List of hit testing result objects to be created. For details, please refer to [AREngine\_ARHitResultList](#ga1f2369453412bd4d77ab8f5aa2d52bb3).

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |
| 

ARENGINE\_ERROR\_RESOURCE\_EXHAUSTED

 | 

Resource exhausted.

 |

#### \[h2\]HMS\_AREngine\_ARHitResultList\_Destroy

void HMS\_AREngine\_ARHitResultList\_Destroy(AREngine\_ARHitResultList \*hitResultList)

**Description**

Releases the list of hit testing result objects, as well as all hit testing result objects in the list.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

hitResultList

 | 

List of hit testing result objects to be released. For details, please refer to [AREngine\_ARHitResultList](#ga1f2369453412bd4d77ab8f5aa2d52bb3).

 |

#### \[h2\]HMS\_AREngine\_ARHitResultList\_GetItem

AREngine\_ARStatus HMS\_AREngine\_ARHitResultList\_GetItem(const AREngine\_ARSession \*session, const AREngine\_ARHitResultList \*hitResultList, int32\_t index, AREngine\_ARHitResult \*outHitResult)

**Description**

Obtains the hit testing result object at a specific index from the list of hit testing results.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

hitResultList

 | 

List of hit testing result objects. For details, please refer to [AREngine\_ARHitResultList](#ga1f2369453412bd4d77ab8f5aa2d52bb3).

 |
| 

index

 | 

Index of the hit testing result object to be obtained.

 |
| 

outHitResult

 | 

Hit testing result object to be obtained. For details, please refer to [AREngine\_ARHitResult](#gaeb304c8b21122eb7ffda7403316a3507).

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |
| 

ARENGINE\_ERROR\_FATAL

 | 

Failure.

 |

#### \[h2\]HMS\_AREngine\_ARHitResultList\_GetSize

AREngine\_ARStatus HMS\_AREngine\_ARHitResultList\_GetSize(const AREngine\_ARSession \*session, const AREngine\_ARHitResultList \*hitResultList, int32\_t \*outSize)

**Description**

Obtains the number of objects in the list of hit testing result objects.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

hitResultList

 | 

List of hit testing result objects. For details, please refer to [AREngine\_ARHitResultList](#ga1f2369453412bd4d77ab8f5aa2d52bb3).

 |
| 

outSize

 | 

Returns the list size.

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |

#### \[h2\]HMS\_AREngine\_ARImage\_GetFormat

AREngine\_ARStatus HMS\_AREngine\_ARImage\_GetFormat(const AREngine\_ARSession \*session, const AREngine\_ARImage \*image, AREngine\_ARImageFormat \*outFormat)

**Description**

Obtains the image format of the current frame.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

image

 | 

Input image data. For details, please refer to [AREngine\_ARImage](#gabfee13b0076f2f00b7efdef2717add59).

 |
| 

outFormat

 | 

Image format of the current frame.

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |
| 

ARENGINE\_ERROR\_FATAL

 | 

Failure.

 |

#### \[h2\]HMS\_AREngine\_ARImage\_GetHeight

AREngine\_ARStatus HMS\_AREngine\_ARImage\_GetHeight(const AREngine\_ARSession \*session, const AREngine\_ARImage \*image, int32\_t \*outHeight)

**Description**

Obtains the image height of the current frame.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

image

 | 

Image object of the current frame. For details, please refer to [AREngine\_ARImage](#gabfee13b0076f2f00b7efdef2717add59).

 |
| 

outHeight

 | 

Height of the image of the current frame, in pixels.

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |
| 

ARENGINE\_ERROR\_FATAL

 | 

Failure.

 |

#### \[h2\]HMS\_AREngine\_ARImage\_GetNativeBuffer

AREngine\_ARStatus HMS\_AREngine\_ARImage\_GetNativeBuffer(const AREngine\_ARSession \*session, const AREngine\_ARImage \*image, OH\_NativeBuffer \*\*outNativeBuffer)

**Description**

Obtains the NativeBuffer data of the current frame's image object.

**Start version**: 6.0.0(20)

**Parameters**:

| 
Name

 | 

**Description**

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

image

 | 

Image object of the current frame. For details, please refer to [AREngine\_ARImage](#gabfee13b0076f2f00b7efdef2717add59).

 |
| 

outNativeBuffer

 | 

NativeBuffer data of the current frame.

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |
| 

ARENGINE\_ERROR\_FATAL

 | 

Failure.

 |
| 

ARENGINE\_ERROR\_NATIVEBUFFER\_CREATE\_FAILED

 | 

Failed to create NativeBuffer.

 |
| 

ARENGINE\_ERROR\_NATIVEBUFFER\_WRITE\_FAILED

 | 

Failed to write to NativeBuffer.

 |

#### \[h2\]HMS\_AREngine\_ARImage\_GetPlaneCount

AREngine\_ARStatus HMS\_AREngine\_ARImage\_GetPlaneCount(const AREngine\_ARSession \*session, const AREngine\_ARImage \*image, int32\_t \*outCount)

**Description**

Obtains the number of planes in the current frame.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

image

 | 

Image object of the current frame. For details, please refer to [AREngine\_ARImage](#gabfee13b0076f2f00b7efdef2717add59).

 |
| 

outCount

 | 

Number of planes in the current frame.

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |
| 

ARENGINE\_ERROR\_FATAL

 | 

Failure.

 |

#### \[h2\]HMS\_AREngine\_ARImage\_GetPlaneData

AREngine\_ARStatus HMS\_AREngine\_ARImage\_GetPlaneData(const AREngine\_ARSession \*session, const AREngine\_ARImage \*image, int32\_t planeIndex, const uint8\_t \*\*outData, int32\_t \*outLength)

**Description**

Obtains the plane data in the current frame.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

image

 | 

Image object of the current frame. For details, please refer to [AREngine\_ARImage](#gabfee13b0076f2f00b7efdef2717add59).

 |
| 

planeIndex

 | 

Plane index. The value ranges from **0** to **_n_\-1**, where **_n_** is the number of planes in the image.

 |
| 

outData

 | 

Pointer to the current image data.

 |
| 

outLength

 | 

Length of the current image (in bytes).

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |
| 

ARENGINE\_ERROR\_FATAL

 | 

Failure.

 |

#### \[h2\]HMS\_AREngine\_ARImage\_GetPlanePixelStride

AREngine\_ARStatus HMS\_AREngine\_ARImage\_GetPlanePixelStride(const AREngine\_ARSession \*session, const AREngine\_ARImage \*image, int32\_t planeIndex, int32\_t \*outPixelStride)

**Description**

Obtains the distance between the start points of two consecutive pixels in an image, in bytes. The pixel stride is always greater than 0.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

image

 | 

Image object of the current frame. For details, please refer to [AREngine\_ARImage](#gabfee13b0076f2f00b7efdef2717add59).

 |
| 

planeIndex

 | 

Plane index. The value ranges from **0** to **_n_\-1**, where **_n_** is the number of planes in the image.

 |
| 

outPixelStride

 | 

Image stride (in bytes).

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |
| 

ARENGINE\_ERROR\_FATAL

 | 

Failure.

 |

#### \[h2\]HMS\_AREngine\_ARImage\_GetPlaneRowStride

AREngine\_ARStatus HMS\_AREngine\_ARImage\_GetPlaneRowStride(const AREngine\_ARSession \*session, const AREngine\_ARImage \*image, int32\_t planeIndex, int32\_t \*outRowStride)

**Description**

Obtains the number of bytes between the start positions of two consecutive pixel lines in an image. The line spacing is always greater than 0.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

image

 | 

Image object of the current frame. For details, please refer to [AREngine\_ARImage](#gabfee13b0076f2f00b7efdef2717add59).

 |
| 

planeIndex

 | 

Plane index. The value ranges from **0** to **_n_\-1**, where **_n_** is the number of planes in the image.

 |
| 

outRowStride

 | 

Row stride (in bytes).

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |
| 

ARENGINE\_ERROR\_FATAL

 | 

Failure.

 |

#### \[h2\]HMS\_AREngine\_ARImage\_GetTimestamp

AREngine\_ARStatus HMS\_AREngine\_ARImage\_GetTimestamp(const AREngine\_ARSession \*session, const AREngine\_ARImage \*image, int64\_t \*outTimestamp)

**Description**

Obtains the timestamp of an image.

Timestamps are typically monotonically increasing and measured in nanoseconds. The specific meaning and time base of the timestamp depend on the image source. Timestamps of images from different sources may have different time bases, so they should not be compared with each other.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

image

 | 

Image object of the current frame. For details, please refer to [AREngine\_ARImage](#gabfee13b0076f2f00b7efdef2717add59).

 |
| 

outTimestamp

 | 

Timestamp of an image (in nanoseconds).

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |
| 

ARENGINE\_ERROR\_FATAL

 | 

Failure.

 |

#### \[h2\]HMS\_AREngine\_ARImage\_GetWidth

AREngine\_ARStatus HMS\_AREngine\_ARImage\_GetWidth(const AREngine\_ARSession \*session, const AREngine\_ARImage \*image, int32\_t \*outWidth)

**Description**

Obtains the image width of the current frame.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

image

 | 

Image object of the current frame. For details, please refer to [AREngine\_ARImage](#gabfee13b0076f2f00b7efdef2717add59).

 |
| 

outWidth

 | 

Width of the image of the current frame, in pixels.

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |
| 

ARENGINE\_ERROR\_FATAL

 | 

Failure.

 |

#### \[h2\]HMS\_AREngine\_ARImage\_Release

void HMS\_AREngine\_ARImage\_Release(AREngine\_ARImage \*image)

**Description**

Releases the image object of the current frame, that is, the object created by [HMS\_AREngine\_ARFrame\_AcquireCameraImage](#gad5619c3cbd2b9ea0cfeff22b72f8d81d).

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

image

 | 

Image object of the current frame to be released. For details, please refer to [AREngine\_ARImage](#gabfee13b0076f2f00b7efdef2717add59).

 |

#### \[h2\]HMS\_AREngine\_ARPlane\_AcquireSubsumedBy

AREngine\_ARStatus HMS\_AREngine\_ARPlane\_AcquireSubsumedBy(const AREngine\_ARSession \*session, const AREngine\_ARPlane \*plane, AREngine\_ARPlane \*\*outSubsumedBy)

**Description**

Obtains the parent plane of a plane (a parent plane is generated when a plane is merged with another one). If there is no parent plane, **NULL** is returned.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

plane

 | 

Plane object to be processed. For details, please refer to [AREngine\_ARPlane](#ga76f9bdb23634312b8488fcbaff4aa9b5).

 |
| 

outSubsumedBy

 | 

Parent plane object of a specific plane. For details, please refer to [AREngine\_ARPlane](#ga76f9bdb23634312b8488fcbaff4aa9b5).

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |

#### \[h2\]HMS\_AREngine\_ARPlane\_GetCenterPose

AREngine\_ARStatus HMS\_AREngine\_ARPlane\_GetCenterPose(const AREngine\_ARSession \*session, const AREngine\_ARPlane \*plane, AREngine\_ARPose \*outPose)

**Description**

Obtains the pose information for the conversion from the local coordinate system of a plane to the world coordinate system.

In the plane's local coordinate system (right-handed): The origin is at the center of the plane's bounding rectangle; the x-axis is along the longer edge, the z-axis is along the shorter edge, and Y+ indicates the plane's normal vector.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

plane

 | 

Plane object to be processed. For details, please refer to [AREngine\_ARPlane](#ga76f9bdb23634312b8488fcbaff4aa9b5).

 |
| 

outPose

 | 

Pose information for the conversion from the local coordinate system of a plane to the world coordinate system. For details, please refer to [AREngine\_ARPose](#gab2fa63142ebfb09f0c2ddf88cdb86604).

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |

#### \[h2\]HMS\_AREngine\_ARPlane\_GetExtentX

AREngine\_ARStatus HMS\_AREngine\_ARPlane\_GetExtentX(const AREngine\_ARSession \*session, const AREngine\_ARPlane \*plane, float \*outExtentX)

**Description**

Obtains the length of the plane's bounding rectangle along the X axis of the plane's local coordinate system, such as the width of the rectangle.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

plane

 | 

Plane object to be processed. For details, please refer to [AREngine\_ARPlane](#ga76f9bdb23634312b8488fcbaff4aa9b5).

 |
| 

outExtentX

 | 

Length of the plane's bounding rectangle along the X axis of the plane's local coordinate system, in meters.

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |

#### \[h2\]HMS\_AREngine\_ARPlane\_GetExtentZ

AREngine\_ARStatus HMS\_AREngine\_ARPlane\_GetExtentZ(const AREngine\_ARSession \*session, const AREngine\_ARPlane \*plane, float \*outExtentZ)

**Description**

Obtains the length of the plane's bounding rectangle along the Z axis of the plane's local coordinate system, such as the height of the rectangle.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

plane

 | 

Plane object to be processed. For details, please refer to [AREngine\_ARPlane](#ga76f9bdb23634312b8488fcbaff4aa9b5).

 |
| 

outExtentZ

 | 

Length of the plane's bounding rectangle along the Z axis of the plane's local coordinate system, in meters.

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |

#### \[h2\]HMS\_AREngine\_ARPlane\_GetLabel

AREngine\_ARStatus HMS\_AREngine\_ARPlane\_GetLabel(const AREngine\_ARSession \*session, const AREngine\_ARPlane \*plane, AREngine\_ARSemanticPlaneLabel \*label)

**Description**

Obtains the semantic type of a plane, such as desktop and floor.

You need to use [HMS\_AREngine\_ARConfig\_SetSemanticMode](#gaae87c1ef02b6e9bab123fae2086da248) to enable the semantic recognition mode.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

plane

 | 

Plane object to be processed. For details, please refer to [AREngine\_ARPlane](#ga76f9bdb23634312b8488fcbaff4aa9b5).

 |
| 

label

 | 

Semantic type of the current plane. For details, please refer to [AREngine\_ARSemanticPlaneLabel](#gafbb6b69fefdc417ba6437ce2fe587cb1).

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |

#### \[h2\]HMS\_AREngine\_ARPlane\_GetPolygon

AREngine\_ARStatus HMS\_AREngine\_ARPlane\_GetPolygon(const AREngine\_ARSession \*session, const AREngine\_ARPlane \*plane, float \*outPolygonXz, int32\_t polygonSize)

**Description**

Obtains the 2D vertex array of the detected plane, in the format of \[x1, z1, x2, z2, ...\].

These values are defined in the x-z plane of the plane's local coordinate system and must be converted to the world coordinate system through [HMS\_AREngine\_ARPlane\_GetCenterPose](#gabbb03027afb984be8542d00d2eebd063).

Note: The returned coordinates \[x1, z1, x2, z2, ...\] in the vertical plane are also the coordinates in the local coordinate system, which should be converted to the world coordinate system through [HMS\_AREngine\_ARPlane\_GetCenterPose](#gabbb03027afb984be8542d00d2eebd063).

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

plane

 | 

Plane object to be processed. For details, please refer to [AREngine\_ARPlane](#ga76f9bdb23634312b8488fcbaff4aa9b5).

 |
| 

outPolygonXz

 | 

Array consisting of 2D vertices of the detected plane.

 |
| 

polygonSize

 | 

Size of the 2D vertex array, which is obtained through [HMS\_AREngine\_ARPlane\_GetPolygonSize](#ga98760556eee2a4a69c33699b7ce3edc6).

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |

#### \[h2\]HMS\_AREngine\_ARPlane\_GetPolygonSize

AREngine\_ARStatus HMS\_AREngine\_ARPlane\_GetPolygonSize(const AREngine\_ARSession \*session, const AREngine\_ARPlane \*plane, int32\_t \*outPolygonSize)

**Description**

Obtains the size of the 2D vertex array of the detected plane.

This function is used together with [HMS\_AREngine\_ARPlane\_GetPolygon](#ga3537ce62e6a92dcdbddff0f39de0fae3).

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

plane

 | 

Plane object to be processed. For details, please refer to [AREngine\_ARPlane](#ga76f9bdb23634312b8488fcbaff4aa9b5).

 |
| 

outPolygonSize

 | 

Size of a 2D vertex array.

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |

#### \[h2\]HMS\_AREngine\_ARPlane\_GetType

AREngine\_ARStatus HMS\_AREngine\_ARPlane\_GetType(const AREngine\_ARSession \*session, const AREngine\_ARPlane \*plane, AREngine\_ARPlaneType \*outPlaneType)

**Description**

Obtains the plane type.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

plane

 | 

Plane object to be processed. For details, please refer to [AREngine\_ARPlane](#ga76f9bdb23634312b8488fcbaff4aa9b5).

 |
| 

outPlaneType

 | 

Plane type. For details, please refer to [AREngine\_ARPlaneType](#ga895db37a92155584c5448bee30a8beab).

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |

#### \[h2\]HMS\_AREngine\_ARPlane\_IsPoseInExtents

AREngine\_ARStatus HMS\_AREngine\_ARPlane\_IsPoseInExtents(const AREngine\_ARSession \*session, const AREngine\_ARPlane \*plane, const AREngine\_ARPose \*pose, int32\_t \*outPoseInExtents)

**Description**

Checks whether a pose is within the plane's bounding rectangle.

A none-zero value is returned if the input pose (obtained through [HMS\_AREngine\_ARHitResult\_GetHitPose](#ga8beaa085410712425041e81f9bc6aa09)) is within the plane's bounding rectangle.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

plane

 | 

Plane object to be processed. For details, please refer to [AREngine\_ARPlane](#ga76f9bdb23634312b8488fcbaff4aa9b5).

 |
| 

pose

 | 

Pose information. For details, please refer to [AREngine\_ARPose](#gab2fa63142ebfb09f0c2ddf88cdb86604).

 |
| 

outPoseInExtents

 | 

Result indicating whether the pose is within the plane's bounding rectangle. Value **0** indicates that it is out of the range, and other values indicate that it is within the range.

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |

#### \[h2\]HMS\_AREngine\_ARPlane\_IsPoseInPolygon

AREngine\_ARStatus HMS\_AREngine\_ARPlane\_IsPoseInPolygon(const AREngine\_ARSession \*session, const AREngine\_ARPlane \*plane, const AREngine\_ARPose \*pose, int32\_t \*outPoseInPolygon)

**Description**

Checks whether a pose is within the plane's bounding polygon.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

plane

 | 

Plane object to be processed. For details, please refer to [AREngine\_ARPlane](#ga76f9bdb23634312b8488fcbaff4aa9b5).

 |
| 

pose

 | 

Pose information. For details, please refer to [AREngine\_ARPose](#gab2fa63142ebfb09f0c2ddf88cdb86604).

 |
| 

outPoseInPolygon

 | 

Result indicating whether the pose is within the plane's bounding polygon. Value **0** indicates that it is out of the range, and other values indicate that it is within the range.

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |

#### \[h2\]HMS\_AREngine\_ARPoint\_GetOrientationMode

AREngine\_ARStatus HMS\_AREngine\_ARPoint\_GetOrientationMode(const AREngine\_ARSession \*session, const AREngine\_ARPoint \*point, AREngine\_ARPointOrientationMode \*outOrientationMode)

**Description**

Obtains the orientation mode of an input point.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

point

 | 

Input point object. For details, please refer to [AREngine\_ARPoint](#gac7b6923d92487d68e77543dd223364d6).

 |
| 

outOrientationMode

 | 

Orientation mode of an input point. For details, please refer to [AREngine\_ARPointOrientationMode](#ga0e2893593f4372954fd97519e0a63855).

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |

#### \[h2\]HMS\_AREngine\_ARPoint\_GetPose

AREngine\_ARStatus HMS\_AREngine\_ARPoint\_GetPose(const AREngine\_ARSession \*session, const AREngine\_ARPoint \*point, AREngine\_ARPose \*outPose)

**Description**

Obtains the pose information of an input point.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

point

 | 

Input point object. For details, please refer to [AREngine\_ARPoint](#gac7b6923d92487d68e77543dd223364d6).

 |
| 

outPose

 | 

Pose information of the input point. For details, please refer to [AREngine\_ARPose](#gab2fa63142ebfb09f0c2ddf88cdb86604).

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |

#### \[h2\]HMS\_AREngine\_ARPointCloud\_GetData

AREngine\_ARStatus HMS\_AREngine\_ARPointCloud\_GetData(const AREngine\_ARSession \*session, const AREngine\_ARPointCloud \*pointCloud, const float \*\*outPointCloudData)

**Description**

Obtains the coordinates of all points in a point cloud, as well as their confidence array.

The coordinates are in the world coordinate system and are right-handed coordinates. You can obtain the point cloud object by calling [HMS\_AREngine\_ARFrame\_AcquirePointCloud](#ga877f7fc9d9c303f1fd8efb00ec383b34).

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

pointCloud

 | 

Point cloud object. For details, please refer to [AREngine\_ARPointCloud](#gacc054cea4851be61b160f32b433737fc).

 |
| 

outPointCloudData

 | 

Coordinates of all points in a point cloud, as well as their confidence array, in the format \[x0, y0, z0, c0, x1, y1, z1, c1, x2...\].

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |

#### \[h2\]HMS\_AREngine\_ARPointCloud\_GetNumberOfPoints

AREngine\_ARStatus HMS\_AREngine\_ARPointCloud\_GetNumberOfPoints(const AREngine\_ARSession \*session, const AREngine\_ARPointCloud \*pointCloud, int32\_t \*outNumberOfPoints)

**Description**

Obtains the coordinates of all points in a point cloud, as well as their confidence array size.

This function is used together with [HMS\_AREngine\_ARPointCloud\_GetData](#ga4061cacb3f3ce45e529acb9afbcdc5ce).

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

pointCloud

 | 

Point cloud object. For details, please refer to [AREngine\_ARPointCloud](#gacc054cea4851be61b160f32b433737fc).

 |
| 

outNumberOfPoints

 | 

Coordinates of all points in a point cloud, as well as their confidence array size.

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |

#### \[h2\]HMS\_AREngine\_ARPointCloud\_GetTimestamp

AREngine\_ARStatus HMS\_AREngine\_ARPointCloud\_GetTimestamp(const AREngine\_ARSession \*session, const AREngine\_ARPointCloud \*pointCloud, int64\_t \*outTimestampNs)

**Description**

Obtains the timestamp when the current feature point cloud is detected, in nanoseconds.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

pointCloud

 | 

Point cloud object. For details, please refer to [AREngine\_ARPointCloud](#gacc054cea4851be61b160f32b433737fc).

 |
| 

outTimestampNs

 | 

Timestamp when the current point cloud is detected.

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |

#### \[h2\]HMS\_AREngine\_ARPointCloud\_Release

void HMS\_AREngine\_ARPointCloud\_Release(AREngine\_ARPointCloud \*pointCloud)

**Description**

Releases the memory used by the point cloud object.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

pointCloud

 | 

Point cloud object to be released. For details, please refer to [AREngine\_ARPointCloud](#gacc054cea4851be61b160f32b433737fc).

 |

#### \[h2\]HMS\_AREngine\_ARPose\_Create

AREngine\_ARStatus HMS\_AREngine\_ARPose\_Create(const AREngine\_ARSession \*session, const float \*poseRaw, const uint32\_t poseRawSize, AREngine\_ARPose \*\*outPose)

**Description**

Allocates and initializes a new pose object.

You can leave **poseRaw** empty to create an uninitialized pose object, and then call [HMS\_AREngine\_ARPoint\_GetPose](#ga8255eece88d8dc76c554eed360fb7c7b) and [HMS\_AREngine\_ARAnchor\_GetPose](#gad937acfc5d49f0909bdd84677bb0731a) to assign a value to the pose object.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

poseRaw

 | 

Pose data, including translation components and rotation components. The obtained pose data is an array with 7 elements: **poseRaw\[0\]** to **poseRaw\[3\]** are rotation quaternions, and **poseRaw\[4\]** to **poseRaw\[6\]** are translation components (x, y, z).

 |
| 

poseRawSize

 | 

Array size. The value must be greater than or equal to 7.

 |
| 

outPose

 | 

Newly created pose object. For details, please refer to [AREngine\_ARPose](#gab2fa63142ebfb09f0c2ddf88cdb86604).

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |

#### \[h2\]HMS\_AREngine\_ARPose\_Destroy

void HMS\_AREngine\_ARPose\_Destroy(AREngine\_ARPose \*pose)

**Description**

Releases the memory used by the pose object.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

pose

 | 

Pose object to be released. For details, please refer to [AREngine\_ARPose](#gab2fa63142ebfb09f0c2ddf88cdb86604).

 |

#### \[h2\]HMS\_AREngine\_ARPose\_GetMatrix

AREngine\_ARStatus HMS\_AREngine\_ARPose\_GetMatrix(const AREngine\_ARSession \*session, const AREngine\_ARPose \*pose, float \*outMatrixColMajor4x4, int32\_t matrixColMajor4x4Size)

**Description**

Converts the pose data into a 4 × 4 matrix.

**outMatrixColMajor4x4** is the array for storing the matrix, where data is stored in column-major order. Coordinates in the local coordinate system can be converted into ones in the world coordinate system by multiplying this matrix with the coordinates in the local coordinate system.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

pose

 | 

Pose object. For details, please refer to [AREngine\_ARPose](#gab2fa63142ebfb09f0c2ddf88cdb86604).

 |
| 

outMatrixColMajor4x4

 | 

Array with 16 floating-point numbers, which are stored in a column-major order.

 |
| 

matrixColMajor4x4Size

 | 

Array size: [ARENGINE\_VIEW\_MATRIX\_SIZE](#section02261581599).

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |
| 

ARENGINE\_ERROR\_FATAL

 | 

Failure.

 |

#### \[h2\]HMS\_AREngine\_ARPose\_GetPoseRaw

AREngine\_ARStatus HMS\_AREngine\_ARPose\_GetPoseRaw(const AREngine\_ARSession \*session, const AREngine\_ARPose \*pose, float \*outPoseRaw, int32\_t poseRawSize)

**Description**

Extracts pose data from a pose object.

Includes translation components and rotation components. The obtained pose data is an array with 7 elements: **poseRaw\[0\]** to **poseRaw\[3\]** are rotation quaternions, and **poseRaw\[4\]** to **poseRaw\[6\]** are translation components (x, y, z).

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

pose

 | 

Pose object. For details, please refer to [AREngine\_ARPose](#gab2fa63142ebfb09f0c2ddf88cdb86604).

 |
| 

outPoseRaw

 | 

Pose data.

 |
| 

poseRawSize

 | 

Array size: [ARENGINE\_POSE\_RAW\_SIZE](#section14280842115815).

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |

#### \[h2\]HMS\_AREngine\_ARSceneMesh\_AcquireIndexList

AREngine\_ARStatus HMS\_AREngine\_ARSceneMesh\_AcquireIndexList(const AREngine\_ARSession \*session, const AREngine\_ARSceneMesh \*sceneMesh, int32\_t \*outData, int32\_t dataSize)

**Description**

Obtains the index set of mesh faces.

**Start version**: 5.1.0(18)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

sceneMesh

 | 

Mesh information of the current frame. For details, please refer to [AREngine\_ARSceneMesh](#section543212520614).

 |
| 

outData

 | 

Index set of mesh faces.

 |
| 

dataSize

 | 

Number of indexes of the mesh faces. For details, please refer to [HMS\_AREngine\_ARSceneMesh\_AcquireIndexListSize](#section12621161917152).

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |

#### \[h2\]HMS\_AREngine\_ARSceneMesh\_AcquireIndexListSize

AREngine\_ARStatus HMS\_AREngine\_ARSceneMesh\_AcquireIndexListSize(const AREngine\_ARSession \*session, const AREngine\_ARSceneMesh \*sceneMesh, int32\_t \*outSize)

**Description**

Obtains the number of indexes of the mesh faces.

**Start version**: 5.1.0(18)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

sceneMesh

 | 

Mesh information of the current frame. For details, please refer to [AREngine\_ARSceneMesh](#section543212520614).

 |
| 

outSize

 | 

Number of indexes of the mesh faces.

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |

#### \[h2\]HMS\_AREngine\_ARSceneMesh\_AcquireVertexList

AREngine\_ARStatus HMS\_AREngine\_ARSceneMesh\_AcquireVertexList(const AREngine\_ARSession \*session, const AREngine\_ARSceneMesh \*sceneMesh, float \*outData, int32\_t dataSize)

**Description**

Obtains the vertex set of a mesh.

**Start version**: 5.1.0(18)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

sceneMesh

 | 

Mesh information of the current frame. For details, please refer to [AREngine\_ARSceneMesh](#section543212520614).

 |
| 

outData

 | 

Mesh vertex set. The array content is the world coordinates of each vertex, for example, \[x1, y1, z1, x2, y2, z2, ...\].

 |
| 

dataSize

 | 

Number of vertices of a mesh face. For details, please refer to [HMS\_AREngine\_ARSceneMesh\_AcquireVerticesSize](#section1860218429179).

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |

#### \[h2\]HMS\_AREngine\_ARSceneMesh\_AcquireVertexNormalList

AREngine\_ARStatus HMS\_AREngine\_ARSceneMesh\_AcquireVertexNormalList(const AREngine\_ARSession \*session, const AREngine\_ARSceneMesh \*sceneMesh, float \*outData, int32\_t dataSize)

**Description**

Obtains the normal vector set of the mesh faces.

**Start version**: 5.1.0(18)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

sceneMesh

 | 

Mesh information of the current frame. For details, please refer to [AREngine\_ARSceneMesh](#section543212520614).

 |
| 

outData

 | 

Normal vector set of mesh faces. The array content is the world coordinates of each normal vector of the mesh patches, for example, \[x1, y1, z1, x2, y2, z2, ...\].

 |
| 

dataSize

 | 

Number of indexes of the mesh faces. For details, please refer to [HMS\_AREngine\_ARSceneMesh\_AcquireIndexListSize](#section12621161917152).

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |

#### \[h2\]HMS\_AREngine\_ARSceneMesh\_AcquireVerticesSize

AREngine\_ARStatus HMS\_AREngine\_ARSceneMesh\_AcquireVerticesSize(const AREngine\_ARSession \*session, const AREngine\_ARSceneMesh \*sceneMesh, int32\_t \*outSize)

**Description**

Obtains the number of vertices of a mesh.

**Start version**: 5.1.0(18)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

sceneMesh

 | 

Mesh information of the current frame. For details, please refer to [AREngine\_ARSceneMesh](#section543212520614).

 |
| 

outSize

 | 

Number of mesh vertices.

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |

#### \[h2\]HMS\_AREngine\_ARSceneMesh\_Release

void HMS\_AREngine\_ARSceneMesh\_Release(AREngine\_ARSceneMesh \*sceneMesh)

**Description**

Releases the mesh information of the current frame.

**Start version**: 5.1.0(18)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

sceneMesh

 | 

Mesh information of the current frame. For details, please refer to [AREngine\_ARSceneMesh](#section543212520614).

 |

#### \[h2\]HMS\_AREngine\_ARSemanticDense\_AcquireCubeData

AREngine\_ARStatus HMS\_AREngine\_ARSemanticDense\_AcquireCubeData(const AREngine\_ARSession \*session, const AREngine\_ARSemanticDenseData\* semanticDenseData, AREngine\_ARSemanticDenseCubeData \*\*outCubeData)

**Description**

Obtains the cube data from the recognized high-precision geometric reconstruction object data.

**Start version**: 6.0.0(20)

**Parameters**:

| 
Name

 | 

**Description**

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

semanticDenseData

 | 

High-precision geometric reconstruction object data set. For details, please refer to [AREngine\_ARSemanticDenseData](#section1410813229144).

 |
| 

outCubeData

 | 

Cube data in the high-precision geometric reconstruction object data. For details, please refer to [AREngine\_ARSemanticDenseCubeData](../../header-files-and-structs/structs/arengine-arsemanticdensecubedata/document.md).

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |

#### \[h2\]HMS\_AREngine\_ARSemanticDense\_AcquireCubeDataSize

AREngine\_ARStatus HMS\_AREngine\_ARSemanticDense\_AcquireCubeDataSize(const AREngine\_ARSession \*session, const AREngine\_ARSemanticDenseData\* semanticDenseData, int64\_t \*outSize)

**Description**

Obtains the cube count from the recognized high-precision geometric reconstruction object data.

**Start version**: 6.0.0(20)

**Parameters**:

| 
Name

 | 

**Description**

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

semanticDenseData

 | 

High-precision geometric reconstruction object data set. For details, please refer to [AREngine\_ARSemanticDenseData](#section1410813229144).

 |
| 

outSize

 | 

Number of cubes in the [AREngine\_ARSemanticDenseData](#section1410813229144) object.

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |

#### \[h2\]HMS\_AREngine\_ARSemanticDense\_AcquirePointData

AREngine\_ARStatus HMS\_AREngine\_ARSemanticDense\_AcquirePointData(const AREngine\_ARSession \*session, const AREngine\_ARSemanticDenseData\* semanticDenseData, AREngine\_ARSemanticDensePointData \*\*outPointData)

**Description**

Obtains the dense point cloud data from the recognized high-precision geometric reconstruction object data.

**Start version**: 6.0.0(20)

**Parameters**:

| 
Name

 | 

**Description**

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

semanticDenseData

 | 

High-precision geometric reconstruction object data set. For details, please refer to [AREngine\_ARSemanticDenseData](#section1410813229144).

 |
| 

outPointData

 | 

Dense point cloud data in the high-precision geometric reconstruction object data. For details, please refer to [AREngine\_ARSemanticDensePointData](../../header-files-and-structs/structs/arengine-arsemanticdensepointdata/document.md).

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |

#### \[h2\]HMS\_AREngine\_ARSemanticDense\_AcquirePointDataSize

AREngine\_ARStatus HMS\_AREngine\_ARSemanticDense\_AcquirePointDataSize(const AREngine\_ARSession \*session, const AREngine\_ARSemanticDenseData\* semanticDenseData, int64\_t \*outSize)

**Description**

Obtains the dense point cloud size from the recognized high-precision geometric reconstruction object data.

**Start version**: 6.0.0(20)

**Parameters**:

| 
Name

 | 

**Description**

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

semanticDenseData

 | 

Data set of a dense point cloud. For details, please refer to [AREngine\_ARSemanticDenseData](#section1410813229144).

 |
| 

outSize

 | 

Dense point cloud size in the [AREngine\_ARSemanticDenseData](#section1410813229144) object.

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |

#### \[h2\]HMS\_AREngine\_ARSemanticDense\_Release

void HMS\_AREngine\_ARSemanticDense\_Release(AREngine\_ARSemanticDenseData \*semanticDenseData)

**Description**

Releases a high-precision geometric reconstruction object.

**Start version**: 6.0.0(20)

**Parameters**:

| 
Name

 | 

**Description**

 |
| :-- | :-- |
| 

semanticDenseData

 | 

High-precision geometric reconstruction object. For details, please refer to [AREngine\_ARSemanticDenseData](#section1410813229144).

 |

#### \[h2\]HMS\_AREngine\_ARSession\_AcquireNewAnchor

AREngine\_ARStatus HMS\_AREngine\_ARSession\_AcquireNewAnchor(AREngine\_ARSession \*session, const AREngine\_ARPose \*pose, AREngine\_ARAnchor \*\*outAnchor)

**Description**

Creates an anchor for continuous tracking.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

pose

 | 

Pose object used for creating an anchor. For details, please refer to [AREngine\_ARPose](#gab2fa63142ebfb09f0c2ddf88cdb86604).

 |
| 

outAnchor

 | 

Created anchor object. For details, please refer to [AREngine\_ARAnchor](#ga76c16c9d68ba9a3b76f1869c60d8ca1d).

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |
| 

ARENGINE\_ERROR\_NOT\_TRACKING

 | 

Not tracking.

 |
| 

ARENGINE\_ERROR\_RESOURCE\_EXHAUSTED

 | 

Resource exhausted.

 |

#### \[h2\]HMS\_AREngine\_ARSession\_Configure

AREngine\_ARStatus HMS\_AREngine\_ARSession\_Configure(AREngine\_ARSession \*session, const AREngine\_ARConfig \*config)

**Description**

Configures an [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) session.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

config

 | 

Configuration object to be applied on the device. For details, please refer to [AREngine\_ARConfig](#gab0b32ef6018535fd30000f4b6d65f619).

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |
| 

ARENGINE\_ERROR\_FATAL

 | 

Failure.

 |
| 

ARENGINE\_ERROR\_SESSION\_NOT\_PAUSED

 | 

Session not paused.

 |

#### \[h2\]HMS\_AREngine\_ARSession\_Create

AREngine\_ARStatus HMS\_AREngine\_ARSession\_Create(void \*env, void \*applicationContext, AREngine\_ARSession \*\*outSessionPointer)

**Description**

Creates an [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) session.

This function depends on the camera, acceleration sensor, and gyroscope sensor permissions.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

env

 | 

JNI environment for the current app.

 |
| 

applicationContext

 | 

App context.

 |
| 

outSessionPointer

 | 

Created session object. For details, please refer to [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650).

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_PERMISSION\_NOT\_GRANTED

 | 

Permissions not granted, such as the camera permission.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |
| 

ARENGINE\_ERROR\_DEVICE\_NOT\_SUPPORTED

 | 

Device not compatible.

 |
| 

ARENGINE\_ERROR\_FATAL

 | 

Failure.

 |

#### \[h2\]HMS\_AREngine\_ARSession\_Destroy

void HMS\_AREngine\_ARSession\_Destroy(AREngine\_ARSession \*session)

**Description**

Releases the resources used by the [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) session.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |

#### \[h2\]HMS\_AREngine\_ARSession\_GetAllAnchors

AREngine\_ARStatus HMS\_AREngine\_ARSession\_GetAllAnchors(const AREngine\_ARSession \*session, AREngine\_ARAnchorList \*outAnchorList)

**Description**

Obtains all anchors, including anchors in all states contained in [AREngine\_ARTrackingState](#gaae57d2f58331e1033b60cdb2d506a382).

During app processing, only anchors in the [ARENGINE\_TRACKING\_STATE\_TRACKING](#gaae57d2f58331e1033b60cdb2d506a382) state need to be drawn, and anchors in the [ARENGINE\_TRACKING\_STATE\_STOPPED](#gaae57d2f58331e1033b60cdb2d506a382) state need to be deleted.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

outAnchorList

 | 

List of all anchor objects. For details, please refer to [AREngine\_ARAnchorList](#ga516a7f0954dcfda438799aa9e7c6e872).

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |

#### \[h2\]HMS\_AREngine\_ARSession\_GetAllTrackables

AREngine\_ARStatus HMS\_AREngine\_ARSession\_GetAllTrackables(const AREngine\_ARSession \*session, AREngine\_ARTrackableType filterType, AREngine\_ARTrackableList \*outTrackableList)

**Description**

Obtains the list of all trackable objects of the specified type.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

filterType

 | 

Type of the current trackable object. For details, please refer to [AREngine\_ARTrackableType](#ga993948a19fd2bdfa5b946e13a8d4fe3d).

 |
| 

outTrackableList

 | 

List of trackable objects of a specified type. For details, please refer to [AREngine\_ARTrackableList](#gae69e4963b595036fc5e6119a055bb205).

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |

#### \[h2\]HMS\_AREngine\_ARSession\_GetCameraConfig

AREngine\_ARStatus HMS\_AREngine\_ARSession\_GetCameraConfig(const AREngine\_ARSession \*session, AREngine\_ARCameraConfig \*outCameraConfig)

**Description**

Obtains the camera configuration information.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

outCameraConfig

 | 

Camera configuration. For details, please refer to [AREngine\_ARCameraConfig](#ga9b7a5a2082a4127f85a1c9a95cb9acba).

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |

#### \[h2\]HMS\_AREngine\_ARSession\_Pause

AREngine\_ARStatus HMS\_AREngine\_ARSession\_Pause(AREngine\_ARSession \*session)

**Description**

Pauses the session, stops the camera preview stream, and releases the camera (otherwise, other apps will not be able to use the camera service), without clearing the plane and anchor data.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |
| 

ARENGINE\_ERROR\_FATAL

 | 

Failure.

 |

#### \[h2\]HMS\_AREngine\_ARSession\_Resume

AREngine\_ARStatus HMS\_AREngine\_ARSession\_Resume(AREngine\_ARSession \*session)

**Description**

Starts [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650), or restores [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) after [HMS\_AREngine\_ARSession\_Pause](#ga09dedb5c633141321591db0981629de1) is called.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |
| 

ARENGINE\_ERROR\_FATAL

 | 

Failure.

 |
| 

ARENGINE\_ERROR\_CAMERA\_NOT\_AVAILABLE

 | 

Camera unavailable.

 |

#### \[h2\]HMS\_AREngine\_ARSession\_SetCameraGLTexture

AREngine\_ARStatus HMS\_AREngine\_ARSession\_SetCameraGLTexture(AREngine\_ARSession \*session, uint32\_t textureId)

**Description**

Sets the OpenGL texture for storing the camera preview stream data.

After your app calls [HMS\_AREngine\_ARSession\_Update](#ga1d1cacf372a8011a439f0e4e76994259), AR Engine will update the camera preview to the texture.

When using the texture, set it to the **GL\_TEXTURE\_EXTERNAL\_OES** type, for example, by calling **glBindTexture(GL\_TEXTURE\_EXTERNAL\_OES, textureId)**.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

textureId

 | 

OpenGL **textureId** of the camera preview data stream. The value is greater than **0**.

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |

#### \[h2\]HMS\_AREngine\_ARSession\_SetDisplayGeometry

AREngine\_ARStatus HMS\_AREngine\_ARSession\_SetDisplayGeometry(AREngine\_ARSession \*session, AREngine\_ARPoseType rotation, int32\_t width, int32\_t height)

**Description**

Sets the display height and width (in pixels).

Ensure that the height and width you set here are consistent with those of the display view. A mismatch will result in a camera preview failure.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

rotation

 | 

Displayed rotation constant. The value is an enum defined in [AREngine\_ARPoseType](#gae551da7b220b8b38140c3c28882e5010).

 |
| 

width

 | 

Displayed width, in pixels. Its maximum value is limited by the device screen's pixel resolution and can be obtained via [XComponent](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/napi-xcomponent-guidelines).

 |
| 

height

 | 

Displayed height, in pixels. Its maximum value is limited by the device screen's pixel resolution and can be obtained via [XComponent](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/napi-xcomponent-guidelines).

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |

#### \[h2\]HMS\_AREngine\_ARSession\_Stop

AREngine\_ARStatus HMS\_AREngine\_ARSession\_Stop(AREngine\_ARSession \*session)

**Description**

Stops AR Engine and the camera preview stream, clears the plane and anchor data, releases the camera, and terminates the session.

After this method is called, you need to create [AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) if you want to start AR Engine again.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |
| 

ARENGINE\_ERROR\_FATAL

 | 

Failure.

 |

#### \[h2\]HMS\_AREngine\_ARSession\_Update

AREngine\_ARStatus HMS\_AREngine\_ARSession\_Update(AREngine\_ARSession \*session, AREngine\_ARFrame \*outFrame)

**Description**

Updates the computation result of AR Engine.

Call this API when you need to obtain the latest data. For example, after the camera moves, call this API to obtain the new anchor's coordinates, plane coordinates, and image frames obtained by the camera.

If [HMS\_AREngine\_ARConfig\_GetUpdateMode](#gaf32a3cb1f345cd5a243683ecdec63cef) returns [ARENGINE\_UPDATE\_MODE\_BLOCKING](#gabd21cc975ee97b7fb2133af0068ebb5e), this function is blocked until a new frame is available.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

outFrame

 | 

Updated frame object. For details, please refer to [AREngine\_ARFrame](#gaf35f728a1179ef54a3eba9f1cf021719).

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |
| 

ARENGINE\_ERROR\_FATAL

 | 

Failure.

 |
| 

ARENGINE\_ERROR\_SESSION\_PAUSED

 | 

Session paused.

 |
| 

ARENGINE\_ERROR\_MISSING\_GL\_CONTEXT

 | 

GL context missing.

 |
| 

ARENGINE\_ERROR\_CAMERA\_NOT\_AVAILABLE

 | 

Camera unavailable.

 |
| 

ARENGINE\_ERROR\_IMAGE\_INVALID\_DATABASE

 | 

No valid image database exists.

**Start version**: 5.1.0(18)

 |

#### \[h2\]HMS\_AREngine\_ARTarget\_GetAxisAlignedBoundingBox

AREngine\_ARStatus HMS\_AREngine\_ARTarget\_GetAxisAlignedBoundingBox(const AREngine\_ARSession \*session, const AREngine\_ARTarget \*target, float \*outAabb, int32\_t aabbSize)

**Description**

Obtains the coordinates of the minimum bounding box of a semantic object, in the format of (xmin, ymin, zmin, xmax, ymax, zmax).

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

target

 | 

Target semantic object to be processed. For details, please refer to [AREngine\_ARTarget](#ga9af9c1d51ed065f80b373824e0425fa0).

 |
| 

outAabb

 | 

Coordinate set of the minimum bounding box of a semantic object.

 |
| 

aabbSize

 | 

Array size: [ARENGINE\_AABB\_POINT\_SIZE](#section1046854145717).

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |

#### \[h2\]HMS\_AREngine\_ARTarget\_GetCenterPose

AREngine\_ARStatus HMS\_AREngine\_ARTarget\_GetCenterPose(const AREngine\_ARSession \*session, const AREngine\_ARTarget \*target, AREngine\_ARPose \*outARPose)

**Description**

Obtains the pose object for the conversion from the local coordinate system of the target semantic object to the world coordinate system.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

target

 | 

Target semantic object to be processed. For details, please refer to [AREngine\_ARTarget](#ga9af9c1d51ed065f80b373824e0425fa0).

 |
| 

outARPose

 | 

Pose for the conversion from the local coordinate system of the target semantic object to the world coordinate system. For details, please refer to [AREngine\_ARPose](#gab2fa63142ebfb09f0c2ddf88cdb86604).

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |

#### \[h2\]HMS\_AREngine\_ARTarget\_GetRadius

AREngine\_ARStatus HMS\_AREngine\_ARTarget\_GetRadius(const AREngine\_ARSession \*session, const AREngine\_ARTarget \*target, float \*radius)

**Description**

Obtains the sphere radius of a semantic object.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

target

 | 

Target semantic object to be processed. For details, please refer to [AREngine\_ARTarget](#ga9af9c1d51ed065f80b373824e0425fa0).

 |
| 

radius

 | 

Sphere radius of the target semantic object, in meters.

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |

#### \[h2\]HMS\_AREngine\_ARTarget\_GetShapeType

AREngine\_ARStatus HMS\_AREngine\_ARTarget\_GetShapeType(const AREngine\_ARSession \*session, const AREngine\_ARTarget \*target, AREngine\_ARTargetShapeLabel \*shape)

**Description**

Obtains the shape type of a semantic object.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

target

 | 

Target semantic object to be processed. For details, please refer to [AREngine\_ARTarget](#ga9af9c1d51ed065f80b373824e0425fa0).

 |
| 

shape

 | 

Shape type of the target semantic object. For details, please refer to [AREngine\_ARTargetShapeLabel](#gaed68dc13cc314da98d79c88b12d3ae49).

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |

#### \[h2\]HMS\_AREngine\_ARTrackable\_AcquireNewAnchor

AREngine\_ARStatus HMS\_AREngine\_ARTrackable\_AcquireNewAnchor(AREngine\_ARSession \*session, AREngine\_ARTrackable \*trackable, AREngine\_ARPose \*pose, AREngine\_ARAnchor \*\*outAnchor)

**Description**

Creates an anchor object using the pose information of the trackable object. This anchor will be bound to the current trackable object.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

trackable

 | 

Trackable object.

 |
| 

pose

 | 

Pose information of a trackable object.

 |
| 

outAnchor

 | 

Newly created anchor object.

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |
| 

ARENGINE\_ERROR\_NOT\_TRACKING

 | 

Not tracking.

 |
| 

ARENGINE\_ERROR\_RESOURCE\_EXHAUSTED

 | 

Resource exhausted.

 |

#### \[h2\]HMS\_AREngine\_ARTrackable\_GetAnchors

AREngine\_ARStatus HMS\_AREngine\_ARTrackable\_GetAnchors(AREngine\_ARSession \*session, const AREngine\_ARTrackable \*trackable, AREngine\_ARAnchorList \*outAnchorList)

**Description**

Obtains a list of anchor objects bound to the input trackable objects.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

trackable

 | 

Trackable object. For details, please refer to [AREngine\_ARTrackable](#ga54808ebd1a6ed026494acdd945c4f970).

 |
| 

outAnchorList

 | 

List of anchor objects. This list must be created using [HMS\_AREngine\_ARAnchorList\_Create](#ga30492334f7a06b98ef0ad5831d33b198). If you use a list that has been created, values will be reassigned for this list.

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |

#### \[h2\]HMS\_AREngine\_ARTrackable\_GetTrackingState

AREngine\_ARStatus HMS\_AREngine\_ARTrackable\_GetTrackingState(const AREngine\_ARSession \*session, const AREngine\_ARTrackable \*trackable, AREngine\_ARTrackingState \*outTrackingState)

**Description**

Obtains the tracking state of the current trackable object.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

trackable

 | 

Trackable object. For details, please refer to [AREngine\_ARTrackable](#ga54808ebd1a6ed026494acdd945c4f970).

 |
| 

outTrackingState

 | 

Tracking state of the trackable object. For details, please refer to [AREngine\_ARTrackingState](#gaae57d2f58331e1033b60cdb2d506a382).

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |

#### \[h2\]HMS\_AREngine\_ARTrackable\_GetType

AREngine\_ARStatus HMS\_AREngine\_ARTrackable\_GetType(const AREngine\_ARSession \*session, const AREngine\_ARTrackable \*trackable, AREngine\_ARTrackableType \*outTrackableType)

**Description**

Obtains the type of a trackable object.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

trackable

 | 

Trackable object. For details, please refer to [AREngine\_ARTrackable](#ga54808ebd1a6ed026494acdd945c4f970).

 |
| 

outTrackableType

 | 

Type of the trackable object. For details, please refer to [AREngine\_ARTrackableType](#ga993948a19fd2bdfa5b946e13a8d4fe3d).

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |

#### \[h2\]HMS\_AREngine\_ARTrackable\_Release

void HMS\_AREngine\_ARTrackable\_Release(AREngine\_ARTrackable \*trackable)

**Description**

Releases a trackable object.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

trackable

 | 

Trackable object to be released. For details, please refer to [AREngine\_ARTrackable](#ga54808ebd1a6ed026494acdd945c4f970).

 |

#### \[h2\]HMS\_AREngine\_ARTrackableList\_AcquireItem

AREngine\_ARStatus HMS\_AREngine\_ARTrackableList\_AcquireItem(const AREngine\_ARSession \*session, const AREngine\_ARTrackableList \*trackableList, int32\_t index, AREngine\_ARTrackable \*\*outTrackable)

**Description**

Obtains the object at a specific index from the trackable object list.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

trackableList

 | 

List of trackable objects. For details, please refer to [AREngine\_ARTrackableList](#gae69e4963b595036fc5e6119a055bb205).

 |
| 

index

 | 

Location of a trackable object in the trackable object list. The maximum value cannot exceed the value returned by [HMS\_AREngine\_ARTrackableList\_GetSize](#gad9729d4436f3d969286f31b33d07513e).

 |
| 

outTrackable

 | 

Target trackable object. For details, please refer to [AREngine\_ARTrackable](#ga54808ebd1a6ed026494acdd945c4f970).

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |

#### \[h2\]HMS\_AREngine\_ARTrackableList\_Create

AREngine\_ARStatus HMS\_AREngine\_ARTrackableList\_Create(const AREngine\_ARSession \*session, AREngine\_ARTrackableList \*\*outTrackableList)

**Description**

Creates a list of trackable objects.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

outTrackableList

 | 

List of trackable objects to be created. For details, please refer to [AREngine\_ARTrackableList](#gae69e4963b595036fc5e6119a055bb205).

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |
| 

ARENGINE\_ERROR\_RESOURCE\_EXHAUSTED

 | 

Resource exhausted.

 |

#### \[h2\]HMS\_AREngine\_ARTrackableList\_Destroy

void HMS\_AREngine\_ARTrackableList\_Destroy(AREngine\_ARTrackableList \*trackableList)

**Description**

Releases the list of trackable objects, along with all the anchor references it holds.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

trackableList

 | 

List of trackable objects to be released. For details, please refer to [AREngine\_ARTrackableList](#gae69e4963b595036fc5e6119a055bb205).

 |

#### \[h2\]HMS\_AREngine\_ARTrackableList\_GetSize

AREngine\_ARStatus HMS\_AREngine\_ARTrackableList\_GetSize(const AREngine\_ARSession \*session, const AREngine\_ARTrackableList \*trackableList, int32\_t \*outSize)

**Description**

Obtains the number of trackable objects in the list.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

session

 | 

[AREngine\_ARSession](#ga2dbf3585f50628750ec855501c043650) object that interacts with the AR Engine service.

 |
| 

trackableList

 | 

List of trackable objects. For details, please refer to [AREngine\_ARTrackableList](#gae69e4963b595036fc5e6119a055bb205).

 |
| 

outSize

 | 

Number of trackable objects in the trackable object list.

 |

**Returns**:

Execution status. For details, please refer to [AREngine\_ARStatus](#gacc90fb9320a5ba10bb23f7a37440885d).

| 
Status Code

 | 

Description

 |
| :-- | :-- |
| 

ARENGINE\_SUCCESS

 | 

Success.

 |
| 

ARENGINE\_ERROR\_INVALID\_ARGUMENT

 | 

Invalid parameters, for example, the input parameter is empty or invalid.

 |
