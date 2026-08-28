# @ohos.arkui.node

The **Node** module provides level-2 module APIs of custom nodes to export and use.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/IYz3qzP5ToqPPMdjJkuJAg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062226Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FCA01FFAF714150B7CA6328E42B94D8A66473360BDFF36829A67FBCF508538E1)

-   The initial APIs of this module are supported since API version 11. Newly added APIs will be marked with a superscript to indicate their earliest API version.
    
-   Custom nodes are not available in DevEco Studio Previewer.
    

#### BuilderNode

The [BuilderNode](../arkui/buildernode/document.md) module provides APIs for creating a BuilderNode – a custom node that can be used to mount built-in components. Avoid mounting a BuilderNode as a child node to other custom nodes.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### FrameNode

The [FrameNode](../arkui/framenode/document.md) module provides APIs for a FrameNode, which represents an entity node in the component tree. It can be used by a [NodeController](../arkui/nodecontroller/document.md) to mount a [BuilderNode](../arkui/buildernode/document.md) (that holds the FrameNode) to a [NodeContainer](../../../arkts-components/custom-placeholder-components/nodecontainer/document.md) or mount a [RenderNode](../arkui/rendernode/document.md) to another FrameNode.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### NodeController

The [NodeController](../arkui/nodecontroller/document.md) module provides APIs for managing custom nodes, such as creating, showing, and updating custom nodes, and APIs for mounting custom nodes to a [NodeContainer](../../../arkts-components/custom-placeholder-components/nodecontainer/document.md) component.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### Graphics

[Graphics](../arkui/graphics/document.md) module: provides APIs for defining attributes of a custom node.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### RenderNode

The [RenderNode](../arkui/rendernode/document.md) module provides APIs for creating a RenderNode in custom drawing settings with C APIs.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### XComponentNode

The [XComponentNode](../../apis-no-longer-maintained/xcomponentnode/document.md) module provides APIs a XComponentNode, an **XComponent** in the component tree. You can write EGL/OpenGL ES and media data and display it on the **XComponent**, whose rendering type can be dynamically modified.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### Obtaining UI Context

To obtain the UI context, use any of the following methods:

1.  Call [getUIContext()](../../window-manager/ohos-window-window/interface-window/document.md#getuicontext10) in **ohos.window** to obtain the \*\*UIContext \*\*instance.
    
2.  Call the built-in method [getUIContext()](../../../arkts-components/custom-components/custom-component-built-in-apis/document.md#getuicontext) of the custom component.
    
3.  Use the [makeNode](../arkui/nodecontroller/document.md#makenode) callback of [NodeController](../arkui/nodecontroller/document.md).
