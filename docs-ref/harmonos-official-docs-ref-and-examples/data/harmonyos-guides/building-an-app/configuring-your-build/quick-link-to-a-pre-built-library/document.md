# Quick Link to a Pre-built Library

Hvigor provides the quick link feature for you to use the native-related .so library and .h or .hpp interface file in a dependent module in your project.

#### Header Files

-   For a shared package:
    
    If an interface file such as .h file exists in the **include** directory of the shared package, Hvigor automatically adds the directory to the CMake interface directory.
    
-   For a local dependent module:
    
    If an interface file such as .h file exists in the local dependent module, you can specify the interface file directory in under **buildOption/nativeLib/headerPath** in the **build-profile.json5** file.
    
    "buildOption": {
      "nativeLib": {
        "headerPath": "src/main/cpp/include"
      }
    }
    

#### Pre-built Library

If the .so library in a shared package or local dependent module is referenced in your project, Hvigor will generate CMake [config-file packages](https://cmake.org/cmake/help/latest/manual/cmake-packages.7.html#config-file-packages) during compilation and automatically import the .so library through CMake [find\_package](https://cmake.org/cmake/help/latest/command/find_package.html#find-package). You only need to declare the library link in ${_moduleName_::_soName_} format in the **CMakeLists.txt** script, where _moduleName_ indicates the dependent module name and _soName_ indicates the .so library name.

For example, in the **oh-package.json5** file, add the dependency on the **curl** shared package that contains **libcurl.so**:

// oh-package.json5
"dependencies": { 
  "curl": "1.0.0" 
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/utFvrY4mSvCd19rcv-RCYw/en-us_image_0000002532750015.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062155Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=01168C400272BE789AF126BD5E24E864DFC1047DD2CD4B26D710F67EBB7461D0)

Declare the link in the **CMakeLists.txt script** of the project:

// CMakeLists.txt
add\_library(entry SHARED napi\_init.cpp)
# ${moduleName::soName}.
target\_link\_libraries(entry PUBLIC curl::curl)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/JsU54kPnT0mxLU4uvhDtMA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062155Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=11428FE3FE972CCAE3F7B1BD35FE44E7D95AD9F40C1832478544FE148C354789)

For a local module, an HAR exposes only the .so libraries built by the module, while an HSP exposes not only the .so libraries built by the module but also those on which the module depends.
