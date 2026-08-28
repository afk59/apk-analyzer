# How do I resolve the "A 'unknown type name' error has occurred" error during C++ compilation?

**Symptom**

The error message "A 'unknown type name' error has occurred" is displayed during compilation of a HarmonyOS C++ project.

**Solution**

This error occurs when the compiler cannot recognize a certain type. This may be due to the type not being defined, the relevant header file not being included, or the path to the included header file being incorrect. To locate and rectify this issue, perform the following steps:

1\. Check for included header files.

Make sure all necessary header files are correctly included in the source file. For example, if you are using a custom type or a type provided by a library, be sure to include the relevant header file in the file where the type is used.

**Example**

#include "myLibrary.h" 
int main() {
     MyType obj;
     // Use custom types
     return 0;
}

#ifndef MY\_LIBRARY\_H
#define MY\_LIBRARY\_H
class MyType {
public:
     MyType() {}
     void doSomething();
};
#endif

2\. Verify header file paths.

Make sure the search paths for header files are correctly set in the **CMakeLists.txt** file. You can add header file directories using **include\_directories**.

Example **CMakeLists.txt**:

cmake\_minimum\_required(VERSION 3.10)
project(MyProject)
set(CMAKE\_CXX\_STANDARD 17)
# Add header file directory
include\_directories(${CMAKE\_SOURCE\_DIR}/include)
# Add source file
add\_library(myProgram SHARED src/main.cpp src/myLibrary.cpp)

3\. Clean and regenerate build files.

Sometimes, build files may become corrupted or symbol definitions may be lost. Try cleaning the build directory and regenerating the build files:

hvigorw clean

Alternatively, manually delete the .cxx directory from the module.

4\. Enable verbose compilation output.

To understand the detailed compilation process, you can enable more verbose output. Add the following to the **CMakeLists.txt** file:

set(CMAKE\_VERBOSE\_MAKEFILE ON)

5\. Check the compilation output logs.

By default, Ninja generates a **.ninja\_log** file containing detailed information about the build process. You can check this log file to identify issues that occur during the build process.

cat .cxx/default/default/arm64-v8a/.ninja\_log

6\. Use CMake's **message** function for debugging.

Add the **message** function in the **CMakeLists.txt** file to print some debug information to ensure that paths and variables are correctly set.

**Example**

message(STATUS "Source directory: ${CMAKE\_SOURCE\_DIR}")
message(STATUS "Include directories: ${CMAKE\_INCLUDE\_PATH}")

7\. Check the availability of the API that caused the error in the current version if it is a system API. For example, **OH\_AudioWorkgroup\_AddCurrentThread** is supported since API version 20.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/wApso1WLQyGBOJEcxrWhYQ/en-us_image_0000002350221468.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062619Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B34A9C2BF5471815D971E9F9299A96C1E14BAD360317693604D907005915FD60)

**Conclusion**

By following the above steps, you can locate and resolve the "error: unknown type name" issue. When compiling a C++ project with CMake, Ninja, and LLVM, it is crucial to ensure that all header files are correctly included and that the correct header file paths are set. If the issue persists, consult the compilation output logs for clues to help you identify the specific cause.
