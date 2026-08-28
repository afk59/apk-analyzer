# Managing AR Sessions

#### Overview

Before developing an AR app, it is necessary to call the AR session API to create a unique AR session for follow-up procedure and management. AR sessions are critical in the entire lifecycle of an AR app.

You can use [ARViewContext](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arviewcontroller#section12681656121519) to create and destroy AR sessions.

[ARViewContext](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arviewcontroller#section12681656121519) is different from [ARSession](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arengine#section19193165314510) in that [ARViewContext](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arviewcontroller#section12681656121519) not only encapsulates AR sessions, but also integrates the creation and management of AR scenes, making development more convenient.

Before developing other features, ensure that a unique functional AR session has been created.

#### API Description

AR sessions mainly depend on [ARViewContext](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arviewcontroller#section12681656121519). The following table lists the APIs related to AR sessions. For details about these APIs, please refer to [arViewController (AR Scene Management Capabilities)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arviewcontroller).

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

#### Development Procedure

For any AR app built with ArkTS, it is first necessary to create an AR session [ARViewContext](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arviewcontroller#section12681656121519), to manage the system status of the AR Engine.

## Modules to Import

Import AR Engine-related modules as follows.

import { arEngine, ARView, arViewController } from '@kit.AREngine';
import { Node, Scene } from '@kit.ArkGraphics3D';
import { BusinessError } from '@kit.BasicServicesKit';

## Initializing AR Session and AR Scene

Use [ARViewContext.init](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arviewcontroller#section07524457283) to initialize an AR session and scene.

Ensure that the Camera permission has been obtained beforehand; otherwise, the AR scene will not load. For details, please refer to [Preparations](../../preparations/document.md#section148162301428) or [Applying for Permissions](../../preparations/document.md#section12219144310509).

Once the AR session and scene are successfully created, use [Component Navigation (Navigation) (Recommended)](../../../../application-framework/arkui/ui-development-arkts-based-declarative-development-paradigm/setting-component-navigation-and-page-routing/component-navigation-recommended/document.md) and [ARView](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-component-arview#section46518288429) to display the AR scene on the device. For instructions about [Component Navigation (Navigation) (Recommended)](../../../../application-framework/arkui/ui-development-arkts-based-declarative-development-paradigm/setting-component-navigation-and-page-routing/component-navigation-recommended/document.md), please refer to [Preparations](../../preparations/document.md#section148162301428).

@Builder
export function ARWorldBuilder(): void {
  ARWorld();
}

@Component
struct ARWorld {
  @State arContext?: arViewController.ARViewContext = undefined;

  // Create the UI window and display the AR scene.
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
      viewContext.callback = new ARViewCallbackImpl();  // Implement service scenarios via callback.
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
}

## Processing Services Using the AR Session Object

Call [ARViewCallback](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arviewcontroller#section9396615174614) to obtain the AR session object using the [onFrameUpdate](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arviewcontroller#section52341758194715) method. Then, compile the processing logic based on the required services.

class ARViewCallbackImpl extends arViewController.ARViewCallback {
  onAnchorAdd(ctx: arViewController.ARViewContext, node: Node, anchor: arEngine.ARAnchor): void {
    // ...
  }

  onAnchorUpdate(ctx: arViewController.ARViewContext, node: Node, anchor: arEngine.ARAnchor): void {
    // ...
  }

  async onFrameUpdate(ctx: arViewController.ARViewContext, sysBootTs: number): Promise<void> {
    if (!ctx.session) {
      return;
    }

    let arSession: arEngine.ARSession = ctx.session; // Obtain the AR session.

    try {
      // This example demonstrates how to obtain and destroy a frame object.
      let frame: arEngine.ARFrame = arSession.getFrame();
      await frame.release();

    } catch (error) {
      const err: BusinessError = error as BusinessError;
      console.error(\`Failed to update data. Code is ${err.code}, message is ${err.message}.\`);
    }
  }
}

## Pausing the AR Session

To pause an AR session, you can use the [ARViewContext.pause](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arviewcontroller#section9795165613212) method to pause the AR session and AR scene when the app is running in the background.

private pauseARView(): void {
  if (!this.arContext) {
    return;
  }
  try {
    this.arContext.pause();
  } catch (error) {
    const err: BusinessError = error as BusinessError;
    console.error(\`Failed to pause context. Code is ${err.code}, message is ${err.message}.\`);
  }
}

## Resuming the AR Session

You can call [ARViewContext.resume](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arviewcontroller#section639015333356) to resume a paused AR session or AR scene.

private resumeARView(): void {
  if (!this.arContext) {
    return;
  }
  try {
    this.arContext.resume();
  } catch (error) {
    const err: BusinessError = error as BusinessError;
    console.error(\`Failed to resume context. Code is ${err.code}, message is ${err.message}.\`);
  }
}

## Destroying the AR Session

When exiting an AR session or AR scene, you can use the [ARViewContext.destroy](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arviewcontroller#section169251835133414) method to destroy both the AR session and AR scene.

private stopARView(): void {
  if (!this.arContext) {
    return;
  }
  try {
    this.arContext.destroy();
  } catch (error) {
    const err: BusinessError = error as BusinessError;
    console.error(\`Failed to stop context. Code is ${err.code}, message is ${err.message}\`);
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/TJMAarJPRbeI4i-9zCYOlQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062046Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DF35BDC29AEA11FCAD0AF2B5BB7E283C31633C9D891862EAD357629AC23C5333)

In addition to [aboutToAppear](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-custom-component-lifecycle#abouttoappear), [aboutToDisappear](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-custom-component-lifecycle#abouttodisappear), [onPageShow](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-custom-component-lifecycle#onpageshow), and [onPageHide](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-custom-component-lifecycle#onpagehide), you can also use the page lifecycle methods described in [Page Lifecycle](../../../../application-framework/arkui/ui-development-arkts-based-declarative-development-paradigm/setting-component-navigation-and-page-routing/component-navigation-recommended/document.md#page-lifecycle) of [Navigation](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-navigation) as needed.
