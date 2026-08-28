# How do I invoke ArkTS system capabilities on the native side?

**Question**

The system provides some ArkTS APIs without the corresponding NDK APIs. How do I use the ArkTS APIs when implementing service logic in C++?

**Solution**

1.  Use **napi\_load\_module** to load the module.
2.  Use **napi\_get\_named\_property** to obtain the module property.
3.  Use **napi\_call\_function** to call the related function.

The following sample code shows how to obtain the screen width and height of a device.

#include "CallSystemModule.h" 
#include "napi/native\_api.h" 
#include <hilog/log.h> 
#define LOG\_TAG "Pure" 
 
napi\_value CallSystemModule::GetDisplaySize(napi\_env env, napi\_callback\_info info) { 
    // Obtain the system library path on the arkts side
    char path\[64\] = "@ohos.display"; 
    size\_t typeLen = 0; 
    napi\_value string; 
    napi\_create\_string\_utf8(env, path, typeLen, &string); 
    // Loading system libraries 
    napi\_value sysModule; 
    napi\_load\_module(env, path, &sysModule); 
    // Retrieve the 'getDefault Display Sync' method from the system library 
    napi\_value func = nullptr; 
    napi\_get\_named\_property(env, sysModule, "getDefaultDisplaySync", &func); 
    napi\_value funcResult; 
    napi\_call\_function(env, sysModule, func, 0, nullptr, &funcResult); 
    napi\_value widthValue = nullptr; 
    napi\_get\_named\_property(env, funcResult, "width", &widthValue); 
    double width; 
    napi\_get\_value\_double(env, widthValue, &width); 
    OH\_LOG\_INFO(LOG\_APP, "width: %{public}f", width); 
    napi\_value heightValue = nullptr; 
    napi\_get\_named\_property(env, funcResult, "height", &heightValue); 
    double height; 
    napi\_get\_value\_double(env, heightValue, &height); 
    OH\_LOG\_INFO(LOG\_APP, "height: %{public}f", height); 
    // By obtaining the width and height of the business, specific business logic can be further processed
    return nullptr; 
}
