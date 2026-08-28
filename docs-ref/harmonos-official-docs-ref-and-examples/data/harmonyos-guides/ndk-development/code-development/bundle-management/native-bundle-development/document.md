# Native Bundle Development

#### When to Use

Use the native bundle APIs to obtain application information.

#### Available APIs

The following table lists the common APIs. For details, see [Native\_Bundle](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-bundle).

| API | Description |
| :-- | :-- |
| [OH\_NativeBundle\_GetCurrentApplicationInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-interface-bundle-h#oh_nativebundle_getcurrentapplicationinfo) | Obtains the information about the current application. |
| [OH\_NativeBundle\_GetAppId](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-interface-bundle-h#oh_nativebundle_getappid) | Obtains the appId information about the application. |
| [OH\_NativeBundle\_GetAppIdentifier](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-interface-bundle-h#oh_nativebundle_getappidentifier) | Obtains the appIdentifier information about the application. |
| [OH\_NativeBundle\_GetMainElementName](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-interface-bundle-h#oh_nativebundle_getmainelementname) | Obtains the entry information of the application. |
| [OH\_NativeBundle\_GetCompatibleDeviceType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-interface-bundle-h#oh_nativebundle_getcompatibledevicetype) | Obtains the compatible device type of the application. |
| [OH\_NativeBundle\_IsDebugMode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-interface-bundle-h#oh_nativebundle_isdebugmode) | Queries the debug mode of the application. This API is supported since API version 20. |
| [OH\_NativeBundle\_GetModuleMetadata](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-interface-bundle-h#oh_nativebundle_getmodulemetadata) | Obtains the metadata information of the application. This API is supported since API version 20. |
| [OH\_NativeBundle\_GetAbilityResourceInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-interface-bundle-h#oh_nativebundle_getabilityresourceinfo) | Obtains a list of ability resource information that supports opening a specific file type. This API is supported since API version 21. |

#### How to Develop

\*\*1. Create a project.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/WuniKpioR-mKx4-u1vKyhQ/en-us_image_0000002537925242.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062135Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C9ECE48FCAEA6F1796C30A37F15582DAC34CC69D4F954AC712486460A7C6EDD2)

\*\*2. Add dependencies.

After the project is created, the **cpp** directory is created in the project directory. In the **cpp** directory, there are files such as **types/libentry/index.d.ts**, **napi\_init.cpp**, and **CMakeLists.txt**.

1.  Open the **src/main/cpp/CMakeLists.txt** file, and add **libbundle\_ndk.z.so** to **target\_link\_libraries**.
    
    target\_link\_libraries(entry PUBLIC libace\_napi.z.so libbundle\_ndk.z.so)
    
2.  Open the **src/main/cpp/napi\_init.cpp** file, and add the header file.
    
    // Include the header file required for napi.
    #include "napi/native\_api.h"
    // Include the header file required for native APIs.
    #include "bundle/ability\_resource\_info.h"
    #include "bundle/native\_interface\_bundle.h"
    // Include the standard library for the free() function.
    #include <cstdlib>
    

\*\*3. Modify the source file.

1.  When the **src/main/cpp/napi\_init.cpp** file is opened, **Init** is called to initialize the API.
    
    EXTERN\_C\_START
    static napi\_value Init(napi\_env env, napi\_value exports)
    {
        napi\_property\_descriptor desc\[\] = {
            { "add", nullptr, Add, nullptr, nullptr, nullptr, napi\_default, nullptr },
            // Add the getCurrentApplicationInfo method.
            { "getCurrentApplicationInfo", nullptr, GetCurrentApplicationInfo, nullptr,
                nullptr, nullptr, napi\_default, nullptr},
            // Add the getAppId method.
            { "getAppId", nullptr, GetAppId, nullptr, nullptr, nullptr, napi\_default, nullptr},
            // Add the getAppIdentifier method.
            { "getAppIdentifier", nullptr, GetAppIdentifier, nullptr, nullptr, nullptr, napi\_default, nullptr},
            // Add the getMainElementName method.
            { "getMainElementName", nullptr, GetMainElementName, nullptr, nullptr, nullptr, napi\_default, nullptr},
            // Add the getCompatibleDeviceType method.
            { "getCompatibleDeviceType", nullptr, GetCompatibleDeviceType, nullptr,
                nullptr, nullptr, napi\_default, nullptr},
            // Add the isDebugMode method.
            { "isDebugMode", nullptr, IsDebugMode, nullptr, nullptr, nullptr, napi\_default, nullptr},
            // Add the getModuleMetadata method.
            { "getModuleMetadata", nullptr, GetModuleMetadata, nullptr, nullptr, nullptr, napi\_default, nullptr},
            // Add the getAbilityResourceInfo method.
            { "getAbilityResourceInfo", nullptr, GetAbilityResourceInfo, nullptr, nullptr, nullptr, napi\_default, nullptr}
        };
        napi\_define\_properties(env, exports, sizeof(desc) / sizeof(desc\[0\]), desc);
        return exports;
    }
    EXTERN\_C\_END
    
2.  Obtain the native bundle information object from the **src/main/cpp/napi\_init.cpp** file and convert it to a JavaScript bundle information object. In this way, you can obtain the application information on the JavaScript side.
    
    static napi\_value GetCurrentApplicationInfo(napi\_env env, napi\_callback\_info info)
    {
        // Call the native API to obtain the application information.
        OH\_NativeBundle\_ApplicationInfo nativeApplicationInfo = OH\_NativeBundle\_GetCurrentApplicationInfo();
        napi\_value result = nullptr;
        napi\_create\_object(env, &result);
        // Convert the bundle name obtained by calling the native API to the bundleName property in the JavaScript object.
        napi\_value bundleName;
        napi\_create\_string\_utf8(env, nativeApplicationInfo.bundleName, NAPI\_AUTO\_LENGTH, &bundleName);
        napi\_set\_named\_property(env, result, "bundleName", bundleName);
        // Convert the fingerprint information obtained by calling the native API to the fingerprint property in the JavaScript object.
        napi\_value fingerprint;
        napi\_create\_string\_utf8(env, nativeApplicationInfo.fingerprint, NAPI\_AUTO\_LENGTH, &fingerprint);
        napi\_set\_named\_property(env, result, "fingerprint", fingerprint);
        // To prevent memory leak, manually release the memory.
        free(nativeApplicationInfo.bundleName);
        free(nativeApplicationInfo.fingerprint);
        return result;
    }
    
    static napi\_value GetAppId(napi\_env env, napi\_callback\_info info)
    {
        // Call the native API to obtain the appId.
        char\* appId = OH\_NativeBundle\_GetAppId();
        // Convert the appId obtained by calling the native API to nAppId and return it.
        napi\_value nAppId;
        napi\_create\_string\_utf8(env, appId, NAPI\_AUTO\_LENGTH, &nAppId);
        // To prevent memory leak, manually release the memory.
        free(appId);
        return nAppId;
    }
    
    static napi\_value GetAppIdentifier(napi\_env env, napi\_callback\_info info)
    {
        // Call the native API to obtain the appIdentifier.
        char\* appIdentifier = OH\_NativeBundle\_GetAppIdentifier();
        // Convert the appIdentifier obtained by calling the native API to nAppIdentifier and return it.
        napi\_value nAppIdentifier;
        napi\_create\_string\_utf8(env, appIdentifier, NAPI\_AUTO\_LENGTH, &nAppIdentifier);
        // To prevent memory leak, manually release the memory.
        free(appIdentifier);
        return nAppIdentifier;
    }
    
    static napi\_value GetMainElementName(napi\_env env, napi\_callback\_info info)
    {
        // Call the native API to obtain the application entry information.
        OH\_NativeBundle\_ElementName elementName = OH\_NativeBundle\_GetMainElementName();
        napi\_value result = nullptr;
        napi\_create\_object(env, &result);
        // Convert the bundle name obtained by calling the native API to the bundleName property in the JavaScript object.
        napi\_value bundleName;
        napi\_create\_string\_utf8(env, elementName.bundleName, NAPI\_AUTO\_LENGTH, &bundleName);
        napi\_set\_named\_property(env, result, "bundleName", bundleName);
        // Convert the module name obtained by calling the native API to the moduleName property in the JavaScript object.
        napi\_value moduleName;
        napi\_create\_string\_utf8(env, elementName.moduleName, NAPI\_AUTO\_LENGTH, &moduleName);
        napi\_set\_named\_property(env, result, "moduleName", moduleName);
        // Convert the ability name obtained by calling the native API to the abilityName property in the JavaScript object.
        napi\_value abilityName;
        napi\_create\_string\_utf8(env, elementName.abilityName, NAPI\_AUTO\_LENGTH, &abilityName);
        napi\_set\_named\_property(env, result, "abilityName", abilityName);
        // To prevent memory leak, manually release the memory.
        free(elementName.bundleName);
        free(elementName.moduleName);
        free(elementName.abilityName);
        return result;
    }
    
    static napi\_value GetCompatibleDeviceType(napi\_env env, napi\_callback\_info info)
    {
        // Call the native API to obtain the device type.
        char\* deviceType = OH\_NativeBundle\_GetCompatibleDeviceType();
        // Convert the device type obtained by calling the native API to nDeviceType and return it.
        napi\_value nDeviceType;
        napi\_create\_string\_utf8(env, deviceType, NAPI\_AUTO\_LENGTH, &nDeviceType);
        // To prevent memory leak, manually release the memory.
        free(deviceType);
        return nDeviceType;
    }
    
    static napi\_value IsDebugMode(napi\_env env, napi\_callback\_info info)
    {
        bool isDebug = false;
        // Call the native API to obtain the DebugMode information of the application. This API is supported since API version 20.
        bool isSuccess = OH\_NativeBundle\_IsDebugMode(&isDebug);
        // Throw an exception if the native API call fails
        if (isSuccess == false) {
            napi\_throw\_error(env, nullptr, "call failed");
            return nullptr;
        }
        // Convert the debug information obtained by calling the native API to debug and return it.
        napi\_value debug;
        napi\_get\_boolean(env, isDebug, &debug);
        return debug;
    }
    
    static napi\_value GetModuleMetadata(napi\_env env, napi\_callback\_info info)
    {
        size\_t moduleCount = 0;
        // Call the native API to obtain the metadata of the application. This API is supported since API version 20.
        OH\_NativeBundle\_ModuleMetadata\* modules = OH\_NativeBundle\_GetModuleMetadata(&moduleCount);
        if (modules == nullptr || moduleCount == 0) {
            napi\_throw\_error(env, nullptr, "no metadata found");
            return nullptr;
        }
        napi\_value result;
        napi\_create\_array(env, &result);
        for (size\_t i = 0; i < moduleCount; i++) {
            napi\_value moduleObj;
            napi\_create\_object(env, &moduleObj);
            // Convert the module name obtained by calling the native API to the moduleName property in the JavaScript object.
            napi\_value moduleName;
            napi\_create\_string\_utf8(env, modules\[i\].moduleName, NAPI\_AUTO\_LENGTH, &moduleName);
            napi\_set\_named\_property(env, moduleObj, "moduleName", moduleName);
            napi\_value metadataArray;
            napi\_create\_array(env, &metadataArray);
            for (size\_t j = 0; j < modules\[i\].metadataArraySize; j++) {
                napi\_value metadataObj;
                napi\_create\_object(env, &metadataObj);
                napi\_value name;
                napi\_value value;
                napi\_value resource;
                napi\_create\_string\_utf8(env, modules\[i\].metadataArray\[j\].name, NAPI\_AUTO\_LENGTH, &name);
                napi\_create\_string\_utf8(env, modules\[i\].metadataArray\[j\].value, NAPI\_AUTO\_LENGTH, &value);
                napi\_create\_string\_utf8(env, modules\[i\].metadataArray\[j\].resource, NAPI\_AUTO\_LENGTH, &resource);
                // Convert the metadata name obtained by calling the native API to the name property in the JavaScript object.
                napi\_set\_named\_property(env, metadataObj, "name", name);
                // Convert the metadata value obtained by calling the native API to the value property in the JavaScript object.
                napi\_set\_named\_property(env, metadataObj, "value", value);
                // Convert the metadata resource obtained by calling the native API to the resource property in the JavaScript object.
                napi\_set\_named\_property(env, metadataObj, "resource", resource);
                napi\_set\_element(env, metadataArray, j, metadataObj);
            }
            napi\_set\_named\_property(env, moduleObj, "metadata", metadataArray);
            napi\_set\_element(env, result, i, moduleObj);
        }
        // To prevent memory leak, manually release the memory.
        for (size\_t i = 0; i < moduleCount; i++) {
            free(modules\[i\].moduleName);
            for (size\_t j = 0; j < modules\[i\].metadataArraySize; j++) {
                free(modules\[i\].metadataArray\[j\].name);
                free(modules\[i\].metadataArray\[j\].value);
                free(modules\[i\].metadataArray\[j\].resource);
            }
            free(modules\[i\].metadataArray);
        }
        free(modules);
        return result;
    }
    
    static void AddDefaultApp(napi\_env env,
        napi\_value &infoObj,
        OH\_NativeBundle\_AbilityResourceInfo\* temp)
    {
        bool isDefaultApp = true;
        // This API is supported since API version 21.
        OH\_NativeBundle\_CheckDefaultApp(temp, &isDefaultApp);
        napi\_value defaultAppValue;
        napi\_get\_boolean(env, isDefaultApp, &defaultAppValue);
        napi\_set\_named\_property(env, infoObj, "isDefaultApp", defaultAppValue);
    }
    
    static void AddAppIndex(napi\_env env,
        napi\_value &infoObj,
        OH\_NativeBundle\_AbilityResourceInfo\* temp)
    {
        int appIndex = -1;
        // This API is supported since API version 21.
        OH\_NativeBundle\_GetAppIndex(temp, &appIndex);
        napi\_value appIndexValue;
        napi\_create\_int32(env, appIndex, &appIndexValue);
        napi\_set\_named\_property(env, infoObj, "appIndex", appIndexValue);
    }
    
    static void AddLabel(napi\_env env,
        napi\_value &infoObj,
        OH\_NativeBundle\_AbilityResourceInfo\* temp)
    {
        char \*label = nullptr;
        // This API is supported since API version 21.
        OH\_NativeBundle\_GetLabel(temp, &label);
        napi\_value labelValue;
        if (label) {
            napi\_create\_string\_utf8(env, label, NAPI\_AUTO\_LENGTH, &labelValue);
            free(label);
        } else {
            napi\_get\_null(env, &labelValue);
        }
        napi\_set\_named\_property(env, infoObj, "label", labelValue);
    }
    
    static void AddBundleName(napi\_env env,
        napi\_value &infoObj,
        OH\_NativeBundle\_AbilityResourceInfo\* temp)
    {
        char \*bundleName = nullptr;
        // This API is supported since API version 21.
        OH\_NativeBundle\_GetBundleName(temp, &bundleName);
        napi\_value bundleNameValue;
        if (bundleName) {
            napi\_create\_string\_utf8(env, bundleName, NAPI\_AUTO\_LENGTH, &bundleNameValue);
            free(bundleName);
        } else {
            napi\_get\_null(env, &bundleNameValue);
        }
        napi\_set\_named\_property(env, infoObj, "bundleName", bundleNameValue);
    }
    
    static void AddModuleName(napi\_env env,
        napi\_value &infoObj,
        OH\_NativeBundle\_AbilityResourceInfo\* temp)
    {
        char \*moduleName = nullptr;
        // This API is supported since API version 21.
        OH\_NativeBundle\_GetModuleName(temp, &moduleName);
        napi\_value moduleNameValue;
        if (moduleName) {
            napi\_create\_string\_utf8(env, moduleName, NAPI\_AUTO\_LENGTH, &moduleNameValue);
            free(moduleName);
        } else {
            napi\_get\_null(env, &moduleNameValue);
        }
        napi\_set\_named\_property(env, infoObj, "moduleName", moduleNameValue);
    }
    
    static void AddAbilityName(napi\_env env,
        napi\_value &infoObj,
        OH\_NativeBundle\_AbilityResourceInfo\* temp)
    {
        char \*abilityName = nullptr;
        // This API is supported since API version 21.
        OH\_NativeBundle\_GetAbilityName(temp, &abilityName);
        napi\_value abilityNameValue;
        if (abilityName) {
            napi\_create\_string\_utf8(env, abilityName, NAPI\_AUTO\_LENGTH, &abilityNameValue);
            free(abilityName);
        } else {
            napi\_get\_null(env, &abilityNameValue);
        }
        napi\_set\_named\_property(env, infoObj, "abilityName", abilityNameValue);
    }
    
    static void GetDrawableDescriptor(
        OH\_NativeBundle\_AbilityResourceInfo\* temp)
    {
        ArkUI\_DrawableDescriptor \*rawDrawable = nullptr;
        // This API is supported since API version 21.
        OH\_NativeBundle\_GetDrawableDescriptor(temp, &rawDrawable);
        if (rawDrawable) {
            // Use the ArkUI\_DrawableDescriptor object to draw an icon.
        }
    }
    
    static void AssemblyAbilityResourceInfo(napi\_env env,
        napi\_value &infoObj,
        OH\_NativeBundle\_AbilityResourceInfo\* temp)
    {
        // 1. Add the default app.
        AddDefaultApp(env, infoObj, temp);
        // 2. Add an app index.
        AddAppIndex(env, infoObj, temp);
        // 3. Add a label.
        AddLabel(env, infoObj, temp);
        // 4. Add a bundle name.
        AddBundleName(env, infoObj, temp);
        // 5. Add a module name.
        AddModuleName(env, infoObj, temp);
        // 6. Add an ability name.
        AddAbilityName(env, infoObj, temp);
        // 7. Obtain the ArkUI\_DrawableDescriptor object.
        GetDrawableDescriptor(temp);
    }
    
    static napi\_value GetAbilityResourceInfo(napi\_env env, napi\_callback\_info info)
    {
        size\_t argc = 1;
        napi\_value args\[1\];
        napi\_status status;
        // Obtain the parameters passed in.
        status = napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);
        if (status != napi\_ok || argc < 1) {
            napi\_throw\_error(env, nullptr, "Invalid arguments. Expected fileType string.");
            return nullptr;
        }
        // Check whether the parameter is a string.
        napi\_valuetype valuetype;
        status = napi\_typeof(env, args\[0\], &valuetype);
        if (status != napi\_ok || valuetype != napi\_string) {
            napi\_throw\_error(env, nullptr, "Argument must be a string");
            return nullptr;
        }
        // Obtain the string.
        char fileType\[256\] = {0}; // Assume that the file type does not exceed 255 characters.
        size\_t strLen;
        status = napi\_get\_value\_string\_utf8(env, args\[0\], fileType, sizeof(fileType) - 1, &strLen);
        if (status != napi\_ok) {
            napi\_throw\_error(env, nullptr, "Failed to get fileType string");
            return nullptr;
        }
        size\_t infosCount = 0;
        OH\_NativeBundle\_AbilityResourceInfo \*infos = nullptr;
        // Call the native API to obtain the component resource information using the passed-in fileType. This API is supported since API version 21.
        BundleManager\_ErrorCode ret = OH\_NativeBundle\_GetAbilityResourceInfo(fileType, &infos, &infosCount);
        if (ret == BUNDLE\_MANAGER\_ERROR\_CODE\_PERMISSION\_DENIED) {
            napi\_throw\_error(env, nullptr, "BUNDLE\_MANAGER\_ERROR\_CODE\_PERMISSION\_DENIED");
            return nullptr;
        }
        if (infos == nullptr || infosCount == 0) {
            napi\_throw\_error(env, nullptr, "no metadata found");
            return nullptr;
        }
        napi\_value result;
        napi\_create\_array(env, &result);
        for (size\_t i = 0; i < infosCount; i++) {
            auto temp = (OH\_NativeBundle\_AbilityResourceInfo \*)((char \*)infos + OH\_NativeBundle\_GetSize() \* i);
            napi\_value infoObj;
            napi\_create\_object(env, &infoObj);
            AssemblyAbilityResourceInfo(env, infoObj, temp);
            napi\_set\_element(env, result, i, infoObj);
        }
        // Release the memory. This API is supported since API version 21.
        OH\_AbilityResourceInfo\_Destroy(infos, infosCount);
        return result;
    }
    

\*\*4. Expose APIs.

1.  Declare the exposed APIs in the **src/main/cpp/types/libentry/Index.d.ts** file.
    
    export const add: (a: number, b: number) => number;
    export const getCurrentApplicationInfo: () => object;   // Add the exposed API getCurrentApplicationInfo.
    export const getAppId: () => string;                    // Add the exposed API getAppId.
    export const getAppIdentifier: () => string;            // Add the exposed API getAppIdentifier.
    export const getMainElementName: () => object;          // Add the exposed API getMainElementName.
    export const getCompatibleDeviceType: () => string;     // Add the exposed API getCompatibleDeviceType.
    export const isDebugMode: () => string;                 // Add the exposed API isDebugMode.
    export const getModuleMetadata: () => object;           // Add the exposed API getModuleMetadata.
    export const getAbilityResourceInfo: (fileType: string) => object;      // Add the exposed API getAbilityResourceInfo.
    

\*\*5. Call APIs on the JavaScript side.

1.  Open the **src/main/ets/pages/index.ets** file, and import **libentry.so**.
    
2.  Call the native APIs to print the obtained information. An example is as follows:
    
    import { hilog } from '@kit.PerformanceAnalysisKit';
    import testNapi from 'libentry.so';
    
    const DOMAIN = 0x0000;
    
    @Entry
    @Component
    struct Index {
      @State message: string = 'Hello World';
    
      build() {
        Row() {
          Column() {
            Text(this.message)
              .fontSize($r('app.float.page\_text\_font\_size'))
              .fontWeight(FontWeight.Bold)
              .onClick(() => {
                this.message = 'Welcome';
                hilog.info(DOMAIN, 'testTag', 'Test NAPI 2 + 3 = %{public}d', testNapi.add(2, 3));
                let appInfo = testNapi.getCurrentApplicationInfo();
                console.info("bundleNative getCurrentApplicationInfo success, data is " + JSON.stringify(appInfo));
                let appId = testNapi.getAppId();
                console.info("bundleNative getAppId success, appId is " + appId);
                let appIdentifier = testNapi.getAppIdentifier();
                console.info("bundleNative getAppIdentifier success, appIdentifier is " + appIdentifier);
                let mainElement = testNapi.getMainElementName();
                console.info("bundleNative getMainElementName success, data is " + JSON.stringify(mainElement));
                let deviceType = testNapi.getCompatibleDeviceType();
                console.info("bundleNative getCompatibleDeviceType success, deviceType is " + deviceType);
                let isDebugMode = testNapi.isDebugMode();
                console.info("bundleNative isDebugMode success, isDebugMode is " + isDebugMode);
                let moduleMetadata = testNapi.getModuleMetadata();
                console.info("bundleNative getModuleMetadata success, data is " + JSON.stringify(moduleMetadata));
                let fileType: string = '.png';
                let abilityResourceInfo = testNapi.getAbilityResourceInfo(fileType);
                console.info("bundleNative getAbilityResourceInfo success, data is " + JSON.stringify(abilityResourceInfo));
              })
          }
          .width('100%')
        }
        .height('100%')
      }
    }
    

For details about the APIs, see [Native\_Bundle](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-bundle).
