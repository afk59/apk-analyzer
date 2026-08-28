# JSVM-API Development Process

To implement cross-language interaction using JSVM-API, you need to register and load modules based on the JSVM-API mechanism first.

-   ArkTS/JS: Import the .so library and call C++ APIs.
    
-   Native: Implement module registration via a .cpp file. You need to declare the name of the library to register and define the mappings between the native and JS/ArkTS APIs in the callback registered.
    

The following demonstrates how to implement cross-language interaction by implementing **RunJsVm()** in ArkTS/JS code and **RunJsVm()** in native code.

#### Creating a Native C++ Project

For details, see [Creating an NDK Project](../../../creating-an-ndk-project/document.md).

#### Implementing Native APIs

By referring to [Node-API Development Process](../../using-node-api/node-api-development-process/document.md#implementing-native-apis), the following code provides a demo for implementing a native method by following "JSVM-API Development Process".

-   In the **index.d.ts** file, declare the JS methods.
    
    // entry/src/main/cpp/types/libentry/index.d.ts
    export const runTest: () => void;
    
-   Associate **index.d.ts** with **.cpp** in the **oh-package.json5** file.
    
    {
      "name": "libentry.so",
      "types": "./index.d.ts",
      "version": "",
      "description": "Please describe the basic information."
    }
    
-   Set CMake packaging parameters in the **CMakeLists.txt** file.
    
    \# entry/src/main/cpp/CMakeLists.txt
    cmake\_minimum\_required(VERSION 3.4.1)
    project(JSVMDemo)
    
    set(NATIVERENDER\_ROOT\_PATH ${CMAKE\_CURRENT\_SOURCE\_DIR})
    # Set logging information.
    add\_definitions( "-DLOG\_DOMAIN=0xd0d0" )
    add\_definitions( "-DLOG\_TAG=\\"testTag\\"" )
    include\_directories(${NATIVERENDER\_ROOT\_PATH}
                        ${NATIVERENDER\_ROOT\_PATH}/include)
    
    # Add a shared library named entry from the source file hello.cpp.
    add\_library(entry SHARED hello.cpp)
    # Link the entry library with the specified shared libraries.
    target\_link\_libraries(entry PUBLIC libace\_napi.z.so libjsvm.so libhilog\_ndk.z.so)
    
-   Create **entry/src/main/cpp/hello.cpp** and implement **runTest()** on the native side. The code is as follows:
    
    // entry/src/main/cpp/hello.cpp
    #include "napi/native\_api.h"
    #include "hilog/log.h"
    #include "ark\_runtime/jsvm.h"
    
    #define LOG\_DOMAIN 0x3200
    #define LOG\_TAG "APP"
    
    static int g\_aa = 0;
    
    #define CHECK\_RET(theCall)                                                                                             \\
        do {                                                                                                               \\
            JSVM\_Status cond = theCall;                                                                                    \\
            if ((cond) != JSVM\_OK) {                                                                                       \\
                const JSVM\_ExtendedErrorInfo \*info;                                                                        \\
                OH\_JSVM\_GetLastErrorInfo(env, &info);                                                                      \\
                OH\_LOG\_ERROR(LOG\_APP, "jsvm fail file: %{public}s line: %{public}d ret = %{public}d message = %{public}s", \\
                             \_\_FILE\_\_, \_\_LINE\_\_, cond, info != nullptr ? info->errorMessage : "");                         \\
                return -1;                                                                                                 \\
            }                                                                                                              \\
        } while (0)
    
    #define CHECK(theCall)                                                                                                 \\
        do {                                                                                                               \\
            JSVM\_Status cond = theCall;                                                                                    \\
            if ((cond) != JSVM\_OK) {                                                                                       \\
                OH\_LOG\_ERROR(LOG\_APP, "jsvm fail file: %{public}s line: %{public}d ret = %{public}d", \_\_FILE\_\_, \_\_LINE\_\_,  \\
                             cond);                                                                                        \\
                return -1;                                                                                                 \\
            }                                                                                                              \\
        } while (0)
    
    // Call theCall and check whether the return value is JSVM\_OK.
    // If not, call OH\_JSVM\_GetLastErrorInfo to handle the error and return retVal.
    #define JSVM\_CALL\_BASE(env, theCall, retVal)                                                                           \\
        do {                                                                                                               \\
            JSVM\_Status cond = theCall;                                                                                    \\
            if (cond != JSVM\_OK) {                                                                                         \\
                const JSVM\_ExtendedErrorInfo \*info;                                                                        \\
                OH\_JSVM\_GetLastErrorInfo(env, &info);                                                                      \\
                OH\_LOG\_ERROR(LOG\_APP, "jsvm fail file: %{public}s line: %{public}d ret = %{public}d message = %{public}s", \\
                             \_\_FILE\_\_, \_\_LINE\_\_, cond, info != nullptr ? info->errorMessage : "");                         \\
                return retVal;                                                                                             \\
            }                                                                                                              \\
        } while (0)
    
    // Simplified version of JSVM\_CALL\_BASE, which returns nullptr.
    #define JSVM\_CALL(theCall) JSVM\_CALL\_BASE(env, theCall, nullptr)
    
    // Define OH\_JSVM\_StrictEquals.
    static JSVM\_Value IsStrictEquals(JSVM\_Env env, JSVM\_CallbackInfo info) {
        // Obtain the two parameters passed from JS.
        size\_t argc = 2;
        JSVM\_Value args\[2\] = {nullptr};
        JSVM\_CALL(OH\_JSVM\_GetCbInfo(env, info, &argc, args, nullptr, nullptr));
        // Call OH\_JSVM\_StrictEquals to check whether two given JS values are strictly equal.
        bool result = false;
        JSVM\_Status status = OH\_JSVM\_StrictEquals(env, args\[0\], args\[1\], &result);
        if (status != JSVM\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "JSVM OH\_JSVM\_StrictEquals: failed");
        } else {
            OH\_LOG\_INFO(LOG\_APP, "JSVM OH\_JSVM\_StrictEquals: success: %{public}d", result);
        }
        JSVM\_Value isStrictEqual;
        JSVM\_CALL(OH\_JSVM\_GetBoolean(env, result, &isStrictEqual));
        return isStrictEqual;
    }
    // Register the IsStrictEquals callback.
    static JSVM\_CallbackStruct param\[\] = {
        {.data = nullptr, .callback = IsStrictEquals},
    };
    static JSVM\_CallbackStruct \*method = param;
    // Set a property descriptor named isStrictEquals and associate it with a callback. This allows the isStrictEquals callback to be called from JS.
    static JSVM\_PropertyDescriptor descriptor\[\] = {
        {"isStrictEquals", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
    };
    // Call the C++ code from JS.
    const char \*srcCallNative = R"JS(    let data = '123';
        let value = 123;
        isStrictEquals(data,value);)JS";
    
    static int32\_t TestJSVM() {
        JSVM\_InitOptions initOptions = {0};
        JSVM\_VM vm;
        JSVM\_Env env = nullptr;
        JSVM\_VMScope vmScope;
        JSVM\_EnvScope envScope;
        JSVM\_HandleScope handleScope;
        JSVM\_Value result;
        // Initialize the JSVM instance.
        if (g\_aa == 0) {
            g\_aa++;
           CHECK(OH\_JSVM\_Init(&initOptions));
        }
        // Create a JSVM environment.
        CHECK(OH\_JSVM\_CreateVM(nullptr, &vm));
        CHECK(OH\_JSVM\_CreateEnv(vm, sizeof(descriptor) / sizeof(descriptor\[0\]), descriptor, &env));
        CHECK(OH\_JSVM\_OpenVMScope(vm, &vmScope));
        CHECK\_RET(OH\_JSVM\_OpenEnvScope(env, &envScope));
        CHECK\_RET(OH\_JSVM\_OpenHandleScope(env, &handleScope));
    
        // Call the test function through the script.
        JSVM\_Script script;
        JSVM\_Value jsSrc;
        CHECK\_RET(OH\_JSVM\_CreateStringUtf8(env, srcCallNative, JSVM\_AUTO\_LENGTH, &jsSrc));
        CHECK\_RET(OH\_JSVM\_CompileScript(env, jsSrc, nullptr, 0, true, nullptr, &script));
        CHECK\_RET(OH\_JSVM\_RunScript(env, script, &result));
    
        // Destroy the JSVM environment.
        CHECK\_RET(OH\_JSVM\_CloseHandleScope(env, handleScope));
        CHECK\_RET(OH\_JSVM\_CloseEnvScope(env, envScope));
        CHECK(OH\_JSVM\_CloseVMScope(vm, vmScope));
        CHECK(OH\_JSVM\_DestroyEnv(env));
        CHECK(OH\_JSVM\_DestroyVM(vm));
        return 0;
    }
    
    static napi\_value RunTest(napi\_env env, napi\_callback\_info info)
    {
        TestJSVM();
        return nullptr;
    }
    
    // Initialize the module.
    EXTERN\_C\_START
    static napi\_value Init(napi\_env env, napi\_value exports) {
        // Implement the mappings between the ArkTS and C++ APIs.
        napi\_property\_descriptor desc\[\] = {
          {"runTest", nullptr, RunTest, nullptr, nullptr, nullptr, napi\_default, nullptr}
        };
        // Register the native RunJsVm function with the JS exports object, making the native function available to JS.
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
    

#### Calling C/C++ APIs in ArkTS

// Import the native APIs.
import napitest from 'libentry.so';

@Entry
@Component
struct Index {
  @State message: string = 'Hello World';

  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
          .onClick(() => {
            // runtest
            napitest.runTest();
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}

Expected result:

JSVM OH\_JSVM\_StrictEquals: success: 0
