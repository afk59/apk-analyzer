# Obtaining the Device Pose

#### Overview

AR Engine supports this capability since version 5.1.0(18).

The device pose describes the position and orientation of an object in the real world. AR Engine provides 6DoF pose computation in the world coordinate system, including the object's position (translation along the x, y, and z axes) and orientation (rotation around the x, y, and z axes). AR Engine allows for obtaining the pose of a device at any time in the space in real time.

#### World Coordinate System and Pose

The device pose is typically represented in the world coordinate system, which describes the absolute position of objects in real physical spaces, with its positive directions shown in the figure.

**Figure 1** World coordinate system  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/MnyOZ-OISWuw6qpEGwOcIA/en-us_image_0000002500426118.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062046Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C400E3E44E2A30C33D22DA65ABCF26997D4F8D6370BD7FD8AF6E96D3C8B6BCD9)

AR Engine will automatically initialize the world coordinate system.

In AR Engine, the device pose is described by a 7-dimensional vector, which consists of the rotation component ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/8a53nroaQzu80OxQ_ngvbA/en-us_formulaimage_0000002532306169.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062046Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=31F65B7DD2EE3103F1C96329F80E87313F5C2D79ABEA5B8A20B30387C42EAEFD) and the translation component ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/9WYaV8SUQ7KYQ0EzhLyifA/en-us_formulaimage_0000002532306171.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062046Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7BC122A7EF706076963447D4E527ADB508FF772BC8687DB401ADB470508C30B7). The rotation component ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/QgMQZLXySCKElbzNHMOx-w/en-us_formulaimage_0000002500306278.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062046Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=53CC95BB453DE3B5CAD6479D0BC3EC10DAF5CEA372F0E45C8D95EB7F02504885) is a quaternion that describes the device's rotation state relative to the coordinate origin, while the translation component ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/P-tqu_kDSfiYoVP0yLVP7A/en-us_formulaimage_0000002500306280.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062046Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B681D79334B75E09C0C74489D46C45210A2CA663CF20C821C23A4136F5FD51ED) is a three-dimensional vector that describes the device's translation state relative to the coordinate origin, as shown in the following figure.

**Figure 2** Rotational and translational changes of the device pose  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/mJFsF36hTDCKAOOIieIjOw/en-us_image_0000002532306167.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062046Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=13C9E9894FE8B5B9873C0EEED290627AC1FC87FED656CDE67E7A36F9D12CA410)

With rotation components and translation components, a device's pose state in space at any given moment can be described.

#### API Description

Device pose can be obtained via the [ARCamera](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arengine#section176984261612) object. The following API is used for obtaining the device pose information. For details about these APIs, please refer to [AR Engine API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-arkts-api).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[ARCamera.getPose](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arengine#section0507108132710)

 | 

Obtains the pose information of the camera in the world space.

 |

#### Development Procedure

For any AR app built with ArkTS, it is first necessary to create an AR session [ARViewContext](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arviewcontroller#section12681656121519), to manage the system status of the AR Engine. For details about how to create an [ARViewContext](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arviewcontroller#section12681656121519) for an AR session, please refer to [Managing AR Sessions](../managing-ar-sessions/document.md).

## Modules to Import

The following modules are required for obtaining the device pose capability.

import { arEngine, ARView, arViewController } from '@kit.AREngine';
import { Node, Scene, Vec3 } from '@kit.ArkGraphics3D';
import { BusinessError } from '@kit.BasicServicesKit';

Vec3 is a three-dimensional vector used to store the device pose information.

## Defining Variables

Define two variables, **pose** and **stateReason**, to receive the pose information and the tracking failure cause.

let pose: arEngine.ARPose;
let stateReason: arEngine.ARTrackingStateReason;

## Displaying the Preview Stream and Device Pose Information

First, initialize the AR session and AR scene. For details, please refer to [Initializing AR Session and AR Scene](../managing-ar-sessions/document.md#section3391814131611).

Display device pose information and tracking failure causes on the device UI. Use a repeated call function method to update the pose and tracking failure information on the device UI in real time.

@Builder
export function ARPoseBuilder(): void {
  ARPose();
}

@Component
struct ARPose {
  @State arContext?: arViewController.ARViewContext = undefined;
  private intervalId: number = -1;
  // The interval for repeated calls is 33 ms, corresponding to a frame rate of 30 fps.
  private delayInterval: number = 33;
  // Information parameters of the pose.
  @State translation: Vec3 = {
    x: 0,
    y: 0,
    z: 0
  }
  // Tracking failure cause.
  @State reason: arEngine.ARTrackingStateReason = stateReason;

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

          // Display the device pose on the screen.
          Column() {
            Text(\`x: ${this.translation.x.toFixed(4)}\`)
              .infoStyles()
            Text(\`y: ${this.translation.y.toFixed(4)}\`)
              .infoStyles()
            Text(\`z: ${this.translation.z.toFixed(4)}\`)
              .infoStyles()
            Text(\`reason: ${this.reason}\`)
              .infoStyles()
          }
          .alignItems(HorizontalAlign.Start)
          .margin({ left: 28, top: 28 })
          .alignRules({
            top: { anchor: "\_\_container\_\_", align: VerticalAlign.Top },
            left: { anchor: "\_\_container\_\_", align: HorizontalAlign.Start }
          })
        }
      }
    }
    .onAppear(() => {
      this.initARView();
      // Update the pose and tracking failure cause information at 30 fps.
      this.intervalId = setInterval(() => {
        if (pose !== undefined) {
          this.translation = pose.translation;
          this.reason = stateReason;
        }
      }, this.delayInterval);
    })
    .onWillDisappear(() => {
      // Exit the setInterval function.
      clearInterval(this.intervalId);
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
    // ...
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

// Text style displayed on the UI
@Extend(Text)
function infoStyles() {
  .fontColor(Color.Yellow)
  .fontSize(24)
  .textShadow({
    radius: 10,
    color: Color.Black,
    offsetX: 0,
    offsetY: 0
  })
  .textAlign(TextAlign.Start)
}

## Obtaining the Device Pose Information

Call [ARViewCallback](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arviewcontroller#section9396615174614) and use its [onFrameUpdate](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arviewcontroller#section52341758194715) method to obtain the AR session object (**arSession**). Then, obtain the device pose information for each frame via **arSession**.

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

    let arSession: arEngine.ARSession = ctx.session; // Obtain the AR session.

    try {
      // Obtain the device pose of each frame and the failure cause.
      let frame: arEngine.ARFrame = arSession.getFrame();
      pose = frame.getCamera().getPose();
      stateReason = frame.getCamera().stateReason;
    } catch (error) {
      const err: BusinessError = error as BusinessError;
      console.error(\`Failed to update data. Code is ${err.code}, message is ${err.message}\`);
    }
  }
}
