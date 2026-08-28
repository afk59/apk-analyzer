# Managing Modules

As a basic functional unit of apps/atomic services, a module contains source code, resource files, third-party libraries, and configuration files. With Hvigor, you can easily manage multiple modules in a project, through the use of the **build-profile.json5** configuration file or the **hvigorconfig.ts** script. hvigor also supports configuration, compilation, and packaging on a per-module basis.

#### Multi-Module Configuration

## Statically Configuring Modules

In the project-level **build-profile.json5** file, set the **modules** field to define modules in the project, including the module names, source code paths, and targets. For details about targets, see [Configuring Multiple Targets and Products](../configuring-multiple-targets-and-products/document.md).

In the following example, the two modules in the project directory are added to the **build-profile.json5** file to bind them to the project.

Project structure
└─ .hvigor directory    // Cache file directory of the build project, which does not need to be modified by developers and can be deleted.
└─ module1
   └─ Module source code file
   └─ build-profile.json5    // Module-level static build configuration file, which defines the build information of the current module and the build behavior of HAP (or HSP or HAR).
   └─ hvigorfile.ts    // Module-level custom dynamic build script file, which defines and extends the HAP (or HSP or HAR) build process.
   └─ Other configuration files
└─ module2
└─ hvigor directory
   └─ hvigor-config.json5    // Configuration file of the build engine, which defines the development-specific version number, dependent plug-in version, and Hvigor capability configuration.
└─ build-profile.json5    // Project-level static build configuration file, which defines the module information, app information, and app build behavior of the current project.
└─ hvigorfile.ts    // Project-level custom dynamic build script file, which defines and extends the app build process.
└─ Other configuration files

Other configuration files:

-   **oh-package.json5**: defines third-party dependencies of the app.
-   **local.properties**: defines local environment configuration of the app.
-   **obfuscation-rules.txt**: defines obfuscation rules of the module.
-   **consumer-rules.txt**: defines the default obfuscation rules of the HAR/HSP module, which will be packaged into the HAR.

The following is an example of module configuration in the **build-profile.json5** file:

{
  "modules": \[
    {
      "name": "module1", // Module name. The name must be the same as the value of module.name in the module.json5 (or config.json in the FA model) file.
      "srcPath": "./module1" // Source code path of the module. It is the relative path of the module root directory relative to the project root directory.
    },
    {
      "name": "module2",
      "srcPath": "./module2"
    }
  \]
}

## Dynamically Configuring Modules

You can dynamically add or exclude a module in the [hvigorconfig.ts](../../overview/build-system-lifecycle/document.md#section810245135914) script. For details about APIs and examples, see [HvigorConfig](../../expanding-build-capabilities/using-apis-for-extending-your-build/basic-build-capability/document.md#section7253174081515).

#### Module-specific Build

Hvigor allows you to build code on a per-module basis. To do so, use either of the following methods:

-   In DevEco Studio, select the target module directory and choose **Build** > **Make module 'module1'**, where **module1** refers to the module name.
-   In **Terminal** of DevEco Studio, specify the target module. For example, to build a HAP module named **entry**, with **target** being **default**, run the following command:
    
    hvigorw --mode module -p product=default -p module=entry@default assembleHap
    

For more commands for building a HAR or an HSP, see [Command Line Tools](../../../command-line-tools/using-hvigorw/document.md#section9580122622012).
