# ar\_engine\_core.h

#### Overview

Declares the APIs for accessing AR Engine; provides APIs related to the AR capabilities; covers basic AR capabilities at its core, including motion tracking, environment tracking, and hit testing.

**Library**: libarengine\_ndk.z.so

**System capability**: SystemCapability.AREngine.Core

**Start version**: 5.0.0(12)

**Related module**: [AR Engine](../../../modules/ar-engine/document.md)

#### \[h2\]Structs

| 
**Name**

 | 

**Description**

 |
| :-- | :-- |
| 

struct [AREngine\_ARAugmentedImageSource](../../structs/arengine-araugmentedimagesource/document.md)

 | 

Image data.

 |
| 

struct [AREngine\_ClipPlaneDistance](../../structs/arengine-clipplanedistance/document.md)

 | 

Distance to the clipping planes.

 |
| 

struct [AREngine\_ARSemanticDensePointData](../../structs/arengine-arsemanticdensepointdata/document.md)

 | 

Dense point cloud data of a high-precision geometric reconstruction object.

 |
| 

struct [AREngine\_ARSemanticDenseCubeData](../../structs/arengine-arsemanticdensecubedata/document.md)

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

[ARENGINE\_AABB\_POINT\_SIZE](../../../modules/ar-engine/document.md#section1046854145717) = 6

 | 

Size of the bounding box coordinate array.

 |
| 

[ARENGINE\_DISTORTION\_COUNT](../../../modules/ar-engine/document.md#section2059093619593) = 5

 | 

Number of camera distortion parameters.

 |
| 

[ARENGINE\_POSE\_RAW\_SIZE](../../../modules/ar-engine/document.md#section14280842115815) = 7

 | 

Size of the pose data array.

 |
| 

[ARENGINE\_VIEW\_MATRIX\_SIZE](../../../modules/ar-engine/document.md#section02261581599) = 16

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

typedef struct [AREngine\_ARAnchor](../../../modules/ar-engine/document.md#ga76c16c9d68ba9a3b76f1869c60d8ca1d) [AREngine\_ARAnchor](../../../modules/ar-engine/document.md#ga76c16c9d68ba9a3b76f1869c60d8ca1d)

 | 

Anchor object.

 |
| 

typedef struct [AREngine\_ARAnchorList](../../../modules/ar-engine/document.md#ga516a7f0954dcfda438799aa9e7c6e872) [AREngine\_ARAnchorList](../../../modules/ar-engine/document.md#ga516a7f0954dcfda438799aa9e7c6e872)

 | 

Anchor object list.

 |
| 

typedef struct [AREngine\_ARAugmentedImage](../../../modules/ar-engine/document.md#section68491824155217) [AREngine\_ARAugmentedImage](../../../modules/ar-engine/document.md#section68491824155217)

 | 

Trackable image object.

 |
| 

typedef struct [AREngine\_ARAugmentedImageDatabase](../../../modules/ar-engine/document.md#section152051642330) [AREngine\_ARAugmentedImageDatabase](../../../modules/ar-engine/document.md#section152051642330)

 | 

Trackable image database object.

 |
| 

typedef struct [AREngine\_ARCamera](../../../modules/ar-engine/document.md#ga7bdcf1fb36c404d36e09ad70d2545d92) [AREngine\_ARCamera](../../../modules/ar-engine/document.md#ga7bdcf1fb36c404d36e09ad70d2545d92)

 | 

Camera information for the current frame.

 |
| 

typedef struct [AREngine\_ARCameraConfig](../../../modules/ar-engine/document.md#ga9b7a5a2082a4127f85a1c9a95cb9acba) [AREngine\_ARCameraConfig](../../../modules/ar-engine/document.md#ga9b7a5a2082a4127f85a1c9a95cb9acba)

 | 

Camera configuration information.

 |
| 

typedef struct [AREngine\_ARCameraIntrinsics](../../../modules/ar-engine/document.md#ga17948eef3aa7ff7f2fa8aff6a63b4b51) [AREngine\_ARCameraIntrinsics](../../../modules/ar-engine/document.md#ga17948eef3aa7ff7f2fa8aff6a63b4b51)

 | 

Intrinsic camera parameters.

 |
| 

typedef struct [AREngine\_ARConfig](../../../modules/ar-engine/document.md#gab0b32ef6018535fd30000f4b6d65f619) [AREngine\_ARConfig](../../../modules/ar-engine/document.md#gab0b32ef6018535fd30000f4b6d65f619)

 | 

Used for configuring [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) capabilities (that is, capabilities and modes to use).

 |
| 

typedef struct [AREngine\_ARFrame](../../../modules/ar-engine/document.md#gaf35f728a1179ef54a3eba9f1cf021719) [AREngine\_ARFrame](../../../modules/ar-engine/document.md#gaf35f728a1179ef54a3eba9f1cf021719)

 | 

A frame of data processed by AR Engine.

 |
| 

typedef struct [AREngine\_ARHitResult](../../../modules/ar-engine/document.md#gaeb304c8b21122eb7ffda7403316a3507) [AREngine\_ARHitResult](../../../modules/ar-engine/document.md#gaeb304c8b21122eb7ffda7403316a3507)

 | 

Hit testing result object.

 |
| 

typedef struct [AREngine\_ARHitResultList](../../../modules/ar-engine/document.md#ga1f2369453412bd4d77ab8f5aa2d52bb3) [AREngine\_ARHitResultList](../../../modules/ar-engine/document.md#ga1f2369453412bd4d77ab8f5aa2d52bb3)

 | 

Hit testing result list.

 |
| 

typedef struct [AREngine\_ARImage](../../../modules/ar-engine/document.md#gabfee13b0076f2f00b7efdef2717add59) [AREngine\_ARImage](../../../modules/ar-engine/document.md#gabfee13b0076f2f00b7efdef2717add59)

 | 

Camera video stream frame object.

 |
| 

typedef struct [AREngine\_ARPlane](../../../modules/ar-engine/document.md#ga76f9bdb23634312b8488fcbaff4aa9b5) [AREngine\_ARPlane](../../../modules/ar-engine/document.md#ga76f9bdb23634312b8488fcbaff4aa9b5)

 | 

Plane object.

 |
| 

typedef struct [AREngine\_ARPoint](../../../modules/ar-engine/document.md#gac7b6923d92487d68e77543dd223364d6) [AREngine\_ARPoint](../../../modules/ar-engine/document.md#gac7b6923d92487d68e77543dd223364d6)

 | 

Point object.

 |
| 

typedef struct [AREngine\_ARPointCloud](../../../modules/ar-engine/document.md#gacc054cea4851be61b160f32b433737fc) [AREngine\_ARPointCloud](../../../modules/ar-engine/document.md#gacc054cea4851be61b160f32b433737fc)

 | 

Collection of trackable 3D point clouds.

 |
| 

typedef struct [AREngine\_ARPose](../../../modules/ar-engine/document.md#gab2fa63142ebfb09f0c2ddf88cdb86604) [AREngine\_ARPose](../../../modules/ar-engine/document.md#gab2fa63142ebfb09f0c2ddf88cdb86604)

 | 

Pose object.

 |
| 

typedef struct [AREngine\_ARSceneMesh](../../../modules/ar-engine/document.md#section543212520614) [AREngine\_ARSceneMesh](../../../modules/ar-engine/document.md#section543212520614)

 | 

Environment mesh data set.

 |
| 

typedef struct [AREngine\_ARSemanticDenseData](../../../modules/ar-engine/document.md#section1410813229144) [AREngine\_ARSemanticDenseData](../../../modules/ar-engine/document.md#section1410813229144)

 | 

High-precision geometric reconstruction object data set.

 |
| 

typedef struct [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650)

 | 

Used to manage the system status of AR Engine.

 |
| 

typedef struct [AREngine\_ARTarget](../../../modules/ar-engine/document.md#ga9af9c1d51ed065f80b373824e0425fa0) [AREngine\_ARTarget](../../../modules/ar-engine/document.md#ga9af9c1d51ed065f80b373824e0425fa0)

 | 

Object.

 |
| 

typedef struct [AREngine\_ARTrackable](../../../modules/ar-engine/document.md#ga54808ebd1a6ed026494acdd945c4f970) [AREngine\_ARTrackable](../../../modules/ar-engine/document.md#ga54808ebd1a6ed026494acdd945c4f970)

 | 

Trackable object, such as a point or a plane.

 |
| 

typedef struct [AREngine\_ARTrackableList](../../../modules/ar-engine/document.md#gae69e4963b595036fc5e6119a055bb205) [AREngine\_ARTrackableList](../../../modules/ar-engine/document.md#gae69e4963b595036fc5e6119a055bb205)

 | 

Trackable object list.

 |
| 

typedef void (\*[HMS\_AREngine\_PhotoAvailableCallback](../../../modules/ar-engine/document.md#section430673420224))([OH\_NativeBuffer](../../../../../../standard-libraries/vulkan/vulkan-extensions/oh-nativebuffer/document.md) \*photoBuffer)

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

[AREngine\_ARAddAugmentedImageReason](../../../modules/ar-engine/document.md#section2441053595) {

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

[AREngine\_ARConfidenceLevel](../../../modules/ar-engine/document.md#section959011484610) {

ARENGINE\_DEPTH\_CONFIDENCE\_LOW = 0,

ARENGINE\_DEPTH\_CONFIDENCE\_MEDIUM = 1,

ARENGINE\_DEPTH\_CONFIDENCE\_HIGH = 2

}

 | 

Depth confidence.

 |
| 

[AREngine\_ARDepthMode](../../../modules/ar-engine/document.md#section12321429115215) {

ARENGINE\_DEPTH\_MODE\_DISABLED = 0,

ARENGINE\_DEPTH\_MODE\_AUTOMATIC = 1

}

 | 

Depth mode.

 |
| 

[AREngine\_ARFocusMode](../../../modules/ar-engine/document.md#gaf50530faa0d094182a0db0c73b75d875) {

ARENGINE\_FOCUS\_MODE\_FIXED = 0,

ARENGINE\_FOCUS\_MODE\_AUTO = 1

}

 | 

Focus mode.

 |
| 

[AREngine\_ARImageDatabaseMode](../../../modules/ar-engine/document.md#section683253471219) {

ARENGINE\_ADD\_NORMAL = 0,

ARENGINE\_ADD\_AUTO = 1

}

 | 

Mode of adding images to the feature database for tracking.

 |
| 

[AREngine\_ARImageFormat](../../../modules/ar-engine/document.md#gadfcf7a1211ed12a90f377610d0f838ac) {

ARENGINE\_IMAGE\_UNKNOWN = 0,

ARENGINE\_IMAGE\_YUV\_420\_888 = 2,

ARENGINE\_IMAGE\_Y\_8 = 3,

ARENGINE\_IMAGE\_Y\_16 = 4

}

 | 

Image format.

 |
| 

[AREngine\_ARImageStreamMode](../../../modules/ar-engine/document.md#section184201559356) {

ARENGINE\_IMAGE\_STREAM\_MODE\_PREVIEW = 0,

ARENGINE\_IMAGE\_STREAM\_MODE\_PREVIEW\_AND\_PHOTO = 1

}

 | 

Image data stream mode. By default, **ARENGINE\_IMAGE\_STREAM\_MODE\_PREVIEW** is used.

 |
| 

[AREngine\_ARMeshMode](../../../modules/ar-engine/document.md#section19436658201620) {

ARENGINE\_MESH\_MODE\_DISABLED = 0,

ARENGINE\_MESH\_MODE\_ENABLE=1

}

 | 

Mesh enabling mode.

 |
| 

[AREngine\_ARPlaneFindingMode](../../../modules/ar-engine/document.md#gab8e7db52d819359026fc4a82815d3fff) {

ARENGINE\_PLANE\_FINDING\_MODE\_DISABLED = 0,

ARENGINE\_PLANE\_FINDING\_MODE\_HORIZONTAL = 1,

ARENGINE\_PLANE\_FINDING\_MODE\_VERTICAL = 2,

ARENGINE\_PLANE\_FINDING\_MODE\_HORIZONTAL\_AND\_VERTICAL = 3

}

 | 

Plane finding mode.

 |
| 

[AREngine\_ARPlaneType](../../../modules/ar-engine/document.md#ga895db37a92155584c5448bee30a8beab) {

ARENGINE\_PLANE\_FACING\_HORIZONTAL\_UPWARD = 0,

ARENGINE\_PLANE\_FACING\_HORIZONTAL\_DOWNWARD = 1,

ARENGINE\_PLANE\_FACING\_VERTICAL = 2,

ARENGINE\_PLANE\_FACING\_INVALID = 3

}

 | 

Plane type.

 |
| 

[AREngine\_ARPointOrientationMode](../../../modules/ar-engine/document.md#ga0e2893593f4372954fd97519e0a63855) {

ARENGINE\_POINT\_ORIENTATION\_INITIALIZED\_TO\_IDENTITY = 0,

ARENGINE\_POINT\_ORIENTATION\_ESTIMATED\_SURFACE\_NORMAL = 1

}

 | 

Orientation mode.

 |
| 

[AREngine\_ARPoseMode](../../../modules/ar-engine/document.md#section1249515330198) {

ARENGINE\_POSE\_MODE\_GRAVITY = 0,

ARENGINE\_POSE\_MODE\_GRAVITY\_HEADING = 1

}

 | 

Output camera pose alignment format of AR Engine.

 |
| 

[AREngine\_ARPoseType](../../../modules/ar-engine/document.md#gae551da7b220b8b38140c3c28882e5010) {

ARENGINE\_POSE\_TYPE\_IDENTITY = 0,

ARENGINE\_POSE\_TYPE\_ROTATE\_90 = 1,

ARENGINE\_POSE\_TYPE\_ROTATE\_180 = 2,

ARENGINE\_POSE\_TYPE\_ROTATE\_270 = 3

}

 | 

Pose type.

 |
| 

[AREngine\_ARPowerMode](../../../modules/ar-engine/document.md#ga3d925e007e2847e69f22af68ec922507) {

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

[AREngine\_ARPreviewMode](../../../modules/ar-engine/document.md#gadef0f2099b106b872a014ef6551906ae) {

ARENGINE\_PREVIEW\_MODE\_ENABLED = 0,

ARENGINE\_PREVIEW\_MODE\_DISABLED = 1

}

 | 

Preview mode.

 |
| 

[AREngine\_ARSemanticDenseMode](../../../modules/ar-engine/document.md#section09971756142213) {

ARENGINE\_SEMANTIC\_DENSE\_MODE\_DISABLED = 0,

ARENGINE\_SEMANTIC\_DENSE\_MODE\_NORMAL = 1,

ARENGINE\_SEMANTIC\_DENSE\_MODE\_CUBE\_VOLUME = 2,

ARENGINE\_SEMANTIC\_DENSE\_MODE\_CUBE\_SPACE = 3

}

 | 

Recognition mode of high-precision geometric reconstruction.

 |
| 

[AREngine\_ARSemanticMode](../../../modules/ar-engine/document.md#ga34d3000de29454b99d89406d288d6ed5) {

ARENGINE\_SEMANTIC\_MODE\_NONE = 0,

ARENGINE\_SEMANTIC\_MODE\_PLANE = 1,

ARENGINE\_SEMANTIC\_MODE\_TARGET = 2

}

 | 

Semantic mode.

 |
| 

[AREngine\_ARSemanticPlaneLabel](../../../modules/ar-engine/document.md#gafbb6b69fefdc417ba6437ce2fe587cb1) {

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

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) {

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

[AREngine\_ARTargetShapeLabel](../../../modules/ar-engine/document.md#gaed68dc13cc314da98d79c88b12d3ae49) {

ARENGINE\_TARGET\_SHAPE\_UNKNOWN = 0,

ARENGINE\_TARGET\_SHAPE\_CUBE = 1,

ARENGINE\_TARGET\_SHAPE\_CIRCLE = 2,

ARENGINE\_TARGET\_SHAPE\_RECTANGLE = 3

}

 | 

Shape of the recognized object.

 |
| 

[AREngine\_ARTrackableType](../../../modules/ar-engine/document.md#ga993948a19fd2bdfa5b946e13a8d4fe3d) {

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

[AREngine\_ARTrackingState](../../../modules/ar-engine/document.md#gaae57d2f58331e1033b60cdb2d506a382) {

ARENGINE\_TRACKING\_STATE\_TRACKING = 0,

ARENGINE\_TRACKING\_STATE\_PAUSED = 1,

ARENGINE\_TRACKING\_STATE\_STOPPED = 2

}

 | 

Tracking state of the trackable object.

 |
| 

[AREngine\_ARTrackingStateReason](../../../modules/ar-engine/document.md#ga67774b71935ef2f8a2ae5e5822c3dcdb) {

ARENGINE\_TRACKING\_STATE\_REASON\_NONE = 0,

ARENGINE\_TRACKING\_STATE\_REASON\_EXCESSIVE\_MOTION = 1,

ARENGINE\_TRACKING\_STATE\_REASON\_INSUFFICIENT\_FEATURES = 2

}

 | 

Possible causes of tracking failures.

 |
| 

[AREngine\_ARType](../../../modules/ar-engine/document.md#ga987888aea7dcaa9abcdb64581c850bf5) {

ARENGINE\_TYPE\_WORLD = 0x01,

ARENGINE\_TYPE\_IMAGE = 0x80

}

 | 

AR capability type.

 |
| 

[AREngine\_ARUpdateMode](../../../modules/ar-engine/document.md#gabd21cc975ee97b7fb2133af0068ebb5e) {

ARENGINE\_UPDATE\_MODE\_BLOCKING = 0,

ARENGINE\_UPDATE\_MODE\_LATEST = 1

}

 | 

Data update mode specified by [HMS\_AREngine\_ARSession\_Update](../../../modules/ar-engine/document.md#ga1d1cacf372a8011a439f0e4e76994259).

 |

#### \[h2\]Functions

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARAnchor\_Detach](../../../modules/ar-engine/document.md#ga6b731c00cc038f62d21ccb280067114b) ([AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, [AREngine\_ARAnchor](../../../modules/ar-engine/document.md#ga76c16c9d68ba9a3b76f1869c60d8ca1d) \*anchor)

 | 

Instructs AR Engine to stop tracking and unbind an anchor.

CAUTION:

This function does not release [AREngine\_ARAnchor](../../../modules/ar-engine/document.md#ga76c16c9d68ba9a3b76f1869c60d8ca1d). You need to call [HMS\_AREngine\_ARAnchor\_Release](../../../modules/ar-engine/document.md#gad04b12f9a2b0415789de5d6e1692f51c) to release this anchor.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARAnchor\_GetPose](../../../modules/ar-engine/document.md#gad937acfc5d49f0909bdd84677bb0731a) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARAnchor](../../../modules/ar-engine/document.md#ga76c16c9d68ba9a3b76f1869c60d8ca1d) \*anchor, [AREngine\_ARPose](../../../modules/ar-engine/document.md#gab2fa63142ebfb09f0c2ddf88cdb86604) \*outPose)

 | 

Obtains the pose of a specific anchor in the world coordinate system.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARAnchor\_GetTrackingState](../../../modules/ar-engine/document.md#ga6d8c173cc1ef3888f1bedfd6adb2efb3) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARAnchor](../../../modules/ar-engine/document.md#ga76c16c9d68ba9a3b76f1869c60d8ca1d) \*anchor, [AREngine\_ARTrackingState](../../../modules/ar-engine/document.md#gaae57d2f58331e1033b60cdb2d506a382) \*outTrackingState)

 | 

Obtains the tracking state of the pose of a specific anchor.

 |
| 

void [HMS\_AREngine\_ARAnchor\_Release](../../../modules/ar-engine/document.md#gad04b12f9a2b0415789de5d6e1692f51c) ([AREngine\_ARAnchor](../../../modules/ar-engine/document.md#ga76c16c9d68ba9a3b76f1869c60d8ca1d) \*anchor)

 | 

Releases the memory used by a specific anchor object.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARAnchorList\_AcquireItem](../../../modules/ar-engine/document.md#ga1f520dddd96c9918163bff8b68f428fc) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARAnchorList](../../../modules/ar-engine/document.md#ga516a7f0954dcfda438799aa9e7c6e872) \*anchorList, int32\_t index, [AREngine\_ARAnchor](../../../modules/ar-engine/document.md#ga76c16c9d68ba9a3b76f1869c60d8ca1d) \*\*outAnchor)

 | 

Obtains the anchor at a specific location from the anchor object list.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARAnchorList\_Create](../../../modules/ar-engine/document.md#ga30492334f7a06b98ef0ad5831d33b198) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, [AREngine\_ARAnchorList](../../../modules/ar-engine/document.md#ga516a7f0954dcfda438799aa9e7c6e872) \*\*outAnchorList)

 | 

Creates a list of anchor objects.

 |
| 

void [HMS\_AREngine\_ARAnchorList\_Destroy](../../../modules/ar-engine/document.md#ga5b1078469a123466245f65524c9c33be) ([AREngine\_ARAnchorList](../../../modules/ar-engine/document.md#ga516a7f0954dcfda438799aa9e7c6e872) \*anchorList)

 | 

Releases a list of anchor objects.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARAnchorList\_GetSize](../../../modules/ar-engine/document.md#ga9e96df41cdb973d7e45c714b1bd31fd1) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARAnchorList](../../../modules/ar-engine/document.md#ga516a7f0954dcfda438799aa9e7c6e872) \*anchorList, int32\_t \*outSize)

 | 

Obtains the number of anchors in the anchor object list.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARAugmentedImage\_AcquireName](../../../modules/ar-engine/document.md#section110712352334) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARAugmentedImage](../../../modules/ar-engine/document.md#section68491824155217) \*augmentedImage, char \*augmentedImageName, uint32\_t \*outNameLength)

 | 

Returns the name of the tracking image.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARAugmentedImage\_GetCenterPose](../../../modules/ar-engine/document.md#section498975343520) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARAugmentedImage](../../../modules/ar-engine/document.md#section68491824155217) \*augmentedImage, [AREngine\_ARPose](../../../modules/ar-engine/document.md#gab2fa63142ebfb09f0c2ddf88cdb86604) \*outPose)

 | 

Obtains the pose information of the center point of a tracking image in the world coordinate system.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARAugmentedImage\_GetExtendX](../../../modules/ar-engine/document.md#section917593011382) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARAugmentedImage](../../../modules/ar-engine/document.md#section68491824155217) \*augmentedImage, float \*outExtendX)

 | 

Obtains the estimated value on the X axis based on the center point of the image as the coordinate origin.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARAugmentedImage\_GetExtendZ](../../../modules/ar-engine/document.md#section9630192711390) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARAugmentedImage](../../../modules/ar-engine/document.md#section68491824155217) \*augmentedImage, float \*outExtendZ)

 | 

Obtains the estimated value on the Z axis based on the center point of the image as the coordinate origin.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARAugmentedImage\_GetIndex](../../../modules/ar-engine/document.md#section27041685401) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARAugmentedImage](../../../modules/ar-engine/document.md#section68491824155217) \*augmentedImage, uint32\_t \*outIndex)

 | 

Obtains the index of a tracking image in the tracking image database.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARAugmentedImageDatabase\_AddImage](../../../modules/ar-engine/document.md#section0315115618403) ([AREngine\_ARAugmentedImageDatabase](../../../modules/ar-engine/document.md#section152051642330) \*database, const [AREngine\_ARAugmentedImageSource](../../structs/arengine-araugmentedimagesource/document.md) \*image, uint32\_t \*outIndex, [AREngine\_ARAddAugmentedImageReason](../../../modules/ar-engine/document.md#section2441053595) \*outReason)

 | 

Adds an image to the image database and outputs the index of the image.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARAugmentedImageDatabase\_Create](../../../modules/ar-engine/document.md#section4108822184411) ([AREngine\_ARAugmentedImageDatabase](../../../modules/ar-engine/document.md#section152051642330) \*\*outDatabase)

 | 

Creates an empty tracking image database.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARAugmentedImageDatabase\_Deserialize](../../../modules/ar-engine/document.md#section1619582764511) (const uint8\_t \*buffer, const uint64\_t bufSize, [AREngine\_ARAugmentedImageDatabase](../../../modules/ar-engine/document.md#section152051642330) \*\*outDatabase)

 | 

Deserializes the feature database.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARAugmentedImageDatabase\_Destroy](../../../modules/ar-engine/document.md#section14702121818469) ([AREngine\_ARAugmentedImageDatabase](../../../modules/ar-engine/document.md#section152051642330) \*database)

 | 

Releases an image database object.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARAugmentedImageDatabase\_GetAddMode](../../../modules/ar-engine/document.md#section1731662218476) (const [AREngine\_ARAugmentedImageDatabase](../../../modules/ar-engine/document.md#section152051642330) \*database, [AREngine\_ARImageDatabaseMode](../../../modules/ar-engine/document.md#section683253471219) \*outAddMode)

 | 

Obtains the mode of adding a tracking image.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARAugmentedImageDatabase\_SetAddMode](../../../modules/ar-engine/document.md#section2579104674818) (const [AREngine\_ARAugmentedImageDatabase](../../../modules/ar-engine/document.md#section152051642330) \*database, [AREngine\_ARImageDatabaseMode](../../../modules/ar-engine/document.md#section683253471219) addMode)

 | 

Sets the mode of adding a tracking image.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARAugmentedImageDatabase\_GetCapacity](../../../modules/ar-engine/document.md#section650873916491) (const [AREngine\_ARAugmentedImageDatabase](../../../modules/ar-engine/document.md#section152051642330) \*database, uint32\_t \*outCapacity)

 | 

Obtains the maximum number of images that can be added.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARAugmentedImageDatabase\_GetImageCount](../../../modules/ar-engine/document.md#section6183812506) (const [AREngine\_ARAugmentedImageDatabase](../../../modules/ar-engine/document.md#section152051642330) \*database, uint32\_t \*outImageCount)

 | 

Obtains the number of images stored in the database.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARAugmentedImageDatabase\_Serialize](../../../modules/ar-engine/document.md#section6536162875117) (const [AREngine\_ARAugmentedImageDatabase](../../../modules/ar-engine/document.md#section152051642330) \*database, uint8\_t \*\*outBuffer, uint64\_t \*outBufSize)

 | 

Serializes the feature database.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARCamera\_GetDisplayOrientedPose](../../../modules/ar-engine/document.md#ga088648130f3a91cdf8d7b95f5ee1faf2) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARCamera](../../../modules/ar-engine/document.md#ga7bdcf1fb36c404d36e09ad70d2545d92) \*camera, [AREngine\_ARPose](../../../modules/ar-engine/document.md#gab2fa63142ebfb09f0c2ddf88cdb86604) \*outPose)

 | 

Sets **outPose** to the pose of the virtual camera (facing the display) in the world space, in order to render AR content into the latest frame.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARCamera\_GetImageIntrinsics](../../../modules/ar-engine/document.md#ga8e6f32adc3bd59504042d4e18bfb3432) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARCamera](../../../modules/ar-engine/document.md#ga7bdcf1fb36c404d36e09ad70d2545d92) \*camera, [AREngine\_ARCameraIntrinsics](../../../modules/ar-engine/document.md#ga17948eef3aa7ff7f2fa8aff6a63b4b51) \*outIntrinsics)

 | 

Obtains the object of the offline intrinsic camera parameters. This object can be used to obtain the camera's focal length, image dimensions, principal point, and distortion parameters.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARCamera\_GetPose](../../../modules/ar-engine/document.md#ga00df108c4ba187967a10e9c4d2e27d3a) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARCamera](../../../modules/ar-engine/document.md#ga7bdcf1fb36c404d36e09ad70d2545d92) \*camera, [AREngine\_ARPose](../../../modules/ar-engine/document.md#gab2fa63142ebfb09f0c2ddf88cdb86604) \*outPose)

 | 

Sets **outPose** to the pose of the physical camera in the world space in the latest frame. The pose is the pose of the OpenGL camera.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARCamera\_GetProjectionMatrix](../../../modules/ar-engine/document.md#ga01feacf9cd393a0598e2ac5cf7b61693) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARCamera](../../../modules/ar-engine/document.md#ga7bdcf1fb36c404d36e09ad70d2545d92) \*camera, [AREngine\_ClipPlaneDistance](../../structs/arengine-clipplanedistance/document.md) clipPlaneDistance, float \*outDestColMajor4x4, int32\_t destColMajor4x4Num)

 | 

Obtains the projection matrix used for rendering virtual content on top of the camera image. This matrix can be used for converting from the camera coordinate system to the clip coordinate system.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARCamera\_GetTrackingState](../../../modules/ar-engine/document.md#ga2dc931eee56ae5ea899f8acc08eb3f36) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARCamera](../../../modules/ar-engine/document.md#ga7bdcf1fb36c404d36e09ad70d2545d92) \*camera, [AREngine\_ARTrackingState](../../../modules/ar-engine/document.md#gaae57d2f58331e1033b60cdb2d506a382) \*outTrackingState)

 | 

Obtains the current tracking state of the camera.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARCamera\_GetTrackingStateReason](../../../modules/ar-engine/document.md#gab5411813f2e4ac6de4ebbccfc1bbbd35) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARCamera](../../../modules/ar-engine/document.md#ga7bdcf1fb36c404d36e09ad70d2545d92) \*camera, [AREngine\_ARTrackingStateReason](../../../modules/ar-engine/document.md#ga67774b71935ef2f8a2ae5e5822c3dcdb) \*outTrackingStateReason)

 | 

Obtains the reason when the current tracking state of the camera is [ARENGINE\_TRACKING\_STATE\_PAUSED](../../../modules/ar-engine/document.md#gaae57d2f58331e1033b60cdb2d506a382).

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARCamera\_GetViewMatrix](../../../modules/ar-engine/document.md#ga130b4689d7d967e812d24fc2be071d68) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARCamera](../../../modules/ar-engine/document.md#ga7bdcf1fb36c404d36e09ad70d2545d92) \*camera, float \*outColMajor4x4, int32\_t colMajor4x4Num)

 | 

Obtains the view matrix of the camera in the latest frame.

 |
| 

void [HMS\_AREngine\_ARCamera\_Release](../../../modules/ar-engine/document.md#ga16909b4002b9c6250dad88bb8397adc9) ([AREngine\_ARCamera](../../../modules/ar-engine/document.md#ga7bdcf1fb36c404d36e09ad70d2545d92) \*camera)

 | 

Releases the reference to the camera.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARCameraConfig\_Create](../../../modules/ar-engine/document.md#gac6402425c6c6390da3c4e57d328da443) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, [AREngine\_ARCameraConfig](../../../modules/ar-engine/document.md#ga9b7a5a2082a4127f85a1c9a95cb9acba) \*\*outCameraConfig)

 | 

Creates a camera configuration object.

 |
| 

void [HMS\_AREngine\_ARCameraConfig\_Destroy](../../../modules/ar-engine/document.md#ga2540153f0404799943470c41dff3b5f4) ([AREngine\_ARCameraConfig](../../../modules/ar-engine/document.md#ga9b7a5a2082a4127f85a1c9a95cb9acba) \*cameraConfig)

 | 

Releases a camera configuration object.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARCameraConfig\_GetImageDimensions](../../../modules/ar-engine/document.md#gac3dc81c1c9e6945dd4a3de30e45ccc8f) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARCameraConfig](../../../modules/ar-engine/document.md#ga9b7a5a2082a4127f85a1c9a95cb9acba) \*cameraConfig, int32\_t \*outWidth, int32\_t \*outHeight)

 | 

Obtains the size of the image sent by the camera to the CPU for processing from a camera configuration object.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARCameraConfig\_GetTextureDimensions](../../../modules/ar-engine/document.md#ga19ade172d2e2dcd67495f6be1bcc2706) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARCameraConfig](../../../modules/ar-engine/document.md#ga9b7a5a2082a4127f85a1c9a95cb9acba) \*cameraConfig, int32\_t \*outWidth, int32\_t \*outHeight)

 | 

Obtains the size of the image texture sent by the camera to the GPU for processing from a camera configuration object.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARCameraIntrinsics\_Create](../../../modules/ar-engine/document.md#ga027e92d8f7b25e6e577a9658545e2c2a) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, [AREngine\_ARCameraIntrinsics](../../../modules/ar-engine/document.md#ga17948eef3aa7ff7f2fa8aff6a63b4b51) \*\*outIntrinsics)

 | 

Creates an object of the intrinsic camera parameters.

 |
| 

void [HMS\_AREngine\_ARCameraIntrinsics\_Destroy](../../../modules/ar-engine/document.md#ga09323e31d8bd08e5c1d60bccb118b68b) ([AREngine\_ARCameraIntrinsics](../../../modules/ar-engine/document.md#ga17948eef3aa7ff7f2fa8aff6a63b4b51) \*intrinsics)

 | 

Releases a specific object of intrinsic camera parameters.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARCameraIntrinsics\_GetDistortion](../../../modules/ar-engine/document.md#ga7caab88bb0e859921004ab1121ee2b5d) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARCameraIntrinsics](../../../modules/ar-engine/document.md#ga17948eef3aa7ff7f2fa8aff6a63b4b51) \*intrinsics, float \*outDistortion, int32\_t distortionNum)

 | 

Obtains the distortion parameters of a camera.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARCameraIntrinsics\_GetFocalLength](../../../modules/ar-engine/document.md#gab57c6586ac4d2da1b87f1c0394ffc1b3) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARCameraIntrinsics](../../../modules/ar-engine/document.md#ga17948eef3aa7ff7f2fa8aff6a63b4b51) \*intrinsics, float \*outFocalX, float \*outFocalY)

 | 

Obtains the focal length of a camera (in pixels).

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARCameraIntrinsics\_GetImageDimensions](../../../modules/ar-engine/document.md#gaab99bc9ba5b9b734ef11888fe2bb3f86) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARCameraIntrinsics](../../../modules/ar-engine/document.md#ga17948eef3aa7ff7f2fa8aff6a63b4b51) \*intrinsics, int32\_t \*outWidth, int32\_t \*outHeight)

 | 

Obtains the camera image dimensions, including the width and height (in pixels).

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARCameraIntrinsics\_GetPrincipalPoint](../../../modules/ar-engine/document.md#gaeb38c1df26e1af9d993574c7f13b8f5c) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARCameraIntrinsics](../../../modules/ar-engine/document.md#ga17948eef3aa7ff7f2fa8aff6a63b4b51) \*intrinsics, float \*outPrincipalX, float \*outPrincipalY)

 | 

Obtains the principal point of a camera, with the location of the point expressed in pixels.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARConfig\_Create](../../../modules/ar-engine/document.md#ga97376432184fe702f2451e32b52298fb) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, [AREngine\_ARConfig](../../../modules/ar-engine/document.md#gab0b32ef6018535fd30000f4b6d65f619) \*\*outConfig)

 | 

Creates a configuration object with a proper default configuration.

 |
| 

void [HMS\_AREngine\_ARConfig\_Destroy](../../../modules/ar-engine/document.md#gac86d0db69e8658f2f6bd267d7b288c0a) ([AREngine\_ARConfig](../../../modules/ar-engine/document.md#gab0b32ef6018535fd30000f4b6d65f619) \*config)

 | 

Releases the memory used by a specific configuration object.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARConfig\_GetARType](../../../modules/ar-engine/document.md#ga827ca7c2c2f288338f781e87e28ef996) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARConfig](../../../modules/ar-engine/document.md#gab0b32ef6018535fd30000f4b6d65f619) \*config, [AREngine\_ARType](../../../modules/ar-engine/document.md#ga987888aea7dcaa9abcdb64581c850bf5) \*type)

 | 

Obtains the AR capability type in use.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARConfig\_SetARType](../../../modules/ar-engine/document.md#gaf12b21d8591c5265f8a0e847b716d65c) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, [AREngine\_ARConfig](../../../modules/ar-engine/document.md#gab0b32ef6018535fd30000f4b6d65f619) \*config, [AREngine\_ARType](../../../modules/ar-engine/document.md#ga987888aea7dcaa9abcdb64581c850bf5) type)

 | 

Sets the AR capability type to use.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARConfig\_GetCameraPreviewMode](../../../modules/ar-engine/document.md#gaf4746b3377bd69a52d0587a582cc4679) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, [AREngine\_ARConfig](../../../modules/ar-engine/document.md#gab0b32ef6018535fd30000f4b6d65f619) \*config, [AREngine\_ARPreviewMode](../../../modules/ar-engine/document.md#gadef0f2099b106b872a014ef6551906ae) \*outMode)

 | 

Obtains the current preview mode.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARConfig\_SetCameraPreviewMode](../../../modules/ar-engine/document.md#gac5e6992e38516f75cc6faf1a34047f5d) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, [AREngine\_ARConfig](../../../modules/ar-engine/document.md#gab0b32ef6018535fd30000f4b6d65f619) \*config, [AREngine\_ARPreviewMode](../../../modules/ar-engine/document.md#gadef0f2099b106b872a014ef6551906ae) mode)

 | 

Sets the preview mode.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARConfig\_GetDepthMode](../../../modules/ar-engine/document.md#section6878812194715) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARConfig](../../../modules/ar-engine/document.md#gab0b32ef6018535fd30000f4b6d65f619) \*config, [AREngine\_ARDepthMode](../../../modules/ar-engine/document.md#section12321429115215) \*outDepthMode)

 | 

Obtains the current depth mode.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARConfig\_SetDepthMode](../../../modules/ar-engine/document.md#section12608229155413) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, [AREngine\_ARConfig](../../../modules/ar-engine/document.md#gab0b32ef6018535fd30000f4b6d65f619) \*config, [AREngine\_ARDepthMode](../../../modules/ar-engine/document.md#section12321429115215) depthMode)

 | 

Sets the depth mode.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARConfig\_GetFocusMode](../../../modules/ar-engine/document.md#gae92d8207f54468354ed52ad132e172f9) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARConfig](../../../modules/ar-engine/document.md#gab0b32ef6018535fd30000f4b6d65f619) \*config, [AREngine\_ARFocusMode](../../../modules/ar-engine/document.md#gaf50530faa0d094182a0db0c73b75d875) \*focusMode)

 | 

Obtains the current camera focus mode.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARConfig\_SetFocusMode](../../../modules/ar-engine/document.md#ga7bcf745a74196cb21dca5e4feec18325) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, [AREngine\_ARConfig](../../../modules/ar-engine/document.md#gab0b32ef6018535fd30000f4b6d65f619) \*config, [AREngine\_ARFocusMode](../../../modules/ar-engine/document.md#gaf50530faa0d094182a0db0c73b75d875) focusMode)

 | 

Sets the required camera focus mode.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARConfig\_GetMaxMapSize](../../../modules/ar-engine/document.md#ga65bae175f2ac6da6dca71988c3ac37df) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARConfig](../../../modules/ar-engine/document.md#gab0b32ef6018535fd30000f4b6d65f619) \*config, uint64\_t \*maxMapSize)

 | 

Obtains the maximum memory size for storing map data.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARConfig\_SetMaxMapSize](../../../modules/ar-engine/document.md#ga82fd530a4377b0c0e01c9031aa238372) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, [AREngine\_ARConfig](../../../modules/ar-engine/document.md#gab0b32ef6018535fd30000f4b6d65f619) \*config, uint64\_t maxMapSize)

 | 

Sets the maximum memory size for storing map data.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARConfig\_GetMeshMode](../../../modules/ar-engine/document.md#section5607016063) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, [AREngine\_ARConfig](../../../modules/ar-engine/document.md#gab0b32ef6018535fd30000f4b6d65f619) \*config, [AREngine\_ARMeshMode](../../../modules/ar-engine/document.md#section19436658201620) \*outMeshMode)

 | 

Obtains the current mesh mode.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARConfig\_SetMeshMode](../../../modules/ar-engine/document.md#section53081741287) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, [AREngine\_ARConfig](../../../modules/ar-engine/document.md#gab0b32ef6018535fd30000f4b6d65f619) \*config, [AREngine\_ARMeshMode](../../../modules/ar-engine/document.md#section19436658201620) meshMode)

 | 

Sets the mesh mode.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARConfig\_GetPlaneFindingMode](../../../modules/ar-engine/document.md#ga8aa9412802c98ece87d140b063f50839) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARConfig](../../../modules/ar-engine/document.md#gab0b32ef6018535fd30000f4b6d65f619) \*config, [AREngine\_ARPlaneFindingMode](../../../modules/ar-engine/document.md#gab8e7db52d819359026fc4a82815d3fff) \*planeFindingMode)

 | 

Obtains the current plane finding mode.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARConfig\_SetPlaneFindingMode](../../../modules/ar-engine/document.md#ga884a7db93778e24eef0dfaa794c45674) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, [AREngine\_ARConfig](../../../modules/ar-engine/document.md#gab0b32ef6018535fd30000f4b6d65f619) \*config, [AREngine\_ARPlaneFindingMode](../../../modules/ar-engine/document.md#gab8e7db52d819359026fc4a82815d3fff) planeFindingMode)

 | 

Sets the required plane finding mode.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARConfig\_GetPoseMode](../../../modules/ar-engine/document.md#section7289861874) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARConfig](../../../modules/ar-engine/document.md#gab0b32ef6018535fd30000f4b6d65f619) \*config, [AREngine\_ARPoseMode](../../../modules/ar-engine/document.md#section1249515330198) \*poseMode)

 | 

Obtains the alignment mode of the pose coordinate system output by the camera.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARConfig\_SetPoseMode](../../../modules/ar-engine/document.md#section53221628698) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, [AREngine\_ARConfig](../../../modules/ar-engine/document.md#gab0b32ef6018535fd30000f4b6d65f619) \*config, [AREngine\_ARPoseMode](../../../modules/ar-engine/document.md#section1249515330198) poseMode)

 | 

Sets the alignment mode of the pose coordinate system output by the camera.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARConfig\_GetPowerMode](../../../modules/ar-engine/document.md#ga3c02b15907c21a20e6efcd018750a29f) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARConfig](../../../modules/ar-engine/document.md#gab0b32ef6018535fd30000f4b6d65f619) \*config, [AREngine\_ARPowerMode](../../../modules/ar-engine/document.md#ga3d925e007e2847e69f22af68ec922507) \*powerMode)

 | 

Obtains the current power consumption mode.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARConfig\_SetPowerMode](../../../modules/ar-engine/document.md#gac5048a3977d04d75ba622a0411b03774) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, [AREngine\_ARConfig](../../../modules/ar-engine/document.md#gab0b32ef6018535fd30000f4b6d65f619) \*config, [AREngine\_ARPowerMode](../../../modules/ar-engine/document.md#ga3d925e007e2847e69f22af68ec922507) powerMode)

 | 

Sets the power consumption mode.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARConfig\_SetPreviewSize](../../../modules/ar-engine/document.md#ga8e9f74ef162604dc9bf07204237b45ab) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, [AREngine\_ARConfig](../../../modules/ar-engine/document.md#gab0b32ef6018535fd30000f4b6d65f619) \*config, uint32\_t width, uint32\_t height)

 | 

Sets preview image dimensions. Only a 4:3 aspect ratio is supported. An image exceeding this ratio will default to 1440 x 1080 px.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARConfig\_GetSemanticDenseMode](../../../modules/ar-engine/document.md#section1099254315514) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARConfig](../../../modules/ar-engine/document.md#gab0b32ef6018535fd30000f4b6d65f619) \*config, [AREngine\_ARSemanticDenseMode](../../../modules/ar-engine/document.md#section09971756142213) \*outSemanticDenseMode)

 | 

Obtains the set high-precision geometric reconstruction mode.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARConfig\_SetSemanticDenseMode](../../../modules/ar-engine/document.md#section1569718841012) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, [AREngine\_ARConfig](../../../modules/ar-engine/document.md#gab0b32ef6018535fd30000f4b6d65f619) \*config, [AREngine\_ARSemanticDenseMode](../../../modules/ar-engine/document.md#section09971756142213) semanticDenseMode)

 | 

Sets the high-precision geometric reconstruction mode.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARConfig\_GetSemanticMode](../../../modules/ar-engine/document.md#ga61325a1e0157e477c2ff95c1c0030567) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARConfig](../../../modules/ar-engine/document.md#gab0b32ef6018535fd30000f4b6d65f619) \*config, [AREngine\_ARSemanticMode](../../../modules/ar-engine/document.md#ga34d3000de29454b99d89406d288d6ed5) \*mode)

 | 

Obtains the configured semantic recognition mode.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARConfig\_SetSemanticMode](../../../modules/ar-engine/document.md#gaae87c1ef02b6e9bab123fae2086da248) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, [AREngine\_ARConfig](../../../modules/ar-engine/document.md#gab0b32ef6018535fd30000f4b6d65f619) \*config, [AREngine\_ARSemanticMode](../../../modules/ar-engine/document.md#ga34d3000de29454b99d89406d288d6ed5) mode)

 | 

Sets the required semantic recognition mode.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARConfig\_GetUpdateMode](../../../modules/ar-engine/document.md#gaf32a3cb1f345cd5a243683ecdec63cef) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARConfig](../../../modules/ar-engine/document.md#gab0b32ef6018535fd30000f4b6d65f619) \*config, [AREngine\_ARUpdateMode](../../../modules/ar-engine/document.md#gabd21cc975ee97b7fb2133af0068ebb5e) \*updateMode)

 | 

Obtains the current preview update mode.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARConfig\_SetUpdateMode](../../../modules/ar-engine/document.md#ga871c8aebc084cbba41220d255c46803b) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, [AREngine\_ARConfig](../../../modules/ar-engine/document.md#gab0b32ef6018535fd30000f4b6d65f619) \*config, [AREngine\_ARUpdateMode](../../../modules/ar-engine/document.md#gabd21cc975ee97b7fb2133af0068ebb5e) updateMode)

 | 

Sets the preview update mode.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARConfig\_SetPhotoStreamSize](../../../modules/ar-engine/document.md#section21861035164816)(const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, [AREngine\_ARConfig](../../../modules/ar-engine/document.md#gab0b32ef6018535fd30000f4b6d65f619) \*config, uint32\_t width, uint32\_t height)

 | 

Sets the resolution of an image captured from the photo stream when [AREngine\_ARImageStreamMode](../../../modules/ar-engine/document.md#section184201559356) is set to **ARENGINE\_IMAGE\_STREAM\_MODE\_PREVIEW\_AND\_PHOTO**. Only resolutions at the aspect ratio 4:3 are supported. If the aspect ratio is not 4:3, the device's maximum resolution at the aspect ratio 4:3 will be automatically used.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARConfig\_SetImageStreamMode](../../../modules/ar-engine/document.md#section10809428846)(const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, [AREngine\_ARConfig](../../../modules/ar-engine/document.md#gab0b32ef6018535fd30000f4b6d65f619) \*config, [AREngine\_ARImageStreamMode](../../../modules/ar-engine/document.md#section184201559356) mode)

 | 

Sets the image stream mode.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARConfig\_GetImageStreamMode](../../../modules/ar-engine/document.md#section387103819713)(const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, [AREngine\_ARConfig](../../../modules/ar-engine/document.md#gab0b32ef6018535fd30000f4b6d65f619) \*config, [AREngine\_ARImageStreamMode](../../../modules/ar-engine/document.md#section184201559356) \*outMode)

 | 

Obtains the image stream mode.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARFrame\_AcquireCamera](../../../modules/ar-engine/document.md#ga5295c975a0ff3d633a1dde5a8eb70863) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARFrame](../../../modules/ar-engine/document.md#gaf35f728a1179ef54a3eba9f1cf021719) \*frame, [AREngine\_ARCamera](../../../modules/ar-engine/document.md#ga7bdcf1fb36c404d36e09ad70d2545d92) \*\*outCamera)

 | 

Obtains the camera parameter object of the current frame.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARFrame\_AcquireCameraImage](../../../modules/ar-engine/document.md#gad5619c3cbd2b9ea0cfeff22b72f8d81d) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARFrame](../../../modules/ar-engine/document.md#gaf35f728a1179ef54a3eba9f1cf021719) \*frame, [AREngine\_ARImage](../../../modules/ar-engine/document.md#gabfee13b0076f2f00b7efdef2717add59) \*\*outImage)

 | 

Obtains the image of the current frame of the camera.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARFrame\_AcquireCameraPhotoImage](../../../modules/ar-engine/document.md#section18751333994)(const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARFrame](../../../modules/ar-engine/document.md#gaf35f728a1179ef54a3eba9f1cf021719)\*frame, [HMS\_AREngine\_PhotoAvailableCallback](../../../modules/ar-engine/document.md#section430673420224) photoCallback)

 | 

Obtains the photo stream image of the current frame.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARFrame\_AcquireDepthConfidenceImage](../../../modules/ar-engine/document.md#section4424501286) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARFrame](../../../modules/ar-engine/document.md#gaf35f728a1179ef54a3eba9f1cf021719) \*frame, [AREngine\_ARImage](../../../modules/ar-engine/document.md#gabfee13b0076f2f00b7efdef2717add59) \*\*outConfidenceImage)

 | 

Obtains the depth confidence map of the current frame.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARFrame\_AcquireDepthImage16Bits](../../../modules/ar-engine/document.md#section138574584154) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARFrame](../../../modules/ar-engine/document.md#gaf35f728a1179ef54a3eba9f1cf021719) \*frame, [AREngine\_ARImage](../../../modules/ar-engine/document.md#gabfee13b0076f2f00b7efdef2717add59) \*\*outDepthImage);

 | 

Obtains the depth image of the current frame.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARFrame\_AcquirePointCloud](../../../modules/ar-engine/document.md#ga877f7fc9d9c303f1fd8efb00ec383b34) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARFrame](../../../modules/ar-engine/document.md#gaf35f728a1179ef54a3eba9f1cf021719) \*frame, [AREngine\_ARPointCloud](../../../modules/ar-engine/document.md#gacc054cea4851be61b160f32b433737fc) \*\*outPointCloud)

 | 

Returns the point cloud data of the current frame.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARFrame\_AcquireSceneMesh](../../../modules/ar-engine/document.md#section25711548111020) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARFrame](../../../modules/ar-engine/document.md#gaf35f728a1179ef54a3eba9f1cf021719) \*frame, [AREngine\_ARSceneMesh](../../../modules/ar-engine/document.md#section543212520614) \*\*outSceneMesh)

 | 

Obtains the mesh information of the current frame.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARFrame\_AcquireSemanticDenseData](../../../modules/ar-engine/document.md#section17136162216547) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARFrame](../../../modules/ar-engine/document.md#gaf35f728a1179ef54a3eba9f1cf021719) \*frame, [AREngine\_ARSemanticDenseData](../../../modules/ar-engine/document.md#section1410813229144) \*\*outSemanticDenseData);

 | 

Obtains the high-precision geometric reconstruction object data of the current frame.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARFrame\_Create](../../../modules/ar-engine/document.md#gadfcb9589137a39c5afcb217e18853a9d) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, [AREngine\_ARFrame](../../../modules/ar-engine/document.md#gaf35f728a1179ef54a3eba9f1cf021719) \*\*outFrame)

 | 

Creates an [AREngine\_ARFrame](../../../modules/ar-engine/document.md#gaf35f728a1179ef54a3eba9f1cf021719) object and stores the pointer in _\*_**outFrame**.

 |
| 

void [HMS\_AREngine\_ARFrame\_Destroy](../../../modules/ar-engine/document.md#ga0ca6a470025dbccb44b4fdefc26513f6) ([AREngine\_ARFrame](../../../modules/ar-engine/document.md#gaf35f728a1179ef54a3eba9f1cf021719) \*frame)

 | 

Deletes the current [AREngine\_ARFrame](../../../modules/ar-engine/document.md#gaf35f728a1179ef54a3eba9f1cf021719) object.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARFrame\_GetDisplayGeometryChanged](../../../modules/ar-engine/document.md#ga4fb55932c19ef9c49523a0a5385a9242) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARFrame](../../../modules/ar-engine/document.md#gaf35f728a1179ef54a3eba9f1cf021719) \*frame, int32\_t \*outGeometryChangeState)

 | 

Obtains whether the display (length, width, and rotation) changes.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARFrame\_GetTimestamp](../../../modules/ar-engine/document.md#ga266c2e5c80a961163d3422b96b079701) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARFrame](../../../modules/ar-engine/document.md#gaf35f728a1179ef54a3eba9f1cf021719) \*frame, int64\_t \*outTimestampNs)

 | 

Obtains the timestamp information (in nanoseconds) of the current frame.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARFrame\_GetUpdatedTrackables](../../../modules/ar-engine/document.md#ga0fc74148f836093108b85ab4c7ecdd1c) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARFrame](../../../modules/ar-engine/document.md#gaf35f728a1179ef54a3eba9f1cf021719) \*frame, [AREngine\_ARTrackableType](../../../modules/ar-engine/document.md#ga993948a19fd2bdfa5b946e13a8d4fe3d) filterType, [AREngine\_ARTrackableList](../../../modules/ar-engine/document.md#gae69e4963b595036fc5e6119a055bb205) \*outTrackableList)

 | 

Obtains the updated trackable object of the specified type after [HMS\_AREngine\_ARSession\_Update](../../../modules/ar-engine/document.md#ga1d1cacf372a8011a439f0e4e76994259) is called.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARFrame\_HitTest](../../../modules/ar-engine/document.md#gad9377f19261d5bbc2044497729b4e0df) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARFrame](../../../modules/ar-engine/document.md#gaf35f728a1179ef54a3eba9f1cf021719) \*frame, float pixelX, float pixelY, [AREngine\_ARHitResultList](../../../modules/ar-engine/document.md#ga1f2369453412bd4d77ab8f5aa2d52bb3) \*hitResultList)

 | 

Casts a ray from the camera, with the direction of the ray determined by the points (**pixelX**, **pixelY**) in the preview area. **pixelX** and **pixelY** can be obtained through the XComponent's [DispatchTouchEvent](../../../../../../application-framework/arkui/c-api/structs/oh-nativexcomponent-callback/document.md#dispatchtouchevent) event.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARFrame\_TransformDisplayUvCoords](../../../modules/ar-engine/document.md#ga4c7699abab9b82369c0d42b496667fc7) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARFrame](../../../modules/ar-engine/document.md#gaf35f728a1179ef54a3eba9f1cf021719) \*frame, int32\_t elementSize, const float \*uvsIn, float \*uvsOut)

 | 

Converts the texture coordinates so that the background image captured by the camera can be correctly displayed.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARHitResult\_AcquireNewAnchor](../../../modules/ar-engine/document.md#ga30abe7b3457c991815dd79fcfaf26018) ([AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, [AREngine\_ARHitResult](../../../modules/ar-engine/document.md#gaeb304c8b21122eb7ffda7403316a3507) \*hitResult, [AREngine\_ARAnchor](../../../modules/ar-engine/document.md#ga76c16c9d68ba9a3b76f1869c60d8ca1d) \*\*outAnchor)

 | 

Creates an anchor at the hit position.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARHitResult\_AcquireTrackable](../../../modules/ar-engine/document.md#gac3a02e30bb7706d87c4c29d38b363840) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARHitResult](../../../modules/ar-engine/document.md#gaeb304c8b21122eb7ffda7403316a3507) \*hitResult, [AREngine\_ARTrackable](../../../modules/ar-engine/document.md#ga54808ebd1a6ed026494acdd945c4f970) \*\*outTrackable)

 | 

Obtains the trackable object that is hit.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARHitResult\_Create](../../../modules/ar-engine/document.md#ga4b06bcca0f6fc0b081ef8210765d9c91) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, [AREngine\_ARHitResult](../../../modules/ar-engine/document.md#gaeb304c8b21122eb7ffda7403316a3507) \*\*outHitResult)

 | 

Creates an empty hit testing result object.

 |
| 

void [HMS\_AREngine\_ARHitResult\_Destroy](../../../modules/ar-engine/document.md#ga3b3796d7186cb09c4861ebabe2d5b654) ([AREngine\_ARHitResult](../../../modules/ar-engine/document.md#gaeb304c8b21122eb7ffda7403316a3507) \*hitResult)

 | 

Releases the memory used by the hit testing result object.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARHitResult\_GetDistance](../../../modules/ar-engine/document.md#ga6929e52bb352622806d2298497c6b4c8) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARHitResult](../../../modules/ar-engine/document.md#gaeb304c8b21122eb7ffda7403316a3507) \*hitResult, float \*outDistance)

 | 

Returns the distance from the camera to the hit location, in meters.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARHitResult\_GetHitPose](../../../modules/ar-engine/document.md#ga8beaa085410712425041e81f9bc6aa09) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARHitResult](../../../modules/ar-engine/document.md#gaeb304c8b21122eb7ffda7403316a3507) \*hitResult, [AREngine\_ARPose](../../../modules/ar-engine/document.md#gab2fa63142ebfb09f0c2ddf88cdb86604) \*outPose)

 | 

Obtains the pose of an intersection.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARHitResultList\_Create](../../../modules/ar-engine/document.md#gad5dfe929e7952954764d05b8d69abace) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, [AREngine\_ARHitResultList](../../../modules/ar-engine/document.md#ga1f2369453412bd4d77ab8f5aa2d52bb3) \*\*outHitResultList)

 | 

Creates a list of hit testing result objects.

 |
| 

void [HMS\_AREngine\_ARHitResultList\_Destroy](../../../modules/ar-engine/document.md#gaae065ef9a28168b420c96b72ca80c892) ([AREngine\_ARHitResultList](../../../modules/ar-engine/document.md#ga1f2369453412bd4d77ab8f5aa2d52bb3) \*hitResultList)

 | 

Releases the list of hit testing result objects, as well as all hit testing result objects in the list.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARHitResultList\_GetItem](../../../modules/ar-engine/document.md#gaf165c7a1c9ae003cac2a1c2ac2e5e5c4) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARHitResultList](../../../modules/ar-engine/document.md#ga1f2369453412bd4d77ab8f5aa2d52bb3) \*hitResultList, int32\_t index, [AREngine\_ARHitResult](../../../modules/ar-engine/document.md#gaeb304c8b21122eb7ffda7403316a3507) \*outHitResult)

 | 

Obtains the hit testing result object at a specific index from the list of hit testing results.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARHitResultList\_GetSize](../../../modules/ar-engine/document.md#ga131d081663d457c594664c977bd9033c) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARHitResultList](../../../modules/ar-engine/document.md#ga1f2369453412bd4d77ab8f5aa2d52bb3) \*hitResultList, int32\_t \*outSize)

 | 

Obtains the number of objects in the list of hit testing result objects.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARImage\_GetFormat](../../../modules/ar-engine/document.md#ga852b211c7e285ccc154295eb1c604f37) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARImage](../../../modules/ar-engine/document.md#gabfee13b0076f2f00b7efdef2717add59) \*image, [AREngine\_ARImageFormat](../../../modules/ar-engine/document.md#gadfcf7a1211ed12a90f377610d0f838ac) \*outFormat)

 | 

Obtains the image format of the current frame.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARImage\_GetHeight](../../../modules/ar-engine/document.md#ga34c21703e40868ce0fe5795fa82a08fa) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARImage](../../../modules/ar-engine/document.md#gabfee13b0076f2f00b7efdef2717add59) \*image, int32\_t \*outHeight)

 | 

Obtains the image height of the current frame.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARImage\_GetWidth](../../../modules/ar-engine/document.md#ga2c2454e9611dc68e26b8fefb39021597) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARImage](../../../modules/ar-engine/document.md#gabfee13b0076f2f00b7efdef2717add59) \*image, int32\_t \*outWidth)

 | 

Obtains the image width of the current frame.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARImage\_GetNativeBuffer](../../../modules/ar-engine/document.md#section367418528228) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARImage](../../../modules/ar-engine/document.md#gabfee13b0076f2f00b7efdef2717add59) \*image, [OH\_NativeBuffer](../../../../../arkgraphics-2d/c-apis/modules/oh-nativebuffer/document.md) \*\*outNativeBuffer);

 | 

Obtains the NativeBuffer data of the current frame's image object.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARImage\_GetPlaneCount](../../../modules/ar-engine/document.md#ga107fbf6737b499aea941fbbfeab1b3e9) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARImage](../../../modules/ar-engine/document.md#gabfee13b0076f2f00b7efdef2717add59) \*image, int32\_t \*outCount)

 | 

Obtains the number of planes in the current frame.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARImage\_GetPlaneData](../../../modules/ar-engine/document.md#gaedc5247eb982443c3f8a2dc8cfd5fdee) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARImage](../../../modules/ar-engine/document.md#gabfee13b0076f2f00b7efdef2717add59) \*image, int32\_t planeIndex, const uint8\_t \*\*outData, int32\_t \*outLength)

 | 

Obtains the plane data in the current frame.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARImage\_GetPlanePixelStride](../../../modules/ar-engine/document.md#gac31f741115e6936f7b8e3ef94579d270) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARImage](../../../modules/ar-engine/document.md#gabfee13b0076f2f00b7efdef2717add59) \*image, int32\_t planeIndex, int32\_t \*outPixelStride)

 | 

Obtains the distance between the start points of two consecutive pixels in an image, in bytes. The pixel stride is always greater than 0.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARImage\_GetPlaneRowStride](../../../modules/ar-engine/document.md#ga35e66d4a869539d2261e41df17730691) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARImage](../../../modules/ar-engine/document.md#gabfee13b0076f2f00b7efdef2717add59) \*image, int32\_t planeIndex, int32\_t \*outRowStride)

 | 

Obtains the number of bytes between the start positions of two consecutive pixel lines in an image. The line spacing is always greater than 0.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARImage\_GetTimestamp](../../../modules/ar-engine/document.md#ga7d2c7f1d596d41bfe1c181057283b740) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARImage](../../../modules/ar-engine/document.md#gabfee13b0076f2f00b7efdef2717add59) \*image, int64\_t \*outTimestamp)

 | 

Obtains the timestamp of an image.

 |
| 

void [HMS\_AREngine\_ARImage\_Release](../../../modules/ar-engine/document.md#ga42fd222576edf6507f6d319a3374cd94) ([AREngine\_ARImage](../../../modules/ar-engine/document.md#gabfee13b0076f2f00b7efdef2717add59) \*image)

 | 

Releases the image object of the current frame, that is, the object created by [HMS\_AREngine\_ARFrame\_AcquireCameraImage](../../../modules/ar-engine/document.md#gad5619c3cbd2b9ea0cfeff22b72f8d81d).

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARPlane\_AcquireSubsumedBy](../../../modules/ar-engine/document.md#ga56686d6a5ff45fcb04812538aa807ac3) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARPlane](../../../modules/ar-engine/document.md#ga76f9bdb23634312b8488fcbaff4aa9b5) \*plane, [AREngine\_ARPlane](../../../modules/ar-engine/document.md#ga76f9bdb23634312b8488fcbaff4aa9b5) \*\*outSubsumedBy)

 | 

Obtains the parent plane of a plane (a parent plane is generated when a plane is merged with another one). If there is no parent plane, **NULL** is returned.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARPlane\_GetCenterPose](../../../modules/ar-engine/document.md#gabbb03027afb984be8542d00d2eebd063) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARPlane](../../../modules/ar-engine/document.md#ga76f9bdb23634312b8488fcbaff4aa9b5) \*plane, [AREngine\_ARPose](../../../modules/ar-engine/document.md#gab2fa63142ebfb09f0c2ddf88cdb86604) \*outPose)

 | 

Obtains the pose information for the conversion from the local coordinate system of a plane to the world coordinate system.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARPlane\_GetExtentX](../../../modules/ar-engine/document.md#ga49db45eb6072384247a057c403a69c8d) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARPlane](../../../modules/ar-engine/document.md#ga76f9bdb23634312b8488fcbaff4aa9b5) \*plane, float \*outExtentX)

 | 

Obtains the length of the plane's bounding rectangle along the X axis of the plane's local coordinate system, such as the width of the rectangle.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARPlane\_GetExtentZ](../../../modules/ar-engine/document.md#ga4daf6a365f1107f146c5d264dfee292c) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARPlane](../../../modules/ar-engine/document.md#ga76f9bdb23634312b8488fcbaff4aa9b5) \*plane, float \*outExtentZ)

 | 

Obtains the length of the plane's bounding rectangle along the Z axis of the plane's local coordinate system, such as the height of the rectangle.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARPlane\_GetLabel](../../../modules/ar-engine/document.md#ga913456f9586c82adcdbcae291ec8e17c) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARPlane](../../../modules/ar-engine/document.md#ga76f9bdb23634312b8488fcbaff4aa9b5) \*plane, [AREngine\_ARSemanticPlaneLabel](../../../modules/ar-engine/document.md#gafbb6b69fefdc417ba6437ce2fe587cb1) \*label)

 | 

Obtains the semantic type of a plane, such as desktop and floor.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARPlane\_GetPolygon](../../../modules/ar-engine/document.md#ga3537ce62e6a92dcdbddff0f39de0fae3) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARPlane](../../../modules/ar-engine/document.md#ga76f9bdb23634312b8488fcbaff4aa9b5) \*plane, float \*outPolygonXz, int32\_t polygonSize)

 | 

Obtains the 2D vertex array of the detected plane, in the format of \[x1, z1, x2, z2, ...\].

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARPlane\_GetPolygonSize](../../../modules/ar-engine/document.md#ga98760556eee2a4a69c33699b7ce3edc6) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARPlane](../../../modules/ar-engine/document.md#ga76f9bdb23634312b8488fcbaff4aa9b5) \*plane, int32\_t \*outPolygonSize)

 | 

Obtains the size of the 2D vertex array of the detected plane.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARPlane\_GetType](../../../modules/ar-engine/document.md#ga8aa35ca398b38eee8c53bd1db8d6ab88) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARPlane](../../../modules/ar-engine/document.md#ga76f9bdb23634312b8488fcbaff4aa9b5) \*plane, [AREngine\_ARPlaneType](../../../modules/ar-engine/document.md#ga895db37a92155584c5448bee30a8beab) \*outPlaneType)

 | 

Obtains the plane type.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARPlane\_IsPoseInExtents](../../../modules/ar-engine/document.md#ga8ded2552569a9e89c1befe8f15123af6) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARPlane](../../../modules/ar-engine/document.md#ga76f9bdb23634312b8488fcbaff4aa9b5) \*plane, const [AREngine\_ARPose](../../../modules/ar-engine/document.md#gab2fa63142ebfb09f0c2ddf88cdb86604) \*pose, int32\_t \*outPoseInExtents)

 | 

Checks whether a pose is within the plane's bounding rectangle.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARPlane\_IsPoseInPolygon](../../../modules/ar-engine/document.md#gab00d22a9c927a2745821023e8e72a8d0) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARPlane](../../../modules/ar-engine/document.md#ga76f9bdb23634312b8488fcbaff4aa9b5) \*plane, const [AREngine\_ARPose](../../../modules/ar-engine/document.md#gab2fa63142ebfb09f0c2ddf88cdb86604) \*pose, int32\_t \*outPoseInPolygon)

 | 

Checks whether a pose is within the plane's bounding polygon.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARPoint\_GetOrientationMode](../../../modules/ar-engine/document.md#gad869ed2a4ac6409bf94c768d9d1d8127) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARPoint](../../../modules/ar-engine/document.md#gac7b6923d92487d68e77543dd223364d6) \*point, [AREngine\_ARPointOrientationMode](../../../modules/ar-engine/document.md#ga0e2893593f4372954fd97519e0a63855) \*outOrientationMode)

 | 

Obtains the orientation mode of an input point.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARPoint\_GetPose](../../../modules/ar-engine/document.md#ga8255eece88d8dc76c554eed360fb7c7b) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARPoint](../../../modules/ar-engine/document.md#gac7b6923d92487d68e77543dd223364d6) \*point, [AREngine\_ARPose](../../../modules/ar-engine/document.md#gab2fa63142ebfb09f0c2ddf88cdb86604) \*outPose)

 | 

Obtains the pose information of an input point.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARPointCloud\_GetData](../../../modules/ar-engine/document.md#ga4061cacb3f3ce45e529acb9afbcdc5ce) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARPointCloud](../../../modules/ar-engine/document.md#gacc054cea4851be61b160f32b433737fc) \*pointCloud, const float \*\*outPointCloudData)

 | 

Obtains the coordinates of all points in a point cloud, as well as their confidence array.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARPointCloud\_GetNumberOfPoints](../../../modules/ar-engine/document.md#gad9701fe82b6468f33f6741cc7f347d45) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARPointCloud](../../../modules/ar-engine/document.md#gacc054cea4851be61b160f32b433737fc) \*pointCloud, int32\_t \*outNumberOfPoints)

 | 

Obtains the coordinates of all points in a point cloud, as well as their confidence array size.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARPointCloud\_GetTimestamp](../../../modules/ar-engine/document.md#ga9e430d52fa372903bcbe40ca5f6a9d9d) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARPointCloud](../../../modules/ar-engine/document.md#gacc054cea4851be61b160f32b433737fc) \*pointCloud, int64\_t \*outTimestampNs)

 | 

Obtains the timestamp when the current feature point cloud is detected, in nanoseconds.

 |
| 

void [HMS\_AREngine\_ARPointCloud\_Release](../../../modules/ar-engine/document.md#ga3751c56632f7f6d383cf9409ec6769bc) ([AREngine\_ARPointCloud](../../../modules/ar-engine/document.md#gacc054cea4851be61b160f32b433737fc) \*pointCloud)

 | 

Releases the memory used by the point cloud object.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARPose\_Create](../../../modules/ar-engine/document.md#gafb471f39563ca1a4947d4f87c77e24e2) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, const float \*poseRaw, const uint32\_t poseRawSize, [AREngine\_ARPose](../../../modules/ar-engine/document.md#gab2fa63142ebfb09f0c2ddf88cdb86604) \*\*outPose)

 | 

Allocates and initializes a new pose object.

 |
| 

void [HMS\_AREngine\_ARPose\_Destroy](../../../modules/ar-engine/document.md#gab988254f4654c8aaadb5740061846057) ([AREngine\_ARPose](../../../modules/ar-engine/document.md#gab2fa63142ebfb09f0c2ddf88cdb86604) \*pose)

 | 

Releases the memory used by the pose object.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARPose\_GetMatrix](../../../modules/ar-engine/document.md#ga787f4daf9efd13c79737ef18cef6d7c7) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARPose](../../../modules/ar-engine/document.md#gab2fa63142ebfb09f0c2ddf88cdb86604) \*pose, float \*outMatrixColMajor4x4, int32\_t matrixColMajor4x4Size)

 | 

Converts the pose data into a 4 × 4 matrix.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARPose\_GetPoseRaw](../../../modules/ar-engine/document.md#ga1ee66c006ffe8255cc04f2a24c277709) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARPose](../../../modules/ar-engine/document.md#gab2fa63142ebfb09f0c2ddf88cdb86604) \*pose, float \*outPoseRaw, int32\_t poseRawSize)

 | 

Extracts pose data from a pose object.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARSceneMesh\_AcquireIndexList](../../../modules/ar-engine/document.md#section7629354145) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARSceneMesh](../../../modules/ar-engine/document.md#section543212520614) \*sceneMesh, int32\_t \*outData, int32\_t dataSize)

 | 

Obtains the index set of mesh faces.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARSceneMesh\_AcquireIndexListSize](../../../modules/ar-engine/document.md#section12621161917152) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARSceneMesh](../../../modules/ar-engine/document.md#section543212520614) \*sceneMesh, int32\_t \*outSize)

 | 

Obtains the number of indexes of the mesh faces.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARSceneMesh\_AcquireVertexList](../../../modules/ar-engine/document.md#section2126723166) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARSceneMesh](../../../modules/ar-engine/document.md#section543212520614) \*sceneMesh, float \*outData, int32\_t dataSize)

 | 

Obtains the vertex set of a mesh.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARSceneMesh\_AcquireVertexNormalList](../../../modules/ar-engine/document.md#section115249588168) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARSceneMesh](../../../modules/ar-engine/document.md#section543212520614) \*sceneMesh, float \*outData, int32\_t dataSize)

 | 

Obtains the normal vector set of the mesh faces.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARSceneMesh\_AcquireVerticesSize](../../../modules/ar-engine/document.md#section1860218429179) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARSceneMesh](../../../modules/ar-engine/document.md#section543212520614) \*sceneMesh, int32\_t \*outSize)

 | 

Obtains the number of vertices of a mesh.

 |
| 

void [HMS\_AREngine\_ARSceneMesh\_Release](../../../modules/ar-engine/document.md#section446832931813) ([AREngine\_ARSceneMesh](../../../modules/ar-engine/document.md#section543212520614) \*SceneMesh)

 | 

Releases the mesh information of the current frame.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARSemanticDense\_AcquireCubeData](../../../modules/ar-engine/document.md#section7554459949) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARSemanticDenseData](../../../modules/ar-engine/document.md#section1410813229144) \*semanticDenseData, [AREngine\_ARSemanticDenseCubeData](../../structs/arengine-arsemanticdensecubedata/document.md) \*\*outCubeData)

 | 

Obtains the cube data from the recognized high-precision geometric reconstruction object data.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARSemanticDense\_AcquireCubeDataSize](../../../modules/ar-engine/document.md#section383013458212) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARSemanticDenseData](../../../modules/ar-engine/document.md#section1410813229144) \*semanticDenseData, int64\_t \*outSize)

 | 

Obtains the cube count from the recognized high-precision geometric reconstruction object data.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARSemanticDense\_AcquirePointData](../../../modules/ar-engine/document.md#section288942515910) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARSemanticDenseData](../../../modules/ar-engine/document.md#section1410813229144) \*semanticDenseData, [AREngine\_ARSemanticDensePointData](../../structs/arengine-arsemanticdensepointdata/document.md) \*\*outPointData)

 | 

Obtains the dense point cloud data from the recognized high-precision geometric reconstruction object data.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARSemanticDense\_AcquirePointDataSize](../../../modules/ar-engine/document.md#section6669112114532) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARSemanticDenseData](../../../modules/ar-engine/document.md#section1410813229144) \*semanticDenseData, int64\_t \*outSize)

 | 

Obtains the dense point cloud size from the recognized high-precision geometric reconstruction object data.

 |
| 

void [HMS\_AREngine\_ARSemanticDense\_Release](../../../modules/ar-engine/document.md#section390280482) ([AREngine\_ARSemanticDenseData](../../../modules/ar-engine/document.md#section1410813229144) \*semanticDenseData)

 | 

Releases a high-precision geometric reconstruction object.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARSession\_AcquireNewAnchor](../../../modules/ar-engine/document.md#ga2ae6dee4baab7cf2c5d0cdd1c845cf0c) ([AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARPose](../../../modules/ar-engine/document.md#gab2fa63142ebfb09f0c2ddf88cdb86604) \*pose, [AREngine\_ARAnchor](../../../modules/ar-engine/document.md#ga76c16c9d68ba9a3b76f1869c60d8ca1d) \*\*outAnchor)

 | 

Creates an anchor for continuous tracking.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARSession\_Configure](../../../modules/ar-engine/document.md#ga6394ae995148abbe3d00082817bf320a) ([AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARConfig](../../../modules/ar-engine/document.md#gab0b32ef6018535fd30000f4b6d65f619) \*config)

 | 

Configures an [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) session.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARSession\_Create](../../../modules/ar-engine/document.md#ga47713cb18234569e03b5216b6c8442d3) (void \*env, void \*applicationContext, [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*\*outSessionPointer)

 | 

Creates an [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) session.

 |
| 

void [HMS\_AREngine\_ARSession\_Destroy](../../../modules/ar-engine/document.md#ga3a2be9998c9cd6373ff1f5209b645a95) ([AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session)

 | 

Releases the resources used by the [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) session.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARSession\_GetCameraConfig](../../../modules/ar-engine/document.md#ga31b28b049ac25b94c02fb27ca56c497d) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, [AREngine\_ARCameraConfig](../../../modules/ar-engine/document.md#ga9b7a5a2082a4127f85a1c9a95cb9acba) \*outCameraConfig)

 | 

Obtains the camera configuration information.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARSession\_GetAllAnchors](../../../modules/ar-engine/document.md#ga4828823e5f3cc1067dbd6a2c8b9c9635) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, [AREngine\_ARAnchorList](../../../modules/ar-engine/document.md#ga516a7f0954dcfda438799aa9e7c6e872) \*outAnchorList)

 | 

Obtains all anchors, including anchors in all states contained in [AREngine\_ARTrackingState](../../../modules/ar-engine/document.md#gaae57d2f58331e1033b60cdb2d506a382).

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARSession\_GetAllTrackables](../../../modules/ar-engine/document.md#gac5b39338f95317671d8de6d4f409cf9c) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, [AREngine\_ARTrackableType](../../../modules/ar-engine/document.md#ga993948a19fd2bdfa5b946e13a8d4fe3d) filterType, [AREngine\_ARTrackableList](../../../modules/ar-engine/document.md#gae69e4963b595036fc5e6119a055bb205) \*outTrackableList)

 | 

Obtains the list of all trackable objects of the specified type.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARSession\_Pause](../../../modules/ar-engine/document.md#ga09dedb5c633141321591db0981629de1) ([AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session)

 | 

Pauses the session, stops the camera preview stream, and releases the camera (otherwise, other apps will not be able to use the camera service), without clearing the plane and anchor data.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARSession\_Resume](../../../modules/ar-engine/document.md#ga7138d56b767738b8aadcbc74f4c328db) ([AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session)

 | 

Starts [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650), or restores [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) after [HMS\_AREngine\_ARSession\_Pause](../../../modules/ar-engine/document.md#ga09dedb5c633141321591db0981629de1) is called.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARSession\_SetCameraGLTexture](../../../modules/ar-engine/document.md#gac697e4be36db63ed6098f154aa9ac01c) ([AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, uint32\_t textureId)

 | 

Sets the OpenGL texture for storing the camera preview stream data.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARSession\_SetDisplayGeometry](../../../modules/ar-engine/document.md#ga3f23bf747def8303c3fb261a9e9a2286) ([AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, [AREngine\_ARPoseType](../../../modules/ar-engine/document.md#gae551da7b220b8b38140c3c28882e5010) rotation, int32\_t width, int32\_t height)

 | 

Sets the display height and width (in pixels).

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARSession\_Stop](../../../modules/ar-engine/document.md#ga0b7405ae0fc1e1257103192a2b7b48d3) ([AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session)

 | 

Stops AR Engine and the camera preview stream, clears the plane and anchor data, releases the camera, and terminates the session.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARSession\_Update](../../../modules/ar-engine/document.md#ga1d1cacf372a8011a439f0e4e76994259) ([AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, [AREngine\_ARFrame](../../../modules/ar-engine/document.md#gaf35f728a1179ef54a3eba9f1cf021719) \*outFrame)

 | 

Updates the computation result of AR Engine.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARTarget\_GetAxisAlignedBoundingBox](../../../modules/ar-engine/document.md#gaaf54fe7a3c38dbb4c0bcaa3c83dd0d76)(const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARTarget](../../../modules/ar-engine/document.md#ga9af9c1d51ed065f80b373824e0425fa0) \*target, float \*outAabb, int32\_t aabbSize)

 | 

Obtains the coordinates of the minimum bounding box of a semantic object, in the format of (xmin, ymin, zmin, xmax, ymax, zmax).

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARTarget\_GetCenterPose](../../../modules/ar-engine/document.md#gaa9a304640d54942be238a7ddd2c13276) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARTarget](../../../modules/ar-engine/document.md#ga9af9c1d51ed065f80b373824e0425fa0) \*target, [AREngine\_ARPose](../../../modules/ar-engine/document.md#gab2fa63142ebfb09f0c2ddf88cdb86604) \*outARPose)

 | 

Obtains the pose object for the conversion from the local coordinate system of the target semantic object to the world coordinate system.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARTarget\_GetRadius](../../../modules/ar-engine/document.md#ga0fb23a8217c7191f765b0d656160ffa1) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARTarget](../../../modules/ar-engine/document.md#ga9af9c1d51ed065f80b373824e0425fa0) \*target, float \*radius)

 | 

Obtains the sphere radius of a semantic object.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARTarget\_GetShapeType](../../../modules/ar-engine/document.md#ga6c702efd6c4fdc3eeb8f5dc38968ec65) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARTarget](../../../modules/ar-engine/document.md#ga9af9c1d51ed065f80b373824e0425fa0) \*target, [AREngine\_ARTargetShapeLabel](../../../modules/ar-engine/document.md#gaed68dc13cc314da98d79c88b12d3ae49) \*shape)

 | 

Obtains the shape type of a semantic object.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARTrackable\_AcquireNewAnchor](../../../modules/ar-engine/document.md#gacf03897f0ac28d338143f3fa350c1491) ([AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, [AREngine\_ARTrackable](../../../modules/ar-engine/document.md#ga54808ebd1a6ed026494acdd945c4f970) \*trackable, [AREngine\_ARPose](../../../modules/ar-engine/document.md#gab2fa63142ebfb09f0c2ddf88cdb86604) \*pose, [AREngine\_ARAnchor](../../../modules/ar-engine/document.md#ga76c16c9d68ba9a3b76f1869c60d8ca1d) \*\*outAnchor)

 | 

Creates an anchor object using the pose information of the trackable object. This anchor will be bound to the current trackable object.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARTrackable\_GetAnchors](../../../modules/ar-engine/document.md#gac7a3b98b0281f2e31ac3d9c47b0dffab) ([AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARTrackable](../../../modules/ar-engine/document.md#ga54808ebd1a6ed026494acdd945c4f970) \*trackable, [AREngine\_ARAnchorList](../../../modules/ar-engine/document.md#ga516a7f0954dcfda438799aa9e7c6e872) \*outAnchorList)

 | 

Obtains a list of anchor objects bound to the input trackable objects.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARTrackable\_GetTrackingState](../../../modules/ar-engine/document.md#ga7805739b2dbeae0d3b04242538a4a840) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARTrackable](../../../modules/ar-engine/document.md#ga54808ebd1a6ed026494acdd945c4f970) \*trackable, [AREngine\_ARTrackingState](../../../modules/ar-engine/document.md#gaae57d2f58331e1033b60cdb2d506a382) \*outTrackingState)

 | 

Obtains the tracking state of the current trackable object.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARTrackable\_GetType](../../../modules/ar-engine/document.md#ga72c800291d0df799fa795db3d3485e4f) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARTrackable](../../../modules/ar-engine/document.md#ga54808ebd1a6ed026494acdd945c4f970) \*trackable, [AREngine\_ARTrackableType](../../../modules/ar-engine/document.md#ga993948a19fd2bdfa5b946e13a8d4fe3d) \*outTrackableType)

 | 

Obtains the type of a trackable object.

 |
| 

void [HMS\_AREngine\_ARTrackable\_Release](../../../modules/ar-engine/document.md#ga6ec735cd18e955442f29416ff58ddd64) ([AREngine\_ARTrackable](../../../modules/ar-engine/document.md#ga54808ebd1a6ed026494acdd945c4f970) \*trackable)

 | 

Releases a trackable object.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARTrackableList\_AcquireItem](../../../modules/ar-engine/document.md#gab1782eeeeddc01b77a140af915cb351c) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARTrackableList](../../../modules/ar-engine/document.md#gae69e4963b595036fc5e6119a055bb205) \*trackableList, int32\_t index, [AREngine\_ARTrackable](../../../modules/ar-engine/document.md#ga54808ebd1a6ed026494acdd945c4f970) \*\*outTrackable)

 | 

Obtains the object at a specific index from the trackable object list.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARTrackableList\_Create](../../../modules/ar-engine/document.md#ga7860d63545ab862e9f3b1fe0a8a83d42) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, [AREngine\_ARTrackableList](../../../modules/ar-engine/document.md#gae69e4963b595036fc5e6119a055bb205) \*\*outTrackableList)

 | 

Creates a list of trackable objects.

 |
| 

void [HMS\_AREngine\_ARTrackableList\_Destroy](../../../modules/ar-engine/document.md#gad6e2ffd71d7cdaa3ae553937437b37c8) ([AREngine\_ARTrackableList](../../../modules/ar-engine/document.md#gae69e4963b595036fc5e6119a055bb205) \*trackableList)

 | 

Releases the list of trackable objects, along with all the anchor references it holds.

 |
| 

[AREngine\_ARStatus](../../../modules/ar-engine/document.md#gacc90fb9320a5ba10bb23f7a37440885d) [HMS\_AREngine\_ARTrackableList\_GetSize](../../../modules/ar-engine/document.md#gad9729d4436f3d969286f31b33d07513e) (const [AREngine\_ARSession](../../../modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) \*session, const [AREngine\_ARTrackableList](../../../modules/ar-engine/document.md#gae69e4963b595036fc5e6119a055bb205) \*trackableList, int32\_t \*outSize)

 | 

Obtains the number of trackable objects in the list.

 |
