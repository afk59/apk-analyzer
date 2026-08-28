# Building an NDK Project with CMake

In many complex application projects, C++ projects are compiled and built in command line mode through build systems such as CMake. The following describes how to switch an existing CMake project to the HarmonyOS toolchain so that CMake can be used to build the project.

#### Obtain the NDK development package

First, download and install DevEco Studio. The NDK development tools are located in the /sdk/default/HarmonyOS/native directory under the DevEco Studio installation directory.

## Configuring the Environment Variable

Skip this step if the NDK is downloaded from DevEco Studio.

1.  Add the CMake tool that comes with the NDK to the environment variables.
    
    -   On Linux
        
        \# Open the .bashrc file.
        vim ~/.bashrc
        # Append the custom CMake path to the file. Save the file and exit.
        export PATH=${sdk\_path}/native/build-tools/cmake/bin:$PATH
        # Run the source ~/.bashrc command to make the environment variable take effect.
        source ~/.bashrc
        
    -   On macOS
        
        #In the current user directory, open the .bash\_profile file. If the file does not exist, create one.
        vim ~/.bash\_profile
        #Append the custom CMake path to the file. Save the file and exit.
        export PATH=${sdk\_path}/native/build-tools/cmake/bin:$PATH
        #Run the source ~/.bash\_profile command to make the environment variable take effect.
        source ~/.bash\_profile
        
    -   On Windows
        
    
    Right-click **This PC** and choose **Properties** from the shortcut menu. In the displayed dialog box, click the **Advanced System Settings** tab and then click **Environment Variables**. Under **System Variables** dialog box, select the **Path** environment variable and click **Edit**. Add the paths, save the settings, and exit. (If the next step cannot be performed, restart the computer.)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/4YSCUXf0RTynkvYZmeQVuA/en-us_image_0000002537925224.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062129Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4BCB35BCE7C6247066F82342C1A0D2082C7AD05DA9152D2A76E73909FC21BE99)
    
    Open the CLI and run the **{cmake\_installation\_path}\\cmake.exe -version** command. If the CMake version number is displayed correctly, the environment variable configuration is complete.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/QTjiVokuRRuWmLFzzaWRIw/en-us_image_0000002568685001.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062129Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FF10E296B5A2895FADBC1FFEAF8430DD8258FDAB6384B1EBE9306A9C2D9A2F8D)
    
2.  Check the default CMake path.
    
    -   On Linux or macOS
        
        #Run the which cmake command.
        which cmake
        #The result should be the same as the custom path previously appended to the .bashrc file.
        ~/ohos-sdk/ohos-sdk/linux/native/build-tools/cmake/bin/cmake
        
    -   On Windows
        
        Right-click **This PC** and choose **Properties** from the shortcut menu. In the displayed dialog box, click the **Advanced System Settings** tab and then click **Environment Variables**. Under **System Variables** dialog box, check the **Path** value. The displayed CMake path should be the one you have added.
        

#### Using the NDK to Compile a Native Program

You can use the NDK to quickly develop a native program, including native dynamic libraries, static libraries, and executable files. The following exemplifies how to use the NDK to compile an executable program and a dynamic library in a C/C++ demo project.

## Demo Project

The following is a CMake demo project. This project contains two directories. The **include** directory contains the header files of the library, and the **src** directory contains all source code. Specifically, the **src** directory contains two files: **sum.cpp** (algorithm file) and **hello.cpp** (main entry file for invoking algorithms). The two files are compiled into an executable program and an algorithm dynamic library.

**Demo Project Directory**

demo
  ├── CMakeLists.txt
  ├── include
       └── sum.h
  └── src
       ├── CMakeLists.txt
       ├── sum.cpp
       └── hello.cpp

**CMakeLists.txt in the demo Directory**

\# Specify the minimum CMake version.
CMAKE\_MINIMUM\_REQUIRED(VERSION 3.16)

# Set the project name, which is HELLO in this example.
PROJECT(HELLO)

#Add a subdirectory and build the subdirectory.
ADD\_SUBDIRECTORY(src)

**CMakeLists.txt in the src Directory**

SET(LIBHELLO\_SRC hello.cpp)

# Set compilation flags.
SET(CMAKE\_CXX\_FLAGS "${CMAKE\_CXX\_FLAGS} -O0")
 
# Set the link parameter. The value below is only for exemplary purposes.
SET(CMAKE\_EXE\_LINKER\_FLAGS "${CMAKE\_EXE\_LINKER\_FLAGS} -Wl,--emit-relocs --verbose")

# Add a libsum dynamic library target. If the compilation is successful, a libsum.so file is generated.
ADD\_LIBRARY(sum SHARED sum.cpp)

# Add the executable target called Hello. If the compilation is successful, a Hello executable is generated.
ADD\_EXECUTABLE(Hello ${LIBHELLO\_SRC})

# Specify the path to the include directory of the Hello target.
TARGET\_INCLUDE\_DIRECTORIES(Hello PUBLIC ../include)

# Specify the name of the library to be linked to the Hello target.
TARGET\_LINK\_LIBRARIES(Hello PUBLIC sum)

**Source Code**

**hello.cpp** source code:

#include <iostream>
#include "sum.h"

int main(int argc,const char \*\*argv)
{
    std::cout<< "hello world!" <<std::endl;
    int total = sum(1, 100);
    std::cout<< "Sum 1 + 100=" << total << std::endl;
    return 0;
}

**sum.h** source code:

int sum(int a, int b);

**sum.cpp** source code:

#include <iostream>
    
int sum(int a, int b)
{
    return a + b;
}

## Compiling and Building the Demo Project

**For Linux and macOS**

In the module directory of the project directory, create the **build** directory to store the intermediate files generated during CMake building. **NOTE**

In the following commands, **ohos-sdk** is the root directory of the downloaded SDK. Replace it with the actual directory.

1.  To build the project using dynamic linking with the C++ shared library, use **OHOS\_STL=c++\_shared**. Note that if **OHOS\_STL** is not specified, **c++\_shared** is used by default. Set **DOHOS\_ARCH** based on the target system architecture. With **DOHOS\_ARCH=armeabi-v7a**, a 32-bit dynamic library is compiled; with **DOHOS\_ARCH=arm64-v8a**, a 64-bit dynamic library is compiled.
    
     >mkdir build && cd build
     >cmake -DOHOS\_STL=c++\_shared -DOHOS\_ARCH=arm64-v8a -DOHOS\_PLATFORM=OHOS -DCMAKE\_TOOLCHAIN\_FILE={ohos-sdk}/linux/native/build/cmake/ohos.toolchain.cmake ..
     >cmake --build .
    
2.  To build the project using static linking with the C++ shared library, use **OHOS\_STL=c++\_static**. Set **DOHOS\_ARCH** based on the target system architecture. With **DOHOS\_ARCH=armeabi-v7a**, a 32-bit static library is compiled; with **DOHOS\_ARCH=arm64-v8a**, a 64-bit static library is compiled.
    
     >mkdir build && cd build
     >cmake -DOHOS\_STL=c++\_static -DOHOS\_ARCH=arm64-v8a -DOHOS\_PLATFORM=OHOS -DCMAKE\_TOOLCHAIN\_FILE={ohos-sdk}/linux/native/build/cmake/ohos.toolchain.cmake ..
     >cmake --build .
    
    In the command, the **OHOS\_ARCH** and **OHOS\_PLATFORM** variables ultimately generate the **\--target** command argument for Clang++. In this example, they correspond to the **\--target=arm-linux-ohos** and **\--march=armv7a** arguments.
    
    In the **CMAKE\_TOOLCHAIN\_FILE** file, **\--sysroot={ndk\_sysroot\_directory}** is set for Clang++ by default, instructing the compiler to search for the root directory of system header files.
    

**For Windows**

Using CMake in Windows, unlike that in Linux, requires you to use the **\-G** option to specify the generator.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/uyon4h3KSYmcMLTmy-w8lg/en-us_image_0000002568765011.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062129Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3DFB670D9DDDEF17BF0E5B220356F9AE8E3726B9D89C5C112365F42B471FAA0A)

In this example, the Ninja generator, which comes with the NDK, is used, as indicated by **\-G "Ninja"**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/Kp6uCY1cQrSF9F1AqO7DBw/en-us_image_0000002537765286.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062129Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A0088956FE2F746A195A8CE73FB78812DE1944DB8E6F645B5A651123AD59F7B9)

Step 1. Create the **build** folder in the module directory of the project directory and run the following command:

 F:\\windows\\native\\build-tools\\cmake\\bin\\cmake.exe -G "Ninja" -D OHOS\_STL=c++\_shared -D OHOS\_ARCH=arm64-v8a -D OHOS\_PLATFORM=OHOS -D CMAKE\_TOOLCHAIN\_FILE=F:\\windows\\native\\build\\cmake\\ohos.toolchain.cmake ..

**NOTE**

If debugging is required, add the **\-D CMAKE\_BUILD\_TYPE=normal** option. Both the CMake path and the toolchain file path (**ohos.toolchain.cmake**) should point to your downloaded NDK directory.

The following figure shows the command output.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/H5ipv1sEQ-Ox799Xk-K5WA/en-us_image_0000002537925226.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062129Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=25FFDF903AAE9350A22F16033274A6CF817915044CABC1A36124F8F48DD04230)

The **build.ninja** file is the build configuration file.

Step 2. Use the ninja command to compile and generate the target file. The following figure shows the location of the target file.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/0wpeItLyTAiMNR8D8chkNA/en-us_image_0000002568685003.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062129Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A08C6028B2CDE4E26588E696731C80B0CF4C545C60243476ED84EBD4A69D10C4)

Use **ninja -f build.ninja** or **cmake --build**. The following figure shows the command output.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/AFlYxDPgT6mNaRtaWrCu-Q/en-us_image_0000002568765013.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062129Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F7FF0CF593F4A3CEBEB9F10A39690DE43F5C45ECC013C58E5C170D6030946BB4)
