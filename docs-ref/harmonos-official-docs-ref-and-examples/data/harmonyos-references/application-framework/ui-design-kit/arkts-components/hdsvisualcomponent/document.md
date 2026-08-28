# HdsVisualComponent

**HdsVisualComponent** is used to implement complex visual effects. You can select specific visual effect scenes through **HdsVisualComponent** to develop corresponding complex visual effects.

**Start version**: 6.0.0(20)

#### Modules to Import

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/Wr0fYwxfS2i_KVqg8qORKg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062329Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9CB235F72A5582A3938B4EB5D16DA52BECDBB6ACB1E1C55938337566B059DFE6)

-   **HdsVisualComponentAttribute** is essential for configuring the **HdsVisualComponent** component. In version 6.0.1(21) and earlier, you must manually import **HdsVisualComponentAttribute** after importing the **HdsVisualComponent** component. Otherwise, a compilation error is reported. However, starting from version 6.0.2(22), the compilation toolchain automatically imports **HdsVisualComponentAttribute** when it detects the **HdsVisualComponent** component, so manual import is no longer necessary.
-   If you manually import **HdsVisualComponentAttribute**, DevEco Studio shows it as disabled (grayed out). In version 6.0.1(21) and earlier, removing this import causes a compilation error. But from version 6.0.2(22) onward, removing it does not affect the functionality.

Version 6.0.1(21) and earlier:

import { HdsVisualComponent, HdsVisualComponentAttribute, HdsSceneController, HdsSceneType, hdsEffect } from '@kit.UIDesignKit';

Version 6.0.2(22) and later:

import { HdsVisualComponent, HdsSceneController, HdsSceneType, hdsEffect } from '@kit.UIDesignKit';

#### Child Components

None

#### API

HdsVisualComponent()

Creates a common visual effect component **HdsVisualComponent**.

**Widget capability**: This API can be used in ArkTS widgets since version 6.0.2(22).

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Start version**: 6.0.0(20)

#### Attributes

In addition to [universal attributes](../../../arkui/arkts-components/universal-attributes/document.md), the following attributes are supported.

#### scene

scene(sceneType: HdsSceneType, controller: HdsSceneController, callback?: HdsSceneFinishCallback, frameRateRange?: hdsEffect.ExpectedFrameRateRange)

Sets a visual effect scene.

**Widget capability**: This API can be used in ArkTS widgets since version 6.0.2(22).

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Start version**: 6.0.0(20)

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

sceneType

 | 

[HdsSceneType](#section92774418495)

 | 

Yes

 | 

Visual effect scene type.

 |
| 

controller

 | 

[HdsSceneController](#section19696213112)

 | 

Yes

 | 

Visual effect scene controller.

 |
| 

callback

 | 

[HdsSceneFinishCallback](#section010418487170)

 | 

No

 | 

Triggered when the visual effect scene ends.

 |
| 

frameRateRange

 | 

hdsEffect.[ExpectedFrameRateRange](../../arkts-apis/hdseffect/document.md#section19809172171211)

 | 

No

 | 

Frame rate range for the visual effect scene.

 |

#### Events

[Universal events](../../../arkui/arkts-components/universal-events/document.md) are supported.

#### HdsSceneType

Sets a visual effect scene.

**Widget capability**: This API can be used in ArkTS widgets since version 6.0.2(22).

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Start version**: 6.0.0(20)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

DUAL\_EDGE\_FLOW\_LIGHT\_WITH\_BACKGROUND\_MASK

 | 

0

 | 

Dual-edge flowing light effect with a background.

NOTE:

This effect does not apply for TVs.

 |

#### HdsSceneFinishCallback

type HdsSceneFinishCallback = () => void

Defines the callback triggered upon visual effect animation ending.

**Widget capability**: This API can be used in ArkTS widgets since version 6.0.2(22).

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Start version**: 6.0.0(20)

#### HdsSceneController

Scene controller.

**Widget capability**: This API can be used in ArkTS widgets since version 6.0.2(22).

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Start version**: 6.0.0(20)

#### \[h2\]constructor

constructor()

Constructor for **HdsSceneController**.

**Widget capability**: This API can be used in ArkTS widgets since version 6.0.2(22).

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Start version**: 6.0.0(20)

#### \[h2\]start

start(): void

Starts the animation of a visual effect scene.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Start version**: 6.0.0(20)

#### \[h2\]pause

pause(): void

Pauses the animation of a visual effect scene.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Start version**: 6.0.0(20)

#### \[h2\]resume

resume(): void

Resumes the animation of a visual effect scene.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Start version**: 6.0.0(20)

#### \[h2\]stop

stop(): void

Stops the animation of a visual effect scene.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Start version**: 6.0.0(20)

#### \[h2\]setSceneParams

setSceneParams(params: SceneParams): HdsSceneController

Sets visual effect scene parameters.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Start version**: 6.0.0(20)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

params

 | 

[SceneParams](#section1636545113020)

 | 

Yes

 | 

Scene parameters.

 |

**Returns:**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[HdsSceneController](#section19696213112)

 | 

[HdsSceneController](#section19696213112) object.

 |

#### SceneParams

type SceneParams = DualEdgeFlowLightWithMaskParam

Sets visual effect scene parameters.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Start version**: 6.0.0(20)

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[DualEdgeFlowLightWithMaskParam](#section12461104631817)

 | 

Dual-edge flowing light effect parameters.

 |

#### DualEdgeFlowLightWithMaskParam

Defines dual-edge flowing light effect parameters.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Start version**: 6.0.0(20)

| 
**Name**

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

backgroundMaskColors

 | 

Array<[ResourceColor](../../../arkui/arkts-components/common-definitions/basic-types/document.md#resourcecolor)\>

 | 

No

 | 

No

 | 

Background overlay color array.

 |
| 

firstEdgeFlowLight

 | 

hdsEffect.[EdgeFlowLightParam](../../arkts-apis/hdseffect/document.md#section63471415181915)

 | 

No

 | 

No

 | 

Parameters of the first flowing light edge.

 |
| 

secondEdgeFlowLight

 | 

hdsEffect.[EdgeFlowLightParam](../../arkts-apis/hdseffect/document.md#section63471415181915)

 | 

No

 | 

No

 | 

Parameters of the second flowing light edge.

 |

#### Example

// Starting from version 6.0.2(22), you do not need to manually import HdsVisualComponentAttribute. For details, refer to the "Modules to Import" section of the HdsVisualComponent reference document.
import { HdsVisualComponent, HdsVisualComponentAttribute, HdsSceneController, HdsSceneType } from '@kit.UIDesignKit';

@Entry
@Component
struct EdgeFlowLightVisualComponent {
  @State sceneController: HdsSceneController = new HdsSceneController()
    .setSceneParams({
      backgroundMaskColors: \[Color.Green, Color.Red\],
      firstEdgeFlowLight: {
        startPos: 0,
        endPos: 0.5,
        color: Color.Red
      },
      secondEdgeFlowLight: {
        startPos: 0,
        endPos: -0.5,
        color: Color.Green
      }
    })

  build() {
    Stack() {
      HdsVisualComponent()
        .scene(HdsSceneType.DUAL\_EDGE\_FLOW\_LIGHT\_WITH\_BACKGROUND\_MASK, this.sceneController, () => {
          console.info('Succeeded in finishing');
        })
        .width('100%')
        .height('50%')
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/a597YlbjQUGMbAmz-yrQ6A/en-us_image_0000002532144143.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062329Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BEB705D5C3CE0A4903435731BA26A4E877CD06D0888362B4F061B7ED7383CD61 "Click to enlarge")
