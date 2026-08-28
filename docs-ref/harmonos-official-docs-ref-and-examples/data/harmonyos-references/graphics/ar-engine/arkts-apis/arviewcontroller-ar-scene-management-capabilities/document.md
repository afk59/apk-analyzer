# arViewController (AR Scene Management Capabilities)

This module provides APIs related to arViewController (AR scene management capabilities) of AR Engine.

The basic core capabilities include AR session management, spatial object management, and scene-based management.

**System capability**: SystemCapability.AREngine.Core

**Start version**: 5.1.0(18)

#### Modules to Import

import { arEngine, arViewController } from '@kit.AREngine';

#### ARViewContext

Defines the ARView context, which is used to manage AR scenes, including initialization, suspension, resumption, and destruction.

**System capability**: SystemCapability.AREngine.Core

**Start version**: 5.1.0(18)

#### \[h2\]ARViewContext.init

init(): Promise<void>

Initializes [ARViewContext](#section12681656121519) to initialize the AR session and configure the AR rendering scene, among other tasks.

This API returns the result asynchronously through a promise.

**Required permissions**: ohos.permission.CAMERA and ohos.permission.GYROSCOPE and ohos.permission.ACCELEROMETER

**System capability**: SystemCapability.AREngine.Core

**Start version**: 5.1.0(18)

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

Promise<void>

 | 

Promise object that returns no value.

 |

**Error codes**:

For details about the error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [AR Engine Error Codes](../../ar-engine-error-codes/document.md).

| 
**Error Code**

 | 

**Error Message**

 |
| :-- | :-- |
| 

201

 | 

Permissions not granted, such as the camera permission.

 |
| 

801

 | 

Device not compatible.

 |
| 

1009200001

 | 

Failure.

 |
| 

1009200007

 | 

Configuration not supported.

 |
| 

1009200008

 | 

Resource exhausted.

 |
| 

1009200009

 | 

Service unavailable.

 |
| 

1009200010

 | 

Camera unavailable.

 |
| 

1009200201

 | 

ARView invalid operation.

 |
| 

1009200202

 | 

Graphics3D AR scene required.

 |
| 

1009200203

 | 

AREngine config required.

 |
| 

1009200204

 | 

AR session setup failed.

 |
| 

1009200205

 | 

AR scene camera setup failed.

 |

**Example**:

import { arViewController } from '@kit.AREngine';
import { BusinessError } from '@kit.BasicServicesKit';

let context: arViewController.ARViewContext = new arViewController.ARViewContext();
context.init().then(() => {
  console.info('Initialization successful.');
}).catch((error: BusinessError) => {
  console.error(\`Initialization failed. error code: ${error.code}\`);
})

#### \[h2\]ARViewContext.pause

pause(): void

Pauses camera tracking and AR scene rendering.

**System capability**: SystemCapability.AREngine.Core

**Start version**: 5.1.0(18)

**Error codes**:

For details about the error codes, please refer to [AR Engine Error Codes](../../ar-engine-error-codes/document.md).

| 
**Error Code**

 | 

**Error Message**

 |
| :-- | :-- |
| 

1009200001

 | 

Failure.

 |
| 

1009200201

 | 

ARView invalid operation.

 |
| 

1009200204

 | 

AR session setup failed.

 |

**Example**:

import { arViewController } from '@kit.AREngine';

let context: arViewController.ARViewContext = new arViewController.ARViewContext();
context.pause();

#### \[h2\]ARViewContext.destroy

destroy(): Promise<void>

Destroys [ARViewContext](#section12681656121519) to release the resources used by ARView, including terminating the AR session and dismantling the presented scene. This should be used when exiting ARView.

This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.AREngine.Core

**Start version**: 5.1.0(18)

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

Promise<void>

 | 

Promise object that returns no value.

 |

**Error codes**:

For details about the error codes, please refer to [AR Engine Error Codes](../../ar-engine-error-codes/document.md).

| 
**Error Code**

 | 

**Error Message**

 |
| :-- | :-- |
| 

1009200001

 | 

Failure.

 |
| 

1009200201

 | 

ARView invalid operation.

 |
| 

1009200204

 | 

AR session setup failed.

 |

**Example**:

import { arViewController } from '@kit.AREngine';
import { BusinessError } from '@kit.BasicServicesKit';

let context: arViewController.ARViewContext = new arViewController.ARViewContext();
context.destroy().then(() => {
  console.info('Destruction successful.');
}).catch((error: BusinessError) => {
  console.error(\`Destruction failed. error code: ${error.code}\`);
})

#### \[h2\]ARViewContext.resume

resume(): void

Resumes paused camera tracking and AR scene rendering.

**System capability**: SystemCapability.AREngine.Core

**Start version**: 5.1.0(18)

**Error codes**:

For details about the error codes, please refer to [AR Engine Error Codes](../../ar-engine-error-codes/document.md).

| 
**Error Code**

 | 

**Error Message**

 |
| :-- | :-- |
| 

1009200001

 | 

Failure.

 |
| 

1009200010

 | 

Camera unavailable.

 |
| 

1009200201

 | 

ARView invalid operation.

 |
| 

1009200204

 | 

AR session setup failed.

 |

**Example**:

import { arViewController } from '@kit.AREngine';

let context: arViewController.ARViewContext = new arViewController.ARViewContext();
context.resume();

#### \[h2\]ARViewContext.scene

set scene(scene: Scene)

Sets the AR scene of ARView.

**System capability**: SystemCapability.AREngine.Core

**Start version**: 5.1.0(18)

**Parameters**:

| 
**Parameter**

 | 

Type

 | 

**Mandatory**

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

scene

 | 

[Scene](../../../arkgraphics-3d/arkts-apis/graphics3d/scene/document.md#scene-1)

 | 

Yes

 | 

AR presentation scene, which is used to manage spatial nodes.

 |

**Error codes**:

For details about the error codes, please refer to [AR Engine Error Codes](../../ar-engine-error-codes/document.md).

| 
**Error Code**

 | 

**Error Message**

 |
| :-- | :-- |
| 

1009200201

 | 

ARView invalid operation.

 |

**Example**:

import { Scene } from '@kit.ArkGraphics3D';
import { arViewController } from '@kit.AREngine';

Scene.load().then((scene: Scene) => {
  let context: arViewController.ARViewContext = new arViewController.ARViewContext();
  context.scene = scene;
})

#### \[h2\]ARViewContext.scene

get scene(): Scene

Obtains the AR scene for managing spatial nodes.

**System capability**: SystemCapability.AREngine.Core

**Start version**: 5.1.0(18)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[Scene](../../../arkgraphics-3d/arkts-apis/graphics3d/scene/document.md#scene-1)

 | 

AR presentation scene, which is used to manage spatial nodes.

 |

**Error codes**:

For details about the error codes, please refer to [AR Engine Error Codes](../../ar-engine-error-codes/document.md).

| 
**Error Code**

 | 

**Error Message**

 |
| :-- | :-- |
| 

1009200201

 | 

ARView invalid operation.

 |

**Example**:

import { Scene } from '@kit.ArkGraphics3D';
import { arViewController } from '@kit.AREngine';

let context: arViewController.ARViewContext = new arViewController.ARViewContext();
let scene: Scene = context.scene;

#### \[h2\]ARViewContext.session

get session(): arEngine.ARSession | undefined

Obtains AR sessions, which are used to obtain AR environment tracking, camera tracking, hit testing, and other capabilities, such as camera pose, plane information, and anchor creation.

**System capability**: SystemCapability.AREngine.Core

**Start version**: 5.1.0(18)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[arEngine](../arengine-ar-capabilities/document.md).[ARSession](../arengine-ar-capabilities/document.md#section19193165314510) | undefined

 | 

AR session content obtained. If the AR session is set successfully, **arEngine.ARSession** is returned. If ARViewContext fails to be initialized due to an abnormal setting or operation, **undefined** is returned.

 |

**Example**:

import { arEngine, arViewController } from '@kit.AREngine';

let context: arViewController.ARViewContext = new arViewController.ARViewContext();
let arSession: arEngine.ARSession | undefined = context.session;

#### \[h2\]ARViewContext.config

set config(conf: arEngine.ARConfig)

Sets the AR session configuration files, including north-facing coordinates, performance modes, and more.

**System capability**: SystemCapability.AREngine.Core

**Start version**: 5.1.0(18)

**Parameters**:

| 
**Parameter**

 | 

Type

 | 

**Mandatory**

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

conf

 | 

[arEngine](../arengine-ar-capabilities/document.md).[ARConfig](../arengine-ar-capabilities/document.md#section1262116345111)

 | 

Yes

 | 

Configuration parameters of [ARSession](../arengine-ar-capabilities/document.md#section19193165314510).

 |

**Error codes**:

For details about the error codes, please refer to [AR Engine Error Codes](../../ar-engine-error-codes/document.md).

| 
**Error Code**

 | 

**Error Message**

 |
| :-- | :-- |
| 

1009200201

 | 

ARView invalid operation.

 |

**Example**:

import { arEngine, arViewController } from '@kit.AREngine';

let context: arViewController.ARViewContext = new arViewController.ARViewContext();
context.config = {
  type: arEngine.ARType.WORLD,
  poseMode: arEngine.ARPoseMode.GRAVITY\_AND\_HEADING,
  powerMode: arEngine.ARPowerMode.POWER\_SAVING,
  depthMode: arEngine.ARDepthMode.AUTOMATIC
}

#### \[h2\]ARViewContext.callback

set callback(callback: ARViewCallback);

Sets callback function to implement corresponding service logic via callback.

**System capability**: SystemCapability.AREngine.Core

**Start version**: 5.1.0(18)

**Parameters**:

| 
**Parameter**

 | 

Type

 | 

**Mandatory**

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

callback

 | 

[ARViewCallback](#section9396615174614)

 | 

Yes

 | 

Abstract class of ARViewCallback, which declares the callback API of ARView.

 |

**Error codes**:

For details about the error codes, please refer to [AR Engine Error Codes](../../ar-engine-error-codes/document.md).

| 
**Error Code**

 | 

**Error Message**

 |
| :-- | :-- |
| 

1009200201

 | 

ARView invalid operation.

 |

**Example**:

import { arEngine, arViewController } from '@kit.AREngine';
import { Node } from '@kit.ArkGraphics3D';

class ARViewCallbackImpl extends arViewController.ARViewCallback {

  onAnchorAdd(ctx: arViewController.ARViewContext, node: Node, anchor: arEngine.ARAnchor): void {
    console.info('onAnchorAdd');
    console.info(\`add anchor id = ${String(anchor.id)}\`);
    console.info(\`add anchor translation = ${anchor.getPose().translation}\`);
    console.info(\`add node pose = ${node.position}\`);
  }

  onAnchorUpdate(ctx: arViewController.ARViewContext, node: Node, anchor: arEngine.ARAnchor): void {
    console.info('onAnchorUpdate');
    console.info(\`update anchor id = ${String(anchor.id)}\`);
    console.info(\`update anchor translation = ${anchor.getPose().translation}\`);
    console.info(\`update node pose = ${node.position}\`);
  }

  onFrameUpdate(ctx: arViewController.ARViewContext, sysBootTs: number): void {
    let arSession: arEngine.ARSession | undefined = ctx.session;
    if (arSession) {
      let frame = arSession.getFrame();
      if (!frame) {
        console.error('Failed to get arSession.frame, it is undefined or null');
      } else {
        console.info(\`Succeeded in getting arSession.frame = ${frame.timestamp}\`);
        await frame.release();
      }
    } else {
      console.error('Failed to get arSession, arSession is undefined');
    }
  }
}

let context: arViewController.ARViewContext = new arViewController.ARViewContext();
context.callback = new ARViewCallbackImpl();

#### ARViewCallback

Abstract class of **ARViewCallback**, which declares the callback API of ARView.

You need to inherit this class and implement the callback subclass based on the service logic.

**System capability**: SystemCapability.AREngine.Core

**Start version**: 5.1.0(18)

#### \[h2\]ARViewCallback.onAnchorAdd

abstract onAnchorAdd(ctx: ARViewContext, node: Node, anchor: arEngine.ARAnchor): void

When a new plane is detected in an AR session, an anchor and a corresponding scene node are automatically created for the plane, and this callback function is automatically triggered in the frame refresh logic.

**System capability**: SystemCapability.AREngine.Core

**Start version**: 5.1.0(18)

**Parameters**:

| 
**Parameter**

 | 

Type

 | 

**Mandatory**

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

ctx

 | 

[ARViewContext](#section12681656121519)

 | 

Yes

 | 

Context information (ARViewContext) of ARView.

 |
| 

node

 | 

[Node](../../../arkgraphics-3d/arkts-apis/graphics3d/scenenode/document.md#node)

 | 

Yes

 | 

AR scene node corresponding to the new anchor.

CAUTION:

Nodes belong to the Ark Graphics Platform (AGP) rendering engine and use the AGP-aligned world coordinate system, which is different from the gravity-aligned world coordinate system used by AR Engine. You need to distinguish between the two when using the **anchor** parameter. For details, please refer to [AR Engine Gravity Aligned with World Coordinate System](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arengine-coordinate#section51232054151614) and [AGP World Coordinate System](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arengine-coordinate#section7594451483).

 |
| 

anchor

 | 

[arEngine](../arengine-ar-capabilities/document.md).[ARAnchor](../arengine-ar-capabilities/document.md#section106411242143016)

 | 

Yes

 | 

Anchor created for the new plane.

CAUTION:

The pose of [ARAnchor](../arengine-ar-capabilities/document.md#section106411242143016) uses the gravity-aligned world coordinate system of AR Engine. For details, please refer to [AR Engine Gravity Aligned with World Coordinate System](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arengine-coordinate#section51232054151614).

 |

**Example**:

import { arEngine, arViewController } from '@kit.AREngine';
import { Node } from '@kit.ArkGraphics3D';

// Create a callback class by referring to the sample code of the ARViewContext.callback API and then implement this API.
onAnchorAdd(ctx: arViewController.ARViewContext, node: Node, anchor: arEngine.ARAnchor): void {
  // Other operations.
}

#### \[h2\]ARViewCallback.onAnchorUpdate

abstract onAnchorUpdate(ctx: ARViewContext, node: Node, anchor: arEngine.ARAnchor): void

Called when ARView automatically detects the scene node corresponding to the anchor and calls the callback function after the anchor in the AR session is updated.

**System capability**: SystemCapability.AREngine.Core

**Start version**: 5.1.0(18)

**Parameters**:

| 
**Parameter**

 | 

Type

 | 

**Mandatory**

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

ctx

 | 

[ARViewContext](#section12681656121519)

 | 

Yes

 | 

Context information (ARViewContext) of ARView.

 |
| 

node

 | 

[Node](../../../arkgraphics-3d/arkts-apis/graphics3d/scenenode/document.md#node)

 | 

Yes

 | 

AR scene node corresponding to the new anchor.

CAUTION:

Nodes belong to the Ark Graphics Platform (AGP) rendering engine and use the AGP-aligned world coordinate system, which is different from the gravity-aligned world coordinate system used by AR Engine. You need to distinguish between the two when using the **anchor** parameter. For details, please refer to [AR Engine Gravity Aligned with World Coordinate System](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arengine-coordinate#section51232054151614) and [AGP World Coordinate System](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arengine-coordinate#section7594451483).

 |
| 

anchor

 | 

[arEngine](../arengine-ar-capabilities/document.md).[ARAnchor](../arengine-ar-capabilities/document.md#section106411242143016)

 | 

Yes

 | 

Anchor to be updated.

CAUTION:

The pose of [ARAnchor](../arengine-ar-capabilities/document.md#section106411242143016) uses the gravity-aligned world coordinate system of AR Engine. For details, please refer to [AR Engine Gravity Aligned with World Coordinate System](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arengine-coordinate#section51232054151614).

 |

**Example**:

import { arEngine, arViewController } from '@kit.AREngine';
import { Node } from '@kit.ArkGraphics3D';

// Create a callback class by referring to the sample code of the ARViewContext.callback API and then implement this API.
onAnchorUpdate(ctx: arViewController.ARViewContext, node: Node, anchor: arEngine.ARAnchor): void {
  // Other operations.
}

#### \[h2\]ARViewCallback.onFrameUpdate

abstract onFrameUpdate(ctx: ARViewContext, sysBootTs: number): void

Automatically triggered before each frame is refreshed in an AR scene. You can adjust the placement pose of AR entities, animations, and camera pose based on this callback.

**System capability**: SystemCapability.AREngine.Core

**Start version**: 5.1.0(18)

**Parameters**:

| 
**Parameter**

 | 

Type

 | 

**Mandatory**

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

ctx

 | 

[ARViewContext](#section12681656121519)

 | 

Yes

 | 

Context information of ARView.

 |
| 

sysBootTs

 | 

number

 | 

Yes

 | 

Timestamp, in microseconds.

 |

**Example**:

import { arEngine, arViewController } from '@kit.AREngine';

// Create a callback class by referring to the sample code of the ARViewContext.callback API and then implement this API.
onFrameUpdate(ctx: arViewController.ARViewContext, sysBootTs: number): void {
  let arSession: arEngine.ARSession | undefined = ctx.session;
  if (arSession) {
    let frame = arSession.getFrame();
    if (!frame){
      console.error('Failed to get arSession.frame, it is undefined or null');
    } else {
      console.info(\`Succeeded in getting arSession.frame = ${frame.timestamp}\`);
      await frame.release();
    }
  } else {
    console.error('Failed to get arSession, arSession is undefined');
  }
}
