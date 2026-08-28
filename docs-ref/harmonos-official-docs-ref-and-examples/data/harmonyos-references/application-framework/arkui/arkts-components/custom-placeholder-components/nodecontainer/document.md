# NodeContainer

**NodeContainer** is a basic component for mounting custom nodes (such as [FrameNode](../../../arkts-api/ui/arkui/framenode/document.md) or [BuilderNode](../../../arkts-api/ui/arkui/buildernode/document.md)) and dynamically managing node attachment and detachment through [NodeController](../../../arkts-api/ui/arkui/nodecontroller/document.md). This component does not support adding trailing child components and requires a [NodeController](../../../arkts-api/ui/arkui/nodecontroller/document.md) instance for operation. It must be used in combination with **NodeController**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/YMr-hftNSGS2-WCU4XLB6w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062249Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=412AE4B134D47E0F5FFF7AFFA20187A0DE3E11C5C162048C2F35E436D3BC7BD9)

This component is supported since API version 11. Updates will be marked with a superscript to indicate their earliest API version.

Only custom [FrameNodes](../../../arkts-api/ui/arkui/framenode/document.md) or the root FrameNode obtained from a [BuilderNode](../../../arkts-api/ui/arkui/buildernode/document.md) can be attached to this component.

[Proxy nodes](../../../arkts-api/ui/arkui/framenode/document.md#ismodifiable12) of built-in system components obtained through querying cannot be attached to this component.

This component does not work with the [attribute modifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md).

A [UIContext](../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-uicontext/document.md) instance is used to construct the node tree for this component. During instance switching, the input parameter of the [makeNode](../../../arkts-api/ui/arkui/nodecontroller/document.md#makenode) callback method of the bound [NodeController](../../../arkts-api/ui/arkui/nodecontroller/document.md) may be **undefined** due to instance mismatch. Therefore, this component does not support cross-instance node reuse.

When this component is not destroyed, the unmounting of its mounted child nodes will not be triggered.

#### Child Components

Not supported

#### APIs

#### \[h2\]NodeContainer

NodeContainer(controller: NodeController)

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| controller | [NodeController](../../../arkts-api/ui/arkui/nodecontroller/document.md) | Yes | **NodeController** instance used to control the upper and lower tree nodes in the **NodeContainer**. It represents the lifecycle of the **NodeContainer**. |

#### Attributes

The [universal attributes](../../universal-attributes/document.md) are supported.

#### Events

The [universal events](../../universal-events/document.md) are supported.

#### Example

This example demonstrates how to mount a BuilderNode through **NodeController**.

import { NodeController, BuilderNode, FrameNode, UIContext } from '@kit.ArkUI';

declare class Params {
  text: string
}

@Builder
function buttonBuilder(params: Params) {
  Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.SpaceEvenly }) {
    Text(params.text)
      .fontSize(12)
    Button(\`This is a Button\`, { type: ButtonType.Normal, stateEffect: true })
      .fontSize(12)
      .borderRadius(8)
      .backgroundColor(0x317aff)
  }
  .height(100)
  .width(200)
}

class MyNodeController extends NodeController {
  private rootNode: BuilderNode<\[Params\]> | null = null;
  private wrapBuilder: WrappedBuilder<\[Params\]> = wrapBuilder(buttonBuilder);

  makeNode(uiContext: UIContext): FrameNode | null {
    if (this.rootNode === null) {
      this.rootNode = new BuilderNode(uiContext);
      this.rootNode.build(this.wrapBuilder, { text: "This is a Text" })
    }
    return this.rootNode.getFrameNode();
  }
}

@Entry
@Component
struct Index {
  private baseNode: MyNodeController = new MyNodeController()

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Start, justifyContent: FlexAlign.SpaceEvenly }) {
      Text("This is a NodeContainer contains a text and a button ")
        .fontSize(9)
        .fontColor(0xCCCCCC)
      NodeContainer(this.baseNode)
        .borderWidth(1)
        .onClick(() => {
          console.info("click event");
        })
    }
    .padding({ left: 35, right: 35, top: 35 })
    .height(200)
    .width(300)
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/sHhQJPRHRAqRpjsRT3B19A/en-us_image_0000002568685669.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062249Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F415C12939A41E1C5FCC9AD3C96D232DA932C9F61014369259A36B59AECA2E71)
