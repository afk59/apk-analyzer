# Obtaining Mesh Scanning Information

#### Overview

AR Engine supports this capability since version 5.1.0(18).

This section describes how to obtain mesh scanning data of a target object, and provides instructions on how to detect freeform surfaces in an environment and process this surface information in apps.

**Figure 1** Environmental mesh scanning  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/g4C6VZA1TziUN-_-lKTy8w/en-us_image_0000002532306163.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062046Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D514A2D06AB4118E12C83E5DC6A11EF3C1B8E80797AC4E206307BA7F50937E28)

AR Engine capabilities involved in this section:

-   Motion tracking
-   Environment tracking (plane detection)
-   Hit testing

#### API Description

Mesh scanning mainly depends on [ARSceneMesh](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arengine#section81184417712). The following table lists the APIs related to mesh scanning. For details about these APIs, please refer to [AR Engine API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-arkts-api).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[ARSceneMesh.getVertices](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arengine#section15211205153115)

 | 

Obtains vertex coordinate data in a scene mesh.

 |
| 

[ARSceneMesh.getVertexNormals](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arengine#section4793111183211)

 | 

Obtains the vertex normal coordinate data in a scene mesh.

 |
| 

[ARSceneMesh.getTriangleIndices](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arengine#section19221187183218)

 | 

Obtains the triangle index data in a scene mesh.

 |
| 

[ARSceneMesh.release](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arengine#section625851110329)

 | 

Releases the environment mesh data object.

 |
| 

[ARFrame.hitTest](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arengine#section20353182861218)

 | 

Obtains the pixel coordinates (**pixelX** and **pixelY**) in the preview area based on the light projected by the camera to determine the ray direction, and then checks whether the ray has an intersection on the plane or point cloud.

 |
| 

[ARHitResult.getHitPose](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arengine#section1864219177109)

 | 

Obtains the pose of the intersection point.

 |
| 

[ARHitResult.getTrackable](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arengine#section727122311104)

 | 

Obtains the trackable object that is hit.

 |
| 

[ARHitResult.createAnchor](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arengine#section12541329171017)

 | 

Creates an anchor at the intersection.

 |
| 

[ARHitResult.release](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arengine#section1690193413100)

 | 

Releases the memory occupied by the hit testing result object.

 |
| 

[ARPose.getMatrix](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arengine#section5278038164917)

 | 

Converts the pose data into a 4 × 4 matrix.

 |
| 

[ARPose.release](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arengine#section22831038104913)

 | 

Releases the memory occupied by the pose object.

 |

#### Development Procedure

This section provides only the key development steps. Click [here](https://gitcode.com/HarmonyOS_Samples/arengine_samplecode_clientdemo_arkts) to access the complete demo code.

The AR Engine only outputs data for detected planes. To enhance observation, you can use either the Ark Graphics Platform (AGP) rendering engine or [XComponent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-xcomponent) to draw the identified planes. For details about AGP, please refer to the [introduction to ArkGraphics 3D](../../../arkgraphics-3d/about-this-kit/document.md) and [AGP Engine](https://gitcode.com/openharmony/graphic_graphic_3d).

For any AR app built with ArkTS, it is first necessary to create an AR session [ARViewContext](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arviewcontroller#section12681656121519), to manage the system status of the AR Engine. For details about how to create an [ARViewContext](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arviewcontroller#section12681656121519) for an AR session, please refer to [Managing AR Sessions](../managing-ar-sessions/document.md).

## Modules to Import

The modules required for mesh scanning capabilities are as follows.

import { arEngine, ARView, arViewController } from '@kit.AREngine';
import { Node, Scene, Vec3 } from '@kit.ArkGraphics3D';
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

## Defining Variables

Define the variables **hitAnchorList** to store anchor point data for placed objects, **hitPoseList** to store pose information for placed objects, and **statusBarHeight** for the device's status bar height.

The user's click coordinates on the device differ from those in the preview stream. Since the preview stream window is slightly smaller than the device screen, subtracting the status bar height is necessary to obtain the accurate click coordinates.

let frame: arEngine.ARFrame;
let hitAnchorList: arEngine.ARAnchor\[\] = \[\];
let hitPoseList: Vec3\[\] = \[\];
let statusBarHeight: number = 0;

## Displaying the Preview Stream

First, initialize the AR session and AR scene. For details, please refer to [Initializing AR Session and AR Scene](../managing-ar-sessions/document.md#section3391814131611).

@Builder
export function ARMeshBuilder(): void {
  ARMesh();
}

@Component
struct ARMesh {
  @State arContext?: arViewController.ARViewContext = undefined;
  @State context: Context = this.getUIContext().getHostContext() as Context;

  build(): void {
    NavDestination() {
      RelativeContainer() {
        if (this.arContext) {
          ARView({ context: this.arContext })
            .height('100%')
            .width('100%')
            .alignRules({
              center: { anchor: '\_\_container\_\_', align: VerticalAlign.Center },
              middle: { anchor: '\_\_container\_\_', align: HorizontalAlign.Center }
            })
            .onClick((event) => {
              this.objectCollisionDetection(event);
            })
        }
      }
    }
    .onAppear(() => {
      this.initARView();
      this.getAvoidArea();
    })
    .onWillDisappear(() => {
      this.stopARView();
    })
    .onShown(() => {
      this.resumeARView();
    })
    .onHidden(() => {
      this.pauseARView();
    })
    .hideTitleBar(true)
    .hideBackButton(true)
    .hideToolBar(true)
  }

  // Obtain the user's click coordinates and hit testing results.
  private objectCollisionDetection(event: ClickEvent): void {
    let x: number = this.getUIContext().vp2px(event.windowX);
    let y: number = this.getUIContext().vp2px(event.windowY) - statusBarHeight;
    console.info(\`Get onclick position, x: ${x} y: ${y}.\`);

    try {
      let result: arEngine.ARHitResult\[\] = frame.hitTest(x, y);
      console.info(\`The hitResult size is: ${result.length}.\`);
      if (!result) {
        return;
      }

      for (let i = 0; i < result.length; i++) {
        let hitResult: arEngine.ARHitResult = result\[i\];
        let distance: number = hitResult.distance;

        if (distance <= 0) {
          continue;
        }

        let hitAnchor: arEngine.ARAnchor = hitResult.createAnchor();
        let pos: Vec3 = hitAnchor.getPose().translation;

        hitPoseList.push(pos);
        hitAnchorList.push(hitAnchor);

      }
      console.info('Succeeded in getting hit result.');  // Successfully obtained the hit target.
    } catch (error) {
      const err: BusinessError = error as BusinessError;
      console.error(\`Failed to get hitResults. Code is ${err.code}, message is ${err.message}\`);
    }
  }

  private initARView(): void {
    Scene.load().then((scene: Scene) => {
      let viewContext: arViewController.ARViewContext = new arViewController.ARViewContext();
      viewContext.scene = scene;
      viewContext.callback = new ARViewCallbackImpl();
      viewContext.config = {
        type: arEngine.ARType.WORLD,
        planeFindingMode: arEngine.ARPlaneFindingMode.HORIZONTAL\_AND\_VERTICAL,
        powerMode: arEngine.ARPowerMode.NORMAL,
        semanticMode: arEngine.ARSemanticMode.NONE,
        poseMode: arEngine.ARPoseMode.GRAVITY,
        depthMode: arEngine.ARDepthMode.AUTOMATIC,
        meshMode: arEngine.ARMeshMode.ENABLE,  // Enable mesh.
        focusMode: arEngine.ARFocusMode.AUTO
      }
      viewContext.init().then(() => {
        this.arContext = viewContext;
        console.info('Succeeded in initializing ARView.');
      }).catch((err: BusinessError) => {
        console.error(\`Failed to init ARView. Code is ${err.code}, message is ${err.message}.\`);
      })
    })
  }

  // Obtain the actual screen height minus the status bar (preview stream height).
  private getAvoidArea(): void {
    let avoidAreaType: window.AvoidAreaType = window.AvoidAreaType.TYPE\_SYSTEM;
    window.getLastWindow(this.context).then((data) => {
      // Obtain the height of the status bar at the top.
      let avoidArea1: window.AvoidArea = data.getWindowAvoidArea(avoidAreaType);
      statusBarHeight = avoidArea1.topRect.height;
      console.info(\`The statusBarHeight is ${statusBarHeight}.\`);
    }).catch((err: BusinessError) => {
      console.error(\`Failed to obtain the window. Code is ${err.code}, message is ${err.message}.\`);
    })
  }

  private stopARView(): void {
    // ...
  }
  private resumeARView(): void {
    // ...
  }
  private pauseARView(): void {
    // ...
  }
}

## Obtaining Mesh Data

Call [ARViewCallback](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arviewcontroller#section9396615174614) and use its [onFrameUpdate](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arviewcontroller#section52341758194715) method to update frame data and obtain mesh data.

class ARViewCallbackImpl extends arViewController.ARViewCallback {
  onAnchorAdd(ctx: arViewController.ARViewContext, node: Node, anchor: arEngine.ARAnchor): void {
    // ...
  }

  onAnchorUpdate(ctx: arViewController.ARViewContext, node: Node, anchor: arEngine.ARAnchor): void {
    // ...
  }

  onFrameUpdate(ctx: arViewController.ARViewContext, sysBootTs: number): void {
    let planeVertices: number\[\] = \[\];
    let vertexNormals: number\[\] = \[\];
    let triangleIndices: number\[\] = \[\];

    if (!ctx.session) {
      return;
    }

    let session: arEngine.ARSession | undefined = ctx.session;

    try {
      frame = session.getFrame();
      let camera: arEngine.ARCamera = frame.getCamera();
      let sceneMesh: arEngine.ARSceneMesh = frame.acquireSceneMesh();

      if (camera.state === arEngine.ARTrackingState.TRACKING) {
        planeVertices = arrayBufferFloat32ToNumber(sceneMesh.getVertices());
        triangleIndices = arrayBufferInt32ToNumber(sceneMesh.getTriangleIndices());
        vertexNormals = arrayBufferFloat32ToNumber(sceneMesh.getVertexNormals());

        // Output mesh data.
        console.info(\`The mesh data planeVertices is: ${planeVertices}, triangleIndices is: ${triangleIndices},
          vertexNormals is: ${vertexNormals}.\`);
      }

    } catch (error) {
      const err: BusinessError = error as BusinessError;
      console.error(\`Failed to acquire depth information. Code is ${err.code}, message is ${err.message}.\`);
    }
  }
}

## Custom Methods for Obtaining Mesh Scanning Information

For details about **arrayBufferFloat32ToNumber** and **arrayBufferInt32ToNumber**, please refer to [Data Type Conversion](../data-type-conversion/document.md).
