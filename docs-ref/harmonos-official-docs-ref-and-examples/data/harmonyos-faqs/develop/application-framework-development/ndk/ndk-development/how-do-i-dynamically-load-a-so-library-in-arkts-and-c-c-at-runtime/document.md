# How do I dynamically load a .so library in ArkTS and C/C++ at runtime?

**Answer**

1\. Use dynamic import to load a .so library in ArkTS.

2\. Use **dlopen** to dynamically load a .so library in C/C++.

Sample code:

1\. Use dynamic import to load a .so library in ArkTS. Add an asynchronous function with **let testNapi = await import ("libentry.so")** to dynamically load the .so library.

import { hilog } from '@kit.PerformanceAnalysisKit';
// import testNapi from 'libentry.so';

@Entry
@Component
struct LoadSoLibrary {
  @State message: string = 'Hello World';

  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
          .onClick(async() => {
            let testNapi = await import("libentry.so")            // Load so library
            hilog.info(0x0000, 'testTag', 'Test NAPI 2 + 3 = %{public}d', testNapi.default.add(2, 3));   // Call library functions by default
            // hilog.info(0x0000, 'testTag', 'Test NAPI 2 + 3 = %{public}d', testNapi.add(2, 3));
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}

2\. Use **dlopen** to dynamically load a .so library in C/C++.

For example, to call the **add()** function in **liba.so**, do as follows:

-   Save the **liba.so** file to the **libs/arm64-v8a/** directory.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/Au8U8Z4ERy65Yfm_eLylEA/en-us_image_0000002229603757.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062545Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=43E66458E770B720AFA19E10CD46EDFD1253DA307C5233341DCB19CC19A1A8DF "Click to enlarge")
    
-   Pass the .so library path from ArkTS to native.
    
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
                let path = this.getUIContext().getHostContext()!.bundleCodeDir;     // Get project path
                hilog.info(0x0000, 'testTag', 'Test NAPI 2 + 3 = %{public}d', testNapi.addByLibPath(2, 3, path + '/libs/arm64/liba.so'));   // Transfer parameter path information to the native side
              })
          }
          .width('100%')
        }
        .height('100%')
      }
    }
    
-   Use **dlopen** to dynamically load the .so library on the native side.
    
    #include "napi/native\_api.h" 
    #include <dlfcn.h> 
    typedef double (\*FUNC\_ADD)(int, int); 
    static napi\_value AddByLibPath(napi\_env env, napi\_callback\_info info) { 
        size\_t requireArgc = 3; 
        size\_t argc = 3; 
        napi\_value args\[3\] = {nullptr}; 
        napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr); 
        double value0; 
        napi\_get\_value\_double(env, args\[0\], &value0); 
        double value1; 
        napi\_get\_value\_double(env, args\[1\], &value1); 
        char path\[255\]; 
        size\_t size = 255; 
        napi\_get\_value\_string\_utf8(env, args\[2\], path, 255, &size); // Obtain dynamic library path information 
        void \*handle = dlopen(path, RTLD\_LAZY);                     // Open a dynamic link library, The path is "path".  
        dlerror(); 
        FUNC\_ADD add\_func = (FUNC\_ADD)dlsym(handle, "add"); // Retrieve the function named "add" 
        if (dlerror()) { 
            return nullptr; 
        } 
        double res = add\_func(value0, value1);              // Call add and pass the parameter information 
        dlclose(handle);                                    // Close the dynamic library 
        napi\_value sum; 
        napi\_create\_double(env, res, &sum); 
        return sum; 
    } 
    // ...
