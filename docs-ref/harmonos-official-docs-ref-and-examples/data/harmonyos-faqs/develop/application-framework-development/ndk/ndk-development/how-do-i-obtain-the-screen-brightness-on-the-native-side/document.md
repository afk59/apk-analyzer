# How do I obtain the screen brightness on the native side?

**Question**

How do I obtain the screen brightness on the native side? Please give me an example.

**Answer**

You can use **napi\_load\_module** to load the module used to obtain the screen brightness and use **get\_value** to obtain the screen brightness.

Sample code:

1.  Pass the module name from ArkTS.
    
    // Screenbrightness/src/main/ets/pages/Index.ets
    import testNapi from 'libscreenbrightness.so';
    
    
    @Entry
    @Component
    struct Index {
      @State message: string = 'Get Screen Brightness';
    
    
      build() {
        Row() {
          Column() {
            Text(this.message)
              .fontSize(50)
              .fontWeight(FontWeight.Bold)
              .onClick(() => {
                testNapi.napiLoadModule("@system.brightness");
              })
          }
          .width('100%')
        }
        .height('100%')
      }
    }
    
2.  Obtain the screen brightness on the native side.
    
    // Screenbrightness/src/main/cpp/napi\_init.cpp
    #include "hilog/log.h"
    #include "napi/native\_api.h"
    #include <string>
    
    
    #define LOG\_TAG "Pure"
    
    
    static napi\_value Success(napi\_env env, napi\_callback\_info info) {
        size\_t argc = 1;
        napi\_value args\[1\] = {nullptr};
        napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);
        napi\_value obj = args\[0\];
        napi\_value key;
        napi\_value rv;
        std::string x = "value";
        napi\_create\_string\_utf8(env, x.c\_str(), 5, &key);
        napi\_get\_property(env, obj, key, &rv);
        uint32\_t result;
        napi\_get\_value\_uint32(env, rv, &result);
        OH\_LOG\_INFO(LOG\_APP, "napi get brightness %{public}d", result);
        return nullptr;
    };
    static napi\_value Fail(napi\_env env, napi\_callback\_info info) { return nullptr; };
    static napi\_value Complete(napi\_env env, napi\_callback\_info info) { return nullptr; };
    static napi\_value NapiLoadModule(napi\_env env, napi\_callback\_info info) {
        napi\_value result;
        size\_t argc = 1;
        napi\_value args\[1\] = {nullptr};
        napi\_status get = napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);
        char path\[64\] = {0};
        size\_t typeLen = 0;
        napi\_get\_value\_string\_utf8(env, args\[0\], path, sizeof(path), &typeLen);
        napi\_status status = napi\_load\_module(env, path, &result);
        if (status != napi\_ok) {
            OH\_LOG\_ERROR(LOG\_APP, "napi\_load\_module failed");
            return nullptr;
        }
        napi\_value outputObject;
        napi\_get\_named\_property(env, result, "getValue", &outputObject);
        napi\_value arg;
        napi\_create\_object(env, &arg);
        napi\_property\_descriptor desc\[\] = {
            {"success", nullptr, Success, nullptr, nullptr, nullptr, napi\_default, nullptr},
            {"fail", nullptr, Fail, nullptr, nullptr, nullptr, napi\_default, nullptr},
            {"complete", nullptr, Complete, nullptr, nullptr, nullptr, napi\_default, nullptr}};
        napi\_define\_properties(env, arg, sizeof(desc) / sizeof(desc\[0\]), desc);
        napi\_call\_function(env, result, outputObject, 1, &arg, nullptr);
        return result;
    };
    EXTERN\_C\_START
    static napi\_value Init(napi\_env env, napi\_value exports) {
        napi\_property\_descriptor desc\[\] = {
            {"napiLoadModule", nullptr, NapiLoadModule, nullptr, nullptr, nullptr, napi\_default, nullptr},
        };
        napi\_define\_properties(env, exports, sizeof(desc) / sizeof(desc\[0\]), desc);
        return exports;
    }
    EXTERN\_C\_END
    
    
    static napi\_module demoModule = {
        .nm\_version = 1,
        .nm\_flags = 0,
        .nm\_filename = nullptr,
        .nm\_register\_func = Init,
        .nm\_modname = "screenbrightness",
        .nm\_priv = ((void \*)0),
        .reserved = {0},
    };
    extern "C" \_\_attribute\_\_((constructor)) void RegisterScreenBrightnessModule(void) { napi\_module\_register(&demoModule); }
    
3.  Declare the native APIs mapped to ArkTS in the **Index.d.ts** file.
    
    // Screenbrightness/src/main/cpp/types/libscreenbrightness/Index.d.ts
    export const napiLoadModule: (a: string) => object;
    
4.  Add the log dependencies to the **CMakeLists** file.
    
    \# Screenbrightness/src/main/cpp/CMakeLists.txt
    target\_link\_libraries(screenbrightness PUBLIC libace\_napi.z.so libhilog\_ndk.z.so)
