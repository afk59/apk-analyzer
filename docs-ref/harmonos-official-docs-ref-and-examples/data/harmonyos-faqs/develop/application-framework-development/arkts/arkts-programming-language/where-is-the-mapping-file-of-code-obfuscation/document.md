# Where is the mapping file of code obfuscation?

1.  **obfuscation.txt**: stores the obfuscation rules in the **consumer-rules.txt** file after packaging.
    
    Directory: **build/default/intermediates/obfuscation/default/obfuscation.txt**
    
2.  **nameCache.json**: records the mappings between source code names and their mapping names after obfuscation.
    
    Directory: **build/default/cache/default@CompileArkTS/esmodule/release/obfuscation/nameCache.json**
    
3.  .d.ets and .js files after obfuscation
    
    Directory: **build/default/intermediates/loader\_out/default/...**
    
4.  **sourceMaps.json**: associates the compiled code with the source code through the mappings between row numbers and column numbers.
    
    Directory: **build/default/cache/default@CompileArkTS/esmodule/release/sourceMaps.json**
    

**Reference**

[Obfuscation Principles and Capabilities of ArkGuard](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/source-obfuscation)
