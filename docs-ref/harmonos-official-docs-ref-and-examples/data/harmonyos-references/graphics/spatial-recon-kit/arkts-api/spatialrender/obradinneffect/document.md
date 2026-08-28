# ObraDinnEffect

The **ObraDinnEffect** API encapsulates effect parameters for the bit style, so you can customize the style.

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

noiseStrength

 | 

number

 | 

No

 | 

No

 | 

Noise level used to specify pixels used for [color dithering](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/spatial-recon-glossary#section1745314193505). Color dithering helps smooth edges. Increasing the noise level results in more blurred edges. The value range is \[0, 1\]. The default value is **0.3**.

 |
| 

threshold

 | 

number

 | 

No

 | 

No

 | 

Threshold for classifying pixels into foreground or background color. Pixels with values greater than the threshold are processed as foreground color. A lower **threshold** shifts the overall image toward the foreground color, while a higher **threshold** shifts it toward the background color. The value range is \[0, 1\]. The default value is **0.4**.

 |
| 

foregroundColor

 | 

[Color](../../../../arkgraphics-3d/arkts-apis/graphics3d/scenetype/document.md#color)

 | 

No

 | 

No

 | 

Foreground color.

 |
| 

backgroundColor

 | 

[Color](../../../../arkgraphics-3d/arkts-apis/graphics3d/scenetype/document.md#color)

 | 

No

 | 

No

 | 

Background color.

 |

**Example:**

import { Scene, RenderContext, RenderingPipelineType } from '@kit.ArkGraphics3D';
import { spatialRender } from '@kit.SpatialReconKit';
let renderContext: RenderContext | null = Scene.getDefaultRenderContext();

if (renderContext != null) {
  renderContext.loadPlugin(spatialRender.GSPlugin.PLUGIN\_ID);
  Scene.load().then(async (scene: Scene) => {
    let rf = scene.getResourceFactory();
    let effect : spatialRender.ObraDinnEffect =
      await rf.createEffect({ effectId: spatialRender.GSPlugin.OBRA\_DINN\_EFFECT\_ID }) as spatialRender.ObraDinnEffect;
    let camera = await rf.createCamera({ name: "gsCam", path: "//gsCam" }, { renderingPipeline: RenderingPipelineType.FORWARD });
    camera.effects.append(effect)
  });
}
