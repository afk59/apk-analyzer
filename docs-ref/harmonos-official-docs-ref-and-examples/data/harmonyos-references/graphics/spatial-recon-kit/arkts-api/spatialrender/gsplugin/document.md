# GSPlugin

The **GSPlugin** class encapsulates 3DGS-related content, including the 3DGS plug-in ID and 3DGS model loading API, helping you implement custom functionality for 3DGS models.

**System capability**: SystemCapability.Graphics.SpatialRender

**Start version**: 6.0.1(21)

#### Modules to Import

import { spatialRender } from '@kit.SpatialReconKit';

#### Precautions

Before calling a GSPlugin API, you must load the corresponding plugin ID. Otherwise, undefined behavior may occur.

import { spatialRender } from '@kit.SpatialReconKit';
import { Scene } from '@kit.ArkGraphics3D';

let renderContext = Scene.getDefaultRenderContext();
if (renderContext != null) {
  renderContext.loadPlugin(spatialRender.GSPlugin.PLUGIN\_ID);
}

#### Constants

**System capability**: SystemCapability.Graphics.SpatialRender

**Start version**: 6.0.1(21)

| 
Name

 | 

Type

 | 

Description

 |
| :-- | :-- | :-- |
| 

PLUGIN\_ID

 | 

string

 | 

Plugin ID of the class.

 |
| 

RETRO\_EFFECT\_ID

 | 

string

 | 

ID of the retro effect.

 |
| 

COMIC\_EFFECT\_ID

 | 

string

 | 

ID of the comic effect.

 |
| 

OBRA\_DINN\_EFFECT\_ID

 | 

string

 | 

ID of the black-and-white (bit) effect.

 |
| 

COLOR\_EDITING\_EFFECT\_ID

 | 

string

 | 

ID of the color editing effect.

 |

You do not need to be aware of the specific value of each ID. You are advised to use the corresponding string variable directly.

#### loadGSNode

Loads a 3DGS model.

**System capability**: SystemCapability.Graphics.SpatialRender

**Start version**: 6.0.1(21)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

scene

 | 

[Scene](../../../../arkgraphics-3d/arkts-apis/graphics3d/scene/document.md)

 | 

Yes

 | 

Basic module of ArkGraphics 3D, which specifies the scene to be displayed on the app UI. You are advised to call [Scene.load](../../../../arkgraphics-3d/arkts-apis/graphics3d/scene/document.md#load) to obtain the value.

 |
| 

params

 | 

[GSImportSettings](../gsimportsettings/document.md)

 | 

Yes

 | 

Settings for loading a 3DGS model.

 |
| 

parent

 | 

[Node](../../../../arkgraphics-3d/arkts-apis/graphics3d/scenenode/document.md#node)

 | 

No

 | 

Node where the 3DGS model is expected to be mounted. If this parameter is not specified, the loaded 3DGS model will be mounted to the root node of **Scene**.

 |

**Returns:**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[GSNode](../gsnode-3dgs-rendering-object/document.md)\>

 | 

Promise used to obtain the [GSNode](../gsnode-3dgs-rendering-object/document.md) corresponding to the 3DGS model.

 |

**Example:**

import { Scene, RenderContext } from '@kit.ArkGraphics3D';
import { spatialRender } from '@kit.SpatialReconKit';

let renderContext: RenderContext | null = Scene.getDefaultRenderContext();

if (renderContext != null) {
  renderContext.loadPlugin(spatialRender.GSPlugin.PLUGIN\_ID);
  let scene = Scene.load().then(async (scene: Scene) => {
    let uri = "OhosRawFile://assets/gltf/model.glb"; // URI of the 3DGS model. Modify as needed.
    let offset = 0;
    let gsNodeext: spatialRender.GSNode = await spatialRender.GSPlugin.loadGSNode(scene, {uri, offset}, scene.root);
  });
}
