# High-Precision Geometric Reconstruction

#### Overview

AR Engine supports this capability since version 6.0.0(20).

This section describes how to use the high-precision geometric reconstruction of AR Engine to identify cube objects or embedded cube spaces in a space and calculate the length, width, height, and volume of the identified objects or spaces. This capability can be used to measure the volume of a cube and the size of an embedded space.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/KI-WLQoGTC2desBac6yhZg/notice_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062046Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E9FFFC9D716CD2A19270372E04626E30D11ADC20BB90CE3ECDE33B60FA3FE631)

This feature only provides functionality and does not constitute a guarantee of product quality or any commitment. For details, please refer to [AR Engine High-Precision Geometric Reconstruction Limitations and Disclaimer](../../appendix/document.md#section68356131976).

#### API Description

High-precision geometric reconstruction mainly depends on [ARSemanticDenseData](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arengine#section137161158185414). The following APIs are related to high-precision geometric reconstruction. For details about these APIs, please refer to [AR Engine API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-arkts-api).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[ARSession.getFrame](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arengine#section114051108916)

 | 

Obtains a frame of data after AR Engine processing.

 |
| 

[ARFrame.acquireSemanticDense](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arengine#section945690181710)

 | 

Returns the high-precision geometric reconstruction object data of the current frame.

 |
| 

[ARSemanticDenseData.acquireCubeData](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arengine#section1458368561)

 | 

Returns a list of cube data of the high-precision geometric reconstruction object.

 |
| 

[ARSemanticDenseData.release](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arengine#section13749838482)

 | 

Releases the high-precision geometric reconstruction object data.

 |

#### Development Procedure

For any AR app built with ArkTS, it is first necessary to create an AR session [ARViewContext](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arviewcontroller#section12681656121519), to manage the system status of the AR Engine. For details about how to create an [ARViewContext](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arviewcontroller#section12681656121519) for an AR session, please refer to [Managing AR Sessions](../managing-ar-sessions/document.md).

## Modules to Import

The following modules are required for high-precision geometric reconstruction.

import { arEngine, ARView, arViewController } from '@kit.AREngine';
import { Node, Scene } from '@kit.ArkGraphics3D';
import { BusinessError } from '@kit.BasicServicesKit';

## Defining Variables

Define the variables **cubeVertexData** to receive the vertex buffer of the cube, **cubeConfidence** to receive the confidence data of the identified cube, and **cubeLabel** to receive the semantic information of the cube.

let cubeVertexData: Array<number>;
let cubeConfidence: number;
let cubeLabel: arEngine.ARSemanticPlaneLabel;

## Displaying the Preview Stream

First, initialize the AR session and AR scene. For details, please refer to [Initializing AR Session and AR Scene](../managing-ar-sessions/document.md#section3391814131611).

Set **semanticDenseMode** to [ARSemanticDenseMode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arengine#section162053411246).CUBE\_VOLUME to enable volume measurement and recognition.

Display the recognized geometric data on the device UI and use a repeated call function method to update the geometric data in real time.

@Builder
export function ARSemanticDenseBuilder(): void {
  ARSemanticDense();
}

@Component
struct ARSemanticDense {
  @State arContext?: arViewController.ARViewContext = undefined;

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
        }
      }
    }
    .onAppear(() => {
      this.initARView();
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

  private initARView(): void {
    Scene.load().then((scene: Scene) => {
      let viewContext: arViewController.ARViewContext = new arViewController.ARViewContext();
      viewContext.scene = scene;
      viewContext.callback = new ARViewCallbackImpl();
      viewContext.config = {
        type: arEngine.ARType.WORLD,
        planeFindingMode: arEngine.ARPlaneFindingMode.HORIZONTAL\_AND\_VERTICAL,
        powerMode: arEngine.ARPowerMode.NORMAL,
        semanticDenseMode: arEngine.ARSemanticDenseMode.CUBE\_VOLUME, // Enable volume measurement.
        poseMode: arEngine.ARPoseMode.GRAVITY,
        depthMode: arEngine.ARDepthMode.DISABLED,
        meshMode: arEngine.ARMeshMode.DISABLED,
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

## Obtaining the Volume Data of a Cube

Call [ARViewCallback](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arviewcontroller#section9396615174614) and use its [onFrameUpdate](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arviewcontroller#section52341758194715) method to update the frame data, use the [ARSession.getFrame](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arengine#section114051108916) method to obtain the current frame, use the [ARFrame.acquireSemanticDense](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arengine#section945690181710) method to obtain the high-precision geometric reconstruction object data, and use the [ARSemanticDenseData.acquireCubeData](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arengine#section1458368561) method to obtain the volume data of a cube from the high-precision geometric reconstruction object data. For details about the definition of related variables, please refer to [Defining Variables](#section57509123317).

class ARViewCallbackImpl extends arViewController.ARViewCallback {
  onAnchorAdd(ctx: arViewController.ARViewContext, node: Node, anchor: arEngine.ARAnchor): void {
    // ...
  }

  onAnchorUpdate(ctx: arViewController.ARViewContext, node: Node, anchor: arEngine.ARAnchor): void {
    // ...
  }

  onFrameUpdate(ctx: arViewController.ARViewContext, sysBootTs: number): void {
    if (!ctx.session) {
      return;
    }

    let arSession: arEngine.ARSession = ctx.session;

    try {
      let frame: arEngine.ARFrame = arSession.getFrame();
      if (frame) {
        let semanticData : arEngine.ARSemanticDenseData = frame.acquireSemanticDense();
        if(semanticData){
          if(semanticData.cubeDataSize>0){
            // Obtain the volume data of the first cube.
            let semanticCubeData: arEngine.ARSemanticDenseCubeData = semanticData.acquireCubeData()\[0\];
            cubeVertexData = semanticCubeData.vertexData;
            cubeConfidence = semanticCubeData.confidence;
            cubeLabel = semanticCubeData.label;
          }
          semanticData.release();
        }
      }
    } catch (error) {
      const err: BusinessError = error as BusinessError;
      console.error(\`Failed to update data. Code is ${err.code}, message is ${err.message}.\`);
    }
  }
}
