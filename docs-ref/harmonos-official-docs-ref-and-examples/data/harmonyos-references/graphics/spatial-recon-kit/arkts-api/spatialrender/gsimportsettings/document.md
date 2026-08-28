# GSImportSettings

The **GSImportSettings** class encapsulates the settings for loading a 3DGS model, including the model path and data offset in the file, helping you load 3DGS models.

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

uri

 | 

string

 | 

No

 | 

No

 | 

Sandbox path of the 3DGS model.

 |
| 

offset

 | 

number

 | 

No

 | 

Yes

 | 

Offset of the data to be loaded in the 3DGS model file. The default value is **0**.

 |

**Example:**

import { Scene, RenderContext } from '@kit.ArkGraphics3D';
import { spatialRender } from '@kit.SpatialReconKit';

let renderContext: RenderContext | null = Scene.getDefaultRenderContext();

if (renderContext != null) {
  renderContext.loadPlugin(spatialRender.GSPlugin.PLUGIN\_ID);
  let scene = Scene.load().then(async (scene: Scene) => {
    let uri = "OhosRawFile://assets/gltf/doll.glb";
    let offset = 0;
    let setting: spatialRender.GSImportSettings = { uri: uri, offset : offset};
    let gsNodeext: spatialRender.GSNode = await spatialRender.GSPlugin.loadGSNode(scene, setting, scene.root);
  });
}
