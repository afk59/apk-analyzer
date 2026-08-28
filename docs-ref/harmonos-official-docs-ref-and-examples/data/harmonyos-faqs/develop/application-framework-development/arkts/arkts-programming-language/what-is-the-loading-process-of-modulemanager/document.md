# What is the loading process of ModuleManager?

napi\_module is a struct that contains the information required for module registration. The definition is as follows:

static napi\_module demoModule = {
  .nm\_version = 1, // Nm version number, default value is 1, type is int
  .nm\_flags = 0, // Nm identifier, type unsigned int
  .nm\_filename = nullptr, // File name, not currently paid attention to, use default value, type is char\*
  .nm\_register\_func = Init, // Specify the entry function for nm, type napi\_addon\_register\_func
  .nm\_modname = "entry", // Specify the module name for TS page import, type char\*
  .nm\_priv = ((void\*)0),  // Not paying attention for now, just use the default, type is void\*
  .reserved = { 0 } // Not paying attention for now, just use the default value, type is void\*
};

In **requireNapi**, during module loading using **loadNativeModule**, **FindNativeModuleByCache** is called to search for the target module in the cache. If the target module is found in the cache, **GetNativeModulePath** is used to concatenate the .so file path, and then **LoadModuleLibrary** is used to open the. so file. If the file is not found in the cache, **dlopen** is used to open the .so file. With the .so file open, the **extern "C" \_\_attribute\_\_((constructor)) void RegisterModule(void)** function in the native code is called to load the native module. Subsequently, **static napi\_value Init(napi\_env env, napi\_value export)** is called to perform the registration process and return an export JS object. This object includes the native methods provided by the developers, enabling them to call these methods on the JS side. The following figure shows the module loading process.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/RShXBGlLTSqoUUiQMWV6bw/en-us_image_0000002229604001.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062542Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E58C5C6D9C092DD5F1B9E31A19331ED033DBD5D057B9A9C252D98175C30C76E4 "Click to enlarge")
