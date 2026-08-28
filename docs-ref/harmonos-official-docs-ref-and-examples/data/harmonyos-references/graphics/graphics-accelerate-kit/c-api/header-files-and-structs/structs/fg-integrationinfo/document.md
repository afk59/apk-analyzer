# FG\_IntegrationInfo

#### Overview

Describes the integration information about frame generation, including the display mode, whether to separately buffer depth and color textures, and whether to flip the color texture. It takes effect only when [FG\_PredictionMode](../../../modules/graphicsaccelerate/document.md#gaea2169cd5ae4bf9e8a17dc58f33e8766) is set to **FG\_PREDICTION\_MODE\_INTERPOLATION**.

**Start version**: 5.1.0(18)

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

[FG\_PresentMode](../../../modules/graphicsaccelerate/document.md#section11881356193212) [presentMode](#section423381092419)

 | 

Display mode of predicted frames. When it is set to **FG\_PRESENT\_BY\_SYSTEM**, the value takes effect only when [FG\_PredictionMode](../../../modules/graphicsaccelerate/document.md#ga79e55783a2a38873fc6890c297885275) is set to **FG\_PREDICTION\_MODE\_INTERPOLATION**.

 |
| 

bool [textureCachedByGame](#section0704957113217)

 | 

Indicates whether the game separately buffers the depth texture and color texture for frame generation. If the textures are already buffered, the algorithm will use them directly, without creating additional copies. When it is set to **True**, the value takes effect only when [FG\_PredictionMode](../../../modules/graphicsaccelerate/document.md#ga79e55783a2a38873fc6890c297885275) is set to **FG\_PREDICTION\_MODE\_INTERPOLATION**.

The value is **true** or **false**.

 |
| 

bool [needFlipInputColor](#section035114548349)

 | 

Indicates whether the input color texture needs to be flipped. If flipping is required, the algorithm maps the Y-axis coordinates to read the color texture. When it is set to **True**, the value takes effect only when [FG\_PredictionMode](../../../modules/graphicsaccelerate/document.md#ga79e55783a2a38873fc6890c297885275) is set to **FG\_PREDICTION\_MODE\_INTERPOLATION**.

The value is **true** or **false**.

 |
| 

bool [needFlipOutputColor](#section2628111719383)

 | 

Indicates whether a predicted frame needs to be flipped. If flipping is required, the algorithm maps the Y-axis coordinates to produce a flipped output. When it is set to **True**, the value takes effect only when [FG\_PredictionMode](../../../modules/graphicsaccelerate/document.md#ga79e55783a2a38873fc6890c297885275) is set to **FG\_PREDICTION\_MODE\_INTERPOLATION**.

The value is **true** or **false**.

 |

#### Member Variable Description

#### \[h2\]presentMode

[FG\_PresentMode](../../../modules/graphicsaccelerate/document.md#section131101213459) FG\_IntegrationInfo::presentMode

**Description**

Display mode.

#### \[h2\]textureCachedByGame

bool FG\_IntegrationInfo::textureCachedByGame

**Description**

Indicates whether the game separately buffers the depth texture and color texture for frame generation. If the textures are already buffered, the algorithm will use them directly, without creating additional copies. When it is set to **True**, the value takes effect only when [FG\_PredictionMode](../../../modules/graphicsaccelerate/document.md#gaea2169cd5ae4bf9e8a17dc58f33e8766) is set to **FG\_PREDICTION\_MODE\_INTERPOLATION**.

#### \[h2\]needFlipInputColor

bool FG\_IntegrationInfo::needFlipInputColor

**Description**

Indicates whether the input color texture needs to be flipped. If flipping is required, the algorithm maps the Y-axis coordinates to read the color texture. When it is set to **True**, the value takes effect only when [FG\_PredictionMode](../../../modules/graphicsaccelerate/document.md#gaea2169cd5ae4bf9e8a17dc58f33e8766) is set to **FG\_PREDICTION\_MODE\_INTERPOLATION**.

#### \[h2\]needFlipOutputColor

bool FG\_IntegrationInfo::needFlipOutputColor

**Description**

Indicates whether a predicted frame needs to be flipped. If flipping is required, the algorithm maps the Y-axis coordinates to produce a flipped output. When it is set to **True**, the value takes effect only when [FG\_PredictionMode](../../../modules/graphicsaccelerate/document.md#gaea2169cd5ae4bf9e8a17dc58f33e8766) is set to **FG\_PREDICTION\_MODE\_INTERPOLATION**.
