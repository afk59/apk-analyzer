# Project Directory Structure

#### ArkTS Project Directory Structure (Stage Model)

ArkTS projects in the stage model support API version 10 and later versions. The project directory is shown below.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/Ge6s7gHuSDS8E1bKR6L9XA/en-us_image_0000002500910066.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062136Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7B1D1E39D2A5EDF56DE7DB172D54C8CB3AA449E7F068B94AE424D86D69BAD9C6)

-   **AppScope** > **app.json5**: global configuration of your app.
-   **entry**: app/atomic service module, which can be built into a Harmony Ability Package (HAP).
    -   **src > main > ets**: a collection of ArkTS source code.
    -   **src > main > ets > entryability**: entry to your app/atomic service.
    -   **src > main > ets > entrybackupability**: ability to [back up and restore data](../../../application-framework/core-file-kit/application-files/application-data-backup-and-restore/accessing-backup-and-restore/document.md).
    -   **src > main > ets > pages**: a collection of pages contained in your app/atomic service.
    -   **src > main > resources**: a collection of resource files used by your app/atomic service modules, such as graphics, multimedia, character strings, and layout files. For details about resource files, see [Resource Categories and Access](../../../getting-started/resource-categories-and-access/document.md).
        
        | 
        Directory
        
         | 
        
        Resource File Description
        
         |
        | :-- | :-- |
        | 
        
        base > element
        
         | 
        
        JSON file that contains resources such as character strings, integers, colors, and styles. Each resource is defined in JSON format, including:
        
        -   boolean.json
        -   color.json
        -   float.json
        -   intarray.json
        -   integer.json
        -   pattern.json
        -   plural.json
        -   strarray.json
        -   string.json
        
         |
        | 
        
        base > media
        
         | 
        
        Multimedia files, such as graphics, videos, and audios. Supported file formats include .png, .gif, .mp3, and .mp4.
        
         |
        | 
        
        rawfile
        
         | 
        
        Raw resource files in any format. **rawfile** does not look for resources based on the device status. You need to specify the directory, including the file name, for reference.
        
         |
        
    -   **src > main > module.json5**: module configuration file in the stage model, which describes the global configuration of your app/atomic service, device-specific configuration, and HAP configuration. For details, see [module.json5 Configuration File](../../../getting-started/development-fundamentals/application-configuration-files-in-stage-model/module-json5-configuration-file/document.md).
    -   **src > main > mock**: mock capability of the test framework. For details, see [Mock](../../../coding-and-debugging/conducting-self-test/test-framework/mock/document.md).
    -   **src > main > ohosTest**: instrument test classes (storage directory). For details, see [Instrument Test](../../../coding-and-debugging/conducting-self-test/test-framework/code-test/instrument-test/document.md).
    -   **src > main > test**: local test classes (storage directory). For details, see [Local Test](../../../coding-and-debugging/conducting-self-test/test-framework/code-test/local-test/document.md).
    -   **build-profile.json5**: current module information and build configuration options, including **buildOption** and **targets**.
    -   **hvigorfile.ts**: module-level build script.
    -   **obfuscation-rules.txt**: obfuscation rule file. With the obfuscation feature enabled, the code will be compiled, obfuscated, and compressed during builds in release mode to protect code assets. For details, see [Using Obfuscation for Code Hardening](../../../building-an-app/using-obfuscation-for-code-hardening/document.md).
    -   **oh-package.json5**: bundle name, version, entry file (type declaration file), and dependencies.
-   **oh\_modules**: information about third-party library dependencies, including third-party library files on which the app/atomic service depends.
-   **build-profile.json5**: app-level configuration information, including the signature and product configuration.
-   **code-linter.json5**: code check rule configurations, including the code check scope and effective rules.
-   **hvigorfile.ts**: app-level build script.
-   **oh-package.json5**: global configuration, including **overrides**, **overrideDependencyMap**, and **parameterFile**.
-   **oh-package-lock.json5**: app-level dependent version locks and cache metadata of the dependencies.

#### C++ Project Directory Structure (Stage Model)

C++ projects in the stage model support API version 10 and later and can be developed using a combination of ArkTS and C++. The project directory is shown below.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/BLPu-zfdT_OzaI107n95Og/en-us_image_0000002500910068.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062136Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B02867DBF913E62F7FDB18E9D7ACD999043270652AC3334DF2F718FDCF2FBC51)

-   **entry**: app module, which can be built into a HAP.
    -   **src > main > cpp > types**: a collection of C++ API description files.
    -   **src > main > cpp > types > libentry > index.d.ts**: file that describes the C++ API behavior, such as the API name, input parameters, and output parameters.
    -   **src > main > cpp > types > libentry > oh-package.json5**: configuration of the entry to the .so third-party package declaration file and third-party package names.
    -   **src > main > cpp > CMakeLists.txt**: CMake configuration file, which provides CMake build scripts.
    -   **src > main > cpp > napi\_init.cpp**: file that defines C++ APIs.
    -   **src > main > ets**: a collection of ArkTS source code.
    -   **src > main > resources**: a collection of resource files used by your app, such as graphics, multimedia, character strings, and layout files. For details about resource files, see [Resource Categories and Access](../../../getting-started/resource-categories-and-access/document.md).
        
        | 
        Directory
        
         | 
        
        Resource File Description
        
         |
        | :-- | :-- |
        | 
        
        base > element
        
         | 
        
        JSON file that contains resources such as character strings, integers, colors, and styles. Each resource is defined in JSON format, including:
        
        -   boolean.json
        -   color.json
        -   float.json
        -   intarray.json
        -   integer.json
        -   pattern.json
        -   plural.json
        -   strarray.json
        -   string.json
        
         |
        | 
        
        base > media
        
         | 
        
        Multimedia files, such as graphics, videos, and audios. Supported file formats include .png, .gif, .mp3, and .mp4.
        
         |
        | 
        
        rawfile
        
         | 
        
        Raw resource files in any format. **rawfile** does not look for resources based on the device status. You need to specify the directory, including the file name, for reference.
        
         |
        
    -   **src > main > module.json5**: module configuration file, which describes the global configuration of your app/atomic service, device-specific configuration, and HAP configuration. For details, see [module.json5 Configuration File](../../../getting-started/development-fundamentals/application-configuration-files-in-stage-model/module-json5-configuration-file/document.md).
    -   **build-profile.json5**: current module information and build configuration options, including **buildOption** and **targets**.
    -   **hvigorfile.ts**: module-level build script.
    -   **obfuscation-rules.txt**: obfuscation rule file. With the obfuscation feature enabled, the code will be compiled, obfuscated, and compressed during builds in release mode to protect code assets. For details, see [Using Obfuscation for Code Hardening](../../../building-an-app/using-obfuscation-for-code-hardening/document.md).
    -   **oh-package.json5**: bundle name, version, entry file (type declaration file), and dependencies.
    -   **oh-package-lock.json5**: module-level dependent version locks and cache metadata of the dependencies.
-   **oh\_modules**: information about third-party library dependencies, including third-party library files on which the app/atomic service depends.
-   **build-profile.json5**: app-level configuration information, including the signature and product configuration.
-   **code-linter.json5**: code check rule configurations, including the code check scope and effective rules.
-   **hvigorfile.ts**: app-level build script.
-   **oh-package.json5**: global configuration, including **overrides**, **overrideDependencyMap**, and **parameterFile**.
-   **oh-package-lock.json5**: app-level dependent version locks and cache metadata of the dependencies.

#### JS Project Directory Structure (FA Model)

JS projects can only be built in the FA model. The following figure shows the project directory structure.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/wyrYCtIwR7iuKEAJVdH0xQ/en-us_image_0000002500910062.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062136Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1CB646D45809E81FE9D0DC2CEE8FF78E03C223E018C675A96201F98AC51DDB75)

-   **entry**: app/atomic service module, which can be built into a HAP.
    -   **src > main > js**: a collection of JavaScript source code.
    -   **src > main > js > MainAbility**: entry to your app/atomic service.
    -   **src > main > js > MainAbility > i18n**: resources in different languages, for example, UI strings and image paths.
    -   **src > main > js > MainAbility > pages**: pages contained in **MainAbility**.
    -   **src > main > js > MainAbility > app.js**: ability lifecycle file.
    -   **src > main > resources**: a collection of resource files used by your app/atomic service, such as graphics, multimedia, character strings, and layout files. For details about resource files, see [Resource Categories and Access](../../../getting-started/resource-categories-and-access/document.md).
        
        | 
        Directory
        
         | 
        
        Resource File Description
        
         |
        | :-- | :-- |
        | 
        
        base > element
        
         | 
        
        JSON file that contains resources such as character strings, integers, colors, and styles. Each resource is defined in JSON format, including:
        
        -   boolean.json
        -   color.json
        -   float.json
        -   intarray.json
        -   integer.json
        -   pattern.json
        -   plural.json
        -   strarray.json
        -   string.json
        
         |
        | 
        
        base > media
        
         | 
        
        Multimedia files, such as graphics, videos, and audios. Supported file formats include .png, .gif, .mp3, and .mp4.
        
         |
        | 
        
        rawfile
        
         | 
        
        Raw resource files in any format. **rawfile** does not look for resources based on the device status. You need to specify the directory, including the file name, for reference.
        
         |
        
    -   **src > main > config.json**: module configuration file, which describes the global configuration of your app, device-specific configuration, and HAP configuration.
    -   **build-profile.json5**: current module information and build configuration options, including **buildOption** and **targets**.
    -   **hvigorfile.ts**: module-level build script.
    -   **oh-package.json5**: configuration of the entry to the third-party package declaration file and third-party package names.
-   **build-profile.json5**: app-level configuration information, including the signature and product configuration.
-   **hvigorfile.ts**: app-level build script.
