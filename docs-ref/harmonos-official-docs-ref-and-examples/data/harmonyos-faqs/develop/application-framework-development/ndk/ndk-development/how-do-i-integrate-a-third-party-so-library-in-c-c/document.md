# How do I integrate a third-party .so library in C/C++?

The development process is as follows:

1.  Build the .so library.
    
    For details, see:
    
    [Building an NDK Project with CMake](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/build-with-ndk-cmake)
    
2.  Integrate the .so library.
    -   Method 1: Directly integrate the library in C/C++.
    -   Method 2: Use dlopen to integrate the library in C/C++.

Sample code:

1.  Build the .so library.
    
    // sub.h 
    extern "C" {
    double sub(double a, double b); 
    }
    
    // sub.cpp 
    #include <iostream> 
    #include "sub.h" 
    double sub(double a, double b) 
    { 
        return a - b; 
    }
    
    \# CMakeLists.txt
    cmake\_minimum\_required(VERSION 3.4.1)
    project(libSub)
    # Compile source code 
    add\_library(nativeSub SHARED sub.cpp)
    
2.  Integrate the .so library.
    -   Directly integrate the library in C/C++.
        
        Place the generated .so library in the **entry/libs** directory of your project, and place the corresponding header file in the **cpp** directory. Modify the **CMakeLists.txt** file and add the .so library to the project for build and reference. Then, include the header file to the native side.
        
        \# CMakeLists.txt
        # the minimum version of CMake.
        cmake\_minimum\_required(VERSION 3.5.0)
        project(ndk1)
        
        set(NATIVERENDER\_ROOT\_PATH ${CMAKE\_CURRENT\_SOURCE\_DIR})
        
        if(DEFINED PACKAGE\_FIND\_FILE)
            include(${PACKAGE\_FIND\_FILE})
        endif()
        
        include\_directories(${NATIVERENDER\_ROOT\_PATH}
                            ${NATIVERENDER\_ROOT\_PATH}/include)
        
        add\_library(entry SHARED napi\_init.cpp)
        target\_link\_libraries(entry PUBLIC libace\_napi.z.so  libhilog\_ndk.z.so)
        target\_link\_libraries(entry PUBLIC ${NATIVERENDER\_ROOT\_PATH}/../../../libs/arm64-v8a/libnativeSub.so)
        
        #include "sub.h"
        
        static napi\_value Sub(napi\_env env, napi\_callback\_info info)
        {
            size\_t requireArgc = 2;
            size\_t argc = 2;
            napi\_value args\[2\] = {nullptr};
            napi\_get\_cb\_info(env, info, &argc, args , nullptr, nullptr);
            napi\_valuetype valuetype0;
            napi\_typeof(env, args\[0\], &valuetype0);
            napi\_valuetype valuetype1;
            napi\_typeof(env, args\[1\], &valuetype1);
            double value0;
            napi\_get\_value\_double(env, args\[0\], &value0);
            double value1;
            napi\_get\_value\_double(env, args\[1\], &value1);
            napi\_value sum;
            napi\_create\_double(env, sub(value0, value1), &sum);
            return sum;
        }
        
    -   Use **dlopen** to integrate the library in C/C++.
        
        Place the .so library in the **entry/libs** directory, pass the sandbox path from ArkTS to native, and call **dlopen** to load the library. Note that the source code of the .so library referenced in this mode must be enclosed in extern "C" {} during compilation. That is, the functions must be compiled in C compilation mode.
        
        import { hilog } from '@kit.PerformanceAnalysisKit';
        import testNapi from 'libentry.so';
        
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
                    let path = this.getUIContext().getHostContext()!.bundleCodeDir; // Get project path
                    hilog.info(0x0000, 'testTag', 'Test NAPI 2 + 3 = %{public}d', testNapi.subSobyDlOpenSo(2, 3, path + '/libs/arm64/libnativeSub.so')); // Transfer parameter path information to the native side
                  })
              }
              .width('100%')
            }
            .height('100%')
          }
        }
        
        #include <dlfcn.h>
        typedef double (\*Sub)(double, double);
        static napi\_value SubSobyDlOpenSo(napi\_env env, napi\_callback\_info info) {
            size\_t requireArgc = 3;
            size\_t argc = 3;
            napi\_value args\[3\] = {nullptr};
            napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);
            double value0;
            napi\_get\_value\_double(env, args\[0\], &value0);    
            double value1;
            napi\_get\_value\_double(env, args\[1\], &value1);
            char\* path = new char\[1024\];
            size\_t size = 1024;
            napi\_get\_value\_string\_utf8(env, args\[2\], path, 255, &size); // Obtain dynamic library path information
            void \*handle = dlopen(path, RTLD\_LAZY);                     // Open the dynamic link library with path as path
            napi\_value result;
            Sub sub\_func = (Sub)dlsym(handle, "sub");                   // Get the function named sub
            napi\_create\_double(env, sub\_func(value0, value1), &result);
            dlclose(handle);                                            // Finally, close the dynamic library
            return result;
        }
