# ContentSlot

The **ContentSlot** component is a component designed to render and manage components created on the native layer using C APIs.

With support for hybrid development, the **ContentSlot** component is recommended when the container is an ArkTS component and the child component is created on the native side.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0d/v3/r7QjDI51RHOOID7pECKh8A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062249Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=88B55153B885F2D75AB149C67D36F97269C7AD0370591553135C4F6B9C245779)

The initial APIs of this module are supported since API version 12. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### APIs

ContentSlot(content: Content)

Called when content is added to a placeholder component

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| content | [Content](#content) | Yes | Manager of the **ContentSlot** component. Through the APIs provided by the native side, it can register and trigger the attach and detach event callbacks for **ContentSlot**, as well as manage the child components of **ContentSlot**. |

#### Content

type Content = Content

Defines a base class for **ComponentContent** and **NodeContent**.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Type | Description |
| :-- | :-- |
| [Content](../../../arkts-api/ui/arkui/content/document.md) | Base class for **ComponentContent** and **NodeContent**. |

#### Example

The following example shows the basic usage of **ContentSlot**.

import { nativeNode } from 'libNativeNode.so'; // Developer-implemented .so file.
import { NodeContent } from '@kit.ArkUI';

@Entry
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

For details about the implementation of the .so file in the preceding code, see [Native XComponent](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/BasicFeature/Native/NdkXComponent).
