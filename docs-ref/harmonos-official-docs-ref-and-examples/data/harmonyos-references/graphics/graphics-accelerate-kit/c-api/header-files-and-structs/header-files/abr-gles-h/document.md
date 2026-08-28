# abr\_gles.h

#### Overview

Declares ABR APIs used for the OpenGL ES graphics API.

**Library**: libabr.so

**System capability**: SystemCapability.GraphicsGame.RenderAccelerate

**Start version**: 5.0.0(12)

**Related module**: [GraphicsAccelerate](../../../modules/graphicsaccelerate/document.md)

#### Summary

#### \[h2\]Functions

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

[ABR\_ErrorCode](../../../modules/graphicsaccelerate/document.md#ga72df702d70a8326b5b46c118be6ad1d7) [HMS\_ABR\_MarkFrameBuffer\_GLES](../../../modules/graphicsaccelerate/document.md#ga821fb33620312d3adba51d30254c1ef0)([ABR\_Context](../../../modules/graphicsaccelerate/document.md#ga52e8dba39ee979b70826401b3d36574e)\* context)

 | 

Marks a GLES buffer for adaptive rendering. This API must be called before the rendering is started.

 |
| 

[ABR\_ErrorCode](../../../modules/graphicsaccelerate/document.md#ga72df702d70a8326b5b46c118be6ad1d7) [HMS\_ABR\_GetScaledTexture\_GLES](../../../modules/graphicsaccelerate/document.md#section791920394423)([ABR\_Context](../../../modules/graphicsaccelerate/document.md#ga52e8dba39ee979b70826401b3d36574e)\* context, uint32\_t originTexture, uint32\_t\* scaledTexture)

 | 

Obtains the GLES texture after ABR rendering based on the original GLES texture.

 |
