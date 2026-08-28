# What should I do if multiple SO libraries depend on each other?

**Symptom**

Module A has a.so, and module B has b.so. The a.so file calls the functions of the b.so file, and the b.so file also calls the functions of the a.so file. The compilation fails no matter which .so file is compiled first.

**Solution**

Use **dlopen** and **dlsym** to decouple the compilation dependencies between the SO libraries and convert implicit dependencies to explicit dependencies. The sample code is as follows:

1.  Modify the code and **CMakeLists.txt** file, and use **dlopen()** on the native side to generate **liba.so** and **libb.so**. The generated .so files are in the **build/default/intermediates/cmake/default/obj** directory.
    
    (Note that the function must be enclosed in extern "C" {}. Otherwise, the corresponding function cannot be identified, causing a compilation error.)
    
    // a.cpp
    extern "C" {     // Be sure to enclose it with extern 'C' {}
    #include "a.h"
    #include <dlfcn.h>
    #include "stdio.h"
    typedef int (\*FUNC\_SUB)(int, int);
    int add(int a, int b) { return a + b; }
    int getb(char \*path, int a, int b) {       // Path:The sandbox path for passing So files from ArkTS side (note that the path should be passed from ArkTS side, otherwise it may not be found, and the specific code will be listed later)
        void \*handle = dlopen(path, RTLD\_LAZY);  // Open the dynamic link library with path as path
        if (!handle) {
            return 0;
        }
        FUNC\_SUB sub\_func = (FUNC\_SUB)dlsym(handle, "sub"); // Get the function named sub
        int res = sub\_func(a, b);                           // caller function
        dlclose(handle);                                    // Close dynamic link library
        return res;
    }
    }
    
    // a.h
    extern "C" {
    #ifndef DemoSO\_a\_H
    #define DemoSO\_a\_H
    int add(int a, int b);
    int getb(char \*path, int a, int b);
    #endif // DemoSO\_a\_H
    }
    
    // b.cpp
    extern "C" {     // Be sure to enclose it with extern 'C' {}
    #include "b.h"
    #include <dlfcn.h>
    #include "stdio.h"
    typedef int (\*FUNC\_ADD)(int, int);
    int sub(int a, int b) { return a - b; }
    int geta(char \*path, int a, int b) {    // Path: The sandbox path for passing So files from ArkTS side (note that the path should be passed from ArkTS side, otherwise it may not be found, and the specific code will be listed later)
        void \*handle = dlopen(path, RTLD\_LAZY);    // Open the dynamic link library with path as path
        if (!handle) {
            return 0;
        }
        FUNC\_ADD add\_func = (FUNC\_ADD)dlsym(handle, "add");      // Get the function named sub
        int res = add\_func(a, b);                                // caller function
        dlclose(handle);                                         // Close dynamic link library
        return res;
    }
    }
    
    // b.h
    extern "C" {
    #ifndef DemoSO\_b\_H
    #define DemoSO\_b\_H
    int sub(int a, int b);
    int geta(char \*path, int a, int b);
    #endif // DemoSO\_b\_H
    }
    
    \# CMakeLists.txt
    cmake\_minimum\_required(VERSION 3.4.1)
    project(liba)
    # Compile library liba.so
    add\_library(a SHARED a.cpp)
    target\_link\_libraries(a PUBLIC libace\_napi.z.so libhilog\_ndk.z.so)
    project(libb)
    # Compile library libb.so
    add\_library(b SHARED b.cpp)
    target\_link\_libraries(b PUBLIC libace\_napi.z.so libhilog\_ndk.z.so)
    
2.  Move the generated .so files (relative path: **build/default/intermediates/cmake/default/obj**) to the **libs** directory.
    
    The directory structure after the move is as follows:
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/q7f1XsmkQTmRlnRpAzIRhQ/en-us_image_0000002194158924.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062546Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F4E26746AB37457A286FC7887968E39794E56FE40093E943E0820AA412547B99 "Click to enlarge")
    
3.  Modify the **CMakeLists.txt** file and import the generated .so files to the project for compilation.
    
    \# CMakeLists.txt
    cmake\_minimum\_required(VERSION 3.4.1)
    project(DemoSO)
    set(NATIVERENDER\_ROOT\_PATH ${CMAKE\_CURRENT\_SOURCE\_DIR})
    include\_directories(${NATIVERENDER\_ROOT\_PATH}
                        ${NATIVERENDER\_ROOT\_PATH}/include)
    # Add libdemoso. so file
    add\_library(demoso SHARED hello.cpp)
    # Add dependency libraries liba.so and libb.so. Please note to include the path, otherwise the corresponding SO library cannot be found
    target\_link\_libraries(demoso PUBLIC libace\_napi.z.so ${CMAKE\_CURRENT\_SOURCE\_DIR}/../../../libs/${OHOS\_ARCH}/liba.so ${CMAKE\_CURRENT\_SOURCE\_DIR}/../../../libs/${OHOS\_ARCH}/libb.so)
    
    // index.ets
    import testNapi from 'libdemoso.so';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    
    @Entry
    @Component
    struct Index {
      @State message: string = 'Hello World';
      private path: string = '';
    
      build() {
        Row() {
          Column() {
            Text(this.message)
              .fontSize(50)
              .fontWeight(FontWeight.Bold)
              .onClick(() => {
                this.path = this.getUIContext().getHostContext()!.bundleCodeDir;   // get path
                hilog.info(0x0000, 'testTag', 'Test NAPI 5 + 3 = %{public}d', testNapi.add(5, 3, this.path + '/libs/arm64/liba.so'));  // Call the native side function
                hilog.info(0x0000, 'testTag', 'Test NAPI 5 - 3 = %{public}d', testNapi.sub(5, 3, this.path + '/libs/arm64/libb.so'));
              })
          }
          .width('100%')
        }
        .height('100%')
      }
    }
    
    // index.d.ts
    export const add: (a: number, b: number, path: string) => number;
    export const sub: (a: number, b: number, path: string) => number;
    
    // hello.cpp
    #include "a.h"
    #include "b.h"
    #include "napi/native\_api.h"
    
    static napi\_value Add(napi\_env env, napi\_callback\_info info) {
        size\_t requireArgc = 3;
        size\_t argc = 3;
        napi\_value args\[3\] = {nullptr};
        napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);
        napi\_valuetype valuetype0;
        napi\_typeof(env, args\[0\], &valuetype0);
        napi\_valuetype valuetype1;
        napi\_typeof(env, args\[1\], &valuetype1);
        napi\_valuetype valuetype2;
        napi\_typeof(env, args\[2\], &valuetype2);
        int value0;
        napi\_get\_value\_int32(env, args\[0\], &value0);
        int value1;
        napi\_get\_value\_int32(env, args\[1\], &value1);
        char path\[255\];
        size\_t size = 255;
        napi\_get\_value\_string\_utf8(env, args\[2\], path, 255, &size);
        int res = geta(path, value0, value1);                    // Call the function and pass the sandbox path
        napi\_value sum;
        napi\_create\_int32(env, res, &sum);
        return sum;
    }
    static napi\_value Sub(napi\_env env, napi\_callback\_info info) {
        size\_t requireArgc = 3;
        size\_t argc = 3;
        napi\_value args\[3\] = {nullptr};
        napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);
        napi\_valuetype valuetype0;
        napi\_typeof(env, args\[0\], &valuetype0);
        napi\_valuetype valuetype1;
        napi\_typeof(env, args\[1\], &valuetype1);
        napi\_valuetype valuetype2;
        napi\_typeof(env, args\[2\], &valuetype2);
        int value0;
        napi\_get\_value\_int32(env, args\[0\], &value0);
        int value1;
        napi\_get\_value\_int32(env, args\[1\], &value1);
        char path\[255\];
        size\_t size = 255;
        napi\_get\_value\_string\_utf8(env, args\[2\], path, 255, &size);
        int res = getb(path, value0, value1);                 // Call the function and pass the sandbox path
        napi\_value sum;
        napi\_create\_int32(env, res, &sum);
        return sum;
    }
    EXTERN\_C\_START
    static napi\_value Init(napi\_env env, napi\_value exports) {
        napi\_property\_descriptor desc\[\] = {{"add", nullptr, Add, nullptr, nullptr, nullptr, napi\_default, nullptr},
                                           {"sub", nullptr, Sub, nullptr, nullptr, nullptr, napi\_default, nullptr}};
        napi\_define\_properties(env, exports, sizeof(desc) / sizeof(desc\[0\]), desc);
        return exports;
    }
    EXTERN\_C\_END
    
    static napi\_module demoModule = {
        .nm\_version = 1,
        .nm\_flags = 0,
        .nm\_filename = nullptr,
        .nm\_register\_func = Init,
        .nm\_modname = "demoso",
        .nm\_priv = ((void \*)0),
        .reserved = {0},
    };
    extern "C" \_\_attribute\_\_((constructor)) void RegisterDemosoModule(void) { napi\_module\_register(&demoModule); }
