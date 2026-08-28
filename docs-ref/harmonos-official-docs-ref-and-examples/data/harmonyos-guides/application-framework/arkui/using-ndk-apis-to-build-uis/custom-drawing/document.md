# Custom Drawing

The NDK supports custom drawing nodes, enabling you to implement custom rendering logic using the NDK APIs.

#### Custom Drawing Content

When the registered event is detected as a drawing type, you can use the custom drawing feature to implement your own drawing logic and custom content.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/uXKJzU7_T8OV5upvUiALZg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061941Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7EDE091D5028B4D7A7A4A9569EB26C70A29066C4237E72DDC0CB174DA5BEDCDA)

-   During event registration, you must register the event as a drawing event (for example, **ARKUI\_NODE\_CUSTOM\_EVENT\_ON\_DRAW**). You can find the event types and their meanings by referring to the [ArkUI\_NodeCustomEventType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-node-h#arkui_nodecustomeventtype) enum.
    
-   To implement custom drawing logic, you must define custom **UserData** and pass it during event registration.
    

The following scenarios are based on the project configuration described in [Integrating with ArkTS Pages](../integrating-with-arkts-pages/document.md).

-   Create a custom node by passing the [ARKUI\_NODE\_CUSTOM](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-node-h#arkui_nodetype) enumerated value through the [createNode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1#createnode) API of [ArkUI\_NativeNodeAPI\_1](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1).
    
    auto customNode = nodeAPI->createNode(ARKUI\_NODE\_CUSTOM);
    
-   Register the custom event with the custom node, event type (for example, **ARKUI\_NODE\_CUSTOM\_EVENT\_ON\_FOREGROUND\_DRAW**; for details about the supported event types, see [ArkUI\_NodeCustomEventType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-node-h#arkui_nodecustomeventtype)), event ID, and **UserData**.
    
    // UserData
    struct A {
        int32\_t a = 6;
        bool flag = true;
        ArkUI\_NodeHandle node;
    };
    A \*a = new A;
    a->node = customNode;
    // ...
    nodeAPI->registerNodeCustomEvent(customNode, ARKUI\_NODE\_CUSTOM\_EVENT\_ON\_FOREGROUND\_DRAW, 1, a);
    // Define the event callback.
    nodeAPI->registerNodeCustomEventReceiver(\[\](ArkUI\_NodeCustomEvent \*event) {
        // Event callback logic
        // ...
    });
    
-   In the callback, obtain the event type, event ID, and UserData to determine the execution logic using the following APIs: [OH\_ArkUI\_NodeCustomEvent\_GetEventType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-node-h#oh_arkui_nodecustomevent_geteventtype), [OH\_ArkUI\_NodeCustomEvent\_GetEventTargetId](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-node-h#oh_arkui_nodecustomevent_geteventtargetid), and [OH\_ArkUI\_NodeCustomEvent\_GetUserData](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-node-h#oh_arkui_nodecustomevent_getuserdata).
    
    auto type = OH\_ArkUI\_NodeCustomEvent\_GetEventType(event);
    auto targetId = OH\_ArkUI\_NodeCustomEvent\_GetEventTargetId(event);
    auto userData = reinterpret\_cast<A \*>(OH\_ArkUI\_NodeCustomEvent\_GetUserData(event));
    
-   [OH\_ArkUI\_NodeCustomEvent\_GetDrawContextInDraw](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-node-h#oh_arkui_nodecustomevent_getdrawcontextindraw) obtains the drawing context through the custom component event and transfers the drawing context to [OH\_ArkUI\_DrawContext\_GetCanvas](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-type-h#oh_arkui_drawcontext_getcanvas) to obtain the canvas pointer for drawing. The pointer is then converted to a [OH\_Drawing\_Canvas](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-drawing-oh-drawing-canvas) pointer for drawing.
    
    // Obtain the drawing context for the custom event.
    auto \*drawContext = OH\_ArkUI\_NodeCustomEvent\_GetDrawContextInDraw(event);
    // Obtain the drawing canvas pointer.
    auto \*canvas1 = OH\_ArkUI\_DrawContext\_GetCanvas(drawContext);
    // Cast the pointer to an OH\_Drawing\_Canvas pointer for drawing.
    OH\_Drawing\_Canvas \*canvas = reinterpret\_cast<OH\_Drawing\_Canvas \*>(canvas1);
    // Drawing logic.
    int32\_t width = SIZE\_1000;  // SIZE\_1000 = 1000
    int32\_t height = SIZE\_1000; // SIZE\_1000 = 1000
    auto path = OH\_Drawing\_PathCreate();
    OH\_Drawing\_PathMoveTo(path, width / SIZE\_4, height / SIZE\_4);                   // SIZE\_4 = 4
    OH\_Drawing\_PathLineTo(path, width \* SIZE\_3 / SIZE\_4, height \* SIZE\_3 / SIZE\_4); // SIZE\_3 = 3,SIZE\_4 = 4
    OH\_Drawing\_PathClose(path);
    auto pen = OH\_Drawing\_PenCreate();
    OH\_Drawing\_PenSetWidth(pen, SIZE\_10); // SIZE\_10=10
    OH\_Drawing\_PenSetColor(pen, OH\_Drawing\_ColorSetArgb(0xFF, 0x00, 0x4A, 0x4F));
    OH\_Drawing\_CanvasAttachPen(canvas, pen);
    OH\_Drawing\_CanvasDrawPath(canvas, path);
    

**Complete content drawing example**:

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/06/v3/aN_1XWOhSyqSM4JBzWo-DQ/en-us_image_0000002537764892.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061941Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2B084D935E8652FDDF1E1439BB5E656CE36A99F505253FB6404C7A2C4BF7D02B)

#### Custom Drawing Foreground and Background

The following example creates a custom drawing component capable of rendering custom rectangles, customizing foreground and background elements, and using the [custom layout container](../building-custom-components/document.md#custom-layout-container) for layout management.

1.  Prepare a project as instructed in [Custom Layout Container](../building-custom-components/document.md#custom-layout-container).
    
2.  Create an encapsulated object for the custom drawing component.
    
    #ifndef MYAPPLICATION\_ARKUICUSTOMNODE\_H
    #define MYAPPLICATION\_ARKUICUSTOMNODE\_H
    
    #include <native\_drawing/drawing\_brush.h>
    #include <native\_drawing/drawing\_canvas.h>
    #include <native\_drawing/drawing\_path.h>
    
    #include "ArkUINode.h"
    
    namespace NativeModule {
    class ArkUICustomNode : public ArkUINode {
    public:
        // Create the component using the custom component type ARKUI\_NODE\_CUSTOM.
        ArkUICustomNode()
            : ArkUINode((NativeModuleInstance::GetInstance()->GetNativeNodeAPI())->createNode(ARKUI\_NODE\_CUSTOM))
        {
            // Register the custom event listener.
            nativeModule\_->addNodeCustomEventReceiver(handle\_, OnStaticCustomEvent);
            // Declare the custom event and pass itself as custom data.
            nativeModule\_->registerNodeCustomEvent(handle\_, ARKUI\_NODE\_CUSTOM\_EVENT\_ON\_DRAW\_FRONT, 0, this);
            nativeModule\_->registerNodeCustomEvent(handle\_, ARKUI\_NODE\_CUSTOM\_EVENT\_ON\_DRAW, 0, this);
            nativeModule\_->registerNodeCustomEvent(handle\_, ARKUI\_NODE\_CUSTOM\_EVENT\_ON\_DRAW\_BEHIND, 0, this);
            // Register a callback for the drawing completion event.
            OH\_ArkUI\_RegisterDrawCallbackOnNodeHandle(handle\_, nullptr, \[\](void\* userData) {});
        }
    
        ~ArkUICustomNode() override
        {
            // Unregister the custom event listener.
            nativeModule\_->removeNodeCustomEventReceiver(handle\_, OnStaticCustomEvent);
            // Remove the declaration of the custom event.
            nativeModule\_->unregisterNodeCustomEvent(handle\_, ARKUI\_NODE\_CUSTOM\_EVENT\_ON\_DRAW\_FRONT);
            nativeModule\_->unregisterNodeCustomEvent(handle\_, ARKUI\_NODE\_CUSTOM\_EVENT\_ON\_DRAW);
            nativeModule\_->unregisterNodeCustomEvent(handle\_, ARKUI\_NODE\_CUSTOM\_EVENT\_ON\_DRAW\_BEHIND);
            OH\_ArkUI\_UnregisterDrawCallbackOnNodeHandle(handle\_);
        }
    
    private:
        int32\_t NUM\_2 = 2;
        int32\_t NUM\_3 = 3;
        int32\_t NUM\_4 = 4;
        int32\_t NUM\_5 = 5;
        static void OnStaticCustomEvent(ArkUI\_NodeCustomEvent \*event)
        {
            // Obtain the component instance object and call the related instance method.
            // ...
            auto customNode = reinterpret\_cast<ArkUICustomNode \*>(OH\_ArkUI\_NodeCustomEvent\_GetUserData(event));
            auto type = OH\_ArkUI\_NodeCustomEvent\_GetEventType(event);
            switch (type) {
                // The drawing layer is from low to high.
                case ARKUI\_NODE\_CUSTOM\_EVENT\_ON\_DRAW\_BEHIND:
                    customNode->OnDrawBehind(event);
                    break;
                case ARKUI\_NODE\_CUSTOM\_EVENT\_ON\_DRAW:
                    customNode->OnDraw(event);
                    break;
                case ARKUI\_NODE\_CUSTOM\_EVENT\_ON\_DRAW\_FRONT:
                    customNode->OnDrawFront(event);
                    break;
                // ...
                default:
                    break;
            }
        }
    
        // Custom drawing logic
        void OnDrawBehind(ArkUI\_NodeCustomEvent \*event)
        {
            auto drawContext = OH\_ArkUI\_NodeCustomEvent\_GetDrawContextInDraw(event);
            // Obtain the graphics drawing object.
            auto drawCanvas = reinterpret\_cast<OH\_Drawing\_Canvas \*>(OH\_ArkUI\_DrawContext\_GetCanvas(drawContext));
            // Obtain the component size.
            auto size = OH\_ArkUI\_DrawContext\_GetSize(drawContext);
            // Draw custom content.
            auto path = OH\_Drawing\_PathCreate();
            OH\_Drawing\_PathMoveTo(path, size.width / NUM\_5, size.height / NUM\_5);
            OH\_Drawing\_PathLineTo(path, size.width \* NUM\_4 / NUM\_5, size.height / NUM\_5);
            OH\_Drawing\_PathLineTo(path, size.width \* NUM\_4 / NUM\_5, size.height \* NUM\_4 / NUM\_5);
            OH\_Drawing\_PathLineTo(path, size.width / NUM\_5, size.height \* NUM\_4 / NUM\_5);
            OH\_Drawing\_PathLineTo(path, size.width / NUM\_5, size.height / NUM\_5);
            OH\_Drawing\_PathClose(path);
            auto brush = OH\_Drawing\_BrushCreate();
            OH\_Drawing\_BrushSetColor(brush, 0xFFF0FAFF); // Pale blue
            OH\_Drawing\_CanvasAttachBrush(drawCanvas, brush);
            OH\_Drawing\_CanvasDrawPath(drawCanvas, path);
            // Release resources.
            OH\_Drawing\_BrushDestroy(brush);
            OH\_Drawing\_PathDestroy(path);
        }
    
        void OnDraw(ArkUI\_NodeCustomEvent \*event)
        {
            auto drawContext = OH\_ArkUI\_NodeCustomEvent\_GetDrawContextInDraw(event);
            // Obtain the graphics drawing object.
            auto drawCanvas = reinterpret\_cast<OH\_Drawing\_Canvas \*>(OH\_ArkUI\_DrawContext\_GetCanvas(drawContext));
            // Obtain the component size.
            auto size = OH\_ArkUI\_DrawContext\_GetSize(drawContext);
            // Draw custom content.
            auto path = OH\_Drawing\_PathCreate();
            OH\_Drawing\_PathMoveTo(path, size.width / NUM\_4, size.height / NUM\_4);
            OH\_Drawing\_PathLineTo(path, size.width \* NUM\_3 / NUM\_4, size.height / NUM\_4);
            OH\_Drawing\_PathLineTo(path, size.width \* NUM\_3 / NUM\_4, size.height \* NUM\_3 / NUM\_4);
            OH\_Drawing\_PathLineTo(path, size.width / NUM\_4, size.height \* NUM\_3 / NUM\_4);
            OH\_Drawing\_PathLineTo(path, size.width / NUM\_4, size.height / NUM\_4);
            OH\_Drawing\_PathClose(path);
            auto brush = OH\_Drawing\_BrushCreate();
            OH\_Drawing\_BrushSetColor(brush, 0xff2787D9); // Light blue
            OH\_Drawing\_CanvasAttachBrush(drawCanvas, brush);
            OH\_Drawing\_CanvasDrawPath(drawCanvas, path);
            // Release resources.
            OH\_Drawing\_BrushDestroy(brush);
            OH\_Drawing\_PathDestroy(path);
        }
    
        void OnDrawFront(ArkUI\_NodeCustomEvent \*event)
        {
            auto drawContext = OH\_ArkUI\_NodeCustomEvent\_GetDrawContextInDraw(event);
            // Obtain the graphics drawing object.
            auto drawCanvas = reinterpret\_cast<OH\_Drawing\_Canvas \*>(OH\_ArkUI\_DrawContext\_GetCanvas(drawContext));
            // Obtain the component size.
            auto size = OH\_ArkUI\_DrawContext\_GetSize(drawContext);
            // Draw custom content.
            auto path = OH\_Drawing\_PathCreate();
            OH\_Drawing\_PathMoveTo(path, size.width / NUM\_3, size.height / NUM\_3);
            OH\_Drawing\_PathLineTo(path, size.width \* NUM\_2 / NUM\_3, size.height / NUM\_3);
            OH\_Drawing\_PathLineTo(path, size.width \* NUM\_2 / NUM\_3, size.height \* NUM\_2 / NUM\_3);
            OH\_Drawing\_PathLineTo(path, size.width / NUM\_3, size.height \* NUM\_2 / NUM\_3);
            OH\_Drawing\_PathLineTo(path, size.width / NUM\_3, size.height / NUM\_3);
            OH\_Drawing\_PathClose(path);
            auto brush = OH\_Drawing\_BrushCreate();
            OH\_Drawing\_BrushSetColor(brush, 0xFF004AAF); // Dark blue
            OH\_Drawing\_CanvasAttachBrush(drawCanvas, brush);
            OH\_Drawing\_CanvasDrawPath(drawCanvas, path);
            // Release resources.
            OH\_Drawing\_BrushDestroy(brush);
            OH\_Drawing\_PathDestroy(path);
        }
        // ...
    };
    
    } // namespace NativeModule
    
    #endif // MYAPPLICATION\_ARKUICUSTOMNODE\_H
    
3.  Use the custom drawing component and custom container to create a sample UI.
    
    #include <arkui/native\_node\_napi.h>
    #include <arkui/native\_type.h>
    #include <js\_native\_api.h>
    
    #include "NativeEntry.h"
    #include "ArkUICustomContainerNode.h"
    #include "ArkUICustomNode.h"
    
    // Declare global environment variables.
    static napi\_env g\_env = nullptr;
    // ···
    namespace NativeModule {
    // ···
    napi\_value CreateNativeRoot(napi\_env env, napi\_callback\_info info)
    {
        size\_t argc = 1;
        napi\_value args\[1\] = {nullptr};
    
        napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);
    
        // Obtain the NodeContent object.
        ArkUI\_NodeContentHandle contentHandle;
        OH\_ArkUI\_GetNodeContentFromNapiValue(env, args\[0\], &contentHandle);
        NativeEntry::GetInstance()->SetContentHandle(contentHandle);
    
        // Create a custom container and a custom drawing component.
        auto node = std::make\_shared<ArkUICustomContainerNode>();
        node->SetBackgroundColor(0xFFD5D5D5); // Light gray.
        auto customNode = std::make\_shared<ArkUICustomNode>();
        customNode->SetBackgroundColor(0xFF707070); // Dark gray.
        customNode->SetWidth(SIZE\_150);
        customNode->SetHeight(SIZE\_150);
        node->AddChild(customNode);
    
        // Keep the native-side object in the management class to maintain its lifecycle.
        NativeEntry::GetInstance()->SetRootNode(node);
        g\_env = env;
        return nullptr;
    }
    
    napi\_value DestroyNativeRoot(napi\_env env, napi\_callback\_info info)
    {
        // Release the native-side object from the management class.
        NativeEntry::GetInstance()->DisposeRootNode();
        return nullptr;
    }
    } // namespace NativeModule
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/QRMLTju3QhS1pYZjmZqx6Q/en-us_image_0000002537924832.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061941Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=854828CDAB5733971372E29496121F4BDF10E9147A605DD0FCE2E5F547AC941A)
