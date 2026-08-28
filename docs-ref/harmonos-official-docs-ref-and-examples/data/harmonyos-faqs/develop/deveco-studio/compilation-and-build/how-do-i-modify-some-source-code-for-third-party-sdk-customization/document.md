# How do I modify some source code for third-party SDK customization?

**Question**

The SDK user needs to customize features on the SDK, while the SDK provider only wants to provide the SDK and some source code files. The SDK user modifies some source code files and replaces the modified part during compilation.

**Answer**

Since DevEco Studio 6.0.2 Beta1, the capability to replace certain files in ABC files has been provided, which supports compiling customized files and replacing files of the same name compiled in the third-party SDK.

The capability is used as follows:

**SDK Provider**:

Provides the SDK (that is, the bytecode HAR package) and the source code files of the part to be modified.

**SDK user**:

Add a new Static Library module A, which has the same **packageName** and **moduleName** as the SDK HAR package provided by the user (the **name** fields in **oh-package.json5** and **module.json5**). Delete the source code in the template A, and copy all declaration files, ABC files, and resource-related files from the third-party SDK to module A.

1.  Source code:
    1.  Copy all declaration files to the new module based on the original directory structure.
    2.  Add the source code files to be modified based on the directory structure of the third-party SDK.
2.  Resource file:
    
    Use the **resources** directory in the third-party SDK to overwrite the **resources** directory in module A.
    
3.  Configuration file:
    1.  Copy the dependency configuration (**dependencies** field in **oh-package.json5**) of the third-party SDK to the dependency configuration of module A.
    2.  If the third-party SDK contains abilities, the abilities included in the modified source code should be retained, while those not included should be removed.
4.  ABC file:
    1.  Copy the **modules.abc** file in the provider product to the current module directory.
    2.  In the module-level **build-profile.json5** file, add **customizedOptions** to **buildOption** > **packingOptions** and add the **basePackage** field to specify the location of ABC files.
        
        "buildOption": {
            "packingOptions": {
              "customizedOptions": {
                "basePackage": "./basePackage/modules.abc" //Relative path
              }
            }
          },
        
5.  After the code is modified, choose **Build** > **Make Module 'library'** to compile the module.

Restrictions:

1.  Do not set **ohos.compile.lib.entryfile** under **properties** in the **hvigor-config.json5** file to **false**.
2.  You can add and modify the source code and resources in module A, but cannot delete them.
3.  If other modules in the project reference a third-party SDK, you need to configure the [overrides](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/ide-oh-package-json5#en-us_topic_0000001792256137_overrides) in the project-level **oh-package.json5** file and use the local module to overwrite the third-party SDK. If no reference is configured, **overrides** is not required.
4.  You are not allowed to modify the configuration files (**oh-package.json5** and **module.json5**) of the third-party SDK.
5.  The C++ code cannot be modified or replaced.
6.  Only the source code of the HAR can be modified. The source code of the HAP and HSP cannot be modified or replaced.
7.  The obfuscation rules in the third-party SDK must be inherited.
    1.  Add trustlist configuration as needed. If the source file names and API names in the abc files are obfuscated, they will fail to match the original files and APIs during secondary replacement. For example, if MainPage is changed to "a", retaining MainPage during secondary modification will result in inconsistency with the one in the abc files. Therefore, you need to add **MainPage** to the obfuscation trustlist, and add the file name and external export API name to the trustlist.
    2.  After obfuscation is enabled, the automatically generated file **moduleInfo.ts** and its parent directory need to be added to the trustlist.
8.  After this feature is enabled, the **.d.ets** and **.d.ts files** in the source code directory are packed into the HAR file. Do not store important information in the .d.ets and .d.ts files.
