# Creating an ArkTS Runtime Environment Using Node-API

#### When to Use

After creating a thread using **pthread\_create**, you can use **napi\_create\_ark\_runtime** to create an ArkTS runtime environment and load the ArkTS module in the runtime environment. To destroy an ArkTS runtime environment that is not required, use **napi\_destroy\_ark\_runtime**.

#### Constraints

A maximum of 64 runtime environments can be created for a process.

#### Example

1.  Declare the APIs, configure compile settings, and register the module.
    
    **Declare the APIs.**
    
    // index.d.ts
    export const createArkRuntime: () => object;
    
    **Configure compile settings.**
    
    // CMakeLists.txt
    # the minimum version of CMake.
    cmake\_minimum\_required(VERSION 3.4.1)
    project(MyApplication)
    
    set(NATIVERENDER\_ROOT\_PATH ${CMAKE\_CURRENT\_SOURCE\_DIR})
    
    include\_directories(${NATIVERENDER\_ROOT\_PATH}
                        ${NATIVERENDER\_ROOT\_PATH}/include)
    add\_library(entry SHARED create\_ark\_runtime.cpp)
    target\_link\_libraries(entry PUBLIC libace\_napi.z.so libhilog\_ndk.z.so)
    
    Configure the **build-profile.json5** file of the current module as follows:
    
    {
        "buildOption" : {
            "arkOptions" : {
                "runtimeOnly" : {
                    "sources": \[
                        "./src/main/ets/pages/ObjectUtils.ets"
                    \]
                }
            }
        }
    }
    
    **Register modules.**
    
    // create\_ark\_runtime.cpp
    EXTERN\_C\_START
    static napi\_value Init(napi\_env env, napi\_value exports)
    {
        napi\_property\_descriptor desc\[\] = {
            { "createArkRuntime", nullptr, CreateArkRuntime, nullptr, nullptr, nullptr, napi\_default, nullptr }
        };
        napi\_define\_properties(env, exports, sizeof(desc) / sizeof(desc\[0\]), desc);
        return exports;
    }
    EXTERN\_C\_END
    
    static napi\_module nativeModule = {
        .nm\_version = 1,
        .nm\_flags = 0,
        .nm\_filename = nullptr,
        .nm\_register\_func = Init,
        .nm\_modname = "entry",
        .nm\_priv = nullptr,
        .reserved = { 0 },
    };
    
    extern "C" \_\_attribute\_\_((constructor)) void RegisterQueueWorkModule()
    {
        napi\_module\_register(&nativeModule);
    }
    
2.  Create a thread and an ArkTS runtime environment, and load the module. For details about how to load a custom module, see [Loading a Module Using Node-API](../loading-a-module-using-node-api/document.md).
    
    // create\_ark\_runtime.cpp
    #include <pthread.h>
    #include "napi/native\_api.h"
    
    static void \*CreateArkRuntimeFunc(void \*arg)
    {
        // 1. Create the ArkTS runtime environment.
        napi\_env env;
        napi\_status ret = napi\_create\_ark\_runtime(&env);
        if (ret != napi\_ok) {
            return nullptr;
        }
    
        // 2. Load custom modules.
        napi\_value objUtils;
        ret = napi\_load\_module\_with\_info(env, "entry/src/main/ets/pages/ObjectUtils", "com.example.myapplication/entry", &objUtils);
        if (ret != napi\_ok) {
            return nullptr;
        }
    
        // 3. Use the logger in ArkTS.
        napi\_value logger;
        ret = napi\_get\_named\_property(env, objUtils, "Logger", &logger);
        if (ret != napi\_ok) {
            return nullptr;
        }
        ret = napi\_call\_function(env, objUtils, logger, 0, nullptr, nullptr);
    
        // 4. Destroy the ArkTS runtime environment.
        ret = napi\_destroy\_ark\_runtime(&env);
        return nullptr;
    }
    
    static napi\_value CreateArkRuntime(napi\_env env, napi\_callback\_info info)
    {
        pthread\_t tid;
        pthread\_create(&tid, nullptr, CreateArkRuntimeFunc, nullptr);
        pthread\_join(tid, nullptr);
        return nullptr;
    }
    
3.  Write the ArkTS code.
    
    // ObjectUtils.ets
    export function Logger() {
        console.info("print log");
    }
    
    // Call ArkTS APIs.
    import testNapi from 'libentry.so';
    
    testNapi.createArkRuntime();
