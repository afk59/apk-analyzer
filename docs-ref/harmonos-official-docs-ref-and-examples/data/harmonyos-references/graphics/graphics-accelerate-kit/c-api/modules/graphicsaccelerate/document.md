# GraphicsAccelerate

#### Overview

The module provides APIs related to the graphics rendering acceleration capabilities of Graphics Accelerate Kit.

**System capability**: SystemCapability.GraphicsGame.RenderAccelerate

**Start version**: 5.0.0(12)

#### Summary

#### \[h2\]Files

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

[abr\_base.h](../../header-files-and-structs/header-files/abr-base-h/document.md)

 | 

Declares ABR APIs used for different graphics APIs.

 |
| 

[abr\_gles.h](../../header-files-and-structs/header-files/abr-gles-h/document.md)

 | 

Declares ABR APIs used for the OpenGL ES graphics API.

 |
| 

[frame\_generation\_base.h](../../header-files-and-structs/header-files/frame-generation-base-h/document.md)

 | 

Declares frame generation APIs used for different graphics APIs.

 |
| 

[frame\_generation\_gles.h](../../header-files-and-structs/header-files/frame-generation-gles-h/document.md)

 | 

Declares frame generation APIs used for the OpenGL ES graphics API.

 |
| 

[frame\_generation\_vk.h](../../header-files-and-structs/header-files/frame-generation-vk-h/document.md)

 | 

Declares frame generation APIs used for the Vulkan graphics API.

 |
| 

[opengtx\_base.h](../../header-files-and-structs/header-files/opengtx-base-h/document.md)

 | 

Declares OpenGTX APIs used for both the OpenGL ES and Vulkan graphics APIs.

 |

#### \[h2\]Structs

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

struct [ABR\_Vector3](../../header-files-and-structs/structs/abr-vector3/document.md)

 | 

Describes an ABR 3D vector.

 |
| 

struct [ABR\_CameraData](../../header-files-and-structs/structs/abr-cameradata/document.md)

 | 

Describes the camera motion data of a game app's each frame. The ABR capability adaptively adjusts the buffer resolution factor according to the camera motion data.

 |
| 

struct [FG\_Mat4x4](../../header-files-and-structs/structs/fg-mat4x4/document.md)

 | 

Describes a 4x4 matrix in column-major order.

 |
| 

struct [FG\_AlgorithmModeInfo](../../header-files-and-structs/structs/fg-algorithmmodeinfo/document.md)

 | 

Describes the frame generation algorithm mode information.

 |
| 

struct [FG\_Dimension2D](../../header-files-and-structs/structs/fg-dimension2d/document.md)

 | 

Describes the 2D image resolution, in pixels.

 |
| 

struct [FG\_ResolutionInfo](../../header-files-and-structs/structs/fg-resolutioninfo/document.md)

 | 

Describes the resolutions of input and output images for frame generation.

 |
| 

struct [FG\_Vec3D](../../header-files-and-structs/structs/fg-vec3d/document.md)

 | 

Describes a frame generation 3D vector.

 |
| 

struct [FG\_PerFrameExtendedCameraInfo](../../header-files-and-structs/structs/fg-perframeextendedcamerainfo/document.md)

 | 

Describes extended camera information. When the translation component of the view projection matrix is very large, more detailed camera information can be provided for more accurate frame prediction.

 |
| 

struct [FG\_IntegrationInfo](../../header-files-and-structs/structs/fg-integrationinfo/document.md)

 | 

Describes the integration information about frame generation, including the display mode, whether to separately buffer depth and color textures, and whether to flip the color texture. It takes effect only when [FG\_PredictionMode](#gaea2169cd5ae4bf9e8a17dc58f33e8766) is set to **FG\_PREDICTION\_MODE\_INTERPOLATION**.

 |
| 

struct [FG\_DispatchDescription\_GLES](../../header-files-and-structs/structs/fg-dispatchdescription-gles/document.md)

 | 

Describes the parameter information required by [HMS\_FG\_Dispatch\_GLES](#gab135a0f59582d168d461ef115423cfb4). The parameter information needs to be updated for each frame. This API applies only to the OpenGL ES graphics API.

 |
| 

struct [FG\_ContextDescription\_VK](../../header-files-and-structs/structs/fg-contextdescription-vk/document.md)

 | 

Describes the attribute information required for creating a frame generation context instance [FG\_Context\_VK](#ga4022ab63c2296d63dcf2c2df178508b7).

 |
| 

struct [FG\_ImageFormat\_VK](../../header-files-and-structs/structs/fg-imageformat-vk/document.md)

 | 

Describes the input and output image format information for frame generation. This API applies only to the Vulkan graphics API.

 |
| 

struct [FG\_ImageSync\_VK](../../header-files-and-structs/structs/fg-imagesync-vk/document.md)

 | 

Describes the synchronization status information about the input and output images for frame generation. It is used to create a memory barrier for the images. This API applies only to the Vulkan graphics API.

 |
| 

struct [FG\_ImageInfo\_VK](../../header-files-and-structs/structs/fg-imageinfo-vk/document.md)

 | 

Describes the input and output image information for frame generation. This API applies only to the Vulkan graphics API.

 |
| 

struct [FG\_DispatchDescription\_VK](../../header-files-and-structs/structs/fg-dispatchdescription-vk/document.md)

 | 

Describes the parameter information required by [HMS\_FG\_Dispatch\_VK](#ga21f86a194e72e99dd54fd39080385a37). The parameter information needs to be updated for each frame. This API applies only to the Vulkan graphics API.

 |
| 

struct [OpenGTX\_ConfigDescription](../../header-files-and-structs/structs/opengtx-configdescription/document.md)

 | 

Describes the OpenGTX attribute settings.

 |
| 

struct [OpenGTX\_GameSceneInfo](../../header-files-and-structs/structs/opengtx-gamesceneinfo/document.md)

 | 

Describes the game scene information. This struct is passed by a game app after obtaining the scene information.

 |
| 

struct [OpenGTX\_FrameRenderInfo](../../header-files-and-structs/structs/opengtx-framerenderinfo/document.md)

 | 

Describes the frame rendering information. This struct is passed by a game app after obtaining the frame attributes.

 |
| 

struct [OpenGTX\_NetworkInfo](../../header-files-and-structs/structs/opengtx-networkinfo/document.md)

 | 

Describes the current device network information. This struct is passed by a game app after obtaining the network information.

 |
| 

struct [OpenGTX\_ResolutionValue](../../header-files-and-structs/structs/opengtx-resolutionvalue/document.md)

 | 

Describes the resolution of a game app.

 |
| 

struct [OpenGTX\_Vector3](../../header-files-and-structs/structs/opengtx-vector3/document.md)

 | 

Describes an OpenGTX 3D vector.

 |
| 

struct [OpenGTX\_NetworkLatency](../../header-files-and-structs/structs/opengtx-networklatency/document.md)

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

typedef struct [ABR\_Context](#ga52e8dba39ee979b70826401b3d36574e) [ABR\_Context](#ga52e8dba39ee979b70826401b3d36574e)

 | 

Describes the ABR context.

 |
| 

typedef enum [ABR\_RenderAPI\_Type](#ga9359d16ecefa21f0e6e5f29732cbf6f4) [ABR\_RenderAPI\_Type](#ga3a6ead3a3c0f19a6434e97fda13f42f2)

 | 

Describes the graphics API types supported by the ABR capability.

 |
| 

typedef struct [ABR\_Vector3](../../header-files-and-structs/structs/abr-vector3/document.md) [ABR\_Vector3](#ga71a845f23f7ec4c0935db8e9f00ab8b9)

 | 

Describes an ABR 3D vector.

 |
| 

typedef struct [ABR\_CameraData](../../header-files-and-structs/structs/abr-cameradata/document.md) [ABR\_CameraData](#gada21a47272d5db8e28e2a9bb4fd033d4)

 | 

Describes the camera motion data of a game app's each frame. The ABR capability adaptively adjusts the buffer resolution factor according to the camera motion data.

 |
| 

typedef enum [ABR\_ErrorCode](#ga72df702d70a8326b5b46c118be6ad1d7) [ABR\_ErrorCode](#ga86d5860f91dc4f1de6b381cd65389b9d)

 | 

Describes the error codes of ABR API calls.

 |
| 

typedef struct [FG\_Mat4x4](../../header-files-and-structs/structs/fg-mat4x4/document.md) [FG\_Mat4x4](#gabbf87d3423630e0b50f19da2cbda3e90)

 | 

Describes a 4x4 matrix in column-major order.

 |
| 

typedef enum [FG\_PredictionMode](#gaea2169cd5ae4bf9e8a17dc58f33e8766) [FG\_PredictionMode](#ga79e55783a2a38873fc6890c297885275)

 | 

Describes the frame prediction algorithm modes for frame generation.

 |
| 

typedef enum [FG\_MeMode](#ga8bd44b6bea12774dd2ee6014d696e7d1) [FG\_MeMode](#ga81cbe226af620e6ef19cd8ec5e9b5256)

 | 

Describes the motion estimation algorithm modes. The basic mode and enhanced mode are supported.

 |
| 

typedef enum [FG\_PresentMode](#section131101213459) [FG\_PresentMode](#section11881356193212)

 | 

Defines the predicted frame display modes, including the game display mode (the game sends predicted frames for display) and system display mode (the system sends predicted frames for display).

 |
| 

typedef struct [FG\_AlgorithmModeInfo](../../header-files-and-structs/structs/fg-algorithmmodeinfo/document.md) [FG\_AlgorithmModeInfo](#ga1750087784d7cbf19957243db12a7ba3)

 | 

Describes the frame generation algorithm mode information.

 |
| 

typedef struct [FG\_Vec3D](../../header-files-and-structs/structs/fg-vec3d/document.md) [FG\_Vec3D](../../header-files-and-structs/structs/fg-vec3d/document.md)

 | 

Describes a frame generation 3D vector.

 |
| 

typedef struct [FG\_PerFrameExtendedCameraInfo](../../header-files-and-structs/structs/fg-perframeextendedcamerainfo/document.md) [FG\_PerFrameExtendedCameraInfo](../../header-files-and-structs/structs/fg-perframeextendedcamerainfo/document.md)

 | 

Describes extended camera information. When the translation component of the view projection matrix is very large, more detailed camera information can be provided for more accurate frame prediction.

 |
| 

typedef struct [FG\_IntegrationInfo](../../header-files-and-structs/structs/fg-integrationinfo/document.md) [FG\_IntegrationInfo](../../header-files-and-structs/structs/fg-integrationinfo/document.md)

 | 

Describes the integration information about frame generation, including the display mode, whether to separately buffer depth and color textures, and whether to flip the color texture. It takes effect only when [FG\_PredictionMode](#gaea2169cd5ae4bf9e8a17dc58f33e8766) is set to **FG\_PREDICTION\_MODE\_INTERPOLATION**.

 |
| 

typedef enum [FG\_ErrorCode](#ga68efbf5ff41faeb835f5587654c1e669) [FG\_ErrorCode](#ga394c554fc5d056d702180ee031ccee2c)

 | 

Describes the error codes of frame generation API calls.

 |
| 

typedef enum [FG\_CvvZSemantic](#ga530448309918d6d703e28c61a848a267) [FG\_CvvZSemantic](#gabac7987ddc62b712f36d95b185e47bb2)

 | 

Describes the homogeneous clip space Z/W ranges and depth functions after camera projection transformation.

 |
| 

typedef struct [FG\_Dimension2D](../../header-files-and-structs/structs/fg-dimension2d/document.md) [FG\_Dimension2D](#ga545268ccc070666954981580f5764d20)

 | 

Describes the 2D image resolution, in pixels.

 |
| 

typedef struct [FG\_ResolutionInfo](../../header-files-and-structs/structs/fg-resolutioninfo/document.md) [FG\_ResolutionInfo](#gacbc0d894e11f18711fd4558d45c7cd39)

 | 

Describes the resolutions of input and output images for frame generation.

 |
| 

typedef struct [FG\_Context\_GLES](#ga62e666292d67fd19fd35ad07463e21cc) [FG\_Context\_GLES](#ga62e666292d67fd19fd35ad07463e21cc)

 | 

Describes the frame generation context. This API applies only to the OpenGL ES graphics API.

 |
| 

typedef struct [FG\_DispatchDescription\_GLES](../../header-files-and-structs/structs/fg-dispatchdescription-gles/document.md) [FG\_DispatchDescription\_GLES](#ga3f4c6e065ff13670d8c64cb9cc3796a7)

 | 

Describes the parameter information required by [HMS\_FG\_Dispatch\_GLES](#gab135a0f59582d168d461ef115423cfb4). The parameter information needs to be updated for each frame. This API applies only to the OpenGL ES graphics API.

 |
| 

typedef enum [FG\_ImageFormat\_GLES](#ga3bec27405891e089234bf50d0589c3cd) [FG\_ImageFormat\_GLES](#ga5fbce7432ad1a2e3d9a37554bce2352a)

 | 

Describes the image formats of the real frame color buffer and the predicted frame buffer. This API applies only to the OpenGL ES graphics API.

 |
| 

typedef struct [FG\_Context\_VK](#ga4022ab63c2296d63dcf2c2df178508b7) [FG\_Context\_VK](#ga4022ab63c2296d63dcf2c2df178508b7)

 | 

Describes the frame generation context. This API applies only to the Vulkan graphics API.

 |
| 

typedef struct [FG\_Image\_VK](#gabd6ee9704e997ffc2792ad3c89847019) [FG\_Image\_VK](#gabd6ee9704e997ffc2792ad3c89847019)

 | 

Describes the input and output images for frame generation. This API applies only to the Vulkan graphics API.

 |
| 

typedef struct [FG\_ContextDescription\_VK](../../header-files-and-structs/structs/fg-contextdescription-vk/document.md) [FG\_ContextDescription\_VK](#ga6d3f20ae7b60a4a38baf696031d609c0)

 | 

Describes the attribute information required for creating a frame generation context instance [FG\_Context\_VK](#ga4022ab63c2296d63dcf2c2df178508b7).

 |
| 

typedef struct [FG\_ImageFormat\_VK](../../header-files-and-structs/structs/fg-imageformat-vk/document.md) [FG\_ImageFormat\_VK](#ga2ef395664c0fd54102510c62a84ebc3a)

 | 

Describes the input and output image format information for frame generation. This API applies only to the Vulkan graphics API.

 |
| 

typedef struct [FG\_ImageSync\_VK](../../header-files-and-structs/structs/fg-imagesync-vk/document.md) [FG\_ImageSync\_VK](#ga847779a17b04d183b31397007b11735f)

 | 

Describes the synchronization status information about the input and output images for frame generation. It is used to create a memory barrier for the images. This API applies only to the Vulkan graphics API.

 |
| 

typedef struct [FG\_ImageInfo\_VK](../../header-files-and-structs/structs/fg-imageinfo-vk/document.md) [FG\_ImageInfo\_VK](#gabf275c34e4b1335ddcda4b576009d6c7)

 | 

Describes the input and output image information for frame generation. This API applies only to the Vulkan graphics API.

 |
| 

typedef struct [FG\_DispatchDescription\_VK](../../header-files-and-structs/structs/fg-dispatchdescription-vk/document.md) [FG\_DispatchDescription\_VK](#gabdf63f9fb31687516fee81d83b609302)

 | 

Describes the parameter information required by [HMS\_FG\_Dispatch\_VK](#ga21f86a194e72e99dd54fd39080385a37). The parameter information needs to be updated for each frame. This API applies only to the Vulkan graphics API.

 |
| 

typedef enum [OpenGTX\_ErrorCode](#ga97deebd9adf3e19947ec5b4615fa1d9c) [OpenGTX\_ErrorCode](#gaa2c657ed21a175b099bea0ed2491cc34)

 | 

Describes the error codes of OpenGTX API calls.

 |
| 

typedef enum [OpenGTX\_LTPO\_Mode](#gad531d05ca502b93f4153e4b1f749ed0c) [OpenGTX\_LTPO\_Mode](#gace5aaeeb51bae6d9cfa77ff009787fac)

 | 

Describes the OpenGTX\_LTPO modes for controlling the game frame rate.

 |
| 

typedef enum [OpenGTX\_EngineType](#gadd5a5e0b3b4aa3ea8b0974cba13c0389) [OpenGTX\_EngineType](#ga1f7722a3c293500468662b4ab531a6cf)

 | 

Describes the underlying game engine types used by game apps.

 |
| 

typedef enum [OpenGTX\_GameType](#ga34d898acfaacb3750db454a9ed2038a5) [OpenGTX\_GameType](#ga25a7691e1e839f1a242927d70633d816)

 | 

Describes the game types.

 |
| 

typedef enum [OpenGTX\_SceneID](#gad7e5d2d235183dc0c6549331d6bc2932) [OpenGTX\_SceneID](#gaef86d901a97a6e16dfff3f3d68bf123c)

 | 

Describes the OpenGTX game scene types.

 |
| 

typedef enum [OpenGTX\_PictureQualityMaxLevel](#gacd5c090213b3593e7c9ab6c93118ff8e) [OpenGTX\_PictureQualityMaxLevel](#gae9ef047f7f1e854186af0d62dacff68d)

 | 

Describes the game app image quality levels.

 |
| 

typedef enum [OpenGTX\_TempLevel](#gaeff4735d18eb3086603ab6d04e7ad133) [OpenGTX\_TempLevel](#ga4571f1a424d551ba387ab3ea4fd6d8b8)

 | 

Describes the device temperature levels.

 |
| 

typedef struct [OpenGTX\_Context](#ga3ef8c7447a236d882b625ec8434385ed) [OpenGTX\_Context](#ga3ef8c7447a236d882b625ec8434385ed)

 | 

Describes the OpenGTX context.

 |
| 

typedef struct [OpenGTX\_ConfigDescription](../../header-files-and-structs/structs/opengtx-configdescription/document.md) [OpenGTX\_ConfigDescription](#ga2536aca243f80e8fee0a4f3b6a9c2b63)

 | 

Describes the OpenGTX attribute settings.

 |
| 

typedef struct [OpenGTX\_GameSceneInfo](../../header-files-and-structs/structs/opengtx-gamesceneinfo/document.md) [OpenGTX\_GameSceneInfo](#gae72bdc657dfd31dae48df5e069eaddda)

 | 

Describes the game scene information. This struct is passed by a game app after obtaining the scene information.

 |
| 

typedef struct [OpenGTX\_FrameRenderInfo](../../header-files-and-structs/structs/opengtx-framerenderinfo/document.md) [OpenGTX\_FrameRenderInfo](#gab7cf8edc160e7a0c9050e39443df34b1)

 | 

Describes the frame rendering information. This struct is passed by a game app after obtaining the frame attributes.

 |
| 

typedef struct [OpenGTX\_NetworkInfo](../../header-files-and-structs/structs/opengtx-networkinfo/document.md) [OpenGTX\_NetworkInfo](#ga8f8b321e53382f5f07e850c79478204b)

 | 

Describes the current device network information. This struct is passed by a game app after obtaining the network information.

 |
| 

typedef struct [OpenGTX\_ResolutionValue](../../header-files-and-structs/structs/opengtx-resolutionvalue/document.md) [OpenGTX\_ResolutionValue](#ga36078da348203d9ce874cb4b4d953d40)

 | 

Describes the resolution of a game app.

 |
| 

typedef struct [OpenGTX\_Vector3](../../header-files-and-structs/structs/opengtx-vector3/document.md) [OpenGTX\_Vector3](#gaba0a76029883a1c315a61c28719b9839)

 | 

Describes an OpenGTX 3D vector.

 |
| 

typedef struct [OpenGTX\_NetworkLatency](../../header-files-and-structs/structs/opengtx-networklatency/document.md) [OpenGTX\_NetworkLatency](#ga75435c59fdcf1b9d651d2a00f154be7b)

 | 

Describes the current device network latency information. This struct is passed by a game app after obtaining the network latency information.

 |
| 

typedef void(\* [OpenGTX\_DeviceInfoCallback](#ga1d66cec4aa0e01696d878c330f012d7a)) ([OpenGTX\_TempLevel](#gaeff4735d18eb3086603ab6d04e7ad133))

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

[ABR\_RenderAPI\_Type](#ga9359d16ecefa21f0e6e5f29732cbf6f4) {

RENDER\_API\_GLES = 0

}

 | 

Describes the graphics API types supported by the ABR capability.

 |
| 

[ABR\_ErrorCode](#ga72df702d70a8326b5b46c118be6ad1d7) {

ABR\_SUCCESS = 0,

ABR\_INVALID\_PARAMETER = 401,

ABR\_CONTEXT\_CONFIG\_AFTER\_ACTIVE = 1009501001,

ABR\_CONTEXT\_NOT\_CONFIG = 1009501002,

ABR\_CONTEXT\_NOT\_ACTIVE = 1009501003,

ABR\_METADATA\_INVALID = 1009501004,

ABR\_FRAMEBUFFER\_INVALID = 1009501005

}

 | 

Describes the error codes of ABR API calls.

 |
| 

[FG\_PredictionMode](#gaea2169cd5ae4bf9e8a17dc58f33e8766) {

FG\_PREDICTION\_MODE\_INTERPOLATION = 0,

FG\_PREDICTION\_MODE\_EXTRAPOLATION = 1

}

 | 

Describes the frame prediction algorithm modes for frame generation.

 |
| 

[FG\_MeMode](#ga8bd44b6bea12774dd2ee6014d696e7d1) {

FG\_ME\_MODE\_BASIC = 0,

FG\_ME\_MODE\_ENHANCED = 1

}

 | 

Describes the motion estimation algorithm modes. The basic mode and enhanced mode are supported.

 |
| 

[FG\_ErrorCode](#ga68efbf5ff41faeb835f5587654c1e669) {

FG\_SUCCESS = 0,

FG\_INVALID\_PARAMETER = 401,

FG\_CONTEXT\_NOT\_CONFIG = 1009500001,

FG\_CONTEXT\_NOT\_ACTIVE = 1009500002,

FG\_COLLECTING\_PREVIOUS\_FRAMES = 1009500003

}

 | 

Describes the error codes of frame generation API calls.

 |
| 

[FG\_CvvZSemantic](#ga530448309918d6d703e28c61a848a267) {

FG\_CVV\_Z\_SEMANTIC\_MINUS\_ONE\_TO\_ONE\_FORWARD\_Z = 0,

FG\_CVV\_Z\_SEMANTIC\_ZERO\_TO\_ONE\_REVERSE\_Z = 1,

FG\_CVV\_Z\_SEMANTIC\_MINUS\_ONE\_TO\_ONE\_REVERSE\_Z = 2,

FG\_CVV\_Z\_SEMANTIC\_ZERO\_TO\_ONE\_FORWARD\_Z = 3

}

 | 

Describes the homogeneous clip space Z/W ranges and depth functions after camera projection transformation.

 |
| 

[FG\_ImageFormat\_GLES](#ga3bec27405891e089234bf50d0589c3cd) {

FG\_FORMAT\_R8G8B8A8\_UNORM = 0,

FG\_FORMAT\_R11G11B10\_SFLOAT = 1,

FG\_FORMAT\_R16G16B16A16\_SFLOAT = 2

}

 | 

Describes the image formats of the real frame color buffer and the predicted frame buffer. This API applies only to the OpenGL ES graphics API.

 |
| 

[FG\_PresentMode](#section131101213459) {

FG\_PRESENT\_BY\_GAME = 0,

FG\_PRESENT\_BY\_SYSTEM = 1

}

 | 

Defines the predicted frame display modes. There are two modes: game display mode (the game sends predicted frames for display) and system display mode (the system sends predicted frames for display).

 |
| 

[OpenGTX\_ErrorCode](#ga97deebd9adf3e19947ec5b4615fa1d9c) {

OPENGTX\_SUCCESS = 0,

OPENGTX\_INVALID\_PARAMETER = 401,

OPENGTX\_CONTEXT\_NOT\_CONFIG = 1009502001,

OPENGTX\_CONTEXT\_NOT\_ACTIVE = 1009502002

}

 | 

Describes the error codes of OpenGTX API calls.

 |
| 

[OpenGTX\_LTPO\_Mode](#gad531d05ca502b93f4153e4b1f749ed0c) {

SCENE\_MODE = 0x0001,

TOUCH\_MODE = 0x0010,

ADAPTIVE\_MODE = 0x0100

}

 | 

Describes the OpenGTX\_LTPO modes for controlling the game frame rate.

 |
| 

[OpenGTX\_EngineType](#gadd5a5e0b3b4aa3ea8b0974cba13c0389) {

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

[OpenGTX\_GameType](#ga34d898acfaacb3750db454a9ed2038a5) {

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

[OpenGTX\_SceneID](#gad7e5d2d235183dc0c6549331d6bc2932) {

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

[OpenGTX\_PictureQualityMaxLevel](#gacd5c090213b3593e7c9ab6c93118ff8e) {

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

[OpenGTX\_TempLevel](#gaeff4735d18eb3086603ab6d04e7ad133) {

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

[ABR\_Context](#ga52e8dba39ee979b70826401b3d36574e)\* [HMS\_ABR\_CreateContext](#ga8f785903a5382ff31baef78a3968f66a)([ABR\_RenderAPI\_Type](#ga9359d16ecefa21f0e6e5f29732cbf6f4) type)

 | 

Creates an ABR context instance. Each time this API is successfully called, an [ABR\_Context](#ga52e8dba39ee979b70826401b3d36574e) object is created and a pointer to the [ABR\_Context](#ga52e8dba39ee979b70826401b3d36574e) object is returned.

 |
| 

[ABR\_ErrorCode](#ga72df702d70a8326b5b46c118be6ad1d7) [HMS\_ABR\_SetTargetFps](#ga6c613e02088d559b9dc1450fde15bc2a)([ABR\_Context](#ga52e8dba39ee979b70826401b3d36574e)\* context, const uint32\_t targetFps)

 | 

Sets the target frame rate of an ABR context instance.

 |
| 

[ABR\_ErrorCode](#ga72df702d70a8326b5b46c118be6ad1d7) [HMS\_ABR\_SetScaleRange](#ga1001c6a7739d8ce57bf851986f121bf5)([ABR\_Context](#ga52e8dba39ee979b70826401b3d36574e)\* context, const float minValue, const float maxValue)

 | 

Sets the buffer resolution factor range of an ABR context instance.

 |
| 

[ABR\_ErrorCode](#ga72df702d70a8326b5b46c118be6ad1d7) [HMS\_ABR\_Activate](#ga463d8d5396bfd5f6ed800ddab616479a)([ABR\_Context](#ga52e8dba39ee979b70826401b3d36574e)\* context)

 | 

Activates an ABR context instance. Before the activation, the [HMS\_ABR\_SetTargetFps](#ga6c613e02088d559b9dc1450fde15bc2a) and [HMS\_ABR\_SetScaleRange](#ga1001c6a7739d8ce57bf851986f121bf5) APIs must be called to set instance attributes.

 |
| 

[ABR\_ErrorCode](#ga72df702d70a8326b5b46c118be6ad1d7) [HMS\_ABR\_IsActive](#ga791519fde19801e6da60094cf077b00f)([ABR\_Context](#ga52e8dba39ee979b70826401b3d36574e)\* context, bool\* isActive)

 | 

Checks whether an ABR context instance is activated.

 |
| 

[ABR\_ErrorCode](#ga72df702d70a8326b5b46c118be6ad1d7) [HMS\_ABR\_Deactivate](#ga4abb4b37392e77c15fbedfa8ceba3da4)([ABR\_Context](#ga52e8dba39ee979b70826401b3d36574e)\* context)

 | 

Deactivates an ABR context instance. To activate the instance again, call the [HMS\_ABR\_Activate](#ga463d8d5396bfd5f6ed800ddab616479a) API.

 |
| 

[ABR\_ErrorCode](#ga72df702d70a8326b5b46c118be6ad1d7) [HMS\_ABR\_UpdateCameraData](#ga5b895e36d31e46f71d04aba78c8f3716)([ABR\_Context](#ga52e8dba39ee979b70826401b3d36574e)\* context, [ABR\_CameraData](../../header-files-and-structs/structs/abr-cameradata/document.md)\* data)

 | 

Updates the camera motion data of each frame. Before the update, the [HMS\_ABR\_Activate](#ga463d8d5396bfd5f6ed800ddab616479a) API must be called to activate the ABR context instance.

 |
| 

[ABR\_ErrorCode](#ga72df702d70a8326b5b46c118be6ad1d7) [HMS\_ABR\_GetScale](#ga936129328fea3a5f77b2aae4935f67c6)([ABR\_Context](#ga52e8dba39ee979b70826401b3d36574e)\* context, float\* scale)

 | 

Obtains the buffer resolution factor for adaptive resolution adjustment.

 |
| 

[ABR\_ErrorCode](#ga72df702d70a8326b5b46c118be6ad1d7) [HMS\_ABR\_GetNextScale](#section157311245143415)([ABR\_Context](#ga52e8dba39ee979b70826401b3d36574e)\* context, float\* scale)

 | 

Obtains the ABR buffer resolution factor of the next frame.

 |
| 

[ABR\_ErrorCode](#ga72df702d70a8326b5b46c118be6ad1d7) [HMS\_ABR\_DestroyContext](#gaf3c03179b9bcf1b8475230cbbb0d877c)([ABR\_Context](#ga52e8dba39ee979b70826401b3d36574e)\*\* context)

 | 

Destroys an ABR context instance and releases memory resources.

 |
| 

[ABR\_ErrorCode](#ga72df702d70a8326b5b46c118be6ad1d7) [HMS\_ABR\_MarkFrameBuffer\_GLES](#ga821fb33620312d3adba51d30254c1ef0)([ABR\_Context](#ga52e8dba39ee979b70826401b3d36574e)\* context)

 | 

Marks a GLES buffer for adaptive rendering. This API must be called before the rendering is started.

 |
| 

[ABR\_ErrorCode](#ga72df702d70a8326b5b46c118be6ad1d7) [HMS\_ABR\_GetScaledTexture\_GLES](#section791920394423)([ABR\_Context](#ga52e8dba39ee979b70826401b3d36574e)\* context, uint32\_t originTexture, uint32\_t\* scaledTexture)

 | 

Obtains the GLES texture index after adaptive buffer resolution adjustment based on the GLES texture index corresponding to the original resolution.

 |
| 

[FG\_Context\_GLES](#ga62e666292d67fd19fd35ad07463e21cc)\* [HMS\_FG\_CreateContext\_GLES](#ga58e6b601cc4a7e8f0208d4f10f16c7e5)(void)

 | 

Creates a frame generation context instance. If the call is successful, a pointer to the [FG\_Context\_GLES](#ga62e666292d67fd19fd35ad07463e21cc) object will be returned. This API applies only to the OpenGL ES graphics API.

 |
| 

[FG\_ErrorCode](#ga68efbf5ff41faeb835f5587654c1e669) [HMS\_FG\_SetAlgorithmMode\_GLES](#ga79cc36ec768553a6560d1c553ef83c3b)([FG\_Context\_GLES](#ga62e666292d67fd19fd35ad07463e21cc)\* context, const [FG\_AlgorithmModeInfo](../../header-files-and-structs/structs/fg-algorithmmodeinfo/document.md)\* predictionModeInfo)

 | 

Sets the frame prediction algorithm mode and motion estimation mode for frame generation. This API is mandatory. This API applies only to the OpenGL ES graphics API.

 |
| 

[FG\_ErrorCode](#ga68efbf5ff41faeb835f5587654c1e669) [HMS\_FG\_SetResolution\_GLES](#gae46fcee6c715a6fda24df727465d42b1)([FG\_Context\_GLES](#ga62e666292d67fd19fd35ad07463e21cc)\* context, const [FG\_ResolutionInfo](../../header-files-and-structs/structs/fg-resolutioninfo/document.md)\* resolutionInfo)

 | 

Sets the resolutions of input and output images for frame generation. This API is mandatory. This API applies only to the OpenGL ES graphics API.

 |
| 

[FG\_ErrorCode](#ga68efbf5ff41faeb835f5587654c1e669) [HMS\_FG\_SetCvvZSemantic\_GLES](#ga6247264302a139024a92cf89da565b52)([FG\_Context\_GLES](#ga62e666292d67fd19fd35ad07463e21cc)\* context, [FG\_CvvZSemantic](#ga530448309918d6d703e28c61a848a267) semantic)

 | 

Sets the homogeneous clip space Z/W range and depth function. This API is optional. If it is not called, the default value **FG\_CVV\_Z\_SEMANTIC\_MINUS\_ONE\_TO\_ONE\_FORWARD\_Z** will be used. This API applies only to the OpenGL ES graphics API.

 |
| 

[FG\_ErrorCode](#ga68efbf5ff41faeb835f5587654c1e669) [HMS\_FG\_SetImageFormat\_GLES](#gaafa490d4377cc5babbc0ac0f4f7b78a7)([FG\_Context\_GLES](#ga62e666292d67fd19fd35ad07463e21cc)\* context, [FG\_ImageFormat\_GLES](#ga3bec27405891e089234bf50d0589c3cd) format)

 | 

Sets the image format of the real frame color buffer and the predicted frame buffer. This API is optional. If it is not called, the default value **FG\_FORMAT\_R8G8B8A8\_UNORM** will be used. This API applies only to the OpenGL ES graphics API.

 |
| 

[FG\_ErrorCode](#ga68efbf5ff41faeb835f5587654c1e669) [HMS\_FG\_SetDepthStencilYDirectionInverted\_GLES](#gaa6e340d0b1f1bc4dcd6abf378aa933df)([FG\_Context\_GLES](#ga62e666292d67fd19fd35ad07463e21cc)\* context, bool inverted)

 | 

Sets the flag bit for flipping the color buffer around the Y axis relative to the depth stencil buffer. This API is optional. If it is not called, no flipping is performed by default. This API applies only to the OpenGL ES graphics API.

 |
| 

[FG\_ErrorCode](#ga68efbf5ff41faeb835f5587654c1e669) [HMS\_FG\_Activate\_GLES](#gaa5f1d5b98694100aa3e3dbb4c99ac23a)([FG\_Context\_GLES](#ga62e666292d67fd19fd35ad07463e21cc)\* context)

 | 

Activates a frame generation context instance. Before the activation, the instance attributes must be set. For an activated frame generation context instance, the [HMS\_FG\_Dispatch\_GLES](#gab135a0f59582d168d461ef115423cfb4) API can be called to generate a predicted frame. This API applies only to the OpenGL ES graphics API.

 |
| 

[FG\_ErrorCode](#ga68efbf5ff41faeb835f5587654c1e669) [HMS\_FG\_Deactivate\_GLES](#gad08ff75c271a0c7c99ae3ebc596928b9)([FG\_Context\_GLES](#ga62e666292d67fd19fd35ad07463e21cc)\* context)

 | 

Deactivates a frame generation context instance. To activate the instance again, call the [HMS\_FG\_Activate\_GLES](#gaa5f1d5b98694100aa3e3dbb4c99ac23a) API.

 |
| 

[FG\_ErrorCode](#ga68efbf5ff41faeb835f5587654c1e669) [HMS\_FG\_IsActive\_GLES](#gaaa592e60d1cda40068b51c36d436b8eb)([FG\_Context\_GLES](#ga62e666292d67fd19fd35ad07463e21cc)\* context, bool\* isActive)

 | 

Checks whether a frame generation context instance is activated. This API applies only to the OpenGL ES graphics API.

 |
| 

[FG\_ErrorCode](#ga68efbf5ff41faeb835f5587654c1e669) [HMS\_FG\_Dispatch\_GLES](#gab135a0f59582d168d461ef115423cfb4)([FG\_Context\_GLES](#ga62e666292d67fd19fd35ad07463e21cc)\* context, const [FG\_DispatchDescription\_GLES](../../header-files-and-structs/structs/fg-dispatchdescription-gles/document.md)\* desc)

 | 

Sets the parameter information required for frame prediction to generate a predicted frame. This API applies only to the OpenGL ES graphics API.

 |
| 

[FG\_ErrorCode](#ga68efbf5ff41faeb835f5587654c1e669) [HMS\_FG\_SetExtendedCameraInfo\_GLES](#section1450921818712)([FG\_Context\_GLES](#ga62e666292d67fd19fd35ad07463e21cc)\* context, const [FG\_PerFrameExtendedCameraInfo](../../header-files-and-structs/structs/fg-perframeextendedcamerainfo/document.md)\* info)

 | 

Sets the extended camera attribute information. When the translation component of the view projection matrix is very large, this information is provided for more accurate frame generation. This API is optional. This API applies only to the OpenGL ES graphics API.

 |
| 

[FG\_ErrorCode](#ga68efbf5ff41faeb835f5587654c1e669) [HMS\_FG\_DestroyContext\_GLES](#ga8c61d12e9e4c8f7e95bed76006ee3335)([FG\_Context\_GLES](#ga62e666292d67fd19fd35ad07463e21cc)\*\* context)

 | 

Destroys a frame generation context instance and releases memory resources. This API applies only to the OpenGL ES graphics API.

 |
| 

[FG\_ErrorCode](#ga68efbf5ff41faeb835f5587654c1e669) [HMS\_FG\_SetIntegrationMode\_GLES](#section291123211916)([FG\_Context\_GLES](#ga62e666292d67fd19fd35ad07463e21cc)\* context, const [FG\_IntegrationInfo](../../header-files-and-structs/structs/fg-integrationinfo/document.md)\* integrationInfo)

 | 

Sets the integration information for frame generation. This API applies only to the OpenGL ES graphics API.

 |
| 

[FG\_ErrorCode](#ga68efbf5ff41faeb835f5587654c1e669) [HMS\_FG\_SetUiPredictionEnabled\_GLES](#section41231648141914)([FG\_Context\_GLES](#ga62e666292d67fd19fd35ad07463e21cc)\* context, bool isEnabled)

 | 

Sets whether to enable the UI prediction function. This function can be enabled only in system display mode. It is invalid in game display mode. This API applies only to the OpenGL ES graphics API.

 |
| 

[FG\_ErrorCode](#ga68efbf5ff41faeb835f5587654c1e669) [HMS\_FG\_SetTargetFps\_GLES](#section19112185207)([FG\_Context\_GLES](#ga62e666292d67fd19fd35ad07463e21cc)\* context, int targetFps)

 | 

Sets the target frame rate for frame generation. The setting takes effect only for the system display mode and is invalid for the game display mode. This API takes effect after the game is released for the first time and applies only to the OpenGL ES graphics API.

 |
| 

[FG\_Context\_VK](#ga4022ab63c2296d63dcf2c2df178508b7)\* [HMS\_FG\_CreateContext\_VK](#gac39606d03c25d898c656ab6973bb54f3)(const [FG\_ContextDescription\_VK](../../header-files-and-structs/structs/fg-contextdescription-vk/document.md)\* contextDescription)

 | 

Creates a frame generation context instance. If the call is successful, a pointer to the [FG\_Context\_VK](#ga4022ab63c2296d63dcf2c2df178508b7) object will be returned. This API applies only to the Vulkan graphics API.

 |
| 

[FG\_ErrorCode](#ga68efbf5ff41faeb835f5587654c1e669) [HMS\_FG\_SetAlgorithmMode\_VK](#ga9262d0cde377603a6ccc1239095be917)([FG\_Context\_VK](#ga4022ab63c2296d63dcf2c2df178508b7)\* context, const [FG\_AlgorithmModeInfo](../../header-files-and-structs/structs/fg-algorithmmodeinfo/document.md)\* predictionModeInfo)

 | 

Sets the frame generation algorithm mode, including the prediction algorithm mode and motion estimation mode. This API is mandatory. This API applies only to the Vulkan graphics API.

 |
| 

[FG\_ErrorCode](#ga68efbf5ff41faeb835f5587654c1e669) [HMS\_FG\_SetResolution\_VK](#ga2295f5bde5b0186e0f89f7d49e3338bf)([FG\_Context\_VK](#ga4022ab63c2296d63dcf2c2df178508b7)\* context, const [FG\_ResolutionInfo](../../header-files-and-structs/structs/fg-resolutioninfo/document.md)\* resolutionInfo)

 | 

Sets the resolutions of input and output images for frame generation. This API is mandatory. This API applies only to the Vulkan graphics API.

 |
| 

[FG\_ErrorCode](#ga68efbf5ff41faeb835f5587654c1e669) [HMS\_FG\_SetCvvZSemantic\_VK](#ga7a71df6640e6e95d5d6f67b2e24448fd)([FG\_Context\_VK](#ga4022ab63c2296d63dcf2c2df178508b7)\* context, [FG\_CvvZSemantic](#ga530448309918d6d703e28c61a848a267) semantic)

 | 

Sets the homogeneous clip space Z/W range and depth function. This API is optional. If it is not called, the default value **FG\_CVV\_Z\_SEMANTIC\_ZERO\_TO\_ONE\_FORWARD\_Z** will be used. This API applies only to the Vulkan graphics API.

 |
| 

[FG\_ErrorCode](#ga68efbf5ff41faeb835f5587654c1e669) [HMS\_FG\_SetImageFormat\_VK](#gabcb428cb2187ce986cf8ac0f1c76a3ca)([FG\_Context\_VK](#ga4022ab63c2296d63dcf2c2df178508b7)\* context, const [FG\_ImageFormat\_VK](../../header-files-and-structs/structs/fg-imageformat-vk/document.md)\* format)

 | 

Sets the input and output image formats for frame generation. This API is optional. If it is not called, the default value **VK\_FORMAT\_R8G8B8A8\_UNORM** will be used for the real frame color buffer and predicted frame buffer, and **VK\_FORMAT\_D24\_UNORM\_S8\_UINT** will be used for the depth stencil buffer. This API applies only to the Vulkan graphics API.

 |
| 

[FG\_ErrorCode](#ga68efbf5ff41faeb835f5587654c1e669) [HMS\_FG\_SetDepthStencilYDirectionInverted\_VK](#ga5148977465964658f817de45e28ab80a)([FG\_Context\_VK](#ga4022ab63c2296d63dcf2c2df178508b7)\* context, bool inverted)

 | 

Sets the flag bit for flipping the color buffer around the Y axis relative to the depth stencil buffer. This API is optional. If it is not called, no flipping is performed by default. This API applies only to the Vulkan graphics API. If flipping occurs but **inverted** is not set to **true**, the predicted frame effect may be abnormal.

 |
| 

[FG\_Image\_VK](#gabd6ee9704e997ffc2792ad3c89847019)\* [HMS\_FG\_CreateImage\_VK](#ga7733f097ea5f4ae4d2aa53d11d7e60ff)([FG\_Context\_VK](#ga4022ab63c2296d63dcf2c2df178508b7)\* context, VkImage image, VkImageView view)

 | 

Creates input and output image instances for frame generation. An image instance must be created through this API for the real frame color buffer, depth stencil buffer, and predicted frame buffer, respectively. Then, the created image instances are passed to the [HMS\_FG\_Dispatch\_VK](#ga21f86a194e72e99dd54fd39080385a37) API to generate a predicted frame. This API is used to associate the image resources in a game app with the frame generation algorithm implementation.

 |
| 

[FG\_ErrorCode](#ga68efbf5ff41faeb835f5587654c1e669) [HMS\_FG\_DestroyImage\_VK](#gac850c7cd41a1aebaf9bcf943ebff372a)([FG\_Context\_VK](#ga4022ab63c2296d63dcf2c2df178508b7)\* context, [FG\_Image\_VK](#gabd6ee9704e997ffc2792ad3c89847019)\* image)

 | 

Destroys input and output image instances for frame generation and cancels the corresponding association.

 |
| 

[FG\_ErrorCode](#ga68efbf5ff41faeb835f5587654c1e669) [HMS\_FG\_Activate\_VK](#ga6871faa08ebf19d380301cf400c086a8)([FG\_Context\_VK](#ga4022ab63c2296d63dcf2c2df178508b7)\* context)

 | 

Activates a frame generation context instance. Before the activation, the instance attributes must be set. For an activated frame generation context instance, the [HMS\_FG\_Dispatch\_VK](#ga21f86a194e72e99dd54fd39080385a37) API can be called to generate a predicted frame. This API applies only to the Vulkan graphics API.

 |
| 

[FG\_ErrorCode](#ga68efbf5ff41faeb835f5587654c1e669) [HMS\_FG\_Deactivate\_VK](#gad52fbbb8dcfd929300224cb91ce96380)([FG\_Context\_VK](#ga4022ab63c2296d63dcf2c2df178508b7)\* context)

 | 

Deactivates a frame generation context instance. To activate the instance again, call the [HMS\_FG\_Activate\_VK](#ga6871faa08ebf19d380301cf400c086a8) API.

 |
| 

[FG\_ErrorCode](#ga68efbf5ff41faeb835f5587654c1e669) [HMS\_FG\_IsActive\_VK](#ga2b8aea406b51b42083c740fbe44b3ad1)([FG\_Context\_VK](#ga4022ab63c2296d63dcf2c2df178508b7)\* context, bool\* isActive)

 | 

Checks whether a frame generation context instance is activated. This API applies only to the Vulkan graphics API.

 |
| 

[FG\_ErrorCode](#ga68efbf5ff41faeb835f5587654c1e669) [HMS\_FG\_Dispatch\_VK](#ga21f86a194e72e99dd54fd39080385a37)([FG\_Context\_VK](#ga4022ab63c2296d63dcf2c2df178508b7)\* context, const [FG\_DispatchDescription\_VK](../../header-files-and-structs/structs/fg-dispatchdescription-vk/document.md)\* desc)

 | 

Sets the parameter information required for frame prediction to generate a predicted frame. This API applies only to the Vulkan graphics API.

 |
| 

[FG\_ErrorCode](#ga68efbf5ff41faeb835f5587654c1e669) [HMS\_FG\_DestroyContext\_VK](#ga6be707669124e0bb6e5d61c2e24043be)([FG\_Context\_VK](#ga4022ab63c2296d63dcf2c2df178508b7)\*\* context)

 | 

Destroys a frame generation context instance and releases memory resources. This API applies only to the Vulkan graphics API.

 |
| 

[FG\_ErrorCode](#ga394c554fc5d056d702180ee031ccee2c) [HMS\_FG\_SetIntegrationMode\_VK](#section1557174711191)([FG\_Context\_VK](#ga4022ab63c2296d63dcf2c2df178508b7)\* context, const [FG\_IntegrationInfo](../../header-files-and-structs/structs/fg-integrationinfo/document.md)\* integrationInfo)

 | 

Sets the integration information for frame generation. This API applies only to the Vulkan graphics API.

 |
| 

[FG\_ErrorCode](#ga68efbf5ff41faeb835f5587654c1e669) [HMS\_FG\_SetUiPredictionEnabled\_VK](#section9619114861914)([FG\_Context\_VK](#ga4022ab63c2296d63dcf2c2df178508b7)\* context, bool isEnabled)

 | 

Sets whether to enable the UI prediction function. This function can be enabled only in system display mode. It is invalid in game display mode. This API applies only to the Vulkan graphics API.

 |
| 

[FG\_ErrorCode](#ga68efbf5ff41faeb835f5587654c1e669) [HMS\_FG\_SetTargetFps\_VK](#section655214195204)([FG\_Context\_VK](#ga4022ab63c2296d63dcf2c2df178508b7)\* context, int targetFps)

 | 

Sets the target frame rate for frame generation. The setting takes effect only for the system display mode and is invalid for the game display mode. This API takes effect after the game is released for the first time and applies only to the Vulkan graphics API.

 |
| 

[OpenGTX\_Context](#ga3ef8c7447a236d882b625ec8434385ed)\* [HMS\_OpenGTX\_CreateContext](#ga94aadbb64ffb5382a4661790c040f1c3)([OpenGTX\_DeviceInfoCallback](#ga1d66cec4aa0e01696d878c330f012d7a) deviceInfoCallback)

 | 

Creates an OpenGTX context instance. Each time this API is successfully called, an [OpenGTX\_Context](#ga3ef8c7447a236d882b625ec8434385ed) object is created and a pointer to the [OpenGTX\_Context](#ga3ef8c7447a236d882b625ec8434385ed) object is returned.

 |
| 

[OpenGTX\_ErrorCode](#ga97deebd9adf3e19947ec5b4615fa1d9c) [HMS\_OpenGTX\_Activate](#ga67e6cc5b491539c5e219f9e9ef15abca)([OpenGTX\_Context](#ga3ef8c7447a236d882b625ec8434385ed)\* context)

 | 

Activates an OpenGTX context instance. Before using an OpenGTX context instance, you need to activate it.

 |
| 

[OpenGTX\_ErrorCode](#ga97deebd9adf3e19947ec5b4615fa1d9c) [HMS\_OpenGTX\_Deactivate](#gaa741745687d067180d27d3be30db7422)([OpenGTX\_Context](#ga3ef8c7447a236d882b625ec8434385ed)\* context)

 | 

Deactivates an OpenGTX context instance. To activate the instance again, call the [HMS\_OpenGTX\_Activate](#ga67e6cc5b491539c5e219f9e9ef15abca) API.

 |
| 

[OpenGTX\_ErrorCode](#ga97deebd9adf3e19947ec5b4615fa1d9c) [HMS\_OpenGTX\_SetConfiguration](#gaaa09a16f113a0a9e0014b495ff961b6e)([OpenGTX\_Context](#ga3ef8c7447a236d882b625ec8434385ed)\* context, const [OpenGTX\_ConfigDescription](../../header-files-and-structs/structs/opengtx-configdescription/document.md)\* config)

 | 

Initializes an OpenGTX context instance and sets the OpenGTX context instance attributes.

 |
| 

[OpenGTX\_ErrorCode](#ga97deebd9adf3e19947ec5b4615fa1d9c) [HMS\_OpenGTX\_DispatchFrameRenderInfo](#ga0c0b0034e4a6337e509888b2a9611489)([OpenGTX\_Context](#ga3ef8c7447a236d882b625ec8434385ed)\* context, const [OpenGTX\_FrameRenderInfo](../../header-files-and-structs/structs/opengtx-framerenderinfo/document.md)\* frameRenderInfo)

 | 

Sets the frame rendering information required for OpenGTX running. The information needs to be updated after each change to a frame.

 |
| 

[OpenGTX\_ErrorCode](#ga97deebd9adf3e19947ec5b4615fa1d9c) [HMS\_OpenGTX\_DispatchGameSceneInfo](#gafd01b1b2726f10b10968cdcd73da632f)([OpenGTX\_Context](#ga3ef8c7447a236d882b625ec8434385ed)\* context, const [OpenGTX\_GameSceneInfo](../../header-files-and-structs/structs/opengtx-gamesceneinfo/document.md)\* gameSceneInfo)

 | 

Sets the game scene information required for OpenGTX running.

 |
| 

[OpenGTX\_ErrorCode](#ga97deebd9adf3e19947ec5b4615fa1d9c) [HMS\_OpenGTX\_DispatchNetworkInfo](#gad7a6544a832f28ef068df580ac8a1b78)([OpenGTX\_Context](#ga3ef8c7447a236d882b625ec8434385ed)\* context, const [OpenGTX\_NetworkInfo](../../header-files-and-structs/structs/opengtx-networkinfo/document.md)\* networkInfo)

 | 

Sets the network latency information required for OpenGTX running.

 |
| 

[OpenGTX\_ErrorCode](#ga97deebd9adf3e19947ec5b4615fa1d9c) [HMS\_OpenGTX\_DestroyContext](#ga0b757b487acf42e92b06178e159b03ac)([OpenGTX\_Context](#ga3ef8c7447a236d882b625ec8434385ed)\*\* context)

 | 

Destroys an OpenGTX context instance and releases memory resources.

 |

#### Type Definition Description

#### \[h2\]ABR\_CameraData

typedef struct [ABR\_CameraData](../../header-files-and-structs/structs/abr-cameradata/document.md) [ABR\_CameraData](../../header-files-and-structs/structs/abr-cameradata/document.md)

**Description**

Describes the camera motion data of a game app's each frame. The ABR capability adaptively adjusts the buffer resolution factor according to the camera motion data.

**Start version**: 5.0.0(12)

#### \[h2\]ABR\_Context

typedef struct [ABR\_Context](#ga52e8dba39ee979b70826401b3d36574e) [ABR\_Context](#ga52e8dba39ee979b70826401b3d36574e)

**Description**

Describes the ABR context.

**Start version**: 5.0.0(12)

#### \[h2\]ABR\_ErrorCode

typedef enum [ABR\_ErrorCode](#ga72df702d70a8326b5b46c118be6ad1d7) [ABR\_ErrorCode](#ga72df702d70a8326b5b46c118be6ad1d7)

**Description**

Describes the error codes of ABR API calls.

**Start version**: 5.0.0(12)

#### \[h2\]ABR\_RenderAPI\_Type

typedef enum [ABR\_RenderAPI\_Type](#ga9359d16ecefa21f0e6e5f29732cbf6f4) [ABR\_RenderAPI\_Type](#ga9359d16ecefa21f0e6e5f29732cbf6f4)

**Description**

Describes the graphics API types supported by the ABR capability.

**Start version**: 5.0.0(12)

#### \[h2\]ABR\_Vector3

typedef struct [ABR\_Vector3](../../header-files-and-structs/structs/abr-vector3/document.md) [ABR\_Vector3](../../header-files-and-structs/structs/abr-vector3/document.md)

**Description**

Describes an ABR 3D vector.

**Start version**: 5.0.0(12)

#### \[h2\]FG\_AlgorithmModeInfo

typedef struct [FG\_AlgorithmModeInfo](../../header-files-and-structs/structs/fg-algorithmmodeinfo/document.md) [FG\_AlgorithmModeInfo](../../header-files-and-structs/structs/fg-algorithmmodeinfo/document.md)

**Description**

Describes the frame generation algorithm mode information.

**Start version**: 5.0.0(12)

#### \[h2\]FG\_Context\_GLES

typedef struct [FG\_Context\_GLES](#ga62e666292d67fd19fd35ad07463e21cc) [FG\_Context\_GLES](#ga62e666292d67fd19fd35ad07463e21cc)

**Description**

Describes the frame generation context. This API applies only to the OpenGL ES graphics API.

**Start version**: 5.0.0(12)

#### \[h2\]FG\_Context\_VK

typedef struct [FG\_Context\_VK](#ga4022ab63c2296d63dcf2c2df178508b7) [FG\_Context\_VK](#ga4022ab63c2296d63dcf2c2df178508b7)

**Description**

Describes the frame generation context. This API applies only to the Vulkan graphics API.

**Start version**: 5.0.0(12)

#### \[h2\]FG\_ContextDescription\_VK

typedef struct [FG\_ContextDescription\_VK](../../header-files-and-structs/structs/fg-contextdescription-vk/document.md) [FG\_ContextDescription\_VK](../../header-files-and-structs/structs/fg-contextdescription-vk/document.md)

**Description**

Describes the attribute information required for creating a frame generation context instance [FG\_Context\_VK](#ga4022ab63c2296d63dcf2c2df178508b7).

**Start version**: 5.0.0(12)

#### \[h2\]FG\_CvvZSemantic

typedef enum [FG\_CvvZSemantic](#ga530448309918d6d703e28c61a848a267) [FG\_CvvZSemantic](#ga530448309918d6d703e28c61a848a267)

**Description**

Describes the homogeneous clip space Z/W ranges and depth functions after camera projection transformation.

**Start version**: 5.0.0(12)

#### \[h2\]FG\_Dimension2D

typedef struct [FG\_Dimension2D](../../header-files-and-structs/structs/fg-dimension2d/document.md) [FG\_Dimension2D](../../header-files-and-structs/structs/fg-dimension2d/document.md)

**Description**

Describes the 2D image resolution, in pixels.

**Start version**: 5.0.0(12)

#### \[h2\]FG\_DispatchDescription\_GLES

typedef struct [FG\_DispatchDescription\_GLES](../../header-files-and-structs/structs/fg-dispatchdescription-gles/document.md) [FG\_DispatchDescription\_GLES](../../header-files-and-structs/structs/fg-dispatchdescription-gles/document.md)

**Description**

Describes the parameter information required by [HMS\_FG\_Dispatch\_GLES](#gab135a0f59582d168d461ef115423cfb4). The parameter information needs to be updated for each frame. This API applies only to the OpenGL ES graphics API.

**Start version**: 5.0.0(12)

#### \[h2\]FG\_DispatchDescription\_VK

typedef struct [FG\_DispatchDescription\_VK](../../header-files-and-structs/structs/fg-dispatchdescription-vk/document.md) [FG\_DispatchDescription\_VK](../../header-files-and-structs/structs/fg-dispatchdescription-vk/document.md)

**Description**

Describes the parameter information required by [HMS\_FG\_Dispatch\_VK](#ga21f86a194e72e99dd54fd39080385a37). The parameter information needs to be updated for each frame. This API applies only to the Vulkan graphics API.

**Start version**: 5.0.0(12)

#### \[h2\]FG\_ErrorCode

typedef enum [FG\_ErrorCode](#ga68efbf5ff41faeb835f5587654c1e669) [FG\_ErrorCode](#ga68efbf5ff41faeb835f5587654c1e669)

**Description**

Describes the error codes of frame generation API calls.

**Start version**: 5.0.0(12)

#### \[h2\]FG\_Image\_VK

typedef struct [FG\_Image\_VK](#gabd6ee9704e997ffc2792ad3c89847019) [FG\_Image\_VK](#gabd6ee9704e997ffc2792ad3c89847019)

**Description**

Describes the input and output images for frame generation. This API applies only to the Vulkan graphics API.

**Start version**: 5.0.0(12)

#### \[h2\]FG\_ImageFormat\_GLES

typedef enum [FG\_ImageFormat\_GLES](#ga3bec27405891e089234bf50d0589c3cd) [FG\_ImageFormat\_GLES](#ga3bec27405891e089234bf50d0589c3cd)

**Description**

Describes the image formats of the real frame color buffer and the predicted frame buffer. This API applies only to the OpenGL ES graphics API.

**Start version**: 5.0.0(12)

#### \[h2\]FG\_ImageFormat\_VK

typedef struct [FG\_ImageFormat\_VK](../../header-files-and-structs/structs/fg-imageformat-vk/document.md) [FG\_ImageFormat\_VK](../../header-files-and-structs/structs/fg-imageformat-vk/document.md)

**Description**

Describes the input and output image format information for frame generation. This API applies only to the Vulkan graphics API.

**Start version**: 5.0.0(12)

#### \[h2\]FG\_ImageInfo\_VK

typedef struct [FG\_ImageInfo\_VK](../../header-files-and-structs/structs/fg-imageinfo-vk/document.md) [FG\_ImageInfo\_VK](../../header-files-and-structs/structs/fg-imageinfo-vk/document.md)

**Description**

Describes the input and output image information for frame generation.

**Start version**: 5.0.0(12)

#### \[h2\]FG\_ImageSync\_VK

typedef struct [FG\_ImageSync\_VK](../../header-files-and-structs/structs/fg-imagesync-vk/document.md) [FG\_ImageSync\_VK](../../header-files-and-structs/structs/fg-imagesync-vk/document.md)

**Description**

Describes the synchronization status information about the input and output images for frame generation. It is used to create a memory barrier for the images.

**Start version**: 5.0.0(12)

#### \[h2\]FG\_Mat4x4

typedef struct [FG\_Mat4x4](../../header-files-and-structs/structs/fg-mat4x4/document.md) [FG\_Mat4x4](../../header-files-and-structs/structs/fg-mat4x4/document.md)

**Description**

Describes a 4x4 matrix in column-major order.

**Start version**: 5.0.0(12)

#### \[h2\]FG\_MeMode

typedef enum [FG\_MeMode](#ga8bd44b6bea12774dd2ee6014d696e7d1) [FG\_MeMode](#ga8bd44b6bea12774dd2ee6014d696e7d1)

**Description**

Describes the motion estimation algorithm modes. The basic mode and enhanced mode are supported.

**Start version**: 5.0.0(12)

#### \[h2\]FG\_PredictionMode

typedef enum [FG\_PredictionMode](#gaea2169cd5ae4bf9e8a17dc58f33e8766) [FG\_PredictionMode](#gaea2169cd5ae4bf9e8a17dc58f33e8766)

**Description**

Describes the frame prediction algorithm modes for frame generation.

**Start version**: 5.0.0(12)

#### \[h2\]FG\_PresentMode

typedef struct [FG\_PresentMode](#section131101213459) [FG\_PresentMode](#section131101213459)

**Description**

Defines the predicted frame display modes, including the game display mode (the game sends predicted frames for display) and system display mode (the system sends predicted frames for display).

**Start version**: 5.1.0(18)

#### \[h2\]FG\_ResolutionInfo

typedef struct [FG\_ResolutionInfo](../../header-files-and-structs/structs/fg-resolutioninfo/document.md) [FG\_ResolutionInfo](../../header-files-and-structs/structs/fg-resolutioninfo/document.md)

**Description**

Describes the resolutions of input and output images for frame generation.

**Start version**: 5.0.0(12)

#### \[h2\]FG\_Vec3D

typedef struct [FG\_Vec3D](../../header-files-and-structs/structs/fg-vec3d/document.md) [FG\_Vec3D](../../header-files-and-structs/structs/fg-vec3d/document.md)

**Description**

Describes a frame generation 3D vector.

**Start version**: 5.0.0(12)

#### \[h2\]FG\_PerFrameExtendedCameraInfo

typedef struct [FG\_PerFrameExtendedCameraInfo](../../header-files-and-structs/structs/fg-perframeextendedcamerainfo/document.md) [FG\_PerFrameExtendedCameraInfo](../../header-files-and-structs/structs/fg-perframeextendedcamerainfo/document.md)

**Description**

Describes extended camera information. When the translation component of the view projection matrix is very large, more detailed camera information can be provided for more accurate frame prediction.

**Start version**: 5.0.0(12)

#### \[h2\]FG\_IntegrationInfo

typedef struct [FG\_IntegrationInfo](../../header-files-and-structs/structs/fg-integrationinfo/document.md) [FG\_IntegrationInfo](../../header-files-and-structs/structs/fg-integrationinfo/document.md)

**Description**

Describes the integration information about frame generation, including the display mode, whether to separately buffer depth and color textures, and whether to flip the color texture. It takes effect only when [FG\_PredictionMode](#gaea2169cd5ae4bf9e8a17dc58f33e8766) is set to **FG\_PREDICTION\_MODE\_INTERPOLATION**.

**Start version**: 5.1.0(18)

#### \[h2\]OpenGTX\_ConfigDescription

typedef struct [OpenGTX\_ConfigDescription](../../header-files-and-structs/structs/opengtx-configdescription/document.md) [OpenGTX\_ConfigDescription](../../header-files-and-structs/structs/opengtx-configdescription/document.md)

**Description**

Describes the OpenGTX attribute settings.

**Start version**: 5.0.0(12)

#### \[h2\]OpenGTX\_Context

typedef struct [OpenGTX\_Context](#ga3ef8c7447a236d882b625ec8434385ed) [OpenGTX\_Context](#ga3ef8c7447a236d882b625ec8434385ed)

**Description**

Describes the OpenGTX context.

**Start version**: 5.0.0(12)

#### \[h2\]OpenGTX\_DeviceInfoCallback

typedef void(\* OpenGTX\_DeviceInfoCallback) ([OpenGTX\_TempLevel](#gaeff4735d18eb3086603ab6d04e7ad133))

**Description**

Callback for device temperature information.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

OpenGTX\_TempLevel

 | 

Device temperature level ([OpenGTX\_TempLevel](#ga4571f1a424d551ba387ab3ea4fd6d8b8)).

 |

#### \[h2\]OpenGTX\_EngineType

typedef enum [OpenGTX\_EngineType](#gadd5a5e0b3b4aa3ea8b0974cba13c0389) [OpenGTX\_EngineType](#gadd5a5e0b3b4aa3ea8b0974cba13c0389)

**Description**

Describes the underlying game engine types used by game apps.

**Start version**: 5.0.0(12)

#### \[h2\]OpenGTX\_ErrorCode

typedef enum [OpenGTX\_ErrorCode](#ga97deebd9adf3e19947ec5b4615fa1d9c) [OpenGTX\_ErrorCode](#ga97deebd9adf3e19947ec5b4615fa1d9c)

**Description**

Describes the error codes of OpenGTX API calls.

**Start version**: 5.0.0(12)

#### \[h2\]OpenGTX\_FrameRenderInfo

typedef struct [OpenGTX\_FrameRenderInfo](../../header-files-and-structs/structs/opengtx-framerenderinfo/document.md) [OpenGTX\_FrameRenderInfo](../../header-files-and-structs/structs/opengtx-framerenderinfo/document.md)

**Description**

Describes the frame rendering information. This struct is passed by a game app after obtaining the frame attributes.

**Start version**: 5.0.0(12)

#### \[h2\]OpenGTX\_GameSceneInfo

typedef struct [OpenGTX\_GameSceneInfo](../../header-files-and-structs/structs/opengtx-gamesceneinfo/document.md) [OpenGTX\_GameSceneInfo](../../header-files-and-structs/structs/opengtx-gamesceneinfo/document.md)

**Description**

Describes the game scene information. This struct is passed by a game app after obtaining the scene information.

**Start version**: 5.0.0(12)

#### \[h2\]OpenGTX\_GameType

typedef enum [OpenGTX\_GameType](#ga34d898acfaacb3750db454a9ed2038a5) [OpenGTX\_GameType](#ga34d898acfaacb3750db454a9ed2038a5)

**Description**

Describes the game types.

**Start version**: 5.0.0(12)

#### \[h2\]OpenGTX\_LTPO\_Mode

typedef enum [OpenGTX\_LTPO\_Mode](#gad531d05ca502b93f4153e4b1f749ed0c) [OpenGTX\_LTPO\_Mode](#gad531d05ca502b93f4153e4b1f749ed0c)

**Description**

Describes the OpenGTX\_LTPO modes for controlling the game frame rate.

**Start version**: 5.0.0(12)

#### \[h2\]OpenGTX\_NetworkInfo

typedef struct [OpenGTX\_NetworkInfo](../../header-files-and-structs/structs/opengtx-networkinfo/document.md) [OpenGTX\_NetworkInfo](../../header-files-and-structs/structs/opengtx-networkinfo/document.md)

**Description**

Describes the current device network information. This struct is passed by a game app after obtaining the network information.

**Start version**: 5.0.0(12)

#### \[h2\]OpenGTX\_NetworkLatency

typedef struct [OpenGTX\_NetworkLatency](../../header-files-and-structs/structs/opengtx-networklatency/document.md) [OpenGTX\_NetworkLatency](../../header-files-and-structs/structs/opengtx-networklatency/document.md)

**Description**

Describes the current device network latency information. This struct is passed by a game app after obtaining the network latency information.

**Start version**: 5.0.0(12)

#### \[h2\]OpenGTX\_PictureQualityMaxLevel

typedef enum [OpenGTX\_PictureQualityMaxLevel](#gacd5c090213b3593e7c9ab6c93118ff8e) [OpenGTX\_PictureQualityMaxLevel](#gacd5c090213b3593e7c9ab6c93118ff8e)

**Description**

Describes the game app image quality levels.

**Start version**: 5.0.0(12)

#### \[h2\]OpenGTX\_ResolutionValue

typedef struct [OpenGTX\_ResolutionValue](../../header-files-and-structs/structs/opengtx-resolutionvalue/document.md) [OpenGTX\_ResolutionValue](../../header-files-and-structs/structs/opengtx-resolutionvalue/document.md)

**Description**

Describes the resolution of a game app.

**Start version**: 5.0.0(12)

#### \[h2\]OpenGTX\_SceneID

typedef enum [OpenGTX\_SceneID](#gad7e5d2d235183dc0c6549331d6bc2932) [OpenGTX\_SceneID](#gad7e5d2d235183dc0c6549331d6bc2932)

**Description**

Describes the OpenGTX game scene types.

**Start version**: 5.0.0(12)

#### \[h2\]OpenGTX\_TempLevel

typedef enum [OpenGTX\_TempLevel](#gaeff4735d18eb3086603ab6d04e7ad133) [OpenGTX\_TempLevel](#gaeff4735d18eb3086603ab6d04e7ad133)

**Description**

Describes the device temperature levels.

**Start version**: 5.0.0(12)

#### \[h2\]OpenGTX\_Vector3

typedef struct [OpenGTX\_Vector3](../../header-files-and-structs/structs/opengtx-vector3/document.md) [OpenGTX\_Vector3](../../header-files-and-structs/structs/opengtx-vector3/document.md)

**Description**

Describes an OpenGTX 3D vector.

**Start version**: 5.0.0(12)

#### Enumeration Description

#### \[h2\]ABR\_ErrorCode

enum [ABR\_ErrorCode](#ga72df702d70a8326b5b46c118be6ad1d7)

**Description**

Describes the error codes of ABR API calls.

**Start version**: 5.0.0(12)

| 
Enumerated Value

 | 

Description

 |
| :-- | :-- |
| 

ABR\_SUCCESS

 | 

The API execution is successful.

 |
| 

ABR\_INVALID\_PARAMETER

 | 

Invalid parameters, including a missing mandatory parameter, an incorrect parameter type, and an invalid parameter value.

 |
| 

ABR\_CONTEXT\_CONFIG\_AFTER\_ACTIVE

 | 

The attributes of an ABR context instance are to be set after the instance is activated. This error code is returned if an ABR context instance has been activated before attribute setting.

 |
| 

ABR\_CONTEXT\_NOT\_CONFIG

 | 

The ABR context instance attributes are not set. This error code is returned if the ABR context instance attributes are not set or fail to be set when [HMS\_ABR\_Activate](#ga463d8d5396bfd5f6ed800ddab616479a) is called.

 |
| 

ABR\_CONTEXT\_NOT\_ACTIVE

 | 

The ABR context instance is not activated. This error code is returned if the ABR context instance is not activated when [HMS\_ABR\_MarkFrameBuffer\_GLES](#ga821fb33620312d3adba51d30254c1ef0) or an ABR update-related function is called.

 |
| 

ABR\_METADATA\_INVALID

 | 

Invalid ABR metadata. This error code is returned if invalid metadata is detected during ABR context instance attribute setting.

 |
| 

ABR\_FRAMEBUFFER\_INVALID

 | 

Invalid buffer. This error code is returned if an invalid buffer is detected when [HMS\_ABR\_MarkFrameBuffer\_GLES](#ga821fb33620312d3adba51d30254c1ef0) is called.

 |

#### \[h2\]ABR\_RenderAPI\_Type

enum [ABR\_RenderAPI\_Type](#ga9359d16ecefa21f0e6e5f29732cbf6f4)

**Description**

Describes the graphics API types supported by the ABR capability.

**Start version**: 5.0.0(12)

| 
Enumerated Value

 | 

Description

 |
| :-- | :-- |
| 

RENDER\_API\_GLES

 | 

OpenGL ES API

 |

#### \[h2\]FG\_CvvZSemantic

enum [FG\_CvvZSemantic](#ga530448309918d6d703e28c61a848a267)

**Description**

Describes the homogeneous clip space Z/W ranges and depth functions after camera projection transformation.

**Start version**: 5.0.0(12)

| 
Enumerated Value

 | 

Description

 |
| :-- | :-- |
| 

FG\_CVV\_Z\_SEMANTIC\_MINUS\_ONE\_TO\_ONE\_FORWARD\_Z

 | 

After projection transformation, the homogeneous clip space Z/W range is \[–1, 1\] and the depth function is **less equal**, which are usually used by the OpenGL ES graphics API.

 |
| 

FG\_CVV\_Z\_SEMANTIC\_ZERO\_TO\_ONE\_REVERSE\_Z

 | 

After projection transformation, the homogeneous clip space Z/W range is \[0, 1\] and the depth function is **greater equal**, which are usually used by the DirectX or Vulkan graphics API.

 |
| 

FG\_CVV\_Z\_SEMANTIC\_MINUS\_ONE\_TO\_ONE\_REVERSE\_Z

 | 

After projection transformation, the homogeneous clip space Z/W range is \[–1, 1\] and the depth function is **greater equal**.

 |
| 

FG\_CVV\_Z\_SEMANTIC\_ZERO\_TO\_ONE\_FORWARD\_Z

 | 

After projection transformation, the homogeneous clip space Z/W range is \[0, 1\] and the depth function is **less equal**.

 |

#### \[h2\]FG\_ErrorCode

enum [FG\_ErrorCode](#ga68efbf5ff41faeb835f5587654c1e669)

**Description**

Describes the error codes of frame generation API calls.

**Start version**: 5.0.0(12)

| 
Enumerated Value

 | 

Description

 |
| :-- | :-- |
| 

FG\_SUCCESS

 | 

The API execution is successful.

 |
| 

FG\_INVALID\_PARAMETER

 | 

Invalid parameters, including a missing mandatory parameter, an incorrect parameter type, and an invalid parameter value.

 |
| 

FG\_CONTEXT\_NOT\_CONFIG

 | 

The frame generation context instance attributes are not set. This error code is returned if the frame generation context instance attributes are not set or fail to be set when [HMS\_FG\_Activate\_GLES](#gaa5f1d5b98694100aa3e3dbb4c99ac23a) is called.

 |
| 

FG\_CONTEXT\_NOT\_ACTIVE

 | 

The frame generation context instance is not activated. This error code is returned if the frame generation context instance is not activated when [HMS\_FG\_Dispatch\_GLES](#gab135a0f59582d168d461ef115423cfb4) is called.

 |
| 

FG\_COLLECTING\_PREVIOUS\_FRAMES

 | 

Multiple historical frames need to be passed for motion estimation during frame generation. This error code is returned and no predicted frame will be generated if the number of passed frames is less than a fixed threshold when [HMS\_FG\_Dispatch\_GLES](#gab135a0f59582d168d461ef115423cfb4) is called. The threshold value is **2** for the following modes: GLES basic interpolation mode, GLES enhanced interpolation mode, and GLES enhanced extrapolation mode. The threshold value is **3** for the following modes: GLES basic extrapolation mode, Vulkan basic interpolation mode, and Vulkan basic extrapolation mode. When the number of passed frames reaches the fixed threshold, the call will be successful and **FG\_SUCCESS** is returned.

 |

#### \[h2\]FG\_ImageFormat\_GLES

enum [FG\_ImageFormat\_GLES](#ga3bec27405891e089234bf50d0589c3cd)

**Description**

Describes the image formats of the real frame color buffer and the predicted frame buffer. This API applies only to the OpenGL ES graphics API.

**Start version**: 5.0.0(12)

| 
Enumerated Value

 | 

Description

 |
| :-- | :-- |
| 

FG\_FORMAT\_R8G8B8A8\_UNORM

 | 

GL\_RGBA8.

 |
| 

FG\_FORMAT\_R11G11B10\_SFLOAT

 | 

GL\_R11F\_G11F\_B10F.

 |
| 

FG\_FORMAT\_R16G16B16A16\_SFLOAT

 | 

GL\_RGBA16F.

 |

#### \[h2\]FG\_MeMode

enum [FG\_MeMode](#ga8bd44b6bea12774dd2ee6014d696e7d1)

**Description**

Describes the motion estimation algorithm modes. The basic mode and enhanced mode are supported.

**Start version**: 5.0.0(12)

| 
Enumerated Value

 | 

Description

 |
| :-- | :-- |
| 

FG\_ME\_MODE\_BASIC

 | 

Basic mode. Motion estimation is performed by using the color, depth, and camera matrix information about historical frames.

 |
| 

FG\_ME\_MODE\_ENHANCED

 | 

Enhanced mode. The geometric vertex information about historical frames is used for more accurate motion estimation to draw predicted frames with higher quality. In this mode, you need to mark the draw calls for drawing vertices. If depth information is not passed, you can switch to the AI-based frame generation mode.

 |

#### \[h2\]FG\_PredictionMode

enum [FG\_PredictionMode](#gaea2169cd5ae4bf9e8a17dc58f33e8766)

**Description**

Describes the frame prediction algorithm modes for frame generation.

**Start version**: 5.0.0(12)

| 
Enumerated Value

 | 

Description

 |
| :-- | :-- |
| 

FG\_PREDICTION\_MODE\_INTERPOLATION

 | 

Interpolation mode. A predicted frame (frame N-0.5) is generated between two adjacent real frames (frame N–1 and frame N). This mode applies to role-playing games, racing games, and other games that have high requirements on rendering quality and running smoothness.

 |
| 

FG\_PREDICTION\_MODE\_EXTRAPOLATION

 | 

Extrapolation mode. A future predicted frame (frame N+0.5) is generated based on two adjacent real frames (frame N–1 and frame N). This mode applies to action games, shooting games, and other games that have high requirements on response latency and operation sensitivity.

 |

#### \[h2\]FG\_PresentMode

enum FG\_PresentMode

**Description**

Defines the predicted frame display modes, including the game display mode (the game sends predicted frames for display) and system display mode (the system sends predicted frames for display).

**Start version**: 5.1.0(18)

| 
Enumerated Value

 | 

Description

 |
| :-- | :-- |
| 

FG\_PRESENT\_BY\_GAME

 | 

The game applies for and manages predicted frames, and sends the predicted frames for display.

 |
| 

FG\_PRESENT\_BY\_SYSTEM

 | 

The system applies for and manages predicted frames, and sends the predicted frames for display.

 |

#### \[h2\]OpenGTX\_EngineType

enum [OpenGTX\_EngineType](#gadd5a5e0b3b4aa3ea8b0974cba13c0389)

**Description**

Describes the underlying game engine types used by game apps.

**Start version**: 5.0.0(12)

| 
Enumerated Value

 | 

Description

 |
| :-- | :-- |
| 

UNITY

 | 

Unity.

 |
| 

UNREAL

 | 

Unreal.

 |
| 

MESSIAH

 | 

Messiah.

 |
| 

COCOS

 | 

Cocos.

 |
| 

OTHERS\_ENGINE

 | 

Other engines.

 |

#### \[h2\]OpenGTX\_ErrorCode

enum [OpenGTX\_ErrorCode](#ga97deebd9adf3e19947ec5b4615fa1d9c)

**Description**

Describes the error codes of OpenGTX API calls.

**Start version**: 5.0.0(12)

| 
Enumerated Value

 | 

Description

 |
| :-- | :-- |
| 

OPENGTX\_SUCCESS

 | 

The API execution is successful.

 |
| 

OPENGTX\_INVALID\_PARAMETER

 | 

Invalid parameters, including a missing mandatory parameter, an incorrect parameter type, and an invalid parameter value.

 |
| 

OPENGTX\_CONTEXT\_NOT\_CONFIG

 | 

The OpenGTX context instance attributes are not set. This error code is returned if the OpenGTX context instance attributes are not set when functions such as [HMS\_OpenGTX\_DispatchFrameRenderInfo](#ga0c0b0034e4a6337e509888b2a9611489) are called.

 |
| 

OPENGTX\_CONTEXT\_NOT\_ACTIVE

 | 

The OpenGTX context instance is not activated. This error code is returned if the OpenGTX context instance is not activated when functions such as [HMS\_OpenGTX\_DispatchFrameRenderInfo](#ga0c0b0034e4a6337e509888b2a9611489) are called.

 |

#### \[h2\]OpenGTX\_GameType

enum [OpenGTX\_GameType](#ga34d898acfaacb3750db454a9ed2038a5)

**Description**

Describes the game types.

**Start version**: 5.0.0(12)

| 
Enumerated Value

 | 

Description

 |
| :-- | :-- |
| 

MOBA

 | 

Multiplayer online battle arena (MOBA).

 |
| 

RPG

 | 

Role-playing game (RPG).

 |
| 

FPS

 | 

First-person shooter (FPS).

 |
| 

RAC

 | 

Racing (RAC).

 |
| 

OTHERS\_TYPE

 | 

Other game types.

 |

#### \[h2\]OpenGTX\_LTPO\_Mode

enum [OpenGTX\_LTPO\_Mode](#gad531d05ca502b93f4153e4b1f749ed0c)

**Description**

Describes the OpenGTX\_LTPO modes for controlling the game frame rate.

**Start version**: 5.0.0(12)

| 
Enumerated Value

 | 

Description

 |
| :-- | :-- |
| 

SCENE\_MODE

 | 

Scene mode.

 |
| 

TOUCH\_MODE

 | 

Touch mode.

 |
| 

ADAPTIVE\_MODE

 | 

Adaptive mode.

 |

#### \[h2\]OpenGTX\_PictureQualityMaxLevel

enum [OpenGTX\_PictureQualityMaxLevel](#gacd5c090213b3593e7c9ab6c93118ff8e)

**Description**

Describes the game app image quality levels.

**Start version**: 5.0.0(12)

| 
Enumerated Value

 | 

Description

 |
| :-- | :-- |
| 

SD

 | 

SD, for example, 480p.

 |
| 

HD

 | 

HD, for example, 720p.

 |
| 

FHD

 | 

FHD, for example, 1080p.

 |
| 

QHD

 | 

QHD, for example, 2K.

 |
| 

UHD

 | 

UHD, for example, 4K.

 |

#### \[h2\]OpenGTX\_SceneID

enum [OpenGTX\_SceneID](#gad7e5d2d235183dc0c6549331d6bc2932)

**Description**

Describes the OpenGTX game scene types.

**Start version**: 5.0.0(12)

| 
Enumerated Value

 | 

Description

 |
| :-- | :-- |
| 

LOGIN

 | 

Login.

 |
| 

GAME\_INTERFACE

 | 

Game hall.

 |
| 

LOADING

 | 

Loading a game.

 |
| 

PLAYING

 | 

Playing a game.

 |
| 

SPECTATOR

 | 

Spectating a game.

 |
| 

DEATH

 | 

Preparing for combat.

 |
| 

HEAVY\_LOAD

 | 

Heavy load.

 |
| 

OTHERS\_SCENE

 | 

Other scenes.

 |

#### \[h2\]OpenGTX\_TempLevel

enum [OpenGTX\_TempLevel](#gaeff4735d18eb3086603ab6d04e7ad133)

**Description**

Describes the device temperature levels.

**Start version**: 5.0.0(12)

| 
Enumerated Value

 | 

Description

 |
| :-- | :-- |
| 

TEMP\_LEVEL1

 | 

Temperature level 1. The game can retain the current settings.

 |
| 

TEMP\_LEVEL2

 | 

Temperature level 2. The game should reduce unnecessary services, such as background updates.

 |
| 

TEMP\_LEVEL3

 | 

Temperature level 3. The game should stop non-key services.

 |
| 

TEMP\_LEVEL4

 | 

Temperature level 4. The game should lower its gaming effect.

 |
| 

TEMP\_LEVEL5

 | 

Temperature level 5. The game should lower its scene settings, such as the frame resolution, frame rate, and image quality.

 |
| 

TEMP\_LEVEL6

 | 

Temperature level 6. The game should maintain the minimum settings.

 |

#### Function Description

#### \[h2\]HMS\_ABR\_Activate()

[ABR\_ErrorCode](#ga72df702d70a8326b5b46c118be6ad1d7) HMS\_ABR\_Activate([ABR\_Context](#ga52e8dba39ee979b70826401b3d36574e)\* context)

**Description**

Activates an ABR context instance. Before the activation, the [HMS\_ABR\_SetTargetFps](#ga6c613e02088d559b9dc1450fde15bc2a) and [HMS\_ABR\_SetScaleRange](#ga1001c6a7739d8ce57bf851986f121bf5) APIs must be called to set instance attributes.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

context

 | 

Created ABR context instance, that is, a pointer to the [ABR\_Context](#ga52e8dba39ee979b70826401b3d36574e) instance. The pointer should not be null. Otherwise, an error code indicating failure is returned.

 |

**Returns**:

Execution result of the function. If the execution is successful, **ABR\_SUCCESS** is returned. If the execution fails, an error code is returned. For details about the error codes, please refer to [ABR\_ErrorCode](#ga86d5860f91dc4f1de6b381cd65389b9d).

#### \[h2\]HMS\_ABR\_CreateContext()

[ABR\_Context](#ga52e8dba39ee979b70826401b3d36574e)\* HMS\_ABR\_CreateContext([ABR\_RenderAPI\_Type](#ga9359d16ecefa21f0e6e5f29732cbf6f4) type)

**Description**

Creates an ABR context instance. Each time this API is successfully called, an [ABR\_Context](#ga52e8dba39ee979b70826401b3d36574e) object is created and a pointer to the [ABR\_Context](#ga52e8dba39ee979b70826401b3d36574e) object is returned.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

type

 | 

Graphics API type. The options are specified by [ABR\_RenderAPI\_Type](#ga3a6ead3a3c0f19a6434e97fda13f42f2).

 |

**Returns**:

If the call is successful, a pointer to [ABR\_Context](#ga52e8dba39ee979b70826401b3d36574e) is returned. If the call fails, a null pointer is returned.

#### \[h2\]HMS\_ABR\_Deactivate()

[ABR\_ErrorCode](#ga72df702d70a8326b5b46c118be6ad1d7) HMS\_ABR\_Deactivate([ABR\_Context](#ga52e8dba39ee979b70826401b3d36574e)\* context)

**Description**

Deactivates an ABR context instance. To activate the instance again, call the [HMS\_ABR\_Activate](#ga463d8d5396bfd5f6ed800ddab616479a) API.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

context

 | 

Created ABR context instance, that is, a pointer to the [ABR\_Context](#ga52e8dba39ee979b70826401b3d36574e) instance. The pointer should not be null. Otherwise, an error code indicating failure is returned.

 |

**Returns**:

Execution result of the function. If the execution is successful, **ABR\_SUCCESS** is returned. If the execution fails, an error code is returned. For details about the error codes, please refer to [ABR\_ErrorCode](#ga86d5860f91dc4f1de6b381cd65389b9d).

#### \[h2\]HMS\_ABR\_DestroyContext()

[ABR\_ErrorCode](#ga72df702d70a8326b5b46c118be6ad1d7) HMS\_ABR\_DestroyContext([ABR\_Context](#ga52e8dba39ee979b70826401b3d36574e)\*\* context)

**Description**

Destroys an ABR context instance and releases memory resources.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

context

 | 

Level-2 pointer to a created [ABR\_Context](#ga52e8dba39ee979b70826401b3d36574e) instance. The pointer should not be null. Otherwise, an error code indicating failure is returned.

 |

**Returns**:

Execution result of the function. If the execution is successful, **ABR\_SUCCESS** is returned. If the execution fails, an error code is returned. For details about the error codes, please refer to [ABR\_ErrorCode](#ga86d5860f91dc4f1de6b381cd65389b9d).

#### \[h2\]HMS\_ABR\_GetScale()

[ABR\_ErrorCode](#ga72df702d70a8326b5b46c118be6ad1d7) HMS\_ABR\_GetScale([ABR\_Context](#ga52e8dba39ee979b70826401b3d36574e)\* context, float\* scale )

**Description**

Obtains the buffer resolution factor for adaptive resolution adjustment.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

context

 | 

Created ABR context instance, that is, a pointer to the [ABR\_Context](#ga52e8dba39ee979b70826401b3d36574e) instance. The pointer should not be null. Otherwise, an error code indicating failure is returned.

 |
| 

scale

 | 

Points to a variable used to specify the ABR resolution factor. The pointer should not be null. Otherwise, an error code indicating failure is returned. The value range of **scale** is \[0.5, 1.0\].

 |

**Returns**:

Execution result of the function. If the execution is successful, **ABR\_SUCCESS** is returned. If the execution fails, an error code is returned. For details about the error codes, please refer to [ABR\_ErrorCode](#ga86d5860f91dc4f1de6b381cd65389b9d).

#### \[h2\]HMS\_ABR\_GetNextScale()

[ABR\_ErrorCode](#ga72df702d70a8326b5b46c118be6ad1d7) HMS\_ABR\_GetNextScale([ABR\_Context](#ga52e8dba39ee979b70826401b3d36574e)\* context, float\* scale)

**Description**

Obtains the ABR buffer resolution factor of the next frame.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

context

 | 

Created ABR context instance, that is, a pointer to the [ABR\_Context](#ga52e8dba39ee979b70826401b3d36574e) instance. The pointer should not be null. Otherwise, an error code indicating failure is returned.

 |
| 

scale

 | 

Points to a variable used to specify the ABR resolution factor. The pointer should not be null. Otherwise, an error code indicating failure is returned. The value range of **scale** is \[0.5, 1.0\].

 |

**Returns**:

Execution result of the function. If the execution is successful, **ABR\_SUCCESS** is returned. If the execution fails, an error code is returned. For details about the error codes, please refer to [ABR\_ErrorCode](#ga86d5860f91dc4f1de6b381cd65389b9d).

#### \[h2\]HMS\_ABR\_IsActive()

[ABR\_ErrorCode](#ga72df702d70a8326b5b46c118be6ad1d7) HMS\_ABR\_IsActive([ABR\_Context](#ga52e8dba39ee979b70826401b3d36574e)\* context, bool\* isActive )

**Description**

Checks whether an ABR context instance is activated.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

context

 | 

Created ABR context instance, that is, a pointer to the [ABR\_Context](#ga52e8dba39ee979b70826401b3d36574e) instance. The pointer should not be null. Otherwise, an error code indicating failure is returned.

 |
| 

isActive

 | 

Indicates whether an ABR context instance is activated.

-   **true**: yes
-   **false**: no

 |

**Returns**:

Execution result of the function. If the execution is successful, **ABR\_SUCCESS** is returned. If the execution fails, an error code is returned. For details about the error codes, please refer to [ABR\_ErrorCode](#ga86d5860f91dc4f1de6b381cd65389b9d).

#### \[h2\]HMS\_ABR\_MarkFrameBuffer\_GLES()

[ABR\_ErrorCode](#ga72df702d70a8326b5b46c118be6ad1d7) HMS\_ABR\_MarkFrameBuffer\_GLES([ABR\_Context](#ga52e8dba39ee979b70826401b3d36574e)\* context)

**Description**

Marks a GLES buffer for adaptive rendering. This API must be called before the rendering is started.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

context

 | 

Created ABR context instance, that is, a pointer to the [ABR\_Context](#ga52e8dba39ee979b70826401b3d36574e) instance. The pointer should not be null. Otherwise, an error code indicating failure is returned.

 |

**Returns**:

Execution result of the function. If the execution is successful, **ABR\_SUCCESS** is returned. If the execution fails, an error code is returned. For details about the error codes, please refer to [ABR\_ErrorCode](#ga86d5860f91dc4f1de6b381cd65389b9d).

#### \[h2\]HMS\_ABR\_GetScaledTexture\_GLES()

[ABR\_ErrorCode](#ga72df702d70a8326b5b46c118be6ad1d7) HMS\_ABR\_GetScaledTexture\_GLES([ABR\_Context](#ga52e8dba39ee979b70826401b3d36574e)\* context, uint32\_t originTexture, uint32\_t\* scaledTexture)

**Description**

Obtains the GLES texture index after adaptive buffer resolution adjustment based on the GLES texture index corresponding to the original resolution.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

context

 | 

Created ABR context instance, that is, a pointer to the [ABR\_Context](#ga52e8dba39ee979b70826401b3d36574e) instance. The pointer should not be null. Otherwise, an error code indicating failure is returned.

 |
| 

originTexture

 | 

GLES texture index of the original resolution.

 |
| 

scaledTexture

 | 

GLES texture index after adaptive buffer resolution adjustment.

 |

**Returns**:

Execution result of the function. If the execution is successful, **ABR\_SUCCESS** is returned. If the execution fails, an error code is returned. For details about the error codes, please refer to [ABR\_ErrorCode](#ga86d5860f91dc4f1de6b381cd65389b9d).

#### \[h2\]HMS\_ABR\_SetScaleRange()

[ABR\_ErrorCode](#ga72df702d70a8326b5b46c118be6ad1d7) HMS\_ABR\_SetScaleRange([ABR\_Context](#ga52e8dba39ee979b70826401b3d36574e)\* context, const float minValue, const float maxValue )

**Description**

Sets the buffer resolution factor range of an ABR context instance.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

context

 | 

Created ABR context instance, that is, a pointer to the [ABR\_Context](#ga52e8dba39ee979b70826401b3d36574e) instance. The pointer should not be null. Otherwise, an error code indicating failure is returned.

 |
| 

minValue

 | 

Minimum buffer resolution factor of an ABR context instance. The value range is \[0.5, 1.0\].

 |
| 

maxValue

 | 

Maximum buffer resolution factor of an ABR context instance. The value range is \[0.5, 1.0\].

 |

**Returns**:

Execution result of the function. If the execution is successful, **ABR\_SUCCESS** is returned. If the execution fails, an error code is returned. For details about the error codes, please refer to [ABR\_ErrorCode](#ga86d5860f91dc4f1de6b381cd65389b9d).

#### \[h2\]HMS\_ABR\_SetTargetFps()

[ABR\_ErrorCode](#ga72df702d70a8326b5b46c118be6ad1d7) HMS\_ABR\_SetTargetFps([ABR\_Context](#ga52e8dba39ee979b70826401b3d36574e)\* context, const uint32\_t targetFps )

**Description**

Sets the target frame rate of an ABR context instance.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

context

 | 

Created ABR context instance, that is, a pointer to the [ABR\_Context](#ga52e8dba39ee979b70826401b3d36574e) instance. The pointer should not be null. Otherwise, an error code indicating failure is returned.

 |
| 

targetFps

 | 

Target frame rate of an ABR context instance. The value range is \[30, 120\].

 |

**Returns**:

Execution result of the function. If the execution is successful, **ABR\_SUCCESS** is returned. If the execution fails, an error code is returned. For details about the error codes, please refer to [ABR\_ErrorCode](#ga86d5860f91dc4f1de6b381cd65389b9d).

#### \[h2\]HMS\_ABR\_UpdateCameraData()

[ABR\_ErrorCode](#ga72df702d70a8326b5b46c118be6ad1d7) HMS\_ABR\_UpdateCameraData([ABR\_Context](#ga52e8dba39ee979b70826401b3d36574e)\* context, [ABR\_CameraData](../../header-files-and-structs/structs/abr-cameradata/document.md)\* data )

**Description**

Updates the camera motion data of each frame. Before the update, the [HMS\_ABR\_Activate](#ga463d8d5396bfd5f6ed800ddab616479a) API must be called to activate the ABR context instance.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

context

 | 

Created ABR context instance, that is, a pointer to the [ABR\_Context](#ga52e8dba39ee979b70826401b3d36574e) instance. The pointer should not be null. Otherwise, an error code indicating failure is returned.

 |
| 

data

 | 

Camera motion data of a game app's each frame, that is, a pointer to [ABR\_CameraData](../../header-files-and-structs/structs/abr-cameradata/document.md). The pointer should not be null. Otherwise, an error code indicating failure is returned.

 |

**Returns**:

Execution result of the function. If the execution is successful, **ABR\_SUCCESS** is returned. If the execution fails, an error code is returned. For details about the error codes, please refer to [ABR\_ErrorCode](#ga86d5860f91dc4f1de6b381cd65389b9d).

#### \[h2\]HMS\_FG\_Activate\_GLES()

[FG\_ErrorCode](#ga68efbf5ff41faeb835f5587654c1e669) HMS\_FG\_Activate\_GLES([FG\_Context\_GLES](#ga62e666292d67fd19fd35ad07463e21cc)\* context)

**Description**

Activates a frame generation context instance. Before the activation, the instance attributes must be set. For an activated frame generation context instance, the [HMS\_FG\_Dispatch\_GLES](#gab135a0f59582d168d461ef115423cfb4) API can be called to generate a predicted frame. This API applies only to the OpenGL ES graphics API.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

context

 | 

Created frame generation context instance, that is, a pointer to the [FG\_Context\_GLES](#ga62e666292d67fd19fd35ad07463e21cc) object. The pointer should not be null.

 |

**Returns**:

Execution result of the function. If the execution is successful, **FG\_SUCCESS** is returned. If the execution fails, an error code is returned. For details about the error codes, please refer to [FG\_ErrorCode](#ga394c554fc5d056d702180ee031ccee2c).

#### \[h2\]HMS\_FG\_Activate\_VK()

[FG\_ErrorCode](#ga68efbf5ff41faeb835f5587654c1e669) HMS\_FG\_Activate\_VK([FG\_Context\_VK](#ga4022ab63c2296d63dcf2c2df178508b7)\* context)

**Description**

Activates a frame generation context instance. Before the activation, the instance attributes must be set. For an activated frame generation context instance, the [HMS\_FG\_Dispatch\_VK](#ga21f86a194e72e99dd54fd39080385a37) API can be called to generate a predicted frame. This API applies only to the Vulkan graphics API.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

context

 | 

Created frame generation context instance, that is, a pointer to the [FG\_Context\_VK](#ga4022ab63c2296d63dcf2c2df178508b7) object. The pointer should not be null.

 |

**Returns**:

Execution result of the function. If the execution is successful, **FG\_SUCCESS** is returned. If the execution fails, an error code is returned. For details about the error codes, please refer to [FG\_ErrorCode](#ga394c554fc5d056d702180ee031ccee2c).

#### \[h2\]HMS\_FG\_CreateContext\_GLES()

[FG\_Context\_GLES](#ga62e666292d67fd19fd35ad07463e21cc)\* HMS\_FG\_CreateContext\_GLES(void )

**Description**

Creates a frame generation context instance. If the call is successful, a pointer to the [FG\_Context\_GLES](#ga62e666292d67fd19fd35ad07463e21cc) object will be returned. This API applies only to the OpenGL ES graphics API.

**Start version**: 5.0.0(12)

**Returns**:

If the call is successful, a pointer to [FG\_Context\_GLES](#ga62e666292d67fd19fd35ad07463e21cc) is returned. If the call fails, a null pointer is returned.

#### \[h2\]HMS\_FG\_CreateContext\_VK()

[FG\_Context\_VK](#ga4022ab63c2296d63dcf2c2df178508b7)\* HMS\_FG\_CreateContext\_VK(const [FG\_ContextDescription\_VK](../../header-files-and-structs/structs/fg-contextdescription-vk/document.md)\* contextDescription)

**Description**

Creates a frame generation context instance. If the call is successful, a pointer to the [FG\_Context\_VK](#ga4022ab63c2296d63dcf2c2df178508b7) object will be returned. This API applies only to the Vulkan graphics API.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

contextDescription

 | 

Pointer to an [FG\_ContextDescription\_VK](../../header-files-and-structs/structs/fg-contextdescription-vk/document.md) object. The pointer should not be null.

 |

**Returns**:

If the call is successful, a pointer to [FG\_Context\_VK](#ga4022ab63c2296d63dcf2c2df178508b7) is returned. If the call fails, a null pointer is returned.

#### \[h2\]HMS\_FG\_CreateImage\_VK()

[FG\_Image\_VK](#gabd6ee9704e997ffc2792ad3c89847019)\* HMS\_FG\_CreateImage\_VK([FG\_Context\_VK](#ga4022ab63c2296d63dcf2c2df178508b7)\* context, VkImage image, VkImageView view )

**Description**

Creates input and output image instances for frame generation. An image instance must be created through this API for the real frame color buffer, depth stencil buffer, and predicted frame buffer, respectively. Then, the created image instances are passed to the [HMS\_FG\_Dispatch\_VK](#ga21f86a194e72e99dd54fd39080385a37) API to generate a predicted frame. This API is used to associate the image resources in a game app with the frame generation algorithm implementation.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

context

 | 

Created frame generation context instance, that is, a pointer to the [FG\_Context\_VK](#ga4022ab63c2296d63dcf2c2df178508b7) object. The pointer should not be null.

 |
| 

image

 | 

**VkImage** object.

 |
| 

view

 | 

**VkImageView** object.

 |

**Returns**:

Input and output image instances for frame generation.

#### \[h2\]HMS\_FG\_Deactivate\_GLES()

[FG\_ErrorCode](#ga68efbf5ff41faeb835f5587654c1e669) HMS\_FG\_Deactivate\_GLES([FG\_Context\_GLES](#ga62e666292d67fd19fd35ad07463e21cc)\* context)

**Description**

Deactivates a frame generation context instance. To activate the instance again, call the [HMS\_FG\_Activate\_GLES](#gaa5f1d5b98694100aa3e3dbb4c99ac23a) API.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

context

 | 

Created frame generation context instance, that is, a pointer to the [FG\_Context\_GLES](#ga62e666292d67fd19fd35ad07463e21cc) object. The pointer should not be null.

 |

**Returns**:

Execution result of the function. If the execution is successful, **FG\_SUCCESS** is returned. If the execution fails, an error code is returned. For details about the error codes, please refer to [FG\_ErrorCode](#ga394c554fc5d056d702180ee031ccee2c).

#### \[h2\]HMS\_FG\_Deactivate\_VK()

[FG\_ErrorCode](#ga68efbf5ff41faeb835f5587654c1e669) HMS\_FG\_Deactivate\_VK([FG\_Context\_VK](#ga4022ab63c2296d63dcf2c2df178508b7)\* context)

**Description**

Deactivates a frame generation context instance. To activate the instance again, call the [HMS\_FG\_Activate\_VK](#ga6871faa08ebf19d380301cf400c086a8) API.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

context

 | 

Created frame generation context instance, that is, a pointer to the [FG\_Context\_VK](#ga4022ab63c2296d63dcf2c2df178508b7) object. The pointer should not be null.

 |

**Returns**:

Execution result of the function. If the execution is successful, **FG\_SUCCESS** is returned. If the execution fails, an error code is returned. For details about the error codes, please refer to [FG\_ErrorCode](#ga394c554fc5d056d702180ee031ccee2c).

#### \[h2\]HMS\_FG\_DestroyContext\_GLES()

[FG\_ErrorCode](#ga68efbf5ff41faeb835f5587654c1e669) HMS\_FG\_DestroyContext\_GLES([FG\_Context\_GLES](#ga62e666292d67fd19fd35ad07463e21cc)\*\* context)

**Description**

Destroys a frame generation context instance and releases memory resources. This API applies only to the OpenGL ES graphics API.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

context

 | 

Level-2 pointer to a created [FG\_Context\_GLES](#ga62e666292d67fd19fd35ad07463e21cc) object. The pointer should not be null.

 |

**Returns**:

Execution result of the function. If the execution is successful, **FG\_SUCCESS** is returned. If the execution fails, an error code is returned. For details about the error codes, please refer to [FG\_ErrorCode](#ga394c554fc5d056d702180ee031ccee2c).

#### \[h2\]HMS\_FG\_DestroyContext\_VK()

[FG\_ErrorCode](#ga68efbf5ff41faeb835f5587654c1e669) HMS\_FG\_DestroyContext\_VK([FG\_Context\_VK](#ga4022ab63c2296d63dcf2c2df178508b7)\*\* context)

**Description**

Destroys a frame generation context instance and releases memory resources. This API applies only to the Vulkan graphics API.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

context

 | 

Level-2 pointer to a created [FG\_Context\_VK](#ga4022ab63c2296d63dcf2c2df178508b7) object. The pointer should not be null.

 |

**Returns**:

Execution result of the function. If the execution is successful, **FG\_SUCCESS** is returned. If the execution fails, an error code is returned. For details about the error codes, please refer to [FG\_ErrorCode](#ga394c554fc5d056d702180ee031ccee2c).

#### \[h2\]HMS\_FG\_DestroyImage\_VK()

[FG\_ErrorCode](#ga68efbf5ff41faeb835f5587654c1e669) HMS\_FG\_DestroyImage\_VK([FG\_Context\_VK](#ga4022ab63c2296d63dcf2c2df178508b7)\* context, [FG\_Image\_VK](#gabd6ee9704e997ffc2792ad3c89847019)\* image )

**Description**

Destroys input and output image instances for frame generation and cancels the corresponding association.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

context

 | 

Created frame generation context instance, that is, a pointer to the [FG\_Context\_VK](#ga4022ab63c2296d63dcf2c2df178508b7) object. The pointer should not be null.

 |
| 

image

 | 

Pointer to an [FG\_Image\_VK](#gabd6ee9704e997ffc2792ad3c89847019) object.

 |

**Returns**:

Execution result of the function. If the execution is successful, **FG\_SUCCESS** is returned. If the execution fails, an error code is returned. For details about the error codes, please refer to [FG\_ErrorCode](#ga394c554fc5d056d702180ee031ccee2c).

#### \[h2\]HMS\_FG\_Dispatch\_GLES()

[FG\_ErrorCode](#ga68efbf5ff41faeb835f5587654c1e669) HMS\_FG\_Dispatch\_GLES([FG\_Context\_GLES](#ga62e666292d67fd19fd35ad07463e21cc)\* context, const [FG\_DispatchDescription\_GLES](../../header-files-and-structs/structs/fg-dispatchdescription-gles/document.md)\* desc )

**Description**

Sets the parameter information required for frame prediction to generate a predicted frame. This API applies only to the OpenGL ES graphics API.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

context

 | 

Created frame generation context instance, that is, a pointer to the [FG\_Context\_GLES](#ga62e666292d67fd19fd35ad07463e21cc) object. The pointer should not be null.

 |
| 

desc

 | 

Pointer to [FG\_DispatchDescription\_GLES](../../header-files-and-structs/structs/fg-dispatchdescription-gles/document.md). The pointer should not be null. The parameter information needs to be updated for each frame.

 |

**Returns**:

Execution result of the function. If the execution is successful, **FG\_SUCCESS** is returned. If the number of input historical frames does not reach the fixed threshold (which is **2** for the basic interpolation mode, enhanced interpolation mode, and enhanced extrapolation mode, and **3** for the basic extrapolation mode), **FG\_COLLECTING\_PREVIOUS\_FRAMES** is returned. If the execution fails, an error code is returned. For details about the error codes, please refer to [FG\_ErrorCode](#ga394c554fc5d056d702180ee031ccee2c).

#### \[h2\]HMS\_FG\_SetExtendedCameraInfo\_GLES()

[FG\_ErrorCode](#ga68efbf5ff41faeb835f5587654c1e669) HMS\_FG\_SetExtendedCameraInfo\_GLES([FG\_Context\_GLES](#ga62e666292d67fd19fd35ad07463e21cc)\* context, const [FG\_PerFrameExtendedCameraInfo](../../header-files-and-structs/structs/fg-perframeextendedcamerainfo/document.md)\* info)

**Description**

Sets the extended camera attribute information. When the translation component of the view projection matrix is very large, this information is provided for more accurate frame generation. This API is optional. This API applies only to the OpenGL ES graphics API.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

context

 | 

Created frame generation context instance, that is, a pointer to the [FG\_Context\_GLES](#ga62e666292d67fd19fd35ad07463e21cc) object. The pointer should not be null.

 |
| 

info

 | 

Pointer to an [FG\_PerFrameExtendedCameraInfo](../../header-files-and-structs/structs/fg-perframeextendedcamerainfo/document.md) object. The pointer should not be null.

 |

**Returns**:

Execution result of the function. If the execution is successful, **FG\_SUCCESS** is returned. If the execution fails, an error code is returned. For details about the error codes, please refer to [FG\_ErrorCode](#ga394c554fc5d056d702180ee031ccee2c).

#### \[h2\]HMS\_FG\_Dispatch\_VK()

[FG\_ErrorCode](#ga68efbf5ff41faeb835f5587654c1e669) HMS\_FG\_Dispatch\_VK([FG\_Context\_VK](#ga4022ab63c2296d63dcf2c2df178508b7)\* context, const [FG\_DispatchDescription\_VK](../../header-files-and-structs/structs/fg-dispatchdescription-vk/document.md)\* desc )

**Description**

Sets the parameter information required for frame prediction to generate a predicted frame. This API applies only to the Vulkan graphics API.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

context

 | 

Created frame generation context instance, that is, a pointer to the [FG\_Context\_VK](#ga4022ab63c2296d63dcf2c2df178508b7) object. The pointer should not be null.

 |
| 

desc

 | 

Pointer to [FG\_DispatchDescription\_VK](../../header-files-and-structs/structs/fg-dispatchdescription-vk/document.md). The pointer should not be null. The parameter information needs to be updated for each frame.

 |

**Returns**:

Execution result of the function. If the execution is successful, **FG\_SUCCESS** is returned. If the number of input historical frames does not reach the fixed threshold (which is **3** for both the interpolation and extrapolation modes), **FG\_COLLECTING\_PREVIOUS\_FRAMES** is returned. If the execution fails, an error code is returned. For details about the error codes, please refer to [FG\_ErrorCode](#ga394c554fc5d056d702180ee031ccee2c).

#### \[h2\]HMS\_FG\_IsActive\_GLES()

[FG\_ErrorCode](#ga68efbf5ff41faeb835f5587654c1e669) HMS\_FG\_IsActive\_GLES([FG\_Context\_GLES](#ga62e666292d67fd19fd35ad07463e21cc)\* context, bool\* isActive )

**Description**

Checks whether a frame generation context instance is activated. This API applies only to the OpenGL ES graphics API.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

context

 | 

Created frame generation context instance, that is, a pointer to the [FG\_Context\_GLES](#ga62e666292d67fd19fd35ad07463e21cc) object. The pointer should not be null.

 |
| 

isActive

 | 

Indicates whether a frame generation context instance is activated.

**true**: yes

**false**: no

 |

**Returns**:

Execution result of the function. If the execution is successful, **FG\_SUCCESS** is returned. If the execution fails, an error code is returned. For details about the error codes, please refer to [FG\_ErrorCode](#ga394c554fc5d056d702180ee031ccee2c).

#### \[h2\]HMS\_FG\_IsActive\_VK()

[FG\_ErrorCode](#ga68efbf5ff41faeb835f5587654c1e669) HMS\_FG\_IsActive\_VK([FG\_Context\_VK](#ga4022ab63c2296d63dcf2c2df178508b7)\* context, bool\* isActive )

**Description**

Checks whether a frame generation context instance is activated. This API applies only to the Vulkan graphics API.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

context

 | 

Created frame generation context instance, that is, a pointer to the [FG\_Context\_VK](#ga4022ab63c2296d63dcf2c2df178508b7) object. The pointer should not be null.

 |
| 

isActive

 | 

Indicates whether a frame generation context instance is activated.

**true**: yes

**false**: no

 |

**Returns**:

Execution result of the function. If the execution is successful, **FG\_SUCCESS** is returned. If the execution fails, an error code is returned. For details about the error codes, please refer to [FG\_ErrorCode](#ga394c554fc5d056d702180ee031ccee2c).

#### \[h2\]HMS\_FG\_SetAlgorithmMode\_GLES()

[FG\_ErrorCode](#ga68efbf5ff41faeb835f5587654c1e669) HMS\_FG\_SetAlgorithmMode\_GLES([FG\_Context\_GLES](#ga62e666292d67fd19fd35ad07463e21cc)\* context, const [FG\_AlgorithmModeInfo](../../header-files-and-structs/structs/fg-algorithmmodeinfo/document.md)\* predictionModeInfo )

**Description**

Sets the frame prediction algorithm mode and motion estimation mode for frame generation. This API is mandatory. This API applies only to the OpenGL ES graphics API.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

context

 | 

Created frame generation context instance, that is, a pointer to the [FG\_Context\_GLES](#ga62e666292d67fd19fd35ad07463e21cc) object. The pointer should not be null.

 |
| 

predictionModeInfo

 | 

Pointer to an [FG\_AlgorithmModeInfo](../../header-files-and-structs/structs/fg-algorithmmodeinfo/document.md) object. The pointer should not be null.

 |

**Returns**:

Execution result of the function. If the execution is successful, **FG\_SUCCESS** is returned. If the execution fails, an error code is returned. For details about the error codes, please refer to [FG\_ErrorCode](#ga394c554fc5d056d702180ee031ccee2c).

#### \[h2\]HMS\_FG\_SetAlgorithmMode\_VK()

[FG\_ErrorCode](#ga68efbf5ff41faeb835f5587654c1e669) HMS\_FG\_SetAlgorithmMode\_VK([FG\_Context\_VK](#ga4022ab63c2296d63dcf2c2df178508b7)\* context, const [FG\_AlgorithmModeInfo](../../header-files-and-structs/structs/fg-algorithmmodeinfo/document.md)\* predictionModeInfo )

**Description**

Sets the frame generation algorithm mode, including the prediction algorithm mode and motion estimation mode. This API is mandatory. This API applies only to the Vulkan graphics API.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

context

 | 

Created frame generation context instance, that is, a pointer to the [FG\_Context\_VK](#ga4022ab63c2296d63dcf2c2df178508b7) object. The pointer should not be null.

 |
| 

predictionModeInfo

 | 

Pointer to an [FG\_AlgorithmModeInfo](../../header-files-and-structs/structs/fg-algorithmmodeinfo/document.md) object. The pointer should not be null.

 |

**Returns**:

Execution result of the function. If the execution is successful, **FG\_SUCCESS** is returned. If the execution fails, an error code is returned. For details about the error codes, please refer to [FG\_ErrorCode](#ga394c554fc5d056d702180ee031ccee2c).

#### \[h2\]HMS\_FG\_SetCvvZSemantic\_GLES()

[FG\_ErrorCode](#ga68efbf5ff41faeb835f5587654c1e669) HMS\_FG\_SetCvvZSemantic\_GLES([FG\_Context\_GLES](#ga62e666292d67fd19fd35ad07463e21cc)\* context, [FG\_CvvZSemantic](#ga530448309918d6d703e28c61a848a267) semantic )

**Description**

Sets the homogeneous clip space Z/W range and depth function. This API is optional. If it is not called, the default value **FG\_CVV\_Z\_SEMANTIC\_MINUS\_ONE\_TO\_ONE\_FORWARD\_Z** will be used. This API applies only to the OpenGL ES graphics API.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

context

 | 

Created frame generation context instance, that is, a pointer to the [FG\_Context\_GLES](#ga62e666292d67fd19fd35ad07463e21cc) object. The pointer should not be null.

 |
| 

semantic

 | 

Enumerated values of the homogeneous clip space Z/W range and depth function.

 |

**Returns**:

Execution result of the function. If the execution is successful, **FG\_SUCCESS** is returned. If the execution fails, an error code is returned. For details about the error codes, please refer to [FG\_ErrorCode](#ga394c554fc5d056d702180ee031ccee2c).

#### \[h2\]HMS\_FG\_SetCvvZSemantic\_VK()

[FG\_ErrorCode](#ga68efbf5ff41faeb835f5587654c1e669) HMS\_FG\_SetCvvZSemantic\_VK([FG\_Context\_VK](#ga4022ab63c2296d63dcf2c2df178508b7)\* context, [FG\_CvvZSemantic](#ga530448309918d6d703e28c61a848a267) semantic )

**Description**

Sets the homogeneous clip space Z/W range and depth function. This API is optional. If it is not called, the default value **FG\_CVV\_Z\_SEMANTIC\_ZERO\_TO\_ONE\_FORWARD\_Z** will be used. This API applies only to the Vulkan graphics API.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

context

 | 

Created frame generation context instance, that is, a pointer to the [FG\_Context\_VK](#ga4022ab63c2296d63dcf2c2df178508b7) object. The pointer should not be null.

 |
| 

semantic

 | 

Enumerated values of the homogeneous clip space Z/W range and depth function.

 |

**Returns**:

Execution result of the function. If the execution is successful, **FG\_SUCCESS** is returned. If the execution fails, an error code is returned. For details about the error codes, please refer to [FG\_ErrorCode](#ga394c554fc5d056d702180ee031ccee2c).

#### \[h2\]HMS\_FG\_SetDepthStencilYDirectionInverted\_GLES()

[FG\_ErrorCode](#ga68efbf5ff41faeb835f5587654c1e669) HMS\_FG\_SetDepthStencilYDirectionInverted\_GLES([FG\_Context\_GLES](#ga62e666292d67fd19fd35ad07463e21cc)\* context, bool inverted )

**Description**

Sets the flag bit for flipping the color buffer around the Y axis relative to the depth stencil buffer. This API is optional. If it is not called, no flipping is performed by default. This API applies only to the OpenGL ES graphics API.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

context

 | 

Created frame generation context instance, that is, a pointer to the [FG\_Context\_GLES](#ga62e666292d67fd19fd35ad07463e21cc) object. The pointer should not be null.

 |
| 

inverted

 | 

Flag bit indicating whether the color buffer is flipped around the Y axis relative to the depth stencil buffer.

**true**: The color buffer is flipped 180 degrees around the Y axis relative to the depth stencil buffer.

**false**: The color buffer is not flipped relative to the depth stencil buffer.

 |

**Returns**:

Execution result of the function. If the execution is successful, **FG\_SUCCESS** is returned. If the execution fails, an error code is returned. For details about the error codes, please refer to [FG\_ErrorCode](#ga394c554fc5d056d702180ee031ccee2c).

#### \[h2\]HMS\_FG\_SetDepthStencilYDirectionInverted\_VK()

[FG\_ErrorCode](#ga68efbf5ff41faeb835f5587654c1e669) HMS\_FG\_SetDepthStencilYDirectionInverted\_VK([FG\_Context\_VK](#ga4022ab63c2296d63dcf2c2df178508b7)\* context, bool inverted )

**Description**

Sets the flag bit for flipping the color buffer around the Y axis relative to the depth stencil buffer. This API is optional. If it is not called, no flipping is performed by default. This API applies only to the Vulkan graphics API. If flipping occurs but **inverted** is not set to **true**, the predicted frame effect may be abnormal.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

context

 | 

Created frame generation context instance, that is, a pointer to the [FG\_Context\_VK](#ga4022ab63c2296d63dcf2c2df178508b7) object. The pointer should not be null.

 |
| 

inverted

 | 

Flag bit indicating whether the color buffer is flipped around the Y axis relative to the depth stencil buffer.

**true**: The color buffer is flipped 180 degrees around the Y axis relative to the depth stencil buffer.

**false**: The color buffer is not flipped relative to the depth stencil buffer.

 |

**Returns**:

Execution result of the function. If the execution is successful, **FG\_SUCCESS** is returned. If the execution fails, an error code is returned. For details about the error codes, please refer to [FG\_ErrorCode](#ga394c554fc5d056d702180ee031ccee2c).

#### \[h2\]HMS\_FG\_SetImageFormat\_GLES()

[FG\_ErrorCode](#ga68efbf5ff41faeb835f5587654c1e669) HMS\_FG\_SetImageFormat\_GLES([FG\_Context\_GLES](#ga62e666292d67fd19fd35ad07463e21cc)\* context, [FG\_ImageFormat\_GLES](#ga3bec27405891e089234bf50d0589c3cd) format )

**Description**

Sets the image format of the real frame color buffer and the predicted frame buffer. This API is optional. If it is not called, the default value **FG\_FORMAT\_R8G8B8A8\_UNORM** will be used. This API applies only to the OpenGL ES graphics API.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

context

 | 

Created frame generation context instance, that is, a pointer to the [FG\_Context\_GLES](#ga62e666292d67fd19fd35ad07463e21cc) object. The pointer should not be null.

 |
| 

format

 | 

Enumerated values of the image formats of the real frame color buffer and the predicted frame buffer.

 |

**Returns**:

Execution result of the function. If the execution is successful, **FG\_SUCCESS** is returned. If the execution fails, an error code is returned. For details about the error codes, please refer to [FG\_ErrorCode](#ga394c554fc5d056d702180ee031ccee2c).

#### \[h2\]HMS\_FG\_SetImageFormat\_VK()

[FG\_ErrorCode](#ga68efbf5ff41faeb835f5587654c1e669) HMS\_FG\_SetImageFormat\_VK([FG\_Context\_VK](#ga4022ab63c2296d63dcf2c2df178508b7)\* context, const [FG\_ImageFormat\_VK](../../header-files-and-structs/structs/fg-imageformat-vk/document.md)\* format )

**Description**

Sets the input and output image formats for frame generation. This API is optional. If it is not called, the default value **VK\_FORMAT\_R8G8B8A8\_UNORM** will be used for the real frame color buffer and predicted frame buffer, and **VK\_FORMAT\_D24\_UNORM\_S8\_UINT** will be used for the depth stencil buffer. This API applies only to the Vulkan graphics API.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

context

 | 

Created frame generation context instance, that is, a pointer to the [FG\_Context\_VK](#ga4022ab63c2296d63dcf2c2df178508b7) object. The pointer should not be null.

 |
| 

format

 | 

Pointer to an [FG\_ImageFormat\_VK](../../header-files-and-structs/structs/fg-imageformat-vk/document.md) object. The pointer should not be null.

 |

**Returns**:

Execution result of the function. If the execution is successful, **FG\_SUCCESS** is returned. If the execution fails, an error code is returned. For details about the error codes, please refer to [FG\_ErrorCode](#ga394c554fc5d056d702180ee031ccee2c).

#### \[h2\]HMS\_FG\_SetResolution\_GLES()

[FG\_ErrorCode](#ga68efbf5ff41faeb835f5587654c1e669) HMS\_FG\_SetResolution\_GLES([FG\_Context\_GLES](#ga62e666292d67fd19fd35ad07463e21cc)\* context, const [FG\_ResolutionInfo](../../header-files-and-structs/structs/fg-resolutioninfo/document.md)\* resolutionInfo )

**Description**

Sets the resolutions of input and output images for frame generation. This API is mandatory. This API applies only to the OpenGL ES graphics API.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

context

 | 

Created frame generation context instance, that is, a pointer to the [FG\_Context\_GLES](#ga62e666292d67fd19fd35ad07463e21cc) object. The pointer should not be null.

 |
| 

resolutionInfo

 | 

Pointer to an [FG\_ResolutionInfo](../../header-files-and-structs/structs/fg-resolutioninfo/document.md) object. The pointer should not be null.

 |

**Returns**:

Execution result of the function. If the execution is successful, **FG\_SUCCESS** is returned. If the execution fails, an error code is returned. For details about the error codes, please refer to [FG\_ErrorCode](#ga394c554fc5d056d702180ee031ccee2c).

#### \[h2\]HMS\_FG\_SetResolution\_VK()

[FG\_ErrorCode](#ga68efbf5ff41faeb835f5587654c1e669) HMS\_FG\_SetResolution\_VK([FG\_Context\_VK](#ga4022ab63c2296d63dcf2c2df178508b7)\* context, const [FG\_ResolutionInfo](../../header-files-and-structs/structs/fg-resolutioninfo/document.md)\* resolutionInfo )

**Description**

Sets the resolutions of input and output images for frame generation. This API is mandatory. This API applies only to the Vulkan graphics API.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

context

 | 

Created frame generation context instance, that is, a pointer to the [FG\_Context\_VK](#ga4022ab63c2296d63dcf2c2df178508b7) object. The pointer should not be null.

 |
| 

resolutionInfo

 | 

Pointer to an [FG\_ResolutionInfo](../../header-files-and-structs/structs/fg-resolutioninfo/document.md) object. The pointer should not be null.

 |

**Returns**:

Execution result of the function. If the execution is successful, **FG\_SUCCESS** is returned. If the execution fails, an error code is returned. For details about the error codes, please refer to [FG\_ErrorCode](#ga394c554fc5d056d702180ee031ccee2c).

#### \[h2\]HMS\_FG\_SetIntegrationMode\_GLES()

[FG\_ErrorCode](#ga68efbf5ff41faeb835f5587654c1e669) HMS\_FG\_SetIntegrationMode\_GLES([FG\_Context\_GLES](#ga62e666292d67fd19fd35ad07463e21cc)\* context, const [FG\_IntegrationInfo](../../header-files-and-structs/structs/fg-integrationinfo/document.md)\* integrationInfo)

**Description**

Sets the integration information for frame generation. This API applies only to the OpenGL ES graphics API.

**Start version**: 5.1.0(18)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

context

 | 

Created frame generation context instance, that is, a pointer to the [FG\_Context\_GLES](#ga62e666292d67fd19fd35ad07463e21cc) object. The pointer should not be null.

 |
| 

integrationInfo

 | 

Pointer to an [FG\_IntegrationInfo](../../header-files-and-structs/structs/fg-integrationinfo/document.md) object. The pointer should not be null.

 |

**Returns**:

Execution result of the function. If the execution is successful, **FG\_SUCCESS** is returned. If the execution fails, an error code is returned. For details about the error codes, please refer to [FG\_ErrorCode](#ga394c554fc5d056d702180ee031ccee2c).

#### \[h2\]HMS\_FG\_SetIntegrationMode\_VK()

[FG\_ErrorCode](#ga68efbf5ff41faeb835f5587654c1e669) HMS\_FG\_SetIntegrationMode\_VK([FG\_Context\_VK](#ga4022ab63c2296d63dcf2c2df178508b7)\* context, const [FG\_IntegrationInfo](../../header-files-and-structs/structs/fg-integrationinfo/document.md)\* integrationInfo)

**Description**

Sets the integration information for frame generation. This API applies only to the Vulkan graphics API.

**Start version**: 5.1.0(18)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

context

 | 

Created frame generation context instance, that is, a pointer to the [FG\_Context\_VK](#ga4022ab63c2296d63dcf2c2df178508b7) object. The pointer should not be null.

 |
| 

integrationInfo

 | 

Pointer to an [FG\_IntegrationInfo](../../header-files-and-structs/structs/fg-integrationinfo/document.md) object. The pointer should not be null.

 |

**Returns**:

Execution result of the function. If the execution is successful, **FG\_SUCCESS** is returned. If the execution fails, an error code is returned. For details about the error codes, please refer to [FG\_ErrorCode](#ga394c554fc5d056d702180ee031ccee2c).

#### \[h2\]HMS\_FG\_SetUiPredictionEnabled\_GLES()

[FG\_ErrorCode](#ga68efbf5ff41faeb835f5587654c1e669) HMS\_FG\_SetUiPredictionEnabled\_GLES([FG\_Context\_GLES](#ga62e666292d67fd19fd35ad07463e21cc)\* context, bool isEnabled)

**Description**

Sets whether to enable the UI prediction function. This function can be enabled only in system display mode. It is invalid in game display mode. This API applies only to the OpenGL ES graphics API.

**Start version**: 5.1.0(18)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

context

 | 

Created frame generation context instance, that is, a pointer to the [FG\_Context\_GLES](#ga62e666292d67fd19fd35ad07463e21cc) object. The pointer should not be null.

 |
| 

isEnabled

 | 

Indicates whether the UI prediction function is enabled.

**true**: yes

**false**: no

 |

**Returns**:

Execution result of the function. If the execution is successful, **FG\_SUCCESS** is returned. If the execution fails, an error code is returned. For details about the error codes, please refer to [FG\_ErrorCode](#ga394c554fc5d056d702180ee031ccee2c).

#### \[h2\]HMS\_FG\_SetUiPredictionEnabled\_VK()

[FG\_ErrorCode](#ga68efbf5ff41faeb835f5587654c1e669) HMS\_FG\_SetUiPredictionEnabled\_VK([FG\_Context\_VK](#ga4022ab63c2296d63dcf2c2df178508b7)\* context, bool isEnabled)

**Description**

Sets whether to enable the UI prediction function. This function can be enabled only in system display mode. It is invalid in game display mode. This API applies only to the Vulkan graphics API.

**Start version**: 5.1.0(18)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

context

 | 

Created frame generation context instance, that is, a pointer to the [FG\_Context\_VK](#ga4022ab63c2296d63dcf2c2df178508b7) object. The pointer should not be null.

 |
| 

isEnabled

 | 

Indicates whether the UI prediction function is enabled.

**true**: yes

**false**: no

 |

**Returns**:

Execution result of the function. If the execution is successful, **FG\_SUCCESS** is returned. If the execution fails, an error code is returned. For details about the error codes, please refer to [FG\_ErrorCode](#ga394c554fc5d056d702180ee031ccee2c).

#### \[h2\]HMS\_FG\_SetTargetFps\_GLES()

[FG\_ErrorCode](#ga68efbf5ff41faeb835f5587654c1e669) HMS\_FG\_SetTargetFps\_GLES([FG\_Context\_GLES](#ga62e666292d67fd19fd35ad07463e21cc)\* context, int targetFps)

**Description**

Sets the target frame rate for frame generation. The setting takes effect only for the system display mode and is invalid for the game display mode. This API takes effect after the game is released for the first time and applies only to the OpenGL ES graphics API.

**Start version**: 5.1.0(18)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

context

 | 

Created frame generation context instance, that is, a pointer to the [FG\_Context\_GLES](#ga62e666292d67fd19fd35ad07463e21cc) object. The pointer should not be null.

 |
| 

targetFps

 | 

Target frame rate for frame generation. The value ranges from 30 to 144.

 |

**Returns**:

Execution result of the function. If the execution is successful, **FG\_SUCCESS** is returned. If the execution fails, an error code is returned. For details about the error codes, please refer to [FG\_ErrorCode](#ga394c554fc5d056d702180ee031ccee2c).

#### \[h2\]HMS\_FG\_SetTargetFps\_VK()

[FG\_ErrorCode](#ga68efbf5ff41faeb835f5587654c1e669) HMS\_FG\_SetTargetFps\_VK([FG\_Context\_VK](#ga4022ab63c2296d63dcf2c2df178508b7)\* context, int targetFps)

**Description**

Sets the target frame rate for frame generation. The setting takes effect only for the system display mode and is invalid for the game display mode. This API takes effect after the game is released for the first time and applies only to the Vulkan graphics API.

**Start version**: 5.1.0(18)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

context

 | 

Created frame generation context instance, that is, a pointer to the [FG\_Context\_VK](#ga4022ab63c2296d63dcf2c2df178508b7) object. The pointer should not be null.

 |
| 

targetFps

 | 

Target frame rate for frame generation. The value ranges from 30 to 144.

 |

**Returns**:

Execution result of the function. If the execution is successful, **FG\_SUCCESS** is returned. If the execution fails, an error code is returned. For details about the error codes, please refer to [FG\_ErrorCode](#ga394c554fc5d056d702180ee031ccee2c).

#### \[h2\]HMS\_OpenGTX\_Activate()

[OpenGTX\_ErrorCode](#ga97deebd9adf3e19947ec5b4615fa1d9c) HMS\_OpenGTX\_Activate([OpenGTX\_Context](#ga3ef8c7447a236d882b625ec8434385ed)\* context)

**Description**

Activates an OpenGTX context instance. Before using an OpenGTX context instance, you need to activate it.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

context

 | 

Created OpenGTX context instance, that is, a pointer to the [OpenGTX\_Context](#ga3ef8c7447a236d882b625ec8434385ed) instance. The pointer should not be null. Otherwise, an error code indicating failure is returned.

 |

**Returns**:

Execution result of the function. If the execution is successful, **OPENGTX\_SUCCESS** is returned. If the execution fails, an error code is returned. For details about the error codes, please refer to [OpenGTX\_ErrorCode](#gaa2c657ed21a175b099bea0ed2491cc34).

#### \[h2\]HMS\_OpenGTX\_CreateContext()

[OpenGTX\_Context](#ga3ef8c7447a236d882b625ec8434385ed)\* HMS\_OpenGTX\_CreateContext([OpenGTX\_DeviceInfoCallback](#ga1d66cec4aa0e01696d878c330f012d7a) deviceInfoCallback)

**Description**

Creates an OpenGTX context instance. Each time this API is successfully called, an [OpenGTX\_Context](#ga3ef8c7447a236d882b625ec8434385ed) object is created and a pointer to the [OpenGTX\_Context](#ga3ef8c7447a236d882b625ec8434385ed) object is returned.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

deviceInfoCallback

 | 

Callback for device temperature information, corresponding to [OpenGTX\_DeviceInfoCallback](#ga1d66cec4aa0e01696d878c330f012d7a).

 |

**Returns**:

If the call is successful, a pointer to [OpenGTX\_Context](#ga3ef8c7447a236d882b625ec8434385ed) is returned. If the call fails, a null pointer is returned.

#### \[h2\]HMS\_OpenGTX\_Deactivate()

[OpenGTX\_ErrorCode](#ga97deebd9adf3e19947ec5b4615fa1d9c) HMS\_OpenGTX\_Deactivate([OpenGTX\_Context](#ga3ef8c7447a236d882b625ec8434385ed)\* context)

**Description**

Deactivates an OpenGTX context instance. To activate the instance again, call the [HMS\_OpenGTX\_Activate](#ga67e6cc5b491539c5e219f9e9ef15abca) API.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

context

 | 

Created OpenGTX context instance, that is, a pointer to the [OpenGTX\_Context](#ga3ef8c7447a236d882b625ec8434385ed) instance. The pointer should not be null. Otherwise, an error code indicating failure is returned.

 |

**Returns**:

Execution result of the function. If the execution is successful, **OPENGTX\_SUCCESS** is returned. If the execution fails, an error code is returned. For details about the error codes, please refer to [OpenGTX\_ErrorCode](#gaa2c657ed21a175b099bea0ed2491cc34).

#### \[h2\]HMS\_OpenGTX\_DestroyContext()

[OpenGTX\_ErrorCode](#ga97deebd9adf3e19947ec5b4615fa1d9c) HMS\_OpenGTX\_DestroyContext([OpenGTX\_Context](#ga3ef8c7447a236d882b625ec8434385ed)\*\* context)

**Description**

Destroys an OpenGTX context instance and releases memory resources.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

context

 | 

Created OpenGTX context instance, that is, a pointer to the [OpenGTX\_Context](#ga3ef8c7447a236d882b625ec8434385ed) instance. The pointer should not be null. Otherwise, an error code indicating failure is returned.

 |

**Returns**:

Execution result of the function. If the execution is successful, **OPENGTX\_SUCCESS** is returned. If the execution fails, an error code is returned. For details about the error codes, please refer to [OpenGTX\_ErrorCode](#gaa2c657ed21a175b099bea0ed2491cc34).

#### \[h2\]HMS\_OpenGTX\_DispatchFrameRenderInfo()

[OpenGTX\_ErrorCode](#ga97deebd9adf3e19947ec5b4615fa1d9c) HMS\_OpenGTX\_DispatchFrameRenderInfo([OpenGTX\_Context](#ga3ef8c7447a236d882b625ec8434385ed)\* context, const [OpenGTX\_FrameRenderInfo](../../header-files-and-structs/structs/opengtx-framerenderinfo/document.md)\* frameRenderInfo )

**Description**

Sets the frame rendering information required for OpenGTX running. The information needs to be updated after each change to a frame.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

context

 | 

Created OpenGTX context instance, that is, a pointer to the [OpenGTX\_Context](#ga3ef8c7447a236d882b625ec8434385ed) instance. The pointer should not be null. Otherwise, an error code indicating failure is returned.

 |
| 

frameRenderInfo

 | 

Frame rendering information struct, that is, a pointer to [OpenGTX\_FrameRenderInfo](../../header-files-and-structs/structs/opengtx-framerenderinfo/document.md). The pointer should not be null. Otherwise, an error code indicating failure is returned.

 |

**Returns**:

Execution result of the function. If the execution is successful, **OPENGTX\_SUCCESS** is returned. If the execution fails, an error code is returned. For details about the error codes, please refer to [OpenGTX\_ErrorCode](#gaa2c657ed21a175b099bea0ed2491cc34).

#### \[h2\]HMS\_OpenGTX\_DispatchGameSceneInfo()

[OpenGTX\_ErrorCode](#ga97deebd9adf3e19947ec5b4615fa1d9c) HMS\_OpenGTX\_DispatchGameSceneInfo([OpenGTX\_Context](#ga3ef8c7447a236d882b625ec8434385ed)\* context, const [OpenGTX\_GameSceneInfo](../../header-files-and-structs/structs/opengtx-gamesceneinfo/document.md)\* gameSceneInfo )

**Description**

Sets the game scene information required for OpenGTX running.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

context

 | 

Created OpenGTX context instance, that is, a pointer to the [OpenGTX\_Context](#ga3ef8c7447a236d882b625ec8434385ed) instance. The pointer should not be null. Otherwise, an error code indicating failure is returned.

 |
| 

gameSceneInfo

 | 

Game scene information, that is, a pointer to [OpenGTX\_GameSceneInfo](../../header-files-and-structs/structs/opengtx-gamesceneinfo/document.md). The pointer should not be null. Otherwise, an error code indicating failure is returned.

 |

**Returns**:

Execution result of the function. If the execution is successful, **OPENGTX\_SUCCESS** is returned. If the execution fails, an error code is returned. For details about the error codes, please refer to [OpenGTX\_ErrorCode](#gaa2c657ed21a175b099bea0ed2491cc34).

#### \[h2\]HMS\_OpenGTX\_DispatchNetworkInfo()

[OpenGTX\_ErrorCode](#ga97deebd9adf3e19947ec5b4615fa1d9c) HMS\_OpenGTX\_DispatchNetworkInfo([OpenGTX\_Context](#ga3ef8c7447a236d882b625ec8434385ed)\* context, const [OpenGTX\_NetworkInfo](../../header-files-and-structs/structs/opengtx-networkinfo/document.md)\* networkInfo )

**Description**

Sets the network latency information required for OpenGTX running.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

context

 | 

Created OpenGTX context instance, that is, a pointer to the [OpenGTX\_Context](#ga3ef8c7447a236d882b625ec8434385ed) instance. The pointer should not be null. Otherwise, an error code indicating failure is returned.

 |
| 

networkInfo

 | 

Network information, that is, a pointer to [OpenGTX\_NetworkInfo](../../header-files-and-structs/structs/opengtx-networkinfo/document.md). The pointer should not be null. Otherwise, an error code indicating failure is returned.

 |

**Returns**:

Execution result of the function. If the execution is successful, **OPENGTX\_SUCCESS** is returned. If the execution fails, an error code is returned. For details about the error codes, please refer to [OpenGTX\_ErrorCode](#gaa2c657ed21a175b099bea0ed2491cc34).

#### \[h2\]HMS\_OpenGTX\_SetConfiguration()

[OpenGTX\_ErrorCode](#ga97deebd9adf3e19947ec5b4615fa1d9c) HMS\_OpenGTX\_SetConfiguration ([OpenGTX\_Context](#ga3ef8c7447a236d882b625ec8434385ed)\* context, const [OpenGTX\_ConfigDescription](../../header-files-and-structs/structs/opengtx-configdescription/document.md)\* config )

**Description**

Initializes an OpenGTX context instance and sets the OpenGTX context instance attributes.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

context

 | 

Created OpenGTX context instance, that is, a pointer to the [OpenGTX\_Context](#ga3ef8c7447a236d882b625ec8434385ed) instance. The pointer should not be null. Otherwise, an error code indicating failure is returned.

 |
| 

config

 | 

Initialization parameters of an OpenGTX context instance, that is, a pointer to [OpenGTX\_ConfigDescription](../../header-files-and-structs/structs/opengtx-configdescription/document.md). The pointer should not be null. Otherwise, an error code indicating failure is returned.

 |

**Returns**:

Execution result of the function. If the execution is successful, **OPENGTX\_SUCCESS** is returned. If the execution fails, an error code is returned. For details about the error codes, please refer to [OpenGTX\_ErrorCode](#gaa2c657ed21a175b099bea0ed2491cc34).
