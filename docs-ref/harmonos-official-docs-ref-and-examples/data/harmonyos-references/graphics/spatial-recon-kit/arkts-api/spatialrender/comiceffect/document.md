# ComicEffect

The **ComicEffect** API encapsulates effect parameters for the comic style, so you can customize the style.

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

lineThreshold

 | 

number

 | 

No

 | 

No

 | 

Threshold for determining whether a pixel belongs to a contour line. Pixels with the image gradient greater than the threshold are considered as part of contour lines. The value range is \[0, 1\]. The default value is **0.2**.

 |
| 

lineColor

 | 

[Color](../../../../arkgraphics-3d/arkts-apis/graphics3d/scenetype/document.md#color)

 | 

No

 | 

No

 | 

Color of a contour line.

 |

**Example:**

import { Scene, RenderContext, RenderingPipelineType } from '@kit.ArkGraphics3D';
import { spatialRender } from '@kit.SpatialReconKit';
let renderContext: RenderContext | null = Scene.getDefaultRenderContext();

if (renderContext != null) {
  renderContext.loadPlugin(spatialRender.GSPlugin.PLUGIN\_ID);
  Scene.load().then(async (scene: Scene) => {
    let rf = scene.getResourceFactory();
    let effect : spatialRender.ComicEffect =
      await rf.createEffect({ effectId: spatialRender.GSPlugin.COMIC\_EFFECT\_ID }) as spatialRender.ComicEffect;
    let camera = await rf.createCamera({ name: "gsCam", path: "//gsCam" }, { renderingPipeline: RenderingPipelineType.FORWARD });
    camera.effects.append(effect)
  });
}
