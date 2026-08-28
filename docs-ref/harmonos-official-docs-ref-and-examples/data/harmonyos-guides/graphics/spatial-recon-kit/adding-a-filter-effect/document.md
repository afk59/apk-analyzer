# Adding a Filter Effect

Adds different filter effects to the rendered image of the 3DGS model.

#### API Description

The following lists only some key APIs called in the demo. For details about all APIs, please refer to the [API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/spatial-recon-arkts).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

RETRO\_EFFECT\_ID

 | 

ID of the retro effect.

 |
| 

COMIC\_EFFECT\_ID

 | 

ID of the comic effect.

 |
| 

OBRA\_DINN\_EFFECT\_ID

 | 

ID of the black-and-white (bit) effect.

 |
| 

COLOR\_EDITING\_EFFECT\_ID

 | 

ID of the color editing effect.

 |

#### Development Procedure

1.  In the project root directory, open **/src/main/ets/entryability/EntryAbility.ets** and import the spatial modeling module.
    
    import { Scene, RenderContext } from '@kit.ArkGraphics3D';
    import { spatialRender } from '@kit.SpatialReconKit';
    import { RenderingPipelineType } from '@ohos.graphics.scene'
    
2.  Load the context of the current scene.
    
    let renderContext: RenderContext | null = Scene.getDefaultRenderContext();
    
3.  Call the filter API.
    
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
