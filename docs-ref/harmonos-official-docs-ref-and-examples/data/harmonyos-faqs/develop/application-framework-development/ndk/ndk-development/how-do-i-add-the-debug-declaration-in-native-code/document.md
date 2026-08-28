# How do I add the debug declaration in native code?

**Symptom**

Although **{ "name": "debug", "externalNativeOptions": { "arguments": "-DDEBUG=1" } }** is added to the **buildOptionSet** field or **\-DDEBUG=1** is set in **buildOption.externalNativeOptions.arguments** in the **build-profile.json5** file of the library to build, the statement in **#ifdef DEBUG** is not executed during the compilation of a debug build.

**Solution**

1\. Add the following statement to the **CMakeLists.txt** file:

if(CMAKE\_BUILD\_TYPE STREQUAL Debug)
    add\_definitions(-D\_DEBUG)
endif()

2\. Add the following code to the C++ file.

\# include "napi/native\_api.h" 
# include "hilog/log.h" 
# define LOG\_TAG "Pure" 
 
static napi\_value DefDebug(napi\_env env, napi\_callback\_info info) { 
#ifdef \_DEBUG 
    OH\_LOG\_INFO(LOG\_APP, "debug enter Project"); 
#else 
    OH\_LOG\_INFO(LOG\_APP, "release enter Project"); 
#endif 
    return nullptr; 
}
