# How do I configure and optimize the oversized package size?

**Symptom**

The package size is 16 MB, which is much larger than expected.

**Solution**

1\. Check the packing type first. The debug package contains debugging information, which is larger than the release package. You can configure **"strip": true** to remove the debugging information from the .so file to reduce its size. This [configuration](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/ide-hvigor-cpp) needs to be performed in the HAP and HSP modules in either release or debug mode.

"nativeLib": {
  "debugSymbol": {
    // This configuration can be used to execute strip on the cpp compiled product so, removing debugging information and symbol tables from so
    "strip": true,
    // Execute strip
    "exclude": \[\]
    //Execute strip filtering regular expression rules
  }
},

2\. By default, DevEco Studio does not compress the .so library file when packaging an application. After the compression option for the .so file is configured, DevEco Studio compresses the .so library file to reduce the application package size. In the **module.json5** file of the application module, set **compressNativeLibs** to **true**, and then recompile and package the application.

{
  "module": {
    // ...
    "compressNativeLibs": true // Package libs library in compressed storage format
  }
}
