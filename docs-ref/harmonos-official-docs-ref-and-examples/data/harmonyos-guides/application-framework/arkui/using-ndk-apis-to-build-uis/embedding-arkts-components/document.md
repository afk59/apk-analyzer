# Embedding ArkTS Components

ArkUI on the native side offers a subset of ArkTS features, which excludes certain capabilities such as declarative UI syntax, custom struct components, and some advanced UI components.

For scenarios requiring ArkTS-specific features, ArkUI provides a mechanism to embed ArkTS components using [ComponentContent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-arkui-componentcontent). This involves encapsulating ArkTS components and passing them to the native side, where they are converted into **ArkUI\_NodeHandle** objects through the [OH\_ArkUI\_GetNodeHandleFromNapiValue](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-node-napi-h#oh_arkui_getnodehandlefromnapivalue) API for component mounting.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f/v3/FBzYdo5OSZKJFePBAZFGyw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061941Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2571F5F3D42B648B5BED07B803F5744DBC63ABB591D3D6F1559B56B629DFB337)

-   **ArkUI\_NodeHandle** objects obtained from **OH\_ArkUI\_GetNodeHandleFromNapiValue** are for child component parameters only, such as the second parameter of the [addChild](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1#addchild) API. Using such objects in other scenarios, such as setting attributes with [setAttribute](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1#setattribute), will not take effect and will return an error code.
    
-   To modify ArkTS components on the native side, construct update data using Node-APIs, and then call the [update](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-arkui-componentcontent#update) API of **ComponentContent**.
    
-   During the process of [building custom components](../building-custom-components/document.md), functions such as **measureNode** cannot be used to call components within the ArkTS module.
    

The following example introduces the ArkTS **Refresh** component based on the [Integrating with ArkTS Pages](../integrating-with-arkts-pages/document.md) section.

**Figure 1** Mounting a text list to a Refresh component

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/GPL0qEQPRzKJRnE-oJbNGg/en-us_image_0000002568764617.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061941Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0ED7B590E1726CE545BDCA4843706E56A108338C79F6122DC1E915BF87CF2047)

1.  Register the ArkTS component creation function to the native side for it to call, and use the **ComponentContent** capability to encapsulate the creation function.
    
    // Create ArkTS components using the ComponentContent capability.
    
    import { NodeContent, UIContext, RefreshModifier, ComponentContent } from '@kit.ArkUI';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    
    const DOMAIN = 0x0000;
    
    // Define the data object for interaction between the native side and ArkTS.
    interface NativeRefreshAttribute {
      isRefreshing: boolean;
      width?: number;
      height?: number;
      backgroundColor?: number;
      refreshOffset?: number;
      pullToRefresh?: boolean;
      onRefreshing?: () => void;
      onOffsetChange?: (offset: number) => void;
    }
    
    // Define the format of the input parameters for the @Builder function.
    interface RefreshAttribute {
      isRefreshing: boolean;
      // Optimize attribute settings for performance with Modifier.
      modifier?: RefreshModifier;
      slot?: NodeContent;
      onRefreshing?: () => void;
      onOffsetChange?: (offset: number) => void;
    }
    
    // ComponentContent encapsulates the ArkTS component dependency on the global @Builder function. You can nest @Component decorated custom components within the @Builder function when needed.
    // The @Builder function provides a way of passing parameters, making it convenient to update parameters later through the update API of ComponentContent.
    @Builder
    function mixedRefresh(attribute: RefreshAttribute) {
      Refresh({ refreshing: attribute.isRefreshing }) {
        // As a container component, Refresh needs to use the ContentSlot mechanism to reserve a place for child components.
        ContentSlot(attribute.slot);
      }.attributeModifier(attribute.modifier)
      .onRefreshing(() => {
        hilog.info(DOMAIN, 'testTag', 'on onRefreshing');
        if (attribute.onRefreshing) {
          hilog.info(DOMAIN, 'testTag', 'on native onRefreshing');
          attribute.onRefreshing();
        }
      })
      .onOffsetChange((value: number) => {
        hilog.info(DOMAIN, 'testTag', 'on offset change: ' + value);
        if (attribute.onOffsetChange) {
          hilog.info(DOMAIN, 'testTag', 'on native onOffsetChange');
          attribute.onOffsetChange(value);
        }
      });
    }
    
    // Define the return value of the creation function for interaction between the ArkTS side and the native side.
    interface MixedModuleResult {
      // Define the encapsulated object for the Refresh construction function, used by the native side to convert to an ArkUI\_NodeHandle object.
      content?: ComponentContent<RefreshAttribute>;
      // As a container component, Refresh needs to use the ContentSlot mechanism to mount child components from the native side.
      childSlot?: NodeContent;
    }
    
    // Provide an entry function for creating ArkTS components.
    export function createMixedRefresh(value: NativeRefreshAttribute): MixedModuleResult {
      hilog.info(DOMAIN, 'testTag', 'createMixedRefresh');
      // Use the AppStorage object to maintain the UI context object when the ability starts.
      let uiContent = AppStorage.get<UIContext>('context');
      let modifier = new RefreshModifier();
      if (value.width) {
        modifier.width(value.width);
      }
      if (value.height) {
        modifier.height(value.height);
      }
      if (value.backgroundColor) {
        modifier.backgroundColor(value.backgroundColor);
      }
      if (value.pullToRefresh) {
        modifier.pullToRefresh(value.pullToRefresh);
      }
      if (value.refreshOffset) {
        modifier.refreshOffset(value.refreshOffset);
      }
      // Create a NodeContent slot object for mounting Refresh child components.
      let nodeSlot = new NodeContent();
      // Create the Refresh component using ComponentContent and encapsulate it.
      let content = new ComponentContent<RefreshAttribute>(uiContent!, wrapBuilder<\[RefreshAttribute\]>(mixedRefresh),
        {
          isRefreshing: value.isRefreshing,
          modifier: modifier,
          slot: nodeSlot,
          onRefreshing: value.onRefreshing,
          onOffsetChange: value.onOffsetChange
        });
      // Pass the encapsulated object of the Refresh component and its child component slot object to the native side.
      return { content: content, childSlot: nodeSlot };
    }
    
    // Define the update function for the Refresh component for updating by the native side.
    // In the update scenario, you need to return the encapsulated object of the Refresh component and its child component slot object to prevent the component from being re-created.
    export function updateMixedRefresh(refresh: ComponentContent<RefreshAttribute>, childSlot: NodeContent,
      value: NativeRefreshAttribute): void {
      let modifier = new RefreshModifier();
      if (value.width) {
        modifier.width(value.width);
      }
      if (value.height) {
        modifier.height(value.height);
      }
      if (value.backgroundColor) {
        modifier.backgroundColor(value.backgroundColor);
      }
      if (value.pullToRefresh) {
        modifier.pullToRefresh(value.pullToRefresh);
      }
      if (value.refreshOffset) {
        modifier.refreshOffset(value.refreshOffset);
      }
      // Call the update API of ComponentContent to update.
      refresh.update({
        isRefreshing: value.isRefreshing,
        modifier: modifier,
        slot: childSlot,
        onRefreshing: value.onRefreshing,
        onOffsetChange: value.onOffsetChange
      });
    }
    
2.  Register the creation and update functions with the native side.
    
    //  Index.ets
    import nativeNode from 'libentry.so';
    import { NodeContent } from '@kit.ArkUI';
    import { createMixedRefresh, updateMixedRefresh } from './MixedModule';
    
    @Entry
    @Component
    struct Index {
      private rootSlot = new NodeContent();
      @State @Watch('changeNativeFlag') showNative: boolean = false;
    
      aboutToAppear(): void {
        // Set the UI context.
        AppStorage.setOrCreate<UIContext>('context', this.getUIContext());
        // Set the builder function for mixed mode.
        nativeNode.registerCreateMixedRefreshNode(createMixedRefresh);
        nativeNode.registerUpdateMixedRefreshNode(updateMixedRefresh);
      }
    
      changeNativeFlag(): void {
        if (this.showNative) {
          // Create and mount the NativeModule component.
          nativeNode.createNativeRoot(this.rootSlot);
        } else {
          // Destroy the NativeModule component.
          nativeNode.destroyNativeRoot();
        }
      }
    
      build() {
        Column() {
          Button(this.showNative ? 'HideNativeUI' : 'ShowNativeUI').onClick(() => {
            this.showNative = !this.showNative;
          });
          Row() {
            // ArkTS inserts the native component.
            ContentSlot(this.rootSlot);
          }.layoutWeight(1)
          .id('row\_');
        }
        .width('100%')
        .height('100%');
      }
    }
    
    // native\_init.cpp
    #include "napi/native\_api.h"
    #include "ArkUIMixedRefresh.h"
    #include "NativeEntry.h"
    
    EXTERN\_C\_START
    static napi\_value Init(napi\_env env, napi\_value exports)
    {
        napi\_property\_descriptor desc\[\] = {
            {"createNativeRoot", nullptr, NativeModule::CreateNativeRoot, nullptr, nullptr, nullptr, napi\_default, nullptr},
            {"registerCreateMixedRefreshNode", nullptr, NativeModule::ArkUIMixedRefresh::RegisterCreateRefresh, nullptr,
             nullptr, nullptr, napi\_default, nullptr},
            {"registerUpdateMixedRefreshNode", nullptr, NativeModule::ArkUIMixedRefresh::RegisterUpdateRefresh, nullptr,
             nullptr, nullptr, napi\_default, nullptr},
            {"destroyNativeRoot", nullptr, NativeModule::DestroyNativeRoot, nullptr, nullptr, nullptr, napi\_default,
             nullptr}};
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
    
3.  The native side saves the creation and update functions through the Node-API for subsequent calls.
    
    // Mixed mode interaction class.
    
    #ifndef MYAPPLICATION\_ARKUIMIXEDREFRESHTEMPLATE\_H
    #define MYAPPLICATION\_ARKUIMIXEDREFRESHTEMPLATE\_H
    
    #include "ArkUIMixedNode.h"
    
    #include <optional>
    
    #include <arkui/native\_node\_napi.h>
    #include <js\_native\_api\_types.h>
    
    namespace NativeModule {
    
    class ArkUIMixedRefresh : public ArkUIMixedNode {
    public:
        static napi\_value RegisterCreateAndUpdateRefresh(napi\_env env, napi\_callback\_info info);
    };
    
    } // namespace NativeModule
    
    #endif // MYAPPLICATION\_ARKUIMIXEDREFRESHTEMPLATE\_H
    
    Related implementation class description:
    
    // Mixed mode interaction class.
    
    #include "ArkUIMixedRefreshTemplate.h"
    
    namespace NativeModule {
    namespace {
    napi\_env g\_env;
    napi\_ref g\_createRefresh;
    napi\_ref g\_updateRefresh;
    } // namespace
    
    napi\_value ArkUIMixedRefresh::RegisterCreateAndUpdateRefresh(napi\_env env, napi\_callback\_info info)
    {
        size\_t argc = 1;
        napi\_value args\[1\] = {nullptr};
    
        napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);
    
        g\_env = env;
        napi\_ref refer;
        // Save the reference after creation to prevent it from being released.
        napi\_create\_reference(env, args\[0\], 1, &refer);
    
        g\_createRefresh = refer;
        return nullptr;
    }
    
    } // namespace NativeModule
    
    Related CMakeLists configuration:
    
      # CMakeLists.txt
     
      # the minimum version of CMake.
      cmake\_minimum\_required(VERSION 3.4.1)
      project(testndk)
      
      # optional depends on C++17.
      set(CMAKE\_CXX\_STANDARD 17)
      set(NATIVERENDER\_ROOT\_PATH ${CMAKE\_CURRENT\_SOURCE\_DIR})
      
      include\_directories(${NATIVERENDER\_ROOT\_PATH}
                           ${NATIVERENDER\_ROOT\_PATH}/include)
      
      add\_library(entry SHARED NativeEntry.cpp ArkUIMixedRefresh.cpp napi\_init.cpp)
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
    
4.  Abstract the base class of components in mixed mode for general logic management.
    
    // ArkUIMixedNode.h
    // Base class for mixed mode.
    
    #ifndef MYAPPLICATION\_ARKUIMIXEDNODE\_H
    #define MYAPPLICATION\_ARKUIMIXEDNODE\_H
    
    #include <js\_native\_api.h>
    #include <js\_native\_api\_types.h>
    
    #include "ArkUIBaseNode.h"
    #include "NativeModule.h"
    
    namespace NativeModule {
    
    // Wrap ArkTS Node
    class ArkUIMixedNode : public ArkUIBaseNode {
    public:
        ArkUIMixedNode(ArkUI\_NodeHandle handle, napi\_env env, napi\_ref componentContent)
            : ArkUIBaseNode(handle), env\_(env), componentContent\_(componentContent) {}
    
        // In the base class destructor, the object on the ArkTS side in mixed mode needs to be released.
        ~ArkUIMixedNode() override { napi\_delete\_reference(env\_, componentContent\_); }
    
    protected:
        napi\_env env\_;
        napi\_ref componentContent\_;
    };
    
    } // namespace NativeModule
    
    #endif // MYAPPLICATION\_ARKUIMIXEDNODE\_H
    
5.  Implement the encapsulation object for the **Refresh** component in mixed mode.
    
    // ArkUIMixedRefresh.h
    // The encapsulation object of Refresh in mixed mode on the native side.
    
    #ifndef MYAPPLICATION\_ARKUIMIXEDREFRESH\_H
    #define MYAPPLICATION\_ARKUIMIXEDREFRESH\_H
    
    #include "ArkUIMixedNode.h"
    #include "ArkUIBaseNode.h"
    
    #include <optional>
    
    #include <arkui/native\_node\_napi.h>
    #include <js\_native\_api\_types.h>
    
    namespace NativeModule {
    
    // Define the interaction data structure between the native side and the ArkTS side.
    struct NativeRefreshAttribute {
        std::optional<bool> isRefreshing;
        std::optional<float> width;
        std::optional<float> height;
        std::optional<uint32\_t> backgroundColor;
        std::optional<float> refreshOffset;
        std::optional<bool> pullToRefresh;
        std::function<void()> onRefreshing;
        std::function<void(float)> onOffsetChange;
    };
    
    class ArkUIMixedRefresh : public ArkUIMixedNode {
    public:
        // Call the ArkTS method to create the Refresh component.
        static const std::shared\_ptr<ArkUIMixedRefresh> Create(const NativeRefreshAttribute &attribute);
    
        ArkUIMixedRefresh(ArkUI\_NodeHandle handle, ArkUI\_NodeContentHandle contentHandle, napi\_env env,
                          napi\_ref componentContent, napi\_ref nodeContent)
            : ArkUIMixedNode(handle, env, componentContent), contentHandle\_(contentHandle), nodeContent\_(nodeContent) {}
    
        ArkUIMixedRefresh() : ArkUIMixedNode(nullptr, nullptr, nullptr) {}
    
        ~ArkUIMixedRefresh() override { napi\_delete\_reference(env\_, nodeContent\_); } // Release the placeholder component slot object for the child node.
    
        void SetWidth(float width) { attribute\_.width = width; }
    
        void SetHeight(float height) { attribute\_.height = height; }
    
        void SetBackgroundColor(uint32\_t color) { attribute\_.backgroundColor = color; }
    
        void SetRefreshState(bool isRefreshing) { attribute\_.isRefreshing = isRefreshing; }
    
        void SetPullToRefresh(bool pullToRefresh) { attribute\_.pullToRefresh = pullToRefresh; }
    
        void SetRefreshOffset(float offset) { attribute\_.refreshOffset = offset; }
    
        void SetRefreshCallback(const std::function<void()> &callback) { attribute\_.onRefreshing = callback; }
    
        void SetOnOffsetChange(const std::function<void(float)> &callback) { attribute\_.onOffsetChange = callback; }
    
        // To avoid frequent cross-language communication, cache property events on the native side and notify in batches.
        void FlushMixedModeCmd();
    
        static napi\_value RegisterCreateRefresh(napi\_env env, napi\_callback\_info info);
        static napi\_value RegisterUpdateRefresh(napi\_env env, napi\_callback\_info info);
    
    protected:
        void OnAddChild(const std::shared\_ptr<ArkUIBaseNode> &child) override
        {
            // Use NodeContent to mount the component (can be a transformation object of ArkTS on the native side through ComponentContent, or a pure native component) under the ArkTS component.
            OH\_ArkUI\_NodeContent\_AddNode(contentHandle\_, child->GetHandle());
        }
    
        void OnRemoveChild(const std::shared\_ptr<ArkUIBaseNode> &child) override
        {
            // Use NodeContent to remove the component.
            OH\_ArkUI\_NodeContent\_RemoveNode(contentHandle\_, child->GetHandle());
        }
    
        void OnInsertChild(const std::shared\_ptr<ArkUIBaseNode> &child, int32\_t index) override
        {
            // Use NodeContent to insert the component.
            OH\_ArkUI\_NodeContent\_InsertNode(contentHandle\_, child->GetHandle(), index);
        }
    
    private:
        // Use the Node-API to create the data structure on the ArkTS side.
        static napi\_value CreateRefreshAttribute(const NativeRefreshAttribute &attribute, void \*userData);
        
        static void Attribute2Descriptor(const NativeRefreshAttribute &attribute, napi\_property\_descriptor \*desc);
    
        ArkUI\_NodeContentHandle contentHandle\_;
        napi\_ref nodeContent\_;
        NativeRefreshAttribute attribute\_;
    };
    
    } // namespace NativeModule
    
    #endif // MYAPPLICATION\_ARKUIMIXEDREFRESH\_H
    
    Related implementation class description:
    
    // ArkUIMixedRefresh.cpp
    
    #include "ArkUIMixedRefresh.h"
    #include <hilog/log.h>
    
    namespace NativeModule {
    namespace {
    napi\_env g\_env;
    napi\_ref g\_createRefresh;
    napi\_ref g\_updateRefresh;
    const int REFRESH\_OFFSET\_INDEX0 = 0;
    const int REFRESH\_OFFSET\_INDEX1 = 1;
    const int REFRESH\_OFFSET\_INDEX2 = 2;
    const int REFRESH\_OFFSET\_INDEX3 = 3;
    const int REFRESH\_OFFSET\_INDEX4 = 4;
    const int REFRESH\_OFFSET\_INDEX5 = 5;
    const int REFRESH\_OFFSET\_INDEX6 = 6;
    const int REFRESH\_OFFSET\_INDEX7 = 7;
    } // namespace
    
    void ArkUIMixedRefresh::Attribute2Descriptor(const NativeRefreshAttribute &attribute, napi\_property\_descriptor \*desc)
    {
        if (attribute.width) {
            napi\_value width;
            napi\_create\_double(g\_env, attribute.width.value(), &width);
            desc\[REFRESH\_OFFSET\_INDEX0\].value = width;
        }
        if (attribute.height) {
            napi\_value height;
            napi\_create\_double(g\_env, attribute.height.value(), &height);
            desc\[REFRESH\_OFFSET\_INDEX1\].value = height;
        }
        if (attribute.backgroundColor) {
            napi\_value backgroundColor;
            napi\_create\_uint32(g\_env, attribute.backgroundColor.value(), &backgroundColor);
            desc\[REFRESH\_OFFSET\_INDEX2\].value = backgroundColor;
        }
        if (attribute.pullToRefresh) {
            napi\_value pullToRefresh;
            napi\_create\_int32(g\_env, attribute.pullToRefresh.value(), &pullToRefresh);
            desc\[REFRESH\_OFFSET\_INDEX3\].value = pullToRefresh;
        }
        if (attribute.isRefreshing) {
            napi\_value isRefreshing;
            napi\_create\_int32(g\_env, attribute.isRefreshing.value(), &isRefreshing);
            desc\[REFRESH\_OFFSET\_INDEX4\].value = isRefreshing;
        }
        if (attribute.refreshOffset) {
            napi\_value refreshOffset;
            napi\_create\_double(g\_env, attribute.refreshOffset.value(), &refreshOffset);
            desc\[REFRESH\_OFFSET\_INDEX5\].value = refreshOffset;
        }
        if (attribute.onRefreshing) {
            OH\_LOG\_INFO(LOG\_APP, "onRefreshing start");
            desc\[REFRESH\_OFFSET\_INDEX6\].method = \[\](napi\_env env, napi\_callback\_info info) -> napi\_value {
                OH\_LOG\_INFO(LOG\_APP, "onRefreshing callback");
                size\_t argc = 0;
                napi\_value args\[0\];
                void \*data;
                napi\_get\_cb\_info(env, info, &argc, args, nullptr, &data);
                auto refresh = reinterpret\_cast<ArkUIMixedRefresh \*>(data);
                if (refresh && refresh->attribute\_.onRefreshing) {
                    refresh->attribute\_.onRefreshing();
                }
                return nullptr;
            };
        }
    }
    
    // Use the Node-API to create the data structure for interaction with the ArkTS side, used for the creation and update of the Refresh component.
    napi\_value ArkUIMixedRefresh::CreateRefreshAttribute(const NativeRefreshAttribute &attribute, void \*userData)
    {
        napi\_property\_descriptor desc\[\] = {
            {"width", nullptr, nullptr, nullptr, nullptr, nullptr, napi\_default, userData},
            {"height", nullptr, nullptr, nullptr, nullptr, nullptr, napi\_default, userData},
            {"backgroundColor", nullptr, nullptr, nullptr, nullptr, nullptr, napi\_default, userData},
            {"pullToRefresh", nullptr, nullptr, nullptr, nullptr, nullptr, napi\_default, userData},
            {"isRefreshing", nullptr, nullptr, nullptr, nullptr, nullptr, napi\_default, userData},
            {"refreshOffset", nullptr, nullptr, nullptr, nullptr, nullptr, napi\_default, userData},
            {"onRefreshing", nullptr, nullptr, nullptr, nullptr, nullptr, napi\_default, userData},
            {"onOffsetChange", nullptr, nullptr, nullptr, nullptr, nullptr, napi\_default, userData},
        };
        Attribute2Descriptor(attribute, desc);
        if (attribute.onOffsetChange) {
            OH\_LOG\_INFO(LOG\_APP, "onOffsetChange start");
            desc\[REFRESH\_OFFSET\_INDEX7\].method = \[\](napi\_env env, napi\_callback\_info info) -> napi\_value {
                OH\_LOG\_INFO(LOG\_APP, "onOffsetChange callback");
                size\_t argc = 1;
                napi\_value args\[1\] = {nullptr};
                void \*data;
                napi\_get\_cb\_info(env, info, &argc, args, nullptr, &data);
                double offset = 0.0;
                napi\_get\_value\_double(env, args\[0\], &offset);
                auto refresh = reinterpret\_cast<ArkUIMixedRefresh \*>(data);
                if (refresh && refresh->attribute\_.onOffsetChange) {
                    refresh->attribute\_.onOffsetChange(offset);
                }
                return nullptr;
            };
        }
        napi\_value refreshAttribute = nullptr;
        auto result = napi\_create\_object\_with\_properties(g\_env, &refreshAttribute, sizeof(desc) / sizeof(desc\[0\]), desc);
        if (result != napi\_ok) {
            return nullptr;
        }
        return refreshAttribute;
    }
    
    // Create the component on the ArkTS side and save it in the encapsulation object on the native side.
    const std::shared\_ptr<ArkUIMixedRefresh> ArkUIMixedRefresh::Create(const NativeRefreshAttribute &attribute)
    {
        napi\_handle\_scope scope;
        napi\_open\_handle\_scope(g\_env, &scope);
        auto refresh = std::make\_shared<ArkUIMixedRefresh>();
        auto refreshAttribute = CreateRefreshAttribute(attribute, refresh.get());
        if (refreshAttribute == nullptr) {
            napi\_close\_handle\_scope(g\_env, scope);
            return nullptr;
        }
        napi\_value result = nullptr;
        napi\_value argv\[1\] = {refreshAttribute};
        napi\_value createRefresh = nullptr;
        napi\_get\_reference\_value(g\_env, g\_createRefresh, &createRefresh);
        // Call the ArkTS Create function to create the ArkTS ComponentContent.
        napi\_call\_function(g\_env, nullptr, createRefresh, 1, argv, &result);
    
        // Obtain the ArkTS Refresh component.
        napi\_value componentContent = nullptr;
        napi\_get\_named\_property(g\_env, result, "content", &componentContent);
        ArkUI\_NodeHandle handle;
        OH\_ArkUI\_GetNodeHandleFromNapiValue(g\_env, componentContent, &handle);
        // Obtain the child component slot of the ArkTS Refresh component.
        napi\_value nodeContent = nullptr;
        napi\_get\_named\_property(g\_env, result, "childSlot", &nodeContent);
        ArkUI\_NodeContentHandle contentHandle;
        OH\_ArkUI\_GetNodeContentFromNapiValue(g\_env, nodeContent, &contentHandle);
        // Save the ArkTS ComponentContent to prevent the object on the ArkTS side from being released and for subsequent updates.
        napi\_ref componentContentRef;
        napi\_create\_reference(g\_env, componentContent, 1, &componentContentRef);
        // Save the ArkTS NodeContent to prevent the object on the ArkTS side from being released and for subsequent updates.
        napi\_ref nodeContentRef;
        napi\_create\_reference(g\_env, nodeContent, 1, &nodeContentRef);
        // Update the Refresh component related parameters.
        refresh->handle\_ = handle;
        refresh->env\_ = g\_env;
        refresh->componentContent\_ = componentContentRef;
        refresh->nodeContent\_ = nodeContentRef;
        refresh->contentHandle\_ = contentHandle;
        refresh->attribute\_ = attribute;
        return refresh;
    }
    // Implementation of the update function.
    void ArkUIMixedRefresh::FlushMixedModeCmd()
    {
        napi\_handle\_scope scope;
        napi\_open\_handle\_scope(g\_env, &scope);
        // Create the input parameters for the call to the ArkTS API.
        auto refreshAttribute = CreateRefreshAttribute(attribute\_, this);
        if (refreshAttribute == nullptr) {
            napi\_close\_handle\_scope(g\_env, scope);
            return;
        }
        // Obtain the remaining two API parameters for the update API.
        napi\_value componentContent = nullptr;
        napi\_get\_reference\_value(g\_env, componentContent\_, &componentContent);
        napi\_value nodeContent = nullptr;
        napi\_get\_reference\_value(g\_env, nodeContent\_, &nodeContent);
    
        napi\_value argv\[3\] = {componentContent, nodeContent, refreshAttribute};
        napi\_value updateRefresh = nullptr;
        napi\_get\_reference\_value(g\_env, g\_updateRefresh, &updateRefresh);
        // Call the ArkTS Update function to update.
        napi\_value result = nullptr;
        napi\_call\_function(g\_env, nullptr, updateRefresh, sizeof(argv) / sizeof(argv\[0\]), argv, &result);
    }
    
    napi\_value ArkUIMixedRefresh::RegisterCreateRefresh(napi\_env env, napi\_callback\_info info)
    {
        size\_t argc = 1;
        napi\_value args\[1\] = {nullptr};
    
        napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);
    
        g\_env = env;
        napi\_ref refer;
        napi\_create\_reference(env, args\[0\], 1, &refer);
    
        g\_createRefresh = refer;
        return nullptr;
    }
    
    napi\_value ArkUIMixedRefresh::RegisterUpdateRefresh(napi\_env env, napi\_callback\_info info)
    {
        size\_t argc = 1;
        napi\_value args\[1\] = {nullptr};
    
        napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);
    
        g\_env = env;
        napi\_ref refer;
        napi\_create\_reference(env, args\[0\], 1, &refer);
    
        g\_updateRefresh = refer;
        return nullptr;
    }
    
    } // namespace NativeModule
    
6.  Implement a simple timer module.
    
    // UITimer.h
    // Timer module.
    
    #ifndef MYAPPLICATION\_UITIMER\_H
    #define MYAPPLICATION\_UITIMER\_H
    
    #include <hilog/log.h>
    #include <js\_native\_api.h>
    #include <js\_native\_api\_types.h>
    #include <node\_api.h>
    #include <node\_api\_types.h>
    #include <string>
    #include <thread>
    #include <uv.h>
    
    namespace NativeModule {
    
    struct UIData {
        void \*userData = nullptr;
        int32\_t count = 0;
        int32\_t totalCount = 0;
        void (\*func)(void \*userData, int32\_t count) = nullptr;
    };
    
    napi\_threadsafe\_function threadSafeFunction = nullptr;
    
    void CreateNativeTimer(napi\_env env, void \*userData, int32\_t totalCount, void (\*func)(void \*userData, int32\_t count))
    {
        napi\_value name;
        std::string str = "UICallback";
        napi\_create\_string\_utf8(env, str.c\_str(), str.size(), &name);
        // UI main thread callback function.
        napi\_create\_threadsafe\_function(
            env, nullptr, nullptr, name, 0, 1, nullptr, nullptr, nullptr,
            \[\](napi\_env env, napi\_value value, void \*context, void \*data) {
                auto userdata = reinterpret\_cast<UIData \*>(data);
                userdata->func(userdata->userData, userdata->count);
                delete userdata;
            },
            &threadSafeFunction);
        // Start the timer to simulate data changes.
        std::thread timerThread(\[data = userData, totalCount, func\]() {
            uv\_loop\_t \*loop = uv\_loop\_new();
            uv\_timer\_t \*timer = new uv\_timer\_t();
            uv\_timer\_init(loop, timer);
            timer->data = new UIData{data, 0, totalCount, func};
            uint64\_t timeout = 4000;
            uint64\_t repeat = 4000;
            uv\_timer\_start(
                timer,
                \[\](uv\_timer\_t \*handle) {
                    OH\_LOG\_INFO(LOG\_APP, "on timeout");
                    napi\_acquire\_threadsafe\_function(threadSafeFunction);
                    auto \*customData = reinterpret\_cast<UIData \*>(handle->data);
                    // Create callback data.
                    auto \*callbackData =
                        new UIData{customData->userData, customData->count, customData->totalCount, customData->func};
                    napi\_call\_threadsafe\_function(threadSafeFunction, callbackData, napi\_tsfn\_blocking);
                    customData->count++;
                    if (customData->count > customData->totalCount) {
                        uv\_timer\_stop(handle);
                        delete handle;
                        delete customData;
                    }
                },
                timeout, repeat);
            uv\_run(loop, UV\_RUN\_DEFAULT);
            uv\_loop\_delete(loop);
        });
        timerThread.detach();
    }
    } // namespace NativeModule
    
    #endif // MYAPPLICATION\_UITIMER\_H
    
7.  Use the page structure described in [Integrating with ArkTS Pages](../integrating-with-arkts-pages/document.md), making the **Refresh** component the parent component of the text list.
    
    // MixedRefreshExample.h
    // Sample code for mixed mode.
    
    #ifndef MYAPPLICATION\_MIXEDREFRESHEXAMPLE\_H
    #define MYAPPLICATION\_MIXEDREFRESHEXAMPLE\_H
    
    #include "ArkUIBaseNode.h"
    #include "ArkUIMixedRefresh.h"
    #include "NormalTextListExample.h"
    #include "UITimer.h"
    
    #include <js\_native\_api\_types.h>
    
    namespace NativeModule {
    
    std::shared\_ptr<ArkUIBaseNode> CreateMixedRefreshList(napi\_env env)
    {
        auto list = CreateTextListExample();
        // Create the Refresh component in mixed mode and mount the List component.
        NativeRefreshAttribute nativeRefreshAttribute{
            .backgroundColor = 0xFF89CFF0, .refreshOffset = 64, .pullToRefresh = true};
        auto refresh = ArkUIMixedRefresh::Create(nativeRefreshAttribute);
        refresh->AddChild(list);
    
        // Set the event for mixed mode.
        refresh->SetOnOffsetChange(
            \[\](float offset) { OH\_LOG\_INFO(LOG\_APP, "on refresh offset changed: %{public}f", offset); });
        refresh->SetRefreshCallback(\[refreshPtr = refresh.get(), env\]() {
            OH\_LOG\_INFO(LOG\_APP, "on refreshing");
            // Start the timer to simulate data acquisition.
            CreateNativeTimer(env, refreshPtr, 1, \[\](void \*userData, int32\_t count) {
                // Disable the refresh feature after data is obtained.
                auto refresh = reinterpret\_cast<ArkUIMixedRefresh \*>(userData);
                refresh->SetRefreshState(false);
                refresh->FlushMixedModeCmd();
            });
        });
    
        // Update the event to the ArkTS side.
        refresh->FlushMixedModeCmd();
        return refresh;
    }
    
    } // namespace NativeModule
    
    #endif // MYAPPLICATION\_MIXEDREFRESHEXAMPLE\_H
    
    Replace the entry component creation with the pull-to-refresh text list.
    
    // NativeEntry.cpp
    
    #include "NativeEntry.h"
    
    #include "ArkUIMixedRefresh.h"
    #include "MixedRefreshExample.h"
    #include "NormalTextListExample.h"
    
    #include <arkui/native\_node\_napi.h>
    #include <arkui/native\_type.h>
    #include <js\_native\_api.h>
    #include <uv.h>
    
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
    
        // Create a Refresh text list.
        auto refresh = CreateMixedRefreshList(env);
    
        // Keep the native side object in the management class to maintain its lifecycle.
        NativeEntry::GetInstance()->SetRootNode(refresh);
        return nullptr;
    }
    
    napi\_value DestroyNativeRoot(napi\_env env, napi\_callback\_info info)
    {
        // Release the native side object from the management class.
        NativeEntry::GetInstance()->DisposeRootNode();
        return nullptr;
    }
    
    } // namespace NativeModule
    
8.  Implement Node-API bridging to expose NativeNode module APIs from the native side to ArkTS.
    
    export const createNativeRoot: (content: Object) => void;
    export const destroyNativeRoot: () => void;
    
    export const registerCreateMixedRefreshNode: (content: Object) => void;
    export const registerUpdateMixedRefreshNode: (content: Object) => void;
