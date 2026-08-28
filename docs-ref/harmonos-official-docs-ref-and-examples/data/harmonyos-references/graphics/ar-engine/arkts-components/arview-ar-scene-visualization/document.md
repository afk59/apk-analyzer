# ARView (AR Scene Visualization)

Carries ARViewContext to implement AR scene visualization.

This API must be used together with [arViewController (AR Scene Management Capabilities)](../../arkts-apis/arviewcontroller-ar-scene-management-capabilities/document.md) to implement AR scene visualization.

**System capability**: SystemCapability.AREngine.Core

**Start version**: 5.1.0(18)

#### Module Import

import { ARView, arViewController } from '@kit.AREngine';

#### ARView

This class is a visual display component for AR scenes.

**Decorator type**: @Component

**System capability**: SystemCapability.AREngine.Core

**Start version**: 5.1.0(18)

**Parameter**

| 
**Parameter**

 | 

Type

 | 

**Mandatory**

 | 

**Decorator Type**

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

context

 | 

[arViewController](../../arkts-apis/arviewcontroller-ar-scene-management-capabilities/document.md).[ARViewContext](../../arkts-apis/arviewcontroller-ar-scene-management-capabilities/document.md#section12681656121519)

 | 

Yes

 | 

@Require

@State

 | 

Manages the ARView context, AR session, and scene status.

 |

#### \[h2\]build

**build** (): **void**

Constructor used to create an **ARView** object.

**System capability**: SystemCapability.AREngine.Core

**Start version**: 5.1.0(18)

**Example**:

import { ARView, arViewController } from '@kit.AREngine';

let arContext: arViewController.ARViewContext = new arViewController.ARViewContext();

@Entry
@Component
struct ARWorld {
  // Configure and initialize context.
  build() {
    RelativeContainer() {
      if (arContext) {
        ARView({ context: arContext })
          .height('100%')
          .width('100%')
      }
    }
  }
}
