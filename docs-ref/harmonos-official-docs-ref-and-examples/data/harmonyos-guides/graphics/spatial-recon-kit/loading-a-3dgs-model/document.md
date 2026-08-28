# Loading a 3DGS Model

#### Use Case

A 3DGS module can be in MP4, PLY, or GLB format.

The following figure shows an example.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/J072nNKXRlyYR0i6ZRZPKQ/en-us_image_0000002485417565.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062053Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=119F915B55A36DA79DEF7DB26C7773C939534C474565C764D9C0204DAA4C63E7 "Click to enlarge")

#### API Description

The following lists only some key APIs called in the demo. For details about all APIs, please refer to the [API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/spatial-recon-arkts).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

static loadGSNode(scene: [Scene](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-scene), params: [GSImportSettings](https://developer.huawei.com/consumer/en/doc/harmonyos-references/spatial-recon-gsimport), parent?: [Node](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-scene-nodes#node)): Promise<GSNode>

 | 

Loads a 3DGS model.

 |

#### Development Procedure

1.  In the **entry** directory, open **/src/main/ets/entryability/EntryAbility.ets** and import the spatial modeling module.
    
    import { spatialRender } from '@kit.SpatialReconKit';
    import { Scene, RenderContext } from '@kit.ArkGraphics3D'
    
2.  Load the context of the current scene.
    
    let renderContext: RenderContext | null = Scene.getDefaultRenderContext();
    
3.  Call the API for loading a 3DGS model.
    
    if (renderContext != null) {
      renderContext.loadPlugin(spatialRender.GSPlugin.PLUGIN\_ID);
      let scene = Scene.load().then(async (scene: Scene) => {
        let uri = "OhosRawFile://assets/gltf/model.glb"; // URI of the 3DGS model. Modify as needed.
        let offset = 0;
        let gsNodeext: spatialRender.GSNode = await spatialRender.GSPlugin.loadGSNode(scene, {uri, offset}, scene.root);
      });
    }
