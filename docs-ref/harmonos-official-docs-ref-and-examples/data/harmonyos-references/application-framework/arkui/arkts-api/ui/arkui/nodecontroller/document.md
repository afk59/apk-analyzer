# NodeController

The **NodeController** module provides APIs for managing custom nodes, such as creating, showing, and updating custom nodes, and APIs for mounting custom nodes to a [NodeContainer](../../../../arkts-components/custom-placeholder-components/nodecontainer/document.md) component.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/ctXEEaXkTLywAnfde9Vgng/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E885B4E44322B189592382C3B5888967E2A81988C9447A76F45482367C7D2C25)

-   The initial APIs of this module are supported since API version 11. Newly added APIs will be marked with a superscript to indicate their earliest API version.
    
-   NodeController objects do not support JSON serialization.
    

#### Modules to Import

import {  NodeController  } from '@kit.ArkUI';

#### NodeController

Implements a **NodeController** instance to manage the bound [NodeContainer](../../../../arkts-components/custom-placeholder-components/nodecontainer/document.md) component. One **NodeController** instance can be bound to only one [NodeContainer](../../../../arkts-components/custom-placeholder-components/nodecontainer/document.md) component. For best practices, see [Dynamic Component Creation: Dynamically Adding, Updating, and Deleting Components](https://developer.huawei.com/consumer/en/doc/best-practices/bpta-ui-dynamic-operations#section153921947151012).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### \[h2\]makeNode

abstract makeNode(uiContext : UIContext): FrameNode | null

Called when the [NodeContainer](../../../../arkts-components/custom-placeholder-components/nodecontainer/document.md) component bound to this **NodeController** instance is created. This callback returns a node, which will be mounted to the **NodeContainer**.

This callback can also be invoked through the **rebuild()** method of **NodeController**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/SO_gyKVdTCG4dJ2mJCV9pg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=864D140A7582B80A9A874162E996EB92DACF341862CE5A9952B06189604EAB55)

[NodeContainer](../../../../arkts-components/custom-placeholder-components/nodecontainer/document.md) does not support cross-instance reuse. If [NodeContainer](../../../../arkts-components/custom-placeholder-components/nodecontainer/document.md) is reused across instances and \[NodeController\] (#nodecontroller-1) of [NodeContainer](../../../../arkts-components/custom-placeholder-components/nodecontainer/document.md) triggers the \[makeNode\] (#makenode) callback method, the [UIContext](../../ohos-arkui-uicontext-uicontext/class-uicontext/document.md) object in the input parameter may be undefined. In this case, you need to check whether the [UIContext](../../ohos-arkui-uicontext-uicontext/class-uicontext/document.md) object in the input parameter is undefined, which prevents the [invalid UIContext](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-wrong-uicontext-debug#identifying-uicontext-errors) when the input parameter is used.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| uiContext | [UIContext](../../ohos-arkui-uicontext-uicontext/class-uicontext/document.md) | Yes | UI context of the bound [NodeContainer](../../../../arkts-components/custom-placeholder-components/nodecontainer/document.md) component. |

**Return value**

| Type | Description |
| :-- | :-- |
| [FrameNode](../framenode/document.md)| null | **FrameNode** object, which will be mounted to the placeholder node of the [NodeContainer](../../../../arkts-components/custom-placeholder-components/nodecontainer/document.md) component. If a null object is returned, the child nodes of the corresponding [NodeContainer](../../../../arkts-components/custom-placeholder-components/nodecontainer/document.md) component are removed. |

#### \[h2\]aboutToAppear

aboutToAppear?(): void

Called after the [NodeContainer](../../../../arkts-components/custom-placeholder-components/nodecontainer/document.md) component bound to this **NodeController** instance is attached and about to appear.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5/v3/Vgtg57KrTDOsu_IhKmTQkg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5DC17AE57FC7CFEF0B023CC8DE6F7212C3CA160EC6DD651E6A2AFCB0C05440B7)

For details about the callback timing, see [onAppear](../../../../arkts-components/universal-events/component-change-events/show-hide-event/document.md#onappear).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### \[h2\]aboutToDisappear

aboutToDisappear?(): void

Called when the [NodeContainer](../../../../arkts-components/custom-placeholder-components/nodecontainer/document.md) component bound to this **NodeController** instance is destroyed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/CGGlfVxuTj2YU34z7GYftQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=31B9947E30857191BE6094CBC0807F94F0B6309C5F2CC8A1977D0298F1025090)

For details about the callback timing, see [onDisAppear](../../../../arkts-components/universal-events/component-change-events/show-hide-event/document.md#ondisappear).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### \[h2\]onAttach18+

onAttach?(): void

Called when the [NodeContainer](../../../../arkts-components/custom-placeholder-components/nodecontainer/document.md) component bound to this **NodeController** instance is attached to the main node tree.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/ClbVm0dbRXmp2V_ODzNDsA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EA459B4FC4A50A09DEA050A1AD8F0DDAC8DBA89689DDC05AF52F6232F0FD23F9)

For details about the callback timing, see [onAttach](../../../../arkts-components/universal-events/component-change-events/show-hide-event/document.md#onattach12).

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### \[h2\]onDetach18+

onDetach?(): void

Called when the [NodeContainer](../../../../arkts-components/custom-placeholder-components/nodecontainer/document.md) component bound to this **NodeController** instance is detached from the main node tree.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/Yg5T3Z7ZQWy1jlUKxTiKxg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=868E8A29668068C22A39E965E7DA519802DFFA87C00D8B6ECF7873BA2FB69666)

For details about the callback timing, see [onDetach](../../../../arkts-components/universal-events/component-change-events/show-hide-event/document.md#ondetach12).

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### \[h2\]onWillBind18+

onWillBind?(containerId: number): void

Called when this **NodeController** instance is about to be bound to a [NodeContainer](../../../../arkts-components/custom-placeholder-components/nodecontainer/document.md) component.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| containerId | number | Yes | ID of the [NodeContainer](../../../../arkts-components/custom-placeholder-components/nodecontainer/document.md) component to which the **NodeController** instance is about to be bound. |

#### \[h2\]onWillUnbind18+

onWillUnbind?(containerId: number): void

Called when this **NodeController** instance is about to be unbound from a [NodeContainer](../../../../arkts-components/custom-placeholder-components/nodecontainer/document.md) component.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| containerId | number | Yes | ID of the [NodeContainer](../../../../arkts-components/custom-placeholder-components/nodecontainer/document.md) component from which the **NodeController** instance is about to be unbound. |

#### \[h2\]onBind18+

onBind?(containerId: number): void

Called after this **NodeController** instance is bound to a [NodeContainer](../../../../arkts-components/custom-placeholder-components/nodecontainer/document.md) component.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| containerId | number | Yes | ID of the [NodeContainer](../../../../arkts-components/custom-placeholder-components/nodecontainer/document.md) component to which the **NodeController** instance is bound. |

#### \[h2\]onUnbind18+

onUnbind?(containerId: number): void

Called after this **NodeController** instance is unbound from a [NodeContainer](../../../../arkts-components/custom-placeholder-components/nodecontainer/document.md) component.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| containerId | number | Yes | ID of the [NodeContainer](../../../../arkts-components/custom-placeholder-components/nodecontainer/document.md) component from which the **NodeController** instance is unbound. |

#### \[h2\]aboutToResize

aboutToResize?(size: Size): void

Called when the [NodeContainer](../../../../arkts-components/custom-placeholder-components/nodecontainer/document.md) component bound to this **NodeController** instance is resized.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| size | [Size](../graphics/document.md#size) | Yes | Width and height of the component, in vp. |

#### \[h2\]onTouchEvent

onTouchEvent?(event: TouchEvent): void

Called when the [NodeContainer](../../../../arkts-components/custom-placeholder-components/nodecontainer/document.md) component bound to this **NodeController** instance receives a touch event.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | [TouchEvent](../../../../arkts-components/universal-events/basic-input-events/touch-event/document.md#touchevent) | Yes | Touch event. |

#### \[h2\]rebuild

rebuild(): void

Instructs the [NodeContainer](../../../../arkts-components/custom-placeholder-components/nodecontainer/document.md) component bound to this **NodeController** instance to call the [makeNode](#makenode) API again to change child nodes.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/rhIWjPATSMiZHVk0xS_G3w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E0FD302AF268797D42FBE94614642ADE586EC49876132052946C68CCF498E1B5)

Since the **rebuild** API is actively called by the application and is tied to the UI, you need to ensure that the UI context is valid at the time of the call, that is, it must be consistent with the UI context of the bound NodeContainer.

In cases where the [UI context is unclear](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-global-interface#ambiguous-ui-context), for example, during event callbacks, you can use the [runScopedTask](../../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#runscopedtask) method of [UIContext](../../ohos-arkui-uicontext-uicontext/class-uicontext/document.md) to explicitly define the UI context at the time of the call.

#### Example

## Example 1: Implementing Lifecycle Callbacks for Node Layout, Touch, Mounting, and Unmounting Events

This example demonstrates how to manage the lifecycle of a **NodeContainer** component using **aboutToResize**, **onTouchEvent**,

**aboutToAppear**, and **aboutToDisappear**.

It also shows how to mount a BuilderNode using **NodeController**.

import { NodeController, BuilderNode, Size, FrameNode, UIContext } from '@kit.ArkUI';

class Params {
  text: string = "this is a text"
}

@Builder
function buttonBuilder(params: Params) {
  Column() {
    Button(params.text)
      .fontSize(12)
      .borderRadius(8)
      .borderWidth(2)
      .backgroundColor(Color.Orange)
  }
}

class MyNodeController extends NodeController {
  private buttonNode: BuilderNode<\[Params\]> | null = null;
  private wrapBuilder: WrappedBuilder<\[Params\]> = wrapBuilder(buttonBuilder);

  makeNode(uiContext: UIContext): FrameNode {
    if (this.buttonNode == null) {
      this.buttonNode = new BuilderNode(uiContext);
      this.buttonNode.build(this.wrapBuilder, { text: "This is a Button" })
    }
    return this.buttonNode!.getFrameNode()!;
  }

  aboutToResize(size: Size) {
    console.info(\`aboutToResize width : ${size.width} height : ${size.height}\`)
  }

  aboutToAppear() {
    console.info("aboutToAppear")
  }

  aboutToDisappear() {
    console.info("aboutToDisappear");
  }

  onTouchEvent(event: TouchEvent) {
    console.info("onTouchEvent");
  }
}

@Entry
@Component
struct Index {
  private myNodeController: MyNodeController = new MyNodeController();

  build() {
    Column() {
      NodeContainer(this.myNodeController)
    }
    .padding({ left: 35, right: 35, top: 35 })
    .width("100%")
    .height("100%")
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/-U0hTo_0STKOoIqwyTyx-g/en-us_image_0000002568765093.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C984D75A9F3728F5D04743F01CAE25DFE7A7B167242F9B668D5544119ED99837)

## Example 2: Implementing Lifecycle Callbacks for Node Binding/Unbinding and Tree Attachment/Detachment

This example demonstrates how to manage the lifecycle of a **NodeContainer** component when it is attached to or detached from the main node tree and

when it is bound or unbound, using **onAttach**, **onDetach**, **onWillBind**, **onWillUnbind**, **onBind**, and **onUnbind**.

import { NodeController, BuilderNode, FrameNode, UIContext } from '@kit.ArkUI';

class Params {
  text: string = "this is a text"
}

@Builder
function buttonBuilder(params: Params) {
  Column() {
    Button(params.text)
      .fontSize(20)
      .borderRadius(8)
      .borderWidth(2)
      .backgroundColor(Color.Grey)
  }
}

class MyNodeController extends NodeController {
  private buttonNode: BuilderNode<\[Params\]> | null = null;
  private wrapBuilder: WrappedBuilder<\[Params\]> = wrapBuilder(buttonBuilder);

  makeNode(uiContext: UIContext): FrameNode {
    if (this.buttonNode == null) {
      this.buttonNode = new BuilderNode(uiContext);
      this.buttonNode.build(this.wrapBuilder, { text: "This is a Button" })
    }
    return this.buttonNode!.getFrameNode()!;
  }

  onAttach(): void {
    console.info("myButton on attach");
  }

  onDetach(): void {
    console.info("myButton on detach");
  }

  onWillBind(containerId: number): void {
    console.info(\`myButton on WillBind${containerId}\`);
  }

  onWillUnbind(containerId: number): void {
    console.info(\`myButton on WillUnbind${containerId}\`);
  }

  onBind(containerId: number): void {
    console.info(\`myButton on bind: ${containerId}\`);
  }

  onUnbind(containerId: number): void {
    console.info(\`myButton on unbind: ${containerId}\`);
  }
}

@Entry
@Component
struct Index {
  @State buttonShow: boolean = true
  @State buttonIndex: number = 0
  private buttonController: MyNodeController = new MyNodeController();
  private buttonNull: null = null;
  private buttonControllerArray: Array<MyNodeController | null> = \[this.buttonController, this.buttonNull\]

  build() {
    Column() {
      Row() {
        Button("Bind/Unbind")
          .onClick(() => {
            this.buttonIndex++;
          }).margin(5)
        Button("onAttach/onDetach")
          .onClick(() => {
            this.buttonShow = !this.buttonShow
          }).margin(5)
      }

      if (this.buttonShow) {
        NodeContainer(this.buttonControllerArray\[this.buttonIndex % this.buttonControllerArray.length\])
      }
    }
    .padding({ left: 35, right: 35 })
    .width("100%")
    .height("100%")
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/D-s4zRG6SC-6_T5MTHvNSA/en-us_image_0000002537765368.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0200EBF073CBF6BFAC4F23DB70A9914C30B3E997634281BD72F1F44F40DC7C1C)
