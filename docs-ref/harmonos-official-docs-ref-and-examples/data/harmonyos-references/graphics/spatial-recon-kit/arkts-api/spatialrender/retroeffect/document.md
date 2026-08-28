# RetroEffect

The **RetroEffect** API encapsulates effect parameters for the retro style, for you to customize the style.

**System capability**: SystemCapability.Graphics.SpatialRender

**Start version**: 6.0.1(21)

#### Modules to Import

import { spatialRender } from '@kit.SpatialReconKit';

#### Attributes

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

colorNum

 | 

number

 | 

No

 | 

No

 | 

Number of colors used for [color dithering](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/spatial-recon-glossary#section1745314193505). Generally, a larger value indicates higher image quality, while a smaller value indicates a stronger retro effect. The value must be greater than 0. The default value is **8**.

 |
| 

pixelSize

 | 

number

 | 

No

 | 

No

 | 

Degree of downsampling. A larger value indicates heavier downsampling. If the value is **1**, downsampling is not performed. The value must be greater than or equal to 1. The default value is **4**.

 |
| 

blendEnabled

 | 

boolean

 | 

No

 | 

No

 | 

Indicates whether to blend the processed image with the original image. The options are **true** (yes) and **false** (no). The retro style may reduce brightness and cause color shifts. Setting this parameter to **true** helps preserve the brightness and color of the image. The default value is **true**.

 |
| 

curve

 | 

number

 | 

No

 | 

No

 | 

Curvature of the CRT TV screen. The retro style simulates the display features of a CRT TV.

A larger value of **curve** indicates a larger curvature. The value range is \[0, 1\]. The default value is **0.25**.

 |

**Example:**

import { Scene, RenderContext, RenderingPipelineType } from '@kit.ArkGraphics3D';
import { spatialRender } from '@kit.SpatialReconKit';
let renderContext: RenderContext | null = Scene.getDefaultRenderContext();

if (renderContext != null) {
  renderContext.loadPlugin(spatialRender.GSPlugin.PLUGIN\_ID);
  Scene.load().then(async (scene: Scene) => {
    let rf = scene.getResourceFactory();
    let effect : spatialRender.RetroEffect =
      await rf.createEffect({ effectId: spatialRender.GSPlugin.RETRO\_EFFECT\_ID }) as spatialRender.RetroEffect;
    let camera = await rf.createCamera({ name: "gsCam", path: "//gsCam" }, { renderingPipeline: RenderingPipelineType.FORWARD });
    camera.effects.append(effect)
  });
}
