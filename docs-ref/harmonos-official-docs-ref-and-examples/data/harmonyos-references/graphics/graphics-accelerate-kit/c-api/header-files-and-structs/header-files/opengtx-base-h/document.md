# opengtx\_base.h

#### Overview

Declares OpenGTX APIs used for both the OpenGL ES and Vulkan graphics APIs.

**Library**: libopengtx.so

**System capability**: SystemCapability.GraphicsGame.RenderAccelerate

**Start version**: 5.0.0(12)

**Related module**: [GraphicsAccelerate](../../../modules/graphicsaccelerate/document.md)

#### Summary

#### \[h2\]Structs

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

struct [OpenGTX\_ConfigDescription](../../structs/opengtx-configdescription/document.md)

 | 

Describes the OpenGTX attribute settings.

 |
| 

struct [OpenGTX\_GameSceneInfo](../../structs/opengtx-gamesceneinfo/document.md)

 | 

Describes the game scene information. This struct is passed by a game app after obtaining the scene information.

 |
| 

struct [OpenGTX\_FrameRenderInfo](../../structs/opengtx-framerenderinfo/document.md)

 | 

Describes the frame rendering information. This struct is passed by a game app after obtaining the frame attributes.

 |
| 

struct [OpenGTX\_NetworkInfo](../../structs/opengtx-networkinfo/document.md)

 | 

Describes the current device network information. This struct is passed by a game app after obtaining the network information.

 |
| 

struct [OpenGTX\_ResolutionValue](../../structs/opengtx-resolutionvalue/document.md)

 | 

Describes the resolution of a game app.

 |
| 

struct [OpenGTX\_Vector3](../../structs/opengtx-vector3/document.md)

 | 

Describes an OpenGTX 3D vector.

 |
| 

struct [OpenGTX\_NetworkLatency](../../structs/opengtx-networklatency/document.md)

 | 

Describes the current device network latency information. This struct is passed by a game app after obtaining the network latency information.

 |

#### \[h2\]Type Definitions

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

typedef enum [OpenGTX\_ErrorCode](../../../modules/graphicsaccelerate/document.md#ga97deebd9adf3e19947ec5b4615fa1d9c) [OpenGTX\_ErrorCode](../../../modules/graphicsaccelerate/document.md#gaa2c657ed21a175b099bea0ed2491cc34)

 | 

Describes the error codes of OpenGTX API calls.

 |
| 

typedef enum [OpenGTX\_LTPO\_Mode](../../../modules/graphicsaccelerate/document.md#gad531d05ca502b93f4153e4b1f749ed0c) [OpenGTX\_LTPO\_Mode](../../../modules/graphicsaccelerate/document.md#gace5aaeeb51bae6d9cfa77ff009787fac)

 | 

Describes the OpenGTX\_LTPO modes for controlling the game frame rate.

 |
| 

typedef enum [OpenGTX\_EngineType](../../../modules/graphicsaccelerate/document.md#gadd5a5e0b3b4aa3ea8b0974cba13c0389) [OpenGTX\_EngineType](../../../modules/graphicsaccelerate/document.md#ga1f7722a3c293500468662b4ab531a6cf)

 | 

Describes the underlying game engine types used by game apps.

 |
| 

typedef enum [OpenGTX\_GameType](../../../modules/graphicsaccelerate/document.md#ga34d898acfaacb3750db454a9ed2038a5) [OpenGTX\_GameType](../../../modules/graphicsaccelerate/document.md#ga25a7691e1e839f1a242927d70633d816)

 | 

Describes the game types.

 |
| 

typedef enum [OpenGTX\_SceneID](../../../modules/graphicsaccelerate/document.md#gad7e5d2d235183dc0c6549331d6bc2932) [OpenGTX\_SceneID](../../../modules/graphicsaccelerate/document.md#gaef86d901a97a6e16dfff3f3d68bf123c)

 | 

Describes the OpenGTX game scene types.

 |
| 

typedef enum [OpenGTX\_PictureQualityMaxLevel](../../../modules/graphicsaccelerate/document.md#gacd5c090213b3593e7c9ab6c93118ff8e) [OpenGTX\_PictureQualityMaxLevel](../../../modules/graphicsaccelerate/document.md#gae9ef047f7f1e854186af0d62dacff68d)

 | 

Describes the game app image quality levels.

 |
| 

typedef enum [OpenGTX\_TempLevel](../../../modules/graphicsaccelerate/document.md#gaeff4735d18eb3086603ab6d04e7ad133) [OpenGTX\_TempLevel](../../../modules/graphicsaccelerate/document.md#ga4571f1a424d551ba387ab3ea4fd6d8b8)

 | 

Describes the device temperature levels.

 |
| 

typedef struct [OpenGTX\_Context](../../../modules/graphicsaccelerate/document.md#ga3ef8c7447a236d882b625ec8434385ed) [OpenGTX\_Context](../../../modules/graphicsaccelerate/document.md#ga3ef8c7447a236d882b625ec8434385ed)

 | 

Describes the OpenGTX context.

 |
| 

typedef struct [OpenGTX\_ConfigDescription](../../structs/opengtx-configdescription/document.md) [OpenGTX\_ConfigDescription](../../../modules/graphicsaccelerate/document.md#ga2536aca243f80e8fee0a4f3b6a9c2b63)

 | 

Describes the OpenGTX attribute settings.

 |
| 

typedef struct [OpenGTX\_GameSceneInfo](../../structs/opengtx-gamesceneinfo/document.md) [OpenGTX\_GameSceneInfo](../../../modules/graphicsaccelerate/document.md#gae72bdc657dfd31dae48df5e069eaddda)

 | 

Describes the game scene information. This struct is passed by a game app after obtaining the scene information.

 |
| 

typedef struct [OpenGTX\_FrameRenderInfo](../../structs/opengtx-framerenderinfo/document.md) [OpenGTX\_FrameRenderInfo](../../../modules/graphicsaccelerate/document.md#gab7cf8edc160e7a0c9050e39443df34b1)

 | 

Describes the frame rendering information. This struct is passed by a game app after obtaining the frame attributes.

 |
| 

typedef struct [OpenGTX\_NetworkInfo](../../structs/opengtx-networkinfo/document.md) [OpenGTX\_NetworkInfo](../../../modules/graphicsaccelerate/document.md#ga8f8b321e53382f5f07e850c79478204b)

 | 

Describes the current device network information. This struct is passed by a game app after obtaining the network information.

 |
| 

typedef struct [OpenGTX\_ResolutionValue](../../structs/opengtx-resolutionvalue/document.md) [OpenGTX\_ResolutionValue](../../../modules/graphicsaccelerate/document.md#ga36078da348203d9ce874cb4b4d953d40)

 | 

Describes the resolution of a game app.

 |
| 

typedef struct [OpenGTX\_Vector3](../../structs/opengtx-vector3/document.md) [OpenGTX\_Vector3](../../../modules/graphicsaccelerate/document.md#gaba0a76029883a1c315a61c28719b9839)

 | 

Describes an OpenGTX 3D vector.

 |
| 

typedef struct [OpenGTX\_NetworkLatency](../../structs/opengtx-networklatency/document.md) [OpenGTX\_NetworkLatency](../../../modules/graphicsaccelerate/document.md#ga75435c59fdcf1b9d651d2a00f154be7b)

 | 

Describes the current device network latency information. This struct is passed by a game app after obtaining the network latency information.

 |
| 

typedef void(\* [OpenGTX\_DeviceInfoCallback](../../../modules/graphicsaccelerate/document.md#ga1d66cec4aa0e01696d878c330f012d7a)) ([OpenGTX\_TempLevel](../../../modules/graphicsaccelerate/document.md#gaeff4735d18eb3086603ab6d04e7ad133))

 | 

Callback for device temperature information.

 |

#### \[h2\]Enumerations

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

[OpenGTX\_ErrorCode](../../../modules/graphicsaccelerate/document.md#ga97deebd9adf3e19947ec5b4615fa1d9c) {

OPENGTX\_SUCCESS = 0,

OPENGTX\_INVALID\_PARAMETER = 401,

OPENGTX\_CONTEXT\_NOT\_CONFIG = 1009502001,

OPENGTX\_CONTEXT\_NOT\_ACTIVE = 1009502002

}

 | 

Describes the error codes of OpenGTX API calls.

 |
| 

[OpenGTX\_LTPO\_Mode](../../../modules/graphicsaccelerate/document.md#gad531d05ca502b93f4153e4b1f749ed0c) {

SCENE\_MODE = 0x0001,

TOUCH\_MODE = 0x0010,

ADAPTIVE\_MODE = 0x0100

}

 | 

Describes the OpenGTX\_LTPO modes for controlling the game frame rate.

 |
| 

[OpenGTX\_EngineType](../../../modules/graphicsaccelerate/document.md#gadd5a5e0b3b4aa3ea8b0974cba13c0389) {

UNITY = 1,

UNREAL = 2,

MESSIAH = 3,

COCOS = 4,

OTHERS\_ENGINE = 100

}

 | 

Describes the underlying game engine types used by game apps.

 |
| 

[OpenGTX\_GameType](../../../modules/graphicsaccelerate/document.md#ga34d898acfaacb3750db454a9ed2038a5) {

MOBA = 1,

RPG = 2,

FPS = 3,

RAC = 4,

OTHERS\_TYPE = 100

}

 | 

Describes the game types.

 |
| 

[OpenGTX\_SceneID](../../../modules/graphicsaccelerate/document.md#gad7e5d2d235183dc0c6549331d6bc2932) {

LOGIN = 1,

GAME\_INTERFACE = 2,

LOADING = 3,

PLAYING = 4,

SPECTATOR = 5,

DEATH = 6,

HEAVY\_LOAD = 7,

OTHERS\_SCENE = 100

}

 | 

Describes the OpenGTX game scene types.

 |
| 

[OpenGTX\_PictureQualityMaxLevel](../../../modules/graphicsaccelerate/document.md#gacd5c090213b3593e7c9ab6c93118ff8e) {

SD = 1,

HD = 2,

FHD = 3,

QHD = 4,

UHD = 5

}

 | 

Describes the game app image quality levels.

 |
| 

[OpenGTX\_TempLevel](../../../modules/graphicsaccelerate/document.md#gaeff4735d18eb3086603ab6d04e7ad133) {

TEMP\_LEVEL1 = 1,

TEMP\_LEVEL2 = 2,

TEMP\_LEVEL3 = 3,

TEMP\_LEVEL4 = 4,

TEMP\_LEVEL5 = 5,

TEMP\_LEVEL6 = 6

}

 | 

Describes the device temperature levels.

 |

#### \[h2\]Functions

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

[OpenGTX\_Context](../../../modules/graphicsaccelerate/document.md#ga3ef8c7447a236d882b625ec8434385ed)\* [HMS\_OpenGTX\_CreateContext](../../../modules/graphicsaccelerate/document.md#ga94aadbb64ffb5382a4661790c040f1c3)([OpenGTX\_DeviceInfoCallback](../../../modules/graphicsaccelerate/document.md#ga1d66cec4aa0e01696d878c330f012d7a) deviceInfoCallback)

 | 

Creates an OpenGTX context instance. Each time this API is successfully called, an [OpenGTX\_Context](../../../modules/graphicsaccelerate/document.md#ga3ef8c7447a236d882b625ec8434385ed) object is created and a pointer to the [OpenGTX\_Context](../../../modules/graphicsaccelerate/document.md#ga3ef8c7447a236d882b625ec8434385ed) object is returned.

 |
| 

[OpenGTX\_ErrorCode](../../../modules/graphicsaccelerate/document.md#ga97deebd9adf3e19947ec5b4615fa1d9c) [HMS\_OpenGTX\_Activate](../../../modules/graphicsaccelerate/document.md#ga67e6cc5b491539c5e219f9e9ef15abca)([OpenGTX\_Context](../../../modules/graphicsaccelerate/document.md#ga3ef8c7447a236d882b625ec8434385ed)\* context)

 | 

Activates an OpenGTX context instance. Before using an OpenGTX context instance, you need to activate it.

 |
| 

[OpenGTX\_ErrorCode](../../../modules/graphicsaccelerate/document.md#ga97deebd9adf3e19947ec5b4615fa1d9c) [HMS\_OpenGTX\_Deactivate](../../../modules/graphicsaccelerate/document.md#gaa741745687d067180d27d3be30db7422)([OpenGTX\_Context](../../../modules/graphicsaccelerate/document.md#ga3ef8c7447a236d882b625ec8434385ed)\* context)

 | 

Deactivates an OpenGTX context instance. To activate the instance again, call the [HMS\_OpenGTX\_Activate](../../../modules/graphicsaccelerate/document.md#ga67e6cc5b491539c5e219f9e9ef15abca) API.

 |
| 

[OpenGTX\_ErrorCode](../../../modules/graphicsaccelerate/document.md#ga97deebd9adf3e19947ec5b4615fa1d9c) [HMS\_OpenGTX\_SetConfiguration](../../../modules/graphicsaccelerate/document.md#gaaa09a16f113a0a9e0014b495ff961b6e)([OpenGTX\_Context](../../../modules/graphicsaccelerate/document.md#ga3ef8c7447a236d882b625ec8434385ed)\* context, const [OpenGTX\_ConfigDescription](../../structs/opengtx-configdescription/document.md)\* config)

 | 

Initializes an OpenGTX context instance and sets the OpenGTX context instance attributes.

 |
| 

[OpenGTX\_ErrorCode](../../../modules/graphicsaccelerate/document.md#ga97deebd9adf3e19947ec5b4615fa1d9c) [HMS\_OpenGTX\_DispatchFrameRenderInfo](../../../modules/graphicsaccelerate/document.md#ga0c0b0034e4a6337e509888b2a9611489)([OpenGTX\_Context](../../../modules/graphicsaccelerate/document.md#ga3ef8c7447a236d882b625ec8434385ed)\* context, const [OpenGTX\_FrameRenderInfo](../../structs/opengtx-framerenderinfo/document.md)\* frameRenderInfo)

 | 

Sets the frame rendering information required for OpenGTX running. The information needs to be updated after each change to a frame.

 |
| 

[OpenGTX\_ErrorCode](../../../modules/graphicsaccelerate/document.md#ga97deebd9adf3e19947ec5b4615fa1d9c) [HMS\_OpenGTX\_DispatchGameSceneInfo](../../../modules/graphicsaccelerate/document.md#gafd01b1b2726f10b10968cdcd73da632f)([OpenGTX\_Context](../../../modules/graphicsaccelerate/document.md#ga3ef8c7447a236d882b625ec8434385ed)\* context, const [OpenGTX\_GameSceneInfo](../../structs/opengtx-gamesceneinfo/document.md)\* gameSceneInfo)

 | 

Sets the game scene information required for OpenGTX running.

 |
| 

[OpenGTX\_ErrorCode](../../../modules/graphicsaccelerate/document.md#ga97deebd9adf3e19947ec5b4615fa1d9c) [HMS\_OpenGTX\_DispatchNetworkInfo](../../../modules/graphicsaccelerate/document.md#gad7a6544a832f28ef068df580ac8a1b78)([OpenGTX\_Context](../../../modules/graphicsaccelerate/document.md#ga3ef8c7447a236d882b625ec8434385ed)\* context, const [OpenGTX\_NetworkInfo](../../structs/opengtx-networkinfo/document.md)\* networkInfo)

 | 

Sets the network latency information required for OpenGTX running.

 |
| 

[OpenGTX\_ErrorCode](../../../modules/graphicsaccelerate/document.md#ga97deebd9adf3e19947ec5b4615fa1d9c) [HMS\_OpenGTX\_DestroyContext](../../../modules/graphicsaccelerate/document.md#ga0b757b487acf42e92b06178e159b03ac)([OpenGTX\_Context](../../../modules/graphicsaccelerate/document.md#ga3ef8c7447a236d882b625ec8434385ed)\*\* context)

 | 

Destroys an OpenGTX context instance and releases memory resources.

 |
