# CPU Features

CPU features are hardware extensions provided by CPUs. You can call instructions and set special registers to use the CPU features, such as VFP-v32d32, Neon, IDIV, and AES on the ARMv7-A architecture. Many CPU features are optional, and different CPU vendors provide different CPU features.

During native library development in your HarmonyOS project, you can follow this topic to use code related to the CPU features in your application.

Currently, HarmonyOS does not provide APIs for obtaining CPU features. You can import library functions of the existing open source community as described below. Alternatively, you can directly read **/proc/cpuinfo** or call **libc getauxval(AT\_HWCAP)** to obtain the CPU features of a device.

#### How to Use

1.  Introduce the open-source library to the HarmonyOS C++ project. Download the [cpu\_features library](https://github.com/google/cpu_features), decompress it to the **cpp** directory of the project, and change the decompressed file name to **cpu\_features**. The following shows a sample application of the DevEco Studio C++ template.
    
    -   The directory structure after the decompression is as follows:
        
        MyApplication
          |-- entry
           |-- src
                |-- main
                     |-- cpp
                         |--cpu\_features
                         |--CMakeLists.txt
                         |--hello.cpp
        
    -   Add the path to the cpu\_features library to the **CMakeLists.txt** file.
        
        add\_subdirectory(cpu\_features) # Add a subdirectory to the project.
        target\_link\_libraries(entry PUBLIC cpu\_features) # Add the library files that need to be linked.
        
2.  Add the statement for determining the support for the CPU features to the code. The following uses the ARM and AArch64 architectures as an example:
    
    // ...
    // Include the header file for CPU architecture target detection.
    #include "cpu\_features\_macros.h"
    // In the ARM architecture, this macro is automatically defined in the preceding header file based on the target.
    #if defined (CPU\_FEATURES\_ARCH\_ARM)
    #include "cpuinfo\_arm.h" // Include the cpuinfo header file of the ARM architecture.
    #elif defined (CPU\_FEATURES\_ARCH\_AARCH64)
    #include "cpuinfo\_aarch64.h" // Include the cpuinfo header file of the AArch64 architecture.
    #endif
    // Add \`using namespace cpu\_features;\` in the C++ code.
    // Obtain CPU feature information based on the architecture in use.
    #if defined (CPU\_FEATURES\_ARCH\_ARM)
    static const ArmFeatures features = GetArmInfo().features;
    #elif defined (CPU\_FEATURES\_ARCH\_AARCH64)
    static const Aarch64Features features = GetAarch64Info().features;
    #endif
    void Compute(void) {
      // Determine whether the CPU features are supported based on the features field.
      if (features.aes) {
        // ...
      } else {
        // ...
      }
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/JUQR-U9hT6W7uLHP8wgkTA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062135Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DF245484DC592610600BD967E57B9958123F5453367FBAF7BF2A6FC6BB8FD3A3)
    
    The cpu\_features library reads the corresponding CPU feature information from the kernel through **/proc/cpuinfo** or **getauxval**. The information may fail to be read due to the use of the application sandbox. Pay attention to error handling.
