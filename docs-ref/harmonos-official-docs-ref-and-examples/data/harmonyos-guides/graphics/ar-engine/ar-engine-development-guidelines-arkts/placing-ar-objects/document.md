# Placing AR Objects

#### Overview

AR Engine supports this capability since version 5.1.0(18).

This section describes how AR Engine identifies planes surrounding a device and allows users to place virtual objects on them, bridging the virtual and real worlds. It is ideal for virtual home decoration and digital exhibition hall layouts.

**Figure 1** AR object placement  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/e8MfLoqpRpKXUP9zlhSxTA/en-us_image_0000002500306282.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062046Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=60E445ABC38BBAA6908548CAA235102E431127E7E7137F63DFD0518191903A6B "Click to enlarge")

AR Engine capabilities involved in this section:

-   Motion tracking
-   Environment tracking (plane detection)
-   Hit testing

#### API Description

Placing AR objects mainly depends on [ARViewContext](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arviewcontroller#section12681656121519). The following table lists the APIs related to placing AR objects. For details about these APIs, please refer to [AR Engine API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-arkts-api).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[ARViewContext.init](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arviewcontroller#section07524457283)

 | 

Initializes [ARViewContext](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arviewcontroller#section12681656121519) to initialize the AR session and configure the AR rendering scene, among other tasks.

 |
| 

[ARViewContext.pause](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arviewcontroller#section9795165613212)

 | 

Pauses camera tracking and AR scene rendering.

 |
| 

[ARViewContext.destroy](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arviewcontroller#section169251835133414)

 | 

Destroys [ARViewContext](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arviewcontroller#section12681656121519) to release the resources used by ARView, including terminating the AR session and dismantling the presented scene. This should be used when exiting the ARView scene.

 |
| 

[ARViewContext.resume](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arviewcontroller#section639015333356)

 | 

Resumes paused camera tracking and AR scene rendering.

 |
| 

[ARViewContext.scene](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arviewcontroller#section885612613616)

 | 

Sets the AR scene of ARView.

 |
| 

[ARViewContext.scene](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arviewcontroller#section1371542426)

 | 

Obtained AR presentation scene for managing spatial nodes.

 |
| 

[ARViewContext.session](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arviewcontroller#section18461161774312)

 | 

Obtains AR sessions, which are used to obtain AR environment tracking, camera tracking, hit testing, and other capabilities, such as camera pose, plane information, and anchor creation.

 |
| 

[ARViewContext.config](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arviewcontroller#section4323184815436)

 | 

Sets the AR session settings, including north-facing coordinates, performance modes, and more.

 |
| 

[ARViewContext.callback](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arviewcontroller#section20507194174418)

 | 

Sets callback function to implement corresponding service logic via callback.

 |
| 

[ARFrame.getCamera](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arengine#section1293654414328)

 | 

Obtains the camera parameter object of the current frame.

 |
| 

[ARFrame.getUpdatedTrackables](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arengine#section43145512417)

 | 

Obtains the updated trackable object of a specified type.

 |
| 

[ARFrame.hitTest](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arengine#section20353182861218)

 | 

Obtains the pixel coordinates (**pixelX** and **pixelY**) in the preview area based on the light projected by the camera to determine the ray direction, and then checks whether the ray has an intersection on the plane or point cloud.

 |
| 

[ARAnchor.getPose](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arengine#section1448415478356)

 | 

Obtains the pose of the anchor in the world coordinate system.

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

[ARPose.getMatrix](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arengine#section5278038164917)

 | 

Converts the pose data into a 4 × 4 matrix.

 |

#### Development Procedure

This section provides only the key development steps. Click [here](https://gitcode.com/HarmonyOS_Samples/arengine_samplecode_clientdemo_arkts) to access the complete demo code.

The AR Engine only outputs data for detected planes. To enhance observation, you can use either the Ark Graphics Platform (AGP) rendering engine or [XComponent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-xcomponent) to draw the identified planes. For details about AGP, please refer to the [introduction to ArkGraphics 3D](../../../arkgraphics-3d/about-this-kit/document.md) and [AGP Engine](https://gitcode.com/openharmony/graphic_graphic_3d).

For any AR app built with ArkTS, it is first necessary to create an AR session [ARViewContext](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arviewcontroller#section12681656121519), to manage the system status of the AR Engine. For details about how to create an [ARViewContext](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arviewcontroller#section12681656121519) for an AR session, please refer to [Managing AR Sessions](../managing-ar-sessions/document.md).

## Modules to Import

The modules required for placing AR objects are as follows.

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

Add a hit event to **ARView** for collision detection, and obtain the anchor pose data and add it to a list.

@Builder
export function ARWorldBuilder(): void {
  ARWorld();
}

@Component
struct ARWorld {
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
            .onClick((event: ClickEvent) => {
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
        let trackable: arEngine.ARTrackable = hitResult.getTrackable();

        if (trackable.type !== arEngine.ARTrackableType.PLANE) {
          continue;
        }

        let hitPlane: arEngine.ARPlane = trackable as arEngine.ARPlane;
        let hitPose: arEngine.ARPose = hitResult.getHitPose();
        let inPolygon: boolean = hitPlane.isPoseInPolygon(hitPose);
        let distance: number = hitResult.distance;
        console.info(\`The hitResult inPolygon is: ${inPolygon}, distance is: ${distance}.\`);

        if (!inPolygon || distance <= 0) {
          continue;
        }

        let hitAnchor: arEngine.ARAnchor = hitResult.createAnchor();
        let pos: Vec3 = hitAnchor.getPose().translation;

        hitPoseList.push(pos);
        hitAnchorList.push(hitAnchor);

      }
      console.info('Succeeded in getting hit result.');
    } catch (error) {
      const err: BusinessError = error as BusinessError;
      console.error(\`Failed to get hitResults. Code is ${err.code}, message is ${err.message}.\`);
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

 // Obtain the actual screen height minus the status bar (preview stream height).
  private getAvoidArea(): void {
    let avoidAreaType: window.AvoidAreaType = window.AvoidAreaType.TYPE\_SYSTEM;
    window.getLastWindow(this.context).then((data) => {
      // Obtain the height of the status bar at the top.
      let avoidArea: window.AvoidArea = data.getWindowAvoidArea(avoidAreaType);
      statusBarHeight = avoidArea.topRect.height;
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

## Rendering the Detected Plane and Placed Object

Call [ARViewCallback](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arviewcontroller#section9396615174614) and use its [onFrameUpdate](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arviewcontroller#section52341758194715) method to update frame data and obtain plane information.

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
      frame = arSession.getFrame();
      let camera: arEngine.ARCamera = frame.getCamera();
      let trackable: arEngine.ARTrackable\[\] = \[\];

      if (camera.state === arEngine.ARTrackingState.TRACKING) {
        trackable = arSession.getAllTrackables(arEngine.ARTrackableType.PLANE);
        console.info(\`Succeeded in getting tracking plane, length is: ${trackable.length}.\`);  // Output the number of detected planes.
      }

    } catch (error) {
      const err: BusinessError = error as BusinessError;
      console.error(\`Failed to update data. Code is ${err.code}, message is ${err.message}.\`);
    }
  }
}
