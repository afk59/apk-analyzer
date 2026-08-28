# Building an NDK Project with Prebuilt Libraries

In an NDK project, you can use the CMake syntax to import and use prebuilt libraries. When prebuilt libraries are referenced, both those in the module's **libs** directory and those declared in the **CMakeLists.txt** build script are packaged.

#### Constraints for Using Prebuilt Libraries

1.  Ensure that the imported dynamic libraries (.so files) are compiled using the [HarmonyOS NDK toolchain](../overview/document.md). For details about how to compile prebuilt libraries with the HarmonyOS NDK toolchain, see [Adaptation Process of Using CMake to Build Third-Party Libraries](https://developer.huawei.com/consumer/en/doc/best-practices/bpta-cmake-adapts-to-harmonyos#section1826019653918).
    
2.  Ensure that dependencies of the imported .so dynamic libraries are also imported into the project and compiled using the HarmonyOS NDK toolchain.
    

#### Importing a Prebuilt Library

You can import a prebuilt library by directly copying the library files into the project. For example, the prebuilt library **libavcodec\_ffmpeg.so** is located in the following directory during development.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/nqo473fISdek43LN-DfOuA/en-us_image_0000002537765288.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062130Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EE3F3355E6492453A5BF7D22A9E167A76F9D9FD0E05EA1CE37F1B992CB1CFE2E)

To use it in your project, add it through **add\_library** in the module's **CMakeLists.txt** build script and declare information such as the path to the prebuilt library. Then you can declare the link to the prebuilt library in **target\_link\_libraries**. The following is an example of the build script:

add\_library(library SHARED hello.cpp)

add\_library(avcodec\_ffmpeg SHARED IMPORTED)
set\_target\_properties(avcodec\_ffmpeg
    PROPERTIES
    IMPORTED\_LOCATION ${CMAKE\_CURRENT\_SOURCE\_DIR}/third\_party/FFmpeg/libs/${OHOS\_ARCH}/libavcodec\_ffmpeg.so)

target\_link\_libraries(library PUBLIC libace\_napi.z.so avcodec\_ffmpeg)

Add **include\_directories** in the module's **CMakeLists.txt** build script.

include\_directories(
    # ...
    ${CMAKE\_CURRENT\_SOURCE\_DIR}/third\_party/FFmpeg/include
)

When prebuilt libraries are used in the HAR, the currently built libraries and prebuilt libraries required for linking are packed to the **libs** directory in the HAR, as shown in the following figure.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/KbvxOv_jS6y9kIy0x9GiKw/en-us_image_0000002537925228.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062130Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E28B2A6702C76D3893C980D5BD7B639D8EB68ADA94710E246ABB02C83CDE602A)

## Resolving the SONAME Issue with Prebuilt Libraries

Ensure that the imported prebuilt dynamic libraries (.so files) have the correct SONAME set.

If a prebuilt .so file lacks a SONAME, the linker will embed the absolute path of the .so file into the **dynamic section** of dependent binaries. When these binaries are packaged into a HAP for release, the dynamic loader may fail to locate the .so file, leading to runtime errors.

Use the **llvm-readelf** tool to verify whether a .so file has a SONAME set. The tool's path depends on your installation: **${DevEco Studio installation directory}/sdk/default/HarmonyOS/native/llvm/bin** or **${command-line-tools installation directory}/sdk/default/HarmonyOS/native/llvm/bin/llvm-readelf**.

Example:

\> ${YOUR\_PATH}/command-line-tools/sdk/default/HarmonyOS/native/llvm/bin/llvm-readelf -d libavcodec\_ffmpeg.so | grep SONAME
0x000000000000000e (SONAME)             Library soname: \[libavcodec\_ffmpeg.so\]

For prebuilt dynamic libraries (.so files) built with CMake, no additional configuration is required for setting the SONAME, since CMake automatically sets the SONAME for them as long as the target platform supports it.

For prebuilt dynamic libraries (.so files) built with other tools, explicitly configure **ldflags** to set the SONAME.

${...}/clang++ ${...} -Wl,-soname,libavcodec\_ffmpeg.so

#### Using a Prebuilt Library Integrated in a Remote HAR Dependency

To use a prebuilt library integrated in a remote dependency HAR, write the reference script in **CMakeLists.txt** as follows:

set(DEPENDENCY\_PATH ${CMAKE\_CURRENT\_SOURCE\_DIR}/../../../oh\_modules)
add\_library(library SHARED IMPORTED)
set\_target\_properties(library
    PROPERTIES
    IMPORTED\_LOCATION ${DEPENDENCY\_PATH}/library/libs/${OHOS\_ARCH}/liblibrary.so)
add\_library(entry SHARED hello.cpp)
target\_link\_libraries(entry PUBLIC libace\_napi.z.so library)

#### Using a Prebuilt Library Integrated in a Local HAR

To use a prebuilt library integrated in a local HAR, write the reference script in **CMakeLists.txt** as follows:

set(LIBRARY\_DIR "${NATIVERENDER\_ROOT\_PATH}/../../../../library/build/default/intermediates/libs/default/${OHOS\_ARCH}/")
add\_library(library SHARED IMPORTED)
set\_target\_properties(library
    PROPERTIES
    IMPORTED\_LOCATION ${LIBRARY\_DIR}/liblibrary.so)
add\_library(entry SHARED hello.cpp)
target\_link\_libraries(entry PUBLIC libace\_napi.z.so library)
