# Requesting Frame Rates for Custom Content

When you use native APIs to develop an application based on the [XComponent](../../../../application-framework/arkui/ui-development-arkts-based-declarative-development-paradigm/adding-a-component/custom-rendering-xcomponent/document.md), you can request an independent frame rate for custom content in scenarios such as gaming and custom UI framework interconnection.

#### Available APIs

| Name | Description |
| :-- | :-- |
| OH\_NativeXComponent\_SetExpectedFrameRateRange (OH\_NativeXComponent \*component, OH\_NativeXComponent\_ExpectedRateRange \*range) | Sets the expected frame rate range. |
| OH\_NativeXComponent\_RegisterOnFrameCallback (OH\_NativeXComponent \*component, OH\_NativeXComponent\_OnFrameCallback \*callback) | Registers the display update callback and enables the callback for each frame. |
| OH\_NativeXComponent\_UnRegisterOnFrameCallback (OH\_NativeXComponent \*component) | Deregisters the display update callback and disables the callback for each frame. |

For details about the APIs, see [OH\_NativeXComponent Native XComponent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-oh-nativexcomponent-native-xcomponent).

#### How to Develop

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/iEwejUV_RDu5Pxv-Kr_EDQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062048Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=12BD510A561238AEBDEBA50F3A2A91EEB86ED802E38E7752DF0DEDA4C6B5E8CA)

This section draws a graphic through the native Drawing module and presents it using the native Window module. For details, see [Using Drawing to Draw and Display Graphics](../../graphics-drawing-and-display/overview-of-graphics-drawing-and-display/document.md).

1.  Add dependencies.
    
    Add the following library to **CMakeLists.txt**.
    
    target\_link\_libraries(entry PUBLIC libace\_napi.z.so libnative\_drawing.so libnative\_window.so libace\_ndk.z.so)
    
    Import the required header files.
    
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
    
    #include <native\_drawing/drawing\_text\_typography.h>
    
2.  Define an ArkTS API file and name it **XComponentContext.ts**, which is used to connect to the native layer.
    
    export default interface XComponentContext {
      register(): void;
    
      unregister(): void;
    };
    
3.  Define a demo page, which contains two **XComponents**.
    
    import XComponentContext from '../interface/XComponentContext';
    // ...
    
    @Entry
    @Component
    struct Index {
      private xComponentContext1: XComponentContext | undefined = undefined;
      private xComponentContext2: XComponentContext | undefined = undefined;
    
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
    
4.  Configure the frame rate and register the callback function at the native layer.
    
    static void TestCallback(OH\_NativeXComponent \*component, uint64\_t timestamp, uint64\_t targetTimestamp)
    {
        // ...
        
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
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/zOFfvK_7SxGId2p9u7fjPQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062048Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6403EFD230D8F170FE9244BA7E64AD322C862769F9AE54FF2446FF03706EBE48)
    
    -   The callback function runs in the UI main thread. To avoid adverse impact on the performance, time-consuming operations related to the UI thread should not run in the callback function.
    -   After the instance calls **OH\_NativeXComponent\_RegisterOnFrameCallback**, it must call **OH\_NativeXComponent\_UnregisterOnFrameCallback** when it no longer needs to control the frame rate, so as to avoid memory leakage and impact on performance and power consumption.
    -   Before API version 18, if the application calls **OH\_NativeXComponent\_RegisterOnFrameCallback** to set the callback function and does not unregister the callback function, the application can receive the expected callback when the XComponent instance exists.
    -   From API version 18 onwards, if the application calls **OH\_NativeXComponent\_RegisterOnFrameCallback** to set the callback function and does not unregister the callback function, the application can receive the expected callback only when the XComponent is on the tree.
    
    void SampleXComponent::RegisterOnFrameCallback(OH\_NativeXComponent \*nativeXComponent)
    {
        // ...
        OH\_NativeXComponent\_RegisterOnFrameCallback(nativeXComponent, TestCallback);
    }
    
    napi\_value SampleXComponent::NapiRegister(napi\_env env, napi\_callback\_info info)
    {
        // ...
            render->RegisterOnFrameCallback(nativeXComponent);
            // ...
    }
    
    napi\_value SampleXComponent::NapiUnregister(napi\_env env, napi\_callback\_info info)
    {
        // ...
            OH\_NativeXComponent\_UnregisterOnFrameCallback(nativeXComponent);
            // ...
    }
    
5.  Register and deregister the callback function for each frame at the TS layer.
    
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
    
      // ...
    }
