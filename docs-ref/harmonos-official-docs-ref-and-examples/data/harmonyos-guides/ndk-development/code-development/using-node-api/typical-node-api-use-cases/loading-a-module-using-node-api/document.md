# Loading a Module Using Node-API

You can use **napi\_load\_module\_with\_info** to load a module. After the module is loaded, you can use **napi\_get\_property** to obtain the variables of the module or use **napi\_get\_named\_property** to obtain the functions of the module. The **napi\_load\_module\_with\_info** API can be used in a [new ArkTS runtime environment](../creating-an-arkts-runtime-environment-using-node-api/document.md) created by the **napi\_create\_ark\_runtime** API.

#### Function Description

napi\_status napi\_load\_module\_with\_info(napi\_env env, const char\* path, const char\* module\_info, napi\_value\* result);

| Parameter | Description |
| :-- | :-- |
| env | Current VM environment. |
| path | Path of the file or name of the module to load. |
| module\_info | Path composed of **bundleName** and **moduleName**. |
| result | Module loaded. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/gdDy2B5ERfy2b6leqsSc4Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062132Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=66049CABA902F61D8CD9F376BA48F8DE3EB48500FA4CFE03ED4D057BA603AC84)

1.  **bundleName** indicates the project name configured in **AppScope/app.json5**.
2.  **moduleName** must be set to the module name configured in the **module.json5** file in the HAP to which the module belongs.

#### Scenarios Supported by napi\_load\_module\_with\_info

| Scenario | Description | Description |
| :-- | :-- | :-- |
| Local project module | Load the module file. | The file path must start with **moduleName**. |
| Local project module | Load the HAR module name. | \- |
| Remote package | Load the remote HAR module name. | \- |
| Remote package | Load the ohpm package name. | \- |
| API | Load **@ohos.** or **@system.**. | \- |
| Native library | Load **libNativeLibrary.so**. | \- |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/Y9mRYRcVRFOWPJ5P33DgXw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062132Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2A8150CAD2715A820022050CE4D56B30261D654467EFFD6F4028A49DCD314E18)

1.  The module name to be loaded is the entry file, generally **index.ets/ts**, of the module.
2.  To load a HAR to another HAR, ensure that **module\_info** is correct. The value of **moduleName** must be that of the HAP or HSP.
3.  If a third-party package is directly or indirectly used in a HAP/HSP and the third-party package has loaded another module, for example, module A, using **napi\_load\_module\_with\_info**, you must add module A in the dependencies of the HAP/HSP.
4.  Calling this API in the signal function is insecure. Direct calling may cause stack overflow.

#### Exception Scenarios

1.  When no file is found in the package or the **build-profile.json5** configuration is incorrect during module loading, the error code **napi\_generic\_failure** is returned and an error log is printed.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/LRuTknnnSECsODXTr6Y-uw/en-us_image_0000002568685011.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062132Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D3C88E6EA0FC0670FE9710729E88AF6688A1BEC18577DC7E5AF66AC74B827205)
    
2.  The module loading fails due to unexpected behavior on the system side, and **cppcrash** is thrown.
    

#### How to Use

-   **Loading a module file**

Load a module from a file, as shown in the following ArkTS code.

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
    
2.  Call **napi\_load\_module\_with\_info** to load the **Test.ets** file, call the **test()** function, and obtain the variable values.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/mGzsWs9ZTB2ljWlsHP5SzA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062132Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A33484357103AFC37A1E4DBEC7262A1F77928DD04C9CA3097E1FFE78986870E0)
    
    When a module file is loaded with **useNormalizedOHMUrl** enabled (the **useNormalizedOHMUrl** field of **strictMode** in the application's **build-profile.json5** file in the same directory as **entry** in the project is set to **true**):
    
    1.  **bundleName** does not affect the loading logic. The corresponding HAP in the process is intelligently indexed based on the module name. For example, the module can be successfully loaded if **bundleName** is set to **com.example.application1** while the actual bundle name of the project is **com.example.application**.
    2.  The file path must start with **packageName**, which is the value of **name** in the **oh-package.json5** file of the module.
    
     static napi\_value loadModule(napi\_env env, napi\_callback\_info info) {
         napi\_value result;
         // 1. Call napi\_load\_module\_with\_info to load the module from the Test.ets file.
         napi\_status status = napi\_load\_module\_with\_info(env, "entry/src/main/ets/Test", "com.example.application/entry", &result);
         if (status != napi\_ok) {
             return nullptr;
         }
    
         napi\_value testFn;
         // 2. Call napi\_get\_named\_property to obtain the test function.
         napi\_get\_named\_property(env, result, "test", &testFn);
         // 3. Call napi\_call\_function to invoke the test function.
         napi\_call\_function(env, result, testFn, 0, nullptr, nullptr);
    
         napi\_value value;
         napi\_value key;
         std::string keyStr = "value";
         napi\_create\_string\_utf8(env, keyStr.c\_str(), keyStr.size(), &key);
         // 4. Call napi\_get\_property to obtain a variable value.
         napi\_get\_property(env, result, key, &value);
         return result;
     }
    

-   **Loading a source code HAR module**

The **Index.ets** file in the HAR is as follows:

//library Index.ets
let value = 123;
function test() {
    console.info("Hello HarmonyOS");
}
export {value, test};

1.  Configure **dependencies** in the **oh-package.json5** file.
    
    {
        "dependencies": {
            "library": "file:../library"
        }
    }
    
2.  Configure **build-profile.json5** for the module that uses **library**.
    
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
    
3.  Call **napi\_load\_module\_with\_info** to load **library**, call the **test** function, and obtain the variable values.
    
    static napi\_value loadModule(napi\_env env, napi\_callback\_info info) {
        napi\_value result;
        // 1. Call napi\_load\_module\_with\_info to load library.
        napi\_status status = napi\_load\_module\_with\_info(env, "library", "com.example.application/entry", &result);
        if (status != napi\_ok) {
           return nullptr;
        }
    
        napi\_value testFn;
        // 2. Call napi\_get\_named\_property to obtain the test function.
        napi\_get\_named\_property(env, result, "test", &testFn);
        // 3. Call napi\_call\_function to invoke the test function.
        status = napi\_call\_function(env, result, testFn, 0, nullptr, nullptr);
        if (status != napi\_ok) {
           return nullptr;
        }
    
        napi\_value value;
        napi\_value key;
        std::string keyStr = "value";
        napi\_create\_string\_utf8(env, keyStr.c\_str(), keyStr.size(), &key);
        // 4. Call napi\_get\_property to obtain a variable value.
        status = napi\_get\_property(env, result, key, &value);
        if (status != napi\_ok) {
           return nullptr;
        }
        return result;
    }
    

-   **Loading a source code HSP module**

The **Index.ets** file in the HSP is as follows:

//hsp Index.ets
let value = 123;
function test() {
    console.info("Hello World");
}
export {value, test};

1.  Configure **dependencies** in the **oh-package.json5** file.
    
    {
        "dependencies": {
            "hsp": "file:../hsp"
        }
    }
    
2.  Configure **build-profile.json5** for the module that uses the HSP.
    
    {
        "buildOption" : {
            "arkOptions" : {
                "runtimeOnly" : {
                    "packages": \[
                        "hsp"
                    \]
                }
            }
        }
    }
    
3.  Call **napi\_load\_module\_with\_info** to load the HSP, call the **test** function, and obtain the **value** variable.
    
    static napi\_value loadModule(napi\_env env, napi\_callback\_info info) {
        napi\_value result;
        // 1. Call napi\_load\_module\_with\_info to load the HSP.
        napi\_status status = napi\_load\_module\_with\_info(env, "hsp", "com.example.application/entry", &result);
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
        // 4. Call napi\_get\_property to obtain a variable value.
        status = napi\_get\_property(env, result, key, &value);
        if (status != napi\_ok) {
            return nullptr;
        }
        return result;
    }
    

-   **Loading a remote HAR module name**

1.  Configure **dependencies** in the **oh-package.json5** file.
    
    {
        "dependencies": {
            "@ohos/hypium": "1.0.16"
        }
    }
    
2.  Configure **build-profile.json5** for the module that uses @ohos/hypium.
    
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
    
3.  Call **napi\_load\_module\_with\_info** to load **@ohos/hypium** and obtain the **DEFAULT** variable.
    
    static napi\_value loadModule(napi\_env env, napi\_callback\_info info) {
        napi\_value result;
        // 1. Call napi\_load\_module\_with\_info to load @ohos/hypium.
        napi\_status status = napi\_load\_module\_with\_info(env, "@ohos/hypium", "com.example.application/entry", &result);
        if (status != napi\_ok) {
           return nullptr;
        }
    
        napi\_value key;
        std::string keyStr = "DEFAULT";
        napi\_create\_string\_utf8(env, keyStr.c\_str(), keyStr.size(), &key);
        // 2. Call napi\_get\_property to obtain the DEFAULT variable.
        napi\_value defaultValue;
        napi\_get\_property(env, result, key, &defaultValue);
        return result;
    }
    

-   **Loading an ohpm package name**

1.  Configure **dependencies** in the **oh-package.json5** file.
    
    {
        "dependencies": {
            "json5": "^2.2.3"
        }
    }
    
2.  Configure **build-profile.json5** for the module that uses the .json5 file.
    
    {
        "buildOption" : {
            "arkOptions" : {
                "runtimeOnly" : {
                    "packages": \[
                        "json5"
                    \]
                }
            }
        }
    }
    
3.  Call **napi\_load\_module\_with\_info** to load **json5** and call the **stringify** function.
    
    static napi\_value loadModule(napi\_env env, napi\_callback\_info info) {
        napi\_value result;
        // 1. Call napi\_load\_module\_with\_info to load json5.
        napi\_status status = napi\_load\_module\_with\_info(env, "json5", "com.example.application/entry", &result);
        if (status != napi\_ok) {
           return nullptr;
        }
    
        napi\_value key;
        std::string keyStr = "default";
        napi\_create\_string\_utf8(env, keyStr.c\_str(), keyStr.size(), &key);
        // 2. Call napi\_get\_property to obtain the default object.
        napi\_value defaultValue;
        napi\_get\_property(env, result, key, &defaultValue);
    
        napi\_value stringifyFn;
        // 3. Call napi\_get\_named\_property to obtain the stringify function.
        napi\_get\_named\_property(env, defaultValue, "stringify", &stringifyFn);
        // 4. Call napi\_call\_function to invoke the stringify function.
        napi\_value argStr;
        std::string text = "call json5 stringify";
        napi\_create\_string\_utf8(env, text.c\_str(), text.size(), &argStr);
        napi\_value args\[1\] = {argStr};
    
        napi\_value returnValue;
        napi\_call\_function(env, defaultValue, stringifyFn, 1, args, &returnValue);
        return result;
    }
    

-   **Loading an API module**

static napi\_value loadModule(napi\_env env, napi\_callback\_info info) {
    // 1. Call napi\_load\_module\_with\_info to load the @ohos.hilog module.
    napi\_value result;
    napi\_status status = napi\_load\_module\_with\_info(env, "@ohos.hilog", nullptr, &result);
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

-   **Loading a native library**

The **index.d.ts** file of **libentry.so** is as follows:

// index.d.ts
export const add: (a: number, b: number) => number;

1.  Configure **dependencies** in the **oh-package.json5** file.
    
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
    
3.  Call **napi\_load\_module\_with\_info** to load **libentry.so** and call the **add** function.
    
    static constexpr int INT\_NUM\_2 = 2; // Integer 2
    static constexpr int INT\_NUM\_3 = 3; // Integer 3
    
    static napi\_value loadModule(napi\_env env, napi\_callback\_info info) {
        napi\_value result;
        // 1. Call napi\_load\_module\_with\_info to load libentry.so.
        napi\_status status = napi\_load\_module\_with\_info(env, "libentry.so", "com.example.application/entry", &result);
        if (status != napi\_ok) {
            return nullptr;
        }
    
        napi\_value addFn;
        // 2. Call napi\_get\_named\_property to obtain the add function.
        napi\_get\_named\_property(env, result, "add", &addFn);
    
        napi\_value a;
        napi\_value b;
        napi\_create\_int32(env, INT\_NUM\_2, &a);
        napi\_create\_int32(env, INT\_NUM\_3, &b);
        napi\_value args\[2\] = {a, b};
        // 3. Call napi\_call\_function to invoke the add function.
        napi\_value returnValue;
        napi\_call\_function(env, result, addFn, INT\_NUM\_2, args, &returnValue);
        return result;
    }
    

-   **Loading another HAR module to a HAR**

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
    
3.  Call **napi\_load\_module\_with\_info** to load **har2** to **har1**, call the **test** function, and obtain the variable **value**.
    
    static napi\_value loadModule(napi\_env env, napi\_callback\_info info) {
        napi\_value result;
        // 1. Call napi\_load\_module\_with\_info to load har2. Note that moduleName is that of the HAP where the module is located.
        napi\_status status = napi\_load\_module\_with\_info(env, "har2", "com.example.application/entry", &result);
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
        // 4. Call napi\_get\_property to obtain a variable value.
        status = napi\_get\_property(env, result, key, &value);
        if (status != napi\_ok) {
            return nullptr;
        }
        return result;
    }
