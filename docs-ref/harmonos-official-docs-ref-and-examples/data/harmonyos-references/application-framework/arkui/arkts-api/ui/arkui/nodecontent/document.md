# NodeContent

**NodeContent** is the ArkUI-provided manager for [ContentSlot](../../../../arkts-components/custom-placeholder-components/contentslot/document.md).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/UUfiY8MbRhecANqtKe4D4A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062230Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4578B932999602177B88EA55A1714ED10AC70F3A6F9235D7ABACCD6A118B3538)

-   The initial APIs of this module are supported since API version 12. Newly added APIs will be marked with a superscript to indicate their earliest API version.
    
-   **NodeContent** objects do not support JSON serialization.
    

#### Modules to Import

import { NodeContent } from '@kit.ArkUI';

#### NodeContent

**NodeContent** is the entity-level encapsulation of node content.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### \[h2\]constructor

constructor()

A constructor used to create a **NodeContent** object.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Example**

import { nativeNode } from 'libNativeNode.so'; // Developer-implemented .so file.
import { NodeContent } from '@kit.ArkUI';

@Component
struct Parent {
  private nodeContent: Content = new NodeContent();

  aboutToAppear() {
    // Create a node through the C API and add it to the nodeContent manager.
    nativeNode.createNativeNode(this.nodeContent);
  }

  build() {
    Column() {
      // Display the native components stored in the nodeContent manager.
      ContentSlot(this.nodeContent)
    }
  }
}

For details about the implementation of the .so file in the preceding code, see [Native XComponent](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/BasicFeature/Native/NativeXComponent).

#### \[h2\]addFrameNode12+

addFrameNode(node: FrameNode): void

Adds a FrameNode to this **NodeContent** object.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| node | [FrameNode](../framenode/document.md) | Yes | FrameNode to add. |

**Error codes**

For details about the error codes, see [Custom Node Error Codes](../../../../error-codes/ui/custom-node-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 100025 | The parameter is invalid. Details about the invalid parameter and the reason are included in the error message. For example: "The parameter 'node' is invalid: it cannot be adopted." |

#### \[h2\]removeFrameNode12+

removeFrameNode(node: FrameNode): void

Removes a FrameNode from this **NodeContent** object.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| node | [FrameNode](../framenode/document.md) | Yes | FrameNode to remove. |

**Example**

This example shows how to add or remove a FrameNode in the **NodeContent** object.

// xxx.ets
import { NodeContent, typeNode } from '@kit.ArkUI';

class NodeContentCtrl {
  content: NodeContent;
  textNode: Array<typeNode.Text> = new Array();
  uiContext: UIContext;
  width: number;

  constructor(uiContext: UIContext) {
    this.content = new NodeContent();
    this.uiContext = uiContext;
    this.width = Infinity;
  }

  AddNode() {
    let node = typeNode.createNode(this.uiContext, "Text");
    node.initialize("ContentText:" + this.textNode.length).fontSize(20);
    this.textNode.push(node);
    this.content.addFrameNode(node);
  }

  RemoveNode() {
    let node = this.textNode.pop();
    this.content.removeFrameNode(node);
  }

  RemoveFront() {
    let node = this.textNode.shift();
    this.content.removeFrameNode(node);
  }

  GetContent(): NodeContent {
    return this.content;
  }
}

@Entry
@Component
struct Index {
  @State message: string = 'Hello World';
  controller = new NodeContentCtrl(this.getUIContext());

  build() {
    Row() {
      Column() {
        ContentSlot(this.controller.GetContent())
        Button("AddToSlot")
          .onClick(() => {
            this.controller.AddNode();
          })
        Button("RemoveBack")
          .onClick(() => {
            this.controller.RemoveNode();
          })
        Button("RemoveFront")
          .onClick(() => {
            this.controller.RemoveFront();
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
