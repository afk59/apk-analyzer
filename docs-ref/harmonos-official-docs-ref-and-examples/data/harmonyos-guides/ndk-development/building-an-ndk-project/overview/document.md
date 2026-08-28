# Overview

By default, the HarmonyOS NDK uses CMake as the build system. To simplify your configuration process, the NDK provides the configuration file [ohos.toolchain.cmake](#introduction-to-ohostoolchaincmake) that complies with the HarmonyOS toolchain to predefine CMake variables.

You can build your project with the NDK in the following modes:

-   Build from source code
    
    To build from source code, you can use:
    
    -   [C++ application template provided by DevEco Studio](../building-an-ndk-project-with-the-deveco-studio-template/document.md)
    -   [CMake from the command line](../building-an-ndk-project-with-cmake/document.md)
-   [Build with prebuilt libraries](../building-an-ndk-project-with-prebuilt-libraries/document.md)
    

This section uses examples to describe how to use the NDK in a native project and how to write a CMake script to build a project with the NDK.

#### Introduction to ohos.toolchain.cmake

**ohos.toolchain.cmake** is the toolchain script provided by the HarmonyOS NDK for CMake. It predefines the build parameters that need to be set for building HarmonyOS applications, such as the target of the cross compilation device and the link mode of C++ runtime libraries. These parameters can be passed in by running CMake commands to change the default compilation and linking behavior. The following table lists the common parameters in this file.

| Name | Type | Description |
| :-- | :-- | :-- |
| OHOS\_STL | c++\_shared/c++\_static | 
Link mode of libc++.

Default value: **c++\_shared**

Available options are as follows:

**c++\_shared**: The native library dynamically links **libc++\_shared.so**.

**c++\_static**: The native library links the static library **libc++\_static.a**.

Because some global variables are involved during C++ runtime, all native libraries must be linked to your application in the same mode.

 |
| OHOS\_ARCH | armeabi-v7a/arm64-v8a/x86\_64 | Target architecture for native cross compilation. Available options are as follows: **armeabi-v7a**, **arm64-v8a**, and **x86\_64**. |
| OHOS\_PLATFORM | OHOS | Target platform. Currently, only HarmonyOS is supported. |

The preceding parameters control the cross compilation commands of Clang and generate proper command parameters.

-   The **\--target={arch}-linux-ohos** parameter instructs the compiler to generate binary files that comply with HarmonyOS ABI in the corresponding architecture.
    
-   The **\--sysroot={ndk\_root}/sysroot** parameter notifies the compiler of the location of the HarmonyOS header files.
