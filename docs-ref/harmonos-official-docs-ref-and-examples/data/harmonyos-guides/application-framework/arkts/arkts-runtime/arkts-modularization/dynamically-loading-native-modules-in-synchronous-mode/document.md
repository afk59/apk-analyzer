# Dynamically Loading Native Modules in Synchronous Mode

The **loadNativeModule** API is used to dynamically load native modules in synchronous mode. Using this API increases the time for loading the .so file. You need to evaluate the impact on the functionality.

#### API Description

loadNativeModule(moduleName: string): Object;

| Parameter | Description |
| :-- | :-- |
| moduleName | Name of the module to load. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/V5hEStn_QjSK1NfQVOjK9g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061925Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FAEE624A29AFDA57BE1A1226E68873961A61A4F7CD3A2D686FF057293EA768EB)

-   The name of the module loaded by **loadNativeModule** is the name provided in **dependencies** in the **oh-package.json5** file of the dependency.
    
-   **loadNativeModule** must be called in the UI main thread.
    
-   Dependencies must be configured for the API call regardless of whether the parameter is a constant string or variable expression.
    

#### Supported Scenarios

| Scenario | Example |
| :-- | :-- |
| System library module | Load **@ohos.** or **@system.**. |
| Native module in an application | Load **libNativeLibrary.so**. |

#### Usage Example

-   **Loading a system library module to a HAP**

let hilog: ESObject = loadNativeModule("@ohos.hilog");
hilog.info(0, "testTag", "loadNativeModule ohos.hilog success");

-   **Loading a native library to a HAP**

The **index.d.ts** file of **libentry.so** is as follows:

//index.d.ts
export const add: (a: number, b: number) => number;

1.  When loading a local .so library, configure dependencies in the **oh-package.json5** file.

{
  "dependencies": {
    "libentry.so": "file:./src/main/cpp/types/libentry"
  }
}

1.  Configure the **build-profile.json5** file.

{
  "buildOption": {
    "arkOptions": {
      "runtimeOnly": {
        "packages": \[
          "libentry.so"
        \]
      }
    }
  }
}

1.  Use **loadNativeModule** to load **libentry.so** and call the **add** function.

let module: ESObject = loadNativeModule("libentry.so");
let sum: number = module.add(1, 2);
