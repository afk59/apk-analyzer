# Integrating with ArkTS Pages

#### Placeholder Components

When building a UI with NDK APIs, you need to create placeholder components in the ArkTS page for mounting components created by the NDK APIs. The placeholder component type is [ContentSlot](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-components-contentslot), which can bind a [NodeContent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-arkui-nodecontent) object. This object can be passed to the native side through the Node-API for mounting and displaying native components.

-   The NDK configuration file **entry/src/main/cpp/types/libentry/oh-package.json5** must include the following content:
    
    {
      "name": "libentry.so",
      "types": "./Index.d.ts",
      "version": "1.0.0",
      "description": "Please describe the basic information."
    }
    
-   The usage of placeholder components is the same as other built-in ArkTS components. For the sample code, see [Example](#example).
    
    import nativeNode from 'libentry.so';
    import { NodeContent } from '@kit.ArkUI';
    
    @Entry
    @Component
    struct Index {
      // Initialize the NodeContent object.
      private rootSlot:NodeContent = new NodeContent();
      @State @Watch('changeNativeFlag') showNative: boolean = false;
    
      changeNativeFlag(): void {
        if (this.showNative) {
          // Pass the NodeContent object for the native side to create component mounting and display.
          nativeNode.createNativeRoot(this.rootSlot)
        } else {
          // Destroy the NativeModule component.
          nativeNode.destroyNativeRoot()
        }
      }
    
      build() {
        Column() {
          Button(this.showNative ? 'HideNativeUI' : 'ShowNativeUI')
            .onClick(() => {
            this.showNative = !this.showNative
          })
            .id('btn')
          Row() {
            // Bind the NodeContent and ContentSlot placeholder component.
            ContentSlot(this.rootSlot)
          }.layoutWeight(1)
        }
        .width('100%')
        .height('100%')
      }
    }
    
-   The placeholder component can be transformed into a mounting object on the native side through related APIs.
    
    ArkUI\_NodeContentHandle contentHandle;
    OH\_ArkUI\_GetNodeContentFromNapiValue(env, args\[0\], &contentHandle);
    
-   The mounting object provides APIs for mounting and unmounting components.
    
    OH\_ArkUI\_NodeContent\_AddNode(handle\_, myNativeNode);
    OH\_ArkUI\_NodeContent\_RemoveNode(handle\_, myNativeNode);
    

#### NDK Component Module

The UI component capabilities provided by the NDK, including component creation, tree operations, attribute setting, and event registration, are exposed using the function pointer structs (such as [ArkUI\_NativeNodeAPI\_1](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1)), which can be obtained through the [module query API](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-interface-h#oh_arkui_getmoduleinterface).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/7LxEYIomTvmM9yFbchtopQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061940Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D19119F1AD3D92A16CA0D0B9C97A8CE868F4731B3200B912FB000914F50CDA6A)

-   The [module query API](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-interface-h#oh_arkui_getmoduleinterface) handles NDK initialization. It is recommended that you call this API for global initialization before constructing UIs with the NDK.

ArkUI\_NativeNodeAPI\_1\* arkUINativeNodeApi = nullptr;
OH\_ArkUI\_GetModuleInterface(ARKUI\_NATIVE\_NODE, ArkUI\_NativeNodeAPI\_1, arkUINativeNodeApi);

After obtaining a function pointer struct, use the functions within the struct to perform UI component operations.

-   Create and destroy components.
    
    auto listNode = arkUINativeNodeApi->createNode(ARKUI\_NODE\_LIST);
    arkUINativeNodeApi->disposeNode(listNode);
    
    To query the component types supported by the NDK API, use the [ArkUI\_NodeType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-node-h#arkui_nodetype) API.
    
-   Perform component tree operations.
    
    auto parent = arkUINativeNodeApi->createNode(ARKUI\_NODE\_STACK);
    auto child = arkUINativeNodeApi->createNode(ARKUI\_NODE\_STACK);
    arkUINativeNodeApi->addChild(parent, child);
    arkUINativeNodeApi->removeChild(parent, child);
    
-   Set attributes.
    
    auto stack = arkUINativeNodeApi->createNode(ARKUI\_NODE\_STACK);
    ArkUI\_NumberValue value\[\] = {{.f32 = 100}};
    ArkUI\_AttributeItem item = {value, 1};
    arkUINativeNodeApi->setAttribute(stack, NODE\_WIDTH, &item);
    ArkUI\_NumberValue value\_color\[\] = {{.u32 = 0xff112233}};
    ArkUI\_AttributeItem item\_color = {value\_color, 1};
    arkUINativeNodeApi->setAttribute(stack, NODE\_BACKGROUND\_COLOR, &item);
    
    To query the attribute types supported by the NDK API, use the [ArkUI\_NodeAttributeType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-node-h#arkui_nodeattributetype) API.
    
-   Register events.
    
    auto stack = arkUINativeNodeApi->createNode(ARKUI\_NODE\_STACK);
    arkUINativeNodeApi->addNodeEventReceiver(stack, \[\](ArkUI\_NodeEvent\* event){
        // process event
    });
    arkUINativeNodeApi->registerNodeEvent(stack, NODE\_ON\_CLICK, 0, nullptr);
    
    To query the event types supported by the NDK API, use the [ArkUI\_NodeEventType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-node-h#arkui_nodeeventtype) API.
    

#### Example

The following example demonstrates how to use **ContentSlot** to mount a native text list.

Sample code directory structure:

.
|——cpp
|    |——types
|    |      |——libentry
|    |      |       |——index.d.ts Bridge methods between native and ArkTS sides.
|    |——napi\_init.cpp Native bridge definitions.
|    |——NativeEntry.cpp Native bridge implementation.
|    |——NativeEntry.h Native bridge method definitions.
|    |——NativeModule.h Encapsulation of the native modules.
|    |——CMakeLists.txt C library reference file.
|    |——ArkUIBaseNode.h Base node encapsulation class.
|    |——ArkUINode.h Extended node encapsulation class.
|    |——ArkUIListNode.h List component encapsulation class.
|    |——ArkUIListItemNode.h List item component encapsulation class.
|    |——ArkUITextNode.h Text component encapsulation class.
|    |——NormalTextListExample.h Sample implementation.
|
|——ets
|    |——pages
|         |——entry.ets Application entry page hosting native components.
|

**Figure 1** Native text list

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/N9xyoU39TYK4ob89adwzGA/en-us_image_0000002537924824.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061940Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=83099D03DF37E9E78A2645A91258B2774F7C5637483DB292B59329412C5FEB0B)

1.  Declare a placeholder component for native page mounting on the ArkTS page, and notify the native side to create a text list when the page is created.
    
    import nativeNode from 'libentry.so';
    import { NodeContent } from '@kit.ArkUI';
    
    @Entry
    @Component
    struct Index {
      // Initialize the NodeContent object.
      private rootSlot:NodeContent = new NodeContent();
      @State @Watch('changeNativeFlag') showNative: boolean = false;
    
      changeNativeFlag(): void {
        if (this.showNative) {
          // Pass the NodeContent object for the native side to create component mounting and display.
          nativeNode.createNativeRoot(this.rootSlot)
        } else {
          // Destroy the NativeModule component.
          nativeNode.destroyNativeRoot()
        }
      }
    
      build() {
        Column() {
          Button(this.showNative ? 'HideNativeUI' : 'ShowNativeUI')
            .onClick(() => {
            this.showNative = !this.showNative
          })
            .id('btn')
          Row() {
            // Bind the NodeContent and ContentSlot placeholder component.
            ContentSlot(this.rootSlot)
          }.layoutWeight(1)
        }
        .width('100%')
        .height('100%')
      }
    }
    
2.  Use the **Native** template to create a project, and provide a bridging method for the Node-API on the native side, implementing the **NativeNode** module APIs on the ArkTS side.
    
    API declaration:
    
    // entry/src/main/cpp/types/libentry/Index.d.ts
    export const createNativeRoot: (content: Object) => void;
    export const destroyNativeRoot: () => void;
    
    Native implementation:
    
    // entry/src/main/cpp/napi\_init.cpp
    #include "napi/native\_api.h"
    #include "NativeEntry.h"
    
    EXTERN\_C\_START
    static napi\_value Init(napi\_env env, napi\_value exports)
    {
        // Bind the native creation and destruction of components.
        napi\_property\_descriptor desc\[\] = {
            {"createNativeRoot", nullptr,
            NativeModule::CreateNativeRoot, nullptr, nullptr,
            nullptr, napi\_default, nullptr},
            {"destroyNativeRoot", nullptr,
            NativeModule::DestroyNativeRoot, nullptr, nullptr,
            nullptr, napi\_default, nullptr}};
        napi\_define\_properties(env, exports, sizeof(desc) / sizeof(desc\[0\]), desc);
        return exports;
    }
    EXTERN\_C\_END
    
    static napi\_module demoModule = {
        .nm\_version = 1,
        .nm\_flags = 0,
        .nm\_filename = nullptr,
        .nm\_register\_func = Init,
        .nm\_modname = "entry",
        .nm\_priv = ((void \*)0),
        .reserved = {0},
    };
    
    extern "C" \_\_attribute\_\_((constructor)) void RegisterEntryModule(void) { napi\_module\_register(&demoModule); }
    
3.  Create the native page in the **NativeEntry.h** file.
    
    // NativeEntry.h
    
    #ifndef MYAPPLICATION\_NATIVEENTRY\_H
    #define MYAPPLICATION\_NATIVEENTRY\_H
    
    #include <ArkUIBaseNode.h>
    #include <arkui/native\_type.h>
    #include <js\_native\_api\_types.h>
    
    namespace NativeModule {
    
    napi\_value CreateNativeRoot(napi\_env env, napi\_callback\_info info);
    
    napi\_value DestroyNativeRoot(napi\_env env, napi\_callback\_info info);
    
    // Manage the lifecycle and memory of the native component.
    class NativeEntry {
    public:
        static NativeEntry \*GetInstance()
        {
            static NativeEntry nativeEntry;
            return &nativeEntry;
        }
    
        void SetContentHandle(ArkUI\_NodeContentHandle handle)
        {
            handle\_ = handle;
        }
    
        void SetRootNode(const std::shared\_ptr<ArkUIBaseNode> &baseNode)
        {
            root\_ = baseNode;
            // Add the native component to NodeContent for mounting and display.
            OH\_ArkUI\_NodeContent\_AddNode(handle\_, root\_->GetHandle());
        }
        void DisposeRootNode()
        {
            // Unmount the component from NodeContent and destroy the native component.
            OH\_ArkUI\_NodeContent\_RemoveNode(handle\_, root\_->GetHandle());
            root\_.reset();
        }
    
    private:
        std::shared\_ptr<ArkUIBaseNode> root\_;
        ArkUI\_NodeContentHandle handle\_;
    };
    
    } // namespace NativeModule
    
    #endif  // MYAPPLICATION\_NATIVEENTRY\_H
    
    Corresponding implementation file:
    
    // NativeEntry.cpp
    
    #include <arkui/native\_node\_napi.h>
    #include <js\_native\_api.h>
    #include "NativeEntry.h"
    #include "NormalTextListExample.h"
    
    namespace NativeModule {
    
    napi\_value CreateNativeRoot(napi\_env env, napi\_callback\_info info)
    {
        size\_t argc = 1;
        napi\_value args\[1\] = {nullptr};
    
        napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);
    
        // Obtain NodeContent.
        ArkUI\_NodeContentHandle contentHandle;
        OH\_ArkUI\_GetNodeContentFromNapiValue(env, args\[0\], &contentHandle);
        NativeEntry::GetInstance()->SetContentHandle(contentHandle);
    
        // Create a text list.
        auto list = CreateTextListExample();
    
        // Keep the native side object in the management class to maintain its lifecycle.
        NativeEntry::GetInstance()->SetRootNode(list);
        return nullptr;
    }
    
    napi\_value DestroyNativeRoot(napi\_env env, napi\_callback\_info info)
    {
        // Release the native side object from the management class.
        NativeEntry::GetInstance()->DisposeRootNode();
        return nullptr;
    }
    } // namespace NativeModule
    
    To use the C APIs provided by the NDK, add references to the required libraries (such as **libace\_ndk.z.so**) in **CMakeLists.txt**. The example uses **libentry.so** as the default dynamic library name. When adding new .cpp files, ensure that they are included in **CMakeLists.txt**. Files not listed in **CMakeLists.txt** will not be compiled.
    
    add\_library(entry SHARED napi\_init.cpp NativeEntry.cpp)
    target\_link\_libraries(entry PUBLIC libace\_napi.z.so libace\_ndk.z.so)
    
4.  Since the NDK provides C APIs, to simplify programming and project management in an object-oriented manner, it is recommended that you use C++ for secondary encapsulation. The following example shows the encapsulation classes required for the list and text components on the example page.
    
    (1) Obtain the entry module of ArkUI in the NDK API [ArkUI\_NativeNodeAPI\_1](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1), which provides a series of function pointers for component creation, tree construction, attribute setting, and event registration.
    
    // NativeModule.h
    // Provide encapsulated APIs for obtaining ArkUI modules on the native side.
    
    #ifndef MYAPPLICATION\_NATIVEMODULE\_H
    #define MYAPPLICATION\_NATIVEMODULE\_H
    
    #include <arkui/native\_node.h>
    #include <cassert>
    
    #include <arkui/native\_interface.h>
    
    namespace NativeModule {
    
    class NativeModuleInstance {
    public:
        static NativeModuleInstance \*GetInstance()
        {
            static NativeModuleInstance instance;
            return &instance;
        }
        NativeModuleInstance()
        {
            OH\_ArkUI\_GetModuleInterface(ARKUI\_NATIVE\_NODE, ArkUI\_NativeNodeAPI\_1, arkUINativeNodeApi\_);
        }
        // Expose it for use by other modules.
        ArkUI\_NativeNodeAPI\_1 \*GetNativeNodeAPI() { return arkUINativeNodeApi\_; }
    
    private:
        ArkUI\_NativeNodeAPI\_1 \*arkUINativeNodeApi\_ = nullptr;
    };
    
    } // namespace NativeModule
    
    #endif // MYAPPLICATION\_NATIVEMODULE\_H
    
    (2) Provide base class objects for list and text components to encapsulate common attributes and events.
    
    // ArkUIBaseNode.h
    // Provide a base class for component tree operations.
    #ifndef MYAPPLICATION\_ARKUIBASENODE\_H
    #define MYAPPLICATION\_ARKUIBASENODE\_H
    
    #include <arkui/native\_type.h>
    #include <list>
    #include <memory>
    
    #include "NativeModule.h"
    
    namespace NativeModule {
    
    class ArkUIBaseNode {
    public:
        explicit ArkUIBaseNode(ArkUI\_NodeHandle handle)
            : handle\_(handle), nativeModule\_(NativeModuleInstance::GetInstance()->GetNativeNodeAPI()) {}
    
        virtual ~ArkUIBaseNode()
        {
            // Encapsulate the destructor to implement child node removal functionality.
            if (!children\_.empty()) {
                for (const auto& child : children\_) {
                    nativeModule\_->removeChild(handle\_, child->GetHandle());
                }
                children\_.clear();
            }
            // Encapsulate the destructor to uniformly recover node resources.
            nativeModule\_->disposeNode(handle\_);
        }
    
        void AddChild(const std::shared\_ptr<ArkUIBaseNode> &child)
        {
            children\_.emplace\_back(child);
            OnAddChild(child);
        }
    
        void RemoveChild(const std::shared\_ptr<ArkUIBaseNode> &child)
        {
            children\_.remove(child);
            OnRemoveChild(child);
        }
    
        void InsertChild(const std::shared\_ptr<ArkUIBaseNode> &child, int32\_t index)
        {
            if (index >= children\_.size()) {
                AddChild(child);
            } else {
                auto iter = children\_.begin();
                std::advance(iter, index);
                children\_.insert(iter, child);
                OnInsertChild(child, index);
            }
        }
    
        ArkUI\_NodeHandle GetHandle() const { return handle\_; }
    
    protected:
        // Override the following functions in subclasses that act as parent containers to implement component mounting and unmounting.
        virtual void OnAddChild(const std::shared\_ptr<ArkUIBaseNode> &child) {}
        virtual void OnRemoveChild(const std::shared\_ptr<ArkUIBaseNode> &child) {}
        virtual void OnInsertChild(const std::shared\_ptr<ArkUIBaseNode> &child, int32\_t index) {}
    
        ArkUI\_NodeHandle handle\_;
        ArkUI\_NativeNodeAPI\_1 \*nativeModule\_ = nullptr;
    
    private:
        std::list<std::shared\_ptr<ArkUIBaseNode>> children\_;
    };
    } // namespace NativeModule
    
    #endif // MYAPPLICATION\_ARKUIBASENODE\_H
    
    // ArkUINode.h
    // Provide encapsulation of common attributes and events.
    #ifndef MYAPPLICATION\_ARKUINODE\_H
    #define MYAPPLICATION\_ARKUINODE\_H
    
    #include "ArkUIBaseNode.h"
    #include "NativeModule.h"
    #include <arkui/native\_node.h>
    #include <arkui/native\_type.h>
    
    namespace NativeModule {
    
    class ArkUINode : public ArkUIBaseNode {
    public:
        explicit ArkUINode(ArkUI\_NodeHandle handle) : ArkUIBaseNode(handle) {}
    
        ~ArkUINode() override {}
        
        void SetWidth(float width)
        {
            ArkUI\_NumberValue value\[\] = {{.f32 = width}};
            ArkUI\_AttributeItem item = {value, 1};
            nativeModule\_->setAttribute(handle\_, NODE\_WIDTH, &item);
        }
        void SetPercentWidth(float percent)
        {
            ArkUI\_NumberValue value\[\] = {{.f32 = percent}};
            ArkUI\_AttributeItem item = {value, 1};
            nativeModule\_->setAttribute(handle\_, NODE\_WIDTH\_PERCENT, &item);
        }
        void SetHeight(float height)
        {
            ArkUI\_NumberValue value\[\] = {{.f32 = height}};
            ArkUI\_AttributeItem item = {value, 1};
            nativeModule\_->setAttribute(handle\_, NODE\_HEIGHT, &item);
        }
        void SetPercentHeight(float percent)
        {
            ArkUI\_NumberValue value\[\] = {{.f32 = percent}};
            ArkUI\_AttributeItem item = {value, 1};
            nativeModule\_->setAttribute(handle\_, NODE\_HEIGHT\_PERCENT, &item);
        }
        void SetBackgroundColor(uint32\_t color)
        {
            ArkUI\_NumberValue value\[\] = {{.u32 = color}};
            ArkUI\_AttributeItem item = {value, 1};
            nativeModule\_->setAttribute(handle\_, NODE\_BACKGROUND\_COLOR, &item);
        }
    
    protected:
        // Implement class docking for component tree operations.
        void OnAddChild(const std::shared\_ptr<ArkUIBaseNode> &child) override
        {
            nativeModule\_->addChild(handle\_, child->GetHandle());
        }
        void OnRemoveChild(const std::shared\_ptr<ArkUIBaseNode> &child) override
        {
            nativeModule\_->removeChild(handle\_, child->GetHandle());
        }
        void OnInsertChild(const std::shared\_ptr<ArkUIBaseNode> &child, int32\_t index) override
        {
            nativeModule\_->insertChildAt(handle\_, child->GetHandle(), index);
        }
    };
    } // namespace NativeModule
    
    #endif // MYAPPLICATION\_ARKUINODE\_H
    
    (3) Implement the list component.
    
    // ArkUIListNode.h
    // Provide encapsulation for the list component.
    #ifndef MYAPPLICATION\_ARKUILISTNODE\_H
    #define MYAPPLICATION\_ARKUILISTNODE\_H
    
    #include "ArkUINode.h"
    
    namespace NativeModule {
    class ArkUIListNode : public ArkUINode {
    public:
        ArkUIListNode()
            : ArkUINode((NativeModuleInstance::GetInstance()->GetNativeNodeAPI())->createNode(ARKUI\_NODE\_LIST)) {}
    
        ~ArkUIListNode() override {}
        
        void SetScrollBarState(bool isShow)
        {
            ArkUI\_ScrollBarDisplayMode displayMode =
                isShow ? ARKUI\_SCROLL\_BAR\_DISPLAY\_MODE\_ON : ARKUI\_SCROLL\_BAR\_DISPLAY\_MODE\_OFF;
            ArkUI\_NumberValue value\[\] = {{.i32 = displayMode}};
            ArkUI\_AttributeItem item = {value, 1};
            nativeModule\_->setAttribute(handle\_, NODE\_SCROLL\_BAR\_DISPLAY\_MODE, &item);
        }
    };
    } // namespace NativeModule
    
    #endif // MYAPPLICATION\_ARKUILISTNODE\_H
    
    (4) Implement the list item component.
    
    // ArkUIListItemNode.h
    // Provide an encapsulation class for list items
    #ifndef MYAPPLICATION\_ARKUISTACKNODE\_H
    #define MYAPPLICATION\_ARKUISTACKNODE\_H
    
    #include "ArkUINode.h"
    
    namespace NativeModule {
    class ArkUIListItemNode : public ArkUINode {
    public:
        ArkUIListItemNode()
            : ArkUINode((NativeModuleInstance::GetInstance()->GetNativeNodeAPI())->createNode(ARKUI\_NODE\_LIST\_ITEM)) {}
    };
    } // namespace NativeModule
    
    #endif // MYAPPLICATION\_ARKUISTACKNODE\_H
    
    (5) Implement the text component.
    
    // ArkUITextNode.h
    // Implement an encapsulation class for the text component.
    #ifndef MYAPPLICATION\_ARKUITEXTNODE\_H
    #define MYAPPLICATION\_ARKUITEXTNODE\_H
    
    #include "ArkUINode.h"
    
    #include <string>
    
    namespace NativeModule {
    class ArkUITextNode : public ArkUINode {
    public:
        ArkUITextNode()
            : ArkUINode((NativeModuleInstance::GetInstance()->GetNativeNodeAPI())->createNode(ARKUI\_NODE\_TEXT)) {}
        
        void SetFontSize(float fontSize)
        {
            ArkUI\_NumberValue value\[\] = {{.f32 = fontSize}};
            ArkUI\_AttributeItem item = {value, 1};
            nativeModule\_->setAttribute(handle\_, NODE\_FONT\_SIZE, &item);
        }
        void SetFontColor(uint32\_t color)
        {
            ArkUI\_NumberValue value\[\] = {{.u32 = color}};
            ArkUI\_AttributeItem item = {value, 1};
            nativeModule\_->setAttribute(handle\_, NODE\_FONT\_COLOR, &item);
        }
        void SetTextContent(const std::string &content)
        {
            ArkUI\_AttributeItem item = {nullptr, 0, content.c\_str()};
            nativeModule\_->setAttribute(handle\_, NODE\_TEXT\_CONTENT, &item);
        }
        void SetTextAlign(ArkUI\_TextAlignment align)
        {
            ArkUI\_NumberValue value\[\] = {{.i32 = align}};
            ArkUI\_AttributeItem item = {value, 1};
            nativeModule\_->setAttribute(handle\_, NODE\_TEXT\_ALIGN, &item);
        }
    };
    } // namespace NativeModule
    
    #endif // MYAPPLICATION\_ARKUITEXTNODE\_H
    
5.  Complete the **CreateTextListExample** function from step 3 to create and mount the display of the native text list.
    
    // NormalTextListExample.h
    
    #ifndef MYAPPLICATION\_NORMALTEXTLISTEXAMPLE\_H
    #define MYAPPLICATION\_NORMALTEXTLISTEXAMPLE\_H
    
    #include "ArkUIBaseNode.h"
    #include "ArkUIListItemNode.h"
    #include "ArkUIListNode.h"
    #include "ArkUITextNode.h"
    
    namespace NativeModule {
    
    std::shared\_ptr<ArkUIBaseNode> CreateTextListExample()
    {
        // Create components and mount them.
        // 1: Use smart pointers to create a List component.
        auto list = std::make\_shared<ArkUIListNode>();
        list->SetPercentWidth(1);
        list->SetPercentHeight(1);
        list->SetScrollBarState(true);
        const int itemCount = 30;
        const int fontSizes = 16;
        const float screenWidth = 1;
        const int defaultHeight = 100;
        // 2: Create a ListItem child component and mount it to the List component.
        for (int32\_t i = 0; i < itemCount; ++i) {
            auto listItem = std::make\_shared<ArkUIListItemNode>();
            auto textNode = std::make\_shared<ArkUITextNode>();
            textNode->SetTextContent(std::to\_string(i));
            textNode->SetFontSize(fontSizes);
            textNode->SetFontColor(0xFF000000);
            textNode->SetPercentWidth(1);
            textNode->SetPercentWidth(screenWidth);
            textNode->SetHeight(defaultHeight);
            textNode->SetBackgroundColor(0xFFfffacd);
            textNode->SetTextAlign(ARKUI\_TEXT\_ALIGNMENT\_CENTER);
            listItem->InsertChild(textNode, i);
            list->AddChild(listItem);
        }
        return list;
    }
    } // namespace NativeModule
    
    #endif // MYAPPLICATION\_NORMALTEXTLISTEXAMPLE\_H
