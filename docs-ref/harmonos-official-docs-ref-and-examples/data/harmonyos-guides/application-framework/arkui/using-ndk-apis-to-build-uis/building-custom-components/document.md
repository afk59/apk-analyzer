# Building Custom Components

The ArkUI development framework provides capabilities for creating custom UI components through NDK APIs, including custom measurement, layout, and drawing. You can integrate into ArkUI's layout and rendering process by registering custom callback events using the [registerNodeCustomEvent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1#registernodecustomevent) function and adding custom event listeners for components with the [addNodeCustomEventReceiver](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1#addnodecustomeventreceiver) function. The logic for custom measurement, layout, and drawing is handled within the callback functions of these listeners.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/JkVljzEqQZeTLecQCXoKoA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061941Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A36D35237235E67F0B5BF0D3D2C4E05027066E7F07EB8AB8D654352575EB6D8D)

-   Custom component event registration requires [addNodeCustomEventReceiver](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1#addnodecustomeventreceiver) to declare the listener registration and [registerNodeCustomEvent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1#registernodecustomevent) to declare the required custom event types; listeners can only listen for declared events.
    
-   Pay attention to the logic of event deregistration. For example, before the component is destroyed, call [removeNodeCustomEventReceiver](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1#removenodecustomeventreceiver) to remove the event listener and [unregisterNodeCustomEvent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1#unregisternodecustomevent) to notify the ArkUI framework that the listened events no longer need to be listened for.
    
-   [addNodeCustomEventReceiver](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1#addnodecustomeventreceiver) can add multiple function pointers, each of which is triggered when the corresponding event occurs. To remove a listener, the corresponding [removeNodeCustomEventReceiver](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1#removenodecustomeventreceiver) function must be called with the exact function pointer used for adding the listener.
    
-   [registerNodeCustomEventReceiver](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1#registernodecustomeventreceiver) is a global event listener function. Unlike [addNodeCustomEventReceiver](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1#addnodecustomeventreceiver), [registerNodeCustomEventReceiver](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1#registernodecustomeventreceiver) can listen for the event triggers of all native components, but it can only accept a single function pointer. If it is called multiple times, only the last function pointer provided will be used for callbacks. To release the listener, use the **unregisterNodeCustomEventReceiver** function.
    
-   Custom component-related APIs ([measureNode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1#measurenode), [layoutNode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1#layoutnode), [setMeasuredSize](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1#setmeasuredsize), and [setLayoutPosition](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1#setlayoutposition)) can only be used in the corresponding custom event callbacks ([ARKUI\_NODE\_CUSTOM\_EVENT\_ON\_MEASURE, ARKUI\_NODE\_CUSTOM\_EVENT\_ON\_LAYOUT](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-node-h#arkui_nodecustomeventtype)).
    

#### Custom Layout Container

The following example creates a custom container that uses the maximum size of its child components, plus additional padding, as its own size, while center-aligning the child components.

**Figure 1** Custom container component

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/03/v3/61VhtqWZRzyqEfEz9IOOWg/en-us_image_0000002537764890.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061941Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=55C3AC698C0D7512A4FCD7BF799F5F3B59F13F1151884FE8FBBEFC944BF6A291)

1.  Follow the instructions in [Integrating with ArkTS Pages](../integrating-with-arkts-pages/document.md) to create a project.
    
2.  Create an encapsulated object for the custom container component.
    
    // ArkUICustomContainerNode.h
    // Example of a custom container component
    
    #ifndef MYAPPLICATION\_ARKUICUSTOMCONTAINERNODE\_H
    #define MYAPPLICATION\_ARKUICUSTOMCONTAINERNODE\_H
    
    #include "ArkUINode.h"
    
    namespace NativeModule {
    
        class ArkUICustomContainerNode : public ArkUINode {
        public:
            // Create the component using the custom component type ARKUI\_NODE\_CUSTOM.
            ArkUICustomContainerNode()
                : ArkUINode((NativeModuleInstance::GetInstance()->GetNativeNodeAPI())->createNode(ARKUI\_NODE\_CUSTOM))
            {
                // Register the custom event listener.
                nativeModule\_->addNodeCustomEventReceiver(handle\_, OnStaticCustomEvent);
                // Declare the custom event and pass itself as custom data.
                nativeModule\_->registerNodeCustomEvent(handle\_, ARKUI\_NODE\_CUSTOM\_EVENT\_ON\_MEASURE, 0, this);
                nativeModule\_->registerNodeCustomEvent(handle\_, ARKUI\_NODE\_CUSTOM\_EVENT\_ON\_LAYOUT, 0, this);
            }
    
            ~ArkUICustomContainerNode() override
            {
                // Unregister the custom event listener.
                nativeModule\_->removeNodeCustomEventReceiver(handle\_, OnStaticCustomEvent);
                // Remove the declaration of the custom event.
                nativeModule\_->unregisterNodeCustomEvent(handle\_, ARKUI\_NODE\_CUSTOM\_EVENT\_ON\_MEASURE);
                nativeModule\_->unregisterNodeCustomEvent(handle\_, ARKUI\_NODE\_CUSTOM\_EVENT\_ON\_LAYOUT);
            }
    
            void SetPadding(int32\_t padding)
            {
                padding\_ = padding;
                // To update a custom property event, you need to proactively call the API for marking the dirty region.
                nativeModule\_->markDirty(handle\_, NODE\_NEED\_MEASURE);
            }
    
        private:
            static void OnStaticCustomEvent(ArkUI\_NodeCustomEvent \*event)
            {
                // Obtain the component instance object and call the related instance method.
                auto customNode = reinterpret\_cast<ArkUICustomContainerNode \*>(OH\_ArkUI\_NodeCustomEvent\_GetUserData(event));
                auto type = OH\_ArkUI\_NodeCustomEvent\_GetEventType(event);
                switch (type) {
                    case ARKUI\_NODE\_CUSTOM\_EVENT\_ON\_MEASURE:
                        customNode->OnMeasure(event);
                        break;
                    case ARKUI\_NODE\_CUSTOM\_EVENT\_ON\_LAYOUT:
                        customNode->OnLayout(event);
                        break;
                    default:
                        break;
                }
            }
    
            // Custom measurement logic.
            void OnMeasure(ArkUI\_NodeCustomEvent \*event)
            {
                auto layoutConstrain = OH\_ArkUI\_NodeCustomEvent\_GetLayoutConstraintInMeasure(event);
                // Create child node layout constraints, reusing the percentage reference values in the parent component layout.
                auto childLayoutConstrain = OH\_ArkUI\_LayoutConstraint\_Copy(layoutConstrain);
                int32\_t maxConstrain = 1000;
                OH\_ArkUI\_LayoutConstraint\_SetMaxHeight(childLayoutConstrain, maxConstrain);
                OH\_ArkUI\_LayoutConstraint\_SetMaxWidth(childLayoutConstrain, maxConstrain);
                OH\_ArkUI\_LayoutConstraint\_SetMinHeight(childLayoutConstrain, 0);
                OH\_ArkUI\_LayoutConstraint\_SetMinWidth(childLayoutConstrain, 0);
    
                // Measure the child nodes to get the maximum values.
                auto totalSize = nativeModule\_->getTotalChildCount(handle\_);
                int32\_t maxWidth = 0;
                int32\_t maxHeight = 0;
                for (uint32\_t i = 0; i < totalSize; i++) {
                    auto child = nativeModule\_->getChildAt(handle\_, i);
                    // Call the measurement API to measure the native component.
                    nativeModule\_->measureNode(child, childLayoutConstrain);
                    auto size = nativeModule\_->getMeasuredSize(child);
                    if (size.width > maxWidth) {
                        maxWidth = size.width;
                    }
                    if (size.height > maxHeight) {
                        maxHeight = size.height;
                    }
                }
                // The custom measurement result equals the sum of all child node sizes plus a fixed margin. The final size of the custom node will be set to this calculated value.
                const int paddingMultiplier = 2;
                nativeModule\_->setMeasuredSize(handle\_, maxWidth + paddingMultiplier \* padding\_,
                                               maxHeight + paddingMultiplier \* padding\_);
            }
    
            void OnLayout(ArkUI\_NodeCustomEvent \*event)
            {
                // Obtain the desired position of the parent component and set it.
                auto position = OH\_ArkUI\_NodeCustomEvent\_GetPositionInLayout(event);
                nativeModule\_->setLayoutPosition(handle\_, position.x, position.y);
    
                // Set child components to be center-aligned.
                auto totalSize = nativeModule\_->getTotalChildCount(handle\_);
                auto selfSize = nativeModule\_->getMeasuredSize(handle\_);
                for (uint32\_t i = 0; i < totalSize; i++) {
                    auto child = nativeModule\_->getChildAt(handle\_, i);
                    // Obtain the child component size.
                    auto childSize = nativeModule\_->getMeasuredSize(child);
                    // Lay out the child components.
                    int32\_t horizontalMargin = (selfSize.width - childSize.width) / 2;
                    int32\_t verticalMargin = (selfSize.height - childSize.height) / 2;
                    nativeModule\_->layoutNode(child, horizontalMargin, verticalMargin);
                }
            }
    
            int32\_t padding\_ = 100;
        };
    
    } // namespace NativeModule
    
    #endif // MYAPPLICATION\_ARKUICUSTOMCONTAINERNODE\_H
    
3.  Use the custom container to create a sample UI with text.
    
    #include "NativeEntry.h"
    
    #include "ArkUICustomContainerNode.h"
    #include "ArkUITextNode.h"
    #include "UITimer.h"
    
    #include <arkui/native\_node\_napi.h>
    #include <arkui/native\_type.h>
    #include <js\_native\_api.h>
    
    namespace NativeModule {
        namespace {
            napi\_env g\_env;
        } // namespace
    
        napi\_value CreateNativeRoot(napi\_env env, napi\_callback\_info info)
        {
            size\_t argc = 1;
            napi\_value args\[1\] = {nullptr};
    
            napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);
    
            ArkUI\_NodeContentHandle contentHandle;
            OH\_ArkUI\_GetNodeContentFromNapiValue(env, args\[0\], &contentHandle);
            NativeEntry::GetInstance()->SetContentHandle(contentHandle);
    
            // Create a custom container and text component.
            auto node = std::make\_shared<ArkUICustomContainerNode>();
            node->SetBackgroundColor(0xFFE0FFFF);
            auto textNode = std::make\_shared<ArkUITextNode>();
            textNode->SetTextContent("CustomContainer Example");
            const int32\_t fontSize = 16;
            textNode->SetFontSize(fontSize);
            textNode->SetBackgroundColor(0xFFfffacd);
            textNode->SetTextAlign(ARKUI\_TEXT\_ALIGNMENT\_CENTER);
            node->AddChild(textNode);
            auto onClick = \[\](ArkUI\_NodeEvent \*event) {
                auto textNode = (ArkUITextNode \*)OH\_ArkUI\_NodeEvent\_GetUserData(event);
                textNode->SetFontColor(0xFF00FF7F);
            };
            textNode->RegisterOnClick(onClick, textNode.get());
    
            // Keep the native side object in the management class to maintain its lifecycle.
            NativeEntry::GetInstance()->SetRootNode(node);
            g\_env = env;
            return nullptr;
        }
    
        napi\_value DestroyNativeRoot(napi\_env env, napi\_callback\_info info)
        {
            // Release the native side object from the management class.
            NativeEntry::GetInstance()->DisposeRootNode();
            return nullptr;
        }
    
    } // namespace NativeModule
    
4.  Update the **CMakeLists.txt** file and add the required link libraries.
    
      # CMakeLists.txt
    
      # the minimum version of CMake.
      cmake\_minimum\_required(VERSION 3.4.1)
      project(testndk)
    
      set(NATIVERENDER\_ROOT\_PATH ${CMAKE\_CURRENT\_SOURCE\_DIR})
    
      include\_directories(${NATIVERENDER\_ROOT\_PATH}
                           ${NATIVERENDER\_ROOT\_PATH}/include)
    
      add\_library(entry SHARED NativeEntry.cpp napi\_init.cpp)
      # target\_link\_libraries(entry PUBLIC libace\_napi.z.so, libace\_ndk.z.so, libhilog\_ndk.z.so)
    
      find\_library(
           # Sets the name of the path variable.
           hilog-lib
           # Specifies the name of the NDK library that
           # you want CMake to locate.
           hilog\_ndk.z
       )
    
      find\_library(
           # Sets the name of the path variable.
           libace-lib
           # Specifies the name of the NDK library that
           # you want CMake to locate.
           ace\_ndk.z
       )
    
      find\_library(
           # Sets the name of the path variable.
           libnapi-lib
           # Specifies the name of the NDK library that
           # you want CMake to locate.
           ace\_napi.z
       )
    
       find\_library(
            # Sets the name of the path variable.
            libuv-lib
            uv
        )
    
      target\_link\_libraries(entry PUBLIC
           ${hilog-lib} ${libace-lib} ${libnapi-lib} ${libuv-lib} )
    

#### Custom Drawing Component

The following example creates a custom drawing component that can draw a custom rectangle and uses the aforementioned custom container for layout arrangement.

**Figure 2** Custom drawing component

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0a/v3/efdZQTYLSfGESeK67c5_Ng/en-us_image_0000002537924830.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061941Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=131B185A3276B9ED2B33A6CB512C89A751F7E398079D977988283DD2FD9F12B3)

1.  Prepare a project as instructed in [Custom Layout Container](#custom-layout-container).
    
2.  Create an encapsulated object for the custom drawing component.
    
    // ArkUICustomNode.h
    // Example of a custom drawing component
    
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
                nativeModule\_->registerNodeCustomEvent(handle\_, ARKUI\_NODE\_CUSTOM\_EVENT\_ON\_DRAW, 0, this);
            }
    
            ~ArkUICustomNode() override
            {
                // Unregister the custom event listener.
                nativeModule\_->removeNodeCustomEventReceiver(handle\_, OnStaticCustomEvent);
                // Remove the declaration of the custom event.
                nativeModule\_->unregisterNodeCustomEvent(handle\_, ARKUI\_NODE\_CUSTOM\_EVENT\_ON\_DRAW);
            }
    
            void SetRectColor(uint32\_t color)
            {
                color\_ = color;
                // Custom drawing property changes require proactive notification to the framework.
                nativeModule\_->markDirty(handle\_, NODE\_NEED\_RENDER);
            }
    
        private:
            static void OnStaticCustomEvent(ArkUI\_NodeCustomEvent \*event)
            {
                // Obtain the component instance object and call the related instance method.
                auto customNode = reinterpret\_cast<ArkUICustomNode \*>(OH\_ArkUI\_NodeCustomEvent\_GetUserData(event));
                auto type = OH\_ArkUI\_NodeCustomEvent\_GetEventType(event);
                switch (type) {
                    case ARKUI\_NODE\_CUSTOM\_EVENT\_ON\_DRAW:
                        customNode->OnDraw(event);
                        break;
                    default:
                        break;
                }
            }
    
            // Custom drawing logic
            void OnDraw(ArkUI\_NodeCustomEvent \*event)
            {
                auto drawContext = OH\_ArkUI\_NodeCustomEvent\_GetDrawContextInDraw(event);
                // Obtain the graphics drawing object.
                auto drawCanvas = reinterpret\_cast<OH\_Drawing\_Canvas \*>(OH\_ArkUI\_DrawContext\_GetCanvas(drawContext));
                // Obtain the component size.
                auto size = OH\_ArkUI\_DrawContext\_GetSize(drawContext);
                // Draw custom content.
                auto path = OH\_Drawing\_PathCreate();
                const float kQuarter = 0.25f;
                const float kThreeQuarters = 0.75f;
                OH\_Drawing\_PathMoveTo(path, size.width \* kQuarter, size.height \* kQuarter);
                OH\_Drawing\_PathLineTo(path, size.width \* kThreeQuarters, size.height \* kQuarter);
                OH\_Drawing\_PathLineTo(path, size.width \* kThreeQuarters, size.height \* kThreeQuarters);
                OH\_Drawing\_PathLineTo(path, size.width \* kQuarter, size.height \* kThreeQuarters);
                OH\_Drawing\_PathLineTo(path, size.width \* kQuarter, size.height \* kQuarter);
                OH\_Drawing\_PathClose(path);
                auto brush = OH\_Drawing\_BrushCreate();
                OH\_Drawing\_BrushSetColor(brush, color\_);
                OH\_Drawing\_CanvasAttachBrush(drawCanvas, brush);
                OH\_Drawing\_CanvasDrawPath(drawCanvas, path);
                // Release resources.
                OH\_Drawing\_BrushDestroy(brush);
                OH\_Drawing\_PathDestroy(path);
            }
    
            uint32\_t color\_ = 0xFFFFE4B5;
        };
    
    } // namespace NativeModule
    
    #endif // MYAPPLICATION\_ARKUICUSTOMNODE\_H
    
3.  Use the custom drawing component and custom container to create a sample UI.
    
    #include "NativeEntry.h"
    
    #include "ArkUICustomContainerNode.h"
    #include "ArkUICustomNode.h"
    
    #include <arkui/native\_node\_napi.h>
    #include <arkui/native\_type.h>
    #include <js\_native\_api.h>
    #include "UITimer.h"
    
    namespace NativeModule {
        namespace {
            napi\_env g\_env;
        } // namespace
    
        napi\_value CreateNativeRoot(napi\_env env, napi\_callback\_info info)
        {
            size\_t argc = 1;
            napi\_value args\[1\] = {nullptr};
    
            napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);
    
            // Obtain NodeContent.
            ArkUI\_NodeContentHandle contentHandle;
            OH\_ArkUI\_GetNodeContentFromNapiValue(env, args\[0\], &contentHandle);
            NativeEntry::GetInstance()->SetContentHandle(contentHandle);
    
            // Create a custom container and a custom drawing component.
            auto node = std::make\_shared<ArkUICustomContainerNode>();
            node->SetBackgroundColor(0xFFE0FFFF);
            auto customNode = std::make\_shared<ArkUICustomNode>();
            customNode->SetBackgroundColor(0xFFD3D3D3);
            const int width = 150;
            const int height = 150;
            customNode->SetWidth(width);
            customNode->SetHeight(height);
            node->AddChild(customNode);
            auto onClick = \[\](ArkUI\_NodeEvent \*event) {
                auto customNode = (ArkUICustomNode \*)OH\_ArkUI\_NodeEvent\_GetUserData(event);
                customNode->SetRectColor(0xFF00FF7F);
            };
            customNode->RegisterOnClick(onClick, customNode.get());
    
            // Keep the native side object in the management class to maintain its lifecycle.
            NativeEntry::GetInstance()->SetRootNode(node);
            g\_env = env;
            return nullptr;
        }
    
        napi\_value DestroyNativeRoot(napi\_env env, napi\_callback\_info info)
        {
            // Release the native side object from the management class.
            NativeEntry::GetInstance()->DisposeRootNode();
            return nullptr;
        }
    
    } // namespace NativeModule
    
4.  Update the **CMakeLists.txt** file and add the required link libraries.
    
      # CMakeLists.txt
    
      # the minimum version of CMake.
      cmake\_minimum\_required(VERSION 3.4.1)
      project(testndk)
    
      set(NATIVERENDER\_ROOT\_PATH ${CMAKE\_CURRENT\_SOURCE\_DIR})
    
      include\_directories(${NATIVERENDER\_ROOT\_PATH}
                           ${NATIVERENDER\_ROOT\_PATH}/include)
    
      add\_library(entry SHARED NativeEntry.cpp napi\_init.cpp)
      # target\_link\_libraries(entry PUBLIC libace\_napi.z.so, libace\_ndk.z.so, libhilog\_ndk.z.so)
    
      find\_library(
           # Sets the name of the path variable.
           hilog-lib
           # Specifies the name of the NDK library that
           # you want CMake to locate.
           hilog\_ndk.z
       )
    
      find\_library(
           # Sets the name of the path variable.
           libace-lib
           # Specifies the name of the NDK library that
           # you want CMake to locate.
           ace\_ndk.z
       )
    
      find\_library(
           # Sets the name of the path variable.
           libnapi-lib
           # Specifies the name of the NDK library that
           # you want CMake to locate.
           ace\_napi.z
       )
    
       find\_library(
            # Sets the name of the path variable.
            libuv-lib
            uv
        )
    
      target\_link\_libraries(entry PUBLIC
           ${hilog-lib} ${libace-lib} ${libnapi-lib} ${libuv-lib} libnative\_drawing.so)
    

#### Irregular Grid Layout Example

The following example creates an irregular grid layout container that supports grid cells of different sizes to achieve a layout similar to the waterfall layout.

Figure 3 Irregular grid layout

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/re9KpDPPR3-0_C5goYbHLw/en-us_image_0000002568684607.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061941Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1EF4F6246719C93798AFC53DC436FD9227D51746C174FD4870A010A4EFCD88D5)

1.  Prepare a project as instructed in [Custom Layout Container](#custom-layout-container).
    
2.  Create the encapsulation object of the irregular grid layout container component.
    
    // ArkUIIrregularGridNode.h
    // Example of an irregular grid layout container
    
    #ifndef MYAPPLICATION\_ARKUIIRREGULARGRIDNODE\_H
    #define MYAPPLICATION\_ARKUIIRREGULARGRIDNODE\_H
    
    #include "ArkUINode.h"
    #include <vector>
    #include <map>
    
    namespace NativeModule {
    
    // Grid cell configuration
    struct GridItemConfig {
        int32\_t rowSpan = 1; // Number of rows occupied
        int32\_t columnSpan = 1; // Number of columns occupied
    };
    
    class ArkUIIrregularGridNode : public ArkUINode {
    public:
        // Create a component using the custom component type ARKUI\_NODE\_CUSTOM.
        ArkUIIrregularGridNode()
            : ArkUINode((NativeModuleInstance::GetInstance()->GetNativeNodeAPI())->createNode(ARKUI\_NODE\_CUSTOM))
        {
            // Register a custom event listener.
            nativeModule\_->addNodeCustomEventReceiver(handle\_, OnStaticCustomEvent);
            // Declare a custom event and pass itself as the custom data.
            nativeModule\_->registerNodeCustomEvent(handle\_, ARKUI\_NODE\_CUSTOM\_EVENT\_ON\_MEASURE, 0, this);
            nativeModule\_->registerNodeCustomEvent(handle\_, ARKUI\_NODE\_CUSTOM\_EVENT\_ON\_LAYOUT, 0, this);
        }
    
        ~ArkUIIrregularGridNode() override
        {
            // Unregister the custom event listener.
            nativeModule\_->removeNodeCustomEventReceiver(handle\_, OnStaticCustomEvent);
            // Cancel the declaration of the custom event.
            nativeModule\_->unregisterNodeCustomEvent(handle\_, ARKUI\_NODE\_CUSTOM\_EVENT\_ON\_MEASURE);
            nativeModule\_->unregisterNodeCustomEvent(handle\_, ARKUI\_NODE\_CUSTOM\_EVENT\_ON\_LAYOUT);
        }
    
        // Set the number of columns.
        void SetColumnCount(int32\_t count)
        {
            columnCount\_ = count;
            nativeModule\_->markDirty(handle\_, NODE\_NEED\_MEASURE);
        }
    
        // Set the grid spacing.
        void SetGap(int32\_t gap)
        {
            gap\_ = gap;
            nativeModule\_->markDirty(handle\_, NODE\_NEED\_MEASURE);
        }
    
        // Set the grid configuration of the child component.
        void SetItemConfig(ArkUI\_NodeHandle child, int32\_t rowSpan, int32\_t columnSpan)
        {
            GridItemConfig config;
            config.rowSpan = rowSpan;
            config.columnSpan = columnSpan;
            itemConfigs\_\[child\] = config;
            nativeModule\_->markDirty(handle\_, NODE\_NEED\_MEASURE);
        }
    
    private:
        static void OnStaticCustomEvent(ArkUI\_NodeCustomEvent \*event)
        {
            // Obtain the component instance object and call the related instance methods.
            auto customNode = reinterpret\_cast<ArkUIIrregularGridNode \*>(OH\_ArkUI\_NodeCustomEvent\_GetUserData(event));
            auto type = OH\_ArkUI\_NodeCustomEvent\_GetEventType(event);
            switch (type) {
                case ARKUI\_NODE\_CUSTOM\_EVENT\_ON\_MEASURE:
                    customNode->OnMeasure(event);
                    break;
                case ARKUI\_NODE\_CUSTOM\_EVENT\_ON\_LAYOUT:
                    customNode->OnLayout(event);
                    break;
                default:
                    break;
            }
        }
    
        // Calculate the height of a single subcomponent and update the column height information.
        void MeasureChild(ArkUI\_NodeHandle child, int32\_t cellWidth,
            ArkUI\_LayoutConstraint \*childConstraint, std::vector<int32\_t> &columnHeights)
        {
            GridItemConfig config = {1, 1};
            auto it = itemConfigs\_.find(child);
            if (it != itemConfigs\_.end()) {
                config = it->second;
            }
            if (config.columnSpan > columnCount\_) {
                config.columnSpan = columnCount\_;
            }
    
            int32\_t startColumn = FindLowestColumn(columnHeights, config.columnSpan);
            int32\_t startY = 0;
            for (int32\_t col = startColumn; col < startColumn + config.columnSpan && col < columnCount\_; col++) {
                if (columnHeights\[col\] > startY) {
                    startY = columnHeights\[col\];
                }
            }
    
            int32\_t itemWidth = cellWidth \* config.columnSpan + gap\_ \* (config.columnSpan - 1);
            OH\_ArkUI\_LayoutConstraint\_SetMaxWidth(childConstraint, itemWidth);
            OH\_ArkUI\_LayoutConstraint\_SetMinWidth(childConstraint, itemWidth);
            nativeModule\_->measureNode(child, childConstraint);
            auto size = nativeModule\_->getMeasuredSize(child);
    
            LayoutItemInfo info;
            info.x = startColumn \* (cellWidth + gap\_);
            info.y = startY;
            info.width = size.width;
            info.height = size.height;
            layoutInfo\_.push\_back(info);
    
            int32\_t newHeight = startY + size.height + gap\_;
            for (int32\_t col = startColumn; col < startColumn + config.columnSpan && col < columnCount\_; col++) {
                columnHeights\[col\] = newHeight;
            }
        }
    
        //Customized calculation logic: irregular grid layout.
        void OnMeasure(ArkUI\_NodeCustomEvent \*event)
        {
            auto layoutConstrain = OH\_ArkUI\_NodeCustomEvent\_GetLayoutConstraintInMeasure(event);
            int32\_t maxWidth = OH\_ArkUI\_LayoutConstraint\_GetMaxWidth(layoutConstrain);
    
            int32\_t totalGap = gap\_ \* (columnCount\_ - 1);
            int32\_t cellWidth = (maxWidth - totalGap) / columnCount\_;
    
            auto childConstraint = OH\_ArkUI\_LayoutConstraint\_Copy(layoutConstrain);
            std::vector<int32\_t> columnHeights(columnCount\_, 0);
            layoutInfo\_.clear();
    
            auto totalSize = nativeModule\_->getTotalChildCount(handle\_);
            for (uint32\_t i = 0; i < totalSize; i++) {
                auto child = nativeModule\_->getChildAt(handle\_, i);
                MeasureChild(child, cellWidth, childConstraint, columnHeights);
            }
    
            int32\_t maxHeight = 0;
            for (int32\_t height : columnHeights) {
                if (height > maxHeight) {
                    maxHeight = height;
                }
            }
            if (maxHeight > gap\_) {
                maxHeight -= gap\_;
            }
    
            nativeModule\_->setMeasuredSize(handle\_, maxWidth, maxHeight);
            OH\_ArkUI\_LayoutConstraint\_Dispose(childConstraint);
        }
    
        void OnLayout(ArkUI\_NodeCustomEvent \*event)
        {
            // Obtain the expected position of the parent component and set it.
            auto position = OH\_ArkUI\_NodeCustomEvent\_GetPositionInLayout(event);
            nativeModule\_->setLayoutPosition(handle\_, position.x, position.y);
    
            // Layout the child component.
            auto totalSize = nativeModule\_->getTotalChildCount(handle\_);
            for (uint32\_t i = 0; i < totalSize && i < layoutInfo\_.size(); i++) {
                auto child = nativeModule\_->getChildAt(handle\_, i);
                nativeModule\_->layoutNode(child, layoutInfo\_\[i\].x, layoutInfo\_\[i\].y);
            }
        }
    
        // Find the shortest column to ensure that the item with the specified column span can be placed.
        int32\_t FindLowestColumn(const std::vector<int32\_t>& columnHeights, int32\_t columnSpan)
        {
            int32\_t lowestColumn = 0;
            int32\_t lowestHeight = INT32\_MAX;
    
            // Traverse all possible start columns.
            for (int32\_t col = 0; col <= columnCount\_ - columnSpan; col++) {
                // Find the highest column in this range.
                int32\_t maxHeightInRange = 0;
                for (int32\_t i = col; i < col + columnSpan; i++) {
                    if (columnHeights\[i\] > maxHeightInRange) {
                        maxHeightInRange = columnHeights\[i\];
                    }
                }
    
                // If the highest point in this range is lower than the current lowest point, update the lowest column.
                if (maxHeightInRange < lowestHeight) {
                    lowestHeight = maxHeightInRange;
                    lowestColumn = col;
                }
            }
    
            return lowestColumn;
        }
    
        struct LayoutItemInfo {
            int32\_t x;
            int32\_t y;
            int32\_t width;
            int32\_t height;
        };
    
        int32\_t columnCount\_ = 3;
        int32\_t gap\_ = 10;
        std::map<ArkUI\_NodeHandle, GridItemConfig> itemConfigs\_;
        std::vector<LayoutItemInfo> layoutInfo\_;
    };
    
    } // namespace NativeModule
    
    #endif // MYAPPLICATION\_ARKUIIRREGULARGRIDNODE\_H
    
3.  Use the irregular grid layout container to create a sample UI.
    
    #include "NativeEntry.h"
    
    #include "ArkUIIrregularGridNode.h"
    #include "ArkUINode.h"
    
    #include <arkui/native\_node\_napi.h>
    #include <arkui/native\_type.h>
    #include <js\_native\_api.h>
    #include <utility>
    #include <vector>
    
    namespace NativeModule {
    namespace {
    napi\_env g\_env = nullptr;
    
    constexpr uint32\_t GRID\_BACKGROUND\_COLOR = 0xFFF5F5F5;
    constexpr int32\_t GRID\_COLUMN\_COUNT = 4;
    constexpr int32\_t GRID\_GAP = 8;
    constexpr float GRID\_ITEM\_RADIUS = 8.0f;
    constexpr float GRID\_ITEM\_BORDER\_WIDTH = 1.0f;
    constexpr uint32\_t GRID\_ITEM\_BORDER\_COLOR = 0xFFCCCCCC;
    constexpr float GRID\_ITEM\_BASE\_HEIGHT = 60.0f;
    constexpr float GRID\_ITEM\_HEIGHT\_STEP = 40.0f;
    
    using GridItemSize = std::pair<int32\_t, int32\_t>;
    
    const std::vector<GridItemSize>& GetGridItemSizes()
    {
        static const std::vector<GridItemSize> itemSizes = {
            {1, 1}, // Small square
            {2, 1}, // Vertical bar
            {1, 3}, // Horizontal bar
            {2, 2}, // Large square
            {1, 1}, // Small square
            {1, 2}, // Horizontal bar
            {3, 1}, // Very long vertical bar
        };
        return itemSizes;
    }
    
    const std::vector<uint32\_t>& GetGridItemColors()
    {
        static const std::vector<uint32\_t> colors = {
            0xFF64B5F6, // Blue
            0xFFE57373, // Red
            0xFF81C784, // Green
            0xFFFFB74D, // Orange
            0xFF9575CD, // Purple
            0xFF4DB6AC, // Cyan
            0xFFFFD54F, // Yellow
            0xFFF06292, // Pink
            0xFF7986CB, // Indigo
            0xFFA1887F, // Brown
        };
        return colors;
    }
    
    void SetNodeColorAttribute(ArkUI\_NativeNodeAPI\_1\* nodeAPI, ArkUI\_NodeHandle node, uint32\_t color)
    {
        ArkUI\_NumberValue bgColor\[\] = {{.u32 = color}};
        ArkUI\_AttributeItem bgColorItem = {bgColor, 1};
        nodeAPI->setAttribute(node, NODE\_BACKGROUND\_COLOR, &bgColorItem);
    }
    
    void SetNodeBorderRadiusAttribute(ArkUI\_NativeNodeAPI\_1\* nodeAPI, ArkUI\_NodeHandle node, float radius)
    {
        ArkUI\_NumberValue radiusValue\[\] = {{.f32 = radius}};
        ArkUI\_AttributeItem radiusItem = {radiusValue, 1};
        nodeAPI->setAttribute(node, NODE\_BORDER\_RADIUS, &radiusItem);
    }
    
    void SetNodeBorderStyle(ArkUI\_NativeNodeAPI\_1\* nodeAPI, ArkUI\_NodeHandle node)
    {
        ArkUI\_NumberValue borderWidth\[\] = {{.f32 = GRID\_ITEM\_BORDER\_WIDTH}};
        ArkUI\_AttributeItem borderWidthItem = {borderWidth, 1};
        nodeAPI->setAttribute(node, NODE\_BORDER\_WIDTH, &borderWidthItem);
    
        ArkUI\_NumberValue borderColor\[\] = {{.u32 = GRID\_ITEM\_BORDER\_COLOR}};
        ArkUI\_AttributeItem borderColorItem = {borderColor, 1};
        nodeAPI->setAttribute(node, NODE\_BORDER\_COLOR, &borderColorItem);
    }
    
    void SetNodeHeightByRowSpan(ArkUI\_NativeNodeAPI\_1\* nodeAPI, ArkUI\_NodeHandle node, int32\_t rowSpan)
    {
        float minHeight = GRID\_ITEM\_BASE\_HEIGHT + (rowSpan - 1) \* GRID\_ITEM\_HEIGHT\_STEP;
        ArkUI\_NumberValue minHeightValue\[\] = {{.f32 = minHeight}};
        ArkUI\_AttributeItem minHeightItem = {minHeightValue, 1};
        nodeAPI->setAttribute(node, NODE\_HEIGHT, &minHeightItem);
    }
    
    void AddGridItems(
        ArkUI\_NativeNodeAPI\_1\* nodeAPI,
        const std::shared\_ptr<ArkUIIrregularGridNode>& gridNode,
        const std::vector<GridItemSize>& itemSizes,
        const std::vector<uint32\_t>& colors)
    {
        for (size\_t i = 0; i < itemSizes.size(); ++i) {
            auto itemNode = nodeAPI->createNode(ARKUI\_NODE\_STACK);
            SetNodeColorAttribute(nodeAPI, itemNode, colors\[i % colors.size()\]);
            SetNodeBorderRadiusAttribute(nodeAPI, itemNode, GRID\_ITEM\_RADIUS);
            SetNodeBorderStyle(nodeAPI, itemNode);
            SetNodeHeightByRowSpan(nodeAPI, itemNode, itemSizes\[i\].first);
            gridNode->SetItemConfig(itemNode, itemSizes\[i\].first, itemSizes\[i\].second);
            nodeAPI->addChild(gridNode->GetHandle(), itemNode);
        }
    }
    } // namespace
    
    napi\_value CreateNativeRoot(napi\_env env, napi\_callback\_info info)
    {
        size\_t argc = 1;
        napi\_value args\[1\] = {nullptr};
        napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);
    
        ArkUI\_NodeContentHandle contentHandle;
        OH\_ArkUI\_GetNodeContentFromNapiValue(env, args\[0\], &contentHandle);
        NativeEntry::GetInstance()->SetContentHandle(contentHandle);
    
        auto gridNode = std::make\_shared<ArkUIIrregularGridNode>();
        gridNode->SetBackgroundColor(GRID\_BACKGROUND\_COLOR);
        gridNode->SetColumnCount(GRID\_COLUMN\_COUNT);
        gridNode->SetGap(GRID\_GAP);
    
        auto\* nodeAPI = NativeModuleInstance::GetInstance()->GetNativeNodeAPI();
        AddGridItems(nodeAPI, gridNode, GetGridItemSizes(), GetGridItemColors());
    
        // Store the native object in the manager class and maintain its lifecycle.
        NativeEntry::GetInstance()->SetRootNode(gridNode);
        g\_env = env;
        return nullptr;
    }
    
    napi\_value DestroyNativeRoot(napi\_env env, napi\_callback\_info info)
    {
        // Release the native object from the manager class.
        NativeEntry::GetInstance()->DisposeRootNode();
        return nullptr;
    }
    
    } // namespace NativeModule
