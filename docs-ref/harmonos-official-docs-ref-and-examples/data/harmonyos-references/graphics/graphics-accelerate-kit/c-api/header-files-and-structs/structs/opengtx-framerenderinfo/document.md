# OpenGTX\_FrameRenderInfo

#### Overview

Describes the frame rendering information. This struct is passed by a game app after obtaining the frame attributes.

**Start version**: 5.0.0(12)

**Related module**: [GraphicsAccelerate](../../../modules/graphicsaccelerate/document.md)

#### Summary

#### \[h2\]Member Variables

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

[OpenGTX\_Vector3](../opengtx-vector3/document.md) [mainCameraPosition](#aa3ca65cc999276260b31db3a4a5ec477)

 | 

Position of the main camera. The value range for **x**, **y**, and **z** is \[-360, 360\].

 |
| 

[OpenGTX\_Vector3](../opengtx-vector3/document.md) [mainCameraRotate](#a089fb1579868141b741bcd6ee06b8f0b)

 | 

Rotation of the main camera, including yaw, pitch, and roll. The value range for **x**, **y**, and **z** is \[-360, 360\].

 |

#### Member Variable Description

#### \[h2\]mainCameraPosition

[OpenGTX\_Vector3](../opengtx-vector3/document.md) OpenGTX\_FrameRenderInfo::mainCameraPosition

**Description**

Position of the main camera.

#### \[h2\]mainCameraRotate

[OpenGTX\_Vector3](../opengtx-vector3/document.md) OpenGTX\_FrameRenderInfo::mainCameraRotate

**Description**

Rotation of the main camera, including yaw, pitch, and roll. The value range for **x**, **y**, and **z** is \[-360, 360\].
