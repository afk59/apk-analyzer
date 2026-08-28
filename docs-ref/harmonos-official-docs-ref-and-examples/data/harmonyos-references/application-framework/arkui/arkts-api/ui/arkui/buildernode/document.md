# BuilderNode

The **BuilderNode** module provides APIs for a BuilderNode – a custom node that can be used to mount built-in components. A BuilderNode can be used only as a leaf node. For details, see [BuilderNode Development](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-user-defined-arktsnode-buildernode). For best practices, see [Dynamic Component Creation: Dynamically Adding, Updating, and Deleting Components](https://developer.huawei.com/consumer/en/doc/best-practices/bpta-ui-dynamic-operations#section153921947151012).

Compared with **BuilderNode**, **ReactiveBuilderNode** can generate a component tree through the stateless UI method @Builder with multiple parameters.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/7uOPjq9yTs2juWlvY-mf-Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5F2CAC3C8E21C5A5D3479510A1A8E446FAC29C68DB32FD11792B3084539CF130)

-   The initial APIs of this module are supported since API version 11. Newly added APIs will be marked with a superscript to indicate their earliest API version.
    
-   If the root node of the provided Builder is a syntax node ([if/else](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-rendering-control-ifelse)/[ForEach](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-rendering-control-foreach)/[LazyForEach](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-rendering-control-lazyforeach)/[ContentSlot](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-rendering-control-contentslot)...), [Span](../../../../arkts-components/text-and-input/span/document.md), [ContainerSpan](../../../../arkts-components/text-and-input/containerspan/document.md), [SymbolSpan](../../../../arkts-components/text-and-input/symbolspan/document.md), or a custom component, an additional [FrameNode](../framenode/document.md) is generated and displayed as BuilderProxyNode in the node tree. This structural change affects the propagation of certain events. For details, see [BuilderProxyNode in BuilderNode Causes Tree Structure Changes](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-user-defined-arktsnode-buildernode#builderproxynode-in-buildernode-causes-tree-structure-changes).
    
-   If you encounter display issues when reusing a **BuilderNode** across pages, see [Cross-Page Reuse Considerations](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-user-defined-arktsnode-buildernode#cross-page-reuse-considerations) for guidance.
    
-   **BuilderNode** is not available in DevEco Studio Previewer.
    
-   Custom components under **BuilderNode** can use the [@Prop](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-prop) decorator. The [@Link](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-link) decorator cannot be used to synchronize external data and status across **BuilderNode** boundaries.
    
-   If a **BuilderNode** contains custom components as child nodes, these custom components cannot use the [@Reusable](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-reusable) decorator. For details, see [Using the @Reusable Decorator with BuilderNode Child Components](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-user-defined-arktsnode-buildernode#using-the-reusable-decorator-with-buildernode-child-components).
    
-   Since API version 12, custom components can receive [LocalStorage](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-localstorage) instances. You can use LocalStorage related decorators such as [@LocalStorageProp](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-localstorage#localstorageprop) and [@LocalStorageLink](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-localstorage#localstoragelink) by [passing LocalStorage instances](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-localstorage#providing-a-custom-component-with-access-to-a-localstorage-instance).
    
-   Since API version 20, when configured with [BuildOptions](#buildoptions12), custom components within a BuilderNode can access the host page's [@Provide](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-provide-and-consume) data through their [@Consume](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-provide-and-consume) decorated attributes.
    
-   The behavior of other decorators is undefined. Avoid using those decorators.
    
-   [Repeat](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-new-rendering-control-repeat) can be used only in custom components.
    
-   BuilderNode objects do not support JSON serialization.
    

#### Modules to Import

import { BuilderNode, ReactiveBuilderNode, RenderOptions, NodeRenderType } from '@kit.ArkUI';

#### NodeRenderType

Enumerates the node rendering types.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| RENDER\_TYPE\_DISPLAY | 0 | The node is displayed on the screen. |
| RENDER\_TYPE\_TEXTURE | 1 | The node is exported as a texture. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/ZwO2qTf-Tuu7BfX2lHCFYA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=322F5B2DD51CBDA2B94851A1C9750180F4F4EE8EA1159ECEA13E0A720F237C68)

-   Currently, the **RENDER\_TYPE\_TEXTURE** type takes effect only for the [XComponentNode](../../../apis-no-longer-maintained/xcomponentnode/document.md) and the [BuilderNode](#buildernode-1) holding a component tree whose root node is a custom component.
    
-   The following custom components currently support texture export as root nodes in [BuilderNode](#buildernode-1) scenarios: [Badge](../../../../arkts-components/information-display/badge/document.md), [Blank](../../../../arkts-components/blank-and-divider/blank/document.md), [Button](../../../../arkts-components/buttons-and-selections/button/document.md), [CanvasGradient](../../../../arkts-components/canvas-drawing/canvasgradient/document.md), [CanvasPattern](../../../../arkts-components/canvas-drawing/canvaspattern/document.md), [CanvasRenderingContext2D](../../../../arkts-components/canvas-drawing/canvasrenderingcontext2d/document.md), [Canvas](../../../../arkts-components/canvas-drawing/canvas/document.md), [CheckboxGroup](../../../../arkts-components/buttons-and-selections/checkboxgroup/document.md), [Checkbox](../../../../arkts-components/buttons-and-selections/checkbox/document.md), [Circle](../../../../arkts-components/graphic-drawing/circle/document.md), [ColumnSplit](../../../../arkts-components/grid-and-column-layout/columnsplit/document.md), [Column](../../../../arkts-components/rows-columns-and-stacking/column/document.md), [ContainerSpan](../../../../arkts-components/text-and-input/containerspan/document.md), [Counter](../../../../arkts-components/information-display/counter/document.md), [DataPanel](../../../../arkts-components/information-display/datapanel/document.md), [Divider](../../../../arkts-components/blank-and-divider/divider/document.md), [Ellipse](../../../../arkts-components/graphic-drawing/ellipse/document.md), [Flex](../../../../arkts-components/rows-columns-and-stacking/flex/document.md), [Gauge](../../../../arkts-components/information-display/gauge/document.md), [Hyperlink](../../../../arkts-components/text-and-input/hyperlink/document.md), [ImageBitmap](../../../../arkts-components/canvas-drawing/imagebitmap/document.md), [ImageData](../../../../arkts-components/canvas-drawing/imagedata/document.md), [Image](../../../../arkts-components/images-and-videos/image/document.md), [Line](../../../../arkts-components/graphic-drawing/line/document.md), [LoadingProgress](../../../../arkts-components/information-display/loadingprogress/document.md), [Marquee](../../../../arkts-components/information-display/marquee/document.md), [Matrix2D](../../../../arkts-components/canvas-drawing/matrix2d/document.md), [OffscreenCanvasRenderingContext2D](../../../../arkts-components/canvas-drawing/offscreencanvasrenderingcontext2d/document.md), [OffscreenCanvas](../../../../arkts-components/canvas-drawing/offscreencanvas/document.md), [Path2D](../../../../arkts-components/canvas-drawing/path2d/document.md), [Path](../../../../arkts-components/graphic-drawing/path/document.md), [PatternLock](../../../../arkts-components/information-display/patternlock/document.md), [Polygon](../../../../arkts-components/graphic-drawing/polygon/document.md), [Polyline](../../../../arkts-components/graphic-drawing/polyline/document.md), [Progress](../../../../arkts-components/information-display/progress/document.md), [QRCode](../../../../arkts-components/information-display/qrcode/document.md), [Radio](../../../../arkts-components/buttons-and-selections/radio/document.md), [Rating](../../../../arkts-components/buttons-and-selections/rating/document.md), [Rect](../../../../arkts-components/graphic-drawing/rect/document.md), [RelativeContainer](../../../../arkts-components/rows-columns-and-stacking/relativecontainer/document.md), [RowSplit](../../../../arkts-components/grid-and-column-layout/rowsplit/document.md), [Row](../../../../arkts-components/rows-columns-and-stacking/row/document.md), [Shape](../../../../arkts-components/graphic-drawing/shape/document.md), [Slider](../../../../arkts-components/buttons-and-selections/slider/document.md), [Span](../../../../arkts-components/text-and-input/span/document.md), [Stack](../../../../arkts-components/rows-columns-and-stacking/stack/document.md), [TextArea](../../../../arkts-components/text-and-input/textarea/document.md), [TextClock](../../../../arkts-components/information-display/textclock/document.md), [TextInput](../../../../arkts-components/text-and-input/textinput/document.md), [TextTimer](../../../../arkts-components/information-display/texttimer/document.md), [Text](../../../../arkts-components/text-and-input/text/document.md), [Toggle](../../../../arkts-components/buttons-and-selections/toggle/document.md), [Video](../../../../arkts-components/images-and-videos/video/document.md) (excluding full-screen playback), [Web](../../../../../arkweb/arkts-components/web/components/document.md), [XComponent](../../../../arkts-components/rendering-drawing/xcomponent/document.md).
    
-   Since API version 12, the following components also support texture export: [DatePicker](../../../../arkts-components/buttons-and-selections/datepicker/document.md), [ForEach](../../../../arkts-components/state-management-and-rendering-control/foreach/document.md), [Grid](../../../../arkts-components/scroll-and-swipe/grid/document.md), [if/else](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-rendering-control-ifelse), [LazyForEach](../../../../arkts-components/state-management-and-rendering-control/lazyforeach/document.md), [List](../../../../arkts-components/scroll-and-swipe/list/document.md), [Scroll](../../../../arkts-components/scroll-and-swipe/scroll/document.md), [Swiper](../../../../arkts-components/scroll-and-swipe/swiper/document.md), [TimePicker](../../../../arkts-components/buttons-and-selections/timepicker/document.md), custom components decorated with [@Component](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-create-custom-components#component), [NodeContainer](../../../../arkts-components/custom-placeholder-components/nodecontainer/document.md), and [FrameNode](../framenode/document.md) and [RenderNode](../rendernode/document.md) mounted to [NodeContainer](../../../../arkts-components/custom-placeholder-components/nodecontainer/document.md).
    
-   For details, see [Rendering and Drawing Video and Button Components at the Same Layer](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/web-same-layer).
    

#### RenderOptions

Provides optional parameters for creating a BuilderNode.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| selfIdealSize | [Size](../graphics/document.md#size) | No | Yes | 
Ideal size of the node.

Default value: **{ width: 0, height: 0 }**.

 |
| type | [NodeRenderType](#noderendertype) | No | Yes | 

Rendering type of the node.

Default value: **NodeRenderType.RENDER\_TYPE\_DISPLAY**.

 |
| surfaceId | string | No | Yes | 

Surface ID of the texture receiver. Typically, the texture receiver is [OH\_NativeImage](../../../../../../graphics/arkgraphics-2d/c-apis/structs/oh-nativeimage/document.md).

This parameter is effective only when **type** is set to **NodeRenderType.RENDER\_TYPE\_TEXTURE**.

Default value: **""**.

 |

#### BuildOptions12+

Defines the optional build options.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| nestingBuilderSupported | boolean | No | Yes | 
Whether to support nested **@Builder** within **@Builder**. **true** if supported, **false** otherwise.

Default value: **false**.

**Model constraint**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| localStorage20+ | [LocalStorage](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-localstorage) | No | Yes | 

LocalStorage for the current BuilderNode. Custom components mounted under this BuilderNode will share the specified LocalStorage. **NOTE**

If LocalStorage is also passed through a custom component's constructor, the constructor parameter takes precedence.

Default value: **null**.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |
| enableProvideConsumeCrossing20+ | boolean | No | Yes | 

Whether @Consume in the custom components under the current BuilderNode can communicate with @Provide outside the BuilderNode. The value **true** means that this feature is supported, and **false** means the opposite. Default value: **false**.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |

#### InputEventType20+

type InputEventType = TouchEvent | MouseEvent | AxisEvent

Defines the type of input event to be dispatched. For details, see [postInputEvent](#postinputevent20).

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Type | Description |
| :-- | :-- |
| [TouchEvent](../../../../arkts-components/universal-events/basic-input-events/touch-event/document.md#touchevent) | Touch event. |
| [MouseEvent](../../../../arkts-components/universal-events/basic-input-events/mouse-event/document.md#mouseevent) | Mouse event. |
| [AxisEvent](../../../../arkts-components/universal-events/basic-input-events/axis-event/document.md#axisevent) | Axis event. |

#### BuilderNode

class BuilderNode<Args extends Object\[\]>

Implements a BuilderNode, which can create a component tree through the stateless UI method [@Builder](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-builder) and hold the root node of the component tree. A BuilderNode cannot be defined as a state variable. The FrameNode held in the BuilderNode is only used to mount the BuilderNode to other FrameNodes as a child node. Undefined behavior may occur if you set attributes or perform operations on subnodes of the FrameNode held by the BuilderNode. Therefore, after you have obtained a [RenderNode](../rendernode/document.md) through the [getFrameNode](#getframenode) method of the BuilderNode and the [getRenderNode](../framenode/document.md#getrendernode) method of the [FrameNode](../framenode/document.md), avoid setting the attributes or operating the subnodes through APIs of [RenderNode](../rendernode/document.md).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### \[h2\]constructor

constructor(uiContext: UIContext, options?: RenderOptions)

When content generated by BuilderNode is embedded within another RenderNode for display, the **selfIdealSize** parameter in **RenderOptions** must be explicitly specified. Otherwise, the layout constraints for the parent component in Builder default to \[0, 0\]. In this case, if **selfIdealSize** is not set, the root node of the subtree in BuilderNode will have a size of \[0, 0\].

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| uiContext | [UIContext](../../ohos-arkui-uicontext-uicontext/class-uicontext/document.md) | Yes | UI context. For details about how to obtain it, see [Obtaining UI Context](../../ohos-arkui-node/document.md#obtaining-ui-context). |
| options | [RenderOptions](#renderoptions) | No | 
Parameters for creating a BuilderNode.

Default value: **undefined**.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/4uS-QqzWR1i9D6khHelbkA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DF0A690A3E66281DF3C8E7A212DDCDE82B5DF21250E1F2FB210DEBFFAE964CB0)

The input parameter for **uiContext** must be a valid value, that is, the UI context must be correct. If an invalid value is passed in or if no value is specified, creation will fail.

#### \[h2\]build

build(builder: WrappedBuilder<Args>, arg?: Object): void

Creates a component tree based on the passed object and holds the root node of the component tree. The stateless UI method [@Builder](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-builder) has at most one root node.

Custom components are allowed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/QEz-0vpzQqargmaGuoWcjw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=88E72C4186B896F953673BBF22FE4733DB488BD4D4ECA95FAA798832C746E815)

-   When nesting @Builder, ensure that the input objects for the inner and outer @Builder methods are consistent.
    
-   The outermost @Builder supports only one input parameter.
    
-   The build parameter uses the pass-by-value semantics. To implement state updates, you must explicitly use the [update](#update) API.
    
-   To operate objects in a BuilderNode, ensure that the reference to the BuilderNode is not garbage collected. When a BuilderNode object is garbage collected by the virtual machine, the associated [FrameNode](../framenode/document.md) and [RenderNode](../rendernode/document.md) objects are also dereferenced from the backend node tree. This means that any FrameNode objects obtained from a BuilderNode will no longer correspond to any actual node if the BuilderNode is garbage collected.
    
-   The BuilderNode object maintains references to its underlying entity nodes. When the BuilderNode frontend object is no longer required for managing backend nodes, call the [dispose](#dispose12) API to release node references and unbind frontend and backend nodes.
    

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| builder | [WrappedBuilder<Args>](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-wrapbuilder) | Yes | Stateless UI method [@Builder](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-builder) required for creating a component tree. |
| arg | Object | No | 
Argument of the builder. Only one input parameter is supported, and the type of the input parameter must be consistent with the type defined by @Builder.

Default value: **undefined**.

 |

#### \[h2\]build12+

build(builder: WrappedBuilder<Args>, arg: Object, options: BuildOptions): void

Creates a component tree based on the passed object and holds the root node of the component tree. The stateless UI method [@Builder](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-builder) has at most one root node.

Custom components are allowed. Compared with the [build(builder: WrappedBuilder<Args>, arg?: Object)](#build) API, this API can use the builder configuration parameters to determine whether @Builder can be nested with @Builder.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/rYdHKvVbQeCPhmGY0Vmr_A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=03D212E41E9C3C904520CA845D2C428EF23A58E139E14AEE424DF72FC2B85695)

-   For details about the creation and update using @Builder, see [@Builder](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-builder).
    
-   The outermost @Builder supports only one input parameter.
    

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| builder | [WrappedBuilder<Args>](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-wrapbuilder) | Yes | Stateless UI method [@Builder](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-builder) required for creating a component tree. |
| arg | Object | Yes | Argument of the builder. Only one input parameter is supported, and the type of the input parameter must be consistent with the type defined by @Builder. |
| options | [BuildOptions](#buildoptions12) | Yes | Build options, which determine whether to support nesting @Builder within @Builder. |

**Example**

import { BuilderNode, NodeContent } from "@kit.ArkUI";

// Define the API for passing parameters.
interface ParamsInterface {
  text: string;
  func: Function;
}

@Builder
function buildTextWithFunc(fun: Function) {
  Text(fun())
    .fontSize(50)
    .fontWeight(FontWeight.Bold)
    .margin({ bottom: 36 })
}

@Builder
function buildText(params: ParamsInterface) {
  Column() {
    Text(params.text)
      .fontSize(50)
      .fontWeight(FontWeight.Bold)
      .margin({ bottom: 36 })
    buildTextWithFunc(params.func)
  }
}

@Entry
@Component
struct Index {
  @State message: string = "HELLO";
  private content: NodeContent = new NodeContent();

  build() {
    Row() {
      Column() {
        Button('addBuilderNode')
          .onClick(() => {
            let buildNode = new BuilderNode<\[ParamsInterface\]>(this.getUIContext());
            // Create a node tree.
            buildNode.build(wrapBuilder<\[ParamsInterface\]>(buildText), {
              text: this.message, func: () => {
                return "FUNCTION";
              }
            }, { nestingBuilderSupported: true });
            this.content.addFrameNode(buildNode.getFrameNode());
            buildNode.dispose();
          })
        ContentSlot(this.content)
      }
      .id("column")
      .width('100%')
      .height('100%')
    }
    .height('100%')
  }
}

#### \[h2\]getFrameNode

getFrameNode(): FrameNode | null

Obtains the [FrameNode](../framenode/document.md) from the BuilderNode. The FrameNode is generated only after the BuilderNode executes the build operation.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| [FrameNode](../framenode/document.md) | null | **FrameNode** object. If no such object is held by the **BuilderNode** instance, null is returned. |

**Example 1**

The BuilderNode is returned as the root node of [NodeContainer](../../../../arkts-components/custom-placeholder-components/nodecontainer/document.md).

import { NodeController, BuilderNode, FrameNode, UIContext } from "@kit.ArkUI";

// Define the class for passing parameters.
class Params {
  text: string = "";
  constructor(text: string) {
    this.text = text;
  }
}

@Builder
function buildText(params: Params) {
  Column() {
    Text(params.text)
      .fontSize(50)
      .fontWeight(FontWeight.Bold)
      .margin({bottom: 36})
  }
}

// Implement a custom textNode controller by extending NodeController.
class TextNodeController extends NodeController {
  private textNode: BuilderNode<\[Params\]> | null = null;
  private message: string = "DEFAULT";

  constructor(message: string) {
    super();
    this.message = message;
  }

  makeNode(context: UIContext): FrameNode | null {
    this.textNode = new BuilderNode(context);
    this.textNode.build(wrapBuilder<\[Params\]>(buildText), new Params(this.message));
    // Return the FrameNode contained in the current BuilderNode.
    return this.textNode.getFrameNode();
  }
}

@Entry
@Component
struct Index {
  @State message: string = "hello";

  build() {
    Row() {
      Column() {
        NodeContainer(new TextNodeController(this.message))
          .width('100%')
          .height(100)
          .backgroundColor('#FFF0F0F0')
      }
      .width('100%')
      .height('100%')
    }
    .height('100%')
  }
}

**Example 2**

The [FrameNode](../framenode/document.md) of the BuilderNode is mounted to another FrameNode.

import { NodeController, BuilderNode, FrameNode, UIContext } from "@kit.ArkUI";

// Define the class for passing parameters.
class Params {
  text: string = "";

  constructor(text: string) {
    this.text = text;
  }
}

@Builder
function buildText(params: Params) {
  Column() {
    Text(params.text)
      .fontSize(50)
      .fontWeight(FontWeight.Bold)
      .margin({ bottom: 36 })
  }
}

// Implement a custom textNode controller by extending NodeController.
class TextNodeController extends NodeController {
  private rootNode: FrameNode | null = null;
  private textNode: BuilderNode<\[Params\]> | null = null;
  private message: string = "DEFAULT";

  constructor(message: string) {
    super();
    this.message = message;
  }

  makeNode(context: UIContext): FrameNode | null {
    this.rootNode = new FrameNode(context);
    this.textNode = new BuilderNode(context, { selfIdealSize: { width: 150, height: 150 } });
    this.textNode.build(wrapBuilder<\[Params\]>(buildText), new Params(this.message));
    if (this.rootNode !== null) {
      // Mount the FrameNode of the BuilderNode to another FrameNode.
      this.rootNode.appendChild(this.textNode?.getFrameNode());
    }

    return this.rootNode;
  }
}

@Entry
@Component
struct Index {
  @State message: string = "hello";

  build() {
    Row() {
      Column() {
        NodeContainer(new TextNodeController(this.message))
          .width('100%')
          .height(100)
          .backgroundColor('#FFF0F0F0')
      }
      .width('100%')
      .height('100%')
    }
    .height('100%')
  }
}

**Example 3**

The [RenderNode](../rendernode/document.md) of the BuilderNode is mounted to another RenderNode. Since the RenderNode does not pass layout constraints, this mode of mounting nodes is not recommended.

import { NodeController, BuilderNode, FrameNode, UIContext, RenderNode } from "@kit.ArkUI";
// Define the class for passing parameters.
class Params {
  text: string = "";

  constructor(text: string) {
    this.text = text;
  }
}

@Builder
function buildText(params: Params) {
  Column() {
    Text(params.text)
      .fontSize(50)
      .fontWeight(FontWeight.Bold)
      .margin({ bottom: 36 })
  }
}

// Implement a custom textNode controller by extending NodeController.
class TextNodeController extends NodeController {
  private rootNode: FrameNode | null = null;
  private textNode: BuilderNode<\[Params\]> | null = null;
  private message: string = "DEFAULT";

  constructor(message: string) {
    super();
    this.message = message;
  }

  makeNode(context: UIContext): FrameNode | null {
    this.rootNode = new FrameNode(context);
    let renderNode = new RenderNode();
    renderNode.clipToFrame = false;
    this.textNode = new BuilderNode(context, { selfIdealSize: { width: 150, height: 150 } });
    this.textNode.build(wrapBuilder<\[Params\]>(buildText), new Params(this.message));
    const textRenderNode = this.textNode?.getFrameNode()?.getRenderNode();

    const rootRenderNode = this.rootNode.getRenderNode();
    if (rootRenderNode !== null) {
      rootRenderNode.appendChild(renderNode);
    // Mount the RenderNode of the BuilderNode to another RenderNode.
      renderNode.appendChild(textRenderNode);
    }

    return this.rootNode;
  }
}

@Entry
@Component
struct Index {
  @State message: string = "hello";

  build() {
    Row() {
      Column() {
        NodeContainer(new TextNodeController(this.message))
          .width('100%')
          .height(100)
          .backgroundColor('#FFF0F0F0')
      }
      .width('100%')
      .height('100%')
    }
    .height('100%')
  }
}

#### \[h2\]update

update(arg: Object): void

Updates this BuilderNode using the provided parameter, which must be of the same type as the input parameter passed to the [build](#build) API. When updating a custom component, define the variables used in the component as [@Prop](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-prop) decorated properties.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| arg | Object | Yes | Parameter used to update the BuilderNode. It is of the same type as the parameter passed to the [build](#build) API. |

**Example**

import { NodeController, BuilderNode, FrameNode, UIContext } from "@kit.ArkUI";

// Define the class for passing parameters.
class Params {
  text: string = "";
  constructor(text: string) {
    this.text = text;
  }
}

// Custom component
@Component
struct TextBuilder {
  @Prop message: string = "TextBuilder";

  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
          .margin({bottom: 36})
          .backgroundColor(Color.Gray)
      }
    }
  }
}

@Builder
function buildText(params: Params) {
  Column() {
    Text(params.text)
      .fontSize(50)
      .fontWeight(FontWeight.Bold)
      .margin({ bottom: 36 })
    TextBuilder({message: params.text}) // Custom component
  }
}

// Implement a custom textNode controller by extending NodeController.
class TextNodeController extends NodeController {
  private rootNode: FrameNode | null = null;
  private textNode: BuilderNode<\[Params\]> | null = null;
  private message: string = "";

  constructor(message: string) {
    super();
    this.message = message;
  }

  makeNode(context: UIContext): FrameNode | null {
    this.textNode = new BuilderNode(context);
    this.textNode.build(wrapBuilder<\[Params\]>(buildText), new Params(this.message));
    return this.textNode.getFrameNode();
  }

  // Update the BuilderNode based on the input parameters.
  update(message: string) {
    if (this.textNode !== null) {
      this.textNode.update(new Params(message));
    }
  }
}

@Entry
@Component
struct Index {
  @State message: string = "hello";
  private textNodeController: TextNodeController = new TextNodeController(this.message);
  private count = 0;

  build() {
    Row() {
      Column() {
        NodeContainer(this.textNodeController)
          .width('100%')
          .height(200)
          .backgroundColor('#FFF0F0F0')
        Button('Update')
          .onClick(() => {
            this.count += 1;
            const message = "Update " + this.count.toString();
            this.textNodeController.update(message);
          })
      }
      .width('100%')
      .height('100%')
    }
    .height('100%')
  }
}

#### \[h2\]postTouchEvent

postTouchEvent(event: TouchEvent): boolean

Posts a raw touch event to the FrameNode created by this BuilderNode.

**postTouchEvent** dispatches the event from a middle node in the component tree downwards. To ensure the event is dispatched correctly, it needs to be transformed into the coordinate system of the parent component, as shown in the figure below.

**OffsetA** indicates the offset of the BuilderNode relative to the parent component. You can obtain this offset by calling [getPositionToParent](../framenode/document.md#getpositiontoparent12) in the FrameNode. **OffsetB** indicates the offset of the touch point relative to the BuilderNode. You can obtain this offset from the [TouchEvent](../../../../arkts-components/universal-events/basic-input-events/touch-event/document.md#touchevent) object. **OffsetC** is the sum of **OffsetA** and **OffsetB**. It represents the final offset that you need to pass to **postTouchEvent**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/EKDGwRIqQK-AcQeGzBS0AA/en-us_image_0000002537925282.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E476CD97AFF68218E38ACFB20B91586F802C3C2D5ABEFC97FB3F1396E8C69906)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/0uDMo7QfRHWuarQm_yaDnw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3D4E776FC975C5123292AD147AFB8D1E9A441BEA5E9712BD55C15CF947DBE7F7)

-   The coordinates you pass in need to be converted to pixel values (px). If the BuilderNode has any affine transformations applied to it, they must be taken into account and combined with the touch event coordinates.
    
-   In [Webview](../../../../../arkweb/arkts-api/ohos-web-webview-webview/module-description/document.md), coordinate system transformations are already handled internally, so you can directly dispatch the touch event without additional adjustments.
    
-   The **postTouchEvent** API can be called only once for the same timestamp.
    

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | [TouchEvent](../../../../arkts-components/universal-events/basic-input-events/touch-event/document.md#touchevent) | Yes | Touch event. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | 
Whether the event is successfully dispatched. The value **true** means the event is consumed by a component that responds to the event, and **false** means that no component responds to the event.

**NOTE**

If the event does not hit the expected component, ensure the following:

1\. The coordinate system has been correctly transformed

2\. The component is in an interactive state.

3\. The event has been bound to the component.

 |

**Example**

import { NodeController, BuilderNode, FrameNode, UIContext } from '@kit.ArkUI';

// Define the class for passing parameters.
class Params {
  text: string = "this is a text";
}

@Builder
function ButtonBuilder(params: Params) {
  Column() {
    Button(\`button \` + params.text)
      .borderWidth(2)
      .backgroundColor(Color.Orange)
      .width("100%")
      .height("100%")
      .gesture(
        TapGesture()
          .onAction((event: GestureEvent) => {
            console.info("TapGesture");
          })
      )
  }
  .width(500)
  .height(300)
  .backgroundColor(Color.Gray)
}

// Implement a custom UI controller by extending NodeController.
class MyNodeController extends NodeController {
  private rootNode: BuilderNode<\[Params\]> | null = null;
  private wrapBuilder: WrappedBuilder<\[Params\]> = wrapBuilder(ButtonBuilder);

  makeNode(uiContext: UIContext): FrameNode | null {
    this.rootNode = new BuilderNode(uiContext);
    this.rootNode.build(this.wrapBuilder, { text: "this is a string" });
    return this.rootNode.getFrameNode();
  }

  // Coordinate system transformation
  postTouchEvent(event: TouchEvent, uiContext: UIContext): boolean {
    if (this.rootNode == null) {
      return false;
    }
    let node: FrameNode | null = this.rootNode.getFrameNode();
    let offsetX: number | null | undefined = node?.getPositionToParent().x;
    let offsetY: number | null | undefined = node?.getPositionToParent().y;
    
    let changedTouchLen = event.changedTouches.length;
    for (let i = 0; i < changedTouchLen; i++) {
      if (offsetX != null && offsetY != null && offsetX != undefined && offsetY != undefined) {
        event.changedTouches\[i\].x = uiContext.vp2px(offsetX + event.changedTouches\[i\].x);
        event.changedTouches\[i\].y = uiContext.vp2px(offsetY + event.changedTouches\[i\].y);
      }
    }
    // Post the event to the FrameNode created by BuilderNode. result indicates whether the post is successful.
    let result = this.rootNode.postTouchEvent(event);
    console.info(\`result ${result}\`);
    return result;
  }
}

@Entry
@Component
struct MyComponent {
  private nodeController: MyNodeController = new MyNodeController();

  build() {
    Column() {
      NodeContainer(this.nodeController)
        .height(300)
        .width(500)

      Column()
        .width(500)
        .height(300)
        .backgroundColor(Color.Pink)
        .onTouch((event) => {
          if (event != undefined) {
            this.nodeController.postTouchEvent(event, this.getUIContext());
          }
        })
    }
  }
}

#### \[h2\]dispose12+

dispose(): void

Immediately releases the reference relationship between this BuilderNode object and its [entity node](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-user-defined-node#basic-concepts). For details about the scenarios involving BuilderNode unbinding, see [Canceling the Reference to the Entity Node](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-user-defined-arktsnode-buildernode#canceling-the-reference-to-the-entity-node).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/EVsKKuzPSI2aQ7csHZFuQw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FF21FDB6F6216C0E15577061DF7C394E58CA06447F1BCE1BF35A9C1ECB25C63D)

After calling **dispose()**, the BuilderNode object cancels its reference to the backend entity node. If the frontend object BuilderNode cannot be released, memory leaks may occur. To avoid this, be sure to call **dispose()** on the BuilderNode when you no longer need it. This reduces the complexity of reference relationships and lowers the risk of memory leaks. For details, see [Memory Leak Caused by Circular Reference Between BuilderNode Frontend and Backend](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-user-defined-node-faq#memory-leak-caused-by-circular-reference-between-buildernode-frontend-and-backend).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

import { FrameNode, NodeController, BuilderNode } from '@kit.ArkUI';

// Custom component
@Component
struct TestComponent {
  build() {
    Column() {
      Text('This is a BuilderNode.')
        .fontSize(16)
        .fontWeight(FontWeight.Bold)
    }
    .width('100%')
    .backgroundColor(Color.Gray)
  }

  aboutToAppear() {
    console.info('aboutToAppear');
  }

  aboutToDisappear() {
    console.info('aboutToDisappear');
  }
}

@Builder
function buildComponent() {
  TestComponent()
}

// Implement a custom UI controller by extending NodeController.
class MyNodeController extends NodeController {
  private rootNode: FrameNode | null = null;
  private builderNode: BuilderNode<\[\]> | null = null;

  makeNode(uiContext: UIContext): FrameNode | null {
    this.rootNode = new FrameNode(uiContext);
    this.builderNode = new BuilderNode(uiContext, { selfIdealSize: { width: 200, height: 100 } });
    this.builderNode.build(new WrappedBuilder(buildComponent));

    const rootRenderNode = this.rootNode!.getRenderNode();
    if (rootRenderNode !== null) {
      rootRenderNode.size = { width: 200, height: 200 };
      rootRenderNode.backgroundColor = 0xff00ff00;
      rootRenderNode.appendChild(this.builderNode!.getFrameNode()!.getRenderNode());
    }

    return this.rootNode;
  }

  // Remove the reference relationship between the current builderNode and the backend entity.
  dispose() {
    if (this.builderNode !== null) {
      this.builderNode.dispose();
    }
  }

  removeBuilderNode() {
    const rootRenderNode = this.rootNode!.getRenderNode();
    if (rootRenderNode !== null && this.builderNode !== null && this.builderNode.getFrameNode() !== null) {
      rootRenderNode.removeChild(this.builderNode!.getFrameNode()!.getRenderNode());
    }
  }
}

@Entry
@Component
struct Index {
  private myNodeController: MyNodeController = new MyNodeController();

  build() {
    Column({ space: 4 }) {
      NodeContainer(this.myNodeController)
      Button('BuilderNode dispose')
        .onClick(() => {
          this.myNodeController.removeBuilderNode();
          this.myNodeController.dispose();
        })
        .width('100%')
    }
  }
}

#### \[h2\]reuse12+

reuse(param?: Object): void

Triggers component reuse for custom components under this BuilderNode. For details about component reuse, see [@Reusable Decorator: Reusing V1 Components](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-reusable). For details about the scenarios involving BuilderNode unbinding, see [Canceling the Reference to the Entity Node](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-user-defined-arktsnode-buildernode#canceling-the-reference-to-the-entity-node).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| param | Object | No | Parameter used to reuse the BuilderNode. This parameter is passed to all top-level custom components within the BuilderNode during reuse and must include all required constructor parameters for each component; otherwise, undefined behavior may occur. Calling this method synchronously triggers the [aboutToReuse](../../../../arkts-components/custom-components/custom-component-lifecycle/document.md#abouttoreuse10) lifecycle callback of internal custom components, with this parameter as the callback input. Default value: **undefined**, in which case the custom components in the BuilderNode will use their original construction data source. |

#### \[h2\]recycle12+

recycle(): void

Triggers recycling of custom components under this BuilderNode. Component recycling is part of the component reuse mechanism. For details, see [@Reusable Decorator: Reusing V1 Components](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-reusable).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/q56g_4mPTUegem7iWGgFeg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A967FE1E8471AD08EBD3708837829E2A15E012C782827D2AAE339E461C8273A4)

The BuilderNode completes the reuse event transfer between internal and external custom components through **reuse** and **recycle**. For specific usage scenarios, see [Implementing Node Reuse with the BuilderNode reuse and recycle APIs](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-user-defined-arktsnode-buildernode#implementing-node-reuse-with-the-buildernode-reuse-and-recycle-apis).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

import { FrameNode, NodeController, BuilderNode, UIContext } from "@kit.ArkUI";

const TEST\_TAG: string = "Reuse+Recycle";

// Define the class for managing data.
class MyDataSource {
  private dataArray: string\[\] = \[\];
  private listener: DataChangeListener | null = null;

  public totalCount(): number {
    return this.dataArray.length;
  }

  public getData(index: number) {
    return this.dataArray\[index\];
  }

  public pushData(data: string) {
    this.dataArray.push(data);
  }

  public reloadListener(): void {
    this.listener?.onDataReloaded();
  }

  public registerDataChangeListener(listener: DataChangeListener): void {
    this.listener = listener;
  }

  public unregisterDataChangeListener(): void {
    this.listener = null;
  }
}

// Define the class for passing parameters.
class Params {
  item: string = '';

  constructor(item: string) {
    this.item = item;
  }
}

@Builder
function buildNode(param: Params = new Params("hello")) {
  Row() {
    Text(\`C${param.item} -- \`)
    ReusableChildComponent2({ item: param.item }) // This custom component cannot be correctly reused in the BuilderNode.
  }
}

// Implement a custom UI controller by extending NodeController.
class MyNodeController extends NodeController {
  public builderNode: BuilderNode<\[Params\]> | null = null;
  public item: string = "";

  makeNode(uiContext: UIContext): FrameNode | null {
    if (this.builderNode == null) {
      this.builderNode = new BuilderNode(uiContext, { selfIdealSize: { width: 300, height: 200 } });
      this.builderNode.build(wrapBuilder<\[Params\]>(buildNode), new Params(this.item));
    }
    return this.builderNode.getFrameNode();
  }
}

// The custom component that is reused and recycled will have its state variables updated, and the state variables of the nested custom component ReusableChildComponent3 will also be updated. However, the BuilderNode will block this propagation process.
@Reusable
@Component
struct ReusableChildComponent {
  @Prop item: string = '';
  @Prop switch: string = '';
  private controller: MyNodeController = new MyNodeController();

  aboutToAppear() {
    this.controller.item = this.item;
  }

  aboutToRecycle(): void {
    console.info(\`${TEST\_TAG} ReusableChildComponent aboutToRecycle ${this.item}\`);

    // When the switch is open, pass the reuse or recycle event to the nested custom component, such as ReusableChildComponent2, through the BuilderNode's reuse or recycle API to complete reuse or recycling.
    if (this.switch === 'open') {
      this.controller?.builderNode?.recycle();
    }
  }

  aboutToReuse(params: object): void {
    console.info(\`${TEST\_TAG} ReusableChildComponent aboutToReuse ${JSON.stringify(params)}\`);

    // When the switch is open, pass the reuse or recycle event to the nested custom component, such as ReusableChildComponent2, through the BuilderNode's reuse or recycle API to complete reuse or recycling.
    if (this.switch === 'open') {
      this.controller?.builderNode?.reuse(params);
    }
  }

  build() {
    Row() {
      Text(\`A${this.item}--\`)
      ReusableChildComponent3({ item: this.item })
      NodeContainer(this.controller);
    }
  }
}

// Custom component
@Component
struct ReusableChildComponent2 {
  @Prop item: string = "false";

  aboutToReuse(params: Record<string, object>) {
    console.info(\`${TEST\_TAG} ReusableChildComponent2 aboutToReuse ${JSON.stringify(params)}\`);
  }

  aboutToRecycle(): void {
    console.info(\`${TEST\_TAG} ReusableChildComponent2 aboutToRecycle ${this.item}\`);
  }

  build() {
    Row() {
      Text(\`D${this.item}\`)
        .fontSize(20)
        .backgroundColor(Color.Yellow)
        .margin({ left: 10 })
    }.margin({ left: 10, right: 10 })
  }
}

@Component
struct ReusableChildComponent3 {
  @Prop item: string = "false";

  aboutToReuse(params: Record<string, object>) {
    console.info(\`${TEST\_TAG} ReusableChildComponent3 aboutToReuse ${JSON.stringify(params)}\`);
  }

  aboutToRecycle(): void {
    console.info(\`${TEST\_TAG} ReusableChildComponent3 aboutToRecycle ${this.item}\`);
  }

  build() {
    Row() {
      Text(\`B${this.item}\`)
        .fontSize(20)
        .backgroundColor(Color.Yellow)
        .margin({ left: 10 })
    }.margin({ left: 10, right: 10 })
  }
}

@Entry
@Component
struct Index {
  @State data: MyDataSource = new MyDataSource();

  aboutToAppear() {
    for (let i = 0; i < 100; i++) {
      this.data.pushData(i.toString());
    }
  }

  build() {
    Column() {
      List({ space: 3 }) {
        LazyForEach(this.data, (item: string) => {
          ListItem() {
            ReusableChildComponent({
              item: item,
              switch: 'open' // Changing open to close can be used to observe the behavior of custom components inside the BuilderNode when reuse and recycle events are not passed through the BuilderNode's reuse and recycle APIs.
            })
          }
        }, (item: string) => item)
      }
      .width('100%')
      .height('100%')
    }
  }
}

#### \[h2\]updateConfiguration12+

updateConfiguration(): void

Updates the configuration of the entire node by passing in a [system environment change](../../../../../ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-configuration-environment-variables/document.md) event.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/QrhcsRltSgGjHFNVlWuEqw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=168E6B4C87B42B602F68002FAB57495BD9098756A9E68BAD4A657F4BDCA2DDB8)

The **updateConfiguration** API is used to instruct an object to update, with the system environment used for the update being determined by the changes in the application's current system environment.

**Example**

import { NodeController, BuilderNode, FrameNode, UIContext, FrameCallback } from "@kit.ArkUI";
import { AbilityConstant, Configuration, ConfigurationConstant, EnvironmentCallback } from '@kit.AbilityKit';

class Params {
  text: string = "";

  constructor(text: string) {
    this.text = text;
  }
}

// Custom component
@Component
struct TextBuilder {
  // The @Prop decorated attribute is the attribute to be updated in the custom component. It is a basic attribute.
  @Prop message: string = "TextBuilder";

  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
          .margin({ bottom: 36 })
      }
    }
  }
}

@Builder
function buildText(params: Params) {
  Column() {
    Text(params.text)
      .fontSize(50)
      .fontWeight(FontWeight.Bold)
      .margin({ bottom: 36 })
    TextBuilder({ message: params.text }) // Custom component
  }.backgroundColor($r('sys.color.ohos\_id\_color\_background'))
}

// Implement a custom textNode controller by extending NodeController.
class TextNodeController extends NodeController {
  private textNode: BuilderNode<\[Params\]> | null = null;
  private message: string = "";

  constructor(message: string) {
    super();
    this.message = message;
  }

  makeNode(context: UIContext): FrameNode | null {
    return this.textNode?.getFrameNode() ? this.textNode?.getFrameNode() : null;
  }

  createNode(context: UIContext) {
    this.textNode = new BuilderNode(context);
    this.textNode.build(wrapBuilder<\[Params\]>(buildText), new Params(this.message));
    builderNodeMap.push(this.textNode);
  }

  deleteNode() {
    let node = builderNodeMap.pop();
    node?.dispose();
  }

  update(message: string) {
    if (this.textNode !== null) {
      // Call update to perform an update.
      this.textNode.update(new Params(message));
    }
  }
}

// Record the created custom node object.
const builderNodeMap: Array<BuilderNode<\[Params\]>> = new Array();

class MyFrameCallback extends FrameCallback {
  onFrame() {
    updateColorMode();
  }
}

function updateColorMode() {
  builderNodeMap.forEach((value, index) => {
    // Notify the BuilderNode of the environment changes to trigger switching between light and dark modes.
    value.updateConfiguration();
  })
}

@Entry
@Component
struct Index {
  @State message: string = "hello";
  private textNodeController: TextNodeController = new TextNodeController(this.message);
  private count = 0;

  aboutToAppear(): void {
    let environmentCallback: EnvironmentCallback = {
      onMemoryLevel: (level: AbilityConstant.MemoryLevel): void => {
        console.info('onMemoryLevel');
      },
      onConfigurationUpdated: (config: Configuration): void => {
        console.info(\`onConfigurationUpdated ${JSON.stringify(config)}\`);
        this.getUIContext()?.postFrameCallback(new MyFrameCallback());
      }
    };
    // Register a callback.
    this.getUIContext().getHostContext()?.getApplicationContext().on('environment', environmentCallback);
    // Set the application color mode to follow the system settings.
    this.getUIContext()
      .getHostContext()?.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR\_MODE\_NOT\_SET);
    // Create a custom node and add it to builderNodeMap.
    this.textNodeController.createNode(this.getUIContext());
  }

  aboutToDisappear(): void {
    // Remove the reference to the custom node from the map and release the node.
    this.textNodeController.deleteNode();
  }

  build() {
    Row() {
      Column() {
        NodeContainer(this.textNodeController)
          .width('100%')
          .height(200)
          .backgroundColor('#FFF0F0F0')
        Button('Update')
          .onClick(() => {
            this.count += 1;
            const message = "Update " + this.count.toString();
            this.textNodeController.update(message);
          })
        Button('Switch to Dark Mode')
          .onClick(() => {
            this.getUIContext()
              .getHostContext()?.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR\_MODE\_DARK);
          })
        Button('Switch to Light Mode')
          .onClick(() => {
            this.getUIContext()
              .getHostContext()?.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR\_MODE\_LIGHT);
          })
      }
      .width('100%')
      .height('100%')
    }
    .height('100%')
  }
}

#### \[h2\]isDisposed20+

isDisposed(): boolean

Checks whether this BuilderNode object has released its reference to its backend entity node. Frontend nodes maintain references to corresponding backend entity nodes. After a node calls the **dispose** API to release this reference, subsequent API calls may cause crashes or return default values. This API facilitates validation of node validity prior to operations, thereby mitigating risks in scenarios where calls after disposal are required.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Whether the reference to the backend node is released. The value **true** means that the reference to backend node is released, and **false** means the opposite. |

**Example**

The following example shows how to verify a BuilderNode's state using the [isDisposed](#isdisposed20) API. This API returns **true** before node release and **false** after node release.

import { FrameNode, NodeController, BuilderNode } from '@kit.ArkUI';

// Custom component
@Component
struct TestComponent {
  build() {
    Column() {
      Text('This is a BuilderNode.')
        .fontSize(25)
        .fontWeight(FontWeight.Bold)
    }
    .width('100%')
    .height(30)
    .backgroundColor(Color.Gray)
  }

  aboutToAppear() {
    console.info('aboutToAppear');
  }

  aboutToDisappear() {
    console.info('aboutToDisappear');
  }
}

@Builder
function buildComponent() {
  TestComponent()
}

// Implement a custom UI controller by extending NodeController.
class MyNodeController extends NodeController {
  private rootNode: FrameNode | null = null;
  private builderNode: BuilderNode<\[\]> | null = null;

  makeNode(uiContext: UIContext): FrameNode | null {
    this.rootNode = new FrameNode(uiContext);
    this.builderNode = new BuilderNode(uiContext, { selfIdealSize: { width: 200, height: 100 } });
    this.builderNode.build(new WrappedBuilder(buildComponent));

    const rootRenderNode = this.rootNode!.getRenderNode();
    if (rootRenderNode !== null) {
      rootRenderNode.size = { width: 300, height: 300 };
      rootRenderNode.backgroundColor = 0xffd5d5d5;
      rootRenderNode.appendChild(this.builderNode!.getFrameNode()!.getRenderNode());
    }

    return this.rootNode;
  }

  // Release the builderNode.
  dispose() {
    if (this.builderNode !== null) {
      this.builderNode.dispose();
    }
  }

  // Check whether the builderNode has been released.
  isDisposed(): string {
    if (this.builderNode !== null) {
      if (this.builderNode.isDisposed()) {
        return 'builderNode isDisposed is true';
      } else {
        return 'builderNode isDisposed is false';
      }
    }
    return 'builderNode is null';
  }

  removeBuilderNode() {
    const rootRenderNode = this.rootNode!.getRenderNode();
    if (rootRenderNode !== null && this.builderNode !== null && this.builderNode.getFrameNode() !== null) {
      rootRenderNode.removeChild(this.builderNode!.getFrameNode()!.getRenderNode());
    }
  }
}

@Entry
@Component
struct Index {
  @State text: string = ''
  private myNodeController: MyNodeController = new MyNodeController();

  build() {
    Column({ space: 4 }) {
      NodeContainer(this.myNodeController)
      Button('BuilderNode dispose')
        .onClick(() => {
          this.myNodeController.removeBuilderNode();
          this.myNodeController.dispose();
          this.text = '';
        })
        .width(200)
        .height(50)
      Button('BuilderNode isDisposed')
        .onClick(() => {
          this.text = this.myNodeController.isDisposed();
        })
        .width(200)
        .height(50)
      Text(this.text)
        .fontSize(25)
    }
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/Fuprt4I0ShisZ-Nv16QCQA/en-us_image_0000002568685059.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7CD2B08EA2D37A9EFE7571B964F9A2E7F60CECC2BBEFB4CC17C997483F2CC4A1)

#### \[h2\]postInputEvent20+

postInputEvent(event: InputEventType): boolean

Dispatches the specified input event to the target node.

**offsetA** indicates the BuilderNode's offset relative to its parent component, **offsetB** the hit position's offset relative to the BuilderNode, **offsetC** the composite offset (offsetA + offsetB) passed to the window in **postInputEvent**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/-QlEwu91Qz2cIMOH7E6pxA/en-us_image_0000002568765069.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AC866AAE8905833EE6224E970DB75CE39AB3CF2EE3F49B3292203CBAD0AC9F9C)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/l7G12WXrTZG0C6oNrWA2Cg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1C87C5DC630976A00B7F33D615AB2F4F1088FB3BB81C7CB4EC551550C6AE0AE5)

-   The passed coordinates must be converted to the unit of px. The sample code below demonstrates how to perform such coordinate conversion.
    
-   Mouse left-click events are automatically converted to touch events. Avoid binding both touch and mouse events at the outer layer, as this may cause coordinate offsets. This is because the **SourceType** remains unchanged during event conversion. For details, see [onTouch](../../../../arkts-components/universal-events/basic-input-events/touch-event/document.md#ontouch).
    
-   When an [axis event](../../../../arkts-components/universal-events/basic-input-events/axis-event/document.md#axisevent) event is injected, it cannot trigger [rotation gestures](../../../../arkts-components/gesture-handling/basic-gestures/rotationgesture/document.md). This is because axis events do not include rotation axis information.
    
-   A forwarded event undergoes touch testing in the target component's subtree and triggers corresponding gestures. The original event also triggers gestures in the source component tree. There is no guaranteed outcome for gesture competition between these two types of gestures.
    
-   For developer-constructed events, mandatory fields must be assigned values, such as the **touches** field for touch events and the **scrollStep** field for axis events Ensure the completeness of the event, for example, both **DOWN** and **UP** [TouchType](../../../../arkts-components/common-definitions/enums/document.md#touchtype) states must be included for a touch event to prevent undefined behavior.
    
-   [webview](../../../../../arkweb/arkts-api/ohos-web-webview-webview/module-description/document.md) has already handled coordinate system transformation, so events can be dispatched delivered.
    
-   The **postTouchEvent** API needs to provide the gesture coordinates relative to the local coordinates of the target component, and the **postInputEvent** API needs to provide the gesture coordinates relative to the window coordinates of the target component.
    
-   Avoid forwarding a single event multiple times.
    

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | [InputEventType](#inputeventtype20) | Yes | Input event to dispatch. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Whether the event is successfully dispatched. Returns **true** if the event is successfully dispatched; returns **false** otherwise. |

**Example**

See [Example 1: Handling Mouse Events in BuilderNode](#example-1-handling-mouse-events-in-buildernode), [Example 2: Handling Touch Events in BuilderNode](#example-2-handling-touch-events-in-buildernode), and [Example 3: Handling Axis Events in BuilderNode](#example-3-handling-axis-events-in-buildernode).

#### \[h2\]inheritFreezeOptions20+

inheritFreezeOptions(enabled: boolean): void

Sets whether this **BuilderNode** object inherits the freeze policy from its parent component's custom components. When inheritance is disabled (set to **false**), the object's freeze policy is set to **false**, which means its associated node remains unfrozen even in an inactive state.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/Kn1ThjKsTG-uOR9EtiQznw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D017BF0D745C12348F513CD05D8AEC92CC18AD96847005DF2FA98EC15F8D14E1)

When **inheritFreezeOptions** is set to **true** for **BuilderNode** and the parent component is a custom component, BuilderNode, ComponentContent, ReactiveBuilderNode, or ReactiveComponentContent, the freeze policy of the parent component is inherited. If the child component is a custom component, its freeze policy is not transferred to the child component.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| enabled | boolean | Yes | Whether the current **BuilderNode** object inherits the freeze policy from its parent component's custom components. The value **true** means to inherit the freeze policy from parent component's custom components, and **false** means the opposite. |

**Example**

The following example illustrates how to configure the BuilderNode to inherit the freeze policy from its parent component, resulting in the following behavior: It automatically freezes when in inactive state and thaws and updates cached data when in active state.

import { BuilderNode, FrameNode, NodeController } from '@kit.ArkUI';

// Define the class for passing parameters.
class Params {
  count: number = 0;

  constructor(count: number) {
    this.count = count;
  }
}

@Builder
// Builder component
function buildText(params: Params) {

  Column() {
    TextBuilder({ message: params.count })
  }
}

// Implement a custom textNode controller by extending NodeController.
class TextNodeController extends NodeController {
  private rootNode: FrameNode | null = null;
  private textNode: BuilderNode<\[Params\]> | null = null;
  private count: number = 0;

  makeNode(context: UIContext): FrameNode | null {
    this.rootNode = new FrameNode(context);
    this.textNode = new BuilderNode(context, { selfIdealSize: { width: 150, height: 150 } });
    this.textNode.build(wrapBuilder<\[Params\]>(buildText), new Params(this.count)); // Create a BuilderNode node.
    this.textNode.inheritFreezeOptions(true); // Configure the BuilderNode to inherit the freeze policy from its parent component.
    if (this.rootNode !== null) {
      this.rootNode.appendChild(this.textNode.getFrameNode()); // Mount the BuilderNode to the component tree.
    }
    return this.rootNode;
  }

  update(): void {
    if (this.textNode !== null) {
      this.count += 1;
      this.textNode.update(new Params(this.count)); // Update the BuilderNode data, which triggers logs.
    }

  }
}

const textNodeController: TextNodeController = new TextNodeController();

@Entry
@Component
struct MyNavigationTestStack {
  @Provide('pageInfo') pageInfo: NavPathStack = new NavPathStack();
  @State message: number = 0;
  @State logNumber: number = 0;

  @Builder
  PageMap(name: string) {
    if (name === 'pageOne') {
      pageOneStack({ message: this.message, logNumber: this.logNumber })
    } else if (name === 'pageTwo') {
      pageTwoStack({ message: this.message, logNumber: this.logNumber })
    }
  }

  build() {
    Column() {
      Button('update builderNode') // Clicking the button updates builderNode.
        .onClick(() => {
          textNodeController.update();
        })
      Navigation(this.pageInfo) {
        Column() {
          Button('Next Page', { stateEffect: true, type: ButtonType.Capsule })
            .width('80%')
            .height(40)
            .margin(20)
            .onClick(() => {
              this.pageInfo.pushPath({ name: 'pageOne' }); // Push the navigation destination page specified by name to the navigation stack.
            })
        }
      }.title('NavIndex')
      .navDestination(this.PageMap)
      .mode(NavigationMode.Stack)
    }
  }
}

@Component
struct pageOneStack { // Page 1
  @Consume('pageInfo') pageInfo: NavPathStack;
  @State index: number = 1;
  @Link message: number;
  @Link logNumber: number;

  build() {
    NavDestination() {
      Column() {
        NavigationContentMsgStack({ message: this.message, index: this.index, logNumber: this.logNumber })
        Button('Next Page', { stateEffect: true, type: ButtonType.Capsule }) // Navigate to page 2.
          .width('80%')
          .height(40)
          .margin(20)
          .onClick(() => {
            this.pageInfo.pushPathByName('pageTwo', null);
          })
        Button('Back Page', { stateEffect: true, type: ButtonType.Capsule }) // Return to the home page.
          .width('80%')
          .height(40)
          .margin(20)
          .onClick(() => {
            this.pageInfo.pop();
          })
      }.width('100%').height('100%')
    }.title('pageOne')
    .onBackPressed(() => {
      this.pageInfo.pop();
      return true;
    })
  }
}

@Component
struct pageTwoStack { // Page 2
  @Consume('pageInfo') pageInfo: NavPathStack;
  @State index: number = 2;
  @Link message: number;
  @Link logNumber: number;

  build() {
    NavDestination() {
      Column() {
        NavigationContentMsgStack({ message: this.message, index: this.index, logNumber: this.logNumber })
        Text('BuilderNode is frozen')
          .fontWeight(FontWeight.Bold)
          .margin({ top: 48, bottom: 48 })
        Button('Back Page', { stateEffect: true, type: ButtonType.Capsule }) // Return to page 1.
          .width('80%')
          .height(40)
          .margin(20)
          .onClick(() => {
            this.pageInfo.pop();
          })
      }.width('100%').height('100%')
    }.title('pageTwo')
    .onBackPressed(() => {
      this.pageInfo.pop();
      return true;
    })
  }
}

@Component({ freezeWhenInactive: true })
  // Set the freeze policy to inactive freeze.
struct NavigationContentMsgStack {
  @Link message: number;
  @Link index: number;
  @Link logNumber: number;

  build() {
    Column() {
      if (this.index === 1) {
        NodeContainer(textNodeController)
      }
    }
  }
}

@Component({ freezeWhenInactive: true })
  // Set the freeze policy to inactive freeze.
struct TextBuilder {
  @Prop @Watch("info") message: number = 0;
  @State count: number = 0;

  info() {
    this.count++;
    console.info(\`freeze-test TextBuilder message callback change time ${this.count}\`); // Log printed when message content changes, used to check for freezes.
    console.info(\`freeze-test TextBuilder message callback change massage ${this.message}\`); // Log printed when message content changes, used to check for freezes.
  }

  build() {
    Row() {
      Column() {
        Text(\`Update content: ${this.message}\`)
          .fontWeight(FontWeight.Bold)
          .margin({ top: 48, bottom: 48 })
        Text(\`Update count: ${this.count}\`)
          .fontWeight(FontWeight.Bold)
          .margin({ top: 48, bottom: 48 })
      }
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/G1wd8WRuTAOX3YLeDYy3pA/en-us_image_0000002537765344.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=28D0A9F78EC0A853C6523BEAA878CE90D89116EDF95E715923DF169E4EF14E11)

#### ReactiveBuilderNode22+

**ReactiveBuilderNode** uses the stateless UI method [@Builder](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-builder) to generate a component tree and holds the root node of the component tree. A **ReactiveBuilderNode** cannot be defined as a state variable. [FrameNode](../framenode/document.md) held in **ReactiveBuilderNode** is used only to mount the **ReactiveBuilderNode** as a child node to another **FrameNode**. Undefined behavior may occur if you set attributes or perform operations on subnodes of the FrameNode held by the ReactiveBuilderNode. Therefore, after you have obtained a RenderNode through the [getFrameNode](#getframenode) method of the ReactiveBuilderNode and the [getRenderNode](../framenode/document.md#getrendernode) method of the [FrameNode](../framenode/document.md), avoid setting the attributes or operating the subnodes through APIs of [RenderNode](../rendernode/document.md).

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### \[h2\]constructor22+

constructor(uiContext: UIContext, options?: RenderOptions)

Constructs a **ReactiveBuilderNode** class. When the content generated by **ReactiveBuilderNode** is embedded into another [RenderNode](../rendernode/document.md) for display, you need to explicitly specify [selfIdealSize](#renderoptions) in [RenderOptions](#renderoptions). Otherwise, the default parent component layout constraint of the nodes in **ReactiveBuilderNode** is \[0, 0\]. If this API is called and **selfIdealSize** is not set, the size of the root node of the subtree in **ReactiveBuilderNode** is \[0, 0\].

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| uiContext | [UIContext](../../ohos-arkui-uicontext-uicontext/class-uicontext/document.md) | Yes | UI context. For details about how to obtain it, see [Obtaining UI Context](../../ohos-arkui-node/document.md#obtaining-ui-context). The value of **uiContext** must be valid, that is, the UI context is correct. If this parameter is invalid or not set, the creation will fail. |
| options | [RenderOptions](#renderoptions) | No | 
Optional parameter for constructing **ReactiveBuilderNode**. This parameter is used to construct the ideal size of the node and the rendering type of the node.

Default value: **undefined**.

 |

#### \[h2\]build22+

build(builder: WrappedBuilder<Args>, config: BuildOptions, ...args: Args): void

Creates a component tree based on the passed object and holds the root node of the component tree. The stateless UI method [@Builder](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-builder) has at most one root node. Multiple parameters can be transferred.

Custom components are allowed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/dDWq5YVXR0Kh6pM5UlGkgw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=95F5470C43C4EFD61E3C36E2A4C59E8BCFDD7CEF99751ACC83152AC1FCED809F)

For details about the creation and update using @Builder, see [@Builder](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-builder).

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| builder | [WrappedBuilder<Args>](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-wrapbuilder) | Yes | Stateless UI method [@Builder](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-builder) required for creating a component tree. |
| config | [BuildOptions](#buildoptions12) | Yes | Configures the build behavior of the builder. All attributes in BuildOptions are optional. The default value is the corresponding default value in BuildOptions. |
| ...args | Args | No | Input arguments of the builder, which are used to construct the **builder** function encapsulated by the **WrappedBuilder** object. Multiple arguments are supported. The default value is **undefined**. |

**Example**

The following example demonstrates how to use the **build** API of **ReactiveBuilderNode** to dynamically create a responsive UI component tree and dynamically update the UI content through data binding.

import { ReactiveBuilderNode, NodeContent, Binding, MutableBinding, UIUtils} from '@kit.ArkUI';

// Builder function, which is used to build UI components that display multiple data records.
@Builder
function buildText(age: Binding<number>, name: MutableBinding<string>, count: number) {
  Column() {
    Text(age.value.toString());
    Text(name.value);
    Text(count.toString());
  }
}

@Entry
@Component
struct Index {
  private content: NodeContent = new NodeContent();
  private age: number = 10;
  private grades: number = 100;

  build() {
    Row() {
      Column() {
        Text()
        // Dynamically create and add a ReactiveBuilderNode when a click occurs.
        Button('add ReactiveBuilderNode').onClick(
          () => {
            // Create a ReactiveBuilderNode instance and specify the types of the three parameters among generic parameters.
            let node = new ReactiveBuilderNode<\[Binding<number>, MutableBinding<string>, number\]>(this.getUIContext());
            
            // Build the node content and pass the builder function and parameters.
            node.build(
              wrapBuilder<\[Binding<number>, Binding<string>, number\]>(buildText),  // Wrap the builder function.
              {},
              UIUtils.makeBinding<number>(() => {
                return this.age
              }),
              UIUtils.makeBinding<string>(() => 'Hello World'),
              this.grades
            );
            // Add the built FrameNode to the content container for display.
            this.content.addFrameNode(node.getFrameNode());
          })
        ContentSlot(this.content)
      }
      .id('column')
      .width('100%')
      .height('100%')
    }
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/alqPvrJHTeaJDAcdQg0JVg/en-us_image_0000002537925284.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A856E2974CDB5C76E73578237BF94399CFF78E577FEB43C2AE37A0BFAF837110)

#### \[h2\]getFrameNode22+

getFrameNode(): FrameNode | null

Obtains the [FrameNode](../framenode/document.md) from the **ReactiveBuilderNode**. The FrameNode is generated only after the ReactiveBuilderNode executes the build operation.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| [FrameNode](../framenode/document.md) | null | **FrameNode** object. If no such object is held by the **ReactiveBuilderNode** instance, **null** is returned. |

**Example**

The following example demonstrates how to use the **getFrameNode** API to obtain the **FrameNode** built by **ReactiveBuilderNode** and dynamically manage the UI node through **NodeContent**.

import { ReactiveBuilderNode, NodeContent, Binding, MutableBinding, UIUtils } from '@kit.ArkUI';

// Builder function, which is used to build UI components that contain text and buttons.
@Builder
function buildText(age: Binding<number>, name: MutableBinding<string>, count: number) {
  Column() {
    Text(age.value.toString());
    Text(name.value);
    Text(count.toString());
    Button('click').onClick(() => {
      name.value = 'new name';
    });
  }
}

interface GeneratedObjectLiteralInterface\_1 {
  age: number;
  name: string;
  count: number;
}

@Entry
@Component
struct Index {
  private content: NodeContent = new NodeContent();  // Dynamic node content container
  @State params: GeneratedObjectLiteralInterface\_1 = {  // State data object
    age: 10,
    name: 'Hello World',
    count: 100
  };

  // Extend the builder.
  @Builder
  extendBlank(age: Binding<number>) {
    Row() {
      Blank();
      Text(\`age: ${age.value}, blank\`);
    }
    .height(20)
  }

  build() {
    Row() {
      Column() {
        Text()
        // Use the buildText builder to build static content.
        buildText(UIUtils.makeBinding<number>(() => {
          return this.params.age
        }),
          UIUtils.makeBinding<string>(() => this.params.name, val => {
            this.params.name = this.params.name + '+1';
          }),
          this.params.count)
        // Use the extendBlank builder to build extended content.
        this.extendBlank(UIUtils.makeBinding<number>(() => {
          return this.params.age
        }))
        
        // Dynamically add ReactiveBuilderNode.
        Button('add ReactiveBuilderNode').onClick(
          () => {
            // Create a ReactiveBuilderNode instance.
            let node = new ReactiveBuilderNode<\[Binding<number>, MutableBinding<string>, number\]>(this.getUIContext());
            
            // Build node content.
            node.build(
              wrapBuilder<\[Binding<number>, Binding<string>, number\]>(buildText),
              {},
              UIUtils.makeBinding<number>(() => {
                return this.params.age
              }),
              UIUtils.makeBinding<string>(() => this.params.name, val => {
                this.params.name = val;
              }),
              this.params.count
            );
            this.content.addFrameNode(node.getFrameNode());
          })
        ContentSlot(this.content)
      }
      .id('column')
      .width('100%')
      .height('100%')
    }
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/IiWOc8kBQTSK_xKIAgroqA/en-us_image_0000002568685061.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=64841584BBFCA6A9D439C142ED162C046AA6943623D86E52F41828C6225A9765)

#### \[h2\]postTouchEvent22+

postTouchEvent(event: TouchEvent): boolean

Posts a raw touch event to the **FrameNode** created by a **ReactiveBuilderNode**.

**postTouchEvent** dispatches the event from a middle node in the component tree downwards. To ensure the event is dispatched correctly, it needs to be transformed into the coordinate system of the parent component, as shown in the figure below.

**OffsetA** indicates the offset of the BuilderNode relative to the parent component. You can obtain this offset by calling [getPositionToParent](../framenode/document.md#getpositiontoparent12) in the FrameNode. **OffsetB** indicates the offset of the touch point relative to the BuilderNode. You can obtain this offset from the [TouchEvent](../../../../arkts-components/universal-events/basic-input-events/touch-event/document.md#touchevent) object. **OffsetC** is the sum of **OffsetA** and **OffsetB**. It represents the final offset that you need to pass to **postTouchEvent**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/VzzC09ADTne14-N5sPupyg/en-us_image_0000002537925282.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=835EAD0A9C38E81C5D00A0082167214ECA6C67EF95729825DD02354A0673EC10)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/PoMISG7nQn-vBugrOwnoZA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CA143A0FCFA5D133C83E77548388F844277E80C0C0DAF201EC20F3BDF3AA2CFE)

The coordinates you pass in need to be converted to pixel values (px). If the BuilderNode has any affine transformations applied to it, they must be taken into account and combined with the touch event coordinates.

In [Webview](../../../../../arkweb/arkts-api/ohos-web-webview-webview/module-description/document.md), coordinate system transformations are already handled internally, so you can directly dispatch the touch event without additional adjustments.

The **postTouchEvent** API can be called only once for the same timestamp.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | [TouchEvent](../../../../arkts-components/universal-events/basic-input-events/touch-event/document.md#touchevent) | Yes | Touch event. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | 
Whether the event is successfully dispatched. Returns **true** if the event is successfully dispatched; returns **false** otherwise.

**NOTE**

If the event does not hit the expected component, ensure the following:

1\. The coordinate system has been correctly transformed

2\. The component is in an interactive state.

3\. The event has been bound to the component.

 |

**Example**

The following example demonstrates coordinate conversion and cross-node transfer of the touch event in the custom node through the linkage between the button component constructed by **ReactiveBuilderNode** and the touch event of the external container.

When the blue area is touched, the touch event is transferred to the **ReactiveBuilderNode** button after coordinate conversion. The touch feedback and log output of the button are triggered, implementing accurate cross-node transfer of the touch event.

import { NodeController, ReactiveBuilderNode, FrameNode, UIContext } from '@kit.ArkUI';

@Builder
function ButtonBuilder() {
  Column() {
    Button(\`Button\`)
      .borderWidth(2)
      .backgroundColor(Color.Gray)
      .width('100%')
      .height('100%')
      .gesture(
        TapGesture()
          .onAction((event: GestureEvent) => {
            console.info('TapGesture');
          })
      )
      .onTouch(() => {
        console.info(\`postTouchEvent Success\`);
      })
  }
  .width(500)
  .height(300)
  .backgroundColor(Color.Gray)
}

// Implement a custom UI controller by extending NodeController.
class MyNodeController extends NodeController {
  private rootNode: ReactiveBuilderNode<\[\]> | null = null;
  private wrapBuilder: WrappedBuilder<\[\]> = wrapBuilder(ButtonBuilder);

  makeNode(uiContext: UIContext): FrameNode | null {
    this.rootNode = new ReactiveBuilderNode(uiContext);
    this.rootNode.build(this.wrapBuilder, {});
    return this.rootNode.getFrameNode();
  }

  // Coordinate system transformation
  postTouchEvent(event: TouchEvent, uiContext: UIContext): boolean {
    if (this.rootNode == null) {
      return false;
    }
    let node: FrameNode | null = this.rootNode.getFrameNode();
    let offsetX: number | null | undefined = node?.getPositionToParent().x;
    let offsetY: number | null | undefined = node?.getPositionToParent().y;

    let changedTouchLen = event.changedTouches.length;
    for (let i = 0; i < changedTouchLen; i++) {
      if (offsetX != null && offsetY != null && offsetX != undefined && offsetY != undefined) {
        event.changedTouches\[i\].x = uiContext.vp2px(offsetX + event.changedTouches\[i\].x);
        event.changedTouches\[i\].y = uiContext.vp2px(offsetY + event.changedTouches\[i\].y);
      }
    }
    let result = this.rootNode.postTouchEvent(event);
    console.info(\`result ${result}\`);
    return result;
  }
}

@Entry
@Component
struct MyComponent {
  private nodeController: MyNodeController = new MyNodeController();

  build() {
    Column() {
      NodeContainer(this.nodeController)
        .height(300)
        .width(500)

      Column()
        .width(500)
        .height(300)
        .backgroundColor('#ADD8E6')
        .onTouch((event) => {
          if (event != undefined) {
            this.nodeController.postTouchEvent(event, this.getUIContext());
          }
        })
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/L6_Jf6fATtmDlhTnvR5oiQ/en-us_image_0000002568765071.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BDBE9C7C159D5D5BC765CE3C8D61ACD14A297A309C24B28D210D5D1736272136)

#### \[h2\]dispose22+

dispose(): void

Immediately releases the reference relationship between this **ReactiveBuilderNode** object and its [entity node](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-user-defined-node#basic-concepts). For details about the scenarios involving ReactiveBuilderNode unbinding, see [Canceling the Reference to the Entity Node](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-user-defined-arktsnode-buildernode#canceling-the-reference-to-the-entity-node).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/8JOBBrRjSTeJuAka7ffe_A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=80DE12D5455D12E9564DD4C09E18971C2AA6C471F8A6CC73C1DB55571384FBE0)

After calling **dispose()**, the ReactiveBuilderNode object cancels its reference to the backend entity node. If the frontend object ReactiveBuilderNode cannot be released, memory leakage may occur. To avoid this, be sure to call **dispose()** on the ReactiveBuilderNode when you no longer need it. This reduces the complexity of reference relationships and lowers the risk of memory leakage.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Example**

The following example demonstrates how to use the **dispose** API to dynamically remove the **ReactiveBuilderNode** component and release resources.

import { FrameNode, NodeController, ReactiveBuilderNode } from '@kit.ArkUI';

@Component
struct TestComponent {
  build() {
    Column() {
      Text('This is a ReactiveBuilderNode.')
        .fontSize(16)
        .fontWeight(FontWeight.Bold)
    }
    .width('100%')
    .backgroundColor(Color.Gray)
  }

  aboutToAppear() {
    console.info('aboutToAppear');
  }

  aboutToDisappear() {
    console.info('aboutToDisappear');
  }
}

@Builder
function buildComponent() {
  TestComponent()
}

// Custom node controller, which manages ReactiveBuilderNode and FrameNode.
class MyNodeController extends NodeController {
  private rootNode: FrameNode | null = null;
  private builderNode: ReactiveBuilderNode<\[\]> | null = null;

  makeNode(uiContext: UIContext): FrameNode | null {
    // Create a root FrameNode.
    this.rootNode = new FrameNode(uiContext);
    this.builderNode = new ReactiveBuilderNode(uiContext, { selfIdealSize: { width: 200, height: 100 } });
    // Build the ReactiveBuilderNode content.
    this.builderNode.build(new WrappedBuilder(buildComponent), {});

    const rootRenderNode = this.rootNode!.getRenderNode();
    if (rootRenderNode !== null) {
      rootRenderNode.size = { width: 200, height: 200 };
      rootRenderNode.backgroundColor = 0xff666666;
      // Add the RenderNode of the ReactiveBuilderNode to the root node.
      rootRenderNode.appendChild(this.builderNode!.getFrameNode()!.getRenderNode());
    }

    return this.rootNode;
  }

  // Release resources.
  dispose() {
    if (this.builderNode !== null) {
      this.builderNode.dispose(); // Release the ReactiveBuilderNode resources.
    }
  }

  // Remove the BuilderNode.
  removeBuilderNode() {
    const rootRenderNode = this.rootNode!.getRenderNode();
    if (rootRenderNode !== null && this.builderNode !== null && this.builderNode.getFrameNode() !== null) {
      // Remove the RenderNode of the BuilderNode from the root node.
      rootRenderNode.removeChild(this.builderNode!.getFrameNode()!.getRenderNode());
    }
  }
}

@Entry
@Component
struct Index {
  private myNodeController: MyNodeController = new MyNodeController();

  build() {
    Column({ space: 4 }) {
      NodeContainer(this.myNodeController)
      // Remove and release the ReactiveBuilderNode.
      Button('ReactiveBuilderNode dispose')
        .onClick(() => {
          this.myNodeController.removeBuilderNode();
          this.myNodeController.dispose();
        })
        .width('70%')
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
    .alignItems(HorizontalAlign.Center)
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/6w17Jh2aSvqHGcNzlWh5Uw/en-us_image_0000002537765346.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9FF41527D093B9CE15C0FE36EF3FF1B404176AADCF74E9BB447F216E0DB64186)

#### \[h2\]reuse22+

reuse(param?: Object): void

Triggers reuse for custom components in **ReactiveBuilderNode**. For details about component reuse, see [@Reusable Decorator: Reusing V1 Components](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-reusable). For details about the scenarios involving ReactiveBuilderNode unbinding, see [Canceling the Reference to the Entity Node](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-user-defined-arktsnode-buildernode#canceling-the-reference-to-the-entity-node).

ReactiveBuilderNode completes the reuse event transfer between internal and external custom components through **reuse** and [recycle](#recycle22). For specific usage scenarios, see [Implementing Node Reuse with the BuilderNode reuse and recycle APIs](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-user-defined-arktsnode-buildernode#implementing-node-reuse-with-the-buildernode-reuse-and-recycle-apis).

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| param | Object | No | Parameter used to reuse [ReactiveBuilderNode](#reactivebuildernode22). This parameter is passed to all top-level custom components within the [ReactiveBuilderNode](#reactivebuildernode22) during reuse and must include all required constructor parameters for each component; otherwise, undefined behavior may occur. Calling this method synchronously triggers the [aboutToReuse](../../../../arkts-components/custom-components/custom-component-lifecycle/document.md#abouttoreuse10) lifecycle callback of internal custom components, with this parameter as the callback input. Default value: **undefined**, in which case the custom components in the ReactiveBuilderNode will use their original construction data source. |

**Example**

For details, see the example in [recycle](#recycle22).

#### \[h2\]recycle22+

recycle(): void

Recycles the custom component in ReactiveBuilderNode. Component recycling is part of the component reuse mechanism. For details, see [@Reusable Decorator: Reusing V1 Components](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-reusable).

ReactiveBuilderNode completes the reuse event transfer between internal and external custom components through [reuse](#reuse22) and **recycle**. For specific usage scenarios, see [Implementing Node Reuse with the BuilderNode reuse and recycle APIs](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-user-defined-arktsnode-buildernode#implementing-node-reuse-with-the-buildernode-reuse-and-recycle-apis).

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Example**

The following example demonstrates how to use the **reuse** and **recycle** APIs of **ReactiveBuilderNode** to implement the component reuse mechanism and optimize the list scrolling performance for the long list.

import { FrameNode, NodeController, ReactiveBuilderNode, UIContext } from '@kit.ArkUI';

const TEST\_TAG: string = 'Reuse+Recycle';

// Custom data source class, which is used to manage list data.
class MyDataSource {
  private dataArray: string\[\] = \[\];
  private listener: DataChangeListener | null = null;

  public totalCount(): number {
    return this.dataArray.length;
  }

  public getData(index: number) {
    return this.dataArray\[index\];
  }

  public pushData(data: string) {
    this.dataArray.push(data);
  }

  public reloadListener(): void {
    this.listener?.onDataReloaded();
  }

  // Register a data change listener.
  public registerDataChangeListener(listener: DataChangeListener): void {
    this.listener = listener;
  }

  public unregisterDataChangeListener(): void {
    this.listener = null;
  }
}

// Builder function, which is used to create a list item UI.
@Builder
function buildNode(text: string) {
  Row() {
    Text(\`C${text} -- \`)
    ReusableChildComponent2({ item: text }) // Nested reusable component.
  }
}

// Custom node controller, which manages ReactiveBuilderNode.
class MyNodeController extends NodeController {
  public builderNode: ReactiveBuilderNode<\[string\]> | null = null;
  public item: string = '';

  // Create a node.
  makeNode(uiContext: UIContext): FrameNode | null {
    if (this.builderNode == null) {
      // Create a ReactiveBuilderNode and set the ideal size.
      this.builderNode = new ReactiveBuilderNode(uiContext, { selfIdealSize: { width: 300, height: 200 } });
      // Use the builder function to build the node content.
      this.builderNode.build(wrapBuilder<\[string\]>(buildNode), {}, this.item);
    }
    return this.builderNode.getFrameNode();
  }
}

@Reusable
@Component
struct ReusableChildComponent {
  @Prop item: string = '';
  @Prop switch: string = '';
  private controller: MyNodeController = new MyNodeController();

  aboutToAppear() {
    this.controller.item = this.item; // Initialize the controller data.
  }

  // Lifecycle callback to be invoked when a component is recycled.
  aboutToRecycle(): void {
    console.info(\`${TEST\_TAG} ReusableChildComponent aboutToRecycle ${this.item}\`);

    // When the switch is turned on, the builderNode is recycled.
    if (this.switch === 'open') {
      this.controller?.builderNode?.recycle();
    }
  }

  // Lifecycle callback to be invoked when a component is reused
  aboutToReuse(params: object): void {
    console.info(\`${TEST\_TAG} ReusableChildComponent aboutToReuse ${JSON.stringify(params)}\`);

    // When the switch is turned on, the builderNode is reused.
    if (this.switch === 'open') {
      this.controller?.builderNode?.reuse(params);
    }
  }

  build() {
    Row() {
      Text(\`A${this.item}--\`)
      ReusableChildComponent3({ item: this.item })
      NodeContainer(this.controller); // NodeContainer is contained for displaying custom nodes.
    }
  }
}

@Component
struct ReusableChildComponent2 {
  @Prop item: string = 'false';

  // Callback invoked upon reuse.
  aboutToReuse(params: Record<string, object>) {
    console.info(\`${TEST\_TAG} ReusableChildComponent2 aboutToReuse ${JSON.stringify(params)}\`);
  }

  // Callback invoked upon recycling.
  aboutToRecycle(): void {
    console.info(\`${TEST\_TAG} ReusableChildComponent2 aboutToRecycle ${this.item}\`);
  }

  build() {
    Row() {
      Text(\`D${this.item}\`)
        .fontSize(20)
        .backgroundColor(Color.Yellow)
        .margin({ left: 10 })
    }.margin({ left: 10, right: 10 })
  }
}

@Component
struct ReusableChildComponent3 {
  @Prop item: string = 'false';

  // Callback invoked upon reuse.
  aboutToReuse(params: Record<string, object>) {
    console.info(\`${TEST\_TAG} ReusableChildComponent3 aboutToReuse ${JSON.stringify(params)}\`);
  }

  // Callback invoked upon recycling.
  aboutToRecycle(): void {
    console.info(\`${TEST\_TAG} ReusableChildComponent3 aboutToRecycle ${this.item}\`);
  }

  build() {
    Row() {
      Text(\`B${this.item}\`)
        .fontSize(20)
        .backgroundColor(Color.Yellow)
        .margin({ left: 10 })
    }.margin({ left: 10, right: 10 })
  }
}

@Entry
@Component
struct Index {
  @State data: MyDataSource = new MyDataSource();

  aboutToAppear() {
    // Initialize the list data.
    for (let i = 0; i < 100; i++) {
      this.data.pushData(i.toString());
    }
  }

  build() {
    Column() {
      // Use LazyForEach to render the long list and support component reuse.
      List({ space: 3 }) {
        LazyForEach(this.data, (item: string) => {
          ListItem() {
            ReusableChildComponent({
              item: item,
              switch: 'open' // Enable the reuse and recycling features.
            })
          }
        }, (item: string) => item)
      }
      .width('100%')
      .height('100%')
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/R0iZgQbTQZyqHo-5TJl8yg/en-us_image_0000002537925286.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A8EA425E89DF32B3E6E71DB75A612A6ABE7EFF5E591262AF13E3F47A9D577E8A)

#### \[h2\]updateConfiguration22+

updateConfiguration(): void

Updates the configuration of the entire node by passing in a [system environment change](../../../../../ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-configuration-environment-variables/document.md) event. This event can be used to notify the object of the update. Whether the system environment used by the object is updated depends on the current system environment change of the application.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Example**

The following example shows how to use the **updateConfiguration** API to respond to system environment changes and dynamically update the UI node constructed by **ReactiveBuilderNode**.

import { NodeController, ReactiveBuilderNode, FrameNode, UIContext, FrameCallback, Binding, UIUtils } from '@kit.ArkUI';
import { AbilityConstant, Configuration, ConfigurationConstant, EnvironmentCallback } from '@kit.AbilityKit';

// Custom component
@Component
struct TextBuilder {
  // The @Prop decorated attribute is the attribute to be updated in the custom component. It is a basic attribute.
  @Prop message: string = 'TextBuilder';

  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize(20)
          .fontWeight(FontWeight.Bold)
          .margin({ bottom: 30 })
      }
      .justifyContent(FlexAlign.Center)
      .alignItems(HorizontalAlign.Center)
      .width('100%')
    }
    .width('100%')
  }
}

@Builder
function buildText(text: Binding<string>) {
  Column() {
    Text(text.value)
      .fontSize(20)
      .fontWeight(FontWeight.Bold)
      .margin({ bottom: 15 })
    TextBuilder({ message: text.value }) // Custom component.
  }
  .backgroundColor($r('sys.color.ohos\_id\_color\_background'))
  .justifyContent(FlexAlign.Center)
  .alignItems(HorizontalAlign.Center)
  .width('100%')
  .height('100%')
}

// Implement a custom textNode controller by extending NodeController.
class TextNodeController extends NodeController {
  private textNode: ReactiveBuilderNode<\[Binding<string>\]> | null = null;
  private message: string = '';

  constructor(message: string) {
    super();
    this.message = message;
  }

  makeNode(context: UIContext): FrameNode | null {
    return this.textNode?.getFrameNode() ? this.textNode?.getFrameNode() : null;
  }

  createNode(context: UIContext) {
    this.textNode = new ReactiveBuilderNode(context);
    this.textNode.build(wrapBuilder<\[Binding<string>\]>(buildText), {},
      UIUtils.makeBinding<string>(() => this.message, val => {
        this.message = val;
      }));
    builderNodeMap.push(this.textNode);
  }

  deleteNode() {
    let node = builderNodeMap.pop();
    node?.dispose();
  }

  update(message: string) {
    this.message = message
    this.textNode?.flushState();
  }
}

// Record the created custom node object.
const builderNodeMap: Array<ReactiveBuilderNode<\[text: Binding<string>\]>> = new Array();

class MyFrameCallback extends FrameCallback {
  onFrame() {
    updateColorMode();
  }
}

function updateColorMode() {
  builderNodeMap.forEach((value, index) => {
    // Notify the BuilderNode of the environment changes to trigger switching between light and dark modes.
    value.updateConfiguration();
  })
}

@Entry
@Component
struct Index {
  @State message: string = 'hello';
  private textNodeController: TextNodeController = new TextNodeController(this.message);
  private count = 0;

  aboutToAppear(): void {
    let environmentCallback: EnvironmentCallback = {
      onMemoryLevel: (level: AbilityConstant.MemoryLevel): void => {
        console.info('onMemoryLevel');
      },
      onConfigurationUpdated: (config: Configuration): void => {
        console.info(\`onConfigurationUpdated ${JSON.stringify(config)}\`);
        this.getUIContext()?.postFrameCallback(new MyFrameCallback());
      }
    };
    // Register a callback.
    this.getUIContext().getHostContext()?.getApplicationContext().on('environment', environmentCallback);
    // Set the application color mode to follow the system settings.
    this.getUIContext()
      .getHostContext()?.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR\_MODE\_NOT\_SET);
    // Create a custom node and add it to builderNodeMap.
    this.textNodeController.createNode(this.getUIContext());
  }

  aboutToDisappear(): void {
    // Remove the reference from builderNodeMap and release the custom node.
    this.textNodeController.deleteNode();
  }

  build() {
    Row() {
      Column({ space: 12 }) {
        NodeContainer(this.textNodeController)
          .width('100%')
          .height(70)
          .backgroundColor('#FFF0F0F0')
        Button('Update')
          .onClick(() => {
            this.count += 1;
            const message = 'Update ' + this.count.toString();
            this.textNodeController.update(message);
          })
        Button('Switch to Dark Mode')
          .onClick(() => {
            this.getUIContext()
              .getHostContext()?.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR\_MODE\_DARK);
          })
        Button('Switch to Light Mode')
          .onClick(() => {
            this.getUIContext()
              .getHostContext()?.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR\_MODE\_LIGHT);
          })
      }
      .width('100%')
      .height('100%')
    }
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/kXJOHPWwRVuSDa-fKBPUmA/en-us_image_0000002568685063.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=06CF6B20300DE4A703C2AFA0E36763F3010A8783387EDF7E2A8CFB0C3FD9B7C8)

#### \[h2\]flushState22+

flushState(): void

Updates the **ReactiveBuilderNode** based on the provided parameters. If the bound parameters used in the **builder** function encapsulated by the [WrappedBuilder](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-wrapbuilder) object in **ReactiveBuilderNode** are class instances decorated by the V1 decorator (such as @Observed), you need to manually call this API to update data after the data of this class changes. If the bound parameters are class instances decorated by the V2 decorator (such as @ObservedV2), the data can be automatically updated without manual calling.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Example**

The following example demonstrates how to use the **flushState** API in V1 and V2 decorators and update the **ReactiveBuilderNode** in different data response mechanisms.

import { ReactiveBuilderNode, NodeContent, Binding, UIUtils } from '@kit.ArkUI';

@Builder
function buildText(age: Binding<number>) {
  Column() {
    Text(\`age: ${age.value}\`);
  }
}

// Class decorated by the V2 decorator, which supports automatic state update.
@ObservedV2
class GeneratedObjectLiteralInterface\_1 {
  constructor(age: number) {
    this.age = age;
  }

  @Trace age: number = 0;
}

// Use a common class (V1 decorator style). You need to manually trigger the update.
class GeneratedObjectLiteralInterface\_2 {
  constructor(age: number) {
    this.age = age;
  }

  age: number = 0;
}

@Entry
@ComponentV2
struct Index {
  private content: NodeContent = new NodeContent();
  params: GeneratedObjectLiteralInterface\_1 = new GeneratedObjectLiteralInterface\_1(25);
  params2: GeneratedObjectLiteralInterface\_2 = new GeneratedObjectLiteralInterface\_2(25);
  private node1: ReactiveBuilderNode<\[Binding<number>\]> | null = null

  build() {
    Row() {
      Scroll() {
        Column({ space: 12 }) {
          // Create ReactiveBuilderNode using the V2 decorator.
          Button('Bound parameters are decorated by the V2 decorator').onClick(
            () => {
              let node =
                new ReactiveBuilderNode<\[Binding<number>\]>(this.getUIContext());
              node.build(
                wrapBuilder<\[Binding<number>\]>(buildText),
                {},
                UIUtils.makeBinding<number>(() => {
                  return this.params.age;
                })
              );
              this.content.addFrameNode(node.getFrameNode());
            })
          // Create ReactiveBuilderNode using the V1 decorator.
          Button('Bound parameters are decorated by the V1 decorator').onClick(
            () => {
              this.node1 =
                new ReactiveBuilderNode<\[Binding<number>\]>(this.getUIContext());
              this.node1.build(
                wrapBuilder<\[Binding<number>\]>(buildText),
                {},
                UIUtils.makeBinding<number>(() => {
                  return this.params2.age;
                })
              );
              this.content.addFrameNode(this.node1.getFrameNode());
            })
          Button('change age - V2 can be automatically updated').onClick(() => {
            this.params.age += 1; // The V2 decorator automatically detects changes and updates the UI.
          })
          Button('change age - V1 must be manually updated').onClick(() => {
            this.params2.age += 1;
            // For the data of the V1 decorator, you need to manually call flushState to trigger UI update.
            this.node1?.flushState();
          })
          // Display the dynamically created content.
          ContentSlot(this.content)
        }
        .id("column")
        .width('100%')
      }
      .scrollable(ScrollDirection.Vertical)
      .scrollBar(BarState.On)
      .scrollBarColor(Color.Gray)
      .scrollBarWidth(10)
    }
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/Riua-PzIS8u39PcxnnMYrg/en-us_image_0000002568765073.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AF9940A11D811D9D450073367209DC73F76F8944208FF5467DD07162A3E5B78A)

#### \[h2\]postInputEvent22+

postInputEvent(event: InputEventType): boolean

Posts the input event to the target node managed by the **ReactiveBuilderNode**.

**offsetA** indicates the **BuilderNode**'s offset relative to its parent component, **offsetB** the hit position's offset relative to the **BuilderNode**, **offsetC** the composite offset (offsetA + offsetB) passed to the **postInputEvent**.

! [API coordinate conversion example](en-us_image_0000002537925282.png)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/V5n20EyOQHOXxlp6eWJXeA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=362E35779362A9604A6815B5A7C87329F844522CEDF635F370935B1495CBEB44)

The passed coordinates must be converted to the unit of px. The sample code below demonstrates how to perform such coordinate conversion.

Mouse left-click events are automatically converted to touch events. Avoid binding both touch and mouse events at the outer layer, as this may cause coordinate offsets. This is because the **SourceType** remains unchanged during event conversion. For details, see [onTouch](../../../../arkts-components/universal-events/basic-input-events/touch-event/document.md#ontouch).

When an [axis event](../../../../arkts-components/universal-events/basic-input-events/axis-event/document.md#axisevent) event is injected, it cannot trigger [rotation gestures](../../../../arkts-components/gesture-handling/basic-gestures/rotationgesture/document.md). This is because axis events do not include rotation axis information.

A forwarded event undergoes touch testing in the target component's subtree and triggers corresponding gestures. The original event also triggers gestures in the source component tree. There is no guaranteed outcome for gesture competition between these two types of gestures.

For the event you construct, the mandatory fields must be assigned values, for example, the **touches** field of the touch event and the **scrollStep** field of the axis event. In addition, ensure the completeness of the event, for example, both **DOWN** and **UP** in [TouchType](../../../../arkts-components/common-definitions/enums/document.md#touchtype) of the touch event must be included to prevent undefined behavior.

[webview](../../../../../arkweb/arkts-api/ohos-web-webview-webview/module-description/document.md) has already handled coordinate system transformation, so events can be dispatched delivered.

The **postTouchEvent** API needs to provide the gesture coordinates relative to the local coordinates of the target component, and the **postInputEvent** API needs to provide the gesture coordinates relative to the window coordinates of the target component.

Avoid forwarding a single event multiple times.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | [InputEventType](#inputeventtype20) | Yes | Input event to be posted. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Whether the event is successfully dispatched. Returns **true** if the event is successfully dispatched; returns **false** otherwise. |

**Example**

For details, see [Example 6: Handling Mouse Events in ReactiveBuilderNode](#example-6-handling-mouse-events-in-reactivebuildernode), [Example 7: Handling Touch Events in ReactiveBuilderNode](#example-7-handling-touch-events-in-reactivebuildernode), and [Example 8: Handling Axis Events in ReactiveBuilderNode](#example-8-handling-axis-events-in-reactivebuildernode).

#### \[h2\]inheritFreezeOptions22+

inheritFreezeOptions(enabled: boolean): void

Sets whether this **ReactiveBuilderNode** object inherits the freeze policy from its parent component's custom components. When inheritance is disabled (set to **false**), the **ReactiveBuilderNode** object's freeze policy is set to **false**, which means its associated node remains unfrozen even in an inactive state.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/glTW3N6nR5ewASFdh92NBg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3AC6EE6D415AB914B5E8F2491AD400F86594F883C332C3EEB5A4E0670A020FA9)

When **inheritFreezeOptions** is set to **true** for **ReactiveBuilderNode** and the parent component is a custom component, **BuilderNode**, **ComponentContent**, **ReactiveBuilderNode**, or **ReactiveComponentContent**, the freeze policy of the parent component is inherited. If the child component is a custom component, its freeze policy is not transferred to the child component.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| enabled | boolean | Yes | Whether the current **ReactiveBuilderNode** object inherits the freeze policy from its parent component's custom components. The value **true** means to inherit the freeze policy from parent component's custom components, and **false** means the opposite. |

**Example**

The following example demonstrates how to inherit the freeze policy of the parent custom component when ReactiveBuilderNode is set to **true**. When the page is switched to the inactive state, the component is frozen. When the page is switched back to the active state, the component is unfrozen and the cached data is updated.

import { ReactiveBuilderNode, FrameNode, NodeController, Binding, UIUtils } from '@kit.ArkUI';

@Builder
function buildText(count: Binding<number>) {
  Column() {
    TextBuilder({ message: count.value })
  }
}

// Custom node controller (the logic remains unchanged.)
class TextNodeController extends NodeController {
  private rootNode: FrameNode | null = null;
  private textNode: ReactiveBuilderNode<\[Binding<number>\]> | null = null;
  private count: number = 0; // Internal counting status

  makeNode(context: UIContext): FrameNode | null {
    this.rootNode = new FrameNode(context);
    this.textNode = new ReactiveBuilderNode(context, { selfIdealSize: { width: 150, height: 150 } });
    // Build node content.
    this.textNode.build(wrapBuilder<\[Binding<number>\]>(buildText), {}, UIUtils.makeBinding<number>(() => {
      return this.count
    }));
    // Set inheritFreezeOptions to true. When the parent component is frozen, the child component is automatically frozen.
    this.textNode.inheritFreezeOptions(true);
    // Add ReactiveBuilderNode to the root node.
    if (this.rootNode !== null) {
      this.rootNode.appendChild(this.textNode.getFrameNode());
    }
    return this.rootNode;
  }

  update(): void {
    if (this.textNode !== null) {
      this.count += 1; // Increase the count.
      this.textNode.flushState();
    }
  }
}

const textNodeController: TextNodeController = new TextNodeController();

@Entry
@Component
struct MyNavigationTestStack {
  @Provide('pageInfo') pageInfo: NavPathStack = new NavPathStack();
  @State message: number = 0;
  @State logNumber: number = 0;

  @Builder
  PageMap(name: string) {
    if (name === 'pageOne') {
      pageOneStack({ message: $message, logNumber: $logNumber })
    } else if (name === 'pageTwo') {
      pageTwoStack({ message: $message, logNumber: $logNumber })
    }
  }

  @Builder
  CustomTitle() {
    Text('NavIndex')
      .fontSize(20)
      .fontColor(Color.Black)
      .fontWeight(FontWeight.Normal)
  }

  build() {
    Column() {
      Button('update builderNode')
        .fontSize(18)
        .onClick(() => {
          textNodeController.update();
        })

      Navigation(this.pageInfo) {
        Column() {
          Button('Next Page', { stateEffect: true, type: ButtonType.Capsule })
            .fontSize(18)
            .width('80%')
            .height(40)
            .margin(10)
            .onClick(() => {
              this.pageInfo.pushPath({ name: 'pageOne' });
            })
        }
      }
      .title(this.CustomTitle)
      .navDestination(this.PageMap)
      .mode(NavigationMode.Stack)
    }
    .width('100%')
    .height('100%')
    .padding(10)
  }
}

@Component
struct pageOneStack { // Page 1
  @Consume('pageInfo') pageInfo: NavPathStack;
  @State index: number = 1;
  @Link message: number;
  @Link logNumber: number;

  build() {
    NavDestination() {
      Column() {
        NavigationContentMsgStack({ message: this.message, index: this.index, logNumber: this.logNumber })

        Button('Next Page', { stateEffect: true, type: ButtonType.Capsule })
          .fontSize(18)
          .width('80%')
          .height(40)
          .margin(8)
          .onClick(() => {
            this.pageInfo.pushPathByName('pageTwo', null);
          })

        Button('Back Page', { stateEffect: true, type: ButtonType.Capsule })
          .fontSize(18)
          .width('80%')
          .height(40)
          .margin(8)
          .onClick(() => {
            this.pageInfo.pop();
          })
      }
      .width('100%')
      .height('100%')
    }
    .title('pageOne')
    .onBackPressed(() => {
      this.pageInfo.pop();
      return true;
    })
  }
}

@Component
struct pageTwoStack { // Page 2
  @Consume('pageInfo') pageInfo: NavPathStack;
  @State index: number = 2;
  @Link message: number;
  @Link logNumber: number;

  build() {
    NavDestination() {
      Column({ space: 8 }) {
        NavigationContentMsgStack({ message: this.message, index: this.index, logNumber: this.logNumber })

        Text('BuilderNode is frozen')
          .fontSize(18)
          .fontWeight(FontWeight.Bold)
          .margin({ top: 16, bottom: 16 })

        Button('Back Page', { stateEffect: true, type: ButtonType.Capsule })
          .fontSize(18)
          .width('80%')
          .height(40)
          .margin(8)
          .onClick(() => {
            this.pageInfo.pop();
          })
      }
      .width('100%')
      .height('100%')
    }
    .title('pageTwo')
    .onBackPressed(() => {
      this.pageInfo.pop();
      return true;
    })
  }
}

@Component({ freezeWhenInactive: true })
  // Enable the freeze policy when the page is inactive.
struct NavigationContentMsgStack {
  @Link message: number;
  @Link index: number;
  @Link logNumber: number;

  build() {
    Column() {
      if (this.index === 1) {
        NodeContainer(textNodeController)
          .margin({ bottom: 5 })
      }
    }
  }
}

// Text builder component, which supports freezing.
@Component({ freezeWhenInactive: true })
struct TextBuilder {
  @Prop @Watch('info') message: number = 0;
  @State count: number = 0;

  info() {
    this.count++;
    console.info(\`freeze-test TextBuilder message callback change time ${this.count}\`);
    console.info(\`freeze-test TextBuilder message callback change massage ${this.message}\`);
  }

  build() {
    Row() {
      Column() {
        Text(\`Update content: ${this.message}\`)
          .fontSize(18)
          .fontWeight(FontWeight.Bold)
          .margin({ top: 16, bottom: 16 })

        Text(\`Update count: ${this.count}\`)
          .fontSize(18)
          .fontWeight(FontWeight.Bold)
          .margin({ top: 16, bottom: 16 })
      }
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/rW0A9NdATmK_JtQPLCFA3Q/en-us_image_0000002537765348.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=29D0AABA0A3DC0B28FB6BEE338F5BD7E06A40746321529AB1C5327523038B128)

#### \[h2\]isDisposed22+

isDisposed(): boolean

Queries whether the current **ReactiveBuilderNode** object has released its reference to its backend entity node. Frontend nodes maintain references to corresponding backend entity nodes. After a node calls the **dispose** API to release this reference, subsequent API calls may cause crashes or return default values. This API facilitates validation of node validity prior to operations, thereby mitigating risks in scenarios where calls after disposal are required.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Whether the reference to the backend node is released. The value **true** means that the reference to backend node is released, and **false** means the opposite. |

**Example**

For details, see [isDisposed](#isdisposed20).

The following example demonstrates how to verify a **ReactiveBuilderNode**'s state using the [isDisposed](#isdisposed22) API. This API returns **true** before node release and **false** after node release.

import { FrameNode, NodeController, ReactiveBuilderNode } from '@kit.ArkUI';

@Component
struct TestComponent {
  build() {
    Column() {
      Text('This is a BuilderNode.')
        .fontSize(25)
        .fontWeight(FontWeight.Bold)
    }
    .width('100%')
    .height(30)
    .backgroundColor(Color.Gray)
  }

  aboutToAppear() {
    console.info('aboutToAppear');
  }

  aboutToDisappear() {
    console.info('aboutToDisappear');
  }
}

@Builder
function buildComponent() {
  TestComponent()
}

// Implement a custom UI controller by extending NodeController.
class MyNodeController extends NodeController {
  private rootNode: FrameNode | null = null; // Root FrameNode container.
  private builderNode: ReactiveBuilderNode<\[\]> | null = null; // ReactiveBuilderNode instance.

  makeNode(uiContext: UIContext): FrameNode | null {
    this.rootNode = new FrameNode(uiContext);
    this.builderNode = new ReactiveBuilderNode(uiContext, { selfIdealSize: { width: 200, height: 100 } });
    // Build the ReactiveBuilderNode content and use WrappedBuilder to wrap the Builder function.
    this.builderNode.build(new WrappedBuilder(buildComponent), {});

    const rootRenderNode = this.rootNode!.getRenderNode();
    if (rootRenderNode !== null) {
      rootRenderNode.size = { width: 300, height: 50 };
      rootRenderNode.backgroundColor = 0xffd5d5d5;
      // Add the RenderNode of the ReactiveBuilderNode to the root node.
      rootRenderNode.appendChild(this.builderNode!.getFrameNode()!.getRenderNode());
    }

    return this.rootNode;
  }

  // Release resources.
  dispose() {
    if (this.builderNode !== null) {
      this.builderNode.dispose(); // Release the ReactiveBuilderNode resources.
    }
  }

  // Check whether the node has been released.
  isDisposed(): string {
    if (this.builderNode !== null) {
      if (this.builderNode.isDisposed()) {
        return 'builderNode isDisposed is true';
      } else {
        return 'builderNode isDisposed is false';
      }
    }
    return 'builderNode is null';
  }

  removeBuilderNode() {
    const rootRenderNode = this.rootNode!.getRenderNode();
    if (rootRenderNode !== null && this.builderNode !== null && this.builderNode.getFrameNode() !== null) {
      // Remove the RenderNode of the BuilderNode from the root node.
      rootRenderNode.removeChild(this.builderNode!.getFrameNode()!.getRenderNode());
    }
  }
}

@Entry
@Component
struct Index {
  @State text: string = '' // State variable, which is used to display node status information.
  private myNodeController: MyNodeController = new MyNodeController();

  build() {
    Column({ space: 4 }) {
      NodeContainer(this.myNodeController)
      Button('BuilderNode dispose')
        .onClick(() => {
          this.myNodeController.removeBuilderNode();
          this.myNodeController.dispose(); // Release the resources.
          this.text = '';
        })
        .width(200)
        .height(50)
      Button('BuilderNode isDisposed')
        .onClick(() => {
          this.text = this.myNodeController.isDisposed();
        })
        .width(200)
        .height(50)
      // Display node status information.
      Text(this.text)
        .fontSize(20)
    }
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/_oWf75NYT3iR5admjpYBng/en-us_image_0000002537925288.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9F47B74C9B1F6A523C6C1F3297CC5F496D98504169CFF0312A0B23DBFEC1C34C)

#### Example

## Example 1: Handling Mouse Events in BuilderNode

This example demonstrates the end-to-end process for intercepting mouse events in a custom component and performing coordinate conversion. The component reads local x- and y-coordinates through the [onMouse](../../../../arkts-components/universal-events/basic-input-events/mouse-event/document.md#onmouse) callback, then uses **vp2px** to convert relative coordinates to pixel coordinates based on the offset obtained from FrameNode.[getPositionToParent](../framenode/document.md#getpositiontoparent12)(). The **windowX**, **windowY**, **displayX**, and **displayY** values in [MouseEvent](../../../../arkts-components/universal-events/basic-input-events/mouse-event/document.md#mouseevent) are updated accordingly. Finally, the converted mouse event is dispatched to child nodes through rootNode.[postInputEvent](#postinputevent20)(event).

import { NodeController, BuilderNode, FrameNode, PromptAction, UIContext, InputEventType } from '@kit.ArkUI';

// Define the class for passing parameters.
class Params {
  text: string = "this is a text"
  uiContext: UIContext | null = null
}

@Builder
function ButtonBuilder(params: Params) {
  Column() {
    Button(params.text)
      .borderWidth(2)
      .align(Alignment.Center)
      .backgroundColor(Color.Orange)
      .fontSize(20)
      .width("45%")
      .height("30%")
      .offset({ x: 60, y: 100 })
      .borderRadius('50%')
      .onMouse((event) => {
        let promptAction: PromptAction = params.uiContext!.getPromptAction();
        promptAction.showToast({
          message: 'onMouse',
          duration: 3000
        });
        console.info('onMouse')
      })
      .onTouch((event) => {
        let promptAction: PromptAction = params.uiContext!.getPromptAction();
        promptAction.showToast({
          message: 'onTouch',
          duration: 3000
        });
        console.info('onTouch')
      })
  }
  .width(500)
  .height(300)
  .backgroundColor(Color.Gray)
}

// Implement a custom UI controller by extending NodeController.
class MyNodeController extends NodeController {
  private rootNode: BuilderNode<\[Params\]> | null = null;
  private wrapBuilder: WrappedBuilder<\[Params\]> = wrapBuilder(ButtonBuilder);

  makeNode(uiContext: UIContext): FrameNode | null {
    this.rootNode = new BuilderNode(uiContext);
    this.rootNode.build(this.wrapBuilder, { text: "This is a string", uiContext })
    return this.rootNode.getFrameNode();
  }

  postMouseEvent(event: InputEventType, uiContext: UIContext): boolean {
    if (this.rootNode == null) {
      return false;
    }
    // Read the x and y offsets of buildNode relative to its parent component and convert them to pixel coordinates.
    let node: FrameNode | null = this.rootNode.getFrameNode();
    let offsetX: number | null | undefined = node?.getPositionToParent().x;
    let offsetY: number | null | undefined = node?.getPositionToParent().y;

    let mouseEvent = event as MouseEvent;
    if (offsetX != null && offsetY != null && offsetX != undefined && offsetY != undefined) {
      mouseEvent.windowX = uiContext.vp2px(offsetX + mouseEvent.x);
      mouseEvent.windowY = uiContext.vp2px(offsetY + mouseEvent.y);
    }
    // Post the mouse event to the FrameNode created by BuilderNode. result indicates whether the post is successful.
    let result = this.rootNode.postInputEvent(event);
    return result;
  }

  postTouchEvent(event: InputEventType, uiContext: UIContext): boolean {
    if (this.rootNode == null) {
      return false;
    }
    // Read the x and y offsets of buildNode relative to its parent component and convert them to pixel coordinates.
    let node: FrameNode | null = this.rootNode.getFrameNode();
    let offsetX: number | null | undefined = node?.getPositionToParent().x;
    let offsetY: number | null | undefined = node?.getPositionToParent().y;

    let touchEvent = event as TouchEvent;
    let changedTouchLen = touchEvent.changedTouches.length;
    for (let i = 0; i < changedTouchLen; i++) {
      if (offsetX != null && offsetY != null && offsetX != undefined && offsetY != undefined) {
        touchEvent.changedTouches\[i\].windowX = uiContext.vp2px(offsetX + touchEvent.changedTouches\[i\].x);
        touchEvent.changedTouches\[i\].windowY = uiContext.vp2px(offsetY + touchEvent.changedTouches\[i\].y);
      }
    }
    let touchesLen = touchEvent.touches.length;
    for (let i = 0; i < touchesLen; i++) {
      if (offsetX != null && offsetY != null && offsetX != undefined && offsetY != undefined) {
        touchEvent.touches\[i\].windowX = uiContext.vp2px(offsetX + touchEvent.touches\[i\].x);
        touchEvent.touches\[i\].windowY = uiContext.vp2px(offsetY + touchEvent.touches\[i\].y);
      }
    }
    // Post the touch event to the FrameNode created by BuilderNode. result indicates whether the post is successful.
    let result = this.rootNode.postInputEvent(event);
    return result;
  }
}

@Entry
@Component
struct MyComponent {
  private nodeController: MyNodeController = new MyNodeController();

  build() {
    Stack() {
      NodeContainer(this.nodeController)
        .height(300)
        .width(500)
      Column()
        .width(500)
        .height(300)
        .backgroundColor(Color.Transparent)
        .onMouse((event) => {
          if (event != undefined) {
            this.nodeController.postMouseEvent(event, this.getUIContext());
          }
        })
        .onTouch((event) => {
          if (event != undefined) {
            this.nodeController.postTouchEvent(event, this.getUIContext());
          }
        })
    }.offset({ top: 100 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/l9J37qL4SGSQVtASvOUMOw/en-us_image_0000002568685065.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3258820ECB1DA4AA11915F04619BA44B92C6AA33662AD1D88526563CBB16353A)

## Example 2: Handling Touch Events in BuilderNode

This example demonstrates the end-to-end process for intercepting touch events in a custom component and transforming touch point coordinates. The implementation: 1. iterates through **changedTouches** and **touches** arrays of [TouchEvent](../../../../arkts-components/universal-events/basic-input-events/touch-event/document.md#touchevent) in the [onTouch](../../../../arkts-components/universal-events/basic-input-events/touch-event/document.md#ontouch) callback; 2. for each touch point, adds the component offset to the X and Y coordinates and converts the result to pixels using **vp2px**; 3. updates the **windowX**, **windowY**, **displayX**, and **displayY** values of each touch point; 4. posts the processed touch event to child nodes using **rootNode.postInputEvent(event)**.

import { NodeController, BuilderNode, FrameNode, UIContext, PromptAction, InputEventType } from '@kit.ArkUI';

// Define the class for passing parameters.
class Params {
  text: string = "this is a text"
  uiContext: UIContext | null = null
}

@Builder
function ButtonBuilder(params: Params) {
  Column() {
    Button(params.text)
      .borderWidth(2)
      .align(Alignment.Center)
      .backgroundColor(Color.Orange)
      .fontSize(20)
      .width("45%")
      .height("30%")
      .offset({ x: 60, y: 100 })
      .borderRadius('50%')
      .onTouch((event) => {
        let promptAction: PromptAction = params.uiContext!.getPromptAction();
        promptAction.showToast({
          message: 'onTouch',
          duration: 3000
        });
        console.info('onTouch')
      })
  }
  .width(500)
  .height(300)
  .backgroundColor(Color.Gray)
}

// Implement a custom UI controller by extending NodeController.
class MyNodeController extends NodeController {
  private rootNode: BuilderNode<\[Params\]> | null = null;
  private wrapBuilder: WrappedBuilder<\[Params\]> = wrapBuilder(ButtonBuilder);

  makeNode(uiContext: UIContext): FrameNode | null {
    this.rootNode = new BuilderNode(uiContext);
    this.rootNode.build(this.wrapBuilder, { text: "This is a string", uiContext })
    return this.rootNode.getFrameNode();
  }

  postInputEvent(event: InputEventType, uiContext: UIContext): boolean {
    if (this.rootNode == null) {
      return false;
    }
    // Read the x and y offsets of buildNode relative to its parent component and convert them to pixel coordinates.
    let node: FrameNode | null = this.rootNode.getFrameNode();
    let offsetX: number | null | undefined = node?.getPositionToParent().x;
    let offsetY: number | null | undefined = node?.getPositionToParent().y;

    // Forward only original touch events, not mouse-simulated touch events.
    if (event.source == SourceType.TouchScreen) {
      let touchEvent = event as TouchEvent;
      let changedTouchLen = touchEvent.changedTouches.length;
      for (let i = 0; i < changedTouchLen; i++) {
        if (offsetX != null && offsetY != null && offsetX != undefined && offsetY != undefined) {
          touchEvent.changedTouches\[i\].windowX = uiContext.vp2px(offsetX + touchEvent.changedTouches\[i\].x);
          touchEvent.changedTouches\[i\].windowY = uiContext.vp2px(offsetY + touchEvent.changedTouches\[i\].y);
        }
      }
      let touchesLen = touchEvent.touches.length;
      for (let i = 0; i < touchesLen; i++) {
        if (offsetX != null && offsetY != null && offsetX != undefined && offsetY != undefined) {
          touchEvent.touches\[i\].windowX = uiContext.vp2px(offsetX + touchEvent.touches\[i\].x);
          touchEvent.touches\[i\].windowY = uiContext.vp2px(offsetY + touchEvent.touches\[i\].y);
        }
      }
    }

    // Post the touch event to the FrameNode created by BuilderNode. result indicates whether the post is successful.
    let result = this.rootNode.postInputEvent(event);
    return result;
  }
}

@Entry
@Component
struct MyComponent {
  private nodeController: MyNodeController = new MyNodeController();

  build() {
    Stack() {
      NodeContainer(this.nodeController)
        .height(300)
        .width(500)
      Column()
        .width(500)
        .height(300)
        .backgroundColor(Color.Transparent)
        .onTouch((event) => {
          if (event != undefined) {
            this.nodeController.postInputEvent(event, this.getUIContext());
          }
        })
    }.offset({ top: 100 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/pJI1A54iRhu4oJ8kcu_FPw/en-us_image_0000002568765075.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4559F8939B1A6DE0DD056094C78F164E28617635C5724C8B1B23CC1CC32C317F)

## Example 3: Handling Axis Events in BuilderNode

This example demonstrates the end-to-end process for intercepting wheel or trackpad axis events in a custom component and performing coordinate conversion. The implementation: 1. obtains relative X and Y coordinates from the [onAxisEvent](../../../../arkts-components/universal-events/basic-input-events/axis-event/document.md#onaxisevent) callback; 2. adds the component offset and converts the result to pixels using **vp2px**; 3. updates the **windowX**, **windowY**, **displayX**, and **displayY** values in **AxisEvent**; 4. posts the transformed axis event to child nodes using **rootNode.postInputEvent(event)**.

import { NodeController, BuilderNode, FrameNode, UIContext, PromptAction, InputEventType } from '@kit.ArkUI';

// Define the class for passing parameters.
class Params {
  text: string = "this is a text"
  uiContext: UIContext | null = null
}

@Builder
function ButtonBuilder(params: Params) {
  Column() {
    Button(params.text)
      .borderWidth(2)
      .align(Alignment.Center)
      .backgroundColor(Color.Orange)
      .fontSize(20)
      .width("45%")
      .height("30%")
      .offset({ x: 60, y: 100 })
      .borderRadius('50%')
      .onAxisEvent((event) => {
        let promptAction: PromptAction = params.uiContext!.getPromptAction();
        promptAction.showToast({
          message: 'onAxisEvent',
          duration: 3000
        });
        console.info('onAxisEvent')
      })
  }
  .width(500)
  .height(300)
  .backgroundColor(Color.Gray)
}

// Implement a custom UI controller by extending NodeController.
class MyNodeController extends NodeController {
  private rootNode: BuilderNode<\[Params\]> | null = null;
  private wrapBuilder: WrappedBuilder<\[Params\]> = wrapBuilder(ButtonBuilder);

  makeNode(uiContext: UIContext): FrameNode | null {
    this.rootNode = new BuilderNode(uiContext);
    this.rootNode.build(this.wrapBuilder, { text: "This is a string", uiContext })
    return this.rootNode.getFrameNode();
  }

  postInputEvent(event: InputEventType, uiContext: UIContext): boolean {
    if (this.rootNode == null) {
      return false;
    }
    // Read the x and y offsets of buildNode relative to its parent component and convert them to pixel coordinates.
    let node: FrameNode | null = this.rootNode.getFrameNode();
    let offsetX: number | null | undefined = node?.getPositionToParent().x;
    let offsetY: number | null | undefined = node?.getPositionToParent().y;

    let axisEvent = event as AxisEvent;
    if (offsetX != null && offsetY != null && offsetX != undefined && offsetY != undefined) {
      axisEvent.windowX = uiContext.vp2px(offsetX + axisEvent.x);
      axisEvent.windowY = uiContext.vp2px(offsetY + axisEvent.y);
    }
    // Post the axis event to the FrameNode created by BuilderNode. result indicates whether the post is successful.
    let result = this.rootNode.postInputEvent(event);
    return result;
  }
}

@Entry
@Component
struct MyComponent {
  private nodeController: MyNodeController = new MyNodeController();

  build() {
    Stack() {
      NodeContainer(this.nodeController)
        .height(300)
        .width(500)
      Column()
        .width(500)
        .height(300)
        .backgroundColor(Color.Transparent)
        .onAxisEvent((event) => {
          if (event != undefined) {
            this.nodeController.postInputEvent(event, this.getUIContext());
          }
        })
    }.offset({ top: 100 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/HkEiI_F_RDmPlKDa-iGmZQ/en-us_image_0000002537765350.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=96AB33366BE23E791596F552D21975DC35C324335C51C1A62A22D27DD5383F1B)

## Example 4: Passing a BuilderNode Shared localStorage Instance

This example demonstrates how to pass an external [localStorage](../../../../arkts-components/state-management-and-rendering-control/state-management-with-application-level-variables/document.md#localstorage9) instance to a BuilderNode through the **build** method, enabling all custom components mounted under the BuilderNode to share the same **localStorage** instance.

import { NodeController, BuilderNode, FrameNode, UIContext } from '@kit.ArkUI';

// Define the class for passing parameters.
class Params {
  text: string = ""

  constructor(text: string) {
    this.text = text;
  }
}

let globalBuilderNode: BuilderNode<\[Params\]> | null = null;

@Builder
function buildText(params: Params) {
  Column() {
    Text('BuildNodeContentArea')
      .fontSize(25)
    CustomComp()
  }
}

// Implement a custom textNode controller by extending NodeController.
class TextNodeController extends NodeController {
  private rootNode: FrameNode | null = null;

  makeNode(context: UIContext): FrameNode | null {
    this.rootNode = new FrameNode(context);
    if (globalBuilderNode === null) {
      globalBuilderNode = new BuilderNode(context);
      // Pass the external LocalStorage to be shared by all custom components mounted to the current BuilderNode.
      globalBuilderNode.build(wrapBuilder<\[Params\]>(buildText), new Params('builder node text'),
        { localStorage: localStorage1 })
    }
    this.rootNode.appendChild(globalBuilderNode.getFrameNode());
    return this.rootNode;
  }
}

// Create LocalStorage and set initial values.
let localStorage1: LocalStorage = new LocalStorage();
localStorage1.setOrCreate('PropA', 'PropA');

@Entry(localStorage1)
@Component
struct Index {
  private controller: TextNodeController = new TextNodeController();
  @LocalStorageLink('PropA') PropA: string = 'Hello World';

  build() {
    Row() {
      Column() {
        Text(this.PropA)
        NodeContainer(this.controller)
        Button('changeLocalstorage').onClick(() => {
          localStorage1.set('PropA', 'AfterChange')
        })
      }
    }
  }
}

@Component
struct CustomComp {
  @LocalStorageLink('PropA') PropA: string = 'Hello World';

  build() {
    Row() {
      Column() {
        Text(this.PropA)
      }
    }
  }
}

## Example 5: Configuring the BuilderNode for Cross-Boundary @Provide-@Consume Communication

Set **enableProvideConsumeCrossing** in [BuildOptions](#buildoptions12) of the **BuilderNode** to **true** to implement two-way synchronization between the @Consume decorated variable of the custom component inside the **BuilderNode** and the @Provide decorated variable outside the **BuilderNode**.

import { BuilderNode, NodeContent } from '@kit.ArkUI';

// Custom component
@Component
struct ConsumeChild {
  // Two-way synchronization with the state variable decorated with the @Provider outside the BuilderNode.
  @Consume @Watch("ChangeData") message: string = ""

  ChangeData() {
    console.info(\`ChangeData ${this.message}\`);
  }

  build() {
    Column() {
      Text(this.message)
        .fontWeight(FontWeight.Bold)
        .fontSize(20)
      Button("Click to change message to append C")
        .fontWeight(FontWeight.Bold)
        .onClick(() => {
          // Modify the @Consume decorated variable.
          this.message = this.message + "C"
        })
    }
  }
}

@Builder
function CreateText(textMessage: string) {
  Column() {
    Text(textMessage)
      .fontWeight(FontWeight.Bold)
      .fontSize(20)
    ConsumeChild()
  }
}

@Entry
@Component
struct Index {
  // Two-way synchronization with the state variable decorated with the @Consumer inside the BuilderNode.
  @Provide message: string = 'Hello World';
  private content: NodeContent = new NodeContent();
  private builderNode: BuilderNode<\[string\]> = new BuilderNode<\[string\]>(this.getUIContext());

  aboutToAppear(): void {
    // Set enableProvideConsumeCrossing to true to support two-way synchronization between the @Consume decorated variable of the custom component ConsumeChild inside the BuilderNode and the @Provide decorated variable on the page where the ConsumeChild component is located.
    this.builderNode.build(wrapBuilder(CreateText), "Test Consume", { enableProvideConsumeCrossing: true })
    this.content.addFrameNode(this.builderNode.getFrameNode())
  }

  build() {
    Column() {
      Text(this.message)
        .fontWeight(FontWeight.Bold)
        .fontSize(20)
      Button("Click to change message to append I")
        .fontWeight(FontWeight.Bold)
        .onClick(() => {
          this.message = this.message + "I";
        })
      Column() {
        ContentSlot(this.content)
      }
    }
    .height('100%')
    .width('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/TgXuIrgyRbitiU4xGWt0KQ/en-us_image_0000002537925290.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8064FDFFF0DD5F805D350C57743A730500F5BD9140BDC7BC25B59CD877C3D6B3)

## Example 6: Handling Mouse Events in ReactiveBuilderNode

The functionality demonstrated in this example is supported starting from API version 22.

This example demonstrates the end-to-end process for intercepting mouse events in a custom component and performing coordinate conversion. The component reads the local X and Y coordinates through the [onMouse](../../../../arkts-components/universal-events/basic-input-events/mouse-event/document.md#onmouse) callback, calls [vp2px](../../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#vp2px12) to convert the relative coordinates to pixel coordinates based on the offset obtained by **FrameNode.**[getPositionToParent](../framenode/document.md#getpositiontoparent12)**()**, and updates **windowX**, **windowY**, **displayX**, and **displayY** of [MouseEvent](../../../../arkts-components/universal-events/basic-input-events/mouse-event/document.md#mouseevent). Finally, the component uses **rootNode.**[postInputEvent](#postinputevent20) to post the converted mouse event to the child node for handling.

import { NodeController, ReactiveBuilderNode, FrameNode, PromptAction, UIContext, InputEventType } from '@kit.ArkUI';

@Builder
function ButtonBuilder(text: string, uiContext: UIContext) {
  Column() {
    Button(text)
      .borderWidth(2)
      .align(Alignment.Center)
      .backgroundColor(Color.Orange)
      .fontSize(15)
      .width('45%')
      .height('30%')
      .offset({ y: 70 })
      // Handle the mouse event.
      .onMouse((event) => {
        let promptAction: PromptAction = uiContext!.getPromptAction();
        promptAction.showToast({
          message: 'onMouse',
          duration: 3000
        });
        console.info('onMouse')
      })
      // Handle the touch event.
      .onTouch((event) => {
        let promptAction: PromptAction = uiContext!.getPromptAction();
        promptAction.showToast({
          message: 'onTouch',
          duration: 3000
        });
        console.info('onTouch')
      })
  }
  .width(500)
  .height(200)
  .backgroundColor(Color.Gray)
}

// Implement a custom UI controller by extending NodeController.
class MyNodeController extends NodeController {
  private rootNode: ReactiveBuilderNode<\[text: string, uiContext: UIContext\]> | null = null;
  private wrapBuilder: WrappedBuilder<\[text: string, uiContext: UIContext\]> = wrapBuilder(ButtonBuilder);

  makeNode(uiContext: UIContext): FrameNode | null {
    this.rootNode = new ReactiveBuilderNode(uiContext);
    this.rootNode.build(this.wrapBuilder, {}, 'onMouse', uiContext)
    return this.rootNode.getFrameNode();
  }

  postMouseEvent(event: InputEventType, uiContext: UIContext): boolean {
    if (this.rootNode == null) {
      return false;
    }
    let node: FrameNode | null = this.rootNode.getFrameNode();
    // Obtain the offset of the node relative to the parent component.
    let offsetX: number | null | undefined = node?.getPositionToParent().x;
    let offsetY: number | null | undefined = node?.getPositionToParent().y;

    let mouseEvent = event as MouseEvent;
    // Coordinate conversion: Convert the event coordinates to the node coordinates.
    if (offsetX != null && offsetY != null && offsetX != undefined && offsetY != undefined) {
      mouseEvent.windowX = uiContext.vp2px(offsetX + mouseEvent.x);
      mouseEvent.windowY = uiContext.vp2px(offsetY + mouseEvent.y);
    }
    // Call postInputEvent to post the converted event to the ReactiveBuilderNode.
    let result = this.rootNode.postInputEvent(event);
    return result;
  }

  // Handle the touch event.
  postTouchEvent(event: InputEventType, uiContext: UIContext): boolean {
    if (this.rootNode == null) {
      return false;
    }
    let node: FrameNode | null = this.rootNode.getFrameNode();
    // Obtain the offset of the node relative to the parent component.
    let offsetX: number | null | undefined = node?.getPositionToParent().x;
    let offsetY: number | null | undefined = node?.getPositionToParent().y;

    let touchEvent = event as TouchEvent;
    // Convert the coordinates of all touch points in the changedTouches array.
    let changedTouchLen = touchEvent.changedTouches.length;
    for (let i = 0; i < changedTouchLen; i++) {
      if (offsetX != null && offsetY != null && offsetX != undefined && offsetY != undefined) {
        touchEvent.changedTouches\[i\].windowX = uiContext.vp2px(offsetX + touchEvent.changedTouches\[i\].x);
        touchEvent.changedTouches\[i\].windowY = uiContext.vp2px(offsetY + touchEvent.changedTouches\[i\].y);
      }
    }
    // Convert the coordinates of all touch points in the touches array.
    let touchesLen = touchEvent.touches.length;
    for (let i = 0; i < touchesLen; i++) {
      if (offsetX != null && offsetY != null && offsetX != undefined && offsetY != undefined) {
        touchEvent.touches\[i\].windowX = uiContext.vp2px(offsetX + touchEvent.touches\[i\].x);
        touchEvent.touches\[i\].windowY = uiContext.vp2px(offsetY + touchEvent.touches\[i\].y);
      }
    }
    // Call postInputEvent to post the converted event to the ReactiveBuilderNode.
    let result = this.rootNode.postInputEvent(event);
    return result;
  }
}

@Entry
@Component
struct MyComponent {
  private nodeController: MyNodeController = new MyNodeController();

  build() {
    Stack() {
      NodeContainer(this.nodeController)
        .height(300)
        .width(500)
      Column()
        .width(500)
        .height(300)
        .margin({ top: 500 })
        .backgroundColor(Color.Transparent)
        // Capture the mouse event and post it to the custom node.
        .onMouse((event) => {
          if (event != undefined) {
            this.nodeController.postMouseEvent(event, this.getUIContext());
          }
        })
        // Capture the touch event and post it to the custom node.
        .onTouch((event) => {
          if (event != undefined) {
            this.nodeController.postTouchEvent(event, this.getUIContext());
          }
        })
    }.offset({ top: 180 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/9gPo42dGQu-ZTqeu2pR-5g/en-us_image_0000002568685067.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F08D67D32D9D6BF2EF33609F0C4C2A7949CA55D5E74EFB2CD9FE3DD6849B43A5)

## Example 7: Handling Touch Events in ReactiveBuilderNode

The functionality demonstrated in this example is supported starting from API version 22.

This example demonstrates the end-to-end process for intercepting touch events in a custom component and transforming touch point coordinates. In the [onTouch](../../../../arkts-components/universal-events/basic-input-events/touch-event/document.md#ontouch) callback, iterate through the **changedTouches** and **touches** arrays of [TouchEvent](../../../../arkts-components/universal-events/basic-input-events/touch-event/document.md#touchevent), add the component offset to the X and Y coordinates of each touch point, call [vp2px](../../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#vp2px12) to convert the coordinates to pixels, and update **windowX**/**windowY** and **displayX**/**displayY**. Finally, **rootNode.**[postInputEvent](#postinputevent20) is used to post the converted touch event to the child node for handling.

import { NodeController, ReactiveBuilderNode, FrameNode, UIContext, PromptAction, InputEventType } from '@kit.ArkUI';

@Builder
function ButtonBuilder(text: string, uiContext: UIContext) {
  Column() {
    Button(text)
      .borderWidth(2)
      .align(Alignment.Center)
      .backgroundColor(Color.Orange)
      .fontSize(15)
      .width('45%')
      .height('30%')
      .offset({ y: 70 })
      // Handle the touch event.
      .onTouch((event) => {
        let promptAction: PromptAction = uiContext!.getPromptAction();
        promptAction.showToast({
          message: 'onTouch',
          duration: 3000
        });
        console.info('onTouch')
      })
  }
  .width(500)
  .height(200)
  .backgroundColor(Color.Gray)
}

class MyNodeController extends NodeController {
  private rootNode: ReactiveBuilderNode<\[text: string, uiContext: UIContext\]> | null = null;
  private wrapBuilder: WrappedBuilder<\[text: string, uiContext: UIContext\]> =
    wrapBuilder<\[text: string, uiContext: UIContext\]>(ButtonBuilder);

  makeNode(uiContext: UIContext): FrameNode | null {
    this.rootNode = new ReactiveBuilderNode(uiContext);
    // Build the ReactiveBuilderNode and transfer the button text and UI context.
    this.rootNode.build(this.wrapBuilder, {}, 'onTouch', uiContext)
    return this.rootNode.getFrameNode();
  }

  postInputEvent(event: InputEventType, uiContext: UIContext): boolean {
    if (this.rootNode == null) {
      return false;
    }
    let node: FrameNode | null = this.rootNode.getFrameNode();
    // Obtain the offset of the node relative to the parent component.
    let offsetX: number | null | undefined = node?.getPositionToParent().x;
    let offsetY: number | null | undefined = node?.getPositionToParent().y;

    if (event.source == SourceType.TouchScreen) {
      let touchEvent = event as TouchEvent;
      // Convert the coordinates of all touch points in the changedTouches array.
      let changedTouchLen = touchEvent.changedTouches.length;
      for (let i = 0; i < changedTouchLen; i++) {
        if (offsetX != null && offsetY != null && offsetX != undefined && offsetY != undefined) {
          touchEvent.changedTouches\[i\].windowX = uiContext.vp2px(offsetX + touchEvent.changedTouches\[i\].x);
          touchEvent.changedTouches\[i\].windowY = uiContext.vp2px(offsetY + touchEvent.changedTouches\[i\].y);
        }
      }
      // Convert the coordinates of all touch points in the touches array.
      let touchesLen = touchEvent.touches.length;
      for (let i = 0; i < touchesLen; i++) {
        if (offsetX != null && offsetY != null && offsetX != undefined && offsetY != undefined) {
          touchEvent.touches\[i\].windowX = uiContext.vp2px(offsetX + touchEvent.touches\[i\].x);
          touchEvent.touches\[i\].windowY = uiContext.vp2px(offsetY + touchEvent.touches\[i\].y);
        }
      }
    }

    // Call postInputEvent to post the converted event to the ReactiveBuilderNode.
    let result = this.rootNode.postInputEvent(event);
    return result;
  }
}

@Entry
@Component
struct MyComponent {
  private nodeController: MyNodeController = new MyNodeController();

  build() {
    Stack() {
      NodeContainer(this.nodeController)
        .height(300)
        .width(500)
      Column()
        .width(500)
        .height(300)
        .margin({ top: 600 })
        .backgroundColor(Color.Transparent)
        // Capture the touch event and post it to the custom node.
        .onTouch((event) => {
          if (event != undefined) {
            this.nodeController.postInputEvent(event, this.getUIContext());
          }
        })
    }.offset({ top: 180 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/atfY2IZdR-6TiVLFFa3yoA/en-us_image_0000002568765077.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=640365A289E89FF30D99E951E6B2D10BF368D15219A86394B632314A03AFDD53)

## Example 8: Handling Axis Events in ReactiveBuilderNode

The functionality demonstrated in this example is supported starting from API version 22.

This example demonstrates the end-to-end process for intercepting wheel or trackpad axis events in a custom component and performing coordinate conversion. In the [onAxisEvent](../../../../arkts-components/universal-events/basic-input-events/axis-event/document.md#onaxisevent) callback, obtain the relative X and Y coordinates of the axis event, add the component offset, call [vp2px](../../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#vp2px12) to convert the coordinates to pixels, update the **windowX**/**windowY** and **displayX**/**displayY** of the axis event, and use **rootNode.**[postInputEvent](#postinputevent20) to post the converted axis event to the child node for handling.

import { NodeController, ReactiveBuilderNode, FrameNode, UIContext, PromptAction, InputEventType } from '@kit.ArkUI';

@Builder
function ButtonBuilder(text: string, uiContext: UIContext) {
  Column() {
    Button(text)
      .borderWidth(2)
      .align(Alignment.Center)
      .backgroundColor(Color.Orange)
      .fontSize(15)
      .width("45%")
      .height("30%")
      .offset({ y: 80 })
      .onAxisEvent((event) => {
        let promptAction: PromptAction = uiContext!.getPromptAction();
        promptAction.showToast({
          message: 'onAxisEvent', // Display the message when the axis event is triggered.
          duration: 3000
        });
        console.info('onAxisEvent')
      })
  }
  .width(500)
  .height(200)
  .backgroundColor(Color.Gray)
}

// Implement a custom UI controller by extending NodeController.
class MyNodeController extends NodeController {
  private rootNode: ReactiveBuilderNode<\[text: string, uiContext: UIContext\]> | null = null;
  private wrapBuilder: WrappedBuilder<\[text: string, uiContext: UIContext\]> =
    wrapBuilder<\[text: string, uiContext: UIContext\]>(ButtonBuilder);

  makeNode(uiContext: UIContext): FrameNode | null {
    this.rootNode = new ReactiveBuilderNode(uiContext);
    // Build the ReactiveBuilderNode and transfer the button text and UI context.
    this.rootNode.build(this.wrapBuilder, {}, 'onAxisEvent', uiContext)
    return this.rootNode.getFrameNode();
  }

  // Handle the axis event.
  postInputEvent(event: InputEventType, uiContext: UIContext): boolean {
    if (this.rootNode == null) {
      return false;
    }
    // Read the x and y offsets of buildNode relative to its parent component and convert them to pixel coordinates.
    let node: FrameNode | null = this.rootNode.getFrameNode();
    let offsetX: number | null | undefined = node?.getPositionToParent().x;
    let offsetY: number | null | undefined = node?.getPositionToParent().y;

    let axisEvent = event as AxisEvent;
    if (offsetX != null && offsetY != null && offsetX != undefined && offsetY != undefined) {
      axisEvent.windowX = uiContext.vp2px(offsetX + axisEvent.x);
      axisEvent.windowY = uiContext.vp2px(offsetY + axisEvent.y);
    }
    // Call postInputEvent to post the converted event to the ReactiveBuilderNode.
    let result = this.rootNode.postInputEvent(event);
    return result;
  }
}

@Entry
@Component
struct MyComponent {
  private nodeController: MyNodeController = new MyNodeController();

  build() {
    Stack() {
      NodeContainer(this.nodeController)
        .height(300)
        .width(500)
      Column()
        .width(500)
        .height(300)
        .margin({ top: 600 })
        .backgroundColor(Color.Transparent)
        // Capture the axis event and post it to the custom node.
        .onAxisEvent((event) => {
          if (event != undefined) {
            // Call the axis event handling method.
            this.nodeController.postInputEvent(event, this.getUIContext());
          }
        })
    }.offset({ top: 180 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/GgDvWaHKTpu4hfBFQaUOIQ/en-us_image_0000002537765352.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=77ECD3F46A76487FF7813D63CA64F1126324A2C937B6E23D4F03E6DADD96B1AF)
