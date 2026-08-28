# Obtaining Depth Estimation Information

#### Overview

AR Engine supports this capability since version 5.1.0(18).

AR Engine's depth estimation feature utilizes algorithms to generate depth estimation data (distance of object surface from the camera) and depth confidence information, providing 3D environmental perception capabilities. This technology can be applied in scenarios such as measurement, volume estimation, and scene reconstruction to obtain spatial object depth information. Based on this data, various spatial computation tasks, like calculating object volumes, can be accomplished.

To obtain the depth image, use NAPI for development. For details, please refer to [Obtaining Depth Image](../../ar-engine-development-guidelines-c-c/obtaining-depth-image/document.md). The depth image capability will be available in later versions of ArkTS APIs.

**Figure 1** Depth estimation information  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/uFE6IzNRTj-nGWVi1_W55Q/en-us_image_0000002532146185.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062046Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1D4AAC272F405C76DAE36EAA8DC73DCA00F2CC7A61B7431EE659669F5051DA55)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/51cNnEDwS02Zd8GfcN7kuQ/notice_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062046Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=52F61D3309651DC8C76AA0BA7CEB9C124E837DBE4190F4A977E89167BAEE30FF)

This feature only provides functionality and does not constitute a guarantee of product quality or any commitment. For details, please refer to [AR Engine Depth Estimation Technology Limitations and Disclaimer](../../appendix/document.md#section1854314717219).

AR Engine capabilities involved in this section:

-   Motion tracking
-   Environment tracking (plane detection)

#### API Description

Depth estimation information can be obtained using the [ARFrame](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arengine#section83421523123819) object, and the following are the APIs related to depth estimation. For details about these APIs, please refer to [AR Engine API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-arkts-api).

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

[ARFrame.acquireDepthImage16Bits](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arengine#section8978424152512)

 | 

Obtains the depth image object corresponding to the current frame.

 |
| 

[ARFrame.acquireDepthConfidenceImage](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arengine#section58412318287)

 | 

Obtains the depth confidence map of the current frame.

 |

#### Development Procedure

For any AR app built with ArkTS, it is first necessary to create an AR session [ARViewContext](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arviewcontroller#section12681656121519), to manage the system status of the AR Engine. For details about how to create an [ARViewContext](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arviewcontroller#section12681656121519) for an AR session, please refer to [Managing AR Sessions](../managing-ar-sessions/document.md).

## Modules to Import

The following modules are required for obtaining depth estimation information.

import { arEngine, ARView, arViewController } from '@kit.AREngine';
import { Node, Scene } from '@kit.ArkGraphics3D';
import { BusinessError } from '@kit.BasicServicesKit';

## Defining Variables

Define the variables **centerDistance** (depth estimation distance) and **centerConfidence** (depth confidence).

let centerDistance: number;
let centerConfidence: number;

## Displaying Depth Estimation Information

First, initialize the AR session and AR scene. For details, please refer to [Initializing AR Session and AR Scene](../managing-ar-sessions/document.md#section3391814131611).

Display depth estimation and confidence information on the device UI. Use a repeated call function method to update such information on the device UI in real time.

@Builder
export function ARDepthBuilder(): void {
  ARDepth();
}

@Component
struct ARDepth {
  private delayInterval: number = 33;
  private intervalId: number = -1;
  @State arContext?: arViewController.ARViewContext = undefined;
  @State depthConfidence: number = 0;
  @State depthDistance: string = '0';

  build(): void {
    NavDestination() {
      RelativeContainer() {
        if (this.arContext) {
          ARView({ context: this.arContext })
            .height('100%')
            .width('100%')
            .alignRules({
              center: { anchor: "\_\_container\_\_", align: VerticalAlign.Center },
              middle: { anchor: "\_\_container\_\_", align: HorizontalAlign.Center }
            })

          // Display the center point, depth estimation value, and confidence on the screen.
          Text('●')
            .fontSize(8)
            .fontColor(Color.Red)
            .alignRules({
              center: { anchor: '\_\_container\_\_', align: VerticalAlign.Center },
              middle: { anchor: '\_\_container\_\_', align: HorizontalAlign.Center }
            })

          Column() {
            Text(\`${this.depthDistance} | ${this.depthConfidence}\`)
              .fontColor(Color.Yellow)
              .fontSize(24)
              .textShadow({
                radius: 10,
                color: Color.Black,
                offsetX: 0,
                offsetY: 0
              })
          }
          .alignItems(HorizontalAlign.Center)
          .margin({ bottom: 10 })
          .alignRules({
            bottom: { anchor: "\_\_container\_\_", align: VerticalAlign.Bottom },
            middle: { anchor: "\_\_container\_\_", align: HorizontalAlign.Center }
          })
        }
      }
    }
    .onAppear(() => {
      this.initARView();
      this.renderDepthMsg();
    })
    .onWillAppear(() => {
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
        semanticMode: arEngine.ARSemanticMode.NONE,
        poseMode: arEngine.ARPoseMode.GRAVITY,
        depthMode: arEngine.ARDepthMode.AUTOMATIC,
        meshMode: arEngine.ARMeshMode.DISABLED,
        focusMode: arEngine.ARFocusMode.AUTO
      }
      viewContext.init().then(() => {
        this.arContext = viewContext;
        console.info('Succeeded in initializing ARView.');
      }).catch((err: BusinessError) => {
        console.error(\`Failed to init ARView. Code is ${err.code}, message is ${err.message}\`);
      })
    })
  }

  private renderDepthMsg(): void {
    this.intervalId = setInterval(() => {
      if (centerDistance === undefined || centerConfidence === undefined) {
        return;
      }
      this.depthDistance = centerDistance.toFixed(4);
      this.depthConfidence = centerConfidence;
    }, this.delayInterval)
  }

  private stopARView(): void {
    if (!this.arContext) {
      return;
    }
    try {
      clearInterval(this.intervalId);
      this.arContext.destroy();
      centerDistance = 0;
      centerConfidence = 0;
    } catch (error) {
      const err: BusinessError = error as BusinessError;
      console.error(\`Failed to stop context. Code is ${err.code}, message is ${err.message}\`);
    }
  }

  private resumeARView(): void {
    // ...
  }
  private pauseARView(): void {
    // ...
  }
}

## Obtaining Depth Estimation Information

Call [ARViewCallback](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arviewcontroller#section9396615174614) and use its [onFrameUpdate](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arviewcontroller#section52341758194715) method to obtain the AR session object. Then perform depth estimation to obtain depth and confidence information.

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

    let session: arEngine.ARSession | undefined = ctx.session;

    try {
      let frame: arEngine.ARFrame = session.getFrame();
      let depthImage: arEngine.ARImage = frame.acquireDepthImage16Bits();
      let confidenceImage: arEngine.ARImage = frame.acquireDepthConfidenceImage();
      let depthPlane: number\[\] = arrayBufferInt32ToNumber(depthImage.planes\[0\].buffer);
      let confidencePlane: number\[\] = arrayBufferInt32ToNumber(confidenceImage.planes\[0\].buffer);
      const index: number = depthImage.height \* depthImage.width / 2 + depthImage.width / 2;

      centerDistance = depthPlane\[index\] / 1000;
      centerConfidence = confidencePlane\[index\];
    } catch (error) {
      const err: BusinessError = error as BusinessError;
      console.error(\`Failed to acquire depth information. Code is ${err.code}, message is ${err.message}\`);
    }
  }
}

## Custom Methods for Obtaining Depth Estimation Information

For details about **arrayBufferInt32ToNumber**, please refer to [Data Type Conversion](../data-type-conversion/document.md).
