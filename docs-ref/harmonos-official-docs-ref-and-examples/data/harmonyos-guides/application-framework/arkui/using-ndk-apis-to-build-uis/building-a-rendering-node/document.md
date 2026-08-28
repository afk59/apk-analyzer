# Building a Rendering Node

Since API version 20, the ArkUI development framework provides NDK APIs for directly building rendering nodes. These capabilities include rendering node tree operations, attribute configuration, and custom drawing with animations. By leveraging rendering node capabilities, you can bypass the measurement and layout processes associated with [registerNodeCustomEvent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1#registernodecustomevent), directly draw nodes, and adjust their sizes and positions.

-   **Rendering node tree operations**: APIs such as [OH\_ArkUI\_RenderNodeUtils\_AddRenderNode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-render-h#oh_arkui_rendernodeutils_addrendernode) and [OH\_ArkUI\_RenderNodeUtils\_AddChild](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-render-h#oh_arkui_rendernodeutils_addchild) are used to modify the structure of the rendering node tree. Rendering nodes can only be mounted to custom nodes of the ARKUI\_NODE\_CUSTOM type that have no other child nodes (linked to native nodes). Only one rendering node can be mounted per custom node. Specifically, the rendering node is attached as a subtree to a leaf custom node of the ARKUI\_NODE\_CUSTOM type.
    
-   **Rendering node attribute configuration**: For details about APIs used to set rendering node attributes, see [Functions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-render-h#functions).
    
-   **Custom drawing**: For implementation details, see [OH\_ArkUI\_RenderNodeUtils\_SetContentModifierOnDraw](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-render-h#oh_arkui_rendernodeutils_setcontentmodifierondraw) and its associated APIs. You can also use ContentModifier bound APIs (for example, [OH\_ArkUI\_RenderNodeUtils\_SetFloatPropertyValue](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-render-h#oh_arkui_rendernodeutils_setfloatpropertyvalue)) to dynamically modify the content to be drawn.
    

#### Mounting Nodes and Setting Basic Attributes

The following example demonstrates how to create a rendering node, mount it to a custom node, and configure its basic attributes.

1.  Follow the instructions in [Integrating with ArkTS Pages](../integrating-with-arkts-pages/document.md) to create a project.
    
2.  Create a rendering node capability object.
    
    // NativeEntry.cpp
    // Example of a custom container component
    #include <arkui/native\_animate.h>
    #include <arkui/native\_render.h>
    #include <arkui/native\_type.h>
    #include <arkui/native\_node\_napi.h>
    #include <bits/alltypes.h>
    
    #include <string>
    
    #include <arkui/native\_interface.h>
    #include <arkui/native\_node.h>
    #include <native\_drawing/drawing\_canvas.h>
    #include <native\_drawing/drawing\_color.h>
    #include <native\_drawing/drawing\_path.h>
    #include <native\_drawing/drawing\_pen.h>
    
    ArkUI\_NodeHandle testRenderNode(ArkUI\_NativeNodeAPI\_1 \*nodeAPI) {
        //Create the original container logic of the NDK.
        ArkUI\_NodeHandle scroll = nodeAPI->createNode(ARKUI\_NODE\_SCROLL);
        ArkUI\_NumberValue valueWidth\[\] = {400};
        ArkUI\_AttributeItem itemWidth = {valueWidth, sizeof(valueWidth) / sizeof(ArkUI\_NumberValue)};
        nodeAPI->setAttribute(scroll, NODE\_WIDTH, &itemWidth);
        ArkUI\_NumberValue valueHeight\[\] = {600};
        ArkUI\_AttributeItem itemHeight = {valueHeight, sizeof(valueHeight) / sizeof(ArkUI\_NumberValue)};
        nodeAPI->setAttribute(scroll, NODE\_HEIGHT, &itemHeight);
        ArkUI\_NodeHandle column = nodeAPI->createNode(ARKUI\_NODE\_COLUMN);
        nodeAPI->setAttribute(column, NODE\_WIDTH, &itemWidth);
        nodeAPI->setAttribute(column, NODE\_HEIGHT, &itemHeight);
        ArkUI\_NodeHandle text = nodeAPI->createNode(ARKUI\_NODE\_TEXT);
        ArkUI\_AttributeItem content = {.string = "The yellow background is the C API page."};
        nodeAPI->setAttribute(text, NODE\_TEXT\_CONTENT, &content);
        nodeAPI->addChild(column, text);
    
        // Create a RenderNode container – custom component on the NDK side.
        ArkUI\_NodeHandle Custom = nodeAPI->createNode(ARKUI\_NODE\_CUSTOM);
        valueWidth\[0\].f32 = 400;
        nodeAPI->setAttribute(Custom, NODE\_WIDTH, &itemWidth);
        nodeAPI->setAttribute(Custom, NODE\_HEIGHT, &itemWidth);
        nodeAPI->addChild(column, Custom);
    
        // Create, mount, and build the rendering node tree.
        // Create the rendering node and its child nodes.
        auto renderRootNode = OH\_ArkUI\_RenderNodeUtils\_CreateNode();
        auto firstChildRenderNode = OH\_ArkUI\_RenderNodeUtils\_CreateNode();
        auto secondChildRenderNode = OH\_ArkUI\_RenderNodeUtils\_CreateNode();
        auto thirdChildRenderNode = OH\_ArkUI\_RenderNodeUtils\_CreateNode();
    
        auto result = OH\_ArkUI\_RenderNodeUtils\_AddRenderNode(Custom, renderRootNode);
        if (result != ARKUI\_ERROR\_CODE\_NO\_ERROR) {
            // Check whether the root node is successfully mounted based on the error code.
            return scroll;
        }
        
        OH\_ArkUI\_RenderNodeUtils\_AddChild(renderRootNode, firstChildRenderNode);
        OH\_ArkUI\_RenderNodeUtils\_AddChild(renderRootNode, secondChildRenderNode);
        OH\_ArkUI\_RenderNodeUtils\_AddChild(renderRootNode, thirdChildRenderNode);
        
        // Set the node sizes and positions.
        OH\_ArkUI\_RenderNodeUtils\_SetSize(renderRootNode, 500, 500);
        OH\_ArkUI\_RenderNodeUtils\_SetSize(firstChildRenderNode, 120, 120);
        OH\_ArkUI\_RenderNodeUtils\_SetSize(secondChildRenderNode, 120, 120);
        OH\_ArkUI\_RenderNodeUtils\_SetSize(thirdChildRenderNode, 120, 120);
    
        OH\_ArkUI\_RenderNodeUtils\_SetPosition(renderRootNode, 300, 100);
        OH\_ArkUI\_RenderNodeUtils\_SetPosition(firstChildRenderNode, 0, 0);
        OH\_ArkUI\_RenderNodeUtils\_SetPosition(secondChildRenderNode, 140, 140);
        OH\_ArkUI\_RenderNodeUtils\_SetPosition(thirdChildRenderNode, 280, 280);
        
        // Set background colors for rendering nodes (for visual distinction).
        OH\_ArkUI\_RenderNodeUtils\_SetBackgroundColor(renderRootNode, 0xFFFFFFFF);
        OH\_ArkUI\_RenderNodeUtils\_SetBackgroundColor(firstChildRenderNode, 0xFFFF0000); // R
        OH\_ArkUI\_RenderNodeUtils\_SetBackgroundColor(secondChildRenderNode, 0xFF00FF00); // G
        OH\_ArkUI\_RenderNodeUtils\_SetBackgroundColor(thirdChildRenderNode, 0xFF0000FF); // B
        
        // Simple attribute example
        OH\_ArkUI\_RenderNodeUtils\_SetRotation(secondChildRenderNode, 45, 45, 0); // Rotate the node 45 degrees around the x-axis and y-axis and 0 degrees around the z-axis.
    
        // Border attribute example
        auto styleOption = OH\_ArkUI\_RenderNodeUtils\_CreateNodeBorderStyleOption();
        OH\_ArkUI\_RenderNodeUtils\_SetNodeBorderStyleOptionEdgeStyle(styleOption, ArkUI\_BorderStyle::ARKUI\_BORDER\_STYLE\_SOLID,
                                                                   ArkUI\_EdgeDirection::ARKUI\_EDGE\_DIRECTION\_ALL);
        OH\_ArkUI\_RenderNodeUtils\_SetBorderStyle(firstChildRenderNode, styleOption);
        // After using the structure, destroy it to free memory.
        OH\_ArkUI\_RenderNodeUtils\_DisposeNodeBorderStyleOption(styleOption);
        styleOption = nullptr;
        
        auto widthOption = OH\_ArkUI\_RenderNodeUtils\_CreateNodeBorderWidthOption();
        OH\_ArkUI\_RenderNodeUtils\_SetNodeBorderWidthOptionEdgeWidth(widthOption, 5,
                                                                   ArkUI\_EdgeDirection::ARKUI\_EDGE\_DIRECTION\_ALL);
        OH\_ArkUI\_RenderNodeUtils\_SetBorderWidth(firstChildRenderNode, widthOption);
        // After using the structure, destroy it to free memory.
        OH\_ArkUI\_RenderNodeUtils\_DisposeNodeBorderWidthOption(widthOption);
        widthOption = nullptr;
    
        auto colorOption = OH\_ArkUI\_RenderNodeUtils\_CreateNodeBorderColorOption();
        OH\_ArkUI\_RenderNodeUtils\_SetNodeBorderColorOptionEdgeColor(colorOption, 0xFF000000,
                                                                   ArkUI\_EdgeDirection::ARKUI\_EDGE\_DIRECTION\_ALL);
        result = OH\_ArkUI\_RenderNodeUtils\_SetBorderColor(firstChildRenderNode, colorOption);
        // After using the structure, destroy it to free memory.
        OH\_ArkUI\_RenderNodeUtils\_DisposeNodeBorderColorOption(colorOption);
        colorOption = nullptr;
    
        nodeAPI->addChild(scroll, column);
        return scroll;
    }
    
     napi\_value CreateNativeRoot(napi\_env env, napi\_callback\_info info) {
        size\_t argc = 1;
        napi\_value args\[1\] = {nullptr};
    
        napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);
    
        auto \*nodeAPI = reinterpret\_cast<ArkUI\_NativeNodeAPI\_1 \*>(
            OH\_ArkUI\_QueryModuleInterfaceByName(ARKUI\_NATIVE\_NODE, "ArkUI\_NativeNodeAPI\_1"));
        if (nodeAPI != nullptr) {
             ArkUI\_NodeHandle testNode;
             testNode = testRenderNode(nodeAPI);
        }
    
        NativeEntry::GetInstance()->SetRootNode(testNode);
        return nullptr;
    }
    

#### Custom Drawing and Animation

The following example demonstrates how to create a rendering node, implement custom drawing, and add animation effects.

1.  Follow the instructions in [Integrating with ArkTS Pages](../integrating-with-arkts-pages/document.md) to create a project.
    
2.  Create a rendering node capability object.
    
    // NativeEntry.cpp
    // Example of a custom container component
    #include <arkui/native\_animate.h>
    #include <arkui/native\_render.h>
    #include <arkui/native\_type.h>
    #include <arkui/native\_node\_napi.h>
    #include <bits/alltypes.h>
    
    #include <string>
    
    #include <arkui/native\_interface.h>
    #include <arkui/native\_node.h>
    #include <native\_drawing/drawing\_canvas.h>
    #include <native\_drawing/drawing\_color.h>
    #include <native\_drawing/drawing\_path.h>
    #include <native\_drawing/drawing\_pen.h>
    
    ArkUI\_NodeHandle testRenderNode2(ArkUI\_NativeNodeAPI\_1 \*nodeAPI, ArkUI\_ContextHandle context) {
    
        ArkUI\_NodeHandle scroll = nodeAPI->createNode(ARKUI\_NODE\_COLUMN);
        ArkUI\_NumberValue valueWidth\[\] = {400};
        ArkUI\_AttributeItem itemWidth = {valueWidth, sizeof(valueWidth) / sizeof(ArkUI\_NumberValue)};
        nodeAPI->setAttribute(scroll, NODE\_WIDTH, &itemWidth);
        ArkUI\_NumberValue valueHeight\[\] = {600};
        ArkUI\_AttributeItem itemHeight = {valueHeight, sizeof(valueHeight) / sizeof(ArkUI\_NumberValue)};
        nodeAPI->setAttribute(scroll, NODE\_HEIGHT, &itemHeight);
        valueHeight\[0\].u32 = 0xff00F100;
        nodeAPI->setAttribute(scroll, NODE\_BACKGROUND\_COLOR, &itemHeight);
    
        ArkUI\_NodeHandle column = nodeAPI->createNode(ARKUI\_NODE\_COLUMN);
        ArkUI\_NodeHandle text = nodeAPI->createNode(ARKUI\_NODE\_TEXT);
        ArkUI\_AttributeItem content = {.string = "This is the C API page."};
    
        nodeAPI->setAttribute(text, NODE\_TEXT\_CONTENT, &content);
    
        ArkUI\_NodeHandle Custom = nodeAPI->createNode(ARKUI\_NODE\_CUSTOM);
        auto renderNode = OH\_ArkUI\_RenderNodeUtils\_CreateNode();
        OH\_ArkUI\_RenderNodeUtils\_AddRenderNode(Custom, renderNode);
        OH\_ArkUI\_RenderNodeUtils\_SetSize(renderNode, 1000, 1000);
    
        // Define animatable properties (for driving animation and drawing).
        struct AnimatableUserData {
            ArkUI\_FloatAnimatablePropertyHandle width;
            ArkUI\_FloatAnimatablePropertyHandle height;
            ArkUI\_Vector2AnimatablePropertyHandle v2;
            ArkUI\_ColorAnimatablePropertyHandle color;
        };
    
        // Set initial values.
        AnimatableUserData \*userData1 = new AnimatableUserData;
        auto widthAnimProperty = OH\_ArkUI\_RenderNodeUtils\_CreateFloatAnimatableProperty(1000);
        userData1->width = widthAnimProperty;
        auto heightAnimProperty = OH\_ArkUI\_RenderNodeUtils\_CreateFloatAnimatableProperty(1000);
        userData1->height = heightAnimProperty;
        auto vectorAnimP = OH\_ArkUI\_RenderNodeUtils\_CreateVector2AnimatableProperty(1000, 1000);
        userData1->v2 = vectorAnimP;
        auto colorAnimP = OH\_ArkUI\_RenderNodeUtils\_CreateColorAnimatableProperty(0xFFFF11FF);
        userData1->color = colorAnimP;
    
        // Associate the component with modifiers.
        auto animModifier = OH\_ArkUI\_RenderNodeUtils\_CreateContentModifier();
        OH\_ArkUI\_RenderNodeUtils\_AttachContentModifier(renderNode, animModifier);
        // Bind animatable properties to the modifier.
        OH\_ArkUI\_RenderNodeUtils\_AttachFloatAnimatableProperty(animModifier, widthAnimProperty);
        OH\_ArkUI\_RenderNodeUtils\_AttachFloatAnimatableProperty(animModifier, heightAnimProperty);
        OH\_ArkUI\_RenderNodeUtils\_AttachVector2AnimatableProperty(animModifier, vectorAnimP);
        OH\_ArkUI\_RenderNodeUtils\_AttachColorAnimatableProperty(animModifier, colorAnimP);
    
        // Implement custom drawing logic.
        OH\_ArkUI\_RenderNodeUtils\_SetContentModifierOnDraw(
            animModifier, userData1, \[\](ArkUI\_DrawContext \*context, void \*userData) {
                AnimatableUserData \*data = (AnimatableUserData \*)userData;
                float width = 0;
                float height = 0;
                uint32\_t color = 0;
                ArkUI\_Vector2AnimatablePropertyHandle v2 = data->v2;
                // Obtain the animatable property (x and y values used as the width and height here). Custom properties can be defined to pass required parameters.
                OH\_ArkUI\_RenderNodeUtils\_GetVector2AnimatablePropertyValue(v2, &width, &height);
                ArkUI\_ColorAnimatablePropertyHandle cp = data->color;
                OH\_ArkUI\_RenderNodeUtils\_GetColorAnimatablePropertyValue(cp, &color);
    
    
                auto \*canvas1 = OH\_ArkUI\_DrawContext\_GetCanvas(context);
                OH\_Drawing\_Canvas \*canvas = reinterpret\_cast<OH\_Drawing\_Canvas \*>(canvas1);
                auto path = OH\_Drawing\_PathCreate();
                OH\_Drawing\_PathMoveTo(path, width / 4, height / 4);
                OH\_Drawing\_PathLineTo(path, width \* 3 / 4, height / 4);
                OH\_Drawing\_PathLineTo(path, width \* 3 / 4, height \* 3 / 4);
                OH\_Drawing\_PathLineTo(path, width / 4, height \* 3 / 4);
                OH\_Drawing\_PathLineTo(path, width / 4, height / 4);
                OH\_Drawing\_PathClose(path);
                auto pen = OH\_Drawing\_PenCreate();
                OH\_Drawing\_PenSetWidth(pen, 10);
                OH\_Drawing\_PenSetColor(pen, color);
                OH\_Drawing\_CanvasAttachPen(canvas, pen);
                OH\_Drawing\_CanvasDrawPath(canvas, path);
            });
    
        // User-defined parameters.
        ArkUI\_ContextCallback \*update = new ArkUI\_ContextCallback;
        update->userData = userData1;
        update->callback = \[\](void \*user) {
            AnimatableUserData \*data = (AnimatableUserData \*)user;
            OH\_ArkUI\_RenderNodeUtils\_SetFloatAnimatablePropertyValue(data->width, 100);
            OH\_ArkUI\_RenderNodeUtils\_SetFloatAnimatablePropertyValue(data->height, 100);
            OH\_ArkUI\_RenderNodeUtils\_SetVector2AnimatablePropertyValue(data->v2, 100, 100);
            OH\_ArkUI\_RenderNodeUtils\_SetColorAnimatablePropertyValue(data->color, 0xFF0011FF);
        };
        // Execute the corresponding animation.
        ArkUI\_NativeAnimateAPI\_1 \*animateApi = nullptr;
        OH\_ArkUI\_GetModuleInterface(ARKUI\_NATIVE\_ANIMATE, ArkUI\_NativeAnimateAPI\_1, animateApi);
    
        ArkUI\_AnimateCompleteCallback \*completeCallback = new ArkUI\_AnimateCompleteCallback;
        completeCallback->userData = userData1;
        completeCallback->type = ARKUI\_FINISH\_CALLBACK\_REMOVED;
        completeCallback->callback = \[\](void \*userData) {
            AnimatableUserData \*data = (AnimatableUserData \*)userData;
        };
    
        ArkUI\_AnimateOption \*option = OH\_ArkUI\_AnimateOption\_Create();
        OH\_ArkUI\_AnimateOption\_SetDuration(option, 2000);
        OH\_ArkUI\_AnimateOption\_SetTempo(option, 1.1);
        OH\_ArkUI\_AnimateOption\_SetCurve(option, ARKUI\_CURVE\_EASE);
        OH\_ArkUI\_AnimateOption\_SetDelay(option, 20);
        OH\_ArkUI\_AnimateOption\_SetIterations(option, 1);
        OH\_ArkUI\_AnimateOption\_SetPlayMode(option, ARKUI\_ANIMATION\_PLAY\_MODE\_REVERSE);
        ArkUI\_ExpectedFrameRateRange \*range = new ArkUI\_ExpectedFrameRateRange;
        range->min = 10;
        range->max = 120;
        range->expected = 60;
        OH\_ArkUI\_AnimateOption\_SetExpectedFrameRateRange(option, range);
            animateApi->animateTo(context, option, update, completeCallback);
    
    
        nodeAPI->setAttribute(Custom, NODE\_WIDTH, &itemWidth);
        nodeAPI->setAttribute(Custom, NODE\_HEIGHT, &itemHeight);
    
        nodeAPI->addChild(column, text);
        nodeAPI->addChild(column, Custom);
        nodeAPI->addChild(scroll, column);
        return scroll;
    }
    
     napi\_value CreateNativeRoot(napi\_env env, napi\_callback\_info info) {
        size\_t argc = 2;
        napi\_value args\[2\] = {nullptr, nullptr};
    
        napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);
    
        auto \*nodeAPI = reinterpret\_cast<ArkUI\_NativeNodeAPI\_1 \*>(
            OH\_ArkUI\_QueryModuleInterfaceByName(ARKUI\_NATIVE\_NODE, "ArkUI\_NativeNodeAPI\_1"));
        if (nodeAPI != nullptr) {
             ArkUI\_NodeHandle testNode;
             // Obtain the context passed from the ETS side.
             ArkUI\_ContextHandle context = nullptr;
             // Use code to check whether the context is successfully obtained.
             auto code = OH\_ArkUI\_GetContextFromNapiValue(env, args\[1\], &context);
             testNode = testRenderNode2(nodeAPI, context);
        }
    
        NativeEntry::GetInstance()->SetRootNode(testNode);
        return nullptr;
    }
       
    

#### Mixing and Mounting Native Components and Rendering Nodes

Since from API version 22, you can efficiently mix and mount native components and rendering nodes. To be specific, you can obtain the rendering node corresponding to a native component and mount it to that of a non-native component. In this way, the rendering nodes of both the native and non-native components are mixed.

Before mixing and mounting, you need to accept the native components. After the parent node accepts the target child node, the child node becomes an auxiliary node of the parent node. Only the auxiliary node can obtain the rendering node and mount it to another position in the rendering node tree.

## Accepting a Child Node as an Auxiliary Node

A node that meets the following conditions can be used as the parent node in the [OH\_ArkUI\_NativeModule\_AdoptChild](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-node-h#oh_arkui_nativemodule_adoptchild) API to accept other nodes:

1.  The node is an imperative node created on the C-API side.
2.  The node is an imperative node created on the ArkTS side.

A node that meets the following conditions can be used as a child node in the **OH\_ArkUI\_NativeModule\_AdoptChild** API to be accepted by other parent nodes:

1.  The node is an imperative node created on the C-API side.
2.  The node is an imperative node created on the ArkTS side.
3.  The child node is the root node under BuilderNode.

After a child node is accepted as an auxiliary node, it cannot be mounted to other nodes as a regular child node. Otherwise, an error code will be thrown. However, the child node can be accepted by other parent nodes again. In this case, the child node will become a new auxiliary node of the other parent nodes. The accepted child node is not the real child node of its parent node, and cannot be found by the child component query API. It cannot be operated like a regular child node, and does not receive the measurement layout and event transfer from the parent node. It only receives the [lifecycle](../../../ability-kit/stage-model-development/stage-model-application-components/uiability-component/uiability-lifecycle/document.md#overview) propagation from the parent node.

## Obtaining the Rendering Node of an Auxiliary Node

When an auxiliary node is accepted, you can call [OH\_ArkUI\_RenderNodeUtils\_GetRenderNode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-render-h#oh_arkui_rendernodeutils_getrendernode) to obtain its corresponding rendering node.

When you call the [disposeNode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1#disposenode) API of [ArkUI\_NativeNodeAPI\_1](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1) to destroy the parent node, call [OH\_ArkUI\_RenderNodeUtils\_DisposeNode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-render-h#oh_arkui_rendernodeutils_disposenode) to release the rendering node. Otherwise, a memory leak will occur.

## Operating a Rendering Node from an Auxiliary Node

After obtaining a rendering node from an accepted auxiliary node, you can use it for layout. The constraints are as follows:

1.  A rendering node from an auxiliary node must be mounted to another rendering node.
    
    A rendering node from an auxiliary node can only be mounted to another rendering node as a child node or unmounted from another rendering node. Any other operations will fail and an error code will be returned. After the rendering node is mounted, the auxiliary node will be drawn in the target position corresponding to the rendering node.
    
2.  The rendering node of an auxiliary node depends on the offscreen mounting status.
    
    If the parent node of the auxiliary node calls the [OH\_ArkUI\_NativeModule\_RemoveAdoptedChild](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-node-h#oh_arkui_nativemodule_removeadoptedchild) API to cancel the offscreen mounting status, the rendering node will also be removed from the rendering node tree.
    
3.  If the auxiliary node is no longer in the offscreen mounting state, the rendering node from this auxiliary node cannot be mounted to other rendering nodes.
    

## Creating and Accepting Web Components for Mixed Mounting

Before developing the following code, create a project by referring to [Integrating with ArkTS Pages](../integrating-with-arkts-pages/document.md).

1.  Initialize the component environment using the NDK and create the root node of the corresponding rendering node.
    
    std::shared\_ptr<ArkUIBaseNode> custom\_ = nullptr;
    std::shared\_ptr<ArkUIRenderNode> render\_ = nullptr;
    
    std::shared\_ptr<ArkUIBaseNode> testGetRenderNodeDemo()
    {
        auto scroll = std::make\_shared<ArkUIScrollNode>();
        scroll->SetWidth(g\_contentWidth);
        scroll->SetHeight(g\_contentHeight);
        scroll->SetBackgroundColor(0xff00F100);
    
        auto column = std::make\_shared<ArkUIColumnNode>();
        column->SetWidth(g\_contentWidth);
        column->SetHeight(g\_contentHeight);
        auto text = std::make\_shared<ArkUITextNode>();
        text->SetTextContent("This is an example of mounting a rendering node obtained from frameNode. Click the mount button below.");
        text->SetWidth(g\_num300);
        text->SetHeight(g\_num100);
    
        auto Custom = std::make\_shared<ArkUICustomNode>();
        Custom->SetWidth(g\_contentWidth);
        Custom->SetHeight(g\_num100);
        column->AddChild(text);
        column->AddChild(Custom);
        custom\_ = Custom;
        
        // Set up the mountable environment and mount the rendering node as the root node of the custom component.
        auto renderNode = std::make\_shared<ArkUIRenderNode>();
        Custom->AddRenderNode(renderNode);
        renderNode->SetSize(g\_num300, g\_num300);
        Custom->AddRenderNode(renderNode);
        render\_ = renderNode;
    
        scroll->AddChild(column);
        return scroll;
    }
    
    napi\_value CreateRenderNodeGetNodeExample(napi\_env env, napi\_callback\_info info)
    {
        size\_t argc = 2;
        napi\_value args\[2\] = {nullptr, nullptr};
        napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);
        // Obtain the mount point of the component on the ArkTS side.
        ArkUI\_NodeContentHandle contentHandle;
        int32\_t result = OH\_ArkUI\_GetNodeContentFromNapiValue(env, args\[0\], &contentHandle);
        if (result != ARKUI\_ERROR\_CODE\_NO\_ERROR) {
            return nullptr;
        }
    
        // Create the root node of the component tree on the native side.
        auto scrollNode = std::make\_shared<ArkUIScrollNode>();
        // Mount the root node of the component tree on the native side to the main UI tree.
        result = OH\_ArkUI\_NodeContent\_AddNode(contentHandle, scrollNode->GetHandle());
        if (result != ARKUI\_ERROR\_CODE\_NO\_ERROR) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_ArkUI\_NodeContent\_AddNode Failed %{public}d", result);
            return nullptr;
        }
        // Save the component tree on the native side.
        g\_nodeMap\[contentHandle\] = scrollNode;
        auto rootNode = testGetRenderNodeDemo();
        scrollNode->AddChild(rootNode);
        return nullptr;
    }
    
2.  Create a node on the ArkTS side and pass the node to the C-API.
    
    import { BuilderNode, FrameNode, NodeContent, NodeController, typeNode } from '@kit.ArkUI';
    import entry from 'libentry.so';
    import { webview } from '@kit.ArkWeb';
    
    // Define the API for passing parameters.
    interface ParamsInterface {
      text: string;
      func: Function;
    }
    class MyNodeController extends NodeController {
      private imperativeNode: FrameNode | null = null;
      public rootNode: typeNode.Column |null = null;
      private buildNode: FrameNode | null = null;
    
      makeNode(uiContext: UIContext): FrameNode {
        this.rootNode = typeNode.createNode(uiContext, 'Column');
    
        this.imperativeNode = new FrameNode(uiContext);
        this.rootNode?.appendChild(this.imperativeNode);
        return this.rootNode;
      }
    
      adoptNode(uiContext:UIContext, message:string):void {
        let buildNode = new BuilderNode<\[ParamsInterface\]>(uiContext);
        // Create a node tree.
        buildNode.build(wrapBuilder<\[ParamsInterface\]>(buildText), {
          text: message, func: () => {
            return 'FUNCTION';
          }
        }, { nestingBuilderSupported: true });
        this.buildNode = buildNode.getFrameNode();
        entry.adopt(buildNode);
      }
      removeAdoptedNode(uiContext:UIContext):void {
        entry.removeAdopt();
      }
    }
    
    @Builder
    function buildTextWithFunc(fun: Function) {
      Web({ src: 'https://www.example.com', controller: new webview.WebviewController() })
    }
    
    @Builder
    function buildText(params: ParamsInterface) {
      Column() {
        buildTextWithFunc(params.func)
      }
    }
    
    @Component
    struct CAPIComponent {
      private rootSlot = new NodeContent();
    
      aboutToAppear(): void {
        entry.createRenderNodeGetNodeExample(this.rootSlot, this.getUIContext())
      }
    
      aboutToDisappear(): void {
        // Release created native components before page destruction.
        entry.disposeNodeTree(this.rootSlot)
      }
    
      build() {
        Column() {
          // Native component mount point.
          ContentSlot(this.rootSlot)
        }
      }
    }
    
    @Entry
    @Component
    struct Index {
      @State isShow: boolean = false;
      @State isAdopt: boolean = false;
      @State message: string = 'CreateNodeTree';
      @State adoptmsg: string = 'adopt web component';
    
      private myNodeController: MyNodeController = new MyNodeController();
      build() {
        Flex() {
          Column() {
            Text('create CustomDrawNode, ')
              .fontSize(18)
              .fontWeight(FontWeight.Bold)
            Button(this.message)
              .onClick(() => {
                this.isShow = !this.isShow;
              })
            if (this.isShow) {
              CAPIComponent()
    
              Button(this.adoptmsg)
                .onClick(() => {
                  if (this.isAdopt) {
                    this.myNodeController.removeAdoptedNode(this.getUIContext());
                    this.adoptmsg = 'adopt web component';
                  } else {
                    this.myNodeController.adoptNode(this.getUIContext(),this.message);
                    this.adoptmsg = 'remove adopt web';
                  }
                  this.isAdopt = !this.isAdopt;
                })
    
              NodeContainer(this.myNodeController)
            }
          }.width('100%')
        }.width('100%')
      }
    }
    
3.  Obtain and accept the node, and obtain the corresponding rendering node on the C-API side.
    
    napi\_value Adopt(napi\_env env, napi\_callback\_info info)
    {
        size\_t argc = 1;
        napi\_value args\[1\] = {nullptr};
        napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);
        // Obtain the mount point of the component on the ArkTS side.
        int32\_t result = OH\_ArkUI\_GetNodeHandleFromNapiValue(env, args\[0\], &nodeHandle\_);
        if (result != ARKUI\_ERROR\_CODE\_NO\_ERROR) {
            return nullptr;
        }
        result = OH\_ArkUI\_NativeModule\_AdoptChild(custom\_->GetHandle(), nodeHandle\_);
        OH\_ArkUI\_RenderNodeUtils\_GetRenderNode(nodeHandle\_, &renderHandle\_);
        OH\_ArkUI\_RenderNodeUtils\_AddChild(render\_->GetHandle(), renderHandle\_);
        return nullptr;
    }
    
4.  Cancel the accepted state of the node and release the corresponding rendering node on the C-API side.
    
    napi\_value RemoveAdopt(napi\_env env, napi\_callback\_info info)
    {
        OH\_ArkUI\_NativeModule\_RemoveAdoptedChild(custom\_->GetHandle(), nodeHandle\_);
        // After the node is released, you need to call OH\_ArkUI\_RenderNodeUtils\_DisposeNode to release the corresponding rendering node. Otherwise, a memory leak occurs.
        OH\_ArkUI\_RenderNodeUtils\_DisposeNode(renderHandle\_);
        nodeHandle\_ = nullptr;
        renderHandle\_ = nullptr;
        return nullptr;
    }
