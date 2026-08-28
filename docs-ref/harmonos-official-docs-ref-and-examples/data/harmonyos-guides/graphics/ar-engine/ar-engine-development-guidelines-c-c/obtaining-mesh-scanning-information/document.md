# Obtaining Mesh Scanning Information

#### Overview

AR Engine supports this capability since version 5.1.0(18).

This section describes how to obtain mesh scanning data of a target object, and provides instructions on how to detect freeform surfaces (including planes) in an environment and process this surface information in apps.

**Figure 1** Environmental mesh scanning  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/cTiPH6qJSfiVkFrrsPPeRg/en-us_image_0000002532306159.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062047Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9AE99E2E0AF8A79386D6139FDDFDCA5702357BBE9D3C951B0C84E31B55B02C3A)

AR Engine capabilities involved in this section:

-   Motion tracking
-   Environment tracking (plane detection)
-   Hit testing

#### API Description

The following lists APIs used for AR mesh scanning. For details about these APIs, please refer to [AR Engine API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[HMS\_AREngine\_ARSession\_Create](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#ga47713cb18234569e03b5216b6c8442d3)

 | 

Creates an [AREngine\_ARSession](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#ga2dbf3585f50628750ec855501c043650) session.

 |
| 

[HMS\_AREngine\_ARSession\_Update](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#ga1d1cacf372a8011a439f0e4e76994259)

 | 

Updates the computation result of AR Engine.

 |
| 

[HMS\_AREngine\_ARSession\_Configure](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#ga6394ae995148abbe3d00082817bf320a)

 | 

Configures an [AREngine\_ARSession](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#ga2dbf3585f50628750ec855501c043650) session.

 |
| 

[HMS\_AREngine\_ARFrame\_Create](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#gadfcb9589137a39c5afcb217e18853a9d)

 | 

Creates an [AREngine\_ARFrame](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#gaf35f728a1179ef54a3eba9f1cf021719) object and stores the pointer in _\*_**outFrame**.

 |
| 

[HMS\_AREngine\_ARSession\_SetDisplayGeometry](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#ga3f23bf747def8303c3fb261a9e9a2286)

 | 

Sets the display height and width (in pixels). Ensure that the height and width you set here are consistent with those of the display view. A mismatch will result in a camera preview failure.

 |
| 

[HMS\_AREngine\_ARSession\_SetCameraGLTexture](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#gac697e4be36db63ed6098f154aa9ac01c)

 | 

Sets the OpenGL texture for storing the camera preview stream data.

 |
| 

[HMS\_AREngine\_ARSession\_GetAllTrackables](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#gac5b39338f95317671d8de6d4f409cf9c)

 | 

Obtains the list of all trackable objects of the specified type.

 |
| 

[HMS\_AREngine\_ARTrackableList\_AcquireItem](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#gab1782eeeeddc01b77a140af915cb351c)

 | 

Obtains the object at a specified index from the trackable object list.

 |
| 

[HMS\_AREngine\_ARPlane\_GetCenterPose](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#gabbb03027afb984be8542d00d2eebd063)

 | 

Obtains the pose information for the conversion from the plane's local coordinate system to the world coordinate system.

 |
| 

[HMS\_AREngine\_ARFrame\_AcquireCamera](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#ga5295c975a0ff3d633a1dde5a8eb70863)

 | 

Obtains the camera parameter object of the current frame.

 |
| 

[HMS\_AREngine\_ARPose\_Create](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#gafb471f39563ca1a4947d4f87c77e24e2)

 | 

Allocates and initializes a new pose object.

 |
| 

[HMS\_AREngine\_ARCamera\_GetPose](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#ga00df108c4ba187967a10e9c4d2e27d3a)

 | 

Obtains the pose of the current camera object in the AR world space.

 |
| 

[HMS\_AREngine\_ARFrame\_AcquireSceneMesh](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#section25711548111020)

 | 

Obtains the mesh information of the current frame.

 |
| 

[HMS\_AREngine\_ARSceneMesh\_AcquireVerticesSize](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#section1860218429179)

 | 

Obtains the number of vertices of a mesh.

 |
| 

[HMS\_AREngine\_ARSceneMesh\_AcquireVertexList](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#section2126723166)

 | 

Obtains the mesh vertex set.

 |
| 

[HMS\_AREngine\_ARSceneMesh\_AcquireIndexListSize](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#section12621161917152)

 | 

Obtains the number of indexes of the mesh faces.

 |
| 

[HMS\_AREngine\_ARSceneMesh\_AcquireIndexList](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#section7629354145)

 | 

Obtains the index set of mesh faces.

 |
| 

[HMS\_AREngine\_ARSceneMesh\_Release](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#section446832931813)

 | 

Releases the mesh information of the current frame.

 |

#### Development Procedure

This section provides only the key development steps. Click [here](https://gitcode.com/harmonyos_samples/arengine_-sample-code_-clientdemo_cpp) to access the complete demo code.

## Declaring Native APIs

For details, please refer to [Declaring Native APIs](../placing-ar-objects/document.md#section1557014318265) in **Placing AR Objects**.

## Creating a UI

Create a UI, use [XComponent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-xcomponent) to display the camera preview image, and periodically trigger the drawing of each frame.

// Refer to the sample code ARSample/entry/src/main/ets/pages/ARMesh.ets.
import { deviceInfo } from '@kit.BasicServicesKit';
import { resourceManager } from '@kit.LocalizationKit';
import arEngineDemo from 'libentry.so';

@Builder
export function ARMeshBuilder() {
  ARMesh();
}

@Component
struct ARMesh {
  pageInfo: NavPathStack = new NavPathStack();
  private interval: number = -1;
  private xComponentId: string = 'ARMesh';
  @State context: Context = this.getUIContext().getHostContext() as Context;
  private resMgr: resourceManager.ResourceManager = this.context.resourceManager;
  @State rotation: number = deviceInfo.deviceType === 'tablet' ? 3 : 0;

  build(): void {
    NavDestination() {
      RelativeContainer() {
        XComponent({ id: this.xComponentId, type: XComponentType.SURFACE, libraryname: 'entry' })
          .width('100%')
          .height('100%')
          .alignRules({
            center: { anchor: '\_\_container\_\_', align: VerticalAlign.Center },
            middle: { anchor: '\_\_container\_\_', align: HorizontalAlign.Center }
          })
          .onLoad(() => {
            console.info(\`XComponent onLoad ${this.xComponentId}.\`);
            this.interval = setInterval(() => {
              // Call the update Native API to update the calculation result of each frame by AR Engine.
              arEngineDemo.update(this.xComponentId);
            }, 33) // Set the frame rate to 30 fps (refreshing a frame every 33 ms).
          })
          .onDestroy(() => {
            console.info(\`XComponent onDestroy ${this.xComponentId}.\`);
            clearInterval(this.interval);
          })
      }
    }
    .onAppear(() => {
      arEngineDemo.init(this.resMgr);
      let config: Int32Array = new Int32Array(\[1, this.rotation\]);
      arEngineDemo.start(this.xComponentId, config);
    })
    .onWillDisappear(() => {
      arEngineDemo.stop(this.xComponentId);
    })
    .onShown(() => {
      arEngineDemo.show(this.xComponentId);
    })
    .onHidden(() => {
      arEngineDemo.hide(this.xComponentId);
    })
    .onReady((context: NavDestinationContext) => {
      this.pageInfo = context.pathStack;
    })
    .hideTitleBar(true)
    .hideBackButton(true)
    .hideToolBar(true)
  }
}

## Importing AR Engine

For details, please refer to [Importing AR Engine](../placing-ar-objects/document.md#section183721115521) in **Placing AR Objects**.

## Creating an AR Session

Create an AR session and enable mesh mode.

AREngine\_ARSession \*arSession = nullptr;
// Create an AR session.
HMS\_AREngine\_ARSession\_Create(nullptr, nullptr, &arSession);
AREngine\_ARConfig \*arConfig = nullptr;
// Create an AR session configurator.
HMS\_AREngine\_ARConfig\_Create(arSession, &arConfig);
// Enable mesh mode.
HMS\_AREngine\_ARConfig\_SetMeshMode(arSession, arConfig, ARENGINE\_MESH\_MODE\_ENABLED);
// Set the configurator for the AR session.
HMS\_AREngine\_ARSession\_Configure(arSession, arConfig);

## Obtaining the Mesh Information of Current Environment

Call [HMS\_AREngine\_ARFrame\_AcquireSceneMesh](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#section25711548111020) to obtain mesh information from the current environment. The result is stored in **sceneMesh**.

AREngine\_ARFrame \*arFrame = nullptr;
// Create an AR single-frame object.
HMS\_AREngine\_ARFrame\_Create(arSession, &arFrame);
AREngine\_ARSceneMesh \*sceneMesh = nullptr;
// Obtain the mesh information of the current frame.
HMS\_AREngine\_ARFrame\_AcquireSceneMesh(arSession, arFrame, &sceneMesh);

## Obtaining the Mesh Vertex Information for the Current Mesh

1\. Call [HMS\_AREngine\_ARSceneMesh\_AcquireVerticesSize](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#section1860218429179) to obtain the number of floating-point values contained in the mesh vertex data. Each mesh vertex consists of three floating-point values. The result is stored in **meshVerticesSize**.

int32\_t meshVerticesSize = 0;
// Obtain the number of floating-point values in the mesh vertex data.
HMS\_AREngine\_ARSceneMesh\_AcquireVerticesSize(arSession, sceneMesh, &meshVerticesSize);

2\. Call [HMS\_AREngine\_ARSceneMesh\_AcquireVertexList](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#section2126723166) to obtain the mesh vertex information. The result is stored in **meshVertices**.

float \*meshVertices = new float\[meshVerticesSize\];
// Obtain the mesh vertex information.
HMS\_AREngine\_ARSceneMesh\_AcquireVertexList(arSession, sceneMesh, meshVertices, meshVerticesSize);
// Obtain the number of vertices of a mesh.
int32\_t mPointsNum = meshVerticesSize / 3;

## Obtaining the Mesh Face Information for the Current Mesh

1\. Call [HMS\_AREngine\_ARSceneMesh\_AcquireIndexListSize](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#section12621161917152) to obtain the number of vertex indices corresponding to the mesh face information. Each set of three vertex indices represents one mesh face. The result is stored in **triangleIndicesSize**.

int32\_t triangleIndicesSize = 0;
// Obtain the number of vertex indices corresponding to the mesh face information.
HMS\_AREngine\_ARSceneMesh\_AcquireIndexListSize(arSession, sceneMesh, &triangleIndicesSize);

2\. Call [HMS\_AREngine\_ARSceneMesh\_AcquireIndexList](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#section7629354145) to obtain the list of vertex indices corresponding to the mesh face information. The result is stored in **meshTriangleIndices**.

int32\_t \*meshTriangleIndices = new int32\_t\[triangleIndicesSize\];
// Obtain the list of vertex indices corresponding to the mesh face information.
HMS\_AREngine\_ARSceneMesh\_AcquireIndexList(arSession, sceneMesh, meshTriangleIndices, triangleIndicesSize);
// Obtain the number of mesh faces.
int32\_t mTrianglesNum = triangleIndicesSize / 3;

## Destroying Mesh Information when Finished

void HMS\_AREngine\_ARSceneMesh\_Release(AREngine\_ARSceneMesh \*sceneMesh);
