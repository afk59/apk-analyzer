# How do I set the CPU architecture for compilation and packing?

**Symptom**

If you need to remove v7a during compilation and packaging, refer to the following configuration document.

**Solution**

You can refer to [Bundle Manager](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/bm-tool).

"externalNativeOptions": {
  "path": "./src/main/cpp/CMakeLists.txt",
  //CMake configuration file, providing CMake build scripts
  "arguments": "",
  //Optional compilation parameters passed to CMake
  "abiFilters": \[
    "x86\_64",
    "arm64-v8a"
  \],
  //Used to set up the local ABI compilation environment
  "cppFlags": ""
  //Set optional parameters for the C++ compiler
},
