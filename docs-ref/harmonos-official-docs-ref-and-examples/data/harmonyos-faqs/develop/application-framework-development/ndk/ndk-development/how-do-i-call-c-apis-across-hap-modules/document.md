# How do I call C++ APIs across HAP modules?

**Symptom**

To call the code in C++ NativeSDK Module B from C++ NativeSDK Module A and implement source code debugging, perform the following steps to configure the dependencies:

1\. Add the path of Module B to the **CMakeLists.txt** file of Module A.

2\. Compile and generate a library file of Module B, and add the path of the library file to the link path of module A.

3\. Include the header file of Module B in the source code of Module A.

4\. Configure the debugger to ensure that the debugging information of Module B can be loaded.

The procedure is as follows:

1\. Open the **CMakeLists.txt** file of Module A and add the following content:

cmake

add\_subdirectory(path/to/moduleB)

target\_link\_libraries(ModuleA ModuleB)

2\. Include the header file of Module B in the source code of Module A.

cpp

#include "path/to/moduleB/header.h"

3\. Configure the debugger to ensure that the debugging information of Module B can be loaded. For example, when using GDB, you can add the following content to the debugging configuration:

sh

set solib-search-path path/to/moduleB/lib

After the preceding steps are complete, Module A can correctly call the code in Module B and support source code debugging.

**Solution**

The following uses ModuleA and ModuleB as an example to show how to enable C++ code in ModuleA to reference the C++ APIs of ModuleB. The C++ code in ModuleA needs to reference the C++ APIs of ModuleB.

Create Moduleb. (Choose **File** > **New** > **Module...** > **Shared Library**, input the module name, and select **Enable native**.)

Configure Moduleb.

1.  In the **src/main/cpp/** directory, create an **include** directory (or another name, which must be the same in the configuration) and place the header files to be exposed in the **src/main/cpp/include** directory.
2.  Configure the **build-profile.json5** file.
    
    "nativeLib": {
      "debugSymbol": {
        "strip": true,
        "exclude": \[\]
      },
      "headerPath": "src/main/cpp/include"
    },
    

Configure Modulea.

1.  Configure the dependency of moduleb in the **oh-package.json5** file.
    
    "dependencies": {
      "libmodulea.so": "file:./src/main/cpp/types/libmodulea",
      "moduleb": "file:../Moduleb"
    },
    
2.  Configure the link module in the **CMakeLists.txt** file.
    
    target\_link\_libraries(modulea PUBLIC libace\_napi.z.so moduleb::moduleb)
    
3.  Import the header file (**#include** "xxx.h") to the C++ code, and then call the C++ APIs in moduleb.
