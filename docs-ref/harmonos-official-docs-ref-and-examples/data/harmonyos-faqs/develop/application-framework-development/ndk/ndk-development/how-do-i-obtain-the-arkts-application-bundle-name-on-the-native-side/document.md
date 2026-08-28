# How do I obtain the ArkTS application bundle name on the native side?

**Question**

How is the ArkTS application bundle name obtained in a native API called from ArkTS?

**Answer**

You can use the Native Bundle API to obtain application information, including the bundle name and application ID. The dependency **libbundle\_ndk.z.so** must be added to the **CMakeLists** file.

Sample code:

#include "CGetAppPackageName.h" 
#include "napi/native\_api.h" 
#include <bundle/native\_interface\_bundle.h> 
#include <cstdlib> 
#include "hilog/log.h" 
#define LOG\_TAG "Pure" 
 
napi\_value CGetAppPackageName::GetCurrentApplicationPackageName(napi\_env env, napi\_callback\_info info) 
{ 
    // Call the Native interface to obtain application information 
    OH\_NativeBundle\_ApplicationInfo nativeApplicationInfo = OH\_NativeBundle\_GetCurrentApplicationInfo(); 
    // Convert the application package name obtained by the Native interface to the bundleName property in the JS object 
    napi\_value bundleName; 
    napi\_create\_string\_utf8(env, nativeApplicationInfo.bundleName, NAPI\_AUTO\_LENGTH, &bundleName); 
    OH\_LOG\_INFO(LOG\_APP, "napi get application package name: %{public}s", nativeApplicationInfo.bundleName); 
    // Finally, to prevent memory leaks, manually release
    free(nativeApplicationInfo.bundleName); 
    return nullptr; 
}

For more information, see:

[Native Bundle Development](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/native-bundle-guidelines)
