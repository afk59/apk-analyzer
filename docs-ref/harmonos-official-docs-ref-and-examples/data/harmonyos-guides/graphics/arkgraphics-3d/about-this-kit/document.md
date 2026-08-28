# About This Kit

ArkGraphics 3D provides basic 3D scene rendering capabilities based on the lightweight 3D engine and render pipelines. With this service, you can efficiently build and render a 3D scene.

ArkGraphics 3D takes the custom scene mode as its core capability, allowing you to independently construct and manage nodes such as Scene, Camera, and Light, thereby achieving full control over the rendering effects and interactive behaviors of the 3D scene. Meanwhile, to facilitate the quick preview and display of models, it also provides an automatic scene mode, which allows you to directly load glTF models (.gltf and .glb files), with the framework automatically creating basic cameras, light sources, and interactive controls.

#### Function Description

-   Loads and parses standard GL Transmission Format (glTF) models (both .gltf and .glb files). You can place a glTF model file in an application sandbox and use the asynchronous APIs provided by ArkGraphics 3D to load the model and render the scene. For details, see [Scene](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-scene). For details about glTF, see [glTF-Specification](https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html).
-   Provides APIs for customizing light nodes, camera nodes, and common nodes. You can customize scene lights and rendering angles. In addition, users can dynamically adjust the scene tree structure and node properties to adjust a 3D scene. For details, see [Scene](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-scene) and [SceneNode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-scene-nodes).
-   Provides APIs for creating images, materials, environments, and shaders used in a 3D scene. You can also customize a shader to carry out custom 3D material rendering. For details, see [Scene](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-scene) and [SceneResource](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-scene-resources).
-   Provides APIs for controlling the animation status in a 3D scene, such as starting, pausing, and finishing an animation, and playing an animation from a specified position. Callback functions are also provided so that you can perform logic control when an animation starts or ends. For details, see [SceneResource](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-scene-resources).
-   Provides APIs for you to carry out post-processing, for example, tone mapping. For details, see [ScenePostProcessSettings](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-scene-post-process-settings).

To sum up, ArkGraphics 3D provides 3D scene rendering capabilities centered on custom scene nodes, while offering a convenient entry for the quick display of models through the automatic scene mode. This satisfies diverse development requirements ranging from simple preview to complex rendering control.

For details about the API usage and parameters, see [@ohos.graphics.scene (ArkGraphics 3D)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-scene).

#### Working Principles

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/i-PLUKoESZWGSpUY7-9M7Q/en-us_image_0000002537925208.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062050Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B01F4208982A4B9CD62C0C83C4CDC6A540488F7459091BFE413E549C52CABDC1)

The ArkGraphics 3D service consists of three key parts: graphics backend, engine layer, and interface layer.

-   Graphics backend: driver interfaces provided by GPU hardware, including OpenGL ES and Vulkan. The engine layer calls these interfaces by delivering GPU instructions to implement scene rendering.
-   Engine layer: provides the rendering capability based on the rendering engine component of the Ark Graphics Platform (AGP), which features ease of use, high image quality, and scalability. The engine uses the Entity Component System (ECS) architecture design and modular encapsulation (such as material definition and post-processing), providing a development suite that is easy to use.
-   Interface layer: processes data based on the ECS framework through the NAPI layer, and exposes 3D rendering interfaces.

#### Constraints

To use the ArkGraphics 3D service, the device must support the GPU driver of OpenGL ES 3.2 or later or Vulkan 1.0 or later.
