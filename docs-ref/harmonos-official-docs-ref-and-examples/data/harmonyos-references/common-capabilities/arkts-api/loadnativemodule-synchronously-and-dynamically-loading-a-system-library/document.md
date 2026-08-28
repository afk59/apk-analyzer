# loadNativeModule (Synchronously and Dynamically Loading a System Library)

This module provides the capability of synchronously and dynamically loading a system library.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/gRPU5j7vTbalXhTScx1LQQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062526Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CC09802A0FCF1BF36C7439B35FB8CE1D5D271FE5CAB78C1002657CEF1EE935FD)

The initial APIs of this module are supported since API version 12. Newly added APIs will be marked with a superscript to indicate their earliest API version.

The APIs of this module can be used only in the stage model.

#### loadNativeModule

loadNativeModule(moduleName: string): Object

The **loadNativeModule** API is used to synchronously and dynamically load a native module, that is, only load the required module at a time. Using this API increases the time for loading the .so file. You need to evaluate the impact on the functionality.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1/v3/eOgwBSQxQVadMlwbrCk-wA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062526Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D22E5B7525869E08A2A23C3679F7733BEA89BF041E8B657EBC4D545B153A3163)

The name of the module loaded by **loadNativeModule** is the name provided in **dependencies** in the **oh-package.json5** file of the dependency.

**loadNativeModule** can be used only to load native modules in the UI main thread.

Dependencies must be configured for the API call regardless of whether the parameter is a constant string or variable expression.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| moduleName | string | Yes | Name of the module to load. |

**Return value**

| Type | Description |
| :-- | :-- |
| Object | Default export of the native module. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../api-reference-overview/universal-error-codes/document.md) and [Utils Error Codes](../../../application-framework/arkts/error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | The parameter check failed. |
| 10200301 | Loading native module failed. |

**Scenarios supported by loadNativeModule**

| Scenario | Example |
| :-- | :-- |
| System library module | Load **@ohos.** or **@system.**. |
| Native module in an application | Load **libNativeLibrary.so**. |

**Example 1**: Loading a System Library Module to a HAP

let hilog: ESObject = loadNativeModule("@ohos.hilog");
hilog.info(0, "testTag", "loadNativeModule ohos.hilog success");

**Example 2**: Loading a Native Library to a HAP

The **index.d.ts** file of **libentry.so** is as follows:

//index.d.ts
export const add: (a: number, b: number) => number;

1.  When loading a local .so library, configure **dependencies** in the **oh-package.json5** file. For details, see [Fields in the Module-level oh-package.json5 File](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/ide-oh-package-json5#en-us_topic_0000001792256137_oh-packagejson5-字段说明).

{
  "dependencies": {
    "libentry.so": "file:./src/main/cpp/types/libentry"
  }
}

1.  Configure the module-level **build-profile.json5** file. For details, see [Module-level build-profile.json5 File](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/ide-hvigor-build-profile).

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
