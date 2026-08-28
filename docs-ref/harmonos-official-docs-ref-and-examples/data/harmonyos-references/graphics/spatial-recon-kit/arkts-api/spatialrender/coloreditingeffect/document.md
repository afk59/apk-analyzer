# ColorEditingEffect

The **ColorEditingEffect** API encapsulates parameters for color editing effects, so you can customize the image style.

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

exposure

 | 

number

 | 

No

 | 

No

 | 

Image exposure. The recommended value range is \[–5, 5\]. The default value is **0.0**.

 |
| 

contrast

 | 

number

 | 

No

 | 

No

 | 

Image contrast. The recommended value range is \[0, 2\]. The default value is **1.0**.

 |
| 

temperature

 | 

number

 | 

No

 | 

No

 | 

Image color temperature. The recommended value range is \[–2, 2\]. The default value is **0.0**.

 |
| 

tint

 | 

number

 | 

No

 | 

No

 | 

Image hue. The recommended value range is \[–1, 1\]. The default value is **0.0**.

 |
| 

saturation

 | 

number

 | 

No

 | 

No

 | 

Image saturation. The recommended value range is \[0, 2\]. The default value is **1.0**.

 |
| 

vibrance

 | 

number

 | 

No

 | 

No

 | 

Image natural saturation. The recommended value range is \[-1, 1\]. The default value is **0.0**.

 |

**Example:**

import { Scene, RenderContext, RenderingPipelineType } from '@kit.ArkGraphics3D';
import { spatialRender } from '@kit.SpatialReconKit';
let renderContext: RenderContext | null = Scene.getDefaultRenderContext();

if (renderContext != null) {
  renderContext.loadPlugin(spatialRender.GSPlugin.PLUGIN\_ID);
  Scene.load().then(async (scene: Scene) => {
    let rf = scene.getResourceFactory();
    let effect : spatialRender.ColorEditingEffect =
      await rf.createEffect({ effectId: spatialRender.GSPlugin.COLOR\_EDITING\_EFFECT\_ID }) as spatialRender.ColorEditingEffect;
    let camera = await rf.createCamera({ name: "gsCam", path: "//gsCam" }, { renderingPipeline: RenderingPipelineType.FORWARD });
    camera.effects.append(effect)
  });
}
