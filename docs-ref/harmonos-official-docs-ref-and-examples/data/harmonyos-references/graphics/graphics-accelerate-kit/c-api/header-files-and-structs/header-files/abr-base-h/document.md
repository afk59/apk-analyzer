# abr\_base.h

#### Overview

Declares ABR APIs used for different graphics APIs.

**Library**: libabr.so

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

struct [ABR\_Vector3](../../structs/abr-vector3/document.md)

 | 

Describes an ABR 3D vector.

 |
| 

struct [ABR\_CameraData](../../structs/abr-cameradata/document.md)

 | 

Describes the camera motion data of a game app's each frame. The ABR capability adaptively adjusts the buffer resolution factor according to the camera motion data.

 |

#### \[h2\]Type Definitions

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

typedef struct [ABR\_Context](../../../modules/graphicsaccelerate/document.md#ga52e8dba39ee979b70826401b3d36574e) [ABR\_Context](../../../modules/graphicsaccelerate/document.md#ga52e8dba39ee979b70826401b3d36574e)

 | 

Describes the ABR context.

 |
| 

typedef enum [ABR\_RenderAPI\_Type](../../../modules/graphicsaccelerate/document.md#ga9359d16ecefa21f0e6e5f29732cbf6f4) [ABR\_RenderAPI\_Type](../../../modules/graphicsaccelerate/document.md#ga3a6ead3a3c0f19a6434e97fda13f42f2)

 | 

Describes the graphics API types supported by the ABR capability.

 |
| 

typedef struct [ABR\_Vector3](../../structs/abr-vector3/document.md) [ABR\_Vector3](../../../modules/graphicsaccelerate/document.md#ga71a845f23f7ec4c0935db8e9f00ab8b9)

 | 

Describes an ABR 3D vector.

 |
| 

typedef struct [ABR\_CameraData](../../structs/abr-cameradata/document.md) [ABR\_CameraData](../../../modules/graphicsaccelerate/document.md#gada21a47272d5db8e28e2a9bb4fd033d4)

 | 

Describes the camera motion data of a game app's each frame. The ABR capability adaptively adjusts the buffer resolution factor according to the camera motion data.

 |
| 

typedef enum [ABR\_ErrorCode](../../../modules/graphicsaccelerate/document.md#ga72df702d70a8326b5b46c118be6ad1d7) [ABR\_ErrorCode](../../../modules/graphicsaccelerate/document.md#ga86d5860f91dc4f1de6b381cd65389b9d)

 | 

Describes the error codes of ABR API calls.

 |

#### \[h2\]Enumerations

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

[ABR\_RenderAPI\_Type](../../../modules/graphicsaccelerate/document.md#ga9359d16ecefa21f0e6e5f29732cbf6f4) {

RENDER\_API\_GLES = 0

}

 | 

Describes the graphics API types supported by the ABR capability.

 |
| 

[ABR\_ErrorCode](../../../modules/graphicsaccelerate/document.md#ga72df702d70a8326b5b46c118be6ad1d7) {

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

#### \[h2\]Functions

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

[ABR\_Context](../../../modules/graphicsaccelerate/document.md#ga52e8dba39ee979b70826401b3d36574e)\* [HMS\_ABR\_CreateContext](../../../modules/graphicsaccelerate/document.md#ga8f785903a5382ff31baef78a3968f66a)([ABR\_RenderAPI\_Type](../../../modules/graphicsaccelerate/document.md#ga9359d16ecefa21f0e6e5f29732cbf6f4) type)

 | 

Creates an ABR context instance. Each time this API is successfully called, an [ABR\_Context](../../../modules/graphicsaccelerate/document.md#ga52e8dba39ee979b70826401b3d36574e) object is created and a pointer to the [ABR\_Context](../../../modules/graphicsaccelerate/document.md#ga52e8dba39ee979b70826401b3d36574e) object is returned.

 |
| 

[ABR\_ErrorCode](../../../modules/graphicsaccelerate/document.md#ga72df702d70a8326b5b46c118be6ad1d7) [HMS\_ABR\_SetTargetFps](../../../modules/graphicsaccelerate/document.md#ga6c613e02088d559b9dc1450fde15bc2a)([ABR\_Context](../../../modules/graphicsaccelerate/document.md#ga52e8dba39ee979b70826401b3d36574e)\* context, const uint32\_t targetFps)

 | 

Sets the target frame rate of an ABR context instance.

 |
| 

[ABR\_ErrorCode](../../../modules/graphicsaccelerate/document.md#ga72df702d70a8326b5b46c118be6ad1d7) [HMS\_ABR\_SetScaleRange](../../../modules/graphicsaccelerate/document.md#ga1001c6a7739d8ce57bf851986f121bf5)([ABR\_Context](../../../modules/graphicsaccelerate/document.md#ga52e8dba39ee979b70826401b3d36574e)\* context, const float minValue, const float maxValue)

 | 

Sets the buffer resolution factor range of an ABR context instance.

 |
| 

[ABR\_ErrorCode](../../../modules/graphicsaccelerate/document.md#ga72df702d70a8326b5b46c118be6ad1d7) [HMS\_ABR\_Activate](../../../modules/graphicsaccelerate/document.md#ga463d8d5396bfd5f6ed800ddab616479a)([ABR\_Context](../../../modules/graphicsaccelerate/document.md#ga52e8dba39ee979b70826401b3d36574e)\* context)

 | 

Activates an ABR context instance. Before the activation, the [HMS\_ABR\_SetTargetFps](../../../modules/graphicsaccelerate/document.md#ga6c613e02088d559b9dc1450fde15bc2a) and [HMS\_ABR\_SetScaleRange](../../../modules/graphicsaccelerate/document.md#ga1001c6a7739d8ce57bf851986f121bf5) APIs must be called to set instance attributes.

 |
| 

[ABR\_ErrorCode](../../../modules/graphicsaccelerate/document.md#ga72df702d70a8326b5b46c118be6ad1d7) [HMS\_ABR\_IsActive](../../../modules/graphicsaccelerate/document.md#ga791519fde19801e6da60094cf077b00f)([ABR\_Context](../../../modules/graphicsaccelerate/document.md#ga52e8dba39ee979b70826401b3d36574e)\* context, bool\* isActive)

 | 

Checks whether an ABR context instance is activated.

 |
| 

[ABR\_ErrorCode](../../../modules/graphicsaccelerate/document.md#ga72df702d70a8326b5b46c118be6ad1d7) [HMS\_ABR\_Deactivate](../../../modules/graphicsaccelerate/document.md#ga4abb4b37392e77c15fbedfa8ceba3da4)([ABR\_Context](../../../modules/graphicsaccelerate/document.md#ga52e8dba39ee979b70826401b3d36574e)\* context)

 | 

Deactivates an ABR context instance. To activate the instance again, call the [HMS\_ABR\_Activate](../../../modules/graphicsaccelerate/document.md#ga463d8d5396bfd5f6ed800ddab616479a) API.

 |
| 

[ABR\_ErrorCode](../../../modules/graphicsaccelerate/document.md#ga72df702d70a8326b5b46c118be6ad1d7) [HMS\_ABR\_UpdateCameraData](../../../modules/graphicsaccelerate/document.md#ga5b895e36d31e46f71d04aba78c8f3716)([ABR\_Context](../../../modules/graphicsaccelerate/document.md#ga52e8dba39ee979b70826401b3d36574e)\* context, [ABR\_CameraData](../../structs/abr-cameradata/document.md)\* data)

 | 

Updates the camera motion data of each frame. Before the update, the [HMS\_ABR\_Activate](../../../modules/graphicsaccelerate/document.md#ga463d8d5396bfd5f6ed800ddab616479a) API must be called to activate the ABR context instance.

 |
| 

[ABR\_ErrorCode](../../../modules/graphicsaccelerate/document.md#ga72df702d70a8326b5b46c118be6ad1d7) [HMS\_ABR\_GetScale](../../../modules/graphicsaccelerate/document.md#ga936129328fea3a5f77b2aae4935f67c6)([ABR\_Context](../../../modules/graphicsaccelerate/document.md#ga52e8dba39ee979b70826401b3d36574e)\* context, float\* scale)

 | 

Obtains the buffer resolution factor for adaptive resolution adjustment.

 |
| 

[ABR\_ErrorCode](../../../modules/graphicsaccelerate/document.md#ga72df702d70a8326b5b46c118be6ad1d7) [HMS\_ABR\_GetNextScale](../../../modules/graphicsaccelerate/document.md#section157311245143415)([ABR\_Context](../../../modules/graphicsaccelerate/document.md#ga52e8dba39ee979b70826401b3d36574e)\* context, float\* scale)

 | 

Obtains the ABR buffer resolution factor of the next frame.

 |
| 

[ABR\_ErrorCode](../../../modules/graphicsaccelerate/document.md#ga72df702d70a8326b5b46c118be6ad1d7) [HMS\_ABR\_DestroyContext](../../../modules/graphicsaccelerate/document.md#gaf3c03179b9bcf1b8475230cbbb0d877c)([ABR\_Context](../../../modules/graphicsaccelerate/document.md#ga52e8dba39ee979b70826401b3d36574e)\*\* context)

 | 

Destroys an ABR context instance and releases memory resources.

 |
