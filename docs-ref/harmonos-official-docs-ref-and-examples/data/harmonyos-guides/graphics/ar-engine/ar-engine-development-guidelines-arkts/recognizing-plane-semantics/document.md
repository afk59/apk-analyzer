# Recognizing Plane Semantics

#### Overview

AR Engine supports this capability since version 5.1.0(18).

AR Engine allows you to recognize the semantics of a detected plane, which can be wall, floor, seat, table, ceiling, door, window, bed, plane space, cube volume, cube space volume, and unknown types. Specifically, the plane space, cube volume, and cube space volume types are supported only in high-precision geometric reconstruction mode.

#### API Description

Plane semantics information can be obtained using the [ARPlane](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arengine#section3392194311417) object, and the following are the plane-related APIs. For details about these APIs, please refer to [AR Engine API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-arkts-api).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[ARTrackable.getPose](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arengine#section14241133116264)

 | 

Obtains the pose information of the tracking target.

 |
| 

[ARTrackable.getAnchors](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arengine#section10878141483010)

 | 

Obtains the anchor object bound to the input trackable object.

 |
| 

[ARPose.getMatrix](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arengine#section5278038164917)

 | 

Converts the pose data into a 4 × 4 matrix.

 |
| 

[ARPlane.getPolygonXZ](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arengine#section12949442354)

 | 

Obtains the 2D vertex array of the detected plane.

 |
| 

[ARPlane.getSubsumedBy](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arengine#section1127511467514)

 | 

Obtains the parent plane of a plane (a parent plane is generated when a plane is merged with another one).

 |
| 

[ARPlane.isPoseInExtents](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arengine#section102761471453)

 | 

Check if a given pose is within the boundary rectangle of the plane.

 |
| 

[ARPlane.isPoseInPolygon](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arengine#section1471811920162)

 | 

Check if a given pose is within the boundary polygon of the plane.

 |

#### Development Procedure

The AR Engine only outputs data for detected planes. To enhance observation, you can use either the Ark Graphics Platform (AGP) rendering engine or [XComponent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-xcomponent) to draw the identified planes. For details about AGP, please refer to the [introduction to ArkGraphics 3D](../../../arkgraphics-3d/about-this-kit/document.md) and [AGP Engine](https://gitcode.com/openharmony/graphic_graphic_3d).

For any AR app built with ArkTS, it is first necessary to create an AR session [ARViewContext](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arviewcontroller#section12681656121519), to manage the system status of the AR Engine. For details about how to create an [ARViewContext](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arviewcontroller#section12681656121519) for an AR session, please refer to [Managing AR Sessions](../managing-ar-sessions/document.md).

Before identifying plane semantics, detect planes in the recognition environment. For details on how to detect planes in the environment, please refer to [Detecting Planes in the Environment](../detecting-planes-in-the-environment/document.md).

## Modules to Import

The following modules are required for recognizing plane semantics.

import { arEngine, ARView, arViewController } from '@kit.AREngine';
import { Node, Scene } from '@kit.ArkGraphics3D';
import { BusinessError } from '@kit.BasicServicesKit';

## Defining Variables

Define the variable **planeLabel** to receive plane type label information.

let planeLabel: arEngine.ARSemanticPlaneLabel;

## Displaying Plane Semantics Information

First, initialize the AR session and AR scene. For details, please refer to [Initializing AR Session and AR Scene](../managing-ar-sessions/document.md#section3391814131611).

Set **semanticMode** to [ARSemanticMode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arengine#section19325205718138).PLANE to enable plane semantics recognition.

Display the recognized plane information on the device UI and use a repeated call function method to update the plane semantics information in real time.

@Builder
export function ARTargetBuilder(): void {
  ARTarget();
}

@Component
struct ARTarget {
  @State arContext?: arViewController.ARViewContext = undefined;
  // Plane type.
  @State targetPlaneLabel: arEngine.ARSemanticPlaneLabel = planeLabel;
  private intervalId: number = -1;
  // The interval for repeated calls is 33 ms, corresponding to a frame rate of 30 fps.
  private delayInterval: number = 33;

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

          // Display the recognized plane information at the bottom of the screen.
          Column() {
            Text(\`Label: ${convertSemanticLabel(this.targetPlaneLabel)}\`)
              .infoStyles()
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
      // Set the plane semantics information to be updated and recognized at 30 fps.
      this.intervalId = setInterval(() => {
        this.targetPlaneLabel = planeLabel;
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
    Scene.load().then((scene: Scene) => {
      let viewContext: arViewController.ARViewContext = new arViewController.ARViewContext();
      viewContext.scene = scene;
      viewContext.callback = new ARViewCallbackImpl();
      viewContext.config = {
        type: arEngine.ARType.WORLD,
        planeFindingMode: arEngine.ARPlaneFindingMode.HORIZONTAL\_AND\_VERTICAL,
        powerMode: arEngine.ARPowerMode.NORMAL,
        semanticMode: arEngine.ARSemanticMode.PLANE, // Recongnize plane semantics.
        poseMode: arEngine.ARPoseMode.GRAVITY,
        depthMode: arEngine.ARDepthMode.AUTOMATIC,
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

// Text style displayed on the UI.
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

## Obtaining Semantics Information

Call [ARViewCallback](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arviewcontroller#section9396615174614) and use its [onFrameUpdate](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arviewcontroller#section52341758194715) method to update frame data and display the identified plane type on the device UI.

Add the **plane.label** method to obtain the plane semantics information identified in each frame.

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
      let camera: arEngine.ARCamera = frame.getCamera();
      let trackable: arEngine.ARTrackable\[\] = \[\];

      if (camera.state === arEngine.ARTrackingState.TRACKING) {
        trackable = arSession.getAllTrackables(arEngine.ARTrackableType.PLANE);
        console.info(\`Succeeded in getting tracking plane, length is: ${trackable.length}\`);
      }

      for (let i = 0; i < trackable.length; ++i) {
        let plane: arEngine.ARPlane = trackable\[i\] as arEngine.ARPlane;

        // Update the recognized plane semantics information.
        planeLabel = plane.label;
        console.info(\`Succeeded in updating frame data for loop: ${plane.label}\`);
      }

    } catch (error) {
      const err: BusinessError = error as BusinessError;
      console.error(\`Failed to update data. Code is ${err.code}, message is ${err.message}.\`);
    }
  }
}

## Custom Methods for Recognizing Plane Semantics

Use the custom method **getVertices** to obtain vertex data, use the custom method **generateMeshIndex** to create indices, and use the custom method **generateMeshInput** to create mesh data. For details, please refer to [Custom Methods for Plane Detection](../detecting-planes-in-the-environment/document.md#section142331216260).

For details about **arrayBufferFloat32ToNumber**, please refer to [Data Type Conversion](../data-type-conversion/document.md).

For details about **convertSemanticLabel**, see the following information.

function convertSemanticLabel(obj: number): string {
  let res: string = '';
  if (obj === 0) {
    res = 'UNKNOWN';
  } else if (obj === 1) {
    res = 'WALL';
  } else if (obj === 2) {
    res = 'FLOOR';
  } else if (obj === 3) {
    res = 'SEAT';
  } else if (obj === 4) {
    res = 'TABLE';
  } else if (obj === 5) {
    res = 'CEILING';
  } else if (obj === 6) {
    res = 'DOOR';
  } else if (obj === 7) {
    res = 'WINDOW';
  } else if (obj === 8) {
    res = 'BED';
  } else if (obj === 9) {
    res = 'PLANE SPACE';
  } else if (obj === 10) {
    res = 'CUBE VOLUME';
  } else if (obj === 11) {
    res = 'CUBE SPACE';
  }
  return res;
}
