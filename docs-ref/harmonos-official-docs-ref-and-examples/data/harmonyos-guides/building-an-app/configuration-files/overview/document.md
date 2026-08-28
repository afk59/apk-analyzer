# Overview

The project application code contains build configuration files such as **hvigor-config.json5** and **build-profile.json5**, which are used to configure the build environment and customize the build process, including build tool versions and dependencies, and [multi-product builds](../../configuring-your-build/configuring-multiple-targets-and-products/document.md).

The [hvigor-config.json5](../hvigor-config-json5-file/document.md) file is stored in the **hvigor** directory of the project and contains the following information:

-   Development-specific version number of the build tool, build task, and dependency version of the script of the current project.
-   Capabilities of the build tool, including the log level and execution policy.
-   Configuration parameters of the build runtime **node** and other additional parameters transferred to the build script.

The **build-profile.json5** file is available at both the project and module levels, with **buildOption** settings configurable in both. If an item under **buildOption** is configured in both files, its setting in the module-level file is used. If an item under **buildOption** is not configured in the module-level file, its setting in the project-level file is used.

The [project-level build-profile.json5 file](../project-level-build-profile-json5-file/document.md) is stored in the project root directory and contains the following information:

-   Information about the project structure, that is, all modules that need to be built in the app project, including the module name and module path.
-   Basic configuration information required for app build, including the app name, SDK version, and signature.
-   Customized configuration information for building multi-product apps, including **product** and **buildMode**.

Each module also has a [build-profile.json5](../module-level-build-profile-json5-file/document.md) file, which contains the following information:

-   Module-level configuration information, including the API model type and target configuration for multi-product builds.
-   Customized configuration information during compilation and build, including the compilation configuration and packaging configuration of ArkTS/C++ source code and resources.
