# About This Kit

The Native Development Kit (NDK) is a toolset that allows you to use C and C++ code with HarmonyOS. As a subset of HarmonyOS SDK, it provides native APIs, compile scripts, and compile toolchain to help you implement key application features using C or C++. The NDK covers only some basic underlying capabilities of HarmonyOS, such as the C runtime libc, graphics library, window system, multimedia, compression library, and Node-API that bridges ArkTS/JS and C code. It does not provide complete capabilities of ArkTS/JS APIs.

You can use Node-API in the NDK to access, create, and operate JS objects, and use native dynamic libraries in JS objects.

#### Use Scenarios

The NDK can be helpful for the cases in which you need to:

-   Increase performance in compute-intensive cases, such as games or physical simulations.
    
-   Reuse existing C or C++ libraries.
    
-   Customize a library based on CPU features, for example, performing Neon acceleration.
    

You are not advised to use the NDK to develop the following:

-   C or C++ applications
    
-   Applications that can run on a wide variety of HarmonyOS devices
    

#### NDK Basics

Before getting started, familiarity with the following basics is helpful.

## Preparatory Knowledge

-   Linux C programming knowledge
    
    The kernel and libc are extended based on standards such as POSIX. Mastering basic Linux C programming knowledge can help you better understand HarmonyOS development with the NDK.
    
-   CMake
    
    CMake is the default build system of HarmonyOS. For details about how to use CMake, see [CMake Tutorial](https://cmake.org/cmake/help/v3.16/guide/tutorial/).
    
-   Node addons
    
    ArkTS uses Node-API as the cross-language invoking interface. Familiarity with the basic [node addons](https://nodejs.org/api/addons.html) helps you better understand how to use Node-API in the NDK.
    
-   Clang/LLVM
    
    Basic knowledge of the Clang or LLVM compiler helps you compile better native dynamic libraries.
    
-   **[Node-API](../code-development/using-node-api/node-api-overview/document.md)**
    
    Node-API, formerly called NAPI, is a set of APIs provided for you to use C and C++ code with HarmonyOS ArkTS/JS. Node-API is an extension of Node-API in Node.js but is not fully compatible.
    

## NDK Directory Structure

For details about how to obtain the NDK, see [NDK Development Tools Directory](../building-an-ndk-project/building-an-ndk-project-with-cmake/document.md#obtain-the-ndk-development-package).

-   **build** directory: stores the predefined toolchain script file [ohos.toolchain.cmake](../building-an-ndk-project/overview/document.md#introduction-to-ohostoolchaincmake).
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/QeFRt_s8REC6kdoO3mlPuQ/en-us_image_0000002537765282.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062129Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E56B13FC910B2E2CE34570FDDA63B81025327965BE212627DAC5350883DB6A1B)
    
    During compilation, CMake locates the file through **CMAKE\_TOOLCHAIN\_FILE** and reads the default values in this file, such as the compiler architecture and C++ library link mode.
    
-   **build-tools** folder: contains the build tools provided by the NDK.
    
    \# Check the CMake version.
    cmake -version
    # The version information is displayed.
    cmake version 3.16.5
    CMake suite maintained and supported by Kitware (kitware.com/cmake).
    
-   **llvm** folder: contains the compilers provided by the NDK.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/I1RdFXBASTu9DnD3uXGJKA/en-us_image_0000002537925222.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062129Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F7D296EA902D2CB1C544180B426166781E937596D5511D912795EA0204BE0F4C)
    

#### Common NDK Modules

The following table describes the common modules of the NDK and their functionalities.

| Module | Description |
| :-- | :-- |
| C standard library | Provides C standard library APIs based on musl. |
| C++ standard library | Provides the C++ runtime APIs. |
| Log | Provides APIs for outputting HiLog logs to the system. |
| Node-API | Provides APIs for interaction between ArkTS/JS and C/C++. |
| FFRT | Provides a task-based concurrent programming framework. |
| libuv | Provides a third-party asynchronous I/O library. |
| zlib | Provides the zlib library for basic data compression and decompression. |
| Rawfile | Provides APIs for reading various packaged resources of an application. |
| XComponent | Provides surface and touchscreen event APIs for you to develop high-performance graphics applications. |
| Drawing | Provides a 2D graphics library for drawing on the surface. |
| OpenGL | Provides OpenGL 3D graphics interfaces. |
| OpenSL ES | Provides APIs for 2D and 3D audio acceleration. |
