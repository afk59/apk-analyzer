# Native DisplaySoloist Development (C/C++)

To develop a native service that controls the frame rate in an independent thread, you use **DisplaySoloist** to implement the services, such as gaming and self-drawing UI framework interconnection.

A **DisplaySoloist** instance can exclusively occupy a thread or share a thread with others.

#### Available APIs

| Name | Description |
| :-- | :-- |
| OH\_DisplaySoloist\* OH\_DisplaySoloist\_Create (bool useExclusiveThread) | Creates an **OH\_DisplaySoloist** instance. |
| OH\_DisplaySoloist\_Destroy (OH\_DisplaySoloist \* displaySoloist) | Destroys an **OH\_DisplaySoloist** instance. |
| OH\_DisplaySoloist\_Start (OH\_DisplaySoloist \* displaySoloist, OH\_DisplaySoloist\_FrameCallback callback, void \* data ) | Sets a callback function for each frame. The callback function is triggered each time a VSync signal arrives. |
| OH\_DisplaySoloist\_Stop (OH\_DisplaySoloist \* displaySoloist) | Stops requesting the next VSync signal and triggering the callback function. |
| OH\_DisplaySoloist\_SetExpectedFrameRateRange (OH\_DisplaySoloist\* displaySoloist, DisplaySoloist\_ExpectedRateRange\* range) | Sets the expected frame rate range. |

For details, see [NativeDisplaySoloist](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-nativedisplaysoloist).

#### How to Develop

In this example, a graphic is drawn using the native Drawing module. Specifically, an expected frame rate is set through the asynchronous thread, and the graphic is drawn based on the frame rate and displayed on the native window. For details about graphics drawing, see [Using Drawing to Draw and Display Graphics (C/C++)](../../graphics-drawing-and-display/overview-of-graphics-drawing-and-display/document.md).

## Adding Dependencies

**Adding Dynamic Link Libraries**

Add the following libraries to **CMakeLists.txt**.

target\_link\_libraries(entry PUBLIC libace\_napi.z.so libnative\_drawing.so libnative\_window.so libace\_ndk.z.so libnative\_display\_soloist.so)

**Including Header Files**

#include <ace/xcomponent/native\_interface\_xcomponent.h>
#include <arpa/nameser.h>
#include <bits/alltypes.h>
#include <native\_window/external\_window.h>
#include <native\_drawing/drawing\_bitmap.h>
#include <native\_drawing/drawing\_color.h>
#include <native\_drawing/drawing\_canvas.h>
#include <native\_drawing/drawing\_pen.h>
#include <native\_drawing/drawing\_brush.h>
#include <native\_drawing/drawing\_path.h>
#include <cstdint>
#include <map>
#include <sys/mman.h>
#include <string>
#include "napi/native\_api.h"

#include <native\_display\_soloist/native\_display\_soloist.h>

## How to Develop

1.  Define an ArkTS API file and name it **XComponentContext.ts**, which is used to connect to the native layer.
    
    export default interface XComponentContext {
      register(): void;
    
      unregister(): void;
    
      destroy(): void;
    };
    
2.  Define a demo page, which contains two **XComponents**.
    
    import XComponentContext from '../interface/XComponentContext';
    // ...
    
    @Entry
    @Component
    struct Index {
      private xComponentContext1: XComponentContext | undefined = undefined;
      private xComponentContext2: XComponentContext | undefined = undefined;
    
      // ...
    
      build() {
        Column() {
          Row() {
            // ...
    
            XComponent({
              id: 'xcomponentId\_30',
              type: XComponentType.SURFACE,
              libraryname: 'entry'
            })
              .onLoad((xComponentContext) => {
                this.xComponentContext1 = xComponentContext as XComponentContext;
              }).width('640px')
              // ...
          }.height('40%')
    
          Row() {
            // ...
    
            XComponent({
              id: 'xcomponentId\_120',
              type: XComponentType.SURFACE,
              libraryname: 'entry'
            })
              .onLoad((xComponentContext) => {
                this.xComponentContext2 = xComponentContext as XComponentContext;
              }).width('640px')
              // ...
          }.height('40%')
    
          // ...
        }
      }
    }
    
3.  Obtain the native **XComponent** at the C++ layer. You are advised to save the **XComponent** in a singleton. This step must be performed during napi\_init.
    
    Create a **PluginManger** singleton to manage the native **XComponent**.
    
    class PluginManager {
    public:
        ~PluginManager();
    
        static PluginManager \*GetInstance();
    
        void SetNativeXComponent(std::string &id, OH\_NativeXComponent \*nativeXComponent);
        SampleXComponent \*GetRender(std::string &id);
        void Export(napi\_env env, napi\_value exports);
    
    private:
        std::unordered\_map<std::string, OH\_NativeXComponent \*> nativeXComponentMap\_;
        std::unordered\_map<std::string, SampleXComponent \*> pluginRenderMap\_;
    };
    
    The **SampleXComponent** class will be created in the step of drawing the graphic.
    
    void PluginManager::Export(napi\_env env, napi\_value exports)
    {
        nativeXComponentMap\_.clear();
        pluginRenderMap\_.clear();
        if ((env == nullptr) || (exports == nullptr)) {
            SAMPLE\_LOGE("Export: env or exports is null");
            return;
        }
    
        napi\_value exportInstance = nullptr;
        if (napi\_get\_named\_property(env, exports, OH\_NATIVE\_XCOMPONENT\_OBJ, &exportInstance) != napi\_ok) {
            SAMPLE\_LOGE("Export: napi\_get\_named\_property fail");
            return;
        }
    
        OH\_NativeXComponent \*nativeXComponent = nullptr;
        if (napi\_unwrap(env, exportInstance, reinterpret\_cast<void \*\*>(&nativeXComponent)) != napi\_ok) {
            SAMPLE\_LOGE("Export: napi\_unwrap fail");
            return;
        }
    
        char idStr\[OH\_XCOMPONENT\_ID\_LEN\_MAX + 1\] = {'\\0'};
        uint64\_t idSize = OH\_XCOMPONENT\_ID\_LEN\_MAX + 1;
        if (OH\_NativeXComponent\_GetXComponentId(nativeXComponent, idStr, &idSize) != OH\_NATIVEXCOMPONENT\_RESULT\_SUCCESS) {
            SAMPLE\_LOGE("Export: OH\_NativeXComponent\_GetXComponentId fail");
            return;
        }
    
        std::string id(idStr);
        auto context = PluginManager::GetInstance();
        if ((context != nullptr) && (nativeXComponent != nullptr)) {
            context->SetNativeXComponent(id, nativeXComponent);
            auto render = context->GetRender(id);
            if (render != nullptr) {
                render->RegisterCallback(nativeXComponent);
                render->Export(env, exports);
            } else {
                SAMPLE\_LOGE("render is nullptr");
            }
        }
    }
    
4.  Configure the frame rate and register the callback function at the native layer.
    
    Define the callback function for each frame.
    
    static void TestCallback(long long timestamp, long long targetTimestamp, void \*data)
    {
        // ...
        OH\_NativeXComponent \*component = nullptr;
        component = static\_cast<OH\_NativeXComponent \*>(data);
        if (component == nullptr) {
            SAMPLE\_LOGE("TestCallback: component is null");
            return;
        }
    
        char idStr\[OH\_XCOMPONENT\_ID\_LEN\_MAX + 1\] = {'\\0'};
        uint64\_t idSize = OH\_XCOMPONENT\_ID\_LEN\_MAX + 1;
        if (OH\_NativeXComponent\_GetXComponentId(component, idStr, &idSize) != OH\_NATIVEXCOMPONENT\_RESULT\_SUCCESS) {
            SAMPLE\_LOGE("TestCallback: Unable to get XComponent id");
            return;
        }
    
        std::string id(idStr);
        auto render = SampleXComponent::GetInstance(id);
        OHNativeWindow \*nativeWindow = render->GetNativeWindow();
        uint64\_t width;
        uint64\_t height;
    
        int32\_t xSize = OH\_NativeXComponent\_GetXComponentSize(component, nativeWindow, &width, &height);
        if ((xSize == OH\_NATIVEXCOMPONENT\_RESULT\_SUCCESS) && (render != nullptr)) {
            render->Prepare();
            render->Create();
            if (id == "xcomponentId\_30") {
                int offset = 16;
                render->ConstructPath(offset, offset, render->defaultOffsetY);
            }
            if (id == "xcomponentId\_120") {
                int offset = 4;
                render->ConstructPath(offset, offset, render->defaultOffsetY);
            }
            // ...
        }
    }
    
    Call the **DisplaySoloist** APIs to configure the frame rate and register the callback function for each frame. If the input parameter **useExclusiveThread** is set to **true** when **OH\_DisplaySoloist\_Create** is called to create a **DisplaySoloist** instance, **OH\_DisplaySoloist\_FrameCallback** is executed in exclusive thread mode. Otherwise, **OH\_DisplaySoloist\_FrameCallback** is executed in shared thread mode.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/CWF_sC1FSS-HSIv0Ep0ZNw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062048Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=343049C3354152E963803C143D274543A56A5C076083C40FAEC340FD3BC3A17F)
    
    -   After the instance calls **NapiRegister**, it must call **NapiUnregister** when it no longer needs to control the frame rate, so as to avoid memory leakage.
    -   During page redirection, both **NapiUnregister** and **NapiDestroy** must be called to avoid memory leakage.
    
    static std::unordered\_map<std::string, OH\_DisplaySoloist \*> g\_displaySync;
    
    // ...
    
    void ExecuteDisplaySoloist(std::string id, DisplaySoloist\_ExpectedRateRange range, bool useExclusiveThread,
                               OH\_NativeXComponent \*nativeXComponent)
    {
        OH\_DisplaySoloist \*nativeDisplaySoloist = nullptr;
        if (g\_displaySync.find(id) == g\_displaySync.end()) {
            g\_displaySync\[id\] = OH\_DisplaySoloist\_Create(useExclusiveThread);
        }
        nativeDisplaySoloist = g\_displaySync\[id\];
        OH\_DisplaySoloist\_SetExpectedFrameRateRange(nativeDisplaySoloist, &range);
        OH\_DisplaySoloist\_Start(nativeDisplaySoloist, TestCallback, nativeXComponent);
    }
    
    napi\_value SampleXComponent::NapiRegister(napi\_env env, napi\_callback\_info info)
    {
        // ...
    
        napi\_value thisArg;
        if (napi\_get\_cb\_info(env, info, nullptr, nullptr, &thisArg, nullptr) != napi\_ok) {
            SAMPLE\_LOGE("NapiRegister: napi\_get\_cb\_info fail");
            return nullptr;
        }
    
        napi\_value exportInstance;
        if (napi\_get\_named\_property(env, thisArg, OH\_NATIVE\_XCOMPONENT\_OBJ, &exportInstance) != napi\_ok) {
            SAMPLE\_LOGE("NapiRegister: napi\_get\_named\_property fail");
            return nullptr;
        }
    
        OH\_NativeXComponent \*nativeXComponent = nullptr;
        if (napi\_unwrap(env, exportInstance, reinterpret\_cast<void \*\*>(&nativeXComponent)) != napi\_ok) {
            SAMPLE\_LOGE("NapiRegister: napi\_unwrap fail");
            return nullptr;
        }
    
        char idStr\[OH\_XCOMPONENT\_ID\_LEN\_MAX + 1\] = {'\\0'};
        uint64\_t idSize = OH\_XCOMPONENT\_ID\_LEN\_MAX + 1;
        if (OH\_NativeXComponent\_GetXComponentId(nativeXComponent, idStr, &idSize) != OH\_NATIVEXCOMPONENT\_RESULT\_SUCCESS) {
            SAMPLE\_LOGE("NapiRegister: Unable to get XComponent id");
            return nullptr;
        }
        SAMPLE\_LOGI("RegisterID = %{public}s", idStr);
        std::string id(idStr);
        SampleXComponent \*render = SampleXComponent().GetInstance(id);
        if (render != nullptr) {
            DisplaySoloist\_ExpectedRateRange range;
            bool useExclusiveThread = false;
            if (id == "xcomponentId30") {
                range = {30, 120, 30};
            }
    
            if (id == "xcomponentId120") {
                range = {30, 120, 120};
            }
            ExecuteDisplaySoloist(id, range, useExclusiveThread, nativeXComponent);
        }
        return nullptr;
    }
    
    napi\_value SampleXComponent::NapiUnregister(napi\_env env, napi\_callback\_info info)
    {
        // ...
            OH\_DisplaySoloist\_Stop(g\_displaySync\[id\]);
            // ...
    }
    
    napi\_value SampleXComponent::NapiDestroy(napi\_env env, napi\_callback\_info info)
    {
        // ...
            OH\_DisplaySoloist\_Destroy(g\_displaySync\[id\]);
            g\_displaySync.erase(id);
            // ...
    }
    
    // ...
    
    void SampleXComponent::Export(napi\_env env, napi\_value exports)
    {
        if ((env == nullptr) || (exports == nullptr)) {
            SAMPLE\_LOGE("Export: env or exports is null");
            return;
        }
        napi\_property\_descriptor desc\[\] = {
            {"register", nullptr, SampleXComponent::NapiRegister, nullptr, nullptr, nullptr, napi\_default, nullptr},
            {"unregister", nullptr, SampleXComponent::NapiUnregister, nullptr, nullptr, nullptr, napi\_default, nullptr},
            {"destroy", nullptr, SampleXComponent::NapiDestroy, nullptr, nullptr, nullptr, napi\_default, nullptr}};
    
        if (napi\_define\_properties(env, exports, sizeof(desc) / sizeof(desc\[0\]), desc) != napi\_ok) {
            SAMPLE\_LOGE("Export: napi\_define\_properties failed");
        }
    }
    
5.  Register and deregister the callback function for each frame at the TS layer, and destroy the OH\_DisplaySoloist instance.
    
    aboutToDisappear(): void {
      // ...
      if (this.xComponentContext1) {
        this.xComponentContext1.unregister();
        this.xComponentContext1.destroy();
      }
      if (this.xComponentContext2) {
        this.xComponentContext2.unregister();
        this.xComponentContext2.destroy();
      }
    }
    
    // ...
    
        Row() {
          Button('Start')
            .id('Start')
            .fontSize(14)
            .fontWeight(500)
            .margin({ bottom: 20, right: 6, left: 6 })
            .onClick(() => {
              if (this.xComponentContext1) {
                this.xComponentContext1.register();
              }
              if (this.xComponentContext2) {
                this.xComponentContext2.register();
              }
            })
            .width('30%')
            .height(40)
            .shadow(ShadowStyle.OUTER\_DEFAULT\_LG)
    
          Button('Stop')
            .id('Stop')
            .fontSize(14)
            .fontWeight(500)
            .margin({ bottom: 20, left: 6 })
            .onClick(() => {
              if (this.xComponentContext1) {
                this.xComponentContext1.unregister();
              }
              if (this.xComponentContext2) {
                this.xComponentContext2.unregister();
              }
            })
            .width('30%')
            .height(40)
            .shadow(ShadowStyle.OUTER\_DEFAULT\_LG)
        }
