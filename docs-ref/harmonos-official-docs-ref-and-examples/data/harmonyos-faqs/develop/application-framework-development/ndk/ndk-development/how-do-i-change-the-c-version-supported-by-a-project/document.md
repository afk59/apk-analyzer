# How do I change the C++ version supported by a project?

**Question**

How do I modify the C++ version? What are the C++ standards supported by the system?

**Answer**

-   libc++ version
    
    HarmonyOS 3.0 supports libc++ with Clang/LLVM 10.0.1.
    
    HarmonyOS 3.2 supports libc++ with Clang/LLVM 12.0.1.
    
    HarmonyOS NEXT Developer Preview0 supports libc++ with Clang/LLVM 15.0.4.
    
-   Supported C++ capabilities
    
    The C++11 and C++14 standards are fully supported, and the C++17 and C++20 standards are on the way.
    
-   Version modification
    
    The default C++ version of the SDK is 14. To modify the version, use either of the following methods:
    
    -   Modify the version information in the **CMakelists.txt** file.
        
        set(NATIVERENDER\_ROOT\_PATH ${CMAKE\_CURRENT\_SOURCE\_DIR})
        
        \# Add the following line:
        
        set(CMAKE\_CXX\_STANDARD 17)# Set the C++ standard to 17.
        
    -   Add **"cppFlags": "--std=c++17"** to the **build-profile.json5** file of the module.
        
        "buildOption": {
          "externalNativeOptions": {
            "path": "./src/main/cpp/CMakeLists.txt",
            "arguments": "",
            // Modify the following line
            "cppFlags": "--std=c++17"
          },
        },
