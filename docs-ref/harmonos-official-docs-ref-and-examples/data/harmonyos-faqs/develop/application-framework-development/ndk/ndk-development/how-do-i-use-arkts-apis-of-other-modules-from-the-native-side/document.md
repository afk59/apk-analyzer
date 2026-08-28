# How do I use ArkTS APIs of other modules from the native side?

**Question**

The system provides some ArkTS APIs without the corresponding NDK APIs. How do I use these ArkTS APIs when implementing service logic in C++?

**Answer**

You can use **napi\_load\_module** to call the APIs defined in an ArkTS file. The procedure is as follows:

1.  Use **napi\_load\_module** to load the target module.
2.  Use **napi\_get\_named\_property** to obtain the module property.
3.  Use **napi\_call\_function** to call the APIs.
    
    Sample code:
    

Declare the APIs in ArkTS.

// src/main/ets/pages/Test.ets
let value = 123;
function test() {
  console.log('Hello HarmonyOS');
}
export {value, test};

Configure the **build-profile.json5** file of the module as follows:

Note that the configuration is performed in the module-level **build-profile.json5** file, not the project-level **build-profile.json5** file. In addition, ensure that the **sources** item is set to the correct path of the **Test.ets** file.

"buildOption": {
  "externalNativeOptions": {
    "path": "./src/main/cpp/CMakeLists.txt",
    "arguments": "",
    "cppFlags": "",
  },
  "arkOptions": {
    "runtimeOnly": {
      "sources": \[
        "./src/main/ets/pages/Test.ets"
      \]
    }
  },
},

Use **napi\_load\_module** to load the module from the **Test** file, call the **test()** function, and obtain the variable _value_.

#include "napi/native\_api.h" 
#include <string> 
 
static napi\_value LoadModule(napi\_env env, napi\_callback\_info info) { 
    napi\_value result; 
    // 1. Load modules from the Test file using napi\_load\_module 
    napi\_status status = napi\_load\_module(env, "ets/pages/Test", &result); 
    napi\_value testFn; 
    // 2. Use napi\_get\_named\_property to obtain the test function 
    napi\_get\_named\_property(env, result, "test", &testFn); 
    // 3. Call the function test using napi\_call\_function 
    napi\_call\_function(env, result, testFn, 0, nullptr, nullptr); 
    napi\_value value; 
    napi\_value key; 
    std::string keyStr = "value"; 
    napi\_create\_string\_utf8(env, keyStr.c\_str(), keyStr.size(), &key); 
    // 4. Get variable value using napi\_get\_property 
    napi\_get\_property(env, result, key, &value); 
    return value; 
}
