# XComponentNode

The **XComponentNode** module provides APIs for the XComponentNode, which represents an [XComponent](../../../arkts-components/rendering-drawing/xcomponent/document.md) in the component tree. You can write [EGL](../../../../../standard-libraries/egl/document.md)/[OpenGL ES](../../../../../standard-libraries/opengl-es/document.md) and media data and display it on the **XComponent**, whose rendering type can be dynamically modified.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/ojOUrUyoRFaO430uXnwv3w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062231Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=02EFAC3FB3C1344556A6E0EDFF7CC3330576488043AB7AB556CB92C5DB5EEE42)

This module is deprecated since API version 12. You are advised to use the [typeNode of the XComponent type](../../ui/arkui/framenode/document.md#xcomponent12) instead.

The initial APIs of this module are supported since API version 11. Newly added APIs will be marked with a superscript to indicate their earliest API version.

**XComponentNode** is not available in DevEco Studio Previewer.

#### Modules to Import

import { XComponentNode } from "@kit.ArkUI";

#### XComponentNode(deprecated)

#### \[h2\]constructor(deprecated)

constructor(uiContext: UIContext, options: RenderOptions, id: string, type: XComponentType, libraryName?: string)

Constructor used to create an XComponentNode.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/AF7dg9t3RKmWs9cPECeBAw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062231Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=852B487ED4CE0400408B0CED0F699970DC54E7532776C9D018FFBEC5AAA8F502)

This API is supported since API version 11 and deprecated since API version 12. You are advised to use [createNode](../../ui/arkui/framenode/document.md#createnodexcomponent12) instead.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| uiContext | [UIContext](../../ui/ohos-arkui-uicontext-uicontext/class-uicontext/document.md) | Yes | UI context. For details about how to obtain it, see [Obtaining UI Context](../../ui/ohos-arkui-node/document.md#obtaining-ui-context). |
| options | [RenderOptions](../../ui/arkui/buildernode/document.md#renderoptions) | Yes | Parameters for creating an XComponentNode. |
| id | string | Yes | Unique ID of the **XComponent**. The value can contain a maximum of 128 characters. For details, see [XComponent](../../../arkts-components/rendering-drawing/xcomponent/document.md). |
| type | [XComponentType](../../../arkts-components/common-definitions/enums/document.md#xcomponenttype10) | Yes | Type of the **XComponent**. For details, see [XComponent](../../../arkts-components/rendering-drawing/xcomponent/document.md). |
| libraryName | string | No | Name of the dynamic library generated during compilation at the native layer. For details, see [XComponent](../../../arkts-components/rendering-drawing/xcomponent/document.md). |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/syQxY--wRemcks319eSGtQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062231Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=11E3E24C11C1CD720DAAF067C037C8794F940AF6836729694B46CEBFE3C34B95)

You need to explicitly specify **selfIdealSize** in [RenderOptions](../../ui/arkui/buildernode/document.md#renderoptions). Otherwise, the XComponentNode's content size is empty, resulting in no content being displayed.

#### \[h2\]onCreate(deprecated)

onCreate(event?: Object): void

Called when the XComponentNode loading is complete.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/SEQAAEMGQ2Sw1-kTjj1gPg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062231Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2A796BC73080C68E9CA4D42CAC305C8193860726D9087F566D0D25E27A89DB3A)

This API is supported since API version 11 and deprecated since API version 12. You are advised to use [onLoad](../../../arkts-components/rendering-drawing/xcomponent/document.md#onload) instead.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | Object | No | Context of the **XComponent** object. The APIs contained in the context are defined at the C++ layer by developers. |

#### \[h2\]onDestroy(deprecated)

onDestroy(): void

Called when the XComponentNode is destroyed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/VI7xiqa1QgqNrWjy7G_SXQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062231Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=84CC4AF3AA1DDF2969D02AAB68CAB29E7837B9BA8A8507C524FAD41F4C78F676)

This API is supported since API version 11 and deprecated since API version 12. You are advised to use [onDestroy](../../../arkts-components/rendering-drawing/xcomponent/document.md#ondestroy) instead.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### \[h2\]changeRenderType(deprecated)

changeRenderType(type: NodeRenderType): boolean

Changes the rendering type of the XComponentNode.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/bU3tZhc3R-2Rr8_oaIH1ZQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062231Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3A75EA26451D6D370BF20B4BFFECD133637A29B40725D9986D1F3E77449CD08B)

This API is supported since API version 11 and deprecated since API version 12. You are advised to use [appendChild](../../ui/arkui/framenode/document.md#appendchild12) instead.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [NodeRenderType](../../ui/arkui/buildernode/document.md#noderendertype) | Yes | Target rendering type. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | 
Whether the rendering type is changed successfully.

**true**: The rendering type is changed successfully. **false**: The rendering type fails to be changed.

 |

#### Example

import { NodeController, FrameNode, XComponentNode, NodeRenderType, UIContext} from '@kit.ArkUI'

class XComponentNodeController extends NodeController {
  private xComponentNode: MyXComponentNode | null = null;
  private soName: string = "tetrahedron\_napi" // This .so file is written and generated by you using the Node-API.

  constructor() {
    super();
  }

  makeNode(context: UIContext): FrameNode | null {
    this.xComponentNode = new MyXComponentNode(context, {
      selfIdealSize: { width: 200, height: 200 }
    }, "xComponentId", XComponentType.SURFACE, this.soName);
    return this.xComponentNode;
  }

  changeRenderType(renderType: NodeRenderType): void {
    if (this.xComponentNode) {
      this.xComponentNode.changeRenderType(renderType);
    }
  }
}

class MyXComponentNode extends XComponentNode {
  onCreate(event: Object) {
    // do something when XComponentNode has created
  }

  onDestroy() {
    // do something when XComponentNode is destroying
  }
}

@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        NodeContainer(new XComponentNodeController())
      }
      .width('100%')
      .height('100%')
    }
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/tzO3GfUOSlew6DaYG7Hfeg/en-us_image_0000002537765374.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062231Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=59A845B46E41550478047F1472F1BFE72CD1F27D38053820840C69FF84A6002A)
