# Detecting Planes in the Environment

#### Overview

AR Engine supports this capability since version 5.1.0(18).

This section describes how to use AR Engine to detect planes in an environment and process the detected planes in apps.

AR Engine capabilities involved in this section:

-   Motion tracking
-   Environment tracking (plane detection)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/nh6qqzBjR96OlbLEk9Ngwg/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062046Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E1A72D1534C43851463EAF96290A5A738E98BB9DDA4F7EC426284333F813330C)

After initialization, move the camera slowly to search for planes.

#### API Description

Plane detection is performed using the [ARPlane](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arengine#section3392194311417) object, and the following are the plane-related APIs. For details about these APIs, please refer to [AR Engine API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-arkts-api).

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

## Modules to Import

The following modules are required for detecting planes.

import { arEngine, ARView, arViewController } from '@kit.AREngine';
import { Node, Scene, Vec3 } from '@kit.ArkGraphics3D';
import { BusinessError } from '@kit.BasicServicesKit';
import { Matrix4 } from '@kit.ArkUI';

## Displaying the Preview Stream

First, initialize the AR session and AR scene. For details, please refer to [Initializing AR Session and AR Scene](../managing-ar-sessions/document.md#section3391814131611).

@Builder
export function ARPlaneBuilder(): void {
  ARPlane();
}

@Component
struct ARPlane {
  @State arContext?: arViewController.ARViewContext = undefined;

  build(): void {
    // ...
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

## Detecting Environmental Planes

Call [ARViewCallback](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arviewcontroller#section9396615174614) and use its [onFrameUpdate](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arviewcontroller#section52341758194715) method to update frame data and use [ARSession.getAllTrackables](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arengine#section559349112710) to obtain all identified planes.

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
        console.info(\`Succeeded in getting tracking plane, length is: ${trackable.length}\`);  // Print the number of currently detected planes.
      }

    } catch (error) {
      const err: BusinessError = error as BusinessError;
      console.error(\`Failed to update data. Code is ${err.code}, message is ${err.message}.\`);
    }
  }
}

## Custom Methods for Plane Detection

Use the custom method **getVertices** to obtain vertex data, use the custom method **generateMeshIndex** to create indices, and use the custom method **generateMeshInput** to create mesh data.

// Obtain the vertex coordinates in the 3D space using a pose matrix arranged in column-major order as the first input parameter, and a coordinate point (x, 0, z, 1) on the x–z plane as the second.
export function getVertices(mat: Matrix4, point: number\[\]): Vec3\[\] {
  let result: Vec3\[\] = \[\];
  for (let i = 0; i < point.length; i += 2) {
    let single: Vec3 = {
      x: (mat\[2\] \* point\[i\] + mat\[6\] \* 0
        + mat\[10\] \* point\[i + 1\] + mat\[14\] \* 1.0),
      y: mat\[1\] \* point\[i\] + mat\[5\] \* 0
        + mat\[9\] \* point\[i + 1\] + mat\[13\] \* 1.0,
      z: -(mat\[0\] \* point\[i\] + mat\[4\] \* 0
        + mat\[8\] \* point\[i + 1\] + mat\[12\] \* 1.0),
    }
    result.push(single);
  }
  return result;
}
// Create a mesh index for ARWorld. Because a plane is stitched by triangles, the first vertex index of each triangle on each plane is the same.
export function generateMeshIndex(input: Vec3\[\]\[\]): number\[\] {
  let result: number\[\] = \[\];
  let start: number = 0;

  for (let i = 0; i < input.length; i++) {
    let length: number = input\[i\].length;

    for (let j = start + 1; j < start + length - 1; j++) {
      result.push(start);
      result.push(j);
      result.push(j + 1);
    }
    start += length;
  }
  return result;
}

export function generateMeshInput(vex: Vec3\[\]\[\]): Vec3\[\] {
  let result: Vec3\[\] = \[\];
  for (let i = 0; i < vex.length; i++) {
    let tmp: Vec3\[\] = vex\[i\];
    for (let j = 0; j < tmp.length; j++) {
      result.push(tmp\[j\]);
    }
  }
  return result;
}
