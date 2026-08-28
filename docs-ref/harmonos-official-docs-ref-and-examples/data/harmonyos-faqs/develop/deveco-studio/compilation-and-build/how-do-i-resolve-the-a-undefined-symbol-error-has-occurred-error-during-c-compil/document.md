# How do I resolve the "A 'undefined symbol' error has occurred" error during C++ compilation?

**Symptom**

The error message "A 'undefined symbol' error has occurred" is displayed during compilation of a HarmonyOS C++ project.

**Solution**

The "undefined symbol" error typically indicates that the linker cannot find the definition of a specific symbol. This issue often occurs when source files are not compiled or linked correctly, or when the necessary library files are missing. To locate and rectify this issue, perform the following steps:

1\. Make sure all source files are included in the CMake build.

Check your **CMakeLists.txt** file to ensure that all relevant source files are included in the project.

Example **CMakeLists.txt**:

cmake\_minimum\_required(VERSION 3.10)
project(MyProject)
set(CMAKE\_CXX\_STANDARD 17)
include\_directories(${CMAKE\_CURRENT\_SOURCE\_DIR}
                    ${CMAKE\_CURRENT\_SOURCE\_DIR}/include)
# Add all source files
add\_library(myProgram SHARED main.cpp myLibrary.cpp)

2\. Confirm the symbol definitions in the source files.

Make sure symbols are correctly defined in all relevant source files. For example, check whether **myLibrary.cpp** includes the definition of **myFunction**.

**myLibrary.cpp**

#include "myLibrary.h" 
void myFunction() {     
// Function implementation
}

**myLibrary.h**

#ifndef MY\_LIBRARY\_H
#define MY\_LIBRARY\_H 
void myFunction();  
#endif 

3\. Check the compilation and linking order.

Make sure all source files and library files are compiled and linked in the correct order. CMake and Ninja usually handle this order issue, but problems may arise during manual compilation.

4\. Clean and regenerate build files.

Sometimes, build files may become corrupted or symbol definitions may be lost. Try cleaning the build directory and regenerating the build files:

hvigorw clean 1 

Alternatively, manually delete the .cxx directory from the module.

5\. Check library paths and linker flags.

If using third-party libraries, make sure the library paths and linker flags are correctly configured in the **CMakeLists.txt** file. Sample code:

cmake\_minimum\_required(VERSION 3.10)
project(MyProject)
set(CMAKE\_CXX\_STANDARD 17)
# Ensure the addition of the header file for the third-party library
include\_directories(${PATH\_TO\_EXTERNAL\_LIBRARY}
                    ${PATH\_TO\_EXTERNAL\_LIBRARY}/include)
# Add source files
add\_library(myProgram SHARED main.cpp myLibrary.cpp)
# Link to third-party libraries
target\_link\_libraries(myProgram PUBLIC /path/to/external/library)

6\. Enable verbose compilation and linking output.

To understand the detailed compilation and linking process, you can enable more verbose output. Add the following to the **CMakeLists.txt** file:

set(CMAKE\_VERBOSE\_MAKEFILE ON)

7\. Check the Ninja output logs.

By default, Ninja generates a **.ninja\_log** file containing detailed information about the build process. You can check this log file to identify issues that occur during the build process.

cat {module}/.cxx/default/default/arm64-v8a/.ninja\_log 

Check the log file for the source file or header file containing the symbols.

8\. Use the nm tool to check symbols.

Inspect the symbols in the target file and library file to ensure that the symbol definitions exist.

You can do so with the nm tool in the SDK: **sdk/default/openharmony/native/llvm/bin/llvm-nm**.

Check the target file.

nm myLibrary.o | grep myFunction 

Check the third-party library file.

nm /path/to/external/library | grep myFunction

**Conclusion**

By following the above steps, you can locate and resolve the "error: undefined symbol" issue. When compiling a C++ project with CMake, Ninja, and LLVM, ensure that all source files and library files are correctly included in the project and that the compilation and linking options are correctly configured. If the issue persists, consult the compilation and linking output logs for clues to help you identify the specific cause.
