# Node-API Development Process

To implement cross-language interaction using Node-API, you need to register and load modules based on the Node-API mechanism first.

-   ArkTS/JS: Call C++ methods by importing the required .so library.
    
-   Native: Implement module registration via a .cpp file. You need to declare the name of the library to register and define the mappings between the native and JS/ArkTS APIs in the callbacks registered.
    

The following demonstrates how to implement cross-language interaction by calling **callNative()** in ArkTS/JS code and implementing **CallNative()** in native code.

#### Creating a Native C++ Project

-   In DevEco Studio, choose **New** > **Create Project**, select the **Native C++** template, click **Next**, select the API version, set the project name, and click **Finish**.
    
-   The main code of the project created consists of two parts: **cpp** and **ets**. For details about the project structure, see [Project Directory Structure](https://developer.huawei.com/consumer/en/doc/harmonyos-guides-V5/ide-project-structure-V5).
    

#### Implementing Native APIs

-   Set module registration information.
    
    When a native module is imported in ArkTS, the .so file will be loaded. During the loading process, the **napi\_module\_register** method is called to register the module with the system and call the module initialization function.
    
    napi\_module has two key properties: **.nm\_register\_func** and **.nm\_modname**. **.nm\_register\_func** defines the module initialization function, and **.nm\_modname** defines the module name, that is, the name of the .so file imported by ArkTS.
    
    // entry/src/main/cpp/napi\_init.cpp
    
    // Information about the module. Record information such as the Init() function and module name.
    static napi\_module demoModule = {
        .nm\_version = 1,
        .nm\_flags = 0,
        .nm\_filename = nullptr,
        .nm\_register\_func = Init,
        .nm\_modname = "entry",
        .nm\_priv = ((void\*)0),
        .reserved = {0},
    };
    
    // When the .so file is loaded, this function is automatically called to register the demoModule module with the system.
    extern "C" \_\_attribute\_\_((constructor)) void RegisterDemoModule() {
        napi\_module\_register(&demoModule);
    }
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/Dp0mmfQKS3aYkTw15yxW1w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062130Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F0FC859A0BCDECA36807EACC7F651DBADED6B67D44C884951BE1DC27C2010474)

You do not need to copy the above code as it is pre-configured in the **napi\_init.cpp** file when the native C++ project is created.

-   Initialize the module.
    
    Implement the mappings between the ArkTS and C++ APIs.
    
    // entry/src/main/cpp/napi\_init.cpp
    EXTERN\_C\_START
    // Initialize the module.
    static napi\_value Init(napi\_env env, napi\_value exports) {
        // Implement the mappings between the ArkTS and C++ APIs.
        napi\_property\_descriptor desc\[\] = {
            // You only need to copy the following two lines of code. Init has been configured in napi\_init.cpp when the native C++ project is created.
            {"callNative", nullptr, CallNative, nullptr, nullptr, nullptr, napi\_default, nullptr},
            {"nativeCallArkTS", nullptr, NativeCallArkTS, nullptr, nullptr, nullptr, napi\_default, nullptr}
        };
        // Hook the CallNative and NativeCallArkTS APIs to the exports object.
        napi\_define\_properties(env, exports, sizeof(desc) / sizeof(desc\[0\]), desc);
        return exports;
    }
    EXTERN\_C\_END
    
-   Add JS APIs in the index.d.ts file.
    
    // entry/src/main/cpp/types/libentry/index.d.ts
    export const callNative: (a: number, b: number) => number;
    export const nativeCallArkTS: (cb: (a: number) => number) => number;
    
-   Associate **index.d.ts** with **.cpp** in the **oh-package.json5** file.
    
    // entry/src/main/cpp/types/libentry/oh-package.json5
    {
      "name": "libentry.so",
      "types": "./index.d.ts",
      "version": "",
      "description": "Please describe the basic information."
    }
    
-   Set CMake packaging parameters in the **CMakeLists.txt** file.
    
    \# entry/src/main/cpp/CMakeLists.txt
    cmake\_minimum\_required(VERSION 3.4.1)
    project(MyApplication2)
    
    set(NATIVERENDER\_ROOT\_PATH ${CMAKE\_CURRENT\_SOURCE\_DIR})
    
    include\_directories(${NATIVERENDER\_ROOT\_PATH}
                        ${NATIVERENDER\_ROOT\_PATH}/include)
    
    # Add a library named entry.
    add\_library(entry SHARED napi\_init.cpp)
    # Build the library to be linked to this executable.
    target\_link\_libraries(entry PUBLIC libace\_napi.z.so)
    
-   Implement **CallNative** and **NativeCallArkTS**. The code is as follows:
    
    // entry/src/main/cpp/napi\_init.cpp
    static napi\_value CallNative(napi\_env env, napi\_callback\_info info)
    {
        size\_t argc = 2;
        // Declare the parameter array.
        napi\_value args\[2\] = {nullptr};
    
        // Obtain input parameters and put them into the parameter array in sequence.
        napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);
    
        // Obtain the parameters in sequence.
        double value0;
        napi\_get\_value\_double(env, args\[0\], &value0);
        double value1;
        napi\_get\_value\_double(env, args\[1\], &value1);
    
        // Return the sum of the two numbers.
        napi\_value sum;
        napi\_create\_double(env, value0 + value1, &sum);
        return sum;
    }
    
    static napi\_value NativeCallArkTS(napi\_env env, napi\_callback\_info info)
    {
        size\_t argc = 1;
        // Declare the parameter array.
        napi\_value args\[1\] = {nullptr};
    
        // Obtain input parameters and put them into the parameter array in sequence.
        napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);
    
        // Create an int() as the input parameter of ArkTS.
        napi\_value argv = nullptr;
        napi\_create\_int32(env, 2, &argv);
    
        // Invoke the callback that is passed in, and return the result.
        napi\_value result = nullptr;
        napi\_call\_function(env, nullptr, args\[0\], 1, &argv, &result);
        return result;
    }
    

#### Calling C/C++ APIs on ArkTS

On ArkTS, import the .so file that contains the processing logic on the native side to use C/C++ APIs.

// entry/src/main/ets/pages/Index.ets
// Import the native APIs.
import nativeModule from 'libentry.so'

@Entry
@Component
struct Index {
  @State message: string = 'Test Node-API callNative result: ';
  @State message2: string = 'Test Node-API nativeCallArkTS result: ';
  build() {
    Row() {
      Column() {
        // Pressing the first button calls callNative(), which uses CallNative() in the native code to add the two numbers.
        Text(this.message)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
          .onClick(() => {
            this.message += nativeModule.callNative(2, 3);
            })
        // Pressing the second button calls nativeCallArkTS, which corresponds to NativeCallArkTS in the native code. The ArkTS function is called on the native side.
        Text(this.message2)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
          .onClick(() => {
            this.message2 += nativeModule.nativeCallArkTS((a: number)=> {
                return a \* 2;
            });
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}

#### Node-API Constraints

## Naming Rules of .so Files

The case of the module name to import must be the same as that registered. For example, if the module name is **entry**, the **.so** file name must be **libentry.so**, and the **nm\_modname** field in **napi\_module** must be **entry**. When importing the module in ArkTS, use \*\*import \*\*xxx **from 'libentry.so'**.

## Registration

-   To prevent conflicts with symbols in other .so files, add **static** to the function (for example, the **Init** function) corresponding to **nm\_register\_func**.
    
-   The name of the module registration entry, that is, the function modified by ****attribute**((constructor))** must be unique. For example, the **RegisterDemoModule** function in this document.
    

## Multithread Processing

Each engine instance corresponds to an ArkTS thread. The objects of an instance cannot be operated across threads. Otherwise, the application crashes. Observe the following rules:

-   The Node-API can be used only by ArkTS threads.
-   The input parameter **env** of a native API can be bound to an ArkTS thread and can be used only by the thread that creates the env.
-   Data created using Node-APIs must be released before **env** is completely destroyed. Otherwise, memory leaks may be caused. In addition, accessing or using the data after **napi\_env** is destroyed may cause the process to crash.

## Debugging Device Selection

You are advised to use a real device for code debugging. If no real device is available or you do not have the permission to use a real device, use an emulator for debugging. For details about the problems that may occur during emulator debugging, see [Bundle Manager](../../../../system/debugging-tools/debugging-commands/bundle-manager/document.md#error-codes).

The previewer is mainly used to debug UI components. Do not use it for function debugging. Otherwise, the following error message may be displayed:

-   TypeError: undefined is not callable

Maintenance and testing measures have been added to address common errors. For details, see [Analyzing Exceptions and Crashes Using Node-API](../typical-node-api-use-cases/analyzing-error-logs-and-crashes-triggered-by-using-node-api/document.md).
