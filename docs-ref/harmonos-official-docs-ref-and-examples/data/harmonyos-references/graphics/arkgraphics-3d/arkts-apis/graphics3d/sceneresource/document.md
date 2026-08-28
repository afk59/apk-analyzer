# SceneResource

The SceneResource module provides basic resource types in 3D graphics.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/G8JtK644QoqG4EPLn_qESA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062456Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A90693567C0CE9733921E6F20174EAEA91183AD3C29F98F4BE10BF9E95704D56)

-   The initial APIs of this module are supported since API version 12. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { SceneResourceType, SceneResource, Shader, MaterialType, CullMode, Blend, RenderSort, Material,
  MaterialProperty, MetallicRoughnessMaterial, ShaderMaterial, SamplerFilter, SamplerAddressMode, Sampler,
  SubMesh, Morpher, Mesh, MeshResource, Animation, EnvironmentBackgroundType, Environment, Image } from '@kit.ArkGraphics3D';

#### SceneResourceType

Enumerates the scene resource types, which are used to classify resources in a scene.

**System capability**: SystemCapability.ArkUi.Graphics3D

| Name | Value | Description |
| :-- | :-- | :-- |
| UNKNOWN | 0 | Unknown. |
| NODE | 1 | Node resource. |
| ENVIRONMENT | 2 | Environment resource. |
| MATERIAL | 3 | Material type. |
| MESH | 4 | Mesh resource. |
| ANIMATION | 5 | Animation resource. |
| SHADER | 6 | Shader resource. |
| IMAGE | 7 | Image resource. |
| MESH\_RESOURCE18+ | 8 | Mesh resource. |
| EFFECT21+ | 9 | Post-processing effect resource. |

#### SceneResource

Describes a resource in a scene.

#### \[h2\]Properties

**System capability**: SystemCapability.ArkUi.Graphics3D

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| name | string | No | No | Name. There is no special format requirement. |
| resourceType | [SceneResourceType](#sceneresourcetype) | Yes | No | Scene resource type. The default value is undefined. |
| uri | [ResourceStr](../../../../../application-framework/arkui/arkts-components/common-definitions/basic-types/document.md#resourcestr) | Yes | Yes | Resource to load. The default value is undefined. |

#### \[h2\]destroy

destroy(): void

Destroys the scene resource and releases all associated resources or references. Once released, the resource can no longer be used or accessed.

**System capability**: SystemCapability.ArkUi.Graphics3D

**Example**

import { Shader, SceneResourceParameters, SceneResourceFactory, Scene } from '@kit.ArkGraphics3D';

function destroy(): void {
  // Load scene resources, which supports .gltf and .glb formats. The path and file name can be customized based on the specific project resources.
  let scene: Promise<Scene> = Scene.load($rawfile("gltf/CubeWithFloor/glTF/AnimatedCube.glb"));
  scene.then(async (result: Scene) => {
    if (result) {
      let sceneFactory: SceneResourceFactory = result.getResourceFactory();
      // Create shader resources. The path and file name can be customized based on the specific project resources.
      let sceneResourceParameter: SceneResourceParameters = { name: "shaderResource",
        uri: $rawfile("shaders/custom\_shader/custom\_material\_sample.shader") };
      let shader: Promise<Shader> = sceneFactory.createShader(sceneResourceParameter);
      shader.then(async (shaderResult:Shader) => {
         // Release the resource.
         shaderResult.destroy();
      });
    }
  });
}

#### Shader

Shader resource, which inherits from [SceneResource](#sceneresource-1).

**System capability**: SystemCapability.ArkUi.Graphics3D

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| inputs | Record<string, number | [Vec2](../scenetype/document.md#vec2) | [Vec3](../scenetype/document.md#vec3) | [Vec4](../scenetype/document.md#vec4) | Image> | Yes | No | Inputs of the shader. |

#### MaterialType

Enumerates the material types in a scene. The material type defines how materials in a scene are rendered.

**System capability**: SystemCapability.ArkUi.Graphics3D

| Name | Value | Description |
| :-- | :-- | :-- |
| SHADER | 1 | Shader-defined. |
| METALLIC\_ROUGHNESS20+ | 2 | Metallic-Roughness model based on Physically Based Rendering (PBR), simulating realistic material lighting effects through metallicity and roughness parameters. |

#### CullMode20+

Enumerates the culling modes of PBR materials. You can improve rendering performance and visual quality by determining whether the front or back faces of objects are culled.

**System capability**: SystemCapability.ArkUi.Graphics3D

| Name | Value | Description |
| :-- | :-- | :-- |
| NONE | 0 | Culling is disabled. |
| FRONT | 1 | Culls the front faces of geometric objects. |
| BACK | 2 | Culls the back faces of geometric objects. |

#### Blend20+

Controls the transparency of materials.

**System capability**: SystemCapability.ArkUi.Graphics3D

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| enabled | boolean | No | No | Whether the transparency of the material is enabled. **true** if enabled, **false** otherwise. |

#### RenderSort20+

Describes the order in which materials are rendered, controlling the sequence of drawing in the rendering pipeline.

**System capability**: SystemCapability.ArkUi.Graphics3D

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| renderSortLayer | number | No | Yes | Rendering layer ID. A smaller value indicates an earlier rendering order. The value range is \[0, 63\]. The default layer ID is 32. |
| renderSortLayerOrder | number | No | Yes | Rendering order of different objects within the same rendering layer. A smaller value indicates an earlier rendering order. The value range is \[0, 255\]. The default value is **0**. |

#### Material

Material resource, which inherits from [SceneResource](#sceneresource-1).

**System capability**: SystemCapability.ArkUi.Graphics3D

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| materialType | [MaterialType](#materialtype) | Yes | No | Material type. |
| shadowReceiver20+ | boolean | No | Yes | Whether the material receives shadows. **true** if the material receives shadows, **false** otherwise. The default is **false**. |
| cullMode20+ | [CullMode](#cullmode20) | No | Yes | Culling mode of the material, which can be used to determine whether to cull front or back faces. The default value is **BACK**. |
| blend20+ | [Blend](#blend20) | No | Yes | Whether the material is transparent. The default value is **false**. |
| alphaCutoff20+ | number | No | Yes | Threshold of the alpha channel. If the alpha of a pixel is greater than or equal to this threshold, the pixel is rendered; otherwise, the pixel is not rendered. Setting a value less than **1** enables this mode. The value range is \[0, 1\]. The default value is **1**. |
| renderSort20+ | [RenderSort](#rendersort20) | No | Yes | Rendering order, which determines the rendering sequence of materials in the rendering pipeline. The default layer ID is 32, and the default order within the layer is 0. |

#### MaterialProperty20+

Defines the textures, property factors, and texture samplers used by a material.

**System capability**: SystemCapability.ArkUi.Graphics3D

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| image | [Image](#image) | null | No | No | Texture map based on PBR properties to convey the texture information of the material. |
| factor | [Vec4](../scenetype/document.md#vec4) | No | No | PBR property factor, with different meanings for different properties. |
| sampler | [Sampler](#sampler20) | No | Yes | Texture sampler, with the default value set to **LINEAR** for magnification, minification, and mipmaps, and to **REPEAT** for U, V, and W directions. |

#### MetallicRoughnessMaterial20+

Material resource for creating realistic appearances, using the Metallic-Roughness model based on PBR. It simulates the surface lighting and reflection effects of different materials like metal and plastic by adjusting metallicity and roughness parameters. It inherits from [Material](#material).

**System capability**: SystemCapability.ArkUi.Graphics3D

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| baseColor | [MaterialProperty](#materialproperty20) | No | No | Base color map, which is used to represent the material's color in the absence of lighting. |
| normal | [MaterialProperty](#materialproperty20) | No | No | Normal map, which is used to represent the surface structure details of an object to enhance lighting realism without altering the geometric structure. |
| material | [MaterialProperty](#materialproperty20) | No | No | 
Metal material parameters.

**Roughness**: strength of reflection caused by the fine surface structure details of the material.

**Metallic**: metallic properties of the material.

**Reflectance**: reflectivity of the material.

 |
| ambientOcclusion | [MaterialProperty](#materialproperty20) | No | No | Ambient occlusion map, which is used to simulate the occlusion of ambient light in recesses or detailed parts of an object to enhance local shadows and improve detail realism. |
| emissive | [MaterialProperty](#materialproperty20) | No | No | Emissive color, which is the color of the material as a light source. |
| clearCoat | [MaterialProperty](#materialproperty20) | No | No | Clear coat, similar to car paint, carbon fiber, or a wet surface, which requires an additional transparent layer with reflective properties. |
| clearCoatRoughness | [MaterialProperty](#materialproperty20) | No | No | Roughness of the clear coat. |
| clearCoatNormal | [MaterialProperty](#materialproperty20) | No | No | Normal map of the clear coat. |
| sheen | [MaterialProperty](#materialproperty20) | No | No | Gentle, widespread shine of microfiber materials, ideal for representing fabrics and textiles. |
| specular | [MaterialProperty](#materialproperty20) | No | No | Specular reflection of non-metallic materials, showing the intensity of traditional mirror-like reflections. |

#### ShaderMaterial

Shader material, which inherits from [Material](#material).

**System capability**: SystemCapability.ArkUi.Graphics3D

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| colorShader | [Shader](#shader) | No | Yes | Shader. The default value is undefined. |

#### SamplerFilter20+

Enumerates the filtering modes of a sampler. The filtering mode determines the interpolation method used when sampling textures, controlling how final pixel colors are calculated during texture scaling or deformation.

**System capability**: SystemCapability.ArkUi.Graphics3D

| Name | Value | Description |
| :-- | :-- | :-- |
| NEAREST | 0 | Uses nearest-neighbor interpolation, which is fast but can result in jagged edges. |
| LINEAR | 1 | Uses linear interpolation, providing a smoother appearance but with a slight performance cost. |

#### SamplerAddressMode20+

Enumerates the sampler addressing modes, which are used to control how texture coordinates are handled when they go beyond the \[0, 1\] range.

**System capability**: SystemCapability.ArkUi.Graphics3D

| Name | Value | Description |
| :-- | :-- | :-- |
| REPEAT | 0 | The texture repeats when the coordinates exceed the range. |
| MIRRORED\_REPEAT | 1 | The texture mirrors and repeats when the coordinates exceed the range. |
| CLAMP\_TO\_EDGE | 2 | The edge pixels of the texture are stretched when the coordinates exceed the range. |

#### Sampler20+

Describes the sampling modes used during texture sampling.

**System capability**: SystemCapability.ArkUi.Graphics3D

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| magFilter | [SamplerFilter](#samplerfilter20) | No | Yes | Sampling mode when the texture is enlarged. The default value is **LINEAR**. |
| minFilter | [SamplerFilter](#samplerfilter20) | No | Yes | Sampling mode when the texture is reduced. The default value is **LINEAR**. |
| mipMapMode | [SamplerFilter](#samplerfilter20) | No | Yes | Sampling modes between different texture resolutions. The default value is **LINEAR**. |
| addressModeU | [SamplerAddressMode](#sampleraddressmode20) | No | Yes | Sampling mode of the texture in the U (horizontal) direction. The default value is **REPEAT**. |
| addressModeV | [SamplerAddressMode](#sampleraddressmode20) | No | Yes | Sampling mode of the texture in the V (vertical) direction. The default value is **REPEAT**. |

#### SubMesh

Sub-mesh resource.

**System capability**: SystemCapability.ArkUi.Graphics3D

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| name | string | No | No | Name. There is no special format requirement. |
| material | [Material](#material) | No | No | Material. |
| aabb | [Aabb](../scenetype/document.md#aabb) | Yes | No | Axis aligned bounding box. |

#### Morpher20+

Defines the deformation of 3D models by adjusting the weights of different deformation targets to create dynamic effects.

**System capability**: SystemCapability.ArkUi.Graphics3D

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| targets | Record<string, number> | Yes | No | Used to store the names and weights of deformation targets. The weight value is usually within the range of \[0.0, 1.0\]. |

#### Mesh

Mesh resource, which inherits from [SceneResource](#sceneresource-1).

**System capability**: SystemCapability.ArkUi.Graphics3D

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| subMeshes | [SubMesh](#submesh)\[\] | Yes | No | Array of sub-meshes. |
| aabb | [Aabb](../scenetype/document.md#aabb) | Yes | No | Axis aligned bounding box. |
| materialOverride | [Material](#material) | No | Yes | Material. The default value is undefined. |

#### MeshResource18+

Mesh resource, which inherits from [SceneResource](#sceneresource-1).

**System capability**: SystemCapability.ArkUi.Graphics3D

#### Animation

Animation resource, which inherits from [SceneResource](#sceneresource-1).

#### \[h2\]Properties

**System capability**: SystemCapability.ArkUi.Graphics3D

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| enabled | boolean | No | No | Whether the animation is enabled. **true** if enabled, **false** otherwise. |
| speed20+ | number | No | Yes | Playback speed factor of the animation. The default value is **1.0**, indicating that the animation is played at normal speed. If the value is negative, the animation plays in reverse. |
| duration | number | Yes | No | Animation duration, in seconds. The value must be greater than or equal to 0. |
| running | boolean | Yes | No | Whether the animation is running. **true** if running, **false** otherwise. |
| progress | number | Yes | No | Playing progress of the animation. The value range is \[0, 1\]. |

#### \[h2\]onFinished

onFinished(callback: Callback<void>): void

Called when the animation playback is complete or the **finish** API is called.

**System capability**: SystemCapability.ArkUi.Graphics3D

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | Callback<void> | Yes | Callback function. The return value is null. |

**Example**

import { Animation, Scene } from '@kit.ArkGraphics3D';

function onFinished(): void {
  // Load scene resources, which supports .gltf and .glb formats. The path and file name can be customized based on the specific project resources.
  let scene: Promise<Scene> = Scene.load($rawfile("gltf/CubeWithFloor/glTF/AnimatedCube.glb"));
  scene.then(async (result: Scene) => {
    if (result && result.animations && result.animations\[0\]) {
      let anim: Animation = result.animations\[0\];
      // Register a callback.
      anim.onFinished(()=>{
        console.info("onFinished");
      });
    }
  });
}

#### \[h2\]onStarted

onStarted(callback: Callback<void>): void

Called when the animation starts to play. The start operation is triggered by calling **start** or **restart**.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | Callback<void> | Yes | Callback function. The return value is null. |

**System capability**: SystemCapability.ArkUi.Graphics3D

**Example**

import { Animation, Scene } from '@kit.ArkGraphics3D';

function onStarted(): void {
  // Load scene resources, which supports .gltf and .glb formats. The path and file name can be customized based on the specific project resources.
  let scene: Promise<Scene> = Scene.load($rawfile("gltf/CubeWithFloor/glTF/AnimatedCube.glb"));
  scene.then(async (result: Scene) => {
    if (result && result.animations && result.animations\[0\]) {
      let anim: Animation = result.animations\[0\];
      // Register a callback.
      anim.onStarted(()=>{
        console.info("onStarted");
      });
    }
  });
}

#### \[h2\]pause

pause(): void

Pauses the animation. The animation remains in the current playing progress.

**System capability**: SystemCapability.ArkUi.Graphics3D

**Example**

import { Animation, Scene } from '@kit.ArkGraphics3D';

function pause(): void {
  // Load scene resources, which supports .gltf and .glb formats. The path and file name can be customized based on the specific project resources.
  let scene: Promise<Scene> = Scene.load($rawfile("gltf/CubeWithFloor/glTF/AnimatedCube.glb"));
  scene.then(async (result: Scene) => {
    if (result && result.animations && result.animations\[0\]) {
      let anim: Animation = result.animations\[0\];
      // Pause the animation.
      anim.pause();
    }
  });
}

#### \[h2\]restart

restart(): void

Plays the animation from the beginning.

**System capability**: SystemCapability.ArkUi.Graphics3D

**Example**

import { Animation, Scene } from '@kit.ArkGraphics3D';

function restart(): void {
  // Load scene resources, which supports .gltf and .glb formats. The path and file name can be customized based on the specific project resources.
  let scene: Promise<Scene> = Scene.load($rawfile("gltf/CubeWithFloor/glTF/AnimatedCube.glb"));
  scene.then(async (result: Scene) => {
    if (result && result.animations && result.animations\[0\]) {
      let anim: Animation = result.animations\[0\];
      // Restart the animation.
      anim.restart();
    }
  });
}

#### \[h2\]seek

seek(position: number): void

Plays the animation from the specified position.

**System capability**: SystemCapability.ArkUi.Graphics3D

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| position | number | Yes | Position from which the animation playback starts. The value range is \[0, 1\]. |

**Example**

import { Animation, Scene } from '@kit.ArkGraphics3D';

function seek(): void {
  // Load scene resources, which supports .gltf and .glb formats. The path and file name can be customized based on the specific project resources.
  let scene: Promise<Scene> = Scene.load($rawfile("gltf/CubeWithFloor/glTF/AnimatedCube.glb"));
  scene.then(async (result: Scene) => {
    if (result && result.animations && result.animations\[0\]) {
      let anim: Animation = result.animations\[0\];
      // Set the animation playback progress to 10%.
      anim.seek(0.1);
    }
  });
}

#### \[h2\]start

start(): void

Plays the animation based on the current progress.

**System capability**: SystemCapability.ArkUi.Graphics3D

**Example**

import { Animation, Scene } from '@kit.ArkGraphics3D';

function start(): void {
  // Load scene resources, which supports .gltf and .glb formats. The path and file name can be customized based on the specific project resources.
  let scene: Promise<Scene> = Scene.load($rawfile("gltf/CubeWithFloor/glTF/AnimatedCube.glb"));
  scene.then(async (result: Scene) => {
    if (result && result.animations && result.animations\[0\]) {
      let anim: Animation = result.animations\[0\];
      // Start the animation.
      anim.start();
    }
  });
}

#### \[h2\]stop

stop(): void

Stops playing the animation and sets its progress to **0** (not started).

**System capability**: SystemCapability.ArkUi.Graphics3D

**Example**

import { Animation, Scene } from '@kit.ArkGraphics3D';

function stop(): void {
  // Load scene resources, which supports .gltf and .glb formats. The path and file name can be customized based on the specific project resources.
  let scene: Promise<Scene> = Scene.load($rawfile("gltf/CubeWithFloor/glTF/AnimatedCube.glb"));
  scene.then(async (result: Scene) => {
    if (result && result.animations && result.animations\[0\]) {
      let anim: Animation = result.animations\[0\];
      // Stop playing the animation and set its progress to 0 (not started).
      anim.stop();
    }
  });
}

#### \[h2\]finish

finish(): void

Finishes the playing of the animation and sets its progress of **1** (finished).

**System capability**: SystemCapability.ArkUi.Graphics3D

**Example**

import { Animation, Scene } from '@kit.ArkGraphics3D';

function finish(): void {
  // Load scene resources, which supports .gltf and .glb formats. The path and file name can be customized based on the specific project resources.
  let scene: Promise<Scene> = Scene.load($rawfile("gltf/CubeWithFloor/glTF/AnimatedCube.glb"));
  scene.then(async (result: Scene) => {
    if (result && result.animations && result.animations\[0\]) {
      let anim: Animation = result.animations\[0\];
      // Finish the playing of the animation and set its progress of \*\*1\*\* (finished).
      anim.finish();
    }
  });
}

#### EnvironmentBackgroundType

Enumerates the environment background types, which are used to define how the background of a scene is presented.

**System capability**: SystemCapability.ArkUi.Graphics3D

| Name | Value | Description |
| :-- | :-- | :-- |
| BACKGROUND\_NONE | 0 | No background. |
| BACKGROUND\_IMAGE | 1 | Image background. |
| BACKGROUND\_CUBEMAP | 2 | Cubemap background. |
| BACKGROUND\_EQUIRECTANGULAR | 3 | Equirectangular projection background. |

#### Environment

Environment resource, which inherits from [SceneResource](#sceneresource-1).

**System capability**: SystemCapability.ArkUi.Graphics3D

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| backgroundType | [EnvironmentBackgroundType](#environmentbackgroundtype) | No | No | Environment background type. |
| indirectDiffuseFactor | [Vec4](../scenetype/document.md#vec4) | No | No | Indirect diffuse factor. |
| indirectSpecularFactor | [Vec4](../scenetype/document.md#vec4) | No | No | Indirect specular factor. |
| environmentMapFactor | [Vec4](../scenetype/document.md#vec4) | No | No | Environment map factor. |
| environmentImage | [Image](#image) | null | No | Yes | Environment image. The default value is undefined. |
| radianceImage | [Image](#image) | null | No | Yes | Radiance image. The default value is undefined. |
| irradianceCoefficients | [Vec3](../scenetype/document.md#vec3)\[\] | No | Yes | Irradiance coefficients. The default value is undefined. |

#### Image

Image resource, which inherits from [SceneResource](#sceneresource-1).

**System capability**: SystemCapability.ArkUi.Graphics3D

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| width | number | Yes | No | Image width, in px. The value must be greater than 0. |
| height | number | Yes | No | Image height, in px. The value must be greater than 0. |

#### Effect21+

Effect resource, which inherits from [SceneResource](#sceneresource-1).

**System capability**: SystemCapability.ArkUi.Graphics3D

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| enabled | boolean | No | No | Enabled status of the effect. **true** if enabled, **false** otherwise. |
| effectId | string | Yes | No | Effect ID, which is in the format of 'XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX', for example, **'e68a7f45-2d21-4a0d-9aef-7d9c825d3f12'**. It is used to create an effect. |
