# Loading a Module in the Main Thread Using Node-API

#### **Scenario**

You can use **napi\_load\_module** to load a module in the main thread. After the module is loaded, you can use **napi\_get\_property** to obtain the variables of the module or use **napi\_get\_named\_property** to obtain the functions of the module.

#### Function Description

napi\_status napi\_load\_module(napi\_env env, const char\* path, napi\_value\* result);

| Parameter | Description |
| :-- | :-- |
| env | Current JSVM environment. |
| path | Pointer to the path of the file or name of the module to load. |
| result | Pointer to the module loaded. |

#### Constraints

-   Do not use this API in non-main threads.
-   Do not use this API in the **Init()** function.
-   Do not load a file in the callback function of a thread-safe function.
-   Calling this API in the signal function is insecure. Direct calling may cause stack overflow.

You are advised to use [napi\_load\_module\_with\_info](../loading-a-module-using-node-api/document.md) to load modules. This API supports more scenarios.

#### Scenarios Supported by napi\_load\_module

| Scenario | Scenario Description | Remarks |
| :-- | :-- | :-- |
| System module | Load **@ohos.** or **@system.**. | \- |
| Local project module | Load a module defined in a file under the **ets** directory. | The file path must start with **ets**. |
| Local project module | Load a file path in a module. | The file path must start with **moduleName**. |
| Local project module | Load the name of a HAR module. | \- |
| Local project module | Load the name of an HSP module. | \- |
| Remote package | Load the name of a remote HAR module. | \- |
| Remote package | Load the ohpm package name. | \- |
| Native library of a module | Load **libNativeLibrary.so**. | \- |

-   **Loading a System Module**
    
    static napi\_value loadModule(napi\_env env, napi\_callback\_info info) {
        // 1. Call napi\_load\_module to load the @ohos.hilog module.
        napi\_value result;
        napi\_status status = napi\_load\_module(env, "@ohos.hilog", &result);
        if (status != napi\_ok) {
            return nullptr;
        }
    
        // 2. Call napi\_get\_named\_property to obtain the info function.
        napi\_value infoFn;
        status = napi\_get\_named\_property(env, result, "info", &infoFn);
        if (status != napi\_ok) {
            return nullptr;
        }
        
        napi\_value tag;
        std::string formatStr = "test";
        napi\_create\_string\_utf8(env, formatStr.c\_str(), formatStr.size(), &tag);
        
        napi\_value outputString;
        std::string str = "Hello HarmonyOS";
        napi\_create\_string\_utf8(env, str.c\_str(), str.size(), &outputString);
        
        napi\_value flag;
        napi\_create\_int32(env, 0, &flag);
    
        napi\_value args\[3\] = {flag, tag, outputString};
        // 3. Call napi\_call\_function to invoke the info function.
        status = napi\_call\_function(env, result, infoFn, 3, args, nullptr);
        if (status != napi\_ok) {
            return nullptr;
        }
        return result;
    }
    
-   **Loading a Module Defined in a File Under the ets Directory**
    
    For example, load a module from a file as shown in the following ArkTS code:
    
    //./src/main/ets/Test.ets
    let value = 123;
    function test() {
      console.info("Hello HarmonyOS");
    }
    export {value, test};
    

1.  Add the following to the **build-profile.json5** file of the module.
    
    {
      "buildOption" : {
        "arkOptions" : {
          "runtimeOnly" : {
            "sources": \[
              "./src/main/ets/Test.ets"
            \]
          }
        }
      }
    }
    
2.  Call **napi\_load\_module** to load the module from the **Test.ets** file, call the **test()** function, and obtain the **value** variable.
    
    static napi\_value loadModule(napi\_env env, napi\_callback\_info info) {
        napi\_value result;
        // 1. Call napi\_load\_module to load the module from the Test.ets file.
        napi\_status status = napi\_load\_module(env, "ets/Test", &result);
        if (status != napi\_ok) {
            return nullptr;
        }
    
        napi\_value testFn;
        // 2. Call napi\_get\_named\_property to obtain the test function.
        status = napi\_get\_named\_property(env, result, "test", &testFn);
        if (status != napi\_ok) {
            return nullptr;
        }
        // 3. Call napi\_call\_function to invoke the test function.
        status = napi\_call\_function(env, result, testFn, 0, nullptr, nullptr);
        if (status != napi\_ok) {
            return nullptr;
        }
    
        napi\_value value;
        napi\_value key;
        std::string keyStr = "value";
        napi\_create\_string\_utf8(env, keyStr.c\_str(), keyStr.size(), &key);
        // 4. Call napi\_get\_property to obtain the value variable.
        status = napi\_get\_property(env, result, key, &value);
        if (status != napi\_ok) {
            return nullptr;
        }
        return result;
    }
    

-   **Loading a File Path in a Module**
    
    For example, load a module from a file as shown in the following ArkTS code:
    
    //./src/main/ets/Test.ets
    let value = 123;
    function test() {
      console.info("Hello HarmonyOS");
    }
    export {value, test};
    

1.  Configure the **build-profile.json5** file of the current module as follows:
    
    {
      "buildOption" : {
        "arkOptions" : {
          "runtimeOnly" : {
            "sources": \[
              "./src/main/ets/Test.ets"
            \]
          }
        }
      }
    }
    
2.  Call **napi\_load\_module** to load the module from the **Test.ets** file, call the **test()** function, and obtain the **value** variable.
    
    static napi\_value loadModule(napi\_env env, napi\_callback\_info info) {
        napi\_value result;
        // 1. Call napi\_load\_module to load the module from the Test.ets file.
        napi\_status status = napi\_load\_module(env, "entry/src/main/ets/Test", &result);
        if (status != napi\_ok) {
            return nullptr;
        }
    
        napi\_value testFn;
        // 2. Call napi\_get\_named\_property to obtain the test function.
        status = napi\_get\_named\_property(env, result, "test", &testFn);
        if (status != napi\_ok) {
            return nullptr;
        }
        // 3. Call napi\_call\_function to invoke the test function.
        status = napi\_call\_function(env, result, testFn, 0, nullptr, nullptr);
        if (status != napi\_ok) {
            return nullptr;
        }
    
        napi\_value value;
        napi\_value key;
        std::string keyStr = "value";
        napi\_create\_string\_utf8(env, keyStr.c\_str(), keyStr.size(), &key);
        // 4. Call napi\_get\_property to obtain the value variable.
        status = napi\_get\_property(env, result, key, &value);
        if (status != napi\_ok) {
            return nullptr;
        }
        return result;
    }
    

-   **Loading a HAR Module**
    
    For example, the **Index.ets** file in a HAR is as follows:
    
    // Library Index.ets
    let value = 123;
    function test() {
      console.info("Hello HarmonyOS");
    }
    export {value, test};
    

1.  Configure **dependencies** in the **oh-package.json5** file of the module.
    
    {
      "dependencies": {
        "library": "file:../library"
      }
    }
    
2.  Configure **build-profile.json5** for the module that uses the library.
    
    {
      "buildOption" : {
        "arkOptions" : {
          "runtimeOnly" : {
            "packages": \[
              "library"
            \]
          }
        }
      }
    }
    
3.  Call **napi\_load\_module** to load the library, call the **test** function, and obtain the **value** variable.
    
    static napi\_value loadModule(napi\_env env, napi\_callback\_info info) {
        napi\_value result;
        // 1. Call napi\_load\_module to load the library.
        napi\_status status = napi\_load\_module(env, "library", &result);
        if (status != napi\_ok) {
            return nullptr;
        }
    
        napi\_value testFn;
        // 2. Call napi\_get\_named\_property to obtain the test function.
        status = napi\_get\_named\_property(env, result, "test", &testFn);
        if (status != napi\_ok) {
            return nullptr;
        }
        // 3. Call napi\_call\_function to invoke the test function.
        status = napi\_call\_function(env, result, testFn, 0, nullptr, nullptr);
        if (status != napi\_ok) {
            return nullptr;
        }
    
        napi\_value value;
        napi\_value key;
        std::string keyStr = "value";
        napi\_create\_string\_utf8(env, keyStr.c\_str(), keyStr.size(), &key);
        // 4. Call napi\_get\_property to obtain the value variable.
        status = napi\_get\_property(env, result, key, &value);
        if (status != napi\_ok) {
            return nullptr;
        }
        return result;
    }
    

-   **Loading an HSP module**
    
    For example, the **Index.ets** file in an HSP is as follows:
    
    // Shared library Index.ets
    let value = 123;
    function test() {
      console.info("Hello HarmonyOS");
    }
    export {value, test};
    

1.  Configure **dependencies** in the **oh-package.json5** file of the module.
    
    {
      "dependencies": {
        "sharedlibrary": "file:../sharedlibrary"
      }
    }
    
2.  Configure **build-profile.json5** for the module that uses the library.
    
    {
      "buildOption" : {
        "arkOptions" : {
          "runtimeOnly" : {
            "packages": \[
              "sharedlibrary"
            \]
          }
        }
      }
    }
    
3.  Call **napi\_load\_module** to load the shared library, call the **test** function, and obtain the **value** variable.
    
    static napi\_value loadModule(napi\_env env, napi\_callback\_info info) {
        napi\_value result;
        // 1. Call napi\_load\_module to load the shared library.
        napi\_status status = napi\_load\_module(env, "sharedlibrary", &result);
        if (status != napi\_ok) {
            return nullptr;
        }
    
        napi\_value testFn;
        // 2. Call napi\_get\_named\_property to obtain the test function.
        status = napi\_get\_named\_property(env, result, "test", &testFn);
        if (status != napi\_ok) {
            return nullptr;
        }
        // 3. Call napi\_call\_function to invoke the test function.
        status = napi\_call\_function(env, result, testFn, 0, nullptr, nullptr);
        if (status != napi\_ok) {
            return nullptr;
        }
    
        napi\_value value;
        napi\_value key;
        std::string keyStr = "value";
        napi\_create\_string\_utf8(env, keyStr.c\_str(), keyStr.size(), &key);
        // 4. Call napi\_get\_property to obtain the value variable.
        status = napi\_get\_property(env, result, key, &value);
        if (status != napi\_ok) {
            return nullptr;
        }
        return result;
    }
    

-   **Loading a Remote HAR Module**

1.  Configure **dependencies** in the **oh-package.json5** file of the module.
    
    {
      "dependencies": {
        "@ohos/hypium": "1.0.16"
      }
    }
    
2.  Configure **build-profile.json5** for the module that uses **@ohos/hypium**.
    
    {
      "buildOption" : {
        "arkOptions" : {
          "runtimeOnly" : {
            "packages": \[
              "@ohos/hypium"
            \]
          }
        }
      }
    }
    
3.  Call **napi\_load\_module** to load **@ohos/hypium** and obtain the **DEFAULT** variable.
    
    static napi\_value loadModule(napi\_env env, napi\_callback\_info info) {
        napi\_value result;
        // 1. Call napi\_load\_module to load @ohos/hypium.
        napi\_status status = napi\_load\_module(env, "@ohos/hypium", &result);
        if (status != napi\_ok) {
            return nullptr;
        }
    
        napi\_value key;
        std::string keyStr = "DEFAULT";
        napi\_create\_string\_utf8(env, keyStr.c\_str(), keyStr.size(), &key);
        // 2. Call napi\_get\_property to obtain the DEFAULT variable.
        napi\_value defaultValue;
        status = napi\_get\_property(env, result, key, &defaultValue);
        if (status != napi\_ok) {
            return nullptr;
        }
        return result;
    }
    

-   **Loading an ohpm Package**

1.  Configure **dependencies** in the **oh-package.json5** file of the module.
    
    {
      "dependencies": {
        "@ohos/axios": "2.2.4",
      }
    }
    
2.  Configure **build-profile.json5** for the module that uses **@ohos/axios**.
    
    {
      "buildOption" : {
        "arkOptions" : {
          "runtimeOnly" : {
            "packages": \[
              "@ohos/axios"
            \]
          }
        }
      }
    }
    
3.  Call **napi\_load\_module** to load **@ohos/axios** and obtain the **VERSION** variable.
    
    static napi\_value loadModule(napi\_env env, napi\_callback\_info info) {
        napi\_value result;
        // 1. Call napi\_load\_module to load @ohos/axios.
        napi\_status status = napi\_load\_module(env, "@ohos/axios", &result);
        if (status != napi\_ok) {
            return nullptr;
        }
    
        napi\_value key;
        std::string keyStr = "VERSION";
        napi\_create\_string\_utf8(env, keyStr.c\_str(), keyStr.size(), &key);
        // 2. Call napi\_get\_property to obtain the version.
        napi\_value defaultValue;
        status = napi\_get\_property(env, result, key, &defaultValue);
        if (status != napi\_ok) {
            return nullptr;
        }
        return result;
    }
    

-   **Loading a Native Library**
    
    For example, the **index.d.ts** file of **libentry.so** is as follows:
    
    //index.d.ts
    export const add: (a: number, b: number) => number;
    

1.  Configure **dependencies** in the **oh-package.json5** file of the module.
    
    {
      "dependencies": {
        "libentry.so": "file:../src/main/cpp/types/libentry"
      }
    }
    
2.  Configure **build-profile.json5** for the module that uses **libentry.so**.
    
    {
      "buildOption" : {
        "arkOptions" : {
          "runtimeOnly" : {
            "packages": \[
              "libentry.so"
            \]
          }
        }
      }
    }
    
3.  Call **napi\_load\_module** to load **libentry.so** and call the **add** function.
    
    static napi\_value loadModule(napi\_env env, napi\_callback\_info info) {
        napi\_value result;
        // 1. Call napi\_load\_module to load libentry.so.
        napi\_status status = napi\_load\_module(env, "libentry.so", &result);
        if (status != napi\_ok) {
            return nullptr;
        }
    
        napi\_value addFn;
        // 2. Call napi\_get\_named\_property to obtain the add() function.
        status = napi\_get\_named\_property(env, result, "add", &addFn);
        if (status != napi\_ok) {
            return nullptr;
        }
        
        napi\_value a;
        napi\_value b;
        napi\_create\_int32(env, 2, &a);
        napi\_create\_int32(env, 3, &b);
        napi\_value args\[2\] = {a, b};
        // 3. Call napi\_call\_function to invoke the add() function.
        napi\_value returnValue;
        status = napi\_call\_function(env, result, addFn, 2, args, &returnValue);
        if (status != napi\_ok) {
            return nullptr;
        }
        return result;
    }
    

-   **Loading Another HAR Module to a HAR**
    
    For example, load **har2** to **har1**. The **Index.ets** file of **har2** is as follows:
    
    //har2 Index.ets
    let value = 123;
    function test() {
      console.info("Hello HarmonyOS");
    }
    export {value, test};
    

1.  Configure **dependencies** in the **oh-package.json5** file of **har1**.
    
    {
      "dependencies": {
        "har2": "file:../har2"
      }
    }
    
2.  Configure the **build-profile.json5** file for **har1**.
    
    {
      "buildOption" : {
        "arkOptions" : {
          "runtimeOnly" : {
            "packages": \[
              "har2"
            \]
          }
        }
      }
    }
    
3.  Call **napi\_load\_module** to load **har2** to **har1**, call the **test** function, and obtain the **value** variable.
    
    static napi\_value loadModule(napi\_env env, napi\_callback\_info info) {
        napi\_value result;
        // 1. Call napi\_load\_module to load har2.
        napi\_status status = napi\_load\_module(env, "har2", &result);
        if (status != napi\_ok) {
            return nullptr;
        }
        
        napi\_value testFn;
        // 2. Call napi\_get\_named\_property to obtain the test function.
        status = napi\_get\_named\_property(env, result, "test", &testFn);
        if (status != napi\_ok) {
            return nullptr;
        }
        // 3. Call napi\_call\_function to invoke the test function.
        status = napi\_call\_function(env, result, testFn, 0, nullptr, nullptr);
        if (status != napi\_ok) {
            return nullptr;
        }
    
        napi\_value value;
        napi\_value key;
        std::string keyStr = "value";
        napi\_create\_string\_utf8(env, keyStr.c\_str(), keyStr.size(), &key);
        // 4. Call napi\_get\_property to obtain the value variable.
        status = napi\_get\_property(env, result, key, &value);
        if (status != napi\_ok) {
            return nullptr;
        }
        return result;
    }
